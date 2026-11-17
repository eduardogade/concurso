
# Ponto 6 — Aprendizado por Reforço

## 6.1. Elementos Fundamentais e Interação Agente–Ambiente

O aprendizado por reforço constitui um paradigma em que um **agente** aprende por interação com um **ambiente**. No instante \(t\), o agente observa um estado \(s_t\), seleciona uma ação \(a_t\) segundo uma política \(π(a|s)\) e recebe do ambiente uma recompensa \(r_{t+1}\) e um novo estado \(s_{t+1}\):

[
(s_t, a_t) → (r_{t+1}, s_{t+1})
]

O **estado** representa a situação relevante para a decisão, a **ação** corresponde à escolha do agente e a **recompensa** fornece um sinal escalar sobre suas consequências. A política define o comportamento do agente, podendo ser determinística ou estocástica. A interação produz trajetórias, eventualmente organizadas em episódios.

Diferentemente do aprendizado supervisionado, não há, em geral, um rótulo indicando a ação correta em cada estado. O agente deve aprender pelas consequências de suas decisões. Além disso, **recompensa imediata não equivale ao objetivo de longo prazo**: ações presentes podem afetar resultados futuros. Assim, o problema fundamental de RL é aprender uma política capaz de produzir elevado retorno acumulado ao longo da interação.

---

> Mnemonics



---

## 6.2. MDP, Retorno e Objetivo de Longo Prazo

O aprendizado por reforço é frequentemente formalizado como um **Processo de Decisão de Markov (MDP)**:

\[
MDP = (S, A, P, R, \gamma)
\]

em que \(S\) é o conjunto de estados, \(A\) o conjunto de ações, \(P\) a dinâmica de transição, \(R\) a função de recompensa e \(\gamma\) o fator de desconto. A propriedade de Markov estabelece que, dado o estado atual e a ação escolhida, a distribuição do próximo estado independe da história anterior:

\[
P(s_{t+1}|s_t,a_t,história)
=
P(s_{t+1}|s_t,a_t)
\]

O objetivo do agente não é maximizar apenas recompensas imediatas, mas o **retorno acumulado**:

\[
G_t = \Sigma_{k=0}^{\infty} \gamma^k r_{t+k+1}
\]

O fator \(\gamma\) controla a importância das recompensas futuras e o horizonte efetivo de decisão. Assim, uma política é avaliada pelo retorno esperado que produz:

\[
\pi^* = \arg\max_\pi E[G_t | \pi]
\]

Essa formulação explica por que decisões localmente desfavoráveis podem ser globalmente ótimas e introduz o problema de **credit assignment**, isto é, determinar quais ações anteriores contribuíram para recompensas futuras.

---

> Mnemonics

---

## 6.3. Política, Funções de Valor e Equações de Bellman

A política \(\pi(a \mid s)\) define o comportamento do agente, isto é, a probabilidade de escolher uma ação \(a\) em um estado \(s\). Para avaliar as consequências de uma política ao longo do tempo, utilizam-se funções de valor. A função de valor de estado é:

\[
V^\pi(s)
=
\mathbb{E}_\pi[G_t \mid S_t=s]
\]

enquanto a função estado–ação é:

\[
Q^\pi(s,a)
=
\mathbb{E}_\pi[G_t \mid S_t=s,A_t=a]
\]

Essas funções obedecem a uma decomposição recursiva expressa pelas equações de Bellman. Para \(V^\pi\):

\[
V^\pi(s)
=
\mathbb{E}_\pi
\left[
R_{t+1}
+
\gamma V^\pi(S_{t+1})
\mid S_t=s
\right]
\]

ou seja, o valor presente corresponde à recompensa imediata somada ao valor descontado esperado do futuro.

A política ótima \(\pi^*\) maximiza o retorno esperado, e a função ótima \(Q^*\) satisfaz:

\[
Q^*(s,a)
=
\mathbb{E}
\left[
R_{t+1}
+
\gamma
\max_{a'}
Q^*(S_{t+1},a')
\mid S_t=s,A_t=a
\right]
\]

Assim, funções de valor permitem avaliar estados e ações e fundamentam métodos de **avaliação e melhoria de política**, como policy iteration, value iteration e Q-learning.

---

> Mnemonics

---

## 6.4. Exploração × Explotação e Famílias de Métodos

Um dos problemas centrais do aprendizado por reforço é o compromisso entre **exploração** e **explotação**. Explorar significa testar ações ainda pouco conhecidas para adquirir informação; explotar significa selecionar a melhor ação segundo o conhecimento atual. Estratégias como \(\varepsilon\)-greedy equilibram essas alternativas, escolhendo a ação de maior valor com probabilidade \(1-\varepsilon\) e explorando com probabilidade \(\varepsilon\).

Entre os métodos baseados em valor, **Q-learning** atualiza:

\[
Q(s_t,a_t)
\leftarrow
Q(s_t,a_t)
+
\alpha
\left[
r_{t+1}
+
\gamma \max_a Q(s_{t+1},a)
-
Q(s_t,a_t)
\right]
\]

sendo tipicamente **off-policy**. Já SARSA utiliza o valor da ação efetivamente escolhida no estado seguinte e é tipicamente **on-policy**.

Outras famílias incluem métodos **baseados em política**, que parametrizam diretamente \(\pi_\theta(a\mid s)\), e arquiteturas **Actor–Critic**, nas quais o ator escolhe ações e o crítico estima seu valor. Métodos também podem ser classificados como **model-free**, quando aprendem sem modelar explicitamente a dinâmica, ou **model-based**, quando utilizam um modelo para planejamento.

Assim, RL pode ser organizado por três distinções principais:

\[
\text{valor vs. política},
\qquad
\text{model-free vs. model-based},
\qquad
\text{on-policy vs. off-policy}
\]

---

> Mnemonics

---

## 6.5. Aprendizado Temporal, Limitações, Desafios e Síntese

Métodos de **Temporal Difference (TD)** atualizam estimativas de valor a partir da diferença entre o valor esperado e a informação observada no passo seguinte. Uma forma básica é:

\[
V(S_t)
\leftarrow
V(S_t)
+
\alpha \delta_t
\]

com:

\[
\delta_t
=
R_{t+1}
+
\gamma V(S_{t+1})
-
V(S_t)
\]

O termo \(\delta_t\) é o **erro TD** e permite aprendizado incremental por *bootstrapping*, sem necessidade de aguardar o retorno completo de um episódio.

Apesar de sua flexibilidade, RL apresenta desafios importantes. Recompensas esparsas dificultam exploração e **credit assignment**; ambientes complexos podem exigir grande número de interações, reduzindo a eficiência amostral; e funções de recompensa mal especificadas podem produzir **reward hacking**, pois:

\[
\text{maximizar recompensa especificada}
\neq
\text{maximizar objetivo real}
\]

Além disso, exploração pode ser arriscada em ambientes reais, funções de valor podem exigir aproximação em espaços de alta dimensionalidade, e políticas podem perder robustez quando a distribuição do ambiente muda. Assim, desempenho em simulação ou treinamento não garante comportamento seguro e estável em implantação.

Em síntese, RL combina interação sequencial, retorno, funções de valor e melhoria de política:

\[
\text{interação}
\rightarrow
\text{retorno}
\rightarrow
\text{valor}
\rightarrow
\text{política}
\rightarrow
\text{nova interação}
\]

---

> Mnemonics

---

## Texto Final

# Ponto 6 — Aprendizado por Reforço

## 1. Introdução e Delimitação do Problema

O **aprendizado por reforço** (*Reinforcement Learning — RL*) é um paradigma em que um agente aprende a tomar decisões por interação sequencial com um ambiente. No instante \(t\), o agente observa um estado \(s_t\), seleciona uma ação \(a_t\) segundo uma política \(\pi\) e recebe uma recompensa \(r_{t+1}\) e um novo estado \(s_{t+1}\):

\[
(s_t,a_t)\rightarrow(r_{t+1},s_{t+1})
\]

Diferentemente do aprendizado supervisionado, não há, em geral, um rótulo informando a ação correta em cada estado. O agente deve descobrir, pelas consequências de suas decisões, comportamentos capazes de maximizar resultados ao longo do tempo. Assim:

\[
\text{recompensa imediata}
\neq
\text{objetivo de longo prazo}
\]

O problema central de RL é, portanto, aprender uma política que produza **alto retorno acumulado esperado**.

## 2. Fundamentos e Relevância

A interação é frequentemente formalizada por um **Processo de Decisão de Markov (MDP)**:

\[
MDP=(S,A,P,R,\gamma)
\]

em que \(S\) é o espaço de estados, \(A\) o espaço de ações, \(P\) a dinâmica de transição, \(R\) a recompensa e \(\gamma\in[0,1]\) o fator de desconto.

A propriedade de Markov estabelece que, dado o estado atual e a ação escolhida, o futuro independe da história anterior:

\[
P(s_{t+1}\mid s_t,a_t,\text{história})
=
P(s_{t+1}\mid s_t,a_t)
\]

O agente não otimiza recompensas isoladas, mas o **retorno**:

\[
G_t
=
\sum_{k=0}^{\infty}
\gamma^k r_{t+k+1}
\]

O fator \(\gamma\) controla o peso atribuído às consequências futuras. Dessa forma, uma ação localmente desfavorável pode ser globalmente ótima se conduzir a estados de maior valor.

O objetivo pode ser expresso por:

\[
\pi^*
=
\arg\max_\pi
\mathbb{E}[G_t\mid\pi]
\]

Essa natureza temporal introduz o **credit assignment problem**: determinar quais decisões anteriores contribuíram para recompensas recebidas posteriormente.

## 3. Núcleo Técnico

### 3.1. Política e Funções de Valor

A política \(\pi(a\mid s)\) define a probabilidade de selecionar uma ação \(a\) no estado \(s\). Para avaliar suas consequências de longo prazo, utilizam-se funções de valor.

A função de valor de estado é:

\[
V^\pi(s)
=
\mathbb{E}_\pi[G_t\mid S_t=s]
\]

e a função estado–ação:

\[
Q^\pi(s,a)
=
\mathbb{E}_\pi[G_t\mid S_t=s,A_t=a]
\]

Assim, \(V^\pi(s)\) responde quão desejável é estar em determinado estado, enquanto \(Q^\pi(s,a)\) avalia a qualidade de executar uma ação específica nesse estado.

A relação entre comportamento e aprendizado pode ser sintetizada por:

\[
\text{política}
\rightarrow
\text{ações}
\rightarrow
\text{retorno}
\rightarrow
\text{valor}
\rightarrow
\text{melhoria da política}
\]

### 3.2. Equações de Bellman e Aprendizado Temporal

As funções de valor apresentam estrutura recursiva. Para uma política \(\pi\), a equação de Bellman pode ser expressa por:

\[
V^\pi(s)
=
\mathbb{E}_\pi
\left[
R_{t+1}
+
\gamma V^\pi(S_{t+1})
\mid S_t=s
\right]
\]

Logo:

\[
\text{valor presente}
=
\text{recompensa imediata}
+
\text{futuro descontado}
\]

A função ótima \(Q^*\) satisfaz:

\[
Q^*(s,a)
=
\mathbb{E}
\left[
R_{t+1}
+
\gamma\max_{a'}Q^*(S_{t+1},a')
\mid S_t=s,A_t=a
\right]
\]

Essas relações fundamentam métodos de avaliação e melhoria de políticas, como *policy iteration*, *value iteration* e Q-learning.

Métodos de **Temporal Difference (TD)** permitem aprender incrementalmente. Uma atualização básica é:

\[
V(S_t)
\leftarrow
V(S_t)
+
\alpha\delta_t
\]

com erro TD:

\[
\delta_t
=
R_{t+1}
+
\gamma V(S_{t+1})
-
V(S_t)
\]

O TD realiza *bootstrapping*: uma estimativa de valor é atualizada utilizando outra estimativa, sem necessidade de aguardar o término completo do episódio.

### 3.3. Exploração × Explotação

Como o agente inicialmente desconhece as consequências das ações, surge o compromisso entre:

- **exploração**: testar ações pouco conhecidas para adquirir informação;
- **explotação**: selecionar a melhor ação segundo o conhecimento atual.

Uma estratégia clássica é \(\varepsilon\)-greedy: com probabilidade \(1-\varepsilon\), escolhe-se a ação de maior valor conhecido; com probabilidade \(\varepsilon\), explora-se outra alternativa.

Portanto:

\[
\text{exploração}
\leftrightarrow
\text{explotação}
\]

Explorar demais desperdiça recompensa; explotar prematuramente pode prender o agente em políticas subótimas.

### 3.4. Principais Famílias de Métodos

Os métodos de RL podem ser organizados segundo diferentes eixos.

**Métodos baseados em valor** aprendem funções como \(Q(s,a)\). O Q-learning, por exemplo, utiliza:

\[
Q(s_t,a_t)
\leftarrow
Q(s_t,a_t)
+
\alpha
\left[
r_{t+1}
+
\gamma\max_aQ(s_{t+1},a)
-
Q(s_t,a_t)
\right]
\]

e é tipicamente **off-policy**. Já SARSA utiliza a ação efetivamente executada no próximo estado e é tipicamente **on-policy**.

**Métodos baseados em política** parametrizam diretamente:

\[
\pi_\theta(a\mid s)
\]

e ajustam \(\theta\) para maximizar o retorno esperado.

Arquiteturas **Actor–Critic** combinam essas perspectivas:

- **ator**: seleciona ações segundo a política;
- **crítico**: estima valor e fornece sinal para melhorar a política.

Outra distinção é:

\[
\text{model-free}
\quad\text{vs.}\quad
\text{model-based}
\]

Métodos *model-free* aprendem valores ou políticas sem representar explicitamente a dinâmica do ambiente; métodos *model-based* utilizam ou aprendem um modelo de transições e recompensas para planejamento.

Com aproximadores de função, especialmente redes neurais, essas ideias originam o **Deep Reinforcement Learning**, permitindo atuar em espaços de estado de alta dimensionalidade.

## 4. Limitações, Trade-offs e Desafios Atuais

Apesar de poderoso, RL enfrenta desafios específicos.

**Recompensas esparsas** reduzem o sinal disponível para aprendizagem e agravam o problema de atribuição de crédito. Além disso, muitos métodos exigem grande número de interações, tornando a **eficiência amostral** crítica quando cada experiência tem custo real.

Outro desafio fundamental é a especificação da recompensa:

\[
\text{maximizar recompensa especificada}
\neq
\text{maximizar objetivo real}
\]

Funções de recompensa inadequadas podem produzir **reward hacking** ou *specification gaming*, nos quais o agente maximiza numericamente a recompensa sem cumprir a intenção do sistema.

Também existem importantes trade-offs:

- exploração × segurança;
- desempenho × eficiência amostral;
- capacidade de representação × estabilidade;
- planejamento explícito × custo computacional.

Em robótica, medicina ou sistemas industriais, exploração irrestrita pode ser perigosa, motivando **safe RL**. Em espaços de alta dimensionalidade, aproximação de valor ou política pode introduzir instabilidade e sensibilidade a hiperparâmetros.

Finalmente:

\[
\text{bom desempenho no ambiente de treino}
\neq
\text{robustez em implantação}
\]

Mudanças na dinâmica, nos usuários ou na distribuição dos estados podem degradar políticas aprendidas em condições diferentes.

## 5. Conclusão

O aprendizado por reforço trata a aprendizagem como um processo de decisão sequencial no qual ações alteram tanto recompensas imediatas quanto oportunidades futuras. Sua estrutura essencial pode ser sintetizada por:

\[
\text{interação}
\rightarrow
\text{retorno}
\rightarrow
\text{valor}
\rightarrow
\text{política}
\rightarrow
\text{nova interação}
\]

Assim, RL integra modelagem de decisões, estimação de valor, exploração e melhoria de política, buscando comportamentos que maximizem consequências de longo prazo, mas cuja aplicação prática exige eficiência, estabilidade, segurança e especificação cuidadosa dos objetivos.

## Referências

- SUTTON, R. S.; BARTO, A. G. *Reinforcement Learning: An Introduction*. 2018.
- WATKINS, C. J. C. H.; DAYAN, P. *Q-learning*. 1992.
- WILLIAMS, R. J. *Simple Statistical Gradient-Following Algorithms for Connectionist Reinforcement Learning*. 1992.
- MNIH, V. et al. *Human-level Control through Deep Reinforcement Learning*. 2015.

---

## Outras Notas

