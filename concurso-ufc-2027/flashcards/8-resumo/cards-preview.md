# UFC — Prova Escrita — Flashcards de Alto Nível

Prévia gerada a partir de `cards.json`, que é a única fonte; não editar à mão.

10 pontos · 40 cards · os 4 cards de cada ponto ficam sempre nesta ordem.

---

## Ponto 1 — Armazenamento e Gerenciamento Distribuído de Dados

### Ponto 1 — Card 1 de 4

**Frente:** 1.1 Introdução e Delimitação do Problema · 1.2 Fundamentos e Relevância

1. `1.1` **Vertical** (3 limites) → **Horizontal**
2. `1.1` rede + **falhas parciais** → 4 propriedades em risco
3. `1.2` **visão lógica única**, sem ganho automático
4. `1.2` **particionamento** + **replicação**
5. `1.2` **GFS** → falhas são normais

### Ponto 1 — Card 2 de 4

**Frente:** 1.3.1 Particionamento e Distribuição · 1.3.2 Replicação e Tolerância a Falhas

1. `1.3.1` **Range** (localidade) ↔ **Hash** (equilíbrio)
2. `1.3.1` dados equilibrados ≠ **carga** equilibrada
3. `1.3.1` rebalanceamento → **consistent hashing** (anel)
4. `1.3.2` **síncrona** ↔ **assíncrona**: garantia × latência
5. `1.3.2` **failover** sem consenso → **split-brain**
6. `1.3.2` **domínios de falha** + detecção → disponibilidade

### Ponto 1 — Card 3 de 4

**Frente:** 1.3.3 Consistência, Disponibilidade e Quóruns · 1.3.4 Modelos e Arquiteturas

1. `1.3.3` **linearizável** ↔ **eventual**
2. `1.3.3` partição → **CAP** · sem partição → **PACELC**
3. `1.3.3` **R + W > N** → leitura e escrita se sobrepõem
4. `1.3.3` várias partições → **2PC** → bloqueio
5. `1.3.4` mesmos mecanismos → GFS · **Bigtable** · **Dynamo** · objetos
6. `1.3.4` **shared-nothing** · separar computação/armazenamento

### Ponto 1 — Card 4 de 4

**Frente:** 1.4 Limitações, Trade-offs e Desafios Atuais · 1.5 Conclusão

1. `1.4` sem arquitetura **universal** → 4 compromissos
2. `1.4` **códigos de apagamento** → custo de reconstrução
3. `1.4` **workload** decide: banco ↔ catálogo
4. `1.5` particionar + replicar → custo de **coordenar**
5. `1.5` **consistência** sob medida

---

## Ponto 2 — Processamento Paralelo e Distribuído

### Ponto 2 — Card 1 de 4

**Frente:** 2.1 Introdução e Delimitação do Problema · 2.2 Fundamentos e Relevância

1. `2.1` **dividir o trabalho**: intra-nó ↔ entre nós
2. `2.1` decompor → distribuir → coordenar → recuperar
3. `2.1` trabalho útil > **custo da distribuição**
4. `2.2` paralelismo de **dados** ↔ de **tarefas**
5. `2.2` **Amdahl**: S(p) ≤ 1/s (10% serial → máx. 10×)
6. `2.2` problema cresce → **strong** ↔ **weak** scaling

### Ponto 2 — Card 2 de 4

**Frente:** 2.3.1 Decomposição, Granularidade e Balanceamento · 2.3.2 Comunicação, Sincronização e Localidade

1. `2.3.1` **granularidade**: tarefas grandes ↔ pequenas
2. `2.3.1` trabalho ≠ dados: **skew** → **stragglers**
3. `2.3.1` escalonamento dinâmico + **execução especulativa**
4. `2.3.2` T = comp + **comm** + **sync** + overhead
5. `2.3.2` **localidade** ↔ balanceamento
6. `2.3.2` **shuffle** = o mais caro → agregação local

### Ponto 2 — Card 3 de 4

**Frente:** 2.3.3 MapReduce e Modelos de Execução Distribuída · 2.3.4 DAGs, Reutilização e Recuperação

1. `2.3.3` **map** → shuffle → **reduce** (contar palavras)
2. `2.3.3` runtime embute **tolerância a falhas**
3. `2.3.3` grava em **disco** → batch robusto, iterativo lento
4. `2.3.4` **Spark**: memória + avaliação preguiçosa → DAG
5. `2.3.4` dependência estreita ↔ **larga** → estágios
6. `2.3.4` **linhagem**: recomputar × replicar × checkpoint

