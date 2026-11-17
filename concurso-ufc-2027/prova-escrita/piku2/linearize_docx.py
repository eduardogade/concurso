#!/usr/bin/env python3
"""Linearize Word DOCX files without converting native OMML mathematics to text.

Requires: Python 3.9+ and lxml (`python3 -m pip install lxml`).

Default behavior:
    * Produce NAME_linearized.docx next to each source file.
    * Ordinary adjacent paragraphs/manual line breaks: " | ".
    * One or more empty paragraphs: " || ".
    * Adjacent bullets and a complete vertical diagram: a single space at edges.
    * Consecutive bullet items: one space between items.
    * Standalone vertical down-arrow diagrams: inline right-arrow chains.
    * Set normal text to Segoe UI, 6 pt; preserve native OMML equations.

The original DOCX ZIP package, media, and relationships are preserved;
word/document.xml and the default/Normal font settings in word/styles.xml
are rewritten. Headers, footers, comments and text-box content
are not flattened. Formulae are kept as native Office Math (OMML).
"""

from __future__ import annotations

import argparse
import copy
import os
import re
import shutil
import sys
import tempfile
import zipfile
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable, Optional

from lxml import etree

ROOT = Path('/Users/egg/projects/concurso-ufc-2027/prova-escrita/piku2/pontos')
DEFAULT_FILES = [
    ROOT / '1-pdle-armazenamento-e-gerenciamento-distribuido-de-dados_v3.docx',
    ROOT / '2-pdle-processamento-paralelo-e-distribuido-em-larga-escala_v3.docx',
    ROOT / '3-pdle-processamento-de-fluxos-e-arquiteturas-de-dados_v3.docx',
    ROOT / '4-mineracao-de-dados-descoberta-de-conhecimento-aed-identificacao-de-padroes-e-anomalias_v3.docx',
    ROOT / '5-aprendizado-supervisionado-e-nao-supervisionado_v3.docx',
    ROOT / '6-aprendizado-por-reforco_v3.docx',
    ROOT / '7-mlops-desenvolvimento-versionamento-e-experimentacao-de-modelos_v3.docx',
    ROOT / '8-mlops-automacao-implantacao-e-infraestrutura-de-aprendizado-de-maquina_v3.docx',
    ROOT / '9-mlops-monitoramento-governanca-e-manutencao-de-modelos_v3.docx',
    ROOT / '10-xai-metodos-interpretabilidade-avaliacao-e-uso-das-explicacoes_v3.docx',
]

W_URI = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
M_URI = 'http://schemas.openxmlformats.org/officeDocument/2006/math'
XML_URI = 'http://www.w3.org/XML/1998/namespace'
NS = {'w': W_URI, 'm': M_URI}


def w(local: str) -> str:
    return f'{{{W_URI}}}{local}'


def m(local: str) -> str:
    return f'{{{M_URI}}}{local}'


@dataclass
class Line:
    fragments: list[etree._Element] = field(default_factory=list)
    text: str = ''
    is_bullet: bool = False
    is_diagram: bool = False
    empty: bool = False
    boundary: str = 'paragraph'
    # boundary indicates a manual break, paragraph, or a table row.


def text_of(element: etree._Element) -> str:
    """Only visible text and math text, excluding hidden annotations."""
    return ''.join(el.text or '' for el in element.iter()
                   if el.tag in {w('t'), m('t'), w('delText')})


def text_of_parts(parts: list[etree._Element]) -> str:
    return ''.join(text_of(x) for x in parts)


def literal_run(text: str) -> etree._Element:
    run = etree.Element(w('r'))
    t = etree.SubElement(run, w('t'))
    t.set(f'{{{XML_URI}}}space', 'preserve')
    t.text = text
    return run


def set_font_properties(props: etree._Element, font: str, half_points: int) -> None:
    rfonts = props.find(w('rFonts'))
    if rfonts is None:
        rfonts = etree.Element(w('rFonts'))
        props.insert(0, rfonts)
    for a in ('ascii', 'hAnsi', 'eastAsia', 'cs'):
        rfonts.set(w(a), font)

    for tag in ('sz', 'szCs'):
        node = props.find(w(tag))
        if node is None:
            node = etree.SubElement(props, w(tag))
        node.set(w('val'), str(half_points))



