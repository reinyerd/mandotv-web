# Genera las páginas en inglés (EE. UU.) de mandotv.app: marcas, índice de guías y guías principales.
# Textos escritos para búsquedas en inglés (no son traducción literal). La portada /en/ se mantiene a mano.
# Uso: python -I herramientas/generar_en.py <carpeta del sitio>
# Mismo patrón que generar_guias.py y generar_marcas.py; hreflang es + en (+ x-default = español) en las dos versiones
# (las páginas en español lo reciben de sus propios generadores).
import ast, html, json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.dont_write_bytecode = True
import idiomas_sitio

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

# Equivalencias es <-> en: salen de idiomas_sitio.py (carpeta en español, carpeta en inglés)
BRANDS = {k: (idiomas_sitio.carpeta(k, 'es'), idiomas_sitio.carpeta(k, 'en')) for k in ('lg', 'samsung', 'roku', 'android')}
GUIDE_SLUGS = {k: (idiomas_sitio.carpeta(k, 'es'), idiomas_sitio.carpeta(k, 'en')) for k in (
  'lost-tv', 'lost-lg', 'hdmi', 'androidtv', 'lg-on', 'console', 'samsung-lost', 'roku-lost', 'roku-403',
  'androidtv-code', 'not-found', 'wifi', 'pc')}
# Páginas sueltas: (ruta en español, ruta en inglés)
SOPORTE = ('/soporte.html', '/en/support.html')
PRIVACIDAD = ('/privacidad.html', '/en/privacy.html')


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
  ('/en/guides/samsung-tv-without-remote/', 'Samsung TV without a remote'),
  ('/en/guides/lost-roku-remote/', 'Lost Roku remote'),
  ('/en/guides/roku-remote-app-not-working/', 'Roku remote app not working'),
  ('/en/guides/android-tv-pairing-code/', 'Android TV pairing code'),
  ('/en/guides/phone-cant-find-tv/', "Phone can't find the TV"),
  ('/en/guides/connect-phone-to-tv-wifi/', 'Use your phone as a TV remote over Wi-Fi'),
  ('/en/guides/control-tv-from-pc/', 'Control your TV from a Windows PC'),
]


def pie_marcas():
    li = '\n'.join(f'        <li><a href="{u}">{n}</a></li>' for u, n in PIE)
    return f'      <ul class="marcas-enlaces pie-marcas" aria-label="Brands and guides">\n{li}\n      </ul>\n'


def hreflangs(clave):
    return idiomas_sitio.hreflangs(clave)


def fmt(t):
    """Escapa el texto y convierte [texto](/ruta/) en enlaces internos."""
    import re
    return re.sub(r'\[([^\]]+)\]\((/[^)\s]*)\)', lambda m: f'<a href="{m[2]}">{m[1]}</a>', html.escape(t))


def plano(t):
    import re
    return re.sub(r'\[([^\]]+)\]\((/[^)\s]*)\)', r'\1', t)


def cabecera(titulo, desc, url, clave, color, tipo, ld):
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
{hreflangs(clave)}  <meta property="og:site_name" content="Mando TV">
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
          <a href="/en/support.html">Help</a>
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


def pie(clave):
    otros = ''.join(f'          <a href="{r}" hreflang="{l}" lang="{l}">{n}</a>\n' for l, r, n in idiomas_sitio.enlaces_idiomas(clave, 'en'))
    return f'''  <footer class="pie">
    <div class="contenedor">
      <div class="pie-enlaces">
        <nav aria-label="Footer">
          <a href="/en/">Home</a>
          <a href="/en/support.html">Help</a>
          <a href="/en/privacy.html">Privacy</a>
          <a href="mailto:hola@mandotv.app">hola@mandotv.app</a>
{otros}          <button type="button" class="enlace-cookies" data-cookies>Cookies</button>
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
    guias=['<a href="/en/guides/samsung-tv-without-remote/">Samsung TV without the original remote: how to use your phone</a>',
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
    guias=['<a href="/en/guides/roku-remote-app-not-working/">Roku remote app not working (error 403)</a>',
           '<a href="/en/guides/lost-roku-remote/">Lost your Roku remote: how to use your phone</a>',
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
    guias=['<a href="/en/guides/android-tv-pairing-code/">Android TV asks for a pairing code: what to do</a>',
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
    return (cabecera(m['titulo'], m['desc'], url, m['clave'], m['color'], 'website', ld) + f'''      <nav class="migas" aria-label="Breadcrumb"><a href="/en/">Mando TV</a> / <span>{e(m["corto"])}</span></nav>
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

