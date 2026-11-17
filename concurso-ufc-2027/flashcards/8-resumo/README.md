# Flashcards — revisão da prova escrita (UFC)

Player local e offline para os 40 cards de `cards.json` (10 pontos × 4 cards). Sem dependências: HTML, CSS e JavaScript puro, servidos pelo Python do macOS.

## Como iniciar

```bash
cd /Users/egg/projects/concurso-ufc-2027/flashcards/8-resumo
./start.sh
```

O script abre `http://localhost:8000/` no navegador; `Ctrl+C` encerra. Outra porta: `./start.sh 8001`.

Sem o script:

```bash
python3 -m http.server 8000
```

e abra `http://localhost:8000/`. Abrir o `index.html` direto (`file://`) não funciona: o navegador bloqueia a leitura do `cards.json`.

## Teclas

| Tecla | Ação |
|---|---|
| `→` | revela a próxima linha; com todas visíveis, vai ao próximo card |
| `←` | volta um passo (esconde a última linha; da 1ª linha, volta à frente) |
| `Space` | frente do próximo card |
| `Shift` | frente do card anterior (tocar a tecla sozinha) |
| `1`–`9` | ponto 1–9, card 1, frente |
| `0` | ponto 10 |
| `R` | nova ordem aleatória |
| `S` | alterna aleatório / sequencial |
| `F` | tela cheia (`Esc` sai) |

O sorteio é por ponto: a ordem dos 10 pontos muda a cada rodada, mas os 4 cards de cada ponto vêm sempre na ordem 1 → 4.

## Arquivos

- `cards.json`: conteúdo dos cards (fonte única; o player só lê).
- `cards-preview.md`: prévia legível do `cards.json`.
- `index.html`, `style.css`, `app.js`: o player.
- `start.sh`: servidor local e abertura do navegador.
