# Pone en las guías traducidas el mismo video que tiene su gemela en inglés, igual que en inglés:
#   lost-tv  -> Short vertical "Lost your TV remote?" del idioma (media/lost-your-tv-remote-short-<k>-720p.mp4)
#   windows  -> "Mando TV in action" del idioma (media/mando-tv-in-action-<k>-720p.mp4)
# Bloque antes de "<h2 id="pasos">", enlace a YouTube del mismo idioma bajo el video, script /video.js y VideoObject en
# el JSON-LD (título y descripción de YouTube de ese idioma). Idempotente: si ya está, lo reemplaza.
# Correr después de los generadores (generar_guias.py, generar_idiomas.py) y antes de pie_firma.py / versionar.py.
# Uso: python -I -X utf8 herramientas/video_guias.py <carpeta del sitio> [idiomas...]
import html, json, os, re, sys

sys.dont_write_bytecode = True
SITIO = sys.argv[1]
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import idiomas_sitio  # noqa: E402

URL = 'https://mandotv.app'
TX = json.load(open(os.path.join(AQUI, 'video_guias_textos.json'), encoding='utf-8'))['web']
DEMO = json.load(open(os.path.join(AQUI, 'demo_textos.json'), encoding='utf-8'))['web']
VIDEOS_TEXTOS = os.environ.get('MANDOTV_VIDEOS_TEXTOS', '')  # carpeta con los textos de YouTube de cada idioma
# Carpeta web -> archivo de textos de YouTube del estudio de video
YT_TXT = {'no': 'nb', 'zh-hant': 'zh_Hant'}
# Claves de PAGINAS por carpeta web
CLAVE = {'no': 'nb'}
# IDs de YouTube (canal @mandotvapp). Largos = demo_portadas.YT; Shorts "Lost your remote?" por idioma.
SHORT = {'en': 'HVcCFZlNtcI', 'es': 'IWFOq_glG6M', 'pt': 'UqQn4NL8G7g', 'fr': 'QXKAcXIf7rk', 'de': 'mqplC-stBto',
         'it': 'SmbVlRbAwgs', 'nl': 'PyqzJvzlRFg', 'ja': 'U4hJv6CAdvE', 'ko': 'SUtuJRWsc9M', 'sv': '53bmpc1ThWs',
         'da': 'iwRkJvI7leo', 'no': '6Nq9-iqfCuQ', 'fi': 'DaTlvK-FKKc', 'pl': 'oeXV91CxbD0', 'tr': 'OcykYpDMp8Q',
         'ar': 'PVEBUaxFduU', 'he': 'cEbWwf8Ny0s', 'cs': 'Ee8SNcGAto4', 'sk': 'EKLOCi8T-oI', 'ro': 'XRl_7uxHD18',
         'hu': 'l96iw84of3o', 'el': 'UWWQ4xOHxhc', 'uk': '2zD1fbS0JyE', 'hi': 'eoBQekdxpj8', 'th': 'cVO-E75ANrU',
         'vi': '90UMOxelX74', 'id': '9W1nicv761s', 'ms': '4Al9kRCF1wU', 'zh': 'k1wu0H95zNQ', 'zh-hant': 'n23UbXMnU5I'}
LARGO = {'en': 'RyhvFz0ZUDk', 'es': 'Q_xBRIiufgk', 'ar': 'Vxk8IQPLSWg', 'de': 'AhRW1BrGioA', 'el': 'x5vlufspkpI',
         'fr': 'XUnpE7703os', 'hu': 'WuKjH4Euzj8', 'it': '5Ss8KlwbeG4', 'ja': 'csRLl6Rj2lc', 'ko': 'WrpGsXpAN2c',
         'ms': '_rR1d8fcjvs', 'no': 'km_ohKVyhnk', 'nl': 'yh7euESWfdU', 'pl': 'VKcvvg1wkKA', 'pt': 'pUOjCuRVeLU',
         'ro': 'lqmRLLTy5Hc', 'sk': 'JL63mTr_e4w', 'sv': 'awzZLvfmWck', 'th': 'WSd4Yt_zbdU', 'tr': 'RrUpAIV6HOk',
         'uk': 'Db0iqUvaiCw', 'vi': '0V149Qm08Sw', 'zh': 'To1FTqE888E', 'zh-hant': 'titOlDxNBQY', 'cs': 'r8Ry2sSFprs',
         'da': 'Sw6PfIEHJXA', 'fi': 'wy8CNHwThao', 'he': 'z1DkNeGVCVU', 'hi': 'I1gihsq_FXE', 'id': 'pj6gauxMMXk'}

