# Tarefa: gerar "frases-gatilho" de memorização a partir das dissertações (.docx → .note)

## Contexto (leia com atenção: é isso que define o nível de compressão)

Estou em <concurso-ufc-2027> (raiz). Vou fazer a **prova escrita de um concurso público para magistério superior (UFC)**. São 10 pontos; **3 serão sorteados 15 minutos antes da prova**, sem consulta. Para cada ponto sorteado, escrevo uma dissertação em ~80 minutos (240 min no total).

Os arquivos abaixo são o **texto final de cada ponto**, que eu preciso conseguir reproduzir na prova (~5.560 caracteres sem espaços cada, o que consigo escrever em 75–80 min):

```
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

**O drama:** faltam ~2 semanas e eu domino poucos desses pontos. Tentei decorar palavra por palavra (palavras-chave + símbolos por parágrafo) e funciona, mas é exaustivo: estou na metade do ponto 1 e não vai dar tempo para os 10. Mudei de estratégia. Vou decorar **um esqueleto de gatilhos, uma linha por parágrafo**, treinar com recordação ativa (folha em branco → escrevo os gatilhos de memória → confiro) e repetição espaçada, e na prova **reconstruir cada parágrafo com minhas palavras** a partir do gatilho.

Então cada gatilho precisa ser:
- **curto o bastante** para eu decorar 10 esqueletos em 2 semanas;
- **rico o bastante** para eu reconstruir o parágrafo inteiro (ideia central + termos técnicos que a banca espera ver).

Antes de começar, leia a parte da **prova escrita** em `edital/barema-quixada.md` (e, se ajudar, `edital/edital.md` e `edital/resolucao-cepe.md`) para entender o que a banca avalia. Priorize nos gatilhos os elementos que pontuam: conceitos-chave, encadeamento lógico, trade-offs, exemplos/sistemas citados, referências.

## Saída

Para cada `.docx`, escreva no arquivo `.note` correspondente **na mesma pasta** (mesmo nome-base; pode variar o sufixo `_v2`. Procure o que existir. Se não existir nenhum, crie `<nome-base>.note`).

- **Nunca sobrescreva**: use append (`>>`). A maioria está vazia; algumas têm conteúdo meu.
- **Antes de escrever, leia o conteúdo existente do `.note`.** Se houver exemplos meus de gatilhos ou de referências, use-os como padrão de formato.
- Não modifique os `.docx`.

## Regras dos gatilhos

1. **Um gatilho por parágrafo.** Parágrafo é TUDO que "começa" no texto, inclusive frases curtas de abertura, como "Dois mecanismos estruturam o problema:". **Cada bullet point é um parágrafo** e ganha sua própria linha (mantenha o marcador `-`).
2. **Abertura literal:** todo gatilho começa com as palavras que REALMENTE iniciam o parágrafo: o artigo (se houver) + a 1ª palavra. No máximo 2 palavras. Ex.: parágrafo "O crescimento do volume de dados..." → gatilho começa com `O crescimento`.
3. **Resto do gatilho:** livre, otimizado para memória e reconstrução. Corte conectivos e mantenha termos técnicos. Pode usar operadores: `→` (leva a), `∴` (portanto), `≠` (mas/contudo), `=` (é/define), `+` (e), `↑`/`↓` (aumenta/reduz), `×` (versus/trade-off).
4. **Tamanho:** 4 a 6 palavras no total (5 é o ideal), contando a abertura. Máximo de **10 palavras** só para parágrafos realmente complexos.
5. **Fórmulas e diagramas:** mantenha **exatamente** como estão (copie literal). Diagramas costumam ser grandes sínteses, então preserve-os inteiros. Se um diagrama for imagem (sem texto extraível), escreva `[DIAGRAMA: <legenda/descrição curta>]` e me avise no relatório.
6. **Referências:** formato curto, uma por linha:
   `[N] Sobrenome et al. PERIÓDICO/EVENTO. AAAA.`
   - Apenas **um** sobrenome (o do primeiro autor); `et al.` se houver mais autores.
   - Sem título, volume, páginas, DOI ou editora.
   - Ex.: `[3] DeCandia et al. SOSP. 2007.`
7. **Títulos de seção** (ex.: `## 1.2. Particionamento, Sharding e Distribuição dos Dados`): copie-os literalmente, como separadores. Eles não contam como parágrafo.

Exemplo (parágrafo → gatilho):
- "O crescimento do volume de dados e da demanda por acesso pode tornar inadequado o armazenamento em um único nó, ..." → `O crescimento: dado ↑ → 1 nó insuficiente`
- "Embora a escalabilidade vertical amplie os recursos de uma única máquina, ela possui limites físicos e econômicos; ..." → `Embora vertical: limite físico/econômico → horizontal`
- "A distribuição, contudo, não produz escalabilidade ou tolerância a falhas automaticamente." → `A distribuição ≠ escala automática`

## Processo (iterativo, um arquivo por vez)

Para cada `.docx`, em ordem (1 → 10):

1. **Extraia o texto preservando ordem, listas, fórmulas e tabelas.** Prefira `pandoc -t markdown <arquivo>.docx` (preserva equações e listas melhor que python-docx). Instale o que faltar.
2. **Conte os parágrafos** (incluindo aberturas curtas e cada bullet) e as referências.
3. **Gere os gatilhos** seguindo as regras.
4. **Verifique antes de gravar:**
   - nº de gatilhos == nº de parágrafos;
   - todo gatilho começa com as palavras literais do parágrafo (no máximo 2);
   - gatilhos fora de 4–6 palavras são exceções justificadas (≤ 10);
   - fórmulas/diagramas idênticos ao original;
   - referências no formato curto.
5. **Grave com append** no `.note`, com um cabeçalho de bloco:
```
   ===== GATILHOS v1 — <nome do arquivo> — <data> =====
```
6. **Relatório curto** (no terminal, não no arquivo): nº de parágrafos, nº de gatilhos, nº de exceções > 6 palavras, diagramas-imagem encontrados e qualquer dúvida.

Depois do **primeiro arquivo**, pare e me mostre o resultado para eu validar o estilo antes de seguir para os outros 9. Se eu aprovar, processe o restante em sequência, um por vez, com o relatório de cada um.