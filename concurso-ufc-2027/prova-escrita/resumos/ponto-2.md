# Ponto 2 — Processamento de Dados em Larga Escala: Processamento Paralelo e Distribuído em Larga Escala

## 2.1. Introdução e Delimitação do Problema

2.1.A. [2] Apresentar os dois objetivos do processamento paralelo e distribuído e o recurso comum: dividir o trabalho.

2.1.B. [2] Distinguir paralelismo dentro de um nó e entre nós que se comunicam pela rede.

2.1.C. [3] Delimitar o desafio: decompor, distribuir, coordenar e recuperar, com o trabalho útil superando os custos da distribuição.

## 2.2. Fundamentos e Relevância

2.2.A. [2] Contrapor paralelismo de dados e paralelismo de tarefas.

2.2.B. [2] Introduzir as medidas de ganho, speedup e eficiência.

2.2.C. [2] \(S(p) = T_{1}/T_{p}\) e \(E(p) = S(p)/p\)

2.2.D. [1][4] Introduzir a Lei de Amdahl a partir da fração serial \(s\), citando Amdahl.

2.2.E. [1][5]

\[
S(p) = \frac{1}{s + \frac{1 - s}{p}} \le \frac{1}{s}.
\]

2.2.F. [1] Exemplificar o limite com 10% de código serial.

2.2.G. [5] Porém, ressaltar que em larga escala o problema cresce com a máquina, e contrapor strong scaling e weak scaling.

## 2.3. Núcleo Técnico

### 2.3.1. Decomposição, Granularidade e Balanceamento

2.3.1.A. [2] Introduzir a granularidade como escolha da decomposição.

2.3.1.B. [1] Comparar tarefas grandes e pequenas pelo custo de cada extremo.

2.3.1.C. [1] Ressaltar que balancear é distribuir trabalho, não apenas dados.

2.3.1.D. [1][5] Explicar como o skew gera stragglers e por que eles atrasam todo o estágio.

2.3.1.E. [1] Contrapor escalonamento estático e dinâmico.

2.3.1.F. [5] Apresentar a execução especulativa como mitigação dos stragglers.

### 2.3.2. Comunicação, Sincronização e Localidade

2.3.2.A. [1] Partir dos limites da rede e mostrar que o tempo total passa a incluir comunicação e sincronização.

2.3.2.B. [1][5]

\[
T_{total} = T_{comp} + T_{comm} + T_{sync} + T_{overhead}
\]

2.3.2.C. [1] Concluir por que acelerar só a computação não basta, e o efeito das barreiras entre estágios.

2.3.2.D. [2] Introduzir a localidade e seu conflito com o balanceamento.

2.3.2.E. [1][5] Ressaltar os shuffles como as operações mais caras e a agregação local como forma de reduzi-los.

### 2.3.3. MapReduce e Modelos de Execução Distribuída

2.3.3.A. [2][4] Introduzir o MapReduce pelas duas funções que o programador escreve, citando Dean e Ghemawat.

2.3.3.B. [1] Explicar o papel do shuffle entre map e reduce.

2.3.3.C. [3] Diagrama do fluxo MapReduce, da entrada à saída.

2.3.3.D. [2] Exemplificar com a contagem de palavras.

2.3.3.E. [1] Explicar o que o runtime assume, destacando a tolerância a falhas integrada ao modelo.

2.3.3.F. [1][5] Contrapor a robustez em batch à ineficiência em algoritmos iterativos e justificar pela gravação em disco.

### 2.3.4. DAGs, Reutilização e Recuperação

2.3.4.A. [2] Introduzir os modelos baseados em DAGs.

2.3.4.B. [2][4] Apresentar o Spark e os RDDs, citando Zaharia et al.

2.3.4.C. [1][5] Explicar a avaliação preguiçosa e por que ela permite planejar o DAG inteiro.

2.3.4.D. [1][5] Contrapor dependências estreitas e largas e mostrar como elas definem os estágios.

2.3.4.E. [1] Ressaltar o reuso de dados em memória nos algoritmos iterativos.

2.3.4.F. [1][5] Explicar a recuperação de falhas pela linhagem.

2.3.4.G. [5] Bullets com o compromisso entre replicação, recomputação e checkpointing, e o recurso que cada um consome.

## 2.4. Limitações, Trade-offs e Desafios Atuais

2.4.A. [1] Afirmar que distribuição não implica escalabilidade linear e enumerar as causas dos retornos decrescentes.

2.4.B. [5] Ressaltar a importância da cauda da distribuição, não apenas da média.

2.4.C. [1] Mencionar clusters heterogêneos e falhas frequentes.

2.4.D. [1][5] Alertar que abstrações de alto nível não eliminam custos físicos, com o exemplo do agrupamento por chave.

2.4.E. [3] Fechar com os compromissos permanentes do projeto.

## 2.5. Conclusão

2.5.A. [3] Diagrama de síntese.

2.5.B. [1][3] Concluir que escalar não é apenas acrescentar nós, retomando os mecanismos que de fato produzem escala.

2.5.C. [3] Relacionar MapReduce e Spark a esses mecanismos, ressalvando que não eliminam seus custos.

## Referências

R.A. [4] Referências em ABNT.
