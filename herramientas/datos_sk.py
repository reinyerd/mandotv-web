# Textos en eslovaco (vykanie) de mandotv.app. Los usa generar_idiomas.py. Escritos para las búsquedas de Eslovaquia.
# Las claves de las páginas (lg, lost-tv, ...) y sus rutas están en idiomas_sitio.py.
# Los nombres de menús de cada marca (LG, Samsung, Roku, Android TV, iPhone) son los mismos que usa la app en eslovaco
# (lib/l10n/app_sk.arb del proyecto de la app).

UI = dict(
  locale='sk_SK',
  aria_home='Mando TV, domovská stránka', aria_main='Hlavná ponuka', nav_que='Funkcie', nav_ayuda='Pomoc', nav_contacto='Kontakt',
  asunto='Ahoj%20Mando%20TV', inicio='Domov', privacidad='Ochrana súkromia', aria_pie='Pätička stránky', aria_ruta='Navigačná cesta',
  aria_marcas='Značky a návody', hecho='Vyvinuté v Čile',
  aviso='Mando TV je nezávislá aplikácia. Nie je prepojená ani podporovaná uvedenými výrobcami televízorov, ani spoločnosťami Google, Amazon, Apple či Roku. Značky patria ich vlastníkom a uvádzajú sa len na vyznačenie kompatibility. Android TV a Google TV sú ochranné známky spoločnosti Google LLC. Apple TV je ochranná známka spoločnosti Apple Inc.',
  bajar='Stiahnuť zadarmo', descarga='Stiahnuť z', anticipada='Predbežný prístup na',
  apple_aria='Stiahnuť Mando TV zadarmo z App Store', ms_aria='Stiahnuť Mando TV zadarmo z Microsoft Store',
  gp_aria='Predbežný prístup k Mando TV v Google Play pre Android', aria_desc='Stiahnuť Mando TV',
  b_como_btn='Ako sa pripojiť', b_tiendas_label='K dispozícii v obchodoch',
  b_nota='iPhone, iPad, Mac, Android a Windows. Stiahnutie zadarmo, bez reklám. Pro je jednorazový nákup, bez predplatného.',
  b_compat='Kompatibilné televízory', b_otras='Ďalšie značky', b_otras_p='Mando TV ovláda všetky tieto značky jednou aplikáciou:',
  g_guias='Návody', g_ver='Pozrieť postup', g_pasos='Krok za krokom', g_hazlo='Ako na to s Mando TV',
  g_tiendas='Mando TV je univerzálny ovládač pre váš televízor. Stiahnite si ho zadarmo, bez reklám a bez účtu. Pro je voliteľný jednorazový nákup, bez predplatného. Pre iPhone, iPad, Windows a Android:',
  g_nota='Android: bezplatný predbežný prístup v Google Play. <a href="{enlace}">Zapojte sa v dvoch krokoch</a> a pomôžte nám dostať sa do obchodu.',
  g_mas_pagina='Viac podrobností nájdete na stránke {enlace}.', g_mas_marca='Viac podrobností podľa značky:',
  g_faq='Časté otázky', g_mas='Ďalšie návody', g_todas='Všetky návody', g_ayuda='Pomoc a podpora',
  g_idiomas='Tento návod v iných jazykoch',
)

# Pie de página y listas de marcas/guías: (clave, texto)
PIE = [
  ('samsung', 'Ovládač Samsung TV'),
  ('lg', 'Ovládač LG TV'),
  ('roku', 'Ovládač Roku'),
  ('android', 'Ovládač Android TV'),
  ('guias', 'Všetky návody'),
  ('lost-tv', 'Stratený ovládač'),
  ('lost-lg', 'Stratený ovládač LG'),
  ('lg-on', 'Zapnutie televízora LG mobilom'),
  ('hdmi', 'Zmena vstupu HDMI bez ovládača'),
  ('androidtv', 'Android TV bez ovládača'),
  ('console', 'Televízor a HDMI konzoly bez ovládača'),
  ('samsung-lost', 'Samsung TV bez ovládača'),
  ('roku-lost', 'Stratený ovládač Roku'),
  ('roku-403', 'Aplikácia Roku nefunguje'),
  ('androidtv-code', 'Párovací kód Android TV'),
  ('not-found', 'Mobil nenájde televízor'),
  ('wifi', 'Mobil ako ovládač cez Wi-Fi'),
  ('pc', 'Ovládanie televízora z počítača'),
]
NOMBRE_OTRA = {'lg': 'Aplikácia ovládač LG TV', 'samsung': 'Aplikácia ovládač Samsung TV', 'roku': 'Aplikácia ovládač Roku',
               'android': 'Aplikácia ovládač Android TV a Google TV'}
PAGINA_MARCA = {'lg': 'Aplikácia ovládač LG TV', 'samsung': 'Aplikácia ovládač Samsung TV', 'roku': 'Aplikácia ovládač Roku',
                'android': 'Aplikácia ovládač Android TV'}

OTRAS_GUIAS = [
  ('lg-on', 'Zapnutie televízora LG mobilom'),
  ('lost-tv', 'Stratený ovládač: čo môžete urobiť'),
  ('lost-lg', 'Stratený ovládač LG: použite mobil'),
  ('hdmi', 'Zmena vstupu HDMI na televízore bez ovládača'),
  ('androidtv', 'Android TV bez ovládača: použite mobil'),
  ('console', 'Zapnutie televízora a prepnutie na HDMI konzoly bez ovládača'),
  ('samsung-lost', 'Samsung TV bez pôvodného ovládača: použite mobil'),
  ('roku-lost', 'Stratený ovládač Roku: použite mobil'),
  ('roku-403', 'Aplikácia Roku nefunguje: oprava chyby 403'),
  ('androidtv-code', 'Android TV žiada párovací kód: čo robiť'),
  ('not-found', 'Mobil nenájde televízor: čo skontrolovať'),
  ('wifi', 'Ako použiť mobil ako ovládač cez Wi-Fi'),
  ('pc', 'Ako ovládať televízor počítačom s Windowsom'),
]

INDICE = dict(
  titulo='Návody: ovládanie televízora mobilom | Mando TV',
  desc='Návody krok za krokom: použite mobil alebo počítač ako ovládač, zapnite televízor, prepnite HDMI a vyriešte problémy so Samsung, LG a Roku.',
  h1='Návody: mobil ako ovládač televízora',
  intro='Jednoduché postupy, ako pripojiť ovládač televízora Samsung, LG, Roku alebo Android TV cez Mando TV, zapnúť televízor a vyriešiť problémy.',
  h2_guias='Všetky návody', h2_marcas='Aplikácia ovládač podľa značky',
  marcas_extra=[('sony', 'Aplikácia ovládač Sony'), ('philips', 'Aplikácia ovládač Philips')],
)

MARCAS = [
  dict(clave='lg', color='#e0457b', corto='LG',
    titulo='Ovládač LG TV v mobile, zadarmo | Mando TV',
    desc='Mobil alebo PC ako diaľkový ovládač LG TV s webOS cez Wi-Fi. Tlačidlá, klávesnica, aplikácie, vstupy a zapnutie zadarmo; kurzor s Pro.',
    h1='Ovládač LG TV ako aplikácia v mobile',
    intro='Mando TV je aplikácia ovládač pre televízory LG: cez domácu sieť Wi-Fi z mobilu alebo počítača urobí diaľkový ovládač vášho televízora LG so systémom webOS. Hodí sa, keď ste ovládač stratili, vybili sa batérie alebo chcete písať rýchlejšie.',
    compat='Televízory LG Smart TV so systémom webOS (väčšina modelov LG Smart TV od roku 2014). Funguje s televízormi LED, NanoCell, QNED aj OLED. Staršie televízory LG so systémom NetCast (2011 až 2014, pred webOS) sú nová podpora v beta verzii: párujú sa 6-miestnym kľúčom, ktorý televízor zobrazí.',
    h2=dict(funciones='Čo môžete robiť s televízorom LG', como='Ako pripojiť televízor LG k Mando TV',
            encender='Zapnutie televízora LG mobilom', preguntas='Otázky o LG', guias='Návody pre LG'),
    funciones=[
      ('Všetky tlačidlá', 'Smerové tlačidlá, OK, späť, domov, hlasitosť, kanály, stlmenie a prehrávanie.'),
      ('Kurzor ako pri Magic Remote (Pro)', 'Šípku posúvate prstom po obrazovke, presne ako s diaľkovým ovládačom LG Magic Remote.'),
      ('Klávesnica', 'Píšte v YouTube, Netflixe alebo v prehliadači televízora na klávesnici mobilu.'),
      ('Aplikácie a vstupy', 'Otvorte svoje aplikácie a prepnite na HDMI, živé vysielanie, AirPlay alebo Screen Share.'),
      ('Výstup zvuku (Pro)', 'Prepínajte medzi reproduktormi televízora a soundbarom.'),
      ('Zapnutie televízora', 'Ak je vypnutý, Mando TV ho zapne cez sieť a pripojí sa samo.'),
    ],
    pasos=[
      'Pripojte mobil a televízor k tej istej sieti Wi-Fi.',
      'Otvorte Mando TV: váš televízor LG sa v zozname zobrazí sám. Klepnite naň.',
      'Na televízore sa zobrazí výzva so žiadosťou o povolenie. Potvrďte ju svojím bežným ovládačom (len pri prvom pripojení).',
    ],
    encender='Zapnite „Turn on TV with Mobile“ (na niektorých modeloch sa volá „Turn on via Wi-Fi“). Nájdete ho v Settings > General > Devices > External Devices (na starších modeloch Connection > Mobile Connection Management). Potom sa vás aplikácia po klepnutí na vypnutý televízor v Mando TV opýta, či ho má zapnúť, a pripojí sa sama.',
    faq=[
      ('Potrebujem na používanie Mando TV ovládač Magic Remote?', 'Len pri prvom pripojení, aby ste potvrdili výzvu na obrazovke. Potom vám stačí mobil.'),
      ('Nahrádza Mando TV aplikáciu LG ThinQ?', 'Na ovládanie televízora áno: nepotrebujete účet LG ani registráciu televízora. Mando TV sa pripája priamo cez vašu sieť Wi-Fi.'),
      ('Môžem televízor LG zapnúť mobilom?', 'Áno, ak ste na televízore zapli „Turn on TV with Mobile“ a raz ste sa pripojili, keď bol televízor zapnutý.'),
      ('Funguje to so staršími televízormi LG spred webOS?', 'V beta verzii áno, s televízormi LG Smart TV so systémom NetCast z rokov 2011 až 2014. Párujú sa 6-miestnym kľúčom, ktorý televízor zobrazí. Funkcia je nová a môže mať ešte svoje nedostatky.'),
    ],
    guias=[('lg-on', 'Ako zapnúť televízor LG mobilom'),
           ('lost-lg', 'Stratený ovládač LG: použite mobil'),
           ('hdmi', 'Zmena vstupu HDMI na televízore bez ovládača'),
           ('guias', 'Všetky návody na ovládanie televízora mobilom')]),
  dict(clave='samsung', color='#3d7bff', corto='Samsung',
    titulo='Ovládač Samsung TV v mobile | Mando TV',
    desc='Mobil alebo PC ako diaľkový ovládač Samsung TV s Tizen cez Wi-Fi. Tlačidlá, klávesnica, aplikácie a zapnutie zadarmo; touchpad s Pro. Bez reklám.',
    h1='Ovládač Samsung TV ako aplikácia v mobile',
    intro='Mando TV je aplikácia ovládač pre televízory Samsung: cez domácu sieť Wi-Fi z mobilu alebo počítača urobí diaľkový ovládač vášho televízora Samsung Smart TV. Nepotrebujete účet Samsung ani registráciu televízora.',
    compat='Televízory Samsung Smart TV so systémom Tizen, rok výroby 2016 a novšie (rady ako Crystal UHD, QLED, Neo QLED, The Frame a OLED).',
    h2=dict(funciones='Čo môžete robiť s televízorom Samsung', como='Ako pripojiť televízor Samsung k Mando TV',
            encender='Zapnutie televízora Samsung mobilom', preguntas='Otázky o Samsung', guias='Návody pre Samsung'),
    funciones=[
      ('Všetky tlačidlá', 'Smerové tlačidlá, OK, späť, domov, hlasitosť, kanály, stlmenie a zdroj.'),
      ('Touchpad (Pro)', 'Prstom prechádzajte ponukami bez hľadania smerových tlačidiel.'),
      ('Klávesnica', 'Vyhľadávané výrazy a heslá píšte na klávesnici mobilu.'),
      ('Aplikácie', 'Netflix, YouTube, Prime Video a ďalšie aplikácie otvoríte jedným klepnutím.'),
      ('Zapnutie televízora', 'Ak je vypnutý, Mando TV ho zapne cez sieť a pripojí sa samo.'),
      ('Bez účtu', 'Pripojenie ide priamo cez vašu sieť Wi-Fi, bez obchádzky cez internet.'),
    ],
    pasos=[
      'Pripojte mobil a televízor k tej istej sieti Wi-Fi.',
      'Otvorte Mando TV: váš televízor Samsung sa v zozname zobrazí sám. Klepnite naň.',
      'Televízor sa opýta, či pripojenie povoliť. Ovládačom vyberte „Allow“ (len pri prvom pripojení).',
    ],
    encender='Na televízore Samsung zapnite v Nastavenia > General > Network > Expert Settings možnosť „Power On with Mobile“. Potom sa vás aplikácia po klepnutí na vypnutý televízor v Mando TV opýta, či ho má zapnúť, a pripojí sa sama.',
    faq=[
      ('Povolenie som omylom odmietol. Čo mám robiť?', 'Na televízore prejdite do Settings > General > External Device Manager > Device Connection Manager a nastavte Mando TV ako povolené.'),
      ('Nahrádza Mando TV aplikáciu SmartThings?', 'Na ovládanie televízora áno, a to bez účtu Samsung. Mando TV sa pripája priamo cez vašu sieť Wi-Fi.'),
      ('Funguje to so staršími televízormi Samsung?', 'Funguje s televízormi Samsung so systémom Tizen, rok výroby 2016 a novšie. Staršie modely používajú iný systém, ktorý zatiaľ nepodporujeme.'),
    ],
    guias=[('samsung-lost', 'Samsung TV bez pôvodného ovládača: použite mobil'),
           ('smartthings', 'Alternatíva k SmartThings pre televízory Samsung'),
           ('turn-on', 'Ako zapnúť televízor bez ovládača'),
           ('hdmi', 'Zmena vstupu HDMI na televízore bez ovládača'),
           ('guias', 'Všetky návody na ovládanie televízora mobilom')]),
  dict(clave='roku', color='#a77bff', corto='Roku',
    titulo='Ovládač Roku v mobile, zadarmo | Mando TV',
    desc='Mobil alebo PC ako diaľkový ovládač Roku TV a Roku Player cez Wi-Fi. Tlačidlá, klávesnica, kanály, vstupy a zapnutie zadarmo.',
    h1='Ovládač Roku ako aplikácia v mobile',
    intro='Mando TV je aplikácia ovládač pre Roku: cez domácu sieť Wi-Fi z mobilu alebo počítača urobí diaľkový ovládač vášho Roku. Funguje s televízormi Roku TV aj s prehrávačmi Roku pripojenými cez HDMI.',
    compat='Televízory Roku TV (TCL, Hisense, Philips, Sharp, JVC a ďalšie) a prehrávače Roku (Express, Streaming Stick, Ultra).',
    h2=dict(funciones='Čo môžete robiť s Roku', como='Ako pripojiť Roku k Mando TV',
            encender='Zapnutie Roku mobilom', preguntas='Otázky o Roku', guias='Návody pre Roku'),
    funciones=[
      ('Všetky tlačidlá', 'Smerové tlačidlá, OK, späť, domov, hlasitosť, stlmenie, opakovanie a prehrávanie.'),
      ('Klávesnica', 'Vyhľadávané výrazy v kanáloch Roku píšte na klávesnici mobilu.'),
      ('Kanály', 'Netflix, YouTube a ďalšie kanály Roku otvoríte jedným klepnutím.'),
      ('Vstupy', 'Na Roku TV prepínajte v aplikácii medzi HDMI, anténou alebo AV.'),
      ('Zapnutie televízora', 'Na televízoroch Roku TV s rýchlym štartom ich Mando TV zapne z mobilu.'),
      ('Bez párovania', 'Roku nežiada kód: klepnite naň v zozname a ste pripojení.'),
      ('Zvonenie ovládača', 'Ak má váš ovládač Roku reproduktor, napríklad Roku Voice Remote Pro, Mando TV ho rozozvučí, aby ste ho našli. Zadarmo, Roku musí byť zapnuté.'),
    ],
    pasos=[
      'Pripojte mobil a Roku k tej istej sieti Wi-Fi.',
      'Otvorte Mando TV: vaše Roku sa v zozname zobrazí samo. Klepnite naň.',
      'Ak pripojenie nefunguje, na Roku prejdite do Settings > System > Advanced system settings > Control by mobile apps a nastavte Network access na „Default“ alebo „Permissive“ (pri novšom softvéri Roku nastavte „Control by mobile apps“ na „Enabled“).',
    ],
    encender='Na televízoroch Roku TV zapnite v Settings > System > Power možnosť „Fast TV start“. Prehrávače Roku pripojené k inému televízoru sa takto zapnúť nedajú. Potom sa vás aplikácia po klepnutí na vypnutý televízor v Mando TV opýta, či ho má zapnúť, a pripojí sa sama.',
    faq=[
      ('Funguje to s Roku Express alebo Streaming Stick?', 'Áno. Všetky prehrávače Roku a televízory Roku TV sa ovládajú rovnako.'),
      ('Mando TV nenájde moje Roku. Čo mám robiť?', 'Skontrolujte, či sú obe zariadenia v tej istej sieti Wi-Fi a či na Roku nie je vypnuté „Control by mobile apps“. Môžete ho pridať aj cez jeho IP adresu.'),
      ('Potrebujem účet Roku?', 'Nie. Mando TV sa pripája priamo cez vašu sieť Wi-Fi.'),
    ],
    guias=[('roku-403', 'Aplikácia Roku nefunguje (chyba 403)'),
           ('roku-lost', 'Stratený ovládač Roku: použite mobil'),
           ('tcl', 'Aplikácia ovládač TCL'),
           ('hisense', 'Aplikácia ovládač Hisense'),
           ('philips', 'Aplikácia ovládač Philips'),
           ('guias', 'Všetky návody na ovládanie televízora mobilom')]),
  dict(clave='android', color='#2fbf8f', corto='Android TV a Google TV',
    titulo='Ovládač Google TV a Android TV v mobile | Mando TV',
    desc='Diaľkový ovládač Google TV a Android TV (Sony, TCL, Xiaomi) v mobile cez Wi-Fi. Tlačidlá, klávesnica, aplikácie a zapnutie zadarmo; touchpad s Pro.',
    h1='Ovládač Google TV a Android TV ako aplikácia v mobile',
    intro='Mando TV je aplikácia ovládač pre Android TV: cez domácu sieť Wi-Fi z mobilu alebo počítača urobí diaľkový ovládač vášho televízora s Android TV alebo Google TV. Funguje aj z iPhonu a z Windowsu.',
    compat='Televízory s Google TV alebo Android TV od značiek Sony, Philips, TCL, Hisense, Sharp, Xiaomi, Toshiba, Panasonic, Haier, Skyworth, JVC, Thomson, Motorola, OnePlus, iFFALCON, Kogan, Vu a ďalších, a tiež Chromecast s Google TV, Google TV Streamer, onn. a Nvidia Shield. Niektoré z týchto značiek predávajú aj modely s iným systémom: ak váš televízor zobrazuje domovskú obrazovku Google TV alebo má obchod Google Play, Mando TV ho ovláda.',
    h2=dict(funciones='Čo môžete robiť s Android TV', como='Ako pripojiť Android TV k Mando TV',
            encender='Zapnutie Android TV mobilom', preguntas='Otázky o Android TV', guias='Návody pre Android TV'),
    funciones=[
      ('Všetky tlačidlá', 'Smerové tlačidlá, OK, späť, domov, hlasitosť, stlmenie a prehrávanie.'),
      ('Touchpad (Pro)', 'Prejdením prsta rýchlo prechádzajte ponukami Google TV.'),
      ('Klávesnica', 'Vyhľadávané výrazy a heslá píšte na klávesnici mobilu.'),
      ('Aplikácie', 'YouTube, Netflix, Disney+ a ďalšie aplikácie otvoríte jedným klepnutím.'),
      ('Zapnutie televízora', 'Na modeloch so zapnutím cez sieť Mando TV televízor zapne a pripojí sa samo.'),
      ('iPhone, Android a PC', 'Funguje rovnako na každom mobile aj počítači.'),
    ],
    pasos=[
      'Pripojte mobil a televízor k tej istej sieti Wi-Fi.',
      'Otvorte Mando TV: váš Android TV sa v zozname zobrazí sám. Klepnite naň.',
      'Televízor zobrazí 6-znakový kód. Zadajte ho v Mando TV (len pri prvom pripojení).',
    ],
    encender='Závisí od výrobcu. V nastaveniach siete alebo napájania hľadajte „Wake on LAN“, „Network standby“, „Wake on network“ alebo „Remote start“. Niektoré modely túto možnosť nemajú. Potom sa vás aplikácia po klepnutí na vypnutý televízor v Mando TV opýta, či ho má zapnúť, a pripojí sa sama.',
    faq=[
      ('Funguje to s Chromecastom s Google TV?', 'Áno, párovanie prebieha cez 6-znakový kód, ktorý sa zobrazí na obrazovke.'),
      ('Čím sa líši od aplikácie Google TV?', 'Mando TV nepotrebuje účet Google, funguje aj vo Windowse a jednou aplikáciou ovláda aj televízory LG, Samsung a Roku.'),
      ('Kód sa na obrazovke nezobrazuje. Čo mám robiť?', 'Zatvorte Mando TV, znova otvorte aplikáciu a ešte raz klepnite na televízor. Skontrolujte, či televízor nie je v hlbokom úspornom režime.'),
    ],
    guias=[('androidtv-code', 'Android TV žiada párovací kód: čo robiť'),
           ('androidtv', 'Android TV bez ovládača: použite mobil'),
           ('googletv-alt', 'Alternatíva k ovládaču Google TV v mobile'),
           ('sony', 'Aplikácia ovládač Sony'),
           ('tcl', 'Aplikácia ovládač TCL'),
           ('hisense', 'Aplikácia ovládač Hisense'),
           ('philips', 'Aplikácia ovládač Philips'),
           ('guias', 'Všetky návody na ovládanie televízora mobilom')]),
]

