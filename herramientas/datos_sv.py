# Textos i svenska (du) av mandotv.app. Los usa generar_idiomas.py. Escritos para las búsquedas de Suecia.
# Las claves de las páginas (lg, lost-tv, ...) y sus rutas están en idiomas_sitio.py.
# Los nombres de menús de cada marca (LG, Samsung, Roku, Android TV, iPhone) son los mismos que usa la app en sueco
# (lib/l10n/app_sv.arb del proyecto de la app).

UI = dict(
  locale='sv_SE',
  aria_home='Mando TV, startsidan', aria_main='Huvudmeny', nav_que='Funktioner', nav_ayuda='Hjälp', nav_contacto='Kontakt',
  asunto='Hej%20Mando%20TV', inicio='Startsidan', privacidad='Integritet', aria_pie='Sidfot', aria_ruta='Sökväg',
  aria_marcas='Märken och guider', hecho='Utvecklad i Chile',
  aviso='Mando TV är en oberoende app. Den har ingen koppling till och stöds inte av de nämnda tv-tillverkarna, Google, Amazon, Apple eller Roku. Varumärkena tillhör sina ägare och nämns bara för att visa kompatibilitet. Android TV och Google TV är varumärken som tillhör Google LLC. Apple TV är ett varumärke som tillhör Apple Inc.',
  bajar='Ladda ner gratis', descarga='Ladda ner från', anticipada='Tidig åtkomst på',
  apple_aria='Ladda ner Mando TV gratis i App Store', ms_aria='Ladda ner Mando TV gratis i Microsoft Store',
  gp_aria='Tidig åtkomst till Mando TV i Google Play för Android', aria_desc='Ladda ner Mando TV',
  b_como_btn='Så ansluter du', b_tiendas_label='Finns i apparnas butiker',
  b_nota='iPhone, iPad, Mac, Android och Windows. Gratis nedladdning, utan reklam. Pro är ett engångsköp, utan prenumeration.',
  b_compat='Kompatibla tv-apparater', b_otras='Andra märken', b_otras_p='Mando TV styr alla de här märkena med samma app:',
  g_guias='Guider', g_ver='Se stegen', g_pasos='Steg för steg', g_hazlo='Så gör du med Mando TV',
  g_tiendas='Mando TV är en universell fjärrkontroll för din tv. Ladda ner den gratis, utan reklam och utan konto. Pro är ett valfritt engångsköp, utan prenumeration. För iPhone, iPad, Windows och Android:',
  g_nota='Android: gratis tidig åtkomst i Google Play. <a href="{enlace}">Gå med i två steg</a> och hjälp oss nå butiken.',
  g_mas_pagina='Mer information finns på sidan {enlace}.', g_mas_marca='Mer information per märke:',
  g_faq='Vanliga frågor', g_mas='Fler guider', g_todas='Alla guider', g_ayuda='Hjälp och support',
  g_idiomas='Den här guiden på andra språk',
)

# Pie de página y listas de marcas/guías: (clave, texto)
PIE = [
  ('samsung', 'Samsung fjärrkontroll'),
  ('lg', 'LG fjärrkontroll'),
  ('roku', 'Roku fjärrkontroll'),
  ('android', 'Android TV fjärrkontroll'),
  ('guias', 'Alla guider'),
  ('lost-tv', 'Borttappad fjärrkontroll'),
  ('lost-lg', 'Borttappad LG fjärrkontroll'),
  ('lg-on', 'Slå på LG-tv med mobilen'),
  ('hdmi', 'Byt HDMI-ingång utan fjärrkontroll'),
  ('androidtv', 'Android TV utan fjärrkontroll'),
  ('console', 'Slå på tv och spelkonsolens HDMI utan fjärrkontroll'),
  ('samsung-lost', 'Samsung-tv utan fjärrkontroll'),
  ('roku-lost', 'Borttappad Roku fjärrkontroll'),
  ('roku-403', 'Roku-appen fungerar inte'),
  ('androidtv-code', 'Android TV kopplingskod'),
  ('not-found', 'Mobilen hittar inte tv:n'),
  ('wifi', 'Mobilen som fjärrkontroll via wifi'),
  ('pc', 'Styr tv:n med datorn'),
]
NOMBRE_OTRA = {'lg': 'LG fjärrkontrollsapp', 'samsung': 'Samsung fjärrkontrollsapp', 'roku': 'Roku fjärrkontrollsapp',
               'android': 'Android TV och Google TV fjärrkontrollsapp'}
PAGINA_MARCA = {'lg': 'LG fjärrkontrollsapp', 'samsung': 'Samsung fjärrkontrollsapp', 'roku': 'Roku fjärrkontrollsapp',
                'android': 'Android TV fjärrkontrollsapp'}

OTRAS_GUIAS = [
  ('lg-on', 'Slå på LG-tv med mobilen'),
  ('lost-tv', 'Borttappad fjärrkontroll: det här kan du göra'),
  ('lost-lg', 'Borttappad LG fjärrkontroll: så använder du mobilen'),
  ('hdmi', 'Byt HDMI-ingång på tv:n utan fjärrkontroll'),
  ('androidtv', 'Android TV utan fjärrkontroll: så använder du mobilen'),
  ('console', 'Slå på tv:n och byt till spelkonsolens HDMI, utan fjärrkontroll'),
  ('samsung-lost', 'Samsung-tv utan originalfjärrkontroll: så använder du mobilen'),
  ('roku-lost', 'Borttappad Roku fjärrkontroll: så använder du mobilen'),
  ('roku-403', 'Roku-appen fungerar inte: åtgärda fel 403'),
  ('androidtv-code', 'Android TV ber om en kopplingskod: det här gör du'),
  ('not-found', 'Mobilen hittar inte tv:n: det här bör du kontrollera'),
  ('wifi', 'Så använder du mobilen som fjärrkontroll via wifi'),
  ('pc', 'Så styr du tv:n med en Windows-dator'),
]

INDICE = dict(
  titulo='Guider: styr tv:n med mobilen | Mando TV',
  desc='Guider steg för steg: använd mobilen eller datorn som fjärrkontroll, slå på tv:n, byt HDMI och lös problem med Samsung, LG och Roku.',
  h1='Guider: använd mobilen som fjärrkontroll',
  intro='Enkla steg för att ansluta fjärrkontrollen till din Samsung-, LG-, Roku- eller Android TV-tv med Mando TV, slå på tv:n och lösa problem.',
  h2_guias='Alla guider', h2_marcas='Fjärrkontrollsapp per märke',
)

MARCAS = [
  dict(clave='lg', color='#e0457b', corto='LG',
    titulo='LG-tv fjärrkontroll som app i mobilen, gratis | Mando TV',
    desc='Mobilen eller datorn som fjärrkontroll till LG-tv med webOS, via wifi. Knappar, tangentbord, appar, ingångar och påslagning gratis; pekare med Pro.',
    h1='LG-tv fjärrkontroll som app i mobilen',
    intro='Mando TV är en fjärrkontrollsapp för LG-tv: den gör mobilen eller datorn till fjärrkontroll för din LG Smart TV med webOS, via wifi hemma. Det är bra när du har tappat bort fjärrkontrollen, batterierna är slut eller du helt enkelt vill skriva snabbare.',
    compat='LG Smart TV med webOS (de flesta LG Smart TV-modeller sedan 2014). Fungerar med LED-, NanoCell-, QNED- och OLED-tv. Äldre LG Smart TV med NetCast (2011 till 2014, före webOS) stöds nu i betan: de kopplas ihop med den 6-siffriga nyckeln som tv:n visar.',
    h2=dict(funciones='Det här kan du göra med din LG-tv', como='Så ansluter du din LG-tv till Mando TV',
            encender='Slå på LG-tv med mobilen', preguntas='Frågor om LG', guias='Guider för LG'),
    funciones=[
      ('Alla knappar', 'Riktningsknappar, OK, bakåt, hem, volym, kanaler, ljud av och uppspelning.'),
      ('Pekare som med Magic Remote (Pro)', 'Flytta pilen över skärmen med fingret, precis som med LG Magic Remote.'),
      ('Tangentbord', 'Skriv i YouTube, Netflix eller tv:ns webbläsare med mobilens tangentbord.'),
      ('Appar och ingångar', 'Öppna dina appar och byt till HDMI, live-tv, AirPlay eller Screen Share.'),
      ('Ljudutgång (Pro)', 'Växla mellan tv:ns högtalare och din soundbar.'),
      ('Slå på tv:n', 'Om den är avstängd slår Mando TV på den via nätverket och ansluter av sig själv.'),
    ],
    pasos=[
      'Anslut mobilen och tv:n till samma wifi.',
      'Öppna Mando TV: din LG-tv dyker upp i listan av sig själv. Tryck på den.',
      'På tv:n visas en fråga om tillstånd. Godkänn den med din vanliga fjärrkontroll (bara första gången).',
    ],
    encender='Öppna Inställningar på LG-tv:n och leta efter "Slå på tv med mobil" (beroende på modell finns den under Allmänt eller Anslutning). Slå på "Slå på via wifi". Om det finns "Quick Start+", slå på den också. Efter det frågar appen om den ska slå på tv:n när du trycker på den avstängda tv:n i Mando TV, och ansluter av sig själv.',
    faq=[
      ('Behöver jag Magic Remote för att använda Mando TV?', 'Bara första gången, för att godkänna frågan på skärmen. Efter det räcker mobilen.'),
      ('Ersätter Mando TV appen LG ThinQ?', 'För att styra tv:n, ja: du behöver varken LG-konto eller registrera tv:n. Mando TV ansluter direkt via ditt wifi.'),
      ('Kan jag slå på min LG-tv med mobilen?', 'Ja, om du har slagit på "Slå på tv med mobil" i tv:n och har anslutit en gång medan tv:n var på.'),
      ('Fungerar det med äldre LG-tv från tiden före webOS?', 'I betan ja, med LG NetCast Smart TV från 2011 till 2014. De kopplas ihop med den 6-siffriga nyckeln som tv:n visar. Funktionen är ny och kan fortfarande ha kantiga hörn.'),
    ],
    guias=[('lg-on', 'Så slår du på en LG-tv med mobilen'),
           ('lost-lg', 'Borttappad LG fjärrkontroll: så använder du mobilen'),
           ('hdmi', 'Byt HDMI-ingång på tv:n utan fjärrkontroll'),
           ('guias', 'Alla guider för att styra tv:n med mobilen')]),
  dict(clave='samsung', color='#3d7bff', corto='Samsung',
    titulo='Samsung-tv fjärrkontroll som app i mobilen | Mando TV',
    desc='Mobilen eller datorn som fjärrkontroll till Samsung-tv med Tizen, via wifi. Knappar, tangentbord, appar och påslagning gratis; touchpad med Pro. Utan reklam.',
    h1='Samsung-tv fjärrkontroll som app i mobilen',
    intro='Mando TV är en fjärrkontrollsapp för Samsung-tv: den gör mobilen eller datorn till fjärrkontroll för din Samsung Smart TV, via wifi hemma. Du behöver varken Samsung-konto eller registrera tv:n.',
    compat='Samsung Smart TV med Tizen, tillverkade 2016 och senare (serier som Crystal UHD, QLED, Neo QLED, The Frame och OLED).',
    h2=dict(funciones='Det här kan du göra med din Samsung-tv', como='Så ansluter du din Samsung-tv till Mando TV',
            encender='Slå på Samsung-tv med mobilen', preguntas='Frågor om Samsung', guias='Guider för Samsung'),
    funciones=[
      ('Alla knappar', 'Riktningsknappar, OK, bakåt, hem, volym, kanaler, ljud av och källa.'),
      ('Touchpad (Pro)', 'Svep med fingret genom menyerna utan att leta efter pilknapparna.'),
      ('Tangentbord', 'Skriv sökningar och lösenord med mobilens tangentbord.'),
      ('Appar', 'Öppna Netflix, YouTube, Prime Video och dina andra appar med ett tryck.'),
      ('Slå på tv:n', 'Om den är avstängd slår Mando TV på den via nätverket och ansluter av sig själv.'),
      ('Utan konto', 'Anslutningen går direkt via ditt wifi, utan omväg via internet.'),
    ],
    pasos=[
      'Anslut mobilen och tv:n till samma wifi.',
      'Öppna Mando TV: din Samsung-tv dyker upp i listan av sig själv. Tryck på den.',
      'Tv:n frågar om du tillåter anslutningen. Välj "Tillåt" med fjärrkontrollen (bara första gången).',
    ],
    encender='Öppna Inställningar > Allmänt > Nätverk > Expertinställningar på Samsung-tv:n och slå på "Slå på med mobil". Efter det frågar appen om den ska slå på tv:n när du trycker på den avstängda tv:n i Mando TV, och ansluter av sig själv.',
    faq=[
      ('Jag nekade tillståndet av misstag. Vad gör jag?', 'Gå till Inställningar > Allmänt > Hanterare för externa enheter > Enhetsanslutningshanterare på tv:n och sätt Mando TV som tillåten.'),
      ('Ersätter Mando TV SmartThings?', 'För att styra tv:n, ja, och utan Samsung-konto. Mando TV ansluter direkt via ditt wifi.'),
      ('Fungerar det med äldre Samsung-tv?', 'Det fungerar med Samsung-tv med Tizen, tillverkade 2016 och senare. Tidigare modeller använder ett annat system som vi ännu inte stöder.'),
    ],
    guias=[('samsung-lost', 'Samsung-tv utan originalfjärrkontroll: så använder du mobilen'),
           ('hdmi', 'Byt HDMI-ingång på tv:n utan fjärrkontroll'),
           ('guias', 'Alla guider för att styra tv:n med mobilen')]),
  dict(clave='roku', color='#a77bff', corto='Roku',
    titulo='Roku fjärrkontroll som app i mobilen, gratis | Mando TV',
    desc='Mobilen eller datorn som fjärrkontroll till Roku TV och Roku-spelare, via wifi. Knappar, tangentbord, kanaler, ingångar och påslagning gratis.',
    h1='Roku fjärrkontroll som app i mobilen',
    intro='Mando TV är en fjärrkontrollsapp för Roku: den gör mobilen eller datorn till fjärrkontroll för din Roku, via wifi hemma. Den fungerar med Roku TV och med Roku-spelare som sätts i HDMI-porten.',
    compat='Roku TV-apparater (TCL, Hisense, Philips, Sharp, JVC och andra) och Roku-spelare (Express, Streaming Stick, Ultra).',
    h2=dict(funciones='Det här kan du göra med din Roku', como='Så ansluter du din Roku till Mando TV',
            encender='Slå på Roku med mobilen', preguntas='Frågor om Roku', guias='Guider för Roku'),
    funciones=[
      ('Alla knappar', 'Riktningsknappar, OK, bakåt, hem, volym, ljud av, repris och uppspelning.'),
      ('Tangentbord', 'Skriv sökningar i Rokus kanaler med mobilens tangentbord.'),
      ('Kanaler', 'Öppna Netflix, YouTube och dina andra Roku-kanaler med ett tryck.'),
      ('Ingångar', 'På en Roku TV byter du till HDMI, antenn eller AV i appen.'),
      ('Slå på tv:n', 'På Roku TV med snabbstart slår Mando TV på tv:n från mobilen.'),
      ('Utan koppling', 'Roku ber inte om någon kod: tryck på den i listan så är du ansluten.'),
      ('Ring upp fjärrkontrollen', 'Om din Roku-fjärrkontroll har en högtalare, som Roku Voice Remote Pro, får Mando TV den att ringa så att du hittar den. Gratis, Roku måste vara påslagen.'),
    ],
    pasos=[
      'Anslut mobilen och din Roku till samma wifi.',
      'Öppna Mando TV: din Roku dyker upp i listan av sig själv. Tryck på den.',
      'Om anslutningen inte fungerar, gå till Inställningar > System > Avancerade systeminställningar > Styrning via mobilappar på din Roku och sätt nätverksåtkomsten till Standard eller Aktiverad.',
    ],
    encender='På Roku TV slår du på "Snabb tv-start" under Inställningar > System > Ström. Roku-spelare som är anslutna till en annan tv kan inte slås på på det här sättet. Efter det frågar appen om den ska slå på tv:n när du trycker på den avstängda tv:n i Mando TV, och ansluter av sig själv.',
    faq=[
      ('Fungerar det med Roku Express eller Streaming Stick?', 'Ja. Alla Roku-spelare och Roku TV styrs på samma sätt.'),
      ('Mando TV hittar inte min Roku. Vad gör jag?', 'Kontrollera att båda sitter på samma wifi och att "Styrning via mobilappar" inte är avstängt på din Roku. Du kan också lägga till den med dess IP-adress.'),
      ('Behöver jag ett Roku-konto?', 'Nej. Mando TV ansluter direkt via ditt wifi.'),
    ],
    guias=[('roku-403', 'Roku-appen fungerar inte (fel 403)'),
           ('roku-lost', 'Borttappad Roku fjärrkontroll: så använder du mobilen'),
           ('guias', 'Alla guider för att styra tv:n med mobilen')]),
  dict(clave='android', color='#2fbf8f', corto='Android TV och Google TV',
    titulo='Android TV fjärrkontroll som app i mobilen | Mando TV',
    desc='Mobilen eller datorn som fjärrkontroll till Android TV (Sony, TCL, Xiaomi), via wifi. Knappar, tangentbord, appar och påslagning gratis; touchpad med Pro.',
    h1='Android TV fjärrkontroll som app i mobilen',
    intro='Mando TV är en fjärrkontrollsapp för Android TV: den gör mobilen eller datorn till fjärrkontroll för din Android TV- eller Google TV-tv, via wifi hemma. Den fungerar också från iPhone och från Windows.',
    compat='Tv-apparater med Google TV eller Android TV från Sony, Philips, TCL, Hisense, Sharp, Xiaomi, Toshiba, Panasonic, Haier, Skyworth, JVC, Thomson, Motorola, OnePlus, iFFALCON, Kogan, Vu och andra märken, samt Chromecast med Google TV, Google TV Streamer, onn. och Nvidia Shield. En del av de här märkena säljer också modeller med ett annat system: visar din tv startskärmen för Google TV eller har den Google Play Store, styr Mando TV den.',
    h2=dict(funciones='Det här kan du göra med din Android TV', como='Så ansluter du din Android TV till Mando TV',
            encender='Slå på Android TV med mobilen', preguntas='Frågor om Android TV', guias='Guider för Android TV'),
    funciones=[
      ('Alla knappar', 'Riktningsknappar, OK, bakåt, hem, volym, ljud av och uppspelning.'),
      ('Touchpad (Pro)', 'Svep med fingret för att snabbt navigera i menyerna i Google TV.'),
      ('Tangentbord', 'Skriv sökningar och lösenord med mobilens tangentbord.'),
      ('Appar', 'Öppna YouTube, Netflix, Disney+ och dina andra appar med ett tryck.'),
      ('Slå på tv:n', 'På modeller som kan väckas via nätverket slår Mando TV på tv:n och ansluter av sig själv.'),
      ('iPhone, Android och dator', 'Det fungerar likadant på alla mobiler och datorer.'),
    ],
    pasos=[
      'Anslut mobilen och tv:n till samma wifi.',
      'Öppna Mando TV: din Android TV dyker upp i listan av sig själv. Tryck på den.',
      'Tv:n visar en kod med 6 tecken. Skriv in den i Mando TV (bara första gången).',
    ],
    encender='Det beror på tillverkaren. Leta i nätverks- eller energiinställningarna efter "Wake on LAN", "Nätverksstandby" eller "Väck via nätverk". En del modeller har inte det alternativet. Efter det frågar appen om den ska slå på tv:n när du trycker på den avstängda tv:n i Mando TV, och ansluter av sig själv.',
    faq=[
      ('Fungerar det med Chromecast med Google TV?', 'Ja, kopplingen sker med koden på 6 tecken som visas på skärmen.'),
      ('Vad skiljer det från appen Google TV?', 'Mando TV behöver inget Google-konto, fungerar också i Windows och styr tv från LG, Samsung och Roku med samma app.'),
      ('Koden visas inte på skärmen. Vad gör jag?', 'Stäng Mando TV, öppna appen igen och tryck på tv:n en gång till. Kontrollera att tv:n inte ligger i ett djupt energisparläge.'),
    ],
    guias=[('androidtv-code', 'Android TV ber om en kopplingskod: det här gör du'),
           ('androidtv', 'Android TV utan fjärrkontroll: så använder du mobilen'),
           ('guias', 'Alla guider för att styra tv:n med mobilen')]),
]

