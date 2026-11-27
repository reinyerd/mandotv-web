# Textos en neerlandés (je) de mandotv.app. Los usa generar_idiomas.py. Escritos para las búsquedas de los Países Bajos y Bélgica.
# Las claves de las páginas (lg, lost-tv, ...) y sus rutas están en idiomas_sitio.py.
# Los nombres de menús de cada marca (LG, Samsung, Roku, Android TV, iPhone) son los mismos que usa la app en neerlandés
# (lib/l10n/app_nl.arb del proyecto de la app).

UI = dict(
  locale='nl_NL',
  aria_home='Mando TV, startpagina', aria_main='Hoofdmenu', nav_que='Functies', nav_ayuda='Help', nav_contacto='Contact',
  asunto='Hallo%20Mando%20TV', inicio='Startpagina', privacidad='Privacy', aria_pie='Voetgedeelte', aria_ruta='Kruimelpad',
  aria_marcas='Merken en gidsen', hecho='Gemaakt in Chili',
  aviso='Mando TV is een onafhankelijke app. De app is niet verbonden met de genoemde tv-merken, Google, Amazon, Apple of Roku en wordt niet door hen gesteund. De merken zijn eigendom van hun houders en worden alleen genoemd om de compatibiliteit aan te geven. Android TV en Google TV zijn merken van Google LLC. Apple TV is een merk van Apple Inc.',
  bajar='Gratis downloaden', descarga='Download in de', anticipada='Vroege toegang op',
  apple_aria='Mando TV gratis downloaden in de App Store', ms_aria='Mando TV gratis downloaden in de Microsoft Store',
  gp_aria='Vroege toegang tot Mando TV op Google Play voor Android', aria_desc='Mando TV downloaden',
  b_como_btn='Zo maak je verbinding', b_tiendas_label='Beschikbaar in de stores',
  b_nota='iPhone, iPad, Mac, Android en Windows. Gratis download, zonder advertenties. Pro is een eenmalige aankoop, zonder abonnement.',
  b_compat='Compatibele tv’s', b_otras='Andere merken', b_otras_p='Mando TV bedient al deze merken met dezelfde app:',
  g_guias='Gidsen', g_ver='Bekijk de stappen', g_pasos='Stap voor stap', g_hazlo='Zo doe je het met Mando TV',
  g_tiendas='Mando TV is een universele afstandsbediening voor je tv. Download de app gratis, zonder advertenties en zonder account. Pro is een optionele eenmalige aankoop, zonder abonnement. Voor iPhone, iPad, Windows en Android:',
  g_nota='Android: gratis vroege toegang op Google Play. <a href="{enlace}">Doe in twee stappen mee</a> en help ons de store te bereiken.',
  g_mas_pagina='Meer details vind je op de pagina {enlace}.', g_mas_marca='Meer details per merk:',
  g_faq='Veelgestelde vragen', g_mas='Meer gidsen', g_todas='Alle gidsen', g_ayuda='Help en support',
  g_idiomas='Deze gids in andere talen',
)

# Pie de página y listas de marcas/guías: (clave, texto)
PIE = [
  ('samsung', 'Samsung afstandsbediening'),
  ('lg', 'LG afstandsbediening'),
  ('roku', 'Roku afstandsbediening'),
  ('android', 'Android TV afstandsbediening'),
  ('guias', 'Alle gidsen'),
  ('lost-tv', 'Afstandsbediening kwijt'),
  ('lost-lg', 'LG afstandsbediening kwijt'),
  ('lg-on', 'LG tv aanzetten met je telefoon'),
  ('hdmi', 'HDMI-ingang wisselen zonder afstandsbediening'),
  ('androidtv', 'Android TV zonder afstandsbediening'),
  ('console', 'Tv en HDMI van spelconsole zonder afstandsbediening'),
  ('samsung-lost', 'Samsung tv zonder afstandsbediening'),
  ('roku-lost', 'Roku afstandsbediening kwijt'),
  ('roku-403', 'Roku app werkt niet'),
  ('androidtv-code', 'Android TV koppelcode'),
  ('not-found', 'Telefoon vindt de tv niet'),
  ('wifi', 'Telefoon als afstandsbediening via wifi'),
  ('pc', 'Tv bedienen met je pc'),
]
NOMBRE_OTRA = {'lg': 'LG afstandsbediening-app', 'samsung': 'Samsung afstandsbediening-app', 'roku': 'Roku afstandsbediening-app',
               'android': 'Android TV en Google TV afstandsbediening-app'}
PAGINA_MARCA = {'lg': 'LG afstandsbediening-app', 'samsung': 'Samsung afstandsbediening-app', 'roku': 'Roku afstandsbediening-app',
                'android': 'Android TV afstandsbediening-app'}

OTRAS_GUIAS = [
  ('lg-on', 'LG tv aanzetten met je telefoon'),
  ('lost-tv', 'Afstandsbediening kwijt: dit kun je doen'),
  ('lost-lg', 'LG afstandsbediening kwijt: zo gebruik je je telefoon'),
  ('hdmi', 'HDMI-ingang van de tv wisselen zonder afstandsbediening'),
  ('androidtv', 'Android TV zonder afstandsbediening: zo gebruik je je telefoon'),
  ('console', 'Tv aanzetten en naar de HDMI van je spelconsole wisselen, zonder afstandsbediening'),
  ('samsung-lost', 'Samsung tv zonder originele afstandsbediening: zo gebruik je je telefoon'),
  ('roku-lost', 'Roku afstandsbediening kwijt: zo gebruik je je telefoon'),
  ('roku-403', 'Roku app werkt niet: fout 403 oplossen'),
  ('androidtv-code', 'Android TV vraagt om een koppelcode: dit moet je doen'),
  ('not-found', 'Je telefoon vindt de tv niet: dit kun je controleren'),
  ('wifi', 'Zo gebruik je je telefoon via wifi als afstandsbediening'),
  ('pc', 'Zo bedien je je tv met een Windows-pc'),
]

INDICE = dict(
  titulo='Gidsen: tv bedienen met je telefoon | Mando TV',
  desc='Gidsen stap voor stap: telefoon of pc als afstandsbediening gebruiken, tv aanzetten, HDMI wisselen en problemen met Samsung, LG en Roku oplossen.',
  h1='Gidsen: je telefoon als afstandsbediening gebruiken',
  intro='Eenvoudige stappen om de afstandsbediening van je Samsung-, LG-, Roku- of Android TV-tv met Mando TV te koppelen, de tv aan te zetten en problemen op te lossen.',
  h2_guias='Alle gidsen', h2_marcas='Afstandsbediening-app per merk',
  marcas_extra=[('sony', 'Sony-afstandsbediening'), ('philips', 'Philips-afstandsbediening')],
)

MARCAS = [
  dict(clave='lg', color='#e0457b', corto='LG',
    titulo='LG tv afstandsbediening app voor je telefoon, gratis | Mando TV',
    desc='Je telefoon of pc als LG tv afstandsbediening voor webOS, via wifi. Toetsen, toetsenbord, apps, ingangen en aanzetten gratis; aanwijzer met Pro.',
    h1='LG tv afstandsbediening als app voor je telefoon',
    intro='Mando TV is een afstandsbediening-app voor LG-tv’s: de app maakt van je telefoon of computer via het wifi-netwerk thuis de afstandsbediening van je LG Smart-tv met webOS. Handig als je de afstandsbediening kwijt bent, de batterijen leeg zijn of je gewoon sneller wilt typen.',
    compat='LG Smart-tv’s met webOS (de meeste LG Smart-tv-modellen sinds 2014). Werkt met LED-, NanoCell-, QNED- en OLED-tv’s. Oudere LG Smart-tv’s met NetCast (2011 tot 2014, van voor webOS) worden nieuw in de bèta ondersteund: ze koppelen met de sleutel van 6 cijfers die de tv toont.',
    h2=dict(funciones='Dit kun je doen met je LG-tv', como='Zo verbind je je LG-tv met Mando TV',
            encender='LG-tv aanzetten met je telefoon', preguntas='Vragen over LG', guias='Gidsen voor LG'),
    funciones=[
      ('Alle toetsen', 'Richtingstoetsen, OK, Terug, Start, volume, zenders, dempen en afspelen.'),
      ('Aanwijzer zoals bij de Magic Remote (Pro)', 'Beweeg de pijl met je vinger over het scherm, precies zoals met de LG Magic Remote.'),
      ('Twee toetsenborden', 'Typ in het zoeken van de tv en in de meeste apps met het toetsenbord van je telefoon. Met het YouTube-toetsenbord (Pro) typ of zeg je wat je wilt kijken en YouTube opent op de tv met de resultaten.'),
      ('Apps en ingangen', 'Open je apps en wissel naar HDMI, live-tv, AirPlay of Screen Share.'),
      ('Geluidsuitvoer (Pro)', 'Wissel tussen de speakers van de tv en je soundbar.'),
      ('Tv aanzetten', 'Staat hij uit, dan zet Mando TV hem via het netwerk aan en maakt vanzelf verbinding.'),
    ],
    pasos=[
      'Zet je telefoon en tv op hetzelfde wifi-netwerk.',
      'Open Mando TV: je LG-tv verschijnt vanzelf in de lijst. Tik erop.',
      'Op de tv verschijnt een melding die om toestemming vraagt. Bevestig die met je gewone afstandsbediening (alleen de eerste keer).',
    ],
    encender='Open op de LG-tv Instellingen en zoek naar “Tv aanzetten met mobiele telefoon” (onder Algemeen > Apparaten > Externe apparaten, bij oudere modellen onder Verbinding > Beheer van mobiele verbindingen). Zet “Via wifi aanzetten” aan. Staat er “Quick Start+”, zet die dan ook aan. Daarna vraagt de app, als je de uitgeschakelde tv in Mando TV aantikt, of ze hem moet aanzetten, en maakt vanzelf verbinding.',
    faq=[
      ('Heb ik de Magic Remote nodig om Mando TV te gebruiken?', 'Alleen de eerste keer, om de melding op het scherm te bevestigen. Daarna is je telefoon genoeg.'),
      ('Vervangt Mando TV de LG ThinQ app?', 'Om de tv te bedienen wel: je hebt geen LG-account nodig en hoeft de tv niet te registreren. Mando TV maakt rechtstreeks verbinding via je wifi.'),
      ('Kan ik mijn LG-tv met mijn telefoon aanzetten?', 'Ja, als je op de tv “Tv aanzetten met mobiele telefoon” hebt aangezet en één keer verbinding hebt gemaakt terwijl de tv aanstond.'),
      ('Werkt het met oudere LG-tv’s van voor webOS?', 'In de bèta wel, met LG NetCast Smart-tv’s van 2011 tot 2014. Ze koppelen met de sleutel van 6 cijfers die de tv toont. De functie is nieuw en kan nog kleine haperingen hebben.'),
    ],
    guias=[('lg-on', 'Zo zet je een LG-tv aan met je telefoon'),
           ('lost-lg', 'LG afstandsbediening kwijt: zo gebruik je je telefoon'),
           ('hdmi', 'HDMI-ingang van de tv wisselen zonder afstandsbediening'),
           ('guias', 'Alle gidsen om de tv met je telefoon te bedienen')]),
  dict(clave='samsung', color='#3d7bff', corto='Samsung',
    titulo='Samsung tv afstandsbediening app voor je telefoon | Mando TV',
    desc='Je telefoon of pc als Samsung tv afstandsbediening voor Tizen, via wifi. Toetsen, toetsenbord, apps en aanzetten gratis; touchpad met Pro. Zonder advertenties.',
    h1='Samsung tv afstandsbediening als app voor je telefoon',
    intro='Mando TV is een afstandsbediening-app voor Samsung-tv’s: de app maakt van je telefoon of computer via het wifi-netwerk thuis de afstandsbediening van je Samsung Smart-tv. Je hebt geen Samsung-account nodig en hoeft de tv niet te registreren.',
    compat='Samsung Smart-tv’s met Tizen, bouwjaar 2016 en nieuwer (series zoals Crystal UHD, QLED, Neo QLED, The Frame en OLED).',
    h2=dict(funciones='Dit kun je doen met je Samsung-tv', como='Zo verbind je je Samsung-tv met Mando TV',
            encender='Samsung-tv aanzetten met je telefoon', preguntas='Vragen over Samsung', guias='Gidsen voor Samsung'),
    funciones=[
      ('Alle toetsen', 'Richtingstoetsen, OK, Terug, Start, volume, zenders, dempen en bron.'),
      ('Touchpad (Pro)', 'Veeg met je vinger door de menu’s zonder naar de pijltoetsen te zoeken.'),
      ('Twee toetsenborden', 'Typ in het zoeken van de tv en in de meeste apps met het toetsenbord van je telefoon. Met het YouTube-toetsenbord (Pro) typ of zeg je wat je wilt kijken en YouTube opent op de tv met de resultaten.'),
      ('Apps', 'Open Netflix, YouTube, Prime Video en je andere apps met één tik.'),
      ('Tv aanzetten', 'Staat hij uit, dan zet Mando TV hem via het netwerk aan en maakt vanzelf verbinding.'),
      ('Zonder account', 'De verbinding loopt rechtstreeks via je wifi, zonder omweg via internet.'),
    ],
    pasos=[
      'Zet je telefoon en tv op hetzelfde wifi-netwerk.',
      'Open Mando TV: je Samsung-tv verschijnt vanzelf in de lijst. Tik erop.',
      'De tv vraagt of je de verbinding toestaat. Kies met de afstandsbediening “Toestaan” (alleen de eerste keer).',
    ],
    encender='Zet op de Samsung-tv bij Instellingen > Algemeen > Netwerk > Expertinstellingen de optie “Aan met mobiele telefoon” aan. Daarna vraagt de app, als je de uitgeschakelde tv in Mando TV aantikt, of ze hem moet aanzetten, en maakt vanzelf verbinding.',
    faq=[
      ('Ik heb de toestemming per ongeluk geweigerd. Wat nu?', 'Ga op de tv naar Instellingen > Algemeen > Extern apparaatbeheer > Apparaatverbindingsbeheer en zet Mando TV op toegestaan.'),
      ('Vervangt Mando TV SmartThings?', 'Om de tv te bedienen wel, en zonder Samsung-account. Mando TV maakt rechtstreeks verbinding via je wifi.'),
      ('Werkt het met oudere Samsung-tv’s?', 'Het werkt met Samsung-tv’s met Tizen, bouwjaar 2016 en nieuwer. Eerdere modellen gebruiken een ander systeem dat we nog niet ondersteunen.'),
    ],
    guias=[('samsung-lost', 'Samsung tv zonder originele afstandsbediening: zo gebruik je je telefoon'),
           ('smartthings', 'SmartThings-alternatief'),
           ('turn-on', 'Tv aanzetten zonder afstandsbediening'),
           ('hdmi', 'HDMI-ingang van de tv wisselen zonder afstandsbediening'),
           ('guias', 'Alle gidsen om de tv met je telefoon te bedienen')]),
  dict(clave='roku', color='#a77bff', corto='Roku',
    titulo='Roku afstandsbediening app voor je telefoon, gratis | Mando TV',
    desc='Je telefoon of pc als Roku afstandsbediening voor Roku TV en Roku-spelers, via wifi. Toetsen, toetsenbord, kanalen, ingangen en aanzetten gratis.',
    h1='Roku afstandsbediening als app voor je telefoon',
    intro='Mando TV is een afstandsbediening-app voor Roku: de app maakt van je telefoon of computer via het wifi-netwerk thuis de afstandsbediening van je Roku. Ze werkt met Roku TV-toestellen en met Roku-spelers die je op de HDMI-poort aansluit.',
    compat='Roku TV-toestellen (TCL, Hisense, Philips, Sharp, JVC en andere) en Roku-spelers (Express, Streaming Stick, Ultra).',
    h2=dict(funciones='Dit kun je doen met je Roku', como='Zo verbind je je Roku met Mando TV',
            encender='Roku aanzetten met je telefoon', preguntas='Vragen over Roku', guias='Gidsen voor Roku'),
    funciones=[
      ('Alle toetsen', 'Richtingstoetsen, OK, Terug, Start, volume, dempen, opnieuw afspelen en afspelen.'),
      ('Twee toetsenborden', 'Typ in het zoeken van Roku en in kanalen die het toestaan met het toetsenbord van je telefoon. Met het YouTube-toetsenbord (Pro) typ of zeg je wat je wilt kijken en YouTube opent op de tv met de resultaten.'),
      ('Kanalen', 'Open Netflix, YouTube en je andere Roku-kanalen met één tik.'),
      ('Ingangen', 'Wissel bij een Roku TV in de app naar HDMI, antenne of AV.'),
      ('Tv aanzetten', 'Bij Roku TV-toestellen met snelle start zet Mando TV ze vanaf je telefoon aan.'),
      ('Zonder koppelen', 'Roku vraagt niet om een code: tik in de lijst op je Roku en je bent verbonden.'),
      ('Afstandsbediening laten overgaan', 'Heeft je Roku-afstandsbediening een speaker, zoals de Roku Voice Remote Pro, dan laat Mando TV hem overgaan zodat je hem kunt vinden. Gratis, de Roku moet aanstaan.'),
    ],
    pasos=[
      'Zet je telefoon en Roku op hetzelfde wifi-netwerk.',
      'Open Mando TV: je Roku verschijnt vanzelf in de lijst. Tik erop.',
      'Lukt de verbinding niet, ga dan op de Roku naar Instellingen > Systeem > Geavanceerde systeeminstellingen > Bediening door mobiele apps en zet de netwerktoegang op Standaard of Permissief (zet bij nieuwere Roku-software “Bediening door mobiele apps” op Ingeschakeld).',
    ],
    encender='Zet bij Roku TV-toestellen onder Instellingen > Systeem > Stroom de optie “Snelle tv-start” aan. Roku-spelers die op een andere tv zijn aangesloten, kun je zo niet aanzetten. Daarna vraagt de app, als je de uitgeschakelde tv in Mando TV aantikt, of ze hem moet aanzetten, en maakt vanzelf verbinding.',
    faq=[
      ('Werkt het met de Roku Express of de Streaming Stick?', 'Ja. Alle Roku-spelers en Roku TV-toestellen worden op dezelfde manier bediend.'),
      ('Mando TV vindt mijn Roku niet. Wat nu?', 'Controleer of beide op hetzelfde wifi-netwerk zitten en of “Bediening door mobiele apps” op de Roku niet is uitgezet. Je kunt hem ook toevoegen via zijn IP-adres.'),
      ('Heb ik een Roku-account nodig?', 'Nee. Mando TV maakt rechtstreeks verbinding via je wifi.'),
    ],
    guias=[('roku-403', 'Roku app werkt niet (fout 403)'),
           ('roku-lost', 'Roku afstandsbediening kwijt: zo gebruik je je telefoon'),
           ('tcl', 'TCL-afstandsbediening'),
           ('hisense', 'Hisense-afstandsbediening'),
           ('philips', 'Philips-afstandsbediening'),
           ('guias', 'Alle gidsen om de tv met je telefoon te bedienen')]),
  dict(clave='android', color='#2fbf8f', corto='Android TV en Google TV',
    titulo='Google TV en Android TV afstandsbediening-app | Mando TV',
    desc='Google TV en Android TV afstandsbediening (Sony, TCL, Hisense, Xiaomi) op je telefoon of pc via wifi. Toetsen, apps en aanzetten gratis; touchpad met Pro.',
    h1='Google TV en Android TV afstandsbediening als app voor je telefoon',
    intro='Mando TV is een afstandsbediening-app voor Android TV: de app maakt van je telefoon of computer via het wifi-netwerk thuis de afstandsbediening van je Android TV- of Google TV-tv. Ze werkt ook vanaf de iPhone en vanaf Windows.',
    compat='Tv’s met Google TV of Android TV van Sony, Philips, TCL, Hisense, Sharp, Xiaomi, Toshiba, Panasonic, Haier, Skyworth, JVC, Thomson, Motorola, OnePlus, iFFALCON, Kogan, Vu en andere merken, plus Chromecast met Google TV, Google TV Streamer, onn. en Nvidia Shield. Sommige van deze merken verkopen ook modellen met een ander systeem: toont je tv het startscherm van Google TV of heeft hij de Google Play Store, dan bedient Mando TV hem.',
    h2=dict(funciones='Dit kun je doen met je Android TV', como='Zo verbind je je Android TV met Mando TV',
            encender='Android TV aanzetten met je telefoon', preguntas='Vragen over Android TV', guias='Gidsen voor Android TV'),
    funciones=[
      ('Alle toetsen', 'Richtingstoetsen, OK, Terug, Start, volume, dempen en afspelen.'),
      ('Touchpad (Pro)', 'Veeg met je vinger om snel door de menu’s van Google TV te navigeren.'),
      ('Twee toetsenborden', 'Typ in het zoeken van de tv en in de meeste apps met het toetsenbord van je telefoon. Met het YouTube-toetsenbord (Pro) typ of zeg je wat je wilt kijken en YouTube opent op de tv met de resultaten.'),
      ('Apps', 'Open YouTube, Netflix, Disney+ en je andere apps met één tik.'),
      ('Tv aanzetten', 'Bij modellen met aanzetten via het netwerk zet Mando TV de tv aan en maakt vanzelf verbinding.'),
      ('iPhone, Android en pc', 'Het werkt op elke telefoon en elke computer hetzelfde.'),
    ],
    pasos=[
      'Zet je telefoon en tv op hetzelfde wifi-netwerk.',
      'Open Mando TV: je Android TV verschijnt vanzelf in de lijst. Tik erop.',
      'De tv toont een code van 6 tekens. Voer die in bij Mando TV (alleen de eerste keer).',
    ],
    encender='Dat hangt af van de fabrikant. Zoek in de netwerk- of stroominstellingen naar “Wake on LAN”, “Inschakelen via netwerk”, “Netwerk-stand-by” of “Remote start”. Sommige modellen hebben deze optie niet. Daarna vraagt de app, als je de uitgeschakelde tv in Mando TV aantikt, of ze hem moet aanzetten, en maakt vanzelf verbinding.',
    faq=[
      ('Werkt het met Chromecast met Google TV?', 'Ja, het koppelen gaat met de code van 6 tekens die op het scherm verschijnt.'),
      ('Wat is het verschil met de Google TV-app?', 'Mando TV heeft geen Google-account nodig, werkt ook op Windows en bedient tv’s van LG, Samsung en Roku met dezelfde app.'),
      ('De code verschijnt niet op het scherm. Wat nu?', 'Sluit Mando TV, open de app opnieuw en tik nogmaals op de tv. Controleer of de tv niet in een diepe energiespaarstand staat.'),
    ],
    guias=[('androidtv-code', 'Android TV vraagt om een koppelcode: dit moet je doen'),
           ('androidtv', 'Android TV zonder afstandsbediening: zo gebruik je je telefoon'),
           ('googletv-alt', 'Alternatief voor de Google TV-afstandsbediening'),
           ('sony', 'Sony-afstandsbediening'),
           ('tcl', 'TCL-afstandsbediening'),
           ('hisense', 'Hisense-afstandsbediening'),
           ('philips', 'Philips-afstandsbediening'),
           ('guias', 'Alle gidsen om de tv met je telefoon te bedienen')]),
]

