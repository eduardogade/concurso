# Relatório 07 — Dissertações V3 em prosa

Dez arquivos `<N>-<nome>_v3-prosa.md`, ao lado das v2, em `prova-escrita/`. As v2, os baremas, o edital e os relatórios 01–06 não foram alterados. Nenhum arquivo `_v3.md` foi criado.

**Resumo.** As v3 ficaram cerca de 7% mais curtas na prosa (7.744 → 7.172 palavras). Ainda assim, cada ponto ganhou um mecanismo central que faltava: 2PC, EDA concreta, IaC, Shapley, Monte Carlo × TD, entre outros. Todas cabem nos 80 minutos pelo modelo conservador abaixo; nas v2, só os Pontos 1 e 8 cabiam.

## 1. Como o tempo foi estimado

- **Velocidade:** 14 palavras/min (informada). A escrita da prosa leva um acréscimo de 15% pelo esforço de reconstruir de memória e compor o argumento. Na prática, isso equivale a cerca de 12 palavras/min.
- **Fórmulas:** 1,9 s por símbolo, mais 0,4 min por fórmula destacada (diagramação e recordação). Notação inline também conta por símbolo.
- **Quadros e diagramas:** palavras e setas a 1,2 × o tempo da prosa, mais 0,05 min por linha.
- **Referências:** contam como prosa.
- **Reservas:** 4 min de esqueleto e 4 min de revisão.
- **"Margem":** o que sobra dos 80 min depois de tudo isso. Na prova, a folga real é a margem somada aos 4 min de revisão.
- **"Palavras":** prosa do corpo, incluindo títulos de seção e excluindo fórmulas, quadros e referências.

Pelo mesmo modelo, as v2 somavam de 76,7 a 94,1 min por ponto.

## 2. Visão geral

