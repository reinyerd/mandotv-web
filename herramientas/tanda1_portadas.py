# Tanda 1 de la evaluación del 26-nov (Web 1, 3 y 4) en las portadas: cambios exactos, uno por uno, con su texto
# viejo y nuevo por idioma (herramientas/tanda1_textos.json). Falla si un texto viejo no aparece las veces esperadas.
# Uso: python -I -X utf8 herramientas/tanda1_portadas.py <carpeta del sitio> [idiomas...]
import json, os, re, sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import idiomas_sitio as I

SITIO = sys.argv[1]
_AQUI = os.path.dirname(os.path.abspath(__file__))
TX = json.load(open(os.path.join(_AQUI, 'tanda1_textos.json'), encoding='utf-8'))
_DIR = os.path.join(_AQUI, 'tanda1')  # un archivo por idioma (<k>.json), mismo formato que una entrada de TX
if os.path.isdir(_DIR):
    for _f in sorted(os.listdir(_DIR)):
        if _f.endswith('.json'):
            TX[_f[:-5]] = json.load(open(os.path.join(_DIR, _f), encoding='utf-8'))
PLANES_FIN = '\n          </ul>\n        </div>\n      </div>\n    </section>'


def portada(k):
    c = I.ruta('home', k).strip('/')
    return os.path.join(SITIO, c, 'index.html') if c else os.path.join(SITIO, 'index.html')


def aplicar(k, t):
    ruta = portada(k)
    s = open(ruta, encoding='utf-8').read()
    errores = []
    for par in t['cambios']:
        viejo, nuevo, veces = par['viejo'], par['nuevo'], par.get('veces', 1)
        n = s.count(viejo)
        if (nuevo and s.count(nuevo) >= veces) or (not nuevo and n == 0):
            continue  # ya aplicado (también cuando el texto viejo es parte del nuevo)
        if n != veces:
            errores.append(f'{k}: {n} apariciones (se esperaban {veces}) de: {viejo[:90]}')
            continue
        s = s.replace(viejo, nuevo)
    # Web 1: botón de descarga bajo las tarjetas de precio (mismo destino que el principal; app.js lo sincroniza).
    if 'id="precio-descargar"' not in s:
        if s.count(PLANES_FIN) != 1:
            errores.append(f'{k}: no se encontró el cierre de .planes')
        else:
            bloque = ('\n          </ul>\n        </div>\n      </div>\n'
                      '      <div class="precio-accion aparece">\n'
                      f'        <a class="boton" id="precio-descargar" href="#tiendas">{t["boton"]}</a>\n'
                      f'        <p>{t["nota"]}</p>\n'
                      '      </div>\n    </section>')
            s = s.replace(PLANES_FIN, bloque)
    for m in re.finditer(r'<script type="application/ld\+json">(.*?)</script>', s, re.S):
        json.loads(m.group(1))  # el JSON-LD sigue siendo válido
    if errores:
        return errores
    open(ruta, 'w', encoding='utf-8', newline='\n').write(s)
    return []


if __name__ == '__main__':
    pedidos = sys.argv[2:] or list(TX)
    todos = []
    for k in pedidos:
        todos += aplicar(k, TX[k])
    print('\n'.join(todos) or f'OK: {len(pedidos)} portadas')
    sys.exit(1 if todos else 0)
