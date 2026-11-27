# Tanda 2 del jurado de diseño (27-nov) en las 30 portadas, con los textos de herramientas/tanda2/<k>.json:
# - funciones 8, 9 y 10 más cortas (mismo contenido y misma división Gratis/Pro);
# - título de la sección de marcas más claro ("Busca la marca de tu TV");
# - nota bajo los planes: Pro se compra una vez y se restaura con la misma cuenta de la tienda;
# - cierre final con el ícono, frase y botón de descarga (app.js le da el destino de la tienda del equipo);
# - botón de modo claro/oscuro en la barra y /tema.js en el <head> (oscuro por defecto, sin parpadeo).
# Es idempotente: se puede correr de nuevo y deja lo mismo. Falla (sin escribir) si no encuentra lo que debe cambiar.
# Uso: python -I -X utf8 herramientas/tanda2_portadas.py <carpeta del sitio> [idiomas...]
import html, json, os, re, sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import idiomas_sitio as I

AQUI = os.path.dirname(os.path.abspath(__file__))
DIR = os.path.join(AQUI, 'tanda2')
CLAVES = ['f8', 'f9', 'f10', 'marcas_h2', 'nota_pro', 'cierre_h2', 'cierre_p', 'tema_claro']

SOL = ('<svg class="ico-sol" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="4"/>'
       '<path d="M12 2.5v2M12 19.5v2M2.5 12h2M19.5 12h2M5.3 5.3l1.4 1.4M17.3 17.3l1.4 1.4M5.3 18.7l1.4-1.4M17.3 6.7l1.4-1.4"/></svg>')
LUNA = '<svg class="ico-luna" viewBox="0 0 24 24" aria-hidden="true"><path d="M20 14.5A8 8 0 0 1 9.5 4a8 8 0 1 0 10.5 10.5z"/></svg>'


def portada(sitio, k):
    c = I.ruta('home', k).strip('/')
    return os.path.join(sitio, c, 'index.html') if c else os.path.join(sitio, 'index.html')


def e(s):
    return html.escape(s, quote=False)


def aplicar(sitio, k, t):
    ruta = portada(sitio, k)
    s = open(ruta, encoding='utf-8').read()
    errores = []

    # 1. Funciones 8, 9 y 10: solo el texto del <span>, el titular <b> queda igual.
    m = re.search(r'<ul class="lista-funciones">(.*?)</ul>', s, re.S)
    if not m:
        errores.append('no está .lista-funciones')
    else:
        items = re.findall(r'<li class="aparece"><b>.*?</b><span>.*?</span></li>', m.group(1), re.S)
        if len(items) != 10:
            errores.append(f'.lista-funciones tiene {len(items)} funciones (se esperaban 10)')
        else:
            bloque = m.group(1)
            for n, clave in ((8, 'f8'), (9, 'f9'), (10, 'f10')):
                viejo = items[n - 1]
                nuevo = re.sub(r'<span>.*?</span>', lambda _: f'<span>{e(t[clave])}</span>', viejo, count=1, flags=re.S)
                bloque = bloque.replace(viejo, nuevo, 1)
            s = s[:m.start(1)] + bloque + s[m.end(1):]

    # 2. Título de la sección de marcas.
    s, n = re.subn(r'(<h2 class="titulo-seccion aparece" id="t-marcas">).*?(</h2>)', lambda x: x.group(1) + e(t['marcas_h2']) + x.group(2), s, count=1, flags=re.S)
    if n != 1:
        errores.append('no está el h2 #t-marcas')

    # 3. Nota bajo los planes.
    s, n = re.subn(r'(<div class="precio-accion aparece">\s*<a class="boton" id="precio-descargar"[^>]*>(.*?)</a>\s*<p>).*?(</p>)',
                   lambda x: x.group(1) + e(t['nota_pro']) + x.group(3), s, count=1, flags=re.S)
    if n != 1:
        errores.append('no está .precio-accion')
    boton = re.search(r'id="precio-descargar"[^>]*>(.*?)</a>', s, re.S)
    texto_boton = boton.group(1).strip() if boton else None
    if not texto_boton:
        errores.append('no está el texto de #precio-descargar')

    # 4. Botón de tema en la barra, antes de Descargar (app.js lo muestra; sin JS queda oculto).
    boton_tema = (f'<button class="barra-tema" type="button" hidden aria-pressed="false" aria-label="{html.escape(t["tema_claro"])}" '
                  f'title="{html.escape(t["tema_claro"])}">{SOL}{LUNA}</button>')
    if 'class="barra-tema"' in s:
        s = re.sub(r'<button class="barra-tema".*?</button>', lambda _: boton_tema, s, count=1, flags=re.S)
    else:
        s, n = re.subn(r'(\n(\s*)<a class="boton-barra")', lambda x: '\n' + x.group(2) + boton_tema + x.group(1), s, count=1)
        if n != 1:
            errores.append('no está .boton-barra en la barra')

    # 5. /tema.js en el <head>, justo antes de la hoja de estilos (se lee antes de pintar: sin parpadeo).
    if 'src="/tema.js' not in s:
        s, n = re.subn(r'(\n(\s*)<link rel="stylesheet" href="/estilos\.css)', lambda x: '\n' + x.group(2) + '<script src="/tema.js"></script>' + x.group(1), s, count=1)
        if n != 1:
            errores.append('no está el <link> de estilos.css')

    # 6. Cierre final, después de Contacto.
    cierre = ('    <section id="empezar" class="cierre" aria-labelledby="t-empezar">\n'
              '      <img class="cierre-icono aparece" src="/icono.svg" alt="Mando TV" width="88" height="88" loading="lazy">\n'
              f'      <h2 class="titulo-seccion aparece" id="t-empezar">{e(t["cierre_h2"])}</h2>\n'
              f'      <p class="intro aparece">{e(t["cierre_p"])}</p>\n'
              f'      <a class="boton aparece" id="cierre-descargar" href="#tiendas">{texto_boton or ""}</a>\n'
              '    </section>\n')
    if 'id="empezar"' in s:
        s = re.sub(r'    <section id="empezar".*?</section>\n', lambda _: cierre, s, count=1, flags=re.S)
    else:
        s, n = re.subn(r'(<section id="contacto".*?</section>\n)', lambda x: x.group(1) + '\n' + cierre, s, count=1, flags=re.S)
        if n != 1:
            errores.append('no está la sección #contacto')

    for m in re.finditer(r'<script type="application/ld\+json">(.*?)</script>', s, re.S):
        json.loads(m.group(1))
    if errores:
        return [f'{k}: {x}' for x in errores]
    open(ruta, 'w', encoding='utf-8', newline='\n').write(s)
    return []


if __name__ == '__main__':
    sitio = sys.argv[1]
    textos = {f[:-5]: json.load(open(os.path.join(DIR, f), encoding='utf-8')) for f in sorted(os.listdir(DIR)) if f.endswith('.json')}
    pedidos = sys.argv[2:] or list(textos)
    todos = []
    for k in pedidos:
        t = textos.get(k)
        faltan = [c for c in CLAVES if not (t or {}).get(c)]
        if faltan:
            todos.append(f'{k}: faltan textos {faltan}')
            continue
        todos += aplicar(sitio, k, t)
    print('\n'.join(todos) if todos else f'OK: {len(pedidos)} portadas')
    sys.exit(1 if todos else 0)
