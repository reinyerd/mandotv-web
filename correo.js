// Enlaces de correo que funcionan en cualquier equipo.
// Un enlace "mailto:" no hace nada si el equipo no tiene app de correo configurada (muy común en Windows).
// Al pulsarlo mostramos un panel con: abrir Gmail, abrir la app de correo o copiar la dirección.
(function () {
  var panel, asunto, cuerpo, enlaceApp, enlaceGmail, aviso;
  // Textos por idioma (<html lang>): es por defecto; en, de, fr, pt e it con tabla propia.
  var TEXTOS = {
    es: { titulo: 'Escríbenos', es: 'Nuestro correo es', gmail: 'Abrir en Gmail', app: 'Abrir mi app de correo',
          copiar: 'Copiar dirección', cerrar: 'Cerrar', copiada: 'Dirección copiada. Pégala en tu correo.',
          copia: 'Copia la dirección: hola@mandotv.app', asunto: 'Hola Mando TV' },
    en: { titulo: 'Write to us', es: 'Our email is', gmail: 'Open in Gmail', app: 'Open my email app', copiar: 'Copy address',
          cerrar: 'Close', copiada: 'Address copied. Paste it into your email.', copia: 'Copy the address: hola@mandotv.app',
          asunto: 'Hello Mando TV' },
    de: { titulo: 'Schreib uns', es: 'Unsere E-Mail-Adresse ist', gmail: 'In Gmail öffnen', app: 'Meine E-Mail-App öffnen',
          copiar: 'Adresse kopieren', cerrar: 'Schließen', copiada: 'Adresse kopiert. Füge sie in deine E-Mail ein.',
          copia: 'Kopiere die Adresse: hola@mandotv.app', asunto: 'Hallo Mando TV' },
    fr: { titulo: 'Écrivez-nous', es: 'Notre adresse e-mail est', gmail: 'Ouvrir dans Gmail', app: 'Ouvrir mon application de messagerie',
          copiar: "Copier l'adresse", cerrar: 'Fermer', copiada: "Adresse copiée. Collez-la dans votre e-mail.",
          copia: "Copiez l'adresse : hola@mandotv.app", asunto: 'Bonjour Mando TV' },
    pt: { titulo: 'Escreva para a gente', es: 'Nosso e-mail é', gmail: 'Abrir no Gmail', app: 'Abrir meu app de e-mail',
          copiar: 'Copiar endereço', cerrar: 'Fechar', copiada: 'Endereço copiado. Cole no seu e-mail.',
          copia: 'Copie o endereço: hola@mandotv.app', asunto: 'Olá Mando TV' },
    it: { titulo: 'Scrivici', es: 'Il nostro indirizzo e-mail è', gmail: 'Apri in Gmail', app: 'Apri la mia app di posta',
          copiar: 'Copia indirizzo', cerrar: 'Chiudi', copiada: "Indirizzo copiato. Incollalo nella tua e-mail.",
          copia: "Copia l'indirizzo: hola@mandotv.app", asunto: 'Ciao Mando TV' },
    id: { titulo: 'Tulis ke kami', es: 'Email kami adalah', gmail: 'Buka di Gmail', app: 'Buka aplikasi email saya',
          copiar: 'Salin alamat', cerrar: 'Tutup', copiada: 'Alamat disalin. Tempel di email kamu.',
          copia: 'Salin alamatnya: hola@mandotv.app', asunto: 'Halo Mando TV' },
    ms: { titulo: 'Tulis kepada kami', es: 'E-mel kami ialah', gmail: 'Buka dalam Gmail', app: 'Buka aplikasi e-mel saya',
          copiar: 'Salin alamat', cerrar: 'Tutup', copiada: 'Alamat disalin. Tampalkan dalam e-mel anda.',
          copia: 'Salin alamat: hola@mandotv.app', asunto: 'Helo Mando TV' },
    cs: { titulo: 'Napište nám', es: 'Náš e-mail je', gmail: 'Otevřít v Gmailu', app: 'Otevřít e-mailovou aplikaci',
          copiar: 'Kopírovat adresu', cerrar: 'Zavřít', copiada: 'Adresa je zkopírovaná. Vložte ji do e-mailu.',
          copia: 'Zkopírujte adresu: hola@mandotv.app', asunto: 'Dobrý den, Mando TV' },
    da: { titulo: 'Skriv til os', es: 'Vores e-mail er', gmail: 'Åbn i Gmail', app: 'Åbn min mail-app',
          copiar: 'Kopier adresse', cerrar: 'Luk', copiada: 'Adressen er kopieret. Indsæt den i din mail.',
          copia: 'Kopier adressen: hola@mandotv.app', asunto: 'Hej Mando TV' },
    hu: { titulo: 'Írj nekünk', es: 'Az e-mail-címünk', gmail: 'Megnyitás Gmailben', app: 'E-mail alkalmazás megnyitása',
          copiar: 'Cím másolása', cerrar: 'Bezárás', copiada: 'A cím a vágólapon van. Illeszd be az e-mailedbe.',
          copia: 'Másold ki a címet: hola@mandotv.app', asunto: 'Üdv, Mando TV' },
    nl: { titulo: 'Schrijf ons', es: 'Ons e-mailadres is', gmail: 'Openen in Gmail', app: 'Mijn e-mailapp openen',
          copiar: 'Adres kopiëren', cerrar: 'Sluiten', copiada: 'Adres gekopieerd. Plak het in je e-mail.',
          copia: 'Kopieer het adres: hola@mandotv.app', asunto: 'Hallo Mando TV' },
    nb: { titulo: 'Skriv til oss', es: 'E-postadressen vår er', gmail: 'Åpne i Gmail', app: 'Åpne e-postappen min',
          copiar: 'Kopier adressen', cerrar: 'Lukk', copiada: 'Adressen er kopiert. Lim den inn i e-posten din.',
          copia: 'Kopier adressen: hola@mandotv.app', asunto: 'Hei Mando TV' },
    pl: { titulo: 'Napisz do nas', es: 'Nasz adres e-mail to', gmail: 'Otwórz w Gmailu', app: 'Otwórz aplikację pocztową',
          copiar: 'Kopiuj adres', cerrar: 'Zamknij', copiada: 'Adres skopiowany. Wklej go do swojego e-maila.',
          copia: 'Skopiuj adres: hola@mandotv.app', asunto: 'Cześć, Mando TV' },
    ro: { titulo: 'Scrie-ne', es: 'Adresa noastră de e-mail este', gmail: 'Deschide în Gmail', app: 'Deschide aplicația mea de e-mail',
          copiar: 'Copiază adresa', cerrar: 'Închide', copiada: 'Adresa a fost copiată. Lipește-o în e-mailul tău.',
          copia: 'Copiază adresa: hola@mandotv.app', asunto: 'Salut Mando TV' },
    sk: { titulo: 'Napíš nám', es: 'Náš e-mail je', gmail: 'Otvoriť v Gmaile', app: 'Otvoriť e-mailovú aplikáciu',
          copiar: 'Kopírovať adresu', cerrar: 'Zavrieť', copiada: 'Adresa je skopírovaná. Vlož ju do e-mailu.',
          copia: 'Skopíruj adresu: hola@mandotv.app', asunto: 'Dobrý deň, Mando TV' },
    fi: { titulo: 'Kirjoita meille', es: 'Sähköpostiosoitteemme on', gmail: 'Avaa Gmailissa', app: 'Avaa sähköpostisovellus',
          copiar: 'Kopioi osoite', cerrar: 'Sulje', copiada: 'Osoite kopioitu. Liitä se sähköpostiisi.',
          copia: 'Kopioi osoite: hola@mandotv.app', asunto: 'Hei Mando TV' },
    sv: { titulo: 'Skriv till oss', es: 'Vår e-postadress är', gmail: 'Öppna i Gmail', app: 'Öppna min e-postapp',
          copiar: 'Kopiera adressen', cerrar: 'Stäng', copiada: 'Adressen är kopierad. Klistra in den i ditt mejl.',
          copia: 'Kopiera adressen: hola@mandotv.app', asunto: 'Hej Mando TV' },
    vi: { titulo: 'Viết thư cho chúng tôi', es: 'Email của chúng tôi là', gmail: 'Mở trong Gmail', app: 'Mở ứng dụng email của tôi',
          copiar: 'Sao chép địa chỉ', cerrar: 'Đóng', copiada: 'Đã sao chép địa chỉ. Hãy dán vào email của bạn.',
          copia: 'Hãy sao chép địa chỉ: hola@mandotv.app', asunto: 'Xin chào Mando TV' },
    tr: { titulo: 'Bize yaz', es: 'E-posta adresimiz', gmail: "Gmail'de aç", app: 'E-posta uygulamamı aç',
          copiar: 'Adresi kopyala', cerrar: 'Kapat', copiada: 'Adres kopyalandı. E-postana yapıştır.',
          copia: 'Adresi kopyala: hola@mandotv.app', asunto: 'Merhaba Mando TV' },
    el: { titulo: 'Γράψε μας', es: 'Το email μας είναι', gmail: 'Άνοιγμα στο Gmail', app: 'Άνοιγμα της εφαρμογής email',
          copiar: 'Αντιγραφή διεύθυνσης', cerrar: 'Κλείσιμο', copiada: 'Η διεύθυνση αντιγράφηκε. Επικόλλησέ την στο email σου.',
          copia: 'Αντίγραψε τη διεύθυνση: hola@mandotv.app', asunto: 'Γεια σας Mando TV' },
    uk: { titulo: 'Напишіть нам', es: 'Наша електронна адреса', gmail: 'Відкрити в Gmail', app: 'Відкрити мій поштовий застосунок',
          copiar: 'Копіювати адресу', cerrar: 'Закрити', copiada: 'Адресу скопійовано. Вставте її у свій лист.',
          copia: 'Скопіюйте адресу: hola@mandotv.app', asunto: 'Вітаю, Mando TV' },
    he: { titulo: 'כתבו לנו', es: 'כתובת האימייל שלנו היא', gmail: 'פתיחה ב-Gmail', app: 'פתיחת אפליקציית האימייל שלי',
          copiar: 'העתקת הכתובת', cerrar: 'סגירה', copiada: 'הכתובת הועתקה. הדביקו אותה באימייל.',
          copia: 'העתיקו את הכתובת: hola@mandotv.app', asunto: 'שלום Mando TV' },
    ar: { titulo: 'راسلنا', es: 'بريدنا الإلكتروني هو', gmail: 'فتح في Gmail', app: 'فتح تطبيق البريد',
          copiar: 'نسخ العنوان', cerrar: 'إغلاق', copiada: 'تم نسخ العنوان. الصقه في بريدك الإلكتروني.',
          copia: 'انسخ العنوان: hola@mandotv.app', asunto: 'مرحبًا Mando TV' },
    hi: { titulo: 'हमें लिखें', es: 'हमारा ईमेल है', gmail: 'Gmail में खोलें', app: 'मेरा ईमेल ऐप खोलें',
          copiar: 'पता कॉपी करें', cerrar: 'बंद करें', copiada: 'पता कॉपी हो गया। इसे अपने ईमेल में पेस्ट करें।',
          copia: 'पता कॉपी करें: hola@mandotv.app', asunto: 'नमस्ते Mando TV' },
    th: { titulo: 'เขียนถึงเรา', es: 'อีเมลของเราคือ', gmail: 'เปิดใน Gmail', app: 'เปิดแอปอีเมลของฉัน',
          copiar: 'คัดลอกที่อยู่', cerrar: 'ปิด', copiada: 'คัดลอกที่อยู่แล้ว นำไปวางในอีเมลของคุณได้เลย',
          copia: 'คัดลอกที่อยู่นี้: hola@mandotv.app', asunto: 'สวัสดี Mando TV' },
    ko: { titulo: '문의하기', es: '이메일 주소는', gmail: 'Gmail에서 열기', app: '메일 앱 열기',
          copiar: '주소 복사', cerrar: '닫기', copiada: '주소를 복사했어요. 이메일에 붙여넣어 주세요.',
          copia: '주소를 복사해 주세요: hola@mandotv.app', asunto: '안녕하세요 Mando TV' },
    ja: { titulo: 'お問い合わせ', es: 'メールアドレスは次のとおりです', gmail: 'Gmailで開く', app: 'メールアプリを開く',
          copiar: 'アドレスをコピー', cerrar: '閉じる', copiada: 'アドレスをコピーしました。メールに貼り付けてください。',
          copia: 'アドレスをコピーしてください：hola@mandotv.app', asunto: 'Mando TVさんへ' },
    'zh-hans': { titulo: '联系我们', es: '我们的邮箱是', gmail: '在 Gmail 中打开', app: '打开我的邮件应用',
          copiar: '复制地址', cerrar: '关闭', copiada: '地址已复制，请粘贴到你的邮件中。',
          copia: '请复制地址：hola@mandotv.app', asunto: '你好，Mando TV' },
    'zh-hant': { titulo: '聯絡我們', es: '我們的電子郵件是', gmail: '在 Gmail 中開啟', app: '開啟我的郵件應用程式',
          copiar: '複製地址', cerrar: '關閉', copiada: '地址已複製，請貼到你的郵件中。',
          copia: '請複製地址：hola@mandotv.app', asunto: '你好，Mando TV' }
  };
  var L = (document.documentElement.lang || '').toLowerCase();  // zh-hans y zh-hant tienen tabla propia; pt-br usa pt
  var T = TEXTOS[L] || TEXTOS[L.slice(0, 2)] || TEXTOS.es;

  function crearPanel() {
    panel = document.createElement('dialog');
    panel.className = 'panel-correo';
    panel.setAttribute('aria-labelledby', 'panel-correo-titulo');
    panel.innerHTML =
      '<h1 id="panel-correo-titulo">' + T.titulo + '</h1>' +
      '<p>' + T.es + '</p>' +
      '<p class="panel-correo-dir">hola@mandotv.app</p>' +
      '<div class="panel-correo-acciones">' +
      '<a class="boton" id="pc-gmail" target="_blank" rel="noopener">' + T.gmail + '</a>' +
      '<a class="boton claro" id="pc-app">' + T.app + '</a>' +
      '<button type="button" class="boton claro" id="pc-copiar">' + T.copiar + '</button>' +
      '</div>' +
      '<p class="panel-correo-aviso" id="pc-aviso" role="status"></p>' +
      '<button type="button" class="panel-correo-cerrar" id="pc-cerrar" aria-label="' + T.cerrar + '">×</button>';
    document.body.appendChild(panel);
    enlaceGmail = panel.querySelector('#pc-gmail');
    enlaceApp = panel.querySelector('#pc-app');
    aviso = panel.querySelector('#pc-aviso');
    panel.querySelector('#pc-cerrar').addEventListener('click', function () { panel.close(); });
    panel.setAttribute('closedby', 'any'); // clic fuera cierra (nativo en Chrome, Edge y Firefox)
    if (!('closedBy' in HTMLDialogElement.prototype)) { // Safari: mismo cierre, mirando la posición del puntero
      var fuera = function (e) {
        var r = panel.getBoundingClientRect();
        return e.clientX < r.left || e.clientX > r.right || e.clientY < r.top || e.clientY > r.bottom;
      };
      var pulsoFuera = false;
      panel.addEventListener('pointerdown', function (e) { pulsoFuera = fuera(e); });
      panel.addEventListener('pointerup', function (e) { if (pulsoFuera && fuera(e)) panel.close(); });
    }
    panel.querySelector('#pc-copiar').addEventListener('click', copiar);
  }

  function copiar() {
    var listo = function () { decir(T.copiada); };
    if (navigator.clipboard && window.isSecureContext) {
      navigator.clipboard.writeText('hola@mandotv.app').then(listo, function () { decir(T.copia); });
    } else {
      decir(T.copia);
    }
  }

  // VoiceOver no repite un aviso idéntico al anterior: si se repite, se alterna un espacio duro al final.
  var ultimo = '';
  function decir(m) {
    if (m === ultimo) m += ' ';
    ultimo = m;
    aviso.textContent = '';
    requestAnimationFrame(function () { aviso.textContent = m; });
  }

  function abrir(href) {
    if (!panel) crearPanel();
    var url = new URL(href);
    asunto = url.searchParams.get('subject') || T.asunto;
    cuerpo = url.searchParams.get('body') || '';
    enlaceApp.href = href;
    enlaceGmail.href = 'https://mail.google.com/mail/?view=cm&fs=1&to=hola@mandotv.app&su=' +
      encodeURIComponent(asunto) + '&body=' + encodeURIComponent(cuerpo);
    aviso.textContent = '';
    panel.showModal();
  }

  if (typeof HTMLDialogElement !== 'function') return; // navegador antiguo: queda el enlace normal
  document.addEventListener('click', function (e) {
    var a = e.target.closest && e.target.closest('a[href^="mailto:"]');
    if (!a || a.id === 'pc-app') return;
    e.preventDefault();
    abrir(a.href);
  });
})();
