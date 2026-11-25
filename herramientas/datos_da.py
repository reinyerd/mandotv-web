# Tekster på dansk (du) til mandotv.app. Bruges af generar_idiomas.py. Skrevet til søgninger i Danmark.
# Sidernes nøgler (lg, lost-tv, ...) og deres stier står i idiomas_sitio.py.
# Menunavnene for hvert mærke (LG, Samsung, Roku, Android TV, iPhone) er de samme som appen bruger på dansk
# (lib/l10n/app_da.arb i appens projekt).

UI = dict(
  locale='da_DK',
  aria_home='Mando TV, forside', aria_main='Hovedmenu', nav_que='Funktioner', nav_ayuda='Hjælp', nav_contacto='Kontakt',
  asunto='Hej%20Mando%20TV', inicio='Forside', privacidad='Privatliv', aria_pie='Sidefod', aria_ruta='Brødkrummesti',
  aria_marcas='Mærker og guider', hecho='Udviklet i Chile',
  aviso='Mando TV er en uafhængig app. Den har ingen forbindelse til de nævnte tv-producenter eller til Google, Amazon, Apple eller Roku og er ikke godkendt af dem. Mærkerne tilhører deres ejere og nævnes kun for at vise, hvad appen er kompatibel med. Android TV og Google TV er varemærker tilhørende Google LLC. Apple TV er et varemærke tilhørende Apple Inc.',
  bajar='Hent gratis', descarga='Hent i', anticipada='Tidlig adgang på',
  apple_aria='Hent Mando TV gratis i App Store', ms_aria='Hent Mando TV gratis i Microsoft Store',
  gp_aria='Tidlig adgang til Mando TV på Google Play til Android', aria_desc='Hent Mando TV',
  b_como_btn='Sådan forbinder du', b_tiendas_label='Fås i butikkerne',
  b_nota='iPhone, iPad, Mac, Android og Windows. Gratis download, uden reklamer. Pro er et engangskøb, uden abonnement.',
  b_compat='Kompatible tv', b_otras='Andre mærker', b_otras_p='Mando TV styrer alle disse mærker med den samme app:',
  g_guias='Guides', g_ver='Se trinene', g_pasos='Trin for trin', g_hazlo='Sådan gør du med Mando TV',
  g_tiendas='Mando TV er en universel fjernbetjening til dit tv. Hent den gratis, uden reklamer og uden konto. Pro er et valgfrit engangskøb, uden abonnement. Til iPhone, iPad, Windows og Android:',
  g_nota='Android: gratis tidlig adgang på Google Play. <a href="{enlace}">Vær med i to trin</a> og hjælp os med at komme ud i butikken.',
  g_mas_pagina='Du finder flere detaljer på siden {enlace}.', g_mas_marca='Flere detaljer pr. mærke:',
  g_faq='Ofte stillede spørgsmål', g_mas='Flere guider', g_todas='Alle guider', g_ayuda='Hjælp og support',
  g_idiomas='Denne guide på andre sprog',
)

# Sidefod og lister over mærker/guider: (nøgle, tekst)
PIE = [
  ('samsung', 'Samsung fjernbetjening'),
  ('lg', 'LG fjernbetjening'),
  ('roku', 'Roku fjernbetjening'),
  ('android', 'Android TV fjernbetjening'),
  ('guias', 'Alle guider'),
  ('lost-tv', 'Fjernbetjening væk'),
  ('lost-lg', 'LG fjernbetjening væk'),
  ('lg-on', 'Tænd LG-tv med mobilen'),
  ('hdmi', 'Skift HDMI-indgang uden fjernbetjening'),
  ('androidtv', 'Android TV uden fjernbetjening'),
  ('console', 'Tænd tv og konsollens HDMI uden fjernbetjening'),
  ('samsung-lost', 'Samsung-tv uden fjernbetjening'),
  ('roku-lost', 'Roku fjernbetjening væk'),
  ('roku-403', 'Roku-appen virker ikke'),
  ('androidtv-code', 'Android TV parringskode'),
  ('not-found', 'Mobilen finder ikke tv\'et'),
  ('wifi', 'Mobilen som fjernbetjening via wifi'),
  ('pc', 'Styr tv\'et fra pc\'en'),
]
NOMBRE_OTRA = {'lg': 'LG fjernbetjening-app', 'samsung': 'Samsung fjernbetjening-app', 'roku': 'Roku fjernbetjening-app',
               'android': 'Android TV og Google TV fjernbetjening-app'}
PAGINA_MARCA = {'lg': 'LG fjernbetjening-app', 'samsung': 'Samsung fjernbetjening-app', 'roku': 'Roku fjernbetjening-app',
                'android': 'Android TV fjernbetjening-app'}

OTRAS_GUIAS = [
  ('lg-on', 'Tænd LG-tv med mobilen'),
  ('lost-tv', 'Fjernbetjening væk: Det kan du gøre'),
  ('lost-lg', 'LG fjernbetjening væk: Sådan bruger du mobilen'),
  ('hdmi', 'Skift HDMI-indgang på tv\'et uden fjernbetjening'),
  ('androidtv', 'Android TV uden fjernbetjening: Sådan bruger du mobilen'),
  ('console', 'Tænd tv\'et og skift til konsollens HDMI uden fjernbetjening'),
  ('samsung-lost', 'Samsung-tv uden original fjernbetjening: Sådan bruger du mobilen'),
  ('roku-lost', 'Roku fjernbetjening væk: Sådan bruger du mobilen'),
  ('roku-403', 'Roku-appen virker ikke: Ret fejl 403'),
  ('androidtv-code', 'Android TV beder om en parringskode: Det skal du gøre'),
  ('not-found', 'Din mobil finder ikke tv\'et: Det skal du tjekke'),
  ('wifi', 'Sådan bruger du mobilen som fjernbetjening via wifi'),
  ('pc', 'Sådan styrer du dit tv med en Windows-pc'),
]

INDICE = dict(
  titulo='Guider: Styr tv\'et med mobilen | Mando TV',
  desc='Guider trin for trin: brug mobil eller pc som fjernbetjening, tænd tv\'et, skift HDMI og løs problemer med Samsung, LG og Roku.',
  h1='Guider: Brug mobilen som fjernbetjening',
  intro='Enkle trin til at forbinde fjernbetjeningen til dit Samsung-, LG-, Roku- eller Android TV-tv med Mando TV, tænde tv\'et og løse problemer.',
  h2_guias='Alle guider', h2_marcas='Fjernbetjening-app pr. mærke',
)

MARCAS = [
  dict(clave='lg', color='#e0457b', corto='LG',
    titulo='LG tv fjernbetjening-app til mobilen, gratis | Mando TV',
    desc='Din mobil eller pc som LG tv fjernbetjening til webOS, via wifi. Knapper, tastatur, apps, indgange og tænd gratis; markør med Pro.',
    h1='LG tv fjernbetjening som app til mobilen',
    intro='Mando TV er en fjernbetjening-app til LG-tv: Den gør din mobil eller computer til fjernbetjening til dit LG smart-tv med webOS via wifi derhjemme. Det hjælper, når du har mistet fjernbetjeningen, batterierne er tomme, eller du bare vil taste hurtigere.',
    compat='LG smart-tv med webOS (de fleste LG smart-tv-modeller siden 2014). Virker med LED-, NanoCell-, QNED- og OLED-tv. Ældre LG smart-tv med NetCast (2011 til 2014, før webOS) understøttes nu i beta: De parres med den 6-cifrede nøgle, som tv\'et viser.',
    h2=dict(funciones='Det kan du gøre med dit LG-tv', como='Sådan forbinder du dit LG-tv med Mando TV',
            encender='Tænd LG-tv med mobilen', preguntas='Spørgsmål om LG', guias='Guider til LG'),
    funciones=[
      ('Alle knapper', 'Piletaster, OK, Tilbage, Hjem, lydstyrke, kanaler, lydløs og afspilning.'),
      ('Markør som på Magic Remote (Pro)', 'Flyt pilen rundt på skærmen med fingeren, ligesom med LG Magic Remote.'),
      ('Tastatur', 'Skriv i YouTube, Netflix eller tv\'ets browser med din mobils tastatur.'),
      ('Apps og indgange', 'Åbn dine apps og skift til HDMI, live-tv, AirPlay eller Screen Share.'),
      ('Lydudgang (Pro)', 'Skift mellem tv\'ets højttalere og din soundbar.'),
      ('Tænd tv\'et', 'Hvis det er slukket, tænder Mando TV det via netværket og forbinder af sig selv.'),
    ],
    pasos=[
      'Forbind mobil og tv til det samme wifi.',
      'Åbn Mando TV: Dit LG-tv dukker op på listen af sig selv. Tryk på det.',
      'På tv\'et kommer der en forespørgsel om tilladelse. Bekræft den med din almindelige fjernbetjening (kun første gang).',
    ],
    encender='Åbn indstillingerne på LG-tv\'et og find "Tænd tv med mobil" (afhængigt af modellen under Generelt eller Forbindelse). Aktivér "Tænd via wifi". Hvis der findes "Hurtig start+", så aktivér den også. Bagefter spørger appen dig, når du trykker på det slukkede tv i Mando TV, om den skal tænde det, og forbinder af sig selv.',
    faq=[
      ('Skal jeg bruge Magic Remote for at bruge Mando TV?', 'Kun første gang, for at bekræfte forespørgslen på skærmen. Bagefter er din mobil nok.'),
      ('Erstatter Mando TV appen LG ThinQ?', 'Til at styre tv\'et, ja: Du skal hverken have en LG-konto eller registrere tv\'et. Mando TV forbinder direkte via dit wifi.'),
      ('Kan jeg tænde mit LG-tv med mobilen?', 'Ja, hvis du har aktiveret "Tænd tv med mobil" på tv\'et og har forbundet én gang, mens tv\'et var tændt.'),
      ('Virker det med ældre LG-tv fra før webOS?', 'I beta, ja, med LG NetCast smart-tv fra 2011 til 2014. De parres med den 6-cifrede nøgle, som tv\'et viser. Funktionen er ny og kan stadig have skæve kanter.'),
    ],
    guias=[('lg-on', 'Sådan tænder du et LG-tv med mobilen'),
           ('lost-lg', 'LG fjernbetjening væk: Sådan bruger du mobilen'),
           ('hdmi', 'Skift HDMI-indgang på tv\'et uden fjernbetjening'),
           ('guias', 'Alle guider til at styre tv\'et med mobilen')]),
  dict(clave='samsung', color='#3d7bff', corto='Samsung',
    titulo='Samsung tv fjernbetjening-app til mobilen | Mando TV',
    desc='Din mobil eller pc som Samsung tv fjernbetjening til Tizen, via wifi. Knapper, tastatur, apps og tænd gratis; touchpad med Pro. Uden reklamer.',
    h1='Samsung tv fjernbetjening som app til mobilen',
    intro='Mando TV er en fjernbetjening-app til Samsung-tv: Den gør din mobil eller computer til fjernbetjening til dit Samsung smart-tv via wifi derhjemme. Du skal hverken have en Samsung-konto eller registrere tv\'et.',
    compat='Samsung smart-tv med Tizen, årgang 2016 og nyere (serier som Crystal UHD, QLED, Neo QLED, The Frame og OLED).',
    h2=dict(funciones='Det kan du gøre med dit Samsung-tv', como='Sådan forbinder du dit Samsung-tv med Mando TV',
            encender='Tænd Samsung-tv med mobilen', preguntas='Spørgsmål om Samsung', guias='Guider til Samsung'),
    funciones=[
      ('Alle knapper', 'Piletaster, OK, Tilbage, Hjem, lydstyrke, kanaler, lydløs og kilde.'),
      ('Touchpad (Pro)', 'Stryg med fingeren gennem menuerne uden at lede efter piletasterne.'),
      ('Tastatur', 'Skriv søgeord og adgangskoder med din mobils tastatur.'),
      ('Apps', 'Åbn Netflix, YouTube, Prime Video og dine andre apps med et tryk.'),
      ('Tænd tv\'et', 'Hvis det er slukket, tænder Mando TV det via netværket og forbinder af sig selv.'),
      ('Uden konto', 'Forbindelsen kører direkte via dit wifi, uden omvej over internettet.'),
    ],
    pasos=[
      'Forbind mobil og tv til det samme wifi.',
      'Åbn Mando TV: Dit Samsung-tv dukker op på listen af sig selv. Tryk på det.',
      'Tv\'et spørger, om du tillader forbindelsen. Vælg "Tillad" med fjernbetjeningen (kun første gang).',
    ],
    encender='Aktivér på Samsung-tv\'et under Indstillinger > Generelt > Netværk > Ekspertindstillinger muligheden "Tænd med mobil". Bagefter spørger appen dig, når du trykker på det slukkede tv i Mando TV, om den skal tænde det, og forbinder af sig selv.',
    faq=[
      ('Jeg kom til at afvise tilladelsen. Hvad gør jeg?', 'Gå på tv\'et til Indstillinger > Generelt > Administrator af eksterne enheder > Enhedsforbindelsesadministrator og sæt Mando TV til tilladt.'),
      ('Erstatter Mando TV SmartThings?', 'Til at styre tv\'et, ja, og det uden Samsung-konto. Mando TV forbinder direkte via dit wifi.'),
      ('Virker det med ældre Samsung-tv?', 'Det virker med Samsung-tv med Tizen, årgang 2016 og nyere. Tidligere modeller bruger et andet system, som vi endnu ikke understøtter.'),
    ],
    guias=[('samsung-lost', 'Samsung-tv uden original fjernbetjening: Sådan bruger du mobilen'),
           ('hdmi', 'Skift HDMI-indgang på tv\'et uden fjernbetjening'),
           ('guias', 'Alle guider til at styre tv\'et med mobilen')]),
  dict(clave='roku', color='#a77bff', corto='Roku',
    titulo='Roku fjernbetjening-app til mobilen, gratis | Mando TV',
    desc='Din mobil eller pc som Roku fjernbetjening til Roku TV og Roku-afspillere, via wifi. Knapper, tastatur, kanaler, indgange og tænd gratis.',
    h1='Roku fjernbetjening som app til mobilen',
    intro='Mando TV er en fjernbetjening-app til Roku: Den gør din mobil eller computer til fjernbetjening til din Roku via wifi derhjemme. Den virker med Roku TV og med Roku-afspillere, der sættes i HDMI-stikket.',
    compat='Roku TV (TCL, Hisense, Philips, Sharp, JVC og andre) og Roku-afspillere (Express, Streaming Stick, Ultra).',
    h2=dict(funciones='Det kan du gøre med din Roku', como='Sådan forbinder du din Roku med Mando TV',
            encender='Tænd Roku med mobilen', preguntas='Spørgsmål om Roku', guias='Guider til Roku'),
    funciones=[
      ('Alle knapper', 'Piletaster, OK, Tilbage, Hjem, lydstyrke, lydløs, gentag og afspilning.'),
      ('Tastatur', 'Skriv søgeord i Roku-kanaler med din mobils tastatur.'),
      ('Kanaler', 'Åbn Netflix, YouTube og dine andre Roku-kanaler med et tryk.'),
      ('Indgange', 'Skift på et Roku TV til HDMI, antenne eller AV i appen.'),
      ('Tænd tv\'et', 'På Roku TV med hurtig start tænder Mando TV dem fra din mobil.'),
      ('Uden parring', 'Roku spørger ikke efter en kode: Tryk på den på listen, og du er forbundet.'),
      ('Find min fjernbetjening', 'Har din Roku-fjernbetjening en højttaler, f.eks. Roku Voice Remote Pro, får Mando TV den til at ringe, så du kan finde den. Gratis, og Roku skal være tændt.'),
    ],
    pasos=[
      'Forbind mobil og Roku til det samme wifi.',
      'Åbn Mando TV: Din Roku dukker op på listen af sig selv. Tryk på den.',
      'Hvis forbindelsen ikke lykkes, så gå på Roku til Indstillinger > System > Avancerede systemindstillinger > Styring via mobilapps og sæt netværksadgangen til Standard eller Aktiveret.',
    ],
    encender='Aktivér på Roku TV under Indstillinger > System > Strøm muligheden "Hurtig start for tv". Roku-afspillere, der er sluttet til et andet tv, kan ikke tændes på den måde. Bagefter spørger appen dig, når du trykker på det slukkede tv i Mando TV, om den skal tænde det, og forbinder af sig selv.',
    faq=[
      ('Virker det med Roku Express eller Streaming Stick?', 'Ja. Alle Roku-afspillere og Roku TV styres på samme måde.'),
      ('Mando TV finder ikke min Roku. Hvad gør jeg?', 'Tjek, at begge er på det samme wifi, og at "Styring via mobilapps" ikke er slået fra på Roku. Du kan også tilføje den via dens IP-adresse.'),
      ('Skal jeg have en Roku-konto?', 'Nej. Mando TV forbinder direkte via dit wifi.'),
    ],
    guias=[('roku-403', 'Roku-appen virker ikke (fejl 403)'),
           ('roku-lost', 'Roku fjernbetjening væk: Sådan bruger du mobilen'),
           ('guias', 'Alle guider til at styre tv\'et med mobilen')]),
  dict(clave='android', color='#2fbf8f', corto='Android TV og Google TV',
    titulo='Android TV fjernbetjening-app til mobilen | Mando TV',
    desc='Din mobil eller pc som Android TV fjernbetjening (Sony, TCL, Xiaomi), via wifi. Knapper, tastatur, apps og tænd gratis; touchpad med Pro.',
    h1='Android TV fjernbetjening som app til mobilen',
    intro='Mando TV er en fjernbetjening-app til Android TV: Den gør din mobil eller computer til fjernbetjening til dit Android TV- eller Google TV-tv via wifi derhjemme. Den virker også fra iPhone og fra Windows.',
    compat='Tv med Google TV eller Android TV fra Sony, Philips, TCL, Hisense, Sharp, Xiaomi, Toshiba, Panasonic, Haier, Skyworth, JVC, Thomson, Motorola, OnePlus, iFFALCON, Kogan, Vu og andre mærker, dertil Chromecast med Google TV, Google TV Streamer, onn. og Nvidia Shield. Nogle af disse mærker sælger også modeller med et andet system: Viser dit tv startskærmen fra Google TV, eller har det Google Play Butik, styrer Mando TV det.',
    h2=dict(funciones='Det kan du gøre med dit Android TV', como='Sådan forbinder du dit Android TV med Mando TV',
            encender='Tænd Android TV med mobilen', preguntas='Spørgsmål om Android TV', guias='Guider til Android TV'),
    funciones=[
      ('Alle knapper', 'Piletaster, OK, Tilbage, Hjem, lydstyrke, lydløs og afspilning.'),
      ('Touchpad (Pro)', 'Stryg med fingeren for hurtigt at navigere gennem menuerne i Google TV.'),
      ('Tastatur', 'Skriv søgeord og adgangskoder med din mobils tastatur.'),
      ('Apps', 'Åbn YouTube, Netflix, Disney+ og dine andre apps med et tryk.'),
      ('Tænd tv\'et', 'På modeller med tænd via netværket tænder Mando TV tv\'et og forbinder af sig selv.'),
      ('iPhone, Android og pc', 'Det virker ens på alle mobiler og alle computere.'),
    ],
    pasos=[
      'Forbind mobil og tv til det samme wifi.',
      'Åbn Mando TV: Dit Android TV dukker op på listen af sig selv. Tryk på det.',
      'Tv\'et viser en kode med 6 tegn. Indtast den i Mando TV (kun første gang).',
    ],
    encender='Det afhænger af producenten. Led i netværks- eller strømindstillingerne efter "Wake on LAN", "Tænd via netværk" eller "Netværksstandby". Nogle modeller har ikke denne mulighed. Bagefter spørger appen dig, når du trykker på det slukkede tv i Mando TV, om den skal tænde det, og forbinder af sig selv.',
    faq=[
      ('Virker det med Chromecast med Google TV?', 'Ja, parringen sker med koden på 6 tegn, som vises på skærmen.'),
      ('Hvad er forskellen på Google TV-appen?', 'Mando TV kræver ingen Google-konto, virker også på Windows og styrer tv fra LG, Samsung og Roku med den samme app.'),
      ('Koden vises ikke på skærmen. Hvad gør jeg?', 'Luk Mando TV, åbn appen igen, og tryk endnu en gang på tv\'et. Tjek, at tv\'et ikke er i en dyb strømsparetilstand.'),
    ],
    guias=[('androidtv-code', 'Android TV beder om en parringskode: Det skal du gøre'),
           ('androidtv', 'Android TV uden fjernbetjening: Sådan bruger du mobilen'),
           ('guias', 'Alle guider til at styre tv\'et med mobilen')]),
]