GUIAS = [
  dict(clave='lost-tv', corto='Borttappad fjärrkontroll',
    titulo='Borttappad fjärrkontroll? Styr tv:n med mobilen',
    desc='Har du tappat bort fjärrkontrollen? Slå på tv:n med knappen på apparaten och använd mobilen som fjärrkontroll. Steg för LG, Samsung, Roku, Android TV. Gratis.',
    h1='Borttappad fjärrkontroll? Det här kan du göra nu',
    intro='En borttappad fjärrkontroll händer i alla hem: den är borta precis när du vill titta på något. Den goda nyheten är att mobilen kan ersätta fjärrkontrollen via wifi hemma. Här ser du vad du kan göra, steg för steg.',
    pasos=[
      'Slå på tv:n med knappen på själva apparaten. Den sitter nästan alltid nere i mitten eller på baksidan nära ett hörn. Ibland är det en enda knapp, ibland en liten joystick.',
      'Anslut mobilen till samma wifi som tv:n.',
      'Ladda ner Mando TV, som är gratis och inte kräver något konto, och öppna appen. Din tv dyker upp i listan av sig själv. Tryck på den.',
      'Godkänn anslutningen för ditt märke. På LG och Samsung visar tv:n en fråga: godkänn den med knappen eller joysticken på själva tv:n. På Android TV och Google TV skriver du in en kod med 6 tecken som visas på skärmen. Roku frågar inte efter något.',
      'Klart. Pilar, OK, bakåt, hem, volym, kanaler och tangentbord är gratis.',
      'Till nästa gång: slå på påslagning via nätverket i tv:ns inställningar (guiden för ditt märke hittar du nedan). Då kan du slå på tv:n från mobilen utan att röra den.',
    ],
    extra=[
      ('Välj guiden för ditt märke', 'LG: [Borttappad LG fjärrkontroll](@lost-lg). Android TV och Google TV: [Android TV utan fjärrkontroll](@androidtv). Samsung: [Samsung-tv utan fjärrkontroll](@samsung-lost). Roku: [Borttappad Roku fjärrkontroll](@roku-lost).'),
      ('Om tv:n inte går att slå på med knappen', 'Innan du letar efter en annan fjärrkontroll, kontrollera att sladden sitter fast och att vägguttaget har ström. Om knappen på tv:n inte gör något är det tv:n som har problemet och inte fjärrkontrollen.'),
      ('Om fjärrkontrollen helt enkelt har slutat fungera', 'Prova med nya batterier. Du kan kontrollera om den fortfarande skickar en signal genom att rikta den mot mobilkameran och trycka på en knapp: på många mobiler ser du då ett lila ljus på skärmen. Ser du ljuset och tv:n inte reagerar kan sensorn på tv:n vara skymd.'),
      ('Om du har bytt router och tv:n har tappat wifi', 'Utan fjärrkontroll är det svårare att ansluta tv:n till det nya nätverket. Enklast är att koppla tv:n till routern med en nätverkskabel. Du kan också skapa ett wifi med samma namn och lösenord som tidigare: tv:n ansluter oftast till det av sig själv.'),
      ('Vad som är gratis och vad som är Pro', 'Att slå på och stänga av tv:n, pilar, OK, volym, kanaler, siffertangenter, tangentbord, att öppna appar och att byta ingång är gratis. Touchpad, röst och rutiner ingår i Mando TV Pro, ett engångsköp utan prenumeration.'),
    ],
    marca=None,
    faq=[
      ('Kan jag slå på tv:n med mobilen om jag aldrig har anslutit den?', 'Första gången slår du på den med knappen på tv:n. När du har anslutit mobilen och slagit på påslagning via nätverket i tv:ns inställningar kan du slå på den från appen.'),
      ('Måste jag köpa en ny fjärrkontroll?', 'Inte nödvändigtvis. Med Mando TV får du knappar, volym, tangentbord och påslagning gratis. Vill du ändå hellre ha en riktig fjärrkontroll, sök efter den exakta modellen på din tv.'),
      ('Fungerar det om tv:n inte har wifi?', 'Nej. Mobilen och tv:n måste sitta på samma wifi. En tv som inte är en smart-tv går inte att styra med Mando TV.'),
    ]),
  dict(clave='lost-lg', corto='Borttappad LG fjärrkontroll',
    titulo='Borttappad LG fjärrkontroll? Använd mobilen',
    desc='Ingen LG fjärrkontroll? Slå på tv:n med knappen på apparaten, godkänn frågan och använd mobilen via wifi. Utan LG-konto, utan reklam.',
    h1='Borttappad LG fjärrkontroll? Så använder du mobilen',
    intro='Om du har tappat bort din LG fjärrkontroll eller Magic Remote har slutat fungera ersätter mobilen den via wifi. Det fungerar på LG-tv med webOS, alltså på nästan alla LG Smart TV sedan 2014. Du behöver varken LG-konto eller appen ThinQ.',
    pasos=[
      'Slå på tv:n med knappen nere under LG-loggan eller med knappen på baksidan. På många modeller är den en joystick: tryck på den för att öppna menyn och flytta den för att välja.',
      'Anslut mobilen till samma wifi som tv:n.',
      'Öppna Mando TV och tryck på din LG-tv i listan.',
      'Tv:n visar en fråga om tillstånd. Godkänn den med joysticken eller knappen på tv:n. Om du redan har anslutit den här mobilen frågar den inte igen.',
      'Klart. Pilar, OK, bakåt, hem, volym, kanaler och tangentbord är gratis. Pekaren är en Pro-funktion.',
      'När appen är ansluten öppnar du inställningarna med pilarna och OK och slår på "Slå på tv med mobil". Guiden [Slå på LG-tv med mobilen](@lg-on) visar var du hittar alternativet.',
    ],
    extra=[
      ('Om tv:n inte visar frågan', 'Kanske är tillståndet redan sparat, eller så sitter mobilen på ett annat nätverk. Kontrollera att båda sitter på samma wifi och att VPN är avstängt. Om tv:n inte dyker upp i listan hjälper [Mobilen hittar inte tv:n](@not-found) dig vidare.'),
      ('Om tv:n har tappat sitt wifi', 'Koppla tv:n till routern med en nätverkskabel, så använder den kabeln av sig själv. Eller skapa ett wifi med samma namn och lösenord som tidigare, eftersom tv:n oftast ansluter till det av sig själv.'),
      ('Om tv:n har hamnat på en annan ingång', 'Tryck på Ingångar på mobilen och välj HDMI-porten. Mer om det står i [Byt HDMI-ingång på tv:n utan fjärrkontroll](@hdmi).'),
    ],
    marca='lg',
    faq=[
      ('Behöver jag Magic Remote för att använda Mando TV?', 'Du behöver något bara första gången, för att godkänna frågan, och då räcker knappen eller joysticken på själva tv:n. Efter det använder du bara mobilen.'),
      ('Behöver jag appen LG ThinQ?', 'Nej. Mando TV ansluter direkt via ditt wifi och kräver inget LG-konto.'),
      ('Kan jag stänga av och slå på min LG-tv med mobilen?', 'Stänga av, ja. För att slå på måste du ha slagit på "Slå på tv med mobil" i tv:n och ha anslutit en gång medan tv:n var på.'),
    ]),
  dict(clave='hdmi', corto='Byt HDMI utan fjärrkontroll',
    titulo='Byt HDMI-ingång utan fjärrkontroll (Samsung, LG, Roku)',
    desc='Byt HDMI-ingång utan fjärrkontroll på Samsung, LG eller Roku: med knappen på tv:n eller med mobilen. Gratis att börja med, utan reklam.',
    h1='Så byter du HDMI-ingång på tv:n utan fjärrkontroll',
    intro='Spelkonsolen eller streamingspelaren är redo, men tv:n står på en annan ingång och fjärrkontrollen är ingenstans att hitta. För att byta HDMI-ingång utan fjärrkontroll har du två möjligheter: knappen på själva tv:n eller mobilen. Här är stegen för Samsung, LG och Roku.',
    pasos=[
      'Prova först det enklaste: slå på konsolen eller spelaren. Om HDMI-CEC är påslaget på tv:n (på Samsung heter det Anynet+, på LG SIMPLINK) byter tv:n av sig själv till den ingången.',
      'Byter den inte, använd knappen på själva tv:n, nere i mitten eller på baksidan. På många Samsung- och LG-tv är den en joystick och öppnar en meny med Källa eller Ingångar.',
      'Välj ingången i den menyn: HDMI 1, HDMI 2 och så vidare. Numret är porten där kabeln sitter.',
      'Vill du hellre använda mobilen, anslut den till samma wifi, öppna Mando TV och tryck på din tv.',
      'På LG och Roku trycker du på Ingångar och väljer HDMI-porten. På Samsung skickar Ingångar knappen Källa till tv:n, och du väljer med pilarna och OK.',
      'Du kan också gå till ingångarna med pilarna och OK från tv:ns startskärm. Beroende på märke och årsmodell heter de Källa, Anslutna enheter eller Ingångar. På en Roku TV är det HDMI-rutorna på startskärmen.',
    ],
    extra=[
      ('Samsung', 'Om menyn från knappen på tv:n saknar punkten Källa, öppna startskärmens meny med mobilen och leta längst till vänster efter Källa eller Anslutna enheter. Du styr den med pilarna och OK i Mando TV, som är gratis.'),
      ('LG', 'Tryck på joysticken på tv:n och leta efter Ingångar. Med mobilen kan du i Mando TV också öppna listan över ingångar och trycka på den du vill ha.'),
      ('Roku TV', 'På startskärmen finns en ruta för varje ingång, till exempel HDMI 1 eller HDMI 2. Flytta dig med pilarna och öppna med OK, gratis.'),
      ('Om det är en tv med Android TV eller Google TV', 'I Mando TV finns listan över ingångar för Android TV ännu inte. Använd ingångsknappen på själva tv:n eller nå ingångarna med pilarna och OK från startskärmen. Om du inte har någon fjärrkontroll och vill ansluta, läs [Android TV utan fjärrkontroll](@androidtv).'),
      ('Mer hjälp', 'Om tv:n inte slås på alls eller du inte vet var du ska börja, läs [Borttappad fjärrkontroll](@lost-tv). För spel på konsolen innehåller guiden [Slå på tv:n och byt till spelkonsolens HDMI, utan fjärrkontroll](@console) HDMI-CEC-tricket.'),
    ],
    marca=None,
    faq=[
      ('Är det gratis att byta HDMI-ingång?', 'Ja. Listan över ingångar i Mando TV är gratis, precis som att slå på tv:n och pilarna, OK och volymen. Ingångarna når du också via tv:ns meny.'),
      ('Hur vet jag vilken HDMI-ingång jag behöver?', 'Titta på HDMI-portarna på tv:n: var och en har ett nummer. Ta den där kabeln från din konsol eller spelare sitter.'),
      ('Vad gör jag om tv:n inte slås på?', 'Slå på den med knappen på apparaten. Om du redan har anslutit den och slagit på påslagning via nätverket kan du också slå på den med mobilen.'),
    ]),
  dict(clave='androidtv', corto='Android TV utan fjärrkontroll',
    titulo='Android TV utan fjärrkontroll: använd mobilen',
    desc='Ingen fjärrkontroll till Android TV eller Google TV? Anslut mobilen med den 6-tecknade koden på skärmen. Gratis, utan konto, utan reklam.',
    h1='Android TV utan fjärrkontroll: så använder du mobilen',
    intro='Om du har tappat bort fjärrkontrollen till din Android TV eller Google TV, eller dess batterier är slut, ersätter mobilen den. Det bästa: för att ansluta behöver du inte fjärrkontrollen, eftersom tv:n visar en kod på skärmen och du skriver in den på mobilen. Det fungerar på tv från Sony, Philips, TCL, Hisense, Sharp och Xiaomi med Android TV, på Chromecast med Google TV och på Nvidia Shield.',
    pasos=[
      'Slå på tv:n med knappen på apparaten. Den sitter nästan alltid nere i mitten eller på baksidan nära ett hörn.',
      'Anslut mobilen till samma wifi som tv:n.',
      'Ladda ner Mando TV, som är gratis och inte kräver något Google-konto, och öppna appen. Tryck på din tv i listan.',
      'Tv:n visar en kod med 6 bokstäver och siffror. Skriv in den på mobilen och tryck på Parkoppla. Du behöver inte fjärrkontrollen för det.',
      'Nu kan du använda pilar, OK, bakåt, hem, volym, ljud av och tangentbord. De är gratis, liksom applistan. Touchpad är Pro.',
      'För att slå på tv:n från mobilen nästa gång, leta i nätverks- eller energiinställningarna efter "Wake on LAN", "Nätverksstandby" eller "Väck via nätverk".',
    ],
    extra=[
      ('Om din tv inte går att slå på från mobilen', 'Inte alla Android TV kan slås på via nätverket; det beror på tillverkare och modell. Om din saknar funktionen, slå på den med knappen på tv:n och fortsätt på mobilen. Du kan stänga av den från appen.'),
      ('Chromecast med Google TV, Google TV Streamer och Shield', 'De ansluts på samma sätt: samma wifi, tryck på enheten i listan och skriv in koden. Om tv:n visar en annan ingång, byt till den HDMI-port där enheten sitter, som förklaras i [Byt HDMI-ingång på tv:n utan fjärrkontroll](@hdmi).'),
      ('Om koden inte visas eller meddelas som fel', 'Kontrollera att tv:n verkligen är påslagen och inte i standby. Koden ändras vid varje förfrågan: bara den sista fungerar. Mer information finns i [Android TV ber om en kopplingskod](@androidtv-code).'),
      ('Googles app eller Mando TV', 'Google har en egen app där du behöver ett Google-konto. Mando TV kräver inget konto, fungerar också i Windows och styr tv från LG, Samsung och Roku med samma app.'),
    ],
    marca='android',
    faq=[
      ('Behöver jag fjärrkontrollen för att koppla mobilen?', 'Nej. Koden visas på tv-skärmen och du skriver in den på mobilen. Du behöver bara slå på tv:n, vid behov med knappen på apparaten.'),
      ('Fungerar det med en Hisense?', 'På Hisense-tv med Android TV eller Google TV, ja. Hisense-tv med ett annat system är inte kompatibla.'),
      ('Kan jag skriva med mobilens tangentbord?', 'Ja. Tangentbordet är gratis och fungerar för sökning i YouTube, Netflix och de andra apparna.'),
    ]),
  dict(clave='lg-on', corto='Slå på LG-tv med mobilen',
    titulo='Slå på LG-tv med mobilen (steg för steg)',
    desc='Slå på LG-tv via wifi med mobilen: aktivera "Slå på tv med mobil" och använd Mando TV. Steg för steg, gratis.',
    h1='Så slår du på en LG-tv med mobilen',
    intro='Du kan slå på en LG-tv med mobilen, men först måste du aktivera en inställning på tv:n. Därefter slår mobilen på LG-tv:n via ditt wifi, helt utan fjärrkontroll. Det tar fem minuter och du gör det bara en gång.',
    pasos=[
      'Anslut mobilen och LG-tv:n till samma wifi.',
      'Öppna Inställningar på tv:n och leta efter "Slå på tv med mobil". Beroende på modell finns den under Allmänt eller Anslutning.',
      'Slå på "Slå på via wifi". Är tv:n ansluten med nätverkskabel, slå i stället på alternativet för kabel.',
      'Om din tv har "Quick Start+", slå på den också.',
      'Med tv:n påslagen öppnar du Mando TV på mobilen och trycker på din LG-tv i listan. Godkänn frågan som visas på skärmen. Så lär sig appen att väcka den.',
      'Stäng av tv:n och prova: tryck på tv:n i Mando TV, så frågar appen om den ska slå på den.',
    ],
    extra=[
      ('Om den inte slås på', 'Tv:n måste ha suttit på samma wifi när den stängdes av. Kontrollera att inställningen fortfarande är på och att mobilen sitter på samma nätverk. Har du bytt router, anslut igen med tv:n påslagen.'),
    ],
    marca='lg',
    faq=[
      ('Kan jag slå på LG-tv:n med mobilen om jag aldrig har anslutit den?', 'Nej. Först måste du slå på "Slå på tv med mobil" i tv:n och ansluta en gång med Mando TV medan tv:n är på.'),
      ('Behöver jag appen LG ThinQ?', 'Nej. Mando TV ansluter direkt via ditt wifi och kräver inget LG-konto.'),
      ('Fungerar det med mobildata?', 'Nej. Mobilen och tv:n måste sitta på samma wifi.'),
    ]),
  dict(clave='console', corto='Tv och konsol utan fjärrkontroll',
    titulo='Ingen fjärrkontroll? Slå på tv:n och byt HDMI',
    desc='Lanseringsdag och ingen fjärrkontroll? Slå på tv:n och byt med mobilen till HDMI-ingången för din PS5 eller Xbox. Gratis, utan reklam.',
    h1='Så slår du på tv:n och byter till HDMI-ingången för din konsol utan fjärrkontroll',
    intro='Lanseringsdag för GTA VI, konsolen är redo och fjärrkontrollen har försvunnit någonstans mellan soffkuddarna. Det händer oftare än man tror. Med Mando TV slår mobilen på tv:n och byter via ditt wifi hemma till ingången för din PlayStation eller Xbox.',
    pasos=[
      'Anslut mobilen till samma wifi som tv:n.',
      'Öppna Mando TV och tryck på din tv i listan (Samsung, LG, Roku eller Android TV).',
      'Om tv:n är avstängd, tryck på Slå på. Det fungerar när påslagning via nätverket är aktiverad i tv:n. Har du aldrig aktiverat den, slå på tv:n den här enda gången med knappen på apparaten och aktivera den till nästa gång.',
      'Slå på konsolen. Om HDMI-CEC är aktiverat (se det gratis tricket längre ner) byter tv:n av sig själv till dess ingång.',
      'Byter den inte, tryck på Ingångar i Mando TV och välj den HDMI-port där konsolen sitter: HDMI 1, HDMI 2 och så vidare.',
      'För volymen använder du de stora knapparna i appen medan du spelar.',
    ],
    extra=[
      ('Det gratis tricket: låt konsolen byta på tv:n', 'PS5 och Xbox kan slå på tv:n och hoppa direkt till sin HDMI-ingång vid start, tack vare HDMI-CEC. På PS5 hittar du det under Inställningar > System > HDMI > Aktivera HDMI-enhetslänk. På Xbox öppnar du Inställningar > Allmänt > Tv- och skärmalternativ och letar efter alternativet för enhetsstyrning. På tv:n heter funktionen olika beroende på märke: Anynet+ på Samsung, SIMPLINK på LG och BRAVIA Sync eller HDMI-styrning på andra.'),
      ('Om tv:n stannar på en annan bild', 'Är konsolen på men tv:n visar fortfarande antenn eller en app har den inte bytt ingång. Tryck på Ingångar på mobilen och välj konsolens HDMI-ingång. Eller använd pilarna och OK för att komma till tv:ns ingångar, eller knappen på själva tv:n, och välj HDMI-porten. Numret är porten där du har satt i konsolens kabel.'),
      ('Om det är en Roku TV', 'Knappen på tv:n, oftast nere i mitten eller på baksidan, slår på den. Därifrån sköter mobilen resten.'),
    ],
    marca=None,
    faq=[
      ('Har Mando TV något med GTA VI att göra?', 'Nej. Mando TV har ingen koppling till Rockstar Games eller Take-Two. Appen hjälper dig bara att inte förlora speltid för att du inte hittar fjärrkontrollen.'),
      ('Är det gratis att byta HDMI-ingång?', 'Ja. Listan över ingångar i Mando TV är gratis, precis som att slå på tv:n och pilarna, OK och volymen. Du kan också låta konsolen byta ingång själv med HDMI-CEC.'),
      ('Fungerar det med min tv?', 'Det fungerar med tv från Samsung, LG, Roku och Android TV på samma wifi. Är din från ett annat märke kan HDMI-CEC-tricket ändå hjälpa dig.'),
      ('Kan jag använda det för att spela GTA VI (GTA 6) på PS5 eller Xbox?', 'Mando TV påverkar varken konsolen eller spelet. Appen ser bara till att tv:n är på och står på rätt HDMI-ingång, så att du kan sätta dig och spela.'),
    ]),
  dict(clave='samsung-lost', corto='Samsung-tv utan fjärrkontroll',
    titulo='Borttappad Samsung fjärrkontroll? Använd mobilen',
    desc='Borttappad eller trasig Samsung fjärrkontroll? Använd mobilen som fjärrkontroll till Tizen-tv via wifi. Enkelt med Mando TV, gratis, utan reklam.',
    h1='Samsung-tv utan originalfjärrkontroll: så använder du mobilen',
    intro='Om du har tappat bort din Samsung fjärrkontroll eller den har slutat fungera kan du använda mobilen som fjärrkontroll via wifi. Det fungerar på Samsung-tv med Tizen, tillverkade 2016 och senare.',
    pasos=[
      'Slå på tv:n med knappen på apparaten. På de flesta modeller sitter den nere eller på baksidan, ibland som en liten joystick.',
      'Kontrollera att tv:n är ansluten till ditt wifi och att mobilen sitter på samma nätverk.',
      'Öppna Mando TV på mobilen. Din Samsung-tv dyker upp i listan av sig själv. Tryck på den.',
      'Tv:n ber dig godkänna anslutningen. På de flesta modeller godkänner du den med knapparna på tv:n eller med joysticken på baksidan.',
      'Klart, nu kan du använda mobilen som fjärrkontroll. Knapparna, tangentbordet och apparna är gratis; touchpad är en Pro-funktion.',
      'För att slå på tv:n från mobilen nästa gång, gå till Inställningar > Allmänt > Nätverk > Expertinställningar och slå på "Slå på med mobil".',
    ],
    extra=[
      ('Om tv:n inte frågar om tillstånd', 'Kanske är tillståndet redan sparat eller så sitter tv:n på ett annat wifi. Stäng Mando TV och öppna appen igen med tv:n påslagen. Är tv:n äldre än 2016 använder den ett annat system som ännu inte stöds.'),
      ('Om du nekade tillståndet av misstag', 'Gå till Inställningar > Allmänt > Hanterare för externa enheter > Enhetsanslutningshanterare på tv:n och sätt Mando TV som tillåten. Hittar mobilen ändå inte tv:n, läs [Mobilen hittar inte tv:n](@not-found).'),
    ],
    marca='samsung',
    faq=[
      ('Hur godkänner jag anslutningen om jag inte har någon fjärrkontroll?', 'På de flesta modeller godkänner du den med knapparna på tv:n eller med joysticken på baksidan. Har din modell inga knappar, skriv till hola@mandotv.app så hjälper vi dig.'),
      ('Kräver Mando TV ett Samsung-konto?', 'Nej. Anslutningen går direkt via ditt wifi, utan Samsung-konto.'),
      ('Fungerar det med min äldre Samsung-tv?', 'Det fungerar med Samsung-tv med Tizen, tillverkade 2016 och senare.'),
    ]),
  dict(clave='wifi', corto='Mobilen som fjärrkontroll via wifi',
    titulo='Använd mobilen som fjärrkontroll: styr tv:n via wifi',
    desc='Anslut mobilen till tv:n via wifi och använd den som fjärrkontroll till Samsung, LG, Roku och Google TV. Steg per märke med Mando TV. Gratis.',
    h1='Så ansluter du mobilen som fjärrkontroll till tv:n via wifi',
    intro='Du behöver bara mobilen och tv:n på samma wifi samt en fjärrkontrollsapp. Mando TV hittar din tv av sig själv och fungerar med Samsung, LG, Roku, Google TV och Android TV.',
    pasos=[
      'Anslut mobilen och tv:n till samma wifi.',
      'Öppna Mando TV. Din tv dyker upp i listan av sig själv. Tryck på den.',
      'Godkänn anslutningen för ditt märke (detaljerna står längre ner).',
      'Styr tv:n med knapparna eller med mobilens tangentbord. Touchpad är en Pro-funktion.',
    ],
    extra=[
      ('Samsung', 'Tv:n frågar om du tillåter anslutningen. Godkänn den på skärmen första gången. Det fungerar med Tizen, tillverkade 2016 och senare. För att slå på tv:n från mobilen, slå på "Slå på med mobil" under Inställningar > Allmänt > Nätverk > Expertinställningar.'),
      ('LG', 'Tv:n visar en fråga om tillstånd. Godkänn den första gången. För att slå på tv:n från mobilen, leta i inställningarna efter "Slå på tv med mobil" och slå på "Slå på via wifi".'),
      ('Roku', 'Roku kräver ingen koppling: tryck på den i listan så är du ansluten. För att slå på den, slå på "Snabb tv-start" under Inställningar > System > Ström.'),
      ('Google TV och Android TV', 'Tv:n visar en kod på skärmen. Skriv in den i Mando TV första gången. För att slå på tv:n, leta i inställningarna efter "Wake on LAN", "Nätverksstandby" eller "Väck via nätverk".'),
    ],
    marca=None,
    faq=[
      ('Behöver jag internet för att använda mobilen som fjärrkontroll?', 'Du behöver mobilen och tv:n på samma wifi. Mando TV ansluter direkt till din tv via det nätverket.'),
      ('Varför dyker min tv inte upp i listan?', 'Kontrollera att tv:n är på och att mobilen inte använder mobildata eller ett annat wifi. En del routrar har ett gästnätverk som skiljer enheter från varandra.'),
      ('Kan jag använda Mando TV på iPhone eller på en Android-mobil?', 'På iPhone och iPad, ja: appen finns redan i App Store. För Windows finns den också i Microsoft Store. Android kommer snart: du kan gå med i den gratis tidiga åtkomsten i Google Play.'),
    ]),
  dict(clave='pc', corto='Styr tv:n med datorn',
    titulo='Styr tv:n med en Windows-dator (gratis)',
    desc='Använd din Windows-dator som fjärrkontroll till Samsung, LG, Roku eller Google TV via wifi. Knappar, tangentbord och appar gratis; kortkommandon med Pro.',
    h1='Så styr du tv:n med en Windows-dator',
    intro='Om du tillbringar dagen framför datorn behöver du inte leta efter fjärrkontrollen: Mando TV för Windows styr din Samsung-, LG-, Roku-, Google TV- eller Android TV-tv via ditt wifi hemma. Praktiskt för att byta app, höja volymen eller skriva i YouTube med datorns tangentbord.',
    pasos=[
      'Ladda ner Mando TV gratis från Microsoft Store till din dator med Windows 10 eller 11.',
      'Kontrollera att datorn och tv:n sitter på samma nätverk (wifi eller kabel, men via samma router).',
      'Öppna Mando TV: din tv dyker upp i listan av sig själv. Tryck eller klicka på den.',
      'Första gången godkänner du anslutningen på tv-skärmen (på Google TV och Android TV skriver du in koden som tv:n visar).',
      'Klart: använd knapparna eller tangentbordet för att skriva i tv:ns sökruta. Touchpad är en Pro-funktion.',
    ],
    extra=[
      ('Kortkommandon på datorn (Pro)', 'Med Mando TV Pro styr du tv:n med datorns tangentbord: piltangenter för att navigera, Enter för OK, Backspace eller Esc för bakåt, + och - för volym, M för ljud av och mellanslag för paus.'),
      ('Minifjärrkontroll som alltid ligger överst (Pro)', 'Ha ett litet fönster med fjärrkontrollen alltid synligt medan du arbetar eller spelar på datorn.'),
      ('Prata med tv:n från datorn (Pro)', 'Med Mando TV Pro ger du tv:n kommandon via datorns mikrofon: "öppna YouTube", "höj volymen" eller "stäng av om 30 minuter", precis som du pratar. I Windows känns talet igen på själva datorn: du behöver inget internet, inget behöver ändras i Windows-inställningarna, och det fungerar på appens 6 språk. Det du säger lämnar inte datorn och sparas inte. Bara på mycket gamla processorer använder appen Windows diktering. Då måste röstigenkänning online vara påslagen i integritetsinställningarna och svenska (Sverige) vara tillagd i Windows. Saknas något säger appen till och öppnar inställningen med en knapp.'),
    ],
    marca=None,
    faq=[
      ('Behöver jag kabel eller Bluetooth för att styra tv:n med datorn?', 'Nej. Mando TV ansluter via ditt hemmanätverk: datorn och tv:n måste bara sitta på samma router.'),
      ('Fungerar det med alla tv-apparater?', 'Det fungerar med Samsung-tv med Tizen (tillverkade 2016 och senare), LG med webOS, Roku samt Google TV eller Android TV (Sony, Philips, TCL, Hisense, Sharp, Xiaomi, Toshiba, Panasonic, Haier, Skyworth och andra).'),
      ('Vad kostar det?', 'Knapparna, tangentbordet och påslagning via nätverket är gratis och utan reklam. Mando TV Pro är ett engångsköp utan prenumeration för extrafunktioner som touchpad, kortkommandona på datorn och minifjärrkontrollen.'),
      ('Varför förstår mikrofonen mig inte i Windows?', 'Kontrollera att röstfunktionen är aktiv (den ingår i Pro) och att datorns mikrofon fungerar i Windows. På nästan alla datorer känns talet igen på själva enheten, helt utan internet. Bara på mycket gamla processorer använder appen Windows diktering. Kontrollera då att röstigenkänning online är påslagen i Windows integritetsinställningar och att Windows har svenska (Sverige) bland språkinställningarna. Mando TV använder det språket bara medan den lyssnar.'),
    ]),
  dict(clave='roku-403', corto='Roku-appen fungerar inte',
    titulo='Roku-appen fungerar inte? Åtgärda fel 403',
    desc='Mobilen är ansluten men Roku svarar inte? Slå på "Styrning via mobilappar" i 5 steg och använd mobilen som fjärrkontroll igen.',
    h1='Roku-appen fungerar inte: så löser du problemet',
    intro='Om mobilen hittar din Roku och ansluter, men ingen knapp gör något, beror det nästan alltid på en inställning i själva Roku som blockerar fjärrkontrollsappar. Nyare Roku-versioner är mer begränsade som standard. I Rokus meny löser du det på en minut.',
    pasos=[
      'Tryck på Home på din Roku och gå till Inställningar.',
      'Öppna System och sedan Avancerade systeminställningar.',
      'Gå till "Styrning via mobilappar". På en del modeller heter den "Extern styrning".',
      'Välj Standard eller Aktiverad under "Nätverksåtkomst". Är det bara en strömbrytare på din modell, låt den stå på Aktiverad.',
      'Gå tillbaka till Mando TV på mobilen och tryck på din Roku. Knapparna reagerar nu.',
    ],
    extra=[
      ('Så vet du om det är ditt problem', 'Tecknet är tydligt: mobilen ser din Roku i listan och ansluter, men ingenting händer när du trycker på en knapp. Internt svarar Roku med fel 403, som betyder "förbjudet". Mando TV upptäcker det vid anslutningen och visar dig exakt de här stegen på skärmen.'),
      ('Standard eller Aktiverad, vilken väljer jag?', 'Båda fungerar: Mando TV behöver bara kommandon från ditt hemmanätverk. Om alternativet står på Avstängd (Begränsad i nyare programvara) svarar Roku inte på appar.'),
      ('Om du inte har Roku-fjärrkontrollen', 'Om inställningen står på Avstängd går den bara att ändra med den riktiga Roku-fjärrkontrollen. Låna en för att ändra det en gång; efter det kan du göra allt med mobilen. Läs också [Borttappad Roku fjärrkontroll](@roku-lost).'),
    ],
    marca='roku',
    faq=[
      ('Varför svarar min Roku inte längre, fast den fungerade förut?', 'En Roku-uppdatering kan begränsa den här inställningen mer. Det beror inte på din mobil eller ditt wifi: du behöver bara tillåta styrning via appar igen.'),
      ('Gäller det för Roku TV och för Roku-spelare?', 'Ja. Inställningen finns i samma meny på Roku-spelare och på Roku TV.'),
      ('Är det säkert att låta inställningen stå på Standard?', 'Ja. Den tar bara emot kommandon från enheter i ditt hemmanätverk.'),
    ]),
  dict(clave='not-found', corto='Mobilen hittar inte tv:n',
    titulo='Mobilen hittar inte tv:n? 6 saker att kontrollera',
    desc='Hittar fjärrkontrollsappen inte din tv? Kontrollera wifi, VPN och åtkomst till det lokala nätverket. För Samsung, LG, Roku och Android TV.',
    h1='Mobilen hittar inte tv:n: det här bör du kontrollera',
    intro='Du öppnar fjärrkontrollsappen och listan är tom, eller så dyker tv:n upp men anslutningen bryts. Nästan alltid beror det på nätverket och inte på tv:n. Gå igenom de här punkterna i ordning: den första löser de flesta fall.',
    pasos=[
      'Titta efter vilket wifi mobilen sitter på och vilket tv:n sitter på. Det måste vara samma nätverk med samma namn. Ett gästnätverk fungerar inte, eftersom det skiljer enheter från varandra.',
      'Stäng av VPN på mobilen om du använder ett. Med VPN på går mobilen ut på internet via ett annat nätverk och ser inte enheterna hemma hos dig, eller så bryts anslutningen efter några sekunder.',
      'Stäng av mobildata en liten stund. En del mobiler byter av sig själva från wifi till mobildata när signalen är svag.',
      'Slå på tv:n och vänta tills den har startat klart. En avstängd tv svarar inte på sökningen.',
      'Kontrollera på iPhone att appen har behörigheten "Lokalt nätverk": Inställningar > Integritet och säkerhet > Lokalt nätverk.',
      'Dyker den fortfarande inte upp, lägg till den för hand: tryck på "Lägg till med IP" i Mando TV och skriv in tv:ns IP-adress.',
    ],
    extra=[
      ('Låt appen guida dig', 'I tv-listan finns en knapp för när din tv inte dyker upp. Appen kontrollerar de vanligaste orsakerna steg för steg (samma wifi, VPN, behörighet för lokalt nätverk och mer) och visar efter varje åtgärd en knapp för att kontrollera igen. Guiden är gratis.'),
      ('Var du hittar tv:ns IP-adress', 'Den finns i tv:ns nätverksmeny och ser lite olika ut beroende på modell. På LG: Inställningar, Nätverk, Wifi-anslutning, Avancerade wifi-inställningar. På Samsung: Inställningar, Allmänt, Nätverk, Nätverksstatus, IP-inställningar. På Roku: Inställningar, Nätverk, Om. På Android TV och Google TV: Inställningar, Nätverk och internet, tryck sedan på ditt nätverk. Det är ett tal som 192.168.1.86.'),
      ('Om den dyker upp men anslutningen bryts', 'Bryts anslutningen efter några sekunder ligger orsaken oftast hos mobilen: ett VPN, byte till ett annat wifi eller energisparläget. Stäng av VPN, stanna kvar på samma wifi och försök igen.'),
      ('Wifi med 2,4 och 5 GHz', 'Det spelar ingen roll om mobilen sitter på 5 GHz-nätet och tv:n på 2,4 GHz-nätet, så länge båda kommer från samma router. Har du en wifi-förstärkare och tv:n ändå inte dyker upp, gå närmare huvudroutern med mobilen och försök igen.'),
    ],
    marca=None,
    faq=[
      ('Kan jag styra tv:n med mobildata?', 'Nej. Fjärrkontrollssignalen går via ditt wifi hemma, därför måste mobilen och tv:n sitta på samma nätverk.'),
      ('Varför fungerar det inte med VPN påslaget?', 'Eftersom VPN skickar all mobilens trafik via ett annat nätverk och mobilen då inte längre ser enheterna hemma hos dig. Stäng av det medan du använder fjärrkontrollen.'),
      ('Fungerar det med Bluetooth eller infrarött?', 'På smarta tv använder Mando TV wifi. Infrarött fungerar bara på Android-mobiler med infraröd sändare och är till för tv som inte är smarta. Bluetooth finns i betan, gratis och bara från Android 9: mobilen ansluter till tv:n som ett Bluetooth-tangentbord och en fjärrkontroll, helt utan wifi. Det fungerar med Google TV, Android TV och Fire TV; på andra märken som accepterar Bluetooth-tangentbord kan det fungera, Roku accepterar dem inte.'),
    ]),
  dict(clave='androidtv-code', corto='Android TV kopplingskod',
    titulo='Android TV ber om en kopplingskod: det här gör du',
    desc='Din Android TV eller Google TV visar en kod med 6 tecken när du ansluter. Så skriver du in den och det här gör du om den inte dyker upp eller är fel.',
    h1='Android TV ber om en kopplingskod: det här gör du',
    intro='När du ansluter mobilen till en Android TV eller Google TV för första gången visar tv:n en kod med 6 tecken på skärmen. Det är normalt och händer bara en gång: så är det säkert att ingen annan kan styra din tv. Här ser du hur du skriver in den och vad du gör om den inte dyker upp.',
    pasos=[
      'Slå på tv:n och låt startskärmen vara synlig.',
      'Öppna Mando TV på mobilen, på samma wifi som tv:n, och tryck på din tv i listan.',
      'Titta på tv-skärmen: en kod med 6 bokstäver och siffror visas.',
      'Skriv in den exakt som den visas på mobilen och tryck på Parkoppla. Bokstäverna går bara från A till F, så ett runt tecken är alltid siffran noll.',
      'Klart. Tv:n kommer ihåg din mobil och frågar inte efter koden igen.',
    ],
    extra=[
      ('Om koden inte visas på tv:n', 'Kontrollera att tv:n verkligen är påslagen och inte i standby, och att mobilen sitter på samma wifi. Tryck på tv:n en gång till på mobilen. Dyker den fortfarande inte upp, starta om tv:n: dra ut sladden i tio sekunder, sätt i den igen och försök på nytt.'),
      ('Om koden meddelas som fel', 'Koden ändras vid varje förfrågan. Om du har varit långsam eller har begärt den två gånger fungerar bara den sista på skärmen. Tryck på tv:n en gång till på mobilen och skriv in den nya koden.'),
      ('Om tv:n ber om koden igen', 'Det händer om tv:n har återställts till fabriksinställningarna eller om du rensar appens data på mobilen. Parkoppla igen, så sparas den. Har du ingen fjärrkontroll alls, läs [Android TV utan fjärrkontroll](@androidtv).'),
    ],
    marca='android',
    faq=[
      ('Vilka tv-apparater använder den här koden?', 'De med Android TV eller Google TV: Sony, Philips, TCL, Hisense, Sharp, Xiaomi, Chromecast med Google TV och några till.'),
      ('Behöver jag ett Google-konto på mobilen?', 'Nej. Koden på skärmen är allt du behöver.'),
      ('Är det säkert?', 'Ja. Koden bevisar att du sitter framför tv:n: ingen kan koppla utan att se den på skärmen.'),
    ]),
  dict(clave='roku-lost', corto='Borttappad Roku fjärrkontroll',
    titulo='Borttappad Roku fjärrkontroll? Använd mobilen via wifi',
    desc='Borttappad Roku fjärrkontroll? Mobilen ersätter den via wifi. Enkla steg, även om du har bytt router och Roku saknar wifi.',
    h1='Borttappad Roku fjärrkontroll: så använder du mobilen',
    intro='Om du har tappat bort din Roku fjärrkontroll eller den har slutat fungera ersätter mobilen den, så länge Roku fortfarande är ansluten till ditt wifi. Och om du har bytt wifi eller router finns det en utväg också för det.',
    pasos=[
      'Försök först få fjärrkontrollen att ringa. Har din Roku-fjärrkontroll en högtalare, till exempel Roku Voice Remote Pro, öppna Mando TV, anslut till Roku och använd alternativet för att få fjärrkontrollen att ringa, så att du hittar den. Det fungerar bara med Roku-fjärrkontroller med högtalare, och Roku måste vara påslagen.',
      'Slå på tv:n och låt Roku sitta kvar. Du behöver inte röra den.',
      'Anslut mobilen till samma wifi som Roku använder.',
      'Öppna Mando TV. Din Roku dyker upp i listan av sig själv. Tryck på den.',
      'Använd pilar, OK, hem och bakåt som på din vanliga fjärrkontroll. Roku frågar inte efter någon kod.',
      'Gör knapparna ingenting blockerar Roku styrning via appar: guiden [Roku-appen fungerar inte](@roku-403) förklarar hur du tillåter den.',
    ],
    extra=[
      ('Om Roku saknar wifi (bytt router eller flyttat)', 'Utan fjärrkontroll kommer du inte in i menyn för att ställa in det nya nätverket, men det finns ett trick: Roku ansluter av sig själv till ett nätverk som har samma namn och lösenord som det gamla. Skapa en wifi-hotspot med exakt det namnet och lösenordet på en annan mobil, anslut mobilen med Mando TV till den, så dyker Roku upp i listan. Gå därifrån till Inställningar, Nätverk och anslut den till det nya wifit.'),
      ('Om det är en Roku TV', 'Roku TV har en knapp på apparaten, nästan alltid nere i mitten eller på baksidan, som slår på tv:n. Det räcker för att slå på den och fortsätta med mobilen.'),
      ('Om du hellre köper en annan fjärrkontroll', 'Se till att den passar din modell. Små Roku-spelare bakom tv:n behöver en fjärrkontroll utan infrarött, eftersom infrarött inte når dem.'),
    ],
    marca='roku',
    faq=[
      ('Kan mobilen slå på Roku?', 'En ansluten Roku-spelare är alltid på. På en Roku TV slår Mando TV på den via wifi om "Snabb tv-start" är aktiverad under Inställningar > System > Ström.'),
      ('Och volymen?', 'På en Roku TV höjer och sänker mobilen volymen. På en Roku-spelare som är ansluten med HDMI beror det på tv:n: på många fungerar det, på andra inte.'),
      ('Måste jag skapa ett konto?', 'Nej. Mando TV kräver inget konto och styr dessutom tv från Samsung, LG och Android TV med samma app.'),
    ]),
]