GUIAS = [
  dict(clave='lost-tv', corto='Stratený ovládač',
    titulo='Stratený ovládač? Ovládajte televízor mobilom',
    desc='Stratili ste ovládač? Zapnite televízor tlačidlom na ňom a použite mobil ako ovládač. Postup pre LG, Samsung, Roku, Android TV. Zadarmo.',
    h1='Stratený ovládač? Toto môžete urobiť hneď',
    intro='Stratený ovládač sa stane v každej domácnosti: zmizne presne vtedy, keď si chcete niečo pozrieť. Dobrá správa: váš mobil ho môže cez domácu sieť Wi-Fi nahradiť. Tu je postup, ako na to, krok za krokom.',
    pasos=[
      'Zapnite televízor tlačidlom na ňom. Býva takmer vždy dole uprostred alebo vzadu pri rohu. Niekedy je to jedno tlačidlo, niekedy malý joystick.',
      'Pripojte mobil k tej istej sieti Wi-Fi ako televízor.',
      'Stiahnite si Mando TV, ktoré je zadarmo a nevyžaduje účet, a otvorte aplikáciu. Váš televízor sa v zozname zobrazí sám. Klepnite naň.',
      'Potvrďte pripojenie podľa svojej značky. Pri LG a Samsung televízor zobrazí výzvu: potvrďte ju tlačidlom alebo joystickom na samotnom televízore. Pri Android TV a Google TV zadáte 6-znakový kód, ktorý sa zobrazí na obrazovke. Roku sa na nič nepýta.',
      'Hotovo. Smerové tlačidlá, OK, späť, domov, hlasitosť, kanály a klávesnica sú zadarmo.',
      'Nabudúce: v nastaveniach televízora zapnite zapnutie cez sieť (návod pre svoju značku nájdete nižšie). Potom budete môcť televízor zapnúť z mobilu bez toho, aby ste sa ho dotkli.',
    ],
    extra=[
      ('Vyberte si návod pre svoju značku', 'LG: [Stratený ovládač LG](@lost-lg). Android TV a Google TV: [Android TV bez ovládača](@androidtv). Samsung: [Samsung TV bez ovládača](@samsung-lost). Roku: [Stratený ovládač Roku](@roku-lost).'),
      ('Ak sa televízor tlačidlom nezapne', 'Skôr než začnete hľadať iný ovládač, skontrolujte, či je kábel pevne zapojený a v zásuvke je napätie. Ak tlačidlo na televízore nič nerobí, problém je v televízore, nie v ovládači.'),
      ('Ak ovládač jednoducho prestal fungovať', 'Vyskúšajte nové batérie. Či ešte vysiela signál, zistíte tak, že ho namierite na kameru mobilu a stlačíte tlačidlo: na mnohých mobiloch uvidíte na obrazovke fialové svetlo. Ak svetlo vidíte a televízor nereaguje, možno je zakrytý snímač na televízore.'),
      ('Ak ste zmenili router a televízor nemá Wi-Fi', 'Bez ovládača je ťažšie pripojiť televízor k novej sieti. Najjednoduchšie je zapojiť televízor sieťovým káblom do routera. Môžete tiež nastaviť sieť Wi-Fi s rovnakým názvom a heslom ako predtým: televízor sa k nej zvyčajne pripojí sám.'),
      ('Čo je zadarmo a čo Pro', 'Zapnutie a vypnutie televízora, smerové tlačidlá, OK, hlasitosť, kanály, číselné tlačidlá, klávesnica, otváranie aplikácií a prepínanie vstupu sú zadarmo. Touchpad, hlas a rutiny patria do Mando TV Pro, čo je jednorazový nákup bez predplatného.'),
    ],
    marca=None,
    faq=[
      ('Môžem televízor zapnúť mobilom, ak som ho ešte nikdy nepripojil?', 'Prvýkrát ho zapnite tlačidlom na televízore. Keď pripojíte mobil a v nastaveniach televízora zapnete zapnutie cez sieť, môžete ho zapínať cez aplikáciu.'),
      ('Musím si kúpiť nový ovládač?', 'Nie nevyhnutne. S Mando TV máte tlačidlá, hlasitosť, klávesnicu aj zapnutie zadarmo. Ak chcete radšej skutočný ovládač, hľadajte ho podľa presného modelu televízora.'),
      ('Funguje to, ak televízor nemá Wi-Fi?', 'Väčšinou nie. Mobil a televízor musia byť zvyčajne v tej istej sieti Wi-Fi. Výnimkou je infračervený signál na mobiloch s Androidom s infračerveným vysielačom, ktorý ovláda aj televízory bez funkcií Smart TV, a Bluetooth v beta verzii od Androidu 9, ktorý funguje celkom bez Wi-Fi s Google TV, Android TV a Fire TV.'),
    ]),
  dict(clave='lost-lg', corto='Stratený ovládač LG',
    titulo='Stratený ovládač LG? Použite mobil',
    desc='Nemáte ovládač LG? Zapnite televízor tlačidlom na ňom, potvrďte výzvu a použite mobil cez Wi-Fi. Bez účtu LG, bez reklám.',
    h1='Stratený ovládač LG? Takto použijete mobil',
    intro='Ak ste stratili ovládač LG alebo Magic Remote prestal fungovať, mobil ho cez Wi-Fi nahradí. Funguje to s televízormi LG so systémom webOS, teda takmer s každým televízorom LG Smart TV od roku 2014. Nepotrebujete účet LG ani aplikáciu ThinQ.',
    pasos=[
      'Zapnite televízor tlačidlom dole pod logom LG alebo tlačidlom vzadu. Na mnohých modeloch je to joystick: stlačením otvoríte ponuku a pohybom vyberiete položku.',
      'Pripojte mobil k tej istej sieti Wi-Fi ako televízor.',
      'Otvorte Mando TV a v zozname klepnite na svoj televízor LG.',
      'Televízor zobrazí výzvu so žiadosťou o povolenie. Potvrďte ju joystickom alebo tlačidlom na televízore. Ak ste tento mobil už raz pripojili, výzva sa už nezobrazí.',
      'Hotovo. Smerové tlačidlá, OK, späť, domov, hlasitosť, kanály a klávesnica sú zadarmo. Kurzor je funkcia Pro.',
      'Keď je aplikácia pripojená, smerovými tlačidlami a OK otvorte nastavenia a zapnite „Turn on TV with Mobile“. Návod [Zapnutie televízora LG mobilom](@lg-on) ukazuje, kde túto možnosť nájdete.',
    ],
    extra=[
      ('Ak televízor výzvu nezobrazí', 'Možno je povolenie už uložené alebo je mobil v inej sieti. Skontrolujte, či sú obe zariadenia v tej istej sieti Wi-Fi a či je vypnutá VPN. Ak sa televízor v zozname nezobrazuje, pomôže vám návod [Mobil nenájde televízor](@not-found).'),
      ('Ak televízor stratil Wi-Fi', 'Zapojte televízor sieťovým káblom do routera, použije ho sám. Alebo nastavte sieť Wi-Fi s rovnakým názvom a heslom ako predtým, lebo sa k nej televízor zvyčajne pripojí sám.'),
      ('Ak je televízor na inom vstupe', 'V mobile klepnite na Vstupy a vyberte port HDMI. Viac nájdete v návode [Zmena vstupu HDMI na televízore bez ovládača](@hdmi).'),
    ],
    marca='lg',
    faq=[
      ('Potrebujem na používanie Mando TV ovládač Magic Remote?', 'Treba vám len niečo na potvrdenie výzvy pri prvom pripojení, a na to stačí tlačidlo alebo joystick na samotnom televízore. Potom používate už len mobil.'),
      ('Potrebujem aplikáciu LG ThinQ?', 'Nie. Mando TV sa pripája priamo cez vašu sieť Wi-Fi a nevyžaduje účet LG.'),
      ('Môžem televízor LG vypnúť aj zapnúť mobilom?', 'Vypnúť áno. Na zapnutie musíte mať na televízore zapnuté „Turn on TV with Mobile“ a raz sa pripojiť, keď bol televízor zapnutý.'),
    ]),
  dict(clave='hdmi', corto='Zmena HDMI bez ovládača',
    titulo='Zmena vstupu HDMI bez ovládača (Samsung, LG, Roku)',
    desc='Zmeňte vstup HDMI bez ovládača na Samsung, LG alebo Roku: tlačidlom na televízore alebo mobilom. Na začiatok zadarmo, bez reklám.',
    h1='Ako zmeniť vstup HDMI na televízore bez ovládača',
    intro='Konzola alebo streamovacie zariadenie je pripravené, ale televízor je na inom vstupe a ovládač nie je nikde na dohľad. Vstup HDMI zmeníte bez ovládača dvoma spôsobmi: tlačidlom na samotnom televízore alebo mobilom. Tu je postup pre Samsung, LG a Roku.',
    pasos=[
      'Najprv skúste najjednoduchšie: zapnite konzolu alebo zariadenie. Ak je na televízore zapnuté HDMI-CEC (u Samsungu sa volá Anynet+, u LG SIMPLINK), televízor na tento vstup prepne sám.',
      'Ak neprepne, použite tlačidlo na samotnom televízore, dole uprostred alebo vzadu. Na mnohých televízoroch Samsung a LG je to joystick a otvorí ponuku so zdrojom alebo vstupmi.',
      'V tejto ponuke vyberte vstup: HDMI 1, HDMI 2 a tak ďalej. Číslo je port, do ktorého je zapojený kábel.',
      'Ak radšej použijete mobil, pripojte ho k tej istej sieti Wi-Fi, otvorte Mando TV a klepnite na svoj televízor.',
      'Na LG a Roku klepnite na Vstupy a vyberte port HDMI. Na Samsungu Vstupy odošle televízoru tlačidlo zdroja a vyberáte smerovými tlačidlami a OK.',
      'Ku vstupom sa dostanete aj smerovými tlačidlami a OK z domovskej obrazovky televízora. Podľa značky a roku výroby sa volajú Zdroj, Pripojené zariadenia alebo Vstupy. Na Roku TV sú to dlaždice HDMI na domovskej obrazovke.',
    ],
    extra=[
      ('Samsung', 'Ak ponuka tlačidla na televízore nemá položku Zdroj, otvorte mobilom ponuku domovskej obrazovky a vľavo hľadajte Zdroj alebo Pripojené zariadenia. Ovládate ju smerovými tlačidlami a OK v Mando TV, ktoré sú zadarmo.'),
      ('LG', 'Stlačte joystick na televízore a nájdite Vstupy. V Mando TV môžete mobilom otvoriť aj zoznam vstupov a klepnúť na ten, ktorý chcete.'),
      ('Roku TV', 'Na domovskej obrazovke je pre každý vstup dlaždica, napríklad HDMI 1 alebo HDMI 2. Pohybujte sa smerovými tlačidlami a otvorte ju tlačidlom OK, zadarmo.'),
      ('Ak ide o televízor s Android TV alebo Google TV', 'Zoznam vstupov pre Android TV zatiaľ v Mando TV nie je. Použite tlačidlo vstupu na samotnom televízore alebo sa k vstupom dostanete smerovými tlačidlami a OK z domovskej obrazovky. Ak nemáte ovládač a chcete sa pripojiť, prečítajte si [Android TV bez ovládača](@androidtv).'),
      ('Ďalšia pomoc', 'Ak sa televízor vôbec nezapne alebo neviete, kde začať, prečítajte si [Stratený ovládač](@lost-tv). Na hranie na konzole obsahuje návod [Zapnutie televízora a prepnutie na HDMI konzoly bez ovládača](@console) trik s HDMI-CEC.'),
    ],
    marca=None,
    faq=[
      ('Je zmena vstupu HDMI zadarmo?', 'Áno. Zoznam vstupov v Mando TV je zadarmo, rovnako ako zapnutie televízora a smerové tlačidlá, OK a hlasitosť. Ku vstupom sa dostanete aj cez ponuku televízora.'),
      ('Ako zistím, ktorý vstup HDMI potrebujem?', 'Pozrite sa na porty HDMI na televízore: každý má číslo. Vyberte ten, do ktorého je zapojený kábel konzoly alebo zariadenia.'),
      ('Čo ak sa televízor nezapne?', 'Zapnite ho tlačidlom na samotnom televízore. Ak ste ho už raz pripojili a zapli zapnutie cez sieť, môžete ho zapnúť aj mobilom.'),
    ]),
  dict(clave='androidtv', corto='Android TV bez ovládača',
    titulo='Android TV bez ovládača: použite mobil',
    desc='Nemáte ovládač Android TV alebo Google TV? Pripojte mobil 6-znakovým kódom z obrazovky. Zadarmo, bez účtu, bez reklám.',
    h1='Android TV bez ovládača: takto použijete mobil',
    intro='Ak ste stratili ovládač Android TV alebo Google TV alebo sa v ňom vybili batérie, mobil ho nahradí. Najlepšie je, že na pripojenie ovládač nepotrebujete: televízor zobrazí kód na obrazovke a vy ho napíšete v mobile. Funguje to s televízormi Sony, Philips, TCL, Hisense, Sharp a Xiaomi s Android TV, s Chromecastom s Google TV aj s Nvidia Shield.',
    pasos=[
      'Zapnite televízor tlačidlom na ňom. Býva takmer vždy dole uprostred alebo vzadu pri rohu.',
      'Pripojte mobil k tej istej sieti Wi-Fi ako televízor.',
      'Stiahnite si Mando TV, ktoré je zadarmo a nevyžaduje účet Google, a otvorte aplikáciu. V zozname klepnite na svoj televízor.',
      'Televízor zobrazí kód zložený zo 6 písmen a číslic. Napíšte ho v mobile a klepnite na Spárovať. Ovládač na to nepotrebujete.',
      'Teraz môžete používať smerové tlačidlá, OK, späť, domov, hlasitosť, stlmenie a klávesnicu. Sú zadarmo, rovnako ako zoznam aplikácií. Touchpad je Pro.',
      'Ak chcete televízor nabudúce zapnúť z mobilu, v nastaveniach siete alebo napájania hľadajte „Wake on LAN“, „Network standby“, „Wake on network“ alebo „Remote start“.',
    ],
    extra=[
      ('Ak sa televízor z mobilu zapnúť nedá', 'Nie každý Android TV sa dá zapnúť cez sieť; závisí to od výrobcu a modelu. Ak ho váš nemá, zapnite ho tlačidlom na televízore a pokračujte v mobile. Vypnúť ho môžete cez aplikáciu.'),
      ('Chromecast s Google TV, Google TV Streamer a Shield', 'Pripájajú sa rovnako: rovnaká sieť Wi-Fi, klepnutie na zariadenie v zozname a zadanie kódu. Ak televízor zobrazuje iný vstup, prepnite ho na port HDMI, do ktorého je zariadenie zapojené, ako je vysvetlené v návode [Zmena vstupu HDMI na televízore bez ovládača](@hdmi).'),
      ('Ak sa kód nezobrazí alebo ho aplikácia označí za nesprávny', 'Skontrolujte, či je televízor naozaj zapnutý a nie v pohotovostnom režime. Kód sa pri každej žiadosti mení: funguje len ten posledný. Viac podrobností nájdete v návode [Android TV žiada párovací kód](@androidtv-code).'),
      ('Aplikácia Google alebo Mando TV', 'Google má vlastnú aplikáciu, ktorá vyžaduje účet Google. Mando TV účet nevyžaduje, funguje aj vo Windowse a jednou aplikáciou ovláda aj televízory LG, Samsung a Roku.'),
    ],
    marca='android',
    faq=[
      ('Potrebujem na spárovanie mobilu ovládač?', 'Nie. Kód sa zobrazí na obrazovke televízora a vy ho napíšete v mobile. Stačí televízor zapnúť, v prípade potreby tlačidlom na ňom.'),
      ('Funguje to s Hisense?', 'S televízormi Hisense s Android TV alebo Google TV áno. Televízory Hisense s iným systémom nie sú kompatibilné.'),
      ('Môžem písať na klávesnici mobilu?', 'Áno. Klávesnica je zadarmo a funguje na vyhľadávanie v YouTube, Netflixe aj v ostatných aplikáciách.'),
    ]),
  dict(clave='lg-on', corto='Zapnutie LG mobilom',
    titulo='Zapnutie televízora LG mobilom (návod)',
    desc='Zapnite televízor LG mobilom cez Wi-Fi: zapnite „Turn on TV with Mobile“ a použite Mando TV. Krok za krokom, zadarmo.',
    h1='Ako zapnúť televízor LG mobilom',
    intro='Televízor LG môžete zapnúť mobilom, ale najprv musíte na televízore zapnúť jedno nastavenie. Potom ho mobil zapne cez vašu sieť Wi-Fi, celkom bez ovládača. Zaberie to päť minút a robí sa to len raz.',
    pasos=[
      'Pripojte mobil a televízor LG k tej istej sieti Wi-Fi.',
      'Na televízore otvorte Nastavenia a nájdite „Turn on TV with Mobile“. Nájdete ho v Settings > General > Devices > External Devices (na starších modeloch Connection > Mobile Connection Management).',
      'Zapnite „Turn on via Wi-Fi“. Ak je televízor pripojený sieťovým káblom, zapnite namiesto toho možnosť pre kábel.',
      'Ak má televízor „Quick Start+“, zapnite aj ten.',
      'Pri zapnutom televízore otvorte v mobile Mando TV a v zozname klepnite na svoj televízor LG. Potvrďte výzvu, ktorá sa zobrazí na obrazovke. Takto sa aplikácia naučí televízor prebudiť.',
      'Vypnite televízor a vyskúšajte to: klepnite v Mando TV na televízor a aplikácia sa opýta, či ho má zapnúť.',
    ],
    extra=[
      ('Ak sa nezapne', 'Televízor musel byť v tej istej sieti Wi-Fi, keď sa vypol. Skontrolujte, či je nastavenie stále zapnuté a mobil je v tej istej sieti. Ak ste zmenili router, pripojte sa znova pri zapnutom televízore.'),
    ],
    marca='lg',
    faq=[
      ('Môžem televízor LG zapnúť mobilom, ak som ho nikdy nepripojil?', 'Nie. Najprv musíte na televízore zapnúť „Turn on TV with Mobile“ a raz sa pripojiť k Mando TV, keď je televízor zapnutý.'),
      ('Potrebujem aplikáciu LG ThinQ?', 'Nie. Mando TV sa pripája priamo cez vašu sieť Wi-Fi a nevyžaduje účet LG.'),
      ('Funguje to s mobilnými dátami?', 'Nie. Mobil a televízor musia byť v tej istej sieti Wi-Fi.'),
    ]),
  dict(clave='console', corto='Televízor a konzola bez ovládača',
    titulo='Bez ovládača? Zapnite televízor, prepnite HDMI',
    desc='Deň vydania hry a nemáte ovládač? Zapnite televízor a mobilom prepnite na vstup HDMI svojej PS5 alebo Xboxu. Zadarmo, bez reklám.',
    h1='Ako zapnúť televízor a bez ovládača prepnúť na vstup HDMI konzoly',
    intro='Deň vydania GTA VI, konzola je pripravená a ovládač sa stratil kdesi medzi vankúšmi na pohovke. Stáva sa to častejšie, než si myslíte. S Mando TV mobil zapne televízor a cez domácu sieť Wi-Fi ho prepne na vstup vašej PlayStation alebo Xboxu.',
    pasos=[
      'Pripojte mobil k tej istej sieti Wi-Fi ako televízor.',
      'Otvorte Mando TV a v zozname klepnite na svoj televízor (Samsung, LG, Roku alebo Android TV).',
      'Ak je televízor vypnutý, klepnite na Zapnúť. Funguje to, ak je na televízore zapnuté zapnutie cez sieť. Ak ste to nikdy nezapli, zapnite televízor tentoraz tlačidlom na ňom a nabudúce to nastavte.',
      'Zapnite konzolu. Ak je zapnuté HDMI-CEC (pozrite si bezplatný trik nižšie), televízor sa prepne na jej vstup sám.',
      'Ak neprepne, klepnite v Mando TV na Vstupy a vyberte port HDMI, do ktorého je konzola zapojená: HDMI 1, HDMI 2 a tak ďalej.',
      'Hlasitosť počas hrania upravujte veľkými tlačidlami v aplikácii.',
    ],
    extra=[
      ('Bezplatný trik: nech televízor prepne konzola', 'PS5 a Xbox dokážu televízor zapnúť a hneď pri štarte ho prepnúť na svoj vstup HDMI vďaka HDMI-CEC. Na PS5 to nájdete v Nastavenia > Systém > HDMI > Povoliť prepojenie zariadení HDMI. Na Xboxe otvorte Nastavenia > Všeobecné > Možnosti televízora a obrazovky a nájdite možnosť ovládania zariadení. Na televízore sa funkcia podľa značky volá inak: Anynet+ u Samsungu, SIMPLINK u LG a BRAVIA Sync alebo ovládanie HDMI u ďalších.'),
      ('Ak televízor zostane na inom obraze', 'Ak je konzola zapnutá, ale televízor ešte ukazuje anténu alebo aplikáciu, vstup neprepol. Klepnite v mobile na Vstupy a vyberte vstup HDMI konzoly. Alebo sa smerovými tlačidlami a OK dostaňte k vstupom televízora, prípadne použite tlačidlo na samotnom televízore, a vyberte port HDMI. Číslo je port, do ktorého ste zapojili kábel konzoly.'),
      ('Ak ide o Roku TV', 'Tlačidlo na televízore, zvyčajne dole uprostred alebo vzadu, ho zapne. Zvyšok už urobí mobil.'),
    ],
    marca=None,
    faq=[
      ('Má Mando TV niečo spoločné s GTA VI?', 'Nie. Mando TV nemá žiadne prepojenie so spoločnosťami Rockstar Games ani Take-Two. Aplikácia vám len pomáha nestrácať čas na hranie tým, že nemôžete nájsť ovládač.'),
      ('Je zmena vstupu HDMI zadarmo?', 'Áno. Zoznam vstupov v Mando TV je zadarmo, rovnako ako zapnutie televízora a smerové tlačidlá, OK a hlasitosť. Vstup môžete nechať prepínať aj konzolu sama cez HDMI-CEC.'),
      ('Funguje to s mojím televízorom?', 'Funguje s televízormi Samsung, LG, Roku a Android TV v tej istej sieti Wi-Fi. Ak je váš od inej značky, trik s HDMI-CEC vám môže pomôcť aj tak.'),
      ('Môžem to použiť na hranie GTA VI (GTA 6) na PS5 alebo Xboxe?', 'Mando TV nezasahuje ani do konzoly, ani do hry. Len zabezpečí, že televízor je zapnutý a beží na správnom vstupe HDMI, aby ste si mohli sadnúť a hrať.'),
    ]),
  dict(clave='samsung-lost', corto='Samsung TV bez ovládača',
    titulo='Stratený ovládač Samsung? Použite mobil',
    desc='Stratili ste alebo pokazili ovládač Samsung? Použite mobil cez Wi-Fi ako ovládač pre televízory Tizen. Jednoducho s Mando TV, zadarmo, bez reklám.',
    h1='Samsung TV bez pôvodného ovládača: takto použijete mobil',
    intro='Ak ste stratili ovládač Samsung alebo prestal fungovať, môžete mobil cez Wi-Fi používať ako ovládač. Funguje to s televízormi Samsung so systémom Tizen, rok výroby 2016 a novšie.',
    pasos=[
      'Zapnite televízor tlačidlom na ňom. Na väčšine modelov je dole alebo vzadu, niekedy ako malý joystick.',
      'Skontrolujte, či je televízor pripojený k vašej sieti Wi-Fi a mobil je v tej istej sieti.',
      'Otvorte Mando TV v mobile. Váš televízor Samsung sa v zozname zobrazí sám. Klepnite naň.',
      'Televízor vás požiada o potvrdenie pripojenia. Na väčšine modelov ho potvrdíte tlačidlami na televízore alebo joystickom vzadu.',
      'Hotovo, teraz môžete mobil používať ako ovládač. Tlačidlá, klávesnica a aplikácie sú zadarmo; touchpad je funkcia Pro.',
      'Ak chcete televízor nabudúce zapnúť z mobilu, prejdite do Nastavenia > General > Network > Expert Settings a zapnite „Power On with Mobile“.',
    ],
    extra=[
      ('Ak sa televízor na povolenie nepýta', 'Možno je povolenie už uložené alebo je televízor v inej sieti Wi-Fi. Zatvorte Mando TV a pri zapnutom televízore aplikáciu otvorte znova. Ak je televízor starší ako z roku 2016, používa iný systém, ktorý zatiaľ nie je podporovaný.'),
      ('Ak ste povolenie omylom odmietli', 'Na televízore prejdite do Settings > General > External Device Manager > Device Connection Manager a nastavte Mando TV ako povolené. Ak mobil televízor aj tak nenájde, prečítajte si [Mobil nenájde televízor](@not-found).'),
    ],
    marca='samsung',
    faq=[
      ('Ako potvrdím pripojenie, ak nemám ovládač?', 'Na väčšine modelov ho potvrdíte tlačidlami na televízore alebo joystickom vzadu. Ak váš model tlačidlá nemá, napíšte na hola@mandotv.app a pomôžeme vám.'),
      ('Vyžaduje Mando TV účet Samsung?', 'Nie. Pripojenie ide priamo cez vašu sieť Wi-Fi, bez účtu Samsung.'),
      ('Funguje to s mojím starším televízorom Samsung?', 'Funguje s televízormi Samsung so systémom Tizen, rok výroby 2016 a novšie.'),
    ]),
  dict(clave='wifi', corto='Mobil ako ovládač cez Wi-Fi',
    titulo='Mobil ako ovládač: ovládanie televízora cez Wi-Fi',
    desc='Pripojte mobil cez Wi-Fi k televízoru a používajte ho ako ovládač pre Samsung, LG, Roku a Google TV. Postup podľa značky s Mando TV. Zadarmo.',
    h1='Ako pripojiť mobil cez Wi-Fi k televízoru ako ovládač',
    intro='Potrebujete len mobil a televízor v tej istej sieti Wi-Fi a aplikáciu ovládač. Mando TV nájde váš televízor samo a funguje so Samsung, LG, Roku, Google TV a Android TV.',
    pasos=[
      'Pripojte mobil a televízor k tej istej sieti Wi-Fi.',
      'Otvorte Mando TV. Váš televízor sa v zozname zobrazí sám. Klepnite naň.',
      'Potvrďte pripojenie podľa svojej značky (podrobnosti sú nižšie).',
      'Televízor ovládajte tlačidlami alebo klávesnicou mobilu. Touchpad je funkcia Pro.',
    ],
    extra=[
      ('Samsung', 'Televízor sa opýta, či pripojenie povoliť. Potvrďte ho pri prvom pripojení na obrazovke. Funguje s Tizen, rok výroby 2016 a novšie. Ak ho chcete zapínať z mobilu, zapnite v Nastavenia > General > Network > Expert Settings možnosť „Power On with Mobile“.'),
      ('LG', 'Televízor zobrazí výzvu so žiadosťou o povolenie. Potvrďte ju pri prvom pripojení. Ak ho chcete zapínať z mobilu, v nastaveniach nájdite „Turn on TV with Mobile“ a zapnite „Turn on via Wi-Fi“.'),
      ('Roku', 'Roku nevyžaduje párovanie: klepnite naň v zozname a ste pripojení. Ak ho chcete zapínať, zapnite v Settings > System > Power možnosť „Fast TV start“.'),
      ('Google TV a Android TV', 'Televízor zobrazí kód na obrazovke. Pri prvom pripojení ho zadajte v Mando TV. Ak ho chcete zapínať, v nastaveniach hľadajte „Wake on LAN“, „Network standby“ alebo „Wake on network“.'),
    ],
    marca=None,
    faq=[
      ('Potrebujem na používanie mobilu ako ovládača internet?', 'Potrebujete mobil a televízor v tej istej sieti Wi-Fi. Mando TV sa cez túto sieť pripája priamo k vášmu televízoru.'),
      ('Prečo sa môj televízor v zozname nezobrazuje?', 'Skontrolujte, či je televízor zapnutý a mobil nepoužíva mobilné dáta ani inú sieť Wi-Fi. Niektoré routery majú hosťovskú sieť, ktorá zariadenia od seba izoluje.'),
      ('Môžem Mando TV používať na iPhone alebo v mobile s Androidom?', 'Na iPhone a iPad áno: aplikácia je už v App Store. Pre Windows je aj v Microsoft Store. Android prichádza čoskoro: môžete sa zapojiť do bezplatného predbežného prístupu v Google Play.'),
    ]),
  dict(clave='pc', corto='Ovládanie televízora z počítača',
    titulo='Ovládanie televízora z počítača s Windowsom (zadarmo)',
    desc='Použite počítač s Windowsom ako ovládač pre Samsung, LG, Roku alebo Google TV cez Wi-Fi. Tlačidlá, klávesnica a aplikácie zadarmo; klávesové skratky s Pro.',
    h1='Ako ovládať televízor počítačom s Windowsom',
    intro='Ak trávite deň pri počítači, nemusíte hľadať ovládač: Mando TV pre Windows ovláda váš televízor Samsung, LG, Roku, Google TV alebo Android TV cez domácu sieť Wi-Fi. Hodí sa na prepínanie aplikácií, zvýšenie hlasitosti alebo písanie v YouTube na klávesnici počítača.',
    pasos=[
      'Stiahnite si Mando TV zadarmo z Microsoft Store do počítača s Windowsom 10 alebo 11.',
      'Skontrolujte, či sú počítač a televízor v tej istej sieti (Wi-Fi alebo kábel, ale cez ten istý router).',
      'Otvorte Mando TV: váš televízor sa v zozname zobrazí sám. Klepnite alebo kliknite naň.',
      'Pri prvom pripojení potvrďte pripojenie na obrazovke televízora (pri Google TV a Android TV zadáte kód, ktorý televízor zobrazí).',
      'Hotovo: používajte tlačidlá alebo klávesnicu na písanie do vyhľadávacieho poľa televízora. Touchpad je funkcia Pro.',
    ],
    extra=[
      ('Klávesové skratky v počítači (Pro)', 'S Mando TV Pro ovládate televízor klávesnicou počítača: šípky na pohyb, Enter pre OK, Backspace alebo Esc pre späť, + a - pre hlasitosť, M pre stlmenie a medzerník pre pauzu.'),
      ('Mini ovládač vždy navrchu (Pro)', 'Nechajte malé okno s ovládačom stále viditeľné, kým pracujete alebo hráte na počítači.'),
      ('Rozprávanie s televízorom z počítača (Pro)', 'S Mando TV Pro dávate televízoru príkazy cez mikrofón počítača: „otvor YouTube“, „zvýš hlasitosť“ alebo „vypni o 30 minút“, tak, ako sa hovorí. Vo Windowse sa reč rozpoznáva priamo v počítači: nepotrebujete internet, nemusíte nič meniť v nastaveniach Windowsu a funguje v 6 jazykoch aplikácie. To, čo poviete, počítač neopustí a neukladá sa. Len pri veľmi starých procesoroch sa aplikácia vráti k diktovaniu Windowsu. Na to musí byť v nastaveniach súkromia zapnuté online rozpoznávanie reči a vo Windowse pridaná slovenčina (Slovensko). Ak niečo chýba, aplikácia vás upozorní a nastavenie otvorí tlačidlom.'),
    ],
    marca=None,
    faq=[
      ('Potrebujem na ovládanie televízora z počítača kábel alebo Bluetooth?', 'Nie. Mando TV sa pripája cez vašu domácu sieť: počítač a televízor musia byť len na tom istom routeri.'),
      ('Funguje to s každým televízorom?', 'Funguje s televízormi Samsung so systémom Tizen (rok výroby 2016 a novšie), LG s webOS, Roku a Google TV alebo Android TV (Sony, Philips, TCL, Hisense, Sharp, Xiaomi, Toshiba, Panasonic, Haier, Skyworth a ďalšie).'),
      ('Koľko to stojí?', 'Tlačidlá, klávesnica a zapnutie cez sieť sú zadarmo a bez reklám. Mando TV Pro je jednorazový nákup bez predplatného pre doplnky ako touchpad, klávesové skratky v počítači a mini ovládač.'),
      ('Prečo ma mikrofón vo Windowse nerozumie?', 'Skontrolujte, či je zapnutá hlasová funkcia (patrí do Pro) a či mikrofón počítača vo Windowse funguje. Na takmer všetkých počítačoch sa reč rozpoznáva priamo v zariadení, bez internetu. Len pri veľmi starých procesoroch aplikácia používa diktovanie Windowsu. Vtedy skontrolujte, či je v nastaveniach súkromia Windowsu zapnuté online rozpoznávanie reči a či má Windows v jazykových nastaveniach slovenčinu (Slovensko). Mando TV tento jazyk používa, len kým počúva.'),
    ]),
  dict(clave='roku-403', corto='Aplikácia Roku nefunguje',
    titulo='Aplikácia Roku nefunguje? Oprava chyby 403',
    desc='Mobil je pripojený, ale Roku nereaguje? Zapnite „Control by mobile apps“ v 5 krokoch a použite mobil znova ako ovládač.',
    h1='Aplikácia Roku nefunguje: ako to opraviť',
    intro='Ak váš mobil Roku nájde a pripojí sa, ale žiadne tlačidlo nič nerobí, problém je takmer vždy v nastavení na samotnom Roku, ktoré blokuje aplikácie ovládača. Novšie verzie Roku sú v predvolenom nastavení prísnejšie. V ponuke Roku to opravíte za minútu.',
    pasos=[
      'Na Roku stlačte Home a prejdite do Settings.',
      'Otvorte System a potom Advanced system settings.',
      'Prejdite na „Control by mobile apps“. Na niektorých modeloch sa volá „External control“.',
      'V časti „Network access“ vyberte „Default“ alebo „Permissive“. Ak je to na vašom modeli len prepínač, nechajte ho na „Enabled“.',
      'Vráťte sa do Mando TV v mobile a klepnite na svoje Roku. Tlačidlá teraz reagujú.',
    ],
    extra=[
      ('Ako spoznáte, že ide o váš problém', 'Znak je jasný: mobil vidí Roku v zozname a pripojí sa, ale po klepnutí na tlačidlo sa nič nestane. Roku interne odpovedá chybou 403, čo znamená „zakázané“. Mando TV to pri pripájaní rozpozná a zobrazí presne tieto kroky na obrazovke.'),
      ('Default alebo Permissive, čo vybrať?', 'Stačí Default: prijíma príkazy z vašej domácej siete, čo ovládač potrebuje. Permissive je otvorenejší a potrebujete ho len v nezvyčajných sieťach.'),
      ('Ak nemáte ovládač Roku', 'Ak je nastavenie na Disabled, dá sa zmeniť len pôvodným ovládačom Roku. Požičajte si nejaký, zmeňte ho raz; potom už všetko urobíte mobilom. Prečítajte si aj [Stratený ovládač Roku](@roku-lost).'),
    ],
    marca='roku',
    faq=[
      ('Prečo moje Roku prestalo reagovať, hoci predtým fungovalo?', 'Aktualizácia Roku môže toto nastavenie sprísniť. Nie je to vina vášho mobilu ani Wi-Fi: stačí znova povoliť ovládanie aplikáciami.'),
      ('Platí to pre Roku TV aj pre prehrávače Roku?', 'Áno. Nastavenie je pri prehrávačoch Roku aj pri televízoroch Roku TV v tej istej ponuke.'),
      ('Je bezpečné nechať nastavenie na Default?', 'Áno. Prijíma len príkazy zo zariadení vo vašej domácej sieti.'),
    ]),
  dict(clave='not-found', corto='Mobil nenájde televízor',
    titulo='Mobil nenájde televízor? 6 vecí na kontrolu',
    desc='Aplikácia ovládač nenájde váš televízor? Skontrolujte Wi-Fi, VPN a prístup k lokálnej sieti. Pre Samsung, LG, Roku a Android TV.',
    h1='Mobil nenájde televízor: čo skontrolovať',
    intro='Otvoríte aplikáciu ovládač a zoznam je prázdny, alebo sa televízor zobrazí, ale spojenie sa preruší. Takmer vždy je príčina v sieti, nie v televízore. Prejdite tieto body postupne: prvý vyrieši väčšinu prípadov.',
    pasos=[
      'Pozrite sa, v ktorej sieti Wi-Fi je mobil a v ktorej televízor. Musí to byť tá istá sieť s rovnakým názvom. Hosťovská sieť nefunguje, pretože zariadenia od seba izoluje.',
      'Ak používate VPN, vypnite ju. Pri zapnutej VPN ide mobil na internet cez inú sieť a nevidí zariadenia u vás doma, alebo sa spojenie po pár sekundách preruší.',
      'Na chvíľu vypnite mobilné dáta. Niektoré mobily pri slabom signáli prepnú zo siete Wi-Fi na mobilné dáta sami.',
      'Zapnite televízor a počkajte, kým sa úplne spustí. Vypnutý televízor na vyhľadávanie neodpovedá.',
      'Na iPhone skontrolujte, či má aplikácia povolenie „Lokálna sieť“: Nastavenia > Súkromie a zabezpečenie > Lokálna sieť.',
      'Ak sa stále nezobrazuje, pridajte ho ručne: v Mando TV klepnite na „Pridať cez IP adresu“ a zadajte IP adresu televízora.',
    ],
    extra=[
      ('Nechajte sa viesť aplikáciou', 'V zozname televízorov je tlačidlo pre prípad, že sa váš televízor nezobrazí. Aplikácia po krokoch skontroluje najčastejšie príčiny (rovnaká sieť Wi-Fi, VPN, povolenie lokálnej siete a ďalšie) a po každej oprave zobrazí tlačidlo na opätovnú kontrolu. Asistent je zadarmo.'),
      ('Kde nájdete IP adresu televízora', 'Je v sieťovej ponuke televízora a podľa modelu sa mierne líši. Na LG: Nastavenia, Sieť, Pripojenie Wi-Fi, Rozšírené nastavenia Wi-Fi. Na Samsungu: Nastavenia, General, Network, Network Status, IP Settings. Na Roku: Settings, Network, About. Na Android TV a Google TV: Nastavenia, Sieť a internet, potom klepnite na svoju sieť. Je to číslo ako 192.168.1.86.'),
      ('Ak sa zobrazí, ale spojenie sa preruší', 'Ak sa spojenie preruší po niekoľkých sekundách, príčina je zvyčajne v mobile: VPN, prepnutie do inej siete Wi-Fi alebo úsporný režim. Vypnite VPN, zostaňte v tej istej sieti Wi-Fi a skúste to znova.'),
      ('Wi-Fi s 2,4 a 5 GHz', 'Nezáleží na tom, či je mobil v sieti 5 GHz a televízor v sieti 2,4 GHz, pokiaľ obe pochádzajú z toho istého routera. Ak máte opakovač Wi-Fi a televízor sa aj tak nezobrazuje, priblížte sa s mobilom k hlavnému routeru a skúste to znova.'),
    ],
    marca=None,
    faq=[
      ('Môžem televízor ovládať cez mobilné dáta?', 'Nie. Signál ovládača ide cez vašu domácu sieť Wi-Fi, preto musia byť mobil a televízor v tej istej sieti.'),
      ('Prečo to nefunguje so zapnutou VPN?', 'Pretože VPN smeruje všetku prevádzku mobilu cez inú sieť a mobil prestane vidieť zariadenia u vás doma. Kým ovládač používate, vypnite ju.'),
      ('Funguje to cez Bluetooth alebo infračervený signál?', 'Pri televízoroch Smart TV používa Mando TV Wi-Fi. Infračervený signál funguje len v mobiloch s Androidom, ktoré majú infračervený vysielač, a je určený pre televízory, ktoré nie sú Smart TV. Bluetooth je v beta verzii, zadarmo a len od Androidu 9: mobil sa k televízoru pripojí ako klávesnica a ovládač cez Bluetooth, celkom bez Wi-Fi. Funguje s Google TV, Android TV a Fire TV; pri iných značkách, ktoré akceptujú klávesnice Bluetooth, môže fungovať, Roku ich neakceptuje.'),
    ]),
  dict(clave='androidtv-code', corto='Párovací kód Android TV',
    titulo='Android TV žiada párovací kód: čo robiť',
    desc='Váš Android TV alebo Google TV zobrazí pri pripájaní 6-znakový kód. Ako ho zadať a čo robiť, ak sa nezobrazí alebo je nesprávny.',
    h1='Android TV žiada párovací kód: čo robiť',
    intro='Keď mobil prvýkrát pripájate k Android TV alebo Google TV, televízor zobrazí na obrazovke 6-znakový kód. Je to normálne a stane sa to len raz: takto je zaručené, že váš televízor nemôže ovládať nikto iný. Tu zistíte, ako ho zadať a čo robiť, ak sa nezobrazí.',
    pasos=[
      'Zapnite televízor a nechajte zobrazenú domovskú obrazovku.',
      'Otvorte Mando TV v mobile, v tej istej sieti Wi-Fi ako televízor, a v zozname klepnite na svoj televízor.',
      'Pozrite sa na obrazovku televízora: zobrazí sa kód zložený zo 6 písmen a číslic.',
      'Napíšte ho v mobile presne tak, ako sa zobrazuje, a klepnite na Spárovať. Písmená idú len od A po F, takže okrúhly znak je vždy číslica nula.',
      'Hotovo. Televízor si váš mobil zapamätá a na kód sa už nepýta.',
    ],
    extra=[
      ('Ak sa kód na televízore nezobrazí', 'Skontrolujte, či je televízor naozaj zapnutý a nie v pohotovostnom režime a či je mobil v tej istej sieti Wi-Fi. V mobile znova klepnite na televízor. Ak sa stále nezobrazí, televízor reštartujte: na desať sekúnd odpojte kábel zo zásuvky, znova ho zapojte a skúste to znova.'),
      ('Ak aplikácia hlási, že kód je nesprávny', 'Kód sa pri každej žiadosti mení. Ak vám to trvalo dlho alebo ste si ho vyžiadali dvakrát, funguje len ten, ktorý je práve na obrazovke. V mobile znova klepnite na televízor a zadajte nový kód.'),
      ('Ak sa televízor na kód pýta znova', 'Stáva sa to, ak bol televízor obnovený na továrenské nastavenia alebo ste v mobile vymazali dáta aplikácie. Spárujte znova a bude uložený. Ak nemáte vôbec žiadny ovládač, prečítajte si [Android TV bez ovládača](@androidtv).'),
    ],
    marca='android',
    faq=[
      ('Ktoré televízory používajú tento kód?', 'Tie s Android TV alebo Google TV: Sony, Philips, TCL, Hisense, Sharp, Xiaomi, Chromecast s Google TV a niektoré ďalšie.'),
      ('Potrebujem v mobile účet Google?', 'Nie. Kód na obrazovke je všetko, čo potrebujete.'),
      ('Je to bezpečné?', 'Áno. Kód dokazuje, že sedíte pred televízorom: nikto sa nemôže spárovať bez toho, aby videl kód na obrazovke.'),
    ]),
  dict(clave='roku-lost', corto='Stratený ovládač Roku',
    titulo='Stratený ovládač Roku? Použite mobil cez Wi-Fi',
    desc='Stratili ste ovládač Roku? Mobil ho nahradí cez Wi-Fi. Jednoduchý postup, aj keď ste zmenili router a Roku nemá Wi-Fi.',
    h1='Stratený ovládač Roku: takto použijete mobil',
    intro='Ak ste stratili ovládač Roku alebo prestal fungovať, mobil ho nahradí, kým je Roku stále pripojené k vašej sieti Wi-Fi. A ak ste zmenili sieť Wi-Fi alebo router, existuje aj na to východisko.',
    pasos=[
      'Najprv skúste ovládač rozozvučať. Ak má váš ovládač Roku reproduktor, napríklad Roku Voice Remote Pro, otvorte Mando TV, pripojte sa k Roku a použite možnosť zvonenia ovládača, aby ste ho našli. Funguje to len s ovládačmi Roku s reproduktorom a Roku musí byť zapnuté.',
      'Zapnite televízor a nechajte Roku zapojené. Nemusíte sa ho dotýkať.',
      'Pripojte mobil k tej istej sieti Wi-Fi, ktorú používa Roku.',
      'Otvorte Mando TV. Roku sa v zozname zobrazí samo. Klepnite naň.',
      'Používajte smerové tlačidlá, OK, domov a späť ako na bežnom ovládači. Roku nežiada kód.',
      'Ak tlačidlá nič nerobia, Roku blokuje ovládanie aplikáciami: návod [Aplikácia Roku nefunguje](@roku-403) vysvetľuje, ako ho povoliť.',
    ],
    extra=[
      ('Ak Roku nemá Wi-Fi (zmenili ste router alebo ste sa presťahovali)', 'Bez ovládača sa nedostanete do ponuky, aby ste nastavili novú sieť, ale existuje trik: Roku sa pripojí samo k sieti s rovnakým názvom a heslom ako stará. Na inom mobile vytvorte hotspot Wi-Fi presne s týmto názvom a heslom, pripojte k nemu mobil s Mando TV a Roku sa zobrazí v zozname. Odtiaľ prejdite do Settings, Network a pripojte ho k novej sieti Wi-Fi.'),
      ('Ak ide o Roku TV', 'Televízory Roku TV majú tlačidlo na samotnom zariadení, takmer vždy dole uprostred alebo vzadu, ktoré televízor zapne. Stačí to na zapnutie a pokračovať môžete mobilom.'),
      ('Ak si radšej kúpite iný ovládač', 'Dávajte pozor, aby pasoval na váš model. Malé prehrávače Roku za televízorom potrebujú ovládač bez infračerveného signálu, pretože infračervený signál k nim nedosiahne.'),
    ],
    marca='roku',
    faq=[
      ('Môže mobil Roku zapnúť?', 'Zapojený prehrávač Roku je stále zapnutý. Roku TV Mando TV zapne cez Wi-Fi, ak je v Settings > System > Power zapnuté „Fast TV start“.'),
      ('A hlasitosť?', 'Na Roku TV mobil hlasitosť zvyšuje aj znižuje. Pri prehrávači Roku pripojenom cez HDMI to závisí od televízora: na mnohých to funguje, na iných nie.'),
      ('Musím si vytvoriť účet?', 'Nie. Mando TV účet nevyžaduje a jednou aplikáciou ovláda aj televízory Samsung, LG a Android TV.'),
    ]),
]

