# Crea las páginas puente (redirecciones) de las URL viejas de mandotv.app, que ya no existen: GitHub Pages no hace 301,
# así que cada URL vieja deja un archivo que redirige al instante (mismo patrón que la portada vieja /en/): noindex,
# canonical a la URL nueva, location.replace (conserva ?consulta y #ancla) y meta refresh. Las URL viejas siguen
# publicadas en Google, en las fichas de las tiendas (privacidad y soporte) y en enlaces de terceros.
# Esquema nuevo (2026-11-25): inglés en la raíz /, el resto de idiomas bajo su prefijo (/es/, /de/, /fr/, /pt/, /it/).
# Uso: python -I herramientas/generar_redirecciones.py <carpeta del sitio>
# Escribe también docs/REDIRECCIONES.tsv (ruta vieja y ruta nueva, absolutas) para una regla masiva 301 en Cloudflare.
# Las páginas puente no van en sitemap.xml (llevan noindex y versionar.py las excluye).
import os, sys

SITIO = sys.argv[1]
URL = 'https://mandotv.app'

# (ruta vieja, ruta nueva, idioma de la página vieja). Lista explícita: no cambia aunque cambie idiomas_sitio.py.
REDIRECCIONES = [
  ('/control-remoto-android-tv/', '/es/control-remoto-android-tv/', 'es'),
  ('/control-remoto-bgh/', '/es/control-remoto-bgh/', 'es'),
  ('/control-remoto-caixun/', '/es/control-remoto-caixun/', 'es'),
  ('/control-remoto-hyundai/', '/es/control-remoto-hyundai/', 'es'),
  ('/control-remoto-kalley/', '/es/control-remoto-kalley/', 'es'),
  ('/control-remoto-lg/', '/es/control-remoto-lg/', 'es'),
  ('/control-remoto-master-g/', '/es/control-remoto-master-g/', 'es'),
  ('/control-remoto-noblex/', '/es/control-remoto-noblex/', 'es'),
  ('/control-remoto-roku/', '/es/control-remoto-roku/', 'es'),
  ('/control-remoto-samsung/', '/es/control-remoto-samsung/', 'es'),
  ('/en/android-tv-remote/', '/android-tv-remote/', 'en'),
  ('/en/guides/android-tv-pairing-code/', '/guides/android-tv-pairing-code/', 'en'),
  ('/en/guides/android-tv-without-remote/', '/guides/android-tv-without-remote/', 'en'),
  ('/en/guides/change-hdmi-input-without-remote/', '/guides/change-hdmi-input-without-remote/', 'en'),
  ('/en/guides/connect-phone-to-tv-wifi/', '/guides/connect-phone-to-tv-wifi/', 'en'),
  ('/en/guides/control-tv-from-pc/', '/guides/control-tv-from-pc/', 'en'),
  ('/en/guides/fire-tv-remote-app/', '/guides/fire-tv-remote-app/', 'en'),
  ('/en/guides/google-tv-remote-app-alternative/', '/guides/google-tv-remote-app-alternative/', 'en'),
  ('/en/guides/hisense-tv-remote-app/', '/guides/hisense-tv-remote-app/', 'en'),
  ('/en/guides/', '/guides/', 'en'),
  ('/en/guides/insignia-tv-remote-app/', '/guides/insignia-tv-remote-app/', 'en'),
  ('/en/guides/lg-thinq-app-alternative/', '/guides/lg-thinq-app-alternative/', 'en'),
  ('/en/guides/lost-fire-tv-remote/', '/guides/lost-fire-tv-remote/', 'en'),
  ('/en/guides/lost-lg-remote/', '/guides/lost-lg-remote/', 'en'),
  ('/en/guides/lost-roku-remote/', '/guides/lost-roku-remote/', 'en'),
  ('/en/guides/lost-tv-remote/', '/guides/lost-tv-remote/', 'en'),
  ('/en/guides/onn-tv-remote-app/', '/guides/onn-tv-remote-app/', 'en'),
  ('/en/guides/philips-tv-remote-app/', '/guides/philips-tv-remote-app/', 'en'),
  ('/en/guides/phone-cant-find-tv/', '/guides/phone-cant-find-tv/', 'en'),
  ('/en/guides/pioneer-tv-remote-app/', '/guides/pioneer-tv-remote-app/', 'en'),
  ('/en/guides/roku-app-alternative/', '/guides/roku-app-alternative/', 'en'),
  ('/en/guides/roku-remote-app-not-working/', '/guides/roku-remote-app-not-working/', 'en'),
  ('/en/guides/samsung-tv-without-remote/', '/guides/samsung-tv-without-remote/', 'en'),
  ('/en/guides/sharp-tv-remote-app/', '/guides/sharp-tv-remote-app/', 'en'),
  ('/en/guides/smartthings-tv-remote-alternative/', '/guides/smartthings-tv-remote-alternative/', 'en'),
  ('/en/guides/sony-tv-remote-app/', '/guides/sony-tv-remote-app/', 'en'),
  ('/en/guides/tcl-tv-remote-app/', '/guides/tcl-tv-remote-app/', 'en'),
  ('/en/guides/toshiba-tv-remote-app/', '/guides/toshiba-tv-remote-app/', 'en'),
  ('/en/guides/turn-on-lg-tv-with-phone/', '/guides/turn-on-lg-tv-with-phone/', 'en'),
  ('/en/guides/turn-on-tv-console-hdmi-without-remote/', '/guides/turn-on-tv-console-hdmi-without-remote/', 'en'),
  ('/en/guides/turn-on-tv-without-remote/', '/guides/turn-on-tv-without-remote/', 'en'),
  ('/en/guides/tv-remote-app-for-iphone/', '/guides/tv-remote-app-for-iphone/', 'en'),
  ('/en/guides/tv-remote-app-for-windows/', '/guides/tv-remote-app-for-windows/', 'en'),
  ('/en/guides/tv-remote-app-no-subscription/', '/guides/tv-remote-app-no-subscription/', 'en'),
  ('/en/guides/vizio-tv-remote-app/', '/guides/vizio-tv-remote-app/', 'en'),
  ('/en/guides/westinghouse-tv-remote-app/', '/guides/westinghouse-tv-remote-app/', 'en'),
  ('/en/', '/', 'en'),
  ('/en/lg-tv-remote/', '/lg-tv-remote/', 'en'),
  ('/en/privacy.html', '/privacy.html', 'en'),
  ('/en/roku-remote/', '/roku-remote/', 'en'),
  ('/en/samsung-tv-remote/', '/samsung-tv-remote/', 'en'),
  ('/en/support.html', '/support.html', 'en'),
  ('/guias/alternativa-a-la-app-de-roku/', '/es/guias/alternativa-a-la-app-de-roku/', 'es'),
  ('/guias/alternativa-a-la-app-google-tv/', '/es/guias/alternativa-a-la-app-google-tv/', 'es'),
  ('/guias/alternativa-a-lg-thinq/', '/es/guias/alternativa-a-lg-thinq/', 'es'),
  ('/guias/alternativa-a-smartthings/', '/es/guias/alternativa-a-smartthings/', 'es'),
  ('/guias/android-tv-codigo-de-emparejamiento/', '/es/guias/android-tv-codigo-de-emparejamiento/', 'es'),
  ('/guias/android-tv-sin-control-remoto/', '/es/guias/android-tv-sin-control-remoto/', 'es'),
  ('/guias/app-control-remoto-para-iphone/', '/es/guias/app-control-remoto-para-iphone/', 'es'),
  ('/guias/app-control-remoto-para-windows/', '/es/guias/app-control-remoto-para-windows/', 'es'),
  ('/guias/app-control-remoto-sin-suscripcion/', '/es/guias/app-control-remoto-sin-suscripcion/', 'es'),
  ('/guias/cambiar-entrada-hdmi-sin-control/', '/es/guias/cambiar-entrada-hdmi-sin-control/', 'es'),
  ('/guias/conectar-celular-al-tv-por-wifi/', '/es/guias/conectar-celular-al-tv-por-wifi/', 'es'),
  ('/guias/control-remoto-fire-tv-en-el-celular/', '/es/guias/control-remoto-fire-tv-en-el-celular/', 'es'),
  ('/guias/control-remoto-hisense/', '/es/guias/control-remoto-hisense/', 'es'),
  ('/guias/control-remoto-philips/', '/es/guias/control-remoto-philips/', 'es'),
  ('/guias/control-remoto-samsung-sin-control/', '/es/guias/control-remoto-samsung-sin-control/', 'es'),
  ('/guias/control-remoto-sony/', '/es/guias/control-remoto-sony/', 'es'),
  ('/guias/control-remoto-tcl/', '/es/guias/control-remoto-tcl/', 'es'),
  ('/guias/controlar-el-tv-desde-el-pc/', '/es/guias/controlar-el-tv-desde-el-pc/', 'es'),
  ('/guias/el-celular-no-encuentra-el-tv/', '/es/guias/el-celular-no-encuentra-el-tv/', 'es'),
  ('/guias/encender-el-tv-sin-control/', '/es/guias/encender-el-tv-sin-control/', 'es'),
  ('/guias/encender-tv-lg-con-el-celular/', '/es/guias/encender-tv-lg-con-el-celular/', 'es'),
  ('/guias/encender-tv-y-hdmi-de-la-consola-sin-control/', '/es/guias/encender-tv-y-hdmi-de-la-consola-sin-control/', 'es'),
  ('/guias/', '/es/guias/', 'es'),
  ('/guias/perdi-el-control-del-fire-tv/', '/es/guias/perdi-el-control-del-fire-tv/', 'es'),
  ('/guias/perdi-el-control-del-lg/', '/es/guias/perdi-el-control-del-lg/', 'es'),
  ('/guias/perdi-el-control-del-roku/', '/es/guias/perdi-el-control-del-roku/', 'es'),
  ('/guias/perdi-el-control-del-tv/', '/es/guias/perdi-el-control-del-tv/', 'es'),
  ('/guias/roku-no-responde-al-celular/', '/es/guias/roku-no-responde-al-celular/', 'es'),
  ('/privacidad.html', '/es/privacidad.html', 'es'),
  ('/soporte.html', '/es/soporte.html', 'es'),
]

