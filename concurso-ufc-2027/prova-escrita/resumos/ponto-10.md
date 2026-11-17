# Ponto 10 — XAI: Métodos, Interpretabilidade, Avaliação e Uso das Explicações

## 10.1. Introdução e Delimitação do Problema

10.1.A. [2] Apresentar a XAI pelo seu propósito.

10.1.B. [1] Ressaltar que o objetivo é fornecer evidência, não narrativa convincente.

10.1.C. [2][3] Quadro com a primeira distinção, entre interpretabilidade intrínseca e explicação post hoc.

10.1.D. [2][4] Exemplificar modelos intrinsecamente interpretáveis e contrapor os métodos post hoc, citando Molnar.

10.1.E. [3] Lista numerada com as quatro perguntas que organizam o problema.

10.1.F. [3] Concluir que XAI é problema de método, avaliação e uso.

## 10.2. Fundamentos e Relevância

10.2.A. [2] Contrapor explicações locais e globais.

10.2.B. [2] Contrapor métodos model-specific e model-agnostic.

10.2.C. [1][3] Quadro contrapondo importância para o modelo e efeito causal.

## 10.3. Núcleo Técnico

### 10.3.1. Atribuição de Atributos

10.3.1.A. [2] Introduzir a feature attribution.

10.3.1.B. [2][4] Apresentar a decomposição aditiva do SHAP, citando Lundberg e Lee.

10.3.1.C. [1][5]

\[
f(x) = \phi_{0} + \sum_{j = 1}^{p}\phi_{j}
\]

10.3.1.D. [2] Identificar \(\phi_{0}\) e \(\phi_{j}\).

10.3.1.E. [1][5] Explicar os valores de Shapley pela analogia dos jogadores e da contribuição marginal média.

10.3.1.F. [5] Destacar a unicidade, a propriedade de reproduzir a predição e o custo exponencial.

10.3.1.G. [2] Introduzir a permutation importance e sua lógica.

10.3.1.H. [1][5]

\[
I_{j} = M_{\text{original}} - M_{\text{permutado}(j)}
\]

10.3.1.I. [1] Discutir o problema das features correlacionadas.

10.3.1.J. [2] Mencionar os métodos de gradiente em redes neurais, com o Integrated Gradients.

### 10.3.2. Surrogates, Exemplos e Contrafactuais

10.3.2.A. [2] Introduzir os surrogates, com \(g(x) \approx f(x)\).

10.3.2.B. [1][4] Explicar o LIME como surrogate local, citando Ribeiro et al.

10.3.2.C. [1] Ressaltar que fidelidade local não implica fidelidade global.

10.3.2.D. [2] Mencionar as explicações baseadas em exemplos.

10.3.2.E. [2] Introduzir os contrafactuais e a busca da menor mudança.

10.3.2.F. [1][5]

\[
x^{*} = \arg\min_{x'}[d(x,x') + \lambda L(f(x'),y_{\text{desejado}})]
\]

10.3.2.G. [5] Indicar as qualidades de um bom contrafactual, com o exemplo da idade.

### 10.3.3. Avaliação das Explicações

10.3.3.A. [1][3] Quadro contrapondo plausibilidade e fidelidade.

10.3.3.B. [2] Introduzir a fidelidade e acrescentar estabilidade e compreensibilidade.

10.3.3.C. [5] Discutir o trade-off entre fidelidade e simplicidade.

10.3.3.D. [1][4] Apresentar as três formas de avaliação, citando Molnar.

### 10.3.4. Uso das Explicações

10.3.4.A. [1] Mostrar o uso no desenvolvimento para revelar problemas ocultos por uma boa métrica.

10.3.4.B. [2] Indicar o uso em suporte à decisão.

10.3.4.C. [1][5] Diferenciar aumentar a confiança e obter confiança calibrada.

10.3.4.D. [2] Mencionar auditoria e investigação de erros.

## 10.4. Limitações, Trade-offs e Desafios Atuais

10.4.A. [1][3] Quadro com a limitação fundamental, entre explicar o modelo e explicar o fenômeno.

10.4.B. [1][5] Explicar por que uma explicação fiel pode apenas revelar atalhos e correlações espúrias.

10.4.C. [1] Discutir as fragilidades dos métodos post hoc e a discordância entre métodos.

10.4.D. [1] Ressaltar que XAI não corrige o modelo e o que fazer ao revelar um viés.

10.4.E. [1][5] Concluir pela preferência por modelos interpretáveis quando satisfazem os requisitos.

## 10.5. Conclusão

10.5.A. [3] Diagrama de síntese.

10.5.B. [3] Concluir que XAI vai além de gerar explicações, retomando as quatro ações.

10.5.C. [1][3] Fechar com as três qualidades de uma boa explicação.

## Referências

R.A. [4] Referências em ABNT.
