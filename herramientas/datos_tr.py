# Textos en turco (sen) de mandotv.app. Los usa generar_idiomas.py. Escritos para las búsquedas de Turquía.
# Las claves de las páginas (lg, lost-tv, ...) y sus rutas están en idiomas_sitio.py.
# Los nombres de menús de cada marca (LG, Samsung, Roku, Android TV, iPhone) siguen lo que la app usa en turco
# (lib/l10n/app_tr.arb del proyecto de la app).

UI = dict(
  locale='tr_TR',
  aria_home='Mando TV, ana sayfa', aria_main='Ana menü', nav_que='Özellikler', nav_ayuda='Yardım', nav_contacto='İletişim',
  asunto='Merhaba%20Mando%20TV', inicio='Ana sayfa', privacidad='Gizlilik', aria_pie='Sayfa altı', aria_ruta='Gezinti yolu',
  aria_marcas='Markalar ve rehberler', hecho='Şili’de geliştirildi',
  aviso='Mando TV bağımsız bir uygulamadır. Adı geçen TV üreticileriyle, Google, Amazon, Apple veya Roku ile bağlantısı yoktur ve bunlar tarafından desteklenmez. Markalar sahiplerine aittir ve yalnızca uyumluluğu belirtmek için anılır. Android TV ve Google TV, Google LLC’nin ticari markalarıdır. Apple TV, Apple Inc.’in ticari markasıdır.',
  bajar='Ücretsiz indir', descarga='İndir:', anticipada='Erken erişim:',
  apple_aria='Mando TV’yi App Store’dan ücretsiz indir', ms_aria='Mando TV’yi Microsoft Store’dan ücretsiz indir',
  gp_aria='Android için Mando TV’ye Google Play’de erken erişim', aria_desc='Mando TV’yi indir',
  b_como_btn='Nasıl bağlanırsın', b_tiendas_label='Mağazalarda mevcut',
  b_nota='iPhone, iPad, Mac, Android ve Windows. Ücretsiz indirme, reklamsız. Pro tek seferlik satın alımdır, abonelik yok.',
  b_compat='Uyumlu televizyonlar', b_otras='Diğer markalar', b_otras_p='Mando TV bu markaların hepsini aynı uygulamayla kontrol eder:',
  g_guias='Rehberler', g_ver='Adımları gör', g_pasos='Adım adım', g_hazlo='Mando TV ile nasıl yapılır',
  g_tiendas='Mando TV, televizyonun için evrensel bir kumandadır. Ücretsiz indir, reklam ve hesap yok. Pro isteğe bağlı, tek seferlik bir satın alımdır, abonelik yok. iPhone, iPad, Windows ve Android için:',
  g_nota='Android: Google Play’de ücretsiz erken erişim. <a href="{enlace}">İki adımda katıl</a> ve mağazaya ulaşmamıza yardım et.',
  g_mas_pagina='Daha fazla ayrıntıyı {enlace} sayfasında bulabilirsin.', g_mas_marca='Markaya göre daha fazla ayrıntı:',
  g_faq='Sık sorulan sorular', g_mas='Diğer rehberler', g_todas='Tüm rehberler', g_ayuda='Yardım ve destek',
  g_idiomas='Bu rehber diğer dillerde',
)

# Pie de página y listas de marcas/guías: (clave, texto)
PIE = [
  ('samsung', 'Samsung kumanda'),
  ('lg', 'LG kumanda'),
  ('roku', 'Roku kumanda'),
  ('android', 'Android TV kumanda'),
  ('guias', 'Tüm rehberler'),
  ('lost-tv', 'Kumanda kayboldu'),
  ('lost-lg', 'LG kumanda kayboldu'),
  ('lg-on', 'LG TV’yi telefonla açma'),
  ('hdmi', 'Kumandasız HDMI girişini değiştirme'),
  ('androidtv', 'Kumandasız Android TV'),
  ('console', 'Kumandasız TV ve konsol HDMI'),
  ('samsung-lost', 'Kumandasız Samsung TV'),
  ('roku-lost', 'Roku kumanda kayboldu'),
  ('roku-403', 'Roku uygulaması çalışmıyor'),
  ('androidtv-code', 'Android TV eşleştirme kodu'),
  ('not-found', 'Telefon TV’yi bulamıyor'),
  ('wifi', 'Telefonu Wi-Fi ile kumanda olarak kullanma'),
  ('pc', 'TV’yi bilgisayarla kontrol etme'),
]
NOMBRE_OTRA = {'lg': 'LG kumanda uygulaması', 'samsung': 'Samsung kumanda uygulaması', 'roku': 'Roku kumanda uygulaması',
               'android': 'Android TV ve Google TV kumanda uygulaması'}
PAGINA_MARCA = {'lg': 'LG kumanda uygulaması', 'samsung': 'Samsung kumanda uygulaması', 'roku': 'Roku kumanda uygulaması',
                'android': 'Android TV kumanda uygulaması'}

OTRAS_GUIAS = [
  ('lg-on', 'LG TV’yi telefonla açma'),
  ('lost-tv', 'Kumanda kayboldu: yapabileceklerin'),
  ('lost-lg', 'LG kumanda kayboldu: telefonunu böyle kullanırsın'),
  ('hdmi', 'Kumandasız TV’nin HDMI girişini değiştirme'),
  ('androidtv', 'Kumandasız Android TV: telefonunu böyle kullanırsın'),
  ('console', 'Kumandasız TV’yi açma ve konsolun HDMI girişine geçme'),
  ('samsung-lost', 'Orijinal kumandasız Samsung TV: telefonunu böyle kullanırsın'),
  ('roku-lost', 'Roku kumanda kayboldu: telefonunu böyle kullanırsın'),
  ('roku-403', 'Roku uygulaması çalışmıyor: 403 hatasını çözme'),
  ('androidtv-code', 'Android TV eşleştirme kodu istiyor: yapman gerekenler'),
  ('not-found', 'Telefonun TV’yi bulamıyor: şunlara bak'),
  ('wifi', 'Telefonunu Wi-Fi ile kumanda olarak kullanma'),
  ('pc', 'Windows bilgisayarla TV’yi kontrol etme'),
]

INDICE = dict(
  titulo='Rehberler: TV’yi telefonla kontrol etme | Mando TV',
  desc='Adım adım rehberler: telefonu veya bilgisayarı kumanda yap, TV’yi aç, HDMI girişini değiştir, Samsung, LG ve Roku sorunlarını çöz.',
  h1='Rehberler: telefonu kumanda olarak kullanma',
  intro='Samsung, LG, Roku veya Android TV televizyonunun kumandasını Mando TV ile bağlamak, TV’yi açmak ve sorunları çözmek için basit adımlar.',
  h2_guias='Tüm rehberler', h2_marcas='Markaya göre kumanda uygulaması',
  marcas_extra=[('sony', 'Sony kumanda uygulaması'), ('philips', 'Philips kumanda uygulaması')],
)

MARCAS = [
  dict(clave='lg', color='#e0457b', corto='LG',
    titulo='LG TV kumanda uygulaması, telefonda ücretsiz | Mando TV',
    desc='Telefonun veya bilgisayarın, webOS’lu LG TV için Wi-Fi ile kumanda olsun. Tuşlar, klavye, uygulamalar, girişler ve açma ücretsiz; imleç Pro’da.',
    h1='Telefonda LG TV kumanda uygulaması',
    intro='Mando TV, LG televizyonlar için bir kumanda uygulamasıdır: evindeki Wi-Fi üzerinden telefonunu veya bilgisayarını, webOS’lu LG akıllı TV’nin kumandasına çevirir. Kumandayı kaybettiğinde, piller bittiğinde ya da sadece daha hızlı yazmak istediğinde işe yarar.',
    compat='webOS’lu LG akıllı TV’ler (2014’ten bu yana çoğu LG akıllı TV modeli). LED, NanoCell, QNED ve OLED televizyonlarla çalışır. NetCast’li eski LG akıllı TV’ler (2011-2014, webOS öncesi) beta olarak yeni destekleniyor: TV’nin gösterdiği 6 haneli anahtarla eşleşir.',
    h2=dict(funciones='LG TV’nde yapabileceklerin', como='LG TV’ni Mando TV ile nasıl bağlarsın',
            encender='LG TV’yi telefonla açma', preguntas='LG hakkında sorular', guias='LG için rehberler'),
    funciones=[
      ('Tüm tuşlar', 'Yön tuşları, OK, geri, ana ekran, ses, kanallar, sessiz ve oynatma.'),
      ('Magic Remote gibi imleç (Pro)', 'Parmağınla ekranda oku hareket ettir, tıpkı LG Magic Remote’ta olduğu gibi.'),
      ('İki klavye', 'TV’nin aramasına ve çoğu uygulamaya telefonunun klavyesiyle yaz. YouTube Klavyesi (Pro) ile ne izleyeceğini yaz ya da söyle, YouTube TV’de sonuçlarla açılır.'),
      ('Uygulamalar ve girişler', 'Uygulamalarını aç ve HDMI, canlı TV, AirPlay veya Screen Share’e geç.'),
      ('Ses çıkışı (Pro)', 'TV hoparlörleri ile ses çubuğun arasında geçiş yap.'),
      ('TV’yi açma', 'Kapalıysa Mando TV onu ağ üzerinden açar ve kendiliğinden bağlanır.'),
    ],
    pasos=[
      'Telefonunu ve TV’yi aynı Wi-Fi ağına bağla.',
      'Mando TV’yi aç: LG TV’n listede kendiliğinden görünür. Üzerine dokun.',
      'TV’de izin isteyen bir soru çıkar. Alışık olduğun kumandayla onayla (yalnızca ilk seferde).',
    ],
    encender='LG TV’nin ayarlarını aç ve “Mobil cihazla TV’yi aç” seçeneğini ara (Ayarlar, Genel, Cihazlar, Harici Cihazlar altında; eski modellerde Bağlantı, Mobil Bağlantı Yönetimi). “Wi-Fi üzerinden aç”ı etkinleştir. “Hızlı Başlatma+” varsa onu da etkinleştir. Bundan sonra, kapalı TV’ye Mando TV’de dokunduğunda uygulama açmak isteyip istemediğini sorar ve kendiliğinden bağlanır.',
    faq=[
      ('Mando TV’yi kullanmak için Magic Remote’a ihtiyacım var mı?', 'Yalnızca ilk seferde, ekrandaki soruyu onaylamak için. Sonrasında telefonun yeter.'),
      ('Mando TV, LG ThinQ uygulamasının yerini tutar mı?', 'TV’yi kontrol etmek için evet: LG hesabına ihtiyacın yok ve TV’yi kaydettirmen gerekmiyor. Mando TV doğrudan Wi-Fi ağın üzerinden bağlanır.'),
      ('LG TV’mi telefonla açabilir miyim?', 'Evet, TV’de “Mobil cihazla TV’yi aç” seçeneğini etkinleştirdiysen ve TV açıkken bir kez bağlandıysan.'),
      ('webOS öncesi eski LG TV’lerle çalışır mı?', 'Betada evet, 2011-2014 arası LG NetCast akıllı TV’lerle. TV’nin gösterdiği 6 haneli anahtarla eşleşirler. Özellik yeni ve henüz pürüzleri olabilir.'),
    ],
    guias=[('lg-on', 'LG TV’yi telefonla nasıl açarsın'),
           ('lost-lg', 'LG kumanda kayboldu: telefonunu böyle kullanırsın'),
           ('hdmi', 'Kumandasız TV’nin HDMI girişini değiştirme'),
           ('guias', 'TV’yi telefonla kontrol etmek için tüm rehberler')]),
  dict(clave='samsung', color='#3d7bff', corto='Samsung',
    titulo='Samsung TV kumanda uygulaması, telefonda | Mando TV',
    desc='Telefonun veya bilgisayarın, Tizen’li Samsung TV için Wi-Fi ile kumanda olsun. Tuşlar, klavye, uygulamalar ve açma ücretsiz; dokunmatik yüzey Pro’da. Reklamsız.',
    h1='Telefonda Samsung TV kumanda uygulaması',
    intro='Mando TV, Samsung televizyonlar için bir kumanda uygulamasıdır: evindeki Wi-Fi üzerinden telefonunu veya bilgisayarını, Samsung akıllı TV’nin kumandasına çevirir. Samsung hesabına ihtiyacın yok ve TV’yi kaydettirmen gerekmiyor.',
    compat='Tizen’li Samsung akıllı TV’ler, 2016 ve sonrası üretim (Crystal UHD, QLED, Neo QLED, The Frame ve OLED gibi seriler).',
    h2=dict(funciones='Samsung TV’nde yapabileceklerin', como='Samsung TV’ni Mando TV ile nasıl bağlarsın',
            encender='Samsung TV’yi telefonla açma', preguntas='Samsung hakkında sorular', guias='Samsung için rehberler'),
    funciones=[
      ('Tüm tuşlar', 'Yön tuşları, OK, geri, ana ekran, ses, kanallar, sessiz ve kaynak.'),
      ('Dokunmatik yüzey (Pro)', 'Yön tuşlarını aramadan menülerde parmağını kaydırarak gez.'),
      ('İki klavye', 'TV’nin aramasına ve çoğu uygulamaya telefonunun klavyesiyle yaz. YouTube Klavyesi (Pro) ile ne izleyeceğini yaz ya da söyle, YouTube TV’de sonuçlarla açılır.'),
      ('Uygulamalar', 'Netflix’i, YouTube’u, Prime Video’yu ve diğer uygulamalarını tek dokunuşla aç.'),
      ('TV’yi açma', 'Kapalıysa Mando TV onu ağ üzerinden açar ve kendiliğinden bağlanır.'),
      ('Hesapsız', 'Bağlantı doğrudan Wi-Fi ağın üzerinden kurulur, internete çıkmadan.'),
    ],
    pasos=[
      'Telefonunu ve TV’yi aynı Wi-Fi ağına bağla.',
      'Mando TV’yi aç: Samsung TV’n listede kendiliğinden görünür. Üzerine dokun.',
      'TV, bağlantıya izin verip vermediğini sorar. Kumandayla “İzin ver”i seç (yalnızca ilk seferde).',
    ],
    encender='Samsung TV’de Ayarlar > Genel > Ağ > Uzman Ayarları altında “Mobil Cihazla Aç” seçeneğini etkinleştir. Bundan sonra, kapalı TV’ye Mando TV’de dokunduğunda uygulama açmak isteyip istemediğini sorar ve kendiliğinden bağlanır.',
    faq=[
      ('İzni yanlışlıkla reddettim. Ne yapmalıyım?', 'TV’de Ayarlar > Genel > Harici Aygıt Yöneticisi > Aygıt Bağlantı Yöneticisi’ne git ve Mando TV’yi izinli yap.'),
      ('Mando TV, SmartThings’in yerini tutar mı?', 'TV’yi kontrol etmek için evet, üstelik Samsung hesabı olmadan. Mando TV doğrudan Wi-Fi ağın üzerinden bağlanır.'),
      ('Eski Samsung TV’lerle çalışır mı?', 'Tizen’li, 2016 ve sonrası Samsung TV’lerle çalışır. Daha eski modeller henüz desteklemediğimiz farklı bir sistem kullanır.'),
    ],
    guias=[('samsung-lost', 'Orijinal kumandasız Samsung TV: telefonunu böyle kullanırsın'),
           ('smartthings', 'Samsung TV’ler için SmartThings alternatifi'),
           ('turn-on', 'Kumandasız TV nasıl açılır'),
           ('hdmi', 'Kumandasız TV’nin HDMI girişini değiştirme'),
           ('guias', 'TV’yi telefonla kontrol etmek için tüm rehberler')]),
  dict(clave='roku', color='#a77bff', corto='Roku',
    titulo='Roku kumanda uygulaması, telefonda ücretsiz | Mando TV',
    desc='Telefonun veya bilgisayarın, Roku TV ve Roku oynatıcılar için Wi-Fi ile kumanda olsun. Tuşlar, klavye, kanallar, girişler ve açma ücretsiz.',
    h1='Telefonda Roku kumanda uygulaması',
    intro='Mando TV, Roku için bir kumanda uygulamasıdır: evindeki Wi-Fi üzerinden telefonunu veya bilgisayarını Roku’nun kumandasına çevirir. Roku TV cihazlarıyla ve HDMI girişine takılan Roku oynatıcılarla çalışır.',
    compat='Roku TV cihazları (TCL, Hisense, Philips, Sharp, JVC ve diğerleri) ve Roku oynatıcılar (Express, Streaming Stick, Ultra).',
    h2=dict(funciones='Roku’nda yapabileceklerin', como='Roku’nu Mando TV ile nasıl bağlarsın',
            encender='Roku’yu telefonla açma', preguntas='Roku hakkında sorular', guias='Roku için rehberler'),
    funciones=[
      ('Tüm tuşlar', 'Yön tuşları, OK, geri, ana ekran, ses, sessiz, tekrar ve oynatma.'),
      ('İki klavye', 'Roku aramasına ve izin veren kanallara telefonunun klavyesiyle yaz. YouTube Klavyesi (Pro) ile ne izleyeceğini yaz ya da söyle, YouTube TV’de sonuçlarla açılır.'),
      ('Kanallar', 'Netflix’i, YouTube’u ve diğer Roku kanallarını tek dokunuşla aç.'),
      ('Girişler', 'Roku TV’de uygulamadan HDMI, anten veya AV’ye geç.'),
      ('TV’yi açma', 'Hızlı başlatması olan Roku TV cihazlarını Mando TV telefonundan açar.'),
      ('Eşleştirmesiz', 'Roku kod istemez: listede ona dokun ve bağlanmış olursun.'),
      ('Kumandayı çaldırma', 'Roku kumandanın hoparlörü varsa, örneğin Roku Voice Remote Pro, Mando TV onu çaldırır ve bulmana yardım eder. Ücretsiz, Roku’nun açık olması gerekir.'),
    ],
    pasos=[
      'Telefonunu ve Roku’yu aynı Wi-Fi ağına bağla.',
      'Mando TV’yi aç: Roku’n listede kendiliğinden görünür. Üzerine dokun.',
      'Bağlantı kurulmazsa Roku’da Ayarlar > Sistem > Gelişmiş sistem ayarları > Mobil uygulamalarla kontrol’e git ve ağ erişimini Varsayılan veya Permissive yap (daha yeni Roku yazılımında “Mobil uygulamalarla kontrol” ayarını Etkin yap).',
    ],
    encender='Roku TV cihazlarında Ayarlar > Sistem > Güç altında “TV hızlı başlatma”yı etkinleştir. Başka bir TV’ye takılı Roku oynatıcılar bu şekilde açılamaz. Bundan sonra, kapalı TV’ye Mando TV’de dokunduğunda uygulama açmak isteyip istemediğini sorar ve kendiliğinden bağlanır.',
    faq=[
      ('Roku Express veya Streaming Stick ile çalışır mı?', 'Evet. Tüm Roku oynatıcılar ve Roku TV cihazları aynı şekilde kontrol edilir.'),
      ('Mando TV Roku’mu bulamıyor. Ne yapmalıyım?', 'İkisinin de aynı Wi-Fi ağında olduğunu ve Roku’da “Mobil uygulamalarla kontrol”ün kapalı olmadığını kontrol et. Roku’yu IP adresiyle de ekleyebilirsin.'),
      ('Roku hesabına ihtiyacım var mı?', 'Hayır. Mando TV doğrudan Wi-Fi ağın üzerinden bağlanır.'),
    ],
    guias=[('roku-403', 'Roku uygulaması çalışmıyor (403 hatası)'),
           ('roku-lost', 'Roku kumanda kayboldu: telefonunu böyle kullanırsın'),
           ('tcl', 'TCL kumanda uygulaması'),
           ('hisense', 'Hisense kumanda uygulaması'),
           ('philips', 'Philips kumanda uygulaması'),
           ('guias', 'TV’yi telefonla kontrol etmek için tüm rehberler')]),
  dict(clave='android', color='#2fbf8f', corto='Android TV ve Google TV',
    titulo='Google TV ve Android TV kumanda uygulaması | Mando TV',
    desc='Google TV ve Android TV (Sony, TCL, Hisense, Xiaomi) kumandası telefonunda, Wi-Fi ile. Tuşlar, uygulamalar ve açma ücretsiz; dokunmatik yüzey Pro’da.',
    h1='Telefonda Google TV ve Android TV kumanda uygulaması',
    intro='Mando TV, Android TV için bir kumanda uygulamasıdır: evindeki Wi-Fi üzerinden telefonunu veya bilgisayarını Android TV ya da Google TV televizyonunun kumandasına çevirir. iPhone’dan ve Windows’tan da çalışır.',
    compat='Sony, Philips, TCL, Hisense, Sharp, Xiaomi, Toshiba, Panasonic, Haier, Skyworth, JVC, Thomson, Motorola, OnePlus, iFFALCON, Kogan, Vu ve diğer markaların Google TV veya Android TV’li televizyonları, ayrıca Google TV’li Chromecast, Google TV Streamer, onn. ve Nvidia Shield. Bu markaların bir kısmı farklı sistemli modeller de satar: TV’n Google TV ana ekranını gösteriyorsa veya Google Play Store’u varsa Mando TV onu kontrol eder.',
    h2=dict(funciones='Android TV’nde yapabileceklerin', como='Android TV’ni Mando TV ile nasıl bağlarsın',
            encender='Android TV’yi telefonla açma', preguntas='Android TV hakkında sorular', guias='Android TV için rehberler'),
    funciones=[
      ('Tüm tuşlar', 'Yön tuşları, OK, geri, ana ekran, ses, sessiz ve oynatma.'),
      ('Dokunmatik yüzey (Pro)', 'Google TV menülerinde hızlı gezinmek için parmağını kaydır.'),
      ('İki klavye', 'TV’nin aramasına ve çoğu uygulamaya telefonunun klavyesiyle yaz. YouTube Klavyesi (Pro) ile ne izleyeceğini yaz ya da söyle, YouTube TV’de sonuçlarla açılır.'),
      ('Uygulamalar', 'YouTube’u, Netflix’i, Disney+’ı ve diğer uygulamalarını tek dokunuşla aç.'),
      ('TV’yi açma', 'Ağ üzerinden açmayı destekleyen modellerde Mando TV TV’yi açar ve kendiliğinden bağlanır.'),
      ('iPhone, Android ve bilgisayar', 'Her telefonda ve her bilgisayarda aynı şekilde çalışır.'),
    ],
    pasos=[
      'Telefonunu ve TV’yi aynı Wi-Fi ağına bağla.',
      'Mando TV’yi aç: Android TV’n listede kendiliğinden görünür. Üzerine dokun.',
      'TV 6 karakterli bir kod gösterir. Kodu Mando TV’ye gir (yalnızca ilk seferde).',
    ],
    encender='Bu üreticiye göre değişir. Ağ veya güç ayarlarında “Wake on LAN”, “Ağ üzerinden aç”, “Ağ beklemesi” ya da “Remote start” seçeneğini ara. Bazı modellerde bu seçenek yoktur. Bundan sonra, kapalı TV’ye Mando TV’de dokunduğunda uygulama açmak isteyip istemediğini sorar ve kendiliğinden bağlanır.',
    faq=[
      ('Google TV’li Chromecast ile çalışır mı?', 'Evet, eşleştirme ekranda çıkan 6 karakterli kodla yapılır.'),
      ('Google TV uygulamasından farkı ne?', 'Mando TV Google hesabı istemez, Windows’ta da çalışır ve LG, Samsung ve Roku televizyonlarını aynı uygulamayla kontrol eder.'),
      ('Kod ekranda çıkmıyor. Ne yapmalıyım?', 'Mando TV’yi kapat, uygulamayı yeniden aç ve TV’ye tekrar dokun. TV’nin derin bir güç tasarrufu modunda olmadığını kontrol et.'),
    ],
    guias=[('androidtv-code', 'Android TV eşleştirme kodu istiyor: yapman gerekenler'),
           ('androidtv', 'Kumandasız Android TV: telefonunu böyle kullanırsın'),
           ('googletv-alt', 'Telefonda Google TV kumanda alternatifi'),
           ('sony', 'Sony kumanda uygulaması'),
           ('tcl', 'TCL kumanda uygulaması'),
           ('hisense', 'Hisense kumanda uygulaması'),
           ('philips', 'Philips kumanda uygulaması'),
           ('guias', 'TV’yi telefonla kontrol etmek için tüm rehberler')]),
]

