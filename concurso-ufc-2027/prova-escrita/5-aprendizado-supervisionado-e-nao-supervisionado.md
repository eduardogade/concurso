
# Ponto 5 — Aprendizado Supervisionado vs. Não Supervisionado

## 5.1. Formulação do problema: supervisionado vs. não supervisionado

O aprendizado de máquina pode ser classificado, em primeira aproximação, conforme a disponibilidade de uma variável-alvo durante o treinamento. No **aprendizado supervisionado**, cada observação é apresentada como um par `(x_i, y_i)`, no qual `x_i` representa os atributos de entrada e `y_i` o alvo conhecido. O objetivo é aprender uma função `f: X → Y` capaz de generalizar para exemplos não vistos. As tarefas clássicas são **classificação**, quando o alvo é discreto, e **regressão**, quando o alvo é contínuo.

No **aprendizado não supervisionado**, observam-se apenas os `x_i`, sem rótulo-alvo explícito. O objetivo passa a ser identificar estrutura nos dados, por exemplo por agrupamentos, redução de dimensionalidade, estimação de densidade ou detecção de anomalias. Assim:

```text
supervisionado → aprender relação X → Y
não supervisionado → aprender estrutura em X
```

A ausência de rótulos não implica ausência de objetivo: métodos não supervisionados também otimizam critérios formais. A principal diferença está, portanto, na natureza da informação disponível e no tipo de problema que se deseja resolver.

---

> Mnemonics



---

## 5.2. Treinamento, função de perda e generalização

O treinamento consiste em ajustar os parâmetros `θ` de um modelo `f(x; θ)` de modo a minimizar uma função de perda que quantifica a discrepância entre a previsão `ŷ` e o alvo observado `y`:

```text
θ* = arg min_θ L(θ)
```

Entretanto, o objetivo do aprendizado não é minimizar apenas o erro de treinamento, mas **generalizar para dados não vistos**. Por isso, os dados são tipicamente separados em conjuntos de treino, validação e teste: o primeiro ajusta parâmetros, o segundo auxilia na escolha de modelos e hiperparâmetros, e o último estima o desempenho final.

Um modelo excessivamente simples pode apresentar **underfitting**, enquanto um modelo excessivamente flexível pode sofrer **overfitting**, ajustando inclusive ruído e particularidades da amostra. Técnicas de regularização e seleção de modelos procuram equilibrar ajuste e complexidade:

```text
erro empírico + λ · complexidade
```

Assim, baixo erro de treinamento não implica boa generalização; o desempenho relevante é aquele mantido em exemplos novos.

---

> Mnemonics

---

## 5.3. Classes principais de métodos

As principais famílias de métodos refletem diferentes hipóteses sobre a estrutura dos dados. No aprendizado supervisionado, modelos lineares oferecem simplicidade e interpretabilidade; árvores de decisão representam relações não lineares por particionamento do espaço de atributos; ensembles, como Random Forests e métodos de boosting, combinam múltiplos modelos para melhorar robustez e desempenho; k-NN utiliza proximidade entre exemplos; SVM busca fronteiras de máxima margem; e redes neurais permitem modelar relações altamente não lineares.

No aprendizado não supervisionado, k-means busca grupos compactos em torno de centróides, enquanto métodos hierárquicos constroem estruturas de agrupamento em múltiplos níveis. DBSCAN identifica regiões densas e pode separar ruído. PCA realiza redução linear de dimensionalidade preservando direções de maior variância, enquanto modelos de mistura representam grupos de forma probabilística.

Mais importante que a escolha nominal do algoritmo é reconhecer que:

```text
método = algoritmo + hipótese sobre os dados
```

Logo, não existe um método universalmente superior; sua adequação depende da tarefa, da geometria dos dados, da dimensionalidade, da quantidade de exemplos, do custo computacional e da necessidade de interpretabilidade.

---

> Mnemonics

---

## 5.4. Avaliação, escolha de modelos, limitações e síntese

A avaliação de modelos depende da tarefa e do custo dos erros. Em classificação, métricas como acurácia, precisão, recall, F1 e ROC-AUC capturam diferentes aspectos do desempenho; em dados desbalanceados, **acurácia alta não implica modelo útil**. Em regressão, são comuns MAE, MSE, RMSE e \(R^2\), cada qual enfatizando propriedades distintas do erro.

