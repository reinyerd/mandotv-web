"""Content-Security-Policy de mandotv.app (25-nov-2026).

La política vive en Cloudflare (Rules > Transform Rules > Response Header "Cabeceras de seguridad") y su copia exacta en
herramientas/csp.txt. Los scripts en línea se permiten por su hash SHA-256: si cambia uno (por ejemplo el de
idioma_guardado.py, /m/ o /r/), el navegador lo bloquearía en silencio. Por eso el pre-commit corre
    python -I herramientas/csp.py --verificar
que falla si algún script en línea del sitio no está en csp.txt. Entonces: python -I herramientas/csp.py (reescribe
csp.txt) y copiar el valor nuevo en la regla de Cloudflare ANTES de publicar.
"""
import base64, glob, hashlib, os, re, sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ARCHIVO = os.path.join(RAIZ, 'herramientas', 'csp.txt')


def hashes():
    hs = set()
    for p in glob.glob(os.path.join(RAIZ, '**', '*.html'), recursive=True):
        rel = os.path.relpath(p, RAIZ).replace('\\', '/')
        if rel.startswith(('herramientas/', 'docs/', 'node_modules/')):
            continue
        t = open(p, encoding='utf-8').read()
        for attrs, body in re.findall(r'<script([^>]*)>(.*?)</script>', t, re.S):
            if 'src=' in attrs or 'application/ld+json' in attrs:
                continue
            hs.add("'sha256-" + base64.b64encode(hashlib.sha256(body.encode('utf-8')).digest()).decode() + "'")
    return sorted(hs)


def politica():
    return '; '.join([
        "default-src 'self'",
        "script-src 'self' " + ' '.join(hashes()) + " https://static.cloudflareinsights.com https://www.googletagmanager.com",
        "style-src 'self' 'unsafe-inline'",  # atributos style="--marca: ..." en casi todas las páginas
        "img-src 'self' data: https://*.google-analytics.com https://*.googletagmanager.com",
        "font-src 'self'",
        "media-src 'self'",
        "connect-src 'self' https://cloudflareinsights.com https://*.google-analytics.com https://*.analytics.google.com https://*.googletagmanager.com",
        "manifest-src 'self'",
        "frame-src 'none'",
        "object-src 'none'",
        "base-uri 'self'",
        "form-action 'self'",
        "frame-ancestors 'self'",
        "upgrade-insecure-requests",
    ])


if __name__ == '__main__':
    nueva = politica()
    if '--verificar' in sys.argv:
        actual = open(ARCHIVO, encoding='utf-8').read().strip() if os.path.isfile(ARCHIVO) else ''
        faltan = [h for h in hashes() if h not in actual]
        if faltan:
            print('csp.py: hay scripts en línea que la CSP de Cloudflare no permite: ' + ' '.join(faltan))
            print('Corre python -I herramientas/csp.py, copia herramientas/csp.txt en la regla de Cloudflare y vuelve a hacer el commit.')
            sys.exit(1)
        sys.exit(0)
    open(ARCHIVO, 'w', encoding='utf-8', newline='\n').write(nueva + '\n')
    print(nueva)
