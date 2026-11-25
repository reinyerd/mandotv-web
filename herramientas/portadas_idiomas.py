# Mantiene al día los enlaces entre idiomas de TODAS las páginas que ya existen, a partir de idiomas_sitio.py, sin
# rehacerlas: los hreflang del <head>, los idiomas del menú del pie y la lista "esta guía en otros idiomas".
# 25-nov: antes solo tocaba portadas, ayuda y privacidad de es y en. Se amplió a todas porque varias páginas tienen
# arreglos hechos a mano que sus generadores no conocen (por ejemplo la sección Casa de la privacidad en es, en, pt e
# it, o los enlaces #android de las guías en inglés): regenerarlas los borraría. Así, sumar un idioma solo toca enlaces.
# El selector del cierre del pie (pie-firma) lo pone al día pie_firma.py.
# Uso: python -I herramientas/portadas_idiomas.py <carpeta del sitio>
import os, re, sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import idiomas_sitio as I

SITIO = sys.argv[1]
HREFLANG = re.compile(r'(?:  <link rel="alternate" hreflang="[\w-]+" href="[^"]*">\n)+')
SELECTOR = re.compile(r'(?:          <a href="[^"]*" hreflang="[\w-]+" lang="[\w-]+">[^<]*</a>\n)+')
LISTA = re.compile(r'(?:        <li><a href="[^"]*" hreflang="[\w-]+" lang="[\w-]+">[^<]*</a></li>\n)+')


def archivo(clave, lang):
    c = I.carpeta(clave, lang)
    return os.path.join(SITIO, *c.split('/')) if c.endswith('.html') else os.path.join(SITIO, *c.split('/'), 'index.html')


for clave, idiomas in I.PAGINAS.items():
    for lang in idiomas:
        ruta = archivo(clave, lang)
        if lang not in I.ACTIVOS or not os.path.isfile(ruta):
            continue
        t = open(ruta, encoding='utf-8').read()
        enlaces = I.enlaces_idiomas(clave, lang)
        n = HREFLANG.sub(lambda m: I.hreflangs(clave), t, count=1)
        # El cierre del pie lo escribe entero pie_firma.py (la lista de idiomas incluida, con su sangría y su
        # aria-current). Si se toca también aquí queda una lista a medias: el 25-nov, al pasar de 6 a 30 idiomas,
        # dejó 34 entradas con cuatro idiomas repetidos en todas las páginas, y una segunda pasada las dobló a 58.
        # Por eso se trabaja solo en lo que hay ANTES de los marcadores pie-firma.
        antes, marca, resto = n.partition('      <!-- pie-firma')
        antes = SELECTOR.sub(lambda m: ''.join(f'          <a href="{r}" hreflang="{l}" lang="{l}">{nom}</a>\n' for l, r, nom in enlaces), antes, count=1)
        antes = LISTA.sub(lambda m: ''.join(f'        <li><a href="{r}" hreflang="{l}" lang="{l}">{nom}</a></li>\n' for l, r, nom in enlaces), antes, count=1)
        n = antes + marca + resto
        if n != t:
            open(ruta, 'w', encoding='utf-8', newline='\n').write(n)
            print('ok', ruta)