No aprendizado não supervisionado, a avaliação é mais indireta pela ausência de um alvo verdadeiro, podendo considerar coesão, separação, silhouette, estabilidade e relevância no domínio. Técnicas como validação cruzada ajudam a estimar generalização, desde que o conjunto de teste permaneça independente e se evite **data leakage**.

A escolha do modelo deve considerar não apenas desempenho preditivo, mas também dimensionalidade, tamanho da amostra, custo computacional, interpretabilidade, robustez e custo dos erros. Assim:

```text
dados + objetivo + hipótese do modelo + métrica
→ escolha do método
```

Não existe algoritmo universalmente superior; existe método mais adequado ao problema e às restrições.

---

> Mnemonics

---

## Texto Final

# Ponto 5 — Aprendizado Supervisionado e Não Supervisionado

## 1. Introdução e Delimitação do Problema

O aprendizado de máquina pode ser organizado, em primeira aproximação, pela disponibilidade de uma variável-alvo durante o treinamento. No **aprendizado supervisionado**, cada observação é apresentada como um par `(x_i, y_i)`, em que `x_i` representa os atributos de entrada e `y_i` o alvo conhecido; o objetivo é aprender uma função capaz de generalizar para exemplos não vistos. No **aprendizado não supervisionado**, observam-se apenas os `x_i`, sem rótulo-alvo explícito, e busca-se identificar estrutura nos próprios dados.

A distinção central pode ser resumida por:

```text
supervisionado → aprender relação X → Y
não supervisionado → aprender estrutura em X
```

No primeiro caso, predominam tarefas como **classificação** e **regressão**; no segundo, agrupamento, redução de dimensionalidade, estimação de densidade e detecção de anomalias. Em ambos, entretanto, aprender não significa apenas ajustar os dados disponíveis, mas construir representações que sejam úteis fora da amostra de treinamento.

## 2. Fundamentos e Relevância

No aprendizado supervisionado, considera-se um modelo parametrizado `f(x; θ)`, que produz uma previsão `ŷ`. O treinamento ajusta os parâmetros `θ` minimizando uma função de perda `L(θ)`:

```text
θ* = arg min_θ L(θ)
```

A função de perda formaliza o que significa errar. Em regressão, podem ser empregados erros absolutos ou quadráticos; em classificação, funções como entropia cruzada são comuns.

O objetivo, porém, não é apenas reduzir o erro empírico, mas **generalizar para dados não vistos**. Por isso, os dados são tipicamente separados em:

```text
treino → ajustar parâmetros
validação → escolher modelo e hiperparâmetros
teste → estimar desempenho final
```

A distinção entre **parâmetros**, aprendidos diretamente dos dados, e **hiperparâmetros**, escolhidos externamente, é fundamental para seleção de modelos.

Também é central o compromisso entre complexidade e generalização. Modelos excessivamente simples podem sofrer **underfitting**, enquanto modelos excessivamente flexíveis podem sofrer **overfitting**. Técnicas de regularização introduzem penalização à complexidade:

```text
objetivo = erro empírico + λ · complexidade
```

Assim:

```text
baixo erro de treino ≠ boa generalização
```

Em termos clássicos, underfitting associa-se a alto viés, enquanto overfitting associa-se a alta variância.

## 3. Núcleo Técnico

### 3.1. Aprendizado Supervisionado

No aprendizado supervisionado, os exemplos possuem entrada e alvo:

```text
(x_i, y_i)
```

e busca-se aprender:

```text
f: X → Y
```

As duas tarefas fundamentais são:

- **classificação**, quando `Y` representa classes discretas;
- **regressão**, quando `Y` assume valores contínuos.

As principais famílias de métodos refletem diferentes hipóteses sobre a estrutura dos dados. Modelos lineares oferecem simplicidade e interpretabilidade; árvores de decisão representam relações não lineares por particionamento do espaço de atributos; ensembles, como **Random Forests** e métodos de boosting, combinam múltiplos modelos para aumentar robustez e desempenho; k-NN baseia-se em proximidade entre exemplos; SVM busca fronteiras de máxima margem; e redes neurais permitem representar relações altamente não lineares.

A escolha do método depende, portanto, não apenas do algoritmo, mas também da hipótese estrutural que ele impõe:

```text
método = algoritmo + hipótese sobre os dados
```

### 3.2. Aprendizado Não Supervisionado

