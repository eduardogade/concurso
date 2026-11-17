# Auditoria 1 — Matriz de cobertura

Data: 02/11/2026. Para cada ponto, liga critério oficial → exigência DeepSeek → evidência na dissertação → grau → impacto na nota.

**Convenções**

- "DS L" é a linha do subitem em `prova-escrita/barema-deepseek/ponto-N.note`.
- A evidência é dada por linhas do `_v2.md` do ponto, com a seção (§) entre parênteses.
- Peso = valor DeepSeek (normalizado no Ponto 7).
- Obtido = peso × grau; Perda = peso × (1 − grau), ambos na leitura literal R1.
- A linha de síntese de cada item mostra a conversão para R2 (central) e R3.
- Escala de graus, reclassificação [inexigível] e fórmulas: Relatório 1, seções A.3–A.6.
- Faixa entre colchetes após o grau (ex.: 0,75 [0,50–1,00]): alternativa usada só na análise de sensibilidade.

## Ponto 1 — Processamento de Dados em Larga Escala: Armazenamento e Gerenciamento Distribuído de Dados

Dissertação: `prova-escrita/1-pdle-armazenamento-e-gerenciamento-distribuido-de-dados_v2.md` · Barema DeepSeek: `prova-escrita/barema-deepseek/ponto-1.note`

### 1.1 — Domínio técnico/científico/crítico do ponto sorteado (máx. 2,5)

| DS L | Exigência DeepSeek | Prior. | Peso | Evidência na dissertação | Grau | Obtido | Perda | Observação |
|---|---|---|---|---|---|---|---|---|
| 6 | Definição formal de sistema de armazenamento distribuído e propriedades de particionamento, replicação e tolerância a falhas | E | 0,30 | L13–22 (§1.2) | 1,00 | 0,300 | 0,000 | Definição clara de armazenamento distribuído, com particionamento, replicação e tolerância a falhas. |
| 7 | Distinção entre armazenamento em bloco, arquivo e objeto, com critérios de escolha | E | 0,25 | L66 (§1.3.4); L70 (§1.3.4) | 0,50 [0,25–0,50] | 0,125 | 0,125 | Arquivo (DFS) e objeto caracterizados brevemente; armazenamento em bloco ausente; sem critérios de escolha. |
| 8 | Modelos de consistência: forte, eventual, causal e leituras/escritas monotônicas | E | 0,35 | L48–50 (§1.3.3) | 0,75 [0,50–0,75] | 0,263 | 0,087 | Linearizabilidade e consistência eventual bem definidas; causal e monotônicas ausentes (busca "causal", "monot": 0). |
| 9 | Teorema CAP e PACELC: interpretação correta e crítica a leituras simplistas | E | 0,30 | L40 (§1.3.2); L52–54 (§1.3.3); L81 (§1.4) | 0,75 [0,50–1,00] | 0,225 | 0,075 | CAP correto, com crítica ao "escolher dois de três"; PACELC não nomeado, mas o trade-off latência × consistência fora de partição aparece (40, 81). |
| 10 | Transações distribuídas: ACID, 2PC e limitações; BASE como contraponto | E | 0,30 | — | 0,00 | 0,000 | 0,300 | Transações distribuídas ausentes: busca "transa", "2PC", "duas fases" = 0 ("ACID" só casa com "capacidade"). |
| 11 | Particionamento/sharding: hash, range, consistência e hotspots | E | 0,25 | L28–34 (§1.3.1) | 1,00 | 0,250 | 0,000 | Sharding, intervalo × hash, skew/hotspots, rebalanceamento e consistent hashing. |
| 12 | Replicação: líder-seguidor, multi-líder, sem líder; quóruns e consistência | E | 0,30 | L38–44 (§1.3.2); L56–62 (§1.3.3) | 0,75 [0,75–1,00] | 0,225 | 0,075 | Líder-seguidor, sem líder e quóruns; multi-líder ausente. |
| 13 | Consenso e coordenação: Paxos/Raft, leader election, relógios lógicos e vector clocks (fronteira com o Ponto 2) | D | 0,20 | L44 (§1.3.2) | 0,25 | 0,050 | 0,150 | Eleição de líder por consenso só mencionada; Paxos/Raft e relógios lógicos ausentes. |
| 14 | Análise crítica: quando não usar NoSQL/eventual; custos de consistência, latência e complexidade operacional | E | 0,25 | L76–85 (§1.4) | 0,75 [0,75–1,00] | 0,188 | 0,062 | Trade-offs explícitos e "não existe arquitetura universalmente superior"; falta dizer quando não usar NoSQL/consistência eventual. |

Síntese 1.1: A = 1,625 (R1); essenciais exigíveis E = 2,300; R2 = 2,5 × min(1; 1,625/2,300) = **1,77**; R3 = 2,21.

### 1.2 — Abordagem das ideias fundamentais do conteúdo (máx. 2,5)

| DS L | Exigência DeepSeek | Prior. | Peso | Evidência na dissertação | Grau | Obtido | Perda | Observação |
|---|---|---|---|---|---|---|---|---|
| 16 | Arquitetura de DFS: namenode/datanodes, blocos, replicação e rack awareness (GFS/HDFS) | E | 0,35 | L22 (§1.2); L66 (§1.3.4) | 0,25 [0,25–0,50] | 0,087 | 0,263 | GFS citado; namenode/datanodes, blocos e rack awareness ausentes. |
| 17 | Object storage: buckets, objetos, metadados, durabilidade e consistência (modelo S3-like) | E | 0,30 | L70 (§1.3.4) | 0,25 [0,25–0,50] | 0,075 | 0,225 | Uma frase sobre objetos/metadados; buckets, durabilidade e consistência ausentes. |
| 18 | Key-value e wide-column stores: Bigtable/HBase, Dynamo/Cassandra e modelos de dados | E | 0,35 | L34 (§1.3.1); L68 (§1.3.4) | 0,50 | 0,175 | 0,175 | Bigtable e Dynamo situados, consistent hashing; modelos de dados (wide-column, KV) pouco desenvolvidos. |
| 19 | Bancos relacionais distribuídos/NewSQL: sharding, replicação e transações distribuídas | E | 0,30 | — | 0,00 | 0,000 | 0,300 | Bancos relacionais distribuídos/NewSQL ausentes (busca "NewSQL", "relaciona": 0). |
| 20 | Data lake e tabelas abertas: Parquet/ORC, catálogo e layout por partições (fronteira com o Ponto 3) | D | 0,25 | L70 (§1.3.4) | 0,25 | 0,062 | 0,188 | Data lakes mencionados; formatos/catálogo ausentes. |
| 21 | Estratégias de particionamento e rebalanceamento | E | 0,30 | L28–34 (§1.3.1) | 1,00 | 0,300 | 0,000 | Estratégias de particionamento e rebalanceamento desenvolvidas. |
| 22 | Estratégias de replicação e recuperação de falhas | E | 0,30 | L38–44 (§1.3.2) | 1,00 | 0,300 | 0,000 | Replicação, failover, detecção e restauração de réplicas. |
| 23 | Consistência e versionamento: MVCC, snapshots e timestamps | D | 0,20 | L62 (§1.3.3) | 0,00 | 0,000 | 0,200 | MVCC/snapshots ausentes; "coordenar versões" é tangencial. |
| 24 | Gerenciamento de metadados e catálogo | D | 0,15 | L70 (§1.3.4) | 0,25 [0,00–0,25] | 0,037 | 0,113 | Metadados só mencionados no armazenamento de objetos. |

Síntese 1.2: A = 1,038 (R1); essenciais exigíveis E = 1,900; R2 = 2,5 × min(1; 1,038/1,900) = **1,37**; R3 = 1,71.

### 1.4 — Atualização do conteúdo / referências bibliográficas / normas técnicas (máx. 1,0)

| DS L | Exigência DeepSeek | Prior. | Peso | Evidência na dissertação | Grau | Obtido | Perda | Observação |
|---|---|---|---|---|---|---|---|---|
| 26 | GFS (Ghemawat et al., 2003) e HDFS como referências clássicas | E | 0,15 | L22 (§1.2); L109 (Ref.) | 0,75 | 0,113 | 0,037 | GFS citado [1]; HDFS ausente. |
| 27 | Bigtable (Chang et al., 2006) e Dynamo (DeCandia et al., 2007) | E | 0,15 | L34 (§1.3.1); L68 (§1.3.4); L110 (Ref.); L113 (Ref.) | 1,00 | 0,150 | 0,000 | Dynamo [2] e Bigtable [5] citados. |
| 28 | Kleppmann, Designing Data-Intensive Applications (2017) | E | 0,15 | — | 0,00 | 0,000 | 0,150 | Kleppmann não citado. |
| 29 | Abadi (2012), consistency tradeoffs e PACELC | E | 0,10 | — | 0,00 | 0,000 | 0,100 | Abadi/PACELC não citado. |
| 30 | Documentação técnica atual de Apache Hadoop/HDFS, Apache Cassandra, Apache HBase e Amazon S3 (verificar versões) | E · inexig. | 0,20 | — | 0,00 | 0,000 | 0,200 | Nenhuma ferramenta atual (HDFS, Cassandra, HBase, S3) nomeada. |
| 31 | Parquet/ORC e catálogos (Apache Hive Metastore, Apache Iceberg) (fronteira com o Ponto 3) | D | 0,10 | — | 0,00 | 0,000 | 0,100 | Parquet/ORC/catálogos ausentes. |
| 32 | Özsu & Valduriez, Principles of Distributed Database Systems (verificar edição/ano) | D | 0,10 | — | 0,00 | 0,000 | 0,100 | Özsu & Valduriez não citado. |
| 33 | YCSB (Yahoo! Cloud Serving Benchmark) para avaliação de armazenamentos distribuídos | D · inexig. | 0,05 | — | 0,00 | 0,000 | 0,050 | YCSB ausente. |

Síntese 1.4: A = 0,263 (R1); essenciais exigíveis E = 0,550; R2 = 1,0 × min(1; 0,263/0,550) = **0,48**; R3 = 0,60.

### 1.5 — Aprofundamento do conteúdo (máx. 1,0)

| DS L | Exigência DeepSeek | Prior. | Peso | Evidência na dissertação | Grau | Obtido | Perda | Observação |
|---|---|---|---|---|---|---|---|---|
| 35 | Formalização de quórum R + W > N e trade-offs entre latência e consistência | E | 0,20 | L40 (§1.3.2); L56–62 (§1.3.3) | 0,75 [0,75–1,00] | 0,150 | 0,050 | R + W > N formalizado, com ressalva correta sobre o protocolo; o efeito de R e W na latência não é discutido. |
| 36 | CAP/PACELC com análise de latência e partição em cenários concretos | E | 0,15 | L52–54 (§1.3.3) | 0,50 | 0,075 | 0,075 | CAP sob partição descrito em abstrato, sem cenário concreto nem PACELC. |
| 37 | Complexidade e custos de replicação: fan-out, largura de banda e latência de consenso | D | 0,15 | L40 (§1.3.2); L83 (§1.4) | 0,50 | 0,075 | 0,075 | Latência da replicação síncrona; códigos de apagamento × replicação integral. |
| 38 | Hotspots e skew em sharding; técnicas de salting e rebalanceamento | E | 0,15 | L30–34 (§1.3.1) | 0,75 | 0,113 | 0,037 | Skew/hotspots e rebalanceamento; salting ausente. |
| 39 | Casos-limite: falha de coordenador, split-brain, stale reads e perda de quórum | E | 0,15 | L40 (§1.3.2); L44 (§1.3.2); L50 (§1.3.3) | 0,50 | 0,075 | 0,075 | Split-brain e distinção lentidão × falha; divergência temporária; perda de quórum e stale reads não tratados explicitamente. |
| 40 | Relação entre MVCC, snapshots e isolamento; anomalias de concorrência | E | 0,10 | — | 0,00 | 0,000 | 0,100 | MVCC/isolamento/anomalias ausentes. |
| 41 | Exemplo aplicado: modelagem de armazenamento para sessões/telemetria com escolha justificada de store | D | 0,10 | — | 0,00 | 0,000 | 0,100 | Sem exemplo aplicado (busca "exemplo": 0); os sistemas citados não substituem um cenário de decisão. |

Síntese 1.5: A = 0,487 (R1); essenciais exigíveis E = 0,750; R2 = 1,0 × min(1; 0,487/0,750) = **0,65**; R3 = 0,81.

### 1.3 e Item II — sem correspondente DeepSeek

| Critério oficial | Exigência DeepSeek | Evidência | Grau | Impacto |
|---|---|---|---|---|
| 1.3 Organização, coerência, clareza e sequência lógica de ideias | Nenhuma | Seções numeradas 1.1–1.5 com subseções 1.3.x; progressão introdução → fundamentos → núcleo → limitações → conclusão | 95% (hipótese) | 0,475 |
| 2.1 Uso adequado de terminologia técnico-científica | Nenhuma | Terminologia técnica consistente; termos em inglês destacados em itálico | 95% (hipótese) | 0,950 |
| 2.2 Estruturação coerente do texto com introdução, desenvolvimento e conclusão | Nenhuma | Introdução (L3), desenvolvimento e conclusão (L87) explícitos | 95% (hipótese) | 0,475 |
| 2.3 Precisão e objetividade | Nenhuma | Frases curtas, sem digressões; fórmulas e diagramas como síntese | 95% (hipótese) | 0,475 |
| 2.4 Correção ortográfica e gramatical | Nenhuma | Não avaliável integralmente no Markdown (manuscrito); nenhum erro observado no texto-fonte | 95% (hipótese) | 0,475 |

**Total do ponto:** R1 = 6,26 · R2 (central) = **7,11** · R3 = 8,17 · sensibilidade aos graus: 6,81 – 7,62.

## Ponto 2 — Processamento de Dados em Larga Escala: Processamento Paralelo e Distribuído em Larga Escala

Dissertação: `prova-escrita/2-pdle-processamento-paralelo-e-distribuido-em-larga-escala_v2.md` · Barema DeepSeek: `prova-escrita/barema-deepseek/ponto-2.note`

### 1.1 — Domínio técnico/científico/crítico do ponto sorteado (máx. 2,5)

| DS L | Exigência DeepSeek | Prior. | Peso | Evidência na dissertação | Grau | Obtido | Perda | Observação |
|---|---|---|---|---|---|---|---|---|
| 6 | Definição formal de processamento paralelo × distribuído: memória compartilhada × distribuída, acoplamento e implicações | E | 0,30 | L5–9 (§2.1) | 0,75 [0,75–1,00] | 0,225 | 0,075 | Memória compartilhada × memórias independentes com comunicação pela rede; acoplamento não discutido. |
| 7 | Taxonomia de paralelismo: paralelismo de dados, de tarefas e pipeline; granularidade e escala | E | 0,25 | L13 (§2.2); L31 (§2.2); L37–39 (§2.3.1) | 0,75 | 0,188 | 0,062 | Paralelismo de dados e de tarefas, granularidade e escala; paralelismo de pipeline ausente. |
| 8 | Modelos de execução: MapReduce, DAG/dataflow e BSP; propriedades e critérios de adequação | E | 0,35 | L65–81 (§2.3.3) | 0,75 | 0,263 | 0,087 | MapReduce e DAG com critério de adequação (batch × iterativo); BSP ausente (barreiras em 57 só tangenciam). |
| 9 | Métricas de desempenho: speedup, eficiência, throughput, latência; leis de Amdahl e Gustafson | E | 0,30 | L15–31 (§2.2); L43 (§2.3.1); L95 (§2.4) | 0,75 [0,75–1,00] | 0,225 | 0,075 | Speedup, eficiência e Amdahl formalizados; Gustafson só como weak scaling [2], sem a lei; throughput não discutido. |
| 10 | Sincronização e comunicação: barreiras, shuffle, dependências e custos de rede | E | 0,25 | L47–61 (§2.3.2) | 1,00 | 0,250 | 0,000 | Barreiras, shuffle, dependências e custo de rede (inclui a decomposição de T_total). |
| 11 | Tolerância a falhas: reexecução de tarefas, lineage, checkpoints e execução especulativa | E | 0,30 | L43 (§2.3.1); L73 (§2.3.3); L81–89 (§2.3.4) | 1,00 | 0,300 | 0,000 | Reexecução, lineage, checkpoint e execução especulativa. |
| 12 | Análise crítica: overhead de comunicação, skew, stragglers, limites de escala e quando não distribuir | E | 0,30 | L9 (§2.1); L93–107 (§2.4) | 1,00 [0,75–1,00] | 0,300 | 0,000 | Overhead, skew, stragglers, limites de escala; "quando não distribuir" implícito em 9 e 93. |
| 13 | Localidade de dados e relação entre armazenamento e processamento (fronteira com o Ponto 1) | D | 0,20 | L59 (§2.3.2); L73 (§2.3.3) | 1,00 | 0,200 | 0,000 | Localidade × balanceamento bem tratada. |
| 14 | Coordenação de recursos e consenso para escalonamento em cluster (fronteira com o Ponto 1) | D | 0,25 | L95 (§2.4); L97 (§2.4) | 0,25 | 0,062 | 0,188 | Só "gargalos centralizados" e "escalonamento adaptativo"; sem gerenciador de recursos ou consenso. |