GUIAS = [
  dict(clave='lost-tv', corto='Fjernbetjening væk',
    titulo='Fjernbetjeningen væk? Styr tv\'et med mobilen',
    desc='Fjernbetjeningen væk? Tænd tv\'et på selve apparatet og brug mobilen som fjernbetjening. Trin til LG, Samsung, Roku og Android TV. Gratis.',
    h1='Fjernbetjeningen væk? Det kan du gøre nu',
    intro='En fjernbetjening, der er væk, sker i alle hjem: Den er væk lige dér, hvor du vil se noget. Den gode nyhed: Din mobil kan overtage som fjernbetjening via wifi derhjemme. Her kan du se, hvad du kan gøre i rækkefølge.',
    pasos=[
      'Tænd tv\'et med knappen på selve apparatet. Den sidder næsten altid nederst på midten eller bagpå nær et hjørne. Nogle gange er det en enkelt knap, andre gange en lille joystick.',
      'Forbind din mobil til det samme wifi som tv\'et.',
      'Hent Mando TV, som er gratis og ikke kræver en konto, og åbn appen. Dit tv dukker op på listen af sig selv. Tryk på det.',
      'Bekræft forbindelsen for dit mærke. På LG og Samsung viser tv\'et en forespørgsel: Bekræft den med knappen eller joysticken på selve tv\'et. På Android TV og Google TV indtaster du en kode med 6 tegn, som vises på skærmen. Roku spørger ikke om noget.',
      'Så er du klar. Piletaster, OK, Tilbage, Hjem, lydstyrke, kanaler og tastatur er gratis.',
      'Til næste gang: Aktivér i tv\'ets indstillinger, at det kan tændes via netværket (guiden til dit mærke finder du nedenfor). Så kan du tænde tv\'et fra mobilen uden at røre det.',
    ],
    extra=[
      ('Vælg guiden til dit mærke', 'LG: [LG fjernbetjening væk](@lost-lg). Android TV og Google TV: [Android TV uden fjernbetjening](@androidtv). Samsung: [Samsung-tv uden fjernbetjening](@samsung-lost). Roku: [Roku fjernbetjening væk](@roku-lost).'),
      ('Hvis tv\'et ikke vil tænde med knappen', 'Før du leder efter en anden fjernbetjening, så tjek, at kablet sidder fast, og at stikkontakten har strøm. Gør knappen på tv\'et ingenting, ligger problemet i tv\'et og ikke i fjernbetjeningen.'),
      ('Hvis fjernbetjeningen bare ikke virker mere', 'Prøv nye batterier. Om den stadig sender et signal, kan du tjekke ved at pege den mod mobilkameraet og trykke på en knap: På mange mobiler ser du så et violet lys på skærmen. Ser du lyset, og tv\'et ikke reagerer, er sensoren på tv\'et måske dækket til.'),
      ('Hvis du har skiftet router, og tv\'et ikke har wifi mere', 'Uden fjernbetjening er det sværere at få tv\'et på det nye netværk. Det nemmeste er at sætte tv\'et i routeren med et netværkskabel. Du kan også oprette et wifi med samme navn og adgangskode som før: Tv\'et forbinder som regel af sig selv til det.'),
      ('Hvad er gratis, og hvad er Pro', 'At tænde og slukke tv\'et, piletaster, OK, lydstyrke, kanaler, taltaster, tastatur, at åbne apps og at skifte indgang er gratis. Touchpad, tale og rutiner hører til Mando TV Pro, et engangskøb uden abonnement.'),
    ],
    marca=None,
    faq=[
      ('Kan jeg tænde tv\'et med mobilen, hvis jeg aldrig har forbundet det?', 'Første gang tænder du det med knappen på tv\'et. Når du har forbundet din mobil og aktiveret i tv\'ets indstillinger, at det kan tændes via netværket, kan du tænde det fra appen.'),
      ('Skal jeg købe en ny fjernbetjening?', 'Ikke nødvendigvis. Med Mando TV får du knapper, lydstyrke, tastatur og tænd gratis. Vil du alligevel hellere have en rigtig fjernbetjening, så søg efter den præcise model af dit tv.'),
      ('Virker det, hvis tv\'et ikke har wifi?', 'Nej. Mobil og tv skal være på det samme wifi. Et tv, der ikke er et smart-tv, kan ikke styres med Mando TV.'),
    ]),
  dict(clave='lost-lg', corto='LG fjernbetjening væk',
    titulo='LG fjernbetjening væk? Brug din mobil',
    desc='Ingen LG fjernbetjening? Tænd tv\'et på selve apparatet, bekræft forespørgslen og brug mobilen via wifi. Uden LG-konto, uden reklamer.',
    h1='LG fjernbetjening væk? Sådan bruger du mobilen',
    intro='Hvis du har mistet din LG fjernbetjening, eller Magic Remote ikke virker mere, overtager din mobil via wifi. Det virker med LG-tv med webOS, altså næsten alle LG smart-tv siden 2014. Du skal hverken have en LG-konto eller appen ThinQ.',
    pasos=[
      'Tænd tv\'et med knappen nederst under LG-logoet eller med knappen bagpå. På mange modeller er den en joystick: Tryk på den for at åbne menuen, og bevæg den for at vælge noget.',
      'Forbind din mobil til det samme wifi som tv\'et.',
      'Åbn Mando TV og tryk på dit LG-tv på listen.',
      'Tv\'et viser en forespørgsel om tilladelse. Bekræft den med joysticken eller knappen på tv\'et. Har du forbundet denne mobil før, spørger det ikke igen.',
      'Så er du klar. Piletaster, OK, Tilbage, Hjem, lydstyrke, kanaler og tastatur er gratis. Markøren er en Pro-funktion.',
      'Når appen er forbundet, så åbn indstillingerne med piletasterne og OK og aktivér "Tænd tv med mobil". Guiden [Tænd LG-tv med mobilen](@lg-on) viser, hvor du finder muligheden.',
    ],
    extra=[
      ('Hvis tv\'et ikke viser forespørgslen', 'Måske er tilladelsen allerede gemt, eller din mobil er på et andet netværk. Tjek, at begge er på det samme wifi, og at VPN er slået fra. Dukker tv\'et ikke op på listen, hjælper [Din mobil finder ikke tv\'et](@not-found) dig videre.'),
      ('Hvis tv\'et har mistet sit wifi', 'Sæt tv\'et i routeren med et netværkskabel, så bruger det det af sig selv. Eller opret et wifi med samme navn og adgangskode som før, for tv\'et forbinder som regel af sig selv til det.'),
      ('Hvis tv\'et hænger på en anden indgang', 'Tryk på din mobil på Indgange og vælg HDMI-stikket. Du kan læse mere i [Skift HDMI-indgang på tv\'et uden fjernbetjening](@hdmi).'),
    ],
    marca='lg',
    faq=[
      ('Skal jeg bruge Magic Remote for at bruge Mando TV?', 'Du skal kun bruge noget første gang for at bekræfte forespørgslen, og der er knappen eller joysticken på selve tv\'et nok. Bagefter bruger du kun din mobil.'),
      ('Skal jeg have appen LG ThinQ?', 'Nej. Mando TV forbinder direkte via dit wifi og kræver ingen LG-konto.'),
      ('Kan jeg slukke og tænde mit LG-tv med mobilen?', 'Slukke, ja. For at tænde skal du have aktiveret "Tænd tv med mobil" på tv\'et og have forbundet én gang, mens tv\'et var tændt.'),
    ]),
  dict(clave='hdmi', corto='Skift HDMI uden fjernbetjening',
    titulo='Skift HDMI-indgang uden fjernbetjening (Samsung, LG, Roku)',
    desc='Skift HDMI-indgang uden fjernbetjening på Samsung, LG eller Roku: med knappen på tv\'et eller med mobilen. Gratis at starte med, uden reklamer.',
    h1='Sådan skifter du HDMI-indgang på tv\'et uden fjernbetjening',
    intro='Konsollen eller streaming-afspilleren er klar, men tv\'et hænger på en anden indgang, og fjernbetjeningen er ingen steder at finde. For at skifte HDMI-indgang uden fjernbetjening har du to muligheder: knappen på selve tv\'et eller din mobil. Her er trinene til Samsung, LG og Roku.',
    pasos=[
      'Prøv først det enkleste: Tænd konsollen eller afspilleren. Er HDMI-CEC aktiveret på tv\'et (hos Samsung hedder det Anynet+, hos LG SIMPLINK), skifter det af sig selv til den indgang.',
      'Skifter det ikke, så brug knappen på selve tv\'et, nederst på midten eller bagpå. På mange Samsung- og LG-tv er den en joystick og åbner en menu med Kilde eller Indgange.',
      'Vælg indgangen i den menu: HDMI 1, HDMI 2 og så videre. Nummeret er det stik, kablet sidder i.',
      'Vil du hellere bruge mobilen, så forbind den til det samme wifi, åbn Mando TV og tryk på dit tv.',
      'På LG og Roku trykker du på Indgange og vælger HDMI-stikket. På Samsung sender Indgange Kilde-knappen til tv\'et, og du vælger med piletasterne og OK.',
      'Du kan også gå til indgangene med piletasterne og OK på tv\'ets startskærm. Afhængigt af mærke og årgang hedder de Kilde, Tilsluttede enheder eller Indgange. På et Roku TV er det HDMI-felterne på startskærmen.',
    ],
    extra=[
      ('Samsung', 'Har menuen fra knappen på tv\'et ikke punktet Kilde, så åbn startskærmens menu med din mobil og led til venstre efter Kilde eller Tilsluttede enheder. Du styrer den med piletasterne og OK i Mando TV, som er gratis.'),
      ('LG', 'Tryk på joysticken på tv\'et og led efter Indgange. Med din mobil kan du i Mando TV også åbne listen over indgange og trykke på den indgang, du vil have.'),
      ('Roku TV', 'På startskærmen er der et felt for hver indgang, for eksempel HDMI 1 eller HDMI 2. Bevæg dig med piletasterne og åbn dem med OK, gratis.'),
      ('Hvis det er et tv med Android TV eller Google TV', 'I Mando TV findes listen over indgange til Android TV endnu ikke. Brug indgangsknappen på selve tv\'et, eller nå indgangene med piletasterne og OK fra startskærmen. Har du ingen fjernbetjening og vil forbinde, så læs [Android TV uden fjernbetjening](@androidtv).'),
      ('Mere hjælp', 'Tænder tv\'et slet ikke, eller ved du ikke, hvor du skal begynde, så læs [Fjernbetjening væk](@lost-tv). Til spil på konsollen indeholder guiden [Tænd tv\'et og skift til konsollens HDMI uden fjernbetjening](@console) HDMI-CEC-tricket.'),
    ],
    marca=None,
    faq=[
      ('Er det gratis at skifte HDMI-indgang?', 'Ja. Listen over indgange i Mando TV er gratis, ligesom at tænde tv\'et og piletaster, OK og lydstyrke. Indgangene kan du også nå via tv\'ets menu.'),
      ('Hvordan ved jeg, hvilken HDMI-indgang jeg skal bruge?', 'Se på HDMI-stikkene på tv\'et: Hvert har et nummer. Tag det, hvor kablet fra din konsol eller afspiller sidder.'),
      ('Hvad hvis tv\'et ikke tænder?', 'Tænd det med knappen på selve apparatet. Har du forbundet det én gang og aktiveret tænd via netværket, kan du også tænde det fra din mobil.'),
    ]),
  dict(clave='androidtv', corto='Android TV uden fjernbetjening',
    titulo='Android TV uden fjernbetjening: Brug din mobil',
    desc='Ingen Android TV- eller Google TV-fjernbetjening? Forbind din mobil med den 6-tegns kode på skærmen. Gratis, uden konto, uden reklamer.',
    h1='Android TV uden fjernbetjening: Sådan bruger du mobilen',
    intro='Hvis du har mistet fjernbetjeningen til dit Android TV eller Google TV, eller batterierne er flade, overtager din mobil. Det bedste: Til forbindelsen skal du ikke bruge fjernbetjeningen, for tv\'et viser en kode på skærmen, og du taster den ind på mobilen. Det virker på tv fra Sony, Philips, TCL, Hisense, Sharp og Xiaomi med Android TV, på Chromecast med Google TV og på Nvidia Shield.',
    pasos=[
      'Tænd tv\'et med knappen på selve apparatet. Den sidder næsten altid nederst på midten eller bagpå nær et hjørne.',
      'Forbind din mobil til det samme wifi som tv\'et.',
      'Hent Mando TV, som er gratis og ikke kræver en Google-konto, og åbn appen. Tryk på dit tv på listen.',
      'Tv\'et viser en kode på 6 bogstaver og tal. Tast den ind på din mobil og tryk på Par. Til det skal du ikke bruge fjernbetjeningen.',
      'Nu kan du bruge piletaster, OK, Tilbage, Hjem, lydstyrke, lydløs og tastatur. De er gratis, ligesom listen over apps. Touchpad er Pro.',
      'For at tænde tv\'et fra mobilen næste gang så led i netværks- eller strømindstillingerne efter "Wake on LAN", "Tænd via netværk" eller "Netværksstandby".',
    ],
    extra=[
      ('Hvis dit tv ikke kan tændes fra mobilen', 'Ikke alle Android TV kan tændes via netværket; det afhænger af producent og model. Har dit ikke funktionen, så tænd det med knappen på tv\'et og fortsæt på mobilen. Slukke kan du det fra appen.'),
      ('Chromecast med Google TV, Google TV Streamer og Shield', 'De forbinder på samme måde: samme wifi, tryk på enheden på listen og indtast koden. Viser tv\'et en anden indgang, så skift den til det HDMI-stik, enheden sidder i, som forklaret i [Skift HDMI-indgang på tv\'et uden fjernbetjening](@hdmi).'),
      ('Hvis koden ikke vises eller meldes forkert', 'Tjek, at tv\'et virkelig er tændt og ikke i standby. Koden ændrer sig ved hver forespørgsel: Kun den sidste virker. Flere detaljer finder du i [Android TV beder om en parringskode](@androidtv-code).'),
      ('Google-appen eller Mando TV', 'Google har sin egen app, som kræver en Google-konto. Mando TV kræver ingen konto, virker også på Windows og styrer tv fra LG, Samsung og Roku med den samme app.'),
    ],
    marca='android',
    faq=[
      ('Skal jeg bruge fjernbetjeningen for at parre min mobil?', 'Nej. Koden vises på tv\'ets skærm, og du taster den ind på mobilen. Du skal bare tænde tv\'et, om nødvendigt med knappen på apparatet.'),
      ('Virker det med et Hisense?', 'På Hisense-tv med Android TV eller Google TV, ja. Hisense-tv med et andet system er ikke kompatible.'),
      ('Kan jeg skrive med min mobils tastatur?', 'Ja. Tastaturet er gratis og virker til søgning i YouTube, Netflix og de andre apps.'),
    ]),
  dict(clave='lg-on', corto='Tænd LG-tv med mobilen',
    titulo='Tænd LG-tv med mobilen (vejledning)',
    desc='Tænd LG-tv med mobilen via wifi: Aktivér "Tænd tv med mobil" og brug Mando TV. Trin for trin, gratis.',
    h1='Sådan tænder du et LG-tv med mobilen',
    intro='Du kan tænde et LG-tv med mobilen, men du skal først aktivere en indstilling på tv\'et. Bagefter tænder din mobil LG-tv\'et via dit wifi, helt uden fjernbetjening. Det tager fem minutter, og du gør det kun én gang.',
    pasos=[
      'Forbind din mobil og LG-tv\'et til det samme wifi.',
      'Åbn indstillingerne på tv\'et og find "Tænd tv med mobil". Afhængigt af modellen finder du det under Generelt eller Forbindelse.',
      'Aktivér "Tænd via wifi". Er dit tv forbundet med netværkskabel, så aktivér i stedet muligheden for kablet.',
      'Har dit tv "Hurtig start+", så aktivér den også.',
      'Åbn Mando TV på din mobil, mens tv\'et er tændt, og tryk på dit LG-tv på listen. Bekræft forespørgslen, der vises på skærmen. Sådan lærer appen at vække det.',
      'Sluk tv\'et og prøv: Tryk på tv\'et i Mando TV, og appen spørger, om den skal tænde det.',
    ],
    extra=[
      ('Hvis det ikke tænder', 'Tv\'et skal have været på det samme wifi, da det blev slukket. Tjek, at indstillingen stadig er aktiv, og at din mobil er på det samme netværk. Har du skiftet router, så forbind igen, mens tv\'et er tændt.'),
    ],
    marca='lg',
    faq=[
      ('Kan jeg tænde LG-tv\'et med mobilen, hvis jeg aldrig har forbundet det?', 'Nej. Først skal du aktivere "Tænd tv med mobil" på tv\'et og forbinde én gang med Mando TV, mens tv\'et er tændt.'),
      ('Skal jeg have appen LG ThinQ?', 'Nej. Mando TV forbinder direkte via dit wifi og kræver ingen LG-konto.'),
      ('Virker det med mobildata?', 'Nej. Mobil og tv skal være på det samme wifi.'),
    ]),
  dict(clave='console', corto='Tv og konsol uden fjernbetjening',
    titulo='Ingen fjernbetjening? Tænd tv\'et, skift HDMI',
    desc='Udgivelsesdag og ingen fjernbetjening? Tænd tv\'et og skift med mobilen til HDMI-indgangen til din PS5 eller Xbox. Gratis, uden reklamer.',
    h1='Sådan tænder du tv\'et og skifter til konsollens HDMI-indgang uden fjernbetjening',
    intro='Udgivelsesdag for GTA VI, konsollen er klar, og fjernbetjeningen er forsvundet et sted mellem sofapuderne. Det sker oftere, end man tror. Med Mando TV tænder din mobil tv\'et og skifter via dit wifi derhjemme til indgangen til din PlayStation eller Xbox.',
    pasos=[
      'Forbind din mobil til det samme wifi som tv\'et.',
      'Åbn Mando TV og tryk på dit tv på listen (Samsung, LG, Roku eller Android TV).',
      'Er tv\'et slukket, så tryk på Tænd. Det virker, når tænd via netværket er aktiveret på tv\'et. Har du aldrig aktiveret det, så tænd tv\'et denne ene gang med knappen på apparatet og aktivér det til næste gang.',
      'Tænd konsollen. Er HDMI-CEC aktiveret (se det gratis trick længere nede), skifter tv\'et af sig selv til dens indgang.',
      'Skifter det ikke, så tryk i Mando TV på Indgange og vælg det HDMI-stik, konsollen sidder i: HDMI 1, HDMI 2 og så videre.',
      'Til lydstyrken bruger du under spillet de store knapper i appen.',
    ],
    extra=[
      ('Det gratis trick: Lad konsollen skifte tv\'et', 'PS5 og Xbox kan tænde tv\'et og springe til deres HDMI-indgang lige ved start takket være HDMI-CEC. På PS5 finder du det under Indstillinger > System > HDMI > Aktivér HDMI-enhedslink. På Xbox åbner du Indstillinger > Generelt > Tv- og skærmindstillinger og leder efter muligheden for enhedsstyring. På tv\'et hedder funktionen noget forskelligt alt efter mærke: Anynet+ hos Samsung, SIMPLINK hos LG og BRAVIA Sync eller HDMI-styring hos andre.'),
      ('Hvis tv\'et bliver på et andet billede', 'Er konsollen tændt, men tv\'et viser stadig antenne eller en app, har det ikke skiftet indgang. Tryk på din mobil på Indgange og vælg konsollens HDMI-indgang. Eller brug piletasterne og OK til at nå tv\'ets indgange, eller knappen på selve tv\'et, og vælg HDMI-stikket. Nummeret er det stik, du satte konsollens kabel i.'),
      ('Hvis det er et Roku TV', 'Knappen på tv\'et, som oftest sidder nederst på midten eller bagpå, tænder det. Derfra klarer din mobil resten.'),
    ],
    marca=None,
    faq=[
      ('Har Mando TV noget med GTA VI at gøre?', 'Nej. Mando TV har ingen forbindelse til Rockstar Games eller Take-Two. Appen hjælper dig bare med ikke at miste spilletid, fordi du ikke kan finde fjernbetjeningen.'),
      ('Er det gratis at skifte HDMI-indgang?', 'Ja. Listen over indgange i Mando TV er gratis, ligesom at tænde tv\'et og piletaster, OK og lydstyrke. Du kan også lade konsollen skifte indgang af sig selv med HDMI-CEC.'),
      ('Virker det med mit tv?', 'Det virker med tv fra Samsung, LG, Roku og Android TV på det samme wifi. Er dit af et andet mærke, kan HDMI-CEC-tricket stadig hjælpe dig.'),
      ('Kan jeg bruge det til at spille GTA VI (GTA 6) på PS5 eller Xbox?', 'Mando TV blander sig hverken i konsollen eller i spillet. Det sørger bare for, at tv\'et er tændt og kører på den rigtige HDMI-indgang, så du kan sætte dig og spille.'),
    ]),
  dict(clave='samsung-lost', corto='Samsung-tv uden fjernbetjening',
    titulo='Samsung fjernbetjening væk? Brug din mobil',
    desc='Samsung fjernbetjening væk eller i stykker? Brug din mobil via wifi som fjernbetjening til Tizen-tv. Nemt med Mando TV, gratis, uden reklamer.',
    h1='Samsung-tv uden original fjernbetjening: Sådan bruger du mobilen',
    intro='Hvis du har mistet din Samsung fjernbetjening, eller den ikke virker mere, kan du bruge din mobil som fjernbetjening via wifi. Det virker på Samsung-tv med Tizen, årgang 2016 og nyere.',
    pasos=[
      'Tænd tv\'et med knappen på apparatet. På de fleste modeller sidder den nederst eller bagpå, nogle gange som en lille joystick.',
      'Tjek, at tv\'et er forbundet til dit wifi, og at din mobil er på det samme netværk.',
      'Åbn Mando TV på din mobil. Dit Samsung-tv dukker op på listen af sig selv. Tryk på det.',
      'Tv\'et beder dig bekræfte forbindelsen. På de fleste modeller bekræfter du den med knapperne på tv\'et eller med joysticken bagpå.',
      'Så er du klar, nu kan du bruge din mobil som fjernbetjening. Knapperne, tastaturet og apps er gratis; touchpad er en Pro-funktion.',
      'For at tænde tv\'et fra mobilen næste gang så gå til Indstillinger > Generelt > Netværk > Ekspertindstillinger og aktivér "Tænd med mobil".',
    ],
    extra=[
      ('Hvis tv\'et ikke spørger om tilladelse', 'Måske er tilladelsen allerede gemt, eller tv\'et er på et andet wifi. Luk Mando TV og åbn appen igen, mens tv\'et er tændt. Er tv\'et ældre end 2016, bruger det et andet system, som endnu ikke understøttes.'),
      ('Hvis du kom til at afvise tilladelsen', 'Gå på tv\'et til Indstillinger > Generelt > Administrator af eksterne enheder > Enhedsforbindelsesadministrator og sæt Mando TV til tilladt. Finder din mobil stadig ikke tv\'et, så læs [Din mobil finder ikke tv\'et](@not-found).'),
    ],
    marca='samsung',
    faq=[
      ('Hvordan bekræfter jeg forbindelsen, hvis jeg ikke har en fjernbetjening?', 'På de fleste modeller bekræfter du den med knapperne på tv\'et eller med joysticken bagpå. Har din model ingen knapper, så skriv til hola@mandotv.app, så hjælper vi dig.'),
      ('Kræver Mando TV en Samsung-konto?', 'Nej. Forbindelsen kører direkte via dit wifi, uden Samsung-konto.'),
      ('Virker det med mit ældre Samsung-tv?', 'Det virker med Samsung-tv med Tizen, årgang 2016 og nyere.'),
    ]),
  dict(clave='wifi', corto='Mobilen som fjernbetjening via wifi',
    titulo='Brug mobilen som fjernbetjening: Styr tv\'et via wifi',
    desc='Forbind din mobil via wifi med tv\'et og brug den som fjernbetjening til Samsung, LG, Roku og Google TV. Trin pr. mærke med Mando TV. Gratis.',
    h1='Sådan forbinder du din mobil via wifi som fjernbetjening til tv\'et',
    intro='Du skal bare have din mobil og dit tv på det samme wifi og en fjernbetjening-app. Mando TV finder dit tv af sig selv og virker med Samsung, LG, Roku, Google TV og Android TV.',
    pasos=[
      'Forbind mobil og tv til det samme wifi.',
      'Åbn Mando TV. Dit tv dukker op på listen af sig selv. Tryk på det.',
      'Bekræft forbindelsen for dit mærke (detaljerne står længere nede).',
      'Styr tv\'et med knapperne eller med din mobils tastatur. Touchpad er en Pro-funktion.',
    ],
    extra=[
      ('Samsung', 'Tv\'et spørger, om du tillader forbindelsen. Bekræft den første gang på skærmen. Det virker med Tizen, årgang 2016 og nyere. For at tænde det fra mobilen så aktivér under Indstillinger > Generelt > Netværk > Ekspertindstillinger muligheden "Tænd med mobil".'),
      ('LG', 'Tv\'et viser en forespørgsel om tilladelse. Bekræft den første gang. For at tænde det fra mobilen så led i indstillingerne efter "Tænd tv med mobil" og aktivér "Tænd via wifi".'),
      ('Roku', 'Roku kræver ingen parring: Tryk på den på listen, og du er forbundet. For at tænde den så aktivér under Indstillinger > System > Strøm muligheden "Hurtig start for tv".'),
      ('Google TV og Android TV', 'Tv\'et viser en kode på skærmen. Indtast den første gang i Mando TV. For at tænde det så led i indstillingerne efter "Wake on LAN", "Tænd via netværk" eller "Netværksstandby".'),
    ],
    marca=None,
    faq=[
      ('Skal jeg have internet for at bruge mobilen som fjernbetjening?', 'Du skal have din mobil og dit tv på det samme wifi. Mando TV forbinder via det netværk direkte til dit tv.'),
      ('Hvorfor dukker mit tv ikke op på listen?', 'Tjek, at tv\'et er tændt, og at din mobil ikke bruger mobildata eller et andet wifi. Nogle routere har et gæstenetværk, der adskiller enheder fra hinanden.'),
      ('Kan jeg bruge Mando TV på iPhone eller på en Android-mobil?', 'På iPhone og iPad, ja: Appen findes allerede i App Store. Til Windows findes den også i Microsoft Store. Android kommer snart: Du kan være med i den gratis tidlige adgang på Google Play.'),
    ]),
  dict(clave='pc', corto='Styr tv\'et fra pc\'en',
    titulo='Styr tv\'et med Windows-pc (gratis)',
    desc='Brug din Windows-pc som fjernbetjening til Samsung, LG, Roku eller Google TV via wifi. Knapper, tastatur og apps gratis; pc-genveje med Pro.',
    h1='Sådan styrer du dit tv med en Windows-pc',
    intro='Når du bruger dagen foran computeren, skal du ikke lede efter fjernbetjeningen: Mando TV til Windows styrer dit Samsung-, LG-, Roku-, Google TV- eller Android TV-tv via dit wifi derhjemme. Praktisk til at skifte app, skrue op for lyden eller skrive i YouTube med pc\'ens tastatur.',
    pasos=[
      'Hent Mando TV gratis fra Microsoft Store til din computer med Windows 10 eller 11.',
      'Tjek, at computer og tv er på det samme netværk (wifi eller kabel, men via den samme router).',
      'Åbn Mando TV: Dit tv dukker op på listen af sig selv. Tryk eller klik på det.',
      'Bekræft første gang forbindelsen på tv\'ets skærm (på Google TV og Android TV indtaster du den kode, tv\'et viser).',
      'Så er du klar: Brug knapperne eller tastaturet til at skrive i tv\'ets søgefelt. Touchpad er en Pro-funktion.',
    ],
    extra=[
      ('Genveje på pc\'en (Pro)', 'Med Mando TV Pro styrer du tv\'et med computerens tastatur: piletaster til at navigere, Enter til OK, Backspace eller Esc til Tilbage, + og - til lydstyrke, M til lydløs og mellemrumstasten til pause.'),
      ('Mini-fjernbetjening altid øverst (Pro)', 'Hav et lille vindue med fjernbetjeningen synligt hele tiden, mens du arbejder eller spiller på pc\'en.'),
      ('Tal til tv\'et fra pc\'en (Pro)', 'Med Mando TV Pro giver du tv\'et kommandoer med pc\'ens mikrofon: "åbn YouTube", "skru op" eller "sluk om 30 minutter", helt som du taler. På Windows genkendes talen på selve pc\'en: Du skal ikke have internet, du skal ikke ændre noget i Windows-indstillingerne, og det virker på de 6 sprog i appen. Det, du siger, forlader ikke pc\'en og bliver ikke gemt. Kun på meget gamle processorer bruger appen Windows\' diktering i stedet. Til det skal onlinetalegenkendelse være slået til i privatlivsindstillingerne, og dansk (Danmark) skal være tilføjet i Windows. Mangler der noget, siger appen til og åbner indstillingen med en knap.'),
    ],
    marca=None,
    faq=[
      ('Skal jeg have kabel eller Bluetooth for at styre tv\'et med pc\'en?', 'Nej. Mando TV forbinder via dit hjemmenetværk: Pc og tv skal bare sidde på den samme router.'),
      ('Virker det med ethvert tv?', 'Det virker med Samsung-tv med Tizen (årgang 2016 og nyere), LG med webOS, Roku samt Google TV eller Android TV (Sony, Philips, TCL, Hisense, Sharp, Xiaomi, Toshiba, Panasonic, Haier, Skyworth og andre).'),
      ('Hvad koster det?', 'Knapperne, tastaturet og tænd via netværket er gratis og uden reklamer. Mando TV Pro er et engangskøb uden abonnement til ekstra ting som touchpad, pc-genveje og mini-fjernbetjeningen.'),
      ('Hvorfor forstår mikrofonen mig ikke på Windows?', 'Tjek, at talefunktionen er aktiv (den hører til Pro), og at pc\'ens mikrofon virker i Windows. På næsten alle pc\'er genkendes talen på selve enheden, helt uden internet. Kun på meget gamle processorer bruger appen Windows\' diktering. Tjek så, at onlinetalegenkendelse er slået til i Windows\' privatlivsindstillinger, og at Windows har dansk (Danmark) i sprogindstillingerne. Mando TV bruger kun dette sprog, mens det lytter.'),
    ]),
  dict(clave='roku-403', corto='Roku-appen virker ikke',
    titulo='Roku-appen virker ikke? Ret fejl 403',
    desc='Mobilen er forbundet, men din Roku reagerer ikke? Aktivér "Styring via mobilapps" i 5 trin og brug mobilen som fjernbetjening igen.',
    h1='Roku-appen virker ikke: Sådan retter du det',
    intro='Hvis din mobil finder Roku og forbinder, men ingen knap gør noget, skyldes det næsten altid en indstilling på selve Roku, der blokerer fjernbetjening-apps. Nyere Roku-versioner er som standard mere begrænsede. I Roku-menuen er det rettet på et minut.',
    pasos=[
      'Tryk på din Roku på Hjem og gå til Indstillinger.',
      'Åbn System og derefter Avancerede systemindstillinger.',
      'Gå til "Styring via mobilapps". På nogle modeller hedder det "Ekstern styring".',
      'Vælg under "Netværksadgang" Standard eller Aktiveret. Er det kun en kontakt på din model, så lad den stå på Aktiveret.',
      'Gå tilbage til Mando TV på din mobil og tryk på din Roku. Knapperne reagerer nu.',
    ],
    extra=[
      ('Sådan ser du, om det er dit problem', 'Tegnet er tydeligt: Din mobil ser Roku på listen og forbinder, men der sker ingenting, når du trykker på en knap. Internt svarer Roku med fejl 403, som betyder "forbudt". Mando TV opdager det ved forbindelsen og viser dig netop disse trin på skærmen.'),
      ('Standard eller Aktiveret, hvad vælger jeg?', 'Begge dele virker: Mando TV skal bare have kommandoer fra dit hjemmenetværk. Står valget på Deaktiveret (på nyere software Begrænset), reagerer Roku ikke på apps.'),
      ('Hvis du ikke har Roku-fjernbetjeningen', 'Står indstillingen på Deaktiveret, kan den kun ændres med den rigtige Roku fjernbetjening. Lån en for at ændre den én gang; bagefter kan du gøre alt med din mobil. Læs også [Roku fjernbetjening væk](@roku-lost).'),
    ],
    marca='roku',
    faq=[
      ('Hvorfor reagerer min Roku ikke mere, selvom det virkede før?', 'En Roku-opdatering kan begrænse denne indstilling mere. Det skyldes ikke din mobil eller dit wifi: Du skal bare tillade styring via apps igen.'),
      ('Gælder det for Roku TV og for Roku-afspillere?', 'Ja. Indstillingen findes på Roku-afspillere og på Roku TV i den samme menu.'),
      ('Er det sikkert at lade indstillingen stå på Standard?', 'Ja. Den accepterer kun kommandoer fra enheder i dit hjemmenetværk.'),
    ]),
  dict(clave='not-found', corto='Mobilen finder ikke tv\'et',
    titulo='Mobilen finder ikke tv\'et? 6 ting at tjekke',
    desc='Finder fjernbetjening-appen ikke dit tv? Tjek wifi, VPN og adgang til det lokale netværk. Til Samsung, LG, Roku og Android TV.',
    h1='Din mobil finder ikke tv\'et: Det skal du tjekke',
    intro='Du åbner fjernbetjening-appen, og listen er tom, eller tv\'et dukker op, men forbindelsen falder. Næsten altid skyldes det netværket og ikke tv\'et. Tjek disse punkter i rækkefølge: Det første løser de fleste tilfælde.',
    pasos=[
      'Se, hvilket wifi din mobil er på, og hvilket tv\'et er på. Det skal være det samme netværk med det samme navn. Et gæstenetværk virker ikke, fordi det adskiller enheder fra hinanden.',
      'Slå VPN fra på din mobil, hvis du bruger en. Med aktiv VPN går din mobil på internettet via et andet netværk og ser ikke enhederne derhjemme, eller forbindelsen falder efter få sekunder.',
      'Slå mobildata fra et øjeblik. Nogle mobiler skifter af sig selv fra wifi til mobildata ved svagt signal.',
      'Tænd tv\'et og vent, til det er færdigt med at starte. Et slukket tv svarer ikke på søgningen.',
      'Tjek på iPhone, at appen har tilladelsen "Lokalt netværk": Indstillinger > Privatliv og sikkerhed > Lokalt netværk.',
      'Dukker det stadig ikke op, så tilføj det manuelt: Tryk i Mando TV på "Tilføj via IP" og indtast tv\'ets IP-adresse.',
    ],
    extra=[
      ('Lad appen guide dig', 'På tv-listen er der en knap til, når dit tv ikke dukker op. Appen tjekker de hyppigste årsager trin for trin (samme wifi, VPN, tilladelse til lokalt netværk og mere) og viser efter hver rettelse en knap til at tjekke igen. Guiden er gratis.'),
      ('Hvor du finder tv\'ets IP-adresse', 'Den står i tv\'ets netværksmenu og er lidt forskellig alt efter model. På LG: Indstillinger, Netværk, Wifi-forbindelse, Avancerede wifi-indstillinger. På Samsung: Indstillinger, Generelt, Netværk, Netværksstatus, IP-indstillinger. På Roku: Indstillinger, Netværk, Om. På Android TV og Google TV: Indstillinger, Netværk og internet, og tryk så på dit netværk. Det er et tal som 192.168.1.86.'),
      ('Hvis det dukker op, men forbindelsen falder', 'Falder forbindelsen efter få sekunder, ligger årsagen som regel hos mobilen: en VPN, skift til et andet wifi eller strømsparetilstand. Slå VPN fra, bliv på det samme wifi og prøv igen.'),
      ('Wifi på 2,4 og 5 GHz', 'Det gør ikke noget, om din mobil er på 5 GHz-nettet og tv\'et på 2,4 GHz-nettet, så længe begge kommer fra den samme router. Har du en wifi-repeater, og tv\'et stadig ikke dukker op, så gå tættere på hovedroutren med mobilen og prøv igen.'),
    ],
    marca=None,
    faq=[
      ('Kan jeg styre tv\'et med mobildata?', 'Nej. Fjernbetjeningssignalet går via dit wifi derhjemme, derfor skal mobil og tv være på det samme netværk.'),
      ('Hvorfor virker det ikke med aktiv VPN?', 'Fordi VPN\'en leder al din mobils trafik via et andet netværk, og mobilen ikke længere ser enhederne derhjemme. Slå den fra, mens du bruger fjernbetjeningen.'),
      ('Virker det med Bluetooth eller infrarød?', 'På smart-tv bruger Mando TV wifi. Infrarød virker kun på Android-mobiler med infrarød sender og er tænkt til tv, der ikke er smart-tv. Bluetooth findes i beta, gratis og kun fra Android 9: Mobilen forbinder med tv\'et som Bluetooth-tastatur og -fjernbetjening, helt uden wifi. Det virker med Google TV, Android TV og Fire TV; på andre mærker, der accepterer Bluetooth-tastaturer, kan det virke, Roku accepterer dem ikke.'),
    ]),
  dict(clave='androidtv-code', corto='Android TV parringskode',
    titulo='Android TV beder om en parringskode: Det skal du gøre',
    desc='Dit Android TV eller Google TV viser en kode på 6 tegn ved forbindelsen. Sådan indtaster du den, og det gør du, hvis den ikke vises eller er forkert.',
    h1='Android TV beder om en parringskode: Det skal du gøre',
    intro='Når du forbinder din mobil med et Android TV eller Google TV for første gang, viser tv\'et en kode på 6 tegn på skærmen. Det er normalt og sker kun én gang: Sådan er det sikkert, at ingen andre kan styre dit tv. Her kan du se, hvordan du indtaster den, og hvad du gør, hvis den ikke vises.',
    pasos=[
      'Tænd tv\'et og lad startskærmen være synlig.',
      'Åbn Mando TV på din mobil, på det samme wifi som tv\'et, og tryk på dit tv på listen.',
      'Se på tv\'ets skærm: En kode på 6 bogstaver og tal dukker op.',
      'Tast den ind på din mobil præcis, som den vises, og tryk på Par. Bogstaverne går kun fra A til F, så et rundt tegn er altid tallet nul.',
      'Så er du klar. Tv\'et husker din mobil og spørger ikke om koden igen.',
    ],
    extra=[
      ('Hvis koden ikke vises på tv\'et', 'Tjek, at tv\'et virkelig er tændt og ikke i standby, og at din mobil er på det samme wifi. Tryk på tv\'et på din mobil igen. Dukker den stadig ikke op, så genstart tv\'et: Træk stikket ud i ti sekunder, sæt det i igen og prøv igen.'),
      ('Hvis koden meldes forkert', 'Koden ændrer sig ved hver forespørgsel. Har du brugt lang tid eller bedt om den to gange, virker kun den sidste på skærmen. Tryk på tv\'et på din mobil igen og indtast den nye kode.'),
      ('Hvis tv\'et beder om koden igen', 'Det sker, hvis tv\'et er nulstillet til fabriksindstillinger, eller du sletter appens data på din mobil. Par igen, så er det gemt. Har du slet ingen fjernbetjening, så læs [Android TV uden fjernbetjening](@androidtv).'),
    ],
    marca='android',
    faq=[
      ('Hvilke tv bruger denne kode?', 'Dem med Android TV eller Google TV: Sony, Philips, TCL, Hisense, Sharp, Xiaomi, Chromecast med Google TV og nogle flere.'),
      ('Skal jeg have en Google-konto på min mobil?', 'Nej. Koden på skærmen er alt, hvad du skal bruge.'),
      ('Er det sikkert?', 'Ja. Koden beviser, at du sidder foran tv\'et: Ingen kan parre uden at se den på skærmen.'),
    ]),
  dict(clave='roku-lost', corto='Roku fjernbetjening væk',
    titulo='Roku fjernbetjening væk? Brug din mobil via wifi',
    desc='Roku fjernbetjening væk? Din mobil overtager via wifi. Enkle trin, også hvis du har skiftet router, og Roku ikke har wifi.',
    h1='Roku fjernbetjening væk: Sådan bruger du mobilen',
    intro='Hvis du har mistet din Roku fjernbetjening, eller den ikke virker mere, overtager din mobil, så længe Roku stadig er forbundet til dit wifi. Og har du skiftet wifi eller router, findes der også en vej ud af det.',
    pasos=[
      'Prøv først at få fjernbetjeningen til at ringe. Har din Roku-fjernbetjening en højttaler, for eksempel Roku Voice Remote Pro, så åbn Mando TV, forbind med Roku og brug muligheden "Find min fjernbetjening", så du kan finde den. Det virker kun med Roku-fjernbetjeninger med højttaler, og Roku skal være tændt.',
      'Tænd tv\'et og lad Roku sidde i. Du skal ikke røre ved den.',
      'Forbind din mobil til det samme wifi, som Roku bruger.',
      'Åbn Mando TV. Roku dukker op på listen af sig selv. Tryk på den.',
      'Brug piletaster, OK, Hjem og Tilbage som på din vante fjernbetjening. Roku spørger ikke efter en kode.',
      'Gør knapperne ingenting, blokerer Roku styring via apps: Guiden [Roku-appen virker ikke](@roku-403) forklarer, hvordan du tillader den.',
    ],
    extra=[
      ('Hvis Roku ikke har wifi (skiftet router eller flyttet)', 'Uden fjernbetjening kommer du ikke ind i menuen for at sætte det nye netværk op, men der er et trick: Roku forbinder af sig selv til et netværk, der har det samme navn og den samme adgangskode som det gamle. Opret på en anden mobil et wifi-hotspot med præcis dette navn og denne adgangskode, forbind mobilen med Mando TV til det, og Roku dukker op på listen. Gå derfra til Indstillinger, Netværk og forbind den med det nye wifi.'),
      ('Hvis det er et Roku TV', 'Roku TV har en knap på apparatet, næsten altid nederst på midten eller bagpå, som tænder tv\'et. Det er nok til at tænde det og fortsætte med mobilen.'),
      ('Hvis du hellere vil købe en anden fjernbetjening', 'Sørg for, at den passer til din model. Små Roku-afspillere bag tv\'et skal bruge en fjernbetjening uden infrarød, fordi infrarød ikke når dem.'),
    ],
    marca='roku',
    faq=[
      ('Kan min mobil tænde Roku?', 'En tilsluttet Roku-afspiller er altid tændt. På et Roku TV tænder Mando TV det via wifi, hvis "Hurtig start for tv" er aktiveret under Indstillinger > System > Strøm.'),
      ('Og lydstyrken?', 'På et Roku TV skruer din mobil op og ned for lyden. På en Roku-afspiller, der er tilsluttet via HDMI, afhænger det af tv\'et: På mange virker det, på andre ikke.'),
      ('Skal jeg oprette en konto?', 'Nej. Mando TV kræver ingen konto og styrer desuden tv fra Samsung, LG og Android TV med den samme app.'),
    ]),
]

