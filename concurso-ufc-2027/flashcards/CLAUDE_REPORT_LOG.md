---

# Flashcards — Etapa 1/7
## Separação de `_all.note` por ponto

- Arquivo de origem: `flashcards/7-conceitos/_all.note` (1.580 linhas; 50.751 bytes)
- Pontos encontrados: 10 — `# Ponto 1` … `# Ponto 10`, em ordem, um heading por ponto
- Arquivos criados: `7-conceitos/ponto-1.note` … `7-conceitos/ponto-10.note` (cards por ponto: 14, 11, 13, 8, 11, 14, 10, 12, 13, 12 = 118)
- Validação: OK
- Observações:
  - Cada arquivo é cópia byte a byte do trecho que vai de `# Ponto N` até imediatamente antes do heading de nível 1 seguinte. A reconstrução prefixo + 10 arquivos + sufixo é idêntica a `_all.note`.
  - As prioridades somadas nos 10 arquivos (A 50, B 58, C 10, total 118) conferem com a seção `# Totais` do próprio `_all.note`.
  - Ficaram apenas em `_all.note`, sem ir para nenhum ponto:
    - a linha em branco inicial, antes de `# Ponto 1`;
    - as seções finais `# Totais` e `# Possíveis omissões`. São headings de nível 1, irmãos de `# Ponto N`, que resumem o arquivo inteiro e não pertencem ao bloco do Ponto 10.
  - Nenhum outro arquivo foi criado; `_all.note` não foi alterado.

---

# Flashcards — Etapa 2/7
## Criação dos flashcards de seções

- Arquivos-fonte encontrados: 10 — um `X-…_v2.md` por ponto em `prova-escrita/` (nenhum ponto com zero ou múltiplos candidatos)
- Pontos processados: 10 (Ponto 1 a Ponto 10, em ordem)
- Quantidade de subseções por ponto:
  - Ponto 1: 4
  - Ponto 2: 4
  - Ponto 3: 4
  - Ponto 4: 3
  - Ponto 5: 3
  - Ponto 6: 4
  - Ponto 7: 4
  - Ponto 8: 4
  - Ponto 9: 4
  - Ponto 10: 4
- Arquivo consolidado criado: `flashcards/1-secoes/_all.note` (10 títulos de ponto + 38 subseções `X.3.n`)
- Arquivos individuais criados: `flashcards/1-secoes/ponto-1.note` … `ponto-10.note`
- Validação: OK
- Observações:
  - Títulos e subseções copiados literalmente dos `_v2.md`. Só o nível de heading mudou (`###` → `##`). Cada ponto usa apenas `X.3.n` do próprio ponto, numerados de 1 a n sem saltos.
  - `_all.note` contém apenas headings e linhas em branco, sem nenhum texto das dissertações. A concatenação dos 10 `ponto-X.note` reproduz `_all.note` byte a byte.
  - O título do Ponto 10 foi mantido como está no arquivo-fonte (`Ponto 10 — XAI: Métodos, Interpretabilidade, Avaliação e Uso das Explicações`), sem a forma por extenso do edital.
  - Arquivos-fonte não alterados; nenhum outro arquivo criado.

---

# Flashcards — Etapa 3/7
## Extração dos diagramas de conclusão

- Arquivos-fonte encontrados: 10 — um `X-…_v2.md` por ponto em `prova-escrita/`
- Pontos processados: 10 (Ponto 1 a Ponto 10, em ordem)
- Diagramas encontrados:
  - Ponto 1: OK
  - Ponto 2: OK
  - Ponto 3: OK
  - Ponto 4: OK
  - Ponto 5: OK
  - Ponto 6: OK
  - Ponto 7: OK
  - Ponto 8: OK
  - Ponto 9: OK
  - Ponto 10: OK
