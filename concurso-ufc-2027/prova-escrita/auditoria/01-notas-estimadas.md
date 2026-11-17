# Auditoria 1 — Estimativa das notas das dissertações (UFC Quixadá)

Data: 02/11/2026. Escopo: as dez dissertações finais (`prova-escrita/<N>-*_v2.md`) avaliadas pela Ficha de Avaliação da Prova Escrita Subjetiva do Campus de Quixadá, com os baremas DeepSeek como instrumento analítico de cobertura.

Arquivos complementares: [02-matriz-cobertura.md](02-matriz-cobertura.md) (evidência subitem a subitem) e [03-cenarios-tres-pontos.md](03-cenarios-tres-pontos.md) (combinações de três pontos).

## Resposta direta

Se cada dissertação for reproduzida integralmente e com fidelidade, a estimativa central fica entre **7,0** (Pontos 5 e 8) e **9,2** (Ponto 10), com média de **7,8** nos dez pontos.

- Os 3,0 pontos que o DeepSeek não cobre (organização e redação) entram como 2,85, pela hipótese dos 95%.
- Sobre os 7,0 pontos de conteúdo, as perdas vêm sobretudo de dois fatores: tópicos clássicos ausentes (ex.: transações no Ponto 1, IaC e feature store no Ponto 8) e algoritmos tratados em uma linha (Ponto 5).
- Na leitura literal do DeepSeek (banca exaustiva), cinco pontos ficam abaixo de 7,00: 1, 4, 5, 7 e 8. É o principal risco.

## A. Metodologia

### A.1 Fontes localizadas e verificações

| N | Dissertação final | Barema DeepSeek | Palavras (corpo, aprox.) |
|---|---|---|---|
| 1 | `prova-escrita/1-pdle-armazenamento-e-gerenciamento-distribuido-de-dados_v2.md` | `prova-escrita/barema-deepseek/ponto-1.note` | 802 |
| 2 | `prova-escrita/2-pdle-processamento-paralelo-e-distribuido-em-larga-escala_v2.md` | `prova-escrita/barema-deepseek/ponto-2.note` | 872 |
| 3 | `prova-escrita/3-pdle-processamento-de-fluxos-e-arquiteturas-de-dados_v2.md` | `prova-escrita/barema-deepseek/ponto-3.note` | 865 |
| 4 | `prova-escrita/4-mineracao-de-dados-descoberta-de-conhecimento-aed-identificacao-de-padroes-e-anomalias_v2.md` | `prova-escrita/barema-deepseek/ponto-4.note` | 854 |
| 5 | `prova-escrita/5-aprendizado-supervisionado-e-nao-supervisionado_v2.md` | `prova-escrita/barema-deepseek/ponto-5.note` | 862 |
| 6 | `prova-escrita/6-aprendizado-por-reforco_v2.md` | `prova-escrita/barema-deepseek/ponto-6.note` | 986 |
| 7 | `prova-escrita/7-mlops-desenvolvimento-versionamento-e-experimentacao-de-modelos_v2.md` | `prova-escrita/barema-deepseek/ponto-7.note` | 827 |
| 8 | `prova-escrita/8-mlops-automacao-implantacao-e-infraestrutura-de-aprendizado-de-maquina_v2.md` | `prova-escrita/barema-deepseek/ponto-8.note` | 810 |
| 9 | `prova-escrita/9-mlops-monitoramento-governanca-e-manutencao-de-modelos_v2.md` | `prova-escrita/barema-deepseek/ponto-9.note` | 901 |
| 10 | `prova-escrita/10-xai-metodos-interpretabilidade-avaliacao-e-uso-das-explicacoes_v2.md` | `prova-escrita/barema-deepseek/ponto-10.note` | 916 |

Verificações feitas:

- **Correspondência:** exatamente um `_v2.md` e um `ponto-N.note` por ponto, sem duplicidades.
- **Consolidado DeepSeek:** `barema-deepseek/_all.note` é a concatenação dos dez arquivos, diferindo só por linhas em branco.
- **Versões não usadas:** as preliminares (`<N>-*.md`, `.note`, `.docx` sem `_v2`) não foram usadas.
- **Títulos:** os títulos DeepSeek dos Pontos 4 e 7–10 reproduzem a redação do edital ("Operações de Aprendizado de Máquina (MLOps)…"); a correspondência pelo número é inequívoca.
- **`_v2.md` × `_v2.docx`:** a comparação palavra a palavra só acusou diferenças de forma. São espaço antes de vírgula (P1), delimitadores de fórmula (P4), `arg min` × `argmin` (P5, P6, P10), "sign ifica" no DOCX do P5 e apóstrofo (P8). O `.docx` do Ponto 6, alterado em 01/11, continua textualmente igual ao `.md`. Havia um arquivo de trava do LibreOffice sobre o `.docx` do Ponto 7, aberto durante a auditoria; edições posteriores não estão refletidas aqui.
- **Barema oficial:** `edital/barema-quixada.md` foi conferido contra `edital/barema-quixada.pdf` (pdftotext); critérios e pesos são idênticos.
- **Inconsistência no DeepSeek:** no Ponto 7, os subitens de 1.1 somam 2,25 e os de 1.4 somam 1,10, embora os subtotais declarados sejam 2,50 e 1,00. Normalizei proporcionalmente (×2,5/2,25 e ×1,0/1,1). Nos outros nove pontos as somas fecham exatamente (verificação programática).

### A.2 Barema oficial reconstruído

Fonte: `edital/barema-quixada.md`, seção "Ficha de Avaliação – Prova Escrita Subjetiva" (L5–48).

| Item | Critério (terminologia oficial) | Máximo |
|---|---|---|
| 1.1 | Domínio técnico/científico/crítico do ponto sorteado | 2,5 |
| 1.2 | Abordagem das ideias fundamentais do conteúdo | 2,5 |
| 1.3 | Organização, coerência, clareza e sequência lógica de ideias | 0,5 |
| 1.4 | Atualização do conteúdo / referências bibliográficas / normas técnicas | 1,0 |
| 1.5 | Aprofundamento do conteúdo | 1,0 |
| 2.1 | Uso adequado de terminologia técnico-científica | 1,0 |
| 2.2 | Estruturação coerente do texto com introdução, desenvolvimento e conclusão | 0,5 |
| 2.3 | Precisão e objetividade | 0,5 |
| 2.4 | Correção ortográfica e gramatical | 0,5 |
| | **Item I – Conteúdo e desenvolvimento do tema** | **7,5** |
| | **Item II – Redação** | **2,5** |
| | **Total geral (Nota da Prova Escrita)** | **10,0** |

A soma reproduz exatamente o máximo oficial: 7,5 + 2,5 = 10,0.

### A.3 Correspondência com os baremas DeepSeek

Os dez baremas DeepSeek têm a mesma estrutura: subitens rotulados com os códigos oficiais 1.1, 1.2, 1.4 e 1.5, cujos valores somam o máximo oficial de cada item (total 7,00). Não há subitem para 1.3 nem para o Item II.

| Item oficial | Máx. | Cobertura DeepSeek | Subitens por ponto | Tratamento nesta auditoria |
|---|---|---|---|---|
| 1.1 | 2,5 | Direta | 8–11 | Pontuado pelos subitens (A.5–A.6) |
| 1.2 | 2,5 | Direta | 9–12 | Pontuado pelos subitens (A.5–A.6) |
| 1.3 | 0,5 | Nenhuma | 0 | Hipótese dos 95% → 0,475 |
| 1.4 | 1,0 | Direta | 8–10 | Pontuado pelos subitens (A.5–A.6) |
| 1.5 | 1,0 | Direta | 7–10 | Pontuado pelos subitens (A.5–A.6) |
| 2.1 | 1,0 | Nenhuma | 0 | Hipótese dos 95% → 0,950 |
| 2.2 | 0,5 | Nenhuma | 0 | Hipótese dos 95% → 0,475 |
| 2.3 | 0,5 | Nenhuma | 0 | Hipótese dos 95% → 0,475 |
| 2.4 | 0,5 | Nenhuma | 0 | Hipótese dos 95% → 0,475 |

Natureza dos subitens DeepSeek por item oficial:

- **1.1 e 1.2:** listas de conceitos e técnicas, convertidas em checklist de cobertura.
- **1.4:** obras específicas e documentação de software.
- **1.5:** formalizações, trade-offs, casos-limite e exemplos aplicados.

Cada subitem é rotulado "Essencial" ou "Desejável".

**Reclassificação.** 15 subitens (somando os dez pontos) pedem "documentação atual de [ferramentas] (verificar versões)" ou benchmarks de software (YCSB, HiBench, MLPerf). Eles foram tratados como **inexigíveis para a nota máxima**: a prova é manuscrita e sem consulta (Res. 15/CEPE, art. 20 § 6º), e ninguém cita versão de documentação de memória.

- Esses subitens continuam pontuando quando atendidos, como os desejáveis.
- Apenas não entram na régua do máximo.
- Nenhum outro subitem "Essencial" foi rebaixado.

Linhas reclassificadas (em `barema-deepseek/ponto-N.note`): P1: L30, L33; P2: L32, L34; P3: L34, L35; P4: L35; P5: L38; P6: L37; P7: L34; P8: L34, L35, L36; P9: L36; P10: L36.

### A.4 Aplicação da hipótese dos 95%

Aplicada exclusivamente aos componentes oficiais sem nenhum subitem DeepSeek correspondente:

| Item | Máximo | 95% |
|---|---|---|
| 1.3 — Organização, coerência, clareza e sequência lógica de ideias | 0,5 | 0,475 |
| 2.1 — Uso adequado de terminologia técnico-científica | 1,0 | 0,950 |
| 2.2 — Estruturação coerente do texto com introdução, desenvolvimento e conclusão | 0,5 | 0,475 |
| 2.3 — Precisão e objetividade | 0,5 | 0,475 |
| 2.4 — Correção ortográfica e gramatical | 0,5 | 0,475 |
| **Total fixo** | **3,0** | **2,85** |

**Cobertura parcial.** Não identifiquei cobertura parcial a separar.

- Alguns subitens DeepSeek mencionam "precisão conceitual" na justificativa, mas pontuam o conteúdo técnico (1.1/1.2).
- O Item 2.3 avalia a precisão e a objetividade da redação.
- Para evitar dupla contagem: imprecisões técnicas penalizam só 1.1/1.2/1.5; os 95% de 1.3 e do Item II ficam fixos e não são reduzidos por julgamentos de conteúdo.

**Leitura dos textos.** Nada nos textos contradiz a hipótese:

- os dez têm introdução, desenvolvimento e conclusão explícitos;
- a progressão é numerada;
- o português é correto e a terminologia adequada.

**Riscos que o Markdown não permite avaliar:**

- legibilidade manuscrita;
- fidelidade da reprodução sob tempo;
- o efeito, na "redação", de diagramas com setas e de termos em inglês. São usuais em Computação, mas uma banca pode considerá-los telegráficos.

### A.5 Escala de graus por subitem

| Grau | Critério |
|---|---|
| 1 | Núcleo do subitem presente, correto e desenvolvido (mecanismo ou definição + implicação). Não exige enumerar todos os exemplos listados pelo DeepSeek. |
| 0,75 | Núcleo presente e correto, mas falta um elemento listado ou o desenvolvimento é curto. |
| 0,5 | Cerca de metade dos elementos, ou tratamento em uma frase com o princípio enunciado. |
| 0,25 | Menção sem desenvolvimento, ou conceito apenas tangencial ou implícito. |
| 0 | Ausente, verificado por leitura e por busca de termos e paráfrases (ver matriz). |

**Regras específicas para 1.4 (referências):**

- **1:** obra citada (ou obra equivalente do mesmo grupo/sistema, sinalizada).
- **0,25:** a contribuição específica da obra aparece no texto sem citação, ou a ferramenta pedida é nomeada no texto.
- **0:** caso contrário. Livros-texto gerais não citados recebem 0.

Quando o julgamento era ambíguo, registrei um grau alternativo (inferior ou superior), usado só na análise de sensibilidade.

### A.6 Três leituras e cálculo da nota

Para cada item oficial k ∈ {1.1, 1.2, 1.4, 1.5}, com máximo M_k:

- A_k = Σ (peso DeepSeek × grau) sobre todos os subitens do item;
- E_k = soma dos pesos dos subitens essenciais e exigíveis.

| Leitura | Fórmula por item | Interpretação |
|---|---|---|
| R1 — literal | A_k | Banca com espelho idêntico ao DeepSeek: cada omissão, inclusive de desejáveis, custa o peso integral. |
| R2 — calibrada (**central**) | M_k × min(1, A_k / E_k) | Cobrir os essenciais exigíveis basta para o máximo; desejáveis e inexigíveis atendidos compensam lacunas. |
| R3 — viável | M_k × min(1, A_k / (0,8 × E_k)) | Banca que, pelo limite de ~80 min por ponto, considera completo quem cobre 80% dos essenciais. Parâmetro de cenário, não medição. |

**Nota estimada** = S(1.1) + S(1.2) + S(1.4) + S(1.5) + 2,85, em que S(k) é a pontuação do item k na leitura considerada.

Isso é a fórmula pedida: pontuação fundamentada nos critérios avaliáveis + 0,95 × 3,0.

- **Nota central:** R2.
- **Intervalo plausível:** [R1; R3]. Varia o rigor da banca com os graus centrais. A sensibilidade aos graus alternativos (R2 com graus inferiores/superiores) cabe sempre dentro desse intervalo e aparece em cada ponto.
- **Confiança:** "média-alta" se R3 − R1 ≤ 1,25; "média" se ≤ 1,75; "média-baixa" acima disso. Rebaixa um nível quando mais de 25% dos subitens têm grau ambíguo.
- **Por que nenhuma estimativa é "alta":** todas dependem da hipótese dos 95% e da reprodução manuscrita.
- **Arredondamento:** notas finais com uma casa decimal; valores por critério com duas, como resultado de cálculo, não como medição.

### A.7 Hipóteses e limitações

