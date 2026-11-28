# Textos en húngaro (tuteo) de mandotv.app. Los usa generar_idiomas.py. Escritos para las búsquedas de Hungría.
# Las claves de las páginas (lg, lost-tv, ...) y sus rutas están en idiomas_sitio.py.
# Los nombres de menús de cada marca (LG, Samsung, Roku, Android TV, iPhone) son los mismos que usa la app en húngaro
# (lib/l10n/app_hu.arb del proyecto de la app).

UI = dict(
  locale='hu_HU',
  aria_home='Mando TV, főoldal', aria_main='Főmenü', nav_que='Funkciók', nav_ayuda='Súgó', nav_contacto='Kapcsolat',
  asunto='Szia%20Mando%20TV', inicio='Főoldal', privacidad='Adatvédelem', aria_pie='Oldalléc', aria_ruta='Navigációs útvonal',
  aria_marcas='Márkák és útmutatók', hecho='Chilében készült',
  aviso='A Mando TV független alkalmazás. Nem áll kapcsolatban a megnevezett tévégyártókkal, sem a Google-lel, az Amazonnal, az Apple-lel vagy a Rokuval, és ők nem támogatják. A márkák tulajdonosaik védjegyei, csak a kompatibilitás jelzésére szerepelnek. Az Android TV és a Google TV a Google LLC védjegye. Az Apple TV az Apple Inc. védjegye.',
  bajar='Ingyenes letöltés', descarga='Letöltés:', anticipada='Korai hozzáférés:',
  apple_aria='Mando TV ingyenes letöltése az App Store-ból', ms_aria='Mando TV ingyenes letöltése a Microsoft Store-ból',
  gp_aria='Mando TV korai hozzáférés a Google Playen Androidra', aria_desc='Mando TV letöltése',
  b_como_btn='Így csatlakozz', b_tiendas_label='Elérhető az áruházakban',
  b_nota='iPhone, iPad, Mac, Android és Windows. Ingyenes letöltés, reklámok nélkül. A Pro egyszeri vásárlás, előfizetés nélkül.',
  b_compat='Kompatibilis tévék', b_otras='Más márkák', b_otras_p='A Mando TV ugyanazzal az alkalmazással vezérli mindezeket a márkákat:',
  g_guias='Útmutatók', g_ver='Lépések megtekintése', g_pasos='Lépésről lépésre', g_hazlo='Így megy a Mando TV-vel',
  g_tiendas='A Mando TV univerzális távirányító a tévédhez. Töltsd le ingyen, reklámok és fiók nélkül. A Pro egyszeri, opcionális vásárlás, előfizetés nélkül. iPhone-ra, iPadre, Windowsra és Androidra:',
  g_nota='Android: ingyenes korai hozzáférés a Google Playen. <a href="{enlace}">Csatlakozz két lépésben</a>, és segíts nekünk eljutni az áruházba.',
  g_mas_pagina='További részleteket a(z) {enlace} oldalon találsz.', g_mas_marca='További részletek márkák szerint:',
  g_faq='Gyakori kérdések', g_mas='További útmutatók', g_todas='Összes útmutató', g_ayuda='Súgó és támogatás',
  g_idiomas='Ez az útmutató más nyelveken',
)

# Pie de página y listas de marcas/guías: (clave, texto)
PIE = [
  ('samsung', 'Samsung távirányító'),
  ('lg', 'LG távirányító'),
  ('roku', 'Roku távirányító'),
  ('android', 'Android TV távirányító'),
  ('guias', 'Összes útmutató'),
  ('lost-tv', 'Elveszett távirányító'),
  ('lost-lg', 'Elveszett LG távirányító'),
  ('lg-on', 'LG tévé bekapcsolása telefonnal'),
  ('hdmi', 'HDMI-bemenet váltása távirányító nélkül'),
  ('androidtv', 'Android TV távirányító nélkül'),
  ('console', 'Tévé és konzol HDMI távirányító nélkül'),
  ('samsung-lost', 'Samsung tévé távirányító nélkül'),
  ('roku-lost', 'Elveszett Roku távirányító'),
  ('roku-403', 'A Roku alkalmazás nem működik'),
  ('androidtv-code', 'Android TV párosítási kód'),
  ('not-found', 'A telefon nem találja a tévét'),
  ('wifi', 'Telefon távirányítóként Wi-Fi-n'),
  ('pc', 'Tévé vezérlése számítógéppel'),
]
NOMBRE_OTRA = {'lg': 'LG távirányító alkalmazás', 'samsung': 'Samsung távirányító alkalmazás', 'roku': 'Roku távirányító alkalmazás',
               'android': 'Android TV és Google TV távirányító alkalmazás'}
PAGINA_MARCA = {'lg': 'LG távirányító alkalmazás', 'samsung': 'Samsung távirányító alkalmazás', 'roku': 'Roku távirányító alkalmazás',
                'android': 'Android TV távirányító alkalmazás'}

OTRAS_GUIAS = [
  ('lg-on', 'LG tévé bekapcsolása telefonnal'),
  ('lost-tv', 'Elveszett távirányító: ezt teheted'),
  ('lost-lg', 'Elveszett LG távirányító: így használd a telefonod'),
  ('hdmi', 'HDMI-bemenet váltása a tévén távirányító nélkül'),
  ('androidtv', 'Android TV távirányító nélkül: így használd a telefonod'),
  ('console', 'Tévé bekapcsolása és váltás a konzol HDMI-bemenetére, távirányító nélkül'),
  ('samsung-lost', 'Samsung tévé az eredeti távirányító nélkül: így használd a telefonod'),
  ('roku-lost', 'Elveszett Roku távirányító: így használd a telefonod'),
  ('roku-403', 'A Roku alkalmazás nem működik: a 403-as hiba megoldása'),
  ('androidtv-code', 'Az Android TV párosítási kódot kér: ezt kell tenned'),
  ('not-found', 'A telefonod nem találja a tévét: ezt ellenőrizd'),
  ('wifi', 'Így használd a telefonod távirányítóként Wi-Fi-n'),
  ('pc', 'Így vezérelheted a tévédet Windows-számítógéppel'),
]

INDICE = dict(
  titulo='Útmutatók: tévé vezérlése telefonnal | Mando TV',
  desc='Útmutatók lépésről lépésre: telefon vagy számítógép mint távirányító, tévé bekapcsolása, HDMI váltása és Samsung, LG, Roku hibák megoldása.',
  h1='Útmutatók: a telefon mint távirányító',
  intro='Egyszerű lépések, hogy a Samsung, LG, Roku vagy Android TV tévéd távirányítóját összekösd a Mando TV-vel, bekapcsold a tévét és megoldd a problémákat.',
  h2_guias='Összes útmutató', h2_marcas='Távirányító alkalmazás márkák szerint',
  marcas_extra=[('sony', 'Sony távirányító alkalmazás'), ('philips', 'Philips távirányító alkalmazás')],
)

MARCAS = [
  dict(clave='lg', color='#e0457b', corto='LG',
    titulo='LG tévé távirányító alkalmazás telefonra, ingyen | Mando TV',
    desc='A telefonod vagy számítógéped LG tévé távirányítóként webOS-hez, Wi-Fi-n. Gombok, billentyűzet, appok, bemenetek és bekapcsolás ingyen; mutató Proval.',
    h1='LG tévé távirányító alkalmazás a telefonodra',
    intro='A Mando TV távirányító alkalmazás LG tévékhez: az otthoni Wi-Fi-n keresztül a telefonodból vagy számítógépedből webOS-es LG okostévéd távirányítóját csinálja. Jól jön, ha elveszett a távirányító, lemerült az elem, vagy egyszerűen gyorsabban akarsz gépelni.',
    compat='webOS-es LG okostévék (a legtöbb LG okostévé 2014 óta). LED, NanoCell, QNED és OLED tévékkel működik. A régebbi, NetCast rendszerű LG okostévék (2011 és 2014 között, a webOS előtt) újdonságként a bétában támogatottak: a tévé által kijelzett 6 számjegyű kulccsal párosíthatók.',
    h2=dict(funciones='Ezt teheted az LG tévéddel', como='Így csatlakoztasd az LG tévédet a Mando TV-hez',
            encender='LG tévé bekapcsolása telefonnal', preguntas='Kérdések az LG-ről', guias='Útmutatók LG-hez'),
    funciones=[
      ('Minden gomb', 'Iránygombok, OK, Vissza, Home, hangerő, csatornák, némítás és lejátszás.'),
      ('Mutató, mint a Magic Remote-on (Pro)', 'Az ujjaddal mozgasd a nyilat a képernyőn, pont úgy, mint az LG Magic Remote-tal.'),
      ('Két billentyűzet', 'Gépelj a tévé keresőjében és a legtöbb appban a telefonod billentyűzetével. A YouTube-billentyűzettel (Pro) írd be vagy mondd el, mit nézzél, és a YouTube megnyílik a tévén az eredményekkel.'),
      ('Appok és bemenetek', 'Nyisd meg az appjaidat, és válts HDMI-re, élő tévére, AirPlayre vagy Screen Sharere.'),
      ('Hangkimenet (Pro)', 'Válts a tévé hangszórói és a hangprojektorod között.'),
      ('Tévé bekapcsolása', 'Ha ki van kapcsolva, a Mando TV a hálózaton keresztül bekapcsolja, és magától csatlakozik.'),
    ],
    pasos=[
      'Csatlakoztasd a telefonod és a tévét ugyanarra a Wi-Fi-re.',
      'Nyisd meg a Mando TV-t: az LG tévéd magától megjelenik a listában. Koppints rá.',
      'A tévén megjelenik egy kérdés, amely engedélyt kér. Fogadd el a megszokott távirányítóddal (csak az első alkalommal).',
    ],
    encender='Kapcsold be a „Tévé bekapcsolása mobilról” opciót (egyes modelleken „Bekapcsolás Wi-Fi-n keresztül” a neve). Itt találod: Beállítások > Általános > Eszközök > Külső eszközök (régebbi modelleken Csatlakozás > Mobilcsatlakozás-kezelés). Ezután, amikor a kikapcsolt tévére koppintasz a Mando TV-ben, az alkalmazás megkérdezi, bekapcsolja-e, és magától csatlakozik.',
    faq=[
      ('Kell a Magic Remote a Mando TV használatához?', 'Csak az első alkalommal, hogy elfogadd a képernyőn megjelenő kérdést. Utána elég a telefonod.'),
      ('Kiváltja a Mando TV az LG ThinQ alkalmazást?', 'A tévé vezérlésére igen: nincs szükséged LG-fiókra, és a tévét sem kell regisztrálnod. A Mando TV közvetlenül a Wi-Fi-n keresztül csatlakozik.'),
      ('Bekapcsolhatom az LG tévémet a telefonommal?', 'Igen, ha bekapcsoltad a tévén a „Tévé bekapcsolása mobilról” opciót, és egyszer már csatlakoztál, amíg a tévé be volt kapcsolva.'),
      ('Működik a webOS előtti, régebbi LG tévékkel?', 'A bétában igen, a 2011 és 2014 közötti LG NetCast okostévékkel. A tévé által kijelzett 6 számjegyű kulccsal párosíthatók. A funkció új, és még lehetnek hibái.'),
    ],
    guias=[('lg-on', 'Így kapcsolhatod be az LG tévét telefonnal'),
           ('lost-lg', 'Elveszett LG távirányító: így használd a telefonod'),
           ('hdmi', 'HDMI-bemenet váltása a tévén távirányító nélkül'),
           ('guias', 'Összes útmutató a tévé telefonnal való vezérléséhez')]),
  dict(clave='samsung', color='#3d7bff', corto='Samsung',
    titulo='Samsung tévé távirányító alkalmazás telefonra | Mando TV',
    desc='A telefonod vagy számítógéped Samsung tévé távirányítóként Tizenhez, Wi-Fi-n. Gombok, billentyűzet, appok és bekapcsolás ingyen; érintőpad Proval.',
    h1='Samsung tévé távirányító alkalmazás a telefonodra',
    intro='A Mando TV távirányító alkalmazás Samsung tévékhez: az otthoni Wi-Fi-n keresztül a telefonodból vagy számítógépedből Samsung okostévéd távirányítóját csinálja. Nincs szükséged Samsung-fiókra, és a tévét sem kell regisztrálnod.',
    compat='Tizen rendszerű Samsung okostévék, 2016-os és újabb gyártásúak (olyan sorozatok, mint a Crystal UHD, QLED, Neo QLED, The Frame és OLED).',
    h2=dict(funciones='Ezt teheted a Samsung tévéddel', como='Így csatlakoztasd a Samsung tévédet a Mando TV-hez',
            encender='Samsung tévé bekapcsolása telefonnal', preguntas='Kérdések a Samsungról', guias='Útmutatók Samsunghoz'),
    funciones=[
      ('Minden gomb', 'Iránygombok, OK, Vissza, Home, hangerő, csatornák, némítás és forrás.'),
      ('Érintőpad (Pro)', 'Húzd az ujjadat a menükben, anélkül hogy a nyílgombokat keresnéd.'),
      ('Két billentyűzet', 'Gépelj a tévé keresőjében és a legtöbb appban a telefonod billentyűzetével. A YouTube-billentyűzettel (Pro) írd be vagy mondd el, mit nézzél, és a YouTube megnyílik a tévén az eredményekkel.'),
      ('Appok', 'Nyisd meg a Netflixet, a YouTube-ot, a Prime Videót és a többi appodat egy koppintással.'),
      ('Tévé bekapcsolása', 'Ha ki van kapcsolva, a Mando TV a hálózaton keresztül bekapcsolja, és magától csatlakozik.'),
      ('Fiók nélkül', 'A kapcsolat közvetlenül a Wi-Fi-n megy, az internet érintése nélkül.'),
    ],
    pasos=[
      'Csatlakoztasd a telefonod és a tévét ugyanarra a Wi-Fi-re.',
      'Nyisd meg a Mando TV-t: a Samsung tévéd magától megjelenik a listában. Koppints rá.',
      'A tévé megkérdezi, engedélyezed-e a kapcsolatot. A távirányítóval válaszd az „Engedélyezés” lehetőséget (csak az első alkalommal).',
    ],
    encender='Kapcsold be a Samsung tévén a Beállítások > Általános > Hálózat > Szakértői beállítások menüben a „Bekapcsolás mobilról” opciót. Ezután, amikor a kikapcsolt tévére koppintasz a Mando TV-ben, az alkalmazás megkérdezi, bekapcsolja-e, és magától csatlakozik.',
    faq=[
      ('Véletlenül elutasítottam az engedélyt. Mit tegyek?', 'Menj a tévén a Beállítások > Általános > Külső eszközök kezelője > Eszközcsatlakozás-kezelő menübe, és állítsd a Mando TV-t engedélyezettre.'),
      ('Kiváltja a Mando TV a SmartThingst?', 'A tévé vezérlésére igen, és ehhez nem kell Samsung-fiók. A Mando TV közvetlenül a Wi-Fi-n keresztül csatlakozik.'),
      ('Működik régebbi Samsung tévékkel?', 'A 2016-os és újabb, Tizen rendszerű Samsung tévékkel működik. A korábbi modellek más rendszert használnak, amelyet még nem támogatunk.'),
    ],
    guias=[('samsung-lost', 'Samsung tévé az eredeti távirányító nélkül: így használd a telefonod'),
           ('smartthings', 'SmartThings-alternatíva Samsung tévékhez'),
           ('turn-on', 'Így kapcsold be a tévét távirányító nélkül'),
           ('hdmi', 'HDMI-bemenet váltása a tévén távirányító nélkül'),
           ('guias', 'Összes útmutató a tévé telefonnal való vezérléséhez')]),
  dict(clave='roku', color='#a77bff', corto='Roku',
    titulo='Roku távirányító alkalmazás telefonra, ingyen | Mando TV',
    desc='A telefonod vagy számítógéped Roku távirányítóként Roku TV-hez és Roku lejátszóhoz, Wi-Fi-n. Gombok, billentyűzet, csatornák, bemenetek és bekapcsolás ingyen.',
    h1='Roku távirányító alkalmazás a telefonodra',
    intro='A Mando TV távirányító alkalmazás Rokuhoz: az otthoni Wi-Fi-n keresztül a telefonodból vagy számítógépedből a Rokud távirányítóját csinálja. Működik Roku TV készülékekkel és a HDMI-portra dugható Roku lejátszókkal.',
    compat='Roku TV készülékek (TCL, Hisense, Philips, Sharp, JVC és mások) és Roku lejátszók (Express, Streaming Stick, Ultra).',
    h2=dict(funciones='Ezt teheted a Rokuddal', como='Így csatlakoztasd a Rokudat a Mando TV-hez',
            encender='Roku bekapcsolása telefonnal', preguntas='Kérdések a Rokuról', guias='Útmutatók Rokuhoz'),
    funciones=[
      ('Minden gomb', 'Iránygombok, OK, Vissza, Home, hangerő, némítás, ismétlés és lejátszás.'),
      ('Két billentyűzet', 'Gépelj a Roku keresőjében és azokon a csatornákon, amelyek engedik, a telefonod billentyűzetével. A YouTube-billentyűzettel (Pro) írd be vagy mondd el, mit nézzél, és a YouTube megnyílik a tévén az eredményekkel.'),
      ('Csatornák', 'Nyisd meg a Netflixet, a YouTube-ot és a többi Roku-csatornádat egy koppintással.'),
      ('Bemenetek', 'Roku TV esetén az alkalmazásban válts HDMI-re, antennára vagy AV-re.'),
      ('Tévé bekapcsolása', 'Gyorsindítással rendelkező Roku TV készülékeket a Mando TV a telefonodról kapcsolja be.'),
      ('Párosítás nélkül', 'A Roku nem kér kódot: koppints rá a listában, és már csatlakoztál is.'),
      ('Távirányító csörgetése', 'Ha a Roku távirányítódnak van hangszórója, például a Roku Voice Remote Pro-nak, a Mando TV megcsörgeti, hogy megtaláld. Ingyenes, a Rokunak be kell lennie kapcsolva.'),
    ],
    pasos=[
      'Csatlakoztasd a telefonod és a Rokut ugyanarra a Wi-Fi-re.',
      'Nyisd meg a Mando TV-t: a Rokud magától megjelenik a listában. Koppints rá.',
      'Ha a kapcsolat nem sikerül, menj a Rokun a Beállítások > Rendszer > Speciális rendszerbeállítások > Vezérlés mobilappokkal menübe, és állítsd a hálózati hozzáférést Alapértelmezett vagy Permissive értékre (újabb Roku-szoftvernél állítsd a „Vezérlés mobilappokkal” opciót Engedélyezett értékre).',
    ],
    encender='Roku TV készüléken kapcsold be a Beállítások > Rendszer > Energia menüben a „TV gyorsindítás” opciót. A más tévéhez csatlakoztatott Roku lejátszók így nem kapcsolhatók be. Ezután, amikor a kikapcsolt tévére koppintasz a Mando TV-ben, az alkalmazás megkérdezi, bekapcsolja-e, és magától csatlakozik.',
    faq=[
      ('Működik a Roku Expresszel vagy a Streaming Stickkel?', 'Igen. Minden Roku lejátszót és Roku TV készüléket ugyanúgy vezérelhetsz.'),
      ('A Mando TV nem találja a Rokudat. Mit tegyek?', 'Ellenőrizd, hogy mindkettő ugyanazon a Wi-Fi-n van-e, és hogy a Rokun nincs-e kikapcsolva a „Vezérlés mobilappokkal”. IP-címmel is hozzáadhatod.'),
      ('Kell Roku-fiók?', 'Nem. A Mando TV közvetlenül a Wi-Fi-n keresztül csatlakozik.'),
    ],
    guias=[('roku-403', 'A Roku alkalmazás nem működik (403-as hiba)'),
           ('roku-lost', 'Elveszett Roku távirányító: így használd a telefonod'),
           ('tcl', 'TCL távirányító alkalmazás'),
           ('hisense', 'Hisense távirányító alkalmazás'),
           ('philips', 'Philips távirányító alkalmazás'),
           ('guias', 'Összes útmutató a tévé telefonnal való vezérléséhez')]),
  dict(clave='android', color='#2fbf8f', corto='Android TV és Google TV',
    titulo='Google TV és Android TV távirányító telefonra | Mando TV',
    desc='A telefonod Google TV és Android TV távirányítóként (Sony, TCL, Xiaomi), Wi-Fi-n. Gombok, billentyűzet, appok és bekapcsolás ingyen; érintőpad Proval.',
    h1='Google TV és Android TV távirányító alkalmazás a telefonodra',
    intro='A Mando TV távirányító alkalmazás Android TV-hez: az otthoni Wi-Fi-n keresztül a telefonodból vagy számítógépedből Android TV-s vagy Google TV-s tévéd távirányítóját csinálja. iPhone-ról és Windowsról is működik.',
    compat='Google TV-s vagy Android TV-s tévék a Sonytól, Philipstől, TCL-től, Hisense-től, Sharptól, Xiaomitól, Toshibától, Panasonictól, Haiertől, Skyworthtől, JVC-től, Thomsontól, Motorolától, OnePlustól, iFFALCONtól, Kogantól, Vutól és más márkáktól, valamint Chromecast Google TV-vel, Google TV Streamer, onn. és Nvidia Shield. E márkák némelyike más rendszerű modelleket is árul: ha a tévéd a Google TV kezdőképernyőjét mutatja, vagy van Google Play Áruháza, a Mando TV vezérli.',
    h2=dict(funciones='Ezt teheted az Android TV-ddel', como='Így csatlakoztasd az Android TV-det a Mando TV-hez',
            encender='Android TV bekapcsolása telefonnal', preguntas='Kérdések az Android TV-ről', guias='Útmutatók Android TV-hez'),
    funciones=[
      ('Minden gomb', 'Iránygombok, OK, Vissza, Home, hangerő, némítás és lejátszás.'),
      ('Érintőpad (Pro)', 'Húzd az ujjadat, hogy gyorsan navigálj a Google TV menüiben.'),
      ('Két billentyűzet', 'Gépelj a tévé keresőjében és a legtöbb appban a telefonod billentyűzetével. A YouTube-billentyűzettel (Pro) írd be vagy mondd el, mit nézzél, és a YouTube megnyílik a tévén az eredményekkel.'),
      ('Appok', 'Nyisd meg a YouTube-ot, a Netflixet, a Disney+-t és a többi appodat egy koppintással.'),
      ('Tévé bekapcsolása', 'A hálózaton keresztüli bekapcsolást támogató modelleknél a Mando TV bekapcsolja a tévét, és magától csatlakozik.'),
      ('iPhone, Android és számítógép', 'Minden telefonon és számítógépen ugyanúgy működik.'),
    ],
    pasos=[
      'Csatlakoztasd a telefonod és a tévét ugyanarra a Wi-Fi-re.',
      'Nyisd meg a Mando TV-t: az Android TV-d magától megjelenik a listában. Koppints rá.',
      'A tévé egy 6 karakteres kódot jelenít meg. Írd be a Mando TV-ben (csak az első alkalommal).',
    ],
    encender='Ez a gyártótól függ. A hálózati vagy energiabeállításokban keresd a „Wake on LAN”, „Bekapcsolás hálózaton keresztül”, „Hálózati készenlét” vagy „Távoli indítás” opciót. Néhány modellnek nincs ilyen opciója. Ezután, amikor a kikapcsolt tévére koppintasz a Mando TV-ben, az alkalmazás megkérdezi, bekapcsolja-e, és magától csatlakozik.',
    faq=[
      ('Működik Chromecast Google TV-vel?', 'Igen, a párosítás a képernyőn megjelenő 6 karakteres kóddal történik.'),
      ('Miben más, mint a Google TV alkalmazás?', 'A Mando TV-hez nem kell Google-fiók, Windowson is működik, és ugyanazzal az alkalmazással vezérli az LG, a Samsung és a Roku tévéket.'),
      ('A kód nem jelenik meg a képernyőn. Mit tegyek?', 'Zárd be a Mando TV-t, nyisd meg újra, és koppints ismét a tévére. Ellenőrizd, hogy a tévé nincs-e mély energiatakarékos módban.'),
    ],
    guias=[('androidtv-code', 'Az Android TV párosítási kódot kér: ezt kell tenned'),
           ('androidtv', 'Android TV távirányító nélkül: így használd a telefonod'),
           ('googletv-alt', 'A Google TV telefonos távirányítójának alternatívája'),
           ('sony', 'Sony távirányító alkalmazás'),
           ('tcl', 'TCL távirányító alkalmazás'),
           ('hisense', 'Hisense távirányító alkalmazás'),
           ('philips', 'Philips távirányító alkalmazás'),
           ('guias', 'Összes útmutató a tévé telefonnal való vezérléséhez')]),
]

