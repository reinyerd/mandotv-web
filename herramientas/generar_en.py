# Genera las páginas en inglés (EE. UU.) de mandotv.app: marcas, índice de guías y guías principales.
# Textos escritos para búsquedas en inglés (no son traducción literal). La portada /en/ se mantiene a mano.
# Uso: python -I herramientas/generar_en.py <carpeta del sitio>
# Mismo patrón que generar_guias.py y generar_marcas.py; hreflang es + en (+ x-default = español) en las dos versiones
# (las páginas en español lo reciben de sus propios generadores).
import ast, html, json, os, sys

SITIO = sys.argv[1]
URL = 'https://mandotv.app'
FECHA = '2026-11-18'
TIENDA = 'https://apps.microsoft.com/detail/9N3D7T1DP2SW?mode=direct'
TIENDA_APPLE = 'https://apps.apple.com/app/id6834927348'
ANDROID = '/en/#android'


def constantes():
    """Toma los íconos de las tiendas de generar_guias.py (así no se copian aquí)."""
    ruta = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'generar_guias.py')
    arbol = ast.parse(open(ruta, encoding='utf-8').read())
    buscados = {'LOGO', 'APPLE_SVG', 'MS_SVG', 'GPLAY_SVG'}
    datos = {}
    for n in arbol.body:
        if isinstance(n, ast.Assign) and len(n.targets) == 1 and getattr(n.targets[0], 'id', None) in buscados:
            datos[n.targets[0].id] = ast.literal_eval(n.value)
    assert set(datos) == buscados, datos.keys()
    return datos


K = constantes()
LOGO, APPLE_SVG, MS_SVG, GPLAY_SVG = K['LOGO'], K['APPLE_SVG'], K['MS_SVG'], K['GPLAY_SVG']

ORG = {"@type": "Organization", "@id": URL + "/#org", "name": "Mando TV", "url": URL + "/"}

# Equivalencias es <-> en: (carpeta en español, carpeta en inglés)
BRANDS = {
  'lg': ('control-remoto-lg', 'en/lg-tv-remote'),
  'samsung': ('control-remoto-samsung', 'en/samsung-tv-remote'),
  'roku': ('control-remoto-roku', 'en/roku-remote'),
  'android': ('control-remoto-android-tv', 'en/android-tv-remote'),
}
GUIDE_SLUGS = {
  'lost-tv': ('guias/perdi-el-control-del-tv', 'en/guides/lost-tv-remote'),
  'lost-lg': ('guias/perdi-el-control-del-lg', 'en/guides/lost-lg-remote'),
  'hdmi': ('guias/cambiar-entrada-hdmi-sin-control', 'en/guides/change-hdmi-input-without-remote'),
  'androidtv': ('guias/android-tv-sin-control-remoto', 'en/guides/android-tv-without-remote'),
  'lg-on': ('guias/encender-tv-lg-con-el-celular', 'en/guides/turn-on-lg-tv-with-phone'),
  'console': ('guias/encender-tv-y-hdmi-de-la-consola-sin-control', 'en/guides/turn-on-tv-console-hdmi-without-remote'),
}
# Guías que solo existen en español (se enlazan al español, con la etiqueta "(in Spanish)").
ES_ONLY = {
  'roku-lost': ('/guias/perdi-el-control-del-roku/', 'Lost your Roku remote'),
  'samsung-lost': ('/guias/control-remoto-samsung-sin-control/', 'Samsung TV remote without the original remote'),
  'androidtv-code': ('/guias/android-tv-codigo-de-emparejamiento/', 'Android TV asks for a pairing code'),
  'roku-403': ('/guias/roku-no-responde-al-celular/', 'Roku not responding to your phone (error 403)'),
  'not-found': ('/guias/el-celular-no-encuentra-el-tv/', 'Your phone cannot find the TV'),
}


def es_link(k):
    u, t = ES_ONLY[k]
    return f'<a href="{u}" hreflang="es" lang="es">{html.escape(t)} (in Spanish)</a>'


def en_url(clave, tabla):
    return '/' + tabla[clave][1] + '/'


# Pie de página en inglés: marcas y guías que existen en inglés.
PIE = [
  ('/en/samsung-tv-remote/', 'Samsung TV remote'),
  ('/en/lg-tv-remote/', 'LG TV remote'),
  ('/en/roku-remote/', 'Roku remote'),
  ('/en/android-tv-remote/', 'Android TV remote'),
  ('/en/guides/', 'All guides'),
  ('/en/guides/lost-tv-remote/', 'Lost TV remote'),
  ('/en/guides/lost-lg-remote/', 'Lost LG TV remote'),
  ('/en/guides/turn-on-lg-tv-with-phone/', 'Turn on an LG TV with your phone'),
  ('/en/guides/change-hdmi-input-without-remote/', 'Change the HDMI input without a remote'),
  ('/en/guides/android-tv-without-remote/', 'Android TV without a remote'),
  ('/en/guides/turn-on-tv-console-hdmi-without-remote/', 'Turn on the TV and switch to console HDMI'),
]


def pie_marcas():
    li = '\n'.join(f'        <li><a href="{u}">{n}</a></li>' for u, n in PIE)
    return f'      <ul class="marcas-enlaces pie-marcas" aria-label="Brands and guides">\n{li}\n      </ul>\n'


def hreflangs(es, en):
    return (f'  <link rel="alternate" hreflang="es" href="{URL}{es}">\n'
            f'  <link rel="alternate" hreflang="en" href="{URL}{en}">\n'
            f'  <link rel="alternate" hreflang="x-default" href="{URL}{es}">\n')


def fmt(t):
    """Escapa el texto y convierte [texto](/ruta/) en enlaces internos."""
    import re
    return re.sub(r'\[([^\]]+)\]\((/[^)\s]*)\)', lambda m: f'<a href="{m[2]}">{m[1]}</a>', html.escape(t))


