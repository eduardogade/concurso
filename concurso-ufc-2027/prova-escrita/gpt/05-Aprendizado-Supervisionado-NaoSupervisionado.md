# Ponto 4 — Mineração de Dados: Descoberta de Conhecimento, Análise Exploratória de Dados, Identificação de Padrões e Anomalias

## 4.1. Introdução e Delimitação do Problema

Mineração de dados compreende métodos para extrair regularidades relevantes de grandes conjuntos de dados, mas não se confunde com a própria descoberta de conhecimento.

O objetivo não é apenas executar algoritmos, e sim transformar observações em padrões **válidos, novos, úteis e interpretáveis**, capazes de ampliar a compreensão de um fenômeno ou apoiar decisões:

```text
Data Mining ⊂ KDD
```

A mineração é, portanto, uma etapa do processo mais amplo de **Knowledge Discovery in Databases (KDD)** [1], no qual dados são preparados e explorados, padrões são extraídos e os resultados são avaliados e interpretados.

## 4.2. Fundamentos e Relevância

O processo KDD pode ser representado por:

```text
seleção → pré-processamento → transformação
→ mineração → avaliação/interpretação → conhecimento
```

- Na **seleção**, definem-se dados e atributos relevantes.
- O **pré-processamento** trata valores ausentes, duplicações, inconsistências e erros.
- A **transformação** adapta a representação por normalização, discretização, agregação ou construção de atributos.
- A **mineração** identifica associações, agrupamentos ou comportamentos anômalos.

Por fim, os resultados são avaliados segundo validade, novidade, utilidade e interpretabilidade. O processo não é estritamente linear: resultados intermediários podem exigir retorno às etapas anteriores.

É essencial distinguir **dado, padrão e conhecimento**. Um padrão é uma regularidade identificada nos dados, mas sua mera existência não constitui conhecimento:

```text
padrão + validação + interpretação + contexto → conhecimento
```

Um resultado pode ser estatisticamente detectável e, ainda assim, trivial, espúrio ou irrelevante para o domínio.

## 4.3. Núcleo Técnico

### 4.3.1. Preparação dos Dados e Análise Exploratória

A qualidade dos padrões depende da qualidade e da representação dos dados.

A preparação pode envolver limpeza e tratamento de valores ausentes, integração de fontes, normalização, transformação e seleção de atributos e, quando apropriada, redução de dimensionalidade.

Essas operações não são neutras: diferentes representações podem revelar ou ocultar diferentes estruturas.

A **Análise Exploratória de Dados (EDA)** [2] busca compreender os dados antes da imposição de modelos formais, usando estatísticas descritivas e visualizações para examinar distribuições, relações entre variáveis, qualidade dos dados, agrupamentos preliminares e potenciais anomalias.

Pode ser univariada, bivariada ou multivariada e é essencialmente iterativa:

```text
exploração → hipótese → transformação → nova exploração
```

EDA não se reduz à produção de gráficos: orienta as etapas subsequentes da descoberta, e seus achados devem ser tratados como hipóteses, não como conclusões.

### 4.3.2. Identificação e Mineração de Padrões

Padrões podem assumir a forma de coocorrências, associações, agrupamentos, sequências temporais e estruturas locais.

Em regras de associação, três medidas clássicas são [3]:

\[
sup(X \rightarrow Y) = \frac{freq(X \cup Y)}{N},
\]

\[
conf(X \rightarrow Y) = \frac{sup(X \cup Y)}{sup(X)},
\]

\[
lift(X \rightarrow Y) = \frac{conf(X \rightarrow Y)}{sup(Y)}.
\]

O **suporte** mede a frequência conjunta; a **confiança**, a frequência de \(Y\) entre as ocorrências de \(X\); e o **lift** compara essa associação com o esperado a partir da frequência marginal de \(Y\): \(lift > 1\) indica associação positiva em relação à independência.

Agrupamentos revelam estrutura latente ao reunir observações semelhantes; o detalhamento de seus algoritmos pertence ao aprendizado não supervisionado.

Um padrão pode ser **global**, quando descreve o conjunto, ou **local**, quando ocorre apenas em uma subpopulação; em dados temporais, sequências e transições também importam.

Frequência, porém, não é relevância: um padrão muito frequente pode ser trivial, enquanto um padrão raro pode possuir grande significado científico ou operacional.

### 4.3.3. Identificação de Anomalias

Anomalias são observações ou conjuntos de observações que se desviam do comportamento esperado [4].

Não devem ser automaticamente interpretadas como erros: podem representar ruído ou falha de medição, mas também fraude, falha operacional, evento raro ou fenômeno biologicamente relevante.

Distinguem-se:

- **anomalias globais**, atípicas em relação ao conjunto inteiro;
- **anomalias contextuais**, atípicas somente sob determinada condição;
- **anomalias coletivas**, nas quais o caráter anômalo emerge de um conjunto de observações.

A detecção pode basear-se em distribuição estatística, distância, densidade, vizinhança ou isolamento.

Em alta dimensionalidade, porém, distâncias e vizinhanças perdem poder discriminativo, manifestação da *curse of dimensionality*.

## 4.4. Limitações, Trade-offs e Desafios Atuais

O principal risco é confundir **estrutura aparente com conhecimento válido**. Quanto maior o número de variáveis, hipóteses e relações examinadas, maiores as oportunidades de falsos positivos.

Por isso, padrões e anomalias devem ser avaliados quanto à estabilidade, reprodutibilidade e relevância prática. Entre os desafios estão:

- dados incompletos, ruidosos ou enviesados;
- múltiplas comparações e padrões espúrios;
- sensibilidade à representação e aos parâmetros;
- alta dimensionalidade e baixa interpretabilidade;
- mudanças na distribuição dos dados ao longo do tempo.

Além disso:

```text
associação ≠ causalidade
```

Uma relação observada pode decorrer de confundimento, viés de seleção, causalidade reversa ou coincidência; inferência causal exige hipóteses e desenhos adicionais.

Por fim, o conhecimento de domínio continua indispensável: um padrão matematicamente forte pode ser inútil ou biologicamente implausível, enquanto uma anomalia rara pode ser justamente o resultado de maior interesse.

## 4.5. Conclusão

Em síntese:

```text
DADOS
↓
PREPARAÇÃO
↓
EDA
↓
PADRÕES / ANOMALIAS
↓
VALIDAÇÃO
↓
INTERPRETAÇÃO
↓
CONHECIMENTO
```

A mineração de dados é componente de um processo iterativo de descoberta, com retroalimentação entre as etapas, no qual **qualidade dos dados, exploração, identificação de padrões, detecção de anomalias e interpretação** são igualmente relevantes.

Seu valor não reside em encontrar regularidades, mas em distinguir padrões robustos de artefatos e convertê-los, mediante validação e contexto, em conhecimento útil.

## Referências

[1] Fayyad, U. et al. AI Magazine. 1996.
[2] Tukey, J. W. Addison-Wesley. 1977.
[3] Han, J. et al. Morgan Kaufmann. 2012.
[4] Aggarwal, C. C. Springer. 2017.
