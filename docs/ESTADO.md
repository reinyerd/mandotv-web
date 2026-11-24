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

Idea pendiente (no hecha): el aviso de cookies sale en el idioma de la página, no en el del navegador; a quien recibe
el aviso de idioma le sale en español.

Cómo medir: evento `aviso_idioma` en Google Analytics (solo visitas que aceptan cookies) y, en Search Console,
clics de países no hispanohablantes en /en/ antes y después del 24-nov.
