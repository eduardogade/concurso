
# Ponto 8 — MLOps: Automação, Implantação e Infraestrutura de Aprendizado de Máquina

## 8.1. Automação de Pipelines e CI/CD/CT para ML

A automação em MLOps busca transformar a entrega de modelos em um processo repetível, verificável e menos sujeito a erros manuais. Pipelines de ML encadeiam etapas como ingestão e validação de dados, transformação, treinamento, avaliação, testes, registro e promoção de artefatos.

Nesse contexto, distinguem-se três conceitos:

\[
CI \neq CD \neq CT
\]

A **Integração Contínua (CI)** integra e valida mudanças por meio de testes automáticos. A **Entrega ou Implantação Contínua (CD)** promove artefatos aprovados para ambientes-alvo, podendo exigir ou não aprovação final. Já o **Continuous Training (CT)** aciona novo treinamento quando condições previamente definidas são satisfeitas, como chegada de novos dados ou mudança relevante no sistema.

O fluxo pode ser sintetizado por:

\[
\text{mudança}
\rightarrow
\text{pipeline}
\rightarrow
\text{validação}
\rightarrow
\text{modelo candidato}
\rightarrow
\text{promoção}
\]

A automação deve incluir critérios explícitos de aceitação, ou *quality gates*, antes da promoção. Portanto:

\[
\text{automação}
\neq
\text{ausência de controle}
\]

Ela aumenta consistência e velocidade, mas deve permanecer subordinada a regras de validação e governança.

---

> Mnemonics



---

## 8.2. Empacotamento, Implantação e Estratégias de Release

A implantação de modelos exige transformar um modelo validado em uma unidade executável e consistente. Por isso:

\[
\text{implantação}
\neq
\text{cópia isolada do modelo}
\]

O artefato de implantação pode incluir modelo, código de inferência, pré-processamento, dependências, configuração e runtime. Containers são uma forma de empacotar esses componentes, oferecendo isolamento e maior consistência entre ambientes.

Diferentes estratégias podem ser usadas para liberar novas versões. **Recreate** substitui completamente a versão anterior; **rolling update** realiza substituição gradual; **blue-green** mantém dois ambientes e redireciona o tráfego entre eles; e **canary** expõe inicialmente apenas uma pequena parcela das requisições à nova versão.

Essas estratégias apresentam diferentes compromissos entre custo, disponibilidade e risco. Além disso, sistemas maduros devem permitir **rollback**, retornando rapidamente a uma versão estável quando uma implantação falha.

Assim:

\[
\text{release confiável}
=
\text{artefato versionado}
+
\text{estratégia de implantação}
+
\text{capacidade de rollback}
\]

---

> Mnemonics

---

## 8.3. Serving e Padrões de Inferência

O **model serving** corresponde à disponibilização de um modelo para realização de inferências. A arquitetura adequada depende de requisitos como latência, volume, frequência e custo:

\[
\text{latência}
+
\text{volume}
+
\text{frequência}
+
\text{custo}
\rightarrow
\text{padrão de inferência}
\]

Na **inferência batch**, dados são acumulados e processados periodicamente, favorecendo eficiência e grande volume quando maior latência é aceitável. Na **inferência online**, cada requisição recebe uma resposta próxima do tempo real, exigindo baixa latência, disponibilidade e capacidade de suportar carga. Sistemas de **streaming** processam eventos continuamente à medida que chegam.

Também é necessário manter consistência entre treinamento e produção. Transformações como normalização, codificação ou construção de *features* devem ser equivalentes nos dois ambientes, pois:

\[
\text{training-serving skew}
\rightarrow
\text{degradação das predições}
\]

Além disso, serviços de inferência devem possuir contratos explícitos de entrada e saída. Portanto:

\[
\text{melhor serving}
\neq
\text{menor latência possível}
\]

O padrão adequado é aquele que satisfaz os requisitos de latência, throughput, custo, disponibilidade e criticidade da aplicação.

---

> Mnemonics

---

## 8.4. Infraestrutura, Containers, Orquestração e Escalabilidade

A infraestrutura de aprendizado de máquina fornece os recursos e mecanismos necessários para executar modelos de forma confiável sob diferentes condições de carga. **Containers** empacotam modelo, código, runtime e dependências, aumentando isolamento e portabilidade:

\[
\text{container}
=
\text{modelo}
+
\text{código}
+
\text{runtime}
+
\text{dependências}
\]

