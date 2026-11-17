# Ponto 8 — MLOps: Automação, Implantação e Infraestrutura de Aprendizado de Máquina

## 8.1. Introdução e Delimitação do Problema

```text
[modelo validado ≠ **sistema confiável**]
                ↓
[código = pequena parte (**Sculley**)]
                ↓
[escopo: **entrega** + operação]
```

## 8.2. Fundamentos e Relevância

```text
[manual → **pipeline** como DAG (Airflow, Kubeflow)]
                  ↓
[CI · CD · **CT** ≠ retreinar sempre]
                  ↓
[**quality gates** → regra de promoção]
```

## 8.3. Núcleo Técnico

### 8.3.1. Empacotamento e Implantação

```text
[implantar ≠ copiar **pesos**]
               ↓
[pré/pós + **contrato** E/S → container (Docker)]
               ↓
[4 estratégias de liberação + **rollback**]
```

### 8.3.2. Serving e Padrões de Inferência

```text
[**batch**: escore noturno] ↔ [**online**: latência · throughput]
                       ↓
[training-serving **skew** → **feature store**]
```

### 8.3.3. Infraestrutura, Containers e Orquestração

```text
[manual → **IaC** (Terraform): recriar + registrar]
                        ↓
[container tem limite → **Kubernetes** orquestra]
```

### 8.3.4. Escalabilidade e Disponibilidade

```text
[vertical ↔ **horizontal** + balanceador + autoscaling]
                         ↓
[escalável ≠ **disponível**: ponto único de falha]
```

## 8.4. Limitações, Trade-offs e Desafios Atuais

```text
[**under** ↔ **over**provisioning]
                 ↓
[sofisticado ≠ melhor (serviço interno)]
                 ↓
[resiliência + **degradação graciosa**]
```

## 8.5. Conclusão

```text
[atender **requisitos** com controle, não complexidade]
```
