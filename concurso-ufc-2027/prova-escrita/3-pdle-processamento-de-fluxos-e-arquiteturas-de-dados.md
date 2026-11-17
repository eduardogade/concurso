
# Ponto 3 — Processamento de Dados em Larga Escala: Processamento de Fluxos e Arquiteturas de Dados

## 3.1. Fundamentos: Batch, Streaming, Eventos e Dados em Movimento

O processamento de fluxos diferencia-se do processamento batch principalmente pela natureza temporal dos dados. Enquanto cargas batch operam naturalmente sobre conjuntos delimitados (*bounded data*), fluxos podem representar sequências potencialmente não delimitadas de eventos (*unbounded data*) que precisam ser processadas à medida que chegam. Um evento registra uma ocorrência relevante e é produzido por uma fonte, ingerido pela arquitetura e consumido por uma ou mais aplicações; assim, o processamento deixa de depender da existência prévia de um dataset completo e passa a atualizar continuamente resultados e estado.

Essa mudança introduz requisitos próprios de larga escala. Latência e throughput tornam-se simultaneamente relevantes, e streams podem ser particionados para ampliar paralelismo, ao custo de tornar mais difícil preservar uma ordem global. Eventos também podem chegar atrasados ou fora da ordem em que ocorreram, enquanto operadores stateful precisam manter informação entre eventos e recuperá-la após falhas. Dessa forma, batch e streaming devem ser vistos como modelos complementares: o primeiro é apropriado a conjuntos delimitados e processamento global, enquanto o segundo atende aplicações que exigem atualização contínua e baixa latência sobre dados em movimento.

---

> Mnemonics



---

## 3.2. Tempo, Janelas e Watermarks

Em fluxos distribuídos, o tempo associado ao evento pode diferir do instante em que ele é processado. **Event time** representa quando o fato ocorreu no domínio da aplicação, enquanto **processing time** corresponde ao relógio do sistema durante seu processamento. Essa distinção é essencial porque atrasos de rede, buffers e falhas fazem eventos chegarem fora de ordem. Para realizar agregações sobre fluxos não delimitados, empregam-se janelas temporais: janelas fixas ou *tumbling* dividem o tempo em intervalos não sobrepostos; *sliding windows* admitem sobreposição; e *session windows* delimitam grupos de atividade separados por períodos de inatividade.

Como não é possível esperar indefinidamente pela chegada de todos os eventos, sistemas de streaming utilizam **watermarks** como estimativas do progresso em event time. Quando o watermark ultrapassa o final de uma janela, o sistema pode emitir seu resultado, embora eventos com timestamps anteriores ainda possam chegar tardiamente. Triggers determinam quando resultados intermediários ou finais são produzidos, permitindo emissões antecipadas e correções posteriores. Assim, windowing define **quais eventos** são agregados, o watermark estima **até onde o fluxo progrediu**, e os triggers determinam **quando emitir resultados**, estabelecendo um compromisso entre baixa latência, completude e custo de manutenção de estado.

---

> Mnemonics

---

## 3.3. Estado, Entrega e Semântica de Processamento

Muitas operações sobre fluxos são **stateful**: seu resultado depende não apenas do evento corrente, mas também de estado acumulado, como contadores, janelas ou informações associadas a uma chave. Para que esse estado sobreviva a falhas, engines de streaming combinam fontes reprocessáveis, checkpoints consistentes e replay. Após uma falha, o estado pode ser restaurado a partir de um checkpoint e eventos posteriores reexecutados, tornando a recuperação parte do próprio modelo de processamento.

Essa reexecução introduz diferentes semânticas. Em **at-most-once**, um evento é processado no máximo uma vez, admitindo perda em determinadas falhas; em **at-least-once**, eventos são reprocessados quando necessário, evitando perda sob as garantias do sistema, mas permitindo duplicações. Já **exactly-once semantics** busca tornar o efeito lógico equivalente ao processamento de cada evento uma única vez, sem exigir necessariamente que a mensagem seja fisicamente entregue apenas uma vez. Essa propriedade pode requerer checkpoints coordenados, deduplicação ou operações idempotentes e, para garantias end-to-end, integração com sinks transacionais ou capazes de evitar efeitos duplicados. Portanto, garantias mais fortes de processamento aumentam correção e simplicidade semântica para a aplicação, mas também elevam coordenação, estado e custo de recuperação.