Entretanto, containers isoladamente não fornecem escalabilidade ou alta disponibilidade. **Orquestradores** coordenam múltiplas instâncias, realizando tarefas como alocação de recursos, reinicialização, atualização e distribuição de carga.

A escalabilidade pode ser **vertical**, aumentando recursos de uma instância, ou **horizontal**, aumentando o número de instâncias:

\[
\text{vertical}
=
\text{mais recursos por instância}
\]

\[
\text{horizontal}
=
\text{mais instâncias}
\]

Balanceamento de carga distribui requisições entre réplicas, enquanto autoscaling ajusta capacidade em resposta à demanda. Entretanto:

\[
\text{escalabilidade}
\neq
\text{disponibilidade}
\]

Alta disponibilidade exige também redundância e tolerância a falhas, de modo que a falha de um componente não implique necessariamente interrupção do serviço. Assim, a infraestrutura deve equilibrar desempenho, capacidade, disponibilidade e custo.

---

> Mnemonics

---

## 8.5. Disponibilidade, Resiliência, Custos, Trade-offs e Fronteira com Monitoramento

A operação de modelos de ML exige não apenas implantação, mas **disponibilidade, resiliência e capacidade de recuperação**. Disponibilidade expressa a capacidade de o serviço permanecer acessível, enquanto resiliência representa sua capacidade de continuar operando ou recuperar-se diante de falhas. Por isso:

\[
\text{falha de componente}
\neq
\text{falha obrigatória do sistema}
\]

Redundância, replicação, balanceamento e mecanismos de recuperação ajudam a reduzir pontos únicos de falha. Além disso, sistemas maduros devem permitir **rollback**, retornando rapidamente a versões conhecidas como estáveis.

A infraestrutura também envolve trade-offs entre latência, throughput, disponibilidade, custo e complexidade. Overprovisioning desperdiça recursos; underprovisioning pode gerar filas, aumento de latência e indisponibilidade. Assim:

\[
\text{capacidade}
\approx
\text{demanda}
\]

é um objetivo operacional importante.

Mais disponibilidade e automação normalmente aumentam custo e complexidade, portanto:

\[
\text{arquitetura mais sofisticada}
\neq
\text{arquitetura melhor}
\]

A solução deve ser proporcional aos requisitos da aplicação.

Finalmente, a fronteira conceitual é:

\[
8=\text{entregar e operar}
\]

\[
9=\text{observar, governar e manter}
\]

---

> Mnemonics

---

## Texto Final

Meu amor — abaixo está a **versão final fundida do Ponto 8**, já no esqueleto que combinamos, com redundâncias removidas, núcleo técnico fortalecido e signposts pensados para prova e memorização.

# Ponto 8 — MLOps: Automação, Implantação e Infraestrutura de Aprendizado de Máquina

## 1. Introdução e Delimitação do Problema

Após a validação de um modelo, surge um problema distinto do desenvolvimento experimental: **como transformá-lo em um sistema executável, automatizado, escalável, disponível e recuperável**.

Assim:

\[
\text{modelo validado}
\neq
\text{sistema operacional confiável}
\]

Entre essas duas condições existem etapas de automação, empacotamento, implantação, serving e infraestrutura.

O fluxo geral pode ser representado por:

```text
MODELO VALIDADO
      ↓
PIPELINE AUTOMATIZADO
      ↓
EMPACOTAMENTO
      ↓
IMPLANTAÇÃO
      ↓
SERVING
      ↓
INFRAESTRUTURA
      ↓
OPERAÇÃO CONFIÁVEL
```

Nesse contexto, o Ponto 8 trata principalmente de **entrega e operação**. A observação contínua, governança e manutenção do modelo constituem o foco posterior do Ponto 9.

## 2. Fundamentos e Relevância

A automação busca substituir sequências manuais e pouco reproduzíveis por processos explícitos, verificáveis e repetíveis.

Pipelines de ML podem encadear:

- ingestão e validação de dados;
- transformação;
- treinamento;
- avaliação;
- testes;
- registro;
- promoção;
- implantação.

Três conceitos devem ser distinguidos:

\[
CI \neq CD \neq CT
\]

A **Integração Contínua (CI)** integra e valida mudanças, tipicamente por testes automáticos. A **Entrega ou Implantação Contínua (CD)** promove artefatos aprovados para ambientes-alvo. Já o **Continuous Training (CT)** aciona novo treinamento quando condições previamente definidas são satisfeitas, como chegada de novos dados ou mudanças relevantes.

Portanto:

