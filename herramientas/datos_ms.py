# Textos en Bahasa Melayu (Malaysia, "anda") de mandotv.app. Los usa generar_idiomas.py. Escritos para las búsquedas de Malasia.
# Las claves de las páginas (lg, lost-tv, ...) y sus rutas están en idiomas_sitio.py.
# Los nombres de menús y botones de la app (Input, Tambah melalui IP, Peribadikan, Salin laporan ujian, Pulihkan pembelian,
# Sambung semula, Hidupkan, Pasangkan) son los mismos que usa la app en malayo (lib/l10n/app_ms.arb del proyecto de la app).

UI = dict(
  locale='ms_MY',
  aria_home='Mando TV, laman utama', aria_main='Menu utama', nav_que='Ciri', nav_ayuda='Bantuan', nav_contacto='Hubungi kami',
  asunto='Helo%20Mando%20TV', inicio='Laman utama', privacidad='Privasi', aria_pie='Kaki laman', aria_ruta='Laluan navigasi',
  aria_marcas='Jenama dan panduan', hecho='Dibangunkan di Chile',
  aviso='Mando TV ialah aplikasi bebas. Ia tidak berkaitan dengan, dan tidak disokong oleh, mana-mana pengeluar TV yang disebut mahupun Google, Amazon, Apple atau Roku. Jenama dagangan dimiliki oleh pemilik masing-masing dan disebut hanya untuk menyatakan keserasian. Android TV dan Google TV ialah tanda dagangan Google LLC. Apple TV ialah tanda dagangan Apple Inc.',
  bajar='Muat turun percuma', descarga='Muat turun di', anticipada='Akses awal di',
  apple_aria='Muat turun Mando TV percuma di App Store', ms_aria='Muat turun Mando TV percuma di Microsoft Store',
  gp_aria='Akses awal Mando TV di Google Play untuk Android', aria_desc='Muat turun Mando TV',
  b_como_btn='Cara menyambung', b_tiendas_label='Terdapat di kedai aplikasi',
  b_nota='iPhone, iPad, Mac, Android dan Windows. Muat turun percuma, tanpa iklan. Pro ialah pembelian sekali sahaja, tanpa langganan.',
  b_compat='TV yang serasi', b_otras='Jenama lain', b_otras_p='Mando TV mengawal semua jenama ini dengan satu aplikasi yang sama:',
  g_guias='Panduan', g_ver='Lihat langkah', g_pasos='Langkah demi langkah', g_hazlo='Cara melakukannya dengan Mando TV',
  g_tiendas='Mando TV ialah alat kawalan jauh universal untuk TV anda. Muat turun percuma, tanpa iklan dan tanpa akaun. Pro ialah pembelian sekali sahaja yang pilihan, tanpa langganan. Untuk iPhone, iPad, Windows dan Android:',
  g_nota='Android: akses awal percuma di Google Play. <a href="{enlace}">Sertai dalam dua langkah</a> dan bantu kami sampai ke kedai aplikasi.',
  g_mas_pagina='Anda boleh dapatkan butiran lanjut di halaman {enlace}.', g_mas_marca='Butiran lanjut mengikut jenama:',
  g_faq='Soalan lazim', g_mas='Panduan lain', g_todas='Semua panduan', g_ayuda='Bantuan dan sokongan',
  g_idiomas='Panduan ini dalam bahasa lain',
)

# Pie de página y listas de marcas/guías: (clave, texto)
PIE = [
  ('samsung', 'Alat kawalan jauh Samsung'),
  ('lg', 'Alat kawalan jauh LG'),
  ('roku', 'Alat kawalan jauh Roku'),
  ('android', 'Alat kawalan jauh Android TV'),
  ('guias', 'Semua panduan'),
  ('lost-tv', 'Alat kawalan jauh hilang'),
  ('lost-lg', 'Alat kawalan jauh LG hilang'),
  ('lg-on', 'Hidupkan TV LG dengan telefon'),
  ('hdmi', 'Tukar input HDMI tanpa alat kawalan jauh'),
  ('androidtv', 'Android TV tanpa alat kawalan jauh'),
  ('console', 'TV dan HDMI konsol tanpa alat kawalan jauh'),
  ('samsung-lost', 'TV Samsung tanpa alat kawalan jauh'),
  ('roku-lost', 'Alat kawalan jauh Roku hilang'),
  ('roku-403', 'Aplikasi Roku tidak berfungsi'),
  ('androidtv-code', 'Kod pasangan Android TV'),
  ('not-found', 'Telefon tidak jumpa TV'),
  ('wifi', 'Telefon sebagai alat kawalan jauh melalui Wi-Fi'),
  ('pc', 'Kawal TV dengan PC'),
]
NOMBRE_OTRA = {'lg': 'Aplikasi alat kawalan jauh LG', 'samsung': 'Aplikasi alat kawalan jauh Samsung', 'roku': 'Aplikasi alat kawalan jauh Roku',
               'android': 'Aplikasi alat kawalan jauh Android TV dan Google TV'}
PAGINA_MARCA = {'lg': 'Aplikasi alat kawalan jauh LG', 'samsung': 'Aplikasi alat kawalan jauh Samsung', 'roku': 'Aplikasi alat kawalan jauh Roku',
                'android': 'Aplikasi alat kawalan jauh Android TV'}

OTRAS_GUIAS = [
  ('lg-on', 'Hidupkan TV LG dengan telefon'),
  ('lost-tv', 'Alat kawalan jauh hilang: apa yang boleh anda lakukan'),
  ('lost-lg', 'Alat kawalan jauh LG hilang: cara guna telefon anda'),
  ('hdmi', 'Tukar input HDMI pada TV tanpa alat kawalan jauh'),
  ('androidtv', 'Android TV tanpa alat kawalan jauh: cara guna telefon anda'),
  ('console', 'Hidupkan TV dan tukar ke HDMI konsol tanpa alat kawalan jauh'),
  ('samsung-lost', 'TV Samsung tanpa alat kawalan jauh asal: cara guna telefon anda'),
  ('roku-lost', 'Alat kawalan jauh Roku hilang: cara guna telefon anda'),
  ('roku-403', 'Aplikasi Roku tidak berfungsi: betulkan ralat 403'),
  ('androidtv-code', 'Android TV meminta kod pasangan: apa yang perlu dibuat'),
  ('not-found', 'Telefon anda tidak jumpa TV: perkara yang perlu disemak'),
  ('wifi', 'Cara guna telefon sebagai alat kawalan jauh melalui Wi-Fi'),
  ('pc', 'Cara kawal TV anda dengan PC Windows'),
]

INDICE = dict(
  titulo='Panduan: kawal TV dengan telefon anda | Mando TV',
  desc='Panduan langkah demi langkah: guna telefon atau PC sebagai alat kawalan jauh, hidupkan TV, tukar HDMI dan selesaikan masalah pada Samsung, LG dan Roku.',
  h1='Panduan: guna telefon sebagai alat kawalan jauh',
  intro='Langkah mudah untuk menyambungkan alat kawalan jauh TV Samsung, LG, Roku atau Android TV anda dengan Mando TV, menghidupkan TV dan menyelesaikan masalah.',
  h2_guias='Semua panduan', h2_marcas='Aplikasi alat kawalan jauh mengikut jenama',
  marcas_extra=[('sony', 'Aplikasi alat kawalan jauh Sony'), ('philips', 'Aplikasi alat kawalan jauh Philips')],
)

MARCAS = [
  dict(clave='lg', color='#e0457b', corto='LG',
    titulo='Aplikasi Alat Kawalan Jauh TV LG di Telefon, Percuma | Mando TV',
    desc='Telefon atau PC anda sebagai alat kawalan jauh TV LG webOS melalui Wi-Fi. Butang, papan kekunci, apl, input dan hidupkan TV percuma; penuding dengan Pro.',
    h1='Alat kawalan jauh TV LG sebagai aplikasi di telefon',
    intro='Mando TV ialah aplikasi alat kawalan jauh untuk TV LG: ia menjadikan telefon atau komputer anda alat kawalan jauh untuk TV pintar LG webOS anda melalui Wi-Fi di rumah. Berguna apabila alat kawalan jauh hilang, bateri habis, atau anda sekadar mahu menaip dengan lebih pantas.',
    compat='TV pintar LG dengan webOS (kebanyakan model TV pintar LG sejak 2014). Berfungsi dengan TV LED, NanoCell, QNED dan OLED. TV pintar LG yang lebih lama dengan NetCast (2011 hingga 2014, sebelum webOS) kini disokong dalam beta: ia dipasangkan dengan kunci 6 digit yang dipaparkan pada TV.',
    h2=dict(funciones='Apa yang boleh anda lakukan dengan TV LG anda', como='Cara menyambungkan TV LG anda dengan Mando TV',
            encender='Hidupkan TV LG dengan telefon', preguntas='Soalan tentang LG', guias='Panduan untuk LG'),
    funciones=[
      ('Semua butang', 'Pad arah, OK, Kembali, Utama, volum, saluran, senyap dan main semula.'),
      ('Penuding seperti Magic Remote (Pro)', 'Gerakkan anak panah dengan jari pada skrin, sama seperti dengan LG Magic Remote.'),
      ('Papan kekunci', 'Taip dalam YouTube, Netflix atau pelayar TV dengan papan kekunci telefon anda.'),
      ('Apl dan input', 'Buka apl anda dan tukar ke HDMI, TV langsung, AirPlay atau Screen Share.'),
      ('Output audio (Pro)', 'Tukar antara pembesar suara TV dan bar bunyi anda.'),
      ('Hidupkan TV', 'Jika TV dimatikan, Mando TV menghidupkannya melalui rangkaian dan menyambung sendiri.'),
    ],
    pasos=[
      'Sambungkan telefon dan TV ke Wi-Fi yang sama.',
      'Buka Mando TV: TV LG anda muncul sendiri dalam senarai. Ketik padanya.',
      'Satu pertanyaan akan muncul pada TV untuk meminta kebenaran. Sahkannya dengan alat kawalan jauh biasa anda (hanya kali pertama).',
    ],
    encender='Pada TV LG, buka Tetapan dan cari "Hidupkan TV dengan peranti mudah alih" (di bawah Tetapan, Umum, Peranti, Peranti Luaran; pada model lama di Sambungan, Pengurusan Sambungan Mudah Alih). Aktifkan "Hidupkan melalui Wi-Fi". Jika ada "Quick Start+", aktifkan juga. Selepas itu, apabila anda mengetik TV yang dimatikan dalam Mando TV, aplikasi bertanya sama ada anda mahu menghidupkannya dan menyambung sendiri.',
    faq=[
      ('Adakah saya perlukan Magic Remote untuk menggunakan Mando TV?', 'Hanya kali pertama, untuk mengesahkan pertanyaan pada skrin. Selepas itu, telefon anda sudah mencukupi.'),
      ('Adakah Mando TV menggantikan aplikasi LG ThinQ?', 'Untuk mengawal TV, ya: anda tidak perlukan akaun LG dan tidak perlu mendaftarkan TV. Mando TV menyambung terus melalui Wi-Fi anda.'),
      ('Bolehkah saya menghidupkan TV LG saya dengan telefon?', 'Ya, jika anda telah mengaktifkan "Hidupkan TV dengan peranti mudah alih" pada TV dan pernah menyambung sekali semasa TV dihidupkan.'),
      ('Adakah ia berfungsi dengan TV LG lama sebelum webOS?', 'Dalam beta, ya, dengan TV pintar LG NetCast dari 2011 hingga 2014. Ia dipasangkan dengan kunci 6 digit yang dipaparkan pada TV. Ciri ini baharu dan mungkin masih ada kekurangan.'),
    ],
    guias=[('lg-on', 'Cara menghidupkan TV LG dengan telefon'),
           ('lost-lg', 'Alat kawalan jauh LG hilang: cara guna telefon anda'),
           ('hdmi', 'Tukar input HDMI pada TV tanpa alat kawalan jauh'),
           ('guias', 'Semua panduan untuk mengawal TV dengan telefon')]),
  dict(clave='samsung', color='#3d7bff', corto='Samsung',
    titulo='Aplikasi Alat Kawalan Jauh TV Samsung di Telefon | Mando TV',
    desc='Telefon atau PC sebagai alat kawalan jauh TV Samsung Tizen melalui Wi-Fi. Butang, papan kekunci, apl dan hidupkan TV percuma; pad sentuh dengan Pro.',
    h1='Alat kawalan jauh TV Samsung sebagai aplikasi di telefon',
    intro='Mando TV ialah aplikasi alat kawalan jauh untuk TV Samsung: ia menjadikan telefon atau komputer anda alat kawalan jauh untuk TV pintar Samsung anda melalui Wi-Fi di rumah. Anda tidak perlukan akaun Samsung dan tidak perlu mendaftarkan TV.',
    compat='TV pintar Samsung dengan Tizen, model 2016 dan ke atas (siri seperti Crystal UHD, QLED, Neo QLED, The Frame dan OLED).',
    h2=dict(funciones='Apa yang boleh anda lakukan dengan TV Samsung anda', como='Cara menyambungkan TV Samsung anda dengan Mando TV',
            encender='Hidupkan TV Samsung dengan telefon', preguntas='Soalan tentang Samsung', guias='Panduan untuk Samsung'),
    funciones=[
      ('Semua butang', 'Pad arah, OK, Kembali, Utama, volum, saluran, senyap dan sumber.'),
      ('Pad sentuh (Pro)', 'Leret jari anda melalui menu tanpa mencari butang anak panah.'),
      ('Papan kekunci', 'Taip carian dan kata laluan dengan papan kekunci telefon anda.'),
      ('Apl', 'Buka Netflix, YouTube, Prime Video dan apl lain anda dengan satu ketikan.'),
      ('Hidupkan TV', 'Jika TV dimatikan, Mando TV menghidupkannya melalui rangkaian dan menyambung sendiri.'),
      ('Tanpa akaun', 'Sambungan berlaku terus melalui Wi-Fi anda, tanpa melalui internet.'),
    ],
    pasos=[
      'Sambungkan telefon dan TV ke Wi-Fi yang sama.',
      'Buka Mando TV: TV Samsung anda muncul sendiri dalam senarai. Ketik padanya.',
      'TV bertanya sama ada anda membenarkan sambungan. Pilih "Benarkan" dengan alat kawalan jauh (hanya kali pertama).',
    ],
    encender='Pada TV Samsung, di bawah Tetapan > Umum > Rangkaian > Tetapan Pakar, aktifkan "Hidupkan dengan mudah alih" (Power On with Mobile). Selepas itu, apabila anda mengetik TV yang dimatikan dalam Mando TV, aplikasi bertanya sama ada anda mahu menghidupkannya dan menyambung sendiri.',
    faq=[
      ('Saya tertolak kebenaran secara tidak sengaja. Apa yang perlu dibuat?', 'Pada TV, pergi ke Tetapan > Umum > Pengurus Peranti Luaran > Pengurus Sambungan Peranti dan tetapkan Mando TV kepada dibenarkan.'),
      ('Adakah Mando TV menggantikan SmartThings?', 'Untuk mengawal TV, ya, dan tanpa akaun Samsung. Mando TV menyambung terus melalui Wi-Fi anda.'),
      ('Adakah ia berfungsi dengan TV Samsung yang lebih lama?', 'Ia berfungsi dengan TV Samsung dengan Tizen, model 2016 dan ke atas. Model yang lebih awal menggunakan sistem lain yang belum kami sokong.'),
    ],
    guias=[('samsung-lost', 'TV Samsung tanpa alat kawalan jauh asal: cara guna telefon anda'),
           ('smartthings', 'Alternatif SmartThings untuk TV Samsung'),
           ('turn-on', 'Cara menghidupkan TV tanpa alat kawalan jauh'),
           ('hdmi', 'Tukar input HDMI pada TV tanpa alat kawalan jauh'),
           ('guias', 'Semua panduan untuk mengawal TV dengan telefon')]),
  dict(clave='roku', color='#a77bff', corto='Roku',
    titulo='Aplikasi Alat Kawalan Jauh Roku di Telefon, Percuma | Mando TV',
    desc='Telefon atau PC anda sebagai alat kawalan jauh Roku untuk Roku TV dan pemain Roku melalui Wi-Fi. Butang, papan kekunci, saluran, input dan hidupkan TV percuma.',
    h1='Alat kawalan jauh Roku sebagai aplikasi di telefon',
    intro='Mando TV ialah aplikasi alat kawalan jauh untuk Roku: ia menjadikan telefon atau komputer anda alat kawalan jauh untuk Roku anda melalui Wi-Fi di rumah. Ia berfungsi dengan peranti Roku TV dan dengan pemain Roku yang disambungkan ke port HDMI.',
    compat='Peranti Roku TV (TCL, Hisense, Philips, Sharp, JVC dan lain-lain) dan pemain Roku (Express, Streaming Stick, Ultra).',
    h2=dict(funciones='Apa yang boleh anda lakukan dengan Roku anda', como='Cara menyambungkan Roku anda dengan Mando TV',
            encender='Hidupkan Roku dengan telefon', preguntas='Soalan tentang Roku', guias='Panduan untuk Roku'),
    funciones=[
      ('Semua butang', 'Pad arah, OK, Kembali, Utama, volum, senyap, main semula dan main.'),
      ('Papan kekunci', 'Taip carian dalam saluran Roku dengan papan kekunci telefon anda.'),
      ('Saluran', 'Buka Netflix, YouTube dan saluran Roku anda yang lain dengan satu ketikan.'),
      ('Input', 'Pada Roku TV, tukar ke HDMI, antena atau AV daripada aplikasi.'),
      ('Hidupkan TV', 'Pada peranti Roku TV dengan permulaan pantas, Mando TV menghidupkannya daripada telefon anda.'),
      ('Tanpa pemasangan', 'Roku tidak meminta kod: ketik padanya dalam senarai dan anda sudah bersambung.'),
      ('Bunyikan alat kawalan jauh', 'Jika alat kawalan jauh Roku anda mempunyai pembesar suara, seperti Roku Voice Remote Pro, Mando TV membuatnya berbunyi supaya anda dapat mencarinya. Percuma, dan Roku mesti dihidupkan.'),
    ],
    pasos=[
      'Sambungkan telefon dan Roku ke Wi-Fi yang sama.',
      'Buka Mando TV: Roku anda muncul sendiri dalam senarai. Ketik padanya.',
      'Jika sambungan tidak berjaya, pada Roku pergi ke Tetapan > Sistem > Tetapan sistem lanjutan > Kawalan oleh aplikasi mudah alih dan tetapkan akses rangkaian kepada Lalai atau Permissive (pada perisian Roku yang lebih baharu, tetapkan "Kawalan oleh aplikasi mudah alih" kepada Dibenarkan).',
    ],
    encender='Pada peranti Roku TV, di bawah Tetapan > Sistem > Kuasa, aktifkan "Permulaan pantas TV" (Fast TV start). Pemain Roku yang disambungkan ke TV lain tidak boleh dihidupkan dengan cara ini. Selepas itu, apabila anda mengetik TV yang dimatikan dalam Mando TV, aplikasi bertanya sama ada anda mahu menghidupkannya dan menyambung sendiri.',
    faq=[
      ('Adakah ia berfungsi dengan Roku Express atau Streaming Stick?', 'Ya. Semua pemain Roku dan peranti Roku TV dikawal dengan cara yang sama.'),
      ('Mando TV tidak jumpa Roku saya. Apa yang perlu dibuat?', 'Semak sama ada kedua-duanya berada dalam Wi-Fi yang sama dan sama ada "Kawalan oleh aplikasi mudah alih" pada Roku tidak dimatikan. Anda juga boleh menambahnya melalui alamat IP.'),
      ('Adakah saya perlukan akaun Roku?', 'Tidak. Mando TV menyambung terus melalui Wi-Fi anda.'),
    ],
    guias=[('roku-403', 'Aplikasi Roku tidak berfungsi (ralat 403)'),
           ('roku-lost', 'Alat kawalan jauh Roku hilang: cara guna telefon anda'),
           ('tcl', 'Aplikasi alat kawalan jauh TCL'),
           ('hisense', 'Aplikasi alat kawalan jauh Hisense'),
           ('philips', 'Aplikasi alat kawalan jauh Philips'),
           ('guias', 'Semua panduan untuk mengawal TV dengan telefon')]),
  dict(clave='android', color='#2fbf8f', corto='Android TV dan Google TV',
    titulo='Aplikasi Kawalan Jauh Google TV dan Android TV | Mando TV',
    desc='Kawalan jauh Google TV dan Android TV (Sony, TCL) di telefon atau PC melalui Wi-Fi. Butang, papan kekunci, apl, hidupkan TV percuma; pad sentuh dengan Pro.',
    h1='Alat kawalan jauh Google TV dan Android TV sebagai aplikasi di telefon',
    intro='Mando TV ialah aplikasi alat kawalan jauh untuk Android TV: ia menjadikan telefon atau komputer anda alat kawalan jauh untuk TV Android TV atau Google TV anda melalui Wi-Fi di rumah. Ia juga berfungsi daripada iPhone dan Windows.',
    compat='TV dengan Google TV atau Android TV daripada Sony, Philips, TCL, Hisense, Sharp, Xiaomi, Toshiba, Panasonic, Haier, Skyworth, JVC, Thomson, Motorola, OnePlus, iFFALCON, Kogan, Vu dan jenama lain, serta Chromecast dengan Google TV, Google TV Streamer, onn. dan Nvidia Shield. Sesetengah jenama ini turut menjual model dengan sistem lain: jika TV anda memaparkan skrin utama Google TV atau mempunyai Google Play Store, Mando TV mengawalnya.',
    h2=dict(funciones='Apa yang boleh anda lakukan dengan Android TV anda', como='Cara menyambungkan Android TV anda dengan Mando TV',
            encender='Hidupkan Android TV dengan telefon', preguntas='Soalan tentang Android TV', guias='Panduan untuk Android TV'),
    funciones=[
      ('Semua butang', 'Pad arah, OK, Kembali, Utama, volum, senyap dan main semula.'),
      ('Pad sentuh (Pro)', 'Leret jari anda untuk menavigasi menu Google TV dengan pantas.'),
      ('Papan kekunci', 'Taip carian dan kata laluan dengan papan kekunci telefon anda.'),
      ('Apl', 'Buka YouTube, Netflix, Disney+ dan apl lain anda dengan satu ketikan.'),
      ('Hidupkan TV', 'Pada model yang boleh dihidupkan melalui rangkaian, Mando TV menghidupkan TV dan menyambung sendiri.'),
      ('iPhone, Android dan PC', 'Ia berfungsi sama sahaja pada mana-mana telefon dan mana-mana komputer.'),
    ],
    pasos=[
      'Sambungkan telefon dan TV ke Wi-Fi yang sama.',
      'Buka Mando TV: Android TV anda muncul sendiri dalam senarai. Ketik padanya.',
      'TV memaparkan kod 6 aksara. Masukkannya dalam Mando TV (hanya kali pertama).',
    ],
    encender='Ini bergantung pada pengeluar. Dalam tetapan rangkaian atau kuasa, cari "Wake on LAN", "Hidupkan melalui rangkaian", "Network standby" atau "Remote start". Sesetengah model tidak mempunyai pilihan ini. Selepas itu, apabila anda mengetik TV yang dimatikan dalam Mando TV, aplikasi bertanya sama ada anda mahu menghidupkannya dan menyambung sendiri.',
    faq=[
      ('Adakah ia berfungsi dengan Chromecast dengan Google TV?', 'Ya, pemasangan dibuat dengan kod 6 aksara yang muncul pada skrin.'),
      ('Apakah bezanya dengan aplikasi Google TV?', 'Mando TV tidak memerlukan akaun Google, turut berfungsi pada Windows dan mengawal TV LG, Samsung dan Roku dengan aplikasi yang sama.'),
      ('Kod tidak muncul pada skrin. Apa yang perlu dibuat?', 'Tutup Mando TV, buka aplikasi sekali lagi dan ketik TV semula. Pastikan TV tidak berada dalam mod jimat kuasa yang dalam.'),
    ],
    guias=[('androidtv-code', 'Android TV meminta kod pasangan: apa yang perlu dibuat'),
           ('androidtv', 'Android TV tanpa alat kawalan jauh: cara guna telefon anda'),
           ('googletv-alt', 'Alternatif alat kawalan jauh Google TV pada telefon'),
           ('sony', 'Aplikasi alat kawalan jauh Sony'),
           ('tcl', 'Aplikasi alat kawalan jauh TCL'),
           ('hisense', 'Aplikasi alat kawalan jauh Hisense'),
           ('philips', 'Aplikasi alat kawalan jauh Philips'),
           ('guias', 'Semua panduan untuk mengawal TV dengan telefon')]),
]

