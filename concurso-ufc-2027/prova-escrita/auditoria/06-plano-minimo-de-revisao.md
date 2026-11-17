# Auditoria 2 — Plano mínimo de revisão

Checklist final. Contém só o indispensável: o que mudar, onde e o que cortar. A justificativa de cada item está em [04-auditoria-custo-beneficio.md](04-auditoria-custo-beneficio.md) e a ordem global em [05-prioridades-globais.md](05-prioridades-globais.md).

> As dissertações **não foram alteradas** por esta auditoria. Os trechos "atuais" abaixo foram conferidos por script e existem exatamente uma vez em cada arquivo.

## 0. Antes de tudo: medir a velocidade (15 min)

- [ ] **Teste.** Escolha a seção X.3.1 de qualquer ponto (≈ 200–250 palavras). Com caneta e cronômetro, escreva-a de memória por **15 minutos**, no ritmo da prova. Conte as palavras escritas e divida por 15.
- [ ] **Regra de decisão:**

| Velocidade medida | O que aplicar |
|---|---|
| ≥ 16 pal/min | Toda a lista FAZER (seção 2). Cortes só onde marcados como obrigatórios. Pode avançar para "se houver tempo" (relatório 05). |
| 13–15 pal/min | Toda a lista FAZER + cortes **C1** em todos os pontos (seção 3). |
| ≤ 12 pal/min | Só os itens marcados **[ESSENCIAL]** e **[custo ~0]**, usando as versões mínimas + cortes **C1, C2 e C3** em todos os pontos. Nenhuma outra inserção sem corte equivalente. |

Tempo de escrita resultante (minutos; orçamento ≈ 70 por ponto):

| Ponto | Atual (12 / 15 / 18) | Plano FAZER (15) | Plano FAZER + C1 (13–15) | Cenário lento mínimo (12) |
|---|---|---|---|---|
| 1 | 69,7 / 55,9 / 46,6 | 64,2 | 63,2 | 71,8 |
| 2 | 75,6 / 60,6 / 50,6 | 63,2 | 61,2 | 69,1 |
| 3 | 75,0 / 60,1 / 50,1 | 61,3 | 59,8 | 68,8 |
| 4 | 77,2 / 62,0 / 51,7 | 66,2 | 65,1 | 75,2 |
| 5 | 79,0 / 63,4 / 52,9 | 65,6 | 65,6 | 70,1 |
| 6 | 87,3 / 69,9 / 58,0 | 67,7 | 67,7 | 72,8 |
| 7 | 74,5 / 59,9 / 50,1 | 63,6 | 60,3 | 66,9 |
| 8 | 73,4 / 59,0 / 49,4 | 64,3 | 61,0 | 68,6 |
| 9 | 80,6 / 64,7 / 54,0 | 67,3 | 67,3 | 72,3 |
| 10 | 80,1 / 64,2 / 53,5 | 67,4 | 67,4 | 73,0 |

No cenário lento mínimo, os Pontos 1, 4, 5, 6, 9 e 10 ainda ficam até 5,2 min acima de 70. Compense reduzindo a revisão a 3 min nesses pontos e, no Ponto 4, usando a versão mínima de P4-A.

## 1. Ordem recomendada de execução

| Dia | Itens |
|---|---|
| 04/11 (qua) | Teste de velocidade · P6-A (enxugar P6) · P3-A · P9-B · P4-B · P8-C · P8-A · P1-A |
| 05/11 (qui) | P4-A · P5-C · P5-B · P5-A + cortes C1 do P5 · P6-B · P6-C |
| 06/11 (sex) | P8-B · P1-B · P7-B · P3-C · P9-A + cortes C1 do P9 · P7-A · P2-A · P10-A + corte C1 do P10 |
| 07/11 (sáb) | ABNT de custo zero e microajustes · um ensaio cronometrado de **um** ponto alterado (80 min) · nada novo depois disso |

Se o tempo de estudo acabar antes, pare onde estiver: cada item é independente.

## 2. Alterações (por ponto)

Legenda: [ESSENCIAL], [ALTO] = alto custo-benefício, [custo ~0] = troca de até 16 palavras. O número entre parênteses é a prioridade global (relatório 05).

### Ponto 1 — Processamento de Dados em Larga Escala: Armazenamento e Gerenciamento Distribuído de Dados