''' + pie(m['clave']))


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
      ('Pick your brand guide', 'LG: [Lost your LG TV remote](/en/guides/lost-lg-remote/). Android TV and Google TV: [Android TV without a remote](/en/guides/android-tv-without-remote/). Samsung: [Samsung TV without a remote](/en/guides/samsung-tv-without-remote/). Roku: [Lost your Roku remote](/en/guides/lost-roku-remote/).'),
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
      ('If the TV does not show the prompt', 'The permission may already be saved, or your phone may be on a different network. Check that both are on the same Wi-Fi network and that the VPN is off. If the TV does not show up in the list, see [Your phone cannot find the TV](/en/guides/phone-cant-find-tv/).'),
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
      ('If the code does not show up or it says it is wrong', 'Check that the TV is really on and not in standby. The code changes every time it is requested: only the latest one works. There are more details in [Android TV asks for a pairing code](/en/guides/android-tv-pairing-code/).'),
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
  dict(clave='samsung-lost', corto='Samsung TV without a remote',
    titulo='Lost Your Samsung TV Remote? Use Your Phone Instead',
    desc='Lost your Samsung TV remote or it stopped working? Use your phone as a Wi-Fi remote on Tizen TVs. Simple steps with Mando TV, free, no ads.',
    h1='Samsung TV Without the Original Remote: Use Your Phone',
    intro='If you lost your Samsung TV remote or it stopped working, you can use your phone as the remote over Wi-Fi. It works on Samsung TVs running Tizen, 2016 models and newer.',
    pasos=[
      'Turn on the TV with its physical button. On most models it is at the bottom or on the back, sometimes as a small joystick.',
      'Check that the TV is connected to your Wi-Fi and that your phone is on the same network.',
      'Open Mando TV on your phone. Your Samsung TV shows up in the list on its own. Tap it.',
      'The TV asks you to accept the connection. On most models you accept it with the physical buttons on the TV or with the joystick on the back.',
      'Done, you can now use your phone as the remote. The buttons and the keyboard are free; the touchpad and the apps are Pro features.',
      'To turn it on from your phone next time, go to Settings, General, Network, Expert Settings and turn on "Power On with Mobile".',
    ],
    extra=[
      ('If the TV does not ask for permission', 'The permission may already be saved, or the TV may be on a different Wi-Fi network. Close Mando TV and open it again with the TV on. If the TV is older than 2016, it uses a different system that is not supported yet.'),
      ('If you denied the permission by mistake', 'On the TV go to Settings, General, External Device Manager, Device Connection Manager, and set Mando TV to allowed. If your phone still cannot find the TV, see [Your phone cannot find the TV](/en/guides/phone-cant-find-tv/).'),
    ],
    marca=('/en/samsung-tv-remote/', 'Samsung TV remote app'),
    faq=[
      ('How do I accept the connection if I have no remote?', 'On most models you accept it with the physical buttons on the TV or with the joystick on the back. If your model has no buttons, write to hola@mandotv.app and we will help you.'),
      ('Does Mando TV ask for a Samsung account?', 'No. It connects directly over your Wi-Fi, with no Samsung account.'),
      ('Does it work with my older Samsung TV?', 'It works with Samsung TVs running Tizen, 2016 and newer.'),
    ]),
  dict(clave='wifi', corto='Phone as a TV remote over Wi-Fi',
    titulo='How to Use Your Phone as a TV Remote Over Wi-Fi',
    desc='Connect your phone to your TV over Wi-Fi and use it as a remote on Samsung, LG, Roku and Google TV. Steps for each brand with Mando TV. Free, no ads.',
    h1='How to Connect Your Phone to Your TV Over Wi-Fi as a Remote',
    intro='All you need is your phone and your TV on the same Wi-Fi network, plus a remote app. Mando TV finds your TV on its own and works with Samsung, LG, Roku, Google TV and Android TV.',
    pasos=[
      'Connect your phone and the TV to the same Wi-Fi network.',
      'Open Mando TV. Your TV shows up in the list on its own. Tap it.',
      'Accept the connection for your brand (the details for each one are below).',
      'Use the buttons or your phone keyboard to control the TV. The touchpad is a Pro feature.',
    ],
    extra=[
      ('Samsung', 'The TV asks if you allow the connection. Accept it on the screen the first time. It works with Tizen, 2016 and newer. To turn it on from your phone, turn on "Power On with Mobile" under Settings, General, Network, Expert Settings.'),
      ('LG', 'The TV shows a prompt asking for permission. Accept it the first time. To turn it on from your phone, look for "TV On With Mobile" in Settings and turn on "Turn on via Wi-Fi".'),
      ('Roku', 'Roku does not ask you to pair: tap it in the list and you are in. To turn it on, turn on "Fast TV start" under Settings, System, Power.'),
      ('Google TV and Android TV', 'The TV shows a code on the screen. Type it into Mando TV the first time. To turn it on, look for "Wake on LAN", "Turn on over network" or "Network wake-up" in the settings.'),
    ],
    marca=None,
    faq=[
      ('Do I need the internet to use my phone as a remote?', 'You need your phone and the TV on the same Wi-Fi network. Mando TV connects straight to your TV over that network.'),
      ('Why does my TV not show up in the list?', 'Check that the TV is on and that your phone is not using mobile data or a different Wi-Fi network. Some routers have a guest network that keeps devices apart.'),
      ('Can I use Mando TV from an iPhone or an Android phone?', 'Yes on iPhone and iPad: it is already on the App Store. It is also on Microsoft Store for Windows. Android is coming soon: you can join the free early access on Google Play.'),
    ]),
  dict(clave='pc', corto='Control your TV from a PC',
    titulo='How to Control Your TV From a Windows PC (Free)',
    desc='Use your Windows PC as a remote for your Samsung, LG, Roku or Google TV over Wi-Fi. Buttons and keyboard are free; apps and PC shortcuts with Pro.',
    h1='How to Control Your TV From a Windows PC',
    intro='If you spend the day in front of your computer, you do not need to look for the remote: Mando TV for Windows controls your Samsung, LG, Roku, Google TV or Android TV over your home Wi-Fi. It is handy for switching apps, turning up the volume or typing in YouTube with your PC keyboard.',
    pasos=[
      'Download Mando TV free from Microsoft Store on your Windows 10 or 11 computer.',
      'Check that the computer and the TV are on the same network (Wi-Fi or cable, but through the same router).',
      'Open Mando TV: your TV shows up in the list on its own. Tap or click it.',
      'Accept the connection on the TV screen the first time (on Google TV and Android TV, type the code the TV shows).',
      'Done: use the buttons or the keyboard to type in the TV search box. The touchpad is a Pro feature.',
    ],
    extra=[
      ('PC keyboard shortcuts (Pro)', 'With Mando TV Pro you control the TV with your computer keyboard: arrow keys to move around, Enter for OK, Backspace or Esc to go back, + and - for the volume, M to mute and Space to pause.'),
      ('Mini remote always on top (Pro)', 'Keep a small window with the remote always visible while you work or play on your PC.'),
    ],
    marca=None,
    faq=[
      ('Do I need a cable or Bluetooth to control the TV from my PC?', 'No. Mando TV connects over your home network: the PC and the TV only need to be on the same router.'),
      ('Does it work with any TV?', 'It works with Samsung TVs running Tizen (2016 and newer), LG with webOS, Roku, and Google TV or Android TV (Sony, TCL, Philips, Xiaomi and others).'),
      ('How much does it cost?', 'The buttons, the keyboard and power-on over the network are free and ad-free. Mando TV Pro is a one-time purchase, no subscription, for extras such as the touchpad, the apps, the PC keyboard shortcuts and the mini remote.'),
    ]),
  dict(clave='roku-403', corto='Roku remote app not working',
    titulo='Roku Remote App Not Working? Fix Error 403',
    desc='Your phone connects to the Roku but the buttons do nothing? Turn on "Control by mobile apps" on the Roku in 5 steps and use your phone as the remote again.',
    h1='Roku Remote App Not Working: How to Fix It',
    intro='If your phone finds the Roku and connects, but no button does anything, it is almost always a setting on the Roku itself that blocks remote apps. Recent Roku versions are more restricted by default. It takes a minute to fix from the Roku menu.',
    pasos=[
      'On the Roku, press Home and go to Settings.',
      'Open System and then Advanced system settings.',
      'Go into "Control by mobile apps". On some models it is called "External control".',
      'Under "Network access", choose Default or Permissive. If on your model it is just a switch, leave it on Enabled.',
      'Go back to Mando TV on your phone and tap your Roku. The buttons now respond.',
    ],
    extra=[
      ('How to tell if this is your problem', 'The sign is clear: your phone sees the Roku in the list and connects, but nothing happens when you tap a button. Inside, the Roku answers with error 403, which means "forbidden". Mando TV detects it when it connects and shows you these same steps on the screen.'),
      ('Default or Permissive, which one do I pick?', 'Default is enough: it accepts commands that come from your home network, which is what a remote needs. Permissive is more open and is only needed on unusual networks.'),
      ('If you do not have the Roku remote', 'When the setting is Disabled, it can only be changed with the physical Roku remote. Borrow one to change it once; after that you can use your phone for everything. See also [Lost your Roku remote](/en/guides/lost-roku-remote/).'),
    ],
    marca=('/en/roku-remote/', 'Roku remote app'),
    faq=[
      ('Why did my Roku stop responding if it used to work?', 'A Roku update can leave that setting more restricted. It is not a problem with your phone or your Wi-Fi: you just need to allow control by apps again.'),
      ('Does it work for Roku TV and for Roku players?', 'Yes. The setting is in the same menu on Roku players and on Roku TV sets.'),
      ('Is it safe to leave it on Default?', 'Yes. It only accepts commands from devices on your home network.'),
    ]),
  dict(clave='not-found', corto="Phone can't find the TV",
    titulo="Phone Can't Find Your TV? 6 Things to Check",
    desc="If the remote app can't find your TV or drops while connecting, check Wi-Fi, VPN and local network access. Steps for Samsung, LG, Roku and Android TV.",
    h1='Your Phone Cannot Find the TV: What to Check',
    intro='You open the remote app and the list is empty, or the TV shows up but the connection drops. It is almost always the network, not the TV. Check these points in order: the first one solves most cases.',
    pasos=[
      'Look at which Wi-Fi your phone is on and which one the TV is on. It has to be the same network, with the same name. A guest network will not work, because it keeps devices apart.',
      'Turn off the VPN on your phone, if you use one. With the VPN on, your phone goes out through another network and cannot see the devices in your home, or the connection drops after a few seconds.',
      'Turn off mobile data for a moment. Some phones switch from Wi-Fi to mobile data on their own when the signal is weak.',
      'Turn on the TV and wait until it finishes starting up. A TV that is off does not answer the search.',
      'On an iPhone, check that the app has Local Network permission: Settings > Privacy & Security > Local Network.',
      'If it still does not show up, add it by hand: in Mando TV tap "Add by IP" and type the IP address of the TV.',
    ],
    extra=[
      ('Where to find the IP address of the TV', 'It is in the TV network menu and changes a little by model. On LG: Settings, Network, Wi-Fi Connection, Advanced Wi-Fi Settings. On Samsung: Settings, General, Network, Network Status, IP Settings. On Roku: Settings, Network, About. On Android TV and Google TV: Settings, Network & Internet, then tap your network. It is a number like 192.168.1.86.'),
      ('If it shows up but the connection drops', 'When the connection drops after a few seconds, the cause is usually on the phone: a VPN, a switch to another Wi-Fi network or battery saver. Turn off the VPN, stay on the same Wi-Fi and try again.'),
      ('2.4 and 5 GHz Wi-Fi', 'It does not matter if your phone is on the 5 GHz network and the TV is on the 2.4 GHz one, as long as both come from the same router. If you have a range extender and the TV still does not show up, move your phone closer to the main router and try again.'),
    ],
    marca=None,
    faq=[
      ('Can I control the TV with mobile data?', 'No. The remote signal travels over your home Wi-Fi, so your phone and the TV must be on the same network.'),
      ('Why does it not work with the VPN on?', 'Because the VPN sends all of your phone traffic through another network and the phone can no longer see the devices in your home. Turn it off while you use the remote.'),
      ('Does Bluetooth or infrared work?', 'Mando TV uses Wi-Fi only. It does not need Bluetooth or an infrared blaster on your phone.'),
    ]),
  dict(clave='androidtv-code', corto='Android TV pairing code',
    titulo='Android TV Asks for a Pairing Code: What to Do',
    desc='Your Android TV or Google TV shows a 6-character code when you connect your phone. How to enter it and what to do if it does not show up or is wrong.',
    h1='Android TV Asks for a Pairing Code: What to Do',
    intro='The first time you connect your phone to an Android TV or Google TV, the TV shows a 6-character code on the screen. This is normal and happens only once: it makes sure nobody else can control your TV. Here is how to enter it and what to do if it does not show up.',
    pasos=[
      'Turn on the TV and leave the home screen in view.',
      'Open Mando TV on your phone, on the same Wi-Fi as the TV, and tap your TV in the list.',
      'Look at the TV screen: a code of 6 letters and numbers appears.',
      'Type it on your phone exactly as shown and tap Pair. The letters only go from A to F, so a round character is always the number zero.',
      'Done. The TV remembers your phone and does not ask for the code again.',
    ],
    extra=[
      ('If the code does not show up on the TV', 'Check that the TV is really on and not in standby, and that your phone is on the same Wi-Fi. Tap the TV on your phone again. If it still does not appear, restart the TV: unplug it for ten seconds, plug it back in and try again.'),
      ('If it says the code is wrong', 'The code changes every time it is requested. If you took a while or requested it twice, only the latest one on the screen works. Tap the TV on your phone again and type the new code.'),
      ('If the TV asks for the code again', 'This happens when the TV is factory reset or when you clear the app data on your phone. Pair again and it is saved. If you have no remote at all, see [Android TV without a remote](/en/guides/android-tv-without-remote/).'),
    ],
    marca=('/en/android-tv-remote/', 'Android TV remote app'),
    faq=[
      ('Which TVs use this code?', 'The ones with Android TV or Google TV: Sony, TCL, Philips, Xiaomi, Chromecast with Google TV and several more.'),
      ('Do I need a Google account on my phone?', 'No. The code on the screen is all you need.'),
      ('Is it safe?', 'Yes. The code proves you are in front of the TV: nobody can pair without seeing it on the screen.'),
    ]),
  dict(clave='roku-lost', corto='Lost Roku remote',
    titulo='Lost Your Roku Remote? Use Your Phone Over Wi-Fi',
    desc='Lost your Roku remote? Your phone replaces it over Wi-Fi. Simple steps, plus what to do if you changed routers and the Roku lost its connection.',
    h1='Lost Your Roku Remote: How to Use Your Phone',
    intro='If you lost your Roku remote or it stopped working, your phone replaces it, as long as the Roku is still connected to your Wi-Fi. And if you changed Wi-Fi or routers, there is a way out for that too.',
    pasos=[
      'Turn on the TV and leave the Roku plugged in. You do not need to touch anything on it.',
      'Connect your phone to the same Wi-Fi the Roku uses.',
      'Open Mando TV. The Roku shows up in the list on its own. Tap it.',
      'Use the arrows, OK, Home and Back like on your usual remote. The Roku does not ask for a code.',
      'If the buttons do nothing, the Roku is blocking control by apps: the guide [Roku remote app not working](/en/guides/roku-remote-app-not-working/) explains how to allow it.',
    ],
    extra=[
      ('If the Roku has no Wi-Fi (you changed routers or moved)', 'Without the remote you cannot get into the menu to set up the new network, but there is a trick: the Roku connects on its own to a network with the same name and password as the old one. On another phone, create a Wi-Fi hotspot with that exact name and password, connect the phone that has Mando TV to it and the Roku will show up in the list. From there go to Settings, Network and connect it to the new Wi-Fi.'),
      ('If it is a Roku TV', 'Roku TV sets have a physical button, almost always at the bottom center or on the back, that turns the TV on. That is enough to turn it on and continue with your phone.'),
      ('If you prefer to buy another remote', 'Make sure it is compatible with your model. Small Roku players hidden behind the TV need a remote that is not infrared, because infrared does not reach them.'),
    ],
    marca=('/en/roku-remote/', 'Roku remote app'),
    faq=[
      ('Can my phone turn on the Roku?', 'A plugged-in Roku player is always on. On a Roku TV, Mando TV turns it on over Wi-Fi when the TV has "Fast TV start" turned on under Settings, System, Power.'),
      ('What about the volume?', 'On a Roku TV your phone turns the volume up and down. On a Roku player connected over HDMI it depends on the TV: on many it works and on others it does not.'),
      ('Do I have to create an account?', 'No. Mando TV does not ask for an account and it also controls Samsung, LG and Android TV sets from the same app.'),
    ]),
]

OTRAS_GUIAS = [
  ('lg-on', 'How to turn on an LG TV with your phone'),
  ('lost-tv', 'Lost your TV remote: what you can do'),
  ('lost-lg', 'Lost your LG TV remote: how to use your phone'),
  ('hdmi', 'Change the HDMI input on a TV without a remote'),
  ('androidtv', 'Android TV without a remote: how to use your phone'),
  ('console', 'How to turn on the TV and switch to your console HDMI without the remote'),
  ('samsung-lost', 'Samsung TV without the original remote: how to use your phone'),
  ('roku-lost', 'Lost your Roku remote: how to use your phone'),
  ('roku-403', 'Roku remote app not working: fix error 403'),
  ('androidtv-code', 'Android TV asks for a pairing code: what to do'),
  ('not-found', 'Your phone cannot find the TV: what to check'),
  ('wifi', 'How to use your phone as a TV remote over Wi-Fi'),
  ('pc', 'How to control your TV from a Windows PC'),
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
    idiomas = '\n'.join(f'        <li><a href="{r}" hreflang="{l}" lang="{l}">{n}</a></li>' for l, r, n in idiomas_sitio.enlaces_idiomas(g['clave'], 'en'))
    return (cabecera(g['titulo'], g['desc'], url, g['clave'], '#3d7bff', 'article', ld) + f'''      <nav class="migas" aria-label="Breadcrumb"><a href="/en/">Home</a> / <a href="/en/guides/">Guides</a> / <span>{e(g["corto"])}</span></nav>
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
        <li><a href="/en/support.html">Help and support</a></li>
      </ul>

      <h2 id="idiomas">This guide in other languages</h2>
      <ul>
{idiomas}
      </ul>
    </div>
  </main>