GUIAS = [
  dict(clave='lost-tv', corto='Alat kawalan jauh hilang',
    titulo='Alat Kawalan Jauh Hilang? Kawal TV dengan Telefon',
    desc='Alat kawalan jauh hilang? Hidupkan TV dengan butangnya dan guna telefon sebagai alat kawalan. Langkah untuk LG, Samsung, Roku, Android TV. Percuma.',
    h1='Alat kawalan jauh hilang? Apa yang boleh anda lakukan sekarang',
    intro='Alat kawalan jauh hilang berlaku di mana-mana rumah: ia lesap tepat pada masa anda mahu menonton sesuatu. Berita baiknya, telefon anda boleh menggantikan alat kawalan jauh melalui Wi-Fi di rumah. Berikut ialah apa yang boleh anda lakukan, mengikut urutan.',
    pasos=[
      'Hidupkan TV dengan butang pada TV itu sendiri. Hampir selalu ia terletak di bawah di tengah atau di belakang berhampiran satu sudut. Kadangkala ia satu butang, kadangkala kayu bedik kecil.',
      'Sambungkan telefon anda ke Wi-Fi yang sama dengan TV.',
      'Muat turun Mando TV, yang percuma dan tidak meminta akaun, dan buka aplikasi. TV anda muncul sendiri dalam senarai. Ketik padanya.',
      'Sahkan sambungan untuk jenama anda. Pada LG dan Samsung, TV memaparkan pertanyaan: sahkannya dengan butang atau kayu bedik pada TV itu sendiri. Pada Android TV dan Google TV, anda memasukkan kod 6 aksara yang muncul pada skrin. Roku tidak meminta apa-apa.',
      'Siap. Anak panah, OK, Kembali, Utama, volum, saluran dan papan kekunci adalah percuma.',
      'Untuk lain kali: dalam tetapan TV, aktifkan hidupkan melalui rangkaian (panduan untuk jenama anda ada di bawah). Dengan itu anda boleh menghidupkan TV daripada telefon tanpa menyentuhnya.',
    ],
    extra=[
      ('Pilih panduan untuk jenama anda', 'LG: [Alat kawalan jauh LG hilang](@lost-lg). Android TV dan Google TV: [Android TV tanpa alat kawalan jauh](@androidtv). Samsung: [TV Samsung tanpa alat kawalan jauh](@samsung-lost). Roku: [Alat kawalan jauh Roku hilang](@roku-lost).'),
      ('Jika TV tidak dapat dihidupkan dengan butang', 'Sebelum mencari alat kawalan jauh lain, semak sama ada kabel dipasang dengan kemas dan soket ada elektrik. Jika butang pada TV tidak berbuat apa-apa, masalahnya ada pada TV dan bukan pada alat kawalan jauh.'),
      ('Jika alat kawalan jauh sekadar tidak berfungsi lagi', 'Cuba bateri baharu. Untuk menyemak sama ada ia masih menghantar isyarat, halakan ia ke kamera telefon dan tekan satu butang: pada banyak telefon anda akan nampak cahaya ungu pada skrin. Jika cahaya itu ada tetapi TV tidak bertindak balas, mungkin penderia pada TV terlindung.'),
      ('Jika anda menukar penghala dan TV tiada Wi-Fi', 'Tanpa alat kawalan jauh, lebih sukar untuk menyambungkan TV ke rangkaian baharu. Cara paling mudah ialah menyambungkan TV ke penghala dengan kabel rangkaian. Anda juga boleh menyediakan Wi-Fi dengan nama dan kata laluan yang sama seperti dahulu: TV biasanya menyambung sendiri.'),
      ('Apa yang percuma dan apa yang Pro', 'Menghidupkan dan mematikan TV, anak panah, OK, volum, saluran, nombor, papan kekunci, membuka apl dan menukar input adalah percuma. Pad sentuh, suara dan rutin tergolong dalam Mando TV Pro, pembelian sekali sahaja tanpa langganan.'),
    ],
    marca=None,
    faq=[
      ('Bolehkah saya menghidupkan TV dengan telefon jika belum pernah menyambungkannya?', 'Kali pertama, anda menghidupkannya dengan butang pada TV. Selepas anda menyambungkan telefon dan mengaktifkan hidupkan melalui rangkaian dalam tetapan TV, anda boleh menghidupkannya daripada aplikasi.'),
      ('Perlukah saya membeli alat kawalan jauh baharu?', 'Belum tentu. Dengan Mando TV, butang, volum, papan kekunci dan hidupkan TV adalah percuma. Jika anda tetap mahukan alat kawalan jauh sebenar, cari model tepat TV anda.'),
      ('Adakah ia berfungsi jika TV tiada Wi-Fi?', 'Kebanyakannya tidak. Telefon dan TV lazimnya mesti berada dalam Wi-Fi yang sama. Pengecualiannya ialah inframerah pada telefon Android yang ada pemancar inframerah, yang juga boleh mengawal TV yang bukan TV pintar, dan Bluetooth dalam beta mulai Android 9, yang berfungsi tanpa Wi-Fi sama sekali dengan Google TV, Android TV dan Fire TV.'),
    ]),
  dict(clave='lost-lg', corto='Alat kawalan jauh LG hilang',
    titulo='Alat Kawalan Jauh LG Hilang? Guna Telefon Anda',
    desc='Tiada alat kawalan jauh LG? Hidupkan TV dengan butang pada TV, sahkan pertanyaan dan guna telefon anda melalui Wi-Fi. Tanpa akaun LG, tanpa iklan.',
    h1='Alat kawalan jauh LG hilang? Cara guna telefon anda',
    intro='Jika alat kawalan jauh LG anda hilang atau Magic Remote tidak berfungsi lagi, telefon anda menggantikannya melalui Wi-Fi. Ini berfungsi pada TV LG dengan webOS, iaitu hampir semua TV pintar LG sejak 2014. Anda tidak perlukan akaun LG mahupun aplikasi ThinQ.',
    pasos=[
      'Hidupkan TV dengan butang di bawah logo LG atau dengan butang di bahagian belakang. Pada banyak model ia ialah kayu bedik: tekannya untuk membuka menu dan gerakkannya untuk memilih.',
      'Sambungkan telefon anda ke Wi-Fi yang sama dengan TV.',
      'Buka Mando TV dan ketik TV LG anda dalam senarai.',
      'TV memaparkan pertanyaan yang meminta kebenaran. Sahkannya dengan kayu bedik atau butang pada TV. Jika telefon ini pernah disambungkan, TV tidak bertanya lagi.',
      'Siap. Anak panah, OK, Kembali, Utama, volum, saluran dan papan kekunci adalah percuma. Penuding ialah ciri Pro.',
      'Dengan aplikasi bersambung, buka tetapan dengan anak panah dan OK, kemudian aktifkan "Hidupkan TV dengan peranti mudah alih". Panduan [Hidupkan TV LG dengan telefon](@lg-on) menunjukkan di mana pilihan itu berada.',
    ],
    extra=[
      ('Jika TV tidak memaparkan pertanyaan', 'Mungkin kebenaran sudah disimpan atau telefon anda berada dalam rangkaian lain. Semak sama ada kedua-duanya berada dalam Wi-Fi yang sama dan VPN dimatikan. Jika TV tidak muncul dalam senarai, [Telefon anda tidak jumpa TV](@not-found) boleh membantu.'),
      ('Jika TV kehilangan Wi-Fi', 'Sambungkan TV ke penghala dengan kabel rangkaian dan ia akan menggunakannya sendiri. Atau sediakan Wi-Fi dengan nama dan kata laluan yang sama seperti dahulu, kerana TV biasanya menyambung sendiri.'),
      ('Jika TV tersangkut pada input lain', 'Pada telefon anda, ketik Input dan pilih port HDMI. Maklumat lanjut ada dalam [Tukar input HDMI pada TV tanpa alat kawalan jauh](@hdmi).'),
    ],
    marca='lg',
    faq=[
      ('Adakah saya perlukan Magic Remote untuk menggunakan Mando TV?', 'Anda hanya memerlukan sesuatu kali pertama untuk mengesahkan pertanyaan, dan butang atau kayu bedik pada TV itu sendiri sudah mencukupi. Selepas itu anda hanya menggunakan telefon.'),
      ('Adakah saya perlukan aplikasi LG ThinQ?', 'Tidak. Mando TV menyambung terus melalui Wi-Fi anda dan tidak meminta akaun LG.'),
      ('Bolehkah saya mematikan dan menghidupkan TV LG dengan telefon?', 'Mematikan, ya. Untuk menghidupkan, anda mesti telah mengaktifkan "Hidupkan TV dengan peranti mudah alih" pada TV dan menyambung sekali semasa TV dihidupkan.'),
    ]),
  dict(clave='hdmi', corto='Tukar HDMI tanpa alat kawalan jauh',
    titulo='Tukar Input HDMI Tanpa Alat Kawalan Jauh (Samsung, LG, Roku)',
    desc='Tukar input HDMI tanpa alat kawalan jauh pada Samsung, LG atau Roku: dengan butang pada TV atau dengan telefon. Percuma untuk bermula, tanpa iklan.',
    h1='Cara menukar input HDMI pada TV tanpa alat kawalan jauh',
    intro='Konsol atau pemain penstriman sudah sedia, tetapi TV tersangkut pada input lain dan alat kawalan jauh entah di mana. Untuk menukar input HDMI tanpa alat kawalan jauh, anda ada dua pilihan: butang pada TV itu sendiri atau telefon anda. Berikut ialah langkah untuk Samsung, LG dan Roku.',
    pasos=[
      'Cuba yang paling mudah dahulu: hidupkan konsol atau pemain. Jika HDMI-CEC diaktifkan pada TV (pada Samsung dipanggil Anynet+, pada LG SIMPLINK), TV bertukar sendiri ke input itu.',
      'Jika tidak bertukar, guna butang pada TV itu sendiri, di bawah di tengah atau di belakang. Pada banyak TV Samsung dan LG ia ialah kayu bedik yang membuka menu dengan Sumber atau Input.',
      'Dalam menu itu, pilih inputnya: HDMI 1, HDMI 2 dan seterusnya. Nombor itu ialah port tempat kabel disambungkan.',
      'Jika anda lebih suka menggunakan telefon, sambungkannya ke Wi-Fi yang sama, buka Mando TV dan ketik TV anda.',
      'Pada LG dan Roku, ketik Input dan pilih port HDMI. Pada Samsung, Input menghantar butang Sumber ke TV dan anda memilih dengan anak panah dan OK.',
      'Anda juga boleh pergi ke input dengan anak panah dan OK pada skrin utama TV. Bergantung pada jenama dan tahun model, ia dipanggil Sumber, Peranti bersambung atau Input. Pada Roku TV, ia ialah jubin HDMI pada skrin utama.',
    ],
    extra=[
      ('Samsung', 'Jika menu butang pada TV tiada pilihan Sumber, buka menu skrin utama dengan telefon anda dan cari Sumber atau Peranti bersambung di sebelah kiri. Anda mengawalnya dengan anak panah dan OK dalam Mando TV, yang percuma.'),
      ('LG', 'Tekan kayu bedik pada TV dan cari Input. Dengan telefon anda, dalam Mando TV anda juga boleh membuka senarai input dan mengetik input yang anda mahu.'),
      ('Roku TV', 'Pada skrin utama terdapat satu jubin untuk setiap input, contohnya HDMI 1 atau HDMI 2. Bergeraklah dengan anak panah dan buka dengan OK, percuma.'),
      ('Jika ia TV dengan Android TV atau Google TV', 'Dalam Mando TV belum ada senarai input untuk Android TV. Guna butang input pada TV itu sendiri atau capai input dengan anak panah dan OK dari skrin utama. Jika anda tiada alat kawalan jauh dan mahu bersambung, baca [Android TV tanpa alat kawalan jauh](@androidtv).'),
      ('Bantuan lanjut', 'Jika TV langsung tidak dapat dihidupkan atau anda tidak tahu bermula dari mana, baca [Alat kawalan jauh hilang](@lost-tv). Untuk bermain dengan konsol, panduan [Hidupkan TV dan tukar ke HDMI konsol tanpa alat kawalan jauh](@console) mengandungi helah HDMI-CEC.'),
    ],
    marca=None,
    faq=[
      ('Adakah menukar input HDMI percuma?', 'Ya. Senarai input dalam Mando TV adalah percuma, sama seperti menghidupkan TV dan anak panah, OK serta volum. Anda juga boleh mencapai input melalui menu TV.'),
      ('Bagaimana saya tahu input HDMI mana yang saya perlukan?', 'Lihat port HDMI pada TV: setiap satu ada nombor. Pilih yang disambungkan dengan kabel konsol atau pemain anda.'),
      ('Bagaimana jika TV tidak dapat dihidupkan?', 'Hidupkannya dengan butang pada TV itu sendiri. Jika anda pernah menyambungkannya dan mengaktifkan hidupkan melalui rangkaian, anda juga boleh menghidupkannya daripada telefon.'),
    ]),
  dict(clave='androidtv', corto='Android TV tanpa alat kawalan jauh',
    titulo='Android TV Tanpa Alat Kawalan Jauh: Guna Telefon Anda',
    desc='Tiada alat kawalan jauh Android TV atau Google TV? Sambungkan telefon anda dengan kod 6 aksara pada skrin. Percuma, tanpa akaun, tanpa iklan.',
    h1='Android TV tanpa alat kawalan jauh: cara guna telefon anda',
    intro='Jika alat kawalan jauh Android TV atau Google TV anda hilang atau bateri habis, telefon anda menggantikannya. Yang terbaik: anda tidak memerlukan alat kawalan jauh untuk bersambung, kerana TV memaparkan kod pada skrin dan anda menaipnya pada telefon. Ia berfungsi pada TV Sony, Philips, TCL, Hisense, Sharp dan Xiaomi dengan Android TV, pada Chromecast dengan Google TV dan pada Nvidia Shield.',
    pasos=[
      'Hidupkan TV dengan butang pada TV itu sendiri. Hampir selalu ia terletak di bawah di tengah atau di belakang berhampiran satu sudut.',
      'Sambungkan telefon anda ke Wi-Fi yang sama dengan TV.',
      'Muat turun Mando TV, yang percuma dan tidak meminta akaun Google, dan buka aplikasi. Ketik TV anda dalam senarai.',
      'TV memaparkan kod 6 huruf dan nombor. Taipkannya pada telefon anda dan ketik Pasangkan. Anda tidak memerlukan alat kawalan jauh untuk ini.',
      'Sekarang anda boleh menggunakan anak panah, OK, Kembali, Utama, volum, senyap dan papan kekunci. Ia percuma, begitu juga senarai apl. Pad sentuh ialah Pro.',
      'Untuk menghidupkan TV daripada telefon lain kali, dalam tetapan rangkaian atau kuasa cari "Wake on LAN", "Hidupkan melalui rangkaian", "Network standby" atau "Remote start".',
    ],
    extra=[
      ('Jika TV anda tidak boleh dihidupkan daripada telefon', 'Bukan semua Android TV boleh dihidupkan melalui rangkaian; ia bergantung pada pengeluar dan model. Jika TV anda tiada ciri itu, hidupkannya dengan butang pada TV dan teruskan dengan telefon. Anda boleh mematikannya daripada aplikasi.'),
      ('Chromecast dengan Google TV, Google TV Streamer dan Shield', 'Ia disambungkan dengan cara yang sama: Wi-Fi yang sama, ketik peranti dalam senarai dan masukkan kod. Jika TV memaparkan input lain, tukarkannya ke port HDMI tempat peranti disambungkan, seperti dijelaskan dalam [Tukar input HDMI pada TV tanpa alat kawalan jauh](@hdmi).'),
      ('Jika kod tidak muncul atau dilaporkan salah', 'Semak sama ada TV benar-benar dihidupkan dan bukan dalam mod siap sedia. Kod berubah setiap kali diminta: hanya yang terakhir berfungsi. Anda boleh dapatkan butiran lanjut di [Android TV meminta kod pasangan](@androidtv-code).'),
      ('Aplikasi Google atau Mando TV', 'Google mempunyai aplikasinya sendiri yang memerlukan akaun Google. Mando TV tidak meminta akaun, turut berfungsi pada Windows dan mengawal TV LG, Samsung dan Roku dengan aplikasi yang sama.'),
    ],
    marca='android',
    faq=[
      ('Adakah saya perlukan alat kawalan jauh untuk memasangkan telefon saya?', 'Tidak. Kod muncul pada skrin TV dan anda menaipnya pada telefon. Anda hanya perlu menghidupkan TV, dengan butang pada TV jika perlu.'),
      ('Adakah ia berfungsi dengan Hisense?', 'Pada TV Hisense dengan Android TV atau Google TV, ya. TV Hisense dengan sistem lain tidak serasi.'),
      ('Bolehkah saya menaip dengan papan kekunci telefon saya?', 'Ya. Papan kekunci adalah percuma dan berfungsi untuk carian dalam YouTube, Netflix dan apl lain.'),
    ]),
  dict(clave='lg-on', corto='Hidupkan TV LG dengan telefon',
    titulo='Hidupkan TV LG dengan Telefon (Panduan)',
    desc='Hidupkan TV LG dengan telefon melalui Wi-Fi: aktifkan "Hidupkan TV dengan peranti mudah alih" dan guna Mando TV. Langkah demi langkah, percuma.',
    h1='Cara menghidupkan TV LG dengan telefon',
    intro='Anda boleh menghidupkan TV LG dengan telefon, tetapi anda perlu mengaktifkan satu tetapan pada TV terlebih dahulu. Selepas itu, telefon anda menghidupkan TV LG melalui Wi-Fi, tanpa alat kawalan jauh. Ia mengambil lima minit dan anda hanya perlu melakukannya sekali.',
    pasos=[
      'Sambungkan telefon dan TV LG ke Wi-Fi yang sama.',
      'Pada TV, buka Tetapan dan cari "Hidupkan TV dengan peranti mudah alih". Ia berada di bawah Tetapan, Umum, Peranti, Peranti Luaran (pada model lama di Sambungan, Pengurusan Sambungan Mudah Alih).',
      'Aktifkan "Hidupkan melalui Wi-Fi". Jika TV anda disambungkan dengan kabel rangkaian, aktifkan pilihan untuk kabel sebaliknya.',
      'Jika TV anda ada "Quick Start+", aktifkan juga.',
      'Dengan TV dihidupkan, buka Mando TV pada telefon anda dan ketik TV LG anda dalam senarai. Sahkan pertanyaan yang muncul pada skrin. Dengan cara ini aplikasi belajar untuk membangunkannya.',
      'Matikan TV dan cuba: dalam Mando TV, ketik TV, dan aplikasi bertanya sama ada anda mahu menghidupkannya.',
    ],
    extra=[
      ('Jika ia tidak hidup', 'TV mesti berada dalam Wi-Fi yang sama semasa ia dimatikan. Semak sama ada tetapan masih aktif dan telefon anda berada dalam rangkaian yang sama. Jika anda menukar penghala, sambung semula semasa TV dihidupkan.'),
    ],
    marca='lg',
    faq=[
      ('Bolehkah saya menghidupkan TV LG dengan telefon jika belum pernah menyambungkannya?', 'Tidak. Mula-mula anda perlu mengaktifkan "Hidupkan TV dengan peranti mudah alih" pada TV dan menyambung sekali dengan Mando TV semasa TV dihidupkan.'),
      ('Adakah saya perlukan aplikasi LG ThinQ?', 'Tidak. Mando TV menyambung terus melalui Wi-Fi anda dan tidak meminta akaun LG.'),
      ('Adakah ia berfungsi dengan data mudah alih?', 'Tidak. Telefon dan TV mesti berada dalam Wi-Fi yang sama.'),
    ]),
  dict(clave='console', corto='TV dan konsol tanpa alat kawalan jauh',
    titulo='Tiada Alat Kawalan Jauh? Hidupkan TV, Tukar HDMI',
    desc='Hari pelancaran dan tiada alat kawalan jauh? Hidupkan TV dan tukar ke input HDMI PS5 atau Xbox anda dengan telefon. Percuma, tanpa iklan.',
    h1='Cara menghidupkan TV dan menukar ke input HDMI konsol anda tanpa alat kawalan jauh',
    intro='Hari pelancaran GTA VI, konsol sudah sedia dan alat kawalan jauh hilang entah di mana di celah kusyen sofa. Ini lebih kerap berlaku daripada yang disangka. Dengan Mando TV, telefon anda menghidupkan TV dan menukar ke input PlayStation atau Xbox anda melalui Wi-Fi di rumah.',
    pasos=[
      'Sambungkan telefon anda ke Wi-Fi yang sama dengan TV.',
      'Buka Mando TV dan ketik TV anda dalam senarai (Samsung, LG, Roku atau Android TV).',
      'Jika TV dimatikan, ketik Hidupkan. Ini berfungsi jika hidupkan melalui rangkaian diaktifkan pada TV. Jika anda tidak pernah mengaktifkannya, hidupkan TV dengan butang pada TV kali ini sahaja dan aktifkannya untuk lain kali.',
      'Hidupkan konsol. Jika HDMI-CEC diaktifkan (lihat helah percuma di bawah), TV bertukar sendiri ke inputnya.',
      'Jika tidak bertukar, dalam Mando TV ketik Input dan pilih port HDMI tempat konsol disambungkan: HDMI 1, HDMI 2 dan seterusnya.',
      'Untuk volum semasa bermain, guna butang besar dalam aplikasi.',
    ],
    extra=[
      ('Helah percuma: biarkan konsol menukar TV', 'PS5 dan Xbox boleh menghidupkan TV dan terus melompat ke input HDMI mereka semasa dihidupkan, berkat HDMI-CEC. Pada PS5, ia terdapat di Tetapan > Sistem > HDMI > Dayakan Pautan Peranti HDMI. Pada Xbox, buka Tetapan > Umum > Pilihan TV dan paparan dan cari pilihan kawalan peranti. Pada TV, ciri ini dinamakan berbeza mengikut jenama: Anynet+ pada Samsung, SIMPLINK pada LG dan BRAVIA Sync atau Kawalan HDMI pada yang lain.'),
      ('Jika TV kekal pada gambar lain', 'Jika konsol dihidupkan tetapi TV masih memaparkan antena atau sesuatu apl, TV tidak menukar input. Pada telefon anda, ketik Input dan pilih input HDMI konsol. Atau guna anak panah dan OK untuk sampai ke input TV, atau butang pada TV itu sendiri, dan pilih port HDMI. Nombor itu ialah port tempat anda memasang kabel konsol.'),
      ('Jika ia Roku TV', 'Butang pada TV, biasanya di bawah di tengah atau di belakang, menghidupkannya. Selepas itu telefon anda menguruskan selebihnya.'),
    ],
    marca=None,
    faq=[
      ('Adakah Mando TV ada kaitan dengan GTA VI?', 'Tidak. Mando TV tidak berkaitan dengan Rockstar Games atau Take-Two. Aplikasi ini hanya membantu anda supaya tidak kehilangan masa bermain kerana tidak menjumpai alat kawalan jauh.'),
      ('Adakah menukar input HDMI percuma?', 'Ya. Senarai input dalam Mando TV adalah percuma, sama seperti menghidupkan TV dan anak panah, OK serta volum. Anda juga boleh membiarkan konsol menukar input sendiri dengan HDMI-CEC.'),
      ('Adakah ia berfungsi dengan TV saya?', 'Ia berfungsi dengan TV Samsung, LG, Roku dan Android TV dalam Wi-Fi yang sama. Jika TV anda jenama lain, helah HDMI-CEC masih boleh membantu.'),
      ('Bolehkah saya menggunakannya untuk bermain GTA VI (GTA 6) pada PS5 atau Xbox?', 'Mando TV tidak campur tangan dalam konsol atau permainan. Ia hanya memastikan TV dihidupkan dan berada pada input HDMI yang betul supaya anda boleh duduk dan bermain.'),
    ]),
  dict(clave='samsung-lost', corto='TV Samsung tanpa alat kawalan jauh',
    titulo='Alat Kawalan Jauh Samsung Hilang? Guna Telefon Anda',
    desc='Alat kawalan jauh Samsung hilang atau rosak? Guna telefon melalui Wi-Fi sebagai alat kawalan TV Tizen. Mudah dengan Mando TV, percuma, tiada iklan.',
    h1='TV Samsung tanpa alat kawalan jauh asal: cara guna telefon anda',
    intro='Jika alat kawalan jauh Samsung anda hilang atau tidak berfungsi lagi, anda boleh menggunakan telefon sebagai alat kawalan jauh melalui Wi-Fi. Ia berfungsi pada TV Samsung dengan Tizen, model 2016 dan ke atas.',
    pasos=[
      'Hidupkan TV dengan butang pada TV itu sendiri. Pada kebanyakan model ia terletak di bawah atau di belakang, kadangkala sebagai kayu bedik kecil.',
      'Semak sama ada TV bersambung ke Wi-Fi anda dan telefon anda berada dalam rangkaian yang sama.',
      'Buka Mando TV pada telefon anda. TV Samsung anda muncul sendiri dalam senarai. Ketik padanya.',
      'TV meminta anda mengesahkan sambungan. Pada kebanyakan model, anda mengesahkannya dengan butang pada TV atau dengan kayu bedik di bahagian belakang.',
      'Siap, sekarang anda boleh menggunakan telefon sebagai alat kawalan jauh. Butang, papan kekunci dan apl adalah percuma; pad sentuh ialah ciri Pro.',
      'Untuk menghidupkan TV daripada telefon lain kali, pergi ke Tetapan > Umum > Rangkaian > Tetapan Pakar dan aktifkan "Hidupkan dengan mudah alih".',
    ],
    extra=[
      ('Jika TV tidak meminta kebenaran', 'Mungkin kebenaran sudah disimpan atau TV berada dalam Wi-Fi lain. Tutup Mando TV dan buka aplikasi sekali lagi dengan TV dihidupkan. Jika TV lebih lama daripada 2016, ia menggunakan sistem lain yang belum disokong.'),
      ('Jika anda tertolak kebenaran secara tidak sengaja', 'Pada TV, pergi ke Tetapan > Umum > Pengurus Peranti Luaran > Pengurus Sambungan Peranti dan tetapkan Mando TV kepada dibenarkan. Jika telefon anda masih tidak menjumpai TV, baca [Telefon anda tidak jumpa TV](@not-found).'),
    ],
    marca='samsung',
    faq=[
      ('Bagaimana saya mengesahkan sambungan jika saya tiada alat kawalan jauh?', 'Pada kebanyakan model, anda mengesahkannya dengan butang pada TV atau dengan kayu bedik di bahagian belakang. Jika model anda tiada butang, tulis kepada hola@mandotv.app dan kami akan membantu anda.'),
      ('Adakah Mando TV meminta akaun Samsung?', 'Tidak. Sambungan berlaku terus melalui Wi-Fi anda, tanpa akaun Samsung.'),
      ('Adakah ia berfungsi dengan TV Samsung saya yang lebih lama?', 'Ia berfungsi dengan TV Samsung dengan Tizen, model 2016 dan ke atas.'),
    ]),
  dict(clave='wifi', corto='Telefon sebagai alat kawalan jauh melalui Wi-Fi',
    titulo='Guna Telefon sebagai Alat Kawalan Jauh: Kawal TV melalui Wi-Fi',
    desc='Sambungkan telefon ke TV melalui Wi-Fi dan guna sebagai alat kawalan untuk Samsung, LG, Roku, Google TV. Langkah ikut jenama dengan Mando TV. Percuma.',
    h1='Cara menyambungkan telefon anda ke TV melalui Wi-Fi sebagai alat kawalan jauh',
    intro='Anda hanya memerlukan telefon dan TV dalam Wi-Fi yang sama serta aplikasi alat kawalan jauh. Mando TV menjumpai TV anda sendiri dan berfungsi dengan Samsung, LG, Roku, Google TV dan Android TV.',
    pasos=[
      'Sambungkan telefon dan TV ke Wi-Fi yang sama.',
      'Buka Mando TV. TV anda muncul sendiri dalam senarai. Ketik padanya.',
      'Sahkan sambungan untuk jenama anda (butirannya ada di bawah).',
      'Kawal TV dengan butang atau dengan papan kekunci telefon anda. Pad sentuh ialah ciri Pro.',
    ],
    extra=[
      ('Samsung', 'TV bertanya sama ada anda membenarkan sambungan. Sahkannya pada skrin kali pertama. Ia berfungsi dengan Tizen, model 2016 dan ke atas. Untuk menghidupkannya daripada telefon, di bawah Tetapan > Umum > Rangkaian > Tetapan Pakar, aktifkan "Hidupkan dengan mudah alih".'),
      ('LG', 'TV memaparkan pertanyaan yang meminta kebenaran. Sahkannya kali pertama. Untuk menghidupkannya daripada telefon, dalam tetapan cari "Hidupkan TV dengan peranti mudah alih" dan aktifkan "Hidupkan melalui Wi-Fi".'),
      ('Roku', 'Roku tidak memerlukan pemasangan: ketik padanya dalam senarai dan anda sudah bersambung. Untuk menghidupkannya, di bawah Tetapan > Sistem > Kuasa, aktifkan "Permulaan pantas TV".'),
      ('Google TV dan Android TV', 'TV memaparkan kod pada skrin. Masukkannya dalam Mando TV kali pertama. Untuk menghidupkannya, dalam tetapan cari "Wake on LAN", "Hidupkan melalui rangkaian" atau "Network standby".'),
    ],
    marca=None,
    faq=[
      ('Adakah saya perlukan internet untuk menggunakan telefon sebagai alat kawalan jauh?', 'Anda hanya memerlukan telefon dan TV dalam Wi-Fi yang sama. Mando TV menyambung terus ke TV anda melalui rangkaian itu.'),
      ('Mengapa TV saya tidak muncul dalam senarai?', 'Semak sama ada TV dihidupkan dan telefon anda tidak menggunakan data mudah alih atau Wi-Fi lain. Sesetengah penghala mempunyai rangkaian tetamu yang mengasingkan peranti antara satu sama lain.'),
      ('Bolehkah saya menggunakan Mando TV pada iPhone atau telefon Android?', 'Pada iPhone dan iPad, ya: aplikasi sudah ada di App Store. Untuk Windows, ia juga ada di Microsoft Store. Android akan menyusul tidak lama lagi: anda boleh menyertai akses awal percuma di Google Play.'),
    ]),
  dict(clave='pc', corto='Kawal TV dengan PC',
    titulo='Kawal TV dengan PC Windows (Percuma)',
    desc='Guna PC Windows sebagai alat kawalan untuk Samsung, LG, Roku atau Google TV melalui Wi-Fi. Butang, papan kekunci, apl percuma; pintasan PC dengan Pro.',
    h1='Cara mengawal TV anda dengan PC Windows',
    intro='Jika anda menghabiskan hari di hadapan komputer, anda tidak perlu mencari alat kawalan jauh: Mando TV untuk Windows mengawal TV Samsung, LG, Roku, Google TV atau Android TV anda melalui Wi-Fi di rumah. Berguna untuk menukar apl, menguatkan bunyi atau menaip dalam YouTube dengan papan kekunci PC.',
    pasos=[
      'Muat turun Mando TV percuma daripada Microsoft Store ke komputer anda dengan Windows 10 atau 11.',
      'Semak sama ada komputer dan TV berada dalam rangkaian yang sama (Wi-Fi atau kabel, tetapi melalui penghala yang sama).',
      'Buka Mando TV: TV anda muncul sendiri dalam senarai. Ketik atau klik padanya.',
      'Kali pertama, sahkan sambungan pada skrin TV (pada Google TV dan Android TV, masukkan kod yang dipaparkan oleh TV).',
      'Siap: guna butang atau papan kekunci untuk menaip dalam kotak carian TV. Pad sentuh ialah ciri Pro.',
    ],
    extra=[
      ('Pintasan papan kekunci pada PC (Pro)', 'Dengan Mando TV Pro, anda mengawal TV dengan papan kekunci komputer: kekunci anak panah untuk menavigasi, Enter untuk OK, Backspace atau Esc untuk Kembali, + dan - untuk volum, M untuk senyap dan bar ruang untuk jeda.'),
      ('Alat kawalan jauh mini sentiasa di atas (Pro)', 'Kekalkan tetingkap kecil dengan alat kawalan jauh sentiasa kelihatan semasa anda bekerja atau bermain pada PC.'),
      ('Bercakap dengan TV daripada PC (Pro)', 'Dengan Mando TV Pro, anda memberi arahan kepada TV melalui mikrofon PC: "buka YouTube", "kuatkan bunyi" atau "matikan dalam 30 minit", seperti cara anda bercakap. Pada Windows, suara dikenali pada PC itu sendiri: anda tidak memerlukan internet, tidak perlu mengubah apa-apa dalam tetapan Windows, dan ia berfungsi dalam 6 bahasa aplikasi. Apa yang anda katakan tidak keluar dari PC dan tidak disimpan. Hanya pada pemproses yang sangat lama, aplikasi beralih kepada pendiktean Windows. Untuk itu, pengecaman pertuturan dalam talian mesti dihidupkan dalam tetapan privasi dan Bahasa Melayu (Malaysia) mesti ditambah dalam Windows. Jika ada yang tiada, aplikasi memberitahu anda dan membuka tetapan dengan satu butang.'),
    ],
    marca=None,
    faq=[
      ('Adakah saya perlukan kabel atau Bluetooth untuk mengawal TV dengan PC?', 'Tidak. Mando TV menyambung melalui rangkaian rumah anda: PC dan TV hanya perlu berada pada penghala yang sama.'),
      ('Adakah ia berfungsi dengan mana-mana TV?', 'Ia berfungsi dengan TV Samsung dengan Tizen (model 2016 dan ke atas), LG dengan webOS, Roku serta Google TV atau Android TV (Sony, Philips, TCL, Hisense, Sharp, Xiaomi, Toshiba, Panasonic, Haier, Skyworth dan lain-lain).'),
      ('Berapakah kosnya?', 'Butang, papan kekunci dan hidupkan melalui rangkaian adalah percuma dan tanpa iklan. Mando TV Pro ialah pembelian sekali sahaja tanpa langganan untuk tambahan seperti pad sentuh, pintasan papan kekunci PC dan alat kawalan jauh mini.'),
      ('Mengapa mikrofon tidak memahami saya pada Windows?', 'Semak sama ada ciri suara aktif (ia tergolong dalam Pro) dan sama ada mikrofon PC berfungsi dalam Windows. Pada hampir semua PC, suara dikenali pada peranti itu sendiri, tanpa internet. Hanya pada pemproses yang sangat lama, aplikasi menggunakan pendiktean Windows. Dalam kes itu, semak sama ada pengecaman pertuturan dalam talian dihidupkan dalam tetapan privasi Windows dan Windows ada Bahasa Melayu (Malaysia) dalam tetapan bahasa. Mando TV hanya menggunakan bahasa itu semasa ia mendengar.'),
    ]),
  dict(clave='roku-403', corto='Aplikasi Roku tidak berfungsi',
    titulo='Aplikasi Roku Tidak Berfungsi? Betulkan Ralat 403',
    desc='Telefon bersambung tetapi Roku tidak bertindak balas? Aktifkan "Kawalan oleh aplikasi mudah alih" dalam 5 langkah dan guna telefon sebagai kawalan.',
    h1='Aplikasi Roku tidak berfungsi: cara membetulkannya',
    intro='Jika telefon anda menjumpai Roku dan bersambung, tetapi tiada butang yang berfungsi, hampir selalu puncanya ialah satu tetapan pada Roku itu sendiri yang menyekat aplikasi alat kawalan jauh. Versi Roku yang lebih baharu lebih terhad secara lalai. Dalam menu Roku, ia boleh dibetulkan dalam seminit.',
    pasos=[
      'Pada Roku, tekan Utama dan pergi ke Tetapan.',
      'Buka Sistem dan kemudian Tetapan sistem lanjutan.',
      'Pergi ke "Kawalan oleh aplikasi mudah alih". Pada sesetengah model ia dipanggil "Kawalan luaran".',
      'Di bawah "Akses rangkaian", pilih Lalai atau Permissive. Jika model anda hanya ada suis, biarkan ia pada Dibenarkan.',
      'Kembali ke Mando TV pada telefon anda dan ketik Roku anda. Butang kini bertindak balas.',
    ],
    extra=[
      ('Cara mengetahui sama ada ini masalah anda', 'Tandanya jelas: telefon anda melihat Roku dalam senarai dan bersambung, tetapi tiada apa-apa berlaku apabila anda mengetik butang. Secara dalaman, Roku membalas dengan ralat 403, yang bermaksud "dilarang". Mando TV mengesan ini semasa menyambung dan menunjukkan langkah-langkah ini pada skrin.'),
      ('Lalai atau Permissive, mana yang perlu saya pilih?', 'Lalai sudah memadai: ia menerima arahan daripada rangkaian rumah anda, dan itulah yang diperlukan oleh alat kawalan jauh. Permissive lebih terbuka dan hanya diperlukan pada rangkaian yang luar biasa. Jika pilihan ditetapkan kepada Dilumpuhkan (pada perisian yang lebih baharu, Terhad), Roku tidak bertindak balas kepada aplikasi.'),
      ('Jika anda tiada alat kawalan jauh Roku', 'Jika tetapan itu berada pada Dilumpuhkan, ia hanya boleh diubah dengan alat kawalan jauh Roku yang sebenar. Pinjam satu untuk mengubahnya sekali; selepas itu anda boleh melakukan segala-galanya dengan telefon. Baca juga [Alat kawalan jauh Roku hilang](@roku-lost).'),
    ],
    marca='roku',
    faq=[
      ('Mengapa Roku saya tidak bertindak balas lagi walaupun dahulu berfungsi?', 'Kemas kini Roku boleh menghadkan tetapan ini dengan lebih ketat. Ini bukan salah telefon atau Wi-Fi anda: anda hanya perlu membenarkan kawalan oleh aplikasi semula.'),
      ('Adakah ini terpakai untuk Roku TV dan pemain Roku?', 'Ya. Tetapan itu berada dalam menu yang sama pada pemain Roku dan pada peranti Roku TV.'),
      ('Adakah selamat membiarkan tetapan pada Lalai?', 'Ya. Ia hanya menerima arahan daripada peranti dalam rangkaian rumah anda.'),
    ]),
  dict(clave='not-found', corto='Telefon tidak jumpa TV',
    titulo='Telefon Tidak Jumpa TV? 6 Perkara untuk Disemak',
    desc='Aplikasi alat kawalan jauh tidak jumpa TV anda? Semak Wi-Fi, VPN dan akses rangkaian setempat. Untuk Samsung, LG, Roku dan Android TV.',
    h1='Telefon anda tidak jumpa TV: perkara yang perlu disemak',
    intro='Anda membuka aplikasi alat kawalan jauh dan senarai kosong, atau TV muncul tetapi sambungan terputus. Hampir selalu puncanya ialah rangkaian dan bukan TV. Semak perkara ini mengikut urutan: yang pertama menyelesaikan kebanyakan kes.',
    pasos=[
      'Lihat dalam Wi-Fi mana telefon anda berada dan dalam Wi-Fi mana TV berada. Ia mesti rangkaian yang sama dengan nama yang sama. Rangkaian tetamu tidak berfungsi kerana ia mengasingkan peranti antara satu sama lain.',
      'Matikan VPN pada telefon anda jika anda menggunakannya. Apabila VPN aktif, telefon anda keluar ke internet melalui rangkaian lain dan tidak nampak peranti di rumah anda, atau sambungan terputus selepas beberapa saat.',
      'Matikan data mudah alih seketika. Sesetengah telefon beralih sendiri daripada Wi-Fi kepada data mudah alih apabila isyarat lemah.',
      'Hidupkan TV dan tunggu sehingga ia selesai bermula. TV yang dimatikan tidak membalas carian.',
      'Pada iPhone, semak sama ada aplikasi mempunyai kebenaran "Rangkaian Setempat": Tetapan > Privasi & Keselamatan > Rangkaian Setempat.',
      'Jika ia masih tidak muncul, tambahkannya secara manual: dalam Mando TV, ketik "Tambah melalui IP" dan masukkan alamat IP TV.',
    ],
    extra=[
      ('Biarkan aplikasi membimbing anda', 'Dalam senarai TV ada satu butang untuk kes TV anda tidak muncul. Aplikasi menyemak punca yang paling kerap langkah demi langkah (Wi-Fi yang sama, VPN, kebenaran rangkaian setempat dan lain-lain) dan selepas setiap pembetulan menunjukkan butang untuk menyemak semula. Pembantu ini percuma.'),
      ('Di mana mencari alamat IP TV', 'Ia ada dalam menu rangkaian TV dan sedikit berbeza mengikut model. Pada LG: Tetapan, Rangkaian, Sambungan Wi-Fi, Tetapan Wi-Fi lanjutan. Pada Samsung: Tetapan, Umum, Rangkaian, Status rangkaian, Tetapan IP. Pada Roku: Tetapan, Rangkaian, Perihal. Pada Android TV dan Google TV: Tetapan, Rangkaian & Internet, kemudian ketik rangkaian anda. Ia ialah nombor seperti 192.168.1.86.'),
      ('Jika ia muncul tetapi sambungan terputus', 'Jika sambungan terputus selepas beberapa saat, puncanya biasanya pada telefon: VPN, bertukar ke Wi-Fi lain atau mod jimat bateri. Matikan VPN, kekal dalam Wi-Fi yang sama dan cuba semula.'),
      ('Wi-Fi 2.4 dan 5 GHz', 'Tidak mengapa jika telefon anda berada pada rangkaian 5 GHz dan TV pada rangkaian 2.4 GHz, selagi kedua-duanya datang daripada penghala yang sama. Jika anda menggunakan pengulang Wi-Fi dan TV masih tidak muncul, dekatkan telefon anda dengan penghala utama dan cuba semula.'),
    ],
    marca=None,
    faq=[
      ('Bolehkah saya mengawal TV dengan data mudah alih?', 'Tidak. Isyarat alat kawalan jauh melalui Wi-Fi di rumah anda, jadi telefon dan TV mesti berada dalam rangkaian yang sama.'),
      ('Mengapa ia tidak berfungsi apabila VPN aktif?', 'Kerana VPN menghantar semua trafik telefon anda melalui rangkaian lain dan telefon tidak lagi nampak peranti di rumah anda. Matikannya selagi anda menggunakan alat kawalan jauh.'),
      ('Adakah ia berfungsi dengan Bluetooth atau inframerah?', 'Untuk TV pintar, Mando TV menggunakan Wi-Fi. Inframerah hanya berfungsi pada telefon Android yang ada pemancar inframerah dan ditujukan untuk TV yang bukan TV pintar. Bluetooth ada dalam beta, percuma dan hanya dari Android 9: telefon menyambung ke TV sebagai papan kekunci dan alat kawalan jauh Bluetooth, tanpa memerlukan Wi-Fi. Ia berfungsi dengan Google TV, Android TV dan Fire TV; pada jenama lain yang menerima papan kekunci Bluetooth ia mungkin berfungsi, Roku tidak menerimanya.'),
    ]),
  dict(clave='androidtv-code', corto='Kod pasangan Android TV',
    titulo='Android TV Meminta Kod Pasangan: Apa yang Perlu Dibuat',
    desc='Android TV atau Google TV anda memaparkan kod 6 aksara semasa menyambung. Cara memasukkannya dan apa yang perlu dibuat jika kod tidak muncul atau salah.',
    h1='Android TV meminta kod pasangan: apa yang perlu dibuat',
    intro='Apabila anda menyambungkan telefon ke Android TV atau Google TV buat kali pertama, TV memaparkan kod 6 aksara pada skrin. Ini biasa dan hanya berlaku sekali: dengan cara ini tiada orang lain boleh mengawal TV anda. Berikut ialah cara memasukkannya dan apa yang perlu dibuat jika ia tidak muncul.',
    pasos=[
      'Hidupkan TV dan biarkan skrin utama kelihatan.',
      'Buka Mando TV pada telefon anda, dalam Wi-Fi yang sama dengan TV, dan ketik TV anda dalam senarai.',
      'Lihat skrin TV: kod 6 huruf dan nombor akan muncul.',
      'Taipkannya pada telefon anda tepat seperti yang dipaparkan dan ketik Pasangkan. Huruf hanya dari A hingga F, jadi aksara bulat sentiasa ialah nombor sifar.',
      'Siap. TV mengingati telefon anda dan tidak meminta kod lagi.',
    ],
    extra=[
      ('Jika kod tidak muncul pada TV', 'Semak sama ada TV benar-benar dihidupkan dan bukan dalam mod siap sedia, dan sama ada telefon anda berada dalam Wi-Fi yang sama. Ketik TV sekali lagi pada telefon anda. Jika ia masih tidak muncul, mulakan semula TV: cabut palamnya selama sepuluh saat, pasang semula dan cuba lagi.'),
      ('Jika kod dilaporkan salah', 'Kod berubah setiap kali diminta. Jika anda mengambil masa yang lama atau memintanya dua kali, hanya yang terakhir pada skrin berfungsi. Ketik TV sekali lagi pada telefon anda dan masukkan kod baharu.'),
      ('Jika TV meminta kod itu sekali lagi', 'Ini berlaku jika TV ditetapkan semula ke tetapan kilang atau anda memadam data aplikasi pada telefon anda. Pasangkan semula dan ia akan disimpan. Jika anda langsung tiada alat kawalan jauh, baca [Android TV tanpa alat kawalan jauh](@androidtv).'),
    ],
    marca='android',
    faq=[
      ('TV yang mana menggunakan kod ini?', 'Yang menggunakan Android TV atau Google TV: Sony, Philips, TCL, Hisense, Sharp, Xiaomi, Chromecast dengan Google TV dan beberapa lagi.'),
      ('Adakah saya perlukan akaun Google pada telefon saya?', 'Tidak. Kod pada skrin ialah semua yang anda perlukan.'),
      ('Adakah ini selamat?', 'Ya. Kod itu membuktikan anda berada di hadapan TV: tiada orang boleh memasangkan tanpa melihat kod pada skrin.'),
    ]),
  dict(clave='roku-lost', corto='Alat kawalan jauh Roku hilang',
    titulo='Alat Kawalan Jauh Roku Hilang? Guna Telefon Anda Melalui Wi-Fi',
    desc='Alat kawalan jauh Roku hilang? Telefon anda menggantikannya melalui Wi-Fi. Langkah mudah, termasuk jika anda menukar penghala dan Roku tiada Wi-Fi.',
    h1='Alat kawalan jauh Roku hilang: cara guna telefon anda',
    intro='Jika alat kawalan jauh Roku anda hilang atau tidak berfungsi lagi, telefon anda menggantikannya selagi Roku masih bersambung ke Wi-Fi anda. Dan jika anda menukar Wi-Fi atau penghala, ada juga jalan keluarnya.',
    pasos=[
      'Mula-mula cuba bunyikan alat kawalan jauh. Jika alat kawalan jauh Roku anda mempunyai pembesar suara, contohnya Roku Voice Remote Pro, buka Mando TV, sambung ke Roku dan guna pilihan untuk membunyikan alat kawalan jauh supaya anda dapat mencarinya. Ini hanya berfungsi dengan alat kawalan jauh Roku yang ada pembesar suara, dan Roku mesti dihidupkan.',
      'Hidupkan TV dan biarkan Roku disambungkan. Anda tidak perlu menyentuhnya.',
      'Sambungkan telefon anda ke Wi-Fi yang sama dengan yang digunakan Roku.',
      'Buka Mando TV. Roku muncul sendiri dalam senarai. Ketik padanya.',
      'Guna anak panah, OK, Utama dan Kembali seperti pada alat kawalan jauh biasa anda. Roku tidak meminta kod.',
      'Jika butang tidak berbuat apa-apa, Roku menyekat kawalan oleh aplikasi: panduan [Aplikasi Roku tidak berfungsi](@roku-403) menerangkan cara membenarkannya.',
    ],
    extra=[
      ('Jika Roku tiada Wi-Fi (penghala ditukar atau berpindah rumah)', 'Tanpa alat kawalan jauh anda tidak boleh masuk ke menu untuk menyediakan rangkaian baharu, tetapi ada satu helah: Roku menyambung sendiri ke rangkaian yang mempunyai nama dan kata laluan yang sama seperti yang lama. Pada telefon lain, sediakan hotspot Wi-Fi dengan nama dan kata laluan yang sama, sambungkan telefon dengan Mando TV kepadanya, dan Roku akan muncul dalam senarai. Dari situ, pergi ke Tetapan, Rangkaian dan sambungkannya ke Wi-Fi baharu.'),
      ('Jika ia Roku TV', 'Peranti Roku TV mempunyai butang pada TV, hampir selalu di bawah di tengah atau di belakang, yang menghidupkan TV. Itu sudah cukup untuk menghidupkannya dan meneruskan dengan telefon.'),
      ('Jika anda lebih suka membeli alat kawalan jauh lain', 'Pastikan ia sepadan dengan model anda. Pemain Roku kecil di belakang TV memerlukan alat kawalan jauh tanpa inframerah, kerana inframerah tidak sampai kepadanya.'),
    ],
    marca='roku',
    faq=[
      ('Bolehkah telefon saya menghidupkan Roku?', 'Pemain Roku yang disambungkan sentiasa hidup. Pada Roku TV, Mando TV menghidupkannya melalui Wi-Fi jika "Permulaan pantas TV" diaktifkan di bawah Tetapan > Sistem > Kuasa.'),
      ('Bagaimana dengan volum?', 'Pada Roku TV, telefon anda menguatkan dan mengecilkan volum. Pada pemain Roku yang disambungkan melalui HDMI, ia bergantung pada TV: pada banyak TV ia berfungsi, pada yang lain tidak.'),
      ('Perlukah saya membuat akaun?', 'Tidak. Mando TV tidak meminta akaun dan turut mengawal TV Samsung, LG dan Android TV dengan aplikasi yang sama.'),
    ]),
]