SOPORTE = dict(
  titulo='Hjælp: Forbind og tænd tv\'et med Mando TV',
  desc='Sådan forbinder du Mando TV fjernbetjeningen med LG, Samsung, Roku eller Android TV, tænder tv\'et fra mobilen og løser problemer.',
  h1='Hjælp',
  intro='De hyppigste spørgsmål i rækkefølge efter trinene. Finder du ikke dit, så skriv til os på <a href="mailto:hola@mandotv.app?subject=Hj%C3%A6lp%20til%20Mando%20TV">hola@mandotv.app</a>, så svarer vi.',
)
SOPORTE_HTML = '''      <h2 id="encontrar">Find tv\'et</h2>
      <div class="preguntas">
        <details open><summary>Mit tv dukker ikke op på listen</summary>
          <ol>
            <li>Tjek, at din mobil og tv\'et er på det samme wifi. Har din router et 2,4 GHz- og et 5 GHz-netværk med forskellige navne, ser de nogle gange ikke hinanden.</li>
            <li>Sørg for, at tv\'et er tændt.</li>
            <li>Tjek på iPhone, at Mando TV har tilladelsen "Lokalt netværk", under Indstillinger, Mando TV.</li>
            <li>Tryk på tv-listen på knappen til, når dit tv ikke dukker op: Appen tjekker de hyppigste årsager trin for trin (samme wifi, VPN, tilladelse til lokalt netværk og mere) og viser efter hver rettelse en knap til at tjekke igen.</li>
            <li>Dukker det stadig ikke op, så tryk på knappen +, vælg mærket og indtast tv\'ets IP-adresse. Du kan se den i tv\'ets netværksmenu (for eksempel 192.168.1.50).</li>
          </ol>
        </details>
        <details><summary>Virker det med mobildata eller på farten?</summary>
          <p>Nej. Mando TV taler med tv\'et inde i dit hjemmenetværk, så din mobil skal være forbundet til det wifi.</p>
        </details>
      </div>

      <h2 id="conectar">Forbind første gang</h2>
      <p>Komplette guider pr. mærke: <a href="@@R_lg@@">LG</a>, <a href="@@R_samsung@@">Samsung</a>, <a href="@@R_roku@@">Roku</a> og <a href="@@R_android@@">Android TV</a>.</p>
      <div class="preguntas">
        <details><summary>LG</summary>
          <p>Når du trykker på tv\'et, vises der en forespørgsel om tilladelse på skærmen. Bekræft den med din vante fjernbetjening. Det gør du kun én gang.</p>
        </details>
        <details><summary>Samsung</summary>
          <p>Tv\'et spørger, om du tillader forbindelsen fra Mando TV. Vælg "Tillad" med fjernbetjeningen. Har du kommet til at afvise den, så gå til Indstillinger > Generelt > Administrator af eksterne enheder > Enhedsforbindelsesadministrator og ændr det til tilladt.</p>
        </details>
        <details><summary>Roku</summary>
          <p>Roku spørger ikke om tilladelse. Lykkes forbindelsen ikke, så gå på Roku til Indstillinger > System > Avancerede systemindstillinger > Styring via mobilapps og lad netværksadgangen stå på Standard eller Aktiveret.</p>
        </details>
        <details><summary>Android TV og Google TV</summary>
          <p>Tv\'et viser en kode på 6 tegn. Indtast den i Mando TV præcis, som den vises. Det virker på Sony, Philips, TCL, Hisense, Sharp, Xiaomi, Chromecast med Google TV og andre med Android TV.</p>
        </details>
      </div>

      <h2 id="encender">Tænd tv\'et fra appen</h2>
      <p>Mando TV tænder tv\'et via dit hjemmenetværk. Det kræver to ting: Du har forbundet mindst én gang, mens tv\'et var tændt, og på tv\'et er tænd via netværket aktiveret. Indstillingens navn ændrer sig efter model; her er de hyppigste:</p>
      <div class="preguntas">
        <details><summary>LG</summary>
          <p>Led i indstillingerne (afhængigt af modellen under Generelt eller Forbindelse) efter "Tænd tv med mobil" og aktivér "Tænd via wifi". Findes der "Hurtig start+", så aktivér den også.</p>
        </details>
        <details><summary>Samsung</summary>
          <p>Aktivér "Tænd med mobil" under Indstillinger > Generelt > Netværk > Ekspertindstillinger.</p>
        </details>
        <details><summary>Roku</summary>
          <p>Aktivér på Roku TV "Hurtig start for tv" under Indstillinger > System > Strøm. Roku-afspillere, der er sluttet til et tv, kan ikke tændes på den måde.</p>
        </details>
        <details><summary>Android TV og Google TV</summary>
          <p>Det afhænger af producenten. Led i netværks- eller strømindstillingerne efter "Wake on LAN", "Tænd via netværk" eller "Netværksstandby". Nogle modeller har ikke denne mulighed.</p>
        </details>
      </div>

      <h2 id="falla">Når noget ikke virker</h2>
      <div class="preguntas">
        <details><summary>Forbindelsen falder, eller der kommer ingen reaktion</summary>
          <ol>
            <li>Tryk på fjernbetjeningsskærmen på Forbind igen.</li>
            <li>Hjælper det ikke, så luk Mando TV og åbn appen igen.</li>
            <li>Har tv\'et fået en anden IP-adresse, så fjern det fra listen og tilføj det igen.</li>
          </ol>
        </details>
        <details><summary>Sådan sender du os en fejlrapport</summary>
          <ol>
            <li>Tryk i Mando TV på knappen Tilpas (skyderne øverst).</li>
            <li>Tryk på Kopiér testrapport.</li>
            <li>Indsæt den sammen med mærke og model på dit tv i en e-mail til hola@mandotv.app.</li>
          </ol>
          <p>Rapporten indeholder ingen adgangskoder, ingen koder og intet af det, du skriver.</p>
        </details>
        <details><summary>Jeg har købt Pro, og det dukker ikke op</summary>
          <p>Tryk under Tilpas på Gendan køb, med den samme butikskonto, som du købte med. Dukker det stadig ikke op, så skriv til os.</p>
        </details>
      </div>

      <h2 id="guias">Guider trin for trin</h2>
      <p><a href="@@R_guias@@">Se alle guider</a></p>
      <ul>
@@GUIAS@@
      </ul>

      <h2 id="contacto">Har du flere spørgsmål?</h2>
      <p>Skriv til os på <a href="mailto:hola@mandotv.app?subject=Hj%C3%A6lp%20til%20Mando%20TV">hola@mandotv.app</a>. Fortæl os mærke og model på dit tv, og hvilket trin du sidder fast på. Skriv til os på dansk. Vi svarer på spansk eller engelsk og, hvis du ønsker det, på dansk ved hjælp af en oversætter.</p>
'''

