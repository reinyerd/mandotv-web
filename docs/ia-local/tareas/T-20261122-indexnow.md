# T-20261122-indexnow

## Objetivo
Activar IndexNow en mandotv.app: publicar el archivo de clave en la raíz del sitio y crear un script que avisa a
IndexNow (Bing, Yandex, Seznam, Naver) de las URL del sitemap, para que Bing (fuente de ChatGPT y Copilot) las
rastree rápido.

## Contexto mínimo
1. Sitio estático en GitHub Pages (Jekyll). La raíz del repo es la raíz de https://mandotv.app/. `herramientas/` y
   `docs/` no se publican (excluidos en `_config.yml`).
2. Los scripts de `herramientas/` son Python 3 solo con la biblioteca estándar, comentarios en español, se corren
   desde la raíz del repo con `python -I herramientas/<script>.py`.
3. Protocolo IndexNow (https://www.indexnow.org/documentation): POST a `https://api.indexnow.org/indexnow` con
   cabecera `Content-Type: application/json; charset=utf-8` y cuerpo
   `{"host": "mandotv.app", "key": "<clave>", "keyLocation": "https://mandotv.app/<clave>.txt", "urlList": [...]}`.
   Máximo 10000 URL por envío. Respuestas: 200 o 202 = aceptado; 400 = formato inválido; 403 = clave no encontrada o
   no coincide; 422 = URL de otro host o clave inválida; 429 = demasiadas peticiones.
4. La clave es `39669e795b27187d81b484e104572c40`.

## Comportamiento esperado
1. Archivo `39669e795b27187d81b484e104572c40.txt` en la raíz del repo, cuyo contenido es exactamente
   `39669e795b27187d81b484e104572c40` (una sola línea, sin espacios; un salto de línea final es aceptable).
2. `herramientas/indexnow.py`:
   1. Sin argumentos: lee `sitemap.xml` de la raíz, toma todas las `<loc>` y las envía en un solo POST.
   2. Con `--urls URL1 URL2 ...`: envía solo esas URL (para avisar de páginas nuevas o cambiadas).
   3. Con `--simular`: no envía nada; imprime cuántas URL se enviarían y el cuerpo JSON (con indentación).
   4. Antes de enviar comprueba: que el archivo de clave existe en la raíz y su contenido (sin espacios ni saltos)
      es la clave; que todas las URL empiezan con `https://mandotv.app/`; que hay al menos 1 y como mucho 10000.
      Si algo falla, imprime el motivo en español y termina con código 1, sin enviar.
   5. Al enviar imprime el código HTTP y su significado en español (tabla del punto 3 del contexto). Termina con
      código 0 si fue 200 o 202, y con 1 en cualquier otro caso, incluido un error de red (capturar
      `urllib.error.HTTPError` y `urllib.error.URLError`, sin mostrar trazas de Python).
   6. Tiempo de espera de la petición: 30 segundos.
   7. Encabezado de comentario breve al inicio: para qué sirve y cómo se usa (los tres modos).

## Archivos permitidos
1. `39669e795b27187d81b484e104572c40.txt` (crear)
2. `herramientas/indexnow.py` (crear)
3. Este archivo de tarea (solo para agregar el informe al final)

## Archivos de referencia
1. `sitemap.xml` (formato de las URL)
2. `herramientas/versionar.py` (estilo de los scripts del repo; solo las primeras 30 líneas)

## Restricciones
1. No tocar ningún otro archivo: ni HTML, ni `sitemap.xml`, ni `robots.txt`, ni `_config.yml`.
2. Solo biblioteca estándar de Python (`argparse`, `json`, `re` o `xml.etree.ElementTree`, `urllib.request`,
   `pathlib`, `sys`).
3. No hacer el envío real: no hay red. Solo probar con `--simular` y los casos de error.
4. No hacer commit.

## Pruebas obligatorias (correr y pegar la salida resumida en el informe)
1. `python -I herramientas/indexnow.py --simular` debe decir 153 URL y mostrar el JSON con host, key, keyLocation.
2. `python -I herramientas/indexnow.py --simular --urls https://mandotv.app/ https://mandotv.app/en/` debe decir 2.
3. `python -I herramientas/indexnow.py --simular --urls https://otro.com/x` debe terminar con código 1 y un mensaje
   claro.

## Comprobaciones
1. `python -I herramientas/indexnow.py --simular`
2. `python -I -m py_compile herramientas/indexnow.py`
3. `git status --short` (solo deben aparecer los 2 archivos nuevos y esta tarea)

## Criterios de aceptación
1. El archivo de clave existe en la raíz con el contenido exacto.
2. Las 3 pruebas dan el resultado esperado.
3. El código no usa dependencias externas y maneja los errores de red sin trazas.
4. Solo se crearon los 2 archivos permitidos.

## Auditoría de Opus (2026-11-22)

1. Ejecutor local qwen3.6:35b: 6,9 min, 61 turnos, terminó por tope de turnos sin escribir su informe. Creó los dos
   archivos pedidos y nada más.
2. Pruebas corridas por Opus: `--simular` da 153 URL y el JSON correcto; con 2 URL da 2; con `https://otro.com/x`
   termina con código 1 y mensaje claro; `py_compile` sin errores.
3. Corregido por Opus: `leer_clave()` no comprobaba que el contenido del archivo fuera la clave (lo pedía el punto
   2.4); ahora lo compara con el nombre del archivo y sale con código 1 si no coincide (probado alterando el archivo).
   Además, salida en UTF-8 para que las tildes se vean bien en la consola de Windows.
4. Sin cambios visibles en la web: no aplica revisión de UX ni de marketing. La clave de IndexNow es pública por
   diseño (debe estar publicada en la raíz); no es un secreto.
5. Aprobado por Opus.