1. **Reprodução.** A estimativa supõe reprodução integral e fiel de cada texto, com cerca de 800–990 palavras de corpo (ver A.1, contagem aproximada), em ~80 minutos. Reprodução parcial reduz a nota. E o edital elimina quem deixar de desenvolver "total ou parcialmente" qualquer ponto sorteado (item 16.8).
2. **Uma ficha por prova.** A ficha avalia a prova escrita como um todo: os três pontos sorteados formam uma única dissertação, com uma nota por examinador. A nota por ponto é uma aproximação; a agregação está no Relatório 3.
3. **Graus.** Os 370 graus são julgamento meu, com evidência citada; a matriz permite contestar cada um.
4. **Recorte do instrumento.** O DeepSeek pode ser mais exigente que a banca real (ver D.4). A reclassificação dos inexigíveis e a régua R2 são as únicas calibrações aplicadas.
5. **Fora do escopo.** Não considero a qualidade dos demais candidatos, a composição da banca nem probabilidades de aprovação.

## B. Tabela consolidada

| Ponto | Nota central / 10 | Intervalo plausível | Confiança | Maior deficiência |
|---|---|---|---|---|
| 1 | **7,1** | 6,3 – 8,2 | média-baixa | Transações distribuídas (ACID/2PC, NewSQL, MVCC) ausentes; arquiteturas concretas só mencionadas |
| 2 | **8,3** | 7,2 – 9,1 | média-baixa | Hadoop/YARN e operadores do Spark (RDD, joins, repartition) ausentes |
| 3 | **8,5** | 7,7 – 9,2 | média | Motores de stream e detalhes do Kafka (offsets, consumer groups) não nomeados; serving e ingestão superficiais |
| 4 | **7,4** | 6,6 – 8,3 | média | Conteúdo operacional de EDA (estatísticas, gráficos, correlação) e métodos de anomalia só mencionados; medidas de distância ausentes |
| 5 | **7,0** | 6,5 – 7,5 | média | Algoritmos tratados em uma linha cada (regressão, árvores, ensembles, SVM, k-means, DBSCAN, PCA) |
| 6 | **7,8** | 7,2 – 8,6 | média | Aprofundamento teórico (convergência, deadly triad, MC × TD, DQN, PPO) ausente |
| 7 | **7,5** | 6,7 – 8,6 | média-baixa | Camada prática (Git, DVC, MLflow, estrutura de projeto, tuning) e tipos de dívida técnica ausentes |
| 8 | **7,0** | 6,4 – 8,0 | média | Infraestrutura como código e feature store ausentes; nenhuma ferramenta nomeada |
| 9 | **8,3** | 7,7 – 9,3 | média | Testes de drift (PSI, KS) e marcos normativos (NIST AI RMF, ISO/IEC 42001, LGPD) ausentes; feedback loops ausentes |
| 10 | **9,2** | 7,5 – 9,7 | média-baixa | Valores de Shapley e axiomas, PDP/ICE e anchors ausentes; Wachter, Doshi-Velez e Rudin usados sem citação |

Detalhamento por critério (leitura central R2; os itens 1.3 e 2.x somam 2,85 em todos os pontos):

| Ponto | 1.1 (2,5) | 1.2 (2,5) | 1.4 (1,0) | 1.5 (1,0) | Conteúdo avaliável (7,0) | R1 literal | R2 central | R3 viável |
|---|---|---|---|---|---|---|---|---|
| 1 | 1,77 | 1,37 | 0,48 | 0,65 | 4,26 | 6,26 | 7,11 | 8,17 |
| 2 | 2,45 | 1,64 | 0,66 | 0,71 | 5,46 | 7,24 | 8,31 | 9,11 |
| 3 | 2,40 | 1,59 | 0,72 | 0,92 | 5,63 | 7,69 | 8,48 | 9,24 |
| 4 | 2,12 | 1,31 | 0,64 | 0,44 | 4,51 | 6,61 | 7,36 | 8,34 |
| 5 | 2,37 | 0,88 | 0,50 | 0,36 | 4,12 | 6,50 | 6,97 | 7,53 |
| 6 | 2,34 | 1,61 | 0,77 | 0,27 | 4,98 | 7,19 | 7,83 | 8,65 |
| 7 | 1,86 | 1,53 | 0,41 | 0,86 | 4,65 | 6,68 | 7,50 | 8,60 |
| 8 | 1,54 | 1,45 | 0,59 | 0,54 | 4,12 | 6,36 | 6,97 | 8,00 |
| 9 | 2,22 | 1,89 | 0,44 | 0,93 | 5,48 | 7,74 | 8,33 | 9,26 |
| 10 | 2,50 | 2,30 | 0,71 | 0,83 | 6,35 | 7,51 | 9,20 | 9,74 |

## C. Análise individual

### Ponto 1 — Processamento de Dados em Larga Escala: Armazenamento e Gerenciamento Distribuído de Dados

Dissertação: `prova-escrita/1-pdle-armazenamento-e-gerenciamento-distribuido-de-dados_v2.md` · Barema DeepSeek: `prova-escrita/barema-deepseek/ponto-1.note`

**Critérios oficiais e notas**

| Critério oficial | Máx. | Fonte | R1 literal | R2 central | R3 viável |
|---|---|---|---|---|---|
| 1.1 Domínio técnico/científico/crítico do ponto sorteado | 2,5 | DeepSeek (9 subitens) | 1,62 | 1,77 | 2,21 |
| 1.2 Abordagem das ideias fundamentais do conteúdo | 2,5 | DeepSeek (9 subitens) | 1,04 | 1,37 | 1,71 |
| 1.3 Organização, coerência, clareza e sequência lógica de ideias | 0,5 | Hipótese 95% | 0,475 | 0,475 | 0,475 |
| 1.4 Atualização do conteúdo / referências bibliográficas / normas técnicas | 1,0 | DeepSeek (8 subitens) | 0,26 | 0,48 | 0,60 |
| 1.5 Aprofundamento do conteúdo | 1,0 | DeepSeek (7 subitens) | 0,49 | 0,65 | 0,81 |
| 2.1 Uso adequado de terminologia técnico-científica | 1,0 | Hipótese 95% | 0,950 | 0,950 | 0,950 |
| 2.2 Estruturação coerente do texto com introdução, desenvolvimento e conclusão | 0,5 | Hipótese 95% | 0,475 | 0,475 | 0,475 |
| 2.3 Precisão e objetividade | 0,5 | Hipótese 95% | 0,475 | 0,475 | 0,475 |
| 2.4 Correção ortográfica e gramatical | 0,5 | Hipótese 95% | 0,475 | 0,475 | 0,475 |
| **Total** | **10,0** | | **6,26** | **7,11** | **8,17** |

**Evidências textuais relevantes**

- Definição do problema e dos dois mecanismos estruturantes (L13–22).
- Particionamento por intervalo × hash, com skew, hotspots, rebalanceamento e consistent hashing (L28–34).
- Replicação síncrona × assíncrona, líder-seguidor × sem líder, split-brain e eleição de líder por consenso (L38–44).
- Linearizabilidade × consistência eventual (L50); CAP com a crítica correta ao "escolher dois de três" (L52–54).
- Quórum R + W > N, com a ressalva de que as garantias dependem do protocolo (L56–62).
- Seção de trade-offs com critério de decisão pelo workload (L76–85).

**Critérios DeepSeek atendidos (grau 1): 5 de 33**

- 1.1 · L6 · Definição formal de sistema de armazenamento distribuído e propriedades de…
- 1.1 · L11 · Particionamento/sharding: hash, range, consistência e hotspots
- 1.2 · L21 · Estratégias de particionamento e rebalanceamento
- 1.2 · L22 · Estratégias de replicação e recuperação de falhas
- 1.4 · L27 · Bigtable (Chang et al., 2006) e Dynamo (DeCandia et al., 2007)

**Parcialmente atendidos: 17**

- 1.1 · L7 · Distinção entre armazenamento em bloco, arquivo e objeto, com critérios de… — grau 0,50
- 1.1 · L8 · Modelos de consistência: forte, eventual, causal e leituras/escritas… — grau 0,75
- 1.1 · L9 · Teorema CAP e PACELC: interpretação correta e crítica a leituras simplistas — grau 0,75
- 1.1 · L12 · Replicação: líder-seguidor, multi-líder, sem líder; quóruns e consistência — grau 0,75
- 1.1 · L13 · Consenso e coordenação: Paxos/Raft, leader election, relógios lógicos e… (D) — grau 0,25
- 1.1 · L14 · Análise crítica: quando não usar NoSQL/eventual; custos de consistência,… — grau 0,75
- 1.2 · L16 · Arquitetura de DFS: namenode/datanodes, blocos, replicação e rack awareness… — grau 0,25
- 1.2 · L17 · Object storage: buckets, objetos, metadados, durabilidade e consistência… — grau 0,25
- 1.2 · L18 · Key-value e wide-column stores: Bigtable/HBase, Dynamo/Cassandra e modelos de… — grau 0,50
- 1.2 · L20 · Data lake e tabelas abertas: Parquet/ORC, catálogo e layout por partições… (D) — grau 0,25
- 1.2 · L24 · Gerenciamento de metadados e catálogo (D) — grau 0,25
- 1.4 · L26 · GFS (Ghemawat et al., 2003) e HDFS como referências clássicas — grau 0,75
- 1.5 · L35 · Formalização de quórum R + W > N e trade-offs entre latência e consistência — grau 0,75
- 1.5 · L36 · CAP/PACELC com análise de latência e partição em cenários concretos — grau 0,50
- 1.5 · L37 · Complexidade e custos de replicação: fan-out, largura de banda e latência de… (D) — grau 0,50
- 1.5 · L38 · Hotspots e skew em sharding; técnicas de salting e rebalanceamento — grau 0,75
- 1.5 · L39 · Casos-limite: falha de coordenador, split-brain, stale reads e perda de quórum — grau 0,50

**Não atendidos: 11**

