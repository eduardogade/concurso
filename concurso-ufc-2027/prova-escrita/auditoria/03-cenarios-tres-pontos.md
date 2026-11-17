# Auditoria 1 — Cenários com três pontos

Data: 02/11/2026.

## 1. Regra oficial

O que os documentos permitidos estabelecem:

| Regra | Fonte |
|---|---|
| Programa de 10 pontos; 3 sorteados para desenvolvimento obrigatório | Edital 48/2026, item 16.4 (`edital/edital.md` L968) |
| Sorteio único e centralizado, mesmos pontos para todos | Item 16.5–16.6 (L970–972); Res. 15/CEPE, art. 20 § 1º |
| Os 3 pontos em "texto único ou mediante subdivisões", desde que se identifique o desenvolvimento de cada um | Item 16.7 (L974); art. 20 § 2º |
| **Eliminação** de quem deixar de desenvolver, "total ou parcialmente", qualquer um dos 3 pontos | Item 16.8 (L976); art. 20 § 2º |
| Duração de 4 horas | Item 16.1 (L962); art. 20 § 4º |
| Cada examinador atribui **uma** nota de 0 a 10 à prova, com justificativa, na ficha de avaliação | Item 16.10 (L980); art. 21 § 1º |
| Diferença máxima de 3,00 pontos entre examinadores, acima da qual há reavaliação | Item 16.10; art. 21 § 3º |
| Nota = média aritmética dos 3 examinadores; aprovação com média ≥ 7,00 | Item 16.11 (L982); art. 18 § 4º, II |
| A ficha tem um único bloco de critérios (Itens I e II), com 1.1 referido ao "ponto sorteado" no singular | `edital/barema-quixada.md` L5–48 |

O texto da resolução foi conferido no PDF (`edital/resolucao_15_cepe.pdf`, via pdftotext). Os aditivos 1–4 não alteram essas regras: tratam de cronograma (1 e 4), quadro de vagas (2, itens 3.3–3.4) e prova em Libras/anexos de outros setores (3).

**Conclusão: não há regra oficial de agregação de notas por ponto.** Cada examinador aplica a ficha uma única vez à dissertação inteira. Tudo o que segue é **análise exploratória**, sob a hipótese de que a nota holística se aproxime da média aritmética das notas por ponto do Relatório 1.

Duas consequências práticas não dependem de hipótese:

- **Um ponto incompleto elimina**, independentemente da qualidade dos outros dois.
- **1.3 e o Item II (3,0 pontos)** são julgados sobre o texto inteiro. A hipótese dos 95% vale, portanto, para a prova como um todo.

## 2. Modelo exploratório

- **M1 (média):** nota da prova ≈ média das notas dos três pontos sorteados, cada uma nas leituras R1, R2 e R3 do Relatório 1. A mesma banca corrige os três pontos, então os cenários são coerentes: as três notas são tomadas na mesma leitura.
- **M2 (elo mais fraco):** menor das três notas. É só uma lente pessimista, sem base normativa: mostra quanto a combinação depende do pior ponto.

Foram enumeradas as C(10,3) = 120 combinações. Os números abaixo são **contagens de combinações, não probabilidades**: o sorteio é tratado apenas como "qualquer trio é possível".

## 3. Estatísticas descritivas (M1)

| Leitura | Mínimo | 1º quartil | Mediana | 3º quartil | Máximo | Trios < 7,00 | Trios ≥ 8,00 |
|---|---|---|---|---|---|---|---|
| R1 literal | 6,38 | 6,79 | 6,97 | 7,18 | 7,65 | 63 de 120 | 0 de 120 |
| R2 central | 7,01 | 7,55 | 7,77 | 8,05 | 8,67 | 0 de 120 | 34 de 120 |
| R3 viável | 7,90 | 8,43 | 8,66 | 8,89 | 9,41 | 0 de 120 | 118 de 120 |

