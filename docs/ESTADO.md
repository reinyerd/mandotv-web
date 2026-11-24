# Estado de la web mandotv.app

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