- [ ] **P1-A (9) [ESSENCIAL] — Transações distribuídas (ACID, 2PC, BASE)** · +76 palavras · moderada +5,7 min
  - **Onde:** Novo parágrafo ao final de 1.3.3, depois da L62 (após "...dependam do protocolo completo."). No diagrama da conclusão (L98), trocar "CONSISTÊNCIA / QUÓRUNS" por "CONSISTÊNCIA / QUÓRUNS / TRANSAÇÕES".
  - **Inserir:** “Quando uma transação altera várias partições, preservar as garantias **ACID** — em especial a atomicidade — exige coordenação. No *two-phase commit* (**2PC**), um coordenador só efetiva a transação se todos os participantes votarem pela confirmação; caso contrário, ela é abortada. O 2PC acrescenta rodadas de rede e pode bloquear participantes se o coordenador falhar; por isso, muitos sistemas restringem transações a uma partição ou aceitam garantias mais fracas (**BASE**), enquanto sistemas NewSQL combinam 2PC e consenso [7].”
  - *Versão mínima:* “Transações que alteram várias partições exigem coordenação para preservar a atomicidade: no *two-phase commit* (2PC), o coordenador só efetiva a transação se todos os participantes votarem pela confirmação. O 2PC acrescenta latência e bloqueia participantes se o coordenador falhar; por isso, muitos sistemas restringem transações a uma partição ou aceitam garantias mais fracas (BASE) [7].”
  - **Referências:** [7] KLEPPMANN, M.; RICCOMINI, C. Designing data-intensive applications. 2. ed. O'Reilly, 2026. (Alternativa de encaixe exato: ÖZSU, M. T.; VALDURIEZ, P. Principles of distributed database systems. 4. ed. Springer, 2020.)
- [ ] **P1-B (15) [ALTO] — PACELC como complemento do CAP** · +32 palavras · moderada +2,7 min
  - **Onde:** Depois da L54 (após "...e posterior reconciliação."), como frase final do parágrafo.
  - **Inserir:** “O **PACELC** [6] completa essa leitura: havendo partição (P), escolhe-se entre disponibilidade e consistência (A/C); senão (E), entre latência e consistência (L/C), pois coordenar réplicas tem custo mesmo sem falhas.”
  - **Referências:** [6] ABADI, D. Consistency tradeoffs in modern distributed database system design. Computer, 2012. (Renumerar: Abadi passa a [6] por aparecer antes do parágrafo de transações, que cita [7].)

### Ponto 2 — Processamento de Dados em Larga Escala: Processamento Paralelo e Distribuído em Larga Escala

- [ ] **P2-A (20) [ALTO] — RDD, avaliação preguiçosa e dependências estreitas × largas** · +38 palavras · moderada +2,5 min
  - **Onde:** (a) L81: substituir a frase inteira. (b) L79: substituir o trecho "formar estágios separados por *shuffles*".
  - **Trocar:** “O Spark combina DAGs, reutilização de dados em memória e **lineage** [4]: em vez de replicar todos os resultados intermediários, uma partição perdida pode ser recomputada a partir de suas dependências.”
  - **Por:** “O Spark [4] representa os dados como **RDDs**, coleções imutáveis e particionadas cujas transformações são avaliadas de forma preguiçosa até que uma ação exija resultado; isso permite planejar o DAG inteiro, reutilizar dados em memória e explorar **lineage**: em vez de replicar todos os resultados intermediários, uma partição perdida pode ser recomputada a partir de suas dependências.”
  - **E trocar:** “formar estágios separados por *shuffles*” **por** “formar estágios que encadeiam operações com dependências estreitas e terminam nas dependências largas, isto é, nos *shuffles*,”

### Ponto 3 — Processamento de Dados em Larga Escala: Processamento de Fluxos e Arquiteturas de Dados

- [ ] **P3-A (4) [custo ~0] — Correção: o Dataflow não se resume a "três perguntas"** · −3 palavras · moderada −0,2 min
  - **Onde:** L37: substituir o início da frase; os três marcadores seguintes ficam como estão.
  - **Trocar:** “O modelo Dataflow [1] organiza o problema em três perguntas:”
  - **Por:** “O modelo Dataflow [1] articula três mecanismos:”
- [ ] **P3-C (17) [custo ~0] — Nomear engines, ligar [2] ao Flink, citar a Kappa e incluir ACID no lakehouse** · +12 palavras · moderada +1,3 min
  - **Microinserções:** (a) L55: "...e **replay** [2]:" → "...e **replay**, como no Apache Flink [2]:". (b) L67: "não substitui a engine de processamento," → "não substitui a engine de processamento (ex.: Flink, Spark Structured Streaming),". (c) L73: "A **Kappa Architecture** elimina" → "A **Kappa Architecture** [5] elimina". (d) L75: "acrescentam a essa flexibilidade gerenciamento de esquema" → "acrescentam a essa flexibilidade transações ACID, gerenciamento de esquema".
  - **Referências:** [5] KREPS, J. Questioning the Lambda Architecture. O'Reilly Radar, 2014.

### Ponto 4 — Mineração de Dados: Descoberta de Conhecimento, Análise Exploratória de Dados, Identificação de Padrões e Anomalias

- [ ] **P4-A (10) [ESSENCIAL] — Conteúdo operacional mínimo da EDA** · +52 palavras · moderada +3,5 min
  - **Onde:** Novo parágrafo depois da L49 (antes de "Pode ser univariada...").
  - **Inserir:** “Na prática, combinam-se medidas de posição e dispersão — média e desvio padrão, sensíveis a valores extremos; mediana e quartis, mais robustos, que compõem o resumo de cinco números e o *boxplot* de Tukey — com histogramas e diagramas de dispersão; os coeficientes de Pearson (relação linear) e de Spearman (relação monotônica) quantificam associações.”
  - *Versão mínima:* “Na prática, usam-se média, mediana, desvio padrão e quartis (base do *boxplot* de Tukey), histogramas e diagramas de dispersão, além dos coeficientes de Pearson (linear) e Spearman (monotônico).”
