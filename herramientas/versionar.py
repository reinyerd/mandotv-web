"""Pone en cada página la versión de sus archivos (css, js, imágenes) según su contenido.

Así el navegador descarga el archivo nuevo apenas cambia y nunca hace falta vaciar la caché.
La versión son los primeros 10 caracteres del SHA-256 del archivo: si el archivo no cambia, la versión tampoco.
Se ejecuta solo antes de cada commit (herramientas/hooks/pre-commit). Uso manual: python herramientas/versionar.py
Imprime las páginas que cambió.
"""
import hashlib
import pathlib
import re
import sys

RAIZ = pathlib.Path(__file__).resolve().parent.parent
REF = re.compile(
    r'(?P<attr>(?:href|src|content)=")(?P<pre>https://mandotv\.app/|/)?'
    r'(?P<ruta>[\w./-]+\.(?:css|js|png|svg|webmanifest|jpg|jpeg|webp|ico|woff2))(?:\?v=[\w-]*)?"'
)
_cache = {}


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


def main():
    cambiadas = [p for p in sorted(RAIZ.rglob('*.html')) if '.git' not in p.parts and versionar(p)]
    for p in cambiadas:
        print(p.relative_to(RAIZ).as_posix())
    return 0


if __name__ == '__main__':
    sys.exit(main())
