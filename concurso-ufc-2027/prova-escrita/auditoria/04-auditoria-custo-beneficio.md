# Auditoria 2 — Perfeição acadêmica versus desempenho real na prova

Data: 03/11/2026. Prova escrita: 08/11/2026. Escopo: as dez dissertações `prova-escrita/<N>-*_v2.md`, avaliadas pela Ficha de Avaliação – Prova Escrita Subjetiva (`edital/barema-quixada.md`), com os baremas DeepSeek (`prova-escrita/barema-deepseek/ponto-<N>.note`) e os relatórios 01–03 como instrumentos auxiliares.

Relatórios irmãos: [05-prioridades-globais.md](05-prioridades-globais.md) (ordem global) e [06-plano-minimo-de-revisao.md](06-plano-minimo-de-revisao.md) (checklist executável).

## Resposta direta

As menores alterações com maior probabilidade de elevar a nota, sem comprometer os 80 minutos, são:

1. **Medir a própria velocidade manuscrita antes de mudar qualquer texto.** Com 12 palavras/min, nove dos dez textos atuais já passam do orçamento de escrita (~70 min); com 15, todos cabem, e o Ponto 6 fica no limite.
2. **Três inserções essenciais**, cada uma preenchendo uma lacuna conceitual de primeira ordem: transações distribuídas e 2PC (P1-A), conteúdo operacional da EDA (P4-A) e infraestrutura como código (P8-A).
3. **Enxugar o Ponto 6** (P6-A): retirar duas fórmulas e quadros redundantes. O tempo liberado paga duas frases que faltam ao RL moderno (P6-B: deadly triad/DQN; P6-C: Monte Carlo × TD).
4. **Correções e microinserções de custo quase nulo:** o "três perguntas" do Dataflow (P3-A), nomes de testes de drift (P9-B), um método por família de anomalia (P4-B), ferramentas canônicas nos Pontos 7 e 8 (P7-B, P8-C).
5. **Substituições que trocam linhas genéricas por mecanismos**, pagas por cortes: Ponto 5 (ERM/L1/L2, bagging × boosting, k-means), Spark/RDD no Ponto 2, Shapley no Ponto 10. No Ponto 9, uma frase normativa (NIST AI RMF, ISO/IEC 42001, LGPD), único lugar onde a palavra "normas" do critério 1.4 tem aplicação natural.

**Já suficientemente bons:** Pontos 3 e 10 (fechados após microajustes); Pontos 2 e 9 quase fechados.

**Erros técnicos:** nenhum erro conceitual grave nos dez textos. Há uma imprecisão de atribuição (P3, Dataflow) e seis imprecisões menores corrigíveis com custo zero.

**ABNT:** nenhuma das 41 referências atuais está na norma. Faltam títulos, há "et al." para dois ou três autores, sobrenomes em minúsculas nos Pontos 4–10 e chamadas entre colchetes. A correção de custo zero está na seção 11; a forma completa, no Apêndice B.

## 0. Método

### 0.1 Fontes e verificações

- **Lidos na íntegra:** as dez dissertações `_v2.md`, os dez baremas DeepSeek, a ficha oficial (só a seção da prova escrita) e os relatórios 01–03.
- **Conferidos no edital:** duração de 4 h (16.1), caderno de 30 folhas (16.2), eliminação por ponto não desenvolvido "total ou parcialmente" (16.8) e proibição de consulta (15.15; Res. 15/CEPE, art. 20, § 6º).
- **`.docx` × `.md`:** os `.docx` dos Pontos 6 e 7, modificados depois dos `.md`, têm o mesmo texto; diferem só na formatação das fórmulas (comparação palavra a palavra).
- **Trechos citados:** todos os trechos que as propostas substituem ou removem foram verificados por script; cada um existe exatamente uma vez no arquivo correspondente.
- **Referências bibliográficas sugeridas:** conferidas por busca na web quando havia dúvida de edição ou ano (DDIA 2. ed. de 2026, Han–Pei–Tong 4. ed. de 2022, Özsu–Valduriez 4. ed. de 2020, Molnar 3. ed. de 2025, Bishop & Bishop de 2024, Krishna et al. na TMLR de 2024). As regras da NBR 10520:2023 vieram de manuais de bibliotecas universitárias; o texto da norma não foi consultado diretamente.
- **Arquivos-fonte:** nenhum foi alterado.

### 0.2 Classificação das alterações

| Classe | Critério usado |
|---|---|
| ESSENCIAL | A omissão compromete uma ideia fundamental do título do ponto (critérios 1.1/1.2), independentemente do DeepSeek, ou impede concluir o ponto no tempo. |
| ALTO CUSTO-BENEFÍCIO | Inserção ou substituição curta (em geral ≤ 45 palavras) que resolve lacuna relevante com baixo risco e baixa memorização. |
| OPCIONAL | Melhoria legítima, de ganho pequeno ou incerto diante do tempo; documentada, mas fora da execução. |
| DESNECESSÁRIO | Detalhe especializado ou redundante. |
| CONTRAPRODUCENTE | Alongaria o texto, aumentaria o risco de erro ou deslocaria conteúdo central. |

Limite: no máximo três alterações prioritárias por ponto. Microajustes de custo ~0 (troca de 2–6 palavras) ficam listados à parte e não contam no limite.

### 0.3 Como o ganho foi estimado

- **Primário (qualitativo):** relação da alteração com os critérios oficiais 1.1–1.5, classificada como alto, moderado, baixo ou incerto, com justificativa.
- **Indicador secundário:** o mesmo modelo da Auditoria 1 (subitens DeepSeek, leitura central R2), recalculado com os graus que cada alteração passaria a merecer.
  - Ele mede o **teto do instrumento DeepSeek**, que converte cobertura em pontos de forma mecânica; o ganho oficial tende a ser menor.
  - No item 1.4, cada referência listada pesa muito no modelo; trate esse componente com cautela.
  - Nenhum aumento é atribuído sem esse vínculo explícito.

### 0.4 Modelo de tempo manuscrito (hipóteses de trabalho)

| Parâmetro | Lenta | Moderada | Rápida |
|---|---|---|---|
| Prosa reproduzida de memória | 12 pal/min | 15 pal/min | 18 pal/min |
| Símbolo matemático em fórmula | 2,25 s | 1,8 s | 1,44 s |
| Diagrama/quadro | palavras e setas ×1,2 + 3 s por linha | idem | idem |

- **Hipóteses, não medidas:** as velocidades acima não vêm de medição do candidato; por isso o primeiro item do plano é medir a velocidade real (relatório 06, seção 0).
- **Custos extras:** cada fórmula exibida custa mais 9 s (arranjo na página e lembrança); as referências contam como prosa.
- **Orçamento de escrita:** ~70 min por ponto = 80 − 3 (esqueleto) − 5 (revisão) − 2 (folga e fadiga).
- **Fadiga:** 4 h de escrita contínua tendem a reduzir a velocidade no terceiro ponto; isso reforça usar a margem do cenário moderado como alvo.

### 0.5 Factibilidade: visão geral

| Ponto | Palavras (prosa + diagramas) | Fórmulas exibidas | Diagramas/quadros | Atual L / M / R (min) | Com plano FAZER L / M / R | Risco atual (M / L) | Risco com plano (M / L) |
|---|---|---|---|---|---|---|---|
| 1 | 780 | 1 | 1 | 69,7 / 55,9 / 46,6 | 80,2 / 64,2 / 53,6 | baixo / alto | médio / **não cabe** |
| 2 | 821 | 3 | 2 | 75,6 / 60,6 / 50,6 | 78,8 / 63,2 / 52,7 | baixo / **não cabe** | médio / **não cabe** |
| 3 | 823 | 2 | 2 | 75,0 / 60,1 / 50,1 | 76,4 / 61,3 / 51,1 | baixo / **muito alto** (só com revisão encurtada) | baixo / **não cabe** |
| 4 | 813 | 3 | 6 | 77,2 / 62,0 / 51,7 | 82,5 / 66,2 / 55,2 | baixo / **não cabe** | médio / **não cabe** |
| 5 | 827 | 2 | 6 | 79,0 / 63,4 / 52,9 | 81,7 / 65,6 / 54,7 | médio / **não cabe** | médio / **não cabe** |
| 6 | 797 | 11 | 5 | 87,3 / 69,9 / 58,0 | 84,5 / 67,7 / 56,1 | alto / **não cabe** | alto / **não cabe** |
| 7 | 790 | 1 | 9 | 74,5 / 59,9 / 50,1 | 79,2 / 63,6 / 53,2 | baixo / **muito alto** (só com revisão encurtada) | médio / **não cabe** |
| 8 | 786 | 0 | 10 | 73,4 / 59,0 / 49,4 | 80,1 / 64,3 / 53,9 | baixo / **muito alto** (só com revisão encurtada) | médio / **não cabe** |
| 9 | 848 | 2 | 8 | 80,6 / 64,7 / 54,0 | 83,8 / 67,3 / 56,2 | médio / **não cabe** | alto / **não cabe** |
| 10 | 845 | 3 | 5 | 80,1 / 64,2 / 53,5 | 84,1 / 67,4 / 56,2 | médio / **não cabe** | alto / **não cabe** |

**Leitura:**

- **Moderada (15 pal/min):** todos os textos cabem, antes e depois do plano. O Ponto 6 atual (≈70 min) é o único sem folga; o plano o reduz a ≈68 min.
- **Lenta (12 pal/min):** os textos atuais já ultrapassam o orçamento em 3–17 min, exceto o Ponto 1. Nesse cenário, nenhuma inserção deve entrar sem corte equivalente; vale o "cenário lento mínimo" de cada ponto (itens 8) e a regra de decisão do relatório 06.
- **Rápida (18 pal/min):** sobra folga de 12 min ou mais em todos os pontos, mesmo com o plano.
- **Espaço físico:** não é restrição. ≈ 950 palavras × 3 pontos cabem com folga em um caderno de 30 folhas.

## 1. Ponto 1 — Processamento de Dados em Larga Escala: Armazenamento e Gerenciamento Distribuído de Dados

Dissertação: `prova-escrita/1-pdle-armazenamento-e-gerenciamento-distribuido-de-dados_v2.md` · Barema DeepSeek: `prova-escrita/barema-deepseek/ponto-1.note`

### 1.1 Diagnóstico global

Texto sólido, conceitualmente correto e bem encadeado (particionamento → replicação → consistência → arquiteturas → trade-offs). A crítica ao CAP e a ressalva sobre R + W > N mostram domínio fino. A lacuna real é de **gerenciamento**: transações distribuídas não aparecem. As arquiteturas citadas (GFS, Dynamo, Bigtable) servem de rótulos históricos, sem mecanismo. É o texto mais curto dos dez e tem folga para uma inserção de porte médio.

| Pergunta | Resposta |
|---|---|
| Tese ou objetivo central | Armazenamento distribuído é a combinação deliberada de particionamento e replicação, sob um modelo de consistência e mecanismos de recuperação, guiada pelas invariantes do workload (L85, L105). |
| Fundamentos apresentados? | Sim: escalabilidade vertical × horizontal, falhas parciais, abstração lógica sobre distribuição física, particionamento × replicação (L5–22). |
| O núcleo responde ao tema? | Responde a "armazenamento" de forma completa. "Gerenciamento" fica incompleto: sem transações/atomicidade multi-partição. |
| Sequência lógica? | Sim: partição → replicação → consistência/quóruns → arquiteturas → trade-offs → conclusão. |
| Erros técnicos relevantes? | Nenhum (ver item 7). |
| Redundância? | Baixa: a L83 repete a L85; a L15 antecipa a seção 1.4. |
| Aprofundamento compatível? | Sim em CAP, quórum, split-brain e códigos de apagamento; raso nas arquiteturas (uma frase cada). |
| Exemplos ajudam? | GFS, Dynamo e Bigtable são âncoras corretas, mas só nomeadas; o GFS poderia mostrar seu mecanismo (P1-C, opcional). |

### 1.2 Nota anteriormente estimada

- **Auditoria 1:** central **7,1**, intervalo 6,3–8,2.
- **Indicador após as alterações FAZER** (mesmo modelo da Auditoria 1; teto do instrumento, não previsão): central 7,11 → **8,27**; leitura literal (R1) 6,26 → 7,11; viável (R3) 8,17 → 9,24.
- O modelo converte cobertura em pontos de forma mecânica. A direção do efeito é mais confiável que a magnitude, e o ganho oficial tende a ser menor.

### 1.3 Adequação ao barema oficial

| Critério oficial | Avaliação |
|---|---|
| 1.1 | Bom: CAP com crítica correta, quórum com ressalva, split-brain. Perde por omitir transações. |
| 1.2 | Lacuna principal: gerenciamento transacional; arquiteturas só nomeadas. |
| 1.3 / 2.2 | Estrutura exemplar (introdução, fundamentos, núcleo, limitações, conclusão). |
| 1.4 | Referências canônicas, todas de 1990–2007; formatação fora da ABNT (seção 11). |
| 1.5 | Bom: quórum, split-brain, códigos de apagamento. |
| 2.1 / 2.3 / 2.4 | Terminologia precisa; nenhuma falha de redação relevante. |

### 1.4 Principais exigências do DeepSeek atendidas

5 de 33 subitens atendidos integralmente ou de forma equivalente. As seções 1.4, 1.5 e 1.6 juntas classificam todos os 33 subitens.

- 1.1 · L6 · Definição formal de sistema de armazenamento distribuído e propriedades de particionamento, replicação e tole…
- 1.1 · L11 · Particionamento/sharding: hash, range, consistência e hotspots
- 1.2 · L21 · Estratégias de particionamento e rebalanceamento
- 1.2 · L22 · Estratégias de replicação e recuperação de falhas
- 1.4 · L27 · Bigtable (Chang et al., 2006) e Dynamo (DeCandia et al., 2007)

### 1.5 Exigências parcialmente atendidas ou ausentes

"Efeito oficial" é o efeito provável da omissão na ficha da UFC, não no DeepSeek.