def plano(t):
    import re
    return re.sub(r'\[([^\]]+)\]\((/[^)\s]*)\)', r'\1', t)


def cabecera(titulo, desc, url, es, en, color, tipo, ld):
    e = html.escape
    return f'''<!doctype html>
<html lang="en" style="--marca: {color}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="apple-itunes-app" content="app-id=6834927348">
  <title>{e(titulo)}</title>
  <meta name="description" content="{e(desc)}">
  <meta name="robots" content="index, follow, max-image-preview:large">
  <meta name="theme-color" content="{color}">
  <link rel="canonical" href="{url}">
{hreflangs(es, en)}  <meta property="og:site_name" content="Mando TV">
  <meta property="og:locale" content="en_US">
  <meta property="og:type" content="{tipo}">
  <meta property="og:url" content="{url}">
  <meta property="og:title" content="{e(titulo)}">
  <meta property="og:description" content="{e(desc)}">
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
        <a class="logo" href="/en/" aria-label="Mando TV, Home">
          {LOGO}
          Mando TV
        </a>
        <nav aria-label="Main">
          <a href="/en/#funciones">What it does</a>
          <a href="/soporte.html">Help</a>
          <a class="boton-barra" href="mailto:hola@mandotv.app?subject=Hello%20Mando%20TV">Contact</a>
        </nav>
      </header>
'''


def tiendas_html(idn=None, etiqueta='Download Mando TV'):
    ident = f' id="{idn}"' if idn else ''
    return f'''      <ul class="tiendas"{ident} aria-label="{etiqueta}">
        <li><a class="tienda" href="{TIENDA_APPLE}" target="_blank" rel="noopener" aria-label="Download Mando TV free on the App Store">{APPLE_SVG}<span><small>Download on</small>App Store</span></a></li>
        <li><a class="tienda" href="{ANDROID}" aria-label="Early access to Mando TV on Google Play for Android">{GPLAY_SVG}<span><small>Early access on</small>Google Play</span></a></li>
        <li><a class="tienda" href="{TIENDA}" target="_blank" rel="noopener" aria-label="Download Mando TV free on Microsoft Store">{MS_SVG}<span><small>Download on</small>Microsoft Store</span></a></li>
      </ul>'''


def tiendas_guia():
    return f'''      <ul class="tiendas" aria-label="Download Mando TV">
        <li><a class="tienda" href="{TIENDA_APPLE}" target="_blank" rel="noopener" aria-label="Download Mando TV free on the App Store">{APPLE_SVG}<span><small>Download on</small>App Store</span></a></li>
        <li><a class="tienda" href="{TIENDA}" target="_blank" rel="noopener" aria-label="Download Mando TV free on Microsoft Store">{MS_SVG}<span><small>Download on</small>Microsoft Store</span></a></li>
        <li><a class="tienda" href="{ANDROID}" aria-label="Early access to Mando TV on Google Play for Android">{GPLAY_SVG}<span><small>Early access on</small>Google Play</span></a></li>
      </ul>
      <p class="nota">Android: free early access on Google Play. <a href="{ANDROID}">Join in two steps</a> and help us reach the store.</p>'''


def pie(es_url):
    return f'''  <footer class="pie">
    <div class="contenedor">
      <div class="pie-enlaces">
        <nav aria-label="Footer">
          <a href="/en/">Home</a>
          <a href="/soporte.html">Help</a>
          <a href="/privacidad.html">Privacy</a>
          <a href="mailto:hola@mandotv.app">hola@mandotv.app</a>
          <a href="{es_url}" hreflang="es" lang="es">Español</a>
          <button type="button" class="enlace-cookies" data-cookies>Cookies</button>
        </nav>
        <span>Made in Chile</span>
      </div>
{pie_marcas()}      <p class="pie-gigante" aria-hidden="true">MANDO</p>
      <small>Mando TV is not affiliated with LG, Samsung, Roku or Google. Brands named belong to their owners and are mentioned only to show compatibility.</small>
    </div>
  </footer>
  <script src="/correo.js?v=3" defer></script>
  <script src="/cookies.js?v=1" defer></script>
  <!-- Cloudflare Web Analytics: cuenta visitas sin cookies ni datos personales -->
  <script defer src="https://static.cloudflareinsights.com/beacon.min.js" data-cf-beacon='{{"token": "3a3f0250e4b04d5884b033b9a94302b4"}}'></script>
</body>
</html>
'''


