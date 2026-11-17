'use strict';
/*
 * Player de flashcards da prova escrita (UFC).
 * Só lê cards.json: o conteúdo dos cards não é reescrito nem copiado aqui.
 */

const TOTAL_PONTOS = 10;
const CARDS_POR_PONTO = 4;

/*
 * Estado da sessão (máquina de estados de cada card):
 *   FRENTE (revelados = 0) → 1 linha → 2 linhas → … → N linhas → FRENTE do próximo card
 *
 *   modo        'aleatorio' | 'sequencial'
 *   ordem       os pontos 1–10 da rodada, na ordem em que serão estudados
 *   pos         índice do ponto atual em `ordem`
 *   card        0–3: os 4 cards do ponto, sempre nessa ordem
 *   revelados   0 = FRENTE; k = as k primeiras linhas do verso estão visíveis
 *   fim         tela de fim da rodada (não é um card)
 *   concluidos  pontos cujo card 4 já foi deixado para trás nesta rodada
 */
const estado = {
  modo: 'aleatorio', ordem: [], pos: 0, card: 0, revelados: 0, fim: false, concluidos: new Set(),
};
let pontos = null;            // número do ponto → objeto do cards.json
let destacarNova = false;     // a linha recém-revelada entra com um fade curto
let shiftSozinho = false;     // Shift só conta como "card anterior" se nenhuma outra tecla vier junto

// ---------- carregamento ----------

async function iniciar() {
  let resposta;
  try {
    resposta = await fetch('cards.json', { cache: 'no-store' });
    if (!resposta.ok) throw new Error(`HTTP ${resposta.status}`);
  } catch (_) {
    mostrarErro('Não foi possível carregar cards.json.',
      'Execute o player por um servidor HTTP local, na pasta do player:', 'python3 -m http.server 8000');
    return;
  }
  let dados;
  try {
    dados = await resposta.json();
  } catch (_) {
    mostrarErro('cards.json não é um JSON válido.', 'Corrija o arquivo e recarregue a página.');
    return;
  }
  const problema = validar(dados);
  if (problema) {
    mostrarErro('cards.json não tem a estrutura esperada.', problema);
    return;
  }
  aplicarTema(dados.theme);
  pontos = new Map(dados.points.map((p) => [p.point, p]));
  novaRodada('aleatorio');
  render();
}

/** Devolve a descrição do primeiro problema encontrado, ou null. Não corrige nada. */
function validar(d) {
  if (!d || !Array.isArray(d.points) || d.points.length !== TOTAL_PONTOS) {
    return `Eram esperados ${TOTAL_PONTOS} pontos em "points".`;
  }
  const numeros = d.points.map((p) => p.point);
  for (let n = 1; n <= TOTAL_PONTOS; n++) {
    if (!numeros.includes(n)) return `Falta o ponto ${n}.`;
  }
  for (const p of d.points) {
    if (!Array.isArray(p.cards) || p.cards.length !== CARDS_POR_PONTO) {
      return `Ponto ${p.point}: eram esperados ${CARDS_POR_PONTO} cards.`;
    }
    for (const [i, c] of p.cards.entries()) {
      const onde = `Ponto ${p.point}, card ${i + 1}`;
      if (c.card !== i + 1) return `${onde}: os cards não estão na ordem 1–4.`;
      if (!Array.isArray(c.lines) || c.lines.length === 0) return `${onde}: "lines" está vazio.`;
      if (!Array.isArray(c.sectionIds) || !Array.isArray(c.sectionTitles) || c.sectionIds.length === 0
          || c.sectionIds.length !== c.sectionTitles.length) {
        return `${onde}: "sectionIds" e "sectionTitles" não correspondem.`;
      }
      if (!Array.isArray(c.lineSections) || c.lineSections.length !== c.lines.length
          || !c.lineSections.every((s) => c.sectionIds.includes(s))) {
        return `${onde}: "lineSections" não corresponde a "lines".`;
      }
    }
  }
  return null;
}

function aplicarTema(tema) {
  const variaveis = { background: '--bg', text: '--text', border: '--border', muted: '--muted' };
  for (const [chave, nome] of Object.entries(variaveis)) {
    if (tema && typeof tema[chave] === 'string') document.documentElement.style.setProperty(nome, tema[chave]);
  }
}

// ---------- rodada e navegação ----------

// A unidade sorteada é o PONTO: a ordem dos 10 pontos é embaralhada uma vez por rodada
// (Fisher–Yates); os 4 cards de cada ponto nunca são embaralhados.
function embaralhar(lista) {
  const a = lista.slice();
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a;
}

