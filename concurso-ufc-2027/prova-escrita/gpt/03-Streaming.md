# Ponto 2 — Processamento de Dados em Larga Escala: Processamento Paralelo e Distribuído em Larga Escala

## 2.1. Introdução e Delimitação do Problema

O processamento paralelo e distribuído busca reduzir o tempo de execução ou ampliar a capacidade computacional decompondo um problema em unidades de trabalho executáveis simultaneamente.

O paralelismo pode ocorrer dentro de um único nó, com memória compartilhada, ou entre múltiplos nós com memórias independentes e comunicação pela rede.

Em larga escala, o desafio não é apenas adicionar processadores, mas decompor, distribuir, coordenar e recuperar a computação de forma que o trabalho útil supere os custos introduzidos pela própria distribuição.

## 2.2. Fundamentos e Relevância

A decomposição pode explorar **paralelismo de dados**, aplicando operações equivalentes a partições distintas, e **paralelismo de tarefas**, executando operações diferentes conforme suas dependências.

O desempenho é quantificado pelo *speedup* e pela eficiência:

\[
S_{p} = \frac{T_{1}}{T_{p}}\quad\quad\quad\quad E_{p} = \frac{S_{p}}{p}
\]

em que \(T_{1}\) e \(T_{p}\) são os tempos com um e com \(p\) recursos.

Pela Lei de Amdahl [1], uma fração serial \(s\) limita o *speedup* mesmo quando \(p\) cresce:

\[
S(p) = \frac{1}{s + \frac{1 - s}{p}}
\]

Além disso, comunicação, sincronização, I/O e gerenciamento de tarefas introduzem *overhead*.

Distingue-se ainda **strong scaling**, que busca acelerar uma carga fixa, de **weak scaling**, que busca processar cargas proporcionalmente maiores com recursos adicionais [2], perspectiva central em larga escala.

## 2.3. Núcleo Técnico

### 2.3.1. Decomposição, Granularidade e Balanceamento

Uma computação paralela eficiente exige tarefas suficientemente independentes e com granularidade adequada.

Tarefas muito grandes reduzem o *overhead* de gerenciamento, mas limitam o paralelismo e dificultam o balanceamento; tarefas excessivamente pequenas elevam custos de criação, escalonamento e comunicação.

O balanceamento deve distribuir **trabalho computacional**, não apenas volume de dados: partições de mesmo tamanho podem ter custos diferentes, e *skew* de dados ou de acesso pode criar **stragglers**, tarefas significativamente mais lentas que determinam a duração de um estágio.

Escalonamento estático tem baixo *overhead* quando os custos são previsíveis; estratégias dinâmicas redistribuem trabalho e adaptam-se melhor à heterogeneidade. A *speculative execution* duplica tarefas anormalmente lentas, trocando capacidade adicional por redução da latência de cauda.

### 2.3.2. Comunicação, Sincronização e Localidade

Em memória distribuída, a rede possui latência e largura de banda finitas; uma decomposição eficiente maximiza a razão entre computação local e comunicação necessária.

De forma conceitual,

\[
T_{total} = T_{comp} + T_{comm} + T_{sync} + T_{overhead}
\]

mostra que reduzir apenas o componente computacional não garante redução proporcional do tempo total.

Barreiras entre estágios podem transformar uma tarefa lenta em espera global.

A **localidade dos dados** favorece executar a computação próxima às partições consumidas, mas deve ser conciliada com o balanceamento: o nó que contém os dados pode estar ocupado enquanto outro recurso permanece livre.

Redistribuições amplas, ou **shuffles**, são particularmente custosas por envolverem rede, I/O e sincronização; agregações locais ajudam a reduzi-las.

### 2.3.3. MapReduce e Modelos de Execução Distribuída

Modelos de execução abstraem parte da complexidade de decompor, agendar, coordenar e recuperar computações distribuídas.

O paradigma **MapReduce** [3] expressa a computação por funções *map*, que produzem pares intermediários, e *reduce*, que agregam valores de uma mesma chave; entre ambas, o *shuffle* redistribui e agrupa os dados intermediários:

```text
ENTRADA → MAP → SHUFFLE → REDUCE → SAÍDA
```

O *runtime* explora localidade, distribui tarefas, detecta falhas e reexecuta unidades perdidas ou excessivamente lentas: a tolerância a falhas passa a integrar o próprio modelo de execução.

MapReduce é robusto para grandes cargas *batch*, mas perde eficiência em pipelines complexos e algoritmos iterativos, pois sucessivas etapas exigem materialização intermediária.

### 2.3.4. DAGs, Reutilização e Recuperação

Modelos baseados em **grafos acíclicos dirigidos (DAGs)** representam operações como vértices e dependências como arestas, permitindo identificar ramos independentes, formar estágios separados por *shuffles* e evitar materializações desnecessárias.

O Spark combina DAGs, reutilização de dados em memória e **lineage** [4]: em vez de replicar todos os resultados intermediários, uma partição perdida pode ser recomputada a partir de suas dependências.

Surge um compromisso entre:

- **replicação**, que consome armazenamento;
- **recomputação**, que consome processamento;
- **checkpointing**, que persiste estados intermediários e reduz o custo de recuperação ao preço de I/O adicional.

Dessa forma, a tolerância a falhas pode decorrer não apenas da redundância dos dados, mas também da capacidade de reconstruir computações.

## 2.4. Limitações, Trade-offs e Desafios Atuais

Distribuição não implica escalabilidade linear.

Além da fração serial, comunicação, *shuffles*, *skew*, stragglers e gargalos centralizados produzem retornos decrescentes à medida que novos nós são adicionados; como o estágio termina com sua tarefa mais lenta, importa não apenas o desempenho médio, mas a cauda da distribuição.

Clusters reais são heterogêneos e sujeitos a falhas frequentes, exigindo escalonamento adaptativo e decisões sobre quando reexecutar, recomputar ou restaurar *checkpoints*.

Abstrações de alto nível tampouco eliminam custos físicos: uma operação simples no programa pode corresponder a uma grande redistribuição de dados pela rede.

Existe, assim, um compromisso permanente entre:

- **granularidade e overhead**;
- **localidade e balanceamento**;
- **paralelismo e comunicação**;
- **redundância e recomputação**;
- e **desempenho e custo de recursos**.

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

Processamento distribuído escalável não resulta do simples aumento do número de nós, mas da combinação entre paralelismo explorável, comunicação eficiente, balanceamento de carga, tolerância a falhas e uso eficiente dos recursos.

## Referências

[1] AMDAHL, G. AFIPS. 1967.
[2] GUSTAFSON, J. CACM. 1988.
[3] DEAN, J. et al. OSDI. 2004.
[4] ZAHARIA, M. et al. NSDI. 2012.
