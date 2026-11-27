"""Pone en cada página la versión de sus archivos (css, js, imágenes) según su contenido.

Así el navegador descarga el archivo nuevo apenas cambia y nunca hace falta vaciar la caché.
La versión son los primeros 10 caracteres del SHA-256 del archivo: si el archivo no cambia, la versión tampoco.
Se ejecuta solo antes de cada commit (herramientas/hooks/pre-commit). Uso manual: python herramientas/versionar.py
Imprime las páginas que cambió.

También regenera sitemap.xml: lista las páginas indexables (sin noindex, sin herramientas/ ni r/) y pone en cada una
la fecha real de su último cambio (último commit que tocó el archivo; si tiene cambios sin commitear, la fecha de hoy).
Si una página tiene un VideoObject en su JSON-LD, su entrada lleva también <video:video> (sitemap de video de Google)
con los mismos datos del schema: así el video se declara en un solo lugar.
"""
import hashlib
import html
import json
import pathlib
import datetime
import re
import subprocess
import sys

RAIZ = pathlib.Path(__file__).resolve().parent.parent
REF = re.compile(
    r'(?P<attr>(?:href|src|content)=")(?P<pre>https://mandotv\.app/|/)?'
    r'(?P<ruta>[\w./-]+\.(?:css|js|png|svg|webmanifest|jpg|jpeg|webp|ico))(?:\?v=[\w-]*)?"'
)
_cache = {}
DOMINIO = 'https://mandotv.app'
FUERA_DEL_SITEMAP = {'404.html'}  # además, todo lo que lleve noindex y las carpetas de abajo
CARPETAS_FUERA = {'herramientas', 'r', 'app', '.git', '.taste-skill'}


def paginas():
    """Todas las páginas del sitio, sin carpetas ocultas (.git, .claude con worktrees de otras sesiones, etc.)."""
    for p in sorted(RAIZ.rglob('*.html')):
        if not any(parte.startswith('.') for parte in p.relative_to(RAIZ).parts[:-1]):
            yield p


def huella(archivo):
    if archivo not in _cache:
        _cache[archivo] = hashlib.sha256(archivo.read_bytes()).hexdigest()[:10]
    return _cache[archivo]


def versionar(pagina):
    texto = pagina.read_text(encoding='utf-8')

    def cambiar(m):
        base = RAIZ if m['pre'] else pagina.parent
        archivo = (base / m['ruta']).resolve()
        if RAIZ not in archivo.parents or not archivo.is_file():
            return m[0]  # archivo externo o inexistente: no se toca
        return f'{m["attr"]}{m["pre"] or ""}{m["ruta"]}?v={huella(archivo)}"'

    nuevo = REF.sub(cambiar, texto)
    if nuevo != texto:
        pagina.write_text(nuevo, encoding='utf-8', newline='')
        return True
    return False


def git(*args):
    try:
        r = subprocess.run(['git', '-C', str(RAIZ), *args], capture_output=True, text=True, encoding='utf-8')
        return r.stdout.strip() if r.returncode == 0 else None
    except OSError:
        return None


def fecha_cambio(pagina):
    """Fecha (AAAA-MM-DD) del último cambio real de la página."""
    ruta = pagina.relative_to(RAIZ).as_posix()
    hoy = datetime.date.today().isoformat()
    if git('status', '--porcelain', '--', ruta):  # con cambios sin commitear (o nuevo): hoy
        return hoy
    return git('log', '-1', '--format=%cs', '--', ruta) or hoy


def url_de(pagina):
    ruta = pagina.relative_to(RAIZ).as_posix()
    if ruta == 'index.html':
        return DOMINIO + '/'
    if ruta.endswith('/index.html'):
        return DOMINIO + '/' + ruta[:-len('index.html')]
    return DOMINIO + '/' + ruta


def paginas_indexables():
    for p in paginas():
        rel = p.relative_to(RAIZ)
        if rel.parts[0] in CARPETAS_FUERA or rel.as_posix() in FUERA_DEL_SITEMAP:
            continue
        if 'noindex' in p.read_text(encoding='utf-8'):
            continue
        yield p


LD = re.compile(r'<script type="application/ld\+json">(.*?)</script>', re.S)


def videos_de(pagina):
    """Los VideoObject del JSON-LD de la página (dentro de @graph o sueltos)."""
    encontrados = []
    for bloque in LD.findall(pagina.read_text(encoding='utf-8')):
        datos = json.loads(bloque)
        nodos = datos.get('@graph', [datos]) if isinstance(datos, dict) else datos
        encontrados += [n for n in nodos if isinstance(n, dict) and n.get('@type') == 'VideoObject']
    return encontrados


def segundos(iso):
    m = re.fullmatch(r'PT(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?', iso or '')
    return int(m[1] or 0) * 3600 + int(m[2] or 0) * 60 + int(m[3] or 0) if m else 0


def video_xml(v):
    e = lambda s: html.escape(str(s), quote=False)
    partes = [f'<video:thumbnail_loc>{e(v["thumbnailUrl"])}</video:thumbnail_loc>', f'<video:title>{e(v["name"])}</video:title>',
              f'<video:description>{e(v["description"])}</video:description>',
              f'<video:content_loc>{e(v["contentUrl"])}</video:content_loc>']
    if v.get('embedUrl'):
        partes.append(f'<video:player_loc>{e(v["embedUrl"])}</video:player_loc>')
    if segundos(v.get('duration')):
        partes.append(f'<video:duration>{segundos(v["duration"])}</video:duration>')
    if v.get('uploadDate'):
        partes.append(f'<video:publication_date>{e(v["uploadDate"])}</video:publication_date>')
    partes.append('<video:family_friendly>yes</video:family_friendly>')
    return '<video:video>' + ''.join(partes) + '</video:video>'


def sitemap():
    def orden(p):
        u = url_de(p)[len(DOMINIO):]
        grupo = 0 if u == '/' else 1 if u.startswith('/es/control-remoto-') else 2 if u.startswith('/es/guias/') else 3
        return (grupo, u)
    filas = [f'  <url><loc>{url_de(p)}</loc><lastmod>{fecha_cambio(p)}</lastmod>' + ''.join(video_xml(v) for v in videos_de(p)) + '</url>'
             for p in sorted(paginas_indexables(), key=orden)]
    espacios = 'xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:video="http://www.google.com/schemas/sitemap-video/1.1"'
    nuevo = f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset {espacios}>\n' + '\n'.join(filas) + '\n</urlset>\n'
    destino = RAIZ / 'sitemap.xml'
    if not destino.exists() or destino.read_text(encoding='utf-8') != nuevo:
        destino.write_text(nuevo, encoding='utf-8', newline='')
        return True
    return False


def main():
    cambiadas = [p.relative_to(RAIZ).as_posix() for p in paginas() if versionar(p)]
    if sitemap():
        cambiadas.append('sitemap.xml')
    for p in cambiadas:
        print(p)
    return 0


if __name__ == '__main__':
    sys.exit(main())