- [ ] **P4-B (6) [custo ~0] — Nomear um método por família de detecção de anomalias** · +11 palavras · moderada +0,7 min
  - **Onde:** Substituir a frase da L97.
  - **Trocar:** “A detecção pode basear-se em distribuição estatística, distância, densidade, vizinhança ou isolamento.”
  - **Por:** “A detecção pode basear-se em distribuição estatística (escore z, regra do IQR), distância (k vizinhos mais próximos), densidade (LOF) ou isolamento (*Isolation Forest*).”

### Ponto 5 — Aprendizado Supervisionado e Não Supervisionado

- [ ] **P5-A (22) [ALTO] — Risco empírico explícito e regularização L1/L2** · +29 palavras · moderada +1,8 min
  - **Onde:** (a) L22–26; (b) L42–48.
  - **(a) Trocar** "minimizando uma função de perda:" + a fórmula \(\theta^{*} = \arg\min_{\theta}L(\theta)\) **por** "pela **minimização do risco empírico**, isto é, da perda média \(\ell\) na amostra:" + \(\theta^{*} = \arg\min_{\theta}\frac{1}{n}\sum_{i=1}^{n}\ell(f(x_{i};\theta),y_{i})\)
  - **(b) Trocar** "A regularização penaliza a complexidade:" + quadro "objetivo = …" + "pois baixo erro de treino não implica boa generalização." **por** "A regularização acrescenta a esse risco uma penalidade \(\lambda\Omega(\theta)\): na **L2** (*ridge*), \(\Omega = \lVert\theta\rVert_{2}^{2}\), que encolhe os coeficientes; na **L1** (*lasso*), \(\Omega = \lVert\theta\rVert_{1}\), que pode zerá-los e induz esparsidade. O hiperparâmetro \(\lambda\), escolhido na validação, controla o compromisso entre ajuste e complexidade."
- [ ] **P5-B (12) [ALTO] — Bagging × boosting ligados ao viés-variância** · +23 palavras · moderada +1,5 min
  - **Onde:** Substituir o item da lista na L60.
  - **Trocar:** “*ensembles*, como **Random Forests** e *boosting*, combinam múltiplos modelos para aumentar robustez e desempenho;”
  - **Por:** “*ensembles* combinam múltiplos modelos: o *bagging* (base das **Random Forests**) treina modelos em amostras *bootstrap* e reduz sobretudo a variância; o *boosting* (ex.: *gradient boosting*) ajusta modelos sequencialmente aos erros dos anteriores e reduz sobretudo o viés;”
- [ ] **P5-C (11) [ALTO] — Mecanismo e limitações do k-means** · +28 palavras · moderada +1,9 min
  - **Onde:** Substituir o item da lista na L77. P5-A, P5-B e P5-C, juntas, exigem os cortes C1 do Ponto 5.
  - **Trocar:** “**k-means**, que busca grupos compactos em torno de centroides;”
  - **Por:** “**k-means**, que minimiza a soma das distâncias quadráticas dos pontos ao centroide de seu grupo, alternando atribuição e atualização; exige fixar k (escolhido, por exemplo, pela silhueta), depende da inicialização (mitigada pelo k-means++) e favorece grupos esféricos;”

### Ponto 6 — Aprendizado por Reforço

- [ ] **P6-A (3) [ESSENCIAL] — Enxugar: retirar duas fórmulas, dois quadros e uma lista redundantes** · −67 palavras · moderada −7,2 min
  - **Cortes:** (1) L7: terminar a frase em ponto e apagar a fórmula L9–11. (2) L29: terminar em "...o futuro independe da história anterior." e apagar a fórmula L31–33. (3) Apagar L65–69. (4) Apagar o quadro L79–81. (5) Apagar "Também existem importantes trade-offs:" e a lista L143–148. (6) L172: trocar a frase por "Sua aplicação prática, porém, exige eficiência amostral, estabilidade, segurança e especificação cuidadosa da recompensa."
- [ ] **P6-B (13) [ALTO] — Deadly triad e estabilização do DQN** · +34 palavras · moderada +2,3 min
  - **Onde:** Substituir a frase da L127.
  - **Trocar:** “Com aproximadores de função, especialmente redes neurais, essas ideias originam o **Deep Reinforcement Learning** [4], que permite atuar em espaços de estado de alta dimensionalidade.”
  - **Por:** “Com redes neurais como aproximadores de função, essas ideias originam o **Deep Reinforcement Learning**. A combinação de aproximação de função, *bootstrapping* e aprendizado *off-policy* — a *deadly triad* [1] — pode tornar o treinamento instável ou divergente; o DQN [4] estabilizou o Q-learning profundo com *experience replay*, que reutiliza transições armazenadas, e *target network*, que mantém o alvo fixo por intervalos.”