GUIAS = [
  dict(clave='lost-tv', corto='Afstandsbediening kwijt',
    titulo='Afstandsbediening kwijt? Bedien je tv met je telefoon',
    desc='Afstandsbediening kwijt? Zet de tv aan met de knop en gebruik je telefoon als afstandsbediening. Stappen voor LG, Samsung, Roku en Android TV.',
    h1='Afstandsbediening kwijt? Dit kun je nu doen',
    intro='Een kwijtgeraakte afstandsbediening komt in elk huishouden voor: hij is precies weg als je iets wilt kijken. Het goede nieuws: je telefoon kan via het wifi-netwerk thuis de afstandsbediening vervangen. Hier zie je wat je stap voor stap kunt doen.',
    pasos=[
      'Zet de tv aan met de knop op het toestel zelf. Die zit bijna altijd onderaan in het midden of aan de achterkant bij een hoek. Soms is het één knop, soms een klein joystickje.',
      'Zet je telefoon op hetzelfde wifi-netwerk als de tv.',
      'Download Mando TV, dat gratis is en geen account vraagt, en open de app. Je tv verschijnt vanzelf in de lijst. Tik erop.',
      'Bevestig de verbinding voor jouw merk. Bij LG en Samsung toont de tv een melding: bevestig die met de knop of de joystick op de tv zelf. Bij Android TV en Google TV voer je een code van 6 tekens in die op het scherm verschijnt. Roku vraagt nergens om.',
      'Klaar. Richtingstoetsen, OK, Terug, Start, volume, zenders en toetsenbord zijn gratis.',
      'Voor de volgende keer: zet in de instellingen van de tv het aanzetten via het netwerk aan (de gids voor jouw merk vind je hieronder). Dan kun je de tv vanaf je telefoon aanzetten zonder hem aan te raken.',
    ],
    extra=[
      ('Kies de gids voor jouw merk', 'LG: [LG afstandsbediening kwijt](@lost-lg). Android TV en Google TV: [Android TV zonder afstandsbediening](@androidtv). Samsung: [Samsung tv zonder afstandsbediening](@samsung-lost). Roku: [Roku afstandsbediening kwijt](@roku-lost).'),
      ('Als de tv zich niet laat aanzetten met de knop', 'Controleer voordat je een andere afstandsbediening zoekt of de kabel goed vastzit en het stopcontact stroom heeft. Doet de knop op de tv niets, dan ligt het probleem bij de tv en niet bij de afstandsbediening.'),
      ('Als de afstandsbediening gewoon niet meer werkt', 'Probeer nieuwe batterijen. Of hij nog een signaal uitzendt, kun je controleren door hem op de camera van je telefoon te richten en een toets in te drukken: op veel telefoons zie je dan een paars licht op het scherm. Zie je het licht en reageert de tv niet, dan zit de sensor van de tv misschien afgedekt.'),
      ('Als je van router bent veranderd en de tv geen wifi meer heeft', 'Zonder afstandsbediening is het lastiger om de tv met het nieuwe netwerk te verbinden. Het makkelijkst is de tv met een netwerkkabel op de router aan te sluiten. Je kunt ook een wifi-netwerk met dezelfde naam en hetzelfde wachtwoord als eerst instellen: de tv maakt er meestal vanzelf verbinding mee.'),
      ('Wat gratis is en wat Pro', 'De tv aan- en uitzetten, richtingstoetsen, OK, volume, zenders, cijfertoetsen, toetsenbord, apps openen en van ingang wisselen zijn gratis. Het touchpad, spraak en routines horen bij Mando TV Pro, een eenmalige aankoop zonder abonnement.'),
    ],
    marca=None,
    faq=[
      ('Kan ik de tv met mijn telefoon aanzetten als ik hem nog nooit heb verbonden?', 'De eerste keer zet je hem aan met de knop op de tv. Nadat je je telefoon hebt verbonden en in de instellingen van de tv het aanzetten via het netwerk hebt aangezet, kun je hem via de app aanzetten.'),
      ('Moet ik een nieuwe afstandsbediening kopen?', 'Niet per se. Met Mando TV heb je toetsen, volume, toetsenbord en aanzetten gratis. Wil je toch liever een echte afstandsbediening, zoek dan op het exacte model van je tv.'),
      ('Werkt het als de tv geen wifi heeft?', 'Meestal niet. Telefoon en tv moeten meestal op hetzelfde wifi-netwerk zitten. De uitzonderingen zijn infrarood op Android-telefoons met een infraroodzender, dat ook tv’s bedient die geen Smart-tv zijn, en Bluetooth in de bèta vanaf Android 9, dat zonder wifi werkt met Google TV, Android TV en Fire TV.'),
    ]),
  dict(clave='lost-lg', corto='LG afstandsbediening kwijt',
    titulo='LG afstandsbediening kwijt? Gebruik je telefoon',
    desc='Geen LG afstandsbediening? Zet de tv aan met de knop, bevestig de melding en gebruik je telefoon via wifi. Zonder LG-account, zonder advertenties.',
    h1='LG afstandsbediening kwijt? Zo gebruik je je telefoon',
    intro='Als je je LG afstandsbediening kwijt bent of de Magic Remote niet meer werkt, vervangt je telefoon hem via wifi. Dat werkt bij LG-tv’s met webOS, dus bij bijna elke LG Smart-tv sinds 2014. Je hebt geen LG-account en geen ThinQ app nodig.',
    pasos=[
      'Zet de tv aan met de knop onderaan onder het LG-logo of met de knop aan de achterkant. Bij veel modellen is het een joystick: druk erop om het menu te openen en beweeg hem om iets te kiezen.',
      'Zet je telefoon op hetzelfde wifi-netwerk als de tv.',
      'Open Mando TV en tik in de lijst op je LG-tv.',
      'De tv toont een melding die om toestemming vraagt. Bevestig die met de joystick of de knop op de tv. Heb je deze telefoon al eens verbonden, dan vraagt hij het niet nog een keer.',
      'Klaar. Richtingstoetsen, OK, Terug, Start, volume, zenders en toetsenbord zijn gratis. De aanwijzer is een Pro-functie.',
      'Open met de app verbonden met de richtingstoetsen en OK de instellingen en zet “Tv aanzetten met mobiele telefoon” aan. In de gids [LG tv aanzetten met je telefoon](@lg-on) zie je waar je de optie vindt.',
    ],
    extra=[
      ('Als de tv de melding niet toont', 'Misschien is de toestemming al opgeslagen of zit je telefoon op een ander netwerk. Controleer of beide op hetzelfde wifi-netwerk zitten en of de vpn uit staat. Verschijnt de tv niet in de lijst, dan helpt [Je telefoon vindt de tv niet](@not-found) je verder.'),
      ('Als de tv zijn wifi kwijt is', 'Sluit de tv met een netwerkkabel aan op de router, dan gebruikt hij die vanzelf. Of stel een wifi-netwerk in met dezelfde naam en hetzelfde wachtwoord als eerst, want de tv maakt er meestal vanzelf verbinding mee.'),
      ('Als de tv op een andere ingang staat', 'Tik op je telefoon op Ingangen en kies de HDMI-poort. Meer daarover staat in [HDMI-ingang van de tv wisselen zonder afstandsbediening](@hdmi).'),
    ],
    marca='lg',
    faq=[
      ('Heb ik de Magic Remote nodig om Mando TV te gebruiken?', 'Je hebt alleen de eerste keer iets nodig om de melding te bevestigen, en daarvoor is de knop of de joystick op de tv zelf genoeg. Daarna gebruik je alleen je telefoon.'),
      ('Heb ik de LG ThinQ app nodig?', 'Nee. Mando TV maakt rechtstreeks verbinding via je wifi en vraagt geen LG-account.'),
      ('Kan ik mijn LG-tv met mijn telefoon uit- en aanzetten?', 'Uitzetten wel. Om hem aan te zetten moet je op de tv “Tv aanzetten met mobiele telefoon” hebben aangezet en één keer verbinding hebben gemaakt terwijl de tv aanstond.'),
    ]),
  dict(clave='hdmi', corto='HDMI wisselen zonder afstandsbediening',
    titulo='HDMI-ingang wisselen zonder afstandsbediening (Samsung, LG, Roku)',
    desc='HDMI-ingang wisselen zonder afstandsbediening bij Samsung, LG of Roku: met de knop op de tv of met je telefoon. Gratis om te beginnen, zonder advertenties.',
    h1='Zo wissel je de HDMI-ingang van de tv zonder afstandsbediening',
    intro='De spelconsole of streamingspeler is klaar, maar de tv staat op een andere ingang en de afstandsbediening is nergens te vinden. Om de HDMI-ingang zonder afstandsbediening te wisselen heb je twee mogelijkheden: de knop op de tv zelf of je telefoon. Hier de stappen voor Samsung, LG en Roku.',
    pasos=[
      'Probeer eerst het simpelste: zet de console of speler aan. Staat HDMI-CEC aan op de tv (bij Samsung heet het Anynet+, bij LG SIMPLINK), dan wisselt hij vanzelf naar die ingang.',
      'Wisselt hij niet, gebruik dan de knop op de tv zelf, onderaan in het midden of aan de achterkant. Bij veel Samsung- en LG-tv’s is het een joystick en opent hij een menu met Bron of Ingangen.',
      'Kies in dat menu de ingang: HDMI 1, HDMI 2 enzovoort. Het nummer is de poort waarin de kabel zit.',
      'Gebruik je liever je telefoon, zet hem dan op hetzelfde wifi-netwerk, open Mando TV en tik op je tv.',
      'Tik bij LG en Roku op Ingangen en kies de HDMI-poort. Bij Samsung stuurt Ingangen de Bron-toets naar de tv en kies je met de richtingstoetsen en OK.',
      'Je kunt ook met de richtingstoetsen en OK op het startscherm van de tv naar de ingangen gaan. Afhankelijk van merk en bouwjaar heten ze Bron, Aangesloten apparaten of Ingangen. Bij een Roku TV zijn het de HDMI-tegels op het startscherm.',
    ],
    extra=[
      ('Samsung', 'Heeft het menu van de knop op de tv geen item Bron, open dan met je telefoon het menu van het startscherm en zoek links naar Bron of Aangesloten apparaten. Je bedient het met de richtingstoetsen en OK in Mando TV, die gratis zijn.'),
      ('LG', 'Druk op de joystick op de tv en zoek Ingangen. Met je telefoon kun je in Mando TV ook de ingangenlijst openen en de gewenste ingang aantikken.'),
      ('Roku TV', 'Op het startscherm staat voor elke ingang een tegel, bijvoorbeeld HDMI 1 of HDMI 2. Beweeg met de richtingstoetsen en open ze met OK, gratis.'),
      ('Als het een tv met Android TV of Google TV is', 'In Mando TV is de ingangenlijst voor Android TV er nog niet. Gebruik de ingangstoets op de tv zelf of bereik de ingangen met de richtingstoetsen en OK vanaf het startscherm. Heb je geen afstandsbediening en wil je verbinding maken, lees dan [Android TV zonder afstandsbediening](@androidtv).'),
      ('Meer hulp', 'Gaat de tv helemaal niet aan of weet je niet waar je moet beginnen, lees dan [Afstandsbediening kwijt](@lost-tv). Voor gamen op de console bevat de gids [Tv aanzetten en naar de HDMI van je spelconsole wisselen, zonder afstandsbediening](@console) de HDMI-CEC-truc.'),
    ],
    marca=None,
    faq=[
      ('Is het wisselen van de HDMI-ingang gratis?', 'Ja. De ingangenlijst in Mando TV is gratis, net als het aanzetten van de tv en de richtingstoetsen, OK en volume. De ingangen bereik je ook via het menu van de tv.'),
      ('Hoe weet ik welke HDMI-ingang ik nodig heb?', 'Kijk naar de HDMI-poorten van de tv: elke heeft een nummer. Neem de poort waarin de kabel van je console of speler zit.'),
      ('Wat als de tv niet aangaat?', 'Zet hem aan met de knop op het toestel. Heb je hem al eens verbonden en het aanzetten via het netwerk aangezet, dan kun je hem ook met je telefoon aanzetten.'),
    ]),
  dict(clave='androidtv', corto='Android TV zonder afstandsbediening',
    titulo='Android TV zonder afstandsbediening: gebruik je telefoon',
    desc='Geen Android TV- of Google TV-afstandsbediening? Verbind je telefoon met de code van 6 tekens op het scherm. Gratis, zonder account, zonder advertenties.',
    h1='Android TV zonder afstandsbediening: zo gebruik je je telefoon',
    intro='Als je de afstandsbediening van je Android TV of Google TV kwijt bent of de batterijen leeg zijn, vervangt je telefoon hem. Het beste: voor het verbinden heb je de afstandsbediening niet nodig, want de tv toont een code op het scherm en jij typt die op je telefoon in. Het werkt bij tv’s van Sony, Philips, TCL, Hisense, Sharp en Xiaomi met Android TV, bij Chromecast met Google TV en bij Nvidia Shield.',
    pasos=[
      'Zet de tv aan met de knop op het toestel. Die zit bijna altijd onderaan in het midden of aan de achterkant bij een hoek.',
      'Zet je telefoon op hetzelfde wifi-netwerk als de tv.',
      'Download Mando TV, dat gratis is en geen Google-account vraagt, en open de app. Tik in de lijst op je tv.',
      'De tv toont een code van 6 letters en cijfers. Typ die op je telefoon in en tik op Koppelen. Daarvoor heb je de afstandsbediening niet nodig.',
      'Nu kun je richtingstoetsen, OK, Terug, Start, volume, dempen en toetsenbord gebruiken. Ze zijn gratis, net als de lijst met apps. Het touchpad is Pro.',
      'Om de tv de volgende keer vanaf je telefoon aan te zetten, zoek je in de netwerk- of stroominstellingen naar “Wake on LAN”, “Inschakelen via netwerk”, “Netwerk-stand-by” of “Remote start”.',
    ],
    extra=[
      ('Als je tv zich niet vanaf je telefoon laat aanzetten', 'Niet elke Android TV kan via het netwerk worden aangezet; dat hangt af van de fabrikant en het model. Heeft die van jou de functie niet, zet hem dan aan met de knop op de tv en ga op je telefoon verder. Uitzetten kan via de app.'),
      ('Chromecast met Google TV, Google TV Streamer en Shield', 'Ze verbinden op dezelfde manier: hetzelfde wifi-netwerk, het apparaat in de lijst aantikken en de code invoeren. Toont de tv een andere ingang, wissel dan naar de HDMI-poort waarin het apparaat zit, zoals uitgelegd in [HDMI-ingang van de tv wisselen zonder afstandsbediening](@hdmi).'),
      ('Als de code niet verschijnt of als onjuist wordt gemeld', 'Controleer of de tv echt aanstaat en niet in stand-by staat. De code verandert bij elk verzoek: alleen de laatste werkt. Meer details vind je bij [Android TV vraagt om een koppelcode](@androidtv-code).'),
      ('Google-app of Mando TV', 'Google heeft een eigen app waarvoor je een Google-account nodig hebt. Mando TV vraagt geen account, werkt ook op Windows en bedient tv’s van LG, Samsung en Roku met dezelfde app.'),
    ],
    marca='android',
    faq=[
      ('Heb ik de afstandsbediening nodig om mijn telefoon te koppelen?', 'Nee. De code verschijnt op het scherm van de tv en jij typt hem op je telefoon in. Je hoeft alleen de tv aan te zetten, zo nodig met de knop op het toestel.'),
      ('Werkt het met een Hisense?', 'Bij Hisense-tv’s met Android TV of Google TV wel. Hisense-tv’s met een ander systeem zijn niet compatibel.'),
      ('Kan ik typen met het toetsenbord van mijn telefoon?', 'Ja, er zijn er twee. Het gratis toetsenbord typt in het zoekveld en de tekstvelden van de tv en van de meeste apps. YouTube en Netflix accepteren alleen hun eigen toetsenbord op het scherm, dus voor YouTube is er het YouTube-toetsenbord (Pro): typ of zeg wat je wilt kijken en YouTube opent op de tv met de resultaten. Netflix gebruik je met de pijltoetsen en OK.'),
    ]),
  dict(clave='lg-on', corto='LG tv aanzetten met je telefoon',
    titulo='LG tv aanzetten met je telefoon (handleiding)',
    desc='LG tv via wifi aanzetten met je telefoon: zet “Tv aanzetten met mobiele telefoon” aan en gebruik Mando TV. Stap voor stap, gratis.',
    h1='Zo zet je een LG-tv aan met je telefoon',
    intro='Je kunt een LG-tv met je telefoon aanzetten, maar daarvoor moet je eerst een instelling op de tv aanzetten. Daarna zet je telefoon de LG-tv via je wifi aan, helemaal zonder afstandsbediening. Het kost vijf minuten en je doet het maar één keer.',
    pasos=[
      'Zet je telefoon en de LG-tv op hetzelfde wifi-netwerk.',
      'Open op de tv Instellingen en zoek naar “Tv aanzetten met mobiele telefoon”. Je vindt het onder Algemeen > Apparaten > Externe apparaten (bij oudere modellen onder Verbinding > Beheer van mobiele verbindingen).',
      'Zet “Via wifi aanzetten” aan. Is je tv met een netwerkkabel verbonden, zet dan in plaats daarvan de optie voor de kabel aan.',
      'Heeft je tv “Quick Start+”, zet die dan ook aan.',
      'Open met de tv aan Mando TV op je telefoon en tik in de lijst op je LG-tv. Bevestig de melding die op het scherm verschijnt. Zo leert de app hoe ze hem wakker maakt.',
      'Zet de tv uit en probeer het: tik in Mando TV op de tv en de app vraagt of ze hem moet aanzetten.',
    ],
    extra=[
      ('Als hij niet aangaat', 'De tv moet op hetzelfde wifi-netwerk hebben gezeten toen hij werd uitgezet. Controleer of de instelling nog aanstaat en je telefoon op hetzelfde netwerk zit. Ben je van router veranderd, maak dan opnieuw verbinding terwijl de tv aanstaat.'),
    ],
    marca='lg',
    faq=[
      ('Kan ik de LG-tv met mijn telefoon aanzetten als ik hem nooit heb verbonden?', 'Nee. Eerst moet je op de tv “Tv aanzetten met mobiele telefoon” aanzetten en één keer verbinding maken met Mando TV terwijl de tv aanstaat.'),
      ('Heb ik de LG ThinQ app nodig?', 'Nee. Mando TV maakt rechtstreeks verbinding via je wifi en vraagt geen LG-account.'),
      ('Werkt het met mobiele data?', 'Nee. Telefoon en tv moeten op hetzelfde wifi-netwerk zitten.'),
    ]),
  dict(clave='console', corto='Tv en console zonder afstandsbediening',
    titulo='Geen afstandsbediening? Tv aanzetten, HDMI wisselen',
    desc='Releasedag en geen afstandsbediening? Zet de tv aan en wissel met je telefoon naar de HDMI-ingang van je PS5 of Xbox. Gratis, zonder advertenties.',
    h1='Zo zet je de tv aan en wissel je zonder afstandsbediening naar de HDMI-ingang van je spelconsole',
    intro='Releasedag van GTA VI, de console staat klaar en de afstandsbediening is ergens tussen de bankkussens verdwenen. Het gebeurt vaker dan je denkt. Met Mando TV zet je telefoon de tv aan en wisselt via je wifi thuis naar de ingang van je PlayStation of Xbox.',
    pasos=[
      'Zet je telefoon op hetzelfde wifi-netwerk als de tv.',
      'Open Mando TV en tik in de lijst op je tv (Samsung, LG, Roku of Android TV).',
      'Staat de tv uit, tik dan op Aanzetten. Dat werkt als op de tv het aanzetten via het netwerk aanstaat. Heb je dat nooit aangezet, zet de tv dan deze ene keer aan met de knop op het toestel en zet het aan voor de volgende keer.',
      'Zet de console aan. Staat HDMI-CEC aan (zie de gratis truc hieronder), dan wisselt de tv vanzelf naar de ingang van de console.',
      'Wisselt hij niet, tik dan in Mando TV op Ingangen en kies de HDMI-poort waarin de console zit: HDMI 1, HDMI 2 enzovoort.',
      'Voor het volume gebruik je tijdens het gamen de grote toetsen in de app.',
    ],
    extra=[
      ('De gratis truc: laat de console de tv omschakelen', 'De PS5 en de Xbox kunnen de tv aanzetten en meteen bij het opstarten naar hun HDMI-ingang laten springen, dankzij HDMI-CEC. Bij de PS5 vind je het onder Instellingen > Systeem > HDMI > HDMI-apparaatkoppeling inschakelen. Open bij de Xbox Instellingen > Algemeen > Tv- en weergaveopties en zoek de optie voor apparaatbediening. Op de tv heet de functie per merk anders: Anynet+ bij Samsung, SIMPLINK bij LG en BRAVIA Sync of HDMI-bediening bij andere.'),
      ('Als de tv op een ander beeld blijft staan', 'Staat de console aan maar toont de tv nog antenne of een app, dan is hij niet van ingang gewisseld. Tik op je telefoon op Ingangen en kies de HDMI-ingang van de console. Of gebruik de richtingstoetsen en OK om bij de ingangen van de tv te komen, of de knop op de tv zelf, en kies de HDMI-poort. Het nummer is de poort waarin je de kabel van de console hebt gestoken.'),
      ('Als het een Roku TV is', 'De knop op de tv, meestal onderaan in het midden of aan de achterkant, zet hem aan. Vanaf daar doet je telefoon de rest.'),
    ],
    marca=None,
    faq=[
      ('Heeft Mando TV iets met GTA VI te maken?', 'Nee. Mando TV heeft geen enkele band met Rockstar Games of Take-Two. De app helpt je alleen geen speeltijd te verliezen omdat je de afstandsbediening niet kunt vinden.'),
      ('Is het wisselen van de HDMI-ingang gratis?', 'Ja. De ingangenlijst in Mando TV is gratis, net als het aanzetten van de tv en de richtingstoetsen, OK en volume. Je kunt de console de ingang ook zelf laten wisselen met HDMI-CEC.'),
      ('Werkt het met mijn tv?', 'Het werkt met tv’s van Samsung, LG, Roku en Android TV op hetzelfde wifi-netwerk. Is die van jou van een ander merk, dan kan de HDMI-CEC-truc je toch helpen.'),
      ('Kan ik het gebruiken om GTA VI (GTA 6) te spelen op de PS5 of Xbox?', 'Mando TV grijpt niet in op de console of de game. Het zorgt er alleen voor dat de tv aanstaat en op de juiste HDMI-ingang staat, zodat je kunt gaan zitten en spelen.'),
    ]),
  dict(clave='samsung-lost', corto='Samsung tv zonder afstandsbediening',
    titulo='Samsung afstandsbediening kwijt? Gebruik je telefoon',
    desc='Samsung afstandsbediening kwijt of kapot? Gebruik je telefoon via wifi als afstandsbediening voor Tizen-tv’s. Met Mando TV, gratis, geen advertenties.',
    h1='Samsung tv zonder originele afstandsbediening: zo gebruik je je telefoon',
    intro='Als je je Samsung afstandsbediening kwijt bent of hij niet meer werkt, kun je je telefoon via wifi als afstandsbediening gebruiken. Het werkt bij Samsung-tv’s met Tizen, bouwjaar 2016 en nieuwer.',
    pasos=[
      'Zet de tv aan met de knop op het toestel. Bij de meeste modellen zit die onderaan of aan de achterkant, soms als klein joystickje.',
      'Controleer of de tv met je wifi is verbonden en je telefoon op hetzelfde netwerk zit.',
      'Open Mando TV op je telefoon. Je Samsung-tv verschijnt vanzelf in de lijst. Tik erop.',
      'De tv vraagt je de verbinding te bevestigen. Bij de meeste modellen bevestig je die met de knoppen op de tv of met de joystick aan de achterkant.',
      'Klaar, nu kun je je telefoon als afstandsbediening gebruiken. De toetsen, het toetsenbord en de apps zijn gratis; het touchpad is een Pro-functie.',
      'Om de tv de volgende keer vanaf je telefoon aan te zetten, ga je naar Instellingen > Algemeen > Netwerk > Expertinstellingen en zet je “Aan met mobiele telefoon” aan.',
    ],
    extra=[
      ('Als de tv niet om toestemming vraagt', 'Misschien is de toestemming al opgeslagen of zit de tv op een ander wifi-netwerk. Sluit Mando TV en open de app opnieuw met de tv aan. Is de tv ouder dan 2016, dan gebruikt hij een ander systeem dat nog niet wordt ondersteund.'),
      ('Als je de toestemming per ongeluk hebt geweigerd', 'Ga op de tv naar Instellingen > Algemeen > Extern apparaatbeheer > Apparaatverbindingsbeheer en zet Mando TV op toegestaan. Vindt je telefoon de tv dan nog steeds niet, lees dan [Je telefoon vindt de tv niet](@not-found).'),
    ],
    marca='samsung',
    faq=[
      ('Hoe bevestig ik de verbinding als ik geen afstandsbediening heb?', 'Bij de meeste modellen bevestig je die met de knoppen op de tv of met de joystick aan de achterkant. Heeft jouw model geen knoppen, schrijf dan naar hola@mandotv.app en we helpen je.'),
      ('Vraagt Mando TV een Samsung-account?', 'Nee. De verbinding loopt rechtstreeks via je wifi, zonder Samsung-account.'),
      ('Werkt het met mijn oudere Samsung-tv?', 'Het werkt met Samsung-tv’s met Tizen, bouwjaar 2016 en nieuwer.'),
    ]),
  dict(clave='wifi', corto='Telefoon als afstandsbediening via wifi',
    titulo='Telefoon als afstandsbediening gebruiken: tv bedienen via wifi',
    desc='Verbind je telefoon via wifi met de tv en gebruik hem als afstandsbediening bij Samsung, LG, Roku en Google TV. Stappen per merk met Mando TV. Gratis.',
    h1='Zo verbind je je telefoon via wifi als afstandsbediening met de tv',
    intro='Je hebt alleen je telefoon en je tv op hetzelfde wifi-netwerk nodig, plus een afstandsbediening-app. Mando TV vindt je tv vanzelf en werkt met Samsung, LG, Roku, Google TV en Android TV.',
    pasos=[
      'Zet je telefoon en tv op hetzelfde wifi-netwerk.',
      'Open Mando TV. Je tv verschijnt vanzelf in de lijst. Tik erop.',
      'Bevestig de verbinding voor jouw merk (de details staan hieronder).',
      'Bedien de tv met de toetsen of met het toetsenbord van je telefoon. Het touchpad is een Pro-functie.',
    ],
    extra=[
      ('Samsung', 'De tv vraagt of je de verbinding toestaat. Bevestig die de eerste keer op het scherm. Het werkt met Tizen, bouwjaar 2016 en nieuwer. Om hem vanaf je telefoon aan te zetten, zet je onder Instellingen > Algemeen > Netwerk > Expertinstellingen de optie “Aan met mobiele telefoon” aan.'),
      ('LG', 'De tv toont een melding die om toestemming vraagt. Bevestig die de eerste keer. Om hem vanaf je telefoon aan te zetten, zoek je in de instellingen naar “Tv aanzetten met mobiele telefoon” en zet je “Via wifi aanzetten” aan.'),
      ('Roku', 'Roku vraagt geen koppeling: tik in de lijst op je Roku en je bent verbonden. Om hem aan te zetten, zet je onder Instellingen > Systeem > Stroom de optie “Snelle tv-start” aan.'),
      ('Google TV en Android TV', 'De tv toont een code op het scherm. Voer die de eerste keer in bij Mando TV. Om hem aan te zetten, zoek je in de instellingen naar “Wake on LAN”, “Inschakelen via netwerk” of “Netwerk-stand-by”.'),
    ],
    marca=None,
    faq=[
      ('Heb ik internet nodig om mijn telefoon als afstandsbediening te gebruiken?', 'Je hebt je telefoon en de tv op hetzelfde wifi-netwerk nodig. Mando TV maakt via dat netwerk rechtstreeks verbinding met je tv.'),
      ('Waarom verschijnt mijn tv niet in de lijst?', 'Controleer of de tv aanstaat en je telefoon niet op mobiele data of een ander wifi-netwerk zit. Sommige routers hebben een gastnetwerk dat apparaten van elkaar scheidt.'),
      ('Kan ik Mando TV gebruiken op de iPhone of op een Android-telefoon?', 'Op iPhone en iPad wel: de app staat al in de App Store. Voor Windows is ze er ook in de Microsoft Store. Android komt binnenkort: je kunt meedoen aan de gratis vroege toegang op Google Play.'),
    ]),
  dict(clave='pc', corto='Tv bedienen met je pc',
    titulo='Tv bedienen met je Windows-pc (gratis)',
    desc='Gebruik je Windows-pc als afstandsbediening voor Samsung, LG, Roku of Google TV via wifi. Toetsen, toetsenbord en apps gratis; pc-sneltoetsen met Pro.',
    h1='Zo bedien je je tv met een Windows-pc',
    intro='Als je de dag achter de computer doorbrengt, hoef je niet naar de afstandsbediening te zoeken: Mando TV voor Windows bedient je Samsung-, LG-, Roku-, Google TV- of Android TV-tv via je wifi-netwerk thuis. Handig om van app te wisselen, het geluid harder te zetten of in YouTube te typen met het pc-toetsenbord.',
    pasos=[
      'Download Mando TV gratis uit de Microsoft Store op je computer met Windows 10 of 11.',
      'Controleer of computer en tv op hetzelfde netwerk zitten (wifi of kabel, maar via dezelfde router).',
      'Open Mando TV: je tv verschijnt vanzelf in de lijst. Tik of klik erop.',
      'Bevestig de eerste keer de verbinding op het scherm van de tv (bij Google TV en Android TV voer je de code in die de tv toont).',
      'Klaar: gebruik de toetsen of het toetsenbord om in het zoekveld van de tv te typen. Het touchpad is een Pro-functie.',
    ],
    extra=[
      ('Sneltoetsen op de pc (Pro)', 'Met Mando TV Pro bedien je de tv met het toetsenbord van je computer: pijltoetsen om te navigeren, Enter voor OK, Backspace of Esc voor Terug, + en - voor het volume, M om te dempen en de spatiebalk voor pauze.'),
      ('Mini-afstandsbediening altijd bovenop (Pro)', 'Houd een klein venster met de afstandsbediening altijd zichtbaar terwijl je werkt of op de pc gamet.'),
      ('Met de tv praten vanaf de pc (Pro)', 'Met Mando TV Pro geef je de tv opdrachten via de microfoon van de pc: “open YouTube”, “zet harder” of “zet over 30 minuten uit”, precies zoals je praat. Op Windows wordt de spraak op de pc zelf herkend: je hebt geen internet nodig, hoeft niets te veranderen in de Windows-instellingen en het werkt in de 6 talen van de app. Wat je zegt, verlaat de pc niet en wordt niet opgeslagen. Alleen bij zeer oude processors valt de app terug op dicteren van Windows. Daarvoor moet online spraakherkenning aanstaan in de privacy-instellingen en moet Nederlands (Nederland) in Windows zijn toegevoegd. Ontbreekt er dan iets, dan meldt de app dat en opent ze de instelling met een knop.'),
    ],
    marca=None,
    faq=[
      ('Heb ik een kabel of Bluetooth nodig om de tv met de pc te bedienen?', 'Nee. Mando TV maakt verbinding via je thuisnetwerk: pc en tv hoeven alleen op dezelfde router te zitten.'),
      ('Werkt het met elke tv?', 'Het werkt met Samsung-tv’s met Tizen (bouwjaar 2016 en nieuwer), LG met webOS, Roku en Google TV of Android TV (Sony, Philips, TCL, Hisense, Sharp, Xiaomi, Toshiba, Panasonic, Haier, Skyworth en andere).'),
      ('Wat kost het?', 'De toetsen, het toetsenbord en het aanzetten via het netwerk zijn gratis en zonder advertenties. Mando TV Pro is een eenmalige aankoop zonder abonnement voor extra’s zoals het touchpad, de pc-sneltoetsen en de mini-afstandsbediening.'),
      ('Waarom verstaat de microfoon me niet op Windows?', 'Controleer of de spraakfunctie actief is (die hoort bij Pro) en of de microfoon van de pc onder Windows werkt. Op bijna alle pc’s wordt de spraak op het apparaat zelf herkend, helemaal zonder internet. Alleen bij zeer oude processors gebruikt de app dicteren van Windows. Controleer dan of online spraakherkenning aanstaat in de privacy-instellingen van Windows en of Windows Nederlands (Nederland) bij de taalinstellingen heeft. Mando TV gebruikt die taal alleen zolang het luistert.'),
    ]),
  dict(clave='roku-403', corto='Roku app werkt niet',
    titulo='Roku app werkt niet? Fout 403 oplossen',
    desc='Telefoon verbonden, maar reageert de Roku niet? Zet “Bediening door mobiele apps” aan in 5 stappen en gebruik je telefoon weer als afstandsbediening.',
    h1='Roku app werkt niet: zo los je het op',
    intro='Als je telefoon de Roku vindt en verbinding maakt, maar geen enkele toets iets doet, ligt het bijna altijd aan een instelling op de Roku zelf die afstandsbediening-apps blokkeert. Nieuwere Roku-versies zijn standaard strenger. In het Roku-menu los je het in een minuut op.',
    pasos=[
      'Druk op de Roku op Start en ga naar Instellingen.',
      'Open Systeem en dan Geavanceerde systeeminstellingen.',
      'Ga naar “Bediening door mobiele apps”. Bij sommige modellen heet het “Externe bediening”.',
      'Kies bij “Netwerktoegang” Standaard of Permissief. Is het bij jouw model alleen een schakelaar, laat hem dan op Ingeschakeld staan.',
      'Ga terug naar Mando TV op je telefoon en tik op je Roku. De toetsen reageren nu.',
    ],
    extra=[
      ('Zo herken je of dit jouw probleem is', 'Het teken is duidelijk: je telefoon ziet de Roku in de lijst en maakt verbinding, maar er gebeurt niets als je een toets aantikt. Intern antwoordt de Roku met fout 403, wat “verboden” betekent. Mando TV herkent dat bij het verbinden en toont je precies deze stappen op het scherm.'),
      ('Standaard of Permissief, wat kies ik?', 'Standaard is genoeg: het accepteert opdrachten uit je thuisnetwerk, en dat is wat een afstandsbediening nodig heeft. Permissief is opener en alleen nodig op ongewone netwerken. Staat de optie op Uitgeschakeld (bij nieuwere software Beperkt), dan reageert de Roku niet op apps.'),
      ('Als je de Roku-afstandsbediening niet hebt', 'Staat de instelling op Uitgeschakeld, dan kun je hem alleen met de echte Roku-afstandsbediening veranderen. Leen er een om het één keer te veranderen; daarna kun je alles met je telefoon doen. Lees ook [Roku afstandsbediening kwijt](@roku-lost).'),
    ],
    marca='roku',
    faq=[
      ('Waarom reageert mijn Roku niet meer, terwijl het eerst werkte?', 'Een Roku-update kan deze instelling strenger maken. Het ligt niet aan je telefoon of je wifi: je hoeft alleen de bediening door apps weer toe te staan.'),
      ('Geldt dit voor Roku TV en voor Roku-spelers?', 'Ja. De instelling staat bij Roku-spelers en bij Roku TV-toestellen in hetzelfde menu.'),
      ('Is het veilig om de instelling op Standaard te laten?', 'Ja. Ze accepteert alleen opdrachten van apparaten in je thuisnetwerk.'),
    ]),
  dict(clave='not-found', corto='Telefoon vindt de tv niet',
    titulo='Telefoon vindt de tv niet? 6 dingen om te controleren',
    desc='Vindt de afstandsbediening-app je tv niet? Controleer wifi, vpn en toegang tot het lokale netwerk. Voor Samsung, LG, Roku en Android TV.',
    h1='Je telefoon vindt de tv niet: dit kun je controleren',
    intro='Je opent de afstandsbediening-app en de lijst is leeg, of de tv verschijnt maar de verbinding valt weg. Bijna altijd ligt het aan het netwerk en niet aan de tv. Loop deze punten na in volgorde: het eerste lost de meeste gevallen op.',
    pasos=[
      'Kijk op welk wifi-netwerk je telefoon zit en op welk de tv. Het moet hetzelfde netwerk met dezelfde naam zijn. Een gastnetwerk werkt niet, omdat het apparaten van elkaar scheidt.',
      'Zet de vpn op je telefoon uit, als je er een gebruikt. Bij een actieve vpn gaat je telefoon via een ander netwerk het internet op en ziet hij de apparaten bij jou thuis niet, of valt de verbinding na enkele seconden weg.',
      'Zet even de mobiele data uit. Sommige telefoons schakelen bij een zwak signaal vanzelf van wifi naar mobiele data.',
      'Zet de tv aan en wacht tot hij helemaal is opgestart. Een uitgeschakelde tv antwoordt niet op het zoeken.',
      'Controleer bij de iPhone of de app toestemming heeft voor “Lokaal netwerk”: Instellingen > Privacy en beveiliging > Lokaal netwerk.',
      'Verschijnt hij nog steeds niet, voeg hem dan handmatig toe: tik in Mando TV op “Toevoegen via IP” en voer het IP-adres van de tv in.',
    ],
    extra=[
      ('Laat je door de app begeleiden', 'In de lijst met tv’s staat een knop voor het geval je tv niet verschijnt. De app controleert stap voor stap de meest voorkomende oorzaken (hetzelfde wifi-netwerk, vpn, toestemming voor het lokale netwerk en meer) en toont na elke correctie een knop om opnieuw te controleren. De assistent is gratis.'),
      ('Waar je het IP-adres van de tv vindt', 'Het staat in het netwerkmenu van de tv en is per model net anders. Bij LG: Instellingen, Netwerk, Wifi-verbinding, Geavanceerde wifi-instellingen. Bij Samsung: Instellingen, Algemeen, Netwerk, Netwerkstatus, IP-instellingen. Bij Roku: Instellingen, Netwerk, Info. Bij Android TV en Google TV: Instellingen, Netwerk en internet, tik dan op je netwerk. Het is een getal zoals 192.168.1.86.'),
      ('Als hij verschijnt maar de verbinding wegvalt', 'Valt de verbinding na enkele seconden weg, dan ligt de oorzaak meestal bij de telefoon: een vpn, het wisselen naar een ander wifi-netwerk of de energiespaarstand. Zet de vpn uit, blijf op hetzelfde wifi-netwerk en probeer het opnieuw.'),
      ('Wifi met 2,4 en 5 GHz', 'Het maakt niet uit of je telefoon op het 5 GHz-netwerk zit en de tv op het 2,4 GHz-netwerk, zolang ze van dezelfde router komen. Heb je een wifi-versterker en verschijnt de tv toch niet, ga dan met je telefoon dichter bij de hoofdrouter staan en probeer het opnieuw.'),
    ],
    marca=None,
    faq=[
      ('Kan ik de tv met mobiele data bedienen?', 'Nee. Het signaal van de afstandsbediening loopt via je wifi thuis, daarom moeten telefoon en tv op hetzelfde netwerk zitten.'),
      ('Waarom werkt het niet met een actieve vpn?', 'Omdat de vpn al het verkeer van je telefoon via een ander netwerk leidt en de telefoon de apparaten bij jou thuis niet meer ziet. Zet hem uit zolang je de afstandsbediening gebruikt.'),
      ('Werkt het met Bluetooth of infrarood?', 'Bij Smart-tv’s gebruikt Mando TV wifi. Infrarood werkt alleen op Android-telefoons met infraroodzender en is bedoeld voor tv’s die geen Smart-tv zijn. Bluetooth is er in de bèta, gratis en alleen vanaf Android 9: de telefoon maakt verbinding met de tv als Bluetooth-toetsenbord en -afstandsbediening, helemaal zonder wifi. Het werkt met Google TV, Android TV en Fire TV; bij andere merken die Bluetooth-toetsenborden accepteren kan het werken, Roku accepteert ze niet.'),
    ]),
  dict(clave='androidtv-code', corto='Android TV koppelcode',
    titulo='Android TV vraagt om een koppelcode: dit moet je doen',
    desc='Je Android TV of Google TV toont bij het verbinden een code van 6 tekens. Zo voer je hem in en dit doe je als hij niet verschijnt of onjuist is.',
    h1='Android TV vraagt om een koppelcode: dit moet je doen',
    intro='Als je je telefoon voor het eerst met een Android TV of Google TV verbindt, toont de tv een code van 6 tekens op het scherm. Dat is normaal en gebeurt maar één keer: zo weet je zeker dat niemand anders je tv kan bedienen. Hier zie je hoe je hem invoert en wat je doet als hij niet verschijnt.',
    pasos=[
      'Zet de tv aan en laat het startscherm zichtbaar.',
      'Open Mando TV op je telefoon, op hetzelfde wifi-netwerk als de tv, en tik in de lijst op je tv.',
      'Kijk naar het scherm van de tv: er verschijnt een code van 6 letters en cijfers.',
      'Typ hem precies zo op je telefoon in als hij wordt getoond en tik op Koppelen. De letters gaan alleen van A tot F, een rond teken is dus altijd het cijfer nul.',
      'Klaar. De tv onthoudt je telefoon en vraagt niet nog eens om de code.',
    ],
    extra=[
      ('Als de code niet op de tv verschijnt', 'Controleer of de tv echt aanstaat en niet in stand-by staat, en of je telefoon op hetzelfde wifi-netwerk zit. Tik op je telefoon nogmaals op de tv. Verschijnt hij nog steeds niet, start de tv dan opnieuw op: trek de stekker er tien seconden uit, steek hem er weer in en probeer het opnieuw.'),
      ('Als de code als onjuist wordt gemeld', 'De code verandert bij elk verzoek. Heb je lang gedaan of hem twee keer opgevraagd, dan werkt alleen de laatste op het scherm. Tik op je telefoon nogmaals op de tv en voer de nieuwe code in.'),
      ('Als de tv opnieuw om de code vraagt', 'Dat gebeurt als de tv naar de fabrieksinstellingen is teruggezet of als je de app-gegevens op je telefoon wist. Koppel opnieuw, dan is hij opgeslagen. Heb je helemaal geen afstandsbediening, lees dan [Android TV zonder afstandsbediening](@androidtv).'),
    ],
    marca='android',
    faq=[
      ('Welke tv’s gebruiken deze code?', 'Die met Android TV of Google TV: Sony, Philips, TCL, Hisense, Sharp, Xiaomi, Chromecast met Google TV en nog enkele andere.'),
      ('Heb ik een Google-account nodig op mijn telefoon?', 'Nee. De code op het scherm is alles wat je nodig hebt.'),
      ('Is dit veilig?', 'Ja. De code bewijst dat je voor de tv zit: niemand kan koppelen zonder hem op het scherm te zien.'),
    ]),
  dict(clave='roku-lost', corto='Roku afstandsbediening kwijt',
    titulo='Roku afstandsbediening kwijt? Gebruik je telefoon via wifi',
    desc='Roku afstandsbediening kwijt? Je telefoon vervangt hem via wifi. Eenvoudige stappen, ook als je van router bent veranderd en de Roku geen wifi heeft.',
    h1='Roku afstandsbediening kwijt: zo gebruik je je telefoon',
    intro='Als je je Roku-afstandsbediening kwijt bent of hij niet meer werkt, vervangt je telefoon hem, zolang de Roku nog met je wifi is verbonden. En heb je van wifi of router gewisseld, dan is daar ook een uitweg voor.',
    pasos=[
      'Probeer eerst de afstandsbediening te laten overgaan. Heeft je Roku-afstandsbediening een speaker, bijvoorbeeld de Roku Voice Remote Pro, open dan Mando TV, maak verbinding met de Roku en gebruik de optie om de afstandsbediening te laten overgaan, zodat je hem kunt vinden. Dat werkt alleen met Roku-afstandsbedieningen met speaker, en de Roku moet aanstaan.',
      'Zet de tv aan en laat de Roku aangesloten. Je hoeft er niets aan aan te raken.',
      'Zet je telefoon op hetzelfde wifi-netwerk als de Roku.',
      'Open Mando TV. De Roku verschijnt vanzelf in de lijst. Tik erop.',
      'Gebruik richtingstoetsen, OK, Start en Terug zoals bij je gewone afstandsbediening. De Roku vraagt niet om een code.',
      'Doen de toetsen niets, dan blokkeert de Roku de bediening door apps: de gids [Roku app werkt niet](@roku-403) legt uit hoe je die toestaat.',
    ],
    extra=[
      ('Als de Roku geen wifi heeft (van router veranderd of verhuisd)', 'Zonder afstandsbediening kom je niet in het menu om het nieuwe netwerk in te stellen, maar er is een truc: de Roku maakt vanzelf verbinding met een netwerk dat dezelfde naam en hetzelfde wachtwoord heeft als het oude. Stel op een andere telefoon een wifi-hotspot in met precies die naam en dat wachtwoord, verbind je telefoon met Mando TV daarmee, en de Roku verschijnt in de lijst. Ga van daaruit naar Instellingen, Netwerk en verbind hem met het nieuwe wifi-netwerk.'),
      ('Als het een Roku TV is', 'Roku TV-toestellen hebben een knop op het toestel, bijna altijd onderaan in het midden of aan de achterkant, waarmee je de tv aanzet. Dat is genoeg om hem aan te zetten en met je telefoon verder te gaan.'),
      ('Als je liever een andere afstandsbediening koopt', 'Let erop dat hij bij je model past. Kleine Roku-spelers achter de tv hebben een afstandsbediening zonder infrarood nodig, omdat infrarood ze niet bereikt.'),
    ],
    marca='roku',
    faq=[
      ('Kan mijn telefoon de Roku aanzetten?', 'Een aangesloten Roku-speler staat altijd aan. Bij een Roku TV zet Mando TV hem via wifi aan als “Snelle tv-start” aanstaat onder Instellingen > Systeem > Stroom.'),
      ('En het volume?', 'Bij een Roku TV zet je telefoon het volume harder en zachter. Bij een Roku-speler die via HDMI is aangesloten hangt het af van de tv: bij veel werkt het, bij andere niet.'),
      ('Moet ik een account aanmaken?', 'Nee. Mando TV vraagt geen account en bedient ook tv’s van Samsung, LG en Android TV met dezelfde app.'),
    ]),
]

