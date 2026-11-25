"""Pone en el <head> de cada página con gemelas en otros idiomas el script corto del idioma recordado (25-nov).

Si la persona eligió un idioma antes (lo guarda cookies.js en localStorage 'mandotv-idioma' al tocar un idioma del pie,
de la barra o del aviso) y entra desde fuera del sitio a una página en otro idioma, el script la lleva a la gemela en
su idioma antes de pintar (location.replace, así "Atrás" no vuelve a la página que cambió). Solo va a una dirección
de los <link rel="alternate" hreflang> de la propia página, nunca a una que venga de afuera. Los robots no guardan
nada, así que ven cada versión tal cual (Google desaconseja redirigir adivinando el idioma; esto recuerda una elección).
Va justo después del último hreflang porque necesita esos enlaces ya leídos.

Se ejecuta solo antes de cada commit (herramientas/hooks/pre-commit). Uso manual: python -I herramientas/idioma_guardado.py
Imprime las páginas que cambió, relativas a la raíz y con /.
"""
import pathlib
import re
import sys

RAIZ = pathlib.Path(__file__).resolve().parent.parent

SCRIPT = (
    '  <script data-idioma-guardado>(function(){try{var d=document,p=localStorage.getItem("mandotv-idioma"),'
    'h=(d.documentElement.lang||"").toLowerCase();'
    'if(!p||!/^[a-z]{2,3}(-[a-z]{2,4})?$/.test(p)||p===h||p===h.split("-")[0])return;'
    'if(d.referrer&&new URL(d.referrer).host===location.host)return;'
    'var l=d.querySelectorAll(\'link[rel="alternate"][hreflang]\'),aqui=location.origin+location.pathname;'
    'for(var i=0;i<l.length;i++)if(l[i].hreflang.toLowerCase()===p&&l[i].href!==aqui){'
    'sessionStorage.setItem("mandotv-idioma-desde",h);location.replace(l[i].href+location.search+location.hash);return}'
    '}catch(e){}})()</script>\n'
)
VIEJO = re.compile(r'[ \t]*<script data-idioma-guardado>.*?</script>\n', re.DOTALL)
ALTERNOS = re.compile(r'(?:[ \t]*<link rel="alternate" hreflang="[\w-]+" href="[^"]*">\n)+')


def procesar(pagina):
    texto = pagina.read_text(encoding='utf-8')
    limpio = VIEJO.sub('', texto)
    m = ALTERNOS.search(limpio)
    nuevo = limpio[:m.end()] + SCRIPT + limpio[m.end():] if m else limpio
    if nuevo != texto:
        pagina.write_text(nuevo, encoding='utf-8', newline='')
        return True
    return False


def main():
    saltar = {'.git', 'herramientas', 'docs', 'node_modules'}
    for p in sorted(RAIZ.rglob('*.html')):
        rel = p.relative_to(RAIZ)
        if any(c in rel.parts for c in saltar):
            continue
        if procesar(p):
            print(rel.as_posix())
    return 0


if __name__ == '__main__':
    sys.exit(main())