def set_font_run(run: etree._Element, font: str, half_points: int) -> None:
    props = run.find(w('rPr'))
    if props is None:
        props = etree.Element(w('rPr'))
        run.insert(0, props)
    set_font_properties(props, font, half_points)


def patch_default_styles(style_bytes: bytes, font: str, half_points: int) -> bytes:
    parser = etree.XMLParser(resolve_entities=False, no_network=True)
    root = etree.fromstring(style_bytes, parser=parser)
    defaults = root.find(w('docDefaults'))
    if defaults is None:
        defaults = etree.Element(w('docDefaults'))
        root.insert(0, defaults)
    rd = defaults.find(w('rPrDefault'))
    if rd is None:
        rd = etree.SubElement(defaults, w('rPrDefault'))
    props = rd.find(w('rPr'))
    if props is None:
        props = etree.SubElement(rd, w('rPr'))
    set_font_properties(props, font, half_points)

    for st in root.findall(w('style')):
        if st.get(w('styleId')) == 'Normal':
            props = st.find(w('rPr'))
            if props is None:
                props = etree.SubElement(st, w('rPr'))
            set_font_properties(props, font, half_points)
    return etree.tostring(root, encoding='UTF-8', xml_declaration=True, standalone=True)

def explicit_heading(p: etree._Element) -> bool:
    ppr = p.find(w('pPr'))
    if ppr is None:
        return False
    style = ppr.find(w('pStyle'))
    if style is None:
        return False
    val = (style.get(w('val')) or '').lower()
    return bool(re.search(r'heading|^title|^subtitle|t[íi]tulo|^t[íi]tulo', val))


def split_run_at_breaks(run: etree._Element) -> list[Optional[etree._Element]]:
    """Keep all run contents; None represents a manual line/page break."""
    rpr = run.find(w('rPr'))
    chunks: list[list[etree._Element]] = [[]]
    for item in run:
        if item.tag == w('rPr'):
            continue
        if item.tag in (w('br'), w('cr')):
            # A page break is treated as a strong boundary in the linear output.
            chunks.append([])
        elif item.tag == w('lastRenderedPageBreak'):
            continue  # a layout artifact, not an authored break
        elif item.tag == w('tab'):
            t = etree.Element(w('t'))
            t.set(f'{{{XML_URI}}}space', 'preserve')
            t.text = ' '
            chunks[-1].append(t)
        else:
            chunks[-1].append(copy.deepcopy(item))

    result: list[Optional[etree._Element]] = []
    for n, chunk in enumerate(chunks):
        if n:
            result.append(None)
        if chunk:
            cloned = etree.Element(w('r'), nsmap=run.nsmap)
            for k, v in run.attrib.items():
                cloned.set(k, v)
            if rpr is not None:
                cloned.append(copy.deepcopy(rpr))
            for item in chunk:
                cloned.append(item)
            result.append(cloned)
    return result


def normalize_nested_breaks(element: etree._Element) -> etree._Element:
    """Graceful treatment of manual breaks inside hyperlinks/content controls."""
    cloned = copy.deepcopy(element)
    for el in list(cloned.iter()):
        if el.tag in {w('br'), w('cr')}:
            parent = el.getparent()
            if parent is None:
                continue
            pos = parent.index(el)
            parent.remove(el)
            replacement = etree.Element(w('t'))
            replacement.set(f'{{{XML_URI}}}space', 'preserve')
            replacement.text = ' | '
            parent.insert(pos, replacement)
        elif el.tag == w('tab'):
            parent = el.getparent()
            if parent is None:
                continue
            pos = parent.index(el)
            parent.remove(el)
            replacement = etree.Element(w('t'))
            replacement.set(f'{{{XML_URI}}}space', 'preserve')
            replacement.text = ' '
            parent.insert(pos, replacement)
    return cloned


