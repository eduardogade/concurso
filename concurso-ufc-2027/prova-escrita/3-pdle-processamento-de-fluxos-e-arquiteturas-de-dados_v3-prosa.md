# Ponto 3 — Processamento de Dados em Larga Escala: Processamento de Fluxos e Arquiteturas de Dados

## 3.1. Introdução e Delimitação do Problema

O processamento de fluxos trata os dados como uma sequência contínua e potencialmente ilimitada de eventos, enquanto o processamento *batch* opera sobre conjuntos finitos já disponíveis.

Em larga escala, o problema não é apenas processar rápido, mas produzir resultados corretos quando eventos chegam atrasados ou fora de ordem, exigem estado e precisam sobreviver a falhas. Por isso, fluxos e arquiteturas de dados devem ser analisados juntos, articulando **tempo, estado, garantias de processamento e armazenamento**.

## 3.2. Fundamentos e Relevância

Dados *bounded* têm início e fim; dados *unbounded* chegam indefinidamente. *Batch* e *streaming* não se excluem: o primeiro serve a recomputações completas sobre o histórico; o segundo, a resultados atualizados continuamente, com baixa latência.

A **latência** mede o tempo entre a ocorrência do evento e o resultado; o **throughput**, os eventos processados por unidade de tempo. Particionar o fluxo amplia o throughput, mas a ordem em geral só é garantida dentro de cada partição.

## 3.3. Núcleo Técnico

### 3.3.1. Tempo, Janelas e Watermarks

O **event time** é o instante em que o fato ocorreu; o **processing time**, o momento em que o sistema o processa. Como atrasos de rede e falhas fazem eventos chegarem fora de ordem, agregar pelo processing time pode atribuir um evento ao intervalo errado.

Um fluxo ilimitado nunca termina; por isso, agregações usam **janelas**: *tumbling* (intervalos fixos e disjuntos), *sliding* (sobrepostos, como "os últimos 5 minutos") e *session* (atividade separada por inatividade).

O modelo Dataflow¹ articula três mecanismos:

- **windowing:** quais eventos pertencem à mesma agregação;
- **watermark:** até onde se estima que o fluxo avançou em event time;
- **trigger:** quando emitir ou atualizar um resultado.

O watermark é uma estimativa, não uma garantia: um evento tardio pode exigir a correção de um resultado já emitido. Surge o compromisso entre **latência, completude e custo de estado**: esperar mais aumenta a completude, mas atrasa resultados e retém mais estado.

### 3.3.2. Estado, Recuperação e Semântica de Processamento

Muitas operações são **stateful**: o resultado depende do evento atual e de informação acumulada, como contadores ou janelas abertas:

\[
(s_{t + 1},y_{t}) = f(s_{t},x_{t})
\]

em que \(x_{t}\) é o evento, \(s_{t}\) o estado corrente, \(s_{t + 1}\) o novo estado e \(y_{t}\) a saída.

Para que esse estado sobreviva a falhas, combinam-se fontes que permitem reler eventos, **checkpoints** consistentes e **replay**: o sistema restaura o último checkpoint e reprocessa os eventos posteriores, como no Apache Flink².

Daí decorrem três garantias: **at-most-once** pode perder eventos; **at-least-once** não perde, mas pode duplicar; **exactly-once** garante que o *efeito* sobre o estado equivalha a processar cada evento uma vez, ainda que ele seja reprocessado. Para valer de ponta a ponta, o *sink* deve ser idempotente ou transacional.

### 3.3.3. Logs Distribuídos e Arquiteturas Orientadas a Eventos

Arquiteturas orientadas a eventos desacoplam produtores e consumidores. No **log distribuído** do Kafka³, eventos são anexados em sequência a partições e retidos de forma durável; cada consumidor guarda sua posição (*offset*), o que permite vários consumidores independentes e *replay*, exatamente o que a recuperação exige.

A ordem vale dentro de cada partição, não entre partições: troca-se ordenação global por escalabilidade. O log transporta e retém eventos, mas não substitui o motor de processamento (Flink, Spark Structured Streaming), responsável por janelas, *joins* e estado.

### 3.3.4. Integração Batch/Streaming e Arquiteturas de Dados

A **Lambda Architecture** mantém uma camada *batch*, que recomputa sobre o histórico, e uma camada de velocidade, de baixa latência: combina rapidez e correção, mas duplica lógica e manutenção.

A **Kappa Architecture** elimina a duplicação: tudo é fluxo, e recomputar é fazer *replay* do log com o código novo. **Data lakes** oferecem armazenamento histórico escalável, e arquiteturas **lakehouse** acrescentam transações ACID, controle de esquema e consultas eficientes.

## 3.4. Limitações, Trade-offs e Desafios Atuais

Não existe arquitetura universalmente superior. Garantias fortes exigem mais checkpoints e coordenação; retenção longa facilita *replay*, mas custa armazenamento.

Desequilíbrios sustentados também são críticos. Se

\[
\lambda_{\text{produção}} > \lambda_{\text{consumo}},
\]

o *backlog* cresce enquanto a desigualdade persistir: *buffers* absorvem picos, mas um déficit permanente exige *backpressure* (desacelerar a fonte) ou elasticidade (mais consumidores).

Desacoplar, por fim, não dispensa contratos de dados e controle da evolução de esquemas. A arquitetura deve ter **o menor grau de complexidade capaz de satisfazer as garantias exigidas**.

## 3.5. Conclusão

Em síntese:

```text
EVENTOS
↓
INGESTÃO / LOG
↓
TEMPO / JANELAS / WATERMARKS
↓
ESTADO / CHECKPOINT / REPLAY
↓
GARANTIAS DE PROCESSAMENTO
↓
STORAGE / SERVING
```

Arquiteturas de dados em larga escala integram dados em movimento e persistidos, conciliando tempo, estado e tolerância a falhas. A escolha entre *batch*, *streaming* ou modelos híbridos deve decorrer das garantias exigidas, não da tecnologia mais recente.

## Referências

1. AKIDAU, T. et al. The dataflow model [...]. **Proceedings of the VLDB Endowment**, 2015.
2. CARBONE, P. et al. State management in Apache Flink [...]. **Proceedings of the VLDB Endowment**, 2017.
3. KREPS, J.; NARKHEDE, N.; RAO, J. Kafka: a distributed messaging system for log processing. In: NetDB, 2011.