SOPORTE = dict(
  titulo='Hjälp: anslut och slå på tv:n med Mando TV',
  desc='Så ansluter du Mando TV fjärrkontroll till LG, Samsung, Roku eller Android TV, slår på tv:n från mobilen och löser problem.',
  h1='Hjälp',
  intro='De vanligaste frågorna, i den ordning stegen kommer. Hittar du inte din, skriv till oss på <a href="mailto:hola@mandotv.app?subject=Hj%C3%A4lp%20med%20Mando%20TV">hola@mandotv.app</a> så svarar vi.',
)
SOPORTE_HTML = '''      <h2 id="encontrar">Hitta tv:n</h2>
      <div class="preguntas">
        <details open><summary>Min tv dyker inte upp i listan</summary>
          <ol>
            <li>Kontrollera att mobilen och tv:n sitter på samma wifi. Har din router ett 2,4 GHz- och ett 5 GHz-nät med olika namn ser de ibland inte varandra.</li>
            <li>Se till att tv:n är påslagen.</li>
            <li>Kontrollera på iPhone att Mando TV har behörigheten "Lokalt nätverk", under Inställningar, Mando TV.</li>
            <li>Tryck i tv-listan på knappen för när din tv inte dyker upp: appen kontrollerar de vanligaste orsakerna steg för steg (samma wifi, VPN, behörighet för lokalt nätverk och mer) och visar efter varje åtgärd en knapp för att kontrollera igen.</li>
            <li>Dyker den fortfarande inte upp, tryck på knappen +, välj märke och skriv in tv:ns IP-adress. Du ser den i tv:ns nätverksmeny (till exempel 192.168.1.50).</li>
          </ol>
        </details>
        <details><summary>Fungerar det med mobildata eller på språng?</summary>
          <p>Nej. Mando TV pratar med tv:n inom ditt hemmanätverk, så mobilen måste vara ansluten till det wifit.</p>
        </details>
      </div>

      <h2 id="conectar">Ansluta första gången</h2>
      <p>Kompletta guider per märke: <a href="@@R_lg@@">LG</a>, <a href="@@R_samsung@@">Samsung</a>, <a href="@@R_roku@@">Roku</a> och <a href="@@R_android@@">Android TV</a>.</p>
      <div class="preguntas">
        <details><summary>LG</summary>
          <p>När du trycker på tv:n visas en fråga om tillstånd på skärmen. Godkänn den med din vanliga fjärrkontroll. Det gör du bara en gång.</p>
        </details>
        <details><summary>Samsung</summary>
          <p>Tv:n frågar om du tillåter anslutningen från Mando TV. Välj "Tillåt" med fjärrkontrollen. Har du nekat av misstag, gå till Inställningar > Allmänt > Hanterare för externa enheter > Enhetsanslutningshanterare och ändra till tillåten.</p>
        </details>
        <details><summary>Roku</summary>
          <p>Roku frågar inte efter något tillstånd. Fungerar inte anslutningen, gå på Roku till Inställningar > System > Avancerade systeminställningar > Styrning via mobilappar och låt nätverksåtkomsten stå på Standard eller Aktiverad.</p>
        </details>
        <details><summary>Android TV och Google TV</summary>
          <p>Tv:n visar en kod med 6 tecken. Skriv in den exakt som den visas i Mando TV. Det fungerar på Sony, Philips, TCL, Hisense, Sharp, Xiaomi, Chromecast med Google TV och andra med Android TV.</p>
        </details>
      </div>

      <h2 id="encender">Slå på tv:n från appen</h2>
      <p>Mando TV slår på tv:n via ditt hemmanätverk. Det krävs två saker: du har anslutit minst en gång med tv:n påslagen, och påslagning via nätverket är aktiverad i tv:n. Inställningens namn skiljer sig beroende på modell; det här är de vanligaste:</p>
      <div class="preguntas">
        <details><summary>LG</summary>
          <p>Leta i inställningarna (beroende på modell under Allmänt eller Anslutning) efter "Slå på tv med mobil" och slå på "Slå på via wifi". Om det finns "Quick Start+", slå på den också.</p>
        </details>
        <details><summary>Samsung</summary>
          <p>Slå på "Slå på med mobil" under Inställningar > Allmänt > Nätverk > Expertinställningar.</p>
        </details>
        <details><summary>Roku</summary>
          <p>På Roku TV slår du på "Snabb tv-start" under Inställningar > System > Ström. Roku-spelare som är anslutna till en tv kan inte slås på på det här sättet.</p>
        </details>
        <details><summary>Android TV och Google TV</summary>
          <p>Det beror på tillverkaren. Leta i nätverks- eller energiinställningarna efter "Wake on LAN", "Nätverksstandby" eller "Väck via nätverk". En del modeller har inte det alternativet.</p>
        </details>
      </div>

      <h2 id="falla">Om något inte fungerar</h2>
      <div class="preguntas">
        <details><summary>Anslutningen bryts eller inget händer</summary>
          <ol>
            <li>Tryck på Anslut igen på fjärrkontrollens skärm.</li>
            <li>Hjälper inte det, stäng Mando TV och öppna appen igen.</li>
            <li>Har tv:n fått en annan IP-adress, ta bort den från listan och lägg till den igen.</li>
          </ol>
        </details>
        <details><summary>Så skickar du ett felrapport till oss</summary>
          <ol>
            <li>Tryck på knappen Anpassa i Mando TV (reglagen högst upp).</li>
            <li>Tryck på Kopiera testrapport.</li>
            <li>Klistra in den i ett mejl till hola@mandotv.app tillsammans med märke och modell på din tv.</li>
          </ol>
          <p>Rapporten innehåller inga lösenord, inga koder och inget du skriver.</p>
        </details>
        <details><summary>Jag har köpt Pro och det syns inte</summary>
          <p>Tryck på Återställ köp under Anpassa, med samma butikskonto som du köpte med. Syns det fortfarande inte, skriv till oss.</p>
        </details>
      </div>

      <h2 id="guias">Guider steg för steg</h2>
      <p><a href="@@R_guias@@">Se alla guider</a></p>
      <ul>
@@GUIAS@@
      </ul>

      <h2 id="contacto">Fler frågor?</h2>
      <p>Skriv till oss på <a href="mailto:hola@mandotv.app?subject=Hj%C3%A4lp%20med%20Mando%20TV">hola@mandotv.app</a>. Berätta märke och modell på din tv och vid vilket steg du fastnar. Skriv gärna på ditt eget språk. Vi svarar på spanska eller engelska och, om du vill, på ditt språk med hjälp av en översättare.</p>
'''

