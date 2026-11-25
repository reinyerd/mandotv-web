# Pone en la portada de cada idioma la sección "See it in action" (#demo) de la portada en inglés, traducida:
# la demo animada del control (HTML y CSS con los textos de la app en ese idioma, la mueve demo.js), las dos capturas
# de App Store en ese idioma y, si ya existe media/mando-tv-in-action-<k>-720p.mp4, el video arriba.
# La sección en inglés (index.html de la raíz) es el molde: lo que cambie allí se copia al resto al volver a correrlo.
# Es idempotente: si la portada ya tiene #demo, la reemplaza; si no, la pone antes de la sección #funciones.
# Textos: herramientas/demo_textos.json (frases de la web) y los .arb de la app (nombres de los botones).
# Uso: python -I herramientas/demo_portadas.py <carpeta del sitio> <carpeta lib/l10n de la app> [idiomas...]
import json, os, re, sys

sys.dont_write_bytecode = True
SITIO, ARB = sys.argv[1], sys.argv[2]
AQUI = os.path.dirname(os.path.abspath(__file__))
TX = json.load(open(os.path.join(AQUI, 'demo_textos.json'), encoding='utf-8'))
ARB_DE = {'no': 'nb', 'zh-hant': 'zh_Hant'}
CLAVES_ARB = {'Modern': 'controlModoModerno', 'Classic': 'controlModoClasico', 'Home / Menu': 'controlTeclaInicio',
              'Back': 'controlTeclaAtras', 'Settings': 'controlTeclaAjustes', 'Inputs': 'controlTeclaEntradas',
              'Mute': 'controlTeclaSilencio', 'Exit': 'controlTeclaSalir', 'VOL': 'controlVol', 'CH': 'controlCanalAbrev'}
BLOQUE = re.compile(r'  <div class="contenedor">\n    <section id="demo".*?</section>\n  </div>\n\n', re.S)
FUNCIONES = '  <div class="contenedor">\n    <section id="funciones"'
FIGURA_VIDEO = re.compile(r'      <figure class="video-premium.*?</figure>\n', re.S)
SIN_VIDEO = re.compile(r'      <h2 class="titulo-seccion aparece" id="t-demo">.*?</h3>\n', re.S)


def esc(s):
    return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;')


def molde():
    t = open(os.path.join(SITIO, 'index.html'), encoding='utf-8').read()
    m = BLOQUE.search(t)
    if not m:
        sys.exit('No encuentro la sección #demo en index.html')
    return m.group(0)


def cambiar(t, viejo, nuevo, veces=None):
    n = t.count(viejo)
    if n == 0 or (veces is not None and n != veces):
        sys.exit(f'El molde cambió: "{viejo}" aparece {n} veces (esperaba {veces or "al menos 1"})')
    return t.replace(viejo, nuevo)