SOPORTE = dict(
  titulo='Help: tv verbinden met Mando TV en aanzetten',
  desc='Zo verbind je de Mando TV afstandsbediening met LG, Samsung, Roku of Android TV, zet je de tv aan vanaf je telefoon en los je problemen op.',
  h1='Help',
  intro='De meest gestelde vragen, in de volgorde van de stappen. Staat de jouwe er niet bij, schrijf ons dan naar <a href="mailto:hola@mandotv.app?subject=Hulp%20bij%20Mando%20TV">hola@mandotv.app</a> en we antwoorden.',
)
SOPORTE_HTML = '''      <h2 id="encontrar">De tv vinden</h2>
      <div class="preguntas">
        <details open><summary>Mijn tv verschijnt niet in de lijst</summary>
          <ol>
            <li>Controleer of je telefoon en de tv op hetzelfde wifi-netwerk zitten. Heeft je router een 2,4 GHz- en een 5 GHz-netwerk met verschillende namen, dan zien ze elkaar soms niet.</li>
            <li>Zorg dat de tv aanstaat.</li>
            <li>Controleer bij de iPhone of Mando TV toestemming heeft voor “Lokaal netwerk”, bij Instellingen, Mando TV.</li>
            <li>Tik in de lijst met tv’s op de knop voor het geval je tv niet verschijnt: de app controleert stap voor stap de meest voorkomende oorzaken (hetzelfde wifi-netwerk, vpn, toestemming voor het lokale netwerk en meer) en toont na elke correctie een knop om opnieuw te controleren.</li>
            <li>Verschijnt hij nog steeds niet, tik dan op de knop +, kies het merk en voer het IP-adres van de tv in. Je ziet het in het netwerkmenu van de tv (bijvoorbeeld 192.168.1.50).</li>
          </ol>
        </details>
        <details><summary>Werkt het met mobiele data of onderweg?</summary>
          <p>Nee. Mando TV praat met de tv binnen je thuisnetwerk, dus je telefoon moet met dat wifi-netwerk zijn verbonden.</p>
        </details>
      </div>

      <h2 id="conectar">Voor het eerst verbinden</h2>
      <p>Complete gidsen per merk: <a href="@@R_lg@@">LG</a>, <a href="@@R_samsung@@">Samsung</a>, <a href="@@R_roku@@">Roku</a> en <a href="@@R_android@@">Android TV</a>.</p>
      <div class="preguntas">
        <details><summary>LG</summary>
          <p>Als je op de tv tikt, verschijnt op het scherm een melding die om toestemming vraagt. Bevestig die met je gewone afstandsbediening. Dat doe je maar één keer.</p>
        </details>
        <details><summary>Samsung</summary>
          <p>De tv vraagt of je de verbinding van Mando TV toestaat. Kies met de afstandsbediening “Toestaan”. Heb je die per ongeluk geweigerd, ga dan naar Instellingen > Algemeen > Extern apparaatbeheer > Apparaatverbindingsbeheer en zet het op toegestaan.</p>
        </details>
        <details><summary>Roku</summary>
          <p>Roku vraagt niet om toestemming. Lukt de verbinding niet, ga dan op de Roku naar Instellingen > Systeem > Geavanceerde systeeminstellingen > Bediening door mobiele apps en laat de netwerktoegang op Standaard of Permissief staan (zet bij nieuwere Roku-software “Bediening door mobiele apps” op Ingeschakeld).</p>
        </details>
        <details><summary>Android TV en Google TV</summary>
          <p>De tv toont een code van 6 tekens. Voer hem precies zo in bij Mando TV als hij verschijnt. Het werkt bij Sony, Philips, TCL, Hisense, Sharp, Xiaomi, Chromecast met Google TV en andere met Android TV.</p>
        </details>
      </div>

      <h2 id="encender">De tv aanzetten via de app</h2>
      <p>Mando TV zet de tv aan via je thuisnetwerk. Daarvoor zijn twee dingen nodig: je hebt minstens één keer verbinding gemaakt terwijl de tv aanstond, en op de tv staat het aanzetten via het netwerk aan. De naam van de instelling verschilt per model; dit zijn de meest voorkomende:</p>
      <div class="preguntas">
        <details><summary>LG</summary>
          <p>Zoek in de instellingen (onder Algemeen > Apparaten > Externe apparaten, bij oudere modellen onder Verbinding > Beheer van mobiele verbindingen) naar “Tv aanzetten met mobiele telefoon” en zet “Via wifi aanzetten” aan. Staat er “Quick Start+”, zet die dan ook aan.</p>
        </details>
        <details><summary>Samsung</summary>
          <p>Zet “Aan met mobiele telefoon” aan onder Instellingen > Algemeen > Netwerk > Expertinstellingen.</p>
        </details>
        <details><summary>Roku</summary>
          <p>Zet bij Roku TV-toestellen “Snelle tv-start” aan onder Instellingen > Systeem > Stroom. Roku-spelers die op een tv zijn aangesloten, kun je zo niet aanzetten.</p>
        </details>
        <details><summary>Android TV en Google TV</summary>
          <p>Dat hangt af van de fabrikant. Zoek in de netwerk- of stroominstellingen naar “Wake on LAN”, “Inschakelen via netwerk”, “Netwerk-stand-by” of “Remote start”. Sommige modellen hebben deze optie niet.</p>
        </details>
      </div>

      <h2 id="falla">Als er iets niet lukt</h2>
      <div class="preguntas">
        <details><summary>De verbinding valt weg of er komt geen reactie</summary>
          <ol>
            <li>Tik op het scherm van de afstandsbediening op Opnieuw verbinden.</li>
            <li>Helpt dat niet, sluit dan Mando TV en open de app opnieuw.</li>
            <li>Heeft de tv een ander IP-adres gekregen, verwijder hem dan uit de lijst en voeg hem opnieuw toe.</li>
          </ol>
        </details>
        <details><summary>Zo stuur je ons een foutrapport</summary>
          <ol>
            <li>Tik in Mando TV op de knop Aanpassen (de schuifjes bovenin).</li>
            <li>Tik op Testrapport kopiëren.</li>
            <li>Plak het samen met het merk en model van je tv in een e-mail naar hola@mandotv.app.</li>
          </ol>
          <p>Het rapport bevat geen wachtwoorden, geen codes en niets van wat je typt.</p>
        </details>
        <details><summary>Ik heb Pro gekocht en het verschijnt niet</summary>
          <p>Tik bij Aanpassen op Aankoop herstellen, met hetzelfde store-account waarmee je hebt gekocht. Verschijnt het nog steeds niet, schrijf ons dan.</p>
        </details>
      </div>

      <h2 id="guias">Gidsen stap voor stap</h2>
      <p><a href="@@R_guias@@">Bekijk alle gidsen</a></p>
      <ul>
@@GUIAS@@
      </ul>

      <h2 id="contacto">Nog vragen?</h2>
      <p>Schrijf ons naar <a href="mailto:hola@mandotv.app?subject=Hulp%20bij%20Mando%20TV">hola@mandotv.app</a>. Vertel ons het merk en model van je tv en bij welke stap je vastloopt. Schrijf ons gerust in je eigen taal. We antwoorden in het Spaans of Engels en, als je wilt, in jouw taal met behulp van een vertaler.</p>
'''