### Ponto 2 — Card 4 de 4

**Frente:** 2.4 Limitações, Trade-offs e Desafios Atuais · 2.5 Conclusão

1. `2.4` distribuir ≠ escala **linear**
2. `2.4` a **cauda** importa, não só a média
3. `2.4` abstração mantém **custo físico** (agrupar por chave)
4. `2.5` escalar ≠ **somar nós**
5. `2.5` MapReduce e Spark não eliminam **custos**

---

## Ponto 3 — Fluxos e Arquiteturas de Dados

### Ponto 3 — Card 1 de 4

**Frente:** 3.1 Introdução e Delimitação do Problema · 3.2 Fundamentos e Relevância

1. `3.1` **fluxo** ↔ **batch**
2. `3.1` atraso · desordem · estado · falhas → **correção**
3. `3.1` **4 eixos**: tempo · estado · garantias · armazenamento
4. `3.2` **bounded** ↔ **unbounded**
5. `3.2` **latência** · **throughput**
6. `3.2` particionar: + throughput, − **ordem global**

### Ponto 3 — Card 2 de 4

**Frente:** 3.3.1 Tempo, Janelas e Watermarks · 3.3.2 Estado, Recuperação e Semântica de Processamento

1. `3.3.1` **event time** ≠ processing time
2. `3.3.1` **janelas** (3 tipos) · modelo **Dataflow**
3. `3.3.1` **watermark** = estimativa → latência × completude × estado
4. `3.3.2` **stateful**: (sₜ₊₁, yₜ) = f(sₜ, xₜ)
5. `3.3.2` falha → **checkpoint** + replay (Flink)
6. `3.3.2` **exactly-once** = efeito no estado ≠ entrega

### Ponto 3 — Card 3 de 4

**Frente:** 3.3.3 Logs Distribuídos e Arquiteturas Orientadas a Eventos · 3.3.4 Integração Batch/Streaming e Arquiteturas de Dados

1. `3.3.3` **Kafka**: log desacopla produtor ↔ consumidor
2. `3.3.3` **offset** → replay · ordem por partição
3. `3.3.3` **log** ≠ **motor** de processamento
4. `3.3.4` **Lambda**: 2 camadas → duplicação
5. `3.3.4` ↔ **Kappa**: recomputa por replay
6. `3.3.4` data lake → **lakehouse**

### Ponto 3 — Card 4 de 4

**Frente:** 3.4 Limitações, Trade-offs e Desafios Atuais · 3.5 Conclusão

1. `3.4` garantias fortes custam → **menor complexidade**
2. `3.4` λ produção > λ consumo → **backlog** → backpressure
3. `3.4` desacoplar ≠ dispensar **contratos de dados**
4. `3.5` dados em **movimento** + dados **persistidos**
5. `3.5` **garantias** exigidas decidem, não a novidade

---

## Ponto 4 — Mineração de Dados

### Ponto 4 — Card 1 de 4

**Frente:** 4.1 Introdução e Delimitação do Problema · 4.2 Fundamentos e Relevância

1. `4.1` mineração = etapa do **KDD**
2. `4.1` padrão: **4 qualidades** → decisão
3. `4.2` seleção → … → conhecimento (**iterativo**)
4. `4.2` dado → padrão → **conhecimento**
5. `4.2` detectável pode ser trivial · **espúrio** · irrelevante

### Ponto 4 — Card 2 de 4

**Frente:** 4.3.1 Preparação dos Dados e Análise Exploratória · 4.3.2 Identificação e Mineração de Padrões

1. `4.3.1` preparação **não é neutra**
2. `4.3.1` **EDA** (Tukey): boxplot · **IQR**
3. `4.3.1` **Pearson** ↔ **Spearman**
4. `4.3.1` achados = **hipóteses**
5. `4.3.2` pão → manteiga: sup · conf · **lift > 1**
6. `4.3.2` padrão **global** ↔ **local**
7. `4.3.2` frequente ≠ **relevante**

### Ponto 4 — Card 3 de 4

**Frente:** 4.3.3 Identificação de Anomalias

1. `4.3.3` desvio do esperado ≠ **erro**
2. `4.3.3` **3 tipos** (madrugada)
3. `4.3.3` normalidade: z · IQR · **LOF** · **Isolation Forest**
4. `4.3.3` alta dimensão → perde **poder discriminativo**