SOPORTE = dict(
  titulo='Bantuan: sambung dan hidupkan TV dengan Mando TV',
  desc='Cara menyambungkan alat kawalan jauh Mando TV dengan LG, Samsung, Roku atau Android TV, menghidupkan TV daripada telefon dan menyelesaikan masalah.',
  h1='Bantuan',
  intro='Soalan yang paling kerap ditanya, mengikut urutan langkah. Jika anda tidak jumpa soalan anda, tulis kepada kami di <a href="mailto:hola@mandotv.app?subject=Bantuan%20Mando%20TV">hola@mandotv.app</a> dan kami akan membalas.',
)
SOPORTE_HTML = '''      <h2 id="encontrar">Mencari TV</h2>
      <div class="preguntas">
        <details open><summary>TV saya tidak muncul dalam senarai</summary>
          <ol>
            <li>Semak sama ada telefon dan TV anda berada dalam Wi-Fi yang sama. Jika penghala anda mempunyai rangkaian 2.4 GHz dan 5 GHz dengan nama berbeza, kadangkala keduanya tidak nampak antara satu sama lain.</li>
            <li>Pastikan TV dihidupkan.</li>
            <li>Pada iPhone, semak sama ada Mando TV mempunyai kebenaran "Rangkaian Setempat", di bawah Tetapan, Mando TV.</li>
            <li>Dalam senarai TV, ketik butang untuk kes TV anda tidak muncul: aplikasi menyemak punca yang paling kerap langkah demi langkah (Wi-Fi yang sama, VPN, kebenaran rangkaian setempat dan lain-lain) dan selepas setiap pembetulan menunjukkan butang untuk menyemak semula.</li>
            <li>Jika ia masih tidak muncul, ketik butang +, pilih jenama dan masukkan alamat IP TV. Anda boleh melihatnya dalam menu rangkaian TV (contohnya 192.168.1.50).</li>
          </ol>
        </details>
        <details><summary>Adakah ia berfungsi dengan data mudah alih atau dari luar rumah?</summary>
          <p>Tidak. Mando TV bercakap dengan TV dalam rangkaian rumah anda, jadi telefon anda mesti bersambung ke Wi-Fi itu.</p>
        </details>
      </div>

      <h2 id="conectar">Menyambung buat kali pertama</h2>
      <p>Panduan lengkap mengikut jenama: <a href="@@R_lg@@">LG</a>, <a href="@@R_samsung@@">Samsung</a>, <a href="@@R_roku@@">Roku</a> dan <a href="@@R_android@@">Android TV</a>.</p>
      <div class="preguntas">
        <details><summary>LG</summary>
          <p>Apabila anda mengetik TV, satu pertanyaan muncul pada skrin untuk meminta kebenaran. Sahkannya dengan alat kawalan jauh biasa anda. Anda hanya melakukannya sekali.</p>
        </details>
        <details><summary>Samsung</summary>
          <p>TV bertanya sama ada anda membenarkan sambungan daripada Mando TV. Pilih "Benarkan" dengan alat kawalan jauh. Jika anda tertolak secara tidak sengaja, pergi ke Tetapan > Umum > Pengurus Peranti Luaran > Pengurus Sambungan Peranti dan tukar kepada dibenarkan.</p>
        </details>
        <details><summary>Roku</summary>
          <p>Roku tidak meminta kebenaran. Jika sambungan tidak berjaya, pada Roku pergi ke Tetapan > Sistem > Tetapan sistem lanjutan > Kawalan oleh aplikasi mudah alih dan biarkan akses rangkaian pada Lalai atau Permissive (pada perisian Roku yang lebih baharu, tetapkan "Kawalan oleh aplikasi mudah alih" kepada Dibenarkan).</p>
        </details>
        <details><summary>Android TV dan Google TV</summary>
          <p>TV memaparkan kod 6 aksara. Masukkannya dalam Mando TV tepat seperti yang dipaparkan. Ia berfungsi pada Sony, Philips, TCL, Hisense, Sharp, Xiaomi, Chromecast dengan Google TV dan yang lain dengan Android TV.</p>
        </details>
      </div>

      <h2 id="encender">Menghidupkan TV daripada aplikasi</h2>
      <p>Mando TV menghidupkan TV melalui rangkaian rumah anda. Untuk itu dua perkara diperlukan: anda pernah bersambung sekurang-kurangnya sekali semasa TV dihidupkan, dan hidupkan melalui rangkaian diaktifkan pada TV. Nama tetapan berubah mengikut model; yang paling biasa ialah:</p>
      <div class="preguntas">
        <details><summary>LG</summary>
          <p>Dalam tetapan (di bawah Tetapan, Umum, Peranti, Peranti Luaran; pada model lama di Sambungan, Pengurusan Sambungan Mudah Alih), cari "Hidupkan TV dengan peranti mudah alih" dan aktifkan "Hidupkan melalui Wi-Fi". Jika ada "Quick Start+", aktifkan juga.</p>
        </details>
        <details><summary>Samsung</summary>
          <p>Aktifkan "Hidupkan dengan mudah alih" di bawah Tetapan > Umum > Rangkaian > Tetapan Pakar.</p>
        </details>
        <details><summary>Roku</summary>
          <p>Pada peranti Roku TV, aktifkan "Permulaan pantas TV" di bawah Tetapan > Sistem > Kuasa. Pemain Roku yang disambungkan ke TV tidak boleh dihidupkan dengan cara ini.</p>
        </details>
        <details><summary>Android TV dan Google TV</summary>
          <p>Ini bergantung pada pengeluar. Dalam tetapan rangkaian atau kuasa, cari "Wake on LAN", "Hidupkan melalui rangkaian", "Network standby" atau "Remote start". Sesetengah model tidak mempunyai pilihan ini.</p>
        </details>
      </div>

      <h2 id="falla">Jika ada yang tidak berfungsi</h2>
      <div class="preguntas">
        <details><summary>Sambungan terputus atau tiada tindak balas</summary>
          <ol>
            <li>Pada skrin alat kawalan jauh, ketik Sambung semula.</li>
            <li>Jika itu tidak membantu, tutup Mando TV dan buka aplikasi sekali lagi.</li>
            <li>Jika TV mendapat alamat IP lain, keluarkannya daripada senarai dan tambahkannya semula.</li>
          </ol>
        </details>
        <details><summary>Cara menghantar laporan ralat kepada kami</summary>
          <ol>
            <li>Dalam Mando TV, ketik butang Peribadikan (peluncur di bahagian atas).</li>
            <li>Ketik Salin laporan ujian.</li>
            <li>Tampalkannya dalam e-mel kepada hola@mandotv.app bersama jenama dan model TV anda.</li>
          </ol>
          <p>Laporan itu tidak mengandungi kata laluan, kod atau apa-apa yang anda taip.</p>
        </details>
        <details><summary>Saya telah membeli Pro dan ia tidak muncul</summary>
          <p>Di bawah Peribadikan, ketik Pulihkan pembelian, dengan akaun kedai aplikasi yang sama yang anda gunakan untuk membeli. Jika ia masih tidak muncul, tulis kepada kami.</p>
        </details>
      </div>

      <h2 id="guias">Panduan langkah demi langkah</h2>
      <p><a href="@@R_guias@@">Lihat semua panduan</a></p>
      <ul>
@@GUIAS@@
      </ul>

      <h2 id="contacto">Masih ada soalan?</h2>
      <p>Tulis kepada kami di <a href="mailto:hola@mandotv.app?subject=Bantuan%20Mando%20TV">hola@mandotv.app</a>. Beritahu kami jenama dan model TV anda dan pada langkah mana anda tersekat. Tulis kepada kami dalam bahasa anda. Kami membalas dalam bahasa Sepanyol atau Inggeris dan, jika anda mahu, dalam bahasa anda dengan bantuan penterjemah.</p>
'''