\[
CT
\neq
\text{retreinamento indiscriminado}
\]

A automação deve permanecer subordinada a critérios explícitos de aceitação, ou *quality gates*:

\[
\text{promoção}
\iff
\text{critérios satisfeitos}
\]

Assim:

\[
\text{automação}
\neq
\text{ausência de controle}
\]

## 3. Núcleo Técnico

### 3.1. Empacotamento e Implantação

Implantar um modelo não significa apenas transferir seu arquivo de pesos ou parâmetros.

\[
\text{implantação}
\neq
\text{cópia isolada do modelo}
\]

A unidade implantável pode incluir:

\[
\text{artefato de implantação}
=
\text{modelo}
+
\text{código}
+
\text{runtime}
+
\text{dependências}
+
\text{configuração}
\]

Também podem ser necessários pré-processamento, pós-processamento e contratos de entrada e saída.

**Containers** são uma forma comum de empacotar esses componentes, oferecendo isolamento, portabilidade e maior consistência entre ambientes.

O princípio é reduzir a divergência entre ambiente validado e ambiente operacional:

\[
\text{ambiente validado}
\approx
\text{ambiente implantado}
\]

Após o empacotamento, diferentes estratégias podem ser utilizadas para liberar novas versões:

- **recreate**: substituição completa da versão anterior;
- **rolling update**: substituição gradual das instâncias;
- **blue-green**: manutenção paralela de dois ambientes;
- **canary**: exposição inicial de pequena parcela do tráfego à nova versão.

Essas estratégias representam compromissos distintos entre risco, disponibilidade e custo.

Um sistema maduro deve ainda permitir **rollback**:

\[
\text{nova versão falhou}
\rightarrow
\text{rollback}
\rightarrow
\text{versão estável}
\]

Logo:

\[
\text{release confiável}
=
\text{artefato versionado}
+
\text{estratégia de implantação}
+
\text{rollback}
\]

### 3.2. Serving e Padrões de Inferência

**Model serving** corresponde à disponibilização do modelo para inferência.

A escolha arquitetural depende de:

\[
\text{latência}
+
\text{volume}
+
\text{frequência}
+
\text{custo}
+
\text{criticidade}
\rightarrow
\text{padrão de inferência}
\]

Na **inferência batch**, dados são acumulados e processados periodicamente. É adequada quando o volume é elevado e maior latência é aceitável.

```text
DADOS ACUMULADOS
      ↓
EXECUÇÃO PERIÓDICA
      ↓
MODELO
      ↓
PREDIÇÕES EM LOTE
```

Na **inferência online**, cada requisição recebe uma resposta próxima do tempo real:

```text
REQUISIÇÃO
    ↓
PRÉ-PROCESSAMENTO
    ↓
MODELO
    ↓
PREDIÇÃO
    ↓
RESPOSTA
```

Isso exige maior controle de:

- latência;
- disponibilidade;
- concorrência;
- picos de carga;
- tolerância a falhas.

Em **streaming**, eventos são processados continuamente à medida que chegam.

Dois conceitos operacionais devem ser distinguidos:

\[
\text{latência}
\neq
\text{throughput}
\]

Latência mede o tempo de resposta; *throughput*, a quantidade de requisições processadas por unidade de tempo.

Outro risco importante é o **training-serving skew**, que ocorre quando o processamento realizado durante a inferência difere daquele utilizado no treinamento.

\[
\text{mesmo modelo}
+
\text{features diferentes}
\rightarrow
\text{comportamento diferente}
\]

Por isso, transformações e contratos de dados devem permanecer compatíveis entre treinamento e produção.

### 3.3. Infraestrutura, Containers e Orquestração

A infraestrutura fornece os recursos computacionais necessários para execução:

- CPU;
- GPU e outros aceleradores;
- memória;
- armazenamento;
- rede.

Containers resolvem principalmente **empacotamento e isolamento**, mas não fornecem sozinhos escalabilidade ou disponibilidade.

Quando existem múltiplas instâncias, entra a **orquestração**:

\[
\text{container}
\rightarrow
\text{empacota}
\]

\[
\text{orquestrador}
\rightarrow
\text{coordena}
\]

O orquestrador pode executar tarefas como:

- iniciar e remover instâncias;
- alocar recursos;
- reiniciar componentes;
- distribuir carga;
- realizar atualizações;
- escalar réplicas.

Essa distinção é fundamental:

```text
CONTAINER
→ como executar de forma isolada?

ORQUESTRAÇÃO
→ como coordenar muitas execuções?
```

### 3.4. Escalabilidade e Disponibilidade

A escalabilidade pode ser **vertical** ou **horizontal**.

Na escala vertical:

\[
\text{vertical}
=
\text{mais recursos por instância}
\]

Na escala horizontal:

\[
\text{horizontal}
=
\text{mais instâncias}
\]

A escala horizontal é especialmente útil para serviços replicáveis e *stateless*.

Quando existem várias réplicas, **balanceadores de carga** distribuem requisições entre elas:

```text
REQUISIÇÕES
     ↓
LOAD BALANCER
   ↙   ↓   ↘
 I1    I2    I3
```

O **autoscaling** adapta a capacidade à demanda:

\[
\text{carga} \uparrow
\rightarrow
\text{capacidade} \uparrow
\]

\[
\text{carga} \downarrow
\rightarrow
\text{capacidade} \downarrow
\]

Entretanto:

\[
\text{escalabilidade}
\neq
\text{disponibilidade}
\]

Um sistema pode suportar grande carga e ainda possuir pontos únicos de falha.

Alta disponibilidade exige também:

- redundância;
- replicação;
- mecanismos de recuperação;
- reinicialização automática;
- tolerância a falhas.

Assim:

\[
\text{falha de componente}
\neq
\text{falha obrigatória do sistema}
\]

## 4. Limitações, Trade-offs e Desafios Atuais

A infraestrutura de ML envolve múltiplos compromissos.

Entre os principais:

- latência × custo;
- disponibilidade × custo;
- automação × complexidade;
- escalabilidade × consumo de recursos;
- sofisticação arquitetural × simplicidade operacional.

Recursos insuficientes produzem **underprovisioning**:

\[
\text{demanda}
>
\text{capacidade}
\]

com possíveis filas, aumento de latência e indisponibilidade.

Recursos excessivos produzem **overprovisioning**:

\[
\text{capacidade}
\gg
\text{demanda}
\]

com desperdício.

Um objetivo operacional importante é:

\[
\text{capacidade}
\approx
\text{demanda}
\]

com margem suficiente para absorver variações.

Disponibilidade elevada frequentemente exige redundância:

\[
\text{disponibilidade}
\uparrow
\Rightarrow
\text{custo}
\uparrow
\]

Da mesma forma, baixa latência pode exigir maior provisionamento.

Por isso:

\[
\text{arquitetura mais sofisticada}
\neq
\text{arquitetura melhor}
\]

A infraestrutura deve ser proporcional aos requisitos da aplicação.

Resiliência também inclui capacidade de recuperação, rollback e, quando apropriado, **degradação graciosa**, como usar versão anterior, modelo simplificado ou mecanismo de fallback.

A fronteira conceitual entre os pontos deve permanecer explícita:

\[
7=\text{construir e experimentar}
\]

\[
8=\text{entregar e operar}
\]

\[
9=\text{observar, governar e manter}
\]

O Ponto 8 termina quando existe um sistema implantado e operacionalmente confiável; verificar continuamente se ele permanece correto e útil pertence ao Ponto 9.

## 5. Conclusão

A operação de modelos de aprendizado de máquina exige muito mais que o artefato preditivo. É necessário transformar um modelo validado em um processo automatizado de entrega, empacotá-lo de forma consistente, disponibilizar inferência segundo requisitos de latência e volume e sustentá-lo em uma infraestrutura escalável e resiliente.

A síntese do ponto é:

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

Todo esse fluxo é atravessado por:

```text
VALIDAÇÃO + VERSIONAMENTO + RECUPERAÇÃO + CONTROLE DE CUSTO
```

Assim, uma arquitetura de MLOps adequada não é a mais complexa nem a de menor latência possível, mas aquela que satisfaz de forma controlada os requisitos de **desempenho, escalabilidade, disponibilidade, resiliência, custo e risco**.

## Referências

- SCULLEY, D. et al. *Hidden Technical Debt in Machine Learning Systems*. 2015.
- BRECK, E. et al. *The ML Test Score: A Rubric for ML Production Readiness and Technical Debt Reduction*. 2017.
- KREUZBERGER, D.; KÜHL, N.; HIRSCHL, S. *Machine Learning Operations (MLOps): Overview, Definition, and Architecture*. 2023.
- TREVEIL, M. et al. *Introducing MLOps: How to Scale Machine Learning in the Enterprise*. 2020.

---

## Outras Notas