- [ ] **P6-C (21) [ALTO] — Monte Carlo × TD (viés e variância)** · +39 palavras · moderada +2,7 min
  - **Onde:** Depois da L95 (após "...sem aguardar o término do episódio.").
  - **Inserir:** “Já os métodos de **Monte Carlo** atualizam com o retorno completo \(G_{t}\): a estimativa não tem viés, mas tem maior variância e só fica disponível ao fim do episódio; o TD troca algum viés por menor variância e aprendizado incremental.”

### Ponto 7 — MLOps: Desenvolvimento, Versionamento e Experimentação de Modelos

- [ ] **P7-A (19) [ALTO] — Busca de hiperparâmetros e superajuste à validação/benchmark** · +40 palavras · moderada +2,7 min
  - **Onde:** Novo parágrafo depois da L89 (antes do diagrama "EXPERIMENTO ↓ ...").
  - **Inserir:** “A busca de hiperparâmetros — em grade, aleatória ou bayesiana — é parte da experimentação: cada tentativa deve ser registrada e comparada apenas na validação, pois consultar repetidamente o conjunto de teste, ou ajustar-se a um mesmo *benchmark*, superestima o desempenho real.”
- [ ] **P7-B (16) [custo ~0] — Exemplos de ferramentas (Git, DVC, MLflow)** · +16 palavras · moderada +1,1 min
  - **Onde:** Final de 7.3.2, depois da L63.
  - **Inserir:** “Na prática, ferramentas como Git (código), DVC (dados) e MLflow (*tracking* e *registry*) materializam esse controle.”

### Ponto 8 — MLOps: Automação, Implantação e Infraestrutura de Aprendizado de Máquina

- [ ] **P8-A (8) [ESSENCIAL] — Infraestrutura como código (IaC)** · +35 palavras · moderada +2,3 min
  - **Onde:** Novo parágrafo no início de 8.3.3, depois da L82.
  - **Inserir:** “A própria infraestrutura deve ser declarada como código (**IaC**, *Infrastructure as Code*), com ferramentas como Terraform: versionada, revisada e aplicada de forma idempotente, ela torna os ambientes reprodutíveis e auditáveis e evita configurações manuais divergentes.”
- [ ] **P8-B (14) [ALTO] — Feature store como resposta ao training-serving skew** · +29 palavras · moderada +1,9 min
  - **Onde:** Depois da L78 (após "...compatíveis entre treinamento e produção.").
  - **Inserir:** “*Feature stores* reduzem esse risco ao centralizar a definição das *features* e servi-las de forma consistente ao treinamento (camada *offline*, histórica) e à inferência (camada *online*, de baixa latência).”
- [ ] **P8-C (7) [custo ~0] — Nomear ferramentas canônicas (Airflow/Kubeflow, Docker, Kubernetes)** · +16 palavras · moderada +1,1 min
  - **Microinserções:** (a) L19: acrescentar ao fim da frase ", em geral orquestrados como DAGs por ferramentas como Airflow ou Kubeflow Pipelines". (b) L45: "**Containers** empacotam" → "**Containers** (ex.: Docker) empacotam". (c) L86: "entra a **orquestração**, que" → "entra a **orquestração** (ex.: Kubernetes), que".

### Ponto 9 — MLOps: Monitoramento, Governança e Manutenção de Modelos

- [ ] **P9-A (18) [ALTO] — Marcos normativos (NIST AI RMF, ISO/IEC 42001, LGPD)** · +43 palavras · moderada +4,5 min
  - **Onde:** Depois da L86 (após "...controle do escopo de uso."). Exige os cortes C1 do Ponto 9 para não estourar o tempo.
  - **Inserir:** “Marcos normativos estruturam essa gestão: o NIST AI RMF [5] organiza-a em governar, mapear, medir e gerenciar riscos; a ISO/IEC 42001 [6] define um sistema de gestão de IA; e, havendo dados pessoais, inclusive em *logs* de predição, aplica-se a LGPD [7].”
  - *Versão mínima:* “A gestão de risco pode seguir o NIST AI RMF [5] e a ISO/IEC 42001 [6]; havendo dados pessoais, aplica-se a LGPD [7].”
  - **Referências:** [5] NIST. Artificial intelligence risk management framework (AI RMF 1.0). 2023. [6] ISO/IEC 42001: artificial intelligence: management system. 2023. [7] BRASIL. Lei nº 13.709, de 14 de agosto de 2018 (LGPD).
- [ ] **P9-B (5) [custo ~0] — Nomear testes e medidas de drift** · +9 palavras · moderada +0,6 min
  - **Onde:** L64: substituir o trecho indicado.
  - **Trocar:** “por testes ou medidas de distância”
  - **Por:** “por testes estatísticos (ex.: Kolmogorov–Smirnov, qui-quadrado) ou medidas de divergência (ex.: PSI, Jensen–Shannon)”

### Ponto 10 — XAI: Métodos, Interpretabilidade, Avaliação e Uso das Explicações

