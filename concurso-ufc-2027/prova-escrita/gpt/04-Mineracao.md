# Ponto 3 — Processamento de Dados em Larga Escala: Processamento de Fluxos e Arquiteturas de Dados

## 3.1. Introdução e Delimitação do Problema

O processamento de fluxos trata dados como uma sequência contínua de eventos, potencialmente não delimitada, em contraste com o processamento *batch*, que opera sobre conjuntos finitos e previamente disponíveis.

Em larga escala, o problema não é apenas processar eventos rapidamente, mas produzir resultados corretos quando os dados chegam continuamente, atrasados ou fora de ordem, exigem manutenção de estado e precisam sobreviver a falhas.

Por isso, processamento de fluxos e arquiteturas de dados devem ser analisados conjuntamente, articulando **tempo, estado, garantias de processamento, comunicação e armazenamento**.

## 3.2. Fundamentos e Relevância

Dados *bounded* possuem início e fim definidos; dados *unbounded* representam fluxos potencialmente contínuos.

*Batch* e *streaming* não são alternativas excludentes: o primeiro é adequado a recomputações globais; o segundo, a aplicações que exigem atualização contínua e baixa latência, em geral de forma incremental.

Conceitualmente, um evento percorre a cadeia:

```text
FONTE → INGESTÃO → FLUXO → PROCESSAMENTO → ESTADO/SAÍDA → SERVING
```

**Latência** mede o tempo entre a ocorrência e a disponibilização do resultado; **throughput**, a quantidade de eventos processados por unidade de tempo.

Particionar o fluxo amplia o paralelismo, mas em geral preserva a ordenação apenas dentro de cada partição.

## 3.3. Núcleo Técnico

### 3.3.1. Tempo, Janelas e Watermarks

**Event time** é o instante em que o fato ocorre; **processing time**, o relógio do sistema quando o evento é processado.

Buffers, falhas e atrasos de rede fazem eventos chegarem fora de ordem, tornando essa distinção fundamental.

Como um fluxo não delimitado pode nunca terminar, agregações exigem **janelas**: *tumbling* (intervalos fixos não sobrepostos), *sliding* (com sobreposição) e *session* (períodos de atividade separados por inatividade).

O modelo Dataflow [1] organiza o problema em três perguntas:

- **windowing:** quais eventos pertencem à mesma agregação;
- **watermark:** até onde se estima que o fluxo tenha avançado em *event time*;
- **trigger:** quando um resultado deve ser emitido.

Um watermark é uma estimativa de progresso, não uma garantia: eventos tardios podem exigir atualização posterior do resultado. Surge o compromisso entre **latência, completude e custo de manutenção de estado**.

### 3.3.2. Estado, Recuperação e Semântica de Processamento

Muitas operações são **stateful**: o resultado depende do evento atual e de informação acumulada, como contadores, janelas ou estado por chave:

\[
(s_{t + 1},y_{t}) = f(s_{t},x_{t})
\]

em que \(x_{t}\) é o evento, \(s_{t}\) o estado corrente, \(s_{t + 1}\) o novo estado e \(y_{t}\) a saída.

Para tolerar falhas, combinam-se fontes reprocessáveis, **checkpoints consistentes** e **replay** [2]: o sistema restaura um checkpoint e reprocessa os eventos posteriores.

Daí decorrem garantias distintas: **at-most-once** pode perder eventos; **at-least-once** evita perdas, mas admite duplicações; **exactly-once** garante que o efeito lógico equivalha ao processamento de cada evento uma única vez.

Retransmissões físicas podem ocorrer, desde que idempotência, deduplicação e coordenação de estado impeçam efeitos duplicados; para garantias *end-to-end*, o *sink* também deve ser idempotente ou transacional.

### 3.3.3. Logs Distribuídos e Arquiteturas Orientadas a Eventos

Arquiteturas orientadas a eventos desacoplam produtores e consumidores por meio de brokers ou logs distribuídos.

No modelo de log exemplificado pelo Kafka [3], eventos são anexados sequencialmente em partições, o que permite paralelismo, retenção durável, *replay* e múltiplos consumidores independentes.

A ordenação é preservada dentro de uma partição, não entre partições: um trade-off entre **ordenação global e escalabilidade**. O broker transporta e retém eventos, mas não substitui a engine de processamento, responsável por agregações, *joins* e estado.

### 3.3.4. Integração Batch/Streaming e Arquiteturas de Dados

A **Lambda Architecture** [4] mantém uma camada *batch*, que recomputa sobre o histórico, e uma camada de velocidade, de baixa latência; combina resposta rápida e recomputação completa ao custo de duplicar lógica, infraestrutura e manutenção.

A **Kappa Architecture** elimina essa duplicação usando o *replay* de um log durável como caminho principal, embora análises globais extensas possam continuar mais adequadas ao *batch*.

Abordagens recentes tratam dados delimitados e não delimitados sob modelos compatíveis: **data lakes** oferecem armazenamento histórico escalável, e arquiteturas **lakehouse** acrescentam a essa flexibilidade gerenciamento de esquema, governança e consultas eficientes.

## 3.4. Limitações, Trade-offs e Desafios Atuais

Não existe arquitetura universalmente superior. Baixa latência pode reduzir a completude quando eventos tardios ainda não chegaram; aceitar maior *lateness* prolonga a preservação de estado.

Garantias fortes exigem mais checkpoints, coordenação e transações; retenção prolongada facilita *replay* e auditoria, mas aumenta armazenamento e governança.

Desequilíbrios sustentados também são críticos. Se

\[
\lambda_{\text{produção}} > \lambda_{\text{consumo}},
\]

o *backlog* cresce enquanto a desigualdade persistir: buffers absorvem variações temporárias, mas não um déficit permanente de capacidade, que exige *backpressure* ou elasticidade.

Por fim, desacoplamento não elimina contratos de dados: evolução de esquemas, qualidade, *lineage* e observabilidade ganham importância com o número de produtores e consumidores.

A arquitetura deve possuir **o menor grau de complexidade capaz de satisfazer as garantias do workload**.

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

Arquiteturas de dados em larga escala precisam integrar dados em movimento e dados persistidos, conciliando temporalidade, paralelismo, tolerância a falhas e governança. A escolha entre *batch*, *streaming* ou modelos híbridos deve decorrer das garantias exigidas pela aplicação, e não da adoção de tecnologias mais recentes.

## Referências

[1] AKIDAU, T. et al. PVLDB. 2015.
[2] CARBONE, P. et al. PVLDB. 2017.
[3] KREPS, J. et al. NetDB. 2011.
[4] MARZ, N. et al. Manning. 2015.
