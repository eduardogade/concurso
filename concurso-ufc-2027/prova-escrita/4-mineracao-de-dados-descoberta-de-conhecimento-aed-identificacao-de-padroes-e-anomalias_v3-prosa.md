# Ponto 4 — Mineração de Dados: Descoberta de Conhecimento, Análise Exploratória de Dados, Identificação de Padrões e Anomalias

## 4.1. Introdução e Delimitação do Problema

Mineração de dados reúne métodos para extrair regularidades de grandes conjuntos de dados, mas não se confunde com a descoberta de conhecimento. O objetivo não é apenas executar algoritmos, e sim obter padrões **válidos, novos, úteis e interpretáveis**, capazes de apoiar decisões.

A mineração é, portanto, uma etapa do processo mais amplo de **Knowledge Discovery in Databases (KDD)**¹.

## 4.2. Fundamentos e Relevância

O processo KDD pode ser representado por:

```text
seleção → pré-processamento → transformação
→ mineração → avaliação/interpretação → conhecimento
```

Seleciona-se o que é relevante, corrigem-se ausências e erros, adapta-se a representação, buscam-se padrões e avalia-se sua validade e utilidade. O processo é iterativo: um resultado insatisfatório pode exigir o retorno a etapas anteriores.

É essencial distinguir **dado, padrão e conhecimento**. Um padrão é uma regularidade nos dados, mas não é, por si só, conhecimento:

```text
padrão + validação + interpretação + contexto → conhecimento
```

Um resultado pode ser estatisticamente detectável e, ainda assim, trivial, espúrio ou irrelevante.

## 4.3. Núcleo Técnico

### 4.3.1. Preparação dos Dados e Análise Exploratória

A qualidade dos padrões depende da qualidade e da representação dos dados: limpeza, tratamento de ausentes, normalização e seleção de atributos não são neutros, pois podem revelar ou ocultar estruturas.

A **Análise Exploratória de Dados (EDA)**, proposta por Tukey², busca compreender os dados antes de impor modelos formais. Medidas de posição e dispersão resumem cada variável: média e desvio padrão são sensíveis a valores extremos; mediana e quartis são robustos e formam o ***boxplot***, que marca como atípicos os valores a mais de 1,5 intervalo interquartil (IQR) além dos quartis. **Histogramas** mostram a forma da distribuição, como assimetria ou múltiplos picos; **diagramas de dispersão** revelam relações entre pares de variáveis, quantificadas pelos coeficientes de **Pearson** (relação linear) e de **Spearman** (relação monotônica).

Os achados da EDA são hipóteses, não conclusões: orientam, de forma iterativa, as etapas seguintes.

### 4.3.2. Identificação e Mineração de Padrões

Padrões podem ser associações, agrupamentos, sequências temporais ou estruturas locais. Em regras de associação \(X \rightarrow Y\), como "quem compra pão também compra manteiga", três medidas clássicas³ são:

\[
sup(X \rightarrow Y) = \frac{freq(X \cup Y)}{N},
\]

\[
conf(X \rightarrow Y) = \frac{sup(X \cup Y)}{sup(X)},
\]

\[
lift(X \rightarrow Y) = \frac{conf(X \rightarrow Y)}{sup(Y)}.
\]

O **suporte** mede a frequência conjunta; a **confiança**, a frequência de \(Y\) quando \(X\) ocorre; e o **lift** compara essa confiança com a frequência geral de \(Y\): \(lift > 1\) indica que \(X\) aumenta a chance de \(Y\) além do esperado sob independência.

Um padrão pode ser **global**, válido para todo o conjunto, ou **local**, restrito a uma subpopulação. E frequência não é relevância: um padrão frequente pode ser óbvio, enquanto um raro pode ter grande valor científico ou operacional.

### 4.3.3. Identificação de Anomalias

Anomalias são observações que se desviam do comportamento esperado. Não são necessariamente erros: podem indicar falha de medição, mas também fraude, defeito operacional ou fenômeno cientificamente relevante. Distinguem-se:

- **anomalias globais**, atípicas em relação ao conjunto inteiro;
- **anomalias contextuais**, atípicas apenas em certo contexto, como consumo elevado de energia de madrugada;
- **anomalias coletivas**, em que um conjunto de observações é anômalo, embora cada uma pareça normal.

Os métodos de detecção partem de diferentes noções de normalidade. Os **estatísticos** marcam valores improváveis, como os de escore z elevado ou fora da regra do IQR. Os de **distância** consideram anômalo o ponto distante de seus k vizinhos mais próximos; os de **densidade**, como o LOF, comparam a densidade ao redor de um ponto com a de seus vizinhos. O ***Isolation Forest*** parte de outra intuição: anomalias, por serem raras e diferentes, são isoladas com poucas partições aleatórias. Em alta dimensionalidade, distâncias perdem poder discriminativo (*curse of dimensionality*), o que prejudica os métodos de distância e densidade.

## 4.4. Limitações, Trade-offs e Desafios Atuais

O principal risco é confundir **estrutura aparente com conhecimento válido**: quanto mais variáveis e hipóteses se examinam, maior a chance de encontrar padrões por acaso (**múltiplas comparações**). Padrões e anomalias devem, por isso, ser avaliados quanto à estabilidade, reprodutibilidade e relevância prática.

Além disso:

```text
associação ≠ causalidade
```

Uma relação observada pode decorrer de confundimento, viés de seleção, causalidade reversa ou coincidência; inferir causas exige hipóteses e desenhos adicionais. Por fim, o conhecimento de domínio é indispensável: um padrão matematicamente forte pode ser implausível, e uma anomalia rara pode ser o resultado de maior interesse.

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

A mineração de dados vale não por encontrar regularidades, mas por distinguir padrões robustos de artefatos e convertê-los, por validação e contexto, em conhecimento útil.

## Referências

1. FAYYAD, U.; PIATETSKY-SHAPIRO, G.; SMYTH, P. From data mining to knowledge discovery in databases. **AI Magazine**, 1996.
2. TUKEY, J. W. **Exploratory data analysis**. Addison-Wesley, 1977.
3. HAN, J.; PEI, J.; TONG, H. **Data mining**: concepts and techniques. 4. ed. Morgan Kaufmann, 2022.
