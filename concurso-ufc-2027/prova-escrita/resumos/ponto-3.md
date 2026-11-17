# Ponto 3 — Processamento de Dados em Larga Escala: Processamento de Fluxos e Arquiteturas de Dados

## 3.1. Introdução e Delimitação do Problema

3.1.A. [2] Contrapor processamento de fluxos e processamento batch.

3.1.B. [1] Delimitar o problema: produzir resultados corretos com eventos atrasados ou fora de ordem, estado e falhas.

3.1.C. [3] Justificar a análise conjunta de fluxos e arquiteturas pelos quatro eixos: tempo, estado, garantias e armazenamento.

## 3.2. Fundamentos e Relevância

3.2.A. [2] Distinguir dados bounded e unbounded.

3.2.B. [1] Ressaltar que batch e streaming não se excluem, indicando o uso de cada um.

3.2.C. [2] Introduzir latência e throughput.

3.2.D. [1] Relacionar o particionamento do fluxo ao ganho de throughput e à perda da ordem global.

## 3.3. Núcleo Técnico

### 3.3.1. Tempo, Janelas e Watermarks

3.3.1.A. [2] Contrapor event time e processing time.

3.3.1.B. [1] Justificar a distinção pelos eventos fora de ordem e pelo risco de agregar no intervalo errado.

3.3.1.C. [2] Introduzir as janelas como resposta a um fluxo sem fim, com os três tipos e o exemplo dos últimos 5 minutos.

3.3.1.D. [2][4] Apresentar o modelo Dataflow, citando Akidau et al., com bullets dos três mecanismos que ele articula.

3.3.1.E. [1][5] Ressaltar que o watermark é estimativa, não garantia, e a consequência dos eventos tardios.

3.3.1.F. [5] Discutir o compromisso entre latência, completude e custo de estado.

### 3.3.2. Estado, Recuperação e Semântica de Processamento

3.3.2.A. [2] Introduzir as operações stateful, com exemplos de informação acumulada.

3.3.2.B. [1][5]

\[
(s_{t + 1},y_{t}) = f(s_{t},x_{t})
\]

3.3.2.C. [2] Identificar cada símbolo da equação.

3.3.2.D. [1][4] Explicar a recuperação por fontes relíveis, checkpoints e replay, citando o Apache Flink.

3.3.2.E. [1] Derivar daí as três garantias de processamento e o risco de cada uma.

3.3.2.F. [1][5] Precisar que exactly-once se refere ao efeito sobre o estado, não à entrega física.

3.3.2.G. [5] Estender a garantia de ponta a ponta, com o requisito sobre o sink.

### 3.3.3. Logs Distribuídos e Arquiteturas Orientadas a Eventos

3.3.3.A. [2] Introduzir as arquiteturas orientadas a eventos pelo desacoplamento entre produtores e consumidores.

3.3.3.B. [1][4] Apresentar o log distribuído do Kafka, citando Kreps et al.

3.3.3.C. [1][5] Explicar como o offset permite consumidores independentes e replay, ligando à recuperação da seção anterior.

3.3.3.D. [1] Discutir a ordem por partição como troca entre ordenação global e escalabilidade.

3.3.3.E. [1] Distinguir o log do motor de processamento, nomeando exemplos e o que cabe ao motor.

### 3.3.4. Integração Batch/Streaming e Arquiteturas de Dados

3.3.4.A. [2] Apresentar a Lambda Architecture pelas duas camadas.

3.3.4.B. [1] Discutir seu ganho e o custo da duplicação.

3.3.4.C. [1][5] Contrapor a Kappa Architecture e explicar a recomputação por replay.

3.3.4.D. [2][4] Fechar com data lakes e com o que o lakehouse acrescenta.

## 3.4. Limitações, Trade-offs e Desafios Atuais

3.4.A. [1][3] Afirmar que não existe arquitetura universalmente superior.

3.4.B. [1][5] Discutir o custo das garantias fortes e da retenção longa.

3.4.C. [1] Introduzir o risco dos desequilíbrios sustentados entre produção e consumo.

3.4.D. [1][5]

\[
\lambda_{\text{produção}} > \lambda_{\text{consumo}},
\]

3.4.E. [1][5] Explicar o crescimento do backlog e contrapor buffers a backpressure e elasticidade.

3.4.F. [1] Ressaltar que desacoplar não dispensa contratos de dados e controle de esquemas.

3.4.G. [3] Concluir com o princípio da menor complexidade capaz de satisfazer as garantias.

## 3.5. Conclusão

3.5.A. [3] Diagrama de síntese.

3.5.B. [3] Sintetizar a integração entre dados em movimento e dados persistidos.

3.5.C. [1] Concluir que a escolha entre batch, streaming ou híbridos decorre das garantias exigidas, não da tecnologia mais recente.

## Referências

R.A. [4] Referências em ABNT.