GUIAS = [
  dict(clave='lost-tv', corto='Elveszett távirányító',
    titulo='Elveszett a távirányító? Vezéreld a tévét telefonnal',
    desc='Elveszett a távirányító? Kapcsold be a tévét a készüléken, és használd a telefonod távirányítóként. Lépések LG, Samsung, Roku, Android TV esetén. Ingyen.',
    h1='Elveszett a távirányító? Ezt teheted most',
    intro='Az elveszett távirányító minden háztartásban előfordul: pont akkor tűnik el, amikor nézni akarsz valamit. A jó hír: a telefonod az otthoni Wi-Fi-n keresztül ki tudja váltani a távirányítót. Íme, mit tehetsz sorban.',
    pasos=[
      'Kapcsold be a tévét a készüléken lévő gombbal. Szinte mindig alul középen vagy a hátoldalon, valamelyik sarok közelében van. Néha egyetlen gomb, néha egy kis joystick.',
      'Csatlakoztasd a telefonodat ugyanarra a Wi-Fi-re, mint a tévét.',
      'Töltsd le a Mando TV-t, amely ingyenes és nem kér fiókot, és nyisd meg az alkalmazást. A tévéd magától megjelenik a listában. Koppints rá.',
      'Erősítsd meg a kapcsolatot a márkádnak megfelelően. LG és Samsung esetén a tévé megkérdezi, engedélyezed-e: fogadd el a tévén lévő gombbal vagy joystickkal. Android TV és Google TV esetén a képernyőn megjelenő 6 karakteres kódot írod be. A Roku semmit nem kér.',
      'Kész. Az iránygombok, az OK, a Vissza, a Home, a hangerő, a csatornák és a billentyűzet ingyenesek.',
      'A következő alkalomra: kapcsold be a tévé beállításaiban a hálózaton keresztüli bekapcsolást (a márkádhoz tartozó útmutatót lent találod). Így a tévét a telefonodról is bekapcsolhatod, anélkül hogy hozzáérnél.',
    ],
    extra=[
      ('Válaszd ki a márkádhoz tartozó útmutatót', 'LG: [Elveszett LG távirányító](@lost-lg). Android TV és Google TV: [Android TV távirányító nélkül](@androidtv). Samsung: [Samsung tévé távirányító nélkül](@samsung-lost). Roku: [Elveszett Roku távirányító](@roku-lost).'),
      ('Ha a tévé nem kapcsol be a gombbal', 'Mielőtt másik távirányítót keresnél, ellenőrizd, hogy a kábel jól be van-e dugva, és van-e áram a konnektorban. Ha a tévén lévő gomb nem csinál semmit, a probléma a tévével van, nem a távirányítóval.'),
      ('Ha a távirányító egyszerűen nem működik már', 'Próbálj ki új elemeket. Azt, hogy küld-e még jelet, így ellenőrizheted: irányítsd a telefon kamerájára, és nyomj meg egy gombot. Sok telefonon lilás fényt látsz a képernyőn. Ha látod a fényt, de a tévé nem reagál, lehet, hogy a tévé érzékelője el van takarva.'),
      ('Ha routert cseréltél, és a tévének nincs többé Wi-Fi-je', 'Távirányító nélkül nehezebb új hálózatra csatlakoztatni a tévét. A legegyszerűbb, ha hálózati kábellel a routerhez dugod. Beállíthatsz olyan Wi-Fi-t is, amelynek ugyanaz a neve és jelszava, mint korábban: a tévé általában magától csatlakozik hozzá.'),
      ('Mi az ingyenes és mi a Pro', 'A tévé be- és kikapcsolása, az iránygombok, az OK, a hangerő, a csatornák, a számgombok, a billentyűzet, az appok megnyitása és a bemenet váltása ingyenes. Az érintőpad, a hang és a rutinok a Mando TV Pro részei, amely egyszeri vásárlás, előfizetés nélkül.'),
    ],
    marca=None,
    faq=[
      ('Bekapcsolhatom a tévét a telefonnal, ha még sosem csatlakoztattam?', 'Az első alkalommal a tévén lévő gombbal kapcsolod be. Miután összekötötted a telefonodat, és bekapcsoltad a tévé beállításaiban a hálózaton keresztüli bekapcsolást, az alkalmazással is be tudod kapcsolni.'),
      ('Venni kell új távirányítót?', 'Nem feltétlenül. A Mando TV-vel a gombok, a hangerő, a billentyűzet és a bekapcsolás ingyen van. Ha mégis inkább igazi távirányítót szeretnél, keresd a tévéd pontos típusát.'),
      ('Működik, ha a tévének nincs Wi-Fi-je?', 'Többnyire nem. A telefonnak és a tévének általában ugyanazon a Wi-Fi-n kell lennie. Kivétel az infravörös az infravörös adóval rendelkező Android telefonokon, amely a nem okos tévéket is vezérli, és a Bluetooth bétában Android 9-től, amely Wi-Fi nélkül működik Google TV-vel, Android TV-vel és Fire TV-vel.'),
    ]),
  dict(clave='lost-lg', corto='Elveszett LG távirányító',
    titulo='Elveszett az LG távirányító? Használd a telefonod',
    desc='Nincs LG távirányító? Kapcsold be a tévét a készüléken, fogadd el a kérdést, és használd a telefonod Wi-Fi-n. LG-fiók és reklámok nélkül.',
    h1='Elveszett LG távirányító? Így használd a telefonod',
    intro='Ha elveszett az LG távirányítód, vagy a Magic Remote már nem működik, a telefonod kiváltja a Wi-Fi-n keresztül. Ez webOS-es LG tévéken megy, vagyis szinte minden LG okostévén 2014 óta. Nincs szükséged LG-fiókra és a ThinQ alkalmazásra sem.',
    pasos=[
      'Kapcsold be a tévét az LG-logó alatti gombbal vagy a hátoldalon lévő gombbal. Sok modellen ez egy joystick: nyomd meg a menü megnyitásához, és mozgasd a kiválasztáshoz.',
      'Csatlakoztasd a telefonodat ugyanarra a Wi-Fi-re, mint a tévét.',
      'Nyisd meg a Mando TV-t, és koppints a listában az LG tévédre.',
      'A tévén megjelenik egy kérdés, amely engedélyt kér. Fogadd el a tévén lévő joystickkal vagy gombbal. Ha ezt a telefont már összekötötted, nem kérdez újra.',
      'Kész. Az iránygombok, az OK, a Vissza, a Home, a hangerő, a csatornák és a billentyűzet ingyenesek. A mutató Pro funkció.',
      'Ha az alkalmazás csatlakozott, az iránygombokkal és az OK-val nyisd meg a Beállításokat, és kapcsold be a „Tévé bekapcsolása mobilról” opciót. Az [LG tévé bekapcsolása telefonnal](@lg-on) útmutató megmutatja, hol találod.',
    ],
    extra=[
      ('Ha a tévé nem mutatja a kérdést', 'Lehet, hogy az engedély már el van mentve, vagy a telefonod másik hálózaton van. Ellenőrizd, hogy mindkettő ugyanazon a Wi-Fi-n van-e, és hogy a VPN ki van-e kapcsolva. Ha a tévé nem jelenik meg a listában, segít a [A telefonod nem találja a tévét](@not-found) útmutató.'),
      ('Ha a tévé elvesztette a Wi-Fi-jét', 'Dugd a tévét hálózati kábellel a routerhez, és magától használni fogja. Vagy állíts be olyan Wi-Fi-t, amelynek ugyanaz a neve és jelszava, mint korábban, mert a tévé általában magától csatlakozik hozzá.'),
      ('Ha a tévé egy másik bemeneten ragadt', 'Koppints a telefonodon a Bemenetek gombra, és válaszd ki a HDMI-portot. Többet olvashatsz róla a [HDMI-bemenet váltása a tévén távirányító nélkül](@hdmi) útmutatóban.'),
    ],
    marca='lg',
    faq=[
      ('Kell a Magic Remote a Mando TV használatához?', 'Csak az első alkalommal kell valami a kérdés elfogadásához, és ahhoz elég a tévén lévő gomb vagy joystick. Utána már csak a telefonodat használod.'),
      ('Kell az LG ThinQ alkalmazás?', 'Nem. A Mando TV közvetlenül a Wi-Fi-n keresztül csatlakozik, és nem kér LG-fiókot.'),
      ('Ki- és bekapcsolhatom az LG tévémet a telefonnal?', 'Kikapcsolni igen. A bekapcsoláshoz be kell kapcsolnod a tévén a „Tévé bekapcsolása mobilról” opciót, és egyszer csatlakoznod kell, amíg a tévé be van kapcsolva.'),
    ]),
  dict(clave='hdmi', corto='HDMI váltása távirányító nélkül',
    titulo='HDMI-bemenet váltása távirányító nélkül (Samsung, LG, Roku)',
    desc='HDMI-bemenet váltása távirányító nélkül Samsung, LG vagy Roku tévén: a tévén lévő gombbal vagy a telefonoddal. Induláshoz ingyen, reklámok nélkül.',
    h1='Így válts HDMI-bemenetet a tévén távirányító nélkül',
    intro='A konzol vagy a streaminglejátszó készen áll, de a tévé másik bemeneten ragadt, és a távirányító sehol sincs. A HDMI-bemenet távirányító nélküli váltásához két lehetőséged van: a tévén lévő gomb vagy a telefonod. Itt vannak a lépések Samsunghoz, LG-hez és Rokuhoz.',
    pasos=[
      'Először próbáld a legegyszerűbbet: kapcsold be a konzolt vagy a lejátszót. Ha a tévén be van kapcsolva a HDMI-CEC (Samsungnál Anynet+, LG-nél SIMPLINK a neve), a tévé magától átvált erre a bemenetre.',
      'Ha nem vált, használd a tévén lévő gombot, alul középen vagy a hátoldalon. Sok Samsung és LG tévén ez egy joystick, és megnyit egy menüt Forrás vagy Bemenetek pontokkal.',
      'Ebben a menüben válaszd ki a bemenetet: HDMI 1, HDMI 2 és így tovább. A szám annak a portnak a száma, amelybe a kábel be van dugva.',
      'Ha inkább a telefonodat használod, csatlakoztasd ugyanarra a Wi-Fi-re, nyisd meg a Mando TV-t, és koppints a tévédre.',
      'LG és Roku esetén koppints a Bemenetek gombra, és válaszd ki a HDMI-portot. Samsungnál a Bemenetek a Forrás gombot küldi el a tévének, és az iránygombokkal és az OK-val választasz.',
      'Az iránygombokkal és az OK-val a tévé kezdőképernyőjéről is eljuthatsz a bemenetekhez. Márkától és évjárattól függően Forrás, Csatlakoztatott eszközök vagy Bemenetek a nevük. Roku TV-n ezek a HDMI-csempék a kezdőképernyőn.',
    ],
    extra=[
      ('Samsung', 'Ha a tévén lévő gomb menüjében nincs Forrás pont, nyisd meg a telefonoddal a kezdőképernyő menüjét, és balra keresd a Forrást vagy a Csatlakoztatott eszközöket. A Mando TV-ben az iránygombokkal és az OK-val vezérled, amelyek ingyenesek.'),
      ('LG', 'Nyomd meg a tévén lévő joysticket, és keresd a Bemeneteket. A telefonoddal a Mando TV-ben is megnyithatod a bemenetek listáját, és rákoppinthatsz a kívánt bemenetre.'),
      ('Roku TV', 'A kezdőképernyőn minden bemenethez van egy csempe, például HDMI 1 vagy HDMI 2. Mozogj az iránygombokkal, és nyisd meg az OK-val, ingyen.'),
      ('Ha Android TV-s vagy Google TV-s tévéről van szó', 'A Mando TV-ben az Android TV bemeneteinek listája még nincs meg. Használd a tévén lévő bemenet gombot, vagy az iránygombokkal és az OK-val a kezdőképernyőről érd el a bemeneteket. Ha nincs távirányítód, és csatlakozni szeretnél, olvasd el az [Android TV távirányító nélkül](@androidtv) útmutatót.'),
      ('További segítség', 'Ha a tévé egyáltalán nem kapcsol be, vagy nem tudod, hol kezdd, olvasd el az [Elveszett távirányító](@lost-tv) útmutatót. A konzolos játékhoz a [Tévé bekapcsolása és váltás a konzol HDMI-bemenetére, távirányító nélkül](@console) útmutató tartalmazza a HDMI-CEC trükköt.'),
    ],
    marca=None,
    faq=[
      ('Ingyenes a HDMI-bemenet váltása?', 'Igen. A Mando TV bemeneti listája ingyenes, akárcsak a tévé bekapcsolása és az iránygombok, az OK és a hangerő. A bemenetekhez a tévé menüjén keresztül is eljutsz.'),
      ('Honnan tudom, melyik HDMI-bemenetre van szükségem?', 'Nézd meg a tévé HDMI-portjait: mindegyiknek van száma. Azt válaszd, amelyikbe a konzolod vagy a lejátszód kábele be van dugva.'),
      ('Mi van, ha a tévé nem kapcsol be?', 'Kapcsold be a készüléken lévő gombbal. Ha már egyszer csatlakoztattad, és bekapcsoltad a hálózaton keresztüli bekapcsolást, a telefonoddal is be tudod kapcsolni.'),
    ]),
  dict(clave='androidtv', corto='Android TV távirányító nélkül',
    titulo='Android TV távirányító nélkül: használd a telefonod',
    desc='Nincs Android TV vagy Google TV távirányítód? Csatlakoztasd a telefonod a képernyőn látható 6 karakteres kóddal. Ingyen, fiók és reklámok nélkül.',
    h1='Android TV távirányító nélkül: így használd a telefonod',
    intro='Ha elveszett az Android TV-d vagy Google TV-d távirányítója, vagy lemerült az eleme, a telefonod kiváltja. A legjobb: a csatlakozáshoz nincs szükséged a távirányítóra, mert a tévé egy kódot mutat a képernyőn, te pedig beírod a telefonodon. Működik Sony, Philips, TCL, Hisense, Sharp és Xiaomi Android TV-s tévékkel, Chromecast Google TV-vel és Nvidia Shielddel.',
    pasos=[
      'Kapcsold be a tévét a készüléken lévő gombbal. Szinte mindig alul középen vagy a hátoldalon, valamelyik sarok közelében van.',
      'Csatlakoztasd a telefonodat ugyanarra a Wi-Fi-re, mint a tévét.',
      'Töltsd le a Mando TV-t, amely ingyenes és nem kér Google-fiókot, és nyisd meg az alkalmazást. Koppints a listában a tévédre.',
      'A tévé egy 6 betűből és számból álló kódot mutat. Írd be a telefonodon, és koppints a Párosítás gombra. Ehhez nincs szükséged a távirányítóra.',
      'Most már használhatod az iránygombokat, az OK-t, a Vissza, a Home, a hangerő, a némítás gombot és a billentyűzetet. Ezek ingyenesek, akárcsak az appok listája. Az érintőpad Pro.',
      'Hogy legközelebb a telefonodról kapcsold be a tévét, keresd a hálózati vagy energiabeállításokban a „Wake on LAN”, „Bekapcsolás hálózaton keresztül”, „Hálózati készenlét” vagy „Távoli indítás” opciót.',
    ],
    extra=[
      ('Ha a tévéd nem kapcsolható be a telefonról', 'Nem minden Android TV kapcsolható be a hálózaton keresztül; ez a gyártótól és a típustól függ. Ha a tiéd nem tudja, kapcsold be a tévén lévő gombbal, és folytasd a telefonon. Kikapcsolni az alkalmazásból tudod.'),
      ('Chromecast Google TV-vel, Google TV Streamer és Shield', 'Ugyanígy csatlakoznak: ugyanaz a Wi-Fi, koppints az eszközre a listában, és írd be a kódot. Ha a tévé más bemenetet mutat, válts arra a HDMI-portra, amelyben az eszköz van, ahogy az [HDMI-bemenet váltása a tévén távirányító nélkül](@hdmi) útmutató leírja.'),
      ('Ha a kód nem jelenik meg, vagy hibásnak jelzi', 'Ellenőrizd, hogy a tévé tényleg be van-e kapcsolva, és nincs-e készenlétben. A kód minden kérésnél megváltozik: csak az utolsó működik. További részleteket az [Az Android TV párosítási kódot kér](@androidtv-code) útmutatóban találsz.'),
      ('Google alkalmazás vagy Mando TV', 'A Googlenek van saját alkalmazása, amelyhez Google-fiók kell. A Mando TV nem kér fiókot, Windowson is működik, és ugyanazzal az alkalmazással vezérli az LG, a Samsung és a Roku tévéket.'),
    ],
    marca='android',
    faq=[
      ('Kell a távirányító a telefonom párosításához?', 'Nem. A kód a tévé képernyőjén jelenik meg, te pedig beírod a telefonodon. Csak a tévét kell bekapcsolnod, szükség esetén a készüléken lévő gombbal.'),
      ('Működik Hisense-szel?', 'Android TV-s vagy Google TV-s Hisense tévékkel igen. A más rendszerű Hisense tévék nem kompatibilisek.'),
      ('Gépelhetek a telefonom billentyűzetével?', 'Igen, kettő van. Az ingyenes billentyűzet a tévé és a legtöbb app keresőjébe és szövegmezőibe gépel. A YouTube és a Netflix csak a saját képernyőn megjelenő billentyűzetét fogadja el, ezért a YouTube-hoz ott van a YouTube-billentyűzet (Pro): írd be vagy mondd el, mit szeretnél nézni, és a YouTube megnyílik a tévén az eredményekkel. A Netflixet az iránygombokkal és az OK-val használod.'),
    ]),
  dict(clave='lg-on', corto='LG tévé bekapcsolása telefonnal',
    titulo='LG tévé bekapcsolása telefonnal (útmutató)',
    desc='LG tévé bekapcsolása Wi-Fi-n telefonnal: kapcsold be a „Tévé bekapcsolása mobilról” opciót, és használd a Mando TV-t. Lépésről lépésre, ingyen.',
    h1='Így kapcsold be az LG tévét telefonnal',
    intro='Az LG tévét bekapcsolhatod a telefonnal, de ehhez előbb be kell kapcsolnod egy beállítást a tévén. Utána a telefonod a Wi-Fi-n keresztül, távirányító nélkül bekapcsolja az LG tévét. Öt percig tart, és csak egyszer kell megcsinálnod.',
    pasos=[
      'Csatlakoztasd a telefonodat és az LG tévét ugyanarra a Wi-Fi-re.',
      'Nyisd meg a tévén a Beállításokat, és keresd a „Tévé bekapcsolása mobilról” opciót. Itt találod: Beállítások > Általános > Eszközök > Külső eszközök (régebbi modelleken Csatlakozás > Mobilcsatlakozás-kezelés).',
      'Kapcsold be a „Bekapcsolás Wi-Fi-n keresztül” opciót. Ha a tévéd hálózati kábellel csatlakozik, ehelyett a kábelhez tartozó opciót kapcsold be.',
      'Ha a tévédnek van „Gyorsindítás+” funkciója, azt is kapcsold be.',
      'Bekapcsolt tévénél nyisd meg a Mando TV-t a telefonodon, és koppints a listában az LG tévédre. Fogadd el a képernyőn megjelenő kérdést. Így tanulja meg az alkalmazás, hogyan ébressze fel.',
      'Kapcsold ki a tévét, és próbáld ki: koppints a tévére a Mando TV-ben, és az alkalmazás megkérdezi, bekapcsolja-e.',
    ],
    extra=[
      ('Ha nem kapcsol be', 'A tévének ugyanazon a Wi-Fi-n kellett lennie, amikor kikapcsolták. Ellenőrizd, hogy a beállítás még aktív-e, és a telefonod ugyanazon a hálózaton van-e. Ha routert cseréltél, csatlakozz újra bekapcsolt tévénél.'),
    ],
    marca='lg',
    faq=[
      ('Bekapcsolhatom az LG tévét telefonnal, ha még sosem csatlakoztattam?', 'Nem. Előbb be kell kapcsolnod a tévén a „Tévé bekapcsolása mobilról” opciót, és egyszer csatlakoznod kell a Mando TV-vel, amíg a tévé be van kapcsolva.'),
      ('Kell az LG ThinQ alkalmazás?', 'Nem. A Mando TV közvetlenül a Wi-Fi-n keresztül csatlakozik, és nem kér LG-fiókot.'),
      ('Működik mobiladattal?', 'Nem. A telefonnak és a tévének ugyanazon a Wi-Fi-n kell lennie.'),
    ]),
  dict(clave='console', corto='Tévé és konzol távirányító nélkül',
    titulo='Nincs távirányító? Tévé bekapcsolása, HDMI váltása',
    desc='Megjelenési nap, és nincs távirányító? Kapcsold be a tévét, és válts telefonnal a PS5 vagy Xbox HDMI-bemenetére. Ingyen, reklámok nélkül.',
    h1='Így kapcsold be a tévét, és válts távirányító nélkül a konzolod HDMI-bemenetére',
    intro='A GTA VI megjelenési napja, a konzol készen áll, a távirányító pedig valahol eltűnt a kanapépárnák között. Gyakrabban előfordul, mint gondolnád. A Mando TV-vel a telefonod bekapcsolja a tévét, és az otthoni Wi-Fi-n keresztül átvált a PlayStationöd vagy Xboxod bemenetére.',
    pasos=[
      'Csatlakoztasd a telefonodat ugyanarra a Wi-Fi-re, mint a tévét.',
      'Nyisd meg a Mando TV-t, és koppints a listában a tévédre (Samsung, LG, Roku vagy Android TV).',
      'Ha a tévé ki van kapcsolva, koppints a Bekapcsolásra. Ez akkor megy, ha a tévén be van kapcsolva a hálózaton keresztüli bekapcsolás. Ha ezt sosem kapcsoltad be, ezúttal a készüléken lévő gombbal kapcsold be a tévét, és a következő alkalomra kapcsold be a funkciót.',
      'Kapcsold be a konzolt. Ha a HDMI-CEC be van kapcsolva (lásd lejjebb az ingyenes trükköt), a tévé magától átvált a konzol bemenetére.',
      'Ha nem vált, koppints a Mando TV-ben a Bemenetek gombra, és válaszd ki azt a HDMI-portot, amelybe a konzol be van dugva: HDMI 1, HDMI 2 és így tovább.',
      'Játék közben a hangerőhöz használd az alkalmazás nagy gombjait.',
    ],
    extra=[
      ('Az ingyenes trükk: hagyd, hogy a konzol átkapcsolja a tévét', 'A PS5 és az Xbox a HDMI-CEC-nek köszönhetően be tudja kapcsolni a tévét, és induláskor rögtön átugrik a saját HDMI-bemenetére. PS5-nél a Beállítások > Rendszer > HDMI > HDMI-eszközkapcsolat engedélyezése menüben találod. Xboxon nyisd meg a Beállítások > Általános > Tévé- és megjelenítési beállítások menüt, és keresd az eszközvezérlés opcióját. A tévén a funkció márkánként más nevet visel: Samsungnál Anynet+, LG-nél SIMPLINK, másoknál BRAVIA Sync vagy HDMI-vezérlés.'),
      ('Ha a tévé másik képen marad', 'Ha a konzol be van kapcsolva, de a tévé még az antennát vagy egy appot mutat, nem váltott bemenetet. Koppints a telefonodon a Bemenetek gombra, és válaszd ki a konzol HDMI-bemenetét. Vagy az iránygombokkal és az OK-val jutsz el a tévé bemeneteihez, esetleg a tévén lévő gombbal, és válaszd ki a HDMI-portot. A szám annak a portnak a száma, amelybe a konzol kábelét bedugtad.'),
      ('Ha Roku TV-ről van szó', 'A tévén lévő gomb, általában alul középen vagy a hátoldalon, bekapcsolja. Onnantól a telefonod elintézi a többit.'),
    ],
    marca=None,
    faq=[
      ('Van köze a Mando TV-nek a GTA VI-hoz?', 'Nem. A Mando TV semmilyen kapcsolatban nem áll a Rockstar Gamesszel vagy a Take-Twóval. Az alkalmazás csak abban segít, hogy ne veszíts játékidőt azért, mert nem találod a távirányítót.'),
      ('Ingyenes a HDMI-bemenet váltása?', 'Igen. A Mando TV bemeneti listája ingyenes, akárcsak a tévé bekapcsolása és az iránygombok, az OK és a hangerő. A konzolt a HDMI-CEC-cel is megkérheted, hogy magától váltson bemenetet.'),
      ('Működik a tévémmel?', 'Működik Samsung, LG, Roku és Android TV tévékkel ugyanazon a Wi-Fi-n. Ha a tiéd más márkájú, a HDMI-CEC trükk akkor is segíthet.'),
      ('Használhatom a GTA VI (GTA 6) játékához PS5-ön vagy Xboxon?', 'A Mando TV sem a konzolba, sem a játékba nem avatkozik be. Csak azt biztosítja, hogy a tévé be legyen kapcsolva a megfelelő HDMI-bemeneten, hogy leülhess és játszhass.'),
    ]),
  dict(clave='samsung-lost', corto='Samsung tévé távirányító nélkül',
    titulo='Elveszett a Samsung távirányító? Használd a telefonod',
    desc='Elveszett vagy elromlott a Samsung távirányító? Használd a telefonod Wi-Fi-n Tizen tévékhez. Egyszerűen a Mando TV-vel, ingyen, reklámok nélkül.',
    h1='Samsung tévé az eredeti távirányító nélkül: így használd a telefonod',
    intro='Ha elveszett a Samsung távirányítód, vagy már nem működik, a telefonodat a Wi-Fi-n keresztül távirányítóként használhatod. Működik a 2016-os és újabb gyártású, Tizen rendszerű Samsung tévékkel.',
    pasos=[
      'Kapcsold be a tévét a készüléken lévő gombbal. A legtöbb modellen alul vagy a hátoldalon van, néha kis joystickként.',
      'Ellenőrizd, hogy a tévé csatlakozik-e a Wi-Fi-dhez, és a telefonod ugyanazon a hálózaton van-e.',
      'Nyisd meg a Mando TV-t a telefonodon. A Samsung tévéd magától megjelenik a listában. Koppints rá.',
      'A tévé arra kér, hogy erősítsd meg a kapcsolatot. A legtöbb modellen a tévén lévő gombokkal vagy a hátoldali joystickkal erősíted meg.',
      'Kész, most már használhatod a telefonodat távirányítóként. A gombok, a billentyűzet és az appok ingyenesek; az érintőpad Pro funkció.',
      'Hogy legközelebb a telefonodról kapcsold be a tévét, menj a Beállítások > Általános > Hálózat > Szakértői beállítások menübe, és kapcsold be a „Bekapcsolás mobilról” opciót.',
    ],
    extra=[
      ('Ha a tévé nem kér engedélyt', 'Lehet, hogy az engedély már el van mentve, vagy a tévé másik Wi-Fi-n van. Zárd be a Mando TV-t, és nyisd meg újra bekapcsolt tévénél. Ha a tévé 2016-nál régebbi, más rendszert használ, amelyet még nem támogatunk.'),
      ('Ha véletlenül elutasítottad az engedélyt', 'Menj a tévén a Beállítások > Általános > Külső eszközök kezelője > Eszközcsatlakozás-kezelő menübe, és állítsd a Mando TV-t engedélyezettre. Ha a telefonod ennek ellenére sem találja a tévét, olvasd el a [A telefonod nem találja a tévét](@not-found) útmutatót.'),
    ],
    marca='samsung',
    faq=[
      ('Hogyan erősítem meg a kapcsolatot, ha nincs távirányítóm?', 'A legtöbb modellen a tévén lévő gombokkal vagy a hátoldali joystickkal. Ha a te modelledon nincsenek gombok, írj a hola@mandotv.app címre, és segítünk.'),
      ('Kér a Mando TV Samsung-fiókot?', 'Nem. A kapcsolat közvetlenül a Wi-Fi-n megy, Samsung-fiók nélkül.'),
      ('Működik a régebbi Samsung tévémmel?', 'A 2016-os és újabb, Tizen rendszerű Samsung tévékkel működik.'),
    ]),
  dict(clave='wifi', corto='Telefon távirányítóként Wi-Fi-n',
    titulo='Telefon mint távirányító: tévé vezérlése Wi-Fi-n',
    desc='Csatlakoztasd a telefonod Wi-Fi-n a tévédhez, és használd távirányítóként Samsung, LG, Roku és Google TV esetén. Lépések márkánként a Mando TV-vel. Ingyen.',
    h1='Így csatlakoztasd a telefonodat Wi-Fi-n távirányítóként a tévédhez',
    intro='Csak a telefonodra és a tévédre van szükséged ugyanazon a Wi-Fi-n, valamint egy távirányító alkalmazásra. A Mando TV magától megtalálja a tévédet, és működik Samsunggal, LG-vel, Rokuval, Google TV-vel és Android TV-vel.',
    pasos=[
      'Csatlakoztasd a telefonodat és a tévét ugyanarra a Wi-Fi-re.',
      'Nyisd meg a Mando TV-t. A tévéd magától megjelenik a listában. Koppints rá.',
      'Erősítsd meg a kapcsolatot a márkádnak megfelelően (a részleteket lejjebb találod).',
      'Vezéreld a tévét a gombokkal vagy a telefonod billentyűzetével. Az érintőpad Pro funkció.',
    ],
    extra=[
      ('Samsung', 'A tévé megkérdezi, engedélyezed-e a kapcsolatot. Az első alkalommal erősítsd meg a képernyőn. Működik a 2016-os és újabb Tizen tévékkel. Hogy a telefonodról kapcsold be, kapcsold be a Beállítások > Általános > Hálózat > Szakértői beállítások menüben a „Bekapcsolás mobilról” opciót.'),
      ('LG', 'A tévén megjelenik egy kérdés, amely engedélyt kér. Az első alkalommal fogadd el. Hogy a telefonodról kapcsold be, keresd a beállításokban a „Tévé bekapcsolása mobilról” opciót, és kapcsold be a „Bekapcsolás Wi-Fi-n keresztül” lehetőséget.'),
      ('Roku', 'A Roku nem kér párosítást: koppints rá a listában, és már csatlakoztál is. A bekapcsoláshoz kapcsold be a Beállítások > Rendszer > Energia menüben a „TV gyorsindítás” opciót.'),
      ('Google TV és Android TV', 'A tévé egy kódot mutat a képernyőn. Az első alkalommal írd be a Mando TV-ben. A bekapcsoláshoz keresd a beállításokban a „Wake on LAN”, „Bekapcsolás hálózaton keresztül” vagy „Hálózati készenlét” opciót.'),
    ],
    marca=None,
    faq=[
      ('Kell internet ahhoz, hogy a telefonom távirányító legyen?', 'A telefonodnak és a tévének ugyanazon a Wi-Fi-n kell lennie. A Mando TV ezen a hálózaton keresztül közvetlenül csatlakozik a tévédhez.'),
      ('Miért nem jelenik meg a tévém a listában?', 'Ellenőrizd, hogy a tévé be van-e kapcsolva, és a telefonod nem mobiladatot vagy másik Wi-Fi-t használ-e. Néhány routernek van vendéghálózata, amely elszigeteli egymástól az eszközöket.'),
      ('Használhatom a Mando TV-t iPhone-on vagy Android telefonon?', 'iPhone-on és iPaden igen: az alkalmazás már az App Store-ban van. Windowsra a Microsoft Store-ban is megtalálható. Az Android hamarosan jön: csatlakozhatsz az ingyenes korai hozzáféréshez a Google Playen.'),
    ]),
  dict(clave='pc', corto='Tévé vezérlése számítógéppel',
    titulo='Tévé vezérlése Windows-számítógéppel (ingyen)',
    desc='Használd a Windows-gépedet távirányítóként Samsung, LG, Roku vagy Google TV-hez Wi-Fi-n. Gombok, billentyűzet és appok ingyen; PC-s parancsok Proval.',
    h1='Így vezérelheted a tévédet Windows-számítógéppel',
    intro='Ha a napot a számítógép előtt töltöd, nem kell a távirányítót keresned: a Mando TV Windowsra az otthoni Wi-Fi-n keresztül vezérli a Samsung, LG, Roku, Google TV vagy Android TV tévédet. Kényelmes appváltáshoz, hangerőállításhoz, vagy ha a YouTube-on a számítógép billentyűzetével szeretnél gépelni.',
    pasos=[
      'Töltsd le ingyen a Mando TV-t a Microsoft Store-ból a Windows 10-es vagy 11-es számítógépedre.',
      'Ellenőrizd, hogy a számítógép és a tévé ugyanazon a hálózaton van-e (Wi-Fi vagy kábel, de ugyanazon a routeren).',
      'Nyisd meg a Mando TV-t: a tévéd magától megjelenik a listában. Koppints vagy kattints rá.',
      'Az első alkalommal erősítsd meg a kapcsolatot a tévé képernyőjén (Google TV és Android TV esetén a tévé által mutatott kódot írod be).',
      'Kész: használd a gombokat vagy a billentyűzetet, hogy gépelj a tévé keresőmezőjében. Az érintőpad Pro funkció.',
    ],
    extra=[
      ('Billentyűparancsok a számítógépen (Pro)', 'A Mando TV Proval a tévét a számítógép billentyűzetével vezérled: nyílbillentyűk a navigáláshoz, Enter az OK-hoz, Backspace vagy Esc a Visszához, + és - a hangerőhöz, M a némításhoz és szóköz a szünethez.'),
      ('Mini távirányító mindig előtérben (Pro)', 'Tarts egy kis ablakot a távirányítóval mindig láthatóan, miközben dolgozol vagy a számítógépen játszol.'),
      ('Beszélj a tévével a számítógépről (Pro)', 'A Mando TV Proval a számítógép mikrofonján keresztül adsz parancsot a tévének: „nyisd meg a YouTube-ot”, „hangosabban” vagy „kapcsolj ki 30 perc múlva”, úgy, ahogy beszélsz. Windowson a beszédfelismerés magán a számítógépen történik: nincs szükséged internetre, nem kell semmit átállítanod a Windows beállításaiban, és az alkalmazás mind a 6 nyelvén működik. Amit mondasz, nem hagyja el a számítógépet, és nem kerül mentésre. Csak nagyon régi processzoroknál esik vissza az alkalmazás a Windows diktálására. Ehhez az adatvédelmi beállításokban be kell kapcsolni az online beszédfelismerést, és a Windowshoz hozzá kell adni a magyar (Magyarország) nyelvet. Ha ilyenkor valami hiányzik, az alkalmazás szól, és egy gombbal megnyitja a beállítást.'),
    ],
    marca=None,
    faq=[
      ('Kell kábel vagy Bluetooth a tévé számítógépes vezérléséhez?', 'Nem. A Mando TV az otthoni hálózaton keresztül csatlakozik: a számítógépnek és a tévének csak ugyanahhoz a routerhez kell kapcsolódnia.'),
      ('Működik minden tévével?', 'Működik Tizen rendszerű Samsung tévékkel (2016-os és újabb), webOS-es LG-vel, Rokuval, valamint Google TV-vel vagy Android TV-vel (Sony, Philips, TCL, Hisense, Sharp, Xiaomi, Toshiba, Panasonic, Haier, Skyworth és mások).'),
      ('Mennyibe kerül?', 'A gombok, a billentyűzet és a hálózaton keresztüli bekapcsolás ingyenes és reklámmentes. A Mando TV Pro egyszeri vásárlás, előfizetés nélkül, olyan extrákért, mint az érintőpad, a PC-s billentyűparancsok és a mini távirányító.'),
      ('Miért nem ért meg a mikrofon Windowson?', 'Ellenőrizd, hogy a hangfunkció aktív-e (a Pro része), és működik-e a számítógép mikrofonja a Windowsban. Szinte minden számítógépen a beszédfelismerés magán az eszközön történik, internet nélkül. Csak nagyon régi processzoroknál használja az alkalmazás a Windows diktálását. Ilyenkor ellenőrizd, hogy az online beszédfelismerés be van-e kapcsolva a Windows adatvédelmi beállításaiban, és hogy a Windowsban a magyar (Magyarország) nyelv hozzá van-e adva a nyelvi beállításokhoz. A Mando TV ezt a nyelvet csak addig használja, amíg hallgat.'),
    ]),
  dict(clave='roku-403', corto='A Roku alkalmazás nem működik',
    titulo='Nem működik a Roku alkalmazás? A 403-as hiba megoldása',
    desc='A telefon csatlakozott, de a Roku nem reagál? Kapcsold be a „Vezérlés mobilappokkal” opciót 5 lépésben, és használd újra a telefonod távirányítóként.',
    h1='A Roku alkalmazás nem működik: így oldd meg a problémát',
    intro='Ha a telefonod megtalálja a Rokut, és csatlakozik, de egyetlen gomb sem csinál semmit, szinte mindig a Rokun lévő egyik beállítás okozza, amely blokkolja a távirányító alkalmazásokat. Az újabb Roku-verziók alapértelmezetten szigorúbbak. A Roku menüjében ez egy perc alatt megoldható.',
    pasos=[
      'Nyomd meg a Rokun a Home gombot, és menj a Beállításokhoz.',
      'Nyisd meg a Rendszert, majd a Speciális rendszerbeállításokat.',
      'Menj a „Vezérlés mobilappokkal” pontra. Néhány modellen „Külső vezérlés” a neve.',
      'A „Hálózati hozzáférés” alatt válaszd az Alapértelmezett vagy a Permissive értéket. Ha a te modelleden ez csak egy kapcsoló, hagyd Engedélyezettre.',
      'Térj vissza a telefonodon a Mando TV-hez, és koppints a Rokudra. A gombok most már reagálnak.',
    ],
    extra=[
      ('Így ismered fel, hogy ez a problémád', 'A jel egyértelmű: a telefonod látja a Rokut a listában, és csatlakozik, de nem történik semmi, amikor egy gombra koppintasz. Belül a Roku 403-as hibával válaszol, ami azt jelenti: „tiltott”. A Mando TV ezt csatlakozáskor felismeri, és pontosan ezeket a lépéseket mutatja a képernyőn.'),
      ('Alapértelmezett vagy Permissive, melyiket válasszam?', 'Az Alapértelmezett elég: elfogadja az otthoni hálózatodról érkező parancsokat, és a távirányítónak ennyi kell. A Permissive nyitottabb, és csak szokatlan hálózatokon van rá szükség.'),
      ('Ha nincs meg a Roku távirányító', 'Ha a beállítás Letiltott értéken áll, csak az igazi Roku távirányítóval módosítható. Kérj kölcsön egyet, hogy egyszer átállítsd; utána mindent a telefonoddal csinálhatsz. Olvasd el az [Elveszett Roku távirányító](@roku-lost) útmutatót is.'),
    ],
    marca='roku',
    faq=[
      ('Miért nem reagál a Rokum, pedig korábban működött?', 'Egy Roku-frissítés szigoríthatja ezt a beállítást. Nem a telefonoddal vagy a Wi-Fi-vel van baj: csak újra engedélyezned kell az appokkal való vezérlést.'),
      ('Ez a Roku TV-re és a Roku lejátszókra is vonatkozik?', 'Igen. A beállítás a Roku lejátszókon és a Roku TV készülékeken ugyanabban a menüben van.'),
      ('Biztonságos, ha Alapértelmezetten hagyom a beállítást?', 'Igen. Csak az otthoni hálózatodon lévő eszközök parancsait fogadja el.'),
    ]),
  dict(clave='not-found', corto='A telefon nem találja a tévét',
    titulo='A telefon nem találja a tévét? 6 ellenőrizni való',
    desc='A távirányító alkalmazás nem találja a tévédet? Ellenőrizd a Wi-Fi-t, a VPN-t és a helyi hálózathoz való hozzáférést. Samsung, LG, Roku és Android TV esetén.',
    h1='A telefonod nem találja a tévét: ezt ellenőrizd',
    intro='Megnyitod a távirányító alkalmazást, és üres a lista, vagy a tévé megjelenik, de a kapcsolat megszakad. Szinte mindig a hálózattal van a baj, nem a tévével. Ellenőrizd ezeket a pontokat sorban: az első a legtöbb esetet megoldja.',
    pasos=[
      'Nézd meg, melyik Wi-Fi-n van a telefonod, és melyiken a tévé. Ugyanannak a hálózatnak kell lennie, ugyanazzal a névvel. A vendéghálózat nem működik, mert elszigeteli egymástól az eszközöket.',
      'Kapcsold ki a VPN-t a telefonodon, ha használsz. Bekapcsolt VPN-nél a telefonod másik hálózaton keresztül megy az internetre, és nem látja az otthoni eszközöket, vagy a kapcsolat néhány másodperc után megszakad.',
      'Kapcsold ki rövid időre a mobiladatot. Néhány telefon gyenge jelnél magától átvált a Wi-Fi-ről mobiladatra.',
      'Kapcsold be a tévét, és várd meg, amíg teljesen elindul. A kikapcsolt tévé nem válaszol a keresésre.',
      'iPhone-on ellenőrizd, hogy az alkalmazásnak van-e „Helyi hálózat” engedélye: Beállítások > Adatvédelem és biztonság > Helyi hálózat.',
      'Ha még mindig nem jelenik meg, add hozzá kézzel: koppints a Mando TV-ben a „Hozzáadás IP-címmel” gombra, és írd be a tévé IP-címét.',
    ],
    extra=[
      ('Hagyd, hogy az alkalmazás vezessen', 'A tévék listájában van egy gomb arra az esetre, ha a tévéd nem jelenik meg. Az alkalmazás lépésről lépésre ellenőrzi a leggyakoribb okokat (azonos Wi-Fi, VPN, helyi hálózati engedély és más), és minden javítás után megjelenít egy gombot az újraellenőrzéshez. A segéd ingyenes.'),
      ('Hol találod a tévé IP-címét', 'A tévé hálózati menüjében van, és modellenként kicsit más. LG-n: Beállítások, Hálózat, Wi-Fi-kapcsolat, Speciális Wi-Fi-beállítások. Samsungon: Beállítások, Általános, Hálózat, Hálózat állapota, IP-beállítások. Rokun: Beállítások, Hálózat, Névjegy. Android TV-n és Google TV-n: Beállítások, Hálózat és internet, majd koppints a hálózatodra. Ez egy olyan szám, mint a 192.168.1.86.'),
      ('Ha megjelenik, de a kapcsolat megszakad', 'Ha a kapcsolat néhány másodperc után megszakad, az ok általában a telefonnál van: VPN, másik Wi-Fi-re váltás vagy energiatakarékos mód. Kapcsold ki a VPN-t, maradj ugyanazon a Wi-Fi-n, és próbáld újra.'),
      ('2,4 és 5 GHz-es Wi-Fi', 'Nem számít, hogy a telefonod az 5 GHz-es, a tévé pedig a 2,4 GHz-es hálózaton van-e, amíg mindkettő ugyanattól a routertől jön. Ha van Wi-Fi-jelismétlőd, és a tévé ennek ellenére nem jelenik meg, menj a telefonoddal közelebb a fő routerhez, és próbáld újra.'),
    ],
    marca=None,
    faq=[
      ('Vezérelhetem a tévét mobiladattal?', 'Nem. A távirányító jele az otthoni Wi-Fi-n megy, ezért a telefonnak és a tévének ugyanazon a hálózaton kell lennie.'),
      ('Miért nem működik bekapcsolt VPN-nel?', 'Mert a VPN a telefon teljes forgalmát másik hálózaton vezeti át, és a telefon nem látja többé az otthoni eszközöket. Kapcsold ki, amíg a távirányítót használod.'),
      ('Működik Bluetooth-szal vagy infrával?', 'Okostévéknél a Mando TV a Wi-Fi-t használja. Az infra csak infravörös adóval rendelkező Android telefonokon működik, és az olyan tévékhez való, amelyek nem okostévék. A Bluetooth a bétában elérhető, ingyenes és csak Android 9-től: a telefon Bluetooth-billentyűzetként és távirányítóként csatlakozik a tévéhez, Wi-Fi nélkül. Működik Google TV-vel, Android TV-vel és Fire TV-vel; más márkáknál, amelyek elfogadnak Bluetooth-billentyűzetet, működhet, a Roku nem fogadja el.'),
    ]),
  dict(clave='androidtv-code', corto='Android TV párosítási kód',
    titulo='Az Android TV párosítási kódot kér: ezt kell tenned',
    desc='Az Android TV-d vagy Google TV-d csatlakozáskor egy 6 karakteres kódot mutat. Így írod be, és ezt tedd, ha nem jelenik meg vagy hibás.',
    h1='Az Android TV párosítási kódot kér: ezt kell tenned',
    intro='Amikor először csatlakoztatod a telefonodat egy Android TV-hez vagy Google TV-hez, a tévé egy 6 karakteres kódot mutat a képernyőn. Ez normális, és csak egyszer fordul elő: így biztos, hogy rajtad kívül senki nem vezérelheti a tévédet. Itt látod, hogyan írd be, és mit tegyél, ha nem jelenik meg.',
    pasos=[
      'Kapcsold be a tévét, és hagyd láthatóan a kezdőképernyőt.',
      'Nyisd meg a Mando TV-t a telefonodon, ugyanazon a Wi-Fi-n, mint a tévé, és koppints a listában a tévédre.',
      'Nézd a tévé képernyőjét: megjelenik egy 6 betűből és számból álló kód.',
      'Pontosan úgy írd be a telefonodon, ahogy látod, és koppints a Párosítás gombra. A betűk csak A-tól F-ig mennek, ezért egy kerek karakter mindig a nulla szám.',
      'Kész. A tévé megjegyzi a telefonodat, és nem kéri újra a kódot.',
    ],
    extra=[
      ('Ha a kód nem jelenik meg a tévén', 'Ellenőrizd, hogy a tévé tényleg be van-e kapcsolva, és nincs-e készenlétben, és hogy a telefonod ugyanazon a Wi-Fi-n van-e. Koppints újra a telefonodon a tévére. Ha még mindig nem jelenik meg, indítsd újra a tévét: húzd ki a dugót tíz másodpercre, dugd vissza, és próbáld újra.'),
      ('Ha a kódot hibásnak jelzi', 'A kód minden kérésnél megváltozik. Ha sokáig tartott, vagy kétszer kérted, csak a képernyőn látható utolsó működik. Koppints újra a telefonodon a tévére, és írd be az új kódot.'),
      ('Ha a tévé újra kéri a kódot', 'Ez akkor történik, ha a tévét gyári beállításokra állították vissza, vagy törlöd az alkalmazás adatait a telefonodon. Párosíts újra, és el lesz mentve. Ha egyáltalán nincs távirányítód, olvasd el az [Android TV távirányító nélkül](@androidtv) útmutatót.'),
    ],
    marca='android',
    faq=[
      ('Melyik tévék használják ezt a kódot?', 'Az Android TV-sek vagy Google TV-sek: Sony, Philips, TCL, Hisense, Sharp, Xiaomi, Chromecast Google TV-vel és még néhány.'),
      ('Kell Google-fiók a telefonomon?', 'Nem. A képernyőn lévő kód minden, amire szükséged van.'),
      ('Biztonságos ez?', 'Igen. A kód bizonyítja, hogy a tévé előtt ülsz: senki nem tud párosítani anélkül, hogy látná a képernyőn.'),
    ]),
  dict(clave='roku-lost', corto='Elveszett Roku távirányító',
    titulo='Elveszett a Roku távirányító? Használd a telefonod Wi-Fi-n',
    desc='Elveszett a Roku távirányító? A telefonod kiváltja Wi-Fi-n. Egyszerű lépések, akkor is, ha routert cseréltél, és a Rokunak nincs Wi-Fi-je.',
    h1='Elveszett Roku távirányító: így használd a telefonod',
    intro='Ha elveszett a Roku távirányítód, vagy már nem működik, a telefonod kiváltja, amíg a Roku még csatlakozik a Wi-Fi-dhez. És ha Wi-Fi-t vagy routert cseréltél, arra is van kiút.',
    pasos=[
      'Először próbáld megcsörgetni a távirányítót. Ha a Roku távirányítódnak van hangszórója, például a Roku Voice Remote Pro-nak, nyisd meg a Mando TV-t, csatlakozz a Rokuhoz, és használd a távirányító csörgetésének opcióját, hogy megtaláld. Ez csak hangszórós Roku távirányítókkal megy, és a Rokunak be kell lennie kapcsolva.',
      'Kapcsold be a tévét, és hagyd a Rokut csatlakoztatva. Nem kell hozzányúlnod.',
      'Csatlakoztasd a telefonodat ugyanarra a Wi-Fi-re, amelyet a Roku használ.',
      'Nyisd meg a Mando TV-t. A Roku magától megjelenik a listában. Koppints rá.',
      'Használd az iránygombokat, az OK-t, a Home-ot és a Vissza gombot, mint a megszokott távirányítóddal. A Roku nem kér kódot.',
      'Ha a gombok nem csinálnak semmit, a Roku blokkolja az appokkal való vezérlést: a [A Roku alkalmazás nem működik](@roku-403) útmutató elmagyarázza, hogyan engedélyezd.',
    ],
    extra=[
      ('Ha a Rokunak nincs Wi-Fi-je (routert cseréltél vagy költöztél)', 'Távirányító nélkül nem jutsz el a menübe, hogy beállítsd az új hálózatot, de van egy trükk: a Roku magától csatlakozik egy olyan hálózathoz, amelynek ugyanaz a neve és jelszava, mint a réginek. Állíts be egy másik telefonon Wi-Fi-hotspotot pontosan ezzel a névvel és jelszóval, csatlakoztasd hozzá a Mando TV-s telefont, és a Roku megjelenik a listában. Innen menj a Beállítások, Hálózat pontra, és csatlakoztasd az új Wi-Fi-re.'),
      ('Ha Roku TV-ről van szó', 'A Roku TV készülékeken van egy gomb a készüléken, szinte mindig alul középen vagy a hátoldalon, amely bekapcsolja a tévét. Ez elég a bekapcsoláshoz, és onnan a telefonoddal folytathatod.'),
      ('Ha inkább másik távirányítót vennél', 'Figyelj rá, hogy illeszkedjen a modelledhez. A tévé mögött lévő kis Roku lejátszókhoz infravörös nélküli távirányító kell, mert az infravörös nem éri el őket.'),
    ],
    marca='roku',
    faq=[
      ('Be tudja kapcsolni a telefonom a Rokut?', 'A csatlakoztatott Roku lejátszó mindig be van kapcsolva. Roku TV esetén a Mando TV Wi-Fi-n kapcsolja be, ha a Beállítások > Rendszer > Energia menüben be van kapcsolva a „TV gyorsindítás”.'),
      ('És a hangerő?', 'Roku TV-n a telefonod állítja a hangerőt fel és le. HDMI-n csatlakoztatott Roku lejátszónál ez a tévétől függ: sokon működik, máson nem.'),
      ('Kell fiókot létrehoznom?', 'Nem. A Mando TV nem kér fiókot, és ugyanazzal az alkalmazással vezérli a Samsung, LG és Android TV tévéket is.'),
    ]),
]