---

> Mnemonics

---

## 3.4. Arquiteturas Orientadas a Eventos e Integração de Dados

Arquiteturas orientadas a eventos desacoplam produtores e consumidores por meio de uma camada intermediária de ingestão e distribuição. Brokers e logs distribuídos permitem que produtores publiquem eventos sem coordenar diretamente cada consumidor e que consumidores processem esses eventos em ritmos distintos. Em um log particionado e durável, como o modelo exemplificado por Kafka, registros são anexados sequencialmente e mantidos segundo políticas de retenção; consumidores controlam seu progresso e podem realizar replay, enquanto partições ampliam throughput e paralelismo, preservando ordenação local ao custo de uma ordem global simples.

Essa camada pode alimentar múltiplos consumidores independentes ou engines de processamento stateful, que transformam, agregam e encaminham resultados para bancos, data lakes, alertas ou novos fluxos. O modelo publish/subscribe favorece fan-out e desacoplamento temporal, mas não elimina desafios de coordenação: diferenças persistentes entre taxas de produção e consumo geram backlog e exigem backpressure ou escalabilidade dos consumidores, enquanto evolução de schemas e contratos de dados precisa preservar compatibilidade. Assim, arquiteturas orientadas a eventos integram ingestão, transporte, processamento e persistência, permitindo pipelines reprocessáveis e escaláveis sem eliminar os custos de estado, retenção e governança.

---

> Mnemonics

---

## 3.5. Arquiteturas de Dados, Integração Batch/Streaming e Trade-offs

Arquiteturas modernas de dados integram processamento contínuo, processamento batch, armazenamento e serving conforme os requisitos de latência, completude e recomputação da aplicação. A **Lambda Architecture** combina uma camada batch, responsável pela recomputação sobre o histórico, com uma camada de velocidade para resultados de baixa latência; sua principal limitação é a duplicação de lógica e infraestrutura entre os dois caminhos. A **Kappa Architecture** procura reduzir essa complexidade utilizando o fluxo de eventos e o replay de um log durável como caminho principal, embora workloads fortemente orientados a análises históricas globais ainda possam beneficiar-se de processamento batch especializado.

Modelos mais recentes buscam tratar dados delimitados e não delimitados sob abstrações unificadas, enquanto data lakes e arquiteturas lakehouse aproximam armazenamento histórico escalável de recursos de governança e análise. Independentemente da implementação, permanecem trade-offs entre latência e completude, estado e custo, retenção e capacidade de replay, além de correção e overhead de coordenação. Assim, uma arquitetura de dados adequada deve integrar ingestão, processamento, persistência e serving com o menor grau de complexidade compatível com o workload e suas garantias, em vez de simplesmente acumular tecnologias.

---

> Mnemonics

---

## Texto Final

# Ponto 3 — Processamento de Dados em Larga Escala: Processamento de Fluxos e Arquiteturas de Dados

## 1. Introdução e Delimitação do Problema

O processamento de fluxos trata dados como uma sequência contínua de eventos, potencialmente não delimitada, em contraste com o processamento *batch*, que opera naturalmente sobre conjuntos finitos e previamente disponíveis. Em larga escala, o problema não consiste apenas em processar eventos rapidamente, mas em produzir resultados corretos quando os dados chegam continuamente, podem estar atrasados ou fora de ordem, exigem manutenção de estado e precisam sobreviver a falhas.

Esse cenário conecta processamento e arquitetura: eventos precisam ser ingeridos, transportados, particionados, processados e eventualmente persistidos ou disponibilizados a outros consumidores. Assim, processamento de fluxos e arquiteturas de dados devem ser analisados conjuntamente, articulando **tempo, estado, garantias de processamento, comunicação e armazenamento**.

## 2. Fundamentos e Relevância

Dados *bounded* possuem início e fim definidos; dados *unbounded* representam fluxos potencialmente contínuos. Consequentemente, *batch* e *streaming* não são alternativas excludentes: o primeiro é adequado a recomputações globais e cargas delimitadas, enquanto o segundo atende aplicações que exigem atualização contínua e baixa latência.