PRIVACIDAD = dict(
  titulo='Dasar Privasi | Mando TV',
  desc='Mando TV tidak mengumpul data peribadi: tiada akaun, tiada iklan, tiada penjejak. Aplikasi hanya bercakap dengan TV anda dalam Wi-Fi anda.',
  h1='Privasi',
  intro='Ringkasnya: Mando TV tidak mengumpul data anda. Tiada akaun, tiada iklan, tiada penjejak dan tiada pelayan kami sendiri yang menyimpan apa yang anda lakukan.',
)
PRIVACIDAD_HTML = '''      <p class="fecha">Berkuat kuasa sejak 14 November 2026. Dikemas kini kali terakhir pada 26 November 2026.</p>

      <h2>Siapa kami</h2>
      <p>Mando TV ialah aplikasi untuk mengawal TV anda daripada telefon atau komputer. Dasar ini menerangkan maklumat yang digunakan oleh aplikasi dan apa yang dilakukannya dengan maklumat itu. Jika ada soalan, tulis kepada kami di <a href="mailto:hola@mandotv.app">hola@mandotv.app</a>.</p>

      <h2>Data yang kami kumpul</h2>
      <p>Aplikasi: tiada. Aplikasi tidak menghantar maklumat tentang anda atau cara anda menggunakannya kepada kami atau kepada pihak ketiga. Ia tidak menggunakan alat analitik, pengiklanan atau penjejakan.</p>
      <p>Laman web ini: kami mengukur lawatan dengan dua cara yang diterangkan dalam bahagian <a href="#cookies">Kuki di laman web ini</a>.</p>

      <h2>Apa yang disimpan aplikasi pada peranti anda</h2>
      <p>Supaya berfungsi, aplikasi menyimpan perkara berikut hanya pada telefon atau komputer anda:</p>
      <ul>
        <li>TV yang telah anda tambah: nama, jenama, alamat IP dalam rangkaian anda dan alamat perkakasan rangkaian (MAC) yang digunakan untuk menghidupkannya.</li>
        <li>Kunci sambungan yang diberikan oleh setiap TV apabila anda mengesahkan kebenaran. Ia disimpan dengan penyulitan dalam storan selamat sistem (Keychain pada iPhone dan Mac, Keystore pada Android, storan dilindungi pada Windows).</li>
        <li>Pilihan anda: tema cerah atau gelap, warna latar belakang, getaran dan jenis alat kawalan jauh.</li>
        <li>Jika anda menggunakan ciri Pro: apl kegemaran anda, rutin anda dan carian YouTube terakhir anda (anda boleh memadamnya dalam aplikasi).</li>
      </ul>
      <p>Apabila anda memadam aplikasi, semua itu dipadam bersamanya.</p>

      <h2>Dengan siapa aplikasi bercakap</h2>
      <p>Dengan TV anda, dalam Wi-Fi di rumah anda. Untuk menjumpainya, aplikasi mencari dalam rangkaian setempat anda; sebab itu pada iPhone ia meminta kebenaran "Rangkaian Setempat". Teks yang anda taip dengan papan kekunci aplikasi terus dihantar ke TV dan tidak disimpan.</p>
      <p>Selain itu, apabila dibuka, aplikasi memuat turun satu fail awam kecil daripada laman web ini (mandotv.app/app/config.json) untuk mengetahui sama ada ada versi baharu yang patut anda pasang dan ciri mana yang tergolong dalam Mando TV Pro. Ini muat turun seperti membuka satu halaman: aplikasi tidak menghantar data anda, TV anda atau apa yang anda lakukan. Ia hanya menyatakan versi aplikasi dan sistem (contohnya Android) supaya dapat menunjukkan notis yang sesuai. Jika anda tiada internet, aplikasi terus berfungsi dengan fail yang dimuat turun kali terakhir; jika lebih daripada 30 hari berlalu tanpa fail dapat dimuat turun, aplikasi meminta anda menyambung ke internet seketika.</p>

      <p>Apabila anda menghantar foto atau video ke TV (ciri Pro), TV hanya memuat turun fail yang anda pilih, terus daripada telefon atau PC anda melalui Wi-Fi di rumah. Ia tidak melalui internet mahupun melalui kami, aplikasi tidak melihat foto anda yang lain, dan perkongsian tamat sebaik sahaja anda menutup skrin itu.</p>
      <h2>Mikrofon dan suara</h2>
      <p>Pada iPhone, Mac dan Android, carian suara menggunakan mikrofon hanya semasa anda mengetik butang bercakap. Apa yang anda katakan ditukar kepada teks oleh pengecaman pertuturan sistem anda: oleh Apple pada iPhone dan Mac dan oleh Google pada Android, masing-masing mengikut dasar privasi mereka sendiri. Pada Windows, suara dikenali pada PC anda sendiri dan tidak keluar dari peranti; hanya pada pemproses yang sangat lama aplikasi menggunakan pendiktean Windows, daripada Microsoft, mengikut dasar privasi mereka. Pada Windows, mikrofon dibuka apabila anda membuka panel suara dan ditutup apabila anda menutupnya, atau selepas 30 saat tanpa penggunaan; semasa anda tidak bercakap, tiada apa-apa dirakam atau disimpan. Mando TV tidak merakam atau menyimpan audio, dan teks yang terhasil terus dihantar ke TV anda, sama seperti apa yang anda taip dengan papan kekunci.</p>

      <h2>Rumah: peranti daripada Apple Home dan Google Home</h2>
      <p>Apabila anda membuka bahagian Rumah (dalam ujian), aplikasi meminta kebenaran untuk melihat peranti yang sudah anda ada dalam aplikasi Home Apple (HomeKit) atau dalam Google Home. Dengan kebenaran itu, ia membaca nama, bilik dan keadaannya (hidup atau mati, kecerahan, suhu atau di bahagian mana sesuatu perkakas rumah dalam programnya) untuk memaparkannya dan menghantar kepadanya apa yang anda ketik. Semuanya berlaku antara telefon anda dan sistem Apple atau Google: Mando TV tidak menyimpan senarai itu, tidak menghantarnya kepada kami atau pihak ketiga, dan tidak menggunakannya untuk pengiklanan atau analitik. Pada Android, Google Home berfungsi dengan akaun Google anda sendiri, mengikut dasar privasi Google. Anda boleh menarik balik kebenaran pada bila-bila masa: pada iPhone di Tetapan &gt; Privasi &amp; Keselamatan &gt; HomeKit, pada Android dalam tetapan akaun Google anda.</p>
      <p>Apabila anda mengetik "Bagaimana Rumah berfungsi untuk anda?", aplikasi e-mel anda terbuka dengan mesej kepada hola@mandotv.app yang mengandungi ringkasan teknikal: versi aplikasi, sistem dan berapa banyak peranti setiap jenis yang muncul serta sama ada ia bertindak balas. Ia tidak termasuk nama peranti, bilik atau rumah anda, dan mesej hanya dihantar jika anda sendiri menghantarnya.</p>

      <h2>Laporan ujian</h2>
      <p>Aplikasi mempunyai butang "Salin laporan ujian" yang membantu kami membetulkan ralat. Laporan itu kekal dalam memori aplikasi hanya semasa ia dibuka dan tidak pernah dihantar secara automatik: anda yang memutuskan sama ada untuk menyalin dan berkongsinya. Ia tidak mengandungi kunci sambungan, kod pasangan atau apa-apa yang anda taip; hanya langkah yang dilakukan oleh aplikasi, seperti mencari, menyambung dan ralat.</p>

      <h2 id="cookies">Kuki di laman web ini</h2>
      <p>Ini hanya terpakai untuk laman web mandotv.app, bukan untuk aplikasi.</p>
      <h3>Sentiasa tanpa kuki</h3>
      <p>Kami mengira lawatan secara tanpa nama dengan Cloudflare Web Analytics: berapa ramai orang melawat laman web, halaman mana yang mereka baca dan dari negara mana. Ia tidak menggunakan kuki, tidak menggunakan alamat IP anda untuk mengenal pasti anda dan tidak menjejaki apa yang anda lakukan di laman web lain.</p>
      <h3>Dengan kuki, hanya jika anda bersetuju</h3>
      <p>Jika anda mengetik "Terima" pada notis kuki, kami mengaktifkan Google Analytics (daripada Google LLC) untuk lebih memahami cara laman web digunakan: paparan halaman, tempoh lawatan, jenis peranti, bandar anggaran dan dari mana anda datang. Untuk itu ia menyimpan kuki _ga dan _ga_* sehingga 2 tahun dalam pelayar anda. Google boleh memproses data ini pada pelayan di luar Chile. Kami telah melumpuhkan ciri pengiklanan dan Google Signals, dan kami tidak menggunakan data ini untuk menunjukkan iklan kepada anda.</p>
      <p>Jika anda mengetik "Tolak" atau tidak memilih apa-apa, Google Analytics tidak dimuatkan dan tiada kuki disimpan. Anda boleh menukar keputusan anda pada bila-bila masa dengan butang "Kuki" di bahagian bawah setiap halaman; jika anda menarik balik persetujuan, kami memadam kuki ini.</p>
      <p>Pilihan anda disimpan dalam pelayar anda (storan setempat, tidak dihantar kepada sesiapa) supaya kami tidak bertanya lagi.</p>

      <h2>Pembelian</h2>
      <p>Apabila anda membeli Mando TV Pro, pembayaran diuruskan oleh kedai aplikasi (App Store, Google Play atau Microsoft Store). Kami tidak menerima atau menyimpan data kad anda. Kedai aplikasi hanya mengesahkan kepada aplikasi bahawa pembelian itu wujud.</p>

      <h2>E-mel yang anda hantar kepada kami</h2>
      <p>Apabila anda menulis kepada kami di <a href="mailto:hola@mandotv.app">hola@mandotv.app</a>, kami menggunakan alamat e-mel anda dan apa yang anda ceritakan kepada kami hanya untuk membalas anda. Kami tidak berkongsinya dan tidak menggunakannya untuk pengiklanan. Anda boleh meminta kami memadam mesej anda pada bila-bila masa.</p>

      <h2>Kanak-kanak</h2>
      <p>Aplikasi tidak mengumpul data daripada sesiapa pun, termasuk kanak-kanak.</p>

      <h2>Perubahan pada dasar ini</h2>
      <p>Jika suatu hari nanti apa yang dilakukan aplikasi dengan data anda berubah, kami akan mengemas kini halaman ini dan tarikh di atas sebelum perubahan itu sampai kepada aplikasi.</p>
'''


