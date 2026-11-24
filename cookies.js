// Pila fija de abajo (24-nov): el aviso de idioma y el de cookies van uno sobre otro y nunca se tapan entre sí.
function pilaAvisos() {
  var pila = document.querySelector('.avisos');
  if (!pila) {
    pila = document.createElement('div');
    pila.className = 'avisos';
    document.body.appendChild(pila);
  }
  return pila;
}

// Aviso de cookies de Mando TV.
// Google Analytics (cookies) SOLO se carga si la persona pulsa "Aceptar". Sin respuesta o con "Rechazar"
// no se descarga nada de Google. La elección se guarda en este navegador y se puede cambiar con el
// botón "Cookies" del pie de página.
(function () {
  var ID_GA = 'G-2TDRY67ZJC';
  var CLAVE = 'mandotv-cookies'; // 'si' | 'no'
  var cargado = false;
  var aviso;
  // Textos del aviso por idioma (<html lang>): es por defecto; en, de, fr, pt e it con tabla propia.
  var TEXTOS = {
    es: { aria: 'Aviso de cookies', titulo: '¿Nos dejas contar tus visitas con cookies?',
          texto: 'Usamos Google Analytics para saber qué páginas se leen y mejorar la web. Solo se activa si aceptas.',
          url: '/privacidad.html#cookies', mas: 'Más sobre las cookies', si: 'Aceptar', no: 'Rechazar' },
    en: { aria: 'Cookie notice', titulo: 'Can we count your visits with cookies?',
          texto: 'We use Google Analytics to see which pages are read and improve the site. It only turns on if you accept.',
          url: '/en/privacy.html#cookies', mas: 'More about cookies', si: 'Accept', no: 'Decline' },
    de: { aria: 'Cookie-Hinweis', titulo: 'Dürfen wir deine Besuche mit Cookies zählen?',
          texto: 'Wir nutzen Google Analytics, um zu sehen, welche Seiten gelesen werden, und die Website zu verbessern. Es wird nur aktiviert, wenn du akzeptierst.',
          url: '/de/datenschutz.html#cookies', mas: 'Mehr über Cookies', si: 'Akzeptieren', no: 'Ablehnen' },
    fr: { aria: 'Avis sur les cookies', titulo: 'Pouvons-nous compter vos visites avec des cookies ?',
          texto: "Nous utilisons Google Analytics pour savoir quelles pages sont lues et améliorer le site. Il ne s'active que si vous acceptez.",
          url: '/fr/confidentialite.html#cookies', mas: 'En savoir plus sur les cookies', si: 'Accepter', no: 'Refuser' },
    pt: { aria: 'Aviso de cookies', titulo: 'Você deixa a gente contar as suas visitas com cookies?',
          texto: 'Usamos o Google Analytics para saber quais páginas são lidas e melhorar o site. Ele só é ativado se você aceitar.',
          url: '/pt/privacidade.html#cookies', mas: 'Saiba mais sobre cookies', si: 'Aceitar', no: 'Recusar' },
    it: { aria: 'Avviso sui cookie', titulo: 'Possiamo contare le tue visite con i cookie?',
          texto: "Usiamo Google Analytics per sapere quali pagine vengono lette e migliorare il sito. Si attiva solo se accetti.",
          url: '/it/privacy.html#cookies', mas: 'Maggiori informazioni sui cookie', si: 'Accetta', no: 'Rifiuta' }
  };
  var T = TEXTOS[(document.documentElement.lang || '').slice(0, 2)] || TEXTOS.es;

  function leer() { try { return localStorage.getItem(CLAVE); } catch (e) { return null; } }
  function guardar(v) { try { localStorage.setItem(CLAVE, v); } catch (e) { /* sin almacenamiento: se vuelve a preguntar */ } }

  function cargarAnaliticas() {
    if (cargado) return;
    cargado = true;
    window.dataLayer = window.dataLayer || [];
    window.gtag = function () { window.dataLayer.push(arguments); };
    window.gtag('js', new Date());
    window.gtag('config', ID_GA, { allow_google_signals: false, allow_ad_personalization_signals: false });
    var s = document.createElement('script');
    s.async = true;
    s.src = 'https://www.googletagmanager.com/gtag/js?id=' + ID_GA;
    document.head.appendChild(s);
  }

  // Al retirar el permiso: desactiva la medición y borra las cookies de Google Analytics.
  function borrarCookiesGa() {
    window['ga-disable-' + ID_GA] = true;
    document.cookie.split(';').forEach(function (c) {
      var nombre = c.split('=')[0].trim();
      if (/^_ga/.test(nombre)) {
        ['', '; domain=.mandotv.app', '; domain=mandotv.app'].forEach(function (d) {
          document.cookie = nombre + '=; Max-Age=0; path=/' + d;
        });
      }
    });
  }

  function crearAviso() {
    aviso = document.createElement('div');
    aviso.className = 'aviso-cookies';
    aviso.setAttribute('role', 'region');
    aviso.setAttribute('aria-label', T.aria);
    aviso.innerHTML =
      '<p><b>' + T.titulo + '</b> ' + T.texto + ' <a href="' + T.url + '">' + T.mas + '</a></p>' +
      '<div class="aviso-cookies-botones">' +
      '<button type="button" class="boton" data-eleccion="si">' + T.si + '</button>' +
      '<button type="button" class="boton" data-eleccion="no">' + T.no + '</button>' +
      '</div>';
    aviso.addEventListener('click', function (e) {
      var b = e.target.closest('[data-eleccion]');
      if (!b) return;
      var v = b.getAttribute('data-eleccion');
      guardar(v);
      if (v === 'si') { window['ga-disable-' + ID_GA] = false; cargarAnaliticas(); } else { borrarCookiesGa(); }
      aviso.hidden = true;
    });
    pilaAvisos().appendChild(aviso);
  }

  function mostrarAviso() {
    if (!aviso) crearAviso();
    aviso.hidden = false;
    var primero = aviso.querySelector('button');
    if (primero) primero.focus({ preventScroll: true });
  }

  document.addEventListener('click', function (e) {
    if (e.target.closest && e.target.closest('[data-cookies]')) { e.preventDefault(); mostrarAviso(); }
  });

  var eleccion = leer();
  if (eleccion === 'si') cargarAnaliticas();
  else if (eleccion !== 'no') {
    // Aparece cuando ya cargaron las fuentes: así no cambia de alto al llegar la letra y no mueve nada (CLS).
    var crearConFuentes = function () {
      var listas = document.fonts && document.fonts.ready;
      if (listas) listas.then(crearAviso, crearAviso); else crearAviso();
    };
    if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', crearConFuentes);
    else crearConFuentes();
  }
})();

