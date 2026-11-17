Claude,

# MISSÃO

Você está trabalhando na raiz do projeto:

<concurso-ufc-2027>/

Sua tarefa é revisar editorialmente e homogeneizar a formatação dos 10 textos preparados para a Prova Escrita do concurso para Professor do Magistério Superior da Universidade Federal do Ceará (UFC), Campus de Quixadá, área de Processamento de Dados em Larga Escala e Operações de Aprendizado de Máquina (MLOps).

O objetivo final é produzir, para cada arquivo original `.docx`, uma nova versão `_v2.docx`:

- semanticamente correta;
- suficientemente completa para maximizar a nota;
- curta o bastante para ser escrita à mão no tempo disponível;
- homogênea em relação aos outros nove pontos;
- visualmente adequada para estudo e comparação.

NÃO sobrescreva nenhum arquivo original.

---

# CONTEXTO DA PROVA

Existem 10 pontos possíveis:

1. Processamento de Dados em Larga Escala: Armazenamento e Gerenciamento Distribuído de Dados;
2. Processamento de Dados em Larga Escala: Processamento Paralelo e Distribuído em Larga Escala;
3. Processamento de Dados em Larga Escala: Processamento de Fluxos e Arquiteturas de Dados;
4. Mineração de Dados: Descoberta de Conhecimento. Análise Exploratória de Dados. Identificação de Padrões e Anomalias;
5. Aprendizado Supervisionado e Não Supervisionado;
6. Aprendizado por Reforço;
7. Operações de Aprendizado de Máquina (MLOps): Desenvolvimento, Versionamento e Experimentação de Modelos;
8. Operações de Aprendizado de Máquina (MLOps): Automação, Implantação e Infraestrutura de Aprendizado de Máquina;
9. Operações de Aprendizado de Máquina (MLOps): Monitoramento, Governança e Manutenção de Modelos;
10. Inteligência Artificial Explicável (XAI): Métodos, Interpretabilidade, Avaliação e Uso das Explicações.

Na prova, 3 desses pontos serão sorteados.

A prova possui duração total de 4 horas. Portanto, para planejamento, considere aproximadamente 1h20 de escrita para cada ponto.

Esses arquivos representam os TEXTOS FINAIS que pretendo memorizar e reproduzir, com adaptações naturais, caso cada ponto seja sorteado.

O objetivo não é produzir apostilas, capítulos de livro ou textos enciclopédicos. O objetivo é maximizar:

- domínio técnico e científico;
- clareza;
- profundidade;
- objetividade;
- capacidade crítica;
- atualização;
- organização;
- adequação ao barema;

dentro de um tamanho realisticamente escrevível.

---

# DOCUMENTOS NORMATIVOS

Antes de editar qualquer conteúdo, leia:

<concurso-ufc-2027>/edital/edital.md
<concurso-ufc-2027>/edital/resolucao-cepe.md
<concurso-ufc-2027>/edital/barema-quixada.md

No barema, concentre-se especificamente nos critérios relacionados à PROVA ESCRITA.

Use esses documentos para orientar a revisão editorial, mas NÃO invente exigências ausentes neles.

---

# ARQUIVOS DE ENTRADA

Os `.docx` atuais são:

<concurso-ufc-2027>/prova-escrita/1-pdle-armazenamento-e-gerenciamento-distribuido-de-dados.docx
<concurso-ufc-2027>/prova-escrita/2-pdle-processamento-paralelo-e-distribuido-em-larga-escala.docx
<concurso-ufc-2027>/prova-escrita/3-pdle-processamento-de-fluxos-e-arquiteturas-de-dados.docx
<concurso-ufc-2027>/prova-escrita/4-mineracao-de-dados-descoberta-de-conhecimento-aed-identificacao-de-padroes-e-anomalias.docx
<concurso-ufc-2027>/prova-escrita/5-aprendizado-supervisionado-e-nao-supervisionado.docx
<concurso-ufc-2027>/prova-escrita/6-aprendizado-por-reforco.docx
<concurso-ufc-2027>/prova-escrita/7-mlops-desenvolvimento-versionamento-e-experimentacao-de-modelos.docx
<concurso-ufc-2027>/prova-escrita/8-mlops-automacao-implantacao-e-infraestrutura-de-aprendizado-de-maquina.docx
<concurso-ufc-2027>/prova-escrita/9-mlops-monitoramento-governanca-e-manutencao-de-modelos.docx
<concurso-ufc-2027>/prova-escrita/10-xai-metodos-interpretabilidade-avaliacao-e-uso-das-explicacoes.docx