# >>> guías traídas del inglés (ensamblar.py)
# Adaptadas con Ollama (qwen3.6:35b) desde las guías inglesas y auditadas por Opus el 22-nov. Rutas en idiomas_sitio.py.
GUIAS += [
  dict(clave='no-sub', corto='Aplikasi alat kawalan jauh tanpa langganan', fecha='2026-11-23',
    titulo='Aplikasi Alat Kawalan Jauh TV Tanpa Langganan dan Iklan',
    desc='Bosan dengan aplikasi kawalan jauh penuh iklan atau langganan mingguan? Mando TV percuma, tanpa iklan, Pro pembelian sekali. Perbandingan jujur.',
    h1='Aplikasi alat kawalan jauh tanpa langganan dan tanpa iklan',
    intro='Banyak aplikasi alat kawalan jauh universal memaparkan iklan atau meminta langganan mingguan sebelum boleh digunakan. Mando TV memilih cara lain: alat kawalan jauh percuma, tanpa iklan dan tanpa akaun. Pro yang pilihan hanya dibeli sekali. Berikut perbandingannya, termasuk apa yang tidak dapat dilakukan oleh aplikasi ini.',
    pasos=[
      'Sebelum memasang, buka halaman kedai aplikasi dan semak pembelian dalam aplikasi. Harga mingguan atau bulanan biasanya petanda langganan.',
      'Di Google Play, semak sama ada halaman itu menyatakan "Mengandungi iklan" dan baca ulasan terbaharu yang bernilai bintang rendah: di situ selalunya terdedah dinding bayaran yang tidak dijangka.',
      'Pastikan aplikasi itu boleh mengawal TV anda melalui Wi-Fi. Mando TV berfungsi dengan Samsung (2016 ke atas), LG webOS, Roku, Google TV, Android TV dan Fire TV.',
      'Pasang Mando TV, sambungkan telefon anda ke Wi-Fi yang sama dengan TV, kemudian ketik TV anda dalam senarai.',
      'Sahkan pertanyaan pada TV atau masukkan kod yang dipaparkan. Butang, volum, apl dan papan kekunci tidak dikenakan bayaran.',
    ],
    tabla=dict(titulo='Mando TV berbanding banyak aplikasi alat kawalan jauh',
      cabeza=['', 'Mando TV', 'Banyak aplikasi berbayar iklan atau langganan'],
      filas=[
        ['Alat kawalan jauh asas', 'Percuma', 'Selalunya percuma dengan iklan atau disembunyikan di sebalik tempoh percubaan'],
        ['Iklan', 'Tiada', 'Kerap'],
        ['Langganan', 'Tiada. Pro ialah pembelian sekali sahaja yang pilihan', 'Pelan mingguan atau bulanan adalah perkara biasa'],
        ['Akaun', 'Tidak diperlukan', 'Berbeza-beza'],
        ['TV pintar melalui Wi-Fi', 'Samsung (2016 ke atas), LG webOS, Roku, Google TV, Android TV, Fire TV, Apple TV (beta)', 'Bergantung pada aplikasi'],
        ['Inframerah untuk TV lama', 'Percuma pada telefon Android yang ada pemancar inframerah (baharu)', 'Sesetengah aplikasi, hanya pada telefon yang ada pemancar inframerah'],
        ['Bluetooth', 'Beta dari Android 9, percuma', 'Bergantung pada aplikasi'],
        ['Foto dan video ke TV', 'Pro, melalui Wi-Fi (bukan pencerminan)', 'Bergantung pada aplikasi'],
        ['Telefon dan komputer', 'iPhone, iPad, Mac dan Windows, serta Android dalam akses awal', 'Berbeza-beza'],
        ['Pencerminan skrin', 'Percuma pada iPhone, iPad dan Windows dengan fungsi terbina dalam masing-masing. Pada Windows, Pro juga boleh mencerminkan skrin PC ke TV LG, Samsung, Hisense dan Android TV (beta)', 'Sesetengah aplikasi menawarkannya'],
      ],
      nota='Mando TV tidak dibandingkan dengan mana-mana aplikasi tertentu. Harga semasa ada pada halaman kedai setiap aplikasi.'),
    extra=[
      ('Apa yang tidak dilakukan oleh Mando TV', 'Pada iPhone dan iPad, ia membimbing anda ke Pencerminan Skrin di Pusat Kawalan, iaitu fungsi iPhone sendiri yang berfungsi dengan TV yang ada AirPlay. Pada Windows, ia membuka Cast (Windows + K), dan Mando TV Pro boleh menghantar skrin PC ke TV LG, Samsung, Hisense dan Android TV melalui Wi-Fi anda (beta, dengan kelewatan beberapa saat dan tanpa bunyi). Dengan Mando TV Pro, ia juga boleh menghantar foto dan video ke TV melalui Wi-Fi anda. Ia mengawal TV pintar melalui Wi-Fi rumah. TV yang bukan TV pintar boleh dikawal dengan inframerah daripada telefon Android yang ada pemancar inframerah. Dari Android 9, telefon juga boleh menyambung melalui Bluetooth sebagai papan kekunci dan alat kawalan jauh ke Google TV, Android TV dan Fire TV, tanpa Wi-Fi sama sekali. Pilihan ini dalam beta dan percuma.'),
      ('Bagaimana Mando TV menjana pendapatan', 'Bukan dengan iklan dan bukan dengan data anda: aplikasi ini tidak mengumpulnya. Mando TV dibiayai oleh Pro, pembelian sekali sahaja yang pilihan untuk tambahan. Alat kawalan jauh asas adalah percuma.'),
      ('Pada peranti yang sudah anda ada', 'iPhone, iPad dan Mac daripada App Store, PC Windows daripada Microsoft Store, dan Android melalui akses awal percuma di Google Play. Lihat [Aplikasi alat kawalan jauh untuk iPhone](@iphone) dan [Aplikasi alat kawalan jauh untuk Windows](@windows).'),
      ('Privasi', 'Tiada akaun dan tiada penjejakan dalam aplikasi. Komunikasi dengan TV berlaku dalam rangkaian setempat sahaja, dan data sambungan kekal disulitkan pada peranti anda. Butiran dalam [Dasar privasi](@privacidad).'),
    ],
    marca=None,
    faq=[
      ('Adakah ada aplikasi alat kawalan jauh tanpa langganan?', 'Ada. Mando TV tiada langganan langsung: alat kawalan jauh percuma dan tanpa iklan, Pro ialah pembelian sekali sahaja yang pilihan.'),
      ('Adakah Mando TV benar-benar percuma?', 'Ya. Anak panah, OK, Kembali, Utama, volum, saluran, nombor, papan kekunci dan hidupkan atau matikan adalah percuma, tanpa iklan dan tanpa had masa.'),
      ('Adakah ia berfungsi tanpa Wi-Fi?', 'Kebanyakan masa tidak. Mando TV mengawal TV pintar melalui Wi-Fi rumah anda. Pengecualiannya: inframerah pada telefon Android yang ada pemancar inframerah, yang juga berfungsi dengan TV yang bukan TV pintar atau tiada sambungan Wi-Fi, dan Bluetooth, dalam beta dari Android 9, untuk Google TV, Android TV dan Fire TV.'),
    ]),
  dict(clave='roku-app-alt', corto='Alternatif aplikasi Roku', fecha='2026-11-23',
    titulo='Alternatif Aplikasi Roku: Alat Kawalan Jauh Roku Mudah',
    desc='Alternatif aplikasi Roku: Mando TV mengawal TV dan pemain Roku melalui Wi-Fi, tanpa akaun dan iklan, serta Samsung, LG dan Google TV.',
    h1='Alternatif aplikasi Roku: satu aplikasi untuk semua TV',
    intro='Aplikasi Roku rasmi boleh melakukan banyak perkara: Kedai Saluran, penghantaran, Private Listening dan alat kawalan jauh. Jika anda hanya mahukan alat kawalan jauh yang pantas, atau di rumah anda juga ada TV Samsung, LG atau Google TV, Mando TV ialah alternatif mudah yang mengawal Roku melalui Wi-Fi anda tanpa akaun.',
    pasos=[
      'Sambungkan telefon dan Roku ke Wi-Fi yang sama.',
      'Muat turun Mando TV dan buka. TV Roku atau pemain Roku anda muncul dalam senarai. Ketik padanya. Roku tidak meminta kod.',
      'Gunakan anak panah, OK, Kembali, Utama, volum dan papan kekunci. Taip carian dalam saluran Roku dengan papan kekunci telefon.',
      'Jika butang tidak berbuat apa-apa, pada Roku pergi ke Tetapan > Sistem > Tetapan sistem lanjutan > Kawalan oleh aplikasi mudah alih dan tetapkan akses rangkaian kepada Lalai atau Permissive (pada perisian Roku yang lebih baharu, tetapkan Kawalan oleh aplikasi mudah alih kepada Dibenarkan).',
      'Pilihan: pada TV Roku, aktifkan "Permulaan pantas TV" dalam Tetapan > Sistem > Kuasa supaya Mando TV boleh menghidupkan TV.',
    ],
    extra=[
      ('Di mana Mando TV lebih sesuai', 'Satu aplikasi untuk beberapa TV: Roku, Samsung, LG dan Google TV atau Android TV. Tanpa akaun, tanpa iklan. Ia juga berfungsi pada PC Windows, yang berguna di meja kerja. Anak panah dan volum bertindak balas dengan pantas, dan dengan papan kekunci anda menaip carian tanpa susah payah.'),
      ('Di mana aplikasi Roku rasmi lebih baik', 'Kekalkan aplikasi Roku untuk apa yang ditawarkannya selain alat kawalan jauh, seperti menyemak imbas dan menambah saluran daripada Kedai Saluran Roku serta penghantaran dan Private Listening sendiri (bunyi melalui fon kepala pada telefon). Gunakan kedua-duanya jika mahu. Kedua-duanya boleh berada pada telefon yang sama.'),
      ('TV Roku dan pemain Roku', 'Kedua-duanya berfungsi. Ini termasuk model TV Roku daripada TCL, Hisense, Philips dan lain-lain, serta Roku Express, Streaming Stick dan Ultra. Butiran ada pada [halaman aplikasi alat kawalan jauh Roku](@roku).'),
      ('Jika aplikasi Roku tidak berfungsi lagi', 'Jika butang tidak lagi bertindak balas, Roku biasanya menyekat kawalan oleh aplikasi. Panduan [Aplikasi Roku tidak berfungsi](@roku-403) menunjukkan tetapan yang menyelesaikan masalah itu.'),
      ('Percuma dan Pro', 'Anak panah, OK, Kembali, Utama, volum, saluran, nombor, papan kekunci, membuka apl, menukar input dan hidupkan atau matikan adalah percuma, tanpa iklan dan tanpa langganan. Pad sentuh, arahan suara, apl kegemaran, rutin dan pemasa tidur ialah sebahagian daripada Mando TV Pro, pembelian sekali sahaja tanpa langganan.'),
    ],
    marca='roku',
    faq=[
      ('Adakah saya perlukan akaun Roku untuk menggunakan Mando TV?', 'Tidak. Mando TV berhubung dengan Roku melalui rangkaian rumah anda dan tidak meminta akaun.'),
      ('Adakah Mando TV menggantikan sepenuhnya aplikasi mudah alih Roku?', 'Sebagai alat kawalan jauh, ya. Untuk Kedai Saluran, penghantaran dan Private Listening, kekalkan aplikasi Roku rasmi.'),
      ('Adakah ia berfungsi dengan Roku Express atau Streaming Stick saya?', 'Ya. Semua pemain Roku dan TV Roku dikawal dengan cara yang sama.'),
    ]),
  dict(clave='lg-thinq', corto='Alternatif aplikasi LG ThinQ', fecha='2026-11-23',
    titulo='Alternatif Aplikasi LG ThinQ: Alat Kawalan Jauh LG Tanpa Akaun',
    desc='Mencari alternatif aplikasi LG ThinQ hanya sebagai alat kawalan jauh? Mando TV mengawal TV LG dengan webOS melalui Wi-Fi, tanpa akaun LG dan tanpa iklan.',
    h1='Alternatif aplikasi LG ThinQ untuk TV LG anda',
    intro='LG ThinQ ialah aplikasi rasmi LG, direka untuk seluruh rumah pintar: perkakas rumah, TV dan banyak lagi. Jika anda hanya mahukan alat kawalan jauh yang mudah untuk TV LG anda, Mando TV melakukannya melalui Wi-Fi rumah anda, tanpa anda perlu membuat akaun LG dan tanpa iklan.',
    pasos=[
      'Sambungkan telefon atau PC anda (iPhone, Android atau Windows) dan TV LG anda ke Wi-Fi yang sama.',
      'Muat turun Mando TV dan buka. TV LG anda muncul sendiri dalam senarai. Ketik padanya.',
      'Satu pertanyaan muncul pada TV. Sahkannya sekali dengan alat kawalan jauh TV, kayu bedik di bawah skrin atau Magic Remote.',
      'Butang, volum dan papan kekunci berfungsi serta-merta. Anda tidak perlukan akaun LG dan tidak perlu mendaftarkan TV.',
      'Pilihan: aktifkan "Hidupkan TV dengan peranti mudah alih" dalam tetapan TV supaya anda juga boleh menghidupkan TV daripada telefon.',
    ],
    extra=[
      ('Mando TV atau LG ThinQ: untuk apa', 'Gunakan ThinQ jika anda mahu mengurus perkakas rumah LG seperti mesin basuh, peti sejuk atau penghawa dingin, atau memerlukan fungsi akaun LG. Gunakan Mando TV jika anda mahukan alat kawalan jauh TV yang pantas dan mudah, yang juga berfungsi untuk Samsung, Roku dan Google TV dalam aplikasi yang sama. Ramai yang mengekalkan kedua-duanya: ThinQ untuk perkakas rumah, Mando TV untuk TV.'),
      ('Apa yang dilakukan oleh Mando TV pada TV LG', 'Ia berfungsi dengan TV pintar LG yang menggunakan webOS, iaitu kebanyakan model sejak 2014, termasuk LED, NanoCell, QNED dan OLED. Ia memberi anda anak panah, OK, Kembali, Utama, volum, saluran, senyap, kawalan main semula dan papan kekunci untuk menaip dalam YouTube, Netflix atau pelayar. Senarai apl dan senarai input juga percuma. Dengan Pro, anda mendapat penuding seperti pada Magic Remote.'),
      ('Apa yang tidak dilakukan oleh Mando TV', 'Ia tidak mengawal perkakas rumah LG, tidak menggunakan akaun LG anda dan tidak menggantikan perkhidmatan akaun LG pada TV. Ia ialah alat kawalan jauh, bukan hab rumah pintar.'),
      ('Privasi dan iklan', 'Mando TV tiada iklan dan tiada akaun. Ia hanya berhubung dengan TV dalam rangkaian rumah anda dan menyimpan kunci sambungan secara disulitkan pada peranti anda. Semua fungsi ada pada halaman [Aplikasi alat kawalan jauh LG](@lg).'),
      ('Percuma dan Pro', 'Anak panah, OK, Kembali, Utama, volum, saluran, nombor, papan kekunci, membuka apl, menukar input dan hidupkan atau matikan adalah percuma, tanpa iklan dan tanpa langganan. Pad sentuh, arahan suara, apl kegemaran, rutin dan pemasa tidur ialah sebahagian daripada Mando TV Pro, pembelian sekali sahaja tanpa langganan.'),
    ],
    marca='lg',
    faq=[
      ('Bolehkah saya mengawal TV LG saya tanpa aplikasi LG ThinQ?', 'Boleh. Mando TV bersambung terus melalui Wi-Fi anda ke TV LG dengan webOS. Anda menerima satu pertanyaan pada TV sekali sahaja, dan siap, tanpa akaun LG.'),
      ('Adakah Mando TV berfungsi dengan penuding LG Magic Remote?', 'Mando TV Pro mempunyai penuding yang anda gerakkan dengan jari pada skrin telefon, serupa dengan cara Magic Remote menggerakkan anak panah.'),
      ('Adakah Mando TV daripada LG?', 'Bukan. Mando TV ialah aplikasi bebas dan tiada kaitan dengan LG. LG dan ThinQ dimiliki oleh pemiliknya masing-masing dan disebut hanya untuk menyatakan keserasian.'),
    ]),
  dict(clave='smartthings', corto='Alternatif SmartThings', fecha='2026-11-23',
    titulo='SmartThings Tidak Berfungsi? Alternatif Mudah untuk Samsung',
    desc='SmartThings terlalu perlahan? Mando TV mengawal TV Samsung Tizen terus melalui Wi-Fi. Tanpa akaun Samsung, tanpa iklan. Langkah demi langkah.',
    h1='Alternatif SmartThings untuk TV Samsung',
    intro='SmartThings ialah aplikasi Samsung untuk seluruh rumah pintar, dan alat kawalan jauhnya berjalan melalui akaun Samsung anda. Jika ia tidak lagi berfungsi atau anda mahukan penyelesaian pantas, Mando TV mengawal TV Samsung dengan Tizen, buatan 2016 dan ke atas, terus melalui Wi-Fi anda tanpa akaun.',
    pasos=[
      'Sambungkan telefon dan TV Samsung ke Wi-Fi yang sama.',
      'Muat turun Mando TV dan buka aplikasi. TV Samsung anda muncul sendiri dalam senarai. Ketik padanya.',
      'TV bertanya sama ada anda mahu membenarkan sambungan. Pilih "Benarkan" dengan alat kawalan jauh atau dengan butang pada TV (hanya kali pertama).',
      'Terus gunakan anak panah, OK, Kembali, Utama, volum, saluran dan papan kekunci.',
      'Pilihan: aktifkan "Hidupkan dengan mudah alih" dalam Tetapan > Umum > Rangkaian > Tetapan Pakar supaya Mando TV juga boleh menghidupkan TV.',
    ],
    extra=[
      ('Mengapa alat kawalan jauh telefon tidak lagi berfungsi', 'Puncanya biasanya mudah: telefon dan TV berada dalam Wi-Fi yang berbeza, VPN sedang aktif atau TV dalam keadaan tunggu yang dalam. Pada SmartThings, akaun Samsung juga boleh menjadi punca masalah, contohnya apabila anda telah dilog keluar. Mando TV bercakap terus dengan TV dalam rangkaian rumah, tiada akaun untuk dilog masuk. Petua lain ada dalam [Telefon anda tidak jumpa TV](@not-found).'),
      ('Mando TV atau SmartThings: untuk apa', 'Kekalkan SmartThings jika anda menggunakannya untuk perkakas rumah Samsung, lampu atau peranti rumah pintar lain, atau untuk fungsi akaun Samsung anda. Gunakan Mando TV jika anda hanya mahukan alat kawalan jauh TV yang pantas, atau di rumah anda juga ada peranti LG, Roku, Google TV atau Fire TV: satu aplikasi mengawal semuanya. Kedua-dua aplikasi boleh dipasang pada telefon yang sama.'),
      ('Jika anda tertolak kebenaran secara tidak sengaja', 'Pada TV, pergi ke Tetapan > Umum > Pengurus Peranti Luaran > Pengurus Sambungan Peranti dan tetapkan Mando TV kepada dibenarkan.'),
      ('Tiada alat kawalan jauh?', 'Anda boleh mengesahkan pertanyaan itu dengan butang pada TV itu sendiri. Panduan [TV Samsung tanpa alat kawalan jauh](@samsung-lost) menunjukkan caranya.'),
      ('Percuma dan Pro', 'Anda boleh memuat turun dan menggunakan alat kawalan jauh secara percuma, tanpa iklan dan tanpa langganan. Mando TV Pro ialah pembelian sekali sahaja yang pilihan untuk tambahan.'),
    ],
    marca='samsung',
    faq=[
      ('Bolehkah saya mengawal TV Samsung saya tanpa SmartThings?', 'Boleh. Mando TV bersambung terus melalui Wi-Fi anda ke TV Samsung dengan Tizen. Anda membenarkan sambungan sekali sahaja pada TV, tanpa akaun Samsung.'),
      ('Adakah Mando TV juga mengawal perkakas rumah Samsung?', 'Tidak. Ia hanya alat kawalan jauh untuk TV. Untuk perkakas rumah dan peranti rumah pintar lain, anda kekalkan SmartThings.'),
      ('Adakah Mando TV daripada Samsung?', 'Bukan. Mando TV ialah aplikasi bebas dan tiada kaitan dengan Samsung. Samsung dan SmartThings dimiliki oleh pemiliknya masing-masing dan disebut hanya untuk menyatakan keserasian.'),
    ]),
  dict(clave='googletv-alt', corto='Alternatif alat kawalan jauh Google TV', fecha='2026-11-23',
    titulo='Alat Kawalan Jauh Google TV Tidak Berfungsi? Ini Alternatifnya',
    desc='Alat kawalan jauh telefon untuk Google TV tidak jumpa TV? Mando TV mengawal Google TV dan Android TV melalui Wi-Fi, tanpa akaun Google dan tanpa iklan.',
    h1='Alternatif alat kawalan jauh Google TV pada telefon',
    intro='Alat kawalan jauh telefon untuk Google TV dan Android TV terdapat dalam aplikasi Google sendiri dan dipautkan kepada akaun Google anda. Jika ia tidak jumpa TV, anda tersekat. Mando TV ialah aplikasi alat kawalan jauh yang berasingan, dipasangkan dengan kod 6 aksara pada skrin dan berfungsi tanpa akaun Google, pada iPhone, telefon Android atau PC Windows.',
    pasos=[
      'Hidupkan TV dan sambungkan telefon anda ke Wi-Fi yang sama.',
      'Muat turun Mando TV dan buka aplikasi. Dalam senarai, ketik TV anda dengan Google TV atau Android TV.',
      'TV memaparkan kod 6 aksara. Masukkannya dalam Mando TV dan ketik Pasangkan.',
      'Gunakan anak panah, OK, Kembali, Utama, volum dan papan kekunci. Anda tidak perlu log masuk di mana-mana.',
      'Pilihan: dalam tetapan TV, cari Wake on LAN atau "Hidupkan melalui rangkaian" supaya aplikasi juga boleh menghidupkan TV.',
    ],
    extra=[
      ('Mengapa alat kawalan jauh telefon tidak lagi jumpa TV', 'Kebanyakan masa puncanya rangkaian: telefon dan TV berada dalam Wi-Fi yang berbeza, VPN sedang aktif atau rangkaian tetamu memisahkan peranti. Selesaikan ini dahulu kerana ia menjejaskan semua aplikasi alat kawalan jauh. Lebih lanjut dalam [Telefon anda tidak jumpa TV](@not-found).'),
      ('Dengan TV yang mana ia berfungsi', 'TV dengan Google TV dan Android TV daripada Sony, TCL, Hisense, Philips, Sharp, Xiaomi, Toshiba dan lain-lain, serta Chromecast dengan Google TV, Google TV Streamer dan Nvidia Shield. Semuanya dipasangkan dengan cara yang sama, sekali sahaja dengan kod pada skrin.'),
      ('Di mana aplikasi Google lebih baik', 'Aplikasi Google juga membantu anda mencari kandungan untuk ditonton dan mengingati senarai tontonan anda. Kekalkannya untuk itu. Mando TV hanyalah alat kawalan jauh dan juga mengawal Samsung, LG, Roku dan peranti Fire TV daripada aplikasi yang sama serta dari PC Windows.'),
      ('Jika aplikasi alat kawalan jauh Android TV yang lama tiada', 'Google telah memindahkan alat kawalan jauh telefon daripada aplikasi Android TV Remote Control yang lama ke aplikasi Google TV. Jika anda mahukan alat kawalan jauh yang berdiri sendiri, Mando TV ialah satu pilihan.'),
      ('Percuma dan Pro', 'Anda boleh memuat turun dan menggunakan alat kawalan jauh secara percuma, tanpa iklan dan tanpa langganan. Mando TV Pro ialah pembelian sekali sahaja yang pilihan untuk tambahan.'),
    ],
    marca='android',
    faq=[
      ('Adakah saya perlukan akaun Google untuk menggunakan Mando TV dengan Google TV?', 'Tidak. Kod pada TV sudah cukup untuk memasangkan.'),
      ('Adakah ia berfungsi dengan Chromecast dengan Google TV?', 'Ya. Pemasangan berjalan dengan cara yang sama, dengan kod 6 aksara pada skrin.'),
      ('Bolehkah saya menggunakannya dari iPhone?', 'Boleh. Mando TV terdapat di App Store untuk iPhone dan iPad, di Microsoft Store untuk Windows dan dalam akses awal percuma di Google Play untuk Android.'),
    ]),
  dict(clave='windows', corto='Alat kawalan jauh untuk PC Windows', fecha='2026-11-23',
    titulo='Aplikasi Alat Kawalan Jauh untuk Windows: Kawal TV dari PC',
    desc='Kawal Samsung, LG, Roku, Google TV atau Fire TV dari PC Windows dengan Mando TV: pintasan papan kekunci, alat kawalan jauh mini dan Wi-Fi. Di Microsoft Store.',
    h1='Aplikasi alat kawalan jauh untuk PC Windows',
    intro='Mando TV mempunyai aplikasi Windows yang menukar PC atau komputer riba anda menjadi alat kawalan jauh untuk TV melalui rangkaian rumah. Taip pada TV dengan papan kekunci sebenar anda, biarkan tetingkap alat kawalan jauh kecil di hadapan semasa anda bekerja dan kawal Samsung, LG, Roku, Google TV atau Fire TV dengan aplikasi yang sama.',
    pasos=[
      'Pasang Mando TV secara percuma daripada Microsoft Store pada PC dengan Windows 10 atau 11.',
      'Pastikan PC dan TV berada dalam rangkaian yang sama, melalui Wi-Fi atau kabel pada penghala yang sama.',
      'Buka Mando TV. TV muncul dalam senarai. Klik padanya.',
      'Sahkan pertanyaan pada TV jika ia bertanya (LG, Samsung), atau masukkan kod yang dipaparkan (Google TV, Fire TV).',
      'Klik butang atau taip carian dengan papan kekunci anda. Siap.',
    ],
    extra=[
      ('Pintasan papan kekunci (Pro)', 'Dengan Pro, papan kekunci PC anda menjadi alat kawalan jauh: kekunci anak panah untuk bergerak, Enter untuk OK, Backspace atau Esc untuk kembali, tambah dan tolak untuk volum, M untuk senyap dan bar ruang untuk jeda.'),
      ('Alat kawalan jauh mini (Pro)', 'Tetingkap alat kawalan jauh kecil yang kekal di atas semua tetingkap lain. Dengan itu anda boleh menukar volum atau menjeda tanpa mengganggu kerja anda.'),
      ('Menaip pada TV dari PC', 'Papan kekunci pada skrin TV agak perlahan. Dalam Mando TV, anda menaip dengan papan kekunci sebenar dan teks sampai ke medan carian TV. Bahagian ini percuma.'),
      ('Butiran lanjut', 'Panduan langkah demi langkah ada dalam [Kawal TV dengan PC](@pc). Untuk telefon, baca [Telefon sebagai alat kawalan jauh melalui Wi-Fi](@wifi).'),
      ('Percuma dan Pro', 'Anak panah, OK, Kembali, Utama, volum, saluran, nombor, papan kekunci, membuka apl, menukar input dan hidupkan atau matikan adalah percuma, tanpa iklan dan tanpa langganan. Pad sentuh, arahan suara, apl kegemaran, rutin dan pemasa tidur ialah sebahagian daripada Mando TV Pro, pembelian sekali sahaja tanpa langganan. Pada Windows, anda membeli Pro melalui Microsoft Store.'),
      ('Arahan suara dari PC (Pro)', 'Dengan Pro, anda boleh bercakap dengan TV melalui mikrofon PC. Suara dikenali terus pada PC: untuk itu anda tidak memerlukan internet dan tidak perlu menetapkan apa-apa dalam Windows. Apa yang anda katakan tidak pernah meninggalkan PC dan tidak disimpan. Hanya pada pemproses yang sangat lama, aplikasi beralih kepada input suara Windows. Untuk itu pengecaman pertuturan dalam talian mesti dihidupkan dalam tetapan privasi dan bahasa anda ditambah dalam Windows.'),
    ],
    marca=None,
    faq=[
      ('Adakah aplikasi alat kawalan jauh untuk Windows memerlukan Bluetooth atau kabel?', 'Tidak. Ia menggunakan rangkaian rumah anda. PC dan TV hanya perlu disambungkan ke penghala yang sama.'),
      ('TV yang mana boleh saya kawal dari Windows?', 'TV Samsung dengan Tizen, TV LG dengan webOS, TV dan pemain Roku, Google TV dan Android TV serta Fire TV.'),
      ('Bolehkah saya melihat imej TV pada PC atau mendengarnya melalui pembesar suara PC?', 'Tidak. Mando TV hanyalah alat kawalan jauh. Ia tidak mencerminkan atau menstrim imej TV ke komputer.'),
      ('Mengapa suara tidak berfungsi pada PC Windows saya?', 'Kawalan suara ialah fungsi Pro. Semak sama ada Pro aktif dan mikrofon PC berfungsi. Pada kebanyakan PC, suara dikenali terus pada PC, tanpa internet. Hanya pada pemproses yang sangat lama aplikasi menggunakan input suara Windows: dalam kes itu, hidupkan pengecaman pertuturan dalam talian dalam tetapan privasi Windows dan tambahkan bahasa anda dalam tetapan bahasa.'),
    ]),
  dict(clave='iphone', corto='Aplikasi alat kawalan jauh untuk iPhone', fecha='2026-11-23',
    titulo='Aplikasi Alat Kawalan Jauh untuk iPhone: Samsung, LG, Roku, Google TV',
    desc='Guna iPhone anda sebagai alat kawalan jauh untuk Samsung, LG, Roku, Google TV dan Fire TV melalui Wi-Fi. Percuma di App Store, tanpa akaun dan tanpa iklan.',
    h1='Aplikasi alat kawalan jauh untuk iPhone: satu untuk semua TV',
    intro='Mando TV menjadikan iPhone atau iPad anda alat kawalan jauh untuk Samsung, LG, Roku, Google TV atau Android TV serta Fire TV, melalui Wi-Fi rumah anda. Aplikasi ini percuma di App Store, tanpa akaun dan tanpa iklan. Ia juga berjalan pada Android dan Windows.',
    pasos=[
      'Muat turun Mando TV secara percuma daripada App Store.',
      'Sambungkan iPhone dan TV anda ke Wi-Fi yang sama.',
      'Buka Mando TV dan ketik Benarkan apabila iOS meminta akses kepada rangkaian setempat. Aplikasi memerlukannya untuk mencari TV.',
      'Dalam senarai, ketik TV anda. Sahkan pertanyaan pada TV jika ia bertanya (LG dan Samsung), atau masukkan kod yang dipaparkan oleh TV (Google TV atau Fire TV).',
      'Gunakan butang, volum dan papan kekunci. Anda sudah bersambung.',
    ],
    extra=[
      ('Berfungsi dengan TV ini', 'LG webOS, Samsung Tizen (buatan 2016 dan ke atas), TV dan pemain Roku, Google TV dan Android TV serta Fire TV. Halaman jenama ialah [Samsung](@samsung), [LG](@lg), [Roku](@roku) dan [Android TV](@android).'),
      ('Mengapa ia meminta rangkaian setempat', 'iPhone menyekat akses aplikasi kepada peranti dalam rangkaian rumah anda melainkan anda membenarkannya. Jika TV tidak muncul dalam senarai, buka Tetapan > Mando TV dan hidupkan "Local Network". Aplikasi hanya berhubung dengan TV anda dalam rangkaian rumah anda.'),
      ('Mengapa Mando TV dan bukan aplikasi pengeluar', 'Setiap jenama TV mempunyai aplikasinya sendiri dan mahukan persediaan atau akaun tersendiri. Mando TV ialah satu aplikasi untuk semua, tanpa akaun.'),
      ('Percuma dan Pro pada iPhone', 'Anak panah, OK, Kembali, Utama, volum, saluran, nombor, papan kekunci, membuka apl, menukar input dan hidupkan atau matikan adalah percuma, tanpa iklan dan tanpa langganan. Pad sentuh, arahan suara, apl kegemaran, rutin dan pemasa tidur ialah sebahagian daripada Mando TV Pro, pembelian sekali sahaja tanpa langganan. Anda membeli Pro sekali terus dalam aplikasi.'),
    ],
    marca=None,
    faq=[
      ('Adakah Mando TV percuma pada iPhone?', 'Muat turun adalah percuma, tanpa iklan. Alat kawalan jauh asas percuma, begitu juga membuka apl dan menukar input. Tambahan seperti pad sentuh, arahan suara dan rutin ialah sebahagian daripada Mando TV Pro, pembelian sekali sahaja.'),
      ('Adakah ia berfungsi pada iPad?', 'Ya. Aplikasi yang sama berjalan pada iPhone dan iPad.'),
      ('Adakah aplikasi alat kawalan jauh untuk iPhone memerlukan Bluetooth atau pemancar inframerah?', 'Tidak pada iPhone. iPhone tiada pemancar inframerah, jadi kawalan inframerah tidak ada di situ, dan pilihan Bluetooth hanya ada untuk Android 9 ke atas, bukan untuk iPhone. Pada iPhone, Mando TV mengawal TV pintar serta Apple TV (beta) melalui Wi-Fi rumah anda.'),
    ]),
  dict(clave='firetv', corto='Alat kawalan jauh Fire TV', fecha='2026-11-23',
    titulo='Aplikasi Alat Kawalan Jauh Fire TV untuk Telefon dan PC',
    desc='Alat kawalan jauh Fire TV pada telefon: kawal Fire TV Stick, Fire TV Cube atau TV dengan Fire TV melalui Wi-Fi, dengan PIN 4 digit. Tanpa aplikasi Amazon.',
    h1='Alat kawalan jauh Fire TV untuk telefon atau PC anda',
    intro='Jika alat kawalan jauh Fire TV hilang atau bateri habis, Mando TV mengawal Fire TV Stick, Fire TV Cube atau TV dengan Fire TV terbina dalam melalui Wi-Fi. Pemasangan dibuat dengan PIN 4 digit. Fire TV baharu dalam Mando TV, jadi kemas kini aplikasi terlebih dahulu.',
    pasos=[
      'Kemas kini Mando TV kepada versi terkini daripada App Store, Microsoft Store atau Google Play.',
      'Hidupkan Fire TV dan sambungkan telefon anda ke Wi-Fi yang sama.',
      'Buka Mando TV. Fire TV anda muncul dalam senarai. Ketik padanya.',
      'Pada skrin TV, PIN 4 digit dipaparkan. Masukkannya dalam Mando TV. Anda hanya melakukannya sekali.',
      'Gunakan anak panah, OK, Kembali, Utama, butang main semula dan papan kekunci untuk carian.',
    ],
    extra=[
      ('Peranti Fire TV yang disokong', 'Fire TV Stick, Fire TV Stick 4K, Fire TV Cube dan TV dengan Fire TV terbina dalam, seperti TV Amazon Fire TV Edition dan beberapa model Hisense. Sokongan ini baharu dan setakat ini kami hanya sempat menguji beberapa peranti sebenar. Jika sesuatu tidak berfungsi seperti dijangka, hantarkan model anda kepada kami melalui halaman bantuan.'),
      ('Menghidupkan Fire TV', 'Mando TV tidak menghidupkan Fire TV melalui rangkaian. Hidupkan TV dengan butang kuasa pada peranti: Fire TV Stick atau Cube yang dipasang biasanya bangun melalui HDMI-CEC, dan pada TV dengan Fire TV terbina dalam, TV itu sendiri ialah Fire TV. Selepas itu anda mengawalnya dari telefon.'),
      ('Jika Fire TV anda tidak muncul', 'Pastikan kedua-dua peranti berada dalam Wi-Fi yang sama dan Fire TV sedang aktif. Pada iPhone, benarkan "Local Network" untuk Mando TV dalam Tetapan. Lihat [Telefon anda tidak jumpa TV](@not-found).'),
      ('Tiada alat kawalan jauh langsung?', 'Fire TV mesti menunjukkan PIN pada skrin, jadi TV dan Fire TV mesti hidup dan menunjukkan imej. Jika TV berada pada input yang salah, tukarkannya dengan butang pada TV. Lihat [Tukar input HDMI tanpa alat kawalan jauh](@hdmi).'),
      ('Percuma dan Pro', 'Anak panah, OK, Kembali, Utama, volum, saluran, nombor, papan kekunci, membuka apl, menukar input dan hidupkan atau matikan adalah percuma, tanpa iklan dan tanpa langganan. Pad sentuh, arahan suara, apl kegemaran, rutin dan pemasa tidur ialah sebahagian daripada Mando TV Pro, pembelian sekali sahaja tanpa langganan.'),
    ],
    marca=None,
    faq=[
      ('Adakah saya perlukan aplikasi Amazon Fire TV?', 'Tidak. Mando TV bersambung ke Fire TV melalui Wi-Fi anda dengan PIN. Anda tidak memerlukan akaun Amazon pada telefon.'),
      ('Adakah ia berfungsi dengan TV yang ada Fire TV dan dengan Fire TV Stick?', 'Ya, memang untuk itulah ia dibina. Sokongan ini baharu, jadi pastikan aplikasi sentiasa terkini dan maklumkan kepada kami model yang tidak berfungsi seperti dijangka.'),
      ('Mengapa saya memerlukan PIN?', 'Fire TV memaparkan PIN 4 digit untuk membuktikan anda berada di hadapan TV. Tiada sesiapa boleh memasangkan tanpa melihat skrin.'),
    ]),
  dict(clave='firetv-lost', corto='Alat kawalan jauh Fire TV hilang', fecha='2026-11-23',
    titulo='Alat Kawalan Jauh Fire TV Hilang? Telefon Anda Boleh Membantu',
    desc='Alat kawalan jauh Fire TV Stick hilang? Kawalnya melalui Wi-Fi dengan telefon, dipasangkan dengan PIN 4 digit. Petua untuk Wi-Fi baharu dan HDMI-CEC.',
    h1='Alat kawalan jauh Fire TV hilang: cara guna telefon anda',
    intro='Jika alat kawalan jauh untuk Fire TV Stick, Fire TV Cube atau TV pintar dengan Fire TV hilang atau tidak lagi berfungsi, telefon anda mengambil alih kawalan selagi Fire TV masih bersambung ke Wi-Fi anda. Pemasangan dibuat dengan PIN 4 digit pada skrin, jadi anda tidak memerlukan alat kawalan jauh lama untuk itu.',
    pasos=[
      'Hidupkan TV dengan butang pada peranti. Fire TV Stick atau Cube yang dipasang biasanya bangun sekali; dengan HDMI-CEC diaktifkan, TV selalunya bertukar sendiri ke inputnya.',
      'Jika TV menunjukkan input lain, tukarkannya dengan butang input atau sumber pada TV. Lihat [Tukar input HDMI tanpa alat kawalan jauh](@hdmi).',
      'Sambungkan telefon anda ke Wi-Fi yang sama dengan Fire TV.',
      'Muat turun Mando TV dan buka aplikasi. Fire TV anda muncul dalam senarai. Ketik padanya.',
      'TV memaparkan PIN 4 digit. Masukkannya dalam Mando TV. Anda hanya melakukannya sekali.',
      'Gunakan anak panah, OK, Kembali, Utama, volum, butang main semula dan papan kekunci pada telefon anda.',
    ],
    extra=[
      ('Cuba dahulu alat kawalan jauh TV (HDMI-CEC)', 'Banyak alat kawalan jauh TV boleh mengawal Fire TV Stick melalui HDMI-CEC. Jika antara muka Fire TV kelihatan, tekan anak panah dan OK pada alat kawalan jauh TV. Jika tiada apa-apa berlaku, aktifkan CEC dalam tetapan TV (Anynet+ pada Samsung, SIMPLINK pada LG, BRAVIA Sync pada Sony) dan pada Fire TV aktifkan kawalan peranti HDMI-CEC dalam tetapan paparan ("Display & Sounds").'),
      ('Jika anda menukar Wi-Fi', 'Tanpa alat kawalan jauh, anda tidak dapat memasukkan kata laluan Wi-Fi baharu pada Fire TV, tetapi ada jalan keluar: pada telefon kedua, cipta hotspot dengan nama dan kata laluan yang sama seperti Wi-Fi lama anda. Fire TV bersambung kepadanya secara automatik. Sambungkan telefon dengan Mando TV ke hotspot itu, pasangkan dengan PIN, kemudian pada Fire TV pergi ke Tetapan > Rangkaian dan pilih Wi-Fi baharu anda. Akhir sekali, sambungkan juga telefon anda ke Wi-Fi baharu.'),
      ('Memasangkan alat kawalan jauh ganti', 'Kebanyakan alat kawalan jauh Fire TV baharu dipasangkan dengan menahan butang Utama kira-kira 10 saat, berhampiran Fire TV. Jika tidak berjaya, buka Tetapan > Pengawal dan Peranti Bluetooth > Alat Kawalan Jauh Amazon Fire TV > Tambah Alat Kawalan Jauh Baharu. Menu ini juga boleh dicapai daripada telefon anda dengan Mando TV.'),
      ('Fire TV terbina dalam TV', 'Pada TV dengan Fire TV terbina dalam, seperti banyak model Insignia dan Toshiba, langkah yang sama berfungsi kerana TV itu sendiri ialah Fire TV.'),
      ('Sebelum bermula', 'Sokongan Fire TV baharu dalam Mando TV. Kemas kini aplikasi terlebih dahulu. Jika model anda tidak bertindak balas seperti dijangka, hubungi kami melalui [halaman bantuan](@soporte) dan nyatakan modelnya.'),
      ('Percuma dan Pro', 'Anda boleh memuat turun dan menggunakan alat kawalan jauh secara percuma, tanpa iklan dan tanpa langganan. Mando TV Pro ialah pembelian sekali sahaja yang pilihan untuk tambahan.'),
    ],
    marca=('firetv', 'Alat kawalan jauh Fire TV'),
    faq=[
      ('Bolehkah saya mengawal Fire TV Stick dengan telefon tanpa alat kawalan jauh?', 'Boleh, selagi Fire TV hidup dan bersambung ke Wi-Fi anda. Mando TV memasangkan melalui PIN 4 digit pada TV, jadi anda tidak memerlukan alat kawalan jauh lama.'),
      ('Adakah ia berfungsi jika Fire TV berada dalam Wi-Fi baharu?', 'Tidak terus, kerana telefon dan Fire TV mesti berada dalam rangkaian yang sama. Dapatkan Fire TV dalam talian semula terlebih dahulu dengan helah hotspot pada halaman ini.'),
      ('Adakah saya perlukan aplikasi Amazon Fire TV atau akaun Amazon?', 'Tidak. Mando TV bersambung melalui rangkaian rumah anda dengan PIN dan tidak memerlukan akaun sendiri.'),
    ]),
  dict(clave='turn-on', corto='Hidupkan TV tanpa alat kawalan jauh', fecha='2026-11-23',
    titulo='Hidupkan TV Tanpa Alat Kawalan Jauh (Semua Jenama)',
    desc='Hidupkan TV tanpa alat kawalan jauh: di mana butang pada Samsung, LG, TCL, Hisense, Sony dan Vizio. Serta HDMI-CEC dan helah telefon.',
    h1='Cara menghidupkan TV tanpa alat kawalan jauh',
    intro='Hampir setiap TV masih mempunyai butang kuasa fizikal. Ia cuma tersembunyi dengan baik. Berikut tempatnya pada setiap jenama, serta dua cara untuk tidak perlu mencarinya lagi: HDMI-CEC daripada konsol atau peranti strim, dan menghidupkan TV daripada telefon melalui Wi-Fi.',
    pasos=[
      'Lihat di bawah tengah skrin, tepat di belakang logo jenama. Banyak TV ada butang kecil tunggal atau kayu bedik di situ, menghala ke bawah.',
      'Jika ia tiada di situ, raba di belakang TV berhampiran sudut bawah, kemudian di tepi kiri dan kanan.',
      'Tekan butang itu sekali. Pada banyak TV dengan hanya satu butang, tekanan singkat semasa TV hidup membuka menu kecil untuk input dan volum, dan tekanan panjang mematikannya.',
      'Masih tiada apa-apa? Semak kabel kuasa di kedua-dua hujung dan cuba soket lain. Jika lampu tunggu tidak menyala, TV tidak mendapat elektrik.',
      'Setelah TV hidup, sediakannya supaya anda tidak perlukan butang itu lagi: aktifkan HDMI-CEC dan hidupkan melalui rangkaian, kedua-duanya diterangkan di bawah.',
    ],
    extra=[
      ('Di mana butang kuasa mengikut jenama', 'Samsung: butang kawalan atau kayu bedik di bawah tengah skrin atau di belakang pada sudut bawah. LG: butang kayu bedik di bawah logo LG pada kebanyakan model. TCL dan Hisense: biasanya butang kecil di bawah tengah skrin atau di belakang berhampiran sudut bawah. Sony: di belakang atau pada tepi sisi, di bawah dekat pinggir. Vizio: di belakang, di bawah kiri atau bawah kanan, atau pada sisi. Kedudukannya berbeza mengikut model. Jika anda tidak menjumpainya, cari buku panduan dengan nombor model pada pelekat di belakang.'),
      ('Menghidupkan TV melalui konsol atau peranti strim (HDMI-CEC)', 'Dengan HDMI-CEC diaktifkan, menghidupkan PlayStation, Xbox, pemain Roku, Fire TV Stick atau Chromecast turut menghidupkan TV dan menukar ke input yang betul. Setiap jenama menamakan tetapan ini secara berbeza: Anynet+ pada Samsung, SIMPLINK pada LG, BRAVIA Sync pada Sony dan CEC pada kebanyakan yang lain. Lebih lanjut dalam [Hidupkan TV dan tukar ke HDMI konsol](@console).'),
      ('Menghidupkan TV daripada telefon', 'TV pintar boleh dibangunkan melalui Wi-Fi jika anda membenarkannya sekali, dan kemudian Mando TV menghidupkannya daripada telefon anda. Pada Samsung, aktifkan "Hidupkan dengan mudah alih" dalam Tetapan > Umum > Rangkaian > Tetapan Pakar. Pada LG, aktifkan "Hidupkan TV dengan peranti mudah alih" ([langkah demi langkah](@lg-on)). Pada TV Roku, aktifkan "Permulaan pantas TV" dalam Tetapan > Sistem > Kuasa. Pada Google TV dan Android TV, cari Wake on LAN atau "Hidupkan melalui rangkaian" jika model anda ada. Anda melakukannya sekali, semasa TV hidup.'),
      ('Jika anda tidak menjumpai butang', 'Sesetengah TV yang lebih baharu menyembunyikan butang tunggalnya sebegitu rupa sehingga kelihatan seolah-olah tiada. Cari tonjolan kecil atau kawasan penderia cahaya di bawah skrin: butang itu selalunya betul-betul di sebelahnya. Melalui Wi-Fi, Mando TV memerlukan TV pernah dihidupkan dan bersambung. Inframerah ialah pengecualian: pada telefon Android yang ada pemancar inframerah, Mando TV boleh menghidupkan TV yang tidak pernah disediakan, selagi anda menghalakan telefon ke TV. Inframerah ini baharu dan berfungsi dengan jenama dalam senarai kod aplikasi.'),
      ('Percuma dan Pro', 'Anda boleh memuat turun dan menggunakan alat kawalan jauh secara percuma, tanpa iklan dan tanpa langganan. Mando TV Pro ialah pembelian sekali sahaja yang pilihan untuk tambahan.'),
    ],
    marca=None,
    faq=[
      ('Bolehkah saya menghidupkan TV dengan telefon jika saya tidak pernah menyediakannya?', 'Tidak melalui Wi-Fi. TV yang mati hanya bangun daripada rangkaian jika hidupkan melalui rangkaian telah diaktifkan sebelum itu. Kali pertama, gunakan butang pada TV. Pengecualiannya ialah telefon Android yang ada pemancar inframerah: Mando TV boleh menghidupkan TV tanpa persediaan melalui inframerah jika jenamanya ada dalam senarai kod atau anda memilih "Jenama lain atau saya tidak tahu".'),
      ('Bagaimana cara menghidupkan TV Samsung tanpa alat kawalan jauh?', 'Tekan butang kawalan di bawah tengah skrin atau di belakang pada sudut bawah. Kemudian aktifkan "Hidupkan dengan mudah alih" supaya telefon anda boleh menghidupkannya pada kali berikutnya.'),
      ('Bagaimana cara menghidupkan TV Roku tanpa alat kawalan jauh?', 'Gunakan butang pada TV, biasanya di bawah tengah atau di belakang. Kemudian aktifkan "Permulaan pantas TV" dalam Tetapan > Sistem > Kuasa supaya Mando TV boleh menghidupkannya daripada telefon anda.'),
      ('Mengapa TV saya hidup sendiri apabila saya menghidupkan konsol?', 'Itulah HDMI-CEC. Ia memudahkan, dan anda boleh mematikannya dalam tetapan TV jika anda lebih suka begitu.'),
    ]),
  dict(clave='sony', corto='Alat kawalan jauh Sony', fecha='2026-11-23',
    titulo='Aplikasi Alat Kawalan Jauh Sony untuk Telefon dan PC',
    desc='Mando TV mengawal TV Sony Bravia dengan Google TV atau Android TV melalui Wi-Fi. Sokongan beta untuk model 2013 hingga 2015 tanpa Android.',
    h1='Cara mengawal TV Sony anda dengan telefon',
    intro='TV pintar Sony Bravia yang lebih baharu menggunakan Google TV, model lama dari 2015 menggunakan Android TV. Mando TV mengawal kedua-duanya melalui Wi-Fi anda daripada iPhone, telefon Android atau PC Windows. Aplikasi ini menggantikan alat kawalan jauh asal apabila ia hilang atau bateri habis.',
    pasos=[
      'Semak sama ada TV Sony anda menunjukkan skrin utama Google TV atau Android TV. Ini terpakai untuk kebanyakan TV pintar Sony Bravia buatan 2015 ke atas.',
      'Sambungkan telefon dan TV anda ke Wi-Fi yang sama.',
      'Buka Mando TV dan ketik TV Sony anda dalam senarai.',
      'Masukkan kod 6 aksara yang dipaparkan oleh TV pada skrin (hanya kali pertama). Anda tidak memerlukan alat kawalan jauh untuk itu.',
      'Gunakan anak panah, OK, Kembali, Utama, volum dan papan kekunci.',
    ],
    extra=[
      ('Menghidupkan TV Sony daripada telefon', 'Model Sony dengan Google TV atau Android TV boleh dibangunkan melalui rangkaian jika "Remote start" diaktifkan. Pilihan ini biasanya ada dalam Tetapan > Rangkaian & Internet > Remote start (laluannya boleh berbeza sedikit mengikut model). Kemudian, dalam Mando TV, ketik TV semasa ia mati dan aplikasi menghidupkannya.'),
      ('Di mana butang kuasa pada Sony', 'Pada kebanyakan TV Bravia, ia terletak di belakang, berhampiran sudut bawah kiri atau kanan, atau pada tepi sisi. Satu tekanan singkat menghidupkan TV. Lebih lanjut dalam [Hidupkan TV tanpa alat kawalan jauh](@turn-on).'),
      ('TV Sony yang lebih lama', 'TV Sony Bravia dari 2013 hingga 2015 yang tidak menggunakan Android disokong dalam Mando TV dalam status beta. Ini baharu dan mungkin masih ada kekurangan. TV memaparkan PIN 4 digit yang perlu anda masukkan dalam aplikasi. TV Sony lain tanpa Google TV atau Android TV tidak disokong buat masa ini.'),
      ('Percuma dan Pro', 'Anda boleh memuat turun dan menggunakan alat kawalan jauh secara percuma, tanpa iklan dan tanpa langganan. Mando TV Pro ialah pembelian sekali sahaja yang pilihan untuk tambahan.'),
    ],
    marca='android',
    faq=[
      ('Adakah Mando TV berfungsi dengan TV Sony Bravia?', 'Ya, dengan TV Sony yang menggunakan Google TV atau Android TV. Ini termasuk kebanyakan TV pintar Sony buatan 2015 ke atas.'),
      ('Adakah saya perlukan aplikasi Sony atau akaun Google?', 'Tidak. Mando TV dipasangkan dengan kod pada skrin TV dan tidak meminta akaun.'),
      ('Adakah ia berfungsi dengan TV Sony Bravia yang lebih lama tanpa Android?', 'Ya, dalam status beta, pada model Bravia dari 2013 hingga 2015 tanpa Android. Pemasangan dibuat dengan PIN 4 digit yang dipaparkan pada TV.'),
      ('Bolehkah saya menaip pada TV Sony saya dari telefon?', 'Boleh. Papan kekunci adalah percuma dan berfungsi dalam YouTube, Netflix dan carian TV.'),
    ]),
  dict(clave='tcl', corto='Alat kawalan jauh TCL', fecha='2026-11-23',
    titulo='Aplikasi Alat Kawalan Jauh TCL untuk Telefon dan PC',
    desc='Alat kawalan jauh TCL hilang? Kebanyakan TV TCL menggunakan Roku TV atau Google TV. Mando TV mengawal kedua-duanya melalui Wi-Fi, tanpa akaun dan iklan.',
    h1='Cara mengawal TV TCL anda dengan telefon',
    intro='TCL membuat TV, tetapi perisiannya ialah Roku TV atau Google TV (Android TV pada model lama). Mando TV mengawal kedua-dua sistem dan berfungsi sebagai alat kawalan jauh untuk TV TCL anda melalui Wi-Fi. Percuma, tanpa akaun dan tanpa iklan.',
    pasos=[
      'Ketahui sistem yang digunakan oleh TCL anda. Jika skrin utama menunjukkan grid mudah jubin saluran, ia Roku TV. Jika ia kelihatan seperti Google TV atau Android TV dengan baris penuh cadangan, ia Google TV.',
      'Sambungkan telefon dan TV TCL anda ke Wi-Fi yang sama.',
      'Buka Mando TV. TCL muncul sendiri dalam senarai. Ketik padanya.',
      'Pada TCL dengan Roku TV, tiada apa-apa lagi diperlukan. Pada TCL dengan Google TV, masukkan kod 6 aksara yang dipaparkan TV pada skrin (hanya kali pertama).',
      'Gunakan anak panah, OK, Kembali, Utama, volum dan papan kekunci. Hidupkan TV melalui aplikasi jika anda telah mengaktifkan hidupkan melalui rangkaian (lihat di bawah).',
    ],
    extra=[
      ('Menghidupkan TV TCL daripada telefon', 'Pada TCL Roku TV, aktifkan "Permulaan pantas TV" dalam Tetapan > Sistem > Kuasa. Pada TCL Google TV, cari pilihan Wake on LAN, "Hidupkan melalui rangkaian" atau mula jauh dalam tetapan rangkaian atau kuasa. Sesetengah model tidak menawarkannya. Dalam kes itu, hidupkan TV dengan butang kuasa fizikal, biasanya di bawah tengah atau di belakang.'),
      ('Jika TCL anda tidak muncul', 'Semak sama ada telefon dan TV berada dalam Wi-Fi yang sama. Penghala dengan rangkaian 2.4 GHz dan 5 GHz yang berasingan boleh menyembunyikan peranti antara satu sama lain. Pada iPhone, benarkan "Local Network" untuk Mando TV dalam Tetapan. Anda juga boleh menambah TV dengan memasukkan alamat IPnya. Baca [Telefon anda tidak jumpa TV](@not-found).'),
      ('Lebih lanjut tentang TCL anda', 'Untuk TCL dengan Roku TV, lihat [Aplikasi alat kawalan jauh Roku](@roku), untuk TCL dengan Google TV atau Android TV lihat [Aplikasi alat kawalan jauh Android TV](@android).'),
      ('Percuma dan Pro', 'Anak panah, OK, Kembali, Utama, volum, saluran, nombor, papan kekunci, membuka apl, menukar input dan hidupkan atau matikan adalah percuma, tanpa iklan dan tanpa langganan. Pad sentuh, arahan suara, apl kegemaran, rutin dan pemasa tidur ialah sebahagian daripada Mando TV Pro, pembelian sekali sahaja tanpa langganan.'),
    ],
    marca=None,
    faq=[
      ('Adakah Mando TV berfungsi dengan setiap TV TCL?', 'Ia berfungsi dengan TV TCL yang menggunakan Roku TV, Google TV atau Android TV, iaitu kebanyakan TV pintar TCL. TCL yang bukan TV pintar tidak boleh dikawal melalui Wi-Fi.'),
      ('Adakah saya perlukan aplikasi TCL atau akaun TCL?', 'Tidak. Mando TV bersambung terus melalui Wi-Fi rumah anda dan tidak memerlukan akaun.'),
      ('TCL saya meminta kod. Di mana ia?', 'Model TCL dengan Google TV dan Android TV memaparkan kod 6 aksara pada skrin. Masukkannya dalam Mando TV tepat seperti yang tertera. TCL dengan Roku TV tidak meminta kod.'),
    ]),
  dict(clave='hisense', corto='Alat kawalan jauh Hisense', fecha='2026-11-23',
    titulo='Aplikasi Alat Kawalan Jauh Hisense: Apa yang Berfungsi pada Telefon',
    desc='Alat kawalan jauh Hisense dengan Mando TV: kawalan untuk VIDAA, Roku TV, Google TV dan Fire TV melalui Wi-Fi. Gambaran jujur tentang apa yang berfungsi.',
    h1='Aplikasi alat kawalan jauh Hisense: apa yang berfungsi dan apa yang tidak',
    intro='TV Hisense tidak semuanya sama di dalam. Bergantung pada model, ia menggunakan sistem VIDAA milik Hisense sendiri, Roku TV, Google TV atau Fire TV. Mando TV berfungsi sebagai alat kawalan jauh untuk Hisense pada keempat-empat sistem, dengan satu pengecualian pada beberapa model VIDAA yang lebih baharu. Berikut cara mengenal pasti sistem anda dan apa yang boleh dijangka.',
    pasos=[
      'Semak sistem yang digunakan oleh Hisense anda. VIDAA ialah antara muka Hisense sendiri. Roku TV menunjukkan grid jubin saluran. Google TV menunjukkan baris cadangan. Fire TV menunjukkan skrin utama Fire TV dengan baris Amazon.',
      'Sambungkan telefon dan TV Hisense anda ke Wi-Fi yang sama.',
      'Buka Mando TV. TV muncul sendiri dalam senarai. Ketik padanya.',
      'Model VIDAA dan Fire TV mungkin menunjukkan PIN empat digit; Google TV menunjukkan kod enam aksara. Masukkannya dalam aplikasi. Roku TV tidak meminta apa-apa. Anda hanya melakukannya sekali.',
      'Gunakan anak panah, OK, Kembali, Utama, volum dan papan kekunci daripada telefon anda.',
    ],
    extra=[
      ('Hisense dengan Roku TV atau Google TV', 'Ini berfungsi sepenuhnya seperti mana-mana TV Roku atau Google TV yang lain. Butiran pada halaman [Aplikasi alat kawalan jauh Roku](@roku) dan [Aplikasi alat kawalan jauh Android TV](@android).'),
      ('Hisense dengan Fire TV', 'Sokongan Fire TV baharu dalam Mando TV. Kemas kini aplikasi kepada versi terkini daripada kedai anda. Cara pemasangan dengan PIN berfungsi ada pada halaman [Aplikasi alat kawalan jauh Fire TV](@firetv). Jika sesuatu tidak berfungsi seperti dijangka, hubungi kami melalui halaman bantuan dan nyatakan model anda.'),
      ('Hisense dengan VIDAA', 'Kebanyakan model VIDAA berfungsi: butang, volum, papan kekunci, apl dan input. Beberapa model VIDAA yang lebih baharu hanya menerima aplikasi Hisense rasmi. Mando TV mengesannya semasa menyambung dan memberitahu anda dengan jelas, bukannya gagal secara senyap. Dalam kes itu, aplikasi Hisense untuk model anda, butang pada TV atau alat kawalan jauh asal ialah jalan yang betul.'),
      ('Menghidupkan Hisense daripada telefon', 'Pada Hisense Roku TV, aktifkan "Permulaan pantas TV" dalam Tetapan > Sistem > Kuasa. Pada Google TV, cari pilihan Wake on LAN atau "Hidupkan melalui rangkaian". Jika tiada, gunakan butang kuasa pada TV.'),
      ('Percuma dan Pro', 'Anak panah, OK, Kembali, Utama, volum, saluran, nombor, papan kekunci, membuka apl, menukar input dan hidupkan atau matikan adalah percuma, tanpa iklan dan tanpa langganan. Pad sentuh, arahan suara, apl kegemaran, rutin dan pemasa tidur ialah sebahagian daripada Mando TV Pro, pembelian sekali sahaja tanpa langganan.'),
    ],
    marca=None,
    faq=[
      ('Adakah Mando TV berfungsi dengan Hisense VIDAA?', 'Ya, dengan kebanyakan model VIDAA. Beberapa yang lebih baharu hanya menerima aplikasi Hisense rasmi; Mando TV mengesannya dan memberitahu anda. TV Hisense dengan Roku TV, Google TV atau Fire TV juga disokong.'),
      ('Bagaimana saya tahu Hisense saya Roku TV, Google TV atau Fire TV?', 'Lihat skrin utama. Roku TV mempunyai grid jubin yang mudah dan logo Roku semasa permulaan. Google TV mempunyai baris cadangan. Fire TV mempunyai skrin utama Amazon Fire TV. Nama model dalam Tetapan > Perihal juga memberi petunjuk.'),
      ('Adakah saya perlukan akaun Hisense atau Google?', 'Tidak. Mando TV bersambung terus melalui Wi-Fi rumah anda dan tidak mempunyai akaun sendiri.'),
    ]),
  dict(clave='philips', corto='Alat kawalan jauh Philips', fecha='2026-11-23',
    titulo='Aplikasi Alat Kawalan Jauh Philips: Roku TV, Google TV, Android TV',
    desc='Mando TV mengawal TV Philips dengan Roku TV, Google TV atau Android TV melalui Wi-Fi, daripada telefon atau PC. Titan OS tidak disokong.',
    h1='Kawal TV Philips dengan telefon anda',
    intro='TV Philips menggunakan sistem berbeza mengikut negara dan tahun buatan: Roku TV di Amerika Syarikat, Google TV atau Android TV di banyak negara dan Titan OS pada beberapa model Eropah yang lebih baharu. Mando TV mengawal model dengan Roku TV, Google TV dan Android TV melalui Wi-Fi.',
    pasos=[
      'Semak skrin utama. Roku TV menunjukkan grid jubin. Google TV dan Android TV menunjukkan baris cadangan daripada Google. Titan OS mempunyai skrin utama tersendiri.',
      'Sambungkan telefon dan TV anda ke Wi-Fi yang sama.',
      'Buka Mando TV dan ketik TV Philips anda dalam senarai.',
      'Roku TV tidak meminta apa-apa. Google TV dan Android TV menunjukkan kod 6 aksara: masukkannya sekali dalam aplikasi.',
      'Gunakan anak panah, OK, Kembali, Utama, volum dan papan kekunci.',
    ],
    extra=[
      ('Philips Roku TV', 'Berfungsi seperti mana-mana TV Roku. Untuk menghidupkannya daripada telefon, aktifkan "Permulaan pantas TV" dalam Tetapan > Sistem > Kuasa. Lebih lanjut pada halaman [Aplikasi alat kawalan jauh Roku](@roku).'),
      ('Philips dengan Google TV atau Android TV', 'Termasuk banyak model Ambilight. Ia dipasangkan dengan kod pada skrin. Untuk menghidupkannya daripada telefon, cari Wake on LAN atau "Hidupkan melalui rangkaian" dalam tetapan rangkaian atau kuasa. Beberapa model tiada pilihan ini. Lebih lanjut pada halaman [Aplikasi alat kawalan jauh Android TV](@android).'),
      ('TV Philips yang lebih lama tanpa Android', 'TV Philips dari 2011 hingga 2015 yang tidak menggunakan Android disokong dalam Mando TV dalam beta. Ia baharu dan tidak memerlukan kod pemasangan.'),
      ('Philips dengan Titan OS', 'Titan OS ialah sistem lain yang tidak dikawal oleh Mando TV pada masa ini, dan kami lebih suka menyatakannya dengan jelas. Model Philips yang lebih baharu tanpa Android juga tidak dilindungi.'),
      ('Percuma dan Pro', 'Anda boleh memuat turun dan menggunakan alat kawalan jauh secara percuma, tanpa iklan dan tanpa langganan. Mando TV Pro ialah pembelian sekali sahaja yang pilihan untuk tambahan.'),
    ],
    marca=None,
    faq=[
      ('Adakah Mando TV berfungsi dengan TV Philips?', 'Dengan TV Philips yang menggunakan Roku TV, Google TV atau Android TV, ya, dan dalam beta dengan TV Philips dari 2011 hingga 2015 tanpa Android. Model dengan Titan OS tidak disokong.'),
      ('Adakah Mando TV mengawal Ambilight?', 'Mando TV ialah alat kawalan jauh: ia menghantar butang, jadi anda boleh sampai ke tetapan Ambilight dengan anak panah dan OK. Tiada kawalan Ambilight yang berasingan.'),
      ('Adakah saya perlukan akaun Philips atau Google?', 'Tidak. Mando TV bersambung melalui Wi-Fi rumah anda dan tidak memerlukan akaun.'),
    ]),
]
OTRAS_GUIAS += [
  ('no-sub', 'Aplikasi alat kawalan jauh tanpa langganan dan tanpa iklan'),
  ('roku-app-alt', 'Alternatif aplikasi Roku: satu aplikasi untuk semua TV'),
  ('lg-thinq', 'Alternatif aplikasi LG ThinQ untuk TV LG anda'),
  ('smartthings', 'Alternatif SmartThings untuk TV Samsung'),
  ('googletv-alt', 'Alternatif alat kawalan jauh Google TV pada telefon'),
  ('windows', 'Aplikasi alat kawalan jauh untuk PC Windows'),
  ('iphone', 'Aplikasi alat kawalan jauh untuk iPhone: satu untuk semua TV'),
  ('firetv', 'Alat kawalan jauh Fire TV untuk telefon atau PC anda'),
  ('firetv-lost', 'Alat kawalan jauh Fire TV hilang: cara guna telefon anda'),
  ('turn-on', 'Cara menghidupkan TV tanpa alat kawalan jauh'),
  ('sony', 'Cara mengawal TV Sony anda dengan telefon'),
  ('tcl', 'Cara mengawal TV TCL anda dengan telefon'),
  ('hisense', 'Aplikasi alat kawalan jauh Hisense: apa yang berfungsi dan apa yang tidak'),
  ('philips', 'Kawal TV Philips dengan telefon anda'),
]
# <<< guías traídas del inglés