# ---------------------------------------------------------------------------------------------------------------
# Páginas por marca
# ---------------------------------------------------------------------------------------------------------------
MARCAS = [
  dict(clave='lg', nombre='LG', color='#e0457b',
    titulo='LG TV Remote App for Your Phone, Free | Mando TV',
    desc='Use your phone or PC as an LG TV remote for webOS over Wi-Fi. Buttons, keyboard and power-on are free; pointer, apps and inputs with Pro.',
    h1='LG TV Remote App for Your Phone',
    corto='LG',
    intro='Mando TV is an LG TV remote app: it turns your phone or computer into the remote for your LG smart TV with webOS, over your home Wi-Fi. It helps if you lost the remote, if its batteries died, or if you just want to type faster.',
    compat='LG smart TVs running webOS (most LG smart TV models since 2014). Works with LED, NanoCell, QNED and OLED TVs.',
    funciones=[
      ('All the buttons', 'D-pad, OK, Back, Home, volume, channels, mute and playback.'),
      ('Pointer like the Magic Remote (Pro)', 'Move the arrow around the screen with your finger, just like with the LG Magic Remote.'),
      ('Keyboard', 'Type in YouTube, Netflix or the TV browser with your phone keyboard.'),
      ('Apps and inputs (Pro)', 'Open your apps and switch to HDMI, live TV, AirPlay or Screen Share.'),
      ('Audio output (Pro)', 'Switch between the TV speakers and your soundbar.'),
      ('Turn on the TV', 'If it is off, Mando TV turns it on over the network and connects by itself.'),
    ],
    pasos=[
      'Connect your phone and the TV to the same Wi-Fi network.',
      'Open Mando TV: your LG TV shows up in the list on its own. Tap it.',
      'A prompt appears on the TV screen asking for permission. Accept it with your usual remote (first time only).',
    ],
    encender='Turn on "TV On With Mobile" (on some models it is called "Turn on via Wi-Fi"). You will find it under Settings, General or Connection, Mobile Device Settings. After that, when you tap the TV in Mando TV while it is off, the app asks if you want to turn it on and connects by itself.',
    faq=[
      ('Do I need the Magic Remote to use Mando TV?', 'Only the first time, to accept the permission prompt on the screen. After that you can use just your phone.'),
      ('Does Mando TV replace LG ThinQ?', 'To control the TV, yes: you do not need an LG account or to register the TV. Mando TV connects directly over your Wi-Fi.'),
      ('Can I turn on my LG TV from my phone?', 'Yes, if you turn on "TV On With Mobile" on the TV and you connected once while the TV was on.'),
    ],
    guias=['<a href="/en/guides/turn-on-lg-tv-with-phone/">How to turn on an LG TV with your phone</a>',
           '<a href="/en/guides/lost-lg-remote/">Lost your LG TV remote: how to use your phone</a>',
           '<a href="/en/guides/change-hdmi-input-without-remote/">Change the TV HDMI input without a remote</a>',
           '<a href="/en/guides/">All guides to control your TV with your phone</a>']),
  dict(clave='samsung', nombre='Samsung', color='#3d7bff',
    titulo='Samsung TV Remote App for Your Phone, Free | Mando TV',
    desc='Use your phone or PC as a Samsung TV remote for Tizen over Wi-Fi. Buttons, keyboard and power-on are free; touchpad and apps with Pro. No ads.',
    h1='Samsung TV Remote App for Your Phone',
    corto='Samsung',
    intro='Mando TV is a Samsung TV remote app: it turns your phone or computer into the remote for your Samsung smart TV, over your home Wi-Fi. You do not need a Samsung account or to register the TV.',
    compat='Samsung smart TVs running Tizen, 2016 models and newer (series such as Crystal UHD, QLED, Neo QLED, The Frame and OLED).',
    funciones=[
      ('All the buttons', 'D-pad, OK, Return, Home, volume, channels, mute and source.'),
      ('Touchpad (Pro)', 'Swipe your finger to move through the menus without hunting for arrows.'),
      ('Keyboard', 'Type searches and passwords with your phone keyboard.'),
      ('Apps (Pro)', 'Open Netflix, YouTube, Prime Video and your other apps with one tap.'),
      ('Turn on the TV', 'If it is off, Mando TV turns it on over the network and connects by itself.'),
      ('No account', 'It connects directly over your Wi-Fi, without going through the internet.'),
    ],
    pasos=[
      'Connect your phone and the TV to the same Wi-Fi network.',
      'Open Mando TV: your Samsung TV shows up in the list on its own. Tap it.',
      'The TV asks whether you allow the connection. Choose Allow with the remote (first time only).',
    ],
    encender='Turn on "Power On with Mobile" under Settings, General, Network, Expert Settings. After that, when you tap the TV in Mando TV while it is off, the app asks if you want to turn it on and connects by itself.',
    faq=[
      ('I denied the permission by mistake. What do I do?', 'On the TV go to Settings, General, External Device Manager, Device Connection Manager, and set Mando TV to allowed.'),
      ('Does Mando TV replace SmartThings?', 'To control the TV, yes, and without a Samsung account. Mando TV connects directly over your Wi-Fi.'),
      ('Does it work with older Samsung TVs?', 'It works with Samsung TVs running Tizen, 2016 and newer. Earlier models use a different system that we do not support yet.'),
    ],
    guias=[f'{es_link("samsung-lost")}',
           '<a href="/en/guides/change-hdmi-input-without-remote/">Change the TV HDMI input without a remote</a>',
           '<a href="/en/guides/">All guides to control your TV with your phone</a>']),
  dict(clave='roku', nombre='Roku', color='#a77bff',
    titulo='Roku Remote App for Your Phone, Free | Mando TV',
    desc='Use your phone or PC as a Roku remote for Roku TV or Roku players over Wi-Fi. Buttons, keyboard and power-on are free; channels and inputs with Pro.',
    h1='Roku Remote App for Your Phone',
    corto='Roku',
    intro='Mando TV is a Roku remote app: it turns your phone or computer into the remote for your Roku, over your home Wi-Fi. It works with Roku TV sets and with Roku players that plug into HDMI.',
    compat='Roku TV sets (TCL, Hisense, Philips, Sharp, JVC and others) and Roku players (Express, Streaming Stick, Ultra).',
    funciones=[
      ('All the buttons', 'D-pad, OK, Back, Home, volume, mute, replay and playback.'),
      ('Keyboard', 'Type searches in Roku channels with your phone keyboard.'),
      ('Channels (Pro)', 'Open Netflix, YouTube and your other Roku channels with one tap.'),
      ('Inputs (Pro)', 'On a Roku TV, switch to HDMI, antenna or AV from the app.'),
      ('Turn on the TV', 'On Roku TV sets with fast start, Mando TV turns them on from your phone.'),
      ('No pairing', 'Roku does not ask for a code: tap it in the list and you are in.'),
    ],
    pasos=[
      'Connect your phone and the Roku to the same Wi-Fi network.',
      'Open Mando TV: your Roku shows up in the list on its own. Tap it.',
      'If it does not connect, on the Roku go to Settings, System, Advanced system settings, Control by mobile apps, and set network access to Default or Permissive.',
    ],
    encender='On Roku TV sets, turn on "Fast TV start" under Settings, System, Power. Roku players connected to another TV cannot be turned on this way. After that, when you tap the TV in Mando TV while it is off, the app asks if you want to turn it on and connects by itself.',
    faq=[
      ('Does it work with the Roku Express or the Streaming Stick?', 'Yes. All Roku players and Roku TV sets are controlled the same way.'),
      ('Mando TV cannot find my Roku. What do I do?', 'Check that both are on the same Wi-Fi network and that "Control by mobile apps" on the Roku is not turned off. You can also add it by typing its IP address.'),
      ('Do I need a Roku account?', 'No. Mando TV connects directly over your Wi-Fi.'),
    ],
    guias=[es_link('roku-403'), es_link('roku-lost'),
           '<a href="/en/guides/">All guides to control your TV with your phone</a>']),
  dict(clave='android', nombre='Android TV and Google TV', color='#2fbf8f',
    titulo='Android TV Remote App for Your Phone | Mando TV',
    desc='Use your phone or PC as an Android TV remote (Sony, TCL, Xiaomi) over Wi-Fi. Buttons, keyboard and power-on are free; touchpad and apps with Pro.',
    h1='Android TV Remote App for Your Phone',
    corto='Android TV and Google TV',
    intro='Mando TV is an Android TV remote app: it turns your phone or computer into the remote for your Android TV or Google TV, over your home Wi-Fi. It also works from an iPhone and from Windows.',
    compat='TVs with Android TV or Google TV (Sony, TCL, Philips, Xiaomi, Hisense and others), Chromecast with Google TV, Google TV Streamer and Nvidia Shield.',
    funciones=[
      ('All the buttons', 'D-pad, OK, Back, Home, volume, mute and playback.'),
      ('Touchpad (Pro)', 'Swipe your finger to move quickly through the Google TV menus.'),
      ('Keyboard', 'Type searches and passwords with your phone keyboard.'),
      ('Apps (Pro)', 'Open YouTube, Netflix, Disney+ and your other apps with one tap.'),
      ('Turn on the TV', 'On models with power-on over the network, Mando TV turns the TV on and connects by itself.'),
      ('iPhone, Android and PC', 'It works the same from any phone or computer.'),
    ],
    pasos=[
      'Connect your phone and the TV to the same Wi-Fi network.',
      'Open Mando TV: your Android TV shows up in the list on its own. Tap it.',
      'The TV shows a 6-character code. Type it into Mando TV (first time only).',
    ],
    encender='It depends on the manufacturer. Look for "Wake on LAN", "Turn on over network" or "Remote start" in the network or power settings. Some models do not have it. After that, when you tap the TV in Mando TV while it is off, the app asks if you want to turn it on and connects by itself.',
    faq=[
      ('Does it work with Chromecast with Google TV?', 'Yes, it pairs with the 6-character code that appears on the screen.'),
      ('How is it different from the Google TV app?', 'Mando TV does not need a Google account, it also works from Windows, and it controls LG, Samsung and Roku TVs from the same app.'),
      ('The code does not show up on the screen. What do I do?', 'Close Mando TV, open it again and tap the TV once more. Check that the TV is not in a deep power-saving mode.'),
    ],
    guias=[es_link('androidtv-code'),
           '<a href="/en/guides/android-tv-without-remote/">Android TV without a remote: how to use your phone</a>',
           '<a href="/en/guides/">All guides to control your TV with your phone</a>']),
]