Eles estão em estados diferentes:

- alguns já foram parcialmente formatados;
- alguns seguem regras antigas;
- alguns podem conter Markdown praticamente cru;
- alguns receberam intervenções manuais.

NÃO presuma que o estado atual de um `.docx` representa a formatação correta.

---

# FONTE SEMÂNTICA MESTRE

Existem também os arquivos Markdown correspondentes:

<concurso-ufc-2027>/prova-escrita/1-pdle-armazenamento-e-gerenciamento-distribuido-de-dados.md
<concurso-ufc-2027>/prova-escrita/2-pdle-processamento-paralelo-e-distribuido-em-larga-escala.md
<concurso-ufc-2027>/prova-escrita/3-pdle-processamento-de-fluxos-e-arquiteturas-de-dados.md
<concurso-ufc-2027>/prova-escrita/4-mineracao-de-dados-descoberta-de-conhecimento-aed-identificacao-de-padroes-e-anomalias.md
<concurso-ufc-2027>/prova-escrita/5-aprendizado-supervisionado-e-nao-supervisionado.md
<concurso-ufc-2027>/prova-escrita/6-aprendizado-por-reforco.md
<concurso-ufc-2027>/prova-escrita/7-mlops-desenvolvimento-versionamento-e-experimentacao-de-modelos.md
<concurso-ufc-2027>/prova-escrita/8-mlops-automacao-implantacao-e-infraestrutura-de-aprendizado-de-maquina.md
<concurso-ufc-2027>/prova-escrita/9-mlops-monitoramento-governanca-e-manutencao-de-modelos.md
<concurso-ufc-2027>/prova-escrita/10-xai-metodos-interpretabilidade-avaliacao-e-uso-das-explicacoes.md

Em cada Markdown, o TEXTO FINAL relevante está entre:

## Texto Final

e o `---` que encerra essa seção.

Use esse trecho como FONTE SEMÂNTICA MESTRE.

Regra de precedência:

1. Para conteúdo e intenção: Markdown mestre.
2. Para requisitos formais da prova: edital/resolução/barema.
3. Para verificar o estado atual da formatação: DOCX existente.

Não permita que uma formatação ou alteração manual antiga presente no `.docx` sobrescreva silenciosamente conteúdo correto do Markdown mestre.

---

# EXECUÇÃO EM TRÊS FASES

## FASE 1 — AUDITORIA

ANTES de modificar qualquer arquivo:

1. Leia edital, resolução e barema.
2. Leia os 10 trechos `## Texto Final` dos arquivos Markdown.
3. Inspecione os 10 `.docx`.
4. Para cada ponto, registre:
   - contagem atual de caracteres sem espaços;
   - problemas semânticos aparentes;
   - fórmulas possivelmente incorretas;
   - referências potencialmente incorretas;
   - redundâncias;
   - conteúdo excessivamente longo;
   - conteúdo importante aparentemente ausente;
   - inconsistências entre Markdown e DOCX;
   - estado atual da formatação.

Crie na raiz:

<concurso-ufc-2027>/revision-report.md

O relatório deve ser CONCISO e tabular quando possível.

Não pare para pedir confirmação após essa auditoria. Continue para as fases seguintes.

---

## FASE 2 — REVISÃO EDITORIAL E REESCRITA

Revise os 10 textos.

### Objetivo de tamanho

A contagem deve ser feita em CARACTERES NÃO-BRANCOS, isto é, removendo espaços, tabs e quebras de linha.

