# Genera las páginas guía de mandotv.app (/guias/<tema>/index.html). Mismo patrón que generar_marcas.py.
# Uso: python -I herramientas/generar_guias.py <carpeta del sitio>
import json, os, html, sys

SITIO = sys.argv[1]
URL = 'https://mandotv.app'
FECHA = '2026-11-15'
TIENDA = 'https://apps.microsoft.com/detail/9N3D7T1DP2SW?mode=direct'
TIENDA_APPLE = 'https://apps.apple.com/app/id6834927348'

MARCAS_ENLACES = [
  ('control-remoto-samsung', 'Control remoto Samsung'),
  ('control-remoto-lg', 'Control remoto LG'),
  ('control-remoto-roku', 'Control remoto Roku'),
  ('control-remoto-android-tv', 'Control remoto Android TV'),
]

GUIAS = [
  dict(slug='guias/encender-tv-lg-con-el-celular', corto='Encender TV LG con el celular',
    titulo='Cómo encender tu TV LG con el celular (paso a paso) | Mando TV',
    desc='Aprende a encender tu TV LG con el celular por WiFi: activa "Encender TV con móvil" en el televisor y usa Mando TV. Paso a paso, gratis y sin anuncios.',
    h1='Cómo encender el TV LG con el celular',
    intro='Se puede, pero primero hay que activar una opción en el televisor. Una vez hecho, tu celular enciende el TV LG por la red WiFi, sin el control remoto. Son cinco minutos y lo haces una sola vez.',
    pasos=[
      'Conecta el celular y el TV LG a la misma red WiFi.',
      'En el TV, abre Configuración y busca "Encender TV con móvil". Según el modelo está en General o en Conexión.',
      'Activa "Encender a través de Wi-Fi". Si tu TV está conectado con cable de red, activa "Encender a través de cable".',
      'Si tu TV tiene "Quick Start+", actívalo también.',
      'Con el TV encendido, abre Mando TV en el celular y toca tu TV LG en la lista. Acepta el aviso que aparece en la pantalla. Así la app aprende a despertarlo.',
      'Apaga el TV y pruébalo: toca el TV en Mando TV y la app te pregunta si quieres encenderlo.',
    ],
    extra=[
      ('Si no enciende', 'El TV debe haber estado conectado a la misma red WiFi cuando se apagó. Revisa que la opción siga activada y que el celular esté en esa misma red. Si cambiaste de router, vuelve a conectarte una vez con el TV encendido.'),
    ],
    marca=('control-remoto-lg', 'Control remoto para TV LG'),
    faq=[
      ('¿Puedo encender el TV LG con el celular si nunca lo conecté?', 'No. Primero hay que activar "Encender TV con móvil" en el televisor y conectarse una vez con Mando TV con el TV encendido.'),
      ('¿Necesito la app LG ThinQ?', 'No. Mando TV se conecta directo por tu WiFi y no pide cuenta de LG.'),
      ('¿Funciona con el celular con datos móviles?', 'No. El celular y el TV deben estar en la misma red WiFi.'),
    ]),
  dict(slug='guias/control-remoto-samsung-sin-control', corto='TV Samsung sin control',
    titulo='¿Perdiste el control del TV Samsung? Usa tu celular | Mando TV',
    desc='Si perdiste el control de tu TV Samsung o no funciona, usa tu celular como control remoto por WiFi. Pasos simples con Mando TV, gratis y sin anuncios.',
    h1='Control remoto Samsung sin el control original',
    intro='Si perdiste el control del TV Samsung o dejó de funcionar, puedes usar tu celular como control por WiFi. Sirve en televisores Samsung con Tizen, de 2016 en adelante.',
    pasos=[
      'Enciende el TV con el botón físico. En la mayoría de los modelos está abajo o detrás, a veces como un joystick pequeño.',
      'Revisa que el TV esté conectado a tu WiFi y que el celular esté en la misma red.',
      'Abre Mando TV en el celular. Tu TV Samsung aparece solo en la lista. Tócalo.',
      'El TV pide aceptar la conexión. En la mayoría de los modelos se acepta con los botones físicos del TV o con el joystick de atrás.',
      'Listo, ya puedes usar el celular como control: botones, touchpad, teclado y apps.',
      'Para encenderlo la próxima vez desde el celular, ve a Configuración > General > Red > Configuración experta y activa "Encender con dispositivo móvil".',
    ],
    extra=[
      ('Si el TV no pide permiso', 'Puede que el permiso ya esté guardado o que el TV esté en otra red WiFi. Cierra Mando TV y vuelve a abrirla con el TV encendido. Si el TV es anterior a 2016, usa otro sistema y todavía no es compatible.'),
    ],
    marca=('control-remoto-samsung', 'Control remoto para TV Samsung'),
    faq=[
      ('¿Cómo acepto la conexión si no tengo el control?', 'En la mayoría de los modelos se acepta con los botones físicos del TV o con el joystick de atrás. Si tu modelo no tiene botones, escríbenos a hola@mandotv.app y te ayudamos.'),
      ('¿Mando TV pide cuenta Samsung?', 'No. Se conecta directo por tu WiFi, sin cuenta Samsung.'),
      ('¿Funciona con mi Samsung antiguo?', 'Funciona con televisores Samsung con Tizen, de 2016 en adelante.'),
    ]),
  dict(slug='guias/conectar-celular-al-tv-por-wifi', corto='Celular como control por WiFi',
    titulo='Cómo usar el celular como control remoto del TV por WiFi | Mando TV',
    desc='Conecta tu celular al TV por WiFi y úsalo de control remoto en Samsung, LG, Roku y Google TV. Pasos para cada marca con Mando TV, gratis y sin anuncios.',
    h1='Cómo conectar el celular al TV por WiFi para usarlo de control',
    intro='Solo necesitas que el celular y el TV estén en la misma red WiFi y una app de control. Mando TV encuentra tu televisor solo y funciona con Samsung, LG, Roku, Google TV y Android TV.',
    pasos=[
      'Conecta el celular y el TV a la misma red WiFi.',
      'Abre Mando TV. Tu televisor aparece solo en la lista. Tócalo.',
      'Acepta la conexión según tu marca (abajo está el detalle de cada una).',
      'Usa los botones, el touchpad o el teclado del celular para manejar el TV.',
    ],
    extra=[
      ('Samsung', 'El TV pregunta si permites la conexión. Acéptala en la pantalla la primera vez. Funciona con Tizen, de 2016 en adelante. Para encenderlo desde el celular, activa "Encender con dispositivo móvil" en Configuración > General > Red > Configuración experta.'),
      ('LG', 'El TV muestra un aviso pidiendo permiso. Acéptalo la primera vez. Para encenderlo desde el celular, busca "Encender TV con móvil" en Configuración y activa "Encender a través de Wi-Fi".'),
      ('Roku', 'Roku no pide emparejar: lo tocas en la lista y listo. Para encenderlo, activa "Inicio rápido del TV" en Configuración > Sistema > Energía.'),
      ('Google TV y Android TV', 'El TV muestra un código en la pantalla. Escríbelo en Mando TV la primera vez. Para encenderlo, busca "Wake on LAN", "Encender por red" o "Activación en red" en los ajustes.'),
    ],
    marca=None,
    faq=[
      ('¿Necesito internet para usar el celular como control?', 'Necesitas que el celular y el TV estén en la misma red WiFi. Mando TV se conecta directo a tu TV por esa red.'),
      ('¿Por qué no aparece mi TV en la lista?', 'Revisa que el TV esté encendido y que el celular no esté usando datos móviles ni otra red WiFi. Algunos routers tienen una red de invitados que separa los equipos.'),
      ('¿Puedo usar Mando TV desde iPhone o Android?', 'Sí en iPhone y iPad: ya está en App Store. También en Microsoft Store para Windows. Pronto llega a Android y Mac.'),
    ]),
  dict(slug='guias/controlar-el-tv-desde-el-pc', corto='Controlar el TV desde el PC',
    titulo='Cómo controlar el TV desde el PC con Windows (gratis) | Mando TV',
    desc='Usa tu computador con Windows como control remoto del TV Samsung, LG, Roku o Google TV por WiFi. Botones, teclado y apps con Mando TV, gratis y sin anuncios.',
    h1='Cómo controlar el TV desde el PC con Windows',
    intro='Si pasas el día frente al computador, no necesitas buscar el control: Mando TV para Windows maneja tu televisor Samsung, LG, Roku, Google TV o Android TV por la red WiFi de tu casa. Sirve para cambiar de app, subir el volumen o escribir en YouTube con el teclado del PC.',
    pasos=[
      'Descarga Mando TV gratis desde Microsoft Store en tu computador con Windows 10 u 11.',
      'Revisa que el computador y el TV estén en la misma red (WiFi o cable, pero del mismo router).',
      'Abre Mando TV: tu televisor aparece solo en la lista. Tócalo o haz clic en él.',
      'Acepta la conexión en la pantalla del TV la primera vez (en Google TV y Android TV escribe el código que muestra el TV).',
      'Listo: usa los botones, el touchpad o el teclado para escribir en el buscador del TV.',
    ],
    extra=[
      ('Atajos del teclado del PC (Pro)', 'Con Mando TV Pro manejas el TV con el teclado del computador: flechas para moverte, Enter para OK, Retroceso o Esc para volver, + y − para el volumen, M para silenciar y Espacio para pausar.'),
      ('Mini control siempre encima (Pro)', 'Deja una ventana pequeña con el control siempre visible mientras trabajas o juegas en el PC.'),
    ],
    marca=None,
    faq=[
      ('¿Necesito un cable o Bluetooth para controlar el TV desde el PC?', 'No. Mando TV se conecta por la red de tu casa: basta con que el PC y el TV estén en el mismo router.'),
      ('¿Funciona con cualquier TV?', 'Con Samsung con Tizen (2016 en adelante), LG con webOS, Roku y Google TV o Android TV (Sony, TCL, Philips, Xiaomi y otros).'),
      ('¿Cuánto cuesta?', 'El control completo es gratis y sin anuncios. Mando TV Pro es un pago único, sin suscripción, para funciones extra como los atajos del teclado y el mini control.'),
    ]),
]