def seccion(k, base):
    w, en = TX['web'][k], TX['web']['en']
    arb = json.load(open(os.path.join(ARB, f'app_{ARB_DE.get(k, k)}.arb'), encoding='utf-8'))
    b = {ing: esc(arb[c]) for ing, c in CLAVES_ARB.items()}
    t = base
    hay_video = os.path.isfile(os.path.join(SITIO, 'media', f'mando-tv-in-action-{k}-720p.mp4'))
    if hay_video:
        t = cambiar(t, 'mando-tv-in-action-en', f'mando-tv-in-action-{k}')
        t = cambiar(t, f'data-play="{esc(en["video_play"])}"', f'data-play="{esc(w["video_play"])}"', 1)
        t = cambiar(t, f'>{esc(en["video_caption"])}<', f'>{esc(w["video_caption"])}<', 1)
        t = cambiar(t, f'>{esc(en["intro_con_video"])}<', f'>{esc(w["intro_con_video"])}<', 1)
        t = cambiar(t, f'>{esc(en["h2"])}<', f'>{esc(w["h2"])}<', 1)
        t = cambiar(t, f'>{esc(en["h3"])}<', f'>{esc(w["h3"])}<', 1)
    else:
        # Sin video, "See it in action" + su intro quedarían solos sobre el subtítulo: la sección parte directo con
        # "El control, paso a paso" como título. Cuando llegue el video, vuelve a la forma de la portada en inglés.
        t = FIGURA_VIDEO.sub('', t, count=1)
        t, n = SIN_VIDEO.subn(lambda m: f'      <h2 class="titulo-seccion aparece" id="t-demo">{esc(w["h3"])}</h2>\n', t, count=1)
        if n != 1:
            sys.exit('El molde cambió: no encuentro los títulos de #demo')
    t = cambiar(t, f'>{esc(en["demo_intro"])}<', f'>{esc(w["demo_intro"])}<', 1)
    aria_en = en['demo_aria'].replace('{inputs}', 'Inputs')
    t = cambiar(t, f'aria-label="{esc(aria_en)}"', f'aria-label="{esc(w["demo_aria"].replace("{inputs}", arb["controlTeclaEntradas"]))}"', 1)
    # Botones con el texto de la app. Los rótulos van siempre entre </svg> o <b>/<strong>/<small> y la etiqueta que cierra.
    for ing, loc in b.items():
        t = re.sub(r'(</svg>|<b>|<span>|<strong>|<small>)' + re.escape(ing) + r'(</span>|</b>|</strong>|</small>)',
                   lambda m: m.group(1) + loc + m.group(2), t)
    t = cambiar(t, '<span>Live TV</span>', f'<span>{esc(w["live_tv"])}</span>', 1)
    t = cambiar(t, f'data-paso="0">{esc(en["paso_volumen"])}<', f'data-paso="0">{esc(w["paso_volumen"])}<', 1)
    t = cambiar(t, f'data-paso="1">{esc(en["paso_flechas"])}<', f'data-paso="1">{esc(w["paso_flechas"])}<', 1)
    t = cambiar(t, 'data-paso="2">Inputs<', f'data-paso="2">{b["Inputs"]}<', 1)
    t = cambiar(t, f'aria-label="{esc(en["pausar"])}"',
                f'aria-label="{esc(w["pausar"])}" data-pausar="{esc(w["pausar"])}" data-reanudar="{esc(w["reanudar"])}"', 1)
    t = cambiar(t, f'aria-label="{esc(en["capturas_aria"])}"', f'aria-label="{esc(w["capturas_aria"])}"', 1)
    t = cambiar(t, '-en-', f'-{k}-')
    t = re.sub(r'(mando-tv-iphone-(?:remote|touchpad)-[\w-]+?\.webp)\?v=[\w-]+', r'\1', t)  # versionar.py la repone
    t = cambiar(t, f'alt="{esc(en["alt_control"])}"', f'alt="{esc(w["alt_control"])}"', 1)
    t = cambiar(t, f'alt="{esc(en["alt_touchpad"])}"', f'alt="{esc(w["alt_touchpad"])}"', 1)
    t = cambiar(t, f'<figcaption>{esc(en["cap_control"])}</figcaption>', f'<figcaption>{esc(w["cap_control"])}</figcaption>', 1)
    t = cambiar(t, f'<figcaption>{esc(en["cap_touchpad"])}</figcaption>', f'<figcaption>{esc(w["cap_touchpad"])}</figcaption>', 1)
    for img in (f'mando-tv-iphone-remote-{k}-600.webp', f'mando-tv-iphone-touchpad-{k}-600.webp'):
        if not os.path.isfile(os.path.join(SITIO, 'media', img)):
            sys.exit(f'Falta media/{img}')
    return t, hay_video


def scripts(t, hay_video):
    for js, falta in (('video.js', hay_video), ('demo.js', True)):
        if falta and f'src="/{js}' not in t:
            t = cambiar(t, '  <script src="/correo.js', f'  <script src="/{js}" defer></script>\n  <script src="/correo.js', 1)
    if not hay_video and 'src="/video.js' in t:
        t = re.sub(r'  <script src="/video\.js[^"]*" defer></script>\n', '', t)
    return t


def main():
    base = molde()
    idiomas = sys.argv[3:] or [k for k in TX['web'] if k != 'en']
    for k in idiomas:
        ruta = os.path.join(SITIO, k, 'index.html')
        t = open(ruta, encoding='utf-8').read()
        nuevo, hay_video = seccion(k, base)
        if BLOQUE.search(t):
            t = BLOQUE.sub(lambda m: nuevo, t, count=1)
        else:
            t = cambiar(t, FUNCIONES, nuevo + FUNCIONES, 1)
        t = scripts(t, hay_video)
        open(ruta, 'w', encoding='utf-8', newline='\n').write(t)
        print(k, 'con video' if hay_video else 'sin video')


main()
