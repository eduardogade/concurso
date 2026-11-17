# Ponto 7 — MLOps: Desenvolvimento, Versionamento e Experimentação de Modelos

## 7.1. Introdução e Delimitação do Problema

7.1.A. [2] Caracterizar o desenvolvimento de modelos como iterativo, experimental e dependente de contexto.

7.1.B. [1][4] Explicar que o modelo resulta da combinação de vários fatores, não só do código, citando Sculley et al.

7.1.C. [3] Quadro contrapondo modelo treinado e código isolado.

7.1.D. [2][4] Descrever o ciclo de trabalho, citando Amershi et al.

7.1.E. [2][4] Apresentar o objetivo de MLOps neste recorte, citando Kreuzberger et al.

7.1.F. [3] Delimitar: implantação e operação ficam fora, e o ponto termina no modelo candidato validado.

## 7.2. Fundamentos e Relevância

7.2.A. [2] Apresentar cada execução relevante como unidade experimental.

7.2.B. [2][3] Quadro com os quatro componentes de um experimento.

7.2.C. [2] Detalhar o que entra em entradas, procedimento e saídas.

7.2.D. [1] Justificar por que uma métrica isolada não é evidência, com o exemplo da acurácia que subiu.

7.2.E. [1][3] Quadro com o princípio do resultado confiável.

## 7.3. Núcleo Técnico

### 7.3.1. Versionamento, Artefatos e Linhagem

7.3.1.A. [1] Justificar por que versionar só o código é insuficiente.

7.3.1.B. [2] Definir artefato, com exemplos.

7.3.1.C. [2] Diferenciar proveniência e linhagem.

7.3.1.D. [3] Diagrama da cadeia de linhagem, dos dados brutos às métricas.

7.3.1.E. [1] Explicar a pergunta que a linhagem permite responder.

7.3.1.F. [1][5] Exigir versões imutáveis e indicar os identificadores.

7.3.1.G. [4] Exemplificar com Git, DVC e MLflow e o papel de cada um.

### 7.3.2. Experiment Tracking e Rastreabilidade

7.3.2.A. [2] Apresentar o experiment tracking e o que ele registra.

7.3.2.B. [1] Relacionar tracking, versionamento e linhagem à rastreabilidade experimental.

7.3.2.C. [1][5] Explicar por que comparar experimentos exige protocolo equivalente.

7.3.2.D. [2] Introduzir o baseline, com exemplos.

### 7.3.3. Reprodutibilidade

7.3.3.A. [1] Anunciar que a reprodutibilidade depende do controle conjunto dos componentes.

7.3.3.B. [1][5]

\[
\text{resultado} = f(D, C, H, E, S)
\]

7.3.3.C. [2] Identificar as cinco letras.

7.3.3.D. [1] Explicar por que o mesmo script não é o mesmo experimento e como fixar ambiente e semente.

7.3.3.E. [5] Porém, ressalvar que reprodutível não é idêntico bit a bit, e justificar.

7.3.3.F. [1] Concluir com o objetivo realista.

### 7.3.4. Validação, Comparação e Seleção

7.3.4.A. [1] Diferenciar validação dos dados e validação do modelo pelo que cada uma verifica.

7.3.4.B. [1] Concluir que o melhor modelo não é o de maior métrica isolada.

7.3.4.C. [2] Tratar a busca de hiperparâmetros como experimentação, nomeando as três estratégias.

7.3.4.D. [1][5] Explicar o risco de superajuste ao conjunto de validação.

7.3.4.E. [5] Consequentemente, derivar o uso único do teste e estender o risco aos benchmarks públicos.

7.3.4.F. [2] Descrever quando o experimento se torna modelo candidato.

7.3.4.G. [2] Apresentar o registro de modelos.

## 7.4. Limitações, Trade-offs e Desafios Atuais

7.4.A. [1] Discutir o custo da rastreabilidade e da reprodutibilidade.

7.4.B. [1] Concluir que se guarda o suficiente, não tudo.

7.4.C. [1] Reconhecer o ganho da automação, com uma ressalva.

7.4.D. [1][3] Quadro contrapondo automatizar processo ruim e criar processo bom.

7.4.E. [1][5] Discutir o trade-off entre rigor e velocidade.

## 7.5. Conclusão

7.5.A. [3] Diagrama de síntese.

7.5.B. [3] Indicar os três elementos que atravessam todo o fluxo.

7.5.C. [1][3] Concluir que o valor do experimento está em demonstrar condições, validação e reconstrução.

## Referências

R.A. [4] Referências em ABNT.
