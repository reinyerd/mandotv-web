// Tema de la portada: oscuro por defecto; claro solo si la persona lo eligió con el botón de la barra (app.js lo guarda).
// Va en el <head> sin defer para aplicarse antes de pintar: así no hay destello del tema equivocado.
try { if (localStorage.getItem('mando-tema') === 'claro') document.documentElement.dataset.tema = 'claro'; } catch (e) {}
// Con JavaScript, los puntos de color y "Tu equipo" se muestran desde el primer cuadro (27-nov): si esperaban a app.js
// (que quita .sin-js al cargar), aparecían después de pintar y empujaban la portada 14 px (CLS). .aparece sigue
// esperando a app.js para que sin él nada quede invisible.
document.documentElement.classList.add('js-pronto');
// Aviso de idioma de la portada (27-nov): se decide aquí, antes de pintar, para reservar su franja arriba desde el
// primer cuadro (estilos.css, html[data-aviso-idioma]); si entrara después empujaría la portada hacia abajo (CLS).
// Mismas reglas que el aviso de cookies.js, que en la portada usa esta decisión en vez de repetirla.
(function () {
  function codigo(x) {
    x = String(x || '').toLowerCase().replace('_', '-');
    if (/^zh-(tw|hk|mo|hant)/.test(x)) return 'zh-hant';
    if (/^zh/.test(x)) return 'zh-hans';
    if (/^(no|nn|nb)(-|$)/.test(x)) return 'nb';
    if (/^iw(-|$)/.test(x)) return 'he';
    if (/^in(-|$)/.test(x)) return 'id';
    return x.split('-')[0];
  }
  try {
    var d = document.documentElement;
    if (localStorage.getItem('mandotv-idioma')) return;
    if (document.referrer && new URL(document.referrer).host === location.host) return;
    var actual = codigo(d.lang), gemelas = {};
    document.querySelectorAll('link[rel="alternate"][hreflang]').forEach(function (l) {
      gemelas[l.getAttribute('hreflang').toLowerCase()] = true;
    });
    var preferidos = navigator.languages && navigator.languages.length ? navigator.languages : [navigator.language || ''];
    var destino = null;
    for (var i = 0; i < preferidos.length; i++) {
      var c = codigo(preferidos[i]);
      if (c === actual) return;
      if (gemelas[c]) { destino = c; break; }
    }
    if (!destino && actual !== 'en' && gemelas.en) destino = 'en';
    if (destino) d.dataset.avisoIdioma = destino;
  } catch (e) { /* sin almacenamiento o sin hreflang: sin hueco; cookies.js decide solo */ }
})();
