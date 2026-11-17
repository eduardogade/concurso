# Ponto 7 — MLOps: Desenvolvimento, Versionamento e Experimentação de Modelos

## 7.1. Introdução e Delimitação do Problema

```text
[ciclo **iterativo** e experimental]
                 ↓
[modelo ≠ só **código** (Sculley)]
                 ↓
[escopo: até o **candidato validado**]
```

## 7.2. Fundamentos e Relevância

```text
[execução = **unidade experimental** (4 componentes)]
                ↓
[entradas → procedimento → saídas]
                ↓
[acurácia subiu ≠ **evidência**]
```

## 7.3. Núcleo Técnico

### 7.3.1. Versionamento, Artefatos e Linhagem

```text
[só código **não basta** → artefatos]
                  ↓
[proveniência ↔ **linhagem**: dados brutos → métricas]
                  ↓
[versões **imutáveis**: Git · DVC · MLflow]
```

### 7.3.2. Experiment Tracking e Rastreabilidade

```text
[tracking + versão + linhagem → **rastreabilidade**]
                       ↓
[comparar: mesmo **protocolo** + **baseline**]
```

### 7.3.3. Reprodutibilidade

```text
[resultado = f(**D, C, H, E, S**)]
                 ↓
[mesmo script ≠ mesmo experimento]
                 ↓
[reprodutível ≠ idêntico **bit a bit**]
```

### 7.3.4. Validação, Comparação e Seleção

```text
[validar **dados** ↔ validar **modelo**]
                    ↓
[busca de hiperparâmetros → superajuste à **validação**]
                    ↓
[teste **uma vez** → candidato → registro]
```

## 7.4. Limitações, Trade-offs e Desafios Atuais

```text
[guardar o **suficiente**, não tudo]
            ↓
[automatizar processo ruim ≠ criar **bom**]
            ↓
[**rigor** × velocidade]
```

## 7.5. Conclusão

```text
[**3 elementos** atravessam o fluxo]
                  ↓
[valor = condições + validação + **reconstrução**]
```
