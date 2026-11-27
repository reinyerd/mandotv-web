r"""Revisión SEO de mandotv.app con las reglas que revisa Site Scan de Bing Webmaster Tools. Correr antes de publicar.

Lee este repositorio para todas las URL de sitemap.xml (título, meta description, H1, idioma, canónica, hreflang de ida
y vuelta, datos estructurados, imágenes sin alt...) y, con --vivo, pide cada URL publicada para ver su código de
respuesta. Solo lee: no cambia nada. Sale con código 1 si hay títulos o descripciones largos.
Uso: python -I herramientas/escaneo_seo.py [--vivo] [--estricto]
  --estricto: avisa desde 151 caracteres en la descripción y 66 en el título (nuestro tope al escribir), en vez de
  los 160 y 70 de Bing.
Los avisos de "corto" en chino (zh, zh-hant) son falsos positivos: en chino cada carácter dice más.
Nació el 26-nov-2026.
"""
import concurrent.futures
import json
import os
import re
import sys
import urllib.error
import urllib.request
from collections import Counter, defaultdict
from html import unescape
from urllib.parse import urlparse

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = 'https://mandotv.app'
import tempfile
SALIDA = os.path.join(tempfile.gettempdir(), 'mandotv_escaneo_seo.json')
TOPE_DESC, TOPE_TIT = (150, 65) if '--estricto' in sys.argv else (160, 70)
sys.stdout.reconfigure(encoding='utf-8')

sitemap = open(os.path.join(RAIZ, 'sitemap.xml'), encoding='utf-8').read()
URLS = re.findall(r'<loc>\s*([^<\s]+)\s*</loc>', sitemap)


def archivo_de(url):
    p = urlparse(url).path
    if p.endswith('/'):
        p += 'index.html'
    f = os.path.join(RAIZ, p.lstrip('/').replace('/', os.sep))
    if os.path.isfile(f):
        return f
    g = os.path.join(f, 'index.html')
    return g if os.path.isfile(g) else None


def atributo(etiqueta, nombre):
    m = re.search(r'\b' + nombre + r'\s*=\s*("([^"]*)"|\'([^\']*)\'|([^\s>]+))', etiqueta, re.I)
    if not m:
        return None
    return unescape(m.group(2) if m.group(2) is not None else m.group(3) if m.group(3) is not None else m.group(4))


def texto(html):
    return re.sub(r'\s+', ' ', unescape(re.sub(r'<[^>]+>', ' ', html))).strip()


problemas = defaultdict(list)   # regla -> [url]
detalle = {}                    # url -> datos
titulos, descripciones = defaultdict(list), defaultdict(list)
alternos = {}                   # url -> {hreflang: href}

for url in URLS:
    f = archivo_de(url)
    if not f:
        problemas['en el sitemap pero sin archivo en el repo'].append(url)
        continue
    raw = open(f, encoding='utf-8', errors='replace').read()
    cuerpo = re.sub(r'<!--.*?-->', '', raw, flags=re.S)
    sin_script = re.sub(r'<(script|style|noscript|template)\b.*?</\1>', '', cuerpo, flags=re.S | re.I)
    cabeza = (re.search(r'<head\b.*?</head>', cuerpo, re.S | re.I) or re.search(r'.*', cuerpo, re.S)).group(0)
    d = {'bytes': len(raw.encode('utf-8'))}

    ts = [texto(t) for t in re.findall(r'<title\b[^>]*>(.*?)</title>', cabeza, re.S | re.I)]
    d['titulo'] = ts[0] if ts else ''
    if not ts or not ts[0]:
        problemas['sin título'].append(url)
    elif len(ts) > 1:
        problemas['más de un título'].append(url)
    if ts and ts[0]:
        titulos[ts[0]].append(url)
        n = len(ts[0])
        if n > TOPE_TIT:
            problemas['título largo (más de %d caracteres)' % TOPE_TIT].append(url)
        elif n < 15:
            problemas['título corto (menos de 15 caracteres)'].append(url)

    metas = re.findall(r'<meta\b[^>]*>', cabeza, re.I)
    descs = [atributo(m, 'content') or '' for m in metas if (atributo(m, 'name') or '').lower() == 'description']
    d['descripcion'] = descs[0] if descs else ''
    if not descs or not descs[0].strip():
        problemas['sin meta description'].append(url)
    elif len(descs) > 1:
        problemas['más de una meta description'].append(url)
    if descs and descs[0].strip():
        descripciones[descs[0].strip()].append(url)
        n = len(descs[0].strip())
        if n > TOPE_DESC:
            problemas['meta description larga (más de %d caracteres)' % TOPE_DESC].append(url)
        elif n < 50:
            problemas['meta description corta (menos de 50 caracteres)'].append(url)

    robots = ' '.join((atributo(m, 'content') or '') for m in metas if (atributo(m, 'name') or '').lower() in ('robots', 'bingbot', 'googlebot')).lower()
    if 'noindex' in robots:
        problemas['noindex en una página del sitemap'].append(url)
    if any((atributo(m, 'http-equiv') or '').lower() == 'refresh' for m in metas):
        problemas['meta refresh'].append(url)
    if sum(1 for m in metas if (atributo(m, 'name') or '').lower() == 'viewport') == 0:
        problemas['sin meta viewport'].append(url)

    html_tag = re.search(r'<html\b[^>]*>', cuerpo, re.I)
    lang = atributo(html_tag.group(0), 'lang') if html_tag else None
    d['lang'] = lang or ''
    if not lang:
        problemas['sin idioma en <html lang>'].append(url)

    h1 = re.findall(r'<h1\b[^>]*>(.*?)</h1>', sin_script, re.S | re.I)
    if not h1:
        problemas['sin H1'].append(url)
    elif len(h1) > 1:
        problemas['más de un H1'].append(url)
    elif not texto(h1[0]):
        problemas['H1 vacío'].append(url)

    imgs = re.findall(r'<img\b[^>]*>', sin_script, re.I)
    sin_alt = [i for i in imgs if not (atributo(i, 'alt') or '').strip()]
    if sin_alt:
        problemas['imágenes sin texto alternativo'].append(url)
        d['img_sin_alt'] = [(atributo(i, 'src') or '')[:80] for i in sin_alt[:3]]

    enlaces = re.findall(r'<link\b[^>]*>', cabeza, re.I)
    canon = [atributo(e, 'href') for e in enlaces if (atributo(e, 'rel') or '').lower() == 'canonical']
    if not canon:
        problemas['sin canónica'].append(url)
    elif len(canon) > 1:
        problemas['más de una canónica'].append(url)
    elif canon[0] != url:
        problemas['la canónica apunta a otra URL'].append(url)
        d['canonica'] = canon[0]

    alt = {}
    for e in enlaces:
        if (atributo(e, 'rel') or '').lower() == 'alternate' and atributo(e, 'hreflang'):
            alt[atributo(e, 'hreflang')] = atributo(e, 'href')
    alternos[url] = alt
    if not alt:
        problemas['sin hreflang'].append(url)
    else:
        if 'x-default' not in alt:
            problemas['hreflang sin x-default'].append(url)
        if url not in alt.values():
            problemas['hreflang no se nombra a sí misma'].append(url)

    if d['bytes'] > 125 * 1024:
        problemas['HTML de más de 125 KB'].append(url)
    if len(texto(sin_script)) < 400:
        problemas['muy poco texto (menos de 400 caracteres)'].append(url)
    if not re.search(r'<script\b[^>]*type\s*=\s*["\']application/ld\+json', cuerpo, re.I):
        problemas['sin datos estructurados'].append(url)
    detalle[url] = d

