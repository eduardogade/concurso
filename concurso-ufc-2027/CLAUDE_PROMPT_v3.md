# Tarefa: gerar versões `_v2.md` dos 10 pontos da prova escrita da UFC

Você está executando na raiz do projeto:

```text
<concurso-ufc-2027>/
```

Sua tarefa é criar **10 novos arquivos Markdown** em:

```text
prova-escrita/
```

## Objetivo geral

Para cada um dos 10 pontos:

1. Leia o arquivo `.md` original.
2. Extraia **somente o conteúdo da seção `## Texto Final`**.
3. Descarte:
   - todo o conteúdo anterior a `## Texto Final`;
   - o próprio heading `## Texto Final`;
   - qualquer separador `---` que delimite a seção seguinte;
   - `## Outras Notas`;
   - todo o conteúdo posterior a `## Outras Notas`.
4. Use o `.docx` `_v2.docx` correspondente **somente para determinar os limites de parágrafo**.
5. Preserve o conteúdo textual do `## Texto Final` do Markdown.
6. Corrija a numeração dos headings conforme as regras abaixo.
7. Normalize as referências para `[1]`, `[2]`, `[3]` etc.
8. Grave o resultado no arquivo `_v2.md` correspondente.

---

# 1. Arquivos de entrada e saída

Os arquivos Markdown originais são:

```text
prova-escrita/1-pdle-armazenamento-e-gerenciamento-distribuido-de-dados.md
prova-escrita/2-pdle-processamento-paralelo-e-distribuido-em-larga-escala.md
prova-escrita/3-pdle-processamento-de-fluxos-e-arquiteturas-de-dados.md
prova-escrita/4-mineracao-de-dados-descoberta-de-conhecimento-aed-identificacao-de-padroes-e-anomalias.md
prova-escrita/5-aprendizado-supervisionado-e-nao-supervisionado.md
prova-escrita/6-aprendizado-por-reforco.md
prova-escrita/7-mlops-desenvolvimento-versionamento-e-experimentacao-de-modelos.md
prova-escrita/8-mlops-automacao-implantacao-e-infraestrutura-de-aprendizado-de-maquina.md
prova-escrita/9-mlops-monitoramento-governanca-e-manutencao-de-modelos.md
prova-escrita/10-xai-metodos-interpretabilidade-avaliacao-e-uso-das-explicacoes.md
```

Para cada Markdown existe também um `.docx` correspondente já editado manualmente:

```text
prova-escrita/1-pdle-armazenamento-e-gerenciamento-distribuido-de-dados_v2.docx
prova-escrita/2-pdle-processamento-paralelo-e-distribuido-em-larga-escala_v2.docx
prova-escrita/3-pdle-processamento-de-fluxos-e-arquiteturas-de-dados_v2.docx
prova-escrita/4-mineracao-de-dados-descoberta-de-conhecimento-aed-identificacao-de-padroes-e-anomalias_v2.docx
prova-escrita/5-aprendizado-supervisionado-e-nao-supervisionado_v2.docx
prova-escrita/6-aprendizado-por-reforco_v2.docx
prova-escrita/7-mlops-desenvolvimento-versionamento-e-experimentacao-de-modelos_v2.docx
prova-escrita/8-mlops-automacao-implantacao-e-infraestrutura-de-aprendizado-de-maquina_v2.docx
prova-escrita/9-mlops-monitoramento-governanca-e-manutencao-de-modelos_v2.docx
prova-escrita/10-xai-metodos-interpretabilidade-avaliacao-e-uso-das-explicacoes_v2.docx
```

Crie:

```text
prova-escrita/1-pdle-armazenamento-e-gerenciamento-distribuido-de-dados_v2.md
prova-escrita/2-pdle-processamento-paralelo-e-distribuido-em-larga-escala_v2.md
prova-escrita/3-pdle-processamento-de-fluxos-e-arquiteturas-de-dados_v2.md
prova-escrita/4-mineracao-de-dados-descoberta-de-conhecimento-aed-identificacao-de-padroes-e-anomalias_v2.md
prova-escrita/5-aprendizado-supervisionado-e-nao-supervisionado_v2.md
prova-escrita/6-aprendizado-por-reforco_v2.md
prova-escrita/7-mlops-desenvolvimento-versionamento-e-experimentacao-de-modelos_v2.md
prova-escrita/8-mlops-automacao-implantacao-e-infraestrutura-de-aprendizado-de-maquina_v2.md
prova-escrita/9-mlops-monitoramento-governanca-e-manutencao-de-modelos_v2.md
prova-escrita/10-xai-metodos-interpretabilidade-avaliacao-e-uso-das-explicacoes_v2.md
```