- [ ] **P10-A (23) [ALTO] — Valores de Shapley e suas propriedades** · +54 palavras · moderada +3,9 min
  - **Onde:** Depois da L50 (após "...atribuída à *feature* \(j\)."). Exige o corte C1 do Ponto 10 (L111).
  - **Inserir:** “Os \(\phi_{j}\) são **valores de Shapley**, da teoria dos jogos cooperativos: a média da contribuição marginal de \(j\) sobre todas as ordens de entrada das *features*, única atribuição que satisfaz eficiência (as contribuições somam \(f(x) - \phi_{0}\)), simetria, jogador nulo e aditividade; como o cálculo exato é exponencial no número de *features*, usam-se aproximações (KernelSHAP) ou algoritmos específicos (TreeSHAP).”
  - *Versão mínima:* “Os \(\phi_{j}\) são valores de Shapley, da teoria dos jogos cooperativos, únicos a satisfazer eficiência, simetria, jogador nulo e aditividade; seu cálculo exato é exponencial no número de *features*.”

## 3. Cortes

### 3.1 Cortes obrigatórios (pagam inserções do próprio ponto)

- **Ponto 6:** P6-A (seção 2), sempre.
- [ ] **P5-C1a** (L65–69): remover “A escolha depende, portanto, da hipótese estrutural que o método impõe: [quadro: método = algoritmo + hipótese sobre os dados]”. Economia (L / M / R): 1,8 / 1,4 / 1,2 min.
- [ ] **P5-C1b** (L116–122): remover “Não existe, portanto, algoritmo universalmente superior. A escolha deve considerar: [quadro: dados + objetivo + hipótese do modelo + métrica + restrições → método] Entre…” → substituir por “Não existe, portanto, algoritmo universalmente superior: a escolha depende de dados, objetivo, métrica e restrições como interpretabilidade, latência e custo dos erros.”. Economia (L / M / R): 2,0 / 1,6 / 1,4 min.
- [ ] **P9-C1a** (L88): remover “Governança não se confunde com explicabilidade: **governança controla o ciclo de vida; XAI procura interpretar o comportamento do modelo**.”. Economia (L / M / R): 1,6 / 1,3 / 1,1 min.
- [ ] **P9-C1b** (L147–151): remover “Todo esse ciclo é atravessado por: [quadro: GOVERNANÇA + LINEAGE + AUDITORIA + GESTÃO DE RISCO]”. Economia (L / M / R): 1,4 / 1,2 / 1,0 min.
- [ ] **P10-C1a** (L111): remover “Uma boa explicação é adequada ao usuário e à tarefa.”. Economia (L / M / R): 0,8 / 0,7 / 0,6 min.

### 3.2 Cortes de contingência

Aplicar conforme a regra da seção 0, ou **ao vivo, na prova**, se estiver atrasado:
- **C1:** sem perda conceitual.
- **C2:** perda pequena.
- **C3:** conclusão sem o diagrama vertical. Usar só no cenário lento.

