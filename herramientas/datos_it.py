# Textos en italiano (Italia, "tu") de mandotv.app. Los usa generar_idiomas.py. Escritos para las búsquedas de Italia
# ("telecomando", "smartphone", "accendere la TV"), no son traducción literal. Las claves y las rutas están en idiomas_sitio.py.
# Los nombres de menús de las TV no se inventan: cuando no hay certeza se describe la opción y se añade entre paréntesis
# el nombre en inglés que muestran las TV.

# Opciones de las TV que se repiten en varios textos.
LG_OPC = "l'opzione per accendere la TV con il cellulare (in inglese \"TV On With Mobile\"), che si trova in Generali > Dispositivi > Dispositivi esterni (sui modelli più vecchi, in Connessione)"
LG_WIFI = "l'accensione via Wi-Fi (\"Turn on via Wi-Fi\")"
SAM_RUTA = "Impostazioni > Generali > Rete > Impostazioni expert (Expert Settings) e attiva l'opzione per accendere con un dispositivo mobile (\"Power On with Mobile\")"
SAM_PERM = "Impostazioni > Generali > Gestione dispositivi esterni > Gestione connessione dispositivi (\"Device Connection Manager\") e imposta Mando TV come consentito"
ROKU_APPS = "Impostazioni > Sistema > Impostazioni di sistema avanzate > Controllo tramite app mobili (\"Control by mobile apps\")"
ROKU_RAPIDO = "l'avvio rapido della TV (\"Fast TV start\") in Impostazioni > Sistema > Alimentazione"
AND_WOL = "\"Wake on LAN\" o un'opzione per accendere tramite rete"

UI = dict(
  locale='it_IT',
  aria_home='Mando TV, home', aria_main='Principale', nav_que='Funzioni', nav_ayuda='Assistenza', nav_contacto='Contatti',
  asunto='Ciao%20Mando%20TV', inicio='Home', privacidad='Privacy', aria_pie='Piè di pagina', aria_ruta='Percorso',
  aria_marcas='Marche e guide', hecho='Fatto in Cile',
  aviso="Mando TV è un'app indipendente: non è affiliata ai produttori di TV citati né a Google, Amazon o Roku, e non è approvata da loro. I marchi appartengono ai rispettivi proprietari e sono citati solo per indicare la compatibilità. Android TV e Google TV sono marchi di Google LLC.",
  bajar='Scarica gratis', descarga='Scarica su', anticipada='Accesso anticipato su',
  apple_aria="Scarica Mando TV gratis dall'App Store", ms_aria='Scarica Mando TV gratis dal Microsoft Store',
  gp_aria='Accesso anticipato a Mando TV su Google Play per Android', aria_desc='Scarica Mando TV',
  b_como_btn='Come collegarsi', b_tiendas_label='Disponibile negli store',
  b_nota="iPhone, iPad, Android e Windows. Download gratuito, senza pubblicità. Pro è un acquisto una tantum, senza abbonamento.",
  b_compat='TV compatibili', b_otras='Altre marche', b_otras_p="Mando TV controlla tutte queste marche con la stessa app:",
  g_guias='Guide', g_ver='Vedi i passaggi', g_pasos='Passo dopo passo', g_hazlo='Fallo con Mando TV',
  g_tiendas="Mando TV è un telecomando universale per la tua TV. Scaricalo gratis, senza pubblicità e senza account. Pro è un acquisto una tantum facoltativo, senza abbonamento. Per iPhone, iPad, Windows e Android:",
  g_nota='Android: accesso anticipato gratuito su Google Play. <a href="{enlace}">Partecipa in due passaggi</a> e aiutaci ad arrivare nello store.',
  g_mas_pagina='Più dettagli nella pagina {enlace}.', g_mas_marca='Più dettagli per marca:',
  g_faq='Domande frequenti', g_mas='Altre guide', g_todas='Tutte le guide', g_ayuda='Assistenza e supporto',
  g_idiomas='Questa guida in altre lingue',
)

PIE = [
  ('samsung', 'Telecomando Samsung'),
  ('lg', 'Telecomando LG'),
  ('roku', 'Telecomando Roku'),
  ('android', 'Telecomando Android TV'),
  ('guias', 'Tutte le guide'),
  ('lost-tv', 'Telecomando TV perso'),
  ('lost-lg', 'Telecomando LG perso'),
  ('lg-on', 'Accendere la TV LG con lo smartphone'),
  ('hdmi', 'Cambiare ingresso HDMI senza telecomando'),
  ('androidtv', 'Android TV senza telecomando'),
  ('console', "Accendere la TV e l'HDMI della console"),
  ('samsung-lost', 'TV Samsung senza telecomando'),
  ('roku-lost', 'Telecomando Roku perso'),
  ('roku-403', "L'app Roku non funziona"),
  ('androidtv-code', 'Codice di associazione Android TV'),
  ('not-found', 'Lo smartphone non trova la TV'),
  ('wifi', 'Smartphone come telecomando Wi-Fi'),
  ('pc', 'Controllare la TV dal PC'),
]
NOMBRE_OTRA = {'lg': 'App telecomando per LG', 'samsung': 'App telecomando per Samsung', 'roku': 'App telecomando per Roku',
               'android': 'App telecomando per Android TV e Google TV'}
PAGINA_MARCA = {'lg': 'app telecomando per LG', 'samsung': 'app telecomando per Samsung', 'roku': 'app telecomando per Roku',
                'android': 'app telecomando per Android TV'}

OTRAS_GUIAS = [
  ('lg-on', 'Come accendere la TV LG con lo smartphone'),
  ('lost-tv', 'Telecomando della TV perso: cosa fare'),
  ('lost-lg', 'Telecomando LG perso: usa lo smartphone'),
  ('hdmi', "Come cambiare ingresso HDMI su una TV senza telecomando"),
  ('androidtv', 'Android TV senza telecomando: usa lo smartphone'),
  ('console', "Come accendere la TV e passare all'HDMI della console senza telecomando"),
  ('samsung-lost', 'TV Samsung senza il telecomando originale: usa lo smartphone'),
  ('roku-lost', 'Telecomando Roku perso: usa lo smartphone'),
  ('roku-403', "L'app Roku non funziona: come risolvere l'errore 403"),
  ('androidtv-code', 'Android TV chiede un codice di associazione: cosa fare'),
  ('not-found', 'Lo smartphone non trova la TV: cosa controllare'),
  ('wifi', 'Come usare lo smartphone come telecomando via Wi-Fi'),
  ('pc', 'Come controllare la TV dal PC Windows'),
]

INDICE = dict(
  titulo='Guide: controllare la TV con lo smartphone | Mando TV',
  desc="Guide passo dopo passo per usare smartphone o PC come telecomando: accendere la TV, cambiare ingresso HDMI e risolvere i problemi di Samsung, LG e Roku.",
  h1='Guide: usa lo smartphone come telecomando della TV',
  intro='Passaggi semplici per collegare, accendere e risolvere i problemi del telecomando della tua TV Samsung, LG, Roku o Android TV con Mando TV.',
  h2_guias='Tutte le guide', h2_marcas='App telecomando per marca',
)

