# Textos en alemán (du) de mandotv.app. Los usa generar_idiomas.py. Escritos para las búsquedas de Alemania, Austria y Suiza.
# Las claves de las páginas (lg, lost-tv, ...) y sus rutas están en idiomas_sitio.py.
# Los nombres de menús de cada marca (LG, Samsung, Roku, Android TV, iPhone) son los mismos que usa la app en alemán
# (lib/l10n/app_de.arb del proyecto de la app).

UI = dict(
  locale='de_DE',
  aria_home='Mando TV, Startseite', aria_main='Hauptmenü', nav_que='Funktionen', nav_ayuda='Hilfe', nav_contacto='Kontakt',
  asunto='Hallo%20Mando%20TV', inicio='Startseite', privacidad='Datenschutz', aria_pie='Fußbereich', aria_ruta='Brotkrumenpfad',
  aria_marcas='Marken und Ratgeber', hecho='Entwickelt in Chile',
  aviso='Mando TV steht in keiner Verbindung zu LG, Samsung, Roku oder Google. Die genannten Marken gehören ihren jeweiligen Inhabern und werden nur genannt, um die Kompatibilität zu zeigen.',
  bajar='Kostenlos herunterladen', descarga='Herunterladen im', anticipada='Früher Zugang bei',
  apple_aria='Mando TV kostenlos im App Store laden', ms_aria='Mando TV kostenlos im Microsoft Store laden',
  gp_aria='Früher Zugang zu Mando TV bei Google Play für Android', aria_desc='Mando TV herunterladen',
  b_como_btn='So verbindest du dich', b_tiendas_label='In den Stores erhältlich',
  b_nota='iPhone, iPad, Android und Windows. Kostenloser Download, ohne Werbung. Pro ist ein einmaliger Kauf, ohne Abo.',
  b_compat='Kompatible Fernseher', b_otras='Andere Marken', b_otras_p='Mando TV steuert alle diese Marken mit derselben App:',
  g_guias='Ratgeber', g_ver='Schritte ansehen', g_pasos='Schritt für Schritt', g_hazlo='So geht es mit Mando TV',
  g_tiendas='Mando TV ist eine universelle Fernbedienung für deinen Fernseher. Lade sie kostenlos herunter, ohne Werbung und ohne Konto. Pro ist ein optionaler Einmalkauf, ohne Abo. Für iPhone, iPad, Windows und Android:',
  g_nota='Android: kostenloser früher Zugang bei Google Play. <a href="{enlace}">Mach in zwei Schritten mit</a> und hilf uns, den Store zu erreichen.',
  g_mas_pagina='Mehr Details findest du auf der Seite {enlace}.', g_mas_marca='Mehr Details nach Marke:',
  g_faq='Häufige Fragen', g_mas='Weitere Ratgeber', g_todas='Alle Ratgeber', g_ayuda='Hilfe und Support',
  g_idiomas='Dieser Ratgeber in anderen Sprachen',
)

# Pie de página y listas de marcas/guías: (clave, texto)
PIE = [
  ('samsung', 'Samsung Fernbedienung'),
  ('lg', 'LG Fernbedienung'),
  ('roku', 'Roku Fernbedienung'),
  ('android', 'Android TV Fernbedienung'),
  ('guias', 'Alle Ratgeber'),
  ('lost-tv', 'Fernbedienung verloren'),
  ('lost-lg', 'LG Fernbedienung verloren'),
  ('lg-on', 'LG Fernseher mit dem Handy einschalten'),
  ('hdmi', 'HDMI-Eingang ohne Fernbedienung wechseln'),
  ('androidtv', 'Android TV ohne Fernbedienung'),
  ('console', 'Fernseher und Konsolen-HDMI ohne Fernbedienung'),
  ('samsung-lost', 'Samsung Fernseher ohne Fernbedienung'),
  ('roku-lost', 'Roku Fernbedienung verloren'),
  ('roku-403', 'Roku App funktioniert nicht'),
  ('androidtv-code', 'Android TV Kopplungscode'),
  ('not-found', 'Handy findet den Fernseher nicht'),
  ('wifi', 'Handy als Fernbedienung per WLAN'),
  ('pc', 'Fernseher mit dem PC steuern'),
]
NOMBRE_OTRA = {'lg': 'LG Fernbedienungs-App', 'samsung': 'Samsung Fernbedienungs-App', 'roku': 'Roku Fernbedienungs-App',
               'android': 'Android TV und Google TV Fernbedienungs-App'}
PAGINA_MARCA = {'lg': 'LG Fernbedienungs-App', 'samsung': 'Samsung Fernbedienungs-App', 'roku': 'Roku Fernbedienungs-App',
                'android': 'Android TV Fernbedienungs-App'}

OTRAS_GUIAS = [
  ('lg-on', 'LG Fernseher mit dem Handy einschalten'),
  ('lost-tv', 'Fernbedienung verloren: Das kannst du tun'),
  ('lost-lg', 'LG Fernbedienung verloren: So nutzt du dein Handy'),
  ('hdmi', 'HDMI-Eingang am Fernseher ohne Fernbedienung wechseln'),
  ('androidtv', 'Android TV ohne Fernbedienung: So nutzt du dein Handy'),
  ('console', 'Fernseher einschalten und auf Konsolen-HDMI wechseln, ohne Fernbedienung'),
  ('samsung-lost', 'Samsung Fernseher ohne Original-Fernbedienung: So nutzt du dein Handy'),
  ('roku-lost', 'Roku Fernbedienung verloren: So nutzt du dein Handy'),
  ('roku-403', 'Roku App funktioniert nicht: Fehler 403 beheben'),
  ('androidtv-code', 'Android TV fragt nach einem Kopplungscode: Das ist zu tun'),
  ('not-found', 'Dein Handy findet den Fernseher nicht: Das solltest du prüfen'),
  ('wifi', 'So nutzt du dein Handy per WLAN als Fernbedienung'),
  ('pc', 'So steuerst du deinen Fernseher mit einem Windows-PC'),
]

INDICE = dict(
  titulo='Ratgeber: Fernseher mit dem Handy steuern | Mando TV',
  desc='Ratgeber Schritt für Schritt: Handy oder PC als Fernbedienung nutzen, Fernseher einschalten, HDMI wechseln und Probleme bei Samsung, LG, Roku lösen.',
  h1='Ratgeber: Handy als Fernbedienung nutzen',
  intro='Einfache Schritte, um die Fernbedienung deines Samsung-, LG-, Roku- oder Android-TV-Fernsehers mit Mando TV zu verbinden, den Fernseher einzuschalten und Probleme zu lösen.',
  h2_guias='Alle Ratgeber', h2_marcas='Fernbedienungs-App nach Marke',
)