| Ponto | Palavras v2 | Palavras v3 | Conceitos adicionados | Conceitos removidos | Tempo estimado (v2) | Veredito |
|---|---|---|---|---|---|---|
| 1 | 769 | 756 | 2PC e atomicidade distribuída (parágrafo novo); PACELC (uma frase); mecanismo do anel no *consistent hashing* | Nenhum conceito. Saíram as citações de Dynamo, Herlihy e Bigtable (os nomes continuam no texto) | 76,7 (76,7) | Factível, margem 3,3 |
| 2 | 803 | 725 | RDD, avaliação preguiçosa, dependências estreitas × largas; exemplo da contagem de palavras; limite 1/s de Amdahl | Nenhum. Gustafson deixa de ser citado (strong/weak scaling ficam) | 77,1 (82,5) | Factível, margem 2,9 |
| 3 | 802 | 731 | *Offset* do Kafka ligado ao *replay*; ACID no lakehouse; Flink e Spark Structured Streaming nomeados pela função | Nenhum. Saiu a cadeia FONTE→…→SERVING, que repetia a conclusão | 76,5 (81,7) | Factível, margem 3,5 |
| 4 | 783 | 699 | EDA concreta (parágrafo novo); um mecanismo por família de detecção de anomalias | Nenhum. Saíram dois quadros (ver 3.4) e a citação de Aggarwal | 77,2 (83,7) | Factível, margem 2,8 |
| 5 | 759 | 711 | Risco empírico; L1 × L2; princípio de cada algoritmo; ponte *deep learning* → MLOps (parágrafo novo) | k-NN; modelos de mistura | 78,2 (84,8) | Factível, margem 1,8 |
| 6 | 766 | 697 | Monte Carlo × TD (parágrafo novo); *deadly triad* e DQN (*experience replay*, *target network*) | Nenhum conceito. Saíram 7 fórmulas e 2 quadros redundantes (ver 3.6) | 78,4 (94,1) | Factível, margem 1,6 |
| 7 | 733 | 721 | Busca de hiperparâmetros e superajuste à validação/*benchmark* (parágrafo novo); Git, DVC e MLflow pela função | Nenhum. Saíram 3 quadros e a citação de Breck | 77,8 (80,5) | Factível, margem 2,2 |
| 8 | 721 | 736 | IaC (parágrafo novo); *feature store*; Airflow/Kubeflow, Docker e Kubernetes pela função | Nenhum. Saíram 4 quadros e a citação de Treveil | 78,0 (79,2) | Factível, margem 2,0 |
| 9 | 790 | 692 | KS, qui-quadrado e PSI; ISO/IEC 42001 e LGPD; exemplo de *concept drift* | Nenhum. Saíram a frase governança ≠ XAI e 2 quadros | 78,0 (86,5) | Factível, margem 2,0 |
| 10 | 818 | 704 | Valores de Shapley (parágrafo curto) | Nenhum conceito central. Saíram a lista família→pergunta, a frase sobre racionalizações e o detalhe do Integrated Gradients | 77,8 (86,5) | Factível, margem 2,2 |

Em todos os pontos, a seção de referências passou a ter três obras, com título. Isso custa de 0,5 a 1,5 min a mais que as listas sem título das v2, e esse custo já está incluído no tempo estimado.

## 3. Por ponto

Em cada item, "Se atrasar" indica o corte para aplicar ao vivo se, no minuto 45, você estiver mais de 5 minutos atrasado.

### 3.1. Ponto 1 — Armazenamento e gerenciamento distribuído

- **Modificações:** parágrafo do 2PC no fim de 1.3.3, nas duas fases e com o custo do bloqueio. PACELC entra como continuação natural do CAP. O *consistent hashing* ganhou o mecanismo do anel. 1.3.4 foi condensada em uma frase por abstração. O diagrama da conclusão passou a dizer "CONSISTÊNCIA / QUÓRUNS / TRANSAÇÕES".
- **Por quê:** transações distribuídas eram a lacuna mais visível do ponto. Para pagá-las, saíram repetições de 1.2 e 1.4, mantendo o tempo da v2.
- **Rejeitado:**
  - BASE e NewSQL (da proposta P1-A): conceitos extras sem mecanismo.
  - MVCC (P1-O1).
  - Arquitetura detalhada do GFS (P1-C).
  - Citação de Abadi para o PACELC: evita uma 4ª referência.
- **Fórmulas e diagramas:** nada removido.
- **Dificuldades restantes:** o porquê de R + W > N (os dois conjuntos de réplicas se intersectam) e o significado das letras do PACELC.
- **Se atrasar:** reduzir 1.3.4 às duas primeiras abstrações.

### 3.2. Ponto 2 — Processamento paralelo e distribuído

- **Modificações:**
  - *Speedup* e eficiência passaram para a notação única S(p), E(p).
  - Amdahl ganhou o limite 1/s e o exemplo dos 10%.
  - MapReduce ganhou o exemplo da contagem de palavras.
  - 2.3.4 agora explica RDD, avaliação preguiçosa e como dependências estreitas e largas formam os estágios.
  - A lista final de trade-offs virou uma frase.
- **Por quê:** substituir nomes por funcionamento, seguindo o encadeamento pedido: distribuição, MapReduce, *shuffle*, DAG, estágios, recuperação.
- **Rejeitado:**
  - *Join* com *shuffle* × *broadcast* (P2-B).
  - YARN (P2-O1).
  - Gustafson como referência.
- **Fórmulas e diagramas:** a fórmula destacada de S_p/E_p virou notação inline. Amdahl e T_total ficam.
- **Dificuldades restantes:** a álgebra da fórmula de Amdahl e a definição de dependência estreita ("cada partição depende de poucas anteriores").
- **Se atrasar:** escrever T_total em palavras ("computação + comunicação + sincronização + *overhead*").

### 3.3. Ponto 3 — Fluxos e arquiteturas de dados

- **Modificações:**
  - Corrigida a imprecisão do Dataflow: agora "articula três mecanismos".
  - *Offsets* explicam por que o log permite *replay* e vários consumidores.
  - Flink e Spark Structured Streaming aparecem como motores de processamento.
  - Lakehouse ganhou ACID.
  - Retirada a repetição latência × completude de 3.4, que já está em 3.3.1.
- **Por quê:** o ponto já era forte. As mudanças corrigem um erro e tornam explícito o elo entre log e recuperação.
- **Rejeitado:**
  - *Consumer groups* (de P3-B só ficou o *offset*).
  - CDC (P3-O1).
  - Kreps 2014 como 4ª referência: a Kappa fica sem citação.
- **Fórmulas e diagramas:** removida a cadeia FONTE→…→SERVING, quase igual ao diagrama da conclusão.
- **Dificuldades restantes:** separar watermark (até onde o fluxo avançou) de trigger (quando emitir), e dizer que *exactly-once* trata do efeito, não da entrega.
- **Se atrasar:** escrever a desigualdade de λ em palavras.

### 3.4. Ponto 4 — KDD, EDA, padrões e anomalias

- **Modificações:**
  - EDA concreta em um parágrafo: média e desvio padrão × mediana e quartis, *boxplot* com a regra de 1,5 IQR, histogramas, diagramas de dispersão, Pearson e Spearman.
  - Anomalias: uma ideia de normalidade por família (escore z/IQR, k vizinhos, LOF, Isolation Forest), com a consequência da alta dimensionalidade.
  - Exemplo de anomalia contextual: consumo de energia de madrugada.
  - Correções "biologicamente" → "cientificamente" e "implausível".
- **Por quê:** era a prioridade do ponto. A regra do IQR liga a EDA à detecção de anomalias, o que ajuda a reconstruir o texto.
- **Rejeitado:**
  - Apriori (P4-O2).
  - Medidas de proximidade (P4-O1).
  - Crítica ao agrupamento (P4-C).
  - Uma aula de estatística.
- **Fórmulas e diagramas:** saíram os quadros "Data Mining ⊂ KDD" e "exploração → hipótese → …"; o caráter iterativo da EDA continua em prosa. As três fórmulas de associação ficam.
- **Dificuldades restantes:** não confundir confiança com lift (o lift divide a confiança por sup(Y)).
- **Se atrasar:** cortar o parágrafo padrão global/local em 4.3.2.

### 3.5. Ponto 5 — Supervisionado e não supervisionado

- **Modificações:**
  - A fórmula genérica virou o risco empírico, com a perda média explícita.
  - L1 × L2 explicadas em palavras, mantendo o quadro "objetivo = erro + λ·complexidade".
  - Cada algoritmo representativo ganhou "princípio → vantagem ou limitação":
    - linear e logística;
    - árvores (Gini/entropia);
    - *bagging*/Random Forest × *boosting*, ligados à variância e ao viés;
    - SVM (margem, *kernels*);
    - redes (gradiente, retropropagação);
    - k-means (dois passos, k-means++, grupos esféricos);
    - hierárquico, DBSCAN e PCA.
  - Em 5.4, um parágrafo liga *deep learning* (capacidade de representação, dados, computação, superajuste, reprodutibilidade, monitoramento) a MLOps.
