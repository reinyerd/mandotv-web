# Textos en noruego bokmål (du) de mandotv.app. Los usa generar_idiomas.py. Escritos para las búsquedas de Noruega.
# Las claves de las páginas (lg, lost-tv, ...) y sus rutas están en idiomas_sitio.py y herramientas/rutas/nb.json.
# Los nombres de menús de cada marca (LG, Samsung, Roku, Android TV, iPhone) son los mismos que usa la app en noruego
# (lib/l10n/app_nb.arb del proyecto de la app).

UI = dict(
  locale='nb_NO',
  aria_home='Mando TV, forside', aria_main='Hovedmeny', nav_que='Funksjoner', nav_ayuda='Hjelp', nav_contacto='Kontakt',
  asunto='Hei%20Mando%20TV', inicio='Forside', privacidad='Personvern', aria_pie='Bunntekst', aria_ruta='Brødsmulesti',
  aria_marcas='Merker og guider', hecho='Laget i Chile',
  aviso='Mando TV er en uavhengig app. Den har ingen tilknytning til TV-produsentene som nevnes, og heller ikke til Google, Amazon, Apple eller Roku, og er ikke støttet av dem. Varemerkene tilhører sine eiere og brukes bare for å vise hva appen fungerer med. Android TV og Google TV er varemerker som tilhører Google LLC. Apple TV er et varemerke som tilhører Apple Inc.',
  bajar='Last ned gratis', descarga='Last ned på', anticipada='Tidlig tilgang på',
  apple_aria='Last ned Mando TV gratis i App Store', ms_aria='Last ned Mando TV gratis i Microsoft Store',
  gp_aria='Tidlig tilgang til Mando TV på Google Play for Android', aria_desc='Last ned Mando TV',
  b_como_btn='Slik kobler du til', b_tiendas_label='Tilgjengelig i appbutikkene',
  b_nota='iPhone, iPad, Mac, Android og Windows. Gratis nedlasting, uten reklame. Pro er et engangskjøp, uten abonnement.',
  b_compat='Kompatible TV-er', b_otras='Andre merker', b_otras_p='Mando TV styrer alle disse merkene med den samme appen:',
  g_guias='Guider', g_ver='Se trinnene', g_pasos='Steg for steg', g_hazlo='Slik gjør du det med Mando TV',
  g_tiendas='Mando TV er en universell fjernkontroll for TV-en din. Last den ned gratis, uten reklame og uten konto. Pro er et valgfritt engangskjøp, uten abonnement. For iPhone, iPad, Windows og Android:',
  g_nota='Android: gratis tidlig tilgang på Google Play. <a href="{enlace}">Bli med i to enkle steg</a> og hjelp oss å nå butikken.',
  g_mas_pagina='Du finner mer informasjon på siden {enlace}.', g_mas_marca='Mer informasjon per merke:',
  g_faq='Vanlige spørsmål', g_mas='Flere guider', g_todas='Alle guider', g_ayuda='Hjelp og støtte',
  g_idiomas='Denne guiden på andre språk',
)

# Pie de página y listas de marcas/guías: (clave, texto)
PIE = [
  ('samsung', 'Samsung fjernkontroll'),
  ('lg', 'LG fjernkontroll'),
  ('roku', 'Roku fjernkontroll'),
  ('android', 'Android TV fjernkontroll'),
  ('guias', 'Alle guider'),
  ('lost-tv', 'Mistet fjernkontrollen'),
  ('lost-lg', 'Mistet LG-fjernkontrollen'),
  ('lg-on', 'Slå på LG-TV med mobilen'),
  ('hdmi', 'Bytt HDMI-inngang uten fjernkontroll'),
  ('androidtv', 'Android TV uten fjernkontroll'),
  ('console', 'TV og HDMI for spillkonsoll uten fjernkontroll'),
  ('samsung-lost', 'Samsung-TV uten fjernkontroll'),
  ('roku-lost', 'Mistet Roku-fjernkontrollen'),
  ('roku-403', 'Roku-appen fungerer ikke'),
  ('androidtv-code', 'Android TV paringskode'),
  ('not-found', 'Mobilen finner ikke TV-en'),
  ('wifi', 'Mobilen som fjernkontroll via Wi-Fi'),
  ('pc', 'Styr TV-en fra PC-en'),
]
NOMBRE_OTRA = {'lg': 'LG fjernkontroll-app', 'samsung': 'Samsung fjernkontroll-app', 'roku': 'Roku fjernkontroll-app',
               'android': 'Android TV og Google TV fjernkontroll-app'}
PAGINA_MARCA = {'lg': 'LG fjernkontroll-app', 'samsung': 'Samsung fjernkontroll-app', 'roku': 'Roku fjernkontroll-app',
                'android': 'Android TV fjernkontroll-app'}

OTRAS_GUIAS = [
  ('lg-on', 'Slå på LG-TV med mobilen'),
  ('lost-tv', 'Mistet fjernkontrollen: Dette kan du gjøre'),
  ('lost-lg', 'Mistet LG-fjernkontrollen: Slik bruker du mobilen'),
  ('hdmi', 'Bytt HDMI-inngang på TV-en uten fjernkontroll'),
  ('androidtv', 'Android TV uten fjernkontroll: Slik bruker du mobilen'),
  ('console', 'Slå på TV-en og bytt til HDMI for spillkonsollen, uten fjernkontroll'),
  ('samsung-lost', 'Samsung-TV uten original fjernkontroll: Slik bruker du mobilen'),
  ('roku-lost', 'Mistet Roku-fjernkontrollen: Slik bruker du mobilen'),
  ('roku-403', 'Roku-appen fungerer ikke: Slik fikser du feil 403'),
  ('androidtv-code', 'Android TV ber om en paringskode: Dette må du gjøre'),
  ('not-found', 'Mobilen finner ikke TV-en: Dette bør du sjekke'),
  ('wifi', 'Slik bruker du mobilen som fjernkontroll via Wi-Fi'),
  ('pc', 'Slik styrer du TV-en med en Windows-PC'),
]

INDICE = dict(
  titulo='Guider: Styr TV-en med mobilen | Mando TV',
  desc='Guider steg for steg: bruk mobilen eller PC-en som fjernkontroll, slå på TV-en, bytt HDMI og løs problemer med Samsung, LG og Roku.',
  h1='Guider: Bruk mobilen som fjernkontroll',
  intro='Enkle steg for å koble fjernkontrollen til Samsung-, LG-, Roku- eller Android TV-en din med Mando TV, slå på TV-en og løse problemer.',
  h2_guias='Alle guider', h2_marcas='Fjernkontroll-app per merke',
  marcas_extra=[('sony', 'Sony fjernkontroll-app'), ('philips', 'Philips fjernkontroll-app')],
)

MARCAS = [
  dict(clave='lg', color='#e0457b', corto='LG',
    titulo='LG TV fjernkontroll-app for mobilen, gratis | Mando TV',
    desc='Mobilen eller PC-en som LG TV fjernkontroll for webOS, via Wi-Fi. Knapper, tastatur, apper, innganger og påslåing gratis; peker med Pro.',
    h1='LG TV fjernkontroll som app på mobilen',
    intro='Mando TV er en fjernkontroll-app for LG-TV-er: Den gjør mobilen eller datamaskinen din til fjernkontroll for LG Smart-TV-en med webOS, via Wi-Fi hjemme. Det er til hjelp når du har mistet fjernkontrollen, batteriene er tomme eller du bare vil skrive raskere.',
    compat='LG Smart-TV-er med webOS (de fleste LG Smart-TV-modeller siden 2014). Fungerer med LED-, NanoCell-, QNED- og OLED-TV-er. Eldre LG Smart-TV-er med NetCast (2011 til 2014, før webOS) støttes nå i beta: De parer seg med den 6-sifrede nøkkelen som TV-en viser.',
    h2=dict(funciones='Dette kan du gjøre med LG-TV-en din', como='Slik kobler du LG-TV-en til Mando TV',
            encender='Slå på LG-TV-en med mobilen', preguntas='Spørsmål om LG', guias='Guider for LG'),
    funciones=[
      ('Alle knappene', 'Piltaster, OK, Tilbake, Hjem, volum, kanaler, lyd av og avspilling.'),
      ('Peker som på Magic Remote (Pro)', 'Flytt pilen over skjermen med fingeren, akkurat som med LG Magic Remote.'),
      ('Tastatur', 'Skriv i YouTube, Netflix eller nettleseren på TV-en med tastaturet på mobilen.'),
      ('Apper og innganger', 'Åpne appene dine og bytt til HDMI, direkte-TV, AirPlay eller Screen Share.'),
      ('Lydutgang (Pro)', 'Bytt mellom høyttalerne i TV-en og lydplanken din.'),
      ('Slå på TV-en', 'Når den er av, slår Mando TV den på via nettverket og kobler seg til av seg selv.'),
    ],
    pasos=[
      'Koble mobilen og TV-en til det samme Wi-Fi-nettverket.',
      'Åpne Mando TV: LG-TV-en din dukker opp i listen av seg selv. Trykk på den.',
      'På TV-en kommer det en forespørsel om tillatelse. Bekreft den med den vanlige fjernkontrollen (bare første gang).',
    ],
    encender='Aktiver «Slå på TV-en med mobil» (på noen modeller heter den «Slå på via Wi-Fi»). Du finner den under Innstillinger > Generelt > Enheter > Eksterne enheter (på eldre modeller Tilkobling > Administrasjon av mobiltilkobling). Etterpå spør appen deg, når du trykker på den avslåtte TV-en i Mando TV, om den skal slå den på, og kobler seg til av seg selv.',
    faq=[
      ('Trenger jeg Magic Remote for å bruke Mando TV?', 'Bare første gang, for å bekrefte forespørselen på skjermen. Etter det holder det med mobilen.'),
      ('Erstatter Mando TV appen LG ThinQ?', 'For å styre TV-en, ja: Du trenger verken LG-konto eller å registrere TV-en. Mando TV kobler seg direkte via Wi-Fi-nettverket ditt.'),
      ('Kan jeg slå på LG-TV-en med mobilen?', 'Ja, hvis du har slått på «Slå på TV-en med mobil» på TV-en og har koblet til én gang mens TV-en var på.'),
      ('Fungerer det med eldre LG-TV-er fra før webOS?', 'I beta, ja, med LG NetCast Smart-TV-er fra 2011 til 2014. De parer seg med den 6-sifrede nøkkelen som TV-en viser. Funksjonen er ny og kan fortsatt ha noen skjønnhetsfeil.'),
    ],
    guias=[('lg-on', 'Slik slår du på en LG-TV med mobilen'),
           ('lost-lg', 'Mistet LG-fjernkontrollen: Slik bruker du mobilen'),
           ('hdmi', 'Bytt HDMI-inngang på TV-en uten fjernkontroll'),
           ('guias', 'Alle guider for å styre TV-en med mobilen')]),
  dict(clave='samsung', color='#3d7bff', corto='Samsung',
    titulo='Samsung TV fjernkontroll-app for mobilen | Mando TV',
    desc='Mobilen eller PC-en som Samsung TV fjernkontroll for Tizen, via Wi-Fi. Knapper, tastatur, apper og påslåing gratis; touchpad med Pro. Uten reklame.',
    h1='Samsung TV fjernkontroll som app på mobilen',
    intro='Mando TV er en fjernkontroll-app for Samsung-TV-er: Den gjør mobilen eller datamaskinen din til fjernkontroll for Samsung Smart-TV-en, via Wi-Fi hjemme. Du trenger verken Samsung-konto eller å registrere TV-en.',
    compat='Samsung Smart-TV-er med Tizen, fra 2016 og nyere (serier som Crystal UHD, QLED, Neo QLED, The Frame og OLED).',
    h2=dict(funciones='Dette kan du gjøre med Samsung-TV-en din', como='Slik kobler du Samsung-TV-en til Mando TV',
            encender='Slå på Samsung-TV-en med mobilen', preguntas='Spørsmål om Samsung', guias='Guider for Samsung'),
    funciones=[
      ('Alle knappene', 'Piltaster, OK, Tilbake, Hjem, volum, kanaler, lyd av og kilde.'),
      ('Touchpad (Pro)', 'Dra fingeren over menyene uten å lete etter piltastene.'),
      ('Tastatur', 'Skriv søkeord og passord med tastaturet på mobilen.'),
      ('Apper', 'Åpne Netflix, YouTube, Prime Video og de andre appene dine med ett trykk.'),
      ('Slå på TV-en', 'Når den er av, slår Mando TV den på via nettverket og kobler seg til av seg selv.'),
      ('Uten konto', 'Tilkoblingen går direkte via Wi-Fi-nettverket ditt, uten omvei via internett.'),
    ],
    pasos=[
      'Koble mobilen og TV-en til det samme Wi-Fi-nettverket.',
      'Åpne Mando TV: Samsung-TV-en din dukker opp i listen av seg selv. Trykk på den.',
      'TV-en spør om du vil tillate tilkoblingen. Velg «Tillat» med fjernkontrollen (bare første gang).',
    ],
    encender='Slå på «Slå på med mobil» på Samsung-TV-en under Innstillinger > Generelt > Nettverk > Ekspertinnstillinger. Etterpå spør appen deg, når du trykker på den avslåtte TV-en i Mando TV, om den skal slå den på, og kobler seg til av seg selv.',
    faq=[
      ('Jeg avslo tillatelsen ved en feil. Hva gjør jeg?', 'Gå på TV-en til Innstillinger > Generelt > Ekstern enhetsbehandling > Enhetstilkoblingsbehandling og sett Mando TV til tillatt.'),
      ('Erstatter Mando TV SmartThings?', 'For å styre TV-en, ja, og det uten Samsung-konto. Mando TV kobler seg direkte via Wi-Fi-nettverket ditt.'),
      ('Fungerer det med eldre Samsung-TV-er?', 'Det fungerer med Samsung-TV-er med Tizen, fra 2016 og nyere. Tidligere modeller bruker et annet system som vi ikke støtter ennå.'),
    ],
    guias=[('samsung-lost', 'Samsung-TV uten original fjernkontroll: Slik bruker du mobilen'),
           ('smartthings', 'SmartThings-alternativ for Samsung-TV-er'),
           ('turn-on', 'Slik slår du på en TV uten fjernkontroll'),
           ('hdmi', 'Bytt HDMI-inngang på TV-en uten fjernkontroll'),
           ('guias', 'Alle guider for å styre TV-en med mobilen')]),
  dict(clave='roku', color='#a77bff', corto='Roku',
    titulo='Roku fjernkontroll-app for mobilen, gratis | Mando TV',
    desc='Mobilen eller PC-en som Roku fjernkontroll for Roku TV og Roku-spillere, via Wi-Fi. Knapper, tastatur, kanaler, innganger og påslåing gratis.',
    h1='Roku fjernkontroll som app på mobilen',
    intro='Mando TV er en fjernkontroll-app for Roku: Den gjør mobilen eller datamaskinen din til fjernkontroll for Roku-en din, via Wi-Fi hjemme. Den fungerer med Roku TV-er og med Roku-spillere som kobles til HDMI-porten.',
    compat='Roku TV-er (TCL, Hisense, Philips, Sharp, JVC og andre) og Roku-spillere (Express, Streaming Stick, Ultra).',
    h2=dict(funciones='Dette kan du gjøre med Roku-en din', como='Slik kobler du Roku-en til Mando TV',
            encender='Slå på Roku-en med mobilen', preguntas='Spørsmål om Roku', guias='Guider for Roku'),
    funciones=[
      ('Alle knappene', 'Piltaster, OK, Tilbake, Hjem, volum, lyd av, gjenta og avspilling.'),
      ('Tastatur', 'Skriv søkeord i Roku-kanaler med tastaturet på mobilen.'),
      ('Kanaler', 'Åpne Netflix, YouTube og de andre Roku-kanalene dine med ett trykk.'),
      ('Innganger', 'På en Roku TV bytter du til HDMI, antenne eller AV i appen.'),
      ('Slå på TV-en', 'På Roku TV-er med hurtigstart slår Mando TV dem på fra mobilen.'),
      ('Uten paring', 'Roku ber ikke om kode: Trykk på den i listen, så er du koblet til.'),
      ('Få fjernkontrollen til å ringe', 'Har Roku-fjernkontrollen en høyttaler, som Roku Voice Remote Pro, får Mando TV den til å ringe slik at du finner den. Gratis, og Roku-en må være på.'),
    ],
    pasos=[
      'Koble mobilen og Roku-en til det samme Wi-Fi-nettverket.',
      'Åpne Mando TV: Roku-en din dukker opp i listen av seg selv. Trykk på den.',
      'Hvis tilkoblingen ikke fungerer, går du på Roku-en til Innstillinger > System > Avanserte systeminnstillinger > Kontroll fra mobilapper og setter nettverkstilgang til Standard eller Permissive (på nyere Roku-programvare setter du Kontroll fra mobilapper til Aktivert).',
    ],
    encender='På Roku TV-er slår du på «TV-hurtigstart» under Innstillinger > System > Strøm. Roku-spillere som er koblet til en annen TV, kan ikke slås på på denne måten. Etterpå spør appen deg, når du trykker på den avslåtte TV-en i Mando TV, om den skal slå den på, og kobler seg til av seg selv.',
    faq=[
      ('Fungerer det med Roku Express eller Streaming Stick?', 'Ja. Alle Roku-spillere og Roku TV-er styres på samme måte.'),
      ('Mando TV finner ikke Roku-en min. Hva gjør jeg?', 'Sjekk at begge er på det samme Wi-Fi-nettverket og at «Kontroll fra mobilapper» ikke er slått av på Roku-en. Du kan også legge den til via IP-adressen.'),
      ('Trenger jeg en Roku-konto?', 'Nei. Mando TV kobler seg direkte via Wi-Fi-nettverket ditt.'),
    ],
    guias=[('roku-403', 'Roku-appen fungerer ikke (feil 403)'),
           ('roku-lost', 'Mistet Roku-fjernkontrollen: Slik bruker du mobilen'),
           ('tcl', 'TCL fjernkontroll-app'),
           ('hisense', 'Hisense fjernkontroll-app'),
           ('philips', 'Philips fjernkontroll-app'),
           ('guias', 'Alle guider for å styre TV-en med mobilen')]),
  dict(clave='android', color='#2fbf8f', corto='Android TV og Google TV',
    titulo='Android TV fjernkontroll-app for mobilen | Mando TV',
    desc='Mobilen eller PC-en som Android TV fjernkontroll (Sony, TCL, Xiaomi), via Wi-Fi. Knapper, tastatur, apper og påslåing gratis; touchpad med Pro.',
    h1='Android TV fjernkontroll som app på mobilen',
    intro='Mando TV er en fjernkontroll-app for Android TV: Den gjør mobilen eller datamaskinen din til fjernkontroll for Android TV- eller Google TV-en din, via Wi-Fi hjemme. Den fungerer også fra iPhone og fra Windows.',
    compat='TV-er med Google TV eller Android TV fra Sony, Philips, TCL, Hisense, Sharp, Xiaomi, Toshiba, Panasonic, Haier, Skyworth, JVC, Thomson, Motorola, OnePlus, iFFALCON, Kogan, Vu og andre merker, i tillegg til Chromecast med Google TV, Google TV Streamer, onn. og Nvidia Shield. Noen av disse merkene selger også modeller med et annet system: Viser TV-en startskjermen til Google TV eller har den Google Play Store, styrer Mando TV den.',
    h2=dict(funciones='Dette kan du gjøre med Android TV og Google TV', como='Slik kobler du Android TV og Google TV til Mando TV',
            encender='Slå på Android TV og Google TV med mobilen', preguntas='Spørsmål om Android TV og Google TV', guias='Guider for Android TV og Google TV'),
    funciones=[
      ('Alle knappene', 'Piltaster, OK, Tilbake, Hjem, volum, lyd av og avspilling.'),
      ('Touchpad (Pro)', 'Dra fingeren for å navigere raskt i menyene til Google TV.'),
      ('Tastatur', 'Skriv søkeord og passord med tastaturet på mobilen.'),
      ('Apper', 'Åpne YouTube, Netflix, Disney+ og de andre appene dine med ett trykk.'),
      ('Slå på TV-en', 'På modeller som kan slås på via nettverket, slår Mando TV på TV-en og kobler seg til av seg selv.'),
      ('iPhone, Android og PC', 'Det fungerer likt på alle mobiler og alle datamaskiner.'),
    ],
    pasos=[
      'Koble mobilen og TV-en til det samme Wi-Fi-nettverket.',
      'Åpne Mando TV: Android TV-en din dukker opp i listen av seg selv. Trykk på den.',
      'TV-en viser en kode med 6 tegn. Skriv den inn i Mando TV (bare første gang).',
    ],
    encender='Det avhenger av produsenten. Se i nettverks- eller strøminnstillingene etter «Wake on LAN», «Slå på via nettverk», «Nettverksstandby» eller «Remote start». Noen modeller har ikke dette alternativet. Etterpå spør appen deg, når du trykker på den avslåtte TV-en i Mando TV, om den skal slå den på, og kobler seg til av seg selv.',
    faq=[
      ('Fungerer det med Chromecast med Google TV?', 'Ja, paringen skjer med koden på 6 tegn som vises på skjermen.'),
      ('Hva er forskjellen fra Google TV-appen?', 'Mando TV trenger ingen Google-konto, fungerer også på Windows og styrer TV-er fra LG, Samsung og Roku med den samme appen.'),
      ('Koden vises ikke på skjermen. Hva gjør jeg?', 'Lukk Mando TV, åpne appen på nytt og trykk på TV-en igjen. Sjekk at TV-en ikke er i en dyp strømsparemodus.'),
    ],
    guias=[('androidtv-code', 'Android TV ber om en paringskode: Dette må du gjøre'),
           ('androidtv', 'Android TV uten fjernkontroll: Slik bruker du mobilen'),
           ('googletv-alt', 'Alternativ til Google TV-fjernkontrollen på mobilen'),
           ('sony', 'Sony fjernkontroll-app'),
           ('tcl', 'TCL fjernkontroll-app'),
           ('hisense', 'Hisense fjernkontroll-app'),
           ('philips', 'Philips fjernkontroll-app'),
           ('guias', 'Alle guider for å styre TV-en med mobilen')]),
]

