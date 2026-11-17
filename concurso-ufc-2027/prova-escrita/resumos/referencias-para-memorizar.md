# Referências para memorizar

A seleção abaixo é a que já está nas dissertações v3 (`_v3-prosa.md`): três obras por ponto, 28 obras distintas. As trocas da seção 4 são apenas sugestões; as dissertações não foram alteradas.

## 1. Mapa por ponto

| Ponto | Autor-gatilho | Obra | Ano | Reutilizada em |
|---|---|---|---|---|
| 1 | Ghemawat | The Google file system | 2003 | — |
| 1 | Gilbert | Brewer's conjecture [...] | 2002 | — |
| 1 | Kleppmann | Designing data-intensive applications | 2026 | — |
| 2 | Amdahl | Validity of the single processor approach [...] | 1967 | — |
| 2 | Dean | MapReduce: simplified data processing on large clusters | 2004 | — |
| 2 | Zaharia | Resilient distributed datasets [...] | 2012 | — |
| 3 | Akidau | The dataflow model [...] | 2015 | — |
| 3 | Carbone | State management in Apache Flink [...] | 2017 | — |
| 3 | Kreps | Kafka: a distributed messaging system for log processing | 2011 | — |
| 4 | Fayyad | From data mining to knowledge discovery in databases | 1996 | — |
| 4 | Tukey | Exploratory data analysis | 1977 | — |
| 4 | Han | Data mining: concepts and techniques | 2022 | — |
| 5 | Bishop | Pattern recognition and machine learning | 2006 | — |
| 5 | Hastie | The elements of statistical learning | 2009 | — |
| 5 | Goodfellow | Deep learning | 2016 | — |
| 6 | Sutton | Reinforcement learning: an introduction | 2018 | — |
| 6 | Watkins | Q-learning | 1992 | — |
| 6 | Mnih | Human-level control through deep reinforcement learning | 2015 | — |
| 7 | Sculley | Hidden technical debt in machine learning systems | 2015 | 8 |
| 7 | Amershi | Software engineering for machine learning: a case study | 2019 | — |
| 7 | Kreuzberger | Machine learning operations (MLOps) [...] | 2023 | 8 |
| 8 | Breck | The ML test score [...] | 2017 | — |
| 9 | Gama | A survey on concept drift adaptation | 2014 | — |
| 9 | ISO/IEC | ISO/IEC 42001 | 2023 | — |
| 9 | Brasil | Lei nº 13.709 (LGPD) | 2018 | — |
| 10 | Molnar | Interpretable machine learning | 2025 | — |
| 10 | Lundberg | A unified approach to interpreting model predictions | 2017 | — |
| 10 | Ribeiro | "Why should I trust you?" [...] | 2016 | — |

O "[...]" indica título longo abreviado, como a NBR 6023 permite (supressão das últimas palavras).

## 2. Padrões que facilitam a memória

- **Autor único (o mais fácil):** Amdahl, Tukey, Bishop, Molnar.
- **Quatro ou mais autores (basta "et al."):** Zaharia, Akidau, Carbone, Mnih, Sculley, Amershi, Breck, Gama.
- **Dois autores (escrever ambos):** Gilbert e Lynch; Kleppmann e Riccomini; Dean e Ghemawat; Sutton e Barto; Watkins e Dayan; Lundberg e Lee.
- **Três autores (escrever os três):** Ghemawat, Gobioff e Leung; Kreps, Narkhede e Rao; Fayyad, Piatetsky-Shapiro e Smyth; Han, Pei e Tong; Hastie, Tibshirani e Friedman; Goodfellow, Bengio e Courville; Kreuzberger, Kühl e Hirschl; Ribeiro, Singh e Guestrin.
- **Ghemawat aparece duas vezes:** é o primeiro autor do GFS (P1) e o segundo do MapReduce (P2). O Google sustenta os dois pontos.
- **Pares por editora ou veículo:**
  - Springer: Bishop e Hastie (P5).
  - MIT Press: Goodfellow (P5) e Sutton (P6).
  - Proceedings of the VLDB Endowment: Akidau e Carbone (P3).
  - O'Reilly: Kleppmann (P1).
- **Bloco MLOps:** Sculley e Kreuzberger servem a P7 e P8; Breck completa P8, e Amershi completa P7.
- **Ordem cronológica coincidente:** em P2 (1967, 2004, 2012) e em P7 (2015, 2019, 2023), a ordem de citação acompanha os anos.