### Ponto 4 — Card 4 de 4

**Frente:** 4.4 Limitações, Trade-offs e Desafios Atuais · 4.5 Conclusão

1. `4.4` aparente ≠ válido: **múltiplas comparações**
2. `4.4` **associação** ≠ causalidade
3. `4.4` conhecimento de **domínio** (2 sentidos)
4. `4.5` padrão **robusto** ≠ artefato → conhecimento

---

## Ponto 5 — Aprendizado Supervisionado e Não Supervisionado

### Ponto 5 — Card 1 de 4

**Frente:** 5.1 Introdução e Delimitação do Problema · 5.2 Fundamentos e Relevância

1. `5.1` **variável-alvo** disponível?
2. `5.1` sim: (xᵢ, yᵢ) → **f: X → Y**
3. `5.1` não: só xᵢ → **estrutura**
4. `5.2` **risco empírico** ≠ erro em dados novos
5. `5.2` underfitting (**viés**) ↔ overfitting (**variância**)
6. `5.2` **regularização**: erro + λ · complexidade (L1 ↔ L2)

### Ponto 5 — Card 2 de 4

**Frente:** 5.3.1 Aprendizado Supervisionado · 5.3.2 Aprendizado Não Supervisionado

1. `5.3.1` método = **hipótese** sobre os dados
2. `5.3.1` linear · árvore · **ensemble** · SVM · rede
3. `5.3.1` **bagging** − variância ↔ **boosting** − viés
4. `5.3.2` **k-means**: 2 passos · 3 limitações · k-means++
5. `5.3.2` dendrograma · **DBSCAN** (ruído) · PCA

### Ponto 5 — Card 3 de 4

**Frente:** 5.3.3 Avaliação e Seleção de Modelos

1. `5.3.3` **acurácia** engana se desbalanceado (fraude)
2. `5.3.3` sem rótulo → **silhueta**
3. `5.3.3` **k-fold**
4. `5.3.3` teste **intocado** até o fim

### Ponto 5 — Card 4 de 4

**Frente:** 5.4 Limitações, Trade-offs e Desafios Atuais · 5.5 Conclusão

1. `5.4` **leakage** · fora da distribuição → teste engana
2. `5.4` **aprendizado profundo**: + capacidade, + preço
3. `5.4` nenhum algoritmo **universal**
4. `5.5` adequação: problema · dados · modelo · **métrica**

---

## Ponto 6 — Aprendizado por Reforço

### Ponto 6 — Card 1 de 4

**Frente:** 6.1 Introdução e Delimitação do Problema · 6.2 Fundamentos e Relevância

1. `6.1` agente: estado → **ação** → recompensa
2. `6.1` ninguém informa a ação **correta**
3. `6.1` **política** → máx. retorno de longo prazo
4. `6.2` **MDP** (S, A, P, R, γ) · Markov
5. `6.2` **retorno**: Gₜ = Σ γᵏ Rₜ₊ₖ₊₁
6. `6.2` ruim agora, ótima no total → **atribuição de crédito**

### Ponto 6 — Card 2 de 4

**Frente:** 6.3.1 Política e Funções de Valor · 6.3.2 Equações de Bellman e Aprendizado Temporal

1. `6.3.1` política **π(a|s)**
2. `6.3.1` **Vπ(s)**: estado ↔ **Qπ(s,a)**: estado + ação
3. `6.3.1` conhecer **Q** → melhorar π → repetir
4. `6.3.2` **Bellman**: V(s) = E[R + γ V(s′)]
5. `6.3.2` programação dinâmica (modelo) ↔ **model-free**
6. `6.3.2` **MC** ↔ **TD** (bootstrapping): viés × variância

### Ponto 6 — Card 3 de 4

**Frente:** 6.3.3 Exploração × Explotação · 6.3.4 Principais Famílias de Métodos

1. `6.3.3` **explorar** ↔ **explotar**
2. `6.3.3` **ε-greedy** → risco: explorar demais ↔ de menos
3. `6.3.4` **valor**: Q-learning (max → off-policy) ↔ SARSA
4. `6.3.4` **política** + valor → **ator–crítico**
5. `6.3.4` RL profundo → **deadly triad** → DQN (2 mecanismos)

### Ponto 6 — Card 4 de 4

**Frente:** 6.4 Limitações, Trade-offs e Desafios Atuais · 6.5 Conclusão

