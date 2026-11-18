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
          url: '/privacidad.html#cookies', mas: 'Más información', si: 'Aceptar', no: 'Rechazar' },
    en: { aria: 'Cookie notice', titulo: 'Can we count your visits with cookies?',
          texto: 'We use Google Analytics to see which pages are read and improve the site. It only turns on if you accept.',
          url: '/en/privacy.html#cookies', mas: 'Learn more', si: 'Accept', no: 'Decline' },
    de: { aria: 'Cookie-Hinweis', titulo: 'Dürfen wir deine Besuche mit Cookies zählen?',
          texto: 'Wir nutzen Google Analytics, um zu sehen, welche Seiten gelesen werden, und die Website zu verbessern. Es wird nur aktiviert, wenn du akzeptierst.',
          url: '/de/datenschutz.html#cookies', mas: 'Mehr erfahren', si: 'Akzeptieren', no: 'Ablehnen' },
    fr: { aria: 'Avis sur les cookies', titulo: 'Pouvons-nous compter vos visites avec des cookies ?',
          texto: "Nous utilisons Google Analytics pour savoir quelles pages sont lues et améliorer le site. Il ne s'active que si vous acceptez.",
          url: '/fr/confidentialite.html#cookies', mas: 'En savoir plus', si: 'Accepter', no: 'Refuser' },
    pt: { aria: 'Aviso de cookies', titulo: 'Você deixa a gente contar as suas visitas com cookies?',
          texto: 'Usamos o Google Analytics para saber quais páginas são lidas e melhorar o site. Ele só é ativado se você aceitar.',
          url: '/pt/privacidade.html#cookies', mas: 'Saiba mais', si: 'Aceitar', no: 'Recusar' }
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
    document.body.appendChild(aviso);
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
    if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', function () { crearAviso(); });
    else crearAviso();
  }
})();
