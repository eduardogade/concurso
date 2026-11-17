# Ponto 8 — MLOps: Automação, Implantação e Infraestrutura de Aprendizado de Máquina

## 1. Introdução e Delimitação do Problema

Após a validação de um modelo, surge um problema distinto do desenvolvimento experimental: **como transformá-lo em um sistema executável, automatizado, escalável, disponível e recuperável**. Em sistemas reais, o código do modelo é apenas uma pequena parte do sistema em produção [1]:

```text
modelo validado ≠ sistema operacional confiável
```

Este ponto trata, portanto, de **entrega e operação**; a observação contínua, a governança e a manutenção do modelo em produção constituem um problema posterior.

## 2. Fundamentos e Relevância

A automação busca substituir sequências manuais e pouco reproduzíveis por processos explícitos, verificáveis e repetíveis. Pipelines de ML podem encadear ingestão e validação de dados, transformação, treinamento, avaliação, testes, registro, promoção e implantação [2].

Três conceitos devem ser distinguidos. A **Integração Contínua (CI)** integra e valida mudanças, tipicamente por testes automáticos. A **Entrega ou Implantação Contínua (CD)** promove artefatos aprovados para ambientes-alvo. Já o **Continuous Training (CT)** aciona novo treinamento quando condições previamente definidas são satisfeitas, como chegada de novos dados ou mudanças relevantes; CT não é retreinamento indiscriminado.

A automação deve permanecer subordinada a critérios explícitos de aceitação, ou *quality gates* [3]:

```text
promoção ⇒ critérios satisfeitos
```

## 3. Núcleo Técnico

### 3.1. Empacotamento e Implantação

Implantar um modelo não é apenas copiar seu arquivo de pesos. A unidade implantável pode incluir:

```text
artefato de implantação = modelo + código + runtime + dependências + configuração
```

além de pré-processamento, pós-processamento e contratos de entrada e saída. **Containers** empacotam esses componentes com isolamento e portabilidade, reduzindo a divergência entre o ambiente validado e o ambiente implantado.

Diferentes estratégias podem ser utilizadas para liberar novas versões [4]:

- **recreate**: substituição completa da versão anterior;
- **rolling update**: substituição gradual das instâncias;
- **blue-green**: manutenção paralela de dois ambientes;
- **canary**: exposição inicial de pequena parcela do tráfego à nova versão.

Essas estratégias equilibram de modo distinto risco, disponibilidade e custo. Um sistema maduro deve ainda permitir **rollback** para a versão estável:

```text
release confiável = artefato versionado + estratégia de implantação + rollback
```

### 3.2. Serving e Padrões de Inferência

**Model serving** corresponde à disponibilização do modelo para inferência, cuja arquitetura depende de latência, volume, frequência, custo e criticidade. Na **inferência batch**, dados acumulados são processados periodicamente, o que é adequado quando o volume é elevado e maior latência é aceitável. Na **inferência online**, cada requisição recebe resposta próxima do tempo real:

```text
REQUISIÇÃO → PRÉ-PROCESSAMENTO → MODELO → PREDIÇÃO → RESPOSTA
```

o que exige controle de latência, disponibilidade, concorrência, picos de carga e falhas. Em **streaming**, eventos são processados continuamente à medida que chegam. **Latência** (tempo de resposta) e **throughput** (requisições processadas por unidade de tempo) são conceitos distintos.

O **training-serving skew** ocorre quando o processamento na inferência difere do treinamento: o mesmo modelo, com *features* diferentes, comporta-se de modo diferente. Transformações e contratos de dados devem permanecer compatíveis entre treinamento e produção.

### 3.3. Infraestrutura, Containers e Orquestração

A infraestrutura fornece CPU, GPU e outros aceleradores, memória, armazenamento e rede. Containers resolvem principalmente **empacotamento e isolamento**, mas não fornecem sozinhos escalabilidade ou disponibilidade. Quando existem múltiplas instâncias, entra a **orquestração**, que inicia e remove instâncias, aloca recursos, reinicia componentes, distribui carga, realiza atualizações e escala réplicas:

```text
CONTAINER → como executar de forma isolada?
ORQUESTRAÇÃO → como coordenar muitas execuções?
```

### 3.4. Escalabilidade e Disponibilidade

A escala **vertical** adiciona recursos por instância; a **horizontal**, mais instâncias, sendo especialmente útil para serviços replicáveis e *stateless*. Com várias réplicas, **balanceadores de carga** distribuem requisições entre elas:

```text
REQUISIÇÕES
↓
LOAD BALANCER
↙   ↓   ↘
I1     I2     I3
```

O **autoscaling** ajusta a capacidade à demanda. Entretanto:

```text
escalabilidade ≠ disponibilidade
```

Um sistema pode suportar grande carga e ainda possuir pontos únicos de falha. Alta disponibilidade exige também redundância, replicação, reinicialização automática e mecanismos de recuperação, de modo que a falha de um componente não implique a falha do sistema.

## 4. Limitações, Trade-offs e Desafios Atuais

A infraestrutura de ML envolve múltiplos compromissos:

- latência × custo;
- disponibilidade × custo;
- automação × complexidade;
- sofisticação arquitetural × simplicidade operacional.

Recursos insuficientes produzem **underprovisioning** (demanda > capacidade), com filas, aumento de latência e indisponibilidade; recursos excessivos produzem **overprovisioning** (capacidade ≫ demanda), com desperdício. O objetivo operacional é capacidade ≈ demanda, com margem suficiente para absorver variações. Alta disponibilidade e baixa latência exigem redundância e provisionamento, elevando custos.

Por isso, arquitetura mais sofisticada não é arquitetura melhor: a infraestrutura deve ser proporcional aos requisitos da aplicação. Resiliência também inclui capacidade de recuperação, *rollback* e, quando apropriado, **degradação graciosa**, como usar versão anterior, modelo simplificado ou mecanismo de *fallback*.

## 5. Conclusão

Em síntese:

```text
MODELO VALIDADO
↓
AUTOMAÇÃO
↓
EMPACOTAMENTO
↓
IMPLANTAÇÃO
↓
SERVING
↓
ESCALA E DISPONIBILIDADE
↓
OPERAÇÃO CONFIÁVEL
```

Todo esse fluxo é atravessado por:

```text
VALIDAÇÃO + VERSIONAMENTO + RECUPERAÇÃO + CONTROLE DE CUSTO
```

Assim, uma arquitetura de MLOps adequada não é a mais complexa nem a de menor latência possível, mas aquela que satisfaz de forma controlada os requisitos de **desempenho, escalabilidade, disponibilidade, resiliência, custo e risco**.

## Referências

[1] SCULLEY, D. et al. *Hidden Technical Debt in Machine Learning Systems*. 2015.
[2] KREUZBERGER, D.; KÜHL, N.; HIRSCHL, S. *Machine Learning Operations (MLOps): Overview, Definition, and Architecture*. 2023.
[3] BRECK, E. et al. *The ML Test Score: A Rubric for ML Production Readiness and Technical Debt Reduction*. 2017.
[4] TREVEIL, M. et al. *Introducing MLOps: How to Scale Machine Learning in the Enterprise*. 2020.
