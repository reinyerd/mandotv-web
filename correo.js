// Enlaces de correo que funcionan en cualquier equipo.
// Un enlace "mailto:" no hace nada si el equipo no tiene app de correo configurada (muy común en Windows).
// Al pulsarlo mostramos un panel con: abrir Gmail, abrir la app de correo o copiar la dirección.
(function () {
  var panel, asunto, cuerpo, enlaceApp, enlaceGmail, aviso;

  function crearPanel() {
    panel = document.createElement('dialog');
    panel.className = 'panel-correo';
    panel.setAttribute('aria-labelledby', 'panel-correo-titulo');
    panel.innerHTML =
      '<h2 id="panel-correo-titulo">Escríbenos</h2>' +
      '<p>Nuestro correo es</p>' +
      '<p class="panel-correo-dir">hola@mandotv.app</p>' +
      '<div class="panel-correo-acciones">' +
      '<a class="boton" id="pc-gmail" target="_blank" rel="noopener">Abrir en Gmail</a>' +
      '<a class="boton claro" id="pc-app">Abrir mi app de correo</a>' +
      '<button type="button" class="boton claro" id="pc-copiar">Copiar dirección</button>' +
      '</div>' +
      '<p class="panel-correo-aviso" id="pc-aviso" aria-live="polite"></p>' +
      '<button type="button" class="panel-correo-cerrar" id="pc-cerrar" aria-label="Cerrar">×</button>';
    document.body.appendChild(panel);
    enlaceGmail = panel.querySelector('#pc-gmail');
    enlaceApp = panel.querySelector('#pc-app');
    aviso = panel.querySelector('#pc-aviso');
    panel.querySelector('#pc-cerrar').addEventListener('click', function () { panel.close(); });
    panel.addEventListener('click', function (e) { if (e.target === panel) panel.close(); }); // clic fuera
    panel.querySelector('#pc-copiar').addEventListener('click', copiar);
  }

  function copiar() {
    var listo = function () { aviso.textContent = 'Dirección copiada. Pégala en tu correo.'; };
    if (navigator.clipboard && window.isSecureContext) {
      navigator.clipboard.writeText('hola@mandotv.app').then(listo, function () { aviso.textContent = 'Copia la dirección: hola@mandotv.app'; });
    } else {
      aviso.textContent = 'Copia la dirección: hola@mandotv.app';
    }
  }

  function abrir(href) {
    if (!panel) crearPanel();
    var url = new URL(href);
    asunto = url.searchParams.get('subject') || 'Hola Mando TV';
    cuerpo = url.searchParams.get('body') || '';
    enlaceApp.href = href;
    enlaceGmail.href = 'https://mail.google.com/mail/?view=cm&fs=1&to=hola@mandotv.app&su=' +
      encodeURIComponent(asunto) + '&body=' + encodeURIComponent(cuerpo);
    aviso.textContent = '';
    panel.showModal();
  }

  if (typeof HTMLDialogElement !== 'function') return; // navegador antiguo: queda el enlace normal
  document.addEventListener('click', function (e) {
    var a = e.target.closest && e.target.closest('a[href^="mailto:"]');
    if (!a || a.id === 'pc-app') return;
    e.preventDefault();
    abrir(a.href);
  });
})();