// Aviso de idioma (24-nov): a quien llega desde fuera del sitio con el navegador en otro idioma que esta página tiene
// (sus <link rel="alternate" hreflang>), se le ofrece esa versión con un aviso que se cierra. No redirige solo:
// Google desaconseja redirigir por idioma y su robot tiene que ver cada versión tal cual. Se muestra una sola vez.
(function () {
  var CLAVE = 'mandotv-aviso-idioma';
  // Cada texto va en el idioma que se ofrece, el que esa persona entiende.
  var TEXTOS = {
    es: { aria: 'Idioma', texto: 'Esta página también está en español.', ir: 'Ver en español', cerrar: 'Cerrar' },
    en: { aria: 'Language', texto: 'This page is also available in English.', ir: 'View in English', cerrar: 'Close' },
    de: { aria: 'Sprache', texto: 'Diese Seite gibt es auch auf Deutsch.', ir: 'Auf Deutsch ansehen', cerrar: 'Schließen' },
    fr: { aria: 'Langue', texto: 'Cette page existe aussi en français.', ir: 'Voir en français', cerrar: 'Fermer' },
    pt: { aria: 'Idioma', texto: 'Esta página também está em português.', ir: 'Ver em português', cerrar: 'Fechar' },
    it: { aria: 'Lingua', texto: 'Questa pagina è disponibile anche in italiano.', ir: 'Vedi in italiano', cerrar: 'Chiudi' }
  };
  function guardar() { try { localStorage.setItem(CLAVE, '1'); } catch (e) { /* sin almacenamiento: nada que recordar */ } }
  try { if (localStorage.getItem(CLAVE)) return; } catch (e) { /* sigue */ }
  // Quien ya navega dentro del sitio eligió su idioma (por ejemplo con el selector del pie): no se le insiste.
  try { if (document.referrer && new URL(document.referrer).host === location.host) return; } catch (e) { /* sigue */ }

  var actual = (document.documentElement.lang || '').slice(0, 2).toLowerCase();
  var gemelas = {};
  document.querySelectorAll('link[rel="alternate"][hreflang]').forEach(function (l) {
    gemelas[l.getAttribute('hreflang').slice(0, 2).toLowerCase()] = l.href;
  });
  var preferidos = navigator.languages && navigator.languages.length ? navigator.languages : [navigator.language || ''];
  var destino = null;
  for (var i = 0; i < preferidos.length; i++) {
    var c = String(preferidos[i]).slice(0, 2).toLowerCase();
    if (c === actual) return;                       // su idioma preferido es el de esta página
    if (gemelas[c] && TEXTOS[c]) { destino = c; break; }
  }
  // Idioma que el sitio no tiene (japonés, polaco...): se ofrece el inglés, como el x-default de los hreflang.
  if (!destino && actual !== 'en' && gemelas.en) destino = 'en';
  if (!destino) return;

  var T = TEXTOS[destino];
  function crear() {
    var aviso = document.createElement('div');
    aviso.className = 'aviso-idioma';
    aviso.setAttribute('role', 'region');
    aviso.setAttribute('aria-label', T.aria);
    aviso.lang = destino;
    aviso.innerHTML =
      '<svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round">' +
      '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.5 2.6 3.8 5.6 3.8 9s-1.3 6.4-3.8 9c-2.5-2.6-3.8-5.6-3.8-9s1.3-6.4 3.8-9z"/></svg>' +
      '<p>' + T.texto + '</p>' +
      '<a class="boton" href="' + gemelas[destino] + '" hreflang="' + destino + '">' + T.ir + '</a>' +
      '<button type="button" class="aviso-idioma-cerrar" aria-label="' + T.cerrar + '">' +
      '<svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M6 6l12 12M18 6L6 18"/></svg></button>';
    aviso.querySelector('a').addEventListener('click', function () {
      guardar();
      // Para medir cuánto se usa (solo si la persona aceptó las cookies de Google Analytics).
      if (window.gtag) window.gtag('event', 'aviso_idioma', { desde: actual, hacia: destino, transport_type: 'beacon' });
    });
    aviso.querySelector('button').addEventListener('click', function () {
      guardar();
      // Animación propia (con "reducir movimiento" de Windows las de CSS no corren).
      var salida = aviso.animate && aviso.animate([{ opacity: 1, transform: 'none' }, { opacity: 0, transform: 'translateY(10px) scale(.97)' }],
        { duration: 200, easing: 'cubic-bezier(.4, 0, 1, 1)', fill: 'forwards' });
      if (salida) salida.onfinish = function () { aviso.remove(); }; else aviso.remove();
    });
    var pila = pilaAvisos();
    pila.insertBefore(aviso, pila.firstChild);
    if (aviso.animate) {
      aviso.animate([{ opacity: 0, transform: 'translateY(14px) scale(.97)' }, { opacity: 1, transform: 'none' }],
        { duration: 380, easing: 'cubic-bezier(.2, .8, .2, 1)' });
    }
  }
  // Igual que el de cookies: espera las fuentes para no cambiar de tamaño ya visible.
  var crearConFuentes = function () {
    var listas = document.fonts && document.fonts.ready;
    if (listas) listas.then(crear, crear); else crear();
  };
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', crearConFuentes);
  else crearConFuentes();
})();

