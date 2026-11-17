# Ponto 6 — Aprendizado por Reforço

## 6.1. Introdução e Delimitação do Problema

```text
[agente: estado → **ação** → recompensa]
                  ↓
[ninguém informa a ação **correta**]
                  ↓
[**política** que maximiza retorno de longo prazo]
```

## 6.2. Fundamentos e Relevância

```text
[**MDP** (S, A, P, R, γ) · Markov]
                 ↓
[**retorno**: G_t = Σ γ^k R_{t+k+1}]
                 ↓
[ruim agora, ótima no total → **atribuição de crédito**]
```

## 6.3. Núcleo Técnico

### 6.3.1. Política e Funções de Valor

```text
[política **π(a|s)**]
          ↓
[**V^π(s)**: estado ↔ **Q^π(s,a)**: estado + ação]
          ↓
[conhecer **Q** → melhorar π → repetir]
```

### 6.3.2. Equações de Bellman e Aprendizado Temporal

```text
[**Bellman**: V(s) = E[R + γ V(s′)]]
                  ↓
[programação dinâmica (modelo) ↔ **model-free**]
                  ↓
[**MC** ↔ **TD** (bootstrapping): viés × variância]
```

### 6.3.3. Exploração × Explotação

```text
[**explorar** ↔ **explotar**]
            ↓
[estratégia **ε-greedy**]
            ↓
[risco: explorar demais ↔ de menos]
```

### 6.3.4. Principais Famílias de Métodos

```text
[**valor**: Q-learning (max → off-policy) ↔ SARSA]
                    ↓
[**política** + valor → **ator–crítico**]
                    ↓
[RL profundo → **deadly triad** → DQN (2 mecanismos)]
```

## 6.4. Limitações, Trade-offs e Desafios Atuais

```text
[recompensa **esparsa** · experiência cara]
                    ↓
[recompensa ≠ objetivo → **reward hacking**]
                    ↓
[exploração livre arrisca → **safe RL**]
```

## 6.5. Conclusão

```text
[decisão **sequencial**: agora + futuro]
             ↓
[prática: **4 exigências**]
```