Síntese 1.1: A = 2,013 (R1); essenciais exigíveis E = 2,050; R2 = 2,5 × min(1; 2,013/2,050) = **2,45**; R3 = 2,50.

### 1.2 — Abordagem das ideias fundamentais do conteúdo (máx. 2,5)

| DS L | Exigência DeepSeek | Prior. | Peso | Evidência na dissertação | Grau | Obtido | Perda | Observação |
|---|---|---|---|---|---|---|---|---|
| 16 | Modelo MapReduce: funções map, shuffle/sort e reduce; exemplo canônico de contagem de palavras | E | 0,35 | L67–75 (§2.3.3) | 0,75 | 0,263 | 0,087 | Map, shuffle e reduce corretos, com limitação para cargas iterativas; sem o exemplo de contagem de palavras. |
| 17 | Hadoop MapReduce e YARN: arquitetura de job, ResourceManager, NodeManager e containers | E | 0,30 | — | 0,00 | 0,000 | 0,300 | Hadoop/YARN ausentes (busca "YARN", "Hadoop": 0). |
| 18 | Spark: RDDs, linhagem, transformações/ações e avaliação preguiçosa | E | 0,35 | L81 (§2.3.4) | 0,50 | 0,175 | 0,175 | Spark com lineage e reutilização em memória; RDD, transformações/ações e avaliação preguiçosa ausentes. |
| 19 | DataFrames/Datasets e otimizador Catalyst no Spark SQL | D | 0,15 | — | 0,00 | 0,000 | 0,150 | DataFrames/Catalyst ausentes. |
| 20 | Escalonamento por DAG: estágios, dependências narrow/wide e barreiras de shuffle | E | 0,30 | L57 (§2.3.2); L61 (§2.3.2); L79 (§2.3.4) | 0,75 | 0,225 | 0,075 | Estágios separados por shuffles e barreiras; dependências narrow/wide não nomeadas. |
| 21 | Particionamento e paralelismo: partições, repartition/coalesce e número de tarefas | E | 0,25 | L37–41 (§2.3.1) | 0,50 | 0,125 | 0,125 | Granularidade e partições; repartition/coalesce e número de tarefas ausentes. |
| 22 | Operações distribuídas: joins broadcast e shuffle, groupBy e agregações | E | 0,35 | L61 (§2.3.2); L67 (§2.3.3); L99 (§2.4) | 0,50 [0,25–0,50] | 0,175 | 0,175 | Agregação por chave e agregação local; joins ausentes (busca "join": 0). |
| 23 | Tolerância a falhas em Spark: lineage, reexecução de tarefas e checkpoints | E | 0,25 | L81–89 (§2.3.4) | 1,00 | 0,250 | 0,000 | Lineage, recomputação e checkpointing. |
| 24 | Escalonamento de tarefas: localidade de dados, speculative execution e stragglers | D | 0,20 | L41–43 (§2.3.1); L59 (§2.3.2); L73 (§2.3.3) | 1,00 | 0,200 | 0,000 | Localidade, execução especulativa e stragglers. |

Síntese 1.2: A = 1,413 (R1); essenciais exigíveis E = 2,150; R2 = 2,5 × min(1; 1,413/2,150) = **1,64**; R3 = 2,05.

### 1.4 — Atualização do conteúdo / referências bibliográficas / normas técnicas (máx. 1,0)

| DS L | Exigência DeepSeek | Prior. | Peso | Evidência na dissertação | Grau | Obtido | Perda | Observação |
|---|---|---|---|---|---|---|---|---|
| 26 | Dean & Ghemawat, MapReduce (2004) | E | 0,15 | L67 (§2.3.3); L135 (Ref.) | 1,00 | 0,150 | 0,000 | Dean & Ghemawat [3]. |
| 27 | Zaharia et al., Resilient Distributed Datasets (2012) | E | 0,15 | L81 (§2.3.4); L136 (Ref.) | 1,00 | 0,150 | 0,000 | Zaharia et al. [4]. |
| 28 | Malewicz et al., Pregel (2010) | D | 0,10 | — | 0,00 | 0,000 | 0,100 | Pregel ausente. |
| 29 | Valiant, modelo BSP (1990) | D | 0,05 | — | 0,00 | 0,000 | 0,050 | Valiant/BSP ausente. |
| 30 | Kleppmann, Designing Data-Intensive Applications (2017) | E | 0,15 | — | 0,00 | 0,000 | 0,150 | Kleppmann não citado. |
| 31 | Dean & Barroso, The Tail at Scale (2013) | E | 0,10 | L43 (§2.3.1); L95 (§2.4) | 0,25 | 0,025 | 0,075 | Latência de cauda discutida, mas sem citar Dean & Barroso. |
| 32 | Documentação técnica atual de Apache Hadoop/MapReduce/YARN e Apache Spark (verificar versões) | E · inexig. | 0,15 | L81 (§2.3.4) | 0,25 | 0,037 | 0,113 | Spark nomeado; documentação não citada. |
| 33 | Apache Flink para processamento batch/stream unificado (fronteira com o Ponto 3) | D | 0,10 | — | 0,00 | 0,000 | 0,100 | Flink ausente. |
| 34 | Benchmarks HiBench e TPCx-HS (verificar versões) | D · inexig. | 0,05 | — | 0,00 | 0,000 | 0,050 | Benchmarks ausentes. |

Síntese 1.4: A = 0,362 (R1); essenciais exigíveis E = 0,550; R2 = 1,0 × min(1; 0,362/0,550) = **0,66**; R3 = 0,82.

### 1.5 — Aprofundamento do conteúdo (máx. 1,0)

| DS L | Exigência DeepSeek | Prior. | Peso | Evidência na dissertação | Grau | Obtido | Perda | Observação |
|---|---|---|---|---|---|---|---|---|
| 36 | Formalização de speedup S(n) = T1/Tn, eficiência e limites de Amdahl/Gustafson | E | 0,20 | L17–27 (§2.2); L31 (§2.2) | 0,75 [0,75–1,00] | 0,150 | 0,050 | Speedup, eficiência e Amdahl formalizados; a lei de Gustafson não é escrita. |
| 37 | Análise de custo de shuffle: rede, disco, serialização e efeito de particionamento | E | 0,20 | L61 (§2.3.2); L99 (§2.4) | 0,50 | 0,100 | 0,100 | Custo de rede, I/O e sincronização; serialização e efeito do particionamento ausentes. |
| 38 | Stragglers e speculative execution: causas e impacto na latência de cauda | E | 0,15 | L41–43 (§2.3.1); L95 (§2.4) | 1,00 | 0,150 | 0,000 | Causas (skew) e impacto na cauda. |
| 39 | Casos-limite: falha de executor, perda de partição e recomputação longa por lineage | E | 0,15 | L81–89 (§2.3.4); L97 (§2.4) | 0,75 | 0,113 | 0,037 | Perda de partição, recomputação × checkpoint e decisão de reexecutar. |
| 40 | Trade-offs: memória × disco, broadcast join × shuffle join e repartition × coalesce | E | 0,15 | L75 (§2.3.3); L81 (§2.3.4) | 0,25 | 0,037 | 0,113 | Memória × materialização tangenciado; joins e repartition/coalesce ausentes. |
| 41 | Relação não trivial entre localidade de dados, elasticidade e custo de serialização | D | 0,10 | L59 (§2.3.2) | 0,50 | 0,050 | 0,050 | Localidade × balanceamento; elasticidade e serialização ausentes. |
| 42 | Exemplo aplicado: pipeline de agregação em larga escala com escolha justificada de operadores | D | 0,05 | — | 0,00 | 0,000 | 0,050 | Sem exemplo aplicado. |

Síntese 1.5: A = 0,600 (R1); essenciais exigíveis E = 0,850; R2 = 1,0 × min(1; 0,600/0,850) = **0,71**; R3 = 0,88.

### 1.3 e Item II — sem correspondente DeepSeek

| Critério oficial | Exigência DeepSeek | Evidência | Grau | Impacto |
|---|---|---|---|---|
| 1.3 Organização, coerência, clareza e sequência lógica de ideias | Nenhuma | Seções numeradas 2.1–2.5 com subseções 2.3.x; progressão introdução → fundamentos → núcleo → limitações → conclusão | 95% (hipótese) | 0,475 |
| 2.1 Uso adequado de terminologia técnico-científica | Nenhuma | Terminologia técnica consistente; termos em inglês destacados em itálico | 95% (hipótese) | 0,950 |
| 2.2 Estruturação coerente do texto com introdução, desenvolvimento e conclusão | Nenhuma | Introdução (L3), desenvolvimento e conclusão (L109) explícitos | 95% (hipótese) | 0,475 |
| 2.3 Precisão e objetividade | Nenhuma | Frases curtas, sem digressões; fórmulas e diagramas como síntese | 95% (hipótese) | 0,475 |
| 2.4 Correção ortográfica e gramatical | Nenhuma | Não avaliável integralmente no Markdown (manuscrito); nenhum erro observado no texto-fonte | 95% (hipótese) | 0,475 |

**Total do ponto:** R1 = 7,24 · R2 (central) = **8,31** · R3 = 9,11 · sensibilidade aos graus: 8,12 – 8,42.

## Ponto 3 — Processamento de Dados em Larga Escala: Processamento de Fluxos e Arquiteturas de Dados

Dissertação: `prova-escrita/3-pdle-processamento-de-fluxos-e-arquiteturas-de-dados_v2.md` · Barema DeepSeek: `prova-escrita/barema-deepseek/ponto-3.note`

### 1.1 — Domínio técnico/científico/crítico do ponto sorteado (máx. 2,5)

| DS L | Exigência DeepSeek | Prior. | Peso | Evidência na dissertação | Grau | Obtido | Perda | Observação |
|---|---|---|---|---|---|---|---|---|
| 6 | Definição formal de stream e distinção entre dados limitados (batch) e ilimitados (stream) | E | 0,25 | L5 (§3.1); L13 (§3.2) | 1,00 | 0,250 | 0,000 | Bounded × unbounded e batch × fluxo. |
| 7 | Tempo de evento × tempo de ingestão × tempo de processamento; desordem e atrasos | E | 0,30 | L31–33 (§3.3.1) | 0,75 | 0,225 | 0,075 | Event time × processing time e desordem; ingestion time ausente. |
| 8 | Semânticas de entrega: at-most-once, at-least-once e exactly-once; implicações práticas | E | 0,30 | L57–59 (§3.3.2) | 1,00 | 0,300 | 0,000 | At-most-, at-least- e exactly-once com implicações. |
| 9 | Processamento com estado: estado chaveado, backends e recuperação | E | 0,25 | L47–55 (§3.3.2) | 0,75 | 0,188 | 0,062 | Estado por chave e recuperação; backends de estado ausentes. |
| 10 | Watermarks e tratamento de eventos atrasados; allowed lateness | E | 0,25 | L40–43 (§3.3.1); L79 (§3.4) | 1,00 | 0,250 | 0,000 | Watermark como estimativa, eventos tardios e lateness. |
| 11 | Janelas tumbling, sliding, session e global; triggers e eviction | E | 0,30 | L35 (§3.3.1); L41 (§3.3.1) | 0,75 | 0,225 | 0,075 | Tumbling, sliding, session e triggers; janela global e eviction ausentes. |
| 12 | Backpressure e controle de fluxo em pipelines de stream | D | 0,15 | L83–89 (§3.4) | 0,75 | 0,113 | 0,037 | Backlog quando produção > consumo, com backpressure ou elasticidade; mecanismo de propagação não descrito. |
| 13 | Log distribuído, partições, offsets e consumer groups (fronteira com o Ponto 1) | E | 0,25 | L25 (§3.2); L63–67 (§3.3.3) | 0,75 [0,50–0,75] | 0,188 | 0,062 | Log, partições, ordenação por partição, replay e consumidores independentes; offsets e consumer groups não nomeados. |
| 14 | Análise crítica: quando não usar streaming; custos, complexidade e limites do exactly-once | E | 0,30 | L15 (§3.2); L73 (§3.3.4); L79–93 (§3.4); L113 (§3.5) | 1,00 | 0,300 | 0,000 | Quando o batch é preferível, custo das garantias fortes e menor complexidade suficiente. |
| 15 | Trade-offs entre motores unificados batch/stream e pipelines especializados (fronteira com o Ponto 2) | D | 0,15 | L73 (§3.3.4); L75 (§3.3.4) | 0,50 | 0,075 | 0,075 | Kappa × batch e "modelos compatíveis"; trade-off de motores unificados pouco explícito. |

Síntese 1.1: A = 2,112 (R1); essenciais exigíveis E = 2,200; R2 = 2,5 × min(1; 2,112/2,200) = **2,40**; R3 = 2,50.

### 1.2 — Abordagem das ideias fundamentais do conteúdo (máx. 2,5)

| DS L | Exigência DeepSeek | Prior. | Peso | Evidência na dissertação | Grau | Obtido | Perda | Observação |
|---|---|---|---|---|---|---|---|---|
| 17 | Arquitetura Lambda: camadas batch, speed e serving; funcionamento e limitações | E | 0,30 | L71 (§3.3.4) | 0,75 | 0,225 | 0,075 | Camadas batch e velocidade com custo de duplicação; camada de serving não descrita no Lambda. |
| 18 | Arquitetura Kappa: log imutável, reprocessamento e stream único; limitações | E | 0,30 | L73 (§3.3.4) | 1,00 | 0,300 | 0,000 | Log durável e replay como caminho principal, com limitação. |
| 19 | Ingestão de dados: conectores, CDC e pipelines de eventos | E | 0,25 | L20 (§3.2); L102 (§3.5) | 0,25 | 0,062 | 0,188 | Ingestão só como etapa; conectores/CDC ausentes. |
| 20 | Kafka: tópicos, partições, replicação, offsets, retenção e consumer groups | E | 0,35 | L65–67 (§3.3.3) | 0,50 | 0,175 | 0,175 | Partições, retenção, replay e consumidores; tópicos, replicação e offsets ausentes. |
| 21 | Motores de stream: Flink, Kafka Streams e Spark Structured Streaming; operadores e janelas | E | 0,35 | L67 (§3.3.3) | 0,25 [0,25–0,50] | 0,087 | 0,263 | Papel da engine descrito em abstrato; nenhum motor (Flink, Kafka Streams, Spark) nomeado no texto. |
| 22 | Exactly-once fim a fim: checkpoints, transações e idempotência em sinks | E | 0,25 | L55–59 (§3.3.2) | 1,00 | 0,250 | 0,000 | Checkpoints, replay, idempotência e sink transacional. |
| 23 | Camadas de arquitetura: ingestão, armazenamento, processamento e serving; data lake/lakehouse (fronteira com o Ponto 1) | E | 0,25 | L20 (§3.2); L75 (§3.3.4); L99–111 (§3.5) | 1,00 | 0,250 | 0,000 | Cadeia ingestão → processamento → serving; data lake e lakehouse. |
| 24 | Orquestração de pipelines, DAGs e lineage | D | 0,20 | L91 (§3.4) | 0,25 | 0,050 | 0,150 | Lineage mencionado; orquestração ausente. |
| 25 | Padrões de serving: materialized views, CQRS e stores de leitura | E | 0,25 | L20 (§3.2); L110 (§3.5) | 0,25 | 0,062 | 0,188 | Serving só nomeado; views materializadas e CQRS ausentes. |

Síntese 1.2: A = 1,462 (R1); essenciais exigíveis E = 2,300; R2 = 2,5 × min(1; 1,462/2,300) = **1,59**; R3 = 1,99.

### 1.4 — Atualização do conteúdo / referências bibliográficas / normas técnicas (máx. 1,0)