PLANTILLA = """<!doctype html>
<html lang="@@lang@@">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="referrer" content="strict-origin-when-cross-origin">
  <title>Mando TV</title>
  <!-- 25-nov: esta URL se movió. GitHub Pages no hace redirecciones 301: esta página redirige al instante
       (Google trata el refresh de 0 s como redirección permanente) y conserva la consulta y el #. -->
  <meta name="robots" content="noindex">
  <link rel="canonical" href="@@url@@@@nueva@@">
  <script>location.replace('@@nueva@@' + location.search + location.hash);</script>
  <meta http-equiv="refresh" content="0; url=@@nueva@@">
</head>
<body>
  <p><a href="@@nueva@@">Mando TV</a></p>
</body>
</html>
"""


def destino(vieja):
    ruta = vieja.lstrip('/')
    if vieja.endswith('/'):
        ruta += 'index.html'
    return os.path.join(SITIO, *ruta.split('/'))


def pagina(lang, nueva):
    return PLANTILLA.replace('@@lang@@', lang).replace('@@url@@', URL).replace('@@nueva@@', nueva)


for vieja, nueva, lang in REDIRECCIONES:
    d = destino(vieja)
    os.makedirs(os.path.dirname(d), exist_ok=True)
    with open(d, 'w', encoding='utf-8', newline='\n') as f:
        f.write(pagina(lang, nueva))
os.makedirs(os.path.join(SITIO, 'docs'), exist_ok=True)
with open(os.path.join(SITIO, 'docs', 'REDIRECCIONES.tsv'), 'w', encoding='utf-8', newline='\n') as f:
    for vieja, nueva, _ in REDIRECCIONES:
        f.write(vieja + '\t' + nueva + '\n')
print('ok', len(REDIRECCIONES), 'redirecciones')