GUIAS = [
  dict(clave='lost-tv', corto='Mistet fjernkontrollen',
    titulo='Mistet fjernkontrollen? Styr TV-en med mobilen',
    desc='Mistet fjernkontrollen? Slå på TV-en med knappen på selve TV-en og bruk mobilen som fjernkontroll. Steg for LG, Samsung, Roku og Android TV. Gratis.',
    h1='Mistet fjernkontrollen? Dette kan du gjøre nå',
    intro='Å miste fjernkontrollen skjer i alle hjem: Den er borte akkurat når du vil se noe. Den gode nyheten er at mobilen kan erstatte fjernkontrollen via Wi-Fi hjemme. Her ser du hva du kan gjøre, steg for steg.',
    pasos=[
      'Slå på TV-en med knappen på selve TV-en. Den sitter nesten alltid nederst på midten eller bak, nær et hjørne. Noen ganger er det én enkelt knapp, noen ganger en liten joystick.',
      'Koble mobilen til det samme Wi-Fi-nettverket som TV-en.',
      'Last ned Mando TV, som er gratis og ikke krever konto, og åpne appen. TV-en din dukker opp i listen av seg selv. Trykk på den.',
      'Bekreft tilkoblingen for merket ditt. På LG og Samsung viser TV-en en forespørsel: Bekreft den med knappen eller joysticken på selve TV-en. På Android TV og Google TV skriver du inn en kode med 6 tegn som vises på skjermen. Roku spør ikke om noe.',
      'Ferdig. Piltaster, OK, Tilbake, Hjem, volum, kanaler og tastatur er gratis.',
      'Til neste gang: Slå på påslåing via nettverket i innstillingene på TV-en (du finner guiden for merket ditt nedenfor). Da kan du slå på TV-en fra mobilen uten å røre den.',
    ],
    extra=[
      ('Velg guiden for merket ditt', 'LG: [Mistet LG-fjernkontrollen](@lost-lg). Android TV og Google TV: [Android TV uten fjernkontroll](@androidtv). Samsung: [Samsung-TV uten fjernkontroll](@samsung-lost). Roku: [Mistet Roku-fjernkontrollen](@roku-lost).'),
      ('Hvis TV-en ikke lar seg slå på med knappen', 'Før du leter etter en annen fjernkontroll, sjekk at kabelen sitter godt og at stikkontakten har strøm. Gjør knappen på TV-en ingenting, er det TV-en som har problemet og ikke fjernkontrollen.'),
      ('Hvis fjernkontrollen rett og slett ikke virker lenger', 'Prøv nye batterier. Du kan sjekke om den fortsatt sender signal ved å rette den mot mobilkameraet og trykke på en knapp: På mange mobiler ser du da et fiolett lys på skjermen. Ser du lyset og TV-en ikke reagerer, kan sensoren på TV-en være tildekket.'),
      ('Hvis du har byttet ruter og TV-en ikke har Wi-Fi lenger', 'Uten fjernkontroll er det vanskeligere å koble TV-en til det nye nettverket. Det enkleste er å koble TV-en til ruteren med en nettverkskabel. Du kan også opprette et Wi-Fi-nettverk med samme navn og passord som før: TV-en kobler seg som regel til av seg selv.'),
      ('Hva som er gratis og hva som er Pro', 'Å slå TV-en på og av, piltaster, OK, volum, kanaler, siffertaster, tastatur, åpning av apper og bytte av inngang er gratis. Touchpad, tale og rutiner hører til Mando TV Pro, et engangskjøp uten abonnement.'),
    ],
    marca=None,
    faq=[
      ('Kan jeg slå på TV-en med mobilen hvis jeg aldri har koblet til?', 'Første gang slår du den på med knappen på TV-en. Når du har koblet til mobilen og slått på påslåing via nettverket i innstillingene på TV-en, kan du slå den på fra appen.'),
      ('Må jeg kjøpe en ny fjernkontroll?', 'Ikke nødvendigvis. Med Mando TV får du knapper, volum, tastatur og påslåing gratis. Hvis du likevel vil ha en ekte fjernkontroll, søk etter den nøyaktige modellen på TV-en din.'),
      ('Fungerer det hvis TV-en ikke har Wi-Fi?', 'Som regel nei. Mobilen og TV-en må vanligvis være på det samme Wi-Fi-nettverket. Unntak er infrarød på Android-mobiler med infrarød sender, som også styrer TV-er uten smartfunksjon, og Bluetooth i betaen fra Android 9, som fungerer helt uten Wi-Fi med Google TV, Android TV og Fire TV.'),
    ]),
  dict(clave='lost-lg', corto='Mistet LG-fjernkontrollen',
    titulo='Mistet LG-fjernkontrollen? Bruk mobilen',
    desc='Ingen LG-fjernkontroll? Slå på TV-en med knappen på TV-en, bekreft forespørselen og bruk mobilen via Wi-Fi. Uten LG-konto, uten reklame.',
    h1='Mistet LG-fjernkontrollen? Slik bruker du mobilen',
    intro='Hvis du har mistet LG-fjernkontrollen eller Magic Remote ikke virker lenger, erstatter mobilen den via Wi-Fi. Det fungerer med LG-TV-er med webOS, altså nesten alle LG Smart-TV-er siden 2014. Du trenger verken LG-konto eller ThinQ-appen.',
    pasos=[
      'Slå på TV-en med knappen nederst under LG-logoen eller med knappen bak på TV-en. På mange modeller er den en joystick: Trykk på den for å åpne menyen og flytt den for å velge.',
      'Koble mobilen til det samme Wi-Fi-nettverket som TV-en.',
      'Åpne Mando TV og trykk på LG-TV-en din i listen.',
      'TV-en viser en forespørsel om tillatelse. Bekreft den med joysticken eller knappen på TV-en. Hvis du har koblet til denne mobilen før, spør den ikke på nytt.',
      'Ferdig. Piltaster, OK, Tilbake, Hjem, volum, kanaler og tastatur er gratis. Pekeren er en Pro-funksjon.',
      'Når appen er koblet til, åpner du innstillingene med piltastene og OK og slår på «Slå på TV-en med mobil». Guiden [Slå på LG-TV med mobilen](@lg-on) viser hvor du finner alternativet.',
    ],
    extra=[
      ('Hvis TV-en ikke viser forespørselen', 'Kanskje er tillatelsen allerede lagret, eller mobilen er på et annet nettverk. Sjekk at begge er på det samme Wi-Fi-nettverket og at VPN er av. Dukker ikke TV-en opp i listen, hjelper [Mobilen finner ikke TV-en](@not-found) deg videre.'),
      ('Hvis TV-en har mistet Wi-Fi', 'Koble TV-en til ruteren med en nettverkskabel, så bruker den den av seg selv. Eller opprett et Wi-Fi-nettverk med samme navn og passord som før, for TV-en kobler seg som regel til av seg selv.'),
      ('Hvis TV-en står på en annen inngang', 'Trykk på Innganger på mobilen og velg HDMI-porten. Du finner mer i [Bytt HDMI-inngang på TV-en uten fjernkontroll](@hdmi).'),
    ],
    marca='lg',
    faq=[
      ('Trenger jeg Magic Remote for å bruke Mando TV?', 'Du trenger bare noe første gang for å bekrefte forespørselen, og da holder knappen eller joysticken på selve TV-en. Etter det bruker du bare mobilen.'),
      ('Trenger jeg LG ThinQ-appen?', 'Nei. Mando TV kobler seg direkte via Wi-Fi-nettverket ditt og krever ingen LG-konto.'),
      ('Kan jeg slå LG-TV-en av og på med mobilen?', 'Å slå av, ja. For å slå på må du ha slått på «Slå på TV-en med mobil» på TV-en og ha koblet til én gang mens TV-en var på.'),
    ]),
  dict(clave='hdmi', corto='Bytt HDMI uten fjernkontroll',
    titulo='Bytt HDMI-inngang uten fjernkontroll (Samsung, LG, Roku)',
    desc='Bytt HDMI-inngang uten fjernkontroll på Samsung, LG eller Roku: med knappen på TV-en eller med mobilen. Gratis å starte, uten reklame.',
    h1='Slik bytter du HDMI-inngang på TV-en uten fjernkontroll',
    intro='Spillkonsollen eller strømmespilleren er klar, men TV-en står på en annen inngang og fjernkontrollen er ikke å finne. For å bytte HDMI-inngang uten fjernkontroll har du to muligheter: knappen på selve TV-en eller mobilen. Her er stegene for Samsung, LG og Roku.',
    pasos=[
      'Prøv det enkleste først: Slå på konsollen eller spilleren. Hvis HDMI-CEC er slått på på TV-en (hos Samsung heter det Anynet+, hos LG SIMPLINK), bytter den til denne inngangen av seg selv.',
      'Bytter den ikke, bruker du knappen på selve TV-en, nederst på midten eller bak. På mange Samsung- og LG-TV-er er den en joystick og åpner en meny med Kilde eller Innganger.',
      'Velg inngangen i denne menyen: HDMI 1, HDMI 2 og så videre. Tallet er porten som kabelen sitter i.',
      'Hvis du heller vil bruke mobilen, kobler du den til det samme Wi-Fi-nettverket, åpner Mando TV og trykker på TV-en din.',
      'På LG og Roku trykker du på Innganger og velger HDMI-porten. På Samsung sender Innganger Kilde-knappen til TV-en, og du velger med piltastene og OK.',
      'Du kan også gå til inngangene fra startskjermen på TV-en med piltastene og OK. Avhengig av merke og årsmodell heter de Kilde, Tilkoblede enheter eller Innganger. På en Roku TV er det HDMI-rutene på startskjermen.',
    ],
    extra=[
      ('Samsung', 'Har menyen fra knappen på TV-en ikke noe punkt for Kilde, åpner du menyen på startskjermen med mobilen og leter til venstre etter Kilde eller Tilkoblede enheter. Du styrer den med piltastene og OK i Mando TV, som er gratis.'),
      ('LG', 'Trykk på joysticken på TV-en og finn Innganger. Med mobilen kan du også åpne inngangslisten i Mando TV og trykke på ønsket inngang.'),
      ('Roku TV', 'På startskjermen finnes det en rute for hver inngang, for eksempel HDMI 1 eller HDMI 2. Beveg deg med piltastene og åpne den med OK, gratis.'),
      ('Hvis det er en TV med Android TV eller Google TV', 'I Mando TV finnes ikke inngangslisten for Android TV ennå. Bruk inngangsknappen på selve TV-en, eller nå inngangene med piltastene og OK fra startskjermen. Har du ingen fjernkontroll og vil koble til, les [Android TV uten fjernkontroll](@androidtv).'),
      ('Mer hjelp', 'Slår TV-en seg ikke på i det hele tatt, eller vet du ikke hvor du skal begynne, les [Mistet fjernkontrollen](@lost-tv). For spilling på konsollen inneholder guiden [Slå på TV-en og bytt til HDMI for spillkonsollen, uten fjernkontroll](@console) HDMI-CEC-trikset.'),
    ],
    marca=None,
    faq=[
      ('Er det gratis å bytte HDMI-inngang?', 'Ja. Inngangslisten i Mando TV er gratis, akkurat som påslåing av TV-en og piltaster, OK og volum. Du når inngangene også via menyen på TV-en.'),
      ('Hvordan vet jeg hvilken HDMI-inngang jeg trenger?', 'Se på HDMI-portene på TV-en: Hver har et nummer. Velg den som kabelen fra konsollen eller spilleren sitter i.'),
      ('Hva om TV-en ikke slår seg på?', 'Slå den på med knappen på selve TV-en. Har du koblet til én gang og slått på påslåing via nettverket, kan du også slå den på fra mobilen.'),
    ]),
  dict(clave='androidtv', corto='Android TV uten fjernkontroll',
    titulo='Android TV uten fjernkontroll: Bruk mobilen',
    desc='Ingen Android TV- eller Google TV-fjernkontroll? Koble til mobilen med koden med 6 tegn på skjermen. Gratis, uten konto, uten reklame.',
    h1='Android TV uten fjernkontroll: Slik bruker du mobilen',
    intro='Hvis du har mistet fjernkontrollen til Android TV eller Google TV, eller batteriene er tomme, erstatter mobilen den. Det beste er at du ikke trenger fjernkontrollen for å koble til, for TV-en viser en kode på skjermen og du skriver den inn på mobilen. Det fungerer med TV-er fra Sony, Philips, TCL, Hisense, Sharp og Xiaomi med Android TV, med Chromecast med Google TV og med Nvidia Shield.',
    pasos=[
      'Slå på TV-en med knappen på selve TV-en. Den sitter nesten alltid nederst på midten eller bak, nær et hjørne.',
      'Koble mobilen til det samme Wi-Fi-nettverket som TV-en.',
      'Last ned Mando TV, som er gratis og ikke krever Google-konto, og åpne appen. Trykk på TV-en din i listen.',
      'TV-en viser en kode med 6 bokstaver og tall. Skriv den inn på mobilen og trykk på Pare. Du trenger ikke fjernkontrollen til dette.',
      'Nå kan du bruke piltaster, OK, Tilbake, Hjem, volum, lyd av og tastatur. De er gratis, det samme er applisten. Touchpad er Pro.',
      'For å slå på TV-en fra mobilen neste gang, se i nettverks- eller strøminnstillingene etter «Wake on LAN», «Slå på via nettverk», «Nettverksstandby» eller «Remote start».',
    ],
    extra=[
      ('Hvis TV-en ikke lar seg slå på fra mobilen', 'Ikke alle Android TV-er kan slås på via nettverket; det avhenger av produsent og modell. Har ikke din funksjonen, slår du den på med knappen på TV-en og fortsetter på mobilen. Slå av kan du gjøre fra appen.'),
      ('Chromecast med Google TV, Google TV Streamer og Shield', 'De kobles til på samme måte: samme Wi-Fi, trykk på enheten i listen og skriv inn koden. Viser TV-en en annen inngang, bytter du til HDMI-porten enheten sitter i, som forklart i [Bytt HDMI-inngang på TV-en uten fjernkontroll](@hdmi).'),
      ('Hvis koden ikke vises eller meldes som feil', 'Sjekk at TV-en virkelig er på og ikke i standby. Koden endres for hver forespørsel: Bare den siste fungerer. Du finner flere detaljer i [Android TV ber om en paringskode](@androidtv-code).'),
      ('Googles app eller Mando TV', 'Google har en egen app som krever en Google-konto. Mando TV krever ingen konto, fungerer også på Windows og styrer TV-er fra LG, Samsung og Roku med den samme appen.'),
    ],
    marca='android',
    faq=[
      ('Trenger jeg fjernkontrollen for å pare mobilen?', 'Nei. Koden vises på skjermen på TV-en og du skriver den inn på mobilen. Du trenger bare å slå på TV-en, om nødvendig med knappen på selve TV-en.'),
      ('Fungerer det med en Hisense?', 'På Hisense-TV-er med Android TV eller Google TV, ja. Hisense-TV-er med et annet system er ikke kompatible.'),
      ('Kan jeg skrive med tastaturet på mobilen?', 'Ja. Tastaturet er gratis og fungerer for søk i YouTube, Netflix og de andre appene.'),
    ]),
  dict(clave='lg-on', corto='Slå på LG-TV med mobilen',
    titulo='Slå på LG-TV med mobilen (veiledning)',
    desc='Slå på LG-TV med mobilen via Wi-Fi: Slå på «Slå på TV-en med mobil» og bruk Mando TV. Steg for steg, gratis.',
    h1='Slik slår du på en LG-TV med mobilen',
    intro='Du kan slå på en LG-TV med mobilen, men først må du slå på en innstilling på TV-en. Deretter slår mobilen på LG-TV-en via Wi-Fi-nettverket ditt, helt uten fjernkontroll. Det tar fem minutter, og du gjør det bare én gang.',
    pasos=[
      'Koble mobilen og LG-TV-en til det samme Wi-Fi-nettverket.',
      'Åpne innstillingene på TV-en og finn «Slå på TV-en med mobil». Du finner det under Innstillinger > Generelt > Enheter > Eksterne enheter (på eldre modeller Tilkobling > Administrasjon av mobiltilkobling).',
      'Slå på «Slå på via Wi-Fi». Er TV-en koblet til med nettverkskabel, slår du i stedet på alternativet for kabelen.',
      'Har TV-en «Hurtigstart+», slår du på det også.',
      'Åpne Mando TV på mobilen mens TV-en er på, og trykk på LG-TV-en din i listen. Bekreft forespørselen som kommer på skjermen. Slik lærer appen å vekke den.',
      'Slå av TV-en og prøv: Trykk på TV-en i Mando TV, så spør appen om den skal slå den på.',
    ],
    extra=[
      ('Hvis den ikke slår seg på', 'TV-en må ha vært på det samme Wi-Fi-nettverket da den ble slått av. Sjekk at innstillingen fortsatt er på og at mobilen er på det samme nettverket. Har du byttet ruter, kobler du til på nytt mens TV-en er på.'),
    ],
    marca='lg',
    faq=[
      ('Kan jeg slå på LG-TV-en med mobilen hvis jeg aldri har koblet til?', 'Nei. Først må du slå på «Slå på TV-en med mobil» på TV-en og koble til Mando TV én gang mens TV-en er på.'),
      ('Trenger jeg LG ThinQ-appen?', 'Nei. Mando TV kobler seg direkte via Wi-Fi-nettverket ditt og krever ingen LG-konto.'),
      ('Fungerer det med mobildata?', 'Nei. Mobilen og TV-en må være på det samme Wi-Fi-nettverket.'),
    ]),
  dict(clave='console', corto='TV og konsoll uten fjernkontroll',
    titulo='Ingen fjernkontroll? Slå på TV-en, bytt HDMI',
    desc='Lanseringsdag og ingen fjernkontroll? Slå på TV-en og bytt med mobilen til HDMI-inngangen til PS5 eller Xbox. Gratis, uten reklame.',
    h1='Slik slår du på TV-en og bytter til HDMI-inngangen til spillkonsollen uten fjernkontroll',
    intro='Lanseringsdagen til GTA VI, konsollen er klar og fjernkontrollen har forsvunnet et sted mellom sofaputene. Det skjer oftere enn man tror. Med Mando TV slår mobilen på TV-en og bytter via Wi-Fi hjemme til inngangen til PlayStation eller Xbox.',
    pasos=[
      'Koble mobilen til det samme Wi-Fi-nettverket som TV-en.',
      'Åpne Mando TV og trykk på TV-en din i listen (Samsung, LG, Roku eller Android TV).',
      'Er TV-en av, trykker du på Slå på. Det fungerer når påslåing via nettverket er slått på på TV-en. Har du aldri slått det på, slår du på TV-en med knappen på selve TV-en denne ene gangen og slår det på til neste gang.',
      'Slå på konsollen. Er HDMI-CEC slått på (se det gratis trikset lenger ned), bytter TV-en av seg selv til inngangen.',
      'Bytter den ikke, trykker du på Innganger i Mando TV og velger HDMI-porten konsollen sitter i: HDMI 1, HDMI 2 og så videre.',
      'For volumet bruker du de store knappene i appen mens du spiller.',
    ],
    extra=[
      ('Det gratis trikset: La konsollen bytte på TV-en', 'PS5 og Xbox kan slå på TV-en og hoppe rett til HDMI-inngangen sin ved oppstart, takket være HDMI-CEC. På PS5 finner du det under Innstillinger > System > HDMI > Slå på HDMI-enhetskobling. På Xbox åpner du Innstillinger > Generelt > TV- og skjermalternativer og leter etter alternativet for enhetskontroll. På TV-en heter funksjonen noe forskjellig avhengig av merke: Anynet+ hos Samsung, SIMPLINK hos LG og BRAVIA Sync eller HDMI-kontroll hos andre.'),
      ('Hvis TV-en blir stående på et annet bilde', 'Er konsollen på, men TV-en viser fortsatt antenne eller en app, har den ikke byttet inngang. Trykk på Innganger på mobilen og velg HDMI-inngangen til konsollen. Eller bruk piltastene og OK for å komme til inngangene på TV-en, eller knappen på selve TV-en, og velg HDMI-porten. Tallet er porten du koblet konsollkabelen til.'),
      ('Hvis det er en Roku TV', 'Knappen på TV-en, som oftest nederst på midten eller bak, slår den på. Derfra gjør mobilen resten.'),
    ],
    marca=None,
    faq=[
      ('Har Mando TV noe med GTA VI å gjøre?', 'Nei. Mando TV har ingen tilknytning til Rockstar Games eller Take-Two. Appen hjelper deg bare med å ikke miste spilletid fordi du ikke finner fjernkontrollen.'),
      ('Er det gratis å bytte HDMI-inngang?', 'Ja. Inngangslisten i Mando TV er gratis, akkurat som påslåing av TV-en og piltaster, OK og volum. Du kan også la konsollen bytte inngang av seg selv med HDMI-CEC.'),
      ('Fungerer det med TV-en min?', 'Det fungerer med TV-er fra Samsung, LG, Roku og Android TV på det samme Wi-Fi-nettverket. Er din av et annet merke, kan HDMI-CEC-trikset likevel hjelpe deg.'),
      ('Kan jeg bruke det til å spille GTA VI (GTA 6) på PS5 eller Xbox?', 'Mando TV griper hverken inn i konsollen eller i spillet. Det sørger bare for at TV-en er på og står på riktig HDMI-inngang, slik at du kan sette deg ned og spille.'),
    ]),
  dict(clave='samsung-lost', corto='Samsung-TV uten fjernkontroll',
    titulo='Mistet Samsung-fjernkontrollen? Bruk mobilen',
    desc='Mistet eller ødelagt Samsung-fjernkontroll? Bruk mobilen via Wi-Fi som fjernkontroll for Tizen-TV-er. Enkelt med Mando TV, gratis, uten reklame.',
    h1='Samsung-TV uten original fjernkontroll: Slik bruker du mobilen',
    intro='Hvis du har mistet Samsung-fjernkontrollen eller den ikke virker lenger, kan du bruke mobilen som fjernkontroll via Wi-Fi. Det fungerer med Samsung-TV-er med Tizen, fra 2016 og nyere.',
    pasos=[
      'Slå på TV-en med knappen på selve TV-en. På de fleste modeller sitter den nederst eller bak, noen ganger som en liten joystick.',
      'Sjekk at TV-en er koblet til Wi-Fi-nettverket ditt og at mobilen er på det samme nettverket.',
      'Åpne Mando TV på mobilen. Samsung-TV-en din dukker opp i listen av seg selv. Trykk på den.',
      'TV-en ber deg bekrefte tilkoblingen. På de fleste modeller bekrefter du den med knappene på TV-en eller med joysticken bak.',
      'Ferdig, nå kan du bruke mobilen som fjernkontroll. Knappene, tastaturet og appene er gratis; touchpad er en Pro-funksjon.',
      'For å slå på TV-en fra mobilen neste gang, går du til Innstillinger > Generelt > Nettverk > Ekspertinnstillinger og slår på «Slå på med mobil».',
    ],
    extra=[
      ('Hvis TV-en ikke spør om tillatelse', 'Kanskje er tillatelsen allerede lagret, eller TV-en er på et annet Wi-Fi-nettverk. Lukk Mando TV og åpne appen på nytt mens TV-en er på. Er TV-en eldre enn 2016, bruker den et annet system som ennå ikke støttes.'),
      ('Hvis du avslo tillatelsen ved en feil', 'Gå på TV-en til Innstillinger > Generelt > Ekstern enhetsbehandling > Enhetstilkoblingsbehandling og sett Mando TV til tillatt. Finner mobilen fortsatt ikke TV-en, les [Mobilen finner ikke TV-en](@not-found).'),
    ],
    marca='samsung',
    faq=[
      ('Hvordan bekrefter jeg tilkoblingen når jeg ikke har fjernkontroll?', 'På de fleste modeller bekrefter du den med knappene på TV-en eller med joysticken bak. Har modellen din ingen knapper, skriv til hola@mandotv.app, så hjelper vi deg.'),
      ('Krever Mando TV en Samsung-konto?', 'Nei. Tilkoblingen går direkte via Wi-Fi-nettverket ditt, uten Samsung-konto.'),
      ('Fungerer det med den eldre Samsung-TV-en min?', 'Det fungerer med Samsung-TV-er med Tizen, fra 2016 og nyere.'),
    ]),
  dict(clave='wifi', corto='Mobilen som fjernkontroll via Wi-Fi',
    titulo='Bruk mobilen som fjernkontroll: Styr TV-en via Wi-Fi',
    desc='Koble mobilen til TV-en via Wi-Fi og bruk den som fjernkontroll for Samsung, LG, Roku og Google TV. Steg per merke med Mando TV. Gratis.',
    h1='Slik kobler du mobilen til TV-en via Wi-Fi som fjernkontroll',
    intro='Du trenger bare mobilen og TV-en på det samme Wi-Fi-nettverket, og en fjernkontroll-app. Mando TV finner TV-en din av seg selv og fungerer med Samsung, LG, Roku, Google TV og Android TV.',
    pasos=[
      'Koble mobilen og TV-en til det samme Wi-Fi-nettverket.',
      'Åpne Mando TV. TV-en din dukker opp i listen av seg selv. Trykk på den.',
      'Bekreft tilkoblingen for merket ditt (detaljene står lenger ned).',
      'Styr TV-en med knappene eller med tastaturet på mobilen. Touchpad er en Pro-funksjon.',
    ],
    extra=[
      ('Samsung', 'TV-en spør om du vil tillate tilkoblingen. Bekreft den på skjermen første gang. Det fungerer med Tizen, fra 2016 og nyere. For å slå den på fra mobilen slår du på «Slå på med mobil» under Innstillinger > Generelt > Nettverk > Ekspertinnstillinger.'),
      ('LG', 'TV-en viser en forespørsel om tillatelse. Bekreft den første gang. For å slå den på fra mobilen finner du «Slå på TV-en med mobil» i innstillingene og slår på «Slå på via Wi-Fi».'),
      ('Roku', 'Roku krever ingen paring: Trykk på den i listen, så er du koblet til. For å slå den på slår du på «TV-hurtigstart» under Innstillinger > System > Strøm.'),
      ('Google TV og Android TV', 'TV-en viser en kode på skjermen. Skriv den inn i Mando TV første gang. For å slå den på leter du i innstillingene etter «Wake on LAN», «Slå på via nettverk» eller «Nettverksstandby».'),
    ],
    marca=None,
    faq=[
      ('Trenger jeg internett for å bruke mobilen som fjernkontroll?', 'Du trenger mobilen og TV-en på det samme Wi-Fi-nettverket. Mando TV kobler seg direkte til TV-en din via dette nettverket.'),
      ('Hvorfor dukker ikke TV-en opp i listen?', 'Sjekk at TV-en er på og at mobilen ikke bruker mobildata eller et annet Wi-Fi-nettverk. Noen rutere har et gjestenettverk som skiller enheter fra hverandre.'),
      ('Kan jeg bruke Mando TV på iPhone eller på en Android-mobil?', 'På iPhone og iPad, ja: Appen er allerede i App Store. For Windows finnes den også i Microsoft Store. Android kommer snart: Du kan være med i den gratis tidlige tilgangen på Google Play.'),
    ]),
  dict(clave='pc', corto='Styr TV-en fra PC-en',
    titulo='Styr TV-en med Windows-PC (gratis)',
    desc='Bruk Windows-PC-en som fjernkontroll for Samsung, LG, Roku eller Google TV via Wi-Fi. Knapper, tastatur og apper gratis; PC-hurtigtaster med Pro.',
    h1='Slik styrer du TV-en med en Windows-PC',
    intro='Hvis du tilbringer dagen foran datamaskinen, trenger du ikke lete etter fjernkontrollen: Mando TV for Windows styrer Samsung-, LG-, Roku-, Google TV- eller Android TV-en din via Wi-Fi hjemme. Praktisk for å bytte app, skru opp lyden eller skrive i YouTube med PC-tastaturet.',
    pasos=[
      'Last ned Mando TV gratis fra Microsoft Store til datamaskinen med Windows 10 eller 11.',
      'Sjekk at datamaskinen og TV-en er på det samme nettverket (Wi-Fi eller kabel, men via den samme ruteren).',
      'Åpne Mando TV: TV-en din dukker opp i listen av seg selv. Trykk eller klikk på den.',
      'Bekreft tilkoblingen på skjermen til TV-en første gang (på Google TV og Android TV skriver du inn koden som TV-en viser).',
      'Ferdig: Bruk knappene eller tastaturet for å skrive i søkefeltet på TV-en. Touchpad er en Pro-funksjon.',
    ],
    extra=[
      ('Hurtigtaster på PC-en (Pro)', 'Med Mando TV Pro styrer du TV-en med datamaskinens tastatur: piltaster for å navigere, Enter for OK, Backspace eller Esc for Tilbake, + og - for volum, M for lyd av og mellomrom for pause.'),
      ('Minifjernkontroll som alltid ligger øverst (Pro)', 'Ha et lite vindu med fjernkontrollen synlig hele tiden mens du jobber eller spiller på PC-en.'),
      ('Snakk med TV-en fra PC-en (Pro)', 'Med Mando TV Pro gir du TV-en kommandoer via mikrofonen på PC-en: «åpne YouTube», «skru opp lyden» eller «slå av om 30 minutter», akkurat slik du snakker. På Windows gjenkjennes talen på selve PC-en: Du trenger ikke internett, du trenger ikke endre noe i Windows-innstillingene, og det fungerer på de 6 språkene i appen. Det du sier forlater ikke PC-en og blir ikke lagret. Bare på svært gamle prosessorer faller appen tilbake på Windows-diktering. Da må nettbasert talegjenkjenning være slått på i personverninnstillingene og norsk (Norge) være lagt til i Windows. Mangler noe, sier appen fra og åpner innstillingen med en knapp.'),
    ],
    marca=None,
    faq=[
      ('Trenger jeg kabel eller Bluetooth for å styre TV-en fra PC-en?', 'Nei. Mando TV kobler seg via hjemmenettverket ditt: PC-en og TV-en må bare være koblet til den samme ruteren.'),
      ('Fungerer det med alle TV-er?', 'Det fungerer med Samsung-TV-er med Tizen (fra 2016 og nyere), LG med webOS, Roku og Google TV eller Android TV (Sony, Philips, TCL, Hisense, Sharp, Xiaomi, Toshiba, Panasonic, Haier, Skyworth og andre).'),
      ('Hva koster det?', 'Knappene, tastaturet og påslåing via nettverket er gratis og uten reklame. Mando TV Pro er et engangskjøp uten abonnement for ekstrafunksjoner som touchpad, PC-hurtigtaster og minifjernkontrollen.'),
      ('Hvorfor forstår ikke mikrofonen meg på Windows?', 'Sjekk at talefunksjonen er aktiv (den hører til Pro) og at mikrofonen på PC-en fungerer i Windows. På nesten alle PC-er gjenkjennes talen på selve enheten, helt uten internett. Bare på svært gamle prosessorer bruker appen Windows-diktering. Sjekk da at nettbasert talegjenkjenning er slått på i personverninnstillingene i Windows og at Windows har norsk (Norge) i språkinnstillingene. Mando TV bruker dette språket bare så lenge det lytter.'),
    ]),
  dict(clave='roku-403', corto='Roku-appen fungerer ikke',
    titulo='Roku-appen fungerer ikke? Fiks feil 403',
    desc='Mobilen er koblet til, men Roku reagerer ikke? Slå på «Kontroll fra mobilapper» i 5 steg og bruk mobilen som fjernkontroll igjen.',
    h1='Roku-appen fungerer ikke: Slik fikser du problemet',
    intro='Hvis mobilen finner Roku-en og kobler til, men ingen knapp gjør noe, skyldes det nesten alltid en innstilling på selve Roku-en som blokkerer fjernkontroll-apper. Nyere Roku-versjoner er mer begrenset som standard. I Roku-menyen er det fikset på et minutt.',
    pasos=[
      'Trykk på Hjem på Roku-en og gå til Innstillinger.',
      'Åpne System og deretter Avanserte systeminnstillinger.',
      'Gå til «Kontroll fra mobilapper». På noen modeller heter det «Ekstern kontroll».',
      'Velg Standard eller Permissive under «Nettverkstilgang». Er det bare en bryter på modellen din, lar du den stå på Aktivert.',
      'Gå tilbake til Mando TV på mobilen og trykk på Roku-en din. Knappene reagerer nå.',
    ],
    extra=[
      ('Slik ser du om dette er problemet ditt', 'Tegnet er tydelig: Mobilen ser Roku-en i listen og kobler til, men ingenting skjer når du trykker på en knapp. Internt svarer Roku med feil 403, som betyr «forbudt». Mando TV oppdager dette ved tilkobling og viser deg akkurat disse stegene på skjermen.'),
      ('Standard eller Permissive, hva velger jeg?', 'Standard er nok: Den godtar kommandoer fra hjemmenettverket ditt, og det er det en fjernkontroll trenger. Permissive er mer åpen og trengs bare på uvanlige nettverk.'),
      ('Hvis du ikke har Roku-fjernkontrollen', 'Står innstillingen på Deaktivert, kan den bare endres med den ekte Roku-fjernkontrollen. Lån en for å endre den én gang; etterpå kan du gjøre alt med mobilen. Les også [Mistet Roku-fjernkontrollen](@roku-lost).'),
    ],
    marca='roku',
    faq=[
      ('Hvorfor reagerer ikke Roku-en min lenger, selv om den fungerte før?', 'En Roku-oppdatering kan begrense denne innstillingen mer. Det skyldes ikke mobilen eller Wi-Fi-nettverket ditt: Du må bare tillate kontroll fra apper igjen.'),
      ('Gjelder dette for Roku TV og for Roku-spillere?', 'Ja. Innstillingen står i den samme menyen på Roku-spillere og på Roku TV-er.'),
      ('Er det trygt å la innstillingen stå på Standard?', 'Ja. Den godtar bare kommandoer fra enheter i hjemmenettverket ditt.'),
    ]),
  dict(clave='not-found', corto='Mobilen finner ikke TV-en',
    titulo='Mobilen finner ikke TV-en? 6 ting å sjekke',
    desc='Finner ikke fjernkontroll-appen TV-en din? Sjekk Wi-Fi, VPN og tilgang til lokalt nettverk. For Samsung, LG, Roku og Android TV.',
    h1='Mobilen finner ikke TV-en: Dette bør du sjekke',
    intro='Du åpner fjernkontroll-appen og listen er tom, eller TV-en dukker opp, men tilkoblingen brytes. Nesten alltid skyldes det nettverket og ikke TV-en. Sjekk disse punktene i rekkefølge: Det første løser de fleste tilfellene.',
    pasos=[
      'Se hvilket Wi-Fi-nettverk mobilen er på og hvilket TV-en er på. Det må være det samme nettverket med det samme navnet. Et gjestenettverk fungerer ikke, fordi det skiller enheter fra hverandre.',
      'Slå av VPN på mobilen hvis du bruker det. Med VPN på går mobilen ut på internett via et annet nettverk og ser ikke enhetene hjemme hos deg, eller tilkoblingen brytes etter noen sekunder.',
      'Slå av mobildata en kort stund. Noen mobiler bytter av seg selv fra Wi-Fi til mobildata ved svakt signal.',
      'Slå på TV-en og vent til den er ferdig startet. En avslått TV svarer ikke på søket.',
      'På iPhone: Sjekk at appen har tillatelsen «Lokalt nettverk»: Innstillinger > Personvern og sikkerhet > Lokalt nettverk.',
      'Dukker den fortsatt ikke opp, legger du den til manuelt: Trykk på «Legg til via IP» i Mando TV og skriv inn IP-adressen til TV-en.',
    ],
    extra=[
      ('La appen guide deg', 'I TV-listen finnes det en knapp for tilfellet at TV-en din ikke dukker opp. Appen sjekker de vanligste årsakene steg for steg (samme Wi-Fi, VPN, tillatelse for lokalt nettverk og mer) og viser en knapp for å sjekke på nytt etter hver rettelse. Assistenten er gratis.'),
      ('Hvor du finner IP-adressen til TV-en', 'Den står i nettverksmenyen på TV-en og er litt forskjellig fra modell til modell. På LG: Innstillinger, Nettverk, Wi-Fi-tilkobling, Avanserte Wi-Fi-innstillinger. På Samsung: Innstillinger, Generelt, Nettverk, Nettverksstatus, IP-innstillinger. På Roku: Innstillinger, Nettverk, Om. På Android TV og Google TV: Innstillinger, Nettverk og internett, og så trykker du på nettverket ditt. Det er et tall som 192.168.1.86.'),
      ('Hvis den dukker opp, men tilkoblingen brytes', 'Brytes tilkoblingen etter noen sekunder, ligger årsaken som regel hos mobilen: et VPN, bytte til et annet Wi-Fi-nettverk eller strømsparemodus. Slå av VPN, bli på det samme Wi-Fi-nettverket og prøv på nytt.'),
      ('Wi-Fi med 2,4 og 5 GHz', 'Det spiller ingen rolle om mobilen er på 5 GHz-nettet og TV-en på 2,4 GHz-nettet, så lenge begge kommer fra den samme ruteren. Har du en Wi-Fi-forsterker og TV-en likevel ikke dukker opp, går du med mobilen nærmere hovedruteren og prøver igjen.'),
    ],
    marca=None,
    faq=[
      ('Kan jeg styre TV-en med mobildata?', 'Nei. Fjernkontrollsignalet går via Wi-Fi-nettverket ditt hjemme, derfor må mobilen og TV-en være på det samme nettverket.'),
      ('Hvorfor fungerer det ikke med VPN på?', 'Fordi VPN leder all trafikk fra mobilen via et annet nettverk, og mobilen ikke ser enhetene hjemme hos deg lenger. Slå det av så lenge du bruker fjernkontrollen.'),
      ('Fungerer det med Bluetooth eller infrarød?', 'På smart-TV-er bruker Mando TV Wi-Fi. Infrarød fungerer bare på Android-mobiler med infrarød sender og er ment for TV-er som ikke er smart-TV-er. Bluetooth finnes i beta, gratis og bare fra Android 9: Mobilen kobler seg til TV-en som Bluetooth-tastatur og -fjernkontroll, helt uten Wi-Fi. Det fungerer med Google TV, Android TV og Fire TV; på andre merker som godtar Bluetooth-tastaturer kan det fungere, Roku godtar dem ikke.'),
    ]),
  dict(clave='androidtv-code', corto='Android TV paringskode',
    titulo='Android TV ber om en paringskode: Dette må du gjøre',
    desc='Android TV eller Google TV viser en kode med 6 tegn når du kobler til. Slik skriver du den inn, og dette gjør du hvis den ikke vises eller er feil.',
    h1='Android TV ber om en paringskode: Dette må du gjøre',
    intro='Når du kobler mobilen til en Android TV eller Google TV for første gang, viser TV-en en kode med 6 tegn på skjermen. Det er normalt og skjer bare én gang: Slik sikrer vi at ingen andre kan styre TV-en din. Her ser du hvordan du skriver den inn og hva du gjør hvis den ikke vises.',
    pasos=[
      'Slå på TV-en og la startskjermen være synlig.',
      'Åpne Mando TV på mobilen, på det samme Wi-Fi-nettverket som TV-en, og trykk på TV-en din i listen.',
      'Se på skjermen på TV-en: En kode med 6 bokstaver og tall vises.',
      'Skriv den inn på mobilen akkurat slik den vises, og trykk på Pare. Bokstavene går bare fra A til F, så et rundt tegn er alltid tallet null.',
      'Ferdig. TV-en husker mobilen din og spør ikke om koden på nytt.',
    ],
    extra=[
      ('Hvis koden ikke vises på TV-en', 'Sjekk at TV-en virkelig er på og ikke i standby, og at mobilen er på det samme Wi-Fi-nettverket. Trykk på TV-en på mobilen igjen. Vises den fortsatt ikke, starter du TV-en på nytt: Trekk ut støpselet i ti sekunder, sett det inn igjen og prøv på nytt.'),
      ('Hvis koden meldes som feil', 'Koden endres for hver forespørsel. Har du brukt lang tid eller bedt om den to ganger, fungerer bare den siste på skjermen. Trykk på TV-en på mobilen igjen og skriv inn den nye koden.'),
      ('Hvis TV-en spør om koden igjen', 'Det skjer hvis TV-en er satt tilbake til fabrikkinnstillinger eller du sletter appdataene på mobilen. Par på nytt, så blir den lagret. Har du ingen fjernkontroll i det hele tatt, les [Android TV uten fjernkontroll](@androidtv).'),
    ],
    marca='android',
    faq=[
      ('Hvilke TV-er bruker denne koden?', 'De med Android TV eller Google TV: Sony, Philips, TCL, Hisense, Sharp, Xiaomi, Chromecast med Google TV og noen flere.'),
      ('Trenger jeg en Google-konto på mobilen?', 'Nei. Koden på skjermen er alt du trenger.'),
      ('Er det trygt?', 'Ja. Koden beviser at du sitter foran TV-en: Ingen kan pare uten å se den på skjermen.'),
    ]),
  dict(clave='roku-lost', corto='Mistet Roku-fjernkontrollen',
    titulo='Mistet Roku-fjernkontrollen? Bruk mobilen via Wi-Fi',
    desc='Mistet Roku-fjernkontrollen? Mobilen erstatter den via Wi-Fi. Enkle steg, også hvis du har byttet ruter og Roku-en ikke har Wi-Fi.',
    h1='Mistet Roku-fjernkontrollen: Slik bruker du mobilen',
    intro='Hvis du har mistet Roku-fjernkontrollen eller den ikke virker lenger, erstatter mobilen den så lenge Roku-en fortsatt er koblet til Wi-Fi-nettverket ditt. Og har du byttet Wi-Fi eller ruter, finnes det en utvei også for det.',
    pasos=[
      'Prøv først å få fjernkontrollen til å ringe. Har Roku-fjernkontrollen en høyttaler, for eksempel Roku Voice Remote Pro, åpner du Mando TV, kobler til Roku-en og bruker alternativet for å få fjernkontrollen til å ringe slik at du finner den. Det fungerer bare med Roku-fjernkontroller med høyttaler, og Roku-en må være på.',
      'Slå på TV-en og la Roku-en være tilkoblet. Du trenger ikke røre den.',
      'Koble mobilen til det samme Wi-Fi-nettverket som Roku-en bruker.',
      'Åpne Mando TV. Roku-en dukker opp i listen av seg selv. Trykk på den.',
      'Bruk piltaster, OK, Hjem og Tilbake som på den vanlige fjernkontrollen. Roku spør ikke om kode.',
      'Gjør knappene ingenting, blokkerer Roku-en kontroll fra apper: Guiden [Roku-appen fungerer ikke](@roku-403) forklarer hvordan du tillater den.',
    ],
    extra=[
      ('Hvis Roku-en ikke har Wi-Fi (byttet ruter eller flyttet)', 'Uten fjernkontroll kommer du ikke inn i menyen for å sette opp det nye nettverket, men det finnes et triks: Roku-en kobler seg av seg selv til et nettverk som har det samme navnet og det samme passordet som det gamle. Opprett en Wi-Fi-hotspot på en annen mobil med akkurat dette navnet og passordet, koble mobilen med Mando TV til den, så dukker Roku-en opp i listen. Gå derfra til Innstillinger, Nettverk og koble den til det nye Wi-Fi-nettverket.'),
      ('Hvis det er en Roku TV', 'Roku TV-er har en knapp på selve TV-en, nesten alltid nederst på midten eller bak, som slår på TV-en. Det holder for å slå den på og fortsette med mobilen.'),
      ('Hvis du heller vil kjøpe en annen fjernkontroll', 'Pass på at den passer til modellen din. Små Roku-spillere bak TV-en trenger en fjernkontroll uten infrarød, fordi infrarød ikke når dem.'),
    ],
    marca='roku',
    faq=[
      ('Kan mobilen slå på Roku-en?', 'En tilkoblet Roku-spiller er alltid på. På en Roku TV slår Mando TV den på via Wi-Fi hvis «TV-hurtigstart» er slått på under Innstillinger > System > Strøm.'),
      ('Og volumet?', 'På en Roku TV skrur mobilen volumet opp og ned. På en Roku-spiller som er koblet til via HDMI, avhenger det av TV-en: På mange fungerer det, på andre ikke.'),
      ('Må jeg opprette en konto?', 'Nei. Mando TV krever ingen konto og styrer i tillegg TV-er fra Samsung, LG og Android TV med den samme appen.'),
    ]),
]

