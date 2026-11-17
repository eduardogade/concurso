# Ponto 9 — MLOps: Monitoramento, Governança e Manutenção de Modelos

## 9.1. Introdução e Delimitação do Problema

A entrada de um modelo em produção não encerra seu ciclo de vida. Dados, comportamento dos usuários, regras de negócio e a própria relação entre variáveis mudam com o tempo:

```text
modelo implantado ≠ modelo permanentemente válido
```

O objetivo do monitoramento e da manutenção é detectar mudanças relevantes, diagnosticar suas causas e controlar as intervenções. Construção e implantação são pressupostas: o ponto trata de **observar, governar e manter**.

## 9.2. Fundamentos e Relevância

A saúde de um sistema de ML tem duas dimensões:

```text
sistema disponível ≠ modelo correto
```

O **monitoramento operacional** verifica se o serviço está saudável: latência, *throughput*, disponibilidade, erros e recursos. O **monitoramento de ML** verifica se dados, predições e desempenho continuam compatíveis com as condições de validação.

A **observabilidade** permite inferir o estado interno do sistema por sinais externos: métricas indicam se há problema; logs, o que aconteceu; *traces*, onde aconteceu. **SLIs** (indicadores) e **SLOs** (metas) definem quando disparar alertas.

## 9.3. Núcleo Técnico

### 9.3.1. Qualidade de Dados, Data Drift e Concept Drift

Problemas de **qualidade de dados**, como mudança de esquema, valores ausentes ou fora de faixa e falhas de pipeline, afetam a validade das próprias entradas.

O **data drift** é a mudança na distribuição das entradas:

\[
P_{t}(X) \neq P_{\text{train}}(X)
\]

Se \(P(X)\) muda mas \(P(Y \mid X)\) se mantém, fala-se em *covariate shift*. O **concept drift**¹ é a mudança na própria relação entre entrada e alvo, como quando fraudadores mudam de estratégia:

\[
P_{t}(Y \mid X) \neq P_{\text{train}}(Y \mid X)
\]

```text
DATA QUALITY → os dados são válidos?
DATA DRIFT → P(X) mudou?
CONCEPT DRIFT → P(Y|X) mudou?
DEGRADAÇÃO → o desempenho piorou?
```

Esses eventos não são equivalentes: drift detectado não é degradação comprovada. Uma mudança em \(P(X)\) pode não afetar o desempenho, e o concept drift pode degradá-lo sem mudança visível em \(P(X)\).

Para detectar drift, compara-se a distribuição atual de cada *feature* com a do treinamento: testes como o de **Kolmogorov–Smirnov** (variáveis contínuas) e o **qui-quadrado** (categóricas) indicam se a diferença é significativa, e o **PSI** mede sua magnitude. Como, com muitos dados, quase toda diferença é significativa, importam magnitude, persistência e impacto nas predições.

### 9.3.2. Monitoramento Preditivo e Detecção de Degradação

Quando os rótulos verdadeiros (*ground truth*) estão disponíveis, compara-se a métrica atual \(M_{t}\) com a de referência ao longo do tempo. Uma métrica agregada, porém, pode esconder degradação gradual ou restrita a um segmento.

Em muitos sistemas há **atraso no feedback**: o rótulo de um empréstimo só surge meses depois. Enquanto isso, monitoram-se sinais indiretos, como distribuição das *features* e das predições e confiança do modelo, que sugerem, mas não provam, erro.

A detecção por limiar (\(M_{t} < \tau \Rightarrow\) alerta) envolve o compromisso **sensibilidade × estabilidade**: limites sensíveis geram falsos alarmes; limites conservadores atrasam a detecção. E degradação detectada não é causa identificada: o fluxo correto é **detectar → diagnosticar → agir**.

### 9.3.3. Governança, Auditoria e Lineage

```text
governança = responsabilidade + rastreabilidade + controle
```

Para cada modelo deve ser possível identificar versão, finalidade, responsável, dados, aprovações e riscos conhecidos. O **lineage** permite reconstruir a origem e as transformações de dados e modelos, e uma **trilha de auditoria** registra cada intervenção.

A governança deve ser proporcional ao risco: um modelo que decide crédito exige validação independente, aprovação formal e monitoramento mais rigoroso que um recomendador de filmes. A norma **ISO/IEC 42001**² define um sistema de gestão de IA, e, havendo dados pessoais, inclusive em *logs* de predição, aplica-se a **LGPD**³.

### 9.3.4. Manutenção, Retreinamento e Ciclo de Vida

A manutenção deve ser orientada por diagnóstico:

```text
drift detectado ≠ retreinamento obrigatório
```

Se a causa for uma coluna corrompida, uma mudança de unidade ou uma quebra de pipeline, retreinar apenas incorpora o erro ao novo modelo. As intervenções possíveis incluem corrigir dados ou pipeline, recalibrar, retreinar, fazer *rollback*, substituir ou aposentar o modelo.

O retreinamento **periódico** é simples, mas pode desperdiçar recursos ou reagir tarde; o **orientado por eventos** é mais adaptativo, mas depende da qualidade dos gatilhos. Mesmo retreinado, o modelo não é promovido automaticamente: na estratégia **champion–challenger**, o candidato só substitui o modelo em produção se o superar segundo os critérios de aceitação.

## 9.4. Limitações, Trade-offs e Desafios Atuais

Há trade-offs entre frequência de monitoramento e custo, retreinamento frequente e estabilidade, governança rigorosa e agilidade. Monitorar muitas *features* gera excesso de alertas, que acabam ignorados. Automatizar demais também é arriscado: um retreinamento automático mal governado pode aprender com dados corrompidos e amplificar o problema.

## 9.5. Conclusão

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

Manter um modelo não é apenas mantê-lo executando, mas demonstrar que seus **dados, desempenho, finalidade, risco e histórico permanecem sob controle**.

## Referências

1. GAMA, J. et al. A survey on concept drift adaptation. **ACM Computing Surveys**, 2014.
2. ISO. **ISO/IEC 42001**: information technology: artificial intelligence: management system. ISO, 2023.
3. BRASIL. Lei nº 13.709, de 14 de agosto de 2018. Lei Geral de Proteção de Dados Pessoais (LGPD).