SOPORTE = dict(
  titulo='Súgó: tévé csatlakoztatása és bekapcsolása a Mando TV-vel',
  desc='Így csatlakoztasd a Mando TV távirányítót LG, Samsung, Roku vagy Android TV tévéhez, kapcsold be a tévét a telefonodról, és oldd meg a problémákat.',
  h1='Súgó',
  intro='A leggyakoribb kérdések a lépések sorrendjében. Ha nem találod a sajátodat, írj nekünk a <a href="mailto:hola@mandotv.app?subject=Seg%C3%ADts%C3%A9g%20a%20Mando%20TV-hez">hola@mandotv.app</a> címre, és válaszolunk.',
)
SOPORTE_HTML = '''      <h2 id="encontrar">A tévé megtalálása</h2>
      <div class="preguntas">
        <details open><summary>A tévém nem jelenik meg a listában</summary>
          <ol>
            <li>Ellenőrizd, hogy a telefonod és a tévé ugyanazon a Wi-Fi-n van-e. Ha a routerednek van 2,4 GHz-es és 5 GHz-es hálózata különböző nevekkel, néha nem látják egymást.</li>
            <li>Győződj meg róla, hogy a tévé be van kapcsolva.</li>
            <li>iPhone-on ellenőrizd, hogy a Mando TV-nek van-e „Helyi hálózat” engedélye, a Beállítások, Mando TV alatt.</li>
            <li>Koppints a tévék listájában arra a gombra, amely arra az esetre való, ha a tévéd nem jelenik meg: az alkalmazás lépésről lépésre ellenőrzi a leggyakoribb okokat (azonos Wi-Fi, VPN, helyi hálózati engedély és más), és minden javítás után megjelenít egy gombot az újraellenőrzéshez.</li>
            <li>Ha még mindig nem jelenik meg, koppints a + gombra, válaszd ki a márkát, és írd be a tévé IP-címét. A tévé hálózati menüjében látod (például 192.168.1.50).</li>
          </ol>
        </details>
        <details><summary>Működik mobiladattal vagy távolról?</summary>
          <p>Nem. A Mando TV az otthoni hálózatodon belül kommunikál a tévével, ezért a telefonodnak ehhez a Wi-Fi-hez kell csatlakoznia.</p>
        </details>
      </div>

      <h2 id="conectar">Az első csatlakozás</h2>
      <p>Teljes útmutatók márkák szerint: <a href="@@R_lg@@">LG</a>, <a href="@@R_samsung@@">Samsung</a>, <a href="@@R_roku@@">Roku</a> és <a href="@@R_android@@">Android TV</a>.</p>
      <div class="preguntas">
        <details><summary>LG</summary>
          <p>Amikor a tévére koppintasz, a képernyőn megjelenik egy kérdés, amely engedélyt kér. Fogadd el a megszokott távirányítóddal. Ezt csak egyszer kell megtenned.</p>
        </details>
        <details><summary>Samsung</summary>
          <p>A tévé megkérdezi, engedélyezed-e a Mando TV csatlakozását. A távirányítóval válaszd az „Engedélyezés” lehetőséget. Ha véletlenül elutasítottad, menj a Beállítások > Általános > Külső eszközök kezelője > Eszközcsatlakozás-kezelő menübe, és állítsd engedélyezettre.</p>
        </details>
        <details><summary>Roku</summary>
          <p>A Roku nem kér engedélyt. Ha a kapcsolat nem sikerül, menj a Rokun a Beállítások > Rendszer > Speciális rendszerbeállítások > Vezérlés mobilappokkal menübe, és hagyd a hálózati hozzáférést Alapértelmezett vagy Permissive értéken (újabb Roku-szoftvernél állítsd a „Vezérlés mobilappokkal” opciót Engedélyezett értékre).</p>
        </details>
        <details><summary>Android TV és Google TV</summary>
          <p>A tévé egy 6 karakteres kódot mutat. Pontosan úgy írd be a Mando TV-ben, ahogy megjelenik. Működik Sony, Philips, TCL, Hisense, Sharp, Xiaomi, Chromecast Google TV-vel és más Android TV-s eszközökkel.</p>
        </details>
      </div>

      <h2 id="encender">A tévé bekapcsolása az alkalmazásból</h2>
      <p>A Mando TV az otthoni hálózaton keresztül kapcsolja be a tévét. Ehhez két dolog kell: legalább egyszer csatlakoztál bekapcsolt tévénél, és a tévén be van kapcsolva a hálózaton keresztüli bekapcsolás. A beállítás neve típusonként változik; ezek a leggyakoribbak:</p>
      <div class="preguntas">
        <details><summary>LG</summary>
          <p>Keresd a „Tévé bekapcsolása mobilról” (vagy „Bekapcsolás Wi-Fi-n keresztül”) opciót itt: Beállítások > Általános > Eszközök > Külső eszközök (régebbi modelleken Csatlakozás > Mobilcsatlakozás-kezelés), és kapcsold be.</p>
        </details>
        <details><summary>Samsung</summary>
          <p>Kapcsold be a „Bekapcsolás mobilról” opciót a Beállítások > Általános > Hálózat > Szakértői beállítások menüben.</p>
        </details>
        <details><summary>Roku</summary>
          <p>Roku TV készülékeken kapcsold be a „TV gyorsindítás” opciót a Beállítások > Rendszer > Energia menüben. A tévéhez csatlakoztatott Roku lejátszók így nem kapcsolhatók be.</p>
        </details>
        <details><summary>Android TV és Google TV</summary>
          <p>Ez a gyártótól függ. A hálózati vagy energiabeállításokban keresd a „Wake on LAN”, „Bekapcsolás hálózaton keresztül”, „Hálózati készenlét” vagy „Távoli indítás” opciót. Néhány modellnek nincs ilyen opciója.</p>
        </details>
      </div>

      <h2 id="falla">Ha valami nem működik</h2>
      <div class="preguntas">
        <details><summary>A kapcsolat megszakad, vagy nincs reakció</summary>
          <ol>
            <li>Koppints a távirányító képernyőjén az Újracsatlakozás gombra.</li>
            <li>Ha ez nem segít, zárd be a Mando TV-t, és nyisd meg újra.</li>
            <li>Ha a tévé másik IP-címet kapott, töröld a listából, és add hozzá újra.</li>
          </ol>
        </details>
        <details><summary>Így küldhetsz hibajelentést</summary>
          <ol>
            <li>Koppints a Mando TV-ben a Testreszabás gombra (a csúszkák felül).</li>
            <li>Koppints a Tesztjelentés másolása gombra.</li>
            <li>Illeszd be a tévéd márkájával és típusával együtt egy e-mailbe a hola@mandotv.app címre.</li>
          </ol>
          <p>A jelentés nem tartalmaz jelszavakat, kódokat és semmit, amit begépelsz.</p>
        </details>
        <details><summary>Megvettem a Prót, és nem jelenik meg</summary>
          <p>Koppints a Testreszabás alatt a Vásárlás visszaállítása gombra, ugyanazzal az áruházi fiókkal, amellyel vásároltál. Ha még mindig nem jelenik meg, írj nekünk.</p>
        </details>
      </div>

      <h2 id="guias">Útmutatók lépésről lépésre</h2>
      <p><a href="@@R_guias@@">Összes útmutató megtekintése</a></p>
      <ul>
@@GUIAS@@
      </ul>

      <h2 id="contacto">Van még kérdésed?</h2>
      <p>Írj nekünk a <a href="mailto:hola@mandotv.app?subject=Seg%C3%ADts%C3%A9g%20a%20Mando%20TV-hez">hola@mandotv.app</a> címre. Told meg a tévéd márkájával és típusával, és azzal, hogy melyik lépésnél akadtál el. Írhatsz magyarul. Spanyolul vagy angolul válaszolunk, és ha szeretnéd, fordító segítségével magyarul is.</p>
'''