Na leitura central, nenhum trio fica abaixo de 7,00, mas o pior trio fica praticamente no limite. Na leitura literal, a maioria dos trios fica abaixo de 7,00.

## 4. Trios extremos (M1, leitura central)

| | Trio | Central | Literal (R1) | Viável (R3) | Elo mais fraco (M2, central) |
|---|---|---|---|---|---|
| Piores | 1, 5, 8 | 7,01 | 6,38 | 7,90 | 6,97 (P5) |
|  | 4, 5, 8 | 7,10 | 6,49 | 7,96 | 6,97 (P5) |
|  | 1, 4, 5 | 7,15 | 6,46 | 8,01 | 6,97 (P5) |
|  | 5, 7, 8 | 7,15 | 6,51 | 8,04 | 6,97 (P5) |
|  | 1, 4, 8 | 7,15 | 6,41 | 8,17 | 6,97 (P8) |
|  | 1, 5, 7 | 7,19 | 6,48 | 8,10 | 6,97 (P5) |
|  | 1, 7, 8 | 7,19 | 6,43 | 8,26 | 6,97 (P8) |
|  | 5, 6, 8 | 7,25 | 6,68 | 8,06 | 6,97 (P5) |
| Melhores | 3, 9, 10 | 8,67 | 7,65 | 9,41 | 8,33 (P9) |
|  | 2, 3, 10 | 8,66 | 7,48 | 9,36 | 8,31 (P2) |
|  | 2, 9, 10 | 8,61 | 7,50 | 9,37 | 8,31 (P2) |
|  | 3, 6, 10 | 8,50 | 7,46 | 9,21 | 7,83 (P6) |
|  | 6, 9, 10 | 8,45 | 7,48 | 9,22 | 7,83 (P6) |

## 5. Peso de cada ponto nos trios

Média da nota central (M1) dos 36 trios que contêm cada ponto, comparada com a dos 84 que não o contêm:

| Ponto | Central do ponto | Média dos trios com o ponto | Média dos trios sem o ponto | Efeito | Trios com R1 < 7,00 entre os que contêm o ponto |
|---|---|---|---|---|---|
| 1 | 7,1 | 7,62 | 7,88 | −0,26 | 28 de 36 |
| 2 | 8,3 | 7,94 | 7,75 | +0,19 | 13 de 36 |
| 3 | 8,5 | 7,98 | 7,73 | +0,25 | 10 de 36 |
| 4 | 7,4 | 7,69 | 7,85 | −0,16 | 25 de 36 |
| 5 | 7,0 | 7,59 | 7,90 | −0,31 | 27 de 36 |
| 6 | 7,8 | 7,81 | 7,80 | +0,01 | 14 de 36 |
| 7 | 7,5 | 7,73 | 7,84 | −0,11 | 25 de 36 |
| 8 | 7,0 | 7,59 | 7,90 | −0,31 | 27 de 36 |
| 9 | 8,3 | 7,94 | 7,75 | +0,19 | 9 de 36 |
| 10 | 9,2 | 8,17 | 7,65 | +0,52 | 11 de 36 |

## 6. Leitura dos cenários

- **Pior trio na leitura central:** 1, 5, 8, com 7,01.
- **Pontos que mais baixam um trio:** 5 e 8 (central 7,0), seguidos do 1 (7,1). Melhorar qualquer um deles eleva o piso de todos os 36 trios em que aparece.
- **Ponto 10:** é o que mais eleva a média. Um trio com 10, 3 e 2 ou 9 fica acima de 8,6 na leitura central.
- **Faixa de incerteza:** como a mesma banca corrige os três pontos, a incerteza não diminui por agregação. A faixa R1–R3 de cada trio continua com 1,3 a 2,0 pontos de largura.
- **Limites da análise:**
  - nada aqui é probabilidade de sorteio ou de aprovação;
  - a média aritmética é uma hipótese de trabalho, não a fórmula oficial;
  - a regra do item 16.8 (ponto incompleto elimina) domina qualquer cálculo de média.