LOGO = '<img src="/icono.svg?v=1a26271c80" alt="" width="34" height="34">'
APPLE_SVG = '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M12.152 6.896c-.948 0-2.415-1.078-3.96-1.04-2.04.027-3.91 1.183-4.961 3.014-2.117 3.675-.546 9.103 1.519 12.09 1.013 1.454 2.208 3.09 3.792 3.039 1.52-.065 2.09-.987 3.935-.987 1.831 0 2.35.987 3.96.948 1.637-.026 2.676-1.48 3.676-2.948 1.156-1.688 1.636-3.325 1.662-3.415-.039-.013-3.182-1.221-3.22-4.857-.026-3.04 2.48-4.494 2.597-4.559-1.429-2.09-3.623-2.324-4.39-2.376-2-.156-3.675 1.09-4.61 1.09zM15.53 3.83c.843-1.012 1.4-2.427 1.245-3.83-1.207.052-2.662.805-3.532 1.818-.78.896-1.454 2.338-1.273 3.714 1.338.104 2.715-.688 3.559-1.701"/></svg>'
MS_SVG = '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="#f25022" d="M1 1h10.5v10.5H1z"/><path fill="#7fba00" d="M12.5 1H23v10.5H12.5z"/><path fill="#00a4ef" d="M1 12.5h10.5V23H1z"/><path fill="#ffb900" d="M12.5 12.5H23V23H12.5z"/></svg>'