def otras_marcas(m):
    nombres = {'lg': 'LG', 'samsung': 'Samsung', 'roku': 'Roku', 'android': 'Android TV and Google TV'}
    return '\n'.join(f'          <li><a href="{en_url(k, BRANDS)}">{nombres[k]} remote app</a></li>' for k in ('lg', 'samsung', 'roku', 'android') if k != m['clave'])


def pagina_marca(m):
    e = html.escape
    es, en = '/' + BRANDS[m['clave']][0] + '/', '/' + BRANDS[m['clave']][1] + '/'
    url = URL + en
    ld = {"@context": "https://schema.org", "@graph": [
      {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Mando TV", "item": URL + "/en/"},
        {"@type": "ListItem", "position": 2, "name": m['h1'], "item": url}]},
      {"@type": "FAQPage", "inLanguage": "en", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in m['faq']]}]}
    funciones = '\n'.join(f'        <li><b>{e(t)}</b><span>{e(d)}</span></li>' for t, d in m['funciones'])
    pasos = '\n'.join(f'          <li>{e(p)}</li>' for p in m['pasos'])
    guias = '\n'.join(f'        <li>{g}</li>' for g in m['guias'])
    faq = '\n'.join(f'        <details><summary>{e(q)}</summary><p>{e(a)}</p></details>' for q, a in m['faq'])
    return (cabecera(m['titulo'], m['desc'], url, es, en, m['color'], 'website', ld) + f'''      <nav class="migas" aria-label="Breadcrumb"><a href="/en/">Mando TV</a> / <span>{e(m["corto"])}</span></nav>
      <h1>{e(m["h1"])}</h1>
      <p>{e(m["intro"])}</p>
      <div class="acciones">
        <a class="boton" href="#tiendas">Download free</a>
        <a class="boton claro" href="#como">How it connects</a>
      </div>
{tiendas_html('tiendas', 'Available in the stores')}
      <p class="nota">iPhone, iPad, Android and Windows. Free download, no ads. Pro is a one-time purchase, no subscription.</p>
    </div>
  </div>

  <main class="contenedor">
    <div class="documento">
      <h2 id="compatibles">Compatible TVs</h2>
      <p>{e(m["compat"])}</p>

      <h2 id="funciones">What you can do with your {e(m["corto"])}</h2>
      <ul class="lista-funciones">
{funciones}
      </ul>

      <h2 id="como">How to connect your {e(m["corto"])} to Mando TV</h2>
      <ol>
{pasos}
      </ol>

      <h2 id="encender">Turn on your {e(m["corto"])} from your phone</h2>
      <p>{e(m["encender"])}</p>

      <h2 id="preguntas">{e(m["corto"])} questions</h2>
      <div class="preguntas">
{faq}
      </div>

      <h2 id="guias">{e(m["corto"])} guides</h2>
      <ul>
{guias}
      </ul>

      <h2 id="otras">Other brands</h2>
      <p>Mando TV controls all of these brands from the same app:</p>
      <ul>
{otras_marcas(m)}
      </ul>
    </div>
  </main>

''' + pie(es))


