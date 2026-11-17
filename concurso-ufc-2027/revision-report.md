# Relatório de Revisão — Prova Escrita (MLOps / UFC-Quixadá)

## Fase 1 — Auditoria (antes de qualquer modificação)

### Critérios normativos usados (Prova Escrita)

- **Edital 16 / Res. 15/CEPE art. 20–21:** 3 pontos sorteados, desenvolvimento **obrigatório** de todos (o texto pode ser único ou subdividido), 4 h no total, caneta azul ou preta, sem consulta e **sem nenhum elemento que identifique o candidato**.
- **Ficha de Quixadá — Item I (7,5):** domínio técnico/científico/crítico (2,5); ideias fundamentais (2,5); organização e coerência (0,5); atualização e referências (1,0); aprofundamento (1,0).
- **Ficha de Quixadá — Item II (2,5):** terminologia (1,0); introdução, desenvolvimento e conclusão (0,5); precisão e objetividade (0,5); correção ortográfica e gramatical (0,5).
- Nenhuma exigência de formato ou de quantidade de referências consta das normas. Nada foi inventado além do que está nelas.

### Contagem e estado por ponto

A contagem considera caracteres não-brancos (texto do documento + texto das equações) **+ 1 por bullet**.

- **DOCX orig.:** contagem do `.docx` original. Em 7–10, inclui a sintaxe Markdown crua.
- **Mestre renderizado:** a seção `## Texto Final` do `.md` passada pelo mesmo pipeline usado para gerar os `_v2` (comparável ao "depois").

