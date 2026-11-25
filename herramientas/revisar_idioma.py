"""Genera y revisa un idioma nuevo antes de publicarlo (25-nov). Ver docs/AGREGAR-IDIOMA.md.

Uso: python -I herramientas/revisar_idioma.py <clave del idioma>      (por ejemplo nl, ja, zh-hant)
Genera sus páginas (generar_idiomas.py, sin tocar las de otros idiomas) y revisa:
  1. herramientas/rutas/<clave>.json: las mismas páginas que el alemán, rutas en minúsculas ASCII.
  2. herramientas/datos_<clave>.py: la misma forma que datos_de.py (claves, listas, enlaces [texto](@clave),
     {marcadores}, etiquetas HTML y @@marcas@@), sin frases largas copiadas del alemán.
  3. <carpeta>/index.html (portada): lang, canonical, sin enlaces a /de/, mismas etiquetas que de/index.html,
     JSON-LD válido y textos traducidos.
  4. Las páginas generadas existen y todos sus enlaces internos llevan a un archivo que existe.
Termina con código 1 si hay errores. Las advertencias no bloquean, pero hay que mirarlas.
"""
import html.parser
import importlib
import json
import os
import re
import subprocess
import sys
from collections import Counter

sys.dont_write_bytecode = True
AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(AQUI)
LANG = sys.argv[1]
os.environ['MANDO_IDIOMAS_PRUEBA'] = LANG
sys.path.insert(0, AQUI)
import idiomas_sitio as I  # noqa: E402

errores, avisos = [], []
assert LANG in I.NUEVOS, f'{LANG} no está en NUEVOS de idiomas_sitio.py'
NOMBRE, CODIGO, CARPETA, DIR = I.NUEVOS[LANG]


def archivo_de_ruta(r):
    """Ruta pública (/nl/gidsen/) al archivo del sitio."""
    r = r.split('#')[0].split('?')[0]
    p = os.path.join(RAIZ, *[x for x in r.split('/') if x])
    return p if '.' in r.rstrip('/').rsplit('/', 1)[-1] else os.path.join(p, 'index.html')  # con extensión: archivo


# ---------------------------------------------------------------- 1. rutas
f_rutas = os.path.join(AQUI, 'rutas', LANG + '.json')
claves_de = [k for k, v in I.PAGINAS.items() if 'de' in v]
try:
    rutas = json.load(open(f_rutas, encoding='utf-8'))
except (OSError, ValueError) as ex:
    print('ERROR rutas:', ex)
    sys.exit(1)
if sorted(rutas) != sorted(claves_de):
    errores.append(f'rutas: faltan {sorted(set(claves_de) - set(rutas))} / sobran {sorted(set(rutas) - set(claves_de))}')
fijas = {'home': CARPETA, 'soporte': CARPETA + '/support.html', 'privacidad': CARPETA + '/privacy.html'}
for k, v in fijas.items():
    if rutas.get(k) != v:
        errores.append(f'rutas: {k} debe ser "{v}" (es "{rutas.get(k)}")')
for k, v in rutas.items():
    if k in fijas:
        continue
    if not re.fullmatch(re.escape(CARPETA) + r'(/[a-z0-9]+(-[a-z0-9]+)*)+', v):
        errores.append(f'rutas: {k} = "{v}" debe empezar con "{CARPETA}/" y usar solo a-z, 0-9 y guiones')
guias = rutas.get('guias', '')
for k, v in rutas.items():
    if I.PAGINAS[k]['de'].startswith('de/ratgeber/') and not v.startswith(guias + '/'):
        errores.append(f'rutas: la guía {k} debe ir dentro de "{guias}/" ({v})')
if len(set(rutas.values())) != len(rutas):
    errores.append('rutas: hay rutas repetidas')

# ---------------------------------------------------------------- 2. datos
ENLACE = re.compile(r'\]\(@([\w-]+)\)')
MARCADOR = re.compile(r'\{(\w+)\}')
ETIQUETA = re.compile(r'</?([a-zA-Z][\w-]*)')
MARCA = re.compile(r'@@\w+@@')