## 3. Bibliografia em ABNT

Volumes, números, páginas e locais seguem o Apêndice B do relatório 04. Quando o dado não estava confirmado, foi omitido.

### Processamento de dados em larga escala (Pontos 1 a 3)

AKIDAU, T. et al. The dataflow model: a practical approach to balancing correctness, latency, and cost in massive-scale, unbounded, out-of-order data processing. **Proceedings of the VLDB Endowment**, v. 8, n. 12, p. 1792-1803, 2015.

AMDAHL, G. M. Validity of the single processor approach to achieving large scale computing capabilities. In: AFIPS SPRING JOINT COMPUTER CONFERENCE, 1967, Atlantic City. **Proceedings** [...]. New York: ACM, 1967. p. 483-485.

CARBONE, P. et al. State management in Apache Flink: consistent stateful distributed stream processing. **Proceedings of the VLDB Endowment**, v. 10, n. 12, p. 1718-1729, 2017.

DEAN, J.; GHEMAWAT, S. MapReduce: simplified data processing on large clusters. In: SYMPOSIUM ON OPERATING SYSTEMS DESIGN AND IMPLEMENTATION, 6., 2004, San Francisco. **Proceedings** [...]. Berkeley: USENIX Association, 2004. p. 137-150.

GHEMAWAT, S.; GOBIOFF, H.; LEUNG, S.-T. The Google file system. In: ACM SYMPOSIUM ON OPERATING SYSTEMS PRINCIPLES, 19., 2003, Bolton Landing. **Proceedings** [...]. New York: ACM, 2003. p. 29-43.

GILBERT, S.; LYNCH, N. Brewer's conjecture and the feasibility of consistent, available, partition-tolerant web services. **ACM SIGACT News**, v. 33, n. 2, p. 51-59, 2002.

KLEPPMANN, M.; RICCOMINI, C. **Designing data-intensive applications**. 2. ed. Sebastopol: O'Reilly, 2026.

KREPS, J.; NARKHEDE, N.; RAO, J. Kafka: a distributed messaging system for log processing. In: NETWORKING MEETS DATABASES WORKSHOP (NetDB), 2011, Athens. **Proceedings** [...]. 2011.

ZAHARIA, M. et al. Resilient distributed datasets: a fault-tolerant abstraction for in-memory cluster computing. In: USENIX SYMPOSIUM ON NETWORKED SYSTEMS DESIGN AND IMPLEMENTATION, 9., 2012, San Jose. **Proceedings** [...]. Berkeley: USENIX Association, 2012. p. 15-28.

### Mineração de dados e aprendizado de máquina (Pontos 4 a 6)

BISHOP, C. M. **Pattern recognition and machine learning**. New York: Springer, 2006.

FAYYAD, U.; PIATETSKY-SHAPIRO, G.; SMYTH, P. From data mining to knowledge discovery in databases. **AI Magazine**, v. 17, n. 3, p. 37-54, 1996.

GOODFELLOW, I.; BENGIO, Y.; COURVILLE, A. **Deep learning**. Cambridge, MA: MIT Press, 2016.

HAN, J.; PEI, J.; TONG, H. **Data mining**: concepts and techniques. 4. ed. Morgan Kaufmann, 2022.

HASTIE, T.; TIBSHIRANI, R.; FRIEDMAN, J. **The elements of statistical learning**: data mining, inference, and prediction. 2. ed. New York: Springer, 2009.

MNIH, V. et al. Human-level control through deep reinforcement learning. **Nature**, v. 518, n. 7540, p. 529-533, 2015.

SUTTON, R. S.; BARTO, A. G. **Reinforcement learning**: an introduction. 2. ed. Cambridge, MA: MIT Press, 2018.

TUKEY, J. W. **Exploratory data analysis**. Reading: Addison-Wesley, 1977.

WATKINS, C. J. C. H.; DAYAN, P. Q-learning. **Machine Learning**, v. 8, n. 3-4, p. 279-292, 1992.

### MLOps (Pontos 7 a 9)

AMERSHI, S. et al. Software engineering for machine learning: a case study. In: INTERNATIONAL CONFERENCE ON SOFTWARE ENGINEERING: SOFTWARE ENGINEERING IN PRACTICE, 41., 2019, Montreal. **Proceedings** [...]. Piscataway: IEEE, 2019. p. 291-300.