- Arquivo consolidado criado: `flashcards/2-conclusao/_all.note`
- Arquivos individuais criados: `flashcards/2-conclusao/ponto-1.note` … `ponto-10.note`
- Validação: OK
- Observações:
  - Em cada arquivo-fonte há exatamente um `Em síntese:`, posicionado entre `## X.5. Conclusão` e `## Referências` e seguido imediatamente (após uma linha em branco) por um bloco ```` ```text ````.
    - Foi extraído só o conteúdo interno desse bloco, linha a linha e sem alteração.
    - Os demais blocos fenced do corpo foram ignorados.
  - Todos os diagramas são verticais: as linhas de conteúdo se alternam com linhas `↓`.
    - Etapas por ponto: 6, 7, 6, 7, 7, 5, 6, 7, 7, 6.
    - O Ponto 9 termina em `OBSERVAR NOVAMENTE ↺`, preservado como está.
  - `_all.note` não contém triple backticks. A concatenação dos 10 `ponto-X.note` reproduz `_all.note` byte a byte.
  - Arquivos-fonte não alterados; nenhum outro arquivo criado.

---

# Flashcards — Etapa 4/7
## Extração das referências bibliográficas

- Arquivos-fonte encontrados: 10 — um `X-…_v2.md` por ponto em `prova-escrita/`
- Pontos processados: 10 (Ponto 1 a Ponto 10, em ordem)
- Quantidade de referências por ponto:
  - Ponto 1: 5
  - Ponto 2: 4
  - Ponto 3: 4
  - Ponto 4: 4
  - Ponto 5: 4
  - Ponto 6: 4
  - Ponto 7: 4
  - Ponto 8: 4
  - Ponto 9: 4
  - Ponto 10: 4
- Sobrenomes convertidos para caixa alta: 28 ocorrências, 22 sobrenomes distintos, todos nos Pontos 4–10:
  - FAYYAD, TUKEY, HAN, AGGARWAL, BISHOP, MURPHY, HASTIE, GOODFELLOW, SUTTON, WATKINS, WILLIAMS;
  - MNIH, SCULLEY (3×), AMERSHI, KREUZBERGER (3×), BRECK (3×), TREVEIL, GAMA, MOLNAR, LUNDBERG, SUNDARARAJAN, RIBEIRO.
  - Nos Pontos 1–3 os sobrenomes já estavam em caixa alta e foram preservados.
- Arquivo consolidado criado: `flashcards/3-referencias/_all.note` (41 referências)
- Arquivos individuais criados: `flashcards/3-referencias/ponto-1.note` … `ponto-10.note`
- Validação: OK
- Observações:
  - Cada fonte tem exatamente uma seção `## Referências`, a última do arquivo. Todas as linhas `[n] …` foram extraídas na ordem original, com a numeração 1..n sem saltos.
  - A única mudança textual foi a caixa do sobrenome do primeiro autor (trecho entre `[n] ` e a primeira vírgula). Isso foi verificado programaticamente linha a linha: prefixo e restante da referência idênticos ao original.
  - A concatenação dos 10 `ponto-X.note` reproduz `_all.note` byte a byte.
  - Arquivos-fonte não alterados; nenhum outro arquivo criado.

---

# Flashcards — Etapa 5/7
## Extração de diagramas e bullet points

- Arquivos-fonte encontrados: 10 — um `X-…_v2.md` por ponto em `prova-escrita/`
- Pontos processados: 10 (Ponto 1 a Ponto 10, em ordem; nenhum ponto N/A)
- Diagramas extraídos por ponto:
  - Ponto 1: 0
  - Ponto 2: 1
  - Ponto 3: 1
  - Ponto 4: 5
  - Ponto 5: 5
  - Ponto 6: 4
  - Ponto 7: 8
  - Ponto 8: 9
  - Ponto 9: 7
  - Ponto 10: 4
- Blocos de bullet points extraídos por ponto:
  - Ponto 1: 2
  - Ponto 2: 2
  - Ponto 3: 1
  - Ponto 4: 3
  - Ponto 5: 3
  - Ponto 6: 3
  - Ponto 7: 1
  - Ponto 8: 3 (inclui 1 lista numerada: CI/CD/CT)
  - Ponto 9: 1
  - Ponto 10: 2 (inclui 1 lista numerada: as quatro perguntas)