| DS L | Exigência DeepSeek | Prior. | Peso | Evidência na dissertação | Grau | Obtido | Perda | Observação |
|---|---|---|---|---|---|---|---|---|
| 27 | Kreps et al., Kafka (2011) | E | 0,15 | L65 (§3.3.3); L119 (Ref.) | 1,00 | 0,150 | 0,000 | Kreps et al. [3]. |
| 28 | Akidau et al., The Dataflow Model (2015) | E | 0,15 | L37 (§3.3.1); L117 (Ref.) | 1,00 | 0,150 | 0,000 | Akidau et al. [1]. |
| 29 | Carbone et al., Apache Flink (2015) | E | 0,10 | L55 (§3.3.2); L118 (Ref.) | 1,00 [0,75–1,00] | 0,100 | 0,000 | Carbone et al. 2017 (gestão de estado no Flink) no lugar do artigo de 2015: obra equivalente do mesmo sistema. |
| 30 | Akidau, Chernyak & Lax, Streaming Systems (2018) | E | 0,10 | — | 0,00 | 0,000 | 0,100 | Streaming Systems não citado. |
| 31 | Marz & Warren, Big Data (2015) | E | 0,10 | L71 (§3.3.4); L120 (Ref.) | 1,00 | 0,100 | 0,000 | Marz & Warren [4]. |
| 32 | Kreps, Questioning the Lambda Architecture (2014) | E | 0,10 | L73 (§3.3.4) | 0,25 | 0,025 | 0,075 | Kappa descrita sem citar Kreps (2014). |
| 33 | Kleppmann, Designing Data-Intensive Applications (2017) | E | 0,10 | — | 0,00 | 0,000 | 0,100 | Kleppmann não citado. |
| 34 | Documentação atual de Apache Kafka, Apache Flink e Spark Structured Streaming (verificar versões) | E · inexig. | 0,15 | L65 (§3.3.3) | 0,25 | 0,037 | 0,113 | Kafka nomeado; documentação não citada. |
| 35 | Documentação de Apache Iceberg/Hudi/Delta Lake (fronteira com o Ponto 1) | D · inexig. | 0,05 | L75 (§3.3.4) | 0,25 | 0,013 | 0,037 | Lakehouse nomeado; Iceberg/Hudi/Delta ausentes. |

Síntese 1.4: A = 0,575 (R1); essenciais exigíveis E = 0,800; R2 = 1,0 × min(1; 0,575/0,800) = **0,72**; R3 = 0,90.

### 1.5 — Aprofundamento do conteúdo (máx. 1,0)

| DS L | Exigência DeepSeek | Prior. | Peso | Evidência na dissertação | Grau | Obtido | Perda | Observação |
|---|---|---|---|---|---|---|---|---|
| 37 | Formalização de watermarks: completude versus latência e heurísticas de avanço | E | 0,15 | L40–43 (§3.3.1); L79 (§3.4) | 0,75 | 0,113 | 0,037 | Completude × latência explícita; heurísticas de avanço do watermark ausentes. |
| 38 | Janelas e triggers: allowed lateness, modos de acumulação e emissão de resultados | E | 0,15 | L41–43 (§3.3.1); L79 (§3.4) | 0,75 [0,50–0,75] | 0,113 | 0,037 | Trigger, atualização tardia e lateness; modos de acumulação ausentes. |
| 39 | Exactly-once fim a fim: transações, idempotência e trade-offs com latência e custo | E | 0,15 | L59 (§3.3.2); L81 (§3.4) | 1,00 | 0,150 | 0,000 | Idempotência, transações e custo das garantias fortes. |
| 40 | Casos-limite: eventos além da latência permitida, partições quentes e falha de checkpoint | E | 0,15 | L43 (§3.3.1); L79 (§3.4); L83–89 (§3.4) | 0,25 [0,25–0,50] | 0,037 | 0,113 | Eventos tardios e backlog sustentado; partições quentes e falha de checkpoint ausentes. |
| 41 | Trade-offs Lambda × Kappa: reprocessamento, duplicação de código, latência e custo operacional | E | 0,15 | L71–73 (§3.3.4) | 1,00 | 0,150 | 0,000 | Reprocessamento, duplicação de lógica e infraestrutura, latência. |
| 42 | Relação entre ordenação por chave, partições e paralelismo em operadores stateful | D | 0,10 | L25 (§3.2); L47 (§3.3.2); L67 (§3.3.3) | 0,75 | 0,075 | 0,025 | Ordenação por partição e estado por chave. |
| 43 | Backpressure e skew em operadores stateful | D | 0,10 | L89 (§3.4) | 0,50 | 0,050 | 0,050 | Backpressure presente; skew ausente. |
| 44 | Exemplo aplicado: detecção de fraude/anomalia em tempo real com janelas e exactly-once | D | 0,05 | — | 0,00 | 0,000 | 0,050 | Sem exemplo aplicado. |

Síntese 1.5: A = 0,688 (R1); essenciais exigíveis E = 0,750; R2 = 1,0 × min(1; 0,688/0,750) = **0,92**; R3 = 1,00.

### 1.3 e Item II — sem correspondente DeepSeek

| Critério oficial | Exigência DeepSeek | Evidência | Grau | Impacto |
|---|---|---|---|---|
| 1.3 Organização, coerência, clareza e sequência lógica de ideias | Nenhuma | Seções numeradas 3.1–3.5 com subseções 3.3.x; progressão introdução → fundamentos → núcleo → limitações → conclusão | 95% (hipótese) | 0,475 |
| 2.1 Uso adequado de terminologia técnico-científica | Nenhuma | Terminologia técnica consistente; termos em inglês destacados em itálico | 95% (hipótese) | 0,950 |
| 2.2 Estruturação coerente do texto com introdução, desenvolvimento e conclusão | Nenhuma | Introdução (L3), desenvolvimento e conclusão (L95) explícitos | 95% (hipótese) | 0,475 |
| 2.3 Precisão e objetividade | Nenhuma | Frases curtas, sem digressões; fórmulas e diagramas como síntese | 95% (hipótese) | 0,475 |
| 2.4 Correção ortográfica e gramatical | Nenhuma | Não avaliável integralmente no Markdown (manuscrito); nenhum erro observado no texto-fonte | 95% (hipótese) | 0,475 |

**Total do ponto:** R1 = 7,69 · R2 (central) = **8,48** · R3 = 9,24 · sensibilidade aos graus: 8,32 – 8,62.

## Ponto 4 — Mineração de Dados: Descoberta de Conhecimento, Análise Exploratória de Dados, Identificação de Padrões e Anomalias

Dissertação: `prova-escrita/4-mineracao-de-dados-descoberta-de-conhecimento-aed-identificacao-de-padroes-e-anomalias_v2.md` · Barema DeepSeek: `prova-escrita/barema-deepseek/ponto-4.note`

### 1.1 — Domínio técnico/científico/crítico do ponto sorteado (máx. 2,5)

| DS L | Exigência DeepSeek | Prior. | Peso | Evidência na dissertação | Grau | Obtido | Perda | Observação |
|---|---|---|---|---|---|---|---|---|
| 6 | Definição formal de KDD (Knowledge Discovery in Databases) e distinção entre KDD e mineração de dados como etapa do processo | E | 0,30 | L5–13 (§4.1) | 1,00 | 0,300 | 0,000 | KDD definido e mineração como etapa (Data Mining ⊂ KDD). |
| 7 | Definição de Análise Exploratória de Dados (EDA) e seu papel no ciclo de descoberta | E | 0,25 | L49–57 (§4.3.1) | 1,00 | 0,250 | 0,000 | EDA definida, iterativa e orientadora da descoberta. |
| 8 | Definição formal de padrão e de anomalia/outlier, com critérios de distinção | E | 0,30 | L31 (§4.2); L81 (§4.3.2); L87–95 (§4.3.3) | 1,00 [0,75–1,00] | 0,300 | 0,000 | Padrão e anomalia definidos com critérios (global × local, tipos de anomalia). |
| 9 | Tipos de atributos e escalas de medida (nominal, ordinal, intervalar, razão) e implicações analíticas | E | 0,20 | — | 0,00 | 0,000 | 0,200 | Tipos de atributos e escalas de medida ausentes (busca "nominal", "ordinal", "escala": 0). |
| 10 | Medidas de similaridade e distância: Euclidiana, Manhattan, Jaccard e cosseno; critérios de escolha | E | 0,30 | L97–99 (§4.3.3) | 0,25 | 0,075 | 0,225 | Distância só mencionada; nenhuma medida (Euclidiana, Manhattan, Jaccard, cosseno). |
| 11 | Análise crítica da EDA: correlação não implica causalidade e riscos de viés de visualização | E | 0,25 | L57 (§4.3.1); L115–119 (§4.4) | 0,75 | 0,188 | 0,062 | Associação ≠ causalidade, com confundimento e causalidade reversa; achados da EDA como hipóteses; viés de visualização ausente. |
| 12 | Limitações: maldição da dimensionalidade e risco de overfitting em descoberta de padrões | E | 0,25 | L99 (§4.3.3); L103 (§4.4); L108–110 (§4.4) | 1,00 | 0,250 | 0,000 | Maldição da dimensionalidade e falsos positivos por múltiplas comparações. |
| 13 | Pré-processamento: limpeza, normalização, discretização e tratamento de valores ausentes | E | 0,30 | L25–26 (§4.2); L45 (§4.3.1) | 1,00 | 0,300 | 0,000 | Limpeza, ausentes, normalização, discretização e seleção de atributos. |
| 14 | Análise crítica de medidas de avaliação de padrões (ex.: suporte e confiança podem ser enganosos) | D | 0,15 | L77 (§4.3.2); L83 (§4.3.2) | 0,75 | 0,113 | 0,037 | Lift contra a independência e "frequência não é relevância". |
| 15 | Quando não usar métodos: clustering em alta dimensão sem redução, detecção de anomalias sem rótulos confiáveis | D | 0,20 | L99 (§4.3.3) | 0,25 | 0,050 | 0,150 | Perda de discriminação em alta dimensão; não diz explicitamente quando não usar. |

Síntese 1.1: A = 1,825 (R1); essenciais exigíveis E = 2,150; R2 = 2,5 × min(1; 1,825/2,150) = **2,12**; R3 = 2,50.

### 1.2 — Abordagem das ideias fundamentais do conteúdo (máx. 2,5)

| DS L | Exigência DeepSeek | Prior. | Peso | Evidência na dissertação | Grau | Obtido | Perda | Observação |
|---|---|---|---|---|---|---|---|---|
| 17 | Processo KDD: etapas de seleção, pré-processamento, transformação, mineração e interpretação/avaliação; natureza iterativa | E | 0,30 | L19–29 (§4.2) | 1,00 | 0,300 | 0,000 | Etapas do KDD e natureza não linear. |
| 18 | EDA: estatísticas descritivas (média, mediana, desvio padrão, quartis) e sua interpretação | E | 0,25 | L49 (§4.3.1) | 0,25 | 0,062 | 0,188 | Estatísticas descritivas só mencionadas (busca "média", "mediana", "quartil": 0). |
| 19 | EDA: visualizações (histograma, boxplot, dispersão, heatmap) e o que cada uma revela | E | 0,25 | L49–51 (§4.3.1) | 0,25 | 0,062 | 0,188 | Visualizações só mencionadas (busca "histograma", "boxplot", "dispersão": 0). |
| 20 | Análise de correlação: coeficientes de Pearson e Spearman e limitações | E | 0,20 | L49 (§4.3.1); L116–119 (§4.4) | 0,25 | 0,050 | 0,150 | Relações entre variáveis e limites causais; Pearson/Spearman ausentes. |
| 21 | Regras de associação: suporte, confiança e lift; algoritmo Apriori | E | 0,30 | L63–77 (§4.3.2) | 0,75 | 0,225 | 0,075 | Suporte, confiança e lift formalizados e interpretados; Apriori ausente. |
| 22 | Algoritmo FP-Growth e comparação com Apriori | D | 0,15 | — | 0,00 | 0,000 | 0,150 | FP-Growth ausente. |
| 23 | Agrupamento (clustering) como descoberta de padrões: k-means, hierárquico e DBSCAN (fronteira com o Ponto 5) | E | 0,30 | L79 (§4.3.2) | 0,25 | 0,075 | 0,225 | Agrupamento remetido explicitamente ao aprendizado não supervisionado; k-means, hierárquico e DBSCAN ausentes. |
| 24 | Detecção de anomalias: métodos estatísticos (z-score, intervalo interquartil) | E | 0,20 | L97 (§4.3.3) | 0,25 | 0,050 | 0,150 | "Distribuição estatística" só mencionada; z-score/IQR ausentes. |
| 25 | Detecção de anomalias: métodos baseados em distância (k-NN) e densidade (LOF) | E | 0,25 | L97 (§4.3.3) | 0,25 | 0,062 | 0,188 | "Distância, densidade, vizinhança" mencionadas; k-NN e LOF ausentes. |
| 26 | Isolation Forest e One-Class SVM (fronteira com o Ponto 5) | D | 0,15 | L97 (§4.3.3) | 0,25 [0,00–0,25] | 0,037 | 0,113 | "Isolamento" mencionado; Isolation Forest e One-Class SVM não nomeados. |
| 27 | Avaliação de padrões: medidas de interestingness e validação de resultados | D | 0,15 | L29 (§4.2); L105 (§4.4); L145 (§4.5) | 1,00 | 0,150 | 0,000 | Validade, novidade, utilidade e interpretabilidade; estabilidade e reprodutibilidade. |

Síntese 1.2: A = 1,075 (R1); essenciais exigíveis E = 2,050; R2 = 2,5 × min(1; 1,075/2,050) = **1,31**; R3 = 1,64.

### 1.4 — Atualização do conteúdo / referências bibliográficas / normas técnicas (máx. 1,0)

| DS L | Exigência DeepSeek | Prior. | Peso | Evidência na dissertação | Grau | Obtido | Perda | Observação |
|---|---|---|---|---|---|---|---|---|
| 29 | Fayyad, Piatetsky-Shapiro & Smyth (1996), From Data Mining to Knowledge Discovery in Databases | E | 0,10 | L13 (§4.1); L149 (Ref.) | 1,00 | 0,100 | 0,000 | Fayyad et al. [1]. |
| 30 | Han, Kamber & Pei, Data Mining: Concepts and Techniques (verificar edição) | E | 0,15 | L63 (§4.3.2); L151 (Ref.) | 1,00 | 0,150 | 0,000 | Han et al. [3]. |
| 31 | Tukey (1977), Exploratory Data Analysis | E | 0,10 | L49 (§4.3.1); L150 (Ref.) | 1,00 | 0,100 | 0,000 | Tukey [2]. |
| 32 | Chandola, Banerjee & Kumar (2009), Anomaly Detection: A Survey | E | 0,15 | L93–95 (§4.3.3) | 0,25 | 0,037 | 0,113 | Tipologia global/contextual/coletiva (de Chandola) presente, mas citando Aggarwal. |
| 33 | Aggarwal, Outlier Analysis (verificar edição) | E | 0,10 | L87 (§4.3.3); L152 (Ref.) | 1,00 | 0,100 | 0,000 | Aggarwal [4]. |
| 34 | CRISP-DM (Shearer, 2000) como processo padrão de mineração de dados | E | 0,10 | — | 0,00 | 0,000 | 0,100 | CRISP-DM ausente (busca "CRISP": 0). |
| 35 | Documentação atual de scikit-learn, pandas, matplotlib e seaborn (verificar versões) | E · inexig. | 0,15 | — | 0,00 | 0,000 | 0,150 | Nenhuma ferramenta nomeada. |
| 36 | Agrawal & Srikant (1994), Fast Algorithms for Mining Association Rules | E | 0,10 | L63–77 (§4.3.2) | 0,25 | 0,025 | 0,075 | Medidas de associação presentes; Apriori e Agrawal & Srikant ausentes. |
| 37 | Zimek, Schubert & Kriegel (2012), On the Evaluation of Unsupervised Outlier Detection | D | 0,05 | — | 0,00 | 0,000 | 0,050 | Zimek et al. ausente. |

Síntese 1.4: A = 0,512 (R1); essenciais exigíveis E = 0,800; R2 = 1,0 × min(1; 0,512/0,800) = **0,64**; R3 = 0,80.

### 1.5 — Aprofundamento do conteúdo (máx. 1,0)

