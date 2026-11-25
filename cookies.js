// Pila fija de abajo (24-nov): el aviso de idioma y el de cookies van uno sobre otro y nunca se tapan entre sí.
function pilaAvisos() {
  var pila = document.querySelector('.avisos');
  if (!pila) {
    pila = document.createElement('div');
    pila.className = 'avisos';
    document.body.appendChild(pila);
  }
  return pila;
}
// Entrada de un aviso con animación propia (con "reducir movimiento" de Windows las de CSS no corren).
function entraAviso(el) {
  if (el && el.animate) {
    el.animate([{ opacity: 0, transform: 'translateY(14px) scale(.97)' }, { opacity: 1, transform: 'none' }],
      { duration: 380, easing: 'cubic-bezier(.2, .8, .2, 1)' });
  }
}
// Al cerrar el de idioma aparece el siguiente de la pila (el de cookies, si sigue pendiente).
function siguienteAviso() {
  var pila = document.querySelector('.avisos');
  var sig = pila && pila.querySelector(':scope > :not([hidden])');
  if (sig) entraAviso(sig);
}

// Aviso de cookies de Mando TV.
// Google Analytics (cookies) SOLO se carga si la persona pulsa "Aceptar". Sin respuesta o con "Rechazar"
// no se descarga nada de Google. La elección se guarda en este navegador y se puede cambiar con el
// botón "Cookies" del pie de página.
(function () {
  var ID_GA = 'G-2TDRY67ZJC';
  var CLAVE = 'mandotv-cookies'; // 'si' | 'no'
  var cargado = false;
  var aviso;
  // Textos del aviso por idioma (<html lang>): es por defecto; en, de, fr, pt e it con tabla propia.
  var TEXTOS = {
    es: { aria: 'Aviso de cookies', titulo: '¿Nos dejas contar tus visitas con cookies?',
          texto: 'Usamos Google Analytics para saber qué páginas se leen y mejorar la web. Solo se activa si aceptas.',
          url: '/es/privacidad.html#cookies', mas: 'Más sobre las cookies', si: 'Aceptar', no: 'Rechazar' },
    en: { aria: 'Cookie notice', titulo: 'Can we count your visits with cookies?',
          texto: 'We use Google Analytics to see which pages are read and improve the site. It only turns on if you accept.',
          url: '/privacy.html#cookies', mas: 'More about cookies', si: 'Accept', no: 'Decline' },
    de: { aria: 'Cookie-Hinweis', titulo: 'Dürfen wir deine Besuche mit Cookies zählen?',
          texto: 'Wir nutzen Google Analytics, um zu sehen, welche Seiten gelesen werden, und die Website zu verbessern. Es wird nur aktiviert, wenn du akzeptierst.',
          url: '/de/datenschutz.html#cookies', mas: 'Mehr über Cookies', si: 'Akzeptieren', no: 'Ablehnen' },
    fr: { aria: 'Avis sur les cookies', titulo: 'Pouvons-nous compter vos visites avec des cookies ?',
          texto: "Nous utilisons Google Analytics pour savoir quelles pages sont lues et améliorer le site. Il ne s'active que si vous acceptez.",
          url: '/fr/confidentialite.html#cookies', mas: 'En savoir plus sur les cookies', si: 'Accepter', no: 'Refuser' },
    pt: { aria: 'Aviso de cookies', titulo: 'Você deixa a gente contar as suas visitas com cookies?',
          texto: 'Usamos o Google Analytics para saber quais páginas são lidas e melhorar o site. Ele só é ativado se você aceitar.',
          url: '/pt/privacidade.html#cookies', mas: 'Saiba mais sobre cookies', si: 'Aceitar', no: 'Recusar' },
    it: { aria: 'Avviso sui cookie', titulo: 'Possiamo contare le tue visite con i cookie?',
          texto: "Usiamo Google Analytics per sapere quali pagine vengono lette e migliorare il sito. Si attiva solo se accetti.",
          url: '/it/privacy.html#cookies', mas: 'Maggiori informazioni sui cookie', si: 'Accetta', no: 'Rifiuta' },
    id: { aria: 'Pemberitahuan cookie', titulo: 'Boleh kami hitung kunjunganmu dengan cookie?',
          texto: 'Kami memakai Google Analytics untuk melihat halaman mana yang dibaca dan memperbaiki situs. Fitur ini hanya aktif jika kamu setuju.',
          url: '/id/privacy.html#cookies', mas: 'Selengkapnya tentang cookie', si: 'Setuju', no: 'Tolak' },
    ms: { aria: 'Notis kuki', titulo: 'Bolehkah kami kira lawatan anda dengan kuki?',
          texto: 'Kami menggunakan Google Analytics untuk melihat halaman yang dibaca dan memperbaik laman web. Ia hanya diaktifkan jika anda bersetuju.',
          url: '/ms/privacy.html#cookies', mas: 'Lebih lanjut tentang kuki', si: 'Terima', no: 'Tolak' },
    cs: { aria: 'Oznámení o cookies', titulo: 'Můžeme počítat vaše návštěvy pomocí cookies?',
          texto: 'Používáme Google Analytics, abychom zjistili, které stránky se čtou, a mohli web zlepšovat. Zapne se, jen když souhlasíte.',
          url: '/cs/privacy.html#cookies', mas: 'Více o cookies', si: 'Přijmout', no: 'Odmítnout' },
    da: { aria: 'Cookie-besked', titulo: 'Må vi tælle dine besøg med cookies?',
          texto: 'Vi bruger Google Analytics til at se, hvilke sider der bliver læst, og til at forbedre siden. Det slås kun til, hvis du accepterer.',
          url: '/da/privacy.html#cookies', mas: 'Mere om cookies', si: 'Accepter', no: 'Afvis' },
    hu: { aria: 'Süti-tájékoztató', titulo: 'Megszámolhatjuk a látogatásaidat sütikkel?',
          texto: 'A Google Analytics segítségével látjuk, mely oldalakat olvassák, és így fejlesztjük a webhelyet. Csak akkor kapcsol be, ha elfogadod.',
          url: '/hu/privacy.html#cookies', mas: 'Továbbiak a sütikről', si: 'Elfogadom', no: 'Elutasítom' },
    nl: { aria: 'Cookiemelding', titulo: 'Mogen we je bezoeken tellen met cookies?',
          texto: "We gebruiken Google Analytics om te zien welke pagina's gelezen worden en de site te verbeteren. Het gaat alleen aan als je accepteert.",
          url: '/nl/privacy.html#cookies', mas: 'Meer over cookies', si: 'Accepteren', no: 'Weigeren' },
    nb: { aria: 'Varsel om informasjonskapsler', titulo: 'Kan vi telle besøkene dine med informasjonskapsler?',
          texto: 'Vi bruker Google Analytics for å se hvilke sider som blir lest, og for å forbedre nettstedet. Det slås bare på hvis du godtar.',
          url: '/no/privacy.html#cookies', mas: 'Mer om informasjonskapsler', si: 'Godta', no: 'Avslå' },
    pl: { aria: 'Informacja o plikach cookie', titulo: 'Czy możemy liczyć Twoje odwiedziny za pomocą plików cookie?',
          texto: 'Używamy Google Analytics, aby sprawdzać, które strony są czytane, i ulepszać witrynę. Włącza się tylko wtedy, gdy się zgodzisz.',
          url: '/pl/privacy.html#cookies', mas: 'Więcej o plikach cookie', si: 'Akceptuję', no: 'Odrzuć' },
    ro: { aria: 'Notificare cookie-uri', titulo: 'Putem număra vizitele tale cu ajutorul cookie-urilor?',
          texto: 'Folosim Google Analytics pentru a vedea ce pagini sunt citite și pentru a îmbunătăți site-ul. Se activează doar dacă accepți.',
          url: '/ro/privacy.html#cookies', mas: 'Mai multe despre cookie-uri', si: 'Accept', no: 'Refuz' },
    sk: { aria: 'Oznámenie o cookies', titulo: 'Môžeme počítať tvoje návštevy pomocou cookies?',
          texto: 'Používame Google Analytics, aby sme videli, ktoré stránky sa čítajú, a mohli web zlepšovať. Zapne sa, len ak súhlasíš.',
          url: '/sk/privacy.html#cookies', mas: 'Viac o cookies', si: 'Prijať', no: 'Odmietnuť' },
    fi: { aria: 'Evästeilmoitus', titulo: 'Saammeko laskea käyntisi evästeillä?',
          texto: 'Käytämme Google Analyticsia nähdäksemme, mitä sivuja luetaan, ja parantaaksemme sivustoa. Se otetaan käyttöön vain, jos hyväksyt.',
          url: '/fi/privacy.html#cookies', mas: 'Lisää evästeistä', si: 'Hyväksy', no: 'Hylkää' },
    sv: { aria: 'Cookiemeddelande', titulo: 'Får vi räkna dina besök med cookies?',
          texto: 'Vi använder Google Analytics för att se vilka sidor som läses och för att förbättra webbplatsen. Det aktiveras bara om du godkänner.',
          url: '/sv/privacy.html#cookies', mas: 'Mer om cookies', si: 'Godkänn', no: 'Avvisa' },
    vi: { aria: 'Thông báo về cookie', titulo: 'Chúng tôi có thể đếm lượt truy cập của bạn bằng cookie không?',
          texto: 'Chúng tôi dùng Google Analytics để biết những trang nào được đọc và cải thiện trang web. Công cụ này chỉ bật khi bạn chấp nhận.',
          url: '/vi/privacy.html#cookies', mas: 'Tìm hiểu thêm về cookie', si: 'Chấp nhận', no: 'Từ chối' },
    tr: { aria: 'Çerez bildirimi', titulo: 'Ziyaretlerini çerezlerle sayabilir miyiz?',
          texto: 'Hangi sayfaların okunduğunu görmek ve siteyi geliştirmek için Google Analytics kullanıyoruz. Yalnızca kabul edersen açılır.',
          url: '/tr/privacy.html#cookies', mas: 'Çerezler hakkında daha fazla bilgi', si: 'Kabul et', no: 'Reddet' },
    el: { aria: 'Ειδοποίηση για cookies', titulo: 'Μπορούμε να μετράμε τις επισκέψεις σου με cookies;',
          texto: 'Χρησιμοποιούμε το Google Analytics για να βλέπουμε ποιες σελίδες διαβάζονται και να βελτιώνουμε τον ιστότοπο. Ενεργοποιείται μόνο αν αποδεχτείς.',
          url: '/el/privacy.html#cookies', mas: 'Περισσότερα για τα cookies', si: 'Αποδοχή', no: 'Απόρριψη' },
    uk: { aria: 'Повідомлення про cookie', titulo: 'Чи можемо ми рахувати ваші відвідування за допомогою файлів cookie?',
          texto: 'Ми використовуємо Google Analytics, щоб бачити, які сторінки читають, і покращувати сайт. Він вмикається, лише якщо ви погодитеся.',
          url: '/uk/privacy.html#cookies', mas: 'Докладніше про файли cookie', si: 'Прийняти', no: 'Відхилити' },
    he: { aria: 'הודעה על עוגיות', titulo: 'אפשר לספור את הביקורים באתר באמצעות עוגיות?',
          texto: 'אנחנו משתמשים ב-Google Analytics כדי לראות אילו עמודים נקראים ולשפר את האתר. הוא מופעל רק לאחר אישור שלך.',
          url: '/he/privacy.html#cookies', mas: 'עוד על עוגיות', si: 'אישור', no: 'דחייה' },
    ar: { aria: 'إشعار ملفات تعريف الارتباط', titulo: 'هل تسمح لنا بإحصاء زياراتك باستخدام ملفات تعريف الارتباط؟',
          texto: 'نستخدم Google Analytics لمعرفة الصفحات التي تُقرأ وتحسين الموقع. لا يُفعَّل إلا إذا وافقت.',
          url: '/ar/privacy.html#cookies', mas: 'المزيد عن ملفات تعريف الارتباط', si: 'موافق', no: 'رفض' },
    hi: { aria: 'कुकी सूचना', titulo: 'क्या हम कुकी से आपकी विज़िट गिन सकते हैं?',
          texto: 'हम Google Analytics का इस्तेमाल यह देखने के लिए करते हैं कि कौन-से पेज पढ़े जाते हैं, ताकि साइट बेहतर बना सकें। यह तभी चालू होता है जब आप स्वीकार करते हैं।',
          url: '/hi/privacy.html#cookies', mas: 'कुकी के बारे में और जानें', si: 'स्वीकार करें', no: 'अस्वीकार करें' },
    th: { aria: 'ประกาศเกี่ยวกับคุกกี้', titulo: 'ให้เรานับจำนวนการเข้าชมของคุณด้วยคุกกี้ได้ไหม',
          texto: 'เราใช้ Google Analytics เพื่อดูว่าหน้าไหนมีคนอ่าน และนำไปปรับปรุงเว็บไซต์ โดยจะเปิดใช้งานก็ต่อเมื่อคุณยอมรับเท่านั้น',
          url: '/th/privacy.html#cookies', mas: 'ดูข้อมูลเพิ่มเติมเกี่ยวกับคุกกี้', si: 'ยอมรับ', no: 'ปฏิเสธ' },
    ko: { aria: '쿠키 안내', titulo: '쿠키로 방문 수를 집계해도 될까요?',
          texto: '어떤 페이지를 읽는지 확인하고 사이트를 개선하기 위해 Google Analytics를 사용해요. 동의하신 경우에만 켜져요.',
          url: '/ko/privacy.html#cookies', mas: '쿠키에 대해 더 알아보기', si: '동의', no: '거부' },
    ja: { aria: 'Cookieについてのお知らせ', titulo: 'Cookieで訪問数を集計してもよろしいですか？',
          texto: 'どのページが読まれているかを知り、サイトを改善するためにGoogle Analyticsを使っています。同意いただいた場合にのみ有効になります。',
          url: '/ja/privacy.html#cookies', mas: 'Cookieについて詳しく見る', si: '同意する', no: '拒否する' },
    'zh-hans': { aria: 'Cookie 提示', titulo: '可以用 Cookie 统计你的访问量吗？',
          texto: '我们使用 Google Analytics 了解哪些页面被阅读，以便改进网站。只有在你接受后才会启用。',
          url: '/zh/privacy.html#cookies', mas: '进一步了解 Cookie', si: '接受', no: '拒绝' },
    'zh-hant': { aria: 'Cookie 提示', titulo: '可以使用 Cookie 統計你的造訪次數嗎？',
          texto: '我們使用 Google Analytics 了解哪些頁面被閱讀，以便改進網站。只有在你接受後才會啟用。',
          url: '/zh-hant/privacy.html#cookies', mas: '進一步了解 Cookie', si: '接受', no: '拒絕' }
  };
  var L = (document.documentElement.lang || '').toLowerCase();  // zh-hans y zh-hant tienen tabla propia; pt-br usa pt
  var T = TEXTOS[L] || TEXTOS[L.slice(0, 2)] || TEXTOS.es;

  function leer() { try { return localStorage.getItem(CLAVE); } catch (e) { return null; } }
  function guardar(v) { try { localStorage.setItem(CLAVE, v); } catch (e) { /* sin almacenamiento: se vuelve a preguntar */ } }

  function cargarAnaliticas() {
    if (cargado) return;
    cargado = true;
    window.dataLayer = window.dataLayer || [];
    window.gtag = function () { window.dataLayer.push(arguments); };
    window.gtag('js', new Date());
    window.gtag('config', ID_GA, { allow_google_signals: false, allow_ad_personalization_signals: false });
    var s = document.createElement('script');
    s.async = true;
    s.src = 'https://www.googletagmanager.com/gtag/js?id=' + ID_GA;
    document.head.appendChild(s);
  }

  // Al retirar el permiso: desactiva la medición y borra las cookies de Google Analytics.
  function borrarCookiesGa() {
    window['ga-disable-' + ID_GA] = true;
    document.cookie.split(';').forEach(function (c) {
      var nombre = c.split('=')[0].trim();
      if (/^_ga/.test(nombre)) {
        ['', '; domain=.mandotv.app', '; domain=mandotv.app'].forEach(function (d) {
          document.cookie = nombre + '=; Max-Age=0; path=/' + d;
        });
      }
    });
  }

  function crearAviso() {
    aviso = document.createElement('div');
    aviso.className = 'aviso-cookies';
    aviso.setAttribute('role', 'region');
    aviso.setAttribute('aria-label', T.aria);
    aviso.innerHTML =
      '<p><b>' + T.titulo + '</b> <span class="aviso-cookies-texto">' + T.texto + '</span> <a href="' + T.url + '">' + T.mas + '</a></p>' +
      '<div class="aviso-cookies-botones">' +
      '<button type="button" class="boton" data-eleccion="si">' + T.si + '</button>' +
      '<button type="button" class="boton" data-eleccion="no">' + T.no + '</button>' +
      '</div>';
    aviso.addEventListener('click', function (e) {
      var b = e.target.closest('[data-eleccion]');
      if (!b) return;
      var v = b.getAttribute('data-eleccion');
      guardar(v);
      if (v === 'si') { window['ga-disable-' + ID_GA] = false; cargarAnaliticas(); } else { borrarCookiesGa(); }
      var teniaFoco = aviso.contains(document.activeElement);
      aviso.hidden = true;
      // Al ocultar el botón con foco, el foco caería al inicio de la página: vuelve a quien abrió el aviso.
      if (teniaFoco && disparador && disparador.isConnected) disparador.focus({ preventScroll: true });
      disparador = null;
    });
    pilaAvisos().appendChild(aviso);
  }

  var disparador = null;

  function mostrarAviso() {
    if (!aviso) crearAviso();
    disparador = document.activeElement !== document.body ? document.activeElement : null;
    aviso.hidden = false;
    // Los avisos salen uno a la vez: si lo pide el botón "Cookies" del pie, pasa delante del de idioma.
    var pila = aviso.parentNode;
    if (pila && pila.firstChild !== aviso) { pila.insertBefore(aviso, pila.firstChild); entraAviso(aviso); }
    var primero = aviso.querySelector('button');
    if (primero) primero.focus({ preventScroll: true });
  }

  document.addEventListener('click', function (e) {
    if (e.target.closest && e.target.closest('[data-cookies]')) { e.preventDefault(); mostrarAviso(); }
  });

  var eleccion = leer();
  if (eleccion === 'si') cargarAnaliticas();
  else if (eleccion !== 'no') {
    // Aparece cuando ya cargaron las fuentes: así no cambia de alto al llegar la letra y no mueve nada (CLS).
    var crearConFuentes = function () {
      var listas = document.fonts && document.fonts.ready;
      if (listas) listas.then(crearAviso, crearAviso); else crearAviso();
    };
    if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', crearConFuentes);
    else crearConFuentes();
  }
})();