MARCAS = [
  dict(clave='lg', color='#e0457b', corto='LG',
    titulo='LG TV Fernbedienung App fürs Handy, kostenlos | Mando TV',
    desc='Dein Handy oder PC als LG TV Fernbedienung für webOS, per WLAN. Tasten, Tastatur und Einschalten gratis; Zeiger, Apps und Eingänge mit Pro.',
    h1='LG TV Fernbedienung als App fürs Handy',
    intro='Mando TV ist eine Fernbedienungs-App für LG-Fernseher: Sie macht dein Handy oder deinen Computer über das WLAN zu Hause zur Fernbedienung deines LG Smart-TVs mit webOS. Das hilft, wenn du die Fernbedienung verloren hast, die Batterien leer sind oder du einfach schneller tippen möchtest.',
    compat='LG Smart-TVs mit webOS (die meisten LG-Smart-TV-Modelle seit 2014). Funktioniert mit LED-, NanoCell-, QNED- und OLED-Fernsehern.',
    h2=dict(funciones='Das kannst du mit deinem LG-Fernseher machen', como='So verbindest du deinen LG-Fernseher mit Mando TV',
            encender='LG-Fernseher mit dem Handy einschalten', preguntas='Fragen zu LG', guias='Ratgeber für LG'),
    funciones=[
      ('Alle Tasten', 'Steuerkreuz, OK, Zurück, Home, Lautstärke, Programme, Stummschaltung und Wiedergabe.'),
      ('Zeiger wie bei der Magic Remote (Pro)', 'Bewege den Pfeil mit dem Finger über den Bildschirm, genau wie mit der LG Magic Remote.'),
      ('Tastatur', 'Tippe in YouTube, Netflix oder im Browser des Fernsehers mit der Tastatur deines Handys.'),
      ('Apps und Eingänge (Pro)', 'Öffne deine Apps und wechsle zu HDMI, Live-TV, AirPlay oder Screen Share.'),
      ('Audioausgabe (Pro)', 'Wechsle zwischen den Lautsprechern des Fernsehers und deiner Soundbar.'),
      ('Fernseher einschalten', 'Ist er aus, schaltet Mando TV ihn über das Netzwerk ein und verbindet sich von selbst.'),
    ],
    pasos=[
      'Verbinde Handy und Fernseher mit demselben WLAN.',
      'Öffne Mando TV: Dein LG-Fernseher erscheint von selbst in der Liste. Tippe darauf.',
      'Auf dem Fernseher erscheint eine Abfrage, die um Erlaubnis bittet. Bestätige sie mit deiner gewohnten Fernbedienung (nur beim ersten Mal).',
    ],
    encender='Öffne am LG-Fernseher die Einstellungen und suche „Fernseher per Mobilgerät einschalten“ (je nach Modell unter Allgemein oder Verbindung). Aktiviere „Über WLAN einschalten“. Gibt es „Quick Start+“, aktiviere es ebenfalls. Danach fragt dich die App, wenn du den ausgeschalteten Fernseher in Mando TV antippst, ob sie ihn einschalten soll, und verbindet sich von selbst.',
    faq=[
      ('Brauche ich die Magic Remote, um Mando TV zu nutzen?', 'Nur beim ersten Mal, um die Abfrage auf dem Bildschirm zu bestätigen. Danach reicht dein Handy.'),
      ('Ersetzt Mando TV die LG ThinQ App?', 'Zum Steuern des Fernsehers ja: Du brauchst weder ein LG-Konto noch musst du den Fernseher registrieren. Mando TV verbindet sich direkt über dein WLAN.'),
      ('Kann ich meinen LG-Fernseher mit dem Handy einschalten?', 'Ja, wenn du am Fernseher „Fernseher per Mobilgerät einschalten“ aktiviert und dich einmal verbunden hast, während der Fernseher an war.'),
    ],
    guias=[('lg-on', 'So schaltest du einen LG-Fernseher mit dem Handy ein'),
           ('lost-lg', 'LG Fernbedienung verloren: So nutzt du dein Handy'),
           ('hdmi', 'HDMI-Eingang am Fernseher ohne Fernbedienung wechseln'),
           ('guias', 'Alle Ratgeber, um den Fernseher mit dem Handy zu steuern')]),
  dict(clave='samsung', color='#3d7bff', corto='Samsung',
    titulo='Samsung TV Fernbedienung App fürs Handy | Mando TV',
    desc='Dein Handy oder PC als Samsung TV Fernbedienung für Tizen, per WLAN. Tasten, Tastatur und Einschalten gratis; Touchpad und Apps mit Pro. Ohne Werbung.',
    h1='Samsung TV Fernbedienung als App fürs Handy',
    intro='Mando TV ist eine Fernbedienungs-App für Samsung-Fernseher: Sie macht dein Handy oder deinen Computer über das WLAN zu Hause zur Fernbedienung deines Samsung Smart-TVs. Du brauchst weder ein Samsung-Konto noch musst du den Fernseher registrieren.',
    compat='Samsung Smart-TVs mit Tizen, Baujahr 2016 und neuer (Serien wie Crystal UHD, QLED, Neo QLED, The Frame und OLED).',
    h2=dict(funciones='Das kannst du mit deinem Samsung-Fernseher machen', como='So verbindest du deinen Samsung-Fernseher mit Mando TV',
            encender='Samsung-Fernseher mit dem Handy einschalten', preguntas='Fragen zu Samsung', guias='Ratgeber für Samsung'),
    funciones=[
      ('Alle Tasten', 'Steuerkreuz, OK, Zurück, Home, Lautstärke, Programme, Stummschaltung und Quelle.'),
      ('Touchpad (Pro)', 'Wische mit dem Finger durch die Menüs, ohne nach den Pfeiltasten zu suchen.'),
      ('Tastatur', 'Tippe Suchbegriffe und Passwörter mit der Tastatur deines Handys.'),
      ('Apps (Pro)', 'Öffne Netflix, YouTube, Prime Video und deine anderen Apps mit einem Tipp.'),
      ('Fernseher einschalten', 'Ist er aus, schaltet Mando TV ihn über das Netzwerk ein und verbindet sich von selbst.'),
      ('Ohne Konto', 'Die Verbindung läuft direkt über dein WLAN, ohne Umweg über das Internet.'),
    ],
    pasos=[
      'Verbinde Handy und Fernseher mit demselben WLAN.',
      'Öffne Mando TV: Dein Samsung-Fernseher erscheint von selbst in der Liste. Tippe darauf.',
      'Der Fernseher fragt, ob du die Verbindung zulässt. Wähle mit der Fernbedienung „Zulassen“ (nur beim ersten Mal).',
    ],
    encender='Aktiviere am Samsung-Fernseher unter Einstellungen > Allgemein > Netzwerk > Experteneinstellungen die Option „Mit Mobilgerät einschalten“. Danach fragt dich die App, wenn du den ausgeschalteten Fernseher in Mando TV antippst, ob sie ihn einschalten soll, und verbindet sich von selbst.',
    faq=[
      ('Ich habe die Erlaubnis versehentlich abgelehnt. Was tun?', 'Gehe am Fernseher zu Einstellungen > Allgemein > Externer Geräte-Manager > Geräteverbindungs-Manager und stelle Mando TV auf erlaubt.'),
      ('Ersetzt Mando TV SmartThings?', 'Zum Steuern des Fernsehers ja, und das ohne Samsung-Konto. Mando TV verbindet sich direkt über dein WLAN.'),
      ('Funktioniert es mit älteren Samsung-Fernsehern?', 'Es funktioniert mit Samsung-Fernsehern mit Tizen, Baujahr 2016 und neuer. Frühere Modelle nutzen ein anderes System, das wir noch nicht unterstützen.'),
    ],
    guias=[('samsung-lost', 'Samsung Fernseher ohne Original-Fernbedienung: So nutzt du dein Handy'),
           ('hdmi', 'HDMI-Eingang am Fernseher ohne Fernbedienung wechseln'),
           ('guias', 'Alle Ratgeber, um den Fernseher mit dem Handy zu steuern')]),
  dict(clave='roku', color='#a77bff', corto='Roku',
    titulo='Roku Fernbedienung App fürs Handy, kostenlos | Mando TV',
    desc='Dein Handy oder PC als Roku Fernbedienung für Roku TV und Roku Player, per WLAN. Tasten, Tastatur und Einschalten gratis; Kanäle und Eingänge mit Pro.',
    h1='Roku Fernbedienung als App fürs Handy',
    intro='Mando TV ist eine Fernbedienungs-App für Roku: Sie macht dein Handy oder deinen Computer über das WLAN zu Hause zur Fernbedienung deines Roku. Sie funktioniert mit Roku-TV-Geräten und mit Roku-Playern, die an den HDMI-Anschluss kommen.',
    compat='Roku-TV-Geräte (TCL, Hisense, Philips, Sharp, JVC und andere) und Roku-Player (Express, Streaming Stick, Ultra).',
    h2=dict(funciones='Das kannst du mit deinem Roku machen', como='So verbindest du deinen Roku mit Mando TV',
            encender='Roku mit dem Handy einschalten', preguntas='Fragen zu Roku', guias='Ratgeber für Roku'),
    funciones=[
      ('Alle Tasten', 'Steuerkreuz, OK, Zurück, Home, Lautstärke, Stummschaltung, Wiederholen und Wiedergabe.'),
      ('Tastatur', 'Tippe Suchbegriffe in Roku-Kanälen mit der Tastatur deines Handys.'),
      ('Kanäle (Pro)', 'Öffne Netflix, YouTube und deine anderen Roku-Kanäle mit einem Tipp.'),
      ('Eingänge (Pro)', 'Wechsle bei einem Roku TV in der App zu HDMI, Antenne oder AV.'),
      ('Fernseher einschalten', 'Bei Roku-TV-Geräten mit Schnellstart schaltet Mando TV sie von deinem Handy aus ein.'),
      ('Ohne Kopplung', 'Roku fragt nicht nach einem Code: Tippe in der Liste darauf und du bist verbunden.'),
    ],
    pasos=[
      'Verbinde Handy und Roku mit demselben WLAN.',
      'Öffne Mando TV: Dein Roku erscheint von selbst in der Liste. Tippe darauf.',
      'Falls die Verbindung nicht klappt, gehe am Roku zu Einstellungen > System > Erweiterte Systemeinstellungen > Steuerung durch mobile Apps und stelle den Netzwerkzugriff auf Standard oder Permissiv.',
    ],
    encender='Aktiviere bei Roku-TV-Geräten unter Einstellungen > System > Energie die Option „Schneller TV-Start“. Roku-Player, die an einen anderen Fernseher angeschlossen sind, lassen sich so nicht einschalten. Danach fragt dich die App, wenn du den ausgeschalteten Fernseher in Mando TV antippst, ob sie ihn einschalten soll, und verbindet sich von selbst.',
    faq=[
      ('Funktioniert es mit dem Roku Express oder dem Streaming Stick?', 'Ja. Alle Roku-Player und Roku-TV-Geräte werden auf die gleiche Weise gesteuert.'),
      ('Mando TV findet meinen Roku nicht. Was tun?', 'Prüfe, ob beide im selben WLAN sind und ob „Steuerung durch mobile Apps“ am Roku nicht ausgeschaltet ist. Du kannst ihn auch über seine IP-Adresse hinzufügen.'),
      ('Brauche ich ein Roku-Konto?', 'Nein. Mando TV verbindet sich direkt über dein WLAN.'),
    ],
    guias=[('roku-403', 'Roku App funktioniert nicht (Fehler 403)'),
           ('roku-lost', 'Roku Fernbedienung verloren: So nutzt du dein Handy'),
           ('guias', 'Alle Ratgeber, um den Fernseher mit dem Handy zu steuern')]),
  dict(clave='android', color='#2fbf8f', corto='Android TV und Google TV',
    titulo='Android TV Fernbedienung App fürs Handy | Mando TV',
    desc='Dein Handy oder PC als Android TV Fernbedienung (Sony, TCL, Xiaomi), per WLAN. Tasten, Tastatur und Einschalten gratis; Touchpad und Apps mit Pro.',
    h1='Android TV Fernbedienung als App fürs Handy',
    intro='Mando TV ist eine Fernbedienungs-App für Android TV: Sie macht dein Handy oder deinen Computer über das WLAN zu Hause zur Fernbedienung deines Android-TV- oder Google-TV-Fernsehers. Sie funktioniert auch vom iPhone und von Windows aus.',
    compat='Fernseher mit Android TV oder Google TV (Sony, TCL, Philips, Xiaomi, Hisense und andere), Chromecast mit Google TV, Google TV Streamer und Nvidia Shield.',
    h2=dict(funciones='Das kannst du mit deinem Android TV machen', como='So verbindest du deinen Android TV mit Mando TV',
            encender='Android TV mit dem Handy einschalten', preguntas='Fragen zu Android TV', guias='Ratgeber für Android TV'),
    funciones=[
      ('Alle Tasten', 'Steuerkreuz, OK, Zurück, Home, Lautstärke, Stummschaltung und Wiedergabe.'),
      ('Touchpad (Pro)', 'Wische mit dem Finger, um schnell durch die Menüs von Google TV zu navigieren.'),
      ('Tastatur', 'Tippe Suchbegriffe und Passwörter mit der Tastatur deines Handys.'),
      ('Apps (Pro)', 'Öffne YouTube, Netflix, Disney+ und deine anderen Apps mit einem Tipp.'),
      ('Fernseher einschalten', 'Bei Modellen mit Einschalten über das Netzwerk schaltet Mando TV den Fernseher ein und verbindet sich von selbst.'),
      ('iPhone, Android und PC', 'Es funktioniert auf jedem Handy und jedem Computer gleich.'),
    ],
    pasos=[
      'Verbinde Handy und Fernseher mit demselben WLAN.',
      'Öffne Mando TV: Dein Android TV erscheint von selbst in der Liste. Tippe darauf.',
      'Der Fernseher zeigt einen Code mit 6 Zeichen an. Gib ihn in Mando TV ein (nur beim ersten Mal).',
    ],
    encender='Das hängt vom Hersteller ab. Suche in den Netzwerk- oder Energieeinstellungen nach „Wake on LAN“, „Einschalten über Netzwerk“ oder „Netzwerk-Standby“. Manche Modelle haben diese Option nicht. Danach fragt dich die App, wenn du den ausgeschalteten Fernseher in Mando TV antippst, ob sie ihn einschalten soll, und verbindet sich von selbst.',
    faq=[
      ('Funktioniert es mit Chromecast mit Google TV?', 'Ja, die Kopplung läuft über den Code mit 6 Zeichen, der auf dem Bildschirm erscheint.'),
      ('Was unterscheidet es von der Google-TV-App?', 'Mando TV braucht kein Google-Konto, funktioniert auch unter Windows und steuert Fernseher von LG, Samsung und Roku mit derselben App.'),
      ('Der Code erscheint nicht auf dem Bildschirm. Was tun?', 'Schließe Mando TV, öffne die App erneut und tippe noch einmal auf den Fernseher. Prüfe, dass der Fernseher nicht in einem tiefen Energiesparmodus ist.'),
    ],
    guias=[('androidtv-code', 'Android TV fragt nach einem Kopplungscode: Das ist zu tun'),
           ('androidtv', 'Android TV ohne Fernbedienung: So nutzt du dein Handy'),
           ('guias', 'Alle Ratgeber, um den Fernseher mit dem Handy zu steuern')]),
]

