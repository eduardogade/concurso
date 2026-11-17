# Ponto 6 — Aprendizado por Reforço

## 6.1. Introdução e Delimitação do Problema

6.1.A. [2][4] Definir o aprendizado por reforço pela interação do agente com o ambiente, citando Sutton e Barto.

6.1.B. [2] Descrever o ciclo de interação a cada passo.

6.1.C. [1] Contrapor ao aprendizado supervisionado: ninguém informa a ação correta.

6.1.D. [1][3] Quadro contrapondo recompensa imediata e objetivo de longo prazo.

6.1.E. [2] Formular o problema central em termos de política e retorno acumulado esperado.

## 6.2. Fundamentos e Relevância

6.2.A. [2] Formalizar a interação como MDP, com a tupla \((S,A,P,R,\gamma)\) e \(\gamma \in [0,1)\), nomeando cada elemento.

6.2.B. [2] Enunciar a propriedade de Markov.

6.2.C. [2] Introduzir o retorno descontado como aquilo que o agente maximiza.

6.2.D. [1][5]

\[
G_{t} = \sum_{k = 0}^{\infty}\gamma^{k}R_{t + k + 1}
\]

6.2.E. [1] Interpretar os extremos de \(\gamma\) e justificar por que uma ação localmente ruim pode ser ótima.

6.2.F. [5] Consequentemente, introduzir o problema de atribuição de crédito.

## 6.3. Núcleo Técnico

### 6.3.1. Política e Funções de Valor

6.3.1.A. [2] Definir a política \(\pi(a \mid s)\).

6.3.1.B. [2] Introduzir \(V^{\pi}(s)\) e \(Q^{\pi}(s,a)\) e diferenciar o que cada uma avalia.

6.3.1.C. [1] Explicar como conhecer \(Q\) permite melhorar a política.

6.3.1.D. [3] Concluir que avaliar e melhorar, alternadamente, é a base do aprendizado.

### 6.3.2. Equações de Bellman e Aprendizado Temporal

6.3.2.A. [1] Explicar a recursividade das funções de valor antes da equação.

6.3.2.B. [1][5]

\[
V^{\pi}(s) = \mathbb{E}_{\pi}[R_{t + 1} + \gamma V^{\pi}(S_{t + 1}) \mid S_{t} = s]
\]

6.3.2.C. [5] Indicar o que muda na versão ótima.

6.3.2.D. [1] Contrapor programação dinâmica, com modelo conhecido, ao aprendizado por experiência, model-free.

6.3.2.E. [1][5] Apresentar Monte Carlo pelo alvo que usa e pelo seu viés e variância.

6.3.2.F. [2] Introduzir a diferença temporal e sua atualização a cada passo.

6.3.2.G. [1][5]

\[
V(S_{t}) \leftarrow V(S_{t}) + \alpha[R_{t + 1} + \gamma V(S_{t + 1}) - V(S_{t})]
\]

6.3.2.H. [1] Identificar o erro TD e a taxa de aprendizado.

6.3.2.I. [5] Explicar o bootstrapping e o compromisso entre viés e variância em relação a Monte Carlo.

### 6.3.3. Exploração × Explotação

6.3.3.A. [2] Contrapor exploração e explotação.

6.3.3.B. [1] Explicar a estratégia ε-greedy.

6.3.3.C. [1] Discutir o risco de explorar demais e de explorar de menos.

### 6.3.4. Principais Famílias de Métodos

6.3.4.A. [2] Introduzir os métodos baseados em valor.

6.3.4.B. [1][4] Apresentar o Q-learning como TD aplicado a \(Q\), citando Watkins e Dayan.

6.3.4.C. [1][5]

\[
Q(S_{t},A_{t}) \leftarrow Q(S_{t},A_{t}) + \alpha[R_{t + 1} + \gamma\max_{a}Q(S_{t + 1},a) - Q(S_{t},A_{t})]
\]

6.3.4.D. [1][5] Explicar por que o Q-learning é off-policy e contrapor ao SARSA.

6.3.4.E. [2] Apresentar os métodos baseados em política e sua vantagem.

6.3.4.F. [2] Mostrar como o ator–crítico combina as duas famílias.

6.3.4.G. [4][5] Introduzir o aprendizado por reforço profundo e o que ele permite.

6.3.4.H. [5] Porém, discutir a instabilidade da deadly triad, nomeando seus três elementos.

6.3.4.I. [1][4] Apresentar o DQN, citando Mnih et al., e os dois mecanismos de estabilização.

## 6.4. Limitações, Trade-offs e Desafios Atuais

6.4.A. [1] Discutir recompensas esparsas e sua relação com a atribuição de crédito.

6.4.B. [1] Ressaltar a eficiência amostral quando cada experiência é cara.

6.4.C. [1][3] Quadro contrapondo recompensa especificada e objetivo real.

6.4.D. [1][5] Explicar o reward hacking.

6.4.E. [5] Relacionar o risco da exploração livre ao safe RL, com exemplos de domínio.

## 6.5. Conclusão

6.5.A. [3] Diagrama de síntese.

6.5.B. [3] Retomar o RL como decisão sequencial que afeta recompensas imediatas e oportunidades futuras.

6.5.C. [1] Concluir com as quatro exigências da aplicação prática.

## Referências

R.A. [4] Referências em ABNT.