No aprendizado não supervisionado, não existe um alvo `y_i` conhecido durante o treinamento. O objetivo passa a ser caracterizar a estrutura dos dados disponíveis.

Entre os métodos mais representativos estão:

- **k-means**, que busca grupos compactos em torno de centróides;
- **clustering hierárquico**, que constrói agrupamentos em múltiplos níveis;
- **DBSCAN**, que identifica regiões densas e pode tratar pontos isolados como ruído;
- **PCA**, que reduz dimensionalidade preservando direções de maior variância;
- **modelos de mistura**, que representam agrupamentos de forma probabilística.

A ausência de rótulos não significa ausência de objetivo:

```text
sem rótulo ≠ sem critério
```

Métodos não supervisionados também otimizam funções formais, por exemplo dispersão intra-cluster, densidade ou variância explicada.

### 3.3. Avaliação e Seleção de Modelos

A avaliação depende da tarefa e do custo dos erros.

Em **classificação**, métricas comuns incluem:

- acurácia;
- precisão;
- recall;
- F1-score;
- ROC-AUC.

Em dados desbalanceados:

```text
acurácia alta ≠ modelo útil
```

Um classificador que sempre prediz a classe majoritária pode apresentar alta acurácia e ainda ser inútil para detectar a classe de interesse.

Em **regressão**, métricas como MAE, MSE, RMSE e `R²` enfatizam propriedades distintas do erro.

No aprendizado não supervisionado, a avaliação é mais indireta, pois não há alvo verdadeiro disponível. Pode envolver:

- coesão intra-cluster;
- separação entre grupos;
- silhouette;
- estabilidade;
- conhecimento externo;
- utilidade em tarefas posteriores.

Quando a amostra é limitada, técnicas como **validação cruzada** ajudam a estimar generalização. No esquema k-fold:

```text
dados → k partes → treina em k−1 → valida em 1 → repete
```

É essencial, entretanto, que o conjunto de teste permaneça independente.

## 4. Limitações, Trade-offs e Desafios Atuais

A escolha de um modelo envolve múltiplos trade-offs. Entre os mais importantes estão:

- desempenho × interpretabilidade;
- viés × variância;
- precisão × recall;
- custo computacional × ganho preditivo.

Também há riscos metodológicos importantes. **Data leakage** ocorre quando informação que não deveria estar disponível durante o treinamento entra indevidamente no processo, por exemplo quando normalização ou seleção de atributos utilizam também dados de teste:

```text
leakage → desempenho aparente > desempenho real
```

Além disso, desempenho em teste não garante desempenho no mundo real:

```text
bom teste ≠ garantia fora da distribuição
```

Mudanças na distribuição dos dados, rótulos ruidosos, desbalanceamento, alta dimensionalidade e falta de representatividade podem comprometer a generalização.

Não existe, portanto, um algoritmo universalmente superior. A escolha deve considerar:

```text
dados + objetivo + hipótese do modelo + métrica + restrições
→ escolha do método
```

Entre essas restrições estão tamanho da amostra, dimensionalidade, custo computacional, interpretabilidade, robustez, latência e custo dos diferentes tipos de erro.

## 5. Conclusão

Aprendizado supervisionado e não supervisionado diferem principalmente pela disponibilidade de uma variável-alvo e pelo tipo de estrutura que se pretende aprender. No supervisionado, busca-se generalizar relações entre entradas e alvos; no não supervisionado, revelar estrutura latente nos próprios dados.

A síntese do processo pode ser expressa por:

```text
problema
  ↓
dados e rótulos disponíveis?
  ↓
formulação supervisionada / não supervisionada
  ↓
treinamento
  ↓
validação e seleção
  ↓
avaliação
  ↓
generalização
```

A qualidade do aprendizado depende, portanto, não apenas do algoritmo escolhido, mas da adequação entre problema, dados, hipótese do modelo, função de perda, métrica de avaliação e condições reais de uso.

## Referências

- BISHOP, C. M. *Pattern Recognition and Machine Learning*. 2006.
- HASTIE, T.; TIBSHIRANI, R.; FRIEDMAN, J. *The Elements of Statistical Learning*. 2009.
- MURPHY, K. P. *Machine Learning: A Probabilistic Perspective*. 2012.
- GOODFELLOW, I.; BENGIO, Y.; COURVILLE, A. *Deep Learning*. 2016.

---

## Outras Notas

