# Ponto 1 — Processamento de Dados em Larga Escala: Armazenamento e Gerenciamento Distribuído de Dados

## 1.1. Introdução e Delimitação do Problema

```text
[**Vertical** → 3 limites]
             ↓
[**Horizontal** → solução]
             ↓
[rede + **falhas parciais** → 4 propriedades em risco]
```

## 1.2. Fundamentos e Relevância

```text
[**visão lógica única**, sem ganho automático]
                  ↓
[**particionamento** + **replicação**]
                  ↓
[falhas = condição normal → **GFS**]
```

## 1.3. Núcleo Técnico

### 1.3.1. Particionamento e Distribuição

```text
[**Range** (localidade) ↔ **Hash** (equilíbrio)]
                      ↓
[dados equilibrados ≠ **carga** equilibrada]
                      ↓
[rebalanceamento → **consistent hashing** (anel)]
```

### 1.3.2. Replicação e Tolerância a Falhas

```text
[**síncrona** ↔ **assíncrona**: garantia × latência]
                      ↓
[**failover** sem consenso → **split-brain**]
                      ↓
[**domínios de falha** + detecção → disponibilidade]
```

### 1.3.3. Consistência, Disponibilidade e Quóruns

```text
[**linearizável** ↔ **eventual**]
                ↓
[partição → **CAP** · sem partição → **PACELC**]
                ↓
[**R + W > N** → leitura e escrita se sobrepõem]
                ↓
[várias partições → **2PC** → bloqueio]
```

### 1.3.4. Modelos e Arquiteturas

```text
[mesmos mecanismos → GFS · **Bigtable** · **Dynamo** · objetos]
                           ↓
[**shared-nothing** · separar computação/armazenamento]
```

## 1.4. Limitações, Trade-offs e Desafios Atuais

```text
[sem arquitetura **universal** → 4 compromissos]
                   ↓
[**códigos de apagamento** → custo de reconstrução]
                   ↓
[**workload** decide: banco ↔ catálogo]
```

## 1.5. Conclusão

```text
[particionar + replicar → custo de **coordenar**]
              ↓
[**consistência** sob medida]
```
