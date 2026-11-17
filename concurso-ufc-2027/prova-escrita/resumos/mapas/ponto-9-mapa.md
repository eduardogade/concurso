# Ponto 9 — MLOps: Monitoramento, Governança e Manutenção de Modelos

## 9.1. Introdução e Delimitação do Problema

```text
[implantado ≠ **válido para sempre**]
                  ↓
[detectar → diagnosticar → **controlar**]
```

## 9.2. Fundamentos e Relevância

```text
[saúde: **operacional** ↔ **ML**]
                ↓
[**observabilidade**: 3 sinais → SLI/SLO → alertas]
```

## 9.3. Núcleo Técnico

### 9.3.1. Qualidade de Dados, Data Drift e Concept Drift

```text
[**data drift** P(X) ↔ **concept drift** P(Y|X)]
                 ↓
[drift ≠ **degradação** comprovada]
                 ↓
[KS · χ² · **PSI** → significância não basta]
```

### 9.3.2. Monitoramento Preditivo e Detecção de Degradação

```text
[feedback **atrasa** (empréstimo) → sinais indiretos]
                 ↓
[M_t < τ → alerta: **sensibilidade** × estabilidade]
                 ↓
[degradação ≠ **causa** → 3 passos]
```

### 9.3.3. Governança, Auditoria e Lineage

```text
[3 componentes · **lineage** + **auditoria**]
             ↓
[proporcional ao **risco**: crédito ↔ filmes]
             ↓
[**ISO/IEC 42001** · LGPD]
```

### 9.3.4. Manutenção, Retreinamento e Ciclo de Vida

```text
[drift ≠ **retreinar** (pode incorporar o erro)]
              ↓
[periódico ↔ **por eventos**]
              ↓
[**champion–challenger** antes de promover]
```

## 9.4. Limitações, Trade-offs e Desafios Atuais

```text
[**excesso** de alertas]
            ↓
[retreino automático **mal governado**]
```

## 9.5. Conclusão

```text
[manter = demonstrar **controle**, não só executar]
```