MARCAS = [
  dict(clave='lg', color='#e0457b', corto='LG',
    titulo='Telecomando LG sullo smartphone, app gratis | Mando TV',
    desc="Usa smartphone o PC come telecomando della TV LG webOS, via Wi-Fi. Tasti, tastiera, app, ingressi e accensione gratis; puntatore con Pro.",
    h1='Telecomando LG: app per il tuo smartphone',
    intro="Mando TV è un'app telecomando per TV LG: trasforma il tuo smartphone o il tuo computer, tramite il Wi-Fi di casa, nel telecomando della tua Smart TV LG con webOS. Ti salva se hai perso il telecomando, se le batterie sono scariche o se vuoi solo scrivere più in fretta.",
    compat='Smart TV LG con webOS (la maggior parte dei modelli LG Smart TV dal 2014). Funziona con TV LED, NanoCell, QNED e OLED. Le vecchie Smart TV LG con NetCast (dal 2011 al 2014, prima di webOS) hanno un nuovo supporto in beta: si abbinano con la chiave a 6 cifre mostrata dalla TV.',
    h2=dict(funciones='Cosa puoi fare con la tua TV LG', como='Come collegare la TV LG a Mando TV',
            encender='Accendere la TV LG dallo smartphone', preguntas='Domande su LG', guias='Guide per LG'),
    funciones=[
      ('Tutti i tasti', 'Frecce, OK, Indietro, Home, volume, canali, muto e riproduzione.'),
      ('Puntatore come il Magic Remote (Pro)', 'Sposta la freccia sullo schermo con il dito, come con il Magic Remote di LG.'),
      ('Tastiera', 'Scrivi su YouTube, Netflix o nel browser della TV con la tastiera dello smartphone.'),
      ('App e ingressi', 'Apri le tue app e passa a HDMI, TV in diretta, AirPlay o Screen Share.'),
      ('Uscita audio (Pro)', 'Passa dagli altoparlanti della TV alla tua soundbar.'),
      ('Accendere la TV', "Se è spenta, Mando TV la accende tramite la rete e si collega da sola."),
    ],
    pasos=[
      'Collega lo smartphone e la TV alla stessa rete Wi-Fi.',
      'Apri Mando TV: la tua TV LG compare da sola nell\'elenco. Toccala.',
      "Sullo schermo della TV compare un avviso che chiede l'autorizzazione. Accettalo con il telecomando di sempre (solo la prima volta).",
    ],
    encender="Sulla TV LG apri le Impostazioni e cerca " + LG_OPC + ". Attiva " + LG_WIFI + ". Se esiste l'opzione di avvio rapido (\"Quick Start+\" in inglese), attivala anche. Poi, quando tocchi la TV spenta in Mando TV, l'app ti chiede se vuoi accenderla e si collega da sola.",
    faq=[
      ('Mi serve il Magic Remote per usare Mando TV?', "Solo la prima volta, per accettare l'avviso sullo schermo. Poi basta lo smartphone."),
      ("Mando TV sostituisce l'app LG ThinQ?", "Per controllare la TV sì: non serve un account LG né registrare la TV. Mando TV si collega direttamente tramite il tuo Wi-Fi."),
      ('Posso accendere la mia TV LG con lo smartphone?', "Sì, se attivi sulla TV l'opzione per accenderla con il cellulare e ti sei collegato una volta a TV accesa."),
      ('Funziona con le vecchie TV LG di prima di webOS?', 'In beta sì, con le Smart TV LG NetCast dal 2011 al 2014. Si abbinano con la chiave a 6 cifre mostrata dalla TV. È una novità, quindi può avere ancora qualche imperfezione.'),
    ],
    guias=[('lg-on', 'Come accendere la TV LG con lo smartphone'),
           ('lost-lg', 'Telecomando LG perso: usa lo smartphone'),
           ('hdmi', 'Come cambiare ingresso HDMI su una TV senza telecomando'),
           ('guias', 'Tutte le guide per controllare la TV con lo smartphone')]),
  dict(clave='samsung', color='#3d7bff', corto='Samsung',
    titulo='Telecomando Samsung sullo smartphone, app | Mando TV',
    desc="Usa smartphone o PC come telecomando della TV Samsung Tizen, via Wi-Fi. Tasti, tastiera, app e accensione gratis; touchpad con Pro. Senza pubblicità.",
    h1='Telecomando Samsung: app per il tuo smartphone',
    intro="Mando TV è un'app telecomando per TV Samsung: trasforma il tuo smartphone o il tuo computer, tramite il Wi-Fi di casa, nel telecomando della tua Smart TV Samsung. Non serve un account Samsung né registrare la TV.",
    compat="Smart TV Samsung con Tizen, modelli dal 2016 in poi (serie come Crystal UHD, QLED, Neo QLED, The Frame e OLED).",
    h2=dict(funciones='Cosa puoi fare con la tua TV Samsung', como='Come collegare la TV Samsung a Mando TV',
            encender='Accendere la TV Samsung dallo smartphone', preguntas='Domande su Samsung', guias='Guide per Samsung'),
    funciones=[
      ('Tutti i tasti', 'Frecce, OK, Indietro, Home, volume, canali, muto e sorgente.'),
      ('Touchpad (Pro)', 'Fai scorrere il dito per muoverti nei menu senza cercare le frecce.'),
      ('Tastiera', 'Scrivi ricerche e password con la tastiera dello smartphone.'),
      ('App', 'Apri Netflix, YouTube, Prime Video e le altre app con un tocco.'),
      ('Accendere la TV', "Se è spenta, Mando TV la accende tramite la rete e si collega da sola."),
      ('Senza account', 'La connessione è diretta, tramite il tuo Wi-Fi, senza passare da Internet.'),
    ],
    pasos=[
      'Collega lo smartphone e la TV alla stessa rete Wi-Fi.',
      "Apri Mando TV: la tua TV Samsung compare da sola nell'elenco. Toccala.",
      'La TV chiede se consenti la connessione. Scegli "Consenti" con il telecomando (solo la prima volta).',
    ],
    encender="Sulla TV Samsung apri " + SAM_RUTA + ". Poi, quando tocchi la TV spenta in Mando TV, l'app ti chiede se vuoi accenderla e si collega da sola.",
    faq=[
      ("Ho rifiutato l'autorizzazione per sbaglio. Cosa faccio?", "Sulla TV vai in " + SAM_PERM + "."),
      ('Mando TV sostituisce SmartThings?', "Per controllare la TV sì, e senza account Samsung. Mando TV si collega direttamente tramite il tuo Wi-Fi."),
      ('Funziona con le TV Samsung più vecchie?', "Funziona con le TV Samsung con Tizen, modelli dal 2016 in poi. I modelli precedenti usano un altro sistema che non supportiamo ancora."),
    ],
    guias=[('samsung-lost', 'TV Samsung senza il telecomando originale: usa lo smartphone'),
           ('hdmi', 'Come cambiare ingresso HDMI su una TV senza telecomando'),
           ('guias', 'Tutte le guide per controllare la TV con lo smartphone')]),
  dict(clave='roku', color='#a77bff', corto='Roku',
    titulo='Telecomando Roku sullo smartphone, app gratis | Mando TV',
    desc="Usa smartphone o PC come telecomando della Roku TV o del dispositivo Roku, via Wi-Fi. Tasti, tastiera, canali, ingressi e accensione gratis.",
    h1='Telecomando Roku: app per il tuo smartphone',
    intro="Mando TV è un'app telecomando per Roku: trasforma il tuo smartphone o il tuo computer, tramite il Wi-Fi di casa, nel telecomando della tua Roku. Funziona con i televisori Roku TV e con i dispositivi Roku che si collegano in HDMI.",
    compat="Televisori Roku TV (TCL, Hisense, Philips, Sharp, JVC e altri) e dispositivi Roku (Express, Streaming Stick, Ultra).",
    h2=dict(funciones='Cosa puoi fare con la tua Roku', como='Come collegare la Roku a Mando TV',
            encender='Accendere la Roku dallo smartphone', preguntas='Domande su Roku', guias='Guide per Roku'),
    funciones=[
      ('Tutti i tasti', 'Frecce, OK, Indietro, Home, volume, muto, replay e riproduzione.'),
      ('Tastiera', 'Scrivi le ricerche nei canali Roku con la tastiera dello smartphone.'),
      ('Canali', 'Apri Netflix, YouTube e gli altri canali Roku con un tocco.'),
      ('Ingressi', "Su una Roku TV passa a HDMI, antenna o AV direttamente dall'app."),
      ('Accendere la TV', "Sulle Roku TV con avvio rapido, Mando TV le accende dallo smartphone."),
      ('Senza associazione', 'Roku non chiede nessun codice: toccala nell\'elenco e sei collegato.'),
      ('Far squillare il telecomando', 'Se il tuo telecomando Roku ha un altoparlante, come il Roku Voice Remote Pro, Mando TV lo fa squillare per aiutarti a ritrovarlo. È gratis e il Roku deve essere acceso.'),
    ],
    pasos=[
      'Collega lo smartphone e la Roku alla stessa rete Wi-Fi.',
      "Apri Mando TV: la tua Roku compare da sola nell'elenco. Toccala.",
      "Se non si collega, sulla Roku vai in " + ROKU_APPS + " e imposta l'accesso alla rete su Predefinito o Permissivo (nelle versioni più recenti del software Roku, imposta \"Control by mobile apps\" su \"Enabled\").",
    ],
    encender="Sulle Roku TV attiva " + ROKU_RAPIDO + ". I dispositivi Roku collegati a un'altra TV non si possono accendere così. Poi, quando tocchi la TV spenta in Mando TV, l'app ti chiede se vuoi accenderla e si collega da sola.",
    faq=[
      ('Funziona con la Roku Express o la Streaming Stick?', 'Sì. Tutti i dispositivi Roku e i televisori Roku TV si controllano allo stesso modo.'),
      ('Mando TV non trova la mia Roku. Cosa faccio?', "Controlla che siano entrambi sulla stessa rete Wi-Fi e che il controllo tramite app mobili non sia disattivato sulla Roku. Puoi anche aggiungerla digitando l'indirizzo IP."),
      ('Serve un account Roku?', 'No. Mando TV si collega direttamente tramite il tuo Wi-Fi.'),
    ],
    guias=[('roku-403', "L'app Roku non funziona (errore 403)"),
           ('roku-lost', 'Telecomando Roku perso: usa lo smartphone'),
           ('guias', 'Tutte le guide per controllare la TV con lo smartphone')]),
  dict(clave='android', color='#2fbf8f', corto='Android TV e Google TV',
    titulo='Telecomando Android TV sullo smartphone | Mando TV',
    desc="Usa smartphone o PC come telecomando Android TV (Sony, TCL, Xiaomi), via Wi-Fi. Tasti, app e accensione gratis; touchpad con Pro.",
    h1='Telecomando Android TV: app per il tuo smartphone',
    intro="Mando TV è un'app telecomando per Android TV: trasforma il tuo smartphone o il tuo computer, tramite il Wi-Fi di casa, nel telecomando della tua Android TV o Google TV. Funziona anche da un iPhone e da Windows.",
    compat="Televisori con Google TV o Android TV di Sony, Philips, TCL, Hisense, Sharp, Xiaomi, Toshiba, Panasonic, Haier, Skyworth, JVC, Thomson, Motorola, OnePlus, iFFALCON, Kogan, Vu e altre marche, oltre a Chromecast con Google TV, Google TV Streamer, onn. e Nvidia Shield. Alcune di queste marche vendono anche modelli con un altro sistema: se la tua TV mostra la schermata iniziale di Google TV o ha lo store Google Play, Mando TV la controlla.",
    h2=dict(funciones='Cosa puoi fare con la tua Android TV', como='Come collegare la Android TV a Mando TV',
            encender='Accendere la Android TV dallo smartphone', preguntas='Domande su Android TV', guias='Guide per Android TV'),
    funciones=[
      ('Tutti i tasti', 'Frecce, OK, Indietro, Home, volume, muto e riproduzione.'),
      ('Touchpad (Pro)', 'Fai scorrere il dito per muoverti rapidamente nei menu di Google TV.'),
      ('Tastiera', 'Scrivi ricerche e password con la tastiera dello smartphone.'),
      ('App', 'Apri YouTube, Netflix, Disney+ e le altre app con un tocco.'),
      ('Accendere la TV', "Sui modelli che si possono accendere tramite la rete, Mando TV accende la TV e si collega da sola."),
      ('iPhone, Android e PC', 'Funziona allo stesso modo da qualsiasi smartphone o computer.'),
    ],
    pasos=[
      'Collega lo smartphone e la TV alla stessa rete Wi-Fi.',
      "Apri Mando TV: la tua Android TV compare da sola nell'elenco. Toccala.",
      'La TV mostra un codice di 6 caratteri. Inseriscilo in Mando TV (solo la prima volta).',
    ],
    encender="Dipende dal produttore. Cerca nelle impostazioni di rete o di alimentazione l'opzione " + AND_WOL + ". Alcuni modelli non ce l'hanno. Poi, quando tocchi la TV spenta in Mando TV, l'app ti chiede se vuoi accenderla e si collega da sola.",
    faq=[
      ('Funziona con il Chromecast con Google TV?', "Sì, l'associazione si fa con il codice di 6 caratteri che compare sullo schermo."),
      ("Che differenza c'è con l'app Google TV?", "Mando TV non richiede un account Google, funziona anche da Windows e controlla TV LG, Samsung e Roku con la stessa app."),
      ('Il codice non compare sullo schermo. Cosa faccio?', "Chiudi Mando TV, riapri l'app e tocca di nuovo la TV. Verifica che la TV non sia in una modalità di risparmio energetico profondo."),
    ],
    guias=[('androidtv-code', 'Android TV chiede un codice di associazione: cosa fare'),
           ('androidtv', 'Android TV senza telecomando: usa lo smartphone'),
           ('guias', 'Tutte le guide per controllare la TV con lo smartphone')]),
]