- Diagramas da conclusão excluídos: 10 (o bloco que segue `Em síntese:` em cada ponto)
- Arquivo consolidado criado: `flashcards/4-diagramas/_all.note` (44 diagramas + 21 listas)
- Arquivos individuais criados: `flashcards/4-diagramas/ponto-1.note` … `ponto-10.note`
- Validação: OK
- Observações:
  - **Critério de diagrama:** todo bloco fenced ```` ```text ```` do corpo, exceto o de `Em síntese:`. Isso inclui:
    - as sinalizações sem setas (com `≠`, `=`, `⊂`, `⇒`, `+`), que a fonte já marca como diagrama;
    - os 3 blocos `Todo esse fluxo/ciclo é atravessado por:` das conclusões dos Pontos 7–9, que são distintos do bloco de `Em síntese:`.
    - Não há diagramas de setas fora de blocos fenced; setas dentro de frases do texto não foram extraídas.
  - **Conversões para horizontal:**
    - Ponto 7 (7.3.4): cadeia vertical `↓` → `EXPERIMENTO → … → MODELO CANDIDATO`.
    - Ponto 8 (8.3.4): o diagrama vertical do balanceador virou `REQUISIÇÕES → LOAD BALANCER → I1 / I2 / I3`. É a única conversão interpretativa: a linha `↙ ↓ ↘` (fan-out) foi representada por `/` entre os destinos.
    - Ponto 4 (4.2): a segunda linha do diagrama KDD (iniciada por `→`) foi unida à primeira.
    - Blocos já horizontais foram preservados. Os de várias linhas independentes (ex.: `treino → …` / `validação → …`; `DATA QUALITY → …`) foram mantidos linha a linha, sem encadear as linhas entre si.
  - **Parágrafo anterior:** foi copiado literalmente o bloco imediatamente anterior a cada elemento. Exceções:
    - 6.3.2 e 9.3.1: o bloco anterior é uma equação em bloco, copiada como está.
    - 4.2: a lista logo após o diagrama KDD recebeu o parágrafo que introduz o diagrama (`O processo KDD pode ser representado por:`), para não duplicar o diagrama.
    - 9.3.3: o diagrama `governança = …` abre a subseção e ficou sem parágrafo anterior (não foi buscado parágrafo de outra subseção).
  - **Listas:** copiadas exatamente como no Markdown, inclusive as 2 listas numeradas (`1.`, `2.`…), tratadas como equivalentes a bullets. Headings de seção/subseção só são repetidos quando mudam, como no exemplo da tarefa.
  - A concatenação dos 10 `ponto-X.note` reproduz `_all.note` byte a byte. `_all.note` não contém triple backticks nem setas `↓`.
  - Arquivos-fonte não alterados; nenhum outro arquivo criado.

---

# Flashcards — Etapa 6/7
## Extração e formatação das fórmulas

- Arquivos-fonte encontrados: 10 `X-…_v2.md` (fonte principal), com os 10 `X-…_v2.docx` correspondentes usados para conferência
- Pontos processados: 10 (Ponto 1 a Ponto 10, em ordem; nenhum ponto N/A)
- Quantidade de fórmulas por ponto (em bloco + inline relevantes):
  - Ponto 1: 1 (1 + 0)
  - Ponto 2: 3 (3 + 0)
  - Ponto 3: 2 (2 + 0)
  - Ponto 4: 4 (3 + 1)
  - Ponto 5: 5 (2 + 3)
  - Ponto 6: 18 (11 + 7)
  - Ponto 7: 1 (1 + 0)
  - Ponto 8: 3 (0 + 3)
  - Ponto 9: 6 (2 + 4)
  - Ponto 10: 7 (3 + 4)
  - Total: 50 (28 em bloco + 22 inline)
- Fonte matemática utilizada: MD (LaTeX dos `_v2.md`, originalmente extraído dos `_v2.docx`). O conteúdo matemático do MD e do DOCX é idêntico nos 10 pontos.
- Formato matemático utilizado no DOCX: equações nativas Office Math (OMML), inline e em bloco, geradas pelo pandoc 3.12. Nenhuma imagem; nenhum LaTeX cru.
- Arquivo consolidado criado: `flashcards/5-formulas/_all.docx`
- Arquivos individuais criados: `flashcards/5-formulas/ponto-1.docx` … `ponto-10.docx`
- Compatibilidade estrutural DOCX: OK
- Validação visual no ONLYOFFICE: NÃO EXECUTADA
- Validação: OK
- Observações:
  - **Teste com o motor do ONLYOFFICE (headless):** o `_all.docx` foi convertido pelo conversor do próprio ONLYOFFICE 10.0.0 (`x2t`), em cópia fora do projeto e apagada depois.
    - O documento abriu e foi diagramado sem erro; títulos, frações, somatórios, índices, expoentes e operadores aparecem.
    - As letras em itálico dentro das equações não foram desenhadas. O mesmo ocorre, na mesma conversão, com o `6-aprendizado-por-reforco_v2.docx` original. Indica falta de fonte matemática no ambiente headless, não defeito dos arquivos.
    - A aparência na interface do ONLYOFFICE não foi verificada.
  - **Critério de fórmula:**
    - todas as equações em bloco;
    - inline só com relação ou estrutura matemática: `lift > 1`, `(x_i, y_i)`, `f: X → Y`, `f(x;θ)`, `γ ∈ [0,1)`, `π(a|s)`, `V^π(s)`, `Q^π(s,a)`, `1 − ε`, `Q(s,a)`, `π_θ(a|s)`, `P(X)`, `P(Y|X)`, `Mₜ < τ ⇒ alerta`, `f(x)`, `g(x) ≈ f(x)`, `x ≈ x′ ⇒ E(x) ≈ E(x′)`, `E₁(x) ≠ E₂(x)`.
    - Símbolos isolados (N, R, W, T₁, xₜ, φ₀, θ, Q*, Mₜ, R², ŷ…) não contam como fórmula, mas aparecem renderizados nos parágrafos de contexto.
  - **Ponto 8:** as três relações estão em texto corrido na fonte (`demanda > capacidade`, `capacidade ≫ demanda`, `capacidade ≈ demanda`). Foram renderizadas como equações inline com as mesmas palavras (`\text{}`); é o único caso em que texto comum virou equação.
  - **Contexto:**
    - Cada fórmula em bloco traz o bloco imediatamente anterior e o imediatamente posterior. Em 6.3.2 e 9.3.1 o posterior é um diagrama, copiado como linhas de texto.
    - Equações consecutivas (sup/conf/lift; V^π/Q^π) ficam num único cartão.
    - Quando o parágrafo posterior de uma fórmula é o anterior da seguinte (Q* → TD), elas foram encadeadas sem repetir o parágrafo.
    - Fórmulas inline aparecem no seu parágrafo inteiro, que não é repetido quando já serve de contexto de uma equação em bloco.
  - **Divergências MD × DOCX (fora das fórmulas, registradas sem reconciliação):**
    - os DOCX 4 e 5 têm o sobrenome do primeiro autor das referências em caixa alta;
    - o DOCX 5 tem `sign ifica` (palavra partida) onde o MD tem `significa`;
    - diferenças apenas de forma: pontuação dentro da equação (Pontos 1 e 4), `\arg` (5, 6, 10) e apóstrofo tipográfico.
  - **Separação:**
    - Cópia direta dos elementos XML do `_all.docx` (equações OMML copiadas, sem reconversão).
    - Cada `ponto-X.docx` tem só o seu Heading 1; a concatenação dos 10 corpos é idêntica ao corpo do `_all.docx`; as 28 equações em bloco estão no arquivo correto, sem faltas ou extras.
    - Uma primeira tentativa de separação falhou por erro do script, depois de gravar `ponto-1.docx` e parte de `ponto-2.docx`. Ambos foram apagados e recriados; não restou nenhum outro artefato.
  - Arquivos-fonte não alterados; nenhum outro arquivo criado no projeto.

---

# Flashcards — Etapa 7/7
## Criação dos gatilhos de memória

- Arquivos-fonte encontrados: 10 — exatamente um `X-…_v2.md` por ponto em `prova-escrita/` (X = 1…10)
- Pontos processados: 10 (Ponto 1 a Ponto 10, em ordem; títulos copiados da linha `# Ponto X — …` de cada fonte)
- Seções processadas por ponto:
  - Ponto 1: 5 (1.1–1.5)
  - Ponto 2: 5 (2.1–2.5)
  - Ponto 3: 5 (3.1–3.5)
  - Ponto 4: 5 (4.1–4.5)
  - Ponto 5: 5 (5.1–5.5)
  - Ponto 6: 5 (6.1–6.5)
  - Ponto 7: 5 (7.1–7.5)
  - Ponto 8: 5 (8.1–8.5)
  - Ponto 9: 5 (9.1–9.5)
  - Ponto 10: 5 (10.1–10.5)