def forma(x, ruta='') -> list:
    """Lista de (ruta, firma) que deben coincidir entre el alemán y el idioma nuevo."""
    out = []
    if isinstance(x, dict):
        out.append((ruta, ('dict', tuple(sorted(x)))))
        for k in x:
            out += forma(x[k], f'{ruta}.{k}')
    elif isinstance(x, (list, tuple)):
        out.append((ruta, (type(x).__name__, len(x))))
        for i, e in enumerate(x):
            out += forma(e, f'{ruta}[{i}]')
    elif isinstance(x, str):
        out.append((ruta, ('str', tuple(ENLACE.findall(x)), tuple(sorted(MARCADOR.findall(x))),
                           tuple(sorted(Counter(ETIQUETA.findall(x)).items())), tuple(MARCA.findall(x)))))
    else:
        out.append((ruta, ('val', x)))
    return out


def textos(x):
    if isinstance(x, dict):
        for v in x.values():
            yield from textos(v)
    elif isinstance(x, (list, tuple)):
        for v in x:
            yield from textos(v)
    elif isinstance(x, str):
        yield x


try:
    de = importlib.import_module('datos_de')
    nuevo = importlib.import_module('datos_' + LANG.replace('-', '_'))
except Exception as ex:  # noqa: BLE001 (se informa tal cual)
    print('ERROR datos: no se puede importar:', repr(ex))
    sys.exit(1)
publicos = [n for n in dir(de) if n.isupper()]
for n in publicos:
    if not hasattr(nuevo, n):
        errores.append(f'datos: falta {n}')
        continue
    a, b = dict(forma(getattr(de, n), n)), dict(forma(getattr(nuevo, n), n))
    if a.keys() != b.keys():
        errores.append(f'datos: {n} no tiene la misma estructura que el alemán (difieren {sorted(set(a) ^ set(b))[:5]})')
        continue
    malos = [r for r in a if a[r] != b[r] and not (r.endswith('.locale'))]
    for r in malos[:8]:
        errores.append(f'datos: {r} difiere del alemán en enlaces/marcadores/etiquetas: {a[r]} vs {b[r]}')
    if len(malos) > 8:
        errores.append(f'datos: {n} tiene {len(malos) - 8} diferencias más')
    iguales = sorted({t for t in set(textos(getattr(de, n))) & set(textos(getattr(nuevo, n))) if len(t) > 30})
    for t in iguales[:5]:
        errores.append(f'datos: {n} tiene texto sin traducir: "{t[:70]}"')
if not re.fullmatch(r'[a-z]{2}_[A-Z]{2}', getattr(nuevo, 'UI', {}).get('locale', '')):
    errores.append('datos: UI["locale"] debe ser como nl_NL')

# ---------------------------------------------------------------- generar
r = subprocess.run([sys.executable, '-I', os.path.join(AQUI, 'generar_idiomas.py'), RAIZ, LANG],
                   capture_output=True, text=True, encoding='utf-8', env=dict(os.environ))
if r.returncode:
    print('ERROR al generar:\n' + r.stderr[-3000:])
    sys.exit(1)


