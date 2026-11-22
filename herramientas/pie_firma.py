"""Reemplaza la línea vieja pie-gigante por un bloque nuevo de firma en cada página.

Ejecutar manual: python herramientas/pie_firma.py
Imprime las rutas que cambió, una por línea, relativas a la raíz y con /.
"""
import datetime
import html
import pathlib
import re
import sys

RAIZ = pathlib.Path(__file__).resolve().parent.parent

IDIOMAS_ORDEN = ['es', 'en', 'pt', 'fr', 'de', 'it']

IDIOMA_NOMBRE = dict(
    es='Español',
    en='English',
    pt='Português',
    fr='Français',
    de='Deutsch',
    it='Italiano',
)

IDIOMA_TEXTO = dict(
    es=('El control remoto de todos tus televisores, en el celular o el computador.', 'Descargar', 'Para iPhone, iPad, Mac, Android y Windows', 'Idioma'),
    en=('One remote for every TV in your home, on your phone or computer.', 'Download', 'For iPhone, iPad, Mac, Android and Windows', 'Language'),
    pt=('O controle remoto de todas as suas TVs, no celular ou no computador.', 'Baixar', 'Para iPhone, iPad, Mac, Android e Windows', 'Idioma'),
    fr=('La télécommande de tous vos téléviseurs, sur votre téléphone ou votre ordinateur.', 'Télécharger', 'Pour iPhone, iPad, Mac, Android et Windows', 'Langue'),
    de=('Die Fernbedienung für alle deine Fernseher, auf dem Handy oder am Computer.', 'Herunterladen', 'Für iPhone, iPad, Mac, Android und Windows', 'Sprache'),
    it=('Il telecomando di tutte le tue TV, sullo smartphone o sul computer.', 'Scarica', 'Per iPhone, iPad, Mac, Android e Windows', 'Lingua'),
)

INICIO_LANG = dict(es='/', en='/en/', pt='/pt/', fr='/fr/', de='/de/', it='/it/')

BLOCK_INICIO = re.compile(
    r'      <!-- pie-firma: lo escribe herramientas/pie_firma.py \(no editar a mano\) -->'
    r'.*?'
    r'      <!-- /pie-firma -->',
    re.DOTALL,
)
LINEA_VIEJA = '      <p class="pie-gigante" aria-hidden="true">MANDO</p>'

HREFLANG_RE = re.compile(
    r'<link\s+rel="alternate"\s+hreflang="([\w-]+)"\s+href="https://mandotv\.app(/[^"]*)"[^>]*>'
)


def idiomas_de_pagina(pagina):
    """Devuelve un dict con los hreflang encontrados en la página."""
    texto = pagina.read_text(encoding='utf-8')
    resultados = dict()
    for m in HREFLANG_RE.finditer(texto):
        lang_code = m.group(1)
        ruta = m.group(2)
        if lang_code != 'x-default':
            resultados[lang_code] = ruta
    return resultados


def bloque_nuevo(lenguaje, hreflangs, tiene_tiendas):
    """Arma el bloque HTML de firma."""
    inicio = INICIO_LANG.get(lenguaje, '/')
    descargar_href = '#tiendas' if tiene_tiendas else inicio + '#tiendas'
    anio = datetime.date.today().year

    lema, descargar, plataformas, etiqueta = IDIOMA_TEXTO[lenguaje]

    partes_li = list()
    for cod in IDIOMAS_ORDEN:
        nombre = html.escape(IDIOMA_NOMBRE[cod])
        a_href = ' href="' + html.escape(hreflangs.get(cod, INICIO_LANG[cod])) + '"'
        a_lang = ' lang="' + cod + '"'
        a_hreflang = ' hreflang="' + cod + '"'
        cls = ''
        if cod == lenguaje:
            cls = ' aria-current="page"'
        line = '            <li><a' + a_href + a_hreflang + a_lang + cls + '>' + nombre + '</a></li>'
        partes_li.append(line)

    li_menu = '\n'.join(partes_li)

    lema_esc = html.escape(lema)
    descargar_esc = html.escape(descargar)
    plataformas_esc = html.escape(plataformas)
    etiqueta_esc = html.escape(etiqueta)
    inicio_esc = html.escape(inicio)
    descargar_href_esc = html.escape(descargar_href)

    bloque = '      <!-- pie-firma: lo escribe herramientas/pie_firma.py (no editar a mano) -->\n'
    bloque += '      <div class="pie-cierre">\n'
    bloque += '        <div class="pie-firma">\n'
    bloque += '          <a class="pie-logo" href="' + inicio_esc + '"><img src="/icono.svg" alt="" width="44" height="44" loading="lazy" decoding="async">Mando TV</a>\n'
    bloque += '          <p>' + lema_esc + '</p>\n'
    bloque += '        </div>\n'
    bloque += '        <div class="pie-accion">\n'
    bloque += '          <a class="boton" href="' + descargar_href_esc + '">' + descargar_esc + '</a>\n'
    bloque += '          <span>' + plataformas_esc + '</span>\n'
    bloque += '        </div>\n'
    bloque += '      </div>\n'
    bloque += '      <div class="pie-base">\n'
    bloque += '        <span>© ' + str(anio) + ' Mando TV</span>\n'
    bloque += '        <details class="pie-idioma">\n'
    nombre_actual = IDIOMA_NOMBRE[lenguaje]
    bloque += '          <summary><span class="oculto">' + etiqueta_esc + ': </span>' + nombre_actual + '</summary>\n'
    bloque += '          <ul>\n'
    bloque += li_menu + '\n'
    bloque += '          </ul>\n'
    bloque += '        </details>\n'
    bloque += '      </div>\n'
    bloque += '      <!-- /pie-firma -->'

    return bloque


def quitar_version(texto):
    """Quita ?v=XXXXX de todo el texto para comparar."""
    return re.sub(r'\?v=[\w-]+', '', texto)


def procesar(pagina):
    """Procesa una página. Devuelve True si se modificó, False si no cambió."""
    texto = pagina.read_text(encoding='utf-8')

    match = BLOCK_INICIO.search(texto)
    if match:
        inicio_pos, fin_pos = match.start(), match.end()
    else:
        inicio_pos = texto.find(LINEA_VIEJA)
        if inicio_pos == -1:
            return False
        fin_pos = inicio_pos + len(LINEA_VIEJA)

    lang_match = re.search(r'<html[^>]*\slang="([\w-]+)"', texto)
    lenguaje = lang_match.group(1)[:2].lower() if lang_match else 'es'
    if lenguaje not in IDIOMA_TEXTO:
        lenguaje = 'es'

    hreflangs = idiomas_de_pagina(pagina)

    tiene_tiendas = 'id="tiendas"' in texto

    nuevo_bloque = bloque_nuevo(lenguaje, hreflangs, tiene_tiendas)

    resultado = texto[:inicio_pos] + nuevo_bloque + texto[fin_pos:]

    if quitar_version(resultado) != quitar_version(texto):
        pagina.write_text(resultado, encoding='utf-8', newline='')
        return True
    return False


def main():
    carpetas_skip = set(('.git', 'herramientas', 'docs', 'node_modules'))
    cambiadas = list()

    for p in sorted(RAIZ.rglob('*.html')):
        rel = p.relative_to(RAIZ)
        if any(carpeta in rel.parts for carpeta in carpetas_skip):
            continue
        if procesar(p):
            cambiadas.append(rel.as_posix())

    for r in cambiadas:
        print(r)
    return 0


if __name__ == '__main__':
    sys.exit(main())
