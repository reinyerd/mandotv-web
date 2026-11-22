"""Pone en cada página la versión de sus archivos (css, js, imágenes) según su contenido.

Así el navegador descarga el archivo nuevo apenas cambia y nunca hace falta vaciar la caché.
La versión son los primeros 10 caracteres del SHA-256 del archivo: si el archivo no cambia, la versión tampoco.
Se ejecuta solo antes de cada commit (herramientas/hooks/pre-commit). Uso manual: python herramientas/versionar.py
Imprime las páginas que cambió.

También regenera sitemap.xml: lista las páginas indexables (sin noindex, sin herramientas/ ni r/) y pone en cada una
la fecha real de su último cambio (último commit que tocó el archivo; si tiene cambios sin commitear, la fecha de hoy).
"""
import hashlib
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
    for p in sorted(RAIZ.rglob('*.html')):
        rel = p.relative_to(RAIZ)
        if rel.parts[0] in CARPETAS_FUERA or rel.as_posix() in FUERA_DEL_SITEMAP:
            continue
        if 'noindex' in p.read_text(encoding='utf-8'):
            continue
        yield p


def sitemap():
    def orden(p):
        u = url_de(p)[len(DOMINIO):]
        grupo = 0 if u == '/' else 1 if u.startswith('/control-remoto-') else 2 if u.startswith('/guias/') else 3
        return (grupo, u)
    filas = [f'  <url><loc>{url_de(p)}</loc><lastmod>{fecha_cambio(p)}</lastmod></url>' for p in sorted(paginas_indexables(), key=orden)]
    nuevo = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + '\n'.join(filas) + '\n</urlset>\n'
    destino = RAIZ / 'sitemap.xml'
    if not destino.exists() or destino.read_text(encoding='utf-8') != nuevo:
        destino.write_text(nuevo, encoding='utf-8', newline='')
        return True
    return False


def main():
    cambiadas = [p.relative_to(RAIZ).as_posix() for p in sorted(RAIZ.rglob('*.html')) if '.git' not in p.parts and versionar(p)]
    if sitemap():
        cambiadas.append('sitemap.xml')
    for p in cambiadas:
        print(p)
    return 0


if __name__ == '__main__':
    sys.exit(main())
