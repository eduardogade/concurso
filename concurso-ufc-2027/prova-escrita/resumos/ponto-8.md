# Ponto 8 — MLOps: Automação, Implantação e Infraestrutura de Aprendizado de Máquina

## 8.1. Introdução e Delimitação do Problema

8.1.A. [2][3] Apresentar o problema posterior à validação e as propriedades do sistema a construir.

8.1.B. [1][4] Ressaltar que o código do modelo é pequena parte do sistema, citando Sculley et al.

8.1.C. [3] Quadro contrapondo modelo validado e sistema operacional confiável.

8.1.D. [3] Delimitar o ponto: entrega e operação; monitoramento, governança e manutenção ficam para depois.

## 8.2. Fundamentos e Relevância

8.2.A. [2] Justificar a automação frente às sequências manuais.

8.2.B. [2][4] Descrever as etapas do pipeline de ML, citando Kreuzberger et al.

8.2.C. [4] Indicar a orquestração do pipeline como DAG, com Airflow ou Kubeflow.

8.2.D. [2] Lista numerada distinguindo CI, CD e CT.

8.2.E. [5] Ressaltar que CT não é retreinamento indiscriminado.

8.2.F. [1][4] Subordinar a automação aos quality gates, citando Breck et al.

8.2.G. [3] Quadro com a regra de promoção.

## 8.3. Núcleo Técnico

### 8.3.1. Empacotamento e Implantação

8.3.1.A. [1] Afirmar que implantar não é copiar o arquivo de pesos.

8.3.1.B. [2][3] Quadro com os componentes do artefato de implantação.

8.3.1.C. [2] Completar com pré e pós-processamento e o contrato de entrada e saída.

8.3.1.D. [2][4] Apresentar os containers, com o Docker, e justificar pelo ambiente idêntico ao validado.

8.3.1.E. [1][5] Comparar as quatro estratégias de liberação pelo equilíbrio entre risco, disponibilidade e custo.

8.3.1.F. [1] Exigir rollback em todos os casos.

### 8.3.2. Serving e Padrões de Inferência

8.3.2.A. [2] Introduzir o model serving.

8.3.2.B. [2] Apresentar a inferência batch, com o exemplo do escore noturno.

8.3.2.C. [1] Contrapor a inferência online e o que ela exige controlar, distinguindo latência e throughput.

8.3.2.D. [2] Mencionar o streaming.

8.3.2.E. [1][5] Explicar o training-serving skew e sua consequência.

8.3.2.F. [4][5] Apresentar as feature stores como resposta, servindo treinamento e inferência.

### 8.3.3. Infraestrutura, Containers e Orquestração

8.3.3.A. [1] Partir do problema dos ambientes configurados manualmente.

8.3.3.B. [2][4] Apresentar a infraestrutura como código, com o Terraform, e seu caráter declarativo.

8.3.3.C. [1][5] Concluir o ganho: recriar ambientes e registrar cada mudança.

8.3.3.D. [1] Ressaltar o limite dos containers.

8.3.3.E. [2][4] Introduzir a orquestração, com o Kubernetes, e suas funções.

8.3.3.F. [3] Quadro contrapondo as perguntas que container e orquestração respondem.

### 8.3.4. Escalabilidade e Disponibilidade

8.3.4.A. [2] Contrapor escala vertical e horizontal e indicar quando a horizontal funciona bem.

8.3.4.B. [2] Introduzir o balanceador de carga e o autoscaling.

8.3.4.C. [1][3] Quadro contrapondo escalabilidade e disponibilidade.

8.3.4.D. [1][5] Justificar com o ponto único de falha e indicar o que a alta disponibilidade exige.

## 8.4. Limitações, Trade-offs e Desafios Atuais

8.4.A. [1] Enumerar os compromissos da infraestrutura de ML.

8.4.B. [1][5] Contrapor underprovisioning e overprovisioning e indicar o objetivo.

8.4.C. [1] Afirmar que arquitetura mais sofisticada não é melhor, com o exemplo do serviço interno.

8.4.D. [5] Acrescentar a degradação graciosa à resiliência, com exemplos.

## 8.5. Conclusão

8.5.A. [3] Diagrama de síntese.

8.5.B. [1][3] Concluir que a arquitetura adequada atende aos requisitos de forma controlada, e não pela complexidade.

## Referências

R.A. [4] Referências em ABNT.
