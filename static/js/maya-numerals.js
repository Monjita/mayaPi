/**
 * maya-numerals.js
 * Dibuja numerales mayas (0-19) con CSS puro
 * Sin dependencias de fuentes externas
 *
 * Uso:
 *   <div class="maya-glyph" data-value="13"></div>
 *   MayaNumerals.render(element, 13)
 *   MayaNumerals.renderAll()
 */

const MayaNumerals = (() => {

  // 0-19: [barras, puntos]
  // barra = 5, punto = 1
  const GLYPHS = [
    [0, 0], // 0  — concha (especial)
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

  function buildGlyph(value) {
    const n = Math.max(0, Math.min(19, Math.floor(value)));
    const [bars, dots] = GLYPHS[n];
    const wrapper = document.createElement('div');
    wrapper.className = 'mg';

    if (n === 0) {
      // Símbolo especial para el cero: concha/óvalo
      const zero = document.createElement('div');
      zero.className = 'mg__zero';
      wrapper.appendChild(zero);
      return wrapper;
    }

    // Puntos encima
    if (dots > 0) {
      const dotsRow = document.createElement('div');
      dotsRow.className = 'mg__dots';
      for (let i = 0; i < dots; i++) {
        const dot = document.createElement('span');
        dot.className = 'mg__dot';
        dotsRow.appendChild(dot);
      }
      wrapper.appendChild(dotsRow);
    }

    // Barras debajo
    for (let i = 0; i < bars; i++) {
      const bar = document.createElement('div');
      bar.className = 'mg__bar';
      wrapper.appendChild(bar);
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

// Auto-inicializar al cargar el DOM
document.addEventListener('DOMContentLoaded', MayaNumerals.renderAll);