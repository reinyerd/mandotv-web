// Mando TV: elegir marca (cambia el color de toda la página) y tema del teléfono dibujado.
(function () {
  document.documentElement.classList.remove('sin-js');

  var marcas = {
    lg: { color: '#e0457b', tv: 'TV LG', nota: 'LG con webOS: se conecta en segundos y también lo enciende.' },
    samsung: { color: '#3d7bff', tv: 'TV Samsung', nota: 'Samsung con Tizen: aceptas una vez en el televisor y listo.' },
    roku: { color: '#a77bff', tv: 'Roku', nota: 'Roku: televisores y reproductores, sin emparejar nada.' },
    android: { color: '#2fbf8f', tv: 'Google TV', nota: 'Google TV y Android TV (Sony, TCL, Philips, Xiaomi y más): escribes el código que muestra la pantalla.' }
  };
  var orden = ['samsung', 'lg', 'roku', 'android'];
  var actual = 'samsung';
  var raiz = document.documentElement;
  var telefono = document.getElementById('telefono');
  var nombreTv = document.getElementById('app-tv');
  var nota = document.getElementById('marca-nota');
  var botones = document.querySelectorAll('[data-marca]');
  var tema = document.querySelector('meta[name="theme-color"]');

  // Decisión del fundador: la rotación de marcas y el cambio animado del teléfono funcionan siempre, aunque el sistema pida
  // reducir movimiento (son movimientos cortos y solo en el producto, igual que la flotación).
  var reducir = false;
  var pendiente = null;

  function aplicar(id) {
    var m = marcas[id];
    raiz.style.setProperty('--marca', m.color);
    if (tema) tema.setAttribute('content', m.color);
    nombreTv.textContent = m.tv;
    nota.textContent = m.nota;
  }

  // Cambio de marca como vitrina: el teléfono sale hacia un lado, cambian la marca y el color, y el nuevo entra
  // por el lado contrario. "Siguiente" (y la rotación automática) sale por la izquierda y entra por la derecha;
  // "Anterior" al revés, para que la dirección coincida con la flecha.
  var clases = ['sale-izq', 'sale-der', 'entra-der', 'entra-izq'];
  function elegir(id, haciaAtras) {
    if (!marcas[id] || id === actual) return;
    if (haciaAtras === undefined) haciaAtras = orden.indexOf(id) < orden.indexOf(actual);
    actual = id;
    botones.forEach(function (b) { b.setAttribute('aria-pressed', String(b.dataset.marca === id)); });
    if (reducir) { aplicar(id); return; }
    clearTimeout(pendiente);
    telefono.classList.remove.apply(telefono.classList, clases);
    void telefono.offsetWidth; // reinicia la animación
    telefono.classList.add(haciaAtras ? 'sale-der' : 'sale-izq');
    pendiente = setTimeout(function () {
      aplicar(id);
      telefono.classList.remove.apply(telefono.classList, clases);
      void telefono.offsetWidth;
      telefono.classList.add(haciaAtras ? 'entra-izq' : 'entra-der');
    }, 260);
  }

  // Muestra que sirve para todas las marcas: rota sola hasta que el visitante elige una.
  // Se pausa mientras el visitante mira o toca el teléfono o las marcas (mouse, dedo o teclado) y cuando el
  // teléfono no está a la vista (bajó por la página o cambió de pestaña); sigue sola al volver.
  var rotacion = null;
  var mirando = false;
  var aLaVista = true;
  function detenerRotacion() { if (rotacion) { clearInterval(rotacion); rotacion = null; } }
  if (!reducir) rotacion = setInterval(function () {
    if (mirando || !aLaVista || document.hidden) return;
    mover(1);
  }, 3500);
  [document.querySelector('.escaparate'), document.querySelector('.marcas')].forEach(function (zona) {
    if (!zona) return;
    zona.addEventListener('pointerenter', function () { mirando = true; });
    zona.addEventListener('pointerleave', function () { mirando = false; });
    zona.addEventListener('focusin', function () { mirando = true; });
    zona.addEventListener('focusout', function () { mirando = false; });
  });
  if ('IntersectionObserver' in window && document.querySelector('.escaparate')) {
    new IntersectionObserver(function (e) { aLaVista = e[0].isIntersecting; }, { threshold: 0.3 })
      .observe(document.querySelector('.escaparate'));
  }

  botones.forEach(function (b) { b.addEventListener('click', function () { detenerRotacion(); elegir(b.dataset.marca); }); });
  function mover(paso) { elegir(orden[(orden.indexOf(actual) + paso + orden.length) % orden.length], paso < 0); }
  document.getElementById('anterior').addEventListener('click', function () { detenerRotacion(); mover(-1); });
  document.getElementById('siguiente').addEventListener('click', function () { detenerRotacion(); mover(1); });

  // Botón principal "Descargar gratis": en Windows abre Microsoft Store; en los demás aparatos baja a las tiendas.
  var principal = document.getElementById('boton-principal');
  var ua = navigator.userAgent;
  if (principal && /Windows NT/.test(ua) && !/Mobile|Xbox/.test(ua)) {
    principal.href = 'https://apps.microsoft.com/detail/9N3D7T1DP2SW?mode=direct';
    principal.target = '_blank';
    principal.rel = 'noopener';
    document.getElementById('boton-principal-texto').textContent = 'Descargar gratis para Windows';
  }

  var nombreTema = document.getElementById('tema-nombre');
  document.querySelectorAll('[data-tema]').forEach(function (p) {
    p.addEventListener('click', function () {
      var claro = p.dataset.tema === 'claro';
      telefono.classList.toggle('claro', claro);
      nombreTema.textContent = claro ? 'Claro' : 'Oscuro';
      document.querySelectorAll('[data-tema]').forEach(function (o) { o.setAttribute('aria-pressed', String(o === p)); });
    });
  });


  // Inclinación 3D del teléfono siguiendo el mouse (solo con mouse; en pantallas táctiles queda el flotado).
  var escaparate = document.querySelector('.escaparate');
  var inclinador = document.getElementById('inclinador');
  if (escaparate && inclinador && window.matchMedia('(hover: hover) and (pointer: fine)').matches) {
    var reducido = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    var max = reducido ? 9 : 12; // grados
    var pendiente = null;
    escaparate.addEventListener('pointermove', function (e) {
      var r = escaparate.getBoundingClientRect();
      var x = (e.clientX - r.left) / r.width - 0.5;
      var y = (e.clientY - r.top) / r.height - 0.5;
      if (pendiente) cancelAnimationFrame(pendiente);
      pendiente = requestAnimationFrame(function () {
        inclinador.classList.add('siguiendo');
        inclinador.style.setProperty('--ry', (x * max * 2).toFixed(2) + 'deg');
        inclinador.style.setProperty('--rx', (-y * max * 1.4).toFixed(2) + 'deg');
      });
    });
    escaparate.addEventListener('pointerleave', function () {
      inclinador.classList.remove('siguiendo');
      inclinador.style.setProperty('--rx', '0deg');
      inclinador.style.setProperty('--ry', '0deg');
    });
  }

  // Demostración del teclado: escribe búsquedas letra por letra, las borra y escribe la siguiente.
  var textoTeclado = document.getElementById('texto-teclado');
  if (textoTeclado) {
    var frases = ['documentales de volcanes', 'música para cocinar', 'partido de fútbol en vivo', 'película de Navidad'];
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
      opciones.forEach(function (o, i) {
        o.className = i === elegida ? 'sel' : 'vidrio';
      });
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
