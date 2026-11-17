# Ponto 10 — XAI: Métodos, Interpretabilidade, Avaliação e Uso das Explicações

## 10.1. Introdução e Delimitação do Problema

```text
[**evidência** ≠ narrativa convincente]
               ↓
[**intrínseca** ↔ **post hoc**]
               ↓
[método → avaliação → **uso**]
```

## 10.2. Fundamentos e Relevância

```text
[**local** ↔ **global**]
            ↓
[**model-specific** ↔ **model-agnostic**]
            ↓
[importância ≠ **efeito causal**]
```

## 10.3. Núcleo Técnico

### 10.3.1. Atribuição de Atributos

```text
[**SHAP**: f(x) = φ_0 + Σ φ_j · custo exponencial]
                       ↓
[**permutação**: I_j = M_orig − M_perm(j) · correlação]
                       ↓
[redes → gradiente (**Integrated Gradients**)]
```

### 10.3.2. Surrogates, Exemplos e Contrafactuais

```text
[**LIME**: g(x) ≈ f(x) local, ≠ global]
                   ↓
[**contrafactual**: menor mudança → y_desejado (idade)]
```

### 10.3.3. Avaliação das Explicações

```text
[plausível ≠ **fiel** (+ estável, compreensível)]
             ↓
[fidelidade × **simplicidade**]
             ↓
[**3 formas** de avaliação]
```

### 10.3.4. Uso das Explicações

```text
[desenvolvimento: revela o que a **métrica** esconde]
                   ↓
[decisão: mais confiança ≠ confiança **calibrada**]
                   ↓
[**auditoria** · investigação de erros]
```

## 10.4. Limitações, Trade-offs e Desafios Atuais

```text
[explicar **modelo** ≠ fenômeno → revela **atalhos**]
                    ↓
[post hoc frágil · métodos **discordam**]
                    ↓
[não corrige → preferir **interpretável**]
```

## 10.5. Conclusão

```text
[XAI > gerar explicações: **4 ações**]
                 ↓
[boa explicação: **3 qualidades**]
```