function novaRodada(modo) {
  const sequencia = Array.from({ length: TOTAL_PONTOS }, (_, i) => i + 1);
  estado.modo = modo;
  estado.ordem = modo === 'aleatorio' ? embaralhar(sequencia) : sequencia;
  estado.pos = 0;
  estado.card = 0;
  estado.revelados = 0;
  estado.fim = false;
  estado.concluidos.clear();
}

function cardAtual() {
  return pontos.get(estado.ordem[estado.pos]).cards[estado.card];
}

/** → : revela uma linha; com todas visíveis, vai à frente do próximo card. */
function avancar() {
  if (estado.fim) return;
  if (estado.revelados < cardAtual().lines.length) {
    estado.revelados += 1;
    destacarNova = true;
  } else {
    proximoCard();
  }
}

/** ← : volta exatamente um passo; na frente, fica na frente. */
function voltar() {
  if (!estado.fim && estado.revelados > 0) estado.revelados -= 1;
}

/** Space : frente do próximo card, sem revelar nada; depois do card 4, o próximo ponto da ordem. */
function proximoCard() {
  if (estado.fim) return;
  estado.revelados = 0;
  if (estado.card < CARDS_POR_PONTO - 1) {
    estado.card += 1;
    return;
  }
  estado.concluidos.add(estado.ordem[estado.pos]);
  if (estado.pos < estado.ordem.length - 1) {
    estado.pos += 1;
    estado.card = 0;
  } else {
    estado.fim = true;
  }
}

/** Shift : frente do card anterior (do card 1, o card 4 do ponto anterior na ordem). */
function cardAnterior() {
  estado.revelados = 0;
  if (estado.fim) {
    estado.fim = false;               // volta ao último card da rodada
  } else if (estado.card > 0) {
    estado.card -= 1;
  } else if (estado.pos > 0) {
    estado.pos -= 1;
    estado.card = CARDS_POR_PONTO - 1;
  }
}

/** 1–9, 0 : card 1 do ponto, na frente; a rodada continua a partir da posição desse ponto na ordem. */
function abrirPonto(n) {
  estado.pos = estado.ordem.indexOf(n);
  estado.card = 0;
  estado.revelados = 0;
  estado.fim = false;
}

function alternarModo() {
  novaRodada(estado.modo === 'aleatorio' ? 'sequencial' : 'aleatorio');
}

function alternarTelaCheia() {
  const doc = document;
  const el = doc.documentElement;
  try {
    const pedido = (doc.fullscreenElement || doc.webkitFullscreenElement)
      ? (doc.exitFullscreen || doc.webkitExitFullscreen).call(doc)
      : (el.requestFullscreen || el.webkitRequestFullscreen).call(el);
    if (pedido && pedido.catch) pedido.catch(() => {});   // recusado pelo navegador: ignora
  } catch (_) { /* sem suporte: ignora */ }
}

// ---------- teclado ----------

// Cada pressão deliberada = uma ação; a repetição automática de uma tecla segurada é ignorada.
const ACOES = {
  ArrowRight: avancar,
  ArrowLeft: voltar,
  ' ': proximoCard,
  r: () => novaRodada('aleatorio'),
  s: alternarModo,
  f: alternarTelaCheia,
};

window.addEventListener('keydown', (e) => {
  if (e.key === 'Shift') {
    if (!e.repeat) shiftSozinho = !e.metaKey && !e.ctrlKey && !e.altKey;
    return;
  }
  shiftSozinho = false;
  if (e.metaKey || e.ctrlKey || e.altKey) return;     // atalhos do navegador continuam normais
  const tecla = e.key.length === 1 ? e.key.toLowerCase() : e.key;
  let acao = ACOES[tecla];
  if (!acao && /^[0-9]$/.test(tecla)) acao = () => abrirPonto(tecla === '0' ? 10 : Number(tecla));
  if (!acao) return;
  e.preventDefault();                                   // Space não rola a página, setas não rolam
  if (e.repeat || (!pontos && acao !== alternarTelaCheia)) return;
  acao();
  if (pontos) render();
});

// Shift é modificador: a ação dispara ao soltar, e só se a tecla foi tocada sozinha.
window.addEventListener('keyup', (e) => {
  if (e.key !== 'Shift' || !shiftSozinho) return;
  shiftSozinho = false;
  if (!pontos) return;
  cardAnterior();
  render();
});

window.addEventListener('blur', () => { shiftSozinho = false; });

// ---------- desenho ----------

function criar(tag, classe, texto) {
  const el = document.createElement(tag);
  if (classe) el.className = classe;
  if (texto !== undefined) el.textContent = texto;
  return el;
}

/**
 * Markdown mínimo: "**termo**" vira <strong>. O texto entra sempre como nó de texto
 * (nada de innerHTML), então < > & e Unicode aparecem exatamente como estão no JSON.
 */