PRIVACIDAD = dict(
  titulo='Privacyverklaring | Mando TV',
  desc='Mando TV verzamelt geen persoonsgegevens: geen accounts, geen advertenties, geen trackers. De app praat alleen met je tv binnen je wifi-netwerk.',
  h1='Privacy',
  intro='Kort gezegd: Mando TV verzamelt je gegevens niet. Er zijn geen accounts, geen advertenties, geen trackers en geen eigen servers die opslaan wat je doet.',
)
PRIVACIDAD_HTML = '''      <p class="fecha">Geldig sinds 14 november 2026. Laatst bijgewerkt op 26 november 2026.</p>

      <h2>Wie we zijn</h2>
      <p>Mando TV is een app waarmee je je tv bedient vanaf je telefoon of computer. Deze verklaring beschrijft welke informatie de app gebruikt en wat ze ermee doet. Heb je vragen, schrijf ons dan naar <a href="mailto:hola@mandotv.app">hola@mandotv.app</a>.</p>

      <h2>Welke gegevens we verzamelen</h2>
      <p>De app: geen. De app stuurt geen informatie over jou of over hoe je haar gebruikt naar ons of naar derden. Ze gebruikt geen analyse-, advertentie- of trackingtools.</p>
      <p>Deze website: we meten bezoeken op twee manieren, die worden uitgelegd in het gedeelte <a href="#cookies">Cookies op deze website</a>.</p>

      <h2>Wat de app op je apparaat opslaat</h2>
      <p>Om te werken slaat de app het volgende alleen op je telefoon of computer op:</p>
      <ul>
        <li>De tv’s die je hebt toegevoegd: naam, merk, IP-adres in je netwerk en hardwareadres van het netwerk (MAC), dat wordt gebruikt om aan te zetten.</li>
        <li>De verbindingssleutels die elke tv doorgeeft als je de toestemming bevestigt. Ze worden versleuteld opgeslagen in de beveiligde opslag van het systeem (sleutelhanger op iPhone en Mac, Keystore op Android, beschermde opslag op Windows).</li>
        <li>Je instellingen: licht of donker thema, achtergrondkleur, trillen en type afstandsbediening.</li>
        <li>Als je de Pro-functies gebruikt: je favoriete apps, je routines en je laatste YouTube-zoekopdrachten (je kunt ze in de app wissen).</li>
      </ul>
      <p>Als je de app verwijdert, wordt dit allemaal samen met de app gewist.</p>

      <h2>Met wie de app praat</h2>
      <p>Met je tv’s, binnen je wifi-netwerk thuis. Om ze te vinden doorzoekt de app je lokale netwerk; daarom vraagt ze op een iPhone om toestemming voor “Lokaal netwerk”. De tekst die je met het toetsenbord van de app typt, gaat rechtstreeks naar de tv en wordt niet opgeslagen.</p>
      <p>Bovendien downloadt de app bij het openen een klein openbaar bestand van deze website (mandotv.app/app/config.json), om te weten of er een nieuwe versie is die je moet installeren en welke functies bij Mando TV Pro horen. Dat is een download, zoals wanneer je een pagina opent: de app stuurt noch je gegevens, noch je tv’s, noch wat je doet. Ze geeft alleen de appversie en het systeem door (bijvoorbeeld Android), zodat ze je de juiste melding kan tonen. Heb je geen internet, dan werkt de app verder met het laatst gedownloade bestand; gaan er meer dan 30 dagen voorbij zonder dat het kon worden gedownload, dan vraagt de app je even verbinding te maken met internet.</p>

      <p>Als je foto’s of video’s naar de tv stuurt (een Pro-functie), laadt de tv alleen de bestanden die je kiest, rechtstreeks van je telefoon of pc via je wifi thuis. Ze gaan niet via internet en niet via ons, de app ziet je overige foto’s niet, en het delen eindigt zodra je dit scherm sluit.</p>
      <h2>Microfoon en spraak</h2>
      <p>Op iPhone, Mac en Android gebruikt het spraakzoeken de microfoon alleen zolang je op de spreekknop tikt. Wat je zegt, wordt door de spraakherkenning van je systeem omgezet in tekst: door Apple op iPhone en Mac en door Google op Android, telkens volgens hun eigen privacyvoorwaarden. Op Windows wordt de spraak op je eigen pc herkend en verlaat het apparaat niet; alleen op zeer oude processors gebruikt de app de spraakinvoer van Windows, van Microsoft, volgens hun privacyvoorwaarden. Op Windows gaat de microfoon open wanneer je het spraakpaneel opent en dicht wanneer je het sluit, of na 30 seconden zonder gebruik; zolang je niet spreekt, wordt er niets opgenomen of opgeslagen. Mando TV neemt de audio niet op en slaat hem niet op, en de ontstane tekst gaat rechtstreeks naar je tv, precies zoals wat je met het toetsenbord typt.</p>

      <h2>Thuis: apparaten uit Apple Home en Google Home</h2>
      <p>Als je het onderdeel Thuis (in test) opent, vraagt de app om toestemming de apparaten te zien die je al hebt in de Woning-app van Apple (HomeKit) of in Google Home. Met die toestemming leest ze hun naam, hun ruimte en hun status (aan of uit, helderheid, temperatuur of op welk punt van zijn programma een huishoudapparaat zit) om ze te tonen en door te geven wat je aantikt. Alles gebeurt tussen je telefoon en het systeem van Apple of Google: Mando TV slaat deze lijst niet op, stuurt hem niet naar ons of naar derden en gebruikt hem niet voor advertenties of analyses. Op Android werkt Google Home met je eigen Google-account, volgens de privacyverklaring van Google. Je kunt de toestemming op elk moment intrekken: op de iPhone onder Instellingen &gt; Privacy en beveiliging &gt; HomeKit, op Android in de instellingen van je Google-account.</p>
      <p>Als je tikt op “Hoe werkte Thuis bij jou?”, opent je e-mailapp met een bericht aan hola@mandotv.app dat een technische samenvatting bevat: de versie van de app, het systeem en hoeveel apparaten van elk type zijn verschenen en of ze reageren. Namen van apparaten, ruimtes of van je huis zitten er niet in, en het bericht wordt alleen verstuurd als je het zelf verzendt.</p>

      <h2>Testrapport</h2>
      <p>De app heeft een knop “Testrapport kopiëren” die ons helpt fouten op te lossen. Het rapport blijft alleen in het geheugen van de app zolang ze openstaat en wordt nooit uit zichzelf verstuurd: jij beslist of je het kopieert en deelt. Het bevat geen verbindingssleutels, geen koppelcodes en niets wat je invoert; alleen de stappen die de app heeft uitgevoerd, zoals zoeken, verbinden en de fouten.</p>

      <h2 id="cookies">Cookies op deze website</h2>
      <p>Dit geldt alleen voor de website mandotv.app, niet voor de app.</p>
      <h3>Altijd zonder cookies</h3>
      <p>We tellen bezoeken anoniem met Cloudflare Web Analytics: hoeveel mensen de website bezoeken, welke pagina’s ze lezen en uit welk land. Het gebruikt geen cookies, gebruikt je IP-adres niet om je te identificeren en volgt niet wat je op andere websites doet.</p>
      <h3>Met cookies, alleen als je toestemming geeft</h3>
      <p>Als je in de cookiemelding op “Accepteren” tikt, activeren we Google Analytics (van Google LLC) om beter te begrijpen hoe de website wordt gebruikt: paginaweergaven, bezoekduur, soort apparaat, ongeveer de stad en waar je vandaan komt. Daarvoor slaat het de cookies _ga en _ga_* tot 2 jaar op in je browser. Google kan deze gegevens verwerken op servers buiten Chili. We hebben de advertentiefuncties en Google Signals uitgeschakeld en gebruiken deze gegevens niet om je advertenties te tonen.</p>
      <p>Als je op “Weigeren” tikt of niets kiest, wordt Google Analytics niet geladen en wordt er geen cookie opgeslagen. Je kunt je keuze op elk moment wijzigen met de knop “Cookies” onderaan elke pagina; als je de toestemming intrekt, wissen we deze cookies.</p>
      <p>Je keuze wordt opgeslagen in je browser (lokale opslag, aan niemand verstuurd), zodat we het je niet nog een keer vragen.</p>

      <h2>Aankopen</h2>
      <p>Als je Mando TV Pro koopt, wordt de betaling afgehandeld door de appstore (App Store, Google Play of Microsoft Store). Wij ontvangen en bewaren je kaartgegevens niet. De store bevestigt de app alleen dat de aankoop bestaat.</p>

      <h2>E-mails die je ons stuurt</h2>
      <p>Als je ons schrijft naar <a href="mailto:hola@mandotv.app">hola@mandotv.app</a>, gebruiken we je e-mailadres en wat je ons meedeelt alleen om je te antwoorden. We geven ze niet door en gebruiken ze niet voor reclame. Je kunt op elk moment vragen dat we je berichten wissen.</p>

      <h2>Kinderen</h2>
      <p>De app verzamelt van niemand gegevens, ook niet van kinderen.</p>

      <h2>Wijzigingen in deze verklaring</h2>
      <p>Mocht op een dag veranderen wat de app met je gegevens doet, dan werken we deze pagina en de datum bovenaan bij voordat de wijziging de app bereikt.</p>
'''