PRIVACIDAD = dict(
  titulo='Integritetspolicy | Mando TV',
  desc='Mando TV samlar inte in några personuppgifter: inga konton, ingen reklam, inga spårare. Appen pratar bara med din tv i ditt wifi.',
  h1='Integritet',
  intro='Kort sagt: Mando TV samlar inte in dina uppgifter. Det finns inga konton, ingen reklam, inga spårare och inga egna servrar som sparar vad du gör.',
)
PRIVACIDAD_HTML = '''      <p class="fecha">Gäller från den 14 november 2026. Senast uppdaterad den 25 november 2026.</p>

      <h2>Vilka vi är</h2>
      <p>Mando TV är en app som låter dig styra tv:n från mobilen eller datorn. Den här policyn beskriver vilken information appen använder och vad den gör med den. Har du frågor, skriv till oss på <a href="mailto:hola@mandotv.app">hola@mandotv.app</a>.</p>

      <h2>Vilka uppgifter vi samlar in</h2>
      <p>Appen: inga. Appen skickar varken information om dig eller om hur du använder den till oss eller till tredje part. Den använder inga verktyg för analys, reklam eller spårning.</p>
      <p>Den här webbplatsen: vi mäter besök på två sätt, som förklaras i avsnittet <a href="#cookies">Cookies på den här webbplatsen</a>.</p>

      <h2>Vad appen sparar på din enhet</h2>
      <p>För att fungera sparar appen följande bara på din mobil eller dator:</p>
      <ul>
        <li>De tv-apparater du har lagt till: namn, märke, IP-adress i ditt nätverk och nätverkets hårdvaruadress (MAC), som används för att slå på dem.</li>
        <li>Anslutningsnycklarna som varje tv lämnar när du godkänner tillståndet. De sparas krypterade i systemets säkra lagring (Nyckelringen på iPhone och Mac, Keystore på Android, skyddad lagring i Windows).</li>
        <li>Dina inställningar: ljust eller mörkt tema, bakgrundsfärg, vibration och typ av fjärrkontroll.</li>
        <li>Om du använder Pro-funktionerna: dina favoritappar, dina rutiner och dina senaste YouTube-sökningar (du kan radera dem i appen).</li>
      </ul>
      <p>Om du raderar appen raderas allt det med den.</p>

      <h2>Vem appen pratar med</h2>
      <p>Med dina tv-apparater, inom ditt wifi hemma. För att hitta dem söker appen igenom ditt lokala nätverk; därför ber den på en iPhone om behörigheten "Lokalt nätverk". Texten du skriver med appens tangentbord går direkt till tv:n och sparas inte.</p>
      <p>Dessutom hämtar appen vid start en liten offentlig fil från den här webbplatsen (mandotv.app/app/config.json) för att ta reda på om det finns en ny version som du bör installera och vilka funktioner som ingår i Mando TV Pro. Det är en nedladdning, som när man öppnar en sida: appen skickar varken dina uppgifter, dina tv-apparater eller vad du gör. Den anger bara appversionen och systemet (till exempel Android), så att den kan visa rätt meddelande. Har du inget internet fortsätter appen med den senast nedladdade filen; går det mer än 30 dagar utan att den kunnat laddas ner ber appen dig att ansluta till internet en stund.</p>

      <p>När du skickar foton eller videor till tv:n (en Pro-funktion) hämtar tv:n bara de filer du väljer, direkt från din mobil eller dator via ditt wifi hemma. De går varken via internet eller via oss, appen ser inte dina övriga foton, och delningen upphör så fort du stänger den skärmen.</p>
      <h2>Mikrofon och röst</h2>
      <p>Röstsökningen använder mikrofonen bara medan du trycker på talknappen. Det du säger omvandlas till text av systemets taligenkänning: av Apple på iPhone och Mac och av Google på Android, enligt deras egna integritetsvillkor. I Windows känns talet igen på din egen dator och lämnar inte enheten; bara på mycket gamla processorer använder appen röstinmatningen i Windows, från Microsoft, enligt deras integritetsvillkor. Mando TV spelar varken in eller sparar ljudet, och den text som uppstår går direkt till din tv, precis som det du skriver med tangentbordet.</p>

      <h2>Hem: enheter från Apple Home och Google Home</h2>
      <p>När du öppnar området Hem (under test) ber appen om tillstånd att se de enheter du redan har i Apples Hem-app (HomeKit) eller i Google Home. Med det tillståndet läser den deras namn, deras rum och deras status (på eller av, ljusstyrka, temperatur eller var i sitt program en hushållsapparat befinner sig) för att visa dem och skicka dem det du trycker på. Allt sker mellan din mobil och Apples eller Googles system: Mando TV sparar inte den listan, skickar den varken till oss eller till tredje part och använder den varken för reklam eller analys. På Android fungerar Google Home med ditt eget Google-konto, enligt Googles integritetspolicy. Du kan när som helst dra tillbaka tillståndet: på iPhone under Inställningar &gt; Integritet och säkerhet &gt; HomeKit, på Android i inställningarna för ditt Google-konto.</p>
      <p>När du trycker på "Hur fungerade Hem för dig?" öppnas din mejlapp med ett meddelande till hola@mandotv.app som innehåller en teknisk sammanfattning: appens version, systemet och hur många enheter av varje slag som dök upp och om de svarar. Namn på enheter, rum eller ditt hem ingår inte, och meddelandet skickas bara om du själv skickar det.</p>

      <h2>Testrapport</h2>
      <p>Appen har en knapp "Kopiera testrapport" som hjälper oss att åtgärda fel. Rapporten finns bara i appens minne så länge den är öppen och skickas aldrig av sig själv: du bestämmer om du kopierar och delar den. Den innehåller inga anslutningsnycklar, inga kopplingskoder och inget du skriver; bara de steg appen har utfört, som sökningar, anslutningar och felen.</p>

      <h2 id="cookies">Cookies på den här webbplatsen</h2>
      <p>Det här gäller bara webbplatsen mandotv.app, inte appen.</p>
      <h3>Alltid utan cookies</h3>
      <p>Vi räknar besök anonymt med Cloudflare Web Analytics: hur många som besöker webbplatsen, vilka sidor de läser och från vilket land. Den använder inga cookies, använder inte din IP-adress för att identifiera dig och spårar inte vad du gör på andra webbplatser.</p>
      <h3>Med cookies, bara om du samtycker</h3>
      <p>Om du trycker på "Acceptera" i cookiemeddelandet aktiverar vi Google Analytics (från Google LLC) för att bättre förstå hur webbplatsen används: sidvisningar, besökstid, typ av enhet, ungefärlig stad och varifrån du kommer. För det sparar den cookies som _ga och _ga_* i upp till 2 år i din webbläsare. Google kan behandla de här uppgifterna på servrar utanför Chile. Vi har stängt av reklamfunktionerna och Google Signals och använder inte de här uppgifterna för att visa dig reklam.</p>
      <p>Om du trycker på "Avvisa" eller inte väljer något laddas inte Google Analytics och ingen cookie sparas. Du kan ändra ditt val när som helst med knappen "Cookies" längst ner på varje sida; om du drar tillbaka samtycket raderar vi de här cookies.</p>
      <p>Ditt val sparas i din webbläsare (lokal lagring, skickas inte till någon) så att vi inte frågar dig igen.</p>

      <h2>Köp</h2>
      <p>När du köper Mando TV Pro hanteras betalningen av appbutiken (App Store, Google Play eller Microsoft Store). Vi tar inte emot och sparar inte dina kortuppgifter. Butiken bekräftar bara för appen att köpet finns.</p>

      <h2>Mejl du skickar till oss</h2>
      <p>När du skriver till oss på <a href="mailto:hola@mandotv.app">hola@mandotv.app</a> använder vi din e-postadress och det du berättar bara för att svara dig. Vi lämnar inte ut dem och använder dem inte för reklam. Du kan när som helst begära att vi raderar dina meddelanden.</p>

      <h2>Barn</h2>
      <p>Appen samlar inte in uppgifter från någon, inte heller från barn.</p>

      <h2>Ändringar i den här policyn</h2>
      <p>Om det en dag ändras vad appen gör med dina uppgifter uppdaterar vi den här sidan och datumet ovan innan ändringen når appen.</p>
'''


