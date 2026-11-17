
# Ponto 10 — XAI: Métodos, Interpretabilidade, Avaliação e Uso das Explicações

## 10.1. Interpretabilidade, Explicabilidade e Taxonomias Fundamentais

A XAI busca tornar o comportamento de modelos de aprendizado de máquina mais compreensível, mas exige distinções conceituais precisas. **Interpretabilidade intrínseca** refere-se a modelos cuja estrutura pode ser compreendida diretamente, enquanto métodos **post hoc** produzem explicações após o treinamento de modelos mais complexos.

Uma taxonomia fundamental distingue explicações **locais** e **globais**:

\[
\text{local}
\neq
\text{global}
\]

Explicações locais procuram justificar uma predição específica, enquanto explicações globais descrevem o comportamento geral do modelo. Outra distinção separa métodos **model-specific**, que exploram a estrutura interna do modelo, de métodos **model-agnostic**, que podem tratá-lo essencialmente como uma função de entrada e saída.

Também é necessário distinguir explicar o modelo de explicar o fenômeno:

\[
\text{importância para o modelo}
\neq
\text{efeito causal}
\]

Uma feature pode ser importante para a predição sem possuir efeito causal sobre o fenômeno real.

Finalmente, a qualidade de uma explicação depende de seu propósito e de seu destinatário. Assim:

\[
\text{boa explicação}
=
\text{adequação ao usuário}
+
\text{adequação à tarefa}
\]

Essas distinções formam a base para compreender os métodos, critérios de avaliação e usos de XAI.

---

> Mnemonics



---

## 10.2. Principais Famílias de Métodos de XAI

Os métodos de XAI podem ser organizados em famílias segundo o tipo de informação que produzem. Métodos de **feature attribution** estimam a contribuição das variáveis para a saída do modelo. SHAP, por exemplo, representa a predição como uma soma de contribuições:

\[
f(x)
=
\phi_0
+
\sum_{j=1}^{p}\phi_j
\]

enquanto *permutation importance* estima importância global observando a perda de desempenho após perturbar uma feature.

Métodos **surrogate** aproximam o comportamento de modelos complexos por modelos mais simples. LIME, por exemplo, ajusta uma aproximação local em torno de uma observação. Contudo:

\[
\text{surrogate}
\neq
\text{modelo original}
\]

e sua utilidade depende da fidelidade da aproximação.

