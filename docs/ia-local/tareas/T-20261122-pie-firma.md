# T-20261122-pie-firma

## Objetivo
Crear `herramientas/pie_firma.py`, un script de Python que cambia el final del pie de todas las páginas del sitio:
reemplaza la línea vieja `<p class="pie-gigante" aria-hidden="true">MANDO</p>` por un bloque nuevo (firma con logo y
lema, botón Descargar, copyright y selector de idioma), y conectarlo al hook `herramientas/hooks/pre-commit`.

## Contexto mínimo
- Sitio estático (GitHub Pages) en 6 idiomas. La raíz del repo es la carpeta del sitio. Python 3, solo biblioteca
  estándar. Mira `herramientas/versionar.py`: sigue su mismo estilo (RAIZ con pathlib, `main()` que imprime las
  rutas cambiadas, una por línea, relativas a la raíz y con `/`; `sys.exit(main())`).
- Cada página tiene `<html lang="xx" ...>` (es, en, pt, fr, de o it; usar las 2 primeras letras; si falta, `es`).
- Casi todas las páginas tienen en `<head>` enlaces como
  `<link rel="alternate" hreflang="en" href="https://mandotv.app/en/lg-tv-remote/">` (uno por idioma y uno
  `x-default`, que se ignora). La ruta que se usa es la parte después de `https://mandotv.app` (por ejemplo
  `/en/lg-tv-remote/`).
- 154 páginas tienen hoy, con 6 espacios de sangría, la línea exacta:
  `      <p class="pie-gigante" aria-hidden="true">MANDO</p>`
- El hook `versionar.py` agrega `?v=<10 hex>` a las rutas de imágenes, así que `/icono.svg` puede terminar como
  `/icono.svg?v=abc123def0` dentro del bloque ya escrito.
- Textos visibles en el idioma de la página: se usan tal cual, sin traducir nada más.

## Comportamiento esperado
1. Recorre `RAIZ.rglob('*.html')` y salta todo lo que tenga en su ruta relativa una carpeta `.git`, `herramientas`,
   `docs` o `node_modules`.
2. En cada archivo busca, en este orden:
   a. un bloque ya escrito: desde la línea `      <!-- pie-firma: lo escribe herramientas/pie_firma.py (no editar a mano) -->`
      hasta la línea `      <!-- /pie-firma -->` inclusive; o
   b. la línea vieja `      <p class="pie-gigante" aria-hidden="true">MANDO</p>`.
   Si no encuentra ninguno, no toca el archivo.
3. Arma el bloque nuevo (plantilla exacta abajo) y lo pone en ese lugar. Solo escribe el archivo si el bloque cambió.
   Para comparar, quita antes `?v=` seguido de letras, números o guiones en ambos textos (así no reescribe páginas
   solo porque versionar.py ya puso la versión del ícono). Escribe con `encoding='utf-8', newline=''` y conserva el
   resto del archivo byte por byte.
4. Valores:
   - `{inicio}`: portada del idioma de la página: es `/`, en `/en/`, pt `/pt/`, fr `/fr/`, de `/de/`, it `/it/`.
   - `{descargar_href}`: `#tiendas` si el archivo contiene `id="tiendas"`; si no, `{inicio}#tiendas`.
   - `{anio}`: `datetime.date.today().year`.
   - Idiomas del menú, siempre en este orden y con estos nombres: es Español, en English, pt Português,
     fr Français, de Deutsch, it Italiano. La ruta de cada uno es la de su `hreflang` en esa página; si la página no
     tiene `hreflang` de ese idioma, se usa la portada de ese idioma. El del idioma de la página lleva
     `aria-current="page"` (y nada más cambia).
   - Textos por idioma:
     | idioma | lema | descargar | plataformas | etiqueta |
     |---|---|---|---|---|
     | es | El control remoto de todos tus televisores, en el celular o el computador. | Descargar | Para iPhone, iPad, Android y Windows | Idioma |
     | en | One remote for every TV in your home, on your phone or computer. | Download | For iPhone, iPad, Android and Windows | Language |
     | pt | O controle remoto de todas as suas TVs, no celular ou no computador. | Baixar | Para iPhone, iPad, Android e Windows | Idioma |
     | fr | La télécommande de tous vos téléviseurs, sur votre téléphone ou votre ordinateur. | Télécharger | Pour iPhone, iPad, Android et Windows | Langue |
     | de | Die Fernbedienung für alle deine Fernseher, auf dem Handy oder am Computer. | Herunterladen | Für iPhone, iPad, Android und Windows | Sprache |
     | it | Il telecomando di tutte le tue TV, sullo smartphone o sul computer. | Scarica | Per iPhone, iPad, Android e Windows | Lingua |
5. Plantilla exacta del bloque (6 espacios de sangría base, cada `<li>` en su línea; `{nombre_actual}` es el nombre
   del idioma de la página):