1. `6.4` recompensa **esparsa** · experiência cara
2. `6.4` recompensa ≠ objetivo → **reward hacking**
3. `6.4` exploração livre arrisca → **safe RL**
4. `6.5` decisão **sequencial**: agora + futuro
5. `6.5` prática: **4 exigências**

---

## Ponto 7 — MLOps: Desenvolvimento, Versionamento e Experimentação

### Ponto 7 — Card 1 de 4

**Frente:** 7.1 Introdução e Delimitação do Problema · 7.2 Fundamentos e Relevância

1. `7.1` ciclo **iterativo** e experimental
2. `7.1` modelo ≠ só **código** (Sculley)
3. `7.1` escopo: até o **candidato validado**
4. `7.2` execução = **unidade experimental** (4 componentes)
5. `7.2` entradas → procedimento → saídas
6. `7.2` acurácia subiu ≠ **evidência**

### Ponto 7 — Card 2 de 4

**Frente:** 7.3.1 Versionamento, Artefatos e Linhagem · 7.3.2 Experiment Tracking e Rastreabilidade

1. `7.3.1` versionar só código **não basta** → artefatos
2. `7.3.1` proveniência ↔ **linhagem**: dados brutos → métricas
3. `7.3.1` versões **imutáveis**: Git · DVC · MLflow
4. `7.3.2` tracking + versão + linhagem → **rastreabilidade**
5. `7.3.2` comparar: mesmo **protocolo** + **baseline**

### Ponto 7 — Card 3 de 4

**Frente:** 7.3.3 Reprodutibilidade · 7.3.4 Validação, Comparação e Seleção

1. `7.3.3` resultado = f(**D, C, H, E, S**)
2. `7.3.3` mesmo **script** ≠ mesmo experimento
3. `7.3.3` reprodutível ≠ idêntico **bit a bit**
4. `7.3.4` validar **dados** ↔ validar **modelo**
5. `7.3.4` busca de hiperparâmetros → superajuste à **validação**
6. `7.3.4` teste **uma vez** → candidato → registro

### Ponto 7 — Card 4 de 4

**Frente:** 7.4 Limitações, Trade-offs e Desafios Atuais · 7.5 Conclusão

1. `7.4` guardar o **suficiente**, não tudo
2. `7.4` automatizar processo ruim ≠ criar **bom**
3. `7.4` **rigor** × velocidade
4. `7.5` **3 elementos** atravessam o fluxo
5. `7.5` valor = condições + validação + **reconstrução**

---

## Ponto 8 — MLOps: Automação, Implantação e Infraestrutura

### Ponto 8 — Card 1 de 4

**Frente:** 8.1 Introdução e Delimitação do Problema · 8.2 Fundamentos e Relevância

1. `8.1` modelo validado ≠ **sistema confiável**
2. `8.1` código = pequena parte (**Sculley**)
3. `8.1` escopo: **entrega** + operação
4. `8.2` manual → **pipeline** como DAG (Airflow, Kubeflow)
5. `8.2` CI · CD · **CT** ≠ retreinar sempre
6. `8.2` **quality gates** → regra de promoção

### Ponto 8 — Card 2 de 4

**Frente:** 8.3.1 Empacotamento e Implantação · 8.3.2 Serving e Padrões de Inferência

1. `8.3.1` implantar ≠ copiar **pesos**
2. `8.3.1` pré/pós + **contrato** E/S → container (Docker)
3. `8.3.1` 4 estratégias de liberação + **rollback**
4. `8.3.2` **batch**: escore noturno
5. `8.3.2` ↔ **online**: latência · throughput
6. `8.3.2` training-serving **skew** → **feature store**

### Ponto 8 — Card 3 de 4

**Frente:** 8.3.3 Infraestrutura, Containers e Orquestração · 8.3.4 Escalabilidade e Disponibilidade

1. `8.3.3` manual → **IaC** (Terraform): recriar + registrar
2. `8.3.3` container tem limite → **Kubernetes** orquestra
3. `8.3.4` vertical ↔ **horizontal** + balanceador + autoscaling
4. `8.3.4` escalável ≠ **disponível**: ponto único de falha

### Ponto 8 — Card 4 de 4

**Frente:** 8.4 Limitações, Trade-offs e Desafios Atuais · 8.5 Conclusão

1. `8.4` **under** ↔ **over**provisioning
2. `8.4` **sofisticado** ≠ melhor (serviço interno)
3. `8.4` resiliência + **degradação graciosa**
4. `8.5` atender **requisitos** com controle, não complexidade

