"""Programmatic validation of the generated _v2.docx files (checks 1-18)."""
import json
import re
import sys
import zipfile
from pathlib import Path

import docx  # python-docx: confirms the package opens as a Word document
from lxml import etree

W_NS = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
M_NS = 'http://schemas.openxmlformats.org/officeDocument/2006/math'
NS = {'w': W_NS, 'm': M_NS}
W = '{%s}' % W_NS
M = '{%s}' % M_NS
SPECIAL = set('→↓←↑↔⇒⇢↺↙↘≠≈∝⊂∪×·−–—≤≥∞∈∑πγθλφαδεσμ')


def ptext(p, math=True):
    tags = (W + 't', M + 't') if math else (W + 't',)
    return ''.join(t.text or '' for t in p.iter(*tags))


def count_nonws(path):
    root = etree.fromstring(zipfile.ZipFile(path).read('word/document.xml'))
    text = ''.join(t.text or '' for t in root.iter(W + 't', M + 't'))
    bullets = sum(1 for p in root.iter(W + 'p') if p.find('w:pPr/w:numPr', NS) is not None)
    return len(re.sub(r'\s', '', text)), bullets


def validate(path, src_md):
    res = {'file': Path(path).name}
    fails = []
    # 1. opens as DOCX
    try:
        docx.Document(path)
        z = zipfile.ZipFile(path)
        assert z.testzip() is None
        for n in z.namelist():
            if n.endswith('.xml') or n.endswith('.rels'):
                etree.fromstring(z.read(n))
        res['opens'] = True
    except Exception as e:  # noqa: BLE001
        res['opens'] = False
        fails.append(f'1 open: {e}')
        return res, fails
    root = etree.fromstring(z.read('word/document.xml'))
    styles = etree.fromstring(z.read('word/styles.xml'))
    body = root.find('w:body', NS)
    paras = [p for p in body if p.tag == W + 'p']
    nonws, bullets = count_nonws(path)
    res['nonws'] = nonws
    res['bullets'] = bullets
    res['count'] = nonws + bullets
    # 3/4. size
    if not (5200 <= res['count'] <= 5800):
        fails.append(f"3 size {res['count']} outside 5200-5800")
    if res['count'] > 6000:
        fails.append('4 size > 6000')
    # 5. fonts
    dd = styles.find('w:docDefaults/w:rPrDefault/w:rPr', NS)
    rf = dd.find('w:rFonts', NS)
    if rf is None or rf.get(W + 'ascii') != 'Times New Roman' or dd.find('w:sz', NS).get(W + 'val') != '24':
        fails.append('5 docDefaults not TNR 12')
    bad_runs = 0
    for r in body.iter(W + 'r'):
        rpr = r.find('w:rPr', NS)
        f = rpr.find('w:rFonts', NS) if rpr is not None else None
        sz = rpr.find('w:sz', NS) if rpr is not None else None
        if f is None or f.get(W + 'ascii') != 'Times New Roman' or sz is None or sz.get(W + 'val') != '24':
            bad_runs += 1
    if bad_runs:
        fails.append(f'5 runs without TNR 12: {bad_runs}')
    # 6/7. equations
    n_math = len(root.findall('.//m:oMath', NS))
    res['omml'] = n_math
    src = Path(src_md).read_text(encoding='utf-8')
    expects_math = bool(re.search(r'\\\(|\\\[', src))
    if expects_math and n_math == 0:
        fails.append('6 no OMML although source has math')
    for p in paras:
        if p.find('m:oMathPara', NS) is not None:
            jc = p.find('w:pPr/w:jc', NS)
            if jc is None or jc.get(W + 'val') != 'center':
                fails.append('7 display equation not centered')
    # roles
    def jc(p):
        j = p.find('w:pPr/w:jc', NS)
        return j.get(W + 'val') if j is not None else None
    def lvl(p):
        o = p.find('w:pPr/w:outlineLvl', NS)
        return o.get(W + 'val') if o is not None else None
    nonblank = [p for p in paras if ptext(p).strip() or p.find('.//m:oMath', NS) is not None]
    title = nonblank[0]
    if lvl(title) != '0' or jc(title) != 'center':
        fails.append('8 title not centered')
    heads = [p for p in nonblank if lvl(p) in ('0', '1', '2')]
    for h in heads:
        for r in h.iter(W + 'r'):
            if r.find('w:rPr/w:b', NS) is None:
                fails.append(f'11 heading run not bold: {ptext(h)[:40]}')
                break
        if h.find('w:pPr/w:numPr', NS) is not None:
            fails.append(f'14 heading numbered as list: {ptext(h)[:40]}')
    res['headings'] = [ptext(h) for h in heads]
    # 9. diagrams centered: paragraphs with arrows/≠ and no sentence punctuation
    for p in nonblank:
        t = ptext(p, math=False)
        if p.find('w:r/w:br', NS) is not None and jc(p) != 'center':
            fails.append(f'9 multi-line diagram not centered: {t[:40]}')
    # 10. body justified
    body_paras = [p for p in nonblank if lvl(p) is None and p.find('m:oMathPara', NS) is None
                  and p.find('w:r/w:br', NS) is None]
    unjust = [ptext(p)[:40] for p in body_paras if jc(p) not in ('both', 'center')]
    if unjust:
        fails.append(f'10 not justified: {unjust[:3]}')
    # 12. markdown / LaTeX residue in visible text
    plain = '\n'.join(ptext(p, math=False) for p in paras)
    allt = '\n'.join(ptext(p) for p in paras)
    residue = {k: len(re.findall(rx, s, re.M)) for k, rx, s in [
        ('#', r'^\s*#', plain), ('**', r'\*\*', plain), ('*', r'\*', plain),
        ('\\(', r'\\\(', allt), ('\\)', r'\\\)', allt), ('\\[', r'\\\[', allt), ('\\]', r'\\\]', allt),
        ('---', r'^\s*---\s*$', plain), ('```', r'```', plain), ('latex-cmd', r'\\[a-zA-Z]+', allt),
        ('_x_', r'(?<![\w\\])_[^_\s][^_]*_(?!\w)', plain)]}
    residue = {k: v for k, v in residue.items() if v}
    if residue:
        fails.append(f'12 residue {residue}')
    # 13. unicode preserved (symbols in source plain text must survive)
    src_plain = re.sub(r'\\\((.*?)\\\)|\\\[(.*?)\\\]', ' ', src, flags=re.S)
    missing = sorted(c for c in SPECIAL if c in src_plain and c not in allt)
    if missing:
        fails.append(f'13 unicode lost: {missing}')
    # 15. no fake bullets
    fake = [ptext(p)[:30] for p in nonblank if re.match(r'^\s*[-•*]\s', ptext(p, math=False))]
    if fake:
        fails.append(f'15 fake bullets: {fake}')
    # 16-18. references and citations
    texts = [ptext(p) for p in nonblank]
    try:
        ri = next(i for i, t in enumerate(texts) if t.strip() == 'Referências')
    except StopIteration:
        fails.append('16 no Referências heading')
        return res, fails
    refs = texts[ri + 1:]
    nums = [int(m.group(1)) for t in refs for m in [re.match(r'^\[(\d+)\]\s', t)] if m]
    res['refs'] = len(refs)
    if nums != list(range(1, len(refs) + 1)):
        fails.append(f'16 reference numbering {nums}')
    if any(p.find('w:pPr/w:numPr', NS) is not None for p in nonblank[ri + 1:]):
        fails.append('16 references are bullets')
    body_text = '\n'.join(texts[1:ri])
    cites = []
    for m in re.finditer(r'\[(\d+(?:\s*[,–-]\s*\d+)*)\]', body_text):
        for part in re.split(r'\s*,\s*', m.group(1)):
            if re.search(r'[–-]', part):
                a, b = map(int, re.split(r'\s*[–-]\s*', part))
                cites.extend(range(a, b + 1))
            else:
                cites.append(int(part))
    first = []
    for c in cites:
        if c not in first:
            first.append(c)
    res['cites_first_order'] = first
    if any(c > len(refs) or c < 1 for c in cites):
        fails.append('17 citation without reference')
    if sorted(first) != list(range(1, len(refs) + 1)):
        fails.append(f'17 uncited references: {sorted(set(range(1, len(refs) + 1)) - set(first))}')
    if first != sorted(first):
        fails.append(f'16 references not in order of first citation {first}')
    leftover = re.findall(r'\([A-ZÀ-Ú][\w\-]+(?: et al\.)?,? \d{4}\)|\b[A-Z][a-z]+ et al\. \(\d{4}\)', body_text)
    if leftover:
        fails.append(f'17 author-year citations left: {leftover}')
    return res, fails


if __name__ == '__main__':
    out = []
    for pair in sys.argv[1:]:
        d, s = pair.split('::')
        res, fails = validate(d, s)
        res['fails'] = fails
        out.append(res)
        print(json.dumps(res, ensure_ascii=False))