GUIAS = [
  dict(clave='lost-tv', corto='Telecomando TV perso',
    titulo='Telecomando TV perso? Usa lo smartphone come telecomando',
    desc="Hai perso il telecomando della TV? Accendi la TV con il suo tasto e usa lo smartphone come telecomando. LG, Samsung, Roku, Android TV. Gratis.",
    h1='Telecomando della TV perso? Ecco cosa puoi fare',
    intro="Perdere il telecomando capita in tutte le case: sparisce proprio quando vuoi guardare qualcosa. La buona notizia è che lo smartphone può fare da telecomando, tramite il Wi-Fi di casa. Ecco cosa fare, in ordine.",
    pasos=[
      "Accendi la TV con il suo tasto fisico. Quasi sempre si trova in basso al centro, oppure dietro vicino a un angolo. A volte è un semplice pulsante, a volte un piccolo joystick.",
      'Collega il tuo smartphone alla stessa rete Wi-Fi della TV.',
      "Scarica Mando TV, che è gratis e non chiede un account, e aprila. La tua TV compare da sola nell'elenco. Toccala.",
      "Accetta la connessione in base alla tua marca. Su LG e Samsung la TV mostra un avviso: accettalo con il tasto o il joystick della TV stessa. Su Android TV e Google TV inserisci un codice di 6 caratteri che compare sullo schermo. Roku non chiede nulla.",
      'Fatto. Frecce, OK, Indietro, Home, volume, canali e tastiera sono gratis.',
      "Per la prossima volta, attiva nelle impostazioni della TV l'accensione tramite rete (la guida della tua marca è qui sotto) e potrai accendere la TV dallo smartphone senza toccarla.",
    ],
    extra=[
      ('Scegli la guida della tua marca', 'LG: [Telecomando LG perso](@lost-lg). Android TV e Google TV: [Android TV senza telecomando](@androidtv). Samsung: [TV Samsung senza telecomando](@samsung-lost). Roku: [Telecomando Roku perso](@roku-lost).'),
      ("Se la TV non si accende con il tasto", "Prima di cercare un altro telecomando, controlla che il cavo sia ben inserito e che la presa abbia corrente. Se il tasto della TV non fa nulla, il problema è della TV e non del telecomando."),
      ("Se il telecomando ha semplicemente smesso di funzionare", "Prova con batterie nuove. Per sapere se emette ancora il segnale, puntalo verso la fotocamera dello smartphone e premi un tasto: su molti telefoni vedrai una luce viola sullo schermo. Se la luce compare e la TV non risponde, forse il sensore della TV è coperto."),
      ("Se hai cambiato router e la TV ha perso il Wi-Fi", "Senza telecomando è più difficile collegare la TV alla nuova rete. La cosa più semplice è collegare la TV al router con un cavo di rete. Oppure crea una rete Wi-Fi con lo stesso nome e la stessa password di prima: di solito la TV si ricollega da sola."),
      ("Cosa è gratis e cosa è Pro", "Accendere e spegnere la TV, frecce, OK, volume, canali, numeri, tastiera, apertura delle app e cambio di ingresso sono gratis. Il touchpad, la voce e le routine fanno parte di Mando TV Pro, un acquisto una tantum senza abbonamento."),
    ],
    marca=None,
    faq=[
      ("Posso accendere la TV con lo smartphone se non l'ho mai collegata?", "Questa prima volta accendila con il tasto della TV. Dopo aver collegato lo smartphone e attivato l'accensione tramite rete nelle impostazioni della TV, potrai accenderla dall'app."),
      ('Devo comprare un telecomando nuovo?', "Non necessariamente. Con Mando TV hai gratis i tasti, il volume, la tastiera e l'accensione. Se preferisci comunque un telecomando fisico, cerca il modello esatto della tua TV."),
      ("Funziona se la TV non ha il Wi-Fi?", "No. Smartphone e TV devono essere sulla stessa rete Wi-Fi. Una TV che non è una Smart TV non si può controllare con Mando TV."),
    ]),
  dict(clave='lost-lg', corto='Telecomando LG perso',
    titulo='Telecomando LG perso? Usa lo smartphone | Mando TV',
    desc="Senza telecomando LG? Accendi la TV con il tasto, accetta l'avviso e usa lo smartphone come telecomando Wi-Fi. Senza account LG e senza pubblicità.",
    h1='Telecomando LG perso? Come usare lo smartphone',
    intro="Se hai perso il telecomando della tua TV LG o il Magic Remote non funziona più, lo smartphone lo sostituisce tramite Wi-Fi. Funziona sulle TV LG con webOS, cioè quasi tutte le Smart TV LG dal 2014. Non serve un account LG né l'app ThinQ.",
    pasos=[
      "Accendi la TV con il tasto in basso, sotto il logo LG, oppure con quello sul retro. Su molti modelli fa da joystick: premilo per aprire il menu e spostalo per scegliere.",
      'Collega il tuo smartphone alla stessa rete Wi-Fi della TV.',
      "Apri Mando TV e tocca la tua TV LG nell'elenco.",
      "La TV mostra un avviso che chiede l'autorizzazione. Accettalo con il joystick o il tasto della TV. Se hai già collegato questo smartphone, non lo richiede.",
      "Fatto. Frecce, OK, Indietro, Home, volume, canali e tastiera sono gratis. Il puntatore è una funzione Pro.",
      "Con l'app collegata, entra nelle Impostazioni con le frecce e OK e attiva " + LG_OPC + ". La guida [Come accendere la TV LG con lo smartphone](@lg-on) mostra dove trovarla.",
    ],
    extra=[
      ("Se la TV non mostra l'avviso", "L'autorizzazione potrebbe essere già salvata, oppure lo smartphone è su un'altra rete. Controlla che siano sulla stessa rete Wi-Fi e che la VPN sia disattivata. Se la TV non compare nell'elenco, leggi [Lo smartphone non trova la TV](@not-found)."),
      ('Se la TV ha perso il Wi-Fi', "Collega la TV al router con un cavo di rete e la userà da sola. Oppure crea una rete Wi-Fi con lo stesso nome e la stessa password di prima, perché di solito la TV si ricollega da sola."),
      ("Se la TV è rimasta su un altro ingresso", "Dallo smartphone tocca Ingressi e scegli l'HDMI. Più dettagli in [Come cambiare ingresso HDMI su una TV senza telecomando](@hdmi)."),
    ],
    marca='lg',
    faq=[
      ('Mi serve il Magic Remote per usare Mando TV?', "Ti serve solo qualcosa per accettare l'avviso la prima volta, e basta il tasto o il joystick della TV stessa. Poi usi solo lo smartphone."),
      ("Mi serve l'app LG ThinQ?", "No. Mando TV si collega direttamente tramite il tuo Wi-Fi e non chiede un account LG."),
      ('Posso spegnere e accendere la mia TV LG con lo smartphone?', "Spegnerla sì. Per accenderla devi aver attivato l'opzione per accenderla con il cellulare e esserti collegato una volta a TV accesa."),
    ]),
  dict(clave='hdmi', corto='HDMI senza telecomando',
    titulo='Cambiare ingresso HDMI senza telecomando (Samsung, LG)',
    desc="Cambiare ingresso HDMI senza telecomando su Samsung, LG o Roku: con il tasto della TV o con lo smartphone. Gratis per iniziare, senza pubblicità.",
    h1='Come cambiare ingresso HDMI su una TV senza telecomando',
    intro="La console o il dispositivo di streaming è pronto, ma la TV è rimasta su un altro ingresso e il telecomando non si trova. Per cambiare ingresso HDMI senza telecomando hai due opzioni: il tasto della TV stessa o il tuo smartphone. Ecco i passaggi per Samsung, LG e Roku.",
    pasos=[
      "Prova prima la cosa più semplice: accendi la console o il dispositivo. Se l'HDMI-CEC è attivo sulla TV (Anynet+ su Samsung, SIMPLINK su LG), passa da sola a quell'ingresso.",
      "Se non cambia, usa il tasto della TV stessa, in basso al centro o sul retro. Su molte TV Samsung e LG fa da joystick e apre un menu con Sorgente o Ingressi.",
      "Scegli l'ingresso in quel menu: HDMI 1, HDMI 2 e così via. Il numero è quello della presa a cui è collegato il cavo.",
      "Se preferisci lo smartphone, collegalo alla stessa rete Wi-Fi, apri Mando TV e tocca la tua TV.",
      "Su LG e Roku tocca Ingressi e scegli l'HDMI. Su Samsung, Ingressi invia alla TV il tasto Sorgente e scegli con le frecce e OK.",
      "Puoi anche usare le frecce e OK per raggiungere gli ingressi dalla schermata iniziale della TV. A seconda della marca e dell'anno si chiamano Sorgente, Dispositivi collegati o Ingressi. Su una Roku TV sono i riquadri HDMI della schermata iniziale.",
    ],
    extra=[
      ('Samsung', "Se il menu del tasto della TV non ha Sorgente, apri dallo smartphone il menu della schermata iniziale e cerca Sorgente o Dispositivi collegati a sinistra. Lo controlli con le frecce e OK di Mando TV, che sono gratis."),
      ('LG', "Premi il joystick della TV e cerca Ingressi. Con lo smartphone, in Mando TV, puoi anche aprire l'elenco delle sorgenti e toccare quella che vuoi."),
      ('Roku TV', "Nella schermata iniziale c'è un riquadro per ogni ingresso, come HDMI 1 o HDMI 2. Muoviti con le frecce ed entra con OK, gratis."),
      ("Se è una TV con Android TV o Google TV", "In Mando TV l'elenco delle sorgenti non esiste ancora per Android TV. Usa il tasto degli ingressi della TV stessa, oppure raggiungili con le frecce e OK dalla schermata iniziale. Se non hai il telecomando e vuoi collegarti, leggi [Android TV senza telecomando](@androidtv)."),
      ('Altro aiuto', "Se la TV non si accende nemmeno o non sai da dove cominciare, leggi [Telecomando della TV perso](@lost-tv). Per giocare con la console, la guida [Come accendere la TV e passare all'HDMI della console senza telecomando](@console) spiega il trucco dell'HDMI-CEC."),
    ],
    marca=None,
    faq=[
      ("Cambiare ingresso HDMI è gratis?", "Sì. L'elenco delle sorgenti di Mando TV è gratis, come accendere la TV e usare frecce, OK e volume. Puoi anche raggiungere gli ingressi dal menu della TV."),
      ("Come faccio a sapere quale ingresso HDMI usare?", "Guarda le prese HDMI della TV: ognuna ha un numero. Usa quella a cui è collegato il cavo della tua console o del tuo dispositivo."),
      ("E se la TV non si accende?", "Accendila con il suo tasto fisico. Se l'hai già collegata e hai attivato l'accensione tramite rete, puoi accenderla anche dallo smartphone."),
    ]),
  dict(clave='androidtv', corto='Android TV senza telecomando',
    titulo='Android TV senza telecomando: usa lo smartphone',
    desc="Hai perso il telecomando di Android TV o Google TV? Collega lo smartphone con il codice di 6 caratteri sullo schermo. Gratis, senza account né pubblicità.",
    h1='Android TV senza telecomando: come usare lo smartphone',
    intro="Se hai perso il telecomando della tua Android TV o Google TV, o le batterie sono scariche, lo smartphone lo sostituisce. La parte migliore è che per collegarsi non serve il telecomando: la TV mostra un codice sullo schermo e tu lo inserisci nello smartphone. Funziona su TV Sony, Philips, TCL, Hisense, Sharp e Xiaomi con Android TV, su Chromecast con Google TV e su Nvidia Shield.",
    pasos=[
      "Accendi la TV con il suo tasto fisico. Quasi sempre si trova in basso al centro, oppure dietro vicino a un angolo.",
      'Collega il tuo smartphone alla stessa rete Wi-Fi della TV.',
      "Scarica Mando TV, che è gratis e non chiede un account Google, e aprila. Tocca la tua TV nell'elenco.",
      "La TV mostra un codice di 6 lettere e numeri. Inseriscilo nello smartphone e tocca Associa. Per questo non ti serve il telecomando.",
      "Ora puoi usare frecce, OK, Indietro, Home, volume, muto e tastiera. Sono gratis, come l'elenco delle app. Il touchpad è Pro.",
      "Per accenderla dallo smartphone la prossima volta, cerca nelle impostazioni di rete o di alimentazione della TV l'opzione " + AND_WOL + ".",
    ],
    extra=[
      ("Se la TV non si accende dallo smartphone", "Non tutte le Android TV si possono accendere tramite la rete; dipende dal produttore e dal modello. Se la tua non ha questa opzione, accendila con il tasto della TV e continua dallo smartphone. Puoi spegnerla dall'app."),
      ('Chromecast con Google TV, Google TV Streamer e Shield', "Si collegano allo stesso modo: stessa rete Wi-Fi, tocca il dispositivo nell'elenco e inserisci il codice. Se la TV mostra un altro ingresso, passa all'ingresso HDMI a cui è collegato il dispositivo, come spiega [Come cambiare ingresso HDMI su una TV senza telecomando](@hdmi)."),
      ("Se il codice non compare o viene rifiutato", "Controlla che la TV sia davvero accesa e non in standby. Il codice cambia a ogni richiesta: vale solo l'ultimo. Trovi più dettagli in [Android TV chiede un codice di associazione](@androidtv-code)."),
      ("App di Google o Mando TV", "Google ha la sua app, che richiede un account Google. Mando TV non richiede un account, funziona anche da Windows e controlla TV LG, Samsung e Roku con la stessa app."),
    ],
    marca='android',
    faq=[
      ("Mi serve il telecomando per associare lo smartphone?", "No. Il codice compare sullo schermo della TV e lo inserisci nello smartphone. Basta accendere la TV, se serve con il tasto della TV stessa."),
      ('Funziona con una Hisense?', "Sulle TV Hisense con Android TV o Google TV sì. Le TV Hisense con un altro sistema non sono compatibili."),
      ("Posso scrivere con la tastiera dello smartphone?", "Sì. La tastiera è gratis e serve per cercare su YouTube, Netflix e le altre app."),
    ]),
  dict(clave='lg-on', corto='Accendere TV LG con lo smartphone',
    titulo='Accendere la TV LG con lo smartphone (passo dopo passo)',
    desc="Accendi la TV LG con lo smartphone via Wi-Fi: attiva l'opzione per accenderla con il cellulare e usa Mando TV. Guida passo dopo passo, gratis.",
    h1='Come accendere la TV LG con lo smartphone',
    intro="Puoi accendere una TV LG con lo smartphone, ma prima devi attivare un'impostazione sulla TV. Fatto questo, lo smartphone accende la TV LG tramite la tua rete Wi-Fi, senza telecomando. Ci vogliono cinque minuti e lo fai una volta sola.",
    pasos=[
      'Collega lo smartphone e la TV LG alla stessa rete Wi-Fi.',
      "Sulla TV apri le Impostazioni e cerca " + LG_OPC + ".",
      "Attiva " + LG_WIFI + ". Se la TV è collegata con un cavo di rete, attiva invece l'opzione del cavo.",
      'Se la tua TV ha l\'opzione di avvio rapido (\"Quick Start+\" in inglese), attivala anche.',
      "Con la TV accesa, apri Mando TV sullo smartphone e tocca la tua TV LG nell'elenco. Accetta l'avviso che compare sullo schermo. È così che l'app impara a svegliarla.",
      "Spegni la TV e prova: tocca la TV in Mando TV e l'app ti chiede se vuoi accenderla.",
    ],
    extra=[
      ("Se non si accende", "La TV doveva essere sulla stessa rete Wi-Fi quando è stata spenta. Controlla che l'opzione sia ancora attiva e che lo smartphone sia su quella stessa rete. Se hai cambiato router, collegati ancora una volta con la TV accesa."),
    ],
    marca='lg',
    faq=[
      ("Posso accendere la TV LG con lo smartphone se non l'ho mai collegata?", "No. Prima devi attivare sulla TV l'opzione per accenderla con il cellulare e collegarti una volta con Mando TV mentre la TV è accesa."),
      ("Mi serve l'app LG ThinQ?", "No. Mando TV si collega direttamente tramite il tuo Wi-Fi e non chiede un account LG."),
      ('Funziona con i dati mobili?', 'No. Smartphone e TV devono essere sulla stessa rete Wi-Fi.'),
    ]),
  dict(clave='console', corto='TV e console senza telecomando',
    titulo='Senza telecomando? Accendi la TV e passa all\'HDMI',
    desc="Giorno di gioco e telecomando sparito? Accendi la TV e passa all'ingresso HDMI di PS5 o Xbox dallo smartphone. Gratis e senza pubblicità.",
    h1="Come accendere la TV e passare all'HDMI della console senza telecomando",
    intro="Giorno di uscita di GTA VI, la console è pronta e il telecomando della TV è sparito tra i cuscini del divano. Succede più spesso di quanto si pensi. Con Mando TV il tuo smartphone accende la TV e la porta sull'ingresso della tua PlayStation o Xbox, tramite il Wi-Fi di casa.",
    pasos=[
      'Collega il tuo smartphone alla stessa rete Wi-Fi della TV.',
      "Apri Mando TV e tocca la tua TV nell'elenco (Samsung, LG, Roku o Android TV).",
      "Se la TV è spenta, tocca Accendi. Funziona se l'accensione tramite rete è attiva sulla TV. Se non l'hai mai attivata, questa volta accendi la TV con il tasto della TV stessa e attivala per la prossima.",
      "Accendi la console. Se l'HDMI-CEC è attivo (vedi il trucco gratuito qui sotto), la TV passa da sola al suo ingresso.",
      "Se non cambia, tocca Ingressi in Mando TV e scegli l'ingresso HDMI a cui è collegata la console: HDMI 1, HDMI 2 e così via.",
      "Per il volume usa i grandi tasti dell'app mentre giochi.",
    ],
    extra=[
      ("Il trucco gratuito: lascia che sia la console a cambiare la TV", "PS5 e Xbox possono accendere la TV e passare al loro ingresso HDMI appena si avviano, grazie all'HDMI-CEC. Su PS5 si trova in Impostazioni > Sistema > HDMI > Attiva il collegamento dei dispositivi HDMI. Su Xbox apri Impostazioni > Generali > Opzioni TV e schermo e cerca l'opzione di controllo dei dispositivi. Sulla TV la funzione ha un nome diverso a seconda della marca: Anynet+ su Samsung, SIMPLINK su LG, e BRAVIA Sync o controllo HDMI su altre."),
      ("Se la TV resta su un'altra schermata", "Se la console è accesa ma la TV mostra ancora l'antenna o un'app, non ha cambiato ingresso. Dallo smartphone tocca Ingressi e scegli l'HDMI della console. Puoi anche usare le frecce e OK per raggiungere gli ingressi della TV, oppure il tasto della TV stessa, e scegli l'ingresso HDMI. Il numero è quello della presa a cui hai collegato il cavo della console."),
      ("Se è una Roku TV", "Il tasto fisico della TV, di solito in basso al centro o sul retro, la accende. Da lì lo smartphone fa il resto."),
    ],
    marca=None,
    faq=[
      ('Mando TV c\'entra qualcosa con GTA VI?', "No. Mando TV non è affiliata a Rockstar Games né a Take-Two. Ti aiuta solo a non perdere tempo di gioco perché non trovi il telecomando della TV."),
      ("Cambiare ingresso HDMI è gratis?", "Sì. L'elenco delle sorgenti di Mando TV è gratis, come accendere la TV e usare frecce, OK e volume. Puoi anche lasciare che la console cambi ingresso da sola con l'HDMI-CEC."),
      ('Funzionerà con la mia TV?', "Funziona con TV Samsung, LG, Roku e Android TV sulla stessa rete Wi-Fi. Se la tua è di un'altra marca, il trucco dell'HDMI-CEC può comunque aiutare."),
      ("Posso usarla per giocare a GTA VI (GTA 6) su PS5 o Xbox?", "Mando TV non tocca né la console né il gioco. Si occupa solo di far trovare la TV accesa e sull'ingresso HDMI giusto, così puoi sederti e giocare."),
    ]),
  dict(clave='samsung-lost', corto='TV Samsung senza telecomando',
    titulo='Telecomando Samsung perso? Usa lo smartphone',
    desc="Telecomando Samsung perso o rotto? Usa lo smartphone come telecomando Wi-Fi sulle TV Tizen. Semplice con Mando TV, gratis e senza pubblicità.",
    h1='TV Samsung senza il telecomando originale: usa lo smartphone',
    intro="Se hai perso il telecomando della tua TV Samsung o non funziona più, puoi usare lo smartphone come telecomando tramite il Wi-Fi. Funziona sulle TV Samsung con Tizen, modelli dal 2016 in poi.",
    pasos=[
      "Accendi la TV con il suo tasto fisico. Sulla maggior parte dei modelli si trova in basso o sul retro, a volte come un piccolo joystick.",
      "Controlla che la TV sia collegata al tuo Wi-Fi e che lo smartphone sia sulla stessa rete.",
      "Apri Mando TV sullo smartphone. La tua TV Samsung compare da sola nell'elenco. Toccala.",
      "La TV ti chiede di accettare la connessione. Sulla maggior parte dei modelli la accetti con i tasti fisici della TV o con il joystick sul retro.",
      "Fatto, ora puoi usare lo smartphone come telecomando. I tasti, la tastiera e le app sono gratis; il touchpad è una funzione Pro.",
      "Per accenderla dallo smartphone la prossima volta, vai in " + SAM_RUTA + ".",
    ],
    extra=[
      ("Se la TV non chiede l'autorizzazione", "L'autorizzazione potrebbe essere già salvata, oppure la TV è su un'altra rete Wi-Fi. Chiudi Mando TV e riaprila con la TV accesa. Se la TV è precedente al 2016 usa un altro sistema che non è ancora supportato."),
      ("Se hai rifiutato l'autorizzazione per sbaglio", "Sulla TV vai in " + SAM_PERM + ". Se lo smartphone non trova ancora la TV, leggi [Lo smartphone non trova la TV](@not-found)."),
    ],
    marca='samsung',
    faq=[
      ("Come accetto la connessione se non ho il telecomando?", "Sulla maggior parte dei modelli la accetti con i tasti fisici della TV o con il joystick sul retro. Se il tuo modello non ha tasti, scrivi a hola@mandotv.app e ti aiutiamo."),
      ('Mando TV richiede un account Samsung?', 'No. Si collega direttamente tramite il tuo Wi-Fi, senza account Samsung.'),
      ('Funziona con la mia TV Samsung più vecchia?', 'Funziona con le TV Samsung con Tizen, modelli dal 2016 in poi.'),
    ]),
  dict(clave='wifi', corto='Smartphone come telecomando Wi-Fi',
    titulo='Smartphone come telecomando della TV via Wi-Fi',
    desc="Collega lo smartphone alla TV via Wi-Fi e usalo come telecomando Samsung, LG, Roku e Google TV. Passaggi per marca con Mando TV. Gratis.",
    h1='Come collegare lo smartphone alla TV via Wi-Fi come telecomando',
    intro="Bastano lo smartphone e la TV sulla stessa rete Wi-Fi, più un'app telecomando. Mando TV trova la tua TV da sola e funziona con Samsung, LG, Roku, Google TV e Android TV.",
    pasos=[
      'Collega lo smartphone e la TV alla stessa rete Wi-Fi.',
      "Apri Mando TV. La tua TV compare da sola nell'elenco. Toccala.",
      'Accetta la connessione in base alla tua marca (i dettagli di ciascuna sono qui sotto).',
      'Controlla la TV con i tasti o la tastiera dello smartphone. Il touchpad è una funzione Pro.',
    ],
    extra=[
      ('Samsung', "La TV chiede se consenti la connessione. Accettala sullo schermo la prima volta. Funziona con Tizen, dal 2016 in poi. Per accenderla dallo smartphone, vai in " + SAM_RUTA + "."),
      ('LG', "La TV mostra un avviso che chiede l'autorizzazione. Accettalo la prima volta. Per accenderla dallo smartphone cerca nelle Impostazioni " + LG_OPC + " e attiva " + LG_WIFI + "."),
      ('Roku', "Roku non chiede l'associazione: toccala nell'elenco e sei collegato. Per accenderla attiva " + ROKU_RAPIDO + "."),
      ('Google TV e Android TV', "La TV mostra un codice sullo schermo. Inseriscilo in Mando TV la prima volta. Per accenderla cerca nelle impostazioni l'opzione " + AND_WOL + "."),
    ],
    marca=None,
    faq=[
      ("Mi serve Internet per usare lo smartphone come telecomando?", "Servono lo smartphone e la TV sulla stessa rete Wi-Fi. Mando TV si collega direttamente alla TV tramite quella rete."),
      ("Perché la mia TV non compare nell'elenco?", "Controlla che la TV sia accesa e che lo smartphone non usi i dati mobili né un'altra rete Wi-Fi. Alcuni router hanno una rete ospiti che isola i dispositivi."),
      ('Posso usare Mando TV da un iPhone o da uno smartphone Android?', "Sì su iPhone e iPad: l'app è già sull'App Store. È anche sul Microsoft Store per Windows. Android arriva presto: puoi unirti all'accesso anticipato gratuito su Google Play."),
    ]),
  dict(clave='pc', corto='Controllare la TV dal PC',
    titulo='Controllare la TV dal PC Windows (gratis)',
    desc="Usa il PC Windows come telecomando della TV Samsung, LG, Roku o Google TV via Wi-Fi. Tasti, tastiera e app gratis; scorciatoie con Pro.",
    h1='Come controllare la TV dal PC Windows',
    intro="Se passi la giornata al computer, non serve cercare il telecomando: Mando TV per Windows controlla la tua TV Samsung, LG, Roku, Google TV o Android TV tramite il Wi-Fi di casa. Comodo per cambiare app, alzare il volume o scrivere su YouTube con la tastiera del PC.",
    pasos=[
      'Scarica Mando TV gratis dal Microsoft Store sul tuo computer con Windows 10 o 11.',
      "Controlla che computer e TV siano sulla stessa rete (Wi-Fi o cavo, ma dallo stesso router).",
      "Apri Mando TV: la tua TV compare da sola nell'elenco. Toccala o fai clic.",
      "Accetta la connessione sullo schermo della TV la prima volta (su Google TV e Android TV inserisci il codice che mostra la TV).",
      "Fatto: usa i tasti o la tastiera per scrivere nel campo di ricerca della TV. Il touchpad è una funzione Pro.",
    ],
    extra=[
      ('Scorciatoie da tastiera del PC (Pro)', "Con Mando TV Pro controlli la TV con la tastiera del computer: frecce per muoverti, Invio per OK, Backspace o Esc per tornare indietro, + e - per il volume, M per il muto e Spazio per la pausa."),
      ('Mini telecomando sempre in primo piano (Pro)', "Tieni una piccola finestra con il telecomando sempre visibile mentre lavori o giochi al PC."),
      ('Parlare alla TV dal PC (Pro)', 'Con Mando TV Pro dai ordini alla TV con il microfono del PC: "apri YouTube", "alza il volume" o "spegni tra 30 minuti", come ti viene. Su Windows la voce viene riconosciuta sul PC stesso: non serve Internet, non devi cambiare nulla nelle impostazioni di Windows e funziona nelle 6 lingue dell\'app. Ciò che dici non esce dal PC e non viene conservato. Solo sui processori molto vecchi l\'app ripiega sulla digitazione vocale di Windows, che richiede il riconoscimento vocale online attivo nelle impostazioni della privacy e la lingua Italiano (Italia) aggiunta in Windows. In quel caso, se manca qualcosa, l\'app te lo dice e apre l\'impostazione con un pulsante.'),
    ],
    marca=None,
    faq=[
      ("Servono un cavo o il Bluetooth per controllare la TV dal PC?", "No. Mando TV si collega tramite la rete di casa: PC e TV devono solo essere sullo stesso router."),
      ('Funziona con tutte le TV?', "Funziona con TV Samsung con Tizen (dal 2016 in poi), LG con webOS, Roku e Google TV o Android TV (Sony, Philips, TCL, Hisense, Sharp, Xiaomi, Toshiba, Panasonic, Haier, Skyworth e altre)."),
      ('Quanto costa?', "I tasti, la tastiera e l'accensione tramite rete sono gratis e senza pubblicità. Mando TV Pro è un acquisto una tantum, senza abbonamento, per extra come il touchpad, le scorciatoie da tastiera del PC e il mini telecomando."),
      ('Perché il microfono non mi capisce su Windows?', "Controlla che la voce sia attiva (è una funzione Pro) e che il microfono del PC funzioni in Windows. Sulla maggior parte dei PC la voce viene riconosciuta sul dispositivo stesso, senza Internet. Solo sui processori molto vecchi l'app usa la digitazione vocale di Windows: allora controlla che il riconoscimento vocale online sia attivo nelle impostazioni della privacy di Windows e che Windows abbia l'italiano (Italia) nelle impostazioni della lingua. Mando TV usa questa lingua solo mentre ascolta."),
    ]),
  dict(clave='roku-403', corto="L'app Roku non funziona",
    titulo="L'app Roku non funziona? Risolvi l'errore 403",
    desc="Lo smartphone si collega alla Roku ma i tasti non fanno nulla? Attiva il controllo tramite app mobili sulla Roku in 5 passaggi.",
    h1="L'app Roku non funziona: come risolvere",
    intro="Se lo smartphone trova la Roku e si collega, ma nessun tasto fa nulla, quasi sempre è un'impostazione della Roku stessa che blocca le app telecomando. Le versioni più recenti di Roku sono più restrittive per impostazione predefinita. Si risolve in un minuto dal menu della Roku.",
    pasos=[
      'Sulla Roku premi Home e vai in Impostazioni.',
      'Apri Sistema e poi Impostazioni di sistema avanzate.',
      'Entra in "Controllo tramite app mobili" ("Control by mobile apps"). Su alcuni modelli si chiama "Controllo esterno".',
      'In "Accesso alla rete" ("Network access") scegli Predefinito o Permissivo. Se sul tuo modello è solo un interruttore, lascialo attivo.',
      'Torna a Mando TV sullo smartphone e tocca la tua Roku. Ora i tasti rispondono.',
    ],
    extra=[
      ("Come capire se è il tuo problema", "Il segno è netto: lo smartphone vede la Roku nell'elenco e si collega, ma non succede nulla quando tocchi un tasto. Internamente la Roku risponde con l'errore 403, che significa \"vietato\". Mando TV lo rileva alla connessione e ti mostra questi stessi passaggi sullo schermo."),
      ('Predefinito o Permissivo, quale scegliere?', "Predefinito basta: accetta i comandi che arrivano dalla rete di casa, che è ciò di cui ha bisogno un telecomando. Permissivo è più aperto e serve solo su reti insolite."),
      ("Se non hai il telecomando della Roku", "Quando l'impostazione è su Disattivato, si può cambiare solo con il telecomando fisico della Roku. Fattene prestare uno per cambiarla una volta; poi puoi fare tutto con lo smartphone. Leggi anche [Telecomando Roku perso](@roku-lost)."),
    ],
    marca='roku',
    faq=[
      ("Perché la mia Roku non risponde più se prima funzionava?", "Un aggiornamento della Roku può rendere questa impostazione più restrittiva. Non è un problema del tuo smartphone né del Wi-Fi: basta consentire di nuovo il controllo tramite app."),
      ('Riguarda sia le Roku TV sia i dispositivi Roku?', "Sì. L'impostazione si trova nello stesso menu sui dispositivi Roku e sui televisori Roku TV."),
      ('Si può lasciare su Predefinito senza rischi?', "Sì. Accetta solo i comandi dei dispositivi della tua rete di casa."),
    ]),
  dict(clave='not-found', corto='Lo smartphone non trova la TV',
    titulo='Lo smartphone non trova la TV? 6 controlli da fare',
    desc="L'app telecomando non trova la TV o si disconnette? Controlla Wi-Fi, VPN e accesso alla rete locale. Samsung, LG, Roku, Android TV.",
    h1='Lo smartphone non trova la TV: cosa controllare',
    intro="Apri l'app telecomando e l'elenco è vuoto, oppure la TV compare ma la connessione cade. Quasi sempre è la rete, non la TV. Controlla questi punti in ordine: il primo risolve la maggior parte dei casi.",
    pasos=[
      "Guarda su quale Wi-Fi è lo smartphone e su quale è la TV. Deve essere la stessa rete, con lo stesso nome. Una rete ospiti non funziona, perché isola i dispositivi.",
      "Disattiva la VPN dello smartphone, se ne usi una. Con la VPN attiva lo smartphone esce da un'altra rete e non vede i dispositivi di casa, oppure la connessione cade dopo pochi secondi.",
      "Disattiva per un momento i dati mobili. Alcuni telefoni passano da soli dal Wi-Fi ai dati mobili quando il segnale è debole.",
      "Accendi la TV e aspetta che finisca di avviarsi. Una TV spenta non risponde alla ricerca.",
      "Su iPhone controlla che l'app abbia il permesso Rete locale: Impostazioni > Privacy e sicurezza > Rete locale.",
      "Se ancora non compare, aggiungila a mano: in Mando TV tocca \"Aggiungi tramite IP\" e inserisci l'indirizzo IP della TV.",
    ],
    extra=[
      ("Lasciati guidare dall'app", "Nell'elenco delle TV c'è un pulsante per il caso in cui la TV non compaia. L'app controlla passo dopo passo le cause più comuni (stessa rete Wi-Fi, VPN, permesso per la rete locale e altro) e, dopo ogni correzione, mostra un pulsante per ricontrollare. Questo assistente è gratuito."),
      ("Dove trovare l'indirizzo IP della TV", "Si trova nel menu di rete della TV e cambia un po' a seconda del modello. Su LG: Impostazioni, Rete, Connessione Wi-Fi, impostazioni avanzate. Su Samsung: Impostazioni, Generali, Rete, Stato della rete, Impostazioni IP. Su Roku: Impostazioni, Rete, Informazioni. Su Android TV e Google TV: Impostazioni, Rete e Internet, poi tocca la tua rete. È un numero come 192.168.1.86."),
      ("Se compare ma la connessione cade", "Quando la connessione cade dopo pochi secondi, la causa di solito è nello smartphone: una VPN, il passaggio a un'altra rete Wi-Fi o il risparmio energetico. Disattiva la VPN, resta sullo stesso Wi-Fi e riprova."),
      ('Wi-Fi a 2,4 e a 5 GHz', "Non importa se lo smartphone è sulla rete a 5 GHz e la TV su quella a 2,4 GHz, purché vengano dallo stesso router. Se hai un ripetitore Wi-Fi e la TV ancora non compare, avvicina lo smartphone al router principale e riprova."),
    ],
    marca=None,
    faq=[
      ('Posso controllare la TV con i dati mobili?', "No. Il segnale del telecomando passa dal Wi-Fi di casa, quindi smartphone e TV devono essere sulla stessa rete."),
      ('Perché non funziona con la VPN attiva?', "Perché la VPN manda tutto il traffico dello smartphone su un'altra rete e lo smartphone non vede più i dispositivi di casa. Disattivala mentre usi il telecomando."),
      ("Funzionano il Bluetooth o l'infrarosso?", "Per le smart TV, Mando TV usa il Wi-Fi. Gli infrarossi funzionano solo sugli smartphone Android con emettitore a infrarossi e servono per le TV che non sono smart. Il Bluetooth non è ancora disponibile."),
    ]),
  dict(clave='androidtv-code', corto='Codice di associazione Android TV',
    titulo='Android TV chiede un codice di associazione: cosa fare',
    desc="La tua Android TV o Google TV mostra un codice di 6 caratteri quando colleghi lo smartphone. Come inserirlo e cosa fare se manca o viene rifiutato.",
    h1='Android TV chiede un codice di associazione: cosa fare',
    intro="La prima volta che colleghi lo smartphone a una Android TV o Google TV, la TV mostra sullo schermo un codice di 6 caratteri. È normale e succede una sola volta: serve a garantire che nessun altro possa controllare la tua TV. Ecco come inserirlo e cosa fare se non compare.",
    pasos=[
      "Accendi la TV e lascia visibile la schermata iniziale.",
      "Apri Mando TV sullo smartphone, sullo stesso Wi-Fi della TV, e tocca la tua TV nell'elenco.",
      "Guarda lo schermo della TV: compare un codice di 6 lettere e numeri.",
      "Inseriscilo nello smartphone esattamente come appare e tocca Associa. Le lettere vanno solo da A a F: un carattere tondo è quindi sempre il numero zero.",
      "Fatto. La TV memorizza il tuo smartphone e non richiede più il codice.",
    ],
    extra=[
      ("Se il codice non compare sulla TV", "Controlla che la TV sia davvero accesa e non in standby, e che lo smartphone sia sullo stesso Wi-Fi. Tocca di nuovo la TV sullo smartphone. Se ancora non compare, riavvia la TV: staccala per dieci secondi, ricollegala e riprova."),
      ("Se dice che il codice è sbagliato", "Il codice cambia a ogni richiesta. Se hai impiegato troppo o l'hai richiesto due volte, vale solo l'ultimo mostrato sullo schermo. Tocca di nuovo la TV sullo smartphone e inserisci il nuovo codice."),
      ("Se la TV chiede di nuovo il codice", "Succede quando la TV viene ripristinata alle impostazioni di fabbrica o quando cancelli i dati dell'app sullo smartphone. Associa di nuovo e resta salvato. Se non hai nessun telecomando, leggi [Android TV senza telecomando](@androidtv)."),
    ],
    marca='android',
    faq=[
      ('Quali TV usano questo codice?', "Quelle con Android TV o Google TV: Sony, Philips, TCL, Hisense, Sharp, Xiaomi, Chromecast con Google TV e molte altre."),
      ("Mi serve un account Google sullo smartphone?", "No. Basta il codice che compare sullo schermo."),
      ('È sicuro?', "Sì. Il codice dimostra che sei davanti alla TV: nessuno può associare un dispositivo senza vedere lo schermo."),
    ]),
  dict(clave='roku-lost', corto='Telecomando Roku perso',
    titulo='Telecomando Roku perso? Usa lo smartphone via Wi-Fi',
    desc="Telecomando Roku perso? Lo smartphone lo sostituisce via Wi-Fi. Passaggi semplici, anche se hai cambiato router e la Roku non ha più il Wi-Fi.",
    h1='Telecomando Roku perso: come usare lo smartphone',
    intro="Se hai perso il telecomando della Roku o non funziona più, lo smartphone lo sostituisce, finché la Roku è ancora collegata al tuo Wi-Fi. E se hai cambiato Wi-Fi o router, esiste una soluzione anche per questo.",
    pasos=[
      "Prima di tutto, prova a far squillare il telecomando. Se il tuo telecomando Roku ha un altoparlante, come il Roku Voice Remote Pro, apri Mando TV, collegati al Roku e usa l'opzione per far squillare il telecomando, così lo trovi. Funziona solo con i telecomandi Roku dotati di altoparlante, e il Roku deve essere acceso.",
      "Accendi la TV e lascia la Roku collegata. Non devi toccare nulla.",
      'Collega il tuo smartphone allo stesso Wi-Fi della Roku.',
      "Apri Mando TV. La Roku compare da sola nell'elenco. Toccala.",
      "Usa frecce, OK, Home e Indietro come con il tuo telecomando di sempre. La Roku non chiede nessun codice.",
      "Se i tasti non fanno nulla, la Roku sta bloccando il controllo tramite app: la guida [L'app Roku non funziona](@roku-403) spiega come consentirlo.",
    ],
    extra=[
      ("Se la Roku non ha più il Wi-Fi (cambio di router o trasloco)", "Senza telecomando non puoi entrare nel menu per configurare la nuova rete, ma c'è un trucco: la Roku si collega da sola a una rete con lo stesso nome e la stessa password della precedente. Su un altro smartphone crea un hotspot Wi-Fi con esattamente quel nome e quella password, collega a quella rete lo smartphone che ha Mando TV e la Roku comparirà nell'elenco. Da lì vai in Impostazioni, Rete, e collegala al nuovo Wi-Fi."),
      ("Se è una Roku TV", "I televisori Roku TV hanno un tasto fisico, quasi sempre in basso al centro o sul retro, che accende la TV. Basta per accenderla e proseguire con lo smartphone."),
      ("Se preferisci comprare un altro telecomando", "Assicurati che sia compatibile con il tuo modello. I piccoli dispositivi Roku nascosti dietro la TV hanno bisogno di un telecomando che non sia a infrarossi, perché l'infrarosso non li raggiunge."),
    ],
    marca='roku',
    faq=[
      ('Lo smartphone può accendere la Roku?', "Un dispositivo Roku collegato è sempre acceso. Su una Roku TV, Mando TV la accende via Wi-Fi quando l'avvio rapido della TV è attivo in Impostazioni > Sistema > Alimentazione."),
      ('E il volume?', "Su una Roku TV lo smartphone alza e abbassa il volume. Su un dispositivo Roku collegato in HDMI dipende dalla TV: su molte funziona, su altre no."),
      ('Devo creare un account?', "No. Mando TV non richiede un account e controlla anche le TV Samsung, LG e Android TV con la stessa app."),
    ]),
]