PRIVACIDAD = dict(
  titulo='Adatvédelmi nyilatkozat | Mando TV',
  desc='A Mando TV nem kér fiókot és személyes adatot: nincs reklám, nincs követés. A távirányító közvetlenül a tévéddel kommunikál, a Wi-Fi-d hálózatán belül.',
  h1='Adatvédelem',
  intro='Röviden: a Mando TV nem kér fiókot és személyes adatot. Nincs reklám, és nincs követés.',
)
PRIVACIDAD_HTML = '''      <p class="fecha">Hatályos 2026. november 14-től. Utolsó frissítés: 2026. november 28.</p>

      <h2>Kik vagyunk</h2>
      <p>A Mando TV egy alkalmazás, amellyel a telefonodról vagy számítógépedről vezérled a tévédet. Ez a nyilatkozat leírja, milyen információkat használ az alkalmazás, és mit tesz velük. Kérdés esetén írj nekünk a <a href="mailto:hola@mandotv.app">hola@mandotv.app</a> címre.</p>

      <h2>Milyen adatokat gyűjtünk</h2>
      <p>Az alkalmazás: csak azt, ami az Androidon és Windowson elérhető ingyenes Pro próbaidőszakhoz kell, a <a href="#prueba">Ingyenes Pro próbaidőszak</a> részben leírva. Ezen kívül az alkalmazás sem rólad, sem arról, hogyan használod, nem küld információt nekünk vagy harmadik feleknek. Nem használ elemző, hirdetési vagy követő eszközöket.</p>
      <p>Ez a weboldal: a látogatásokat két módon mérjük, ezeket a <a href="#cookies">Sütik ezen a weboldalon</a> szakasz magyarázza.</p>

      <h2>Mit tárol az alkalmazás az eszközödön</h2>
      <p>A működéséhez az alkalmazás a következőket tárolja, kizárólag a telefonodon vagy számítógépeden:</p>
      <ul>
        <li>A hozzáadott tévék: név, márka, IP-cím a hálózatodon és a hálózat hardvercíme (MAC), amelyet a bekapcsoláshoz használ.</li>
        <li>A csatlakozási kulcsok, amelyeket minden tévé átad, amikor megerősíted az engedélyt. Titkosítva, a rendszer biztonságos tárolójában vannak elmentve (kulcstartó iPhone-on és Macen, Keystore Androidon, védett tároló Windowson).</li>
        <li>A beállításaid: világos vagy sötét téma, háttérszín, rezgés és a távirányító típusa.</li>
        <li>Ha a Pro funkciókat használod: a kedvenc appjaid, a rutinjaid és az utolsó YouTube-keresések (az alkalmazásban törölheted őket).</li>
        <li>Ha használod őket: a gyerekmód (a PIN-kódot csak védett kódként őrzi) és a távirányítók, amelyeket mások megosztottak veled.</li>
      </ul>
      <p>Ha törlöd az alkalmazást, ezek az adatok vele együtt törlődnek, két kivétellel. Androidon az alkalmazás beállításai (például a tévélistád és a választásaid) a saját Google-mentésedben maradhatnak, ha használod a Google biztonsági mentését, és az alkalmazás újratelepítésekor visszajönnek; a csatlakozási kulcsok sosem tartoznak ide. iPhone-on és Macen a csatlakozási kulcsok a rendszer kulcstartójában vannak, és az alkalmazás törlése után is ott maradhatnak.</p>

      <h2>Kivel kommunikál az alkalmazás</h2>
      <p>A tévéiddel, az otthoni Wi-Fi-den belül. Hogy megtalálja őket, az alkalmazás átkutatja a helyi hálózatodat; ezért kér iPhone-on „Helyi hálózat” engedélyt. Az alkalmazás billentyűzetével beírt szöveg közvetlenül a tévére megy, és nem kerül mentésre.</p>
      <p>Emellett az alkalmazás megnyitáskor letölt egy kis nyilvános fájlt erről a weboldalról (mandotv.app/app/config.json), hogy megtudja, van-e új verzió, amelyet telepítened kellene, és mely funkciók tartoznak a Mando TV Prohoz. Ez ugyanolyan letöltés, mint egy oldal megnyitása: az alkalmazás sem az adataidat, sem a tévéidet, sem azt nem küldi el, amit csinálsz. Csak az alkalmazás verzióját és a rendszert jelzi (például Android), hogy a megfelelő értesítést mutathassa. Ha nincs interneted, az alkalmazás az utoljára letöltött fájllal dolgozik tovább; ha 30 napnál több telik el anélkül, hogy le tudta volna tölteni, az alkalmazás arra kér, hogy rövid időre csatlakozz az internetre. Mint minden weboldal-látogatásnál, ennél a letöltésnél is látja az IP-címedet a webhelyünk szolgáltatója (Cloudflare).</p>

      <p>Ha fényképeket vagy videókat küldesz a tévére (Pro funkció), a tévé csak az általad kiválasztott fájlokat tölti le, közvetlenül a telefonodról vagy számítógépedről, az otthoni Wi-Fi-n keresztül. Nem mennek át sem az interneten, sem rajtunk, az alkalmazás nem látja a többi fényképedet, és a megosztás megszűnik, amint bezárod ezt a képernyőt. Az otthoni hálózatodon belül ez az átvitel nem titkosított.</p>
      <p>Ha a(z) „Képernyőm megjelenítése a tévén“ funkciót használod (Pro funkció), az alkalmazás csak a tükrözés alatt rögzíti a képernyődet, az eszközödön kódolja, és az otthoni wifin keresztül közvetlenül a kiválasztott tévére küldi. Nem megy át az interneten, és rajtunk sem, semmi nem kerül felvételre vagy mentésre, és leáll, amikor leállítod vagy bezárod az alkalmazást. A tévé mindent megmutat, ami azon a képernyőn megjelenik, az értesítéseket is, és az otthoni hálózatodon belül a közvetítés nem titkosított.</p>
      <h2 id="prueba">Ingyenes Pro próbaidőszak (Android és Windows)</h2>
      <p>Hogy az ingyenes Pro próbaidőszak eszközönként csak egyszer legyen elérhető, az alkalmazás a kezdetekor egyszer két dolgot küld a szerverünknek (api.mandotv.app, a Cloudflare-nél): az azonosító titkosított ujjlenyomatát, amelyet a rendszer az adott eszközön ad az alkalmazásnak (Androidon az alkalmazás saját Android-azonosítóját, Windowson az eszközazonosítót az alkalmazásainkhoz), valamint azt, mióta tart a próbaidőszakod. Az ujjlenyomatból nem derül ki, melyik eszközről van szó, sem az, hogy ki vagy, és a szerver tárolás előtt még egyszer titkosítja saját kulccsal.</p>
      <p>Csak ezt az ujjlenyomatot, a próbaidőszak kezdetének dátumát és azt tároljuk, hogy Android vagy Windows. Az IP-címedet nem tároljuk (a Cloudflare látja, amíg válaszol, mint bármelyik kapcsolatnál). Kizárólag arra használjuk, hogy az alkalmazás újratelepítése ne adjon újabb próbaidőszakot, vagyis csalás megelőzésére, ami jogos érdekünk; soha nem reklámra vagy a követésedre, és senkivel nem osztjuk meg. Minden rekord 24 hónap után magától törlődik. Ha nincs interneted, a próbaidőszak így is működik. iPhone-on és Macen semmi nem megy el: a próbaidőszakot az App Store kezeli.</p>

      <h2>Mikrofon és beszéd</h2>
      <p>iPhone-on, Macen és Androidon a hangalapú keresés csak addig használja a mikrofont, amíg a beszéd gombra koppintasz. Amit mondasz, azt a rendszered beszédfelismerője alakítja szöveggé: iPhone-on és Macen az Apple, Androidon a Google, mindkettő a saját adatvédelmi szabályai szerint. Windowson a beszédet a saját számítógépeden ismeri fel, és nem hagyja el azt. Csak ha ez az eszközön futó felismerő nem tud elindulni, vagy folyton hibázik (például régi processzor vagy hiányzó beszédmodell miatt), használja az alkalmazás a Windows hangalapú gépelését, a Microsoftét, amely online működik, ha bekapcsoltad a Windowsban az online beszédfelismerést, a Microsoft adatvédelmi szabályzata szerint. Windowson a mikrofon akkor nyílik meg, amikor megnyitod a hangpanelt, és akkor záródik be, amikor bezárod, vagy 30 másodperc használat nélkül; amíg nem beszélsz, semmi sem kerül rögzítésre vagy tárolásra. A Mando TV nem rögzíti és nem tárolja a hangot, a kapott szöveg pedig közvetlenül a tévédre megy, akárcsak az, amit a billentyűzettel írsz be.</p>

      <h2>Otthon: Apple Home és Google Home eszközök</h2>
      <p>Amikor megnyitod az Otthon részt (tesztelés alatt), az alkalmazás engedélyt kér, hogy lássa azokat az eszközöket, amelyek már megvannak az Apple Home alkalmazásában (HomeKit) vagy a Google Home-ban. Ezzel az engedéllyel elolvassa a nevüket, a helyiségüket és az állapotukat (be vagy ki, fényerő, hőmérséklet, vagy hogy egy háztartási gép a programjának melyik pontján tart), hogy megjelenítse őket, és elküldje nekik, amire koppintasz. Minden a telefonod és az Apple vagy a Google rendszere között történik: a Mando TV nem tárolja ezt a listát, nem küldi el sem nekünk, sem harmadik feleknek, és nem használja sem reklámra, sem elemzésre. Androidon a Google Home a saját Google-fiókoddal működik, a Google adatvédelmi nyilatkozata szerint. Az engedélyt bármikor visszavonhatod: iPhone-on a Beállítások &gt; Adatvédelem és biztonság &gt; HomeKit menüben, Androidon a Google-fiókod beállításaiban.</p>
      <p>Ha rákoppintasz a „Hogyan működött nálad az Otthon?” gombra, megnyílik az e-mail alkalmazásod egy üzenettel a hola@mandotv.app címre, amely műszaki összefoglalót tartalmaz: az alkalmazás verzióját, a rendszert, és hogy hány eszköz jelent meg az egyes fajtákból, és reagálnak-e. Eszközök, helyiségek vagy az otthonod nevét nem tartalmazza, és az üzenet csak akkor megy el, ha te magad elküldöd.</p>

      <h2>Megosztott hivatkozások és szövegek</h2>
      <p>Amikor megosztasz egy távirányítót (egy mandotv.app/m/ hivatkozást), a hivatkozás tartalmazza a távirányító kinézetét és egy támpontot a tévéd megtalálásához: a nevét, márkáját, modelljét és a hálózatodon belüli címét. Soha nem tartalmaz csatlakozási kulcsot, PIN-kódot vagy a tévé hardvercímét. Ezek az adatok a # jel után utaznak, ezért soha nem jutnak el a szervereinkre, de bárki elolvashatja őket, akinek elküldöd a hivatkozást, például WhatsAppon. A megosztott rutin (egy mandotv.app/r/ hivatkozás) csak a nevét és a lépéseit tartalmazza.</p>
      <p>A biztonsági mentés szövege, amelyet az alkalmazás beállításaiban másolhatsz ki, tartalmazza a kedvenceidet, a rutinjaidat és a beállításaidat. Nem titkosított, és csak oda kerül, ahová beilleszted.</p>

      <h2>Tesztjelentés</h2>
      <p>Az alkalmazásban van egy „Tesztjelentés másolása” gomb, amely segít kijavítani a hibákat. A jelentés csak az alkalmazás memóriájában marad, amíg meg van nyitva, és soha nem megy el magától: te döntöd el, lemásolod-e és megosztod-e. Nem tartalmaz csatlakozási kulcsot, párosítási kódot, sem azt, amit begépelsz. Tartalmazza viszont az alkalmazás lépéseit, például a keresést, a csatlakozást és a hibákat, valamint technikai adatokat: az alkalmazás verzióját, a rendszeredet, valamint a tévéd márkáját, modelljét és a hálózatodon belüli címét.</p>

      <h2 id="cookies">Sütik ezen a weboldalon</h2>
      <p>Ez csak a mandotv.app weboldalra vonatkozik, az alkalmazásra nem.</p>
      <h3>Mindig süti nélkül</h3>
      <p>A látogatásokat anonim módon számoljuk a Cloudflare Web Analytics segítségével: hányan látogatják a weboldalt, mely oldalakat olvassák, és melyik országból. Nem használ sütiket, nem az IP-címedet használja az azonosításodhoz, és nem követi, mit csinálsz más weboldalakon.</p>
      <h3>Sütikkel, csak ha beleegyezel</h3>
      <p>Ha a sütiértesítésben az „Elfogadom” gombra koppintasz, bekapcsoljuk a Google Analyticset (a Google LLC-től), hogy jobban megértsük, hogyan használják a weboldalt: oldalmegtekintések, tartózkodási idő, eszköztípus, hozzávetőleges város és honnan érkezel. Ehhez legfeljebb 2 évig tárolja a _ga és _ga_* sütiket a böngésződben. A Google ezeket az adatokat Chilén kívüli szervereken is feldolgozhatja. A hirdetési funkciókat és a Google Signalst kikapcsoltuk, és ezeket az adatokat nem használjuk arra, hogy reklámot mutassunk neked.</p>
      <p>Ha az „Elutasítom” gombra koppintasz, vagy nem választasz semmit, a Google Analytics nem töltődik be, és semmilyen süti nem kerül tárolásra. A döntésedet bármikor megváltoztathatod az egyes oldalak alján lévő „Sütik” gombbal; ha visszavonod a hozzájárulást, töröljük ezeket a sütiket.</p>
      <p>A választásod a böngésződben van elmentve (helyi tároló, senkinek nem küldjük el), hogy ne kérdezzünk rá újra. Ugyanez a tárhely őrzi az oldal alján választott nyelvet is, hogy a webhely legközelebb azon nyíljon meg. Az országodnak megfelelő Pro-ár megjelenítéséhez minden oldal megkérdezi a Cloudflare-t, amely amúgy is kiszolgálja ezt a webhelyet, melyik országból látogatsz, vagy a böngésző nyelvének régióját használja; a választ nem tárolja.</p>

      <h2>Vásárlások</h2>
      <p>Ha megveszed a Mando TV Prót, a fizetést az alkalmazásáruház kezeli (App Store, Google Play vagy Microsoft Store). Mi nem kapjuk meg és nem tároljuk a kártyaadataidat. Az áruház csak azt igazolja az alkalmazásnak, hogy a vásárlás létezik.</p>

      <h2>E-mailek, amelyeket nekünk küldesz</h2>
      <p>Ha a <a href="mailto:hola@mandotv.app">hola@mandotv.app</a> címre írsz nekünk, az e-mail-címedet és azt, amit közölsz velünk, kizárólag arra használjuk, hogy válaszoljunk neked. Nem adjuk tovább, és nem használjuk reklámra. Bármikor kérheted, hogy töröljük az üzeneteidet.</p>

      <h2>Gyermekek</h2>
      <p>Az alkalmazás senkitől nem gyűjt személyes adatokat, a gyermekektől sem.</p>

      <h2>A nyilatkozat módosításai</h2>
      <p>Ha egyszer megváltozik, mit csinál az alkalmazás az adataiddal, frissítjük ezt az oldalt és a fenti dátumot, mielőtt a változás eljut az alkalmazásba.</p>
'''