# >>> guías traídas del inglés (ensamblar.py)
# Adaptadas con Ollama (qwen3.6:35b) desde las guías inglesas y auditadas por Opus el 22-nov. Rutas en idiomas_sitio.py.
GUIAS += [
  dict(clave='no-sub', corto='Afstandsbediening-app zonder abonnement', fecha='2026-11-23',
    titulo='Afstandsbediening-app voor tv zonder abonnement en advertenties',
    desc='Genoeg van afstandsbediening-apps met advertenties of abonnement? Mando TV is gratis en zonder advertenties, Pro is optioneel. Eerlijke vergelijking.',
    h1='Een afstandsbediening-app zonder abonnement en zonder advertenties',
    intro='Veel universele afstandsbedieningen tonen advertenties of vragen een weekabonnement voordat ze werken. Mando TV kiest een andere weg: de afstandsbediening is gratis, er zijn geen advertenties en geen account. Het optionele Pro koop je maar één keer. Hier de vergelijking, ook met wat de app niet kan.',
    pasos=[
      'Open vóór het installeren de storepagina van een app en controleer de in-app-aankopen. Prijzen per week of per maand wijzen op een abonnement.',
      'Controleer op Google Play of op de pagina “Bevat advertenties” staat, en lees de nieuwste beoordelingen met weinig sterren: daar duiken vaak onverwachte betaalmuren op.',
      'Zorg dat de app je tv via wifi kan bedienen. Mando TV werkt met Samsung (vanaf 2016), LG webOS, Roku, Google TV, Android TV en Fire TV.',
      'Installeer Mando TV, zet je telefoon op hetzelfde wifi-netwerk als de tv en tik in de lijst op je tv.',
      'Bevestig de melding op de tv of voer de getoonde code in. Toetsen, volume, zenders en toetsenbord kosten niets.',
    ],
    tabla=dict(titulo='Mando TV vergeleken met veel afstandsbediening-apps',
      cabeza=['', 'Mando TV', 'Veel apps met advertenties of abonnement'],
      filas=[
        ['Basisafstandsbediening', 'Gratis', 'Vaak gratis met advertenties of verstopt achter een proefperiode'],
        ['Advertenties', 'Geen', 'Veelvoorkomend'],
        ['Abonnement', 'Geen. Pro is een optionele eenmalige aankoop', 'Plannen per week of per maand komen vaak voor'],
        ['Account', 'Niet nodig', 'Verschilt'],
        ['Smart-tv’s via wifi', 'Samsung (vanaf 2016), LG webOS, Roku, Google TV, Android TV, Fire TV, Apple TV (bèta)', 'Afhankelijk van de app'],
        ['Infrarood voor oudere tv’s', 'Gratis op Android-telefoons met infraroodzender (nieuw)', 'Sommige apps, alleen bij telefoons met infraroodzender'],
        ['Bluetooth', 'Bèta vanaf Android 9, gratis', 'Afhankelijk van de app'],
        ['Foto’s en video’s naar de tv', 'Pro, via wifi (geen spiegelen)', 'Afhankelijk van de app'],
        ['Telefoons en computers', 'iPhone, iPad, Mac en Windows, plus Android in vroege toegang', 'Verschilt'],
        ['Schermspiegeling', 'Gratis op iPhone, iPad en Windows met de ingebouwde functie van elk apparaat. Op Windows kan Pro het pc-scherm ook spiegelen naar tv’s van LG, Samsung, Hisense en Android TV (bèta)', 'Sommige apps bieden het aan'],
      ],
      nota='Mando TV wordt met geen enkele specifieke app vergeleken. De actuele prijzen staan op de storepagina van de betreffende app.'),
    extra=[
      ('Wat Mando TV niet doet', 'Op iPhone en iPad verwijst het je naar Schermspiegeling in het Control Center, de functie van de iPhone zelf, die werkt met tv’s met AirPlay. Op Windows opent het Casten (Windows + K), en Mando TV Pro kan het pc-scherm via je wifi naar tv’s van LG, Samsung, Hisense en Android TV sturen (bèta, met enkele seconden vertraging en zonder geluid). Met Mando TV Pro kan het bovendien foto’s en video’s via je wifi naar de tv sturen. Het bedient Smart-tv’s via het wifi-netwerk thuis. Tv’s zonder Smart-tv-functie kun je met een Android-telefoon met infraroodzender via infrarood bedienen. Vanaf Android 9 kan de telefoon ook via Bluetooth als toetsenbord en afstandsbediening verbinding maken met Google TV, Android TV en Fire TV, helemaal zonder wifi. Deze optie is in de bèta en gratis.'),
      ('Hoe Mando TV geld verdient', 'Niet met advertenties en niet met jouw gegevens: de app verzamelt er geen. Mando TV wordt gefinancierd door Pro, een optionele eenmalige aankoop voor extra’s. De basisafstandsbediening is gratis.'),
      ('Op de apparaten die je al hebt', 'iPhone, iPad en Mac uit de App Store, Windows-pc’s uit de Microsoft Store en Android via gratis vroege toegang op Google Play. Zie [Afstandsbediening-app voor iPhone](@iphone) en [Afstandsbediening-app voor Windows](@windows).'),
      ('Privacy', 'Geen account en geen tracking in de app. De communicatie met de tv vindt alleen plaats in het lokale netwerk, de verbindingsgegevens blijven versleuteld op je apparaat. Details in de [privacyverklaring](@privacidad).'),
    ],
    marca=None,
    faq=[
      ('Bestaat er een afstandsbediening-app zonder abonnement?', 'Ja. Mando TV heeft helemaal geen abonnement: de afstandsbediening is gratis en zonder advertenties, Pro is een optionele eenmalige aankoop.'),
      ('Is Mando TV echt gratis?', 'Ja. Pijltoetsen, OK, Terug, Start, volume, zenders, cijfers, toetsenbord en aan-/uitzetten zijn gratis, zonder advertenties en zonder tijdslimiet.'),
      ('Werkt het zonder wifi?', 'Meestal niet. Mando TV bedient Smart-tv’s via je wifi thuis. Uitzonderingen: infrarood op Android-telefoons met infraroodzender, dat ook werkt met tv’s zonder Smart-tv-functie of zonder wifi-verbinding, en Bluetooth, in de bèta vanaf Android 9, voor Google TV, Android TV en Fire TV.'),
    ]),
  dict(clave='roku-app-alt', corto='Alternatief voor de Roku app', fecha='2026-11-23',
    titulo='Alternatief voor de Roku app: eenvoudige Roku-afstandsbediening',
    desc='Alternatief voor de Roku app: Mando TV bedient Roku-tv’s en -spelers via wifi, zonder account en advertenties, plus Samsung, LG en Google TV.',
    h1='Alternatief voor de Roku app: één voor alle tv’s',
    intro='De officiële Roku app kan veel: Channel Store, casten, Private Listening en een afstandsbediening. Zoek je alleen een snelle afstandsbediening of heb je thuis ook een Samsung-, LG- of Google TV-tv, dan is Mando TV een eenvoudig alternatief dat Roku via je wifi bedient, zonder account.',
    pasos=[
      'Zet je telefoon en de Roku op hetzelfde wifi-netwerk.',
      'Download Mando TV en open de app. Je Roku TV of Roku-speler verschijnt in de lijst. Tik erop. De Roku vraagt niet om een code.',
      'Gebruik de pijltoetsen, OK, Terug, Start, volume en het toetsenbord. Typ zoektermen in Roku-kanalen met het toetsenbord van je telefoon.',
      'Doen de toetsen niets, ga dan op de Roku naar Instellingen > Systeem > Geavanceerde systeeminstellingen > Bediening door mobiele apps en zet netwerktoegang op Standaard of Permissief (bij nieuwere Roku-software zet je Bediening door mobiele apps op Ingeschakeld).',
      'Optioneel: zet op de Roku TV “Snelle tv-start” aan onder Instellingen > Systeem > Stroom, zodat Mando TV de tv kan aanzetten.',
    ],
    extra=[
      ('Waar Mando TV beter past', 'Eén app voor meerdere tv’s: Roku, Samsung, LG en Google TV of Android TV. Zonder account, zonder advertenties. Ze werkt ook op een Windows-pc, handig aan je bureau. Pijltoetsen en volume reageren snel, en met het toetsenbord typ je zoektermen moeiteloos.'),
      ('Waar de officiële Roku app beter is', 'Houd de Roku app voor wat ze naast de afstandsbediening biedt, zoals kanalen zoeken en toevoegen uit de Roku Channel Store en het eigen casten en Private Listening (geluid via een koptelefoon op je telefoon). Gebruik beide als je wilt. Ze kunnen op dezelfde telefoon draaien.'),
      ('Roku TV-toestellen en Roku-spelers', 'Beide werken. Dat omvat Roku TV-modellen van TCL, Hisense, Philips en andere, en Roku Express, Streaming Stick en Ultra. Details vind je op de [pagina over de Roku afstandsbediening-app](@roku).'),
      ('Als de Roku app niet meer werkt', 'Reageren de toetsen niet meer, dan blokkeert de Roku meestal de bediening door apps. De gids [Roku app werkt niet](@roku-403) toont de instelling die het probleem oplost.'),
      ('Gratis en Pro', 'Pijltoetsen, OK, Terug, Start, volume, zenders, cijfertoetsen, toetsenbord, apps openen, ingangen wisselen en aan- of uitzetten zijn gratis, zonder advertenties en zonder abonnement. Het touchpad, de spraakopdrachten, favoriete apps, routines en de slaaptimer horen bij Mando TV Pro, een eenmalige aankoop zonder abonnement.'),
    ],
    marca='roku',
    faq=[
      ('Heb ik een Roku-account nodig om Mando TV te gebruiken?', 'Nee. Mando TV communiceert met de Roku via je thuisnetwerk en vraagt niet om een account.'),
      ('Vervangt Mando TV de Roku Mobile app helemaal?', 'Als afstandsbediening wel. Voor de Channel Store, casten en Private Listening houd je de officiële Roku app.'),
      ('Werkt het met mijn Roku Express of Streaming Stick?', 'Ja. Alle Roku-spelers en Roku TV-toestellen worden op dezelfde manier bediend.'),
    ]),
  dict(clave='lg-thinq', corto='Alternatief voor de LG ThinQ app', fecha='2026-11-23',
    titulo='Alternatief voor de LG ThinQ app: LG-afstandsbediening zonder account',
    desc='Zoek je een LG ThinQ-alternatief, alleen als afstandsbediening? Mando TV bedient LG-tv’s met webOS via wifi, zonder LG-account en advertenties.',
    h1='Alternatief voor de LG ThinQ app voor je LG-tv',
    intro='LG ThinQ is de officiële app van LG, bedoeld voor het hele slimme huis: huishoudapparaten, de tv en meer. Wil je alleen een eenvoudige afstandsbediening voor je LG-tv, dan doet Mando TV precies dat via je wifi thuis, zonder dat je een LG-account hoeft aan te maken en zonder advertenties.',
    pasos=[
      'Zet je telefoon of pc (iPhone, Android of Windows) en je LG-tv op hetzelfde wifi-netwerk.',
      'Download Mando TV en open de app. Je LG-tv verschijnt vanzelf in de lijst. Tik erop.',
      'Op de tv verschijnt een melding. Bevestig die één keer met de afstandsbediening van de tv, de joystick onder het scherm of de Magic Remote.',
      'Toetsen, volume en toetsenbord werken meteen. Je hebt geen LG-account nodig en hoeft de tv niet te registreren.',
      'Optioneel: zet “Tv aanzetten met mobiele telefoon” aan in de tv-instellingen, zodat je de tv ook vanaf je telefoon kunt aanzetten.',
    ],
    extra=[
      ('Mando TV of LG ThinQ: wat waarvoor', 'Gebruik ThinQ als je LG-huishoudapparaten zoals een wasmachine, een koelkast of een airco wilt beheren of LG-accountfuncties nodig hebt. Gebruik Mando TV als je een snelle, eenvoudige afstandsbediening voor de tv wilt die ook voor Samsung, Roku en Google TV in dezelfde app werkt. Veel mensen houden beide: ThinQ voor de huishoudapparaten, Mando TV voor de tv.'),
      ('Wat Mando TV op een LG-tv doet', 'Het werkt met LG Smart-tv’s met webOS, dus met de meeste modellen sinds 2014, inclusief LED, NanoCell, QNED en OLED. Het biedt je de pijltoetsen, OK, Terug, Start, volume, zenders, dempen, afspeelbediening en een toetsenbord om te typen in het zoeken van de tv en in de meeste apps. De lijst met apps en de lijst met ingangen zijn ook gratis. Met Pro krijg je er een aanwijzer bij zoals bij de Magic Remote.'),
      ('Wat Mando TV niet doet', 'Het bedient geen LG-huishoudapparaten, gebruikt je LG-account niet en vervangt de LG-accountdiensten op de tv niet. Het is een afstandsbediening, geen smarthome-hub.'),
      ('Privacy en advertenties', 'Mando TV heeft geen advertenties en geen account. Het praat alleen binnen je thuisnetwerk met de tv en slaat de verbindingssleutel versleuteld op je apparaat op. Alle functies vind je op de pagina [LG afstandsbediening-app](@lg).'),
      ('Gratis en Pro', 'Pijltoetsen, OK, Terug, Start, volume, zenders, cijfertoetsen, toetsenbord, apps openen, ingangen wisselen en aan-/uitzetten zijn gratis, zonder advertenties en zonder abonnement. Het touchpad, de spraakopdrachten, favoriete apps, routines en de slaaptimer horen bij Mando TV Pro, een eenmalige aankoop zonder abonnement.'),
    ],
    marca='lg',
    faq=[
      ('Kan ik mijn LG-tv bedienen zonder de LG ThinQ app?', 'Ja. Mando TV maakt via je wifi rechtstreeks verbinding met LG-tv’s met webOS. Je accepteert één keer een melding op de tv en dat was het, helemaal zonder LG-account.'),
      ('Werkt Mando TV met de aanwijzer van de LG Magic Remote?', 'Mando TV Pro heeft een aanwijzer die je met je vinger over het scherm van je telefoon beweegt, vergelijkbaar met hoe de Magic Remote de pijl beweegt.'),
      ('Is Mando TV van LG?', 'Nee. Mando TV is een onafhankelijke app en heeft geen band met LG. LG en ThinQ zijn eigendom van hun houders en worden alleen genoemd om de compatibiliteit te beschrijven.'),
    ]),
  dict(clave='smartthings', corto='SmartThings-alternatief', fecha='2026-11-23',
    titulo='SmartThings werkt niet? Eenvoudig alternatief voor Samsung',
    desc='SmartThings te traag of fout? Mando TV bedient Samsung-tv’s met Tizen rechtstreeks via wifi. Zonder Samsung-account, zonder advertenties. Stap voor stap.',
    h1='SmartThings-alternatief voor Samsung-tv’s',
    intro='SmartThings is de Samsung-app voor het hele slimme huis en de afstandsbediening ervan loopt via je Samsung-account. Werkt ze niet meer of zoek je een snelle oplossing, dan bedient Mando TV Samsung-tv’s met Tizen, bouwjaar 2016 en nieuwer, rechtstreeks via je wifi, zonder account.',
    pasos=[
      'Zet je telefoon en de Samsung-tv op hetzelfde wifi-netwerk.',
      'Download Mando TV en open de app. Je Samsung-tv verschijnt vanzelf in de lijst. Tik erop.',
      'De tv vraagt of je de verbinding wilt toestaan. Kies “Toestaan” met de afstandsbediening of met de knop op de tv (alleen de eerste keer).',
      'Gebruik meteen de pijltoetsen, OK, Terug, Start, volume, zenders en het toetsenbord.',
      'Optioneel: zet “Aan met mobiele telefoon” aan onder Instellingen > Algemeen > Netwerk > Expertinstellingen, zodat Mando TV de tv ook kan aanzetten.',
    ],
    extra=[
      ('Waarom een afstandsbediening op je telefoon niet meer werkt', 'De oorzaken zijn meestal simpel: telefoon en tv zitten op verschillende wifi-netwerken, een vpn is actief of de tv staat in diepe stand-by. Bij SmartThings kan bovendien het Samsung-account problemen geven, bijvoorbeeld als je bent afgemeld. Mando TV praat rechtstreeks met de tv in het thuisnetwerk, er is geen account om in te loggen. Meer tips vind je bij [Je telefoon vindt de tv niet](@not-found).'),
      ('Mando TV of SmartThings: wat waarvoor', 'Houd SmartThings als je het gebruikt voor Samsung-huishoudapparaten, lampen of andere smarthome-apparaten of voor functies van je Samsung-account. Gebruik Mando TV als je gewoon een snelle afstandsbediening voor de tv wilt of thuis ook een apparaat van LG, Roku, Google TV of Fire TV hebt: één app bedient ze allemaal. Beide apps kunnen op dezelfde telefoon staan.'),
      ('Als je de toestemming per ongeluk hebt geweigerd', 'Ga op de tv naar Instellingen > Algemeen > Extern apparaatbeheer > Apparaatverbindingsbeheer en zet Mando TV op toegestaan.'),
      ('Geen afstandsbediening?', 'Je kunt de melding bevestigen met de knop op de tv zelf. De gids [Samsung tv zonder originele afstandsbediening](@samsung-lost) laat zien hoe.'),
      ('Gratis en Pro', 'De afstandsbediening kun je gratis downloaden en gebruiken, zonder advertenties en zonder abonnement. Mando TV Pro is een optionele eenmalige aankoop voor extra’s.'),
    ],
    marca='samsung',
    faq=[
      ('Kan ik mijn Samsung-tv bedienen zonder SmartThings?', 'Ja. Mando TV maakt via je wifi rechtstreeks verbinding met Samsung-tv’s met Tizen. Je staat de verbinding één keer toe op de tv, zonder Samsung-account.'),
      ('Bedient Mando TV ook Samsung-huishoudapparaten?', 'Nee. Het is alleen een afstandsbediening voor de tv. Voor huishoudapparaten en andere smarthome-apparaten houd je SmartThings.'),
      ('Is Mando TV van Samsung?', 'Nee. Mando TV is een onafhankelijke app en heeft geen band met Samsung. Samsung en SmartThings zijn eigendom van hun houders en worden alleen genoemd om de compatibiliteit te beschrijven.'),
    ]),
  dict(clave='googletv-alt', corto='Alternatief voor de Google TV-afstandsbediening', fecha='2026-11-23',
    titulo='Google TV-afstandsbediening werkt niet? Het alternatief',
    desc='Vindt de afstandsbediening-app voor Google TV de tv niet? Mando TV bedient Google TV en Android TV via wifi, zonder Google-account en advertenties.',
    h1='Alternatief voor de Google TV-afstandsbediening op je telefoon',
    intro='De telefoonafstandsbediening voor Google TV en Android TV zit in de app van Google zelf en is gekoppeld aan je Google-account. Vindt ze de tv niet, dan kom je niet verder. Mando TV is een aparte afstandsbediening-app die koppelt met de code van 6 tekens op het scherm en werkt zonder Google-account, op een iPhone, een Android-telefoon of een Windows-pc.',
    pasos=[
      'Zet de tv aan en zet je telefoon op hetzelfde wifi-netwerk.',
      'Download Mando TV en open de app. Tik in de lijst op je tv met Google TV of Android TV.',
      'De tv toont een code van 6 tekens. Voer die in bij Mando TV en tik op Koppelen.',
      'Gebruik de pijltoetsen, OK, Terug, Start, het volume en het toetsenbord. Je hoeft nergens in te loggen.',
      'Optioneel: zoek in de instellingen van de tv naar Wake on LAN of “Inschakelen via netwerk”, zodat de app de tv ook kan aanzetten.',
    ],
    extra=[
      ('Waarom de telefoonafstandsbediening de tv niet meer vindt', 'Meestal ligt het aan het netwerk: telefoon en tv zitten op verschillende wifi-netwerken, een vpn is actief of een gastnetwerk scheidt de apparaten. Los dat eerst op, want het raakt alle afstandsbediening-apps. Meer daarover in [Je telefoon vindt de tv niet](@not-found).'),
      ('Met welke tv’s het werkt', 'Tv’s met Google TV en Android TV van Sony, TCL, Hisense, Philips, Sharp, Xiaomi, Toshiba en meer, plus Chromecast met Google TV, Google TV Streamer en Nvidia Shield. Alle worden op dezelfde manier gekoppeld, eenmalig met de code op het scherm.'),
      ('Waar de app van Google beter is', 'De app van Google helpt je ook bij het vinden van content om te kijken en onthoudt je kijklijst. Houd haar daarvoor. Mando TV is alleen de afstandsbediening en bedient bovendien Samsung, LG, Roku en Fire TV-apparaten vanuit dezelfde app en vanaf een Windows-pc.'),
      ('Als de oude Android TV-afstandsbediening-app ontbreekt', 'Google heeft de telefoonafstandsbediening uit de oude Android TV Remote Control app naar de Google TV app verplaatst. Zoek je een zelfstandige afstandsbediening, dan is Mando TV een optie.'),
      ('Gratis en Pro', 'De afstandsbediening kun je gratis downloaden en gebruiken, zonder advertenties en zonder abonnement. Mando TV Pro is een optionele eenmalige aankoop voor extra’s.'),
    ],
    marca='android',
    faq=[
      ('Heb ik een Google-account nodig om Mando TV met Google TV te gebruiken?', 'Nee. De code op de tv is genoeg om te koppelen.'),
      ('Werkt het met Chromecast met Google TV?', 'Ja. Het koppelen gaat op dezelfde manier, met de code van 6 tekens op het scherm.'),
      ('Kan ik het vanaf een iPhone gebruiken?', 'Ja. Mando TV is beschikbaar in de App Store voor iPhone en iPad, in de Microsoft Store voor Windows en in de gratis vroege toegang op Google Play voor Android.'),
    ]),
  dict(clave='windows', corto='Afstandsbediening voor Windows-pc', fecha='2026-11-23',
    titulo='Afstandsbediening-app voor Windows: tv bedienen met je pc',
    desc='Bedien Samsung, LG, Roku, Google TV of Fire TV vanaf een Windows-pc met Mando TV: sneltoetsen, mini-afstandsbediening en wifi. In de Microsoft Store.',
    h1='Afstandsbediening-app voor de Windows-pc',
    intro='Mando TV heeft een Windows-app die je pc of laptop via het thuisnetwerk verandert in een afstandsbediening voor de tv. Typ op de tv met je echte toetsenbord, laat tijdens het werken een klein afstandsbedieningvenster bovenop staan en bedien Samsung, LG, Roku, Google TV of Fire TV met dezelfde app.',
    pasos=[
      'Installeer Mando TV gratis uit de Microsoft Store op een pc met Windows 10 of 11.',
      'Zorg dat de pc en de tv op hetzelfde netwerk zitten, via wifi of kabel op dezelfde router.',
      'Open Mando TV. De tv verschijnt in de lijst. Klik erop.',
      'Bevestig de melding op de tv als hij erom vraagt (LG, Samsung), of voer de getoonde code in (Google TV, Fire TV).',
      'Klik op de toetsen of typ een zoekopdracht met je toetsenbord. Klaar.',
    ],
    extra=[
      ('Sneltoetsen (Pro)', 'Met Pro wordt het toetsenbord van je pc een afstandsbediening: pijltoetsen om te bewegen, Enter voor OK, Backspace of Esc om terug te gaan, plus en min voor het volume, M om te dempen en de spatiebalk om te pauzeren.'),
      ('Mini-afstandsbediening (Pro)', 'Een klein afstandsbedieningvenster dat boven alle andere vensters blijft. Zo verander je het volume of pauzeer je zonder je werk te onderbreken.'),
      ('Typen op de tv vanaf de pc', 'Het schermtoetsenbord van een tv is traag. In Mando TV typ je met je echte toetsenbord en de tekst komt in het zoekveld van de tv terecht. Dit onderdeel is gratis.'),
      ('Meer details', 'De handleiding stap voor stap vind je bij [Tv bedienen met je pc](@pc). Voor de telefoon lees je [Telefoon als afstandsbediening via wifi](@wifi).'),
      ('Gratis en Pro', 'De pijltoetsen, OK, Terug, Start, volume, zenders, cijfertoetsen, toetsenbord, apps openen, ingangen wisselen en aan- of uitzetten zijn gratis, zonder advertenties en zonder abonnement. Het touchpad, de spraakopdrachten, favoriete apps, routines en de slaaptimer horen bij Mando TV Pro, een eenmalige aankoop zonder abonnement. Op Windows koop je Pro via de Microsoft Store.'),
      ('Spraakopdrachten vanaf de pc (Pro)', 'Met Pro kun je met de tv praten via de pc-microfoon. De spraak wordt rechtstreeks op de pc herkend: daarvoor heb je geen internet nodig en hoef je niets in Windows in te stellen. Wat je zegt, verlaat de pc nooit en wordt niet opgeslagen. Alleen bij zeer oude processors valt de app terug op de spraakinvoer van Windows. Daarvoor moet online spraakherkenning aanstaan in de privacy-instellingen en moet je taal in Windows zijn toegevoegd.'),
    ],
    marca=None,
    faq=[
      ('Heeft de afstandsbediening-app voor Windows Bluetooth of een kabel nodig?', 'Nee. Ze gebruikt je thuisnetwerk. Pc en tv moeten alleen op dezelfde router zijn aangesloten.'),
      ('Welke tv’s kan ik vanaf Windows bedienen?', 'Samsung-tv’s met Tizen, LG-tv’s met webOS, Roku TV en spelers, Google TV en Android TV en Fire TV.'),
      ('Kan ik het tv-beeld op de pc zien of via de pc-speakers horen?', 'Nee. Mando TV is alleen een afstandsbediening. Het spiegelt of streamt het tv-beeld niet naar de computer.'),
      ('Waarom werkt de spraak niet op mijn Windows-pc?', 'De spraakbediening is een Pro-functie. Controleer dus of Pro actief is en de pc-microfoon werkt. Op de meeste pc’s wordt de spraak rechtstreeks op de pc herkend, zonder internet. Alleen bij zeer oude processors gebruikt de app de spraakinvoer van Windows: zet dan online spraakherkenning aan in de privacy-instellingen van Windows en voeg je taal toe in de taalinstellingen.'),
    ]),
  dict(clave='iphone', corto='Afstandsbediening-app voor iPhone', fecha='2026-11-23',
    titulo='Afstandsbediening-app voor iPhone: Samsung, LG, Roku, Google TV',
    desc='Gebruik je iPhone als afstandsbediening voor Samsung, LG, Roku, Google TV en Fire TV via wifi. Gratis in de App Store, zonder account en zonder advertenties.',
    h1='Afstandsbediening-app voor iPhone: één voor alle tv’s',
    intro='Mando TV maakt van je iPhone of iPad de afstandsbediening voor Samsung, LG, Roku, Google TV of Android TV en Fire TV, via je wifi thuis. De app is gratis in de App Store, zonder account en zonder advertenties. Ze draait ook op Android en Windows.',
    pasos=[
      'Download Mando TV gratis uit de App Store.',
      'Zet je iPhone en de tv op hetzelfde wifi-netwerk.',
      'Open Mando TV en tik op Sta toe als iOS vraagt om toegang tot het lokale netwerk. De app heeft dat nodig om de tv te vinden.',
      'Tik in de lijst op je tv. Bevestig de melding op de tv als hij erom vraagt (LG en Samsung), of voer de code in die de tv toont (Google TV of Fire TV).',
      'Gebruik de toetsen, het volume en het toetsenbord. Je bent verbonden.',
    ],
    extra=[
      ('Werkt met deze tv’s', 'LG webOS, Samsung Tizen (bouwjaar 2016 en nieuwer), Roku TV en Roku-spelers, Google TV en Android TV en Fire TV. De merkpagina’s zijn [Samsung](@samsung), [LG](@lg), [Roku](@roku) en [Android TV](@android).'),
      ('Waarom het om het lokale netwerk vraagt', 'De iPhone blokkeert de toegang van apps tot apparaten in je thuisnetwerk, tenzij je het toestaat. Verschijnt de tv niet in de lijst, open dan Instellingen > Mando TV en zet “Lokaal netwerk” aan. De app communiceert alleen met je tv binnen je thuisnetwerk.'),
      ('Waarom Mando TV en niet de app van de fabrikant', 'Elk tv-merk heeft zijn eigen app en wil een eigen installatie of een eigen account. Mando TV is één app voor iedereen, zonder account.'),
      ('Gratis en Pro op de iPhone', 'Pijltoetsen, OK, Terug, Start, volume, zenders, cijfertoetsen, toetsenbord, apps openen, ingangen wisselen en aan- of uitzetten zijn gratis, zonder advertenties en zonder abonnement. Het touchpad, de spraakopdrachten, favoriete apps, routines en de slaaptimer horen bij Mando TV Pro, een eenmalige aankoop zonder abonnement. Je koopt Pro één keer, rechtstreeks in de app.'),
    ],
    marca=None,
    faq=[
      ('Is Mando TV gratis op de iPhone?', 'De download is gratis, zonder advertenties. De basisafstandsbediening is gratis, net als het openen van apps en het wisselen van ingangen. Extra’s zoals het touchpad, de spraakopdrachten en de routines horen bij Mando TV Pro, een eenmalige aankoop.'),
      ('Werkt het op de iPad?', 'Ja. Dezelfde app draait op iPhone en iPad.'),
      ('Heeft een afstandsbediening-app voor iPhone Bluetooth of een infraroodzender nodig?', 'Niet op de iPhone. iPhones hebben geen infraroodzender, dus infraroodbediening is daar niet beschikbaar, en de Bluetooth-optie is er alleen voor Android 9 of nieuwer, niet voor de iPhone. Op de iPhone bedient Mando TV Smart-tv’s en Apple TV (bèta) via je wifi thuis.'),
    ]),
  dict(clave='firetv', corto='Fire TV-afstandsbediening', fecha='2026-11-23',
    titulo='Fire TV afstandsbediening-app voor telefoon en pc',
    desc='Fire TV-afstandsbediening op je telefoon: bedien Fire TV Stick, Fire TV Cube of een tv met Fire TV via wifi, met pincode van 4 cijfers. Zonder Amazon-app.',
    h1='Fire TV-afstandsbediening voor je telefoon of pc',
    intro='Is de Fire TV-afstandsbediening weg of zijn de batterijen leeg, dan bedient Mando TV een Fire TV Stick, een Fire TV Cube of een tv met ingebouwde Fire TV via wifi. Het koppelen gaat met een pincode van 4 cijfers. Fire TV is nieuw in Mando TV, werk de app dus eerst bij.',
    pasos=[
      'Werk Mando TV bij naar de nieuwste versie uit de App Store, Microsoft Store of Google Play.',
      'Zet de Fire TV aan en zet je telefoon op hetzelfde wifi-netwerk.',
      'Open Mando TV. Je Fire TV verschijnt in de lijst. Tik erop.',
      'Op het scherm van de tv verschijnt een pincode van 4 cijfers. Voer die in bij Mando TV. Dat doe je maar één keer.',
      'Gebruik de pijltoetsen, OK, Terug, Start, afspeeltoetsen en het toetsenbord om te zoeken.',
    ],
    extra=[
      ('Ondersteunde Fire TV-apparaten', 'Fire TV Stick, Fire TV Stick 4K, Fire TV Cube en tv’s met ingebouwde Fire TV, zoals tv’s uit de Amazon Fire TV Edition-reeks en sommige Hisense-modellen. De ondersteuning is nieuw en we hebben tot nu toe maar weinig echte apparaten kunnen testen. Werkt er iets niet zoals verwacht, schrijf ons dan je model via de helppagina.'),
      ('Fire TV aanzetten', 'Mando TV zet een Fire TV niet via het netwerk aan. Zet de tv aan met de aan-knop op het toestel: een ingestoken Fire TV Stick of Cube wordt meestal wakker via HDMI-CEC, en bij een tv met ingebouwde Fire TV is de tv de Fire TV. Daarna bedien je hem vanaf je telefoon.'),
      ('Als je Fire TV niet verschijnt', 'Zorg dat beide apparaten op hetzelfde wifi-netwerk zitten en de Fire TV wakker is. Sta op een iPhone “Lokaal netwerk” toe voor Mando TV in de instellingen. Zie [Je telefoon vindt de tv niet](@not-found).'),
      ('Helemaal geen afstandsbediening?', 'De Fire TV moet de pincode op het scherm tonen, dus tv en Fire TV moeten aanstaan en een beeld tonen. Staat de tv op een verkeerde ingang, wissel dan met de toetsen op de tv. Zie [Ingang wisselen zonder afstandsbediening](@hdmi).'),
      ('Gratis en Pro', 'Pijltoetsen, OK, Terug, Start, volume, zenders, cijfers, toetsenbord, apps openen, ingangen wisselen en aan-/uitzetten zijn gratis, zonder advertenties en zonder abonnement. Het touchpad, de spraakopdrachten, favoriete apps, routines en de slaaptimer horen bij Mando TV Pro, een eenmalige aankoop zonder abonnement.'),
    ],
    marca=None,
    faq=[
      ('Heb ik de Amazon Fire TV-app nodig?', 'Nee. Mando TV maakt via je wifi met een pincode verbinding met de Fire TV. Je hebt geen Amazon-account op je telefoon nodig.'),
      ('Werkt het met tv’s met Fire TV en met Fire TV Sticks?', 'Ja, daar is het precies voor gemaakt. De ondersteuning is nieuw, houd de app actueel en laat ons weten welke modellen niet werken zoals verwacht.'),
      ('Waarom heb ik een pincode nodig?', 'De Fire TV toont een pincode van 4 cijfers om te bewijzen dat je voor de tv zit. Niemand kan koppelen zonder het scherm te zien.'),
    ]),
  dict(clave='firetv-lost', corto='Fire TV-afstandsbediening kwijt', fecha='2026-11-23',
    titulo='Fire TV-afstandsbediening kwijt? Zo helpt je telefoon',
    desc='Afstandsbediening van de Fire TV Stick kwijt? Bedien hem via wifi met je telefoon, gekoppeld met een pincode van 4 cijfers. Tips voor nieuw wifi en HDMI-CEC.',
    h1='Fire TV-afstandsbediening kwijt: zo gebruik je je telefoon',
    intro='Is de afstandsbediening van je Fire TV Stick, Fire TV Cube of Smart-tv met Fire TV kwijt of werkt hij niet meer, dan neemt je telefoon de bediening over, zolang de Fire TV nog met je wifi is verbonden. Het koppelen gaat met een pincode van 4 cijfers op het scherm, dus je hebt de oude afstandsbediening er nooit voor nodig.',
    pasos=[
      'Zet de tv aan met de knop op het toestel. Een ingestoken Fire TV Stick of Cube wordt meestal mee wakker; bij ingeschakelde HDMI-CEC wisselt de tv vaak automatisch naar zijn ingang.',
      'Toont de tv een andere ingang, wissel dan met de ingangs- of bronknop op de tv. Zie [Ingang wisselen zonder afstandsbediening](@hdmi).',
      'Zet je telefoon op hetzelfde wifi-netwerk als de Fire TV.',
      'Download Mando TV en open de app. Je Fire TV verschijnt in de lijst. Tik erop.',
      'De tv toont een pincode van 4 cijfers. Voer die in bij Mando TV. Dat doe je maar één keer.',
      'Gebruik de pijltoetsen, OK, Terug, Start, volume, afspeeltoetsen en het toetsenbord op je telefoon.',
    ],
    extra=[
      ('Probeer eerst de tv-afstandsbediening (HDMI-CEC)', 'Veel tv-afstandsbedieningen kunnen een Fire TV Stick bedienen via HDMI-CEC. Is de Fire TV-interface te zien, druk dan op de pijlen en OK op de afstandsbediening van de tv. Gebeurt er niets, zet CEC dan aan in de instellingen van de tv (Anynet+ bij Samsung, SIMPLINK bij LG, BRAVIA Sync bij Sony) en op de Fire TV de HDMI-CEC-apparaatbediening in de weergave-instellingen (“Weergave en geluid”).'),
      ('Als je van wifi bent gewisseld', 'Zonder afstandsbediening kun je het nieuwe wifi-wachtwoord niet op de Fire TV invoeren, maar er is een uitweg: maak op een tweede telefoon een hotspot met exact dezelfde naam en hetzelfde wachtwoord als je oude wifi. De Fire TV maakt er automatisch verbinding mee. Verbind de telefoon met Mando TV daarmee, koppel hem met de pincode, ga dan op de Fire TV naar Instellingen > Netwerk en kies je nieuwe wifi-netwerk. Verbind ten slotte ook je telefoon met het nieuwe wifi-netwerk.'),
      ('Een vervangende afstandsbediening koppelen', 'De meeste nieuwe Fire TV-afstandsbedieningen koppel je door de Start-toets ongeveer 10 seconden ingedrukt te houden, in de buurt van de Fire TV. Lukt het niet, open dan Instellingen > Controllers en Bluetooth-apparaten > Amazon Fire TV-afstandsbedieningen > Nieuwe afstandsbediening toevoegen. Dit menu bereik je ook vanaf je telefoon met Mando TV.'),
      ('Fire TV ingebouwd in de tv', 'Bij tv’s met ingebouwde Fire TV, zoals veel modellen van Insignia en Toshiba, werken dezelfde stappen, want de tv zelf is de Fire TV.'),
      ('Voordat je begint', 'De ondersteuning voor Fire TV is nieuw in Mando TV. Werk de app eerst bij. Reageert je model niet zoals verwacht, schrijf ons dan via de [helppagina](@soporte) en noem het model.'),
      ('Gratis en Pro', 'De afstandsbediening kun je gratis downloaden en gebruiken, zonder advertenties en zonder abonnement. Mando TV Pro is een optionele eenmalige aankoop voor extra’s.'),
    ],
    marca=('firetv', 'Fire TV-afstandsbediening'),
    faq=[
      ('Kan ik een Fire TV Stick met mijn telefoon bedienen zonder de afstandsbediening?', 'Ja, zolang de Fire TV aanstaat en met je wifi is verbonden. Mando TV koppelt via de pincode van 4 cijfers op de tv, dus je hebt de oude afstandsbediening niet nodig.'),
      ('Werkt het als de Fire TV op een nieuw wifi-netwerk zit?', 'Niet rechtstreeks, want telefoon en Fire TV moeten op hetzelfde netwerk zitten. Breng de Fire TV eerst weer online met de hotspot-truc op deze pagina.'),
      ('Heb ik de Amazon Fire TV-app of een Amazon-account nodig?', 'Nee. Mando TV maakt via je thuisnetwerk met de pincode verbinding en heeft geen eigen account nodig.'),
    ]),
  dict(clave='turn-on', corto='Tv aanzetten zonder afstandsbediening', fecha='2026-11-23',
    titulo='Tv aanzetten zonder afstandsbediening (alle merken)',
    desc='Tv aanzetten zonder afstandsbediening: waar de knop zit bij Samsung, LG, TCL, Hisense en Sony. Plus HDMI-CEC en telefoontrucs.',
    h1='Zo zet je een tv aan zonder afstandsbediening',
    intro='Bijna elke tv heeft nog een fysieke aan-/uitknop. Hij zit alleen goed verstopt. Hier zie je waar hij bij elk merk zit, plus twee manieren om het zoeken de volgende keer te besparen: HDMI-CEC vanaf een console of streamingapparaat, en het aanzetten van de tv via je telefoon over wifi.',
    pasos=[
      'Kijk onder het midden van het scherm, vlak achter het merklogo. Veel tv’s hebben daar een kleine losse knop of een joystick, naar beneden gericht.',
      'Zit hij daar niet, voel dan aan de achterkant van de tv in de buurt van de onderste hoeken, daarna langs de linker- en rechterrand.',
      'Druk één keer op de knop. Bij veel tv’s met maar één knop opent een korte druk bij een aangezet toestel een klein menu voor ingangen en volume, en zet een lange druk hem uit.',
      'Nog steeds niets? Controleer het netsnoer aan beide kanten en probeer een ander stopcontact. Brandt het stand-bylampje niet, dan krijgt de tv geen stroom.',
      'Zodra de tv aanstaat, stel hem zo in dat je de knop niet meer nodig hebt: zet HDMI-CEC en het aanzetten via het netwerk aan, beide hieronder uitgelegd.',
    ],
    extra=[
      ('Waar de aan-/uitknop zit, per merk', 'Samsung: een bedieningsknop of joystick onder het midden van het scherm of aan de achterkant bij een onderhoek. LG: bij de meeste modellen een joystickknop onder het LG-logo. TCL en Hisense: meestal een kleine knop onder het midden van het scherm of aan de achterkant in de buurt van een onderhoek. Sony: aan de achterkant of aan een zijrand, onderaan dicht bij de rand. Vizio: aan de achterkant, linksonder of rechtsonder, of aan de zijkant. De posities verschillen per model. Kun je hem niet vinden, zoek dan de handleiding op met het modelnummer op het label aan de achterkant.'),
      ('De tv aanzetten via een console of streamingapparaat (HDMI-CEC)', 'Met HDMI-CEC aan zet het aanzetten van een PlayStation, een Xbox, een Roku-speler, een Fire TV Stick of een Chromecast ook de tv aan en wisselt hij naar de juiste ingang. Elk merk noemt de instelling anders: Anynet+ bij Samsung, SIMPLINK bij LG, BRAVIA Sync bij Sony en CEC bij de meeste andere. Meer in [Tv aanzetten en naar de HDMI van je spelconsole wisselen](@console).'),
      ('De tv aanzetten via je telefoon', 'Smart-tv’s kunnen via wifi worden wakker gemaakt als je dat één keer toestaat, en dan zet Mando TV ze vanaf je telefoon aan. Zet bij Samsung “Aan met mobiele telefoon” aan onder Instellingen > Algemeen > Netwerk > Expertinstellingen. Zet bij LG “Tv aanzetten met mobiele telefoon” aan ([stap voor stap](@lg-on)). Zet bij een Roku TV “Snelle tv-start” aan onder Instellingen > Systeem > Stroom. Zoek bij Google TV en Android TV naar Wake on LAN of “Inschakelen via netwerk”, als je model dat heeft. Dat doe je één keer, met de tv aan.'),
      ('Als je geen knop vindt', 'Sommige nieuwere tv’s verstoppen de enige knop zo goed dat het lijkt alsof er geen is. Zoek naar een kleine verhoging of een lichtsensorgebied onder het scherm: de knop zit er vaak vlak naast. Via wifi heeft Mando TV nodig dat de tv één keer aan is geweest en verbonden is. Infrarood is de uitzondering: op een Android-telefoon met infraroodzender kan Mando TV een tv aanzetten die nooit is ingesteld, zolang je de telefoon op de tv richt. Infrarood is nieuw en werkt met de merken in de codelijst van de app.'),
      ('Gratis en Pro', 'De afstandsbediening kun je gratis downloaden en gebruiken, zonder advertenties en zonder abonnement. Mando TV Pro is een optionele eenmalige aankoop voor extra’s.'),
    ],
    marca=None,
    faq=[
      ('Kan ik een tv met mijn telefoon aanzetten als ik hem nooit heb ingesteld?', 'Niet via wifi. Een uitgeschakelde tv wordt alleen vanuit het netwerk wakker als het aanzetten via het netwerk eerder is ingeschakeld. Gebruik de eerste keer de knop op de tv. De uitzondering is een Android-telefoon met infraroodzender: Mando TV kan een tv zonder instelling via infrarood aanzetten als het merk in de codelijst staat of je “Ander merk of weet ik niet” kiest.'),
      ('Hoe zet ik een Samsung-tv aan zonder afstandsbediening?', 'Druk op de bedieningsknop onder het midden van het scherm of aan de achterkant bij een onderhoek. Zet daarna “Aan met mobiele telefoon” aan, zodat je telefoon hem de volgende keer kan aanzetten.'),
      ('Hoe zet ik een Roku TV aan zonder afstandsbediening?', 'Gebruik de knop op de tv, meestal onder het midden of aan de achterkant. Zet daarna “Snelle tv-start” aan onder Instellingen > Systeem > Stroom, zodat Mando TV hem vanaf je telefoon kan aanzetten.'),
      ('Waarom gaat mijn tv vanzelf aan als ik de console aanzet?', 'Dat is HDMI-CEC. Het is handig, en je kunt het in de tv-instellingen uitzetten als je dat liever hebt.'),
    ]),
  dict(clave='sony', corto='Sony-afstandsbediening', fecha='2026-11-23',
    titulo='Sony afstandsbediening-app voor telefoon en pc',
    desc='Mando TV bedient Sony Bravia-tv’s met Google TV of Android TV via wifi. Bèta-ondersteuning voor modellen van 2013 tot 2015 zonder Android.',
    h1='Zo bedien je je Sony-tv met je telefoon',
    intro='Nieuwere Sony Bravia Smart-tv’s gebruiken Google TV, oudere modellen vanaf 2015 Android TV. Mando TV bedient beide via je wifi vanaf je iPhone, Android-telefoon of Windows-pc. De app vervangt de originele afstandsbediening als die kwijt is of de batterijen leeg zijn.',
    pasos=[
      'Controleer of je Sony-tv het startscherm van Google TV of Android TV toont. Dat geldt voor de meeste Sony Bravia Smart-tv’s vanaf bouwjaar 2015.',
      'Zet je telefoon en de tv op hetzelfde wifi-netwerk.',
      'Open Mando TV en tik in de lijst op je Sony-tv.',
      'Voer de code van 6 tekens in die de tv op het scherm toont (alleen de eerste keer). Daarvoor heb je geen afstandsbediening nodig.',
      'Gebruik de pijltoetsen, OK, Terug, Start, volume en het toetsenbord.',
    ],
    extra=[
      ('Een Sony-tv vanaf je telefoon aanzetten', 'Sony-modellen met Google TV of Android TV kunnen via het netwerk worden wakker gemaakt als “Remote start” aanstaat. De optie vind je meestal onder Instellingen > Netwerk en internet > Remote start (het pad kan per model licht verschillen). Tik daarna in Mando TV op de tv terwijl hij uit staat, en de app zet hem aan.'),
      ('Waar de aan-/uitknop op een Sony zit', 'Bij de meeste Bravia-tv’s zit hij aan de achterkant, bij de linker- of rechteronderhoek, of aan een zijrand. Een korte druk zet de tv aan. Meer daarover vind je bij [Tv aanzetten zonder afstandsbediening](@turn-on).'),
      ('Oudere Sony-tv’s', 'Sony Bravia-tv’s van 2013 tot 2015 die geen Android gebruiken, worden in Mando TV in de bèta ondersteund. Dat is nieuw en kan nog kleine haperingen hebben. De tv toont een pincode van 4 cijfers die je in de app moet invoeren. Andere Sony-tv’s zonder Google TV of Android TV worden op dit moment niet ondersteund.'),
      ('Gratis en Pro', 'De afstandsbediening kun je gratis downloaden en gebruiken, zonder advertenties en zonder abonnement. Mando TV Pro is een optionele eenmalige aankoop voor extra’s.'),
    ],
    marca='android',
    faq=[
      ('Werkt Mando TV met Sony Bravia-tv’s?', 'Ja, met Sony-tv’s die Google TV of Android TV gebruiken. Dat omvat de meeste Sony Smart-tv’s vanaf bouwjaar 2015.'),
      ('Heb ik een Sony-app of een Google-account nodig?', 'Nee. Mando TV koppelt met de code op het tv-scherm en vraagt geen account.'),
      ('Werkt het met oudere Sony Bravia-tv’s zonder Android?', 'Ja, in de bèta, bij Bravia-modellen van 2013 tot 2015 zonder Android. Het koppelen gaat met een pincode van 4 cijfers die op de tv wordt getoond.'),
      ('Kan ik op mijn Sony-tv typen vanaf mijn telefoon?', 'Ja. Het toetsenbord van je telefoon is gratis en typt in het zoekveld van de tv en in andere tekstvelden. Voor YouTube heeft Mando TV ook een YouTube-toetsenbord: typ of zeg wat je wilt kijken en YouTube opent op de tv met de resultaten. Netflix accepteert alleen zijn eigen toetsenbord op het scherm, dus gebruik daar de pijltoetsen en OK.'),
    ]),
  dict(clave='tcl', corto='TCL-afstandsbediening', fecha='2026-11-23',
    titulo='TCL afstandsbediening-app voor telefoon en pc',
    desc='TCL-afstandsbediening kwijt? De meeste TCL-tv’s gebruiken Roku TV of Google TV. Mando TV bedient beide via wifi, zonder account en advertenties.',
    h1='Zo bedien je je TCL-tv met je telefoon',
    intro='TCL maakt de tv, maar de software is Roku TV of Google TV (bij oudere modellen Android TV). Mando TV bedient beide systemen en werkt als afstandsbediening voor je TCL-tv via wifi. Gratis, zonder account en advertenties.',
    pasos=[
      'Zoek uit welk systeem je TCL gebruikt. Toont het startscherm een eenvoudig raster van kanaaltegels, dan is het Roku TV. Ziet het eruit als Google TV of Android TV met rijen vol aanbevelingen, dan is het Google TV.',
      'Zet je telefoon en de TCL-tv op hetzelfde wifi-netwerk.',
      'Open Mando TV. De TCL verschijnt vanzelf in de lijst. Tik erop.',
      'Bij een TCL met Roku TV is verder niets nodig. Bij een TCL met Google TV voer je de code van 6 tekens in die de tv op het scherm toont (alleen de eerste keer).',
      'Gebruik de pijlen, OK, Terug, Start, volume en toetsenbord. Zet de tv aan via de app als je het aanzetten via het netwerk hebt ingeschakeld (zie hieronder).',
    ],
    extra=[
      ('Een TCL-tv vanaf je telefoon aanzetten', 'Zet bij TCL Roku TV “Snelle tv-start” aan onder Instellingen > Systeem > Stroom. Zoek bij TCL Google TV in de netwerk- of stroominstellingen naar een optie voor Wake on LAN, “Inschakelen via netwerk” of externe start. Sommige modellen bieden dit niet. Zet de tv in dat geval aan met de fysieke aan-/uitknop, meestal onderaan in het midden of aan de achterkant.'),
      ('Als je TCL niet verschijnt', 'Controleer of telefoon en tv op hetzelfde wifi-netwerk zitten. Routers met aparte 2,4 GHz- en 5 GHz-netwerken kunnen apparaten voor elkaar verbergen. Sta op de iPhone “Lokaal netwerk” toe voor Mando TV in de instellingen. Je kunt de tv ook toevoegen door zijn IP-adres in te voeren. Lees [Je telefoon vindt de tv niet](@not-found).'),
      ('Meer over je TCL', 'Voor TCL met Roku TV zie [Roku afstandsbediening-app](@roku), voor TCL met Google TV of Android TV [Android TV afstandsbediening-app](@android).'),
      ('Gratis en Pro', 'Pijltoetsen, OK, Terug, Start, volume, zenders, cijfers, toetsenbord, apps openen, ingangen wisselen en aan-/uitzetten zijn gratis, zonder advertenties en abonnement. Het touchpad, de spraakopdrachten, favoriete apps, routines en de slaaptimer horen bij Mando TV Pro, een eenmalige aankoop zonder abonnement.'),
    ],
    marca=None,
    faq=[
      ('Werkt Mando TV met elke TCL-tv?', 'Het werkt met TCL-tv’s met Roku TV, Google TV of Android TV, dus met de meeste TCL Smart-tv’s. Een TCL die geen Smart-tv is, kan niet via wifi worden bediend.'),
      ('Heb ik de TCL-app of een TCL-account nodig?', 'Nee. Mando TV maakt rechtstreeks verbinding via je wifi thuis en heeft geen account nodig.'),
      ('Mijn TCL vraagt om een code. Waar staat die?', 'TCL-modellen met Google TV en Android TV tonen een code van 6 tekens op het scherm. Voer hem precies zo in bij Mando TV. Een TCL met Roku TV vraagt niet om een code.'),
    ]),
  dict(clave='hisense', corto='Hisense-afstandsbediening', fecha='2026-11-23',
    titulo='Hisense afstandsbediening-app: wat werkt op je telefoon',
    desc='Hisense-afstandsbediening met Mando TV: bediening voor VIDAA, Roku TV, Google TV en Fire TV via wifi. Eerlijk overzicht van wat werkt.',
    h1='Hisense afstandsbediening-app: wat werkt en wat niet',
    intro='Hisense-tv’s zijn van binnen niet allemaal gelijk. Afhankelijk van het model gebruiken ze het eigen VIDAA-systeem van Hisense, Roku TV, Google TV of Fire TV. Mando TV werkt als afstandsbediening voor Hisense op alle vier de systemen, met een uitzondering bij enkele nieuwere VIDAA-modellen. Hier zie je hoe je herkent welk systeem je hebt en wat je kunt verwachten.',
    pasos=[
      'Controleer welk systeem je Hisense gebruikt. VIDAA is de eigen interface van Hisense. Roku TV toont een raster van kanaaltegels. Google TV toont rijen met aanbevelingen. Fire TV toont het Fire TV-startscherm met Amazon-rijen.',
      'Zet je telefoon en de Hisense-tv op hetzelfde wifi-netwerk.',
      'Open Mando TV. De tv verschijnt vanzelf in de lijst. Tik erop.',
      'VIDAA- en Fire TV-modellen tonen mogelijk een pincode van vier cijfers; Google TV toont een code van zes tekens. Voer hem in de app in. Roku TV vraagt nergens om. Dat doe je maar één keer.',
      'Gebruik de pijlen, OK, Terug, Start, volume en toetsenbord vanaf je telefoon.',
    ],
    extra=[
      ('Hisense met Roku TV of Google TV', 'Die werken volledig als elke andere Roku- of Google TV-tv. Details op de pagina’s [Roku afstandsbediening-app](@roku) en [Android TV afstandsbediening-app](@android).'),
      ('Hisense met Fire TV', 'De ondersteuning voor Fire TV is nieuw in Mando TV. Werk de app bij naar de nieuwste versie uit je store. Hoe het koppelen met pincode werkt, staat op de pagina [Fire TV afstandsbediening-app](@firetv). Werkt er iets niet zoals verwacht, schrijf ons dan via de helppagina en noem je model.'),
      ('Hisense met VIDAA', 'De meeste VIDAA-modellen werken: toetsen, volume, toetsenbord, apps en ingangen. Enkele nieuwere VIDAA-modellen accepteren alleen de officiële Hisense-app. Mando TV herkent dat bij het verbinden en zegt het je duidelijk, in plaats van stilzwijgend te falen. In dat geval zijn de Hisense-app voor je model, de toetsen op de tv of de originele afstandsbediening de juiste weg.'),
      ('Een Hisense vanaf je telefoon aanzetten', 'Zet bij Hisense Roku TV “Snelle tv-start” aan onder Instellingen > Systeem > Stroom. Zoek bij Google TV naar een optie voor Wake on LAN of “Inschakelen via netwerk”. Bestaat die niet, gebruik dan de aan-/uitknop op de tv.'),
      ('Gratis en Pro', 'Pijltoetsen, OK, Terug, Start, volume, zenders, cijfertoetsen, toetsenbord, apps openen, ingangen wisselen en aan- of uitzetten zijn gratis, zonder advertenties en zonder abonnement. Het touchpad, de spraakopdrachten, favoriete apps, routines en de slaaptimer horen bij Mando TV Pro, een eenmalige aankoop zonder abonnement.'),
    ],
    marca=None,
    faq=[
      ('Werkt Mando TV met Hisense VIDAA?', 'Ja, met de meeste VIDAA-modellen. Enkele nieuwere accepteren alleen de officiële Hisense-app; Mando TV herkent dat en zegt het je. Hisense-tv’s met Roku TV, Google TV of Fire TV worden ook ondersteund.'),
      ('Hoe weet ik of mijn Hisense Roku TV, Google TV of Fire TV is?', 'Kijk naar het startscherm. Roku TV heeft een eenvoudig raster van tegels en een Roku-logo bij het opstarten. Google TV heeft rijen met aanbevelingen. Fire TV heeft het startscherm van Amazon Fire TV. De modelnaam onder Instellingen > Info geeft ook uitsluitsel.'),
      ('Heb ik een Hisense- of Google-account nodig?', 'Nee. Mando TV maakt rechtstreeks verbinding via je wifi thuis en heeft geen eigen account.'),
    ]),
  dict(clave='philips', corto='Philips-afstandsbediening', fecha='2026-11-23',
    titulo='Philips afstandsbediening-app: Roku TV, Google TV, Android TV',
    desc='Mando TV bedient Philips-tv’s met Roku TV, Google TV of Android TV via wifi, vanaf je telefoon of pc. Titan OS wordt niet ondersteund.',
    h1='Philips-tv’s bedienen met je telefoon',
    intro='Philips-tv’s gebruiken afhankelijk van land en bouwjaar verschillende systemen: Roku TV in de VS, Google TV of Android TV in veel landen en Titan OS bij sommige nieuwere Europese modellen. Mando TV bedient de modellen met Roku TV, Google TV en Android TV via wifi.',
    pasos=[
      'Controleer het startscherm. Roku TV toont een raster van tegels. Google TV en Android TV tonen rijen met aanbevelingen van Google. Titan OS heeft een eigen startscherm.',
      'Zet je telefoon en de tv op hetzelfde wifi-netwerk.',
      'Open Mando TV en tik in de lijst op je Philips-tv.',
      'Roku TV vraagt nergens om. Google TV en Android TV tonen een code van 6 tekens: voer die één keer in de app in.',
      'Gebruik de pijltoetsen, OK, Terug, Start, volume en toetsenbord.',
    ],
    extra=[
      ('Philips Roku TV', 'Werkt als elke Roku-tv. Om hem vanaf je telefoon aan te zetten, zet je “Snelle tv-start” aan onder Instellingen > Systeem > Stroom. Meer op de pagina [Roku afstandsbediening-app](@roku).'),
      ('Philips met Google TV of Android TV', 'Omvat veel Ambilight-modellen. Ze koppelen met de code op het scherm. Om ze vanaf je telefoon aan te zetten, zoek je in de netwerk- of stroominstellingen naar Wake on LAN of “Inschakelen via netwerk”. Bij sommige modellen ontbreekt die optie. Meer op de pagina [Android TV afstandsbediening-app](@android).'),
      ('Oudere Philips-tv’s zonder Android', 'Philips-tv’s van 2011 tot 2015 die geen Android gebruiken, worden in Mando TV in de bèta ondersteund. Dat is nieuw en vraagt geen koppelcode.'),
      ('Philips met Titan OS', 'Titan OS is een ander systeem dat Mando TV nu niet bedient, en dat zeggen we liever duidelijk. Nieuwere Philips-modellen zonder Android vallen er ook niet onder.'),
      ('Gratis en Pro', 'De afstandsbediening kun je gratis downloaden en gebruiken, zonder advertenties en zonder abonnement. Mando TV Pro is een optionele eenmalige aankoop voor extra’s.'),
    ],
    marca=None,
    faq=[
      ('Werkt Mando TV met Philips-tv’s?', 'Met Philips-tv’s die Roku TV, Google TV of Android TV gebruiken wel, en in de bèta met Philips-tv’s van 2011 tot 2015 zonder Android. Modellen met Titan OS worden niet ondersteund.'),
      ('Bedient Mando TV Ambilight?', 'Mando TV is een afstandsbediening: het stuurt de toetsen door, zodat je met de pijlen en OK bij de Ambilight-instellingen komt. Aparte Ambilight-bediening is er niet.'),
      ('Heb ik een Philips- of Google-account nodig?', 'Nee. Mando TV maakt verbinding via je wifi thuis en heeft geen account nodig.'),
    ]),
]
OTRAS_GUIAS += [
  ('no-sub', 'Een afstandsbediening-app zonder abonnement en zonder advertenties'),
  ('roku-app-alt', 'Alternatief voor de Roku app: één voor alle tv’s'),
  ('lg-thinq', 'Alternatief voor de LG ThinQ app voor je LG-tv'),
  ('smartthings', 'SmartThings-alternatief voor Samsung-tv’s'),
  ('googletv-alt', 'Alternatief voor de Google TV-afstandsbediening op je telefoon'),
  ('windows', 'Afstandsbediening-app voor de Windows-pc'),
  ('iphone', 'Afstandsbediening-app voor iPhone: één voor alle tv’s'),
  ('firetv', 'Fire TV-afstandsbediening voor je telefoon of pc'),
  ('firetv-lost', 'Fire TV-afstandsbediening kwijt: zo gebruik je je telefoon'),
  ('turn-on', 'Zo zet je een tv aan zonder afstandsbediening'),
  ('sony', 'Zo bedien je je Sony-tv met je telefoon'),
  ('tcl', 'Zo bedien je je TCL-tv met je telefoon'),
  ('hisense', 'Hisense afstandsbediening-app: wat werkt en wat niet'),
  ('philips', 'Philips-tv’s bedienen met je telefoon'),
]
# <<< guías traídas del inglés