def list_metadata(zf: zipfile.ZipFile) -> tuple[dict, dict]:
    """Resolve automatic bullet styles, with a conservative fallback."""
    num_to_abs: dict[str, str] = {}
    numfmts: dict[tuple[str, str], str] = {}
    styles: dict[str, tuple[str, str]] = {}

    if 'word/numbering.xml' in zf.namelist():
        num_root = etree.fromstring(zf.read('word/numbering.xml'))
        for num in num_root.findall('w:num', NS):
            num_id = num.get(w('numId'))
            abs_el = num.find('w:abstractNumId', NS)
            if num_id and abs_el is not None:
                num_to_abs[num_id] = abs_el.get(w('val'), '')
        for abstract in num_root.findall('w:abstractNum', NS):
            aid = abstract.get(w('abstractNumId'), '')
            for lvl in abstract.findall('w:lvl', NS):
                fmt = lvl.find('w:numFmt', NS)
                numfmts[(aid, lvl.get(w('ilvl'), '0'))] = (
                    fmt.get(w('val'), '') if fmt is not None else '')

    if 'word/styles.xml' in zf.namelist():
        style_root = etree.fromstring(zf.read('word/styles.xml'))
        for sty in style_root.findall('w:style', NS):
            sid = sty.get(w('styleId'), '')
            numpr = sty.find('w:pPr/w:numPr', NS)
            if numpr is None:
                continue
            numid_el = numpr.find('w:numId', NS)
            ilvl_el = numpr.find('w:ilvl', NS)
            if numid_el is not None:
                styles[sid] = (
                    numid_el.get(w('val'), ''),
                    ilvl_el.get(w('val'), '0') if ilvl_el is not None else '0',
                )
    return (num_to_abs, numfmts), styles


def is_bullet_paragraph(p: etree._Element, numbering: tuple[dict, dict],
                        styles: dict) -> bool:
    visible = text_of(p).lstrip()
    if re.match(r'^[•●◦▪‣]\s*', visible):
        return True
    ppr = p.find(w('pPr'))
    if ppr is None:
        return False
    sty = ppr.find(w('pStyle'))
    sid = sty.get(w('val'), '') if sty is not None else ''
    if 'listbullet' in sid.lower() or 'list bullet' in sid.lower():
        return True
    numpr = ppr.find(w('numPr'))
    if numpr is not None:
        id_el, lvl_el = numpr.find(w('numId')), numpr.find(w('ilvl'))
        key = (id_el.get(w('val'), '') if id_el is not None else '',
               lvl_el.get(w('val'), '0') if lvl_el is not None else '0')
    else:
        key = styles.get(sid, ('', '0'))
    num_to_abs, numfmts = numbering
    return numfmts.get((num_to_abs.get(key[0], ''), key[1]), '') == 'bullet'


def paragraph_lines(p: etree._Element, numbering: tuple[dict, dict],
                    styles: dict) -> list[Line]:
    bullet = is_bullet_paragraph(p, numbering, styles)
    heading = explicit_heading(p)
    current: list[etree._Element] = []
    lines: list[Line] = []
    boundary = 'paragraph'

    def finish() -> None:
        nonlocal current, boundary
        t = text_of_parts(current)
        has_objects = bool(current)
        lines.append(Line(fragments=current, text=t, empty=not has_objects,
                          boundary=boundary, is_bullet=bullet))
        current = []
        boundary = 'manual'

    for node in p:
        if node.tag == w('pPr'):
            continue
        if node.tag == w('r'):
            for piece in split_run_at_breaks(node):
                if piece is None:
                    finish()
                else:
                    if heading:
                        props = piece.find(w('rPr'))
                        if props is None:
                            props = etree.Element(w('rPr'))
                            piece.insert(0, props)
                        if props.find(w('b')) is None:
                            etree.SubElement(props, w('b')).set(w('val'), '1')
                    current.append(piece)
        elif node.tag == m('oMathPara'):
            # Converting the *container* to inline math does not convert, rasterize,
            # or rewrite the actual <m:oMath> equations.
            for child in node:
                if child.tag == m('oMath'):
                    current.append(copy.deepcopy(child))
        elif node.tag in (w('bookmarkStart'), w('bookmarkEnd')):
            # Bookmark anchors would be ambiguous after collapsing paragraphs.
            # Retain them; bookmarks can still span text in one paragraph.
            current.append(copy.deepcopy(node))
        else:
            current.append(normalize_nested_breaks(node))
    finish()

    if bullet and lines and lines[0].text.strip() and not re.match(
            r'^\s*[•●◦▪‣]', lines[0].text):
        lines[0].fragments.insert(0, literal_run('• '))
        lines[0].text = '• ' + lines[0].text
    return lines