BLOQUE_VIEJO = re.compile(r'      <h2 id="video">.*?<script src="/video\.js[^"]*" defer></script>\n\n', re.S)
PASOS = '      <h2 id="pasos">'
LD = re.compile(r'<script type="application/ld\+json">(.*?)</script>', re.S)


def e(s):
    return html.escape(s, quote=True)


def archivo(ruta):
    p = os.path.join(SITIO, ruta)
    return p if ruta.endswith('.html') else os.path.join(p, 'index.html')


def poner(k, clave, t):
    w, d = TX[k], DEMO[k]
    yt = json.load(open(os.path.join(VIDEOS_TEXTOS, YT_TXT.get(k, k) + '.json'), encoding='utf-8'))
    if clave == 'lost-tv':
        vid, base, ancho, alto, clase = SHORT[k], f'lost-your-tv-remote-short-{k}', 720, 1280, 'guia-video vertical'
        titulo, texto, boton, dur = w['short_h2'], w['short_caption'], d['video_play'].replace('0:25', '0:15'), 'PT15S'
        nombre, desc, fecha = yt['yt_short_titulo'], yt['yt_short_desc'], '2026-11-25T19:00:00-03:00'
        if '0:15' not in boton:
            sys.exit(f'{k}: el botón no tiene 0:25 para cambiar: {d["video_play"]}')
    else:
        vid, base, ancho, alto, clase = LARGO[k], f'mando-tv-in-action-{k}', 1280, 720, 'guia-video'
        titulo, texto, boton, dur = d['h2'], w['win_caption'], d['video_play'], 'PT25S'
        nombre, desc, fecha = yt['yt_accion_titulo'], yt['yt_accion_desc'], '2026-11-25T19:00:00-03:00'
    for f in (f'{base}-720p.mp4', f'{base}.webp', f'{base}.jpg'):
        if not os.path.isfile(os.path.join(SITIO, 'media', f)):
            sys.exit(f'Falta media/{f}')
    bloque = f'''      <h2 id="video">{e(titulo)}</h2>
      <figure class="{clase}">
        <div class="video-marco" data-play="{e(boton)}">
          <video controls muted playsinline preload="none" loading="lazy" width="{ancho}" height="{alto}" poster="/media/{base}.webp" aria-describedby="video-texto">
            <source src="/media/{base}-720p.mp4" type="video/mp4">
          </video>
        </div>
        <figcaption id="video-texto">{e(texto)}<span class="video-yt"> · <a href="https://www.youtube.com/watch?v={vid}" target="_blank" rel="noopener">YouTube</a></span></figcaption>
      </figure>
      <script src="/video.js" defer></script>

'''
    t = BLOQUE_VIEJO.sub('', t)
    if t.count(PASOS) != 1:
        sys.exit(f'{k} {clave}: no encuentro un único {PASOS}')
    t = t.replace(PASOS, bloque + PASOS, 1)
    m = LD.search(t)
    ld = json.loads(m.group(1))
    url = ld['@graph'][0]['mainEntityOfPage']
    lang = re.search(r'<html lang="([^"]+)"', t).group(1)
    ld['@graph'] = [x for x in ld['@graph'] if x.get('@type') != 'VideoObject']
    ld['@graph'].append({"@type": "VideoObject", "@id": url + "#video", "name": nombre, "description": desc,
                         "thumbnailUrl": f"{URL}/media/{base}.jpg", "uploadDate": fecha, "duration": dur,
                         "contentUrl": f"{URL}/media/{base}-720p.mp4", "embedUrl": f"https://www.youtube.com/embed/{vid}",
                         "url": f"https://www.youtube.com/watch?v={vid}",
                         "encodingFormat": "video/mp4", "inLanguage": lang, "publisher": {"@id": URL + "/#org"}})
    nuevo = json.dumps(ld, ensure_ascii=False)
    return t[:m.start(1)] + nuevo + t[m.end(1):]


def main():
    idiomas = sys.argv[2:] or [k for k in TX if k != 'en']
    for k in idiomas:
        for clave in ('lost-tv', 'windows'):
            ruta = archivo(idiomas_sitio.PAGINAS[clave][CLAVE.get(k, k)])
            t = open(ruta, encoding='utf-8').read()
            open(ruta, 'w', encoding='utf-8', newline='\n').write(poner(k, clave, t))
        print(k, 'ok')


main()