# ---------------------------------------------------------------------------------------------------------------
# Guías
# ---------------------------------------------------------------------------------------------------------------
GUIAS = [
  dict(clave='lost-tv', corto='Lost TV remote',
    titulo='Lost Your TV Remote? What to Do Right Now',
    desc='Lost your TV remote? Turn the TV on with its button and use your phone as the remote. Steps for LG, Samsung, Roku and Android TV. Free, no ads.',
    h1='Lost Your TV Remote? What You Can Do',
    intro='A lost TV remote happens in every home: it disappears just when you want to watch something. The good news is that your phone can work as the remote, over your home Wi-Fi. Here is what to do, in order.',
    pasos=[
      'Turn on the TV with its physical button. It is almost always at the bottom center, or on the back near a corner. Sometimes it is a single button and sometimes a tiny joystick.',
      'Connect your phone to the same Wi-Fi network as the TV.',
      'Download Mando TV, which is free and does not ask for an account, and open it. Your TV shows up in the list on its own. Tap it.',
      'Accept the connection for your brand. On LG and Samsung the TV shows a prompt: accept it with the button or joystick on the TV itself. On Android TV and Google TV you type a 6-character code that appears on the screen. Roku does not ask for anything.',
      'Done. The arrows, OK, Back, Home, volume, channels and keyboard are free.',
      f'For next time, turn on power-on over the network in the TV settings (your brand guide is below) and you can turn the TV on from your phone without touching it.',
    ],
    extra=[
      ('Pick your brand guide', 'LG: [Lost your LG TV remote](/en/guides/lost-lg-remote/). Android TV and Google TV: [Android TV without a remote](/en/guides/android-tv-without-remote/). Samsung and Roku: see the Samsung and Roku remote app pages linked below.'),
      ('If the TV does not turn on with the button', 'Before you look for another remote, check that the cable is plugged in firmly and that the wall outlet has power. If the button on the TV does nothing, the problem is the TV and not the remote.'),
      ('If the remote just stopped working', 'Try new batteries. To check whether it still sends a signal, point it at your phone camera and press a button: on many phones you will see a purple light on the screen. If the light shows up and the TV does not respond, the sensor on the TV may be blocked.'),
      ('If you changed routers and the TV lost its Wi-Fi', 'Without a remote it is harder to connect the TV to the new network. The easiest way is to plug the TV into the router with a network cable. You can also create a Wi-Fi network with the same name and password as before: the TV usually reconnects to it by itself.'),
      ('What is free and what is Pro', 'Turning the TV on and off, arrows, OK, volume, channels, numbers and keyboard are free. The touchpad, the apps list, the inputs list, voice and routines are part of Mando TV Pro, a one-time purchase with no subscription.'),
    ],
    marcas=True,
    faq=[
      ('Can I turn on the TV with my phone if I never connected it before?', 'This first time, turn it on with the button on the TV. After you connect your phone and turn on power-on over the network in the TV settings, you can turn it on from the app.'),
      ('Do I need to buy a new remote?', 'Not necessarily. With Mando TV you get buttons, volume, keyboard and power-on for free. If you still prefer a physical one, look for the exact model of your TV.'),
      ('Does it work if the TV has no Wi-Fi?', 'No. The phone and the TV have to be on the same Wi-Fi network. A TV that is not a smart TV cannot be controlled with Mando TV.'),
    ]),
  dict(clave='lost-lg', corto='Lost LG TV remote',
    titulo='Lost Your LG TV Remote? Use Your Phone Instead',
    desc='No LG TV remote? Turn the TV on with its button, accept the prompt and use your phone as the remote over Wi-Fi. No LG account, no ads.',
    h1='Lost Your LG TV Remote? How to Use Your Phone',
    intro='If you lost your LG TV remote or the Magic Remote stopped working, your phone replaces it over Wi-Fi. It works on LG TVs with webOS, which is almost every LG smart TV since 2014. You do not need an LG account or the ThinQ app.',
    pasos=[
      'Turn on the TV with the button at the bottom, under the LG logo, or the one on the back. On many models it works as a joystick: press it to open the menu and move it to choose.',
      'Connect your phone to the same Wi-Fi network as the TV.',
      'Open Mando TV and tap your LG TV in the list.',
      'The TV shows a prompt asking for permission. Accept it with the joystick or the button on the TV. If you connected that phone before, it does not ask again.',
      'Done. The arrows, OK, Back, Home, volume, channels and keyboard are free. The pointer, the apps list and the inputs list are Pro features.',
      'With the app connected, go into Settings with the arrows and OK, and turn on "TV On With Mobile". The guide [How to turn on an LG TV with your phone](/en/guides/turn-on-lg-tv-with-phone/) shows where it is.',
    ],
    extra=[
      ('If the TV does not show the prompt', 'The permission may already be saved, or your phone may be on a different network. Check that both are on the same Wi-Fi network and that the VPN is off. If the TV does not show up in the list, see [Your phone cannot find the TV](/guias/el-celular-no-encuentra-el-tv/) (in Spanish).'),
      ('If the TV lost its Wi-Fi', 'Plug the TV into the router with a network cable and it will use it on its own. Or create a Wi-Fi network with the same name and password as before, because the TV usually reconnects to it by itself.'),
      ('If the TV is stuck on another input', 'On your phone, tap Inputs (a Pro feature) and pick the HDMI. More details in [Change the HDMI input on a TV without a remote](/en/guides/change-hdmi-input-without-remote/).'),
    ],
    marca=('/en/lg-tv-remote/', 'LG TV remote app'),
    faq=[
      ('Do I need the Magic Remote to use Mando TV?', 'You only need something to accept the prompt the first time, and the button or joystick on the TV itself works. After that you use just your phone.'),
      ('Do I need the LG ThinQ app?', 'No. Mando TV connects directly over your Wi-Fi and does not ask for an LG account.'),
      ('Can I turn my LG TV off and on from my phone?', 'Turning it off, yes. To turn it on you need to have turned on "TV On With Mobile" on the TV and to have connected once while the TV was on.'),
    ]),
  dict(clave='hdmi', corto='Change HDMI without a remote',
    titulo='Change HDMI Input Without a Remote (Samsung, LG, Roku)',
    desc='Change the HDMI input without a remote on Samsung, LG or Roku: use the button on the TV or your phone. Free to start, no ads.',
    h1='How to Change the HDMI Input on a TV Without a Remote',
    intro='The console or streaming player is ready, but the TV is stuck on another input and the remote is nowhere to be found. To change the HDMI input without a remote you have two options: the button on the TV itself, or your phone. Here are the steps for Samsung, LG and Roku.',
    pasos=[
      'Try the simplest thing first: turn on the console or player. If the TV has HDMI-CEC turned on (Anynet+ on Samsung, SIMPLINK on LG), it switches to that input by itself.',
      'If it does not switch, use the button on the TV itself, at the bottom center or on the back. On many Samsung and LG TVs it works as a joystick and opens a menu with Source or Inputs.',
      'Pick the input in that menu: HDMI 1, HDMI 2 and so on. The number is the port where the cable is plugged in.',
      'If you prefer your phone, connect it to the same Wi-Fi network, open Mando TV and tap your TV.',
      'On LG and Roku, tap Inputs (a Pro feature) and pick the HDMI. On Samsung, Inputs (a Pro feature) sends the TV Source key and you choose with the arrows and OK.',
      'You can also do it without Pro: with the arrows and OK, go to the inputs on the TV home screen. Depending on the brand and year, they are called Source, Connected Devices or Inputs. On a Roku TV they are the HDMI tiles on the home screen.',
    ],
    extra=[
      ('Samsung', 'If the menu from the button on the TV has no Source, open the home screen menu with your phone and look for Source or Connected Devices on the left. You control it with the arrows and OK in Mando TV, which are free.'),
      ('LG', 'Press the joystick on the TV and look for Inputs. With your phone, in Mando TV you can also open the inputs list (Pro) and tap the one you want.'),
      ('Roku TV', 'On the home screen there is a tile for each input, such as HDMI 1 or HDMI 2. Move with the arrows and go in with OK, for free.'),
      ('If it is a TV with Android TV or Google TV', 'In Mando TV the inputs list is not on Android TV yet. Use the inputs button on the TV itself, or reach them with the arrows and OK from the home screen. If you do not have a remote and want to connect, see [Android TV without a remote](/en/guides/android-tv-without-remote/).'),
      ('More help', 'If the TV does not even turn on or you do not know where to start, see [Lost your TV remote](/en/guides/lost-tv-remote/). For gaming on a console, the guide [Turn on the TV and switch to your console HDMI without the remote](/en/guides/turn-on-tv-console-hdmi-without-remote/) includes the HDMI-CEC trick.'),
    ],
    marcas=True,
    faq=[
      ('Is changing the HDMI input free?', 'The inputs list is part of Mando TV Pro, a one-time purchase with no subscription. For free you can turn the TV on, use the arrows, OK and volume, and reach the inputs from the TV menu.'),
      ('How do I know which HDMI to use?', 'Look at the HDMI ports on the TV: each one has a number. Use the one where the cable from your console or player is plugged in.'),
      ('What if the TV does not turn on?', 'Turn it on with its physical button. If you connected it before and turned on power-on over the network, you can also turn it on from your phone.'),
    ]),
  dict(clave='androidtv', corto='Android TV without a remote',
    titulo='Android TV Without a Remote: Use Your Phone',
    desc='No Android TV or Google TV remote? Connect your phone with the 6-character code on the screen. Free, no account, no ads.',
    h1='Android TV Without a Remote: How to Use Your Phone',
    intro='If you lost your Android TV or Google TV remote, or it ran out of batteries, your phone replaces it. The best part is that connecting does not need the remote: the TV shows a code on the screen and you type it on your phone. It works on Sony, TCL, Philips, Xiaomi and Hisense TVs with Android TV, Chromecast with Google TV and Nvidia Shield.',
    pasos=[
      'Turn on the TV with its physical button. It is almost always at the bottom center, or on the back near a corner.',
      'Connect your phone to the same Wi-Fi network as the TV.',
      'Download Mando TV, which is free and does not ask for a Google account, and open it. Tap your TV in the list.',
      'The TV shows a code of 6 letters and numbers. Type it on your phone and tap Pair. You do not need the remote for this.',
      'Now you can use the arrows, OK, Back, Home, volume, mute and keyboard. They are free. The touchpad and the apps list are Pro.',
      'To turn it on from your phone next time, look for "Wake on LAN", "Turn on over network" or "Remote start" in the TV network or power settings.',
    ],
    extra=[
      ('If your TV does not turn on from your phone', 'Not every Android TV has power-on over the network; it depends on the manufacturer and the model. If yours does not have it, turn it on with the button on the TV and continue from your phone. You can turn it off from the app.'),
      ('Chromecast with Google TV, Google TV Streamer and Shield', 'They connect the same way: same Wi-Fi network, tap the device in the list and type the code. If the TV shows another input, switch it to the HDMI where the device is plugged in, as explained in [Change the HDMI input on a TV without a remote](/en/guides/change-hdmi-input-without-remote/).'),
      ('If the code does not show up or it says it is wrong', 'Check that the TV is really on and not in standby. The code changes every time it is requested: only the latest one works. There are more details in [Android TV asks for a pairing code](/guias/android-tv-codigo-de-emparejamiento/) (in Spanish).'),
      ('Google app or Mando TV', 'Google has its own app that needs a Google account. Mando TV does not ask for an account, it also works from Windows, and it controls LG, Samsung and Roku TVs from the same app.'),
    ],
    marca=('/en/android-tv-remote/', 'Android TV remote app'),
    faq=[
      ('Do I need the remote to pair my phone?', 'No. The code appears on the TV screen and you type it on your phone. You only have to turn on the TV, with the button on the TV if needed.'),
      ('Does it work with a Hisense?', 'On Hisense TVs that have Android TV or Google TV, yes. Hisense TVs with another system are not compatible.'),
      ('Can I type with my phone keyboard?', 'Yes. The keyboard is free and works for searching in YouTube, Netflix and the rest of the apps.'),
    ]),
  dict(clave='lg-on', corto='Turn on LG TV with phone',
    titulo='How to Turn On an LG TV With Your Phone (Step by Step)',
    desc='Turn on your LG TV with your phone over Wi-Fi: enable "TV On With Mobile" on the TV and use Mando TV. Step by step, free, no ads.',
    h1='How to Turn On an LG TV With Your Phone',
    intro='You can turn on an LG TV with your phone, but first you have to switch on one setting on the TV. Once that is done, your phone turns on the LG TV over your Wi-Fi network, with no remote. It takes five minutes and you only do it once.',
    pasos=[
      'Connect your phone and the LG TV to the same Wi-Fi network.',
      'On the TV, open Settings and look for "TV On With Mobile". Depending on the model it is under General or Connection.',
      'Switch on "Turn on via Wi-Fi". If your TV is connected with a network cable, switch on the wired option instead.',
      'If your TV has "Quick Start+", turn it on too.',
      'With the TV on, open Mando TV on your phone and tap your LG TV in the list. Accept the prompt that appears on the screen. That is how the app learns to wake it up.',
      'Turn the TV off and test it: tap the TV in Mando TV and the app asks if you want to turn it on.',
    ],
    extra=[
      ('If it does not turn on', 'The TV must have been on the same Wi-Fi network when it was turned off. Check that the setting is still on and that your phone is on that same network. If you changed routers, connect once more with the TV on.'),
    ],
    marca=('/en/lg-tv-remote/', 'LG TV remote app'),
    faq=[
      ('Can I turn on the LG TV with my phone if I never connected it?', 'No. First you have to turn on "TV On With Mobile" on the TV and connect once with Mando TV while the TV is on.'),
      ('Do I need the LG ThinQ app?', 'No. Mando TV connects directly over your Wi-Fi and does not ask for an LG account.'),
      ('Does it work with mobile data?', 'No. The phone and the TV must be on the same Wi-Fi network.'),
    ]),
]

