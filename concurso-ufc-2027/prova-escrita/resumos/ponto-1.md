# Ponto 1 — Processamento de Dados em Larga Escala: Armazenamento e Gerenciamento Distribuído de Dados

## 1.1. Introdução e Delimitação do Problema

1.1.A. [2] Partir do crescimento de volume e demanda, que faz um único servidor deixar de bastar, e nomear os três limites.

1.1.B. [2] Contrapor escalabilidade vertical e horizontal e justificar por que a larga escala recorre à horizontal.

1.1.C. [3] Delimitar o desafio: as quatro propriedades a preservar, apesar da latência da rede e de falhas parciais.

## 1.2. Fundamentos e Relevância

1.2.A. [2] Definir armazenamento distribuído pela visão lógica única oferecida à aplicação.

1.2.B. [1] Ressalvar que distribuir não traz escalabilidade nem tolerância a falhas automaticamente, e nomear os custos criados.

1.2.C. [2] Bullets com os dois mecanismos estruturantes, particionamento e replicação, e o ganho de cada um.

1.2.D. [1][4] Concluir que falhas são condição normal de projeto, citando o Google File System.

## 1.3. Núcleo Técnico

### 1.3.1. Particionamento e Distribuição

1.3.1.A. [2] Introduzir o sharding pela função da chave de partição.

1.3.1.B. [1][5] Comparar particionamento por intervalos e por hash, com a vantagem e o custo de cada um.

1.3.1.C. [1] Ressaltar que dados equilibrados não garantem carga equilibrada.

1.3.1.D. [2] Introduzir o rebalanceamento quando nós entram ou saem, e seu custo.

1.3.1.E. [1][5] Apresentar o consistent hashing, associado ao Dynamo, e explicar pelo anel por que ele reduz o rebalanceamento.

### 1.3.2. Replicação e Tolerância a Falhas

1.3.2.A. [2] Situar as cópias em domínios de falha independentes.

1.3.2.B. [1][5] Contrapor replicação síncrona e assíncrona pelo compromisso entre garantia e latência.

1.3.2.C. [1] Descrever a arquitetura líder–seguidor e o failover.

1.3.2.D. [1][5] Explicar o risco de split-brain e por que a eleição depende de consenso.

1.3.2.E. [2] Mencionar os sistemas sem líder.

1.3.2.F. [1] Concluir que redundância só vira disponibilidade com detecção, redirecionamento e restauração.

### 1.3.3. Consistência, Disponibilidade e Quóruns

1.3.3.A. [2] Abrir o problema: o que pode ser lido quando há várias cópias.

1.3.3.B. [2] Contrapor linearizabilidade e consistência eventual.

1.3.3.C. [1][4] Enunciar o teorema CAP, citando Gilbert e Lynch, e explicar as duas saídas do sistema durante a partição.

1.3.3.D. [5] Complementar com o PACELC: o compromisso que persiste mesmo sem partição.

1.3.3.E. [1] Introduzir os quóruns como ajuste desse equilíbrio, apresentando \(N\), \(W\) e \(R\).

1.3.3.F. [1][5]

\[
R + W > N,
\]

1.3.3.G. [1][5] Justificar a condição pela sobreposição entre leitura e escrita.

1.3.3.H. [2] Abrir o problema das transações que alteram várias partições e da atomicidade.

1.3.3.I. [1][4] Descrever as duas fases do 2PC, citando Kleppmann e Riccomini.

1.3.3.J. [1][5] Discutir o custo do 2PC: rodadas de rede e bloqueio se o coordenador falhar.

1.3.3.K. [5] Concluir por que muitos sistemas limitam transações a uma partição.

### 1.3.4. Modelos e Arquiteturas

1.3.4.A. [3] Mostrar que os mecanismos anteriores reaparecem em abstrações diferentes.

1.3.4.B. [2] Exemplificar com sistemas de arquivos distribuídos, Bigtable, Dynamo e armazenamento de objetos, indicando a prioridade de cada um.

1.3.4.C. [1] Fechar com shared-nothing e a separação entre computação e armazenamento.

## 1.4. Limitações, Trade-offs e Desafios Atuais

1.4.A. [1][3] Afirmar que não existe arquitetura universalmente superior.

1.4.B. [1][5] Bullets com os quatro compromissos do projeto, retomando as seções anteriores.

1.4.C. [5] Mencionar os códigos de apagamento e seu custo de reconstrução.

1.4.D. [1] Concluir que a arquitetura parte do workload, contrastando sistema bancário e catálogo de produtos.

## 1.5. Conclusão

1.5.A. [3] Diagrama de síntese.

1.5.B. [3] Sintetizar o papel do particionamento e da replicação e o custo de coordenar cópias.

1.5.C. [1][3] Concluir que cada aplicação deve receber o nível de consistência de que realmente precisa.

## Referências

R.A. [4] Referências em ABNT.