Conte TODO o texto visível que seria necessário reproduzir na prova, incluindo:

- títulos;
- subtítulos;
- corpo;
- bullets;
- fórmulas;
- citações;
- referências.

Metas:

- faixa desejável: 5.200–5.800 caracteres sem espaços;
- faixa IDEAL: 5.500–5.600;
- LIMITE MÁXIMO ESTRITO: 6.000.

Nenhum `_v2.docx` pode ultrapassar 6.000 caracteres não-brancos.

Se for necessário sacrificar algum conteúdo para obedecer ao limite de 6.000, preserve prioritariamente:

1. conceitos fundamentais;
2. núcleo técnico do ponto;
3. capacidade crítica e trade-offs;
4. fórmulas/signposts de alto valor;
5. organização;
6. referências essenciais.

Remova primeiro:

- redundâncias;
- explicações duplicadas;
- exemplos dispensáveis;
- enumerações excessivas;
- frases de transição longas;
- detalhes enciclopédicos.

### Acurácia

Os textos já foram extensamente trabalhados e são, em princípio, tecnicamente sólidos.

NÃO reescreva apenas por preferência estilística.

Reescreva quando houver uma razão concreta:

- ultrapassar ou ficar muito abaixo do tamanho-alvo;
- redundância;
- ambiguidade;
- erro técnico;
- inconsistência semântica;
- fórmula incorreta;
- referência incorreta;
- passagem pouco eficiente para prova escrita;
- desalinhamento com o barema.

Verifique cuidadosamente fórmulas, conceitos e referências.

NÃO introduza conteúdo novo apenas para “mostrar conhecimento”.

NÃO transforme os textos em manuais de ferramentas.

Preserve o caráter de dissertação técnico-científica.

---

# ARQUITETURA TEXTUAL

Os dez pontos devem manter, sempre que já presente e adequado, o seguinte macroesqueleto:

1. Introdução e Delimitação do Problema
2. Fundamentos e Relevância
3. Núcleo Técnico
   3.1 ...
   3.2 ...
   3.n ...
4. Limitações, Trade-offs e Desafios Atuais
5. Conclusão
Referências

Isso é um SIGNPOST, não um molde rígido.

Não force a mesma arquitetura interna em todos os pontos.

A Seção 3 deve ser específica ao tema e conter aproximadamente metade do conteúdo técnico.

Preserve diagramas, fluxogramas e fórmulas quando eles realmente funcionarem como signposts úteis à memorização.

Não multiplique elementos visuais desnecessariamente.

---

# FASE 3 — FORMATAÇÃO DOS DOCX

Após estabilizar semanticamente cada texto, gere o `_v2.docx`.

## Regra geral

Todo documento deve usar:

- fonte: Times New Roman;
- tamanho: 12 pt;
- estilo base: normal;
- parágrafo: "Sem Espaçamento" / No Spacing;
- alinhamento padrão: JUSTIFICADO.

EXCEÇÃO:
Equações nativas do Word podem e devem usar o padrão matemático do Word, normalmente Cambria Math.

---

# CABEÇALHOS

Todos os cabeçalhos, independentemente do nível:

- Times New Roman;
- 12 pt;
- negrito.

O título principal deve também ser CENTRALIZADO.

Demais títulos podem permanecer alinhados à esquerda, salvo motivo claro em contrário.

Se ainda houver sintaxe Markdown como:

# Título
## Seção
### Subseção
#### Subseção

remova os `#`.

Cuidado para NÃO interpretar títulos como listas.

Em particular, padrões como:

1. Introdução
2. Fundamentos
3. Núcleo Técnico
3.1. ...
3.2. ...
4. Limitações
5. Conclusão

são TÍTULOS e nunca bullets.

---

# MARKDOWN INLINE

Se houver Markdown cru:

***texto*** ou ___texto___
→ negrito + itálico.

**texto** ou __texto__
→ negrito.

*texto* ou _texto_
→ itálico.

Remova os marcadores Markdown após aplicar a formatação.

Preserve integralmente todos os caracteres Unicode legítimos.

