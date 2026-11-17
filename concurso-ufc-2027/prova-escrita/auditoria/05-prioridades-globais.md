# Auditoria 2 — Prioridades globais

Data: 03/11/2026. Complementa [04-auditoria-custo-beneficio.md](04-auditoria-custo-beneficio.md) e é operacionalizado em [06-plano-minimo-de-revisao.md](06-plano-minimo-de-revisao.md).

## Resposta direta

- **Ordenação:** pelo benefício provável sobre o esforço (palavras, memorização e risco), não pela ordem dos pontos. Os dois primeiros itens não alteram texto: medem e protegem o tempo.
- **Grupo FAZER:** 21 alterações de texto, mais quatro itens globais. Somam ≈ +616 palavras brutas e ≈ +472 líquidas, após os cortes obrigatórios, nos dez textos (≈ 5%).
- **Se faltar tempo de estudo:** pare em qualquer posição da lista; cada item é independente, exceto onde se indica "exige cortes".

## 1. Tabela de prioridades

"Indicador" é a variação da nota central do modelo da Auditoria 1 (teto do instrumento DeepSeek), não previsão da nota oficial.

### FAZER ANTES DA PROVA

| Prioridade | Ponto | Alteração | Motivo | Custo em palavras | Ganho estimado | Decisão |
|---|---|---|---|---|---|---|
| 1 | Todos | **G1** — Medir a velocidade manuscrita real (teste de 15 min) | Decide se o plano cabe e quais cortes aplicar; nenhuma hipótese de velocidade foi medida. | 0 | Indireto e alto: evita estourar o tempo (16.8). | FAZER |
| 2 | Todos | **G2** — Regras de tempo na prova e cortes de contingência memorizados | Ponto incompleto elimina (16.8); cortar ao vivo exige saber o quê cortar. | 0 | Indireto e alto. | FAZER |
| 3 | 6 | **P6-A** — Enxugar: retirar duas fórmulas, dois quadros e uma lista redundantes (ESSENCIAL) | O item 16.8 elimina quem deixar o ponto incompleto. Cortar redundâncias não tira nenhum conceito e libera cerca de 7 min na hipótese moderada (9 min na lenta),… | −67, −2 fórmulas | Indireto e alto; indicador +0,00 | FAZER |
| 4 | 3 | **P3-A** — Correção: o Dataflow não se resume a "três perguntas" (ALTO CUSTO-BENEFÍCIO) | Uma imprecisão de atribuição visível a quem conhece a obra citada afeta o domínio técnico (1.1) e a precisão (2.3). A correção não custa nada. | −3 | Pequeno em pontos; indicador +0,00 | FAZER |
| 5 | 9 | **P9-B** — Nomear testes e medidas de drift (ALTO CUSTO-BENEFÍCIO) | Nove palavras tornam o método verificável (1.2/1.5) e evitam a impressão de conhecimento só genérico. | +9 | Moderado; indicador +0,20 | FAZER |
| 6 | 4 | **P4-B** — Nomear um método por família de detecção de anomalias (ALTO CUSTO-BENEFÍCIO) | Com +11 palavras, cada família ganha um representante canônico (1.2) e a regra do IQR se conecta ao boxplot de P4-A. | +11 | Moderado (1.2); indicador +0,38 | FAZER |
| 7 | 8 | **P8-C** — Nomear ferramentas canônicas (Airflow/Kubeflow, Docker, Kubernetes) (ALTO CUSTO-BENEFÍCIO) | Com cerca de 15 palavras, a banca reconhece a prática atual (1.4: atualização; 1.2) e passa a ver a distinção entre orquestrar pipelines e orquestrar container… | +16 | Moderado; indicador +0,35 | FAZER |
| 8 | 8 | **P8-A** — Infraestrutura como código (IaC) (ESSENCIAL) | IaC é o elo entre os dois termos do título (automação e infraestrutura) e a base da reprodutibilidade de ambientes. Sua ausência total é uma lacuna de ideia fu… | +35 | Alto; indicador +0,46 | FAZER |
| 9 | 1 | **P1-A** — Transações distribuídas (ACID, 2PC, BASE) (ESSENCIAL) | Atomicidade de transações multi-partição e o 2PC são o núcleo clássico de "gerenciamento distribuído de dados" (bancos de dados distribuídos). É uma ideia fund… | +76 (+9 ref.) | Alto e de confiança moderada; indicador +0,85 | FAZER |
| 10 | 4 | **P4-A** — Conteúdo operacional mínimo da EDA (ESSENCIAL) | Sem nenhum instrumento concreto, a banca pode ler a EDA como tratada só de passagem. É ideia fundamental (1.2) de um dos quatro componentes do título. Uma fras… | +52 | Alto e de confiança moderada; indicador +0,53 | FAZER |
| 11 | 5 | **P5-C** — Mecanismo e limitações do k-means (ALTO CUSTO-BENEFÍCIO) | Uma frase mostra objetivo, algoritmo, hiperparâmetro, sensibilidade à inicialização e viés geométrico: ideia fundamental (1.2) e aprofundamento (1.5) do lado n… P5-A/B/C exigem os cortes C1 do Ponto 5. | +28 | Moderado (1.2/1.5); indicador +0,40 | FAZER |
| 12 | 5 | **P5-B** — Bagging × boosting ligados ao viés-variância (ALTO CUSTO-BENEFÍCIO) | Explica o mecanismo dos dois métodos mais usados em dados tabulares e os liga ao compromisso viés-variância já desenvolvido em 5.2. Demonstra domínio (1.1) e i… | +23 | Moderado a alto (1.2); indicador +0,29 | FAZER |
| 13 | 6 | **P6-B** — Deadly triad e estabilização do DQN (ALTO CUSTO-BENEFÍCIO) | Transforma uma menção vaga em análise causal: o que torna o RL profundo instável e como o DQN [4] o estabilizou. É o aprofundamento (1.5) mais esperado em RL m… | +34 | Moderado a alto (1.5/1.2); indicador +0,46 | FAZER |
| 14 | 8 | **P8-B** — Feature store como resposta ao training-serving skew (ALTO CUSTO-BENEFÍCIO) | Completa o raciocínio problema → solução (1.1) e cobre um componente de infraestrutura de ML (1.2), em uma frase. | +29 | Moderado; indicador +0,36 | FAZER |
| 15 | 1 | **P1-B** — PACELC como complemento do CAP (ALTO CUSTO-BENEFÍCIO) | Completa a crítica ao CAP com o caso mais frequente na prática (operação normal, sem partição). É domínio crítico (1.1) e aprofundamento (1.5), com uma citação… | +32 (+9 ref.) | Moderado; indicador +0,31 | FAZER |
| 16 | 7 | **P7-B** — Exemplos de ferramentas (Git, DVC, MLflow) (ALTO CUSTO-BENEFÍCIO) | Uma frase de 15 palavras ancora os princípios em práticas reconhecíveis (1.2 e 1.4: atualização), sem virar tutorial. | +16 | Baixo a moderado; indicador +0,25 | FAZER |
| 17 | 3 | **P3-C** — Nomear engines, ligar [2] ao Flink, citar a Kappa e incluir ACID no lakehouse (ALTO CUSTO-BENEFÍCIO) | Quatro microinserções (+12 palavras no corpo) dão concretude (1.2), atribuem a Kappa a quem a propôs (1.4) e corrigem uma caracterização incompleta do lakehous… | +12 (+8 ref.) | Moderado (1.2 + 1.4); indicador +0,19 | FAZER |
| 18 | 9 | **P9-A** — Marcos normativos (NIST AI RMF, ISO/IEC 42001, LGPD) (ALTO CUSTO-BENEFÍCIO) | Atende diretamente à palavra "normas" do item 1.4 e mostra atualização (2018–2023). Liga a governança a referenciais reconhecíveis por qualquer banca. Exige os cortes C1 do Ponto 9. | +43 (+24 ref.) | Moderado a alto em 1.4; indicador +0,44 | FAZER |
| 19 | 7 | **P7-A** — Busca de hiperparâmetros e superajuste à validação/benchmark (ALTO CUSTO-BENEFÍCIO) | Dá conteúdo metodológico à experimentação (1.2) e acrescenta análise crítica (1.1): o uso repetido do teste ou de um benchmark superestima o desempenho. | +40 | Moderado (1.2 + 1.1); indicador +0,38 | FAZER |
| 20 | 2 | **P2-A** — RDD, avaliação preguiçosa e dependências estreitas × largas (ALTO CUSTO-BENEFÍCIO) | RDD e avaliação preguiçosa são a ideia fundamental (1.2) do modelo de execução mais usado em larga escala. Dependências estreitas × largas explicam tecnicament… | +38 | Moderado; indicador +0,29 | FAZER |
| 21 | 6 | **P6-C** — Monte Carlo × TD (viés e variância) (ALTO CUSTO-BENEFÍCIO) | MC × TD é comparação central de qualquer curso de RL (1.2) e mostra compreensão do bootstrapping (1.5). Uma frase. | +39 | Moderado (1.2/1.5); indicador +0,32 | FAZER |
| 22 | 5 | **P5-A** — Risco empírico explícito e regularização L1/L2 (ALTO CUSTO-BENEFÍCIO) | Converte duas fórmulas genéricas em formalização precisa (1.1/1.5) por substituição: o texto cresce pouco e passa a mostrar o efeito distinto de L1 (esparsidad… | +29 | Moderado; indicador +0,20 | FAZER |
| 23 | 10 | **P10-A** — Valores de Shapley e suas propriedades (ALTO CUSTO-BENEFÍCIO) | Para um examinador de XAI, falar de SHAP sem Shapley é a omissão mais visível do texto. Uma frase dá o fundamento (1.1), a formalização (1.5) e o custo computa… Exige o corte C1 do Ponto 10. | +54 | Moderado; indicador +0,35 | FAZER |
| 24 | Todos | **G3** — ABNT de custo zero: (n) em vez de [n]; sobrenome em MAIÚSCULAS; todos os autores até três; edição; Han–Pei–Tong 4. ed. 2022 e Molnar 3. ed. 2025 | Corrige violações objetivas da NBR 6023/10520 e atualiza duas obras sem custo de conteúdo. | ≈ +5 a +10 por ponto (nomes de coautores) | Baixo a moderado em 1.4; incerto (depende da leitura de "normas técnicas"). | FAZER |
| 25 | 2, 4, 5, 6, 7, 10 | **G4** — Microajustes de precisão (7 trocas de 2–6 palavras) | Imprecisões menores identificadas na leitura independente. | ≈ 0 | Baixo; remove pontos de desconto em 1.1/2.3. | FAZER |

### FAZER SOMENTE SE HOUVER TEMPO

Aplicar só se o teste de velocidade der ≥ 16 palavras/min e a lista FAZER já estiver memorizada.

| Prioridade | Ponto | Alteração | Motivo | Custo em palavras | Ganho estimado | Decisão |
|---|---|---|---|---|---|---|
| 1 | 1 | **P1-C** — Arquitetura mínima de DFS (GFS/HDFS) (OPCIONAL) | Torna concreto o sistema citado [1] e cobre o item 1.2 de maior peso no DeepSeek. Fica abaixo de P1-A/P1-B porque o ganho oficial é menor e o texto já cobre os… | +17 | Baixo a moderado (1.2); indicador +0,30 | SÓ SE HOUVER TEMPO |
| 2 | 3 | **P3-B** — Offsets e consumer groups no Kafka (OPCIONAL) | Explica como o replay funciona (1.1/1.2). Fica como opcional porque o ponto já está forte e o mecanismo é detalhe do Kafka. | +35 | Baixo a moderado (1.2); indicador +0,17 | SÓ SE HOUVER TEMPO |
| 3 | 4 | **P4-C** — Agrupamento sem remeter ao Ponto 5 (OPCIONAL) | Troca a remissão por uma crítica relevante: algoritmos de agrupamento sempre produzem grupos (1.1/1.2). Custo líquido de +20 palavras. | +19 | Moderado (1.2); indicador +0,24 | SÓ SE HOUVER TEMPO |
| 4 | 9 | **P9-C** — Feedback loops e rótulos seletivos (OPCIONAL) | É um caso-limite clássico de monitoramento (1.1/1.5). Fica como opcional porque o ponto já é longo e está entre os mais fortes. | +31 | Baixo a moderado; indicador +0,24 | SÓ SE HOUVER TEMPO |
| 5 | 2 | **P2-B** — Exemplo concreto: join com shuffle × broadcast join (OPCIONAL) | Troca uma frase abstrata por um exemplo que a demonstra (1.5) e cobre operadores distribuídos (1.2). Ganho real, mas o ponto já está entre os mais fortes. | +20 | Baixo a moderado (1.5/1.2); indicador +0,15 | SÓ SE HOUVER TEMPO |
| 6 | 7 | **P7-C** — CACE e dívida técnica (Sculley et al.) (OPCIONAL) | Dá à citação [1] seu conteúdo próprio (1.4) e reforça a justificativa do versionamento (1.1). | +30 | Baixo a moderado (1.1/1.4); indicador +0,09 | SÓ SE HOUVER TEMPO |
| 7 | 10 | **P10-B** — PDP e ICE (OPCIONAL) | Completa os métodos globais (1.2), mas o ponto já é o mais forte e o mais longo; o ganho marginal é pequeno. | +39 | Baixo; indicador +0,20 | SÓ SE HOUVER TEMPO |
| 8 | 8 | **P8-O1** — Shadow deployment (OPCIONAL) | Refinamento; ver Relatório 04, Ponto 8. | ≈ +14 | baixo | SÓ SE HOUVER TEMPO |
| 9 | 8 | **P8-O2** — Latência por percentis (OPCIONAL) | Refinamento; ver Relatório 04, Ponto 8. | ≈ +13 | baixo | SÓ SE HOUVER TEMPO |
| 10 | 1 | **P1-O1** — MVCC e snapshots (OPCIONAL) | Refinamento; ver Relatório 04, Ponto 1. | ≈ +20 | baixo | SÓ SE HOUVER TEMPO |
| 11 | 6 | **P6-O1** — Condições de convergência do Q-learning (OPCIONAL) | Refinamento; ver Relatório 04, Ponto 6. | ≈ +25 | baixo | SÓ SE HOUVER TEMPO |
| 12 | 5 | **P5-O1** — Regressão logística (OPCIONAL) | Refinamento; ver Relatório 04, Ponto 5. | ≈ +11 | baixo | SÓ SE HOUVER TEMPO |
| 13 | 4 | **P4-O1** — Medidas de proximidade por tipo de atributo (OPCIONAL) | Refinamento; ver Relatório 04, Ponto 4. | ≈ +26 | baixo | SÓ SE HOUVER TEMPO |
| 14 | 4 | **P4-O2** — Propriedade do Apriori (OPCIONAL) | Refinamento; ver Relatório 04, Ponto 4. | ≈ +22 | baixo | SÓ SE HOUVER TEMPO |
| 15 | 2 | **P2-O1** — YARN (OPCIONAL) | Refinamento; ver Relatório 04, Ponto 2. | ≈ +24 | baixo | SÓ SE HOUVER TEMPO |
| 16 | 3 | **P3-O1** — CDC na ingestão (OPCIONAL) | Refinamento; ver Relatório 04, Ponto 3. | ≈ +17 | baixo | SÓ SE HOUVER TEMPO |
| 17 | 9 | **P9-O1** — Label shift (OPCIONAL) | Refinamento; ver Relatório 04, Ponto 9. | ≈ +5 | baixo | SÓ SE HOUVER TEMPO |
| 18 | 10 | **P10-O1** — Citar Wachter (contrafactuais) e Rudin (modelos interpretáveis) (OPCIONAL) | Refinamento; ver Relatório 04, Ponto 10. | ≈ +14 | baixo | SÓ SE HOUVER TEMPO |
| 19 | 10 | **P10-O2** — Atribuir a taxonomia de avaliação à origem (OPCIONAL) | Refinamento; ver Relatório 04, Ponto 10. | ≈ +8 | baixo | SÓ SE HOUVER TEMPO |
| 20 | 6 | **P6-O2** — RLHF como exemplo atual de especificação de recompensa (OPCIONAL) | Refinamento; ver Relatório 04, Ponto 6. | ≈ +27 | baixo | SÓ SE HOUVER TEMPO |
| 21 | Todos | **G5** — Títulos nas referências (forma manuscrita do Apêndice B do 04) | Conformidade ABNT mais ampla. | ≈ +40 por ponto | Incerto. | SÓ SE HOUVER TEMPO |
| 22 | 1–10 | **G6** — Uma referência moderna adicional por ponto (tabela 11.4 do 04) | Atualização bibliográfica. | ≈ +10 por ponto | Baixo a moderado em 1.4. | SÓ SE HOUVER TEMPO |

### NÃO FAZER

| Prioridade | Ponto | Alteração | Motivo | Custo em palavras | Ganho estimado | Decisão |
|---|---|---|---|---|---|---|
| — | Todos | Documentação de ferramentas "com versão" e benchmarks (YCSB, HiBench, TPCx-HS, MLPerf) | Inexigível numa prova manuscrita sem consulta (Res. 15/CEPE, art. 20, § 6º). | alto | improvável | DESNECESSÁRIO |
| — | Todos | Exemplos aplicados extensos (telemetria, fraude, crédito, CartPole) | Custam 80–150 palavras (6–12 min) cada e deslocam conteúdo central. | alto | improvável | CONTRAPRODUCENTE |
| — | Todos | Referências ABNT completas (evento, local, editora, páginas) na prova | +3 a 5 min por ponto; risco de erro de memória. Usar a forma manuscrita da seção 11. | alto | improvável | CONTRAPRODUCENTE |
| — | Todos | Mais de uma referência nova por ponto, além das ligadas às propostas | Carga de memorização desproporcional ao ganho em 1.4. | alto | improvável | DESNECESSÁRIO |
| — | 5 | Detalhar os sete algoritmos (árvores com Gini, SVM com kernels e C/γ, MLP com backpropagation…) | +300 a 400 palavras: o ponto deixaria de caber em 80 min. | alto | improvável | CONTRAPRODUCENTE |
| — | 6 | Prova da contração de Bellman; objetivo truncado do PPO em fórmula; Double DQN; UCB/Thompson | Fórmulas longas, alto risco de erro manuscrito, ganho incerto. | alto | improvável | CONTRAPRODUCENTE |
| — | 7 | Avaliação offline × online | Fora do recorte declarado na L17; é conteúdo do Ponto 9. | alto | improvável | DESNECESSÁRIO |
| — | 7 | Boas práticas de Git (branches, tags), notebooks × scripts, model cards e datasheets | Detalhe de engenharia; P7-B já ancora a prática. | alto | improvável | DESNECESSÁRIO |
| — | 8 | Nomear KServe, Seldon, TorchServe, TF Serving, Feast, Tecton | Lista de produtos; Docker, Kubernetes, Airflow/Kubeflow e Terraform bastam. | alto | improvável | DESNECESSÁRIO |
| — | 8 | Cold start, scale-to-zero, multi-tenancy, assinatura de imagens | Detalhe de plataforma ou segurança. | alto | improvável | DESNECESSÁRIO |
| — | 9 | Taxonomia de manutenção corretiva/adaptativa/perfectiva; on-call e runbooks; data poisoning | Periférico ao núcleo do ponto. | alto | improvável | DESNECESSÁRIO |
| — | 10 | Explicações por atenção, XAI para LLMs, direito à explicação na LGPD | Temas vizinhos; abrir frentes novas em 80 min não compensa. | alto | improvável | DESNECESSÁRIO |
| — | 1 | Paxos/Raft, relógios vetoriais, multi-líder em detalhe | O texto já menciona consenso; detalhar desloca o foco. | alto | improvável | DESNECESSÁRIO |
| — | 2 | Componentes do YARN (ResourceManager, NodeManager), Catalyst, Pregel/BSP | Detalhe de produto ou modelo periférico. | alto | improvável | DESNECESSÁRIO |

## 2. Situação de cada dissertação

| Ponto | Situação | O que falta | Veredito |
|---|---|---|---|
| 1 | Exige trabalho | P1-A (essencial), P1-B | CORRIGIR PONTUALMENTE |
| 2 | Quase fechada | P2-A | CORRIGIR PONTUALMENTE (leve) |
| 3 | **Fechada** após microajustes | P3-A (4 palavras), P3-C | MANTER |
| 4 | Exige trabalho | P4-A (essencial), P4-B | CORRIGIR PONTUALMENTE |
| 5 | Exige trabalho | P5-A/B/C + cortes C1 | CORRIGIR PONTUALMENTE E ENXUGAR |
| 6 | Exige enxugamento | P6-A (cortes), P6-B, P6-C | ENXUGAR |
| 7 | Exige trabalho leve | P7-A, P7-B | CORRIGIR PONTUALMENTE |
| 8 | Exige trabalho | P8-A (essencial), P8-B, P8-C | CORRIGIR PONTUALMENTE |
| 9 | Quase fechada | P9-B; P9-A + cortes C1 | CORRIGIR PONTUALMENTE E ENXUGAR |
| 10 | **Fechada** após uma inserção | P10-A + corte C1 | MANTER |

## 3. Efeito agregado (indicador, não previsão)

| Ponto | Central antes | Central após FAZER | Literal (R1) antes → após | Escrita moderada antes → após (min) |
|---|---|---|---|---|
| 1 | 7,11 | 8,27 | 6,26 → 7,11 | 55,9 → 64,2 |
| 2 | 8,31 | 8,60 | 7,24 → 7,49 | 60,6 → 63,2 |
| 3 | 8,48 | 8,66 | 7,69 → 7,85 | 60,1 → 61,3 |
| 4 | 7,36 | 8,28 | 6,61 → 7,36 | 62,0 → 66,2 |
| 5 | 6,97 | 7,85 | 6,50 → 7,31 | 63,4 → 65,6 |
| 6 | 7,83 | 8,60 | 7,19 → 7,84 | 69,9 → 67,7 |
| 7 | 7,50 | 8,13 | 6,68 → 7,21 | 59,9 → 63,6 |
| 8 | 6,97 | 8,13 | 6,36 → 7,42 | 59,0 → 64,3 |
| 9 | 8,33 | 8,95 | 7,74 → 8,28 | 64,7 → 67,3 |
| 10 | 9,20 | 9,55 | 7,51 → 7,80 | 64,2 → 67,4 |

**Combinações de três pontos** (média simples, mesma hipótese exploratória do relatório 03; contagens de combinações, não probabilidades):

| Leitura | Pior trio antes | Pior trio após | Trios < 7,00 antes → após | Trios ≥ 8,00 antes → após |
|---|---|---|---|---|
| Literal (R1) | 6,38 (1, 5, 8) | 7,21 (1, 5, 7) | 63 → 0 | 0 → 0 |
| Central (R2) | 7,01 (1, 5, 8) | 8,04 (5, 7, 8) | 0 → 0 | 34 → 120 |
| Viável (R3) | 7,90 (1, 5, 8) | 8,98 (1, 4, 5) | 0 → 0 | 118 → 120 |

**Leitura:**

- **Mais relevante:** na leitura literal (a banca mais exigente), o plano tira todos os trios de baixo de 7,00.
- **Ressalva:** o modelo é generoso com cobertura (seção 0.3 do relatório 04); trate os números como direção, não como magnitude.
- **Regra dominante:** o item 16.8 do edital (ponto incompleto elimina) continua valendo; por isso, nenhuma inserção deve ser memorizada sem o respectivo corte quando o teste de velocidade indicar ≤ 15 palavras/min.

## 4. Como a ordem foi definida

1. **Itens que protegem o tempo:** G1, G2 e P6-A. Sem eles, qualquer ganho de conteúdo pode ser anulado pelo item 16.8.
2. **Custo ~0 com ganho certo:** P3-A, P9-B, P4-B, P8-C. São trocas de até 16 palavras.
3. **Lacunas essenciais:** P8-A, P1-A, P4-A. Vêm antes dos refinamentos, mesmo custando mais.
4. **Mecanismos que substituem linhas genéricas nos pontos de nota central mais baixa:** 5, 6 e 8.
5. **Refinamentos em pontos já fortes:** 1-B, 7, 3, 9, 2 e 10.
6. **Formalidades ABNT** (G3) e microajustes (G4) no fim: custo baixo, mas ganho incerto e memorização dispersa por dez listas.