Explicações também podem ser baseadas em **exemplos**, utilizando casos semelhantes ou protótipos, ou em **contrafactuais**, que procuram uma entrada \(x'\) próxima de \(x\) capaz de alterar a decisão:

\[
x' \approx x
\quad\text{e}\quad
f(x') \neq f(x)
\]

Contrafactuais devem ainda respeitar plausibilidade e acionabilidade.

Assim, diferentes métodos respondem perguntas distintas:

\[
\text{atribuição}
\rightarrow
\text{quais features?}
\]

\[
\text{surrogate}
\rightarrow
\text{qual regra aproximada?}
\]

\[
\text{exemplos}
\rightarrow
\text{com quais casos se parece?}
\]

\[
\text{contrafactual}
\rightarrow
\text{o que precisaria mudar?}
\]

Logo, a escolha do método deve depender da pergunta explicativa, do modelo, do usuário e da finalidade.

---

> Mnemonics

---

## 10.3. Avaliação das Explicações

A avaliação de métodos de XAI é necessária porque uma explicação intuitiva ou visualmente convincente não é necessariamente correta. A primeira propriedade fundamental é a **fidelidade**, isto é, o grau em que a explicação representa o comportamento real do modelo:

\[
g(x)
\approx
f(x)
\]

onde \(f\) é o modelo original e \(g\) sua explicação ou aproximação. Entretanto:

\[
\text{fidelidade ao modelo}
\neq
\text{verdade sobre o fenômeno}
\]

pois um modelo pode ter aprendido correlações espúrias.

Outros critérios incluem **estabilidade**, robustez, consistência e complexidade. Idealmente:

\[
x \approx x'
\Rightarrow
E(x) \approx E(x')
\]

quando pequenas perturbações não alteram significativamente o comportamento do modelo. Também existe um trade-off entre simplicidade e fidelidade:

\[
\text{fidelidade}
\leftrightarrow
\text{compreensibilidade}
\]

A avaliação pode ser funcional, verificando se a explicação acompanha intervenções no modelo; humana, medindo compreensão e utilidade; ou dependente da aplicação. Para contrafactuais, devem ainda ser avaliadas validade, proximidade, plausibilidade e acionabilidade.

Assim:

\[
\text{boa explicação}
\neq
\text{explicação apenas plausível}
\]

Sua qualidade deve ser avaliada de forma multidimensional, considerando fidelidade, estabilidade e utilidade para o usuário e a tarefa.

---

> Mnemonics

---

## 10.4. Uso das Explicações

As explicações de XAI devem ser avaliadas também por sua **utilidade prática**. Uma explicação adequada depende do usuário e da tarefa:

\[
\text{boa explicação}
=
\text{adequação ao usuário}
+
\text{adequação à finalidade}
\]

Durante desenvolvimento e validação, explicações podem auxiliar na identificação de correlações espúrias, leakage, shortcuts e dependência de features inadequadas. Em sistemas de suporte à decisão, podem ajudar especialistas a compreender fatores relevantes, detectar casos anômalos e decidir quando revisar a saída do modelo.

Entretanto, o objetivo não deve ser simplesmente aumentar confiança:

\[
\text{mais confiança}
\neq
\text{melhor uso}
\]

O ideal é produzir **confiança calibrada**, compatível com as limitações do sistema.

Contrafactuais podem fornecer explicações acionáveis ao indicar quais mudanças poderiam alterar uma decisão, desde que sejam plausíveis e viáveis. Explicações também podem apoiar auditoria, comparação entre modelos e geração de hipóteses.

Contudo:

\[
\text{importância preditiva}
\neq
\text{evidência causal}
\]

Assim, XAI deve ser vista como uma interface entre modelo e usuário, cujo formato deve ser escolhido segundo quem utilizará a explicação, com qual objetivo e para qual decisão.

---

> Mnemonics

---

## 10.5. Limitações, Riscos e Interpretação Responsável

Métodos de XAI possuem limitações importantes e suas explicações devem ser interpretadas com cautela. Em primeiro lugar:

\[
\text{importância de feature}
\neq
\text{efeito causal}
\]

A maioria das técnicas explica o comportamento do modelo, não necessariamente os mecanismos do fenômeno real. Portanto:

\[
\text{explicar o modelo}
\neq
\text{explicar o fenômeno}
\]

Métodos post hoc também podem ser aproximações imperfeitas, instáveis ou sensíveis à escolha de baseline, amostra de referência e correlação entre features. Além disso:

\[
\text{plausibilidade}
\neq
\text{fidelidade}
\]

uma explicação intuitiva pode aumentar confiança sem representar corretamente o modelo.

Diferentes métodos podem produzir explicações distintas porque adotam hipóteses e definições de importância diferentes. Contrafactuais, por sua vez, devem respeitar plausibilidade, restrições do domínio e acionabilidade.

XAI também não corrige automaticamente problemas detectados; ela fornece evidências para investigação. Assim, o uso responsável deve combinar explicação, avaliação, contexto e comunicação explícita de limitações:

\[
\text{explicar}
\rightarrow
\text{avaliar}
\rightarrow
\text{contextualizar}
\rightarrow
\text{usar}
\]

A interpretação adequada exige distinguir fidelidade ao modelo, compreensão humana e validade sobre o mundo real.

---

> Mnemonics

---

## Texto Final

# Ponto 10 — XAI: Métodos, Interpretabilidade, Avaliação e Uso das Explicações

## 1. Introdução e Delimitação do Problema

A **Explainable Artificial Intelligence (XAI)** reúne métodos destinados a tornar mais compreensível o comportamento de modelos de aprendizado de máquina e suas predições. Seu objetivo não é apenas produzir uma narrativa intuitiva, mas fornecer evidências úteis sobre como determinada saída foi obtida e em que medida essa explicação pode ser considerada confiável.

A primeira distinção essencial é:

\[
\text{interpretabilidade intrínseca}
\neq
\text{explicação post hoc}
\]

Modelos intrinsecamente interpretáveis, como regressões simples, pequenas árvores ou sistemas de regras, possuem estrutura diretamente inspecionável. Métodos *post hoc*, por outro lado, procuram explicar após o treinamento modelos cuja lógica interna não é facilmente compreendida.

O problema pode ser organizado por quatro perguntas:

```text
1. O QUE está sendo explicado?
2. COMO a explicação é produzida?
3. A explicação é FIEL?
4. PARA QUEM e PARA QUÊ ela será utilizada?
```

Assim, XAI deve ser tratada como um problema simultaneamente de **método, avaliação e uso**, e não apenas como geração de visualizações ou importâncias de atributos.

## 2. Fundamentos e Relevância

Uma taxonomia importante distingue explicações **locais** e **globais**:

\[
\text{local}
\neq
\text{global}
\]

Explicações locais procuram responder por que uma predição específica \(f(x)\) foi produzida; explicações globais procuram caracterizar o comportamento geral de \(f\).

Outra distinção separa métodos **model-specific**, que exploram propriedades internas de determinada família de modelos, de métodos **model-agnostic**, que tratam o modelo essencialmente como uma função de entrada e saída.

Também é necessário separar dois objetivos:

\[
\text{explicar } f
\neq
\text{explicar } f(x)
\]

isto é, explicar globalmente o modelo não é equivalente a explicar uma decisão individual.

Por fim, XAI descreve primordialmente o comportamento preditivo do modelo. Portanto:

\[
\text{importância para o modelo}
\neq
\text{efeito causal}
\]

Uma variável pode ser decisiva para uma predição sem possuir efeito causal sobre o fenômeno real.

## 3. Núcleo Técnico

### 3.1. Atribuição de Atributos

Métodos de **feature attribution** estimam a contribuição de cada variável para uma saída.

No SHAP, por exemplo, a predição é representada de forma aditiva:

\[
f(x)
=
\phi_0
+
\sum_{j=1}^{p}\phi_j
\]

em que \(\phi_0\) representa um valor de referência e \(\phi_j\) a contribuição atribuída à feature \(j\).

Essa decomposição permite explicações locais e, por agregação, análises globais. Entretanto:

\[
|\phi_j| \text{ elevado}
\neq
\text{efeito causal elevado}
\]

A interpretação depende das hipóteses do método e da distribuição de referência.

Outra abordagem é a **permutation importance**, que estima a relevância global de uma variável observando quanto o desempenho diminui quando seus valores são embaralhados:

\[
I_j
=
M_{\text{original}}
-
M_{\text{permutado}(j)}
\]

Features correlacionadas podem dificultar essa interpretação, pois uma variável pode substituir parcialmente outra.

Em modelos diferenciáveis, métodos baseados em gradientes analisam a sensibilidade da saída em relação às entradas. **Integrated Gradients**, por exemplo, acumula gradientes ao longo de um caminho entre uma entrada de referência e a observação analisada.

### 3.2. Surrogates, Exemplos e Contrafactuais

Métodos **surrogate** aproximam um modelo complexo \(f\) por um modelo mais simples \(g\):

\[
g(x)
\approx
f(x)
\]

LIME é um exemplo clássico de surrogate local: gera perturbações em torno de uma observação, consulta o modelo original e ajusta uma aproximação simples naquela vizinhança.

Contudo:

\[
\text{surrogate}
\neq
\text{modelo original}
\]

e:

\[
\text{fidelidade local}
\not\Rightarrow
\text{fidelidade global}
\]

Explicações **baseadas em exemplos** utilizam protótipos, casos semelhantes ou exemplos influentes para contextualizar uma decisão.

Já explicações **contrafactuais** procuram responder:

> o que precisaria mudar para que a decisão fosse diferente?

Formalmente, busca-se uma entrada \(x'\) próxima de \(x\) tal que:

\[
x' \approx x
\qquad\text{e}\qquad
f(x') \neq f(x)
\]

Uma formulação conceitual é:

\[
x^*
=
\arg\min_{x'}
\left[
d(x,x')
+
\lambda L(f(x'),y_{\text{desejado}})
\right]
\]

Mas um bom contrafactual deve ser não apenas matematicamente válido, como também **plausível, viável e acionável**.

Essas famílias respondem perguntas distintas:

```text
ATRIBUIÇÃO
→ quais variáveis contribuíram?

SURROGATE
→ qual regra simples aproxima o modelo?

EXEMPLOS
→ com quais casos esta decisão se parece?

CONTRAFACTUAL
→ o que precisaria mudar para alterar a decisão?
```

### 3.3. Avaliação das Explicações

Uma explicação pode parecer convincente e ainda representar mal o modelo. Assim:

\[
\text{plausibilidade}
\neq
\text{fidelidade}
\]

A **fidelidade** mede o grau em que a explicação reproduz o comportamento efetivo do modelo:

\[
g(x)
\approx
f(x)
\]

Entretanto:

\[
\text{fidelidade ao modelo}
\neq
\text{verdade sobre o fenômeno}
\]

Um modelo pode ter aprendido correlações espúrias, e uma explicação perfeitamente fiel apenas tornará essas correlações visíveis.

Outras propriedades importantes incluem:

- **estabilidade**: entradas semelhantes devem produzir explicações semelhantes quando o modelo também se comporta de modo semelhante;
- **robustez**: pequenas perturbações irrelevantes não devem alterar excessivamente a explicação;
- **consistência**: situações comparáveis devem produzir explicações coerentes;
- **compreensibilidade**: a explicação deve ter complexidade apropriada ao usuário.

Idealmente:

\[
x \approx x'
\Rightarrow
E(x) \approx E(x')
\]

quando o próprio comportamento do modelo permanece estável.

Há ainda um trade-off fundamental:

\[
\text{fidelidade}
\leftrightarrow
\text{simplicidade}
\]

Uma explicação tão complexa quanto o próprio modelo pode possuir alta fidelidade e pouca utilidade interpretativa.

A avaliação pode ocorrer em três níveis:

- **funcional**, testando se a explicação acompanha intervenções no modelo;
- **humano**, medindo compreensão, confiança e capacidade de uso;
- **dependente da aplicação**, verificando se a explicação melhora a tarefa real.

Para contrafactuais, critérios adicionais incluem validade, proximidade, plausibilidade e acionabilidade.

### 3.4. Uso das Explicações

XAI pode apoiar diferentes etapas do ciclo de ML.

Durante desenvolvimento e validação, explicações podem ajudar a identificar:

- *data leakage*;
- atalhos (*shortcuts*);
- correlações espúrias;
- features inadequadas;
- comportamento inesperado.

Assim:

\[
\text{boa métrica}
\neq
\text{modelo necessariamente saudável}
\]

Em sistemas de suporte à decisão, explicações podem ajudar especialistas a compreender fatores relevantes, detectar casos anômalos e decidir quando revisar a saída do modelo.

O objetivo, entretanto, não deve ser simplesmente aumentar confiança:

\[
\text{mais confiança}
\neq
\text{melhor uso}
\]

O objetivo adequado é **confiança calibrada**: confiar quando há razões para confiar e reconhecer incertezas e limitações quando necessário.

Explicações também podem apoiar:

- auditoria;
- comparação entre modelos;
- investigação de erros;
- comunicação com usuários;
- geração de hipóteses científicas.

Mas:

\[
\text{importância preditiva}
\neq
\text{evidência causal}
\]

XAI pode sugerir hipóteses; validação causal exige evidência adicional.

Consequentemente:

\[
\text{boa explicação}
=
\text{adequação ao usuário}
+
\text{adequação à tarefa}
\]

O mesmo modelo pode exigir explicações diferentes para pesquisadores, especialistas de domínio, auditores ou usuários finais.

## 4. Limitações, Trade-offs e Desafios Atuais

Métodos de XAI possuem limitações importantes.

A mais fundamental é:

\[
\text{explicar o modelo}
\neq
\text{explicar o fenômeno}
\]

Um modelo pode utilizar atalhos, proxies, vieses ou correlações espúrias, e uma explicação fiel simplesmente revelará esse comportamento.

Métodos *post hoc* podem ainda ser:

- aproximados;
- instáveis;
- sensíveis à baseline;
- dependentes da amostra de referência;
- afetados por correlação entre features;
- vulneráveis a interpretações excessivas.

Diferentes métodos podem produzir explicações distintas:

\[
E_1(x)
\neq
E_2(x)
\]

porque podem adotar hipóteses, baselines e conceitos de importância diferentes. Essa discordância não implica automaticamente erro; exige compreender a pergunta respondida por cada técnica.

Contrafactuais também podem ser inválidos no domínio, mesmo quando matematicamente corretos:

\[
\text{válido para o modelo}
\neq
\text{plausível no mundo}
\]

Outro risco é utilizar explicações como **racionalizações**: narrativas convincentes apresentadas após a decisão, mas sem fidelidade suficiente ao mecanismo do modelo.

Assim:

\[
\text{justificativa convincente}
\neq
\text{explicação fiel}
\]

XAI também não corrige automaticamente um modelo problemático:

\[
\text{detectar problema}
\neq
\text{resolver problema}
\]

Se uma explicação revela um shortcut ou viés, ainda será necessário corrigir dados, treinamento, features ou arquitetura e revalidar o sistema.

Finalmente, não existe uma lei universal que determine que modelos opacos sejam necessariamente superiores:

\[
\text{mais complexo}
\neq
\text{sempre mais preciso}
\]

Sempre que possível, deve-se considerar se um modelo intrinsecamente interpretável consegue satisfazer os requisitos da aplicação antes de depender exclusivamente de explicações post hoc.

## 5. Conclusão

XAI não consiste apenas em gerar explicações, mas em **produzi-las, avaliá-las, contextualizá-las e utilizá-las de acordo com uma finalidade explícita**.

A síntese do ponto é:

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

Quatro distinções devem permanecer centrais:

\[
\text{importância}
\neq
\text{causalidade}
\]

\[
\text{fidelidade ao modelo}
\neq
\text{verdade sobre o mundo}
\]

\[
\text{plausibilidade}
\neq
\text{fidelidade}
\]

\[
\text{explicação}
\neq
\text{garantia de decisão correta}
\]

Assim, uma explicação de alta qualidade não é simplesmente aquela que parece intuitiva, mas aquela que é **adequada à pergunta, suficientemente fiel ao modelo, avaliada segundo critérios explícitos e utilizada com conhecimento de suas limitações**.

## Referências

- RIBEIRO, M. T.; SINGH, S.; GUESTRIN, C. *“Why Should I Trust You?”: Explaining the Predictions of Any Classifier*. 2016.
- LUNDBERG, S. M.; LEE, S.-I. *A Unified Approach to Interpreting Model Predictions*. 2017.
- SUNDARARAJAN, M.; TALY, A.; YAN, Q. *Axiomatic Attribution for Deep Networks*. 2017.
- MOLNAR, C. *Interpretable Machine Learning*. 2022.

---

## Outras Notas

