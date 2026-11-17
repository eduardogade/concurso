# Ponto 5 — Aprendizado Supervisionado e Não Supervisionado

## 5.1. Introdução e Delimitação do Problema

5.1.A. [2][4] Organizar o aprendizado de máquina pela disponibilidade de variável-alvo, citando Bishop.

5.1.B. [2] Definir o supervisionado com o par \((x_{i},y_{i})\) e a função \(f:X \rightarrow Y\) que deve generalizar.

5.1.C. [2] Contrapor o não supervisionado, em que só há os \(x_{i}\).

5.1.D. [2] Associar cada paradigma às suas tarefas típicas.

## 5.2. Fundamentos e Relevância

5.2.A. [2] Introduzir o modelo \(f(x;\theta)\) e a função de perda, com um exemplo para regressão e outro para classificação.

5.2.B. [1] Apresentar o treinamento como minimização do risco empírico.

5.2.C. [1][5]

\[
\theta^{*} = \arg\min_{\theta}\frac{1}{n}\sum_{i = 1}^{n}\ell(f(x_{i};\theta),y_{i})
\]

5.2.D. [1] Contrapor o objetivo real, errar pouco em dados novos, e justificar a divisão dos dados.

5.2.E. [2] Quadro com a função de treino, validação e teste.

5.2.F. [2] Diferenciar parâmetros e hiperparâmetros, com exemplos.

5.2.G. [1][4] Relacionar underfitting e overfitting a viés e variância, citando Hastie et al.

5.2.H. [1] Introduzir a regularização como controle desse compromisso.

5.2.I. [1][5]

\[
\text{objetivo} = \text{erro empírico} + \lambda \cdot \text{complexidade}
\]

5.2.J. [5] Contrapor L2 e L1 pelo efeito sobre os pesos.

## 5.3. Núcleo Técnico

### 5.3.1. Aprendizado Supervisionado

5.3.1.A. [3] Abrir os bullets: os métodos diferem pela hipótese que fazem sobre os dados.

5.3.1.B. [2] Regressão linear e logística, com vantagem e limitação.

5.3.1.C. [2] Árvores de decisão, com o critério de divisão e o risco de sobreajuste.

5.3.1.D. [1][5] Ensembles: contrapor bagging e boosting, ligando cada um à variância ou ao viés.

5.3.1.E. [2] SVM e o papel dos kernels.

5.3.1.F. [2][4] Redes neurais e retropropagação, citando Goodfellow et al.

### 5.3.2. Aprendizado Não Supervisionado

5.3.2.A. [3] Abrir os bullets: sem alvo, o objetivo passa a ser caracterizar a estrutura.

5.3.2.B. [1][5] k-means, com os dois passos e as três limitações, incluindo o k-means++.

5.3.2.C. [2] Clustering hierárquico e o dendrograma.

5.3.2.D. [2] DBSCAN, com densidade, formas arbitrárias e ruído.

5.3.2.E. [2] PCA e a redução de dimensionalidade.

### 5.3.3. Avaliação e Seleção de Modelos

5.3.3.A. [2] Enumerar as métricas de classificação.

5.3.3.B. [1][5] Alertar que a acurácia engana com classes desbalanceadas, com o exemplo da fraude.

5.3.3.C. [2] Enumerar as métricas de regressão.

5.3.3.D. [1] Explicar por que a avaliação sem rótulos é indireta, com a silhueta.

5.3.3.E. [1] Introduzir a validação cruzada para amostras pequenas.

5.3.3.F. [2] Diagrama do k-fold.

5.3.3.G. [1] Ressaltar que o teste permanece intocado até o fim.

## 5.4. Limitações, Trade-offs e Desafios Atuais

5.4.A. [1][5] Explicar o data leakage com o exemplo da normalização.

5.4.B. [1] Ressaltar que bom desempenho no teste não garante desempenho fora da distribuição de treino.

5.4.C. [4][5] Introduzir o aprendizado profundo como ampliação da capacidade de representação.

5.4.D. [1][5] Discutir o preço dessa capacidade: dados, computação, superajuste e reprodutibilidade.

5.4.E. [3][4] Relacionar o monitoramento após a implantação à engenharia de MLOps.

5.4.F. [1][3] Concluir que não existe algoritmo universalmente superior e indicar os critérios de escolha.

## 5.5. Conclusão

5.5.A. [3] Diagrama de síntese.

5.5.B. [2][3] Retomar a diferença entre os paradigmas pela disponibilidade do alvo.

5.5.C. [1][3] Concluir que a qualidade depende da adequação entre problema, dados, modelo e métrica.

## Referências

R.A. [4] Referências em ABNT.