def table_lines(table: etree._Element, numbering: tuple[dict, dict],
                styles: dict) -> list[Line]:
    """Flatten table rows/cells; preserve inline mathematics and run formatting."""
    rows: list[Line] = []
    for row in table.findall('w:tr', NS):
        pieces: list[etree._Element] = []
        for cidx, cell in enumerate(row.findall('w:tc', NS)):
            if cidx:
                pieces.append(literal_run(' | '))
            first = True
            for item in cell:
                if item.tag == w('p'):
                    for ln in paragraph_lines(item, numbering, styles):
                        if ln.empty:
                            continue
                        if not first:
                            pieces.append(literal_run(' | '))
                        pieces.extend(ln.fragments)
                        first = False
                elif item.tag == w('tbl'):
                    for ln in table_lines(item, numbering, styles):
                        if not first:
                            pieces.append(literal_run(' || '))
                        pieces.extend(ln.fragments)
                        first = False
        if pieces:
            rows.append(Line(fragments=pieces, text=text_of_parts(pieces),
                             boundary='table_row', empty=False))
    return rows


DOWN = {'↓', '⇩', '⬇', '⬇️'}


def is_down_arrow(line: Line) -> bool:
    return line.text.strip() in DOWN and not line.is_bullet


def diagramish_label(text: str) -> bool:
    text = text.strip()
    if not text or len(text) > 120 or text.endswith(('.', ';', '?', '!')):
        return False
    letters = [x for x in text if x.isalpha()]
    if not letters:
        return False
    return sum(x.isupper() for x in letters) / len(letters) >= 0.70


def collapse_diagrams(lines: list[Line]) -> tuple[list[Line], int]:
    result: list[Line] = []
    count = 0
    i = 0
    while i < len(lines):
        if lines[i].empty or is_down_arrow(lines[i]):
            result.append(lines[i])
            i += 1
            continue
        labels = [lines[i]]
        j = i
        while (j + 2 < len(lines)
               and not lines[j + 1].empty
               and not lines[j + 2].empty
               and is_down_arrow(lines[j + 1])
               and not is_down_arrow(lines[j + 2])
               and not lines[j + 2].is_bullet):
            labels.append(lines[j + 2])
            j += 2

        n_arrows = len(labels) - 1
        valid = n_arrows >= 2 or (n_arrows == 1 and all(
            diagramish_label(label.text) for label in labels))
        valid = valid and all(len(x.text.strip()) <= 150 for x in labels)
        if valid:
            parts: list[etree._Element] = []
            for k, label in enumerate(labels):
                if k:
                    parts.append(literal_run(' → '))
                parts.extend(label.fragments)
            result.append(Line(parts, text_of_parts(parts), is_diagram=True,
                               boundary=lines[i].boundary))
            count += 1
            i = j + 1
        else:
            result.append(lines[i])
            i += 1
    return result, count


def join_lines(lines: list[Line]) -> list[etree._Element]:
    parts: list[etree._Element] = []
    prev: Optional[Line] = None
    empty_between = False
    for line in lines:
        if line.empty:
            if prev is not None:
                empty_between = True
            continue
        if prev is not None:
            if empty_between or line.boundary == 'table_row':
                sep = ' || '
            elif (line.is_bullet or prev.is_bullet
                  or line.is_diagram or prev.is_diagram):
                sep = ' '
            else:
                sep = ' | '
            parts.append(literal_run(sep))
        parts.extend(line.fragments)
        prev = line
        empty_between = False
    return parts