SOPORTE = dict(
  titulo='Hjelp: Koble TV-en til Mando TV og slå den på',
  desc='Slik kobler du Mando TV-fjernkontrollen til LG, Samsung, Roku eller Android TV, slår på TV-en fra mobilen og løser problemer.',
  h1='Hjelp',
  intro='De vanligste spørsmålene, i rekkefølgen av stegene. Finner du ikke ditt, skriv til oss på <a href="mailto:hola@mandotv.app?subject=Hjelp%20med%20Mando%20TV">hola@mandotv.app</a>, så svarer vi.',
)
SOPORTE_HTML = '''      <h2 id="encontrar">Finne TV-en</h2>
      <div class="preguntas">
        <details open><summary>TV-en min dukker ikke opp i listen</summary>
          <ol>
            <li>Sjekk at mobilen og TV-en er på det samme Wi-Fi-nettverket. Har ruteren et 2,4 GHz- og et 5 GHz-nett med forskjellige navn, ser de noen ganger ikke hverandre.</li>
            <li>Sørg for at TV-en er på.</li>
            <li>På iPhone: Sjekk at Mando TV har tillatelsen «Lokalt nettverk», under Innstillinger, Mando TV.</li>
            <li>Trykk på knappen «Dukker ikke TV-en opp?» i TV-listen: Appen sjekker de vanligste årsakene steg for steg (samme Wi-Fi, VPN, tillatelse for lokalt nettverk og mer) og viser en knapp for å sjekke på nytt etter hver rettelse.</li>
            <li>Dukker den fortsatt ikke opp, trykker du på +-knappen, velger merket og skriver inn IP-adressen til TV-en. Du ser den i nettverksmenyen på TV-en (for eksempel 192.168.1.50).</li>
          </ol>
        </details>
        <details><summary>Fungerer det med mobildata eller når jeg er på farten?</summary>
          <p>Nei. Mando TV snakker med TV-en innenfor hjemmenettverket ditt, så mobilen må være koblet til dette Wi-Fi-nettverket.</p>
        </details>
      </div>

      <h2 id="conectar">Koble til for første gang</h2>
      <p>Komplette guider per merke: <a href="@@R_lg@@">LG</a>, <a href="@@R_samsung@@">Samsung</a>, <a href="@@R_roku@@">Roku</a> og <a href="@@R_android@@">Android TV</a>.</p>
      <div class="preguntas">
        <details><summary>LG</summary>
          <p>Når du trykker på TV-en, kommer det en forespørsel om tillatelse på skjermen. Bekreft den med den vanlige fjernkontrollen. Det gjør du bare én gang.</p>
        </details>
        <details><summary>Samsung</summary>
          <p>TV-en spør om du tillater tilkoblingen fra Mando TV. Velg «Tillat» med fjernkontrollen. Har du avslått den ved en feil, går du til Innstillinger > Generelt > Ekstern enhetsbehandling > Enhetstilkoblingsbehandling og endrer den til tillatt.</p>
        </details>
        <details><summary>Roku</summary>
          <p>Roku spør ikke om tillatelse. Fungerer ikke tilkoblingen, går du på Roku-en til Innstillinger > System > Avanserte systeminnstillinger > Kontroll fra mobilapper og lar nettverkstilgang stå på Standard eller Permissive (på nyere Roku-programvare setter du Kontroll fra mobilapper til Aktivert).</p>
        </details>
        <details><summary>Android TV og Google TV</summary>
          <p>TV-en viser en kode med 6 tegn. Skriv den inn i Mando TV akkurat slik den vises. Det fungerer på Sony, Philips, TCL, Hisense, Sharp, Xiaomi, Chromecast med Google TV og andre med Android TV.</p>
        </details>
      </div>

      <h2 id="encender">Slå på TV-en fra appen</h2>
      <p>Mando TV slår på TV-en via hjemmenettverket ditt. Det trengs to ting: Du har koblet til minst én gang mens TV-en var på, og påslåing via nettverket er slått på på TV-en. Navnet på innstillingen varierer fra modell til modell; dette er de vanligste:</p>
      <div class="preguntas">
        <details><summary>LG</summary>
          <p>Finn «Slå på TV-en med mobil» (eller «Slå på via Wi-Fi») under Innstillinger > Generelt > Enheter > Eksterne enheter (på eldre modeller Tilkobling > Administrasjon av mobiltilkobling), og slå det på.</p>
        </details>
        <details><summary>Samsung</summary>
          <p>Slå på «Slå på med mobil» under Innstillinger > Generelt > Nettverk > Ekspertinnstillinger.</p>
        </details>
        <details><summary>Roku</summary>
          <p>På Roku TV-er slår du på «TV-hurtigstart» under Innstillinger > System > Strøm. Roku-spillere som er koblet til en TV, kan ikke slås på på denne måten.</p>
        </details>
        <details><summary>Android TV og Google TV</summary>
          <p>Det avhenger av produsenten. Se i nettverks- eller strøminnstillingene etter «Wake on LAN», «Slå på via nettverk», «Nettverksstandby» eller «Remote start». Noen modeller har ikke dette alternativet.</p>
        </details>
      </div>

      <h2 id="falla">Hvis noe ikke fungerer</h2>
      <div class="preguntas">
        <details><summary>Tilkoblingen brytes eller det kommer ingen reaksjon</summary>
          <ol>
            <li>Trykk på Koble til på nytt på fjernkontrollskjermen.</li>
            <li>Hjelper ikke det, lukker du Mando TV og åpner appen på nytt.</li>
            <li>Har TV-en fått en annen IP-adresse, fjerner du den fra listen og legger den til på nytt.</li>
          </ol>
        </details>
        <details><summary>Slik sender du oss en feilrapport</summary>
          <ol>
            <li>Trykk på Tilpass-knappen i Mando TV (glidebryterne øverst).</li>
            <li>Trykk på Kopier testrapport.</li>
            <li>Lim den inn i en e-post til hola@mandotv.app sammen med merke og modell på TV-en din.</li>
          </ol>
          <p>Rapporten inneholder ingen passord, ingen koder og ingenting av det du skriver.</p>
        </details>
        <details><summary>Jeg har kjøpt Pro og det dukker ikke opp</summary>
          <p>Trykk på Gjenopprett kjøp under Tilpass, med den samme butikkontoen du kjøpte med. Dukker det fortsatt ikke opp, skriv til oss.</p>
        </details>
      </div>

      <h2 id="guias">Guider steg for steg</h2>
      <p><a href="@@R_guias@@">Se alle guider</a></p>
      <ul>
@@GUIAS@@
      </ul>

      <h2 id="contacto">Fortsatt spørsmål?</h2>
      <p>Skriv til oss på <a href="mailto:hola@mandotv.app?subject=Hjelp%20med%20Mando%20TV">hola@mandotv.app</a>. Si fra om merke og modell på TV-en og hvilket steg du står fast på. Skriv til oss på ditt eget språk. Vi svarer på spansk eller engelsk og, hvis du vil, på ditt språk ved hjelp av en oversetter.</p>
'''

