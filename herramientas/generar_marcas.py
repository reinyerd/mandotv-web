# Genera las páginas por marca de mandotv.app (una carpeta con index.html por marca).
import json, os, html, sys

SITIO = sys.argv[1]
URL = 'https://mandotv.app'

MARCAS = [
  dict(slug='control-remoto-lg', nombre='LG', corto='LG', color='#e0457b',
    titulo='Control remoto para TV LG en tu celular, gratis | Mando TV',
    desc='Usa tu celular o tu PC como control remoto de tu Smart TV LG con webOS, por WiFi. Botones, puntero, teclado, apps, entradas, salida de audio y encendido. Gratis y sin anuncios.',
    h1='Control remoto para TV LG',
    intro='Mando TV convierte tu celular o tu computador en el control remoto de tu Smart TV LG con webOS, por la red WiFi de tu casa. Sirve si perdiste el control, si se le acabaron las pilas o si simplemente quieres escribir más rápido.',
    compat='Smart TV LG con sistema webOS (la mayoría de los modelos LG Smart TV desde 2014). Funciona con televisores LED, NanoCell, QNED y OLED.',
    funciones=[
      ('Todos los botones', 'Cruceta, OK, Atrás, Inicio, volumen, canales, silencio y reproducción.'),
      ('Puntero como el Magic Remote', 'Mueve la flecha por la pantalla con el dedo, igual que con el control mágico de LG.'),
      ('Teclado', 'Escribe en YouTube, Netflix o el navegador del TV con el teclado de tu celular.'),
      ('Apps y entradas', 'Abre tus apps y cambia a HDMI, TV en vivo, AirPlay o Screen Share.'),
      ('Salida de audio', 'Cambia entre los parlantes del TV y tu barra de sonido.'),
      ('Encender el TV', 'Si está apagado, Mando TV lo enciende por la red y se conecta solo.'),
    ],
    pasos=[
      'Conecta el celular y el televisor a la misma red WiFi.',
      'Abre Mando TV: tu TV LG aparece solo en la lista. Tócalo.',
      'En la pantalla del televisor aparece un aviso pidiendo permiso. Acéptalo con el control de siempre (solo la primera vez).',
    ],
    encender='Activa "Encender TV con móvil" (en algunos modelos se llama "Encendido por Wi-Fi"). Está en Configuración, General o Conexión, Configuración de dispositivos móviles.',
    faq=[
      ('¿Necesito el Magic Remote para usar Mando TV?', 'Solo la primera vez, para aceptar el permiso en la pantalla. Después puedes usar solo el celular.'),
      ('¿Mando TV reemplaza a LG ThinQ?', 'Para manejar el televisor, sí: no necesitas cuenta de LG ni registrar el TV. Mando TV se conecta directo por tu WiFi.'),
      ('¿Puedo encender mi TV LG desde el celular?', 'Sí, si activas "Encender TV con móvil" en el televisor y te conectaste una vez con el TV encendido.'),
    ]),
  dict(slug='control-remoto-samsung', nombre='Samsung', corto='Samsung', color='#3d7bff',
    titulo='Control remoto para TV Samsung en tu celular, gratis | Mando TV',
    desc='Usa tu celular o tu PC como control remoto de tu Smart TV Samsung con Tizen, por WiFi. Botones, touchpad, teclado, apps y encendido. Gratis, sin anuncios y sin cuenta Samsung.',
    h1='Control remoto para TV Samsung',
    intro='Mando TV convierte tu celular o tu computador en el control remoto de tu Smart TV Samsung, por la red WiFi de tu casa. No necesitas cuenta Samsung ni registrar el televisor.',
    compat='Smart TV Samsung con sistema Tizen, modelos 2016 en adelante (series como Crystal UHD, QLED, Neo QLED, The Frame y OLED).',
    funciones=[
      ('Todos los botones', 'Cruceta, OK, Volver, Inicio, volumen, canales, silencio y fuente.'),
      ('Touchpad', 'Desliza el dedo para moverte por los menús sin buscar flechas.'),
      ('Teclado', 'Escribe búsquedas y contraseñas con el teclado de tu celular.'),
      ('Apps', 'Abre Netflix, YouTube, Prime Video y tus otras apps con un toque.'),
      ('Encender el TV', 'Si está apagado, Mando TV lo enciende por la red y se conecta solo.'),
      ('Sin cuenta', 'Se conecta directo por tu WiFi, sin pasar por internet.'),
    ],
    pasos=[
      'Conecta el celular y el televisor a la misma red WiFi.',
      'Abre Mando TV: tu TV Samsung aparece solo en la lista. Tócalo.',
      'El televisor pregunta si permites la conexión. Elige Permitir con el control (solo la primera vez).',
    ],
    encender='Activa "Encender con dispositivo móvil" en Ajustes, General, Red, Configuración experta.',
    faq=[
      ('Rechacé el permiso por error, ¿qué hago?', 'En el televisor ve a Ajustes, General, Administrador de dispositivos externos, Administrador de conexión de dispositivos, y cambia Mando TV a permitido.'),
      ('¿Mando TV reemplaza a SmartThings?', 'Para manejar el televisor, sí, y sin cuenta Samsung. Mando TV se conecta directo por tu WiFi.'),
      ('¿Funciona con televisores Samsung antiguos?', 'Funciona con los Samsung con Tizen, de 2016 en adelante. Los modelos anteriores usan otro sistema que todavía no soportamos.'),
    ]),
  dict(slug='control-remoto-roku', nombre='Roku', corto='Roku', color='#a77bff',
    titulo='Control remoto para Roku en tu celular, gratis | Mando TV',
    desc='Usa tu celular o tu PC como control remoto de tu Roku TV o reproductor Roku, por WiFi. Botones, teclado, canales, entradas y encendido. Gratis y sin anuncios.',
    h1='Control remoto para Roku',
    intro='Mando TV convierte tu celular o tu computador en el control remoto de tu Roku, por la red WiFi de tu casa. Funciona con televisores Roku TV y con los reproductores Roku que se conectan al HDMI.',
    compat='Televisores Roku TV (TCL, Hisense, Philips, Sharp, JVC y otros) y reproductores Roku (Express, Streaming Stick, Ultra).',
    funciones=[
      ('Todos los botones', 'Cruceta, OK, Atrás, Inicio, volumen, silencio, repetir y reproducción.'),
      ('Teclado', 'Escribe búsquedas en los canales de Roku con el teclado de tu celular.'),
      ('Canales', 'Abre Netflix, YouTube y tus otros canales de Roku con un toque.'),
      ('Entradas', 'En Roku TV, cambia a HDMI, antena o AV desde la app.'),
      ('Encender el TV', 'En televisores Roku TV con inicio rápido, Mando TV lo enciende desde el celular.'),
      ('Sin emparejar', 'Roku no pide código: lo tocas en la lista y listo.'),
    ],
    pasos=[
      'Conecta el celular y el Roku a la misma red WiFi.',
      'Abre Mando TV: tu Roku aparece solo en la lista. Tócalo.',
      'Si no conecta, en el Roku ve a Configuración, Sistema, Configuración avanzada del sistema, Control por apps móviles, y deja el acceso a la red en Predeterminado o Permisivo.',
    ],
    encender='En televisores Roku TV, activa "Inicio rápido de TV" en Configuración, Sistema, Energía. Los reproductores Roku conectados a otro televisor no se pueden encender así.',
    faq=[
      ('¿Funciona con el Roku Express o el Streaming Stick?', 'Sí. Todos los reproductores Roku y los televisores Roku TV se manejan igual.'),
      ('Mando TV no encuentra mi Roku, ¿qué hago?', 'Revisa que estén en la misma red WiFi y que el "Control por apps móviles" del Roku no esté desactivado. También puedes agregarlo escribiendo su dirección IP.'),
      ('¿Necesito cuenta de Roku?', 'No. Mando TV se conecta directo por tu WiFi.'),
    ]),
  dict(slug='control-remoto-android-tv', nombre='Android TV y Google TV', corto='Android TV', color='#2fbf8f',
    titulo='Control remoto para Android TV y Google TV en tu celular | Mando TV',
    desc='Usa tu celular o tu PC como control remoto de tu Android TV o Google TV (Sony, TCL, Philips, Xiaomi, Chromecast). Botones, touchpad, teclado y apps. Gratis y sin anuncios.',
    h1='Control remoto para Android TV',
    intro='Mando TV convierte tu celular o tu computador en el control remoto de tu Android TV o Google TV, por la red WiFi de tu casa. También en iPhone y en Windows.',
    compat='Televisores con Android TV o Google TV (Sony, TCL, Philips, Xiaomi, Hisense y otros), Chromecast con Google TV, Google TV Streamer y Nvidia Shield.',
    funciones=[
      ('Todos los botones', 'Cruceta, OK, Atrás, Inicio, volumen, silencio y reproducción.'),
      ('Touchpad', 'Desliza el dedo para moverte rápido por los menús de Google TV.'),
      ('Teclado', 'Escribe búsquedas y contraseñas con el teclado de tu celular.'),
      ('Apps', 'Abre YouTube, Netflix, Disney+ y tus otras apps con un toque.'),
      ('Encender el TV', 'En los modelos con encendido por red, Mando TV lo enciende y se conecta solo.'),
      ('iPhone, Android y PC', 'Funciona igual desde cualquier celular o computador.'),
    ],
    pasos=[
      'Conecta el celular y el televisor a la misma red WiFi.',
      'Abre Mando TV: tu Android TV aparece solo en la lista. Tócalo.',
      'El televisor muestra un código de 6 caracteres. Escríbelo en Mando TV (solo la primera vez).',
    ],
    encender='Depende del fabricante. Busca "Wake on LAN", "Encender por red" o "Activación remota" en los ajustes de red o de energía. Algunos modelos no lo traen.',
    faq=[
      ('¿Funciona con el Chromecast con Google TV?', 'Sí, se empareja con el código de 6 caracteres que aparece en la pantalla.'),
      ('¿En qué se diferencia de la app de Google TV?', 'Mando TV no necesita cuenta de Google, funciona también desde Windows y Mac, y maneja además televisores LG, Samsung y Roku desde la misma app.'),
      ('El código no aparece en la pantalla, ¿qué hago?', 'Cierra Mando TV, vuelve a abrirla y toca el televisor otra vez. Revisa que el TV no esté en modo de ahorro de energía profundo.'),
    ]),
]