# ---------------------------------------------------------------- 3. portada
class Lector(html.parser.HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.etiquetas, self.textos, self.hrefs, self.ld, self._pila = Counter(), [], [], [], []
        # Enlaces con hreflang: el bloque de alternates y el selector de idioma del pie. Ahí el enlace al alemán es
        # correcto (el pie lista los 30 idiomas), así que no cuentan como texto sin traducir.
        self.hrefs_idioma = []
        self.textos_linea = Counter()   # cuántos nodos de texto hay en cada línea, para localizar diferencias
        self.lang = self.dir = self.canonical = self.og_image = None

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        self.etiquetas[tag] += 1
        self._pila.append(tag)
        if tag == 'html':
            self.lang, self.dir = a.get('lang'), a.get('dir')
        if tag == 'link' and a.get('rel') == 'canonical':
            self.canonical = a.get('href')
        if tag == 'meta' and a.get('property') == 'og:image':
            self.og_image = a.get('content')
        if a.get('href'):
            self.hrefs.append(a['href'])
            if a.get('hreflang'):
                self.hrefs_idioma.append(a['href'])
        if a.get('src'):
            self.hrefs.append(a['src'])

    def handle_endtag(self, tag):
        if tag in self._pila:
            while self._pila and self._pila.pop() != tag:
                pass

    def handle_data(self, d):
        if self._pila and self._pila[-1] == 'script':
            if d.strip().startswith('{'):
                self.ld.append(d)
            return
        if self._pila and self._pila[-1] == 'style':
            return
        if d.strip():
            self.textos.append(d.strip())
            self.textos_linea[self.getpos()[0]] += 1


def leer(p):
    lec = Lector()
    lec.feed(open(p, encoding='utf-8').read())
    return lec


p_portada = archivo_de_ruta(I.ruta('home', LANG))
if not os.path.isfile(p_portada):
    errores.append(f'portada: falta {os.path.relpath(p_portada, RAIZ)}')
else:
    po, pd = leer(p_portada), leer(os.path.join(RAIZ, 'de', 'index.html'))
    if po.lang != CODIGO:
        errores.append(f'portada: <html lang="{po.lang}"> debe ser "{CODIGO}"')
    if (po.dir == 'rtl') != (DIR == 'rtl'):
        errores.append(f'portada: dir="{po.dir}" no corresponde ({DIR})')
    if po.canonical != I.URL + I.ruta('home', LANG):
        errores.append(f'portada: canonical {po.canonical} debe ser {I.URL + I.ruta("home", LANG)}')
    if not (po.og_image or '').startswith(f'{I.URL}/social-{LANG}.png'):
        errores.append(f'portada: og:image debe ser {I.URL}/social-{LANG}.png')
    dif = {t: (pd.etiquetas[t], po.etiquetas[t]) for t in set(pd.etiquetas) | set(po.etiquetas) if pd.etiquetas[t] != po.etiquetas[t]}
    # El bloque de hreflang, el selector del pie y el script del idioma recordado los ponen los scripts: pueden variar.
    dif.pop('link', None), dif.pop('a', None), dif.pop('li', None), dif.pop('script', None)
    if dif:
        errores.append(f'portada: etiquetas distintas a de/index.html (alemán, nuevo): {dif}')
    for bloque in po.ld:
        try:
            json.loads(bloque)
        except ValueError as ex:
            errores.append(f'portada: JSON-LD inválido: {ex}')
    for h in po.hrefs:
        if h in po.hrefs_idioma:   # el selector de idioma del pie y los alternates sí enlazan al alemán
            continue
        if h.startswith('/de/') or h == '/de/':
            errores.append(f'portada: enlace al alemán {h}')
    if len(pd.textos) == len(po.textos):
        iguales = [a for a, b in zip(pd.textos, po.textos) if a == b and len(a) > 25 and not a.startswith(('©', 'hola@'))]
        for t in iguales[:5]:
            errores.append(f'portada: texto sin traducir: "{t[:70]}"')
    else:
        # Decir en qué líneas difiere: así se revisa de un vistazo. Suele ser orden de la frase (en alemán el
        # párrafo empieza con una palabra suelta antes del primer enlace y en otros idiomas empieza por el enlace),
        # no texto perdido. Las líneas son las mismas en todos los idiomas porque la portada es copia de la alemana.
        lineas = sorted(l for l in set(pd.textos_linea) | set(po.textos_linea) if pd.textos_linea[l] != po.textos_linea[l])
        detalle = ', '.join(f'línea {l}: alemán {pd.textos_linea[l]}, aquí {po.textos_linea[l]}' for l in lineas[:6])
        avisos.append(f'portada: {len(po.textos)} textos contra {len(pd.textos)} del alemán ({detalle}); '
                      f'revisar esas líneas por si falta algo')

# ---------------------------------------------------------------- 4. páginas generadas y enlaces
for k in rutas:
    p = archivo_de_ruta(I.ruta(k, LANG))
    if not os.path.isfile(p):
        errores.append(f'páginas: falta {os.path.relpath(p, RAIZ)}')
        continue
    for h in leer(p).hrefs:
        if h.startswith('/') and not h.startswith('//') and not os.path.isfile(archivo_de_ruta(h)):
            errores.append(f'enlaces: {os.path.relpath(p, RAIZ)} lleva a {h}, que no existe')

t = I.TEXTOS_NUEVOS.get(LANG, {})
if not (t.get('ms_texto') and len(t.get('pie', [])) == 4 and len(t.get('social', [])) == 2):
    avisos.append('textos_idiomas.json: faltan los textos cortos de este idioma (los agrega otra tarea)')

for a in avisos:
    print('AVISO', a)
for e in errores:
    print('ERROR', e)
print(f'{LANG}: {len(errores)} errores, {len(avisos)} avisos, {len(rutas)} páginas')
sys.exit(1 if errores else 0)