def make_single_paragraph(parts: list[etree._Element], font: str,
                          half_points: int) -> etree._Element:
    p = etree.Element(w('p'))
    ppr = etree.SubElement(p, w('pPr'))
    etree.SubElement(ppr, w('pStyle')).set(w('val'), 'Normal')
    spacing = etree.SubElement(ppr, w('spacing'))
    spacing.set(w('before'), '0')
    spacing.set(w('after'), '0')
    spacing.set(w('line'), '240')
    spacing.set(w('lineRule'), 'auto')
    indent = etree.SubElement(ppr, w('ind'))
    indent.set(w('left'), '0')
    indent.set(w('right'), '0')
    indent.set(w('firstLine'), '0')
    for piece in parts:
        p.append(piece)
    # w:r descendants of hyperlinks etc. are also formatted; m:r (math runs)
    # are deliberately untouched so Word/ONLYOFFICE retains math glyphs.
    for run in p.iter(w('r')):
        set_font_run(run, font, half_points)
    # The mathematical glyph font is deliberately not replaced by Segoe UI,
    # but math run size is set to the requested number of points.
    for math_run in p.iter(m('r')):
        mrpr = math_run.find(w('rPr'))
        if mrpr is None:
            mrpr = etree.Element(w('rPr'))
            m_rpr = math_run.find(m('rPr'))
            math_run.insert(1 if m_rpr is not None else 0, mrpr)
        for tag in ('sz', 'szCs'):
            node = mrpr.find(w(tag))
            if node is None:
                node = etree.SubElement(mrpr, w(tag))
            node.set(w('val'), str(half_points))
    return p


def process_document(xml_bytes: bytes, zf: zipfile.ZipFile,
                     font: str, half_points: int) -> tuple[bytes, dict]:
    parser = etree.XMLParser(resolve_entities=False, no_network=True)
    document = etree.fromstring(xml_bytes, parser=parser)
    body = document.find('w:body', NS)
    if body is None:
        raise ValueError('DOCX has no word/document.xml <w:body>')
    numbering, styles = list_metadata(zf)
    source_math = sum(1 for _ in document.iter(m('oMath')))

    # The main story is linearized; boundaries around unsupported body-level
    # objects are preserved rather than silently destroying those objects.
    new_children: list[etree._Element] = []
    pending_lines: list[Line] = []
    n_diagrams = 0
    n_bullets = 0
    unsupported: list[str] = []
    n_paras = 0
    n_tables = 0

    def flush() -> None:
        nonlocal n_diagrams, n_bullets
        if not pending_lines:
            return
        collapsed, found = collapse_diagrams(pending_lines)
        n_diagrams += found
        n_bullets += sum(x.is_bullet for x in collapsed)
        parts = join_lines(collapsed)
        if parts:
            new_children.append(make_single_paragraph(parts, font, half_points))
        pending_lines.clear()

    for child in list(body):
        if child.tag == w('p'):
            n_paras += 1
            pending_lines.extend(paragraph_lines(child, numbering, styles))
        elif child.tag == w('tbl'):
            n_tables += 1
            pending_lines.extend(table_lines(child, numbering, styles))
        elif child.tag == w('sectPr'):
            flush()
            new_children.append(copy.deepcopy(child))
        else:
            flush()
            unsupported.append(etree.QName(child).localname)
            new_children.append(copy.deepcopy(child))
    flush()
    # Ensure that sectPr (if present) stays the last body child as required.
    for child in list(body):
        body.remove(child)
    for child in new_children:
        body.append(child)

    new_math = sum(1 for _ in document.iter(m('oMath')))
    if source_math != new_math:
        raise RuntimeError(f'Math preservation failed: {source_math} -> {new_math}')
    out = etree.tostring(document, encoding='UTF-8', xml_declaration=True,
                         standalone=True)
    etree.fromstring(out, parser=parser)  # XML syntax validation
    return out, {
        'source_paragraphs': n_paras,
        'source_tables': n_tables,
        'vertical_diagrams': n_diagrams,
        'bullet_lines': n_bullets,
        'math_objects_preserved': new_math,
        'other_body_objects_left_unmodified': unsupported,
    }


