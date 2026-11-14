// Aviso de cookies de Mando TV.
// Google Analytics (cookies) SOLO se carga si la persona pulsa "Aceptar". Sin respuesta o con "Rechazar"
// no se descarga nada de Google. La elección se guarda en este navegador y se puede cambiar con el
// botón "Cookies" del pie de página.
(function () {
  var ID_GA = 'G-2TDRY67ZJC';
  var CLAVE = 'mandotv-cookies'; // 'si' | 'no'
  var cargado = false;
  var aviso;

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
    aviso.setAttribute('aria-label', 'Aviso de cookies');
    aviso.innerHTML =
      '<p><b>¿Nos dejas contar tus visitas con cookies?</b> Usamos Google Analytics para saber qué páginas se leen ' +
      'y mejorar la web. Solo se activa si aceptas. <a href="/privacidad.html#cookies">Más información</a></p>' +
      '<div class="aviso-cookies-botones">' +
      '<button type="button" class="boton" data-eleccion="si">Aceptar</button>' +
      '<button type="button" class="boton" data-eleccion="no">Rechazar</button>' +
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
