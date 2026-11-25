// Precio de Mando TV Pro según el país de quien visita: el mismo que cobran App Store, Google Play y Microsoft Store.
// Tabla: precio de App Store por país (referencia de las 3 tiendas), leída por API el 25-nov-2026. Regenerar si cambian
// los precios (ver docs/ESTADO.md). País: Cloudflare (/cdn-cgi/trace); si no responde, la región del idioma del
// navegador; si no se sabe, no se muestra nada. Para probar en local: ?pais=MX
(() => {
  const P = {AE:['AED',36.99],AF:['USD',3.99],AG:['USD',3.99],AI:['USD',3.99],AL:['USD',4.99],AM:['USD',4.99],AO:['USD',3.99],AR:['USD',3.99],AT:['EUR',9.99],AU:['AUD',14.99],AZ:['USD',4.99],BA:['EUR',3.99],BB:['USD',4.99],BE:['EUR',9.99],BF:['USD',3.99],BG:['EUR',3.99],BH:['USD',3.99],BJ:['USD',4.99],BM:['USD',3.99],BN:['USD',3.99],BO:['USD',3.99],BR:['BRL',24.9],BS:['USD',3.99],BT:['USD',3.99],BW:['USD',3.99],BY:['USD',4.99],BZ:['USD',3.99],CA:['CAD',12.99],CD:['USD',3.99],CG:['USD',4.99],CH:['CHF',9.9],CI:['USD',4.99],CL:['CLP',3990],CM:['USD',4.99],CN:['CNY',28],CO:['COP',14900],CR:['USD',3.99],CV:['USD',3.99],CY:['EUR',9.99],CZ:['CZK',99],DE:['EUR',9.99],DK:['DKK',79],DM:['USD',3.99],DO:['USD',3.99],DZ:['USD',3.99],EC:['USD',3.99],EE:['EUR',9.99],EG:['EGP',249.99],ES:['EUR',9.99],FI:['EUR',9.99],FJ:['USD',3.99],FM:['USD',3.99],FR:['EUR',9.99],GA:['USD',3.99],GB:['GBP',8.99],GD:['USD',3.99],GE:['USD',4.99],GH:['USD',4.99],GM:['USD',3.99],GR:['EUR',9.99],GT:['USD',3.99],GW:['USD',3.99],GY:['USD',3.99],HK:['HKD',78],HN:['USD',3.99],HR:['EUR',9.99],HU:['HUF',1790],ID:['IDR',79000],IE:['EUR',9.99],IL:['ILS',32.9],IN:['INR',399],IQ:['USD',3.99],IS:['USD',11.99],IT:['EUR',9.99],JM:['USD',3.99],JO:['USD',3.99],JP:['JPY',1500],KE:['USD',4.99],KG:['USD',3.99],KH:['USD',3.99],KN:['USD',3.99],KR:['KRW',15000],KW:['USD',9.99],KY:['USD',3.99],KZ:['KZT',2490],LA:['USD',3.99],LB:['USD',3.99],LC:['USD',3.99],LK:['USD',3.99],LR:['USD',3.99],LT:['EUR',9.99],LU:['EUR',9.99],LV:['EUR',9.99],LY:['USD',3.99],MA:['USD',4.99],MD:['USD',4.99],ME:['EUR',3.99],MG:['USD',3.99],MK:['USD',3.99],ML:['USD',3.99],MM:['USD',3.99],MN:['USD',3.99],MO:['USD',3.99],MR:['USD',3.99],MS:['USD',3.99],MT:['EUR',9.99],MU:['USD',4.99],MV:['USD',3.99],MW:['USD',3.99],MX:['MXN',89],MY:['MYR',19.9],MZ:['USD',3.99],NA:['USD',3.99],NE:['USD',3.99],NG:['NGN',6900],NI:['USD',3.99],NL:['EUR',9.99],NO:['NOK',119],NP:['USD',4.99],NR:['USD',3.99],NZ:['NZD',16.99],OM:['USD',3.99],PA:['USD',3.99],PE:['PEN',17.9],PG:['USD',3.99],PH:['PHP',249],PK:['PKR',1100],PL:['PLN',19.99],PT:['EUR',9.99],PW:['USD',3.99],PY:['USD',3.99],QA:['QAR',36.99],RO:['RON',19.99],RS:['EUR',3.99],RU:['RUB',349],RW:['USD',4.99],SA:['SAR',39.99],SB:['USD',3.99],SC:['USD',3.99],SE:['SEK',119],SG:['SGD',13.98],SI:['EUR',9.99],SK:['EUR',9.99],SL:['USD',3.99],SN:['USD',4.99],SR:['USD',3.99],ST:['USD',3.99],SV:['USD',3.99],SZ:['USD',3.99],TC:['USD',3.99],TD:['USD',3.99],TH:['THB',149],TJ:['USD',3.99],TM:['USD',3.99],TN:['USD',3.99],TO:['USD',3.99],TR:['TRY',249.99],TT:['USD',3.99],TW:['TWD',320],TZ:['TZS',11900],UA:['USD',4.99],UG:['USD',4.99],US:['USD',9.99],UY:['USD',3.99],UZ:['USD',3.99],VC:['USD',3.99],VE:['USD',3.99],VG:['USD',3.99],VN:['VND',119000],VU:['USD',3.99],XK:['EUR',3.99],YE:['USD',3.99],ZA:['ZAR',79.99],ZM:['USD',4.99],ZW:['USD',4.99]};
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
