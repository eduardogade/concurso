
# Ponto 7 — MLOps: Desenvolvimento, Versionamento e Experimentação de Modelos

## 7.1. Ciclo de Desenvolvimento e Natureza Experimental do ML

O desenvolvimento de modelos de aprendizado de máquina possui natureza **iterativa e experimental**. Um modelo treinado não resulta apenas do código, mas da combinação entre dados, configuração, hiperparâmetros, ambiente computacional e procedimento de treinamento. Assim:

\[
\text{modelo treinado}
\neq
\text{código isolado}
\]

O ciclo de desenvolvimento envolve formulação de hipóteses, preparação de dados, treinamento, avaliação, análise e refinamento sucessivo. Cada execução pode ser entendida como um experimento composto por entradas, procedimento e saídas:

\[
\text{experimento}
=
\text{entradas}
+
\text{procedimento}
+
\text{saídas}
\]

As entradas incluem, por exemplo, dados, código e configuração; as saídas incluem modelos, métricas, previsões, logs e demais artefatos. Consequentemente, uma métrica isolada não constitui evidência suficiente: seu significado depende das condições em que foi produzida.

O papel de MLOps é transformar experimentação ad hoc em um processo **controlado, rastreável, comparável e reproduzível**, permitindo identificar quais mudanças produziram determinados resultados e preservar o conhecimento experimental necessário para desenvolvimento e seleção de modelos.

---

> Mnemonics



---

## 7.2. Versionamento, Artefatos e Proveniência

Em MLOps, versionar apenas o código é insuficiente, pois um modelo depende também dos dados, da configuração, dos hiperparâmetros, do ambiente de execução e dos artefatos produzidos. Assim:

\[
\text{versão do modelo}
\neq
\text{arquivo de pesos isolado}
\]

A rastreabilidade exige que esses componentes sejam identificados e relacionados entre si. **Artefatos** incluem modelos, *checkpoints*, métricas, previsões, logs, dados processados e demais produtos intermediários ou finais do pipeline.

A **proveniência** descreve a origem de um artefato, enquanto **lineage** representa as relações de transformação entre dados, código, experimentos, modelos e resultados. Conceitualmente:

\[
\text{dados}
+
\text{código}
+
\text{configuração}
+
\text{ambiente}
\rightarrow
\text{experimento}
\rightarrow
\text{modelo}
\]

Uma versão útil deve referir-se a um estado bem definido e, preferencialmente, imutável, permitindo reconstruir quais condições produziram determinado resultado. Dessa forma, o versionamento em MLOps é mais amplo que o controle de código: ele estabelece a base para **rastreabilidade, auditoria e reprodutibilidade** do ciclo experimental.

---

> Mnemonics

---

## 7.3. Experimentação, Rastreabilidade e Registro de Experimentos

A experimentação em MLOps deve ser registrada de forma sistemática para que cada execução possa ser identificada, comparada e reproduzida. Um experimento pode ser representado como:

\[
\text{experimento}
=
\text{entradas}
+
\text{procedimento}
+
\text{saídas}
+
\text{metadados}
\]

O **experiment tracking** registra informações como versões de dados e código, hiperparâmetros, ambiente, *seed*, métricas, logs e artefatos. Já a **rastreabilidade** permite reconstruir a cadeia que conecta hipótese, configuração, execução, modelo, métrica e decisão.

A comparação entre experimentos exige protocolo compatível; portanto:

\[
\text{métrica isolada}
\neq
\text{evidência experimental suficiente}
\]

Além disso, baselines fornecem referências explícitas para avaliar novos candidatos. O registro persistente das execuções permite recuperar resultados anteriores, comparar configurações e justificar a seleção de modelos.

Conceitualmente:

\[
\text{tracking}
+
\text{artefatos}
+
\text{lineage}
=
\text{rastreabilidade experimental}
\]

Essa rastreabilidade constitui a base para reprodutibilidade, auditoria e seleção confiável de modelos.

---

> Mnemonics

---

## 7.4. Reprodutibilidade, Validação e Seleção de Modelos

A **reprodutibilidade** em MLOps depende do controle coordenado dos elementos que definem o experimento. Como signpost:

\[
\text{reprodutibilidade}
\approx
D + C + H + E + S
\]

