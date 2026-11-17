# Ponto 5 — Aprendizado Supervisionado e Não Supervisionado

## 5.1. Introdução e Delimitação do Problema

O aprendizado de máquina pode ser organizado, em primeira aproximação, pela disponibilidade de uma variável-alvo durante o treinamento¹.

No **aprendizado supervisionado**, cada exemplo é um par \((x_{i},y_{i})\), com atributos \(x_{i}\) e alvo conhecido \(y_{i}\), e busca-se uma função \(f:X \rightarrow Y\) que generalize para exemplos novos. No **não supervisionado**, observam-se apenas os \(x_{i}\), e busca-se estrutura nos próprios dados.

No primeiro caso predominam **classificação** (alvo discreto) e **regressão** (alvo contínuo); no segundo, agrupamento, redução de dimensionalidade e detecção de anomalias.

## 5.2. Fundamentos e Relevância

No caso supervisionado, um modelo \(f(x;\theta)\) faz previsões \(\hat{y}\), e uma **função de perda** \(\ell\) mede o erro de cada uma: erro quadrático na regressão, entropia cruzada na classificação. O treinamento minimiza a perda média na amostra, o **risco empírico**:

\[
\theta^{*} = \arg\min_{\theta}\frac{1}{n}\sum_{i = 1}^{n}\ell(f(x_{i};\theta),y_{i})
\]

O objetivo real, porém, é errar pouco em dados novos. Por isso, os dados são separados em:

```text
treino → ajustar parâmetros
validação → escolher modelo e hiperparâmetros
teste → estimar o desempenho final
```

**Parâmetros** são aprendidos dos dados; **hiperparâmetros**, como a profundidade de uma árvore ou o peso \(\lambda\) da regularização, são escolhidos na validação.

Modelos simples demais não captam o padrão (**underfitting**, alto viés); modelos flexíveis demais aprendem também o ruído (**overfitting**, alta variância)². A **regularização** controla esse compromisso:

\[
\text{objetivo} = \text{erro empírico} + \lambda \cdot \text{complexidade}
\]

Na **L2** (*ridge*), a complexidade é a soma dos quadrados dos pesos, que os encolhe; na **L1** (*lasso*), a soma de seus valores absolutos, que zera parte deles e seleciona atributos.

## 5.3. Núcleo Técnico

### 5.3.1. Aprendizado Supervisionado

Os métodos supervisionados diferem pela hipótese que fazem sobre os dados:

- **regressão linear e logística**: estimam pesos de uma combinação linear dos atributos, que a logística converte em probabilidade de classe; são simples e interpretáveis, mas lineares;
- **árvores de decisão**: dividem os dados, sucessivamente, pelo atributo que mais reduz a impureza das classes (Gini ou entropia); geram regras legíveis, mas sobreajustam se crescem demais;
- ***ensembles***: no *bagging*, base da **Random Forest**, muitas árvores, treinadas em amostras *bootstrap* e com atributos sorteados, votam, o que reduz sobretudo a variância; no *boosting*, modelos simples são treinados em sequência, cada um corrigindo os erros dos anteriores, o que reduz sobretudo o viés;
- **SVM**: busca a fronteira de **margem máxima** entre as classes, definida pelos vetores de suporte; com *kernels*, separa dados não lineares;
- **redes neurais**: compõem camadas de transformações não lineares, com pesos ajustados por gradiente descendente e derivadas calculadas por **retropropagação**³.

### 5.3.2. Aprendizado Não Supervisionado

Sem alvo, o objetivo passa a ser caracterizar a estrutura dos dados:

- **k-means**: alterna dois passos, atribuir cada ponto ao centroide mais próximo e recalcular cada centroide como a média de seu grupo, reduzindo a soma das distâncias quadráticas; exige fixar k, depende da inicialização (mitigada pelo k-means++) e favorece grupos esféricos;
- **clustering hierárquico**: une progressivamente os grupos mais próximos, formando um dendrograma;
- **DBSCAN**: forma grupos a partir de regiões densas, de formato arbitrário, e trata pontos isolados como ruído;
- **PCA**: projeta os dados nas direções de maior variância, reduzindo a dimensionalidade.

### 5.3.3. Avaliação e Seleção de Modelos

Em classificação, usam-se acurácia, precisão, recall, F1 e ROC-AUC. Com classes desbalanceadas, a acurácia engana: se 1% das transações são fraudes, prever sempre "não fraude" acerta 99% e é inútil. Em regressão, usam-se MAE, RMSE e \(R^{2}\). Sem rótulos, a avaliação é indireta: coesão e separação dos grupos (silhueta), estabilidade e utilidade posterior.

Com poucos dados, a **validação cruzada** estima melhor a generalização:

```text
dados → k partes → treina em k−1 → valida em 1 → repete k vezes
```

O teste permanece intocado até o fim.

## 5.4. Limitações, Trade-offs e Desafios Atuais

O **data leakage**, quando informação indisponível no uso real entra no treinamento (por exemplo, normalizar usando os dados de teste), infla o desempenho aparente. E bom desempenho no teste não garante desempenho fora da distribuição de treino.

O **aprendizado profundo** amplia a capacidade de representação, aprendendo atributos diretamente de dados brutos, como imagens e texto. Em troca, aumenta a dependência de dados e de computação, o risco de superajuste e a dificuldade de reproduzir experimentos, e exige monitorar o modelo após a implantação: aqui os fundamentos do aprendizado encontram a engenharia de **MLOps**.

Não existe, portanto, algoritmo universalmente superior: a escolha depende dos dados, do objetivo, da métrica e de restrições como interpretabilidade e custo dos erros.

## 5.5. Conclusão

Em síntese:

```text
PROBLEMA
↓
HÁ RÓTULOS? → SUPERVISIONADO / NÃO SUPERVISIONADO
↓
TREINAMENTO
↓
VALIDAÇÃO E SELEÇÃO
↓
GENERALIZAÇÃO
```

Supervisionado e não supervisionado diferem pela disponibilidade do alvo: um generaliza relações entre entradas e alvos; o outro revela a estrutura dos dados. Em ambos, a qualidade depende da adequação entre problema, dados, modelo e métrica.

## Referências

1. BISHOP, C. M. **Pattern recognition and machine learning**. Springer, 2006.
2. HASTIE, T.; TIBSHIRANI, R.; FRIEDMAN, J. **The elements of statistical learning**. 2. ed. Springer, 2009.
3. GOODFELLOW, I.; BENGIO, Y.; COURVILLE, A. **Deep learning**. MIT Press, 2016.
