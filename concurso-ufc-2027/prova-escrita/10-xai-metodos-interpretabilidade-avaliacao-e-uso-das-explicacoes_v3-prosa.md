# Ponto 10 — XAI: Métodos, Interpretabilidade, Avaliação e Uso das Explicações

## 10.1. Introdução e Delimitação do Problema

A **Explainable Artificial Intelligence (XAI)** reúne métodos para tornar compreensível o comportamento de modelos de aprendizado de máquina e de suas predições. Seu objetivo não é produzir uma narrativa convincente, mas fornecer evidências sobre como uma saída foi obtida e sobre sua confiabilidade.

A primeira distinção é:

```text
interpretabilidade intrínseca ≠ explicação post hoc
```

Modelos intrinsecamente interpretáveis, como regressões simples, árvores pequenas e regras, podem ser inspecionados diretamente; métodos *post hoc* explicam, após o treinamento, modelos cuja lógica interna não é diretamente compreensível¹.

O problema pode ser organizado por quatro perguntas:

1. O QUE está sendo explicado?
2. COMO a explicação é produzida?
3. A explicação é FIEL?
4. PARA QUEM e PARA QUÊ ela será utilizada?

XAI é, assim, um problema de **método, avaliação e uso**.

## 10.2. Fundamentos e Relevância

Explicações **locais** respondem por que uma predição específica \(f(x)\) foi produzida; explicações **globais** caracterizam o comportamento geral de \(f\). Métodos **model-specific** exploram a estrutura interna de uma família de modelos; métodos **model-agnostic** tratam o modelo como caixa-preta, observando apenas entradas e saídas.

XAI descreve o comportamento do modelo, não o mundo:

```text
importância para o modelo ≠ efeito causal
```

## 10.3. Núcleo Técnico

### 10.3.1. Atribuição de Atributos

Métodos de **feature attribution** estimam a contribuição de cada variável para uma saída. No SHAP², a predição é decomposta de forma aditiva:

\[
f(x) = \phi_{0} + \sum_{j = 1}^{p}\phi_{j}
\]

em que \(\phi_{0}\) é a predição média de referência e \(\phi_{j}\) a contribuição da *feature* \(j\). Os \(\phi_{j}\) são **valores de Shapley**, da teoria dos jogos cooperativos: as *features* são tratadas como jogadores que cooperam na predição, e cada uma recebe a média de sua contribuição marginal sobre todas as ordens em que poderia entrar. É a única divisão com certas propriedades desejáveis, como, somadas à referência, reproduzir exatamente a predição; como o cálculo exato é exponencial no número de *features*, usam-se aproximações.

A **permutation importance** mede a relevância global de uma variável pela queda de desempenho quando seus valores são embaralhados, quebrando sua relação com o alvo:

\[
I_{j} = M_{\text{original}} - M_{\text{permutado}(j)}
\]

*Features* correlacionadas dificultam essa interpretação, pois uma pode substituir parcialmente a outra. Em redes neurais, usam-se métodos de gradiente, como o **Integrated Gradients**.

### 10.3.2. Surrogates, Exemplos e Contrafactuais

Métodos **surrogate** aproximam o modelo complexo \(f\) por um modelo simples \(g\), com \(g(x) \approx f(x)\). O LIME³ é um surrogate local: perturba a observação, consulta o modelo original e ajusta, nessa vizinhança, um modelo linear ponderado pela proximidade. Fidelidade local, porém, não implica fidelidade global.

Explicações **baseadas em exemplos** usam protótipos ou casos semelhantes. Explicações **contrafactuais** perguntam o que precisaria mudar para que a decisão fosse outra, buscando a menor mudança que produza o resultado desejado:

\[
x^{*} = \arg\min_{x'}[d(x,x') + \lambda L(f(x'),y_{\text{desejado}})]
\]

Um bom contrafactual deve ser válido, **plausível, viável e acionável**: sugerir "reduzir a idade" é inútil.

### 10.3.3. Avaliação das Explicações

Uma explicação pode parecer convincente e representar mal o modelo:

```text
plausibilidade ≠ fidelidade
```

A **fidelidade** mede o quanto a explicação reproduz o comportamento efetivo do modelo. Também importam a **estabilidade** (entradas semelhantes, explicações semelhantes) e a **compreensibilidade**. Há um trade-off entre **fidelidade e simplicidade**: uma explicação tão complexa quanto o modelo pode ser fiel e inútil.

A avaliação pode ser **funcional**, testando se a explicação acompanha intervenções no modelo; **humana**, medindo compreensão e capacidade de uso; ou **dependente da aplicação**, verificando se a explicação melhora a tarefa real¹.

### 10.3.4. Uso das Explicações

No desenvolvimento, explicações ajudam a identificar *data leakage*, atalhos (*shortcuts*) e correlações espúrias: boa métrica não implica modelo saudável. Em suporte à decisão, ajudam especialistas a decidir quando revisar a saída do modelo. O objetivo não é aumentar a confiança, mas obter **confiança calibrada**: confiar quando há razões para isso. Explicações também apoiam auditoria e investigação de erros.

## 10.4. Limitações, Trade-offs e Desafios Atuais

A limitação mais fundamental é:

```text
explicar o modelo ≠ explicar o fenômeno
```

Um modelo pode usar atalhos, *proxies* ou correlações espúrias, e uma explicação fiel apenas revelará esse comportamento. Métodos *post hoc* podem ser aproximados, instáveis e sensíveis à referência escolhida, e métodos diferentes podem discordar por adotarem hipóteses diferentes.

XAI também não corrige um modelo: revelado um viés, é preciso corrigir dados ou treinamento e revalidar. Por fim, se um modelo interpretável satisfaz os requisitos, deve ser preferido a explicações *post hoc*.

## 10.5. Conclusão

Em síntese:

```text
MODELO
↓
MÉTODO DE XAI
↓
EXPLICAÇÃO
↓
AVALIAÇÃO
↓
CONTEXTUALIZAÇÃO
↓
USO
```

XAI não consiste apenas em gerar explicações, mas em **produzi-las, avaliá-las, contextualizá-las e utilizá-las de acordo com uma finalidade explícita**. Uma boa explicação é a adequada à pergunta, fiel ao modelo e usada com consciência de suas limitações.

## Referências

1. MOLNAR, C. **Interpretable machine learning**: a guide [...]. 3. ed. Leanpub, 2025.
2. LUNDBERG, S. M.; LEE, S.-I. A unified approach to interpreting model predictions. In: NeurIPS, 2017.
3. RIBEIRO, M. T.; SINGH, S.; GUESTRIN, C. "Why should I trust you?" [...]. In: KDD, 2016.