// Idioma recordado (25-nov). La elección de idioma se guarda en este navegador ('mandotv-idioma', con el código del
// hreflang): al tocar un idioma del pie, de la barra o de "esta guía en otros idiomas", al tocar "Ver en..." del
// aviso, o al cerrar el aviso (quedarse en el de la página). La próxima vez que la persona entra desde fuera del sitio,
// el script corto del <head> (lo pone herramientas/idioma_guardado.py) la lleva a la gemela en su idioma antes de
// pintar. Nunca se adivina por el idioma del navegador: solo se recuerda lo que la persona eligió, y los robots (que
// no guardan nada) ven cada versión tal cual, como pide Google.
var IDIOMA_GUARDADO = 'mandotv-idioma';
function codigoIdioma(x) {
  // Etiqueta del navegador o de la página (es-CL, pt-BR, zh-TW, nb-NO...) al código de hreflang del sitio.
  x = String(x || '').toLowerCase().replace('_', '-');
  if (/^zh-(tw|hk|mo|hant)/.test(x)) return 'zh-hant';
  if (/^zh/.test(x)) return 'zh-hans';
  if (/^(no|nn|nb)(-|$)/.test(x)) return 'nb';
  if (/^iw(-|$)/.test(x)) return 'he';
  if (/^in(-|$)/.test(x)) return 'id';
  return x.split('-')[0];
}
function guardarIdioma(c) {
  try {
    localStorage.setItem(IDIOMA_GUARDADO, codigoIdioma(c));
    localStorage.removeItem('mandotv-aviso-idioma');  // marca vieja (solo decía "ya lo vio"), ya no se usa
  } catch (e) { /* sin almacenamiento: no se recuerda, el aviso vuelve a ofrecer */ }
}
document.addEventListener('click', function (e) {
  var a = e.target.closest && e.target.closest('a[hreflang]');
  if (a && a.host === location.host && a.getAttribute('hreflang') !== 'x-default') guardarIdioma(a.getAttribute('hreflang'));
});

