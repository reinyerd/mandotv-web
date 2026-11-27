// Precio de Mando TV Pro según el país de quien visita: el mismo que cobran App Store, Google Play y Microsoft Store.
// Tabla: precio de Google Play por país (igual en Microsoft; Apple usa el redondo más cercano hacia arriba), leída por API el 27-nov-2026; regla de precios calculados (terminación 40). Regenerar si cambian
// los precios (ver docs/ESTADO.md). País: Cloudflare (/cdn-cgi/trace); si no responde, la región del idioma del
// navegador; si no se sabe, no se muestra nada. Para probar en local: ?pais=MX
(() => {
  const P = {AE:['AED',36.4],AF:['USD',3.4],AG:['USD',3.4],AI:['USD',3.4],AL:['USD',4.4],AM:['USD',4.4],AO:['USD',3.4],AR:['ARS',6340],AT:['EUR',9.4],AU:['AUD',14.4],AZ:['AZN',8.4],BA:['USD',4.4],BB:['USD',4.4],BE:['EUR',9.4],BF:['EUR',3.4],BG:['EUR',3.4],BH:['USD',3.4],BJ:['EUR',4.4],BM:['USD',3.4],BN:['USD',3.4],BO:['BOB',46.4],BR:['BRL',24.4],BS:['USD',3.4],BT:['USD',3.4],BW:['USD',3.4],BY:['USD',4.4],BZ:['USD',3.4],CA:['CAD',12.4],CD:['USD',3.4],CG:['USD',4.4],CH:['CHF',9.4],CI:['XOF',3440],CL:['CLP',3940],CM:['XAF',3540],CN:['CNY',27.4],CO:['COP',14840],CR:['CRC',1740],CV:['USD',3.4],CY:['EUR',9.4],CZ:['CZK',98.4],DE:['EUR',9.4],DK:['DKK',78.4],DM:['USD',3.4],DO:['USD',3.4],DZ:['DZD',549.4],EC:['USD',3.4],EE:['EUR',9.4],EG:['EGP',249.4],ES:['EUR',9.4],FI:['EUR',9.4],FJ:['USD',3.4],FM:['USD',3.4],FR:['EUR',9.4],GA:['EUR',3.4],GB:['GBP',8.4],GD:['USD',3.4],GE:['GEL',13.4],GH:['GHS',69.4],GM:['USD',3.4],GR:['EUR',9.4],GT:['USD',3.4],GW:['EUR',3.4],GY:['USD',3.4],HK:['HKD',77.4],HN:['USD',3.4],HR:['EUR',9.4],HU:['HUF',1740],ID:['IDR',78940],IE:['EUR',9.4],IL:['ILS',32.4],IN:['INR',398.4],IQ:['IQD',5940],IS:['EUR',9.4],IT:['EUR',9.4],JM:['USD',3.4],JO:['JOD',2.4],JP:['JPY',1440],KE:['KES',799.4],KG:['USD',3.4],KH:['USD',3.4],KN:['USD',3.4],KR:['KRW',14940],KW:['USD',9.4],KY:['USD',3.4],KZ:['KZT',2440],LA:['USD',3.4],LB:['USD',3.4],LC:['USD',3.4],LK:['LKR',1240],LR:['USD',3.4],LT:['EUR',9.4],LU:['EUR',9.4],LV:['EUR',9.4],LY:['USD',3.4],MA:['MAD',59.4],MD:['USD',4.4],ME:['EUR',3.4],MG:['USD',3.4],MK:['USD',3.4],ML:['EUR',3.4],MM:['MMK',7940],MN:['MNT',14340],MO:['MOP',31.4],MR:['USD',3.4],MS:['USD',3.4],MT:['EUR',9.4],MU:['USD',4.4],MV:['USD',3.4],MW:['USD',3.4],MX:['MXN',88.4],MY:['MYR',19.4],MZ:['USD',3.4],NA:['USD',3.4],NE:['EUR',3.4],NG:['NGN',6840],NI:['USD',3.4],NL:['EUR',9.4],NO:['NOK',118.4],NP:['USD',4.4],NR:['USD',3.4],NZ:['NZD',16.4],OM:['USD',3.4],PA:['USD',3.4],PE:['PEN',17.4],PG:['USD',3.4],PH:['PHP',248.4],PK:['PKR',1040],PL:['PLN',19.4],PT:['EUR',9.4],PW:['USD',3.4],PY:['PYG',29940],QA:['QAR',36.4],RO:['RON',19.4],RS:['RSD',468.4],RU:['RUB',348.4],RW:['USD',4.4],SA:['SAR',39.4],SB:['USD',3.4],SC:['USD',3.4],SE:['SEK',118.4],SG:['SGD',13.4],SI:['EUR',9.4],SK:['EUR',9.4],SL:['USD',3.4],SN:['XOF',3440],SR:['USD',3.4],ST:['USD',3.4],SV:['USD',3.4],SZ:['USD',3.4],TC:['USD',3.4],TD:['USD',3.4],TH:['THB',148.4],TJ:['USD',3.4],TM:['USD',3.4],TN:['USD',3.4],TO:['USD',3.4],TR:['TRY',249.4],TT:['USD',3.4],TW:['TWD',319.4],TZ:['TZS',11840],UA:['UAH',269.4],UG:['USD',4.4],US:['USD',9.4],UY:['USD',3.4],UZ:['UZS',53540],VC:['USD',3.4],VE:['USD',3.4],VG:['USD',3.4],VN:['VND',118940],VU:['USD',3.4],XK:['EUR',3.4],YE:['USD',3.4],ZA:['ZAR',79.4],ZM:['USD',4.4],ZW:['USD',4.4]};
  const PAIS_RE = /^[A-Z]{2}$/;

  const desdeIdioma = () => {
    for (const l of navigator.languages || [navigator.language]) {
      const m = /-([A-Za-z]{2})$/.exec(l || '');
      if (m && P[m[1].toUpperCase()]) return m[1].toUpperCase();
    }
    return null;
  };

  const pais = async () => {
    const q = (new URLSearchParams(location.search).get('pais') || '').toUpperCase();
    if (PAIS_RE.test(q) && P[q]) return q;
    try {
      const c = new AbortController();
      const t = setTimeout(() => c.abort(), 1500);
      const r = await fetch('/cdn-cgi/trace', { signal: c.signal, cache: 'no-store' });
      clearTimeout(t);
      if (r.ok) {
        const m = /^loc=([A-Z]{2})$/m.exec(await r.text());
        if (m && P[m[1]]) return m[1];
      }
    } catch (e) { /* sin Cloudflare (local) o sin red: se usa el idioma */ }
    return desdeIdioma();
  };

  const formato = (pais, moneda, monto) => {
    const entero = Number.isInteger(monto);
    try {
      const idioma = (document.documentElement.lang || navigator.language || 'en').split('-')[0];
      return new Intl.NumberFormat(idioma + '-' + pais, {
        style: 'currency', currency: moneda,
        minimumFractionDigits: entero ? 0 : 2, maximumFractionDigits: entero ? 0 : 2,
      }).format(monto);
    } catch (e) {
      return monto + ' ' + moneda;
    }
  };

  const crear = (etiqueta, clase, html) => {
    const el = document.createElement(etiqueta);
    el.className = clase;
    el.innerHTML = html;
    return el;
  };

  const aparecer = (el) => {
    if (el.animate) el.animate([{ opacity: 0, transform: 'translateY(4px)' }, { opacity: 1, transform: 'none' }],
      { duration: 380, easing: 'cubic-bezier(.2,.7,.2,1)' });
  };

  const mostrar = (precio) => {
    const b = '<b>' + precio + '</b>';
    const nuevos = [];
    const hero = document.querySelector('.precio');
    if (hero) nuevos.push(hero.appendChild(crear('span', 'pro-precio', 'Pro ' + b)));
    for (const plan of document.querySelectorAll('.plan')) {
      const h3 = plan.querySelector('h3');
      if (h3 && /\bPro\b/.test(h3.textContent)) nuevos.push(h3.insertAdjacentElement('afterend', crear('p', 'plan-monto', precio)));
    }
    if (!hero) {
      const tiendas = document.querySelector('ul.tiendas');
      if (tiendas) {
        const sig = tiendas.nextElementSibling;
        const ancla = sig && sig.matches('p.nota') && /\bPro\b/.test(sig.textContent) ? sig : tiendas;
        nuevos.push(ancla.insertAdjacentElement('afterend', crear('p', 'pro-linea', 'Pro: ' + b)));
      }
    }
    nuevos.forEach(aparecer);
  };

  pais().then((p) => {
    if (!p || !P[p]) return;
    const [moneda, monto] = P[p];
    mostrar(formato(p, moneda, monto));
  });
})();