GUIAS = [
  dict(clave='lost-tv', corto='Fernbedienung verloren',
    titulo='Fernbedienung verloren? Fernseher mit dem Handy steuern',
    desc='Fernbedienung verloren? Schalte den Fernseher am Gerät ein und nutze dein Handy als Fernbedienung. Schritte für LG, Samsung, Roku, Android TV. Gratis.',
    h1='Fernbedienung verloren? Das kannst du jetzt tun',
    intro='Eine verlorene Fernbedienung kommt in jedem Haushalt vor: Sie ist genau dann weg, wenn du etwas schauen willst. Die gute Nachricht: Dein Handy kann über das WLAN zu Hause die Fernbedienung ersetzen. Hier siehst du, was du der Reihe nach tun kannst.',
    pasos=[
      'Schalte den Fernseher mit der Taste am Gerät ein. Sie sitzt fast immer unten in der Mitte oder an der Rückseite nahe einer Ecke. Manchmal ist es eine einzelne Taste, manchmal ein kleiner Joystick.',
      'Verbinde dein Handy mit demselben WLAN wie den Fernseher.',
      'Lade Mando TV herunter, das kostenlos ist und kein Konto verlangt, und öffne die App. Dein Fernseher erscheint von selbst in der Liste. Tippe darauf.',
      'Bestätige die Verbindung für deine Marke. Bei LG und Samsung zeigt der Fernseher eine Abfrage: Bestätige sie mit der Taste oder dem Joystick am Fernseher selbst. Bei Android TV und Google TV gibst du einen Code mit 6 Zeichen ein, der auf dem Bildschirm erscheint. Roku fragt nach nichts.',
      'Fertig. Pfeile, OK, Zurück, Home, Lautstärke, Programme und Tastatur sind kostenlos.',
      'Für das nächste Mal: Aktiviere in den Einstellungen des Fernsehers das Einschalten über das Netzwerk (den Ratgeber für deine Marke findest du unten). Dann kannst du den Fernseher vom Handy aus einschalten, ohne ihn anzufassen.',
    ],
    extra=[
      ('Such dir den Ratgeber für deine Marke aus', 'LG: [LG Fernbedienung verloren](@lost-lg). Android TV und Google TV: [Android TV ohne Fernbedienung](@androidtv). Samsung: [Samsung Fernseher ohne Fernbedienung](@samsung-lost). Roku: [Roku Fernbedienung verloren](@roku-lost).'),
      ('Wenn sich der Fernseher mit der Taste nicht einschalten lässt', 'Bevor du nach einer anderen Fernbedienung suchst, prüfe, ob das Kabel fest steckt und die Steckdose Strom hat. Tut die Taste am Fernseher nichts, liegt das Problem am Fernseher und nicht an der Fernbedienung.'),
      ('Wenn die Fernbedienung einfach nicht mehr funktioniert', 'Probiere neue Batterien aus. Ob sie noch ein Signal sendet, kannst du prüfen, indem du sie auf die Handykamera richtest und eine Taste drückst: Bei vielen Handys siehst du dann ein violettes Licht auf dem Bildschirm. Siehst du das Licht und der Fernseher reagiert nicht, ist vielleicht der Sensor am Fernseher verdeckt.'),
      ('Wenn du den Router gewechselt hast und der Fernseher kein WLAN mehr hat', 'Ohne Fernbedienung ist es schwerer, den Fernseher mit dem neuen Netzwerk zu verbinden. Am einfachsten steckst du den Fernseher mit einem Netzwerkkabel in den Router. Du kannst auch ein WLAN mit demselben Namen und Passwort wie vorher einrichten: Der Fernseher verbindet sich meist von selbst damit.'),
      ('Was kostenlos ist und was Pro', 'Fernseher ein- und ausschalten, Pfeile, OK, Lautstärke, Programme, Zifferntasten und Tastatur sind kostenlos. Das Touchpad, die App-Liste, die Eingangsliste, Sprache und Routinen gehören zu Mando TV Pro, einem Einmalkauf ohne Abo.'),
    ],
    marca=None,
    faq=[
      ('Kann ich den Fernseher mit dem Handy einschalten, wenn ich ihn noch nie verbunden habe?', 'Beim ersten Mal schaltest du ihn mit der Taste am Fernseher ein. Nachdem du dein Handy verbunden und in den Einstellungen des Fernsehers das Einschalten über das Netzwerk aktiviert hast, kannst du ihn über die App einschalten.'),
      ('Muss ich eine neue Fernbedienung kaufen?', 'Nicht unbedingt. Mit Mando TV bekommst du Tasten, Lautstärke, Tastatur und Einschalten kostenlos. Wenn du trotzdem lieber eine echte Fernbedienung hast, suche nach dem genauen Modell deines Fernsehers.'),
      ('Funktioniert es, wenn der Fernseher kein WLAN hat?', 'Nein. Handy und Fernseher müssen im selben WLAN sein. Ein Fernseher, der kein Smart-TV ist, lässt sich nicht mit Mando TV steuern.'),
    ]),
  dict(clave='lost-lg', corto='LG Fernbedienung verloren',
    titulo='LG Fernbedienung verloren? Nutze dein Handy',
    desc='Keine LG Fernbedienung? Schalte den Fernseher am Gerät ein, bestätige die Abfrage und nutze dein Handy per WLAN. Ohne LG-Konto, ohne Werbung.',
    h1='LG Fernbedienung verloren? So nutzt du dein Handy',
    intro='Wenn du deine LG Fernbedienung verloren hast oder die Magic Remote nicht mehr funktioniert, ersetzt dein Handy sie über das WLAN. Das klappt bei LG-Fernsehern mit webOS, also bei fast jedem LG Smart-TV seit 2014. Du brauchst weder ein LG-Konto noch die ThinQ App.',
    pasos=[
      'Schalte den Fernseher mit der Taste unten unter dem LG-Logo oder mit der Taste an der Rückseite ein. Bei vielen Modellen ist sie ein Joystick: Drücke ihn, um das Menü zu öffnen, und bewege ihn, um etwas auszuwählen.',
      'Verbinde dein Handy mit demselben WLAN wie den Fernseher.',
      'Öffne Mando TV und tippe in der Liste auf deinen LG-Fernseher.',
      'Der Fernseher zeigt eine Abfrage, die um Erlaubnis bittet. Bestätige sie mit dem Joystick oder der Taste am Fernseher. Wenn du dieses Handy schon einmal verbunden hast, fragt er nicht noch einmal.',
      'Fertig. Pfeile, OK, Zurück, Home, Lautstärke, Programme und Tastatur sind kostenlos. Der Zeiger, die App-Liste und die Eingangsliste sind Pro-Funktionen.',
      'Rufe bei verbundener App mit den Pfeilen und OK die Einstellungen auf und aktiviere „Fernseher per Mobilgerät einschalten“. Der Ratgeber [LG Fernseher mit dem Handy einschalten](@lg-on) zeigt, wo du die Option findest.',
    ],
    extra=[
      ('Wenn der Fernseher die Abfrage nicht anzeigt', 'Vielleicht ist die Erlaubnis schon gespeichert oder dein Handy ist in einem anderen Netzwerk. Prüfe, ob beide im selben WLAN sind und das VPN aus ist. Erscheint der Fernseher nicht in der Liste, hilft dir [Dein Handy findet den Fernseher nicht](@not-found) weiter.'),
      ('Wenn der Fernseher sein WLAN verloren hat', 'Stecke den Fernseher mit einem Netzwerkkabel in den Router, dann nutzt er es von selbst. Oder richte ein WLAN mit demselben Namen und Passwort wie vorher ein, denn der Fernseher verbindet sich meist von selbst damit.'),
      ('Wenn der Fernseher auf einem anderen Eingang hängt', 'Tippe auf deinem Handy auf Eingänge (eine Pro-Funktion) und wähle den HDMI-Anschluss. Mehr dazu steht in [HDMI-Eingang am Fernseher ohne Fernbedienung wechseln](@hdmi).'),
    ],
    marca='lg',
    faq=[
      ('Brauche ich die Magic Remote, um Mando TV zu nutzen?', 'Du brauchst nur beim ersten Mal etwas, um die Abfrage zu bestätigen, und dafür reicht die Taste oder der Joystick am Fernseher selbst. Danach nutzt du nur noch dein Handy.'),
      ('Brauche ich die LG ThinQ App?', 'Nein. Mando TV verbindet sich direkt über dein WLAN und verlangt kein LG-Konto.'),
      ('Kann ich meinen LG-Fernseher mit dem Handy aus- und einschalten?', 'Ausschalten ja. Zum Einschalten musst du am Fernseher „Fernseher per Mobilgerät einschalten“ aktiviert und dich einmal verbunden haben, während der Fernseher an war.'),
    ]),
  dict(clave='hdmi', corto='HDMI ohne Fernbedienung wechseln',
    titulo='HDMI-Eingang wechseln ohne Fernbedienung (Samsung, LG, Roku)',
    desc='HDMI-Eingang ohne Fernbedienung wechseln bei Samsung, LG oder Roku: mit der Taste am Fernseher oder mit dem Handy. Gratis zum Start, ohne Werbung.',
    h1='So wechselst du den HDMI-Eingang am Fernseher ohne Fernbedienung',
    intro='Die Konsole oder der Streaming-Player ist bereit, aber der Fernseher hängt auf einem anderen Eingang und die Fernbedienung ist nirgends zu finden. Um den HDMI-Eingang ohne Fernbedienung zu wechseln, hast du zwei Möglichkeiten: die Taste am Fernseher selbst oder dein Handy. Hier die Schritte für Samsung, LG und Roku.',
    pasos=[
      'Probiere zuerst das Einfachste: Schalte die Konsole oder den Player ein. Ist HDMI-CEC am Fernseher aktiviert (bei Samsung heißt es Anynet+, bei LG SIMPLINK), wechselt er von selbst auf diesen Eingang.',
      'Wechselt er nicht, nutze die Taste am Fernseher selbst, unten in der Mitte oder an der Rückseite. Bei vielen Samsung- und LG-Fernsehern ist sie ein Joystick und öffnet ein Menü mit Quelle oder Eingänge.',
      'Wähle in diesem Menü den Eingang aus: HDMI 1, HDMI 2 und so weiter. Die Nummer ist der Anschluss, an dem das Kabel steckt.',
      'Wenn du lieber dein Handy nutzt, verbinde es mit demselben WLAN, öffne Mando TV und tippe auf deinen Fernseher.',
      'Tippe bei LG und Roku auf Eingänge (eine Pro-Funktion) und wähle den HDMI-Anschluss. Bei Samsung sendet Eingänge (eine Pro-Funktion) die Quelle-Taste an den Fernseher, und du wählst mit den Pfeilen und OK.',
      'Du kannst es auch ohne Pro: Gehe mit den Pfeilen und OK auf dem Startbildschirm des Fernsehers zu den Eingängen. Je nach Marke und Baujahr heißen sie Quelle, Verbundene Geräte oder Eingänge. Bei einem Roku TV sind es die HDMI-Kacheln auf dem Startbildschirm.',
    ],
    extra=[
      ('Samsung', 'Hat das Menü der Taste am Fernseher keinen Punkt Quelle, öffne mit deinem Handy das Menü des Startbildschirms und suche links nach Quelle oder Verbundene Geräte. Du steuerst es mit den Pfeilen und OK in Mando TV, die kostenlos sind.'),
      ('LG', 'Drücke den Joystick am Fernseher und suche Eingänge. Mit deinem Handy kannst du in Mando TV auch die Eingangsliste (Pro) öffnen und den gewünschten Eingang antippen.'),
      ('Roku TV', 'Auf dem Startbildschirm gibt es für jeden Eingang eine Kachel, zum Beispiel HDMI 1 oder HDMI 2. Bewege dich mit den Pfeilen und öffne sie mit OK, kostenlos.'),
      ('Wenn es ein Fernseher mit Android TV oder Google TV ist', 'In Mando TV gibt es die Eingangsliste für Android TV noch nicht. Nutze die Eingangstaste am Fernseher selbst oder erreiche die Eingänge mit den Pfeilen und OK vom Startbildschirm aus. Wenn du keine Fernbedienung hast und dich verbinden möchtest, lies [Android TV ohne Fernbedienung](@androidtv).'),
      ('Mehr Hilfe', 'Schaltet sich der Fernseher gar nicht ein oder weißt du nicht, wo du anfangen sollst, lies [Fernbedienung verloren](@lost-tv). Zum Spielen an der Konsole enthält der Ratgeber [Fernseher einschalten und auf Konsolen-HDMI wechseln, ohne Fernbedienung](@console) den HDMI-CEC-Trick.'),
    ],
    marca=None,
    faq=[
      ('Ist das Wechseln des HDMI-Eingangs kostenlos?', 'Die Eingangsliste gehört zu Mando TV Pro, einem Einmalkauf ohne Abo. Kostenlos kannst du den Fernseher einschalten, Pfeile, OK und Lautstärke nutzen und die Eingänge über das Menü des Fernsehers erreichen.'),
      ('Woher weiß ich, welchen HDMI-Eingang ich brauche?', 'Schau dir die HDMI-Anschlüsse am Fernseher an: Jeder hat eine Nummer. Nimm den, an dem das Kabel deiner Konsole oder deines Players steckt.'),
      ('Was ist, wenn sich der Fernseher nicht einschaltet?', 'Schalte ihn mit seiner Taste am Gerät ein. Hast du ihn schon einmal verbunden und das Einschalten über das Netzwerk aktiviert, kannst du ihn auch über dein Handy einschalten.'),
    ]),
  dict(clave='androidtv', corto='Android TV ohne Fernbedienung',
    titulo='Android TV ohne Fernbedienung: Nutze dein Handy',
    desc='Keine Android-TV- oder Google-TV-Fernbedienung? Verbinde dein Handy mit dem 6-stelligen Code auf dem Bildschirm. Gratis, ohne Konto, ohne Werbung.',
    h1='Android TV ohne Fernbedienung: So nutzt du dein Handy',
    intro='Wenn du die Fernbedienung deines Android TV oder Google TV verloren hast oder ihre Batterien leer sind, ersetzt dein Handy sie. Das Beste: Für die Verbindung brauchst du die Fernbedienung nicht, denn der Fernseher zeigt einen Code auf dem Bildschirm und du tippst ihn auf dem Handy ein. Es funktioniert bei Fernsehern von Sony, TCL, Philips, Xiaomi und Hisense mit Android TV, bei Chromecast mit Google TV und bei Nvidia Shield.',
    pasos=[
      'Schalte den Fernseher mit der Taste am Gerät ein. Sie sitzt fast immer unten in der Mitte oder an der Rückseite nahe einer Ecke.',
      'Verbinde dein Handy mit demselben WLAN wie den Fernseher.',
      'Lade Mando TV herunter, das kostenlos ist und kein Google-Konto verlangt, und öffne die App. Tippe in der Liste auf deinen Fernseher.',
      'Der Fernseher zeigt einen Code aus 6 Buchstaben und Zahlen. Tippe ihn auf deinem Handy ein und tippe auf Koppeln. Dafür brauchst du die Fernbedienung nicht.',
      'Jetzt kannst du Pfeile, OK, Zurück, Home, Lautstärke, Stummschaltung und Tastatur nutzen. Sie sind kostenlos. Das Touchpad und die App-Liste sind Pro.',
      'Um den Fernseher beim nächsten Mal vom Handy aus einzuschalten, suche in den Netzwerk- oder Energieeinstellungen nach „Wake on LAN“, „Einschalten über Netzwerk“ oder „Netzwerk-Standby“.',
    ],
    extra=[
      ('Wenn sich dein Fernseher nicht vom Handy aus einschalten lässt', 'Nicht jeder Android TV kann über das Netzwerk eingeschaltet werden; das hängt vom Hersteller und vom Modell ab. Hat deiner die Funktion nicht, schalte ihn mit der Taste am Fernseher ein und mache am Handy weiter. Ausschalten kannst du ihn über die App.'),
      ('Chromecast mit Google TV, Google TV Streamer und Shield', 'Sie verbinden sich auf die gleiche Weise: gleiches WLAN, Gerät in der Liste antippen und den Code eingeben. Zeigt der Fernseher einen anderen Eingang, wechsle ihn auf den HDMI-Anschluss, an dem das Gerät steckt, wie in [HDMI-Eingang am Fernseher ohne Fernbedienung wechseln](@hdmi) erklärt.'),
      ('Wenn der Code nicht erscheint oder als falsch gemeldet wird', 'Prüfe, ob der Fernseher wirklich eingeschaltet ist und nicht im Standby. Der Code ändert sich bei jeder Anfrage: Nur der letzte funktioniert. Mehr Details findest du unter [Android TV fragt nach einem Kopplungscode](@androidtv-code).'),
      ('Google-App oder Mando TV', 'Google hat eine eigene App, für die du ein Google-Konto brauchst. Mando TV verlangt kein Konto, funktioniert auch unter Windows und steuert Fernseher von LG, Samsung und Roku mit derselben App.'),
    ],
    marca='android',
    faq=[
      ('Brauche ich die Fernbedienung, um mein Handy zu koppeln?', 'Nein. Der Code erscheint auf dem Bildschirm des Fernsehers und du tippst ihn auf dem Handy ein. Du musst nur den Fernseher einschalten, bei Bedarf mit der Taste am Gerät.'),
      ('Funktioniert es mit einem Hisense?', 'Bei Hisense-Fernsehern mit Android TV oder Google TV ja. Hisense-Fernseher mit einem anderen System sind nicht kompatibel.'),
      ('Kann ich mit der Tastatur meines Handys tippen?', 'Ja. Die Tastatur ist kostenlos und funktioniert für die Suche in YouTube, Netflix und den übrigen Apps.'),
    ]),
  dict(clave='lg-on', corto='LG Fernseher mit Handy einschalten',
    titulo='LG Fernseher mit dem Handy einschalten (Anleitung)',
    desc='LG Fernseher per WLAN mit dem Handy einschalten: Aktiviere „Fernseher per Mobilgerät einschalten“ und nutze Mando TV. Schritt für Schritt, gratis.',
    h1='So schaltest du einen LG-Fernseher mit dem Handy ein',
    intro='Du kannst einen LG-Fernseher mit dem Handy einschalten, musst dafür aber zuerst eine Einstellung am Fernseher aktivieren. Danach schaltet dein Handy den LG-Fernseher über dein WLAN ein, ganz ohne Fernbedienung. Es dauert fünf Minuten und du machst es nur einmal.',
    pasos=[
      'Verbinde dein Handy und den LG-Fernseher mit demselben WLAN.',
      'Öffne am Fernseher die Einstellungen und suche „Fernseher per Mobilgerät einschalten“. Je nach Modell findest du es unter Allgemein oder Verbindung.',
      'Aktiviere „Über WLAN einschalten“. Ist dein Fernseher per Netzwerkkabel verbunden, aktiviere stattdessen die Option für das Kabel.',
      'Hat dein Fernseher „Quick Start+“, aktiviere es ebenfalls.',
      'Öffne bei eingeschaltetem Fernseher Mando TV auf deinem Handy und tippe in der Liste auf deinen LG-Fernseher. Bestätige die Abfrage, die auf dem Bildschirm erscheint. So lernt die App, ihn aufzuwecken.',
      'Schalte den Fernseher aus und probiere es: Tippe in Mando TV auf den Fernseher, und die App fragt, ob sie ihn einschalten soll.',
    ],
    extra=[
      ('Wenn er sich nicht einschaltet', 'Der Fernseher muss im selben WLAN gewesen sein, als er ausgeschaltet wurde. Prüfe, ob die Einstellung noch aktiv ist und dein Handy im selben Netzwerk ist. Hast du den Router gewechselt, verbinde dich noch einmal bei eingeschaltetem Fernseher.'),
    ],
    marca='lg',
    faq=[
      ('Kann ich den LG-Fernseher mit dem Handy einschalten, wenn ich ihn nie verbunden habe?', 'Nein. Zuerst musst du am Fernseher „Fernseher per Mobilgerät einschalten“ aktivieren und dich einmal mit Mando TV verbinden, während der Fernseher an ist.'),
      ('Brauche ich die LG ThinQ App?', 'Nein. Mando TV verbindet sich direkt über dein WLAN und verlangt kein LG-Konto.'),
      ('Funktioniert es mit mobilen Daten?', 'Nein. Handy und Fernseher müssen im selben WLAN sein.'),
    ]),
  dict(clave='console', corto='Fernseher und Konsole ohne Fernbedienung',
    titulo='Keine Fernbedienung? Fernseher einschalten, HDMI wechseln',
    desc='Release-Tag und keine Fernbedienung? Schalte den Fernseher ein und wechsle mit dem Handy auf den HDMI-Eingang deiner PS5 oder Xbox. Gratis, ohne Werbung.',
    h1='So schaltest du den Fernseher ein und wechselst ohne Fernbedienung auf den HDMI-Eingang deiner Konsole',
    intro='Release-Tag von GTA VI, die Konsole ist startklar und die Fernbedienung ist irgendwo zwischen den Sofakissen verschwunden. Das passiert öfter, als man denkt. Mit Mando TV schaltet dein Handy den Fernseher ein und wechselt über dein WLAN zu Hause auf den Eingang deiner PlayStation oder Xbox.',
    pasos=[
      'Verbinde dein Handy mit demselben WLAN wie den Fernseher.',
      'Öffne Mando TV und tippe in der Liste auf deinen Fernseher (Samsung, LG, Roku oder Android TV).',
      'Ist der Fernseher aus, tippe auf Einschalten. Das klappt, wenn am Fernseher das Einschalten über das Netzwerk aktiviert ist. Hast du das nie aktiviert, schalte den Fernseher dieses eine Mal mit der Taste am Gerät ein und aktiviere es für das nächste Mal.',
      'Schalte die Konsole ein. Ist HDMI-CEC aktiviert (siehe den kostenlosen Trick weiter unten), wechselt der Fernseher von selbst auf ihren Eingang.',
      'Wechselt er nicht, tippe in Mando TV auf Eingänge (eine Pro-Funktion) und wähle den HDMI-Anschluss, an dem die Konsole steckt: HDMI 1, HDMI 2 und so weiter.',
      'Für die Lautstärke nutzt du beim Spielen die großen Tasten in der App.',
    ],
    extra=[
      ('Der kostenlose Trick: Lass die Konsole den Fernseher umschalten', 'Die PS5 und die Xbox können den Fernseher einschalten und gleich beim Start auf ihren HDMI-Eingang springen, dank HDMI-CEC. Bei der PS5 findest du es unter Einstellungen > System > HDMI > HDMI-Geräteverknüpfung aktivieren. Öffne bei der Xbox Einstellungen > Allgemein > TV- und Anzeigeoptionen und suche die Option für die Gerätesteuerung. Am Fernseher heißt die Funktion je nach Marke anders: Anynet+ bei Samsung, SIMPLINK bei LG und BRAVIA Sync oder HDMI-Steuerung bei anderen.'),
      ('Wenn der Fernseher auf einem anderen Bild bleibt', 'Ist die Konsole an, aber der Fernseher zeigt noch Antenne oder eine App, hat er den Eingang nicht gewechselt. Tippe auf deinem Handy auf Eingänge (Pro) und wähle den HDMI-Eingang der Konsole. Ohne Pro nutzt du die Pfeile und OK, um zu den Eingängen des Fernsehers zu kommen, oder die Taste am Fernseher selbst, und wählst den HDMI-Anschluss. Die Nummer ist der Anschluss, an dem du das Kabel der Konsole eingesteckt hast.'),
      ('Wenn es ein Roku TV ist', 'Die Taste am Fernseher, meist unten in der Mitte oder an der Rückseite, schaltet ihn ein. Von dort aus erledigt dein Handy den Rest.'),
    ],
    marca=None,
    faq=[
      ('Hat Mando TV etwas mit GTA VI zu tun?', 'Nein. Mando TV steht in keiner Verbindung zu Rockstar Games oder Take-Two. Die App hilft dir nur, keine Spielzeit zu verlieren, weil du die Fernbedienung nicht findest.'),
      ('Ist das Wechseln des HDMI-Eingangs kostenlos?', 'Die Eingangsliste gehört zu Mando TV Pro, einem Einmalkauf ohne Abo. Kostenlos kannst du den Fernseher einschalten, Pfeile, OK und Lautstärke nutzen und die Konsole den Eingang mit HDMI-CEC von selbst wechseln lassen.'),
      ('Funktioniert es mit meinem Fernseher?', 'Es funktioniert mit Fernsehern von Samsung, LG, Roku und Android TV im selben WLAN. Ist deiner von einer anderen Marke, kann dir der HDMI-CEC-Trick trotzdem helfen.'),
      ('Kann ich es nutzen, um GTA VI (GTA 6) auf der PS5 oder Xbox zu spielen?', 'Mando TV greift weder in die Konsole noch ins Spiel ein. Es sorgt nur dafür, dass der Fernseher an ist und auf dem richtigen HDMI-Eingang läuft, damit du dich hinsetzen und spielen kannst.'),
    ]),
  dict(clave='samsung-lost', corto='Samsung Fernseher ohne Fernbedienung',
    titulo='Samsung Fernbedienung verloren? Nutze dein Handy',
    desc='Samsung Fernbedienung verloren oder defekt? Nutze dein Handy per WLAN als Fernbedienung für Tizen-Fernseher. Einfach mit Mando TV, gratis, ohne Werbung.',
    h1='Samsung Fernseher ohne Original-Fernbedienung: So nutzt du dein Handy',
    intro='Wenn du deine Samsung Fernbedienung verloren hast oder sie nicht mehr funktioniert, kannst du dein Handy über das WLAN als Fernbedienung nutzen. Es funktioniert bei Samsung-Fernsehern mit Tizen, Baujahr 2016 und neuer.',
    pasos=[
      'Schalte den Fernseher mit der Taste am Gerät ein. Bei den meisten Modellen sitzt sie unten oder an der Rückseite, manchmal als kleiner Joystick.',
      'Prüfe, ob der Fernseher mit deinem WLAN verbunden ist und dein Handy im selben Netzwerk ist.',
      'Öffne Mando TV auf deinem Handy. Dein Samsung-Fernseher erscheint von selbst in der Liste. Tippe darauf.',
      'Der Fernseher bittet dich, die Verbindung zu bestätigen. Bei den meisten Modellen bestätigst du sie mit den Tasten am Fernseher oder mit dem Joystick an der Rückseite.',
      'Fertig, jetzt kannst du dein Handy als Fernbedienung nutzen. Die Tasten und die Tastatur sind kostenlos; das Touchpad und die Apps sind Pro-Funktionen.',
      'Um den Fernseher beim nächsten Mal vom Handy aus einzuschalten, gehe zu Einstellungen > Allgemein > Netzwerk > Experteneinstellungen und aktiviere „Mit Mobilgerät einschalten“.',
    ],
    extra=[
      ('Wenn der Fernseher nicht um Erlaubnis fragt', 'Vielleicht ist die Erlaubnis schon gespeichert oder der Fernseher ist in einem anderen WLAN. Schließe Mando TV und öffne die App erneut bei eingeschaltetem Fernseher. Ist der Fernseher älter als 2016, nutzt er ein anderes System, das noch nicht unterstützt wird.'),
      ('Wenn du die Erlaubnis versehentlich abgelehnt hast', 'Gehe am Fernseher zu Einstellungen > Allgemein > Externer Geräte-Manager > Geräteverbindungs-Manager und stelle Mando TV auf erlaubt. Findet dein Handy den Fernseher trotzdem nicht, lies [Dein Handy findet den Fernseher nicht](@not-found).'),
    ],
    marca='samsung',
    faq=[
      ('Wie bestätige ich die Verbindung, wenn ich keine Fernbedienung habe?', 'Bei den meisten Modellen bestätigst du sie mit den Tasten am Fernseher oder mit dem Joystick an der Rückseite. Hat dein Modell keine Tasten, schreibe an hola@mandotv.app und wir helfen dir.'),
      ('Verlangt Mando TV ein Samsung-Konto?', 'Nein. Die Verbindung läuft direkt über dein WLAN, ohne Samsung-Konto.'),
      ('Funktioniert es mit meinem älteren Samsung-Fernseher?', 'Es funktioniert mit Samsung-Fernsehern mit Tizen, Baujahr 2016 und neuer.'),
    ]),
  dict(clave='wifi', corto='Handy als Fernbedienung per WLAN',
    titulo='Handy als Fernbedienung nutzen: Fernseher per WLAN steuern',
    desc='Verbinde dein Handy per WLAN mit dem Fernseher und nutze es als Fernbedienung bei Samsung, LG, Roku und Google TV. Schritte je Marke mit Mando TV. Gratis.',
    h1='So verbindest du dein Handy per WLAN als Fernbedienung mit dem Fernseher',
    intro='Du brauchst nur dein Handy und deinen Fernseher im selben WLAN sowie eine Fernbedienungs-App. Mando TV findet deinen Fernseher von selbst und funktioniert mit Samsung, LG, Roku, Google TV und Android TV.',
    pasos=[
      'Verbinde Handy und Fernseher mit demselben WLAN.',
      'Öffne Mando TV. Dein Fernseher erscheint von selbst in der Liste. Tippe darauf.',
      'Bestätige die Verbindung für deine Marke (die Einzelheiten stehen weiter unten).',
      'Steuere den Fernseher mit den Tasten oder mit der Tastatur deines Handys. Das Touchpad ist eine Pro-Funktion.',
    ],
    extra=[
      ('Samsung', 'Der Fernseher fragt, ob du die Verbindung zulässt. Bestätige sie beim ersten Mal auf dem Bildschirm. Es funktioniert mit Tizen, Baujahr 2016 und neuer. Um ihn vom Handy aus einzuschalten, aktiviere unter Einstellungen > Allgemein > Netzwerk > Experteneinstellungen die Option „Mit Mobilgerät einschalten“.'),
      ('LG', 'Der Fernseher zeigt eine Abfrage, die um Erlaubnis bittet. Bestätige sie beim ersten Mal. Um ihn vom Handy aus einzuschalten, suche in den Einstellungen „Fernseher per Mobilgerät einschalten“ und aktiviere „Über WLAN einschalten“.'),
      ('Roku', 'Roku verlangt keine Kopplung: Tippe in der Liste darauf und du bist verbunden. Um ihn einzuschalten, aktiviere unter Einstellungen > System > Energie die Option „Schneller TV-Start“.'),
      ('Google TV und Android TV', 'Der Fernseher zeigt einen Code auf dem Bildschirm. Gib ihn beim ersten Mal in Mando TV ein. Um ihn einzuschalten, suche in den Einstellungen nach „Wake on LAN“, „Einschalten über Netzwerk“ oder „Netzwerk-Standby“.'),
    ],
    marca=None,
    faq=[
      ('Brauche ich Internet, um mein Handy als Fernbedienung zu nutzen?', 'Du brauchst dein Handy und den Fernseher im selben WLAN. Mando TV verbindet sich über dieses Netzwerk direkt mit deinem Fernseher.'),
      ('Warum erscheint mein Fernseher nicht in der Liste?', 'Prüfe, ob der Fernseher an ist und dein Handy nicht mobile Daten oder ein anderes WLAN nutzt. Manche Router haben ein Gastnetzwerk, das Geräte voneinander trennt.'),
      ('Kann ich Mando TV auf dem iPhone oder auf einem Android-Handy nutzen?', 'Auf iPhone und iPad ja: Die App ist schon im App Store. Für Windows gibt es sie auch im Microsoft Store. Android kommt bald: Du kannst beim kostenlosen frühen Zugang bei Google Play mitmachen.'),
    ]),
  dict(clave='pc', corto='Fernseher mit dem PC steuern',
    titulo='Fernseher mit dem Windows-PC steuern (kostenlos)',
    desc='Nutze deinen Windows-PC als Fernbedienung für Samsung, LG, Roku oder Google TV per WLAN. Tasten und Tastatur gratis; Apps und PC-Tastenkürzel mit Pro.',
    h1='So steuerst du deinen Fernseher mit einem Windows-PC',
    intro='Wenn du den Tag vor dem Computer verbringst, musst du nicht nach der Fernbedienung suchen: Mando TV für Windows steuert deinen Samsung-, LG-, Roku-, Google-TV- oder Android-TV-Fernseher über dein WLAN zu Hause. Praktisch zum Wechseln der Apps, zum Lauterstellen oder zum Tippen in YouTube mit der PC-Tastatur.',
    pasos=[
      'Lade Mando TV kostenlos aus dem Microsoft Store auf deinen Computer mit Windows 10 oder 11.',
      'Prüfe, ob Computer und Fernseher im selben Netzwerk sind (WLAN oder Kabel, aber über denselben Router).',
      'Öffne Mando TV: Dein Fernseher erscheint von selbst in der Liste. Tippe oder klicke darauf.',
      'Bestätige beim ersten Mal die Verbindung auf dem Bildschirm des Fernsehers (bei Google TV und Android TV gibst du den Code ein, den der Fernseher zeigt).',
      'Fertig: Nutze die Tasten oder die Tastatur, um im Suchfeld des Fernsehers zu tippen. Das Touchpad ist eine Pro-Funktion.',
    ],
    extra=[
      ('Tastenkürzel am PC (Pro)', 'Mit Mando TV Pro steuerst du den Fernseher mit der Computertastatur: Pfeiltasten zum Navigieren, Enter für OK, Rücktaste oder Esc für Zurück, + und - für die Lautstärke, M für Stummschaltung und Leertaste für Pause.'),
      ('Mini-Fernbedienung immer im Vordergrund (Pro)', 'Behalte ein kleines Fenster mit der Fernbedienung immer sichtbar, während du arbeitest oder am PC spielst.'),
    ],
    marca=None,
    faq=[
      ('Brauche ich ein Kabel oder Bluetooth, um den Fernseher mit dem PC zu steuern?', 'Nein. Mando TV verbindet sich über dein Heimnetzwerk: PC und Fernseher müssen nur am selben Router hängen.'),
      ('Funktioniert es mit jedem Fernseher?', 'Es funktioniert mit Samsung-Fernsehern mit Tizen (Baujahr 2016 und neuer), LG mit webOS, Roku sowie Google TV oder Android TV (Sony, TCL, Philips, Xiaomi und andere).'),
      ('Was kostet es?', 'Die Tasten, die Tastatur und das Einschalten über das Netzwerk sind kostenlos und ohne Werbung. Mando TV Pro ist ein Einmalkauf ohne Abo für Extras wie das Touchpad, die Apps, die PC-Tastenkürzel und die Mini-Fernbedienung.'),
    ]),
  dict(clave='roku-403', corto='Roku App funktioniert nicht',
    titulo='Roku App funktioniert nicht? Fehler 403 beheben',
    desc='Handy verbunden, aber der Roku reagiert nicht? Aktiviere „Steuerung durch mobile Apps“ in 5 Schritten und nutze dein Handy wieder als Fernbedienung.',
    h1='Roku App funktioniert nicht: So behebst du das Problem',
    intro='Wenn dein Handy den Roku findet und sich verbindet, aber keine Taste etwas bewirkt, liegt es fast immer an einer Einstellung am Roku selbst, die Fernbedienungs-Apps blockiert. Neuere Roku-Versionen sind standardmäßig stärker eingeschränkt. Im Roku-Menü ist das in einer Minute behoben.',
    pasos=[
      'Drücke am Roku Home und gehe zu Einstellungen.',
      'Öffne System und dann Erweiterte Systemeinstellungen.',
      'Gehe zu „Steuerung durch mobile Apps“. Bei manchen Modellen heißt es „Externe Steuerung“.',
      'Wähle unter „Netzwerkzugriff“ Standard oder Permissiv. Ist es bei deinem Modell nur ein Schalter, lass ihn auf Aktiviert.',
      'Gehe zurück zu Mando TV auf deinem Handy und tippe auf deinen Roku. Die Tasten reagieren jetzt.',
    ],
    extra=[
      ('So erkennst du, ob das dein Problem ist', 'Das Zeichen ist eindeutig: Dein Handy sieht den Roku in der Liste und verbindet sich, aber nichts passiert, wenn du eine Taste antippst. Intern antwortet der Roku mit Fehler 403, was „verboten“ bedeutet. Mando TV erkennt das beim Verbinden und zeigt dir genau diese Schritte auf dem Bildschirm.'),
      ('Standard oder Permissiv, was wähle ich?', 'Standard reicht: Es akzeptiert Befehle aus deinem Heimnetzwerk, und das braucht eine Fernbedienung. Permissiv ist offener und nur in ungewöhnlichen Netzwerken nötig.'),
      ('Wenn du die Roku Fernbedienung nicht hast', 'Steht die Einstellung auf Deaktiviert, lässt sie sich nur mit der echten Roku Fernbedienung ändern. Leihe dir eine aus, um es einmal zu ändern; danach kannst du alles mit deinem Handy machen. Lies auch [Roku Fernbedienung verloren](@roku-lost).'),
    ],
    marca='roku',
    faq=[
      ('Warum reagiert mein Roku nicht mehr, obwohl es früher funktioniert hat?', 'Ein Roku-Update kann diese Einstellung stärker einschränken. Es liegt nicht an deinem Handy oder deinem WLAN: Du musst nur die Steuerung durch Apps wieder erlauben.'),
      ('Gilt das für Roku TV und für Roku Player?', 'Ja. Die Einstellung steht bei Roku-Playern und bei Roku-TV-Geräten im selben Menü.'),
      ('Ist es sicher, die Einstellung auf Standard zu lassen?', 'Ja. Sie akzeptiert nur Befehle von Geräten in deinem Heimnetzwerk.'),
    ]),
  dict(clave='not-found', corto='Handy findet den Fernseher nicht',
    titulo='Handy findet den Fernseher nicht? 6 Dinge zum Prüfen',
    desc='Findet die Fernbedienungs-App deinen Fernseher nicht? Prüfe WLAN, VPN und Zugriff auf das lokale Netzwerk. Für Samsung, LG, Roku und Android TV.',
    h1='Dein Handy findet den Fernseher nicht: Das solltest du prüfen',
    intro='Du öffnest die Fernbedienungs-App und die Liste ist leer, oder der Fernseher erscheint, aber die Verbindung bricht ab. Fast immer liegt es am Netzwerk und nicht am Fernseher. Prüfe diese Punkte der Reihe nach: Der erste löst die meisten Fälle.',
    pasos=[
      'Schau, in welchem WLAN dein Handy ist und in welchem der Fernseher. Es muss dasselbe Netzwerk mit demselben Namen sein. Ein Gastnetzwerk funktioniert nicht, weil es Geräte voneinander trennt.',
      'Schalte das VPN auf deinem Handy aus, falls du eines nutzt. Bei aktivem VPN geht dein Handy über ein anderes Netzwerk ins Internet und sieht die Geräte bei dir zu Hause nicht, oder die Verbindung bricht nach wenigen Sekunden ab.',
      'Schalte kurz die mobilen Daten aus. Manche Handys wechseln bei schwachem Signal von selbst vom WLAN zu mobilen Daten.',
      'Schalte den Fernseher ein und warte, bis er fertig gestartet ist. Ein ausgeschalteter Fernseher antwortet nicht auf die Suche.',
      'Prüfe beim iPhone, ob die App die Berechtigung „Lokales Netzwerk“ hat: Einstellungen > Datenschutz & Sicherheit > Lokales Netzwerk.',
      'Erscheint er immer noch nicht, füge ihn von Hand hinzu: Tippe in Mando TV auf „Per IP hinzufügen“ und gib die IP-Adresse des Fernsehers ein.',
    ],
    extra=[
      ('Wo du die IP-Adresse des Fernsehers findest', 'Sie steht im Netzwerkmenü des Fernsehers und ist je nach Modell etwas anders. Bei LG: Einstellungen, Netzwerk, WLAN-Verbindung, Erweiterte WLAN-Einstellungen. Bei Samsung: Einstellungen, Allgemein, Netzwerk, Netzwerkstatus, IP-Einstellungen. Bei Roku: Einstellungen, Netzwerk, Info. Bei Android TV und Google TV: Einstellungen, Netzwerk & Internet, dann auf dein Netzwerk tippen. Es ist eine Zahl wie 192.168.1.86.'),
      ('Wenn er erscheint, aber die Verbindung abbricht', 'Bricht die Verbindung nach wenigen Sekunden ab, liegt die Ursache meist am Handy: ein VPN, der Wechsel in ein anderes WLAN oder der Energiesparmodus. Schalte das VPN aus, bleibe im selben WLAN und versuche es erneut.'),
      ('WLAN mit 2,4 und 5 GHz', 'Es spielt keine Rolle, ob dein Handy im 5-GHz-Netz und der Fernseher im 2,4-GHz-Netz ist, solange beide vom selben Router kommen. Hast du einen WLAN-Repeater und der Fernseher erscheint trotzdem nicht, gehe mit dem Handy näher an den Haupt-Router und versuche es erneut.'),
    ],
    marca=None,
    faq=[
      ('Kann ich den Fernseher mit mobilen Daten steuern?', 'Nein. Das Fernbedienungssignal läuft über dein WLAN zu Hause, deshalb müssen Handy und Fernseher im selben Netzwerk sein.'),
      ('Warum funktioniert es mit aktivem VPN nicht?', 'Weil das VPN den gesamten Datenverkehr deines Handys über ein anderes Netzwerk leitet und das Handy die Geräte bei dir zu Hause nicht mehr sieht. Schalte es aus, solange du die Fernbedienung nutzt.'),
      ('Funktioniert es mit Bluetooth oder Infrarot?', 'Mando TV nutzt nur WLAN. Du brauchst weder Bluetooth noch einen Infrarot-Sender im Handy.'),
    ]),
  dict(clave='androidtv-code', corto='Android TV Kopplungscode',
    titulo='Android TV fragt nach einem Kopplungscode: Das ist zu tun',
    desc='Dein Android TV oder Google TV zeigt beim Verbinden einen Code mit 6 Zeichen. So gibst du ihn ein und das tust du, wenn er nicht erscheint oder falsch ist.',
    h1='Android TV fragt nach einem Kopplungscode: Das ist zu tun',
    intro='Wenn du dein Handy zum ersten Mal mit einem Android TV oder Google TV verbindest, zeigt der Fernseher einen Code mit 6 Zeichen auf dem Bildschirm. Das ist normal und passiert nur einmal: So ist sichergestellt, dass niemand sonst deinen Fernseher steuern kann. Hier siehst du, wie du ihn eingibst und was du tust, wenn er nicht erscheint.',
    pasos=[
      'Schalte den Fernseher ein und lass den Startbildschirm sichtbar.',
      'Öffne Mando TV auf deinem Handy, im selben WLAN wie der Fernseher, und tippe in der Liste auf deinen Fernseher.',
      'Schau auf den Bildschirm des Fernsehers: Ein Code aus 6 Buchstaben und Zahlen erscheint.',
      'Tippe ihn genau so auf deinem Handy ein, wie er angezeigt wird, und tippe auf Koppeln. Die Buchstaben gehen nur von A bis F, ein rundes Zeichen ist also immer die Zahl Null.',
      'Fertig. Der Fernseher merkt sich dein Handy und fragt nicht noch einmal nach dem Code.',
    ],
    extra=[
      ('Wenn der Code nicht auf dem Fernseher erscheint', 'Prüfe, ob der Fernseher wirklich eingeschaltet ist und nicht im Standby, und ob dein Handy im selben WLAN ist. Tippe auf deinem Handy noch einmal auf den Fernseher. Erscheint er immer noch nicht, starte den Fernseher neu: Ziehe den Stecker zehn Sekunden lang, stecke ihn wieder ein und versuche es erneut.'),
      ('Wenn der Code als falsch gemeldet wird', 'Der Code ändert sich bei jeder Anfrage. Hast du lange gebraucht oder ihn zweimal angefordert, funktioniert nur der letzte auf dem Bildschirm. Tippe auf deinem Handy noch einmal auf den Fernseher und gib den neuen Code ein.'),
      ('Wenn der Fernseher erneut nach dem Code fragt', 'Das passiert, wenn der Fernseher auf Werkseinstellungen zurückgesetzt wurde oder du die App-Daten auf deinem Handy löschst. Koppele erneut, dann ist er gespeichert. Hast du gar keine Fernbedienung, lies [Android TV ohne Fernbedienung](@androidtv).'),
    ],
    marca='android',
    faq=[
      ('Welche Fernseher nutzen diesen Code?', 'Die mit Android TV oder Google TV: Sony, TCL, Philips, Xiaomi, Chromecast mit Google TV und einige mehr.'),
      ('Brauche ich ein Google-Konto auf meinem Handy?', 'Nein. Der Code auf dem Bildschirm ist alles, was du brauchst.'),
      ('Ist das sicher?', 'Ja. Der Code beweist, dass du vor dem Fernseher sitzt: Niemand kann koppeln, ohne ihn auf dem Bildschirm zu sehen.'),
    ]),
  dict(clave='roku-lost', corto='Roku Fernbedienung verloren',
    titulo='Roku Fernbedienung verloren? Nutze dein Handy per WLAN',
    desc='Roku Fernbedienung verloren? Dein Handy ersetzt sie per WLAN. Einfache Schritte, auch wenn du den Router gewechselt hast und der Roku kein WLAN hat.',
    h1='Roku Fernbedienung verloren: So nutzt du dein Handy',
    intro='Wenn du deine Roku Fernbedienung verloren hast oder sie nicht mehr funktioniert, ersetzt dein Handy sie, solange der Roku noch mit deinem WLAN verbunden ist. Und wenn du das WLAN oder den Router gewechselt hast, gibt es auch dafür einen Ausweg.',
    pasos=[
      'Schalte den Fernseher ein und lass den Roku angeschlossen. Du musst nichts daran anfassen.',
      'Verbinde dein Handy mit demselben WLAN, das der Roku nutzt.',
      'Öffne Mando TV. Der Roku erscheint von selbst in der Liste. Tippe darauf.',
      'Nutze Pfeile, OK, Home und Zurück wie bei deiner gewohnten Fernbedienung. Der Roku fragt nicht nach einem Code.',
      'Tun die Tasten nichts, blockiert der Roku die Steuerung durch Apps: Der Ratgeber [Roku App funktioniert nicht](@roku-403) erklärt, wie du sie erlaubst.',
    ],
    extra=[
      ('Wenn der Roku kein WLAN hat (Router gewechselt oder umgezogen)', 'Ohne Fernbedienung kommst du nicht ins Menü, um das neue Netzwerk einzurichten, aber es gibt einen Trick: Der Roku verbindet sich von selbst mit einem Netzwerk, das denselben Namen und dasselbe Passwort hat wie das alte. Richte auf einem anderen Handy einen WLAN-Hotspot mit genau diesem Namen und Passwort ein, verbinde das Handy mit Mando TV damit, und der Roku erscheint in der Liste. Gehe von dort zu Einstellungen, Netzwerk und verbinde ihn mit dem neuen WLAN.'),
      ('Wenn es ein Roku TV ist', 'Roku-TV-Geräte haben eine Taste am Gerät, fast immer unten in der Mitte oder an der Rückseite, die den Fernseher einschaltet. Das reicht, um ihn einzuschalten und mit dem Handy weiterzumachen.'),
      ('Wenn du lieber eine andere Fernbedienung kaufst', 'Achte darauf, dass sie zu deinem Modell passt. Kleine Roku-Player hinter dem Fernseher brauchen eine Fernbedienung ohne Infrarot, weil Infrarot sie nicht erreicht.'),
    ],
    marca='roku',
    faq=[
      ('Kann mein Handy den Roku einschalten?', 'Ein angeschlossener Roku-Player ist immer an. Bei einem Roku TV schaltet Mando TV ihn per WLAN ein, wenn „Schneller TV-Start“ unter Einstellungen > System > Energie aktiviert ist.'),
      ('Und die Lautstärke?', 'Bei einem Roku TV stellt dein Handy die Lautstärke lauter und leiser. Bei einem Roku-Player, der per HDMI angeschlossen ist, hängt es vom Fernseher ab: Bei vielen funktioniert es, bei anderen nicht.'),
      ('Muss ich ein Konto anlegen?', 'Nein. Mando TV verlangt kein Konto und steuert außerdem Fernseher von Samsung, LG und Android TV mit derselben App.'),
    ]),
]

