# Ponto 9 — MLOps: Monitoramento, Governança e Manutenção de Modelos

## 9.1. Introdução e Delimitação do Problema

9.1.A. [2] Afirmar que a implantação não encerra o ciclo de vida e enumerar o que muda com o tempo.

9.1.B. [3] Quadro contrapondo modelo implantado e modelo permanentemente válido.

9.1.C. [2] Apresentar o objetivo: detectar, diagnosticar e controlar intervenções.

9.1.D. [3] Delimitar o ponto: observar, governar e manter.

## 9.2. Fundamentos e Relevância

9.2.A. [3] Quadro com as duas dimensões da saúde de um sistema de ML.

9.2.B. [2] Contrapor monitoramento operacional e monitoramento de ML.

9.2.C. [2] Introduzir a observabilidade pelos três sinais e o que cada um indica.

9.2.D. [2] Mencionar SLIs e SLOs como base dos alertas.

## 9.3. Núcleo Técnico

### 9.3.1. Qualidade de Dados, Data Drift e Concept Drift

9.3.1.A. [2] Introduzir os problemas de qualidade de dados, com exemplos.

9.3.1.B. [2] Introduzir o data drift.

9.3.1.C. [1][5]

\[
P_{t}(X) \neq P_{\text{train}}(X)
\]

9.3.1.D. [5] Diferenciar o covariate shift.

9.3.1.E. [2][4] Introduzir o concept drift, citando Gama et al., com o exemplo dos fraudadores.

9.3.1.F. [1][5]

\[
P_{t}(Y \mid X) \neq P_{\text{train}}(Y \mid X)
\]

9.3.1.G. [3] Quadro com as quatro perguntas de diagnóstico.

9.3.1.H. [1][5] Ressaltar que drift não é degradação comprovada e justificar nos dois sentidos.

9.3.1.I. [1][5] Explicar a detecção de drift, nomeando KS, qui-quadrado e PSI e o papel de cada um.

9.3.1.J. [5] Porém, alertar que significância não basta e indicar o que importa.

### 9.3.2. Monitoramento Preditivo e Detecção de Degradação

9.3.2.A. [1] Explicar o monitoramento quando há ground truth disponível.

9.3.2.B. [5] Alertar que métricas agregadas escondem degradação gradual ou localizada.

9.3.2.C. [1] Introduzir o atraso no feedback, com o exemplo do empréstimo.

9.3.2.D. [1] Apresentar os sinais indiretos e o seu limite.

9.3.2.E. [1][5] Discutir a detecção por limiar, \(M_{t} < \tau \Rightarrow\) alerta, e o compromisso entre sensibilidade e estabilidade.

9.3.2.F. [1][3] Concluir que degradação não é causa identificada, e indicar o fluxo correto em três passos.

### 9.3.3. Governança, Auditoria e Lineage

9.3.3.A. [2][3] Quadro com os três componentes da governança.

9.3.3.B. [2] Enumerar o que deve ser identificável em cada modelo.

9.3.3.C. [1] Apresentar o lineage e a trilha de auditoria.

9.3.3.D. [1][5] Justificar a governança proporcional ao risco, contrastando crédito e recomendação de filmes.

9.3.3.E. [4] Citar a ISO/IEC 42001 e a LGPD, indicando quando a LGPD se aplica.

### 9.3.4. Manutenção, Retreinamento e Ciclo de Vida

9.3.4.A. [1][3] Quadro contrapondo drift detectado e retreinamento obrigatório.

9.3.4.B. [1][5] Justificar com causas em que retreinar apenas incorpora o erro.

9.3.4.C. [2] Enumerar as intervenções possíveis.

9.3.4.D. [1] Contrapor retreinamento periódico e orientado por eventos.

9.3.4.E. [1][5] Explicar que o modelo retreinado não é promovido automaticamente, com o champion–challenger.

## 9.4. Limitações, Trade-offs e Desafios Atuais

9.4.A. [1] Enumerar os trade-offs do monitoramento e da manutenção.

9.4.B. [1] Discutir o excesso de alertas.

9.4.C. [1][5] Alertar para o risco do retreinamento automático mal governado.

## 9.5. Conclusão

9.5.A. [3] Diagrama de síntese.

9.5.B. [1][3] Concluir que manter um modelo é demonstrar controle, e não apenas mantê-lo executando.

## Referências

R.A. [4] Referências em ABNT.
