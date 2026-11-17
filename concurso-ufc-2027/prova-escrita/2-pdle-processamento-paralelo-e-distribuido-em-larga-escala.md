
# Ponto 2 — Processamento de Dados em Larga Escala: Processamento Paralelo e Distribuído em Larga Escala

## 2.1. Fundamentos de Paralelismo e Distribuição

O processamento paralelo busca reduzir tempo de execução ou ampliar a capacidade de processamento pela decomposição de um problema em unidades de trabalho executáveis simultaneamente. Paralelismo pode ocorrer dentro de um único nó, em arquiteturas de memória compartilhada, ou entre múltiplos nós com memórias independentes e comunicação pela rede, caracterizando processamento distribuído. Em aplicações orientadas a dados, essa decomposição pode explorar paralelismo de dados, aplicando operações equivalentes a diferentes partições, ou paralelismo de tarefas, executando operações distintas quando suas dependências permitem.

O ganho obtido depende, contudo, da fração efetivamente paralelizável e dos custos introduzidos pela execução concorrente. Se \(T_1\) e \(T_p\) representam os tempos com um e \(p\) recursos, respectivamente, o speedup é \(S_p=T_1/T_p\), enquanto a eficiência é \(E_p=S_p/p\). A Lei de Amdahl, \(S(p)=1/[s+(1-s)/p]\), evidencia que uma fração serial \(s\) limita o speedup mesmo com grande número de processadores. Além disso, comunicação, sincronização e gerenciamento das tarefas produzem overhead, de modo que paralelismo não implica escalabilidade linear. Em larga escala, o objetivo pode ser tanto reduzir o tempo de uma carga fixa, caracterizando strong scaling, quanto processar volumes crescentes com recursos proporcionais, caracterizando weak scaling.

---

> Mnemonics



---

## 2.2. Decomposição, Granularidade e Balanceamento de Carga

A eficiência do processamento paralelo depende da decomposição do problema em unidades de trabalho suficientemente independentes. Essa decomposição pode explorar paralelismo de dados, aplicando operações equivalentes a diferentes partições, ou paralelismo de tarefas, executando operações distintas conforme suas dependências. A granularidade das tarefas constitui um compromisso central: unidades grandes reduzem overhead de criação, comunicação e escalonamento, mas limitam o balanceamento; unidades menores ampliam oportunidades de paralelismo e redistribuição dinâmica, porém aumentam custos de gerenciamento.

O balanceamento de carga procura distribuir trabalho, e não apenas volume de dados, entre os recursos disponíveis. Partições de mesmo tamanho podem apresentar custos computacionais distintos, e skew de dados ou de acesso pode produzir tarefas significativamente mais lentas, denominadas stragglers, que passam a determinar o tempo de conclusão de um estágio. Escalonamento estático apresenta baixo overhead quando os custos são previsíveis, enquanto estratégias dinâmicas permitem redistribuir tarefas conforme recursos se tornam disponíveis, adaptando-se à heterogeneidade e à variabilidade da execução. Técnicas como speculative execution podem duplicar tarefas anormalmente lentas para reduzir a latência de cauda, ao custo de capacidade adicional.

---

> Mnemonics

---

## 2.3. Comunicação, Sincronização e Localidade

A escalabilidade de uma computação distribuída depende não apenas da quantidade de trabalho paralelizável, mas também do custo de comunicação e sincronização entre as tarefas. Em arquiteturas de memória distribuída, a troca de dados pela rede envolve latência e largura de banda finitas, de modo que decomposições eficientes procuram maximizar a razão entre computação local e comunicação. Sincronizações, como barreiras entre estágios, podem ainda transformar a lentidão de uma única tarefa em espera global, enquanto estado compartilhado e comunicação frequente introduzem contenção e reduzem o paralelismo efetivo.

