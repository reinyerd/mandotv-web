// Demo de "See it in action" (portada en inglés): la interfaz real de la app en modo Moderno, como se ve en Windows.
// Un dedo sube el volumen de 9 a 11 y lo baja, pulsa las flechas y el OK, y abre Inputs para elegir HDMI 1.
// Todo se mueve con la Web Animations API (en Windows "reducir movimiento" viene activo y la demo igual debe verse).
// Se detiene con su botón (WCAG 2.2.2) y sola cuando sale de la pantalla; solo anima transform, opacity y filter.
(function () {
  var raiz = document.querySelector('[data-demo]');
  if (!raiz || !raiz.animate || !raiz.getAnimations || !window.IntersectionObserver) return;
  var $ = function (s) { return raiz.querySelector(s); };
  var d = function (k) { return raiz.querySelector('[data-d="' + k + '"]'); };
  var lienzo = $('.demo-pantalla'), dedo = $('.demo-dedo'), yema = $('.demo-dedo i'), num = $('.demo-num');
  var hoja = $('.demo-hoja'), velo = $('.demo-velo'), reloj = $('.demo-reloj'), boton = $('.demo-pausa');
  var pasos = raiz.querySelectorAll('[data-paso]');
  var SUAVE = 'cubic-bezier(.23, 1, .32, 1)';
  var x = 0, y = 0, barra = null, pausadoPorUsuario = false, visible = false, corriendo = false;

  // Fija el estado final en el elemento y suelta la animación (así no se acumulan vuelta tras vuelta).
  function fijar(a) { return a.finished.then(function () { a.commitStyles(); a.cancel(); }); }
  // Las esperas también son animaciones: al pausar, la demo entera se detiene en el mismo punto.
  function espera(ms) { return reloj.animate([{ opacity: 0 }, { opacity: 0 }], { duration: ms }).finished; }
  function centro(el) {
    var a = el.getBoundingClientRect(), b = lienzo.getBoundingClientRect();
    return [a.left - b.left + a.width / 2, a.top - b.top + a.height / 2];
  }
  function ir(el, ms) {
    var desde = 'translate(' + x + 'px, ' + y + 'px)', c = centro(el);
    x = c[0]; y = c[1];
    return fijar(dedo.animate([{ transform: desde }, { transform: 'translate(' + x + 'px, ' + y + 'px)' }],
      { duration: ms || 520, easing: SUAVE }));
  }
  function pulsar(el, brillo) {
    yema.animate([{ transform: 'scale(1)' }, { transform: 'scale(.72)' }, { transform: 'scale(1)' }], { duration: 300, easing: 'ease-out' });
    el.animate([
      { transform: 'scale(1)', filter: 'brightness(1)' },
      { transform: 'scale(.9)', filter: 'brightness(' + (brillo || 1.7) + ')' },
      { transform: 'scale(1)', filter: 'brightness(1)' }
    ], { duration: 320, easing: 'ease-out' });
    return espera(340);
  }
  function volumen(n, sube) {
    var sale = sube ? -10 : 10;
    return num.animate([{ transform: 'none', opacity: 1 }, { transform: 'translateY(' + sale + 'px)', opacity: 0 }],
      { duration: 110, easing: 'ease-in' }).finished.then(function () {
      num.textContent = n;
      return num.animate([{ transform: 'translateY(' + (-sale) + 'px)', opacity: 0 }, { transform: 'none', opacity: 1 }],
        { duration: 220, easing: SUAVE }).finished;
    });
  }
  function paso(i, ms) {
    pasos.forEach(function (p, k) { p.classList.toggle('activa', k === i); });
    if (barra) barra.cancel();
    barra = pasos[i].querySelector('i').animate([{ transform: 'scaleX(0)' }, { transform: 'scaleX(1)' }],
      { duration: ms, easing: 'linear', fill: 'forwards' });
  }
  function hojaInputs(abrir) {
    fijar(velo.animate([{ opacity: abrir ? 0 : 1 }, { opacity: abrir ? 1 : 0 }], { duration: 300 }));
    return fijar(hoja.animate([{ transform: abrir ? 'translateY(105%)' : 'none' }, { transform: abrir ? 'none' : 'translateY(105%)' }],
      { duration: abrir ? 460 : 380, easing: abrir ? SUAVE : 'cubic-bezier(.4, 0, 1, 1)' }));
  }

  async function ciclo() {
    var c = centro($('.demo-cruceta'));
    x = c[0]; y = c[1] + 40;
    dedo.style.transform = 'translate(' + x + 'px, ' + y + 'px)';
    fijar(dedo.animate([{ opacity: 0 }, { opacity: 1 }], { duration: 400 }));
    for (;;) {
      paso(0, 3700);
      await ir(d('vol+'));
      for (var n = 10; n <= 11; n++) { await pulsar(d('vol+')); await volumen(n, true); await espera(260); }
      await ir(d('vol-'), 380);
      for (n = 10; n >= 9; n--) { await pulsar(d('vol-')); await volumen(n, false); await espera(260); }
      await espera(300);
      paso(1, 3300);
      await ir(d('der')); await pulsar(d('der'), 2.2);
      await ir(d('abajo'), 420); await pulsar(d('abajo'), 2.2);
      await ir(d('ok'), 420); await pulsar(d('ok'), 1.25);
      await espera(600);
      paso(2, 4300);
      await ir(d('inputs')); await pulsar(d('inputs'));
      await hojaInputs(true);
      await ir(d('hdmi1'), 480); await pulsar(d('hdmi1'), 1.3);
      d('hdmi1').classList.add('elegida');
      await espera(950);
      await hojaInputs(false);
      d('hdmi1').classList.remove('elegida');
      await espera(450);
    }
  }

  function aplicar() {
    var parar = pausadoPorUsuario || !visible;
    raiz.getAnimations({ subtree: true }).forEach(function (a) {
      if (parar && a.playState === 'running') a.pause();
      else if (!parar && a.playState === 'paused') a.play();
    });
    if (!parar && !corriendo) { corriendo = true; ciclo(); }
  }
  boton.addEventListener('click', function () {
    pausadoPorUsuario = !pausadoPorUsuario;
    boton.setAttribute('aria-pressed', String(pausadoPorUsuario));
    boton.setAttribute('aria-label', pausadoPorUsuario ? 'Play the demo' : 'Pause the demo');
    aplicar();
  });
  new IntersectionObserver(function (e) { visible = e[0].isIntersecting; aplicar(); }, { threshold: 0.3 }).observe(raiz);
})();