SOPORTE = dict(
  titulo='Assistenza: collegare e accendere la TV con Mando TV',
  desc="Come collegare il telecomando Mando TV alla tua TV LG, Samsung, Roku o Android TV, accenderla dallo smartphone e cosa fare se qualcosa non va.",
  h1='Assistenza',
  intro="Le domande più frequenti, nell'ordine dei passaggi. Se non trovi la tua, scrivici a <a href=\"mailto:hola@mandotv.app?subject=Assistenza%20Mando%20TV\">hola@mandotv.app</a> e ti risponderemo. Scrivici nella tua lingua. Rispondiamo in spagnolo o in inglese e, se preferisci, nella tua lingua con l'aiuto di un traduttore.",
)
SOPORTE_HTML = '''      <h2 id="encontrar">Trovare la TV</h2>
      <div class="preguntas">
        <details open><summary>La mia TV non compare nell'elenco</summary>
          <ol>
            <li>Controlla che smartphone e TV siano sulla stessa rete Wi-Fi. Se il tuo router ha una rete a 2,4 GHz e una a 5 GHz con nomi diversi, a volte non si vedono.</li>
            <li>Assicurati che la TV sia accesa.</li>
            <li>Su iPhone controlla che Mando TV abbia il permesso "Rete locale" in Impostazioni, Mando TV.</li>
            <li>Tocca, nell'elenco delle TV, il pulsante per il caso in cui la TV non compaia: l'app controlla passo dopo passo le cause più comuni (stessa rete Wi-Fi, VPN, permesso per la rete locale e altro) e mostra un pulsante per ricontrollare dopo ogni correzione.</li>
            <li>Se ancora non compare, tocca il pulsante +, scegli la marca e inserisci l'indirizzo IP della TV. Lo vedi nel menu di rete della TV (per esempio 192.168.1.50).</li>
          </ol>
        </details>
        <details><summary>Funziona con i dati mobili o fuori casa?</summary>
          <p>No. Mando TV comunica con la TV all'interno della tua rete domestica, quindi lo smartphone deve essere collegato a quel Wi-Fi.</p>
        </details>
      </div>

      <h2 id="conectar">Collegarsi per la prima volta</h2>
      <p>Guide complete per marca: <a href="@@R_lg@@">LG</a>, <a href="@@R_samsung@@">Samsung</a>, <a href="@@R_roku@@">Roku</a> e <a href="@@R_android@@">Android TV</a>.</p>
      <div class="preguntas">
        <details><summary>LG</summary>
          <p>Quando tocchi la TV, sul suo schermo compare un avviso che chiede l'autorizzazione. Accettalo con il telecomando di sempre. Lo fai una volta sola.</p>
        </details>
        <details><summary>Samsung</summary>
          <p>La TV chiede se consenti la connessione di Mando TV. Scegli "Consenti" con il telecomando. Se hai rifiutato per sbaglio, vai in Impostazioni > Generali > Gestione dispositivi esterni > Gestione connessione dispositivi ("Device Connection Manager") e cambia in consentito.</p>
        </details>
        <details><summary>Roku</summary>
          <p>Roku non chiede autorizzazione. Se la connessione fallisce, sulla Roku vai in Impostazioni > Sistema > Impostazioni di sistema avanzate > Controllo tramite app mobili ("Control by mobile apps") e lascia l'accesso alla rete su Predefinito o Permissivo (nelle versioni più recenti del software Roku, imposta "Control by mobile apps" su "Enabled").</p>
        </details>
        <details><summary>Android TV e Google TV</summary>
          <p>La TV mostra un codice di 6 caratteri. Inseriscilo in Mando TV esattamente come appare. Funziona per Sony, Philips, TCL, Hisense, Sharp, Xiaomi, Chromecast con Google TV e altre con Android TV.</p>
        </details>
      </div>

      <h2 id="encender">Accendere la TV dall'app</h2>
      <p>Mando TV accende la TV tramite la tua rete domestica. Servono due cose: esserti collegato almeno una volta a TV accesa e aver attivato sulla TV l'accensione tramite rete. Il nome dell'opzione cambia a seconda del modello; ecco i più comuni:</p>
      <div class="preguntas">
        <details><summary>LG</summary>
          <p>Cerca nelle Impostazioni ''' + LG_OPC + ''' e attiva ''' + LG_WIFI + '''. Se esiste l'opzione di avvio rapido ("Quick Start+" in inglese), attivala anche.</p>
        </details>
        <details><summary>Samsung</summary>
          <p>Attiva l'opzione per accendere con un dispositivo mobile ("Power On with Mobile") in Impostazioni > Generali > Rete > Impostazioni expert (Expert Settings).</p>
        </details>
        <details><summary>Roku</summary>
          <p>Sulle Roku TV attiva ''' + ROKU_RAPIDO + '''. I dispositivi Roku collegati a una TV non si possono accendere così.</p>
        </details>
        <details><summary>Android TV e Google TV</summary>
          <p>Dipende dal produttore. Cerca nelle impostazioni di rete o di alimentazione l'opzione ''' + AND_WOL + '''. Alcuni modelli non ce l'hanno.</p>
        </details>
      </div>

      <h2 id="falla">Se qualcosa non va</h2>
      <div class="preguntas">
        <details><summary>Si disconnette o non risponde</summary>
          <ol>
            <li>Nella schermata del telecomando tocca Riconnetti.</li>
            <li>Se non funziona, chiudi Mando TV e riaprila.</li>
            <li>Se la TV ha cambiato indirizzo IP, eliminala dall'elenco e aggiungila di nuovo.</li>
          </ol>
        </details>
        <details><summary>Come inviarci un rapporto di errore</summary>
          <ol>
            <li>In Mando TV tocca il pulsante Personalizza (i cursori in alto).</li>
            <li>Tocca Copia rapporto di prova.</li>
            <li>Incollalo in un'e-mail a hola@mandotv.app con la marca e il modello della tua TV.</li>
          </ol>
          <p>Il rapporto non include password, codici né nulla di ciò che scrivi.</p>
        </details>
        <details><summary>Ho acquistato Pro e non compare</summary>
          <p>In Personalizza tocca Ripristina acquisto, con lo stesso account dello store usato per l'acquisto. Se ancora non compare, scrivici.</p>
        </details>
      </div>

      <h2 id="guias">Guide passo dopo passo</h2>
      <p><a href="@@R_guias@@">Vedi tutte le guide</a></p>
      <ul>
@@GUIAS@@
      </ul>

      <h2 id="contacto">Hai ancora domande?</h2>
      <p>Scrivici a <a href="mailto:hola@mandotv.app?subject=Assistenza%20Mando%20TV">hola@mandotv.app</a>. Indica la marca e il modello della tua TV e il passaggio in cui ti sei bloccato. Scrivici nella tua lingua. Rispondiamo in spagnolo o in inglese e, se preferisci, nella tua lingua con l'aiuto di un traduttore.</p>
'''

