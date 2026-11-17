# Ponto 9 — MLOps: Monitoramento, Governança e Manutenção de Modelos

## 1. Introdução e Delimitação do Problema

A entrada de um modelo em produção não encerra seu ciclo de vida. Dados, comportamento dos usuários, regras de negócio, infraestrutura e a própria relação entre variáveis podem mudar ao longo do tempo [1]:

```text
modelo implantado ≠ modelo permanentemente válido
```

O objetivo do monitoramento e da manutenção é identificar mudanças relevantes, diagnosticar suas causas e controlar as intervenções durante toda a vida operacional do modelo. Construção e implantação são pressupostas: o ponto trata de **observar, governar e manter**.

## 2. Fundamentos e Relevância

A saúde de um sistema de ML possui duas dimensões:

```text
sistema disponível ≠ modelo correto
```

O **monitoramento operacional** verifica se o serviço continua tecnicamente saudável: latência, *throughput*, disponibilidade, erros e recursos. O **monitoramento de ML** verifica se dados, predições e desempenho continuam compatíveis com as condições em que o modelo foi validado.

A **observabilidade** permite inferir o estado interno do sistema a partir de sinais externos: métricas indicam se há problema; logs, o que aconteceu; *traces*, onde aconteceu. SLIs e SLOs formalizam indicadores e objetivos, permitindo alertas quando limites são violados. Um sinal isolado, porém, não é diagnóstico.

## 3. Núcleo Técnico

### 3.1. Qualidade de Dados, Data Drift e Concept Drift

Problemas de **qualidade de dados**, como alterações de esquema, valores ausentes ou fora de faixa e falhas de pipeline, afetam a validade das próprias entradas. O **data drift** representa mudança na distribuição dos dados:

\[
P_t(X)\neq P_{\text{train}}(X)
\]

Um caso particular é o *covariate shift*, no qual \(P(X)\) muda enquanto \(P(Y\mid X)\) permanece aproximadamente estável. O **concept drift** ocorre quando muda a relação entre entrada e alvo [2]:

\[
P_t(Y\mid X)\neq P_{\text{train}}(Y\mid X)
\]

```text
DATA QUALITY → os dados são válidos?
DATA DRIFT → P(X) mudou?
CONCEPT DRIFT → P(Y|X) mudou?
DEGRADAÇÃO → o desempenho piorou?
```

Esses eventos não são equivalentes: drift detectado não é degradação comprovada. Uma mudança estatística pode ser irrelevante para a tarefa, enquanto concept drift pode degradar o modelo sem mudança evidente em \(P(X)\). A detecção compara distribuições atuais com uma baseline por testes ou medidas de distância; como significância estatística não equivale a relevância operacional, importam magnitude, persistência e impacto preditivo.

### 3.2. Monitoramento Preditivo e Detecção de Degradação

Quando o *ground truth* está disponível, o desempenho em produção é medido por métricas adequadas à tarefa, comparando-se \(M_t\) com \(M_{\text{baseline}}\) ao longo do tempo, pois uma métrica agregada pode esconder degradação gradual ou localizada [3]. Em muitos sistemas, porém, existe **feedback delay** entre a predição e o rótulo verdadeiro; enquanto isso, monitoram-se sinais indiretos, como distribuições de *features* e predições e confiança do modelo, que sugerem, mas não provam, erro.

A detecção por *thresholds* (\(M_t<\tau\Rightarrow\text{alerta}\)) envolve o trade-off **sensibilidade × estabilidade**: limites sensíveis produzem falsos alarmes; limites conservadores atrasam a detecção. A análise deve considerar segmentos, pois média global estável não implica segmentos estáveis. Por fim, degradação detectada não é causa identificada: o fluxo correto é **detectar → diagnosticar → agir**.

### 3.3. Governança, Auditoria e Lineage

```text
governança = responsabilidade + rastreabilidade + controle
```

Para cada modelo deve ser possível identificar versão, finalidade, responsável, dados, validações, aprovações, histórico de alterações e riscos conhecidos. O **lineage** permite reconstruir a origem, a transformação e o uso de dados e modelos [4], e uma **trilha de auditoria** registra validação, implantação, *rollback*, retreinamento, substituição e aposentadoria.

A governança deve ser proporcional ao risco: modelos críticos podem exigir validação independente, aprovação formal, monitoramento mais rigoroso, contingência e controle do escopo de uso. Governança não se confunde com explicabilidade: **governança controla o ciclo de vida; XAI procura interpretar o comportamento do modelo**.

### 3.4. Manutenção, Retreinamento e Ciclo de Vida

A manutenção deve ser orientada por diagnóstico:

```text
drift detectado ≠ retreinamento obrigatório
```

Se a causa for uma coluna corrompida, mudança de unidade ou quebra do pipeline, retreinar pode simplesmente incorporar o erro ao novo modelo. As intervenções possíveis incluem corrigir dados ou pipeline, recalibrar, retreinar, realizar *rollback*, substituir ou aposentar o modelo.

O retreinamento **periódico** é simples, mas pode gerar desperdício ou reação tardia; o **orientado por eventos** é mais adaptativo, mas depende da qualidade dos gatilhos. Mesmo após retreinamento, o novo candidato não é promovido automaticamente: deve ser validado, comparado com a baseline e submetido aos critérios de aceitação, como em estratégias **champion–challenger**. O modelo é, assim, um artefato com ciclo de vida, que inclui sua aposentadoria.

## 4. Limitações, Trade-offs e Desafios Atuais

A primeira limitação é o *ground truth* tardio ou ausente, que torna os sinais indiretos menos conclusivos. Há ainda trade-offs entre:

- sensibilidade × falsos alarmes;
- frequência de monitoramento × custo;
- retreinamento frequente × estabilidade operacional;
- governança rigorosa × agilidade.

Monitorar muitas *features* e métricas gera excesso de alertas e resultados estatisticamente significativos sem relevância prática. Automatizar ações demais também é arriscado, pois retreinamento automático mal governado pode introduzir erros ou amplificar problemas nos dados:

```text
detecção automática ≠ correção automática obrigatória
```

## 5. Conclusão

Em síntese:

```text
OBSERVAR
↓
DETECTAR
↓
DIAGNOSTICAR
↓
AGIR
↓
VALIDAR
↓
PROMOVER / REVERTER
↓
OBSERVAR NOVAMENTE ↺
```

Todo esse ciclo é atravessado por:

```text
GOVERNANÇA + LINEAGE + AUDITORIA + GESTÃO DE RISCO
```

Monitoramento e manutenção fecham o ciclo operacional de MLOps ao transformar observações de produção em decisões controladas. Manter um modelo não significa apenas garantir que ele continue executando, mas demonstrar que seus **dados, desempenho, finalidade, risco e histórico permanecem sob controle durante todo o ciclo de vida**.

## Referências

[1] SCULLEY, D. et al. *Hidden Technical Debt in Machine Learning Systems*. 2015.
[2] GAMA, J. et al. *A Survey on Concept Drift Adaptation*. 2014.
[3] BRECK, E. et al. *The ML Test Score: A Rubric for ML Production Readiness and Technical Debt Reduction*. 2017.
[4] KREUZBERGER, D.; KÜHL, N.; HIRSCHL, S. *Machine Learning Operations (MLOps): Overview, Definition, and Architecture*. 2023.
