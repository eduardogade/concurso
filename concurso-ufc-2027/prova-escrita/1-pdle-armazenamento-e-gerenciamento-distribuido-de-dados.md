
# Ponto 1 — Processamento de Dados em Larga Escala: Armazenamento e Gerenciamento Distribuído de Dados

## 1.1. Fundamentos, Motivação e Modelo do Problema

O crescimento do volume de dados e da demanda por acesso pode tornar inadequado o armazenamento em um único nó, não apenas por limitações de capacidade, mas também de desempenho, disponibilidade e escalabilidade.

Embora a escalabilidade vertical amplie os recursos de uma única máquina, ela possui limites físicos e econômicos; portanto, sistemas de larga escala frequentemente recorrem à escalabilidade horizontal, distribuindo dados e responsabilidades entre múltiplos nós interconectados.

Um sistema de armazenamento distribuído deve, assim, organizar e gerenciar esses recursos como um conjunto coerente, abstraindo da aplicação parte de sua localização física.

A distribuição, contudo, não produz escalabilidade ou tolerância a falhas automaticamente.

Ao substituir um sistema centralizado por múltiplos nós comunicando-se por rede, surgem novos problemas, como latência de comunicação, falhas parciais, coordenação e manutenção de uma visão consistente dos dados.

Em larga escala, a ocorrência de falhas de componentes deve ser tratada como condição normal de projeto, e não como evento excepcional.

Consequentemente, arquiteturas distribuídas precisam combinar mecanismos de distribuição, redundância e gerenciamento capazes de sustentar capacidade, desempenho e disponibilidade à medida que o sistema cresce.

## 1.2. Particionamento, Sharding e Distribuição dos Dados

A escalabilidade horizontal do armazenamento depende de mecanismos de particionamento que dividam o conjunto de dados em subconjuntos distribuíveis entre diferentes nós. No particionamento horizontal, frequentemente denominado sharding, uma chave de partição determina a localização lógica de cada registro. A estratégia escolhida afeta diretamente balanceamento, localidade e custo de acesso: o particionamento por intervalos preserva a ordenação das chaves e favorece consultas contíguas, mas pode criar partições desbalanceadas e hotspots; o particionamento por hash tende a distribuir chaves mais uniformemente, ao custo de perder sua localidade natural.

Um esquema adequado deve considerar não apenas o volume armazenado, mas também a distribuição da carga, pois balanceamento de dados não implica necessariamente balanceamento de acessos. Mudanças na composição do cluster também exigem rebalanceamento, com movimentação de partições e consequente custo de rede e I/O. Técnicas como consistent hashing reduzem o remapeamento provocado pela entrada ou saída de nós, associando chaves e recursos a um espaço de identificadores e permitindo escalabilidade incremental. Assim, o particionamento constitui um compromisso entre distribuição uniforme, localidade, flexibilidade de expansão e custo de redistribuição.

## 1.3. Replicação, Disponibilidade e Tolerância a Falhas

Além do particionamento, sistemas de armazenamento distribuído empregam replicação para manter múltiplas cópias de dados ou partições em nós distintos, aumentando disponibilidade, durabilidade e tolerância a falhas. Enquanto o particionamento distribui capacidade, a replicação introduz redundância. Seu benefício depende, contudo, da distribuição das cópias por domínios de falha suficientemente independentes e da existência de mecanismos capazes de detectar falhas, redirecionar requisições e restaurar réplicas perdidas.

A coordenação das réplicas envolve compromissos entre desempenho e garantias de atualização. Na replicação síncrona, a confirmação de uma escrita pode depender da persistência em múltiplos nós, aumentando as garantias imediatas ao custo de maior latência; na replicação assíncrona, a confirmação antecipada reduz a latência, mas permite períodos de divergência entre cópias. Arquiteturas leader–follower centralizam a ordenação das escritas em um líder e utilizam failover em caso de falha, enquanto outros modelos admitem coordenação sem um único líder. Assim, embora a replicação aumente a resiliência do armazenamento, ela introduz o problema fundamental de manter uma visão coerente dos dados entre réplicas potencialmente atrasadas, indisponíveis ou isoladas pela rede.

## 1.4. Consistência, Disponibilidade e Trade-Offs do Gerenciamento Distribuído

A replicação introduz a necessidade de definir quais estados podem ser observados quando diferentes cópias recebem atualizações em momentos distintos. Modelos de consistência especificam essas garantias. Em uma garantia forte como a linearizabilidade, cada operação deve parecer ocorrer atomicamente sobre uma única cópia lógica, respeitando a precedência temporal das operações concluídas. Modelos mais fracos reduzem a necessidade de coordenação imediata; na consistência eventual, por exemplo, réplicas podem divergir temporariamente, mas devem convergir quando cessam novas atualizações. A escolha do modelo deve refletir as invariantes da aplicação, pois garantias mais fortes geralmente exigem maior coordenação e podem aumentar latência ou reduzir disponibilidade durante falhas.