BRASIL. Lei nº 13.709, de 14 de agosto de 2018. Lei Geral de Proteção de Dados Pessoais (LGPD). **Diário Oficial da União**: seção 1, Brasília, DF, 15 ago. 2018.

BRECK, E. et al. The ML test score: a rubric for ML production readiness and technical debt reduction. In: IEEE INTERNATIONAL CONFERENCE ON BIG DATA, 2017, Boston. **Proceedings** [...]. Piscataway: IEEE, 2017. p. 1123-1132.

GAMA, J. et al. A survey on concept drift adaptation. **ACM Computing Surveys**, v. 46, n. 4, art. 44, 2014.

INTERNATIONAL ORGANIZATION FOR STANDARDIZATION; INTERNATIONAL ELECTROTECHNICAL COMMISSION. **ISO/IEC 42001**: information technology: artificial intelligence: management system. Geneva: ISO, 2023.

KREUZBERGER, D.; KÜHL, N.; HIRSCHL, S. Machine learning operations (MLOps): overview, definition, and architecture. **IEEE Access**, v. 11, p. 31866-31879, 2023.

SCULLEY, D. et al. Hidden technical debt in machine learning systems. In: ADVANCES IN NEURAL INFORMATION PROCESSING SYSTEMS, 28., 2015, Montreal. **Proceedings** [...]. 2015. p. 2503-2511.

### XAI (Ponto 10)

LUNDBERG, S. M.; LEE, S.-I. A unified approach to interpreting model predictions. In: ADVANCES IN NEURAL INFORMATION PROCESSING SYSTEMS, 30., 2017, Long Beach. **Proceedings** [...]. 2017. p. 4765-4774.

MOLNAR, C. **Interpretable machine learning**: a guide for making black box models explainable. 3. ed. 2025.

RIBEIRO, M. T.; SINGH, S.; GUESTRIN, C. "Why should I trust you?": explaining the predictions of any classifier. In: ACM SIGKDD INTERNATIONAL CONFERENCE ON KNOWLEDGE DISCOVERY AND DATA MINING, 22., 2016, San Francisco. **Proceedings** [...]. New York: ACM, 2016. p. 1135-1144.

Na prova, use a forma curta das listas das v3 (autor, título, veículo e ano). Os dados completos acima servem para conferência.

## 4. Sugestões (não aplicadas às dissertações)

- **P1, Kleppmann:** a 1ª edição tem um único autor, o que é mais fácil de lembrar: KLEPPMANN, M. **Designing data-intensive applications**. Sebastopol: O'Reilly, 2017. Em troca, perde-se a atualização da 2ª edição (2026). Ou mantenha a 2ª edição, pensando em "K&R".
- **Kleppmann como reserva em P2 e P3:** o livro trata de processamento em lote e de fluxos. Se esquecer uma referência nesses pontos, ele é cientificamente pertinente e já está memorizado. Use-o como reserva, sem tirar Dean, Zaharia ou Akidau.
- **P4, Han, Pei e Tong (três autores):** a alternativa de autor único é AGGARWAL, C. C. **Data mining**: the textbook. Springer, 2015. Ela cobre associação e anomalias e repete a Springer de P5. Han continua sendo a obra mais canônica.
- **P5, Hastie et al. (três autores):** a alternativa de autor único é MURPHY, K. P. **Machine learning**: a probabilistic perspective. Cambridge, MA: MIT Press, 2012, que repete a MIT Press de P5 e P6. Para viés e variância, porém, Hastie é a fonte mais associada ao tema; só troque se a lista de três nomes for um obstáculo real.
- **P9, reaproveitamento:** Sculley et al. (2015), já memorizado em P7 e P8, também trata da degradação dos sistemas de ML em produção e poderia sustentar a frase de abertura de 9.1. Breck et al. (2017), de P8, inclui testes de monitoramento e poderia apoiar 9.3.2. As duas opções são acréscimos opcionais, não trocas.
- **Pendências de verificação:**
  - Editora da 3ª edição de Molnar: a v3 usa Leanpub, conforme a Auditoria 2, mas aqui ficou omitida.
  - Local de publicação da 4ª edição de Han, Pei e Tong: omitido.
  - Em 2015 e 2017, o evento de Sculley e de Lundberg ainda se chamava NIPS; as v3 usam "NeurIPS", o nome atual.
