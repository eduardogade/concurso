# Ponto 10 — XAI: Métodos, Interpretabilidade, Avaliação e Uso das Explicações

## 1. Introdução e Delimitação do Problema

A **Explainable Artificial Intelligence (XAI)** reúne métodos destinados a tornar mais compreensível o comportamento de modelos de aprendizado de máquina e suas predições. Seu objetivo não é produzir uma narrativa intuitiva, mas fornecer evidências sobre como uma saída foi obtida e em que medida a explicação é confiável. A primeira distinção é:

```text
interpretabilidade intrínseca ≠ explicação post hoc
```

Modelos intrinsecamente interpretáveis, como regressões simples, pequenas árvores ou sistemas de regras, possuem estrutura diretamente inspecionável; métodos *post hoc* procuram explicar, após o treinamento, modelos cuja lógica interna não é facilmente compreendida [1]. O problema pode ser organizado por quatro perguntas:

```text
1. O QUE está sendo explicado?
2. COMO a explicação é produzida?
3. A explicação é FIEL?
4. PARA QUEM e PARA QUÊ ela será utilizada?
```

XAI é, assim, um problema de **método, avaliação e uso**.

## 2. Fundamentos e Relevância

Explicações **locais** procuram responder por que uma predição específica \(f(x)\) foi produzida; explicações **globais**, caracterizar o comportamento geral de \(f\). Métodos **model-specific** exploram propriedades internas de uma família de modelos; métodos **model-agnostic** tratam o modelo como uma função de entrada e saída.

XAI descreve primordialmente o comportamento preditivo do modelo:

```text
importância para o modelo ≠ efeito causal
```

## 3. Núcleo Técnico

### 3.1. Atribuição de Atributos

Métodos de **feature attribution** estimam a contribuição de cada variável para uma saída. No SHAP [2], a predição é representada de forma aditiva:

\[
f(x)=\phi_0+\sum_{j=1}^{p}\phi_j
\]

em que \(\phi_0\) representa um valor de referência e \(\phi_j\) a contribuição atribuída à *feature* \(j\). Essa decomposição permite explicações locais e, por agregação, globais, mas sua interpretação depende das hipóteses do método e da distribuição de referência.

A **permutation importance** estima a relevância global de uma variável pela queda de desempenho quando seus valores são embaralhados:

\[
I_j=M_{\text{original}}-M_{\text{permutado}(j)}
\]

*Features* correlacionadas dificultam essa interpretação, pois uma variável pode substituir parcialmente outra. Em modelos diferenciáveis, métodos de gradiente analisam a sensibilidade da saída às entradas; **Integrated Gradients** [3] acumula gradientes ao longo de um caminho entre uma referência e a observação.

### 3.2. Surrogates, Exemplos e Contrafactuais

Métodos **surrogate** aproximam um modelo complexo \(f\) por um modelo mais simples \(g\), com \(g(x)\approx f(x)\). O LIME [4] é um surrogate local: gera perturbações em torno de uma observação, consulta o modelo original e ajusta uma aproximação simples naquela vizinhança. Contudo, fidelidade local não implica fidelidade global.

Explicações **baseadas em exemplos** utilizam protótipos, casos semelhantes ou exemplos influentes. Explicações **contrafactuais** perguntam o que precisaria mudar para que a decisão fosse diferente:

\[
x^*=\arg\min_{x'}\left[d(x,x')+\lambda L(f(x'),y_{\text{desejado}})\right]
\]

Um bom contrafactual deve ser, além de válido, **plausível, viável e acionável**. Essas famílias respondem perguntas distintas:

```text
ATRIBUIÇÃO → quais variáveis contribuíram?
SURROGATE → qual regra simples aproxima o modelo?
EXEMPLOS → com quais casos a decisão se parece?
CONTRAFACTUAL → o que mudaria a decisão?
```

### 3.3. Avaliação das Explicações

Uma explicação pode parecer convincente e ainda representar mal o modelo:

```text
plausibilidade ≠ fidelidade
```

A **fidelidade** mede o quanto a explicação reproduz o comportamento efetivo do modelo. Também importam a **estabilidade**, idealmente \(x\approx x'\Rightarrow E(x)\approx E(x')\) quando o modelo se comporta de modo semelhante; a **robustez** a perturbações irrelevantes; e a **compreensibilidade** para o usuário. Há um trade-off entre **fidelidade e simplicidade**: uma explicação tão complexa quanto o modelo pode ser fiel e pouco útil.

A avaliação pode ser **funcional**, testando se a explicação acompanha intervenções no modelo; **humana**, medindo compreensão e capacidade de uso; ou **dependente da aplicação**, verificando se a explicação melhora a tarefa real [1].

### 3.4. Uso das Explicações

Durante desenvolvimento e validação, explicações ajudam a identificar *data leakage*, atalhos (*shortcuts*), correlações espúrias e *features* inadequadas: boa métrica não implica modelo saudável. Em sistemas de suporte à decisão, ajudam especialistas a decidir quando revisar a saída do modelo. O objetivo não é simplesmente aumentar a confiança, mas obter **confiança calibrada**: confiar quando há razões para isso e reconhecer incertezas e limitações.

Explicações também apoiam auditoria, investigação de erros, comunicação com usuários e geração de hipóteses científicas, cuja validação causal exige evidência adicional. Uma boa explicação é adequada ao usuário e à tarefa.

## 4. Limitações, Trade-offs e Desafios Atuais

A limitação mais fundamental é:

```text
explicar o modelo ≠ explicar o fenômeno
```

Um modelo pode utilizar atalhos, *proxies*, vieses ou correlações espúrias, e uma explicação fiel apenas revelará esse comportamento. Métodos *post hoc* podem ser aproximados, instáveis, sensíveis à baseline e afetados por correlação entre *features*. Diferentes métodos podem produzir explicações distintas, \(E_1(x)\neq E_2(x)\), por adotarem hipóteses diferentes; a discordância exige compreender a pergunta respondida por cada técnica.

Outro risco é utilizar explicações como **racionalizações**: narrativas convincentes, sem fidelidade ao mecanismo do modelo. XAI também não corrige um modelo: revelado um *shortcut* ou viés, ainda é necessário corrigir dados ou treinamento e revalidar o sistema. Por fim, modelos complexos não são sempre mais precisos; sempre que possível, deve-se verificar se um modelo intrinsecamente interpretável satisfaz os requisitos antes de depender de explicações *post hoc*.

## 5. Conclusão

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

XAI não consiste apenas em gerar explicações, mas em **produzi-las, avaliá-las, contextualizá-las e utilizá-las de acordo com uma finalidade explícita**. Uma boa explicação não é a que parece intuitiva, mas a **adequada à pergunta, suficientemente fiel ao modelo, avaliada segundo critérios explícitos e utilizada com conhecimento de suas limitações**.

## Referências

[1] MOLNAR, C. *Interpretable Machine Learning*. 2022.
[2] LUNDBERG, S. M.; LEE, S.-I. *A Unified Approach to Interpreting Model Predictions*. 2017.
[3] SUNDARARAJAN, M.; TALY, A.; YAN, Q. *Axiomatic Attribution for Deep Networks*. 2017.
[4] RIBEIRO, M. T.; SINGH, S.; GUESTRIN, C. *“Why Should I Trust You?”: Explaining the Predictions of Any Classifier*. 2016.
