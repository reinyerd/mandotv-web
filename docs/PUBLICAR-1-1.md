# Publicar la web de la 1.1 (rama `web-1-1`)

Preparado el 22-nov-2026. **Se publica solo con el sí del fundador** a la comparación privada
https://claude.ai/artifact/SJMuTCAYnFpC9fsNQ6bx7H (publicado contra propuesta, escritorio 1440 px, celular 375 px y
con "reducir movimiento"). El sí incluye fusionar `web-1-1-mac` y `web-1-1-windows` el día que cada tienda los
publique, sin volver a preguntar.

## Estado

**Publicada el 22-nov (~21:12 hora de Chile), commit `db8181b` en `main`**, con el sí del fundador. Comprobado en vivo:
las 7 páginas responden 200 con los textos nuevos, Descargar va a Microsoft Store en Windows y a App Store en iPhone y
Mac, sin errores de consola ni desplazamiento lateral. IndexNow aceptó las 7 URL (HTTP 200). Search Console: sitemap
reenviado ("Se ha enviado el sitemap correctamente"). Bing: sitemap reenviado ("successfully submitted").
**Pendiente:** pedir la indexación de las 7 URL en Search Console (Inspección de URL > Solicitar indexación). El 22-nov
Google respondió "Cuota superada" (el cupo diario ya se había usado); hacerlo el 23-nov, la portada en español primero.
`web-1-1-mac` y `web-1-1-windows` siguen sin fusionar, esperando a sus tiendas.

## Qué lleva cada rama

| Rama | Se sube cuando | Qué cambia |
|---|---|---|
| `web-1-1` | El fundador dice que sí | Lo que trae la 1.1 de iPhone y iPad (a la venta desde el 22-nov): duplicar pantalla con la función del iPhone y el iPad (gratis), widgets, Centro de control, Siri y Atajos (Pro, beta), 30 idiomas y voz en 29 (Pro) "en iPhone y iPad", modo audífonos en LG (Pro). "Pronto" para duplicar en Android y Windows y para el widget de Android. La sección de la prueba de Android dice que ya trae la 1.1. 6 portadas, guía en inglés sin suscripción y llms.txt. |
| `web-1-1-mac` | App Store muestra la 1.1 para Mac (READY_FOR_SALE de la versión MAC_OS) | "Mac" en antetítulo, Tu equipo (en un Mac se elige solo; Descargar va a la App Store, compra universal), pie de todas las páginas, nota de las páginas de marca (6 idiomas), "¿Dónde lo descargo?", operatingSystem y llms.txt. |
| `web-1-1-windows` | Microsoft Store muestra la 1.1 (no basta con que pase la certificación: que esté publicada) | Duplicar con Windows + K (gratis) y el duplicado propio a TV LG, Samsung, Hisense y Android TV (Pro, beta, unos segundos de demora y sin sonido). Los 30 idiomas y la voz en 29 pasan a "iPhone, iPad y Windows". |

Las dos ramas salen de `web-1-1` y se fusionan entre sí sin conflictos (probado con `git merge-tree`). Si se fusiona
`web-1-1` de nuevo (por ejemplo tras otro cambio en `main`), rehacer las ramas con los scripts de la sesión que las
creó o resolver a mano: son cambios de texto chicos.

## Pasos al recibir el sí

1. En `C:\server\htdocs\mandotv-web` (en `main`, limpio): `git fetch` y `git merge --no-ff web-1-1`. Si `main` avanzó y
   choca en los `?v=` o en el bloque JSON-LD de las portadas, quedarse con el texto de `web-1-1` y recalcular.
2. `python -I herramientas/pie_firma.py` y `python -I herramientas/versionar.py` (un merge no corre el hook de
   pre-commit); si cambian archivos, commit. `versionar.py` también deja en `sitemap.xml` el `lastmod` de hoy en las
   páginas cambiadas.
