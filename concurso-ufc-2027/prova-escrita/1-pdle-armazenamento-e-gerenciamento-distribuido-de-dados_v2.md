# Ponto 1 — Processamento de Dados em Larga Escala: Armazenamento e Gerenciamento Distribuído de Dados

## 1.1. Introdução e Delimitação do Problema

O crescimento do volume de dados e da demanda por acesso pode tornar inadequado o armazenamento em um único nó, não apenas por limitações de capacidade, mas também de desempenho, disponibilidade e escalabilidade.

A escalabilidade vertical amplia recursos de uma máquina, porém encontra limites físicos e econômicos; sistemas de larga escala recorrem, portanto, à escalabilidade horizontal, distribuindo dados e responsabilidades entre múltiplos nós interconectados.

O desafio passa a ser gerenciar dados de forma escalável, disponível, durável e coerente diante de comunicação pela rede e falhas parciais.

## 1.2. Fundamentos e Relevância

Um sistema de armazenamento distribuído organiza dados sobre múltiplos nós, oferecendo à aplicação uma abstração lógica coerente apesar da distribuição física.

Essa distribuição não produz automaticamente escalabilidade ou tolerância a falhas: introduz latência, coordenação, localização dos dados, redistribuição de carga e recuperação.

Dois mecanismos estruturam o problema:

- **particionamento** distribui dados distintos entre nós, ampliando capacidade e paralelismo;
- **replicação** mantém cópias, introduzindo redundância para disponibilidade, durabilidade e tolerância a falhas.

Em larga escala, falhas devem ser tratadas como condição normal de projeto, princípio exemplificado pelo Google File System [1].

## 1.3. Núcleo Técnico

### 1.3.1. Particionamento e Distribuição

No particionamento horizontal, ou *sharding*, uma chave de partição determina a localização lógica dos registros.

Particionamento por intervalos preserva ordenação e favorece consultas contíguas, mas pode produzir *skew* e *hotspots*; particionamento por hash tende a distribuir chaves mais uniformemente, sacrificando localidade.

A escolha deve considerar volume e padrão de acesso, pois balanceamento de dados não implica balanceamento de carga. Alterações no cluster exigem rebalanceamento, com custo de rede e I/O.

Técnicas como *consistent hashing*, empregadas em arquiteturas inspiradas no Dynamo [2], reduzem o remapeamento causado pela entrada ou saída de nós e favorecem escalabilidade incremental.

### 1.3.2. Replicação e Tolerância a Falhas

A replicação mantém cópias de uma partição em nós distintos. Seu benefício depende do fator de replicação e da distribuição das cópias entre domínios de falha independentes.

Replicação síncrona pode exigir confirmação de múltiplos nós, aumentando garantias imediatas ao custo de latência; replicação assíncrona reduz latência, mas permite divergência temporária.

Arquiteturas *leader–follower* centralizam a ordenação das escritas em um líder e utilizam *failover*; modelos sem líder admitem operações em múltiplas réplicas. Redundância, porém, só se converte em disponibilidade quando o sistema detecta falhas, redireciona requisições e restaura réplicas perdidas.

O *failover* exige ainda distinguir lentidão de falha e evitar dois líderes simultâneos (*split-brain*), razão pela qual a eleição de líder costuma depender de consenso.

### 1.3.3. Consistência, Disponibilidade e Quóruns

Múltiplas réplicas exigem modelos de consistência que determinem quais estados podem ser observados.

Na linearizabilidade [3], cada operação deve parecer ocorrer atomicamente sobre uma única cópia lógica e respeitar a precedência temporal das operações concluídas. Na consistência eventual, réplicas podem divergir temporariamente, mas convergem quando cessam novas atualizações.

O teorema CAP [4] estabelece que, diante de uma partição de rede, não se pode garantir simultaneamente consistência linearizável e disponibilidade de todas as operações.

Logo, CAP não significa simplesmente “escolher dois de três”: durante uma partição, preserva-se consistência recusando ou adiando operações, ou privilegia-se disponibilidade aceitando divergência temporária e posterior reconciliação.

Quóruns de leitura e escrita modulam essas garantias. Para \(N\) réplicas, uma condição clássica é:

\[
R + W > N,
\]

em que \(R\) é o número de réplicas consultadas na leitura e \(W\) o número de confirmações exigidas na escrita; a sobreposição resultante ajuda a coordenar versões, embora as garantias finais dependam do protocolo completo.

### 1.3.4. Modelos e Arquiteturas

Os mecanismos anteriores aparecem em diferentes abstrações. Sistemas de arquivos distribuídos, como o GFS, distribuem e replicam unidades de arquivos para obter *throughput* e tolerância a falhas.

O Bigtable [5] exemplifica armazenamento distribuído de dados estruturados em escala muito grande; o Dynamo, um *key-value store* altamente disponível.

Armazenamento de objetos organiza dados e metadados por identificadores e constitui base comum para grandes repositórios e *data lakes*.

Arquiteturas *shared-nothing* e a separação entre computação e armazenamento favorecem escalabilidade horizontal e evolução independente dos recursos.

## 1.4. Limitações, Trade-offs e Desafios Atuais

Não existe arquitetura universalmente superior. O projeto deve compatibilizar:

- **localidade versus balanceamento**;
- **redundância versus custo**;
- **consistência versus disponibilidade sob partições;** e
- **garantias fortes versus latência e coordenação**.

Devem ainda ser considerados padrão de acesso, *throughput*, durabilidade, domínios de falha e custo operacional. Para grandes volumes, códigos de apagamento podem reduzir o *overhead* da replicação integral ao custo de maior complexidade de reconstrução.

Assim, a arquitetura deve ser guiada pelas invariantes e pelo *workload*: requisitos distintos justificam combinações distintas de particionamento, replicação, consistência e recuperação.

## 1.5. Conclusão

Em síntese:

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

[1] GHEMAWAT, S. et al. ACM. 2003.
[2] DECANDIA, G. et al. ACM. 2007.
[3] HERLIHY, M. et al. ACM. 1990.
[4] GILBERT, S. et al. ACM. 2002.
[5] CHANG, F. et al. USENIX. 2006.