| DS L | Exigência DeepSeek | Prior. | Peso | Evidência na dissertação | Grau | Obtido | Perda | Observação |
|---|---|---|---|---|---|---|---|---|
| 39 | Formalização de suporte, confiança e lift; propriedades (ex.: confiança não é simétrica) | E | 0,15 | L65–77 (§4.3.2) | 0,75 | 0,113 | 0,037 | Fórmulas e interpretação do lift; a assimetria da confiança não é dita. |
| 40 | Complexidade do Apriori (exponencial no pior caso) e otimizações via FP-Growth | E | 0,10 | — | 0,00 | 0,000 | 0,100 | Complexidade do Apriori/FP-Growth ausente. |
| 41 | Escolha de medida de distância e impacto em clustering/anomalias; efeito da alta dimensionalidade | E | 0,15 | L47 (§4.3.1); L99 (§4.3.3); L109 (§4.4) | 0,50 | 0,075 | 0,075 | Efeito da alta dimensionalidade e sensibilidade à representação; escolha da medida de distância ausente. |
| 42 | Sensibilidade a parâmetros: k em k-NN, eps/minPts em DBSCAN, contaminação em Isolation Forest | E | 0,15 | L109 (§4.4) | 0,25 | 0,037 | 0,113 | "Sensibilidade aos parâmetros" só mencionada. |
| 43 | Casos-limite: anomalias em alta dimensionalidade, dados categóricos e dados temporais | E | 0,15 | L81 (§4.3.2); L94 (§4.3.3); L99 (§4.3.3); L111 (§4.4) | 0,50 | 0,075 | 0,075 | Alta dimensionalidade, contexto e mudança temporal; dados categóricos ausentes. |
| 44 | Relação entre EDA e detecção automática de anomalias: visualização versus métodos algorítmicos | D | 0,10 | L49 (§4.3.1) | 0,25 | 0,025 | 0,075 | EDA examina "potenciais anomalias"; relação com detecção automática não desenvolvida. |
| 45 | Trade-offs em detecção de anomalias: precisão versus recall e custo de falsos positivos | E | 0,10 | L103 (§4.4) | 0,25 | 0,025 | 0,075 | Falsos positivos (múltiplas comparações); precisão × recall ausente. |
| 46 | Exemplo aplicado: detecção de fraude em transações com EDA e Isolation Forest | D | 0,10 | L89 (§4.3.3) | 0,00 | 0,000 | 0,100 | Fraude citada só como significado possível de anomalia; sem exemplo aplicado. |

Síntese 1.5: A = 0,350 (R1); essenciais exigíveis E = 0,800; R2 = 1,0 × min(1; 0,350/0,800) = **0,44**; R3 = 0,55.

### 1.3 e Item II — sem correspondente DeepSeek

| Critério oficial | Exigência DeepSeek | Evidência | Grau | Impacto |
|---|---|---|---|---|
| 1.3 Organização, coerência, clareza e sequência lógica de ideias | Nenhuma | Seções numeradas 4.1–4.5 com subseções 4.3.x; progressão introdução → fundamentos → núcleo → limitações → conclusão | 95% (hipótese) | 0,475 |
| 2.1 Uso adequado de terminologia técnico-científica | Nenhuma | Terminologia técnica consistente; termos em inglês destacados em itálico | 95% (hipótese) | 0,950 |
| 2.2 Estruturação coerente do texto com introdução, desenvolvimento e conclusão | Nenhuma | Introdução (L3), desenvolvimento e conclusão (L123) explícitos | 95% (hipótese) | 0,475 |
| 2.3 Precisão e objetividade | Nenhuma | Frases curtas, sem digressões; fórmulas e diagramas como síntese | 95% (hipótese) | 0,475 |
| 2.4 Correção ortográfica e gramatical | Nenhuma | Não avaliável integralmente no Markdown (manuscrito); nenhum erro observado no texto-fonte | 95% (hipótese) | 0,475 |

**Total do ponto:** R1 = 6,61 · R2 (central) = **7,36** · R3 = 8,34 · sensibilidade aos graus: 7,23 – 7,36.

## Ponto 5 — Aprendizado Supervisionado e Não Supervisionado

Dissertação: `prova-escrita/5-aprendizado-supervisionado-e-nao-supervisionado_v2.md` · Barema DeepSeek: `prova-escrita/barema-deepseek/ponto-5.note`

### 1.1 — Domínio técnico/científico/crítico do ponto sorteado (máx. 2,5)

| DS L | Exigência DeepSeek | Prior. | Peso | Evidência na dissertação | Grau | Obtido | Perda | Observação |
|---|---|---|---|---|---|---|---|---|
| 6 | Definição formal de aprendizado supervisionado (dados rotulados) e não supervisionado (sem rótulos), com objetivos distintos | E | 0,25 | L5–13 (§5.1) | 1,00 | 0,250 | 0,000 | Definições contrastadas pela disponibilidade da variável-alvo. |
| 7 | Formulação das tarefas: classificação, regressão, agrupamento e redução de dimensionalidade | E | 0,25 | L16 (§5.1); L54 (§5.3.1) | 1,00 | 0,250 | 0,000 | Classificação, regressão, agrupamento, redução de dimensionalidade, densidade e anomalias. |
| 8 | Risco esperado, risco empírico e minimização do risco empírico (ERM); função de perda | E | 0,30 | L22–28 (§5.2); L45–48 (§5.2) | 0,75 [0,50–0,75] | 0,225 | 0,075 | θ* = arg min L(θ) e erro empírico × generalização; o risco esperado não é formalizado. |
| 9 | Trade-off viés-variância; overfitting, underfitting e capacidade de generalização | E | 0,30 | L40 (§5.2); L108 (§5.4) | 1,00 | 0,300 | 0,000 | Viés-variância ligado a under/overfitting e à generalização. |
| 10 | Regularização L1/L2 e seu papel no controle de complexidade | E | 0,20 | L42–48 (§5.2) | 0,75 [0,50–0,75] | 0,150 | 0,050 | Penalização λ·complexidade e seu papel; L1/L2 não nomeadas (busca "L1", "ridge", "lasso": 0). |
| 11 | Validação: holdout, k-fold, validação estratificada e vazamento de dados (data leakage) | E | 0,25 | L32–36 (§5.2); L95–101 (§5.3.3); L112 (§5.4) | 0,75 [0,75–1,00] | 0,188 | 0,062 | Holdout, k-fold, independência do teste e data leakage; validação estratificada ausente. |
| 12 | Métricas de classificação: acurácia, precisão, recall, F1, ROC-AUC e PR-AUC; limitações | E | 0,30 | L87–89 (§5.3.3) | 0,75 [0,75–1,00] | 0,225 | 0,075 | Acurácia, precisão, recall, F1 e ROC-AUC, com a limitação do desbalanceamento; PR-AUC ausente. |
| 13 | Métricas de regressão: MSE, MAE e R²; interpretação e limitações | E | 0,15 | L91 (§5.3.3) | 0,75 [0,50–0,75] | 0,113 | 0,037 | MAE, MSE, RMSE e R² listados; interpretação mínima. |
| 14 | Análise crítica: desbalanceamento de classes, custos assimétricos de erro e métrica única enganosa | E | 0,20 | L87–89 (§5.3.3); L109 (§5.4); L122 (§5.4) | 1,00 | 0,200 | 0,000 | Desbalanceamento, custo assimétrico e métrica enganosa. |
| 15 | Distinção entre avaliação supervisionada e não supervisionada: critérios objetivos versus validação interna | D | 0,15 | L83 (§5.3.2); L93 (§5.3.3) | 1,00 | 0,150 | 0,000 | Avaliação não supervisionada "mais indireta" e seus critérios. |
| 16 | Quando não usar aprendizado supervisionado (rótulos escassos) ou não supervisionado (sem critério objetivo de validação) | D | 0,15 | L83 (§5.3.2); L116 (§5.4) | 0,25 | 0,037 | 0,113 | Contraindicações não explicitadas. |

Síntese 1.1: A = 2,087 (R1); essenciais exigíveis E = 2,200; R2 = 2,5 × min(1; 2,087/2,200) = **2,37**; R3 = 2,50.

### 1.2 — Abordagem das ideias fundamentais do conteúdo (máx. 2,5)

| DS L | Exigência DeepSeek | Prior. | Peso | Evidência na dissertação | Grau | Obtido | Perda | Observação |
|---|---|---|---|---|---|---|---|---|
| 18 | Regressão linear e regressão logística: hipóteses, funções de custo e estimação | E | 0,35 | L58 (§5.3.1) | 0,25 | 0,087 | 0,263 | Modelos lineares em uma linha; regressão logística, funções de custo e estimação ausentes. |
| 19 | Árvores de decisão: impureza (Gini/entropia), divisão e poda | E | 0,25 | L59 (§5.3.1) | 0,25 [0,25–0,50] | 0,062 | 0,188 | Árvores em uma linha (particionamento do espaço); impureza e poda ausentes. |
| 20 | Ensembles: bagging/Random Forest e boosting (AdaBoost/Gradient Boosting) | E | 0,35 | L60 (§5.3.1) | 0,25 [0,25–0,50] | 0,087 | 0,263 | Random Forest e boosting nomeados com mecanismo mínimo. |
| 21 | SVM: margem máxima, vetores de suporte, kernels e parâmetro C | E | 0,25 | L62 (§5.3.1) | 0,25 [0,25–0,50] | 0,062 | 0,188 | Só "máxima margem"; vetores de suporte, kernels e C ausentes. |
| 22 | Redes neurais: perceptron/MLP, funções de ativação e backpropagation | E | 0,20 | L63 (§5.3.1) | 0,25 | 0,050 | 0,150 | Redes neurais em uma linha. |
| 23 | k-means: funcionamento, inicialização k-means++, escolha de k e limitações | E | 0,30 | L77 (§5.3.2); L83 (§5.3.2) | 0,25 [0,25–0,50] | 0,075 | 0,225 | k-means em uma linha (centroides, dispersão intra-cluster); k-means++, escolha de k e limitações ausentes. |
| 24 | DBSCAN: eps, minPts, ruído e agrupamentos de forma arbitrária | E | 0,20 | L79 (§5.3.2) | 0,50 [0,25–0,50] | 0,100 | 0,100 | Regiões densas e ruído; eps/minPts ausentes. |
| 25 | PCA: componentes principais, variância explicada e redução de dimensionalidade | E | 0,25 | L80 (§5.3.2); L83 (§5.3.2) | 0,50 [0,50–0,75] | 0,125 | 0,125 | Direções de maior variância e variância explicada, em uma linha. |
| 26 | Avaliação não supervisionada: silhouette, Davies-Bouldin, inércia e limitações | E | 0,15 | L93 (§5.3.3) | 0,75 | 0,113 | 0,037 | Coesão, separação, silhouette e estabilidade; Davies-Bouldin e inércia não nomeados. |
| 27 | k-NN e maldição da dimensionalidade | D | 0,10 | L61 (§5.3.1); L114 (§5.4) | 0,25 | 0,025 | 0,075 | k-NN mencionado; maldição da dimensionalidade não associada a ele. |
| 28 | Agrupamento hierárquico: linkage e dendrograma | D | 0,10 | L78 (§5.3.2) | 0,25 | 0,025 | 0,075 | Hierárquico mencionado; linkage e dendrograma ausentes. |

Síntese 1.2: A = 0,812 (R1); essenciais exigíveis E = 2,300; R2 = 2,5 × min(1; 0,812/2,300) = **0,88**; R3 = 1,10.

### 1.4 — Atualização do conteúdo / referências bibliográficas / normas técnicas (máx. 1,0)

| DS L | Exigência DeepSeek | Prior. | Peso | Evidência na dissertação | Grau | Obtido | Perda | Observação |
|---|---|---|---|---|---|---|---|---|
| 30 | Hastie, Tibshirani & Friedman, The Elements of Statistical Learning (verificar edição) | E | 0,15 | L40 (§5.2); L152 (Ref.) | 1,00 | 0,150 | 0,000 | Hastie et al. [3]. |
| 31 | Bishop, Pattern Recognition and Machine Learning (2006) | E | 0,10 | L5 (§5.1); L150 (Ref.) | 1,00 | 0,100 | 0,000 | Bishop [1]. |
| 32 | Murphy, Machine Learning: A Probabilistic Perspective (2012) | E | 0,10 | L5 (§5.1); L151 (Ref.) | 1,00 | 0,100 | 0,000 | Murphy [2]. |
| 33 | James et al., An Introduction to Statistical Learning (verificar edição) | E | 0,10 | — | 0,00 | 0,000 | 0,100 | James et al. ausente. |
| 34 | Cortes & Vapnik (1995), Support-Vector Networks | E | 0,10 | L62 (§5.3.1) | 0,25 | 0,025 | 0,075 | SVM mencionado sem citar Cortes & Vapnik. |
| 35 | Breiman (2001), Random Forests | E | 0,10 | L60 (§5.3.1) | 0,25 | 0,025 | 0,075 | Random Forest mencionado sem citar Breiman. |
| 36 | Arthur & Vassilvitskii (2007), k-means++ | E | 0,10 | — | 0,00 | 0,000 | 0,100 | k-means++ ausente. |
| 37 | Ester et al. (1996), A Density-Based Algorithm for Discovering Clusters (DBSCAN) | E | 0,10 | L79 (§5.3.2) | 0,25 | 0,025 | 0,075 | DBSCAN mencionado sem citar Ester et al. |
| 38 | Documentação atual do scikit-learn (verificar versão) | E · inexig. | 0,10 | — | 0,00 | 0,000 | 0,100 | scikit-learn ausente. |
| 39 | Jolliffe, Principal Component Analysis (verificar edição) | D | 0,05 | — | 0,00 | 0,000 | 0,050 | Jolliffe ausente. |

Síntese 1.4: A = 0,425 (R1); essenciais exigíveis E = 0,850; R2 = 1,0 × min(1; 0,425/0,850) = **0,50**; R3 = 0,62.

### 1.5 — Aprofundamento do conteúdo (máx. 1,0)

| DS L | Exigência DeepSeek | Prior. | Peso | Evidência na dissertação | Grau | Obtido | Perda | Observação |
|---|---|---|---|---|---|---|---|---|
| 41 | Formalização de ERM e decomposição viés-variância | E | 0,15 | L25 (§5.2); L45 (§5.2) | 0,50 | 0,075 | 0,075 | Minimização da perda e objetivo regularizado; decomposição viés-variância não formalizada. |
| 42 | Regularização L1/L2: trade-off entre ajuste e complexidade; seleção de hiperparâmetros | E | 0,10 | L34 (§5.2); L38 (§5.2); L45–48 (§5.2) | 0,75 | 0,075 | 0,025 | Trade-off ajuste × complexidade via λ e hiperparâmetros escolhidos na validação; L1/L2 ausentes. |
| 43 | SVM: trade-offs de kernels e dos parâmetros C e gamma | E | 0,10 | — | 0,00 | 0,000 | 0,100 | Kernels, C e gamma ausentes. |
| 44 | k-means: complexidade, sensibilidade à inicialização e escolha de k; papel do k-means++ | E | 0,15 | — | 0,00 | 0,000 | 0,150 | Complexidade, inicialização e escolha de k ausentes. |
| 45 | DBSCAN: sensibilidade a eps/minPts e degradação em alta dimensionalidade | E | 0,15 | — | 0,00 | 0,000 | 0,150 | Sensibilidade do DBSCAN ausente. |
| 46 | PCA: variância explicada, limite linear e perda de interpretabilidade | E | 0,10 | L80 (§5.3.2); L83 (§5.3.2) | 0,25 | 0,025 | 0,075 | Variância explicada; limite linear e interpretabilidade ausentes. |
| 47 | Casos-limite: desbalanceamento, data leakage, overfitting em alta dimensão e validação inadequada | E | 0,15 | L89 (§5.3.3); L101 (§5.3.3); L112–114 (§5.4) | 1,00 | 0,150 | 0,000 | Desbalanceamento, leakage, alta dimensionalidade e validação inadequada. |
| 48 | Relação não trivial entre redução dimensional e clustering/classificação | D | 0,05 | — | 0,00 | 0,000 | 0,050 | Relação redução dimensional × clustering/classificação ausente. |
| 49 | Exemplo aplicado: pipeline com validação, escolha de modelo e comparação supervisionado × não supervisionado | D | 0,05 | — | 0,00 | 0,000 | 0,050 | Sem exemplo aplicado de pipeline. |

Síntese 1.5: A = 0,325 (R1); essenciais exigíveis E = 0,900; R2 = 1,0 × min(1; 0,325/0,900) = **0,36**; R3 = 0,45.

### 1.3 e Item II — sem correspondente DeepSeek

