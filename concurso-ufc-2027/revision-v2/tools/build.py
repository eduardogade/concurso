"""Build a _v2.docx from a revised Markdown source.

Pipeline: custom Markdown -> pandoc Markdown (diagrams as line blocks in a
"Diagram" div, references in a "Reference" div) -> pandoc docx (native OMML
math) -> OOXML post-processing (No Spacing, TNR 12, alignment by role, blank
paragraph between blocks, A4 page setup).
"""
import copy
import re
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path

from lxml import etree

W_NS = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
M_NS = 'http://schemas.openxmlformats.org/officeDocument/2006/math'
NS = {'w': W_NS, 'm': M_NS}
W = '{%s}' % W_NS
M = '{%s}' % M_NS
FONT = 'Times New Roman'
NBSP = ' '


def to_pandoc_md(src: str) -> str:
    out, lines, i = [], src.splitlines(), 0
    in_refs = False
    while i < len(lines):
        line = lines[i]
        if line.startswith('```'):
            block = []
            i += 1
            while not lines[i].startswith('```'):
                block.append(lines[i])
                i += 1
            i += 1
            while block and not block[0].strip():
                block.pop(0)
            while block and not block[-1].strip():
                block.pop()
            out.append('::: {custom-style="Diagram"}')
            for b in block:
                b = b.strip()
                # keep intentional internal spacing (e.g. fan-out diagrams)
                b = re.sub(r' {2,}', lambda m: NBSP * len(m.group(0)), b)
                out.append('| ' + b if b else '|')
            out.append(':::')
            continue
        if re.match(r'^##\s+Refer[êe]ncias\s*$', line):
            in_refs = True
            out.append(line)
            out.append('')
            out.append('::: {custom-style="Reference"}')
            i += 1
            continue
        if in_refs:
            if line.strip():
                out.append(line.strip())
                out.append('')
            i += 1
            continue
        out.append(line)
        i += 1
    if in_refs:
        out.append(':::')
    return '\n'.join(out) + '\n'


def run_pandoc(md_text: str, out_docx: Path) -> None:
    with tempfile.NamedTemporaryFile('w', suffix='.md', delete=False, encoding='utf-8') as f:
        f.write(md_text)
        tmp = f.name
    subprocess.run(
        ['pandoc', '-f', 'markdown-auto_identifiers-smart+tex_math_single_backslash',
         '-t', 'docx', '-o', str(out_docx), tmp],
        check=True)


def el(tag, **attrs):
    ns, name = tag.split(':')
    e = etree.Element('{%s}%s' % (NS[ns], name))
    for k, v in attrs.items():
        kns, kname = k.split('_', 1)
        e.set('{%s}%s' % (NS[kns], kname), v)
    return e


def rfonts():
    return el('w:rFonts', w_ascii=FONT, w_hAnsi=FONT, w_cs=FONT, w_eastAsia=FONT)


def fix_styles(xml: bytes) -> bytes:
    root = etree.fromstring(xml)
    dd = root.find('w:docDefaults', NS)
    for child in list(dd):
        dd.remove(child)
    rpd = etree.SubElement(dd, W + 'rPrDefault')
    rpr = etree.SubElement(rpd, W + 'rPr')
    rpr.append(rfonts())
    rpr.append(el('w:sz', w_val='24'))
    rpr.append(el('w:szCs', w_val='24'))
    rpr.append(el('w:lang', w_val='pt-BR', w_eastAsia='en-US', w_bidi='ar-SA'))
    ppd = etree.SubElement(dd, W + 'pPrDefault')
    ppr = etree.SubElement(ppd, W + 'pPr')
    ppr.append(el('w:spacing', w_after='0', w_line='240', w_lineRule='auto'))
    # Normal: plain TNR 12, no spacing
    normal = root.find("w:style[@w:styleId='Normal']", NS)
    for child in list(normal):
        if child.tag in (W + 'pPr', W + 'rPr'):
            normal.remove(child)
    npr = etree.SubElement(normal, W + 'pPr')
    npr.append(el('w:spacing', w_after='0', w_line='240', w_lineRule='auto'))
    nrpr = etree.SubElement(normal, W + 'rPr')
    nrpr.append(rfonts())
    nrpr.append(el('w:sz', w_val='24'))
    nrpr.append(el('w:szCs', w_val='24'))
    # No Spacing (Word built-in; shown as "Sem Espaçamento" in pt-BR Word)
    old = root.find("w:style[@w:styleId='NoSpacing']", NS)
    if old is not None:
        root.remove(old)
    ns_style = el('w:style', w_type='paragraph', w_styleId='NoSpacing')
    ns_style.append(el('w:name', w_val='No Spacing'))
    ns_style.append(el('w:basedOn', w_val='Normal'))
    ns_style.append(el('w:uiPriority', w_val='1'))
    ns_style.append(etree.Element(W + 'qFormat'))
    sp = etree.SubElement(ns_style, W + 'pPr')
    sp.append(el('w:spacing', w_after='0', w_line='240', w_lineRule='auto'))
    sr = etree.SubElement(ns_style, W + 'rPr')
    sr.append(rfonts())
    sr.append(el('w:sz', w_val='24'))
    sr.append(el('w:szCs', w_val='24'))
    normal.addnext(ns_style)
    return etree.tostring(root, xml_declaration=True, encoding='UTF-8', standalone=True)


