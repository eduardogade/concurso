# Ponto 4 — Mineração de Dados: Descoberta de Conhecimento, Análise Exploratória de Dados, Identificação de Padrões e Anomalias

## 4.1. Introdução e Delimitação do Problema

4.1.A. [2] Introduzir a mineração de dados e diferenciá-la da descoberta de conhecimento.

4.1.B. [2] Ressaltar o objetivo: padrões com as quatro qualidades, capazes de apoiar decisões.

4.1.C. [2][4] Situar a mineração como etapa do KDD, citando Fayyad et al.

## 4.2. Fundamentos e Relevância

4.2.A. [2][3] Diagrama do processo KDD, da seleção ao conhecimento.

4.2.B. [2] Percorrer a função de cada etapa.

4.2.C. [1] Ressaltar o caráter iterativo do processo.

4.2.D. [2] Distinguir dado, padrão e conhecimento.

4.2.E. [3] Quadro com o que transforma padrão em conhecimento.

4.2.F. [1] Alertar que um resultado detectável pode ser trivial, espúrio ou irrelevante.

## 4.3. Núcleo Técnico

### 4.3.1. Preparação dos Dados e Análise Exploratória

4.3.1.A. [1] Relacionar a qualidade dos padrões à qualidade e à representação dos dados, ressaltando que a preparação não é neutra.

4.3.1.B. [2][4] Introduzir a EDA pelo propósito de compreender antes de modelar, citando Tukey.

4.3.1.C. [2][5] Contrapor medidas sensíveis e robustas a valores extremos e ligar mediana e quartis ao boxplot.

4.3.1.D. [5] Explicar o critério de atípicos do boxplot pelo IQR.

4.3.1.E. [2] Apresentar histogramas e diagramas de dispersão pelo que cada um revela.

4.3.1.F. [5] Diferenciar Pearson e Spearman.

4.3.1.G. [1][3] Concluir que os achados da EDA são hipóteses que orientam as etapas seguintes.

### 4.3.2. Identificação e Mineração de Padrões

4.3.2.A. [2] Enumerar as formas que um padrão pode assumir.

4.3.2.B. [2][4] Introduzir as regras de associação com o exemplo do pão e da manteiga, citando Han, Pei e Tong.

4.3.2.C. [2][5]

\[
sup(X \rightarrow Y) = \frac{freq(X \cup Y)}{N},
\]

4.3.2.D. [2][5]

\[
conf(X \rightarrow Y) = \frac{sup(X \cup Y)}{sup(X)},
\]

4.3.2.E. [2][5]

\[
lift(X \rightarrow Y) = \frac{conf(X \rightarrow Y)}{sup(Y)}.
\]

4.3.2.F. [1] Interpretar cada medida e o significado de \(lift > 1\).

4.3.2.G. [2] Distinguir padrões globais e locais.

4.3.2.H. [1][5] Ressaltar que frequência não é relevância, nos dois sentidos.

### 4.3.3. Identificação de Anomalias

4.3.3.A. [2] Introduzir anomalias como desvio do comportamento esperado.

4.3.3.B. [1] Ressaltar que anomalia não é necessariamente erro e exemplificar outras origens.

4.3.3.C. [2] Bullets com os três tipos de anomalia, incluindo o exemplo do consumo de energia de madrugada.

4.3.3.D. [3] Anunciar que os métodos partem de diferentes noções de normalidade.

4.3.3.E. [1][5] Apresentar os métodos estatísticos, retomando o escore z e a regra do IQR.

4.3.3.F. [1][5] Contrapor os métodos de distância e de densidade, com o LOF.

4.3.3.G. [1][5] Apresentar o Isolation Forest e sua intuição.

4.3.3.H. [5] Discutir a perda de poder discriminativo em alta dimensionalidade e quais métodos ela prejudica.

## 4.4. Limitações, Trade-offs e Desafios Atuais

4.4.A. [1] Apresentar o principal risco: confundir estrutura aparente com conhecimento válido.

4.4.B. [1][5] Explicar o problema das múltiplas comparações.

4.4.C. [1] Concluir com os critérios de avaliação de padrões e anomalias.

4.4.D. [1][3] Quadro contrapondo associação e causalidade.

4.4.E. [1][5] Enumerar as explicações alternativas para uma relação observada e o que a inferência causal exige.

4.4.F. [1] Ressaltar o papel do conhecimento de domínio, nos dois sentidos.

## 4.5. Conclusão

4.5.A. [3] Diagrama de síntese.

4.5.B. [1][3] Concluir que o valor da mineração está em distinguir padrões robustos de artefatos e convertê-los em conhecimento.

## Referências

R.A. [4] Referências em ABNT.