function comNegrito(el, texto) {
  const partes = texto.split('**');
  if (partes.length % 2 === 0) {        // ** sem par: mostra literalmente, sem adivinhar
    el.textContent = texto;
    return el;
  }
  partes.forEach((parte, i) => {
    if (parte) el.append(i % 2 ? criar('strong', null, parte) : parte);
  });
  return el;
}

function definirHud(esquerda, direita) {
  document.getElementById('posicao').textContent = esquerda;
  document.getElementById('progresso').textContent = direita;
}

function render() {
  const raiz = document.getElementById('card');
  const modo = estado.modo === 'aleatorio' ? 'Aleatório' : 'Sequencial';
  document.body.dataset.ordem = estado.ordem.join(',');
  if (estado.fim) {
    definirHud(`Fim da rodada · ${modo}`, '');
    raiz.dataset.estado = 'fim';
    raiz.replaceChildren(telaFim());
    return;
  }
  const p = pontos.get(estado.ordem[estado.pos]);
  const c = p.cards[estado.card];
  definirHud(`Ponto ${p.point} — Card ${c.card} de ${CARDS_POR_PONTO} · ${modo}`,
    `${estado.revelados} / ${c.lines.length}`);
  Object.assign(raiz.dataset, {
    estado: estado.revelados ? 'verso' : 'frente', ponto: p.point, card: c.card, revelados: estado.revelados,
  });
  raiz.replaceChildren(estado.revelados ? verso(p, c) : frente(p, c));
  const nova = raiz.querySelector('.nova');
  if (nova) nova.scrollIntoView({ block: 'nearest' });
  else if (!estado.revelados) raiz.scrollTop = 0;
  destacarNova = false;
}

/** Frente: só o ponto, o número do card e as seções (o prompt da recuperação). */
function frente(p, c) {
  const el = criar('div', 'frente');
  el.append(
    criar('p', 'rotulo', `Ponto ${p.point}`),
    criar('h1', 'titulo', p.title),
    criar('p', 'rotulo', `Card ${c.card} / ${CARDS_POR_PONTO}`),
  );
  const lista = criar('ol', 'secoes');
  c.sectionIds.forEach((id, i) => {
    const li = criar('li');
    li.append(criar('span', 'id', id), criar('span', 'nome', c.sectionTitles[i]));
    lista.append(li);
  });
  el.append(lista, criar('p', 'dica', '→ para começar'));
  return el;
}

/** Verso: só as linhas já reveladas; o título de uma seção entra junto com a 1ª linha dela. */
function verso(p, c) {
  const el = criar('div', 'verso');
  el.append(criar('p', 'rotulo', `Ponto ${p.point} · Card ${c.card} / ${CARDS_POR_PONTO} · ${p.title}`));
  let bloco = null;
  for (let i = 0; i < estado.revelados; i++) {
    const sec = c.lineSections[i];
    const nova = destacarNova && i === estado.revelados - 1;
    let alvoDoFade = null;
    if (!bloco || bloco.dataset.secao !== sec) {
      bloco = criar('section', 'bloco');
      bloco.dataset.secao = sec;
      bloco.append(criar('h2', 'secao', `${sec} — ${c.sectionTitles[c.sectionIds.indexOf(sec)]}`));
      el.append(bloco);
      alvoDoFade = bloco;               // seção nova: título, divisória e linha entram juntos
    }
    const linha = comNegrito(criar('p', 'linha'), c.lines[i]);
    bloco.append(linha);
    if (nova) (alvoDoFade || linha).classList.add('nova');
  }
  return el;
}

function telaFim() {
  const el = criar('div', 'fim');
  const n = estado.concluidos.size;
  el.append(
    criar('p', 'rotulo', 'Fim da rodada'),
    criar('h1', 'titulo', n === TOTAL_PONTOS ? `${n} pontos concluídos` : `${n} de ${TOTAL_PONTOS} pontos concluídos`),
  );
  const opcoes = criar('ul', 'opcoes');
  const outroModo = estado.modo === 'aleatorio' ? 'modo sequencial' : 'modo aleatório';
  for (const [tecla, texto] of [['R', 'nova ordem aleatória'], ['S', outroModo], ['1–0', 'abrir ponto']]) {
    const li = criar('li');
    li.append(criar('kbd', null, tecla), texto);
    opcoes.append(li);
  }
  el.append(opcoes);
  return el;
}

function mostrarErro(titulo, texto, comando) {
  definirHud('Erro', '');
  const raiz = document.getElementById('card');
  raiz.dataset.estado = 'erro';
  const el = criar('div', 'erro');
  el.append(criar('h1', 'titulo', titulo), criar('p', null, texto));
  if (comando) el.append(criar('pre', null, comando));
  raiz.replaceChildren(el);
}

iniciar();
