# Ponto 4 — Mineração de Dados: Descoberta de Conhecimento, Análise Exploratória de Dados, Identificação de Padrões e Anomalias

## 4.1. Introdução e Delimitação do Problema

```text
[mineração = etapa do **KDD**]
               ↓
[padrão: **4 qualidades** → decisão]
```

## 4.2. Fundamentos e Relevância

```text
[**KDD**: seleção → … → conhecimento (iterativo)]
                 ↓
[dado → padrão → **conhecimento**]
                 ↓
[detectável pode ser trivial · **espúrio** · irrelevante]
```

## 4.3. Núcleo Técnico

### 4.3.1. Preparação dos Dados e Análise Exploratória

```text
[preparação **não é neutra**]
            ↓
[**EDA** (Tukey): boxplot · **IQR** · Pearson ↔ Spearman]
            ↓
[achados = **hipóteses**]
```

### 4.3.2. Identificação e Mineração de Padrões

```text
[pão → manteiga: sup · conf · **lift > 1**]
             ↓
[padrão **global** ↔ **local**]
             ↓
[frequente ≠ **relevante**]
```

### 4.3.3. Identificação de Anomalias

```text
[desvio do esperado ≠ **erro** · 3 tipos (madrugada)]
                        ↓
[normalidade: z · IQR · **LOF** · **Isolation Forest**]
                        ↓
[alta dimensão → perde **poder discriminativo**]
```

## 4.4. Limitações, Trade-offs e Desafios Atuais

```text
[aparente ≠ válido: **múltiplas comparações**]
               ↓
[**associação** ≠ causalidade]
               ↓
[conhecimento de **domínio** (2 sentidos)]
```

## 4.5. Conclusão

```text
[padrão **robusto** ≠ artefato → conhecimento]
```