# >>> guías traídas del inglés (ensamblar.py)
# Adaptadas con Ollama (qwen3.6:35b) desde las guías inglesas y auditadas por Opus el 22-nov. Rutas en idiomas_sitio.py.
GUIAS += [
  dict(clave='no-sub', corto='Fjärrkontrollsapp utan prenumeration', fecha='2026-11-23',
    titulo='Fjärrkontrollsapp för tv utan prenumeration och reklam',
    desc='Trött på fjärrkontrollsappar med reklam eller veckoprenumeration? Mando TV är gratis och utan reklam, Pro är ett valfritt engångsköp. Ärlig jämförelse.',
    h1='En fjärrkontrollsapp utan prenumeration och utan reklam',
    intro='Många universalfjärrkontroller visar reklam eller kräver en veckoprenumeration innan de fungerar. Mando TV går en annan väg: fjärrkontrollen är gratis, det finns ingen reklam och inget konto. Det valfria Pro köper du bara en gång. Här är jämförelsen, även med det appen inte kan.',
    pasos=[
      'Öppna appens sida i butiken före installationen och kontrollera köpen i appen. Vecko- eller månadspriser tyder på en prenumeration.',
      'Kontrollera i Google Play om det står "Innehåller reklam" på sidan, och läs de senaste recensionerna med få stjärnor: där dyker ofta oväntade betalväggar upp.',
      'Se till att appen kan styra din tv via wifi. Mando TV fungerar med Samsung (från 2016), LG webOS, Roku, Google TV, Android TV och Fire TV.',
      'Installera Mando TV, anslut mobilen till samma wifi som tv:n och tryck på din tv i listan.',
      'Godkänn frågan på tv:n eller skriv in koden som visas. Knappar, volym, kanaler och tangentbord kostar ingenting.',
    ],
    tabla=dict(titulo='Mando TV jämfört med många fjärrkontrollsappar',
      cabeza=['', 'Mando TV', 'Många reklamfinansierade appar eller appar med prenumeration'],
      filas=[
        ['Grundläggande fjärrkontroll', 'Gratis', 'Ofta gratis med reklam eller gömd bakom en provperiod'],
        ['Reklam', 'Ingen', 'Vanligt'],
        ['Prenumeration', 'Ingen. Pro är ett valfritt engångsköp', 'Vecko- eller månadsplaner är vanliga'],
        ['Konto', 'Behövs inte', 'Varierar'],
        ['Smarta tv via wifi', 'Samsung (från 2016), LG webOS, Roku, Google TV, Android TV, Fire TV, Apple TV (beta)', 'Beror på appen'],
        ['Infrarött för äldre tv', 'Gratis på Android-mobiler med infraröd sändare (nytt)', 'Några appar, bara på mobiler med infraröd sändare'],
        ['Bluetooth', 'Beta från Android 9, gratis', 'Beror på appen'],
        ['Foton och videor till tv:n', 'Pro, via wifi (ingen skärmspegling)', 'Beror på appen'],
        ['Mobiler och datorer', 'iPhone, iPad och Windows, samt Android i tidig åtkomst', 'Varierar'],
        ['Skärmspegling', 'Gratis på iPhone och iPad, via skärmsynkronisering i Kontrollcenter (tv med AirPlay)', 'Några appar erbjuder det'],
      ],
      nota='Mando TV jämförs inte med någon särskild app. De aktuella priserna står på butikssidan för respektive app.'),
    extra=[
      ('Vad Mando TV inte gör', 'Den har ingen egen skärmspegling: på iPhone och iPad leder den dig till skärmsynkronisering i Kontrollcenter, iPhones egen funktion, som fungerar med tv med AirPlay. Med Mando TV Pro kan den dessutom skicka foton och videor till tv:n via ditt wifi. Den styr smarta tv via hemmets wifi. Tv utan smart-funktion kan styras med infrarött från en Android-mobil med infraröd sändare. Från Android 9 kan mobilen också ansluta via Bluetooth som tangentbord och fjärrkontroll till Google TV, Android TV och Fire TV, helt utan wifi. Det alternativet finns i betan och är gratis.'),
      ('Hur Mando TV tjänar pengar', 'Inte på reklam och inte på dina uppgifter: appen samlar inte in några. Mando TV finansieras av Pro, ett valfritt engångsköp för extrafunktioner. Den grundläggande fjärrkontrollen är gratis.'),
      ('På de enheter du redan har', 'iPhone och iPad från App Store, Windows-datorer från Microsoft Store och Android via gratis tidig åtkomst i Google Play. Se [Fjärrkontrollsapp för iPhone](@iphone) och [Fjärrkontrollsapp för Windows](@windows).'),
      ('Integritet', 'Inget konto och ingen spårning i appen. Kommunikationen med tv:n sker bara i det lokala nätverket, anslutningsuppgifterna ligger krypterade kvar på din enhet. Detaljer finns i [integritetspolicyn](@privacidad).'),
    ],
    marca=None,
    faq=[
      ('Finns det en fjärrkontrollsapp utan prenumeration?', 'Ja. Mando TV har ingen prenumeration alls: fjärrkontrollen är gratis och utan reklam, Pro är ett valfritt engångsköp.'),
      ('Är Mando TV verkligen gratis?', 'Ja. Pilknappar, OK, bakåt, hem, volym, kanaler, siffror, tangentbord och på- och avstängning är gratis, utan reklam och utan tidsgräns.'),
      ('Fungerar det utan wifi?', 'Oftast nej. Mando TV styr smarta tv via ditt hemmawifi. Undantag: infrarött på Android-mobiler med infraröd sändare, som också fungerar med tv utan smart-funktion eller utan wifi-anslutning, och Bluetooth, i betan från Android 9, för Google TV, Android TV och Fire TV.'),
    ]),
  dict(clave='roku-app-alt', corto='Alternativ till Roku-appen', fecha='2026-11-23',
    titulo='Alternativ till Roku-appen: enkel Roku fjärrkontroll',
    desc='Ett alternativ till Roku-appen som fjärrkontroll: Mando TV styr Roku TV och Roku-spelare via wifi, utan konto och reklam, samt Samsung, LG och Google TV.',
    h1='Alternativ till Roku-appen: en för alla tv-apparater',
    intro='Den officiella Roku-appen kan mycket: Channel Store, casting, Private Listening och en fjärrkontroll. Om du bara vill ha en snabb fjärrkontroll eller även har en Samsung-, LG- eller Google TV-tv hemma är Mando TV ett enkelt alternativ som styr Roku via ditt wifi utan konto.',
    pasos=[
      'Anslut mobilen och Roku till samma wifi.',
      'Ladda ner Mando TV och öppna det. Din Roku TV eller Roku-spelare dyker upp i listan. Tryck på den. Roku frågar inte efter någon kod.',
      'Använd pilknapparna, OK, bakåt, hem, volym och tangentbordet. Skriv sökningar i Rokus kanaler med mobilens tangentbord.',
      'Om knapparna inte gör något, gå på Roku till Inställningar > System > Avancerade systeminställningar > Styrning via mobilappar och sätt Nätverksåtkomst till Standard eller Aktiverad (på nyare Roku-programvara, sätt Styrning via mobilappar till Aktiverad).',
      'Valfritt: slå på "Snabb tv-start" på Roku TV under Inställningar > System > Ström, så att Mando TV kan slå på tv:n.',
    ],
    extra=[
      ('Där Mando TV passar bättre', 'En app för flera tv-apparater: Roku, Samsung, LG och Google TV eller Android TV. Utan konto, utan reklam. Den fungerar också på en Windows-dator, vilket är praktiskt vid skrivbordet. Pilknappar och volym reagerar snabbt, och med tangentbordet skriver du sökningar utan besvär.'),
      ('Där den officiella Roku-appen är bättre', 'Behåll Roku-appen för det den erbjuder utöver fjärrkontrollen, som att bläddra bland och lägga till kanaler från Roku Channel Store samt den egna castingen och Private Listening (ljud i hörlurar på mobilen). Använd båda om du vill. De kan finnas på samma mobil.'),
      ('Roku TV och Roku-spelare', 'Båda fungerar. Det omfattar Roku TV-modeller från TCL, Hisense, Philips och andra samt Roku Express, Streaming Stick och Ultra. Detaljer finns på [sidan om Roku fjärrkontrollsapp](@roku).'),
      ('Om Roku-appen har slutat fungera', 'Om knapparna inte längre reagerar blockerar Roku oftast styrning via appar. Guiden [Roku-appen fungerar inte](@roku-403) visar inställningen som löser problemet.'),
      ('Gratis och Pro', 'Pilknappar, OK, bakåt, hem, volym, kanaler, siffertangenter, tangentbord, att öppna appar, att byta ingångar och att slå på eller stänga av är gratis, utan reklam och utan prenumeration. Mando TV Pro är ett valfritt engångsköp för extrafunktioner.'),
    ],
    marca='roku',
    faq=[
      ('Behöver jag ett Roku-konto för att använda Mando TV?', 'Nej. Mando TV kommunicerar med Roku via ditt hemmanätverk och frågar inte efter något konto.'),
      ('Ersätter Mando TV Roku Mobile-appen helt?', 'Som fjärrkontroll ja. För Channel Store, casting och Private Listening, behåll den officiella Roku-appen.'),
      ('Fungerar det med min Roku Express eller Streaming Stick?', 'Ja. Alla Roku-spelare och Roku TV styrs på samma sätt.'),
    ]),
  dict(clave='lg-thinq', corto='Alternativ till appen LG ThinQ', fecha='2026-11-23',
    titulo='Alternativ till appen LG ThinQ: LG fjärrkontroll utan konto',
    desc='Söker du ett alternativ till appen LG ThinQ bara som fjärrkontroll? Mando TV styr LG-tv med webOS via wifi, utan LG-konto och utan reklam.',
    h1='Alternativ till appen LG ThinQ för din LG-tv',
    intro='LG ThinQ är LG:s officiella app, gjord för hela det smarta hemmet: hushållsapparater, tv:n och mer. Om du bara vill ha en enkel fjärrkontroll till din LG-tv gör Mando TV precis det via ditt wifi hemma, utan att du behöver skapa ett LG-konto och utan reklam.',
    pasos=[
      'Anslut mobilen eller datorn (iPhone, Android eller Windows) och din LG-tv till samma wifi.',
      'Ladda ner Mando TV och öppna det. Din LG-tv dyker upp i listan av sig själv. Tryck på den.',
      'På tv:n visas en fråga. Godkänn den en gång med tv:ns fjärrkontroll, joysticken under skärmen eller Magic Remote.',
      'Knappar, volym och tangentbord fungerar direkt. Du behöver inget LG-konto och behöver inte registrera tv:n.',
      'Valfritt: slå på "Slå på tv med mobil" i tv:ns inställningar så att du även kan slå på tv:n från mobilen.',
    ],
    extra=[
      ('Mando TV eller LG ThinQ: vad passar till vad', 'Använd ThinQ om du vill hantera LG:s hushållsapparater som en tvättmaskin, ett kylskåp eller en luftkonditionering, eller behöver funktioner i ditt LG-konto. Använd Mando TV om du vill ha en snabb, enkel fjärrkontroll till tv:n som också fungerar för Samsung, Roku och Google TV i samma app. Många behåller båda: ThinQ för hushållsapparaterna, Mando TV för tv:n.'),
      ('Vad Mando TV gör på en LG-tv', 'Det fungerar med LG Smart TV med webOS, alltså de flesta modeller sedan 2014, inklusive LED, NanoCell, QNED och OLED. Du får pilknapparna, OK, bakåt, hem, volym, kanaler, ljud av, uppspelningsstyrning och ett tangentbord för att skriva i YouTube, Netflix eller webbläsaren. Applistan och listan över ingångar är också gratis. Med Pro får du dessutom en pekare som med Magic Remote.'),
      ('Vad Mando TV inte gör', 'Det styr inga LG-hushållsapparater, använder inte ditt LG-konto och ersätter inte LG:s kontotjänster på tv:n. Det är en fjärrkontroll, inte en nav för det smarta hemmet.'),
      ('Integritet och reklam', 'Mando TV har ingen reklam och inget konto. Det pratar med tv:n bara inom ditt hemmanätverk och sparar anslutningsnyckeln krypterad på din enhet. Alla funktioner hittar du på sidan [LG fjärrkontrollsapp](@lg).'),
      ('Gratis och Pro', 'Pilknappar, OK, bakåt, hem, volym, kanaler, siffertangenter, tangentbord, att öppna appar, att byta ingångar och att slå på eller stänga av är gratis, utan reklam och utan prenumeration. Mando TV Pro är ett valfritt engångsköp för extrafunktioner.'),
    ],
    marca='lg',
    faq=[
      ('Kan jag styra min LG-tv utan appen LG ThinQ?', 'Ja. Mando TV ansluter direkt via ditt wifi till LG-tv med webOS. Du godkänner en fråga på tv:n en gång och det var allt, helt utan LG-konto.'),
      ('Fungerar Mando TV med pekaren på LG Magic Remote?', 'Mando TV Pro har en pekare som du flyttar med fingret på mobilens skärm, ungefär som Magic Remote flyttar pilen.'),
      ('Är Mando TV från LG?', 'Nej. Mando TV är en oberoende app och har ingen koppling till LG. LG och ThinQ tillhör sina ägare och nämns bara för att beskriva kompatibilitet.'),
    ]),
  dict(clave='smartthings', corto='Alternativ till SmartThings', fecha='2026-11-23',
    titulo='SmartThings fungerar inte? Enkelt alternativ för Samsung',
    desc='SmartThings för långsamt eller buggigt? Mando TV styr Samsung-tv med Tizen direkt via wifi. Utan Samsung-konto, utan reklam. Steg för steg.',
    h1='Alternativ till SmartThings för Samsung-tv',
    intro='SmartThings är Samsungs app för hela det smarta hemmet, och dess fjärrkontroll går via ditt Samsung-konto. Om den har slutat fungera eller du söker en snabb lösning styr Mando TV Samsung-tv med Tizen, tillverkade 2016 och senare, direkt via ditt wifi utan konto.',
    pasos=[
      'Anslut mobilen och Samsung-tv:n till samma wifi.',
      'Ladda ner Mando TV och öppna appen. Din Samsung-tv dyker upp i listan av sig själv. Tryck på den.',
      'Tv:n frågar om du vill tillåta anslutningen. Välj "Tillåt" med fjärrkontrollen eller med knappen på tv:n (bara första gången).',
      'Använd direkt pilknapparna, OK, bakåt, hem, volym, kanaler och tangentbordet.',
      'Valfritt: slå på "Slå på med mobil" under Inställningar > Allmänt > Nätverk > Expertinställningar så att Mando TV också kan slå på tv:n.',
    ],
    extra=[
      ('Varför en mobilfjärrkontroll slutar fungera', 'Orsakerna är oftast enkla: mobilen och tv:n sitter på olika wifi, ett VPN är aktivt eller tv:n ligger i djup standby. I SmartThings kan dessutom Samsung-kontot ställa till det, till exempel om du har blivit utloggad. Mando TV pratar direkt med tv:n i hemmanätverket, det finns inget konto att logga in på. Fler tips finns i [Mobilen hittar inte tv:n](@not-found).'),
      ('Mando TV eller SmartThings: vad passar till vad', 'Behåll SmartThings om du använder det för Samsungs hushållsapparater, lampor eller andra smarta hem-enheter eller för funktioner i ditt Samsung-konto. Använd Mando TV om du helt enkelt vill ha en snabb fjärrkontroll till tv:n eller även har en enhet från LG, Roku, Google TV eller Fire TV hemma: en app styr alla. Båda apparna kan finnas på samma mobil.'),
      ('Om du nekade tillståndet av misstag', 'Gå till Inställningar > Allmänt > Hanterare för externa enheter > Enhetsanslutningshanterare på tv:n och sätt Mando TV som tillåten.'),
      ('Ingen fjärrkontroll?', 'Du kan godkänna frågan med knappen på själva tv:n. Guiden [Samsung-tv utan originalfjärrkontroll](@samsung-lost) visar hur du gör.'),
      ('Gratis och Pro', 'Fjärrkontrollen kan du ladda ner och använda gratis, utan reklam och utan prenumeration. Mando TV Pro är ett valfritt engångsköp för extrafunktioner.'),
    ],
    marca='samsung',
    faq=[
      ('Kan jag styra min Samsung-tv utan SmartThings?', 'Ja. Mando TV ansluter direkt via ditt wifi till Samsung-tv med Tizen. Du tillåter anslutningen en gång på tv:n, utan Samsung-konto.'),
      ('Styr Mando TV också Samsungs hushållsapparater?', 'Nej. Det är bara en fjärrkontroll till tv:n. För hushållsapparater och andra smarta hem-enheter behåller du SmartThings.'),
      ('Är Mando TV från Samsung?', 'Nej. Mando TV är en oberoende app och har ingen koppling till Samsung. Samsung och SmartThings tillhör sina ägare och nämns bara för att beskriva kompatibilitet.'),
    ]),
  dict(clave='googletv-alt', corto='Alternativ till Google TV-fjärrkontrollen', fecha='2026-11-23',
    titulo='Google TV-fjärrkontrollen fungerar inte? Alternativet',
    desc='Hittar mobilfjärrkontrollen för Google TV inte tv:n? Mando TV styr Google TV och Android TV via wifi, utan Google-konto och reklam.',
    h1='Alternativ till Google TV-fjärrkontrollen i mobilen',
    intro='Mobilfjärrkontrollen för Google TV och Android TV ligger i Googles egen app och är kopplad till ditt Google-konto. Hittar den inte tv:n kommer du ingenstans. Mando TV är en separat fjärrkontrollsapp som kopplas med koden på 6 tecken på skärmen och fungerar utan Google-konto, på en iPhone, en Android-mobil eller en Windows-dator.',
    pasos=[
      'Slå på tv:n och anslut mobilen till samma wifi.',
      'Ladda ner Mando TV och öppna appen. Tryck i listan på din tv med Google TV eller Android TV.',
      'Tv:n visar en kod med 6 tecken. Skriv in den i Mando TV och tryck på Parkoppla.',
      'Använd pilknapparna, OK, bakåt, hem, volymen och tangentbordet. Du behöver inte logga in någonstans.',
      'Valfritt: leta i tv:ns inställningar efter Wake on LAN eller "Väck via nätverk" så att appen också kan slå på tv:n.',
    ],
    extra=[
      ('Varför mobilfjärrkontrollen inte hittar tv:n längre', 'Oftast beror det på nätverket: mobilen och tv:n sitter på olika wifi, ett VPN är aktivt eller ett gästnätverk skiljer enheterna åt. Åtgärda det först, eftersom det påverkar alla fjärrkontrollsappar. Mer om det i [Mobilen hittar inte tv:n](@not-found).'),
      ('Vilka tv-apparater det fungerar med', 'Tv med Google TV och Android TV från Sony, TCL, Hisense, Philips, Sharp, Xiaomi, Toshiba med flera, samt Chromecast med Google TV, Google TV Streamer och Nvidia Shield. Alla kopplas på samma sätt, en gång med koden på skärmen.'),
      ('Där Googles app är bättre', 'Googles app hjälper dig också att hitta innehåll att titta på och kommer ihåg din bevakningslista. Behåll den för det. Mando TV är bara fjärrkontrollen och styr dessutom Samsung, LG, Roku och Fire TV-enheter från samma app samt från en Windows-dator.'),
      ('Om den gamla fjärrkontrollsappen för Android TV saknas', 'Google har flyttat mobilfjärrkontrollen från den gamla appen Android TV Remote Control till appen Google TV. Om du söker en fristående fjärrkontroll är Mando TV ett alternativ.'),
      ('Gratis och Pro', 'Fjärrkontrollen kan du ladda ner och använda gratis, utan reklam och utan prenumeration. Mando TV Pro är ett valfritt engångsköp för extrafunktioner.'),
    ],
    marca='android',
    faq=[
      ('Behöver jag ett Google-konto för att använda Mando TV med Google TV?', 'Nej. Koden på tv:n räcker för kopplingen.'),
      ('Fungerar det med Chromecast med Google TV?', 'Ja. Kopplingen går likadant, med koden på 6 tecken på skärmen.'),
      ('Kan jag använda det från en iPhone?', 'Ja. Mando TV finns i App Store för iPhone och iPad, i Microsoft Store för Windows och i den gratis tidiga åtkomsten i Google Play för Android.'),
    ]),
  dict(clave='windows', corto='Fjärrkontroll för Windows-dator', fecha='2026-11-23',
    titulo='Fjärrkontrollsapp för Windows: styr tv:n från datorn',
    desc='Styr Samsung, LG, Roku, Google TV eller Fire TV från en Windows-dator med Mando TV: kortkommandon, minifjärrkontroll och wifi. I Microsoft Store.',
    h1='Fjärrkontrollsapp för Windows-datorn',
    intro='Mando TV har en Windows-app som förvandlar din dator eller bärbara dator till en fjärrkontroll för tv:n via hemmanätverket. Skriv på tv:n med ditt riktiga tangentbord, låt ett litet fjärrkontrollsfönster ligga överst medan du arbetar och styr Samsung, LG, Roku, Google TV eller Fire TV med samma app.',
    pasos=[
      'Installera Mando TV gratis från Microsoft Store på en dator med Windows 10 eller 11.',
      'Se till att datorn och tv:n sitter på samma nätverk, via wifi eller kabel till samma router.',
      'Öppna Mando TV. Tv:n dyker upp i listan. Klicka på den.',
      'Godkänn frågan på tv:n om den frågar (LG, Samsung), eller skriv in koden som visas (Google TV, Fire TV).',
      'Klicka på knapparna eller skriv en sökning med tangentbordet. Klart.',
    ],
    extra=[
      ('Kortkommandon (Pro)', 'Med Pro blir datorns tangentbord en fjärrkontroll: piltangenter för att röra dig, Enter för OK, Backspace eller Esc för att gå tillbaka, plus och minus för volym, M för ljud av och mellanslag för paus.'),
      ('Minifjärrkontroll (Pro)', 'Ett litet fjärrkontrollsfönster som ligger kvar ovanpå alla andra fönster. Så ändrar du volymen eller pausar utan att avbryta ditt arbete.'),
      ('Skriva på tv:n från datorn', 'Skärmtangentbordet på en tv är långsamt. I Mando TV skriver du med ditt riktiga tangentbord och texten hamnar i tv:ns sökruta. Den delen är gratis.'),
      ('Mer information', 'Steg-för-steg-guiden hittar du i [Styr tv:n med datorn](@pc). För mobilen, läs [Mobilen som fjärrkontroll via wifi](@wifi).'),
      ('Gratis och Pro', 'Pilknapparna, OK, bakåt, hem, volym, kanaler, siffertangenter, tangentbord, att öppna appar, att byta ingångar och att slå på eller stänga av är gratis, utan reklam och utan prenumeration. Mando TV Pro är ett valfritt engångsköp för extrafunktioner. I Windows köper du Pro via Microsoft Store.'),
      ('Röstkommandon från datorn (Pro)', 'Med Pro kan du prata med tv:n via datorns mikrofon. Talet känns igen direkt på datorn: du behöver inget internet och behöver inte ställa in något i Windows. Det du säger lämnar aldrig datorn och sparas inte. Bara på mycket gamla processorer faller appen tillbaka på röstinmatningen i Windows. Då måste röstigenkänning online vara påslagen i integritetsinställningarna och ditt språk vara tillagt i Windows.'),
    ],
    marca=None,
    faq=[
      ('Behöver fjärrkontrollsappen för Windows Bluetooth eller kabel?', 'Nej. Den använder ditt hemmanätverk. Datorn och tv:n måste bara vara anslutna till samma router.'),
      ('Vilka tv-apparater kan jag styra från Windows?', 'Samsung-tv med Tizen, LG-tv med webOS, Roku TV och spelare, Google TV och Android TV samt Fire TV.'),
      ('Kan jag se tv-bilden på datorn eller höra den i datorns högtalare?', 'Nej. Mando TV är bara en fjärrkontroll. Det speglar eller strömmar inte tv-bilden till datorn.'),
      ('Varför fungerar rösten inte på min Windows-dator?', 'Röststyrningen är en Pro-funktion. Kontrollera alltså att Pro är aktivt och att datorns mikrofon fungerar. På de flesta datorer känns talet igen direkt på datorn, utan internet. Bara på mycket gamla processorer använder appen röstinmatningen i Windows: slå då på röstigenkänning online i Windows integritetsinställningar och lägg till ditt språk i språkinställningarna.'),
    ]),
  dict(clave='iphone', corto='Fjärrkontrollsapp för iPhone', fecha='2026-11-23',
    titulo='Fjärrkontrollsapp för iPhone: Samsung, LG, Roku, Google TV',
    desc='Använd din iPhone som fjärrkontroll till Samsung, LG, Roku, Google TV och Fire TV via wifi. Gratis i App Store, utan konto och utan reklam.',
    h1='Fjärrkontrollsapp för iPhone: en för alla tv-apparater',
    intro='Mando TV gör din iPhone eller iPad till fjärrkontroll för Samsung, LG, Roku, Google TV eller Android TV samt Fire TV, via ditt wifi hemma. Appen är gratis i App Store, utan konto och utan reklam. Den finns också för Android och Windows.',
    pasos=[
      'Ladda ner Mando TV gratis från App Store.',
      'Anslut iPhone och tv:n till samma wifi.',
      'Öppna Mando TV och tryck på Tillåt när iOS frågar om åtkomst till det lokala nätverket. Appen behöver det för att hitta tv:n.',
      'Tryck på din tv i listan. Godkänn frågan på tv:n om den frågar (LG och Samsung), eller skriv in koden som tv:n visar (Google TV eller Fire TV).',
      'Använd knapparna, volymen och tangentbordet. Du är ansluten.',
    ],
    extra=[
      ('Fungerar med de här tv-apparaterna', 'LG webOS, Samsung Tizen (tillverkade 2016 och senare), Roku TV och Roku-spelare, Google TV och Android TV samt Fire TV. Märkenas sidor är [Samsung](@samsung), [LG](@lg), [Roku](@roku) och [Android TV](@android).'),
      ('Varför den frågar efter lokalt nätverk', 'iPhone blockerar appars åtkomst till enheter i ditt hemmanätverk om du inte tillåter det. Om tv:n inte dyker upp i listan, öppna Inställningar > Mando TV och slå på "Lokalt nätverk". Appen kommunicerar bara med din tv inom ditt hemmanätverk.'),
      ('Varför Mando TV och inte tillverkarens app', 'Varje tv-märke har sin egen app och vill ha en egen inställning eller ett eget konto. Mando TV är en app för alla, utan konto.'),
      ('Gratis och Pro på iPhone', 'Pilknappar, OK, bakåt, hem, volym, kanaler, siffertangenter, tangentbord, att öppna appar, att byta ingångar och att slå på eller stänga av är gratis, utan reklam och utan prenumeration. Mando TV Pro är ett valfritt engångsköp för extrafunktioner, direkt i appen.'),
    ],
    marca=None,
    faq=[
      ('Är Mando TV gratis på iPhone?', 'Nedladdningen är gratis, utan reklam. Den grundläggande fjärrkontrollen är gratis, liksom att öppna appar och byta ingångar. Extrafunktioner ingår i Mando TV Pro, ett valfritt engångsköp.'),
      ('Fungerar det på iPad?', 'Ja. Samma app fungerar på iPhone och iPad.'),
      ('Behöver en fjärrkontrollsapp för iPhone Bluetooth eller en infraröd sändare?', 'Inte på iPhone. iPhone har ingen infraröd sändare, därför finns inte infraröd styrning där, och Bluetooth-alternativet finns bara för Android 9 eller senare, inte för iPhone. På iPhone styr Mando TV smarta tv samt Apple TV (beta) via ditt wifi hemma.'),
    ]),
  dict(clave='firetv', corto='Fire TV-fjärrkontroll', fecha='2026-11-23',
    titulo='Fire TV-fjärrkontrollsapp för mobil och dator',
    desc='Fire TV-fjärrkontroll i mobilen: styr Fire TV Stick, Fire TV Cube eller en tv med Fire TV via wifi, med 4-siffrig PIN. Utan Amazon-app.',
    h1='Fire TV-fjärrkontroll för din mobil eller dator',
    intro='Om Fire TV-fjärrkontrollen är borta eller batterierna är slut styr Mando TV en Fire TV Stick, en Fire TV Cube eller en tv med inbyggd Fire TV via wifi. Kopplingen sker med en 4-siffrig PIN. Fire TV är nytt i Mando TV, så uppdatera appen först.',
    pasos=[
      'Uppdatera Mando TV till den senaste versionen från App Store, Microsoft Store eller Google Play.',
      'Slå på Fire TV och anslut mobilen till samma wifi.',
      'Öppna Mando TV. Din Fire TV dyker upp i listan. Tryck på den.',
      'På tv-skärmen visas en 4-siffrig PIN. Skriv in den i Mando TV. Det gör du bara en gång.',
      'Använd pilknapparna, OK, bakåt, hem, uppspelningsknapparna och tangentbordet för sökningar.',
    ],
    extra=[
      ('Fire TV-enheter som stöds', 'Fire TV Stick, Fire TV Stick 4K, Fire TV Cube och tv med inbyggd Fire TV. Stödet är nytt, och vi har hittills bara kunnat testa några få riktiga enheter. Om något inte fungerar som väntat, skriv till oss med din modell via hjälpsidan.'),
      ('Slå på Fire TV', 'Mando TV slår inte på en Fire TV via nätverket. Slå på tv:n med strömknappen på apparaten: en isatt Fire TV Stick eller Cube vaknar oftast via HDMI-CEC, och på en tv med inbyggd Fire TV är tv:n själva Fire TV. Därefter styr du den från mobilen.'),
      ('Om din Fire TV inte dyker upp', 'Se till att båda enheterna sitter på samma wifi och att Fire TV är vaken. Tillåt "Lokalt nätverk" för Mando TV i inställningarna på en iPhone. Se [Mobilen hittar inte tv:n](@not-found).'),
      ('Ingen fjärrkontroll alls?', 'Fire TV måste visa PIN-koden på skärmen, så tv:n och Fire TV måste vara på och visa en bild. Om tv:n står på fel ingång, byt med knapparna på tv:n. Se [Byt ingång utan fjärrkontroll](@hdmi).'),
      ('Gratis och Pro', 'Pilknappar, OK, bakåt, hem, volym, kanaler, siffror, tangentbord, att öppna appar, att byta ingångar och att slå på eller stänga av är gratis, utan reklam och utan prenumeration. Mando TV Pro är ett valfritt engångsköp för extrafunktioner.'),
    ],
    marca=None,
    faq=[
      ('Behöver jag appen Amazon Fire TV?', 'Nej. Mando TV ansluter via ditt wifi till Fire TV med PIN. Du behöver inget Amazon-konto på mobilen.'),
      ('Fungerar det med tv med Fire TV och med Fire TV Stick?', 'Ja, det är precis det det är gjort för. Stödet är nytt, håll appen uppdaterad och berätta för oss om modeller som inte fungerar som väntat.'),
      ('Varför behöver jag en PIN?', 'Fire TV visar en 4-siffrig PIN för att bevisa att du sitter framför tv:n. Ingen kan koppla utan att se skärmen.'),
    ]),
  dict(clave='firetv-lost', corto='Borttappad Fire TV-fjärrkontroll', fecha='2026-11-23',
    titulo='Borttappad Fire TV-fjärrkontroll? Så hjälper mobilen',
    desc='Borttappad fjärrkontroll till Fire TV Stick? Styr den via wifi med mobilen, kopplad med en 4-siffrig PIN. Tips för nytt wifi och HDMI-CEC.',
    h1='Borttappad Fire TV-fjärrkontroll: så använder du mobilen',
    intro='Om fjärrkontrollen till din Fire TV Stick, Fire TV Cube eller smarta tv med Fire TV är borttappad eller har slutat fungera tar mobilen över styrningen, så länge Fire TV fortfarande är ansluten till ditt wifi. Kopplingen sker med en 4-siffrig PIN på skärmen, så du behöver aldrig den gamla fjärrkontrollen för det.',
    pasos=[
      'Slå på tv:n med knappen på apparaten. En isatt Fire TV Stick eller Cube vaknar oftast med; med HDMI-CEC aktiverat byter tv:n ofta automatiskt till dess ingång.',
      'Visar tv:n en annan ingång, byt med ingångs- eller källknappen på tv:n. Se [Byt ingång utan fjärrkontroll](@hdmi).',
      'Anslut mobilen till samma wifi som Fire TV.',
      'Ladda ner Mando TV och öppna appen. Din Fire TV dyker upp i listan. Tryck på den.',
      'Tv:n visar en 4-siffrig PIN. Skriv in den i Mando TV. Det gör du bara en gång.',
      'Använd pilknapparna, OK, bakåt, hem, volym, uppspelningsknapparna och tangentbordet på mobilen.',
    ],
    extra=[
      ('Testa först tv:ns fjärrkontroll (HDMI-CEC)', 'Många tv-fjärrkontroller kan styra en Fire TV Stick via HDMI-CEC. Om Fire TV-gränssnittet syns, tryck på pilarna och OK på tv:ns fjärrkontroll. Händer ingenting, slå på CEC i tv:ns inställningar (Anynet+ på Samsung, SIMPLINK på LG, BRAVIA Sync på Sony) och på Fire TV styrningen av HDMI-CEC-enheter i skärminställningarna ("Display & Sounds").'),
      ('Om du har bytt wifi', 'Utan fjärrkontroll kan du inte skriva in det nya wifi-lösenordet på Fire TV, men det finns en utväg: skapa på en andra mobil en hotspot med exakt samma namn och lösenord som ditt gamla wifi. Fire TV ansluter automatiskt till den. Anslut mobilen med Mando TV till den hotspoten, koppla med PIN-koden, gå sedan på Fire TV till Inställningar > Nätverk och välj ditt nya wifi. Anslut till sist även mobilen till det nya wifit.'),
      ('Koppla en ersättningsfjärrkontroll', 'De flesta nya Fire TV-fjärrkontroller kopplas genom att du håller in hemknappen i cirka 10 sekunder nära Fire TV. Om det inte fungerar, öppna Inställningar > Handkontroller och Bluetooth-enheter > Amazon Fire TV-fjärrkontroller > Lägg till ny fjärrkontroll. Den menyn når du också från mobilen med Mando TV.'),
      ('Fire TV inbyggd i tv:n', 'På tv med inbyggd Fire TV fungerar samma steg, eftersom tv:n själv är Fire TV.'),
      ('Innan du börjar', 'Stödet för Fire TV är nytt i Mando TV. Uppdatera appen först. Om din modell inte reagerar som väntat, skriv till oss via [hjälpsidan](@soporte) och ange modellen.'),
      ('Gratis och Pro', 'Fjärrkontrollen kan du ladda ner och använda gratis, utan reklam och utan prenumeration. Mando TV Pro är ett valfritt engångsköp för extrafunktioner.'),
    ],
    marca=('firetv', 'Fire TV-fjärrkontroll'),
    faq=[
      ('Kan jag styra en Fire TV Stick med mobilen utan fjärrkontrollen?', 'Ja, så länge Fire TV är på och ansluten till ditt wifi. Mando TV kopplar med den 4-siffriga PIN-koden på tv:n, så du behöver inte den gamla fjärrkontrollen.'),
      ('Fungerar det om Fire TV sitter på ett nytt wifi?', 'Inte direkt, eftersom mobilen och Fire TV måste sitta på samma nätverk. Få först Fire TV online igen med hotspot-tricket på den här sidan.'),
      ('Behöver jag appen Amazon Fire TV eller ett Amazon-konto?', 'Nej. Mando TV ansluter via ditt hemmanätverk med PIN och behöver inget eget konto.'),
    ]),
  dict(clave='turn-on', corto='Slå på tv:n utan fjärrkontroll', fecha='2026-11-23',
    titulo='Slå på tv:n utan fjärrkontroll (alla märken)',
    desc='Slå på tv:n utan fjärrkontroll: var knappen sitter på Samsung, LG, TCL, Hisense och Sony. Plus HDMI-CEC och mobiltrick.',
    h1='Så slår du på en tv utan fjärrkontroll',
    intro='Nästan varje tv har fortfarande en fysisk strömknapp. Den är bara väl gömd. Här ser du var den sitter på varje märke, plus två sätt att slippa leta nästa gång: HDMI-CEC från en konsol eller en streamingenhet, och att slå på tv:n från mobilen via wifi.',
    pasos=[
      'Titta under mitten av skärmen, precis bakom märkeslogotypen. Många tv har där en liten enda knapp eller en joystick som pekar nedåt.',
      'Sitter den inte där, känn dig fram på tv:ns baksida nära de nedre hörnen, sedan på vänstra och högra kanten.',
      'Tryck på knappen en gång. På många tv med bara en knapp öppnar ett kort tryck när den är på en liten meny för ingångar och volym, och ett långt tryck stänger av den.',
      'Fortfarande ingenting? Kontrollera nätsladden i båda ändarna och prova ett annat vägguttag. Lyser inte standby-lampan får tv:n ingen ström.',
      'När tv:n är på, ställ in den så att du slipper knappen: slå på HDMI-CEC och påslagning via nätverket, båda förklaras längre ner.',
    ],
    extra=[
      ('Var strömknappen sitter, per märke', 'Samsung: en styrknapp eller en joystick under mitten av skärmen eller på baksidan vid ett nedre hörn. LG: en joystickknapp under LG-loggan på de flesta modeller. TCL och Hisense: oftast en liten knapp under mitten av skärmen eller på baksidan nära ett nedre hörn. Sony: på baksidan eller på en sidokant, nere nära kanten. Placeringen varierar beroende på modell. Hittar du den inte, sök efter bruksanvisningen med modellnumret på etiketten på baksidan.'),
      ('Slå på tv:n från en konsol eller streamingenhet (HDMI-CEC)', 'Med HDMI-CEC påslaget slår en PlayStation, en Xbox, en Roku-spelare, en Fire TV Stick eller en Chromecast också på tv:n och byter till rätt ingång när du slår på den. Varje märke kallar inställningen något annat: Anynet+ på Samsung, SIMPLINK på LG, BRAVIA Sync på Sony och CEC på de flesta andra. Mer i [Slå på tv:n och byt till spelkonsolens HDMI](@console).'),
      ('Slå på tv:n från mobilen', 'Smarta tv kan väckas via wifi om du tillåter det en gång, och då slår Mando TV på dem från mobilen. På Samsung slår du på "Slå på med mobil" under Inställningar > Allmänt > Nätverk > Expertinställningar. På LG slår du på "Slå på tv med mobil" ([steg för steg](@lg-on)). På en Roku TV slår du på "Snabb tv-start" under Inställningar > System > Ström. På Google TV och Android TV, leta efter Wake on LAN eller "Väck via nätverk", om din modell har det. Det gör du en gång, med tv:n påslagen.'),
      ('Om du inte hittar någon knapp', 'Några nyare tv gömmer den enda knappen så bra att det verkar som om det inte finns någon. Leta efter en liten buckla eller ett ljussensorområde under skärmen: knappen sitter ofta alldeles intill. Via wifi kräver Mando TV att tv:n har varit på och ansluten en gång. Infrarött är undantaget: på en Android-mobil med infraröd sändare kan Mando TV slå på en tv som aldrig har ställts in, så länge du riktar mobilen mot tv:n. Infrarött är nytt och fungerar med märkena i appens kodlista.'),
      ('Gratis och Pro', 'Fjärrkontrollen kan du ladda ner och använda gratis, utan reklam och utan prenumeration. Mando TV Pro är ett valfritt engångsköp för extrafunktioner.'),
    ],
    marca=None,
    faq=[
      ('Kan jag slå på en tv med mobilen om jag aldrig har ställt in den?', 'Inte via wifi. En avstängd tv vaknar bara från nätverket om påslagning via nätverket var aktiverad tidigare. Första gången, använd knappen på tv:n. Undantaget är en Android-mobil med infraröd sändare: Mando TV kan slå på en tv utan inställning med infrarött om märket finns i kodlistan eller du väljer "Annat märke eller vet inte".'),
      ('Hur slår jag på en Samsung-tv utan fjärrkontroll?', 'Tryck på styrknappen under mitten av skärmen eller på baksidan vid ett nedre hörn. Slå sedan på "Slå på med mobil" så att mobilen kan slå på den nästa gång.'),
      ('Hur slår jag på en Roku TV utan fjärrkontroll?', 'Använd knappen på tv:n, oftast under mitten eller på baksidan. Slå sedan på "Snabb tv-start" under Inställningar > System > Ström så att Mando TV kan slå på den från mobilen.'),
      ('Varför slås min tv på av sig själv när jag slår på konsolen?', 'Det är HDMI-CEC. Det är praktiskt, och du kan stänga av det i tv:ns inställningar om du föredrar det.'),
    ]),
  dict(clave='sony', corto='Sony-fjärrkontroll', fecha='2026-11-23',
    titulo='Sony fjärrkontrollsapp för mobil och dator',
    desc='Mando TV styr Sony Bravia-tv med Google TV eller Android TV via wifi. Betastöd för modeller från 2013 till 2015 utan Android.',
    h1='Så styr du din Sony-tv med mobilen',
    intro='Nyare Sony Bravia Smart TV använder Google TV, äldre modeller från 2015 Android TV. Mando TV styr båda via ditt wifi från iPhone, Android-mobil eller Windows-dator. Appen ersätter originalfjärrkontrollen om den har tappats bort eller batterierna är slut.',
    pasos=[
      'Kontrollera att din Sony-tv visar startskärmen för Google TV eller Android TV. Det gäller de flesta Sony Bravia Smart TV från och med tillverkningsår 2015.',
      'Anslut mobilen och tv:n till samma wifi.',
      'Öppna Mando TV och tryck på din Sony-tv i listan.',
      'Skriv in koden med 6 tecken som tv:n visar på skärmen (bara första gången). Du behöver ingen fjärrkontroll för det.',
      'Använd pilknapparna, OK, bakåt, hem, volym och tangentbordet.',
    ],
    extra=[
      ('Slå på en Sony-tv från mobilen', 'Sony-modeller med Google TV eller Android TV kan väckas via nätverket om "Remote start" är aktiverat. Alternativet hittar du oftast under Inställningar > Nätverk och internet > Remote start (vägen kan skilja sig något beroende på modell). Tryck sedan på tv:n i Mando TV medan den är avstängd, så slår appen på den.'),
      ('Var strömknappen sitter på en Sony', 'På de flesta Bravia-tv sitter den på baksidan, nära det nedre vänstra eller högra hörnet, eller på en sidokant. Ett kort tryck slår på tv:n. Mer om det finns i [Slå på tv:n utan fjärrkontroll](@turn-on).'),
      ('Äldre Sony-tv', 'Sony Bravia-tv från 2013 till 2015 som inte använder Android stöds i Mando TV i betastatus. Det är nytt och kan fortfarande ha kantiga hörn. Tv:n visar en 4-siffrig PIN som du måste skriva in i appen. Andra Sony-tv utan Google TV eller Android TV stöds inte just nu.'),
      ('Gratis och Pro', 'Fjärrkontrollen kan du ladda ner och använda gratis, utan reklam och utan prenumeration. Mando TV Pro är ett valfritt engångsköp för extrafunktioner.'),
    ],
    marca='android',
    faq=[
      ('Fungerar Mando TV med Sony Bravia-tv?', 'Ja, med Sony-tv som använder Google TV eller Android TV. Det omfattar de flesta Sony Smart TV från och med tillverkningsår 2015.'),
      ('Behöver jag en Sony-app eller ett Google-konto?', 'Nej. Mando TV kopplas med koden på tv-skärmen och kräver inget konto.'),
      ('Fungerar det med äldre Sony Bravia-tv utan Android?', 'Ja, i betastatus, på Bravia-modeller från 2013 till 2015 utan Android. Kopplingen sker med en 4-siffrig PIN som visas på tv:n.'),
      ('Kan jag skriva från mobilen på min Sony-tv?', 'Ja. Tangentbordet är gratis och fungerar i YouTube, Netflix och tv:ns sökning.'),
    ]),
  dict(clave='tcl', corto='TCL-fjärrkontroll', fecha='2026-11-23',
    titulo='TCL fjärrkontrollsapp för mobil och dator',
    desc='Borttappad TCL-fjärrkontroll? De flesta TCL-tv använder Roku TV eller Google TV. Mando TV styr båda via wifi, utan konto och reklam.',
    h1='Så styr du din TCL-tv med mobilen',
    intro='TCL bygger tv:n, men programvaran är Roku TV eller Google TV (på äldre modeller Android TV). Mando TV styr båda systemen och fungerar som fjärrkontroll till din TCL-tv via wifi. Gratis, utan konto och reklam.',
    pasos=[
      'Ta reda på vilket system din TCL använder. Visar startskärmen ett enkelt rutnät av kanalrutor är det Roku TV. Ser den ut som Google TV eller Android TV med rader fulla av rekommendationer är det Google TV.',
      'Anslut mobilen och TCL-tv:n till samma wifi.',
      'Öppna Mando TV. Din TCL dyker upp i listan av sig själv. Tryck på den.',
      'På en TCL med Roku TV behövs inget mer. På en TCL med Google TV skriver du in koden med 6 tecken som tv:n visar på skärmen (bara första gången).',
      'Använd pilarna, OK, bakåt, hem, volym och tangentbord. Slå på tv:n från appen om du har aktiverat påslagning via nätverket (se nedan).',
    ],
    extra=[
      ('Slå på en TCL-tv från mobilen', 'På TCL Roku TV slår du på "Snabb tv-start" under Inställningar > System > Ström. På TCL Google TV, leta efter ett alternativ för Wake on LAN, "Väck via nätverk" eller fjärrstart i nätverks- eller energiinställningarna. En del modeller erbjuder inte det. Slå i så fall på tv:n med den fysiska strömknappen, oftast nere i mitten eller på baksidan.'),
      ('Om din TCL inte dyker upp', 'Kontrollera att mobilen och tv:n sitter på samma wifi. Routrar med separata 2,4 GHz- och 5 GHz-nät kan gömma enheter för varandra. Tillåt "Lokalt nätverk" för Mando TV i inställningarna på iPhone. Du kan också lägga till tv:n genom att skriva in dess IP-adress. Läs [Mobilen hittar inte tv:n](@not-found).'),
      ('Mer om din TCL', 'För TCL med Roku TV, se [Roku fjärrkontrollsapp](@roku), för TCL med Google TV eller Android TV [Android TV fjärrkontrollsapp](@android).'),
      ('Gratis och Pro', 'Pilknappar, OK, bakåt, hem, volym, kanaler, siffror, tangentbord, att öppna appar, att byta ingångar och att slå på eller stänga av är gratis, utan reklam och prenumeration. Mando TV Pro är ett valfritt engångsköp för extrafunktioner.'),
    ],
    marca=None,
    faq=[
      ('Fungerar Mando TV med alla TCL-tv?', 'Det fungerar med TCL-tv med Roku TV, Google TV eller Android TV, alltså med de flesta TCL Smart TV. En TCL som inte är en smart-tv går inte att styra via wifi.'),
      ('Behöver jag TCL-appen eller ett TCL-konto?', 'Nej. Mando TV ansluter direkt via ditt wifi hemma och behöver inget konto.'),
      ('Min TCL ber om en kod. Var finns den?', 'TCL-modeller med Google TV och Android TV visar en kod med 6 tecken på skärmen. Skriv in den exakt så i Mando TV. En TCL med Roku TV frågar inte efter någon kod.'),
    ]),
  dict(clave='hisense', corto='Hisense-fjärrkontroll', fecha='2026-11-23',
    titulo='Hisense fjärrkontrollsapp: vad som fungerar i mobilen',
    desc='Hisense-fjärrkontroll med Mando TV: styrning för VIDAA, Roku TV, Google TV och Fire TV via wifi. Ärlig översikt över vad som fungerar.',
    h1='Hisense fjärrkontrollsapp: vad som fungerar och inte',
    intro='Hisense-tv är inte likadana inuti. Beroende på modell använder de Hisenses egna system VIDAA, Roku TV, Google TV eller Fire TV. Mando TV fungerar som fjärrkontroll till Hisense på alla fyra systemen, med ett undantag på några nyare VIDAA-modeller. Här ser du hur du tar reda på vilket system du har och vad du kan vänta dig.',
    pasos=[
      'Kontrollera vilket system din Hisense använder. VIDAA är Hisenses eget gränssnitt. Roku TV visar ett rutnät av kanalrutor. Google TV visar rader med rekommendationer. Fire TV visar startskärmen för Fire TV med Amazon-rader.',
      'Anslut mobilen och Hisense-tv:n till samma wifi.',
      'Öppna Mando TV. Tv:n dyker upp i listan av sig själv. Tryck på den.',
      'VIDAA- och Fire TV-modeller kan visa en PIN med fyra siffror; Google TV visar en kod med sex tecken. Skriv in den i appen. Roku TV frågar inte efter något. Det gör du bara en gång.',
      'Använd pilarna, OK, bakåt, hem, volym och tangentbord från mobilen.',
    ],
    extra=[
      ('Hisense med Roku TV eller Google TV', 'De fungerar fullt ut som vilken annan Roku- eller Google TV-tv som helst. Detaljer på sidorna [Roku fjärrkontrollsapp](@roku) och [Android TV fjärrkontrollsapp](@android).'),
      ('Hisense med Fire TV', 'Stödet för Fire TV är nytt i Mando TV. Uppdatera appen till den senaste versionen från din butik. Hur kopplingen med PIN fungerar står på sidan [Fire TV-fjärrkontrollsapp](@firetv). Om något inte fungerar som väntat, skriv till oss via hjälpsidan och ange din modell.'),
      ('Hisense med VIDAA', 'De flesta VIDAA-modeller fungerar: knappar, volym, tangentbord, appar och ingångar. Några nyare VIDAA-modeller accepterar bara den officiella Hisense-appen. Mando TV upptäcker det vid anslutningen och säger det tydligt i stället för att tyst misslyckas. I så fall är Hisense-appen för din modell, knapparna på tv:n eller originalfjärrkontrollen rätt väg.'),
      ('Slå på en Hisense från mobilen', 'På Hisense Roku TV slår du på "Snabb tv-start" under Inställningar > System > Ström. På Google TV, leta efter ett alternativ för Wake on LAN eller "Väck via nätverk". Finns inget, använd strömknappen på tv:n.'),
      ('Gratis och Pro', 'Pilknappar, OK, bakåt, hem, volym, kanaler, siffertangenter, tangentbord, att öppna appar, att byta ingångar och att slå på eller stänga av är gratis, utan reklam och utan prenumeration. Mando TV Pro är ett valfritt engångsköp för extrafunktioner.'),
    ],
    marca=None,
    faq=[
      ('Fungerar Mando TV med Hisense VIDAA?', 'Ja, med de flesta VIDAA-modeller. Några nyare accepterar bara den officiella Hisense-appen; Mando TV upptäcker det och säger det till dig. Hisense-tv med Roku TV, Google TV eller Fire TV stöds också.'),
      ('Hur vet jag om min Hisense är Roku TV, Google TV eller Fire TV?', 'Titta på startskärmen. Roku TV har ett enkelt rutnät av rutor och en Roku-logotyp vid start. Google TV har rader med rekommendationer. Fire TV har startskärmen för Amazon Fire TV. Modellnamnet under Inställningar > Om ger också svar.'),
      ('Behöver jag ett Hisense- eller Google-konto?', 'Nej. Mando TV ansluter direkt via ditt wifi hemma och har inget eget konto.'),
    ]),
  dict(clave='philips', corto='Philips-fjärrkontroll', fecha='2026-11-23',
    titulo='Philips fjärrkontrollsapp: Roku TV, Google TV, Android TV',
    desc='Mando TV styr Philips-tv med Roku TV, Google TV eller Android TV via wifi, från mobilen eller datorn. Titan OS stöds inte.',
    h1='Styr Philips-tv med mobilen',
    intro='Philips-tv använder olika system beroende på land och tillverkningsår: Roku TV i USA, Google TV eller Android TV i många länder och Titan OS på några nyare europeiska modeller. Mando TV styr modellerna med Roku TV, Google TV och Android TV via wifi.',
    pasos=[
      'Kontrollera startskärmen. Roku TV visar ett rutnät av rutor. Google TV och Android TV visar rader med rekommendationer från Google. Titan OS har en egen startskärm.',
      'Anslut mobilen och tv:n till samma wifi.',
      'Öppna Mando TV och tryck på din Philips-tv i listan.',
      'Roku TV frågar inte efter något. Google TV och Android TV visar en kod med 6 tecken: skriv in den en gång i appen.',
      'Använd pilknapparna, OK, bakåt, hem, volym och tangentbord.',
    ],
    extra=[
      ('Philips Roku TV', 'Fungerar som vilken Roku-tv som helst. För att slå på den från mobilen, slå på "Snabb tv-start" under Inställningar > System > Ström. Mer på sidan [Roku fjärrkontrollsapp](@roku).'),
      ('Philips med Google TV eller Android TV', 'Omfattar många Ambilight-modeller. De kopplas med koden på skärmen. För att slå på dem från mobilen, leta i nätverks- eller energiinställningarna efter Wake on LAN eller "Väck via nätverk". På några modeller saknas det alternativet. Mer på sidan [Android TV fjärrkontrollsapp](@android).'),
      ('Äldre Philips-tv utan Android', 'Philips-tv från 2011 till 2015 som inte använder Android stöds i Mando TV i betan. Den är ny och behöver ingen kopplingskod.'),
      ('Philips med Titan OS', 'Titan OS är ett annat system som Mando TV inte styr idag, och det säger vi hellre rakt ut. Nyare Philips-modeller utan Android omfattas inte heller.'),
      ('Gratis och Pro', 'Fjärrkontrollen kan du ladda ner och använda gratis, utan reklam och utan prenumeration. Mando TV Pro är ett valfritt engångsköp för extrafunktioner.'),
    ],
    marca=None,
    faq=[
      ('Fungerar Mando TV med Philips-tv?', 'Med Philips-tv som använder Roku TV, Google TV eller Android TV, ja, och i betan med Philips-tv från 2011 till 2015 utan Android. Modeller med Titan OS stöds inte.'),
      ('Styr Mando TV Ambilight?', 'Mando TV är en fjärrkontroll: den skickar knapparna, så du kommer med pilarna och OK till Ambilight-inställningarna. Det finns inga separata Ambilight-kontroller.'),
      ('Behöver jag ett Philips- eller Google-konto?', 'Nej. Mando TV ansluter via ditt wifi hemma och behöver inget konto.'),
    ]),
]
OTRAS_GUIAS += [
  ('no-sub', 'En fjärrkontrollsapp utan prenumeration och utan reklam'),
  ('roku-app-alt', 'Alternativ till Roku-appen: en för alla tv-apparater'),
  ('lg-thinq', 'Alternativ till appen LG ThinQ för din LG-tv'),
  ('smartthings', 'Alternativ till SmartThings för Samsung-tv'),
  ('googletv-alt', 'Alternativ till Google TV-fjärrkontrollen i mobilen'),
  ('windows', 'Fjärrkontrollsapp för Windows-datorn'),
  ('iphone', 'Fjärrkontrollsapp för iPhone: en för alla tv-apparater'),
  ('firetv', 'Fire TV-fjärrkontroll för din mobil eller dator'),
  ('firetv-lost', 'Borttappad Fire TV-fjärrkontroll: så använder du mobilen'),
  ('turn-on', 'Så slår du på en tv utan fjärrkontroll'),
  ('sony', 'Så styr du din Sony-tv med mobilen'),
  ('tcl', 'Så styr du din TCL-tv med mobilen'),
  ('hisense', 'Hisense fjärrkontrollsapp: vad som fungerar och inte'),
  ('philips', 'Styr Philips-tv med mobilen'),
]
# <<< guías traídas del inglés