def para_text(p):
    return ''.join(t.text or '' for t in p.iter(W + 't', M + 't'))


def role_of(p):
    ppr = p.find('w:pPr', NS)
    st = ''
    if ppr is not None and ppr.find('w:pStyle', NS) is not None:
        st = ppr.find('w:pStyle', NS).get(W + 'val')
    if st == 'Heading1':
        return 'title'
    if st == 'Heading2':
        return 'h2'
    if st in ('Heading3', 'Heading4'):
        return 'h3'
    if ppr is not None and ppr.find('w:numPr', NS) is not None:
        return 'li'
    if st == 'Diagram':
        return 'diagram'
    if st == 'Reference':
        return 'ref'
    has_para_math = p.find('m:oMathPara', NS) is not None
    plain = ''.join(t.text or '' for t in p.iter(W + 't')).strip()
    if has_para_math and not plain:
        return 'eq'
    return 'body'


JC = {'title': 'center', 'h2': 'left', 'h3': 'left', 'li': 'both', 'diagram': 'center',
      'ref': 'both', 'eq': 'center', 'body': 'both'}
OUTLINE = {'title': '0', 'h2': '1', 'h3': '2'}


def make_ppr(role, numpr=None):
    ppr = etree.Element(W + 'pPr')
    ppr.append(el('w:pStyle', w_val='NoSpacing'))
    if role in ('title', 'h2', 'h3'):
        ppr.append(etree.Element(W + 'keepNext'))
    if numpr is not None:
        ppr.append(numpr)
    if role in OUTLINE:
        # outline level keeps the Navigation Pane useful without Heading styles
        pass
    ppr.append(el('w:jc', w_val=JC[role]))
    if role in OUTLINE:
        ppr.append(el('w:outlineLvl', w_val=OUTLINE[role]))
    mark = etree.SubElement(ppr, W + 'rPr')
    mark.append(rfonts())
    if role in ('title', 'h2', 'h3'):
        mark.append(etree.Element(W + 'b'))
        mark.append(etree.Element(W + 'bCs'))
    mark.append(el('w:sz', w_val='24'))
    mark.append(el('w:szCs', w_val='24'))
    return ppr


def normalize_runs(p, bold):
    for r in p.iter(W + 'r'):
        if r.getparent() is not None and r.getparent().tag.startswith(M):
            continue
        rpr = r.find('w:rPr', NS)
        if rpr is None:
            rpr = etree.Element(W + 'rPr')
            r.insert(0, rpr)
        for tag in ('rStyle', 'rFonts', 'sz', 'szCs', 'color'):
            for x in rpr.findall('w:' + tag, NS):
                rpr.remove(x)
        rpr.insert(0, rfonts())
        if bold and rpr.find('w:b', NS) is None:
            rpr.append(etree.Element(W + 'b'))
            rpr.append(etree.Element(W + 'bCs'))
        rpr.append(el('w:sz', w_val='24'))
        rpr.append(el('w:szCs', w_val='24'))
        # OOXML schema order inside rPr: rFonts, b, bCs, i, iCs, ..., sz, szCs
        order = ['rFonts', 'b', 'bCs', 'i', 'iCs', 'sz', 'szCs']
        kids = sorted(list(rpr), key=lambda e: order.index(etree.QName(e).localname)
                      if etree.QName(e).localname in order else 99)
        for k in list(rpr):
            rpr.remove(k)
        for k in kids:
            rpr.append(k)


