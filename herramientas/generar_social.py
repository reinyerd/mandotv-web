# Genera las fuentes de las imágenes para compartir por idioma (herramientas/social-<idioma>.html) a partir de social.html.
# Los rótulos del teléfono salen de la portada de cada idioma (mismo orden que social.html), así coinciden con la página.
# Después se saca cada captura de 1200x630 (social.png es el español):
#   python -m http.server 8090 (en la raíz del sitio) y, por idioma:
#   msedge --headless --hide-scrollbars --virtual-time-budget=8000 --screenshot=social-en.png --window-size=1200,630 http://127.0.0.1:8090/herramientas/social-en.html
# Uso: python -I herramientas/generar_social.py <carpeta del sitio>
import os, re, sys

sys.dont_write_bytecode = True
SITIO = sys.argv[1]

# idioma: (portada, título, subtítulo, tamaño del título en px o None, rótulo de la TV del teléfono o None)
IDIOMAS = {
  'en': ('index.html', 'One remote for all your TVs', 'Free, no ads and no accounts.', None, None),
  'de': ('de/index.html', 'Eine Fernbedienung für alle TVs', 'Kostenlos, ohne Werbung und ohne Konto.', 72, 'Samsung TV'),
  'fr': ('fr/index.html', 'Une télécommande pour toutes vos TV', 'Gratuite, sans publicité et sans compte.', 74, None),
  'pt': ('pt/index.html', 'Um controle para todas as TVs', 'Grátis, sem anúncios e sem conta.', None, None),
  'it': ('it/index.html', 'Un telecomando per tutte le TV', 'Gratis, senza pubblicità e senza account.', 84, None),
}
TEXTO = re.compile(r'>([^<>]+)<')


def leer(ruta):
    return open(os.path.join(SITIO, *ruta.split('/')), encoding='utf-8').read().replace(' ', ' ')


def telefono(html):
    a = html.index('<div class="telefono"')
    return a, html.index('<div class="reflejo">', a)


base = leer('herramientas/social.html')
a0, b0 = telefono(base)
textos0 = [t for t in TEXTO.findall(base[a0:b0]) if t.strip()]
alt0 = re.search(r'id="telefono" role="img" aria-label="([^"]*)"', base)[1]

for lang, (portada, titulo, sub, tam, tv) in IDIOMAS.items():
    home = leer(portada)
    a1, b1 = telefono(home)
    bloque = home[a1:b1]
    textos1 = [t for t in TEXTO.findall(bloque) if t.strip()]
    assert len(textos0) == len(textos1), (lang, len(textos0), len(textos1))
    alt1 = re.search(r'id="telefono" role="img" aria-label="([^"]*)"', home)[1]
    if tv:  # el rótulo de la TV del teléfono (#app-tv), no el primer texto (la hora de la barra de estado)
        textos1[textos0.index(re.search(r'<span id="app-tv">([^<]*)</span>', base)[1])] = tv
    it = iter(textos1)
    nuevo = TEXTO.sub(lambda m: '>' + next(it) + '<' if m[1].strip() else m[0], base[a0:b0])
    s = base[:a0] + nuevo + base[b0:]
    s = s.replace(alt0, alt1)
    if tam:
        s = s.replace('font-size: 96px; line-height: .9;', f'font-size: {tam}px; line-height: .95;')
    s = s.replace('<html lang="es"', f'<html lang="{lang}"', 1)
    s = s.replace('Un control para todos tus TV', titulo).replace('Gratis, sin anuncios y sin cuentas.', sub)
    s = s.replace('Genera social.png', f'Genera social-{lang}.png').replace('herramientas/social.html', f'herramientas/social-{lang}.html')
    open(os.path.join(SITIO, 'herramientas', f'social-{lang}.html'), 'w', encoding='utf-8', newline='\n').write(s)
    print('ok', lang)