PRIVACIDAD = dict(
  titulo='Privatlivspolitik | Mando TV',
  desc='Mando TV indsamler ingen personlige data: ingen konti, ingen reklamer, ingen trackere. Appen taler kun med dit tv inde i dit wifi.',
  h1='Privatliv',
  intro='Kort sagt: Mando TV indsamler ikke dine data. Der er ingen konti, ingen reklamer, ingen trackere og ingen egne servere, der gemmer, hvad du gør.',
)
PRIVACIDAD_HTML = '''      <p class="fecha">Gælder fra 14. november 2026. Senest opdateret 25. november 2026.</p>

      <h2>Hvem vi er</h2>
      <p>Mando TV er en app, som du styrer dit tv med fra din mobil eller computer. Denne politik beskriver, hvilke oplysninger appen bruger, og hvad den gør med dem. Har du spørgsmål, så skriv til os på <a href="mailto:hola@mandotv.app">hola@mandotv.app</a>.</p>

      <h2>Hvilke data vi indsamler</h2>
      <p>Appen: ingen. Appen sender hverken oplysninger om dig eller om, hvordan du bruger den, til os eller til tredjeparter. Den bruger ingen analyse-, reklame- eller sporingsværktøjer.</p>
      <p>Denne hjemmeside: Vi måler besøg på to måder, som er forklaret i afsnittet <a href="#cookies">Cookies på denne hjemmeside</a>.</p>

      <h2>Hvad appen gemmer på din enhed</h2>
      <p>For at fungere gemmer appen følgende kun på din mobil eller computer:</p>
      <ul>
        <li>De tv, du har tilføjet: navn, mærke, IP-adresse i dit netværk og netværkets hardwareadresse (MAC), som bruges til at tænde dem.</li>
        <li>De forbindelsesnøgler, som hvert tv udleverer, når du bekræfter tilladelsen. De gemmes krypteret i systemets sikre lager (nøglering på iPhone og Mac, Keystore på Android, beskyttet lager på Windows).</li>
        <li>Dine indstillinger: lyst eller mørkt tema, baggrundsfarve, vibration og typen af fjernbetjening.</li>
        <li>Hvis du bruger Pro-funktionerne: dine yndlingsapps, dine rutiner og dine seneste YouTube-søgninger (du kan slette dem i appen).</li>
      </ul>
      <p>Når du sletter appen, bliver alt dette slettet sammen med den.</p>

      <h2>Hvem appen taler med</h2>
      <p>Med dine tv, inde i dit wifi derhjemme. For at finde dem gennemsøger appen dit lokale netværk; derfor beder den på en iPhone om tilladelsen "Lokalt netværk". Den tekst, du skriver med appens tastatur, går direkte til tv\'et og bliver ikke gemt.</p>
      <p>Derudover henter appen ved åbning en lille offentlig fil fra denne hjemmeside (mandotv.app/app/config.json) for at finde ud af, om der er en ny version, du bør installere, og hvilke funktioner der hører til Mando TV Pro. Det er en download, som når man åbner en side: Appen sender hverken dine data eller dine tv eller det, du gør. Den oplyser kun appens version og systemet (for eksempel Android), så den kan vise dig den rigtige besked. Har du intet internet, arbejder appen videre med den senest hentede fil; går der mere end 30 dage, uden at den har kunnet hentes, beder appen dig om kort at forbinde til internettet.</p>

      <p>Når du sender fotos eller videoer til tv\'et (en Pro-funktion), henter tv\'et kun de filer, du vælger, direkte fra din mobil eller pc via dit wifi derhjemme. De går hverken over internettet eller via os, appen ser ikke dine øvrige fotos, og delingen slutter, så snart du lukker den skærm.</p>
      <h2>Mikrofon og tale</h2>
      <p>Stemmesøgningen bruger mikrofonen kun, mens du trykker på taleknappen. Det, du siger, omdannes til tekst af dit systems talegenkendelse: af Apple på iPhone og Mac og af Google på Android, hver efter deres egne privatlivsvilkår. På Windows genkendes talen på din egen pc og forlader ikke enheden; kun på meget gamle processorer bruger appen Windows\' taleinput, fra Microsoft, efter deres privatlivsvilkår. Mando TV optager eller gemmer ikke lyden, og den tekst, der opstår, går direkte til dit tv, ligesom det, du skriver med tastaturet.</p>

      <h2>Hjem: enheder fra Apple Home og Google Home</h2>
      <p>Når du åbner området Hjem (i test), beder appen om tilladelse til at se de enheder, du allerede har i Apples Hjem-app (HomeKit) eller i Google Home. Med den tilladelse læser den deres navn, deres rum og deres tilstand (tændt eller slukket, lysstyrke, temperatur eller hvor langt et husholdningsapparat er i sit program) for at vise dem og sende dem det, du trykker på. Alt sker mellem din mobil og Apples eller Googles system: Mando TV gemmer ikke denne liste, sender den hverken til os eller til tredjeparter og bruger den hverken til reklamer eller analyser. På Android virker Google Home med din egen Google-konto, efter Googles privatlivspolitik. Du kan til enhver tid tilbagekalde tilladelsen: på iPhone under Indstillinger &gt; Privatliv og sikkerhed &gt; HomeKit, på Android i indstillingerne til din Google-konto.</p>
      <p>Når du trykker på "Hvordan fungerede Hjem for dig?", åbner din e-mail-app med en besked til hola@mandotv.app, der indeholder en teknisk sammenfatning: appens version, systemet og hvor mange enheder af hver type der dukkede op, og om de reagerer. Navne på enheder, rum eller dit hjem er ikke med, og beskeden sendes kun, hvis du selv sender den.</p>

      <h2>Testrapport</h2>
      <p>Appen har en knap "Kopiér testrapport", der hjælper os med at rette fejl. Rapporten bliver kun i appens hukommelse, mens den er åben, og bliver aldrig sendt af sig selv: Du bestemmer, om du kopierer og deler den. Den indeholder ingen forbindelsesnøgler, ingen parringskoder og intet af det, du indtaster; kun de trin, appen har udført, som søgning, forbindelse og fejlene.</p>

      <h2 id="cookies">Cookies på denne hjemmeside</h2>
      <p>Det gælder kun hjemmesiden mandotv.app, ikke appen.</p>
      <h3>Altid uden cookies</h3>
      <p>Vi tæller besøg anonymt med Cloudflare Web Analytics: hvor mange der besøger hjemmesiden, hvilke sider de læser, og fra hvilket land. Det bruger ingen cookies, bruger ikke din IP-adresse til at identificere dig og følger ikke, hvad du gør på andre hjemmesider.</p>
      <h3>Med cookies, kun hvis du accepterer</h3>
      <p>Når du i cookie-beskeden trykker på "Accepter", aktiverer vi Google Analytics (fra Google LLC) for bedre at forstå, hvordan hjemmesiden bruges: sidevisninger, besøgstid, enhedstype, omtrentlig by og hvor du kommer fra. Til det gemmer det cookies af typen _ga og _ga_* i op til 2 år i din browser. Google kan behandle disse data på servere uden for Chile. Vi har slået reklamefunktionerne og Google Signals fra og bruger ikke disse data til at vise dig reklamer.</p>
      <p>Trykker du på "Afvis" eller ikke vælger noget, indlæses Google Analytics ikke, og der gemmes ingen cookie. Du kan til enhver tid ændre dit valg med knappen "Cookies" nederst på hver side; trækker du samtykket tilbage, sletter vi disse cookies.</p>
      <p>Dit valg gemmes i din browser (lokalt lager, sendes ikke til nogen), så vi ikke spørger dig igen.</p>

      <h2>Køb</h2>
      <p>Når du køber Mando TV Pro, håndteres betalingen af app-butikken (App Store, Google Play eller Microsoft Store). Vi modtager og gemmer ikke dine kortoplysninger. Butikken bekræfter kun over for appen, at købet findes.</p>

      <h2>E-mails, du sender os</h2>
      <p>Når du skriver til os på <a href="mailto:hola@mandotv.app">hola@mandotv.app</a>, bruger vi din e-mailadresse og det, du fortæller os, kun til at svare dig. Vi giver dem ikke videre og bruger dem ikke til reklamer. Du kan til enhver tid kræve, at vi sletter dine beskeder.</p>

      <h2>Børn</h2>
      <p>Appen indsamler ikke data fra nogen, heller ikke fra børn.</p>

      <h2>Ændringer i denne politik</h2>
      <p>Skulle det en dag ændre sig, hvad appen gør med dine data, opdaterer vi denne side og datoen øverst, før ændringen når appen.</p>
'''


