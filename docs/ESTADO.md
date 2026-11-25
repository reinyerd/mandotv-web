# Estado de la web mandotv.app

## 25-nov: web en 30 idiomas e idioma recordado (EN CURSO, rama `web-idiomas-30`, carpeta `mandotv-web-idiomas`)

Pedido del fundador: traducir la web a los 24 idiomas que la app ya tiene (hoy 6), y que el idioma elegido se
recuerde (antes el aviso salía una vez y después no dejaba cambiar). Decisión del panel: recordar la elección (pie,
barra, aviso o cerrar el aviso) y, al volver desde fuera, llevar a la gemela en ese idioma (script del `<head>`,
`herramientas/idioma_guardado.py`, corre en el pre-commit) + botón de idioma (globo) en la barra. Commits `a1f5d6e6`
(idioma recordado) y `cc0f16d0` (base 30 idiomas, sección Casa de la privacidad en de/fr). Proceso y reglas en
`docs/AGREGAR-IDIOMA.md`; revisor `herramientas/revisar_idioma.py <k>`.
- 25 agentes Sonnet en segundo plano: 1 hace las tablas cortas (app.js, cookies.js, correo.js y
  `herramientas/textos_idiomas.json`); 24 traducen cada idioma (rutas, datos, portada).
- Falta al juntar: sumar a `LISTOS` los que den 0 errores, correr generadores y scripts, imágenes social-<k>.png,
  `:lang(vi)` con fuente del sistema, revisar RTL (ar, he), llms.txt, comparación lado a lado y OK del fundador,
  publicar, IndexNow, Search Console y Bing.
### Avance 25-nov (sesión de retoma, tras cortarse los 25 agentes)

Recuento real hecho con el revisor idioma por idioma (no con la lista de memoria):
- 0 errores ya: `da`, `nl`, `nb`, `sv`, `zh-hant`, `fi`.
- `ja`: 0 errores pero 1 aviso (298 textos en la portada contra 299 del alemán); hay que revisarlo.
- Solo faltaba la portada `index.html` (rutas y datos correctos): `id`, `cs`, `sk`, `he`, `ar`, `ko`, `zh`.
- `pl` y `tr`: las partes `_parte_<k>_NN.py` concatenadas en orden daban exactamente la estructura del alemán
  (1056 líneas, mismos marcadores). Se armaron `datos_pl.py` y `datos_tr.py` con `cat`; quedó solo la portada.
- `ro`: `datos_ro.py` cortado en 666 líneas (falta el bloque final `GUIAS += [...]` y `OTRAS_GUIAS += [...]` del
  alemán, líneas 671-1056). Hay una parte traducida en `_parte_ro_05.py`. La portada ya existe.
- `ms` (partes = 666 líneas), `hu` (988), `el` (913): falta completar el bloque final y la portada; `el` además no
  tenía rutas.
- `th`, `uk`, `hi`, `vi`: sin datos. `th` tenía rutas; `uk`, `hi`, `vi` no.
- Arreglado: `rutas/fi.json` tenía `firetv` y `firetv-lost` sin el prefijo `fi/oppaat/`, lo que había generado dos
  carpetas sueltas en la raíz (`fire-tv-kaukosaadin-*`), ya borradas.

Hecho: `fi` con 0 errores. En curso: agentes Sonnet en paralelo por idioma para las portadas que faltan y para
completar los datos de `ro`, `ms`, `hu`, `el`, `th`, `uk`, `hi`, `vi`.

**LOS 30 IDIOMAS CON 0 ERRORES (25-nov).** Los 24 nuevos pasaron `herramientas/revisar_idioma.py <k>` con
0 errores y están en `LISTOS` de `herramientas/idiomas_sitio.py`; `ACTIVOS` da 30. Comprobado además: el selector de
idioma del pie tiene los 30 idiomas en las 30 portadas, sin duplicados y con un solo `aria-current` por página; el
`<head>` lleva 31 `hreflang` (los 30 más `x-default`); `ar` y `he` llevan `dir="rtl"`.

**Dos fallos de los generadores encontrados y arreglados al juntar (importante para la próxima vez):**

