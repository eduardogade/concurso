# Ponto 6 — Aprendizado por Reforço

## 1. Introdução e Delimitação do Problema

O **aprendizado por reforço** (*Reinforcement Learning — RL*) é um paradigma em que um agente aprende a tomar decisões por interação sequencial com um ambiente [1]. No instante \(t\), o agente observa um estado \(S_t\), seleciona uma ação \(A_t\) segundo uma política \(\pi\) e recebe uma recompensa \(R_{t+1}\) e um novo estado \(S_{t+1}\):

\[
(S_t,A_t)\rightarrow(R_{t+1},S_{t+1})
\]

Diferentemente do aprendizado supervisionado, não há, em geral, um rótulo informando a ação correta em cada estado. O agente deve descobrir, pelas consequências de suas decisões, comportamentos capazes de maximizar resultados ao longo do tempo:

```text
recompensa imediata ≠ objetivo de longo prazo
```

O problema central de RL é, portanto, aprender uma política que produza **alto retorno acumulado esperado**.

## 2. Fundamentos e Relevância

A interação é frequentemente formalizada por um **Processo de Decisão de Markov (MDP)**:

\[
\mathrm{MDP}=(S,A,P,R,\gamma)
\]

em que \(S\) é o espaço de estados, \(A\) o espaço de ações, \(P\) a dinâmica de transição, \(R\) a recompensa e \(\gamma\in[0,1)\) o fator de desconto. A propriedade de Markov estabelece que, dados o estado atual e a ação escolhida, o futuro independe da história anterior:

\[
P(S_{t+1}\mid S_t,A_t,\text{história})=P(S_{t+1}\mid S_t,A_t)
\]

O agente não otimiza recompensas isoladas, mas o **retorno**:

\[
G_t=\sum_{k=0}^{\infty}\gamma^k R_{t+k+1}
\]

O fator \(\gamma\) controla o peso das consequências futuras: uma ação localmente desfavorável pode ser globalmente ótima se conduzir a estados de maior valor. O objetivo é:

\[
\pi^*=\arg\max_\pi\mathbb{E}_\pi[G_t]
\]

Essa natureza temporal introduz o **credit assignment problem**: determinar quais decisões anteriores contribuíram para recompensas recebidas posteriormente.

## 3. Núcleo Técnico

### 3.1. Política e Funções de Valor

A política \(\pi(a\mid s)\) define a probabilidade de selecionar a ação \(a\) no estado \(s\). Suas consequências de longo prazo são avaliadas por funções de valor:

\[
V^\pi(s)=\mathbb{E}_\pi[G_t\mid S_t=s]
\]

\[
Q^\pi(s,a)=\mathbb{E}_\pi[G_t\mid S_t=s,A_t=a]
\]

Assim, \(V^\pi(s)\) indica quão desejável é estar em determinado estado, enquanto \(Q^\pi(s,a)\) avalia a qualidade de executar uma ação específica nesse estado. A relação entre comportamento e aprendizado pode ser sintetizada por:

```text
política → ações → retorno → valor → melhoria da política
```

### 3.2. Equações de Bellman e Aprendizado Temporal

As funções de valor apresentam estrutura recursiva. Para uma política \(\pi\), a equação de Bellman é:

\[
V^\pi(s)=\mathbb{E}_\pi\left[R_{t+1}+\gamma V^\pi(S_{t+1})\mid S_t=s\right]
\]

```text
valor presente = recompensa imediata + futuro descontado
```

A função ótima \(Q^*\) satisfaz:

\[
Q^*(s,a)=\mathbb{E}\left[R_{t+1}+\gamma\max_{a'}Q^*(S_{t+1},a')\mid S_t=s,A_t=a\right]
\]

Essas relações fundamentam *policy iteration*, *value iteration* e Q-learning. Métodos de **Temporal Difference (TD)** aprendem incrementalmente:

\[
V(S_t)\leftarrow V(S_t)+\alpha\delta_t,\qquad\delta_t=R_{t+1}+\gamma V(S_{t+1})-V(S_t)
\]

O TD realiza *bootstrapping*: uma estimativa de valor é atualizada utilizando outra estimativa, sem aguardar o término do episódio.

### 3.3. Exploração × Explotação