en_sitemap = set(URLS)
for url, alt in alternos.items():
    for codigo, destino in alt.items():
        if destino not in en_sitemap:
            problemas['hreflang apunta a una URL que no está en el sitemap'].append(url)
            break
    else:
        for codigo, destino in alt.items():
            if destino != url and url not in alternos.get(destino, {}).values():
                problemas['hreflang sin enlace de vuelta'].append(url)
                break

for t, us in titulos.items():
    if len(us) > 1:
        problemas['título repetido en varias páginas'].extend(us)
for t, us in descripciones.items():
    if len(us) > 1:
        problemas['meta description repetida en varias páginas'].extend(us)

vivo = {}
if '--vivo' in sys.argv:
    class SinRedirigir(urllib.request.HTTPRedirectHandler):
        def redirect_request(self, *a, **k):
            return None
    abridor = urllib.request.build_opener(SinRedirigir)

    def pedir(u):
        pet = urllib.request.Request(u, method='GET', headers={'User-Agent': 'Mozilla/5.0 (compatible; escaneo-propio)'})
        for _ in range(2):
            try:
                with abridor.open(pet, timeout=25) as r:
                    return u, r.status, r.headers.get('Location', ''), r.headers.get('X-Robots-Tag', '')
            except urllib.error.HTTPError as e:
                return u, e.code, e.headers.get('Location', ''), e.headers.get('X-Robots-Tag', '')
            except Exception as e:  # red: un reintento
                ultimo = repr(e)[:80]
        return u, 0, ultimo, ''

    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as ex:
        for u, cod, loc, xr in ex.map(pedir, URLS):
            vivo[u] = cod
            if cod != 200:
                problemas['publicada no responde 200'].append('%s -> %s %s' % (u, cod, loc))
            if 'noindex' in (xr or '').lower():
                problemas['cabecera X-Robots-Tag noindex'].append(u)

json.dump({'problemas': problemas, 'detalle': detalle}, open(SALIDA, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('páginas del sitemap revisadas:', len(URLS), '| pedidas en vivo:', len(vivo), '| en vivo con 200:', sum(1 for c in vivo.values() if c == 200))
if not problemas:
    print('sin problemas')
for regla, us in sorted(problemas.items(), key=lambda kv: -len(kv[1])):
    idiomas = Counter((urlparse(u.split(' ')[0]).path.strip('/').split('/')[0] or 'raíz') for u in us)
    print('\n[%d] %s' % (len(us), regla))
    print('   por carpeta:', dict(idiomas.most_common(8)))
    for u in us[:4]:
        extra = detalle.get(u, {})
        nota = ''
        if 'título' in regla:
            nota = ' | "%s" (%d)' % (extra.get('titulo', '')[:90], len(extra.get('titulo', '')))
        elif 'description' in regla:
            nota = ' | "%s" (%d)' % (extra.get('descripcion', '')[:110], len(extra.get('descripcion', '')))
        elif 'alternativo' in regla:
            nota = ' | ' + str(extra.get('img_sin_alt'))
        elif 'canónica' in regla:
            nota = ' | ' + str(extra.get('canonica'))
        print('   -', u + nota)
print('\ndetalle completo en', SALIDA)
if any('largo' in r or 'larga' in r for r in problemas):
    sys.exit(1)