OTRAS_GUIAS = [
  ('lg-on', 'How to turn on an LG TV with your phone'),
  ('lost-tv', 'Lost your TV remote: what you can do'),
  ('lost-lg', 'Lost your LG TV remote: how to use your phone'),
  ('hdmi', 'Change the HDMI input on a TV without a remote'),
  ('androidtv', 'Android TV without a remote: how to use your phone'),
  ('console', 'How to turn on the TV and switch to your console HDMI without the remote'),
]


def pagina_guia(g):
    e = html.escape
    es, en = '/' + GUIDE_SLUGS[g['clave']][0] + '/', '/' + GUIDE_SLUGS[g['clave']][1] + '/'
    url = URL + en
    ld = {"@context": "https://schema.org", "@graph": [
      {"@type": "Article", "headline": g["h1"], "description": g["desc"], "inLanguage": "en",
       "datePublished": FECHA, "dateModified": FECHA, "mainEntityOfPage": url, "image": URL + "/social.png",
       "author": {"@id": URL + "/#org"}, "publisher": {"@id": URL + "/#org"}},
      ORG,
      {"@type": "HowTo", "name": g["h1"], "description": g["desc"], "inLanguage": "en",
       "step": [{"@type": "HowToStep", "position": n, "text": plano(p)} for n, p in enumerate(g["pasos"], 1)]},
      {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": URL + "/en/"},
        {"@type": "ListItem", "position": 2, "name": "Guides", "item": URL + "/en/guides/"},
        {"@type": "ListItem", "position": 3, "name": g["h1"], "item": url}]},
      {"@type": "FAQPage", "inLanguage": "en", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in g["faq"]]}]}
    pasos = '\n'.join(f'        <li>{fmt(p)}</li>' for p in g['pasos'])
    extra = '\n\n'.join(f'      <h2>{e(t)}</h2>\n      <p>{fmt(p)}</p>' for t, p in g['extra'])
    faq = '\n'.join(f'        <details><summary>{e(q)}</summary><p>{e(a)}</p></details>' for q, a in g['faq'])
    if g.get('marca'):
        marcas = f'<p>More details on the <a href="{g["marca"][0]}">{e(g["marca"][1])}</a> page.</p>'
    else:
        marcas = ('<p>More details by brand:</p>\n      <ul>\n' + '\n'.join(
          f'        <li><a href="{u}">{n}</a></li>' for u, n in PIE[:4]) + '\n      </ul>')
    otras = '\n'.join(f'        <li><a href="{en_url(k, GUIDE_SLUGS)}">{e(t)}</a></li>' for k, t in OTRAS_GUIAS if k != g['clave'])
    return (cabecera(g['titulo'], g['desc'], url, es, en, '#3d7bff', 'article', ld) + f'''      <nav class="migas" aria-label="Breadcrumb"><a href="/en/">Home</a> / <a href="/en/guides/">Guides</a> / <span>{e(g["corto"])}</span></nav>
      <h1>{e(g["h1"])}</h1>
      <p>{e(g["intro"])}</p>
      <div class="acciones">
        <a class="boton" href="#pasos">See the steps</a>
        <a class="boton claro" href="#mando-tv">Download free</a>
      </div>
    </div>
  </div>

  <main class="contenedor">
    <div class="documento">
      <h2 id="pasos">Step by step</h2>
      <ol>
{pasos}
      </ol>

{extra}

      <h2 id="mando-tv">Do it with Mando TV</h2>
      <p>Mando TV is a universal TV remote. Download it free, with no ads and no account. Pro is an optional one-time purchase, no subscription. For iPhone, iPad, Windows and Android:</p>
{tiendas_guia()}
      {marcas}

      <h2 id="preguntas">Frequently asked questions</h2>
      <div class="preguntas">
{faq}
      </div>

      <h2 id="otras">More guides</h2>
      <ul>
{otras}
        <li><a href="/en/guides/">All guides</a></li>
        <li><a href="/soporte.html">Help and support (in Spanish)</a></li>
      </ul>

      <h2 id="idiomas">This guide in other languages</h2>
      <ul>
        <li><a href="{es}" hreflang="es" lang="es">Español</a></li>
      </ul>
    </div>
  </main>

''' + pie(es))