# >>> guider hentet fra engelsk (ensamblar.py)
GUIAS += [
  dict(clave='no-sub', corto='Fjernbetjening-app uden abonnement', fecha='2026-11-23',
    titulo='Fjernbetjening-app til tv uden abonnement og reklamer',
    desc='Træt af fjernbetjening-apps med reklamer eller ugeabonnement? Mando TV er gratis og uden reklamer, Pro er et valgfrit engangskøb. Ærlig sammenligning.',
    h1='En fjernbetjening-app uden abonnement og uden reklamer',
    intro='Mange universalfjernbetjeninger viser reklamer eller kræver et ugentligt abonnement, før de virker. Mando TV går en anden vej: Fjernbetjeningen er gratis, der er ingen reklamer og ingen konto. Det valgfrie Pro køber du kun én gang. Her er sammenligningen, også med det, appen ikke kan.',
    pasos=[
      'Åbn før installationen en apps butikside og tjek køb i appen. Ugentlige eller månedlige priser tyder på et abonnement.',
      'Tjek på Google Play, om der på siden står "Indeholder reklamer", og læs de nyeste anmeldelser med få stjerner: Dér dukker uventede betalingsmure ofte op.',
      'Sørg for, at appen kan styre dit tv via wifi. Mando TV virker med Samsung (fra 2016), LG webOS, Roku, Google TV, Android TV og Fire TV.',
      'Installer Mando TV, forbind din mobil til det samme wifi som tv\'et og tryk på dit tv på listen.',
      'Bekræft forespørgslen på tv\'et eller indtast den viste kode. Knapper, lydstyrke, kanaler og tastatur koster ingenting.',
    ],
    tabla=dict(titulo='Mando TV sammenlignet med mange fjernbetjening-apps',
      cabeza=['', 'Mando TV', 'Mange reklamefinansierede apps eller abonnementsapps'],
      filas=[
        ['Grundlæggende fjernbetjening', 'Gratis', 'Ofte gratis med reklamer eller skjult bag en prøveperiode'],
        ['Reklamer', 'Ingen', 'Hyppige'],
        ['Abonnement', 'Intet. Pro er et valgfrit engangskøb', 'Ugentlige eller månedlige planer er almindelige'],
        ['Konto', 'Ikke nødvendig', 'Varierer'],
        ['Smart-tv via wifi', 'Samsung (fra 2016), LG webOS, Roku, Google TV, Android TV, Fire TV, Apple TV (beta)', 'Afhænger af appen'],
        ['Infrarød til ældre tv', 'Gratis på Android-mobiler med infrarød sender (ny)', 'Nogle apps, kun på mobiler med infrarød sender'],
        ['Bluetooth', 'Beta fra Android 9, gratis', 'Afhænger af appen'],
        ['Fotos og videoer på tv\'et', 'Pro, via wifi (ingen skærmdublering)', 'Afhænger af appen'],
        ['Mobiler og computere', 'iPhone, iPad og Windows, desuden Android i tidlig adgang', 'Varierer'],
        ['Skærmdublering', 'Gratis på iPhone og iPad, via skærmdublering i Kontrolcenter (tv med AirPlay)', 'Nogle apps tilbyder det'],
      ],
      nota='Mando TV sammenlignes ikke med nogen bestemt app. De aktuelle priser står på hver apps butikside.'),
    extra=[
      ('Hvad Mando TV ikke gør', 'Den har ingen egen skærmdublering: På iPhone og iPad fører den dig til skærmdublering i Kontrolcenter, en funktion i selve iPhone, der virker med tv med AirPlay. Med Mando TV Pro kan den desuden sende fotos og videoer til tv\'et via dit wifi. Den styrer smart-tv via wifi derhjemme. Tv uden smart-funktion kan styres med infrarød fra en Android-mobil med infrarød sender. Fra Android 9 kan mobilen også via Bluetooth forbinde som tastatur og fjernbetjening med Google TV, Android TV og Fire TV, helt uden wifi. Denne mulighed er i beta og gratis.'),
      ('Hvordan Mando TV tjener penge', 'Ikke med reklamer og ikke med dine data: Appen indsamler ingen. Mando TV finansieres af Pro, et valgfrit engangskøb til ekstra ting. Den grundlæggende fjernbetjening er gratis.'),
      ('På de enheder, du allerede har', 'iPhone og iPad fra App Store, Windows-pc\'er fra Microsoft Store og Android via gratis tidlig adgang på Google Play. Se [Fjernbetjening-app til iPhone](@iphone) og [Fjernbetjening-app til Windows](@windows).'),
      ('Privatliv', 'Ingen konto og ingen sporing i appen. Kommunikationen med tv\'et sker kun i det lokale netværk, forbindelsesdataene bliver krypteret på din enhed. Detaljer i [privatlivspolitikken](@privacidad).'),
    ],
    marca=None,
    faq=[
      ('Findes der en fjernbetjening-app uden abonnement?', 'Ja. Mando TV har slet intet abonnement: Fjernbetjeningen er gratis og uden reklamer, Pro er et valgfrit engangskøb.'),
      ('Er Mando TV virkelig gratis?', 'Ja. Piletaster, OK, Tilbage, Hjem, lydstyrke, kanaler, tal, tastatur og tænd/sluk er gratis, uden reklamer og uden tidsgrænse.'),
      ('Virker det uden wifi?', 'For det meste nej. Mando TV styrer smart-tv via dit wifi derhjemme. Undtagelser: Infrarød på Android-mobiler med infrarød sender, som også virker med tv uden smart-funktion eller uden wifi-forbindelse, og Bluetooth, i beta fra Android 9, til Google TV, Android TV og Fire TV.'),
    ]),
  dict(clave='roku-app-alt', corto='Alternativ til Roku-appen', fecha='2026-11-23',
    titulo='Alternativ til Roku-appen: enkel Roku-fjernbetjening',
    desc='Et alternativ til Roku-appen som fjernbetjening: Mando TV styrer Roku TV og -afspillere via wifi, uden konto og reklamer, desuden Samsung, LG og Google TV.',
    h1='Alternativ til Roku-appen: én til alle tv',
    intro='Den officielle Roku-app kan meget: Channel Store, casting, privat lytning og en fjernbetjening. Leder du bare efter en hurtig fjernbetjening, eller har du derhjemme også et Samsung-, LG- eller Google TV-tv, er Mando TV et enkelt alternativ, der styrer Roku via dit wifi uden konto.',
    pasos=[
      'Forbind din mobil og Roku til det samme wifi.',
      'Hent Mando TV og åbn det. Dit Roku TV eller din Roku-afspiller dukker op på listen. Tryk på det. Roku spørger ikke efter en kode.',
      'Brug piletasterne, OK, Tilbage, Hjem, lydstyrke og tastaturet. Indtast søgeord i Roku-kanaler med mobilens tastatur.',
      'Gør knapperne ingenting, så gå på Roku til Indstillinger > System > Avancerede systemindstillinger > Styring via mobilapps og sæt netværksadgang til Standard eller Aktiveret (på nyere Roku-software sættes Styring via mobilapps til Aktiveret).',
      'Valgfrit: Aktivér på Roku TV "Hurtig start for tv" under Indstillinger > System > Strøm, så Mando TV kan tænde tv\'et.',
    ],
    extra=[
      ('Hvor Mando TV passer bedre', 'Én app til flere tv: Roku, Samsung, LG og Google TV eller Android TV. Uden konto, uden reklamer. Den virker også på en Windows-pc, hvilket er praktisk ved skrivebordet. Piletaster og lydstyrke reagerer hurtigt, og med tastaturet skriver du søgeord uden besvær.'),
      ('Hvor den officielle Roku-app er bedre', 'Behold Roku-appen til det, den kan ud over fjernbetjeningen, som at gennemse og tilføje kanaler fra Roku Channel Store samt den egen casting og privat lytning (lyd i hovedtelefoner på mobilen). Brug begge, hvis du vil. De kan køre på den samme mobil.'),
      ('Roku TV og Roku-afspillere', 'Begge virker. Det omfatter Roku TV-modeller fra TCL, Hisense, Philips og andre samt Roku Express, Streaming Stick og Ultra. Detaljer finder du på [siden om Roku fjernbetjening-appen](@roku).'),
      ('Hvis Roku-appen ikke virker mere', 'Når knapperne ikke reagerer mere, blokerer Roku som regel styring via apps. Vejledningen [Roku-appen virker ikke](@roku-403) viser den indstilling, der løser problemet.'),
      ('Gratis og Pro', 'Piletaster, OK, Tilbage, Hjem, lydstyrke, kanaler, taltaster, tastatur, at åbne apps, at skifte indgange og at tænde eller slukke er gratis, uden reklamer og uden abonnement. Mando TV Pro er et valgfrit engangskøb til ekstra ting.'),
    ],
    marca='roku',
    faq=[
      ('Skal jeg have en Roku-konto for at bruge Mando TV?', 'Nej. Mando TV kommunikerer med Roku via dit hjemmenetværk og spørger ikke efter en konto.'),
      ('Erstatter Mando TV Roku Mobile-appen helt?', 'Som fjernbetjening, ja. Til Channel Store, casting og privat lytning beholder du den officielle Roku-app.'),
      ('Virker det med min Roku Express eller Streaming Stick?', 'Ja. Alle Roku-afspillere og Roku TV styres på samme måde.'),
    ]),
  dict(clave='lg-thinq', corto='Alternativ til LG ThinQ-appen', fecha='2026-11-23',
    titulo='Alternativ til LG ThinQ-appen: LG-fjernbetjening uden konto',
    desc='Leder du efter et alternativ til LG ThinQ-appen kun som fjernbetjening? Mando TV styrer LG-tv med webOS via wifi, uden LG-konto og uden reklamer.',
    h1='Alternativ til LG ThinQ-appen til dit LG-tv',
    intro='LG ThinQ er LG\'s officielle app, tænkt til hele det smarte hjem: husholdningsapparater, tv\'et og mere. Vil du bare have en enkel fjernbetjening til dit LG-tv, klarer Mando TV netop det via dit wifi derhjemme, uden at du skal oprette en LG-konto og uden reklamer.',
    pasos=[
      'Forbind din mobil eller pc (iPhone, Android eller Windows) og dit LG-tv til det samme wifi.',
      'Hent Mando TV og åbn det. Dit LG-tv dukker op på listen af sig selv. Tryk på det.',
      'På tv\'et kommer der en forespørgsel. Bekræft den én gang med tv\'ets fjernbetjening, joysticken under skærmen eller Magic Remote.',
      'Knapper, lydstyrke og tastatur virker med det samme. Du skal ikke have en LG-konto og skal ikke registrere tv\'et.',
      'Valgfrit: Aktivér "Tænd tv med mobil" i tv\'ets indstillinger, så du også kan tænde tv\'et fra mobilen.',
    ],
    extra=[
      ('Mando TV eller LG ThinQ: hvad til hvad', 'Brug ThinQ, hvis du vil styre LG-husholdningsapparater som en vaskemaskine, et køleskab eller et klimaanlæg eller har brug for LG-kontofunktioner. Brug Mando TV, hvis du vil have en hurtig, enkel fjernbetjening til tv\'et, der også virker til Samsung, Roku og Google TV i den samme app. Mange beholder begge: ThinQ til apparaterne, Mando TV til tv\'et.'),
      ('Hvad Mando TV gør på et LG-tv', 'Det virker med LG smart-tv med webOS, altså de fleste modeller siden 2014, herunder LED, NanoCell, QNED og OLED. Det giver dig piletaster, OK, Tilbage, Hjem, lydstyrke, kanaler, lydløs, afspilningsstyring og et tastatur til at skrive i YouTube, Netflix eller browseren. Listen over apps og listen over indgange er også gratis. Med Pro får du desuden en markør som på Magic Remote.'),
      ('Hvad Mando TV ikke gør', 'Det styrer ingen LG-husholdningsapparater, det bruger ikke din LG-konto, og det erstatter ikke LG\'s kontotjenester på tv\'et. Det er en fjernbetjening, ikke en smart home-hub.'),
      ('Privatliv og reklamer', 'Mando TV har ingen reklamer og ingen konto. Det taler kun inde i dit hjemmenetværk med tv\'et og gemmer forbindelsesnøglen krypteret på din enhed. Alle funktioner finder du på siden [LG fjernbetjening-app](@lg).'),
      ('Gratis og Pro', 'Piletaster, OK, Tilbage, Hjem, lydstyrke, kanaler, taltaster, tastatur, at åbne apps, at skifte indgange og tænd/sluk er gratis, uden reklamer og uden abonnement. Mando TV Pro er et valgfrit engangskøb til ekstra ting.'),
    ],
    marca='lg',
    faq=[
      ('Kan jeg styre mit LG-tv uden appen LG ThinQ?', 'Ja. Mando TV forbinder direkte via dit wifi med LG-tv med webOS. Du accepterer én gang en forespørgsel på tv\'et, og så er det det, helt uden LG-konto.'),
      ('Virker Mando TV med markøren fra LG Magic Remote?', 'Mando TV Pro har en markør, som du flytter med fingeren på mobilens skærm, ligesom Magic Remote flytter pilen.'),
      ('Er Mando TV fra LG?', 'Nej. Mando TV er en uafhængig app og har ingen forbindelse til LG. LG og ThinQ tilhører deres ejere og nævnes kun for at beskrive kompatibiliteten.'),
    ]),
  dict(clave='smartthings', corto='SmartThings-alternativ', fecha='2026-11-23',
    titulo='SmartThings virker ikke? Enkelt alternativ til Samsung',
    desc='SmartThings for langsom eller fejlbehæftet? Mando TV styrer Samsung-tv med Tizen direkte via wifi. Uden Samsung-konto, uden reklamer. Trin for trin.',
    h1='SmartThings-alternativ til Samsung-tv',
    intro='SmartThings er Samsungs app til hele det smarte hjem, og dens fjernbetjening kører via din Samsung-konto. Virker den ikke mere, eller leder du efter en hurtig løsning, styrer Mando TV Samsung-tv med Tizen, årgang 2016 og nyere, direkte via dit wifi uden konto.',
    pasos=[
      'Forbind din mobil og Samsung-tv\'et til det samme wifi.',
      'Hent Mando TV og åbn appen. Dit Samsung-tv dukker op på listen af sig selv. Tryk på det.',
      'Tv\'et spørger, om du vil tillade forbindelsen. Vælg "Tillad" med fjernbetjeningen eller med knappen på tv\'et (kun første gang).',
      'Brug med det samme piletasterne, OK, Tilbage, Hjem, lydstyrke, kanaler og tastaturet.',
      'Valgfrit: Aktivér "Tænd med mobil" under Indstillinger > Generelt > Netværk > Ekspertindstillinger, så Mando TV også kan tænde tv\'et.',
    ],
    extra=[
      ('Hvorfor en mobil-fjernbetjening ikke virker mere', 'Årsagerne er som regel enkle: Mobil og tv er på forskellige wifi, en VPN er aktiv, eller tv\'et er i dyb standby. Hos SmartThings kan desuden Samsung-kontoen give problemer, for eksempel hvis du er blevet logget ud. Mando TV taler direkte med tv\'et i hjemmenetværket, der er ingen konto at logge ind på. Flere tips finder du under [Din mobil finder ikke tv\'et](@not-found).'),
      ('Mando TV eller SmartThings: hvad til hvad', 'Behold SmartThings, hvis du bruger det til Samsung-husholdningsapparater, lamper eller andre smart home-enheder eller til funktioner i din Samsung-konto. Brug Mando TV, hvis du bare vil have en hurtig fjernbetjening til tv\'et eller derhjemme også har en enhed fra LG, Roku, Google TV eller Fire TV: Én app styrer alle. Begge apps kan være installeret på den samme mobil.'),
      ('Hvis du kom til at afvise tilladelsen', 'Gå på tv\'et til Indstillinger > Generelt > Administrator af eksterne enheder > Enhedsforbindelsesadministrator og sæt Mando TV til tilladt.'),
      ('Ingen fjernbetjening?', 'Du kan bekræfte forespørgslen med knappen på selve tv\'et. Vejledningen [Samsung-tv uden original fjernbetjening](@samsung-lost) viser dig, hvordan.'),
      ('Gratis og Pro', 'Fjernbetjeningen kan du hente og bruge gratis, uden reklamer og uden abonnement. Mando TV Pro er et valgfrit engangskøb til ekstra ting.'),
    ],
    marca='samsung',
    faq=[
      ('Kan jeg styre mit Samsung-tv uden SmartThings?', 'Ja. Mando TV forbinder direkte via dit wifi med Samsung-tv med Tizen. Du tillader forbindelsen én gang på tv\'et, uden Samsung-konto.'),
      ('Styrer Mando TV også Samsung-husholdningsapparater?', 'Nej. Det er kun en fjernbetjening til tv\'et. Til husholdningsapparater og andre smart home-enheder beholder du SmartThings.'),
      ('Er Mando TV fra Samsung?', 'Nej. Mando TV er en uafhængig app og har ingen forbindelse til Samsung. Samsung og SmartThings tilhører deres ejere og nævnes kun for at beskrive kompatibiliteten.'),
    ]),
  dict(clave='googletv-alt', corto='Alternativ til Google TV-fjernbetjeningen', fecha='2026-11-23',
    titulo='Google TV-fjernbetjeningen virker ikke? Alternativet',
    desc='Finder mobil-fjernbetjeningen til Google TV ikke tv\'et? Mando TV styrer Google TV og Android TV via wifi, uden Google-konto og reklamer.',
    h1='Alternativ til Google TV-fjernbetjeningen på mobilen',
    intro='Mobil-fjernbetjeningen til Google TV og Android TV sidder i Googles egen app og er knyttet til din Google-konto. Finder den ikke tv\'et, kommer du ingen vegne. Mando TV er en separat fjernbetjening-app, der parres med koden på 6 tegn på skærmen og virker uden Google-konto, på en iPhone, en Android-mobil eller en Windows-pc.',
    pasos=[
      'Tænd tv\'et og forbind din mobil til det samme wifi.',
      'Hent Mando TV og åbn appen. Tryk på dit tv med Google TV eller Android TV på listen.',
      'Tv\'et viser en kode på 6 tegn. Indtast den i Mando TV og tryk på Par.',
      'Brug piletasterne, OK, Tilbage, Hjem, lydstyrken og tastaturet. Du skal ikke logge ind nogen steder.',
      'Valgfrit: Led i tv\'ets indstillinger efter Wake on LAN eller "Tænd via netværk", så appen også kan tænde tv\'et.',
    ],
    extra=[
      ('Hvorfor mobil-fjernbetjeningen ikke finder tv\'et mere', 'For det meste ligger det i netværket: Mobil og tv er på forskellige wifi, en VPN er aktiv, eller et gæstenetværk adskiller enhederne. Ret det først, da det rammer alle fjernbetjening-apps. Mere i [Din mobil finder ikke tv\'et](@not-found).'),
      ('Med hvilke tv det virker', 'Tv med Google TV og Android TV fra Sony, TCL, Hisense, Philips, Sharp, Xiaomi, Toshiba og flere, samt Chromecast med Google TV, Google TV Streamer og Nvidia Shield. Alle parres ens, én gang med koden på skærmen.'),
      ('Hvor Googles app er bedre', 'Googles app hjælper dig også med at finde indhold at se og husker din huskeliste. Behold den til det. Mando TV er kun fjernbetjeningen og styrer desuden Samsung, LG, Roku og Fire TV-enheder fra den samme app samt fra en Windows-pc.'),
      ('Hvis den gamle Android TV-fjernbetjening-app mangler', 'Google har flyttet mobil-fjernbetjeningen fra den gamle app Android TV Remote Control til Google TV-appen. Leder du efter en selvstændig fjernbetjening, er Mando TV en mulighed.'),
      ('Gratis og Pro', 'Fjernbetjeningen kan du hente og bruge gratis, uden reklamer og uden abonnement. Mando TV Pro er et valgfrit engangskøb til ekstra ting.'),
    ],
    marca='android',
    faq=[
      ('Skal jeg have en Google-konto for at bruge Mando TV med Google TV?', 'Nej. Koden på tv\'et er nok til parringen.'),
      ('Virker det med Chromecast med Google TV?', 'Ja. Parringen foregår på samme måde, med koden på 6 tegn på skærmen.'),
      ('Kan jeg bruge det fra en iPhone?', 'Ja. Mando TV findes i App Store til iPhone og iPad, i Microsoft Store til Windows og i den gratis tidlige adgang på Google Play til Android.'),
    ]),
  dict(clave='windows', corto='Fjernbetjening til Windows-pc', fecha='2026-11-23',
    titulo='Fjernbetjening-app til Windows: Styr tv\'et fra pc\'en',
    desc='Styr Samsung, LG, Roku, Google TV eller Fire TV fra en Windows-pc med Mando TV: genveje, mini-fjernbetjening og wifi. I Microsoft Store.',
    h1='Fjernbetjening-app til Windows-pc',
    intro='Mando TV har en Windows-app, der forvandler din pc eller bærbare til en fjernbetjening til tv\'et via hjemmenetværket. Skriv på tv\'et med dit rigtige tastatur, lad et lille fjernbetjeningsvindue ligge øverst, mens du arbejder, og styr Samsung, LG, Roku, Google TV eller Fire TV med den samme app.',
    pasos=[
      'Installer Mando TV gratis fra Microsoft Store på en pc med Windows 10 eller 11.',
      'Sørg for, at pc\'en og tv\'et er på det samme netværk, via wifi eller kabel på den samme router.',
      'Åbn Mando TV. Tv\'et dukker op på listen. Klik på det.',
      'Bekræft forespørgslen på tv\'et, hvis det spørger (LG, Samsung), eller indtast den viste kode (Google TV, Fire TV).',
      'Klik på knapperne eller skriv en søgning med dit tastatur. Så er du klar.',
    ],
    extra=[
      ('Genveje (Pro)', 'Med Pro bliver pc\'ens tastatur til fjernbetjening: piletaster til at bevæge sig, Enter til OK, Backspace eller Esc til at gå tilbage, plus og minus til lydstyrke, M til lydløs og mellemrumstasten til pause.'),
      ('Mini-fjernbetjening (Pro)', 'Et lille fjernbetjeningsvindue, der bliver liggende over alle andre vinduer. Så ændrer du lydstyrken eller sætter på pause uden at afbryde dit arbejde.'),
      ('Skriv på tv\'et fra pc\'en', 'Skærmtastaturet på et tv er langsomt. I Mando TV skriver du med dit rigtige tastatur, og teksten havner i tv\'ets søgefelt. Denne del er gratis.'),
      ('Flere detaljer', 'Vejledningen trin for trin finder du under [Styr tv\'et fra pc\'en](@pc). Til mobilen læs [Mobilen som fjernbetjening via wifi](@wifi).'),
      ('Gratis og Pro', 'Piletaster, OK, Tilbage, Hjem, lydstyrke, kanaler, taltaster, tastatur, at åbne apps, at skifte indgange og at tænde eller slukke er gratis, uden reklamer og uden abonnement. Mando TV Pro er et valgfrit engangskøb til ekstra ting. På Windows køber du Pro via Microsoft Store.'),
      ('Talekommandoer fra pc\'en (Pro)', 'Med Pro kan du tale til tv\'et via pc\'ens mikrofon. Talen genkendes direkte på pc\'en: Til det skal du ikke have internet og skal ikke indstille noget i Windows. Det, du siger, forlader aldrig pc\'en og bliver ikke gemt. Kun på meget gamle processorer falder appen tilbage på Windows\' taleinput. Til det skal onlinetalegenkendelse være slået til i privatlivsindstillingerne, og dit sprog være tilføjet i Windows.'),
    ],
    marca=None,
    faq=[
      ('Skal fjernbetjening-appen til Windows have Bluetooth eller et kabel?', 'Nej. Den bruger dit hjemmenetværk. Pc og tv skal bare være sluttet til den samme router.'),
      ('Hvilke tv kan jeg styre fra Windows?', 'Samsung-tv med Tizen, LG-tv med webOS, Roku TV og afspillere, Google TV og Android TV samt Fire TV.'),
      ('Kan jeg se tv-billedet på pc\'en eller høre det i pc\'ens højttalere?', 'Nej. Mando TV er kun en fjernbetjening. Det dublerer eller streamer ikke tv-billedet til computeren.'),
      ('Hvorfor virker talen ikke på min Windows-pc?', 'Stemmestyring er en Pro-funktion. Tjek altså, at Pro er aktivt, og at pc\'ens mikrofon virker. På de fleste pc\'er genkendes talen direkte på pc\'en, uden internet. Kun på meget gamle processorer bruger appen Windows\' taleinput: Slå så onlinetalegenkendelse til i Windows\' privatlivsindstillinger og tilføj dit sprog i sprogindstillingerne.'),
    ]),
  dict(clave='iphone', corto='Fjernbetjening-app til iPhone', fecha='2026-11-23',
    titulo='Fjernbetjening-app til iPhone: Samsung, LG, Roku, Google TV',
    desc='Brug din iPhone som fjernbetjening til Samsung, LG, Roku, Google TV og Fire TV via wifi. Gratis i App Store, uden konto og uden reklamer.',
    h1='Fjernbetjening-app til iPhone: én til alle tv',
    intro='Mando TV gør din iPhone eller iPad til fjernbetjening til Samsung, LG, Roku, Google TV eller Android TV samt Fire TV, via dit wifi derhjemme. Appen er gratis i App Store, uden konto og uden reklamer. Den kører også på Android og Windows.',
    pasos=[
      'Hent Mando TV gratis fra App Store.',
      'Forbind din iPhone og tv\'et til det samme wifi.',
      'Åbn Mando TV og tryk på Tillad, når iOS spørger om adgang til det lokale netværk. Appen har brug for det for at finde tv\'et.',
      'Tryk på dit tv på listen. Bekræft forespørgslen på tv\'et, hvis det spørger (LG og Samsung), eller indtast den kode, tv\'et viser (Google TV eller Fire TV).',
      'Brug knapperne, lydstyrken og tastaturet. Du er forbundet.',
    ],
    extra=[
      ('Virker med disse tv', 'LG webOS, Samsung Tizen (årgang 2016 og nyere), Roku TV og Roku-afspillere, Google TV og Android TV samt Fire TV. Siderne om mærkerne er [Samsung](@samsung), [LG](@lg), [Roku](@roku) og [Android TV](@android).'),
      ('Hvorfor den spørger om lokalt netværk', 'iPhone blokerer apps\' adgang til enheder i dit hjemmenetværk, medmindre du tillader det. Dukker tv\'et ikke op på listen, så åbn Indstillinger > Mando TV og aktivér "Lokalt netværk". Appen kommunikerer kun med dit tv inde i dit hjemmenetværk.'),
      ('Hvorfor Mando TV og ikke producentens app', 'Hvert tv-mærke har sin egen app og vil have sin egen opsætning eller sin egen konto. Mando TV er én app til alle, uden konto.'),
      ('Gratis og Pro på iPhone', 'Piletaster, OK, Tilbage, Hjem, lydstyrke, kanaler, taltaster, tastatur, at åbne apps, at skifte indgange og at tænde eller slukke er gratis, uden reklamer og uden abonnement. Mando TV Pro er et valgfrit engangskøb til ekstra ting, direkte i appen.'),
    ],
    marca=None,
    faq=[
      ('Er Mando TV gratis på iPhone?', 'Downloadet er gratis, uden reklamer. Den grundlæggende fjernbetjening er gratis, ligesom at åbne apps og skifte indgange. Ekstra ting hører til Mando TV Pro, et valgfrit engangskøb.'),
      ('Virker det på iPad?', 'Ja. Den samme app kører på iPhone og iPad.'),
      ('Skal en fjernbetjening-app til iPhone have Bluetooth eller en infrarød sender?', 'Ikke på iPhone. iPhone har ingen infrarød sender, derfor findes infrarød styring ikke dér, og Bluetooth-muligheden findes kun til Android 9 eller nyere, ikke til iPhone. På iPhone styrer Mando TV smart-tv samt Apple TV (beta) via dit wifi derhjemme.'),
    ]),
  dict(clave='firetv', corto='Fire TV-fjernbetjening', fecha='2026-11-23',
    titulo='Fire TV-fjernbetjening-app til mobil og pc',
    desc='Fire TV-fjernbetjening på mobilen: Styr Fire TV Stick, Fire TV Cube eller et tv med Fire TV via wifi, med 4-cifret pinkode. Uden Amazon-app.',
    h1='Fire TV-fjernbetjening til din mobil eller pc',
    intro='Hvis Fire TV-fjernbetjeningen er væk, eller batterierne er flade, styrer Mando TV en Fire TV Stick, en Fire TV Cube eller et tv med indbygget Fire TV via wifi. Parringen sker med en 4-cifret pinkode. Fire TV er nyt i Mando TV, så opdater først appen.',
    pasos=[
      'Opdater Mando TV til den nyeste version fra App Store, Microsoft Store eller Google Play.',
      'Tænd Fire TV og forbind din mobil til det samme wifi.',
      'Åbn Mando TV. Dit Fire TV dukker op på listen. Tryk på det.',
      'På tv\'ets skærm vises en 4-cifret pinkode. Indtast den i Mando TV. Det gør du kun én gang.',
      'Brug piletasterne, OK, Tilbage, Hjem, afspilningsknapperne og tastaturet til søgninger.',
    ],
    extra=[
      ('Understøttede Fire TV-enheder', 'Fire TV Stick, Fire TV Stick 4K, Fire TV Cube og tv med indbygget Fire TV. Understøttelsen er ny, og vi har indtil videre kun kunnet teste få rigtige enheder. Virker noget ikke som forventet, så skriv til os din model via hjælpesiden.'),
      ('Tænd Fire TV', 'Mando TV tænder ikke et Fire TV via netværket. Tænd tv\'et med tænd-knappen på apparatet: En isat Fire TV Stick eller Cube vågner som regel via HDMI-CEC, og på et tv med indbygget Fire TV er tv\'et selve Fire TV. Bagefter styrer du det fra mobilen.'),
      ('Hvis dit Fire TV ikke dukker op', 'Sørg for, at begge enheder er på det samme wifi, og at Fire TV er vågent. Tillad på en iPhone "Lokalt netværk" til Mando TV i indstillingerne. Se [din mobil finder ikke tv\'et](@not-found).'),
      ('Slet ingen fjernbetjening?', 'Fire TV skal vise pinkoden på skærmen, så tv og Fire TV skal være tændt og vise et billede. Står tv\'et på en forkert indgang, så skift den med knapperne på tv\'et. Se [Skift indgang uden fjernbetjening](@hdmi).'),
      ('Gratis og Pro', 'Piletaster, OK, Tilbage, Hjem, lydstyrke, kanaler, tal, tastatur, at åbne apps, at skifte indgange og tænd/sluk er gratis, uden reklamer og uden abonnement. Mando TV Pro er et valgfrit engangskøb til ekstra ting.'),
    ],
    marca=None,
    faq=[
      ('Skal jeg have Amazon Fire TV-appen?', 'Nej. Mando TV forbinder via dit wifi med Fire TV ved hjælp af en pinkode. Du skal ikke have en Amazon-konto på mobilen.'),
      ('Virker det med tv med Fire TV og med Fire TV Sticks?', 'Ja, det er netop det, det er lavet til. Understøttelsen er ny, hold appen opdateret og fortæl os om modeller, der ikke virker som forventet.'),
      ('Hvorfor skal jeg bruge en pinkode?', 'Fire TV viser en 4-cifret pinkode for at bevise, at du sidder foran tv\'et. Ingen kan parre uden at se skærmen.'),
    ]),
  dict(clave='firetv-lost', corto='Fire TV-fjernbetjening væk', fecha='2026-11-23',
    titulo='Fire TV-fjernbetjening væk? Sådan hjælper din mobil',
    desc='Fjernbetjeningen til Fire TV Stick væk? Styr den via wifi med mobilen, parret med en 4-cifret pinkode. Tips til nyt wifi og HDMI-CEC.',
    h1='Fire TV-fjernbetjening væk: Sådan bruger du mobilen',
    intro='Hvis fjernbetjeningen til din Fire TV Stick, Fire TV Cube eller dit smart-tv med Fire TV er væk eller ikke virker mere, overtager din mobil styringen, så længe Fire TV stadig er forbundet til dit wifi. Parringen sker med en 4-cifret pinkode på skærmen, så du aldrig skal bruge den gamle fjernbetjening til det.',
    pasos=[
      'Tænd tv\'et med knappen på apparatet. En isat Fire TV Stick eller Cube vågner som regel med; med aktiveret HDMI-CEC skifter tv\'et ofte automatisk til dens indgang.',
      'Viser tv\'et en anden indgang, så skift den med indgangs- eller kildeknappen på tv\'et. Se [Skift indgang uden fjernbetjening](@hdmi).',
      'Forbind din mobil til det samme wifi som Fire TV.',
      'Hent Mando TV og åbn appen. Dit Fire TV dukker op på listen. Tryk på det.',
      'Tv\'et viser en 4-cifret pinkode. Indtast den i Mando TV. Det gør du kun én gang.',
      'Brug piletasterne, OK, Tilbage, Hjem, lydstyrke, afspilningsknapperne og tastaturet på din mobil.',
    ],
    extra=[
      ('Prøv først tv\'ets fjernbetjening (HDMI-CEC)', 'Mange tv-fjernbetjeninger kan styre en Fire TV Stick via HDMI-CEC. Kan du se Fire TV-fladen, så tryk på pilene og OK på tv\'ets fjernbetjening. Sker der ingenting, så aktivér CEC i tv\'ets indstillinger (Anynet+ hos Samsung, SIMPLINK hos LG, BRAVIA Sync hos Sony) og på Fire TV HDMI-CEC-enhedsstyring i skærmindstillingerne ("Display & Sounds").'),
      ('Hvis du har skiftet wifi', 'Uden fjernbetjening kan du ikke indtaste den nye wifi-adgangskode på Fire TV, men der er en udvej: Opret på en anden mobil et hotspot med præcis samme navn og adgangskode som dit gamle wifi. Fire TV forbinder automatisk til det. Forbind mobilen med Mando TV til dette hotspot, par den med pinkoden, gå så på Fire TV til Indstillinger > Netværk og vælg dit nye wifi. Forbind til sidst også din mobil til det nye wifi.'),
      ('Par en ny fjernbetjening', 'De fleste nye Fire TV-fjernbetjeninger parres ved, at du holder Hjem-knappen inde i cirka 10 sekunder tæt på Fire TV. Virker det ikke, så åbn Indstillinger > Controllere og Bluetooth-enheder > Amazon Fire TV-fjernbetjeninger > Tilføj ny fjernbetjening. Denne menu når du også fra din mobil med Mando TV.'),
      ('Fire TV indbygget i tv\'et', 'På tv med indbygget Fire TV virker de samme trin, da tv\'et selv er Fire TV.'),
      ('Før du begynder', 'Fire TV-understøttelsen er ny i Mando TV. Opdater først appen. Reagerer din model ikke som forventet, så skriv til os via [hjælpesiden](@soporte) og nævn modellen.'),
      ('Gratis og Pro', 'Fjernbetjeningen kan du hente og bruge gratis, uden reklamer og uden abonnement. Mando TV Pro er et valgfrit engangskøb til ekstra ting.'),
    ],
    marca=('firetv', 'Fire TV-fjernbetjening'),
    faq=[
      ('Kan jeg styre en Fire TV Stick med mobilen uden fjernbetjeningen?', 'Ja, så længe Fire TV er tændt og forbundet til dit wifi. Mando TV parrer med den 4-cifrede pinkode på tv\'et, så du behøver ikke den gamle fjernbetjening.'),
      ('Virker det, hvis Fire TV er på et nyt wifi?', 'Ikke direkte, da mobil og Fire TV skal være på det samme netværk. Få først Fire TV online igen med hotspot-tricket på denne side.'),
      ('Skal jeg have Amazon Fire TV-appen eller en Amazon-konto?', 'Nej. Mando TV forbinder via dit hjemmenetværk med pinkoden og kræver ingen egen konto.'),
    ]),
  dict(clave='turn-on', corto='Tænd tv uden fjernbetjening', fecha='2026-11-23',
    titulo='Tænd tv uden fjernbetjening (alle mærker)',
    desc='Tænd tv uden fjernbetjening: Hvor knappen sidder på Samsung, LG, TCL, Hisense og Sony. Plus HDMI-CEC og mobiltricks.',
    h1='Sådan tænder du et tv uden fjernbetjening',
    intro='Næsten alle tv har stadig en fysisk tænd/sluk-knap. Den er bare godt gemt. Her kan du se, hvor den sidder på hvert mærke, plus to måder at slippe for at lede næste gang: HDMI-CEC fra en konsol eller en streamingenhed og at tænde tv\'et fra din mobil via wifi.',
    pasos=[
      'Kig under midten af skærmen, lige bag mærkelogoet. Mange tv har dér en lille enkelt knap eller en joystick, der peger nedad.',
      'Er den ikke dér, så føl dig frem på tv\'ets bagside nær de nederste hjørner, derefter på venstre og højre kant.',
      'Tryk på knappen én gang. På mange tv med kun én knap åbner et kort tryk, mens tv\'et kører, en lille menu til indgange og lydstyrke, og et langt tryk slukker det.',
      'Stadig ingenting? Tjek strømkablet i begge ender og prøv en anden stikkontakt. Lyser standby-lampen ikke, får tv\'et ikke strøm.',
      'Så snart tv\'et er tændt, så sæt det op, så du ikke mere skal bruge knappen: Aktivér HDMI-CEC og tænd via netværket, begge dele forklaret længere nede.',
    ],
    extra=[
      ('Hvor tænd/sluk-knappen sidder, pr. mærke', 'Samsung: en styreknap eller en joystick under midten af skærmen eller på bagsiden ved et nederste hjørne. LG: en joystick-knap under LG-logoet på de fleste modeller. TCL og Hisense: som regel en lille knap under midten af skærmen eller på bagsiden nær et nederste hjørne. Sony: på bagsiden eller på en sidekant, nederst tæt ved kanten. Placeringerne ændrer sig efter model. Kan du ikke finde den, så søg efter brugsanvisningen med modelnummeret på mærkaten på bagsiden.'),
      ('Tænd tv\'et via en konsol eller en streamingenhed (HDMI-CEC)', 'Med aktiveret HDMI-CEC tænder det også tv\'et og skifter til den rigtige indgang, når du tænder en PlayStation, en Xbox, en Roku-afspiller, en Fire TV Stick eller en Chromecast. Hvert mærke kalder indstillingen noget forskelligt: Anynet+ hos Samsung, SIMPLINK hos LG, BRAVIA Sync hos Sony og CEC hos de fleste andre. Mere i [Tænd tv\'et og skift til konsollens HDMI](@console).'),
      ('Tænd tv\'et fra din mobil', 'Smart-tv kan vækkes via wifi, hvis du tillader det én gang, og så tænder Mando TV dem fra din mobil. På Samsung aktivér "Tænd med mobil" under Indstillinger > Generelt > Netværk > Ekspertindstillinger. På LG aktivér "Tænd tv med mobil" ([trin for trin](@lg-on)). På et Roku TV aktivér "Hurtig start for tv" under Indstillinger > System > Strøm. På Google TV og Android TV led efter Wake on LAN eller "Tænd via netværk", hvis din model har det. Det gør du én gang, mens tv\'et er tændt.'),
      ('Hvis du ikke finder nogen knap', 'Nogle nyere tv gemmer den eneste knap så godt, at det ser ud, som om der ikke er nogen. Led efter en lille bule eller et lyssensorområde under skærmen: Knappen sidder ofte lige ved siden af. Via wifi kræver Mando TV, at tv\'et en gang har været tændt og forbundet. Infrarød er undtagelsen: På en Android-mobil med infrarød sender kan Mando TV tænde et tv, der aldrig er sat op, så længe du peger mobilen mod tv\'et. Infrarød er ny og virker med de mærker, der står i appens kodeliste.'),
      ('Gratis og Pro', 'Fjernbetjeningen kan du hente og bruge gratis, uden reklamer og uden abonnement. Mando TV Pro er et valgfrit engangskøb til ekstra ting.'),
    ],
    marca=None,
    faq=[
      ('Kan jeg tænde et tv med mobilen, hvis jeg aldrig har sat det op?', 'Ikke via wifi. Et slukket tv vågner kun fra netværket, hvis tænd via netværket var aktiveret før. Første gang bruger du knappen på tv\'et. Undtagelsen er en Android-mobil med infrarød sender: Mando TV kan tænde et tv uden opsætning med infrarød, hvis mærket står i kodelisten, eller du vælger "Andet mærke eller jeg ved det ikke".'),
      ('Hvordan tænder jeg et Samsung-tv uden fjernbetjening?', 'Tryk på styreknappen under midten af skærmen eller på bagsiden ved et nederste hjørne. Aktivér derefter "Tænd med mobil", så din mobil kan tænde det næste gang.'),
      ('Hvordan tænder jeg et Roku TV uden fjernbetjening?', 'Brug knappen på tv\'et, som oftest under midten eller på bagsiden. Aktivér derefter "Hurtig start for tv" under Indstillinger > System > Strøm, så Mando TV kan tænde det fra din mobil.'),
      ('Hvorfor tænder mit tv automatisk, når jeg tænder konsollen?', 'Det er HDMI-CEC. Det er praktisk, og du kan slå det fra i tv\'ets indstillinger, hvis du foretrækker det.'),
    ]),
  dict(clave='sony', corto='Sony-fjernbetjening', fecha='2026-11-23',
    titulo='Sony fjernbetjening-app til mobil og pc',
    desc='Mando TV styrer Sony Bravia-tv med Google TV eller Android TV via wifi. Beta-understøttelse af modeller fra 2013 til 2015 uden Android.',
    h1='Sådan styrer du dit Sony-tv med mobilen',
    intro='Nyere Sony Bravia smart-tv bruger Google TV, ældre modeller fra 2015 Android TV. Mando TV styrer begge via dit wifi fra iPhone, Android-mobil eller Windows-pc. Appen erstatter den originale fjernbetjening, hvis den er væk, eller batterierne er flade.',
    pasos=[
      'Tjek, at dit Sony-tv viser startskærmen fra Google TV eller Android TV. Det gælder de fleste Sony Bravia smart-tv fra årgang 2015.',
      'Forbind din mobil og tv\'et til det samme wifi.',
      'Åbn Mando TV og tryk på dit Sony-tv på listen.',
      'Indtast koden på 6 tegn, som tv\'et viser på skærmen (kun første gang). Til det skal du ikke bruge en fjernbetjening.',
      'Brug piletasterne, OK, Tilbage, Hjem, lydstyrke og tastaturet.',
    ],
    extra=[
      ('Tænd et Sony-tv fra mobilen', 'Sony-modeller med Google TV eller Android TV kan vækkes via netværket, hvis "Remote start" er aktiveret. Muligheden finder du som regel under Indstillinger > Netværk og internet > Remote start (stien kan afvige lidt efter model). Tryk så i Mando TV på tv\'et, mens det er slukket, og appen tænder det.'),
      ('Hvor tænd/sluk-knappen sidder på et Sony', 'På de fleste Bravia-tv sidder den på bagsiden, nær det nederste venstre eller højre hjørne, eller på en sidekant. Et kort tryk tænder tv\'et. Mere finder du i [Tænd tv uden fjernbetjening](@turn-on).'),
      ('Ældre Sony-tv', 'Sony Bravia-tv fra 2013 til 2015, der ikke bruger Android, understøttes i Mando TV i beta. Det er nyt og kan stadig have skæve kanter. Tv\'et viser en 4-cifret pinkode, som du skal indtaste i appen. Andre Sony-tv uden Google TV eller Android TV understøttes i øjeblikket ikke.'),
      ('Gratis og Pro', 'Fjernbetjeningen kan du hente og bruge gratis, uden reklamer og uden abonnement. Mando TV Pro er et valgfrit engangskøb til ekstra ting.'),
    ],
    marca='android',
    faq=[
      ('Virker Mando TV med Sony Bravia-tv?', 'Ja, med Sony-tv, der bruger Google TV eller Android TV. Det omfatter de fleste Sony smart-tv fra årgang 2015.'),
      ('Skal jeg have en Sony-app eller en Google-konto?', 'Nej. Mando TV parrer med koden på tv-skærmen og kræver ingen konto.'),
      ('Virker det med ældre Sony Bravia-tv uden Android?', 'Ja, i beta, på Bravia-modeller fra 2013 til 2015 uden Android. Parringen sker med en 4-cifret pinkode, der vises på tv\'et.'),
      ('Kan jeg skrive fra mobilen på mit Sony-tv?', 'Ja. Tastaturet er gratis og virker i YouTube, Netflix og tv\'ets søgning.'),
    ]),
  dict(clave='tcl', corto='TCL-fjernbetjening', fecha='2026-11-23',
    titulo='TCL fjernbetjening-app til mobil og pc',
    desc='TCL-fjernbetjening væk? De fleste TCL-tv bruger Roku TV eller Google TV. Mando TV styrer begge via wifi, uden konto og reklamer.',
    h1='Sådan styrer du dit TCL-tv med mobilen',
    intro='TCL bygger tv\'et, men softwaren er Roku TV eller Google TV (på ældre modeller Android TV). Mando TV styrer begge systemer og virker som fjernbetjening til dit TCL-tv via wifi. Gratis, uden konto og reklamer.',
    pasos=[
      'Find ud af, hvilket system dit TCL bruger. Viser startskærmen et enkelt gitter af kanalfelter, er det Roku TV. Ligner den Google TV eller Android TV med rækker fulde af anbefalinger, er det Google TV.',
      'Forbind din mobil og TCL-tv\'et til det samme wifi.',
      'Åbn Mando TV. TCL\'et dukker op på listen af sig selv. Tryk på det.',
      'På et TCL med Roku TV skal du ikke gøre mere. På et TCL med Google TV indtaster du koden på 6 tegn, som tv\'et viser på skærmen (kun første gang).',
      'Brug pilene, OK, Tilbage, Hjem, lydstyrke og tastatur. Tænd tv\'et fra appen, hvis du har aktiveret tænd via netværket (se nedenfor).',
    ],
    extra=[
      ('Tænd et TCL-tv fra mobilen', 'På TCL Roku TV aktivér "Hurtig start for tv" under Indstillinger > System > Strøm. På TCL Google TV led efter en mulighed for Wake on LAN, "Tænd via netværk" eller fjernstart i netværks- eller strømindstillingerne. Nogle modeller har ikke dette. Tænd i så fald tv\'et med den fysiske tænd/sluk-knap, som oftest sidder nederst på midten eller bagpå.'),
      ('Hvis dit TCL ikke dukker op', 'Tjek, at mobil og tv er på det samme wifi. Routere med adskilte 2,4 GHz- og 5 GHz-net kan skjule enheder for hinanden. Tillad på iPhone "Lokalt netværk" til Mando TV i indstillingerne. Du kan også tilføje tv\'et ved at indtaste dets IP-adresse. Læs [Din mobil finder ikke tv\'et](@not-found).'),
      ('Mere om dit TCL', 'Til TCL med Roku TV se [Roku fjernbetjening-app](@roku), til TCL med Google TV eller Android TV [Android TV fjernbetjening-app](@android).'),
      ('Gratis og Pro', 'Piletaster, OK, Tilbage, Hjem, lydstyrke, kanaler, tal, tastatur, at åbne apps, at skifte indgange og tænd/sluk er gratis, uden reklamer og abonnement. Mando TV Pro er et valgfrit engangskøb til ekstra ting.'),
    ],
    marca=None,
    faq=[
      ('Virker Mando TV med ethvert TCL-tv?', 'Det virker med TCL-tv med Roku TV, Google TV eller Android TV, altså de fleste TCL smart-tv. Et TCL, der ikke er et smart-tv, kan ikke styres via wifi.'),
      ('Skal jeg have TCL-appen eller en TCL-konto?', 'Nej. Mando TV forbinder direkte via dit wifi derhjemme og kræver ingen konto.'),
      ('Mit TCL beder om en kode. Hvor er den?', 'TCL-modeller med Google TV og Android TV viser en kode på 6 tegn på skærmen. Indtast den præcis sådan i Mando TV. Et TCL med Roku TV spørger ikke efter en kode.'),
    ]),
  dict(clave='hisense', corto='Hisense-fjernbetjening', fecha='2026-11-23',
    titulo='Hisense fjernbetjening-app: Hvad virker på mobilen',
    desc='Hisense-fjernbetjening med Mando TV: Styring til VIDAA, Roku TV, Google TV og Fire TV via wifi. Ærligt overblik over, hvad der virker.',
    h1='Hisense fjernbetjening-app: hvad virker, og hvad virker ikke',
    intro='Hisense-tv er ikke alle ens indeni. Afhængigt af modellen bruger de Hisenses eget VIDAA-system, Roku TV, Google TV eller Fire TV. Mando TV virker som fjernbetjening til Hisense på alle fire systemer, med en undtagelse på nogle nyere VIDAA-modeller. Her kan du se, hvordan du finder ud af, hvilket system du har, og hvad du kan forvente.',
    pasos=[
      'Tjek, hvilket system dit Hisense bruger. VIDAA er Hisenses egen overflade. Roku TV viser et gitter af kanalfelter. Google TV viser rækker med anbefalinger. Fire TV viser Fire TV-startskærmen med Amazon-rækker.',
      'Forbind din mobil og Hisense-tv\'et til det samme wifi.',
      'Åbn Mando TV. Tv\'et dukker op på listen af sig selv. Tryk på det.',
      'VIDAA- og Fire TV-modeller viser måske en pinkode med fire cifre; Google TV viser en kode med seks tegn. Indtast den i appen. Roku TV spørger ikke om noget. Det gør du kun én gang.',
      'Brug pilene, OK, Tilbage, Hjem, lydstyrke og tastatur fra din mobil.',
    ],
    extra=[
      ('Hisense med Roku TV eller Google TV', 'Disse virker helt som ethvert andet Roku- eller Google TV-tv. Detaljer på siderne [Roku fjernbetjening-app](@roku) og [Android TV fjernbetjening-app](@android).'),
      ('Hisense med Fire TV', 'Understøttelsen af Fire TV er ny i Mando TV. Opdater appen til den nyeste version fra din butik. Hvordan parringen med pinkode fungerer, står på siden [Fire TV-fjernbetjening-app](@firetv). Virker noget ikke som forventet, så skriv til os via hjælpesiden og nævn din model.'),
      ('Hisense med VIDAA', 'De fleste VIDAA-modeller virker: knapper, lydstyrke, tastatur, apps og indgange. Nogle nyere VIDAA-modeller accepterer kun den officielle Hisense-app. Mando TV opdager det ved forbindelsen og siger det klart i stedet for stiltiende at svigte. I så fald er Hisense-appen til din model, knapperne på tv\'et eller den originale fjernbetjening den rigtige vej.'),
      ('Tænd et Hisense fra mobilen', 'På Hisense Roku TV aktivér "Hurtig start for tv" under Indstillinger > System > Strøm. På Google TV led efter en mulighed for Wake on LAN eller "Tænd via netværk". Findes der ingen, så brug tænd/sluk-knappen på tv\'et.'),
      ('Gratis og Pro', 'Piletaster, OK, Tilbage, Hjem, lydstyrke, kanaler, taltaster, tastatur, at åbne apps, at skifte indgange og at tænde eller slukke er gratis, uden reklamer og uden abonnement. Mando TV Pro er et valgfrit engangskøb til ekstra ting.'),
    ],
    marca=None,
    faq=[
      ('Virker Mando TV med Hisense VIDAA?', 'Ja, med de fleste VIDAA-modeller. Nogle nyere accepterer kun den officielle Hisense-app; Mando TV opdager det og siger det til dig. Hisense-tv med Roku TV, Google TV eller Fire TV understøttes også.'),
      ('Hvordan ved jeg, om mit Hisense er Roku TV, Google TV eller Fire TV?', 'Se på startskærmen. Roku TV har et enkelt gitter af felter og et Roku-logo ved start. Google TV har rækker med anbefalinger. Fire TV har Amazon Fire TV\'s startskærm. Modelnavnet under Indstillinger > Om giver også besked.'),
      ('Skal jeg have en Hisense- eller Google-konto?', 'Nej. Mando TV forbinder direkte via dit wifi derhjemme og har ingen egen konto.'),
    ]),
  dict(clave='philips', corto='Philips-fjernbetjening', fecha='2026-11-23',
    titulo='Philips fjernbetjening-app: Roku TV, Google TV, Android TV',
    desc='Mando TV styrer Philips-tv med Roku TV, Google TV eller Android TV via wifi, fra mobil eller pc. Titan OS understøttes ikke.',
    h1='Styr Philips-tv med mobilen',
    intro='Philips-tv bruger forskellige systemer efter land og årgang: Roku TV i USA, Google TV eller Android TV i mange lande og Titan OS på nogle nyere europæiske modeller. Mando TV styrer modellerne med Roku TV, Google TV og Android TV via wifi.',
    pasos=[
      'Tjek startskærmen. Roku TV viser et gitter af felter. Google TV og Android TV viser rækker af anbefalinger fra Google. Titan OS har sin egen startskærm.',
      'Forbind din mobil og tv\'et til det samme wifi.',
      'Åbn Mando TV og tryk på dit Philips-tv på listen.',
      'Roku TV spørger ikke om noget. Google TV og Android TV viser en kode på 6 tegn: Indtast den én gang i appen.',
      'Brug piletasterne, OK, Tilbage, Hjem, lydstyrke og tastatur.',
    ],
    extra=[
      ('Philips Roku TV', 'Virker som ethvert Roku-tv. For at tænde det fra mobilen aktivér "Hurtig start for tv" under Indstillinger > System > Strøm. Mere på siden [Roku fjernbetjening-app](@roku).'),
      ('Philips med Google TV eller Android TV', 'Omfatter mange Ambilight-modeller. De parres med koden på skærmen. For at tænde dem fra mobilen led i netværks- eller strømindstillingerne efter Wake on LAN eller "Tænd via netværk". På nogle modeller mangler denne mulighed. Mere på siden [Android TV fjernbetjening-app](@android).'),
      ('Ældre Philips-tv uden Android', 'Philips-tv fra 2011 til 2015, der ikke bruger Android, understøttes i Mando TV i beta. Det er nyt og kræver ingen parringskode.'),
      ('Philips med Titan OS', 'Titan OS er et andet system, som Mando TV i dag ikke styrer, og det siger vi hellere klart. Nyere Philips-modeller uden Android er heller ikke dækket.'),
      ('Gratis og Pro', 'Fjernbetjeningen kan du hente og bruge gratis, uden reklamer og uden abonnement. Mando TV Pro er et valgfrit engangskøb til ekstra ting.'),
    ],
    marca=None,
    faq=[
      ('Virker Mando TV med Philips-tv?', 'Med Philips-tv, der bruger Roku TV, Google TV eller Android TV, ja, og i beta med Philips-tv fra 2011 til 2015 uden Android. Modeller med Titan OS understøttes ikke.'),
      ('Styrer Mando TV Ambilight?', 'Mando TV er en fjernbetjening: Den sender knapperne, så du kan nå Ambilight-indstillingerne med pilene og OK. Der findes ingen separate Ambilight-styringer.'),
      ('Skal jeg have en Philips- eller Google-konto?', 'Nej. Mando TV forbinder via dit wifi derhjemme og kræver ingen konto.'),
    ]),
]
OTRAS_GUIAS += [
  ('no-sub', 'En fjernbetjening-app uden abonnement og uden reklamer'),
  ('roku-app-alt', 'Alternativ til Roku-appen: én til alle tv'),
  ('lg-thinq', 'Alternativ til LG ThinQ-appen til dit LG-tv'),
  ('smartthings', 'SmartThings-alternativ til Samsung-tv'),
  ('googletv-alt', 'Alternativ til Google TV-fjernbetjeningen på mobilen'),
  ('windows', 'Fjernbetjening-app til Windows-pc'),
  ('iphone', 'Fjernbetjening-app til iPhone: én til alle tv'),
  ('firetv', 'Fire TV-fjernbetjening til din mobil eller pc'),
  ('firetv-lost', 'Fire TV-fjernbetjening væk: Sådan bruger du mobilen'),
  ('turn-on', 'Sådan tænder du et tv uden fjernbetjening'),
  ('sony', 'Sådan styrer du dit Sony-tv med mobilen'),
  ('tcl', 'Sådan styrer du dit TCL-tv med mobilen'),
  ('hisense', 'Hisense fjernbetjening-app: hvad virker, og hvad virker ikke'),
  ('philips', 'Styr Philips-tv med mobilen'),
]
# <<< guider hentet fra engelsk