1. `herramientas/portadas_idiomas.py` rompía el selector de idioma del pie. Ese bloque lo escribe entero
   `pie_firma.py` (con sangría de 12 espacios y `aria-current`), pero `portadas_idiomas.py` también lo tocaba con
   expresiones regulares de 8 y 10 espacios que no casaban con lo que escribe `pie_firma.py`. Resultado al pasar de
   6 a 30 idiomas: **34 entradas con cuatro idiomas repetidos en todas las páginas**, y una segunda pasada las
   dobló a 58. Arreglado: ahora `portadas_idiomas.py` solo trabaja en lo que hay antes de los marcadores
   `<!-- pie-firma -->` y deja ese bloque a `pie_firma.py`. Comprobado que dos pasadas seguidas dejan 30 sin
   duplicados (es idempotente).
2. `herramientas/revisar_idioma.py`, los dos arreglos ya descritos más abajo (el `/de/` del selector del pie y el
   aviso que no decía dónde estaba la diferencia).

**Orden correcto al juntar** (sirve para la próxima vez): primero sumar los idiomas a `LISTOS`, después
`pie_firma.py` y solo después `portadas_idiomas.py`. Si se corre `portadas_idiomas.py` con el pie escrito para menos
idiomas, el pie queda mal.

**Continuación programada (sí del fundador, 25-nov)**: tarea única `mandotv-web-30-idiomas-seguir` para el 27-nov a
las 18:10 de Chile (al renovarse el semanal). Sigue con la lista de abajo hasta dejar la comparación lado a lado; no
publica ni indexa. Corre solo si la app de Claude está abierta (si no, al abrirla).

**LISTO PARA QUE EL FUNDADOR LO MIRE (25-nov, tarde).** Comparación lado a lado en
`docs/comparacion-30-idiomas/index.html` (fuera de git; se abre con el servidor local en
`http://localhost:8090/docs/comparacion-30-idiomas/`): antes y propuesta en escritorio, celular y con los efectos de
Windows apagados, más árabe de derecha a izquierda, el selector con los 30 y las imágenes para compartir.
Hecho en esta tanda, con los 24 idiomas nuevos todavía en 0 errores:
- La pregunta "¿en qué idiomas está?" dice en las 30 portadas que la web está en los mismos 30 (texto y JSON-LD).
- 24 imágenes `social-<k>.png`. `generar_social.py` ahora ajusta solo el título a 2 líneas y el subtítulo a 1, no deja
  que el texto tape el sello, pone `dir="rtl"` en árabe y hebreo y no parte palabras en coreano ni japonés.
- `estilos.css`: vietnamita con fuente del sistema (Archivo e Inter no traen sus letras con doble tilde), árabe sin
  espaciado entre letras, coreano sin partir palabras, y el menú de idioma del pie en árabe y hebreo se abre hacia
  la derecha (anclado a la derecha se salía de la pantalla en el celular).
- `llms.txt` con los 30 idiomas.
- Revisado en navegador: `ar` y `he` de derecha a izquierda, 30 idiomas en el pie y en el botón de la barra (lista
  desplazable, actual marcado), 0 imágenes sin alt, sin desborde en 375 px, sin errores propios de consola.
**Falta**: el sí del fundador; después publicar (merge a main, push), IndexNow, sitemap en Search Console y Bing, e
indexación de las portadas nuevas (primero ko, nl, sv, da, no, fi, pl). **Videos**: regla nueva del fundador
(25-nov): un video por idioma en 16:9 y en 9:16; hoy la web solo tiene el video de la portada en inglés, así que
faltan los de los otros 29 idiomas (no se pudo contar los ya hechos desde este proyecto). La tarea programada del
27-nov ya no hace falta.

**Lista anterior (ya resuelta salvo la publicación):**

1. La pregunta frecuente "¿en qué idiomas está?" sigue diciendo que la WEB está en seis idiomas (cada agente le sumó
   el suyo, así que hay 30 versiones distintas de la frase). Hay que corregirla en las 30 portadas, en el texto
   visible y en el JSON-LD, para que diga 30.
2. Imágenes `social-<k>.png` de los 24 idiomas nuevos (`generar_social.py` y captura con Edge sin ventana).
3. `:lang(vi)` con fuente del sistema.
4. `llms.txt`.
5. Revisar en el navegador: escritorio, celular, efectos de Windows apagados, y `ar` y `he` de derecha a izquierda.
6. Comparación lado a lado para el fundador y su OK. Después: publicar, IndexNow, Search Console y Bing.