GUIAS = [
  dict(clave='lost-tv', corto='Kumanda kayboldu',
    titulo='Kumanda kayboldu mu? TV’yi telefonla kontrol et',
    desc='Kumandayı mı kaybettin? TV’yi üzerindeki tuşla aç ve telefonunu kumanda olarak kullan. LG, Samsung, Roku, Android TV için adımlar. Ücretsiz.',
    h1='Kumanda kayboldu mu? Şimdi yapabileceklerin',
    intro='Kaybolan kumanda her evde olur: tam bir şey izlemek istediğinde ortadan kaybolur. İyi haber şu: telefonun, evindeki Wi-Fi üzerinden kumandanın yerini alabilir. İşte sırayla yapabileceklerin.',
    pasos=[
      'TV’yi üzerindeki tuşla aç. Tuş neredeyse hep alt ortada ya da arka tarafta, köşelerden birinin yakınındadır. Bazen tek bir tuş, bazen küçük bir joystick olur.',
      'Telefonunu TV’yle aynı Wi-Fi ağına bağla.',
      'Ücretsiz olan ve hesap istemeyen Mando TV’yi indir ve uygulamayı aç. TV’n listede kendiliğinden görünür. Üzerine dokun.',
      'Bağlantıyı markan için onayla. LG ve Samsung’da TV bir soru gösterir: TV’nin kendi tuşuyla veya joystick’iyle onayla. Android TV ve Google TV’de ekranda çıkan 6 karakterli kodu girersin. Roku hiçbir şey sormaz.',
      'Hepsi bu. Yön tuşları, OK, geri, ana ekran, ses, kanallar ve klavye ücretsiz.',
      'Bir dahaki sefer için: TV’nin ayarlarında ağ üzerinden açmayı etkinleştir (markan için rehberi aşağıda bulabilirsin). Böylece TV’ye dokunmadan telefondan açabilirsin.',
    ],
    extra=[
      ('Markan için rehberi seç', 'LG: [LG kumanda kayboldu](@lost-lg). Android TV ve Google TV: [Kumandasız Android TV](@androidtv). Samsung: [Kumandasız Samsung TV](@samsung-lost). Roku: [Roku kumanda kayboldu](@roku-lost).'),
      ('TV tuşla açılmıyorsa', 'Başka bir kumanda aramadan önce kablonun iyice takılı olduğunu ve prizde elektrik olduğunu kontrol et. TV’deki tuş hiçbir şey yapmıyorsa sorun kumandada değil, TV’dedir.'),
      ('Kumanda artık hiç çalışmıyorsa', 'Yeni pil dene. Hâlâ sinyal gönderip göndermediğini, telefonunun kamerasına doğrultup bir tuşa basarak kontrol edebilirsin: birçok telefonda ekranda mor bir ışık görürsün. Işığı görüyorsun ama TV tepki vermiyorsa TV’deki sensör örtülmüş olabilir.'),
      ('Router’ı değiştirdiysen ve TV’nin Wi-Fi’ı gittiyse', 'Kumanda olmadan TV’yi yeni ağa bağlamak daha zordur. En kolayı, TV’yi bir ağ kablosuyla router’a takmaktır. Eskisiyle aynı ad ve şifreye sahip bir Wi-Fi de kurabilirsin: TV genellikle ona kendiliğinden bağlanır.'),
      ('Neler ücretsiz, neler Pro', 'TV’yi açıp kapatma, yön tuşları, OK, ses, kanallar, rakam tuşları, klavye, uygulama açma ve girişi değiştirme ücretsizdir. Dokunmatik yüzey, ses komutu ve rutinler, tek seferlik satın alımla gelen ve abonelik gerektirmeyen Mando TV Pro’dadır.'),
    ],
    marca=None,
    faq=[
      ('TV’yi hiç bağlamadıysam telefonla açabilir miyim?', 'İlk seferde TV’deki tuşla açarsın. Telefonunu bağladıktan ve TV’nin ayarlarında ağ üzerinden açmayı etkinleştirdikten sonra uygulamadan açabilirsin.'),
      ('Yeni bir kumanda almam gerekir mi?', 'Şart değil. Mando TV ile tuşlar, ses, klavye ve açma ücretsiz. Yine de gerçek bir kumanda istersen TV’nin tam modelini ara.'),
      ('TV’nin Wi-Fi’ı yoksa çalışır mı?', 'Çoğunlukla hayır. Telefon ve TV genellikle aynı Wi-Fi ağında olmalı. İstisnalar, kızılötesi vericisi olan Android telefonlarda kızılötesi (akıllı TV özelliği olmayan televizyonları da kontrol eder) ve Android 9’dan itibaren betadaki Bluetooth (Google TV, Android TV ve Fire TV ile hiç Wi-Fi olmadan çalışır).'),
    ]),
  dict(clave='lost-lg', corto='LG kumanda kayboldu',
    titulo='LG kumanda kayboldu mu? Telefonunu kullan',
    desc='LG kumandan yok mu? TV’yi üzerindeki tuşla aç, soruyu onayla ve telefonunu Wi-Fi ile kullan. LG hesabı yok, reklam yok.',
    h1='LG kumanda kayboldu mu? Telefonunu böyle kullanırsın',
    intro='LG kumandanı kaybettiysen ya da Magic Remote artık çalışmıyorsa telefonun Wi-Fi üzerinden onun yerini alır. Bu, webOS’lu LG TV’lerde, yani 2014’ten bu yana neredeyse her LG akıllı TV’de çalışır. LG hesabına da ThinQ uygulamasına da ihtiyacın yok.',
    pasos=[
      'TV’yi LG logosunun altındaki tuşla ya da arkadaki tuşla aç. Birçok modelde bu bir joystick’tir: menüyü açmak için bas, bir şey seçmek için hareket ettir.',
      'Telefonunu TV’yle aynı Wi-Fi ağına bağla.',
      'Mando TV’yi aç ve listede LG TV’ne dokun.',
      'TV izin isteyen bir soru gösterir. Joystick’le ya da TV’deki tuşla onayla. Bu telefonu daha önce bağladıysan tekrar sormaz.',
      'Hepsi bu. Yön tuşları, OK, geri, ana ekran, ses, kanallar ve klavye ücretsiz. İmleç Pro özelliğidir.',
      'Uygulama bağlıyken yön tuşları ve OK ile ayarlara gir ve “Mobil cihazla TV’yi aç”ı etkinleştir. [LG TV’yi telefonla açma](@lg-on) rehberi seçeneği nerede bulacağını gösterir.',
    ],
    extra=[
      ('TV soruyu göstermiyorsa', 'İzin zaten kayıtlı olabilir ya da telefonun başka bir ağda olabilir. İkisinin de aynı Wi-Fi’da olduğunu ve VPN’in kapalı olduğunu kontrol et. TV listede görünmüyorsa [Telefonun TV’yi bulamıyor](@not-found) sana yardımcı olur.'),
      ('TV’nin Wi-Fi bağlantısı gittiyse', 'TV’yi bir ağ kablosuyla router’a tak, kendiliğinden kullanır. Ya da eskisiyle aynı ad ve şifreye sahip bir Wi-Fi kur, çünkü TV genellikle ona kendiliğinden bağlanır.'),
      ('TV başka bir girişte kaldıysa', 'Telefonunda Girişler’e dokun ve HDMI girişini seç. Daha fazlası için [Kumandasız TV’nin HDMI girişini değiştirme](@hdmi) rehberine bak.'),
    ],
    marca='lg',
    faq=[
      ('Mando TV’yi kullanmak için Magic Remote’a ihtiyacım var mı?', 'Yalnızca ilk seferde soruyu onaylamak için bir şeye ihtiyacın var ve bunun için TV’nin kendi tuşu ya da joystick’i yeter. Sonrasında yalnızca telefonunu kullanırsın.'),
      ('LG ThinQ uygulamasına ihtiyacım var mı?', 'Hayır. Mando TV doğrudan Wi-Fi ağın üzerinden bağlanır ve LG hesabı istemez.'),
      ('LG TV’mi telefonla açıp kapatabilir miyim?', 'Kapatmak evet. Açmak için TV’de “Mobil cihazla TV’yi aç”ı etkinleştirmiş ve TV açıkken bir kez bağlanmış olman gerekir.'),
    ]),
  dict(clave='hdmi', corto='Kumandasız HDMI değiştirme',
    titulo='Kumandasız HDMI girişini değiştirme (Samsung, LG, Roku)',
    desc='Samsung, LG veya Roku’da kumandasız HDMI girişini değiştir: TV’nin üzerindeki tuşla ya da telefonla. Başlamak ücretsiz, reklamsız.',
    h1='Kumandasız TV’nin HDMI girişini nasıl değiştirirsin',
    intro='Konsol ya da medya oynatıcı hazır, ama TV başka bir girişte takılı kaldı ve kumanda hiçbir yerde yok. HDMI girişini kumandasız değiştirmek için iki yolun var: TV’nin kendi üzerindeki tuş ya da telefonun. İşte Samsung, LG ve Roku için adımlar.',
    pasos=[
      'Önce en kolayını dene: konsolu ya da oynatıcıyı aç. TV’de HDMI-CEC etkinse (Samsung’da adı Anynet+, LG’de SIMPLINK) o girişe kendiliğinden geçer.',
      'Geçmezse TV’nin kendi üzerindeki tuşu kullan; alt ortada ya da arkadadır. Birçok Samsung ve LG TV’de bu bir joystick’tir ve Kaynak ya da Girişler içeren bir menü açar.',
      'Bu menüde girişi seç: HDMI 1, HDMI 2 ve böyle devam eder. Numara, kablonun takılı olduğu bağlantı noktasıdır.',
      'Telefonunu kullanmak istersen aynı Wi-Fi ağına bağla, Mando TV’yi aç ve TV’ne dokun.',
      'LG ve Roku’da Girişler’e dokun ve HDMI girişini seç. Samsung’da Girişler, Kaynak tuşunu TV’ye gönderir ve sen yön tuşları ve OK ile seçersin.',
      'TV’nin ana ekranından yön tuşları ve OK ile girişlere de gidebilirsin. Markaya ve üretim yılına göre Kaynak, Bağlı cihazlar ya da Girişler adını taşırlar. Roku TV’de bunlar ana ekrandaki HDMI karolarıdır.',
    ],
    extra=[
      ('Samsung', 'TV’deki tuşun menüsünde Kaynak seçeneği yoksa telefonunla ana ekran menüsünü aç ve solda Kaynak ya da Bağlı cihazlar’ı ara. Mando TV’deki ücretsiz yön tuşları ve OK ile kontrol edersin.'),
      ('LG', 'TV’deki joystick’e bas ve Girişler’i ara. Telefonunla Mando TV’de giriş listesini de açıp istediğin girişe dokunabilirsin.'),
      ('Roku TV', 'Ana ekranda her giriş için bir karo vardır, örneğin HDMI 1 veya HDMI 2. Yön tuşlarıyla git ve OK ile aç, ücretsiz.'),
      ('Android TV veya Google TV’li bir televizyonsa', 'Mando TV’de Android TV için giriş listesi henüz yok. TV’nin kendi giriş tuşunu kullan ya da girişlere ana ekrandan yön tuşları ve OK ile ulaş. Kumandan yoksa ve bağlanmak istiyorsan [Kumandasız Android TV](@androidtv) rehberini oku.'),
      ('Daha fazla yardım', 'TV hiç açılmıyorsa ya da nereden başlayacağını bilmiyorsan [Kumanda kayboldu](@lost-tv) rehberini oku. Konsolda oyun oynamak için [Kumandasız TV’yi açma ve konsolun HDMI girişine geçme](@console) rehberinde HDMI-CEC hilesi var.'),
    ],
    marca=None,
    faq=[
      ('HDMI girişini değiştirmek ücretsiz mi?', 'Evet. Mando TV’deki giriş listesi, TV’yi açma, yön tuşları, OK ve ses gibi ücretsizdir. Girişlere TV’nin kendi menüsünden de ulaşabilirsin.'),
      ('Hangi HDMI girişine ihtiyacım olduğunu nasıl anlarım?', 'TV’deki HDMI bağlantı noktalarına bak: her birinin bir numarası var. Konsolunun ya da oynatıcının kablosunun takılı olduğunu seç.'),
      ('TV açılmıyorsa ne yapmalıyım?', 'Üzerindeki tuşla aç. Daha önce bağladıysan ve ağ üzerinden açmayı etkinleştirdiysen telefonundan da açabilirsin.'),
    ]),
  dict(clave='androidtv', corto='Kumandasız Android TV',
    titulo='Kumandasız Android TV: telefonunu kullan',
    desc='Android TV veya Google TV kumandan yok mu? Telefonunu ekrandaki 6 karakterli kodla bağla. Ücretsiz, hesapsız, reklamsız.',
    h1='Kumandasız Android TV: telefonunu böyle kullanırsın',
    intro='Android TV ya da Google TV kumandanı kaybettiysen ya da pilleri bittiyse telefonun onun yerini alır. En güzeli: bağlanmak için kumandaya ihtiyacın yok, çünkü TV ekranda bir kod gösterir ve sen onu telefonuna yazarsın. Android TV’li Sony, Philips, TCL, Hisense, Sharp ve Xiaomi televizyonlarda, Google TV’li Chromecast’te ve Nvidia Shield’da çalışır.',
    pasos=[
      'TV’yi üzerindeki tuşla aç. Tuş neredeyse hep alt ortada ya da arka tarafta, köşelerden birinin yakınındadır.',
      'Telefonunu TV’yle aynı Wi-Fi ağına bağla.',
      'Ücretsiz olan ve Google hesabı istemeyen Mando TV’yi indir ve uygulamayı aç. Listede TV’ne dokun.',
      'TV, 6 harf ve rakamdan oluşan bir kod gösterir. Onu telefonuna yaz ve Eşleştir’e dokun. Bunun için kumandaya ihtiyacın yok.',
      'Şimdi yön tuşlarını, OK’i, geri, ana ekran, sesi, sessizi ve klavyeyi kullanabilirsin. Bunlar ücretsiz, uygulama listesi de öyle. Dokunmatik yüzey Pro’dur.',
      'Bir dahaki sefer TV’yi telefondan açmak için ağ ya da güç ayarlarında “Wake on LAN”, “Ağ üzerinden aç”, “Ağ beklemesi” ya da “Remote start” seçeneğini ara.',
    ],
    extra=[
      ('TV’n telefondan açılmıyorsa', 'Her Android TV ağ üzerinden açılamaz; bu üreticiye ve modele bağlıdır. Seninkinde bu özellik yoksa TV’yi üzerindeki tuşla aç ve telefondan devam et. Kapatmayı uygulamadan yapabilirsin.'),
      ('Google TV’li Chromecast, Google TV Streamer ve Shield', 'Aynı şekilde bağlanırlar: aynı Wi-Fi, listede cihaza dokun ve kodu gir. TV başka bir girişi gösteriyorsa [Kumandasız TV’nin HDMI girişini değiştirme](@hdmi) rehberinde anlatıldığı gibi cihazın takılı olduğu HDMI girişine geç.'),
      ('Kod çıkmıyorsa ya da yanlış deniyorsa', 'TV’nin gerçekten açık olduğunu ve beklemede olmadığını kontrol et. Kod her istekte değişir: yalnızca sonuncusu çalışır. Daha fazla ayrıntı için [Android TV eşleştirme kodu istiyor](@androidtv-code) rehberine bak.'),
      ('Google uygulaması mı, Mando TV mi', 'Google’ın kendi uygulaması var ve bir Google hesabı gerektiriyor. Mando TV hesap istemez, Windows’ta da çalışır ve LG, Samsung ve Roku televizyonlarını aynı uygulamayla kontrol eder.'),
    ],
    marca='android',
    faq=[
      ('Telefonumu eşleştirmek için kumandaya ihtiyacım var mı?', 'Hayır. Kod TV’nin ekranında çıkar ve sen onu telefonuna yazarsın. Yalnızca TV’yi açman gerekir; gerekirse üzerindeki tuşla.'),
      ('Hisense ile çalışır mı?', 'Android TV veya Google TV’li Hisense televizyonlarda evet. Farklı sistemli Hisense televizyonlar uyumlu değildir.'),
      ('Telefonumun klavyesiyle yazabilir miyim?', 'Evet, iki tane var. Ücretsiz klavye TV’nin ve çoğu uygulamanın arama ve metin kutularına yazar. YouTube ve Netflix yalnızca kendi ekran klavyesini kabul eder, bu yüzden YouTube için YouTube Klavyesi (Pro) var: ne izlemek istediğini yazarsın ya da söylersin, YouTube TV’de sonuçlarla açılır. Netflix oklar ve OK ile kullanılır.'),
    ]),
  dict(clave='lg-on', corto='LG TV’yi telefonla açma',
    titulo='LG TV’yi telefonla açma (rehber)',
    desc='LG TV’yi Wi-Fi ile telefondan aç: “Mobil cihazla TV’yi aç”ı etkinleştir ve Mando TV’yi kullan. Adım adım, ücretsiz.',
    h1='LG TV’yi telefonla nasıl açarsın',
    intro='LG TV’yi telefonla açabilirsin, ama bunun için önce TV’de bir ayarı etkinleştirmen gerekir. Bundan sonra telefonun, LG TV’yi Wi-Fi ağın üzerinden kumandasız açar. Beş dakika sürer ve bunu yalnızca bir kez yaparsın.',
    pasos=[
      'Telefonunu ve LG TV’yi aynı Wi-Fi ağına bağla.',
      'TV’de ayarları aç ve “Mobil cihazla TV’yi aç”ı ara. Ayarlar, Genel, Cihazlar, Harici Cihazlar altında bulursun (eski modellerde Bağlantı, Mobil Bağlantı Yönetimi).',
      '“Wi-Fi üzerinden aç”ı etkinleştir. TV’n ağ kablosuyla bağlıysa onun yerine kablo seçeneğini etkinleştir.',
      'TV’nde “Hızlı Başlatma+” varsa onu da etkinleştir.',
      'TV açıkken telefonunda Mando TV’yi aç ve listede LG TV’ne dokun. Ekranda çıkan soruyu onayla. Uygulama onu uyandırmayı böyle öğrenir.',
      'TV’yi kapat ve dene: Mando TV’de TV’ye dokun, uygulama onu açmak isteyip istemediğini sorar.',
    ],
    extra=[
      ('Açılmıyorsa', 'TV kapatıldığında aynı Wi-Fi ağında olmuş olmalı. Ayarın hâlâ etkin olduğunu ve telefonunun aynı ağda olduğunu kontrol et. Router’ı değiştirdiysen TV açıkken yeniden bağlan.'),
    ],
    marca='lg',
    faq=[
      ('LG TV’yi hiç bağlamadıysam telefonla açabilir miyim?', 'Hayır. Önce TV’de “Mobil cihazla TV’yi aç”ı etkinleştirmeli ve TV açıkken bir kez Mando TV ile bağlanmalısın.'),
      ('LG ThinQ uygulamasına ihtiyacım var mı?', 'Hayır. Mando TV doğrudan Wi-Fi ağın üzerinden bağlanır ve LG hesabı istemez.'),
      ('Mobil veriyle çalışır mı?', 'Hayır. Telefon ve TV aynı Wi-Fi ağında olmalı.'),
    ]),
  dict(clave='console', corto='Kumandasız TV ve konsol',
    titulo='Kumandan yok mu? TV’yi aç, HDMI girişini değiştir',
    desc='Çıkış günü ve kumandan yok mu? TV’yi aç ve telefonunla PS5 ya da Xbox’ının HDMI girişine geç. Ücretsiz, reklamsız.',
    h1='Kumandasız TV’yi nasıl açarsın ve konsolunun HDMI girişine nasıl geçersin',
    intro='GTA VI’nın çıkış günü, konsol hazır ve kumanda kanepenin minderleri arasında bir yerde kayboldu. Sandığından sık olur. Mando TV ile telefonun TV’yi açar ve evindeki Wi-Fi üzerinden PlayStation ya da Xbox’ının girişine geçer.',
    pasos=[
      'Telefonunu TV’yle aynı Wi-Fi ağına bağla.',
      'Mando TV’yi aç ve listede TV’ne dokun (Samsung, LG, Roku veya Android TV).',
      'TV kapalıysa Aç’a dokun. TV’de ağ üzerinden açma etkinse çalışır. Hiç etkinleştirmediysen bu seferlik TV’yi üzerindeki tuşla aç ve bir dahaki sefer için etkinleştir.',
      'Konsolu aç. HDMI-CEC etkinse (aşağıdaki ücretsiz hileye bak) TV kendiliğinden onun girişine geçer.',
      'Geçmezse Mando TV’de Girişler’e dokun ve konsolun takılı olduğu HDMI girişini seç: HDMI 1, HDMI 2 ve böyle devam eder.',
      'Oyun oynarken ses için uygulamadaki büyük tuşları kullan.',
    ],
    extra=[
      ('Ücretsiz hile: girişi konsolun değiştirmesini sağla', 'PS5 ve Xbox, HDMI-CEC sayesinde TV’yi açabilir ve başlar başlamaz kendi HDMI girişine geçebilir. PS5’te Ayarlar > Sistem > HDMI > HDMI Cihaz Bağlantısını Etkinleştir altında bulursun. Xbox’ta Ayarlar > Genel > TV ve görüntü seçenekleri’ni aç ve cihaz kontrolü seçeneğini ara. TV’de bu özelliğin adı markaya göre değişir: Samsung’da Anynet+, LG’de SIMPLINK, Sony’de BRAVIA Sync ya da diğerlerinde HDMI kontrolü.'),
      ('TV başka bir görüntüde kalırsa', 'Konsol açık ama TV hâlâ anten ya da bir uygulamayı gösteriyorsa girişi değiştirmemiştir. Telefonunda Girişler’e dokun ve konsolun HDMI girişini seç. Ya da yön tuşları ve OK ile TV’nin girişlerine git ya da TV’nin kendi tuşunu kullan ve HDMI girişini seç. Numara, konsolun kablosunu taktığın bağlantı noktasıdır.'),
      ('Roku TV’ysa', 'TV’nin üzerindeki, çoğunlukla alt ortadaki ya da arkadaki tuş onu açar. Oradan sonrasını telefonun halleder.'),
    ],
    marca=None,
    faq=[
      ('Mando TV’nin GTA VI ile bir ilgisi var mı?', 'Hayır. Mando TV’nin Rockstar Games veya Take-Two ile bir bağlantısı yoktur. Uygulama yalnızca kumandayı bulamadığın için oyun zamanı kaybetmemene yardımcı olur.'),
      ('HDMI girişini değiştirmek ücretsiz mi?', 'Evet. Mando TV’deki giriş listesi, TV’yi açma, yön tuşları, OK ve ses gibi ücretsizdir. Konsolun HDMI-CEC ile girişi kendiliğinden değiştirmesini de sağlayabilirsin.'),
      ('TV’mle çalışır mı?', 'Aynı Wi-Fi ağındaki Samsung, LG, Roku ve Android TV televizyonlarla çalışır. Seninki başka bir markaysa HDMI-CEC hilesi yine de işe yarayabilir.'),
      ('PS5’te ya da Xbox’ta GTA VI (GTA 6) oynamak için kullanabilir miyim?', 'Mando TV konsola da oyuna da karışmaz. Yalnızca TV’nin açık ve doğru HDMI girişinde olmasını sağlar; böylece oturup oynayabilirsin.'),
    ]),
  dict(clave='samsung-lost', corto='Kumandasız Samsung TV',
    titulo='Samsung kumanda kayboldu mu? Telefonunu kullan',
    desc='Samsung kumandan kayıp ya da bozuk mu? Telefonunu Tizen’li TV’ler için Wi-Fi ile kumanda olarak kullan. Mando TV ile kolay, ücretsiz, reklamsız.',
    h1='Orijinal kumandasız Samsung TV: telefonunu böyle kullanırsın',
    intro='Samsung kumandanı kaybettiysen ya da artık çalışmıyorsa telefonunu Wi-Fi üzerinden kumanda olarak kullanabilirsin. Tizen’li, 2016 ve sonrası üretim Samsung TV’lerde çalışır.',
    pasos=[
      'TV’yi üzerindeki tuşla aç. Çoğu modelde altta ya da arkadadır, bazen küçük bir joystick biçimindedir.',
      'TV’nin Wi-Fi’ına bağlı olduğunu ve telefonunun aynı ağda olduğunu kontrol et.',
      'Telefonunda Mando TV’yi aç. Samsung TV’n listede kendiliğinden görünür. Üzerine dokun.',
      'TV senden bağlantıyı onaylamanı ister. Çoğu modelde bunu TV’deki tuşlarla ya da arkadaki joystick’le onaylarsın.',
      'Hepsi bu, artık telefonunu kumanda olarak kullanabilirsin. Tuşlar, klavye ve uygulamalar ücretsiz; dokunmatik yüzey Pro özelliğidir.',
      'Bir dahaki sefer TV’yi telefondan açmak için Ayarlar > Genel > Ağ > Uzman Ayarları’na git ve “Mobil Cihazla Aç”ı etkinleştir.',
    ],
    extra=[
      ('TV izin sormuyorsa', 'İzin zaten kayıtlı olabilir ya da TV başka bir Wi-Fi’da olabilir. Mando TV’yi kapat ve TV açıkken uygulamayı yeniden aç. TV 2016’dan eskiyse henüz desteklenmeyen farklı bir sistem kullanıyordur.'),
      ('İzni yanlışlıkla reddettiysen', 'TV’de Ayarlar > Genel > Harici Aygıt Yöneticisi > Aygıt Bağlantı Yöneticisi’ne git ve Mando TV’yi izinli yap. Telefonun yine de TV’yi bulamıyorsa [Telefonun TV’yi bulamıyor](@not-found) rehberini oku.'),
    ],
    marca='samsung',
    faq=[
      ('Kumandam yoksa bağlantıyı nasıl onaylarım?', 'Çoğu modelde TV’deki tuşlarla ya da arkadaki joystick’le onaylarsın. Modelinde tuş yoksa hola@mandotv.app adresine yaz, yardımcı oluruz.'),
      ('Mando TV Samsung hesabı ister mi?', 'Hayır. Bağlantı doğrudan Wi-Fi ağın üzerinden kurulur, Samsung hesabı gerekmez.'),
      ('Eski Samsung TV’mle çalışır mı?', 'Tizen’li, 2016 ve sonrası Samsung TV’lerle çalışır.'),
    ]),
  dict(clave='wifi', corto='Telefonu Wi-Fi ile kumanda yapma',
    titulo='Telefonu kumanda olarak kullan: TV’yi Wi-Fi ile kontrol et',
    desc='Telefonunu Wi-Fi ile TV’ne bağla ve Samsung, LG, Roku ve Google TV’de kumanda olarak kullan. Mando TV ile markaya göre adımlar. Ücretsiz.',
    h1='Telefonunu Wi-Fi ile TV’ne kumanda olarak nasıl bağlarsın',
    intro='Tek ihtiyacın, aynı Wi-Fi ağındaki telefonun ve TV’n ile bir kumanda uygulaması. Mando TV TV’ni kendiliğinden bulur ve Samsung, LG, Roku, Google TV ve Android TV ile çalışır.',
    pasos=[
      'Telefonunu ve TV’yi aynı Wi-Fi ağına bağla.',
      'Mando TV’yi aç. TV’n listede kendiliğinden görünür. Üzerine dokun.',
      'Bağlantıyı markan için onayla (ayrıntılar aşağıda).',
      'TV’yi tuşlarla ya da telefonunun klavyesiyle kontrol et. Dokunmatik yüzey Pro özelliğidir.',
    ],
    extra=[
      ('Samsung', 'TV, bağlantıya izin verip vermediğini sorar. İlk seferde ekranda onayla. Tizen’li, 2016 ve sonrası modellerle çalışır. TV’yi telefondan açmak için Ayarlar > Genel > Ağ > Uzman Ayarları altında “Mobil Cihazla Aç”ı etkinleştir.'),
      ('LG', 'TV izin isteyen bir soru gösterir. İlk seferde onayla. TV’yi telefondan açmak için ayarlarda “Mobil cihazla TV’yi aç”ı ara ve “Wi-Fi üzerinden aç”ı etkinleştir.'),
      ('Roku', 'Roku eşleştirme istemez: listede ona dokun ve bağlanmış olursun. Açmak için Ayarlar > Sistem > Güç altında “TV hızlı başlatma”yı etkinleştir.'),
      ('Google TV ve Android TV', 'TV ekranda bir kod gösterir. İlk seferde Mando TV’ye gir. Açmak için ayarlarda “Wake on LAN”, “Ağ üzerinden aç” ya da “Ağ beklemesi” seçeneğini ara.'),
    ],
    marca=None,
    faq=[
      ('Telefonumu kumanda olarak kullanmak için internete ihtiyacım var mı?', 'Telefonun ve TV’nin aynı Wi-Fi ağında olması gerekir. Mando TV bu ağ üzerinden doğrudan TV’ne bağlanır.'),
      ('TV’m neden listede görünmüyor?', 'TV’nin açık olduğunu ve telefonunun mobil veri ya da başka bir Wi-Fi kullanmadığını kontrol et. Bazı router’larda cihazları birbirinden ayıran bir misafir ağı bulunur.'),
      ('Mando TV’yi iPhone’da ya da Android telefonda kullanabilir miyim?', 'iPhone ve iPad’de evet: uygulama App Store’da. Windows için Microsoft Store’da da var. Android yakında geliyor: Google Play’deki ücretsiz erken erişime katılabilirsin.'),
    ]),
  dict(clave='pc', corto='TV’yi bilgisayarla kontrol etme',
    titulo='TV’yi Windows bilgisayarla kontrol et (ücretsiz)',
    desc='Windows bilgisayarını Samsung, LG, Roku ya da Google TV için Wi-Fi ile kumanda yap. Tuşlar, klavye, uygulamalar ücretsiz; kısayollar Pro’da.',
    h1='TV’yi Windows bilgisayarla nasıl kontrol edersin',
    intro='Günü bilgisayarın başında geçiriyorsan kumanda aramana gerek yok: Windows için Mando TV, Samsung, LG, Roku, Google TV ya da Android TV televizyonunu evindeki Wi-Fi üzerinden kontrol eder. Uygulamaları değiştirmek, sesi açmak ya da bilgisayarın klavyesiyle YouTube’da yazmak için çok pratik.',
    pasos=[
      'Mando TV’yi Windows 10 veya 11’li bilgisayarına Microsoft Store’dan ücretsiz indir.',
      'Bilgisayarın ve TV’nin aynı ağda olduğunu kontrol et (Wi-Fi veya kablo, ama aynı router üzerinden).',
      'Mando TV’yi aç: TV’n listede kendiliğinden görünür. Üzerine dokun ya da tıkla.',
      'İlk seferde bağlantıyı TV’nin ekranında onayla (Google TV ve Android TV’de TV’nin gösterdiği kodu girersin).',
      'Hepsi bu: TV’nin arama kutusuna yazmak için tuşları ya da klavyeyi kullan. Dokunmatik yüzey Pro özelliğidir.',
    ],
    extra=[
      ('Bilgisayarda klavye kısayolları (Pro)', 'Mando TV Pro ile TV’yi bilgisayarın klavyesiyle kontrol edersin: gezinmek için yön tuşları, OK için Enter, geri için Backspace ya da Esc, ses için + ve -, sessiz için M ve duraklatmak için Boşluk.'),
      ('Her zaman önde duran mini kumanda (Pro)', 'Çalışırken ya da bilgisayarda oyun oynarken kumandanın küçük bir penceresini sürekli görünür tut.'),
      ('Bilgisayardan TV’yle konuşma (Pro)', 'Mando TV Pro ile TV’ye bilgisayarın mikrofonundan komut verirsin: “YouTube’u aç”, “sesi aç” ya da “30 dakika sonra kapat”, tam konuştuğun gibi. Windows’ta konuşma bilgisayarın kendisinde tanınır: internete ihtiyacın yok, Windows ayarlarında bir şey değiştirmen gerekmez ve uygulamanın 6 dilinde çalışır. Söylediğin bilgisayardan çıkmaz ve kaydedilmez. Yalnızca çok eski işlemcilerde uygulama Windows’un dikte özelliğine geçer. Bunun için gizlilik ayarlarında çevrimiçi konuşma tanıma açık olmalı ve Windows’a Türkçe (Türkiye) eklenmiş olmalı. Bir şey eksikse uygulama seni uyarır ve ayarı bir düğmeyle açar.'),
    ],
    marca=None,
    faq=[
      ('TV’yi bilgisayarla kontrol etmek için kabloya ya da Bluetooth’a ihtiyacım var mı?', 'Hayır. Mando TV ev ağın üzerinden bağlanır: bilgisayarın ve TV’nin aynı router’a bağlı olması yeterli.'),
      ('Her TV ile çalışır mı?', 'Tizen’li Samsung TV’lerle (2016 ve sonrası), webOS’lu LG’lerle, Roku’yla ve Google TV ya da Android TV ile (Sony, Philips, TCL, Hisense, Sharp, Xiaomi, Toshiba, Panasonic, Haier, Skyworth ve diğerleri) çalışır.'),
      ('Ne kadar tutar?', 'Tuşlar, klavye ve ağ üzerinden açma ücretsiz ve reklamsız. Mando TV Pro, dokunmatik yüzey, bilgisayar klavye kısayolları ve mini kumanda gibi ekstralar için tek seferlik, abonelik gerektirmeyen bir satın alımdır.'),
      ('Windows’ta mikrofon beni neden anlamıyor?', 'Ses özelliğinin etkin olduğunu (Pro’ya dahildir) ve bilgisayarın mikrofonunun Windows’ta çalıştığını kontrol et. Neredeyse tüm bilgisayarlarda konuşma, internet olmadan cihazın kendisinde tanınır. Yalnızca çok eski işlemcilerde uygulama Windows’un dikte özelliğini kullanır. O zaman Windows’un gizlilik ayarlarında çevrimiçi konuşma tanımanın açık olduğunu ve Windows’un dil ayarlarında Türkçe (Türkiye)’nin bulunduğunu kontrol et. Mando TV bu dili yalnızca dinlediği sürece kullanır.'),
    ]),
  dict(clave='roku-403', corto='Roku uygulaması çalışmıyor',
    titulo='Roku uygulaması çalışmıyor mu? 403 hatasını çöz',
    desc='Telefon bağlı ama Roku tepki vermiyor mu? “Mobil uygulamalarla kontrol”ü 5 adımda etkinleştir ve telefonunu yeniden kumanda yap.',
    h1='Roku uygulaması çalışmıyor: sorunu böyle çözersin',
    intro='Telefonun Roku’yu bulup bağlanıyor ama hiçbir tuş bir şey yapmıyorsa neredeyse her zaman Roku’nun kendisinde kumanda uygulamalarını engelleyen bir ayar vardır. Yeni Roku sürümleri varsayılan olarak daha kısıtlıdır. Roku menüsünden bu bir dakikada çözülür.',
    pasos=[
      'Roku’da Ana ekran’a bas ve Ayarlar’a git.',
      'Sistem’i, ardından Gelişmiş sistem ayarları’nı aç.',
      '“Mobil uygulamalarla kontrol”e git. Bazı modellerde adı “Harici kontrol”dür.',
      '“Ağ erişimi” altında Varsayılan ya da Permissive’i seç. Modelinde yalnızca bir anahtar varsa Etkin’de bırak.',
      'Telefonundaki Mando TV’ye dön ve Roku’na dokun. Tuşlar artık tepki verir.',
    ],
    extra=[
      ('Sorunun bu olup olmadığını nasıl anlarsın', 'İşaret açık: telefonun Roku’yu listede görüyor ve bağlanıyor, ama bir tuşa dokunduğunda hiçbir şey olmuyor. Roku arka planda “yasak” anlamına gelen 403 hatasıyla yanıt verir. Mando TV bunu bağlanırken fark eder ve sana bu adımları ekranda gösterir.'),
      ('Varsayılan mı, Permissive mi, hangisini seçeyim?', 'Varsayılan yeterli: ev ağından gelen komutları kabul eder, bir kumandanın ihtiyacı da budur. Permissive daha açıktır ve yalnızca alışılmadık ağlarda gerekir. Seçenek Devre dışı (yeni yazılımlarda Kısıtlı) olarak duruyorsa Roku uygulamalara yanıt vermez.'),
      ('Roku kumandan yoksa', 'Ayar Devre dışı olarak duruyorsa yalnızca gerçek Roku kumandasıyla değiştirilebilir. Bir kez değiştirmek için birinden ödünç al; sonrasında her şeyi telefonunla yapabilirsin. [Roku kumanda kayboldu](@roku-lost) rehberini de oku.'),
    ],
    marca='roku',
    faq=[
      ('Roku’m eskiden çalışırken neden artık tepki vermiyor?', 'Bir Roku güncellemesi bu ayarı daha kısıtlı hale getirmiş olabilir. Sorun telefonunda ya da Wi-Fi’ında değil: uygulamalarla kontrole yeniden izin vermen yeterli.'),
      ('Bu, Roku TV için de Roku oynatıcılar için de geçerli mi?', 'Evet. Ayar, Roku oynatıcılarda ve Roku TV cihazlarında aynı menüde bulunur.'),
      ('Ayarı Varsayılan olarak bırakmak güvenli mi?', 'Evet. Yalnızca ev ağındaki cihazlardan gelen komutları kabul eder.'),
    ]),
  dict(clave='not-found', corto='Telefon TV’yi bulamıyor',
    titulo='Telefon TV’yi bulamıyor mu? Kontrol edilecek 6 şey',
    desc='Kumanda uygulaması TV’ni bulamıyor mu? Wi-Fi’ı, VPN’i ve yerel ağ erişimini kontrol et. Samsung, LG, Roku ve Android TV için.',
    h1='Telefonun TV’yi bulamıyor: şunlara bak',
    intro='Kumanda uygulamasını açıyorsun ve liste boş, ya da TV görünüyor ama bağlantı kopuyor. Neredeyse her zaman sorun TV’de değil, ağdadır. Şu noktaları sırayla kontrol et: ilki vakaların çoğunu çözer.',
    pasos=[
      'Telefonunun hangi Wi-Fi’da, TV’nin hangisinde olduğuna bak. Aynı adlı aynı ağ olmalı. Misafir ağı çalışmaz, çünkü cihazları birbirinden ayırır.',
      'Kullanıyorsan telefonundaki VPN’i kapat. VPN açıkken telefonun internete başka bir ağ üzerinden çıkar ve evindeki cihazları göremez, ya da bağlantı birkaç saniye sonra kopar.',
      'Mobil veriyi kısa bir süre kapat. Bazı telefonlar sinyal zayıfken kendiliğinden Wi-Fi’dan mobil veriye geçer.',
      'TV’yi aç ve tamamen açılmasını bekle. Kapalı bir TV aramaya yanıt vermez.',
      'iPhone’da uygulamanın “Yerel Ağ” iznine sahip olduğunu kontrol et: Ayarlar > Gizlilik ve Güvenlik > Yerel Ağ.',
      'Hâlâ görünmüyorsa elle ekle: Mando TV’de “IP ile ekle”ye dokun ve TV’nin IP adresini gir.',
    ],
    extra=[
      ('Uygulamanın seni yönlendirmesine izin ver', 'TV listesinde, TV’n görünmediğinde kullanabileceğin bir düğme var. Uygulama en sık nedenleri adım adım kontrol eder (aynı Wi-Fi, VPN, yerel ağ izni ve daha fazlası) ve her düzeltmeden sonra yeniden kontrol etmen için bir düğme gösterir. Sihirbaz ücretsiz.'),
      ('TV’nin IP adresini nerede bulursun', 'TV’nin ağ menüsündedir ve modele göre biraz değişir. LG’de: Ayarlar, Ağ, Wi-Fi Bağlantısı, Gelişmiş Wi-Fi Ayarları. Samsung’da: Ayarlar, Genel, Ağ, Ağ Durumu, IP Ayarları. Roku’da: Ayarlar, Ağ, Hakkında. Android TV ve Google TV’de: Ayarlar, Ağ ve İnternet, ardından ağına dokun. 192.168.1.86 gibi bir sayıdır.'),
      ('Görünüyor ama bağlantı kopuyorsa', 'Bağlantı birkaç saniye sonra kopuyorsa neden genellikle telefondadır: bir VPN, başka bir Wi-Fi’a geçiş ya da güç tasarrufu modu. VPN’i kapat, aynı Wi-Fi’da kal ve tekrar dene.'),
      ('2,4 ve 5 GHz’lik Wi-Fi', 'İkisi de aynı router’dan geldiği sürece telefonun 5 GHz’lik ağda, TV’nin 2,4 GHz’lik ağda olması fark etmez. Wi-Fi tekrarlayıcın varsa ve TV yine de görünmüyorsa telefonla ana router’a yaklaş ve tekrar dene.'),
    ],
    marca=None,
    faq=[
      ('TV’yi mobil veriyle kontrol edebilir miyim?', 'Hayır. Kumanda sinyali evindeki Wi-Fi üzerinden gider, bu yüzden telefon ve TV aynı ağda olmalı.'),
      ('VPN açıkken neden çalışmıyor?', 'Çünkü VPN, telefonunun tüm trafiğini başka bir ağ üzerinden geçirir ve telefon evindeki cihazları göremez. Kumandayı kullandığın sürece kapat.'),
      ('Bluetooth ya da kızılötesiyle çalışır mı?', 'Akıllı TV’lerde Mando TV Wi-Fi kullanır. Kızılötesi yalnızca kızılötesi vericisi olan Android telefonlarda çalışır ve akıllı olmayan televizyonlar için düşünülmüştür. Bluetooth betadadır, ücretsizdir ve yalnızca Android 9’dan itibaren: telefon, TV’ye Bluetooth klavye ve kumanda olarak bağlanır, Wi-Fi’a hiç ihtiyaç duymadan. Google TV, Android TV ve Fire TV ile çalışır; Bluetooth klavye kabul eden diğer markalarda çalışabilir, Roku kabul etmez.'),
    ]),
  dict(clave='androidtv-code', corto='Android TV eşleştirme kodu',
    titulo='Android TV eşleştirme kodu istiyor: yapman gerekenler',
    desc='Android TV veya Google TV bağlanırken 6 karakterli bir kod gösterir. Kodu nasıl girersin ve çıkmazsa ya da yanlış çıkarsa ne yaparsın.',
    h1='Android TV eşleştirme kodu istiyor: yapman gerekenler',
    intro='Telefonunu bir Android TV ya da Google TV’ye ilk kez bağladığında TV ekranda 6 karakterli bir kod gösterir. Bu normaldir ve yalnızca bir kez olur: böylece başka hiç kimse TV’ni kontrol edemez. İşte kodu nasıl gireceğin ve çıkmazsa ne yapacağın.',
    pasos=[
      'TV’yi aç ve ana ekranı görünür bırak.',
      'Telefonunda, TV’yle aynı Wi-Fi’da Mando TV’yi aç ve listede TV’ne dokun.',
      'TV’nin ekranına bak: 6 harf ve rakamdan oluşan bir kod çıkar.',
      'Gösterildiği gibi aynen telefonuna yaz ve Eşleştir’e dokun. Harfler yalnızca A’dan F’ye kadar gider, yani yuvarlak bir karakter her zaman sıfır rakamıdır.',
      'Hepsi bu. TV telefonunu hatırlar ve kodu bir daha sormaz.',
    ],
    extra=[
      ('Kod TV’de çıkmıyorsa', 'TV’nin gerçekten açık olduğunu, beklemede olmadığını ve telefonunun aynı Wi-Fi’da olduğunu kontrol et. Telefonunda TV’ye tekrar dokun. Hâlâ çıkmıyorsa TV’yi yeniden başlat: fişi on saniye boyunca çek, tekrar tak ve yeniden dene.'),
      ('Kod yanlış deniyorsa', 'Kod her istekte değişir. Geç girdiysen ya da iki kez istediysen yalnızca ekrandaki son kod çalışır. Telefonunda TV’ye tekrar dokun ve yeni kodu gir.'),
      ('TV yine kodu soruyorsa', 'Bu, TV fabrika ayarlarına döndürüldüğünde ya da telefonundaki uygulama verilerini sildiğinde olur. Yeniden eşleştir, kayıtlı kalır. Hiç kumandan yoksa [Kumandasız Android TV](@androidtv) rehberini oku.'),
    ],
    marca='android',
    faq=[
      ('Hangi televizyonlar bu kodu kullanır?', 'Android TV veya Google TV’li olanlar: Sony, Philips, TCL, Hisense, Sharp, Xiaomi, Google TV’li Chromecast ve birkaç tane daha.'),
      ('Telefonumda Google hesabına ihtiyacım var mı?', 'Hayır. Tek ihtiyacın ekrandaki kod.'),
      ('Bu güvenli mi?', 'Evet. Kod, TV’nin karşısında olduğunu kanıtlar: Ekrandaki kodu görmeden hiç kimse eşleşemez.'),
    ]),
  dict(clave='roku-lost', corto='Roku kumanda kayboldu',
    titulo='Roku kumanda kayboldu mu? Telefonunu Wi-Fi ile kullan',
    desc='Roku kumandayı mı kaybettin? Telefonun Wi-Fi ile onun yerini alır. Router’ı değiştirdiysen ve Roku’nun Wi-Fi’ı yoksa bile basit adımlar.',
    h1='Roku kumanda kayboldu: telefonunu böyle kullanırsın',
    intro='Roku kumandanı kaybettiysen ya da artık çalışmıyorsa Roku hâlâ Wi-Fi ağına bağlı olduğu sürece telefonun onun yerini alır. Wi-Fi’ı ya da router’ı değiştirdiysen buna da bir çıkış yolu var.',
    pasos=[
      'Önce kumandayı çaldırmayı dene. Roku kumandanın hoparlörü varsa, örneğin Roku Voice Remote Pro, Mando TV’yi aç, Roku’ya bağlan ve bulman için kumandayı çaldırma seçeneğini kullan. Bu yalnızca hoparlörlü Roku kumandalarla çalışır ve Roku’nun açık olması gerekir.',
      'TV’yi aç ve Roku’yu takılı bırak. Ona dokunman gerekmez.',
      'Telefonunu Roku’nun kullandığı Wi-Fi’a bağla.',
      'Mando TV’yi aç. Roku listede kendiliğinden görünür. Üzerine dokun.',
      'Yön tuşlarını, OK’i, ana ekranı ve geri tuşunu alışık olduğun kumanda gibi kullan. Roku kod istemez.',
      'Tuşlar hiçbir şey yapmıyorsa Roku uygulamalarla kontrolü engelliyordur: [Roku uygulaması çalışmıyor](@roku-403) rehberi nasıl izin vereceğini anlatır.',
    ],
    extra=[
      ('Roku’nun Wi-Fi’ı yoksa (router değişti ya da taşındın)', 'Kumanda olmadan yeni ağı kurmak için menüye giremezsin, ama bir hile var: Roku, eski ağla aynı ada ve şifreye sahip bir ağa kendiliğinden bağlanır. Başka bir telefonda tam bu ad ve şifreyle bir Wi-Fi hotspot kur, Mando TV’li telefonu ona bağla ve Roku listede görünür. Oradan Ayarlar, Ağ’a git ve onu yeni Wi-Fi’a bağla.'),
      ('Roku TV’ysa', 'Roku TV cihazlarında TV’nin üzerinde, neredeyse hep alt ortada ya da arkada, TV’yi açan bir tuş vardır. Açıp telefonla devam etmek için bu yeter.'),
      ('Başka bir kumanda almak istersen', 'Modeline uyduğundan emin ol. TV’nin arkasındaki küçük Roku oynatıcılar kızılötesiz bir kumanda ister, çünkü kızılötesi onlara ulaşmaz.'),
    ],
    marca='roku',
    faq=[
      ('Telefonum Roku’yu açabilir mi?', 'Takılı bir Roku oynatıcı her zaman açıktır. Roku TV’de Ayarlar > Sistem > Güç altında “TV hızlı başlatma” etkinse Mando TV onu Wi-Fi ile açar.'),
      ('Peki ses?', 'Roku TV’de telefonun sesi açıp kısar. HDMI ile bağlı bir Roku oynatıcıda bu TV’ye bağlıdır: birçoğunda çalışır, bazılarında çalışmaz.'),
      ('Hesap oluşturmam gerekir mi?', 'Hayır. Mando TV hesap istemez ve Samsung, LG ve Android TV televizyonlarını da aynı uygulamayla kontrol eder.'),
    ]),
]