PRIVACIDAD = dict(
  titulo='Personvernerklæring | Mando TV',
  desc='Mando TV samler ikke inn personopplysninger: ingen kontoer, ingen reklame, ingen sporere. Appen snakker bare med TV-en din innenfor Wi-Fi-nettverket ditt.',
  h1='Personvern',
  intro='Kort sagt: Mando TV samler ikke inn dataene dine. Det finnes ingen kontoer, ingen reklame, ingen sporere og ingen egne servere som lagrer det du gjør.',
)
PRIVACIDAD_HTML = '''      <p class="fecha">Gyldig fra 14. november 2026. Sist oppdatert 26. november 2026.</p>

      <h2>Hvem vi er</h2>
      <p>Mando TV er en app som lar deg styre TV-en fra mobilen eller datamaskinen. Denne erklæringen beskriver hvilken informasjon appen bruker og hva den gjør med den. Har du spørsmål, skriv til oss på <a href="mailto:hola@mandotv.app">hola@mandotv.app</a>.</p>

      <h2>Hvilke data vi samler inn</h2>
      <p>Appen: ingen. Appen sender verken informasjon om deg eller om hvordan du bruker den til oss eller til tredjeparter. Den bruker ingen analyse-, reklame- eller sporingsverktøy.</p>
      <p>Dette nettstedet: Vi måler besøk på to måter, som er forklart i avsnittet <a href="#cookies">Informasjonskapsler på dette nettstedet</a>.</p>

      <h2>Hva appen lagrer på enheten din</h2>
      <p>For å fungere lagrer appen følgende bare på mobilen eller datamaskinen din:</p>
      <ul>
        <li>TV-ene du har lagt til: navn, merke, IP-adresse i nettverket ditt og maskinvareadressen til nettverket (MAC), som brukes til å slå dem på.</li>
        <li>Tilkoblingsnøklene som hver TV utleverer når du bekrefter tillatelsen. De lagres kryptert i systemets sikre lagring (nøkkelring på iPhone og Mac, Keystore på Android, beskyttet lagring på Windows).</li>
        <li>Innstillingene dine: lyst eller mørkt tema, bakgrunnsfarge, vibrasjon og type fjernkontroll.</li>
        <li>Hvis du bruker Pro-funksjonene: favorittappene dine, rutinene dine og de siste YouTube-søkene dine (du kan slette dem i appen).</li>
      </ul>
      <p>Når du sletter appen, slettes alt dette sammen med den.</p>

      <h2>Hvem appen snakker med</h2>
      <p>Med TV-ene dine, innenfor Wi-Fi-nettverket ditt hjemme. For å finne dem søker appen gjennom det lokale nettverket ditt; derfor ber den om tillatelsen «Lokalt nettverk» på en iPhone. Teksten du skriver med tastaturet i appen går direkte til TV-en og blir ikke lagret.</p>
      <p>I tillegg laster appen ned en liten offentlig fil fra dette nettstedet når den åpnes (mandotv.app/app/config.json), for å finne ut om det finnes en ny versjon du bør installere og hvilke funksjoner som hører til Mando TV Pro. Det er en nedlasting, som når man åpner en side: Appen sender verken dataene dine, TV-ene dine eller det du gjør. Den oppgir bare appversjonen og systemet (for eksempel Android), slik at den kan vise deg riktig melding. Har du ikke internett, fortsetter appen med den sist nedlastede filen; går det mer enn 30 dager uten at den har kunnet lastes ned, ber appen deg om å koble til internett en kort stund.</p>

      <p>Når du sender bilder eller videoer til TV-en (en Pro-funksjon), laster TV-en bare ned filene du velger, direkte fra mobilen eller PC-en via Wi-Fi-nettverket ditt hjemme. De går verken via internett eller via oss, appen ser ikke de andre bildene dine, og delingen tar slutt så snart du lukker denne skjermen.</p>
      <h2>Mikrofon og tale</h2>
      <p>På iPhone, Mac og Android bruker talesøket mikrofonen bare så lenge du trykker på snakkeknappen. Det du sier, gjøres om til tekst av systemets talegjenkjenning: av Apple på iPhone og Mac og av Google på Android, i begge tilfeller etter deres egne personvernvilkår. På Windows gjenkjennes talen på din egen PC og forlater ikke enheten; bare på svært gamle prosessorer bruker appen taleinndata fra Windows, fra Microsoft, etter deres personvernvilkår. På Windows åpnes mikrofonen når du åpner stemmepanelet og lukkes når du lukker det, eller etter 30 sekunder uten bruk; mens du ikke snakker, blir ingenting tatt opp eller lagret. Mando TV tar verken opp eller lagrer lyden, og teksten som oppstår går direkte til TV-en din, akkurat som det du skriver med tastaturet.</p>

      <h2>Hjem: enheter fra Apple Home og Google Home</h2>
      <p>Når du åpner området Hjem (i test), ber appen om tillatelse til å se enhetene du allerede har i Apples Hjem-app (HomeKit) eller i Google Home. Med denne tillatelsen leser den navnet, rommet og tilstanden deres (på eller av, lysstyrke, temperatur eller hvor et hvitevare er i programmet sitt) for å vise dem og sende dem det du trykker på. Alt skjer mellom mobilen din og systemet til Apple eller Google: Mando TV lagrer ikke denne listen, sender den verken til oss eller til tredjeparter og bruker den hverken til reklame eller analyse. På Android fungerer Google Home med din egen Google-konto, etter Googles personvernerklæring. Du kan trekke tilbake tillatelsen når som helst: på iPhone under Innstillinger &gt; Personvern og sikkerhet &gt; HomeKit, på Android i innstillingene til Google-kontoen din.</p>
      <p>Når du trykker på «Hvordan fungerte Hjem for deg?», åpnes e-postappen din med en melding til hola@mandotv.app som inneholder et teknisk sammendrag: versjonen av appen, systemet og hvor mange enheter av hver type som dukket opp og om de reagerer. Navn på enheter, rom eller hjemmet ditt er ikke med, og meldingen sendes bare hvis du selv sender den.</p>

      <h2>Testrapport</h2>
      <p>Appen har en knapp «Kopier testrapport» som hjelper oss med å rette feil. Rapporten blir bare i appens minne så lenge den er åpen, og sendes aldri av seg selv: Du bestemmer om du kopierer og deler den. Den inneholder ingen tilkoblingsnøkler, ingen paringskoder og ingenting av det du skriver inn; bare stegene appen har utført, som søk, tilkobling og feilene.</p>

      <h2 id="cookies">Informasjonskapsler på dette nettstedet</h2>
      <p>Dette gjelder bare nettstedet mandotv.app, ikke appen.</p>
      <h3>Alltid uten informasjonskapsler</h3>
      <p>Vi teller besøk anonymt med Cloudflare Web Analytics: hvor mange som besøker nettstedet, hvilke sider de leser og fra hvilket land. Det bruker ingen informasjonskapsler, bruker ikke IP-adressen din til å identifisere deg og sporer ikke det du gjør på andre nettsteder.</p>
      <h3>Med informasjonskapsler, bare hvis du samtykker</h3>
      <p>Når du trykker på «Godta» i informasjonskapselvarselet, slår vi på Google Analytics (fra Google LLC) for å forstå bedre hvordan nettstedet brukes: sidevisninger, tid på siden, enhetstype, omtrentlig by og hvor du kommer fra. For dette lagrer det informasjonskapslene _ga og _ga_* i opptil 2 år i nettleseren din. Google kan behandle disse dataene på servere utenfor Chile. Vi har slått av reklamefunksjonene og Google Signals og bruker ikke disse dataene til å vise deg reklame.</p>
      <p>Når du trykker på «Avslå» eller ikke velger noe, lastes ikke Google Analytics, og det lagres ingen informasjonskapsel. Du kan endre valget når som helst med knappen «Informasjonskapsler» nederst på hver side; når du trekker tilbake samtykket, sletter vi disse informasjonskapslene.</p>
      <p>Valget ditt lagres i nettleseren din (lokal lagring, sendes ikke til noen), slik at vi ikke spør deg igjen.</p>

      <h2>Kjøp</h2>
      <p>Når du kjøper Mando TV Pro, håndteres betalingen av appbutikken (App Store, Google Play eller Microsoft Store). Vi mottar og lagrer ikke kortopplysningene dine. Butikken bekrefter bare overfor appen at kjøpet finnes.</p>

      <h2>E-poster du sender oss</h2>
      <p>Når du skriver til oss på <a href="mailto:hola@mandotv.app">hola@mandotv.app</a>, bruker vi e-postadressen din og det du forteller oss bare til å svare deg. Vi gir dem ikke videre og bruker dem ikke til reklame. Du kan når som helst kreve at vi sletter meldingene dine.</p>

      <h2>Barn</h2>
      <p>Appen samler ikke inn data fra noen, heller ikke fra barn.</p>

      <h2>Endringer i denne erklæringen</h2>
      <p>Skulle det en dag endre seg hva appen gjør med dataene dine, oppdaterer vi denne siden og datoen øverst før endringen når appen.</p>
'''



