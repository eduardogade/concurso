#!/usr/bin/env python3
"""Gera os diagramas dos mapas de memória a partir dos arquivos Markdown.

Fonte única:  mapas/ponto-N-mapa.md
Saídas:       diagramas/src/ponto-N.dot   (Graphviz, gerado)
              diagramas/ponto-N.svg       (gerado; não editar à mão)

Uso:
    python3 render_diagramas.py           # todos os pontos
    python3 render_diagramas.py 3 7       # só os pontos 3 e 7
    python3 render_diagramas.py --png     # também grava diagramas/ponto-N.png

Requer o Graphviz (comando `dot`) no PATH.

Convenções lidas em cada bloco ```text dos mapas:
    [texto]            caixa; **termo** sai em negrito
    x_i, x_{t+1}       índice (subscrito);  x^k, V^π: expoente
    ↓   ou   ↕         liga a fileira de caixas de cima à de baixo (↕ = trade-off, ponta dupla)
    [A] ↔ [B]          duas caixas lado a lado, em contraste (ponta dupla)
    [A] → [B]          duas caixas lado a lado, em sequência
    [A]   [B]          duas caixas lado a lado, sem seta entre elas
    ├→ [A]  └→ [B]     ramos que saem da fileira imediatamente acima
Seções ## com subseções ### viram um quadro que agrupa as subseções.
"""
import html
import itertools
import re
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path

BASE = Path(__file__).resolve().parent
MAPAS = BASE / 'mapas'
SAIDA = BASE / 'diagramas'
FONTES_DOT = SAIDA / 'src'

# --- aparência (tudo neutro: fundo branco, cinzas, uma única fonte) -----------
FONTE = 'Arial'
TAM_CAIXA = 12          # pt; no navegador, 1 pt = 1,33 px
TAM_INDICE = 9          # subscritos e expoentes
TAM_SECAO = 11
TAM_TITULO = 16
LARGURA_MAX = 54        # caracteres visíveis por linha antes de quebrar a caixa em duas
COR_TEXTO = '#111111'
COR_BORDA = '#2b2b2b'
COR_SETA = '#333333'
COR_SECAO_FUNDO = '#f2f2f2'
COR_SECAO_BORDA = '#d4d4d4'
COR_GRUPO_BORDA = '#bdbdbd'

SETAS_VERTICAIS = ('↓', '↕')
SETAS_HORIZONTAIS = ('↔', '→', '')
RAMOS = ('├→', '└→')


@dataclass
class Fileira:
    """Caixas na mesma altura; `entrada` diz como a fileira se liga à anterior."""
    caixas: list
    seps: list            # conector entre caixas vizinhas: '↔', '→' ou '' (nenhum)
    entrada: str | None   # '↓', '↕', 'ramo' ou None (primeira fileira)


@dataclass
class Secao:
    numero: str
    titulo: str
    nivel: int            # 2 para ##, 3 para ###
    fileiras: list = field(default_factory=list)


# --- leitura do Markdown -------------------------------------------------------

def separar_caixas(linha):
    """Divide uma linha em caixas [..] (aceita colchetes internos, como E[R]) e conectores."""
    caixas, seps, dentro, fora, prof = [], [], '', '', 0
    for ch in linha:
        if ch == '[':
            prof += 1
            if prof == 1:
                seps.append(fora.strip())
                fora, dentro = '', ''
                continue
        elif ch == ']':
            prof -= 1
            if prof == 0:
                caixas.append(dentro.strip())
                continue
        if prof > 0:
            dentro += ch
        else:
            fora += ch
    if prof != 0 or fora.strip() or not caixas or seps[0]:
        raise ValueError(f'linha de caixas malformada: {linha!r}')
    seps = seps[1:]
    for s in seps:
        if s not in SETAS_HORIZONTAIS:
            raise ValueError(f'conector desconhecido {s!r} em: {linha!r}')
    return caixas, seps