- 1.1 · L10 · Transações distribuídas: ACID, 2PC e limitações; BASE como contraponto
- 1.2 · L19 · Bancos relacionais distribuídos/NewSQL: sharding, replicação e transações…
- 1.2 · L23 · Consistência e versionamento: MVCC, snapshots e timestamps (D)
- 1.4 · L28 · Kleppmann, Designing Data-Intensive Applications (2017)
- 1.4 · L29 · Abadi (2012), consistency tradeoffs e PACELC
- 1.4 · L30 · Documentação técnica atual de Apache Hadoop/HDFS, Apache Cassandra, Apache… [inexigível]
- 1.4 · L31 · Parquet/ORC e catálogos (Apache Hive Metastore, Apache Iceberg) (fronteira… (D)
- 1.4 · L32 · Özsu & Valduriez, Principles of Distributed Database Systems (verificar… (D)
- 1.4 · L33 · YCSB (Yahoo! Cloud Serving Benchmark) para avaliação de armazenamentos… (D) [inexigível]
- 1.5 · L40 · Relação entre MVCC, snapshots e isolamento; anomalias de concorrência
- 1.5 · L41 · Exemplo aplicado: modelagem de armazenamento para sessões/telemetria com… (D)

(D) = desejável no DeepSeek; [inexigível] = documentação/benchmark reclassificado (A.3); L = linha em `barema-deepseek/ponto-1.note`.

**Penalizações justificadas**

- Transações distribuídas (ACID, 2PC, BASE), bancos relacionais distribuídos/NewSQL e MVCC estão ausentes. O DeepSeek cobra esse bloco em 1.1, 1.2 e 1.5 (peso literal somado de 0,90), por isso é a maior perda do ponto.
- Arquiteturas concretas ficam em uma frase cada: DFS (namenode/datanodes, blocos), object storage e modelos wide-column/key-value (L66–70).
- As referências vão de 1990 a 2007; não há obra atual (Kleppmann, Abadi/PACELC), o que pesa em "atualização" (1.4).
- Não há exemplo aplicado (busca por "exemplo": 0 ocorrências).
- Avaliação técnica independente: Nenhum erro conceitual encontrado. As cinco referências conferem com obras reais (GFS 2003, Dynamo 2007, Herlihy & Wing 1990, Gilbert & Lynch 2002, Bigtable 2006). As referências não trazem título; numa prova manuscrita isso costuma ser aceito.

Maiores ganhos possíveis na leitura central (quanto a nota subiria se o subitem estivesse completo, respeitado o teto do item; inexigíveis excluídos):

| Subitem DeepSeek | Item | Grau atual | Ganho na nota |
|---|---|---|---|
| L19 · Bancos relacionais distribuídos/NewSQL: sharding, replicação e… | 1.2 | 0,00 | +0,39 |
| L16 · Arquitetura de DFS: namenode/datanodes, blocos, replicação e rack… | 1.2 | 0,25 | +0,35 |
| L10 · Transações distribuídas: ACID, 2PC e limitações; BASE como contraponto | 1.1 | 0,00 | +0,33 |
| L17 · Object storage: buckets, objetos, metadados, durabilidade e… | 1.2 | 0,25 | +0,30 |
| L28 · Kleppmann, Designing Data-Intensive Applications (2017) | 1.4 | 0,00 | +0,27 |

**Nota final**

- Nota central: **7,1**.
- Intervalo plausível: 6,3 – 8,2, entre banca literal (R1) e banca viável (R3).
- Sensibilidade aos graus ambíguos (9 de 33 subitens): 6,8 – 7,6.
- Confiança: média-baixa.

**Risco de superestimação**

- Menções breves (L66–70) receberam 0,25–0,5; uma banca que exija arquitetura de HDFS/S3 pode zerá-las.
- Se a banca considerar "gerenciamento de dados" sinônimo de transações, a lacuna pode pesar mais do que o DeepSeek prevê.

**Risco de subestimação**

- Precisão e crítica (CAP, quórum, "balanceamento de dados ≠ balanceamento de carga") podem valer mais em 1.1 do que a lista de cobertura credita.
- Herlihy & Wing e Gilbert & Lynch são referências canônicas fora da lista DeepSeek e não receberam crédito.

### Ponto 2 — Processamento de Dados em Larga Escala: Processamento Paralelo e Distribuído em Larga Escala

Dissertação: `prova-escrita/2-pdle-processamento-paralelo-e-distribuido-em-larga-escala_v2.md` · Barema DeepSeek: `prova-escrita/barema-deepseek/ponto-2.note`

**Critérios oficiais e notas**

| Critério oficial | Máx. | Fonte | R1 literal | R2 central | R3 viável |
|---|---|---|---|---|---|
| 1.1 Domínio técnico/científico/crítico do ponto sorteado | 2,5 | DeepSeek (9 subitens) | 2,01 | 2,45 | 2,50 |
| 1.2 Abordagem das ideias fundamentais do conteúdo | 2,5 | DeepSeek (9 subitens) | 1,41 | 1,64 | 2,05 |
| 1.3 Organização, coerência, clareza e sequência lógica de ideias | 0,5 | Hipótese 95% | 0,475 | 0,475 | 0,475 |
| 1.4 Atualização do conteúdo / referências bibliográficas / normas técnicas | 1,0 | DeepSeek (9 subitens) | 0,36 | 0,66 | 0,82 |
| 1.5 Aprofundamento do conteúdo | 1,0 | DeepSeek (7 subitens) | 0,60 | 0,71 | 0,88 |
| 2.1 Uso adequado de terminologia técnico-científica | 1,0 | Hipótese 95% | 0,950 | 0,950 | 0,950 |
| 2.2 Estruturação coerente do texto com introdução, desenvolvimento e conclusão | 0,5 | Hipótese 95% | 0,475 | 0,475 | 0,475 |
| 2.3 Precisão e objetividade | 0,5 | Hipótese 95% | 0,475 | 0,475 | 0,475 |
| 2.4 Correção ortográfica e gramatical | 0,5 | Hipótese 95% | 0,475 | 0,475 | 0,475 |
| **Total** | **10,0** | | **7,24** | **8,31** | **9,11** |

**Evidências textuais relevantes**

- Speedup, eficiência e Lei de Amdahl formalizados (L15–27); strong × weak scaling com Gustafson [2] (L31).
- Granularidade, balanceamento por trabalho, stragglers e execução especulativa (L37–43).
- Decomposição T_total = T_comp + T_comm + T_sync + T_overhead (L51–55); localidade × balanceamento; custo do shuffle (L59–61).
- MapReduce com fluxo e limitação para cargas iterativas (L67–75).
- DAG, Spark e lineage, com o trade-off replicação × recomputação × checkpointing (L79–89).
- Seção crítica com cauda da distribuição e custos físicos sob abstrações (L93–107).

**Critérios DeepSeek atendidos (grau 1): 9 de 34**

- 1.1 · L10 · Sincronização e comunicação: barreiras, shuffle, dependências e custos de rede
- 1.1 · L11 · Tolerância a falhas: reexecução de tarefas, lineage, checkpoints e execução…
- 1.1 · L12 · Análise crítica: overhead de comunicação, skew, stragglers, limites de escala…
- 1.1 · L13 · Localidade de dados e relação entre armazenamento e processamento (fronteira… (D)
- 1.2 · L23 · Tolerância a falhas em Spark: lineage, reexecução de tarefas e checkpoints
- 1.2 · L24 · Escalonamento de tarefas: localidade de dados, speculative execution e… (D)
- 1.4 · L26 · Dean & Ghemawat, MapReduce (2004)
- 1.4 · L27 · Zaharia et al., Resilient Distributed Datasets (2012)
- 1.5 · L38 · Stragglers e speculative execution: causas e impacto na latência de cauda

**Parcialmente atendidos: 17**

- 1.1 · L6 · Definição formal de processamento paralelo × distribuído: memória… — grau 0,75
- 1.1 · L7 · Taxonomia de paralelismo: paralelismo de dados, de tarefas e pipeline;… — grau 0,75
- 1.1 · L8 · Modelos de execução: MapReduce, DAG/dataflow e BSP; propriedades e critérios… — grau 0,75
- 1.1 · L9 · Métricas de desempenho: speedup, eficiência, throughput, latência; leis de… — grau 0,75
- 1.1 · L14 · Coordenação de recursos e consenso para escalonamento em cluster (fronteira… (D) — grau 0,25
- 1.2 · L16 · Modelo MapReduce: funções map, shuffle/sort e reduce; exemplo canônico de… — grau 0,75
- 1.2 · L18 · Spark: RDDs, linhagem, transformações/ações e avaliação preguiçosa — grau 0,50
- 1.2 · L20 · Escalonamento por DAG: estágios, dependências narrow/wide e barreiras de… — grau 0,75
- 1.2 · L21 · Particionamento e paralelismo: partições, repartition/coalesce e número de… — grau 0,50
- 1.2 · L22 · Operações distribuídas: joins broadcast e shuffle, groupBy e agregações — grau 0,50
- 1.4 · L31 · Dean & Barroso, The Tail at Scale (2013) — grau 0,25
- 1.4 · L32 · Documentação técnica atual de Apache Hadoop/MapReduce/YARN e Apache Spark… [inexigível] — grau 0,25
- 1.5 · L36 · Formalização de speedup S(n) = T1/Tn, eficiência e limites de Amdahl/Gustafson — grau 0,75
- 1.5 · L37 · Análise de custo de shuffle: rede, disco, serialização e efeito de… — grau 0,50
- 1.5 · L39 · Casos-limite: falha de executor, perda de partição e recomputação longa por… — grau 0,75
- 1.5 · L40 · Trade-offs: memória × disco, broadcast join × shuffle join e repartition ×… — grau 0,25
- 1.5 · L41 · Relação não trivial entre localidade de dados, elasticidade e custo de… (D) — grau 0,50

**Não atendidos: 8**

- 1.2 · L17 · Hadoop MapReduce e YARN: arquitetura de job, ResourceManager, NodeManager e…
- 1.2 · L19 · DataFrames/Datasets e otimizador Catalyst no Spark SQL (D)
- 1.4 · L28 · Malewicz et al., Pregel (2010) (D)
- 1.4 · L29 · Valiant, modelo BSP (1990) (D)
- 1.4 · L30 · Kleppmann, Designing Data-Intensive Applications (2017)
- 1.4 · L33 · Apache Flink para processamento batch/stream unificado (fronteira com o Ponto… (D)
- 1.4 · L34 · Benchmarks HiBench e TPCx-HS (verificar versões) (D) [inexigível]
- 1.5 · L42 · Exemplo aplicado: pipeline de agregação em larga escala com escolha… (D)

(D) = desejável no DeepSeek; [inexigível] = documentação/benchmark reclassificado (A.3); L = linha em `barema-deepseek/ponto-2.note`.

**Penalizações justificadas**

- Hadoop MapReduce/YARN ausente (0,30 essencial em 1.2).
- O Spark aparece só por lineage e memória; RDD, transformações/ações e avaliação preguiçosa ausentes (L81).
- Operadores distribuídos (joins broadcast × shuffle, repartition/coalesce) ausentes, o que afeta 1.2 e 1.5.
- Paralelismo de pipeline e BSP ausentes; não há exemplo aplicado (contagem de palavras).
- Kleppmann e "The Tail at Scale" não citados, embora a latência de cauda seja discutida.
- Avaliação técnica independente: Nenhum erro encontrado. A fórmula de Amdahl está correta. Gustafson [2] é citado para weak scaling sem a lei escrita, o que é correto mas incompleto.

Maiores ganhos possíveis na leitura central (quanto a nota subiria se o subitem estivesse completo, respeitado o teto do item; inexigíveis excluídos):

| Subitem DeepSeek | Item | Grau atual | Ganho na nota |
|---|---|---|---|
| L17 · Hadoop MapReduce e YARN: arquitetura de job, ResourceManager,… | 1.2 | 0,00 | +0,35 |
| L30 · Kleppmann, Designing Data-Intensive Applications (2017) | 1.4 | 0,00 | +0,27 |
| L18 · Spark: RDDs, linhagem, transformações/ações e avaliação preguiçosa | 1.2 | 0,50 | +0,20 |
| L22 · Operações distribuídas: joins broadcast e shuffle, groupBy e… | 1.2 | 0,50 | +0,20 |
| L28 · Malewicz et al., Pregel (2010) (D) | 1.4 | 0,00 | +0,18 |

**Nota final**

- Nota central: **8,3**.
- Intervalo plausível: 7,2 – 9,1, entre banca literal (R1) e banca viável (R3).
- Sensibilidade aos graus ambíguos (5 de 34 subitens): 8,1 – 8,4.
- Confiança: média-baixa.

**Risco de superestimação**

- Baixo: as notas parciais se apoiam em trechos explícitos.

**Risco de subestimação**

- YARN e a API do Spark são detalhes de produto; uma banca centrada em conceitos pode não cobrá-los (cenário viável: 9,1).
- Amdahl (1967) e Gustafson (1988) são citações corretas que a lista DeepSeek não pontua.

### Ponto 3 — Processamento de Dados em Larga Escala: Processamento de Fluxos e Arquiteturas de Dados

Dissertação: `prova-escrita/3-pdle-processamento-de-fluxos-e-arquiteturas-de-dados_v2.md` · Barema DeepSeek: `prova-escrita/barema-deepseek/ponto-3.note`

**Critérios oficiais e notas**

| Critério oficial | Máx. | Fonte | R1 literal | R2 central | R3 viável |
|---|---|---|---|---|---|
| 1.1 Domínio técnico/científico/crítico do ponto sorteado | 2,5 | DeepSeek (10 subitens) | 2,11 | 2,40 | 2,50 |
| 1.2 Abordagem das ideias fundamentais do conteúdo | 2,5 | DeepSeek (9 subitens) | 1,46 | 1,59 | 1,99 |
| 1.3 Organização, coerência, clareza e sequência lógica de ideias | 0,5 | Hipótese 95% | 0,475 | 0,475 | 0,475 |
| 1.4 Atualização do conteúdo / referências bibliográficas / normas técnicas | 1,0 | DeepSeek (9 subitens) | 0,57 | 0,72 | 0,90 |
| 1.5 Aprofundamento do conteúdo | 1,0 | DeepSeek (8 subitens) | 0,69 | 0,92 | 1,00 |
| 2.1 Uso adequado de terminologia técnico-científica | 1,0 | Hipótese 95% | 0,950 | 0,950 | 0,950 |
| 2.2 Estruturação coerente do texto com introdução, desenvolvimento e conclusão | 0,5 | Hipótese 95% | 0,475 | 0,475 | 0,475 |
| 2.3 Precisão e objetividade | 0,5 | Hipótese 95% | 0,475 | 0,475 | 0,475 |
| 2.4 Correção ortográfica e gramatical | 0,5 | Hipótese 95% | 0,475 | 0,475 | 0,475 |
| **Total** | **10,0** | | **7,69** | **8,48** | **9,24** |

**Evidências textuais relevantes**

- Bounded × unbounded e batch × streaming complementares (L13–15); cadeia fonte → serving (L20).
- Event time × processing time, tipos de janela e as três perguntas do Dataflow (L31–43).
- Estado formalizado como (s_{t+1}, y_t) = f(s_t, x_t), com checkpoint e replay (L47–55).
- Semânticas at-most/at-least/exactly-once e a condição fim a fim no sink (L57–59).
- Log particionado e o trade-off ordenação global × escalabilidade (L63–67).
- Lambda × Kappa e lakehouse (L71–75); backlog por λ_produção > λ_consumo e backpressure (L83–89).

**Critérios DeepSeek atendidos (grau 1): 13 de 36**

- 1.1 · L6 · Definição formal de stream e distinção entre dados limitados (batch) e…
- 1.1 · L8 · Semânticas de entrega: at-most-once, at-least-once e exactly-once;…
- 1.1 · L10 · Watermarks e tratamento de eventos atrasados; allowed lateness
- 1.1 · L14 · Análise crítica: quando não usar streaming; custos, complexidade e limites do…
- 1.2 · L18 · Arquitetura Kappa: log imutável, reprocessamento e stream único; limitações
- 1.2 · L22 · Exactly-once fim a fim: checkpoints, transações e idempotência em sinks
- 1.2 · L23 · Camadas de arquitetura: ingestão, armazenamento, processamento e serving;…
- 1.4 · L27 · Kreps et al., Kafka (2011)
- 1.4 · L28 · Akidau et al., The Dataflow Model (2015)
- 1.4 · L29 · Carbone et al., Apache Flink (2015)
- 1.4 · L31 · Marz & Warren, Big Data (2015)
- 1.5 · L39 · Exactly-once fim a fim: transações, idempotência e trade-offs com latência e…
- 1.5 · L41 · Trade-offs Lambda × Kappa: reprocessamento, duplicação de código, latência e…

**Parcialmente atendidos: 20**

- 1.1 · L7 · Tempo de evento × tempo de ingestão × tempo de processamento; desordem e… — grau 0,75
- 1.1 · L9 · Processamento com estado: estado chaveado, backends e recuperação — grau 0,75
- 1.1 · L11 · Janelas tumbling, sliding, session e global; triggers e eviction — grau 0,75
- 1.1 · L12 · Backpressure e controle de fluxo em pipelines de stream (D) — grau 0,75
- 1.1 · L13 · Log distribuído, partições, offsets e consumer groups (fronteira com o Ponto… — grau 0,75
- 1.1 · L15 · Trade-offs entre motores unificados batch/stream e pipelines especializados… (D) — grau 0,50
- 1.2 · L17 · Arquitetura Lambda: camadas batch, speed e serving; funcionamento e limitações — grau 0,75
- 1.2 · L19 · Ingestão de dados: conectores, CDC e pipelines de eventos — grau 0,25
- 1.2 · L20 · Kafka: tópicos, partições, replicação, offsets, retenção e consumer groups — grau 0,50
- 1.2 · L21 · Motores de stream: Flink, Kafka Streams e Spark Structured Streaming;… — grau 0,25
- 1.2 · L24 · Orquestração de pipelines, DAGs e lineage (D) — grau 0,25
- 1.2 · L25 · Padrões de serving: materialized views, CQRS e stores de leitura — grau 0,25
- 1.4 · L32 · Kreps, Questioning the Lambda Architecture (2014) — grau 0,25
- 1.4 · L34 · Documentação atual de Apache Kafka, Apache Flink e Spark Structured Streaming… [inexigível] — grau 0,25
- 1.4 · L35 · Documentação de Apache Iceberg/Hudi/Delta Lake (fronteira com o Ponto 1) (D) [inexigível] — grau 0,25
- 1.5 · L37 · Formalização de watermarks: completude versus latência e heurísticas de avanço — grau 0,75
- 1.5 · L38 · Janelas e triggers: allowed lateness, modos de acumulação e emissão de… — grau 0,75
- 1.5 · L40 · Casos-limite: eventos além da latência permitida, partições quentes e falha… — grau 0,25
- 1.5 · L42 · Relação entre ordenação por chave, partições e paralelismo em operadores… (D) — grau 0,75
- 1.5 · L43 · Backpressure e skew em operadores stateful (D) — grau 0,50

**Não atendidos: 3**

- 1.4 · L30 · Akidau, Chernyak & Lax, Streaming Systems (2018)
- 1.4 · L33 · Kleppmann, Designing Data-Intensive Applications (2017)
- 1.5 · L44 · Exemplo aplicado: detecção de fraude/anomalia em tempo real com janelas e… (D)

(D) = desejável no DeepSeek; [inexigível] = documentação/benchmark reclassificado (A.3); L = linha em `barema-deepseek/ponto-3.note`.

**Penalizações justificadas**

- Nenhum motor (Flink, Kafka Streams, Spark Structured Streaming) é nomeado no texto; Carbone et al. é citado, mas o Flink não aparece.
- Kafka sem tópicos, offsets, consumer groups e replicação (L65–67).
- Ingestão (CDC, conectores) e padrões de serving (views materializadas, CQRS) só nomeados.
- Casos-limite (partição quente, falha de checkpoint) e exemplo aplicado ausentes.
- Avaliação técnica independente: Nenhum erro encontrado. Carbone et al. 2017 (gestão de estado no Flink) é obra real e pertinente; o DeepSeek lista o artigo de 2015 do mesmo grupo.

Maiores ganhos possíveis na leitura central (quanto a nota subiria se o subitem estivesse completo, respeitado o teto do item; inexigíveis excluídos):

| Subitem DeepSeek | Item | Grau atual | Ganho na nota |
|---|---|---|---|
| L21 · Motores de stream: Flink, Kafka Streams e Spark Structured Streaming;… | 1.2 | 0,25 | +0,29 |
| L19 · Ingestão de dados: conectores, CDC e pipelines de eventos | 1.2 | 0,25 | +0,20 |
| L25 · Padrões de serving: materialized views, CQRS e stores de leitura | 1.2 | 0,25 | +0,20 |
| L20 · Kafka: tópicos, partições, replicação, offsets, retenção e consumer… | 1.2 | 0,50 | +0,19 |
| L24 · Orquestração de pipelines, DAGs e lineage (D) | 1.2 | 0,25 | +0,16 |

**Nota final**

- Nota central: **8,5**.
- Intervalo plausível: 7,7 – 9,2, entre banca literal (R1) e banca viável (R3).
- Sensibilidade aos graus ambíguos (5 de 36 subitens): 8,3 – 8,6.
- Confiança: média.

**Risco de superestimação**

- Baixo.

**Risco de subestimação**

- A cobertura conceitual das engines (L67) pode bastar para uma banca não orientada a produtos.

### Ponto 4 — Mineração de Dados: Descoberta de Conhecimento, Análise Exploratória de Dados, Identificação de Padrões e Anomalias

Dissertação: `prova-escrita/4-mineracao-de-dados-descoberta-de-conhecimento-aed-identificacao-de-padroes-e-anomalias_v2.md` · Barema DeepSeek: `prova-escrita/barema-deepseek/ponto-4.note`

**Critérios oficiais e notas**

| Critério oficial | Máx. | Fonte | R1 literal | R2 central | R3 viável |
|---|---|---|---|---|---|
| 1.1 Domínio técnico/científico/crítico do ponto sorteado | 2,5 | DeepSeek (10 subitens) | 1,82 | 2,12 | 2,50 |
| 1.2 Abordagem das ideias fundamentais do conteúdo | 2,5 | DeepSeek (11 subitens) | 1,07 | 1,31 | 1,64 |
| 1.3 Organização, coerência, clareza e sequência lógica de ideias | 0,5 | Hipótese 95% | 0,475 | 0,475 | 0,475 |
| 1.4 Atualização do conteúdo / referências bibliográficas / normas técnicas | 1,0 | DeepSeek (9 subitens) | 0,51 | 0,64 | 0,80 |
| 1.5 Aprofundamento do conteúdo | 1,0 | DeepSeek (8 subitens) | 0,35 | 0,44 | 0,55 |
| 2.1 Uso adequado de terminologia técnico-científica | 1,0 | Hipótese 95% | 0,950 | 0,950 | 0,950 |
| 2.2 Estruturação coerente do texto com introdução, desenvolvimento e conclusão | 0,5 | Hipótese 95% | 0,475 | 0,475 | 0,475 |
| 2.3 Precisão e objetividade | 0,5 | Hipótese 95% | 0,475 | 0,475 | 0,475 |
| 2.4 Correção ortográfica e gramatical | 0,5 | Hipótese 95% | 0,475 | 0,475 | 0,475 |
| **Total** | **10,0** | | **6,61** | **7,36** | **8,34** |

**Evidências textuais relevantes**

- Mineração como etapa do KDD e critérios válido/novo/útil/interpretável (L5–13).
- Etapas do KDD com processo não linear (L19–29); distinção dado × padrão × conhecimento (L31–37).
- EDA como exploração iterativa que gera hipóteses (L43–57).
- Suporte, confiança e lift formalizados e interpretados (L63–77).
- Tipologia de anomalias e maldição da dimensionalidade (L87–99); seção crítica com associação ≠ causalidade (L103–121).

**Critérios DeepSeek atendidos (grau 1): 11 de 38**

- 1.1 · L6 · Definição formal de KDD (Knowledge Discovery in Databases) e distinção entre…
- 1.1 · L7 · Definição de Análise Exploratória de Dados (EDA) e seu papel no ciclo de…
- 1.1 · L8 · Definição formal de padrão e de anomalia/outlier, com critérios de distinção
- 1.1 · L12 · Limitações: maldição da dimensionalidade e risco de overfitting em descoberta…
- 1.1 · L13 · Pré-processamento: limpeza, normalização, discretização e tratamento de…
- 1.2 · L17 · Processo KDD: etapas de seleção, pré-processamento, transformação, mineração…
- 1.2 · L27 · Avaliação de padrões: medidas de interestingness e validação de resultados (D)
- 1.4 · L29 · Fayyad, Piatetsky-Shapiro & Smyth (1996), From Data Mining to Knowledge…
- 1.4 · L30 · Han, Kamber & Pei, Data Mining: Concepts and Techniques (verificar edição)
- 1.4 · L31 · Tukey (1977), Exploratory Data Analysis
- 1.4 · L33 · Aggarwal, Outlier Analysis (verificar edição)

**Parcialmente atendidos: 20**

- 1.1 · L10 · Medidas de similaridade e distância: Euclidiana, Manhattan, Jaccard e… — grau 0,25
- 1.1 · L11 · Análise crítica da EDA: correlação não implica causalidade e riscos de viés… — grau 0,75
- 1.1 · L14 · Análise crítica de medidas de avaliação de padrões (ex.: suporte e confiança… (D) — grau 0,75
- 1.1 · L15 · Quando não usar métodos: clustering em alta dimensão sem redução, detecção de… (D) — grau 0,25
- 1.2 · L18 · EDA: estatísticas descritivas (média, mediana, desvio padrão, quartis) e sua… — grau 0,25
- 1.2 · L19 · EDA: visualizações (histograma, boxplot, dispersão, heatmap) e o que cada uma… — grau 0,25
- 1.2 · L20 · Análise de correlação: coeficientes de Pearson e Spearman e limitações — grau 0,25
- 1.2 · L21 · Regras de associação: suporte, confiança e lift; algoritmo Apriori — grau 0,75
- 1.2 · L23 · Agrupamento (clustering) como descoberta de padrões: k-means, hierárquico e… — grau 0,25
- 1.2 · L24 · Detecção de anomalias: métodos estatísticos (z-score, intervalo interquartil) — grau 0,25
- 1.2 · L25 · Detecção de anomalias: métodos baseados em distância (k-NN) e densidade (LOF) — grau 0,25
- 1.2 · L26 · Isolation Forest e One-Class SVM (fronteira com o Ponto 5) (D) — grau 0,25
- 1.4 · L32 · Chandola, Banerjee & Kumar (2009), Anomaly Detection: A Survey — grau 0,25
- 1.4 · L36 · Agrawal & Srikant (1994), Fast Algorithms for Mining Association Rules — grau 0,25
- 1.5 · L39 · Formalização de suporte, confiança e lift; propriedades (ex.: confiança não é… — grau 0,75
- 1.5 · L41 · Escolha de medida de distância e impacto em clustering/anomalias; efeito da… — grau 0,50
- 1.5 · L42 · Sensibilidade a parâmetros: k em k-NN, eps/minPts em DBSCAN, contaminação em… — grau 0,25
- 1.5 · L43 · Casos-limite: anomalias em alta dimensionalidade, dados categóricos e dados… — grau 0,50
- 1.5 · L44 · Relação entre EDA e detecção automática de anomalias: visualização versus… (D) — grau 0,25
- 1.5 · L45 · Trade-offs em detecção de anomalias: precisão versus recall e custo de falsos… — grau 0,25

**Não atendidos: 7**

- 1.1 · L9 · Tipos de atributos e escalas de medida (nominal, ordinal, intervalar, razão)…
- 1.2 · L22 · Algoritmo FP-Growth e comparação com Apriori (D)
- 1.4 · L34 · CRISP-DM (Shearer, 2000) como processo padrão de mineração de dados
- 1.4 · L35 · Documentação atual de scikit-learn, pandas, matplotlib e seaborn (verificar… [inexigível]
- 1.4 · L37 · Zimek, Schubert & Kriegel (2012), On the Evaluation of Unsupervised Outlier… (D)
- 1.5 · L40 · Complexidade do Apriori (exponencial no pior caso) e otimizações via FP-Growth
- 1.5 · L46 · Exemplo aplicado: detecção de fraude em transações com EDA e Isolation Forest (D)

(D) = desejável no DeepSeek; [inexigível] = documentação/benchmark reclassificado (A.3); L = linha em `barema-deepseek/ponto-4.note`.

**Penalizações justificadas**

- EDA sem conteúdo operacional: estatísticas descritivas, tipos de gráfico e coeficientes de correlação só aparecem como palavras (L49–51).
- Tipos de atributos/escalas de medida e medidas de distância/similaridade ausentes (essenciais em 1.1).
- Agrupamento remetido ao Ponto 5 (L79). É coerente se ambos forem sorteados, mas o DeepSeek trata k-means/DBSCAN como essenciais aqui.
- Métodos de anomalia só por categoria (L97): sem z-score/IQR, k-NN/LOF ou Isolation Forest. Apriori, CRISP-DM e Chandola não aparecem.
- Avaliação técnica independente: Nenhum erro encontrado. As fórmulas de suporte, confiança e lift estão corretas. A tipologia global/contextual/coletiva é a de Chandola et al., citada via Aggarwal; isso é aceitável, mas citar a origem seria melhor.

Maiores ganhos possíveis na leitura central (quanto a nota subiria se o subitem estivesse completo, respeitado o teto do item; inexigíveis excluídos):

| Subitem DeepSeek | Item | Grau atual | Ganho na nota |
|---|---|---|---|
| L23 · Agrupamento (clustering) como descoberta de padrões: k-means,… | 1.2 | 0,25 | +0,27 |
| L10 · Medidas de similaridade e distância: Euclidiana, Manhattan, Jaccard e… | 1.1 | 0,25 | +0,26 |
| L9 · Tipos de atributos e escalas de medida (nominal, ordinal, intervalar,… | 1.1 | 0,00 | +0,23 |
| L18 · EDA: estatísticas descritivas (média, mediana, desvio padrão,… | 1.2 | 0,25 | +0,23 |
| L19 · EDA: visualizações (histograma, boxplot, dispersão, heatmap) e o que… | 1.2 | 0,25 | +0,23 |

**Nota final**

- Nota central: **7,4**.
- Intervalo plausível: 6,6 – 8,3, entre banca literal (R1) e banca viável (R3).
- Sensibilidade aos graus ambíguos (2 de 38 subitens): 7,2 – 7,4.
- Confiança: média.

**Risco de superestimação**

- O grau 1 em "definição formal de padrão e anomalia" pode cair para 0,75 numa banca que espere formalização.

**Risco de subestimação**

- A banca pode aceitar as categorias de métodos (L97) e a fronteira com o Ponto 5 como escolha de recorte.

### Ponto 5 — Aprendizado Supervisionado e Não Supervisionado

Dissertação: `prova-escrita/5-aprendizado-supervisionado-e-nao-supervisionado_v2.md` · Barema DeepSeek: `prova-escrita/barema-deepseek/ponto-5.note`

**Critérios oficiais e notas**

| Critério oficial | Máx. | Fonte | R1 literal | R2 central | R3 viável |
|---|---|---|---|---|---|
| 1.1 Domínio técnico/científico/crítico do ponto sorteado | 2,5 | DeepSeek (11 subitens) | 2,09 | 2,37 | 2,50 |
| 1.2 Abordagem das ideias fundamentais do conteúdo | 2,5 | DeepSeek (11 subitens) | 0,81 | 0,88 | 1,10 |
| 1.3 Organização, coerência, clareza e sequência lógica de ideias | 0,5 | Hipótese 95% | 0,475 | 0,475 | 0,475 |
| 1.4 Atualização do conteúdo / referências bibliográficas / normas técnicas | 1,0 | DeepSeek (10 subitens) | 0,42 | 0,50 | 0,62 |
| 1.5 Aprofundamento do conteúdo | 1,0 | DeepSeek (9 subitens) | 0,33 | 0,36 | 0,45 |
| 2.1 Uso adequado de terminologia técnico-científica | 1,0 | Hipótese 95% | 0,950 | 0,950 | 0,950 |
| 2.2 Estruturação coerente do texto com introdução, desenvolvimento e conclusão | 0,5 | Hipótese 95% | 0,475 | 0,475 | 0,475 |
| 2.3 Precisão e objetividade | 0,5 | Hipótese 95% | 0,475 | 0,475 | 0,475 |
| 2.4 Correção ortográfica e gramatical | 0,5 | Hipótese 95% | 0,475 | 0,475 | 0,475 |
| **Total** | **10,0** | | **6,50** | **6,97** | **7,53** |

**Evidências textuais relevantes**

- Formalização supervisionado × não supervisionado (L7–13) e mapa de tarefas (L16).
- Treinamento como θ* = arg min L(θ), funções de perda (L22–28) e treino/validação/teste com parâmetros × hiperparâmetros (L32–38).
- Viés-variância (L40) e regularização formalizada (L44–48).
- Métricas com a crítica do desbalanceamento (L87–91) e avaliação não supervisionada (L93).
- Validação cruzada, independência do teste e data leakage (L95–112); fórmula de decisão (L118).

**Critérios DeepSeek atendidos (grau 1): 9 de 41**

- 1.1 · L6 · Definição formal de aprendizado supervisionado (dados rotulados) e não…
- 1.1 · L7 · Formulação das tarefas: classificação, regressão, agrupamento e redução de…
- 1.1 · L9 · Trade-off viés-variância; overfitting, underfitting e capacidade de…
- 1.1 · L14 · Análise crítica: desbalanceamento de classes, custos assimétricos de erro e…
- 1.1 · L15 · Distinção entre avaliação supervisionada e não supervisionada: critérios… (D)
- 1.4 · L30 · Hastie, Tibshirani & Friedman, The Elements of Statistical Learning…
- 1.4 · L31 · Bishop, Pattern Recognition and Machine Learning (2006)
- 1.4 · L32 · Murphy, Machine Learning: A Probabilistic Perspective (2012)
- 1.5 · L47 · Casos-limite: desbalanceamento, data leakage, overfitting em alta dimensão e…

**Parcialmente atendidos: 23**

- 1.1 · L8 · Risco esperado, risco empírico e minimização do risco empírico (ERM); função… — grau 0,75
- 1.1 · L10 · Regularização L1/L2 e seu papel no controle de complexidade — grau 0,75
- 1.1 · L11 · Validação: holdout, k-fold, validação estratificada e vazamento de dados… — grau 0,75
- 1.1 · L12 · Métricas de classificação: acurácia, precisão, recall, F1, ROC-AUC e PR-AUC;… — grau 0,75
- 1.1 · L13 · Métricas de regressão: MSE, MAE e R²; interpretação e limitações — grau 0,75
- 1.1 · L16 · Quando não usar aprendizado supervisionado (rótulos escassos) ou não… (D) — grau 0,25
- 1.2 · L18 · Regressão linear e regressão logística: hipóteses, funções de custo e… — grau 0,25
- 1.2 · L19 · Árvores de decisão: impureza (Gini/entropia), divisão e poda — grau 0,25
- 1.2 · L20 · Ensembles: bagging/Random Forest e boosting (AdaBoost/Gradient Boosting) — grau 0,25
- 1.2 · L21 · SVM: margem máxima, vetores de suporte, kernels e parâmetro C — grau 0,25
- 1.2 · L22 · Redes neurais: perceptron/MLP, funções de ativação e backpropagation — grau 0,25
- 1.2 · L23 · k-means: funcionamento, inicialização k-means++, escolha de k e limitações — grau 0,25
- 1.2 · L24 · DBSCAN: eps, minPts, ruído e agrupamentos de forma arbitrária — grau 0,50
- 1.2 · L25 · PCA: componentes principais, variância explicada e redução de dimensionalidade — grau 0,50
- 1.2 · L26 · Avaliação não supervisionada: silhouette, Davies-Bouldin, inércia e limitações — grau 0,75
- 1.2 · L27 · k-NN e maldição da dimensionalidade (D) — grau 0,25
- 1.2 · L28 · Agrupamento hierárquico: linkage e dendrograma (D) — grau 0,25
- 1.4 · L34 · Cortes & Vapnik (1995), Support-Vector Networks — grau 0,25
- 1.4 · L35 · Breiman (2001), Random Forests — grau 0,25
- 1.4 · L37 · Ester et al. (1996), A Density-Based Algorithm for Discovering Clusters… — grau 0,25
- 1.5 · L41 · Formalização de ERM e decomposição viés-variância — grau 0,50
- 1.5 · L42 · Regularização L1/L2: trade-off entre ajuste e complexidade; seleção de… — grau 0,75
- 1.5 · L46 · PCA: variância explicada, limite linear e perda de interpretabilidade — grau 0,25

**Não atendidos: 9**

- 1.4 · L33 · James et al., An Introduction to Statistical Learning (verificar edição)
- 1.4 · L36 · Arthur & Vassilvitskii (2007), k-means++
- 1.4 · L38 · Documentação atual do scikit-learn (verificar versão) [inexigível]
- 1.4 · L39 · Jolliffe, Principal Component Analysis (verificar edição) (D)
- 1.5 · L43 · SVM: trade-offs de kernels e dos parâmetros C e gamma
- 1.5 · L44 · k-means: complexidade, sensibilidade à inicialização e escolha de k; papel do…
- 1.5 · L45 · DBSCAN: sensibilidade a eps/minPts e degradação em alta dimensionalidade
- 1.5 · L48 · Relação não trivial entre redução dimensional e clustering/classificação (D)
- 1.5 · L49 · Exemplo aplicado: pipeline com validação, escolha de modelo e comparação… (D)

(D) = desejável no DeepSeek; [inexigível] = documentação/benchmark reclassificado (A.3); L = linha em `barema-deepseek/ponto-5.note`.

**Penalizações justificadas**

- O item 1.2 do DeepSeek dedica 2,35 dos 2,50 pontos a mecanismos de algoritmos (2,15 deles essenciais). O texto descreve cada método em uma linha (L58–63, L77–81), o que dá a maior perda isolada entre os dez pontos (1.2 = 0,88/2,5).
- O aprofundamento sobre hiperparâmetros específicos (C/γ do SVM, inicialização e escolha de k, eps/minPts) está ausente: 1.5 = 0,36/1,0.
- L1/L2 não são nomeadas; a regularização aparece só na forma geral.
- Faltam referências dos algoritmos (Breiman, Cortes & Vapnik, Ester et al., k-means++).
- Avaliação técnica independente: Nenhum erro encontrado. As afirmações sobre viés/variância, PCA, DBSCAN e leakage estão corretas.

Maiores ganhos possíveis na leitura central (quanto a nota subiria se o subitem estivesse completo, respeitado o teto do item; inexigíveis excluídos):

| Subitem DeepSeek | Item | Grau atual | Ganho na nota |
|---|---|---|---|
| L18 · Regressão linear e regressão logística: hipóteses, funções de custo e… | 1.2 | 0,25 | +0,29 |
| L20 · Ensembles: bagging/Random Forest e boosting (AdaBoost/Gradient… | 1.2 | 0,25 | +0,29 |
| L23 · k-means: funcionamento, inicialização k-means++, escolha de k e… | 1.2 | 0,25 | +0,24 |
| L19 · Árvores de decisão: impureza (Gini/entropia), divisão e poda | 1.2 | 0,25 | +0,20 |
| L21 · SVM: margem máxima, vetores de suporte, kernels e parâmetro C | 1.2 | 0,25 | +0,20 |

**Nota final**

- Nota central: **7,0**.
- Intervalo plausível: 6,5 – 7,5, entre banca literal (R1) e banca viável (R3).
- Sensibilidade aos graus ambíguos (11 de 41 subitens): 6,7 – 7,5.
- Confiança: média.

**Risco de superestimação**

- Baixo: a nota já reflete a superficialidade algorítmica.

**Risco de subestimação**

- O eixo metodológico (validação, leakage, métricas, decisão) é mais forte do que o DeepSeek premia; uma banca que valorize síntese conceitual pode subir a nota (cenário viável: 7,5).
- Se os pontos 4 e 5 forem sorteados juntos, o agrupamento remetido pelo Ponto 4 não volta a ser cobrado, mas aqui também está em uma linha.

### Ponto 6 — Aprendizado por Reforço

Dissertação: `prova-escrita/6-aprendizado-por-reforco_v2.md` · Barema DeepSeek: `prova-escrita/barema-deepseek/ponto-6.note`

**Critérios oficiais e notas**

| Critério oficial | Máx. | Fonte | R1 literal | R2 central | R3 viável |
|---|---|---|---|---|---|
| 1.1 Domínio técnico/científico/crítico do ponto sorteado | 2,5 | DeepSeek (10 subitens) | 2,15 | 2,34 | 2,50 |
| 1.2 Abordagem das ideias fundamentais do conteúdo | 2,5 | DeepSeek (12 subitens) | 1,41 | 1,61 | 2,01 |
| 1.3 Organização, coerência, clareza e sequência lógica de ideias | 0,5 | Hipótese 95% | 0,475 | 0,475 | 0,475 |
| 1.4 Atualização do conteúdo / referências bibliográficas / normas técnicas | 1,0 | DeepSeek (8 subitens) | 0,57 | 0,77 | 0,96 |
| 1.5 Aprofundamento do conteúdo | 1,0 | DeepSeek (10 subitens) | 0,20 | 0,27 | 0,33 |
| 2.1 Uso adequado de terminologia técnico-científica | 1,0 | Hipótese 95% | 0,950 | 0,950 | 0,950 |
| 2.2 Estruturação coerente do texto com introdução, desenvolvimento e conclusão | 0,5 | Hipótese 95% | 0,475 | 0,475 | 0,475 |
| 2.3 Precisão e objetividade | 0,5 | Hipótese 95% | 0,475 | 0,475 | 0,475 |
| 2.4 Correção ortográfica e gramatical | 0,5 | Hipótese 95% | 0,475 | 0,475 | 0,475 |
| **Total** | **10,0** | | **7,19** | **7,83** | **8,65** |

**Evidências textuais relevantes**

- Ciclo agente-ambiente formalizado e contraste com o supervisionado (L7–19).
- MDP (S, A, P, R, γ), propriedade de Markov, retorno e objetivo π* (L23–45); credit assignment (L47).
- V^π e Q^π (L53–63); Bellman de expectativa e de otimalidade (L73–87).
- TD(0) com δ_t e bootstrapping (L89–95); ε-greedy (L104).
- Q-learning com regra de atualização, off- × on-policy (L110–116); policy gradient e actor-critic (L118–123); model-free × model-based (L125).
- Limitações: recompensas esparsas, eficiência amostral, reward hacking e safe RL (L131–152).

**Critérios DeepSeek atendidos (grau 1): 15 de 40**

- 1.1 · L6 · Definição formal de Processo de Decisão de Markov (MDP): estados, ações,…
- 1.1 · L7 · Política, retorno descontado e funções de valor V^π e Q^π
- 1.1 · L8 · Equações de Bellman esperadas e de otimalidade; relação entre avaliação e…
- 1.1 · L9 · Exploração versus exploitation e necessidade de exploração em ambientes…
- 1.1 · L10 · Distinção model-based × model-free e on-policy × off-policy
- 1.1 · L11 · Atribuição de crédito, recompensa atrasada, horizonte e papel do fator de…
- 1.1 · L12 · Análise crítica: ineficiência amostral, instabilidade, reward hacking e risco…
- 1.1 · L14 · Distinção entre RL e aprendizado supervisionado (fronteira com o Ponto 5)
- 1.2 · L22 · Q-learning (off-policy) e SARSA (on-policy)
- 1.2 · L25 · Policy gradient/REINFORCE e actor-critic
- 1.4 · L30 · Sutton & Barto, Reinforcement Learning: An Introduction (2ª ed., 2018)
- 1.4 · L32 · Watkins & Dayan (1992), Q-learning
- 1.4 · L33 · Mnih et al. (2015), Human-level control through deep reinforcement learning
- 1.4 · L34 · Williams (1992), Simple Statistical Gradient-Following Algorithms for…
- 1.5 · L47 · Casos-limite: recompensas esparsas, ações contínuas, não estacionariedade e…

**Parcialmente atendidos: 12**

- 1.1 · L13 · Pressupostos de convergência e sensibilidade a hiperparâmetros (gamma, taxa… — grau 0,25
- 1.2 · L17 · Loop agente-ambiente; episódios versus tarefas contínuas — grau 0,75
- 1.2 · L18 · Retorno descontado e políticas determinísticas versus estocásticas — grau 0,75
- 1.2 · L19 · Programação dinâmica: avaliação de política, policy iteration e value… — grau 0,25
- 1.2 · L20 · Monte Carlo: estimação por retornos e variantes primeira visita/todas as… — grau 0,25
- 1.2 · L21 · TD(0): atualização por diferença temporal e comparação com Monte Carlo — grau 0,75
- 1.2 · L23 · ε-greedy, softmax e decaimento da exploração — grau 0,50
- 1.2 · L24 · DQN: aproximação de função, experience replay e target network — grau 0,25
- 1.2 · L27 · Model-based RL: Dyna e uso de planejamento (D) — grau 0,50
- 1.4 · L31 · Bellman (1957), Dynamic Programming — grau 0,25
- 1.5 · L41 · Deadly triad: aproximação de função, bootstrapping e off-policy — grau 0,25
- 1.5 · L44 · Reward shaping e shaping baseado em potenciais (D) — grau 0,25

**Não atendidos: 13**

- 1.1 · L15 · Quando não usar RL: se há supervisão, planejamento ou bandit simples… (D)
- 1.2 · L26 · Bandit multi-armado: exploração, recompensa e regret (D)
- 1.2 · L28 · Exemplo aplicado canônico (gridworld ou CartPole) (D)
- 1.4 · L35 · Schulman et al. (2017), Proximal Policy Optimization Algorithms
- 1.4 · L36 · Puterman (1994), Markov Decision Processes (D)
- 1.4 · L37 · Documentação atual de Gymnasium, Stable-Baselines3 e RLlib (verificar versões) [inexigível]
- 1.5 · L39 · Operador de Bellman como contração e convergência de métodos de valor
- 1.5 · L40 · Condições de convergência do Q-learning: exploração suficiente, taxas…
- 1.5 · L42 · Trade-off Monte Carlo × TD: viés, variância e eficiência amostral
- 1.5 · L43 · Exploração formal: regret, UCB e Thompson sampling em bandits (D)
- 1.5 · L45 · Superestimação no DQN e Double DQN (D)
- 1.5 · L46 · PPO: objetivo truncado e trade-offs entre estabilidade e eficiência amostral
- 1.5 · L48 · Exemplo aprofundado: comparação Q-learning × policy gradient em ambiente com… (D)

(D) = desejável no DeepSeek; [inexigível] = documentação/benchmark reclassificado (A.3); L = linha em `barema-deepseek/ponto-6.note`.

**Penalizações justificadas**

- O item 1.5 rende só 0,27/1,0: contração de Bellman, condições de convergência do Q-learning, deadly triad, MC × TD (viés/variância) e PPO estão ausentes (busca: 0).
- Monte Carlo e programação dinâmica só mencionados (L89, L95).
- DQN sem experience replay e target network (L127).
- Faltam bandits e uma seção "quando não usar RL"; Bellman (1957) e PPO não são citados.
- Avaliação técnica independente: Nenhum erro relevante. Uma nuance menor: no ε-greedy usual, a ação aleatória é sorteada entre todas, e "explora-se outra alternativa" (L104) sugere excluir a gulosa; isso não muda a nota. γ ∈ [0,1) está correto para horizonte infinito.

Maiores ganhos possíveis na leitura central (quanto a nota subiria se o subitem estivesse completo, respeitado o teto do item; inexigíveis excluídos):

| Subitem DeepSeek | Item | Grau atual | Ganho na nota |
|---|---|---|---|
| L24 · DQN: aproximação de função, experience replay e target network | 1.2 | 0,25 | +0,26 |
| L19 · Programação dinâmica: avaliação de política, policy iteration e value… | 1.2 | 0,25 | +0,21 |
| L39 · Operador de Bellman como contração e convergência de métodos de valor | 1.5 | 0,00 | +0,20 |
| L20 · Monte Carlo: estimação por retornos e variantes primeira visita/todas… | 1.2 | 0,25 | +0,17 |
| L26 · Bandit multi-armado: exploração, recompensa e regret (D) | 1.2 | 0,00 | +0,17 |

**Nota final**

- Nota central: **7,8**.
- Intervalo plausível: 7,2 – 8,6, entre banca literal (R1) e banca viável (R3).
- Sensibilidade aos graus ambíguos (3 de 40 subitens): 7,6 – 7,8.
- Confiança: média.

**Risco de superestimação**

- Baixo.

**Risco de subestimação**

- A profundidade formal existe (Bellman de otimalidade, TD, atualização do Q-learning), mas o DeepSeek a credita em 1.1/1.2, não em 1.5. Uma banca que a conte como aprofundamento pode dar 0,5–0,7 em 1.5, cerca de +0,3 a +0,4 no total.

### Ponto 7 — MLOps: Desenvolvimento, Versionamento e Experimentação de Modelos

Dissertação: `prova-escrita/7-mlops-desenvolvimento-versionamento-e-experimentacao-de-modelos_v2.md` · Barema DeepSeek: `prova-escrita/barema-deepseek/ponto-7.note`

**Critérios oficiais e notas**

| Critério oficial | Máx. | Fonte | R1 literal | R2 central | R3 viável |
|---|---|---|---|---|---|
| 1.1 Domínio técnico/científico/crítico do ponto sorteado | 2,5 | DeepSeek (8 subitens) | 1,65 | 1,86 | 2,32 |
| 1.2 Abordagem das ideias fundamentais do conteúdo | 2,5 | DeepSeek (10 subitens) | 1,31 | 1,53 | 1,91 |
| 1.3 Organização, coerência, clareza e sequência lógica de ideias | 0,5 | Hipótese 95% | 0,475 | 0,475 | 0,475 |
| 1.4 Atualização do conteúdo / referências bibliográficas / normas técnicas | 1,0 | DeepSeek (10 subitens) | 0,26 | 0,41 | 0,51 |
| 1.5 Aprofundamento do conteúdo | 1,0 | DeepSeek (8 subitens) | 0,60 | 0,86 | 1,00 |
| 2.1 Uso adequado de terminologia técnico-científica | 1,0 | Hipótese 95% | 0,950 | 0,950 | 0,950 |
| 2.2 Estruturação coerente do texto com introdução, desenvolvimento e conclusão | 0,5 | Hipótese 95% | 0,475 | 0,475 | 0,475 |
| 2.3 Precisão e objetividade | 0,5 | Hipótese 95% | 0,475 | 0,475 | 0,475 |
| 2.4 Correção ortográfica e gramatical | 0,5 | Hipótese 95% | 0,475 | 0,475 | 0,475 |
| **Total** | **10,0** | | **6,68** | **7,50** | **8,60** |

**Evidências textuais relevantes**

- "Modelo ≠ código" e experimento como unidade com proveniência (L7–33).
- Versionamento além do código, artefato, proveniência × linhagem e IDs imutáveis (L39–49).
- Conteúdo do experiment tracking e comparação justa com baselines (L53–63).
- Fórmula da reprodutibilidade com a ressalva de não ser identidade bit a bit (L67–81).
- Validação de dados e de modelo, critérios de aceitação e model registry (L85–105); custos e trade-offs (L109–121).

**Critérios DeepSeek atendidos (grau 1): 9 de 36**

- 1.1 · L8 · Reprodutibilidade formal: determinismo, sementes, ambientes, linhagem e…
- 1.1 · L9 · Versionamento de código, dados, modelo, configuração e ambiente;…
- 1.1 · L10 · Experimentação: hipótese, variáveis, métricas, validação e comparação justa…
- 1.2 · L19 · Versionamento de modelos e artefatos: model registry, metadados, estágios e…
- 1.2 · L24 · Testes de dados e validação de esquema (D)
- 1.4 · L26 · Sculley et al. (2015), Hidden Technical Debt in Machine Learning Systems
- 1.4 · L27 · Breck et al. (2017), The ML Test Score
- 1.5 · L37 · Formalização da reprodutibilidade: mesma tupla (código, dados, ambiente,…
- 1.5 · L38 · Linhagem e grafo de dependências entre datasets, runs e modelos; auditoria

**Parcialmente atendidos: 15**

- 1.1 · L6 · Definição formal de MLOps e delimitação do escopo de desenvolvimento,… — grau 0,75
- 1.1 · L7 · Ciclo de vida de ML e diferenças em relação ao software tradicional: dados… — grau 0,75
- 1.1 · L11 · Dívida técnica em ML: entanglement, undeclared consumers, pipeline jungles e… — grau 0,25
- 1.1 · L12 · Análise crítica: vazamento de dados, overfitting de benchmark, seleção… — grau 0,50
- 1.2 · L15 · Processo CRISP-DM e ciclo iterativo de desenvolvimento de modelos — grau 0,50
- 1.2 · L17 · Controle de versão de código com Git e boas práticas de branches, commits e… — grau 0,25
- 1.2 · L18 · Versionamento de dados: DVC, hashes, armazenamento remoto e reprodutibilidade — grau 0,50
- 1.2 · L20 · Rastreamento de experimentos: parâmetros, métricas, artefatos, runs e… — grau 0,75
- 1.2 · L21 · Gestão de hiperparâmetros: grid/random/Bayesian optimization e registro dos… — grau 0,25
- 1.2 · L22 · Ambientes reprodutíveis: dependências, containers, seeds e configuração — grau 0,75
- 1.2 · L23 · Documentação de experimentos e model cards (D) — grau 0,25
- 1.4 · L28 · Zaharia et al. (2018), Accelerating the Machine Learning Lifecycle with MLflow — grau 0,25
- 1.5 · L39 · Trade-offs: tracking detalhado versus overhead; registry centralizado versus… — grau 0,75
- 1.5 · L40 · Casos-limite: dados mutáveis, dependências não fixadas, seeds não… — grau 0,75
- 1.5 · L41 · Comparação justa de experimentos: mesmos splits, mesma métrica, controle de… — grau 0,75

**Não atendidos: 12**

- 1.1 · L13 · Distinção entre avaliação offline e online (fronteira com o Ponto 9) (D)
- 1.2 · L16 · Estruturação de projeto: organização de código, notebooks versus scripts,…
- 1.4 · L29 · Shearer (2000), CRISP-DM
- 1.4 · L30 · Mitchell et al. (2019), Model Cards for Model Reporting
- 1.4 · L31 · Gebru et al. (2021), Datasheets for Datasets
- 1.4 · L32 · Vartak et al. (2016), ModelDB (D)
- 1.4 · L33 · Snoek et al. (2012), Practical Bayesian Optimization of Machine Learning… (D)
- 1.4 · L34 · Documentação atual de Git, DVC, MLflow, Weights & Biases e TensorBoard… (D) [inexigível]
- 1.4 · L35 · Pineau et al., Machine Learning Reproducibility Checklist (verificar) (D)
- 1.5 · L42 · Relação entre versionamento de dados e vazamento temporal/leakage (D)
- 1.5 · L43 · Estratégias de tuning: espaço de busca, orçamento e early stopping (D)
- 1.5 · L44 · Exemplo aplicado: pipeline reprodutível com Git + DVC + MLflow e registro de… (D)

(D) = desejável no DeepSeek; [inexigível] = documentação/benchmark reclassificado (A.3); L = linha em `barema-deepseek/ponto-7.note`.

**Penalizações justificadas**

- Sculley [1] é citado, mas os tipos de dívida técnica (entanglement, glue code, pipeline jungles) não aparecem: 0,30 essencial em 1.1.
- Camada prática ausente: Git e boas práticas, DVC, MLflow/W&B, estrutura de projeto, busca de hiperparâmetros e containers. É o grosso de 1.2.
- A crítica metodológica não trata data leakage nem overfitting de benchmark (L63, L89).
- Avaliação offline × online não é discutida, por escolha de recorte (L17). CRISP-DM, model cards, datasheets e MLflow não são citados.
- Avaliação técnica independente: Nenhum erro encontrado. Observação sobre o instrumento: no barema DeepSeek do Ponto 7 os subitens de 1.1 somam 2,25 e os de 1.4 somam 1,10, apesar dos subtotais declarados (2,50 e 1,00). Os pesos foram normalizados proporcionalmente.

Maiores ganhos possíveis na leitura central (quanto a nota subiria se o subitem estivesse completo, respeitado o teto do item; inexigíveis excluídos):

| Subitem DeepSeek | Item | Grau atual | Ganho na nota |
|---|---|---|---|
| L13 · Distinção entre avaliação offline e online (fronteira com o Ponto 9) (D) | 1.1 | 0,00 | +0,31 |
| L16 · Estruturação de projeto: organização de código, notebooks versus… | 1.2 | 0,00 | +0,29 |
| L11 · Dívida técnica em ML: entanglement, undeclared consumers, pipeline… | 1.1 | 0,25 | +0,28 |
| L17 · Controle de versão de código com Git e boas práticas de branches,… | 1.2 | 0,25 | +0,22 |
| L21 · Gestão de hiperparâmetros: grid/random/Bayesian optimization e… | 1.2 | 0,25 | +0,22 |

**Nota final**

- Nota central: **7,5**.
- Intervalo plausível: 6,7 – 8,6, entre banca literal (R1) e banca viável (R3).
- Sensibilidade aos graus ambíguos (3 de 36 subitens): 7,4 – 7,7.
- Confiança: média-baixa.

**Risco de superestimação**

- Baixo.

**Risco de subestimação**

- Um texto agnóstico de ferramentas pode ser preferido por uma banca conceitual (cenário viável: 8,6). Amershi (2019) e Kreuzberger (2023) são referências atuais não pontuadas pelo DeepSeek neste ponto.

### Ponto 8 — MLOps: Automação, Implantação e Infraestrutura de Aprendizado de Máquina

Dissertação: `prova-escrita/8-mlops-automacao-implantacao-e-infraestrutura-de-aprendizado-de-maquina_v2.md` · Barema DeepSeek: `prova-escrita/barema-deepseek/ponto-8.note`

**Critérios oficiais e notas**

| Critério oficial | Máx. | Fonte | R1 literal | R2 central | R3 viável |
|---|---|---|---|---|---|
| 1.1 Domínio técnico/científico/crítico do ponto sorteado | 2,5 | DeepSeek (10 subitens) | 1,45 | 1,54 | 1,93 |
| 1.2 Abordagem das ideias fundamentais do conteúdo | 2,5 | DeepSeek (11 subitens) | 1,36 | 1,45 | 1,81 |
| 1.3 Organização, coerência, clareza e sequência lógica de ideias | 0,5 | Hipótese 95% | 0,475 | 0,475 | 0,475 |
| 1.4 Atualização do conteúdo / referências bibliográficas / normas técnicas | 1,0 | DeepSeek (9 subitens) | 0,33 | 0,59 | 0,74 |
| 1.5 Aprofundamento do conteúdo | 1,0 | DeepSeek (8 subitens) | 0,38 | 0,54 | 0,67 |
| 2.1 Uso adequado de terminologia técnico-científica | 1,0 | Hipótese 95% | 0,950 | 0,950 | 0,950 |
| 2.2 Estruturação coerente do texto com introdução, desenvolvimento e conclusão | 0,5 | Hipótese 95% | 0,475 | 0,475 | 0,475 |
| 2.3 Precisão e objetividade | 0,5 | Hipótese 95% | 0,475 | 0,475 | 0,475 |
| 2.4 Correção ortográfica e gramatical | 0,5 | Hipótese 95% | 0,475 | 0,475 | 0,475 |
| **Total** | **10,0** | | **6,36** | **6,97** | **8,00** |

**Evidências textuais relevantes**

- Delimitação "modelo validado ≠ sistema confiável" (L5–13).
- CI × CD × CT, com "CT não é retreinamento indiscriminado" e quality gates (L21–31).
- Artefato de implantação, containers e estratégias de release com rollback (L37–57).
- Inferência batch × online × streaming, latência ≠ throughput e training-serving skew (L62–78).
- Container × orquestração (L84–91); escala, balanceamento e escalabilidade ≠ disponibilidade (L95–115).
- Under/overprovisioning e degradação graciosa (L119–132).

**Critérios DeepSeek atendidos (grau 1): 6 de 38**

- 1.1 · L6 · Definição formal de automação de pipeline de ML e distinção entre CI, CD e…
- 1.1 · L7 · Distinção entre implantação batch, online (tempo real) e streaming; critérios…
- 1.2 · L22 · Infraestrutura em nuvem e escalabilidade: instâncias, autoscaling, GPUs e…
- 1.4 · L30 · Treveil et al., Introducing MLOps (2020)
- 1.4 · L31 · Kreuzberger, Kühl & Hirschl (2023), Machine Learning Operations (MLOps):…
- 1.4 · L33 · Breck et al. (2017), The ML Test Score

**Parcialmente atendidos: 20**

- 1.1 · L9 · Conteinerização e isolamento de dependências; imagens reprodutíveis e… — grau 0,75
- 1.1 · L10 · Orquestração de pipelines e agendamento de tarefas; dependências e paralelismo — grau 0,25
- 1.1 · L11 · Serving de modelos: APIs REST/gRPC, inferência em lote versus tempo real e… — grau 0,75
- 1.1 · L12 · Feature store: definição, consistência treino/serving e camadas online/offline — grau 0,25
- 1.1 · L13 · Análise crítica: custos, complexidade operacional, vendor lock-in, automação… — grau 0,75
- 1.1 · L14 · Distinção entre infraestrutura de ML e infraestrutura de software tradicional — grau 0,50
- 1.1 · L15 · Quando não automatizar: fase exploratória, baixa frequência de retreino e… (D) — grau 0,25
- 1.2 · L17 · CI/CD para ML: testes de código, dados e modelo; pipeline automatizado de… — grau 0,75
- 1.2 · L18 · Continuous Training (CT): gatilhos por novos dados, agendamento e drift… — grau 0,75
- 1.2 · L19 · Padrões de implantação: shadow, canário, blue-green e A/B testing — grau 0,75
- 1.2 · L20 · Empacotamento e serving: Docker, Kubernetes, KServe/Seldon e TorchServe/TF… — grau 0,50
- 1.2 · L21 · Orquestração de pipelines: Airflow, Kubeflow Pipelines e MLflow (fronteira… — grau 0,25
- 1.2 · L24 · Batch scoring e pipelines agendados para inferência em lote — grau 0,75
- 1.2 · L25 · API de inferência e contrato de entrada/saída; versionamento de endpoints — grau 0,75
- 1.4 · L32 · Humble & Farley, Continuous Delivery (2010) — grau 0,25
- 1.5 · L39 · Formalização de SLO/SLA de inferência: latência p95/p99, throughput e… — grau 0,25
- 1.5 · L40 · Trade-offs entre padrões de implantação: canário, blue-green e shadow; risco,… — grau 0,50
- 1.5 · L41 · Autoscaling e custo: cold start, scale-to-zero, utilização de GPU e… — grau 0,50
- 1.5 · L42 · Casos-limite: skew treino/serving, falha de feature store e indisponibilidade… — grau 0,75
- 1.5 · L43 · Trade-off entre serving online e batch: latência, custo e atualidade das… — grau 0,75

**Não atendidos: 12**

- 1.1 · L8 · Infraestrutura como código (IaC): declaração, idempotência, versionamento e…
- 1.2 · L23 · Feature store: Feast/Tecton e padrões de acesso online/offline
- 1.2 · L26 · IaC com Terraform e gestão declarativa de recursos
- 1.2 · L27 · Edge deployment e otimização de modelos (quantização, pruning) (D)
- 1.4 · L29 · Huyen, Designing Machine Learning Systems (2022)
- 1.4 · L34 · Documentação atual de Kubernetes, Docker e Terraform (verificar versões) [inexigível]
- 1.4 · L35 · Documentação atual de Kubeflow, Feast, KServe/Seldon e TorchServe/TF Serving… [inexigível]
- 1.4 · L36 · MLPerf Inference benchmark (verificar versão) [inexigível]
- 1.4 · L37 · Sato, Wider & Windheuser (2019), Continuous Delivery for Machine Learning… (D)
- 1.5 · L44 · Segurança e isolamento multi-tenant; supply chain de imagens e assinatura de… (D)
- 1.5 · L45 · Relação entre IaC e reprodutibilidade; detecção de drift de infraestrutura (D)
- 1.5 · L46 · Exemplo aplicado: pipeline CI/CD/CT com implantação canário e rollback… (D)

(D) = desejável no DeepSeek; [inexigível] = documentação/benchmark reclassificado (A.3); L = linha em `barema-deepseek/ponto-8.note`.

**Penalizações justificadas**

- IaC ausente (busca: 0), cobrada em 1.1, 1.2 e 1.5 (peso literal somado de 0,50).
- Feature store ausente, cobrada em 1.1, 1.2 e 1.5; o skew (L76) motiva o conceito sem nomeá-lo.
- A orquestração de pipelines (Airflow/Kubeflow) não aparece; a orquestração tratada é a de containers. Nenhuma ferramenta é nomeada (Docker, Kubernetes, KServe).
- Faltam SLO/percentis de latência, shadow deployment e A/B testing; Huyen (2022) não é citada.
- Avaliação técnica independente: Nenhum erro encontrado. A atribuição de "quality gates" a Breck et al. (ML Test Score) é razoável, mas indireta.

Maiores ganhos possíveis na leitura central (quanto a nota subiria se o subitem estivesse completo, respeitado o teto do item; inexigíveis excluídos):

| Subitem DeepSeek | Item | Grau atual | Ganho na nota |
|---|---|---|---|
| L29 · Huyen, Designing Machine Learning Systems (2022) | 1.4 | 0,00 | +0,27 |
| L8 · Infraestrutura como código (IaC): declaração, idempotência,… | 1.1 | 0,00 | +0,27 |
| L23 · Feature store: Feast/Tecton e padrões de acesso online/offline | 1.2 | 0,00 | +0,21 |
| L10 · Orquestração de pipelines e agendamento de tarefas; dependências e… | 1.1 | 0,25 | +0,20 |
| L12 · Feature store: definição, consistência treino/serving e camadas… | 1.1 | 0,25 | +0,20 |

**Nota final**

- Nota central: **7,0**.
- Intervalo plausível: 6,4 – 8,0, entre banca literal (R1) e banca viável (R3).
- Sensibilidade aos graus ambíguos (3 de 38 subitens): 7,0 – 7,2.
- Confiança: média.

**Risco de superestimação**

- Baixo.

**Risco de subestimação**

- Uma banca conceitual pode aceitar a ausência de ferramentas (cenário viável: 8,0). IaC e feature store, porém, são conceitos, não produtos, e devem ser cobrados.

### Ponto 9 — MLOps: Monitoramento, Governança e Manutenção de Modelos

Dissertação: `prova-escrita/9-mlops-monitoramento-governanca-e-manutencao-de-modelos_v2.md` · Barema DeepSeek: `prova-escrita/barema-deepseek/ponto-9.note`

**Critérios oficiais e notas**

| Critério oficial | Máx. | Fonte | R1 literal | R2 central | R3 viável |
|---|---|---|---|---|---|
| 1.1 Domínio técnico/científico/crítico do ponto sorteado | 2,5 | DeepSeek (10 subitens) | 2,00 | 2,22 | 2,50 |
| 1.2 Abordagem das ideias fundamentais do conteúdo | 2,5 | DeepSeek (10 subitens) | 1,89 | 1,89 | 2,36 |
| 1.3 Organização, coerência, clareza e sequência lógica de ideias | 0,5 | Hipótese 95% | 0,475 | 0,475 | 0,475 |
| 1.4 Atualização do conteúdo / referências bibliográficas / normas técnicas | 1,0 | DeepSeek (9 subitens) | 0,35 | 0,44 | 0,55 |
| 1.5 Aprofundamento do conteúdo | 1,0 | DeepSeek (9 subitens) | 0,65 | 0,93 | 1,00 |
| 2.1 Uso adequado de terminologia técnico-científica | 1,0 | Hipótese 95% | 0,950 | 0,950 | 0,950 |
| 2.2 Estruturação coerente do texto com introdução, desenvolvimento e conclusão | 0,5 | Hipótese 95% | 0,475 | 0,475 | 0,475 |
| 2.3 Precisão e objetividade | 0,5 | Hipótese 95% | 0,475 | 0,475 | 0,475 |
| 2.4 Correção ortográfica e gramatical | 0,5 | Hipótese 95% | 0,475 | 0,475 | 0,475 |
| **Total** | **10,0** | | **7,74** | **8,33** | **9,26** |

**Evidências textuais relevantes**

- Sistema disponível ≠ modelo correto, observabilidade e SLI/SLO (L19–31).
- Qualidade de dados × data drift × concept drift formalizados, com covariate shift (L37–58).
- Drift ≠ degradação nos dois sentidos e significância ≠ relevância (L60–64).
- Monitoramento com feedback delay, sensibilidade × estabilidade dos thresholds e segmentos (L68–74).
- Governança proporcional ao risco, lineage e trilha de auditoria (L78–88).
- Manutenção orientada por diagnóstico e champion–challenger (L92–106).

**Critérios DeepSeek atendidos (grau 1): 12 de 38**

- 1.1 · L6 · Definição formal de monitoramento de modelos e distinção de observabilidade…
- 1.1 · L9 · Métricas de desempenho em produção e problema do atraso de rótulos (label…
- 1.1 · L10 · Governança de ML: definição, papéis, accountability, políticas e gestão de…
- 1.1 · L14 · Quando não retreinar automaticamente: riscos de feedback loops, degradação… (D)
- 1.2 · L17 · Métricas operacionais: latência, throughput, taxa de erros, disponibilidade e…
- 1.2 · L20 · Monitoramento de performance: métricas de modelo, janelas, segmentação e…
- 1.2 · L25 · Manutenção: retreino agendado/por gatilho, rollback, aposentadoria e…
- 1.4 · L28 · Sculley et al. (2015), Hidden Technical Debt in Machine Learning Systems
- 1.4 · L29 · Breck et al. (2017), The ML Test Score
- 1.4 · L31 · Gama et al. (2014), A Survey on Concept Drift Adaptation
- 1.5 · L40 · Trade-offs de alertas: sensibilidade versus especificidade e custo de falsos…
- 1.5 · L43 · Manutenção: retreino automático versus manual; validação pós-retreino e…

**Parcialmente atendidos: 18**

- 1.1 · L7 · Distinção entre monitoramento de sistema, de modelo e de negócio — grau 0,75
- 1.1 · L8 · Data drift, concept drift, label drift e covariate shift: definições e… — grau 0,75
- 1.1 · L11 · Manutenção de modelos: tipos (corretiva, adaptativa e perfectiva) e gatilhos… — grau 0,75
- 1.1 · L12 · Análise crítica: falsos alarmes, drift sem degradação, métricas agregadas… — grau 0,75
- 1.1 · L13 · Distinção entre monitoramento offline e online e avaliação contínua em… — grau 0,50
- 1.2 · L18 · Monitoramento de dados: schema, estatísticas, valores ausentes, ranges e… — grau 0,75
- 1.2 · L19 · Detecção de drift: PSI, KS, Jensen-Shannon e testes estatísticos — grau 0,50
- 1.2 · L21 · Alertas: SLI/SLO, limiares, severidade, on-call e runbooks — grau 0,75
- 1.2 · L22 · Logging e auditoria: predições, entradas, versões, lineage e retenção — grau 0,75
- 1.2 · L23 · Governança: políticas, catálogo, model registry, aprovação, auditoria e… — grau 0,75
- 1.2 · L24 · Gestão de risco de modelo: inventário, classificação, revisão periódica e… — grau 0,75
- 1.2 · L26 · Feedback loop e coleta de rótulos em produção — grau 0,25
- 1.5 · L38 · Formalização de drift: mudança em P(X) versus mudança em P(y/X), com testes… — grau 0,75
- 1.5 · L39 · Label delay e avaliação retardada: estratégias de estimação e viés associado — grau 0,75
- 1.5 · L41 · Casos-limite: drift sem degradação, degradação sem drift, feedback loops e… — grau 0,75
- 1.5 · L42 · Governança: auditoria e rastreabilidade fim a fim; retenção e privacidade de… — grau 0,50
- 1.5 · L44 · Relação entre monitoramento e versionamento/linhagem (fronteira com o Ponto 7) (D) — grau 0,75
- 1.5 · L45 · Exemplo aplicado: monitoramento de modelo de crédito com PSI, performance e… (D) — grau 0,25

**Não atendidos: 8**

- 1.1 · L15 · Segurança e privacidade no monitoramento: PII em logs, anonimização e retenção (D)
- 1.4 · L30 · Huyen, Designing Machine Learning Systems (2022)
- 1.4 · L32 · Lu et al. (2018), Learning under Concept Drift: A Review (verificar) (D)
- 1.4 · L33 · NIST AI Risk Management Framework (AI RMF 1.0, 2023)
- 1.4 · L34 · ISO/IEC 42001:2023 — AI management system
- 1.4 · L35 · LGPD (Lei 13.709/2018) e GDPR (Regulamento UE 2016/679)
- 1.4 · L36 · Documentação atual de Evidently AI, WhyLabs, Prometheus/Grafana e MLflow… [inexigível]
- 1.5 · L46 · Riscos adversariais e envenenamento de dados em produção (data poisoning) (D)

(D) = desejável no DeepSeek; [inexigível] = documentação/benchmark reclassificado (A.3); L = linha em `barema-deepseek/ponto-9.note`.

**Penalizações justificadas**

- Detecção de drift só por "testes ou medidas de distância" (L64), sem PSI, KS ou Jensen-Shannon.
- Faltam feedback loops, coleta de rótulos e label drift; privacidade/retenção também ausentes.
- Item 1.4 = 0,44: nenhum marco normativo (NIST AI RMF, ISO/IEC 42001, LGPD), apesar de 1.4 nomear "normas técnicas"; Huyen não é citada.
- Avaliação técnica independente: Nenhum erro encontrado. As definições de covariate shift e concept drift estão corretas.

Maiores ganhos possíveis na leitura central (quanto a nota subiria se o subitem estivesse completo, respeitado o teto do item; inexigíveis excluídos):

| Subitem DeepSeek | Item | Grau atual | Ganho na nota |
|---|---|---|---|
| L30 · Huyen, Designing Machine Learning Systems (2022) | 1.4 | 0,00 | +0,19 |
| L19 · Detecção de drift: PSI, KS, Jensen-Shannon e testes estatísticos | 1.2 | 0,50 | +0,15 |
| L26 · Feedback loop e coleta de rótulos em produção | 1.2 | 0,25 | +0,15 |
| L32 · Lu et al. (2018), Learning under Concept Drift: A Review (verificar) (D) | 1.4 | 0,00 | +0,12 |
| L33 · NIST AI Risk Management Framework (AI RMF 1.0, 2023) | 1.4 | 0,00 | +0,12 |

**Nota final**

- Nota central: **8,3**.
- Intervalo plausível: 7,7 – 9,3, entre banca literal (R1) e banca viável (R3).
- Sensibilidade aos graus ambíguos (7 de 38 subitens): 8,1 – 8,6.
- Confiança: média.

**Risco de superestimação**

- Os graus 1 em governança (L10) e 0,75 em drift (L8) são do lado generoso.

**Risco de subestimação**

- Baixo a moderado: a precisão conceitual é alta.

### Ponto 10 — XAI: Métodos, Interpretabilidade, Avaliação e Uso das Explicações

Dissertação: `prova-escrita/10-xai-metodos-interpretabilidade-avaliacao-e-uso-das-explicacoes_v2.md` · Barema DeepSeek: `prova-escrita/barema-deepseek/ponto-10.note`

**Critérios oficiais e notas**

| Critério oficial | Máx. | Fonte | R1 literal | R2 central | R3 viável |
|---|---|---|---|---|---|
| 1.1 Domínio técnico/científico/crítico do ponto sorteado | 2,5 | DeepSeek (10 subitens) | 1,93 | 2,50 | 2,50 |
| 1.2 Abordagem das ideias fundamentais do conteúdo | 2,5 | DeepSeek (10 subitens) | 1,61 | 2,30 | 2,50 |
| 1.3 Organização, coerência, clareza e sequência lógica de ideias | 0,5 | Hipótese 95% | 0,475 | 0,475 | 0,475 |
| 1.4 Atualização do conteúdo / referências bibliográficas / normas técnicas | 1,0 | DeepSeek (10 subitens) | 0,50 | 0,71 | 0,89 |
| 1.5 Aprofundamento do conteúdo | 1,0 | DeepSeek (8 subitens) | 0,62 | 0,83 | 1,00 |
| 2.1 Uso adequado de terminologia técnico-científica | 1,0 | Hipótese 95% | 0,950 | 0,950 | 0,950 |
| 2.2 Estruturação coerente do texto com introdução, desenvolvimento e conclusão | 0,5 | Hipótese 95% | 0,475 | 0,475 | 0,475 |
| 2.3 Precisão e objetividade | 0,5 | Hipótese 95% | 0,475 | 0,475 | 0,475 |
| 2.4 Correção ortográfica e gramatical | 0,5 | Hipótese 95% | 0,475 | 0,475 | 0,475 |
| **Total** | **10,0** | | **7,51** | **9,20** | **9,74** |

**Evidências textuais relevantes**

- Objetivo de XAI e intrínseco × post hoc (L5–15); quatro perguntas organizadoras (L19–24).
- Local × global e specific × agnostic (L28–30); importância ≠ efeito causal (L34–35).
- SHAP aditivo, permutation importance com fórmula e ressalva de correlação, Integrated Gradients (L44–62).
- Surrogate e LIME, exemplos e contrafactual formalizado (L66–78); mapa família → pergunta (L80–83).
- Critérios de avaliação e tipos de avaliação (L87–99); usos e confiança calibrada (L103–111).
- Limitações: modelo ≠ fenômeno, E₁ ≠ E₂, racionalização e preferência por modelos interpretáveis (L115–131).

**Critérios DeepSeek atendidos (grau 1): 13 de 38**

- 1.1 · L7 · Distinção entre explicações globais e locais; model-specific ×…
- 1.1 · L8 · Definição de fidelidade (faithfulness), estabilidade, robustez e…
- 1.1 · L11 · Adequação da explicação ao público-alvo: desenvolvedores, usuários finais,…
- 1.1 · L13 · Distinção entre explicabilidade e causalidade; explicações preditivas não… (D)
- 1.2 · L19 · LIME: perturbações locais, modelo substituto e escopo de aplicação
- 1.2 · L21 · Gradientes de saliência e Integrated Gradients para entradas contínuas e…
- 1.4 · L28 · Ribeiro, Singh & Guestrin (2016), "Why Should I Trust You?": Explaining the…
- 1.4 · L29 · Lundberg & Lee (2017), A Unified Approach to Interpreting Model Predictions…
- 1.4 · L30 · Sundararajan, Taly & Yan (2017), Axiomatic Attribution for Deep Networks…
- 1.4 · L32 · Molnar, Interpretable Machine Learning (2ª ed., 2022) (verificar)
- 1.5 · L42 · Casos-limite: explicadores instáveis, dependência entre features,…
- 1.5 · L43 · Avaliação de explicações: métricas funcionais (fidelidade, estabilidade) e…
- 1.5 · L44 · Relação entre explicabilidade e causalidade; explicações preditivas × causais (D)

**Parcialmente atendidos: 18**

- 1.1 · L6 · Definição formal de interpretabilidade, explicabilidade e transparência;… — grau 0,75
- 1.1 · L9 · Pressupostos e limites: explicações como aproximações, multiplicidade de… — grau 0,75
- 1.1 · L10 · Análise crítica do trade-off entre desempenho preditivo e interpretabilidade;… — grau 0,75
- 1.1 · L12 · Quando não usar XAI: explicação não acionável, risco de confiança excessiva e… — grau 0,75
- 1.1 · L15 · Crítica à XAI como substituto de governança, validação humana e controle… (D) — grau 0,50
- 1.2 · L17 · Modelos intrinsecamente interpretáveis: regressão linear/logística, árvores… — grau 0,75
- 1.2 · L18 · Importância de features: permutation importance, PDP/ICE e suas limitações — grau 0,75
- 1.2 · L20 · SHAP: valores de Shapley, propriedades (eficiência, simetria, dummy,… — grau 0,50
- 1.2 · L22 · Explicações contrafactuais e âncoras (anchors): definição, geração e uso — grau 0,75
- 1.2 · L23 · Explicações baseadas em exemplos/protótipos e k-NN explicável (D) — grau 0,50
- 1.2 · L24 · Surrogate models globais (árvore substituta) e regras de decisão (D) — grau 0,75
- 1.4 · L31 · Wachter, Mittelstadt & Russell (2017), Counterfactual Explanations Without… — grau 0,25
- 1.4 · L33 · Doshi-Velez & Kim (2017), Towards A Rigorous Science of Interpretable Machine… — grau 0,25
- 1.4 · L34 · Rudin (2019), Stop Explaining Black Box Machine Learning Models for High… — grau 0,25
- 1.4 · L36 · Documentação atual de SHAP, LIME, InterpretML, Captum e Alibi (verificar… (D) [inexigível] — grau 0,25
- 1.5 · L39 · Formalização dos valores de Shapley e das propriedades de eficiência,… — grau 0,25
- 1.5 · L40 · Formalização de fidelidade: correlação entre importância atribuída e mudança… — grau 0,50
- 1.5 · L41 · Trade-offs: fidelidade × compreensibilidade, estabilidade × sensibilidade e… — grau 0,75

**Não atendidos: 7**

- 1.1 · L14 · Limitações de explicabilidade em modelos de alta dimensionalidade e dados não… (D)
- 1.2 · L25 · Visualizações de explicabilidade: heatmaps, SHAP force plots, PDP/ICE (D)
- 1.2 · L26 · Explicações baseadas em atenção em modelos de linguagem/visão e suas… (D)
- 1.4 · L35 · Miller (2019), Explanation in Artificial Intelligence: Insights from the… (D)
- 1.4 · L37 · LGPD (Lei 13.709/2018) e GDPR: direito à explicação (fronteira com o Ponto 9) (D)
- 1.5 · L45 · Exemplo aplicado: explicação local com SHAP/LIME para decisão de crédito e… (D)
- 1.5 · L46 · Limitações em modelos de linguagem e imagens: risco de explicações… (D)

(D) = desejável no DeepSeek; [inexigível] = documentação/benchmark reclassificado (A.3); L = linha em `barema-deepseek/ponto-10.note`.

**Penalizações justificadas**

- SHAP sem valores de Shapley e sem axiomas (eficiência, simetria, dummy), o que afeta 1.2 e 1.5.
- PDP/ICE, anchors e GAMs ausentes.
- Dados não estruturados e atenção ausentes; ambos são desejáveis no DeepSeek.
- Formulações de Wachter, Doshi-Velez & Kim e Rudin aparecem sem citação (1.4).
- Avaliação técnica independente: Nenhum erro encontrado. A taxonomia funcional/humana/aplicação (L99) é de Doshi-Velez & Kim e está atribuída a Molnar [1], que a reproduz; aceitável, mas citar a origem seria melhor.

Maiores ganhos possíveis na leitura central (quanto a nota subiria se o subitem estivesse completo, respeitado o teto do item; inexigíveis excluídos):

| Subitem DeepSeek | Item | Grau atual | Ganho na nota |
|---|---|---|---|
| L20 · SHAP: valores de Shapley, propriedades (eficiência, simetria, dummy,… | 1.2 | 0,50 | +0,20 |
| L25 · Visualizações de explicabilidade: heatmaps, SHAP force plots, PDP/ICE (D) | 1.2 | 0,00 | +0,20 |
| L26 · Explicações baseadas em atenção em modelos de linguagem/visão e suas… (D) | 1.2 | 0,00 | +0,20 |
| L39 · Formalização dos valores de Shapley e das propriedades de eficiência,… | 1.5 | 0,25 | +0,15 |
| L23 · Explicações baseadas em exemplos/protótipos e k-NN explicável (D) | 1.2 | 0,50 | +0,14 |

**Nota final**

- Nota central: **9,2**.
- Intervalo plausível: 7,5 – 9,7, entre banca literal (R1) e banca viável (R3).
- Sensibilidade aos graus ambíguos (3 de 38 subitens): 9,2 – 9,2.
- Confiança: média-baixa.

**Risco de superestimação**

- Na leitura calibrada, os desejáveis compensam lacunas e o item 1.1 atinge o teto. Uma banca que exija axiomas de Shapley pode descontar, e a leitura literal dá 7,5.

**Risco de subestimação**

- Pouca margem: o teto possível é 9,85.

## D. Síntese comparativa

### D.1 Ordenação pela nota central

| Posição | Ponto | Central | Intervalo | R1 < 7,00? |
|---|---|---|---|---|
| 1 | 10 | 9,2 | 7,5 – 9,7 | não |
| 2 | 3 | 8,5 | 7,7 – 9,2 | não |
| 3 | 9 | 8,3 | 7,7 – 9,3 | não |
| 4 | 2 | 8,3 | 7,2 – 9,1 | não |
| 5 | 6 | 7,8 | 7,2 – 8,6 | não |
| 6 | 7 | 7,5 | 6,7 – 8,6 | sim |
| 7 | 4 | 7,4 | 6,6 – 8,3 | sim |
| 8 | 1 | 7,1 | 6,3 – 8,2 | sim |
| 9 | 8 | 7,0 | 6,4 – 8,0 | sim |
| 10 | 5 | 7,0 | 6,5 – 7,5 | sim |

**Pontos mais fortes**

- **Ponto 10 (9,2):** a cobertura dos essenciais é a mais alta (78%) e nenhum essencial está ausente.
- **Pontos 3, 2 e 9 (8,3–8,5):** núcleo técnico completo e seções críticas fortes; perdem sobretudo em ferramentas e referências.

**Pontos mais frágeis**

- **Pontos 5 e 8 (7,0):** no 5, os algoritmos estão em uma linha cada; no 8, faltam IaC e feature store e nenhuma ferramenta é nomeada.
- **Ponto 1 (7,1):** faltam transações distribuídas; é também o ponto com mais graus ambíguos.
- **Pontos 4 (7,4) e 7 (7,5):** no 4, EDA e métodos de anomalia ficam só nomeados; no 7, falta a camada prática e a dívida técnica.

### D.2 Critérios responsáveis pelas maiores perdas

| Critério | Máx. | Média R2 (10 pontos) | % do máximo | Perda média | Pior ponto |
|---|---|---|---|---|---|
| 1.1 | 2,5 | 2,16 | 86% | 0,34 | P8 (1,54) |
| 1.2 | 2,5 | 1,56 | 62% | 0,94 | P5 (0,88) |
| 1.4 | 1,0 | 0,59 | 59% | 0,41 | P7 (0,41) |
| 1.5 | 1,0 | 0,65 | 65% | 0,35 | P6 (0,27) |

Leitura da tabela:

- **1.2 (ideias fundamentais):** maior perda absoluta. Os textos privilegiam síntese conceitual e omitem algoritmos, arquiteturas e ferramentas que o DeepSeek trata como essenciais.
- **1.4 (atualização/referências):** maior perda relativa. Os textos citam 4–5 obras canônicas; o DeepSeek lista 8 a 10 itens por ponto, incluindo documentação. Só quatro obras são posteriores a 2018 (Amershi 2019, Kreuzberger 2023 em três pontos, Molnar 2022), e não há normas técnicas (relevante no Ponto 9).
- **1.5 (aprofundamento):** concentra as perdas dos Pontos 4, 5 e 6.

### D.3 Repetição temática no DeepSeek

O mesmo tema costuma aparecer em 1.1, 1.2 e 1.5. Uma única omissão, portanto, custa várias vezes:

| Ponto | Tema omitido ou só mencionado | Peso literal somado |
|---|---|---|
| 1 | Transações/NewSQL/MVCC (L10, L19, L23, L40) | 0,90 |
| 8 | IaC (L8, L26, L45) | 0,50 |
| 8 | Feature store (L12, L23; parte de L42) | 0,45 + parte de 0,15 |
| 6 | DQN/Monte Carlo/PPO (L20, L24, L35, L42, L45, L46) | 0,90 |

Não é dupla contagem formal (os pesos somam o máximo oficial), mas concentra a penalidade. Uma banca real tende a descontar uma vez por tema.

### D.4 Discrepâncias entre o rigor DeepSeek e a exigência oficial

1. **Item 1.1:** o oficial avalia "domínio técnico/científico/crítico" (qualidade). O DeepSeek o transforma em checklist de cobertura, o que penaliza textos precisos mas compactos.
2. **Item 1.4:** o DeepSeek pede obras específicas e documentação de software com versão, inviável de memória (tratada em A.3). Também não credita citações canônicas fora da sua lista (Herlihy & Wing, Gilbert & Lynch, Amdahl, Gustafson, Goodfellow, Amershi).
3. **1.3 e Item II:** nenhum subitem DeepSeek cobre esses 3,0 pontos (30% da nota); aqui entram pela hipótese dos 95%.
4. **Ponto 6:** a profundidade formal (Bellman, TD, Q-learning) é creditada em 1.1/1.2, enquanto 1.5 exige teoria de convergência ausente. Uma banca pode contar essas formalizações como aprofundamento.
5. **Ponto 7:** os pesos são internamente inconsistentes (normalizados).
6. **Limite de extensão:** o conjunto completo de essenciais de cada ponto supera em muito o que cabe em ~80 minutos manuscritos. A leitura R3 existe para dimensionar esse efeito.

### D.5 Incertezas importantes

- **Rigor da banca:** é a maior fonte de incerteza. R1 e R3 diferem de 1,0 a 2,2 pontos, conforme o ponto.
- **Hipótese dos 95%:** se a redação manuscrita obtiver 85% em vez de 95% nos 3,0 pontos, todas as notas caem 0,3.
- **Agregação dos três pontos:** a ficha tem um único "1.1 ... do ponto sorteado" para três pontos e nenhuma regra de agregação (Relatório 3).
- **Reprodução sob tempo:** um ponto incompleto não só perde pontos; pode eliminar (edital 16.8).