''' + pie(g['clave']))


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
      **{k: next(g['desc'] for g in GUIAS if g['clave'] == k) for k in ('samsung-lost', 'roku-lost', 'roku-403', 'androidtv-code', 'not-found', 'wifi', 'pc')},
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
    return (cabecera(titulo, desc, url, 'guias', '#3d7bff', 'website', ld) + f'''      <nav class="migas" aria-label="Breadcrumb"><a href="/en/">Home</a> / <span>Guides</span></nav>
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
        <li><a href="/en/support.html">Help and support</a></li>
      </ul>

    </div>
  </main>

''' + pie('guias'))


# ---------------------------------------------------------------------------------------------------------------
# Ayuda y privacidad (traducción fiel de soporte.html y privacidad.html, que se mantienen a mano en español)
# ---------------------------------------------------------------------------------------------------------------
def migas_simple(nombre):
    return f'<nav class="migas" aria-label="Breadcrumb"><a href="/en/">Home</a> / <span>{nombre}</span></nav>'


def ld_simple(nombre, url):
    return {"@context": "https://schema.org", "@graph": [
      ORG,
      {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": URL + "/en/"},
        {"@type": "ListItem", "position": 2, "name": nombre, "item": url}]}]}


def pagina_soporte():
    url = URL + SOPORTE[1]
    titulo = 'Help: Connect and Turn On Your TV With Mando TV'
    desc = 'How to connect the Mando TV remote to your LG, Samsung, Roku or Android TV, how to turn it on from your phone and what to do if something fails.'
    guias = '\n'.join(f'        <li><a href="{en_url(k, GUIDE_SLUGS)}">{html.escape(t)}</a></li>' for k, t in OTRAS_GUIAS)
    return (cabecera(titulo, desc, url, 'soporte', '#e0457b', 'website', ld_simple('Help', url)) + f'''      {migas_simple('Help')}
      <h1>Help</h1>
      <p>The most common questions, in step order. If you do not find yours, write to us at <a href="mailto:hola@mandotv.app?subject=Help%20with%20Mando%20TV">hola@mandotv.app</a> and we will reply.</p>
    </div>
  </div>

  <main class="contenedor">
    <div class="documento">
      <h2 id="encontrar">Finding the TV</h2>
      <div class="preguntas">
        <details open><summary>My TV does not show up in the list</summary>
          <ol>
            <li>Check that your phone and the TV are on the same Wi-Fi network. If your router has a 2.4 GHz network and a 5 GHz network with different names, they sometimes cannot see each other.</li>
            <li>Make sure the TV is on.</li>
            <li>On an iPhone, check that Mando TV has the "Local Network" permission in Settings, Mando TV.</li>
            <li>If it still does not show up, tap the + button, choose the brand and type the IP address of the TV. You can see it in the network menu of the TV (for example, 192.168.1.50).</li>
          </ol>
        </details>
        <details><summary>Does it work with mobile data or away from home?</summary>
          <p>No. Mando TV talks to the TV inside your home network, so your phone has to be connected to that Wi-Fi.</p>
        </details>
      </div>

      <h2 id="conectar">Connecting for the first time</h2>
      <p>Full guides by brand: <a href="/en/lg-tv-remote/">LG</a>, <a href="/en/samsung-tv-remote/">Samsung</a>, <a href="/en/roku-remote/">Roku</a> and <a href="/en/android-tv-remote/">Android TV</a>.</p>
      <div class="preguntas">
        <details><summary>LG</summary>
          <p>When you tap the TV, a prompt appears on the TV screen asking for permission. Accept it with your usual remote. You only do this once.</p>
        </details>
        <details><summary>Samsung</summary>
          <p>The TV asks if you allow the Mando TV connection. Choose Allow with the remote. If you denied it by mistake, go to Settings, General, External Device Manager, Device Connection Manager, and change it to allowed.</p>
        </details>
        <details><summary>Roku</summary>
          <p>Roku does not ask for permission. If it does not connect, on the Roku go to Settings, System, Advanced system settings, Control by mobile apps, and leave network access on Default or Permissive.</p>
        </details>
        <details><summary>Android TV and Google TV</summary>
          <p>The TV shows a 6-character code. Type it into Mando TV exactly as it appears. It works for Sony, TCL, Philips, Xiaomi, Chromecast with Google TV and others with Android TV.</p>
        </details>
      </div>

      <h2 id="encender">Turning on the TV from the app</h2>
      <p>Mando TV turns on the TV over your home network. Two things are needed for that: you have connected at least once with the TV on, and the TV has power-on over the network turned on. The name of the setting changes by model; these are the most common:</p>
      <div class="preguntas">
        <details><summary>LG</summary>
          <p>Look for "TV On With Mobile" (or "Turn on via Wi-Fi") in Settings, General or Connection, Mobile Device Settings, and turn it on.</p>
        </details>
        <details><summary>Samsung</summary>
          <p>Turn on "Power On with Mobile" in Settings, General, Network, Expert Settings.</p>
        </details>
        <details><summary>Roku</summary>
          <p>On Roku TV sets, turn on "Fast TV start" in Settings, System, Power. Roku players connected to a TV cannot be turned on this way.</p>
        </details>
        <details><summary>Android TV and Google TV</summary>
          <p>It depends on the manufacturer. Look for "Wake on LAN", "Turn on over network" or "Remote start" in the network or power settings. Some models do not have it.</p>
        </details>
      </div>

      <h2 id="falla">If something fails</h2>
      <div class="preguntas">
        <details><summary>It disconnects or does not respond</summary>
          <ol>
            <li>On the remote screen, tap Reconnect.</li>
            <li>If that does not work, close Mando TV and open it again.</li>
            <li>If the TV changed its IP address, remove it from the list and add it again.</li>
          </ol>
        </details>
        <details><summary>How to send us an error report</summary>
          <ol>
            <li>In Mando TV, tap the Customize button (the sliders at the top).</li>
            <li>Tap Copy test report.</li>
            <li>Paste it into an email to hola@mandotv.app together with the brand and model of your TV.</li>
          </ol>
          <p>The report does not include passwords, codes or anything you type.</p>
        </details>
        <details><summary>I bought Pro and it does not show up</summary>
          <p>In Customize, tap Restore purchases, with the same store account you bought with. If it still does not show up, write to us.</p>
        </details>
      </div>

      <h2 id="guias">Step-by-step guides</h2>
      <p><a href="/en/guides/">See all the guides</a></p>
      <ul>
{guias}
      </ul>

      <h2 id="contacto">Still have questions?</h2>
      <p>Write to us at <a href="mailto:hola@mandotv.app?subject=Help%20with%20Mando%20TV">hola@mandotv.app</a>. Tell us the brand and model of your TV and which step you got stuck on.</p>
    </div>
  </main>