def indice():
    e = html.escape
    url = URL + '/en/guides/'
    titulo = 'Guides: Control Your TV With Your Phone | Mando TV'
    desc = 'Step-by-step guides to use your phone or PC as a TV remote: turn on the TV, change the HDMI input and fix problems on Samsung, LG, Roku and Android TV.'
    descripciones = {
      'lg-on': next(g['desc'] for g in GUIAS if g['clave'] == 'lg-on'),
      'lost-tv': next(g['desc'] for g in GUIAS if g['clave'] == 'lost-tv'),
      'lost-lg': next(g['desc'] for g in GUIAS if g['clave'] == 'lost-lg'),
      'hdmi': next(g['desc'] for g in GUIAS if g['clave'] == 'hdmi'),
      'androidtv': next(g['desc'] for g in GUIAS if g['clave'] == 'androidtv'),
      'console': 'Launch day and no TV remote? Turn on your TV and switch to your PS5 or Xbox HDMI input from your phone. Free, no ads.',
    }
    ld = {"@context": "https://schema.org", "@graph": [
      ORG,
      {"@type": "CollectionPage", "name": titulo, "description": desc, "url": url, "inLanguage": "en",
       "publisher": {"@id": URL + "/#org"},
       "mainEntity": {"@type": "ItemList", "itemListElement": [
         {"@type": "ListItem", "position": n, "name": t, "url": URL + en_url(k, GUIDE_SLUGS)}
         for n, (k, t) in enumerate(OTRAS_GUIAS, 1)]}}]}
    lista = '\n'.join(f'        <li><a href="{en_url(k, GUIDE_SLUGS)}">{e(t)}</a>: {e(descripciones[k])}</li>' for k, t in OTRAS_GUIAS)
    marcas = '\n'.join(f'        <li><a href="{u}">{n}</a></li>' for u, n in PIE[:4])
    return (cabecera(titulo, desc, url, '/guias/', '/en/guides/', '#3d7bff', 'website', ld) + f'''      <nav class="migas" aria-label="Breadcrumb"><a href="/en/">Home</a> / <span>Guides</span></nav>
      <h1>Guides to Use Your Phone as a TV Remote</h1>
      <p>Simple steps to connect, turn on and fix the remote of your Samsung, LG, Roku or Android TV with Mando TV.</p>
    </div>
  </div>

  <main class="contenedor">
    <div class="documento">
      <h2 id="guias">All guides</h2>
      <ul>
{lista}
      </ul>

      <h2 id="marcas">TV remote app by brand</h2>
      <ul>
{marcas}
        <li><a href="/soporte.html">Help and support (in Spanish)</a></li>
      </ul>

      <h2 id="mas">More guides in Spanish</h2>
      <p>We also have guides in Spanish for other problems, such as {es_link('not-found')}, {es_link('roku-403')} and {es_link('androidtv-code')}. See <a href="/guias/" hreflang="es" lang="es">all the guides in Spanish</a>.</p>
    </div>
  </main>

''' + pie('/guias/'))


def escribir(ruta, texto):
    d = os.path.join(SITIO, *ruta.split('/'))
    os.makedirs(d, exist_ok=True)
    open(os.path.join(d, 'index.html'), 'w', encoding='utf-8', newline='\n').write(texto)


for m in MARCAS:
    escribir(BRANDS[m['clave']][1], pagina_marca(m))
    print('ok', BRANDS[m['clave']][1], len(m['titulo']), len(m['desc']))
escribir('en/guides', indice())
print('ok en/guides')
for g in GUIAS:
    escribir(GUIDE_SLUGS[g['clave']][1], pagina_guia(g))
    print('ok', GUIDE_SLUGS[g['clave']][1], len(g['titulo']), len(g['desc']))
