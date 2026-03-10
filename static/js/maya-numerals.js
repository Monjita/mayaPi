/**
 * maya-numerals.js
 * Numerales mayas 0–59 en sistema posicional vigesimal
 * 0–19  → 1 glifo
 * 20–39 → 2 glifos apilados (1 arriba, resto abajo)
 * 40–59 → 2 glifos apilados (2 arriba, resto abajo)
 */

const MayaNumerals = (() => {

  // [barras, puntos] para 0–19
  const GLYPHS = [
    [0, 0], // 0
    [0, 1], // 1
    [0, 2], // 2
    [0, 3], // 3
    [0, 4], // 4
    [1, 0], // 5
    [1, 1], // 6
    [1, 2], // 7
    [1, 3], // 8
    [1, 4], // 9
    [2, 0], // 10
    [2, 1], // 11
    [2, 2], // 12
    [2, 3], // 13
    [2, 4], // 14
    [3, 0], // 15
    [3, 1], // 16
    [3, 2], // 17
    [3, 3], // 18
    [3, 4], // 19
  ];

  // Construye un glifo simple (0–19)
  function buildSingle(value) {
    const n = Math.max(0, Math.min(19, Math.floor(value)));
    const [bars, dots] = GLYPHS[n];
    const el = document.createElement('div');
    el.className = 'mg__glyph';

    if (n === 0) {
      const zero = document.createElement('div');
      zero.className = 'mg__zero';
      el.appendChild(zero);
      return el;
    }

    // Puntos
    if (dots > 0) {
      const dotsRow = document.createElement('div');
      dotsRow.className = 'mg__dots';
      for (let i = 0; i < dots; i++) {
        const dot = document.createElement('span');
        dot.className = 'mg__dot';
        dotsRow.appendChild(dot);
      }
      el.appendChild(dotsRow);
    }

    // Barras
    for (let i = 0; i < bars; i++) {
      const bar = document.createElement('div');
      bar.className = 'mg__bar';
      el.appendChild(bar);
    }

    return el;
  }

  // Construye el contenedor completo para un valor 0–59
  // Sistema posicional: upper = floor(value/20), lower = value % 20
  function buildGlyph(value) {
    const n = Math.max(0, Math.min(59, Math.floor(value)));
    const upper = Math.floor(n / 20); // 0, 1 o 2
    const lower = n % 20;

    const wrapper = document.createElement('div');
    wrapper.className = 'mg';

    if (upper === 0) {
      // Solo 1 glifo
      wrapper.appendChild(buildSingle(lower));
    } else {
      // 2 glifos apilados: upper arriba, lower abajo
      // separados por una línea divisoria
      const top = buildSingle(upper);
      top.classList.add('mg__glyph--top');

      const divider = document.createElement('div');
      divider.className = 'mg__divider';

      const bot = buildSingle(lower);
      bot.classList.add('mg__glyph--bot');

      wrapper.classList.add('mg--stacked');
      wrapper.appendChild(top);
      wrapper.appendChild(divider);
      wrapper.appendChild(bot);
    }

    return wrapper;
  }

  function render(element, value) {
    element.innerHTML = '';
    element.appendChild(buildGlyph(value));
  }

  function renderAll() {
    document.querySelectorAll('[data-maya]').forEach(el => {
      const val = parseInt(el.getAttribute('data-maya'), 10);
      if (!isNaN(val)) render(el, val);
    });
  }

  return { render, renderAll, buildGlyph };
})();

document.addEventListener('DOMContentLoaded', MayaNumerals.renderAll);