**Al día 25-nov (se actualiza a cada idioma terminado):**

- **0 errores en el revisor (20)**: `da`, `nl`, `nb`, `sv`, `zh-hant`, `ja`, `ko`, `id`, `he`, `ar`, `zh`, `cs`,
  `sk`, `fi`, `pl`, `tr`, `ro`, `hu`, `el`, `vi`. Todavía **no** sumados a `LISTOS`: se suman todos juntos al final, porque
  `pie_firma.py` (que corre en el pre-commit) reescribe el pie de todas las páginas y conviene no hacerlo mientras
  haya agentes trabajando.
- **`ms`: datos y portada terminados, 2 errores que se arreglan solos al juntar.** Los dos son textos en alemán
  dentro del bloque `<!-- pie-firma -->`, que no se edita a mano: lo escribe `pie_firma.py`. Ese script solo toca
  las páginas que existen cuando corre, y la portada en malayo se creó después de la última pasada. Se arregla al
  sumar `ms` a `LISTOS` y correr `pie_firma.py` en el paso de juntar. Comprobado: `textos_idiomas.json` ya tiene los
  textos cortos completos de los 24 idiomas (pie, Microsoft Store e imagen para compartir), así que no falta nada
  para que el pie salga en malayo. Lo mismo pasará con los idiomas que terminen después.
- **En curso (3 agentes)**: `th`, `uk`, `hi`. Los tres ya tienen `herramientas/rutas/<k>.json` y
  `herramientas/datos_<k>.py` con las 1056 líneas del alemán; les falta **solo la portada** `<k>/index.html`. Si hay
  que retomarlos, el trabajo que queda es ese archivo: se copia `de/index.html` traducido siguiendo el punto 3 de
  `docs/AGREGAR-IDIOMA.md` (son alfabetos no latinos, así que la referencia es `ja/index.html` y los slugs ya están
  en su `rutas/<k>.json`).
- **Nada por relanzar de los otros**: `el` y `vi` terminaron con 0 errores (rutas, datos y portada).

**Semanal al 99 % al escribir esto.** Por eso no se empezó ningún idioma nuevo. Si se corta antes de que `th`, `uk`
y `hi` terminen, lo único pendiente de ellos es la portada, como dice el punto de arriba.
- Si el plan semanal se corta: se termina el idioma que esté a medias y no se empieza otro. El semanal se renueva
  el 27-nov a las 18:00 de Chile.

**Dos arreglos al revisor en esta sesión (`herramientas/revisar_idioma.py`):**

1. Daba `ERROR portada: enlace al alemán /de/` en TODOS los idiomas, hasta en los que ya estaban en 0. Causa: el
   pre-commit corre `pie_firma.py`, que reescribe el selector de idioma del pie de cada página, y ahí el enlace a
   `/de/` es correcto (el pie lista los 30 idiomas, alemán incluido). El revisor marcaba cualquier `/de/` de la
   portada. Ahora salta los enlaces que llevan `hreflang` (el selector del pie y el bloque de alternates) y sigue
   marcando los demás. Con esto los 18 vuelven a 0 errores.
2. El aviso "N textos contra 299 del alemán" ahora dice en qué líneas está la diferencia, para poder revisarlo de
   un vistazo.

**Aviso "298 textos contra 299" (ja, ko, ar, tr, hu): comprobado, no falta nada.** En los cinco la diferencia está
en la misma línea 429 de la portada, la pregunta "¿con qué televisores funciona?": en alemán el párrafo empieza con
la palabra suelta "Mit" antes del primer enlace y en esos idiomas la frase empieza directamente por el enlace, así
que hay un nodo de texto menos. Verificado en el húngaro (alfabeto latino, legible): están los 4 enlaces de marca,
las 5 marcas de televisores antiguos (NetCast, SmartCast, Bravia, Viera, Philips), Apple TV y HDMI-CEC, igual que en
alemán. No es texto sin traducir.

