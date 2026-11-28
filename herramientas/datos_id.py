# Textos en indonesio (kamu) de mandotv.app. Los usa generar_idiomas.py. Escritos para las búsquedas de Indonesia.
# Las claves de las páginas (lg, lost-tv, ...) y sus rutas están en idiomas_sitio.py.
# Los nombres de menús de cada marca (LG, Samsung, Roku, Android TV, iPhone) son los mismos que usa la app en indonesio
# (lib/l10n/app_id.arb del proyecto de la app).

UI = dict(
  locale='id_ID',
  aria_home='Mando TV, beranda', aria_main='Menu utama', nav_que='Fitur', nav_ayuda='Bantuan', nav_contacto='Kontak',
  asunto='Halo%20Mando%20TV', inicio='Beranda', privacidad='Privasi', aria_pie='Kaki halaman', aria_ruta='Jejak navigasi',
  aria_marcas='Merek dan panduan', hecho='Dibuat di Chili',
  aviso='Mando TV adalah aplikasi independen. Aplikasi ini tidak berafiliasi dengan para produsen TV yang disebutkan maupun dengan Google, Amazon, Apple atau Roku, dan tidak didukung oleh mereka. Merek dagang adalah milik pemiliknya masing-masing dan hanya disebutkan untuk menunjukkan kompatibilitas. Android TV dan Google TV adalah merek dagang Google LLC. Apple TV adalah merek dagang Apple Inc.',
  bajar='Unduh gratis', descarga='Unduh di', anticipada='Akses awal di',
  apple_aria='Unduh Mando TV gratis di App Store', ms_aria='Unduh Mando TV gratis di Microsoft Store',
  gp_aria='Akses awal Mando TV di Google Play untuk Android', aria_desc='Unduh Mando TV',
  b_como_btn='Cara menghubungkan', b_tiendas_label='Tersedia di toko aplikasi',
  b_nota='iPhone, iPad, Mac, Android, dan Windows. Unduh gratis, tanpa iklan. Pro adalah pembelian sekali bayar, tanpa langganan.',
  b_compat='TV yang kompatibel', b_otras='Merek lain', b_otras_p='Mando TV mengontrol semua merek ini dengan satu aplikasi yang sama:',
  g_guias='Panduan', g_ver='Lihat langkah-langkahnya', g_pasos='Langkah demi langkah', g_hazlo='Begini caranya dengan Mando TV',
  g_tiendas='Mando TV adalah remote universal untuk TV kamu. Unduh gratis, tanpa iklan dan tanpa akun. Pro adalah pembelian sekali bayar yang opsional, tanpa langganan. Untuk iPhone, iPad, Windows, dan Android:',
  g_nota='Android: akses awal gratis di Google Play. <a href="{enlace}">Ikuti dalam dua langkah</a> dan bantu kami masuk ke toko aplikasi.',
  g_mas_pagina='Detail lainnya ada di halaman {enlace}.', g_mas_marca='Detail lainnya menurut merek:',
  g_faq='Pertanyaan umum', g_mas='Panduan lainnya', g_todas='Semua panduan', g_ayuda='Bantuan dan dukungan',
  g_idiomas='Panduan ini dalam bahasa lain',
)

# Pie de página y listas de marcas/guías: (clave, texto)
PIE = [
  ('samsung', 'Remote Samsung'),
  ('lg', 'Remote LG'),
  ('roku', 'Remote Roku'),
  ('android', 'Remote Android TV'),
  ('guias', 'Semua panduan'),
  ('lost-tv', 'Remote TV hilang'),
  ('lost-lg', 'Remote LG hilang'),
  ('lg-on', 'Menyalakan TV LG dengan HP'),
  ('hdmi', 'Ganti input HDMI tanpa remote'),
  ('androidtv', 'Android TV tanpa remote'),
  ('console', 'TV dan HDMI konsol tanpa remote'),
  ('samsung-lost', 'TV Samsung tanpa remote'),
  ('roku-lost', 'Remote Roku hilang'),
  ('roku-403', 'Aplikasi Roku tidak berfungsi'),
  ('androidtv-code', 'Kode pemasangan Android TV'),
  ('not-found', 'HP tidak menemukan TV'),
  ('wifi', 'HP jadi remote lewat Wi-Fi'),
  ('pc', 'Kontrol TV dari PC'),
]
NOMBRE_OTRA = {'lg': 'Aplikasi remote LG', 'samsung': 'Aplikasi remote Samsung', 'roku': 'Aplikasi remote Roku',
               'android': 'Aplikasi remote Android TV dan Google TV'}
PAGINA_MARCA = {'lg': 'Aplikasi remote LG', 'samsung': 'Aplikasi remote Samsung', 'roku': 'Aplikasi remote Roku',
                'android': 'Aplikasi remote Android TV'}

OTRAS_GUIAS = [
  ('lg-on', 'Cara menyalakan TV LG dengan HP'),
  ('lost-tv', 'Remote TV hilang: ini yang bisa kamu lakukan'),
  ('lost-lg', 'Remote LG hilang: pakai HP sebagai gantinya'),
  ('hdmi', 'Ganti input HDMI di TV tanpa remote'),
  ('androidtv', 'Android TV tanpa remote: pakai HP kamu'),
  ('console', 'Nyalakan TV dan pindah ke HDMI konsol tanpa remote'),
  ('samsung-lost', 'TV Samsung tanpa remote asli: pakai HP kamu'),
  ('roku-lost', 'Remote Roku hilang: pakai HP kamu'),
  ('roku-403', 'Aplikasi Roku tidak berfungsi: atasi error 403'),
  ('androidtv-code', 'Android TV meminta kode pemasangan: begini caranya'),
  ('not-found', 'HP tidak menemukan TV: ini yang perlu kamu periksa'),
  ('wifi', 'Cara memakai HP sebagai remote lewat Wi-Fi'),
  ('pc', 'Cara mengontrol TV dengan PC Windows'),
]

INDICE = dict(
  titulo='Panduan: kontrol TV dengan HP | Mando TV',
  desc='Panduan langkah demi langkah: pakai HP atau PC sebagai remote TV, nyalakan TV, ganti HDMI, dan atasi masalah di Samsung, LG, Roku.',
  h1='Panduan: pakai HP sebagai remote TV',
  intro='Langkah-langkah mudah untuk menghubungkan remote TV Samsung, LG, Roku, atau Android TV kamu dengan Mando TV, menyalakan TV, dan mengatasi masalah.',
  h2_guias='Semua panduan', h2_marcas='Aplikasi remote menurut merek',
  marcas_extra=[('sony', 'Aplikasi remote Sony'), ('philips', 'Aplikasi remote Philips')],
)

MARCAS = [
  dict(clave='lg', color='#e0457b', corto='LG',
    titulo='Aplikasi remote TV LG di HP, gratis | Mando TV',
    desc='HP atau PC kamu jadi remote TV LG webOS lewat Wi-Fi. Tombol, keyboard, aplikasi, input, dan menyalakan TV gratis; penunjuk dengan Pro.',
    h1='Remote TV LG sebagai aplikasi di HP',
    intro='Mando TV adalah aplikasi remote untuk TV LG: HP atau komputer kamu menjadi remote Smart TV LG webOS lewat Wi-Fi di rumah. Berguna kalau remote hilang, baterainya habis, atau kamu cuma ingin mengetik lebih cepat.',
    compat='Smart TV LG dengan webOS (sebagian besar model Smart TV LG sejak 2014). Berfungsi dengan TV LED, NanoCell, QNED, dan OLED. Smart TV LG lama dengan NetCast (2011 sampai 2014, sebelum webOS) kini didukung dalam versi beta: dipasangkan dengan kunci 6 digit yang ditampilkan TV.',
    h2=dict(funciones='Yang bisa kamu lakukan dengan TV LG', como='Cara menghubungkan TV LG ke Mando TV',
            encender='Menyalakan TV LG dengan HP', preguntas='Pertanyaan tentang LG', guias='Panduan untuk LG'),
    funciones=[
      ('Semua tombol', 'Tombol arah, OK, Kembali, Beranda, volume, saluran, bisukan, dan putar.'),
      ('Penunjuk seperti Magic Remote (Pro)', 'Gerakkan panah di layar dengan jarimu, persis seperti memakai Magic Remote LG.'),
      ('Dua keyboard', 'Ketik di pencarian TV dan di sebagian besar aplikasi dengan keyboard HP kamu. Dengan Keyboard YouTube (Pro), ketik atau ucapkan apa yang mau ditonton, lalu YouTube terbuka di TV dengan hasilnya.'),
      ('Aplikasi dan input', 'Buka aplikasi favoritmu dan pindah ke HDMI, TV langsung, AirPlay, atau Screen Share.'),
      ('Keluaran audio (Pro)', 'Pindah antara speaker TV dan soundbar kamu.'),
      ('Menyalakan TV', 'Kalau TV mati, Mando TV menyalakannya lewat jaringan dan tersambung sendiri.'),
    ],
    pasos=[
      'Hubungkan HP dan TV ke Wi-Fi yang sama.',
      'Buka Mando TV: TV LG kamu muncul sendiri di daftar. Ketuk TV tersebut.',
      'Di TV akan muncul permintaan izin. Setujui dengan remote yang biasa kamu pakai (hanya sekali, saat pertama kali).',
    ],
    encender='Di TV LG, buka Pengaturan dan cari "Nyalakan TV dengan perangkat seluler" (ada di Pengaturan, Umum, Perangkat, Perangkat Eksternal; pada model lama di Koneksi, Manajemen Koneksi Seluler). Aktifkan "Nyalakan lewat Wi-Fi". Kalau ada "Quick Start+", aktifkan juga. Setelah itu, saat kamu mengetuk TV yang sedang mati di Mando TV, aplikasi akan bertanya apakah mau menyalakannya, lalu tersambung sendiri.',
    faq=[
      ('Apakah saya butuh Magic Remote untuk memakai Mando TV?', 'Hanya sekali, saat pertama kali, untuk menyetujui permintaan di layar. Setelah itu HP kamu sudah cukup.'),
      ('Apakah Mando TV menggantikan aplikasi LG ThinQ?', 'Untuk mengontrol TV, ya: kamu tidak butuh akun LG dan tidak perlu mendaftarkan TV. Mando TV tersambung langsung lewat Wi-Fi kamu.'),
      ('Bisakah saya menyalakan TV LG dengan HP?', 'Bisa, kalau di TV kamu sudah mengaktifkan "Nyalakan TV dengan perangkat seluler" dan pernah tersambung satu kali saat TV menyala.'),
      ('Apakah berfungsi dengan TV LG lama sebelum webOS?', 'Dalam versi beta, ya, untuk Smart TV LG NetCast tahun 2011 sampai 2014. TV dipasangkan dengan kunci 6 digit yang ditampilkan di layar. Fitur ini masih baru dan mungkin belum sempurna.'),
    ],
    guias=[('lg-on', 'Cara menyalakan TV LG dengan HP'),
           ('lost-lg', 'Remote LG hilang: pakai HP sebagai gantinya'),
           ('hdmi', 'Ganti input HDMI di TV tanpa remote'),
           ('guias', 'Semua panduan untuk mengontrol TV dengan HP')]),
  dict(clave='samsung', color='#3d7bff', corto='Samsung',
    titulo='Aplikasi remote TV Samsung di HP | Mando TV',
    desc='HP atau PC kamu jadi remote TV Samsung Tizen lewat Wi-Fi. Tombol, keyboard, aplikasi, dan menyalakan TV gratis; touchpad dengan Pro. Tanpa iklan.',
    h1='Remote TV Samsung sebagai aplikasi di HP',
    intro='Mando TV adalah aplikasi remote untuk TV Samsung: HP atau komputer kamu menjadi remote Smart TV Samsung lewat Wi-Fi di rumah. Kamu tidak butuh akun Samsung dan tidak perlu mendaftarkan TV.',
    compat='Smart TV Samsung dengan Tizen, tahun 2016 ke atas (seri seperti Crystal UHD, QLED, Neo QLED, The Frame, dan OLED).',
    h2=dict(funciones='Yang bisa kamu lakukan dengan TV Samsung', como='Cara menghubungkan TV Samsung ke Mando TV',
            encender='Menyalakan TV Samsung dengan HP', preguntas='Pertanyaan tentang Samsung', guias='Panduan untuk Samsung'),
    funciones=[
      ('Semua tombol', 'Tombol arah, OK, Kembali, Beranda, volume, saluran, bisukan, dan sumber.'),
      ('Touchpad (Pro)', 'Geser jari untuk menjelajah menu, tanpa perlu mencari tombol arah.'),
      ('Dua keyboard', 'Ketik di pencarian TV dan di sebagian besar aplikasi dengan keyboard HP kamu. Dengan Keyboard YouTube (Pro), ketik atau ucapkan apa yang mau ditonton, lalu YouTube terbuka di TV dengan hasilnya.'),
      ('Aplikasi', 'Buka Netflix, YouTube, Prime Video, dan aplikasi lainnya dengan satu ketukan.'),
      ('Menyalakan TV', 'Kalau TV mati, Mando TV menyalakannya lewat jaringan dan tersambung sendiri.'),
      ('Tanpa akun', 'Koneksi berjalan langsung lewat Wi-Fi kamu, tanpa melewati internet.'),
    ],
    pasos=[
      'Hubungkan HP dan TV ke Wi-Fi yang sama.',
      'Buka Mando TV: TV Samsung kamu muncul sendiri di daftar. Ketuk TV tersebut.',
      'TV akan bertanya apakah kamu mengizinkan koneksi. Pilih "Izinkan" dengan remote (hanya sekali, saat pertama kali).',
    ],
    encender='Di TV Samsung, buka Pengaturan > Umum > Jaringan > Pengaturan Pakar dan aktifkan "Nyalakan dengan perangkat seluler". Setelah itu, saat kamu mengetuk TV yang sedang mati di Mando TV, aplikasi akan bertanya apakah mau menyalakannya, lalu tersambung sendiri.',
    faq=[
      ('Saya tidak sengaja menolak izin. Apa yang harus dilakukan?', 'Di TV, buka Pengaturan > Umum > Pengelola Perangkat Eksternal > Pengelola Koneksi Perangkat, lalu ubah Mando TV menjadi diizinkan.'),
      ('Apakah Mando TV menggantikan SmartThings?', 'Untuk mengontrol TV, ya, dan tanpa akun Samsung. Mando TV tersambung langsung lewat Wi-Fi kamu.'),
      ('Apakah berfungsi dengan TV Samsung lama?', 'Berfungsi dengan TV Samsung ber-Tizen tahun 2016 ke atas. Model sebelumnya memakai sistem lain yang belum kami dukung.'),
    ],
    guias=[('samsung-lost', 'TV Samsung tanpa remote asli: pakai HP kamu'),
           ('smartthings', 'Alternatif SmartThings untuk TV Samsung'),
           ('turn-on', 'Cara menyalakan TV tanpa remote'),
           ('hdmi', 'Ganti input HDMI di TV tanpa remote'),
           ('guias', 'Semua panduan untuk mengontrol TV dengan HP')]),
  dict(clave='roku', color='#a77bff', corto='Roku',
    titulo='Aplikasi remote Roku di HP, gratis | Mando TV',
    desc='HP atau PC kamu jadi remote Roku TV dan Roku Player lewat Wi-Fi. Tombol, keyboard, kanal, input, dan menyalakan TV gratis.',
    h1='Remote Roku sebagai aplikasi di HP',
    intro='Mando TV adalah aplikasi remote untuk Roku: HP atau komputer kamu menjadi remote Roku lewat Wi-Fi di rumah. Berfungsi dengan perangkat Roku TV dan dengan Roku Player yang dipasang ke port HDMI.',
    compat='Perangkat Roku TV (TCL, Hisense, Philips, Sharp, JVC, dan lainnya) dan Roku Player (Express, Streaming Stick, Ultra).',
    h2=dict(funciones='Yang bisa kamu lakukan dengan Roku', como='Cara menghubungkan Roku ke Mando TV',
            encender='Menyalakan Roku dengan HP', preguntas='Pertanyaan tentang Roku', guias='Panduan untuk Roku'),
    funciones=[
      ('Semua tombol', 'Tombol arah, OK, Kembali, Beranda, volume, bisukan, ulangi, dan putar.'),
      ('Dua keyboard', 'Ketik di pencarian Roku dan di kanal yang mendukungnya dengan keyboard HP kamu. Dengan Keyboard YouTube (Pro), ketik atau ucapkan apa yang mau ditonton, lalu YouTube terbuka di TV dengan hasilnya.'),
      ('Kanal', 'Buka Netflix, YouTube, dan kanal Roku lainnya dengan satu ketukan.'),
      ('Input', 'Di Roku TV, pindah ke HDMI, antena, atau AV langsung dari aplikasi.'),
      ('Menyalakan TV', 'Di perangkat Roku TV dengan Quick Start, Mando TV menyalakannya dari HP kamu.'),
      ('Tanpa pemasangan', 'Roku tidak meminta kode: ketuk di daftar dan kamu langsung tersambung.'),
      ('Bunyikan remote', 'Kalau remote Roku kamu punya speaker, misalnya Roku Voice Remote Pro, Mando TV akan membunyikannya supaya mudah ditemukan. Gratis, dan Roku harus menyala.'),
    ],
    pasos=[
      'Hubungkan HP dan Roku ke Wi-Fi yang sama.',
      'Buka Mando TV: Roku kamu muncul sendiri di daftar. Ketuk Roku tersebut.',
      'Kalau koneksi gagal, di Roku buka Pengaturan > Sistem > Pengaturan sistem lanjutan > Kontrol oleh aplikasi seluler, lalu atur akses jaringan ke Default atau Permissive (pada software Roku yang lebih baru, atur "Kontrol oleh aplikasi seluler" ke Diaktifkan).',
    ],
    encender='Di perangkat Roku TV, aktifkan "Quick Start TV" di Pengaturan > Sistem > Daya. Roku Player yang dipasang ke TV lain tidak bisa dinyalakan dengan cara ini. Setelah itu, saat kamu mengetuk TV yang sedang mati di Mando TV, aplikasi akan bertanya apakah mau menyalakannya, lalu tersambung sendiri.',
    faq=[
      ('Apakah berfungsi dengan Roku Express atau Streaming Stick?', 'Ya. Semua Roku Player dan perangkat Roku TV dikontrol dengan cara yang sama.'),
      ('Mando TV tidak menemukan Roku saya. Apa yang harus dilakukan?', 'Pastikan keduanya di Wi-Fi yang sama dan "Kontrol oleh aplikasi seluler" di Roku tidak dimatikan. Kamu juga bisa menambahkannya lewat alamat IP.'),
      ('Apakah saya butuh akun Roku?', 'Tidak. Mando TV tersambung langsung lewat Wi-Fi kamu.'),
    ],
    guias=[('roku-403', 'Aplikasi Roku tidak berfungsi (error 403)'),
           ('roku-lost', 'Remote Roku hilang: pakai HP kamu'),
           ('tcl', 'Aplikasi remote TCL'),
           ('hisense', 'Aplikasi remote Hisense'),
           ('philips', 'Aplikasi remote Philips'),
           ('guias', 'Semua panduan untuk mengontrol TV dengan HP')]),
  dict(clave='android', color='#2fbf8f', corto='Android TV dan Google TV',
    titulo='Aplikasi Remote Google TV dan Android TV | Mando TV',
    desc='Remote Google TV dan Android TV (Sony, TCL, Xiaomi) di HP atau PC lewat Wi-Fi. Tombol, keyboard, aplikasi, dan menyalakan TV gratis; touchpad dengan Pro.',
    h1='Remote Google TV dan Android TV sebagai aplikasi di HP',
    intro='Mando TV adalah aplikasi remote untuk Android TV: HP atau komputer kamu menjadi remote TV Android TV atau Google TV lewat Wi-Fi di rumah. Berfungsi juga dari iPhone dan Windows.',
    compat='TV dengan Google TV atau Android TV dari Sony, Philips, TCL, Hisense, Sharp, Xiaomi, Toshiba, Panasonic, Haier, Skyworth, JVC, Thomson, Motorola, OnePlus, iFFALCON, Kogan, Vu, dan merek lainnya, ditambah Chromecast with Google TV, Google TV Streamer, onn., dan Nvidia Shield. Beberapa merek ini juga menjual model dengan sistem lain: kalau TV kamu menampilkan layar utama Google TV atau punya Google Play Store, Mando TV bisa mengontrolnya.',
    h2=dict(funciones='Yang bisa kamu lakukan dengan Android TV', como='Cara menghubungkan Android TV ke Mando TV',
            encender='Menyalakan Android TV dengan HP', preguntas='Pertanyaan tentang Android TV', guias='Panduan untuk Android TV'),
    funciones=[
      ('Semua tombol', 'Tombol arah, OK, Kembali, Beranda, volume, bisukan, dan putar.'),
      ('Touchpad (Pro)', 'Geser jari untuk berpindah cepat di menu Google TV.'),
      ('Dua keyboard', 'Ketik di pencarian TV dan di sebagian besar aplikasi dengan keyboard HP kamu. Dengan Keyboard YouTube (Pro), ketik atau ucapkan apa yang mau ditonton, lalu YouTube terbuka di TV dengan hasilnya.'),
      ('Aplikasi', 'Buka YouTube, Netflix, Disney+, dan aplikasi lainnya dengan satu ketukan.'),
      ('Menyalakan TV', 'Di model yang bisa dinyalakan lewat jaringan, Mando TV menyalakan TV dan tersambung sendiri.'),
      ('iPhone, Android, dan PC', 'Berfungsi sama di HP dan komputer mana pun.'),
    ],
    pasos=[
      'Hubungkan HP dan TV ke Wi-Fi yang sama.',
      'Buka Mando TV: Android TV kamu muncul sendiri di daftar. Ketuk TV tersebut.',
      'TV menampilkan kode 6 karakter. Masukkan kode itu di Mando TV (hanya sekali, saat pertama kali).',
    ],
    encender='Ini tergantung produsennya. Cari "Wake on LAN", "Nyalakan lewat jaringan", "Siaga jaringan", atau "Remote start" di pengaturan jaringan atau daya. Beberapa model tidak punya opsi ini. Setelah itu, saat kamu mengetuk TV yang sedang mati di Mando TV, aplikasi akan bertanya apakah mau menyalakannya, lalu tersambung sendiri.',
    faq=[
      ('Apakah berfungsi dengan Chromecast with Google TV?', 'Ya, pemasangannya lewat kode 6 karakter yang muncul di layar.'),
      ('Apa bedanya dengan aplikasi Google TV?', 'Mando TV tidak butuh akun Google, berfungsi juga di Windows, dan mengontrol TV LG, Samsung, dan Roku dengan satu aplikasi yang sama.'),
      ('Kode tidak muncul di layar. Apa yang harus dilakukan?', 'Tutup Mando TV, buka lagi, lalu ketuk TV sekali lagi. Pastikan TV tidak berada dalam mode hemat daya yang dalam.'),
    ],
    guias=[('androidtv-code', 'Android TV meminta kode pemasangan: begini caranya'),
           ('androidtv', 'Android TV tanpa remote: pakai HP kamu'),
           ('googletv-alt', 'Alternatif remote Google TV di HP'),
           ('sony', 'Aplikasi remote Sony'),
           ('tcl', 'Aplikasi remote TCL'),
           ('hisense', 'Aplikasi remote Hisense'),
           ('philips', 'Aplikasi remote Philips'),
           ('guias', 'Semua panduan untuk mengontrol TV dengan HP')]),
]

