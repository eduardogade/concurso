# Ponto 1 — Processamento de Dados em Larga Escala: Armazenamento e Gerenciamento Distribuído de Dados

## 1.1. Introdução e Delimitação do Problema

Quando o volume de dados e a demanda por acesso crescem, um único servidor deixa de bastar, por limites de capacidade, desempenho e disponibilidade. A escalabilidade vertical, que amplia uma máquina, esbarra em limites físicos e econômicos; sistemas de larga escala recorrem, então, à escalabilidade horizontal, distribuindo os dados entre muitos nós.

O desafio passa a ser manter os dados escaláveis, disponíveis, duráveis e coerentes, apesar da latência da rede e de falhas parciais.

## 1.2. Fundamentos e Relevância

Um sistema de armazenamento distribuído espalha os dados por vários nós, mas oferece à aplicação uma visão lógica única. Distribuir não traz escalabilidade nem tolerância a falhas automaticamente: cria custos de latência, coordenação e recuperação.

Dois mecanismos estruturam o problema:

- **particionamento**: colocar partes distintas dos dados em nós distintos, ampliando capacidade e paralelismo;
- **replicação**: manter cópias dos mesmos dados em nós diferentes, preservando disponibilidade e durabilidade.

Em larga escala, falhas são frequentes e devem ser tratadas como condição normal de projeto, princípio do Google File System¹.

## 1.3. Núcleo Técnico

### 1.3.1. Particionamento e Distribuição

No *sharding*, uma chave de partição decide em que nó cada registro fica. O particionamento por **intervalos** mantém chaves vizinhas juntas e favorece consultas por faixa, mas pode concentrar acessos (*hotspots*); o particionamento por **hash** distribui melhor as chaves, mas perde a ordenação.

Dados equilibrados não garantem carga equilibrada, pois algumas chaves são muito mais acessadas. Quando nós entram ou saem, os dados precisam ser rebalanceados, com custo de rede e disco. O *consistent hashing*, usado em sistemas inspirados no Dynamo, reduz esse custo: chaves e nós ocupam um anel, e a entrada de um nó desloca apenas as chaves vizinhas.

### 1.3.2. Replicação e Tolerância a Falhas

Cada partição é copiada em nós de domínios de falha independentes. Na replicação **síncrona**, a escrita só é confirmada após as réplicas a receberem: mais garantia, mais latência. Na **assíncrona**, confirma-se antes, reduzindo a latência, mas admitindo réplicas temporariamente desatualizadas.

Na arquitetura **líder–seguidor**, o líder ordena as escritas; se falhar, um seguidor é promovido (*failover*). Para evitar dois líderes simultâneos (*split-brain*), a eleição depende de consenso. Sistemas **sem líder** aceitam escritas em várias réplicas. Redundância só vira disponibilidade quando o sistema detecta a falha, redireciona requisições e restaura as cópias perdidas.

### 1.3.3. Consistência, Disponibilidade e Quóruns

Com várias cópias, é preciso definir o que pode ser lido. Na **linearizabilidade**, o sistema se comporta como uma cópia única, com cada operação ocorrendo em um instante. Na **consistência eventual**, réplicas divergem temporariamente, mas convergem quando cessam as atualizações.

O teorema CAP² mostra que, durante uma partição de rede, não se pode garantir ao mesmo tempo consistência linearizável e disponibilidade: o sistema recusa operações ou as aceita e reconcilia divergências depois. O **PACELC** acrescenta que, mesmo sem partição, há um compromisso entre latência e consistência.

Quóruns ajustam esse equilíbrio. Com \(N\) réplicas, a escrita espera \(W\) confirmações e a leitura consulta \(R\) réplicas; se

\[
R + W > N,
\]

leitura e escrita compartilham ao menos uma réplica, e a leitura consulta ao menos uma cópia com a versão mais recente.

Quando uma transação altera várias partições, preservar a **atomicidade** (tudo ou nada) exige coordenação. No *two-phase commit* (**2PC**)³, o coordenador primeiro pergunta aos participantes se podem confirmar; na segunda fase, efetiva a transação se todos votarem "sim" ou a aborta caso contrário. O custo são rodadas extras de rede e bloqueio: se o coordenador falhar entre as fases, os participantes esperam com recursos travados. Por isso, muitos sistemas limitam transações a uma partição.

### 1.3.4. Modelos e Arquiteturas

Esses mecanismos aparecem em abstrações diferentes: sistemas de arquivos distribuídos, como GFS e HDFS, replicam grandes blocos e priorizam *throughput*; o Bigtable particiona tabelas por intervalos de chave; o Dynamo é um armazenamento chave-valor que privilegia disponibilidade; e o armazenamento de objetos sustenta *data lakes*. Arquiteturas *shared-nothing* e a separação entre computação e armazenamento permitem escalar cada recurso independentemente.

## 1.4. Limitações, Trade-offs e Desafios Atuais

Não existe arquitetura universalmente superior. O projeto equilibra:

- **localidade × balanceamento**;
- **redundância × custo**;
- **consistência × disponibilidade e latência**;
- **atomicidade distribuída × desempenho**.

Para grandes volumes, códigos de apagamento reduzem o custo da replicação integral, ao preço de reconstruções mais caras. A arquitetura deve partir do *workload*: um sistema bancário e um catálogo de produtos justificam escolhas diferentes de particionamento, replicação e consistência.

## 1.5. Conclusão

Em síntese:

```text
DATASET
↓
PARTICIONAMENTO
↓
REPLICAÇÃO
↓
CONSISTÊNCIA / QUÓRUNS / TRANSAÇÕES
↓
RECUPERAÇÃO E REBALANCEAMENTO
↓
ABSTRAÇÃO DE ARMAZENAMENTO
```

Particiona-se para ganhar escala e replica-se para sobreviver a falhas, aceitando que coordenar cópias tem custo. O bom projeto oferece a cada aplicação o nível de consistência de que ela realmente precisa.

## Referências

1. GHEMAWAT, S.; GOBIOFF, H.; LEUNG, S.-T. The Google file system. In: SOSP, 2003.
2. GILBERT, S.; LYNCH, N. Brewer's conjecture and the feasibility of consistent, available, partition-tolerant web services. **ACM SIGACT News**, 2002.
3. KLEPPMANN, M.; RICCOMINI, C. **Designing data-intensive applications**. 2. ed. O'Reilly, 2026.