// Aviso de idioma (24-nov): a quien llega desde fuera del sitio con el navegador en otro idioma que esta página tiene
// (sus <link rel="alternate" hreflang>), se le ofrece esa versión con un aviso que se cierra. No redirige solo:
// Google desaconseja redirigir por idioma y su robot tiene que ver cada versión tal cual. Sale hasta que la persona
// elige (ver "Idioma recordado" arriba); después ya no se le pregunta.
(function () {
  // Cada texto va en el idioma que se ofrece, el que esa persona entiende.
  var TEXTOS = {
    es: { aria: 'Idioma', texto: 'Esta página también está en español.', ir: 'Ver en español', cerrar: 'Cerrar' },
    en: { aria: 'Language', texto: 'This page is also available in English.', ir: 'View in English', cerrar: 'Close' },
    de: { aria: 'Sprache', texto: 'Diese Seite gibt es auch auf Deutsch.', ir: 'Auf Deutsch ansehen', cerrar: 'Schließen' },
    fr: { aria: 'Langue', texto: 'Cette page existe aussi en français.', ir: 'Voir en français', cerrar: 'Fermer' },
    pt: { aria: 'Idioma', texto: 'Esta página também está em português.', ir: 'Ver em português', cerrar: 'Fechar' },
    it: { aria: 'Lingua', texto: 'Questa pagina è disponibile anche in italiano.', ir: 'Vedi in italiano', cerrar: 'Chiudi' },
    id: { aria: 'Bahasa', texto: 'Halaman ini juga tersedia dalam Bahasa Indonesia.', ir: 'Lihat dalam Bahasa Indonesia', cerrar: 'Tutup' },
    ms: { aria: 'Bahasa', texto: 'Halaman ini turut tersedia dalam Bahasa Melayu.', ir: 'Lihat dalam Bahasa Melayu', cerrar: 'Tutup' },
    cs: { aria: 'Jazyk', texto: 'Tato stránka je k dispozici také v češtině.', ir: 'Zobrazit v češtině', cerrar: 'Zavřít' },
    da: { aria: 'Sprog', texto: 'Denne side findes også på dansk.', ir: 'Se på dansk', cerrar: 'Luk' },
    hu: { aria: 'Nyelv', texto: 'Ez az oldal magyarul is elérhető.', ir: 'Megtekintés magyarul', cerrar: 'Bezárás' },
    nl: { aria: 'Taal', texto: 'Deze pagina is ook beschikbaar in het Nederlands.', ir: 'Bekijk in het Nederlands', cerrar: 'Sluiten' },
    nb: { aria: 'Språk', texto: 'Denne siden finnes også på norsk.', ir: 'Se på norsk', cerrar: 'Lukk' },
    pl: { aria: 'Język', texto: 'Ta strona jest dostępna także po polsku.', ir: 'Zobacz po polsku', cerrar: 'Zamknij' },
    ro: { aria: 'Limba', texto: 'Această pagină este disponibilă și în română.', ir: 'Vezi în română', cerrar: 'Închide' },
    sk: { aria: 'Jazyk', texto: 'Táto stránka je dostupná aj v slovenčine.', ir: 'Zobraziť po slovensky', cerrar: 'Zavrieť' },
    fi: { aria: 'Kieli', texto: 'Tämä sivu on saatavilla myös suomeksi.', ir: 'Näytä suomeksi', cerrar: 'Sulje' },
    sv: { aria: 'Språk', texto: 'Den här sidan finns också på svenska.', ir: 'Visa på svenska', cerrar: 'Stäng' },
    vi: { aria: 'Ngôn ngữ', texto: 'Trang này cũng có bằng tiếng Việt.', ir: 'Xem bằng tiếng Việt', cerrar: 'Đóng' },
    tr: { aria: 'Dil', texto: 'Bu sayfa Türkçe olarak da mevcut.', ir: 'Türkçe görüntüle', cerrar: 'Kapat' },
    el: { aria: 'Γλώσσα', texto: 'Αυτή η σελίδα είναι διαθέσιμη και στα ελληνικά.', ir: 'Προβολή στα ελληνικά', cerrar: 'Κλείσιμο' },
    uk: { aria: 'Мова', texto: 'Ця сторінка доступна також українською.', ir: 'Дивитися українською', cerrar: 'Закрити' },
    he: { aria: 'שפה', texto: 'הדף הזה זמין גם בעברית.', ir: 'צפייה בעברית', cerrar: 'סגירה' },
    ar: { aria: 'اللغة', texto: 'هذه الصفحة متوفرة أيضًا باللغة العربية.', ir: 'عرض بالعربية', cerrar: 'إغلاق' },
    hi: { aria: 'भाषा', texto: 'यह पेज हिन्दी में भी उपलब्ध है।', ir: 'हिन्दी में देखें', cerrar: 'बंद करें' },
    th: { aria: 'ภาษา', texto: 'หน้านี้มีให้บริการเป็นภาษาไทยด้วย', ir: 'ดูเป็นภาษาไทย', cerrar: 'ปิด' },
    ko: { aria: '언어', texto: '이 페이지는 한국어로도 볼 수 있어요.', ir: '한국어로 보기', cerrar: '닫기' },
    ja: { aria: '言語', texto: 'このページは日本語でもご覧いただけます。', ir: '日本語で見る', cerrar: '閉じる' },
    'zh-hans': { aria: '语言', texto: '本页面也提供简体中文版本。', ir: '查看简体中文版', cerrar: '关闭' },
    'zh-hant': { aria: '語言', texto: '本頁面也提供繁體中文版本。', ir: '檢視繁體中文版', cerrar: '關閉' }
  };
  var actual = codigoIdioma(document.documentElement.lang);
  // Para medir el idioma recordado: el script del <head> deja de qué idioma venía antes de llevar a la persona aquí.
  try {
    var desde = sessionStorage.getItem('mandotv-idioma-desde');
    if (desde) {
      sessionStorage.removeItem('mandotv-idioma-desde');
      if (window.gtag) window.gtag('event', 'idioma_recordado', { desde: codigoIdioma(desde), hacia: actual });
    }
  } catch (e) { /* sigue */ }
  try { if (localStorage.getItem(IDIOMA_GUARDADO)) return; } catch (e) { /* sigue */ }
  // Quien ya navega dentro del sitio eligió su idioma (por ejemplo con el selector del pie): no se le insiste.
  try { if (document.referrer && new URL(document.referrer).host === location.host) return; } catch (e) { /* sigue */ }

  var gemelas = {};
  document.querySelectorAll('link[rel="alternate"][hreflang]').forEach(function (l) {
    gemelas[l.getAttribute('hreflang').toLowerCase()] = l.href;
  });
  var preferidos = navigator.languages && navigator.languages.length ? navigator.languages : [navigator.language || ''];
  var destino = null;
  for (var i = 0; i < preferidos.length; i++) {
    var c = codigoIdioma(preferidos[i]);
    if (c === actual) return;                       // su idioma preferido es el de esta página
    if (gemelas[c] && TEXTOS[c]) { destino = c; break; }
  }
  // Idioma que el sitio no tiene (japonés, polaco...): se ofrece el inglés, como el x-default de los hreflang.
  if (!destino && actual !== 'en' && gemelas.en) destino = 'en';
  if (!destino) return;

  var T = TEXTOS[destino];
  function crear() {
    var aviso = document.createElement('div');
    aviso.className = 'aviso-idioma';
    aviso.setAttribute('role', 'region');
    aviso.setAttribute('aria-label', T.aria);
    aviso.lang = destino;
    aviso.innerHTML =
      '<svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round">' +
      '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.5 2.6 3.8 5.6 3.8 9s-1.3 6.4-3.8 9c-2.5-2.6-3.8-5.6-3.8-9s1.3-6.4 3.8-9z"/></svg>' +
      '<p>' + T.texto + '</p>' +
      '<a class="boton" href="' + gemelas[destino] + '" hreflang="' + destino + '">' + T.ir + '</a>' +
      '<button type="button" class="aviso-idioma-cerrar" aria-label="' + T.cerrar + '">' +
      '<svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M6 6l12 12M18 6L6 18"/></svg></button>';
    aviso.querySelector('a').addEventListener('click', function () {
      guardarIdioma(destino);
      // Para medir cuánto se usa (solo si la persona aceptó las cookies de Google Analytics).
      if (window.gtag) window.gtag('event', 'aviso_idioma', { desde: actual, hacia: destino, transport_type: 'beacon' });
    });
    aviso.querySelector('button').addEventListener('click', function () {
      guardarIdioma(actual);  // cerrar es elegir quedarse en el idioma de esta página
      // Animación propia (con "reducir movimiento" de Windows las de CSS no corren).
      var salida = aviso.animate && aviso.animate([{ opacity: 1, transform: 'none' }, { opacity: 0, transform: 'translateY(10px) scale(.97)' }],
        { duration: 200, easing: 'cubic-bezier(.4, 0, 1, 1)', fill: 'forwards' });
      var quitar = function () { aviso.remove(); siguienteAviso(); };
      if (salida) salida.onfinish = quitar; else quitar();
    });
    var pila = pilaAvisos();
    pila.insertBefore(aviso, pila.firstChild);
    if (aviso.animate) {
      aviso.animate([{ opacity: 0, transform: 'translateY(14px) scale(.97)' }, { opacity: 1, transform: 'none' }],
        { duration: 380, easing: 'cubic-bezier(.2, .8, .2, 1)' });
    }
  }
  // Igual que el de cookies: espera las fuentes para no cambiar de tamaño ya visible.
  var crearConFuentes = function () {
    var listas = document.fonts && document.fonts.ready;
    if (listas) listas.then(crear, crear); else crear();
  };
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', crearConFuentes);
  else crearConFuentes();
})();

