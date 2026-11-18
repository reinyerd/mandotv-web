// Enlaces de correo que funcionan en cualquier equipo.
// Un enlace "mailto:" no hace nada si el equipo no tiene app de correo configurada (muy común en Windows).
// Al pulsarlo mostramos un panel con: abrir Gmail, abrir la app de correo o copiar la dirección.
(function () {
  var panel, asunto, cuerpo, enlaceApp, enlaceGmail, aviso;
  // Textos por idioma (<html lang>): es por defecto; en, de, fr, pt e it con tabla propia.
  var TEXTOS = {
    es: { titulo: 'Escríbenos', es: 'Nuestro correo es', gmail: 'Abrir en Gmail', app: 'Abrir mi app de correo',
          copiar: 'Copiar dirección', cerrar: 'Cerrar', copiada: 'Dirección copiada. Pégala en tu correo.',
          copia: 'Copia la dirección: hola@mandotv.app', asunto: 'Hola Mando TV' },
    en: { titulo: 'Write to us', es: 'Our email is', gmail: 'Open in Gmail', app: 'Open my email app', copiar: 'Copy address',
          cerrar: 'Close', copiada: 'Address copied. Paste it into your email.', copia: 'Copy the address: hola@mandotv.app',
          asunto: 'Hello Mando TV' },
    de: { titulo: 'Schreib uns', es: 'Unsere E-Mail-Adresse ist', gmail: 'In Gmail öffnen', app: 'Meine E-Mail-App öffnen',
          copiar: 'Adresse kopieren', cerrar: 'Schließen', copiada: 'Adresse kopiert. Füge sie in deine E-Mail ein.',
          copia: 'Kopiere die Adresse: hola@mandotv.app', asunto: 'Hallo Mando TV' },
    fr: { titulo: 'Écrivez-nous', es: 'Notre adresse e-mail est', gmail: 'Ouvrir dans Gmail', app: 'Ouvrir mon application de messagerie',
          copiar: "Copier l'adresse", cerrar: 'Fermer', copiada: "Adresse copiée. Collez-la dans votre e-mail.",
          copia: "Copiez l'adresse : hola@mandotv.app", asunto: 'Bonjour Mando TV' },
    pt: { titulo: 'Escreva para a gente', es: 'Nosso e-mail é', gmail: 'Abrir no Gmail', app: 'Abrir meu app de e-mail',
          copiar: 'Copiar endereço', cerrar: 'Fechar', copiada: 'Endereço copiado. Cole no seu e-mail.',
          copia: 'Copie o endereço: hola@mandotv.app', asunto: 'Olá Mando TV' }
  };
  var T = TEXTOS[(document.documentElement.lang || '').slice(0, 2)] || TEXTOS.es;

  function crearPanel() {
    panel = document.createElement('dialog');
    panel.className = 'panel-correo';
    panel.setAttribute('aria-labelledby', 'panel-correo-titulo');
    panel.innerHTML =
      '<h2 id="panel-correo-titulo">' + T.titulo + '</h2>' +
      '<p>' + T.es + '</p>' +
      '<p class="panel-correo-dir">hola@mandotv.app</p>' +
      '<div class="panel-correo-acciones">' +
      '<a class="boton" id="pc-gmail" target="_blank" rel="noopener">' + T.gmail + '</a>' +
      '<a class="boton claro" id="pc-app">' + T.app + '</a>' +
      '<button type="button" class="boton claro" id="pc-copiar">' + T.copiar + '</button>' +
      '</div>' +
      '<p class="panel-correo-aviso" id="pc-aviso" aria-live="polite"></p>' +
      '<button type="button" class="panel-correo-cerrar" id="pc-cerrar" aria-label="' + T.cerrar + '">×</button>';
    document.body.appendChild(panel);
    enlaceGmail = panel.querySelector('#pc-gmail');
    enlaceApp = panel.querySelector('#pc-app');
    aviso = panel.querySelector('#pc-aviso');
    panel.querySelector('#pc-cerrar').addEventListener('click', function () { panel.close(); });
    panel.addEventListener('click', function (e) { if (e.target === panel) panel.close(); }); // clic fuera
    panel.querySelector('#pc-copiar').addEventListener('click', copiar);
  }

  function copiar() {
    var listo = function () { aviso.textContent = T.copiada; };
    if (navigator.clipboard && window.isSecureContext) {
      navigator.clipboard.writeText('hola@mandotv.app').then(listo, function () { aviso.textContent = T.copia; });
    } else {
      aviso.textContent = T.copia;
    }
  }

  function abrir(href) {
    if (!panel) crearPanel();
    var url = new URL(href);
    asunto = url.searchParams.get('subject') || T.asunto;
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