- **Por quê:** é a área que você domina. Explicar o funcionamento mostra domínio e é mais fácil de reconstruir do que uma lista de nomes.
- **Rejeitado:**
  - Notação ‖θ‖₁, ‖θ‖₂ (P5-A formal): a versão em palavras basta.
  - Detalhar todos os algoritmos por igual.
  - Parâmetros C e γ do SVM (os *kernels* ficam, em meia frase).
- **Removido:**
  - k-NN e modelos de mistura, periféricos.
  - Os quadros "método = algoritmo + hipótese", "dados + objetivo … → método" e o de 5.1 (repetia a frase anterior).
  - A frase "a ausência de rótulos não significa ausência de critério": os itens já dizem o critério de cada método.
  - O diagrama da conclusão foi de 7 para 5 linhas.
- **Dificuldades restantes:** é a margem mais curta depois da do Ponto 6, compensada pela sua familiaridade com os algoritmos. O risco real é escrever demais sobre eles.
- **Se atrasar:** cortar o clustering hierárquico e o exemplo da fraude.

### 3.6. Ponto 6 — Aprendizado por reforço

- **Modificações:**
  - Ficam quatro fórmulas fundamentais: G_t, Bellman para V^π, atualização TD e Q-learning, cada uma seguida da explicação intuitiva.
  - V^π e Q^π definidas em palavras, com notação inline.
  - Novo parágrafo Monte Carlo × TD (viés × variância, *bootstrapping*).
  - A frase genérica sobre *deep RL* deu lugar à *deadly triad* e aos dois mecanismos do DQN.
  - Correção do ε-greedy: "uma ação ao acaso".