SOPORTE = dict(
  titulo='Pomoc: pripojenie a zapnutie televízora cez Mando TV',
  desc='Ako pripojiť ovládač Mando TV k LG, Samsung, Roku alebo Android TV, zapnúť televízor z mobilu a vyriešiť problémy.',
  h1='Pomoc',
  intro='Najčastejšie otázky v poradí podľa krokov. Ak svoju nenájdete, napíšte nám na <a href="mailto:hola@mandotv.app?subject=Pomoc%20s%20Mando%20TV">hola@mandotv.app</a> a odpovieme.',
)
SOPORTE_HTML = '''      <h2 id="encontrar">Nájdenie televízora</h2>
      <div class="preguntas">
        <details open><summary>Môj televízor sa v zozname nezobrazuje</summary>
          <ol>
            <li>Skontrolujte, či sú mobil a televízor v tej istej sieti Wi-Fi. Ak má váš router sieť 2,4 GHz a 5 GHz s rôznymi názvami, niekedy sa navzájom nevidia.</li>
            <li>Uistite sa, že je televízor zapnutý.</li>
            <li>Na iPhone skontrolujte, či má Mando TV povolenie „Lokálna sieť“, v Nastaveniach, Mando TV.</li>
            <li>V zozname televízorov klepnite na tlačidlo pre prípad, že sa váš televízor nezobrazí: aplikácia po krokoch skontroluje najčastejšie príčiny (rovnaká sieť Wi-Fi, VPN, povolenie lokálnej siete a ďalšie) a po každej oprave zobrazí tlačidlo na opätovnú kontrolu.</li>
            <li>Ak sa stále nezobrazuje, klepnite na tlačidlo +, vyberte značku a zadajte IP adresu televízora. Nájdete ju v sieťovej ponuke televízora (napríklad 192.168.1.50).</li>
          </ol>
        </details>
        <details><summary>Funguje to s mobilnými dátami alebo z cesty?</summary>
          <p>Nie. Mando TV komunikuje s televízorom vo vašej domácej sieti, preto musí byť mobil pripojený k tejto sieti Wi-Fi.</p>
        </details>
      </div>

      <h2 id="conectar">Prvé pripojenie</h2>
      <p>Úplné návody podľa značky: <a href="@@R_lg@@">LG</a>, <a href="@@R_samsung@@">Samsung</a>, <a href="@@R_roku@@">Roku</a> a <a href="@@R_android@@">Android TV</a>.</p>
      <div class="preguntas">
        <details><summary>LG</summary>
          <p>Keď klepnete na televízor, na obrazovke sa zobrazí výzva so žiadosťou o povolenie. Potvrďte ju svojím bežným ovládačom. Urobíte to len raz.</p>
        </details>
        <details><summary>Samsung</summary>
          <p>Televízor sa opýta, či povolíte pripojenie Mando TV. Ovládačom vyberte „Allow“. Ak ste ho omylom odmietli, prejdite do Settings > General > External Device Manager > Device Connection Manager a zmeňte to na povolené.</p>
        </details>
        <details><summary>Roku</summary>
          <p>Roku sa na povolenie nepýta. Ak pripojenie nefunguje, na Roku prejdite do Settings > System > Advanced system settings > Control by mobile apps a nechajte Network access na „Default“ alebo „Permissive“ (pri novšom softvéri Roku nastavte „Control by mobile apps“ na „Enabled“).</p>
        </details>
        <details><summary>Android TV a Google TV</summary>
          <p>Televízor zobrazí 6-znakový kód. Zadajte ho v Mando TV presne tak, ako sa zobrazí. Funguje to so Sony, Philips, TCL, Hisense, Sharp, Xiaomi, Chromecastom s Google TV a ďalšími s Android TV.</p>
        </details>
      </div>

      <h2 id="encender">Zapnutie televízora cez aplikáciu</h2>
      <p>Mando TV zapína televízor cez vašu domácu sieť. Treba na to dve veci: aspoň raz ste sa pripojili pri zapnutom televízore a na televízore je zapnuté zapnutie cez sieť. Názov nastavenia sa líši podľa modelu; toto sú najčastejšie:</p>
      <div class="preguntas">
        <details><summary>LG</summary>
          <p>Hľadajte „Turn on TV with Mobile“ (alebo „Turn on via Wi-Fi“) v Settings > General > Devices > External Devices (na starších modeloch Connection > Mobile Connection Management) a zapnite ho.</p>
        </details>
        <details><summary>Samsung</summary>
          <p>Zapnite „Power On with Mobile“ v Nastavenia > General > Network > Expert Settings.</p>
        </details>
        <details><summary>Roku</summary>
          <p>Na televízoroch Roku TV zapnite „Fast TV start“ v Settings > System > Power. Prehrávače Roku pripojené k televízoru sa takto zapnúť nedajú.</p>
        </details>
        <details><summary>Android TV a Google TV</summary>
          <p>Závisí od výrobcu. V nastaveniach siete alebo napájania hľadajte „Wake on LAN“, „Network standby“, „Wake on network“ alebo „Remote start“. Niektoré modely túto možnosť nemajú.</p>
        </details>
      </div>

      <h2 id="falla">Ak niečo nefunguje</h2>
      <div class="preguntas">
        <details><summary>Spojenie sa preruší alebo nič nereaguje</summary>
          <ol>
            <li>Na obrazovke ovládača klepnite na Pripojiť znova.</li>
            <li>Ak to nepomôže, zatvorte Mando TV a znova otvorte aplikáciu.</li>
            <li>Ak televízor dostal inú IP adresu, odstráňte ho zo zoznamu a pridajte ho znova.</li>
          </ol>
        </details>
        <details><summary>Ako nám poslať hlásenie o chybe</summary>
          <ol>
            <li>V Mando TV klepnite na tlačidlo Personalizovať (posuvníky hore).</li>
            <li>Klepnite na Kopírovať skúšobné hlásenie.</li>
            <li>Vložte ho spolu so značkou a modelom televízora do e-mailu na hola@mandotv.app.</li>
          </ol>
          <p>Hlásenie neobsahuje heslá, kódy ani nič, čo píšete.</p>
        </details>
        <details><summary>Kúpil som Pro a nezobrazuje sa</summary>
          <p>V časti Personalizovať klepnite na Obnoviť nákup, s rovnakým účtom obchodu, s ktorým ste nákup uskutočnili. Ak sa stále nezobrazuje, napíšte nám.</p>
        </details>
      </div>

      <h2 id="guias">Návody krok za krokom</h2>
      <p><a href="@@R_guias@@">Zobraziť všetky návody</a></p>
      <ul>
@@GUIAS@@
      </ul>

      <h2 id="contacto">Máte ešte otázky?</h2>
      <p>Napíšte nám na <a href="mailto:hola@mandotv.app?subject=Pomoc%20s%20Mando%20TV">hola@mandotv.app</a>. Uveďte značku a model televízora a krok, pri ktorom ste sa zasekli. Píšte nám vo svojom jazyku. Odpovedáme po španielsky alebo anglicky a, ak chcete, aj vo vašom jazyku s pomocou prekladača.</p>
'''