3. Revisar antes de subir: abrir la portada en escritorio y celular (Edge sin interfaz o Playwright, con "reducir
   movimiento"), JSON-LD válido en las 6 portadas y enlaces sin fallas.
4. `git push origin main` (GitHub Pages publica en ~1 min). Comprobar en vivo con `curl -s https://mandotv.app/ | grep
   "Duplica la pantalla"` y lo mismo en /en/, /pt/, /fr/, /de/ y /it/.
5. Indexación (orden por importancia; Search Console tiene límite diario de pedidos):
   1. IndexNow (Bing, Yandex, Seznam, Naver):
      `python -I herramientas/indexnow.py --urls https://mandotv.app/ https://mandotv.app/en/ https://mandotv.app/pt/ https://mandotv.app/fr/ https://mandotv.app/de/ https://mandotv.app/it/ https://mandotv.app/en/guides/tv-remote-app-no-subscription/`
   2. Google Search Console, propiedad `sc-domain:mandotv.app` (sesión abierta en el navegador integrado; usar una
      pestaña nueva y nunca cerrar sesión): Sitemaps > volver a enviar `https://mandotv.app/sitemap.xml`; luego
      Inspección de URL > "Solicitar indexación" para: `/`, `/en/`, `/pt/`, `/de/`, `/fr/`, `/it/`,
      `/en/guides/tv-remote-app-no-subscription/`.
   3. Bing Webmaster Tools (`https://www.bing.com/webmasters/sitemaps?siteUrl=https://mandotv.app/`, sesión abierta):
      volver a enviar el sitemap; las URL ya van por IndexNow.
   4. Comprobar en la fuente: en Search Console, cada URL dice "Indexación solicitada"; en Bing, el sitemap con la fecha
      de hoy y Success. Si algo no se puede (sesión caída, límite diario), anotarlo en `docs/ESTADO.md` del proyecto
      Mando y avisar al fundador en una línea.
6. Al fusionar después `web-1-1-mac` o `web-1-1-windows`: mismos pasos 1 a 5. Mac cambia el pie de todas las páginas:
   pedir indexación solo de las 6 portadas y de las 4 páginas de marca en español (las demás van por sitemap e
   IndexNow). Windows: las 6 portadas y la guía en inglés sin suscripción.

Estado comprobado el 22-nov (solo lectura): Search Console y Bing tienen la sesión abierta; el sitemap se leyó hoy en
los dos (153 URL, sin errores).

## Cuando Android salga a producción (~30-nov), a mano

No hay rama: toca las mismas frases que la de Windows. Los textos originales en los 6 idiomas están en el commit
`e962a23` de esta rama (`git show e962a23:index.html` y lo mismo en en/, pt/, fr/, de/, it/).
- Tarjeta "Duplica la pantalla": sumar Transmitir en Android y quitar "Pronto en Android".
- Tarjeta "Sin abrir la app (Pro)": cambiar "En Android llega con su versión pública" por el widget de inicio.
- Volver a poner la tarjeta "Más aparatos por infrarrojo (beta)" y su línea en el plan Gratis y el featureList.
- Planes, featureList, pregunta de idiomas y llms.txt: quitar "en iPhone y iPad" (o "iPhone, iPad y Windows") de los
  30 idiomas y la voz en 29: ahí ya estarán en todas las plataformas, Mac incluido.
- Sección de la prueba anticipada: cambiarla por el enlace de Google Play y la insignia oficial (regla de enlaces de
  tiendas) y quitar la nota "En Android es una prueba anticipada" de `app.js`.
- Reloj Wear OS: solo cuando Google lo publique (regla de `docs/PRO.md` del proyecto Mando). Texto en `e962a23`.
Esto es un cambio visible grande: comparación lado a lado y sí del fundador antes de subirlo.

## Detalles que conviene saber

- Con Mac y Windows fusionados, los idiomas dicen "iPhone, iPad y Windows" sin nombrar el Mac (la 1.1 de Mac también
  los tiene). No es falso, solo dice de menos; se arregla al quitar el calificativo con Android.
- La tarjeta de Infrarrojo de "WiFi, infrarrojo y Bluetooth" ya estaba publicada como "Nuevo" (Android, prueba
  anticipada) y no se tocó.
- Frases de Siri: la app usa el nombre "Mando TV" (`CFBundleDisplayName`), así que la web cita "Silencia el TV con
  Mando TV" y su traducción exacta de `ios/Runner/<idioma>.lproj/AppShortcuts.strings`.