PRIVACIDAD = dict(
  titulo='Informativa sulla privacy | Mando TV',
  desc="Mando TV non raccoglie dati personali: niente account, pubblicità o tracker. L'app parla solo con la tua TV, all'interno della tua rete Wi-Fi.",
  h1='Privacy',
  intro="In breve: Mando TV non raccoglie i tuoi dati. Non ci sono account, pubblicità, tracker né un nostro server che conservi ciò che fai.",
)
PRIVACIDAD_HTML = '''      <p class="fecha">In vigore dal 14 novembre 2026. Ultimo aggiornamento: 21 novembre 2026.</p>

      <h2>Chi siamo</h2>
      <p>Mando TV è un'app per controllare la tua TV dallo smartphone o dal computer. Questa informativa spiega quali informazioni usa l'app e cosa ne fa. Per qualsiasi domanda scrivici a <a href="mailto:hola@mandotv.app">hola@mandotv.app</a>.</p>

      <h2>Quali dati raccogliamo</h2>
      <p>Nell'app: nessuno. L'app non invia a noi né a terzi alcuna informazione su di te o su come la usi. Non usa strumenti di analisi, pubblicità o tracciamento.</p>
      <p>In questo sito web: misuriamo le visite in due modi, spiegati nella sezione <a href="#cookies">Cookie su questo sito web</a>.</p>

      <h2>Cosa conserva l'app sul tuo dispositivo</h2>
      <p>Per funzionare, l'app conserva quanto segue solo sul tuo smartphone o computer:</p>
      <ul>
        <li>Le TV che hai aggiunto: nome, marca, indirizzo IP nella tua rete e indirizzo fisico di rete (MAC), usato per accenderla.</li>
        <li>Le chiavi di connessione che ogni TV consegna quando accetti l'autorizzazione. Sono conservate cifrate nell'archivio sicuro del sistema (Portachiavi su iPhone e Mac, Keystore su Android, archivio protetto su Windows).</li>
        <li>Le tue preferenze: tema chiaro o scuro, colore di sfondo, vibrazione e tipo di telecomando.</li>
        <li>Se usi le funzioni Pro: le tue app preferite, le tue routine e le tue ultime ricerche su YouTube (puoi eliminarle dall'app).</li>
      </ul>
      <p>Se elimini l'app, tutto questo viene eliminato con lei.</p>

      <h2>Con chi comunica l'app</h2>
      <p>Con le tue TV, all'interno della rete Wi-Fi di casa. Per trovarle, l'app esplora la tua rete locale; per questo, su iPhone, chiede il permesso "Rete locale". Il testo che scrivi con la tastiera dell'app va direttamente alla TV e non viene conservato.</p>
      <p>Inoltre, all'apertura l'app scarica un piccolo file pubblico da questo sito web (mandotv.app/app/config.json) per sapere se c'è una nuova versione da installare e quali funzioni fanno parte di Mando TV Pro. È un download, come aprire una pagina: l'app non invia i tuoi dati, le tue TV né ciò che fai. Indica solo la versione dell'app e il sistema (per esempio Android), per poterti mostrare l'avviso giusto. Se non hai Internet, l'app continua a funzionare con l'ultimo file scaricato; se passano più di 30 giorni senza poterlo scaricare, ti chiederà di collegarti un momento a Internet.</p>

      <p>Se invii foto o video alla TV (una funzione Pro), la TV scarica solo i file che scegli, direttamente dallo smartphone o dal PC tramite il Wi-Fi di casa. Non passano da internet né da noi, l'app non vede il resto delle tue foto e la condivisione si ferma quando chiudi quella schermata.</p>
      <h2>Microfono e voce</h2>
      <p>La ricerca vocale usa il microfono solo mentre tocchi il pulsante per parlare. Ciò che dici viene convertito in testo dal riconoscimento vocale del tuo sistema: Apple su iPhone e Mac e Google su Android, secondo le rispettive informative sulla privacy. Su Windows la voce viene riconosciuta sul tuo PC e non esce dal computer; solo sui processori molto vecchi l'app usa la dettatura vocale di Windows, di Microsoft, secondo la sua informativa sulla privacy. Mando TV non registra né conserva l'audio, e il testo ottenuto va direttamente alla tua TV, come ciò che scrivi con la tastiera.</p>

      <h2>Rapporto di prova</h2>
      <p>L'app ha un pulsante "Copia rapporto di prova" per aiutarci a correggere gli errori. Il rapporto resta solo nella memoria dell'app finché è aperta e non viene mai inviato da solo: sei tu a decidere se copiarlo e condividerlo. Non include chiavi di connessione, codici di associazione né nulla di ciò che scrivi; solo i passaggi seguiti dall'app, come la ricerca, la connessione e gli errori.</p>

      <h2 id="cookies">Cookie su questo sito web</h2>
      <p>Questo vale solo per il sito web mandotv.app, non per l'app.</p>
      <h3>Mai cookie</h3>
      <p>Contiamo le visite in modo anonimo con Cloudflare Web Analytics: quante persone visitano il sito, quali pagine leggono e da quale paese. Non usa cookie, non usa il tuo indirizzo IP per identificarti e non segue ciò che fai su altri siti.</p>
      <h3>Con i cookie, solo se accetti</h3>
      <p>Se tocchi "Accetta" nell'avviso sui cookie, attiviamo Google Analytics (di Google LLC) per capire meglio come viene usato il sito: pagine viste, tempo sulla pagina, tipo di dispositivo, città approssimativa e provenienza. Per questo conserva i cookie _ga e _ga_* nel tuo browser per un massimo di 2 anni. Google può trattare questi dati su server situati fuori dal Cile. Abbiamo disattivato le funzioni pubblicitarie e Google Signals, e non usiamo questi dati per mostrarti pubblicità.</p>
      <p>Se tocchi "Rifiuta" o non scegli nulla, Google Analytics non viene caricato e non viene conservato alcun cookie. Puoi cambiare idea in qualsiasi momento con il pulsante "Cookies" in fondo a ogni pagina; se ritiri il consenso, eliminiamo quei cookie.</p>
      <p>La tua scelta è conservata nel tuo browser (archivio locale, che non viene inviato a nessuno) per non chiedertela di nuovo.</p>

      <h2>Acquisti</h2>
      <p>Se acquisti Mando TV Pro, il pagamento è gestito dallo store di app (App Store, Google Play o Microsoft Store). Noi non riceviamo né conserviamo i dati della tua carta. Lo store conferma all'app solo che l'acquisto esiste.</p>

      <h2>E-mail che ci invii</h2>
      <p>Se ci scrivi a <a href="mailto:hola@mandotv.app">hola@mandotv.app</a>, usiamo il tuo indirizzo e-mail e ciò che ci dici solo per risponderti. Non lo condividiamo e non lo usiamo per pubblicità. Puoi chiederci in qualsiasi momento di eliminare i tuoi messaggi.</p>

      <h2>Minori</h2>
      <p>L'app non raccoglie dati di nessuno, compresi i minori.</p>

      <h2>Modifiche a questa informativa</h2>
      <p>Se un giorno ciò che l'app fa con i tuoi dati cambiasse, aggiorneremo questa pagina e la data qui sopra prima che la modifica arrivi nell'app.</p>
'''
