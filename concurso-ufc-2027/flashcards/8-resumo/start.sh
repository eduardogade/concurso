#!/bin/bash
# Serve o player em http://localhost:8000/ (ou na porta passada como argumento) e abre o navegador.
# Ctrl+C encerra o servidor.
cd "$(dirname "$0")" || exit 1
PORTA="${1:-8000}"
(sleep 1 && open "http://localhost:${PORTA}/") &
exec python3 -m http.server "$PORTA" --bind 127.0.0.1