SOPORTE = dict(
  titulo='Yardım: TV’yi Mando TV ile bağla ve aç',
  desc='Mando TV kumandasını LG, Samsung, Roku veya Android TV ile nasıl bağlarsın, TV’yi telefondan nasıl açarsın ve sorunları nasıl çözersin.',
  h1='Yardım',
  intro='En sık sorulan sorular, adımların sırasıyla. Seninkini bulamazsan bize <a href="mailto:hola@mandotv.app?subject=Mando%20TV%20yard%C4%B1m">hola@mandotv.app</a> adresinden yaz, yanıtlarız.',
)
SOPORTE_HTML = '''      <h2 id="encontrar">TV’yi bulma</h2>
      <div class="preguntas">
        <details open><summary>TV’m listede görünmüyor</summary>
          <ol>
            <li>Telefonunun ve TV’nin aynı Wi-Fi ağında olduğunu kontrol et. Router’ında farklı adlı bir 2,4 GHz ve bir 5 GHz ağ varsa bazen birbirlerini göremezler.</li>
            <li>TV’nin açık olduğundan emin ol.</li>
            <li>iPhone’da Mando TV’nin “Yerel Ağ” iznine sahip olduğunu kontrol et: Ayarlar, Mando TV.</li>
            <li>TV listesinde, TV’n görünmediğinde kullanabileceğin düğmeye dokun: uygulama en sık nedenleri adım adım kontrol eder (aynı Wi-Fi, VPN, yerel ağ izni ve daha fazlası) ve her düzeltmeden sonra yeniden kontrol etmen için bir düğme gösterir.</li>
            <li>Hâlâ görünmüyorsa + tuşuna dokun, markayı seç ve TV’nin IP adresini gir. Onu TV’nin ağ menüsünde görürsün (örneğin 192.168.1.50).</li>
          </ol>
        </details>
        <details><summary>Mobil veriyle ya da evden uzakta çalışır mı?</summary>
          <p>Hayır. Mando TV, TV’yle ev ağının içinde konuşur; bu yüzden telefonunun bu Wi-Fi’a bağlı olması gerekir.</p>
        </details>
      </div>

      <h2 id="conectar">İlk kez bağlanma</h2>
      <p>Markaya göre tam rehberler: <a href="@@R_lg@@">LG</a>, <a href="@@R_samsung@@">Samsung</a>, <a href="@@R_roku@@">Roku</a> ve <a href="@@R_android@@">Android TV</a>.</p>
      <div class="preguntas">
        <details><summary>LG</summary>
          <p>TV’ye dokunduğunda ekranda izin isteyen bir soru çıkar. Alışık olduğun kumandayla onayla. Bunu yalnızca bir kez yaparsın.</p>
        </details>
        <details><summary>Samsung</summary>
          <p>TV, Mando TV’nin bağlanmasına izin verip vermediğini sorar. Kumandayla “İzin ver”i seç. Yanlışlıkla reddettiysen Ayarlar > Genel > Harici Aygıt Yöneticisi > Aygıt Bağlantı Yöneticisi’ne git ve izinli olarak değiştir.</p>
        </details>
        <details><summary>Roku</summary>
          <p>Roku izin sormaz. Bağlantı kurulmazsa Roku’da Ayarlar > Sistem > Gelişmiş sistem ayarları > Mobil uygulamalarla kontrol’e git ve ağ erişimini Varsayılan veya Permissive olarak bırak (daha yeni Roku yazılımında “Mobil uygulamalarla kontrol” ayarını Etkin yap).</p>
        </details>
        <details><summary>Android TV ve Google TV</summary>
          <p>TV 6 karakterli bir kod gösterir. Onu Mando TV’ye çıktığı gibi aynen gir. Android TV’li Sony, Philips, TCL, Hisense, Sharp, Xiaomi, Google TV’li Chromecast ve diğerlerinde çalışır.</p>
        </details>
      </div>

      <h2 id="encender">TV’yi uygulamadan açma</h2>
      <p>Mando TV, TV’yi ev ağın üzerinden açar. Bunun için iki şey gerekir: TV açıkken en az bir kez bağlanmış olman ve TV’de ağ üzerinden açmanın etkin olması. Ayarın adı modele göre değişir; en yaygın olanlar şunlar:</p>
      <div class="preguntas">
        <details><summary>LG</summary>
          <p>Ayarlarda (Ayarlar, Genel, Cihazlar, Harici Cihazlar altında; eski modellerde Bağlantı, Mobil Bağlantı Yönetimi) “Mobil cihazla TV’yi aç”ı ara ve “Wi-Fi üzerinden aç”ı etkinleştir. “Hızlı Başlatma+” varsa onu da etkinleştir.</p>
        </details>
        <details><summary>Samsung</summary>
          <p>Ayarlar > Genel > Ağ > Uzman Ayarları altında “Mobil Cihazla Aç”ı etkinleştir.</p>
        </details>
        <details><summary>Roku</summary>
          <p>Roku TV cihazlarında Ayarlar > Sistem > Güç altında “TV hızlı başlatma”yı etkinleştir. Bir TV’ye takılı Roku oynatıcılar bu şekilde açılamaz.</p>
        </details>
        <details><summary>Android TV ve Google TV</summary>
          <p>Bu üreticiye göre değişir. Ağ ya da güç ayarlarında “Wake on LAN”, “Ağ üzerinden aç”, “Ağ beklemesi” ya da “Remote start” seçeneğini ara. Bazı modellerde bu seçenek yoktur.</p>
        </details>
      </div>

      <h2 id="falla">Bir şey yolunda gitmezse</h2>
      <div class="preguntas">
        <details><summary>Bağlantı kopuyor ya da tepki gelmiyor</summary>
          <ol>
            <li>Kumanda ekranında Yeniden bağlan’a dokun.</li>
            <li>Yardımcı olmazsa Mando TV’yi kapat ve uygulamayı yeniden aç.</li>
            <li>TV başka bir IP adresi aldıysa onu listeden kaldır ve yeniden ekle.</li>
          </ol>
        </details>
        <details><summary>Bize hata raporu nasıl gönderirsin</summary>
          <ol>
            <li>Mando TV’de Kişiselleştir düğmesine dokun (üstteki ayar çubukları).</li>
            <li>Test raporunu kopyala’ya dokun.</li>
            <li>Raporu, TV’nin markası ve modeliyle birlikte hola@mandotv.app adresine bir e-postaya yapıştır.</li>
          </ol>
          <p>Rapor şifre, kod ve yazdığın hiçbir şeyi içermez.</p>
        </details>
        <details><summary>Pro’yu satın aldım ama görünmüyor</summary>
          <p>Kişiselleştir altında, satın aldığın mağaza hesabıyla Satın alımı geri yükle’ye dokun. Hâlâ görünmüyorsa bize yaz.</p>
        </details>
      </div>

      <h2 id="guias">Adım adım rehberler</h2>
      <p><a href="@@R_guias@@">Tüm rehberleri gör</a></p>
      <ul>
@@GUIAS@@
      </ul>

      <h2 id="contacto">Hâlâ sorun mu var?</h2>
      <p>Bize <a href="mailto:hola@mandotv.app?subject=Mando%20TV%20yard%C4%B1m">hola@mandotv.app</a> adresinden yaz. TV’nin markasını, modelini ve hangi adımda takıldığını söyle. Bize kendi dilinde yazabilirsin. İspanyolca veya İngilizce yanıtlarız, istersen çevirmen yardımıyla kendi dilinde de.</p>
'''