**Não modifique os `.md` ou `.docx` existentes.**

---

# 2. Fonte autoritativa para o CONTEÚDO

O arquivo `.md` original é a **fonte autoritativa para o texto**.

Para cada arquivo:

```text
N-....md
```

localize:

```markdown
## Texto Final
```

Extraia o conteúdo que começa imediatamente **depois** desse heading e termina:

1. imediatamente antes de `## Outras Notas`, se essa seção existir; ou
2. no fim do arquivo, caso ela não exista.

Se houver um:

```markdown
---
```

imediatamente antes de `## Outras Notas`, remova também esse separador.

O novo `_v2.md` deve começar diretamente pelo título:

```markdown
# Ponto N — ...
```

**Não inclua `## Texto Final` no arquivo de saída.**

---

# 3. REGRA CRÍTICA: não reescrever o conteúdo

Não faça revisão editorial.

Não:

- resuma;
- expanda;
- parafraseie;
- corrija estilo;
- troque terminologia;
- reorganize argumentos;
- acrescente conhecimento;
- remova conhecimento;
- altere frases;
- altere citações;
- altere fórmulas;
- altere diagramas;
- altere listas;
- altere ênfases Markdown;
- altere palavras em inglês;
- altere pontuação apenas por preferência estilística.

O **texto do `## Texto Final` deve permanecer semanticamente e lexicalmente o mesmo**.

As únicas transformações permitidas são:

1. inserir limites de parágrafo conforme o `.docx`;
2. ajustar a numeração dos headings;
3. numerar as referências no formato definido abaixo;
4. remover as partes que explicitamente devem ser excluídas.

---

# 4. Uso dos arquivos `_v2.docx`: PARÁGRAFOS

Esta é a parte mais importante da tarefa.

Os `.docx` `_v2.docx` contêm essencialmente o mesmo texto final, porém foram editados manualmente para introduzir **parágrafos menores e mais digeríveis**.

Use cada `.docx` correspondente como **autoridade para identificar onde um parágrafo termina e o próximo começa**.

Exemplo conceitual:

Markdown original:

```markdown
Uma frase. Outra frase. Terceira frase. Quarta frase.
```

Se o `.docx` correspondente estiver dividido visual/logicamente como:

```text
Uma frase. Outra frase.

Terceira frase. Quarta frase.
```

o `_v2.md` deverá conter:

```markdown
Uma frase. Outra frase.

Terceira frase. Quarta frase.
```

## Importante

O `.docx` **NÃO é autoridade textual**.

Se houver pequenas diferenças de caracteres, formatação ou conteúdo entre `.md` e `.docx`:

- preserve o texto do `.md`;
- use o `.docx` apenas para identificar **onde inserir linhas em branco entre parágrafos**.

Em outras palavras:

```text
.md   → autoridade para O QUE está escrito
.docx → autoridade para ONDE os parágrafos são separados
```

Não copie cegamente o texto extraído do `.docx`.

---

# 5. Como determinar os limites de parágrafo

Você pode inspecionar os `.docx` com `python-docx`, XML interno do DOCX ou outro método confiável.

Para cada seção textual:

1. extraia os parágrafos do `.docx`;
2. normalize temporariamente apenas para realizar correspondência, por exemplo:
   - whitespace;
   - quebras de linha;
   - caracteres de formatação invisíveis;
3. localize no texto Markdown os mesmos conjuntos de sentenças;
4. introduza uma linha em branco no Markdown onde o `.docx` muda de parágrafo.

A normalização usada para **matching** não deve alterar o conteúdo efetivamente escrito no arquivo final.

Quando houver ambiguidade, preserve o Markdown original e faça a intervenção mínima.

---

# 6. Numeração do título e das seções

O número do ponto é determinado pelo prefixo do filename.

Por exemplo:

```text
1-pdle-...
```

significa:

```text
Ponto 1
```

e:

```text
10-xai-...
```

significa:

```text
Ponto 10
```

## Título

Garanta que o título principal tenha:

```markdown
# Ponto <N> — <título existente>
```

Exemplo:

```markdown
# Ponto 1 — Processamento de Dados em Larga Escala: Armazenamento e Gerenciamento Distribuído de Dados
```

---

# 7. Numeração das seções principais

O esqueleto final possui:

```text
1. Introdução e Delimitação do Problema
2. Fundamentos e Relevância
3. Núcleo Técnico
4. Limitações, Trade-offs e Desafios Atuais
5. Conclusão
Referências
```

No arquivo do **Ponto N**, converta os headings para:

```markdown
## N.1. Introdução e Delimitação do Problema
## N.2. Fundamentos e Relevância
## N.3. Núcleo Técnico
## N.4. Limitações, Trade-offs e Desafios Atuais
## N.5. Conclusão
## Referências
```

Exemplos:

### Ponto 1

```markdown
## 1.1. Introdução e Delimitação do Problema
## 1.2. Fundamentos e Relevância
## 1.3. Núcleo Técnico
## 1.4. Limitações, Trade-offs e Desafios Atuais
## 1.5. Conclusão
```

### Ponto 7

```markdown
## 7.1. Introdução e Delimitação do Problema
## 7.2. Fundamentos e Relevância
## 7.3. Núcleo Técnico
## 7.4. Limitações, Trade-offs e Desafios Atuais
## 7.5. Conclusão
```

### Ponto 10

```markdown
## 10.1. Introdução e Delimitação do Problema
## 10.2. Fundamentos e Relevância
## 10.3. Núcleo Técnico
## 10.4. Limitações, Trade-offs e Desafios Atuais
## 10.5. Conclusão
```

**`## Referências` permanece sem número de seção.**

---

# 8. Numeração das subseções do Núcleo Técnico

Dentro da seção:

```markdown
## N.3. Núcleo Técnico
```

existem normalmente 3 ou 4 subseções.

Converta:

```markdown
### 3.1. ...
### 3.2. ...
### 3.3. ...
### 3.4. ...
```

para:

```markdown
### N.3.1. ...
### N.3.2. ...
### N.3.3. ...
### N.3.4. ...
```

Exemplo no Ponto 2:

```markdown
## 2.3. Núcleo Técnico

### 2.3.1. Decomposição, Granularidade e Balanceamento

### 2.3.2. Comunicação, Sincronização e Localidade

### 2.3.3. MapReduce e Modelos de Execução Distribuída

### 2.3.4. DAGs, Reutilização e Recuperação
```

Exemplo no Ponto 10:

```markdown
## 10.3. Núcleo Técnico

### 10.3.1. ...
### 10.3.2. ...
### 10.3.3. ...
```

Preserve o **texto do título da subseção**. Altere somente sua numeração.

Não presuma que todos os pontos possuem exatamente quatro subseções: detecte quantas realmente existem.

---

# 9. Referências

A seção final deve ser:

```markdown
## Referências
```

Cada referência deve estar numerada sequencialmente:

```markdown
[1] PRIMEIRA REFERÊNCIA
[2] SEGUNDA REFERÊNCIA
[3] TERCEIRA REFERÊNCIA
...
```

## Conversão necessária

Se o Markdown original contiver:

```markdown
- AMDAHL, G. ...
- DEAN, J.; GHEMAWAT, S. ...
- GUSTAFSON, J. ...
- ZAHARIA, M. et al. ...
```

converta para:

```markdown
[1] AMDAHL, G. ...
[2] DEAN, J.; GHEMAWAT, S. ...
[3] GUSTAFSON, J. ...
[4] ZAHARIA, M. et al. ...
```

Se já estiver:

```markdown
[1] ...
[2] ...
```

preserve o conteúdo, apenas verificando que:

- começa em `[1]`;
- cresce de 1 em 1;
- não existem números repetidos;
- não existem saltos.

Não altere o conteúdo bibliográfico das referências.

O objetivo é reproduzir o padrão já usado no Ponto 1:

```markdown
## Referências

[1] ...
[2] ...
[3] ...
```

---

# 10. Elementos Markdown que devem permanecer intactos

Preserve integralmente:

- fórmulas LaTeX inline;
- fórmulas LaTeX em bloco;
- fenced code blocks;
- diagramas ASCII;
- setas;
- tabelas Markdown;
- listas;
- bullets;
- negrito;
- itálico;
- `inline code`;
- citações bibliográficas presentes no corpo;
- caracteres matemáticos;
- nomes próprios;
- anos;
- terminologia técnica.

Não transforme diagramas em prosa.

Não transforme listas em parágrafos.

Não transforme fórmulas em texto.

---

# 11. Espaçamento Markdown

Use uma linha em branco:

- entre headings e conteúdo;
- entre parágrafos;
- antes e depois de listas;
- antes e depois de fórmulas em bloco;
- antes e depois de fenced code blocks;
- entre a última parte do texto e `## Referências`.

Não introduza múltiplas linhas vazias desnecessárias.

A segmentação dos **parágrafos em prosa** deve seguir o `_v2.docx`.

---

# 12. Validação automática obrigatória

Depois de criar os 10 arquivos, faça uma segunda passagem de validação.