| # | DOCX orig. | Mestre renderizado | Excesso sobre 5.600 | Estado da formatação do DOCX |
|---|---:|---:|---:|---|
| 1 | 5.564 | 5.555 | — | TNR, No Spacing, OMML ok. Título **não centralizado**; bullets digitados com "-"; refs `[n]`, mas citações autor-ano no corpo |
| 2 | 6.527 | 6.518 | ~920 | TNR + OMML; alinhamento misto (13 parágrafos sem `jc`); 3 itens de lista numerados |
| 3 | 8.156 | 8.163 | ~2.560 | TNR + OMML; alinhamento misto |
| 4 | 6.548 | 6.570 | ~970 | TNR + OMML; 14 itens de lista |
| 5 | 6.219 | 6.244 | ~640 | TNR + OMML; listas parcialmente formatadas |
| 6 | 5.883 | 5.853 | ~250 | TNR + OMML, mas **3 equações com LaTeX cru dentro do OMML** (`\mathbb{E}\left[…`, `\varepsilon`, `\theta`) |
| 7 | 7.740 | 7.078 | ~1.480 | **Markdown cru** (`#`, `**`, `\[ \]`, ```` ``` ````, `\text`); sem OMML |
| 8 | 8.357 | 7.231 | ~1.630 | **Markdown cru**; contém o preâmbulo de chat "Meu amor — abaixo está…"; fonte Apple Color Emoji |
| 9 | 8.612 | 7.784 | ~2.180 | **Markdown cru**; contém o preâmbulo de chat |
| 10 | 9.244 | 8.343 | ~2.740 | **Markdown cru** |

### Problemas encontrados

| # | Semântica / conceitos | Fórmulas | Referências | Redundâncias / excesso | Ausências | MD × DOCX |
|---|---|---|---|---|---|---|
| 1 | Sólido | `R+W>N` correto | Lista fora da ordem de citação; citações autor-ano no corpo | — | — | Idênticos (diferenças só de formatação) |
| 2 | Sólido | Speedup, eficiência e Amdahl corretos | **Gustafson listado, mas não citado** (*weak scaling* sem atribuição); Spark citado sem Zaharia | Seção 4 repete Amdahl e stragglers; fluxograma final com 9 etapas | — | Idênticos |
| 3 | Sólido | **`y_t` não definido** em `(s_{t+1},y_t)=f(s_t,x_t)` | **Carbone e Marz vagos** ("Trabalhos sobre…") | Seções 2 e 3.3 longas; `text id="…"` (lixo de exportação) | — | Idênticos |
| 4 | Sólido | support, confidence e lift corretos, mas em blocos de texto (não equações) | Nenhuma citação no corpo | 6 signposts "≠/→"; `---` internos; legendas "Figura 1/2" (só este ponto as usa) | — | Idênticos |
| 5 | Sólido | `θ*`, `(x_i,y_i)`, `R²` em código ou texto, não em equação | Nenhuma citação no corpo | Muitos signposts curtos ("≠") | — | Idênticos |
| 6 | Sólido | `γ∈[0,1]` com soma infinita (precisão: `[0,1)` ou tarefa episódica); notação `r`/`R` misturada | Nenhuma citação no corpo | 8 "equações" só com `\text{…}` (signposts verbais) | — | DOCX com OMML quebrado |
| 7 | Sólido | `D+C+H+E+S` é signpost, não fórmula | Nenhuma citação no corpo | "métrica ≠ evidência" aparece **3 vezes**; bloco "7=/8=/9=" | — | Idênticos |
| 8 | **Preâmbulo de chat dentro do Texto Final** | `promoção ⟺ critérios` (forte demais: o correto é ⇒) | Nenhuma citação no corpo | ~25 signposts; bloco "7=/8=/9=" | — | Idênticos |
| 9 | **Preâmbulo de chat**; frase sobre o Ponto 10 fora de escopo | `P(X)`, `P(Y|X)` corretos | Nenhuma citação no corpo | "drift ≠ …" repetido; ~20 signposts | — | **DOCX sem o bloco "7=/8=/9=" e sem a frase do Ponto 10** (remoção manual não refletida no MD) |
| 10 | Sólido; taxonomia de avaliação (funcional/humano/aplicação) sem atribuição | SHAP, permutação e contrafactual corretos; `g(x)≈f(x)` repetido | Nenhuma citação no corpo | 4 distinções da conclusão repetem a seção 4 | — | Idênticos |

Nenhum ponto tem lacuna conceitual importante em relação ao programa. O problema dominante é **tamanho**: 9 de 10 pontos estão acima da faixa.

---

## Fases 2 e 3 — Resultado final

**Convenção de contagem:** caracteres não-brancos de todo o texto visível do `_v2.docx`. Isso inclui título, cabeçalhos, corpo, fórmulas (texto das equações OMML), diagramas, citações e referências, **+ 1 por bullet** (o marcador que seria escrito à mão).

| # | Arquivo `_v2.docx` | Antes: DOCX orig. / mestre | Depois | Reescrita? | Principais motivos | Correções técnicas | Refs | Validação |
|---|---|---:|---:|:-:|---|---|:-:|:-:|
| 1 | `1-pdle-armazenamento-…_v2` | 5.564 / 5.555 | **5.528** | SIM (pontual) | Citações autor-ano → `[n]`; refs reordenadas pela ordem de citação | +1 frase em 3.2: *failover* seguro exige distinguir lentidão de falha e evitar *split-brain* (consenso na eleição de líder) | 5 | 20/20 |
| 2 | `2-pdle-processamento-paralelo-…_v2` | 6.527 / 6.518 | **5.597** | SIM | Seção 4 repetia Amdahl e stragglers; MapReduce em diagrama de uma linha; fluxograma final de 9 → 7 etapas | **Gustafson** passa a ser citado (*weak scaling*) e **Zaharia** (Spark/lineage); antes, refs sem citação | 4 | 20/20 |
| 3 | `3-pdle-processamento-de-fluxos-…_v2` | 8.156 / 8.163 | **5.595** | SIM | Corte de ~2.570: 3.2–3.4 e Lambda/Kappa/lakehouse condensados; fluxograma de 8 → 6 | **`y_t` definido**; refs vagas corrigidas para os títulos reais: CARBONE *State Management in Apache Flink…* (2017) e MARZ & WARREN *Big Data: Principles and Best Practices…* (2015); lixo `id="…"` removido | 4 | 20/20 |
| 4 | `4-mineracao-de-dados-…_v2` | 6.548 / 6.570 | **5.597** | SIM | `---` internos removidos; "Figura 1/2" viraram frase (só este ponto as tinha); 3 signposts curtos incorporados ao texto | support/confidence/lift como **equações nativas**; "válidos, **novos**, úteis e interpretáveis" (alinhado à definição de Fayyad et al.) | 4 | 20/20 |
| 5 | `5-aprendizado-supervisionado-…_v2` | 6.219 / 6.244 | **5.517** | SIM | Signposts curtos incorporados; duplicação `(x_i,y_i)` / `f:X→Y` eliminada | Fórmulas em código → equações nativas; **"centróides" → "centroides"** (Acordo Ortográfico); teste "independente de todas as escolhas de modelo" | 4 | 20/20 |
| 6 | `6-aprendizado-por-reforco_v2` | 5.883 / 5.853 | **5.530** | SIM | 8 "equações" só de `\text{}` → diagramas de texto; "exploração ↔ explotação" e "model-free vs. model-based" removidos (redundantes com o texto) | **OMML quebrado do DOCX corrigido**; `γ∈[0,1]` → **`[0,1)`** (convergência da soma infinita); notação harmonizada com Sutton & Barto (`S_t, A_t, R_{t+1}`); `E[G_t\|π]` → `E_π[G_t]`; Q-learning/SARSA são off/on-policy **por definição** ("tipicamente" removido); +motivação dos métodos de política (políticas estocásticas, ações contínuas) | 4 | 20/20 |
| 7 | `7-mlops-desenvolvimento-…_v2` | 7.740 / 7.078 | **5.571** | SIM | "métrica ≠ evidência" aparecia 3× (agora 1× + 1 menção); bloco "7=/8=/9=" virou uma frase de delimitação na Introdução | — | 4 | 20/20 |
| 8 | `8-mlops-automacao-…_v2` | 8.357 / 7.231 | **5.594** | SIM | **Preâmbulo "Meu amor — …" removido**; fluxo da Introdução duplicava a Conclusão; ~20 signposts → 6; bloco 7/8/9 → frase | `promoção ⟺ critérios` → **`promoção ⇒ critérios`** (critérios são necessários, não suficientes) | 4 | 20/20 |
| 9 | `9-mlops-monitoramento-…_v2` | 8.612 / 7.784 | **5.585** | SIM | **Preâmbulo removido**; bloco 7/8/9 e frase do Ponto 10 removidos (como você já tinha feito no DOCX); ciclo da Introdução duplicava a Conclusão; listas condensadas | — | 4 | 20/20 |
| 10 | `10-xai-…_v2` | 9.244 / 8.343 | **5.595** | SIM | As 4 distinções da Conclusão repetiam o corpo; `g(x)≈f(x)` aparecia 2×; "consistência" sobrepunha "estabilidade"; critérios de contrafactual repetidos | Taxonomia de avaliação (funcional/humana/aplicação) atribuída a [1] | 4 | 20/20 |

**Regras aplicadas a todos os pontos:**

- **Citações:** toda chamada no corpo é `[n]`, numerada pela 1ª aparição. Nos pontos 3–10 não havia nenhuma citação no corpo; elas foram inseridas apenas onde a correspondência é inequívoca. **Nenhuma referência nova foi criada.** Só os títulos vagos de Carbone e Marz foram substituídos pelos títulos reais das mesmas obras.
- **Escopo do conteúdo:** nenhuma ferramenta ou tecnologia foi acrescentada. O caráter dissertativo e o esqueleto 1–5 + Referências foram preservados.
- **Fórmulas:** toda fórmula real virou equação nativa do Word (OMML, Cambria Math). Os "signposts" puramente verbais (≠, →) viraram diagramas de texto centralizados em TNR. Assim, os 10 seguem o mesmo padrão. O ponto 8 não tem nenhuma equação real.

**Fontes `_v2` em Markdown:** [revision-v2/md/](revision-v2/md/). Os `.md` mestres **não foram alterados** e agora divergem dos `_v2`. Se quiser manter o Markdown como fonte mestre, copie esses textos para a seção `## Texto Final`. Os scripts estão em [revision-v2/tools/](revision-v2/tools/) (requerem `pandoc`, `python-docx` e `lxml`).

### Validação obrigatória (por arquivo)

| Itens | Como foi verificado | Resultado (10 arquivos) |
|---|---|---|
| 1 | `python-docx` abre o arquivo; ZIP íntegro; todas as partes XML parseiam | OK |
| 3–4 | Contagem programática (faixa 5.517–5.597; todos ≤ 6.000) | OK (todos na faixa ideal 5.500–5.600) |
| 5, 11 | `docDefaults`, estilo No Spacing e todos os runs fora das equações em TNR 12; cabeçalhos em negrito | OK |
| 6–7 | 101 equações OMML; nenhum LaTeX cru; *round-trip* DOCX → LaTeX equivalente à fonte em **101/101**; parágrafos de equação com `jc=center` | OK |
| 8–10 | Título centralizado (nível 0), diagramas centralizados, corpo justificado | OK |
| 12 | Nenhum `#`, `**`, `*`, `\(`, `\)`, `\[`, `\]`, `---`, ```` ``` ```` ou comando LaTeX no texto | OK |
| 13 | Símbolos Unicode (→ ↓ ↺ ↙ ↘ ≠ ≈ ⊂ ∪ × …) presentes na fonte também presentes no DOCX | OK |
| 14–15 | Nenhum título com numeração de lista; bullets reais do Word (`numPr`); nenhum "-" ou "•" digitado | OK |
| 16–18 | Refs `[1]…[n]` sequenciais, sem bullets; toda citação tem referência; toda referência é citada; ordem = 1ª citação; nenhuma citação autor-ano restante | OK |
| 2, 19, 20 | Segunda leitura integral dos 10 textos (precisão, ortografia, legibilidade); comparação com o mestre | OK; 1 frase ajustada no ponto 3 (lakehouse) |

**Limitação da verificação visual:** o Quick Look do macOS **não desenha equações OMML**. O próprio DOCX 6 original, feito no Word, também aparece sem equações nele. Por isso, as equações foram validadas estruturalmente e por *round-trip*, não visualmente. Os `_v2` não foram abertos no Microsoft Word nesta sessão.

## Global Consistency Check

Os 10 `_v2.docx` foram comparados entre si **após a geração** (`revision-v2/tools/consistency.py`). Foram comparados:

- `docDefaults`, estilos Normal e No Spacing, página e margens;
- definição dos bullets;
- espaçamento (no máximo 1 parágrafo vazio entre blocos e nenhum no início);
- para cada papel (título, seção, subseção, corpo, lista, equação, diagrama, referência): estilo, alinhamento, fonte, tamanho e negrito.

**Resultado: nenhuma diferença.** Especificação comum:

| Elemento | Especificação |
|---|---|
| Página | A4, margens de 2,54 cm (igual aos originais) |
| Parágrafos | Estilo "Sem Espaçamento" (No Spacing); TNR 12; `pt-BR` para revisão ortográfica |
| Título | Negrito, centralizado (nível de tópico 0) |
| Seções e subseções | Negrito, à esquerda (níveis 1 e 2, visíveis no Painel de Navegação) |
| Corpo, listas e referências | Justificados |
| Equações (display) e diagramas | Centralizados |
| Bullets | • no 1º nível, – no 2º |
| Espaçamento | 1 linha em branco entre blocos; nenhuma dentro de listas ou referências |
| Conclusão | "Em síntese:" + fluxograma vertical em MAIÚSCULAS; nos pontos 7–9, também "Todo esse fluxo/ciclo é atravessado por:" |
| Referências | `[n] SOBRENOME, I. *Título*. Ano.` |

Uma diferença inicial apareceu no próprio verificador (diagramas de uma linha classificados como corpo). Corrigido o classificador, não restou diferença real nos documentos.
