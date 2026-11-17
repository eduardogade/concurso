# Ponto 6 — Aprendizado por Reforço

## 6.1. Introdução e Delimitação do Problema

O **aprendizado por reforço** (*Reinforcement Learning*, RL) é o paradigma em que um agente aprende a tomar decisões interagindo com um ambiente¹. A cada passo, o agente observa um estado, escolhe uma ação e recebe uma recompensa e um novo estado.

Diferentemente do aprendizado supervisionado, ninguém informa a ação correta: o agente a descobre pelas consequências de suas escolhas, que podem demorar a aparecer:

```text
recompensa imediata ≠ objetivo de longo prazo
```

O problema central é aprender uma **política** que maximize o **retorno acumulado esperado**.

## 6.2. Fundamentos e Relevância

A interação é formalizada por um **Processo de Decisão de Markov (MDP)**, a tupla \((S,A,P,R,\gamma)\): estados, ações, dinâmica de transição, recompensa e fator de desconto \(\gamma \in [0,1)\). A **propriedade de Markov** supõe que o estado atual resume toda a história relevante.

O agente maximiza o **retorno descontado**:

\[
G_{t} = \sum_{k = 0}^{\infty}\gamma^{k}R_{t + k + 1}
\]

Com \(\gamma\) próximo de 0, o agente é imediatista; próximo de 1, valoriza o longo prazo. Assim, uma ação localmente ruim pode ser ótima se levar a estados melhores. Essa natureza temporal cria o **problema de atribuição de crédito**: quais decisões anteriores explicam uma recompensa recebida depois?

## 6.3. Núcleo Técnico

### 6.3.1. Política e Funções de Valor

A política \(\pi(a \mid s)\) é a probabilidade de escolher a ação \(a\) no estado \(s\). Para avaliá-la, usam-se **funções de valor**: \(V^{\pi}(s)\), o retorno esperado a partir de \(s\) seguindo \(\pi\), e \(Q^{\pi}(s,a)\), o retorno esperado ao executar \(a\) em \(s\) e depois seguir \(\pi\).

Conhecida \(Q\), melhora-se a política escolhendo, em cada estado, a ação de maior valor. Avaliar e melhorar a política, alternadamente, é a base do aprendizado.

### 6.3.2. Equações de Bellman e Aprendizado Temporal

As funções de valor são recursivas: o valor de um estado é a recompensa imediata mais o valor descontado do estado seguinte. É a **equação de Bellman**:

\[
V^{\pi}(s) = \mathbb{E}_{\pi}[R_{t + 1} + \gamma V^{\pi}(S_{t + 1}) \mid S_{t} = s]
\]

Na versão ótima, a média sobre as ações dá lugar ao máximo. Com o modelo do ambiente conhecido, essas equações são resolvidas por programação dinâmica (*policy iteration*, *value iteration*); sem ele (*model-free*), o agente aprende por experiência.

Os métodos de **Monte Carlo** esperam o fim do episódio e usam o retorno real como alvo: sem viés, mas com alta variância. Os de **diferença temporal (TD)** atualizam a cada passo:

\[
V(S_{t}) \leftarrow V(S_{t}) + \alpha[R_{t + 1} + \gamma V(S_{t + 1}) - V(S_{t})]
\]

O termo entre colchetes é o **erro TD**, diferença entre o observado e o esperado; \(\alpha\) é a taxa de aprendizado. Por usar uma estimativa para atualizar outra (*bootstrapping*), o TD aceita algum viés em troca de menor variância e de aprendizado contínuo.

### 6.3.3. Exploração × Explotação

O agente precisa equilibrar **exploração**, testar ações pouco conhecidas para obter informação, e **explotação**, escolher a melhor ação conhecida. Na estratégia ε-greedy, com probabilidade 1 − ε escolhe-se a ação de maior valor estimado e, com probabilidade ε, uma ação ao acaso. Explorar demais desperdiça recompensa; explorar de menos pode prender o agente em uma política subótima.

### 6.3.4. Principais Famílias de Métodos

Os **métodos baseados em valor** aprendem \(Q\). O **Q-learning**² aplica a ideia do TD à função \(Q\):

\[
Q(S_{t},A_{t}) \leftarrow Q(S_{t},A_{t}) + \alpha[R_{t + 1} + \gamma\max_{a}Q(S_{t + 1},a) - Q(S_{t},A_{t})]
\]

É **off-policy**: o alvo usa a melhor ação do próximo estado, mesmo que o agente, explorando, execute outra. O **SARSA** usa a ação efetivamente executada e é **on-policy**.

Os **métodos baseados em política** ajustam diretamente a política por gradiente, acomodando ações contínuas; os **ator–crítico** combinam ambos: o ator escolhe ações, e o crítico estima valores que o orientam.

Com redes neurais como aproximadores, surge o **aprendizado por reforço profundo**, capaz de lidar com estados de alta dimensão, como imagens, mas que pode ser instável quando combina aproximação de funções, *bootstrapping* e aprendizado *off-policy* (a *deadly triad*). O **DQN**³ estabilizou o Q-learning profundo com *experience replay*, que reutiliza transições passadas em ordem aleatória, e *target network*, cópia da rede que mantém o alvo estável.

## 6.4. Limitações, Trade-offs e Desafios Atuais

**Recompensas esparsas** fornecem pouco sinal e agravam a atribuição de crédito. Muitos métodos exigem milhões de interações, o que torna crítica a **eficiência amostral** quando cada experiência é cara.

Outro desafio é especificar a recompensa:

```text
maximizar recompensa especificada ≠ maximizar objetivo real
```

Recompensas mal definidas levam ao **reward hacking**: o agente aumenta a recompensa sem cumprir a intenção do projetista. Em robótica ou medicina, explorar livremente pode ser perigoso, o que motiva o **safe RL**.

## 6.5. Conclusão

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

O aprendizado por reforço trata a aprendizagem como decisão sequencial, em que ações alteram recompensas imediatas e oportunidades futuras. Sua aplicação prática exige eficiência amostral, estabilidade, segurança e especificação cuidadosa da recompensa.

## Referências

1. SUTTON, R. S.; BARTO, A. G. **Reinforcement learning**: an introduction. 2. ed. MIT Press, 2018.
2. WATKINS, C. J. C. H.; DAYAN, P. Q-learning. **Machine Learning**, 1992.
3. MNIH, V. et al. Human-level control through deep reinforcement learning. **Nature**, 2015.