def ler_bloco(linhas):
    """Converte as linhas de um bloco ```text em fileiras de caixas."""
    fileiras, pendente, ramo_aberto = [], None, False
    for bruta in linhas:
        s = bruta.strip()
        if not s:
            continue
        if s in SETAS_VERTICAIS:
            if not fileiras or pendente:
                raise ValueError(f'seta {s} sem caixa acima ou repetida')
            pendente, ramo_aberto = s, False
            continue
        if s.startswith(RAMOS):
            caixas, _ = separar_caixas(s[2:].strip())
            if ramo_aberto:                      # ramos consecutivos formam uma fileira
                fileiras[-1].caixas += caixas
                fileiras[-1].seps.append('')
            else:
                if not fileiras or pendente:
                    raise ValueError(f'ramo sem caixa-mãe: {s!r}')
                fileiras.append(Fileira(caixas, [''] * (len(caixas) - 1), 'ramo'))
            ramo_aberto = True
            continue
        caixas, seps = separar_caixas(s)
        if fileiras and not pendente:
            raise ValueError(f'falta seta (↓ ou ↕) antes de: {s!r}')
        fileiras.append(Fileira(caixas, seps, pendente))
        pendente, ramo_aberto = None, False
    if pendente:
        raise ValueError('bloco termina com seta solta')
    return fileiras


def ler_mapa(caminho):
    """Título do ponto e lista de seções (com as fileiras de cada bloco ```text)."""
    titulo, secoes = None, []
    linhas = caminho.read_text(encoding='utf-8').splitlines()
    i = 0
    while i < len(linhas):
        linha = linhas[i]
        m = re.match(r'^(#{2,3}) (\d+(?:\.\d+)+)\. (.+)$', linha)
        if linha.startswith('# ') and titulo is None:
            titulo = linha[2:].strip()
        elif m:
            secoes.append(Secao(m.group(2), m.group(3).strip(), len(m.group(1))))
        elif linha.strip() == '```text':
            fim = linhas.index('```', i + 1)
            secoes[-1].fileiras = ler_bloco(linhas[i + 1:fim])
            i = fim
        i += 1
    return titulo, secoes


# --- texto das caixas → rótulo HTML do Graphviz --------------------------------

def atomos(texto):
    """Quebra o texto em (tipo, conteúdo, negrito), com tipo 'txt', 'sub' ou 'sup'."""
    res, negrito, i = [], False, 0
    while i < len(texto):
        if texto.startswith('**', i):
            negrito = not negrito
            i += 2
            continue
        c = texto[i]
        if c in '_^' and i + 1 < len(texto):
            tipo = 'sub' if c == '_' else 'sup'
            if texto[i + 1] == '{':
                fim = texto.index('}', i + 2)
                conteudo, i = texto[i + 2:fim], fim + 1
            elif tipo == 'sub':
                conteudo = re.match(r'[0-9A-Za-zÀ-ÿα-ω]+', texto[i + 1:]).group(0)
                i += 1 + len(conteudo)
            else:
                conteudo, i = texto[i + 1], i + 2
            res.append((tipo, conteudo, negrito))
            continue
        if res and res[-1][0] == 'txt' and res[-1][2] == negrito:
            res[-1] = ('txt', res[-1][1] + c, negrito)
        else:
            res.append(('txt', c, negrito))
        i += 1
    if negrito:
        raise ValueError(f'** sem fechamento em: {texto!r}')
    return res


def quebrar(ats):
    """Se a caixa passa de LARGURA_MAX caracteres, quebra num espaço perto do meio,
    de preferência logo depois de '→', ':' ou ',' (a seta fica no fim da primeira linha)."""
    total = sum(len(t) for _, t, _ in ats)
    if total <= LARGURA_MAX:
        return [ats]
    melhor, pos = None, 0
    for k, (tipo, t, _) in enumerate(ats):
        for j, c in enumerate(t):
            if tipo == 'txt' and c == ' ':
                custo = abs(pos + j - total / 2) - (8 if j and t[j - 1] in '→:,' else 0)
                if melhor is None or custo < melhor[2]:
                    melhor = (k, j, custo)
        pos += len(t)
    if melhor is None:
        return [ats]
    k, j, _ = melhor
    tipo, t, b = ats[k]
    antes = ats[:k] + ([(tipo, t[:j], b)] if t[:j] else [])
    depois = ([(tipo, t[j + 1:], b)] if t[j + 1:] else []) + ats[k + 1:]
    return [antes, depois]