PRIVACIDAD = dict(
  titulo='Gizlilik Politikası | Mando TV',
  desc='Mando TV kişisel veri toplamaz: hesap, reklam ve izleyici yok. Uygulama yalnızca Wi-Fi ağının içinde TV’nle konuşur.',
  h1='Gizlilik',
  intro='Kısacası: Mando TV verilerini toplamaz. Hesap, reklam, izleyici ve yaptıklarını kaydeden kendi sunucularımız yok.',
)
PRIVACIDAD_HTML = '''      <p class="fecha">14 Kasım 2026’dan beri geçerlidir. Son güncelleme: 26 Kasım 2026.</p>

      <h2>Biz kimiz</h2>
      <p>Mando TV, televizyonunu telefonundan ya da bilgisayarından kontrol etmeni sağlayan bir uygulamadır. Bu politika, uygulamanın hangi bilgileri kullandığını ve bunlarla ne yaptığını anlatır. Sorularında bize <a href="mailto:hola@mandotv.app">hola@mandotv.app</a> adresinden yazabilirsin.</p>

      <h2>Hangi verileri topluyoruz</h2>
      <p>Uygulama: hiçbirini. Uygulama, senin hakkında ya da onu nasıl kullandığın hakkında bize veya üçüncü kişilere hiçbir bilgi göndermez. Analiz, reklam veya izleme aracı kullanmaz.</p>
      <p>Bu web sitesi: Ziyaretleri, <a href="#cookies">Bu sitedeki çerezler</a> bölümünde açıklanan iki şekilde ölçüyoruz.</p>

      <h2>Uygulamanın cihazında sakladıkları</h2>
      <p>Çalışabilmek için uygulama aşağıdakileri yalnızca telefonunda ya da bilgisayarında saklar:</p>
      <ul>
        <li>Eklediğin televizyonlar: ad, marka, ağındaki IP adresi ve açmak için kullanılan ağın donanım adresi (MAC).</li>
        <li>İzni onayladığında her televizyonun verdiği bağlantı anahtarları. Bunlar sistemin güvenli deposunda şifreli olarak saklanır (iPhone ve Mac’te Anahtar Zinciri, Android’de Keystore, Windows’ta korumalı depolama).</li>
        <li>Ayarların: açık ya da koyu tema, arka plan rengi, titreşim ve kumanda türü.</li>
        <li>Pro özelliklerini kullanırsan: favori uygulamaların, rutinlerin ve son YouTube aramaların (bunları uygulamadan silebilirsin).</li>
      </ul>
      <p>Uygulamayı sildiğinde bunların hepsi onunla birlikte silinir.</p>

      <h2>Uygulama kimlerle konuşur</h2>
      <p>Televizyonlarınla, evindeki Wi-Fi ağının içinde. Onları bulmak için uygulama yerel ağını tarar; bu yüzden iPhone’da “Yerel Ağ” izni ister. Uygulamanın klavyesiyle yazdığın metin doğrudan televizyona gider ve kaydedilmez.</p>
      <p>Ayrıca uygulama açılırken bu web sitesinden küçük bir herkese açık dosya indirir (mandotv.app/app/config.json); amaç, kurman gereken yeni bir sürüm olup olmadığını ve hangi özelliklerin Mando TV Pro’ya ait olduğunu öğrenmektir. Bu, bir sayfayı açmak gibi bir indirmedir: uygulama ne verilerini, ne televizyonlarını ne de yaptığın şeyi gönderir. Yalnızca sana uygun bildirimi gösterebilmek için uygulama sürümünü ve sistemi (örneğin Android) belirtir. İnternetin yoksa uygulama en son indirdiği dosyayla çalışmaya devam eder; indirilemeden 30 günden fazla geçerse uygulama senden kısa bir süre internete bağlanmanı ister.</p>

      <p>Televizyona fotoğraf ya da video gönderirsen (bir Pro özelliği), televizyon yalnızca seçtiğin dosyaları doğrudan telefonundan veya bilgisayarından evindeki Wi-Fi üzerinden indirir. Bunlar ne internetten ne de bizden geçer, uygulama diğer fotoğraflarını görmez ve paylaşım, o ekranı kapattığında sona erer.</p>
      <h2>Mikrofon ve ses</h2>
      <p>iPhone, Mac ve Android’de sesli arama, mikrofonu yalnızca konuşma düğmesine dokunduğun sürece kullanır. Söylediklerin sistemin konuşma tanıma özelliği tarafından metne çevrilir: iPhone ve Mac’te Apple, Android’de Google tarafından, her biri kendi gizlilik koşullarına göre. Windows’ta konuşma kendi bilgisayarında tanınır ve cihazdan çıkmaz; yalnızca çok eski işlemcilerde uygulama Microsoft’un Windows ses girişini kullanır, onların gizlilik koşullarına göre. Windows’ta mikrofon, ses panelini açtığında açılır; kapattığında veya 30 saniye kullanılmadığında kapanır; konuşmadığın sürece hiçbir şey kaydedilmez ve saklanmaz. Mando TV sesi ne kaydeder ne de saklar ve ortaya çıkan metin, klavyeyle yazdığın gibi doğrudan televizyonuna gider.</p>

      <h2>Ev: Apple Home ve Google Home cihazları</h2>
      <p>Ev bölümünü (test aşamasında) açtığında uygulama, Apple’ın Ev uygulamasında (HomeKit) ya da Google Home’da zaten bulunan cihazları görmek için izin ister. Bu izinle adlarını, odalarını ve durumlarını (açık ya da kapalı, parlaklık, sıcaklık veya bir ev aletinin programının hangi aşamada olduğu) okur; bunları göstermek ve dokunduğunu onlara iletmek için. Her şey telefonun ile Apple ya da Google’ın sistemi arasında gerçekleşir: Mando TV bu listeyi saklamaz, ne bize ne üçüncü kişilere gönderir ve ne reklam ne de analiz için kullanır. Android’de Google Home, kendi Google hesabınla ve Google’ın gizlilik politikasına göre çalışır. İzni istediğin zaman geri alabilirsin: iPhone’da Ayarlar &gt; Gizlilik ve Güvenlik &gt; HomeKit’ten, Android’de Google hesabının ayarlarından.</p>
      <p>“Ev senin için nasıl çalıştı?”ya dokunduğunda e-posta uygulaman, hola@mandotv.app adresine teknik bir özet içeren bir mesajla açılır: uygulamanın sürümü, sistem ve her türden kaç cihazın göründüğü ve yanıt verip vermedikleri. Cihazların, odaların ya da evinin adları yer almaz ve mesaj yalnızca sen kendin gönderirsen gönderilir.</p>

      <h2>Test raporu</h2>
      <p>Uygulamada, hataları gidermemize yardım eden bir “Test raporunu kopyala” düğmesi var. Rapor, uygulama açık olduğu sürece yalnızca uygulamanın belleğinde kalır ve kendiliğinden asla gönderilmez: kopyalayıp paylaşmak sana kalmış. Bağlantı anahtarlarını, eşleştirme kodlarını ve yazdığın hiçbir şeyi içermez; yalnızca uygulamanın attığı adımları içerir, örneğin aramalar, bağlantılar ve hatalar.</p>

      <h2 id="cookies">Bu sitedeki çerezler</h2>
      <p>Bu yalnızca mandotv.app web sitesi için geçerlidir, uygulama için değil.</p>
      <h3>Her zaman çerezsiz</h3>
      <p>Ziyaretleri Cloudflare Web Analytics ile anonim olarak sayıyoruz: sitenin kaç kişi tarafından ziyaret edildiği, hangi sayfaların okunduğu ve hangi ülkeden. Çerez kullanmaz, seni tanımlamak için IP adresini kullanmaz ve diğer web sitelerinde yaptıklarını izlemez.</p>
      <h3>Çerezli, yalnızca kabul edersen</h3>
      <p>Çerez bildiriminde “Kabul et”e dokunursan sitenin nasıl kullanıldığını daha iyi anlamak için (Google LLC’nin) Google Analytics’i etkinleştiririz: sayfa görüntülemeleri, kalış süresi, cihaz türü, yaklaşık şehir ve nereden geldiğin. Bunun için tarayıcında _ga ve _ga_* çerezlerini 2 yıla kadar saklar. Google bu verileri Şili dışındaki sunucularda işleyebilir. Reklam özelliklerini ve Google Signals’ı devre dışı bıraktık ve bu verileri sana reklam göstermek için kullanmıyoruz.</p>
      <p>“Reddet”e dokunursan ya da hiçbir şey seçmezsen Google Analytics yüklenmez ve hiçbir çerez saklanmaz. Kararını her sayfanın en altındaki “Çerezler” düğmesiyle istediğin zaman değiştirebilirsin; onayı geri çekersen bu çerezleri sileriz.</p>
      <p>Seçimin, bir daha sormamamız için tarayıcında saklanır (yerel depolama, kimseye gönderilmez).</p>

      <h2>Satın alımlar</h2>
      <p>Mando TV Pro’yu satın aldığında ödemeyi uygulama mağazası işler (App Store, Google Play veya Microsoft Store). Kart bilgilerini almayız ve saklamayız. Mağaza uygulamaya yalnızca satın alımın var olduğunu bildirir.</p>

      <h2>Bize gönderdiğin e-postalar</h2>
      <p>Bize <a href="mailto:hola@mandotv.app">hola@mandotv.app</a> adresinden yazdığında e-posta adresini ve bize anlattıklarını yalnızca sana yanıt vermek için kullanırız. Onları paylaşmayız ve reklam için kullanmayız. İstediğin zaman mesajlarının silinmesini isteyebilirsin.</p>

      <h2>Çocuklar</h2>
      <p>Uygulama hiç kimseden, çocuklardan da, veri toplamaz.</p>

      <h2>Bu politikadaki değişiklikler</h2>
      <p>Bir gün uygulamanın verilerinle yaptığı şey değişirse, değişiklik uygulamaya ulaşmadan önce bu sayfayı ve yukarıdaki tarihi güncelleriz.</p>
'''