Um evento representa uma ocorrência relevante e percorre, conceitualmente, a seguinte cadeia:

```text id="j61k4v"
FONTE → INGESTÃO → FLUXO → PROCESSAMENTO → ESTADO/SAÍDA → ARMAZENAMENTO/SERVING
```

Nessa cadeia, **latência** mede o tempo entre ocorrência e disponibilização do resultado, enquanto **throughput** expressa a quantidade de eventos processados por unidade de tempo. Streams podem ser particionados para ampliar paralelismo, embora isso geralmente preserve ordenação apenas localmente por partição e torne mais difícil estabelecer uma ordem global.

O processamento contínuo também é frequentemente incremental: cada evento atualiza resultados ou estado previamente mantido, em vez de exigir recomputação completa.

## 3. Núcleo Técnico

### 3.1. Tempo, Janelas e Watermarks

Em sistemas distribuídos, o instante em que um evento ocorre pode diferir do instante em que ele é processado. **Event time** representa o tempo do fato no domínio da aplicação; **processing time**, o relógio do sistema quando o evento é efetivamente processado. Essa distinção é fundamental porque buffers, falhas e atrasos de rede podem fazer eventos chegarem fora de ordem.

Como um fluxo não delimitado pode nunca terminar, agregações requerem delimitação lógica por **janelas**. Janelas *tumbling* ou fixas dividem o tempo em intervalos não sobrepostos; *sliding windows* admitem sobreposição; e *session windows* agrupam períodos de atividade separados por intervalos de inatividade.

O modelo Dataflow, descrito por Akidau et al., organiza esse problema por meio de três perguntas complementares:

- **windowing:** quais eventos pertencem à mesma agregação;
- **watermark:** até onde se estima que o fluxo tenha avançado em *event time*;
- **trigger:** quando um resultado deve ser emitido.

Um watermark não garante que todos os eventos anteriores chegaram; ele representa uma estimativa de progresso. Eventos tardios podem, portanto, exigir atualização posterior do resultado. Surge daí um compromisso fundamental entre **latência, completude e custo de manutenção de estado**.

### 3.2. Estado, Recuperação e Semântica de Processamento

Muitas operações de streaming são **stateful**: o resultado depende do evento atual e de informação acumulada, como contadores, janelas, sessões ou estado associado a uma chave. Em termos conceituais:

\[
(s_{t+1},y_t)=f(s_t,x_t)
\]

onde \(x_t\) é o evento, \(s_t\) o estado corrente e \(s_{t+1}\) o novo estado.

Para tolerar falhas, engines de streaming combinam fontes reprocessáveis, **checkpoints consistentes** e **replay**. Após uma falha, o sistema restaura um checkpoint e reexecuta eventos posteriores, o que introduz diferentes garantias:

**At-most-once** processa um evento no máximo uma vez, podendo haver perda; **at-least-once** privilegia reexecução e evita perda sob as garantias do sistema, mas admite duplicações; **exactly-once semantics** procura garantir que o efeito lógico seja equivalente ao processamento de cada evento uma única vez.

Essa última garantia não implica necessariamente uma única entrega física. Retransmissões podem ocorrer, desde que mecanismos como idempotência, deduplicação e coordenação de estado impeçam efeitos duplicados. Para garantias *end-to-end*, a consistência também deve alcançar o *sink*, por exemplo mediante operações idempotentes ou suporte transacional.

### 3.3. Logs Distribuídos e Arquiteturas Orientadas a Eventos

Arquiteturas orientadas a eventos desacoplam produtores e consumidores mediante uma camada intermediária de ingestão e distribuição. Brokers e logs distribuídos permitem que produtores publiquem eventos sem conhecer diretamente cada consumidor e que diferentes consumidores processem o mesmo fluxo em ritmos independentes.

No modelo de log distribuído exemplificado por Kafka, eventos são anexados sequencialmente e organizados em partições. Essa organização permite:

- distribuição de armazenamento e processamento;
- aumento de throughput e paralelismo;
- retenção durável e replay;
- múltiplos consumidores independentes.

A ordenação é normalmente preservada dentro de uma partição, não necessariamente entre todas elas, produzindo um trade-off entre **ordenação global e escalabilidade**.