```
      <!-- pie-firma: lo escribe herramientas/pie_firma.py (no editar a mano) -->
      <div class="pie-cierre">
        <div class="pie-firma">
          <a class="pie-logo" href="{inicio}"><img src="/icono.svg" alt="" width="44" height="44" loading="lazy" decoding="async">Mando TV</a>
          <p>{lema}</p>
        </div>
        <div class="pie-accion">
          <a class="boton" href="{descargar_href}">{descargar}</a>
          <span>{plataformas}</span>
        </div>
      </div>
      <div class="pie-base">
        <span>© {anio} Mando TV</span>
        <details class="pie-idioma">
          <summary><span class="oculto">{etiqueta}: </span>{nombre_actual}</summary>
          <ul>
            <li><a href="{ruta_es}" hreflang="es" lang="es">Español</a></li>
            <li><a href="{ruta_en}" hreflang="en" lang="en">English</a></li>
            <li><a href="{ruta_pt}" hreflang="pt" lang="pt">Português</a></li>
            <li><a href="{ruta_fr}" hreflang="fr" lang="fr">Français</a></li>
            <li><a href="{ruta_de}" hreflang="de" lang="de">Deutsch</a></li>
            <li><a href="{ruta_it}" hreflang="it" lang="it">Italiano</a></li>
          </ul>
        </details>
      </div>
      <!-- /pie-firma -->
```
   (en el `<li>` del idioma actual: `... lang="es" aria-current="page">Español</a>`.)
6. Escapa `&`, `<`, `>` y `"` en los textos y rutas que pongas en el HTML (`html.escape`).
7. Imprime las rutas cambiadas, una por línea, y termina con código 0.
8. Hook: en `herramientas/hooks/pre-commit`, ANTES de la línea que llama a `versionar.py`, agrega lo mismo para
   `pie_firma.py` (llamada con `python -I`, falla con mensaje "pie_firma.py falló" y `exit 1`, y `git add` de cada
   ruta impresa, quitando `\r` igual que hace el hook con versionar). Conserva finales de línea LF en el hook.

## Archivos permitidos
- `herramientas/pie_firma.py` (nuevo)
- `herramientas/hooks/pre-commit`
- Las páginas `*.html` del sitio, solo al ejecutar el script (no a mano).

## Archivos de referencia
- `herramientas/versionar.py` (estilo y contrato de salida)
- `index.html` línea ~410 y `en/control-remoto-lg` equivalentes: `control-remoto-lg/index.html` (hreflang en líneas 12 a 18)

## Restricciones
- No tocar `estilos.css`, `app.js`, `cookies.js`, los generadores `herramientas/generar_*.py` ni ningún otro archivo.
- Sin dependencias nuevas. Sin git commit ni push.

## Pruebas obligatorias
Ejecuta y copia en el informe la salida resumida de cada paso:
1. `python -I herramientas/pie_firma.py | wc -l` → debe ser 154.
2. `python -I herramientas/pie_firma.py | wc -l` otra vez → debe ser 0 (idempotente).
3. `python -I herramientas/versionar.py > /dev/null; python -I herramientas/pie_firma.py | wc -l` → 0.
4. `grep -c 'pie-gigante' index.html` → 0, y `grep -rl 'pie-firma: lo escribe' --include=*.html . | wc -l` → 154.
5. Muestra el bloque resultante de `en/lg-tv-remote/index.html` (o la página inglesa de LG que exista) y comprueba
   que el enlace Español apunta a `/control-remoto-lg/` y que English lleva `aria-current="page"`.

## Comprobaciones
python -I herramientas/pie_firma.py ; python -I -c "import ast,sys; ast.parse(open('herramientas/pie_firma.py',encoding='utf-8').read())"

## Criterios de aceptación
- 154 páginas con el bloque nuevo, ninguna con la línea vieja, resto del HTML intacto (`git diff --stat` solo muestra
  las páginas, el script y el hook).
- Segunda ejecución sin cambios, también después de versionar.py.
- Rutas de idioma correctas tomadas de cada página; portada del idioma cuando falta el hreflang.

## Informe (lo escribe Opus: el ejecutor no alcanzó a escribirlo)
- qwen3.6:35b, 8,3 min, cortado por el límite de 60 turnos (error_max_turns) sin correr las pruebas ni tocar el hook.
- El script que dejó armaba bien el bloque, pero al reemplazar cortaba texto después del pie (rebanaba el texto ya
  sin la línea vieja con las posiciones del original). Opus lo corrigió, tomó solo las 2 letras de `lang`, limpió
  variables sin uso y conectó el hook.
- Pruebas (Opus): 154 páginas cambiadas, segunda pasada 0, después de versionar.py 0; ninguna página con la línea vieja;
  rutas de idioma correctas en la página inglesa de LG y en las guías; revisión de las 155 páginas con el servidor
  local, en celular con tema oscuro y movimiento reducido, más las 6 portadas: 0 fallas.