| Corte | Nível | Onde | O que sai | Substituto | Economia L / M / R (min) |
|---|---|---|---|---|---|
| P1-C1a | C1 | L83, 1ª frase | Devem ainda ser considerados padrão de acesso, *throughput*, durabilidade, domínios de falha e custo operacional. | — | 1,2 / 1,0 / 0,8 |
| P1-C2a | C2 | L72 | Arquiteturas *shared-nothing* e a separação entre computação e armazenamento favorecem escalabilidade horizontal e evol… | — | 1,4 / 1,1 / 0,9 |
| P2-C1a | C1 | L101–107 | Existe, assim, um compromisso permanente entre: - **granularidade e overhead**; - **localidade e balanceamento**; - **p… | — | 2,4 / 1,9 / 1,6 |
| P2-C2a | C2 | L49–55 | De forma conceitual, [fórmula: T_{total} = T_{comp} + T_{comm} + T_{sync} + T_{overhead}] mostra que reduzir apenas o c… | Como o tempo total soma computação, comunicação, sincronização e *overhead*, reduzir apen… | 1,4 / 1,1 / 0,9 |
| P3-C1a | C1 | L17–21 | Conceitualmente, um evento percorre a cadeia: [quadro: FONTE → INGESTÃO → FLUXO → PROCESSAMENTO → ESTADO/SAÍDA → SERVIN… | — | 1,8 / 1,4 / 1,2 |
| P3-C2a | C2 | L81 | Garantias fortes exigem mais checkpoints, coordenação e transações; retenção prolongada facilita *replay* e auditoria,… | — | 1,6 / 1,3 / 1,1 |
| P4-C1a | C1 | L7–11 (trocar ":" por "." no fim da L7) | [quadro: Data Mining ⊂ KDD] | — | 0,4 / 0,4 / 0,3 |
| P4-C1b | C1 | L51–55 (trocar ":" por "." no fim da L51) | [quadro: exploração → hipótese → transformação → nova exploração] | — | 0,8 / 0,7 / 0,6 |
| P4-C2a | C2 | L143 | A mineração de dados é componente de um processo iterativo de descoberta, com retroalimentação entre as etapas, no qual… | — | 2,8 / 2,3 / 1,9 |
| P5-C2a | C2 | L105–110 | A escolha de um modelo envolve múltiplos trade-offs: - desempenho × interpretabilidade; - viés × variância; - precisão… | — | 2,2 / 1,7 / 1,4 |
| P6-C2a | C2 | L53–61 (trocar ":" por "." no fim da L53) | [fórmula: V^{\pi}(s) = \mathbb{E}_{\pi}\lbrack G_{t} \mid S_{t} = s\rbrack] [fórmula: Q^{\pi}(s,a) = \mathbb{E}_{\pi}\l… | — | 1,9 / 1,5 / 1,2 |
| P6-C2b | C2 | L73–77 | Para uma política \(\pi\), a equação de Bellman é: [fórmula: V^{\pi}(s) = \mathbb{E}_{\pi}\left\lbrack R_{t + 1} + \gam… | — | 2,0 / 1,6 / 1,3 |
| P7-C1a | C1 | L91–101 | [quadro: EXPERIMENTO ↓ VALIDAÇÃO DE DADOS E DO MODELO ↓ COMPARAÇÃO COM BASELINE ↓ CRITÉRIOS DE ACEITAÇÃO ↓ MODELO CANDI… | — | 2,4 / 2,0 / 1,7 |
| P7-C1b | C1 | L141–145 | Todo esse fluxo é atravessado por: [quadro: PROVENIÊNCIA + LINEAGE + REPRODUTIBILIDADE] | — | 1,1 / 0,9 / 0,7 |
| P7-C1c | C1 | L75–79 (trocar ":" por "." no fim da L75) | [quadro: reprodutível ≠ idêntico bit a bit] | — | 0,7 / 0,5 / 0,4 |
| P7-C2a | C2 | L113 | Outros desafios incluem dados mutáveis, dependências externas, não determinismo, proliferação de experimentos e artefat… | — | 1,7 / 1,3 / 1,1 |
| P8-C1a | C1 | L86–91 (trocar ":" por "." no fim da L86) | [quadro: CONTAINER → como executar de forma isolada? ORQUESTRAÇÃO → como coordenar muitas execuções?] | — | 1,4 / 1,1 / 1,0 |
| P8-C1b | C1 | L97–105 (trocar ":" por "." no fim da L97) | [quadro: REQUISIÇÕES ↓ LOAD BALANCER ↙ ↓ ↘ I1 I2 I3] | — | 1,2 / 1,1 / 0,9 |
| P8-C1c | C1 | L154–158 | Todo esse fluxo é atravessado por: [quadro: VALIDAÇÃO + VERSIONAMENTO + RECUPERAÇÃO + CONTROLE DE CUSTO] | — | 1,4 / 1,2 / 1,0 |
| P8-C2a | C2 | L54–58 (trocar ":" por "." no fim da L54) | [quadro: release confiável = artefato versionado + estratégia de implantação + rollback] | — | 1,1 / 0,9 / 0,8 |
| P9-C2a | C2 | L119 | Monitorar muitas *features* e métricas gera excesso de alertas e resultados estatisticamente significativos sem relevân… | — | 1,3 / 1,1 / 0,9 |
| P9-C2b | C2 | L121–125 | Automatizar ações demais também é arriscado, pois retreinamento automático mal governado pode introduzir erros ou ampli… | — | 2,2 / 1,8 / 1,5 |
| P10-C2a | C2 | L78–83 | Essas famílias respondem perguntas distintas: - ATRIBUIÇÃO → quais variáveis contribuíram? - SURROGATE → qual regra sim… | — | 2,8 / 2,3 / 1,9 |
| P10-C2b | C2 | L123 | Métodos *post hoc* podem ser aproximados, instáveis, sensíveis à baseline e afetados por correlação entre *features*. | — | 1,3 / 1,1 / 0,9 |
| P1-C3a | C3 | Conclusão (1.5): diagrama vertical | Em síntese: [quadro: DATASET ↓ PARTICIONAMENTO ↓ REPLICAÇÃO ↓ CONSISTÊNCIA / QUÓRUNS ↓ RECUPERAÇÃO E REBALANCEAMENTO ↓… | — | 2,3 / 2,0 / 1,7 |
| P2-C3a | C3 | Conclusão (2.5): diagrama vertical | Em síntese: [quadro: PROBLEMA ↓ DECOMPOSIÇÃO ↓ ESCALONAMENTO E BALANCEAMENTO ↓ COMUNICAÇÃO / SHUFFLE ↓ MODELO DE EXECUÇ… | — | 2,7 / 2,3 / 2,0 |
| P3-C3a | C3 | Conclusão (3.5): diagrama vertical | Em síntese: [quadro: EVENTOS ↓ INGESTÃO / LOG ↓ TEMPO / JANELAS / WATERMARKS ↓ ESTADO / CHECKPOINT / REPLAY ↓ GARANTIAS… | — | 2,6 / 2,2 / 1,9 |
| P4-C3a | C3 | Conclusão (4.5): diagrama vertical | Em síntese: [quadro: DADOS ↓ PREPARAÇÃO ↓ EDA ↓ PADRÕES / ANOMALIAS ↓ VALIDAÇÃO ↓ INTERPRETAÇÃO ↓ CONHECIMENTO] | — | 2,2 / 1,9 / 1,7 |
| P5-C3a | C3 | Conclusão (5.5): diagrama vertical | Em síntese: [quadro: PROBLEMA ↓ DADOS E RÓTULOS DISPONÍVEIS? ↓ FORMULAÇÃO SUPERVISIONADA / NÃO SUPERVISIONADA ↓ TREINAM… | — | 2,9 / 2,5 / 2,2 |
| P6-C3a | C3 | Conclusão (6.5): diagrama vertical | Em síntese: [quadro: INTERAÇÃO ↓ RETORNO ↓ VALOR ↓ POLÍTICA ↓ NOVA INTERAÇÃO] | — | 1,6 / 1,4 / 1,2 |
| P7-C3a | C3 | Conclusão (7.5): diagrama vertical | Em síntese: [quadro: HIPÓTESE ↓ EXPERIMENTO ↓ VERSIONAMENTO ↓ TRACKING ↓ VALIDAÇÃO ↓ MODELO CANDIDATO] | — | 1,9 / 1,6 / 1,5 |
| P8-C3a | C3 | Conclusão (8.5): diagrama vertical | Em síntese: [quadro: MODELO VALIDADO ↓ AUTOMAÇÃO ↓ EMPACOTAMENTO ↓ IMPLANTAÇÃO ↓ SERVING ↓ ESCALA E DISPONIBILIDADE ↓ O… | — | 2,5 / 2,1 / 1,9 |
| P9-C3a | C3 | Conclusão (9.5): diagrama vertical | Em síntese: [quadro: OBSERVAR ↓ DETECTAR ↓ DIAGNOSTICAR ↓ AGIR ↓ VALIDAR ↓ PROMOVER / REVERTER ↓ OBSERVAR NOVAMENTE ↺] | — | 2,4 / 2,1 / 1,8 |
| P10-C3a | C3 | Conclusão (10.5): diagrama vertical | Em síntese: [quadro: MODELO ↓ MÉTODO DE XAI ↓ EXPLICAÇÃO ↓ AVALIAÇÃO ↓ CONTEXTUALIZAÇÃO ↓ USO] | — | 2,0 / 1,7 / 1,5 |

## 4. Microcorreções de precisão (custo ~0)

- [ ] **P2** L18 e L23–26: “S_{p} / E_{p} (L18) e S(p) (L26)” → “usar uma só notação, S(p) e E(p)”.
- [ ] **P4** L89: “fenômeno biologicamente relevante” → “fenômeno cientificamente relevante”.
- [ ] **P4** L121: “biologicamente implausível” → “implausível no domínio”.
- [ ] **P5** L83: “também otimizam funções formais” → “também seguem critérios formais”.
- [ ] **P6** L104: “explora-se outra alternativa” → “escolhe-se uma ação ao acaso”.
- [ ] **P7** L70: “reprodutibilidade ≈ D + C + H + E + S” → “execução = f(D, C, H, E, S)”.
- [ ] **P10** L54–57: “pela queda de desempenho quando seus valores são embaralhados” → “pela queda de desempenho (em métricas nas quais maior é melhor) quando seus valores são embaralhados”.

## 5. ABNT mínimo (custo ~0)

- [ ] **Chamadas no texto:** escrever **(1)** ou expoente ¹, nunca [1].
- [ ] **Listas de referências:**
  - sobrenome em MAIÚSCULAS (Pontos 4–10);
  - todos os autores quando forem até três, separados por ";";
  - "et al." só com quatro ou mais;
  - "2. ed." quando houver.
- [ ] **Atualizar duas obras:**
  - P4 [3] → HAN, J.; PEI, J.; TONG, H. (4. ed., 2022);
  - P10 [1] → MOLNAR, C. (3. ed., 2025).
- [ ] **Novas referências ligadas às propostas** (forma manuscrita):
  - P1 [6] ABADI, D. Computer, 2012; P1 [7] KLEPPMANN, M.; RICCOMINI, C. (2. ed., 2026);
  - P3 [5] KREPS, J. Questioning the Lambda Architecture, 2014;
  - P9 [5] NIST AI RMF, 2023; P9 [6] ISO/IEC 42001, 2023; P9 [7] BRASIL, Lei nº 13.709/2018.
- **Listas finais na forma mínima** (custo ~0; a forma com títulos, se houver tempo, está no Apêndice B do relatório 04):

  - **P1:** (1) GHEMAWAT, S.; GOBIOFF, H.; LEUNG, S.-T. SOSP, 2003. (2) DECANDIA, G. et al. SOSP, 2007. (3) HERLIHY, M. P.; WING, J. M. ACM TOPLAS, 1990. (4) GILBERT, S.; LYNCH, N. ACM SIGACT News, 2002. (5) CHANG, F. et al. OSDI, 2006. (6) ABADI, D. Computer, 2012. (7) KLEPPMANN, M.; RICCOMINI, C. 2. ed. O'Reilly, 2026.
  - **P2:** (1) AMDAHL, G. M. AFIPS, 1967. (2) GUSTAFSON, J. L. Communications of the ACM, 1988. (3) DEAN, J.; GHEMAWAT, S. OSDI, 2004. (4) ZAHARIA, M. et al. NSDI, 2012.
  - **P3:** (1) AKIDAU, T. et al. PVLDB, 2015. (2) CARBONE, P. et al. PVLDB, 2017. (3) KREPS, J.; NARKHEDE, N.; RAO, J. NetDB, 2011. (4) MARZ, N.; WARREN, J. Manning, 2015. (5) KREPS, J. O'Reilly Radar, 2014.
  - **P4:** (1) FAYYAD, U.; PIATETSKY-SHAPIRO, G.; SMYTH, P. AI Magazine, 1996. (2) TUKEY, J. W. Addison-Wesley, 1977. (3) HAN, J.; PEI, J.; TONG, H. 4. ed. Morgan Kaufmann, 2022. (4) AGGARWAL, C. C. 2. ed. Springer, 2017.
  - **P5:** (1) BISHOP, C. M. Springer, 2006. (2) MURPHY, K. P. MIT Press, 2012. (3) HASTIE, T.; TIBSHIRANI, R.; FRIEDMAN, J. 2. ed. Springer, 2009. (4) GOODFELLOW, I.; BENGIO, Y.; COURVILLE, A. MIT Press, 2016.
  - **P6:** (1) SUTTON, R. S.; BARTO, A. G. 2. ed. MIT Press, 2018. (2) WATKINS, C. J. C. H.; DAYAN, P. Machine Learning, 1992. (3) WILLIAMS, R. J. Machine Learning, 1992. (4) MNIH, V. et al. Nature, 2015.
  - **P7:** (1) SCULLEY, D. et al. NeurIPS, 2015. (2) AMERSHI, S. et al. ICSE-SEIP, 2019. (3) KREUZBERGER, D.; KÜHL, N.; HIRSCHL, S. IEEE Access, 2023. (4) BRECK, E. et al. IEEE BigData, 2017.
  - **P8:** (1) SCULLEY, D. et al. NeurIPS, 2015. (2) KREUZBERGER, D.; KÜHL, N.; HIRSCHL, S. IEEE Access, 2023. (3) BRECK, E. et al. IEEE BigData, 2017. (4) TREVEIL, M. et al. O'Reilly, 2020.
  - **P9:** (1) SCULLEY, D. et al. NeurIPS, 2015. (2) GAMA, J. et al. ACM Computing Surveys, 2014. (3) BRECK, E. et al. IEEE BigData, 2017. (4) KREUZBERGER, D.; KÜHL, N.; HIRSCHL, S. IEEE Access, 2023. (5) NIST. AI RMF 1.0, 2023. (6) ISO/IEC 42001, 2023. (7) BRASIL. Lei nº 13.709, de 14 de agosto de 2018 (LGPD).
  - **P10:** (1) MOLNAR, C. 3. ed. Leanpub, 2025. (2) LUNDBERG, S. M.; LEE, S.-I. NeurIPS, 2017. (3) SUNDARARAJAN, M.; TALY, A.; YAN, Q. ICML, 2017. (4) RIBEIRO, M. T.; SINGH, S.; GUESTRIN, C. KDD, 2016.

## 6. Na prova

- **Ordem de escrita (sugestão):** comece pelo ponto sorteado com mais fórmulas (6, depois 10, 4, 2) e termine por um com poucas ou nenhuma (8, 7, 1, 3). Fórmulas são o que mais sofre com a fadiga: ficam mais lentas e mais sujeitas a erro.
- **Identificação:** dê a cada ponto o título com o número e o nome do edital (16.7: os três pontos devem ser identificáveis).
- **Marcos de tempo** (início às 9h):
  - terminar o 1º ponto até 10h20;
  - terminar o 2º até 11h40;
  - encerrar às 13h.
- **Dentro de cada ponto:**
  - minuto 0–3: esqueleto;
  - minuto ~45: terminando a seção X.3 (núcleo);
  - minuto ~70: conclusão escrita;
  - minutos 70–78: revisão.
- **Atraso no minuto 45:**
  - acima de 5 min: aplicar os cortes C1 do ponto ao vivo;
  - acima de 10 min: aplicar também C2 e C3.
- **Nunca omitir a conclusão** (critério 2.2) e nunca deixar um ponto pela metade (16.8). Se faltar tempo, as referências podem ir na forma mínima.

## 7. Não fazer

- Não acrescentar documentação de ferramentas, benchmarks, exemplos aplicados longos, listas de produtos nem fórmulas novas longas (PPO, contração de Bellman).
- Não detalhar todos os algoritmos do Ponto 5.
- Não escrever referências ABNT completas na prova (local, editora, páginas).
- Não memorizar nenhum item "se houver tempo" antes de concluir a lista FAZER.
- Lista completa e motivos: relatório 05, seção "NÃO FAZER".