A retenção torna o log mais do que um mecanismo de entrega: consumidores podem recuperar progresso, reprocessar eventos históricos e reconstruir resultados. Entretanto, um broker não substitui uma engine de processamento; a primeira camada transporta e retém eventos, enquanto operadores de stream processing realizam agregações, joins, manutenção de estado e produção de novos fluxos ou dados persistidos.

### 3.4. Integração Batch/Streaming e Arquiteturas de Dados

Arquiteturas modernas combinam processamento contínuo, histórico e armazenamento segundo requisitos de latência, completude e recomputação.

A **Lambda Architecture** utiliza dois caminhos: uma camada *batch*, responsável por recomputações sobre o histórico, e uma camada de velocidade, responsável por resultados de baixa latência. Sua principal vantagem é combinar resposta rápida e recomputação completa; sua principal limitação é a duplicação de lógica, infraestrutura e manutenção.

A **Kappa Architecture** procura eliminar essa duplicação utilizando o fluxo de eventos e o replay de um log durável como caminho principal. Dados históricos são reprocessados pela mesma lógica empregada nos eventos novos. Entretanto, cargas que dependem de grandes análises globais podem continuar adequadas a processamento batch especializado.

Abordagens mais recentes procuram reduzir essa dicotomia tratando dados delimitados e não delimitados sob modelos compatíveis. Nesse contexto, **data lakes** oferecem armazenamento histórico escalável, enquanto arquiteturas **lakehouse** procuram aproximar essa flexibilidade de recursos tradicionalmente associados a ambientes analíticos, como gerenciamento de esquema, governança e suporte eficiente a consultas.

## 4. Limitações, Trade-offs e Desafios Atuais

Não existe arquitetura universalmente superior. Processamento de fluxos exige compromissos entre propriedades que frequentemente competem entre si.

Baixa latência pode reduzir completude quando eventos tardios ainda não chegaram; aceitar maior *lateness* aumenta o período durante o qual estado precisa ser preservado. Garantias fortes de processamento podem exigir mais checkpoints, coordenação e transações. Retenção prolongada facilita replay e auditoria, mas aumenta armazenamento e governança.

Diferenças sustentadas entre produção e consumo também são críticas. Se

\[
\lambda_{\text{produção}} > \lambda_{\text{consumo}},
\]

o backlog cresce enquanto essa desigualdade persistir. Buffers e logs absorvem variações temporárias, mas não eliminam déficit permanente de capacidade; *backpressure* e elasticidade devem controlar ou redistribuir essa pressão.

Por fim, desacoplamento arquitetural não elimina contratos de dados. Evolução de schemas, qualidade, *lineage*, observabilidade e governança tornam-se mais importantes à medida que aumentam produtores e consumidores. Da mesma forma, acumular brokers, engines, lakes, warehouses e serviços não constitui modernidade por si só: a arquitetura deve possuir **o menor grau de complexidade capaz de satisfazer as garantias do workload**.

## 5. Conclusão

O processamento de fluxos pode ser sintetizado pela seguinte cadeia:

```text id="of4a8e"
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
STREAM PROCESSING
   ↓
STORAGE / SERVING
   ↓
BATCH + STREAMING
```

Assim, arquiteturas de dados em larga escala precisam integrar dados em movimento e dados persistidos, conciliando temporalidade, paralelismo, tolerância a falhas e governança. A escolha entre batch, streaming ou modelos híbridos deve decorrer das garantias exigidas pela aplicação, e não simplesmente da adoção de tecnologias mais recentes.

## Referências

- AKIDAU, T. et al. *The Dataflow Model: A Practical Approach to Balancing Correctness, Latency, and Cost in Massive-Scale, Unbounded, Out-of-Order Data Processing*. 2015.
- KREPS, J.; NARKHEDE, N.; RAO, J. *Kafka: A Distributed Messaging System for Log Processing*. 2011.
- CARBONE, P. et al. Trabalhos sobre Apache Flink e processamento stateful distribuído.
- MARZ, N.; WARREN, J. Trabalhos sobre Lambda Architecture e arquiteturas de processamento de dados em larga escala.

---

## Outras Notas