onde \(D\) representa dados, \(C\) código, \(H\) hiperparâmetros e configuração, \(E\) ambiente e \(S\) o estado estocástico. Executar novamente o mesmo script não garante o mesmo experimento, pois alterações nesses componentes podem modificar o resultado.

Além disso, reprodutibilidade não implica necessariamente determinismo absoluto:

\[
\text{reprodutível}
\neq
\text{idêntico bit a bit}
\]

A validação deve abranger tanto os dados quanto o modelo. Dados podem ser verificados quanto a esquema, integridade e distribuição; modelos devem ser avaliados por métricas, estabilidade, custo, latência, robustez e demais restrições relevantes.

A seleção deve ocorrer sob protocolo comparável e critérios explícitos. Assim:

\[
\text{melhor modelo}
\neq
\text{maior métrica isolada}
\]

O candidato selecionado deve possuir identidade, proveniência, métricas e evidências de validação. Registros de modelos permitem organizar versões, estados e metadados, preparando o candidato para posterior promoção e implantação.

---

> Mnemonics

---

## 7.5. Limitações, Trade-offs, Automação e Fronteira com Operação

As práticas de desenvolvimento e experimentação em MLOps introduzem ganhos de rastreabilidade, reprodutibilidade e auditabilidade, mas também possuem custos. O aumento do controle experimental exige armazenamento de artefatos, registro de metadados, versionamento de dados e manutenção de mecanismos de rastreamento. Assim:

\[
\text{mais controle}
\rightarrow
\text{mais reprodutibilidade}
\rightarrow
\text{mais custo operacional}
\]

A reprodutibilidade também pode ser limitada por paralelismo, hardware, dependências externas e fontes de dados mutáveis. Por isso:

\[
\text{reprodutível}
\neq
\text{necessariamente idêntico bit a bit}
\]

Em muitos contextos, busca-se reconstrução metodológica e resultados estatisticamente compatíveis.

A automação pode ampliar consistência em validação, tracking e seleção, mas:

\[
\text{automatizar processo ruim}
\neq
\text{criar processo bom}
\]

O objetivo do Ponto 7 é controlar o ciclo de construção e experimentação até a produção de um modelo candidato validado e rastreável. A fronteira conceitual é:

\[
7=\text{construir e experimentar}
\]

\[
8=\text{entregar e operar}
\]

\[
9=\text{observar, governar e manter}
\]

Assim, MLOps deve equilibrar rigor experimental, velocidade, custo e complexidade para produzir modelos cuja origem, validação e estado possam ser explicados e reconstruídos.

---

> Mnemonics

---

## Texto Final

# Ponto 7 — MLOps: Desenvolvimento, Versionamento e Experimentação de Modelos

## 1. Introdução e Delimitação do Problema

O desenvolvimento de modelos de aprendizado de máquina possui natureza **iterativa, experimental e fortemente dependente de contexto**. Um modelo treinado não resulta apenas do código que implementa o algoritmo, mas da combinação entre dados, configuração, hiperparâmetros, ambiente computacional e procedimento de treinamento.

Assim:

\[
\text{modelo treinado}
\neq
\text{código isolado}
\]

O ciclo de desenvolvimento envolve sucessivos ciclos de formulação de hipóteses, preparação de dados, treinamento, avaliação e refinamento:

```text
HIPÓTESE
   ↓
DADOS
   ↓
TREINAMENTO
   ↓
AVALIAÇÃO
   ↓
ANÁLISE
   ↓
NOVA HIPÓTESE
   ↺
```

O objetivo de MLOps, neste contexto, é transformar uma experimentação ad hoc em um processo **controlado, rastreável, comparável e reproduzível**, preservando informação suficiente para compreender como cada resultado foi produzido e justificar a seleção de modelos.

## 2. Fundamentos e Relevância

Cada execução relevante pode ser entendida como uma unidade experimental:

\[
\text{experimento}
=
\text{entradas}
+
\text{procedimento}
+
\text{saídas}
+
\text{metadados}
\]

As entradas incluem dados, código, configuração e hiperparâmetros; o procedimento compreende transformações, treinamento e avaliação; e as saídas incluem modelos, métricas, previsões, logs e demais artefatos.

Consequentemente:

\[
\text{métrica isolada}
\neq
\text{evidência experimental suficiente}
\]

Uma melhoria de desempenho somente é interpretável quando se conhecem as condições responsáveis pelo resultado.

Essa característica distingue o desenvolvimento de ML de um processo centrado exclusivamente no código. Para reconstruir um experimento, é necessário controlar conjuntamente seus diferentes componentes:

\[
\text{dados}
+
\text{código}
+
\text{configuração}
+
\text{ambiente}
\rightarrow
\text{experimento}
\rightarrow
\text{modelo}
\]

O princípio central do Ponto 7 pode, portanto, ser resumido como:

\[
\text{resultado confiável}
=
\text{resultado}
+
\text{proveniência}
\]

## 3. Núcleo Técnico

### 3.1. Versionamento, Artefatos e Linhagem

Em MLOps, versionar somente o código é insuficiente. O estado experimental depende também de:

- dados;
- configurações e hiperparâmetros;
- dependências e ambiente;
- modelos e *checkpoints*;
- artefatos intermediários e finais.

Assim:

\[
\text{versão do modelo}
\neq
\text{arquivo de pesos isolado}
\]

Um **artefato** é um objeto produzido ou consumido ao longo do pipeline, como um conjunto de dados processado, modelo serializado, *checkpoint*, previsão, log, métrica ou transformação aprendida.

A **proveniência** identifica a origem de um artefato, enquanto a **linhagem** (*lineage*) representa as relações de transformação entre os componentes:

```text
dados brutos
    ↓
dados processados
    ↓
features
    ↓
treinamento
    ↓
modelo
    ↓
predições e métricas
```

Uma cadeia de proveniência permite responder, por exemplo, quais dados, código e configuração originaram determinado modelo.

Uma versão útil deve, preferencialmente, referir-se a um estado bem definido e imutável. Identificadores, hashes, commits ou IDs de execução podem ser utilizados para estabelecer essa identidade.

Portanto:

\[
\text{versionamento em MLOps}
>
\text{versionamento de código}
\]

### 3.2. Experiment Tracking e Rastreabilidade

O **experiment tracking** registra sistematicamente as condições e os resultados de cada execução.

Entre os elementos rastreados estão:

- versões de dados e código;
- hiperparâmetros e configuração;
- *seed*;
- ambiente;
- métricas;
- logs;
- artefatos;
- estado e identificador da execução.

A rastreabilidade conecta esses elementos:

```text
hipótese
   ↓
configuração
   ↓
execução
   ↓
modelo
   ↓
métrica
   ↓
decisão
```

Nesse contexto, três conceitos se complementam:

\[
\text{tracking}
+
\text{artefatos}
+
\text{lineage}
=
\text{rastreabilidade experimental}
\]

O *tracking* informa o que ocorreu; os artefatos representam o que foi produzido; e a linhagem descreve como entradas e saídas estão relacionadas.

A comparação entre experimentos também exige protocolo compatível. Um valor numérico maior não implica automaticamente um experimento superior:

\[
\text{maior métrica observada}
\neq
\text{melhor evidência experimental}
\]

Conjuntos de teste, definição de métricas, pré-processamento e condições de avaliação devem ser compatíveis. **Baselines** fornecem referências explícitas contra as quais novos candidatos podem ser avaliados.

### 3.3. Reprodutibilidade

A reprodutibilidade depende do controle coordenado dos componentes que definem uma execução. Como signpost:

\[
\text{reprodutibilidade}
\approx
D + C + H + E + S
\]

em que:

- \(D\) = dados;
- \(C\) = código;
- \(H\) = hiperparâmetros e configuração;
- \(E\) = ambiente;
- \(S\) = estado estocástico ou *seed*.

Logo:

\[
\text{mesmo script}
\neq
\text{mesmo experimento}
\]

se dados, dependências, configuração ou ambiente forem diferentes.

Também é importante distinguir reprodutibilidade de determinismo absoluto:

\[
\text{reprodutível}
\neq
\text{necessariamente idêntico bit a bit}
\]

Paralelismo, aceleradores e operações numéricas não determinísticas podem impedir identidade exata. Em muitos sistemas, o objetivo apropriado é obter condições metodologicamente reconstruíveis e resultados estatisticamente compatíveis.