Dos hallazgos de esta sesión:
- El aviso de `ja` (298 textos contra 299) es falso positivo: en alemán el párrafo de "con qué televisores funciona"
  empieza con la preposición "Mit" antes del primer enlace y en japonés empieza directo con el enlace. No falta nada.
  El revisor cuenta nodos de texto, así que este aviso puede repetirse en otros idiomas y no es error.
- **Pendiente real de contenido**: la pregunta frecuente "¿en qué idiomas está?" dice en cada portada en cuántos
  idiomas está la WEB (hoy "seis": español, inglés, portugués, francés, alemán e italiano; cada agente le sumó el
  suyo). Al publicar los 30 hay que corregirla en las 30 portadas, en el texto visible y en el JSON-LD, para que
  diga 30 idiomas. Se hace de una sola pasada cuando todos los idiomas pasen la revisión.

Aviso de presupuesto: el semanal iba al 96 % al retomar, así que se priorizó lo barato de más valor (las portadas)
y se guarda el estado a cada paso.

- Ojo: los generadores no conocen arreglos hechos a mano (Casa en la privacidad es/en/pt/it, `/#android` en las guías
  en inglés, la portada en inglés en la raíz). No regenerar páginas existentes: usar `portadas_idiomas.py`, que solo
  refresca los enlaces de idioma.

## 25-nov: envío a directorios (hecho con Claude in Chrome)

Resultado (detalle en la tabla de `docs/DIRECTORIOS.md`): **Uneed agendado** en la cola gratis para el 23-jun-2027
(uneed.best/tool/mando-tv); **Fazier omitido** (el plan gratis exige un enlace de vuelta; decisión del fundador);
**Peerlist** con perfil y proyecto Mando TV listos (perfil al 60 %), y el lanzamiento descartado por el fundador (exigía verificación de 19 USD); **Slant** caído (error
526), reintentar otro día; **SaaSHub**: la ficha original saashub.com/mando-tv ya estaba verificada y en cola (se le sumó Mac);
el envío del 25-nov creó un duplicado ("Mando TV - Control Universal") que el fundador pide borrar por correo. Claude in Chrome sí conectó en esta sesión.

Con el sí del fundador ("Sí, empieza" y "Te doy permiso"). Textos listos en `docs/DIRECTORIOS.md`. Desde el navegador
de la app el control de seguridad bloqueó llenar formularios, así que se sigue con **Claude in Chrome en el Chrome
normal** (`C:\Program Files\Google\Chrome\Application\chrome.exe`, nunca Canary); la extensión ya está conectada
pero la sesión anterior no la veía. Orden: Uneed, Fazier, Peerlist, Slant (SaaSHub lo envía el fundador: su página
pide que lo haga una persona). En cada sitio: el fundador crea la cuenta y escribe la contraseña; pedir su OK antes de
enviar cada ficha; usar la cola gratis, no pagar ni pedir votos. Anotar cada ficha publicada con fecha y URL.

## 25-nov: auditor auditarweb.co en 98/100

Único aviso: "No hay datos de autoridad de dominio" (se mide con enlaces de otras webs; no se arregla con código).
Enlaces conseguidos: AlternativeTo publicado (alternativeto.net/software/mando-tv/, visto el 25-nov). mandotv.net
redirige con 301 a mandotv.app. Siguiente: kit de directorios de `control/docs/ENLACES-SEO.md` (SaaSHub, Slant,
Uneed, Fazier, Peerlist; Product Hunt cuando Google Play esté en producción), cada sitio con el OK del fundador.

## 25-nov: Cloudflare delante de mandotv.app, ACTIVO (sí del fundador)

- Porkbun con `brynne.ns.cloudflare.com` y `owen.ns.cloudflare.com` (registro .app confirmado por RDAP). Sin DNSSEC.
- Al activarse, el certificado de Cloudflare tardó unos minutos ("Pending Validation") y por Google DNS y Quad9 la web
  no abría: se pausó Cloudflare (las visitas fueron directo a GitHub) hasta que el certificado estuvo listo y luego se
  reactivó. **Lección para la receta**: no cambiar servidores hasta que el certificado de Cloudflare esté activo, o
  pausar la zona apenas se active y reanudarla cuando el certificado esté listo.