def html_linha(ats):
    partes = []
    for tipo, t, negrito in ats:
        t = html.escape(t, quote=False)
        if tipo != 'txt':
            tag = 'SUB' if tipo == 'sub' else 'SUP'
            t = f'<FONT POINT-SIZE="{TAM_INDICE}"><{tag}>{t}</{tag}></FONT>'
        partes.append(f'<B>{t}</B>' if negrito else t)
    return ''.join(partes)


def rotulo(texto):
    return '<' + '<BR/>'.join(html_linha(l) for l in quebrar(atomos(texto))) + '>'


def rotulo_secao(sec):
    return f'<<B>{sec.numero}</B>&#160;&#160;{html.escape(sec.titulo, quote=False)}>'


def linhas_equilibradas(texto, largura=56):
    """Quebra o texto no menor número de linhas que cabe em `largura`, com linhas de tamanho parecido."""
    palavras = texto.split()
    k = -(-len(texto) // largura)
    if k <= 1 or len(palavras) < k:
        return [texto]
    melhor = None
    for cortes in itertools.combinations(range(1, len(palavras)), k - 1):
        limites = (0,) + cortes + (len(palavras),)
        linhas = [' '.join(palavras[i:j]) for i, j in zip(limites, limites[1:])]
        if melhor is None or max(map(len, linhas)) < max(map(len, melhor)):
            melhor = linhas
    return melhor


def rotulo_titulo(titulo):
    """'Ponto N — Área: Tema' vira 'Ponto N' em destaque e o título quebrado (área longa em linha própria)."""
    ponto, _, resto = titulo.partition(' — ')
    area, dois_pontos, tema = resto.partition(': ')
    partes = [area + ':', tema] if dois_pontos and len(area) > 15 else [resto]
    linhas = [l for p in partes for l in linhas_equilibradas(p)]
    corpo = '<BR/>'.join(html.escape(l, quote=False) for l in linhas)
    return (f'<<FONT POINT-SIZE="{TAM_TITULO}"><B>{html.escape(ponto)}</B></FONT><BR/>'
            f'<FONT POINT-SIZE="{TAM_CAIXA}">{corpo}</FONT><BR/> >')


# --- montagem do .dot ------------------------------------------------------------

def ids(sec, r):
    base = 'n' + sec.numero.replace('.', '_')
    return [f'{base}_{r}_{c}' for c in range(len(sec.fileiras[r].caixas))]


def eixo(sec, r):
    """Nó do eixo vertical da fileira: a própria caixa, ou um ponto invisível entre duas caixas.

    Todos os nós do eixo estão no mesmo `group`, o que faz o Graphviz alinhá-los numa reta:
    a coluna não entorta depois de uma fileira com duas caixas.
    """
    nos = ids(sec, r)
    return nos[0] if len(nos) == 1 else f'n{sec.numero.replace(".", "_")}_{r}_m'


def cluster_folha(sec, recuo):
    """Quadro de uma seção: suas caixas, as setas internas e o alinhamento das fileiras."""
    p = recuo
    out = [f'{p}subgraph cluster_{sec.numero.replace(".", "_")} {{',
           f'{p}  label={rotulo_secao(sec)}; labeljust="l"; style="filled"; '
           f'fillcolor="{COR_SECAO_FUNDO}"; color="{COR_SECAO_BORDA}"; margin=10;']
    for r, fil in enumerate(sec.fileiras):
        nos = ids(sec, r)
        if len(nos) > 2:
            raise ValueError(f'{sec.numero}: no máximo duas caixas por fileira')
        for no, texto in zip(nos, fil.caixas):
            grupo = ' group="eixo"' if len(nos) == 1 else ''
            out.append(f'{p}  {no} [label={rotulo(texto)}{grupo}];')
        if len(nos) == 2:
            # a seta horizontal passa pelo ponto do eixo: A -> ponto -> B
            a, b, m = nos[0], nos[1], eixo(sec, r)
            esq, dir_ = {'↔': ('dir=back', ''), '→': ('arrowhead=none', ''),
                         '': ('style=invis', 'style=invis')}[fil.seps[0]]
            out += [f'{p}  {m} [shape=point width=0 height=0 style=invis group="eixo"];',
                    f'{p}  {{ rank=same; {a}; {m}; {b}; }}',
                    f'{p}  {a} -> {m} [{esq} headclip=false];',    # as duas metades se encontram
                    f'{p}  {m} -> {b} [{dir_} tailclip=false];']   # no centro do ponto, sem fresta
        if r == 0:
            continue
        acima = ids(sec, r - 1)
        if fil.entrada == 'ramo' or len(acima) == 1 or len(nos) == 1:
            pares = [(a, b) for a in acima for b in nos]
        else:
            pares = list(zip(acima, nos))
        estilo = ' [dir=both]' if fil.entrada == '↕' else ''
        out += [f'{p}  {a} -> {b}{estilo};' for a, b in pares]
        if len(acima) == 2 or len(nos) == 2:
            out.append(f'{p}  {eixo(sec, r - 1)} -> {eixo(sec, r)} [style=invis];')
    out.append(f'{p}}}')
    return out


def para_dot(titulo, secoes):
    out = ['digraph mapa {',
           f'  graph [fontname="{FONTE}" fontsize={TAM_SECAO} fontcolor="{COR_TEXTO}" bgcolor="white" '
           'rankdir=TB newrank=true nodesep=0.55 ranksep=0.24 labelloc="t" labeljust="c" '
           'margin=0.1 pad=0.2];',
           f'  node [shape=box style="filled" fillcolor="white" color="{COR_BORDA}" penwidth=1.2 '
           f'fontname="{FONTE}" fontsize={TAM_CAIXA} fontcolor="{COR_TEXTO}" margin="0.14,0.06" '
           'height=0.36];',
           f'  edge [color="{COR_SETA}" penwidth=1.3 arrowsize=0.8];',
           f'  label={rotulo_titulo(titulo)};']
    folhas = []
    i = 0
    while i < len(secoes):
        sec = secoes[i]
        filhas = []
        while i + 1 + len(filhas) < len(secoes) and secoes[i + 1 + len(filhas)].nivel > sec.nivel:
            filhas.append(secoes[i + 1 + len(filhas)])
        if filhas:                           # seção-mãe (ex.: N.3) agrupa as subseções
            out.append(f'  subgraph cluster_{sec.numero.replace(".", "_")} {{')
            out.append(f'    label={rotulo_secao(sec)}; labeljust="l"; style="dashed"; '
                       f'color="{COR_GRUPO_BORDA}"; margin=10;')
            for f in filhas:
                out += cluster_folha(f, '    ')
            out.append('  }')
            folhas += filhas
        elif sec.fileiras:
            out += cluster_folha(sec, '  ')
            folhas.append(sec)
        i += 1 + len(filhas)
    # empilha as seções numa coluna: seta invisível do eixo de uma seção ao eixo da seguinte
    for a, b in zip(folhas, folhas[1:]):
        out.append(f'  {eixo(a, len(a.fileiras) - 1)} -> {eixo(b, 0)} [style=invis];')
    out.append('}')
    return '\n'.join(out) + '\n'


# --- SVG: pós-processamento determinístico -----------------------------------------

TEXTO = re.compile(r'<text ([^>]*)>(.*?)</text>\n?')


def atributos(s):
    return dict(re.findall(r'([\w:-]+)="([^"]*)"', s))


def linha_unica(pecas, x, ancora):
    """Junta os pedaços de uma linha num só <text> com <tspan>s.

    O Graphviz posiciona cada trecho (negrito, índice...) com x absoluto calculado pela
    sua própria medida da fonte; um espaço no fim de um trecho às vezes some nessa medida.
    Com <tspan>, quem encadeia as palavras é o próprio leitor de SVG, e os espaços ficam certos.
    """
    base = pecas[0][0]
    tam = max(float(a['font-size']) for a, _ in pecas)
    out, desl = [], 0.0
    for a, conteudo in pecas:
        alvo = {'sub': tam * 0.3, 'super': -tam * 0.4}.get(a.get('baseline-shift'), 0.0)
        extra = f' dy="{alvo - desl:.2f}"' if alvo != desl else ''
        desl = alvo
        if a.get('font-weight') == 'bold':
            extra += ' font-weight="bold"'
        if float(a['font-size']) != tam:
            extra += f' font-size="{a["font-size"]}"'
        out.append(f'<tspan{extra}>{conteudo}</tspan>')
    return (f'<text xml:space="preserve" text-anchor="{ancora}" x="{x:.2f}" y="{base["y"]}" '
            f'font-family="{base["font-family"]}" font-size="{tam:.2f}" fill="{base.get("fill", "black")}">'
            + ''.join(out) + '</text>\n')


def refazer_textos(trecho, ancora, x_fixo=None):
    """Reescreve os <text> de um trecho do SVG, uma linha (mesmo y) por <text>."""
    linhas = {}
    for attrs, conteudo in TEXTO.findall(trecho):
        a = atributos(attrs)
        if conteudo.strip():
            linhas.setdefault(a['y'], []).append((a, conteudo))
    novos = ''.join(linha_unica(p, x_fixo if x_fixo is not None else float(p[0][0]['x']), ancora)
                    for p in linhas.values())
    sem_textos = TEXTO.sub('', trecho)
    return sem_textos.replace('</g>', novos + '</g>') if '</g>' in sem_textos else sem_textos + novos


def centro_x(trecho):
    xs = [float(v) for v in re.findall(r'(-?[\d.]+),-?[\d.]+', re.search(r'points="([^"]*)"', trecho).group(1))]
    return (min(xs) + max(xs)) / 2


def ajustar_svg(svg, titulo, origem):
    """Linhas de texto inteiras (caixas centradas, rótulos de seção à esquerda) e título do documento."""
    def grupo(m):
        trecho = m.group(0)
        if '<text' not in trecho:            # pontos invisíveis do eixo
            return trecho
        if m.group(1) == 'node':
            return refazer_textos(trecho, 'middle', centro_x(trecho))
        return refazer_textos(trecho, 'start')
    svg = re.sub(r'<g id="[^"]*" class="(node|cluster)">.*?</g>\n', grupo, svg, flags=re.S)
    # título do ponto: os <text> soltos entre o fundo do grafo e o primeiro quadro
    ini = svg.index('class="graph"')
    fim = svg.index('<g id=', ini)
    cabeca = svg[ini:fim]
    svg = svg[:ini] + refazer_textos(cabeca, 'middle', centro_x(cabeca)) + svg[fim:]
    svg = re.sub(r'\s*<title>.*?</title>', '', svg)
    aviso = f'<!-- Gerado por render_diagramas.py a partir de {origem}; não editar à mão -->'
    return re.sub(r'(<svg[^>]*>)', lambda m: f'{aviso}\n{m.group(1)}\n<title>{html.escape(titulo)}</title>',
                  svg, count=1)


def gerar(n, png=False):
    md = MAPAS / f'ponto-{n}-mapa.md'
    titulo, secoes = ler_mapa(md)
    dot = para_dot(titulo, secoes)
    FONTES_DOT.mkdir(parents=True, exist_ok=True)
    arq_dot = FONTES_DOT / f'ponto-{n}.dot'
    arq_dot.write_text(dot, encoding='utf-8')
    svg = subprocess.run(['dot', '-Tsvg', str(arq_dot)], check=True, capture_output=True, text=True).stdout
    (SAIDA / f'ponto-{n}.svg').write_text(ajustar_svg(svg, titulo, f'mapas/{md.name}'), encoding='utf-8')
    if png:
        subprocess.run(['dot', '-Tpng', '-Gdpi=144', str(arq_dot), '-o', str(SAIDA / f'ponto-{n}.png')],
                       check=True)
    print(f'ponto-{n}: {sum(len(f.caixas) for s in secoes for f in s.fileiras)} caixas → diagramas/ponto-{n}.svg')


if __name__ == '__main__':
    args = sys.argv[1:]
    png = '--png' in args
    pontos = [int(a) for a in args if a != '--png'] or range(1, 11)
    for n in pontos:
        gerar(n, png)