Essa tensão é formalizada pelo teorema CAP, conjecturado por Brewer e demonstrado por Gilbert e Lynch: na presença de uma partição de rede, um serviço distribuído não pode garantir simultaneamente consistência linearizável e disponibilidade de todas as operações. Portanto, CAP não deve ser interpretado simplesmente como uma escolha permanente de “dois entre três”; quando ocorre uma partição, arquiteturas podem preservar consistência recusando ou adiando operações em parte do sistema, ou privilegiar disponibilidade aceitando divergência temporária e posterior reconciliação. Quóruns de leitura e escrita constituem um mecanismo para modular essas garantias. Assim, o gerenciamento distribuído de dados envolve escolher explicitamente compromissos entre consistência, disponibilidade e desempenho conforme os requisitos semânticos e operacionais do sistema.

## 1.5. Modelos de Armazenamento Distribuído, Arquiteturas e Síntese das Escolhas

Os mecanismos de particionamento, replicação e consistência são combinados de formas distintas conforme a abstração e o padrão de acesso oferecidos pelo sistema. Sistemas de arquivos distribuídos, como o Google File System, dividem arquivos em unidades distribuídas e replicadas, buscando elevado throughput e tolerância a falhas; bancos e stores distribuídos oferecem acesso mais granular a dados estruturados, como ilustram Bigtable e o key-value store Dynamo. Já o armazenamento de objetos organiza dados e metadados por identificadores e tornou-se uma base importante para repositórios de grande escala e data lakes. Esses modelos não determinam, por si sós, uma única política de consistência ou replicação: tais garantias dependem do projeto do sistema.

Consequentemente, a escolha de uma arquitetura de armazenamento distribuído deve partir do workload e de suas garantias, considerando volume e crescimento dos dados, padrão de acesso, latência e throughput, disponibilidade, durabilidade, consistência e custo. Arquiteturas shared-nothing e, mais recentemente, a separação entre computação e armazenamento favorecem escalabilidade horizontal e evolução independente dos recursos. Técnicas adicionais, como códigos de apagamento, podem reduzir o custo da redundância para determinados dados. Assim, não há uma solução universalmente superior: o gerenciamento distribuído consiste em combinar distribuição, redundância, coordenação e recuperação de acordo com as propriedades exigidas pela aplicação.

## Texto Final

# Ponto 1 — Processamento de Dados em Larga Escala: Armazenamento e Gerenciamento Distribuído de Dados

## 1. Introdução e Delimitação do Problema

O crescimento do volume de dados e da demanda por acesso pode tornar inadequado o armazenamento em um único nó, não apenas por limitações de capacidade, mas também de desempenho, disponibilidade e escalabilidade. A escalabilidade vertical amplia recursos de uma máquina, porém encontra limites físicos e econômicos; sistemas de larga escala recorrem, portanto, à escalabilidade horizontal, distribuindo dados e responsabilidades entre múltiplos nós interconectados. O desafio passa a ser gerenciar dados de forma escalável, disponível, durável e coerente diante de comunicação pela rede e falhas parciais.

## 2. Fundamentos e Relevância

Um sistema de armazenamento distribuído organiza dados sobre múltiplos nós, oferecendo à aplicação uma abstração lógica coerente apesar da distribuição física. Essa distribuição não produz automaticamente escalabilidade ou tolerância a falhas: introduz latência, coordenação, localização dos dados, redistribuição de carga e recuperação.

Dois mecanismos estruturam o problema:

- **particionamento** distribui dados distintos entre nós, ampliando capacidade e paralelismo;
- **replicação** mantém cópias, introduzindo redundância para disponibilidade, durabilidade e tolerância a falhas.

Em larga escala, falhas devem ser tratadas como condição normal de projeto, princípio exemplificado pelo Google File System de Ghemawat, Gobioff e Leung (2003).

## 3. Núcleo Técnico

### 3.1. Particionamento e Distribuição

No particionamento horizontal, ou *sharding*, uma chave de partição determina a localização lógica dos registros. Particionamento por intervalos preserva ordenação e favorece consultas contíguas, mas pode produzir *skew* e *hotspots*; particionamento por hash tende a distribuir chaves mais uniformemente, sacrificando localidade.