A localização dos dados constitui, portanto, uma consideração central. Quando o volume transferido é grande, frequentemente é mais eficiente executar a computação próxima às partições que ela consome do que movimentar os dados pela rede, embora essa preferência precise ser conciliada com balanceamento de carga e disponibilidade dos recursos. Operações que redistribuem dados amplamente entre nós, como shuffles necessários a determinadas agregações e agrupamentos por chave, possuem custo elevado de rede, I/O e sincronização; agregações locais e outras estratégias de redução de comunicação podem mitigar esse overhead. Assim, aumentar o número de nós somente produz escalabilidade enquanto o ganho de trabalho paralelo superar os custos adicionais de comunicação e coordenação.

---

> Mnemonics

---

## 2.4. MapReduce, DAGs e Modelos de Execução Distribuída

Modelos de execução distribuída abstraem parte da complexidade de decompor, agendar, coordenar e recuperar computações sobre grandes conjuntos de dados. O paradigma MapReduce, sistematizado por Dean e Ghemawat, expressa a computação por funções `map`, que produzem pares intermediários, e `reduce`, que agregam valores associados a uma mesma chave. Entre ambas ocorre o `shuffle`, responsável por particionar, transferir e agrupar dados intermediários entre os nós. O runtime pode explorar localidade dos dados, balancear tarefas e reexecutar unidades perdidas ou excessivamente lentas, incorporando tolerância a falhas ao próprio modelo de execução.

Embora robusto para grandes cargas batch, MapReduce possui limitações para pipelines complexos e algoritmos iterativos, sobretudo quando múltiplas etapas exigem materialização de resultados intermediários. Modelos baseados em grafos acíclicos dirigidos (DAGs) representam explicitamente dependências entre operações, permitindo explorar paralelismo entre ramos independentes, organizar estágios separados por shuffles e reduzir materializações desnecessárias. Sistemas como Spark exemplificam essa evolução ao combinar DAGs, reutilização de dados em memória e lineage, pelo qual partições perdidas podem ser recomputadas a partir de suas dependências. Assim, modelos de execução oferecem diferentes compromissos entre simplicidade, expressividade, comunicação, uso de memória e recuperação de falhas.

---

> Mnemonics

---

## 2.5. Escalabilidade, Tolerância a Falhas e Limitações

A escalabilidade de uma aplicação distribuída não decorre apenas da adição de recursos, mas da capacidade de converter esses recursos em trabalho útil com overhead controlado. Além da fração serial destacada pela Lei de Amdahl, comunicação, sincronização, I/O, scheduling, skew e stragglers limitam o speedup e podem produzir retornos decrescentes. Em strong scaling, uma carga fixa é acelerada com mais recursos; em weak scaling, o volume processado cresce proporcionalmente ao sistema, perspectiva frequentemente mais adequada ao processamento de dados em larga escala. Assim, gargalos centralizados e tarefas de cauda podem limitar o desempenho global mesmo em clusters extensos.

A tolerância a falhas também deve integrar o modelo de execução. Tarefas perdidas podem ser reexecutadas; dados intermediários podem ser reconstruídos a partir de lineage ou preservados por checkpoints, que reduzem o custo de recuperação ao preço de I/O adicional. Essas estratégias estabelecem compromissos entre armazenamento, recomputação e tempo de recuperação. Heterogeneidade dos recursos, falhas frequentes e custo operacional reforçam a necessidade de escalonamento adaptativo e recuperação localizada. Portanto, processamento distribuído escalável resulta do equilíbrio entre paralelismo, comunicação, balanceamento, resiliência e eficiência de recursos, e não do simples aumento do número de nós.

---

> Mnemonics

---

## Texto Final

# Ponto 2 — Processamento de Dados em Larga Escala: Processamento Paralelo e Distribuído em Larga Escala

## 1. Introdução e Delimitação do Problema

O processamento paralelo e distribuído busca reduzir tempo de execução ou ampliar a capacidade computacional pela decomposição de um problema em unidades de trabalho executáveis simultaneamente. O paralelismo pode ocorrer dentro de um único nó, em arquiteturas de memória compartilhada, ou entre múltiplos nós com memórias independentes e comunicação pela rede. Em processamento de dados em larga escala, o desafio não consiste apenas em adicionar processadores, mas em decompor, distribuir, coordenar e recuperar a computação de forma que o trabalho útil supere os custos introduzidos pela própria distribuição.