- Comprobado por Cloudflare (`curl --resolve` a 104.21.75.146): `/`, `www` (301 a `/`), `/es/`, `/guias/`,
  `estilos.css` y `robots.txt` responden con HSTS 1 año, X-Frame-Options SAMEORIGIN, Referrer-Policy,
  Permissions-Policy y nosniff. `robots.txt` igual al del repositorio. Google DNS ya entrega las IP de Cloudflare.
- Correo: MX `fwd1`/`fwd2.porkbun.com` y SPF servidos por Cloudflare; no se probó un envío real.
- **Pendiente**: repetir el auditor (auditarweb.co) cuando el fundador quiera; vigilar en GitHub > Settings > Pages
  que el dominio siga verde (con Cloudflare delante GitHub puede marcar aviso de DNS, la web sigue funcionando).

## 24-nov (noche): avisos del auditor auditarweb.co (91/100), PUBLICADO (merge `824f6aa4`, sí del fundador)

- Hecho en la rama (commit `16efd5c7`): logo con `alt="Mando TV"` en barra, pie y barra fija (226 páginas, generadores
  y `app.js`), `<meta name="referrer" content="strict-origin-when-cross-origin">` en todas las páginas, y el selector
  de idioma del pie con alto máximo y desplazamiento (listo para 30 idiomas o más). Probado en local: 0 imágenes sin
  alt, 6 idiomas en el selector (la web está en 6), sin errores propios en consola.
- **Falta y no se puede en GitHub Pages**: `X-Frame-Options` y `Strict-Transport-Security` (HSTS) solo van como
  cabeceras HTTP y GitHub Pages no deja ponerlas. Solución propuesta: poner Cloudflare (plan gratis; el sitio ya usa
  Cloudflare Web Analytics) delante, cambiando los servidores DNS en Porkbun y copiando todos los registros (MX del
  correo hola@mandotv.app, TXT de verificación). Espera el sí del fundador.
- Comprobado en vivo: `/`, `/es/`, `/de/`, `/guias/`, `/control-remoto-lg/` con la meta referrer y sin alt vacío;
  portada con 0 imágenes sin alt (5 imágenes), selector con 6 idiomas y alto máximo 440px, sin errores de consola.
- IndexNow aceptó todo el sitemap (HTTP 200).
- **Pendiente**: reenviar el sitemap en Search Console y en Bing Webmaster Tools. El 24-nov ninguno de los dos
  navegadores tenía la sesión iniciada (el panel de la app pedía inicio de sesión y Claude in Chrome no estaba
  conectado). El cambio no se ve en la página, así que no es urgente.

## 24-nov: aviso de idioma y x-default en inglés (publicado)

Publicado con el sí del fundador (merge `442156f2` en `main`). Comprobado en vivo: con el navegador en inglés la
portada ofrece /en/, en español no sale nada y en alemán /en/ ofrece /de/, sin errores de consola. El x-default de
210 páginas apunta a la versión en inglés (las 6 marcas solo de Latinoamérica siguen en español).

Indexación:
- IndexNow: aceptó todo el sitemap (HTTP 200).
- Search Console: sitemap reenviado ("Se ha enviado el sitemap correctamente", leído el 24-nov).
- **Pendiente 25-nov**: Inspección de URL > Solicitar indexación de `https://mandotv.app/` y luego
  `https://mandotv.app/en/`. El 24-nov Google respondió "Se ha superado la cuota" (cupo diario ya usado).
- Bing Webmaster Tools: el fundador inició sesión y el sitemap se reenvió el 24-nov ("successfully submitted", 153
  URL, sin errores ni advertencias). Única notificación: consejo general "Improve the search presence", informativo.

## 24-nov (noche): "See it in action" con el video primero (publicado)

Con el sí del fundador. En la portada en inglés (`/`), la sección `#demo` lleva primero el video de 25 s (protagonista,
a todo el ancho) y debajo el subtítulo "The remote, step by step" con la demo animada y las dos capturas. Comprobado
en vivo en escritorio y celular con movimiento reducido: todo aparece, sin desborde ni errores. IndexNow aceptó `/`,
sitemap reenviado en Search Console y en Bing. Solo la portada en inglés tiene el video; las demás no cambian.

## 24-nov (tarde): portada en inglés PUBLICADA