- Total de linhas de gatilhos: 50
- Linhas com 2 gatilhos: 2 (4.1, 9.1)
- Linhas com 3 gatilhos: 27
- Linhas com 4 gatilhos: 21
- Violações de limite de 3 palavras: 0
- Arquivo consolidado criado: `flashcards/6-gatilhos/_all.note`
- Arquivos individuais criados: `flashcards/6-gatilhos/ponto-1.note` … `ponto-10.note`
- Validação: OK
- Observações:
  - **Contagem de palavras:**
    - Não contam: os símbolos `× → + / > ≠ ⊂ ≈ = ↺`, a vírgula e as referências `[n]`.
    - Contam como uma palavra: compostos com hífen (`Variável-alvo`, `exactly-once`, `k-means`, `Actor–Critic`, `Model-specific`) e fórmulas escritas sem espaço (`R+W>N`, `D+C+H+E+S`, `(S,A,P,R,γ)`, `V^π`, `E₁`).
  - **Subseções:**
    - As subseções X.3.Y foram lidas como conteúdo de X.3 e não geraram linhas próprias. As seções "Referências" não são numeradas e não foram processadas.
    - Nas linhas X.3, os gatilhos seguem em geral a ordem das subseções. Nos Pontos 4 e 5 há 3 subseções e 4 gatilhos: em 4.3.2 e 5.3.3 entram dois.
  - **Número de gatilhos:**
    - As linhas X.3 (núcleo técnico) e X.4 (listas de trade-offs) concentram as linhas com 4 gatilhos.
    - Numa revisão, seis linhas passaram de 4 para 3 gatilhos para não forçar o máximo: 2.2, 3.2, 5.1, 7.4, 9.2 e 9.4. Os eixos retirados (eficiência, ordem por partição, fora da amostra, custo da rastreabilidade, SLIs/SLOs, excesso de alertas) ficam implícitos nos gatilhos vizinhos.
  - **Fidelidade:**
    - Cada termo dos gatilhos foi conferido automaticamente no texto da própria seção.
    - Nove termos não aparecem literalmente na seção. Sete deles são compressões do próprio texto:
      - `GFS` (1.2) = "Google File System";
      - `novidade` (3.5) = "tecnologias mais recentes";
      - `insuficiente` (7.2) = "não constitui evidência experimental suficiente";
      - `além código` (7.3) = "versionar somente o código é insuficiente";
      - `complexidade` (8.5) = "não é a mais complexa";
      - `sempre válido` (9.1) = "permanentemente válido";
      - `primeiro` (10.4) = "antes de depender de explicações post hoc".
    - Os outros dois são variações de forma: `Decomposição`, da seção que usa "decompondo" (2.1), e `argmin`, escrito `\arg\min` na fórmula (5.2).
    - `Mais` (2.5) e `Sem` (6.1) também foram sinalizados, mas são palavras funcionais.
    - Nenhum conceito externo foi introduzido.
  - **Referências** usadas só como âncoras, todas citadas na própria seção: 1.2 [1]; 1.3 [4]; 2.2 [1] [2]; 2.3 [3] [4]; 3.3 [4]; 4.1 [1]; 4.3 [2] [3] [4]; 5.2 [3]; 8.1 [1]; 8.2 [2] [3]; 10.1 [1].
  - **Fórmulas e relações compactas:** `R+W>N`, `θ* = argmin L`, `MDP (S,A,P,R,γ)`, `V^π / Q^π`, `D+C+H+E+S`, `E₁ ≠ E₂`, `Produção > consumo`, `Capacidade ≈ demanda`.
  - **Títulos:**
    - Nenhum gatilho repete o título da seção principal.
    - Única coincidência com um título de subseção: `Exploração × explotação` (6.3) é igual ao título de 6.3.3. Foi mantido por ser a relação estrutural da subseção e por constar como exemplo de bom gatilho na própria tarefa.
  - **Separação:**
    - Cada `ponto-X.note` é o trecho exato do `_all.note` entre os títulos `# Ponto X`, e a concatenação dos 10 arquivos é idêntica ao `_all.note`.
    - Mesma convenção das etapas anteriores: os pontos 1–9 terminam com a linha em branco de separação; o ponto 10, com quebra de linha simples.
  - **Diretório:** `flashcards/6-gatilhos/` já existia, vazio, antes desta tarefa; nenhum diretório foi criado.
  - **Integridade:** arquivos-fonte não alterados; nenhum outro arquivo criado. A validação rodou em memória, sem scripts persistidos.