Como o agente inicialmente desconhece as consequências das ações, surge o compromisso entre:

- **exploração**: testar ações pouco conhecidas para adquirir informação;
- **explotação**: selecionar a melhor ação segundo o conhecimento atual.

Na estratégia \(\varepsilon\)-greedy, com probabilidade \(1-\varepsilon\) escolhe-se a ação de maior valor estimado e, com probabilidade \(\varepsilon\), explora-se outra alternativa. Explorar demais desperdiça recompensa; explotar prematuramente pode prender o agente em políticas subótimas.

### 3.4. Principais Famílias de Métodos

Os métodos de RL podem ser organizados segundo diferentes eixos. **Métodos baseados em valor** aprendem funções como \(Q(s,a)\). O Q-learning [2] utiliza:

\[
Q(S_t,A_t)\leftarrow Q(S_t,A_t)+\alpha\left[R_{t+1}+\gamma\max_a Q(S_{t+1},a)-Q(S_t,A_t)\right]
\]

e é **off-policy**; já o SARSA utiliza a ação efetivamente executada no próximo estado e é **on-policy**.

**Métodos baseados em política** parametrizam diretamente \(\pi_\theta(a\mid s)\) e ajustam \(\theta\) por gradiente para maximizar o retorno esperado [3], o que acomoda políticas estocásticas e ações contínuas. Arquiteturas **Actor–Critic** combinam essas perspectivas:

- **ator**: seleciona ações segundo a política;
- **crítico**: estima valor e fornece sinal para melhorar a política.

Métodos *model-free* aprendem valores ou políticas sem representar explicitamente a dinâmica do ambiente; métodos *model-based* utilizam ou aprendem um modelo de transições e recompensas para planejamento. Com aproximadores de função, especialmente redes neurais, essas ideias originam o **Deep Reinforcement Learning** [4], que permite atuar em espaços de estado de alta dimensionalidade.

## 4. Limitações, Trade-offs e Desafios Atuais

Apesar de poderoso, RL enfrenta desafios específicos. **Recompensas esparsas** reduzem o sinal disponível para aprendizagem e agravam o problema de atribuição de crédito. Muitos métodos exigem grande número de interações, tornando a **eficiência amostral** crítica quando cada experiência tem custo real. Outro desafio fundamental é a especificação da recompensa:

```text
maximizar recompensa especificada ≠ maximizar objetivo real
```

Funções de recompensa inadequadas podem produzir **reward hacking** ou *specification gaming*, nos quais o agente maximiza numericamente a recompensa sem cumprir a intenção do sistema. Também existem importantes trade-offs:

- exploração × segurança;
- desempenho × eficiência amostral;
- capacidade de representação × estabilidade;
- planejamento explícito × custo computacional.

Em robótica, medicina ou sistemas industriais, exploração irrestrita pode ser perigosa, motivando o **safe RL**; em espaços de alta dimensionalidade, a aproximação de valor ou política pode introduzir instabilidade e sensibilidade a hiperparâmetros. Por fim, bom desempenho no ambiente de treino não garante robustez em implantação: mudanças na dinâmica, nos usuários ou na distribuição dos estados podem degradar políticas aprendidas.

## 5. Conclusão

Em síntese:

```text
INTERAÇÃO
↓
RETORNO
↓
VALOR
↓
POLÍTICA
↓
NOVA INTERAÇÃO
```

O aprendizado por reforço trata a aprendizagem como um processo de decisão sequencial no qual ações alteram tanto recompensas imediatas quanto oportunidades futuras. Integra modelagem de decisões, estimação de valor, exploração e melhoria de política, buscando comportamentos que maximizem consequências de longo prazo, mas sua aplicação prática exige eficiência, estabilidade, segurança e especificação cuidadosa dos objetivos.

## Referências

[1] SUTTON, R. S.; BARTO, A. G. *Reinforcement Learning: An Introduction*. 2018.
[2] WATKINS, C. J. C. H.; DAYAN, P. *Q-learning*. 1992.
[3] WILLIAMS, R. J. *Simple Statistical Gradient-Following Algorithms for Connectionist Reinforcement Learning*. 1992.
[4] MNIH, V. et al. *Human-level Control through Deep Reinforcement Learning*. 2015.