GUIAS = [
  dict(clave='lost-tv', corto='Remote TV hilang',
    titulo='Remote TV hilang? Kontrol TV dengan HP',
    desc='Remote TV hilang? Nyalakan TV dari tombol di badan TV dan pakai HP sebagai remote. Langkah untuk LG, Samsung, Roku, Android TV. Gratis.',
    h1='Remote TV hilang? Ini yang bisa kamu lakukan sekarang',
    intro='Remote hilang itu hal biasa di setiap rumah: selalu lenyap tepat saat kamu mau menonton. Kabar baiknya, HP kamu bisa menggantikan remote lewat Wi-Fi di rumah. Berikut urutan yang bisa kamu coba.',
    pasos=[
      'Nyalakan TV dengan tombol di badan TV. Hampir selalu ada di bagian bawah tengah atau di belakang dekat salah satu sudut. Kadang berupa satu tombol, kadang joystick kecil.',
      'Hubungkan HP kamu ke Wi-Fi yang sama dengan TV.',
      'Unduh Mando TV, yang gratis dan tidak meminta akun, lalu buka aplikasinya. TV kamu muncul sendiri di daftar. Ketuk TV tersebut.',
      'Setujui koneksi sesuai merek TV kamu. Di LG dan Samsung, TV menampilkan permintaan: setujui dengan tombol atau joystick di TV itu sendiri. Di Android TV dan Google TV, kamu memasukkan kode 6 karakter yang muncul di layar. Roku tidak meminta apa pun.',
      'Selesai. Tombol arah, OK, Kembali, Beranda, volume, saluran, dan keyboard semuanya gratis.',
      'Untuk lain kali: aktifkan fitur menyalakan lewat jaringan di pengaturan TV (panduan untuk merek kamu ada di bawah). Dengan begitu kamu bisa menyalakan TV dari HP tanpa menyentuhnya.',
    ],
    extra=[
      ('Pilih panduan untuk merek kamu', 'LG: [Remote LG hilang](@lost-lg). Android TV dan Google TV: [Android TV tanpa remote](@androidtv). Samsung: [TV Samsung tanpa remote](@samsung-lost). Roku: [Remote Roku hilang](@roku-lost).'),
      ('Kalau TV tidak mau menyala dengan tombolnya', 'Sebelum mencari remote lain, pastikan kabel tercolok dengan benar dan stopkontak ada listriknya. Kalau tombol di TV tidak melakukan apa-apa, masalahnya ada di TV, bukan di remote.'),
      ('Kalau remote tiba-tiba tidak berfungsi', 'Coba ganti baterai. Untuk memeriksa apakah remote masih mengirim sinyal, arahkan ke kamera HP lalu tekan satu tombol: di banyak HP kamu akan melihat cahaya keunguan di layar. Kalau cahayanya terlihat tapi TV tidak bereaksi, mungkin sensor di TV tertutup.'),
      ('Kalau kamu ganti router dan TV tidak punya Wi-Fi lagi', 'Tanpa remote, lebih sulit menghubungkan TV ke jaringan baru. Cara termudah adalah mencolokkan TV ke router dengan kabel jaringan. Kamu juga bisa membuat Wi-Fi dengan nama dan kata sandi yang sama seperti sebelumnya: TV biasanya tersambung sendiri.'),
      ('Apa yang gratis dan apa yang Pro', 'Menyalakan dan mematikan TV, tombol arah, OK, volume, saluran, tombol angka, keyboard, membuka aplikasi, dan mengganti input semuanya gratis. Touchpad, suara, dan rutinitas adalah bagian dari Mando TV Pro, pembelian sekali bayar tanpa langganan.'),
    ],
    marca=None,
    faq=[
      ('Bisakah saya menyalakan TV dengan HP kalau belum pernah menyambungkannya?', 'Pertama kali, nyalakan dengan tombol di TV. Setelah HP tersambung dan kamu mengaktifkan fitur menyalakan lewat jaringan di pengaturan TV, kamu bisa menyalakannya dari aplikasi.'),
      ('Apakah saya harus membeli remote baru?', 'Belum tentu. Dengan Mando TV, tombol, volume, keyboard, dan menyalakan TV gratis. Kalau kamu tetap lebih suka remote fisik, cari sesuai model TV kamu.'),
      ('Apakah berfungsi kalau TV tidak punya Wi-Fi?', 'Biasanya tidak. HP dan TV umumnya harus berada di Wi-Fi yang sama. Pengecualiannya adalah inframerah pada HP Android dengan pemancar inframerah, yang juga bisa mengontrol TV yang bukan Smart TV, dan Bluetooth di versi beta mulai Android 9, yang berfungsi tanpa Wi-Fi sama sekali dengan Google TV, Android TV, dan Fire TV.'),
    ]),
  dict(clave='lost-lg', corto='Remote LG hilang',
    titulo='Remote LG hilang? Pakai HP kamu',
    desc='Tidak punya remote LG? Nyalakan TV dari badan TV, setujui permintaan di layar, lalu pakai HP lewat Wi-Fi. Tanpa akun LG, tanpa iklan.',
    h1='Remote LG hilang? Begini cara memakai HP kamu',
    intro='Kalau remote LG kamu hilang atau Magic Remote tidak berfungsi lagi, HP kamu bisa menggantikannya lewat Wi-Fi. Ini berfungsi di TV LG dengan webOS, yaitu hampir semua Smart TV LG sejak 2014. Kamu tidak butuh akun LG maupun aplikasi ThinQ.',
    pasos=[
      'Nyalakan TV dengan tombol di bagian bawah di bawah logo LG atau tombol di bagian belakang. Di banyak model tombol itu berupa joystick: tekan untuk membuka menu dan gerakkan untuk memilih.',
      'Hubungkan HP kamu ke Wi-Fi yang sama dengan TV.',
      'Buka Mando TV dan ketuk TV LG kamu di daftar.',
      'TV menampilkan permintaan izin. Setujui dengan joystick atau tombol di TV. Kalau HP ini sudah pernah tersambung, TV tidak akan bertanya lagi.',
      'Selesai. Tombol arah, OK, Kembali, Beranda, volume, saluran, dan keyboard gratis. Penunjuk adalah fitur Pro.',
      'Dengan aplikasi tersambung, buka pengaturan memakai tombol arah dan OK, lalu aktifkan "Nyalakan TV dengan perangkat seluler". Panduan [Cara menyalakan TV LG dengan HP](@lg-on) menunjukkan di mana opsi itu berada.',
    ],
    extra=[
      ('Kalau TV tidak menampilkan permintaan izin', 'Mungkin izinnya sudah tersimpan atau HP kamu berada di jaringan lain. Pastikan keduanya di Wi-Fi yang sama dan VPN dimatikan. Kalau TV tidak muncul di daftar, baca [HP tidak menemukan TV](@not-found).'),
      ('Kalau TV kehilangan Wi-Fi', 'Colokkan TV ke router dengan kabel jaringan, maka TV akan memakainya sendiri. Atau buat Wi-Fi dengan nama dan kata sandi yang sama seperti sebelumnya, karena TV biasanya tersambung sendiri.'),
      ('Kalau TV tersangkut di input lain', 'Di HP, ketuk Input dan pilih port HDMI. Selengkapnya ada di [Ganti input HDMI di TV tanpa remote](@hdmi).'),
    ],
    marca='lg',
    faq=[
      ('Apakah saya butuh Magic Remote untuk memakai Mando TV?', 'Kamu hanya butuh sesuatu untuk menyetujui permintaan saat pertama kali, dan tombol atau joystick di TV sudah cukup. Setelah itu kamu hanya memakai HP.'),
      ('Apakah saya butuh aplikasi LG ThinQ?', 'Tidak. Mando TV tersambung langsung lewat Wi-Fi kamu dan tidak meminta akun LG.'),
      ('Bisakah saya mematikan dan menyalakan TV LG dengan HP?', 'Mematikan bisa. Untuk menyalakan, kamu harus sudah mengaktifkan "Nyalakan TV dengan perangkat seluler" di TV dan pernah tersambung satu kali saat TV menyala.'),
    ]),
  dict(clave='hdmi', corto='Ganti HDMI tanpa remote',
    titulo='Ganti input HDMI tanpa remote (Samsung, LG, Roku)',
    desc='Ganti input HDMI tanpa remote di Samsung, LG, atau Roku: lewat tombol di TV atau lewat HP. Gratis, tanpa iklan.',
    h1='Cara mengganti input HDMI di TV tanpa remote',
    intro='Konsol atau streaming player sudah siap, tapi TV tersangkut di input lain dan remote entah ke mana. Untuk mengganti input HDMI tanpa remote ada dua cara: tombol di TV itu sendiri atau HP kamu. Berikut langkah untuk Samsung, LG, dan Roku.',
    pasos=[
      'Coba yang paling mudah dulu: nyalakan konsol atau player. Kalau HDMI-CEC aktif di TV (di Samsung namanya Anynet+, di LG SIMPLINK), TV akan pindah sendiri ke input itu.',
      'Kalau tidak pindah, pakai tombol di TV itu sendiri, di bagian bawah tengah atau di belakang. Di banyak TV Samsung dan LG tombol itu berupa joystick yang membuka menu dengan Sumber atau Input.',
      'Di menu itu pilih inputnya: HDMI 1, HDMI 2, dan seterusnya. Nomornya adalah port tempat kabel tercolok.',
      'Kalau kamu lebih suka memakai HP, hubungkan ke Wi-Fi yang sama, buka Mando TV, lalu ketuk TV kamu.',
      'Di LG dan Roku, ketuk Input lalu pilih port HDMI. Di Samsung, Input mengirim tombol Sumber ke TV, lalu kamu memilih dengan tombol arah dan OK.',
      'Kamu juga bisa menuju input dengan tombol arah dan OK dari layar utama TV. Tergantung merek dan tahun, namanya Sumber, Perangkat terhubung, atau Input. Di Roku TV, itu berupa kotak HDMI di layar utama.',
    ],
    extra=[
      ('Samsung', 'Kalau menu tombol di TV tidak punya pilihan Sumber, buka menu layar utama dari HP dan cari Sumber atau Perangkat terhubung di sebelah kiri. Kamu mengontrolnya dengan tombol arah dan OK di Mando TV, yang gratis.'),
      ('LG', 'Tekan joystick di TV dan cari Input. Dari HP, kamu juga bisa membuka daftar input di Mando TV dan mengetuk input yang diinginkan.'),
      ('Roku TV', 'Di layar utama ada kotak untuk setiap input, misalnya HDMI 1 atau HDMI 2. Bergeraklah dengan tombol arah dan buka dengan OK, gratis.'),
      ('Kalau TV kamu memakai Android TV atau Google TV', 'Di Mando TV belum ada daftar input untuk Android TV. Pakai tombol input di TV itu sendiri atau capai input dengan tombol arah dan OK dari layar utama. Kalau kamu tidak punya remote dan ingin menyambungkan HP, baca [Android TV tanpa remote](@androidtv).'),
      ('Bantuan lainnya', 'Kalau TV sama sekali tidak mau menyala atau kamu tidak tahu harus mulai dari mana, baca [Remote TV hilang](@lost-tv). Untuk bermain di konsol, panduan [Nyalakan TV dan pindah ke HDMI konsol tanpa remote](@console) berisi trik HDMI-CEC.'),
    ],
    marca=None,
    faq=[
      ('Apakah mengganti input HDMI gratis?', 'Ya. Daftar input di Mando TV gratis, begitu juga menyalakan TV serta tombol arah, OK, dan volume. Kamu juga bisa membuka input dari menu TV.'),
      ('Bagaimana saya tahu input HDMI mana yang harus dipilih?', 'Lihat port HDMI di TV: masing-masing punya nomor. Pilih yang kabel konsol atau player kamu tercolok.'),
      ('Bagaimana kalau TV tidak mau menyala?', 'Nyalakan dengan tombol di badan TV. Kalau kamu pernah menyambungkannya dan mengaktifkan fitur menyalakan lewat jaringan, kamu juga bisa menyalakannya dari HP.'),
    ]),
  dict(clave='androidtv', corto='Android TV tanpa remote',
    titulo='Android TV tanpa remote: pakai HP kamu',
    desc='Tidak punya remote Android TV atau Google TV? Hubungkan HP dengan kode 6 karakter di layar. Gratis, tanpa akun, tanpa iklan.',
    h1='Android TV tanpa remote: begini cara memakai HP kamu',
    intro='Kalau remote Android TV atau Google TV kamu hilang atau baterainya habis, HP kamu bisa menggantikannya. Yang terbaik: untuk menyambungkan kamu tidak butuh remote, karena TV menampilkan kode di layar dan kamu tinggal mengetiknya di HP. Berfungsi di TV Sony, Philips, TCL, Hisense, Sharp, dan Xiaomi dengan Android TV, di Chromecast with Google TV, dan di Nvidia Shield.',
    pasos=[
      'Nyalakan TV dengan tombol di badan TV. Hampir selalu ada di bagian bawah tengah atau di belakang dekat salah satu sudut.',
      'Hubungkan HP kamu ke Wi-Fi yang sama dengan TV.',
      'Unduh Mando TV, yang gratis dan tidak meminta akun Google, lalu buka aplikasinya. Ketuk TV kamu di daftar.',
      'TV menampilkan kode berisi 6 huruf dan angka. Ketik di HP kamu lalu ketuk Pasangkan. Untuk ini kamu tidak butuh remote.',
      'Sekarang kamu bisa memakai tombol arah, OK, Kembali, Beranda, volume, bisukan, dan keyboard. Semuanya gratis, begitu juga daftar aplikasi. Touchpad adalah fitur Pro.',
      'Agar lain kali TV bisa dinyalakan dari HP, cari "Wake on LAN", "Nyalakan lewat jaringan", "Siaga jaringan", atau "Remote start" di pengaturan jaringan atau daya.',
    ],
    extra=[
      ('Kalau TV kamu tidak bisa dinyalakan dari HP', 'Tidak semua Android TV bisa dinyalakan lewat jaringan; itu tergantung produsen dan model. Kalau TV kamu tidak punya fitur ini, nyalakan dengan tombol di TV lalu lanjutkan dari HP. Untuk mematikan, kamu bisa memakai aplikasi.'),
      ('Chromecast with Google TV, Google TV Streamer, dan Shield', 'Semuanya tersambung dengan cara yang sama: Wi-Fi yang sama, ketuk perangkat di daftar, lalu masukkan kode. Kalau TV menampilkan input lain, pindahkan ke port HDMI tempat perangkat itu tercolok, seperti dijelaskan di [Ganti input HDMI di TV tanpa remote](@hdmi).'),
      ('Kalau kode tidak muncul atau dibilang salah', 'Pastikan TV benar-benar menyala dan tidak dalam mode siaga. Kode berubah setiap kali diminta: hanya yang terakhir yang berlaku. Detail lengkapnya ada di [Android TV meminta kode pemasangan](@androidtv-code).'),
      ('Aplikasi Google atau Mando TV', 'Google punya aplikasi sendiri, dan kamu butuh akun Google untuk memakainya. Mando TV tidak meminta akun, berfungsi juga di Windows, dan mengontrol TV LG, Samsung, dan Roku dengan satu aplikasi yang sama.'),
    ],
    marca='android',
    faq=[
      ('Apakah saya butuh remote untuk memasangkan HP?', 'Tidak. Kode muncul di layar TV dan kamu mengetiknya di HP. Kamu hanya perlu menyalakan TV, kalau perlu dengan tombol di badan TV.'),
      ('Apakah berfungsi dengan Hisense?', 'Di TV Hisense dengan Android TV atau Google TV, ya. TV Hisense dengan sistem lain tidak kompatibel.'),
      ('Bisakah saya mengetik dengan keyboard HP?', 'Bisa, ada dua. Keyboard gratis mengetik di pencarian dan kolom teks TV serta sebagian besar aplikasi. YouTube dan Netflix hanya menerima keyboard di layarnya sendiri, jadi untuk YouTube ada Keyboard YouTube (Pro): ketik atau ucapkan apa yang mau kamu tonton, lalu YouTube terbuka di TV dengan hasilnya. Netflix dipakai dengan tombol arah dan OK.'),
    ]),
  dict(clave='lg-on', corto='Menyalakan TV LG dengan HP',
    titulo='Cara menyalakan TV LG dengan HP (panduan)',
    desc='Nyalakan TV LG lewat Wi-Fi dengan HP: aktifkan "Nyalakan TV dengan perangkat seluler" dan pakai Mando TV. Langkah demi langkah, gratis.',
    h1='Cara menyalakan TV LG dengan HP',
    intro='Kamu bisa menyalakan TV LG dengan HP, tapi sebelumnya harus mengaktifkan satu pengaturan di TV. Setelah itu HP kamu menyalakan TV LG lewat Wi-Fi, tanpa remote sama sekali. Butuh lima menit dan hanya dilakukan satu kali.',
    pasos=[
      'Hubungkan HP dan TV LG ke Wi-Fi yang sama.',
      'Di TV, buka Pengaturan dan cari "Nyalakan TV dengan perangkat seluler". Ada di Pengaturan, Umum, Perangkat, Perangkat Eksternal (pada model lama di Koneksi, Manajemen Koneksi Seluler).',
      'Aktifkan "Nyalakan lewat Wi-Fi". Kalau TV kamu tersambung dengan kabel jaringan, aktifkan opsi untuk kabel.',
      'Kalau TV kamu punya "Quick Start+", aktifkan juga.',
      'Dengan TV menyala, buka Mando TV di HP dan ketuk TV LG kamu di daftar. Setujui permintaan yang muncul di layar. Dengan begitu aplikasi belajar cara membangunkannya.',
      'Matikan TV lalu coba: ketuk TV di Mando TV, dan aplikasi akan bertanya apakah kamu mau menyalakannya.',
    ],
    extra=[
      ('Kalau TV tidak menyala', 'TV harus berada di Wi-Fi yang sama saat dimatikan. Pastikan pengaturannya masih aktif dan HP kamu berada di jaringan yang sama. Kalau kamu ganti router, sambungkan lagi saat TV menyala.'),
    ],
    marca='lg',
    faq=[
      ('Bisakah saya menyalakan TV LG dengan HP kalau belum pernah menyambungkannya?', 'Tidak. Pertama, kamu harus mengaktifkan "Nyalakan TV dengan perangkat seluler" di TV dan tersambung satu kali dengan Mando TV saat TV menyala.'),
      ('Apakah saya butuh aplikasi LG ThinQ?', 'Tidak. Mando TV tersambung langsung lewat Wi-Fi kamu dan tidak meminta akun LG.'),
      ('Apakah berfungsi dengan data seluler?', 'Tidak. HP dan TV harus berada di Wi-Fi yang sama.'),
    ]),
  dict(clave='console', corto='TV dan konsol tanpa remote',
    titulo='Tanpa remote? Nyalakan TV dan ganti HDMI',
    desc='Hari rilis game dan remote hilang? Nyalakan TV dan pindah ke input HDMI PS5 atau Xbox kamu dengan HP. Gratis, tanpa iklan.',
    h1='Cara menyalakan TV dan pindah ke input HDMI konsol tanpa remote',
    intro='Hari rilis GTA VI, konsol sudah siap, dan remote entah menghilang di sela-sela bantal sofa. Ini lebih sering terjadi daripada yang kamu kira. Dengan Mando TV, HP kamu menyalakan TV dan pindah ke input PlayStation atau Xbox lewat Wi-Fi di rumah.',
    pasos=[
      'Hubungkan HP kamu ke Wi-Fi yang sama dengan TV.',
      'Buka Mando TV dan ketuk TV kamu di daftar (Samsung, LG, Roku, atau Android TV).',
      'Kalau TV mati, ketuk Nyalakan. Ini berhasil kalau di TV sudah diaktifkan fitur menyalakan lewat jaringan. Kalau belum pernah mengaktifkannya, nyalakan TV kali ini dengan tombol di badan TV, lalu aktifkan untuk lain kali.',
      'Nyalakan konsol. Kalau HDMI-CEC aktif (lihat trik gratis di bawah), TV pindah sendiri ke inputnya.',
      'Kalau tidak pindah, ketuk Input di Mando TV dan pilih port HDMI tempat konsol tercolok: HDMI 1, HDMI 2, dan seterusnya.',
      'Untuk volume saat bermain, pakai tombol besar di aplikasi.',
    ],
    extra=[
      ('Trik gratisnya: biarkan konsol yang memindahkan TV', 'PS5 dan Xbox bisa menyalakan TV dan langsung melompat ke input HDMI-nya saat dinyalakan, berkat HDMI-CEC. Di PS5, ada di Pengaturan > Sistem > HDMI > Aktifkan Tautan Perangkat HDMI. Di Xbox, buka Pengaturan > Umum > Opsi TV & tampilan dan cari opsi kontrol perangkat. Di TV, fitur ini namanya berbeda tergantung merek: Anynet+ di Samsung, SIMPLINK di LG, dan BRAVIA Sync atau Kontrol HDMI di merek lain.'),
      ('Kalau TV tetap menampilkan gambar lain', 'Kalau konsol menyala tapi TV masih menampilkan antena atau sebuah aplikasi, berarti TV belum pindah input. Di HP, ketuk Input dan pilih input HDMI konsol. Atau pakai tombol arah dan OK untuk menuju input TV, atau tombol di TV itu sendiri, lalu pilih port HDMI. Nomornya adalah port tempat kamu mencolokkan kabel konsol.'),
      ('Kalau TV kamu Roku TV', 'Tombol di TV, biasanya di bagian bawah tengah atau di belakang, menyalakannya. Dari sana HP kamu melakukan sisanya.'),
    ],
    marca=None,
    faq=[
      ('Apakah Mando TV ada hubungannya dengan GTA VI?', 'Tidak. Mando TV tidak berafiliasi dengan Rockstar Games maupun Take-Two. Aplikasi ini hanya membantu kamu supaya tidak kehilangan waktu bermain karena remote tidak ketemu.'),
      ('Apakah mengganti input HDMI gratis?', 'Ya. Daftar input di Mando TV gratis, begitu juga menyalakan TV serta tombol arah, OK, dan volume. Kamu juga bisa membiarkan konsol memindahkan input sendiri dengan HDMI-CEC.'),
      ('Apakah berfungsi dengan TV saya?', 'Berfungsi dengan TV Samsung, LG, Roku, dan Android TV di Wi-Fi yang sama. Kalau TV kamu merek lain, trik HDMI-CEC tetap bisa membantu.'),
      ('Bisakah saya memakainya untuk bermain GTA VI (GTA 6) di PS5 atau Xbox?', 'Mando TV tidak ikut campur dengan konsol maupun game. Aplikasi ini hanya memastikan TV menyala dan berada di input HDMI yang benar, supaya kamu tinggal duduk dan bermain.'),
    ]),
  dict(clave='samsung-lost', corto='TV Samsung tanpa remote',
    titulo='Remote Samsung hilang? Pakai HP kamu',
    desc='Remote Samsung hilang atau rusak? Pakai HP sebagai remote lewat Wi-Fi untuk TV Tizen. Mudah dengan Mando TV, gratis, tanpa iklan.',
    h1='TV Samsung tanpa remote asli: begini cara memakai HP kamu',
    intro='Kalau remote Samsung kamu hilang atau tidak berfungsi lagi, kamu bisa memakai HP sebagai remote lewat Wi-Fi. Berfungsi di TV Samsung dengan Tizen, tahun 2016 ke atas.',
    pasos=[
      'Nyalakan TV dengan tombol di badan TV. Di sebagian besar model ada di bagian bawah atau di belakang, kadang berupa joystick kecil.',
      'Pastikan TV tersambung ke Wi-Fi kamu dan HP berada di jaringan yang sama.',
      'Buka Mando TV di HP. TV Samsung kamu muncul sendiri di daftar. Ketuk TV tersebut.',
      'TV meminta kamu menyetujui koneksi. Di sebagian besar model, kamu menyetujuinya dengan tombol di TV atau dengan joystick di bagian belakang.',
      'Selesai, sekarang kamu bisa memakai HP sebagai remote. Tombol, keyboard, dan aplikasi gratis; touchpad adalah fitur Pro.',
      'Agar lain kali TV bisa dinyalakan dari HP, buka Pengaturan > Umum > Jaringan > Pengaturan Pakar dan aktifkan "Nyalakan dengan perangkat seluler".',
    ],
    extra=[
      ('Kalau TV tidak meminta izin', 'Mungkin izinnya sudah tersimpan atau TV berada di Wi-Fi lain. Tutup Mando TV dan buka lagi saat TV menyala. Kalau TV kamu lebih lama dari 2016, TV itu memakai sistem lain yang belum didukung.'),
      ('Kalau kamu tidak sengaja menolak izin', 'Di TV, buka Pengaturan > Umum > Pengelola Perangkat Eksternal > Pengelola Koneksi Perangkat dan ubah Mando TV menjadi diizinkan. Kalau HP tetap tidak menemukan TV, baca [HP tidak menemukan TV](@not-found).'),
    ],
    marca='samsung',
    faq=[
      ('Bagaimana cara menyetujui koneksi kalau saya tidak punya remote?', 'Di sebagian besar model, kamu menyetujuinya dengan tombol di TV atau dengan joystick di bagian belakang. Kalau model kamu tidak punya tombol, tulis ke hola@mandotv.app dan kami bantu.'),
      ('Apakah Mando TV meminta akun Samsung?', 'Tidak. Koneksi berjalan langsung lewat Wi-Fi kamu, tanpa akun Samsung.'),
      ('Apakah berfungsi dengan TV Samsung lama saya?', 'Berfungsi dengan TV Samsung ber-Tizen tahun 2016 ke atas.'),
    ]),
  dict(clave='wifi', corto='HP jadi remote lewat Wi-Fi',
    titulo='HP jadi remote TV: kontrol TV lewat Wi-Fi',
    desc='Hubungkan HP ke TV lewat Wi-Fi dan pakai sebagai remote TV Samsung, LG, Roku, dan Google TV. Langkah per merek dengan Mando TV. Gratis.',
    h1='Cara menghubungkan HP ke TV lewat Wi-Fi sebagai remote',
    intro='Kamu hanya butuh HP dan TV di Wi-Fi yang sama, ditambah aplikasi remote. Mando TV menemukan TV kamu sendiri dan berfungsi dengan Samsung, LG, Roku, Google TV, dan Android TV.',
    pasos=[
      'Hubungkan HP dan TV ke Wi-Fi yang sama.',
      'Buka Mando TV. TV kamu muncul sendiri di daftar. Ketuk TV tersebut.',
      'Setujui koneksi sesuai merek TV kamu (detailnya ada di bawah).',
      'Kontrol TV dengan tombol atau dengan keyboard HP. Touchpad adalah fitur Pro.',
    ],
    extra=[
      ('Samsung', 'TV bertanya apakah kamu mengizinkan koneksi. Setujui saat pertama kali di layar. Berfungsi dengan Tizen tahun 2016 ke atas. Agar bisa dinyalakan dari HP, aktifkan "Nyalakan dengan perangkat seluler" di Pengaturan > Umum > Jaringan > Pengaturan Pakar.'),
      ('LG', 'TV menampilkan permintaan izin. Setujui saat pertama kali. Agar bisa dinyalakan dari HP, cari "Nyalakan TV dengan perangkat seluler" di pengaturan dan aktifkan "Nyalakan lewat Wi-Fi".'),
      ('Roku', 'Roku tidak meminta pemasangan: ketuk di daftar dan kamu langsung tersambung. Agar bisa dinyalakan, aktifkan "Quick Start TV" di Pengaturan > Sistem > Daya.'),
      ('Google TV dan Android TV', 'TV menampilkan kode di layar. Masukkan di Mando TV saat pertama kali. Agar bisa dinyalakan, cari "Wake on LAN", "Nyalakan lewat jaringan", atau "Siaga jaringan" di pengaturan.'),
    ],
    marca=None,
    faq=[
      ('Apakah saya butuh internet untuk memakai HP sebagai remote?', 'Kamu butuh HP dan TV di Wi-Fi yang sama. Mando TV tersambung langsung ke TV kamu lewat jaringan itu.'),
      ('Kenapa TV saya tidak muncul di daftar?', 'Pastikan TV menyala dan HP kamu tidak memakai data seluler atau Wi-Fi lain. Beberapa router punya jaringan tamu yang memisahkan perangkat satu sama lain.'),
      ('Bisakah saya memakai Mando TV di iPhone atau HP Android?', 'Di iPhone dan iPad, ya: aplikasinya sudah ada di App Store. Untuk Windows, ada juga di Microsoft Store. Android segera hadir: kamu bisa ikut akses awal gratis di Google Play.'),
    ]),
  dict(clave='pc', corto='Kontrol TV dari PC',
    titulo='Kontrol TV dengan PC Windows (gratis)',
    desc='Pakai PC Windows sebagai remote TV Samsung, LG, Roku, atau Google TV lewat Wi-Fi. Tombol, keyboard, dan aplikasi gratis; pintasan PC dengan Pro.',
    h1='Cara mengontrol TV dengan PC Windows',
    intro='Kalau seharian kamu di depan komputer, tidak perlu mencari remote: Mando TV untuk Windows mengontrol TV Samsung, LG, Roku, Google TV, atau Android TV kamu lewat Wi-Fi di rumah. Praktis untuk berganti aplikasi, menaikkan volume, atau mengetik di YouTube dengan keyboard PC.',
    pasos=[
      'Unduh Mando TV gratis dari Microsoft Store ke komputer Windows 10 atau 11 kamu.',
      'Pastikan komputer dan TV berada di jaringan yang sama (Wi-Fi atau kabel, tapi lewat router yang sama).',
      'Buka Mando TV: TV kamu muncul sendiri di daftar. Ketuk atau klik TV tersebut.',
      'Saat pertama kali, setujui koneksi di layar TV (di Google TV dan Android TV, masukkan kode yang ditampilkan TV).',
      'Selesai: pakai tombol atau keyboard untuk mengetik di kolom pencarian TV. Touchpad adalah fitur Pro.',
    ],
    extra=[
      ('Pintasan keyboard di PC (Pro)', 'Dengan Mando TV Pro kamu mengontrol TV dengan keyboard komputer: tombol panah untuk bernavigasi, Enter untuk OK, Backspace atau Esc untuk Kembali, + dan - untuk volume, M untuk bisukan, dan spasi untuk jeda.'),
      ('Mini remote selalu di atas (Pro)', 'Biarkan jendela kecil berisi remote selalu terlihat saat kamu bekerja atau bermain di PC.'),
      ('Berbicara ke TV dari PC (Pro)', 'Dengan Mando TV Pro kamu memberi perintah ke TV lewat mikrofon PC: "buka YouTube", "keraskan volume", atau "matikan dalam 30 menit", persis seperti kamu berbicara. Di Windows, suara dikenali di PC itu sendiri: kamu tidak butuh internet, tidak perlu mengubah apa pun di pengaturan Windows, dan berfungsi di 6 bahasa aplikasi. Apa yang kamu ucapkan tidak keluar dari PC dan tidak disimpan. Hanya pada prosesor yang sangat lama, aplikasi beralih ke dikte Windows. Untuk itu, pengenalan suara online harus diaktifkan di pengaturan privasi dan bahasa Indonesia (Indonesia) harus ditambahkan di Windows. Kalau ada yang kurang, aplikasi akan memberi tahu dan membuka pengaturannya lewat sebuah tombol.'),
    ],
    marca=None,
    faq=[
      ('Apakah saya butuh kabel atau Bluetooth untuk mengontrol TV dari PC?', 'Tidak. Mando TV tersambung lewat jaringan rumah kamu: PC dan TV hanya perlu terhubung ke router yang sama.'),
      ('Apakah berfungsi dengan semua TV?', 'Berfungsi dengan TV Samsung ber-Tizen (tahun 2016 ke atas), LG dengan webOS, Roku, serta Google TV atau Android TV (Sony, Philips, TCL, Hisense, Sharp, Xiaomi, Toshiba, Panasonic, Haier, Skyworth, dan lainnya).'),
      ('Berapa harganya?', 'Tombol, keyboard, dan menyalakan lewat jaringan gratis dan tanpa iklan. Mando TV Pro adalah pembelian sekali bayar tanpa langganan untuk fitur ekstra seperti touchpad, pintasan keyboard PC, dan mini remote.'),
      ('Kenapa mikrofon tidak memahami saya di Windows?', 'Pastikan fitur suara aktif (fitur ini bagian dari Pro) dan mikrofon PC berfungsi di Windows. Di hampir semua PC, suara dikenali di perangkat itu sendiri, tanpa internet. Hanya pada prosesor yang sangat lama aplikasi memakai dikte Windows. Kalau begitu, pastikan pengenalan suara online aktif di pengaturan privasi Windows dan Windows punya bahasa Indonesia (Indonesia) di pengaturan bahasa. Mando TV memakai bahasa itu hanya saat sedang mendengarkan.'),
    ]),
  dict(clave='roku-403', corto='Aplikasi Roku tidak berfungsi',
    titulo='Aplikasi Roku tidak berfungsi? Atasi error 403',
    desc='HP tersambung tapi Roku tidak merespons? Aktifkan "Kontrol oleh aplikasi seluler" dalam 5 langkah dan pakai HP sebagai remote lagi.',
    h1='Aplikasi Roku tidak berfungsi: begini cara mengatasinya',
    intro='Kalau HP kamu menemukan Roku dan tersambung, tapi tidak ada tombol yang bereaksi, hampir selalu penyebabnya adalah pengaturan di Roku itu sendiri yang memblokir aplikasi remote. Versi Roku yang lebih baru membatasi lebih ketat secara bawaan. Di menu Roku, ini beres dalam satu menit.',
    pasos=[
      'Di Roku, tekan Beranda lalu buka Pengaturan.',
      'Buka Sistem, lalu Pengaturan sistem lanjutan.',
      'Masuk ke "Kontrol oleh aplikasi seluler". Di beberapa model namanya "Kontrol eksternal".',
      'Di "Akses jaringan", pilih Default atau Permissive. Kalau di model kamu hanya berupa tombol geser, biarkan Diaktifkan.',
      'Kembali ke Mando TV di HP dan ketuk Roku kamu. Sekarang tombolnya bereaksi.',
    ],
    extra=[
      ('Cara mengetahui apakah ini masalahmu', 'Tandanya jelas: HP melihat Roku di daftar dan tersambung, tapi tidak terjadi apa-apa saat kamu mengetuk tombol. Di dalam, Roku menjawab dengan error 403, artinya "dilarang". Mando TV mendeteksinya saat menyambung dan menampilkan langkah-langkah ini di layar.'),
      ('Default atau Permissive, mana yang dipilih?', 'Default sudah cukup: ia menerima perintah dari jaringan rumah kamu, dan itu yang dibutuhkan sebuah remote. Permissive lebih terbuka dan hanya perlu di jaringan yang tidak biasa. Kalau opsinya Dinonaktifkan (di perangkat lunak yang lebih baru: Dibatasi), Roku tidak merespons aplikasi.'),
      ('Kalau kamu tidak punya remote Roku', 'Kalau pengaturannya Dinonaktifkan, hanya bisa diubah dengan remote Roku yang asli. Pinjam satu untuk mengubahnya sekali; setelah itu semuanya bisa kamu lakukan dengan HP. Baca juga [Remote Roku hilang](@roku-lost).'),
    ],
    marca='roku',
    faq=[
      ('Kenapa Roku saya tidak merespons lagi padahal dulu berfungsi?', 'Pembaruan Roku bisa membuat pengaturan ini lebih ketat. Ini bukan salah HP atau Wi-Fi kamu: kamu hanya perlu mengizinkan kembali kontrol oleh aplikasi.'),
      ('Apakah ini berlaku untuk Roku TV dan Roku Player?', 'Ya. Pengaturan ini ada di menu yang sama pada Roku Player maupun perangkat Roku TV.'),
      ('Apakah aman membiarkan pengaturan di Default?', 'Ya. Pengaturan itu hanya menerima perintah dari perangkat di jaringan rumah kamu.'),
    ]),
  dict(clave='not-found', corto='HP tidak menemukan TV',
    titulo='HP tidak menemukan TV? 6 hal yang perlu diperiksa',
    desc='Aplikasi remote tidak menemukan TV kamu? Periksa Wi-Fi, VPN, dan akses jaringan lokal. Untuk Samsung, LG, Roku, dan Android TV.',
    h1='HP tidak menemukan TV: ini yang perlu kamu periksa',
    intro='Kamu membuka aplikasi remote dan daftarnya kosong, atau TV muncul tapi koneksinya terputus. Hampir selalu penyebabnya ada di jaringan, bukan di TV. Periksa poin-poin ini secara berurutan: yang pertama menyelesaikan sebagian besar kasus.',
    pasos=[
      'Lihat HP kamu berada di Wi-Fi yang mana dan TV di Wi-Fi yang mana. Harus jaringan yang sama dengan nama yang sama. Jaringan tamu tidak berfungsi karena memisahkan perangkat satu sama lain.',
      'Matikan VPN di HP kalau kamu memakainya. Saat VPN aktif, HP kamu mengakses internet lewat jaringan lain dan tidak melihat perangkat di rumah, atau koneksinya terputus setelah beberapa detik.',
      'Matikan data seluler sebentar. Beberapa HP berpindah sendiri dari Wi-Fi ke data seluler saat sinyalnya lemah.',
      'Nyalakan TV dan tunggu sampai selesai menyala. TV yang mati tidak menjawab pencarian.',
      'Di iPhone, pastikan aplikasi punya izin "Jaringan Lokal": Pengaturan > Privasi & Keamanan > Jaringan Lokal.',
      'Kalau TV masih belum muncul, tambahkan secara manual: di Mando TV ketuk "Tambah lewat IP" dan masukkan alamat IP TV.',
    ],
    extra=[
      ('Biarkan aplikasi memandu kamu', 'Di daftar TV ada tombol untuk kasus ketika TV kamu tidak muncul. Aplikasi memeriksa penyebab yang paling sering langkah demi langkah (Wi-Fi yang sama, VPN, izin jaringan lokal, dan lainnya) dan setelah setiap perbaikan menampilkan tombol untuk memeriksa ulang. Pemandunya gratis.'),
      ('Di mana menemukan alamat IP TV', 'Ada di menu jaringan TV, sedikit berbeda tergantung model. Di LG: Pengaturan, Jaringan, Koneksi Wi-Fi, Pengaturan Wi-Fi lanjutan. Di Samsung: Pengaturan, Umum, Jaringan, Status jaringan, Pengaturan IP. Di Roku: Pengaturan, Jaringan, Tentang. Di Android TV dan Google TV: Pengaturan, Jaringan & internet, lalu ketuk jaringan kamu. Bentuknya angka seperti 192.168.1.86.'),
      ('Kalau TV muncul tapi koneksinya terputus', 'Kalau koneksi terputus setelah beberapa detik, penyebabnya biasanya di HP: VPN, pindah ke Wi-Fi lain, atau mode hemat daya. Matikan VPN, tetap di Wi-Fi yang sama, dan coba lagi.'),
      ('Wi-Fi 2,4 dan 5 GHz', 'Tidak masalah kalau HP kamu di jaringan 5 GHz dan TV di jaringan 2,4 GHz, selama keduanya berasal dari router yang sama. Kalau kamu memakai repeater Wi-Fi dan TV tetap tidak muncul, dekatkan HP ke router utama dan coba lagi.'),
    ],
    marca=None,
    faq=[
      ('Bisakah saya mengontrol TV dengan data seluler?', 'Tidak. Sinyal remote berjalan lewat Wi-Fi di rumah kamu, jadi HP dan TV harus berada di jaringan yang sama.'),
      ('Kenapa tidak berfungsi kalau VPN aktif?', 'Karena VPN mengarahkan seluruh lalu lintas HP kamu lewat jaringan lain, sehingga HP tidak lagi melihat perangkat di rumah. Matikan selama kamu memakai remote.'),
      ('Apakah berfungsi dengan Bluetooth atau inframerah?', 'Untuk Smart TV, Mando TV memakai Wi-Fi. Inframerah hanya berfungsi di HP Android dengan pemancar inframerah dan ditujukan untuk TV yang bukan Smart TV. Bluetooth ada dalam versi beta, gratis dan hanya mulai Android 9: HP tersambung ke TV sebagai keyboard dan remote Bluetooth, tanpa Wi-Fi sama sekali. Berfungsi dengan Google TV, Android TV, dan Fire TV; di merek lain yang menerima keyboard Bluetooth mungkin bisa, sedangkan Roku tidak menerimanya.'),
    ]),
  dict(clave='androidtv-code', corto='Kode pemasangan Android TV',
    titulo='Android TV meminta kode pemasangan: begini caranya',
    desc='Android TV atau Google TV kamu menampilkan kode 6 karakter saat menyambung. Begini cara memasukkannya dan apa yang dilakukan kalau kode tidak muncul atau salah.',
    h1='Android TV meminta kode pemasangan: begini caranya',
    intro='Saat pertama kali menyambungkan HP ke Android TV atau Google TV, TV menampilkan kode 6 karakter di layar. Ini normal dan hanya terjadi sekali: dengan begitu dipastikan tidak ada orang lain yang bisa mengontrol TV kamu. Berikut cara memasukkannya dan apa yang dilakukan kalau kode tidak muncul.',
    pasos=[
      'Nyalakan TV dan biarkan layar utama terlihat.',
      'Buka Mando TV di HP, di Wi-Fi yang sama dengan TV, lalu ketuk TV kamu di daftar.',
      'Lihat layar TV: muncul kode berisi 6 huruf dan angka.',
      'Ketik persis seperti yang ditampilkan di HP kamu lalu ketuk Pasangkan. Hurufnya hanya dari A sampai F, jadi karakter yang bulat selalu angka nol.',
      'Selesai. TV mengingat HP kamu dan tidak akan meminta kode lagi.',
    ],
    extra=[
      ('Kalau kode tidak muncul di TV', 'Pastikan TV benar-benar menyala dan tidak dalam mode siaga, dan HP kamu berada di Wi-Fi yang sama. Di HP, ketuk TV sekali lagi. Kalau masih belum muncul, restart TV: cabut kabel listrik selama sepuluh detik, colokkan lagi, lalu coba lagi.'),
      ('Kalau kode dibilang salah', 'Kode berubah setiap kali diminta. Kalau kamu butuh waktu lama atau memintanya dua kali, hanya kode terakhir di layar yang berlaku. Di HP, ketuk TV sekali lagi dan masukkan kode yang baru.'),
      ('Kalau TV meminta kode lagi', 'Ini terjadi kalau TV direset ke pengaturan pabrik atau kamu menghapus data aplikasi di HP. Pasangkan lagi, maka tersimpan. Kalau kamu sama sekali tidak punya remote, baca [Android TV tanpa remote](@androidtv).'),
    ],
    marca='android',
    faq=[
      ('TV mana yang memakai kode ini?', 'Yang memakai Android TV atau Google TV: Sony, Philips, TCL, Hisense, Sharp, Xiaomi, Chromecast with Google TV, dan beberapa lainnya.'),
      ('Apakah saya butuh akun Google di HP?', 'Tidak. Kode di layar sudah semua yang kamu butuhkan.'),
      ('Apakah ini aman?', 'Ya. Kode itu membuktikan bahwa kamu berada di depan TV: tidak ada yang bisa memasangkan tanpa melihatnya di layar.'),
    ]),
  dict(clave='roku-lost', corto='Remote Roku hilang',
    titulo='Remote Roku hilang? Pakai HP lewat Wi-Fi',
    desc='Remote Roku hilang? HP kamu menggantikannya lewat Wi-Fi. Langkah mudah, juga kalau kamu ganti router dan Roku tidak punya Wi-Fi.',
    h1='Remote Roku hilang: begini cara memakai HP kamu',
    intro='Kalau remote Roku kamu hilang atau tidak berfungsi lagi, HP kamu menggantikannya selama Roku masih tersambung ke Wi-Fi kamu. Dan kalau kamu ganti Wi-Fi atau router, ada juga jalan keluarnya.',
    pasos=[
      'Coba dulu membunyikan remote. Kalau remote Roku kamu punya speaker, misalnya Roku Voice Remote Pro, buka Mando TV, sambungkan ke Roku, dan pakai opsi untuk membunyikan remote supaya mudah ditemukan. Ini hanya berfungsi dengan remote Roku yang punya speaker, dan Roku harus menyala.',
      'Nyalakan TV dan biarkan Roku tetap terpasang. Kamu tidak perlu menyentuhnya.',
      'Hubungkan HP kamu ke Wi-Fi yang sama dengan yang dipakai Roku.',
      'Buka Mando TV. Roku muncul sendiri di daftar. Ketuk Roku tersebut.',
      'Pakai tombol arah, OK, Beranda, dan Kembali seperti di remote yang biasa kamu pakai. Roku tidak meminta kode.',
      'Kalau tombolnya tidak melakukan apa-apa, Roku memblokir kontrol oleh aplikasi: panduan [Aplikasi Roku tidak berfungsi](@roku-403) menjelaskan cara mengizinkannya.',
    ],
    extra=[
      ('Kalau Roku tidak punya Wi-Fi (ganti router atau pindah rumah)', 'Tanpa remote kamu tidak bisa masuk ke menu untuk mengatur jaringan baru, tapi ada triknya: Roku tersambung sendiri ke jaringan yang namanya dan kata sandinya sama dengan yang lama. Di HP lain, buat hotspot Wi-Fi dengan nama dan kata sandi yang persis sama, sambungkan HP dengan Mando TV ke hotspot itu, dan Roku akan muncul di daftar. Dari sana buka Pengaturan, Jaringan dan sambungkan ke Wi-Fi yang baru.'),
      ('Kalau ini Roku TV', 'Perangkat Roku TV punya tombol di badan TV, hampir selalu di bagian bawah tengah atau di belakang, yang menyalakan TV. Itu cukup untuk menyalakannya dan melanjutkan dengan HP.'),
      ('Kalau kamu lebih suka membeli remote lain', 'Pastikan cocok dengan model kamu. Roku Player kecil di belakang TV butuh remote tanpa inframerah, karena inframerah tidak menjangkaunya.'),
    ],
    marca='roku',
    faq=[
      ('Bisakah HP saya menyalakan Roku?', 'Roku Player yang terpasang selalu menyala. Di Roku TV, Mando TV menyalakannya lewat Wi-Fi kalau "Quick Start TV" diaktifkan di Pengaturan > Sistem > Daya.'),
      ('Bagaimana dengan volume?', 'Di Roku TV, HP kamu menaikkan dan menurunkan volume. Di Roku Player yang tersambung lewat HDMI, hasilnya tergantung TV: di banyak TV berfungsi, di yang lain tidak.'),
      ('Apakah saya harus membuat akun?', 'Tidak. Mando TV tidak meminta akun dan juga mengontrol TV Samsung, LG, dan Android TV dengan satu aplikasi yang sama.'),
    ]),
]

