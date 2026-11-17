### Ponto 1 — Armazenamento e Gerenciamento Distribuído

| Conceito | Prioridade | Ponto principal | Também aparece em | Observação curta |
|---|:---:|---|---|---|
| Armazenamento distribuído | B | 1 | — | — |
| Escalabilidade vertical × horizontal | B | 1 | 8 | — |
| Particionamento / sharding | A | 1 | 2, 3 | — |
| Particionamento por intervalo × por hash | B | 1 | — | — |
| Skew / hotspot | C | 1 | 2 | — |
| Replicação | A | 1 | 2, 8 | — |
| Replicação síncrona × assíncrona | B | 1 | — | — |
| Linearizabilidade | A | 1 | — | — |
| Consistência eventual | A | 1 | — | — |
| Teorema CAP | A | 1 | — | — |
| Quórum de leitura/escrita | A | 1 | — | — |
| Consenso | B | 1 | — | — |
| Separação entre computação e armazenamento | B | 1 | — | — |

Nota:

- Você não separou assim, mas acho importante.
- Eu trocaria `Particionamento / sharding` por 2 conceitos: `Particionamento (Vertical/Horizontal)` e `Sharding`, com definições aproximadas (você melhora):
	- Particionamento (Vertical/Horizontal): Geralmente ocorre dentro de um único servidor ou instância de banco de dados. Uma tabela gigante é dividida em sub-tabelas menores (por exemplo, separando vendas por ano), mas todas permanecem armazenadas na mesma máquina.
	- Sharding (Particionamento Horizontal entre múltiplas máquinas): Os dados são divididos e distribuídos entre servidores (nós) totalmente diferentes. Cada máquina (chamada de shard) armazena uma fração única e exclusiva dos dados.
- Com isso, definir corretamente `Escalabilidade vertical × horizontal`

### Ponto 2 — Processamento Paralelo e Distribuído

| Conceito | Prioridade | Ponto principal | Também aparece em | Observação curta |
|---|:---:|---|---|---|
| Paralelismo de dados × de tarefas | A | 2 | — | — |
| Speedup e eficiência paralela | B | 2 | — | — |
| Lei de Amdahl | A | 2 | — | — |
| Strong scaling × weak scaling | B | 2 | — | — |
| Granularidade de tarefas | B | 2 | — | — |
| Localidade dos dados | B | 2 | 1 | — |
| Shuffle | A | 2 | 3 | — |
| MapReduce | A | 2 | — | — |
| DAG de execução | B | 2 | — | — |
| Lineage computacional | C | 2 | — | Manter separado de lineage de dados/modelos dos Pontos 7 e 9. |
| Recomputação × replicação × checkpointing | B | 2 | 1, 3 | — |

### Ponto 3 — Processamento de Fluxos e Arquiteturas de Dados

| Conceito | Prioridade | Ponto principal | Também aparece em | Observação curta |
|---|:---:|---|---|---|
| Batch × streaming | A | 3 | 8 | — |
| Dados bounded × unbounded | B | 3 | — | — |
| Latência × throughput | A | 3 | 1, 2, 8, 9 | — |
| Event time × processing time | A | 3 | — | — |
| Janelas de processamento | B | 3 | — | — |
| Watermark | A | 3 | — | — |
| Processamento stateful | A | 3 | — | — |
| Replay | A | 3 | — | — |
| At-most-once × at-least-once × exactly-once | A | 3 | — | — |
| Idempotência / deduplicação | B | 3 | — | — |
| Lambda Architecture × Kappa Architecture | B | 3 | — | — |
| Data lake × lakehouse | C | 3 | — | — |
| Backpressure | B | 3 | — | — |

### Ponto 4 — Mineração de Dados

| Conceito | Prioridade | Ponto principal | Também aparece em | Observação curta |
|---|:---:|---|---|---|
| KDD | A | 4 | — | — |
| Dado × padrão × conhecimento | B | 4 | — | — |
| Análise Exploratória de Dados (EDA) | A | 4 | — | — |
| Suporte, confiança e lift | A | 4 | — | — |
| Padrão global × local | C | 4 | — | — |
| Anomalia global × contextual × coletiva | A | 4 | — | — |
| Detecção de anomalias | B | 4 | — | — |
| Associação ≠ causalidade | A | 4 | — | Há princípio análogo em XAI, mas em contexto diferente. |

### Ponto 5 — Aprendizado Supervisionado e Não Supervisionado

| Conceito | Prioridade | Ponto principal | Também aparece em | Observação curta |
|---|:---:|---|---|---|
| Aprendizado supervisionado × não supervisionado | A | 5 | 4, 6 | — |
| Função de perda | B | 5 | — | — |
| Treino × validação × teste | B | 5 | — | — |
| Parâmetro × hiperparâmetro | B | 5 | 6, 7 | — |
| Generalização | B | 5 | — | — |
| Underfitting × overfitting | A | 5 | — | — |
| Viés × variância | A | 5 | — | — |
| Classificação × regressão | B | 5 | — | — |
| Clustering | C | 5 | 4 | — |
| Validação cruzada | B | 5 | — | — |
| Data leakage | A | 5 | 10 | — |