- **Por quê:** era o ponto mais longo (94 min estimados). Saíram as formalizações redundantes, não as fundamentais.
- **Rejeitado:**
  - Convergência do Q-learning (P6-O1).
  - RLHF (P6-O2).
  - PPO e formalização de *policy gradient*.
  - Williams como referência.
- **Fórmulas removidas:**
  - transição (S_t, A_t) → (R_{t+1}, S_{t+1});
  - MDP como fórmula destacada (ficou inline);
  - propriedade de Markov (ficou em palavras);
  - π* = argmax (o objetivo está em 6.1);
  - V^π e Q^π como fórmulas destacadas (ficaram em palavras);
  - Q* de otimalidade (substituída pela frase "a média dá lugar ao máximo");
  - a fórmula separada do erro δ_t (está dentro da atualização TD).
- **Quadros removidos:** "política → ações → retorno → …" e "valor presente = …", que virou a frase que introduz Bellman. Também saiu a lista de trade-offs.
- **Dificuldades restantes:** as duas atualizações se parecem. A regra para lembrar: Q-learning = TD aplicado a Q, com máximo no próximo estado.
- **Se atrasar:** omitir a fórmula TD, mantendo a frase do erro TD; o Q-learning já mostra a forma.

### 3.7. Ponto 7 — Desenvolvimento, versionamento e experimentação

- **Modificações:**
  - Parágrafo novo sobre a busca de hiperparâmetros (grade, aleatória, bayesiana) e o superajuste à validação e a *benchmarks*.
  - Git, DVC (guarda no Git só os *hashes*) e MLflow, pela função.
  - Exemplo da acurácia que subiu: algoritmo, dados ou semente?
  - O quadro "≈ D + C + H + E + S" virou resultado = f(D, C, H, E, S).
  - A lista do *tracking* virou frase.
- **Por quê:** a seleção ganhou conteúdo metodológico e as ferramentas aparecem pela função, não como catálogo.
- **Rejeitado:** CACE e dívida técnica (P7-C); Breck como 4ª referência.
- **Diagramas removidos:** o fluxo de seleção em 7.3.4 (quase igual ao da conclusão), "reprodutível ≠ idêntico bit a bit" (ficou em prosa) e "PROVENIÊNCIA + LINEAGE + REPRODUTIBILIDADE" (ficou como frase da conclusão).
- **Dificuldades restantes:** lembrar as cinco letras D, C, H, E, S.
- **Se atrasar:** escrever a cadeia de linhagem em uma linha de prosa.

### 3.8. Ponto 8 — Automação, implantação e infraestrutura

- **Modificações:**
  - 8.3.3 começa pelo problema da IaC (ambientes configurados à mão divergem), depois o mecanismo (estado desejado declarado, versionado, revisado e aplicado automaticamente, ex.: Terraform) e a consequência (recriar um ambiente é reexecutar a especificação).
  - *Feature store* como resposta ao *training-serving skew*.
  - Airflow/Kubeflow, Docker e Kubernetes nomeados pela função.
  - Exemplos de inferência *batch* e de infraestrutura desproporcional.
- **Por quê:** IaC é o elo entre "automação" e "infraestrutura" no título do ponto.
- **Rejeitado:** *shadow deployment* (P8-O1); latência por percentis (P8-O2); Treveil como referência (as estratégias de implantação ficam sem citação).
- **Diagramas removidos:** "release confiável = …" (dito em prosa), a cadeia da requisição online, o desenho do balanceador e "VALIDAÇÃO + VERSIONAMENTO + …".
- **Dificuldades restantes:** diferenciar *blue-green* (troca de todo o tráfego) de *canary* (pequena fração primeiro).
- **Se atrasar:** cortar *recreate* e *rolling update*.

### 3.9. Ponto 9 — Monitoramento, governança e manutenção

- **Modificações:**
  - Detecção de *drift* concreta: KS para variáveis contínuas, qui-quadrado para categóricas, PSI para magnitude, e por que significância não basta.
  - Exemplo de *concept drift* (fraudadores mudam de estratégia).
  - Governança proporcional ao risco, com exemplo (crédito × recomendador de filmes), ISO/IEC 42001 e LGPD em uma frase.
  - *Champion–challenger* explicado.
  - O atraso do *ground truth* ficou só em 9.3.2.