| Critério oficial | Exigência DeepSeek | Evidência | Grau | Impacto |
|---|---|---|---|---|
| 1.3 Organização, coerência, clareza e sequência lógica de ideias | Nenhuma | Seções numeradas 5.1–5.5 com subseções 5.3.x; progressão introdução → fundamentos → núcleo → limitações → conclusão | 95% (hipótese) | 0,475 |
| 2.1 Uso adequado de terminologia técnico-científica | Nenhuma | Terminologia técnica consistente; termos em inglês destacados em itálico | 95% (hipótese) | 0,950 |
| 2.2 Estruturação coerente do texto com introdução, desenvolvimento e conclusão | Nenhuma | Introdução (L3), desenvolvimento e conclusão (L124) explícitos | 95% (hipótese) | 0,475 |
| 2.3 Precisão e objetividade | Nenhuma | Frases curtas, sem digressões; fórmulas e diagramas como síntese | 95% (hipótese) | 0,475 |
| 2.4 Correção ortográfica e gramatical | Nenhuma | Não avaliável integralmente no Markdown (manuscrito); nenhum erro observado no texto-fonte | 95% (hipótese) | 0,475 |

**Total do ponto:** R1 = 6,50 · R2 (central) = **6,97** · R3 = 7,53 · sensibilidade aos graus: 6,73 – 7,47.

## Ponto 6 — Aprendizado por Reforço

Dissertação: `prova-escrita/6-aprendizado-por-reforco_v2.md` · Barema DeepSeek: `prova-escrita/barema-deepseek/ponto-6.note`

### 1.1 — Domínio técnico/científico/crítico do ponto sorteado (máx. 2,5)

| DS L | Exigência DeepSeek | Prior. | Peso | Evidência na dissertação | Grau | Obtido | Perda | Observação |
|---|---|---|---|---|---|---|---|---|
| 6 | Definição formal de Processo de Decisão de Markov (MDP): estados, ações, transições, recompensa e fator de desconto | E | 0,30 | L23–33 (§6.2) | 1,00 | 0,300 | 0,000 | Tupla (S, A, P, R, γ) e propriedade de Markov formalizadas. |
| 7 | Política, retorno descontado e funções de valor V^π e Q^π | E | 0,30 | L37–63 (§6.2) | 1,00 | 0,300 | 0,000 | Política, retorno descontado, V^π e Q^π. |
| 8 | Equações de Bellman esperadas e de otimalidade; relação entre avaliação e melhoria de política | E | 0,30 | L68 (§6.3.1); L75–89 (§6.3.2) | 1,00 | 0,300 | 0,000 | Bellman de expectativa (V^π) e de otimalidade (Q*); ciclo avaliação → melhoria. |
| 9 | Exploração versus exploitation e necessidade de exploração em ambientes desconhecidos | E | 0,25 | L97–106 (§6.3.3) | 1,00 | 0,250 | 0,000 | Exploração × explotação. |
| 10 | Distinção model-based × model-free e on-policy × off-policy | E | 0,30 | L116 (§6.3.4); L125 (§6.3.4) | 1,00 | 0,300 | 0,000 | On/off-policy e model-free/model-based. |
| 11 | Atribuição de crédito, recompensa atrasada, horizonte e papel do fator de desconto | E | 0,25 | L41 (§6.2); L47 (§6.2); L131 (§6.4) | 1,00 | 0,250 | 0,000 | Credit assignment e papel de γ. |
| 12 | Análise crítica: ineficiência amostral, instabilidade, reward hacking e risco de exploração insegura | E | 0,30 | L131–152 (§6.4) | 1,00 | 0,300 | 0,000 | Ineficiência amostral, instabilidade, reward hacking e safe RL. |
| 13 | Pressupostos de convergência e sensibilidade a hiperparâmetros (gamma, taxa de aprendizado, exploração) | E | 0,20 | L150 (§6.4) | 0,25 | 0,050 | 0,150 | Só sensibilidade a hiperparâmetros; pressupostos de convergência ausentes (busca "converg": 0). |
| 14 | Distinção entre RL e aprendizado supervisionado (fronteira com o Ponto 5) | E | 0,10 | L13 (§6.1) | 1,00 | 0,100 | 0,000 | Contraste com o aprendizado supervisionado. |
| 15 | Quando não usar RL: se há supervisão, planejamento ou bandit simples suficiente | D | 0,20 | — | 0,00 | 0,000 | 0,200 | Quando não usar RL: ausente. |

Síntese 1.1: A = 2,150 (R1); essenciais exigíveis E = 2,300; R2 = 2,5 × min(1; 2,150/2,300) = **2,34**; R3 = 2,50.

### 1.2 — Abordagem das ideias fundamentais do conteúdo (máx. 2,5)

| DS L | Exigência DeepSeek | Prior. | Peso | Evidência na dissertação | Grau | Obtido | Perda | Observação |
|---|---|---|---|---|---|---|---|---|
| 17 | Loop agente-ambiente; episódios versus tarefas contínuas | E | 0,25 | L5–11 (§6.1) | 0,75 | 0,188 | 0,062 | Ciclo agente-ambiente formalizado; episódico × contínuo não distinguido. |
| 18 | Retorno descontado e políticas determinísticas versus estocásticas | E | 0,20 | L37–41 (§6.2); L53 (§6.3.1); L118 (§6.3.4) | 0,75 | 0,150 | 0,050 | Retorno descontado e política estocástica; determinística × estocástica não contrastadas. |
| 19 | Programação dinâmica: avaliação de política, policy iteration e value iteration | E | 0,25 | L89 (§6.3.2) | 0,25 | 0,062 | 0,188 | Policy/value iteration só mencionadas. |
| 20 | Monte Carlo: estimação por retornos e variantes primeira visita/todas as visitas | E | 0,20 | L95 (§6.3.2) | 0,25 [0,00–0,25] | 0,050 | 0,150 | Monte Carlo ausente (busca: 0); só aludido em "sem aguardar o término do episódio". |
| 21 | TD(0): atualização por diferença temporal e comparação com Monte Carlo | E | 0,25 | L89–95 (§6.3.2) | 0,75 | 0,188 | 0,062 | Atualização TD(0) e bootstrapping; comparação com MC só implícita. |
| 22 | Q-learning (off-policy) e SARSA (on-policy) | E | 0,30 | L110–116 (§6.3.4) | 1,00 | 0,300 | 0,000 | Atualização do Q-learning, off-policy × SARSA on-policy. |
| 23 | ε-greedy, softmax e decaimento da exploração | E | 0,20 | L104 (§6.3.3) | 0,50 | 0,100 | 0,100 | ε-greedy; softmax e decaimento ausentes. |
| 24 | DQN: aproximação de função, experience replay e target network | E | 0,30 | L127 (§6.3.4) | 0,25 | 0,075 | 0,225 | Deep RL com aproximadores [4]; experience replay e target network ausentes (busca "DQN", "replay": 0). |
| 25 | Policy gradient/REINFORCE e actor-critic | E | 0,25 | L118–123 (§6.3.4) | 1,00 [0,75–1,00] | 0,250 | 0,000 | Policy gradient [3] e actor-critic. |
| 26 | Bandit multi-armado: exploração, recompensa e regret | D | 0,15 | — | 0,00 | 0,000 | 0,150 | Bandits ausentes. |
| 27 | Model-based RL: Dyna e uso de planejamento | D | 0,10 | L125 (§6.3.4) | 0,50 | 0,050 | 0,050 | Model-based com planejamento; Dyna ausente. |
| 28 | Exemplo aplicado canônico (gridworld ou CartPole) | D | 0,05 | — | 0,00 | 0,000 | 0,050 | Sem exemplo canônico. |

Síntese 1.2: A = 1,413 (R1); essenciais exigíveis E = 2,200; R2 = 2,5 × min(1; 1,413/2,200) = **1,61**; R3 = 2,01.

### 1.4 — Atualização do conteúdo / referências bibliográficas / normas técnicas (máx. 1,0)

| DS L | Exigência DeepSeek | Prior. | Peso | Evidência na dissertação | Grau | Obtido | Perda | Observação |
|---|---|---|---|---|---|---|---|---|
| 30 | Sutton & Barto, Reinforcement Learning: An Introduction (2ª ed., 2018) | E | 0,20 | L5 (§6.1); L176 (Ref.) | 1,00 | 0,200 | 0,000 | Sutton & Barto [1]. |
| 31 | Bellman (1957), Dynamic Programming | E | 0,10 | L75–87 (§6.3.2) | 0,25 | 0,025 | 0,075 | Equações de Bellman sem citar Bellman (1957). |
| 32 | Watkins & Dayan (1992), Q-learning | E | 0,10 | L110 (§6.3.4); L177 (Ref.) | 1,00 | 0,100 | 0,000 | Watkins & Dayan [2]. |
| 33 | Mnih et al. (2015), Human-level control through deep reinforcement learning | E | 0,15 | L127 (§6.3.4); L179 (Ref.) | 1,00 | 0,150 | 0,000 | Mnih et al. [4]. |
| 34 | Williams (1992), Simple Statistical Gradient-Following Algorithms for Connectionist Reinforcement Learning | E | 0,10 | L118 (§6.3.4); L178 (Ref.) | 1,00 | 0,100 | 0,000 | Williams [3]. |
| 35 | Schulman et al. (2017), Proximal Policy Optimization Algorithms | E | 0,10 | — | 0,00 | 0,000 | 0,100 | PPO ausente. |
| 36 | Puterman (1994), Markov Decision Processes | D | 0,10 | — | 0,00 | 0,000 | 0,100 | Puterman ausente. |
| 37 | Documentação atual de Gymnasium, Stable-Baselines3 e RLlib (verificar versões) | E · inexig. | 0,15 | — | 0,00 | 0,000 | 0,150 | Ferramentas ausentes. |

Síntese 1.4: A = 0,575 (R1); essenciais exigíveis E = 0,750; R2 = 1,0 × min(1; 0,575/0,750) = **0,77**; R3 = 0,96.

### 1.5 — Aprofundamento do conteúdo (máx. 1,0)

| DS L | Exigência DeepSeek | Prior. | Peso | Evidência na dissertação | Grau | Obtido | Perda | Observação |
|---|---|---|---|---|---|---|---|---|
| 39 | Operador de Bellman como contração e convergência de métodos de valor | E | 0,15 | — | 0,00 | 0,000 | 0,150 | Contração/convergência ausentes. |
| 40 | Condições de convergência do Q-learning: exploração suficiente, taxas decrescentes e ambiente finito | E | 0,10 | — | 0,00 | 0,000 | 0,100 | Condições de convergência do Q-learning ausentes. |
| 41 | Deadly triad: aproximação de função, bootstrapping e off-policy | E | 0,15 | L95 (§6.3.2); L116 (§6.3.4); L150 (§6.4) | 0,25 | 0,037 | 0,113 | Aproximação, bootstrapping e off-policy aparecem separados; a tríade não é articulada. |
| 42 | Trade-off Monte Carlo × TD: viés, variância e eficiência amostral | E | 0,10 | — | 0,00 | 0,000 | 0,100 | MC × TD (viés/variância) ausente. |
| 43 | Exploração formal: regret, UCB e Thompson sampling em bandits | D | 0,05 | — | 0,00 | 0,000 | 0,050 | Regret/UCB/Thompson ausentes. |
| 44 | Reward shaping e shaping baseado em potenciais | D | 0,05 | L135–141 (§6.4) | 0,25 | 0,013 | 0,037 | Especificação da recompensa e reward hacking; shaping não tratado. |
| 45 | Superestimação no DQN e Double DQN | D | 0,10 | — | 0,00 | 0,000 | 0,100 | Double DQN ausente. |
| 46 | PPO: objetivo truncado e trade-offs entre estabilidade e eficiência amostral | E | 0,10 | — | 0,00 | 0,000 | 0,100 | PPO ausente. |
| 47 | Casos-limite: recompensas esparsas, ações contínuas, não estacionariedade e sim-to-real | E | 0,15 | L118 (§6.3.4); L131 (§6.4); L152 (§6.4) | 1,00 [0,75–1,00] | 0,150 | 0,000 | Recompensas esparsas, ações contínuas e mudança de dinâmica entre treino e implantação. |
| 48 | Exemplo aprofundado: comparação Q-learning × policy gradient em ambiente com recompensa esparsa | D | 0,05 | — | 0,00 | 0,000 | 0,050 | Sem exemplo comparativo. |

Síntese 1.5: A = 0,200 (R1); essenciais exigíveis E = 0,750; R2 = 1,0 × min(1; 0,200/0,750) = **0,27**; R3 = 0,33.

### 1.3 e Item II — sem correspondente DeepSeek

| Critério oficial | Exigência DeepSeek | Evidência | Grau | Impacto |
|---|---|---|---|---|
| 1.3 Organização, coerência, clareza e sequência lógica de ideias | Nenhuma | Seções numeradas 6.1–6.5 com subseções 6.3.x; progressão introdução → fundamentos → núcleo → limitações → conclusão | 95% (hipótese) | 0,475 |
| 2.1 Uso adequado de terminologia técnico-científica | Nenhuma | Terminologia técnica consistente; termos em inglês destacados em itálico | 95% (hipótese) | 0,950 |
| 2.2 Estruturação coerente do texto com introdução, desenvolvimento e conclusão | Nenhuma | Introdução (L3), desenvolvimento e conclusão (L154) explícitos | 95% (hipótese) | 0,475 |
| 2.3 Precisão e objetividade | Nenhuma | Frases curtas, sem digressões; fórmulas e diagramas como síntese | 95% (hipótese) | 0,475 |
| 2.4 Correção ortográfica e gramatical | Nenhuma | Não avaliável integralmente no Markdown (manuscrito); nenhum erro observado no texto-fonte | 95% (hipótese) | 0,475 |

**Total do ponto:** R1 = 7,19 · R2 (central) = **7,83** · R3 = 8,65 · sensibilidade aos graus: 7,65 – 7,83.

## Ponto 7 — MLOps: Desenvolvimento, Versionamento e Experimentação de Modelos

Dissertação: `prova-escrita/7-mlops-desenvolvimento-versionamento-e-experimentacao-de-modelos_v2.md` · Barema DeepSeek: `prova-escrita/barema-deepseek/ponto-7.note`

### 1.1 — Domínio técnico/científico/crítico do ponto sorteado (máx. 2,5)

| DS L | Exigência DeepSeek | Prior. | Peso | Evidência na dissertação | Grau | Obtido | Perda | Observação |
|---|---|---|---|---|---|---|---|---|
| 6 | Definição formal de MLOps e delimitação do escopo de desenvolvimento, versionamento e experimentação frente à operação | E | 0,278 | L15–17 (§7.1) | 0,75 [0,75–1,00] | 0,208 | 0,069 | Objetivo do MLOps neste recorte e delimitação explícita; definição geral de MLOps ausente. |
| 7 | Ciclo de vida de ML e diferenças em relação ao software tradicional: dados como código, não determinismo e dívida técnica | E | 0,333 | L7–10 (§7.1); L39 (§7.3.1); L81 (§7.3.3) | 0,75 | 0,250 | 0,083 | Modelo ≠ código, dados e ambiente versionados, não determinismo; dívida técnica não nomeada. |
| 8 | Reprodutibilidade formal: determinismo, sementes, ambientes, linhagem e artefatos imutáveis | E | 0,333 | L49 (§7.3.1); L57 (§7.3.2); L67–81 (§7.3.3) | 1,00 | 0,333 | 0,000 | Seeds, ambiente, linhagem e imutabilidade; reprodutível ≠ bit a bit. |
| 9 | Versionamento de código, dados, modelo, configuração e ambiente; identificação e rastreabilidade | E | 0,333 | L39–49 (§7.3.1) | 1,00 | 0,333 | 0,000 | Código, dados, configuração, ambiente, modelos e checkpoints, com IDs imutáveis. |
| 10 | Experimentação: hipótese, variáveis, métricas, validação e comparação justa de experimentos | E | 0,278 | L13 (§7.1); L21–29 (§7.2); L61–63 (§7.3.2) | 1,00 | 0,278 | 0,000 | Hipótese, entradas/saídas, métricas e comparação justa. |
| 11 | Dívida técnica em ML: entanglement, undeclared consumers, pipeline jungles e glue code | E | 0,333 | L7 (§7.1); L151 (Ref.) | 0,25 | 0,083 | 0,250 | Sculley citado, mas os tipos de dívida técnica estão ausentes (busca "dívida", "entanglement", "glue": 0). |
| 12 | Análise crítica: vazamento de dados, overfitting de benchmark, seleção enviesada e comparação não controlada | E | 0,333 | L63 (§7.3.2); L89 (§7.3.4) | 0,50 | 0,167 | 0,167 | Comparação não controlada e "melhor ≠ maior métrica isolada"; leakage e overfitting de benchmark ausentes (busca: 0). |
| 13 | Distinção entre avaliação offline e online (fronteira com o Ponto 9) | D | 0,278 | L17 (§7.1) | 0,00 | 0,000 | 0,278 | O recorte exclui a produção, mas avaliação offline × online não é discutida. |

