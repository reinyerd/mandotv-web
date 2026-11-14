// Mando TV: elegir marca (cambia el color de toda la página) y tema del teléfono dibujado.
(function () {
  document.documentElement.classList.remove('sin-js');

  var marcas = {
    lg: { color: '#e0457b', tv: 'TV LG', nota: 'LG con webOS: se conecta en segundos y también lo enciende.' },
    samsung: { color: '#3d7bff', tv: 'TV Samsung', nota: 'Samsung con Tizen: aceptas una vez en el televisor y listo.' },
    roku: { color: '#a77bff', tv: 'Roku', nota: 'Roku: televisores y reproductores, sin emparejar nada.' },
    android: { color: '#2fbf8f', tv: 'Android TV', nota: 'Android TV y Google TV: escribes el código que muestra la pantalla.' }
  };
  var orden = ['lg', 'samsung', 'roku', 'android'];
  var actual = 'lg';
  var raiz = document.documentElement;
  var telefono = document.getElementById('telefono');
  var nombreTv = document.getElementById('app-tv');
  var nota = document.getElementById('marca-nota');
  var botones = document.querySelectorAll('[data-marca]');
  var tema = document.querySelector('meta[name="theme-color"]');

  function elegir(id) {
    if (!marcas[id] || id === actual) return;
    actual = id;
    var m = marcas[id];
    raiz.style.setProperty('--marca', m.color);
    if (tema) tema.setAttribute('content', m.color);
    nombreTv.textContent = m.tv;
    nota.textContent = m.nota;
    botones.forEach(function (b) { b.setAttribute('aria-pressed', String(b.dataset.marca === id)); });
    telefono.classList.remove('cambiando');
    void telefono.offsetWidth; // reinicia la animación
    telefono.classList.add('cambiando');
  }

  botones.forEach(function (b) { b.addEventListener('click', function () { elegir(b.dataset.marca); }); });
  function mover(paso) { elegir(orden[(orden.indexOf(actual) + paso + orden.length) % orden.length]); }
  document.getElementById('anterior').addEventListener('click', function () { mover(-1); });
  document.getElementById('siguiente').addEventListener('click', function () { mover(1); });

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
    var max = reducido ? 4 : 12; // grados
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