### Ponto 6 — Aprendizado por Reforço

| Conceito | Prioridade | Ponto principal | Também aparece em | Observação curta |
|---|:---:|---|---|---|
| Aprendizado por reforço (RL) | A | 6 | — | — |
| Processo de Decisão de Markov (MDP) | A | 6 | — | — |
| Retorno e fator de desconto | B | 6 | — | — |
| Política | B | 6 | — | — |
| Funções \(V^\pi\) e \(Q^\pi\) | A | 6 | — | — |
| Equações de Bellman | A | 6 | — | — |
| Temporal Difference / bootstrapping | B | 6 | — | — |
| Exploração × explotação | A | 6 | — | — |
| Q-learning × SARSA | A | 6 | — | — |
| On-policy × off-policy | B | 6 | — | — |
| Métodos baseados em valor × em política | B | 6 | — | — |
| Actor–Critic | A | 6 | — | — |
| Model-free × model-based | C | 6 | — | — |
| Reward hacking / specification gaming | B | 6 | — | — |

### Ponto 7 — MLOps: Desenvolvimento, Versionamento e Experimentação

| Conceito | Prioridade | Ponto principal | Também aparece em | Observação curta |
|---|:---:|---|---|---|
| Artefato | B | 7 | 8, 9 | — |
| Versionamento de ML | B | 7 | 8, 9 | — |
| Proveniência | B | 7 | 9 | — |
| Lineage de dados/modelos | A | 7 | 9 | Não confundir com lineage computacional do Ponto 2. |
| Experiment tracking | A | 7 | — | — |
| Rastreabilidade experimental | B | 7 | 9 | — |
| Baseline | B | 7 | 9 | — |
| Reprodutibilidade | A | 7 | 4 | — |
| Validação de dados × validação de modelo | B | 7 | 8, 9 | — |
| Critérios de aceitação / quality gates | B | 7 | 8, 9 | — |

### Ponto 8 — MLOps: Automação, Implantação e Infraestrutura

| Conceito | Prioridade | Ponto principal | Também aparece em | Observação curta |
|---|:---:|---|---|---|
| CI × CD × CT | A | 8 | — | — |
| Pipeline de ML | B | 8 | 7, 9 | — |
| Empacotamento de modelo | B | 8 | — | — |
| Container | A | 8 | — | — |
| Rollback | B | 8 | 9 | — |
| Model serving | B | 8 | — | — |
| Inferência batch × online × streaming | A | 8 | 3 | — |
| Training-serving skew | A | 8 | 9 | — |
| Orquestração | B | 8 | — | — |
| Autoscaling | B | 8 | — | — |
| Underprovisioning × overprovisioning | C | 8 | — | — |
| Alta disponibilidade × escalabilidade | B | 8 | 1 | — |

### Ponto 9 — MLOps: Monitoramento, Governança e Manutenção

| Conceito | Prioridade | Ponto principal | Também aparece em | Observação curta |
|---|:---:|---|---|---|
| Monitoramento operacional × monitoramento de ML | A | 9 | — | — |
| Observabilidade | B | 9 | 3 | — |
| SLI × SLO | C | 9 | — | — |
| Qualidade de dados | B | 9 | 4, 7 | — |
| Data drift | A | 9 | — | — |
| Covariate shift | B | 9 | — | — |
| Concept drift | A | 9 | — | — |
| Drift × degradação | B | 9 | — | — |
| Feedback delay | C | 9 | — | — |
| Governança de modelos | B | 9 | 8 | — |
| Trilha de auditoria | B | 9 | 7 | — |
| Retreinamento periódico × orientado por eventos | A | 9 | 8 | — |
| Ciclo de vida do modelo | B | 9 | 7, 8 | — |

### Ponto 10 — XAI

| Conceito | Prioridade | Ponto principal | Também aparece em | Observação curta |
|---|:---:|---|---|---|
| XAI | A | 10 | — | — |
| Interpretabilidade intrínseca × explicação post hoc | A | 10 | — | — |
| Explicação local × global | B | 10 | — | — |
| Model-specific × model-agnostic | B | 10 | — | — |
| Feature attribution | B | 10 | — | — |
| SHAP | B | 10 | — | — |
| Surrogate model / LIME | B | 10 | — | — |
| Explicação contrafactual | A | 10 | — | — |
| Fidelidade da explicação | A | 10 | — | — |
| Estabilidade × robustez da explicação | C | 10 | — | — |
| Plausibilidade × fidelidade | A | 10 | — | — |
| Explicação ≠ causalidade | B | 10 | — | Mantive separado de “associação ≠ causalidade” do Ponto 4. |