SOPORTE = dict(
  titulo='Bantuan: hubungkan dan nyalakan TV dengan Mando TV',
  desc='Cara menghubungkan remote Mando TV ke LG, Samsung, Roku, atau Android TV, menyalakan TV dari HP, dan mengatasi masalah.',
  h1='Bantuan',
  intro='Pertanyaan yang paling sering muncul, sesuai urutan langkahnya. Kalau pertanyaanmu tidak ada, tulis ke kami di <a href="mailto:hola@mandotv.app?subject=Bantuan%20Mando%20TV">hola@mandotv.app</a> dan kami akan membalas.',
)
SOPORTE_HTML = '''      <h2 id="encontrar">Menemukan TV</h2>
      <div class="preguntas">
        <details open><summary>TV saya tidak muncul di daftar</summary>
          <ol>
            <li>Pastikan HP dan TV kamu berada di Wi-Fi yang sama. Kalau router kamu punya jaringan 2,4 GHz dan 5 GHz dengan nama berbeda, kadang keduanya tidak saling melihat.</li>
            <li>Pastikan TV menyala.</li>
            <li>Di iPhone, pastikan Mando TV punya izin "Jaringan Lokal", di Pengaturan, Mando TV.</li>
            <li>Di daftar TV, ketuk tombol untuk kasus ketika TV kamu tidak muncul: aplikasi memeriksa penyebab yang paling sering langkah demi langkah (Wi-Fi yang sama, VPN, izin jaringan lokal, dan lainnya) dan setelah setiap perbaikan menampilkan tombol untuk memeriksa ulang.</li>
            <li>Kalau masih belum muncul, ketuk tombol +, pilih merek, dan masukkan alamat IP TV. Alamatnya ada di menu jaringan TV (misalnya 192.168.1.50).</li>
          </ol>
        </details>
        <details><summary>Apakah berfungsi dengan data seluler atau saat saya di luar rumah?</summary>
          <p>Tidak. Mando TV berbicara dengan TV di dalam jaringan rumah kamu, jadi HP kamu harus tersambung ke Wi-Fi itu.</p>
        </details>
      </div>

      <h2 id="conectar">Menyambungkan untuk pertama kali</h2>
      <p>Panduan lengkap menurut merek: <a href="@@R_lg@@">LG</a>, <a href="@@R_samsung@@">Samsung</a>, <a href="@@R_roku@@">Roku</a>, dan <a href="@@R_android@@">Android TV</a>.</p>
      <div class="preguntas">
        <details><summary>LG</summary>
          <p>Saat kamu mengetuk TV, di layar muncul permintaan izin. Setujui dengan remote yang biasa kamu pakai. Ini hanya dilakukan sekali.</p>
        </details>
        <details><summary>Samsung</summary>
          <p>TV bertanya apakah kamu mengizinkan koneksi dari Mando TV. Pilih "Izinkan" dengan remote. Kalau tidak sengaja menolaknya, buka Pengaturan > Umum > Pengelola Perangkat Eksternal > Pengelola Koneksi Perangkat dan ubah menjadi diizinkan.</p>
        </details>
        <details><summary>Roku</summary>
          <p>Roku tidak meminta izin. Kalau koneksi gagal, di Roku buka Pengaturan > Sistem > Pengaturan sistem lanjutan > Kontrol oleh aplikasi seluler dan biarkan akses jaringan di Default atau Permissive (pada software Roku yang lebih baru, atur "Kontrol oleh aplikasi seluler" ke Diaktifkan).</p>
        </details>
        <details><summary>Android TV dan Google TV</summary>
          <p>TV menampilkan kode 6 karakter. Masukkan persis seperti yang muncul di Mando TV. Berfungsi di Sony, Philips, TCL, Hisense, Sharp, Xiaomi, Chromecast with Google TV, dan merek lain dengan Android TV.</p>
        </details>
      </div>

      <h2 id="encender">Menyalakan TV lewat aplikasi</h2>
      <p>Mando TV menyalakan TV lewat jaringan rumah kamu. Untuk itu ada dua syarat: kamu pernah tersambung setidaknya satu kali saat TV menyala, dan di TV fitur menyalakan lewat jaringan sudah diaktifkan. Nama pengaturannya berubah tergantung model; ini yang paling umum:</p>
      <div class="preguntas">
        <details><summary>LG</summary>
          <p>Cari "Nyalakan TV dengan perangkat seluler" di pengaturan (ada di Pengaturan, Umum, Perangkat, Perangkat Eksternal; pada model lama di Koneksi, Manajemen Koneksi Seluler) dan aktifkan "Nyalakan lewat Wi-Fi". Kalau ada "Quick Start+", aktifkan juga.</p>
        </details>
        <details><summary>Samsung</summary>
          <p>Aktifkan "Nyalakan dengan perangkat seluler" di Pengaturan > Umum > Jaringan > Pengaturan Pakar.</p>
        </details>
        <details><summary>Roku</summary>
          <p>Di perangkat Roku TV, aktifkan "Quick Start TV" di Pengaturan > Sistem > Daya. Roku Player yang dipasang ke TV tidak bisa dinyalakan dengan cara ini.</p>
        </details>
        <details><summary>Android TV dan Google TV</summary>
          <p>Ini tergantung produsennya. Cari "Wake on LAN", "Nyalakan lewat jaringan", "Siaga jaringan", atau "Remote start" di pengaturan jaringan atau daya. Beberapa model tidak punya opsi ini.</p>
        </details>
      </div>

      <h2 id="falla">Kalau ada yang tidak berfungsi</h2>
      <div class="preguntas">
        <details><summary>Koneksi terputus atau tidak ada respons</summary>
          <ol>
            <li>Di layar remote, ketuk Hubungkan ulang.</li>
            <li>Kalau belum membantu, tutup Mando TV dan buka lagi aplikasinya.</li>
            <li>Kalau TV mendapat alamat IP baru, hapus dari daftar dan tambahkan lagi.</li>
          </ol>
        </details>
        <details><summary>Cara mengirim laporan masalah ke kami</summary>
          <ol>
            <li>Di Mando TV, ketuk tombol Personalisasi (pengatur di bagian atas).</li>
            <li>Ketuk Salin laporan pengujian.</li>
            <li>Tempel laporan itu bersama merek dan model TV kamu di email ke hola@mandotv.app.</li>
          </ol>
          <p>Laporan itu tidak berisi kata sandi, kode, atau apa pun yang kamu ketik.</p>
        </details>
        <details><summary>Saya sudah membeli Pro tapi tidak muncul</summary>
          <p>Di Personalisasi, ketuk Pulihkan pembelian, dengan akun toko aplikasi yang sama dengan yang kamu pakai saat membeli. Kalau masih belum muncul, tulis ke kami.</p>
        </details>
      </div>

      <h2 id="guias">Panduan langkah demi langkah</h2>
      <p><a href="@@R_guias@@">Lihat semua panduan</a></p>
      <ul>
@@GUIAS@@
      </ul>

      <h2 id="contacto">Masih ada pertanyaan?</h2>
      <p>Tulis ke kami di <a href="mailto:hola@mandotv.app?subject=Bantuan%20Mando%20TV">hola@mandotv.app</a>. Beri tahu kami merek dan model TV kamu serta di langkah mana kamu tersangkut. Tulis dalam bahasa kamu. Kami membalas dalam bahasa Spanyol atau Inggris dan, kalau kamu mau, dalam bahasa kamu dengan bantuan penerjemah.</p>
'''

