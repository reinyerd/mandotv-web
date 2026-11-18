# Mantiene al día, en las páginas hechas a mano (portadas, ayuda y privacidad de es y en; las demás las generan los otros scripts), los hreflang del <head> y el selector de
# idiomas del pie, a partir de idiomas_sitio.py. Es lo único que cambia solo en esas portadas; el resto del texto es manual.
# Uso: python -I herramientas/portadas_idiomas.py <carpeta del sitio>
import os, re, sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import idiomas_sitio as I

SITIO = sys.argv[1]
HREFLANG = re.compile(r'(?:  <link rel="alternate" hreflang="[\w-]+" href="[^"]*">\n)+')
SELECTOR = re.compile(r'(?:          <a href="[^"]*" hreflang="\w+" lang="\w+">[^<]*</a>\n)+')

PAGINAS = []
for lang in I.ACTIVOS:
    for clave in ('home', 'soporte', 'privacidad'):
        c = I.carpeta(clave, lang)
        PAGINAS.append((lang, clave, os.path.join(SITIO, *c.split('/')) if c.endswith('.html') else os.path.join(SITIO, *c.split('/'), 'index.html')))

for lang, clave, ruta in PAGINAS:
    if not os.path.isfile(ruta):
        continue
    t = open(ruta, encoding='utf-8').read()
    n = HREFLANG.sub(lambda m: I.hreflangs(clave), t, count=1)
    otros = ''.join(f'          <a href="{r}" hreflang="{l}" lang="{l}">{nom}</a>\n' for l, r, nom in I.enlaces_idiomas(clave, lang))
    n = SELECTOR.sub(lambda m: otros, n, count=1)
    if n != t:
        open(ruta, 'w', encoding='utf-8', newline='\n').write(n)
        print('ok', ruta)
