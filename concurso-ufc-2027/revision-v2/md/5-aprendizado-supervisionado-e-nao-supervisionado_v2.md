# Ponto 5 — Aprendizado Supervisionado e Não Supervisionado

## 1. Introdução e Delimitação do Problema

O aprendizado de máquina pode ser organizado, em primeira aproximação, pela disponibilidade de uma variável-alvo durante o treinamento [1, 2]. No **aprendizado supervisionado**, cada observação é um par \((x_i,y_i)\), em que \(x_i\) representa os atributos de entrada e \(y_i\) o alvo conhecido; o objetivo é aprender uma função \(f:X\rightarrow Y\) capaz de generalizar para exemplos não vistos. No **aprendizado não supervisionado**, observam-se apenas os \(x_i\), sem rótulo-alvo explícito, e busca-se identificar estrutura nos próprios dados:

```text
supervisionado → aprender a relação X → Y
não supervisionado → aprender a estrutura em X
```

No primeiro caso predominam **classificação** e **regressão**; no segundo, agrupamento, redução de dimensionalidade, estimação de densidade e detecção de anomalias. Em ambos, aprender não significa apenas ajustar os dados disponíveis, mas construir representações úteis fora da amostra de treinamento.

## 2. Fundamentos e Relevância

No caso supervisionado, um modelo parametrizado \(f(x;\theta)\) produz uma previsão \(\hat{y}\), e o treinamento ajusta \(\theta\) minimizando uma função de perda:

\[
\theta^{*}=\arg\min_{\theta}L(\theta)
\]

A função de perda formaliza o que significa errar: erros absolutos ou quadráticos em regressão; entropia cruzada em classificação. O objetivo, porém, não é apenas reduzir o erro empírico, mas **generalizar para dados não vistos**. Por isso, os dados são tipicamente separados em:

```text
treino → ajustar parâmetros
validação → escolher modelo e hiperparâmetros
teste → estimar o desempenho final
```

A distinção entre **parâmetros**, aprendidos dos dados, e **hiperparâmetros**, escolhidos externamente, é fundamental para a seleção de modelos. Também é central o compromisso entre complexidade e generalização: modelos excessivamente simples sofrem **underfitting**, associado a alto viés; modelos excessivamente flexíveis, **overfitting**, associado a alta variância [3]. A regularização penaliza a complexidade:

\[
\text{objetivo}=\text{erro empírico}+\lambda\cdot\text{complexidade}
\]

pois baixo erro de treino não implica boa generalização.

## 3. Núcleo Técnico

### 3.1. Aprendizado Supervisionado

As duas tarefas fundamentais são a **classificação**, quando \(Y\) representa classes discretas, e a **regressão**, quando \(Y\) assume valores contínuos.

As famílias de métodos refletem diferentes hipóteses sobre a estrutura dos dados. Modelos lineares oferecem simplicidade e interpretabilidade; árvores de decisão representam relações não lineares por particionamento do espaço de atributos; *ensembles*, como **Random Forests** e *boosting*, combinam múltiplos modelos para aumentar robustez e desempenho; k-NN baseia-se em proximidade entre exemplos; SVM busca fronteiras de máxima margem; e redes neurais permitem representar relações altamente não lineares [4]. A escolha depende, portanto, da hipótese estrutural que o método impõe:

```text
método = algoritmo + hipótese sobre os dados
```

### 3.2. Aprendizado Não Supervisionado

Sem alvo conhecido durante o treinamento, o objetivo passa a ser caracterizar a estrutura dos dados. Entre os métodos mais representativos estão:

- **k-means**, que busca grupos compactos em torno de centroides;
- **clustering hierárquico**, que constrói agrupamentos em múltiplos níveis;
- **DBSCAN**, que identifica regiões densas e pode tratar pontos isolados como ruído;
- **PCA**, que reduz a dimensionalidade preservando direções de maior variância;
- **modelos de mistura**, que representam agrupamentos de forma probabilística.

A ausência de rótulos não significa ausência de critério: métodos não supervisionados também otimizam funções formais, como dispersão intra-cluster, densidade ou variância explicada.

### 3.3. Avaliação e Seleção de Modelos

A avaliação depende da tarefa e do custo dos erros. Em **classificação**, métricas comuns incluem acurácia, precisão, recall, F1-score e ROC-AUC. Em dados desbalanceados, acurácia alta não garante utilidade: um classificador que sempre prediz a classe majoritária pode ser inútil para detectar a classe de interesse. Em **regressão**, MAE, MSE, RMSE e \(R^2\) enfatizam propriedades distintas do erro.

No aprendizado não supervisionado, a avaliação é mais indireta: coesão intra-cluster, separação entre grupos, *silhouette*, estabilidade, conhecimento externo e utilidade em tarefas posteriores.

Quando a amostra é limitada, a **validação cruzada** ajuda a estimar a generalização. No esquema k-fold:

```text
dados → k partes → treina em k−1 → valida em 1 → repete k vezes
```

É essencial, entretanto, que o conjunto de teste permaneça independente de todas as escolhas de modelo.

## 4. Limitações, Trade-offs e Desafios Atuais

A escolha de um modelo envolve múltiplos trade-offs:

- desempenho × interpretabilidade;
- viés × variância;
- precisão × recall;
- custo computacional × ganho preditivo.

Há também riscos metodológicos. **Data leakage** ocorre quando informação que não deveria estar disponível entra indevidamente no treinamento, por exemplo quando normalização ou seleção de atributos utilizam dados de teste, tornando o desempenho aparente superior ao real. Além disso, bom desempenho em teste não garante desempenho fora da distribuição: mudanças nos dados, rótulos ruidosos, desbalanceamento, alta dimensionalidade e falta de representatividade podem comprometer a generalização.

Não existe, portanto, algoritmo universalmente superior. A escolha deve considerar:

```text
dados + objetivo + hipótese do modelo + métrica + restrições → método
```

Entre essas restrições estão tamanho da amostra, dimensionalidade, custo computacional, interpretabilidade, robustez, latência e custo dos diferentes tipos de erro.

## 5. Conclusão

Em síntese:

```text
PROBLEMA
↓
DADOS E RÓTULOS DISPONÍVEIS?
↓
FORMULAÇÃO SUPERVISIONADA / NÃO SUPERVISIONADA
↓
TREINAMENTO
↓
VALIDAÇÃO E SELEÇÃO
↓
AVALIAÇÃO
↓
GENERALIZAÇÃO
```

Aprendizado supervisionado e não supervisionado diferem principalmente pela disponibilidade de uma variável-alvo e pelo tipo de estrutura que se pretende aprender: no primeiro, generalizam-se relações entre entradas e alvos; no segundo, revela-se a estrutura latente dos dados. Em ambos, a qualidade do aprendizado depende da adequação entre problema, dados, hipótese do modelo, função de perda, métrica de avaliação e condições reais de uso.

## Referências

[1] BISHOP, C. M. *Pattern Recognition and Machine Learning*. 2006.
[2] MURPHY, K. P. *Machine Learning: A Probabilistic Perspective*. 2012.
[3] HASTIE, T.; TIBSHIRANI, R.; FRIEDMAN, J. *The Elements of Statistical Learning*. 2009.
[4] GOODFELLOW, I.; BENGIO, Y.; COURVILLE, A. *Deep Learning*. 2016.
