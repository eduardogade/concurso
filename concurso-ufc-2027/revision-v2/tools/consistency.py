"""Global consistency check: every _v2.docx must share the same visual spec."""
import json
import sys
import zipfile

from lxml import etree

W_NS = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
M_NS = 'http://schemas.openxmlformats.org/officeDocument/2006/math'
NS = {'w': W_NS, 'm': M_NS}
W = '{%s}' % W_NS
M = '{%s}' % M_NS


def sig(path):
    z = zipfile.ZipFile(path)
    doc = etree.fromstring(z.read('word/document.xml'))
    sty = etree.fromstring(z.read('word/styles.xml'))
    num = etree.fromstring(z.read('word/numbering.xml')) if 'word/numbering.xml' in z.namelist() else None
    body = doc.find('w:body', NS)
    paras = [p for p in body if p.tag == W + 'p']

    def c14n(e):
        return etree.tostring(e, method='c14n').decode() if e is not None else None

    roles = {}
    blank_runs, prev_blank, max_blank = 0, False, 0
    for p in paras:
        ppr = p.find('w:pPr', NS)
        text = ''.join(t.text or '' for t in p.iter(W + 't', M + 't')).strip()
        if not text and p.find('.//m:oMath', NS) is None:
            blank_runs = blank_runs + 1 if prev_blank else 1
            max_blank = max(max_blank, blank_runs)
            prev_blank = True
            continue
        prev_blank = False
        ol = ppr.find('w:outlineLvl', NS)
        if ol is not None:
            role = 'H' + ol.get(W + 'val')
        elif ppr.find('w:numPr', NS) is not None:
            role = 'LI'
        elif p.find('m:oMathPara', NS) is not None:
            role = 'EQ'
        elif p.find('w:r/w:br', NS) is not None or ppr.find('w:jc', NS).get(W + 'val') == 'center':
            role = 'DIAGRAM'
        elif text.startswith('[') and text[1:2].isdigit():
            role = 'REF'
        else:
            role = 'BODY'
        style = ppr.find('w:pStyle', NS).get(W + 'val')
        jc = ppr.find('w:jc', NS).get(W + 'val')
        fonts = set()
        sizes = set()
        bold = set()
        for r in p.iter(W + 'r'):
            rpr = r.find('w:rPr', NS)
            fonts.add(rpr.find('w:rFonts', NS).get(W + 'ascii'))
            sizes.add(rpr.find('w:sz', NS).get(W + 'val'))
            bold.add(rpr.find('w:b', NS) is not None)
        key = role
        cur = roles.setdefault(key, {'style': set(), 'jc': set(), 'fonts': set(), 'sizes': set(), 'bold': set()})
        cur['style'].add(style)
        cur['jc'].add(jc)
        cur['fonts'] |= fonts
        cur['sizes'] |= sizes
        if role.startswith('H'):
            cur['bold'] |= bold
    first_nonblank = next(i for i, p in enumerate(paras)
                          if ''.join(t.text or '' for t in p.iter(W + 't')).strip())
    roles = {k: {kk: sorted(map(str, vv)) for kk, vv in v.items()} for k, v in roles.items()}
    # single-line diagrams (no <w:br/>) are centered BODY-like paragraphs: report them apart
    bullets = sorted({(l.get(W + 'ilvl'), l.find('w:lvlText', NS).get(W + 'val'))
                      for l in num.iter(W + 'lvl') if l.find('w:numFmt', NS).get(W + 'val') == 'bullet'}) if num is not None else []
    return {
        'docDefaults': c14n(sty.find('w:docDefaults', NS)),
        'NoSpacing': c14n(sty.find("w:style[@w:styleId='NoSpacing']", NS)),
        'Normal': c14n(sty.find("w:style[@w:styleId='Normal']", NS)),
        'sectPr': c14n(body.find('w:sectPr', NS)),
        'bullets': bullets[:4],
        'max_consecutive_blank': max_blank,
        'leading_blank': first_nonblank,
        'roles': roles,
    }


if __name__ == '__main__':
    sigs = {p: sig(p) for p in sys.argv[1:]}
    base_p = sys.argv[1]
    base = sigs[base_p]
    diffs = []
    for p, s in sigs.items():
        for k in ('docDefaults', 'NoSpacing', 'Normal', 'sectPr', 'bullets', 'max_consecutive_blank', 'leading_blank'):
            if s[k] != base[k]:
                diffs.append((p, k))
        for role, spec in s['roles'].items():
            ref = next((x['roles'][role] for x in sigs.values() if role in x['roles']), None)
            for kk in ('style', 'jc', 'fonts', 'sizes', 'bold'):
                if spec[kk] != ref[kk]:
                    diffs.append((p, f'{role}.{kk}: {spec[kk]} vs {ref[kk]}'))
    union = {}
    for s in sigs.values():
        for role, spec in s['roles'].items():
            u = union.setdefault(role, {k: set() for k in spec})
            for k, v in spec.items():
                u[k] |= set(v)
    print(json.dumps({r: {k: sorted(v) for k, v in d.items()} for r, d in union.items()}, ensure_ascii=False, indent=1))
    print('bullets:', base['bullets'], 'max_consecutive_blank:', base['max_consecutive_blank'], 'leading_blank:', base['leading_blank'])
    print('DIFFS:', diffs if diffs else 'none')