LOGO = '<svg viewBox="0 0 34 34" aria-hidden="true"><rect x="7" y="1" width="20" height="32" rx="10" fill="#0d0f17"/><circle cx="17" cy="12" r="5" fill="#fff"/><rect x="13" y="22" width="8" height="3" rx="1.5" fill="#fff"/></svg>'

def otras(actual):
    return '\n'.join(f'          <li><a href="/{m["slug"]}/">Control remoto para {m["nombre"]}</a></li>' for m in MARCAS if m is not actual)

def pagina(m):
    e = html.escape
    url = f'{URL}/{m["slug"]}/'
    ld = {"@context": "https://schema.org", "@graph": [
      {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Mando TV", "item": URL + "/"},
        {"@type": "ListItem", "position": 2, "name": f'Control remoto para {m["nombre"]}', "item": url}]},
      {"@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in m["faq"]]}]}
    funciones = '\n'.join(f'        <li><b>{e(t)}</b><span>{e(d)}</span></li>' for t, d in m['funciones'])
    pasos = '\n'.join(f'          <li>{e(p)}</li>' for p in m['pasos'])
    faq = '\n'.join(f'        <details><summary>{e(q)}</summary><p>{e(a)}</p></details>' for q, a in m['faq'])
    asunto = f'Avísame cuando salga Mando TV ({m["corto"]})'
    from urllib.parse import quote
    mailto = f'mailto:hola@mandotv.app?subject={quote(asunto)}&amp;body={quote("Hola, quiero saber cuando Mando TV esté en la tienda. Mi televisor es: ")}'
    return f'''<!doctype html>
<html lang="es" style="--marca: {m["color"]}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{e(m["titulo"])}</title>
  <meta name="description" content="{e(m["desc"])}">
  <meta name="robots" content="index, follow, max-image-preview:large">
  <meta name="theme-color" content="{m["color"]}">
  <link rel="canonical" href="{url}">
  <meta property="og:site_name" content="Mando TV">
  <meta property="og:locale" content="es_LA">
  <meta property="og:type" content="website">
  <meta property="og:url" content="{url}">
  <meta property="og:title" content="{e(m["titulo"])}">
  <meta property="og:description" content="{e(m["desc"])}">
  <meta property="og:image" content="{URL}/social.png">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="apple-touch-icon" href="/apple-touch-icon.png">
  <link rel="icon" href="/icono.svg" type="image/svg+xml">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..100,600..900&family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/estilos.css?v=10">
  <script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
</head>
<body>
  <div class="cabecera-pagina">
    <div class="contenedor">
      <header class="barra">
        <a class="logo" href="/" aria-label="Mando TV, inicio">
          {LOGO}
          Mando TV
        </a>
        <nav aria-label="Principal">
          <a href="/#funciones">Qué hace</a>
          <a href="/soporte.html">Ayuda</a>
          <a class="boton-barra" href="mailto:hola@mandotv.app?subject=Hola%20Mando%20TV">Contacto</a>
        </nav>
      </header>
      <nav class="migas" aria-label="Ruta"><a href="/">Mando TV</a> / <span>{e(m["nombre"])}</span></nav>
      <h1>{e(m["h1"])}</h1>
      <p>{e(m["intro"])}</p>
      <div class="acciones">
        <a class="boton" href="{mailto}">Avísame cuando salga</a>
        <a class="boton claro" href="#como">Cómo se conecta</a>
      </div>
      <ul class="tiendas" aria-label="Disponible en las tiendas">
        <li><a class="tienda" href="mailto:hola@mandotv.app?subject=Av%C3%ADsame%20cuando%20Mando%20TV%20salga%20en%20App%20Store&amp;body=Hola%2C%20quiero%20saber%20cuando%20Mando%20TV%20est%C3%A9%20disponible%20en%20iPhone%20y%20iPad%20%28App%20Store%29.%20Mi%20televisor%20es%3A%20" aria-label="Próximamente en App Store: avísame cuando salga"><svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M12.152 6.896c-.948 0-2.415-1.078-3.96-1.04-2.04.027-3.91 1.183-4.961 3.014-2.117 3.675-.546 9.103 1.519 12.09 1.013 1.454 2.208 3.09 3.792 3.039 1.52-.065 2.09-.987 3.935-.987 1.831 0 2.35.987 3.96.948 1.637-.026 2.676-1.48 3.676-2.948 1.156-1.688 1.636-3.325 1.662-3.415-.039-.013-3.182-1.221-3.22-4.857-.026-3.04 2.48-4.494 2.597-4.559-1.429-2.09-3.623-2.324-4.39-2.376-2-.156-3.675 1.09-4.61 1.09zM15.53 3.83c.843-1.012 1.4-2.427 1.245-3.83-1.207.052-2.662.805-3.532 1.818-.78.896-1.454 2.338-1.273 3.714 1.338.104 2.715-.688 3.559-1.701"/></svg><span><small>Próximamente en</small>App Store</span></a></li>
        <li><a class="tienda" href="mailto:hola@mandotv.app?subject=Av%C3%ADsame%20cuando%20Mando%20TV%20salga%20en%20Google%20Play&amp;body=Hola%2C%20quiero%20saber%20cuando%20Mando%20TV%20est%C3%A9%20disponible%20en%20Android%20%28Google%20Play%29.%20Mi%20televisor%20es%3A%20" aria-label="Próximamente en Google Play: avísame cuando salga"><svg viewBox="0 0 24 24" aria-hidden="true"><path fill="#00d7fe" d="M1.337.924a1.486 1.486 0 0 0-.112.568v21.017c0 .217.045.419.124.6l11.155-11.087L1.337.924z"/><path fill="#ffce00" d="M22.018 13.298l-3.919 2.218-3.515-3.493 3.543-3.521 3.891 2.202a1.49 1.49 0 0 1 0 2.594z"/><path fill="#00f076" d="M13.544 10.989l3.258-3.238L3.45.195a1.466 1.466 0 0 0-.946-.179l11.04 10.973z"/><path fill="#ff3a44" d="M13.544 13.056l-11 10.933c.298.036.612-.016.906-.183l13.324-7.54-3.23-3.21z"/></svg><span><small>Próximamente en</small>Google Play</span></a></li>
        <li><a class="tienda" href="https://apps.microsoft.com/detail/9N3D7T1DP2SW?mode=direct" target="_blank" rel="noopener" aria-label="Descargar Mando TV gratis en Microsoft Store"><svg viewBox="0 0 24 24" aria-hidden="true"><path fill="#f25022" d="M1 1h10.5v10.5H1z"/><path fill="#7fba00" d="M12.5 1H23v10.5H12.5z"/><path fill="#00a4ef" d="M1 12.5h10.5V23H1z"/><path fill="#ffb900" d="M12.5 12.5H23V23H12.5z"/></svg><span><small>Descárgalo en</small>Microsoft Store</span></a></li>
      </ul>
      <p class="nota">iPhone, iPad, Android, Windows y Mac. Gratis y sin anuncios.</p>
    </div>
  </div>

  <main class="contenedor">
    <div class="documento">
      <h2 id="compatibles">Televisores compatibles</h2>
      <p>{e(m["compat"])}</p>

      <h2 id="funciones">Qué puedes hacer con tu {e(m["corto"])}</h2>
      <ul class="lista-funciones">
{funciones}
      </ul>

      <h2 id="como">Cómo conectar tu {e(m["corto"])} con Mando TV</h2>
      <ol>
{pasos}
      </ol>

      <h2 id="encender">Encender tu {e(m["corto"])} desde el celular</h2>
      <p>{e(m["encender"])} Después, cuando toques el televisor apagado en Mando TV, la app te preguntará si quieres encenderlo y se conectará sola.</p>

      <h2 id="preguntas">Preguntas sobre {e(m["corto"])}</h2>
      <div class="preguntas">
{faq}
      </div>

      <h2 id="otras">Otras marcas</h2>
      <p>Mando TV maneja todas estas marcas desde la misma app:</p>
      <ul>
{otras(m)}
      </ul>
    </div>
  </main>

  <footer class="pie">
    <div class="contenedor">
      <div class="pie-enlaces">
        <nav aria-label="Pie de página">
          <a href="/">Inicio</a>
          <a href="/soporte.html">Ayuda</a>
          <a href="/privacidad.html">Privacidad</a>
          <a href="mailto:hola@mandotv.app">hola@mandotv.app</a>
          <button type="button" class="enlace-cookies" data-cookies>Cookies</button>
        </nav>
        <span>Hecho en Chile</span>
      </div>
      <p class="pie-gigante" aria-hidden="true">MANDO</p>
      <small>Mando TV no está afiliado a LG, Samsung, Roku ni Google. Las marcas nombradas pertenecen a sus dueños y se mencionan solo para indicar compatibilidad.</small>
    </div>
  </footer>
  <script src="/correo.js?v=3" defer></script>
  <script src="/cookies.js?v=1" defer></script>
  <!-- Cloudflare Web Analytics: cuenta visitas sin cookies ni datos personales -->
  <script defer src="https://static.cloudflareinsights.com/beacon.min.js" data-cf-beacon='{{"token": "3a3f0250e4b04d5884b033b9a94302b4"}}'></script>
</body>
</html>
'''

for m in MARCAS:
    d = os.path.join(SITIO, m['slug'])
    os.makedirs(d, exist_ok=True)
    open(os.path.join(d, 'index.html'), 'w', encoding='utf-8', newline='\n').write(pagina(m))
    print('ok', m['slug'])