// Selector de idioma del pie (está en todas las páginas, igual que este archivo): se cierra al tocar fuera o con
// Escape, y el menú entra con una animación propia, porque con "reducir movimiento" de Windows no anima nada solo.
(function () {
  document.querySelectorAll('.pie-idioma').forEach(function (d) {
    var menu = d.querySelector('ul');
    d.addEventListener('toggle', function () {
      if (d.open && menu && menu.animate) {
        menu.animate([{ opacity: 0, transform: 'translateY(8px) scale(.97)' }, { opacity: 1, transform: 'none' }],
          { duration: 220, easing: 'cubic-bezier(.2, .8, .2, 1)' });
      }
    });
    document.addEventListener('click', function (e) { if (d.open && !d.contains(e.target)) d.open = false; });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && d.open) { d.open = false; d.querySelector('summary').focus(); }
    });
  });
})();

// Descargar del pie: va directo a la tienda del equipo, con la misma detección que el botón principal de la portada
// (app.js): iPhone, iPad y Mac a la App Store, Windows a Microsoft Store y Android a los dos pasos de la prueba
// anticipada de Google Play (#android en la portada del idioma, como las insignias de las tiendas). Si no se reconoce
// el equipo, queda como está: baja a las tiendas (#tiendas).
(function () {
  var boton = document.querySelector('.pie-accion .boton');
  var logo = document.querySelector('.pie-logo');
  if (!boton || !logo) return;
  var ua = navigator.userAgent;
  var equipo = /iPad|iPhone|iPod|Macintosh/.test(ua) ? 'apple'
    : /Android/.test(ua) ? 'android'
    : (/Windows NT/.test(ua) && !/Mobile|Xbox/.test(ua)) ? 'windows' : null;
  var destino = {
    apple: 'https://apps.apple.com/app/id6834927348',
    windows: 'https://apps.microsoft.com/detail/9N3D7T1DP2SW?mode=direct',
    android: logo.getAttribute('href') + '#android'
  }[equipo];
  if (!destino) return;
  boton.href = destino;
  if (equipo !== 'android') { boton.target = '_blank'; boton.rel = 'noopener'; }
})();
