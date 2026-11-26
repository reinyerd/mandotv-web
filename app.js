// Mando TV: vitrina del inicio. Elegir marca de TV (cambia el color de toda la página), elegir equipo (el botón
// Descargar va a la tienda correcta), tema del teléfono dibujado y teclas que responden al toque.
(function () {
  document.documentElement.classList.remove('sin-js');

  var marcas = {
    samsung: { color: '#3d7bff', color2: '#43d3ff', tv: 'TV Samsung', nota: 'Samsung con Tizen: aceptas una vez en el televisor y listo.' },
    lg: { color: '#e0457b', color2: '#ff9a62', tv: 'TV LG', nota: 'LG con webOS: se conecta por WiFi y también puede encenderlo.' },
    roku: { color: '#a77bff', color2: '#ff7be5', tv: 'Roku', nota: 'Roku: televisores y reproductores, sin emparejar nada.' },
    android: { color: '#2fbf8f', color2: '#c4f04f', tv: 'Google TV', nota: 'Google TV y Android TV (Sony, TCL, Philips, Xiaomi y más): escribes el código que muestra la pantalla.' }
  };
  // Textos en español (/es/ y páginas sin idioma propio). Las páginas en otros idiomas (/, /de/, /fr/, /pt/, /it/) toman los suyos de
  // TEXTOS según <html lang>.
  var ES = {
    mac: 'Descargar gratis para Mac', ipad: 'Descargar gratis para iPad', iphone: 'Descargar gratis para iPhone', windows: 'Descargar gratis para Windows',
    android: 'Descargar gratis para Android', boton: 'Descargar gratis',
    notaAndroid: 'En Android es una prueba anticipada en Google Play: son dos pasos.',
    barra: 'Descargar', claro: 'Claro', oscuro: 'Oscuro', pausar: 'Pausar las marcas', reanudar: 'Reanudar las marcas',
    frases: ['documentales de volcanes', 'música para cocinar', 'partido de fútbol en vivo', 'película de Navidad']
  };
  var TEXTOS = {
    en: {
      marcas: {
        lg: ['LG TV', 'LG with webOS: it connects over Wi-Fi and can also turn the TV on.'],
        samsung: ['Samsung TV', 'Samsung with Tizen: you accept once on the TV and you are set.'],
        roku: ['Roku', 'Roku: TVs and players, nothing to pair.'],
        android: ['Google TV', 'Google TV and Android TV (Sony, TCL, Philips, Xiaomi and more): you type the code the screen shows.']
      },
      mac: 'Download free for Mac', ipad: 'Download free for iPad', iphone: 'Download free for iPhone', windows: 'Download free for Windows',
      android: 'Download free for Android', boton: 'Download free',
      notaAndroid: "On Android it's early access on Google Play: two quick steps.",
      barra: 'Download', claro: 'Light', oscuro: 'Dark', pausar: 'Pause the brands', reanudar: 'Play the brands',
      frases: ['volcano documentaries', 'cooking music', 'live soccer game', 'Christmas movie']
    },
    de: {
      marcas: {
        lg: ['LG Fernseher', 'LG mit webOS: Die Verbindung läuft über WLAN und er lässt sich auch einschalten.'],
        samsung: ['Samsung Fernseher', 'Samsung mit Tizen: Du bestätigst einmal am Fernseher und bist fertig.'],
        roku: ['Roku', 'Roku: Fernseher und Player, ohne etwas zu koppeln.'],
        android: ['Google TV', 'Google TV und Android TV (Sony, TCL, Philips, Xiaomi und mehr): Du gibst den Code ein, den der Bildschirm zeigt.']
      },
      mac: 'Kostenlos für Mac laden', ipad: 'Kostenlos für iPad laden', iphone: 'Kostenlos für iPhone laden', windows: 'Kostenlos für Windows laden',
      android: 'Kostenlos für Android laden', boton: 'Kostenlos laden',
      notaAndroid: 'Auf Android gibt es einen frühen Zugang über Google Play: zwei Schritte.',
      barra: 'Laden', claro: 'Hell', oscuro: 'Dunkel', pausar: 'Marken anhalten', reanudar: 'Marken fortsetzen',
      frases: ['Dokumentationen über Vulkane', 'Musik zum Kochen', 'Fußballspiel live', 'Weihnachtsfilm']
    },
    fr: {
      marcas: {
        lg: ['TV LG', 'LG avec webOS : la connexion passe par le Wi-Fi et elle peut aussi allumer la TV.'],
        samsung: ['TV Samsung', "Samsung avec Tizen : vous acceptez une fois sur la TV et c'est terminé."],
        roku: ['Roku', 'Roku : téléviseurs et lecteurs, rien à associer.'],
        android: ['Google TV', "Google TV et Android TV (Sony, TCL, Philips, Xiaomi et plus) : vous saisissez le code affiché à l'écran."]
      },
      mac: 'Télécharger gratuitement pour Mac', ipad: 'Télécharger gratuitement pour iPad', iphone: 'Télécharger gratuitement pour iPhone', windows: 'Télécharger gratuitement pour Windows',
      android: 'Télécharger gratuitement pour Android', boton: 'Télécharger gratuitement',
      notaAndroid: "Sur Android, c'est un accès anticipé sur Google Play : deux étapes.",
      barra: 'Télécharger', claro: 'Clair', oscuro: 'Sombre', pausar: 'Mettre les marques en pause', reanudar: 'Relancer les marques',
      frases: ['documentaires sur les volcans', 'musique pour cuisiner', 'match de foot en direct', 'film de Noël']
    },
    pt: {
      marcas: {
        lg: ['TV LG', 'LG com webOS: conecta pelo Wi-Fi e também pode ligar a TV.'],
        samsung: ['TV Samsung', 'Samsung com Tizen: você aceita uma vez na TV e pronto.'],
        roku: ['Roku', 'Roku: TVs e aparelhos, sem precisar parear nada.'],
        android: ['Google TV', 'Google TV e Android TV (Sony, TCL, Philips, Xiaomi e outras): você digita o código que aparece na tela.']
      },
      mac: 'Baixar grátis para Mac', ipad: 'Baixar grátis para iPad', iphone: 'Baixar grátis para iPhone', windows: 'Baixar grátis para Windows',
      android: 'Baixar grátis para Android', boton: 'Baixar grátis',
      notaAndroid: 'No Android é um teste antecipado no Google Play: são dois passos.',
      barra: 'Baixar', claro: 'Claro', oscuro: 'Escuro', pausar: 'Pausar as marcas', reanudar: 'Retomar as marcas',
      frases: ['documentários sobre vulcões', 'música para cozinhar', 'jogo de futebol ao vivo', 'filme de Natal']
    },
    it: {
      marcas: {
        lg: ['TV LG', 'LG con webOS: si collega in Wi-Fi e può anche accendere la TV.'],
        samsung: ['TV Samsung', 'Samsung con Tizen: accetti una volta sulla TV e hai finito.'],
        roku: ['Roku', 'Roku: televisori e dispositivi, senza nulla da associare.'],
        android: ['Google TV', 'Google TV e Android TV (Sony, TCL, Philips, Xiaomi e altre): inserisci il codice che compare sullo schermo.']
      },
      mac: 'Scarica gratis per Mac', ipad: 'Scarica gratis per iPad', iphone: 'Scarica gratis per iPhone', windows: 'Scarica gratis per Windows',
      android: 'Scarica gratis per Android', boton: 'Scarica gratis',
      notaAndroid: 'Su Android è un accesso anticipato su Google Play: bastano due passaggi.',
      barra: 'Scarica', claro: 'Chiaro', oscuro: 'Scuro', pausar: 'Metti in pausa le marche', reanudar: 'Riprendi le marche',
      frases: ['documentari sui vulcani', 'musica per cucinare', 'partita di calcio in diretta', 'film di Natale']
    },
    id: {
      marcas: {
        lg: ['TV LG', 'LG dengan webOS: terhubung lewat Wi-Fi dan bisa menyalakan TV juga.'],
        samsung: ['TV Samsung', 'Samsung dengan Tizen: cukup setujui sekali di TV, lalu siap dipakai.'],
        roku: ['Roku', 'Roku: TV dan perangkat, tanpa perlu dipasangkan.'],
        android: ['Google TV', 'Google TV dan Android TV (Sony, TCL, Philips, Xiaomi, dan lainnya): ketik kode yang tampil di layar.']
      },
      mac: 'Unduh gratis untuk Mac', ipad: 'Unduh gratis untuk iPad', iphone: 'Unduh gratis untuk iPhone', windows: 'Unduh gratis untuk Windows',
      android: 'Unduh gratis untuk Android', boton: 'Unduh gratis',
      notaAndroid: 'Di Android ini akses awal di Google Play: cukup dua langkah.',
      barra: 'Unduh', claro: 'Terang', oscuro: 'Gelap', pausar: 'Jeda merek', reanudar: 'Putar merek',
      frases: ['dokumenter gunung berapi', 'musik untuk memasak', 'pertandingan sepak bola langsung', 'film keluarga']
    },
    ms: {
      marcas: {
        lg: ['TV LG', 'LG dengan webOS: bersambung melalui Wi-Fi dan boleh menghidupkan TV juga.'],
        samsung: ['TV Samsung', 'Samsung dengan Tizen: anda setuju sekali pada TV, dan sedia digunakan.'],
        roku: ['Roku', 'Roku: TV dan peranti, tanpa perlu dipasangkan.'],
        android: ['Google TV', 'Google TV dan Android TV (Sony, TCL, Philips, Xiaomi dan banyak lagi): anda menaip kod yang dipaparkan pada skrin.']
      },
      mac: 'Muat turun percuma untuk Mac', ipad: 'Muat turun percuma untuk iPad', iphone: 'Muat turun percuma untuk iPhone', windows: 'Muat turun percuma untuk Windows',
      android: 'Muat turun percuma untuk Android', boton: 'Muat turun percuma',
      notaAndroid: 'Di Android, ini akses awal di Google Play: dua langkah mudah.',
      barra: 'Muat turun', claro: 'Cerah', oscuro: 'Gelap', pausar: 'Jeda jenama', reanudar: 'Main jenama',
      frases: ['dokumentari gunung berapi', 'muzik untuk memasak', 'perlawanan bola sepak secara langsung', 'filem keluarga']
    },
    cs: {
      marcas: {
        lg: ['TV LG', 'LG s webOS: připojí se přes Wi-Fi a umí televizi i zapnout.'],
        samsung: ['TV Samsung', 'Samsung s Tizenem: na televizi jednou potvrdíte a máte hotovo.'],
        roku: ['Roku', 'Roku: televizory a přehrávače, nic se nepáruje.'],
        android: ['Google TV', 'Google TV a Android TV (Sony, TCL, Philips, Xiaomi a další): opíšete kód, který se zobrazí na obrazovce.']
      },
      mac: 'Stáhnout zdarma pro Mac', ipad: 'Stáhnout zdarma pro iPad', iphone: 'Stáhnout zdarma pro iPhone', windows: 'Stáhnout zdarma pro Windows',
      android: 'Stáhnout zdarma pro Android', boton: 'Stáhnout zdarma',
      notaAndroid: 'Na Androidu jde o předběžný přístup v Google Play: stačí dva kroky.',
      barra: 'Stáhnout', claro: 'Světlý', oscuro: 'Tmavý', pausar: 'Pozastavit značky', reanudar: 'Spustit značky',
      frases: ['dokumenty o sopkách', 'hudba na vaření', 'fotbalový zápas živě', 'vánoční film']
    },
    da: {
      marcas: {
        lg: ['LG-tv', "LG med webOS: den forbinder via Wi-Fi og kan også tænde for tv'et."],
        samsung: ['Samsung-tv', "Samsung med Tizen: du godkender én gang på tv'et, og så er du klar."],
        roku: ['Roku', 'Roku: tv og afspillere, uden noget at parre.'],
        android: ['Google TV', 'Google TV og Android TV (Sony, TCL, Philips, Xiaomi og flere): du skriver koden, som skærmen viser.']
      },
      mac: 'Hent gratis til Mac', ipad: 'Hent gratis til iPad', iphone: 'Hent gratis til iPhone', windows: 'Hent gratis til Windows',
      android: 'Hent gratis til Android', boton: 'Hent gratis',
      notaAndroid: 'På Android er det tidlig adgang på Google Play: to hurtige trin.',
      barra: 'Hent', claro: 'Lys', oscuro: 'Mørk', pausar: 'Sæt mærkerne på pause', reanudar: 'Afspil mærkerne',
      frases: ['dokumentarer om vulkaner', 'musik til madlavning', 'live fodboldkamp', 'julefilm']
    },
    hu: {
      marcas: {
        lg: ['LG tévé', 'LG webOS-szel: Wi-Fi-n csatlakozik, és a tévét be is tudja kapcsolni.'],
        samsung: ['Samsung tévé', 'Samsung Tizennel: egyszer elfogadod a tévén, és kész.'],
        roku: ['Roku', 'Roku: tévék és lejátszók, párosítani sem kell semmit.'],
        android: ['Google TV', 'Google TV és Android TV (Sony, TCL, Philips, Xiaomi és mások): beírod a képernyőn látható kódot.']
      },
      mac: 'Ingyenes letöltés Machez', ipad: 'Ingyenes letöltés iPadhez', iphone: 'Ingyenes letöltés iPhone-hoz', windows: 'Ingyenes letöltés Windowshoz',
      android: 'Ingyenes letöltés Androidhoz', boton: 'Ingyenes letöltés',
      notaAndroid: 'Androidon ez korai hozzáférés a Google Playen: két gyors lépés.',
      barra: 'Letöltés', claro: 'Világos', oscuro: 'Sötét', pausar: 'Márkák szüneteltetése', reanudar: 'Márkák lejátszása',
      frases: ['dokumentumfilmek vulkánokról', 'zene főzéshez', 'élő focimeccs', 'karácsonyi film']
    },
    nl: {
      marcas: {
        lg: ['LG-tv', 'LG met webOS: verbindt via wifi en kan de tv ook aanzetten.'],
        samsung: ['Samsung-tv', 'Samsung met Tizen: je bevestigt één keer op de tv en klaar.'],
        roku: ['Roku', "Roku: tv's en spelers, niets om te koppelen."],
        android: ['Google TV', 'Google TV en Android TV (Sony, TCL, Philips, Xiaomi en meer): je typt de code die op het scherm staat.']
      },
      mac: 'Download gratis voor Mac', ipad: 'Download gratis voor iPad', iphone: 'Download gratis voor iPhone', windows: 'Download gratis voor Windows',
      android: 'Download gratis voor Android', boton: 'Download gratis',
      notaAndroid: 'Op Android is het vroege toegang in Google Play: twee korte stappen.',
      barra: 'Download', claro: 'Licht', oscuro: 'Donker', pausar: 'Merken pauzeren', reanudar: 'Merken afspelen',
      frases: ['documentaires over vulkanen', 'muziek om bij te koken', 'live voetbalwedstrijd', 'kerstfilm']
    },
    nb: {
      marcas: {
        lg: ['LG-TV', 'LG med webOS: kobler til over Wi-Fi og kan også slå på TV-en.'],
        samsung: ['Samsung-TV', 'Samsung med Tizen: du godkjenner én gang på TV-en, og så er du klar.'],
        roku: ['Roku', 'Roku: TV-er og spillere, uten noe å koble sammen.'],
        android: ['Google TV', 'Google TV og Android TV (Sony, TCL, Philips, Xiaomi og flere): du skriver inn koden som vises på skjermen.']
      },
      mac: 'Last ned gratis for Mac', ipad: 'Last ned gratis for iPad', iphone: 'Last ned gratis for iPhone', windows: 'Last ned gratis for Windows',
      android: 'Last ned gratis for Android', boton: 'Last ned gratis',
      notaAndroid: 'På Android er det tidlig tilgang på Google Play: to raske steg.',
      barra: 'Last ned', claro: 'Lys', oscuro: 'Mørk', pausar: 'Sett merkene på pause', reanudar: 'Spill av merkene',
      frases: ['dokumentarer om vulkaner', 'musikk til matlaging', 'direkte fotballkamp', 'julefilm']
    },
    pl: {
      marcas: {
        lg: ['Telewizor LG', 'LG z webOS: łączy się przez Wi-Fi i potrafi też włączyć telewizor.'],
        samsung: ['Telewizor Samsung', 'Samsung z Tizenem: raz potwierdzasz na telewizorze i gotowe.'],
        roku: ['Roku', 'Roku: telewizory i odtwarzacze, nic nie trzeba parować.'],
        android: ['Google TV', 'Google TV i Android TV (Sony, TCL, Philips, Xiaomi i inne): wpisujesz kod, który pokazuje ekran.']
      },
      mac: 'Pobierz za darmo na Maca', ipad: 'Pobierz za darmo na iPada', iphone: "Pobierz za darmo na iPhone'a", windows: 'Pobierz za darmo na Windows',
      android: 'Pobierz za darmo na Androida', boton: 'Pobierz za darmo',
      notaAndroid: 'Na Androidzie to wczesny dostęp w Google Play: dwa szybkie kroki.',
      barra: 'Pobierz', claro: 'Jasny', oscuro: 'Ciemny', pausar: 'Wstrzymaj marki', reanudar: 'Odtwarzaj marki',
      frases: ['dokumenty o wulkanach', 'muzyka do gotowania', 'mecz piłkarski na żywo', 'film świąteczny']
    },
    ro: {
      marcas: {
        lg: ['TV LG', 'LG cu webOS: se conectează prin Wi-Fi și poate porni și televizorul.'],
        samsung: ['TV Samsung', 'Samsung cu Tizen: accepți o singură dată pe televizor și gata.'],
        roku: ['Roku', 'Roku: televizoare și playere, nimic de asociat.'],
        android: ['Google TV', 'Google TV și Android TV (Sony, TCL, Philips, Xiaomi și altele): scrii codul afișat pe ecran.']
      },
      mac: 'Descarcă gratuit pentru Mac', ipad: 'Descarcă gratuit pentru iPad', iphone: 'Descarcă gratuit pentru iPhone', windows: 'Descarcă gratuit pentru Windows',
      android: 'Descarcă gratuit pentru Android', boton: 'Descarcă gratuit',
      notaAndroid: 'Pe Android este acces anticipat în Google Play: doi pași rapizi.',
      barra: 'Descarcă', claro: 'Luminos', oscuro: 'Întunecat', pausar: 'Oprește mărcile', reanudar: 'Pornește mărcile',
      frases: ['documentare despre vulcani', 'muzică pentru gătit', 'meci de fotbal în direct', 'film de Crăciun']
    },
    sk: {
      marcas: {
        lg: ['TV LG', 'LG s webOS: pripojí sa cez Wi-Fi a vie televízor aj zapnúť.'],
        samsung: ['TV Samsung', 'Samsung s Tizenom: raz potvrdíš na televízore a máš hotovo.'],
        roku: ['Roku', 'Roku: televízory a prehrávače, nič sa nepáruje.'],
        android: ['Google TV', 'Google TV a Android TV (Sony, TCL, Philips, Xiaomi a ďalšie): prepíšeš kód, ktorý sa zobrazí na obrazovke.']
      },
      mac: 'Stiahnuť zadarmo pre Mac', ipad: 'Stiahnuť zadarmo pre iPad', iphone: 'Stiahnuť zadarmo pre iPhone', windows: 'Stiahnuť zadarmo pre Windows',
      android: 'Stiahnuť zadarmo pre Android', boton: 'Stiahnuť zadarmo',
      notaAndroid: 'Na Androide ide o predbežný prístup v Google Play: stačia dva kroky.',
      barra: 'Stiahnuť', claro: 'Svetlý', oscuro: 'Tmavý', pausar: 'Pozastaviť značky', reanudar: 'Spustiť značky',
      frases: ['dokumenty o sopkách', 'hudba na varenie', 'futbalový zápas naživo', 'vianočný film']
    },
    fi: {
      marcas: {
        lg: ['LG-televisio', 'LG ja webOS: yhdistyy Wi-Fin kautta ja osaa myös käynnistää television.'],
        samsung: ['Samsung-televisio', 'Samsung ja Tizen: hyväksyt kerran televisiossa, ja se on siinä.'],
        roku: ['Roku', 'Roku: televisiot ja soittimet, mitään ei tarvitse yhdistää.'],
        android: ['Google TV', 'Google TV ja Android TV (Sony, TCL, Philips, Xiaomi ja muut): kirjoitat näytöllä näkyvän koodin.']
      },
      mac: 'Lataa ilmaiseksi Macille', ipad: 'Lataa ilmaiseksi iPadille', iphone: 'Lataa ilmaiseksi iPhonelle', windows: 'Lataa ilmaiseksi Windowsille',
      android: 'Lataa ilmaiseksi Androidille', boton: 'Lataa ilmaiseksi',
      notaAndroid: 'Androidilla tämä on varhainen käyttöoikeus Google Playssa: kaksi nopeaa vaihetta.',
      barra: 'Lataa', claro: 'Vaalea', oscuro: 'Tumma', pausar: 'Keskeytä merkit', reanudar: 'Toista merkit',
      frases: ['dokumentit tulivuorista', 'musiikkia ruoanlaittoon', 'jalkapallo-ottelu suorana', 'jouluelokuva']
    },
    sv: {
      marcas: {
        lg: ['LG-tv', 'LG med webOS: ansluter via wifi och kan också sätta på tv:n.'],
        samsung: ['Samsung-tv', 'Samsung med Tizen: du godkänner en gång på tv:n och sedan är du klar.'],
        roku: ['Roku', 'Roku: tv-apparater och spelare, inget att para ihop.'],
        android: ['Google TV', 'Google TV och Android TV (Sony, TCL, Philips, Xiaomi med flera): du skriver in koden som visas på skärmen.']
      },
      mac: 'Ladda ner gratis för Mac', ipad: 'Ladda ner gratis för iPad', iphone: 'Ladda ner gratis för iPhone', windows: 'Ladda ner gratis för Windows',
      android: 'Ladda ner gratis för Android', boton: 'Ladda ner gratis',
      notaAndroid: 'På Android är det tidig åtkomst på Google Play: två snabba steg.',
      barra: 'Ladda ner', claro: 'Ljust', oscuro: 'Mörkt', pausar: 'Pausa märkena', reanudar: 'Spela upp märkena',
      frases: ['dokumentärer om vulkaner', 'musik att laga mat till', 'fotbollsmatch live', 'julfilm']
    },
    vi: {
      marcas: {
        lg: ['TV LG', 'LG với webOS: kết nối qua Wi-Fi và cũng có thể bật TV.'],
        samsung: ['TV Samsung', 'Samsung với Tizen: bạn chỉ cần đồng ý một lần trên TV là xong.'],
        roku: ['Roku', 'Roku: TV và đầu phát, không cần ghép nối gì cả.'],
        android: ['Google TV', 'Google TV và Android TV (Sony, TCL, Philips, Xiaomi và nhiều hãng khác): bạn nhập mã hiển thị trên màn hình.']
      },
      mac: 'Tải miễn phí cho Mac', ipad: 'Tải miễn phí cho iPad', iphone: 'Tải miễn phí cho iPhone', windows: 'Tải miễn phí cho Windows',
      android: 'Tải miễn phí cho Android', boton: 'Tải miễn phí',
      notaAndroid: 'Trên Android, đây là bản truy cập sớm trên Google Play: chỉ hai bước nhanh.',
      barra: 'Tải về', claro: 'Sáng', oscuro: 'Tối', pausar: 'Tạm dừng các hãng', reanudar: 'Phát các hãng',
      frases: ['phim tài liệu về núi lửa', 'nhạc để nấu ăn', 'trận bóng đá trực tiếp', 'phim Giáng sinh']
    },
    tr: {
      marcas: {
        lg: ['LG TV', "LG ve webOS: Wi-Fi ile bağlanır ve TV'yi de açabilir."],
        samsung: ['Samsung TV', "Samsung ve Tizen: TV'de bir kez onaylarsın, hepsi bu."],
        roku: ['Roku', "Roku: TV'ler ve oynatıcılar, eşleştirilecek bir şey yok."],
        android: ['Google TV', 'Google TV ve Android TV (Sony, TCL, Philips, Xiaomi ve diğerleri): ekranda görünen kodu yazarsın.']
      },
      mac: 'Mac için ücretsiz indir', ipad: 'iPad için ücretsiz indir', iphone: 'iPhone için ücretsiz indir', windows: 'Windows için ücretsiz indir',
      android: 'Android için ücretsiz indir', boton: 'Ücretsiz indir',
      notaAndroid: "Android'de Google Play'de erken erişim: iki kısa adım.",
      barra: 'İndir', claro: 'Açık', oscuro: 'Koyu', pausar: 'Markaları duraklat', reanudar: 'Markaları oynat',
      frases: ['yanardağ belgeselleri', 'yemek yaparken müzik', 'canlı futbol maçı', 'aile filmi']
    },
    el: {
      marcas: {
        lg: ['Τηλεόραση LG', 'LG με webOS: συνδέεται μέσω Wi-Fi και μπορεί να ανοίξει και την τηλεόραση.'],
        samsung: ['Τηλεόραση Samsung', 'Samsung με Tizen: αποδέχεσαι μία φορά στην τηλεόραση και τελείωσες.'],
        roku: ['Roku', 'Roku: τηλεοράσεις και συσκευές, χωρίς κανένα ζευγάρωμα.'],
        android: ['Google TV', 'Google TV και Android TV (Sony, TCL, Philips, Xiaomi και άλλες): πληκτρολογείς τον κωδικό που εμφανίζει η οθόνη.']
      },
      mac: 'Δωρεάν λήψη για Mac', ipad: 'Δωρεάν λήψη για iPad', iphone: 'Δωρεάν λήψη για iPhone', windows: 'Δωρεάν λήψη για Windows',
      android: 'Δωρεάν λήψη για Android', boton: 'Δωρεάν λήψη',
      notaAndroid: 'Στο Android είναι πρώιμη πρόσβαση στο Google Play: δύο γρήγορα βήματα.',
      barra: 'Λήψη', claro: 'Φωτεινό', oscuro: 'Σκούρο', pausar: 'Παύση των μαρκών', reanudar: 'Αναπαραγωγή των μαρκών',
      frases: ['ντοκιμαντέρ για ηφαίστεια', 'μουσική για μαγείρεμα', 'ποδοσφαιρικός αγώνας ζωντανά', 'χριστουγεννιάτικη ταινία']
    },
    uk: {
      marcas: {
        lg: ['Телевізор LG', 'LG із webOS: підключається через Wi-Fi і може також увімкнути телевізор.'],
        samsung: ['Телевізор Samsung', 'Samsung із Tizen: ви підтверджуєте один раз на телевізорі, і все готово.'],
        roku: ['Roku', "Roku: телевізори та програвачі, нічого не потрібно з'єднувати."],
        android: ['Google TV', 'Google TV і Android TV (Sony, TCL, Philips, Xiaomi та інші): ви вводите код, який показує екран.']
      },
      mac: 'Завантажити безкоштовно для Mac', ipad: 'Завантажити безкоштовно для iPad', iphone: 'Завантажити безкоштовно для iPhone', windows: 'Завантажити безкоштовно для Windows',
      android: 'Завантажити безкоштовно для Android', boton: 'Завантажити безкоштовно',
      notaAndroid: 'На Android це ранній доступ у Google Play: два швидкі кроки.',
      barra: 'Завантажити', claro: 'Світла', oscuro: 'Темна', pausar: 'Призупинити бренди', reanudar: 'Відтворити бренди',
      frases: ['документальні фільми про вулкани', 'музика для приготування їжі', 'футбольний матч наживо', 'різдвяний фільм']
    },
    he: {
      marcas: {
        lg: ['טלוויזיית LG', 'LG עם webOS: מתחברת דרך Wi-Fi ויכולה גם להדליק את הטלוויזיה.'],
        samsung: ['טלוויזיית Samsung', 'Samsung עם Tizen: מאשרים פעם אחת בטלוויזיה וזהו.'],
        roku: ['Roku', 'Roku: טלוויזיות ונגנים, בלי צורך בצימוד.'],
        android: ['Google TV', 'Google TV ו-Android TV (Sony, TCL, Philips, Xiaomi ועוד): מקלידים את הקוד שמופיע במסך.']
      },
      mac: 'הורדה חינם ל-Mac', ipad: 'הורדה חינם ל-iPad', iphone: 'הורדה חינם ל-iPhone', windows: 'הורדה חינם ל-Windows',
      android: 'הורדה חינם ל-Android', boton: 'הורדה חינם',
      notaAndroid: 'ב-Android זו גישה מוקדמת ב-Google Play: שני שלבים קצרים.',
      barra: 'הורדה', claro: 'בהיר', oscuro: 'כהה', pausar: 'השהיית המותגים', reanudar: 'הפעלת המותגים',
      frases: ['סרטים דוקומנטריים על הרי געש', 'מוזיקה לבישול', 'משחק כדורגל בשידור חי', 'סרט משפחתי']
    },
    ar: {
      marcas: {
        lg: ['تلفزيون LG', 'LG مع webOS: يتصل عبر Wi-Fi ويمكنه أيضًا تشغيل التلفزيون.'],
        samsung: ['تلفزيون Samsung', 'Samsung مع Tizen: توافق مرة واحدة على التلفزيون وينتهي الأمر.'],
        roku: ['Roku', 'Roku: تلفزيونات ومشغلات، بلا أي إقران.'],
        android: ['Google TV', 'Google TV وAndroid TV (Sony وTCL وPhilips وXiaomi وغيرها): تكتب الرمز الذي تعرضه الشاشة.']
      },
      mac: 'نزّل مجانًا لجهاز Mac', ipad: 'نزّل مجانًا لجهاز iPad', iphone: 'نزّل مجانًا لجهاز iPhone', windows: 'نزّل مجانًا لنظام Windows',
      android: 'نزّل مجانًا لنظام Android', boton: 'نزّل مجانًا',
      notaAndroid: 'على Android هو وصول مبكر في Google Play: خطوتان سريعتان.',
      barra: 'تنزيل', claro: 'فاتح', oscuro: 'داكن', pausar: 'إيقاف العلامات مؤقتًا', reanudar: 'تشغيل العلامات',
      frases: ['وثائقيات عن البراكين', 'موسيقى للطبخ', 'مباراة كرة قدم مباشرة', 'فيلم عائلي']
    },
    hi: {
      marcas: {
        lg: ['LG टीवी', 'webOS वाला LG: Wi-Fi से जुड़ता है और टीवी चालू भी कर सकता है।'],
        samsung: ['Samsung टीवी', 'Tizen वाला Samsung: टीवी पर एक बार मंज़ूरी दें और बस हो गया।'],
        roku: ['Roku', 'Roku: टीवी और प्लेयर, कुछ भी पेयर करने की ज़रूरत नहीं।'],
        android: ['Google TV', 'Google TV और Android TV (Sony, TCL, Philips, Xiaomi और अन्य): स्क्रीन पर दिखने वाला कोड डालें।']
      },
      mac: 'Mac के लिए मुफ़्त डाउनलोड करें', ipad: 'iPad के लिए मुफ़्त डाउनलोड करें', iphone: 'iPhone के लिए मुफ़्त डाउनलोड करें', windows: 'Windows के लिए मुफ़्त डाउनलोड करें',
      android: 'Android के लिए मुफ़्त डाउनलोड करें', boton: 'मुफ़्त डाउनलोड करें',
      notaAndroid: 'Android पर यह Google Play में शुरुआती एक्सेस है: बस दो आसान चरण।',
      barra: 'डाउनलोड', claro: 'लाइट', oscuro: 'डार्क', pausar: 'ब्रांड रोकें', reanudar: 'ब्रांड चलाएँ',
      frases: ['ज्वालामुखी पर डॉक्यूमेंट्री', 'खाना बनाने के लिए संगीत', 'फ़ुटबॉल मैच लाइव', 'पारिवारिक फ़िल्म']
    },
    th: {
      marcas: {
        lg: ['ทีวี LG', 'LG ที่ใช้ webOS: เชื่อมต่อผ่าน Wi-Fi และเปิดทีวีได้ด้วย'],
        samsung: ['ทีวี Samsung', 'Samsung ที่ใช้ Tizen: กดยอมรับบนทีวีเพียงครั้งเดียวก็พร้อมใช้งาน'],
        roku: ['Roku', 'Roku: ทีวีและกล่องสตรีมมิง ไม่ต้องจับคู่อะไรเลย'],
        android: ['Google TV', 'Google TV และ Android TV (Sony, TCL, Philips, Xiaomi และยี่ห้ออื่นอีกมาก): พิมพ์รหัสที่แสดงบนหน้าจอ']
      },
      mac: 'ดาวน์โหลดฟรีสำหรับ Mac', ipad: 'ดาวน์โหลดฟรีสำหรับ iPad', iphone: 'ดาวน์โหลดฟรีสำหรับ iPhone', windows: 'ดาวน์โหลดฟรีสำหรับ Windows',
      android: 'ดาวน์โหลดฟรีสำหรับ Android', boton: 'ดาวน์โหลดฟรี',
      notaAndroid: 'บน Android เป็นการเข้าถึงก่อนใครบน Google Play: ทำแค่สองขั้นตอน',
      barra: 'ดาวน์โหลด', claro: 'สว่าง', oscuro: 'มืด', pausar: 'หยุดแบรนด์ชั่วคราว', reanudar: 'เล่นแบรนด์ต่อ',
      frases: ['สารคดีภูเขาไฟ', 'เพลงสำหรับทำอาหาร', 'ถ่ายทอดสดฟุตบอล', 'หนังครอบครัว']
    },
    ko: {
      marcas: {
        lg: ['LG TV', 'webOS를 쓰는 LG: Wi-Fi로 연결되고 TV 전원도 켤 수 있어요.'],
        samsung: ['Samsung TV', 'Tizen을 쓰는 Samsung: TV에서 한 번만 허용하면 바로 쓸 수 있어요.'],
        roku: ['Roku', 'Roku: TV와 플레이어 모두, 따로 페어링할 필요가 없어요.'],
        android: ['Google TV', 'Google TV와 Android TV (Sony, TCL, Philips, Xiaomi 등): 화면에 나오는 코드를 입력하면 돼요.']
      },
      mac: 'Mac용 무료 다운로드', ipad: 'iPad용 무료 다운로드', iphone: 'iPhone용 무료 다운로드', windows: 'Windows용 무료 다운로드',
      android: 'Android용 무료 다운로드', boton: '무료 다운로드',
      notaAndroid: 'Android에서는 Google Play 사전 체험으로 제공돼요: 두 단계면 끝나요.',
      barra: '다운로드', claro: '라이트', oscuro: '다크', pausar: '브랜드 일시정지', reanudar: '브랜드 재생',
      frases: ['화산 다큐멘터리', '요리할 때 듣는 음악', '축구 경기 생중계', '크리스마스 영화']
    },
    ja: {
      marcas: {
        lg: ['LGテレビ', 'webOS搭載のLG：Wi-Fiで接続でき、テレビの電源も入れられます。'],
        samsung: ['Samsungテレビ', 'Tizen搭載のSamsung：テレビで一度許可するだけで使えます。'],
        roku: ['Roku', 'Roku：テレビもプレーヤーも、ペアリングは不要です。'],
        android: ['Google TV', 'Google TVとAndroid TV（Sony、TCL、Philips、Xiaomiなど）：画面に表示されるコードを入力します。']
      },
      mac: 'Mac用に無料ダウンロード', ipad: 'iPad用に無料ダウンロード', iphone: 'iPhone用に無料ダウンロード', windows: 'Windows用に無料ダウンロード',
      android: 'Android用に無料ダウンロード', boton: '無料ダウンロード',
      notaAndroid: 'Androidでは、Google Playの先行アクセスです。2ステップで始められます。',
      barra: 'ダウンロード', claro: 'ライト', oscuro: 'ダーク', pausar: 'ブランドを一時停止', reanudar: 'ブランドを再生',
      frases: ['火山のドキュメンタリー', '料理のときの音楽', 'サッカーの生中継', 'クリスマス映画']
    },
    'zh-hans': {
      marcas: {
        lg: ['LG 电视', '搭载 webOS 的 LG：通过 Wi-Fi 连接，还能开启电视。'],
        samsung: ['Samsung 电视', '搭载 Tizen 的 Samsung：在电视上确认一次就能用。'],
        roku: ['Roku', 'Roku：电视和播放器都无需配对。'],
        android: ['Google TV', 'Google TV 和 Android TV（Sony、TCL、Philips、小米等）：输入屏幕上显示的代码即可。']
      },
      mac: '免费下载 Mac 版', ipad: '免费下载 iPad 版', iphone: '免费下载 iPhone 版', windows: '免费下载 Windows 版',
      android: '免费下载 Android 版', boton: '免费下载',
      notaAndroid: '在 Android 上是 Google Play 的抢先体验：只需两步。',
      barra: '下载', claro: '浅色', oscuro: '深色', pausar: '暂停品牌', reanudar: '播放品牌',
      frases: ['火山纪录片', '做饭时听的音乐', '足球比赛直播', '圣诞电影']
    },
    'zh-hant': {
      marcas: {
        lg: ['LG 電視', '搭載 webOS 的 LG：透過 Wi-Fi 連線，還能開啟電視。'],
        samsung: ['Samsung 電視', '搭載 Tizen 的 Samsung：在電視上確認一次就能使用。'],
        roku: ['Roku', 'Roku：電視與播放器都不需要配對。'],
        android: ['Google TV', 'Google TV 與 Android TV（Sony、TCL、Philips、小米等）：輸入畫面上顯示的代碼即可。']
      },
      mac: '免費下載 Mac 版', ipad: '免費下載 iPad 版', iphone: '免費下載 iPhone 版', windows: '免費下載 Windows 版',
      android: '免費下載 Android 版', boton: '免費下載',
      notaAndroid: '在 Android 上是 Google Play 的搶先體驗：只要兩個步驟。',
      barra: '下載', claro: '淺色', oscuro: '深色', pausar: '暫停品牌', reanudar: '播放品牌',
      frases: ['火山紀錄片', '烹飪時聽的音樂', '足球賽直播', '聖誕電影']
    }
  };
  var L = (document.documentElement.lang || '').toLowerCase();  // zh-hans y zh-hant tienen tabla propia; pt-br usa pt
  var T = TEXTOS[L] || TEXTOS[L.slice(0, 2)] || ES;
  if (T.marcas) {
    Object.keys(T.marcas).forEach(function (k) { marcas[k].tv = T.marcas[k][0]; marcas[k].nota = T.marcas[k][1]; });
  }
  var raiz = document.documentElement;
  var telefono = document.getElementById('telefono');
  if (!telefono) return;
  var orden = ['samsung', 'lg', 'roku', 'android'];
  var actual = 'samsung';
  var nombreTv = document.getElementById('app-tv');
  var nota = document.getElementById('marca-nota');
  var botones = document.querySelectorAll('[data-marca]');
  var tema = document.querySelector('meta[name="theme-color"]');
  var gigante = document.querySelector('.gigante');
  var vitrina = document.querySelector('.vitrina');
  var num = document.getElementById('vitrina-num');
  var nombreVitrina = document.getElementById('vitrina-nombre');
  var barras = document.querySelectorAll('.vitrina-barras i');
  var nombres = {};
  botones.forEach(function (b) { nombres[b.dataset.marca] = b.textContent.trim(); });
  var volumen = document.getElementById('app-volumen');

  // Demostración sola (23-nov, "que llame más la atención"): con cada marca que entra, un dedo invisible toca una
  // tecla (onda de luz y la tecla se hunde; en LG sube el volumen de 12 a 13) y, cada dos marcas, un brillo cruza el
  // vidrio. Una sola cosa a la vez y solo mientras la vitrina gira sola. Con la Web Animations API, que funciona aunque
  // Windows tenga los efectos desactivados (decisión del fundador).
  var pantallaApp = telefono.querySelector('.app');
  var brillo = telefono.querySelector('.t-brillo');
  var onda = null, demoPendiente = [];
  var DEMO = { samsung: '.ok', lg: '.balancin b', roku: '.flecha.der', android: '.ok' };
  function cancelarDemo() { demoPendiente.forEach(clearTimeout); demoPendiente = []; }
  function enPantalla(el) { // posición en la pantalla de la app (440 x 956), sin contar la escala ni el giro
    var x = 0, y = 0, n = el;
    while (n && n !== pantallaApp) { x += n.offsetLeft; y += n.offsetTop; n = n.offsetParent; }
    return { x: x + el.offsetWidth / 2, y: y + el.offsetHeight / 2 };
  }
  function tocarDemo(id) {
    var el = pantallaApp && pantallaApp.querySelector(DEMO[id]);
    if (!el || !el.animate) return;
    if (!onda) { onda = document.createElement('i'); onda.className = 't-onda'; pantallaApp.appendChild(onda); }
    var c = enPantalla(el);
    onda.style.left = c.x + 'px';
    onda.style.top = c.y + 'px';
    onda.animate([
      { opacity: 0, transform: 'scale(.35)' }, { opacity: .7, transform: 'scale(.7)', offset: .25 }, { opacity: 0, transform: 'scale(1.45)' }
    ], { duration: 720, easing: 'cubic-bezier(.23, 1, .32, 1)' });
    el.animate([
      { transform: 'scale(1)', filter: 'brightness(1)' }, { transform: 'scale(.92)', filter: 'brightness(1.4)', offset: .3 },
      { transform: 'scale(1)', filter: 'brightness(1)' }
    ], { duration: 460, easing: 'cubic-bezier(.23, 1, .32, 1)' });
    if (id === 'lg' && volumen) {
      demoPendiente.push(setTimeout(function () {
        volumen.textContent = '13';
        volumen.animate([{ opacity: 0, transform: 'translateY(6px)' }, { opacity: 1, transform: 'none' }],
          { duration: 260, easing: 'cubic-bezier(.23, 1, .32, 1)' });
      }, 140));
    }
  }
  function cruzarBrillo() {
    if (!brillo || !brillo.animate) return;
    brillo.animate([
      { opacity: 0, transform: 'translateX(-150%) skewX(-14deg)' }, { opacity: 1, offset: .25 }, { opacity: 1, offset: .75 },
      { opacity: 0, transform: 'translateX(330%) skewX(-14deg)' }
    ], { duration: 1200, easing: 'cubic-bezier(.4, 0, .2, 1)' });
  }
  function demostrar(id) {
    cancelarDemo();
    demoPendiente.push(setTimeout(function () { if (!enPausa()) tocarDemo(id); }, 1000));
    if (id === 'samsung' || id === 'roku') demoPendiente.push(setTimeout(function () { if (!enPausa()) cruzarBrillo(); }, 1900));
  }

  function aplicar(id, porUsuario) {
    var m = marcas[id];
    raiz.style.setProperty('--marca', m.color);
    raiz.style.setProperty('--marca-2', m.color2);
    if (tema) tema.setAttribute('content', m.color);
    nombreTv.textContent = m.tv;
    // El número del volumen solo lo muestran los TV LG en la app (estilos.css); cada marca entra con 12.
    telefono.dataset.marca = id;
    if (volumen) volumen.textContent = '12';
    // Solo se anuncia a los lectores de pantalla cuando la persona elige; la rotación sola no interrumpe.
    nota.setAttribute('aria-live', porUsuario ? 'polite' : 'off');
    nota.textContent = m.nota;
    var i = orden.indexOf(id);
    if (num) num.textContent = '0' + (i + 1);
    if (nombreVitrina) nombreVitrina.textContent = nombres[id] || m.tv;
  }

  // Avance de la rotación: la barra de la marca actual se llena en el tiempo de cada vuelta.
  // Se reinicia en el cuadro siguiente (sin forzar un cálculo de diseño con offsetWidth).
  function marcarBarras() {
    var i = orden.indexOf(actual);
    barras.forEach(function (b, k) {
      b.classList.remove('activa');
      b.classList.toggle('pasada', k < i);
    });
    if (barras[i]) requestAnimationFrame(function () { requestAnimationFrame(function () { barras[i].classList.add('activa'); }); });
  }

  // Cambio de marca como vitrina: el teléfono sale hacia un lado, cambian la marca y el color, y el nuevo entra por
  // el lado contrario ("Siguiente" y la rotación salen por la izquierda; "Anterior" al revés).
  var clases = ['sale-izq', 'sale-der', 'entra-der', 'entra-izq'];
  var cambio = null;
  function elegir(id, haciaAtras, porUsuario) {
    if (!marcas[id] || id === actual) return;
    if (haciaAtras === undefined) haciaAtras = orden.indexOf(id) < orden.indexOf(actual);
    actual = id;
    botones.forEach(function (b) { b.setAttribute('aria-pressed', String(b.dataset.marca === id)); });
    marcarBarras();
    clearTimeout(cambio);
    cancelarDemo();
    telefono.classList.remove.apply(telefono.classList, clases);
    void telefono.offsetWidth; // reinicia la animación
    telefono.classList.add(haciaAtras ? 'sale-der' : 'sale-izq');
    cambio = setTimeout(function () {
      aplicar(id, porUsuario);
      telefono.classList.remove.apply(telefono.classList, clases);
      void telefono.offsetWidth;
      telefono.classList.add(haciaAtras ? 'entra-izq' : 'entra-der');
      if (!porUsuario) demostrar(id);
      // La palabra gigante se desliza un poco en la misma dirección.
      if (gigante && gigante.animate) {
        gigante.animate([
          { transform: 'translateY(-50%) translateX(' + (haciaAtras ? '-6%' : '6%') + ')', opacity: 0 },
          { transform: 'translateY(-50%) translateX(0)', opacity: 1 }
        ], { duration: 620, easing: 'cubic-bezier(.23, 1, .32, 1)' });
      }
    }, 260);
  }
  function mover(paso, porUsuario) { elegir(orden[(orden.indexOf(actual) + paso + orden.length) % orden.length], paso < 0, porUsuario); }

  // Rotación sola, para mostrar que sirve con todas las marcas. Se pausa mientras la persona mira o toca la vitrina
  // (mouse, dedo o teclado), si el teléfono no está a la vista o la pestaña está oculta; el botón de pausa la detiene.
  // Sigue con "reducir movimiento" (decisión del fundador: es el producto).
  var VUELTA = 3500, restante = VUELTA, inicio = 0, temporizador = null;
  var detenida = false, mirando = false, aLaVista = true;
  var pausa = document.getElementById('pausa');
  if (vitrina) vitrina.style.setProperty('--vuelta', VUELTA + 'ms');
  function enPausa() { return detenida || mirando || !aLaVista || document.hidden; }
  function actualizar() {
    if (enPausa()) {
      if (temporizador) { clearTimeout(temporizador); temporizador = null; restante = Math.max(0, restante - (performance.now() - inicio)); }
      if (vitrina) vitrina.classList.add('en-pausa');
      return;
    }
    if (vitrina) vitrina.classList.remove('en-pausa');
    if (temporizador) return;
    inicio = performance.now();
    temporizador = setTimeout(function () {
      temporizador = null; restante = VUELTA;
      mover(1, false);
      actualizar();
    }, restante);
  }
  function ponerPausa(si) {
    detenida = si;
    if (vitrina) vitrina.classList.toggle('quieta', si);
    if (pausa) {
      pausa.dataset.estado = si ? 'pausa' : 'gira';
      pausa.setAttribute('aria-label', si ? T.reanudar : T.pausar);
    }
    if (!si) { restante = VUELTA; marcarBarras(); }
    actualizar();
  }
  if (pausa) {
    pausa.setAttribute('aria-label', T.pausar);
    pausa.addEventListener('click', function () { ponerPausa(!detenida); });
  }
  // Con el mouse se pausa sobre el teléfono y los selectores; con el teclado, mientras el foco esté en cualquier parte
  // del hero (WCAG 2.2.2: el color no cambia mientras la persona recorre la ficha).
  var conMouse = false, conFoco = false;
  var esperaToque = null;
  [document.querySelector('.escaparate'), document.querySelector('.marcas'), document.querySelector('.equipos')].forEach(function (zona) {
    if (!zona) return;
    zona.addEventListener('pointerenter', function (e) { if (e.pointerType === 'mouse') { conMouse = true; mirando = true; actualizar(); } });
    zona.addEventListener('pointerleave', function (e) { if (e.pointerType === 'mouse') { conMouse = false; mirando = conFoco; actualizar(); } });
  });
  var panel = document.querySelector('.panel');
  if (panel) {
    panel.addEventListener('focusin', function () { conFoco = true; mirando = true; actualizar(); });
    panel.addEventListener('focusout', function (e) {
      if (panel.contains(e.relatedTarget)) return;
      conFoco = false; mirando = conMouse; actualizar();
    });
  }
  if ('IntersectionObserver' in window && document.querySelector('.escaparate')) {
    new IntersectionObserver(function (e) { aLaVista = e[0].isIntersecting; actualizar(); }, { threshold: 0.3 })
      .observe(document.querySelector('.escaparate'));
  }
  document.addEventListener('visibilitychange', actualizar);

  botones.forEach(function (b) { b.addEventListener('click', function () { ponerPausa(true); elegir(b.dataset.marca, undefined, true); }); });
  document.getElementById('anterior').addEventListener('click', function () { ponerPausa(true); mover(-1, true); });
  document.getElementById('siguiente').addEventListener('click', function () { ponerPausa(true); mover(1, true); });
  // Puntos de color bajo el teléfono: tocar uno elige esa marca (las flechas y la pausa siguen para el teclado).
  barras.forEach(function (b, k) { b.addEventListener('click', function () { ponerPausa(true); elegir(orden[k], undefined, true); }); });
  marcarBarras();
  actualizar();

  // Tu equipo: iPhone, iPad, Android o Windows. El botón Descargar va directo a su tienda (Android, en prueba
  // anticipada, baja a los dos pasos para unirse). Se elige sola según el aparato.
  var principal = document.getElementById('boton-principal');
  var textoPrincipal = document.getElementById('boton-principal-texto');
  var notaBoton = document.getElementById('boton-nota');
  var APPLE = 'https://apps.apple.com/app/id6834927348';
  var MICROSOFT = 'https://apps.microsoft.com/detail/9N3D7T1DP2SW?mode=direct';
  var destinos = { iphone: APPLE, ipad: APPLE, mac: APPLE, windows: MICROSOFT, android: '#android' };
  var equipos = document.querySelectorAll('[data-equipo]');
  function elegirEquipo(id) {
    equipos.forEach(function (b) { b.setAttribute('aria-pressed', String(b.dataset.equipo === id)); });
    if (!principal) return;
    var externo = destinos[id] && destinos[id].charAt(0) !== '#';
    principal.href = destinos[id] || '#tiendas';
    if (externo) { principal.target = '_blank'; principal.rel = 'noopener'; }
    else { principal.removeAttribute('target'); principal.removeAttribute('rel'); }
    textoPrincipal.textContent = T[id] || T.boton;
    if (notaBoton) {
      notaBoton.textContent = id === 'android' ? T.notaAndroid : '';
      notaBoton.hidden = id !== 'android';
    }
    sincronizarBarra();
  }
  equipos.forEach(function (b) { b.addEventListener('click', function () { elegirEquipo(b.dataset.equipo); }); });
  var ua = navigator.userAgent;
  var esIpad = /iPad/.test(ua) || (/Macintosh/.test(ua) && navigator.maxTouchPoints > 1);
  var inicial = esIpad ? 'ipad'
    : /iPhone|iPod/.test(ua) ? 'iphone'
    : /Android/.test(ua) ? 'android'
    : (/Windows NT/.test(ua) && !/Mobile|Xbox/.test(ua)) ? 'windows'
    : /Macintosh/.test(ua) ? 'mac' : null;
  // Barra fija al bajar (estilo Apple): logo y Descargar siempre a mano, con el mismo destino que el botón principal.
  // Mientras no se ve queda inerte para que el teclado no llegue a enlaces ocultos.
  var barraFija = null, barraDescargar = null;
  // También el botón de la barra de arriba y el de la sección de precio (tanda 1, 26-nov): todos van a la misma tienda.
  function sincronizarBarra() {
    if (!principal) return;
    [barraDescargar, document.querySelector('.barra .boton-barra'), document.getElementById('precio-descargar')].forEach(function (b) {
      if (!b) return;
      b.href = principal.getAttribute('href');
      ['target', 'rel'].forEach(function (a) {
        if (principal.hasAttribute(a)) b.setAttribute(a, principal.getAttribute(a));
        else b.removeAttribute(a);
      });
    });
  }
  var portada = document.querySelector('.escena');
  if (principal && portada && 'IntersectionObserver' in window) {
    barraFija = document.createElement('div');
    barraFija.className = 'barra-fija';
    barraFija.setAttribute('inert', '');
    var logoFijo = document.createElement('a');
    logoFijo.className = 'logo';
    logoFijo.href = '#inicio';
    var iconoFijo = document.createElement('img');
    iconoFijo.src = '/icono.svg';
    iconoFijo.alt = 'Mando TV';
    iconoFijo.width = 26;
    iconoFijo.height = 26;
    logoFijo.appendChild(iconoFijo);
    logoFijo.appendChild(document.createTextNode('Mando TV'));
    barraDescargar = document.createElement('a');
    barraDescargar.className = 'boton';
    barraDescargar.id = 'barra-descargar';
    barraDescargar.textContent = T.barra;
    barraFija.appendChild(logoFijo);
    barraFija.appendChild(barraDescargar);
    document.body.appendChild(barraFija);
    new IntersectionObserver(function (e) {
      var fuera = !e[0].isIntersecting;
      barraFija.classList.toggle('visible', fuera);
      if (fuera) barraFija.removeAttribute('inert'); else barraFija.setAttribute('inert', '');
    }).observe(portada);
  }
  if (inicial) elegirEquipo(inicial);
  sincronizarBarra();

  var nombreTema = document.getElementById('tema-nombre');
  document.querySelectorAll('[data-tema]').forEach(function (p) {
    p.addEventListener('click', function () {
      var claro = p.dataset.tema === 'claro';
      telefono.classList.toggle('claro', claro);
      if (nombreTema) nombreTema.textContent = claro ? T.claro : T.oscuro;
      document.querySelectorAll('[data-tema]').forEach(function (o) { o.setAttribute('aria-pressed', String(o === p)); });
    });
  });

  // Teclas del teléfono dibujado: responden al toque y muestran qué se envió al TV (demostración, como en la app).
  var escaparate = document.querySelector('.escaparate');
  // La etiqueta solo aparece al tocar una tecla (antes había una pista fija, "Toca los botones", que tapaba el
  // teléfono: pedido del fundador). Para invitar a tocar, el OK late dos veces al cargar y nada más.
  var chip = document.createElement('span');
  chip.className = 'toque';
  chip.setAttribute('aria-hidden', 'true');
  if (escaparate) escaparate.appendChild(chip);
  // Al cargar, la primera demostración invita a tocar (antes el OK latía dos veces).
  var tocado = false;
  setTimeout(function () { if (!tocado && actual === 'samsung' && !enPausa()) { tocarDemo('samsung'); } }, 1400);
  setTimeout(function () { if (!tocado && actual === 'samsung' && !enPausa()) cruzarBrillo(); }, 2300);
  var FLECHAS = { arriba: '▲', abajo: '▼', izq: '◀', der: '▶' };
  function etiquetaDe(el, e) {
    if (el.classList.contains('cruceta')) {
      var r = el.getBoundingClientRect();
      var x = e.clientX - (r.left + r.width / 2), y = e.clientY - (r.top + r.height / 2);
      if (Math.hypot(x, y) < r.width * 0.2) return { el: el.querySelector('.ok'), txt: 'OK' };
      var lado = Math.abs(x) > Math.abs(y) ? (x > 0 ? 'der' : 'izq') : (y > 0 ? 'abajo' : 'arriba');
      return { el: el.querySelector('.' + lado), txt: FLECHAS[lado] };
    }
    if (el.classList.contains('balancin')) {
      var rb = el.getBoundingClientRect();
      var arriba = e.clientY < rb.top + rb.height / 2;
      var bs = el.querySelectorAll('b');
      return { el: arriba ? bs[0] : bs[1], txt: el.querySelector('small').textContent + (arriba ? ' +' : ' −') };
    }
    var s = el.querySelector('span');
    return { el: el, txt: (s ? s.textContent : el.textContent).trim() };
  }
  var ocultar = null;
  telefono.addEventListener('pointerdown', function (e) {
    // Al tocar el teléfono la rotación de marcas espera (con el dedo no hay "pasar por encima" que la pause, y el
    // teléfono cambiaba de marca en mitad del toque). Sigue sola 8 s después del último toque: los botones de pausa
    // y flechas ya no se muestran (pedido del fundador), así que no puede quedar detenida para siempre.
    mirando = true; actualizar();
    clearTimeout(esperaToque);
    esperaToque = setTimeout(function () { mirando = conMouse || conFoco; actualizar(); }, 8000);
    var el = e.target.closest('.cruceta, .balancin, .tecla, .pestanas span');
    if (!el) return;
    var t = etiquetaDe(el, e);
    if (!t.el) return;
    t.el.classList.add('pulsada');
    setTimeout(function () { t.el.classList.remove('pulsada'); }, 160);
    tocado = true;
    chip.textContent = t.txt;
    // Vibra solo si el navegador ya registró un toque real (si no, Chrome bloquea la llamada y deja un error en la consola).
    var activo = !navigator.userActivation || navigator.userActivation.hasBeenActive;
    if (navigator.vibrate && activo) { try { navigator.vibrate(8); } catch (err) { /* sin vibración */ } }
    if (chip.animate) {
      chip.animate([{ opacity: 0, transform: 'translateY(6px) scale(.96)' }, { opacity: 1, transform: 'none' }],
        { duration: 180, easing: 'cubic-bezier(.23, 1, .32, 1)', fill: 'both' });
      clearTimeout(ocultar);
      ocultar = setTimeout(function () {
        chip.animate([{ opacity: 1 }, { opacity: 0 }], { duration: 200, easing: 'ease-out', fill: 'both' });
      }, 900);
    }
  });

  // Inclinación 3D del teléfono siguiendo el mouse (solo con mouse; en pantallas táctiles queda el flotado).
  var inclinador = document.getElementById('inclinador');
  if (escaparate && inclinador && window.matchMedia('(hover: hover) and (pointer: fine)').matches) {
    var max = 12; // grados
    var cuadro = null;
    escaparate.addEventListener('pointermove', function (e) {
      var r = escaparate.getBoundingClientRect();
      var x = (e.clientX - r.left) / r.width - 0.5;
      var y = (e.clientY - r.top) / r.height - 0.5;
      if (cuadro) cancelAnimationFrame(cuadro);
      cuadro = requestAnimationFrame(function () {
        inclinador.classList.add('siguiendo');
        // Parte de la pose de reposo (estilos.css: --rx 3deg, --ry -9deg).
        inclinador.style.transform = 'rotateX(' + (3 - y * max * 1.4).toFixed(2) + 'deg) rotateY(' + (-9 + x * max * 2).toFixed(2) + 'deg)';
      });
    });
    escaparate.addEventListener('pointerleave', function () {
      inclinador.classList.remove('siguiendo');
      inclinador.style.transform = '';
    });
  }

  // Banda de marcas: se mueve con la Web Animations API, que funciona aunque Windows tenga los efectos desactivados
  // (decisión del fundador); con el mouse encima se detiene para poder leerla.
  var pista = document.querySelector('.banda-pista');
  if (pista && pista.animate) {
    var giro = pista.animate([{ transform: 'translateX(0)' }, { transform: 'translateX(-50%)' }],
      { duration: 46000, iterations: Infinity, easing: 'linear' });
    if (window.matchMedia('(hover: hover) and (pointer: fine)').matches) {
      pista.addEventListener('pointerenter', function () { giro.pause(); });
      pista.addEventListener('pointerleave', function () { giro.play(); });
    }
  }

  // Demostración del teclado: escribe búsquedas letra por letra, las borra y escribe la siguiente.
  var textoTeclado = document.getElementById('texto-teclado');
  if (textoTeclado) {
    var frases = T.frases;
    var f = 0, n = frases[0].length, borrando = true;
    (function escribir() {
      var frase = frases[f];
      if (borrando) {
        n--;
        if (n <= 0) { borrando = false; f = (f + 1) % frases.length; frase = frases[f]; }
      } else {
        n++;
        if (n >= frase.length) { borrando = true; textoTeclado.textContent = frase; setTimeout(escribir, 2200); return; }
      }
      textoTeclado.textContent = frase.slice(0, Math.max(n, 0));
      setTimeout(escribir, borrando ? 35 : 75);
    })();
  }

  // Demostración de entradas: va cambiando sola entre TV en vivo, HDMI 1 y HDMI 2.
  var entradasDemo = document.getElementById('entradas-demo');
  if (entradasDemo) {
    var opciones = entradasDemo.querySelectorAll('span');
    var elegida = 1;
    setInterval(function () {
      elegida = (elegida + 1) % opciones.length;
      opciones.forEach(function (o, i) { o.className = i === elegida ? 'sel' : 'vidrio'; });
    }, 1800);
  }

  // Pieza "Widget (Pro)": como las otras piezas, muestra su uso solo, con un toque suave en subir volumen cada
  // tanto (Web Animations: funciona aunque Windows tenga los efectos desactivados).
  var volWidget = document.querySelector('.pieza-widget .w-vol i:last-child');
  if (volWidget && volWidget.animate) {
    setInterval(function () {
      volWidget.animate([
        { transform: 'scale(1)', filter: 'brightness(1)' }, { transform: 'scale(.86)', filter: 'brightness(1.25)', offset: .35 },
        { transform: 'scale(1)', filter: 'brightness(1)' }
      ], { duration: 520, easing: 'cubic-bezier(.23, 1, .32, 1)' });
    }, 2600);
  }

  // Entrada escalonada de cada sección al aparecer en pantalla.
  var piezas = document.querySelectorAll('.aparece');
  if (!('IntersectionObserver' in window)) {
    piezas.forEach(function (el) { el.classList.add('visible'); });
    return;
  }
  var obs = new IntersectionObserver(function (entradas) {
    entradas.forEach(function (e) {
      if (!e.isIntersecting) return;
      var hermanos = Array.prototype.filter.call(e.target.parentNode.children, function (h) { return h.classList.contains('aparece'); });
      e.target.style.transitionDelay = Math.min(hermanos.indexOf(e.target), 6) * 70 + 'ms';
      e.target.classList.add('visible');
      obs.unobserve(e.target);
    });
  }, { rootMargin: '0px 0px -8% 0px' });
  piezas.forEach(function (el) { obs.observe(el); });
})();