PRIVACIDAD = dict(
  titulo='Zásady ochrany súkromia | Mando TV',
  desc='Mando TV nezbiera osobné údaje: žiadne účty, žiadne reklamy, žiadne sledovače. Aplikácia komunikuje len s vaším televízorom vo vašej sieti Wi-Fi.',
  h1='Ochrana súkromia',
  intro='Stručne: Mando TV nezbiera vaše údaje. Neexistujú účty, reklamy, sledovače ani vlastné servery, ktoré by ukladali, čo robíte.',
)
PRIVACIDAD_HTML = '''      <p class="fecha">Platné od 14. novembra 2026. Naposledy aktualizované 26. novembra 2026.</p>

      <h2>Kto sme</h2>
      <p>Mando TV je aplikácia na ovládanie televízora z mobilu alebo počítača. Tieto zásady opisujú, aké informácie aplikácia používa a čo s nimi robí. Ak máte otázky, napíšte nám na <a href="mailto:hola@mandotv.app">hola@mandotv.app</a>.</p>

      <h2>Aké údaje zbierame</h2>
      <p>Aplikácia: žiadne. Aplikácia nám ani tretím stranám neodosiela informácie o vás ani o tom, ako ju používate. Nepoužíva žiadne analytické, reklamné ani sledovacie nástroje.</p>
      <p>Táto webová stránka: návštevy meriame dvoma spôsobmi, ktoré sú vysvetlené v časti <a href="#cookies">Súbory cookie na tejto webovej stránke</a>.</p>

      <h2>Čo aplikácia ukladá vo vašom zariadení</h2>
      <p>Aby aplikácia fungovala, ukladá nasledujúce údaje len vo vašom mobile alebo počítači:</p>
      <ul>
        <li>Televízory, ktoré ste pridali: názov, značku, IP adresu vo vašej sieti a hardvérovú adresu sieťovej karty (MAC), ktorá sa používa na zapnutie.</li>
        <li>Kľúče pripojenia, ktoré každý televízor odovzdá po potvrdení povolenia. Ukladajú sa zašifrované v zabezpečenom úložisku systému (Kľúčenka v iPhone a Macu, Keystore v Androide, chránené úložisko vo Windowse).</li>
        <li>Vaše nastavenia: svetlý alebo tmavý vzhľad, farba pozadia, vibrácie a typ ovládača.</li>
        <li>Ak používate funkcie Pro: vaše obľúbené aplikácie, rutiny a posledné vyhľadávania v YouTube (môžete ich v aplikácii vymazať).</li>
      </ul>
      <p>Keď aplikáciu odstránite, všetko sa odstráni spolu s ňou.</p>

      <h2>S kým aplikácia komunikuje</h2>
      <p>S vašimi televízormi, vo vašej domácej sieti Wi-Fi. Aby ich našla, aplikácia prehľadáva vašu lokálnu sieť; preto sa na iPhone pýta na povolenie „Lokálna sieť“. Text, ktorý píšete na klávesnici aplikácie, ide priamo do televízora a neukladá sa.</p>
      <p>Okrem toho aplikácia pri otvorení stiahne z tejto webovej stránky malý verejný súbor (mandotv.app/app/config.json), aby zistila, či existuje nová verzia, ktorú by ste mali nainštalovať, a ktoré funkcie patria do Mando TV Pro. Je to sťahovanie ako pri otvorení stránky: aplikácia neodosiela vaše údaje, vaše televízory ani to, čo robíte. Uvádza len verziu aplikácie a systém (napríklad Android), aby vám mohla zobraziť vhodné upozornenie. Ak nemáte internet, aplikácia pracuje ďalej s naposledy stiahnutým súborom; ak uplynie viac ako 30 dní bez toho, aby sa ho podarilo stiahnuť, aplikácia vás požiada, aby ste sa nakrátko pripojili k internetu.</p>

      <p>Keď do televízora posielate fotografie alebo videá (funkcia Pro), televízor sťahuje iba súbory, ktoré vyberiete, priamo z vášho mobilu alebo počítača cez vašu domácu sieť Wi-Fi. Nejdú cez internet ani cez nás, aplikácia nevidí vaše ostatné fotografie a zdieľanie sa skončí, len čo túto obrazovku zatvoríte.</p>
      <h2>Mikrofón a hlas</h2>
      <p>V iPhone, Macu a Androide hlasové vyhľadávanie používa mikrofón, len kým klepnete na tlačidlo hovorenia. To, čo poviete, premení na text rozpoznávanie reči vášho systému: spoločnosť Apple v iPhone a Macu a spoločnosť Google v Androide, vždy podľa ich vlastných zásad ochrany súkromia. Vo Windowse sa reč rozpoznáva priamo vo vašom počítači a zariadenie neopúšťa; len pri veľmi starých procesoroch aplikácia používa hlasový vstup Windowsu, od spoločnosti Microsoft, podľa jej zásad ochrany súkromia. Vo Windowse sa mikrofón otvorí, keď otvoríte hlasový panel, a zatvorí sa, keď ho zatvoríte, alebo po 30 sekundách bez používania; kým nehovoríte, nič sa nenahráva ani neukladá. Mando TV zvuk nenahráva ani neukladá a výsledný text ide priamo do vášho televízora, rovnako ako to, čo píšete na klávesnici.</p>

      <h2>Domov: zariadenia z Apple Home a Google Home</h2>
      <p>Keď otvoríte sekciu Domov (v testovaní), aplikácia požiada o povolenie vidieť zariadenia, ktoré už máte v aplikácii Domov od Apple (HomeKit) alebo v Google Home. S týmto povolením číta ich názov, miestnosť a stav (zapnuté alebo vypnuté, jas, teplota alebo v ktorej fáze programu je domáci spotrebič), aby ich zobrazila a posielala im to, na čo klepnete. Všetko prebieha medzi vaším mobilom a systémom Apple alebo Google: Mando TV tento zoznam neukladá, neodosiela ho nám ani tretím stranám a nepoužíva ho na reklamu ani analýzu. V Androide funguje Google Home s vaším vlastným účtom Google podľa zásad ochrany súkromia spoločnosti Google. Povolenie môžete kedykoľvek odvolať: v iPhone v Nastavenia &gt; Súkromie a zabezpečenie &gt; HomeKit, v Androide v nastaveniach vášho účtu Google.</p>
      <p>Keď klepnete na „Ako vám fungoval Domov?“, otvorí sa vaša e-mailová aplikácia so správou pre hola@mandotv.app, ktorá obsahuje technické zhrnutie: verziu aplikácie, systém a koľko zariadení každého druhu sa zobrazilo a či reagujú. Neobsahuje názvy zariadení, miestností ani vašej domácnosti a správa sa odošle, len ak ju odošlete sami.</p>

      <h2>Skúšobné hlásenie</h2>
      <p>Aplikácia má tlačidlo „Kopírovať skúšobné hlásenie“, ktoré nám pomáha opravovať chyby. Hlásenie zostáva len v pamäti aplikácie, kým je otvorená, a nikdy sa neodosiela samo: rozhodujete vy, či ho skopírujete a pošlete. Neobsahuje kľúče pripojenia, párovacie kódy ani nič, čo zadávate; len kroky, ktoré aplikácia vykonala, ako vyhľadávanie, pripájanie a chyby.</p>

      <h2 id="cookies">Súbory cookie na tejto webovej stránke</h2>
      <p>Týka sa to len webovej stránky mandotv.app, nie aplikácie.</p>
      <h3>Vždy bez súborov cookie</h3>
      <p>Návštevy počítame anonymne pomocou Cloudflare Web Analytics: koľko ľudí stránku navštívi, ktoré stránky čítajú a z ktorej krajiny. Nepoužíva súbory cookie, nepoužíva vašu IP adresu na vašu identifikáciu a nesleduje, čo robíte na iných webových stránkach.</p>
      <h3>So súbormi cookie, len ak súhlasíte</h3>
      <p>Ak v oznámení o súboroch cookie klepnete na „Prijať“, zapneme Google Analytics (od spoločnosti Google LLC), aby sme lepšie pochopili, ako sa stránka používa: zobrazenia stránok, čas strávený na stránke, typ zariadenia, približné mesto a odkiaľ prichádzate. Na to ukladá súbory cookie _ga a _ga_* vo vašom prehliadači až na 2 roky. Google môže tieto údaje spracúvať na serveroch mimo Čile. Vypli sme reklamné funkcie a Google Signals a tieto údaje nepoužívame na zobrazovanie reklám.</p>
      <p>Ak klepnete na „Odmietnuť“ alebo nevyberiete nič, Google Analytics sa nenačíta a neuloží sa žiadny súbor cookie. Svoje rozhodnutie môžete kedykoľvek zmeniť tlačidlom „Cookies“ na konci každej stránky; ak súhlas odvoláte, tieto súbory cookie vymažeme.</p>
      <p>Váš výber sa ukladá vo vašom prehliadači (lokálne úložisko, nikomu sa neodosiela), aby sme sa vás nemuseli pýtať znova.</p>

      <h2>Nákupy</h2>
      <p>Keď si kúpite Mando TV Pro, platbu spracuje obchod s aplikáciami (App Store, Google Play alebo Microsoft Store). Údaje o vašej karte neprijímame ani neukladáme. Obchod aplikácii len potvrdí, že nákup existuje.</p>

      <h2>E-maily, ktoré nám posielate</h2>
      <p>Keď nám napíšete na <a href="mailto:hola@mandotv.app">hola@mandotv.app</a>, používame vašu e-mailovú adresu a to, čo nám oznámite, len na odpoveď. Nezdieľame ich a nepoužívame ich na reklamu. Kedykoľvek môžete požiadať o vymazanie svojich správ.</p>

      <h2>Deti</h2>
      <p>Aplikácia nezbiera údaje od nikoho, ani od detí.</p>

      <h2>Zmeny týchto zásad</h2>
      <p>Ak sa niekedy zmení to, čo aplikácia robí s vašimi údajmi, aktualizujeme túto stránku a dátum navrchu skôr, než sa zmena dostane do aplikácie.</p>
'''


