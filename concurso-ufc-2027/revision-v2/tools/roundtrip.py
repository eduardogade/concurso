import re, subprocess, sys
def norm(s):
    s = re.sub(r'\\(left|right|mathrm|text|operatorname|mathbb|,|;|quad|qquad)\b', '', s)
    s = re.sub(r'\\(left|right)', '', s)
    s = re.sub(r'[\s{}]', '', s)
    return s.replace('\\lbrack','[').replace('\\rbrack',']').replace('\\mid', '|').replace('\\neq','≠').replace('\\rightarrow','→').replace('\\Rightarrow','⇒').replace('\\leftarrow','←')
bad = 0
for n in range(1, 11):
    src = open(f'v2md/{n}.md', encoding='utf-8').read()
    s_math = [m.group(1) or m.group(2) for m in re.finditer(r'\\\((.*?)\\\)|\\\[(.*?)\\\]', src, re.S)]
    md = subprocess.run(['pandoc', '-f', 'docx', '-t', 'markdown', f'v2docx/{n}.docx'], capture_output=True, text=True).stdout
    d_math = [m.group(1) or m.group(2) for m in re.finditer(r'\$\$(.*?)\$\$|\$([^$]+?)\$', md, re.S)]
    ok = len(s_math) == len(d_math)
    mism = []
    for a, b in zip(s_math, d_math):
        if norm(a) != norm(b):
            mism.append((a.strip(), b.strip()))
    print(f'{n}: source={len(s_math)} roundtrip={len(d_math)} count_ok={ok} mismatches={len(mism)}')
    for a, b in mism:
        print('   SRC:', a[:110]); print('   RT :', b[:110])
    bad += (not ok) + len(mism)
sys.exit(1 if bad else 0)