Para cada `_v2.md`, confirme:

### Conteúdo

- [ ] começa com `# Ponto N — ...`;
- [ ] não contém `## Texto Final`;
- [ ] não contém a parte didática inicial;
- [ ] não contém `> Mnemonics`;
- [ ] não contém `## Outras Notas`;
- [ ] não contém conteúdo posterior a `## Outras Notas`;
- [ ] mantém todo o conteúdo pertencente ao `Texto Final`.

### Numeração

- [ ] título contém o número correto do ponto;
- [ ] headings principais são `N.1` a `N.5`;
- [ ] subseções do núcleo são `N.3.1`, `N.3.2`, ...;
- [ ] `## Referências` não recebe número.

### Referências

- [ ] todas possuem `[1]`, `[2]`, ...;
- [ ] ordem é crescente;
- [ ] não existem bullets `- <REF>` na seção de referências;
- [ ] conteúdo bibliográfico não foi alterado.

### Formatação

- [ ] limites de parágrafo refletem o `_v2.docx`;
- [ ] fórmulas permanecem válidas;
- [ ] fenced code blocks continuam fechados;
- [ ] diagramas permanecem intactos;
- [ ] listas permanecem válidas.

---

# 13. Validação textual contra o Markdown original

Faça também uma validação destinada especificamente a impedir reescrita acidental.

Para cada ponto:

1. obtenha o conteúdo original de `## Texto Final`;
2. obtenha o `_v2.md`;
3. remova temporariamente, **somente para comparação**:
   - numeração dos headings;
   - numeração `[N]` das referências;
   - diferenças de whitespace/linhas em branco;
4. compare os conteúdos.

A expectativa é que sejam equivalentes.

Qualquer diferença lexical que não seja explicada por:

- numeração de heading;
- numeração de referência;
- nova quebra de parágrafo;

deve ser investigada e corrigida.

**O processo não deve silenciosamente reescrever o texto.**

---

# 14. Não invente conteúdo ausente

Se algum `.docx`:

- estiver ausente;
- estiver corrompido;
- não corresponder ao Markdown;
- tiver diferenças grandes demais para inferir parágrafos com segurança;

não tente reconstruir criativamente.

Nesse caso:

1. preserve os parágrafos do Markdown original para aquele trecho;
2. registre o problema no relatório final;
3. continue processando os demais arquivos.

Da mesma forma, se um arquivo não possuir exatamente a estrutura esperada, inspecione-o antes de alterar qualquer coisa.

---

# 15. Ordem de execução recomendada

Faça primeiro os Pontos **1 e 2** como casos de validação.

Eles fornecem padrões úteis:

- o Ponto 1 já demonstra o formato desejado de referências `[1]`, `[2]`, ...;
- o Ponto 2 demonstra um caso em que referências com `-` precisam ser convertidas;
- ambos contêm a divisão entre material preparatório e `## Texto Final`.

Depois de confirmar que o procedimento funciona para ambos, aplique-o aos Pontos 3–10.

---

# 16. Resultado esperado

Ao terminar, devem existir exatamente estes novos arquivos:

```text
prova-escrita/1-pdle-armazenamento-e-gerenciamento-distribuido-de-dados_v2.md
prova-escrita/2-pdle-processamento-paralelo-e-distribuido-em-larga-escala_v2.md
prova-escrita/3-pdle-processamento-de-fluxos-e-arquiteturas-de-dados_v2.md
prova-escrita/4-mineracao-de-dados-descoberta-de-conhecimento-aed-identificacao-de-padroes-e-anomalias_v2.md
prova-escrita/5-aprendizado-supervisionado-e-nao-supervisionado_v2.md
prova-escrita/6-aprendizado-por-reforco_v2.md
prova-escrita/7-mlops-desenvolvimento-versionamento-e-experimentacao-de-modelos_v2.md
prova-escrita/8-mlops-automacao-implantacao-e-infraestrutura-de-aprendizado-de-maquina_v2.md
prova-escrita/9-mlops-monitoramento-governanca-e-manutencao-de-modelos_v2.md
prova-escrita/10-xai-metodos-interpretabilidade-avaliacao-e-uso-das-explicacoes_v2.md
```

---

# 17. Relatório final

Depois de concluir a edição, responda de forma concisa com:

1. os 10 arquivos criados;
2. confirmação de que os arquivos originais não foram modificados;
3. confirmação de que a segmentação dos parágrafos foi baseada nos `_v2.docx`;
4. quaisquer discrepâncias ou ambiguidades encontradas;
5. resultado da validação textual e estrutural.

Não faça nenhuma outra alteração no projeto.