| L | Item | Exigência DeepSeek | Situação | Efeito oficial provável | Decisão |
|---|---|---|---|---|---|
| 7 | 1.1 | Distinção entre armazenamento em bloco, arquivo e objeto, com critérios de esco… | Parcial (0,50) | baixo | Não fazer |
| 8 | 1.1 | Modelos de consistência: forte, eventual, causal e leituras/escritas monotônicas | Parcial (0,75) | baixo | Não fazer |
| 9 | 1.1 | Teorema CAP e PACELC: interpretação correta e crítica a leituras simplistas | Parcial (0,75) | moderado | Fazer (P1-B) |
| 10 | 1.1 | Transações distribuídas: ACID, 2PC e limitações; BASE como contraponto | Ausente | alto | Fazer (P1-A) |
| 12 | 1.1 | Replicação: líder-seguidor, multi-líder, sem líder; quóruns e consistência | Parcial (0,75) | baixo | Não fazer |
| 14 | 1.1 | Análise crítica: quando não usar NoSQL/eventual; custos de consistência, latênc… | Parcial (0,75) | baixo | Não fazer |
| 16 | 1.2 | Arquitetura de DFS: namenode/datanodes, blocos, replicação e rack awareness (GF… | Parcial (0,25) | baixo a moderado | Se houver tempo (P1-C) |
| 17 | 1.2 | Object storage: buckets, objetos, metadados, durabilidade e consistência (model… | Parcial (0,25) | baixo | Não fazer |
| 18 | 1.2 | Key-value e wide-column stores: Bigtable/HBase, Dynamo/Cassandra e modelos de d… | Parcial (0,50) | baixo | Não fazer |
| 19 | 1.2 | Bancos relacionais distribuídos/NewSQL: sharding, replicação e transações distr… | Ausente | alto | Fazer (P1-A) |
| 23 | 1.2 | Consistência e versionamento: MVCC, snapshots e timestamps | Ausente | baixo a moderado | Opcional (P1-O1) |
| 24 | 1.2 | Gerenciamento de metadados e catálogo | Parcial (0,25) | baixo | Não fazer |
| 26 | 1.4 | GFS (Ghemawat et al., 2003) e HDFS como referências clássicas | Parcial (0,75) | baixo a moderado | Se houver tempo (P1-C) |
| 28 | 1.4 | Kleppmann, Designing Data-Intensive Applications (2017) | Ausente | baixo a moderado | Fazer (P1-A) |
| 29 | 1.4 | Abadi (2012), consistency tradeoffs e PACELC | Ausente | baixo a moderado | Fazer (P1-B) |
| 32 | 1.4 | Özsu & Valduriez, Principles of Distributed Database Systems (verificar edição/… | Ausente | baixo | Não fazer |
| 35 | 1.5 | Formalização de quórum R + W > N e trade-offs entre latência e consistência | Parcial (0,75) | baixo | Não fazer |
| 36 | 1.5 | CAP/PACELC com análise de latência e partição em cenários concretos | Parcial (0,50) | moderado | Fazer (P1-B) |
| 37 | 1.5 | Complexidade e custos de replicação: fan-out, largura de banda e latência de co… | Parcial (0,50) | baixo | Não fazer |
| 38 | 1.5 | Hotspots e skew em sharding; técnicas de salting e rebalanceamento | Parcial (0,75) | baixo | Não fazer |
| 39 | 1.5 | Casos-limite: falha de coordenador, split-brain, stale reads e perda de quórum | Parcial (0,50) | moderado | Fazer (P1-A) |
| 40 | 1.5 | Relação entre MVCC, snapshots e isolamento; anomalias de concorrência | Ausente | baixo a moderado | Opcional (P1-O1) |

### 1.6 Exigências do DeepSeek consideradas excessivas ou pouco pertinentes

- L13 (1.1) · Consenso e coordenação: Paxos/Raft, leader election, relógios lógicos e vector… — Paxos/Raft e relógios vetoriais em detalhe: o texto já menciona consenso; detalhar desloca o foco.
- L20 (1.2) · Data lake e tabelas abertas: Parquet/ORC, catálogo e layout por partições (fron… — Formatos abertos de tabela: fronteira com o Ponto 3.
- L30 (1.4) · Documentação técnica atual de Apache Hadoop/HDFS, Apache Cassandra, Apache HBas… — Documentação com versão: inexigível sem consulta.
- L31 (1.4) · Parquet/ORC e catálogos (Apache Hive Metastore, Apache Iceberg) (fronteira com… — Parquet/ORC e catálogos: fronteira com o Ponto 3.
- L33 (1.4) · YCSB (Yahoo! Cloud Serving Benchmark) para avaliação de armazenamentos distribu… — Benchmark: inexigível sem consulta.
- L41 (1.5) · Exemplo aplicado: modelagem de armazenamento para sessões/telemetria com escolh… — Exemplo aplicado extenso: 80–150 palavras sem ganho proporcional.

### 1.7 Erros técnicos encontrados independentemente

Segunda leitura com conhecimento próprio, separada dos critérios DeepSeek.

- Nenhum erro conceitual. As definições de linearizabilidade, consistência eventual, CAP e quórum estão corretas e com as ressalvas adequadas.
- Lacuna (não erro): replicação multi-líder não é mencionada (L42 trata líder único e sem líder).
- Redação (L15): "introduz latência, coordenação, localização dos dados…" — o que se introduz é o *problema* de localizar dados; aceitável.
- Trade-off essencial ausente: atomicidade × disponibilidade em transações multi-partição (P1-A).

### 1.8 Factibilidade em 80 minutos

- **Palavras:** 769 de prosa (inclui títulos) + 11 em 1 diagrama(s)/quadro(s) (11 linhas) + 35 nas referências.
- **Fórmulas:** 1 exibida(s), 6 símbolos; simples; 3 expressões matemáticas na linha.
- **Planejamento:** ~3 min (esqueleto de seções; o texto está memorizado). **Revisão mínima:** ~5 min.
- **Orçamento de escrita:** ~70 min (80 − 3 − 5 − 2 de folga).

| Versão | Lenta (12 pal/min) | Moderada (15) | Rápida (18) | Risco de não terminar (moderada / lenta) |
|---|---|---|---|---|
| Texto atual | 69,7 min | 55,9 min | 46,6 min | baixo / alto |
| Com as alterações FAZER (e cortes obrigatórios) | 80,2 min | 64,2 min | 53,6 min | médio / **não cabe** |
| … + cortes C1 | 78,9 min | 63,2 min | 52,8 min | médio / **não cabe** |
| … + cortes C1 + C2 | 77,5 min | 62,1 min | 51,8 min | médio / **não cabe** |
| … + cortes C1 + C2 + C3 | 75,2 min | 60,2 min | 50,1 min | baixo / **não cabe** |
| Cenário lento mínimo (só ESSENCIAL/custo zero + todos os cortes) | 71,8 min | 57,4 min | 47,8 min | baixo / **muito alto** (só com revisão encurtada) |

### 1.9 Alterações prioritárias

#### P1-A — Transações distribuídas (ACID, 2PC, BASE)

1. **Problema.** O texto não trata transações que envolvem várias partições.
2. **Evidência.** Busca por "transa", "2PC", "duas fases", "ACID": nenhuma ocorrência em todo o texto; o "gerenciamento" do título fica restrito a particionamento, replicação e consistência.
3. **Justificativa.** Atomicidade de transações multi-partição e o 2PC são o núcleo clássico de "gerenciamento distribuído de dados" (bancos de dados distribuídos). É uma ideia fundamental (item 1.2) e um ponto de análise crítica (1.1: bloqueio do coordenador; BASE como contraponto), não um detalhe de ferramenta.
4. **Proposta.** Inserir: “Quando uma transação altera várias partições, preservar as garantias **ACID** — em especial a atomicidade — exige coordenação. No *two-phase commit* (**2PC**), um coordenador só efetiva a transação se todos os participantes votarem pela confirmação; caso contrário, ela é abortada. O 2PC acrescenta rodadas de rede e pode bloquear participantes se o coordenador falhar; por isso, muitos sistemas restringem transações a uma partição ou aceitam garantias mais fracas (**BASE**), enquanto sistemas NewSQL combinam 2PC e consenso [7].”
   *Versão mínima (cenário lento):* “Transações que alteram várias partições exigem coordenação para preservar a atomicidade: no *two-phase commit* (2PC), o coordenador só efetiva a transação se todos os participantes votarem pela confirmação. O 2PC acrescenta latência e bloqueia participantes se o coordenador falhar; por isso, muitos sistemas restringem transações a uma partição ou aceitam garantias mais fracas (BASE) [7].”
   *Referência:* [7] KLEPPMANN, M.; RICCOMINI, C. Designing data-intensive applications. 2. ed. O'Reilly, 2026. (Alternativa de encaixe exato: ÖZSU, M. T.; VALDURIEZ, P. Principles of distributed database systems. 4. ed. Springer, 2020.)
5. **Localização.** Novo parágrafo ao final de 1.3.3, depois da L62 (após "...dependam do protocolo completo."). No diagrama da conclusão (L98), trocar "CONSISTÊNCIA / QUÓRUNS" por "CONSISTÊNCIA / QUÓRUNS / TRANSAÇÕES".
6. **Custo.** +76 palavras no corpo; +9 nas referências. Tempo de escrita (lenta / moderada / rápida): +7,1 / +5,7 / +4,7 min. Memorização: média-alta.
7. **Ganho.** Alto e de confiança moderada: preenche a única lacuna conceitual de primeira ordem do ponto; afeta 1.1 (domínio crítico), 1.2 (ideias fundamentais) e 1.4 (referência de 2026). Indicador do modelo da Auditoria 1: +0,85 na leitura central (teto do instrumento). Risco técnico: baixo: afirmações clássicas e com ressalvas. Não afirmar que o 2PC "garante consistência" (garante atomicidade).
8. **Veredito.** **ESSENCIAL**.

#### P1-B — PACELC como complemento do CAP

1. **Problema.** O compromisso latência × consistência fora de partições aparece só como tópico (L81), sem o nome nem a referência que o consagraram.
2. **Evidência.** L52–54 (CAP correto, com a crítica ao "dois de três") e L81 ("garantias fortes versus latência e coordenação"); "PACELC" e "Abadi" ausentes.
3. **Justificativa.** Completa a crítica ao CAP com o caso mais frequente na prática (operação normal, sem partição). É domínio crítico (1.1) e aprofundamento (1.5), com uma citação nova (1.4). Custa uma frase.
4. **Proposta.** Inserir: “O **PACELC** [6] completa essa leitura: havendo partição (P), escolhe-se entre disponibilidade e consistência (A/C); senão (E), entre latência e consistência (L/C), pois coordenar réplicas tem custo mesmo sem falhas.”
   *Referência:* [6] ABADI, D. Consistency tradeoffs in modern distributed database system design. Computer, 2012. (Renumerar: Abadi passa a [6] por aparecer antes do parágrafo de transações, que cita [7].)
5. **Localização.** Depois da L54 (após "...e posterior reconciliação."), como frase final do parágrafo.
6. **Custo.** +32 palavras no corpo; +9 nas referências. Tempo de escrita (lenta / moderada / rápida): +3,4 / +2,7 / +2,3 min. Memorização: média.
7. **Ganho.** Moderado, confiança moderada: 1.1 e 1.5 (crítica mais fina do CAP) e 1.4. Indicador do modelo da Auditoria 1: +0,31 na leitura central (teto do instrumento). Risco técnico: baixo. Não confundir o "E" (else) com "eventual".
8. **Veredito.** **ALTO CUSTO-BENEFÍCIO**.

**Opcionais documentados (não entram na lista de execução):**

- **P1-C — Arquitetura mínima de DFS (GFS/HDFS)** (OPCIONAL; +17 palavras). Torna concreto o sistema citado [1] e cobre o item 1.2 de maior peso no DeepSeek. Fica abaixo de P1-A/P1-B porque o ganho oficial é menor e o texto já cobre os mecanismos genéricos. Texto: “Sistemas de arquivos distribuídos, como o GFS e o HDFS, separam um nó mestre, que mantém os metadados, de servidores que armazenam blocos grandes replicados (tipicamente três cópias, distribuídas entre *racks*), obtendo *throughput* e tolerância a falhas.” Local: Substituir a primeira frase da L66.
- **P1-O1 — MVCC e snapshots** (OPCIONAL; ~20 palavras). Texto: “Muitos sistemas usam MVCC: cada escrita cria uma versão com *timestamp*, e leituras observam um *snapshot* consistente sem bloquear escritas.” Local: Final do parágrafo de P1-A.

### 1.10 Veredito final

**CORRIGIR PONTUALMENTE.** Uma inserção essencial (P1-A) e uma frase (P1-B). No cenário moderado, o texto tem folga para ambas; no lento, usar a versão mínima de P1-A e os cortes do ponto.

## 2. Ponto 2 — Processamento de Dados em Larga Escala: Processamento Paralelo e Distribuído em Larga Escala

Dissertação: `prova-escrita/2-pdle-processamento-paralelo-e-distribuido-em-larga-escala_v2.md` · Barema DeepSeek: `prova-escrita/barema-deepseek/ponto-2.note`

### 2.1 Diagnóstico global

Um dos textos mais fortes. Cobre métricas (speedup, eficiência, Amdahl, strong × weak scaling), granularidade, stragglers, execução especulativa, comunicação, shuffle, MapReduce e DAG/lineage com precisão. A única lacuna relevante é o Spark aparecer sem o RDD e a avaliação preguiçosa, que são o conteúdo do artigo que o próprio texto cita.

| Pergunta | Resposta |
|---|---|
| Tese ou objetivo central | Escalabilidade distribuída não decorre de "mais nós", e sim de paralelismo explorável, pouca comunicação, balanceamento e recuperação (L129). |
| Fundamentos apresentados? | Sim: speedup, eficiência, Amdahl, strong × weak scaling, paralelismo de dados × tarefas (L13–31). |
| O núcleo responde ao tema? | Sim. Lacuna única: o modelo do Spark (RDD, avaliação preguiçosa) é citado [4] sem ser descrito. |
| Sequência lógica? | Sim: fundamentos → decomposição → comunicação → modelos de execução → recuperação → limites. |
| Erros técnicos relevantes? | Nenhum; só notação inconsistente S_p × S(p). |
| Redundância? | Moderada em 2.4: a lista final de cinco pares (L101–107) repete 2.3. |
| Aprofundamento compatível? | Sim, alto para 80 min (três fórmulas, execução especulativa, lineage × checkpoint). |
| Exemplos ajudam? | O fluxo MapReduce ajuda; falta um exemplo de operador (join), opcional. |

### 2.2 Nota anteriormente estimada

- **Auditoria 1:** central **8,3**, intervalo 7,2–9,1.
- **Indicador após as alterações FAZER** (mesmo modelo da Auditoria 1; teto do instrumento, não previsão): central 8,31 → **8,60**; leitura literal (R1) 7,24 → 7,49; viável (R3) 9,11 → 9,47.
- O modelo converte cobertura em pontos de forma mecânica. A direção do efeito é mais confiável que a magnitude, e o ganho oficial tende a ser menor.

### 2.3 Adequação ao barema oficial

| Critério oficial | Avaliação |
|---|---|
| 1.1 | Muito bom. |
| 1.2 | Perde em Spark (RDD, avaliação preguiçosa) e Hadoop/YARN. |
| 1.3 / 2.2 | Exemplar. |
| 1.4 | Clássicos corretos (Amdahl, Gustafson, Dean, Zaharia); nenhuma obra recente. |
| 1.5 | Bom (fórmulas, cauda, especulação). |
| 2.1 / 2.3 / 2.4 | Sem problemas; unificar a notação S(p). |

### 2.4 Principais exigências do DeepSeek atendidas

9 de 34 subitens atendidos integralmente ou de forma equivalente. As seções 2.4, 2.5 e 2.6 juntas classificam todos os 34 subitens.

- 1.1 · L10 · Sincronização e comunicação: barreiras, shuffle, dependências e custos de rede
- 1.1 · L11 · Tolerância a falhas: reexecução de tarefas, lineage, checkpoints e execução especulativa
- 1.1 · L12 · Análise crítica: overhead de comunicação, skew, stragglers, limites de escala e quando não distribuir
- 1.1 · L13 · Localidade de dados e relação entre armazenamento e processamento (fronteira com o Ponto 1)
- 1.2 · L23 · Tolerância a falhas em Spark: lineage, reexecução de tarefas e checkpoints
- 1.2 · L24 · Escalonamento de tarefas: localidade de dados, speculative execution e stragglers
- 1.4 · L26 · Dean & Ghemawat, MapReduce (2004)
- 1.4 · L27 · Zaharia et al., Resilient Distributed Datasets (2012)
- 1.5 · L38 · Stragglers e speculative execution: causas e impacto na latência de cauda

### 2.5 Exigências parcialmente atendidas ou ausentes

"Efeito oficial" é o efeito provável da omissão na ficha da UFC, não no DeepSeek.

| L | Item | Exigência DeepSeek | Situação | Efeito oficial provável | Decisão |
|---|---|---|---|---|---|
| 6 | 1.1 | Definição formal de processamento paralelo × distribuído: memória compartilhada… | Parcial (0,75) | baixo | Não fazer |
| 7 | 1.1 | Taxonomia de paralelismo: paralelismo de dados, de tarefas e pipeline; granular… | Parcial (0,75) | baixo | Não fazer |
| 8 | 1.1 | Modelos de execução: MapReduce, DAG/dataflow e BSP; propriedades e critérios de… | Parcial (0,75) | baixo | Não fazer |
| 9 | 1.1 | Métricas de desempenho: speedup, eficiência, throughput, latência; leis de Amda… | Parcial (0,75) | baixo | Não fazer |
| 16 | 1.2 | Modelo MapReduce: funções map, shuffle/sort e reduce; exemplo canônico de conta… | Parcial (0,75) | baixo | Não fazer |
| 17 | 1.2 | Hadoop MapReduce e YARN: arquitetura de job, ResourceManager, NodeManager e con… | Ausente | baixo a moderado | Opcional (P2-O1) |
| 18 | 1.2 | Spark: RDDs, linhagem, transformações/ações e avaliação preguiçosa | Parcial (0,50) | moderado | Fazer (P2-A) |
| 20 | 1.2 | Escalonamento por DAG: estágios, dependências narrow/wide e barreiras de shuffle | Parcial (0,75) | moderado | Fazer (P2-A) |
| 21 | 1.2 | Particionamento e paralelismo: partições, repartition/coalesce e número de tare… | Parcial (0,50) | baixo | Não fazer |
| 22 | 1.2 | Operações distribuídas: joins broadcast e shuffle, groupBy e agregações | Parcial (0,50) | baixo a moderado | Se houver tempo (P2-B) |
| 30 | 1.4 | Kleppmann, Designing Data-Intensive Applications (2017) | Ausente | baixo | Não fazer |
| 31 | 1.4 | Dean & Barroso, The Tail at Scale (2013) | Parcial (0,25) | baixo | Não fazer |
| 36 | 1.5 | Formalização de speedup S(n) = T1/Tn, eficiência e limites de Amdahl/Gustafson | Parcial (0,75) | baixo | Não fazer |
| 37 | 1.5 | Análise de custo de shuffle: rede, disco, serialização e efeito de particioname… | Parcial (0,50) | baixo | Não fazer |
| 39 | 1.5 | Casos-limite: falha de executor, perda de partição e recomputação longa por lin… | Parcial (0,75) | baixo | Não fazer |
| 40 | 1.5 | Trade-offs: memória × disco, broadcast join × shuffle join e repartition × coal… | Parcial (0,25) | baixo a moderado | Se houver tempo (P2-B) |
| 41 | 1.5 | Relação não trivial entre localidade de dados, elasticidade e custo de serializ… | Parcial (0,50) | baixo | Não fazer |

### 2.6 Exigências do DeepSeek consideradas excessivas ou pouco pertinentes

- L14 (1.1) · Coordenação de recursos e consenso para escalonamento em cluster (fronteira com… — Consenso para escalonamento: fronteira com o Ponto 1, detalhe.
- L19 (1.2) · DataFrames/Datasets e otimizador Catalyst no Spark SQL — Otimizador Catalyst: detalhe de produto.
- L28 (1.4) · Malewicz et al., Pregel (2010) — Pregel: modelo de grafos, periférico.
- L29 (1.4) · Valiant, modelo BSP (1990) — BSP (Valiant): periférico para o recorte.
- L32 (1.4) · Documentação técnica atual de Apache Hadoop/MapReduce/YARN e Apache Spark (veri… — Documentação com versão: inexigível.
- L33 (1.4) · Apache Flink para processamento batch/stream unificado (fronteira com o Ponto 3) — Flink: fronteira com o Ponto 3.
- L34 (1.4) · Benchmarks HiBench e TPCx-HS (verificar versões) — Benchmarks: inexigíveis.
- L42 (1.5) · Exemplo aplicado: pipeline de agregação em larga escala com escolha justificada… — Exemplo aplicado extenso.

### 2.7 Erros técnicos encontrados independentemente

Segunda leitura com conhecimento próprio, separada dos critérios DeepSeek.

- Nenhum erro conceitual. A Lei de Amdahl está correta; Gustafson é citado para weak scaling sem a fórmula (correto, incompleto).
- Notação: S_p e E_p na L18, S(p) na L26 para a mesma grandeza. Unificar como S(p) e E(p) (microajuste).

### 2.8 Factibilidade em 80 minutos

- **Palavras:** 803 de prosa (inclui títulos) + 18 em 2 diagrama(s)/quadro(s) (14 linhas) + 24 nas referências.
- **Fórmulas:** 3 exibida(s), 63 símbolos; moderada; 5 expressões matemáticas na linha.
- **Planejamento:** ~3 min (esqueleto de seções; o texto está memorizado). **Revisão mínima:** ~5 min.
- **Orçamento de escrita:** ~70 min (80 − 3 − 5 − 2 de folga).

| Versão | Lenta (12 pal/min) | Moderada (15) | Rápida (18) | Risco de não terminar (moderada / lenta) |
|---|---|---|---|---|
| Texto atual | 75,6 min | 60,6 min | 50,6 min | baixo / **não cabe** |
| Com as alterações FAZER (e cortes obrigatórios) | 78,8 min | 63,2 min | 52,7 min | médio / **não cabe** |
| … + cortes C1 | 76,4 min | 61,2 min | 51,1 min | baixo / **não cabe** |
| … + cortes C1 + C2 | 75,0 min | 60,1 min | 50,2 min | baixo / **muito alto** (só com revisão encurtada) |
| … + cortes C1 + C2 + C3 | 72,3 min | 57,8 min | 48,1 min | baixo / **muito alto** (só com revisão encurtada) |
| Cenário lento mínimo (só ESSENCIAL/custo zero + todos os cortes) | 69,1 min | 55,3 min | 46,0 min | baixo / alto |

### 2.9 Alterações prioritárias

#### P2-A — RDD, avaliação preguiçosa e dependências estreitas × largas

1. **Problema.** O texto cita o artigo dos RDDs [4] sem nomear o RDD nem a avaliação preguiçosa, que é o que permite ao Spark planejar o DAG.
2. **Evidência.** L79 ("formar estágios separados por shuffles") e L81 ("O Spark combina DAGs, reutilização de dados em memória e lineage [4]"); "RDD" e "preguiçosa/lazy" ausentes.
3. **Justificativa.** RDD e avaliação preguiçosa são a ideia fundamental (1.2) do modelo de execução mais usado em larga escala. Dependências estreitas × largas explicam tecnicamente a fronteira de estágio que o texto já menciona (1.1). Exige só substituir duas frases.
4. **Proposta.** Substituir “O Spark combina DAGs, reutilização de dados em memória e **lineage** [4]: em vez de replicar todos os resultados intermediários, uma partição perdida pode ser recomputada a partir de suas dependências.” por: “O Spark [4] representa os dados como **RDDs**, coleções imutáveis e particionadas cujas transformações são avaliadas de forma preguiçosa até que uma ação exija resultado; isso permite planejar o DAG inteiro, reutilizar dados em memória e explorar **lineage**: em vez de replicar todos os resultados intermediários, uma partição perdida pode ser recomputada a partir de suas dependências.”
   Também substituir “formar estágios separados por *shuffles*” por “formar estágios que encadeiam operações com dependências estreitas e terminam nas dependências largas, isto é, nos *shuffles*,”.
5. **Localização.** (a) L81: substituir a frase inteira. (b) L79: substituir o trecho "formar estágios separados por *shuffles*".
6. **Custo.** +38 palavras no corpo. Tempo de escrita (lenta / moderada / rápida): +3,2 / +2,5 / +2,1 min. Memorização: média.
7. **Ganho.** Moderado, confiança moderada a alta: 1.2 (Spark) e 1.1 (precisão do modelo de execução). Indicador do modelo da Auditoria 1: +0,29 na leitura central (teto do instrumento). Risco técnico: baixo. "Preguiçosa" vale para as transformações; as ações disparam a execução.
8. **Veredito.** **ALTO CUSTO-BENEFÍCIO**.

**Opcionais documentados (não entram na lista de execução):**

- **P2-B — Exemplo concreto: join com shuffle × broadcast join** (OPCIONAL; +20 palavras). Troca uma frase abstrata por um exemplo que a demonstra (1.5) e cobre operadores distribuídos (1.2). Ganho real, mas o ponto já está entre os mais fortes. Texto: “Abstrações de alto nível tampouco eliminam custos físicos: um *join* entre duas tabelas grandes exige *shuffle* de ambas pela rede, ao passo que, se uma delas for pequena, ela pode ser replicada em todos os nós (*broadcast join*), evitando a redistribuição da maior.” Local: Substituir a frase da L99.
- **P2-O1 — YARN** (OPCIONAL; ~24 palavras). Texto: “No ecossistema Hadoop, o YARN separa o gerenciamento de recursos do modelo de programação, permitindo executar MapReduce, Spark e outros frameworks no mesmo cluster.” Local: Final de 2.3.3.

**Microajustes de precisão (custo ~0; fora do limite de três):**

- L18 e L23–26: “S_{p} / E_{p} (L18) e S(p) (L26)” → “usar uma só notação, S(p) e E(p)”. Notação inconsistente para a mesma grandeza.

### 2.10 Veredito final

**CORRIGIR PONTUALMENTE (leve).** Uma substituição (P2-A). Quase fechada.

## 3. Ponto 3 — Processamento de Dados em Larga Escala: Processamento de Fluxos e Arquiteturas de Dados

Dissertação: `prova-escrita/3-pdle-processamento-de-fluxos-e-arquiteturas-de-dados_v2.md` · Barema DeepSeek: `prova-escrita/barema-deepseek/ponto-3.note`

### 3.1 Diagnóstico global

Texto maduro: trata tempo, estado e garantias como eixo, com formalização de estado, condição de backlog e exactly-once fim a fim. Há uma imprecisão de atribuição (as "três perguntas" do Dataflow) e falta concretude nominal (nenhuma engine nomeada; Kappa sem citação). Não há lacuna conceitual que justifique inserção de porte.

| Pergunta | Resposta |
|---|---|
| Tese ou objetivo central | Processamento de fluxos é um problema de tempo, estado e garantias; a arquitetura deve ter a menor complexidade que satisfaça as garantias do workload (L93, L113). |
| Fundamentos apresentados? | Sim: bounded × unbounded, batch × streaming complementares, latência × throughput, ordem por partição (L13–25). |
| O núcleo responde ao tema? | Sim, com amplitude: tempo de evento, janelas, watermark, trigger, estado, checkpoints, semânticas, log, Lambda/Kappa, lakehouse, backpressure. |
| Sequência lógica? | Sim. |
| Erros técnicos relevantes? | Uma imprecisão de atribuição (L37: "três perguntas" do Dataflow). Ver P3-A. |
| Redundância? | Baixa: a cadeia L19–21 reaparece no diagrama final; L93 e L113 dizem o mesmo. |
| Aprofundamento compatível? | Sim, alto (fórmula de estado, condição de backlog, exactly-once fim a fim com sink transacional). |
| Exemplos ajudam? | Sim; nenhum ocupa espaço indevido. |

### 3.2 Nota anteriormente estimada

- **Auditoria 1:** central **8,5**, intervalo 7,7–9,2.
- **Indicador após as alterações FAZER** (mesmo modelo da Auditoria 1; teto do instrumento, não previsão): central 8,48 → **8,66**; leitura literal (R1) 7,69 → 7,85; viável (R3) 9,24 → 9,46.
- O modelo converte cobertura em pontos de forma mecânica. A direção do efeito é mais confiável que a magnitude, e o ganho oficial tende a ser menor.

### 3.3 Adequação ao barema oficial

| Critério oficial | Avaliação |
|---|---|
| 1.1 | Muito bom; uma imprecisão de atribuição (L37). |
| 1.2 | Perde por não nomear engines e por tratar o Kafka sem offsets/consumer groups. |
| 1.3 / 2.2 | Exemplar. |
| 1.4 | Boa (Akidau, Carbone, Kreps, Marz); a Kappa (L73) está sem citação. |
| 1.5 | Muito bom. |
| 2.1 / 2.3 / 2.4 | Sem problemas. |

### 3.4 Principais exigências do DeepSeek atendidas

13 de 36 subitens atendidos integralmente ou de forma equivalente. As seções 3.4, 3.5 e 3.6 juntas classificam todos os 36 subitens.

- 1.1 · L6 · Definição formal de stream e distinção entre dados limitados (batch) e ilimitados (stream)
- 1.1 · L8 · Semânticas de entrega: at-most-once, at-least-once e exactly-once; implicações práticas
- 1.1 · L10 · Watermarks e tratamento de eventos atrasados; allowed lateness
- 1.1 · L14 · Análise crítica: quando não usar streaming; custos, complexidade e limites do exactly-once
- 1.2 · L18 · Arquitetura Kappa: log imutável, reprocessamento e stream único; limitações
- 1.2 · L22 · Exactly-once fim a fim: checkpoints, transações e idempotência em sinks
- 1.2 · L23 · Camadas de arquitetura: ingestão, armazenamento, processamento e serving; data lake/lakehouse (fronteira com…
- 1.4 · L27 · Kreps et al., Kafka (2011)
- 1.4 · L28 · Akidau et al., The Dataflow Model (2015)
- 1.4 · L29 · Carbone et al., Apache Flink (2015) — *equivalente:* Carbone et al. 2017 (gestão de estado no Flink) em vez do artigo de 2015 do mesmo grupo.
- 1.4 · L31 · Marz & Warren, Big Data (2015)
- 1.5 · L39 · Exactly-once fim a fim: transações, idempotência e trade-offs com latência e custo
- 1.5 · L41 · Trade-offs Lambda × Kappa: reprocessamento, duplicação de código, latência e custo operacional

### 3.5 Exigências parcialmente atendidas ou ausentes

"Efeito oficial" é o efeito provável da omissão na ficha da UFC, não no DeepSeek.

| L | Item | Exigência DeepSeek | Situação | Efeito oficial provável | Decisão |
|---|---|---|---|---|---|
| 7 | 1.1 | Tempo de evento × tempo de ingestão × tempo de processamento; desordem e atrasos | Parcial (0,75) | baixo | Não fazer |
| 9 | 1.1 | Processamento com estado: estado chaveado, backends e recuperação | Parcial (0,75) | baixo | Não fazer |
| 11 | 1.1 | Janelas tumbling, sliding, session e global; triggers e eviction | Parcial (0,75) | baixo | Não fazer |
| 12 | 1.1 | Backpressure e controle de fluxo em pipelines de stream | Parcial (0,75) | baixo | Não fazer |
| 13 | 1.1 | Log distribuído, partições, offsets e consumer groups (fronteira com o Ponto 1) | Parcial (0,75) | baixo a moderado | Se houver tempo (P3-B) |
| 17 | 1.2 | Arquitetura Lambda: camadas batch, speed e serving; funcionamento e limitações | Parcial (0,75) | baixo | Não fazer |
| 19 | 1.2 | Ingestão de dados: conectores, CDC e pipelines de eventos | Parcial (0,25) | baixo a moderado | Opcional (P3-O1) |
| 20 | 1.2 | Kafka: tópicos, partições, replicação, offsets, retenção e consumer groups | Parcial (0,50) | baixo a moderado | Se houver tempo (P3-B) |
| 21 | 1.2 | Motores de stream: Flink, Kafka Streams e Spark Structured Streaming; operadore… | Parcial (0,25) | moderado | Fazer (P3-C) |
| 30 | 1.4 | Akidau, Chernyak & Lax, Streaming Systems (2018) | Ausente | baixo | Não fazer |
| 32 | 1.4 | Kreps, Questioning the Lambda Architecture (2014) | Parcial (0,25) | baixo a moderado | Fazer (P3-C) |
| 33 | 1.4 | Kleppmann, Designing Data-Intensive Applications (2017) | Ausente | baixo | Não fazer |
| 37 | 1.5 | Formalização de watermarks: completude versus latência e heurísticas de avanço | Parcial (0,75) | baixo | Não fazer |
| 38 | 1.5 | Janelas e triggers: allowed lateness, modos de acumulação e emissão de resultad… | Parcial (0,75) | baixo | Não fazer |
| 40 | 1.5 | Casos-limite: eventos além da latência permitida, partições quentes e falha de… | Parcial (0,25) | baixo | Não fazer |
| 42 | 1.5 | Relação entre ordenação por chave, partições e paralelismo em operadores statef… | Parcial (0,75) | baixo | Não fazer |
| 43 | 1.5 | Backpressure e skew em operadores stateful | Parcial (0,50) | baixo | Não fazer |

### 3.6 Exigências do DeepSeek consideradas excessivas ou pouco pertinentes

- L15 (1.1) · Trade-offs entre motores unificados batch/stream e pipelines especializados (fr… — Motores unificados × especializados: comparação de produtos.
- L24 (1.2) · Orquestração de pipelines, DAGs e lineage — Orquestração de pipelines: periférico.
- L25 (1.2) · Padrões de serving: materialized views, CQRS e stores de leitura — CQRS/materialized views: padrão de software, periférico ao tema.
- L34 (1.4) · Documentação atual de Apache Kafka, Apache Flink e Spark Structured Streaming (… — Documentação com versão: inexigível.
- L35 (1.4) · Documentação de Apache Iceberg/Hudi/Delta Lake (fronteira com o Ponto 1) — Documentação de Iceberg/Hudi/Delta: inexigível.
- L44 (1.5) · Exemplo aplicado: detecção de fraude/anomalia em tempo real com janelas e exact… — Exemplo aplicado extenso.

### 3.7 Erros técnicos encontrados independentemente

Segunda leitura com conhecimento próprio, separada dos critérios DeepSeek.

- Imprecisão de atribuição (L37): "três perguntas" (windowing, watermark, trigger). O watermark é um mecanismo, não uma pergunta. No livro de Akidau, Chernyak e Lax (2018), cujo subtítulo é "the what, where, when, and how", as perguntas são quatro. Ver P3-A.
- L43: "watermark é uma estimativa, não uma garantia" é verdadeiro para watermarks heurísticos (o caso usual).
- L75: o lakehouse é caracterizado sem sua propriedade distintiva (transações ACID sobre o lago). Ver P3-C.

### 3.8 Factibilidade em 80 minutos

- **Palavras:** 802 de prosa (inclui títulos) + 21 em 2 diagrama(s)/quadro(s) (12 linhas) + 28 nas referências.
- **Fórmulas:** 2 exibida(s), 37 símbolos; simples; 4 expressões matemáticas na linha.
- **Planejamento:** ~3 min (esqueleto de seções; o texto está memorizado). **Revisão mínima:** ~5 min.
- **Orçamento de escrita:** ~70 min (80 − 3 − 5 − 2 de folga).

| Versão | Lenta (12 pal/min) | Moderada (15) | Rápida (18) | Risco de não terminar (moderada / lenta) |
|---|---|---|---|---|
| Texto atual | 75,0 min | 60,1 min | 50,1 min | baixo / **muito alto** (só com revisão encurtada) |
| Com as alterações FAZER (e cortes obrigatórios) | 76,4 min | 61,3 min | 51,1 min | baixo / **não cabe** |
| … + cortes C1 | 74,7 min | 59,8 min | 49,9 min | baixo / **muito alto** (só com revisão encurtada) |
| … + cortes C1 + C2 | 73,1 min | 58,6 min | 48,9 min | baixo / **muito alto** (só com revisão encurtada) |
| … + cortes C1 + C2 + C3 | 70,5 min | 56,4 min | 46,9 min | baixo / **muito alto** (só com revisão encurtada) |
| Cenário lento mínimo (só ESSENCIAL/custo zero + todos os cortes) | 68,8 min | 55,0 min | 45,8 min | baixo / alto |

### 3.9 Alterações prioritárias

#### P3-A — Correção: o Dataflow não se resume a "três perguntas"

1. **Problema.** O texto atribui ao modelo Dataflow "três perguntas" (windowing, watermark, trigger). O watermark é um mecanismo, não uma pergunta, e a formulação canônica do grupo de Akidau usa quatro perguntas (o quê, onde, quando, como).
2. **Evidência.** L37: "O modelo Dataflow [1] organiza o problema em três perguntas:".
3. **Justificativa.** Uma imprecisão de atribuição visível a quem conhece a obra citada afeta o domínio técnico (1.1) e a precisão (2.3). A correção não custa nada.
4. **Proposta.** Substituir “O modelo Dataflow [1] organiza o problema em três perguntas:” por: “O modelo Dataflow [1] articula três mecanismos:”
5. **Localização.** L37: substituir o início da frase; os três marcadores seguintes ficam como estão.
6. **Custo.** −3 palavras no corpo. Tempo de escrita (lenta / moderada / rápida): −0,2 / −0,2 / −0,2 min. Memorização: baixa.
7. **Ganho.** Pequeno em pontos, mas remove um risco de desconto em 1.1/2.3; confiança alta quanto ao acerto da correção. Indicador do modelo da Auditoria 1: +0,00 na leitura central (teto do instrumento). Risco técnico: nenhum.
8. **Veredito.** **ALTO CUSTO-BENEFÍCIO**.

#### P3-C — Nomear engines, ligar [2] ao Flink, citar a Kappa e incluir ACID no lakehouse

1. **Problema.** Nenhuma engine de stream é nomeada; a Kappa (L73) não tem citação; o lakehouse (L75) omite sua característica definidora (transações ACID sobre o data lake).
2. **Evidência.** L55 ("replay [2]"), L67 ("engine de processamento"), L73 ("Kappa Architecture"), L75 ("gerenciamento de esquema, governança e consultas eficientes").
3. **Justificativa.** Quatro microinserções (+12 palavras no corpo) dão concretude (1.2), atribuem a Kappa a quem a propôs (1.4) e corrigem uma caracterização incompleta do lakehouse (1.1).
4. **Proposta.** Microinserções: (a) L55: "...e **replay** [2]:" → "...e **replay**, como no Apache Flink [2]:". (b) L67: "não substitui a engine de processamento," → "não substitui a engine de processamento (ex.: Flink, Spark Structured Streaming),". (c) L73: "A **Kappa Architecture** elimina" → "A **Kappa Architecture** [5] elimina". (d) L75: "acrescentam a essa flexibilidade gerenciamento de esquema" → "acrescentam a essa flexibilidade transações ACID, gerenciamento de esquema".
   *Referência:* [5] KREPS, J. Questioning the Lambda Architecture. O'Reilly Radar, 2014.
5. **Localização.** Indicada no item 4.
6. **Custo.** +12 palavras no corpo; +8 nas referências. Tempo de escrita (lenta / moderada / rápida): +1,7 / +1,3 / +1,1 min. Memorização: baixa.
7. **Ganho.** Moderado (1.2 + 1.4), confiança moderada. Indicador do modelo da Auditoria 1: +0,19 na leitura central (teto do instrumento). Risco técnico: nenhum relevante.
8. **Veredito.** **ALTO CUSTO-BENEFÍCIO**.

**Opcionais documentados (não entram na lista de execução):**

- **P3-B — Offsets e consumer groups no Kafka** (OPCIONAL; +35 palavras). Explica como o replay funciona (1.1/1.2). Fica como opcional porque o ponto já está forte e o mecanismo é detalhe do Kafka. Texto: “Cada evento recebe um *offset* em sua partição; consumidores de um mesmo *consumer group* dividem as partições entre si e registram o último *offset* processado, o que permite retomar o consumo e reprocessar o histórico.” Local: Final do parágrafo da L65.
- **P3-O1 — CDC na ingestão** (OPCIONAL; ~17 palavras). Texto: “Bancos operacionais podem alimentar o log por *change data capture* (CDC), que publica cada alteração como evento.” Local: Final do parágrafo da L63.

### 3.10 Veredito final

**MANTER.** Só a correção de quatro palavras (P3-A) e as microinserções nominais (P3-C). Pode ser considerada fechada.

## 4. Ponto 4 — Mineração de Dados: Descoberta de Conhecimento, Análise Exploratória de Dados, Identificação de Padrões e Anomalias

Dissertação: `prova-escrita/4-mineracao-de-dados-descoberta-de-conhecimento-aed-identificacao-de-padroes-e-anomalias_v2.md` · Barema DeepSeek: `prova-escrita/barema-deepseek/ponto-4.note`

### 4.1 Diagnóstico global

Boa tese (padrão ≠ conhecimento), KDD bem posicionado, regras de associação formalizadas corretamente e seção crítica forte. O ponto fraco é que a **EDA**, um dos quatro termos do título, é descrita só em abstrato, sem nenhum instrumento concreto. Os métodos de anomalia aparecem apenas como famílias.

| Pergunta | Resposta |
|---|---|
| Tese ou objetivo central | Mineração é etapa do KDD; um padrão só vira conhecimento com validação, interpretação e contexto (L31–35, L145). |
| Fundamentos apresentados? | Sim: KDD, etapas, dado × padrão × conhecimento, critérios de Fayyad (L5–37). |
| O núcleo responde ao tema? | Responde a KDD, padrões e anomalias. A EDA é tratada só conceitualmente (P4-A). |
| Sequência lógica? | Sim: preparação → EDA → padrões → anomalias → limitações. |
| Erros técnicos relevantes? | Nenhum. Registro: "biologicamente" (L89, L121) é específico demais para a banca. |
| Redundância? | Moderada: quatro quadros curtos repetem as frases vizinhas (L9–11, L53–55, L115–117). |
| Aprofundamento compatível? | Bom em regras de associação (três fórmulas corretas) e na crítica (múltiplas comparações, causalidade); raso em EDA e métodos de anomalia. |
| Exemplos ajudam? | As fórmulas de associação, sim. Faltam instrumentos concretos de EDA. |

### 4.2 Nota anteriormente estimada

- **Auditoria 1:** central **7,4**, intervalo 6,6–8,3.
- **Indicador após as alterações FAZER** (mesmo modelo da Auditoria 1; teto do instrumento, não previsão): central 7,36 → **8,28**; leitura literal (R1) 6,61 → 7,36; viável (R3) 8,34 → 9,24.
- O modelo converte cobertura em pontos de forma mecânica. A direção do efeito é mais confiável que a magnitude, e o ganho oficial tende a ser menor.

### 4.3 Adequação ao barema oficial

| Critério oficial | Avaliação |
|---|---|
| 1.1 | Bom. |
| 1.2 | Perde em EDA operacional, agrupamento e métodos de anomalia. |
| 1.3 / 2.2 | Exemplar. |
| 1.4 | Boa (Fayyad, Tukey, Han, Aggarwal); Han pode ser atualizado para a 4ª ed. (2022). |
| 1.5 | Médio: regras de associação formalizadas; o resto é enumerativo. |
| 2.1 / 2.3 / 2.4 | Trocar "biologicamente" por termos neutros. |

### 4.4 Principais exigências do DeepSeek atendidas

11 de 38 subitens atendidos integralmente ou de forma equivalente. As seções 4.4, 4.5 e 4.6 juntas classificam todos os 38 subitens.

- 1.1 · L6 · Definição formal de KDD (Knowledge Discovery in Databases) e distinção entre KDD e mineração de dados como et…
- 1.1 · L7 · Definição de Análise Exploratória de Dados (EDA) e seu papel no ciclo de descoberta
- 1.1 · L8 · Definição formal de padrão e de anomalia/outlier, com critérios de distinção
- 1.1 · L12 · Limitações: maldição da dimensionalidade e risco de overfitting em descoberta de padrões
- 1.1 · L13 · Pré-processamento: limpeza, normalização, discretização e tratamento de valores ausentes
- 1.2 · L17 · Processo KDD: etapas de seleção, pré-processamento, transformação, mineração e interpretação/avaliação; natur…
- 1.2 · L27 · Avaliação de padrões: medidas de interestingness e validação de resultados
- 1.4 · L29 · Fayyad, Piatetsky-Shapiro & Smyth (1996), From Data Mining to Knowledge Discovery in Databases
- 1.4 · L30 · Han, Kamber & Pei, Data Mining: Concepts and Techniques (verificar edição)
- 1.4 · L31 · Tukey (1977), Exploratory Data Analysis
- 1.4 · L33 · Aggarwal, Outlier Analysis (verificar edição)

### 4.5 Exigências parcialmente atendidas ou ausentes

"Efeito oficial" é o efeito provável da omissão na ficha da UFC, não no DeepSeek.

| L | Item | Exigência DeepSeek | Situação | Efeito oficial provável | Decisão |
|---|---|---|---|---|---|
| 9 | 1.1 | Tipos de atributos e escalas de medida (nominal, ordinal, intervalar, razão) e… | Ausente | baixo | Não fazer |
| 10 | 1.1 | Medidas de similaridade e distância: Euclidiana, Manhattan, Jaccard e cosseno;… | Parcial (0,25) | baixo a moderado | Opcional (P4-O1) |
| 11 | 1.1 | Análise crítica da EDA: correlação não implica causalidade e riscos de viés de… | Parcial (0,75) | baixo | Não fazer |
| 14 | 1.1 | Análise crítica de medidas de avaliação de padrões (ex.: suporte e confiança po… | Parcial (0,75) | baixo | Não fazer |
| 15 | 1.1 | Quando não usar métodos: clustering em alta dimensão sem redução, detecção de a… | Parcial (0,25) | baixo a moderado | Se houver tempo (P4-C) |
| 18 | 1.2 | EDA: estatísticas descritivas (média, mediana, desvio padrão, quartis) e sua in… | Parcial (0,25) | alto | Fazer (P4-A) |
| 19 | 1.2 | EDA: visualizações (histograma, boxplot, dispersão, heatmap) e o que cada uma r… | Parcial (0,25) | alto | Fazer (P4-A) |
| 20 | 1.2 | Análise de correlação: coeficientes de Pearson e Spearman e limitações | Parcial (0,25) | alto | Fazer (P4-A) |
| 21 | 1.2 | Regras de associação: suporte, confiança e lift; algoritmo Apriori | Parcial (0,75) | baixo a moderado | Opcional (P4-O2) |
| 23 | 1.2 | Agrupamento (clustering) como descoberta de padrões: k-means, hierárquico e DBS… | Parcial (0,25) | baixo a moderado | Se houver tempo (P4-C) |
| 24 | 1.2 | Detecção de anomalias: métodos estatísticos (z-score, intervalo interquartil) | Parcial (0,25) | moderado | Fazer (P4-B) |
| 25 | 1.2 | Detecção de anomalias: métodos baseados em distância (k-NN) e densidade (LOF) | Parcial (0,25) | moderado | Fazer (P4-B) |
| 26 | 1.2 | Isolation Forest e One-Class SVM (fronteira com o Ponto 5) | Parcial (0,25) | moderado | Fazer (P4-B) |
| 32 | 1.4 | Chandola, Banerjee & Kumar (2009), Anomaly Detection: A Survey | Parcial (0,25) | baixo | Não fazer |
| 34 | 1.4 | CRISP-DM (Shearer, 2000) como processo padrão de mineração de dados | Ausente | baixo | Não fazer |
| 36 | 1.4 | Agrawal & Srikant (1994), Fast Algorithms for Mining Association Rules | Parcial (0,25) | baixo | Não fazer |
| 39 | 1.5 | Formalização de suporte, confiança e lift; propriedades (ex.: confiança não é s… | Parcial (0,75) | baixo | Não fazer |
| 41 | 1.5 | Escolha de medida de distância e impacto em clustering/anomalias; efeito da alt… | Parcial (0,50) | baixo a moderado | Opcional (P4-O1) |
| 42 | 1.5 | Sensibilidade a parâmetros: k em k-NN, eps/minPts em DBSCAN, contaminação em Is… | Parcial (0,25) | moderado | Fazer (P4-B) |
| 43 | 1.5 | Casos-limite: anomalias em alta dimensionalidade, dados categóricos e dados tem… | Parcial (0,50) | baixo | Não fazer |
| 44 | 1.5 | Relação entre EDA e detecção automática de anomalias: visualização versus métod… | Parcial (0,25) | moderado | Fazer (P4-A) |
| 45 | 1.5 | Trade-offs em detecção de anomalias: precisão versus recall e custo de falsos p… | Parcial (0,25) | baixo | Não fazer |

### 4.6 Exigências do DeepSeek consideradas excessivas ou pouco pertinentes

- L22 (1.2) · Algoritmo FP-Growth e comparação com Apriori — FP-Growth: segundo algoritmo de associação, detalhe.
- L35 (1.4) · Documentação atual de scikit-learn, pandas, matplotlib e seaborn (verificar ver… — Documentação de bibliotecas: inexigível.
- L37 (1.4) · Zimek, Schubert & Kriegel (2012), On the Evaluation of Unsupervised Outlier Det… — Zimek et al.: referência especializada.
- L40 (1.5) · Complexidade do Apriori (exponencial no pior caso) e otimizações via FP-Growth — Complexidade do Apriori e FP-Growth: detalhe algorítmico.
- L46 (1.5) · Exemplo aplicado: detecção de fraude em transações com EDA e Isolation Forest — Exemplo aplicado extenso.

### 4.7 Erros técnicos encontrados independentemente

Segunda leitura com conhecimento próprio, separada dos critérios DeepSeek.

- Nenhum erro. As fórmulas de suporte, confiança e lift estão corretas.
- Registro: "biologicamente relevante" (L89) e "biologicamente implausível" (L121) soam como marca do autor (bioinformática) numa banca de Computação; trocar por termos neutros (microajuste).

### 4.8 Factibilidade em 80 minutos

- **Palavras:** 783 de prosa (inclui títulos) + 30 em 6 diagrama(s)/quadro(s) (19 linhas) + 28 nas referências.
- **Fórmulas:** 3 exibida(s), 74 símbolos; moderada; 4 expressões matemáticas na linha.
- **Planejamento:** ~3 min (esqueleto de seções; o texto está memorizado). **Revisão mínima:** ~5 min.
- **Orçamento de escrita:** ~70 min (80 − 3 − 5 − 2 de folga).

| Versão | Lenta (12 pal/min) | Moderada (15) | Rápida (18) | Risco de não terminar (moderada / lenta) |
|---|---|---|---|---|
| Texto atual | 77,2 min | 62,0 min | 51,7 min | baixo / **não cabe** |
| Com as alterações FAZER (e cortes obrigatórios) | 82,5 min | 66,2 min | 55,2 min | médio / **não cabe** |
| … + cortes C1 | 81,2 min | 65,1 min | 54,3 min | médio / **não cabe** |
| … + cortes C1 + C2 | 78,3 min | 62,8 min | 52,4 min | médio / **não cabe** |
| … + cortes C1 + C2 + C3 | 76,1 min | 60,9 min | 50,7 min | baixo / **não cabe** |
| Cenário lento mínimo (só ESSENCIAL/custo zero + todos os cortes) | 75,2 min | 60,2 min | 50,1 min | baixo / **não cabe** |

### 4.9 Alterações prioritárias

#### P4-A — Conteúdo operacional mínimo da EDA

1. **Problema.** A EDA, que está no título do ponto, é definida só em termos genéricos ("estatísticas descritivas e visualizações"), sem nenhuma medida, gráfico ou coeficiente.
2. **Evidência.** L49–51. Busca por "mediana", "quartil", "boxplot", "histograma", "Pearson", "Spearman": nenhuma ocorrência. Tukey [2], criador do boxplot, é citado sem conteúdo associado.
3. **Justificativa.** Sem nenhum instrumento concreto, a banca pode ler a EDA como tratada só de passagem. É ideia fundamental (1.2) de um dos quatro componentes do título. Uma frase resolve e ainda dá função à citação de Tukey.
4. **Proposta.** Inserir: “Na prática, combinam-se medidas de posição e dispersão — média e desvio padrão, sensíveis a valores extremos; mediana e quartis, mais robustos, que compõem o resumo de cinco números e o *boxplot* de Tukey — com histogramas e diagramas de dispersão; os coeficientes de Pearson (relação linear) e de Spearman (relação monotônica) quantificam associações.”
   *Versão mínima (cenário lento):* “Na prática, usam-se média, mediana, desvio padrão e quartis (base do *boxplot* de Tukey), histogramas e diagramas de dispersão, além dos coeficientes de Pearson (linear) e Spearman (monotônico).”
5. **Localização.** Novo parágrafo depois da L49 (antes de "Pode ser univariada...").
6. **Custo.** +52 palavras no corpo. Tempo de escrita (lenta / moderada / rápida): +4,3 / +3,5 / +2,9 min. Memorização: média-alta.
7. **Ganho.** Alto e de confiança moderada: torna verificável o domínio de EDA (1.2) e acrescenta crítica (robustez a extremos, linear × monotônico). Indicador do modelo da Auditoria 1: +0,53 na leitura central (teto do instrumento). Risco técnico: baixo. Não dizer que Pearson "mede causalidade" nem que Spearman "mede relação não linear qualquer" (mede relação monotônica).
8. **Veredito.** **ESSENCIAL**.

#### P4-B — Nomear um método por família de detecção de anomalias

1. **Problema.** As famílias de detecção são listadas sem nenhum método.
2. **Evidência.** L97: "distribuição estatística, distância, densidade, vizinhança ou isolamento".
3. **Justificativa.** Com +11 palavras, cada família ganha um representante canônico (1.2) e a regra do IQR se conecta ao boxplot de P4-A.
4. **Proposta.** Substituir “A detecção pode basear-se em distribuição estatística, distância, densidade, vizinhança ou isolamento.” por: “A detecção pode basear-se em distribuição estatística (escore z, regra do IQR), distância (k vizinhos mais próximos), densidade (LOF) ou isolamento (*Isolation Forest*).”
5. **Localização.** Substituir a frase da L97.
6. **Custo.** +11 palavras no corpo. Tempo de escrita (lenta / moderada / rápida): +0,9 / +0,7 / +0,6 min. Memorização: baixa.
7. **Ganho.** Moderado (1.2), confiança moderada a alta. Indicador do modelo da Auditoria 1: +0,38 na leitura central (teto do instrumento). Risco técnico: nenhum relevante.
8. **Veredito.** **ALTO CUSTO-BENEFÍCIO**.

**Opcionais documentados (não entram na lista de execução):**

- **P4-C — Agrupamento sem remeter ao Ponto 5** (OPCIONAL; +19 palavras). Troca a remissão por uma crítica relevante: algoritmos de agrupamento sempre produzem grupos (1.1/1.2). Custo líquido de +20 palavras. Texto: “Agrupamentos revelam estrutura latente ao reunir observações semelhantes — por centroides (k-means), por densidade (DBSCAN) ou hierarquicamente —, mas algoritmos de agrupamento sempre produzem grupos, mesmo em dados sem estrutura; por isso, coesão, separação e estabilidade devem ser verificadas.” Local: Substituir a frase da L79.
- **P4-O1 — Medidas de proximidade por tipo de atributo** (OPCIONAL; ~26 palavras). Texto: “A medida de proximidade deve respeitar o tipo de atributo: euclidiana para atributos numéricos padronizados, Jaccard para conjuntos binários e cosseno para vetores esparsos, como textos.” Local: Antes da L99.
- **P4-O2 — Propriedade do Apriori** (OPCIONAL; ~22 palavras). Texto: “O algoritmo Apriori explora a antimonotonicidade do suporte: se um conjunto de itens é infrequente, todos os seus superconjuntos também o são.” Local: Depois da L77.

**Microajustes de precisão (custo ~0; fora do limite de três):**

- L89: “fenômeno biologicamente relevante” → “fenômeno cientificamente relevante”. Exemplo de domínio específico demais para a banca de Computação.
- L121: “biologicamente implausível” → “implausível no domínio”. Idem.

### 4.10 Veredito final

**CORRIGIR PONTUALMENTE.** Uma inserção essencial (P4-A) e uma substituição curta (P4-B).

## 5. Ponto 5 — Aprendizado Supervisionado e Não Supervisionado

Dissertação: `prova-escrita/5-aprendizado-supervisionado-e-nao-supervisionado_v2.md` · Barema DeepSeek: `prova-escrita/barema-deepseek/ponto-5.note`

### 5.1 Diagnóstico global

Metodologicamente excelente (ERM implícito, split, parâmetros × hiperparâmetros, viés-variância, métricas, leakage, validação cruzada), mas com desequilíbrio: os algoritmos, que são as "ideias fundamentais" mais óbvias do tema, aparecem em uma linha cada. A correção mais eficiente é trocar três linhas genéricas por mecanismos e enxugar duas repetições da tese "método = algoritmo + hipótese".

| Pergunta | Resposta |
|---|---|
| Tese ou objetivo central | Os paradigmas diferem pela presença do alvo; em ambos, aprender é generalizar, e a escolha depende da adequação problema–dados–hipótese–métrica (L144–146). |
| Fundamentos apresentados? | Sim e muito bem: formalização, perda, split, parâmetros × hiperparâmetros, viés-variância, regularização (L5–48). |
| O núcleo responde ao tema? | Na metodologia, sim. Nos algoritmos, só por rótulos de uma linha (L58–63, L77–81). |
| Sequência lógica? | Sim. |
| Erros técnicos relevantes? | Uma imprecisão menor (L83: o DBSCAN não otimiza função). |
| Redundância? | Alta para o tamanho: a tese "método = algoritmo + hipótese" aparece três vezes (L56, L65–69, L116–122); a lista de trade-offs repete 5.2. |
| Aprofundamento compatível? | Desequilibrado: alto em avaliação e validação, baixo em mecanismos. |
| Exemplos ajudam? | O classificador majoritário (L89) é ótimo; as "fórmulas" textuais em quadro ocupam espaço sem ganho. |

### 5.2 Nota anteriormente estimada

- **Auditoria 1:** central **7,0**, intervalo 6,5–7,5.
- **Indicador após as alterações FAZER** (mesmo modelo da Auditoria 1; teto do instrumento, não previsão): central 6,97 → **7,85**; leitura literal (R1) 6,50 → 7,31; viável (R3) 7,53 → 8,47.
- O modelo converte cobertura em pontos de forma mecânica. A direção do efeito é mais confiável que a magnitude, e o ganho oficial tende a ser menor.

### 5.3 Adequação ao barema oficial

| Critério oficial | Avaliação |
|---|---|
| 1.1 | Bom em metodologia. |
| 1.2 | A maior perda dos dez pontos: algoritmos em uma linha. |
| 1.3 / 2.2 | Exemplar. |
| 1.4 | Manuais corretos; nenhum posterior a 2016. |
| 1.5 | Baixo: falta formalização de L1/L2 e dos mecanismos. |
| 2.1 / 2.3 / 2.4 | Imprecisão menor na L83. |

### 5.4 Principais exigências do DeepSeek atendidas

9 de 41 subitens atendidos integralmente ou de forma equivalente. As seções 5.4, 5.5 e 5.6 juntas classificam todos os 41 subitens.

- 1.1 · L6 · Definição formal de aprendizado supervisionado (dados rotulados) e não supervisionado (sem rótulos), com obje…
- 1.1 · L7 · Formulação das tarefas: classificação, regressão, agrupamento e redução de dimensionalidade
- 1.1 · L9 · Trade-off viés-variância; overfitting, underfitting e capacidade de generalização
- 1.1 · L14 · Análise crítica: desbalanceamento de classes, custos assimétricos de erro e métrica única enganosa
- 1.1 · L15 · Distinção entre avaliação supervisionada e não supervisionada: critérios objetivos versus validação interna
- 1.4 · L30 · Hastie, Tibshirani & Friedman, The Elements of Statistical Learning (verificar edição)
- 1.4 · L31 · Bishop, Pattern Recognition and Machine Learning (2006)
- 1.4 · L32 · Murphy, Machine Learning: A Probabilistic Perspective (2012)
- 1.5 · L47 · Casos-limite: desbalanceamento, data leakage, overfitting em alta dimensão e validação inadequada

### 5.5 Exigências parcialmente atendidas ou ausentes

"Efeito oficial" é o efeito provável da omissão na ficha da UFC, não no DeepSeek.

| L | Item | Exigência DeepSeek | Situação | Efeito oficial provável | Decisão |
|---|---|---|---|---|---|
| 8 | 1.1 | Risco esperado, risco empírico e minimização do risco empírico (ERM); função de… | Parcial (0,75) | moderado | Fazer (P5-A) |
| 10 | 1.1 | Regularização L1/L2 e seu papel no controle de complexidade | Parcial (0,75) | moderado | Fazer (P5-A) |
| 11 | 1.1 | Validação: holdout, k-fold, validação estratificada e vazamento de dados (data… | Parcial (0,75) | baixo | Não fazer |
| 12 | 1.1 | Métricas de classificação: acurácia, precisão, recall, F1, ROC-AUC e PR-AUC; li… | Parcial (0,75) | baixo | Não fazer |
| 13 | 1.1 | Métricas de regressão: MSE, MAE e R²; interpretação e limitações | Parcial (0,75) | baixo | Não fazer |
| 16 | 1.1 | Quando não usar aprendizado supervisionado (rótulos escassos) ou não supervisio… | Parcial (0,25) | baixo | Não fazer |
| 18 | 1.2 | Regressão linear e regressão logística: hipóteses, funções de custo e estimação | Parcial (0,25) | baixo a moderado | Opcional (P5-O1) |
| 19 | 1.2 | Árvores de decisão: impureza (Gini/entropia), divisão e poda | Parcial (0,25) | baixo | Não fazer |
| 20 | 1.2 | Ensembles: bagging/Random Forest e boosting (AdaBoost/Gradient Boosting) | Parcial (0,25) | moderado | Fazer (P5-B) |
| 21 | 1.2 | SVM: margem máxima, vetores de suporte, kernels e parâmetro C | Parcial (0,25) | baixo | Não fazer |
| 23 | 1.2 | k-means: funcionamento, inicialização k-means++, escolha de k e limitações | Parcial (0,25) | moderado | Fazer (P5-C) |
| 24 | 1.2 | DBSCAN: eps, minPts, ruído e agrupamentos de forma arbitrária | Parcial (0,50) | baixo | Não fazer |
| 25 | 1.2 | PCA: componentes principais, variância explicada e redução de dimensionalidade | Parcial (0,50) | baixo | Não fazer |
| 26 | 1.2 | Avaliação não supervisionada: silhouette, Davies-Bouldin, inércia e limitações | Parcial (0,75) | baixo | Não fazer |
| 33 | 1.4 | James et al., An Introduction to Statistical Learning (verificar edição) | Ausente | baixo | Não fazer |
| 34 | 1.4 | Cortes & Vapnik (1995), Support-Vector Networks | Parcial (0,25) | baixo | Não fazer |
| 35 | 1.4 | Breiman (2001), Random Forests | Parcial (0,25) | baixo | Não fazer |
| 36 | 1.4 | Arthur & Vassilvitskii (2007), k-means++ | Ausente | baixo a moderado | Fazer (P5-C) |
| 37 | 1.4 | Ester et al. (1996), A Density-Based Algorithm for Discovering Clusters (DBSCAN) | Parcial (0,25) | baixo | Não fazer |
| 41 | 1.5 | Formalização de ERM e decomposição viés-variância | Parcial (0,50) | moderado | Fazer (P5-A) |
| 42 | 1.5 | Regularização L1/L2: trade-off entre ajuste e complexidade; seleção de hiperpar… | Parcial (0,75) | moderado | Fazer (P5-A) |
| 44 | 1.5 | k-means: complexidade, sensibilidade à inicialização e escolha de k; papel do k… | Ausente | moderado | Fazer (P5-C) |
| 45 | 1.5 | DBSCAN: sensibilidade a eps/minPts e degradação em alta dimensionalidade | Ausente | baixo | Não fazer |
| 46 | 1.5 | PCA: variância explicada, limite linear e perda de interpretabilidade | Parcial (0,25) | baixo | Não fazer |

### 5.6 Exigências do DeepSeek consideradas excessivas ou pouco pertinentes

- L22 (1.2) · Redes neurais: perceptron/MLP, funções de ativação e backpropagation — Perceptron/backpropagation: pertence a deep learning; uma linha basta aqui.
- L27 (1.2) · k-NN e maldição da dimensionalidade — k-NN e maldição da dimensionalidade: desejável periférico.
- L28 (1.2) · Agrupamento hierárquico: linkage e dendrograma — Linkage e dendrograma: detalhe.
- L38 (1.4) · Documentação atual do scikit-learn (verificar versão) — Documentação do scikit-learn: inexigível.
- L39 (1.4) · Jolliffe, Principal Component Analysis (verificar edição) — Jolliffe: referência especializada.
- L43 (1.5) · SVM: trade-offs de kernels e dos parâmetros C e gamma — Kernels e parâmetros C/γ do SVM: detalhe que custa tempo e convida a erro.
- L48 (1.5) · Relação não trivial entre redução dimensional e clustering/classificação — Desejável periférico.
- L49 (1.5) · Exemplo aplicado: pipeline com validação, escolha de modelo e comparação superv… — Exemplo aplicado extenso.

### 5.7 Erros técnicos encontrados independentemente

Segunda leitura com conhecimento próprio, separada dos critérios DeepSeek.

- Nenhum erro relevante.
- Imprecisão menor (L83): "otimizam funções formais, como … densidade" — o DBSCAN não otimiza função-objetivo; "seguem critérios formais" é exato (microajuste).

### 5.8 Factibilidade em 80 minutos

- **Palavras:** 759 de prosa (inclui títulos) + 68 em 6 diagrama(s)/quadro(s) (21 linhas) + 28 nas referências.
- **Fórmulas:** 2 exibida(s), 46 símbolos; moderada; 11 expressões matemáticas na linha.
- **Planejamento:** ~3 min (esqueleto de seções; o texto está memorizado). **Revisão mínima:** ~5 min.
- **Orçamento de escrita:** ~70 min (80 − 3 − 5 − 2 de folga).

| Versão | Lenta (12 pal/min) | Moderada (15) | Rápida (18) | Risco de não terminar (moderada / lenta) |
|---|---|---|---|---|
| Texto atual | 79,0 min | 63,4 min | 52,9 min | médio / **não cabe** |
| Com as alterações FAZER (e cortes obrigatórios) | 81,7 min | 65,6 min | 54,7 min | médio / **não cabe** |
| … + cortes C1 | 81,7 min | 65,6 min | 54,7 min | médio / **não cabe** |
| … + cortes C1 + C2 | 79,6 min | 63,8 min | 53,3 min | médio / **não cabe** |
| … + cortes C1 + C2 + C3 | 76,6 min | 61,4 min | 51,1 min | baixo / **não cabe** |
| Cenário lento mínimo (só ESSENCIAL/custo zero + todos os cortes) | 70,1 min | 56,2 min | 46,8 min | baixo / **muito alto** (só com revisão encurtada) |

### 5.9 Alterações prioritárias

#### P5-A — Risco empírico explícito e regularização L1/L2

1. **Problema.** A otimização aparece como "arg min L(θ)" abstrato, e a regularização como "erro empírico + λ·complexidade", sem L1/L2.
2. **Evidência.** L24–26 e L42–48; "risco empírico", "L1", "L2", "ridge", "lasso" ausentes.
3. **Justificativa.** Converte duas fórmulas genéricas em formalização precisa (1.1/1.5) por substituição: o texto cresce pouco e passa a mostrar o efeito distinto de L1 (esparsidade) e L2 (encolhimento).
4. **Proposta.** (a) Substituir “minimizando uma função de perda:” e a fórmula seguinte por: “pela **minimização do risco empírico**, isto é, da perda média \(\ell\) na amostra:” seguido de \[\theta^{*} = \arg\min_{\theta}\frac{1}{n}\sum_{i=1}^{n}\ell(f(x_{i};\theta),y_{i})\] (b) Substituir “A regularização penaliza a complexidade:”, o quadro “objetivo = …” e “pois baixo erro de treino não implica boa generalização.” por: “A regularização acrescenta a esse risco uma penalidade \(\lambda\Omega(\theta)\): na **L2** (*ridge*), \(\Omega = \lVert\theta\rVert_{2}^{2}\), que encolhe os coeficientes; na **L1** (*lasso*), \(\Omega = \lVert\theta\rVert_{1}\), que pode zerá-los e induz esparsidade. O hiperparâmetro \(\lambda\), escolhido na validação, controla o compromisso entre ajuste e complexidade.”
5. **Localização.** (a) L22–26: substituir o fim da frase e a fórmula. (b) L42–48: substituir o parágrafo da regularização, incluindo a fórmula textual.
6. **Custo.** +29 palavras no corpo; −1 fórmula(s) exibida(s); +1 símbolos matemáticos. Tempo de escrita (lenta / moderada / rápida): +2,3 / +1,8 / +1,5 min. Memorização: média.
7. **Ganho.** Moderado, confiança moderada: 1.1 (ERM, L1/L2) e 1.5 (formalização). Indicador do modelo da Auditoria 1: +0,20 na leitura central (teto do instrumento). Risco técnico: médio-baixo: memorizar a fórmula com 1/n e a soma. Na dúvida, escrever em palavras ("média das perdas na amostra").
8. **Veredito.** **ALTO CUSTO-BENEFÍCIO**.

#### P5-B — Bagging × boosting ligados ao viés-variância

1. **Problema.** Ensembles aparecem em uma linha genérica ("aumentar robustez e desempenho").
2. **Evidência.** L60.
3. **Justificativa.** Explica o mecanismo dos dois métodos mais usados em dados tabulares e os liga ao compromisso viés-variância já desenvolvido em 5.2. Demonstra domínio (1.1) e ideia fundamental (1.2) por substituição de uma linha.
4. **Proposta.** Substituir “*ensembles*, como **Random Forests** e *boosting*, combinam múltiplos modelos para aumentar robustez e desempenho;” por: “*ensembles* combinam múltiplos modelos: o *bagging* (base das **Random Forests**) treina modelos em amostras *bootstrap* e reduz sobretudo a variância; o *boosting* (ex.: *gradient boosting*) ajusta modelos sequencialmente aos erros dos anteriores e reduz sobretudo o viés;”
5. **Localização.** Substituir o item da lista na L60.
6. **Custo.** +23 palavras no corpo. Tempo de escrita (lenta / moderada / rápida): +1,9 / +1,5 / +1,3 min. Memorização: média.
7. **Ganho.** Moderado a alto (1.2), confiança moderada. Indicador do modelo da Auditoria 1: +0,29 na leitura central (teto do instrumento). Risco técnico: baixo. Manter "sobretudo": boosting também pode reduzir variância.
8. **Veredito.** **ALTO CUSTO-BENEFÍCIO**.

#### P5-C — Mecanismo e limitações do k-means

1. **Problema.** O algoritmo não supervisionado mais conhecido aparece em uma linha.
2. **Evidência.** L77: "k-means, que busca grupos compactos em torno de centroides".
3. **Justificativa.** Uma frase mostra objetivo, algoritmo, hiperparâmetro, sensibilidade à inicialização e viés geométrico: ideia fundamental (1.2) e aprofundamento (1.5) do lado não supervisionado, que hoje é o mais raso.
4. **Proposta.** Substituir “**k-means**, que busca grupos compactos em torno de centroides;” por: “**k-means**, que minimiza a soma das distâncias quadráticas dos pontos ao centroide de seu grupo, alternando atribuição e atualização; exige fixar k (escolhido, por exemplo, pela silhueta), depende da inicialização (mitigada pelo k-means++) e favorece grupos esféricos;”
5. **Localização.** Substituir o item da lista na L77. P5-A, P5-B e P5-C, juntas, exigem os cortes C1 do Ponto 5.
6. **Custo.** +28 palavras no corpo. Tempo de escrita (lenta / moderada / rápida): +2,3 / +1,9 / +1,6 min. Memorização: média.
7. **Ganho.** Moderado (1.2/1.5), confiança moderada. Indicador do modelo da Auditoria 1: +0,40 na leitura central (teto do instrumento). Risco técnico: baixo.
8. **Veredito.** **ALTO CUSTO-BENEFÍCIO**.

**Cortes obrigatórios que pagam estas inserções** (detalhes no relatório 06, seção 3.1):

- P5-C1a (L65–69): remover “A escolha depende, portanto, da hipótese estrutural que o método impõe: [quadro: método = algoritmo + hipótese sobre os dados]”. A L56 já afirma que as famílias "refletem diferentes hipóteses sobre a estrutura dos dados".
- P5-C1b (L116–122): remover “Não existe, portanto, algoritmo universalmente superior. A escolha deve considerar: [quadro: dados + objetivo + hipótese do modelo + métrica + restrições → método] Entre…” → “Não existe, portanto, algoritmo universalmente superior: a escolha depende de dados, objetivo, métrica e restrições como interpretabilidade, latência e custo dos erros.”. Compacta sem perder a tese.

**Opcionais documentados (não entram na lista de execução):**

- **P5-O1 — Regressão logística** (OPCIONAL; ~11 palavras). Texto: “a regressão logística modela \(P(y = 1 \mid x) = \sigma(w^{T}x + b)\) e é ajustada pela entropia cruzada;” Local: Item "modelos lineares" (L58).

**Microajustes de precisão (custo ~0; fora do limite de três):**

- L83: “também otimizam funções formais” → “também seguem critérios formais”. O DBSCAN não otimiza uma função-objetivo; "critérios" é exato para os três exemplos.

### 5.10 Veredito final

**CORRIGIR PONTUALMENTE E ENXUGAR.** Três substituições (P5-A/B/C), pagas pelos cortes C1 do ponto.

## 6. Ponto 6 — Aprendizado por Reforço

Dissertação: `prova-escrita/6-aprendizado-por-reforco_v2.md` · Barema DeepSeek: `prova-escrita/barema-deepseek/ponto-6.note`

### 6.1 Diagnóstico global

O texto mais formal dos dez e o mais caro de escrever (11 fórmulas exibidas). Está correto, mas não há tempo para reproduzi-lo integralmente em 80 min, salvo com escrita rápida. A prioridade é **enxugar redundâncias** (fórmulas e quadros que repetem frases vizinhas) e usar o tempo liberado em duas frases que faltam ao RL moderno (deadly triad/DQN e Monte Carlo × TD).

| Pergunta | Resposta |
|---|---|
| Tese ou objetivo central | RL é decisão sequencial que maximiza retorno de longo prazo; sua prática exige eficiência, estabilidade, segurança e boa especificação da recompensa (L170–172). |
| Fundamentos apresentados? | Sim: MDP, propriedade de Markov, retorno, objetivo, atribuição de crédito (L23–47). |
| O núcleo responde ao tema? | Sim: V/Q, Bellman (expectativa e otimalidade), TD, ε-greedy, Q-learning, SARSA, gradiente de política, actor–critic, model-based/free, deep RL. |
| Sequência lógica? | Sim. |
| Erros técnicos relevantes? | Nenhum relevante; imprecisão menor no ε-greedy (L104). |
| Redundância? | Alta no custo: fórmulas que repetem a frase anterior (L9–11, L31–33) e quadros que repetem fórmulas e o diagrama final (L65–69, L79–81). |
| Aprofundamento compatível? | Alto em formalismo, mas é o texto mais caro de reproduzir; falta análise de estabilidade (deadly triad) e MC × TD. |
| Exemplos ajudam? | Aplicações (robótica, medicina) breves e adequadas. |

### 6.2 Nota anteriormente estimada

- **Auditoria 1:** central **7,8**, intervalo 7,2–8,6.
- **Indicador após as alterações FAZER** (mesmo modelo da Auditoria 1; teto do instrumento, não previsão): central 7,83 → **8,60**; leitura literal (R1) 7,19 → 7,84; viável (R3) 8,65 → 9,50.
- O modelo converte cobertura em pontos de forma mecânica. A direção do efeito é mais confiável que a magnitude, e o ganho oficial tende a ser menor.

### 6.3 Adequação ao barema oficial

| Critério oficial | Avaliação |
|---|---|
| 1.1 | Muito bom. |
| 1.2 | Bom; Monte Carlo e DQN só mencionados. |
| 1.3 / 2.2 | Exemplar. |
| 1.4 | Boa e adequada (Sutton & Barto 2018, Watkins, Williams, Mnih). |
| 1.5 | Formalismo alto, mas sem análise de estabilidade nem MC × TD. |
| 2.1 / 2.3 / 2.4 | Imprecisão menor no ε-greedy. |

### 6.4 Principais exigências do DeepSeek atendidas

15 de 40 subitens atendidos integralmente ou de forma equivalente. As seções 6.4, 6.5 e 6.6 juntas classificam todos os 40 subitens.

- 1.1 · L6 · Definição formal de Processo de Decisão de Markov (MDP): estados, ações, transições, recompensa e fator de de…
- 1.1 · L7 · Política, retorno descontado e funções de valor V^π e Q^π
- 1.1 · L8 · Equações de Bellman esperadas e de otimalidade; relação entre avaliação e melhoria de política
- 1.1 · L9 · Exploração versus exploitation e necessidade de exploração em ambientes desconhecidos
- 1.1 · L10 · Distinção model-based × model-free e on-policy × off-policy
- 1.1 · L11 · Atribuição de crédito, recompensa atrasada, horizonte e papel do fator de desconto
- 1.1 · L12 · Análise crítica: ineficiência amostral, instabilidade, reward hacking e risco de exploração insegura
- 1.1 · L14 · Distinção entre RL e aprendizado supervisionado (fronteira com o Ponto 5)
- 1.2 · L22 · Q-learning (off-policy) e SARSA (on-policy)
- 1.2 · L25 · Policy gradient/REINFORCE e actor-critic
- 1.4 · L30 · Sutton & Barto, Reinforcement Learning: An Introduction (2ª ed., 2018)
- 1.4 · L32 · Watkins & Dayan (1992), Q-learning
- 1.4 · L33 · Mnih et al. (2015), Human-level control through deep reinforcement learning
- 1.4 · L34 · Williams (1992), Simple Statistical Gradient-Following Algorithms for Connectionist Reinforcement Learning
- 1.5 · L47 · Casos-limite: recompensas esparsas, ações contínuas, não estacionariedade e sim-to-real

### 6.5 Exigências parcialmente atendidas ou ausentes

"Efeito oficial" é o efeito provável da omissão na ficha da UFC, não no DeepSeek.

| L | Item | Exigência DeepSeek | Situação | Efeito oficial provável | Decisão |
|---|---|---|---|---|---|
| 13 | 1.1 | Pressupostos de convergência e sensibilidade a hiperparâmetros (gamma, taxa de… | Parcial (0,25) | moderado | Fazer (P6-B) |
| 15 | 1.1 | Quando não usar RL: se há supervisão, planejamento ou bandit simples suficiente | Ausente | baixo | Não fazer |
| 17 | 1.2 | Loop agente-ambiente; episódios versus tarefas contínuas | Parcial (0,75) | baixo | Não fazer |
| 18 | 1.2 | Retorno descontado e políticas determinísticas versus estocásticas | Parcial (0,75) | baixo | Não fazer |
| 19 | 1.2 | Programação dinâmica: avaliação de política, policy iteration e value iteration | Parcial (0,25) | baixo | Não fazer |
| 20 | 1.2 | Monte Carlo: estimação por retornos e variantes primeira visita/todas as visitas | Parcial (0,25) | moderado | Fazer (P6-C) |
| 21 | 1.2 | TD(0): atualização por diferença temporal e comparação com Monte Carlo | Parcial (0,75) | moderado | Fazer (P6-C) |
| 23 | 1.2 | ε-greedy, softmax e decaimento da exploração | Parcial (0,50) | baixo | Não fazer |
| 24 | 1.2 | DQN: aproximação de função, experience replay e target network | Parcial (0,25) | moderado | Fazer (P6-B) |
| 31 | 1.4 | Bellman (1957), Dynamic Programming | Parcial (0,25) | baixo | Não fazer |
| 35 | 1.4 | Schulman et al. (2017), Proximal Policy Optimization Algorithms | Ausente | baixo | Não fazer |
| 40 | 1.5 | Condições de convergência do Q-learning: exploração suficiente, taxas decrescen… | Ausente | baixo a moderado | Opcional (P6-O1) |
| 41 | 1.5 | Deadly triad: aproximação de função, bootstrapping e off-policy | Parcial (0,25) | moderado | Fazer (P6-B) |
| 42 | 1.5 | Trade-off Monte Carlo × TD: viés, variância e eficiência amostral | Ausente | moderado | Fazer (P6-C) |

### 6.6 Exigências do DeepSeek consideradas excessivas ou pouco pertinentes

- L26 (1.2) · Bandit multi-armado: exploração, recompensa e regret — Bandits: tópico vizinho.
- L27 (1.2) · Model-based RL: Dyna e uso de planejamento — Dyna: detalhe.
- L28 (1.2) · Exemplo aplicado canônico (gridworld ou CartPole) — Exemplo canônico extenso.
- L36 (1.4) · Puterman (1994), Markov Decision Processes — Puterman: referência especializada.
- L37 (1.4) · Documentação atual de Gymnasium, Stable-Baselines3 e RLlib (verificar versões) — Documentação de bibliotecas: inexigível.
- L39 (1.5) · Operador de Bellman como contração e convergência de métodos de valor — Contração do operador de Bellman: prova, não cabe em 80 min.
- L43 (1.5) · Exploração formal: regret, UCB e Thompson sampling em bandits — Regret, UCB, Thompson sampling: tópico de bandits.
- L44 (1.5) · Reward shaping e shaping baseado em potenciais — Shaping baseado em potencial: detalhe.
- L45 (1.5) · Superestimação no DQN e Double DQN — Double DQN: detalhe.
- L46 (1.5) · PPO: objetivo truncado e trade-offs entre estabilidade e eficiência amostral — Objetivo truncado do PPO: fórmula longa com risco de erro.
- L48 (1.5) · Exemplo aprofundado: comparação Q-learning × policy gradient em ambiente com re… — Exemplo comparativo extenso.

### 6.7 Erros técnicos encontrados independentemente

Segunda leitura com conhecimento próprio, separada dos critérios DeepSeek.

- Nenhum erro relevante. γ ∈ [0,1) está correto para horizonte infinito; Bellman, TD e Q-learning estão corretos.
- Imprecisão menor (L104): "explora-se outra alternativa" sugere excluir a ação gulosa; no ε-greedy usual, sorteia-se entre todas (microajuste).

### 6.8 Factibilidade em 80 minutos

- **Palavras:** 766 de prosa (inclui títulos) + 31 em 5 diagrama(s)/quadro(s) (13 linhas) + 34 nas referências.
- **Fórmulas:** 11 exibida(s), 294 símbolos; alta; 25 expressões matemáticas na linha.
- **Planejamento:** ~3 min (esqueleto de seções; o texto está memorizado). **Revisão mínima:** ~5 min.
- **Orçamento de escrita:** ~70 min (80 − 3 − 5 − 2 de folga).

| Versão | Lenta (12 pal/min) | Moderada (15) | Rápida (18) | Risco de não terminar (moderada / lenta) |
|---|---|---|---|---|
| Texto atual | 87,3 min | 69,9 min | 58,0 min | alto / **não cabe** |
| Com as alterações FAZER (e cortes obrigatórios) | 84,5 min | 67,7 min | 56,1 min | alto / **não cabe** |
| … + cortes C1 | 84,5 min | 67,7 min | 56,1 min | alto / **não cabe** |
| … + cortes C1 + C2 | 80,6 min | 64,6 min | 53,6 min | médio / **não cabe** |
| … + cortes C1 + C2 + C3 | 79,0 min | 63,2 min | 52,4 min | médio / **não cabe** |
| Cenário lento mínimo (só ESSENCIAL/custo zero + todos os cortes) | 72,8 min | 58,3 min | 48,3 min | baixo / **muito alto** (só com revisão encurtada) |

### 6.9 Alterações prioritárias

#### P6-A — Enxugar: retirar duas fórmulas, dois quadros e uma lista redundantes

1. **Problema.** É o texto mais caro de escrever (11 fórmulas exibidas). Na hipótese moderada, consome cerca de 70 min só de escrita, sem folga para revisão; na lenta, cerca de 87 min.
2. **Evidência.** Fórmulas L9–11 e L31–33 repetem a frase anterior; os quadros L65–69 e L79–81 repetem o diagrama final e a fórmula de Bellman; a lista L143–148 repete a L150; a L172 repete a L170.
3. **Justificativa.** O item 16.8 elimina quem deixar o ponto incompleto. Cortar redundâncias não tira nenhum conceito e libera cerca de 7 min na hipótese moderada (9 min na lenta), que pagam P6-B e P6-C com sobra.
4. **Proposta.** Cortes sem perda conceitual, na ordem do texto: (1) L7: terminar a frase em ponto e apagar a fórmula L9–11. (2) L29: terminar em "...o futuro independe da história anterior." e apagar a fórmula L31–33. (3) Apagar L65–69. (4) Apagar o quadro L79–81. (5) Apagar "Também existem importantes trade-offs:" e a lista L143–148. (6) L172: trocar a frase por "Sua aplicação prática, porém, exige eficiência amostral, estabilidade, segurança e especificação cuidadosa da recompensa."
5. **Localização.** Indicada no item 4.
6. **Custo.** −67 palavras no corpo; −2 fórmula(s) exibida(s); −55 símbolos matemáticos. Tempo de escrita (lenta / moderada / rápida): −8,9 / −7,2 / −5,9 min. Memorização: nenhuma (é corte).
7. **Ganho.** Indireto e alto: viabiliza a conclusão do ponto em 80 min. Não altera a cobertura conceitual (as ideias continuam nas frases vizinhas). Indicador do modelo da Auditoria 1: +0,00 na leitura central (teto do instrumento). Risco técnico: nenhum conceitual.
8. **Veredito.** **ESSENCIAL**.

#### P6-B — Deadly triad e estabilização do DQN

1. **Problema.** O Deep RL é apresentado só pelo alcance ("alta dimensionalidade"), sem a razão da instabilidade nem os mecanismos que a contornaram.
2. **Evidência.** L127 e L150 ("pode introduzir instabilidade"); "deadly triad", "replay", "target" ausentes.
3. **Justificativa.** Transforma uma menção vaga em análise causal: o que torna o RL profundo instável e como o DQN [4] o estabilizou. É o aprofundamento (1.5) mais esperado em RL moderno, ligado a duas referências já citadas.
4. **Proposta.** Substituir “Com aproximadores de função, especialmente redes neurais, essas ideias originam o **Deep Reinforcement Learning** [4], que permite atuar em espaços de estado de alta dimensionalidade.” por: “Com redes neurais como aproximadores de função, essas ideias originam o **Deep Reinforcement Learning**. A combinação de aproximação de função, *bootstrapping* e aprendizado *off-policy* — a *deadly triad* [1] — pode tornar o treinamento instável ou divergente; o DQN [4] estabilizou o Q-learning profundo com *experience replay*, que reutiliza transições armazenadas, e *target network*, que mantém o alvo fixo por intervalos.”
5. **Localização.** Substituir a frase da L127.
6. **Custo.** +34 palavras no corpo. Tempo de escrita (lenta / moderada / rápida): +2,8 / +2,3 / +1,9 min. Memorização: média.
7. **Ganho.** Moderado a alto (1.5/1.2), confiança moderada. Indicador do modelo da Auditoria 1: +0,46 na leitura central (teto do instrumento). Risco técnico: baixo. A deadly triad indica risco de divergência, não divergência garantida ("pode").
8. **Veredito.** **ALTO CUSTO-BENEFÍCIO**.

#### P6-C — Monte Carlo × TD (viés e variância)

1. **Problema.** O TD é definido pelo bootstrapping, mas falta o contraponto clássico (Monte Carlo) e o compromisso viés-variância entre os dois.
2. **Evidência.** L95; "Monte Carlo" ausente.
3. **Justificativa.** MC × TD é comparação central de qualquer curso de RL (1.2) e mostra compreensão do bootstrapping (1.5). Uma frase.
4. **Proposta.** Inserir: “Já os métodos de **Monte Carlo** atualizam com o retorno completo \(G_{t}\): a estimativa não tem viés, mas tem maior variância e só fica disponível ao fim do episódio; o TD troca algum viés por menor variância e aprendizado incremental.”
5. **Localização.** Depois da L95 (após "...sem aguardar o término do episódio.").
6. **Custo.** +39 palavras no corpo; +2 símbolos matemáticos. Tempo de escrita (lenta / moderada / rápida): +3,3 / +2,7 / +2,2 min. Memorização: média.
7. **Ganho.** Moderado (1.2/1.5), confiança moderada a alta. Indicador do modelo da Auditoria 1: +0,32 na leitura central (teto do instrumento). Risco técnico: baixo.
8. **Veredito.** **ALTO CUSTO-BENEFÍCIO**.

**Opcionais documentados (não entram na lista de execução):**

- **P6-O1 — Condições de convergência do Q-learning** (OPCIONAL; ~25 palavras). Texto: “Em MDPs finitos, o Q-learning converge para \(Q^{*}\) se todos os pares \((s,a)\) forem visitados infinitas vezes e as taxas satisfizerem \(\sum\alpha_{t} = \infty\) e \(\sum\alpha_{t}^{2} < \infty\) [2].” Local: Depois da L116.
- **P6-O2 — RLHF como exemplo atual de especificação de recompensa** (OPCIONAL; ~27 palavras). Texto: “Hoje, o RL com feedback humano (RLHF) ajusta grandes modelos de linguagem a um modelo de recompensa aprendido, o que torna o *reward hacking* um problema prático.” Local: Depois da L141.

**Microajustes de precisão (custo ~0; fora do limite de três):**

- L104: “explora-se outra alternativa” → “escolhe-se uma ação ao acaso”. No ε-greedy usual, a ação aleatória é sorteada entre todas (pode coincidir com a gulosa).

### 6.10 Veredito final

**ENXUGAR.** O corte P6-A é obrigatório; P6-B e P6-C cabem no tempo liberado.

## 7. Ponto 7 — MLOps: Desenvolvimento, Versionamento e Experimentação de Modelos

Dissertação: `prova-escrita/7-mlops-desenvolvimento-versionamento-e-experimentacao-de-modelos_v2.md` · Barema DeepSeek: `prova-escrita/barema-deepseek/ponto-7.note`

### 7.1 Diagnóstico global

Texto conceitualmente coeso (resultado + proveniência), com a bibliografia mais atual do conjunto. Falta a experimentação propriamente dita (busca de hiperparâmetros e o risco de superajuste à validação/benchmark) e qualquer ancoragem prática (ferramentas). Há dois diagramas de fluxo quase idênticos.

| Pergunta | Resposta |
|---|---|
| Tese ou objetivo central | Experimento confiável = resultado + proveniência; MLOps de desenvolvimento torna a experimentação rastreável, comparável e reprodutível até um candidato validado (L31–33, L147). |
| Fundamentos apresentados? | Sim: experimento como unidade (entradas, procedimento, saídas, metadados) (L21–33). |
| O núcleo responde ao tema? | Em versionamento, tracking, reprodutibilidade e validação, sim. Em "experimentação", falta a busca de hiperparâmetros; em prática, nenhuma ferramenta. |
| Sequência lógica? | Sim. |
| Erros técnicos relevantes? | Nenhum. "Reprodutibilidade ≈ D + C + H + E + S" é pseudoformal (micro). |
| Redundância? | Dois diagramas de fluxo quase iguais (L91–101 e conclusão) e dois quadros finais. |
| Aprofundamento compatível? | Sim; "reprodutível ≠ idêntico bit a bit" é um ponto fino e correto. |
| Exemplos ajudam? | A cadeia de linhagem (L45–47) ajuda. |

### 7.2 Nota anteriormente estimada

- **Auditoria 1:** central **7,5**, intervalo 6,7–8,6.
- **Indicador após as alterações FAZER** (mesmo modelo da Auditoria 1; teto do instrumento, não previsão): central 7,50 → **8,13**; leitura literal (R1) 6,68 → 7,21; viável (R3) 8,60 → 9,29.
- O modelo converte cobertura em pontos de forma mecânica. A direção do efeito é mais confiável que a magnitude, e o ganho oficial tende a ser menor.

### 7.3 Adequação ao barema oficial

| Critério oficial | Avaliação |
|---|---|
| 1.1 | Bom; falta a crítica do vazamento por seleção repetida. |
| 1.2 | Perde por ausência de prática (ferramentas, busca de hiperparâmetros). |
| 1.3 / 2.2 | Exemplar. |
| 1.4 | A mais atual do conjunto (2015–2023). |
| 1.5 | Bom. |
| 2.1 / 2.3 / 2.4 | Sem problemas. |

### 7.4 Principais exigências do DeepSeek atendidas

9 de 36 subitens atendidos integralmente ou de forma equivalente. As seções 7.4, 7.5 e 7.6 juntas classificam todos os 36 subitens.

- 1.1 · L8 · Reprodutibilidade formal: determinismo, sementes, ambientes, linhagem e artefatos imutáveis
- 1.1 · L9 · Versionamento de código, dados, modelo, configuração e ambiente; identificação e rastreabilidade
- 1.1 · L10 · Experimentação: hipótese, variáveis, métricas, validação e comparação justa de experimentos
- 1.2 · L19 · Versionamento de modelos e artefatos: model registry, metadados, estágios e linhagem
- 1.2 · L24 · Testes de dados e validação de esquema
- 1.4 · L26 · Sculley et al. (2015), Hidden Technical Debt in Machine Learning Systems
- 1.4 · L27 · Breck et al. (2017), The ML Test Score
- 1.5 · L37 · Formalização da reprodutibilidade: mesma tupla (código, dados, ambiente, hiperparâmetros, seed) produz o mesm…
- 1.5 · L38 · Linhagem e grafo de dependências entre datasets, runs e modelos; auditoria

### 7.5 Exigências parcialmente atendidas ou ausentes

"Efeito oficial" é o efeito provável da omissão na ficha da UFC, não no DeepSeek.

| L | Item | Exigência DeepSeek | Situação | Efeito oficial provável | Decisão |
|---|---|---|---|---|---|
| 6 | 1.1 | Definição formal de MLOps e delimitação do escopo de desenvolvimento, versionam… | Parcial (0,75) | baixo | Não fazer |
| 7 | 1.1 | Ciclo de vida de ML e diferenças em relação ao software tradicional: dados como… | Parcial (0,75) | baixo | Não fazer |
| 11 | 1.1 | Dívida técnica em ML: entanglement, undeclared consumers, pipeline jungles e gl… | Parcial (0,25) | baixo a moderado | Se houver tempo (P7-C) |
| 12 | 1.1 | Análise crítica: vazamento de dados, overfitting de benchmark, seleção enviesad… | Parcial (0,50) | moderado | Fazer (P7-A) |
| 15 | 1.2 | Processo CRISP-DM e ciclo iterativo de desenvolvimento de modelos | Parcial (0,50) | baixo | Não fazer |
| 17 | 1.2 | Controle de versão de código com Git e boas práticas de branches, commits e tags | Parcial (0,25) | moderado | Fazer (P7-B) |
| 18 | 1.2 | Versionamento de dados: DVC, hashes, armazenamento remoto e reprodutibilidade | Parcial (0,50) | moderado | Fazer (P7-B) |
| 20 | 1.2 | Rastreamento de experimentos: parâmetros, métricas, artefatos, runs e comparaçã… | Parcial (0,75) | moderado | Fazer (P7-B) |
| 21 | 1.2 | Gestão de hiperparâmetros: grid/random/Bayesian optimization e registro dos tri… | Parcial (0,25) | moderado | Fazer (P7-A) |
| 22 | 1.2 | Ambientes reprodutíveis: dependências, containers, seeds e configuração | Parcial (0,75) | baixo | Não fazer |
| 23 | 1.2 | Documentação de experimentos e model cards | Parcial (0,25) | baixo | Não fazer |
| 28 | 1.4 | Zaharia et al. (2018), Accelerating the Machine Learning Lifecycle with MLflow | Parcial (0,25) | baixo a moderado | Fazer (P7-B) |
| 29 | 1.4 | Shearer (2000), CRISP-DM | Ausente | baixo | Não fazer |
| 30 | 1.4 | Mitchell et al. (2019), Model Cards for Model Reporting | Ausente | baixo | Não fazer |
| 31 | 1.4 | Gebru et al. (2021), Datasheets for Datasets | Ausente | baixo | Não fazer |
| 39 | 1.5 | Trade-offs: tracking detalhado versus overhead; registry centralizado versus au… | Parcial (0,75) | baixo | Não fazer |
| 40 | 1.5 | Casos-limite: dados mutáveis, dependências não fixadas, seeds não controladas,… | Parcial (0,75) | baixo | Não fazer |
| 41 | 1.5 | Comparação justa de experimentos: mesmos splits, mesma métrica, controle de var… | Parcial (0,75) | baixo | Não fazer |
| 42 | 1.5 | Relação entre versionamento de dados e vazamento temporal/leakage | Ausente | baixo | Não fazer |
| 43 | 1.5 | Estratégias de tuning: espaço de busca, orçamento e early stopping | Ausente | moderado | Fazer (P7-A) |

### 7.6 Exigências do DeepSeek consideradas excessivas ou pouco pertinentes

- L13 (1.1) · Distinção entre avaliação offline e online (fronteira com o Ponto 9) — Avaliação offline × online: fora do recorte declarado (L17); pertence ao Ponto 9.
- L16 (1.2) · Estruturação de projeto: organização de código, notebooks versus scripts, módul… — Notebooks × scripts: prática de engenharia, periférica.
- L32 (1.4) · Vartak et al. (2016), ModelDB — ModelDB: referência histórica especializada.
- L33 (1.4) · Snoek et al. (2012), Practical Bayesian Optimization of Machine Learning Algori… — Snoek et al.: referência especializada.
- L34 (1.4) · Documentação atual de Git, DVC, MLflow, Weights & Biases e TensorBoard (verific… — Documentação com versão: inexigível.
- L35 (1.4) · Pineau et al., Machine Learning Reproducibility Checklist (verificar) — Checklist de reprodutibilidade: periférico.
- L44 (1.5) · Exemplo aplicado: pipeline reprodutível com Git + DVC + MLflow e registro de mo… — Exemplo aplicado extenso.

### 7.7 Erros técnicos encontrados independentemente

Segunda leitura com conhecimento próprio, separada dos critérios DeepSeek.

- Nenhum erro.
- "reprodutibilidade ≈ D + C + H + E + S" é mnemônico, não equação; uma banca rigorosa pode ver a soma como pseudoformal. "execução = f(D, C, H, E, S)" diz o que o texto quer dizer (microajuste).

### 7.8 Factibilidade em 80 minutos

- **Palavras:** 733 de prosa (inclui títulos) + 57 em 9 diagrama(s)/quadro(s) (27 linhas) + 30 nas referências.
- **Fórmulas:** 1 exibida(s), 27 símbolos; simples; 5 expressões matemáticas na linha.
- **Planejamento:** ~3 min (esqueleto de seções; o texto está memorizado). **Revisão mínima:** ~5 min.
- **Orçamento de escrita:** ~70 min (80 − 3 − 5 − 2 de folga).

| Versão | Lenta (12 pal/min) | Moderada (15) | Rápida (18) | Risco de não terminar (moderada / lenta) |
|---|---|---|---|---|
| Texto atual | 74,5 min | 59,9 min | 50,1 min | baixo / **muito alto** (só com revisão encurtada) |
| Com as alterações FAZER (e cortes obrigatórios) | 79,2 min | 63,6 min | 53,2 min | médio / **não cabe** |
| … + cortes C1 | 75,1 min | 60,3 min | 50,3 min | baixo / **não cabe** |
| … + cortes C1 + C2 | 73,5 min | 58,9 min | 49,2 min | baixo / **muito alto** (só com revisão encurtada) |
| … + cortes C1 + C2 + C3 | 71,6 min | 57,3 min | 47,7 min | baixo / **muito alto** (só com revisão encurtada) |
| Cenário lento mínimo (só ESSENCIAL/custo zero + todos os cortes) | 66,9 min | 53,6 min | 44,6 min | baixo / médio |

### 7.9 Alterações prioritárias

#### P7-A — Busca de hiperparâmetros e superajuste à validação/benchmark

1. **Problema.** A "experimentação" do título não trata da principal atividade experimental (busca de hiperparâmetros) nem do vazamento por seleção repetida.
2. **Evidência.** L51–63 e L83–89; "grade", "bayesian", "trial", "benchmark", "vazamento" ausentes.
3. **Justificativa.** Dá conteúdo metodológico à experimentação (1.2) e acrescenta análise crítica (1.1): o uso repetido do teste ou de um benchmark superestima o desempenho.
4. **Proposta.** Inserir: “A busca de hiperparâmetros — em grade, aleatória ou bayesiana — é parte da experimentação: cada tentativa deve ser registrada e comparada apenas na validação, pois consultar repetidamente o conjunto de teste, ou ajustar-se a um mesmo *benchmark*, superestima o desempenho real.”
5. **Localização.** Novo parágrafo depois da L89 (antes do diagrama "EXPERIMENTO ↓ ...").
6. **Custo.** +40 palavras no corpo. Tempo de escrita (lenta / moderada / rápida): +3,3 / +2,7 / +2,2 min. Memorização: média.
7. **Ganho.** Moderado (1.2 + 1.1), confiança moderada. Indicador do modelo da Auditoria 1: +0,38 na leitura central (teto do instrumento). Risco técnico: baixo.
8. **Veredito.** **ALTO CUSTO-BENEFÍCIO**.

#### P7-B — Exemplos de ferramentas (Git, DVC, MLflow)

1. **Problema.** O texto é inteiramente agnóstico de ferramentas, embora o tema seja prático.
2. **Evidência.** Busca por "Git", "DVC", "MLflow": nenhuma ocorrência.
3. **Justificativa.** Uma frase de 15 palavras ancora os princípios em práticas reconhecíveis (1.2 e 1.4: atualização), sem virar tutorial.
4. **Proposta.** Inserir: “Na prática, ferramentas como Git (código), DVC (dados) e MLflow (*tracking* e *registry*) materializam esse controle.”
5. **Localização.** Final de 7.3.2, depois da L63.
6. **Custo.** +16 palavras no corpo. Tempo de escrita (lenta / moderada / rápida): +1,3 / +1,1 / +0,9 min. Memorização: baixa.
7. **Ganho.** Baixo a moderado, confiança moderada (depende do perfil da banca). Indicador do modelo da Auditoria 1: +0,25 na leitura central (teto do instrumento). Risco técnico: nenhum.
8. **Veredito.** **ALTO CUSTO-BENEFÍCIO**.

**Opcionais documentados (não entram na lista de execução):**

- **P7-C — CACE e dívida técnica (Sculley et al.)** (OPCIONAL; +30 palavras). Dá à citação [1] seu conteúdo próprio (1.4) e reforça a justificativa do versionamento (1.1). Texto: “Sculley et al. [1] chamam esse entrelaçamento de CACE (*changing anything changes everything*): alterar uma *feature*, um dado ou um hiperparâmetro pode mudar todo o modelo, gerando dívida técnica oculta.” Local: Depois do quadro da L9–11.

**Microajustes de precisão (custo ~0; fora do limite de três):**

- L70: “reprodutibilidade ≈ D + C + H + E + S” → “execução = f(D, C, H, E, S)”. A soma é só mnemônica; a notação de função diz que a execução é determinada pela tupla, como no próprio texto.

### 7.10 Veredito final

**CORRIGIR PONTUALMENTE.** Duas inserções curtas (P7-A, P7-B).

## 8. Ponto 8 — MLOps: Automação, Implantação e Infraestrutura de Aprendizado de Máquina

Dissertação: `prova-escrita/8-mlops-automacao-implantacao-e-infraestrutura-de-aprendizado-de-maquina_v2.md` · Barema DeepSeek: `prova-escrita/barema-deepseek/ponto-8.note`

### 8.1 Diagnóstico global

Boa progressão (automação → empacotamento → serving → orquestração → escala) e distinções corretas (CI/CD/CT, escalabilidade ≠ disponibilidade). Faltam dois conceitos centrais de infraestrutura de ML: **infraestrutura como código** (ausência total) e **feature store** (o skew é diagnosticado sem a solução padrão). Nenhuma ferramenta é nomeada. É o texto com mais diagramas (10 blocos), vários redundantes.

| Pergunta | Resposta |
|---|---|
| Tese ou objetivo central | Modelo validado ≠ sistema confiável; a infraestrutura deve ser proporcional aos requisitos (L10, L130, L160). |
| Fundamentos apresentados? | Sim: CI, CD, CT e quality gates (L17–31). |
| O núcleo responde ao tema? | Implantação, serving, containers, orquestração e escala, sim. Infraestrutura como código e feature store, não. |
| Sequência lógica? | Sim. |
| Erros técnicos relevantes? | Nenhum. |
| Redundância? | Alta em diagramas: dez blocos, vários repetindo a frase anterior (L88–91, L99–105, L154–158). |
| Aprofundamento compatível? | Adequado em estratégias de release e escala; sem ferramentas nem percentis de latência. |
| Exemplos ajudam? | O diagrama de load balancer é caro de desenhar e pouco informativo. |

### 8.2 Nota anteriormente estimada

- **Auditoria 1:** central **7,0**, intervalo 6,4–8,0.
- **Indicador após as alterações FAZER** (mesmo modelo da Auditoria 1; teto do instrumento, não previsão): central 6,97 → **8,13**; leitura literal (R1) 6,36 → 7,42; viável (R3) 8,00 → 9,27.
- O modelo converte cobertura em pontos de forma mecânica. A direção do efeito é mais confiável que a magnitude, e o ganho oficial tende a ser menor.

### 8.3 Adequação ao barema oficial

| Critério oficial | Avaliação |
|---|---|
| 1.1 | Perde em IaC e feature store. |
| 1.2 | Médio; nenhuma ferramenta, nenhuma orquestração de pipelines. |
| 1.3 / 2.2 | Exemplar. |
| 1.4 | Boa (2015–2023). |
| 1.5 | Médio. |
| 2.1 / 2.3 / 2.4 | Sem problemas. |

### 8.4 Principais exigências do DeepSeek atendidas

6 de 38 subitens atendidos integralmente ou de forma equivalente. As seções 8.4, 8.5 e 8.6 juntas classificam todos os 38 subitens.

- 1.1 · L6 · Definição formal de automação de pipeline de ML e distinção entre CI, CD e Continuous Training (CT)
- 1.1 · L7 · Distinção entre implantação batch, online (tempo real) e streaming; critérios técnicos de escolha
- 1.2 · L22 · Infraestrutura em nuvem e escalabilidade: instâncias, autoscaling, GPUs e balanceamento de carga
- 1.4 · L30 · Treveil et al., Introducing MLOps (2020)
- 1.4 · L31 · Kreuzberger, Kühl & Hirschl (2023), Machine Learning Operations (MLOps): Overview, Definition, and Architectu…
- 1.4 · L33 · Breck et al. (2017), The ML Test Score

### 8.5 Exigências parcialmente atendidas ou ausentes

"Efeito oficial" é o efeito provável da omissão na ficha da UFC, não no DeepSeek.

| L | Item | Exigência DeepSeek | Situação | Efeito oficial provável | Decisão |
|---|---|---|---|---|---|
| 8 | 1.1 | Infraestrutura como código (IaC): declaração, idempotência, versionamento e rep… | Ausente | alto | Fazer (P8-A) |
| 9 | 1.1 | Conteinerização e isolamento de dependências; imagens reprodutíveis e imutáveis | Parcial (0,75) | baixo | Não fazer |
| 10 | 1.1 | Orquestração de pipelines e agendamento de tarefas; dependências e paralelismo | Parcial (0,25) | moderado | Fazer (P8-C) |
| 11 | 1.1 | Serving de modelos: APIs REST/gRPC, inferência em lote versus tempo real e esca… | Parcial (0,75) | baixo | Não fazer |
| 12 | 1.1 | Feature store: definição, consistência treino/serving e camadas online/offline | Parcial (0,25) | moderado | Fazer (P8-B) |
| 13 | 1.1 | Análise crítica: custos, complexidade operacional, vendor lock-in, automação pr… | Parcial (0,75) | baixo | Não fazer |
| 14 | 1.1 | Distinção entre infraestrutura de ML e infraestrutura de software tradicional | Parcial (0,50) | baixo | Não fazer |
| 15 | 1.1 | Quando não automatizar: fase exploratória, baixa frequência de retreino e custo… | Parcial (0,25) | baixo | Não fazer |
| 17 | 1.2 | CI/CD para ML: testes de código, dados e modelo; pipeline automatizado de build… | Parcial (0,75) | baixo | Não fazer |
| 18 | 1.2 | Continuous Training (CT): gatilhos por novos dados, agendamento e drift (fronte… | Parcial (0,75) | baixo | Não fazer |
| 19 | 1.2 | Padrões de implantação: shadow, canário, blue-green e A/B testing | Parcial (0,75) | baixo a moderado | Opcional (P8-O1) |
| 20 | 1.2 | Empacotamento e serving: Docker, Kubernetes, KServe/Seldon e TorchServe/TF Serv… | Parcial (0,50) | moderado | Fazer (P8-C) |
| 21 | 1.2 | Orquestração de pipelines: Airflow, Kubeflow Pipelines e MLflow (fronteira com… | Parcial (0,25) | moderado | Fazer (P8-C) |
| 23 | 1.2 | Feature store: Feast/Tecton e padrões de acesso online/offline | Ausente | moderado | Fazer (P8-B) |
| 24 | 1.2 | Batch scoring e pipelines agendados para inferência em lote | Parcial (0,75) | baixo | Não fazer |
| 25 | 1.2 | API de inferência e contrato de entrada/saída; versionamento de endpoints | Parcial (0,75) | baixo | Não fazer |
| 26 | 1.2 | IaC com Terraform e gestão declarativa de recursos | Ausente | alto | Fazer (P8-A) |
| 29 | 1.4 | Huyen, Designing Machine Learning Systems (2022) | Ausente | baixo | Não fazer |
| 32 | 1.4 | Humble & Farley, Continuous Delivery (2010) | Parcial (0,25) | baixo | Não fazer |
| 39 | 1.5 | Formalização de SLO/SLA de inferência: latência p95/p99, throughput e disponibi… | Parcial (0,25) | baixo a moderado | Opcional (P8-O2) |
| 40 | 1.5 | Trade-offs entre padrões de implantação: canário, blue-green e shadow; risco, c… | Parcial (0,50) | baixo a moderado | Opcional (P8-O1) |
| 42 | 1.5 | Casos-limite: skew treino/serving, falha de feature store e indisponibilidade d… | Parcial (0,75) | moderado | Fazer (P8-B) |
| 43 | 1.5 | Trade-off entre serving online e batch: latência, custo e atualidade das previs… | Parcial (0,75) | baixo | Não fazer |
| 45 | 1.5 | Relação entre IaC e reprodutibilidade; detecção de drift de infraestrutura | Ausente | moderado | Fazer (P8-A) |

### 8.6 Exigências do DeepSeek consideradas excessivas ou pouco pertinentes

- L27 (1.2) · Edge deployment e otimização de modelos (quantização, pruning) — Edge e quantização: tema vizinho.
- L34 (1.4) · Documentação atual de Kubernetes, Docker e Terraform (verificar versões) — Documentação com versão: inexigível.
- L35 (1.4) · Documentação atual de Kubeflow, Feast, KServe/Seldon e TorchServe/TF Serving (v… — Documentação com versão: inexigível.
- L36 (1.4) · MLPerf Inference benchmark (verificar versão) — MLPerf: benchmark, inexigível.
- L37 (1.4) · Sato, Wider & Windheuser (2019), Continuous Delivery for Machine Learning (veri… — Sato et al.: referência especializada.
- L41 (1.5) · Autoscaling e custo: cold start, scale-to-zero, utilização de GPU e elasticidade — Cold start, scale-to-zero, GPU: detalhe de plataforma.
- L44 (1.5) · Segurança e isolamento multi-tenant; supply chain de imagens e assinatura de ar… — Supply chain e assinatura de imagens: segurança, periférico.
- L46 (1.5) · Exemplo aplicado: pipeline CI/CD/CT com implantação canário e rollback automati… — Exemplo aplicado extenso.

### 8.7 Erros técnicos encontrados independentemente

Segunda leitura com conhecimento próprio, separada dos critérios DeepSeek.

- Nenhum erro. "Entrega ou Implantação Contínua" agrupa continuous delivery e deployment; aceitável com a disjunção explícita.
- Trade-off essencial pouco explorado: latência média × cauda (p95/p99), que é como SLOs de inferência são definidos (opcional P8-O2).

### 8.8 Factibilidade em 80 minutos

- **Palavras:** 721 de prosa (inclui títulos) + 65 em 10 diagrama(s)/quadro(s) (27 linhas) + 30 nas referências.
- **Fórmulas:** nenhuma; 0 expressões matemáticas na linha.
- **Planejamento:** ~3 min (esqueleto de seções; o texto está memorizado). **Revisão mínima:** ~5 min.
- **Orçamento de escrita:** ~70 min (80 − 3 − 5 − 2 de folga).

| Versão | Lenta (12 pal/min) | Moderada (15) | Rápida (18) | Risco de não terminar (moderada / lenta) |
|---|---|---|---|---|
| Texto atual | 73,4 min | 59,0 min | 49,4 min | baixo / **muito alto** (só com revisão encurtada) |
| Com as alterações FAZER (e cortes obrigatórios) | 80,1 min | 64,3 min | 53,9 min | médio / **não cabe** |
| … + cortes C1 | 76,0 min | 61,0 min | 51,0 min | baixo / **não cabe** |
| … + cortes C1 + C2 | 74,9 min | 60,1 min | 50,2 min | baixo / **muito alto** (só com revisão encurtada) |
| … + cortes C1 + C2 + C3 | 72,3 min | 57,9 min | 48,3 min | baixo / **muito alto** (só com revisão encurtada) |
| Cenário lento mínimo (só ESSENCIAL/custo zero + todos os cortes) | 68,6 min | 54,9 min | 45,8 min | baixo / alto |

### 8.9 Alterações prioritárias

#### P8-A — Infraestrutura como código (IaC)

1. **Problema.** O ponto "Automação, Implantação e Infraestrutura" não menciona a automação da própria infraestrutura.
2. **Evidência.** Busca por "IaC", "infraestrutura como código", "Terraform", "declarativ": nenhuma ocorrência. 8.3.3 trata a infraestrutura como recursos (CPU, GPU), não como artefato versionado.
3. **Justificativa.** IaC é o elo entre os dois termos do título (automação e infraestrutura) e a base da reprodutibilidade de ambientes. Sua ausência total é uma lacuna de ideia fundamental (1.2) e de domínio (1.1).
4. **Proposta.** Inserir: “A própria infraestrutura deve ser declarada como código (**IaC**, *Infrastructure as Code*), com ferramentas como Terraform: versionada, revisada e aplicada de forma idempotente, ela torna os ambientes reprodutíveis e auditáveis e evita configurações manuais divergentes.”
5. **Localização.** Novo parágrafo no início de 8.3.3, depois da L82.
6. **Custo.** +35 palavras no corpo. Tempo de escrita (lenta / moderada / rápida): +2,9 / +2,3 / +1,9 min. Memorização: média.
7. **Ganho.** Alto, confiança moderada. Indicador do modelo da Auditoria 1: +0,46 na leitura central (teto do instrumento). Risco técnico: baixo. Idempotência: aplicar a mesma declaração de novo não muda o estado já alcançado.
8. **Veredito.** **ESSENCIAL**.

#### P8-B — Feature store como resposta ao training-serving skew

1. **Problema.** O texto diagnostica o skew, mas não apresenta a solução arquitetural padrão.
2. **Evidência.** L76–78; "feature store" ausente.
3. **Justificativa.** Completa o raciocínio problema → solução (1.1) e cobre um componente de infraestrutura de ML (1.2), em uma frase.
4. **Proposta.** Inserir: “*Feature stores* reduzem esse risco ao centralizar a definição das *features* e servi-las de forma consistente ao treinamento (camada *offline*, histórica) e à inferência (camada *online*, de baixa latência).”
5. **Localização.** Depois da L78 (após "...compatíveis entre treinamento e produção.").
6. **Custo.** +29 palavras no corpo. Tempo de escrita (lenta / moderada / rápida): +2,4 / +1,9 / +1,6 min. Memorização: média.
7. **Ganho.** Moderado, confiança moderada. Indicador do modelo da Auditoria 1: +0,36 na leitura central (teto do instrumento). Risco técnico: baixo.
8. **Veredito.** **ALTO CUSTO-BENEFÍCIO**.

#### P8-C — Nomear ferramentas canônicas (Airflow/Kubeflow, Docker, Kubernetes)

1. **Problema.** Nenhuma ferramenta é nomeada, e a orquestração de pipelines (diferente da de containers) não aparece.
2. **Evidência.** L19, L45, L86.
3. **Justificativa.** Com cerca de 15 palavras, a banca reconhece a prática atual (1.4: atualização; 1.2) e passa a ver a distinção entre orquestrar pipelines e orquestrar containers.
4. **Proposta.** Microinserções: (a) L19: acrescentar ao fim da frase ", em geral orquestrados como DAGs por ferramentas como Airflow ou Kubeflow Pipelines". (b) L45: "**Containers** empacotam" → "**Containers** (ex.: Docker) empacotam". (c) L86: "entra a **orquestração**, que" → "entra a **orquestração** (ex.: Kubernetes), que".
5. **Localização.** Indicada no item 4.
6. **Custo.** +16 palavras no corpo. Tempo de escrita (lenta / moderada / rápida): +1,3 / +1,1 / +0,9 min. Memorização: baixa.
7. **Ganho.** Moderado, confiança moderada. Indicador do modelo da Auditoria 1: +0,35 na leitura central (teto do instrumento). Risco técnico: nenhum.
8. **Veredito.** **ALTO CUSTO-BENEFÍCIO**.

**Opcionais documentados (não entram na lista de execução):**

- **P8-O1 — Shadow deployment** (OPCIONAL; ~14 palavras). Texto: “- **shadow**: a nova versão recebe cópia do tráfego real sem afetar as respostas;” Local: Lista de estratégias (após L52).
- **P8-O2 — Latência por percentis** (OPCIONAL; ~13 palavras). Texto: “A latência deve ser acompanhada por percentis (p95, p99), não só pela média.” Local: Final da L74.

### 8.10 Veredito final

**CORRIGIR PONTUALMENTE.** Uma inserção essencial (P8-A), uma frase (P8-B) e três microinserções (P8-C).

## 9. Ponto 9 — MLOps: Monitoramento, Governança e Manutenção de Modelos

Dissertação: `prova-escrita/9-mlops-monitoramento-governanca-e-manutencao-de-modelos_v2.md` · Barema DeepSeek: `prova-escrita/barema-deepseek/ponto-9.note`

### 9.1 Diagnóstico global

Texto forte e preciso (data × concept drift, covariate shift, label delay, segmentação, champion–challenger, retreino orientado por diagnóstico). A lacuna é a ausência de **qualquer marco normativo** num ponto de governança, justamente onde o critério 1.4 fala em "normas". A ideia "detecção ≠ ação automática" aparece três vezes.

| Pergunta | Resposta |
|---|---|
| Tese ou objetivo central | Modelo implantado ≠ permanentemente válido; observar → diagnosticar → agir, sob governança proporcional ao risco (L10, L155). |
| Fundamentos apresentados? | Sim: monitoramento operacional × de ML, observabilidade, SLI/SLO (L19–31). |
| O núcleo responde ao tema? | Sim, com amplitude: qualidade, data/concept drift, covariate shift, label delay, thresholds, segmentos, governança, lineage, auditoria, manutenção, champion–challenger. |
| Sequência lógica? | Sim. |
| Erros técnicos relevantes? | Nenhum. |
| Redundância? | Moderada: "detecção ≠ ação automática" aparece três vezes (L74, L94–98, L121–125); dois quadros finais. |
| Aprofundamento compatível? | Sim, alto. |
| Exemplos ajudam? | O da coluna corrompida (L98) é excelente. |

### 9.2 Nota anteriormente estimada

- **Auditoria 1:** central **8,3**, intervalo 7,7–9,3.
- **Indicador após as alterações FAZER** (mesmo modelo da Auditoria 1; teto do instrumento, não previsão): central 8,33 → **8,95**; leitura literal (R1) 7,74 → 8,28; viável (R3) 9,26 → 9,83.
- O modelo converte cobertura em pontos de forma mecânica. A direção do efeito é mais confiável que a magnitude, e o ganho oficial tende a ser menor.

### 9.3 Adequação ao barema oficial

| Critério oficial | Avaliação |
|---|---|
| 1.1 | Muito bom. |
| 1.2 | Bom; testes de drift só genéricos. |
| 1.3 / 2.2 | Exemplar. |
| 1.4 | Sem nenhuma norma ou marco regulatório: a lacuna mais clara em relação à redação oficial do item. |
| 1.5 | Muito bom. |
| 2.1 / 2.3 / 2.4 | Sem problemas. |

### 9.4 Principais exigências do DeepSeek atendidas

12 de 38 subitens atendidos integralmente ou de forma equivalente. As seções 9.4, 9.5 e 9.6 juntas classificam todos os 38 subitens.

- 1.1 · L6 · Definição formal de monitoramento de modelos e distinção de observabilidade (métricas, logs e traces)
- 1.1 · L9 · Métricas de desempenho em produção e problema do atraso de rótulos (label delay)
- 1.1 · L10 · Governança de ML: definição, papéis, accountability, políticas e gestão de risco
- 1.1 · L14 · Quando não retreinar automaticamente: riscos de feedback loops, degradação silenciosa e instabilidade
- 1.2 · L17 · Métricas operacionais: latência, throughput, taxa de erros, disponibilidade e uso de recursos
- 1.2 · L20 · Monitoramento de performance: métricas de modelo, janelas, segmentação e label delay
- 1.2 · L25 · Manutenção: retreino agendado/por gatilho, rollback, aposentadoria e versionamento
- 1.4 · L28 · Sculley et al. (2015), Hidden Technical Debt in Machine Learning Systems
- 1.4 · L29 · Breck et al. (2017), The ML Test Score
- 1.4 · L31 · Gama et al. (2014), A Survey on Concept Drift Adaptation
- 1.5 · L40 · Trade-offs de alertas: sensibilidade versus especificidade e custo de falsos positivos/negativos
- 1.5 · L43 · Manutenção: retreino automático versus manual; validação pós-retreino e rollback

### 9.5 Exigências parcialmente atendidas ou ausentes

"Efeito oficial" é o efeito provável da omissão na ficha da UFC, não no DeepSeek.

| L | Item | Exigência DeepSeek | Situação | Efeito oficial provável | Decisão |
|---|---|---|---|---|---|
| 7 | 1.1 | Distinção entre monitoramento de sistema, de modelo e de negócio | Parcial (0,75) | baixo | Não fazer |
| 8 | 1.1 | Data drift, concept drift, label drift e covariate shift: definições e critério… | Parcial (0,75) | baixo a moderado | Opcional (P9-O1) |
| 11 | 1.1 | Manutenção de modelos: tipos (corretiva, adaptativa e perfectiva) e gatilhos de… | Parcial (0,75) | baixo | Não fazer |
| 12 | 1.1 | Análise crítica: falsos alarmes, drift sem degradação, métricas agregadas engan… | Parcial (0,75) | baixo a moderado | Se houver tempo (P9-C) |
| 13 | 1.1 | Distinção entre monitoramento offline e online e avaliação contínua em produção | Parcial (0,50) | baixo | Não fazer |
| 15 | 1.1 | Segurança e privacidade no monitoramento: PII em logs, anonimização e retenção | Ausente | moderado | Fazer (P9-A) |
| 18 | 1.2 | Monitoramento de dados: schema, estatísticas, valores ausentes, ranges e freshn… | Parcial (0,75) | baixo | Não fazer |
| 19 | 1.2 | Detecção de drift: PSI, KS, Jensen-Shannon e testes estatísticos | Parcial (0,50) | moderado | Fazer (P9-B) |
| 21 | 1.2 | Alertas: SLI/SLO, limiares, severidade, on-call e runbooks | Parcial (0,75) | baixo | Não fazer |
| 22 | 1.2 | Logging e auditoria: predições, entradas, versões, lineage e retenção | Parcial (0,75) | baixo | Não fazer |
| 23 | 1.2 | Governança: políticas, catálogo, model registry, aprovação, auditoria e conform… | Parcial (0,75) | baixo | Não fazer |
| 24 | 1.2 | Gestão de risco de modelo: inventário, classificação, revisão periódica e valid… | Parcial (0,75) | baixo | Não fazer |
| 26 | 1.2 | Feedback loop e coleta de rótulos em produção | Parcial (0,25) | baixo a moderado | Se houver tempo (P9-C) |
| 30 | 1.4 | Huyen, Designing Machine Learning Systems (2022) | Ausente | baixo | Não fazer |
| 32 | 1.4 | Lu et al. (2018), Learning under Concept Drift: A Review (verificar) | Ausente | baixo | Não fazer |
| 33 | 1.4 | NIST AI Risk Management Framework (AI RMF 1.0, 2023) | Ausente | baixo a moderado | Fazer (P9-A) |
| 34 | 1.4 | ISO/IEC 42001:2023 — AI management system | Ausente | baixo a moderado | Fazer (P9-A) |
| 35 | 1.4 | LGPD (Lei 13.709/2018) e GDPR (Regulamento UE 2016/679) | Ausente | baixo a moderado | Fazer (P9-A) |
| 38 | 1.5 | Formalização de drift: mudança em P(X) versus mudança em P(y/X), com testes est… | Parcial (0,75) | moderado | Fazer (P9-B) |
| 39 | 1.5 | Label delay e avaliação retardada: estratégias de estimação e viés associado | Parcial (0,75) | baixo | Não fazer |
| 41 | 1.5 | Casos-limite: drift sem degradação, degradação sem drift, feedback loops e sazo… | Parcial (0,75) | baixo a moderado | Se houver tempo (P9-C) |
| 42 | 1.5 | Governança: auditoria e rastreabilidade fim a fim; retenção e privacidade de da… | Parcial (0,50) | moderado | Fazer (P9-A) |
| 44 | 1.5 | Relação entre monitoramento e versionamento/linhagem (fronteira com o Ponto 7) | Parcial (0,75) | baixo | Não fazer |

### 9.6 Exigências do DeepSeek consideradas excessivas ou pouco pertinentes

- L36 (1.4) · Documentação atual de Evidently AI, WhyLabs, Prometheus/Grafana e MLflow (verif… — Documentação de ferramentas: inexigível.
- L45 (1.5) · Exemplo aplicado: monitoramento de modelo de crédito com PSI, performance e ale… — Exemplo aplicado extenso.
- L46 (1.5) · Riscos adversariais e envenenamento de dados em produção (data poisoning) — Envenenamento de dados: segurança, fora do recorte.

### 9.7 Erros técnicos encontrados independentemente

Segunda leitura com conhecimento próprio, separada dos critérios DeepSeek.

- Nenhum erro. Covariate shift e concept drift estão corretamente definidos.
- Lacuna menor: label shift (mudança em P(Y)) não aparece (opcional).

### 9.8 Factibilidade em 80 minutos

- **Palavras:** 790 de prosa (inclui títulos) + 58 em 8 diagrama(s)/quadro(s) (23 linhas) + 32 nas referências.
- **Fórmulas:** 2 exibida(s), 34 símbolos; simples; 6 expressões matemáticas na linha.
- **Planejamento:** ~3 min (esqueleto de seções; o texto está memorizado). **Revisão mínima:** ~5 min.
- **Orçamento de escrita:** ~70 min (80 − 3 − 5 − 2 de folga).

| Versão | Lenta (12 pal/min) | Moderada (15) | Rápida (18) | Risco de não terminar (moderada / lenta) |
|---|---|---|---|---|
| Texto atual | 80,6 min | 64,7 min | 54,0 min | médio / **não cabe** |
| Com as alterações FAZER (e cortes obrigatórios) | 83,8 min | 67,3 min | 56,2 min | alto / **não cabe** |
| … + cortes C1 | 83,8 min | 67,3 min | 56,2 min | alto / **não cabe** |
| … + cortes C1 + C2 | 80,3 min | 64,4 min | 53,8 min | médio / **não cabe** |
| … + cortes C1 + C2 + C3 | 77,9 min | 62,4 min | 52,0 min | médio / **não cabe** |
| Cenário lento mínimo (só ESSENCIAL/custo zero + todos os cortes) | 72,3 min | 57,9 min | 48,2 min | baixo / **muito alto** (só com revisão encurtada) |

### 9.9 Alterações prioritárias

#### P9-A — Marcos normativos (NIST AI RMF, ISO/IEC 42001, LGPD)

1. **Problema.** O ponto de governança não cita nenhuma norma ou marco regulatório, embora o critério oficial 1.4 mencione "normas técnicas".
2. **Evidência.** Busca por "NIST", "ISO", "LGPD", "norma": nenhuma ocorrência; L86 (governança proporcional ao risco) é o lugar natural.
3. **Justificativa.** Atende diretamente à palavra "normas" do item 1.4 e mostra atualização (2018–2023). Liga a governança a referenciais reconhecíveis por qualquer banca.
4. **Proposta.** Inserir: “Marcos normativos estruturam essa gestão: o NIST AI RMF [5] organiza-a em governar, mapear, medir e gerenciar riscos; a ISO/IEC 42001 [6] define um sistema de gestão de IA; e, havendo dados pessoais, inclusive em *logs* de predição, aplica-se a LGPD [7].”
   *Versão mínima (cenário lento):* “A gestão de risco pode seguir o NIST AI RMF [5] e a ISO/IEC 42001 [6]; havendo dados pessoais, aplica-se a LGPD [7].”
   *Referência:* [5] NIST. Artificial intelligence risk management framework (AI RMF 1.0). 2023. [6] ISO/IEC 42001: artificial intelligence: management system. 2023. [7] BRASIL. Lei nº 13.709, de 14 de agosto de 2018 (LGPD).
5. **Localização.** Depois da L86 (após "...controle do escopo de uso."). Exige os cortes C1 do Ponto 9 para não estourar o tempo.
6. **Custo.** +43 palavras no corpo; +24 nas referências. Tempo de escrita (lenta / moderada / rápida): +5,6 / +4,5 / +3,7 min. Memorização: média.
7. **Ganho.** Moderado a alto em 1.4, confiança moderada. Também conta para 1.1 (governança aplicada). Indicador do modelo da Auditoria 1: +0,44 na leitura central (teto do instrumento). Risco técnico: baixo. As quatro funções do NIST são Govern, Map, Measure, Manage; não inventar números de artigos.
8. **Veredito.** **ALTO CUSTO-BENEFÍCIO**.

#### P9-B — Nomear testes e medidas de drift

1. **Problema.** A detecção de drift é descrita só como "testes ou medidas de distância".
2. **Evidência.** L64.
3. **Justificativa.** Nove palavras tornam o método verificável (1.2/1.5) e evitam a impressão de conhecimento só genérico.
4. **Proposta.** Substituir “por testes ou medidas de distância” por: “por testes estatísticos (ex.: Kolmogorov–Smirnov, qui-quadrado) ou medidas de divergência (ex.: PSI, Jensen–Shannon)”
5. **Localização.** L64: substituir o trecho indicado.
6. **Custo.** +9 palavras no corpo. Tempo de escrita (lenta / moderada / rápida): +0,8 / +0,6 / +0,5 min. Memorização: baixa.
7. **Ganho.** Moderado, confiança alta quanto ao acerto técnico. Indicador do modelo da Auditoria 1: +0,20 na leitura central (teto do instrumento). Risco técnico: nenhum. KS para variáveis contínuas e qui-quadrado para categóricas.
8. **Veredito.** **ALTO CUSTO-BENEFÍCIO**.

**Cortes obrigatórios que pagam estas inserções** (detalhes no relatório 06, seção 3.1):

- P9-C1a (L88): remover “Governança não se confunde com explicabilidade: **governança controla o ciclo de vida; XAI procura interpretar o comportamento do modelo**.”. Delimitação de fronteira com o Ponto 10, dispensável.
- P9-C1b (L147–151): remover “Todo esse ciclo é atravessado por: [quadro: GOVERNANÇA + LINEAGE + AUDITORIA + GESTÃO DE RISCO]”. A L155 retoma os mesmos elementos.

**Opcionais documentados (não entram na lista de execução):**

- **P9-C — Feedback loops e rótulos seletivos** (OPCIONAL; +31 palavras). É um caso-limite clássico de monitoramento (1.1/1.5). Fica como opcional porque o ponto já é longo e está entre os mais fortes. Texto: “As próprias predições também podem alterar os dados futuros (*feedback loops*): em crédito, só se observa o rótulo de quem foi aprovado, o que enviesa tanto o monitoramento quanto o retreinamento.” Local: Depois da L70.
- **P9-O1 — Label shift** (OPCIONAL; ~5 palavras). Texto: “; no *label shift*, muda \(P(Y)\)” Local: Final da frase da L45.

### 9.10 Veredito final

**CORRIGIR PONTUALMENTE E ENXUGAR.** Uma frase normativa (P9-A), paga pelos cortes C1, e uma substituição de nove palavras (P9-B).

## 10. Ponto 10 — XAI: Métodos, Interpretabilidade, Avaliação e Uso das Explicações

Dissertação: `prova-escrita/10-xai-metodos-interpretabilidade-avaliacao-e-uso-das-explicacoes_v2.md` · Barema DeepSeek: `prova-escrita/barema-deepseek/ponto-10.note`

### 10.1 Diagnóstico global

O texto mais completo e equilibrado. Cobre método, avaliação e uso, com crítica madura (plausibilidade ≠ fidelidade, discordância entre métodos, racionalização). A omissão mais visível para um especialista é o SHAP sem os valores de Shapley. Tudo o mais é refinamento.

| Pergunta | Resposta |
|---|---|
| Tese ou objetivo central | XAI é um problema de método, avaliação e uso; boa explicação é fiel, avaliada e adequada à finalidade (L24, L151–153). |
| Fundamentos apresentados? | Sim: intrínseca × post hoc, local × global, específico × agnóstico, importância ≠ causalidade (L9–36). |
| O núcleo responde ao tema? | Sim: SHAP, permutação, gradientes/IG, surrogates/LIME, exemplos, contrafactuais, fidelidade, estabilidade, avaliação funcional/humana/aplicação, usos. |
| Sequência lógica? | Sim; as quatro perguntas iniciais organizam o texto. |
| Erros técnicos relevantes? | Nenhum. Sinal da importância por permutação depende da métrica (micro); a taxonomia de avaliação (L99) é de Doshi-Velez & Kim, atribuída a Molnar. |
| Redundância? | Baixa (L111 × L153). |
| Aprofundamento compatível? | Alto; falta o fundamento teórico do SHAP. |
| Exemplos ajudam? | Sim. |

### 10.2 Nota anteriormente estimada

- **Auditoria 1:** central **9,2**, intervalo 7,5–9,7.
- **Indicador após as alterações FAZER** (mesmo modelo da Auditoria 1; teto do instrumento, não previsão): central 9,20 → **9,55**; leitura literal (R1) 7,51 → 7,80; viável (R3) 9,74 → 9,74.
- O modelo converte cobertura em pontos de forma mecânica. A direção do efeito é mais confiável que a magnitude, e o ganho oficial tende a ser menor.

### 10.3 Adequação ao barema oficial

| Critério oficial | Avaliação |
|---|---|
| 1.1 | Muito bom. |
| 1.2 | Muito bom; falta PDP/ICE (opcional). |
| 1.3 / 2.2 | Exemplar. |
| 1.4 | Boa (2016–2022); pode atribuir Wachter e Rudin (opcional) e atualizar Molnar (3ª ed., 2025). |
| 1.5 | Bom; falta Shapley. |
| 2.1 / 2.3 / 2.4 | Sem problemas. |

### 10.4 Principais exigências do DeepSeek atendidas

13 de 38 subitens atendidos integralmente ou de forma equivalente. As seções 10.4, 10.5 e 10.6 juntas classificam todos os 38 subitens.

- 1.1 · L7 · Distinção entre explicações globais e locais; model-specific × model-agnostic; ante-hoc × post-hoc
- 1.1 · L8 · Definição de fidelidade (faithfulness), estabilidade, robustez e compreensibilidade como critérios de qualida…
- 1.1 · L11 · Adequação da explicação ao público-alvo: desenvolvedores, usuários finais, auditores e reguladores
- 1.1 · L13 · Distinção entre explicabilidade e causalidade; explicações preditivas não estabelecem relações causais
- 1.2 · L19 · LIME: perturbações locais, modelo substituto e escopo de aplicação
- 1.2 · L21 · Gradientes de saliência e Integrated Gradients para entradas contínuas e imagens
- 1.4 · L28 · Ribeiro, Singh & Guestrin (2016), "Why Should I Trust You?": Explaining the Predictions of Any Classifier (LI…
- 1.4 · L29 · Lundberg & Lee (2017), A Unified Approach to Interpreting Model Predictions (SHAP)
- 1.4 · L30 · Sundararajan, Taly & Yan (2017), Axiomatic Attribution for Deep Networks (Integrated Gradients)
- 1.4 · L32 · Molnar, Interpretable Machine Learning (2ª ed., 2022) (verificar)
- 1.5 · L42 · Casos-limite: explicadores instáveis, dependência entre features, colinearidade distorcendo SHAP/permutation…
- 1.5 · L43 · Avaliação de explicações: métricas funcionais (fidelidade, estabilidade) e estudos humanos (compreensibilidad…
- 1.5 · L44 · Relação entre explicabilidade e causalidade; explicações preditivas × causais

### 10.5 Exigências parcialmente atendidas ou ausentes

"Efeito oficial" é o efeito provável da omissão na ficha da UFC, não no DeepSeek.

| L | Item | Exigência DeepSeek | Situação | Efeito oficial provável | Decisão |
|---|---|---|---|---|---|
| 6 | 1.1 | Definição formal de interpretabilidade, explicabilidade e transparência; distin… | Parcial (0,75) | baixo | Não fazer |
| 9 | 1.1 | Pressupostos e limites: explicações como aproximações, multiplicidade de explic… | Parcial (0,75) | baixo | Não fazer |
| 10 | 1.1 | Análise crítica do trade-off entre desempenho preditivo e interpretabilidade; c… | Parcial (0,75) | baixo | Não fazer |
| 12 | 1.1 | Quando não usar XAI: explicação não acionável, risco de confiança excessiva e c… | Parcial (0,75) | baixo | Não fazer |
| 15 | 1.1 | Crítica à XAI como substituto de governança, validação humana e controle instit… | Parcial (0,50) | baixo | Não fazer |
| 17 | 1.2 | Modelos intrinsecamente interpretáveis: regressão linear/logística, árvores de… | Parcial (0,75) | baixo | Não fazer |
| 18 | 1.2 | Importância de features: permutation importance, PDP/ICE e suas limitações | Parcial (0,75) | baixo a moderado | Se houver tempo (P10-B) |
| 20 | 1.2 | SHAP: valores de Shapley, propriedades (eficiência, simetria, dummy, aditividad… | Parcial (0,50) | moderado | Fazer (P10-A) |
| 22 | 1.2 | Explicações contrafactuais e âncoras (anchors): definição, geração e uso | Parcial (0,75) | baixo | Não fazer |
| 23 | 1.2 | Explicações baseadas em exemplos/protótipos e k-NN explicável | Parcial (0,50) | baixo | Não fazer |
| 24 | 1.2 | Surrogate models globais (árvore substituta) e regras de decisão | Parcial (0,75) | baixo | Não fazer |
| 25 | 1.2 | Visualizações de explicabilidade: heatmaps, SHAP force plots, PDP/ICE | Ausente | baixo a moderado | Se houver tempo (P10-B) |
| 31 | 1.4 | Wachter, Mittelstadt & Russell (2017), Counterfactual Explanations Without Open… | Parcial (0,25) | baixo a moderado | Opcional (P10-O1) |
| 33 | 1.4 | Doshi-Velez & Kim (2017), Towards A Rigorous Science of Interpretable Machine L… | Parcial (0,25) | baixo a moderado | Opcional (P10-O2) |
| 34 | 1.4 | Rudin (2019), Stop Explaining Black Box Machine Learning Models for High Stakes… | Parcial (0,25) | baixo a moderado | Opcional (P10-O1) |
| 39 | 1.5 | Formalização dos valores de Shapley e das propriedades de eficiência, simetria,… | Parcial (0,25) | moderado | Fazer (P10-A) |
| 40 | 1.5 | Formalização de fidelidade: correlação entre importância atribuída e mudança na… | Parcial (0,50) | baixo | Não fazer |
| 41 | 1.5 | Trade-offs: fidelidade × compreensibilidade, estabilidade × sensibilidade e cus… | Parcial (0,75) | moderado | Fazer (P10-A) |

### 10.6 Exigências do DeepSeek consideradas excessivas ou pouco pertinentes

- L14 (1.1) · Limitações de explicabilidade em modelos de alta dimensionalidade e dados não e… — Dados não estruturados: tema vizinho.
- L26 (1.2) · Explicações baseadas em atenção em modelos de linguagem/visão e suas limitações — Explicações por atenção: tema vizinho e controverso.
- L35 (1.4) · Miller (2019), Explanation in Artificial Intelligence: Insights from the Social… — Miller: referência de ciências sociais, periférica.
- L36 (1.4) · Documentação atual de SHAP, LIME, InterpretML, Captum e Alibi (verificar versõe… — Documentação de bibliotecas: inexigível.
- L37 (1.4) · LGPD (Lei 13.709/2018) e GDPR: direito à explicação (fronteira com o Ponto 9) — Direito à explicação (LGPD/GDPR): fronteira com o Ponto 9.
- L45 (1.5) · Exemplo aplicado: explicação local com SHAP/LIME para decisão de crédito e anál… — Exemplo aplicado extenso.
- L46 (1.5) · Limitações em modelos de linguagem e imagens: risco de explicações plausíveis,… — Limitações em LLMs: tema vizinho.

### 10.7 Erros técnicos encontrados independentemente

Segunda leitura com conhecimento próprio, separada dos critérios DeepSeek.

- Nenhum erro.
- L57: \(I_{j} = M_{\text{original}} - M_{\text{permutado}(j)}\) supõe métrica em que "maior é melhor"; para métricas de erro, o sinal se inverte (microajuste).
- L99: a taxonomia funcional/humana/aplicação é de Doshi-Velez & Kim (2017); está atribuída a Molnar [1], que a reproduz. Aceitável; citar a origem seria melhor (opcional).

### 10.8 Factibilidade em 80 minutos

- **Palavras:** 818 de prosa (inclui títulos) + 27 em 5 diagrama(s)/quadro(s) (15 linhas) + 28 nas referências.
- **Fórmulas:** 3 exibida(s), 77 símbolos; moderada; 10 expressões matemáticas na linha.
- **Planejamento:** ~3 min (esqueleto de seções; o texto está memorizado). **Revisão mínima:** ~5 min.
- **Orçamento de escrita:** ~70 min (80 − 3 − 5 − 2 de folga).

| Versão | Lenta (12 pal/min) | Moderada (15) | Rápida (18) | Risco de não terminar (moderada / lenta) |
|---|---|---|---|---|
| Texto atual | 80,1 min | 64,2 min | 53,5 min | médio / **não cabe** |
| Com as alterações FAZER (e cortes obrigatórios) | 84,1 min | 67,4 min | 56,2 min | alto / **não cabe** |
| … + cortes C1 | 84,1 min | 67,4 min | 56,2 min | alto / **não cabe** |
| … + cortes C1 + C2 | 79,9 min | 64,1 min | 53,4 min | médio / **não cabe** |
| … + cortes C1 + C2 + C3 | 77,9 min | 62,4 min | 51,9 min | médio / **não cabe** |
| Cenário lento mínimo (só ESSENCIAL/custo zero + todos os cortes) | 73,0 min | 58,5 min | 48,6 min | baixo / **muito alto** (só com revisão encurtada) |

### 10.9 Alterações prioritárias

#### P10-A — Valores de Shapley e suas propriedades

1. **Problema.** O SHAP é apresentado sem os valores de Shapley, que são seu fundamento teórico.
2. **Evidência.** L44–52; "Shapley", "eficiência", "simetria" ausentes.
3. **Justificativa.** Para um examinador de XAI, falar de SHAP sem Shapley é a omissão mais visível do texto. Uma frase dá o fundamento (1.1), a formalização (1.5) e o custo computacional (crítica).
4. **Proposta.** Inserir: “Os \(\phi_{j}\) são **valores de Shapley**, da teoria dos jogos cooperativos: a média da contribuição marginal de \(j\) sobre todas as ordens de entrada das *features*, única atribuição que satisfaz eficiência (as contribuições somam \(f(x) - \phi_{0}\)), simetria, jogador nulo e aditividade; como o cálculo exato é exponencial no número de *features*, usam-se aproximações (KernelSHAP) ou algoritmos específicos (TreeSHAP).”
   *Versão mínima (cenário lento):* “Os \(\phi_{j}\) são valores de Shapley, da teoria dos jogos cooperativos, únicos a satisfazer eficiência, simetria, jogador nulo e aditividade; seu cálculo exato é exponencial no número de *features*.”
5. **Localização.** Depois da L50 (após "...atribuída à *feature* \(j\)."). Exige o corte C1 do Ponto 10 (L111).
6. **Custo.** +54 palavras no corpo; +10 símbolos matemáticos. Tempo de escrita (lenta / moderada / rápida): +4,9 / +3,9 / +3,2 min. Memorização: média-alta.
7. **Ganho.** Moderado, confiança moderada a alta. Indicador do modelo da Auditoria 1: +0,35 na leitura central (teto do instrumento). Risco técnico: médio-baixo: memorizar os quatro axiomas na ordem eficiência, simetria, jogador nulo, aditividade.
8. **Veredito.** **ALTO CUSTO-BENEFÍCIO**.

**Cortes obrigatórios que pagam estas inserções** (detalhes no relatório 06, seção 3.1):

- P10-C1a (L111): remover “Uma boa explicação é adequada ao usuário e à tarefa.”. A L153 diz o mesmo.

**Opcionais documentados (não entram na lista de execução):**

- **P10-B — PDP e ICE** (OPCIONAL; +39 palavras). Completa os métodos globais (1.2), mas o ponto já é o mais forte e o mais longo; o ganho marginal é pequeno. Texto: “Para efeitos globais, o *partial dependence plot* (PDP) mostra a predição média em função de uma *feature*, e as curvas ICE mostram esse efeito por instância, revelando heterogeneidade que a média oculta; ambos se distorcem quando há *features* correlacionadas.” Local: Depois da L60.
- **P10-O1 — Citar Wachter (contrafactuais) e Rudin (modelos interpretáveis)** (OPCIONAL; ~14 palavras). Texto: “L75: "Explicações **contrafactuais** [5] perguntam…"; L131: "…antes de depender de explicações *post hoc* [6]."” Local: L75 e L131 + duas referências.
- **P10-O2 — Atribuir a taxonomia de avaliação à origem** (OPCIONAL; ~8 palavras). Texto: “L99: trocar "[1]" por "[7]" (Doshi-Velez & Kim, 2017).” Local: L99.

**Microajustes de precisão (custo ~0; fora do limite de três):**

- L54–57: “pela queda de desempenho quando seus valores são embaralhados” → “pela queda de desempenho (em métricas nas quais maior é melhor) quando seus valores são embaralhados”. Para métricas de erro, o sinal da fórmula se inverte.

### 10.10 Veredito final

**MANTER.** Uma inserção (P10-A), paga pelo corte C1. Pode ser considerada fechada.

## 11. ABNT: referências e citações

Normas aplicáveis: NBR 6023:2018 (referências) e NBR 10520:2023 (citações).
As regras da NBR 10520:2023 aqui resumidas foram conferidas em manuais de bibliotecas universitárias, não no texto oficial da norma.

### 11.1 Trechos fora da norma

**(a) Chamadas no texto entre colchetes.** Os dez textos usam "[1]", "[2]" etc. No sistema numérico, a NBR 10520:2023 prevê o número entre parênteses ou em expoente.
- Exemplo: P1 L22, "pelo Google File System [1]" → "pelo Google File System (1)" ou "…System¹".
- Lista por ponto: o texto de 2002 da NBR 10520 admitia remeter à lista "ao final do trabalho, do capítulo ou da parte". Tratar cada ponto como uma "parte", com lista própria (como hoje), é defensável; confirme na versão de 2023, que não consultei diretamente.

**(b) Referências sem título.** Todas as 41 referências seguem o padrão "AUTOR. Veículo. Ano.". O título é elemento essencial (NBR 6023:2018), e o veículo aparece abreviado ou trocado pela editora ("ACM", "USENIX"). Exemplos:

| Atual | Problemas |
|---|---|
| P1: `[1] GHEMAWAT, S. et al. ACM. 2003.` | sem título; "et al." com 3 autores; "ACM" é a editora, não o evento |
| P1: `[3] HERLIHY, M. et al. ACM. 1990.` | sem título; "et al." com 2 autores |
| P6: `[1] Sutton, R. S. et al. MIT Press. 2018.` | sobrenome em minúsculas; "et al." com 2 autores; sem título; sem edição (2. ed.) |
| P7: `[3] Kreuzberger, D. et al. IEEE Access. 2023.` | sobrenome em minúsculas; "et al." com 3 autores; sem título |
| P10: `[2] Lundberg, S. M. et al. NeurIPS. 2017.` | sobrenome em minúsculas; "et al." com 2 autores; sem título |

**(c) "et al." com até três autores (18 referências distintas).** Até três autores, a NBR 6023:2018 manda indicar todos; "et al." só a partir de quatro (e mesmo então é permitido, não obrigatório). Casos:
- P1 `[1] GHEMAWAT, S…` (3 autores); P1 `[3] HERLIHY, M…` (2 autores); P1 `[4] GILBERT, S…` (2 autores); P2 `[3] DEAN, J…` (2 autores); P3 `[3] KREPS, J…` (3 autores); P3 `[4] MARZ, N…` (2 autores); P4 `[1] Fayyad, U…` (3 autores); P4 `[3] Han, J…` (3 autores); P5 `[3] Hastie, T…` (3 autores); P5 `[4] Goodfellow, I…` (3 autores); P6 `[1] Sutton, R…` (2 autores); P6 `[2] Watkins, C…` (2 autores); P7 `[3] Kreuzberger, D…` (3 autores); P8 `[2] Kreuzberger, D…` (3 autores); P9 `[4] Kreuzberger, D…` (3 autores); P10 `[2] Lundberg, S…` (2 autores); P10 `[3] Sundararajan, M…` (3 autores); P10 `[4] Ribeiro, M…` (3 autores).

**(d) Sobrenome em minúsculas nos Pontos 4–10** ("Fayyad, U.", "Sculley, D."). Na lista de referências, o sobrenome vai em MAIÚSCULAS (os Pontos 1–3 já fazem isso). A mudança de 2023 para minúsculas vale para as **citações no texto**, não para a lista.

**(e) Edição omitida** em obras de 2ª edição ou posterior: Sutton & Barto (2. ed., 2018), Hastie et al. (2. ed., 2009), Han et al. (3. ed., 2012), Aggarwal (2. ed., 2017), Molnar (2. ed., 2022).

**(f) Destaque tipográfico.** A NBR 6023 exige destacar de forma uniforme o título do livro ou do periódico (negrito, itálico **ou sublinhado**). No manuscrito, use **sublinhado**.

### 11.2 Como citar no texto (NBR 10520:2023)

| Situação | Sistema numérico (recomendado na prova) | Sistema autor-data (alternativa) |
|---|---|---|
| Citação indireta, 2 autores | "…linearizabilidade (3)…" ou "…linearizabilidade³…" | "(Herlihy; Wing, 1990)" ou "Herlihy e Wing (1990) definem…" |
| 3 autores | "(1)" | "(Ghemawat; Gobioff; Leung, 2003)" |
| 4 ou mais autores | "(2)" | "(DeCandia et al., 2007)"; et al. opcional, mas uniforme |
| Citação direta | "(1, p. 29)" | "(Ghemawat; Gobioff; Leung, 2003, p. 29)" |
| Norma/lei | "(5)" | "(NIST, 2023)", "(Brasil, 2018)" |

Recomendações:

- **Manter o sistema numérico:** é o mais barato de escrever à mão, e no texto basta trocar colchetes por parênteses ou expoente.
- **Autor-data:** acrescentaria ≈ 3–5 palavras por citação (≈ 20 por ponto), em troca de deixar o ano visível no corpo.
- **Uniformidade:** não misturar os dois sistemas na mesma prova.

### 11.3 Como referenciar (NBR 6023:2018)

Modelos por tipo, com a forma completa e a **forma manuscrita recomendada**.
A forma manuscrita conserva autoria completa (até três autores), título e veículo com ano. É mais curta que a completa e mais defensável que a atual, mas tem conformidade parcial: omite local, editora e páginas.

| Tipo | Forma completa | Forma manuscrita |
|---|---|---|
| Livro | HASTIE, T.; TIBSHIRANI, R.; FRIEDMAN, J. **The elements of statistical learning**: data mining, inference, and prediction. 2. ed. New York: Springer, 2009. | HASTIE, T.; TIBSHIRANI, R.; FRIEDMAN, J. <u>The elements of statistical learning</u>. 2. ed. Springer, 2009. |
| Artigo em periódico | GILBERT, S.; LYNCH, N. Brewer's conjecture and the feasibility of consistent, available, partition-tolerant web services. **ACM SIGACT News**, New York, v. 33, n. 2, p. 51-59, 2002. | GILBERT, S.; LYNCH, N. Brewer's conjecture [...]. <u>ACM SIGACT News</u>, 2002. |
| Trabalho em evento | GHEMAWAT, S.; GOBIOFF, H.; LEUNG, S.-T. The Google file system. In: ACM SYMPOSIUM ON OPERATING SYSTEMS PRINCIPLES, 19., 2003, Bolton Landing. **Proceedings** [...]. New York: ACM, 2003. p. 29-43. | GHEMAWAT, S.; GOBIOFF, H.; LEUNG, S.-T. The Google file system. SOSP, 2003. |
| Norma técnica | INTERNATIONAL ORGANIZATION FOR STANDARDIZATION. **ISO/IEC 42001**: information technology: artificial intelligence: management system. Geneva: ISO, 2023. | ISO/IEC 42001: artificial intelligence: management system. 2023. |
| Lei | BRASIL. Lei nº 13.709, de 14 de agosto de 2018. Lei Geral de Proteção de Dados Pessoais (LGPD). **Diário Oficial da União**, Brasília, DF, 15 ago. 2018. | BRASIL. Lei nº 13.709, de 14 de agosto de 2018 (LGPD). |

Regras usadas:

- Títulos longos podem ser abreviados com "[...]" (NBR 6023:2018, 8.2.2).
- A lista segue a ordem numérica das chamadas.
- As 41 referências atuais estão no Apêndice B, nas duas formas.

**Custo:** a forma manuscrita acrescenta ≈ 8–12 palavras por referência (≈ +40 por ponto, ≈ +2,7 min no cenário moderado). Por isso, ela fica em "fazer somente se houver tempo".
As correções de custo zero (parênteses, MAIÚSCULAS, todos os autores até três, edição) entram no plano.

### 11.4 Citações mais atuais que se encaixam nos mesmos trechos

Critério:

- Só obras reais, de atribuição verificável, que sustentam exatamente a frase em que entram.
- Clássicos fundadores (Amdahl, Gustafson, Herlihy & Wing, Gilbert & Lynch, Fayyad, Tukey, Watkins & Dayan, Williams) **não devem ser substituídos**: a atribuição histórica é parte do rigor. Para eles, a obra atual entra como complemento, não como troca.
- "Substitui" só quando se trata da mesma obra em nova edição ou de sucessor direto do mesmo autor.

Mnemônicos:

- Quando possível, o sobrenome ou as iniciais formam uma palavra em português, inglês, espanhol ou alemão.
- Quando não há palavra natural, uso outra âncora (sigla, número, associação), indicada na coluna "Tipo de âncora". Não forcei palavras artificiais.

| Ponto | Trecho | Citação atual | Sugestão (forma manuscrita) | Encaixe | Mnemônico | Tipo de âncora | Decisão |
|---|---|---|---|---|---|---|---|
| 1 | Parágrafo novo de P1-A (2PC) | — | KLEPPMANN, M.; RICCOMINI, C. Designing data-intensive applications. 2. ed. O'Reilly, 2026. | nova; atualiza DDIA (2017) | **K&R dos dados** (como o K&R do C); Riccomini → "rico": edição mais rica | sigla consagrada | FAZER (vem com P1-A) |
| 1 | Frase nova de P1-B (PACELC) | — | ABADI, D. Consistency tradeoffs in modern distributed database system design. Computer, 2012. | nova | Abadi ≈ **abadia**; mesma revista e mesmo número de Brewer (Computer, fev. 2012) | palavra (PT) | FAZER (vem com P1-B) |
| 1 | L54 ("não significa escolher dois de três") | [4] Gilbert & Lynch 2002 | BREWER, E. CAP twelve years later: how the "rules" have changed. Computer, 2012. | complementa (encaixe exato: é a tese do artigo) | BREWER, **E.** → "**BE**": *to be or not to be consistent* | palavra (EN) | SE HOUVER TEMPO |
| 1 | Alternativa a K&R no 2PC | — | ÖZSU, M. T.; VALDURIEZ, P. Principles of distributed database systems. 4. ed. Springer, 2020. | alternativa (cobre 2PC e NewSQL) | Ö + V (+ o) → **OVO**; 4ª ed., 2020 | palavra (PT, com vogal de apoio) | alternativa |
| 2 | L95 (cauda da distribuição) | sem citação | DEAN, J.; BARROSO, L. A. The tail at scale. Communications of the ACM, 2013. | nova (encaixe exato) | Dean volta nove anos depois do MapReduce (2004 → 2013); D&B = **DB** | sigla | SE HOUVER TEMPO |
| 2 | L81 [4] (Spark) | Zaharia et al. 2012 | ZAHARIA, M. et al. Apache Spark: a unified engine for big data processing. Communications of the ACM, 2016. | complementa (versão "madura" do Spark) | Zaharia 12 → 16: do RDD ao motor unificado | associação | SE HOUVER TEMPO |
| 3 | L37 [1] (janelas, watermark, trigger) | Akidau et al. 2015 | AKIDAU, T.; CHERNYAK, S.; LAX, R. Streaming systems: the what, where, when, and how of large-scale data processing. O'Reilly, 2018. | complementa (o subtítulo traz as quatro perguntas) | **LAX** (inglês: frouxo): o watermark tolera atraso | palavra (EN) | SE HOUVER TEMPO |
| 3 | L73 (Kappa) | sem citação | KREPS, J. Questioning the Lambda Architecture. O'Reilly Radar, 2014. | nova (atribuição exata) | 3K: **K**reps — **K**afka (2011) — **K**appa (2014) | aliteração | FAZER (vem com P3-C) |
| 3 | L75 (lakehouse) | sem citação | ARMBRUST, M. et al. Lakehouse: a new generation of open platforms that unify data warehousing and advanced analytics. CIDR, 2021. | nova (atribuição exata) | **Armbrust** (alemão: besta, a arma): a besta acerta o lago | palavra (DE) | SE HOUVER TEMPO |
| 4 | L63 [3] (regras de associação) | Han, Kamber & Pei 2012 | HAN, J.; PEI, J.; TONG, H. Data mining: concepts and techniques. 4. ed. Morgan Kaufmann, 2022. | substitui (mesma obra, nova edição) | Han-Pei-Tong → "**hão de pôr o tom**" | frase (PT) | FAZER (custo quase nulo) |
| 5 | L5 [2] (taxonomia) | Murphy 2012 | MURPHY, K. P. Probabilistic machine learning: an introduction. MIT Press, 2022. | substitui (sucessor do mesmo autor) | lei de **Murphy**, dez anos depois (2012 → 2022) | associação | SE HOUVER TEMPO |
| 5 | L40 [3] (viés-variância) | Hastie et al. 2009 | JAMES, G. et al. An introduction to statistical learning: with applications in Python. Springer, 2023. | complementa | ISL → **isla** (espanhol: ilha) do Python | palavra (ES) | SE HOUVER TEMPO |
| 5 | L63 [4] (redes neurais) | Goodfellow et al. 2016 | PRINCE, S. J. D. Understanding deep learning. MIT Press, 2023. | substitui ou complementa | **Prince** (príncipe) sucede o **Goodfellow** (bom sujeito) | palavra (EN) | SE HOUVER TEMPO |
| 5 | Alternativa para [4] | Goodfellow et al. 2016 | BISHOP, C. M.; BISHOP, H. Deep learning: foundations and concepts. Springer, 2024. | alternativa | **dois bispos** (Bishop & Bishop) | palavra (EN) | alternativa |
| 6 | L118 [3] (gradiente de política) | Williams 1992 | SCHULMAN, J. et al. Proximal policy optimization algorithms. arXiv:1707.06347, 2017. | complementa (gradiente de política moderno) | **Schul + Mann** (alemão: escola + homem): o professor "corta" (*clip*) o passo | palavras (DE) | SE HOUVER TEMPO |
| 6 | L141 (reward hacking) | sem citação | AMODEI, D. et al. Concrete problems in AI safety. arXiv:1606.06565, 2016. | nova (atribuição) | "problemas **de concreto**" | tradução do título | SE HOUVER TEMPO |
| 7 | L67–81 (reprodutibilidade) | sem citação | PINEAU, J. et al. Improving reproducibility in machine learning research. Journal of Machine Learning Research, 2021. | nova (encaixe exato) | **PIN** (inglês: fixar): fixe versões e sementes | palavra (EN) | SE HOUVER TEMPO |
| 7 | Frase de P7-B (MLflow) | — | ZAHARIA, M. et al. Accelerating the machine learning lifecycle with MLflow. IEEE Data Engineering Bulletin, 2018. | nova | Zaharia de novo: do Spark ao MLflow | associação | SE HOUVER TEMPO |
| 8 | L62–74 (serving batch × online) | sem citação | HUYEN, C. Designing machine learning systems. O'Reilly, 2022. | nova | **CHIP** Huyen (prenome = chip) | palavra (EN) | SE HOUVER TEMPO |
| 9 | L47 [2] (concept drift) | Gama et al. 2014 | LU, J. et al. Learning under concept drift: a review. IEEE Transactions on Knowledge and Data Engineering, 2019. | complementa | **Lu** → lua: muda de fase (drift) | palavra (PT) | SE HOUVER TEMPO |
| 9 | Frase de P9-A | — | NIST. Artificial intelligence risk management framework (AI RMF 1.0). 2023. | nova (norma) | **G-M-M-M**: governar, mapear, medir, gerenciar | acrônimo | FAZER (vem com P9-A) |
| 9 | Frase de P9-A | — | ISO/IEC 42001: information technology: artificial intelligence: management system. 2023. | nova (norma) | **42**, "a resposta para tudo" + **001**, o primeiro sistema de gestão de IA | associação numérica | FAZER (vem com P9-A) |
| 9 | Frase de P9-A | — | BRASIL. Lei nº 13.709, de 14 de agosto de 2018. Lei Geral de Proteção de Dados Pessoais (LGPD). | nova (lei) | sancionada em **14/08/2018** | data | FAZER (vem com P9-A) |
| 10 | L15 e L99 [1] | Molnar 2022 (2. ed.) | MOLNAR, C. Interpretable machine learning. 3. ed. Leanpub, 2025. | substitui (mesma obra, nova edição) | **3**ª edição em 20**25** | associação numérica | FAZER (custo quase nulo) |
| 10 | L52 (agregação local → global) | [2] Lundberg & Lee 2017 | LUNDBERG, S. M. et al. From local explanations to global understanding with explainable AI for trees. Nature Machine Intelligence, 2020. | complementa (encaixe exato) | Lundberg **17 → 20**: do local ao global | associação | SE HOUVER TEMPO |
| 10 | L72–75 (contrafactuais) | sem citação | WACHTER, S.; MITTELSTADT, B.; RUSSELL, C. Counterfactual explanations without opening the black box [...]. Harvard Journal of Law & Technology, 2018. | nova (atribuição exata da fórmula) | o **Wächter** (alemão: vigia) da **Mittelstadt** (cidade do meio) pergunta o que mudaria a decisão | palavras (DE) | SE HOUVER TEMPO (P10-O1) |
| 10 | L99 (avaliação funcional/humana/aplicação) | [1] Molnar | DOSHI-VELEZ, F.; KIM, B. Towards a rigorous science of interpretable machine learning. arXiv:1702.08608, 2017. | substitui a atribuição (origem da taxonomia) | "**rigor** em três níveis" | associação | SE HOUVER TEMPO (P10-O2) |
| 10 | L125 (E₁(x) ≠ E₂(x)) | sem citação | KRISHNA, S. et al. The disagreement problem in explainable machine learning: a practitioner's perspective. Transactions on Machine Learning Research, 2024. | nova (encaixe exato) | **Krish**na ≈ **crise**: a crise da discordância entre explicações | palavra (PT, aproximada) | SE HOUVER TEMPO |
| 10 | L131 (verificar modelo interpretável antes) | sem citação | RUDIN, C. Stop explaining black box machine learning models for high stakes decisions and use interpretable models instead. Nature Machine Intelligence, 2019. | nova (é a tese do artigo) | Rudin ≈ **rude** com as caixas-pretas | palavra (PT/EN, aproximada) | SE HOUVER TEMPO (P10-O1) |

**Mnemônicos para as referências atuais** (sobrenome ou iniciais que já formam palavra):

- **GooGLe** (Ghemawat, Gobioff, Leung)
- **candeia** (DeCandia)
- **FPS** (Fayyad, Piatetsky-Shapiro, Smyth)
- **turkey** (Tukey)
- **bispo** (Bishop) e **bom sujeito** (Goodfellow)
- **Kreuz–kühl–Hirsch** (Kreuzberger, Kühl, Hirschl)
- **sty** (Sundararajan, Taly, Yan)
- **riacho** (Ribeiro)
- **carbono** (Carbone)
- **3K** (Kreps, Kafka, Kappa)

## 12. Auditoria adversarial final

### 12.1 Primeira leitura — banca exigente

*"Estou deixando passar alguma ausência conceitual realmente importante que comprometeria a nota?"*

| Ponto | Ausência que sobra após o plano | Julgamento |
|---|---|---|
| 5 | Regressão logística, impureza em árvores e kernels do SVM continuam em uma linha | **Risco residual aceito.** Detalhar todos é contraproducente (+300–400 palavras). P5-B/C cobrem os dois métodos mais cobrados (ensembles e k-means), e P5-O1 é o primeiro opcional se houver tempo. O Ponto 5 continua o mais vulnerável a uma banca exaustiva. |
| 1 | MVCC e níveis de isolamento | Aceito. Com o 2PC (P1-A), a lacuna de primeira ordem está fechada; MVCC fica como P1-O1. |
| 8 | Shadow deployment, SLO por percentis | Aceito. São refinamentos de 8.3.1/8.3.2; P8-O1 e P8-O2 são opcionais de 10–13 palavras. |
| 2 | Gerenciamento de recursos (YARN) | Aceito. O runtime do MapReduce já cobre escalonamento e reexecução; YARN é sobretudo produto. |
| 9 | Feedback loops | Limítrofe: é caso-limite clássico de monitoramento. Mantido como o primeiro opcional do ponto (P9-C), porque o texto já é longo e forte. |
| 3, 10 | — | Nenhuma ausência relevante. |
| 4, 6, 7 | — | As lacunas de primeira ordem estão cobertas pelas propostas (EDA, deadly triad, MC × TD, experimentação). |

Conclusão: nenhuma omissão grave fica sem tratamento. A única exposição residual relevante é a profundidade algorítmica do Ponto 5, deliberadamente limitada pelo tempo.

### 12.2 Segunda leitura — professor experiente sob pressão de tempo

*"Estou recomendando detalhes que apenas tornariam a dissertação mais longa, sem ganho avaliativo relevante?"*

**Rebaixados para "fazer somente se houver tempo" depois desta leitura:**

- P1-C (arquitetura GFS/HDFS)
- P2-B (exemplo de join)
- P3-B (offsets/consumer groups)
- P4-C (agrupamento)
- P7-C (CACE)
- P9-C (feedback loops)
- P10-B (PDP/ICE)
- títulos nas referências
- todas as referências modernas não ligadas a uma proposta

Motivos: o ganho é real, mas incremental, em pontos já fortes ou longos; ou o custo de memorização supera o ganho.

**Mantidos, porque sobrevivem às duas leituras:**

- itens de até 16 palavras: P3-A, P3-C, P4-B, P7-B, P8-C, P9-B;
- as três lacunas de primeira ordem: P1-A, P4-A, P8-A;
- substituições pagas por cortes do próprio ponto: P5-A/B/C, P6-B/C, P9-A, P10-A;
- inserções de 30–40 palavras que acrescentam mecanismo, não enumeração: P1-B, P2-A, P7-A, P8-B.

**Rejeitados nas duas leituras, porque só demonstrariam atualidade:**

- RLHF/LLMs no Ponto 6 (ficou opcional, P6-O2);
- explicações por atenção no Ponto 10;
- listas de produtos (KServe, Feast, Evidently);
- documentação com versão.

**Verificação de equilíbrio:** a lista FAZER não aumenta nenhum texto em mais de ≈ 14%. O maior acréscimo líquido é o do Ponto 1, +108 palavras, justamente o texto mais curto. Quatro pontos (5, 6, 9, 10) compensam as inserções com cortes no próprio texto.

## 13. Incertezas e limitações

- **Velocidade manuscrita:** é a maior incerteza prática. As três velocidades são hipóteses; o teste do relatório 06 resolve isso em 15 minutos.
- **"Normas técnicas" no item 1.4:** pode significar normas ABNT de apresentação ou normas técnicas do domínio (ISO, NIST). As propostas cobrem as duas leituras com custo baixo: ABNT de custo zero em todos os pontos e P9-A no Ponto 9.
- **Indicador numérico:** deriva do instrumento DeepSeek e mede o teto desse instrumento. A banca real pode valorizar menos a cobertura e mais a precisão; nesse caso, as substituições de precisão (P3-A, microajustes) ganham peso relativo.
- **Memorização em cinco dias:** a lista FAZER soma ≈ +616 palavras brutas (≈ +472 líquidas, após os cortes) nos dez textos. Se não houver tempo para tudo, siga a ordem do relatório 05 e pare onde o tempo acabar; cada item é independente.
- **Agregação dos três pontos:** continua sem regra oficial (relatório 03). A regra que domina é a do item 16.8: ponto incompleto elimina.

## Apêndice B — Referências atuais em ABNT completa e forma manuscrita

Paginação e numeração de eventos foram conferidas de memória; confira na fonte antes de usar num texto definitivo. Na prova, use a coluna "manuscrita".

### B.1 Ponto 1

| Atual | Problemas | ABNT completa (NBR 6023:2018) | Forma manuscrita | Mnemônico |
|---|---|---|---|---|
| `[1] GHEMAWAT, S. et al. ACM. 2003.` | sem título; "et al." com 3 autores; "ACM" é a editora, não o evento | GHEMAWAT, S.; GOBIOFF, H.; LEUNG, S.-T. The Google file system. In: ACM SYMPOSIUM ON OPERATING SYSTEMS PRINCIPLES, 19., 2003, Bolton Landing. **Proceedings** [...]. New York: ACM, 2003. p. 29-43. | GHEMAWAT, S.; GOBIOFF, H.; LEUNG, S.-T. The Google file system. SOSP, 2003. | G-G-L → **GooGLe** (o GFS é do Google) |
| `[2] DECANDIA, G. et al. ACM. 2007.` | sem título; evento ausente | DECANDIA, G. et al. Dynamo: Amazon's highly available key-value store. In: ACM SYMPOSIUM ON OPERATING SYSTEMS PRINCIPLES, 21., 2007, Stevenson. **Proceedings** [...]. New York: ACM, 2007. p. 205-220. | DECANDIA, G. et al. Dynamo: Amazon's highly available key-value store. SOSP, 2007. | DeCandia ≈ **candeia** sempre acesa (alta disponibilidade) |
| `[3] HERLIHY, M. et al. ACM. 1990.` | sem título; "et al." com 2 autores | HERLIHY, M. P.; WING, J. M. Linearizability: a correctness condition for concurrent objects. **ACM Transactions on Programming Languages and Systems**, New York, v. 12, n. 3, p. 463-492, 1990. | HERLIHY, M. P.; WING, J. M. Linearizability: a correctness condition for concurrent objects. ACM TOPLAS, 1990. | **Wing** (asa): a operação "voa" de uma vez, atômica |
| `[4] GILBERT, S. et al. ACM. 2002.` | sem título; "et al." com 2 autores | GILBERT, S.; LYNCH, N. Brewer's conjecture and the feasibility of consistent, available, partition-tolerant web services. **ACM SIGACT News**, New York, v. 33, n. 2, p. 51-59, 2002. | GILBERT, S.; LYNCH, N. Brewer's conjecture [...]. ACM SIGACT News, 2002. | a "conjectura de Brewer" vira teorema em 2002 |
| `[5] CHANG, F. et al. USENIX. 2006.` | sem título; "USENIX" é a associação, não o evento | CHANG, F. et al. Bigtable: a distributed storage system for structured data. In: USENIX SYMPOSIUM ON OPERATING SYSTEMS DESIGN AND IMPLEMENTATION, 7., 2006, Seattle. **Proceedings** [...]. Berkeley: USENIX Association, 2006. p. 205-218. | CHANG, F. et al. Bigtable: a distributed storage system for structured data. OSDI, 2006. | — |

### B.2 Ponto 2

| Atual | Problemas | ABNT completa (NBR 6023:2018) | Forma manuscrita | Mnemônico |
|---|---|---|---|---|
| `[1] AMDAHL, G. AFIPS. 1967.` | sem título; prenome incompleto (G. M.) | AMDAHL, G. M. Validity of the single processor approach to achieving large scale computing capabilities. In: AFIPS SPRING JOINT COMPUTER CONFERENCE, 1967, Atlantic City. **Proceedings** [...]. New York: ACM, 1967. p. 483-485. | AMDAHL, G. M. Validity of the single processor approach [...]. AFIPS, 1967. | A de **acelerar** o mesmo problema (1967) |
| `[2] GUSTAFSON, J. CACM. 1988.` | sem título; periódico abreviado | GUSTAFSON, J. L. Reevaluating Amdahl's law. **Communications of the ACM**, New York, v. 31, n. 5, p. 532-533, 1988. | GUSTAFSON, J. L. Reevaluating Amdahl's law. Communications of the ACM, 1988. | G de **grande** problema (weak scaling), 21 anos depois |
| `[3] DEAN, J. et al. OSDI. 2004.` | sem título; "et al." com 2 autores | DEAN, J.; GHEMAWAT, S. MapReduce: simplified data processing on large clusters. In: SYMPOSIUM ON OPERATING SYSTEMS DESIGN AND IMPLEMENTATION, 6., 2004, San Francisco. **Proceedings** [...]. Berkeley: USENIX Association, 2004. p. 137-150. | DEAN, J.; GHEMAWAT, S. MapReduce: simplified data processing on large clusters. OSDI, 2004. | Ghemawat de novo (GFS 2003 → MapReduce 2004) |
| `[4] ZAHARIA, M. et al. NSDI. 2012.` | sem título | ZAHARIA, M. et al. Resilient distributed datasets: a fault-tolerant abstraction for in-memory cluster computing. In: USENIX SYMPOSIUM ON NETWORKED SYSTEMS DESIGN AND IMPLEMENTATION, 9., 2012, San Jose. **Proceedings** [...]. Berkeley: USENIX Association, 2012. p. 15-28. | ZAHARIA, M. et al. Resilient distributed datasets [...]. NSDI, 2012. | Z de Zaharia, o último modelo da história (RDD) |

### B.3 Ponto 3

| Atual | Problemas | ABNT completa (NBR 6023:2018) | Forma manuscrita | Mnemônico |
|---|---|---|---|---|
| `[1] AKIDAU, T. et al. PVLDB. 2015.` | sem título; periódico abreviado | AKIDAU, T. et al. The dataflow model: a practical approach to balancing correctness, latency, and cost in massive-scale, unbounded, out-of-order data processing. **Proceedings of the VLDB Endowment**, [s. l.], v. 8, n. 12, p. 1792-1803, 2015. | AKIDAU, T. et al. The dataflow model [...]. Proceedings of the VLDB Endowment, 2015. | — |
| `[2] CARBONE, P. et al. PVLDB. 2017.` | sem título; periódico abreviado | CARBONE, P. et al. State management in Apache Flink: consistent stateful distributed stream processing. **Proceedings of the VLDB Endowment**, [s. l.], v. 10, n. 12, p. 1718-1729, 2017. | CARBONE, P. et al. State management in Apache Flink [...]. PVLDB, 2017. | Carbone ≈ **carbono**: o Flink "conserva" o estado |
| `[3] KREPS, J. et al. NetDB. 2011.` | sem título; "et al." com 3 autores | KREPS, J.; NARKHEDE, N.; RAO, J. Kafka: a distributed messaging system for log processing. In: NETWORKING MEETS DATABASES WORKSHOP (NetDB), 2011, Athens. **Proceedings** [...]. [S. l.: s. n.], 2011. | KREPS, J.; NARKHEDE, N.; RAO, J. Kafka: a distributed messaging system for log processing. NetDB, 2011. | 3K: **K**reps, **K**afka, **K**appa |
| `[4] MARZ, N. et al. Manning. 2015.` | sem título; "et al." com 2 autores; local ausente | MARZ, N.; WARREN, J. **Big data**: principles and best practices of scalable real-time data systems. Shelter Island: Manning, 2015. | MARZ, N.; WARREN, J. Big data. Manning, 2015. | Marz ≈ **Mars**: a Lambda "vem de Marte" |

### B.4 Ponto 4

| Atual | Problemas | ABNT completa (NBR 6023:2018) | Forma manuscrita | Mnemônico |
|---|---|---|---|---|
| `[1] Fayyad, U. et al. AI Magazine. 1996.` | sobrenome em minúsculas; "et al." com 3 autores; sem título | FAYYAD, U.; PIATETSKY-SHAPIRO, G.; SMYTH, P. From data mining to knowledge discovery in databases. **AI Magazine**, [s. l.], v. 17, n. 3, p. 37-54, 1996. | FAYYAD, U.; PIATETSKY-SHAPIRO, G.; SMYTH, P. From data mining to knowledge discovery in databases. AI Magazine, 1996. | F-P-S → **FPS** (frames por segundo do KDD) |
| `[2] Tukey, J. W. Addison-Wesley. 1977.` | sobrenome em minúsculas; sem título; local ausente | TUKEY, J. W. **Exploratory data analysis**. Reading: Addison-Wesley, 1977. | TUKEY, J. W. Exploratory data analysis. Addison-Wesley, 1977. | Tukey ≈ **turkey** (peru); 1977 |
| `[3] Han, J. et al. Morgan Kaufmann. 2012.` | sobrenome em minúsculas; "et al." com 3 autores; sem título; sem edição | HAN, J.; KAMBER, M.; PEI, J. **Data mining**: concepts and techniques. 3. ed. Waltham: Morgan Kaufmann, 2012. | HAN, J.; PEI, J.; TONG, H. Data mining: concepts and techniques. 4. ed. Morgan Kaufmann, 2022. (atualizada) | Han-Pei-Tong → "**hão de pôr o tom**"; Kamber saiu, Tong entrou |
| `[4] Aggarwal, C. C. Springer. 2017.` | sobrenome em minúsculas; sem título; sem edição | AGGARWAL, C. C. **Outlier analysis**. 2. ed. Cham: Springer, 2017. | AGGARWAL, C. C. Outlier analysis. 2. ed. Springer, 2017. | — |

### B.5 Ponto 5

| Atual | Problemas | ABNT completa (NBR 6023:2018) | Forma manuscrita | Mnemônico |
|---|---|---|---|---|
| `[1] Bishop, C. M. Springer. 2006.` | sobrenome em minúsculas; sem título | BISHOP, C. M. **Pattern recognition and machine learning**. New York: Springer, 2006. | BISHOP, C. M. Pattern recognition and machine learning. Springer, 2006. | **Bishop** = bispo |
| `[2] Murphy, K. P. MIT Press. 2012.` | sobrenome em minúsculas; sem título | MURPHY, K. P. **Machine learning**: a probabilistic perspective. Cambridge, MA: MIT Press, 2012. | MURPHY, K. P. Machine learning: a probabilistic perspective. MIT Press, 2012. | lei de **Murphy** |
| `[3] Hastie, T. et al. Springer. 2009.` | sobrenome em minúsculas; "et al." com 3 autores; sem título; sem edição | HASTIE, T.; TIBSHIRANI, R.; FRIEDMAN, J. **The elements of statistical learning**: data mining, inference, and prediction. 2. ed. New York: Springer, 2009. | HASTIE, T.; TIBSHIRANI, R.; FRIEDMAN, J. The elements of statistical learning. 2. ed. Springer, 2009. | — |
| `[4] Goodfellow, I. et al. MIT Press. 2016.` | sobrenome em minúsculas; "et al." com 3 autores; sem título | GOODFELLOW, I.; BENGIO, Y.; COURVILLE, A. **Deep learning**. Cambridge, MA: MIT Press, 2016. | GOODFELLOW, I.; BENGIO, Y.; COURVILLE, A. Deep learning. MIT Press, 2016. | **Goodfellow** = bom sujeito |

### B.6 Ponto 6

| Atual | Problemas | ABNT completa (NBR 6023:2018) | Forma manuscrita | Mnemônico |
|---|---|---|---|---|
| `[1] Sutton, R. S. et al. MIT Press. 2018.` | sobrenome em minúsculas; "et al." com 2 autores; sem título; sem edição (2. ed.) | SUTTON, R. S.; BARTO, A. G. **Reinforcement learning**: an introduction. 2. ed. Cambridge, MA: MIT Press, 2018. | SUTTON, R. S.; BARTO, A. G. Reinforcement learning: an introduction. 2. ed. MIT Press, 2018. | — |
| `[2] Watkins, C. J. C. H. et al. Machine Learning. 1992.` | sobrenome em minúsculas; "et al." com 2 autores; sem título | WATKINS, C. J. C. H.; DAYAN, P. Q-learning. **Machine Learning**, [s. l.], v. 8, n. 3-4, p. 279-292, 1992. | WATKINS, C. J. C. H.; DAYAN, P. Q-learning. Machine Learning, 1992. | mesmo volume que Williams (Machine Learning, v. 8, 1992) |
| `[3] Williams, R. J. Machine Learning. 1992.` | sobrenome em minúsculas; sem título | WILLIAMS, R. J. Simple statistical gradient-following algorithms for connectionist reinforcement learning. **Machine Learning**, [s. l.], v. 8, n. 3-4, p. 229-256, 1992. | WILLIAMS, R. J. Simple statistical gradient-following algorithms [...]. Machine Learning, 1992. | — |
| `[4] Mnih, V. et al. Nature. 2015.` | sobrenome em minúsculas; sem título | MNIH, V. et al. Human-level control through deep reinforcement learning. **Nature**, London, v. 518, n. 7540, p. 529-533, 2015. | MNIH, V. et al. Human-level control through deep reinforcement learning. Nature, 2015. | — |

### B.7 Ponto 7

| Atual | Problemas | ABNT completa (NBR 6023:2018) | Forma manuscrita | Mnemônico |
|---|---|---|---|---|
| `[1] Sculley, D. et al. NeurIPS. 2015.` | sobrenome em minúsculas; sem título | SCULLEY, D. et al. Hidden technical debt in machine learning systems. In: CONFERENCE ON NEURAL INFORMATION PROCESSING SYSTEMS, 29., 2015, Montreal. **Advances in Neural Information Processing Systems 28**. [S. l.]: Curran Associates, 2015. p. 2503-2511. | SCULLEY, D. et al. Hidden technical debt in machine learning systems. NeurIPS, 2015. | Sculley ≈ **skull** (caveira): a dívida escondida |
| `[2] Amershi, S. et al. ICSE-SEIP. 2019.` | sobrenome em minúsculas; sem título | AMERSHI, S. et al. Software engineering for machine learning: a case study. In: INTERNATIONAL CONFERENCE ON SOFTWARE ENGINEERING: SOFTWARE ENGINEERING IN PRACTICE, 41., 2019, Montreal. **Proceedings** [...]. Piscataway: IEEE, 2019. p. 291-300. | AMERSHI, S. et al. Software engineering for machine learning: a case study. ICSE-SEIP, 2019. | nove etapas, 2019 |
| `[3] Kreuzberger, D. et al. IEEE Access. 2023.` | sobrenome em minúsculas; "et al." com 3 autores; sem título | KREUZBERGER, D.; KÜHL, N.; HIRSCHL, S. Machine learning operations (MLOps): overview, definition, and architecture. **IEEE Access**, [s. l.], v. 11, p. 31866-31879, 2023. | KREUZBERGER, D.; KÜHL, N.; HIRSCHL, S. Machine learning operations (MLOps): overview, definition, and architecture. IEEE Access, 2023. | **Kreuz–kühl–Hirsch** (alemão: cruz, fresco, cervo) |
| `[4] Breck, E. et al. IEEE BigData. 2017.` | sobrenome em minúsculas; sem título | BRECK, E. et al. The ML test score: a rubric for ML production readiness and technical debt reduction. In: IEEE INTERNATIONAL CONFERENCE ON BIG DATA, 2017, Boston. **Proceedings** [...]. Piscataway: IEEE, 2017. p. 1123-1132. | BRECK, E. et al. The ML test score [...]. IEEE BigData, 2017. | — |

### B.8 Ponto 8

| Atual | Problemas | ABNT completa (NBR 6023:2018) | Forma manuscrita | Mnemônico |
|---|---|---|---|---|
| `[1] Sculley, D. et al. NeurIPS. 2015.` | idem P7 | SCULLEY, D. et al. Hidden technical debt in machine learning systems. In: CONFERENCE ON NEURAL INFORMATION PROCESSING SYSTEMS, 29., 2015, Montreal. **Advances in Neural Information Processing Systems 28**. [S. l.]: Curran Associates, 2015. p. 2503-2511. | SCULLEY, D. et al. Hidden technical debt in machine learning systems. NeurIPS, 2015. | idem |
| `[2] Kreuzberger, D. et al. IEEE Access. 2023.` | idem P7 | KREUZBERGER, D.; KÜHL, N.; HIRSCHL, S. Machine learning operations (MLOps): overview, definition, and architecture. **IEEE Access**, [s. l.], v. 11, p. 31866-31879, 2023. | KREUZBERGER, D.; KÜHL, N.; HIRSCHL, S. Machine learning operations (MLOps): overview, definition, and architecture. IEEE Access, 2023. | idem |
| `[3] Breck, E. et al. IEEE BigData. 2017.` | idem P7 | BRECK, E. et al. The ML test score: a rubric for ML production readiness and technical debt reduction. In: IEEE INTERNATIONAL CONFERENCE ON BIG DATA, 2017, Boston. **Proceedings** [...]. Piscataway: IEEE, 2017. p. 1123-1132. | BRECK, E. et al. The ML test score [...]. IEEE BigData, 2017. | idem |
| `[4] Treveil, M. et al. O'Reilly. 2020.` | sobrenome em minúsculas; sem título; local ausente | TREVEIL, M. et al. **Introducing MLOps**: how to scale machine learning in the enterprise. Sebastopol: O'Reilly, 2020. | TREVEIL, M. et al. Introducing MLOps. O'Reilly, 2020. | — |

### B.9 Ponto 9

| Atual | Problemas | ABNT completa (NBR 6023:2018) | Forma manuscrita | Mnemônico |
|---|---|---|---|---|
| `[1] Sculley, D. et al. NeurIPS. 2015.` | idem P7 | SCULLEY, D. et al. Hidden technical debt in machine learning systems. In: CONFERENCE ON NEURAL INFORMATION PROCESSING SYSTEMS, 29., 2015, Montreal. **Advances in Neural Information Processing Systems 28**. [S. l.]: Curran Associates, 2015. p. 2503-2511. | SCULLEY, D. et al. Hidden technical debt in machine learning systems. NeurIPS, 2015. | idem |
| `[2] Gama, J. et al. ACM Computing Surveys. 2014.` | sobrenome em minúsculas; sem título | GAMA, J. et al. A survey on concept drift adaptation. **ACM Computing Surveys**, New York, v. 46, n. 4, art. 44, p. 1-37, 2014. | GAMA, J. et al. A survey on concept drift adaptation. ACM Computing Surveys, 2014. | **Gama** = faixa de valores que se desloca |
| `[3] Breck, E. et al. IEEE BigData. 2017.` | idem P7 | BRECK, E. et al. The ML test score: a rubric for ML production readiness and technical debt reduction. In: IEEE INTERNATIONAL CONFERENCE ON BIG DATA, 2017, Boston. **Proceedings** [...]. Piscataway: IEEE, 2017. p. 1123-1132. | BRECK, E. et al. The ML test score [...]. IEEE BigData, 2017. | idem |
| `[4] Kreuzberger, D. et al. IEEE Access. 2023.` | idem P7 | KREUZBERGER, D.; KÜHL, N.; HIRSCHL, S. Machine learning operations (MLOps): overview, definition, and architecture. **IEEE Access**, [s. l.], v. 11, p. 31866-31879, 2023. | KREUZBERGER, D.; KÜHL, N.; HIRSCHL, S. Machine learning operations (MLOps): overview, definition, and architecture. IEEE Access, 2023. | idem |

### B.10 Ponto 10

| Atual | Problemas | ABNT completa (NBR 6023:2018) | Forma manuscrita | Mnemônico |
|---|---|---|---|---|
| `[1] Molnar, C. Leanpub. 2022.` | sobrenome em minúsculas; sem título; sem edição | MOLNAR, C. **Interpretable machine learning**: a guide for making black box models explainable. 2. ed. [S. l.]: Leanpub, 2022. | MOLNAR, C. Interpretable machine learning. 3. ed. Leanpub, 2025. (atualizada) | 3ª edição em 2025 |
| `[2] Lundberg, S. M. et al. NeurIPS. 2017.` | sobrenome em minúsculas; "et al." com 2 autores; sem título | LUNDBERG, S. M.; LEE, S.-I. A unified approach to interpreting model predictions. In: CONFERENCE ON NEURAL INFORMATION PROCESSING SYSTEMS, 31., 2017, Long Beach. **Advances in Neural Information Processing Systems 30**. [S. l.]: Curran Associates, 2017. p. 4765-4774. | LUNDBERG, S. M.; LEE, S.-I. A unified approach to interpreting model predictions. NeurIPS, 2017. | — |
| `[3] Sundararajan, M. et al. ICML. 2017.` | sobrenome em minúsculas; "et al." com 3 autores; sem título | SUNDARARAJAN, M.; TALY, A.; YAN, Q. Axiomatic attribution for deep networks. In: INTERNATIONAL CONFERENCE ON MACHINE LEARNING, 34., 2017, Sydney. **Proceedings** [...]. [S. l.]: PMLR, 2017. p. 3319-3328. | SUNDARARAJAN, M.; TALY, A.; YAN, Q. Axiomatic attribution for deep networks. ICML, 2017. | S-T-Y → **sty** (inglês: chiqueiro) |
| `[4] Ribeiro, M. T. et al. KDD. 2016.` | sobrenome em minúsculas; "et al." com 3 autores; sem título | RIBEIRO, M. T.; SINGH, S.; GUESTRIN, C. "Why should I trust you?": explaining the predictions of any classifier. In: ACM SIGKDD INTERNATIONAL CONFERENCE ON KNOWLEDGE DISCOVERY AND DATA MINING, 22., 2016, San Francisco. **Proceedings** [...]. New York: ACM, 2016. p. 1135-1144. | RIBEIRO, M. T.; SINGH, S.; GUESTRIN, C. "Why should I trust you?" [...]. KDD, 2016. | **Ribeiro** = riacho; o LIME é "local" como um riacho |