---

## Ponto 9 — MLOps: Monitoramento, Governança e Manutenção

### Ponto 9 — Card 1 de 4

**Frente:** 9.1 Introdução e Delimitação do Problema · 9.2 Fundamentos e Relevância

1. `9.1` implantado ≠ **válido para sempre**
2. `9.1` detectar → diagnosticar → **controlar**
3. `9.2` saúde: **operacional** ↔ **ML**
4. `9.2` **observabilidade**: 3 sinais → SLI/SLO → alertas

### Ponto 9 — Card 2 de 4

**Frente:** 9.3.1 Qualidade de Dados, Data Drift e Concept Drift · 9.3.2 Monitoramento Preditivo e Detecção de Degradação

1. `9.3.1` **data drift** → P(X) mudou?
2. `9.3.1` **concept drift** → P(Y|X) mudou?
3. `9.3.1` drift ≠ **degradação** comprovada
4. `9.3.1` KS · χ² · **PSI** → significância não basta
5. `9.3.2` feedback **atrasa** (empréstimo) → sinais indiretos
6. `9.3.2` Mₜ < τ → alerta: **sensibilidade** × estabilidade
7. `9.3.2` degradação ≠ **causa** → 3 passos

### Ponto 9 — Card 3 de 4

**Frente:** 9.3.3 Governança, Auditoria e Lineage · 9.3.4 Manutenção, Retreinamento e Ciclo de Vida

1. `9.3.3` 3 componentes · **lineage** + **auditoria**
2. `9.3.3` proporcional ao **risco**: crédito ↔ filmes
3. `9.3.3` **ISO/IEC 42001** · LGPD
4. `9.3.4` drift ≠ **retreinar** (pode incorporar o erro)
5. `9.3.4` periódico ↔ **por eventos**
6. `9.3.4` **champion–challenger** antes de promover

### Ponto 9 — Card 4 de 4

**Frente:** 9.4 Limitações, Trade-offs e Desafios Atuais · 9.5 Conclusão

1. `9.4` **excesso** de alertas
2. `9.4` retreino automático **mal governado**
3. `9.5` manter = demonstrar **controle**, não só executar

---

## Ponto 10 — XAI: Métodos, Interpretabilidade, Avaliação e Uso

### Ponto 10 — Card 1 de 4

**Frente:** 10.1 Introdução e Delimitação do Problema · 10.2 Fundamentos e Relevância

1. `10.1` **evidência** ≠ narrativa convincente
2. `10.1` **intrínseca** ↔ **post hoc**
3. `10.1` método → avaliação → **uso**
4. `10.2` **local** ↔ **global**
5. `10.2` **model-specific** ↔ **model-agnostic**
6. `10.2` importância ≠ **efeito causal**

### Ponto 10 — Card 2 de 4

**Frente:** 10.3.1 Atribuição de Atributos · 10.3.2 Surrogates, Exemplos e Contrafactuais

1. `10.3.1` **SHAP**: f(x) = φ₀ + Σ φⱼ · custo exponencial
2. `10.3.1` **permutação**: Iⱼ = M orig − M perm(j) · correlação
3. `10.3.1` redes → gradiente (**Integrated Gradients**)
4. `10.3.2` **LIME**: g(x) ≈ f(x) local, ≠ global
5. `10.3.2` **contrafactual**: menor mudança → y desejado (idade)

### Ponto 10 — Card 3 de 4

**Frente:** 10.3.3 Avaliação das Explicações · 10.3.4 Uso das Explicações

1. `10.3.3` plausível ≠ **fiel** (+ estável, compreensível)
2. `10.3.3` fidelidade × **simplicidade**
3. `10.3.3` **3 formas** de avaliação
4. `10.3.4` desenvolvimento: revela o que a **métrica** esconde
5. `10.3.4` decisão: mais confiança ≠ confiança **calibrada**
6. `10.3.4` **auditoria** · investigação de erros

### Ponto 10 — Card 4 de 4

**Frente:** 10.4 Limitações, Trade-offs e Desafios Atuais · 10.5 Conclusão

1. `10.4` explicar **modelo** ≠ fenômeno → revela **atalhos**
2. `10.4` post hoc frágil · métodos **discordam**
3. `10.4` não corrige → preferir **interpretável**
4. `10.5` XAI > gerar explicações: **4 ações**
5. `10.5` boa explicação: **3 qualidades**
