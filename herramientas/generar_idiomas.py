# Genera las páginas de mandotv.app en alemán (/de/) y francés (/fr/): marcas, guías, índice de guías, ayuda y privacidad.
# Un solo motor; los textos de cada idioma están en herramientas/datos_de.py y herramientas/datos_fr.py (escritos para las
# búsquedas de cada país, no son traducción literal). Las portadas /de/ y /fr/ se mantienen a mano, como /en/.
# Uso: python -I herramientas/generar_idiomas.py <carpeta del sitio> [de] [fr]   (sin idiomas: todos los activos)
# Las rutas y los hreflang salen de idiomas_sitio.py, igual que en generar_en.py, generar_guias.py y generar_marcas.py.
import ast, html, importlib, json, os, re, sys

sys.dont_write_bytecode = True
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import idiomas_sitio as I

SITIO = sys.argv[1]
URL = I.URL
FECHA = '2026-11-18'
TIENDA = 'https://apps.microsoft.com/detail/9N3D7T1DP2SW?mode=direct'
TIENDA_APPLE = 'https://apps.apple.com/app/id6834927348'
MARCA_ORDEN = ('lg', 'samsung', 'roku', 'android')


def constantes():
    """Toma los íconos de las tiendas de generar_guias.py (así no se copian aquí)."""
    arbol = ast.parse(open(os.path.join(AQUI, 'generar_guias.py'), encoding='utf-8').read())
    buscados = {'LOGO', 'APPLE_SVG', 'MS_SVG', 'GPLAY_SVG'}
    datos = {}
    for n in arbol.body:
        if isinstance(n, ast.Assign) and len(n.targets) == 1 and getattr(n.targets[0], 'id', None) in buscados:
            datos[n.targets[0].id] = ast.literal_eval(n.value)
    assert set(datos) == buscados, datos.keys()
    return datos


K = constantes()
LOGO, APPLE_SVG, MS_SVG, GPLAY_SVG = K['LOGO'], K['APPLE_SVG'], K['MS_SVG'], K['GPLAY_SVG']
ORG = {"@type": "Organization", "@id": URL + "/#org", "name": "Mando TV", "url": URL + "/"}
e = html.escape


ENLACE = re.compile(r'\[([^\]]+)\]\(@([\w-]+)\)')