A escolha deve considerar volume e padrão de acesso, pois balanceamento de dados não implica balanceamento de carga. Alterações no cluster exigem rebalanceamento, com custo de rede e I/O. Técnicas como *consistent hashing*, empregadas em arquiteturas inspiradas no Dynamo de DeCandia et al. (2007), reduzem o remapeamento causado pela entrada ou saída de nós e favorecem escalabilidade incremental.

### 3.2. Replicação e Tolerância a Falhas

A replicação mantém cópias de uma partição em nós distintos. Seu benefício depende do fator de replicação e da distribuição das cópias entre domínios de falha independentes. Replicação síncrona pode exigir confirmação de múltiplos nós, aumentando garantias imediatas ao custo de latência; replicação assíncrona reduz latência, mas permite divergência temporária.

Arquiteturas *leader–follower* centralizam a ordenação das escritas em um líder e utilizam *failover*; modelos sem líder admitem operações em múltiplas réplicas. Redundância, porém, só se converte em disponibilidade quando o sistema detecta falhas, redireciona requisições e restaura réplicas perdidas.

### 3.3. Consistência, Disponibilidade e Quóruns

Múltiplas réplicas exigem modelos de consistência que determinem quais estados podem ser observados. Na linearizabilidade, formalizada por Herlihy e Wing (1990), cada operação deve parecer ocorrer atomicamente sobre uma única cópia lógica e respeitar a precedência temporal das operações concluídas. Na consistência eventual, réplicas podem divergir temporariamente, mas convergem quando cessam novas atualizações.

O teorema CAP, formalizado por Gilbert e Lynch (2002), estabelece que, diante de uma partição de rede, não se pode garantir simultaneamente consistência linearizável e disponibilidade de todas as operações. Logo, CAP não significa simplesmente “escolher dois de três”: durante uma partição, preserva-se consistência recusando ou adiando operações, ou privilegia-se disponibilidade aceitando divergência temporária e posterior reconciliação.

Quóruns de leitura e escrita modulam essas garantias. Para \(N\) réplicas, uma condição clássica é:

\[
R + W > N
\]

em que \(R\) é o número de réplicas consultadas na leitura e \(W\) o número de confirmações exigidas na escrita; a sobreposição resultante ajuda a coordenar versões, embora as garantias finais dependam do protocolo completo.

### 3.4. Modelos e Arquiteturas

Os mecanismos anteriores aparecem em diferentes abstrações. Sistemas de arquivos distribuídos, como o GFS, distribuem e replicam unidades de arquivos para obter *throughput* e tolerância a falhas. Bigtable, de Chang et al. (2006), exemplifica armazenamento distribuído de dados estruturados em escala muito grande; Dynamo exemplifica um *key-value store* altamente disponível. Armazenamento de objetos organiza dados e metadados por identificadores e constitui base comum para grandes repositórios e *data lakes*. Arquiteturas *shared-nothing* e a separação entre computação e armazenamento favorecem escalabilidade horizontal e evolução independente dos recursos.

## 4. Limitações, Trade-offs e Desafios Atuais

Não existe arquitetura universalmente superior. O projeto deve compatibilizar **localidade versus balanceamento**, **redundância versus custo**, **consistência versus disponibilidade sob partições** e **garantias fortes versus latência e coordenação**. Devem ainda ser considerados padrão de acesso, *throughput*, durabilidade, domínios de falha e custo operacional. Para grandes volumes, códigos de apagamento podem reduzir o *overhead* da replicação integral ao custo de maior complexidade de reconstrução.

Assim, a arquitetura deve ser guiada pelas invariantes e pelo *workload*: requisitos distintos justificam combinações distintas de particionamento, replicação, consistência e recuperação.

## 5. Conclusão

A lógica do armazenamento distribuído pode ser sintetizada como:

```text
DATASET
   ↓
PARTICIONAMENTO
   ↓
REPLICAÇÃO
   ↓
CONSISTÊNCIA / QUÓRUNS
   ↓
RECUPERAÇÃO E REBALANCEAMENTO
   ↓
ABSTRAÇÃO DE ARMAZENAMENTO
```

O objetivo é combinar escala, desempenho, disponibilidade, durabilidade e consistência de acordo com as necessidades da aplicação.

## Referências

[1] GHEMAWAT, S.; GOBIOFF, H.; LEUNG, S.-T. *The Google File System*. 2003.
[2] HERLIHY, M.; WING, J. *Linearizability: A Correctness Condition for Concurrent Objects*. 1990.
[3] GILBERT, S.; LYNCH, N. *Brewer's Conjecture and the Feasibility of Consistent, Available, Partition-Tolerant Web Services*. 2002.
[4] CHANG, F. et al. *Bigtable: A Distributed Storage System for Structured Data*. 2006.
[5] DECANDIA, G. et al. *Dynamo: Amazon's Highly Available Key-value Store*. 2007.