NÃO translitere setas, letras gregas, símbolos matemáticos ou outros caracteres Unicode.

---

# EQUAÇÕES

Expressões matemáticas inline aparecem no Markdown como:

\(x_t\)

Expressões display aparecem como:

\[
T_{\mathrm{total}}
=
T_{\mathrm{comp}}
+
T_{\mathrm{comm}}
+
T_{\mathrm{sync}}
+
T_{\mathrm{overhead}}
\]

No DOCX final:

- NÃO deixe os delimitadores `\(` `\)` `\[` `\]`;
- converta as expressões para equações nativas do Microsoft Word / Office Math;
- preserve a notação matemática;
- equações display devem ficar CENTRALIZADAS;
- equações inline devem permanecer incorporadas ao parágrafo;
- use o font/default matemático normal do Word, normalmente Cambria Math.

Se a biblioteca de alto nível usada para DOCX não suportar Office Math adequadamente, manipule o OOXML necessário diretamente.

NÃO substitua equações por imagens.

NÃO deixe LaTeX cru no documento final.

Valide que o DOCX produzido continua íntegro e abre normalmente.

---

# FLUXOGRAMAS E DIAGRAMAS TEXTUAIS

Existem diagramas textuais usando caracteres Unicode, particularmente:

→
↓
←
↑
↔
⇒
⇢

Muitos possuem também palavras em LETRAS MAIÚSCULAS.

Exemplo:

MODELO VALIDADO
      ↓
AUTOMAÇÃO
      ↓
EMPACOTAMENTO
      ↓
IMPLANTAÇÃO

Detecte blocos desse tipo com cuidado.

Todos os fluxogramas/diagramas textuais devem ser CENTRALIZADOS.

Podem ocupar uma ou várias linhas.

Preserve exatamente os símbolos Unicode.

NÃO converta automaticamente texto comum contendo uma única seta em fluxograma se o contexto não sustentar essa interpretação.

---

# LINHAS DIVISÓRIAS

Uma linha contendo apenas:

---

deve ser removida completamente.

Ela deve equivaler a NADA:

- nenhuma linha;
- nenhum caractere;
- nenhum espaço extra;
- nenhum parágrafo vazio adicional.

---

# LISTAS

Todas as listas reais, exceto Referências, devem utilizar bullets do Word.

Primeiro nível:
• bullet normal do Word.

Segundo nível:
pode usar bullet secundário ou hífen visual, desde que fique homogêneo entre os 10 arquivos.

IMPORTANTE:

Não transforme títulos numerados em listas.

Use contexto estrutural para distinguir:

3. Núcleo Técnico
3.1. Versionamento
3.2. Experimentação

de uma lista verdadeira.

Uma lista verdadeira normalmente contém dois ou mais itens semanticamente paralelos.

---

# REFERÊNCIAS

No final de cada arquivo existe a seção:

Referências

Ela deve:

- estar em Times New Roman 12;
- negrito;
- permanecer como cabeçalho;
- NÃO virar bullet.

As referências devem ser numeradas na ordem em que aparecem:

[1] ...
[2] ...
[3] ...
[4] ...

Preserve itálicos nos títulos quando apropriado.

---

# CITAÇÕES NO CORPO DO TEXTO

Converta TODAS as chamadas bibliográficas no corpo para o número correspondente entre colchetes.

Exemplo:

(Sculley et al., 2015)

pode se tornar:

[1]

se Sculley et al. for a referência [1].

Objetivo: reduzir caracteres e tornar os dez arquivos homogêneos.

Faça essa conversão somente quando a correspondência bibliográfica for inequívoca.

NÃO converta:

- números comuns;
- fórmulas;
- enumerações;
- referências vagas a autores que não sejam citações.

Verifique que toda citação `[n]` tenha referência correspondente e que nenhuma referência renumerada fique quebrada.

---

# ESTILO FINAL

Os documentos devem parecer partes de uma MESMA coleção de estudo.

Ao compará-los lado a lado, devem ter:

- mesma fonte;
- mesmo tamanho;
- mesmos padrões de cabeçalho;
- mesmos padrões de equação;
- mesmos padrões de diagramas;
- mesma lógica de listas;
- mesma lógica de referências;
- mesma densidade visual;
- mesma filosofia editorial.

Homogeneização NÃO significa tornar os textos semanticamente idênticos.

Preserve a personalidade técnica de cada ponto.

---

# ARQUIVOS DE SAÍDA

Para cada original:

arquivo.docx

crie:

arquivo_v2.docx

no mesmo diretório.

Exemplo:

1-pdle-armazenamento-e-gerenciamento-distribuido-de-dados.docx

→

1-pdle-armazenamento-e-gerenciamento-distribuido-de-dados_v2.docx

NÃO altere nem sobrescreva:

- `.docx` originais;
- `.md` originais;
- edital;
- resolução;
- barema.

Logs, relatórios e arquivos auxiliares devem ficar na raiz:

<concurso-ufc-2027>/

Remova arquivos temporários ao final, se não forem necessários.

---

# VALIDAÇÃO OBRIGATÓRIA POR ARQUIVO

Após criar cada `_v2.docx`, faça uma segunda leitura/inspeção e confirme:

1. O arquivo abre como DOCX válido.
2. O conteúdo essencial do Markdown mestre está preservado.
3. A contagem está entre 5.200 e 5.800 caracteres não-brancos, idealmente 5.500–5.600.
4. Nunca ultrapassa 6.000.
5. Times New Roman 12 foi aplicado onde esperado.
6. Equações são Office Math nativas.
7. Equações display estão centralizadas.
8. Título principal está centralizado.
9. Fluxogramas estão centralizados.
10. Corpo está justificado.
11. Cabeçalhos estão em TNR 12 bold.
12. Não restam `#`, `**`, `*`, `\(`, `\)`, `\[`, `\]` ou `---` como sintaxe Markdown residual.
13. Símbolos Unicode foram preservados.
14. Títulos numerados não viraram bullets.
15. Listas verdadeiras usam bullets consistentemente.
16. Referências usam `[1]`, `[2]`, etc.
17. Citações no corpo correspondem à numeração final.
18. Nenhuma referência inexistente foi criada.
19. Nenhum erro técnico foi introduzido pela compressão.
20. O documento mantém boa legibilidade.

---

# RELATÓRIO FINAL

Atualize:

<concurso-ufc-2027>/revision-report.md

com uma tabela final contendo, para cada ponto:

- arquivo;
- caracteres não-brancos antes;
- caracteres não-brancos depois;
- reescrita realizada? SIM/NÃO;
- principais motivos de reescrita;
- correções técnicas realizadas;
- número de referências;
- resultado da validação;
- observações relevantes.

Adicione ao final uma seção:

## Global Consistency Check

Nela, confirme se os 10 arquivos foram comparados entre si após a geração e se seguem a mesma especificação visual.

Se encontrar alguma diferença injustificada, corrija o `_v2.docx` correspondente antes de encerrar.

---

# PRINCÍPIOS DE SEGURANÇA EDITORIAL

Ao longo de todo o trabalho:

- NÃO faça alterações silenciosas de conteúdo científico sem registrar no relatório.
- NÃO invente referências.
- NÃO invente fórmulas.
- NÃO acrescente ferramentas ou tecnologias apenas por associação temática.
- NÃO transforme o texto em tutorial operacional.
- NÃO ultrapasse 6.000 caracteres não-brancos.
- NÃO sobrescreva os originais.
- NÃO confunda homogeneização visual com uniformização semântica.
- NÃO confie apenas na aparência: valide programaticamente o conteúdo e a estrutura dos DOCX produzidos.

Prioridade final:

ACURÁCIA
→ ADEQUAÇÃO AO BAREMA
→ CONTEÚDO ESSENCIAL
→ TAMANHO ESCREVÍVEL
→ HOMOGENEIDADE
→ FORMATAÇÃO

Execute o processo completo para os 10 pontos.