# >>> guías traídas del inglés (ensamblar.py)
# Adaptadas con Ollama (qwen3.6:35b) desde las guías inglesas y auditadas por Opus el 22-nov. Rutas en idiomas_sitio.py.
GUIAS += [
  dict(clave='no-sub', corto='Távirányító alkalmazás előfizetés nélkül', fecha='2026-11-23',
    titulo='Tévé távirányító alkalmazás előfizetés és reklámok nélkül',
    desc='Elegged van a reklámos vagy előfizetéses távirányító appokból? A Mando TV ingyenes, reklámmentes, a Pro egyszeri vásárlás. Őszinte összehasonlítás.',
    h1='Távirányító alkalmazás előfizetés és reklámok nélkül',
    intro='Sok univerzális távirányító reklámot mutat, vagy heti előfizetést kér, mielőtt működne. A Mando TV más úton jár: a távirányító ingyenes, nincs reklám és nincs fiók. Az opcionális Prót csak egyszer veszed meg. Itt az összehasonlítás, azzal együtt is, amit az alkalmazás nem tud.',
    pasos=[
      'Telepítés előtt nyisd meg egy app áruházi oldalát, és nézd meg az alkalmazáson belüli vásárlásokat. A heti vagy havi árak előfizetésre utalnak.',
      'A Google Playen nézd meg, hogy az oldalon szerepel-e a „Hirdetéseket tartalmaz”, és olvasd el a legújabb, kevés csillagos értékeléseket: ott gyakran előkerülnek a váratlan fizetőfalak.',
      'Győződj meg róla, hogy az alkalmazás Wi-Fi-n tudja vezérelni a tévédet. A Mando TV működik Samsunggal (2016-tól), LG webOS-sel, Rokuval, Google TV-vel, Android TV-vel és Fire TV-vel.',
      'Telepítsd a Mando TV-t, csatlakoztasd a telefonodat ugyanarra a Wi-Fi-re, mint a tévét, és koppints a listában a tévédre.',
      'Erősítsd meg a tévén megjelenő kérdést, vagy írd be a kijelzett kódot. A gombok, a hangerő, a csatornák és a billentyűzet nem kerülnek semmibe.',
    ],
    tabla=dict(titulo='A Mando TV összehasonlítva sok távirányító alkalmazással',
      cabeza=['', 'Mando TV', 'Sok reklámos vagy előfizetéses app'],
      filas=[
        ['Alap távirányító', 'Ingyenes', 'Gyakran ingyenes reklámokkal, vagy próbaidőszak mögé rejtve'],
        ['Reklámok', 'Nincs', 'Gyakori'],
        ['Előfizetés', 'Nincs. A Pro opcionális egyszeri vásárlás', 'A heti vagy havi csomagok megszokottak'],
        ['Fiók', 'Nem kell', 'Változó'],
        ['Okostévék Wi-Fi-n', 'Samsung (2016-tól), LG webOS, Roku, Google TV, Android TV, Fire TV, Apple TV (béta)', 'Appfüggő'],
        ['Infravörös régebbi tévékhez', 'Ingyenes infravörös adós Android telefonokon (új)', 'Néhány app, csak infravörös adós telefonokon'],
        ['Bluetooth', 'Béta Android 9-től, ingyenes', 'Appfüggő'],
        ['Fényképek és videók a tévére', 'Pro, Wi-Fi-n (nem képernyőtükrözés)', 'Appfüggő'],
        ['Telefonok és számítógépek', 'iPhone, iPad, Mac és Windows, valamint Android korai hozzáféréssel', 'Változó'],
        ['Képernyőtükrözés', 'Ingyenes iPhone-on, iPaden és Windowson a rendszer beépített funkciójával. Windowson a Pro ezenkívül tükrözheti a számítógép képernyőjét LG, Samsung, Hisense és Android TV tévékre (béta)', 'Néhány app kínálja'],
      ],
      nota='A Mando TV-t nem hasonlítjuk egyetlen konkrét apphoz sem. A naprakész árak az adott alkalmazás áruházi oldalán találhatók.'),
    extra=[
      ('Mit nem csinál a Mando TV', 'iPhone-on és iPaden a Vezérlőközpont képernyőtükrözéséhez vezet, amely az iPhone saját funkciója, és AirPlay-es tévékkel működik. Windowson megnyitja az Átküldést (Windows + K), a Mando TV Pro pedig el tudja küldeni a számítógép képernyőjét az otthoni Wi-Fi-n keresztül LG, Samsung, Hisense és Android TV tévékre (béta, néhány másodperc késéssel és hang nélkül). A Mando TV Proval ezenkívül fényképeket és videókat tud küldeni a tévére a Wi-Fi-n keresztül. Okostévéket vezérel az otthoni Wi-Fi-n. A nem okos tévéket infravörös adóval rendelkező Android telefonról infravörösön vezérelheted. Android 9-től a telefon Bluetooth-on is csatlakozhat billentyűzetként és távirányítóként Google TV-hez, Android TV-hez és Fire TV-hez, Wi-Fi nélkül. Ez az opció bétában van, és ingyenes.'),
      ('Miből él a Mando TV', 'Nem reklámból, és nem az adataidból: az alkalmazásban nincs reklám, és nem követ téged. A Mando TV-t a Pro finanszírozza, egy opcionális egyszeri vásárlás extrákért. Az alap távirányító ingyenes.'),
      ('A már meglévő eszközeiden', 'iPhone, iPad és Mac az App Store-ból, Windows-számítógépek a Microsoft Store-ból, Android pedig ingyenes korai hozzáféréssel a Google Playen. Lásd a [Távirányító alkalmazás iPhone-ra](@iphone) és a [Távirányító alkalmazás Windowsra](@windows) útmutatót.'),
      ('Adatvédelem', 'Az alkalmazásban nincs fiók és nincs követés. A tévével való kommunikáció csak a helyi hálózaton belül zajlik, a csatlakozási adatok titkosítva maradnak az eszközödön. A részleteket az [Adatvédelmi nyilatkozatban](@privacidad) találod.'),
    ],
    marca=None,
    faq=[
      ('Van előfizetés nélküli távirányító alkalmazás?', 'Igen. A Mando TV-nek egyáltalán nincs előfizetése: a távirányító ingyenes és reklámmentes, a Pro opcionális egyszeri vásárlás.'),
      ('Tényleg ingyenes a Mando TV?', 'Igen. Az iránygombok, az OK, a Vissza, a Home, a hangerő, a csatornák, a számok, a billentyűzet és a be-/kikapcsolás ingyenes, reklámok és időkorlát nélkül.'),
      ('Működik Wi-Fi nélkül?', 'Többnyire nem. A Mando TV az otthoni Wi-Fi-n vezérli az okostévéket. Kivételek: az infravörös infravörös adós Android telefonokon, amely okos funkció nélküli vagy Wi-Fi-re nem csatlakozó tévékkel is működik, és a Bluetooth, a bétában Android 9-től, Google TV-hez, Android TV-hez és Fire TV-hez.'),
    ]),
  dict(clave='roku-app-alt', corto='A Roku alkalmazás alternatívája', fecha='2026-11-23',
    titulo='A Roku alkalmazás alternatívája: egyszerű Roku távirányító',
    desc='A Roku alkalmazás alternatívája: a Mando TV Wi-Fi-n vezérli a Roku TV-ket és lejátszókat, fiók és reklám nélkül, Samsunggal, LG-vel és Google TV-vel.',
    h1='A Roku alkalmazás alternatívája: egy minden tévéhez',
    intro='A hivatalos Roku alkalmazás sokat tud: Channel Store, átküldés, privát hallgatás és távirányító. Ha csak egy gyors távirányítót keresel, vagy otthon Samsung, LG vagy Google TV tévéd is van, a Mando TV egyszerű alternatíva, amely a Wi-Fi-n keresztül, fiók nélkül vezérli a Rokut.',
    pasos=[
      'Csatlakoztasd a telefonodat és a Rokut ugyanarra a Wi-Fi-re.',
      'Töltsd le és nyisd meg a Mando TV-t. A Roku TV-d vagy Roku lejátszód megjelenik a listában. Koppints rá. A Roku nem kér kódot.',
      'Használd az iránygombokat, az OK-t, a Vissza, a Home gombot, a hangerőt és a billentyűzetet. A keresőszavakat a Roku csatornáin a telefon billentyűzetével add meg.',
      'Ha a gombok nem csinálnak semmit, menj a Rokun a Beállítások > Rendszer > Speciális rendszerbeállítások > Vezérlés mobilappokkal menübe, és állítsd a hálózati hozzáférést Alapértelmezett vagy Permissive értékre (újabb Roku-szoftvernél a Vezérlés mobilappokkal legyen Engedélyezett).',
      'Opcionális: kapcsold be a Roku TV-n a „TV gyorsindítás” opciót a Beállítások > Rendszer > Energia menüben, hogy a Mando TV be tudja kapcsolni a tévét.',
    ],
    extra=[
      ('Ahol a Mando TV jobban illik', 'Egy alkalmazás több tévéhez: Roku, Samsung, LG és Google TV vagy Android TV. Fiók és reklámok nélkül. Windows-számítógépen is működik, ami az íróasztalnál kényelmes. Az iránygombok és a hangerő gyorsan reagálnak, a billentyűzettel pedig fáradság nélkül gépeled be a keresőszavakat.'),
      ('Ahol a hivatalos Roku alkalmazás jobb', 'Tartsd meg a Roku alkalmazást arra, amit a távirányítón túl nyújt, például a Roku Channel Store csatornáinak böngészésére és hozzáadására, valamint a saját átküldésére és a privát hallgatásra (hang a telefonra csatlakoztatott fejhallgatón). Használd mindkettőt, ha szeretnéd. Futhatnak ugyanazon a telefonon.'),
      ('Roku TV készülékek és Roku lejátszók', 'Mindkettő működik. Ide tartoznak a TCL, Hisense, Philips és más gyártók Roku TV modelljei, valamint a Roku Express, a Streaming Stick és az Ultra. A részleteket a [Roku távirányító alkalmazás oldalán](@roku) találod.'),
      ('Ha a Roku alkalmazás már nem működik', 'Ha a gombok nem reagálnak, a Roku általában blokkolja az appokkal való vezérlést. A [A Roku alkalmazás nem működik](@roku-403) útmutató megmutatja a beállítást, amely megoldja a problémát.'),
      ('Ingyenes és Pro', 'Az iránygombok, az OK, a Vissza, a Home, a hangerő, a csatornák, a számgombok, a billentyűzet, az appok megnyitása, a bemenetek váltása és a be- vagy kikapcsolás ingyenes, reklámok és előfizetés nélkül. Az érintőpad, a hangparancsok, a kedvenc appok, a rutinok és a kikapcsolási időzítő a Mando TV Pro részei, amely egyszeri vásárlás előfizetés nélkül.'),
    ],
    marca='roku',
    faq=[
      ('Kell Roku-fiók a Mando TV használatához?', 'Nem. A Mando TV az otthoni hálózaton keresztül kommunikál a Rokuval, és nem kér fiókot.'),
      ('Teljesen kiváltja a Mando TV a Roku Mobile alkalmazást?', 'Távirányítóként igen. A Channel Store-hoz, az átküldéshez és a privát hallgatáshoz tartsd meg a hivatalos Roku alkalmazást.'),
      ('Működik a Roku Expresszel vagy a Streaming Stickkel?', 'Igen. Minden Roku lejátszót és Roku TV készüléket ugyanúgy vezérelhetsz.'),
    ]),
  dict(clave='lg-thinq', corto='Az LG ThinQ alkalmazás alternatívája', fecha='2026-11-23',
    titulo='Az LG ThinQ alkalmazás alternatívája: LG távirányító fiók nélkül',
    desc='Az LG ThinQ alkalmazás alternatíváját keresed csak távirányítóként? A Mando TV Wi-Fi-n vezérli a webOS-es LG tévéket, LG-fiók és reklámok nélkül.',
    h1='Az LG ThinQ alkalmazás alternatívája az LG tévédhez',
    intro='Az LG ThinQ az LG hivatalos alkalmazása, az egész okosotthonhoz: háztartási gépekhez, a tévéhez és másokhoz. Ha csak egy egyszerű távirányítót szeretnél az LG tévédhez, a Mando TV pontosan ezt végzi az otthoni Wi-Fi-n keresztül, anélkül hogy LG-fiókot kellene létrehoznod, és reklámok nélkül.',
    pasos=[
      'Csatlakoztasd a telefonodat vagy a számítógépedet (iPhone, Android vagy Windows) és az LG tévédet ugyanarra a Wi-Fi-re.',
      'Töltsd le és nyisd meg a Mando TV-t. Az LG tévéd magától megjelenik a listában. Koppints rá.',
      'A tévén megjelenik egy kérdés. Egyszer erősítsd meg a tévé távirányítójával, a képernyő alatti joystickkal vagy a Magic Remote-tal.',
      'A gombok, a hangerő és a billentyűzet azonnal működnek. Nincs szükséged LG-fiókra, és a tévét sem kell regisztrálnod.',
      'Opcionális: kapcsold be a tévé beállításaiban a „Tévé bekapcsolása mobilról” opciót, hogy a tévét a telefonodról is be tudd kapcsolni.',
    ],
    extra=[
      ('Mando TV vagy LG ThinQ: melyik mire jó', 'A ThinQ-t használd, ha LG háztartási gépeket, például mosógépet, hűtőszekrényt vagy légkondicionálót akarsz kezelni, vagy LG-fiókfunkciókra van szükséged. A Mando TV-t használd, ha gyors, egyszerű távirányítót akarsz a tévéhez, amely ugyanabban az alkalmazásban Samsunghoz, Rokuhoz és Google TV-hez is működik. Sokan mindkettőt megtartják: a ThinQ-t a háztartási gépekhez, a Mando TV-t a tévéhez.'),
      ('Mit tud a Mando TV LG tévén', 'Működik webOS-es LG okostévékkel, vagyis a legtöbb modellel 2014 óta, beleértve a LED, NanoCell, QNED és OLED tévéket. Kínálja az iránygombokat, az OK-t, a Vissza, a Home gombot, a hangerőt, a csatornákat, a némítást, a lejátszásvezérlőket és egy billentyűzetet a tévé keresőjében és a legtöbb appban való gépeléshez. Az appok listája és a bemenetek listája szintén ingyenes. A Proval ráadásul kapsz egy mutatót, mint a Magic Remote-nál.'),
      ('Mit nem csinál a Mando TV', 'Nem vezérel LG háztartási gépeket, nem használja az LG-fiókodat, és nem helyettesíti a tévén lévő LG-fiókszolgáltatásokat. Távirányító, nem okosotthon-központ.'),
      ('Adatvédelem és reklámok', 'A Mando TV-ben nincs reklám és nincs fiók. Csak az otthoni hálózaton belül kommunikál a tévével, és a csatlakozási kulcsot titkosítva tárolja az eszközödön. Az összes funkciót az [LG távirányító alkalmazás](@lg) oldalon találod.'),
      ('Ingyenes és Pro', 'Az iránygombok, az OK, a Vissza, a Home, a hangerő, a csatornák, a számgombok, a billentyűzet, az appok megnyitása, a bemenetek váltása és a be-/kikapcsolás ingyenes, reklámok és előfizetés nélkül. Az érintőpad, a hangparancsok, a kedvenc appok, a rutinok és a kikapcsolási időzítő a Mando TV Pro részei, amely egyszeri vásárlás előfizetés nélkül.'),
    ],
    marca='lg',
    faq=[
      ('Vezérelhetem az LG tévémet az LG ThinQ alkalmazás nélkül?', 'Igen. A Mando TV közvetlenül a Wi-Fi-n keresztül csatlakozik a webOS-es LG tévékhez. Egyszer elfogadsz egy kérdést a tévén, és ennyi, LG-fiók nélkül.'),
      ('Működik a Mando TV az LG Magic Remote mutatójához hasonlóan?', 'A Mando TV Prónak van mutatója, amelyet az ujjaddal mozgatsz a telefon képernyőjén, hasonlóan ahhoz, ahogy a Magic Remote mozgatja a nyilat.'),
      ('Az LG-é a Mando TV?', 'Nem. A Mando TV független alkalmazás, és nem áll kapcsolatban az LG-vel. Az LG és a ThinQ tulajdonosaik védjegyei, csak a kompatibilitás leírására szerepelnek.'),
    ]),
  dict(clave='smartthings', corto='A SmartThings alternatívája', fecha='2026-11-23',
    titulo='Nem megy a SmartThings? Egyszerű alternatíva Samsunghoz',
    desc='Túl lassú vagy hibás a SmartThings? A Mando TV a Tizen rendszerű Samsung tévéket közvetlenül Wi-Fi-n vezérli. Samsung-fiók és reklámok nélkül. Lépésről lépésre.',
    h1='SmartThings-alternatíva Samsung tévékhez',
    intro='A SmartThings a Samsung alkalmazása az egész okosotthonhoz, és a távirányítója a Samsung-fiókodon keresztül működik. Ha már nem megy, vagy gyors megoldást keresel, a Mando TV a 2016-os és újabb, Tizen rendszerű Samsung tévéket közvetlenül a Wi-Fi-n keresztül vezérli, fiók nélkül.',
    pasos=[
      'Csatlakoztasd a telefonodat és a Samsung tévét ugyanarra a Wi-Fi-re.',
      'Töltsd le a Mando TV-t, és nyisd meg az alkalmazást. A Samsung tévéd magától megjelenik a listában. Koppints rá.',
      'A tévé megkérdezi, engedélyezed-e a kapcsolatot. Válaszd az „Engedélyezés” lehetőséget a távirányítóval vagy a tévén lévő gombbal (csak az első alkalommal).',
      'Azonnal használhatod az iránygombokat, az OK-t, a Vissza, a Home gombot, a hangerőt, a csatornákat és a billentyűzetet.',
      'Opcionális: kapcsold be a „Bekapcsolás mobilról” opciót a Beállítások > Általános > Hálózat > Szakértői beállítások menüben, hogy a Mando TV be is tudja kapcsolni a tévét.',
    ],
    extra=[
      ('Miért nem működik már a telefonos távirányító', 'Az okok többnyire egyszerűek: a telefon és a tévé különböző Wi-Fi-n van, be van kapcsolva egy VPN, vagy a tévé mély készenlétben van. A SmartThingsnél a Samsung-fiók is okozhat gondot, például ha kijelentkeztettek. A Mando TV közvetlenül a tévével kommunikál az otthoni hálózaton, nincs fiók, amelybe be kellene jelentkezni. További tippeket a [A telefonod nem találja a tévét](@not-found) útmutatóban találsz.'),
      ('Mando TV vagy SmartThings: melyik mire jó', 'Tartsd meg a SmartThingst, ha Samsung háztartási gépekhez, lámpákhoz vagy más okosotthon-eszközökhöz használod, vagy a Samsung-fiókod funkcióihoz. A Mando TV-t használd, ha egyszerűen gyors távirányítót akarsz a tévéhez, vagy otthon LG, Roku, Google TV vagy Fire TV eszközöd is van: egy alkalmazás mindet vezérli. Mindkét app telepítve lehet ugyanazon a telefonon.'),
      ('Ha véletlenül elutasítottad az engedélyt', 'Menj a tévén a Beállítások > Általános > Külső eszközök kezelője > Eszközcsatlakozás-kezelő menübe, és állítsd a Mando TV-t engedélyezettre.'),
      ('Nincs távirányító?', 'A kérdést a tévén lévő gombbal is megerősítheted. A [Samsung tévé az eredeti távirányító nélkül](@samsung-lost) útmutató megmutatja, hogyan.'),
      ('Ingyenes és Pro', 'A távirányítót ingyen töltheted le és használhatod, reklámok és előfizetés nélkül. A Mando TV Pro opcionális egyszeri vásárlás extrákért.'),
    ],
    marca='samsung',
    faq=[
      ('Vezérelhetem a Samsung tévémet SmartThings nélkül?', 'Igen. A Mando TV közvetlenül a Wi-Fi-n keresztül csatlakozik a Tizen rendszerű Samsung tévékhez. Egyszer engedélyezed a kapcsolatot a tévén, Samsung-fiók nélkül.'),
      ('Vezérel a Mando TV Samsung háztartási gépeket is?', 'Nem. Csak a tévé távirányítója. A háztartási gépekhez és más okosotthon-eszközökhöz megtartod a SmartThingst.'),
      ('A Samsungé a Mando TV?', 'Nem. A Mando TV független alkalmazás, és nem áll kapcsolatban a Samsunggal. A Samsung és a SmartThings tulajdonosaik védjegyei, csak a kompatibilitás leírására szerepelnek.'),
    ]),
  dict(clave='googletv-alt', corto='A Google TV távirányító alternatívája', fecha='2026-11-23',
    titulo='Nem megy a Google TV távirányító? Az alternatíva',
    desc='A Google TV telefonos távirányítója nem találja a tévét? A Mando TV Wi-Fi-n vezérli a Google TV-t és az Android TV-t, Google-fiók és reklámok nélkül.',
    h1='A Google TV telefonos távirányítójának alternatívája',
    intro='A Google TV és az Android TV telefonos távirányítója magában a Google alkalmazásában van, és a Google-fiókodhoz kötődik. Ha nem találja a tévét, nem jutsz tovább. A Mando TV különálló távirányító alkalmazás, amely a képernyőn lévő 6 karakteres kóddal párosít, és Google-fiók nélkül működik, iPhone-on, Android telefonon vagy Windows-számítógépen.',
    pasos=[
      'Kapcsold be a tévét, és csatlakoztasd a telefonodat ugyanarra a Wi-Fi-re.',
      'Töltsd le a Mando TV-t, és nyisd meg az alkalmazást. Koppints a listában a Google TV-s vagy Android TV-s tévédre.',
      'A tévé egy 6 karakteres kódot mutat. Írd be a Mando TV-ben, és koppints a Párosítás gombra.',
      'Használd az iránygombokat, az OK-t, a Vissza, a Home gombot, a hangerőt és a billentyűzetet. Sehova nem kell bejelentkezned.',
      'Opcionális: keresd a tévé beállításaiban a Wake on LAN vagy a „Bekapcsolás hálózaton keresztül” opciót, hogy az alkalmazás be is tudja kapcsolni a tévét.',
    ],
    extra=[
      ('Miért nem találja már a telefonos távirányító a tévét', 'Többnyire a hálózattal van baj: a telefon és a tévé különböző Wi-Fi-n van, be van kapcsolva egy VPN, vagy egy vendéghálózat elszigeteli az eszközöket. Ezt javítsd ki először, mert minden távirányító alkalmazást érint. Többet olvashatsz róla a [A telefonod nem találja a tévét](@not-found) útmutatóban.'),
      ('Mely tévékkel működik', 'Google TV-s és Android TV-s tévék a Sonytól, TCL-től, Hisense-től, Philipstől, Sharptól, Xiaomitól, Toshibától és másoktól, valamint Chromecast Google TV-vel, Google TV Streamer és Nvidia Shield. Mindegyiket ugyanúgy kell párosítani, egyszer, a képernyőn lévő kóddal.'),
      ('Ahol a Google alkalmazása jobb', 'A Google alkalmazása abban is segít, hogy megtaláld a nézni való tartalmakat, és megjegyzi a figyelőlistádat. Tartsd meg erre. A Mando TV csak a távirányító, és ugyanabból az alkalmazásból Samsungot, LG-t, Rokut és Fire TV eszközöket is vezérel, valamint Windows-számítógépről is.'),
      ('Ha hiányzik a régi Android TV távirányító alkalmazás', 'A Google a telefonos távirányítót a régi Android TV Remote Control alkalmazásból átvitte a Google TV alkalmazásba. Ha különálló távirányítót keresel, a Mando TV egy lehetőség.'),
      ('Ingyenes és Pro', 'A távirányítót ingyen töltheted le és használhatod, reklámok és előfizetés nélkül. A Mando TV Pro opcionális egyszeri vásárlás extrákért.'),
    ],
    marca='android',
    faq=[
      ('Kell Google-fiók a Mando TV használatához Google TV-vel?', 'Nem. A tévén lévő kód elég a párosításhoz.'),
      ('Működik Chromecast Google TV-vel?', 'Igen. A párosítás ugyanígy megy, a képernyőn lévő 6 karakteres kóddal.'),
      ('Használhatom iPhone-ról?', 'Igen. A Mando TV elérhető az App Store-ban iPhone-ra és iPadre, a Microsoft Store-ban Windowsra, és az ingyenes korai hozzáféréssel a Google Playen Androidra.'),
    ]),
  dict(clave='windows', corto='Távirányító Windows-számítógéphez', fecha='2026-11-23',
    titulo='Távirányító alkalmazás Windowsra: tévé vezérlése a számítógépről',
    desc='Vezérelj Samsung, LG, Roku, Google TV vagy Fire TV tévét Windows PC-ről a Mando TV-vel: billentyűparancsok, mini távirányító, Wi-Fi. Microsoft Store.',
    h1='Távirányító alkalmazás Windows-számítógéphez',
    intro='A Mando TV-nek van Windows-alkalmazása, amely az otthoni hálózaton keresztül a számítógépedet vagy laptopodat a tévé távirányítójává alakítja. Gépelj a tévén az igazi billentyűzeteddel, hagyj munka közben egy kis távirányító ablakot az előtérben, és vezérelj Samsungot, LG-t, Rokut, Google TV-t vagy Fire TV-t ugyanazzal az alkalmazással.',
    pasos=[
      'Telepítsd ingyen a Mando TV-t a Microsoft Store-ból egy Windows 10-es vagy 11-es számítógépre.',
      'Győződj meg róla, hogy a számítógép és a tévé ugyanazon a hálózaton van, Wi-Fi-n vagy kábellel ugyanahhoz a routerhez csatlakozva.',
      'Nyisd meg a Mando TV-t. A tévé megjelenik a listában. Kattints rá.',
      'Erősítsd meg a tévén megjelenő kérdést, ha kérdez (LG, Samsung), vagy írd be a kijelzett kódot (Google TV, Fire TV).',
      'Kattints a gombokra, vagy gépelj be egy keresést a billentyűzeteddel. Kész.',
    ],
    extra=[
      ('Billentyűparancsok (Pro)', 'A Proval a számítógéped billentyűzete távirányítóvá válik: nyílbillentyűk a mozgáshoz, Enter az OK-hoz, Backspace vagy Esc a visszalépéshez, Plusz és Mínusz a hangerőhöz, M a némításhoz és szóköz a szünethez.'),
      ('Mini távirányító (Pro)', 'Egy kis távirányító ablak, amely minden más ablak felett marad. Így hangerőt állíthatsz vagy szünetelhetsz anélkül, hogy megszakítanád a munkádat.'),
      ('Gépelés a tévén a számítógépről', 'A tévé képernyőbillentyűzete lassú. A Mando TV-ben az igazi billentyűzeteddel gépelsz, és a szöveg a tévé keresőmezőjébe kerül. Ez a rész ingyenes.'),
      ('További részletek', 'A lépésről lépésre útmutatót a [Tévé vezérlése számítógéppel](@pc) oldalon találod. A telefonhoz olvasd el a [Telefon távirányítóként Wi-Fi-n](@wifi) útmutatót.'),
      ('Ingyenes és Pro', 'Az iránygombok, az OK, a Vissza, a Home, a hangerő, a csatornák, a számgombok, a billentyűzet, az appok megnyitása, a bemenetek váltása és a be- vagy kikapcsolás ingyenes, reklámok és előfizetés nélkül. Az érintőpad, a hangparancsok, a kedvenc appok, a rutinok és a kikapcsolási időzítő a Mando TV Pro részei, amely egyszeri vásárlás előfizetés nélkül. Windowson a Prót a Microsoft Store-on keresztül veszed meg.'),
      ('Hangparancsok a számítógépről (Pro)', 'A Proval a számítógép mikrofonján keresztül beszélhetsz a tévével. A beszédet közvetlenül a számítógép ismeri fel: ehhez nincs szükséged internetre, és semmit nem kell beállítanod a Windowsban. Amit mondasz, soha nem hagyja el a számítógépet, és nem kerül mentésre. Csak nagyon régi processzoroknál esik vissza az alkalmazás a Windows hangbevitelére. Ehhez az adatvédelmi beállításokban be kell kapcsolni az online beszédfelismerést, és a nyelvedet hozzá kell adni a Windowshoz.'),
    ],
    marca=None,
    faq=[
      ('Kell Bluetooth vagy kábel a Windows távirányító alkalmazáshoz?', 'Nem. Az otthoni hálózatodat használja. A számítógépnek és a tévének csak ugyanahhoz a routerhez kell csatlakoznia.'),
      ('Mely tévéket vezérelhetem Windowsról?', 'Tizen rendszerű Samsung tévéket, webOS-es LG tévéket, Roku TV-t és lejátszókat, Google TV-t és Android TV-t, valamint Fire TV-t.'),
      ('Láthatom a tévéképet a számítógépen, vagy hallhatom a számítógép hangszóróin?', 'Nem. A Mando TV csak távirányító. Nem tükrözi és nem streameli a tévéképet a számítógépre.'),
      ('Miért nem működik a hang a Windows-számítógépemen?', 'A hangvezérlés Pro funkció. Ellenőrizd tehát, hogy a Pro aktív-e, és működik-e a számítógép mikrofonja. A legtöbb számítógépen a beszédet közvetlenül a számítógép ismeri fel, internet nélkül. Csak nagyon régi processzoroknál használja az alkalmazás a Windows hangbevitelét: ilyenkor kapcsold be az online beszédfelismerést a Windows adatvédelmi beállításaiban, és add hozzá a nyelvedet a nyelvi beállításokban.'),
    ]),
  dict(clave='iphone', corto='Távirányító alkalmazás iPhone-ra', fecha='2026-11-23',
    titulo='Távirányító alkalmazás iPhone-ra: Samsung, LG, Roku, Google TV',
    desc='Használd az iPhone-odat távirányítóként Samsung, LG, Roku, Google TV és Fire TV esetén Wi-Fi-n. Ingyen az App Store-ban, fiók és reklámok nélkül.',
    h1='Távirányító alkalmazás iPhone-ra: egy minden tévéhez',
    intro='A Mando TV az iPhone-odat vagy iPadedet távirányítóvá teszi Samsung, LG, Roku, Google TV vagy Android TV, valamint Fire TV tévékhez, az otthoni Wi-Fi-n keresztül. Az alkalmazás ingyenes az App Store-ban, fiók és reklámok nélkül. Androidon és Windowson is fut.',
    pasos=[
      'Töltsd le ingyen a Mando TV-t az App Store-ból.',
      'Csatlakoztasd az iPhone-odat és a tévét ugyanarra a Wi-Fi-re.',
      'Nyisd meg a Mando TV-t, és koppints az Engedélyezés gombra, amikor az iOS a helyi hálózathoz való hozzáférést kéri. Az alkalmazásnak erre van szüksége, hogy megtalálja a tévét.',
      'Koppints a listában a tévédre. Erősítsd meg a tévén megjelenő kérdést, ha kérdez (LG és Samsung), vagy írd be a tévé által mutatott kódot (Google TV vagy Fire TV).',
      'Használd a gombokat, a hangerőt és a billentyűzetet. Csatlakoztál.',
    ],
    extra=[
      ('Ezekkel a tévékkel működik', 'LG webOS, Samsung Tizen (2016-os és újabb gyártású), Roku TV és Roku lejátszók, Google TV és Android TV, valamint Fire TV. A márkák oldalai: [Samsung](@samsung), [LG](@lg), [Roku](@roku) és [Android TV](@android).'),
      ('Miért kér helyi hálózatot', 'Az iPhone blokkolja, hogy az appok hozzáférjenek az otthoni hálózatodon lévő eszközökhöz, hacsak nem engedélyezed. Ha a tévé nem jelenik meg a listában, nyisd meg a Beállítások > Mando TV menüt, és kapcsold be a „Helyi hálózat” opciót. Az alkalmazás csak a tévéddel kommunikál, az otthoni hálózatodon belül.'),
      ('Miért a Mando TV, és nem a gyártó alkalmazása', 'Minden tévémárkának saját alkalmazása van, és saját beállítást vagy fiókot akar. A Mando TV egy alkalmazás mindenkinek, fiók nélkül.'),
      ('Ingyenes és Pro iPhone-on', 'Az iránygombok, az OK, a Vissza, a Home, a hangerő, a csatornák, a számgombok, a billentyűzet, az appok megnyitása, a bemenetek váltása és a be- vagy kikapcsolás ingyenes, reklámok és előfizetés nélkül. Az érintőpad, a hangparancsok, a kedvenc appok, a rutinok és a kikapcsolási időzítő a Mando TV Pro részei, amely egyszeri vásárlás előfizetés nélkül. A Prót egyszer veszed meg, közvetlenül az alkalmazásban.'),
    ],
    marca=None,
    faq=[
      ('Ingyenes a Mando TV iPhone-on?', 'A letöltés ingyenes, reklámok nélkül. Az alap távirányító ingyenes, akárcsak az appok megnyitása és a bemenetek váltása. Az olyan extrák, mint az érintőpad, a hangparancsok és a rutinok, a Mando TV Pro részei, amely egyszeri vásárlás.'),
      ('Működik iPaden?', 'Igen. Ugyanaz az alkalmazás fut iPhone-on és iPaden.'),
      ('Kell az iPhone-os távirányító alkalmazáshoz Bluetooth vagy infravörös adó?', 'iPhone-on nem. Az iPhone-oknak nincs infravörös adójuk, ezért az infravörös vezérlés ott nem érhető el, a Bluetooth opció pedig csak Android 9 vagy újabb rendszerhez van, iPhone-hoz nem. iPhone-on a Mando TV az okostévéket, valamint az Apple TV-t (béta) az otthoni Wi-Fi-n keresztül vezérli.'),
    ]),
  dict(clave='firetv', corto='Fire TV távirányító', fecha='2026-11-23',
    titulo='Fire TV távirányító alkalmazás telefonra és számítógépre',
    desc='Fire TV távirányító a telefonodon: vezérelj Fire TV Sticket, Fire TV Cube-ot vagy Fire TV-s tévét Wi-Fi-n, 4 számjegyű PIN-nel. Amazon-alkalmazás nélkül.',
    h1='Fire TV távirányító a telefonodra vagy számítógépedre',
    intro='Ha elveszett a Fire TV távirányítója, vagy lemerült az eleme, a Mando TV Wi-Fi-n keresztül vezérel egy Fire TV Sticket, egy Fire TV Cube-ot vagy beépített Fire TV-s tévét. A párosítás 4 számjegyű PIN-nel történik. A Fire TV új a Mando TV-ben, ezért először frissítsd az alkalmazást.',
    pasos=[
      'Frissítsd a Mando TV-t a legújabb verzióra az App Store-ból, a Microsoft Store-ból vagy a Google Playről.',
      'Kapcsold be a Fire TV-t, és csatlakoztasd a telefonodat ugyanarra a Wi-Fi-re.',
      'Nyisd meg a Mando TV-t. A Fire TV-d megjelenik a listában. Koppints rá.',
      'A tévé képernyőjén megjelenik egy 4 számjegyű PIN. Írd be a Mando TV-ben. Ezt csak egyszer kell megtenned.',
      'Használd az iránygombokat, az OK-t, a Vissza, a Home gombot, a lejátszógombokat és a billentyűzetet a kereséshez.',
    ],
    extra=[
      ('Támogatott Fire TV eszközök', 'Fire TV Stick, Fire TV Stick 4K, Fire TV Cube és beépített Fire TV-s tévék, például az Amazon Fire TV Edition tévék és néhány Hisense modell. A támogatás új, és eddig csak kevés valódi eszközön tudtuk tesztelni. Ha valami nem a várt módon működik, írd meg nekünk a modelledet a Súgó oldalon.'),
      ('A Fire TV bekapcsolása', 'A Mando TV nem kapcsol be hálózaton keresztül Fire TV-t. Kapcsold be a tévét a készüléken lévő bekapcsológombbal: a bedugott Fire TV Stick vagy Cube általában a HDMI-CEC-nek köszönhetően felébred, és beépített Fire TV-s tévénél a tévé maga a Fire TV. Utána a telefonodról vezérled.'),
      ('Ha a Fire TV-d nem jelenik meg', 'Győződj meg róla, hogy mindkét eszköz ugyanazon a Wi-Fi-n van, és a Fire TV fel van ébredve. iPhone-on engedélyezd a „Helyi hálózat” opciót a Mando TV-nek a Beállításokban. Lásd a [A telefonod nem találja a tévét](@not-found) útmutatót.'),
      ('Egyáltalán nincs távirányító?', 'A Fire TV-nek meg kell mutatnia a PIN-t a képernyőn, ezért a tévének és a Fire TV-nek be kell lennie kapcsolva, és képet kell mutatnia. Ha a tévé rossz bemeneten áll, váltsd át a tévén lévő gombokkal. Lásd a [Bemenet váltása távirányító nélkül](@hdmi) útmutatót.'),
      ('Ingyenes és Pro', 'Az iránygombok, az OK, a Vissza, a Home, a hangerő, a csatornák, a számok, a billentyűzet, az appok megnyitása, a bemenetek váltása és a be-/kikapcsolás ingyenes, reklámok és előfizetés nélkül. Az érintőpad, a hangparancsok, a kedvenc appok, a rutinok és a kikapcsolási időzítő a Mando TV Pro részei, amely egyszeri vásárlás előfizetés nélkül.'),
    ],
    marca=None,
    faq=[
      ('Kell az Amazon Fire TV alkalmazás?', 'Nem. A Mando TV Wi-Fi-n, PIN-nel csatlakozik a Fire TV-hez. Nincs szükséged Amazon-fiókra a telefonodon.'),
      ('Működik Fire TV-s tévékkel és Fire TV Stickekkel?', 'Igen, pontosan erre készült. A támogatás új, tartsd naprakészen az alkalmazást, és jelezd nekünk azokat a modelleket, amelyek nem a várt módon működnek.'),
      ('Miért kell PIN?', 'A Fire TV egy 4 számjegyű PIN-t mutat, hogy bizonyítsd: a tévé előtt ülsz. Senki nem tud párosítani anélkül, hogy látná a képernyőt.'),
    ]),
  dict(clave='firetv-lost', corto='Elveszett Fire TV távirányító', fecha='2026-11-23',
    titulo='Elveszett a Fire TV távirányító? Így segít a telefonod',
    desc='Elveszett a Fire TV Stick távirányítója? Vezéreld Wi-Fi-n a telefonoddal, 4 számjegyű PIN-nel párosítva. Tippek új Wi-Fi-hez és HDMI-CEC-hez.',
    h1='Elveszett Fire TV távirányító: így használd a telefonod',
    intro='Ha elveszett a Fire TV Stick, a Fire TV Cube vagy a Fire TV-s okostévé távirányítója, vagy már nem működik, a telefonod átveszi a vezérlést, amíg a Fire TV még csatlakozik a Wi-Fi-dhez. A párosítás a képernyőn megjelenő 4 számjegyű PIN-nel történik, így ehhez sosem kell a régi távirányító.',
    pasos=[
      'Kapcsold be a tévét a készüléken lévő gombbal. A bedugott Fire TV Stick vagy Cube általában vele együtt felébred; bekapcsolt HDMI-CEC mellett a tévé gyakran magától átvált a bemenetére.',
      'Ha a tévé másik bemenetet mutat, váltsd át a tévén lévő bemenet- vagy forrásgombbal. Lásd a [Bemenet váltása távirányító nélkül](@hdmi) útmutatót.',
      'Csatlakoztasd a telefonodat ugyanarra a Wi-Fi-re, mint a Fire TV-t.',
      'Töltsd le a Mando TV-t, és nyisd meg az alkalmazást. A Fire TV-d megjelenik a listában. Koppints rá.',
      'A tévé egy 4 számjegyű PIN-t mutat. Írd be a Mando TV-ben. Ezt csak egyszer kell megtenned.',
      'Használd a telefonodon az iránygombokat, az OK-t, a Vissza, a Home gombot, a hangerőt, a lejátszógombokat és a billentyűzetet.',
    ],
    extra=[
      ('Először próbáld ki a tévé távirányítóját (HDMI-CEC)', 'Sok tévétávirányító HDMI-CEC-en keresztül tud vezérelni egy Fire TV Sticket. Ha a Fire TV felülete látszik, nyomd meg a tévé távirányítóján az iránygombokat és az OK-t. Ha nem történik semmi, kapcsold be a CEC-et a tévé beállításaiban (Samsungnál Anynet+, LG-nél SIMPLINK, Sonynál BRAVIA Sync), a Fire TV-n pedig a HDMI-CEC eszközvezérlést a kijelzőbeállításokban („Kijelző és hangok”).'),
      ('Ha Wi-Fi-t cseréltél', 'Távirányító nélkül nem tudod beírni az új Wi-Fi-jelszót a Fire TV-n, de van kiút: hozz létre egy második telefonon hotspotot pontosan ugyanazzal a névvel és jelszóval, mint a régi Wi-Fi-d. A Fire TV magától csatlakozik hozzá. Csatlakoztasd a Mando TV-s telefont ehhez a hotspothoz, párosítsd a PIN-nel, majd a Fire TV-n menj a Beállítások > Hálózat pontra, és válaszd ki az új Wi-Fi-det. Végül a telefonodat is csatlakoztasd az új Wi-Fi-re.'),
      ('Pótló távirányító párosítása', 'A legtöbb új Fire TV távirányító úgy párosítható, hogy a Fire TV közelében körülbelül 10 másodpercig nyomva tartod a Home gombot. Ha nem sikerül, nyisd meg a Beállítások > Vezérlők és Bluetooth-eszközök > Amazon Fire TV távirányítók > Új távirányító hozzáadása menüt. Ezt a menüt a telefonodról is eléred a Mando TV-vel.'),
      ('A tévébe beépített Fire TV', 'A beépített Fire TV-s tévéknél, például sok Insignia és Toshiba modellnél, ugyanezek a lépések működnek, mert maga a tévé a Fire TV.'),
      ('Mielőtt nekilátsz', 'A Fire TV támogatása új a Mando TV-ben. Először frissítsd az alkalmazást. Ha a modelled nem a várt módon reagál, írj nekünk a [Súgó oldalon](@soporte), és add meg a modellt.'),
      ('Ingyenes és Pro', 'A távirányítót ingyen töltheted le és használhatod, reklámok és előfizetés nélkül. A Mando TV Pro opcionális egyszeri vásárlás extrákért.'),
    ],
    marca=('firetv', 'Fire TV távirányító alkalmazás'),
    faq=[
      ('Vezérelhetek Fire TV Sticket a telefonommal a távirányító nélkül?', 'Igen, amíg a Fire TV be van kapcsolva és csatlakozik a Wi-Fi-dhez. A Mando TV a tévén lévő 4 számjegyű PIN-nel párosít, így nincs szükséged a régi távirányítóra.'),
      ('Működik, ha a Fire TV új Wi-Fi-n van?', 'Közvetlenül nem, mert a telefonnak és a Fire TV-nek ugyanazon a hálózaton kell lennie. Előbb hozd vissza online a Fire TV-t az ezen az oldalon leírt hotspot-trükkel.'),
      ('Kell az Amazon Fire TV alkalmazás vagy Amazon-fiók?', 'Nem. A Mando TV az otthoni hálózaton keresztül, PIN-nel csatlakozik, és nincs saját fiókja.'),
    ]),
  dict(clave='turn-on', corto='Tévé bekapcsolása távirányító nélkül', fecha='2026-11-23',
    titulo='Tévé bekapcsolása távirányító nélkül (minden márka)',
    desc='Tévé bekapcsolása távirányító nélkül: hol van a gomb Samsungon, LG-n, TCL-en, Hisense-en és Sonyn. Plusz HDMI-CEC és telefonos trükkök.',
    h1='Így kapcsold be a tévét távirányító nélkül',
    intro='Szinte minden tévén van még fizikai be-/kikapcsoló gomb. Csak jól el van rejtve. Itt látod, hol van minden márkánál, plusz két módot, hogy legközelebb megspórold a keresgélést: a HDMI-CEC egy konzolról vagy streamingeszközről, és a tévé bekapcsolása a telefonoddal Wi-Fi-n.',
    pasos=[
      'Nézz a képernyő közepe alá, közvetlenül a márkalogó mögé. Sok tévén van ott egy kis különálló gomb vagy joystick, lefelé nézve.',
      'Ha ott nincs, tapogass végig a tévé hátoldalán az alsó sarkok közelében, aztán a bal és jobb szélen.',
      'Nyomd meg egyszer a gombot. Sok egygombos tévén bekapcsolt állapotban a rövid nyomás megnyit egy kis menüt a bemenetekhez és a hangerőhöz, a hosszú nyomás pedig kikapcsolja.',
      'Még mindig semmi? Ellenőrizd a hálózati kábelt mindkét végén, és próbálj másik konnektort. Ha a készenléti lámpa nem világít, a tévé nem kap áramot.',
      'Miután a tévé bekapcsolt, állítsd be úgy, hogy többé ne legyen szükséged a gombra: kapcsold be a HDMI-CEC-et és a hálózaton keresztüli bekapcsolást, mindkettőt lejjebb magyarázzuk.',
    ],
    extra=[
      ('Hol van a be-/kikapcsoló gomb, márkánként', 'Samsung: egy vezérlőgomb vagy joystick a képernyő közepe alatt vagy a hátoldalon az egyik alsó sarokban. LG: a legtöbb modellen egy joystickgomb az LG-logó alatt. TCL és Hisense: többnyire egy kis gomb a képernyő közepe alatt vagy a hátoldalon az egyik alsó sarok közelében. Sony: a hátoldalon vagy az egyik oldalélen, alul, a széléhez közel. Vizio: a hátoldalon, alul balra vagy alul jobbra, vagy az oldalán. A helyek modellenként változnak. Ha nem találod, keresd meg a kezelési útmutatót a hátoldali címkén lévő típusszámmal.'),
      ('A tévé bekapcsolása konzollal vagy streamingeszközzel (HDMI-CEC)', 'Bekapcsolt HDMI-CEC mellett egy PlayStation, Xbox, Roku lejátszó, Fire TV Stick vagy Chromecast bekapcsolása a tévét is bekapcsolja, és a megfelelő bemenetre vált. Minden márka másként nevezi a beállítást: Samsungnál Anynet+, LG-nél SIMPLINK, Sonynál BRAVIA Sync, a legtöbb másnál CEC. Többet olvashatsz a [Tévé bekapcsolása és váltás a konzol HDMI-bemenetére](@console) útmutatóban.'),
      ('A tévé bekapcsolása a telefonoddal', 'Az okostévék Wi-Fi-n felébreszthetők, ha ezt egyszer engedélyezed, és akkor a Mando TV a telefonodról bekapcsolja őket. Samsungnál kapcsold be a „Bekapcsolás mobilról” opciót a Beállítások > Általános > Hálózat > Szakértői beállítások menüben. LG-nél kapcsold be a „Tévé bekapcsolása mobilról” opciót ([lépésről lépésre](@lg-on)). Roku TV-nél kapcsold be a „TV gyorsindítás” opciót a Beállítások > Rendszer > Energia menüben. Google TV-nél és Android TV-nél keresd a Wake on LAN vagy a „Bekapcsolás hálózaton keresztül” opciót, ha a modelled rendelkezik vele. Ezt egyszer kell megtenned, bekapcsolt tévénél.'),
      ('Ha nem találsz gombot', 'Néhány újabb tévé olyan jól elrejti az egyetlen gombot, hogy úgy tűnik, nincs is. Keress egy kis dudort vagy fényérzékelő területet a képernyő alatt: a gomb gyakran közvetlenül mellette van. Wi-Fi-n a Mando TV-nek az kell, hogy a tévé egyszer be legyen kapcsolva és csatlakoztatva. Kivétel az infravörös: infravörös adós Android telefonon a Mando TV be tud kapcsolni egy sosem beállított tévét is, amíg a tévére irányítod a telefont. Az infravörös új, és az alkalmazás kódlistájában szereplő márkákkal működik.'),
      ('Ingyenes és Pro', 'A távirányítót ingyen töltheted le és használhatod, reklámok és előfizetés nélkül. A Mando TV Pro opcionális egyszeri vásárlás extrákért.'),
    ],
    marca=None,
    faq=[
      ('Bekapcsolhatok a telefonommal egy tévét, amelyet sosem állítottam be?', 'Wi-Fi-n nem. A kikapcsolt tévé csak akkor ébred fel a hálózatról, ha a hálózaton keresztüli bekapcsolás előtte be volt kapcsolva. Az első alkalommal használd a tévén lévő gombot. A kivétel egy infravörös adós Android telefon: a Mando TV beállítás nélkül is be tud kapcsolni egy tévét infravörösön, ha a márka szerepel a kódlistán, vagy az „Más márka vagy nem tudom” lehetőséget választod.'),
      ('Hogyan kapcsolok be egy Samsung tévét távirányító nélkül?', 'Nyomd meg a vezérlőgombot a képernyő közepe alatt vagy a hátoldalon az egyik alsó sarokban. Utána kapcsold be a „Bekapcsolás mobilról” opciót, hogy legközelebb a telefonod be tudja kapcsolni.'),
      ('Hogyan kapcsolok be egy Roku TV-t távirányító nélkül?', 'Használd a tévén lévő gombot, többnyire a közepe alatt vagy a hátoldalon. Utána kapcsold be a „TV gyorsindítás” opciót a Beállítások > Rendszer > Energia menüben, hogy a Mando TV a telefonodról be tudja kapcsolni.'),
      ('Miért kapcsol be magától a tévém, ha bekapcsolom a konzolt?', 'Ez a HDMI-CEC. Kényelmes, és a tévé beállításaiban kikapcsolhatod, ha inkább úgy szeretnéd.'),
    ]),
  dict(clave='sony', corto='Sony távirányító', fecha='2026-11-23',
    titulo='Sony távirányító alkalmazás telefonra és számítógépre',
    desc='A Mando TV Wi-Fi-n vezérli a Google TV-s vagy Android TV-s Sony Bravia tévéket. Béta támogatás a 2013 és 2015 közötti, Android nélküli modellekhez.',
    h1='Így vezérelheted a Sony tévédet a telefonoddal',
    intro='Az újabb Sony Bravia okostévék Google TV-t használnak, a 2015-től készült régebbi modellek Android TV-t. A Mando TV mindkettőt vezérli a Wi-Fi-n keresztül iPhone-ról, Android telefonról vagy Windows-számítógépről. Az alkalmazás kiváltja az eredeti távirányítót, ha elveszett, vagy lemerült az eleme.',
    pasos=[
      'Ellenőrizd, hogy a Sony tévéd a Google TV vagy az Android TV kezdőképernyőjét mutatja-e. Ez a legtöbb 2015-től készült Sony Bravia okostévére igaz.',
      'Csatlakoztasd a telefonodat és a tévét ugyanarra a Wi-Fi-re.',
      'Nyisd meg a Mando TV-t, és koppints a listában a Sony tévédre.',
      'Írd be a 6 karakteres kódot, amelyet a tévé a képernyőn mutat (csak az első alkalommal). Ehhez nincs szükséged távirányítóra.',
      'Használd az iránygombokat, az OK-t, a Vissza, a Home gombot, a hangerőt és a billentyűzetet.',
    ],
    extra=[
      ('Sony tévé bekapcsolása a telefonról', 'A Google TV-s vagy Android TV-s Sony modellek felébreszthetők a hálózaton keresztül, ha be van kapcsolva a „Távoli indítás”. Az opciót többnyire a Beállítások > Hálózat és internet > Távoli indítás menüben találod (az útvonal modellenként kissé eltérhet). Utána koppints a Mando TV-ben a tévére, amíg ki van kapcsolva, és az alkalmazás bekapcsolja.'),
      ('Hol van a be-/kikapcsoló gomb egy Sonyn', 'A legtöbb Bravia tévén a hátoldalon van, az alsó bal vagy jobb sarok közelében, vagy az egyik oldalélen. A rövid nyomás bekapcsolja a tévét. Többet olvashatsz a [Tévé bekapcsolása távirányító nélkül](@turn-on) útmutatóban.'),
      ('Régebbi Sony tévék', 'A 2013 és 2015 közötti, Androidot nem használó Sony Bravia tévéket a Mando TV bétaállapotban támogatja. Ez új, és még lehetnek hibái. A tévé egy 4 számjegyű PIN-t mutat, amelyet be kell írnod az alkalmazásban. A Google TV vagy Android TV nélküli többi Sony tévét jelenleg nem támogatjuk.'),
      ('Ingyenes és Pro', 'A távirányítót ingyen töltheted le és használhatod, reklámok és előfizetés nélkül. A Mando TV Pro opcionális egyszeri vásárlás extrákért.'),
    ],
    marca='android',
    faq=[
      ('Működik a Mando TV Sony Bravia tévékkel?', 'Igen, a Google TV-t vagy Android TV-t használó Sony tévékkel. Ide tartozik a legtöbb 2015-től készült Sony okostévé.'),
      ('Kell Sony-alkalmazás vagy Google-fiók?', 'Nem. A Mando TV a tévé képernyőjén lévő kóddal párosít, és nem kér fiókot.'),
      ('Működik régebbi, Android nélküli Sony Bravia tévékkel?', 'Igen, bétaállapotban, a 2013 és 2015 közötti, Android nélküli Bravia modelleknél. A párosítás a tévén megjelenő 4 számjegyű PIN-nel történik.'),
      ('Gépelhetek a Sony tévén a telefonomról?', 'Igen. A telefon billentyűzete ingyenes, és a tévé keresőjébe meg más szövegmezőkbe gépel. A YouTube-hoz a Mando TV-ben van YouTube-billentyűzet is: írd be vagy mondd el, mit nézzél, és a YouTube megnyílik a tévén az eredményekkel. A Netflix csak a saját képernyőn megjelenő billentyűzetét fogadja el, ezért ott az iránygombokat és az OK-t használd.'),
    ]),
  dict(clave='tcl', corto='TCL távirányító', fecha='2026-11-23',
    titulo='TCL távirányító alkalmazás telefonra és számítógépre',
    desc='Elveszett a TCL távirányító? A legtöbb TCL tévé Roku TV-t vagy Google TV-t használ. A Mando TV mindkettőt vezérli Wi-Fi-n, fiók és reklámok nélkül.',
    h1='Így vezérelheted a TCL tévédet a telefonoddal',
    intro='A TCL gyártja a tévét, de a szoftver Roku TV vagy Google TV (régebbi modelleknél Android TV). A Mando TV mindkét rendszert vezérli, és a Wi-Fi-n keresztül távirányítóként működik a TCL tévédhez. Ingyen, fiók és reklámok nélkül.',
    pasos=[
      'Derítsd ki, melyik rendszert használja a TCL-ed. Ha a kezdőképernyő csatornacsempék egyszerű rácsát mutatja, Roku TV. Ha úgy néz ki, mint a Google TV vagy az Android TV ajánlásokkal teli sorokkal, akkor Google TV.',
      'Csatlakoztasd a telefonodat és a TCL tévét ugyanarra a Wi-Fi-re.',
      'Nyisd meg a Mando TV-t. A TCL magától megjelenik a listában. Koppints rá.',
      'Roku TV-s TCL-nél nincs más teendő. Google TV-s TCL-nél írd be a 6 karakteres kódot, amelyet a tévé a képernyőn mutat (csak az első alkalommal).',
      'Használd az iránygombokat, az OK-t, a Vissza, a Home gombot, a hangerőt és a billentyűzetet. Kapcsold be a tévét az alkalmazásból, ha bekapcsoltad a hálózaton keresztüli bekapcsolást (lásd lent).',
    ],
    extra=[
      ('TCL tévé bekapcsolása a telefonról', 'TCL Roku TV-nél kapcsold be a „TV gyorsindítás” opciót a Beállítások > Rendszer > Energia menüben. TCL Google TV-nél keress egy Wake on LAN, „Bekapcsolás hálózaton keresztül” vagy távoli indítás opciót a hálózati vagy energiabeállításokban. Néhány modell ezt nem kínálja. Ilyenkor kapcsold be a tévét a fizikai be-/kikapcsoló gombbal, többnyire alul középen vagy a hátoldalon.'),
      ('Ha a TCL-ed nem jelenik meg', 'Ellenőrizd, hogy a telefon és a tévé ugyanazon a Wi-Fi-n van-e. A külön 2,4 GHz-es és 5 GHz-es hálózatú routerek elrejthetik egymás elől az eszközöket. iPhone-on engedélyezd a „Helyi hálózat” opciót a Mando TV-nek a Beállításokban. A tévét az IP-címének megadásával is hozzáadhatod. Olvasd el a [A telefonod nem találja a tévét](@not-found) útmutatót.'),
      ('Továbbiak a TCL-edről', 'Roku TV-s TCL-hez lásd a [Roku távirányító alkalmazás](@roku) oldalt, Google TV-s vagy Android TV-s TCL-hez az [Android TV távirányító alkalmazás](@android) oldalt.'),
      ('Ingyenes és Pro', 'Az iránygombok, az OK, a Vissza, a Home, a hangerő, a csatornák, a számok, a billentyűzet, az appok megnyitása, a bemenetek váltása és a be-/kikapcsolás ingyenes, reklámok és előfizetés nélkül. Az érintőpad, a hangparancsok, a kedvenc appok, a rutinok és a kikapcsolási időzítő a Mando TV Pro részei, amely egyszeri vásárlás előfizetés nélkül.'),
    ],
    marca=None,
    faq=[
      ('Működik a Mando TV minden TCL tévével?', 'Működik Roku TV-s, Google TV-s vagy Android TV-s TCL tévékkel, vagyis a legtöbb TCL okostévével. Az olyan TCL, amely nem okostévé, nem vezérelhető Wi-Fi-n.'),
      ('Kell a TCL alkalmazás vagy TCL-fiók?', 'Nem. A Mando TV közvetlenül az otthoni Wi-Fi-n keresztül csatlakozik, és nem kér fiókot.'),
      ('A TCL-em kódot kér. Hol van?', 'A Google TV-s és Android TV-s TCL modellek egy 6 karakteres kódot mutatnak a képernyőn. Pontosan úgy írd be a Mando TV-ben. A Roku TV-s TCL nem kér kódot.'),
    ]),
  dict(clave='hisense', corto='Hisense távirányító', fecha='2026-11-23',
    titulo='Hisense távirányító alkalmazás: mi működik a telefonon',
    desc='Hisense távirányító a Mando TV-vel: VIDAA, Roku TV, Google TV és Fire TV vezérlése Wi-Fi-n. Őszinte áttekintés arról, mi működik.',
    h1='Hisense távirányító alkalmazás: mi működik és mi nem',
    intro='A Hisense tévék belül nem egyformák. Modelltől függően a Hisense saját VIDAA rendszerét, Roku TV-t, Google TV-t vagy Fire TV-t használják. A Mando TV mind a négy rendszeren működik Hisense távirányítóként, néhány újabb VIDAA modell kivételével. Itt megtudod, hogyan ismered fel, melyik rendszered van, és mire számíthatsz.',
    pasos=[
      'Nézd meg, melyik rendszert használja a Hisense-ed. A VIDAA a Hisense saját felülete. A Roku TV csatornacsempék rácsát mutatja. A Google TV ajánlásokkal teli sorokat mutat. A Fire TV az Amazon-sorokkal teli Fire TV kezdőképernyőt mutatja.',
      'Csatlakoztasd a telefonodat és a Hisense tévét ugyanarra a Wi-Fi-re.',
      'Nyisd meg a Mando TV-t. A tévé magától megjelenik a listában. Koppints rá.',
      'A VIDAA-s és Fire TV-s modellek négyjegyű PIN-kódot kérhetnek, a Google TV 6 karakteres kódot mutat. Írd be az alkalmazásba. A Roku TV nem kér semmit. Ezt csak egyszer kell megtenned.',
      'Használd a telefonodról az iránygombokat, az OK-t, a Vissza, a Home gombot, a hangerőt és a billentyűzetet.',
    ],
    extra=[
      ('Hisense Roku TV-vel vagy Google TV-vel', 'Ezek teljesen úgy működnek, mint bármelyik másik Roku vagy Google TV tévé. A részleteket a [Roku távirányító alkalmazás](@roku) és az [Android TV távirányító alkalmazás](@android) oldalon találod.'),
      ('Hisense Fire TV-vel', 'A Fire TV támogatása új a Mando TV-ben. Frissítsd az alkalmazást a legújabb verzióra az áruházadból. Azt, hogyan működik a PIN-kódos párosítás, a [Fire TV távirányító alkalmazás](@firetv) oldalon olvashatod. Ha valami nem úgy működik, ahogy várod, írj nekünk a Súgó oldalon, és add meg a modelledet.'),
      ('Hisense VIDAA-val', 'A legtöbb VIDAA modell működik: gombok, hangerő, billentyűzet, appok és bemenetek. Néhány újabb VIDAA modell csak a hivatalos Hisense alkalmazást fogadja el. A Mando TV ezt csatlakozáskor felismeri, és világosan megmondja, ahelyett hogy csendben cserbenhagyna. Ilyenkor a modelledhez való Hisense alkalmazás, a tévén lévő gombok vagy az eredeti távirányító a megoldás.'),
      ('Hisense bekapcsolása a telefonról', 'Hisense Roku TV-nél kapcsold be a „TV gyorsindítás” opciót a Beállítások > Rendszer > Energia menüben. Google TV-nél keress egy Wake on LAN vagy „Bekapcsolás hálózaton keresztül” opciót. Ha nincs ilyen, használd a tévén lévő be-/kikapcsoló gombot.'),
      ('Ingyenes és Pro', 'Az iránygombok, az OK, a Vissza, a Home, a hangerő, a csatornák, a számgombok, a billentyűzet, az appok megnyitása, a bemenetek váltása és a be- vagy kikapcsolás ingyenes, reklámok és előfizetés nélkül. Az érintőpad, a hangparancsok, a kedvenc appok, a rutinok és a kikapcsolási időzítő a Mando TV Pro részei, amely egyszeri vásárlás előfizetés nélkül.'),
    ],
    marca=None,
    faq=[
      ('Működik a Mando TV Hisense VIDAA-val?', 'Igen, a legtöbb VIDAA modellel. Néhány újabb csak a hivatalos Hisense alkalmazást fogadja el. A Mando TV ezt felismeri, és megmondja neked. A Roku TV-s, Google TV-s vagy Fire TV-s Hisense tévék szintén támogatottak.'),
      ('Honnan tudom, hogy a Hisense-em Roku TV, Google TV vagy Fire TV?', 'Nézd meg a kezdőképernyőt. A Roku TV egyszerű csempe-rácsot mutat, és indításkor Roku-logót. A Google TV ajánlásokkal teli sorokat mutat. A Fire TV az Amazon Fire TV kezdőképernyőjét mutatja. A modellnevet a Beállítások > Névjegy menüben is megtalálod.'),
      ('Kell Hisense- vagy Google-fiók?', 'Nem. A Mando TV közvetlenül az otthoni Wi-Fi-n keresztül csatlakozik, és nincs saját fiókja.'),
    ]),
  dict(clave='philips', corto='Philips távirányító', fecha='2026-11-23',
    titulo='Philips távirányító alkalmazás: Roku TV, Google TV, Android TV',
    desc='A Mando TV Wi-Fi-n vezérli a Roku TV-s, Google TV-s vagy Android TV-s Philips tévéket telefonról vagy számítógépről. A Titan OS nem támogatott.',
    h1='Így vezérelheted a Philips tévédet a telefonoddal',
    intro='A Philips tévék országtól és gyártási évtől függően különböző rendszereket használnak: Roku TV az Egyesült Államokban, Google TV vagy Android TV sok országban, és Titan OS néhány újabb európai modellen. A Mando TV Wi-Fi-n vezérli a Roku TV-s, Google TV-s és Android TV-s modelleket.',
    pasos=[
      'Nézd meg a kezdőképernyőt. A Roku TV csempék rácsát mutatja. A Google TV és az Android TV a Google ajánlásaival teli sorokat mutat. A Titan OS saját kezdőképernyővel rendelkezik.',
      'Csatlakoztasd a telefonodat és a tévét ugyanarra a Wi-Fi-re.',
      'Nyisd meg a Mando TV-t, és a listában koppints a Philips tévédre.',
      'A Roku TV nem kér semmit. A Google TV és az Android TV 6 karakteres kódot mutat: írd be egyszer az alkalmazásba.',
      'Használd az iránygombokat, az OK-t, a Vissza, a Home gombot, a hangerőt és a billentyűzetet.',
    ],
    extra=[
      ('Philips Roku TV', 'Úgy működik, mint bármelyik Roku tévé. A telefonról való bekapcsoláshoz kapcsold be a „TV gyorsindítás” opciót a Beállítások > Rendszer > Energia menüben. Továbbiak a [Roku távirányító alkalmazás](@roku) oldalon.'),
      ('Philips Google TV-vel vagy Android TV-vel', 'Sok Ambilight modell idetartozik. A képernyőn lévő kóddal párosodnak. A telefonról való bekapcsoláshoz keress Wake on LAN vagy „Bekapcsolás hálózaton keresztül” opciót a hálózati vagy energiabeállításokban. Néhány modellen ez az opció hiányzik. Továbbiak az [Android TV távirányító alkalmazás](@android) oldalon.'),
      ('Régebbi, nem Android-os Philips tévék', 'A 2011 és 2015 közötti, Androidot nem használó Philips tévék támogatása a Mando TV-ben béta. Új, és nem kér párosítási kódot.'),
      ('Philips Titan OS-szel', 'A Titan OS egy másik rendszer, amelyet a Mando TV ma nem vezérel, és ezt inkább világosan kimondjuk. Az újabb, nem Android-os Philips modellek szintén nincsenek lefedve.'),
      ('Ingyenes és Pro', 'A távirányítót ingyen töltheted le és használhatod, reklámok és előfizetés nélkül. A Mando TV Pro opcionális egyszeri vásárlás extrákért.'),
    ],
    marca=None,
    faq=[
      ('Működik a Mando TV Philips tévékkel?', 'Roku TV-t, Google TV-t vagy Android TV-t használó Philips tévékkel igen, a 2011 és 2015 közötti, Android nélküli Philips tévékkel pedig bétában. A Titan OS-es modellek nem támogatottak.'),
      ('Vezérli a Mando TV az Ambilightot?', 'A Mando TV távirányító: elküldi a gombokat, így a nyilakkal és az OK-val eljuthatsz az Ambilight beállításaihoz. Külön Ambilight vezérlők nincsenek.'),
      ('Kell Philips- vagy Google-fiók?', 'Nem. A Mando TV az otthoni Wi-Fi-n keresztül csatlakozik, és nem kér fiókot.'),
    ]),
]
OTRAS_GUIAS += [
  ('no-sub', 'Távirányító alkalmazás előfizetés és reklámok nélkül'),
  ('roku-app-alt', 'A Roku alkalmazás alternatívája: egy minden tévéhez'),
  ('lg-thinq', 'Az LG ThinQ alkalmazás alternatívája az LG tévédhez'),
  ('smartthings', 'SmartThings-alternatíva Samsung tévékhez'),
  ('googletv-alt', 'A Google TV telefonos távirányítójának alternatívája'),
  ('windows', 'Távirányító alkalmazás Windows-számítógéphez'),
  ('iphone', 'Távirányító alkalmazás iPhone-ra: egy minden tévéhez'),
  ('firetv', 'Fire TV távirányító a telefonodra vagy számítógépedre'),
  ('firetv-lost', 'Elveszett Fire TV távirányító: így használd a telefonod'),
  ('turn-on', 'Így kapcsold be a tévét távirányító nélkül'),
  ('sony', 'Így vezérelheted a Sony tévédet a telefonoddal'),
  ('tcl', 'Így vezérelheted a TCL tévédet a telefonoddal'),
  ('hisense', 'Hisense távirányító alkalmazás: mi működik és mi nem'),
  ('philips', 'Így vezérelheted a Philips tévédet a telefonoddal'),
]
# <<< guías traídas del inglés
