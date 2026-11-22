// Mando TV: vitrina del inicio. Elegir marca de TV (cambia el color de toda la página), elegir equipo (el botón
// Descargar va a la tienda correcta), tema del teléfono dibujado y teclas que responden al toque.
(function () {
  document.documentElement.classList.remove('sin-js');

  var marcas = {
    samsung: { color: '#3d7bff', color2: '#43d3ff', tv: 'TV Samsung', nota: 'Samsung con Tizen: aceptas una vez en el televisor y listo.' },
    lg: { color: '#e0457b', color2: '#ff9a62', tv: 'TV LG', nota: 'LG con webOS: se conecta por WiFi y también puede encenderlo.' },
    roku: { color: '#a77bff', color2: '#ff7be5', tv: 'Roku', nota: 'Roku: televisores y reproductores, sin emparejar nada.' },
    android: { color: '#2fbf8f', color2: '#c4f04f', tv: 'Google TV', nota: 'Google TV y Android TV (Sony, TCL, Philips, Xiaomi y más): escribes el código que muestra la pantalla.' }
  };
  // Textos en español (página raíz). Las páginas en otros idiomas (/en/, /de/, /fr/, /pt/, /it/) toman los suyos de
  // TEXTOS según <html lang>.
  var ES = {
    mac: 'Descargar gratis para Mac', ipad: 'Descargar gratis para iPad', iphone: 'Descargar gratis para iPhone', windows: 'Descargar gratis para Windows',
    android: 'Descargar gratis para Android', boton: 'Descargar gratis',
    notaAndroid: 'En Android es una prueba anticipada en Google Play: son dos pasos.',
    barra: 'Descargar', claro: 'Claro', oscuro: 'Oscuro', pausar: 'Pausar las marcas', reanudar: 'Reanudar las marcas',
    frases: ['documentales de volcanes', 'música para cocinar', 'partido de fútbol en vivo', 'película de Navidad']
  };
  var TEXTOS = {
    en: {
      marcas: {
        lg: ['LG TV', 'LG with webOS: it connects over Wi-Fi and can also turn the TV on.'],
        samsung: ['Samsung TV', 'Samsung with Tizen: you accept once on the TV and you are set.'],
        roku: ['Roku', 'Roku: TVs and players, nothing to pair.'],
        android: ['Google TV', 'Google TV and Android TV (Sony, TCL, Philips, Xiaomi and more): you type the code the screen shows.']
      },
      mac: 'Download free for Mac', ipad: 'Download free for iPad', iphone: 'Download free for iPhone', windows: 'Download free for Windows',
      android: 'Download free for Android', boton: 'Download free',
      notaAndroid: "On Android it's early access on Google Play: two quick steps.",
      barra: 'Download', claro: 'Light', oscuro: 'Dark', pausar: 'Pause the brands', reanudar: 'Play the brands',
      frases: ['volcano documentaries', 'cooking music', 'live soccer game', 'Christmas movie']
    },
    de: {
      marcas: {
        lg: ['LG Fernseher', 'LG mit webOS: Die Verbindung läuft über WLAN und er lässt sich auch einschalten.'],
        samsung: ['Samsung Fernseher', 'Samsung mit Tizen: Du bestätigst einmal am Fernseher und bist fertig.'],
        roku: ['Roku', 'Roku: Fernseher und Player, ohne etwas zu koppeln.'],
        android: ['Google TV', 'Google TV und Android TV (Sony, TCL, Philips, Xiaomi und mehr): Du gibst den Code ein, den der Bildschirm zeigt.']
      },
      mac: 'Kostenlos für Mac laden', ipad: 'Kostenlos für iPad laden', iphone: 'Kostenlos für iPhone laden', windows: 'Kostenlos für Windows laden',
      android: 'Kostenlos für Android laden', boton: 'Kostenlos laden',
      notaAndroid: 'Auf Android gibt es einen frühen Zugang über Google Play: zwei Schritte.',
      barra: 'Laden', claro: 'Hell', oscuro: 'Dunkel', pausar: 'Marken anhalten', reanudar: 'Marken fortsetzen',
      frases: ['Dokumentationen über Vulkane', 'Musik zum Kochen', 'Fußballspiel live', 'Weihnachtsfilm']
    },
    fr: {
      marcas: {
        lg: ['TV LG', 'LG avec webOS : la connexion passe par le Wi-Fi et elle peut aussi allumer la TV.'],
        samsung: ['TV Samsung', "Samsung avec Tizen : vous acceptez une fois sur la TV et c'est terminé."],
        roku: ['Roku', 'Roku : téléviseurs et lecteurs, rien à associer.'],
        android: ['Google TV', "Google TV et Android TV (Sony, TCL, Philips, Xiaomi et plus) : vous saisissez le code affiché à l'écran."]
      },
      mac: 'Télécharger gratuitement pour Mac', ipad: 'Télécharger gratuitement pour iPad', iphone: 'Télécharger gratuitement pour iPhone', windows: 'Télécharger gratuitement pour Windows',
      android: 'Télécharger gratuitement pour Android', boton: 'Télécharger gratuitement',
      notaAndroid: "Sur Android, c'est un accès anticipé sur Google Play : deux étapes.",
      barra: 'Télécharger', claro: 'Clair', oscuro: 'Sombre', pausar: 'Mettre les marques en pause', reanudar: 'Relancer les marques',
      frases: ['documentaires sur les volcans', 'musique pour cuisiner', 'match de foot en direct', 'film de Noël']
    },
    pt: {
      marcas: {
        lg: ['TV LG', 'LG com webOS: conecta pelo Wi-Fi e também pode ligar a TV.'],
        samsung: ['TV Samsung', 'Samsung com Tizen: você aceita uma vez na TV e pronto.'],
        roku: ['Roku', 'Roku: TVs e aparelhos, sem precisar parear nada.'],
        android: ['Google TV', 'Google TV e Android TV (Sony, TCL, Philips, Xiaomi e outras): você digita o código que aparece na tela.']
      },
      mac: 'Baixar grátis para Mac', ipad: 'Baixar grátis para iPad', iphone: 'Baixar grátis para iPhone', windows: 'Baixar grátis para Windows',
      android: 'Baixar grátis para Android', boton: 'Baixar grátis',
      notaAndroid: 'No Android é um teste antecipado no Google Play: são dois passos.',
      barra: 'Baixar', claro: 'Claro', oscuro: 'Escuro', pausar: 'Pausar as marcas', reanudar: 'Retomar as marcas',
      frases: ['documentários sobre vulcões', 'música para cozinhar', 'jogo de futebol ao vivo', 'filme de Natal']
    },
    it: {
      marcas: {
        lg: ['TV LG', 'LG con webOS: si collega in Wi-Fi e può anche accendere la TV.'],
        samsung: ['TV Samsung', 'Samsung con Tizen: accetti una volta sulla TV e hai finito.'],
        roku: ['Roku', 'Roku: televisori e dispositivi, senza nulla da associare.'],
        android: ['Google TV', 'Google TV e Android TV (Sony, TCL, Philips, Xiaomi e altre): inserisci il codice che compare sullo schermo.']
      },
      mac: 'Scarica gratis per Mac', ipad: 'Scarica gratis per iPad', iphone: 'Scarica gratis per iPhone', windows: 'Scarica gratis per Windows',
      android: 'Scarica gratis per Android', boton: 'Scarica gratis',
      notaAndroid: 'Su Android è un accesso anticipato su Google Play: bastano due passaggi.',
      barra: 'Scarica', claro: 'Chiaro', oscuro: 'Scuro', pausar: 'Metti in pausa le marche', reanudar: 'Riprendi le marche',
      frases: ['documentari sui vulcani', 'musica per cucinare', 'partita di calcio in diretta', 'film di Natale']
    }
  };
  var T = TEXTOS[(document.documentElement.lang || '').slice(0, 2)] || ES;
  if (T.marcas) {
    Object.keys(T.marcas).forEach(function (k) { marcas[k].tv = T.marcas[k][0]; marcas[k].nota = T.marcas[k][1]; });
  }
  var raiz = document.documentElement;
  var telefono = document.getElementById('telefono');
  if (!telefono) return;
  var orden = ['samsung', 'lg', 'roku', 'android'];
  var actual = 'samsung';
  var nombreTv = document.getElementById('app-tv');
  var nota = document.getElementById('marca-nota');
  var botones = document.querySelectorAll('[data-marca]');
  var tema = document.querySelector('meta[name="theme-color"]');
  var gigante = document.querySelector('.gigante');
  var vitrina = document.querySelector('.vitrina');
  var num = document.getElementById('vitrina-num');
  var nombreVitrina = document.getElementById('vitrina-nombre');
  var barras = document.querySelectorAll('.vitrina-barras i');
  var nombres = {};
  botones.forEach(function (b) { nombres[b.dataset.marca] = b.textContent.trim(); });

  function aplicar(id, porUsuario) {
    var m = marcas[id];
    raiz.style.setProperty('--marca', m.color);
    raiz.style.setProperty('--marca-2', m.color2);
    if (tema) tema.setAttribute('content', m.color);
    nombreTv.textContent = m.tv;
    // Solo se anuncia a los lectores de pantalla cuando la persona elige; la rotación sola no interrumpe.
    nota.setAttribute('aria-live', porUsuario ? 'polite' : 'off');
    nota.textContent = m.nota;
    var i = orden.indexOf(id);
    if (num) num.textContent = '0' + (i + 1);
    if (nombreVitrina) nombreVitrina.textContent = nombres[id] || m.tv;
  }

  // Avance de la rotación: la barra de la marca actual se llena en el tiempo de cada vuelta.
  // Se reinicia en el cuadro siguiente (sin forzar un cálculo de diseño con offsetWidth).
  function marcarBarras() {
    var i = orden.indexOf(actual);
    barras.forEach(function (b, k) {
      b.classList.remove('activa');
      b.classList.toggle('vista', k < i);
    });
    if (barras[i]) requestAnimationFrame(function () { requestAnimationFrame(function () { barras[i].classList.add('activa'); }); });
  }

  // Cambio de marca como vitrina: el teléfono sale hacia un lado, cambian la marca y el color, y el nuevo entra por
  // el lado contrario ("Siguiente" y la rotación salen por la izquierda; "Anterior" al revés).
  var clases = ['sale-izq', 'sale-der', 'entra-der', 'entra-izq'];
  var cambio = null;
  function elegir(id, haciaAtras, porUsuario) {
    if (!marcas[id] || id === actual) return;
    if (haciaAtras === undefined) haciaAtras = orden.indexOf(id) < orden.indexOf(actual);
    actual = id;
    botones.forEach(function (b) { b.setAttribute('aria-pressed', String(b.dataset.marca === id)); });
    marcarBarras();
    clearTimeout(cambio);
    telefono.classList.remove.apply(telefono.classList, clases);
    void telefono.offsetWidth; // reinicia la animación
    telefono.classList.add(haciaAtras ? 'sale-der' : 'sale-izq');
    cambio = setTimeout(function () {
      aplicar(id, porUsuario);
      telefono.classList.remove.apply(telefono.classList, clases);
      void telefono.offsetWidth;
      telefono.classList.add(haciaAtras ? 'entra-izq' : 'entra-der');
      // La palabra gigante se desliza un poco en la misma dirección.
      if (gigante && gigante.animate) {
        gigante.animate([
          { transform: 'translateY(-50%) translateX(' + (haciaAtras ? '-6%' : '6%') + ')', opacity: 0 },
          { transform: 'translateY(-50%) translateX(0)', opacity: 1 }
        ], { duration: 620, easing: 'cubic-bezier(.23, 1, .32, 1)' });
      }
    }, 260);
  }
  function mover(paso, porUsuario) { elegir(orden[(orden.indexOf(actual) + paso + orden.length) % orden.length], paso < 0, porUsuario); }

  // Rotación sola, para mostrar que sirve con todas las marcas. Se pausa mientras la persona mira o toca la vitrina
  // (mouse, dedo o teclado), si el teléfono no está a la vista o la pestaña está oculta; el botón de pausa la detiene.
  // Sigue con "reducir movimiento" (decisión del fundador: es el producto).
  var VUELTA = 3500, restante = VUELTA, inicio = 0, temporizador = null;
  var detenida = false, mirando = false, aLaVista = true;
  var pausa = document.getElementById('pausa');
  if (vitrina) vitrina.style.setProperty('--vuelta', VUELTA + 'ms');
  function enPausa() { return detenida || mirando || !aLaVista || document.hidden; }
  function actualizar() {
    if (enPausa()) {
      if (temporizador) { clearTimeout(temporizador); temporizador = null; restante = Math.max(0, restante - (performance.now() - inicio)); }
      if (vitrina) vitrina.classList.add('en-pausa');
      return;
    }
    if (vitrina) vitrina.classList.remove('en-pausa');
    if (temporizador) return;
    inicio = performance.now();
    temporizador = setTimeout(function () {
      temporizador = null; restante = VUELTA;
      mover(1, false);
      actualizar();
    }, restante);
  }
  function ponerPausa(si) {
    detenida = si;
    if (vitrina) vitrina.classList.toggle('quieta', si);
    if (pausa) {
      pausa.dataset.estado = si ? 'pausa' : 'gira';
      pausa.setAttribute('aria-label', si ? T.reanudar : T.pausar);
    }
    if (!si) { restante = VUELTA; marcarBarras(); }
    actualizar();
  }
  if (pausa) {
    pausa.setAttribute('aria-label', T.pausar);
    pausa.addEventListener('click', function () { ponerPausa(!detenida); });
  }
  // Con el mouse se pausa sobre el teléfono y los selectores; con el teclado, mientras el foco esté en cualquier parte
  // del hero (WCAG 2.2.2: el color no cambia mientras la persona recorre la ficha).
  var conMouse = false, conFoco = false;
  [document.querySelector('.escaparate'), document.querySelector('.marcas'), document.querySelector('.equipos')].forEach(function (zona) {
    if (!zona) return;
    zona.addEventListener('pointerenter', function (e) { if (e.pointerType === 'mouse') { conMouse = true; mirando = true; actualizar(); } });
    zona.addEventListener('pointerleave', function (e) { if (e.pointerType === 'mouse') { conMouse = false; mirando = conFoco; actualizar(); } });
  });
  var panel = document.querySelector('.panel');
  if (panel) {
    panel.addEventListener('focusin', function () { conFoco = true; mirando = true; actualizar(); });
    panel.addEventListener('focusout', function (e) {
      if (panel.contains(e.relatedTarget)) return;
      conFoco = false; mirando = conMouse; actualizar();
    });
  }
  if ('IntersectionObserver' in window && document.querySelector('.escaparate')) {
    new IntersectionObserver(function (e) { aLaVista = e[0].isIntersecting; actualizar(); }, { threshold: 0.3 })
      .observe(document.querySelector('.escaparate'));
  }
  document.addEventListener('visibilitychange', actualizar);

  botones.forEach(function (b) { b.addEventListener('click', function () { ponerPausa(true); elegir(b.dataset.marca, undefined, true); }); });
  document.getElementById('anterior').addEventListener('click', function () { ponerPausa(true); mover(-1, true); });
  document.getElementById('siguiente').addEventListener('click', function () { ponerPausa(true); mover(1, true); });
  // Puntos de color bajo el teléfono: tocar uno elige esa marca (las flechas y la pausa siguen para el teclado).
  barras.forEach(function (b, k) { b.addEventListener('click', function () { ponerPausa(true); elegir(orden[k], undefined, true); }); });
  marcarBarras();
  actualizar();

  // Tu equipo: iPhone, iPad, Android o Windows. El botón Descargar va directo a su tienda (Android, en prueba
  // anticipada, baja a los dos pasos para unirse). Se elige sola según el aparato.
  var principal = document.getElementById('boton-principal');
  var textoPrincipal = document.getElementById('boton-principal-texto');
  var notaBoton = document.getElementById('boton-nota');
  var APPLE = 'https://apps.apple.com/app/id6834927348';
  var MICROSOFT = 'https://apps.microsoft.com/detail/9N3D7T1DP2SW?mode=direct';
  var destinos = { iphone: APPLE, ipad: APPLE, mac: APPLE, windows: MICROSOFT, android: '#android' };
  var equipos = document.querySelectorAll('[data-equipo]');
  function elegirEquipo(id) {
    equipos.forEach(function (b) { b.setAttribute('aria-pressed', String(b.dataset.equipo === id)); });
    if (!principal) return;
    var externo = destinos[id] && destinos[id].charAt(0) !== '#';
    principal.href = destinos[id] || '#tiendas';
    if (externo) { principal.target = '_blank'; principal.rel = 'noopener'; }
    else { principal.removeAttribute('target'); principal.removeAttribute('rel'); }
    textoPrincipal.textContent = T[id] || T.boton;
    if (notaBoton) {
      notaBoton.textContent = id === 'android' ? T.notaAndroid : '';
      notaBoton.hidden = id !== 'android';
    }
    sincronizarBarra();
  }
  equipos.forEach(function (b) { b.addEventListener('click', function () { elegirEquipo(b.dataset.equipo); }); });
  var ua = navigator.userAgent;
  var esIpad = /iPad/.test(ua) || (/Macintosh/.test(ua) && navigator.maxTouchPoints > 1);
  var inicial = esIpad ? 'ipad'
    : /iPhone|iPod/.test(ua) ? 'iphone'
    : /Android/.test(ua) ? 'android'
    : (/Windows NT/.test(ua) && !/Mobile|Xbox/.test(ua)) ? 'windows'
    : /Macintosh/.test(ua) ? 'mac' : null;
  // Barra fija al bajar (estilo Apple): logo y Descargar siempre a mano, con el mismo destino que el botón principal.
  // Mientras no se ve queda inerte para que el teclado no llegue a enlaces ocultos.
  var barraFija = null, barraDescargar = null;
  function sincronizarBarra() {
    if (!barraDescargar || !principal) return;
    barraDescargar.href = principal.getAttribute('href');
    ['target', 'rel'].forEach(function (a) {
      if (principal.hasAttribute(a)) barraDescargar.setAttribute(a, principal.getAttribute(a));
      else barraDescargar.removeAttribute(a);
    });
  }
  var portada = document.querySelector('.escena');
  if (principal && portada && 'IntersectionObserver' in window) {
    barraFija = document.createElement('div');
    barraFija.className = 'barra-fija';
    barraFija.setAttribute('inert', '');
    var logoFijo = document.createElement('a');
    logoFijo.className = 'logo';
    logoFijo.href = '#inicio';
    var iconoFijo = document.createElement('img');
    iconoFijo.src = '/icono.svg';
    iconoFijo.alt = '';
    iconoFijo.width = 26;
    iconoFijo.height = 26;
    logoFijo.appendChild(iconoFijo);
    logoFijo.appendChild(document.createTextNode('Mando TV'));
    barraDescargar = document.createElement('a');
    barraDescargar.className = 'boton';
    barraDescargar.id = 'barra-descargar';
    barraDescargar.textContent = T.barra;
    barraFija.appendChild(logoFijo);
    barraFija.appendChild(barraDescargar);
    document.body.appendChild(barraFija);
    new IntersectionObserver(function (e) {
      var fuera = !e[0].isIntersecting;
      barraFija.classList.toggle('visible', fuera);
      if (fuera) barraFija.removeAttribute('inert'); else barraFija.setAttribute('inert', '');
    }).observe(portada);
  }
  if (inicial) elegirEquipo(inicial);
  sincronizarBarra();

  var nombreTema = document.getElementById('tema-nombre');
  document.querySelectorAll('[data-tema]').forEach(function (p) {
    p.addEventListener('click', function () {
      var claro = p.dataset.tema === 'claro';
      telefono.classList.toggle('claro', claro);
      if (nombreTema) nombreTema.textContent = claro ? T.claro : T.oscuro;
      document.querySelectorAll('[data-tema]').forEach(function (o) { o.setAttribute('aria-pressed', String(o === p)); });
    });
  });

  // Teclas del teléfono dibujado: responden al toque y muestran qué se envió al TV (demostración, como en la app).
  var escaparate = document.querySelector('.escaparate');
  // La etiqueta solo aparece al tocar una tecla (antes había una pista fija, "Toca los botones", que tapaba el
  // teléfono: pedido del fundador). Para invitar a tocar, el OK late dos veces al cargar y nada más.
  var chip = document.createElement('span');
  chip.className = 'toque';
  chip.setAttribute('aria-hidden', 'true');
  if (escaparate) escaparate.appendChild(chip);
  var tocado = false;
  var okInvita = telefono.querySelector('.ok');
  if (okInvita && okInvita.animate) {
    setTimeout(function () {
      if (tocado) return;
      okInvita.animate([{ transform: 'scale(1)' }, { transform: 'scale(1.14)' }, { transform: 'scale(1)' }],
        { duration: 650, iterations: 2, delay: 0, easing: 'cubic-bezier(.45, 0, .55, 1)' });
    }, 1400);
  }
  var FLECHAS = { arriba: '▲', abajo: '▼', izq: '◀', der: '▶' };
  function etiquetaDe(el, e) {
    if (el.classList.contains('cruceta')) {
      var r = el.getBoundingClientRect();
      var x = e.clientX - (r.left + r.width / 2), y = e.clientY - (r.top + r.height / 2);
      if (Math.hypot(x, y) < r.width * 0.2) return { el: el.querySelector('.ok'), txt: 'OK' };
      var lado = Math.abs(x) > Math.abs(y) ? (x > 0 ? 'der' : 'izq') : (y > 0 ? 'abajo' : 'arriba');
      return { el: el.querySelector('.' + lado), txt: FLECHAS[lado] };
    }
    if (el.classList.contains('balancin')) {
      var rb = el.getBoundingClientRect();
      var arriba = e.clientY < rb.top + rb.height / 2;
      var bs = el.querySelectorAll('b');
      return { el: arriba ? bs[0] : bs[1], txt: el.querySelector('small').textContent + (arriba ? ' +' : ' −') };
    }
    var s = el.querySelector('span');
    return { el: el, txt: (s ? s.textContent : el.textContent).trim() };
  }
  var ocultar = null;
  telefono.addEventListener('pointerdown', function (e) {
    var el = e.target.closest('.cruceta, .balancin, .tecla, .pestanas span');
    if (!el) return;
    var t = etiquetaDe(el, e);
    if (!t.el) return;
    t.el.classList.add('pulsada');
    setTimeout(function () { t.el.classList.remove('pulsada'); }, 160);
    tocado = true;
    chip.textContent = t.txt;
    // Vibra solo si el navegador ya registró un toque real (si no, Chrome bloquea la llamada y deja un error en la consola).
    var activo = !navigator.userActivation || navigator.userActivation.hasBeenActive;
    if (navigator.vibrate && activo) { try { navigator.vibrate(8); } catch (err) { /* sin vibración */ } }
    if (chip.animate) {
      chip.animate([{ opacity: 0, transform: 'translateY(6px) scale(.96)' }, { opacity: 1, transform: 'none' }],
        { duration: 180, easing: 'cubic-bezier(.23, 1, .32, 1)', fill: 'both' });
      clearTimeout(ocultar);
      ocultar = setTimeout(function () {
        chip.animate([{ opacity: 1 }, { opacity: 0 }], { duration: 200, easing: 'ease-out', fill: 'both' });
      }, 900);
    }
  });

  // Inclinación 3D del teléfono siguiendo el mouse (solo con mouse; en pantallas táctiles queda el flotado).
  var inclinador = document.getElementById('inclinador');
  if (escaparate && inclinador && window.matchMedia('(hover: hover) and (pointer: fine)').matches) {
    var max = 12; // grados
    var cuadro = null;
    escaparate.addEventListener('pointermove', function (e) {
      var r = escaparate.getBoundingClientRect();
      var x = (e.clientX - r.left) / r.width - 0.5;
      var y = (e.clientY - r.top) / r.height - 0.5;
      if (cuadro) cancelAnimationFrame(cuadro);
      cuadro = requestAnimationFrame(function () {
        inclinador.classList.add('siguiendo');
        inclinador.style.transform = 'rotateX(' + (-y * max * 1.4).toFixed(2) + 'deg) rotateY(' + (x * max * 2).toFixed(2) + 'deg)';
      });
    });
    escaparate.addEventListener('pointerleave', function () {
      inclinador.classList.remove('siguiendo');
      inclinador.style.transform = '';
    });
  }

  // Banda de marcas: se mueve con la Web Animations API, que funciona aunque Windows tenga los efectos desactivados
  // (decisión del fundador); con el mouse encima se detiene para poder leerla.
  var pista = document.querySelector('.banda-pista');
  if (pista && pista.animate) {
    var giro = pista.animate([{ transform: 'translateX(0)' }, { transform: 'translateX(-50%)' }],
      { duration: 46000, iterations: Infinity, easing: 'linear' });
    if (window.matchMedia('(hover: hover) and (pointer: fine)').matches) {
      pista.addEventListener('pointerenter', function () { giro.pause(); });
      pista.addEventListener('pointerleave', function () { giro.play(); });
    }
  }

  // Demostración del teclado: escribe búsquedas letra por letra, las borra y escribe la siguiente.
  var textoTeclado = document.getElementById('texto-teclado');
  if (textoTeclado) {
    var frases = T.frases;
    var f = 0, n = frases[0].length, borrando = true;
    (function escribir() {
      var frase = frases[f];
      if (borrando) {
        n--;
        if (n <= 0) { borrando = false; f = (f + 1) % frases.length; frase = frases[f]; }
      } else {
        n++;
        if (n >= frase.length) { borrando = true; textoTeclado.textContent = frase; setTimeout(escribir, 2200); return; }
      }
      textoTeclado.textContent = frase.slice(0, Math.max(n, 0));
      setTimeout(escribir, borrando ? 35 : 75);
    })();
  }

  // Demostración de entradas: va cambiando sola entre TV en vivo, HDMI 1 y HDMI 2.
  var entradasDemo = document.getElementById('entradas-demo');
  if (entradasDemo) {
    var opciones = entradasDemo.querySelectorAll('span');
    var elegida = 1;
    setInterval(function () {
      elegida = (elegida + 1) % opciones.length;
      opciones.forEach(function (o, i) { o.className = i === elegida ? 'sel' : 'vidrio'; });
    }, 1800);
  }

  // Entrada escalonada de cada sección al aparecer en pantalla.
  var piezas = document.querySelectorAll('.aparece');
  if (!('IntersectionObserver' in window)) {
    piezas.forEach(function (el) { el.classList.add('visible'); });
    return;
  }
  var obs = new IntersectionObserver(function (entradas) {
    entradas.forEach(function (e) {
      if (!e.isIntersecting) return;
      var hermanos = Array.prototype.filter.call(e.target.parentNode.children, function (h) { return h.classList.contains('aparece'); });
      e.target.style.transitionDelay = Math.min(hermanos.indexOf(e.target), 6) * 70 + 'ms';
      e.target.classList.add('visible');
      obs.unobserve(e.target);
    });
  }, { rootMargin: '0px 0px -8% 0px' });
  piezas.forEach(function (el) { obs.observe(el); });
})();