# >>> guías traídas del inglés (ensamblar.py)
# Adaptadas con Ollama (qwen3.6:35b) desde las guías inglesas y auditadas por Opus el 22-nov. Rutas en idiomas_sitio.py.
GUIAS += [
  dict(clave='no-sub', corto='Fjernkontroll-app uten abonnement', fecha='2026-11-23',
    titulo='Fjernkontroll-app for TV uten abonnement og reklame',
    desc='Lei av fjernkontroll-apper med reklame eller ukesabonnement? Mando TV er gratis og uten reklame, Pro er et valgfritt engangskjøp. Ærlig sammenligning.',
    h1='En fjernkontroll-app uten abonnement og uten reklame',
    intro='Mange universalfjernkontroller viser reklame eller krever et ukentlig abonnement før de fungerer. Mando TV går en annen vei: Fjernkontrollen er gratis, det finnes ingen reklame og ingen konto. Det valgfrie Pro kjøper du bare én gang. Her er sammenligningen, også med det appen ikke kan.',
    pasos=[
      'Før du installerer, åpner du butikksiden til en app og sjekker kjøp i appen. Ukentlige eller månedlige priser tyder på et abonnement.',
      'Sjekk på Google Play om det står «Inneholder annonser» på siden, og les de nyeste anmeldelsene med få stjerner: Der dukker det ofte opp uventede betalingsmurer.',
      'Sørg for at appen kan styre TV-en din via Wi-Fi. Mando TV fungerer med Samsung (fra 2016), LG webOS, Roku, Google TV, Android TV og Fire TV.',
      'Installer Mando TV, koble mobilen til det samme Wi-Fi-nettverket som TV-en og trykk på TV-en din i listen.',
      'Bekreft forespørselen på TV-en eller skriv inn koden som vises. Knapper, volum, kanaler og tastatur koster ingenting.',
    ],
    tabla=dict(titulo='Mando TV sammenlignet med mange fjernkontroll-apper',
      cabeza=['', 'Mando TV', 'Mange annonsefinansierte apper eller abonnementsapper'],
      filas=[
        ['Grunnleggende fjernkontroll', 'Gratis', 'Ofte gratis med reklame eller skjult bak en prøveperiode'],
        ['Reklame', 'Ingen', 'Hyppig'],
        ['Abonnement', 'Ingen. Pro er et valgfritt engangskjøp', 'Ukentlige eller månedlige planer er vanlig'],
        ['Konto', 'Ikke nødvendig', 'Varierer'],
        ['Smart-TV-er via Wi-Fi', 'Samsung (fra 2016), LG webOS, Roku, Google TV, Android TV, Fire TV, Apple TV (beta)', 'Avhenger av appen'],
        ['Infrarød for eldre TV-er', 'Gratis på Android-mobiler med infrarød sender (nytt)', 'Noen apper, bare på mobiler med infrarød sender'],
        ['Bluetooth', 'Beta fra Android 9, gratis', 'Avhenger av appen'],
        ['Bilder og videoer til TV-en', 'Pro, via Wi-Fi (ikke speiling)', 'Avhenger av appen'],
        ['Mobiler og datamaskiner', 'iPhone, iPad, Mac og Windows, i tillegg Android i tidlig tilgang', 'Varierer'],
        ['Skjermspeiling', 'Gratis på iPhone, iPad og Windows med den innebygde funksjonen på hver. På Windows kan Pro i tillegg speile PC-skjermen til TV-er fra LG, Samsung, Hisense og Android TV (beta)', 'Noen apper tilbyr det'],
      ],
      nota='Mando TV sammenlignes ikke med noen bestemt app. De gjeldende prisene står på butikksiden til hver enkelt app.'),
    extra=[
      ('Hva Mando TV ikke gjør', 'På iPhone og iPad leder den deg til skjermdeling i Kontrollsenter, en funksjon i selve iPhone som fungerer med TV-er med AirPlay. På Windows åpner den Cast (Windows + K), og Mando TV Pro kan sende PC-skjermen til TV-er fra LG, Samsung, Hisense og Android TV via Wi-Fi-nettverket ditt (beta, med noen sekunders forsinkelse og uten lyd). Med Mando TV Pro kan den dessuten sende bilder og videoer til TV-en via Wi-Fi-nettverket ditt. Den styrer smart-TV-er via Wi-Fi hjemme. TV-er uten smartfunksjon kan styres med infrarød fra en Android-mobil med infrarød sender. Fra Android 9 kan mobilen også koble seg til Google TV, Android TV og Fire TV via Bluetooth som tastatur og fjernkontroll, helt uten Wi-Fi. Dette alternativet er i beta og gratis.'),
      ('Hvordan Mando TV tjener penger', 'Ikke på reklame og ikke på dataene dine: Appen samler ikke inn noen. Mando TV finansieres av Pro, et valgfritt engangskjøp for ekstrafunksjoner. Den grunnleggende fjernkontrollen er gratis.'),
      ('På enhetene du allerede har', 'iPhone, iPad og Mac fra App Store, Windows-PC-er fra Microsoft Store og Android via gratis tidlig tilgang på Google Play. Se [Fjernkontroll-app for iPhone](@iphone) og [Fjernkontroll-app for Windows](@windows).'),
      ('Personvern', 'Ingen konto og ingen sporing i appen. Kommunikasjonen med TV-en skjer bare i det lokale nettverket, tilkoblingsdataene blir kryptert på enheten din. Detaljer i [personvernvilkårene](@privacidad).'),
    ],
    marca=None,
    faq=[
      ('Finnes det en fjernkontroll-app uten abonnement?', 'Ja. Mando TV har ikke noe abonnement i det hele tatt: Fjernkontrollen er gratis og uten reklame, Pro er et valgfritt engangskjøp.'),
      ('Er Mando TV virkelig gratis?', 'Ja. Piltaster, OK, Tilbake, Hjem, volum, kanaler, siffer, tastatur og av/på er gratis, uten reklame og uten tidsgrense.'),
      ('Fungerer det uten Wi-Fi?', 'Som regel ikke. Mando TV styrer smart-TV-er via Wi-Fi-nettverket hjemme. Unntak: infrarød på Android-mobiler med infrarød sender, som også fungerer med TV-er uten smartfunksjon eller uten Wi-Fi-tilkobling, og Bluetooth, i beta fra Android 9, for Google TV, Android TV og Fire TV.'),
    ]),
  dict(clave='roku-app-alt', corto='Alternativ til Roku-appen', fecha='2026-11-23',
    titulo='Alternativ til Roku-appen: enkel Roku-fjernkontroll',
    desc='Et alternativ til Roku-appen som fjernkontroll: Mando TV styrer Roku TV-er og -spillere via Wi-Fi, uten konto og reklame, i tillegg til Samsung, LG og Google TV.',
    h1='Alternativ til Roku-appen: én for alle TV-er',
    intro='Den offisielle Roku-appen kan mye: Channel Store, casting, privat lytting og en fjernkontroll. Hvis du bare vil ha en rask fjernkontroll eller også har en Samsung-, LG- eller Google TV hjemme, er Mando TV et enkelt alternativ som styrer Roku via Wi-Fi-nettverket ditt uten konto.',
    pasos=[
      'Koble mobilen og Roku-en til det samme Wi-Fi-nettverket.',
      'Last ned Mando TV og åpne den. Roku TV-en eller Roku-spilleren din dukker opp i listen. Trykk på den. Roku spør ikke om kode.',
      'Bruk piltaster, OK, Tilbake, Hjem, volum og tastaturet. Skriv søkeord i Roku-kanaler med mobiltastaturet.',
      'Hvis knappene ikke gjør noe, går du på Roku-en til Innstillinger > System > Avanserte systeminnstillinger > Kontroll fra mobilapper og setter nettverkstilgang til Standard eller Permissive (på nyere Roku-programvare setter du Kontroll fra mobilapper til Aktivert).',
      'Valgfritt: Slå på «TV-hurtigstart» på Roku TV-en under Innstillinger > System > Strøm, slik at Mando TV kan slå på TV-en.',
    ],
    extra=[
      ('Hvor Mando TV passer bedre', 'Én app for flere TV-er: Roku, Samsung, LG og Google TV eller Android TV. Uten konto, uten reklame. Den fungerer også på en Windows-PC, noe som er praktisk ved skrivebordet. Piltaster og volum reagerer raskt, og med tastaturet skriver du søkeord uten problemer.'),
      ('Hvor den offisielle Roku-appen er bedre', 'Behold Roku-appen for det den tilbyr utover fjernkontrollen, som å bla i og legge til kanaler fra Roku Channel Store samt egen casting og privat lytting (lyd i hodetelefoner på mobilen). Bruk begge hvis du vil. De kan kjøre på den samme mobilen.'),
      ('Roku TV-er og Roku-spillere', 'Begge fungerer. Det omfatter Roku TV-modeller fra TCL, Hisense, Philips og andre samt Roku Express, Streaming Stick og Ultra. Detaljer finner du på [siden om Roku fjernkontroll-appen](@roku).'),
      ('Hvis Roku-appen ikke fungerer lenger', 'Hvis knappene ikke reagerer lenger, blokkerer Roku-en som regel kontroll fra apper. Veiledningen [Roku-appen fungerer ikke](@roku-403) viser innstillingen som løser problemet.'),
      ('Gratis og Pro', 'Piltaster, OK, Tilbake, Hjem, volum, kanaler, siffertaster, tastatur, åpning av apper, bytte av innganger og av/på er gratis, uten reklame og uten abonnement. Touchpad, talekommandoer, favorittapper, rutiner og sovetimer er en del av Mando TV Pro, et engangskjøp uten abonnement.'),
    ],
    marca='roku',
    faq=[
      ('Trenger jeg en Roku-konto for å bruke Mando TV?', 'Nei. Mando TV kommuniserer med Roku-en via hjemmenettverket ditt og spør ikke om konto.'),
      ('Erstatter Mando TV Roku Mobile-appen helt?', 'Som fjernkontroll, ja. For Channel Store, casting og privat lytting beholder du den offisielle Roku-appen.'),
      ('Fungerer det med Roku Express eller Streaming Stick?', 'Ja. Alle Roku-spillere og Roku TV-er styres på samme måte.'),
    ]),
  dict(clave='lg-thinq', corto='Alternativ til LG ThinQ-appen', fecha='2026-11-23',
    titulo='Alternativ til LG ThinQ-appen: LG-fjernkontroll uten konto',
    desc='Leter du etter et alternativ til LG ThinQ-appen bare som fjernkontroll? Mando TV styrer LG-TV-er med webOS via Wi-Fi, uten LG-konto og uten reklame.',
    h1='Alternativ til LG ThinQ-appen for LG-TV-en din',
    intro='LG ThinQ er LGs offisielle app, laget for hele smarthjemmet: hvitevarer, TV-en og mer. Hvis du bare vil ha en enkel fjernkontroll for LG-TV-en din, gjør Mando TV akkurat det via Wi-Fi-nettverket hjemme, uten at du må opprette en LG-konto og uten reklame.',
    pasos=[
      'Koble mobilen eller PC-en (iPhone, Android eller Windows) og LG-TV-en til det samme Wi-Fi-nettverket.',
      'Last ned Mando TV og åpne den. LG-TV-en din dukker opp i listen av seg selv. Trykk på den.',
      'På TV-en kommer det en forespørsel. Bekreft den én gang med fjernkontrollen til TV-en, joysticken under skjermen eller Magic Remote.',
      'Knapper, volum og tastatur fungerer med en gang. Du trenger ingen LG-konto og trenger ikke registrere TV-en.',
      'Valgfritt: Slå på «Slå på TV-en med mobil» i TV-innstillingene, slik at du også kan slå på TV-en fra mobilen.',
    ],
    extra=[
      ('Mando TV eller LG ThinQ: hva til hva', 'Bruk ThinQ hvis du vil administrere LG-hvitevarer som vaskemaskin, kjøleskap eller klimaanlegg, eller trenger funksjoner knyttet til LG-kontoen. Bruk Mando TV hvis du vil ha en rask, enkel fjernkontroll for TV-en som også fungerer for Samsung, Roku og Google TV i den samme appen. Mange beholder begge: ThinQ for hvitevarene, Mando TV for TV-en.'),
      ('Hva Mando TV gjør på en LG-TV', 'Den fungerer med LG Smart-TV-er med webOS, altså de fleste modeller siden 2014, inkludert LED, NanoCell, QNED og OLED. Den gir deg piltaster, OK, Tilbake, Hjem, volum, kanaler, lyd av, avspillingskontroll og et tastatur for å skrive i YouTube, Netflix eller nettleseren. Applisten og inngangslisten er også gratis. Med Pro får du i tillegg en peker som på Magic Remote.'),
      ('Hva Mando TV ikke gjør', 'Den styrer ingen LG-hvitevarer, den bruker ikke LG-kontoen din og den erstatter ikke LG-kontotjenestene på TV-en. Det er en fjernkontroll, ikke en smarthjem-hub.'),
      ('Personvern og reklame', 'Mando TV har ingen reklame og ingen konto. Den snakker bare med TV-en innenfor hjemmenettverket ditt og lagrer tilkoblingsnøkkelen kryptert på enheten din. Du finner alle funksjonene på siden [LG fjernkontroll-app](@lg).'),
      ('Gratis og Pro', 'Piltaster, OK, Tilbake, Hjem, volum, kanaler, siffertaster, tastatur, åpning av apper, bytte av innganger og av/på er gratis, uten reklame og uten abonnement. Touchpad, talekommandoer, favorittapper, rutiner og sovetimer er en del av Mando TV Pro, et engangskjøp uten abonnement.'),
    ],
    marca='lg',
    faq=[
      ('Kan jeg styre LG-TV-en uten LG ThinQ-appen?', 'Ja. Mando TV kobler seg direkte via Wi-Fi-nettverket ditt til LG-TV-er med webOS. Du godtar en forespørsel på TV-en én gang, og det er alt, helt uten LG-konto.'),
      ('Fungerer Mando TV med pekeren til LG Magic Remote?', 'Mando TV Pro har en peker som du flytter med fingeren på mobilskjermen, på samme måte som Magic Remote flytter pilen.'),
      ('Er Mando TV fra LG?', 'Nei. Mando TV er en uavhengig app og har ingen tilknytning til LG. LG og ThinQ tilhører sine eiere og nevnes bare for å beskrive kompatibilitet.'),
    ]),
  dict(clave='smartthings', corto='SmartThings-alternativ', fecha='2026-11-23',
    titulo='Fungerer ikke SmartThings? Enkelt alternativ for Samsung',
    desc='SmartThings for tregt eller feil? Mando TV styrer Samsung-TV-er med Tizen direkte via Wi-Fi. Uten Samsung-konto, uten reklame. Steg for steg.',
    h1='SmartThings-alternativ for Samsung-TV-er',
    intro='SmartThings er Samsungs app for hele smarthjemmet, og fjernkontrollen i den går via Samsung-kontoen din. Hvis den ikke fungerer lenger eller du leter etter en rask løsning, styrer Mando TV Samsung-TV-er med Tizen, fra 2016 og nyere, direkte via Wi-Fi uten konto.',
    pasos=[
      'Koble mobilen og Samsung-TV-en til det samme Wi-Fi-nettverket.',
      'Last ned Mando TV og åpne appen. Samsung-TV-en din dukker opp i listen av seg selv. Trykk på den.',
      'TV-en spør om du vil tillate tilkoblingen. Velg «Tillat» med fjernkontrollen eller med knappen på TV-en (bare første gang).',
      'Bruk piltaster, OK, Tilbake, Hjem, volum, kanaler og tastaturet med en gang.',
      'Valgfritt: Slå på «Slå på med mobil» under Innstillinger > Generelt > Nettverk > Ekspertinnstillinger, slik at Mando TV også kan slå på TV-en.',
    ],
    extra=[
      ('Hvorfor en mobilfjernkontroll ikke fungerer lenger', 'Årsakene er som regel enkle: Mobilen og TV-en er på forskjellige Wi-Fi-nettverk, et VPN er aktivt eller TV-en er i dyp standby. Med SmartThings kan i tillegg Samsung-kontoen skape problemer, for eksempel hvis du er blitt logget ut. Mando TV snakker direkte med TV-en i hjemmenettverket, det finnes ingen konto å logge inn på. Flere tips finner du under [Mobilen finner ikke TV-en](@not-found).'),
      ('Mando TV eller SmartThings: hva til hva', 'Behold SmartThings hvis du bruker det til Samsung-hvitevarer, lamper eller andre smarthjem-enheter eller til funksjoner i Samsung-kontoen din. Bruk Mando TV hvis du bare vil ha en rask fjernkontroll for TV-en eller også har en enhet fra LG, Roku, Google TV eller Fire TV hjemme: Én app styrer alle. Begge appene kan være installert på den samme mobilen.'),
      ('Hvis du avslo tillatelsen ved en feil', 'Gå på TV-en til Innstillinger > Generelt > Ekstern enhetsbehandling > Enhetstilkoblingsbehandling og sett Mando TV til tillatt.'),
      ('Ingen fjernkontroll?', 'Du kan bekrefte forespørselen med knappen på selve TV-en. Veiledningen [Samsung-TV uten original fjernkontroll](@samsung-lost) viser deg hvordan.'),
      ('Gratis og Pro', 'Fjernkontrollen kan du laste ned og bruke gratis, uten reklame og uten abonnement. Mando TV Pro er et valgfritt engangskjøp for ekstrafunksjoner.'),
    ],
    marca='samsung',
    faq=[
      ('Kan jeg styre Samsung-TV-en uten SmartThings?', 'Ja. Mando TV kobler seg direkte via Wi-Fi-nettverket ditt til Samsung-TV-er med Tizen. Du tillater tilkoblingen én gang på TV-en, uten Samsung-konto.'),
      ('Styrer Mando TV også Samsung-hvitevarer?', 'Nei. Det er bare en fjernkontroll for TV-en. For hvitevarer og andre smarthjem-enheter beholder du SmartThings.'),
      ('Er Mando TV fra Samsung?', 'Nei. Mando TV er en uavhengig app og har ingen tilknytning til Samsung. Samsung og SmartThings tilhører sine eiere og nevnes bare for å beskrive kompatibilitet.'),
    ]),
  dict(clave='googletv-alt', corto='Alternativ til Google TV-fjernkontrollen', fecha='2026-11-23',
    titulo='Fungerer ikke Google TV-fjernkontrollen? Alternativet',
    desc='Finner ikke mobilfjernkontrollen for Google TV TV-en? Mando TV styrer Google TV og Android TV via Wi-Fi, uten Google-konto og reklame.',
    h1='Alternativ til Google TV-fjernkontrollen på mobilen',
    intro='Mobilfjernkontrollen for Google TV og Android TV ligger i Googles egen app og er knyttet til Google-kontoen din. Finner den ikke TV-en, kommer du ikke videre. Mando TV er en separat fjernkontroll-app som parer seg med koden på 6 tegn på skjermen og fungerer uten Google-konto, på en iPhone, en Android-mobil eller en Windows-PC.',
    pasos=[
      'Slå på TV-en og koble mobilen til det samme Wi-Fi-nettverket.',
      'Last ned Mando TV og åpne appen. Trykk i listen på TV-en din med Google TV eller Android TV.',
      'TV-en viser en kode med 6 tegn. Skriv den inn i Mando TV og trykk på Pare.',
      'Bruk piltaster, OK, Tilbake, Hjem, volum og tastaturet. Du trenger ikke logge inn noe sted.',
      'Valgfritt: Se i innstillingene på TV-en etter Wake on LAN eller «Slå på via nettverk», slik at appen også kan slå på TV-en.',
    ],
    extra=[
      ('Hvorfor mobilfjernkontrollen ikke finner TV-en lenger', 'Som regel skyldes det nettverket: Mobilen og TV-en er på forskjellige Wi-Fi-nettverk, et VPN er aktivt eller et gjestenettverk skiller enhetene. Fiks det først, siden det rammer alle fjernkontroll-apper. Mer i [Mobilen finner ikke TV-en](@not-found).'),
      ('Hvilke TV-er det fungerer med', 'TV-er med Google TV og Android TV fra Sony, TCL, Hisense, Philips, Sharp, Xiaomi, Toshiba og flere, samt Chromecast med Google TV, Google TV Streamer og Nvidia Shield. Alle pares på samme måte, én gang med koden på skjermen.'),
      ('Hvor Googles app er bedre', 'Googles app hjelper deg også med å finne innhold å se og husker overvåkningslisten din. Behold den til det. Mando TV er bare fjernkontrollen og styrer i tillegg Samsung, LG, Roku og Fire TV-enheter fra den samme appen samt fra en Windows-PC.'),
      ('Hvis den gamle Android TV-fjernkontroll-appen mangler', 'Google har flyttet mobilfjernkontrollen fra den gamle appen Android TV Remote Control til Google TV-appen. Leter du etter en egen fjernkontroll, er Mando TV et alternativ.'),
      ('Gratis og Pro', 'Fjernkontrollen kan du laste ned og bruke gratis, uten reklame og uten abonnement. Mando TV Pro er et valgfritt engangskjøp for ekstrafunksjoner.'),
    ],
    marca='android',
    faq=[
      ('Trenger jeg en Google-konto for å bruke Mando TV med Google TV?', 'Nei. Koden på TV-en er nok til paring.'),
      ('Fungerer det med Chromecast med Google TV?', 'Ja. Paringen fungerer på samme måte, med koden på 6 tegn på skjermen.'),
      ('Kan jeg bruke det fra en iPhone?', 'Ja. Mando TV finnes i App Store for iPhone og iPad, i Microsoft Store for Windows og i den gratis tidlige tilgangen på Google Play for Android.'),
    ]),
  dict(clave='windows', corto='Fjernkontroll for Windows-PC', fecha='2026-11-23',
    titulo='Fjernkontroll-app for Windows: Styr TV-en fra PC-en',
    desc='Styr Samsung, LG, Roku, Google TV eller Fire TV fra en Windows-PC med Mando TV: hurtigtaster, minifjernkontroll og Wi-Fi. I Microsoft Store.',
    h1='Fjernkontroll-app for Windows-PC',
    intro='Mando TV har en Windows-app som gjør PC-en eller den bærbare datamaskinen din til fjernkontroll for TV-en via hjemmenettverket. Skriv på TV-en med det ekte tastaturet ditt, la et lite fjernkontrollvindu ligge øverst mens du jobber og styr Samsung, LG, Roku, Google TV eller Fire TV med den samme appen.',
    pasos=[
      'Installer Mando TV gratis fra Microsoft Store på en PC med Windows 10 eller 11.',
      'Sørg for at PC-en og TV-en er på det samme nettverket, via Wi-Fi eller kabel til den samme ruteren.',
      'Åpne Mando TV. TV-en dukker opp i listen. Klikk på den.',
      'Bekreft forespørselen på TV-en hvis den spør (LG, Samsung), eller skriv inn koden som vises (Google TV, Fire TV).',
      'Klikk på knappene eller skriv et søk med tastaturet. Ferdig.',
    ],
    extra=[
      ('Hurtigtaster (Pro)', 'Med Pro blir PC-tastaturet en fjernkontroll: piltaster for å bevege seg, Enter for OK, Backspace eller Esc for å gå tilbake, pluss og minus for volum, M for lyd av og mellomrom for pause.'),
      ('Minifjernkontroll (Pro)', 'Et lite fjernkontrollvindu som blir liggende over alle andre vinduer. Slik endrer du volumet eller pauser uten å avbryte arbeidet.'),
      ('Skrive på TV-en fra PC-en', 'Skjermtastaturet på en TV er tregt. I Mando TV skriver du med det ekte tastaturet ditt, og teksten havner i søkefeltet på TV-en. Denne delen er gratis.'),
      ('Flere detaljer', 'Veiledningen steg for steg finner du under [Styr TV-en fra PC-en](@pc). For mobilen, les [Mobilen som fjernkontroll via Wi-Fi](@wifi).'),
      ('Gratis og Pro', 'Piltaster, OK, Tilbake, Hjem, volum, kanaler, siffertaster, tastatur, åpning av apper, bytte av innganger og av/på er gratis, uten reklame og uten abonnement. Touchpad, talekommandoer, favorittapper, rutiner og sovetimer er en del av Mando TV Pro, et engangskjøp uten abonnement. På Windows kjøper du Pro via Microsoft Store.'),
      ('Talekommandoer fra PC-en (Pro)', 'Med Pro kan du snakke med TV-en via mikrofonen på PC-en. Talen gjenkjennes direkte på PC-en: Du trenger ikke internett og trenger ikke stille inn noe i Windows. Det du sier forlater aldri PC-en og blir ikke lagret. Bare på svært gamle prosessorer faller appen tilbake på taleinndata fra Windows. Da må nettbasert talegjenkjenning være slått på i personverninnstillingene og språket ditt være lagt til i Windows.'),
    ],
    marca=None,
    faq=[
      ('Trenger fjernkontroll-appen for Windows Bluetooth eller kabel?', 'Nei. Den bruker hjemmenettverket ditt. PC-en og TV-en må bare være koblet til den samme ruteren.'),
      ('Hvilke TV-er kan jeg styre fra Windows?', 'Samsung-TV-er med Tizen, LG-TV-er med webOS, Roku TV og -spillere, Google TV og Android TV samt Fire TV.'),
      ('Kan jeg se TV-bildet på PC-en eller høre det i PC-høyttalerne?', 'Nei. Mando TV er bare en fjernkontroll. Den speiler eller strømmer ikke TV-bildet til datamaskinen.'),
      ('Hvorfor fungerer ikke talen på Windows-PC-en min?', 'Talestyring er en Pro-funksjon. Sjekk altså at Pro er aktiv og at mikrofonen på PC-en fungerer. På de fleste PC-er gjenkjennes talen direkte på PC-en, uten internett. Bare på svært gamle prosessorer bruker appen taleinndata fra Windows: Slå da på nettbasert talegjenkjenning i personverninnstillingene i Windows og legg til språket ditt i språkinnstillingene.'),
    ]),
  dict(clave='iphone', corto='Fjernkontroll-app for iPhone', fecha='2026-11-23',
    titulo='Fjernkontroll-app for iPhone: Samsung, LG, Roku, Google TV',
    desc='Bruk iPhone som fjernkontroll for Samsung, LG, Roku, Google TV og Fire TV via Wi-Fi. Gratis i App Store, uten konto og uten reklame.',
    h1='Fjernkontroll-app for iPhone: én for alle TV-er',
    intro='Mando TV gjør iPhone eller iPad til fjernkontroll for Samsung, LG, Roku, Google TV eller Android TV samt Fire TV, via Wi-Fi-nettverket hjemme. Appen er gratis i App Store, uten konto og uten reklame. Den kjører også på Android og Windows.',
    pasos=[
      'Last ned Mando TV gratis fra App Store.',
      'Koble iPhone og TV-en til det samme Wi-Fi-nettverket.',
      'Åpne Mando TV og trykk på Tillat når iOS spør om tilgang til det lokale nettverket. Appen trenger det for å finne TV-en.',
      'Trykk på TV-en din i listen. Bekreft forespørselen på TV-en hvis den spør (LG og Samsung), eller skriv inn koden som TV-en viser (Google TV eller Fire TV).',
      'Bruk knappene, volumet og tastaturet. Du er koblet til.',
    ],
    extra=[
      ('Fungerer med disse TV-ene', 'LG webOS, Samsung Tizen (fra 2016 og nyere), Roku TV og Roku-spillere, Google TV og Android TV samt Fire TV. Merkesidene er [Samsung](@samsung), [LG](@lg), [Roku](@roku) og [Android TV](@android).'),
      ('Hvorfor den spør om lokalt nettverk', 'iPhone blokkerer tilgangen for apper til enheter i hjemmenettverket ditt med mindre du tillater det. Dukker ikke TV-en opp i listen, åpner du Innstillinger > Mando TV og slår på «Lokalt nettverk». Appen kommuniserer bare med TV-en din innenfor hjemmenettverket ditt.'),
      ('Hvorfor Mando TV og ikke appen til produsenten', 'Hvert TV-merke har sin egen app og vil ha et eget oppsett eller en egen konto. Mando TV er én app for alle, uten konto.'),
      ('Gratis og Pro på iPhone', 'Piltaster, OK, Tilbake, Hjem, volum, kanaler, siffertaster, tastatur, åpning av apper, bytte av innganger og av/på er gratis, uten reklame og uten abonnement. Touchpad, talekommandoer, favorittapper, rutiner og sovetimer er en del av Mando TV Pro, et engangskjøp uten abonnement. Du kjøper Pro én gang direkte i appen.'),
    ],
    marca=None,
    faq=[
      ('Er Mando TV gratis på iPhone?', 'Nedlastingen er gratis, uten reklame. Den grunnleggende fjernkontrollen er gratis, det samme er åpning av apper og bytte av innganger. Ekstrafunksjoner som touchpad, talekommandoene og rutinene hører til Mando TV Pro, et engangskjøp.'),
      ('Fungerer det på iPad?', 'Ja. Den samme appen kjører på iPhone og iPad.'),
      ('Trenger en fjernkontroll-app for iPhone Bluetooth eller en infrarød sender?', 'Ikke på iPhone. iPhone har ingen infrarød sender, derfor er infrarød styring ikke tilgjengelig der, og Bluetooth-alternativet finnes bare for Android 9 eller nyere, ikke for iPhone. På iPhone styrer Mando TV smart-TV-er samt Apple TV (beta) via Wi-Fi-nettverket hjemme.'),
    ]),
  dict(clave='firetv', corto='Fire TV-fjernkontroll', fecha='2026-11-23',
    titulo='Fire TV-fjernkontroll-app for mobil og PC',
    desc='Fire TV-fjernkontroll på mobilen: Styr Fire TV Stick, Fire TV Cube eller en TV med Fire TV via Wi-Fi, med 4-sifret PIN. Uten Amazon-app.',
    h1='Fire TV-fjernkontroll for mobilen eller PC-en din',
    intro='Når Fire TV-fjernkontrollen er borte eller batteriene er tomme, styrer Mando TV en Fire TV Stick, en Fire TV Cube eller en TV med innebygd Fire TV via Wi-Fi. Paringen skjer med en 4-sifret PIN. Fire TV er nytt i Mando TV, så oppdater appen først.',
    pasos=[
      'Oppdater Mando TV til den nyeste versjonen fra App Store, Microsoft Store eller Google Play.',
      'Slå på Fire TV og koble mobilen til det samme Wi-Fi-nettverket.',
      'Åpne Mando TV. Fire TV-en din dukker opp i listen. Trykk på den.',
      'På skjermen til TV-en vises en 4-sifret PIN. Skriv den inn i Mando TV. Det gjør du bare én gang.',
      'Bruk piltaster, OK, Tilbake, Hjem, avspillingstaster og tastaturet for søk.',
    ],
    extra=[
      ('Støttede Fire TV-enheter', 'Fire TV Stick, Fire TV Stick 4K, Fire TV Cube og TV-er med innebygd Fire TV, som TV-er i Amazon Fire TV Edition og noen Hisense-modeller. Støtten er ny, og vi har til nå bare kunnet teste noen få ekte enheter. Hvis noe ikke fungerer som forventet, skriv til oss med modellen din via hjelpesiden.'),
      ('Slå på Fire TV', 'Mando TV slår ikke på en Fire TV via nettverket. Slå på TV-en med av/på-knappen på selve TV-en: En innkoblet Fire TV Stick eller Cube våkner som regel via HDMI-CEC, og på en TV med innebygd Fire TV er TV-en selve Fire TV-en. Etterpå styrer du den fra mobilen.'),
      ('Hvis Fire TV-en ikke dukker opp', 'Sørg for at begge enhetene er på det samme Wi-Fi-nettverket og at Fire TV-en er våken. På en iPhone tillater du «Lokalt nettverk» for Mando TV i innstillingene. Se [Mobilen finner ikke TV-en](@not-found).'),
      ('Ingen fjernkontroll i det hele tatt?', 'Fire TV må vise PIN-en på skjermen, så TV-en og Fire TV-en må være på og vise et bilde. Står TV-en på feil inngang, bytter du den med knappene på TV-en. Se [Bytt inngang uten fjernkontroll](@hdmi).'),
      ('Gratis og Pro', 'Piltaster, OK, Tilbake, Hjem, volum, kanaler, siffer, tastatur, åpning av apper, bytte av innganger og av/på er gratis, uten reklame og uten abonnement. Touchpad, talekommandoer, favorittapper, rutiner og sovetimer er en del av Mando TV Pro, et engangskjøp uten abonnement.'),
    ],
    marca=None,
    faq=[
      ('Trenger jeg Amazon Fire TV-appen?', 'Nei. Mando TV kobler seg via Wi-Fi-nettverket ditt til Fire TV-en med PIN. Du trenger ingen Amazon-konto på mobilen.'),
      ('Fungerer det med TV-er med Fire TV og med Fire TV Sticks?', 'Ja, det er nettopp det det er laget for. Støtten er ny, hold appen oppdatert og fortell oss om modeller som ikke fungerer som forventet.'),
      ('Hvorfor trenger jeg en PIN?', 'Fire TV viser en 4-sifret PIN for å bevise at du sitter foran TV-en. Ingen kan pare uten å se skjermen.'),
    ]),
  dict(clave='firetv-lost', corto='Mistet Fire TV-fjernkontrollen', fecha='2026-11-23',
    titulo='Mistet Fire TV-fjernkontrollen? Slik hjelper mobilen',
    desc='Mistet fjernkontrollen til Fire TV Stick? Styr den via Wi-Fi med mobilen, paret med en 4-sifret PIN. Tips for nytt Wi-Fi og HDMI-CEC.',
    h1='Mistet Fire TV-fjernkontrollen: Slik bruker du mobilen',
    intro='Hvis fjernkontrollen til Fire TV Stick, Fire TV Cube eller smart-TV-en med Fire TV er mistet eller ikke fungerer lenger, overtar mobilen styringen så lenge Fire TV-en fortsatt er koblet til Wi-Fi-nettverket ditt. Paringen skjer med en 4-sifret PIN på skjermen, slik at du aldri trenger den gamle fjernkontrollen til det.',
    pasos=[
      'Slå på TV-en med knappen på selve TV-en. En innkoblet Fire TV Stick eller Cube våkner som regel også; med HDMI-CEC på bytter TV-en ofte automatisk til inngangen.',
      'Viser TV-en en annen inngang, bytter du den med inngangs- eller kildeknappen på TV-en. Se [Bytt inngang uten fjernkontroll](@hdmi).',
      'Koble mobilen til det samme Wi-Fi-nettverket som Fire TV-en.',
      'Last ned Mando TV og åpne appen. Fire TV-en din dukker opp i listen. Trykk på den.',
      'TV-en viser en 4-sifret PIN. Skriv den inn i Mando TV. Det gjør du bare én gang.',
      'Bruk piltaster, OK, Tilbake, Hjem, volum, avspillingstaster og tastaturet på mobilen.',
    ],
    extra=[
      ('Test først TV-fjernkontrollen (HDMI-CEC)', 'Mange TV-fjernkontroller kan styre en Fire TV Stick via HDMI-CEC. Når Fire TV-grensesnittet er synlig, trykker du på pilene og OK på TV-ens fjernkontroll. Skjer det ingenting, slår du på CEC i innstillingene på TV-en (Anynet+ hos Samsung, SIMPLINK hos LG, BRAVIA Sync hos Sony) og på Fire TV-en HDMI-CEC-enhetskontroll i skjerminnstillingene («Display og lyd»).'),
      ('Hvis du har byttet Wi-Fi', 'Uten fjernkontroll kan du ikke skrive inn det nye Wi-Fi-passordet på Fire TV-en, men det finnes en utvei: Opprett en hotspot på en annen mobil med nøyaktig det samme navnet og passordet som det gamle Wi-Fi-nettverket ditt. Fire TV-en kobler seg automatisk til det. Koble mobilen med Mando TV til denne hotspoten, par den med PIN-en, gå deretter på Fire TV-en til Innstillinger > Nettverk og velg det nye Wi-Fi-nettverket ditt. Koble til slutt også mobilen til det nye Wi-Fi-nettverket.'),
      ('Pare en ny fjernkontroll', 'De fleste nye Fire TV-fjernkontroller parer du ved å holde inne Hjem-knappen i omtrent 10 sekunder, i nærheten av Fire TV-en. Hvis det ikke fungerer, åpner du Innstillinger > Kontrollere og Bluetooth-enheter > Amazon Fire TV-fjernkontroller > Legg til ny fjernkontroll. Denne menyen når du også fra mobilen med Mando TV.'),
      ('Fire TV innebygd i TV-en', 'På TV-er med innebygd Fire TV, som mange modeller fra Insignia og Toshiba, fungerer de samme stegene, siden TV-en selv er Fire TV-en.'),
      ('Før du begynner', 'Fire TV-støtten er ny i Mando TV. Oppdater appen først. Reagerer modellen din ikke som forventet, skriv til oss via [hjelpesiden](@soporte) og oppgi modellen.'),
      ('Gratis og Pro', 'Fjernkontrollen kan du laste ned og bruke gratis, uten reklame og uten abonnement. Mando TV Pro er et valgfritt engangskjøp for ekstrafunksjoner.'),
    ],
    marca=('firetv', 'Fire TV-fjernkontroll'),
    faq=[
      ('Kan jeg styre en Fire TV Stick med mobilen uten fjernkontrollen?', 'Ja, så lenge Fire TV-en er på og koblet til Wi-Fi-nettverket ditt. Mando TV parer med den 4-sifrede PIN-en på TV-en, så du trenger ikke den gamle fjernkontrollen.'),
      ('Fungerer det hvis Fire TV-en er på et nytt Wi-Fi-nettverk?', 'Ikke direkte, siden mobilen og Fire TV-en må være på det samme nettverket. Få Fire TV-en på nett igjen først med hotspot-trikset på denne siden.'),
      ('Trenger jeg Amazon Fire TV-appen eller en Amazon-konto?', 'Nei. Mando TV kobler seg via hjemmenettverket ditt med PIN-en og trenger ingen egen konto.'),
    ]),
  dict(clave='turn-on', corto='Slå på TV-en uten fjernkontroll', fecha='2026-11-23',
    titulo='Slå på TV-en uten fjernkontroll (alle merker)',
    desc='Slå på TV-en uten fjernkontroll: Hvor knappen sitter på Samsung, LG, TCL, Hisense og Sony. Pluss HDMI-CEC og mobiltriks.',
    h1='Slik slår du på en TV uten fjernkontroll',
    intro='Nesten alle TV-er har fortsatt en fysisk av/på-knapp. Den er bare godt gjemt. Her ser du hvor den sitter på hvert merke, pluss to måter å slippe å lete neste gang: HDMI-CEC fra en konsoll eller en strømmeenhet, og påslåing av TV-en med mobilen via Wi-Fi.',
    pasos=[
      'Se under midten av skjermen, rett bak merkelogoen. Mange TV-er har en liten enkeltknapp eller en joystick der, som peker nedover.',
      'Er den ikke der, kjenn deg frem på baksiden av TV-en nær de nedre hjørnene, deretter langs venstre og høyre kant.',
      'Trykk på knappen én gang. På mange TV-er med bare én knapp åpner et kort trykk, mens TV-en er på, en liten meny for innganger og volum, og et langt trykk slår den av.',
      'Fortsatt ingenting? Sjekk strømkabelen i begge ender og prøv en annen stikkontakt. Lyser ikke standby-lampen, får ikke TV-en strøm.',
      'Så snart TV-en er på, setter du den opp slik at du ikke trenger knappen lenger: Slå på HDMI-CEC og påslåing via nettverket, begge forklart lenger ned.',
    ],
    extra=[
      ('Hvor av/på-knappen sitter, per merke', 'Samsung: en kontrollknapp eller en joystick under midten av skjermen eller på baksiden i et nedre hjørne. LG: en joystick-knapp under LG-logoen på de fleste modeller. TCL og Hisense: som regel en liten knapp under midten av skjermen eller på baksiden nær et nedre hjørne. Sony: på baksiden eller på en sidekant, nede nær kanten. Vizio: på baksiden, nede til venstre eller nede til høyre, eller på siden. Plasseringen varierer fra modell til modell. Finner du den ikke, søk opp bruksanvisningen med modellnummeret på klistremerket på baksiden.'),
      ('Slå på TV-en via en konsoll eller en strømmeenhet (HDMI-CEC)', 'Med HDMI-CEC på slår påslåing av en PlayStation, en Xbox, en Roku-spiller, en Fire TV Stick eller en Chromecast også på TV-en og bytter til riktig inngang. Hvert merke kaller innstillingen noe forskjellig: Anynet+ hos Samsung, SIMPLINK hos LG, BRAVIA Sync hos Sony og CEC hos de fleste andre. Mer i [Slå på TV-en og bytt til HDMI for konsollen](@console).'),
      ('Slå på TV-en med mobilen', 'Smart-TV-er kan vekkes via Wi-Fi hvis du tillater det én gang, og da slår Mando TV dem på fra mobilen. På Samsung slår du på «Slå på med mobil» under Innstillinger > Generelt > Nettverk > Ekspertinnstillinger. På LG slår du på «Slå på TV-en med mobil» ([steg for steg](@lg-on)). På en Roku TV slår du på «TV-hurtigstart» under Innstillinger > System > Strøm. På Google TV og Android TV leter du etter Wake on LAN eller «Slå på via nettverk» hvis modellen din har det. Det gjør du én gang, mens TV-en er på.'),
      ('Hvis du ikke finner noen knapp', 'Noen nyere TV-er gjemmer den eneste knappen så godt at det virker som om det ikke finnes noen. Se etter en liten bule eller et lyssensorområde under skjermen: Knappen sitter ofte rett ved siden av. Via Wi-Fi trenger Mando TV at TV-en har vært på én gang og er tilkoblet. Infrarød er unntaket: På en Android-mobil med infrarød sender kan Mando TV slå på en TV som aldri er blitt satt opp, så lenge du retter mobilen mot TV-en. Infrarød er nytt og fungerer med merkene i appens kodeliste.'),
      ('Gratis og Pro', 'Fjernkontrollen kan du laste ned og bruke gratis, uten reklame og uten abonnement. Mando TV Pro er et valgfritt engangskjøp for ekstrafunksjoner.'),
    ],
    marca=None,
    faq=[
      ('Kan jeg slå på en TV med mobilen hvis jeg aldri har satt den opp?', 'Ikke via Wi-Fi. En avslått TV våkner bare fra nettverket hvis påslåing via nettverket var slått på på forhånd. Første gang bruker du knappen på TV-en. Unntaket er en Android-mobil med infrarød sender: Mando TV kan slå på en TV uten oppsett via infrarød hvis merket står i kodelisten eller du velger «Annet merke eller vet ikke».'),
      ('Hvordan slår jeg på en Samsung-TV uten fjernkontroll?', 'Trykk på kontrollknappen under midten av skjermen eller på baksiden i et nedre hjørne. Slå deretter på «Slå på med mobil», slik at mobilen kan slå den på neste gang.'),
      ('Hvordan slår jeg på en Roku TV uten fjernkontroll?', 'Bruk knappen på TV-en, som regel under midten eller på baksiden. Slå deretter på «TV-hurtigstart» under Innstillinger > System > Strøm, slik at Mando TV kan slå den på fra mobilen.'),
      ('Hvorfor slår TV-en seg på av seg selv når jeg slår på konsollen?', 'Det er HDMI-CEC. Det er praktisk, og du kan slå det av i TV-innstillingene hvis du foretrekker det.'),
    ]),
  dict(clave='sony', corto='Sony-fjernkontroll', fecha='2026-11-23',
    titulo='Sony fjernkontroll-app for mobil og PC',
    desc='Mando TV styrer Sony Bravia-TV-er med Google TV eller Android TV via Wi-Fi. Betastøtte for modeller fra 2013 til 2015 uten Android.',
    h1='Slik styrer du Sony-TV-en med mobilen',
    intro='Nyere Sony Bravia Smart-TV-er bruker Google TV, eldre modeller fra 2015 bruker Android TV. Mando TV styrer begge via Wi-Fi-nettverket ditt fra iPhone, Android-mobil eller Windows-PC. Appen erstatter den originale fjernkontrollen når den er mistet eller batteriene er tomme.',
    pasos=[
      'Sjekk at Sony-TV-en viser startskjermen til Google TV eller Android TV. Det gjelder de fleste Sony Bravia Smart-TV-er fra 2015.',
      'Koble mobilen og TV-en til det samme Wi-Fi-nettverket.',
      'Åpne Mando TV og trykk på Sony-TV-en din i listen.',
      'Skriv inn koden på 6 tegn som TV-en viser på skjermen (bare første gang). Du trenger ingen fjernkontroll til dette.',
      'Bruk piltaster, OK, Tilbake, Hjem, volum og tastaturet.',
    ],
    extra=[
      ('Slå på en Sony-TV fra mobilen', 'Sony-modeller med Google TV eller Android TV kan vekkes via nettverket hvis «Remote start» er slått på. Alternativet finner du som regel under Innstillinger > Nettverk og internett > Remote start (stien kan avvike litt fra modell til modell). Trykk deretter på TV-en i Mando TV mens den er avslått, så slår appen den på.'),
      ('Hvor av/på-knappen sitter på en Sony', 'På de fleste Bravia-TV-er sitter den på baksiden, nær nedre venstre eller høyre hjørne, eller på en sidekant. Et kort trykk slår på TV-en. Mer finner du i [Slå på TV-en uten fjernkontroll](@turn-on).'),
      ('Eldre Sony-TV-er', 'Sony Bravia-TV-er fra 2013 til 2015 som ikke bruker Android, støttes i Mando TV i betastatus. Det er nytt og kan fortsatt ha noen skjønnhetsfeil. TV-en viser en 4-sifret PIN som du må skrive inn i appen. Andre Sony-TV-er uten Google TV eller Android TV støttes foreløpig ikke.'),
      ('Gratis og Pro', 'Fjernkontrollen kan du laste ned og bruke gratis, uten reklame og uten abonnement. Mando TV Pro er et valgfritt engangskjøp for ekstrafunksjoner.'),
    ],
    marca='android',
    faq=[
      ('Fungerer Mando TV med Sony Bravia-TV-er?', 'Ja, med Sony-TV-er som bruker Google TV eller Android TV. Det omfatter de fleste Sony Smart-TV-er fra 2015.'),
      ('Trenger jeg en Sony-app eller en Google-konto?', 'Nei. Mando TV parer seg med koden på TV-skjermen og krever ingen konto.'),
      ('Fungerer det med eldre Sony Bravia-TV-er uten Android?', 'Ja, i betastatus, på Bravia-modeller fra 2013 til 2015 uten Android. Paringen skjer med en 4-sifret PIN som vises på TV-en.'),
      ('Kan jeg skrive på Sony-TV-en fra mobilen?', 'Ja. Tastaturet er gratis og fungerer i YouTube, Netflix og TV-søket.'),
    ]),
  dict(clave='tcl', corto='TCL-fjernkontroll', fecha='2026-11-23',
    titulo='TCL fjernkontroll-app for mobil og PC',
    desc='Mistet TCL-fjernkontrollen? De fleste TCL-TV-er bruker Roku TV eller Google TV. Mando TV styrer begge via Wi-Fi, uten konto og reklame.',
    h1='Slik styrer du TCL-TV-en med mobilen',
    intro='TCL bygger TV-en, men programvaren er Roku TV eller Google TV (på eldre modeller Android TV). Mando TV styrer begge systemene og fungerer som fjernkontroll for TCL-TV-en din via Wi-Fi. Gratis, uten konto og reklame.',
    pasos=[
      'Finn ut hvilket system TCL-en din bruker. Viser startskjermen et enkelt rutenett med kanalruter, er det Roku TV. Ser den ut som Google TV eller Android TV med rader fulle av anbefalinger, er det Google TV.',
      'Koble mobilen og TCL-TV-en til det samme Wi-Fi-nettverket.',
      'Åpne Mando TV. TCL-en dukker opp i listen av seg selv. Trykk på den.',
      'På en TCL med Roku TV trengs ikke noe mer. På en TCL med Google TV skriver du inn koden på 6 tegn som TV-en viser på skjermen (bare første gang).',
      'Bruk pilene, OK, Tilbake, Hjem, volum og tastatur. Slå på TV-en fra appen hvis du har slått på påslåing via nettverket (se nedenfor).',
    ],
    extra=[
      ('Slå på en TCL-TV fra mobilen', 'På TCL Roku TV slår du på «TV-hurtigstart» under Innstillinger > System > Strøm. På TCL Google TV leter du etter et alternativ for Wake on LAN, «Slå på via nettverk» eller fjernstart i nettverks- eller strøminnstillingene. Noen modeller tilbyr ikke dette. Slå i så fall på TV-en med den fysiske av/på-knappen, som regel nederst på midten eller på baksiden.'),
      ('Hvis TCL-en din ikke dukker opp', 'Sjekk at mobilen og TV-en er på det samme Wi-Fi-nettverket. Rutere med atskilte 2,4 GHz- og 5 GHz-nett kan skjule enheter for hverandre. På iPhone tillater du «Lokalt nettverk» for Mando TV i innstillingene. Du kan også legge til TV-en ved å skrive inn IP-adressen. Les [Mobilen finner ikke TV-en](@not-found).'),
      ('Mer om TCL-en din', 'For TCL med Roku TV, se [Roku fjernkontroll-app](@roku), for TCL med Google TV eller Android TV [Android TV fjernkontroll-app](@android).'),
      ('Gratis og Pro', 'Piltaster, OK, Tilbake, Hjem, volum, kanaler, siffer, tastatur, åpning av apper, bytte av innganger og av/på er gratis, uten reklame og abonnement. Touchpad, talekommandoer, favorittapper, rutiner og sovetimer er en del av Mando TV Pro, et engangskjøp uten abonnement.'),
    ],
    marca=None,
    faq=[
      ('Fungerer Mando TV med alle TCL-TV-er?', 'Det fungerer med TCL-TV-er med Roku TV, Google TV eller Android TV, altså de fleste TCL Smart-TV-er. En TCL som ikke er en smart-TV, kan ikke styres via Wi-Fi.'),
      ('Trenger jeg TCL-appen eller en TCL-konto?', 'Nei. Mando TV kobler seg direkte via Wi-Fi-nettverket ditt hjemme og trenger ingen konto.'),
      ('TCL-en min spør om en kode. Hvor er den?', 'TCL-modeller med Google TV og Android TV viser en kode på 6 tegn på skjermen. Skriv den inn i Mando TV akkurat slik den vises. En TCL med Roku TV spør ikke om kode.'),
    ]),
  dict(clave='hisense', corto='Hisense-fjernkontroll', fecha='2026-11-23',
    titulo='Hisense fjernkontroll-app: Hva som fungerer på mobilen',
    desc='Hisense-fjernkontroll med Mando TV: Styring for VIDAA, Roku TV, Google TV og Fire TV via Wi-Fi. Ærlig oversikt over hva som fungerer.',
    h1='Hisense fjernkontroll-app: hva som fungerer og hva som ikke gjør det',
    intro='Hisense-TV-er er ikke like på innsiden. Avhengig av modell bruker de Hisenses eget VIDAA-system, Roku TV, Google TV eller Fire TV. Mando TV fungerer som fjernkontroll for Hisense på alle fire systemene, med ett unntak på noen nyere VIDAA-modeller. Her ser du hvordan du finner ut hvilket system du har og hva du kan forvente.',
    pasos=[
      'Sjekk hvilket system Hisense-en din bruker. VIDAA er Hisenses eget grensesnitt. Roku TV viser et rutenett med kanalruter. Google TV viser rader med anbefalinger. Fire TV viser Fire TV-startskjermen med Amazon-rader.',
      'Koble mobilen og Hisense-TV-en til det samme Wi-Fi-nettverket.',
      'Åpne Mando TV. TV-en dukker opp i listen av seg selv. Trykk på den.',
      'VIDAA- og Fire TV-modeller viser kanskje en PIN med fire sifre; Google TV viser en kode med seks tegn. Skriv den inn i appen. Roku TV spør ikke om noe. Det gjør du bare én gang.',
      'Bruk pilene, OK, Tilbake, Hjem, volum og tastatur fra mobilen.',
    ],
    extra=[
      ('Hisense med Roku TV eller Google TV', 'Disse fungerer fullt ut som alle andre Roku- eller Google TV-er. Detaljer på sidene [Roku fjernkontroll-app](@roku) og [Android TV fjernkontroll-app](@android).'),
      ('Hisense med Fire TV', 'Støtten for Fire TV er ny i Mando TV. Oppdater appen til den nyeste versjonen fra butikken din. Hvordan paringen med PIN fungerer, står på siden [Fire TV fjernkontroll-app](@firetv). Hvis noe ikke fungerer som forventet, skriv til oss via hjelpesiden og oppgi modellen din.'),
      ('Hisense med VIDAA', 'De fleste VIDAA-modeller fungerer: knapper, volum, tastatur, apper og innganger. Noen nyere VIDAA-modeller godtar bare den offisielle Hisense-appen. Mando TV oppdager det ved tilkobling og sier det tydelig, i stedet for å svikte i det stille. I så fall er Hisense-appen for modellen din, knappene på TV-en eller den originale fjernkontrollen riktig vei.'),
      ('Slå på en Hisense fra mobilen', 'På Hisense Roku TV slår du på «TV-hurtigstart» under Innstillinger > System > Strøm. På Google TV leter du etter et alternativ for Wake on LAN eller «Slå på via nettverk». Finnes det ikke, bruker du av/på-knappen på TV-en.'),
      ('Gratis og Pro', 'Piltaster, OK, Tilbake, Hjem, volum, kanaler, siffertaster, tastatur, åpning av apper, bytte av innganger og av/på er gratis, uten reklame og uten abonnement. Touchpad, talekommandoer, favorittapper, rutiner og sovetimer er en del av Mando TV Pro, et engangskjøp uten abonnement.'),
    ],
    marca=None,
    faq=[
      ('Fungerer Mando TV med Hisense VIDAA?', 'Ja, med de fleste VIDAA-modeller. Noen nyere godtar bare den offisielle Hisense-appen; Mando TV oppdager det og sier det til deg. Hisense-TV-er med Roku TV, Google TV eller Fire TV støttes også.'),
      ('Hvordan vet jeg om Hisense-en min er Roku TV, Google TV eller Fire TV?', 'Se på startskjermen. Roku TV har et enkelt rutenett og en Roku-logo ved oppstart. Google TV har rader med anbefalinger. Fire TV har startskjermen til Amazon Fire TV. Modellnavnet under Innstillinger > Om gir også svar.'),
      ('Trenger jeg en Hisense- eller Google-konto?', 'Nei. Mando TV kobler seg direkte via Wi-Fi-nettverket ditt hjemme og har ingen egen konto.'),
    ]),
  dict(clave='philips', corto='Philips-fjernkontroll', fecha='2026-11-23',
    titulo='Philips fjernkontroll-app: Roku TV, Google TV, Android TV',
    desc='Mando TV styrer Philips-TV-er med Roku TV, Google TV eller Android TV via Wi-Fi, fra mobil eller PC. Titan OS støttes ikke.',
    h1='Styr Philips-TV-en med mobilen',
    intro='Philips-TV-er bruker forskjellige systemer avhengig av land og årsmodell: Roku TV i USA, Google TV eller Android TV i mange land og Titan OS på noen nyere europeiske modeller. Mando TV styrer modellene med Roku TV, Google TV og Android TV via Wi-Fi.',
    pasos=[
      'Sjekk startskjermen. Roku TV viser et rutenett med ruter. Google TV og Android TV viser rader med anbefalinger fra Google. Titan OS har sin egen startskjerm.',
      'Koble mobilen og TV-en til det samme Wi-Fi-nettverket.',
      'Åpne Mando TV og trykk på Philips-TV-en din i listen.',
      'Roku TV spør ikke om noe. Google TV og Android TV viser en kode på 6 tegn: Skriv den inn i appen én gang.',
      'Bruk piltaster, OK, Tilbake, Hjem, volum og tastatur.',
    ],
    extra=[
      ('Philips Roku TV', 'Fungerer som alle Roku-TV-er. For å slå den på fra mobilen slår du på «TV-hurtigstart» under Innstillinger > System > Strøm. Mer på siden [Roku fjernkontroll-app](@roku).'),
      ('Philips med Google TV eller Android TV', 'Omfatter mange Ambilight-modeller. De parer med koden på skjermen. For å slå dem på fra mobilen leter du i nettverks- eller strøminnstillingene etter Wake on LAN eller «Slå på via nettverk». På noen modeller mangler dette alternativet. Mer på siden [Android TV fjernkontroll-app](@android).'),
      ('Eldre Philips-TV-er uten Android', 'Philips-TV-er fra 2011 til 2015 som ikke bruker Android, støttes i Mando TV i beta. Støtten er ny og trenger ingen paringskode.'),
      ('Philips med Titan OS', 'Titan OS er et annet system som Mando TV ikke styrer i dag, og det sier vi heller tydelig. Nyere Philips-modeller uten Android dekkes heller ikke.'),
      ('Gratis og Pro', 'Fjernkontrollen kan du laste ned og bruke gratis, uten reklame og uten abonnement. Mando TV Pro er et valgfritt engangskjøp for ekstrafunksjoner.'),
    ],
    marca=None,
    faq=[
      ('Fungerer Mando TV med Philips-TV-er?', 'Med Philips-TV-er som bruker Roku TV, Google TV eller Android TV, ja, og i beta med Philips-TV-er fra 2011 til 2015 uten Android. Modeller med Titan OS støttes ikke.'),
      ('Styrer Mando TV Ambilight?', 'Mando TV er en fjernkontroll: Den sender knappene, slik at du kommer til Ambilight-innstillingene med pilene og OK. Det finnes ingen separate Ambilight-kontroller.'),
      ('Trenger jeg en Philips- eller Google-konto?', 'Nei. Mando TV kobler seg via Wi-Fi-nettverket ditt hjemme og trenger ingen konto.'),
    ]),
]
OTRAS_GUIAS += [
  ('no-sub', 'En fjernkontroll-app uten abonnement og uten reklame'),
  ('roku-app-alt', 'Alternativ til Roku-appen: én for alle TV-er'),
  ('lg-thinq', 'Alternativ til LG ThinQ-appen for LG-TV-en din'),
  ('smartthings', 'SmartThings-alternativ for Samsung-TV-er'),
  ('googletv-alt', 'Alternativ til Google TV-fjernkontrollen på mobilen'),
  ('windows', 'Fjernkontroll-app for Windows-PC'),
  ('iphone', 'Fjernkontroll-app for iPhone: én for alle TV-er'),
  ('firetv', 'Fire TV-fjernkontroll for mobilen eller PC-en din'),
  ('firetv-lost', 'Mistet Fire TV-fjernkontrollen: Slik bruker du mobilen'),
  ('turn-on', 'Slik slår du på en TV uten fjernkontroll'),
  ('sony', 'Slik styrer du Sony-TV-en med mobilen'),
  ('tcl', 'Slik styrer du TCL-TV-en med mobilen'),
  ('hisense', 'Hisense fjernkontroll-app: hva som fungerer og hva som ikke gjør det'),
  ('philips', 'Styr Philips-TV-en med mobilen'),
]
# <<< guías traídas del inglés
