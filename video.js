// Videos propios (.video-marco): un botón grande "Play" sobre el póster en vez de la barra nativa, que en el celular
// tapa medio póster. Los controles nativos aparecen al reproducir. Sin JavaScript quedan los controles nativos.
// El video no descarga nada hasta que se pulsa (preload="none"): solo el póster.
(function () {
  document.querySelectorAll('.video-marco').forEach(function (marco) {
    var video = marco.querySelector('video');
    if (!video) return;
    var boton = document.createElement('button');
    boton.type = 'button';
    boton.className = 'video-play';
    boton.innerHTML = '<i aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg></i>';
    boton.appendChild(document.createTextNode(marco.dataset.play || 'Play'));
    video.controls = false;
    marco.appendChild(boton);

    boton.addEventListener('click', function () {
      video.controls = true;
      var p = video.play();
      if (p && p.catch) p.catch(function () { /* el navegador no dejó: quedan los controles nativos */ });
    });
    video.addEventListener('play', function () { boton.hidden = true; video.controls = true; });
    video.addEventListener('ended', function () { boton.hidden = false; });
  });
})();