def otras(actual):
    return '\n'.join(f'        <li><a href="/{g["slug"]}/">{html.escape(g["h1"])}</a></li>' for g in GUIAS if g is not actual)

def pagina(g):
    e = html.escape
    url = f'{URL}/{g["slug"]}/'
    ld = {"@context": "https://schema.org", "@graph": [
      {"@type": "Article", "headline": g["h1"], "description": g["desc"], "inLanguage": "es",
       "datePublished": FECHA, "dateModified": FECHA, "mainEntityOfPage": url, "image": URL + "/social.png",
       "author": {"@type": "Organization", "name": "Mando TV", "url": URL + "/"},
       "publisher": {"@type": "Organization", "name": "Mando TV", "url": URL + "/"}},
      {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Inicio", "item": URL + "/"},
        {"@type": "ListItem", "position": 2, "name": "Guías", "item": URL + "/soporte.html#guias"},
        {"@type": "ListItem", "position": 3, "name": g["h1"], "item": url}]},
      {"@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in g["faq"]]}]}
    pasos = '\n'.join(f'        <li>{e(p)}</li>' for p in g['pasos'])
    extra = '\n\n'.join(f'      <h2>{e(t)}</h2>\n      <p>{e(p)}</p>' for t, p in g['extra'])
    faq = '\n'.join(f'        <details><summary>{e(q)}</summary><p>{e(a)}</p></details>' for q, a in g['faq'])
    if g['marca']:
        marcas = f'<p>Más detalles en la página de <a href="/{g["marca"][0]}/">{e(g["marca"][1])}</a>.</p>'
    else:
        marcas = '<p>Más detalles por marca:</p>\n      <ul>\n' + '\n'.join(f'        <li><a href="/{s}/">{e(n)}</a></li>' for s, n in MARCAS_ENLACES) + '\n      </ul>'
    return f'''<!doctype html>
<html lang="es" style="--marca: #3d7bff">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{e(g["titulo"])}</title>
  <meta name="description" content="{e(g["desc"])}">
  <meta name="robots" content="index, follow, max-image-preview:large">
  <meta name="theme-color" content="#3d7bff">
  <link rel="canonical" href="{url}">
  <meta property="og:site_name" content="Mando TV">
  <meta property="og:locale" content="es_LA">
  <meta property="og:type" content="article">
  <meta property="og:url" content="{url}">
  <meta property="og:title" content="{e(g["titulo"])}">
  <meta property="og:description" content="{e(g["desc"])}">
  <meta property="og:image" content="{URL}/social.png">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="apple-touch-icon" href="/apple-touch-icon.png">
  <link rel="icon" href="/icono.svg" type="image/svg+xml">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..100,600..900&family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/estilos.css?v=12">
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
      <nav class="migas" aria-label="Ruta"><a href="/">Inicio</a> / <a href="/soporte.html#guias">Guías</a> / <span>{e(g["corto"])}</span></nav>
      <h1>{e(g["h1"])}</h1>
      <p>{e(g["intro"])}</p>
      <div class="acciones">
        <a class="boton" href="#pasos">Ver los pasos</a>
        <a class="boton claro" href="#mando-tv">Descargar gratis</a>
      </div>
    </div>
  </div>

  <main class="contenedor">
    <div class="documento">
      <h2 id="pasos">Paso a paso</h2>
      <ol>
{pasos}
      </ol>

{extra}

      <h2 id="mando-tv">Hazlo con Mando TV</h2>
      <p>Mando TV es un control remoto universal para tu televisor. Es gratis y sin anuncios, y no pide cuenta. Descárgalo para iPhone, iPad o Windows:</p>
      <ul class="tiendas" aria-label="Descargar Mando TV">
        <li><a class="tienda" href="{TIENDA_APPLE}" target="_blank" rel="noopener" aria-label="Descargar Mando TV gratis en App Store">{APPLE_SVG}<span><small>Descárgalo en</small>App Store</span></a></li>
        <li><a class="tienda" href="{TIENDA}" target="_blank" rel="noopener" aria-label="Descargar Mando TV gratis en Microsoft Store">{MS_SVG}<span><small>Descárgalo en</small>Microsoft Store</span></a></li>
      </ul>
      <p class="nota">Pronto en Android y Mac.</p>
      {marcas}

      <h2 id="preguntas">Preguntas frecuentes</h2>
      <div class="preguntas">
{faq}
      </div>

      <h2 id="otras">Otras guías</h2>
      <ul>
{otras(g)}
        <li><a href="/soporte.html">Ayuda y soporte</a></li>
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

for g in GUIAS:
    d = os.path.join(SITIO, *g['slug'].split('/'))
    os.makedirs(d, exist_ok=True)
    open(os.path.join(d, 'index.html'), 'w', encoding='utf-8', newline='\n').write(pagina(g))
    print('ok', g['slug'], len(g['titulo']), len(g['desc']))
