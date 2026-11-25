# Agregar un idioma a mandotv.app

Proceso usado el 25-nov para los 24 idiomas que la app ya tenía. Un idioma = 35 páginas: portada, 4 marcas (LG,
Samsung, Roku, Android TV), índice de guías, 27 guías, ayuda y privacidad. La fuente es el alemán, que tiene
exactamente esas 35 páginas.

## Qué se entrega por idioma (clave del idioma = `<k>`, ver `NUEVOS` en `herramientas/idiomas_sitio.py`)

1. `herramientas/rutas/<k>.json`: `{clave de página: ruta}` con las mismas claves que tienen ruta en alemán (columna
   `de` de `_FILAS` en `idiomas_sitio.py`). Rutas sin barra inicial ni final, solo `a-z`, `0-9` y guiones.
   - Fijas: `"home": "<carpeta>"`, `"soporte": "<carpeta>/support.html"`, `"privacidad": "<carpeta>/privacy.html"`.
   - Marcas: `<carpeta>/<slug>` (por ejemplo `nl/lg-afstandsbediening`). Índice de guías: `<carpeta>/<carpeta de
     guías>` (por ejemplo `nl/gidsen`). Cada guía: `<carpeta>/<carpeta de guías>/<slug>`.
   - Alfabeto latino: slug en el idioma, como lo buscaría la gente, sin tildes (ø→o, å→a, æ→ae, ß→ss, ş→s, ı→i,
     ő→o, ă→a, ț→t, đ→d, vietnamita sin tonos). Otros alfabetos (ja, ko, zh, zh-hant, th, hi, ar, he, el, uk): el
     slug en inglés de la columna `en` (sin `en/`) y la carpeta de guías `guides`.
2. `herramientas/datos_<k con _>.py`: traducción completa de `herramientas/datos_de.py`, con la misma estructura
   exacta (mismas variables, claves, listas, cantidad y orden de elementos). Solo cambian los textos.
   - Intactos: `[texto](@clave)` (se traduce el texto, la `@clave` no), `{enlace}` y otros `{marcadores}`, las
     etiquetas HTML de `SOPORTE_HTML` y `PRIVACIDAD_HTML` (con sus atributos), `@@R_lg@@`, `@@GUIAS@@` y similares,
     las claves (`clave='lg'`), colores, fechas (`fecha=`), direcciones y correos.
   - `UI['locale']` del país principal del idioma (`nl_NL`, `ja_JP`, `zh_CN`, `zh_TW`, `nb_NO`, `ar_SA`...).
   - El comentario de arriba, en español: "Textos en <idioma> de mandotv.app. Los usa generar_idiomas.py...".
3. `<carpeta>/index.html`: la portada, traducida desde `de/index.html` (copia exacta con el texto traducido).
   - Traducir todo texto visible y los atributos de texto (`alt`, `aria-label`, `title`, `placeholder`, `content`
     de `description`, `og:title`, `og:description`, `twitter:*`), y los textos del JSON-LD (`name` de preguntas,
     `text`, `description`...; `"name": "Mando TV"` queda igual). El JSON-LD debe seguir siendo JSON válido.
   - `<html lang="de"` pasa a `<html lang="<código de hreflang>"` (y `dir="rtl"` en árabe y hebreo).
     `og:locale` = el locale de `UI`. `inLanguage` del JSON-LD = el código de hreflang.
   - `canonical` y `og:url` = `https://mandotv.app/<carpeta>/`. `og:image` = `https://mandotv.app/social-<k>.png`
     (sin `?v=`).
   - Cada enlace `/de/...` pasa a la ruta del mismo `clave` en `rutas/<k>.json` (se busca la clave por su ruta en
     alemán en `idiomas_sitio.py`), conservando `#ancla`. Ejemplo: `/de/hilfe.html` → `/<carpeta>/support.html`,
     `/de/samsung-fernbedienung/#encender` → `/<ruta de samsung>/#encender`.
   - No tocar: el bloque `<link rel="alternate" hreflang>`, el script `data-idioma-guardado`, la lista de idiomas del
     pie y el bloque entre `<!-- pie-firma -->` y `<!-- /pie-firma -->` (los ponen los scripts), clases, ids, SVG,
     scripts, estilos ni `?v=` de css/js.

## Cómo escribir

- Español de referencia de la marca: claro, cercano, seguro y sin relleno, como una app premium (Apple). Pocas
  palabras, frases directas. Nada de exageraciones ni de "la mejor app del mundo".
- No es traducción palabra por palabra: escribirlo como lo escribiría alguien de ese país, con las palabras que esa
  gente busca en Google (por ejemplo "afstandsbediening" en neerlandés, "リモコン アプリ" en japonés). Títulos de unos
  60 caracteres y descripciones de unos 150 (menos en chino, japonés y coreano).
- Trato del usuario: el que usan las apps de consumo de ese país (neerlandés je, sueco du, japonés です・ます,
  coreano 해요체, polaco forma directa, etc.).
- Los hechos no cambian: las mismas funciones, marcas compatibles, plataformas (iPhone, iPad, Mac, Android,
  Windows), "gratis, sin anuncios y sin cuenta", "Pro es una compra única, sin suscripción", Android en acceso
  anticipado en Google Play. No inventar funciones, cifras, precios, premios ni opiniones.
- Nombres que no se traducen: Mando TV, LG, Samsung, Roku, Google TV, Android TV, Fire TV, webOS, Tizen, App Store,
  Google Play, Microsoft Store, iPhone, iPad, Mac, Windows, HomeKit, Google Home y demás marcas.
- Nombres de botones y menús de la app: los mismos que usa la app en ese idioma. Están en
  `C:\server\htdocs\control\lib\l10n\app_<código>.arb` (zh-hant: `app_zh_Hant.arb`; nb: `app_nb.arb`). Buscar la clave
  con el texto alemán en `app_de.arb` y usar el valor de esa clave en el idioma (con grep; no leer el archivo entero).
- Contenido universal: ejemplos y búsquedas que usa la mayoría (música relajante, documentales, fútbol, películas),
  nunca religión ni gustos personales.
- Signos de puntuación propios del idioma (comillas „“ en alemán, « » en francés, 「」 en japonés, etc.).

## Revisar antes de entregar

```
python -I herramientas/revisar_idioma.py <k>
```

Genera las 35 páginas de ese idioma (solo en su carpeta) y revisa rutas, estructura de los datos, textos sin
traducir, portada, enlaces y páginas. Corregir hasta que diga `0 errores`. No ejecutar otros scripts que cambian
páginas (pie_firma.py, portadas_idiomas.py, versionar.py, idioma_guardado.py) ni hacer commit: eso lo hace Opus
cuando junta todos los idiomas, porque esos scripts tocan las páginas de todos los idiomas a la vez.

## Al juntar los idiomas (Opus)

1. Textos cortos de cada idioma en `herramientas/textos_idiomas.json` (pie, Microsoft Store, imagen para compartir)
   y tablas de `app.js`, `cookies.js` (aviso de cookies y aviso de idioma) y `correo.js`.
2. Sumar los idiomas revisados a `LISTOS` en `idiomas_sitio.py`, y correr `generar_idiomas.py`,
   `portadas_idiomas.py`, `pie_firma.py`, `idioma_guardado.py` y `versionar.py` (el commit corre los tres últimos).
3. Imágenes `social-<k>.png` (`generar_social.py` y captura con Edge sin ventana).
4. Revisar en el navegador: escritorio, celular, efectos de Windows apagados, árabe y hebreo de derecha a izquierda.
5. `llms.txt`, sitemap (lo hace `versionar.py`), IndexNow, Search Console y Bing.