SOPORTE = dict(
  titulo='Hilfe: Fernseher mit Mando TV verbinden und einschalten',
  desc='So verbindest du die Mando TV Fernbedienung mit LG, Samsung, Roku oder Android TV, schaltest den Fernseher vom Handy ein und löst Probleme.',
  h1='Hilfe',
  intro='Die häufigsten Fragen, in der Reihenfolge der Schritte. Findest du deine nicht, schreib uns an <a href="mailto:hola@mandotv.app?subject=Hilfe%20zu%20Mando%20TV">hola@mandotv.app</a> und wir antworten.',
)
SOPORTE_HTML = '''      <h2 id="encontrar">Den Fernseher finden</h2>
      <div class="preguntas">
        <details open><summary>Mein Fernseher erscheint nicht in der Liste</summary>
          <ol>
            <li>Prüfe, ob dein Handy und der Fernseher im selben WLAN sind. Hat dein Router ein 2,4-GHz- und ein 5-GHz-Netz mit unterschiedlichen Namen, sehen sie sich manchmal nicht.</li>
            <li>Stelle sicher, dass der Fernseher eingeschaltet ist.</li>
            <li>Prüfe beim iPhone, ob Mando TV die Berechtigung „Lokales Netzwerk“ hat, unter Einstellungen, Mando TV.</li>
            <li>Erscheint er immer noch nicht, tippe auf die Taste +, wähle die Marke und gib die IP-Adresse des Fernsehers ein. Du siehst sie im Netzwerkmenü des Fernsehers (zum Beispiel 192.168.1.50).</li>
          </ol>
        </details>
        <details><summary>Funktioniert es mit mobilen Daten oder von unterwegs?</summary>
          <p>Nein. Mando TV spricht mit dem Fernseher innerhalb deines Heimnetzwerks, dein Handy muss also mit diesem WLAN verbunden sein.</p>
        </details>
      </div>

      <h2 id="conectar">Zum ersten Mal verbinden</h2>
      <p>Komplette Ratgeber nach Marke: <a href="@@R_lg@@">LG</a>, <a href="@@R_samsung@@">Samsung</a>, <a href="@@R_roku@@">Roku</a> und <a href="@@R_android@@">Android TV</a>.</p>
      <div class="preguntas">
        <details><summary>LG</summary>
          <p>Wenn du auf den Fernseher tippst, erscheint auf dem Bildschirm eine Abfrage, die um Erlaubnis bittet. Bestätige sie mit deiner gewohnten Fernbedienung. Das machst du nur einmal.</p>
        </details>
        <details><summary>Samsung</summary>
          <p>Der Fernseher fragt, ob du die Verbindung von Mando TV zulässt. Wähle mit der Fernbedienung „Zulassen“. Hast du sie versehentlich abgelehnt, gehe zu Einstellungen > Allgemein > Externer Geräte-Manager > Geräteverbindungs-Manager und ändere es auf erlaubt.</p>
        </details>
        <details><summary>Roku</summary>
          <p>Roku fragt nicht nach einer Erlaubnis. Klappt die Verbindung nicht, gehe am Roku zu Einstellungen > System > Erweiterte Systemeinstellungen > Steuerung durch mobile Apps und lass den Netzwerkzugriff auf Standard oder Permissiv.</p>
        </details>
        <details><summary>Android TV und Google TV</summary>
          <p>Der Fernseher zeigt einen Code mit 6 Zeichen. Gib ihn genau so in Mando TV ein, wie er erscheint. Es funktioniert bei Sony, TCL, Philips, Xiaomi, Chromecast mit Google TV und anderen mit Android TV.</p>
        </details>
      </div>

      <h2 id="encender">Den Fernseher über die App einschalten</h2>
      <p>Mando TV schaltet den Fernseher über dein Heimnetzwerk ein. Dafür sind zwei Dinge nötig: Du hast dich mindestens einmal bei eingeschaltetem Fernseher verbunden, und am Fernseher ist das Einschalten über das Netzwerk aktiviert. Der Name der Einstellung ändert sich je nach Modell; das sind die häufigsten:</p>
      <div class="preguntas">
        <details><summary>LG</summary>
          <p>Suche in den Einstellungen (je nach Modell unter Allgemein oder Verbindung) nach „Fernseher per Mobilgerät einschalten“ und aktiviere „Über WLAN einschalten“. Gibt es „Quick Start+“, aktiviere es ebenfalls.</p>
        </details>
        <details><summary>Samsung</summary>
          <p>Aktiviere „Mit Mobilgerät einschalten“ unter Einstellungen > Allgemein > Netzwerk > Experteneinstellungen.</p>
        </details>
        <details><summary>Roku</summary>
          <p>Aktiviere bei Roku-TV-Geräten „Schneller TV-Start“ unter Einstellungen > System > Energie. Roku-Player, die an einen Fernseher angeschlossen sind, lassen sich so nicht einschalten.</p>
        </details>
        <details><summary>Android TV und Google TV</summary>
          <p>Das hängt vom Hersteller ab. Suche in den Netzwerk- oder Energieeinstellungen nach „Wake on LAN“, „Einschalten über Netzwerk“ oder „Netzwerk-Standby“. Manche Modelle haben diese Option nicht.</p>
        </details>
      </div>

      <h2 id="falla">Wenn etwas nicht klappt</h2>
      <div class="preguntas">
        <details><summary>Die Verbindung bricht ab oder es kommt keine Reaktion</summary>
          <ol>
            <li>Tippe auf dem Fernbedienungsbildschirm auf Neu verbinden.</li>
            <li>Hilft das nicht, schließe Mando TV und öffne die App erneut.</li>
            <li>Hat der Fernseher eine andere IP-Adresse bekommen, entferne ihn aus der Liste und füge ihn erneut hinzu.</li>
          </ol>
        </details>
        <details><summary>So schickst du uns einen Fehlerbericht</summary>
          <ol>
            <li>Tippe in Mando TV auf die Schaltfläche Anpassen (die Regler oben).</li>
            <li>Tippe auf Testbericht kopieren.</li>
            <li>Füge ihn zusammen mit Marke und Modell deines Fernsehers in eine E-Mail an hola@mandotv.app ein.</li>
          </ol>
          <p>Der Bericht enthält keine Passwörter, keine Codes und nichts, was du tippst.</p>
        </details>
        <details><summary>Ich habe Pro gekauft und es erscheint nicht</summary>
          <p>Tippe unter Anpassen auf Kauf wiederherstellen, mit demselben Store-Konto, mit dem du gekauft hast. Erscheint es immer noch nicht, schreib uns.</p>
        </details>
      </div>

      <h2 id="guias">Ratgeber Schritt für Schritt</h2>
      <p><a href="@@R_guias@@">Alle Ratgeber ansehen</a></p>
      <ul>
@@GUIAS@@
      </ul>

      <h2 id="contacto">Noch Fragen?</h2>
      <p>Schreib uns an <a href="mailto:hola@mandotv.app?subject=Hilfe%20zu%20Mando%20TV">hola@mandotv.app</a>. Sag uns Marke und Modell deines Fernsehers und bei welchem Schritt du nicht weiterkommst.</p>
'''