PRIVACIDAD = dict(
  titulo='Kebijakan Privasi | Mando TV',
  desc='Mando TV tidak meminta akun atau data pribadi: tanpa iklan, tanpa pelacak. Remote berbicara langsung dengan TV kamu di dalam Wi-Fi kamu.',
  h1='Privasi',
  intro='Singkatnya: Mando TV tidak meminta akun atau data pribadi. Tidak ada iklan dan tidak ada pelacak.',
)
PRIVACIDAD_HTML = '''      <p class="fecha">Berlaku sejak 14 November 2026. Terakhir diperbarui pada 28 November 2026.</p>

      <h2>Siapa kami</h2>
      <p>Mando TV adalah aplikasi untuk mengontrol TV kamu dari HP atau komputer. Kebijakan ini menjelaskan informasi apa yang dipakai aplikasi dan apa yang dilakukannya dengan informasi itu. Kalau ada pertanyaan, tulis ke kami di <a href="mailto:hola@mandotv.app">hola@mandotv.app</a>.</p>

      <h2>Data apa yang kami kumpulkan</h2>
      <p>Aplikasi: hanya yang diperlukan untuk uji coba Pro gratis di Android dan Windows, dijelaskan di <a href="#prueba">Uji coba Pro gratis</a>. Di luar itu, aplikasi tidak mengirimkan informasi tentang kamu atau tentang cara kamu memakainya kepada kami maupun pihak ketiga. Aplikasi tidak memakai alat analitik, iklan, atau pelacakan.</p>
      <p>Situs web ini: kami mengukur kunjungan dengan dua cara, yang dijelaskan di bagian <a href="#cookies">Cookie di situs ini</a>.</p>

      <h2>Apa yang disimpan aplikasi di perangkat kamu</h2>
      <p>Agar bisa berfungsi, aplikasi menyimpan hal berikut hanya di HP atau komputer kamu:</p>
      <ul>
        <li>TV yang kamu tambahkan: nama, merek, alamat IP di jaringan kamu, dan alamat perangkat keras jaringan (MAC) yang dipakai untuk menyalakannya.</li>
        <li>Kunci koneksi yang diberikan setiap TV saat kamu menyetujui izin. Kunci itu disimpan terenkripsi di penyimpanan aman sistem (Keychain di iPhone dan Mac, Keystore di Android, penyimpanan terlindungi di Windows).</li>
        <li>Pengaturan kamu: tema terang atau gelap, warna latar, getar, dan jenis remote.</li>
        <li>Kalau kamu memakai fitur Pro: aplikasi favorit, rutinitas, dan pencarian YouTube terakhir kamu (bisa kamu hapus di aplikasi).</li>
        <li>Kalau kamu memakainya: mode anak (PIN hanya disimpan sebagai kode terlindungi) dan remote yang dibagikan orang lain kepadamu.</li>
      </ul>
      <p>Kalau kamu menghapus aplikasi, data ini ikut terhapus, dengan dua pengecualian. Di Android, kalau kamu memakai pencadangan Google, preferensi aplikasi (seperti daftar TV dan pengaturanmu) bisa tetap ada di cadangan Google milikmu dan kembali saat kamu memasang ulang aplikasi; kunci koneksi tidak pernah termasuk di dalamnya. Di iPhone dan Mac, kunci koneksi disimpan di Keychain sistem dan bisa tetap ada di sana setelah kamu menghapus aplikasi.</p>

      <h2>Dengan siapa aplikasi berkomunikasi</h2>
      <p>Dengan TV kamu, di dalam Wi-Fi di rumah. Untuk menemukannya, aplikasi memindai jaringan lokal kamu; karena itu di iPhone aplikasi meminta izin "Jaringan Lokal". Teks yang kamu ketik dengan keyboard aplikasi langsung dikirim ke TV dan tidak disimpan.</p>
      <p>Selain itu, saat dibuka, aplikasi mengunduh sebuah berkas publik kecil dari situs ini (mandotv.app/app/config.json) untuk mengetahui apakah ada versi baru yang sebaiknya kamu pasang dan fitur mana yang termasuk Mando TV Pro. Ini hanya sebuah unduhan, seperti saat membuka halaman: aplikasi tidak mengirim datamu, TV kamu, maupun apa yang kamu lakukan. Aplikasi hanya menyebutkan versi aplikasi dan sistemnya (misalnya Android) agar bisa menampilkan pemberitahuan yang sesuai. Kalau kamu tidak punya internet, aplikasi tetap bekerja dengan berkas yang terakhir diunduh; kalau lebih dari 30 hari berlalu tanpa berhasil mengunduhnya, aplikasi akan meminta kamu terhubung ke internet sebentar. Seperti setiap kunjungan ke situs web, unduhan itu juga memperlihatkan alamat IP-mu kepada penyedia situs kami (Cloudflare).</p>

      <p>Kalau kamu mengirim foto atau video ke TV (fitur Pro), TV hanya mengunduh berkas yang kamu pilih, langsung dari HP atau PC kamu lewat Wi-Fi di rumah. Berkas itu tidak lewat internet maupun kami, aplikasi tidak melihat foto kamu yang lain, dan pembagiannya berakhir begitu kamu menutup layar itu. Di dalam jaringan rumahmu, transfer ini tidak dienkripsi.</p>
      <p>Kalau kamu memakai "Tampilkan layar saya di TV" (fitur Pro), aplikasi menangkap layarmu hanya selama kamu menduplikasinya, mengodekannya di perangkatmu, lalu mengirimnya lewat Wi-Fi rumah langsung ke TV yang kamu pilih. Data itu tidak lewat internet maupun kami, tidak ada yang direkam atau disimpan, dan berhenti saat kamu menghentikannya atau menutup aplikasi. TV menampilkan semua yang muncul di layar itu, termasuk notifikasi, dan di dalam jaringan rumahmu siarannya tidak dienkripsi.</p>
      <h2 id="prueba">Uji coba Pro gratis (Android dan Windows)</h2>
      <p>Agar uji coba Pro gratis hanya satu kali per perangkat, saat dimulai aplikasi mengirim satu kali dua hal ke server kami (api.mandotv.app, di Cloudflare): sidik terenkripsi dari pengenal yang diberikan sistem kepada aplikasi di perangkat itu (di Android, ID Android milik aplikasi itu sendiri; di Windows, pengenal perangkat untuk aplikasi kami) dan sudah berapa lama uji cobamu berjalan. Sidik itu tidak menunjukkan perangkat mana itu atau siapa kamu, dan server mengenkripsinya sekali lagi dengan kunci sendiri sebelum menyimpannya.</p>
      <p>Kami hanya menyimpan sidik itu, tanggal uji coba dimulai, dan apakah itu Android atau Windows. Kami tidak menyimpan alamat IP-mu (Cloudflare melihatnya saat menjawab, seperti pada sambungan apa pun). Kami memakainya hanya agar memasang ulang aplikasi tidak memberi uji coba lagi, yaitu pencegahan penipuan dan kepentingan sah kami; tidak pernah untuk iklan atau untuk mengikutimu, dan tidak kami bagikan kepada siapa pun. Setiap catatan terhapus otomatis setelah 24 bulan. Kalau kamu tidak punya internet, uji coba tetap berjalan. Di iPhone dan Mac tidak ada yang dikirim: uji coba diurus oleh App Store.</p>

      <h2>Mikrofon dan suara</h2>
      <p>Di iPhone, Mac, dan Android, pencarian suara memakai mikrofon hanya selama kamu menekan tombol bicara. Apa yang kamu ucapkan diubah menjadi teks oleh pengenalan suara sistem kamu: oleh Apple di iPhone dan Mac serta oleh Google di Android, masing-masing sesuai kebijakan privasi mereka. Di Windows, suara dikenali di PC-mu sendiri dan tidak keluar dari sana. Hanya kalau mesin di perangkat itu tidak bisa dimulai atau terus gagal (misalnya karena prosesor lama atau model suara yang tidak ada), aplikasi memakai pengetikan suara Windows dari Microsoft, yang bekerja secara online jika kamu mengaktifkan pengenalan suara online di Windows, sesuai kebijakan privasi Microsoft. Di Windows, mikrofon dibuka saat kamu membuka panel suara dan ditutup saat kamu menutupnya, atau setelah 30 detik tidak dipakai; selama kamu tidak berbicara, tidak ada yang direkam atau disimpan. Mando TV tidak merekam maupun menyimpan audio, dan teks hasilnya langsung dikirim ke TV kamu, sama seperti yang kamu ketik dengan keyboard.</p>

      <h2>Rumah: perangkat dari Apple Home dan Google Home</h2>
      <p>Kalau kamu membuka bagian Rumah (dalam pengujian), aplikasi meminta izin untuk melihat perangkat yang sudah kamu miliki di aplikasi Rumah milik Apple (HomeKit) atau di Google Home. Dengan izin itu, aplikasi membaca nama, ruangan, dan statusnya (menyala atau mati, kecerahan, suhu, atau sampai di bagian mana program sebuah peralatan rumah tangga) untuk menampilkannya dan mengirimkan apa yang kamu ketuk. Semuanya terjadi antara HP kamu dan sistem Apple atau Google: Mando TV tidak menyimpan daftar ini, tidak mengirimkannya kepada kami maupun pihak ketiga, dan tidak memakainya untuk iklan atau analitik. Di Android, Google Home berfungsi dengan akun Google kamu sendiri, sesuai kebijakan privasi Google. Kamu bisa mencabut izin kapan saja: di iPhone lewat Pengaturan &gt; Privasi &amp; Keamanan &gt; HomeKit, di Android lewat pengaturan akun Google kamu.</p>
      <p>Kalau kamu mengetuk "Bagaimana fitur Rumah bekerja untuk Anda?", aplikasi email kamu terbuka dengan pesan ke hola@mandotv.app yang berisi ringkasan teknis: versi aplikasi, sistem, serta berapa banyak perangkat dari setiap jenis yang muncul dan apakah merespons. Nama perangkat, ruangan, atau rumah kamu tidak disertakan, dan pesan hanya terkirim kalau kamu sendiri yang mengirimnya.</p>

      <h2>Tautan dan teks yang kamu bagikan</h2>
      <p>Saat kamu membagikan remote (tautan mandotv.app/m/), tautan itu berisi desain remote dan petunjuk untuk menemukan TV-mu: nama, merek, model, dan alamatnya di jaringanmu. Tautan itu tidak pernah berisi kunci koneksi, PIN, atau alamat perangkat keras TV. Informasi itu berada setelah tanda #, jadi tidak pernah sampai ke server kami, tetapi siapa pun yang kamu kirimi tautan, misalnya lewat WhatsApp, bisa membacanya. Rutinitas yang dibagikan (tautan mandotv.app/r/) hanya berisi nama dan langkahnya.</p>
      <p>Teks cadangan yang bisa kamu salin di pengaturan aplikasi berisi favorit, rutinitas, dan pengaturanmu. Teks itu tidak dienkripsi dan hanya pergi ke tempat kamu menempelkannya.</p>

      <h2>Laporan pengujian</h2>
      <p>Aplikasi punya tombol "Salin laporan pengujian" yang membantu kami memperbaiki kesalahan. Laporan itu hanya ada di memori aplikasi selama aplikasi terbuka dan tidak pernah dikirim otomatis: kamu yang memutuskan apakah akan menyalin dan membagikannya. Laporan itu tidak berisi kunci koneksi, kode pemasangan, atau apa pun yang kamu ketik. Laporan itu berisi langkah yang dijalankan aplikasi, seperti mencari, menyambung, dan error, serta data teknis: versi aplikasi, sistemmu, dan merek, model, serta alamat TV-mu di jaringanmu.</p>

      <h2 id="cookies">Cookie di situs ini</h2>
      <p>Ini hanya berlaku untuk situs mandotv.app, bukan untuk aplikasi.</p>
      <h3>Selalu tanpa cookie</h3>
      <p>Kami menghitung kunjungan secara anonim dengan Cloudflare Web Analytics: berapa orang yang mengunjungi situs, halaman apa yang mereka baca, dan dari negara mana. Layanan ini tidak memakai cookie, tidak memakai alamat IP kamu untuk mengidentifikasi kamu, dan tidak melacak apa yang kamu lakukan di situs lain.</p>
      <h3>Dengan cookie, hanya kalau kamu setuju</h3>
      <p>Kalau di pemberitahuan cookie kamu mengetuk "Terima", kami mengaktifkan Google Analytics (dari Google LLC) untuk lebih memahami cara situs dipakai: tampilan halaman, lama kunjungan, jenis perangkat, perkiraan kota, dan dari mana kamu datang. Untuk itu layanan ini menyimpan cookie _ga dan _ga_* hingga 2 tahun di browser kamu. Google dapat memproses data ini di server di luar Chili. Kami menonaktifkan fitur iklan dan Google Signals, dan kami tidak memakai data ini untuk menampilkan iklan kepada kamu.</p>
      <p>Kalau kamu mengetuk "Tolak" atau tidak memilih apa pun, Google Analytics tidak dimuat dan tidak ada cookie yang disimpan. Kamu bisa mengubah keputusan kapan saja dengan tombol "Cookie" di bagian bawah setiap halaman; kalau kamu mencabut persetujuan, kami menghapus cookie tersebut.</p>
      <p>Pilihan kamu disimpan di browser kamu (penyimpanan lokal, tidak dikirim ke siapa pun) agar kami tidak bertanya lagi. Penyimpanan yang sama menyimpan bahasa yang kamu pilih di bagian bawah halaman, supaya lain kali situs terbuka dalam bahasa itu. Untuk menampilkan harga Pro di negaramu, setiap halaman bertanya kepada Cloudflare, yang memang sudah melayani situs ini, kamu berkunjung dari negara mana, atau memakai wilayah bahasa browser-mu; jawaban itu tidak disimpan.</p>

      <h2>Pembelian</h2>
      <p>Kalau kamu membeli Mando TV Pro, pembayaran diproses oleh toko aplikasi (App Store, Google Play, atau Microsoft Store). Kami tidak menerima maupun menyimpan data kartu kamu. Toko aplikasi hanya mengonfirmasi kepada aplikasi bahwa pembelian itu ada.</p>

      <h2>Email yang kamu kirim kepada kami</h2>
      <p>Kalau kamu menulis ke kami di <a href="mailto:hola@mandotv.app">hola@mandotv.app</a>, kami memakai alamat email kamu dan apa yang kamu sampaikan hanya untuk membalasmu. Kami tidak membagikannya dan tidak memakainya untuk iklan. Kamu bisa meminta kami menghapus pesan kamu kapan saja.</p>

      <h2>Anak-anak</h2>
      <p>Aplikasi tidak mengumpulkan data pribadi dari siapa pun, termasuk anak-anak.</p>

      <h2>Perubahan pada kebijakan ini</h2>
      <p>Kalau suatu hari apa yang dilakukan aplikasi dengan datamu berubah, kami akan memperbarui halaman ini dan tanggal di atas sebelum perubahan itu sampai ke aplikasi.</p>
'''