''' + pie('soporte'))


def pagina_privacidad():
    url = URL + PRIVACIDAD[1]
    titulo = 'Privacy Policy | Mando TV'
    desc = 'Mando TV collects no personal data: no accounts, no ads and no trackers. The app only talks to your TV inside your Wi-Fi network.'
    return (cabecera(titulo, desc, url, 'privacidad', '#e0457b', 'website', ld_simple('Privacy', url)) + f'''      {migas_simple('Privacy')}
      <h1>Privacy</h1>
      <p>In short: Mando TV does not collect your data. There are no accounts, no ads, no trackers and no servers of ours that store what you do.</p>
    </div>
  </div>

  <main class="contenedor">
    <article class="documento">
      <p class="fecha">Effective November 14, 2026. Last updated: November 15, 2026.</p>

      <h2>Who we are</h2>
      <p>Mando TV is an app to control your TV from your phone or computer. This policy explains what information the app uses and what it does with it. If you have questions, write to us at <a href="mailto:hola@mandotv.app">hola@mandotv.app</a>.</p>

      <h2>What data we collect</h2>
      <p>The app: none. The app does not send information about you or about how you use it to us or to third parties. It does not use analytics, advertising or tracking tools.</p>
      <p>This website: we measure visits in two ways, explained in the section <a href="#cookies">Cookies on this website</a>.</p>

      <h2>What the app stores on your device</h2>
      <p>To work, the app stores the following only on your phone or computer:</p>
      <ul>
        <li>The TVs you added: name, brand, IP address inside your network and network hardware address (MAC), which is used to turn it on.</li>
        <li>The connection keys that each TV hands over when you accept the permission. They are stored encrypted in the secure storage of the system (Keychain on iPhone and Mac, Keystore on Android, protected storage on Windows).</li>
        <li>Your preferences: light or dark theme, background color, vibration and type of remote.</li>
        <li>If you use the Pro features: your favorite apps, your routines and your latest YouTube searches (you can delete them from the app).</li>
      </ul>
      <p>If you delete the app, all of this is deleted with it.</p>

      <h2>Who the app talks to</h2>
      <p>With your TVs, inside your home Wi-Fi network. To find them, the app searches your local network; that is why on an iPhone it asks for the "Local Network" permission. The text you type with the app keyboard goes straight to the TV and is not stored.</p>
      <p>In addition, when it opens, the app downloads a small public file from this website (mandotv.app/app/config.json) to find out whether there is a new version you should install and which features belong to Mando TV Pro. It is a download, like opening a page: the app does not send your data, your TVs or what you do. It only states the app version and the system (for example, Android), so it can show you the right notice. If you have no internet, the app keeps working with the last file it downloaded; if more than 30 days pass without being able to download it, it will ask you to connect to the internet for a moment.</p>

      <h2>Microphone and voice</h2>
      <p>Voice search uses the microphone only while you tap the speak button. What you say is converted to text by the speech recognition of your system: Apple on iPhone and Mac, Google on Android and Microsoft on Windows, under their own privacy policies. Mando TV does not record or store the audio, and the resulting text goes straight to your TV, just like what you type with the keyboard.</p>

      <h2>Test report</h2>
      <p>The app has a "Copy test report" button to help us fix errors. The report is kept only in the memory of the app while it is open and is never sent on its own: you decide whether to copy it and share it. It does not include connection keys, pairing codes or anything you type; only the steps the app took, such as searching, connecting and the errors.</p>

      <h2 id="cookies">Cookies on this website</h2>
      <p>This applies only to the mandotv.app website, not to the app.</p>
      <h3>No cookies, always</h3>
      <p>We count visits anonymously with Cloudflare Web Analytics: how many people visit, which pages they read and from which country. It does not use cookies, it does not use your IP address to identify you and it does not follow what you do on other sites.</p>
      <h3>With cookies, only if you accept</h3>
      <p>If you tap "Accept" on the cookie notice, we turn on Google Analytics (from Google LLC) to better understand how the website is used: page views, time on the page, device type, approximate city and where you came from. To do this it stores the _ga and _ga_* cookies in your browser for up to 2 years. Google may process this data on servers outside Chile. We turned off the advertising features and Google Signals, and we do not use this data to show you ads.</p>
      <p>If you tap "Decline" or choose nothing, Google Analytics is not loaded and no cookie is stored. You can change your decision at any time with the "Cookies" button at the bottom of every page; if you withdraw permission, we delete those cookies.</p>
      <p>Your choice is stored in your browser (local storage, not sent to anyone) so that we do not ask you again.</p>

      <h2>Purchases</h2>
      <p>If you buy Mando TV Pro, the payment is processed by the app store (App Store, Google Play or Microsoft Store). We do not receive or store your card details. The store only confirms to the app that the purchase exists.</p>

      <h2>Emails you send us</h2>
      <p>If you write to us at <a href="mailto:hola@mandotv.app">hola@mandotv.app</a>, we use your email address and what you tell us only to reply to you. We do not share it or use it for advertising. You can ask us to delete your messages at any time.</p>

      <h2>Children</h2>
      <p>The app does not collect data from anyone, including children.</p>

      <h2>Changes to this policy</h2>
      <p>If one day what the app does with your data changes, we will update this page and the date above before the change reaches the app.</p>
    </article>
  </main>

''' + pie('privacidad'))


def escribir_archivo(ruta, texto):
    destino = os.path.join(SITIO, *ruta.strip('/').split('/'))
    open(destino, 'w', encoding='utf-8', newline='\n').write(texto)


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
escribir_archivo(SOPORTE[1], pagina_soporte())
print('ok', SOPORTE[1])
escribir_archivo(PRIVACIDAD[1], pagina_privacidad())
print('ok', PRIVACIDAD[1])
