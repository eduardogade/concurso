# Ponto 7 — MLOps: Desenvolvimento, Versionamento e Experimentação de Modelos

## 7.1. Introdução e Delimitação do Problema

O desenvolvimento de modelos de aprendizado de máquina possui natureza **iterativa, experimental e fortemente dependente de contexto**.

Um modelo treinado não resulta apenas do código que implementa o algoritmo, mas da combinação entre dados, configuração, hiperparâmetros, ambiente computacional e procedimento de treinamento [1]:

```text
modelo treinado ≠ código isolado
```

O desenvolvimento avança por ciclos sucessivos de formulação de hipóteses, preparação de dados, treinamento, avaliação e refinamento [2].

O objetivo de MLOps, neste contexto, é transformar uma experimentação *ad hoc* em um processo **controlado, rastreável, comparável e reproduzível** [3].

Implantação e operação em produção estão fora deste recorte: o ponto termina em um **modelo candidato validado**.

## 7.2. Fundamentos e Relevância

Cada execução relevante pode ser entendida como uma unidade experimental:

```text
experimento = entradas + procedimento + saídas + metadados
```

As entradas incluem dados, código, configuração e hiperparâmetros; o procedimento compreende transformações, treinamento e avaliação; e as saídas incluem modelos, métricas, previsões, logs e demais artefatos.

Uma melhoria de desempenho somente é interpretável quando se conhecem as condições responsáveis pelo resultado: uma métrica isolada não constitui evidência experimental suficiente. O princípio central é:

```text
resultado confiável = resultado + proveniência
```

## 7.3. Núcleo Técnico

### 7.3.1. Versionamento, Artefatos e Linhagem

Em MLOps, versionar somente o código é insuficiente. O estado experimental depende também de dados, configurações e hiperparâmetros, dependências e ambiente, modelos e *checkpoints* e artefatos intermediários.

Um **artefato** é um objeto produzido ou consumido ao longo do pipeline, como um conjunto de dados processado, modelo serializado, previsão, métrica ou transformação aprendida.

A **proveniência** identifica a origem de um artefato, enquanto a **linhagem** (*lineage*) representa as relações de transformação entre os componentes:

```text
dados brutos → dados processados → features → treinamento → modelo → métricas
```

Uma cadeia de proveniência permite responder quais dados, código e configuração originaram determinado modelo. Cada versão deve referir-se a um estado bem definido e imutável, identificado por hashes, commits ou IDs de execução.

### 7.3.2. Experiment Tracking e Rastreabilidade

O **experiment tracking** registra sistematicamente as condições e os resultados de cada execução:

- versões de dados e código;
- hiperparâmetros e configuração;
- *seed* e ambiente;
- métricas, logs e artefatos;
- estado e identificador da execução.

O *tracking* informa o que ocorreu; os artefatos representam o que foi produzido; e a linhagem descreve como entradas e saídas estão relacionadas. Juntos, constituem a **rastreabilidade experimental**, que conecta hipótese, configuração, execução, modelo, métrica e decisão.

A comparação entre experimentos exige protocolo compatível: conjuntos de teste, definição de métricas, pré-processamento e condições de avaliação devem ser equivalentes. **Baselines** fornecem referências explícitas contra as quais novos candidatos podem ser avaliados.

### 7.3.3. Reprodutibilidade

A reprodutibilidade depende do controle coordenado dos componentes que definem uma execução:

\[
\text{reprodutibilidade} \approx D + C + H + E + S
\]

em que \(D\) são os dados, \(C\) o código, \(H\) os hiperparâmetros e a configuração, \(E\) o ambiente e \(S\) o estado estocástico (*seed*).

O mesmo script não constitui o mesmo experimento se dados, dependências ou ambiente forem diferentes. Reprodutibilidade, contudo, não é determinismo absoluto:

```text
reprodutível ≠ idêntico bit a bit
```

Paralelismo, aceleradores e operações numéricas não determinísticas podem impedir identidade exata; o objetivo apropriado é obter condições metodologicamente reconstruíveis e resultados estatisticamente compatíveis.

### 7.3.4. Validação, Comparação e Seleção

Antes de selecionar um modelo, devem ser validados tanto os **dados** quanto o **modelo** [4].

A validação dos dados verifica esquema e tipos, valores ausentes, integridade, distribuição e consistência das *features*. A validação do modelo considera métricas principal e secundárias, estabilidade, robustez, custo computacional, latência, memória e restrições do domínio.

Logo, o melhor modelo não é o de maior métrica isolada: a seleção deve ocorrer sob critérios explícitos de aceitação e protocolo comparável.

```text
EXPERIMENTO
↓
VALIDAÇÃO DE DADOS E DO MODELO
↓
COMPARAÇÃO COM BASELINE
↓
CRITÉRIOS DE ACEITAÇÃO
↓
MODELO CANDIDATO
```

Um modelo candidato deve possuir identidade, proveniência, métricas e evidências de validação.

Um **registro de modelos** (*model registry*) organiza versões, metadados e estados desses candidatos, preparando-os para eventual promoção.

## 7.4. Limitações, Trade-offs e Desafios Atuais

Rastreabilidade e reprodutibilidade possuem custo: armazenamento de artefatos, manutenção de metadados, versionamento de dados e execução de validações.

O objetivo não é preservar tudo, mas informação suficiente para reconstrução, comparação e auditoria; rastreabilidade útil não é acumulação indiscriminada.

Outros desafios incluem dados mutáveis, dependências externas, não determinismo, proliferação de experimentos e artefatos, divergência entre ambientes e documentação incompleta.

A automação pode reduzir erro manual e aumentar a consistência de validação, rastreamento e registro. Entretanto:

```text
automatizar processo ruim ≠ criar processo bom
```

Existe também um trade-off entre rigor e velocidade: um processo pouco controlado pode parecer mais rápido por execução, mas gerar retrabalho, resultados irreproduzíveis e decisões pouco auditáveis.

## 7.5. Conclusão

Em síntese:

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

[1] Sculley, D. et al. NeurIPS. 2015.
[2] Amershi, S. et al. ICSE-SEIP. 2019.
[3] Kreuzberger, D. et al. IEEE Access. 2023.
[4] Breck, E. et al. IEEE BigData. 2017.
