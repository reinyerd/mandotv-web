# Cloudflare delante de mandotv.app

**Estado 25-nov**: zona creada en Cloudflare (plan Free, cuenta del fundador) con los 13 registros importados
(web con proxy, correo y TXT solo DNS), SSL Full, Always Use HTTPS, HSTS 12 meses + nosniff y la regla
"Cabeceras de seguridad" activa. Bot Preference Sync desactivado (no toca robots.txt) y bots de IA en "Allow"
(bueno para GEO). Servidores cambiados en Porkbun y zona **activa** desde el 25-nov (ver `docs/ESTADO.md`). Ojo: el certificado de
Cloudflare tarda unos minutos tras activarse; pausar la zona mientras tanto para no dejar la web sin HTTPS.

Objetivo: enviar las cabeceras de seguridad que GitHub Pages no permite (X-Frame-Options, HSTS y las demás).
La web sigue en GitHub Pages; Cloudflare (plan gratis, cuenta del fundador, la misma de Web Analytics) solo
pasa las visitas y les agrega las cabeceras.

## 1. Registros DNS que hay que copiar (leídos el 24-nov desde 1.1.1.1)

| Tipo | Nombre | Valor | Proxy |
| --- | --- | --- | --- |
| A | @ | 185.199.108.153, .109.153, .110.153, .111.153 | Sí (nube naranja) |
| AAAA | @ | 2606:50c0:8000::153, 8001::153, 8002::153, 8003::153 | Sí |
| CNAME | www | reinyerd.github.io | Sí |
| MX | @ | fwd1.porkbun.com (prioridad 10), fwd2.porkbun.com (20) | No aplica |
| TXT | @ | google-site-verification=uL5C-EKKLz51dNDfDhks7Y25UhfT3g-DpQNMgkMyUp8 | No aplica |
| TXT | @ | v=spf1 include:_spf.porkbun.com ~all | No aplica |
| TXT | @ | apple-domain-verification=czUGHRuFfO3XrnJD | No aplica |

Antes de cambiar servidores, comparar con la lista del panel de Porkbun por si hay alguno más (DKIM, _dmarc,
verificaciones). El reenvío de hola@mandotv.app de Porkbun funciona con otros servidores DNS si están los MX y el
SPF (kb.porkbun.com, artículo 47).

## 2. Ajustes en Cloudflare

- SSL/TLS: modo **Full** (no Strict, para que una renovación atrasada del certificado de GitHub no corte la web).
  Always Use HTTPS: activado.
- SSL/TLS > Edge Certificates > HSTS: max-age 12 meses, sin includeSubDomains ni preload al principio,
  No-Sniff activado (`X-Content-Type-Options: nosniff`).
- Rules > Transform Rules > Modify Response Header, para todo el sitio:
  - `X-Frame-Options: SAMEORIGIN` (la web no usa iframes; SAMEORIGIN por si algún día se usa uno propio)
  - `Referrer-Policy: strict-origin-when-cross-origin`
  - `Permissions-Policy: camera=(), microphone=(), geolocation=()` (la web no usa ninguno, revisado el 24-nov)

## 3. Cambio de servidores (solo con el sí del fundador)

En Porkbun > mandotv.app > Authoritative Nameservers, poner los 2 que muestre Cloudflare. Tarda de minutos a horas.
Mientras tanto la web sigue igual (unos visitantes llegan por Porkbun y otros por Cloudflare, ambos a GitHub).

## 4. Comprobar después

`curl -sI https://mandotv.app/` debe mostrar las cabeceras; probar `www`, una guía, el correo a hola@mandotv.app,
que GitHub Pages siga con el dominio verde y repetir el auditor. Para volver atrás basta poner otra vez los
servidores de Porkbun (la zona de Porkbun no se borra).