def blank_para():
    p = etree.Element(W + 'p')
    p.append(make_ppr('body'))
    return p


def fix_document(xml: bytes) -> bytes:
    root = etree.fromstring(xml)
    body = root.find('w:body', NS)
    paras = [p for p in body if p.tag == W + 'p']
    roles = []
    for p in paras:
        # drop pandoc bookmarks (heading anchors)
        for b in p.findall('w:bookmarkStart', NS) + p.findall('w:bookmarkEnd', NS):
            p.remove(b)
        role = role_of(p)
        old = p.find('w:pPr', NS)
        numpr = None
        if old is not None:
            n = old.find('w:numPr', NS)
            numpr = copy.deepcopy(n) if n is not None else None
            p.remove(old)
        p.insert(0, make_ppr(role, numpr))
        normalize_runs(p, bold=role in ('title', 'h2', 'h3'))
        for jc in p.iter(M + 'jc'):
            jc.set(M + 'val', 'center')
        roles.append(role)
    # one blank paragraph between blocks; none inside lists or reference lists
    for idx in range(len(paras) - 1, 0, -1):
        a, b = roles[idx - 1], roles[idx]
        if (a == b == 'li') or (a == b == 'ref'):
            continue
        paras[idx].addprevious(blank_para())
    # A4 page, 2.54 cm margins (same as the original files)
    sect = body.find('w:sectPr', NS)
    if sect is not None:
        body.remove(sect)
    sect = etree.SubElement(body, W + 'sectPr')
    sect.append(el('w:pgSz', w_w='11906', w_h='16838'))
    sect.append(el('w:pgMar', w_top='1440', w_right='1440', w_bottom='1440', w_left='1440',
                   w_header='708', w_footer='708', w_gutter='0'))
    sect.append(el('w:cols', w_space='708'))
    return etree.tostring(root, xml_declaration=True, encoding='UTF-8', standalone=True)


def fix_numbering(xml: bytes) -> bytes:
    root = etree.fromstring(xml)
    for lvl in root.iter(W + 'lvl'):
        rpr = lvl.find('w:rPr', NS)
        fmt = lvl.find('w:numFmt', NS)
        if fmt is not None and fmt.get(W + 'val') == 'bullet':
            txt = lvl.find('w:lvlText', NS)
            ilvl = int(lvl.get(W + 'ilvl'))
            # homogeneous markers: • first level, – second level
            txt.set(W + 'val', '•' if ilvl % 2 == 0 else '–')
            if rpr is None:
                rpr = etree.SubElement(lvl, W + 'rPr')
            for x in list(rpr):
                rpr.remove(x)
            rpr.append(rfonts())
    return etree.tostring(root, xml_declaration=True, encoding='UTF-8', standalone=True)


def fix_settings(xml: bytes) -> bytes:
    root = etree.fromstring(xml)
    # let Word re-run pt-BR spelling/grammar checks instead of trusting pandoc's "clean" flag
    for ps in root.findall('w:proofState', NS):
        root.remove(ps)
    return etree.tostring(root, xml_declaration=True, encoding='UTF-8', standalone=True)


def fix_core(xml: bytes, title: str) -> bytes:
    root = etree.fromstring(xml)
    t = root.find('{http://purl.org/dc/elements/1.1/}title')
    if t is not None:
        t.text = title
    return etree.tostring(root, xml_declaration=True, encoding='UTF-8', standalone=True)


def build(src: Path, dst: Path) -> None:
    raw = src.read_text(encoding='utf-8')
    title = next(l[2:].strip() for l in raw.splitlines() if l.startswith('# '))
    md = to_pandoc_md(raw)
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td) / 'raw.docx'
        run_pandoc(md, tmp)
        zin = zipfile.ZipFile(tmp)
        with zipfile.ZipFile(dst, 'w', zipfile.ZIP_DEFLATED) as zout:
            for item in zin.infolist():
                data = zin.read(item.filename)
                if item.filename == 'word/document.xml':
                    data = fix_document(data)
                elif item.filename == 'word/styles.xml':
                    data = fix_styles(data)
                elif item.filename == 'word/numbering.xml':
                    data = fix_numbering(data)
                elif item.filename == 'word/settings.xml':
                    data = fix_settings(data)
                elif item.filename == 'docProps/core.xml':
                    data = fix_core(data, title)
                zout.writestr(item, data)


if __name__ == '__main__':
    build(Path(sys.argv[1]), Path(sys.argv[2]))
