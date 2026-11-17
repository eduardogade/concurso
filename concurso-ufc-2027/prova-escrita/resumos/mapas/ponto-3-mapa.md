# Ponto 3 — Processamento de Dados em Larga Escala: Processamento de Fluxos e Arquiteturas de Dados

## 3.1. Introdução e Delimitação do Problema

```text
[**fluxo** ↔ **batch**]
           ↓
[atraso · desordem · estado · falhas → **correção**]
           ↓
[**4 eixos**: tempo · estado · garantias · armazenamento]
```

## 3.2. Fundamentos e Relevância

```text
[**bounded** ↔ **unbounded**]
              ↓
[**latência** · **throughput**]
              ↓
[particionar: + throughput, − **ordem global**]
```

## 3.3. Núcleo Técnico

### 3.3.1. Tempo, Janelas e Watermarks

```text
[**event time** ≠ processing time]
                 ↓
[**janelas** (3 tipos) · modelo **Dataflow**]
                 ↓
[**watermark** = estimativa → latência × completude × estado]
```

### 3.3.2. Estado, Recuperação e Semântica de Processamento

```text
[**stateful**: (s_{t+1}, y_t) = f(s_t, x_t)]
                    ↓
[falha → **checkpoint** + replay (Flink)]
                    ↓
[**exactly-once** = efeito no estado ≠ entrega]
```

### 3.3.3. Logs Distribuídos e Arquiteturas Orientadas a Eventos

```text
[**Kafka**: log desacopla produtor ↔ consumidor]
                   ↓
[**offset** → replay · ordem por partição]
                   ↓
[**log** ≠ **motor** de processamento]
```

### 3.3.4. Integração Batch/Streaming e Arquiteturas de Dados

```text
[**Lambda**: 2 camadas → duplicação] ↔ [**Kappa**: recomputa por replay]
             ↓
[data lake → **lakehouse**]
```

## 3.4. Limitações, Trade-offs e Desafios Atuais

```text
[garantias fortes custam → **menor complexidade**]
                       ↓
[λ_produção > λ_consumo → **backlog** → backpressure]
                       ↓
[desacoplar ≠ dispensar **contratos de dados**]
```

## 3.5. Conclusão

```text
[dados em **movimento** + dados **persistidos**]
                        ↓
[**garantias** exigidas decidem, não a novidade]
```