Con el sí del fundador (merge `0d6d9bc6`). Comprobado en vivo: `/` en inglés (navegador en español ve "Esta página
también está en español" → `/es/`), `/es/` en español (navegador en inglés ve la oferta de `/`), `/en/#tiendas`
redirige a `/#tiendas`, 404 legible, sin errores. IndexNow aceptó portadas y sitemap (HTTP 200). Sitemap reenviado
en Search Console ("Se ha enviado el sitemap correctamente") y en Bing ("successfully submitted", 223 URL).
**Pendiente 25-nov**: Search Console > Inspección de URL > Solicitar indexación de `https://mandotv.app/` y luego
`https://mandotv.app/es/` (el 24-nov seguía "Se ha superado la cuota").

Microsoft Store: envío 14 con privacidad `/en/privacy.html` y soporte `/en/support.html` (sitio web
`https://mandotv.app` sin cambio) enviado a certificación el 24-nov; solo cambian las Propiedades. Aviso del Action
Center: "Your contact email address: not provided": el 24-nov se puso el Gmail del fundador (idioma Español) en
My Preferences y quedó "Verified" con el segundo código (el primero no se confirmó). Resuelto. La app (control) no tiene enlace propio a la política de privacidad; Ajustes solo abre `https://mandotv.app`.

## 24-nov: portada en inglés en la raíz (preparación; ya publicada, ver arriba)

Pedido del fundador tras ver Search Console (16 de 22 clics de países que no hablan español). En la rama:
- `/` = portada en inglés (antes `/en/`), `/es/` = portada en español (antes `/`), `/en/` = redirección al instante a
  `/` (noindex, canonical a `/`, conserva el #). Solo cambian las portadas; guías y marcas siguen igual.
- 90 páginas con enlaces ajustados según su idioma (logo, migas, #android, #tiendas, selectores de idioma),
  hreflang de las 6 portadas, generadores (`idiomas_sitio.py`, `pie_firma.py`, `generar_en.py`, `generar_marcas.py`,
  `generar_guias.py`), `llms.txt` y `manifest` (lang en). La página de mandos compartidos `m/` enlaza a `/`.
- Arreglo aparte: los botones de la 404 se veían blancos sobre blanco (en vivo hoy).
- Probado en local: 0 enlaces rotos en 223 páginas, aviso de idioma correcto en 10 casos, sin errores de consola.
- Al publicar: fusionar, `pie_firma.py` + `versionar.py`, push, comprobar en vivo, IndexNow, sitemap en Search Console
  y Bing, y pedir indexación de `/` y `/es/` (después de `/` y `/en/` pendientes de hoy).

## 24-nov: enlaces de las tiendas en inglés (pedido del fundador)

- App Store: privacidad `https://mandotv.app/en/privacy.html` y soporte `https://mandotv.app/en/support.html` en los
  36 idiomas de la versión 1.2.0 de iPhone (en revisión; salen en vivo cuando Apple la apruebe). La ficha publicada no
  se puede editar (409). La de Mac 1.2.0 ya está a la venta: su soporte cambia en la próxima versión de Mac (la
  privacidad es común a iPhone y Mac). Marketing sigue `https://mandotv.app` (será la portada en inglés).
  `control/tool/fichas_mac_apple.mjs` y `control/docs/ficha-tiendas.md` actualizados (commit e207329 en control).
- Google Play: política de privacidad cambiada a `/en/privacy.html` y enviada a revisión (24-nov, "Cambios en
  revisión"). Sitio web de la ficha: `https://mandotv.app` (sin cambio). Aviso de la consola sobre
  androidx.fragment 1.1.0: ya anotado en `control/docs/ESTADO.md` para la 1.2.1 de Android.
- Microsoft Store: hecho el 24-nov (ver arriba, envío 14 en certificación). Antes: Propiedades > URL de
  privacidad y sitio web/soporte a inglés, y enviar (pasa por certificación).

Idea pendiente (no hecha): el aviso de cookies sale en el idioma de la página, no en el del navegador; a quien recibe
el aviso de idioma le sale en español.

Cómo medir: evento `aviso_idioma` en Google Analytics (solo visitas que aceptan cookies) y, en Search Console,
clics de países no hispanohablantes en /en/ antes y después del 24-nov.
