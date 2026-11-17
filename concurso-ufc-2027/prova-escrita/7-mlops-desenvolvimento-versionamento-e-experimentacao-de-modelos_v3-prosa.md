# Ponto 7 — MLOps: Desenvolvimento, Versionamento e Experimentação de Modelos

## 7.1. Introdução e Delimitação do Problema

O desenvolvimento de modelos de aprendizado de máquina é **iterativo, experimental e dependente de contexto**. Um modelo treinado não resulta apenas do código do algoritmo, mas da combinação entre dados, configuração, hiperparâmetros, ambiente computacional e procedimento de treinamento¹:

```text
modelo treinado ≠ código isolado
```

O trabalho avança em ciclos de hipótese, preparação de dados, treinamento, avaliação e refinamento². O objetivo de MLOps, neste recorte, é transformar essa experimentação *ad hoc* em um processo **controlado, rastreável, comparável e reproduzível**³. Implantação e operação ficam fora: o ponto termina em um **modelo candidato validado**.

## 7.2. Fundamentos e Relevância

Cada execução relevante é uma unidade experimental:

```text
experimento = entradas + procedimento + saídas + metadados
```

As entradas são dados, código, configuração e hiperparâmetros; o procedimento inclui transformações, treinamento e avaliação; as saídas são modelos, métricas e logs.

Uma melhoria só é interpretável quando se sabe o que a produziu: se a acurácia subiu, foi pelo novo algoritmo, por outros dados ou por uma semente aleatória favorável? Sem esse registro, a métrica isolada não é evidência. O princípio central é:

```text
resultado confiável = resultado + proveniência
```

## 7.3. Núcleo Técnico

### 7.3.1. Versionamento, Artefatos e Linhagem

Como o resultado não depende só do código, versioná-lo isoladamente é insuficiente. Um **artefato** é qualquer objeto produzido ou consumido no pipeline, como um conjunto de dados processado, um modelo serializado ou uma métrica.

A **proveniência** identifica a origem de um artefato; a **linhagem** (*lineage*) registra a cadeia de transformações entre eles:

```text
dados brutos → dados processados → features → treinamento → modelo → métricas
```

Com ela, responde-se quais dados, código e configuração produziram determinado modelo. Para isso, cada versão deve apontar para um estado imutável, identificado por *hash*, *commit* ou ID de execução. Na prática, o Git versiona o código; o DVC versiona dados e modelos grandes, guardando no Git apenas seus *hashes*; e o MLflow registra execuções e modelos.

### 7.3.2. Experiment Tracking e Rastreabilidade

O **experiment tracking** registra, para cada execução, versões de dados e código, hiperparâmetros, semente, ambiente, métricas e artefatos. Com versionamento e linhagem, esse registro forma a **rastreabilidade experimental**, que liga hipótese, execução, modelo, métrica e decisão.

Comparar experimentos exige protocolo equivalente: mesmos dados de teste, métricas e pré-processamento; do contrário, a diferença pode vir do protocolo, não do modelo. Um **baseline**, como o modelo atual ou um modelo simples, é a referência explícita que todo candidato deve superar.

### 7.3.3. Reprodutibilidade

A reprodutibilidade depende do controle conjunto dos componentes de uma execução:

\[
\text{resultado} = f(D, C, H, E, S)
\]

em que \(D\) são os dados, \(C\) o código, \(H\) os hiperparâmetros e a configuração, \(E\) o ambiente (bibliotecas, versões, hardware) e \(S\) a semente aleatória. O mesmo script não constitui o mesmo experimento se um desses elementos mudar; contêineres e arquivos de dependências fixam o ambiente, e a semente controla a aleatoriedade.

Reprodutível, porém, não significa idêntico bit a bit: paralelismo em GPUs e operações numéricas não determinísticas geram pequenas diferenças. O objetivo realista é reconstruir as condições do experimento e obter resultados estatisticamente compatíveis.

### 7.3.4. Validação, Comparação e Seleção

Antes da seleção, validam-se os **dados** (esquema, tipos, ausentes, distribuição) e o **modelo** (métricas, estabilidade, robustez, latência e restrições do domínio); o melhor modelo não é, portanto, o de maior métrica isolada.

A busca de hiperparâmetros, em grade, aleatória ou bayesiana, também é experimentação e deve ser registrada. Ela traz um risco sutil: quanto mais configurações se testam contra o mesmo conjunto de validação, maior a chance de escolher uma que acertou por acaso, superestimando o desempenho. Por isso, o conjunto de teste é usado uma única vez, ao final; o mesmo risco vale para *benchmarks* públicos reutilizados à exaustão.

Aprovado nos critérios de aceitação e comparado ao baseline, o experimento torna-se um **modelo candidato**, com identidade, proveniência, métricas e evidências de validação. Um **registro de modelos** (*model registry*) organiza essas versões e seus estados, preparando a eventual promoção.

## 7.4. Limitações, Trade-offs e Desafios Atuais

Rastreabilidade e reprodutibilidade têm custo: armazenar artefatos, manter metadados e versionar dados volumosos. O objetivo não é guardar tudo, mas o suficiente para reconstruir, comparar e auditar.

A automação reduz erros manuais e padroniza validação e registro, mas:

```text
automatizar processo ruim ≠ criar processo bom
```

Há ainda um trade-off entre rigor e velocidade: um processo pouco controlado parece mais rápido a cada execução, mas gera retrabalho, resultados irreproduzíveis e decisões difíceis de auditar.

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

Todo esse fluxo é atravessado por proveniência, linhagem e reprodutibilidade. O valor de um experimento não está apenas no modelo ou na métrica, mas na capacidade de demonstrar **quais condições produziram o resultado, como ele foi validado e como pode ser reconstruído**.

## Referências

1. SCULLEY, D. et al. Hidden technical debt in machine learning systems. In: NeurIPS, 2015.
2. AMERSHI, S. et al. Software engineering for machine learning: a case study. In: ICSE-SEIP, 2019.
3. KREUZBERGER, D.; KÜHL, N.; HIRSCHL, S. Machine learning operations (MLOps): overview, definition, and architecture. **IEEE Access**, 2023.
