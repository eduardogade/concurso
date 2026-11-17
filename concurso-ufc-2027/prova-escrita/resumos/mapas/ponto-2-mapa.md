# Ponto 2 — Processamento de Dados em Larga Escala: Processamento Paralelo e Distribuído em Larga Escala

## 2.1. Introdução e Delimitação do Problema

```text
[**dividir o trabalho**: intra-nó ↔ entre nós]
                     ↓
[decompor → distribuir → coordenar → recuperar]
                     ↓
[trabalho útil > **custo da distribuição**]
```

## 2.2. Fundamentos e Relevância

```text
[paralelismo de **dados** ↔ de **tarefas**]
                     ↓
[**Amdahl**: S(p) ≤ 1/s (10% serial → máx. 10×)]
                     ↓
[problema cresce → **strong** ↔ **weak** scaling]
```

## 2.3. Núcleo Técnico

### 2.3.1. Decomposição, Granularidade e Balanceamento

```text
[**granularidade**: tarefas grandes ↔ pequenas]
                      ↓
[trabalho ≠ dados: **skew** → **stragglers**]
                      ↓
[escalonamento dinâmico + **execução especulativa**]
```

### 2.3.2. Comunicação, Sincronização e Localidade

```text
[T_total = comp + **comm** + **sync** + overhead]
                ↓
[**localidade** ↔ balanceamento]
                ↓
[**shuffle** é o mais caro → agregação local]
```

### 2.3.3. MapReduce e Modelos de Execução Distribuída

```text
[**map** → shuffle → **reduce** (contar palavras)]
                    ↓
[runtime embute **tolerância a falhas**]
                    ↓
[grava em **disco** → batch robusto, iterativo lento]
```

### 2.3.4. DAGs, Reutilização e Recuperação

```text
[**Spark**: memória + avaliação preguiçosa → DAG]
                      ↓
[dependência estreita ↔ **larga** → estágios]
                      ↓
[**linhagem**: recomputar × replicar × checkpoint]
```

## 2.4. Limitações, Trade-offs e Desafios Atuais

```text
[distribuir ≠ escala **linear**]
                ↓
[a **cauda** importa, não só a média]
                ↓
[abstração mantém **custo físico** (agrupar por chave)]
```

## 2.5. Conclusão

```text
[escalar ≠ **somar nós**]
            ↓
[MapReduce e Spark não eliminam **custos**]
```
