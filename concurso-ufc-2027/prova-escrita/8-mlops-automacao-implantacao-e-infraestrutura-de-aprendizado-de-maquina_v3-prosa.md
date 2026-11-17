# Ponto 8 — MLOps: Automação, Implantação e Infraestrutura de Aprendizado de Máquina

## 8.1. Introdução e Delimitação do Problema

Após a validação de um modelo, surge um problema distinto do desenvolvimento: **como transformá-lo em um sistema executável, automatizado, escalável, disponível e recuperável**. Em sistemas reais, o código do modelo é uma pequena parte do sistema em produção¹:

```text
modelo validado ≠ sistema operacional confiável
```

Este ponto trata de **entrega e operação**; monitoramento, governança e manutenção constituem um problema posterior.

## 8.2. Fundamentos e Relevância

A automação substitui sequências manuais, sujeitas a erro e difíceis de repetir, por processos explícitos e verificáveis. Um pipeline de ML encadeia ingestão e validação de dados, transformação, treinamento, avaliação, registro e implantação², orquestrados como um DAG por ferramentas como Airflow ou Kubeflow.

Três práticas devem ser distinguidas:

1. A **Integração Contínua (CI)** testa automaticamente cada mudança em código, dados e modelo.
2. A **Entrega ou Implantação Contínua (CD)** promove artefatos aprovados aos ambientes de destino.
3. O **Continuous Training (CT)** dispara novo treinamento sob condições definidas, como a chegada de novos dados; não é retreinamento indiscriminado.

A automação permanece subordinada a critérios explícitos de aceitação, os *quality gates*³:

```text
promoção ⇒ critérios satisfeitos
```

## 8.3. Núcleo Técnico

### 8.3.1. Empacotamento e Implantação

Implantar um modelo não é copiar seu arquivo de pesos. A unidade implantável inclui:

```text
artefato de implantação = modelo + código + runtime + dependências + configuração
```

além do pré e pós-processamento e do contrato de entrada e saída. **Containers**, como os do Docker, empacotam tudo isso em uma imagem isolada e portátil, de modo que a produção execute o mesmo ambiente que foi validado.

As estratégias de liberação equilibram risco, disponibilidade e custo: **recreate** substitui tudo de uma vez, com interrupção; **rolling update** troca as instâncias gradualmente; **blue-green** mantém dois ambientes e alterna o tráfego, permitindo retorno imediato; **canary** expõe a nova versão a uma pequena parcela do tráfego antes de ampliá-la. Em todos os casos, deve ser possível o **rollback** para a última versão estável.

### 8.3.2. Serving e Padrões de Inferência

O **model serving** disponibiliza o modelo para inferência. Na **inferência *batch***, previsões são calculadas periodicamente para muitos registros, como o escore de todos os clientes a cada noite, quando a resposta imediata é dispensável. Na **inferência *online***, cada requisição recebe resposta em milissegundos, o que exige controlar a latência (tempo por resposta), o *throughput* (respostas por segundo) e os picos de carga. Em **streaming**, eventos são processados à medida que chegam.

O **training-serving skew** ocorre quando as *features* são calculadas de um modo no treinamento e de outro na produção: o mesmo modelo, com entradas diferentes, comporta-se de forma diferente. As ***feature stores*** reduzem esse risco ao centralizar a definição de cada *feature* e servi-la de forma consistente ao treinamento (histórico) e à inferência (baixa latência).

### 8.3.3. Infraestrutura, Containers e Orquestração

Se os recursos de computação, armazenamento e rede forem configurados manualmente, desenvolvimento, teste e produção tendem a divergir, e ninguém sabe reconstruí-los com exatidão. A **infraestrutura como código** (*Infrastructure as Code*, IaC) resolve esse problema: o estado desejado dos recursos é declarado em arquivos, com ferramentas como o Terraform, versionado e revisado como qualquer código, e aplicado automaticamente. Recriar um ambiente passa a ser executar a mesma especificação, e toda mudança fica registrada.

Containers resolvem **empacotamento e isolamento**, mas não garantem, sozinhos, escalabilidade ou disponibilidade. Com muitas instâncias, entra a **orquestração**, como a do Kubernetes, que inicia e remove instâncias, aloca recursos, reinicia componentes com falha e distribui a carga:

```text
CONTAINER → como executar de forma isolada?
ORQUESTRAÇÃO → como coordenar muitas execuções?
```

### 8.3.4. Escalabilidade e Disponibilidade

A escala **vertical** adiciona recursos a uma instância; a **horizontal** adiciona instâncias, o que funciona bem para serviços sem estado (*stateless*). Um **balanceador de carga** distribui as requisições entre as réplicas, e o **autoscaling** ajusta seu número à demanda. Entretanto:

```text
escalabilidade ≠ disponibilidade
```

Um sistema pode suportar grande carga e ainda ter um ponto único de falha. Alta disponibilidade exige redundância, reinicialização automática e recuperação, de modo que a falha de um componente não derrube o sistema.

## 8.4. Limitações, Trade-offs e Desafios Atuais

A infraestrutura de ML envolve compromissos entre latência e custo, disponibilidade e custo, automação e complexidade. Recursos insuficientes (**underprovisioning**) geram filas, latência e indisponibilidade; recursos excessivos (**overprovisioning**) geram desperdício. Busca-se capacidade próxima da demanda, com margem para variações.

Arquitetura mais sofisticada não é arquitetura melhor: um pequeno serviço interno não precisa de Kubernetes, e a infraestrutura deve ser proporcional aos requisitos. Resiliência inclui ainda a **degradação graciosa**, como recorrer a uma versão anterior ou a um modelo mais simples quando o principal falha.

## 8.5. Conclusão

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

A arquitetura adequada não é a mais complexa, mas a que atende, de forma controlada, aos requisitos de **desempenho, disponibilidade, custo e risco**.

## Referências

1. SCULLEY, D. et al. Hidden technical debt in machine learning systems. In: NeurIPS, 2015.
2. KREUZBERGER, D.; KÜHL, N.; HIRSCHL, S. Machine learning operations (MLOps): overview, definition, and architecture. **IEEE Access**, 2023.
3. BRECK, E. et al. The ML test score [...]. In: IEEE BigData, 2017.