// Selector de idioma del pie (está en todas las páginas, igual que este archivo): se cierra al tocar fuera o con
// Escape, y el menú entra con una animación propia, porque con "reducir movimiento" de Windows no anima nada solo.
// Desde el 25-nov la misma lista sale también arriba, en la barra (globo y código del idioma), para cambiar de idioma
// sin bajar hasta el pie. Se arma aquí a partir de la lista del pie, así las páginas no repiten la lista.
(function () {
  function entrar(menu, y) {
    if (menu && menu.animate) {
      menu.animate([{ opacity: 0, transform: 'translateY(' + y + 'px) scale(.97)' }, { opacity: 1, transform: 'none' }],
        { duration: 220, easing: 'cubic-bezier(.2, .8, .2, 1)' });
    }
  }
  document.querySelectorAll('.pie-idioma').forEach(function (d) {
    var menu = d.querySelector('ul');
    d.addEventListener('toggle', function () { if (d.open) entrar(menu, 8); });
    document.addEventListener('click', function (e) { if (d.open && !d.contains(e.target)) d.open = false; });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && d.open) { d.open = false; d.querySelector('summary').focus(); }
    });
  });

  var pie = document.querySelector('.pie-idioma');
  var nav = document.querySelector('.barra nav');
  if (!pie || !nav || nav.querySelector('.barra-idioma')) return;
  var lista = pie.querySelector('ul');
  var actual = lista.querySelector('a[aria-current]');
  var cod = (actual ? actual.getAttribute('hreflang') : document.documentElement.lang) || '';
  var caja = document.createElement('div');
  caja.className = 'barra-idioma';
  var boton = document.createElement('button');
  boton.type = 'button';
  boton.className = 'barra-idioma-boton';
  boton.setAttribute('aria-expanded', 'false');
  boton.setAttribute('aria-controls', 'barra-idiomas');
  boton.setAttribute('aria-label', pie.querySelector('summary').textContent.replace(/\s+/g, ' ').trim());
  boton.innerHTML = '<svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.7">' +
    '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.4 2.6 3.6 5.6 3.6 9s-1.2 6.4-3.6 9c-2.4-2.6-3.6-5.6-3.6-9S9.6 5.6 12 3z"/></svg>' +
    '<span aria-hidden="true"></span>';
  boton.querySelector('span').textContent = cod.split('-')[0].toUpperCase();
  var menu = lista.cloneNode(true);
  menu.id = 'barra-idiomas';
  menu.hidden = true;
  caja.appendChild(boton);
  caja.appendChild(menu);
  nav.insertBefore(caja, nav.firstChild);
  function cerrar(foco) {
    if (menu.hidden) return;
    menu.hidden = true;
    boton.setAttribute('aria-expanded', 'false');
    if (foco) boton.focus();
  }
  boton.addEventListener('click', function () {
    if (!menu.hidden) { cerrar(false); return; }
    menu.hidden = false;
    boton.setAttribute('aria-expanded', 'true');
    entrar(menu, -8);
    var elegido = menu.querySelector('[aria-current]');
    if (elegido && elegido.scrollIntoView) elegido.scrollIntoView({ block: 'nearest' });
  });
  document.addEventListener('click', function (e) { if (!caja.contains(e.target)) cerrar(false); });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') cerrar(true); });
})();

// Descargar del pie: va directo a la tienda del equipo, con la misma detección que el botón principal de la portada
// (app.js): iPhone, iPad y Mac a la App Store, Windows a Microsoft Store y Android a los dos pasos de la prueba
// anticipada de Google Play (#android en la portada del idioma, como las insignias de las tiendas). Si no se reconoce
// el equipo, queda como está: baja a las tiendas (#tiendas).
(function () {
  var boton = document.querySelector('.pie-accion .boton');
  var logo = document.querySelector('.pie-logo');
  if (!boton || !logo) return;
  var ua = navigator.userAgent;
  var equipo = /iPad|iPhone|iPod|Macintosh/.test(ua) ? 'apple'
    : /Android/.test(ua) ? 'android'
    : (/Windows NT/.test(ua) && !/Mobile|Xbox/.test(ua)) ? 'windows' : null;
  var destino = {
    apple: 'https://apps.apple.com/app/id6834927348',
    windows: 'https://apps.microsoft.com/detail/9N3D7T1DP2SW?mode=direct',
    android: logo.getAttribute('href') + '#android'
  }[equipo];
  if (!destino) return;
  boton.href = destino;
  if (equipo !== 'android') { boton.target = '_blank'; boton.rel = 'noopener'; }
})();