// El teléfono de la vitrina se toca, no se selecciona. Con user-select: none el navegador igual marcaba el texto
// vecino al hacer doble o triple clic sobre una tecla (por ejemplo "OK"), así que se cancela el inicio de la selección
// dentro de la vitrina. El clic y el toque siguen llegando a las teclas.
(function () {
  var vitrina = document.querySelector('.escaparate');
  if (!vitrina) return;
  vitrina.addEventListener('selectstart', function (e) { e.preventDefault(); });
  vitrina.addEventListener('mousedown', function (e) { if (e.detail > 1) e.preventDefault(); });
})();

// Pestañas del teléfono de la vitrina (25-nov, pedido del fundador): Touchpad, Teclado y Apps responden al toque y
// cambian la zona central del teléfono, como en la app. Las vistas se crean aquí para no repetir marcado en las
// portadas de los 30 idiomas: no llevan texto que traducir (letras, íconos y nombres de apps).
(function () {
  var telefono = document.getElementById('telefono');
  var app = telefono && telefono.querySelector('.app');
  var pestanas = app && app.querySelectorAll('.pestanas span');
  if (!app || !pestanas || pestanas.length !== 4) return;
  var NOMBRES = ['control', 'touchpad', 'teclado', 'apps'];
  var chip = document.querySelector('.escaparate .toque');
  var ocultar = null;
  function avisar(txt) {   // la misma etiqueta que muestran las teclas del control
    if (!chip) return;
    chip.textContent = txt;
    if (!chip.animate) return;
    chip.animate([{ opacity: 0, transform: 'translateY(6px) scale(.96)' }, { opacity: 1, transform: 'none' }],
      { duration: 140, easing: 'cubic-bezier(.23, 1, .32, 1)', fill: 'both' });
    clearTimeout(ocultar);
    ocultar = setTimeout(function () {
      chip.animate([{ opacity: 1 }, { opacity: 0 }], { duration: 200, easing: 'ease-out', fill: 'both' });
    }, 900);
  }
  function pulsar(el) {
    el.classList.add('pulsada');
    setTimeout(function () { el.classList.remove('pulsada'); }, 130);
  }
  function crear(clase, html) {
    var d = document.createElement('div');
    d.className = 'vista ' + clase;
    d.innerHTML = html;
    app.insertBefore(d, app.querySelector('.pestanas'));
    return d;
  }

  // Touchpad: el punto sigue al dedo; un toque corto es OK.
  var icono = pestanas[1].querySelector('svg');
  var vPad = crear('v-touchpad', '<div class="v-pad">' + (icono ? icono.outerHTML : '') + '<i class="v-punto"></i></div>');
  var pad = vPad.querySelector('.v-pad'), punto = vPad.querySelector('.v-punto');
  var arrastre = null;
  function mover(e) {
    var r = pad.getBoundingClientRect();
    var x = Math.max(0, Math.min(1, (e.clientX - r.left) / r.width)), y = Math.max(0, Math.min(1, (e.clientY - r.top) / r.height));
    punto.style.left = (x * pad.offsetWidth) + 'px';
    punto.style.top = (y * pad.offsetHeight) + 'px';
  }
  pad.addEventListener('pointerdown', function (e) {
    arrastre = { x: e.clientX, y: e.clientY, movido: false };
    try { pad.setPointerCapture(e.pointerId); } catch (err) { /* sin captura */ }
    mover(e);
    punto.style.opacity = '1';
  });
  pad.addEventListener('pointermove', function (e) {
    if (!arrastre) return;
    if (Math.hypot(e.clientX - arrastre.x, e.clientY - arrastre.y) > 6) arrastre.movido = true;
    mover(e);
  });
  function soltar() {
    if (!arrastre) return;
    if (!arrastre.movido) avisar('OK');
    arrastre = null;
    if (punto.animate) punto.animate([{ opacity: 1, transform: 'scale(1)' }, { opacity: 0, transform: 'scale(1.9)' }], { duration: 260, easing: 'ease-out' });
    punto.style.opacity = '0';
  }
  pad.addEventListener('pointerup', soltar);
  pad.addEventListener('pointercancel', soltar);

  // Teclado: lo que se toca aparece en el campo, como al escribir en el buscador del TV.
  var BORRAR = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 5H9l-6 7 6 7h12a1 1 0 0 0 1-1V6a1 1 0 0 0-1-1z"/><path d="m16 9-5 6m0-6 5 6"/></svg>';
  var ENVIAR = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14m-6-6 6 6-6 6"/></svg>';
  var filas = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm'].map(function (f, n) {
    var t = f.split('').map(function (c) { return '<span class="v-letra" data-t="' + c + '">' + c + '</span>'; }).join('');
    if (n === 2) t += '<span class="v-letra ancha" data-t="borrar">' + BORRAR + '</span>';
    return '<div class="v-fila">' + t + '</div>';
  }).join('');
  filas += '<div class="v-fila"><span class="v-letra espacio" data-t=" "></span><span class="v-letra ancha enviar" data-t="enviar">' + ENVIAR + '</span></div>';
  var vTec = crear('v-teclado', '<div class="v-campo"><span class="v-texto"></span><i class="v-cursor"></i></div><div class="v-filas">' + filas + '</div>');
  var texto = vTec.querySelector('.v-texto'), cursor = vTec.querySelector('.v-cursor');
  if (cursor.animate) cursor.animate([{ opacity: 1 }, { opacity: 1, offset: .5 }, { opacity: 0, offset: .51 }, { opacity: 0 }], { duration: 1000, iterations: Infinity });
  vTec.addEventListener('pointerdown', function (e) {
    var k = e.target.closest('.v-letra');
    if (!k) return;
    pulsar(k);
    var t = k.dataset.t;
    if (t === 'borrar') { texto.textContent = texto.textContent.slice(0, -1); avisar('⌫'); }
    else if (t === 'enviar') { avisar(texto.textContent.trim() ? texto.textContent.trim() + '  ↵' : '↵'); texto.textContent = ''; }
    else { if (texto.textContent.length < 22) texto.textContent += t; avisar(t === ' ' ? '␣' : t.toUpperCase()); }
  });

  // Apps: al tocar una, la etiqueta dice cuál se abriría en el TV. Sin logos: la inicial sobre un color.
  var APPS = [['YouTube', '#e5352b'], ['Netflix', '#c2101a'], ['Prime Video', '#1a8fe3'], ['Disney+', '#2a4fd6'], ['Spotify', '#1a9f4b'],
    ['Twitch', '#8a45f0'], ['Apple TV', '#6f7480'], ['Max', '#5b3df5'], ['Plex', '#c98a06']];
  var vApps = crear('v-apps', '<div class="v-rejilla">' + APPS.map(function (a) {
    return '<span class="v-app" data-t="' + a[0] + '"><i style="background:' + a[1] + '">' + a[0].charAt(0) + '</i>' + a[0] + '</span>';
  }).join('') + '</div>');
  vApps.addEventListener('pointerdown', function (e) {
    var k = e.target.closest('.v-app');
    if (!k) return;
    pulsar(k);
    avisar(k.dataset.t);
  });

  // Cambio de pestaña: al instante en el pointerdown (sin esperar al clic) y con una entrada corta hecha con la
  // Web Animations API, que también se ve con los efectos de Windows apagados.
  var vistas = { touchpad: vPad, teclado: vTec, apps: vApps };
  app.dataset.vista = 'control';
  Array.prototype.forEach.call(pestanas, function (p, i) {
    p.addEventListener('pointerdown', function () {
      var nombre = NOMBRES[i];
      if (app.dataset.vista === nombre) return;
      app.dataset.vista = nombre;
      Array.prototype.forEach.call(pestanas, function (o) { o.classList.toggle('activa', o === p); });
      var entra = vistas[nombre] ? [vistas[nombre]] : Array.prototype.slice.call(app.querySelectorAll('.t-chips, .t-teclas, .cruceta'));
      entra.forEach(function (el) {
        if (el.animate) el.animate([{ opacity: 0 }, { opacity: 1 }], { duration: 150, easing: 'ease-out' });
      });
    });
  });
})();
