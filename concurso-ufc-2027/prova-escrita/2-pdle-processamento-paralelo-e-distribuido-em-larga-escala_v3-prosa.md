# Ponto 2 — Processamento de Dados em Larga Escala: Processamento Paralelo e Distribuído em Larga Escala

## 2.1. Introdução e Delimitação do Problema

O processamento paralelo e distribuído busca reduzir o tempo de execução, ou ampliar a capacidade de processamento, dividindo um problema em unidades de trabalho executadas simultaneamente, seja em um nó com memória compartilhada, seja em vários nós que se comunicam pela rede.

Em larga escala, o desafio não é apenas adicionar processadores, mas decompor, distribuir, coordenar e recuperar a computação de modo que o trabalho útil supere os custos da própria distribuição.

## 2.2. Fundamentos e Relevância

O **paralelismo de dados** aplica a mesma operação a partes distintas dos dados; o **paralelismo de tarefas** executa operações diferentes ao mesmo tempo, respeitando suas dependências.

O ganho é medido pelo *speedup* \(S(p) = T_{1}/T_{p}\), razão entre os tempos com um e com \(p\) processadores, e pela eficiência \(E(p) = S(p)/p\). Pela Lei de Amdahl¹, se uma fração \(s\) do programa é serial,

\[
S(p) = \frac{1}{s + \frac{1 - s}{p}} \le \frac{1}{s}.
\]

Com 10% de código serial, o *speedup* nunca passa de 10. Em larga escala, porém, o problema costuma crescer com a máquina: distingue-se o **strong scaling**, que acelera uma carga fixa, do **weak scaling**, que processa cargas proporcionalmente maiores com mais recursos.

## 2.3. Núcleo Técnico

### 2.3.1. Decomposição, Granularidade e Balanceamento

A decomposição define a **granularidade**: tarefas grandes têm pouco custo de gerenciamento, mas limitam o paralelismo; tarefas muito pequenas multiplicam custos de escalonamento e comunicação.

O balanceamento deve distribuir **trabalho**, não apenas dados: chaves muito frequentes (*skew*) geram **stragglers**, tarefas lentas que atrasam todo o estágio. O escalonamento estático é barato quando os custos são previsíveis; o dinâmico adapta-se melhor à heterogeneidade. A **execução especulativa** lança cópias de tarefas lentas e aproveita a que terminar primeiro.

### 2.3.2. Comunicação, Sincronização e Localidade

Em memória distribuída, a rede tem latência e largura de banda limitadas, e o tempo total passa a incluir comunicação e sincronização:

\[
T_{total} = T_{comp} + T_{comm} + T_{sync} + T_{overhead}
\]

Por isso, acelerar apenas a computação não reduz o tempo total na mesma proporção, e barreiras entre estágios fazem todos esperarem pela tarefa mais lenta.

A **localidade** recomenda levar a computação até os dados, conciliando-a com o balanceamento: o nó que guarda os dados pode estar ocupado. As operações mais caras são os **shuffles**, redistribuições amplas que envolvem rede, disco e sincronização; agregar localmente antes de enviar reduz seu volume.

### 2.3.3. MapReduce e Modelos de Execução Distribuída

No **MapReduce**², o programador escreve duas funções: *map*, que transforma cada registro em pares chave-valor, e *reduce*, que agrega os valores de cada chave. Entre elas, o *shuffle* agrupa os pares por chave:

```text
ENTRADA → MAP → SHUFFLE → REDUCE → SAÍDA
```

Na contagem de palavras, *map* emite (palavra, 1) e *reduce* soma os valores. O *runtime* agenda tarefas perto dos dados, detecta falhas e reexecuta tarefas perdidas ou lentas: a tolerância a falhas integra o modelo. O MapReduce é robusto para grandes cargas *batch*, mas ineficiente em algoritmos iterativos, pois cada etapa grava seus resultados em disco.

### 2.3.4. DAGs, Reutilização e Recuperação

Modelos baseados em **grafos acíclicos dirigidos (DAGs)** representam operações como vértices e dependências como arestas. O Spark³ organiza os dados em **RDDs**, coleções imutáveis e particionadas, com avaliação preguiçosa: nada é executado até que uma ação peça um resultado, o que permite planejar o DAG inteiro.

Operações com **dependências estreitas**, em que cada partição depende de poucas partições anteriores (*map*, *filter*), são encadeadas em um mesmo estágio; **dependências largas**, como agrupar por chave, exigem *shuffle* e iniciam novo estágio. Dados reutilizados permanecem em memória, acelerando algoritmos iterativos.

Para recuperar falhas, o Spark usa a **linhagem** (*lineage*): uma partição perdida é recomputada a partir das transformações que a geraram. Surge um compromisso entre:

- **replicação**, que consome armazenamento;
- **recomputação**, que consome processamento;
- **checkpointing**, que grava estados intermediários e encurta a recomputação ao custo de I/O.

## 2.4. Limitações, Trade-offs e Desafios Atuais

Distribuição não implica escalabilidade linear: fração serial, comunicação, *shuffles*, *skew* e gargalos centralizados produzem retornos decrescentes, e, como cada estágio termina com sua tarefa mais lenta, importa a cauda da distribuição, não apenas a média.

Clusters reais são heterogêneos e falham com frequência. Abstrações de alto nível tampouco eliminam custos físicos: uma linha que agrupa por chave pode redistribuir todo o conjunto de dados. O projeto equilibra granularidade e *overhead*, localidade e balanceamento, paralelismo e comunicação, redundância e recomputação.

## 2.5. Conclusão

Em síntese:

```text
PROBLEMA
↓
DECOMPOSIÇÃO
↓
ESCALONAMENTO E BALANCEAMENTO
↓
COMUNICAÇÃO / SHUFFLE
↓
MODELO DE EXECUÇÃO
↓
REEXECUÇÃO / CHECKPOINT
↓
ESCALABILIDADE
```

Escalar não é apenas acrescentar nós, mas decompor bem o problema, reduzir comunicação, equilibrar a carga e recuperar falhas a baixo custo; MapReduce e Spark automatizam esses mecanismos, sem eliminar seus custos.

## Referências

1. AMDAHL, G. M. Validity of the single processor approach [...]. In: AFIPS, 1967.
2. DEAN, J.; GHEMAWAT, S. MapReduce: simplified data processing on large clusters. In: OSDI, 2004.
3. ZAHARIA, M. et al. Resilient distributed datasets [...]. In: NSDI, 2012.