## 2. Fundamentos e Relevância

A decomposição pode explorar **paralelismo de dados**, aplicando operações equivalentes a partições distintas, e **paralelismo de tarefas**, executando operações diferentes conforme suas dependências. O desempenho pode ser quantificado pelo *speedup* e pela eficiência:

\[
S_p=\frac{T_1}{T_p}
\qquad\qquad
E_p=\frac{S_p}{p}
\]

em que \(T_1\) e \(T_p\) são os tempos com um e \(p\) recursos.

Entretanto, apenas a fração paralelizável pode beneficiar-se do aumento de processadores. Pela Lei de Amdahl,

\[
S(p)=\frac{1}{s+\frac{1-s}{p}}
\]

uma fração serial \(s\) limita o *speedup* mesmo quando \(p\) cresce. Além disso, comunicação, sincronização, I/O e gerenciamento das tarefas introduzem *overhead*. Deve-se distinguir ainda **strong scaling**, que busca acelerar uma carga fixa, de **weak scaling**, que busca processar cargas proporcionalmente maiores com recursos adicionais, perspectiva especialmente relevante em larga escala.

## 3. Núcleo Técnico

### 3.1. Decomposição, Granularidade e Balanceamento

Uma computação paralela eficiente exige tarefas suficientemente independentes e com granularidade adequada. Tarefas muito grandes reduzem o *overhead* de gerenciamento, mas limitam o paralelismo e dificultam o balanceamento; tarefas excessivamente pequenas aumentam oportunidades de distribuição, porém elevam custos de criação, escalonamento e comunicação.

O balanceamento deve distribuir **trabalho computacional**, não apenas volume de dados. Partições de mesmo tamanho podem possuir custos diferentes, enquanto *skew* de dados ou acesso pode criar **stragglers**, tarefas significativamente mais lentas que passam a determinar a duração de um estágio. Escalonamento estático apresenta baixo *overhead* quando os custos são previsíveis; estratégias dinâmicas redistribuem trabalho conforme recursos se tornam disponíveis e adaptam-se melhor à heterogeneidade. Em alguns sistemas, *speculative execution* duplica tarefas anormalmente lentas, trocando capacidade adicional por redução da latência de cauda.

### 3.2. Comunicação, Sincronização e Localidade

Em memória distribuída, a comunicação pela rede possui latência e largura de banda finitas. Assim, uma decomposição eficiente procura maximizar a razão entre computação local e comunicação necessária. De forma conceitual,

\[
T_{\mathrm{total}}
=
T_{\mathrm{comp}}
+
T_{\mathrm{comm}}
+
T_{\mathrm{sync}}
+
T_{\mathrm{overhead}}
\]

mostra que reduzir apenas o componente computacional não garante redução proporcional do tempo total.

Sincronizações, como barreiras entre estágios, podem transformar uma tarefa lenta em espera global. Por outro lado, a **localidade dos dados** favorece executar a computação próxima às partições consumidas, evitando transferências volumosas pela rede. Essa preferência deve ser conciliada com balanceamento de carga: o nó que contém os dados pode estar ocupado enquanto outro recurso permanece disponível.

Operações de redistribuição ampla, ou **shuffles**, são particularmente custosas por envolverem rede, I/O e sincronização. Agregações locais e outras estratégias que reduzam comunicação ajudam a preservar escalabilidade.

### 3.3. MapReduce e Modelos de Execução Distribuída

Modelos de execução abstraem parte da complexidade de decompor, agendar, coordenar e recuperar computações distribuídas. O paradigma **MapReduce**, sistematizado por Dean e Ghemawat (2004), expressa a computação por funções `map`, que produzem pares intermediários, e `reduce`, que agregam valores de uma mesma chave. Entre ambas ocorre o `shuffle`, que redistribui e agrupa dados intermediários:

```text
ENTRADA
   ↓
  MAP
   ↓
SHUFFLE
   ↓
 REDUCE
   ↓
 SAÍDA
```

O *runtime* pode explorar localidade, distribuir tarefas, detectar falhas e reexecutar unidades perdidas ou excessivamente lentas. Dessa forma, tolerância a falhas passa a fazer parte do próprio modelo de execução.

MapReduce é robusto para grandes cargas *batch*, mas torna-se menos eficiente em pipelines complexos ou algoritmos iterativos quando sucessivas etapas exigem materialização intermediária.

### 3.4. DAGs, Reutilização e Recuperação

Modelos baseados em **grafos acíclicos dirigidos (DAGs)** representam operações como vértices e dependências como arestas. Essa representação permite identificar ramos independentes, explorar paralelismo, formar estágios separados por *shuffles* e evitar materializações desnecessárias.

Sistemas como Spark exemplificam essa evolução ao combinar DAGs, reutilização de dados em memória e **lineage**. Em vez de replicar todos os resultados intermediários, uma partição perdida pode ser recomputada a partir de suas dependências. Surge então um compromisso entre:

- **replicação**, que consome armazenamento;
- **recomputação**, que consome processamento;
- **checkpointing**, que persiste estados intermediários e reduz o custo de recuperação ao preço de I/O adicional.

Dessa forma, tolerância a falhas pode ser obtida não apenas pela redundância dos dados, mas também pela capacidade de reconstruir computações.

## 4. Limitações, Trade-offs e Desafios Atuais

Distribuição não implica escalabilidade linear. Além da fração serial descrita por Amdahl, comunicação, sincronização, *shuffles*, I/O, *skew*, stragglers e gargalos centralizados podem produzir retornos decrescentes à medida que novos nós são adicionados. Em muitos estágios, o tempo global aproxima-se do tempo da tarefa mais lenta, tornando relevante não apenas o desempenho médio, mas também a cauda da distribuição.

Clusters reais também são heterogêneos e sujeitos a falhas frequentes. A execução deve, portanto, adaptar o escalonamento, recuperar tarefas localmente e decidir quando reexecutar, recomputar ou restaurar *checkpoints*. Arquiteturas modernas ampliam ainda a elasticidade e a capacidade de executar DAGs complexos, mas abstrações de alto nível não eliminam custos físicos: uma operação simples no programa pode corresponder a uma grande redistribuição de dados pela rede.

Assim, existe um compromisso permanente entre **granularidade e overhead**, **localidade e balanceamento**, **paralelismo e comunicação**, **redundância e recomputação** e, finalmente, **desempenho e custo de recursos**.

## 5. Conclusão

A lógica do processamento paralelo e distribuído em larga escala pode ser sintetizada como:

```text
PROBLEMA
   ↓
DECOMPOSIÇÃO
   ↓
TAREFAS / PARTIÇÕES
   ↓
ESCALONAMENTO E BALANCEAMENTO
   ↓
COMUNICAÇÃO / SINCRONIZAÇÃO
   ↓
LOCALIDADE / SHUFFLE
   ↓
MODELO DE EXECUÇÃO
   ↓
REEXECUÇÃO / CHECKPOINT
   ↓
ESCALABILIDADE
```

Portanto, processamento distribuído escalável não resulta do simples aumento do número de nós, mas da combinação entre paralelismo explorável, comunicação eficiente, balanceamento de carga, tolerância a falhas e uso eficiente dos recursos.

## Referências

- AMDAHL, G. *Validity of the Single Processor Approach to Achieving Large-Scale Computing Capabilities*. 1967.
- DEAN, J.; GHEMAWAT, S. *MapReduce: Simplified Data Processing on Large Clusters*. 2004.
- GUSTAFSON, J. *Reevaluating Amdahl's Law*. 1988.
- ZAHARIA, M. et al. *Resilient Distributed Datasets: A Fault-Tolerant Abstraction for In-Memory Cluster Computing*. 2012.

---

## Outras Notas