- **Por quê:** o ponto era forte. As mudanças são refinamentos e reduzem a extensão.
- **Rejeitado:**
  - NIST AI RMF: custaria uma 4ª referência; a ISO cobre "norma técnica" e a LGPD, a obrigação legal no Brasil.
  - *Feedback loops* (P9-C).
  - *Label shift* (P9-O1).
  - Sculley, Breck e Kreuzberger como referências.
- **Diagramas removidos:** "detecção automática ≠ correção automática" (a ideia continua na frase sobre automatizar demais) e "GOVERNANÇA + LINEAGE + AUDITORIA + GESTÃO DE RISCO".
- **Dificuldades restantes:** o papel de cada teste e a forma da referência da ISO.
- **Se atrasar:** cortar o quadro de quatro linhas DATA QUALITY / DRIFT…

### 3.10. Ponto 10 — XAI

- **Modificações:**
  - Shapley explicado pela intuição dos jogadores e da contribuição marginal média, com unicidade e custo exponencial.
  - LIME com o mecanismo (modelo linear ponderado pela proximidade).
  - Contrafactual com exemplo do que não é acionável ("reduzir a idade").
  - Estabilidade e discordância entre métodos em palavras, sem fórmula inline.
- **Por quê:** o texto estava adequado; o Shapley era a omissão mais visível.
- **Rejeitado:**
  - PDP/ICE (P10-B).
  - Wachter e Rudin como referências (P10-O1).
  - Nomes KernelSHAP/TreeSHAP e a lista dos quatro axiomas.
  - Sundararajan como referência.
- **Removido:**
  - A lista "família → pergunta" (a pergunta de cada família já está em sua descrição).
  - A frase sobre racionalizações (coberta por "plausibilidade ≠ fidelidade").
  - A geração de hipóteses científicas em 10.3.4.
- **Dificuldades restantes:** a fórmula do contrafactual.
- **Se atrasar:** omitir essa fórmula e manter a frase "a menor mudança que produz o resultado desejado".

## 4. Referências (ABNT simplificada)

- **Citação no texto:** sistema numérico com número em expoente (¹), em ordem de aparição (NBR 10520:2023). À mão, um número pequeno elevado.
- **Lista:** sobrenome em maiúsculas; todos os autores até três; "et al." a partir de quatro; título obrigatório; destaque em negrito no periódico ou livro, que à mão vira sublinhado.
- **Trabalhos em evento:** "In: SIGLA, ano." Local, páginas e *Proceedings* ficam de fora, como você autorizou.
- **Títulos longos:** abreviados com "[...]", como a NBR 6023:2018 permite (supressão das últimas palavras).
- **Exceção:** o título de Gilbert e Lynch ficou inteiro de propósito, porque soletra o próprio CAP ("consistent, available, partition-tolerant").
- **Atualizações:** Kleppmann e Riccomini, 2. ed., 2026; Han, Pei e Tong, 4. ed., 2022; Molnar, 3. ed., 2025 (conferidas na Auditoria 2); ISO/IEC 42001:2023; LGPD.
- **Incertezas:**
  - Em 2015 o evento ainda se chamava NIPS. "NeurIPS" é o nome atual e costuma ser aceito; se quiser exatidão histórica, escreva NIPS (Pontos 7 e 8).
  - A editora da 3ª edição de Molnar (Leanpub) segue o que foi registrado na Auditoria 2.
  - A referência da LGPD está na forma mínima (jurisdição, número, data e ementa).

## 5. Verificações automáticas

- **Cabeçalhos:** a sequência de títulos de cada v3 é idêntica à da v2 (texto, número, nível e ordem), nos dez arquivos.
- **Citações:** em cada ponto, as chamadas aparecem pela primeira vez na ordem 1, 2, 3, e cada número corresponde a uma entrada da lista. Não sobrou nenhuma chamada no formato [n].
- **Originais:** as v2, os baremas, o edital e os relatórios 01–06 mantêm as datas de modificação anteriores a esta tarefa.