def write_docx(src: Path, dst: Path, *, font: str, half_points: int) -> dict:
    with zipfile.ZipFile(src, 'r') as source:
        if 'word/document.xml' not in source.namelist():
            raise ValueError('Not a Word DOCX (word/document.xml is missing)')
        converted_xml, stats = process_document(
            source.read('word/document.xml'), source, font, half_points)
        converted_styles = (patch_default_styles(source.read('word/styles.xml'), font, half_points)
                            if 'word/styles.xml' in source.namelist() else None)
        dst.parent.mkdir(parents=True, exist_ok=True)
        fd, name = tempfile.mkstemp(prefix='.linearize_', suffix='.docx',
                                    dir=str(dst.parent))
        os.close(fd)
        tmp = Path(name)
        try:
            with zipfile.ZipFile(tmp, 'w') as result:
                for item in source.infolist():
                    if item.filename == 'word/document.xml':
                        data = converted_xml
                    elif item.filename == 'word/styles.xml' and converted_styles is not None:
                        data = converted_styles
                    else:
                        data = source.read(item.filename)
                    result.writestr(item, data)
            with zipfile.ZipFile(tmp, 'r') as check:
                bad = check.testzip()
                if bad:
                    raise RuntimeError(f'Invalid ZIP member: {bad}')
                etree.fromstring(check.read('word/document.xml'))
            os.replace(tmp, dst)
        except BaseException:
            tmp.unlink(missing_ok=True)
            raise
    return stats


def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser(
        description='Linearize DOCX text without rasterizing Office Math equations.')
    parser.add_argument('files', metavar='DOCX', type=Path, nargs='*',
                        help='Source documents; defaults to the 10 UFC DOCX paths.')
    parser.add_argument('--font', default='Segoe UI', help='Text font (default: Segoe UI).')
    parser.add_argument('--size', type=float, default=6.0,
                        help='Text size, in pt, multiples of 0.5 (default: 6).')
    parser.add_argument('--suffix', default='_linearized',
                        help='Output filename suffix (default: _linearized).')
    parser.add_argument('--output-dir', type=Path,
                        help='Optional destination directory for all outputs.')
    parser.add_argument('--in-place', action='store_true',
                        help='Replace original DOCX, writing a .docx.bak backup first.')
    args = parser.parse_args(argv)

    if args.size < 1 or args.size > 100 or abs(args.size * 2 - round(args.size * 2)) > 1e-6:
        parser.error('--size must be between 1 and 100 points, in 0.5 pt steps')
    if args.in_place and args.output_dir:
        parser.error('--in-place and --output-dir cannot be combined')
    if args.in_place and args.suffix != '_linearized':
        parser.error('--suffix is not used with --in-place')
    if not args.font.strip():
        parser.error('--font cannot be empty')

    files = args.files or DEFAULT_FILES
    failed = 0
    for src in files:
        try:
            if not src.is_file():
                raise FileNotFoundError(f'Input not found: {src}')
            if src.suffix.lower() != '.docx':
                raise ValueError('Input must be .docx')
            if args.in_place:
                backup = src.with_name(src.name + '.bak')
                shutil.copy2(src, backup)
                dst = src
            else:
                new_name = src.stem + args.suffix + '.docx'
                dst = (args.output_dir / new_name if args.output_dir
                       else src.with_name(new_name))
                if src.resolve() == dst.resolve():
                    raise ValueError('Output would overwrite source; use --in-place')
            stats = write_docx(src, dst, font=args.font,
                               half_points=int(round(args.size * 2)))
            print(f'OK  {src.name} -> {dst}')
            print(f'    {stats["source_paragraphs"]} paragraphs, '
                  f'{stats["bullet_lines"]} bullets, '
                  f'{stats["vertical_diagrams"]} down-arrow diagrams, '
                  f'{stats["math_objects_preserved"]} math objects retained')
            if stats['other_body_objects_left_unmodified']:
                print('    NOTE: other body blocks not linearized:',
                      ', '.join(stats['other_body_objects_left_unmodified']))
        except Exception as exc:
            failed += 1
            print(f'ERROR {src}: {exc}', file=sys.stderr)
    return 1 if failed else 0


if __name__ == '__main__':
    raise SystemExit(main())