Síntese 1.1: A = 1,653 (R1); essenciais exigíveis E = 2,222; R2 = 2,5 × min(1; 1,653/2,222) = **1,86**; R3 = 2,32. Pesos normalizados ×1,1111.

### 1.2 — Abordagem das ideias fundamentais do conteúdo (máx. 2,5)

| DS L | Exigência DeepSeek | Prior. | Peso | Evidência na dissertação | Grau | Obtido | Perda | Observação |
|---|---|---|---|---|---|---|---|---|
| 15 | Processo CRISP-DM e ciclo iterativo de desenvolvimento de modelos | E | 0,25 | L5 (§7.1); L13 (§7.1) | 0,50 | 0,125 | 0,125 | Ciclo iterativo [2]; CRISP-DM ausente. |
| 16 | Estruturação de projeto: organização de código, notebooks versus scripts, módulos e configuração | E | 0,25 | — | 0,00 | 0,000 | 0,250 | Estrutura de projeto (notebooks × scripts, módulos) ausente. |
| 17 | Controle de versão de código com Git e boas práticas de branches, commits e tags | E | 0,25 | L49 (§7.3.1) | 0,25 | 0,062 | 0,188 | Só "commits"; Git e boas práticas ausentes. |
| 18 | Versionamento de dados: DVC, hashes, armazenamento remoto e reprodutibilidade | E | 0,30 | L39 (§7.3.1); L49 (§7.3.1) | 0,50 | 0,150 | 0,150 | Dados versionados com hashes; DVC e armazenamento remoto ausentes. |
| 19 | Versionamento de modelos e artefatos: model registry, metadados, estágios e linhagem | E | 0,30 | L41–49 (§7.3.1); L105 (§7.3.4) | 1,00 | 0,300 | 0,000 | Artefatos, linhagem e model registry com metadados e estados. |
| 20 | Rastreamento de experimentos: parâmetros, métricas, artefatos, runs e comparação (MLflow, W&B, TensorBoard) | E | 0,30 | L53–63 (§7.3.2) | 0,75 [0,75–1,00] | 0,225 | 0,075 | Conteúdo do tracking completo; nenhuma ferramenta (MLflow, W&B) nomeada. |
| 21 | Gestão de hiperparâmetros: grid/random/Bayesian optimization e registro dos trials | E | 0,25 | L56 (§7.3.2) | 0,25 | 0,062 | 0,188 | Hiperparâmetros registrados; estratégias de busca ausentes. |
| 22 | Ambientes reprodutíveis: dependências, containers, seeds e configuração | E | 0,25 | L39 (§7.3.1); L57 (§7.3.2); L73–75 (§7.3.3) | 0,75 | 0,188 | 0,062 | Dependências, ambiente e seed; containers ausentes. |
| 23 | Documentação de experimentos e model cards | D | 0,20 | L113 (§7.4) | 0,25 | 0,050 | 0,150 | "Documentação incompleta" como desafio; model cards ausentes. |
| 24 | Testes de dados e validação de esquema | D | 0,15 | L87 (§7.3.4) | 1,00 | 0,150 | 0,000 | Validação de esquema, tipos, ausentes, integridade e distribuição. |

Síntese 1.2: A = 1,312 (R1); essenciais exigíveis E = 2,150; R2 = 2,5 × min(1; 1,312/2,150) = **1,53**; R3 = 1,91.

### 1.4 — Atualização do conteúdo / referências bibliográficas / normas técnicas (máx. 1,0)

| DS L | Exigência DeepSeek | Prior. | Peso | Evidência na dissertação | Grau | Obtido | Perda | Observação |
|---|---|---|---|---|---|---|---|---|
| 26 | Sculley et al. (2015), Hidden Technical Debt in Machine Learning Systems | E | 0,136 | L7 (§7.1); L151 (Ref.) | 1,00 | 0,136 | 0,000 | Sculley et al. [1]. |
| 27 | Breck et al. (2017), The ML Test Score | E | 0,091 | L85 (§7.3.4); L154 (Ref.) | 1,00 | 0,091 | 0,000 | Breck et al. [4]. |
| 28 | Zaharia et al. (2018), Accelerating the Machine Learning Lifecycle with MLflow | E | 0,136 | L53–63 (§7.3.2) | 0,25 | 0,034 | 0,102 | Conceito de tracking presente; MLflow não citado. |
| 29 | Shearer (2000), CRISP-DM | E | 0,091 | — | 0,00 | 0,000 | 0,091 | CRISP-DM ausente. |
| 30 | Mitchell et al. (2019), Model Cards for Model Reporting | E | 0,091 | — | 0,00 | 0,000 | 0,091 | Model cards ausentes. |
| 31 | Gebru et al. (2021), Datasheets for Datasets | E | 0,091 | — | 0,00 | 0,000 | 0,091 | Datasheets ausentes. |
| 32 | Vartak et al. (2016), ModelDB | D | 0,091 | — | 0,00 | 0,000 | 0,091 | ModelDB ausente. |
| 33 | Snoek et al. (2012), Practical Bayesian Optimization of Machine Learning Algorithms | D | 0,091 | — | 0,00 | 0,000 | 0,091 | Snoek et al. ausente. |
| 34 | Documentação atual de Git, DVC, MLflow, Weights & Biases e TensorBoard (verificar versões) | D · inexig. | 0,136 | — | 0,00 | 0,000 | 0,136 | Nenhuma ferramenta nomeada. |
| 35 | Pineau et al., Machine Learning Reproducibility Checklist (verificar) | D | 0,045 | — | 0,00 | 0,000 | 0,045 | Checklist de Pineau ausente. |

Síntese 1.4: A = 0,261 (R1); essenciais exigíveis E = 0,636; R2 = 1,0 × min(1; 0,261/0,636) = **0,41**; R3 = 0,51. Pesos normalizados ×0,9091.

### 1.5 — Aprofundamento do conteúdo (máx. 1,0)

| DS L | Exigência DeepSeek | Prior. | Peso | Evidência na dissertação | Grau | Obtido | Perda | Observação |
|---|---|---|---|---|---|---|---|---|
| 37 | Formalização da reprodutibilidade: mesma tupla (código, dados, ambiente, hiperparâmetros, seed) produz o mesmo artefato | E | 0,15 | L67–81 (§7.3.3) | 1,00 | 0,150 | 0,000 | Fórmula D + C + H + E + S, com a ressalva sobre determinismo. |
| 38 | Linhagem e grafo de dependências entre datasets, runs e modelos; auditoria | E | 0,15 | L43–49 (§7.3.1); L61 (§7.3.2); L111 (§7.4) | 1,00 [0,75–1,00] | 0,150 | 0,000 | Cadeia de linhagem e auditoria. |
| 39 | Trade-offs: tracking detalhado versus overhead; registry centralizado versus autonomia; versionamento de dados versus custo | E | 0,15 | L109–111 (§7.4); L121 (§7.4) | 0,75 | 0,113 | 0,037 | Custo da rastreabilidade e rigor × velocidade; registry central × autonomia ausente. |
| 40 | Casos-limite: dados mutáveis, dependências não fixadas, seeds não controladas, experimentos concorrentes e conflitos de versão | E | 0,15 | L113 (§7.4) | 0,75 | 0,113 | 0,037 | Dados mutáveis, dependências, não determinismo, proliferação e divergência de ambientes listados, sem desenvolvimento. |
| 41 | Comparação justa de experimentos: mesmos splits, mesma métrica, controle de variáveis e significância | E | 0,10 | L63 (§7.3.2); L81 (§7.3.3) | 0,75 | 0,075 | 0,025 | Mesmos conjuntos, métricas e pré-processamento; significância só como "estatisticamente compatíveis". |
| 42 | Relação entre versionamento de dados e vazamento temporal/leakage | D | 0,10 | — | 0,00 | 0,000 | 0,100 | Vazamento temporal ausente. |
| 43 | Estratégias de tuning: espaço de busca, orçamento e early stopping | D | 0,10 | — | 0,00 | 0,000 | 0,100 | Tuning ausente. |
| 44 | Exemplo aplicado: pipeline reprodutível com Git + DVC + MLflow e registro de modelo | D | 0,10 | — | 0,00 | 0,000 | 0,100 | Sem exemplo aplicado com ferramentas. |

Síntese 1.5: A = 0,600 (R1); essenciais exigíveis E = 0,700; R2 = 1,0 × min(1; 0,600/0,700) = **0,86**; R3 = 1,00.

### 1.3 e Item II — sem correspondente DeepSeek

| Critério oficial | Exigência DeepSeek | Evidência | Grau | Impacto |
|---|---|---|---|---|
| 1.3 Organização, coerência, clareza e sequência lógica de ideias | Nenhuma | Seções numeradas 7.1–7.5 com subseções 7.3.x; progressão introdução → fundamentos → núcleo → limitações → conclusão | 95% (hipótese) | 0,475 |
| 2.1 Uso adequado de terminologia técnico-científica | Nenhuma | Terminologia técnica consistente; termos em inglês destacados em itálico | 95% (hipótese) | 0,950 |
| 2.2 Estruturação coerente do texto com introdução, desenvolvimento e conclusão | Nenhuma | Introdução (L3), desenvolvimento e conclusão (L123) explícitos | 95% (hipótese) | 0,475 |
| 2.3 Precisão e objetividade | Nenhuma | Frases curtas, sem digressões; fórmulas e diagramas como síntese | 95% (hipótese) | 0,475 |
| 2.4 Correção ortográfica e gramatical | Nenhuma | Não avaliável integralmente no Markdown (manuscrito); nenhum erro observado no texto-fonte | 95% (hipótese) | 0,475 |

**Total do ponto:** R1 = 6,68 · R2 (central) = **7,50** · R3 = 8,60 · sensibilidade aos graus: 7,45 – 7,67.

## Ponto 8 — MLOps: Automação, Implantação e Infraestrutura de Aprendizado de Máquina

Dissertação: `prova-escrita/8-mlops-automacao-implantacao-e-infraestrutura-de-aprendizado-de-maquina_v2.md` · Barema DeepSeek: `prova-escrita/barema-deepseek/ponto-8.note`

### 1.1 — Domínio técnico/científico/crítico do ponto sorteado (máx. 2,5)

| DS L | Exigência DeepSeek | Prior. | Peso | Evidência na dissertação | Grau | Obtido | Perda | Observação |
|---|---|---|---|---|---|---|---|---|
| 6 | Definição formal de automação de pipeline de ML e distinção entre CI, CD e Continuous Training (CT) | E | 0,25 | L17–31 (§8.2) | 1,00 | 0,250 | 0,000 | Automação e distinção CI/CD/CT, com quality gates. |
| 7 | Distinção entre implantação batch, online (tempo real) e streaming; critérios técnicos de escolha | E | 0,30 | L62–74 (§8.3.2) | 1,00 | 0,300 | 0,000 | Inferência batch, online e streaming, com critérios. |
| 8 | Infraestrutura como código (IaC): declaração, idempotência, versionamento e reprodutibilidade da infraestrutura | E | 0,25 | — | 0,00 | 0,000 | 0,250 | IaC ausente (busca "IaC", "Terraform", "infraestrutura como código": 0). |
| 9 | Conteinerização e isolamento de dependências; imagens reprodutíveis e imutáveis | E | 0,25 | L45 (§8.3.1); L84 (§8.3.3) | 0,75 | 0,188 | 0,062 | Containers: isolamento e portabilidade; imagens imutáveis não explicitadas. |
| 10 | Orquestração de pipelines e agendamento de tarefas; dependências e paralelismo | E | 0,25 | L19 (§8.2) | 0,25 [0,25–0,50] | 0,062 | 0,188 | Pipeline como encadeamento de etapas; a orquestração tratada é a de containers, não a de pipelines. |
| 11 | Serving de modelos: APIs REST/gRPC, inferência em lote versus tempo real e escalabilidade horizontal | E | 0,30 | L62–74 (§8.3.2); L95–97 (§8.3.4) | 0,75 | 0,225 | 0,075 | Batch × online e escala horizontal; REST/gRPC ausentes. |
| 12 | Feature store: definição, consistência treino/serving e camadas online/offline | E | 0,25 | L76–78 (§8.3.2) | 0,25 | 0,062 | 0,188 | Consistência treino/serving motivada pelo skew; feature store ausente (busca: 0). |
| 13 | Análise crítica: custos, complexidade operacional, vendor lock-in, automação prematura e riscos de segurança | E | 0,30 | L119–132 (§8.4) | 0,75 | 0,225 | 0,075 | Custo, complexidade e sofisticação × simplicidade; lock-in e segurança ausentes. |
| 14 | Distinção entre infraestrutura de ML e infraestrutura de software tradicional | E | 0,20 | L7–10 (§8.1); L76 (§8.3.2); L82 (§8.3.3) | 0,50 | 0,100 | 0,100 | Código do modelo como pequena parte do sistema e skew; distinção explícita ML × software tradicional ausente. |
| 15 | Quando não automatizar: fase exploratória, baixa frequência de retreino e custo superior ao benefício | D | 0,15 | L25 (§8.2); L123 (§8.4) | 0,25 [0,25–0,50] | 0,037 | 0,113 | "CT não é retreinamento indiscriminado" e automação × complexidade; não diz quando não automatizar. |

Síntese 1.1: A = 1,450 (R1); essenciais exigíveis E = 2,350; R2 = 2,5 × min(1; 1,450/2,350) = **1,54**; R3 = 1,93.

### 1.2 — Abordagem das ideias fundamentais do conteúdo (máx. 2,5)

| DS L | Exigência DeepSeek | Prior. | Peso | Evidência na dissertação | Grau | Obtido | Perda | Observação |
|---|---|---|---|---|---|---|---|---|
| 17 | CI/CD para ML: testes de código, dados e modelo; pipeline automatizado de build, teste e implantação | E | 0,30 | L19–31 (§8.2) | 0,75 [0,75–1,00] | 0,225 | 0,075 | Testes, validação de dados, quality gates e promoção. |
| 18 | Continuous Training (CT): gatilhos por novos dados, agendamento e drift (fronteira com o Ponto 9) | E | 0,25 | L25 (§8.2) | 0,75 | 0,188 | 0,062 | CT acionado por novos dados ou mudanças relevantes; agendamento não citado. |
| 19 | Padrões de implantação: shadow, canário, blue-green e A/B testing | E | 0,30 | L47–57 (§8.3.1) | 0,75 | 0,225 | 0,075 | Recreate, rolling, blue-green, canary e rollback; shadow e A/B ausentes. |
| 20 | Empacotamento e serving: Docker, Kubernetes, KServe/Seldon e TorchServe/TF Serving | E | 0,30 | L37–45 (§8.3.1); L84–91 (§8.3.3) | 0,50 | 0,150 | 0,150 | Empacotamento, containers e orquestração conceituais; nenhuma ferramenta nomeada. |
| 21 | Orquestração de pipelines: Airflow, Kubeflow Pipelines e MLflow (fronteira com o Ponto 7) | E | 0,25 | L19 (§8.2) | 0,25 | 0,062 | 0,188 | Pipelines descritos; Airflow/Kubeflow ausentes. |
| 22 | Infraestrutura em nuvem e escalabilidade: instâncias, autoscaling, GPUs e balanceamento de carga | E | 0,25 | L82 (§8.3.3); L95–115 (§8.3.4) | 1,00 | 0,250 | 0,000 | Recursos, escala, balanceamento e autoscaling. |
| 23 | Feature store: Feast/Tecton e padrões de acesso online/offline | E | 0,20 | — | 0,00 | 0,000 | 0,200 | Feature store ausente. |
| 24 | Batch scoring e pipelines agendados para inferência em lote | E | 0,20 | L64 (§8.3.2) | 0,75 | 0,150 | 0,050 | Inferência batch periódica. |
| 25 | API de inferência e contrato de entrada/saída; versionamento de endpoints | E | 0,15 | L43 (§8.3.1); L78 (§8.3.2) | 0,75 | 0,113 | 0,037 | Contratos de entrada e saída; versionamento de endpoints ausente. |
| 26 | IaC com Terraform e gestão declarativa de recursos | E | 0,15 | — | 0,00 | 0,000 | 0,150 | Terraform ausente. |
| 27 | Edge deployment e otimização de modelos (quantização, pruning) | D | 0,15 | — | 0,00 | 0,000 | 0,150 | Edge/quantização ausentes. |

Síntese 1.2: A = 1,363 (R1); essenciais exigíveis E = 2,350; R2 = 2,5 × min(1; 1,363/2,350) = **1,45**; R3 = 1,81.

### 1.4 — Atualização do conteúdo / referências bibliográficas / normas técnicas (máx. 1,0)