# >>> guías traídas del inglés (ensamblar.py)
# Adaptadas con Ollama (qwen3.6:35b) desde las guías inglesas y auditadas por Opus el 22-nov. Rutas en idiomas_sitio.py.
GUIAS += [
  dict(clave='no-sub', corto='Aplikasi remote tanpa langganan', fecha='2026-11-23',
    titulo='Aplikasi remote TV tanpa langganan dan tanpa iklan',
    desc='Bosan dengan aplikasi remote penuh iklan atau langganan mingguan? Mando TV gratis dan tanpa iklan, Pro opsional sekali bayar. Perbandingan jujur.',
    h1='Aplikasi remote tanpa langganan dan tanpa iklan',
    intro='Banyak remote universal menampilkan iklan atau meminta langganan mingguan sebelum bisa dipakai. Mando TV memilih jalan lain: remotenya gratis, tanpa iklan, dan tanpa akun. Pro yang opsional hanya dibeli sekali. Berikut perbandingannya, termasuk hal-hal yang tidak bisa dilakukan aplikasi ini.',
    pasos=[
      'Sebelum memasang, buka halaman sebuah aplikasi di toko dan periksa pembelian dalam aplikasinya. Harga mingguan atau bulanan menandakan langganan.',
      'Di Google Play, lihat apakah di halamannya tertulis "Berisi iklan", dan baca ulasan terbaru dengan bintang sedikit: di sanalah sering muncul paywall yang tak terduga.',
      'Pastikan aplikasi bisa mengontrol TV kamu lewat Wi-Fi. Mando TV berfungsi dengan Samsung (2016 ke atas), LG webOS, Roku, Google TV, Android TV, dan Fire TV.',
      'Pasang Mando TV, hubungkan HP ke Wi-Fi yang sama dengan TV, lalu ketuk TV kamu di daftar.',
      'Setujui permintaan di TV atau masukkan kode yang ditampilkan. Tombol, volume, saluran, dan keyboard tidak dipungut biaya.',
    ],
    tabla=dict(titulo='Mando TV dibandingkan dengan banyak aplikasi remote',
      cabeza=['', 'Mando TV', 'Banyak aplikasi berbasis iklan atau langganan'],
      filas=[
        ['Remote dasar', 'Gratis', 'Sering gratis dengan iklan atau tersembunyi di balik masa percobaan'],
        ['Iklan', 'Tidak ada', 'Sering'],
        ['Langganan', 'Tidak ada. Pro adalah pembelian sekali bayar yang opsional', 'Paket mingguan atau bulanan itu lazim'],
        ['Akun', 'Tidak perlu', 'Bervariasi'],
        ['Smart TV lewat Wi-Fi', 'Samsung (2016 ke atas), LG webOS, Roku, Google TV, Android TV, Fire TV, Apple TV (beta)', 'Tergantung aplikasinya'],
        ['Inframerah untuk TV lama', 'Gratis di HP Android dengan pemancar inframerah (baru)', 'Beberapa aplikasi, hanya di HP dengan pemancar inframerah'],
        ['Bluetooth', 'Beta mulai Android 9, gratis', 'Tergantung aplikasinya'],
        ['Foto dan video ke TV', 'Pro, lewat Wi-Fi (bukan mirroring)', 'Tergantung aplikasinya'],
        ['HP dan komputer', 'iPhone, iPad, Mac, dan Windows, ditambah Android dalam akses awal', 'Bervariasi'],
        ['Mirroring layar', 'Gratis di iPhone, iPad, dan Windows dengan fitur bawaan masing-masing. Di Windows, Pro juga bisa mencerminkan layar PC ke TV LG, Samsung, Hisense, dan Android TV (beta)', 'Beberapa aplikasi menawarkannya'],
      ],
      nota='Mando TV tidak dibandingkan dengan aplikasi tertentu. Harga terkini ada di halaman toko masing-masing aplikasi.'),
    extra=[
      ('Yang tidak dilakukan Mando TV', 'Di iPhone dan iPad, aplikasi mengarahkan kamu ke Pencerminan Layar di Pusat Kontrol, fitur iPhone itu sendiri yang berfungsi dengan TV ber-AirPlay. Di Windows, aplikasi membuka Cast (Windows + K), dan Mando TV Pro bisa mengirim layar PC ke TV LG, Samsung, Hisense, dan Android TV lewat Wi-Fi kamu (beta, dengan jeda beberapa detik dan tanpa suara). Dengan Mando TV Pro, aplikasi juga bisa mengirim foto dan video ke TV lewat Wi-Fi kamu. Aplikasi ini mengontrol Smart TV lewat Wi-Fi rumah. TV yang bukan Smart TV bisa dikontrol lewat inframerah dari HP Android dengan pemancar inframerah. Mulai Android 9, HP juga bisa tersambung lewat Bluetooth sebagai keyboard dan remote ke Google TV, Android TV, dan Fire TV, tanpa Wi-Fi sama sekali. Opsi ini dalam versi beta dan gratis.'),
      ('Bagaimana Mando TV menghasilkan uang', 'Bukan dari iklan dan bukan dari datamu: aplikasi ini tidak punya iklan dan tidak melacakmu. Mando TV dibiayai oleh Pro, pembelian sekali bayar yang opsional untuk fitur ekstra. Remote dasarnya gratis.'),
      ('Di perangkat yang sudah kamu punya', 'iPhone, iPad, dan Mac dari App Store, PC Windows dari Microsoft Store, dan Android lewat akses awal gratis di Google Play. Lihat [Aplikasi remote TV untuk iPhone](@iphone) dan [Aplikasi remote TV untuk Windows](@windows).'),
      ('Privasi', 'Tanpa akun dan tanpa pelacakan di aplikasi. Komunikasi dengan TV hanya terjadi di jaringan lokal, dan data koneksi tetap tersimpan terenkripsi di perangkat kamu. Detailnya ada di [Kebijakan Privasi](@privacidad).'),
    ],
    marca=None,
    faq=[
      ('Apakah ada aplikasi remote tanpa langganan?', 'Ada. Mando TV sama sekali tidak punya langganan: remotenya gratis dan tanpa iklan, Pro adalah pembelian sekali bayar yang opsional.'),
      ('Apakah Mando TV benar-benar gratis?', 'Ya. Tombol arah, OK, Kembali, Beranda, volume, saluran, angka, keyboard, dan menyalakan atau mematikan TV gratis, tanpa iklan dan tanpa batas waktu.'),
      ('Apakah berfungsi tanpa Wi-Fi?', 'Biasanya tidak. Mando TV mengontrol Smart TV lewat Wi-Fi rumah kamu. Pengecualian: inframerah di HP Android dengan pemancar inframerah, yang juga berfungsi di TV yang bukan Smart TV atau tidak tersambung ke Wi-Fi, dan Bluetooth, dalam versi beta mulai Android 9, untuk Google TV, Android TV, dan Fire TV.'),
    ]),
  dict(clave='roku-app-alt', corto='Alternatif aplikasi Roku', fecha='2026-11-23',
    titulo='Alternatif aplikasi Roku: remote Roku yang simpel',
    desc='Alternatif aplikasi Roku sebagai remote: Mando TV mengontrol Roku TV dan Player lewat Wi-Fi, tanpa akun dan iklan, plus Samsung, LG, dan Google TV.',
    h1='Alternatif aplikasi Roku: satu aplikasi untuk semua TV',
    intro='Aplikasi Roku resmi punya banyak fitur: Channel Store, casting, Private Listening, dan remote. Kalau kamu hanya butuh remote yang cepat atau di rumah juga punya TV Samsung, LG, atau Google TV, Mando TV adalah alternatif simpel yang mengontrol Roku lewat Wi-Fi kamu tanpa akun.',
    pasos=[
      'Hubungkan HP dan Roku ke Wi-Fi yang sama.',
      'Unduh Mando TV dan buka. Roku TV atau Roku Player kamu muncul di daftar. Ketuk. Roku tidak meminta kode.',
      'Pakai tombol arah, OK, Kembali, Beranda, volume, dan keyboard. Ketik kata pencarian di kanal Roku dengan keyboard HP.',
      'Kalau tombolnya tidak melakukan apa-apa, di Roku buka Pengaturan > Sistem > Pengaturan sistem lanjutan > Kontrol oleh aplikasi seluler dan atur akses jaringan ke Default atau Permissive (di perangkat lunak Roku yang lebih baru, atur Kontrol oleh aplikasi seluler ke Diaktifkan).',
      'Opsional: di Roku TV, aktifkan "Quick Start TV" di Pengaturan > Sistem > Daya agar Mando TV bisa menyalakan TV.',
    ],
    extra=[
      ('Di mana Mando TV lebih cocok', 'Satu aplikasi untuk beberapa TV: Roku, Samsung, LG, dan Google TV atau Android TV. Tanpa akun, tanpa iklan. Berfungsi juga di PC Windows, praktis di meja kerja. Tombol arah dan volume cepat bereaksi, dan dengan keyboard kamu mengetik kata pencarian tanpa repot.'),
      ('Di mana aplikasi Roku resmi lebih baik', 'Pertahankan aplikasi Roku untuk hal-hal yang ditawarkannya di luar remote, seperti menelusuri dan menambah kanal dari Roku Channel Store, serta casting dan Private Listening (suara lewat headphone di HP). Pakai keduanya kalau kamu mau. Keduanya bisa ada di HP yang sama.'),
      ('Roku TV dan Roku Player', 'Keduanya berfungsi. Termasuk model Roku TV dari TCL, Hisense, Philips, dan lainnya, serta Roku Express, Streaming Stick, dan Ultra. Detailnya ada di [halaman aplikasi remote Roku](@roku).'),
      ('Kalau aplikasi Roku tidak berfungsi lagi', 'Kalau tombol berhenti bereaksi, biasanya Roku memblokir kontrol oleh aplikasi. Panduan [Aplikasi Roku tidak berfungsi](@roku-403) menunjukkan pengaturan yang menyelesaikan masalah ini.'),
      ('Gratis dan Pro', 'Tombol arah, OK, Kembali, Beranda, volume, saluran, tombol angka, keyboard, membuka aplikasi, mengganti input, dan menyalakan atau mematikan TV gratis, tanpa iklan dan tanpa langganan. Touchpad, perintah suara, aplikasi favorit, rutinitas, dan timer tidur adalah bagian dari Mando TV Pro, pembelian sekali bayar tanpa langganan.'),
    ],
    marca='roku',
    faq=[
      ('Apakah saya butuh akun Roku untuk memakai Mando TV?', 'Tidak. Mando TV berkomunikasi dengan Roku lewat jaringan rumah kamu dan tidak meminta akun.'),
      ('Apakah Mando TV menggantikan aplikasi Roku Mobile sepenuhnya?', 'Sebagai remote, ya. Untuk Channel Store, casting, dan Private Listening, pertahankan aplikasi Roku resmi.'),
      ('Apakah berfungsi dengan Roku Express atau Streaming Stick saya?', 'Ya. Semua Roku Player dan perangkat Roku TV dikontrol dengan cara yang sama.'),
    ]),
  dict(clave='lg-thinq', corto='Alternatif aplikasi LG ThinQ', fecha='2026-11-23',
    titulo='Alternatif aplikasi LG ThinQ: remote LG tanpa akun',
    desc='Mencari alternatif LG ThinQ khusus sebagai remote? Mando TV mengontrol TV LG webOS lewat Wi-Fi, tanpa akun LG dan tanpa iklan.',
    h1='Alternatif aplikasi LG ThinQ untuk TV LG kamu',
    intro='LG ThinQ adalah aplikasi resmi LG yang dirancang untuk seluruh smart home: peralatan rumah tangga, TV, dan lainnya. Kalau kamu hanya ingin remote sederhana untuk TV LG, Mando TV melakukan persis itu lewat Wi-Fi di rumah, tanpa perlu membuat akun LG dan tanpa iklan.',
    pasos=[
      'Hubungkan HP atau PC kamu (iPhone, Android, atau Windows) dan TV LG ke Wi-Fi yang sama.',
      'Unduh Mando TV dan buka. TV LG kamu muncul sendiri di daftar. Ketuk TV tersebut.',
      'Di TV muncul sebuah permintaan. Setujui sekali dengan remote TV, joystick di bawah layar, atau Magic Remote.',
      'Tombol, volume, dan keyboard langsung berfungsi. Kamu tidak butuh akun LG dan tidak perlu mendaftarkan TV.',
      'Opsional: aktifkan "Nyalakan TV dengan perangkat seluler" di pengaturan TV agar kamu juga bisa menyalakan TV dari HP.',
    ],
    extra=[
      ('Mando TV atau LG ThinQ: untuk apa masing-masing', 'Pakai ThinQ kalau kamu ingin mengelola peralatan LG seperti mesin cuci, kulkas, atau AC, atau butuh fitur akun LG. Pakai Mando TV kalau kamu ingin remote TV yang cepat dan sederhana yang juga berfungsi untuk Samsung, Roku, dan Google TV dalam satu aplikasi. Banyak orang menyimpan keduanya: ThinQ untuk peralatan rumah, Mando TV untuk TV.'),
      ('Apa yang dilakukan Mando TV di TV LG', 'Berfungsi dengan Smart TV LG webOS, yaitu sebagian besar model sejak 2014, termasuk LED, NanoCell, QNED, dan OLED. Aplikasi menyediakan tombol arah, OK, Kembali, Beranda, volume, saluran, bisukan, kontrol pemutaran, dan keyboard untuk mengetik di pencarian TV dan di sebagian besar aplikasi. Daftar aplikasi dan daftar input juga gratis. Dengan Pro kamu mendapat tambahan penunjuk seperti Magic Remote.'),
      ('Yang tidak dilakukan Mando TV', 'Aplikasi ini tidak mengontrol peralatan rumah LG, tidak memakai akun LG kamu, dan tidak menggantikan layanan akun LG di TV. Ini adalah remote, bukan hub smart home.'),
      ('Privasi dan iklan', 'Mando TV tidak punya iklan dan tidak punya akun. Aplikasi hanya berbicara dengan TV di dalam jaringan rumah kamu dan menyimpan kunci koneksi terenkripsi di perangkat kamu. Semua fiturnya ada di halaman [Aplikasi remote LG](@lg).'),
      ('Gratis dan Pro', 'Tombol arah, OK, Kembali, Beranda, volume, saluran, tombol angka, keyboard, membuka aplikasi, mengganti input, dan menyalakan atau mematikan TV gratis, tanpa iklan dan tanpa langganan. Touchpad, perintah suara, aplikasi favorit, rutinitas, dan timer tidur adalah bagian dari Mando TV Pro, pembelian sekali bayar tanpa langganan.'),
    ],
    marca='lg',
    faq=[
      ('Bisakah saya mengontrol TV LG tanpa aplikasi LG ThinQ?', 'Bisa. Mando TV tersambung langsung lewat Wi-Fi kamu ke TV LG dengan webOS. Kamu cukup menyetujui satu permintaan di TV, selesai, tanpa akun LG.'),
      ('Apakah Mando TV berfungsi dengan penunjuk LG Magic Remote?', 'Mando TV Pro punya penunjuk yang kamu gerakkan dengan jari di layar HP, mirip cara Magic Remote menggerakkan panah.'),
      ('Apakah Mando TV dari LG?', 'Bukan. Mando TV adalah aplikasi independen dan tidak berafiliasi dengan LG. LG dan ThinQ adalah milik pemiliknya dan hanya disebutkan untuk menjelaskan kompatibilitas.'),
    ]),
  dict(clave='smartthings', corto='Alternatif SmartThings', fecha='2026-11-23',
    titulo='SmartThings bermasalah? Alternatif simpel untuk Samsung',
    desc='SmartThings terlalu lambat atau error? Mando TV mengontrol TV Samsung Tizen langsung lewat Wi-Fi. Tanpa akun Samsung, tanpa iklan. Langkah demi langkah.',
    h1='Alternatif SmartThings untuk TV Samsung',
    intro='SmartThings adalah aplikasi Samsung untuk seluruh smart home, dan remotenya berjalan lewat akun Samsung kamu. Kalau tidak berfungsi lagi atau kamu mencari solusi cepat, Mando TV mengontrol TV Samsung Tizen tahun 2016 ke atas langsung lewat Wi-Fi kamu tanpa akun.',
    pasos=[
      'Hubungkan HP dan TV Samsung ke Wi-Fi yang sama.',
      'Unduh Mando TV dan buka aplikasinya. TV Samsung kamu muncul sendiri di daftar. Ketuk TV tersebut.',
      'TV bertanya apakah kamu mengizinkan koneksi. Pilih "Izinkan" dengan remote atau dengan tombol di TV (hanya sekali, saat pertama kali).',
      'Langsung pakai tombol arah, OK, Kembali, Beranda, volume, saluran, dan keyboard.',
      'Opsional: aktifkan "Nyalakan dengan perangkat seluler" di Pengaturan > Umum > Jaringan > Pengaturan Pakar agar Mando TV juga bisa menyalakan TV.',
    ],
    extra=[
      ('Kenapa remote di HP bisa berhenti berfungsi', 'Penyebabnya biasanya sederhana: HP dan TV berada di Wi-Fi yang berbeda, VPN aktif, atau TV berada di siaga dalam. Di SmartThings, akun Samsung juga bisa jadi masalah, misalnya kalau kamu keluar dari akun. Mando TV berbicara langsung dengan TV di jaringan rumah, tidak ada akun untuk masuk. Tips lainnya ada di [HP tidak menemukan TV](@not-found).'),
      ('Mando TV atau SmartThings: untuk apa masing-masing', 'Pertahankan SmartThings kalau kamu memakainya untuk peralatan rumah Samsung, lampu, atau perangkat smart home lainnya, atau untuk fitur akun Samsung kamu. Pakai Mando TV kalau kamu hanya ingin remote TV yang cepat atau di rumah juga punya perangkat LG, Roku, Google TV, atau Fire TV: satu aplikasi mengontrol semuanya. Kedua aplikasi bisa dipasang di HP yang sama.'),
      ('Kalau kamu tidak sengaja menolak izin', 'Di TV, buka Pengaturan > Umum > Pengelola Perangkat Eksternal > Pengelola Koneksi Perangkat dan ubah Mando TV menjadi diizinkan.'),
      ('Tidak punya remote?', 'Kamu bisa menyetujui permintaan dengan tombol di TV itu sendiri. Panduan [TV Samsung tanpa remote asli](@samsung-lost) menunjukkan caranya.'),
      ('Gratis dan Pro', 'Remote bisa kamu unduh dan pakai gratis, tanpa iklan dan tanpa langganan. Mando TV Pro adalah pembelian sekali bayar yang opsional untuk fitur ekstra.'),
    ],
    marca='samsung',
    faq=[
      ('Bisakah saya mengontrol TV Samsung tanpa SmartThings?', 'Bisa. Mando TV tersambung langsung lewat Wi-Fi kamu ke TV Samsung dengan Tizen. Kamu mengizinkan koneksi sekali di TV, tanpa akun Samsung.'),
      ('Apakah Mando TV juga mengontrol peralatan rumah Samsung?', 'Tidak. Ini hanya remote untuk TV. Untuk peralatan rumah dan perangkat smart home lainnya, tetap pakai SmartThings.'),
      ('Apakah Mando TV dari Samsung?', 'Bukan. Mando TV adalah aplikasi independen dan tidak berafiliasi dengan Samsung. Samsung dan SmartThings adalah milik pemiliknya dan hanya disebutkan untuk menjelaskan kompatibilitas.'),
    ]),
  dict(clave='googletv-alt', corto='Alternatif remote Google TV', fecha='2026-11-23',
    titulo='Remote Google TV bermasalah? Ini alternatifnya',
    desc='Remote Google TV di HP tidak menemukan TV? Mando TV mengontrol Google TV dan Android TV lewat Wi-Fi, tanpa akun Google dan tanpa iklan.',
    h1='Alternatif remote Google TV di HP',
    intro='Remote HP untuk Google TV dan Android TV ada di dalam aplikasi Google sendiri dan terhubung dengan akun Google kamu. Kalau tidak menemukan TV, kamu tidak bisa berbuat apa-apa. Mando TV adalah aplikasi remote terpisah yang dipasangkan dengan kode 6 karakter di layar dan berfungsi tanpa akun Google, di iPhone, HP Android, atau PC Windows.',
    pasos=[
      'Nyalakan TV dan hubungkan HP kamu ke Wi-Fi yang sama.',
      'Unduh Mando TV dan buka aplikasinya. Di daftar, ketuk TV Google TV atau Android TV kamu.',
      'TV menampilkan kode 6 karakter. Masukkan di Mando TV dan ketuk Pasangkan.',
      'Pakai tombol arah, OK, Kembali, Beranda, volume, dan keyboard. Kamu tidak perlu masuk ke akun mana pun.',
      'Opsional: di pengaturan TV, cari Wake on LAN atau "Nyalakan lewat jaringan" agar aplikasi juga bisa menyalakan TV.',
    ],
    extra=[
      ('Kenapa remote HP tidak menemukan TV lagi', 'Biasanya masalahnya di jaringan: HP dan TV berada di Wi-Fi yang berbeda, VPN aktif, atau jaringan tamu memisahkan perangkat. Atasi dulu hal itu karena memengaruhi semua aplikasi remote. Selengkapnya di [HP tidak menemukan TV](@not-found).'),
      ('TV mana saja yang didukung', 'TV dengan Google TV dan Android TV dari Sony, TCL, Hisense, Philips, Sharp, Xiaomi, Toshiba, dan lainnya, serta Chromecast with Google TV, Google TV Streamer, dan Nvidia Shield. Semuanya dipasangkan dengan cara yang sama, sekali dengan kode di layar.'),
      ('Di mana aplikasi Google lebih baik', 'Aplikasi Google juga membantu kamu menemukan tontonan dan mengingat daftar tontonan kamu. Pertahankan untuk itu. Mando TV hanyalah remote, dan sekaligus mengontrol perangkat Samsung, LG, Roku, dan Fire TV dari aplikasi yang sama serta dari PC Windows.'),
      ('Kalau aplikasi remote Android TV yang lama hilang', 'Google memindahkan remote HP dari aplikasi Android TV Remote Control yang lama ke aplikasi Google TV. Kalau kamu mencari remote yang berdiri sendiri, Mando TV adalah salah satu pilihannya.'),
      ('Gratis dan Pro', 'Remote bisa kamu unduh dan pakai gratis, tanpa iklan dan tanpa langganan. Mando TV Pro adalah pembelian sekali bayar yang opsional untuk fitur ekstra.'),
    ],
    marca='android',
    faq=[
      ('Apakah saya butuh akun Google untuk memakai Mando TV dengan Google TV?', 'Tidak. Kode di TV sudah cukup untuk memasangkan.'),
      ('Apakah berfungsi dengan Chromecast with Google TV?', 'Ya. Pemasangannya sama, dengan kode 6 karakter di layar.'),
      ('Bisakah saya memakainya dari iPhone?', 'Bisa. Mando TV tersedia di App Store untuk iPhone dan iPad, di Microsoft Store untuk Windows, dan dalam akses awal gratis di Google Play untuk Android.'),
    ]),
  dict(clave='windows', corto='Remote untuk PC Windows', fecha='2026-11-23',
    titulo='Aplikasi remote untuk Windows: kontrol TV dari PC',
    desc='Kontrol Samsung, LG, Roku, Google TV, atau Fire TV dari PC Windows dengan Mando TV: pintasan keyboard, mini remote, dan Wi-Fi. Ada di Microsoft Store.',
    h1='Aplikasi remote untuk PC Windows',
    intro='Mando TV punya aplikasi Windows yang mengubah PC atau laptop kamu menjadi remote TV lewat jaringan rumah. Ketik di TV dengan keyboard asli kamu, biarkan jendela remote kecil selalu di atas saat bekerja, dan kontrol Samsung, LG, Roku, Google TV, atau Fire TV dengan aplikasi yang sama.',
    pasos=[
      'Pasang Mando TV gratis dari Microsoft Store di PC dengan Windows 10 atau 11.',
      'Pastikan PC dan TV berada di jaringan yang sama, lewat Wi-Fi atau kabel ke router yang sama.',
      'Buka Mando TV. TV muncul di daftar. Klik TV tersebut.',
      'Setujui permintaan di TV kalau diminta (LG, Samsung), atau masukkan kode yang ditampilkan (Google TV, Fire TV).',
      'Klik tombolnya atau ketik pencarian dengan keyboard kamu. Selesai.',
    ],
    extra=[
      ('Pintasan keyboard (Pro)', 'Dengan Pro, keyboard PC kamu menjadi remote: tombol panah untuk bergerak, Enter untuk OK, Backspace atau Esc untuk kembali, plus dan minus untuk volume, M untuk bisukan, dan spasi untuk jeda.'),
      ('Mini remote (Pro)', 'Jendela remote kecil yang tetap berada di atas jendela lain. Dengan begitu kamu bisa mengubah volume atau menjeda tanpa mengganggu pekerjaan.'),
      ('Mengetik di TV dari PC', 'Keyboard layar di TV itu lambat. Di Mando TV kamu mengetik dengan keyboard asli dan teksnya masuk ke kolom pencarian TV. Bagian ini gratis.'),
      ('Detail lainnya', 'Panduan langkah demi langkahnya ada di [Kontrol TV dari PC](@pc). Untuk HP, baca [HP jadi remote lewat Wi-Fi](@wifi).'),
      ('Gratis dan Pro', 'Tombol arah, OK, Kembali, Beranda, volume, saluran, tombol angka, keyboard, membuka aplikasi, mengganti input, dan menyalakan atau mematikan TV gratis, tanpa iklan dan tanpa langganan. Touchpad, perintah suara, aplikasi favorit, rutinitas, dan timer tidur adalah bagian dari Mando TV Pro, pembelian sekali bayar tanpa langganan. Di Windows, kamu membeli Pro lewat Microsoft Store.'),
      ('Perintah suara dari PC (Pro)', 'Dengan Pro kamu bisa berbicara ke TV lewat mikrofon PC. Suara dikenali langsung di PC: untuk itu kamu tidak butuh internet dan tidak perlu mengatur apa pun di Windows. Apa yang kamu ucapkan tidak pernah keluar dari PC dan tidak disimpan. Hanya pada prosesor yang sangat lama aplikasi beralih ke input suara Windows. Untuk itu, pengenalan suara online harus diaktifkan di pengaturan privasi dan bahasa kamu harus ditambahkan di Windows.'),
    ],
    marca=None,
    faq=[
      ('Apakah aplikasi remote untuk Windows butuh Bluetooth atau kabel?', 'Tidak. Aplikasi memakai jaringan rumah kamu. PC dan TV hanya perlu terhubung ke router yang sama.'),
      ('TV apa saja yang bisa saya kontrol dari Windows?', 'TV Samsung dengan Tizen, TV LG dengan webOS, Roku TV dan Player, Google TV dan Android TV, serta Fire TV.'),
      ('Bisakah saya melihat gambar TV di PC atau mendengarnya lewat speaker PC?', 'Tidak. Mando TV hanyalah remote. Aplikasi ini tidak memirror atau men-streaming gambar TV ke komputer.'),
      ('Kenapa suara tidak berfungsi di PC Windows saya?', 'Kontrol suara adalah fitur Pro. Jadi pastikan Pro aktif dan mikrofon PC berfungsi. Di sebagian besar PC, suara dikenali langsung di PC, tanpa internet. Hanya pada prosesor yang sangat lama aplikasi memakai input suara Windows: kalau begitu, aktifkan pengenalan suara online di pengaturan privasi Windows dan tambahkan bahasa kamu di pengaturan bahasa.'),
    ]),
  dict(clave='iphone', corto='Aplikasi remote untuk iPhone', fecha='2026-11-23',
    titulo='Aplikasi remote untuk iPhone: Samsung, LG, Roku, Google TV',
    desc='Pakai iPhone sebagai remote Samsung, LG, Roku, Google TV, dan Fire TV lewat Wi-Fi. Gratis di App Store, tanpa akun dan tanpa iklan.',
    h1='Aplikasi remote untuk iPhone: satu aplikasi untuk semua TV',
    intro='Mando TV mengubah iPhone atau iPad kamu menjadi remote Samsung, LG, Roku, Google TV, Android TV, atau Fire TV lewat Wi-Fi di rumah. Aplikasi ini gratis di App Store, tanpa akun dan tanpa iklan. Berfungsi juga di Android dan Windows.',
    pasos=[
      'Unduh Mando TV gratis dari App Store.',
      'Hubungkan iPhone dan TV ke Wi-Fi yang sama.',
      'Buka Mando TV dan ketuk Izinkan saat iOS meminta akses ke jaringan lokal. Aplikasi membutuhkannya untuk menemukan TV.',
      'Ketuk TV kamu di daftar. Setujui permintaan di TV kalau diminta (LG dan Samsung), atau masukkan kode yang ditampilkan TV (Google TV atau Fire TV).',
      'Pakai tombol, volume, dan keyboard. Kamu sudah tersambung.',
    ],
    extra=[
      ('Berfungsi dengan TV ini', 'LG webOS, Samsung Tizen (tahun 2016 ke atas), Roku TV dan Roku Player, Google TV dan Android TV, serta Fire TV. Halaman per merek: [Samsung](@samsung), [LG](@lg), [Roku](@roku), dan [Android TV](@android).'),
      ('Kenapa aplikasi meminta jaringan lokal', 'iPhone memblokir akses aplikasi ke perangkat di jaringan rumah kamu kecuali kamu mengizinkannya. Kalau TV tidak muncul di daftar, buka Pengaturan > Mando TV dan aktifkan "Jaringan Lokal". Aplikasi hanya berkomunikasi dengan TV kamu di dalam jaringan rumah.'),
      ('Kenapa Mando TV dan bukan aplikasi dari produsen', 'Setiap merek TV punya aplikasi sendiri dan menginginkan pengaturan atau akun sendiri. Mando TV adalah satu aplikasi untuk semuanya, tanpa akun.'),
      ('Gratis dan Pro di iPhone', 'Tombol arah, OK, Kembali, Beranda, volume, saluran, tombol angka, keyboard, membuka aplikasi, mengganti input, dan menyalakan atau mematikan TV gratis, tanpa iklan dan tanpa langganan. Touchpad, perintah suara, aplikasi favorit, rutinitas, dan timer tidur adalah bagian dari Mando TV Pro, pembelian sekali bayar tanpa langganan. Kamu membeli Pro sekali langsung di dalam aplikasi.'),
    ],
    marca=None,
    faq=[
      ('Apakah Mando TV gratis di iPhone?', 'Unduhannya gratis, tanpa iklan. Remote dasar gratis, begitu juga membuka aplikasi dan mengganti input. Fitur ekstra seperti touchpad, perintah suara, dan rutinitas adalah bagian dari Mando TV Pro, pembelian sekali bayar.'),
      ('Apakah berfungsi di iPad?', 'Ya. Aplikasi yang sama berjalan di iPhone dan iPad.'),
      ('Apakah aplikasi remote untuk iPhone butuh Bluetooth atau pemancar inframerah?', 'Tidak di iPhone. iPhone tidak punya pemancar inframerah, jadi kontrol inframerah tidak tersedia di sana, dan opsi Bluetooth hanya untuk Android 9 atau lebih baru, bukan untuk iPhone. Di iPhone, Mando TV mengontrol Smart TV serta Apple TV (beta) lewat Wi-Fi di rumah kamu.'),
    ]),
  dict(clave='firetv', corto='Remote Fire TV', fecha='2026-11-23',
    titulo='Aplikasi remote Fire TV untuk HP dan PC',
    desc='Remote Fire TV di HP: kontrol Fire TV Stick, Fire TV Cube, atau TV dengan Fire TV lewat Wi-Fi, dengan PIN 4 digit. Tanpa aplikasi Amazon.',
    h1='Remote Fire TV untuk HP atau PC kamu',
    intro='Kalau remote Fire TV hilang atau baterainya habis, Mando TV mengontrol Fire TV Stick, Fire TV Cube, atau TV dengan Fire TV bawaan lewat Wi-Fi. Pemasangannya memakai PIN 4 digit. Fire TV baru ada di Mando TV, jadi perbarui aplikasinya terlebih dahulu.',
    pasos=[
      'Perbarui Mando TV ke versi terbaru dari App Store, Microsoft Store, atau Google Play.',
      'Nyalakan Fire TV dan hubungkan HP kamu ke Wi-Fi yang sama.',
      'Buka Mando TV. Fire TV kamu muncul di daftar. Ketuk.',
      'Di layar TV muncul PIN 4 digit. Masukkan di Mando TV. Ini hanya dilakukan sekali.',
      'Pakai tombol arah, OK, Kembali, Beranda, tombol putar, dan keyboard untuk pencarian.',
    ],
    extra=[
      ('Perangkat Fire TV yang didukung', 'Fire TV Stick, Fire TV Stick 4K, Fire TV Cube, dan TV dengan Fire TV bawaan, seperti TV Amazon Fire TV Edition dan beberapa model Hisense. Dukungannya baru, dan sejauh ini kami baru bisa menguji beberapa perangkat nyata. Kalau ada yang tidak berfungsi sesuai harapan, tulis model kamu lewat halaman Bantuan.'),
      ('Menyalakan Fire TV', 'Mando TV tidak menyalakan Fire TV lewat jaringan. Nyalakan TV dengan tombol daya di TV: Fire TV Stick atau Cube yang terpasang biasanya ikut bangun lewat HDMI-CEC, dan pada TV dengan Fire TV bawaan, TV itu sendiri adalah Fire TV. Setelah itu kamu mengontrolnya dari HP.'),
      ('Kalau Fire TV kamu tidak muncul', 'Pastikan kedua perangkat berada di Wi-Fi yang sama dan Fire TV dalam keadaan aktif. Di iPhone, izinkan "Jaringan Lokal" untuk Mando TV di Pengaturan. Lihat [HP tidak menemukan TV](@not-found).'),
      ('Sama sekali tidak punya remote?', 'Fire TV harus menampilkan PIN di layar, jadi TV dan Fire TV harus menyala dan menampilkan gambar. Kalau TV berada di input yang salah, ganti dengan tombol di TV. Lihat [Ganti input tanpa remote](@hdmi).'),
      ('Gratis dan Pro', 'Tombol arah, OK, Kembali, Beranda, volume, saluran, angka, keyboard, membuka aplikasi, mengganti input, dan menyalakan atau mematikan TV gratis, tanpa iklan dan tanpa langganan. Touchpad, perintah suara, aplikasi favorit, rutinitas, dan timer tidur adalah bagian dari Mando TV Pro, pembelian sekali bayar tanpa langganan.'),
    ],
    marca=None,
    faq=[
      ('Apakah saya butuh aplikasi Amazon Fire TV?', 'Tidak. Mando TV tersambung ke Fire TV lewat Wi-Fi dengan PIN. Kamu tidak butuh akun Amazon di HP.'),
      ('Apakah berfungsi dengan TV ber-Fire TV dan dengan Fire TV Stick?', 'Ya, memang untuk itulah dibuat. Dukungannya baru, jadi selalu perbarui aplikasi dan beri tahu kami model yang tidak berfungsi sesuai harapan.'),
      ('Kenapa saya butuh PIN?', 'Fire TV menampilkan PIN 4 digit untuk membuktikan bahwa kamu berada di depan TV. Tidak ada yang bisa memasangkan tanpa melihat layar.'),
    ]),
  dict(clave='firetv-lost', corto='Remote Fire TV hilang', fecha='2026-11-23',
    titulo='Remote Fire TV hilang? Begini HP kamu membantu',
    desc='Remote Fire TV Stick hilang? Kontrol lewat Wi-Fi dengan HP, dipasangkan dengan PIN 4 digit. Tips untuk Wi-Fi baru dan HDMI-CEC.',
    h1='Remote Fire TV hilang: begini cara memakai HP kamu',
    intro='Kalau remote Fire TV Stick, Fire TV Cube, atau Smart TV dengan Fire TV kamu hilang atau tidak berfungsi lagi, HP kamu mengambil alih kontrol selama Fire TV masih tersambung ke Wi-Fi kamu. Pemasangannya lewat PIN 4 digit di layar, jadi untuk itu kamu tidak pernah butuh remote lama.',
    pasos=[
      'Nyalakan TV dengan tombol di badan TV. Fire TV Stick atau Cube yang terpasang biasanya ikut bangun; kalau HDMI-CEC aktif, TV sering pindah sendiri ke inputnya.',
      'Kalau TV menampilkan input lain, ganti dengan tombol input atau sumber di TV. Lihat [Ganti input tanpa remote](@hdmi).',
      'Hubungkan HP kamu ke Wi-Fi yang sama dengan Fire TV.',
      'Unduh Mando TV dan buka aplikasinya. Fire TV kamu muncul di daftar. Ketuk.',
      'TV menampilkan PIN 4 digit. Masukkan di Mando TV. Ini hanya dilakukan sekali.',
      'Pakai tombol arah, OK, Kembali, Beranda, volume, tombol putar, dan keyboard di HP kamu.',
    ],
    extra=[
      ('Coba dulu remote TV (HDMI-CEC)', 'Banyak remote TV bisa mengontrol Fire TV Stick lewat HDMI-CEC. Kalau antarmuka Fire TV terlihat, tekan panah dan OK di remote TV. Kalau tidak terjadi apa-apa, aktifkan CEC di pengaturan TV (Anynet+ di Samsung, SIMPLINK di LG, BRAVIA Sync di Sony) dan di Fire TV aktifkan kontrol perangkat HDMI-CEC di pengaturan tampilan ("Tampilan & Suara").'),
      ('Kalau kamu mengganti Wi-Fi', 'Tanpa remote kamu tidak bisa memasukkan kata sandi Wi-Fi baru di Fire TV, tapi ada jalan keluarnya: di HP kedua, buat hotspot dengan nama dan kata sandi yang persis sama dengan Wi-Fi lama kamu. Fire TV tersambung otomatis ke hotspot itu. Sambungkan HP dengan Mando TV ke hotspot itu, pasangkan dengan PIN, lalu di Fire TV buka Pengaturan > Jaringan dan pilih Wi-Fi baru kamu. Terakhir, sambungkan juga HP kamu ke Wi-Fi yang baru.'),
      ('Memasangkan remote pengganti', 'Sebagian besar remote Fire TV baru dipasangkan dengan menahan tombol Beranda sekitar 10 detik, di dekat Fire TV. Kalau tidak berhasil, buka Pengaturan > Pengontrol & Perangkat Bluetooth > Remote Amazon Fire TV > Tambahkan remote baru. Menu ini juga bisa kamu capai dari HP dengan Mando TV.'),
      ('Fire TV bawaan di dalam TV', 'Pada TV dengan Fire TV bawaan, seperti banyak model Insignia dan Toshiba, langkahnya sama, karena TV itu sendiri adalah Fire TV.'),
      ('Sebelum mulai', 'Dukungan Fire TV baru ada di Mando TV. Perbarui aplikasinya terlebih dahulu. Kalau model kamu tidak merespons sesuai harapan, tulis ke kami lewat [halaman Bantuan](@soporte) dan sebutkan modelnya.'),
      ('Gratis dan Pro', 'Remote bisa kamu unduh dan pakai gratis, tanpa iklan dan tanpa langganan. Mando TV Pro adalah pembelian sekali bayar yang opsional untuk fitur ekstra.'),
    ],
    marca=('firetv', 'Remote Fire TV'),
    faq=[
      ('Bisakah saya mengontrol Fire TV Stick dengan HP tanpa remote?', 'Bisa, selama Fire TV menyala dan tersambung ke Wi-Fi kamu. Mando TV memasangkan lewat PIN 4 digit di TV, jadi kamu tidak butuh remote lama.'),
      ('Apakah berfungsi kalau Fire TV berada di Wi-Fi baru?', 'Tidak langsung, karena HP dan Fire TV harus berada di jaringan yang sama. Hubungkan dulu Fire TV ke jaringan dengan trik hotspot di halaman ini.'),
      ('Apakah saya butuh aplikasi Amazon Fire TV atau akun Amazon?', 'Tidak. Mando TV tersambung lewat jaringan rumah kamu dengan PIN dan tidak membutuhkan akun sendiri.'),
    ]),
  dict(clave='turn-on', corto='Menyalakan TV tanpa remote', fecha='2026-11-23',
    titulo='Menyalakan TV tanpa remote (semua merek)',
    desc='Menyalakan TV tanpa remote: di mana letak tombolnya di Samsung, LG, TCL, Hisense, Sony, dan Vizio. Plus trik HDMI-CEC dan HP.',
    h1='Cara menyalakan TV tanpa remote',
    intro='Hampir semua TV masih punya tombol daya fisik. Hanya saja tersembunyi dengan baik. Berikut letaknya di setiap merek, ditambah dua cara supaya lain kali kamu tidak perlu mencarinya: HDMI-CEC dari konsol atau perangkat streaming, dan menyalakan TV dari HP lewat Wi-Fi.',
    pasos=[
      'Lihat di bawah bagian tengah layar, tepat di belakang logo merek. Banyak TV punya satu tombol kecil atau joystick di sana, menghadap ke bawah.',
      'Kalau tidak ada di sana, rabalah bagian belakang TV di dekat sudut bawah, lalu di tepi kiri dan kanan.',
      'Tekan tombolnya sekali. Di banyak TV dengan satu tombol, saat TV menyala, tekan singkat membuka menu kecil untuk input dan volume, dan tekan lama mematikannya.',
      'Masih belum? Periksa kabel listrik di kedua ujungnya dan coba stopkontak lain. Kalau lampu siaga tidak menyala, TV tidak mendapat listrik.',
      'Begitu TV menyala, atur supaya kamu tidak butuh tombol itu lagi: aktifkan HDMI-CEC dan menyalakan lewat jaringan, keduanya dijelaskan di bawah.',
    ],
    extra=[
      ('Letak tombol daya menurut merek', 'Samsung: satu tombol kontrol atau joystick di bawah bagian tengah layar atau di belakang pada salah satu sudut bawah. LG: tombol joystick di bawah logo LG pada sebagian besar model. TCL dan Hisense: biasanya tombol kecil di bawah bagian tengah layar atau di belakang dekat salah satu sudut bawah. Sony: di belakang atau di tepi samping, di bawah dekat pinggir. Vizio: di belakang, di bawah kiri atau bawah kanan, atau di sisi. Letaknya berbeda tergantung model. Kalau tidak ketemu, cari buku petunjuk dengan nomor model di stiker di bagian belakang.'),
      ('Menyalakan TV lewat konsol atau perangkat streaming (HDMI-CEC)', 'Dengan HDMI-CEC aktif, menyalakan PlayStation, Xbox, Roku Player, Fire TV Stick, atau Chromecast juga menyalakan TV dan pindah ke input yang benar. Setiap merek menamai pengaturannya berbeda: Anynet+ di Samsung, SIMPLINK di LG, BRAVIA Sync di Sony, dan CEC di sebagian besar lainnya. Selengkapnya di [Nyalakan TV dan pindah ke HDMI konsol](@console).'),
      ('Menyalakan TV dari HP', 'Smart TV bisa dibangunkan lewat Wi-Fi kalau kamu mengizinkannya sekali, lalu Mando TV menyalakannya dari HP. Di Samsung, aktifkan "Nyalakan dengan perangkat seluler" di Pengaturan > Umum > Jaringan > Pengaturan Pakar. Di LG, aktifkan "Nyalakan TV dengan perangkat seluler" ([langkah demi langkah](@lg-on)). Di Roku TV, aktifkan "Quick Start TV" di Pengaturan > Sistem > Daya. Di Google TV dan Android TV, cari Wake on LAN atau "Nyalakan lewat jaringan" kalau model kamu punya. Ini dilakukan sekali, saat TV menyala.'),
      ('Kalau kamu tidak menemukan tombolnya', 'Beberapa TV baru menyembunyikan satu-satunya tombol dengan sangat baik sampai terasa seperti tidak ada. Cari tonjolan kecil atau area sensor cahaya di bawah layar: tombolnya sering tepat di sebelahnya. Lewat Wi-Fi, Mando TV membutuhkan TV pernah menyala dan tersambung satu kali. Inframerah adalah pengecualian: di HP Android dengan pemancar inframerah, Mando TV bisa menyalakan TV yang belum pernah diatur, asalkan HP diarahkan ke TV. Inframerah itu baru dan berfungsi dengan merek-merek di daftar kode aplikasi.'),
      ('Gratis dan Pro', 'Remote bisa kamu unduh dan pakai gratis, tanpa iklan dan tanpa langganan. Mando TV Pro adalah pembelian sekali bayar yang opsional untuk fitur ekstra.'),
    ],
    marca=None,
    faq=[
      ('Bisakah saya menyalakan TV dengan HP kalau belum pernah mengaturnya?', 'Tidak lewat Wi-Fi. TV yang mati hanya bangun lewat jaringan kalau fitur menyalakan lewat jaringan sudah diaktifkan sebelumnya. Untuk pertama kali, pakai tombol di TV. Pengecualiannya adalah HP Android dengan pemancar inframerah: Mando TV bisa menyalakan TV tanpa pengaturan lewat inframerah, kalau mereknya ada di daftar kode atau kamu memilih "Merek lain atau tidak tahu".'),
      ('Bagaimana cara menyalakan TV Samsung tanpa remote?', 'Tekan tombol kontrol di bawah bagian tengah layar atau di belakang pada salah satu sudut bawah. Lalu aktifkan "Nyalakan dengan perangkat seluler" agar lain kali HP kamu bisa menyalakannya.'),
      ('Bagaimana cara menyalakan Roku TV tanpa remote?', 'Pakai tombol di TV, biasanya di bawah bagian tengah atau di belakang. Lalu aktifkan "Quick Start TV" di Pengaturan > Sistem > Daya agar Mando TV bisa menyalakannya dari HP kamu.'),
      ('Kenapa TV saya menyala sendiri saat saya menyalakan konsol?', 'Itu HDMI-CEC. Fitur ini praktis, dan kamu bisa mematikannya di pengaturan TV kalau lebih suka begitu.'),
    ]),
  dict(clave='sony', corto='Remote Sony', fecha='2026-11-23',
    titulo='Aplikasi remote Sony untuk HP dan PC',
    desc='Mando TV mengontrol TV Sony Bravia dengan Google TV atau Android TV lewat Wi-Fi. Dukungan beta untuk model 2013 sampai 2015 tanpa Android.',
    h1='Cara mengontrol TV Sony kamu dengan HP',
    intro='Smart TV Sony Bravia yang lebih baru memakai Google TV, model lama sejak 2015 memakai Android TV. Mando TV mengontrol keduanya lewat Wi-Fi dari iPhone, HP Android, atau PC Windows. Aplikasi ini menggantikan remote asli kalau hilang atau baterainya habis.',
    pasos=[
      'Pastikan TV Sony kamu menampilkan layar utama Google TV atau Android TV. Ini berlaku untuk sebagian besar Smart TV Sony Bravia sejak tahun 2015.',
      'Hubungkan HP dan TV ke Wi-Fi yang sama.',
      'Buka Mando TV dan ketuk TV Sony kamu di daftar.',
      'Masukkan kode 6 karakter yang ditampilkan TV di layar (hanya sekali, saat pertama kali). Untuk itu kamu tidak butuh remote.',
      'Pakai tombol arah, OK, Kembali, Beranda, volume, dan keyboard.',
    ],
    extra=[
      ('Menyalakan TV Sony dari HP', 'Model Sony dengan Google TV atau Android TV bisa dibangunkan lewat jaringan kalau "Remote start" diaktifkan. Opsinya biasanya ada di Pengaturan > Jaringan & internet > Remote start (jalurnya bisa sedikit berbeda tergantung model). Lalu ketuk TV di Mando TV saat TV mati, dan aplikasi menyalakannya.'),
      ('Di mana tombol daya di Sony', 'Di sebagian besar TV Bravia, tombolnya ada di belakang, dekat sudut bawah kiri atau kanan, atau di tepi samping. Tekan singkat untuk menyalakan TV. Selengkapnya ada di [Menyalakan TV tanpa remote](@turn-on).'),
      ('TV Sony yang lebih lama', 'TV Sony Bravia tahun 2013 sampai 2015 yang tidak memakai Android didukung di Mando TV dalam status beta. Ini baru dan mungkin belum sempurna. TV menampilkan PIN 4 digit yang harus kamu masukkan di aplikasi. TV Sony lain tanpa Google TV atau Android TV saat ini belum didukung.'),
      ('Gratis dan Pro', 'Remote bisa kamu unduh dan pakai gratis, tanpa iklan dan tanpa langganan. Mando TV Pro adalah pembelian sekali bayar yang opsional untuk fitur ekstra.'),
    ],
    marca='android',
    faq=[
      ('Apakah Mando TV berfungsi dengan TV Sony Bravia?', 'Ya, dengan TV Sony yang memakai Google TV atau Android TV. Itu mencakup sebagian besar Smart TV Sony sejak tahun 2015.'),
      ('Apakah saya butuh aplikasi Sony atau akun Google?', 'Tidak. Mando TV dipasangkan dengan kode di layar TV dan tidak meminta akun.'),
      ('Apakah berfungsi dengan TV Sony Bravia lama tanpa Android?', 'Ya, dalam status beta, pada model Bravia 2013 sampai 2015 tanpa Android. Pemasangannya lewat PIN 4 digit yang ditampilkan di TV.'),
      ('Bisakah saya mengetik dari HP di TV Sony saya?', 'Bisa. Keyboard HP gratis dan mengetik di kotak pencarian TV dan kolom teks lainnya. Untuk YouTube, Mando TV juga punya Keyboard YouTube: ketik atau ucapkan apa yang mau ditonton, lalu YouTube terbuka di TV dengan hasilnya. Netflix hanya menerima keyboard di layarnya sendiri, jadi di sana pakai tombol arah dan OK.'),
    ]),
  dict(clave='tcl', corto='Remote TCL', fecha='2026-11-23',
    titulo='Aplikasi remote TCL untuk HP dan PC',
    desc='Remote TCL hilang? Sebagian besar TV TCL memakai Roku TV atau Google TV. Mando TV mengontrol keduanya lewat Wi-Fi, tanpa akun dan iklan.',
    h1='Cara mengontrol TV TCL kamu dengan HP',
    intro='TCL membuat TV-nya, tetapi perangkat lunaknya adalah Roku TV atau Google TV (pada model lama Android TV). Mando TV mengontrol kedua sistem itu dan berfungsi sebagai remote untuk TV TCL kamu lewat Wi-Fi. Gratis, tanpa akun dan iklan.',
    pasos=[
      'Cari tahu sistem apa yang dipakai TCL kamu. Kalau layar utama menampilkan kotak-kotak kanal yang sederhana, itu Roku TV. Kalau terlihat seperti Google TV atau Android TV dengan baris-baris rekomendasi, itu Google TV.',
      'Hubungkan HP dan TV TCL ke Wi-Fi yang sama.',
      'Buka Mando TV. TCL muncul sendiri di daftar. Ketuk.',
      'Di TCL dengan Roku TV tidak perlu apa-apa lagi. Di TCL dengan Google TV, masukkan kode 6 karakter yang ditampilkan TV di layar (hanya sekali, saat pertama kali).',
      'Pakai panah, OK, Kembali, Beranda, volume, dan keyboard. Nyalakan TV lewat aplikasi kalau kamu sudah mengaktifkan menyalakan lewat jaringan (lihat di bawah).',
    ],
    extra=[
      ('Menyalakan TV TCL dari HP', 'Di TCL Roku TV, aktifkan "Quick Start TV" di Pengaturan > Sistem > Daya. Di TCL Google TV, cari opsi Wake on LAN, "Nyalakan lewat jaringan", atau start jarak jauh di pengaturan jaringan atau daya. Beberapa model tidak menyediakannya. Kalau begitu, nyalakan TV dengan tombol daya fisik, biasanya di bawah bagian tengah atau di belakang.'),
      ('Kalau TCL kamu tidak muncul', 'Pastikan HP dan TV berada di Wi-Fi yang sama. Router dengan jaringan 2,4 GHz dan 5 GHz yang terpisah bisa membuat perangkat saling tidak terlihat. Di iPhone, izinkan "Jaringan Lokal" untuk Mando TV di Pengaturan. Kamu juga bisa menambahkan TV dengan memasukkan alamat IP-nya. Baca [HP tidak menemukan TV](@not-found).'),
      ('Selengkapnya tentang TCL kamu', 'Untuk TCL dengan Roku TV, lihat [Aplikasi remote Roku](@roku); untuk TCL dengan Google TV atau Android TV, lihat [Aplikasi remote Android TV](@android).'),
      ('Gratis dan Pro', 'Tombol arah, OK, Kembali, Beranda, volume, saluran, angka, keyboard, membuka aplikasi, mengganti input, dan menyalakan atau mematikan TV gratis, tanpa iklan dan tanpa langganan. Touchpad, perintah suara, aplikasi favorit, rutinitas, dan timer tidur adalah bagian dari Mando TV Pro, pembelian sekali bayar tanpa langganan.'),
    ],
    marca=None,
    faq=[
      ('Apakah Mando TV berfungsi dengan semua TV TCL?', 'Berfungsi dengan TV TCL yang memakai Roku TV, Google TV, atau Android TV, yaitu sebagian besar Smart TV TCL. TCL yang bukan Smart TV tidak bisa dikontrol lewat Wi-Fi.'),
      ('Apakah saya butuh aplikasi TCL atau akun TCL?', 'Tidak. Mando TV tersambung langsung lewat Wi-Fi di rumah kamu dan tidak membutuhkan akun.'),
      ('TCL saya meminta kode. Di mana kodenya?', 'Model TCL dengan Google TV dan Android TV menampilkan kode 6 karakter di layar. Masukkan persis seperti itu di Mando TV. TCL dengan Roku TV tidak meminta kode.'),
    ]),
  dict(clave='hisense', corto='Remote Hisense', fecha='2026-11-23',
    titulo='Aplikasi remote Hisense: apa yang berfungsi di HP',
    desc='Remote Hisense dengan Mando TV: kontrol untuk VIDAA, Roku TV, Google TV, dan Fire TV lewat Wi-Fi. Gambaran jujur tentang apa yang berfungsi.',
    h1='Aplikasi remote Hisense: apa yang berfungsi dan apa yang tidak',
    intro='TV Hisense tidak semuanya sama di dalamnya. Tergantung model, TV ini memakai sistem VIDAA milik Hisense sendiri, Roku TV, Google TV, atau Fire TV. Mando TV berfungsi sebagai remote Hisense di keempat sistem itu, dengan satu pengecualian pada beberapa model VIDAA yang lebih baru. Berikut cara mengetahui sistem yang kamu punya dan apa yang bisa kamu harapkan.',
    pasos=[
      'Periksa sistem apa yang dipakai Hisense kamu. VIDAA adalah antarmuka Hisense sendiri. Roku TV menampilkan kotak-kotak kanal. Google TV menampilkan baris-baris rekomendasi. Fire TV menampilkan layar utama Fire TV dengan baris-baris Amazon.',
      'Hubungkan HP dan TV Hisense ke Wi-Fi yang sama.',
      'Buka Mando TV. TV muncul sendiri di daftar. Ketuk.',
      'Model VIDAA dan Fire TV mungkin menampilkan PIN empat digit; Google TV menampilkan kode enam karakter. Masukkan ke aplikasi. Roku TV tidak meminta apa pun. Ini hanya dilakukan sekali.',
      'Pakai panah, OK, Kembali, Beranda, volume, dan keyboard dari HP kamu.',
    ],
    extra=[
      ('Hisense dengan Roku TV atau Google TV', 'Keduanya berfungsi penuh seperti TV Roku atau Google TV lainnya. Detailnya ada di halaman [Aplikasi remote Roku](@roku) dan [Aplikasi remote Android TV](@android).'),
      ('Hisense dengan Fire TV', 'Dukungan Fire TV baru ada di Mando TV. Perbarui aplikasi ke versi terbaru dari toko kamu. Cara pemasangan dengan PIN dijelaskan di halaman [Aplikasi remote Fire TV](@firetv). Kalau ada yang tidak berfungsi sesuai harapan, tulis ke kami lewat halaman Bantuan dan sebutkan model kamu.'),
      ('Hisense dengan VIDAA', 'Sebagian besar model VIDAA berfungsi: tombol, volume, keyboard, aplikasi, dan input. Beberapa model VIDAA yang lebih baru hanya menerima aplikasi Hisense resmi. Mando TV mendeteksinya saat menyambung dan memberi tahu kamu dengan jelas, bukannya gagal diam-diam. Dalam kasus itu, aplikasi Hisense untuk model kamu, tombol di TV, atau remote asli adalah jalan yang tepat.'),
      ('Menyalakan Hisense dari HP', 'Di Hisense Roku TV, aktifkan "Quick Start TV" di Pengaturan > Sistem > Daya. Di Google TV, cari opsi Wake on LAN atau "Nyalakan lewat jaringan". Kalau tidak ada, pakai tombol daya di TV.'),
      ('Gratis dan Pro', 'Tombol arah, OK, Kembali, Beranda, volume, saluran, tombol angka, keyboard, membuka aplikasi, mengganti input, dan menyalakan atau mematikan TV gratis, tanpa iklan dan tanpa langganan. Touchpad, perintah suara, aplikasi favorit, rutinitas, dan timer tidur adalah bagian dari Mando TV Pro, pembelian sekali bayar tanpa langganan.'),
    ],
    marca=None,
    faq=[
      ('Apakah Mando TV berfungsi dengan Hisense VIDAA?', 'Ya, dengan sebagian besar model VIDAA. Beberapa yang lebih baru hanya menerima aplikasi Hisense resmi; Mando TV mendeteksinya dan memberi tahu kamu. TV Hisense dengan Roku TV, Google TV, atau Fire TV juga didukung.'),
      ('Bagaimana saya tahu Hisense saya Roku TV, Google TV, atau Fire TV?', 'Lihat layar utama. Roku TV punya kotak-kotak sederhana dan logo Roku saat dinyalakan. Google TV punya baris-baris rekomendasi. Fire TV punya layar utama Amazon Fire TV. Nama model di Pengaturan > Tentang juga memberi petunjuk.'),
      ('Apakah saya butuh akun Hisense atau Google?', 'Tidak. Mando TV tersambung langsung lewat Wi-Fi di rumah kamu dan tidak punya akun sendiri.'),
    ]),
  dict(clave='philips', corto='Remote Philips', fecha='2026-11-23',
    titulo='Aplikasi remote Philips: Roku TV, Google TV, Android TV',
    desc='Mando TV mengontrol TV Philips dengan Roku TV, Google TV, atau Android TV lewat Wi-Fi, dari HP atau PC. Titan OS tidak didukung.',
    h1='Cara mengontrol TV Philips dengan HP',
    intro='TV Philips memakai sistem yang berbeda tergantung negara dan tahun: Roku TV di Amerika Serikat, Google TV atau Android TV di banyak negara, dan Titan OS pada beberapa model Eropa yang lebih baru. Mando TV mengontrol model dengan Roku TV, Google TV, dan Android TV lewat Wi-Fi.',
    pasos=[
      'Periksa layar utama. Roku TV menampilkan kotak-kotak. Google TV dan Android TV menampilkan baris-baris rekomendasi dari Google. Titan OS punya layar utama sendiri.',
      'Hubungkan HP dan TV ke Wi-Fi yang sama.',
      'Buka Mando TV dan ketuk TV Philips kamu di daftar.',
      'Roku TV tidak meminta apa pun. Google TV dan Android TV menampilkan kode 6 karakter: masukkan sekali di aplikasi.',
      'Pakai tombol arah, OK, Kembali, Beranda, volume, dan keyboard.',
    ],
    extra=[
      ('Philips Roku TV', 'Berfungsi seperti TV Roku lainnya. Agar bisa dinyalakan dari HP, aktifkan "Quick Start TV" di Pengaturan > Sistem > Daya. Selengkapnya di halaman [Aplikasi remote Roku](@roku).'),
      ('Philips dengan Google TV atau Android TV', 'Mencakup banyak model Ambilight. Dipasangkan dengan kode di layar. Agar bisa dinyalakan dari HP, cari Wake on LAN atau "Nyalakan lewat jaringan" di pengaturan jaringan atau daya. Beberapa model tidak punya opsi ini. Selengkapnya di halaman [Aplikasi remote Android TV](@android).'),
      ('TV Philips lama tanpa Android', 'TV Philips tahun 2011 sampai 2015 yang tidak memakai Android didukung di Mando TV dalam versi beta. Fitur ini baru dan tidak butuh kode pemasangan.'),
      ('Philips dengan Titan OS', 'Titan OS adalah sistem lain yang saat ini tidak dikontrol Mando TV, dan lebih baik kami katakan dengan jelas. Model Philips yang lebih baru tanpa Android juga belum tercakup.'),
      ('Gratis dan Pro', 'Remote bisa kamu unduh dan pakai gratis, tanpa iklan dan tanpa langganan. Mando TV Pro adalah pembelian sekali bayar yang opsional untuk fitur ekstra.'),
    ],
    marca=None,
    faq=[
      ('Apakah Mando TV berfungsi dengan TV Philips?', 'Dengan TV Philips yang memakai Roku TV, Google TV, atau Android TV, ya, dan dalam versi beta dengan TV Philips tahun 2011 sampai 2015 tanpa Android. Model dengan Titan OS tidak didukung.'),
      ('Apakah Mando TV mengontrol Ambilight?', 'Mando TV adalah remote: aplikasi ini mengirim tombol, jadi dengan panah dan OK kamu bisa menuju pengaturan Ambilight. Tidak ada kontrol Ambilight tersendiri.'),
      ('Apakah saya butuh akun Philips atau Google?', 'Tidak. Mando TV tersambung lewat Wi-Fi di rumah kamu dan tidak membutuhkan akun.'),
    ]),
]
OTRAS_GUIAS += [
  ('no-sub', 'Aplikasi remote tanpa langganan dan tanpa iklan'),
  ('roku-app-alt', 'Alternatif aplikasi Roku: satu aplikasi untuk semua TV'),
  ('lg-thinq', 'Alternatif aplikasi LG ThinQ untuk TV LG kamu'),
  ('smartthings', 'Alternatif SmartThings untuk TV Samsung'),
  ('googletv-alt', 'Alternatif remote Google TV di HP'),
  ('windows', 'Aplikasi remote untuk PC Windows'),
  ('iphone', 'Aplikasi remote untuk iPhone: satu aplikasi untuk semua TV'),
  ('firetv', 'Remote Fire TV untuk HP atau PC kamu'),
  ('firetv-lost', 'Remote Fire TV hilang: begini cara memakai HP kamu'),
  ('turn-on', 'Cara menyalakan TV tanpa remote'),
  ('sony', 'Cara mengontrol TV Sony kamu dengan HP'),
  ('tcl', 'Cara mengontrol TV TCL kamu dengan HP'),
  ('hisense', 'Aplikasi remote Hisense: apa yang berfungsi dan apa yang tidak'),
  ('philips', 'Cara mengontrol TV Philips dengan HP'),
]
# <<< guías traídas del inglés