# >>> guías traídas del inglés (ensamblar.py)
GUIAS += [
  dict(clave='no-sub', corto='Abonelik gerektirmeyen kumanda uygulaması', fecha='2026-11-23',
    titulo='Abonelik ve reklam olmadan TV kumanda uygulaması',
    desc='Reklamlı ya da haftalık abonelikli kumanda uygulamalarından bıktın mı? Mando TV ücretsiz ve reklamsız, Pro isteğe bağlı. Dürüst karşılaştırma.',
    h1='Abonelik ve reklam olmadan bir kumanda uygulaması',
    intro='Birçok evrensel kumanda uygulaması reklam gösterir ya da çalışmadan önce haftalık abonelik ister. Mando TV farklı bir yol izler: kumanda ücretsizdir, reklam ve hesap yoktur. İsteğe bağlı Pro’yu yalnızca bir kez satın alırsın. İşte karşılaştırma, uygulamanın yapamadıklarıyla birlikte.',
    pasos=[
      'Yüklemeden önce bir uygulamanın mağaza sayfasını aç ve uygulama içi satın alımlara bak. Haftalık ya da aylık fiyatlar abonelik demektir.',
      'Google Play’de sayfada “Reklam içerir” yazıp yazmadığına bak ve az yıldızlı en yeni yorumları oku: beklenmedik ödeme duvarları genellikle orada ortaya çıkar.',
      'Uygulamanın TV’ni Wi-Fi ile kontrol edebildiğinden emin ol. Mando TV, Samsung (2016’dan itibaren), LG webOS, Roku, Google TV, Android TV ve Fire TV ile çalışır.',
      'Mando TV’yi yükle, telefonunu TV’yle aynı Wi-Fi ağına bağla ve listede TV’ne dokun.',
      'TV’deki soruyu onayla ya da gösterilen kodu gir. Tuşlar, ses, kanallar ve klavye ücretsiz.',
    ],
    tabla=dict(titulo='Mando TV ile birçok kumanda uygulamasının karşılaştırması',
      cabeza=['', 'Mando TV', 'Reklamla ya da abonelikle çalışan birçok uygulama'],
      filas=[
        ['Temel kumanda', 'Ücretsiz', 'Çoğu zaman reklamlı ücretsiz ya da deneme süresinin ardında gizli'],
        ['Reklam', 'Yok', 'Sık'],
        ['Abonelik', 'Yok. Pro isteğe bağlı tek seferlik satın alım', 'Haftalık ya da aylık planlar yaygın'],
        ['Hesap', 'Gerekmez', 'Değişir'],
        ['Wi-Fi üzerinden akıllı TV’ler', 'Samsung (2016’dan itibaren), LG webOS, Roku, Google TV, Android TV, Fire TV, Apple TV (beta)', 'Uygulamaya göre değişir'],
        ['Eski televizyonlar için kızılötesi', 'Kızılötesi vericisi olan Android telefonlarda ücretsiz (yeni)', 'Bazı uygulamalar, yalnızca kızılötesi vericisi olan telefonlarda'],
        ['Bluetooth', 'Android 9’dan itibaren beta, ücretsiz', 'Uygulamaya göre değişir'],
        ['TV’ye fotoğraf ve video', 'Pro, Wi-Fi ile (yansıtma değil)', 'Uygulamaya göre değişir'],
        ['Telefonlar ve bilgisayarlar', 'iPhone, iPad, Mac ve Windows, ayrıca erken erişimde Android', 'Değişir'],
        ['Ekran yansıtma', 'iPhone, iPad ve Windows’ta her birinin kendi yerleşik özelliğiyle ücretsiz. Windows’ta Pro, bilgisayar ekranını LG, Samsung, Hisense ve Android TV televizyonlara da yansıtabilir (beta)', 'Bazı uygulamalar sunar'],
      ],
      nota='Mando TV belirli bir uygulamayla karşılaştırılmıyor. Güncel fiyatlar her uygulamanın mağaza sayfasında yer alır.'),
    extra=[
      ('Mando TV’nin yapmadıkları', 'iPhone ve iPad’de seni Denetim Merkezi’ndeki Ekran Yansıtma’ya yönlendirir; bu, iPhone’un kendi özelliğidir ve AirPlay’li televizyonlarla çalışır. Windows’ta Yayınla’yı (Windows + K) açar ve Mando TV Pro, bilgisayar ekranını Wi-Fi’ın üzerinden LG, Samsung, Hisense ve Android TV televizyonlara gönderebilir (beta, birkaç saniye gecikmeli ve sessiz). Mando TV Pro ile ayrıca fotoğrafları ve videoları Wi-Fi’ın üzerinden TV’ne gönderebilir. Akıllı TV’leri ev Wi-Fi’ı üzerinden kontrol eder. Akıllı TV özelliği olmayan televizyonlar, kızılötesi vericisi olan bir Android telefondan kızılötesiyle kontrol edilebilir. Android 9’dan itibaren telefon, Google TV, Android TV ve Fire TV’ye Wi-Fi’a hiç gerek kalmadan Bluetooth klavye ve kumanda olarak da bağlanabilir. Bu seçenek betadadır ve ücretsizdir.'),
      ('Mando TV nasıl para kazanır', 'Reklamla değil, verilerinle de değil: uygulama hiç veri toplamaz. Mando TV, ekstralar için isteğe bağlı tek seferlik bir satın alım olan Pro ile finanse edilir. Temel kumanda ücretsizdir.'),
      ('Zaten sahip olduğun cihazlarda', 'iPhone, iPad ve Mac için App Store’dan, Windows bilgisayarlar için Microsoft Store’dan ve Android için Google Play’deki ücretsiz erken erişimden. Bkz. [iPhone kumanda uygulaması](@iphone) ve [Windows kumanda uygulaması](@windows).'),
      ('Gizlilik', 'Uygulamada hesap ve izleme yok. TV’yle iletişim yalnızca yerel ağda gerçekleşir, bağlantı verileri cihazında şifreli olarak kalır. Ayrıntılar [Gizlilik Politikası](@privacidad) sayfasında.'),
    ],
    marca=None,
    faq=[
      ('Abonelik gerektirmeyen bir kumanda uygulaması var mı?', 'Evet. Mando TV’de hiç abonelik yok: kumanda ücretsiz ve reklamsız, Pro isteğe bağlı tek seferlik satın alım.'),
      ('Mando TV gerçekten ücretsiz mi?', 'Evet. Yön tuşları, OK, geri, ana ekran, ses, kanallar, rakamlar, klavye ve açma/kapatma ücretsiz, reklamsız ve süre sınırı olmadan.'),
      ('Wi-Fi olmadan çalışır mı?', 'Çoğunlukla hayır. Mando TV akıllı TV’leri ev Wi-Fi’ın üzerinden kontrol eder. İstisnalar: kızılötesi vericisi olan Android telefonlarda kızılötesi; akıllı TV özelliği olmayan ya da Wi-Fi’a bağlı olmayan televizyonlarda da çalışır. Bir de Bluetooth: Android 9’dan itibaren betada, Google TV, Android TV ve Fire TV için.'),
    ]),
  dict(clave='roku-app-alt', corto='Roku uygulaması alternatifi', fecha='2026-11-23',
    titulo='Roku uygulaması alternatifi: basit Roku kumandası',
    desc='Roku uygulamasına alternatif: Mando TV, Roku TV ve oynatıcıları Wi-Fi ile hesapsız ve reklamsız kontrol eder; Samsung, LG ve Google TV’yi de.',
    h1='Roku uygulaması alternatifi: tüm televizyonlar için tek uygulama',
    intro='Resmî Roku uygulaması çok şey yapar: Channel Store, yayın aktarma, Private Listening ve bir kumanda. Yalnızca hızlı bir kumanda arıyorsan ya da evde bir Samsung, LG veya Google TV de varsa Mando TV, Roku’yu Wi-Fi’ın üzerinden hesapsız kontrol eden basit bir alternatiftir.',
    pasos=[
      'Telefonunu ve Roku’yu aynı Wi-Fi ağına bağla.',
      'Mando TV’yi indir ve aç. Roku TV’n ya da Roku oynatıcın listede görünür. Üzerine dokun. Roku kod istemez.',
      'Yön tuşlarını, OK’i, geri, ana ekran, sesi ve klavyeyi kullan. Roku kanallarında aramaları telefonun klavyesiyle yaz.',
      'Tuşlar hiçbir şey yapmıyorsa Roku’da Ayarlar > Sistem > Gelişmiş sistem ayarları > Mobil uygulamalarla kontrol’e git ve ağ erişimini Varsayılan veya Permissive yap (yeni Roku yazılımında Mobil uygulamalarla kontrol’ü Etkin yap).',
      'İsteğe bağlı: Mando TV’nin TV’yi açabilmesi için Roku TV’de Ayarlar > Sistem > Güç altında “TV hızlı başlatma”yı etkinleştir.',
    ],
    extra=[
      ('Mando TV’nin daha uygun olduğu yerler', 'Birden çok televizyon için tek uygulama: Roku, Samsung, LG ve Google TV ya da Android TV. Hesap ve reklam yok. Masa başında pratik olan Windows bilgisayarda da çalışır. Yön tuşları ve ses hızlı tepki verir, klavyeyle aramaları zahmetsizce yazarsın.'),
      ('Resmî Roku uygulamasının daha iyi olduğu yerler', 'Roku uygulamasını, kumandanın ötesinde sunduğu şeyler için tut: Roku Channel Store’dan kanal gezmek ve eklemek, kendi yayın aktarması ve Private Listening (sesi telefondaki kulaklıktan dinleme). İstersen ikisini de kullan. Aynı telefonda çalışabilirler.'),
      ('Roku TV cihazları ve Roku oynatıcılar', 'İkisi de çalışır. Buna TCL, Hisense, Philips ve diğerlerinin Roku TV modelleri ile Roku Express, Streaming Stick ve Ultra dahildir. Ayrıntılar [Roku kumanda uygulaması sayfasında](@roku).'),
      ('Roku uygulaması artık çalışmıyorsa', 'Tuşlar artık tepki vermiyorsa Roku genellikle uygulamalarla kontrolü engelliyordur. [Roku uygulaması çalışmıyor](@roku-403) rehberi sorunu çözen ayarı gösterir.'),
      ('Ücretsiz ve Pro', 'Yön tuşları, OK, geri, ana ekran, ses, kanallar, rakam tuşları, klavye, uygulama açma, girişleri değiştirme ve açma ya da kapatma ücretsizdir, reklamsız ve aboneliksiz. Touchpad, sesli komutlar, favori uygulamalar, rutinler ve uyku zamanlayıcısı, aboneliksiz tek seferlik bir satın alım olan Mando TV Pro’nun parçasıdır.'),
    ],
    marca='roku',
    faq=[
      ('Mando TV’yi kullanmak için Roku hesabına ihtiyacım var mı?', 'Hayır. Mando TV, Roku’yla ev ağın üzerinden iletişim kurar ve hesap istemez.'),
      ('Mando TV, Roku Mobile uygulamasının yerini tamamen tutar mı?', 'Kumanda olarak evet. Channel Store, yayın aktarma ve Private Listening için resmî Roku uygulamasını tut.'),
      ('Roku Express’im ya da Streaming Stick’im ile çalışır mı?', 'Evet. Tüm Roku oynatıcılar ve Roku TV cihazları aynı şekilde kontrol edilir.'),
    ]),
  dict(clave='lg-thinq', corto='LG ThinQ uygulaması alternatifi', fecha='2026-11-23',
    titulo='LG ThinQ uygulaması alternatifi: hesapsız LG kumanda',
    desc='Yalnızca kumanda olarak LG ThinQ uygulamasına alternatif mi arıyorsun? Mando TV, webOS’lu LG TV’leri Wi-Fi ile LG hesabı ve reklam olmadan kontrol eder.',
    h1='LG TV’n için LG ThinQ uygulaması alternatifi',
    intro='LG ThinQ, LG’nin tüm akıllı ev için tasarladığı resmî uygulamasıdır: ev aletleri, TV ve daha fazlası. LG TV’n için yalnızca basit bir kumanda istiyorsan Mando TV tam olarak bunu evindeki Wi-Fi üzerinden yapar; LG hesabı oluşturman gerekmez ve reklam yoktur.',
    pasos=[
      'Telefonunu ya da bilgisayarını (iPhone, Android veya Windows) ve LG TV’ni aynı Wi-Fi ağına bağla.',
      'Mando TV’yi indir ve aç. LG TV’n listede kendiliğinden görünür. Üzerine dokun.',
      'TV’de bir soru çıkar. TV’nin kumandasıyla, ekranın altındaki joystick’le ya da Magic Remote ile bir kez onayla.',
      'Tuşlar, ses ve klavye hemen çalışır. LG hesabına ihtiyacın yok ve TV’yi kaydettirmen gerekmez.',
      'İsteğe bağlı: TV’yi telefondan da açabilmen için TV ayarlarında “Mobil cihazla TV’yi aç”ı etkinleştir.',
    ],
    extra=[
      ('Mando TV mi, LG ThinQ mu: hangisi ne için', 'Çamaşır makinesi, buzdolabı ya da klima gibi LG ev aletlerini yönetmek istiyorsan veya LG hesabı özelliklerine ihtiyacın varsa ThinQ’yu kullan. TV için hızlı, basit ve aynı uygulamada Samsung, Roku ve Google TV’de de çalışan bir kumanda istiyorsan Mando TV’yi kullan. Birçok kişi ikisini de tutar: ev aletleri için ThinQ, TV için Mando TV.'),
      ('Mando TV bir LG TV’de ne yapar', 'webOS’lu LG akıllı TV’lerle, yani 2014’ten bu yana çoğu modelle çalışır; LED, NanoCell, QNED ve OLED dahil. Sana yön tuşlarını, OK, geri, ana ekran, ses, kanal, sessiz, oynatma kontrollerini ve TV aramasında ve çoğu uygulamada yazmak için bir klavye sunar. Uygulama listesi ve giriş listesi de ücretsizdir. Pro ile ayrıca Magic Remote gibi bir imleç gelir.'),
      ('Mando TV’nin yapmadıkları', 'LG ev aletlerini kontrol etmez, LG hesabını kullanmaz ve TV’deki LG hesap hizmetlerinin yerini tutmaz. Bir kumandadır, akıllı ev merkezi değil.'),
      ('Gizlilik ve reklam', 'Mando TV’de reklam ve hesap yoktur. TV’yle yalnızca ev ağının içinde konuşur ve bağlantı anahtarını cihazında şifreli olarak saklar. Tüm özellikleri [LG kumanda uygulaması](@lg) sayfasında bulabilirsin.'),
      ('Ücretsiz ve Pro', 'Yön tuşları, OK, geri, ana ekran, ses, kanallar, rakam tuşları, klavye, uygulama açma, girişleri değiştirme ve açma/kapatma ücretsizdir, reklamsız ve aboneliksiz. Touchpad, sesli komutlar, favori uygulamalar, rutinler ve uyku zamanlayıcısı, aboneliksiz tek seferlik bir satın alım olan Mando TV Pro’nun parçasıdır.'),
    ],
    marca='lg',
    faq=[
      ('LG TV’mi LG ThinQ uygulaması olmadan kontrol edebilir miyim?', 'Evet. Mando TV, webOS’lu LG TV’lere doğrudan Wi-Fi ağın üzerinden bağlanır. TV’de bir kez soruyu kabul edersin ve hepsi bu, LG hesabı olmadan.'),
      ('Mando TV, LG Magic Remote’un imleciyle çalışır mı?', 'Mando TV Pro’da, Magic Remote’un oku hareket ettirmesine benzer şekilde telefon ekranında parmağınla hareket ettirdiğin bir imleç var.'),
      ('Mando TV LG’ye mi ait?', 'Hayır. Mando TV bağımsız bir uygulamadır ve LG ile bağlantısı yoktur. LG ve ThinQ sahiplerine aittir ve yalnızca uyumluluğu açıklamak için anılır.'),
    ]),
  dict(clave='smartthings', corto='SmartThings alternatifi', fecha='2026-11-23',
    titulo='SmartThings çalışmıyor mu? Samsung için basit alternatif',
    desc='SmartThings çok mu yavaş ya da hatalı? Mando TV, Tizen’li Samsung TV’leri doğrudan Wi-Fi ile kontrol eder. Samsung hesabı yok, reklam yok. Adım adım.',
    h1='Samsung TV’ler için SmartThings alternatifi',
    intro='SmartThings, tüm akıllı ev için Samsung uygulamasıdır ve kumandası Samsung hesabın üzerinden çalışır. Artık çalışmıyorsa ya da hızlı bir çözüm arıyorsan Mando TV, Tizen’li, 2016 ve sonrası Samsung TV’leri doğrudan Wi-Fi ağın üzerinden, hesapsız kontrol eder.',
    pasos=[
      'Telefonunu ve Samsung TV’yi aynı Wi-Fi ağına bağla.',
      'Mando TV’yi indir ve uygulamayı aç. Samsung TV’n listede kendiliğinden görünür. Üzerine dokun.',
      'TV, bağlantıya izin vermek isteyip istemediğini sorar. Kumandayla ya da TV’deki tuşla “İzin ver”i seç (yalnızca ilk seferde).',
      'Hemen yön tuşlarını, OK, geri, ana ekran, ses, kanallar ve klavyeyi kullan.',
      'İsteğe bağlı: Mando TV’nin TV’yi de açabilmesi için Ayarlar > Genel > Ağ > Uzman Ayarları altında “Mobil Cihazla Aç”ı etkinleştir.',
    ],
    extra=[
      ('Telefon kumandası neden artık çalışmıyor', 'Nedenler genellikle basittir: telefon ve TV farklı Wi-Fi ağlarındadır, bir VPN etkindir ya da TV derin beklemededir. SmartThings’te ayrıca Samsung hesabı sorun çıkarabilir, örneğin oturumun kapatıldıysa. Mando TV ev ağındaki TV’yle doğrudan konuşur, oturum açılacak bir hesap yoktur. Daha fazla ipucunu [Telefonun TV’yi bulamıyor](@not-found) sayfasında bulabilirsin.'),
      ('Mando TV mi, SmartThings mi: hangisi ne için', 'SmartThings’i Samsung ev aletleri, lambalar ya da diğer akıllı ev cihazları veya Samsung hesabının özellikleri için kullanıyorsan tut. TV için sadece hızlı bir kumanda istiyorsan ya da evde LG, Roku, Google TV veya Fire TV’den bir cihaz da varsa Mando TV’yi kullan: tek uygulama hepsini kontrol eder. İki uygulama aynı telefonda yüklü olabilir.'),
      ('İzni yanlışlıkla reddettiysen', 'TV’de Ayarlar > Genel > Harici Aygıt Yöneticisi > Aygıt Bağlantı Yöneticisi’ne git ve Mando TV’yi izinli yap.'),
      ('Kumandan yok mu?', 'Soruyu TV’nin kendi üzerindeki tuşla onaylayabilirsin. [Orijinal kumandasız Samsung TV](@samsung-lost) rehberi nasıl yapacağını gösterir.'),
      ('Ücretsiz ve Pro', 'Kumandayı ücretsiz indirip kullanabilirsin, reklamsız ve aboneliksiz. Mando TV Pro, ekstralar için isteğe bağlı tek seferlik bir satın alımdır.'),
    ],
    marca='samsung',
    faq=[
      ('Samsung TV’mi SmartThings olmadan kontrol edebilir miyim?', 'Evet. Mando TV, Tizen’li Samsung TV’lere doğrudan Wi-Fi ağın üzerinden bağlanır. Bağlantıya TV’de bir kez izin verirsin, Samsung hesabı olmadan.'),
      ('Mando TV Samsung ev aletlerini de kontrol eder mi?', 'Hayır. Yalnızca TV için bir kumandadır. Ev aletleri ve diğer akıllı ev cihazları için SmartThings’i tutarsın.'),
      ('Mando TV Samsung’a mı ait?', 'Hayır. Mando TV bağımsız bir uygulamadır ve Samsung ile bağlantısı yoktur. Samsung ve SmartThings sahiplerine aittir ve yalnızca uyumluluğu açıklamak için anılır.'),
    ]),
  dict(clave='googletv-alt', corto='Google TV kumanda alternatifi', fecha='2026-11-23',
    titulo='Google TV kumandası çalışmıyor mu? Alternatifi',
    desc='Google TV için telefon kumandası TV’yi bulamıyor mu? Mando TV, Google TV ve Android TV’yi Wi-Fi ile Google hesabı ve reklam olmadan kontrol eder.',
    h1='Telefonda Google TV kumanda alternatifi',
    intro='Google TV ve Android TV için telefon kumandası Google’ın kendi uygulamasının içindedir ve Google hesabına bağlıdır. TV’yi bulamazsa elin kolun bağlanır. Mando TV, ekrandaki 6 karakterli kodla eşleşen ve Google hesabı olmadan çalışan ayrı bir kumanda uygulamasıdır; iPhone’da, Android telefonda ya da Windows bilgisayarda.',
    pasos=[
      'TV’yi aç ve telefonunu aynı Wi-Fi ağına bağla.',
      'Mando TV’yi indir ve uygulamayı aç. Listede Google TV ya da Android TV’li televizyonuna dokun.',
      'TV 6 karakterli bir kod gösterir. Kodu Mando TV’ye gir ve Eşleştir’e dokun.',
      'Yön tuşlarını, OK, geri, ana ekran, ses ve klavyeyi kullan. Hiçbir yerde oturum açman gerekmez.',
      'İsteğe bağlı: uygulamanın TV’yi de açabilmesi için TV ayarlarında Wake on LAN ya da “Ağ üzerinden aç”ı ara.',
    ],
    extra=[
      ('Telefon kumandası TV’yi neden artık bulamıyor', 'Çoğunlukla sorun ağdadır: telefon ve TV farklı Wi-Fi ağlarındadır, bir VPN etkindir ya da bir misafir ağı cihazları ayırır. Önce bunu çöz, çünkü tüm kumanda uygulamalarını etkiler. Daha fazlası için [Telefonun TV’yi bulamıyor](@not-found) sayfasına bak.'),
      ('Hangi televizyonlarla çalışır', 'Sony, TCL, Hisense, Philips, Sharp, Xiaomi, Toshiba ve daha fazlasının Google TV ve Android TV’li televizyonları, ayrıca Google TV’li Chromecast, Google TV Streamer ve Nvidia Shield. Hepsi aynı şekilde eşleşir, ekrandaki kodla bir kez.'),
      ('Google’ın uygulamasının daha iyi olduğu yerler', 'Google’ın uygulaması izlenecek içerik bulmana da yardım eder ve izleme listeni hatırlar. Bunun için onu tut. Mando TV yalnızca kumandadır ve aynı uygulamadan ayrıca Samsung, LG, Roku ve Fire TV cihazlarını, bir de Windows bilgisayardan kontrol eder.'),
      ('Eski Android TV kumanda uygulaması yoksa', 'Google, telefon kumandasını eski Android TV Remote Control uygulamasından Google TV uygulamasına taşıdı. Bağımsız bir kumanda arıyorsan Mando TV bir seçenektir.'),
      ('Ücretsiz ve Pro', 'Kumandayı ücretsiz indirip kullanabilirsin, reklamsız ve aboneliksiz. Mando TV Pro, ekstralar için isteğe bağlı tek seferlik bir satın alımdır.'),
    ],
    marca='android',
    faq=[
      ('Mando TV’yi Google TV ile kullanmak için Google hesabına ihtiyacım var mı?', 'Hayır. Eşleşmek için TV’deki kod yeter.'),
      ('Google TV’li Chromecast ile çalışır mı?', 'Evet. Eşleştirme aynı şekilde, ekrandaki 6 karakterli kodla yapılır.'),
      ('iPhone’dan kullanabilir miyim?', 'Evet. Mando TV, iPhone ve iPad için App Store’da, Windows için Microsoft Store’da ve Android için Google Play’deki ücretsiz erken erişimde mevcut.'),
    ]),
  dict(clave='windows', corto='Windows bilgisayar için kumanda', fecha='2026-11-23',
    titulo='Windows kumanda uygulaması: TV’yi bilgisayardan kontrol et',
    desc='Samsung, LG, Roku, Google TV veya Fire TV’yi Mando TV ile Windows bilgisayardan kontrol et: klavye kısayolları, mini kumanda ve Wi-Fi. Microsoft Store’da.',
    h1='Windows bilgisayar için kumanda uygulaması',
    intro='Mando TV’nin, bilgisayarını ya da dizüstünü ev ağı üzerinden televizyonun kumandasına çeviren bir Windows uygulaması var. TV’de gerçek klavyenle yaz, çalışırken küçük bir kumanda penceresini önde tut ve Samsung, LG, Roku, Google TV ya da Fire TV’yi aynı uygulamayla kontrol et.',
    pasos=[
      'Mando TV’yi Windows 10 veya 11’li bir bilgisayara Microsoft Store’dan ücretsiz yükle.',
      'Bilgisayarın ve TV’nin aynı ağda, Wi-Fi ya da kabloyla aynı router’da olduğundan emin ol.',
      'Mando TV’yi aç. TV listede görünür. Üzerine tıkla.',
      'TV soruyorsa (LG, Samsung) soruyu onayla ya da gösterilen kodu gir (Google TV, Fire TV).',
      'Tuşlara tıkla ya da klavyenle bir arama yaz. Hepsi bu.',
    ],
    extra=[
      ('Klavye kısayolları (Pro)', 'Pro ile bilgisayarının klavyesi kumandaya dönüşür: hareket için yön tuşları, OK için Enter, geri için Backspace ya da Esc, ses için artı ve eksi, sessiz için M ve duraklatmak için Boşluk.'),
      ('Mini kumanda (Pro)', 'Diğer tüm pencerelerin üstünde duran küçük bir kumanda penceresi. Böylece işini bölmeden sesi değiştirir ya da duraklatırsın.'),
      ('Bilgisayardan TV’de yazma', 'TV’nin ekran klavyesi yavaştır. Mando TV’de gerçek klavyenle yazarsın ve metin TV’nin arama kutusuna gider. Bu kısım ücretsiz.'),
      ('Daha fazla ayrıntı', 'Adım adım rehberi [TV’yi bilgisayarla kontrol etme](@pc) sayfasında bulabilirsin. Telefon için [Telefonu Wi-Fi ile kumanda olarak kullanma](@wifi) sayfasını oku.'),
      ('Ücretsiz ve Pro', 'Yön tuşları, OK, geri, ana ekran, ses, kanallar, rakam tuşları, klavye, uygulama açma, girişleri değiştirme ve açma ya da kapatma ücretsizdir, reklamsız ve aboneliksiz. Touchpad, sesli komutlar, favori uygulamalar, rutinler ve uyku zamanlayıcısı, aboneliksiz tek seferlik bir satın alım olan Mando TV Pro’nun parçasıdır. Windows’ta Pro’yu Microsoft Store üzerinden satın alırsın.'),
      ('Bilgisayardan sesli komutlar (Pro)', 'Pro ile TV’yle bilgisayarın mikrofonundan konuşabilirsin. Konuşma doğrudan bilgisayarda tanınır: internete ihtiyacın yok ve Windows’ta hiçbir şey ayarlaman gerekmez. Söylediğin bilgisayardan asla çıkmaz ve kaydedilmez. Yalnızca çok eski işlemcilerde uygulama Windows ses girişine geçer. Bunun için gizlilik ayarlarında çevrimiçi konuşma tanıma açık olmalı ve dilin Windows’a eklenmiş olmalı.'),
    ],
    marca=None,
    faq=[
      ('Windows kumanda uygulaması Bluetooth ya da kablo gerektirir mi?', 'Hayır. Ev ağını kullanır. Bilgisayarın ve TV’nin aynı router’a bağlı olması yeterli.'),
      ('Windows’tan hangi televizyonları kontrol edebilirim?', 'Tizen’li Samsung TV’ler, webOS’lu LG TV’ler, Roku TV ve oynatıcılar, Google TV ve Android TV ile Fire TV.'),
      ('TV görüntüsünü bilgisayarda görebilir ya da bilgisayarın hoparlörlerinden dinleyebilir miyim?', 'Hayır. Mando TV yalnızca bir kumandadır. TV görüntüsünü bilgisayara yansıtmaz ya da aktarmaz.'),
      ('Windows bilgisayarımda ses neden çalışmıyor?', 'Ses kontrolü bir Pro özelliğidir. Bu yüzden Pro’nun etkin olduğunu ve bilgisayarın mikrofonunun çalıştığını kontrol et. Çoğu bilgisayarda konuşma, internet olmadan doğrudan bilgisayarda tanınır. Yalnızca çok eski işlemcilerde uygulama Windows ses girişini kullanır: o zaman Windows’un gizlilik ayarlarında çevrimiçi konuşma tanımayı aç ve dil ayarlarında dilini ekle.'),
    ]),
  dict(clave='iphone', corto='iPhone kumanda uygulaması', fecha='2026-11-23',
    titulo='iPhone kumanda uygulaması: Samsung, LG, Roku, Google TV',
    desc='iPhone’unu Wi-Fi ile Samsung, LG, Roku, Google TV ve Fire TV için kumanda olarak kullan. App Store’da ücretsiz, hesapsız ve reklamsız.',
    h1='iPhone kumanda uygulaması: tüm televizyonlar için tek uygulama',
    intro='Mando TV, iPhone’unu ya da iPad’ini evindeki Wi-Fi üzerinden Samsung, LG, Roku, Google TV veya Android TV ile Fire TV için kumandaya çevirir. Uygulama App Store’da ücretsizdir, hesap ve reklam yoktur. Android’de ve Windows’ta da çalışır.',
    pasos=[
      'Mando TV’yi App Store’dan ücretsiz indir.',
      'iPhone’unu ve TV’yi aynı Wi-Fi ağına bağla.',
      'Mando TV’yi aç ve iOS yerel ağa erişim sorduğunda İzin Ver’e dokun. Uygulamanın TV’yi bulması için buna ihtiyacı var.',
      'Listede TV’ne dokun. TV soruyorsa (LG ve Samsung) soruyu onayla ya da TV’nin gösterdiği kodu gir (Google TV veya Fire TV).',
      'Tuşları, sesi ve klavyeyi kullan. Bağlandın.',
    ],
    extra=[
      ('Şu televizyonlarla çalışır', 'LG webOS, Samsung Tizen (2016 ve sonrası), Roku TV ve Roku oynatıcılar, Google TV ve Android TV ile Fire TV. Marka sayfaları: [Samsung](@samsung), [LG](@lg), [Roku](@roku) ve [Android TV](@android).'),
      ('Neden yerel ağı soruyor', 'iPhone, sen izin vermedikçe uygulamaların ev ağındaki cihazlara erişmesini engeller. TV listede görünmüyorsa Ayarlar > Mando TV’yi aç ve “Yerel Ağ”ı etkinleştir. Uygulama yalnızca ev ağının içinde TV’nle iletişim kurar.'),
      ('Neden üreticinin uygulaması değil de Mando TV', 'Her televizyon markasının kendi uygulaması var ve kendi kurulumunu ya da hesabını ister. Mando TV herkes için tek uygulamadır, hesapsız.'),
      ('iPhone’da ücretsiz ve Pro', 'Yön tuşları, OK, geri, ana ekran, ses, kanallar, rakam tuşları, klavye, uygulama açma, girişleri değiştirme ve açma ya da kapatma ücretsizdir, reklamsız ve aboneliksiz. Touchpad, sesli komutlar, favori uygulamalar, rutinler ve uyku zamanlayıcısı, aboneliksiz tek seferlik bir satın alım olan Mando TV Pro’nun parçasıdır. Pro’yu bir kez doğrudan uygulamada satın alırsın.'),
    ],
    marca=None,
    faq=[
      ('Mando TV iPhone’da ücretsiz mi?', 'İndirme ücretsiz ve reklamsız. Temel kumanda ücretsizdir, uygulama açma ve girişleri değiştirme de öyle. Touchpad, sesli komutlar ve rutinler gibi ekstralar, tek seferlik bir satın alım olan Mando TV Pro’ya dahildir.'),
      ('iPad’de çalışır mı?', 'Evet. Aynı uygulama iPhone’da ve iPad’de çalışır.'),
      ('iPhone için bir kumanda uygulaması Bluetooth ya da kızılötesi verici gerektirir mi?', 'iPhone’da hayır. iPhone’larda kızılötesi verici yoktur, bu yüzden kızılötesi kontrol orada kullanılamaz ve Bluetooth seçeneği yalnızca Android 9 ve sonrası içindir, iPhone için değil. iPhone’da Mando TV, akıllı TV’leri ve Apple TV’yi (beta) evindeki Wi-Fi üzerinden kontrol eder.'),
    ]),
  dict(clave='firetv', corto='Fire TV kumanda', fecha='2026-11-23',
    titulo='Telefon ve bilgisayar için Fire TV kumanda uygulaması',
    desc='Telefonda Fire TV kumandası: Fire TV Stick, Fire TV Cube veya Fire TV’li televizyonu 4 haneli PIN ile Wi-Fi üzerinden kontrol et. Amazon uygulaması gerekmez.',
    h1='Telefonun ya da bilgisayarın için Fire TV kumanda',
    intro='Fire TV kumandası kaybolduysa ya da pilleri bittiyse Mando TV, bir Fire TV Stick’i, Fire TV Cube’u ya da Fire TV’si yerleşik bir televizyonu Wi-Fi üzerinden kontrol eder. Eşleştirme 4 haneli bir PIN ile yapılır. Fire TV, Mando TV’de yenidir, bu yüzden önce uygulamayı güncelle.',
    pasos=[
      'Mando TV’yi App Store’dan, Microsoft Store’dan ya da Google Play’den en son sürüme güncelle.',
      'Fire TV’yi aç ve telefonunu aynı Wi-Fi ağına bağla.',
      'Mando TV’yi aç. Fire TV’n listede görünür. Üzerine dokun.',
      'TV’nin ekranında 4 haneli bir PIN çıkar. Onu Mando TV’ye gir. Bunu yalnızca bir kez yaparsın.',
      'Yön tuşlarını, OK, geri, ana ekran, oynatma tuşlarını ve arama için klavyeyi kullan.',
    ],
    extra=[
      ('Desteklenen Fire TV cihazları', 'Fire TV Stick, Fire TV Stick 4K, Fire TV Cube ve Fire TV’si yerleşik televizyonlar, örneğin Amazon Fire TV Edition televizyonlar ve bazı Hisense modelleri. Destek yenidir ve şimdiye kadar yalnızca birkaç gerçek cihazı test edebildik. Bir şey beklediğin gibi çalışmazsa modelini yardım sayfasından bize yaz.'),
      ('Fire TV’yi açma', 'Mando TV bir Fire TV’yi ağ üzerinden açmaz. TV’yi üzerindeki açma tuşuyla aç: takılı bir Fire TV Stick ya da Cube genellikle HDMI-CEC ile uyanır; Fire TV’si yerleşik bir televizyonda TV’nin kendisi Fire TV’dir. Sonra onu telefondan kontrol edersin.'),
      ('Fire TV’n görünmüyorsa', 'İki cihazın da aynı Wi-Fi’da olduğundan ve Fire TV’nin uyanık olduğundan emin ol. iPhone’da ayarlarda Mando TV için “Yerel Ağ”a izin ver. Bkz. [telefonun TV’yi bulamıyor](@not-found).'),
      ('Hiç kumandan yok mu?', 'Fire TV’nin PIN’i ekranda göstermesi gerekir, yani TV ve Fire TV açık olmalı ve görüntü vermeli. TV yanlış girişteyse TV’nin üzerindeki tuşlarla değiştir. Bkz. [Kumandasız girişi değiştirme](@hdmi).'),
      ('Ücretsiz ve Pro', 'Yön tuşları, OK, geri, ana ekran, ses, kanallar, rakamlar, klavye, uygulama açma, girişleri değiştirme ve açma/kapatma ücretsizdir, reklamsız ve aboneliksiz. Touchpad, sesli komutlar, favori uygulamalar, rutinler ve uyku zamanlayıcısı, aboneliksiz tek seferlik bir satın alım olan Mando TV Pro’nun parçasıdır.'),
    ],
    marca=None,
    faq=[
      ('Amazon Fire TV uygulamasına ihtiyacım var mı?', 'Hayır. Mando TV, Wi-Fi ağın üzerinden Fire TV’ye PIN ile bağlanır. Telefonda Amazon hesabına ihtiyacın yok.'),
      ('Fire TV’li televizyonlarla ve Fire TV Stick’lerle çalışır mı?', 'Evet, tam da bunun için geliştirildi. Destek yeni, uygulamayı güncel tut ve beklediğin gibi çalışmayan modelleri bize bildir.'),
      ('Neden PIN’e ihtiyacım var?', 'Fire TV, TV’nin karşısında olduğunu kanıtlamak için 4 haneli bir PIN gösterir. Ekranı görmeden hiç kimse eşleşemez.'),
    ]),
  dict(clave='firetv-lost', corto='Fire TV kumanda kayboldu', fecha='2026-11-23',
    titulo='Fire TV kumanda kayboldu mu? Telefonun böyle yardım eder',
    desc='Fire TV Stick kumandasını mı kaybettin? Telefonunla Wi-Fi üzerinden kontrol et, 4 haneli PIN ile eşleştir. Yeni Wi-Fi ve HDMI-CEC için ipuçları.',
    h1='Fire TV kumanda kayboldu: telefonunu böyle kullanırsın',
    intro='Fire TV Stick’in, Fire TV Cube’un ya da Fire TV’li akıllı TV’nin kumandası kaybolduysa ya da artık çalışmıyorsa Fire TV hâlâ Wi-Fi ağına bağlı olduğu sürece telefonun kontrolü devralır. Eşleştirme ekrandaki 4 haneli bir PIN ile yapılır, bunun için eski kumandaya hiç ihtiyacın olmaz.',
    pasos=[
      'TV’yi üzerindeki tuşla aç. Takılı bir Fire TV Stick ya da Cube genellikle birlikte uyanır; HDMI-CEC etkinse TV çoğu zaman kendiliğinden onun girişine geçer.',
      'TV başka bir girişi gösteriyorsa TV’nin giriş ya da kaynak tuşuyla değiştir. Bkz. [Kumandasız girişi değiştirme](@hdmi).',
      'Telefonunu Fire TV’yle aynı Wi-Fi ağına bağla.',
      'Mando TV’yi indir ve uygulamayı aç. Fire TV’n listede görünür. Üzerine dokun.',
      'TV 4 haneli bir PIN gösterir. Onu Mando TV’ye gir. Bunu yalnızca bir kez yaparsın.',
      'Telefonundaki yön tuşlarını, OK, geri, ana ekran, ses, oynatma tuşlarını ve klavyeyi kullan.',
    ],
    extra=[
      ('Önce TV’nin kumandasını dene (HDMI-CEC)', 'Birçok TV kumandası bir Fire TV Stick’i HDMI-CEC ile kontrol edebilir. Fire TV arayüzü görünüyorsa TV’nin kumandasındaki yön tuşlarına ve OK’e bas. Hiçbir şey olmazsa TV ayarlarında CEC’i etkinleştir (Samsung’da Anynet+, LG’de SIMPLINK, Sony’de BRAVIA Sync) ve Fire TV’de görüntü ayarlarında (“Görüntü ve Sesler”) HDMI-CEC cihaz kontrolünü etkinleştir.'),
      ('Wi-Fi’ı değiştirdiysen', 'Kumanda olmadan Fire TV’ye yeni Wi-Fi şifresini giremezsin, ama bir çıkış yolu var: ikinci bir telefonda eski Wi-Fi’ınla tamamen aynı ad ve şifreye sahip bir hotspot oluştur. Fire TV ona kendiliğinden bağlanır. Mando TV’li telefonu bu hotspot’a bağla, PIN ile eşleştir, ardından Fire TV’de Ayarlar > Ağ’a git ve yeni Wi-Fi’ını seç. Sonunda telefonunu da yeni Wi-Fi’a bağla.'),
      ('Yedek bir kumandayı eşleştirme', 'Çoğu yeni Fire TV kumandası, Fire TV’nin yakınında Ana ekran tuşunu yaklaşık 10 saniye basılı tutarak eşleşir. Olmazsa Ayarlar > Kontrolcüler ve Bluetooth Cihazlar > Amazon Fire TV Kumandaları > Yeni Kumanda Ekle’yi aç. Bu menüye Mando TV’li telefonundan da ulaşabilirsin.'),
      ('Televizyona yerleşik Fire TV', 'Insignia ve Toshiba’nın birçok modeli gibi Fire TV’si yerleşik televizyonlarda aynı adımlar işe yarar, çünkü televizyonun kendisi Fire TV’dir.'),
      ('Başlamadan önce', 'Fire TV desteği Mando TV’de yenidir. Önce uygulamayı güncelle. Modelin beklediğin gibi tepki vermezse [Yardım sayfası](@soporte) üzerinden bize yaz ve modeli belirt.'),
      ('Ücretsiz ve Pro', 'Kumandayı ücretsiz indirip kullanabilirsin, reklamsız ve aboneliksiz. Mando TV Pro, ekstralar için isteğe bağlı tek seferlik bir satın alımdır.'),
    ],
    marca=('firetv', 'Fire TV kumanda'),
    faq=[
      ('Kumanda olmadan bir Fire TV Stick’i telefonla kontrol edebilir miyim?', 'Evet, Fire TV açık ve Wi-Fi’ına bağlı olduğu sürece. Mando TV, TV’deki 4 haneli PIN ile eşleşir, yani eski kumandaya ihtiyacın yok.'),
      ('Fire TV yeni bir Wi-Fi’daysa çalışır mı?', 'Doğrudan değil, çünkü telefon ve Fire TV aynı ağda olmalı. Önce Fire TV’yi bu sayfadaki hotspot hilesiyle yeniden çevrimiçi yap.'),
      ('Amazon Fire TV uygulamasına ya da Amazon hesabına ihtiyacım var mı?', 'Hayır. Mando TV ev ağın üzerinden PIN ile bağlanır ve kendi hesabını gerektirmez.'),
    ]),
  dict(clave='turn-on', corto='Kumandasız TV açma', fecha='2026-11-23',
    titulo='Kumandasız TV açma (tüm markalar)',
    desc='Kumandasız TV açma: Samsung, LG, TCL, Hisense, Sony ve Vizio’da tuş nerede. Ayrıca HDMI-CEC ve telefon hileleri.',
    h1='Kumandasız TV nasıl açılır',
    intro='Neredeyse her televizyonda hâlâ fiziksel bir açma/kapama tuşu vardır. Sadece iyi saklanmıştır. İşte her markada nerede olduğu ve bir dahaki sefere aramayı ortadan kaldıracak iki yol: bir konsoldan ya da medya cihazından HDMI-CEC ve TV’yi telefonundan Wi-Fi ile açma.',
    pasos=[
      'Ekranın ortasının altına, marka logosunun hemen arkasına bak. Birçok televizyonda orada aşağıya bakan küçük tek bir tuş ya da joystick vardır.',
      'Orada değilse TV’nin arkasında alt köşelerin yakınını, sonra sol ve sağ kenarları elle ara.',
      'Tuşa bir kez bas. Tek tuşlu birçok televizyonda, açıkken kısa basış giriş ve ses için küçük bir menü açar, uzun basış kapatır.',
      'Hâlâ bir şey yok mu? Güç kablosunu iki ucundan da kontrol et ve başka bir priz dene. Bekleme ışığı yanmıyorsa TV elektrik almıyordur.',
      'TV açıldığında bir daha tuşa ihtiyacın olmayacak şekilde ayarla: HDMI-CEC’i ve ağ üzerinden açmayı etkinleştir, ikisi de aşağıda anlatılıyor.',
    ],
    extra=[
      ('Açma/kapama tuşu markaya göre nerede', 'Samsung: ekranın ortasının altında ya da arkada alt köşelerden birinde bir kontrol tuşu veya joystick. LG: çoğu modelde LG logosunun altında bir joystick tuşu. TCL ve Hisense: genellikle ekranın ortasının altında ya da arkada bir alt köşenin yakınında küçük bir tuş. Sony: arkada ya da bir yan kenarda, altta kenara yakın. Vizio: arkada, sol altta ya da sağ altta, veya yan tarafta. Konumlar modele göre değişir. Bulamazsan arkadaki etiketteki model numarasıyla kullanım kılavuzunu ara.'),
      ('TV’yi bir konsoldan ya da medya cihazından açma (HDMI-CEC)', 'HDMI-CEC etkinken bir PlayStation, Xbox, Roku oynatıcı, Fire TV Stick ya da Chromecast’i açmak TV’yi de açar ve doğru girişe geçer. Her marka ayara farklı bir ad verir: Samsung’da Anynet+, LG’de SIMPLINK, Sony’de BRAVIA Sync ve diğerlerinin çoğunda CEC. Daha fazlası için [Kumandasız TV’yi açma ve konsolun HDMI girişine geçme](@console).'),
      ('TV’yi telefonundan açma', 'Bunu bir kez onaylarsan akıllı TV’ler Wi-Fi ile uyandırılabilir ve Mando TV onları telefonundan açar. Samsung’da Ayarlar > Genel > Ağ > Uzman Ayarları altında “Mobil Cihazla Aç”ı etkinleştir. LG’de “Mobil cihazla TV’yi aç”ı etkinleştir ([adım adım](@lg-on)). Roku TV’de Ayarlar > Sistem > Güç altında “TV hızlı başlatma”yı etkinleştir. Google TV ve Android TV’de modelinde varsa Wake on LAN ya da “Ağ üzerinden aç”ı ara. Bunu TV açıkken bir kez yaparsın.'),
      ('Hiç tuş bulamıyorsan', 'Bazı yeni televizyonlar tek tuşu o kadar iyi saklar ki hiç yokmuş gibi görünür. Ekranın altında küçük bir kabartı ya da ışık sensörü bölgesi ara: tuş çoğu zaman hemen yanındadır. Wi-Fi ile Mando TV’nin çalışması için TV’nin bir kez açılmış ve bağlanmış olması gerekir. İstisna kızılötesidir: kızılötesi vericisi olan bir Android telefonda, telefonu TV’ye doğrulttuğun sürece Mando TV hiç kurulmamış bir TV’yi açabilir. Kızılötesi yenidir ve uygulamadaki kod listesinde bulunan markalarla çalışır.'),
      ('Ücretsiz ve Pro', 'Kumandayı ücretsiz indirip kullanabilirsin, reklamsız ve aboneliksiz. Mando TV Pro, ekstralar için isteğe bağlı tek seferlik bir satın alımdır.'),
    ],
    marca=None,
    faq=[
      ('TV’yi hiç kurmadıysam telefonla açabilir miyim?', 'Wi-Fi ile değil. Kapalı bir TV, ağ üzerinden açma önceden etkinleştirilmediyse ağdan uyanmaz. İlk seferde TV’deki tuşu kullan. İstisna, kızılötesi vericisi olan bir Android telefondur: marka kod listesinde varsa ya da “Başka marka veya bilmiyorum”u seçersen Mando TV kurulum olmadan bir TV’yi kızılötesiyle açabilir.'),
      ('Kumandasız bir Samsung TV’yi nasıl açarım?', 'Ekranın ortasının altındaki ya da arkada bir alt köşedeki kontrol tuşuna bas. Sonra telefonun bir dahaki sefere açabilsin diye “Mobil Cihazla Aç”ı etkinleştir.'),
      ('Kumandasız bir Roku TV’yi nasıl açarım?', 'TV’deki tuşu kullan; genellikle ortanın altında ya da arkadadır. Sonra Mando TV’nin onu telefonundan açabilmesi için Ayarlar > Sistem > Güç altında “TV hızlı başlatma”yı etkinleştir.'),
      ('Konsolu açtığımda TV neden kendiliğinden açılıyor?', 'Bu HDMI-CEC. Pratiktir ve tercih edersen TV ayarlarından kapatabilirsin.'),
    ]),
  dict(clave='sony', corto='Sony kumanda', fecha='2026-11-23',
    titulo='Telefon ve bilgisayar için Sony kumanda uygulaması',
    desc='Mando TV, Google TV veya Android TV’li Sony Bravia televizyonları Wi-Fi ile kontrol eder. Android’siz 2013-2015 modelleri için beta destek.',
    h1='Sony TV’ni telefonla nasıl kontrol edersin',
    intro='Yeni Sony Bravia akıllı TV’ler Google TV kullanır, 2015’ten itibaren eski modeller Android TV. Mando TV ikisini de Wi-Fi’ın üzerinden iPhone’dan, Android telefondan ya da Windows bilgisayardan kontrol eder. Uygulama, kaybolduğunda ya da pilleri bittiğinde orijinal kumandanın yerini tutar.',
    pasos=[
      'Sony TV’nin Google TV ya da Android TV ana ekranını gösterip göstermediğine bak. Bu, 2015’ten itibaren üretilen çoğu Sony Bravia akıllı TV için geçerlidir.',
      'Telefonunu ve TV’yi aynı Wi-Fi ağına bağla.',
      'Mando TV’yi aç ve listede Sony TV’ne dokun.',
      'TV’nin ekranda gösterdiği 6 karakterli kodu gir (yalnızca ilk seferde). Bunun için kumandaya ihtiyacın yok.',
      'Yön tuşlarını, OK, geri, ana ekran, ses ve klavyeyi kullan.',
    ],
    extra=[
      ('Sony TV’yi telefondan açma', 'Google TV veya Android TV’li Sony modelleri, “Remote start” etkinse ağ üzerinden uyandırılabilir. Seçeneği genellikle Ayarlar > Ağ ve İnternet > Remote start altında bulursun (yol modele göre biraz değişebilir). Sonra TV kapalıyken Mando TV’de TV’ye dokun, uygulama onu açar.'),
      ('Bir Sony’de açma/kapama tuşu nerede', 'Çoğu Bravia televizyonda arkada, sol ya da sağ alt köşenin yakınında ya da bir yan kenardadır. Kısa bir basış TV’yi açar. Daha fazlası için [Kumandasız TV açma](@turn-on) sayfasına bak.'),
      ('Eski Sony televizyonlar', 'Android kullanmayan 2013-2015 arası Sony Bravia televizyonlar Mando TV’de beta olarak desteklenir. Bu yenidir ve henüz pürüzleri olabilir. TV, uygulamaya girmen gereken 4 haneli bir PIN gösterir. Google TV ya da Android TV’si olmayan diğer Sony televizyonlar şu an desteklenmiyor.'),
      ('Ücretsiz ve Pro', 'Kumandayı ücretsiz indirip kullanabilirsin, reklamsız ve aboneliksiz. Mando TV Pro, ekstralar için isteğe bağlı tek seferlik bir satın alımdır.'),
    ],
    marca='android',
    faq=[
      ('Mando TV Sony Bravia televizyonlarla çalışır mı?', 'Evet, Google TV ya da Android TV kullanan Sony televizyonlarla. Bu, 2015’ten itibaren üretilen çoğu Sony akıllı TV’yi kapsar.'),
      ('Sony uygulamasına ya da Google hesabına ihtiyacım var mı?', 'Hayır. Mando TV, TV ekranındaki kodla eşleşir ve hesap istemez.'),
      ('Android’siz eski Sony Bravia televizyonlarla çalışır mı?', 'Evet, beta olarak, Android’siz 2013-2015 arası Bravia modellerinde. Eşleştirme, TV’de gösterilen 4 haneli bir PIN ile yapılır.'),
      ('Sony TV’mde telefondan yazabilir miyim?', 'Evet. Telefon klavyesi ücretsizdir ve TV’nin arama kutusuna ve diğer metin kutularına yazar. YouTube için Mando TV’de bir YouTube Klavyesi de var: ne izleyeceğini yaz ya da söyle, YouTube TV’de sonuçlarla açılır. Netflix yalnızca kendi ekran klavyesini kabul eder, orada oklar ve OK kullan.'),
    ]),
  dict(clave='tcl', corto='TCL kumanda', fecha='2026-11-23',
    titulo='Telefon ve bilgisayar için TCL kumanda uygulaması',
    desc='TCL kumandayı mı kaybettin? Çoğu TCL TV, Roku TV ya da Google TV kullanır. Mando TV ikisini de Wi-Fi ile, hesapsız ve reklamsız kontrol eder.',
    h1='TCL TV’ni telefonla nasıl kontrol edersin',
    intro='TCL televizyonu yapar, ama yazılım Roku TV ya da Google TV’dir (eski modellerde Android TV). Mando TV iki sistemi de kontrol eder ve Wi-Fi üzerinden TCL televizyonun için kumanda olarak çalışır. Ücretsiz, hesap ve reklam yok.',
    pasos=[
      'TCL’nin hangi sistemi kullandığını öğren. Ana ekran kanal karolarından oluşan basit bir ızgara gösteriyorsa Roku TV’dir. Öneri dolu sıralarla Google TV ya da Android TV gibi görünüyorsa Google TV’dir.',
      'Telefonunu ve TCL TV’yi aynı Wi-Fi ağına bağla.',
      'Mando TV’yi aç. TCL kendiliğinden listede görünür. Üzerine dokun.',
      'Roku TV’li bir TCL’de başka bir şey gerekmez. Google TV’li bir TCL’de TV’nin ekranda gösterdiği 6 karakterli kodu gir (yalnızca ilk seferde).',
      'Yön tuşlarını, OK, geri, ana ekran, ses ve klavyeyi kullan. Ağ üzerinden açmayı etkinleştirdiysen TV’yi uygulamadan aç (aşağıya bak).',
    ],
    extra=[
      ('TCL TV’yi telefondan açma', 'TCL Roku TV’de Ayarlar > Sistem > Güç altında “TV hızlı başlatma”yı etkinleştir. TCL Google TV’de ağ ya da güç ayarlarında Wake on LAN, “Ağ üzerinden aç” ya da uzaktan başlatma seçeneğini ara. Bazı modeller bunu sunmaz. Bu durumda TV’yi fiziksel açma/kapama tuşuyla aç; genellikle alt ortada ya da arkadadır.'),
      ('TCL’n görünmüyorsa', 'Telefonun ve TV’nin aynı Wi-Fi’da olduğunu kontrol et. Ayrı 2,4 GHz ve 5 GHz ağlı router’lar cihazları birbirinden gizleyebilir. iPhone’da ayarlarda Mando TV için “Yerel Ağ”a izin ver. TV’yi IP adresini girerek de ekleyebilirsin. [Telefonun TV’yi bulamıyor](@not-found) sayfasını oku.'),
      ('TCL’n hakkında daha fazlası', 'Roku TV’li TCL için [Roku kumanda uygulaması](@roku), Google TV ya da Android TV’li TCL için [Android TV kumanda uygulaması](@android) sayfasına bak.'),
      ('Ücretsiz ve Pro', 'Yön tuşları, OK, geri, ana ekran, ses, kanallar, rakamlar, klavye, uygulama açma, girişleri değiştirme ve açma/kapatma ücretsizdir, reklamsız ve aboneliksiz. Touchpad, sesli komutlar, favori uygulamalar, rutinler ve uyku zamanlayıcısı, aboneliksiz tek seferlik bir satın alım olan Mando TV Pro’nun parçasıdır.'),
    ],
    marca=None,
    faq=[
      ('Mando TV her TCL televizyonla çalışır mı?', 'Roku TV, Google TV ya da Android TV’li TCL televizyonlarla, yani çoğu TCL akıllı TV ile çalışır. Akıllı olmayan bir TCL Wi-Fi ile kontrol edilemez.'),
      ('TCL uygulamasına ya da TCL hesabına ihtiyacım var mı?', 'Hayır. Mando TV doğrudan evindeki Wi-Fi üzerinden bağlanır ve hesap gerektirmez.'),
      ('TCL’m kod soruyor. Nerede?', 'Google TV ve Android TV’li TCL modelleri ekranda 6 karakterli bir kod gösterir. Onu Mando TV’ye aynen gir. Roku TV’li bir TCL kod sormaz.'),
    ]),
  dict(clave='hisense', corto='Hisense kumanda', fecha='2026-11-23',
    titulo='Hisense kumanda uygulaması: telefonda neler çalışır',
    desc='Mando TV ile Hisense kumanda: VIDAA, Roku TV, Google TV ve Fire TV için Wi-Fi ile kontrol. Nelerin çalıştığına dair dürüst özet.',
    h1='Hisense kumanda uygulaması: neler çalışır, neler çalışmaz',
    intro='Hisense televizyonlar içeriden hepsi aynı değildir. Modele göre Hisense’in kendi VIDAA sistemini, Roku TV’yi, Google TV’yi ya da Fire TV’yi kullanırlar. Mando TV, bazı yeni VIDAA modellerindeki bir istisna dışında Hisense için dört sistemde de kumanda olarak çalışır. İşte hangi sisteme sahip olduğunu nasıl anlayacağın ve seni neyin beklediği.',
    pasos=[
      'Hisense’inin hangi sistemi kullandığını kontrol et. VIDAA, Hisense’in kendi arayüzüdür. Roku TV kanal karolarından oluşan bir ızgara gösterir. Google TV öneri sıraları gösterir. Fire TV, Amazon sıralarıyla Fire TV ana ekranını gösterir.',
      'Telefonunu ve Hisense TV’yi aynı Wi-Fi ağına bağla.',
      'Mando TV’yi aç. TV listede kendiliğinden görünür. Üzerine dokun.',
      'VIDAA ve Fire TV modelleri dört haneli bir PIN gösterebilir; Google TV altı karakterli bir kod gösterir. Onu uygulamaya gir. Roku TV hiçbir şey sormaz. Bunu yalnızca bir kez yaparsın.',
      'Telefonundan yön tuşlarını, OK, geri, ana ekran, ses ve klavyeyi kullan.',
    ],
    extra=[
      ('Roku TV ya da Google TV’li Hisense', 'Bunlar diğer tüm Roku ya da Google TV televizyonlar gibi tam çalışır. Ayrıntılar [Roku kumanda uygulaması](@roku) ve [Android TV kumanda uygulaması](@android) sayfalarında.'),
      ('Fire TV’li Hisense', 'Fire TV desteği Mando TV’de yenidir. Uygulamayı mağazandan en son sürüme güncelle. PIN ile eşleştirmenin nasıl çalıştığı [Fire TV kumanda uygulaması](@firetv) sayfasında. Bir şey beklediğin gibi çalışmazsa yardım sayfasından modelini belirterek bize yaz.'),
      ('VIDAA’lı Hisense', 'Çoğu VIDAA modeli çalışır: tuşlar, ses, klavye, uygulamalar ve girişler. Bazı yeni VIDAA modelleri yalnızca resmî Hisense uygulamasını kabul eder. Mando TV bunu bağlanırken fark eder ve sessizce başarısız olmak yerine sana açıkça söyler. Bu durumda modelin için Hisense uygulaması, TV’deki tuşlar ya da orijinal kumanda doğru yoldur.'),
      ('Hisense’i telefondan açma', 'Hisense Roku TV’de Ayarlar > Sistem > Güç altında “TV hızlı başlatma”yı etkinleştir. Google TV’de Wake on LAN ya da “Ağ üzerinden aç” seçeneğini ara. Yoksa TV’deki açma/kapama tuşunu kullan.'),
      ('Ücretsiz ve Pro', 'Yön tuşları, OK, geri, ana ekran, ses, kanallar, rakam tuşları, klavye, uygulama açma, girişleri değiştirme ve açma ya da kapatma ücretsizdir, reklamsız ve aboneliksiz. Touchpad, sesli komutlar, favori uygulamalar, rutinler ve uyku zamanlayıcısı, aboneliksiz tek seferlik bir satın alım olan Mando TV Pro’nun parçasıdır.'),
    ],
    marca=None,
    faq=[
      ('Mando TV Hisense VIDAA ile çalışır mı?', 'Evet, çoğu VIDAA modeliyle. Bazı yeni modeller yalnızca resmî Hisense uygulamasını kabul eder; Mando TV bunu fark eder ve sana söyler. Roku TV, Google TV ya da Fire TV’li Hisense televizyonlar da desteklenir.'),
      ('Hisense’imin Roku TV mi, Google TV mi, Fire TV mi olduğunu nasıl anlarım?', 'Ana ekrana bak. Roku TV’de basit bir karo ızgarası ve açılışta Roku logosu vardır. Google TV’de öneri sıraları vardır. Fire TV’de Amazon Fire TV ana ekranı vardır. Ayarlar > Hakkında altındaki model adı da bilgi verir.'),
      ('Hisense ya da Google hesabına ihtiyacım var mı?', 'Hayır. Mando TV doğrudan evindeki Wi-Fi üzerinden bağlanır ve kendi hesabı yoktur.'),
    ]),
  dict(clave='philips', corto='Philips kumanda', fecha='2026-11-23',
    titulo='Philips kumanda uygulaması: Roku TV, Google TV, Android TV',
    desc='Mando TV, Roku TV, Google TV ya da Android TV’li Philips televizyonları telefondan veya bilgisayardan Wi-Fi ile kontrol eder. Titan OS desteklenmez.',
    h1='Philips TV’ni telefonla kontrol et',
    intro='Philips televizyonlar ülkeye ve üretim yılına göre farklı sistemler kullanır: ABD’de Roku TV, birçok ülkede Google TV ya da Android TV ve bazı yeni Avrupa modellerinde Titan OS. Mando TV, Roku TV, Google TV ve Android TV’li modelleri Wi-Fi ile kontrol eder.',
    pasos=[
      'Ana ekrana bak. Roku TV bir karo ızgarası gösterir. Google TV ve Android TV, Google’ın önerilerinden oluşan sıralar gösterir. Titan OS’un kendi ana ekranı vardır.',
      'Telefonunu ve TV’yi aynı Wi-Fi ağına bağla.',
      'Mando TV’yi aç ve listede Philips TV’ne dokun.',
      'Roku TV hiçbir şey sormaz. Google TV ve Android TV 6 karakterli bir kod gösterir: onu uygulamaya bir kez gir.',
      'Yön tuşlarını, OK, geri, ana ekran, ses ve klavyeyi kullan.',
    ],
    extra=[
      ('Philips Roku TV', 'Her Roku televizyon gibi çalışır. Telefondan açmak için Ayarlar > Sistem > Güç altında “TV hızlı başlatma”yı etkinleştir. Daha fazlası [Roku kumanda uygulaması](@roku) sayfasında.'),
      ('Google TV ya da Android TV’li Philips', 'Birçok Ambilight modelini kapsar. Ekrandaki kodla eşleşirler. Telefondan açmak için ağ ya da güç ayarlarında Wake on LAN ya da “Ağ üzerinden aç” seçeneğini ara. Bazı modellerde bu seçenek yoktur. Daha fazlası [Android TV kumanda uygulaması](@android) sayfasında.'),
      ('Android’siz eski Philips televizyonlar', 'Android kullanmayan 2011-2015 arası Philips televizyonlar Mando TV’de betada desteklenir. Yenidir ve eşleştirme kodu gerektirmez.'),
      ('Titan OS’li Philips', 'Titan OS, Mando TV’nin bugün kontrol etmediği farklı bir sistemdir ve bunu açıkça söylemeyi tercih ederiz. Android’siz yeni Philips modelleri de kapsanmıyor.'),
      ('Ücretsiz ve Pro', 'Kumandayı ücretsiz indirip kullanabilirsin, reklamsız ve aboneliksiz. Mando TV Pro, ekstralar için isteğe bağlı tek seferlik bir satın alımdır.'),
    ],
    marca=None,
    faq=[
      ('Mando TV Philips televizyonlarla çalışır mı?', 'Roku TV, Google TV ya da Android TV kullanan Philips televizyonlarla evet, ayrıca betada Android’siz 2011-2015 arası Philips televizyonlarla. Titan OS’li modeller desteklenmez.'),
      ('Mando TV Ambilight’ı kontrol eder mi?', 'Mando TV bir kumandadır: tuşları gönderir, böylece yön tuşları ve OK ile Ambilight ayarlarına ulaşabilirsin. Ayrı Ambilight kontrolleri yoktur.'),
      ('Philips ya da Google hesabına ihtiyacım var mı?', 'Hayır. Mando TV evindeki Wi-Fi üzerinden bağlanır ve hesap gerektirmez.'),
    ]),
]
OTRAS_GUIAS += [
  ('no-sub', 'Abonelik ve reklam olmadan bir kumanda uygulaması'),
  ('roku-app-alt', 'Roku uygulaması alternatifi: tüm televizyonlar için tek uygulama'),
  ('lg-thinq', 'LG TV’n için LG ThinQ uygulaması alternatifi'),
  ('smartthings', 'Samsung TV’ler için SmartThings alternatifi'),
  ('googletv-alt', 'Telefonda Google TV kumanda alternatifi'),
  ('windows', 'Windows bilgisayar için kumanda uygulaması'),
  ('iphone', 'iPhone kumanda uygulaması: tüm televizyonlar için tek uygulama'),
  ('firetv', 'Telefonun ya da bilgisayarın için Fire TV kumanda'),
  ('firetv-lost', 'Fire TV kumanda kayboldu: telefonunu böyle kullanırsın'),
  ('turn-on', 'Kumandasız TV nasıl açılır'),
  ('sony', 'Sony TV’ni telefonla nasıl kontrol edersin'),
  ('tcl', 'TCL TV’ni telefonla nasıl kontrol edersin'),
  ('hisense', 'Hisense kumanda uygulaması: neler çalışır, neler çalışmaz'),
  ('philips', 'Philips TV’ni telefonla kontrol et'),
]
# <<< guías traídas del inglés