| DS L | Exigência DeepSeek | Prior. | Peso | Evidência na dissertação | Grau | Obtido | Perda | Observação |
|---|---|---|---|---|---|---|---|---|
| 29 | Huyen, Designing Machine Learning Systems (2022) | E | 0,15 | — | 0,00 | 0,000 | 0,150 | Huyen não citada. |
| 30 | Treveil et al., Introducing MLOps (2020) | E | 0,10 | L47 (§8.3.1); L167 (Ref.) | 1,00 | 0,100 | 0,000 | Treveil et al. [4]. |
| 31 | Kreuzberger, Kühl & Hirschl (2023), Machine Learning Operations (MLOps): Overview, Definition, and Architecture (verificar) | E | 0,10 | L19 (§8.2); L165 (Ref.) | 1,00 | 0,100 | 0,000 | Kreuzberger et al. [2]. |
| 32 | Humble & Farley, Continuous Delivery (2010) | E | 0,10 | L23–24 (§8.2) | 0,25 | 0,025 | 0,075 | CI/CD descritos sem citar Humble & Farley. |
| 33 | Breck et al. (2017), The ML Test Score | E | 0,10 | L27 (§8.2); L166 (Ref.) | 1,00 | 0,100 | 0,000 | Breck et al. [3]. |
| 34 | Documentação atual de Kubernetes, Docker e Terraform (verificar versões) | E · inexig. | 0,15 | — | 0,00 | 0,000 | 0,150 | Docker/Kubernetes/Terraform não nomeados. |
| 35 | Documentação atual de Kubeflow, Feast, KServe/Seldon e TorchServe/TF Serving (verificar versões) | E · inexig. | 0,15 | — | 0,00 | 0,000 | 0,150 | Kubeflow/Feast/KServe não nomeados. |
| 36 | MLPerf Inference benchmark (verificar versão) | E · inexig. | 0,10 | — | 0,00 | 0,000 | 0,100 | MLPerf ausente. |
| 37 | Sato, Wider & Windheuser (2019), Continuous Delivery for Machine Learning (verificar) | D | 0,05 | — | 0,00 | 0,000 | 0,050 | Sato et al. ausente. |

Síntese 1.4: A = 0,325 (R1); essenciais exigíveis E = 0,550; R2 = 1,0 × min(1; 0,325/0,550) = **0,59**; R3 = 0,74.

### 1.5 — Aprofundamento do conteúdo (máx. 1,0)

| DS L | Exigência DeepSeek | Prior. | Peso | Evidência na dissertação | Grau | Obtido | Perda | Observação |
|---|---|---|---|---|---|---|---|---|
| 39 | Formalização de SLO/SLA de inferência: latência p95/p99, throughput e disponibilidade | E | 0,15 | L72–74 (§8.3.2) | 0,25 | 0,037 | 0,113 | Latência e throughput definidos; SLO/percentis ausentes. |
| 40 | Trade-offs entre padrões de implantação: canário, blue-green e shadow; risco, custo e complexidade | E | 0,15 | L54 (§8.3.1) | 0,50 | 0,075 | 0,075 | Estratégias "equilibram risco, disponibilidade e custo", sem comparação entre elas. |
| 41 | Autoscaling e custo: cold start, scale-to-zero, utilização de GPU e elasticidade | E | 0,15 | L107 (§8.3.4); L126–128 (§8.4) | 0,50 | 0,075 | 0,075 | Under/overprovisioning e capacidade ≈ demanda; cold start e scale-to-zero ausentes. |
| 42 | Casos-limite: skew treino/serving, falha de feature store e indisponibilidade de endpoint | E | 0,15 | L76 (§8.3.2); L113–115 (§8.3.4); L132 (§8.4) | 0,75 | 0,113 | 0,037 | Skew, ponto único de falha e degradação graciosa; falha de feature store ausente. |
| 43 | Trade-off entre serving online e batch: latência, custo e atualidade das previsões | E | 0,10 | L64–72 (§8.3.2) | 0,75 | 0,075 | 0,025 | Latência e volume; atualidade das previsões não tratada. |
| 44 | Segurança e isolamento multi-tenant; supply chain de imagens e assinatura de artefatos | D | 0,10 | — | 0,00 | 0,000 | 0,100 | Segurança/supply chain ausente. |
| 45 | Relação entre IaC e reprodutibilidade; detecção de drift de infraestrutura | D | 0,10 | — | 0,00 | 0,000 | 0,100 | IaC ausente. |
| 46 | Exemplo aplicado: pipeline CI/CD/CT com implantação canário e rollback automatizado | D | 0,10 | — | 0,00 | 0,000 | 0,100 | Sem exemplo aplicado. |

Síntese 1.5: A = 0,375 (R1); essenciais exigíveis E = 0,700; R2 = 1,0 × min(1; 0,375/0,700) = **0,54**; R3 = 0,67.

### 1.3 e Item II — sem correspondente DeepSeek

| Critério oficial | Exigência DeepSeek | Evidência | Grau | Impacto |
|---|---|---|---|---|
| 1.3 Organização, coerência, clareza e sequência lógica de ideias | Nenhuma | Seções numeradas 8.1–8.5 com subseções 8.3.x; progressão introdução → fundamentos → núcleo → limitações → conclusão | 95% (hipótese) | 0,475 |
| 2.1 Uso adequado de terminologia técnico-científica | Nenhuma | Terminologia técnica consistente; termos em inglês destacados em itálico | 95% (hipótese) | 0,950 |
| 2.2 Estruturação coerente do texto com introdução, desenvolvimento e conclusão | Nenhuma | Introdução (L3), desenvolvimento e conclusão (L134) explícitos | 95% (hipótese) | 0,475 |
| 2.3 Precisão e objetividade | Nenhuma | Frases curtas, sem digressões; fórmulas e diagramas como síntese | 95% (hipótese) | 0,475 |
| 2.4 Correção ortográfica e gramatical | Nenhuma | Não avaliável integralmente no Markdown (manuscrito); nenhum erro observado no texto-fonte | 95% (hipótese) | 0,475 |

**Total do ponto:** R1 = 6,36 · R2 (central) = **6,97** · R3 = 8,00 · sensibilidade aos graus: 6,97 – 7,15.

## Ponto 9 — MLOps: Monitoramento, Governança e Manutenção de Modelos

Dissertação: `prova-escrita/9-mlops-monitoramento-governanca-e-manutencao-de-modelos_v2.md` · Barema DeepSeek: `prova-escrita/barema-deepseek/ponto-9.note`

### 1.1 — Domínio técnico/científico/crítico do ponto sorteado (máx. 2,5)

| DS L | Exigência DeepSeek | Prior. | Peso | Evidência na dissertação | Grau | Obtido | Perda | Observação |
|---|---|---|---|---|---|---|---|---|
| 6 | Definição formal de monitoramento de modelos e distinção de observabilidade (métricas, logs e traces) | E | 0,25 | L25–31 (§9.2) | 1,00 | 0,250 | 0,000 | Monitoramento e observabilidade (métricas, logs e traces). |
| 7 | Distinção entre monitoramento de sistema, de modelo e de negócio | E | 0,30 | L19–27 (§9.2) | 0,75 | 0,225 | 0,075 | Sistema × modelo; monitoramento de negócio ausente. |
| 8 | Data drift, concept drift, label drift e covariate shift: definições e critérios de detecção | E | 0,35 | L37–64 (§9.3.1) | 0,75 [0,75–1,00] | 0,263 | 0,087 | Data drift, covariate shift e concept drift formalizados; label drift ausente. |
| 9 | Métricas de desempenho em produção e problema do atraso de rótulos (label delay) | E | 0,30 | L68–70 (§9.3.2) | 1,00 | 0,300 | 0,000 | Métricas em produção e feedback delay. |
| 10 | Governança de ML: definição, papéis, accountability, políticas e gestão de risco | E | 0,30 | L78–88 (§9.3.3) | 1,00 [0,75–1,00] | 0,300 | 0,000 | Responsabilidade, rastreabilidade, controle e proporcionalidade ao risco. |
| 11 | Manutenção de modelos: tipos (corretiva, adaptativa e perfectiva) e gatilhos de retreino | E | 0,25 | L92–106 (§9.3.4) | 0,75 | 0,188 | 0,062 | Intervenções e gatilhos de retreino; tipologia corretiva/adaptativa/perfectiva ausente. |
| 12 | Análise crítica: falsos alarmes, drift sem degradação, métricas agregadas enganosas e feedback loops | E | 0,30 | L60–62 (§9.3.1); L68 (§9.3.2); L72–74 (§9.3.2); L119 (§9.4) | 0,75 | 0,225 | 0,075 | Falsos alarmes, drift sem degradação e métricas agregadas; feedback loops ausentes. |
| 13 | Distinção entre monitoramento offline e online e avaliação contínua em produção | E | 0,20 | L27 (§9.2); L68 (§9.3.2) | 0,50 | 0,100 | 0,100 | Avaliação contínua contra a baseline; offline × online não explicitado. |
| 14 | Quando não retreinar automaticamente: riscos de feedback loops, degradação silenciosa e instabilidade | D | 0,15 | L92–98 (§9.3.4); L121–124 (§9.4) | 1,00 | 0,150 | 0,000 | Retreino automático arriscado e orientado por diagnóstico. |
| 15 | Segurança e privacidade no monitoramento: PII em logs, anonimização e retenção | D | 0,10 | — | 0,00 | 0,000 | 0,100 | Privacidade/PII ausentes. |

Síntese 1.1: A = 2,000 (R1); essenciais exigíveis E = 2,250; R2 = 2,5 × min(1; 2,000/2,250) = **2,22**; R3 = 2,50.

### 1.2 — Abordagem das ideias fundamentais do conteúdo (máx. 2,5)

| DS L | Exigência DeepSeek | Prior. | Peso | Evidência na dissertação | Grau | Obtido | Perda | Observação |
|---|---|---|---|---|---|---|---|---|
| 17 | Métricas operacionais: latência, throughput, taxa de erros, disponibilidade e uso de recursos | E | 0,20 | L25 (§9.2) | 1,00 | 0,200 | 0,000 | Latência, throughput, disponibilidade, erros e recursos. |
| 18 | Monitoramento de dados: schema, estatísticas, valores ausentes, ranges e freshness | E | 0,25 | L37 (§9.3.1) | 0,75 [0,75–1,00] | 0,188 | 0,062 | Esquema, ausentes, fora de faixa e falhas de pipeline; freshness ausente. |
| 19 | Detecção de drift: PSI, KS, Jensen-Shannon e testes estatísticos | E | 0,30 | L64 (§9.3.1) | 0,50 | 0,150 | 0,150 | "Testes ou medidas de distância" genéricos; PSI/KS/JS ausentes. |
| 20 | Monitoramento de performance: métricas de modelo, janelas, segmentação e label delay | E | 0,30 | L68–74 (§9.3.2) | 1,00 | 0,300 | 0,000 | Métricas ao longo do tempo, segmentação e atraso de rótulos. |
| 21 | Alertas: SLI/SLO, limiares, severidade, on-call e runbooks | E | 0,20 | L31 (§9.2); L72 (§9.3.2) | 0,75 [0,50–0,75] | 0,150 | 0,050 | SLI/SLO e thresholds; severidade, on-call e runbooks ausentes. |
| 22 | Logging e auditoria: predições, entradas, versões, lineage e retenção | E | 0,25 | L70 (§9.3.2); L82–84 (§9.3.3) | 0,75 | 0,188 | 0,062 | Versões, lineage e trilha de auditoria; retenção ausente. |
| 23 | Governança: políticas, catálogo, model registry, aprovação, auditoria e conformidade | E | 0,30 | L82–86 (§9.3.3) | 0,75 | 0,225 | 0,075 | Aprovação, auditoria e validação; catálogo/registry e conformidade não nomeados. |
| 24 | Gestão de risco de modelo: inventário, classificação, revisão periódica e validação independente | E | 0,25 | L82 (§9.3.3); L86 (§9.3.3) | 0,75 [0,75–1,00] | 0,188 | 0,062 | Inventário por modelo, risco e validação independente; revisão periódica ausente. |
| 25 | Manutenção: retreino agendado/por gatilho, rollback, aposentadoria e versionamento | E | 0,25 | L100–106 (§9.3.4) | 1,00 | 0,250 | 0,000 | Retreino periódico × por eventos, rollback e aposentadoria. |
| 26 | Feedback loop e coleta de rótulos em produção | E | 0,20 | L70 (§9.3.2) | 0,25 | 0,050 | 0,150 | Só feedback delay; coleta de rótulos e feedback loops ausentes. |

Síntese 1.2: A = 1,887 (R1); essenciais exigíveis E = 2,500; R2 = 2,5 × min(1; 1,887/2,500) = **1,89**; R3 = 2,36.

### 1.4 — Atualização do conteúdo / referências bibliográficas / normas técnicas (máx. 1,0)

| DS L | Exigência DeepSeek | Prior. | Peso | Evidência na dissertação | Grau | Obtido | Perda | Observação |
|---|---|---|---|---|---|---|---|---|
| 28 | Sculley et al. (2015), Hidden Technical Debt in Machine Learning Systems | E | 0,10 | L7 (§9.1); L159 (Ref.) | 1,00 | 0,100 | 0,000 | Sculley et al. [1]. |
| 29 | Breck et al. (2017), The ML Test Score | E | 0,10 | L68 (§9.3.2); L161 (Ref.) | 1,00 | 0,100 | 0,000 | Breck et al. [3]. |
| 30 | Huyen, Designing Machine Learning Systems (2022) | E | 0,15 | — | 0,00 | 0,000 | 0,150 | Huyen não citada. |
| 31 | Gama et al. (2014), A Survey on Concept Drift Adaptation | E | 0,15 | L47 (§9.3.1); L160 (Ref.) | 1,00 | 0,150 | 0,000 | Gama et al. [2]. |
| 32 | Lu et al. (2018), Learning under Concept Drift: A Review (verificar) | D | 0,10 | — | 0,00 | 0,000 | 0,100 | Lu et al. ausente. |
| 33 | NIST AI Risk Management Framework (AI RMF 1.0, 2023) | E | 0,10 | — | 0,00 | 0,000 | 0,100 | NIST AI RMF ausente. |
| 34 | ISO/IEC 42001:2023 — AI management system | E | 0,10 | — | 0,00 | 0,000 | 0,100 | ISO/IEC 42001 ausente. |
| 35 | LGPD (Lei 13.709/2018) e GDPR (Regulamento UE 2016/679) | E | 0,10 | — | 0,00 | 0,000 | 0,100 | LGPD/GDPR ausentes. |
| 36 | Documentação atual de Evidently AI, WhyLabs, Prometheus/Grafana e MLflow (verificar versões) | E · inexig. | 0,10 | — | 0,00 | 0,000 | 0,100 | Ferramentas não nomeadas. |

Síntese 1.4: A = 0,350 (R1); essenciais exigíveis E = 0,800; R2 = 1,0 × min(1; 0,350/0,800) = **0,44**; R3 = 0,55.

### 1.5 — Aprofundamento do conteúdo (máx. 1,0)

| DS L | Exigência DeepSeek | Prior. | Peso | Evidência na dissertação | Grau | Obtido | Perda | Observação |
|---|---|---|---|---|---|---|---|---|
| 38 | Formalização de drift: mudança em P(X) versus mudança em P(y/X), com testes estatísticos e poder | E | 0,15 | L41–51 (§9.3.1); L64 (§9.3.1) | 0,75 [0,75–1,00] | 0,113 | 0,037 | P(X) × P(Y|X) formalizados e significância × relevância; poder estatístico ausente. |
| 39 | Label delay e avaliação retardada: estratégias de estimação e viés associado | E | 0,10 | L70 (§9.3.2); L110 (§9.4) | 0,75 | 0,075 | 0,025 | Sinais indiretos durante o atraso; viés de estimação não discutido. |
| 40 | Trade-offs de alertas: sensibilidade versus especificidade e custo de falsos positivos/negativos | E | 0,10 | L72 (§9.3.2); L114 (§9.4) | 1,00 | 0,100 | 0,000 | Sensibilidade × estabilidade e falsos alarmes. |
| 41 | Casos-limite: drift sem degradação, degradação sem drift, feedback loops e sazonalidade | E | 0,15 | L60–62 (§9.3.1) | 0,75 [0,50–0,75] | 0,113 | 0,037 | Drift sem degradação e degradação sem drift aparente; feedback loops e sazonalidade ausentes. |
| 42 | Governança: auditoria e rastreabilidade fim a fim; retenção e privacidade de dados | E | 0,10 | L84 (§9.3.3) | 0,50 | 0,050 | 0,050 | Auditoria e lineage; retenção e privacidade ausentes. |
| 43 | Manutenção: retreino automático versus manual; validação pós-retreino e rollback | E | 0,10 | L102–104 (§9.3.4); L121–124 (§9.4) | 1,00 | 0,100 | 0,000 | Automático × governado, validação pós-retreino e champion–challenger. |
| 44 | Relação entre monitoramento e versionamento/linhagem (fronteira com o Ponto 7) | D | 0,10 | L82–84 (§9.3.3) | 0,75 | 0,075 | 0,025 | Monitoramento ligado a versões e lineage. |
| 45 | Exemplo aplicado: monitoramento de modelo de crédito com PSI, performance e alertas segmentados | D | 0,10 | L98 (§9.3.4) | 0,25 | 0,025 | 0,075 | Mini-exemplos diagnósticos (coluna corrompida, unidade); sem caso aplicado completo. |
| 46 | Riscos adversariais e envenenamento de dados em produção (data poisoning) | D | 0,10 | — | 0,00 | 0,000 | 0,100 | Riscos adversariais ausentes. |