class Idioma:
    def __init__(self, cod):
        self.cod = cod
        d = importlib.import_module('datos_' + cod.replace('-', '_'))
        self.d = d
        self.U = d.UI
        self.home = I.ruta('home', cod)
        self.android = self.home + '#android'

    def r(self, clave):
        return I.ruta(clave, self.cod)

    def fmt(self, t):
        """Escapa el texto y convierte [texto](@clave) en enlaces internos a la página de esa clave."""
        return ENLACE.sub(lambda m: f'<a href="{self.r(m[2])}">{m[1]}</a>', html.escape(t))

    @staticmethod
    def plano(t):
        return ENLACE.sub(lambda m: m[1], t)

    # ------------------------------------------------------------------ piezas comunes
    def cabecera(self, titulo, desc, url, clave, color, tipo, ld):
        U = self.U
        return f'''<!doctype html>
<html lang="{I.CODIGO_LANG[self.cod]}"{' dir="rtl"' if I.DIRECCION[self.cod] == 'rtl' else ''} style="--marca: {color}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="referrer" content="strict-origin-when-cross-origin">
  <meta name="apple-itunes-app" content="app-id=6834927348">
  <title>{e(titulo)}</title>
  <meta name="description" content="{e(desc)}">
  <meta name="robots" content="index, follow, max-image-preview:large">
  <meta name="theme-color" content="{color}">
  <link rel="canonical" href="{url}">
{I.hreflangs(clave)}  <meta property="og:site_name" content="Mando TV">
  <meta property="og:locale" content="{U['locale']}">
  <meta property="og:type" content="{tipo}">
  <meta property="og:url" content="{url}">
  <meta property="og:title" content="{e(titulo)}">
  <meta property="og:description" content="{e(desc)}">
  <meta property="og:image" content="{URL}/social-{self.cod}.png">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="apple-touch-icon" href="/apple-touch-icon.png">
  <link rel="icon" href="/icono.svg" type="image/svg+xml">
  <link rel="stylesheet" href="/estilos.css?v=12">
  <script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
</head>
<body>
  <div class="cabecera-pagina">
    <div class="contenedor">
      <header class="barra">
        <a class="logo" href="{self.home}" aria-label="{e(U['aria_home'])}">
          {LOGO}
          Mando TV
        </a>
        <nav aria-label="{e(U['aria_main'])}">
          <a href="{self.home}#funciones">{e(U['nav_que'])}</a>
          <a href="{self.r('soporte')}">{e(U['nav_ayuda'])}</a>
          <a class="boton-barra" href="mailto:hola@mandotv.app?subject={U['asunto']}">{e(U['nav_contacto'])}</a>
        </nav>
      </header>
'''

    def lista_tiendas(self, idn=None, etiqueta=None, guia=False):
        U = self.U
        ident = f' id="{idn}"' if idn else ''
        apple = f'<li><a class="tienda" href="{TIENDA_APPLE}" target="_blank" rel="noopener" aria-label="{e(U["apple_aria"])}">{APPLE_SVG}<span><small>{e(U["descarga"])}</small>App Store</span></a></li>'
        ms = f'<li><a class="tienda" href="{TIENDA}" target="_blank" rel="noopener" aria-label="{e(U["ms_aria"])}">{MS_SVG}<span><small>{e(U["descarga"])}</small>Microsoft Store</span></a></li>'
        gp = f'<li><a class="tienda" href="{self.android}" aria-label="{e(U["gp_aria"])}">{GPLAY_SVG}<span><small>{e(U["anticipada"])}</small>Google Play</span></a></li>'
        orden = (apple, ms, gp) if guia else (apple, gp, ms)
        li = '\n'.join('        ' + x for x in orden)
        return f'      <ul class="tiendas"{ident} aria-label="{e(etiqueta or U["aria_desc"])}">\n{li}\n      </ul>'

    def pie_marcas(self):
        d = self.d
        li = '\n'.join(f'        <li><a href="{self.r(k)}">{e(n)}</a></li>' for k, n in d.PIE)
        return f'      <ul class="marcas-enlaces pie-marcas" aria-label="{e(self.U["aria_marcas"])}">\n{li}\n      </ul>\n'

    def pie(self, clave):
        U = self.U
        otros = ''.join(f'          <a href="{r}" hreflang="{l}" lang="{l}">{n}</a>\n' for l, r, n in I.enlaces_idiomas(clave, self.cod))
        return f'''  <footer class="pie">
    <div class="contenedor">
      <div class="pie-enlaces">
        <nav aria-label="{e(U['aria_pie'])}">
          <a href="{self.home}">{e(U['inicio'])}</a>
          <a href="{self.r('soporte')}">{e(U['nav_ayuda'])}</a>
          <a href="{self.r('privacidad')}">{e(U['privacidad'])}</a>
          <a href="mailto:hola@mandotv.app">hola@mandotv.app</a>
{otros}          <button type="button" class="enlace-cookies" data-cookies>Cookies</button>
        </nav>
        <span>{e(U['hecho'])}</span>
      </div>
{self.pie_marcas()}      <p class="pie-gigante" aria-hidden="true">MANDO</p>
      <small>{e(U['aviso'])}</small>
    </div>
  </footer>
  <script src="/correo.js?v=3" defer></script>
  <script src="/cookies.js?v=1" defer></script>
  <!-- Cloudflare Web Analytics: cuenta visitas sin cookies ni datos personales -->
  <script defer src="https://static.cloudflareinsights.com/beacon.min.js" data-cf-beacon='{{"token": "3a3f0250e4b04d5884b033b9a94302b4"}}'></script>
</body>
</html>
'''

    # ------------------------------------------------------------------ marcas
    def pagina_marca(self, m):
        U = self.U
        url = URL + self.r(m['clave'])
        ld = {"@context": "https://schema.org", "@graph": [
          {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Mando TV", "item": URL + self.home},
            {"@type": "ListItem", "position": 2, "name": m['h1'], "item": url}]},
          {"@type": "FAQPage", "inLanguage": I.CODIGO_LANG[self.cod], "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in m['faq']]}]}
        funciones = '\n'.join(f'        <li><b>{e(t)}</b><span>{e(x)}</span></li>' for t, x in m['funciones'])
        pasos = '\n'.join(f'          <li>{e(p)}</li>' for p in m['pasos'])
        guias = '\n'.join(f'        <li><a href="{self.r(k)}">{e(t)}</a></li>' for k, t in m['guias'])
        faq = '\n'.join(f'        <details><summary>{e(q)}</summary><p>{e(a)}</p></details>' for q, a in m['faq'])
        otras = '\n'.join(f'          <li><a href="{self.r(k)}">{e(self.d.NOMBRE_OTRA[k])}</a></li>' for k in MARCA_ORDEN if k != m['clave'])
        c = m['corto']
        return (self.cabecera(m['titulo'], m['desc'], url, m['clave'], m['color'], 'website', ld) + f'''      <nav class="migas" aria-label="{e(U['aria_ruta'])}"><a href="{self.home}">Mando TV</a> / <span>{e(c)}</span></nav>
      <h1>{e(m["h1"])}</h1>
      <p>{e(m["intro"])}</p>
      <div class="acciones">
        <a class="boton" href="#tiendas">{e(U['bajar'])}</a>
        <a class="boton claro" href="#como">{e(U['b_como_btn'])}</a>
      </div>
{self.lista_tiendas('tiendas', U['b_tiendas_label'])}
      <p class="nota">{e(U['b_nota'])}</p>
    </div>
  </div>

  <main class="contenedor">
    <div class="documento">
      <h2 id="compatibles">{e(U['b_compat'])}</h2>
      <p>{e(m["compat"])}</p>

      <h2 id="funciones">{e(m['h2']['funciones'])}</h2>
      <ul class="lista-funciones">
{funciones}
      </ul>

      <h2 id="como">{e(m['h2']['como'])}</h2>
      <ol>
{pasos}
      </ol>

      <h2 id="encender">{e(m['h2']['encender'])}</h2>
      <p>{e(m["encender"])}</p>

      <h2 id="preguntas">{e(m['h2']['preguntas'])}</h2>
      <div class="preguntas">
{faq}
      </div>

      <h2 id="guias">{e(m['h2']['guias'])}</h2>
      <ul>
{guias}
      </ul>

      <h2 id="otras">{e(U['b_otras'])}</h2>
      <p>{e(U['b_otras_p'])}</p>
      <ul>
{otras}
      </ul>
    </div>
  </main>

''' + self.pie(m['clave']))

    def tabla(self, t):
        """Tabla comparativa (igual que tabla_html de generar_en.py): en el celular se desplaza dentro de su caja."""
        cabeza = ''.join(f'<th scope="col">{e(c)}</th>' for c in t['cabeza'])
        filas = '\n'.join('            <tr><th scope="row">' + e(f[0]) + '</th>' + ''.join(f'<td>{e(c)}</td>' for c in f[1:]) + '</tr>' for f in t['filas'])
        nota = f'\n      <p class="nota">{self.fmt(t["nota"])}</p>' if t.get('nota') else ''
        return f'''      <h2 id="comparacion">{e(t["titulo"])}</h2>
      <div class="tabla" role="region" aria-labelledby="comparacion" tabindex="0">
        <table>
          <thead><tr>{cabeza}</tr></thead>
          <tbody>
{filas}
          </tbody>
        </table>
      </div>''' + nota

    # ------------------------------------------------------------------ guías
    def pagina_guia(self, g):
        U = self.U
        url = URL + self.r(g['clave'])
        ld = {"@context": "https://schema.org", "@graph": [
          {"@type": "Article", "headline": g["h1"], "description": g["desc"], "inLanguage": I.CODIGO_LANG[self.cod],
           "datePublished": g.get("fecha", FECHA), "dateModified": g.get("modificada", g.get("fecha", FECHA)),
           "mainEntityOfPage": url, "image": URL + f"/social-{self.cod}.png",
           "author": {"@id": URL + "/#org"}, "publisher": {"@id": URL + "/#org"}},
          ORG,
          {"@type": "HowTo", "name": g["h1"], "description": g["desc"], "inLanguage": I.CODIGO_LANG[self.cod],
           "step": [{"@type": "HowToStep", "position": n, "text": self.plano(p)} for n, p in enumerate(g["pasos"], 1)]},
          {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": U['inicio'], "item": URL + self.home},
            {"@type": "ListItem", "position": 2, "name": U['g_guias'], "item": URL + self.r('guias')},
            {"@type": "ListItem", "position": 3, "name": g["h1"], "item": url}]},
          {"@type": "FAQPage", "inLanguage": I.CODIGO_LANG[self.cod], "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in g["faq"]]}]}
        ms = ''
        if I.es_guia_pc(self.r(g['clave'])):  # ficha de Microsoft Store visible y en JSON-LD (GEO, 23-nov)
            ld['@graph'].append(I.app_windows(url))
            ms = '\n      ' + I.linea_ms_store(self.cod)
        pasos = '\n'.join(f'        <li>{self.fmt(p)}</li>' for p in g['pasos'])
        extra = '\n\n'.join(f'      <h2>{e(t)}</h2>\n      <p>{self.fmt(p)}</p>' for t, p in g['extra'])
        if g.get('tabla'):
            extra = self.tabla(g['tabla']) + '\n\n' + extra
        faq = '\n'.join(f'        <details><summary>{e(q)}</summary><p>{e(a)}</p></details>' for q, a in g['faq'])
        if g.get('marca'):
            # marca: clave de una página de marca (texto de PAGINA_MARCA) o (clave de cualquier página, texto del enlace)
            clave_m, texto_m = g['marca'] if isinstance(g['marca'], tuple) else (g['marca'], self.d.PAGINA_MARCA[g['marca']])
            enlace = f'<a href="{self.r(clave_m)}">{e(texto_m)}</a>'
            marcas = '<p>' + U['g_mas_pagina'].format(enlace=enlace) + '</p>'
        else:
            marcas = (f'<p>{e(U["g_mas_marca"])}</p>\n      <ul>\n' + '\n'.join(
              f'        <li><a href="{self.r(k)}">{e(n)}</a></li>' for k, n in self.d.PIE[:4]) + '\n      </ul>')
        otras = '\n'.join(f'        <li><a href="{self.r(k)}">{e(t)}</a></li>' for k, t in self.d.OTRAS_GUIAS if k != g['clave'])
        idiomas = '\n'.join(f'        <li><a href="{r}" hreflang="{l}" lang="{l}">{n}</a></li>' for l, r, n in I.enlaces_idiomas(g['clave'], self.cod))
        return (self.cabecera(g['titulo'], g['desc'], url, g['clave'], '#3d7bff', 'article', ld) + f'''      <nav class="migas" aria-label="{e(U['aria_ruta'])}"><a href="{self.home}">{e(U['inicio'])}</a> / <a href="{self.r('guias')}">{e(U['g_guias'])}</a> / <span>{e(g["corto"])}</span></nav>
      <h1>{e(g["h1"])}</h1>
      <p>{e(g["intro"])}</p>
      <div class="acciones">
        <a class="boton" href="#pasos">{e(U['g_ver'])}</a>
        <a class="boton claro" href="#mando-tv">{e(U['bajar'])}</a>
      </div>
    </div>
  </div>

  <main class="contenedor">
    <div class="documento">
      <h2 id="pasos">{e(U['g_pasos'])}</h2>
      <ol>
{pasos}
      </ol>

{extra}

      <h2 id="mando-tv">{e(U['g_hazlo'])}</h2>
      <p>{e(U['g_tiendas'])}</p>
{self.lista_tiendas(None, None, guia=True)}
      <p class="nota">{U['g_nota'].format(enlace=self.android)}</p>{ms}
      {marcas}

      <h2 id="preguntas">{e(U['g_faq'])}</h2>
      <div class="preguntas">
{faq}
      </div>

      <h2 id="otras">{e(U['g_mas'])}</h2>
      <ul>
{otras}
        <li><a href="{self.r('guias')}">{e(U['g_todas'])}</a></li>
        <li><a href="{self.r('soporte')}">{e(U['g_ayuda'])}</a></li>
      </ul>

      <h2 id="idiomas">{e(U['g_idiomas'])}</h2>
      <ul>
{idiomas}
      </ul>
    </div>
  </main>

''' + self.pie(g['clave']))

    def indice(self):
        U, d = self.U, self.d
        url = URL + self.r('guias')
        titulo, desc = d.INDICE['titulo'], d.INDICE['desc']
        gd = {g['clave']: g['desc'] for g in d.GUIAS}
        ld = {"@context": "https://schema.org", "@graph": [
          ORG,
          {"@type": "CollectionPage", "name": titulo, "description": desc, "url": url, "inLanguage": I.CODIGO_LANG[self.cod],
           "publisher": {"@id": URL + "/#org"},
           "mainEntity": {"@type": "ItemList", "itemListElement": [
             {"@type": "ListItem", "position": n, "name": t, "url": URL + self.r(k)}
             for n, (k, t) in enumerate(d.OTRAS_GUIAS, 1)]}}]}
        lista = '\n'.join(f'        <li><a href="{self.r(k)}">{e(t)}</a>: {e(gd[k])}</li>' for k, t in d.OTRAS_GUIAS)
        marcas = '\n'.join(f'        <li><a href="{self.r(k)}">{e(n)}</a></li>' for k, n in d.PIE[:4])
        return (self.cabecera(titulo, desc, url, 'guias', '#3d7bff', 'website', ld) + f'''      <nav class="migas" aria-label="{e(U['aria_ruta'])}"><a href="{self.home}">{e(U['inicio'])}</a> / <span>{e(U['g_guias'])}</span></nav>
      <h1>{e(d.INDICE['h1'])}</h1>
      <p>{e(d.INDICE['intro'])}</p>
    </div>
  </div>

  <main class="contenedor">
    <div class="documento">
      <h2 id="guias">{e(d.INDICE['h2_guias'])}</h2>
      <ul>
{lista}
      </ul>

      <h2 id="marcas">{e(d.INDICE['h2_marcas'])}</h2>
      <ul>
{marcas}
        <li><a href="{self.r('soporte')}">{e(U['g_ayuda'])}</a></li>
      </ul>

    </div>
  </main>

''' + self.pie('guias'))

    # ------------------------------------------------------------------ ayuda y privacidad
    def ld_simple(self, nombre, url):
        return {"@context": "https://schema.org", "@graph": [
          ORG,
          {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": self.U['inicio'], "item": URL + self.home},
            {"@type": "ListItem", "position": 2, "name": nombre, "item": url}]}]}

    def migas_simple(self, nombre):
        return f'<nav class="migas" aria-label="{e(self.U["aria_ruta"])}"><a href="{self.home}">{e(self.U["inicio"])}</a> / <span>{e(nombre)}</span></nav>'

    def pagina_soporte(self):
        d = self.d
        url = URL + self.r('soporte')
        guias = '\n'.join(f'        <li><a href="{self.r(k)}">{e(t)}</a></li>' for k, t in d.OTRAS_GUIAS)
        cuerpo = d.SOPORTE_HTML
        for k in ('lg', 'samsung', 'roku', 'android', 'guias'):
            cuerpo = cuerpo.replace(f'@@R_{k}@@', self.r(k))
        cuerpo = cuerpo.replace('@@GUIAS@@', guias)
        return (self.cabecera(d.SOPORTE['titulo'], d.SOPORTE['desc'], url, 'soporte', '#e0457b', 'website', self.ld_simple(d.SOPORTE['h1'], url))
                + f'''      {self.migas_simple(d.SOPORTE['h1'])}
      <h1>{e(d.SOPORTE['h1'])}</h1>
      <p>{d.SOPORTE['intro']}</p>
    </div>
  </div>

  <main class="contenedor">
    <div class="documento">
{cuerpo}    </div>
  </main>

''' + self.pie('soporte'))

    def pagina_privacidad(self):
        d = self.d
        url = URL + self.r('privacidad')
        return (self.cabecera(d.PRIVACIDAD['titulo'], d.PRIVACIDAD['desc'], url, 'privacidad', '#e0457b', 'website', self.ld_simple(d.PRIVACIDAD['h1'], url))
                + f'''      {self.migas_simple(d.PRIVACIDAD['h1'])}
      <h1>{e(d.PRIVACIDAD['h1'])}</h1>
      <p>{e(d.PRIVACIDAD['intro'])}</p>
    </div>
  </div>

  <main class="contenedor">
    <article class="documento">
{d.PRIVACIDAD_HTML}    </article>
  </main>

''' + self.pie('privacidad'))

    # ------------------------------------------------------------------ escritura
    def escribir(self, clave, texto):
        carpeta = I.carpeta(clave, self.cod)
        if carpeta.endswith('.html'):
            destino = os.path.join(SITIO, *carpeta.split('/'))
        else:
            d = os.path.join(SITIO, *carpeta.split('/'))
            os.makedirs(d, exist_ok=True)
            destino = os.path.join(d, 'index.html')
        os.makedirs(os.path.dirname(destino), exist_ok=True)
        open(destino, 'w', encoding='utf-8', newline='\n').write(texto)
        print('ok', self.r(clave))

    def generar(self):
        for m in self.d.MARCAS:
            self.escribir(m['clave'], self.pagina_marca(m))
        self.escribir('guias', self.indice())
        for g in self.d.GUIAS:
            self.escribir(g['clave'], self.pagina_guia(g))
        self.escribir('soporte', self.pagina_soporte())
        self.escribir('privacidad', self.pagina_privacidad())


pedidos = [a for a in sys.argv[2:]] or [l for l in I.ACTIVOS if l not in ('es', 'en')]
for cod in pedidos:
    assert cod in I.ACTIVOS, f'{cod} no está en ACTIVOS de idiomas_sitio.py'
    Idioma(cod).generar()