### 3.4. Validação, Comparação e Seleção

Antes de selecionar um modelo, deve-se validar tanto os **dados** quanto o **modelo**.

A validação dos dados pode verificar:

- esquema e tipos;
- valores ausentes;
- integridade;
- distribuição;
- consistência das *features*.

A validação do modelo pode envolver:

- métrica principal e métricas secundárias;
- estabilidade;
- robustez;
- custo computacional;
- latência;
- memória;
- restrições específicas do domínio.

Assim:

\[
\text{melhor modelo}
\neq
\text{maior métrica isolada}
\]

A seleção deve ocorrer sob critérios explícitos de aceitação e protocolo comparável.

Conceitualmente:

```text
EXPERIMENTO
    ↓
VALIDAÇÃO DE DADOS
    ↓
VALIDAÇÃO DO MODELO
    ↓
COMPARAÇÃO COM BASELINE
    ↓
CRITÉRIOS DE ACEITAÇÃO
    ↓
MODELO CANDIDATO
```

Um modelo candidato deve possuir identidade, proveniência, métricas e evidências de validação.

Um **registro de modelos** (*model registry*) organiza versões, metadados e estados desses candidatos, preparando-os para eventual promoção e implantação.

## 4. Limitações, Trade-offs e Desafios Atuais

Rastreabilidade e reprodutibilidade possuem custo.

\[
\text{mais controle}
\rightarrow
\text{mais reprodutibilidade}
\rightarrow
\text{mais custo operacional}
\]

Esse custo envolve armazenamento de artefatos, manutenção de metadados, versionamento de dados, execução de validações e administração do histórico experimental.

Por isso:

\[
\text{rastreabilidade útil}
\neq
\text{acumulação indiscriminada}
\]

O objetivo não é preservar tudo, mas preservar informação suficiente para reconstrução, comparação e auditoria.

Outros desafios incluem:

- dados mutáveis;
- dependências externas;
- não determinismo;
- proliferação de experimentos e artefatos;
- custo de armazenamento;
- divergência entre ambientes;
- documentação incompleta.

A automação pode reduzir erro manual e aumentar consistência em validação, rastreamento e registro. Entretanto:

\[
\text{automatizar processo ruim}
\neq
\text{criar processo bom}
\]

Existe também um trade-off entre rigor e velocidade:

\[
\text{velocidade local}
\neq
\text{eficiência do ciclo completo}
\]

Um processo pouco controlado pode parecer mais rápido por execução, mas gerar retrabalho, resultados irreproduzíveis e decisões pouco auditáveis.

Finalmente, a fronteira conceitual entre os três pontos de MLOps deve permanecer clara:

\[
7=\text{construir e experimentar}
\]

\[
8=\text{entregar e operar}
\]

\[
9=\text{observar, governar e manter}
\]

O Ponto 7 termina, portanto, quando existe um **modelo candidato validado, versionado, rastreável e reproduzível**; implantação e operação pertencem ao Ponto 8.

## 5. Conclusão

MLOps transforma o desenvolvimento experimental de modelos em um processo no qual resultados podem ser comparados, explicados e reconstruídos.

A síntese do Ponto 7 é:

```text
HIPÓTESE
   ↓
EXPERIMENTO
   ↓
VERSIONAMENTO
   ↓
TRACKING
   ↓
VALIDAÇÃO
   ↓
MODELO CANDIDATO
```

Todo esse fluxo é atravessado por:

```text
PROVENIÊNCIA + LINEAGE + REPRODUTIBILIDADE
```

Assim, o valor de um experimento não reside apenas no modelo ou na métrica produzida, mas na capacidade de demonstrar **quais condições produziram o resultado, como ele foi validado e como pode ser reconstruído**.

## Referências

- SCULLEY, D. et al. *Hidden Technical Debt in Machine Learning Systems*. 2015.
- BRECK, E. et al. *The ML Test Score: A Rubric for ML Production Readiness and Technical Debt Reduction*. 2017.
- AMERSHI, S. et al. *Software Engineering for Machine Learning: A Case Study*. 2019.
- KREUZBERGER, D.; KÜHL, N.; HIRSCHL, S. *Machine Learning Operations (MLOps): Overview, Definition, and Architecture*. 2023.

---

## Outras Notas