Síntese 1.5: A = 0,650 (R1); essenciais exigíveis E = 0,700; R2 = 1,0 × min(1; 0,650/0,700) = **0,93**; R3 = 1,00.

### 1.3 e Item II — sem correspondente DeepSeek

| Critério oficial | Exigência DeepSeek | Evidência | Grau | Impacto |
|---|---|---|---|---|
| 1.3 Organização, coerência, clareza e sequência lógica de ideias | Nenhuma | Seções numeradas 9.1–9.5 com subseções 9.3.x; progressão introdução → fundamentos → núcleo → limitações → conclusão | 95% (hipótese) | 0,475 |
| 2.1 Uso adequado de terminologia técnico-científica | Nenhuma | Terminologia técnica consistente; termos em inglês destacados em itálico | 95% (hipótese) | 0,950 |
| 2.2 Estruturação coerente do texto com introdução, desenvolvimento e conclusão | Nenhuma | Introdução (L3), desenvolvimento e conclusão (L127) explícitos | 95% (hipótese) | 0,475 |
| 2.3 Precisão e objetividade | Nenhuma | Frases curtas, sem digressões; fórmulas e diagramas como síntese | 95% (hipótese) | 0,475 |
| 2.4 Correção ortográfica e gramatical | Nenhuma | Não avaliável integralmente no Markdown (manuscrito); nenhum erro observado no texto-fonte | 95% (hipótese) | 0,475 |

**Total do ponto:** R1 = 7,74 · R2 (central) = **8,33** · R3 = 9,26 · sensibilidade aos graus: 8,14 – 8,60.

## Ponto 10 — XAI: Métodos, Interpretabilidade, Avaliação e Uso das Explicações

Dissertação: `prova-escrita/10-xai-metodos-interpretabilidade-avaliacao-e-uso-das-explicacoes_v2.md` · Barema DeepSeek: `prova-escrita/barema-deepseek/ponto-10.note`

### 1.1 — Domínio técnico/científico/crítico do ponto sorteado (máx. 2,5)

| DS L | Exigência DeepSeek | Prior. | Peso | Evidência na dissertação | Grau | Obtido | Perda | Observação |
|---|---|---|---|---|---|---|---|---|
| 6 | Definição formal de interpretabilidade, explicabilidade e transparência; distinção entre modelo interpretável e explicação post-hoc | E | 0,25 | L5–15 (§10.1) | 0,75 | 0,188 | 0,062 | XAI definida e intrínseca × post hoc; interpretabilidade, explicabilidade e transparência não distinguidas formalmente. |
| 7 | Distinção entre explicações globais e locais; model-specific × model-agnostic; ante-hoc × post-hoc | E | 0,30 | L12–15 (§10.1); L28–30 (§10.2) | 1,00 | 0,300 | 0,000 | Local × global, specific × agnostic, intrínseco × post hoc. |
| 8 | Definição de fidelidade (faithfulness), estabilidade, robustez e compreensibilidade como critérios de qualidade | E | 0,30 | L87–97 (§10.3.3) | 1,00 | 0,300 | 0,000 | Fidelidade, estabilidade, robustez e compreensibilidade. |
| 9 | Pressupostos e limites: explicações como aproximações, multiplicidade de explicações (Rashomon) e risco de explicações enganosas | E | 0,30 | L123–127 (§10.4) | 0,75 [0,75–1,00] | 0,225 | 0,075 | Aproximação, instabilidade, discordância E₁ ≠ E₂ e racionalização; efeito Rashomon (múltiplos modelos) não nomeado. |
| 10 | Análise crítica do trade-off entre desempenho preditivo e interpretabilidade; crítica à suposição de sacrifício inevitável de acurácia | E | 0,25 | L131 (§10.4) | 0,75 [0,75–1,00] | 0,188 | 0,062 | "Modelos complexos não são sempre mais precisos" — a crítica aparece em uma frase. |
| 11 | Adequação da explicação ao público-alvo: desenvolvedores, usuários finais, auditores e reguladores | E | 0,25 | L22 (§10.1); L103–111 (§10.3.4) | 1,00 | 0,250 | 0,000 | Desenvolvedores, especialistas, usuários e auditoria; adequação ao usuário. |
| 12 | Quando não usar XAI: explicação não acionável, risco de confiança excessiva e casos de modelos intrinsecamente interpretáveis | E | 0,20 | L107 (§10.3.4); L131 (§10.4) | 0,75 [0,75–1,00] | 0,150 | 0,050 | Confiança calibrada e preferência por modelo interpretável; explicação não acionável pouco tratada. |
| 13 | Distinção entre explicabilidade e causalidade; explicações preditivas não estabelecem relações causais | D | 0,20 | L34–35 (§10.2); L109 (§10.3.4); L117–121 (§10.4) | 1,00 | 0,200 | 0,000 | Importância ≠ efeito causal; explicar modelo ≠ fenômeno. |
| 14 | Limitações de explicabilidade em modelos de alta dimensionalidade e dados não estruturados (texto, imagem, áudio) | D | 0,20 | — | 0,00 | 0,000 | 0,200 | Dados não estruturados ausentes (busca "texto", "imagem": 0). |
| 15 | Crítica à XAI como substituto de governança, validação humana e controle institucional (fronteira com o Ponto 9) | D | 0,25 | L105 (§10.3.4); L129 (§10.4) | 0,50 | 0,125 | 0,125 | "XAI não corrige um modelo" e revisão por especialistas; relação com governança não explicitada. |

Síntese 1.1: A = 1,925 (R1); essenciais exigíveis E = 1,850; R2 = 2,5 × min(1; 1,925/1,850) = **2,50**; R3 = 2,50.

### 1.2 — Abordagem das ideias fundamentais do conteúdo (máx. 2,5)

| DS L | Exigência DeepSeek | Prior. | Peso | Evidência na dissertação | Grau | Obtido | Perda | Observação |
|---|---|---|---|---|---|---|---|---|
| 17 | Modelos intrinsecamente interpretáveis: regressão linear/logística, árvores de decisão, rule lists e GAMs | E | 0,30 | L15 (§10.1) | 0,75 | 0,225 | 0,075 | Regressões, árvores pequenas e regras; GAMs ausentes; tratamento breve. |
| 18 | Importância de features: permutation importance, PDP/ICE e suas limitações | E | 0,30 | L54–60 (§10.3.1) | 0,75 | 0,225 | 0,075 | Permutation importance com a limitação da correlação; PDP/ICE ausentes. |
| 19 | LIME: perturbações locais, modelo substituto e escopo de aplicação | E | 0,30 | L68 (§10.3.2) | 1,00 | 0,300 | 0,000 | LIME: perturbações, surrogate local e limite de fidelidade. |
| 20 | SHAP: valores de Shapley, propriedades (eficiência, simetria, dummy, aditividade) e TreeSHAP/KernelSHAP | E | 0,35 | L44–52 (§10.3.1) | 0,50 | 0,175 | 0,175 | Forma aditiva e referência; valores de Shapley, propriedades e variantes ausentes. |
| 21 | Gradientes de saliência e Integrated Gradients para entradas contínuas e imagens | E | 0,25 | L62 (§10.3.1) | 1,00 | 0,250 | 0,000 | Gradientes e Integrated Gradients. |
| 22 | Explicações contrafactuais e âncoras (anchors): definição, geração e uso | E | 0,25 | L72–78 (§10.3.2) | 0,75 | 0,188 | 0,062 | Contrafactual formalizado e com requisitos; anchors ausentes. |
| 23 | Explicações baseadas em exemplos/protótipos e k-NN explicável | D | 0,20 | L70 (§10.3.2) | 0,50 | 0,100 | 0,100 | Protótipos e exemplos influentes em uma frase. |
| 24 | Surrogate models globais (árvore substituta) e regras de decisão | D | 0,20 | L66 (§10.3.2); L81 (§10.3.2) | 0,75 | 0,150 | 0,050 | Surrogate g ≈ f. |
| 25 | Visualizações de explicabilidade: heatmaps, SHAP force plots, PDP/ICE | D | 0,15 | — | 0,00 | 0,000 | 0,150 | Visualizações ausentes. |
| 26 | Explicações baseadas em atenção em modelos de linguagem/visão e suas limitações | D | 0,20 | — | 0,00 | 0,000 | 0,200 | Atenção ausente. |

Síntese 1.2: A = 1,613 (R1); essenciais exigíveis E = 1,750; R2 = 2,5 × min(1; 1,613/1,750) = **2,30**; R3 = 2,50.

### 1.4 — Atualização do conteúdo / referências bibliográficas / normas técnicas (máx. 1,0)

| DS L | Exigência DeepSeek | Prior. | Peso | Evidência na dissertação | Grau | Obtido | Perda | Observação |
|---|---|---|---|---|---|---|---|---|
| 28 | Ribeiro, Singh & Guestrin (2016), "Why Should I Trust You?": Explaining the Predictions of Any Classifier (LIME) | E | 0,10 | L68 (§10.3.2); L160 (Ref.) | 1,00 | 0,100 | 0,000 | Ribeiro et al. [4]. |
| 29 | Lundberg & Lee (2017), A Unified Approach to Interpreting Model Predictions (SHAP) | E | 0,10 | L44 (§10.3.1); L158 (Ref.) | 1,00 | 0,100 | 0,000 | Lundberg & Lee [2]. |
| 30 | Sundararajan, Taly & Yan (2017), Axiomatic Attribution for Deep Networks (Integrated Gradients) | E | 0,10 | L62 (§10.3.1); L159 (Ref.) | 1,00 | 0,100 | 0,000 | Sundararajan et al. [3]. |
| 31 | Wachter, Mittelstadt & Russell (2017), Counterfactual Explanations Without Opening the Black Box | E | 0,10 | L74–76 (§10.3.2) | 0,25 | 0,025 | 0,075 | Formulação de Wachter presente sem citação. |
| 32 | Molnar, Interpretable Machine Learning (2ª ed., 2022) (verificar) | E | 0,10 | L15 (§10.1); L157 (Ref.) | 1,00 | 0,100 | 0,000 | Molnar [1]. |
| 33 | Doshi-Velez & Kim (2017), Towards A Rigorous Science of Interpretable Machine Learning | E | 0,10 | L99 (§10.3.3) | 0,25 | 0,025 | 0,075 | Taxonomia funcional/humana/aplicação (Doshi-Velez & Kim) atribuída a Molnar. |
| 34 | Rudin (2019), Stop Explaining Black Box Machine Learning Models for High Stakes Decisions and Use Interpretable Models Instead | E | 0,10 | L131 (§10.4) | 0,25 | 0,025 | 0,075 | A crítica de Rudin aparece sem citação. |
| 35 | Miller (2019), Explanation in Artificial Intelligence: Insights from the Social Sciences | D | 0,10 | — | 0,00 | 0,000 | 0,100 | Miller ausente. |
| 36 | Documentação atual de SHAP, LIME, InterpretML, Captum e Alibi (verificar versões) | D · inexig. | 0,10 | L44 (§10.3.1); L68 (§10.3.2) | 0,25 | 0,025 | 0,075 | SHAP e LIME nomeados (também bibliotecas); documentação não citada. |
| 37 | LGPD (Lei 13.709/2018) e GDPR: direito à explicação (fronteira com o Ponto 9) | D | 0,10 | — | 0,00 | 0,000 | 0,100 | LGPD/GDPR ausentes. |

Síntese 1.4: A = 0,500 (R1); essenciais exigíveis E = 0,700; R2 = 1,0 × min(1; 0,500/0,700) = **0,71**; R3 = 0,89.

### 1.5 — Aprofundamento do conteúdo (máx. 1,0)

| DS L | Exigência DeepSeek | Prior. | Peso | Evidência na dissertação | Grau | Obtido | Perda | Observação |
|---|---|---|---|---|---|---|---|---|
| 39 | Formalização dos valores de Shapley e das propriedades de eficiência, simetria, dummy e aditividade | E | 0,15 | L47 (§10.3.1) | 0,25 | 0,037 | 0,113 | Só a decomposição aditiva (eficiência); fórmula de Shapley e axiomas ausentes. |
| 40 | Formalização de fidelidade: correlação entre importância atribuída e mudança na predição; métricas de deletion/insertion | E | 0,15 | L93 (§10.3.3); L99 (§10.3.3) | 0,50 | 0,075 | 0,075 | Fidelidade definida e testada por intervenções; métricas deletion/insertion ausentes. |
| 41 | Trade-offs: fidelidade × compreensibilidade, estabilidade × sensibilidade e custo computacional de SHAP/LIME | E | 0,15 | L95–97 (§10.3.3) | 0,75 | 0,113 | 0,037 | Fidelidade × simplicidade e estabilidade; custo computacional ausente. |
| 42 | Casos-limite: explicadores instáveis, dependência entre features, colinearidade distorcendo SHAP/permutation importance | E | 0,15 | L52 (§10.3.1); L60 (§10.3.1); L123 (§10.4) | 1,00 | 0,150 | 0,000 | Referência, correlação entre features e instabilidade. |
| 43 | Avaliação de explicações: métricas funcionais (fidelidade, estabilidade) e estudos humanos (compreensibilidade, confiança) | E | 0,15 | L99 (§10.3.3) | 1,00 | 0,150 | 0,000 | Avaliação funcional, humana e por aplicação. |
| 44 | Relação entre explicabilidade e causalidade; explicações preditivas × causais | D | 0,10 | L34 (§10.2); L109 (§10.3.4); L117–121 (§10.4) | 1,00 | 0,100 | 0,000 | Explicação preditiva × causal. |
| 45 | Exemplo aplicado: explicação local com SHAP/LIME para decisão de crédito e análise de contrafactual | D | 0,10 | — | 0,00 | 0,000 | 0,100 | Sem exemplo aplicado. |
| 46 | Limitações em modelos de linguagem e imagens: risco de explicações plausíveis, porém infiéis | D | 0,05 | — | 0,00 | 0,000 | 0,050 | Limitações em linguagem/imagem ausentes. |

Síntese 1.5: A = 0,625 (R1); essenciais exigíveis E = 0,750; R2 = 1,0 × min(1; 0,625/0,750) = **0,83**; R3 = 1,00.

### 1.3 e Item II — sem correspondente DeepSeek

| Critério oficial | Exigência DeepSeek | Evidência | Grau | Impacto |
|---|---|---|---|---|
| 1.3 Organização, coerência, clareza e sequência lógica de ideias | Nenhuma | Seções numeradas 10.1–10.5 com subseções 10.3.x; progressão introdução → fundamentos → núcleo → limitações → conclusão | 95% (hipótese) | 0,475 |
| 2.1 Uso adequado de terminologia técnico-científica | Nenhuma | Terminologia técnica consistente; termos em inglês destacados em itálico | 95% (hipótese) | 0,950 |
| 2.2 Estruturação coerente do texto com introdução, desenvolvimento e conclusão | Nenhuma | Introdução (L3), desenvolvimento e conclusão (L133) explícitos | 95% (hipótese) | 0,475 |
| 2.3 Precisão e objetividade | Nenhuma | Frases curtas, sem digressões; fórmulas e diagramas como síntese | 95% (hipótese) | 0,475 |
| 2.4 Correção ortográfica e gramatical | Nenhuma | Não avaliável integralmente no Markdown (manuscrito); nenhum erro observado no texto-fonte | 95% (hipótese) | 0,475 |

**Total do ponto:** R1 = 7,51 · R2 (central) = **9,20** · R3 = 9,74 · sensibilidade aos graus: 9,20 – 9,20.