# >>> guías traídas del inglés (ensamblar.py)
# Adaptadas con Ollama (qwen3.6:35b) desde las guías inglesas y auditadas por Opus el 22-nov. Rutas en idiomas_sitio.py.
GUIAS += [
  dict(clave='no-sub', corto='Aplikácia ovládač bez predplatného', fecha='2026-11-23',
    titulo='Aplikácia ovládač televízora bez predplatného a reklám',
    desc='Máte dosť ovládačov s reklamami alebo týždenným predplatným? Mando TV je zadarmo a bez reklám, Pro je voliteľný jednorazový nákup. Poctivé porovnanie.',
    h1='Aplikácia ovládač bez predplatného a bez reklám',
    intro='Mnohé univerzálne ovládače zobrazujú reklamy alebo si pred použitím pýtajú týždenné predplatné. Mando TV ide inou cestou: ovládač je zadarmo, bez reklám a bez účtu. Voliteľné Pro si kúpite len raz. Tu je porovnanie, aj s tým, čo aplikácia nedokáže.',
    pasos=[
      'Pred inštaláciou otvorte stránku aplikácie v obchode a skontrolujte nákupy v aplikácii. Týždenné alebo mesačné ceny naznačujú predplatné.',
      'V Google Play skontrolujte, či sa na stránke uvádza „Obsahuje reklamy“, a prečítajte si najnovšie recenzie s nízkym hodnotením: často sa v nich objavia nečakané platobné bariéry.',
      'Uistite sa, že aplikácia dokáže ovládať váš televízor cez Wi-Fi. Mando TV funguje so Samsung (od roku 2016), LG webOS, Roku, Google TV, Android TV a Fire TV.',
      'Nainštalujte Mando TV, pripojte mobil k tej istej sieti Wi-Fi ako televízor a v zozname klepnite na svoj televízor.',
      'Potvrďte výzvu na televízore alebo zadajte zobrazený kód. Tlačidlá, hlasitosť, kanály a klávesnica nič nestoja.',
    ],
    tabla=dict(titulo='Mando TV v porovnaní s mnohými aplikáciami ovládač',
      cabeza=['', 'Mando TV', 'Mnohé aplikácie s reklamami alebo predplatným'],
      filas=[
        ['Základný ovládač', 'Zadarmo', 'Často zadarmo s reklamami alebo ukrytý za skúšobnou dobou'],
        ['Reklamy', 'Žiadne', 'Časté'],
        ['Predplatné', 'Žiadne. Pro je voliteľný jednorazový nákup', 'Týždenné alebo mesačné plány sú bežné'],
        ['Účet', 'Nie je potrebný', 'Rôzne'],
        ['Televízory Smart TV cez Wi-Fi', 'Samsung (od roku 2016), LG webOS, Roku, Google TV, Android TV, Fire TV, Apple TV (beta)', 'Podľa aplikácie'],
        ['Infračervený signál pre staršie televízory', 'Zadarmo v mobiloch s Androidom s infračerveným vysielačom (novinka)', 'Niektoré aplikácie, len v mobiloch s infračerveným vysielačom'],
        ['Bluetooth', 'Beta od Androidu 9, zadarmo', 'Podľa aplikácie'],
        ['Fotografie a videá do televízora', 'Pro, cez Wi-Fi (nie zrkadlenie)', 'Podľa aplikácie'],
        ['Mobily a počítače', 'iPhone, iPad, Mac a Windows, a Android v predbežnom prístupe', 'Rôzne'],
        ['Zrkadlenie obrazovky', 'Zadarmo na iPhone, iPad a vo Windowse s vstavanou funkciou každého systému. Vo Windowse môže Pro navyše zrkadliť obrazovku počítača na televízory LG, Samsung, Hisense a Android TV (beta)', 'Niektoré aplikácie ho ponúkajú'],
      ],
      nota='Mando TV sa neporovnáva so žiadnou konkrétnou aplikáciou. Aktuálne ceny nájdete na stránke každej aplikácie v obchode.'),
    extra=[
      ('Čo Mando TV nerobí', 'Na iPhone a iPad vás privedie k funkcii Zrkadlenie obrazovky v Ovládacom centre, ktorá je súčasťou samotného iPhonu a funguje s televízormi s AirPlay. Vo Windowse otvorí Prenos (Windows + K) a Mando TV Pro dokáže posielať obrazovku počítača cez vašu sieť Wi-Fi na televízory LG, Samsung, Hisense a Android TV (beta, s oneskorením niekoľkých sekúnd a bez zvuku). S Mando TV Pro dokáže navyše posielať fotografie a videá do televízora cez vašu sieť Wi-Fi. Ovláda televízory Smart TV cez domácu sieť Wi-Fi. Televízory bez funkcií Smart TV sa dajú ovládať z mobilu s Androidom s infračerveným vysielačom cez infračervený signál. Od Androidu 9 sa môže mobil pripojiť aj cez Bluetooth ako klávesnica a ovládač k Google TV, Android TV a Fire TV, celkom bez Wi-Fi. Táto možnosť je v beta verzii a zadarmo.'),
      ('Ako Mando TV zarába', 'Nie reklamami ani vašimi údajmi: aplikácia žiadne nezbiera. Mando TV sa financuje cez Pro, voliteľný jednorazový nákup doplnkov. Základný ovládač je zadarmo.'),
      ('Na zariadeniach, ktoré už máte', 'iPhone, iPad a Mac z App Store, počítače s Windowsom z Microsoft Store a Android cez bezplatný predbežný prístup v Google Play. Pozrite si [Aplikácia ovládač pre iPhone](@iphone) a [Aplikácia ovládač pre Windows](@windows).'),
      ('Súkromie', 'Žiadny účet a žiadne sledovanie v aplikácii. Komunikácia s televízorom prebieha len v lokálnej sieti, údaje o pripojení zostávajú zašifrované vo vašom zariadení. Podrobnosti nájdete v [zásadách ochrany súkromia](@privacidad).'),
    ],
    marca=None,
    faq=[
      ('Existuje aplikácia ovládač bez predplatného?', 'Áno. Mando TV nemá žiadne predplatné: ovládač je zadarmo a bez reklám, Pro je voliteľný jednorazový nákup.'),
      ('Je Mando TV naozaj zadarmo?', 'Áno. Smerové tlačidlá, OK, späť, domov, hlasitosť, kanály, číslice, klávesnica a zapnutie a vypnutie sú zadarmo, bez reklám a bez časového limitu.'),
      ('Funguje to bez Wi-Fi?', 'Väčšinou nie. Mando TV ovláda televízory Smart TV cez vašu domácu sieť Wi-Fi. Výnimky: infračervený signál v mobiloch s Androidom s infračerveným vysielačom, ktorý funguje aj s televízormi bez funkcií Smart TV alebo bez pripojenia k Wi-Fi, a Bluetooth, v beta verzii od Androidu 9, pre Google TV, Android TV a Fire TV.'),
    ]),
  dict(clave='roku-app-alt', corto='Alternatíva k aplikácii Roku', fecha='2026-11-23',
    titulo='Alternatíva k aplikácii Roku: jednoduchý ovládač Roku',
    desc='Alternatíva k aplikácii Roku ako ovládač: Mando TV ovláda Roku TV a prehrávače Roku cez Wi-Fi, bez účtu a reklám, a navyše Samsung, LG a Google TV.',
    h1='Alternatíva k aplikácii Roku: jedna pre všetky televízory',
    intro='Oficiálna aplikácia Roku toho dokáže veľa: Channel Store, prenos obrazu, Private Listening aj ovládač. Ak hľadáte len rýchly ovládač alebo máte doma aj televízor Samsung, LG alebo Google TV, Mando TV je jednoduchá alternatíva, ktorá ovláda Roku cez vašu sieť Wi-Fi bez účtu.',
    pasos=[
      'Pripojte mobil a Roku k tej istej sieti Wi-Fi.',
      'Stiahnite si Mando TV a otvorte ho. Váš televízor Roku alebo prehrávač Roku sa zobrazí v zozname. Klepnite naň. Roku nežiada kód.',
      'Používajte smerové tlačidlá, OK, späť, domov, hlasitosť a klávesnicu. Vyhľadávané výrazy v kanáloch Roku píšte na klávesnici mobilu.',
      'Ak tlačidlá nič nerobia, na Roku prejdite do Settings > System > Advanced system settings > Control by mobile apps a nastavte Network access na „Default“ alebo „Permissive“ (pri novšom softvéri Roku nastavte Control by mobile apps na „Enabled“).',
      'Voliteľne: na televízore Roku zapnite „Fast TV start“ v Settings > System > Power, aby ho Mando TV mohlo zapnúť.',
    ],
    extra=[
      ('Kde Mando TV sedí lepšie', 'Jedna aplikácia pre viac televízorov: Roku, Samsung, LG a Google TV alebo Android TV. Bez účtu, bez reklám. Funguje aj na počítači s Windowsom, čo sa pri písacom stole hodí. Smerové tlačidlá a hlasitosť reagujú rýchlo a na klávesnici bez námahy napíšete vyhľadávané výrazy.'),
      ('Kde je oficiálna aplikácia Roku lepšia', 'Aplikáciu Roku si nechajte na to, čo ponúka nad rámec ovládača, napríklad prehliadanie a pridávanie kanálov z Roku Channel Store, vlastný prenos obrazu a Private Listening (zvuk cez slúchadlá v mobile). Používajte obe, ak chcete. Môžu bežať v tom istom mobile.'),
      ('Televízory Roku TV a prehrávače Roku', 'Fungujú obe. Zahŕňa to modely Roku TV od TCL, Hisense, Philips a ďalších, ako aj Roku Express, Streaming Stick a Ultra. Podrobnosti nájdete na [stránke aplikácie ovládač Roku](@roku).'),
      ('Ak aplikácia Roku prestala fungovať', 'Ak tlačidlá prestali reagovať, Roku zvyčajne blokuje ovládanie aplikáciami. Návod [Aplikácia Roku nefunguje](@roku-403) ukazuje nastavenie, ktoré problém opraví.'),
      ('Zadarmo a Pro', 'Smerové tlačidlá, OK, späť, domov, hlasitosť, kanály, číselné tlačidlá, klávesnica, otváranie aplikácií, prepínanie vstupov a zapnutie alebo vypnutie sú zadarmo, bez reklám a bez predplatného. Touchpad, hlasové príkazy, obľúbené aplikácie, rutiny a časovač vypnutia sú súčasťou Mando TV Pro, jednorazového nákupu bez predplatného.'),
    ],
    marca='roku',
    faq=[
      ('Potrebujem na používanie Mando TV účet Roku?', 'Nie. Mando TV komunikuje s Roku cez vašu domácu sieť a na účet sa nepýta.'),
      ('Nahrádza Mando TV mobilnú aplikáciu Roku úplne?', 'Ako ovládač áno. Na Channel Store, prenos obrazu a Private Listening si nechajte oficiálnu aplikáciu Roku.'),
      ('Funguje to s mojím Roku Express alebo Streaming Stick?', 'Áno. Všetky prehrávače Roku a televízory Roku TV sa ovládajú rovnako.'),
    ]),
  dict(clave='lg-thinq', corto='Alternatíva k aplikácii LG ThinQ', fecha='2026-11-23',
    titulo='Alternatíva k aplikácii LG ThinQ: ovládač LG bez účtu',
    desc='Hľadáte alternatívu k aplikácii LG ThinQ len ako ovládač? Mando TV ovláda televízory LG s webOS cez Wi-Fi, bez účtu LG a bez reklám.',
    h1='Alternatíva k aplikácii LG ThinQ pre váš televízor LG',
    intro='LG ThinQ je oficiálna aplikácia LG, určená pre celú inteligentnú domácnosť: domáce spotrebiče, televízor a ďalšie. Ak chcete len jednoduchý ovládač pre televízor LG, Mando TV urobí presne to cez vašu domácu sieť Wi-Fi, bez toho, aby ste museli vytvárať účet LG, a bez reklám.',
    pasos=[
      'Pripojte mobil alebo počítač (iPhone, Android alebo Windows) a televízor LG k tej istej sieti Wi-Fi.',
      'Stiahnite si Mando TV a otvorte ho. Váš televízor LG sa v zozname zobrazí sám. Klepnite naň.',
      'Na televízore sa zobrazí výzva. Raz ju potvrďte ovládačom televízora, joystickom pod obrazovkou alebo ovládačom Magic Remote.',
      'Tlačidlá, hlasitosť a klávesnica fungujú hneď. Nepotrebujete účet LG a televízor nemusíte registrovať.',
      'Voliteľne: v nastaveniach televízora zapnite „Turn on TV with Mobile“, aby ste televízor mohli zapínať aj z mobilu.',
    ],
    extra=[
      ('Mando TV alebo LG ThinQ: čo na čo', 'ThinQ používajte, ak chcete spravovať domáce spotrebiče LG, ako je práčka, chladnička alebo klimatizácia, alebo potrebujete funkcie účtu LG. Mando TV používajte, ak chcete rýchly a jednoduchý ovládač televízora, ktorý funguje aj pre Samsung, Roku a Google TV v tej istej aplikácii. Mnohí si nechávajú obe: ThinQ pre spotrebiče, Mando TV pre televízor.'),
      ('Čo Mando TV robí na televízore LG', 'Funguje s televízormi LG Smart TV s webOS, teda s väčšinou modelov od roku 2014, vrátane LED, NanoCell, QNED a OLED. Ponúka smerové tlačidlá, OK, späť, domov, hlasitosť, kanály, stlmenie, ovládanie prehrávania a klávesnicu na písanie v YouTube, Netflixe alebo prehliadači. Zoznam aplikácií a zoznam vstupov sú tiež zadarmo. S Pro navyše získate kurzor ako pri Magic Remote.'),
      ('Čo Mando TV nerobí', 'Neovláda domáce spotrebiče LG, nepoužíva váš účet LG a nenahrádza služby účtu LG v televízore. Je to ovládač, nie centrála inteligentnej domácnosti.'),
      ('Súkromie a reklamy', 'Mando TV nemá reklamy ani účet. Komunikuje s televízorom len vo vašej domácej sieti a kľúč pripojenia ukladá zašifrovaný vo vašom zariadení. Všetky funkcie nájdete na stránke [Aplikácia ovládač LG TV](@lg).'),
      ('Zadarmo a Pro', 'Smerové tlačidlá, OK, späť, domov, hlasitosť, kanály, číselné tlačidlá, klávesnica, otváranie aplikácií, prepínanie vstupov a zapnutie alebo vypnutie sú zadarmo, bez reklám a bez predplatného. Touchpad, hlasové príkazy, obľúbené aplikácie, rutiny a časovač vypnutia sú súčasťou Mando TV Pro, jednorazového nákupu bez predplatného.'),
    ],
    marca='lg',
    faq=[
      ('Môžem televízor LG ovládať bez aplikácie LG ThinQ?', 'Áno. Mando TV sa pripája priamo cez vašu sieť Wi-Fi k televízorom LG s webOS. Raz potvrdíte výzvu na televízore a hotovo, celkom bez účtu LG.'),
      ('Funguje Mando TV s kurzorom ovládača LG Magic Remote?', 'Mando TV Pro má kurzor, ktorý posúvate prstom po obrazovke mobilu, podobne ako Magic Remote posúva šípku.'),
      ('Je Mando TV od LG?', 'Nie. Mando TV je nezávislá aplikácia a nemá žiadne prepojenie s LG. LG a ThinQ patria ich vlastníkom a uvádzajú sa len na opis kompatibility.'),
    ]),
  dict(clave='smartthings', corto='Alternatíva k SmartThings', fecha='2026-11-23',
    titulo='SmartThings nefunguje? Jednoduchá alternatíva pre Samsung',
    desc='SmartThings je pomalé alebo chybuje? Mando TV ovláda televízory Samsung s Tizen priamo cez Wi-Fi. Bez účtu Samsung, bez reklám. Krok za krokom.',
    h1='Alternatíva k SmartThings pre televízory Samsung',
    intro='SmartThings je aplikácia Samsung pre celú inteligentnú domácnosť a jej ovládač beží cez váš účet Samsung. Ak prestala fungovať alebo hľadáte rýchle riešenie, Mando TV ovláda televízory Samsung s Tizen, rok výroby 2016 a novšie, priamo cez vašu sieť Wi-Fi bez účtu.',
    pasos=[
      'Pripojte mobil a televízor Samsung k tej istej sieti Wi-Fi.',
      'Stiahnite si Mando TV a otvorte aplikáciu. Váš televízor Samsung sa v zozname zobrazí sám. Klepnite naň.',
      'Televízor sa opýta, či chcete pripojenie povoliť. Vyberte „Allow“ ovládačom alebo tlačidlom na televízore (len pri prvom pripojení).',
      'Hneď používajte smerové tlačidlá, OK, späť, domov, hlasitosť, kanály a klávesnicu.',
      'Voliteľne: zapnite „Power On with Mobile“ v Nastavenia > General > Network > Expert Settings, aby mohlo Mando TV televízor aj zapnúť.',
    ],
    extra=[
      ('Prečo ovládač v mobile prestal fungovať', 'Príčiny sú zvyčajne jednoduché: mobil a televízor sú v rôznych sieťach Wi-Fi, je zapnutá VPN alebo je televízor v hlbokom pohotovostnom režime. Pri SmartThings môže robiť problémy aj účet Samsung, napríklad ak ste boli odhlásení. Mando TV komunikuje priamo s televízorom v domácej sieti, nie je tam žiadny účet na prihlásenie. Ďalšie tipy nájdete v návode [Mobil nenájde televízor](@not-found).'),
      ('Mando TV alebo SmartThings: čo na čo', 'SmartThings si nechajte, ak ho používate pre spotrebiče Samsung, svetlá alebo iné zariadenia inteligentnej domácnosti či pre funkcie účtu Samsung. Mando TV používajte, ak chcete jednoducho rýchly ovládač televízora alebo máte doma aj zariadenie od LG, Roku, Google TV alebo Fire TV: jedna aplikácia ovláda všetky. Obe aplikácie môžu byť nainštalované v tom istom mobile.'),
      ('Ak ste povolenie omylom odmietli', 'Na televízore prejdite do Settings > General > External Device Manager > Device Connection Manager a nastavte Mando TV ako povolené.'),
      ('Nemáte ovládač?', 'Výzvu môžete potvrdiť tlačidlom na samotnom televízore. Návod [Samsung TV bez pôvodného ovládača](@samsung-lost) vám ukáže, ako na to.'),
      ('Zadarmo a Pro', 'Ovládač si môžete stiahnuť a používať zadarmo, bez reklám a bez predplatného. Mando TV Pro je voliteľný jednorazový nákup doplnkov.'),
    ],
    marca='samsung',
    faq=[
      ('Môžem televízor Samsung ovládať bez SmartThings?', 'Áno. Mando TV sa pripája priamo cez vašu sieť Wi-Fi k televízorom Samsung s Tizen. Pripojenie raz povolíte na televízore, bez účtu Samsung.'),
      ('Ovláda Mando TV aj domáce spotrebiče Samsung?', 'Nie. Je to len ovládač televízora. Pre spotrebiče a ďalšie zariadenia inteligentnej domácnosti si nechajte SmartThings.'),
      ('Je Mando TV od Samsungu?', 'Nie. Mando TV je nezávislá aplikácia a nemá žiadne prepojenie so Samsungom. Samsung a SmartThings patria ich vlastníkom a uvádzajú sa len na opis kompatibility.'),
    ]),
  dict(clave='googletv-alt', corto='Alternatíva k ovládaču Google TV', fecha='2026-11-23',
    titulo='Ovládač Google TV nefunguje? Alternatíva',
    desc='Ovládač Google TV v mobile nenájde televízor? Mando TV ovláda Google TV a Android TV cez Wi-Fi, bez účtu Google a reklám.',
    h1='Alternatíva k ovládaču Google TV v mobile',
    intro='Ovládač pre Google TV a Android TV v mobile je súčasťou samotnej aplikácie Google a je prepojený s vaším účtom Google. Ak televízor nenájde, nepohnete sa ďalej. Mando TV je samostatná aplikácia ovládač, ktorá sa páruje 6-znakovým kódom z obrazovky a funguje bez účtu Google, na iPhone, v mobile s Androidom aj na počítači s Windowsom.',
    pasos=[
      'Zapnite televízor a pripojte mobil k tej istej sieti Wi-Fi.',
      'Stiahnite si Mando TV a otvorte aplikáciu. V zozname klepnite na svoj televízor s Google TV alebo Android TV.',
      'Televízor zobrazí 6-znakový kód. Zadajte ho v Mando TV a klepnite na Spárovať.',
      'Používajte smerové tlačidlá, OK, späť, domov, hlasitosť a klávesnicu. Nikde sa nemusíte prihlasovať.',
      'Voliteľne: v nastaveniach televízora hľadajte Wake on LAN alebo „Wake on network“, aby mohla aplikácia televízor aj zapnúť.',
    ],
    extra=[
      ('Prečo ovládač v mobile už televízor nenájde', 'Najčastejšie je to v sieti: mobil a televízor sú v rôznych sieťach Wi-Fi, je zapnutá VPN alebo hosťovská sieť zariadenia izoluje. Opravte to najprv, lebo sa to týka všetkých aplikácií ovládač. Viac v návode [Mobil nenájde televízor](@not-found).'),
      ('S ktorými televízormi to funguje', 'Televízory s Google TV a Android TV od Sony, TCL, Hisense, Philips, Sharp, Xiaomi, Toshiba a ďalších, ako aj Chromecast s Google TV, Google TV Streamer a Nvidia Shield. Všetky sa párujú rovnako, raz kódom z obrazovky.'),
      ('Kde je aplikácia Google lepšia', 'Aplikácia Google vám pomáha aj hľadať obsah na pozeranie a pamätá si váš zoznam na pozretie. Nechajte si ju na to. Mando TV je len ovládač a navyše ovláda zariadenia Samsung, LG, Roku a Fire TV z tej istej aplikácie aj z počítača s Windowsom.'),
      ('Ak chýba stará aplikácia ovládač Android TV', 'Google presunul ovládač v mobile zo starej aplikácie Android TV Remote Control do aplikácie Google TV. Ak hľadáte samostatný ovládač, Mando TV je jedna z možností.'),
      ('Zadarmo a Pro', 'Ovládač si môžete stiahnuť a používať zadarmo, bez reklám a bez predplatného. Mando TV Pro je voliteľný jednorazový nákup doplnkov.'),
    ],
    marca='android',
    faq=[
      ('Potrebujem na používanie Mando TV s Google TV účet Google?', 'Nie. Na spárovanie stačí kód na televízore.'),
      ('Funguje to s Chromecastom s Google TV?', 'Áno. Párovanie prebieha rovnako, 6-znakovým kódom na obrazovke.'),
      ('Môžem to používať z iPhonu?', 'Áno. Mando TV je dostupné v App Store pre iPhone a iPad, v Microsoft Store pre Windows a v bezplatnom predbežnom prístupe v Google Play pre Android.'),
    ]),
  dict(clave='windows', corto='Ovládač pre počítač s Windowsom', fecha='2026-11-23',
    titulo='Aplikácia ovládač pre Windows: televízor z počítača',
    desc='Ovládajte Samsung, LG, Roku, Google TV alebo Fire TV z počítača s Windowsom cez Mando TV: klávesové skratky, mini ovládač a Wi-Fi. V Microsoft Store.',
    h1='Aplikácia ovládač pre počítač s Windowsom',
    intro='Mando TV má aplikáciu pre Windows, ktorá z vášho počítača alebo notebooku urobí cez domácu sieť ovládač televízora. Píšte na televízore na skutočnej klávesnici, nechajte pri práci malé okno ovládača navrchu a jednou aplikáciou ovládajte Samsung, LG, Roku, Google TV alebo Fire TV.',
    pasos=[
      'Nainštalujte si Mando TV zadarmo z Microsoft Store do počítača s Windowsom 10 alebo 11.',
      'Uistite sa, že sú počítač a televízor v tej istej sieti, cez Wi-Fi alebo kábel na tom istom routeri.',
      'Otvorte Mando TV. Televízor sa zobrazí v zozname. Kliknite naň.',
      'Potvrďte výzvu na televízore, ak sa pýta (LG, Samsung), alebo zadajte zobrazený kód (Google TV, Fire TV).',
      'Klikajte na tlačidlá alebo napíšte vyhľadávanie na klávesnici. Hotovo.',
    ],
    extra=[
      ('Klávesové skratky (Pro)', 'S Pro sa klávesnica počítača stane ovládačom: šípky na pohyb, Enter pre OK, Backspace alebo Esc pre návrat, plus a mínus pre hlasitosť, M na stlmenie a medzerník na pauzu.'),
      ('Mini ovládač (Pro)', 'Malé okno ovládača, ktoré zostáva nad všetkými ostatnými oknami. Takto zmeníte hlasitosť alebo pozastavíte prehrávanie bez prerušenia práce.'),
      ('Písanie na televízore z počítača', 'Klávesnica na obrazovke televízora je pomalá. V Mando TV píšete na skutočnej klávesnici a text sa objaví vo vyhľadávacom poli televízora. Táto časť je zadarmo.'),
      ('Viac podrobností', 'Postup krok za krokom nájdete v návode [Ovládanie televízora z počítača](@pc). Pre mobil si prečítajte [Mobil ako ovládač cez Wi-Fi](@wifi).'),
      ('Zadarmo a Pro', 'Smerové tlačidlá, OK, späť, domov, hlasitosť, kanály, číselné tlačidlá, klávesnica, otváranie aplikácií, prepínanie vstupov a zapnutie alebo vypnutie sú zadarmo, bez reklám a bez predplatného. Touchpad, hlasové príkazy, obľúbené aplikácie, rutiny a časovač vypnutia sú súčasťou Mando TV Pro, jednorazového nákupu bez predplatného. Vo Windowse kúpite Pro cez Microsoft Store.'),
      ('Hlasové príkazy z počítača (Pro)', 'S Pro môžete s televízorom hovoriť cez mikrofón počítača. Reč sa rozpoznáva priamo v počítači: nepotrebujete internet ani nič nastavovať vo Windowse. To, čo poviete, počítač nikdy neopustí a neukladá sa. Len pri veľmi starých procesoroch sa aplikácia vráti k hlasovému vstupu Windowsu. Na to musí byť v nastaveniach súkromia zapnuté online rozpoznávanie reči a vo Windowse pridaný váš jazyk.'),
    ],
    marca=None,
    faq=[
      ('Potrebuje aplikácia ovládač pre Windows Bluetooth alebo kábel?', 'Nie. Používa vašu domácu sieť. Počítač a televízor musia byť len pripojené k tomu istému routeru.'),
      ('Ktoré televízory môžem ovládať z Windowsu?', 'Televízory Samsung s Tizen, LG s webOS, Roku TV a prehrávače, Google TV a Android TV a Fire TV.'),
      ('Môžem vidieť obraz televízora v počítači alebo ho počuť cez reproduktory počítača?', 'Nie. Mando TV je len ovládač. Obraz televízora nezrkadlí ani nestreamuje do počítača.'),
      ('Prečo hlas v mojom počítači s Windowsom nefunguje?', 'Hlasové ovládanie je funkcia Pro. Skontrolujte teda, či je Pro aktívne a mikrofón počítača funguje. Na väčšine počítačov sa reč rozpoznáva priamo v počítači, bez internetu. Len pri veľmi starých procesoroch aplikácia používa hlasový vstup Windowsu: vtedy zapnite online rozpoznávanie reči v nastaveniach súkromia Windowsu a pridajte svoj jazyk v jazykových nastaveniach.'),
    ]),
  dict(clave='iphone', corto='Aplikácia ovládač pre iPhone', fecha='2026-11-23',
    titulo='Aplikácia ovládač pre iPhone: Samsung, LG, Roku, Google TV',
    desc='Použite iPhone ako ovládač pre Samsung, LG, Roku, Google TV a Fire TV cez Wi-Fi. Zadarmo v App Store, bez účtu a bez reklám.',
    h1='Aplikácia ovládač pre iPhone: jedna pre všetky televízory',
    intro='Mando TV zmení váš iPhone alebo iPad na ovládač pre Samsung, LG, Roku, Google TV alebo Android TV a Fire TV cez vašu domácu sieť Wi-Fi. Aplikácia je zadarmo v App Store, bez účtu a bez reklám. Beží aj na Androide a vo Windowse.',
    pasos=[
      'Stiahnite si Mando TV zadarmo z App Store.',
      'Pripojte iPhone a televízor k tej istej sieti Wi-Fi.',
      'Otvorte Mando TV a klepnite na Povoliť, keď sa iOS opýta na prístup k lokálnej sieti. Aplikácia ho potrebuje, aby televízor našla.',
      'V zozname klepnite na svoj televízor. Potvrďte výzvu na televízore, ak sa pýta (LG a Samsung), alebo zadajte kód, ktorý televízor zobrazí (Google TV alebo Fire TV).',
      'Používajte tlačidlá, hlasitosť a klávesnicu. Ste pripojení.',
    ],
    extra=[
      ('Funguje s týmito televízormi', 'LG webOS, Samsung Tizen (rok výroby 2016 a novšie), Roku TV a prehrávače Roku, Google TV a Android TV a Fire TV. Stránky značiek sú [Samsung](@samsung), [LG](@lg), [Roku](@roku) a [Android TV](@android).'),
      ('Prečo sa pýta na lokálnu sieť', 'iPhone blokuje aplikáciám prístup k zariadeniam vo vašej domácej sieti, pokiaľ to nepovolíte. Ak sa televízor v zozname nezobrazí, otvorte Nastavenia > Mando TV a zapnite „Lokálna sieť“. Aplikácia komunikuje len s vaším televízorom vo vašej domácej sieti.'),
      ('Prečo Mando TV a nie aplikácia výrobcu', 'Každá značka televízorov má vlastnú aplikáciu a chce vlastné nastavenie alebo účet. Mando TV je jedna aplikácia pre všetky, bez účtu.'),
      ('Zadarmo a Pro na iPhone', 'Smerové tlačidlá, OK, späť, domov, hlasitosť, kanály, číselné tlačidlá, klávesnica, otváranie aplikácií, prepínanie vstupov a zapnutie alebo vypnutie sú zadarmo, bez reklám a bez predplatného. Touchpad, hlasové príkazy, obľúbené aplikácie, rutiny a časovač vypnutia sú súčasťou Mando TV Pro, jednorazového nákupu bez predplatného. Pro kúpite raz priamo v aplikácii.'),
    ],
    marca=None,
    faq=[
      ('Je Mando TV na iPhone zadarmo?', 'Stiahnutie je zadarmo, bez reklám. Základný ovládač je zadarmo, rovnako ako otváranie aplikácií a prepínanie vstupov. Doplnky ako touchpad, hlasové príkazy a rutiny sú súčasťou Mando TV Pro, jednorazového nákupu.'),
      ('Funguje to na iPade?', 'Áno. Tá istá aplikácia beží na iPhone aj iPade.'),
      ('Potrebuje aplikácia ovládač pre iPhone Bluetooth alebo infračervený vysielač?', 'Na iPhone nie. iPhony nemajú infračervený vysielač, preto tam ovládanie infračerveným signálom nie je k dispozícii, a možnosť Bluetooth je len pre Android 9 alebo novší, nie pre iPhone. Na iPhone ovláda Mando TV televízory Smart TV aj Apple TV (beta) cez vašu domácu sieť Wi-Fi.'),
    ]),
  dict(clave='firetv', corto='Ovládač Fire TV', fecha='2026-11-23',
    titulo='Aplikácia ovládač Fire TV pre mobil a počítač',
    desc='Ovládač Fire TV v mobile: ovládajte Fire TV Stick, Fire TV Cube alebo televízor s Fire TV cez Wi-Fi so 4-miestnym PIN-om. Bez aplikácie Amazon.',
    h1='Ovládač Fire TV pre váš mobil alebo počítač',
    intro='Ak je ovládač Fire TV preč alebo sú vybité batérie, Mando TV ovláda Fire TV Stick, Fire TV Cube alebo televízor s vstavaným Fire TV cez Wi-Fi. Párovanie prebieha 4-miestnym PIN-om. Fire TV je v Mando TV novinka, preto najprv aktualizujte aplikáciu.',
    pasos=[
      'Aktualizujte Mando TV na najnovšiu verziu z App Store, Microsoft Store alebo Google Play.',
      'Zapnite Fire TV a pripojte mobil k tej istej sieti Wi-Fi.',
      'Otvorte Mando TV. Váš Fire TV sa zobrazí v zozname. Klepnite naň.',
      'Na obrazovke televízora sa zobrazí 4-miestny PIN. Zadajte ho v Mando TV. Urobíte to len raz.',
      'Používajte smerové tlačidlá, OK, späť, domov, tlačidlá prehrávania a klávesnicu na vyhľadávanie.',
    ],
    extra=[
      ('Podporované zariadenia Fire TV', 'Fire TV Stick, Fire TV Stick 4K, Fire TV Cube a televízory s vstavaným Fire TV, napríklad televízory Amazon Fire TV Edition a niektoré modely Hisense. Podpora je nová a zatiaľ sme mohli otestovať len málo skutočných zariadení. Ak niečo nefunguje podľa očakávania, napíšte nám model cez stránku pomoci.'),
      ('Zapnutie Fire TV', 'Mando TV Fire TV cez sieť nezapína. Zapnite televízor tlačidlom napájania na ňom: zapojený Fire TV Stick alebo Cube sa zvyčajne prebudí cez HDMI-CEC a pri televízore s vstavaným Fire TV je televízor samotný Fire TV. Potom ho ovládate z mobilu.'),
      ('Ak sa váš Fire TV nezobrazí', 'Uistite sa, že sú obe zariadenia v tej istej sieti Wi-Fi a Fire TV je prebudený. Na iPhone povoľte pre Mando TV v nastaveniach „Lokálna sieť“. Pozrite si [mobil nenájde televízor](@not-found).'),
      ('Nemáte vôbec žiadny ovládač?', 'Fire TV musí zobraziť PIN na obrazovke, takže televízor aj Fire TV musia byť zapnuté a zobrazovať obraz. Ak je televízor na nesprávnom vstupe, prepnite ho tlačidlami na televízore. Pozrite si [Zmena vstupu bez ovládača](@hdmi).'),
      ('Zadarmo a Pro', 'Smerové tlačidlá, OK, späť, domov, hlasitosť, kanály, číslice, klávesnica, otváranie aplikácií, prepínanie vstupov a zapnutie alebo vypnutie sú zadarmo, bez reklám a bez predplatného. Touchpad, hlasové príkazy, obľúbené aplikácie, rutiny a časovač vypnutia sú súčasťou Mando TV Pro, jednorazového nákupu bez predplatného.'),
    ],
    marca=None,
    faq=[
      ('Potrebujem aplikáciu Amazon Fire TV?', 'Nie. Mando TV sa pripája k Fire TV cez vašu sieť Wi-Fi pomocou PIN-u. V mobile nepotrebujete účet Amazon.'),
      ('Funguje to s televízormi s Fire TV a s Fire TV Stickmi?', 'Áno, práve na to bolo vytvorené. Podpora je nová, aplikáciu udržiavajte aktuálnu a dajte nám vedieť o modeloch, ktoré nefungujú podľa očakávania.'),
      ('Prečo potrebujem PIN?', 'Fire TV zobrazí 4-miestny PIN ako dôkaz, že sedíte pred televízorom. Nikto sa nemôže spárovať bez toho, aby videl obrazovku.'),
    ]),
  dict(clave='firetv-lost', corto='Stratený ovládač Fire TV', fecha='2026-11-23',
    titulo='Stratený ovládač Fire TV? Pomôže mobil',
    desc='Stratili ste ovládač Fire TV Stick? Ovládajte ho mobilom cez Wi-Fi, spárovaným 4-miestnym PIN-om. Tipy pre novú sieť Wi-Fi a HDMI-CEC.',
    h1='Stratený ovládač Fire TV: takto použijete mobil',
    intro='Ak je ovládač pre váš Fire TV Stick, Fire TV Cube alebo televízor Smart TV s Fire TV stratený alebo prestal fungovať, ovládanie prevezme mobil, kým je Fire TV stále pripojený k vašej sieti Wi-Fi. Párovanie prebieha 4-miestnym PIN-om na obrazovke, takže starý ovládač na to nikdy nepotrebujete.',
    pasos=[
      'Zapnite televízor tlačidlom na ňom. Zapojený Fire TV Stick alebo Cube sa zvyčajne prebudí tiež; pri zapnutom HDMI-CEC televízor často prepne na jeho vstup sám.',
      'Ak televízor ukazuje iný vstup, prepnite ho tlačidlom vstupu alebo zdroja na televízore. Pozrite si [Zmena vstupu bez ovládača](@hdmi).',
      'Pripojte mobil k tej istej sieti Wi-Fi ako Fire TV.',
      'Stiahnite si Mando TV a otvorte aplikáciu. Váš Fire TV sa zobrazí v zozname. Klepnite naň.',
      'Televízor zobrazí 4-miestny PIN. Zadajte ho v Mando TV. Urobíte to len raz.',
      'Používajte smerové tlačidlá, OK, späť, domov, hlasitosť, tlačidlá prehrávania a klávesnicu v mobile.',
    ],
    extra=[
      ('Najprv vyskúšajte ovládač televízora (HDMI-CEC)', 'Mnohé ovládače televízorov dokážu ovládať Fire TV Stick cez HDMI-CEC. Ak vidíte rozhranie Fire TV, stlačte šípky a OK na ovládači televízora. Ak sa nič nestane, zapnite CEC v nastaveniach televízora (Anynet+ u Samsungu, SIMPLINK u LG, BRAVIA Sync u Sony) a vo Fire TV ovládanie zariadení HDMI-CEC v nastaveniach zobrazenia („Display & Sounds“).'),
      ('Ak ste zmenili sieť Wi-Fi', 'Bez ovládača nemôžete na Fire TV zadať heslo novej siete Wi-Fi, ale existuje východisko: na druhom mobile vytvorte hotspot s presne rovnakým názvom a heslom ako vaša stará sieť Wi-Fi. Fire TV sa k nemu pripojí automaticky. Pripojte k tomuto hotspotu mobil s Mando TV, spárujte ho PIN-om, potom na Fire TV prejdite do Nastavenia > Sieť a vyberte svoju novú sieť Wi-Fi. Nakoniec pripojte k novej sieti Wi-Fi aj svoj mobil.'),
      ('Spárovanie náhradného ovládača', 'Väčšina nových ovládačov Fire TV sa páruje podržaním tlačidla Home asi 10 sekúnd v blízkosti Fire TV. Ak to nepomôže, otvorte Nastavenia > Ovládače a zariadenia Bluetooth > Diaľkové ovládače Amazon Fire TV > Pridať nový ovládač. K tejto ponuke sa dostanete aj z mobilu cez Mando TV.'),
      ('Fire TV vstavaný v televízore', 'Pri televízoroch s vstavaným Fire TV, ako sú mnohé modely Insignia a Toshiba, fungujú rovnaké kroky, pretože televízor je samotný Fire TV.'),
      ('Predtým, než začnete', 'Podpora Fire TV je v Mando TV novinka. Najprv aplikáciu aktualizujte. Ak váš model nereaguje podľa očakávania, napíšte nám cez [stránku pomoci](@soporte) a uveďte model.'),
      ('Zadarmo a Pro', 'Ovládač si môžete stiahnuť a používať zadarmo, bez reklám a bez predplatného. Mando TV Pro je voliteľný jednorazový nákup doplnkov.'),
    ],
    marca=('firetv', 'Ovládač Fire TV'),
    faq=[
      ('Môžem Fire TV Stick ovládať mobilom bez ovládača?', 'Áno, kým je Fire TV zapnutý a pripojený k vašej sieti Wi-Fi. Mando TV páruje cez 4-miestny PIN na televízore, takže starý ovládač nepotrebujete.'),
      ('Funguje to, ak je Fire TV v novej sieti Wi-Fi?', 'Nie priamo, pretože mobil a Fire TV musia byť v tej istej sieti. Najprv dostaňte Fire TV znova online trikom s hotspotom z tejto stránky.'),
      ('Potrebujem aplikáciu Amazon Fire TV alebo účet Amazon?', 'Nie. Mando TV sa pripája cez vašu domácu sieť pomocou PIN-u a nepotrebuje vlastný účet.'),
    ]),
  dict(clave='turn-on', corto='Zapnutie televízora bez ovládača', fecha='2026-11-23',
    titulo='Zapnutie televízora bez ovládača (všetky značky)',
    desc='Zapnite televízor bez ovládača: kde je tlačidlo na Samsung, LG, TCL, Hisense a Sony. Plus HDMI-CEC a triky s mobilom.',
    h1='Ako zapnúť televízor bez ovládača',
    intro='Takmer každý televízor má stále fyzické tlačidlo zapnutia a vypnutia. Len je dobre skryté. Tu zistíte, kde je pri každej značke, plus dva spôsoby, ako si nabudúce ušetriť hľadanie: HDMI-CEC z konzoly alebo streamovacieho zariadenia a zapnutie televízora z mobilu cez Wi-Fi.',
    pasos=[
      'Pozrite sa pod stred obrazovky, hneď za logo značky. Mnohé televízory majú tam malé jedno tlačidlo alebo joystick smerujúci nadol.',
      'Ak tam nie je, ohmatajte zadnú stranu televízora pri dolných rohoch, potom na ľavom a pravom okraji.',
      'Stlačte tlačidlo raz. Pri mnohých televízoroch s jedným tlačidlom krátke stlačenie pri zapnutom televízore otvorí malú ponuku vstupov a hlasitosti a dlhé stlačenie ho vypne.',
      'Stále nič? Skontrolujte napájací kábel na oboch koncoch a skúste inú zásuvku. Ak nesvieti kontrolka pohotovostného režimu, televízor nedostáva napätie.',
      'Keď je televízor zapnutý, nastavte ho tak, aby ste tlačidlo už nepotrebovali: zapnite HDMI-CEC a zapnutie cez sieť, obe sú vysvetlené nižšie.',
    ],
    extra=[
      ('Kde je tlačidlo zapnutia podľa značky', 'Samsung: ovládacie tlačidlo alebo joystick pod stredom obrazovky alebo vzadu pri dolnom rohu. LG: joystick pod logom LG pri väčšine modelov. TCL a Hisense: zvyčajne malé tlačidlo pod stredom obrazovky alebo vzadu pri dolnom rohu. Sony: vzadu alebo na bočnom okraji, dole blízko okraja. Vizio: vzadu, dole vľavo alebo dole vpravo, alebo na boku. Polohy sa líšia podľa modelu. Ak ho nenájdete, vyhľadajte návod na obsluhu podľa čísla modelu na štítku vzadu.'),
      ('Zapnutie televízora cez konzolu alebo streamovacie zariadenie (HDMI-CEC)', 'So zapnutým HDMI-CEC zapnutie PlayStation, Xboxu, prehrávača Roku, Fire TV Sticku alebo Chromecastu zapne aj televízor a prepne na správny vstup. Každá značka nastavenie nazýva inak: Anynet+ u Samsungu, SIMPLINK u LG, BRAVIA Sync u Sony a CEC u väčšiny ostatných. Viac v návode [Zapnutie televízora a prepnutie na HDMI konzoly](@console).'),
      ('Zapnutie televízora z mobilu', 'Televízory Smart TV sa dajú prebudiť cez Wi-Fi, keď to raz povolíte, a potom ich Mando TV zapne z mobilu. Na Samsungu zapnite „Power On with Mobile“ v Nastavenia > General > Network > Expert Settings. Na LG zapnite „Turn on TV with Mobile“ ([krok za krokom](@lg-on)). Na Roku TV zapnite „Fast TV start“ v Settings > System > Power. Na Google TV a Android TV hľadajte Wake on LAN alebo „Wake on network“, ak ho váš model má. Robí sa to raz, pri zapnutom televízore.'),
      ('Ak tlačidlo nenájdete', 'Niektoré novšie televízory ukrývajú jediné tlačidlo tak dobre, že pôsobí, akoby žiadne nebolo. Hľadajte malú vypuklinu alebo oblasť svetelného snímača pod obrazovkou: tlačidlo je často hneď vedľa. Cez Wi-Fi potrebuje Mando TV, aby bol televízor raz zapnutý a pripojený. Výnimkou je infračervený signál: v mobile s Androidom s infračerveným vysielačom dokáže Mando TV zapnúť televízor, ktorý nebol nikdy nastavený, ak mobil namierite na televízor. Infračervený signál je novinka a funguje so značkami v zozname kódov aplikácie.'),
      ('Zadarmo a Pro', 'Ovládač si môžete stiahnuť a používať zadarmo, bez reklám a bez predplatného. Mando TV Pro je voliteľný jednorazový nákup doplnkov.'),
    ],
    marca=None,
    faq=[
      ('Môžem televízor zapnúť mobilom, ak som ho nikdy nenastavil?', 'Nie cez Wi-Fi. Vypnutý televízor sa prebudí zo siete, len ak bolo predtým zapnuté zapnutie cez sieť. Prvýkrát použite tlačidlo na televízore. Výnimkou je mobil s Androidom s infračerveným vysielačom: Mando TV dokáže televízor bez nastavenia zapnúť infračerveným signálom, ak je značka v zozname kódov alebo vyberiete „Iná značka alebo neviem“.'),
      ('Ako zapnem televízor Samsung bez ovládača?', 'Stlačte ovládacie tlačidlo pod stredom obrazovky alebo vzadu pri dolnom rohu. Potom zapnite „Power On with Mobile“, aby ho mohol mobil nabudúce zapnúť.'),
      ('Ako zapnem Roku TV bez ovládača?', 'Použite tlačidlo na televízore, zvyčajne pod stredom alebo vzadu. Potom zapnite „Fast TV start“ v Settings > System > Power, aby ho mohlo Mando TV zapnúť z mobilu.'),
      ('Prečo sa môj televízor zapne automaticky, keď zapnem konzolu?', 'To je HDMI-CEC. Je to praktické a v nastaveniach televízora ho môžete vypnúť, ak chcete.'),
    ]),
  dict(clave='sony', corto='Ovládač Sony', fecha='2026-11-23',
    titulo='Aplikácia ovládač Sony pre mobil a počítač',
    desc='Mando TV ovláda televízory Sony Bravia s Google TV alebo Android TV cez Wi-Fi. Beta podpora modelov z rokov 2013 až 2015 bez Androidu.',
    h1='Ako ovládať televízor Sony mobilom',
    intro='Novšie televízory Sony Bravia Smart TV používajú Google TV, staršie modely od roku 2015 Android TV. Mando TV ovláda oba cez vašu sieť Wi-Fi z iPhonu, mobilu s Androidom alebo počítača s Windowsom. Aplikácia nahradí pôvodný ovládač, ak sa stratil alebo sa vybili batérie.',
    pasos=[
      'Skontrolujte, či váš televízor Sony zobrazuje domovskú obrazovku Google TV alebo Android TV. Platí to pre väčšinu televízorov Sony Bravia Smart TV od roku výroby 2015.',
      'Pripojte mobil a televízor k tej istej sieti Wi-Fi.',
      'Otvorte Mando TV a v zozname klepnite na svoj televízor Sony.',
      'Zadajte 6-znakový kód, ktorý televízor zobrazí na obrazovke (len pri prvom pripojení). Ovládač na to nepotrebujete.',
      'Používajte smerové tlačidlá, OK, späť, domov, hlasitosť a klávesnicu.',
    ],
    extra=[
      ('Zapnutie televízora Sony z mobilu', 'Modely Sony s Google TV alebo Android TV sa dajú prebudiť cez sieť, ak je zapnuté „Remote start“. Možnosť zvyčajne nájdete v Nastavenia > Sieť a internet > Remote start (cesta sa podľa modelu môže mierne líšiť). Potom klepnite v Mando TV na televízor, keď je vypnutý, a aplikácia ho zapne.'),
      ('Kde je tlačidlo zapnutia na Sony', 'Pri väčšine televízorov Bravia je vzadu, blízko dolného ľavého alebo pravého rohu, alebo na bočnom okraji. Krátke stlačenie televízor zapne. Viac nájdete v návode [Zapnutie televízora bez ovládača](@turn-on).'),
      ('Staršie televízory Sony', 'Televízory Sony Bravia z rokov 2013 až 2015, ktoré nepoužívajú Android, sú v Mando TV podporované v beta verzii. Je to novinka a môže mať ešte svoje nedostatky. Televízor zobrazí 4-miestny PIN, ktorý musíte zadať v aplikácii. Ostatné televízory Sony bez Google TV alebo Android TV sa momentálne nepodporujú.'),
      ('Zadarmo a Pro', 'Ovládač si môžete stiahnuť a používať zadarmo, bez reklám a bez predplatného. Mando TV Pro je voliteľný jednorazový nákup doplnkov.'),
    ],
    marca='android',
    faq=[
      ('Funguje Mando TV s televízormi Sony Bravia?', 'Áno, s televízormi Sony, ktoré používajú Google TV alebo Android TV. Zahŕňa to väčšinu televízorov Sony Smart TV od roku výroby 2015.'),
      ('Potrebujem aplikáciu Sony alebo účet Google?', 'Nie. Mando TV sa páruje kódom na obrazovke televízora a nevyžaduje účet.'),
      ('Funguje to so staršími televízormi Sony Bravia bez Androidu?', 'Áno, v beta verzii, pri modeloch Bravia z rokov 2013 až 2015 bez Androidu. Párovanie prebieha 4-miestnym PIN-om, ktorý televízor zobrazí.'),
      ('Môžem na televízore Sony písať z mobilu?', 'Áno. Klávesnica je zadarmo a funguje v YouTube, Netflixe aj vo vyhľadávaní televízora.'),
    ]),
  dict(clave='tcl', corto='Ovládač TCL', fecha='2026-11-23',
    titulo='Aplikácia ovládač TCL pre mobil a počítač',
    desc='Stratili ste ovládač TCL? Väčšina televízorov TCL používa Roku TV alebo Google TV. Mando TV ovláda oboje cez Wi-Fi, bez účtu a reklám.',
    h1='Ako ovládať televízor TCL mobilom',
    intro='TCL vyrába televízor, ale softvér je Roku TV alebo Google TV (pri starších modeloch Android TV). Mando TV ovláda oba systémy a funguje ako ovládač vášho televízora TCL cez Wi-Fi. Zadarmo, bez účtu a reklám.',
    pasos=[
      'Zistite, aký systém váš TCL používa. Ak domovská obrazovka zobrazuje jednoduchú mriežku dlaždíc kanálov, je to Roku TV. Ak vyzerá ako Google TV alebo Android TV s radmi plnými odporúčaní, je to Google TV.',
      'Pripojte mobil a televízor TCL k tej istej sieti Wi-Fi.',
      'Otvorte Mando TV. TCL sa v zozname zobrazí sám. Klepnite naň.',
      'Pri TCL s Roku TV nie je potrebné nič ďalšie. Pri TCL s Google TV zadáte 6-znakový kód, ktorý televízor zobrazí na obrazovke (len pri prvom pripojení).',
      'Používajte šípky, OK, späť, domov, hlasitosť a klávesnicu. Televízor zapnite cez aplikáciu, ak ste zapli zapnutie cez sieť (pozrite nižšie).',
    ],
    extra=[
      ('Zapnutie televízora TCL z mobilu', 'Pri TCL Roku TV zapnite „Fast TV start“ v Settings > System > Power. Pri TCL Google TV hľadajte v nastaveniach siete alebo napájania možnosť Wake on LAN, „Wake on network“ alebo vzdialený štart. Niektoré modely ju nemajú. V takom prípade zapnite televízor fyzickým tlačidlom, zvyčajne dole uprostred alebo vzadu.'),
      ('Ak sa váš TCL nezobrazí', 'Skontrolujte, či sú mobil a televízor v tej istej sieti Wi-Fi. Routery s oddelenými sieťami 2,4 GHz a 5 GHz môžu zariadenia pred sebou skrývať. Na iPhone povoľte pre Mando TV v nastaveniach „Lokálna sieť“. Televízor môžete pridať aj zadaním jeho IP adresy. Prečítajte si [Mobil nenájde televízor](@not-found).'),
      ('Viac o vašom TCL', 'Pre TCL s Roku TV pozrite [Aplikácia ovládač Roku](@roku), pre TCL s Google TV alebo Android TV [Aplikácia ovládač Android TV](@android).'),
      ('Zadarmo a Pro', 'Smerové tlačidlá, OK, späť, domov, hlasitosť, kanály, číslice, klávesnica, otváranie aplikácií, prepínanie vstupov a zapnutie alebo vypnutie sú zadarmo, bez reklám a bez predplatného. Touchpad, hlasové príkazy, obľúbené aplikácie, rutiny a časovač vypnutia sú súčasťou Mando TV Pro, jednorazového nákupu bez predplatného.'),
    ],
    marca=None,
    faq=[
      ('Funguje Mando TV s každým televízorom TCL?', 'Funguje s televízormi TCL s Roku TV, Google TV alebo Android TV, teda s väčšinou televízorov TCL Smart TV. TCL, ktorý nie je Smart TV, sa cez Wi-Fi ovládať nedá.'),
      ('Potrebujem aplikáciu TCL alebo účet TCL?', 'Nie. Mando TV sa pripája priamo cez vašu domácu sieť Wi-Fi a nevyžaduje účet.'),
      ('Môj TCL žiada kód. Kde je?', 'Modely TCL s Google TV a Android TV zobrazia 6-znakový kód na obrazovke. Zadajte ho v Mando TV presne tak, ako sa zobrazí. TCL s Roku TV na kód nežiada.'),
    ]),
  dict(clave='hisense', corto='Ovládač Hisense', fecha='2026-11-23',
    titulo='Aplikácia ovládač Hisense: čo funguje v mobile',
    desc='Ovládač Hisense s Mando TV: ovládanie pre VIDAA, Roku TV, Google TV a Fire TV cez Wi-Fi. Poctivý prehľad toho, čo funguje.',
    h1='Aplikácia ovládač Hisense: čo funguje a čo nie',
    intro='Televízory Hisense nie sú vo vnútri všetky rovnaké. Podľa modelu používajú vlastný systém VIDAA od Hisense, Roku TV, Google TV alebo Fire TV. Mando TV funguje ako ovládač Hisense na všetkých štyroch systémoch, s jednou výnimkou pri niektorých novších modeloch VIDAA. Tu zistíte, ako rozpoznať, aký systém máte a čo vás čaká.',
    pasos=[
      'Skontrolujte, aký systém váš Hisense používa. VIDAA je vlastné rozhranie Hisense. Roku TV zobrazuje mriežku dlaždíc kanálov. Google TV zobrazuje rady odporúčaní. Fire TV zobrazuje domovskú obrazovku Fire TV s radmi Amazonu.',
      'Pripojte mobil a televízor Hisense k tej istej sieti Wi-Fi.',
      'Otvorte Mando TV. Televízor sa v zozname zobrazí sám. Klepnite naň.',
      'Modely VIDAA a Fire TV môžu zobraziť štvorciferný PIN; Google TV zobrazí šesťznakový kód. Zadajte ho v aplikácii. Roku TV sa na nič nepýta. Urobíte to len raz.',
      'Používajte šípky, OK, späť, domov, hlasitosť a klávesnicu v mobile.',
    ],
    extra=[
      ('Hisense s Roku TV alebo Google TV', 'Fungujú úplne ako každý iný televízor Roku alebo Google TV. Podrobnosti na stránkach [Aplikácia ovládač Roku](@roku) a [Aplikácia ovládač Android TV](@android).'),
      ('Hisense s Fire TV', 'Podpora Fire TV je v Mando TV novinka. Aktualizujte aplikáciu na najnovšiu verziu vo svojom obchode. Ako funguje párovanie s PIN-om, nájdete na stránke [Ovládač Fire TV](@firetv). Ak niečo nefunguje podľa očakávania, napíšte nám cez stránku pomoci a uveďte model.'),
      ('Hisense s VIDAA', 'Väčšina modelov VIDAA funguje: tlačidlá, hlasitosť, klávesnica, aplikácie a vstupy. Niektoré novšie modely VIDAA akceptujú len oficiálnu aplikáciu Hisense. Mando TV to pri pripájaní rozpozná a jasne vám to povie namiesto toho, aby ticho zlyhalo. V takom prípade je správnou cestou aplikácia Hisense pre váš model, tlačidlá na televízore alebo pôvodný ovládač.'),
      ('Zapnutie Hisense z mobilu', 'Pri Hisense Roku TV zapnite „Fast TV start“ v Settings > System > Power. Pri Google TV hľadajte možnosť Wake on LAN alebo „Wake on network“. Ak žiadna neexistuje, použite tlačidlo zapnutia na televízore.'),
      ('Zadarmo a Pro', 'Smerové tlačidlá, OK, späť, domov, hlasitosť, kanály, číselné tlačidlá, klávesnica, otváranie aplikácií, prepínanie vstupov a zapnutie alebo vypnutie sú zadarmo, bez reklám a bez predplatného. Touchpad, hlasové príkazy, obľúbené aplikácie, rutiny a časovač vypnutia sú súčasťou Mando TV Pro, jednorazového nákupu bez predplatného.'),
    ],
    marca=None,
    faq=[
      ('Funguje Mando TV s Hisense VIDAA?', 'Áno, s väčšinou modelov VIDAA. Niektoré novšie akceptujú len oficiálnu aplikáciu Hisense; Mando TV to rozpozná a povie vám to. Televízory Hisense s Roku TV, Google TV alebo Fire TV sú tiež podporované.'),
      ('Ako zistím, či je môj Hisense Roku TV, Google TV alebo Fire TV?', 'Pozrite sa na domovskú obrazovku. Roku TV má jednoduchú mriežku dlaždíc a pri štarte logo Roku. Google TV má rady odporúčaní. Fire TV má domovskú obrazovku Amazon Fire TV. Názov modelu v Nastavenia > Informácie tiež napovie.'),
      ('Potrebujem účet Hisense alebo Google?', 'Nie. Mando TV sa pripája priamo cez vašu domácu sieť Wi-Fi a nemá vlastný účet.'),
    ]),
  dict(clave='philips', corto='Ovládač Philips', fecha='2026-11-23',
    titulo='Aplikácia ovládač Philips: Roku TV, Google TV, Android TV',
    desc='Mando TV ovláda televízory Philips s Roku TV, Google TV alebo Android TV cez Wi-Fi, z mobilu alebo počítača. Titan OS nie je podporovaný.',
    h1='Ako ovládať televízor Philips mobilom',
    intro='Televízory Philips používajú podľa krajiny a roku výroby rôzne systémy: Roku TV v USA, Google TV alebo Android TV v mnohých krajinách a Titan OS pri niektorých novších európskych modeloch. Mando TV ovláda modely s Roku TV, Google TV a Android TV cez Wi-Fi.',
    pasos=[
      'Skontrolujte domovskú obrazovku. Roku TV zobrazuje mriežku dlaždíc. Google TV a Android TV zobrazujú rady odporúčaní od Googlu. Titan OS má vlastnú domovskú obrazovku.',
      'Pripojte mobil a televízor k tej istej sieti Wi-Fi.',
      'Otvorte Mando TV a v zozname klepnite na svoj televízor Philips.',
      'Roku TV sa na nič nepýta. Google TV a Android TV zobrazia 6-znakový kód: zadajte ho v aplikácii raz.',
      'Používajte smerové tlačidlá, OK, späť, domov, hlasitosť a klávesnicu.',
    ],
    extra=[
      ('Philips Roku TV', 'Funguje ako každý televízor Roku. Ak ho chcete zapínať z mobilu, zapnite „Fast TV start“ v Settings > System > Power. Viac na stránke [Aplikácia ovládač Roku](@roku).'),
      ('Philips s Google TV alebo Android TV', 'Zahŕňa mnohé modely Ambilight. Párujú sa kódom na obrazovke. Ak ich chcete zapínať z mobilu, v nastaveniach siete alebo napájania hľadajte Wake on LAN alebo „Wake on network“. Niektoré modely túto možnosť nemajú. Viac na stránke [Aplikácia ovládač Android TV](@android).'),
      ('Staršie televízory Philips bez Androidu', 'Televízory Philips z rokov 2011 až 2015, ktoré nepoužívajú Android, sú v Mando TV podporované v beta verzii. Je to novinka a nevyžaduje párovací kód.'),
      ('Philips s Titan OS', 'Titan OS je iný systém, ktorý Mando TV dnes neovláda, a radšej to povieme jasne. Novšie modely Philips bez Androidu tiež nie sú pokryté.'),
      ('Zadarmo a Pro', 'Ovládač si môžete stiahnuť a používať zadarmo, bez reklám a bez predplatného. Mando TV Pro je voliteľný jednorazový nákup doplnkov.'),
    ],
    marca=None,
    faq=[
      ('Funguje Mando TV s televízormi Philips?', 'S televízormi Philips, ktoré používajú Roku TV, Google TV alebo Android TV, áno, a v beta verzii s televízormi Philips z rokov 2011 až 2015 bez Androidu. Modely s Titan OS nie sú podporované.'),
      ('Ovláda Mando TV Ambilight?', 'Mando TV je ovládač: odosiela tlačidlá, takže sa šípkami a OK dostanete k nastaveniam Ambilight. Samostatné ovládanie Ambilight neexistuje.'),
      ('Potrebujem účet Philips alebo Google?', 'Nie. Mando TV sa pripája cez vašu domácu sieť Wi-Fi a nevyžaduje účet.'),
    ]),
]
OTRAS_GUIAS += [
  ('no-sub', 'Aplikácia ovládač bez predplatného a bez reklám'),
  ('roku-app-alt', 'Alternatíva k aplikácii Roku: jedna pre všetky televízory'),
  ('lg-thinq', 'Alternatíva k aplikácii LG ThinQ pre váš televízor LG'),
  ('smartthings', 'Alternatíva k SmartThings pre televízory Samsung'),
  ('googletv-alt', 'Alternatíva k ovládaču Google TV v mobile'),
  ('windows', 'Aplikácia ovládač pre počítač s Windowsom'),
  ('iphone', 'Aplikácia ovládač pre iPhone: jedna pre všetky televízory'),
  ('firetv', 'Ovládač Fire TV pre váš mobil alebo počítač'),
  ('firetv-lost', 'Stratený ovládač Fire TV: použite mobil'),
  ('turn-on', 'Ako zapnúť televízor bez ovládača'),
  ('sony', 'Ako ovládať televízor Sony mobilom'),
  ('tcl', 'Ako ovládať televízor TCL mobilom'),
  ('hisense', 'Aplikácia ovládač Hisense: čo funguje a čo nie'),
  ('philips', 'Ako ovládať televízor Philips mobilom'),
]
# <<< guías traídas del inglés