PRIVACIDAD = dict(
  titulo='Datenschutzerklärung | Mando TV',
  desc='Mando TV erhebt keine personenbezogenen Daten: keine Konten, keine Werbung, keine Tracker. Die App spricht nur mit deinem Fernseher innerhalb deines WLANs.',
  h1='Datenschutz',
  intro='Kurz gesagt: Mando TV erhebt deine Daten nicht. Es gibt keine Konten, keine Werbung, keine Tracker und keine eigenen Server, die speichern, was du tust.',
)
PRIVACIDAD_HTML = '''      <p class="fecha">Gültig seit dem 14. November 2026. Zuletzt aktualisiert am 15. November 2026.</p>

      <h2>Wer wir sind</h2>
      <p>Mando TV ist eine App, mit der du deinen Fernseher von deinem Handy oder Computer aus steuerst. Diese Erklärung beschreibt, welche Informationen die App verwendet und was sie damit macht. Bei Fragen schreib uns an <a href="mailto:hola@mandotv.app">hola@mandotv.app</a>.</p>

      <h2>Welche Daten wir erheben</h2>
      <p>Die App: keine. Die App sendet weder Informationen über dich noch darüber, wie du sie nutzt, an uns oder an Dritte. Sie verwendet keine Analyse-, Werbe- oder Tracking-Werkzeuge.</p>
      <p>Diese Website: Wir messen Besuche auf zwei Arten, die im Abschnitt <a href="#cookies">Cookies auf dieser Website</a> erklärt sind.</p>

      <h2>Was die App auf deinem Gerät speichert</h2>
      <p>Damit sie funktioniert, speichert die App Folgendes nur auf deinem Handy oder Computer:</p>
      <ul>
        <li>Die Fernseher, die du hinzugefügt hast: Name, Marke, IP-Adresse in deinem Netzwerk und Hardware-Adresse des Netzwerks (MAC), die zum Einschalten verwendet wird.</li>
        <li>Die Verbindungsschlüssel, die jeder Fernseher übergibt, wenn du die Erlaubnis bestätigst. Sie werden verschlüsselt im sicheren Speicher des Systems abgelegt (Schlüsselbund auf iPhone und Mac, Keystore auf Android, geschützter Speicher unter Windows).</li>
        <li>Deine Einstellungen: helles oder dunkles Design, Hintergrundfarbe, Vibration und Art der Fernbedienung.</li>
        <li>Wenn du die Pro-Funktionen nutzt: deine Lieblings-Apps, deine Routinen und deine letzten YouTube-Suchen (du kannst sie in der App löschen).</li>
      </ul>
      <p>Wenn du die App löschst, wird all das mit ihr gelöscht.</p>

      <h2>Mit wem die App spricht</h2>
      <p>Mit deinen Fernsehern, innerhalb deines WLANs zu Hause. Um sie zu finden, durchsucht die App dein lokales Netzwerk; deshalb fragt sie auf einem iPhone nach der Berechtigung „Lokales Netzwerk“. Der Text, den du mit der App-Tastatur eingibst, geht direkt an den Fernseher und wird nicht gespeichert.</p>
      <p>Außerdem lädt die App beim Öffnen eine kleine öffentliche Datei von dieser Website herunter (mandotv.app/app/config.json), um zu erfahren, ob es eine neue Version gibt, die du installieren solltest, und welche Funktionen zu Mando TV Pro gehören. Das ist ein Download, wie wenn man eine Seite öffnet: Die App sendet weder deine Daten noch deine Fernseher noch das, was du tust. Sie gibt nur die App-Version und das System an (zum Beispiel Android), damit sie dir den passenden Hinweis zeigen kann. Hast du kein Internet, arbeitet die App mit der zuletzt heruntergeladenen Datei weiter; vergehen mehr als 30 Tage, ohne dass sie heruntergeladen werden konnte, bittet dich die App, dich kurz mit dem Internet zu verbinden.</p>

      <h2>Mikrofon und Sprache</h2>
      <p>Die Sprachsuche nutzt das Mikrofon nur, solange du auf die Sprechtaste tippst. Was du sagst, wird von der Spracherkennung deines Systems in Text umgewandelt: von Apple auf iPhone und Mac, von Google auf Android und von Microsoft unter Windows, jeweils nach deren eigenen Datenschutzbestimmungen. Mando TV nimmt das Audio weder auf noch speichert es, und der entstandene Text geht direkt an deinen Fernseher, genau wie das, was du mit der Tastatur eingibst.</p>

      <h2>Testbericht</h2>
      <p>Die App hat eine Schaltfläche „Testbericht kopieren“, die uns hilft, Fehler zu beheben. Der Bericht bleibt nur im Speicher der App, solange sie geöffnet ist, und wird nie von selbst gesendet: Du entscheidest, ob du ihn kopierst und weitergibst. Er enthält keine Verbindungsschlüssel, keine Kopplungscodes und nichts, was du eingibst; nur die Schritte, die die App ausgeführt hat, wie Suchen, Verbinden und die Fehler.</p>

      <h2 id="cookies">Cookies auf dieser Website</h2>
      <p>Das gilt nur für die Website mandotv.app, nicht für die App.</p>
      <h3>Immer ohne Cookies</h3>
      <p>Wir zählen Besuche anonym mit Cloudflare Web Analytics: wie viele Personen die Website besuchen, welche Seiten sie lesen und aus welchem Land. Es verwendet keine Cookies, nutzt deine IP-Adresse nicht, um dich zu identifizieren, und verfolgt nicht, was du auf anderen Websites tust.</p>
      <h3>Mit Cookies, nur wenn du zustimmst</h3>
      <p>Wenn du im Cookie-Hinweis auf „Akzeptieren“ tippst, aktivieren wir Google Analytics (von Google LLC), um besser zu verstehen, wie die Website genutzt wird: Seitenaufrufe, Verweildauer, Gerätetyp, ungefähre Stadt und woher du kommst. Dafür speichert es die Cookies _ga und _ga_* bis zu 2 Jahre lang in deinem Browser. Google kann diese Daten auf Servern außerhalb von Chile verarbeiten. Wir haben die Werbefunktionen und Google Signals deaktiviert und nutzen diese Daten nicht, um dir Werbung zu zeigen.</p>
      <p>Wenn du auf „Ablehnen“ tippst oder nichts wählst, wird Google Analytics nicht geladen und es wird kein Cookie gespeichert. Du kannst deine Entscheidung jederzeit mit der Schaltfläche „Cookies“ am Ende jeder Seite ändern; wenn du die Zustimmung widerrufst, löschen wir diese Cookies.</p>
      <p>Deine Auswahl wird in deinem Browser gespeichert (lokaler Speicher, an niemanden gesendet), damit wir dich nicht noch einmal fragen.</p>

      <h2>Käufe</h2>
      <p>Wenn du Mando TV Pro kaufst, wird die Zahlung vom App-Store abgewickelt (App Store, Google Play oder Microsoft Store). Wir erhalten und speichern deine Kartendaten nicht. Der Store bestätigt der App nur, dass der Kauf existiert.</p>

      <h2>E-Mails, die du uns schickst</h2>
      <p>Wenn du uns an <a href="mailto:hola@mandotv.app">hola@mandotv.app</a> schreibst, verwenden wir deine E-Mail-Adresse und das, was du uns mitteilst, nur, um dir zu antworten. Wir geben sie nicht weiter und nutzen sie nicht für Werbung. Du kannst jederzeit verlangen, dass wir deine Nachrichten löschen.</p>

      <h2>Kinder</h2>
      <p>Die App erhebt von niemandem Daten, auch nicht von Kindern.</p>

      <h2>Änderungen dieser Erklärung</h2>
      <p>Sollte sich eines Tages ändern, was die App mit deinen Daten macht, aktualisieren wir diese Seite und das Datum oben, bevor die Änderung die App erreicht.</p>
'''
