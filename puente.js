// Páginas puente de URL viejas (las escribe herramientas/generar_redirecciones.py): llevan a la URL nueva conservando
// ?consulta y #ancla. Archivo externo para que la Content-Security-Policy no necesite permitir scripts en línea.
// Solo acepta rutas del mismo sitio ("/algo"), nunca otro dominio ni "//dominio".
(function () {
  var s = document.currentScript;
  var d = s && s.getAttribute('data-destino');
  if (d && d.charAt(0) === '/' && d.charAt(1) !== '/' && d.indexOf('\\') < 0) {
    location.replace(d + location.search + location.hash);
  }
})();
