# Ponto 5 — Aprendizado Supervisionado e Não Supervisionado

## 5.1. Introdução e Delimitação do Problema

```text
[**variável-alvo** disponível?]
   ├→ [sim: (x_i, y_i) → **f: X → Y**]
   └→ [não: só x_i → **estrutura**]
```

## 5.2. Fundamentos e Relevância

```text
[**risco empírico** ≠ erro em dados novos]
                     ↓
[underfitting (**viés**) ↔ overfitting (**variância**)]
                     ↓
[**regularização**: erro + λ · complexidade (L1 ↔ L2)]
```

## 5.3. Núcleo Técnico

### 5.3.1. Aprendizado Supervisionado

```text
[método = **hipótese** sobre os dados]
                   ↓
[linear · árvore · **ensemble** · SVM · rede]
                   ↓
[**bagging** − variância ↔ **boosting** − viés]
```

### 5.3.2. Aprendizado Não Supervisionado

```text
[**k-means**: 2 passos · 3 limitações · k-means++]
                    ↓
[dendrograma · **DBSCAN** (ruído) · PCA]
```

### 5.3.3. Avaliação e Seleção de Modelos

```text
[**acurácia** engana se desbalanceado (fraude)]
             ↓
[sem rótulo → **silhueta**]
             ↓
[**k-fold** · teste intocado até o fim]
```

## 5.4. Limitações, Trade-offs e Desafios Atuais

```text
[**leakage** · fora da distribuição → teste engana]
                ↓
[**aprendizado profundo**: + capacidade, + preço]
                ↓
[nenhum algoritmo **universal**]
```

## 5.5. Conclusão

```text
[adequação: problema · dados · modelo · **métrica**]
```
