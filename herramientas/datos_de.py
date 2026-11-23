# Textos en alemán (du) de mandotv.app. Los usa generar_idiomas.py. Escritos para las búsquedas de Alemania, Austria y Suiza.
# Las claves de las páginas (lg, lost-tv, ...) y sus rutas están en idiomas_sitio.py.
# Los nombres de menús de cada marca (LG, Samsung, Roku, Android TV, iPhone) son los mismos que usa la app en alemán
# (lib/l10n/app_de.arb del proyecto de la app).

UI = dict(
  locale='de_DE',
  aria_home='Mando TV, Startseite', aria_main='Hauptmenü', nav_que='Funktionen', nav_ayuda='Hilfe', nav_contacto='Kontakt',
  asunto='Hallo%20Mando%20TV', inicio='Startseite', privacidad='Datenschutz', aria_pie='Fußbereich', aria_ruta='Brotkrumenpfad',
  aria_marcas='Marken und Ratgeber', hecho='Entwickelt in Chile',
  aviso='Mando TV ist eine unabhängige App. Sie steht weder mit den genannten TV-Herstellern noch mit Google, Amazon, Apple oder Roku in Verbindung und wird nicht von ihnen unterstützt. Die Marken gehören ihren Inhabern und werden nur genannt, um die Kompatibilität anzugeben. Android TV und Google TV sind Marken von Google LLC. Apple TV ist eine Marke von Apple Inc.',
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
    desc='Dein Handy oder PC als LG TV Fernbedienung für webOS, per WLAN. Tasten, Tastatur, Apps, Eingänge und Einschalten gratis; Zeiger mit Pro.',
    h1='LG TV Fernbedienung als App fürs Handy',
    intro='Mando TV ist eine Fernbedienungs-App für LG-Fernseher: Sie macht dein Handy oder deinen Computer über das WLAN zu Hause zur Fernbedienung deines LG Smart-TVs mit webOS. Das hilft, wenn du die Fernbedienung verloren hast, die Batterien leer sind oder du einfach schneller tippen möchtest.',
    compat='LG Smart-TVs mit webOS (die meisten LG-Smart-TV-Modelle seit 2014). Funktioniert mit LED-, NanoCell-, QNED- und OLED-Fernsehern. Ältere LG-Smart-TVs mit NetCast (2011 bis 2014, vor webOS) werden neu in der Beta unterstützt: Sie koppeln sich mit dem 6-stelligen Schlüssel, den der Fernseher anzeigt.',
    h2=dict(funciones='Das kannst du mit deinem LG-Fernseher machen', como='So verbindest du deinen LG-Fernseher mit Mando TV',
            encender='LG-Fernseher mit dem Handy einschalten', preguntas='Fragen zu LG', guias='Ratgeber für LG'),
    funciones=[
      ('Alle Tasten', 'Steuerkreuz, OK, Zurück, Home, Lautstärke, Programme, Stummschaltung und Wiedergabe.'),
      ('Zeiger wie bei der Magic Remote (Pro)', 'Bewege den Pfeil mit dem Finger über den Bildschirm, genau wie mit der LG Magic Remote.'),
      ('Tastatur', 'Tippe in YouTube, Netflix oder im Browser des Fernsehers mit der Tastatur deines Handys.'),
      ('Apps und Eingänge', 'Öffne deine Apps und wechsle zu HDMI, Live-TV, AirPlay oder Screen Share.'),
      ('Audioausgabe (Pro)', 'Wechsle zwischen den Lautsprechern des Fernsehers und deiner Soundbar.'),
      ('Fernseher einschalten', 'Ist er aus, schaltet Mando TV ihn über das Netzwerk ein und verbindet sich von selbst.'),
    ],
    pasos=[
      'Verbinde Handy und Fernseher mit demselben WLAN.',
      'Öffne Mando TV: Dein LG-Fernseher erscheint von selbst in der Liste. Tippe darauf.',
      'Auf dem Fernseher erscheint eine Abfrage, die um Erlaubnis bittet. Bestätige sie mit deiner gewohnten Fernbedienung (nur beim ersten Mal).',
    ],
    encender='Öffne am LG-Fernseher die Einstellungen und suche „Fernseher per Mobilgerät einschalten“ (je nach Modell unter Allgemein oder Verbindung). Aktiviere „Über WLAN einschalten“. Gibt es „Schnellstart+“, aktiviere es ebenfalls. Danach fragt dich die App, wenn du den ausgeschalteten Fernseher in Mando TV antippst, ob sie ihn einschalten soll, und verbindet sich von selbst.',
    faq=[
      ('Brauche ich die Magic Remote, um Mando TV zu nutzen?', 'Nur beim ersten Mal, um die Abfrage auf dem Bildschirm zu bestätigen. Danach reicht dein Handy.'),
      ('Ersetzt Mando TV die LG ThinQ App?', 'Zum Steuern des Fernsehers ja: Du brauchst weder ein LG-Konto noch musst du den Fernseher registrieren. Mando TV verbindet sich direkt über dein WLAN.'),
      ('Kann ich meinen LG-Fernseher mit dem Handy einschalten?', 'Ja, wenn du am Fernseher „Fernseher per Mobilgerät einschalten“ aktiviert und dich einmal verbunden hast, während der Fernseher an war.'),
      ('Funktioniert es mit älteren LG-Fernsehern aus der Zeit vor webOS?', 'In der Beta ja, mit LG-NetCast-Smart-TVs von 2011 bis 2014. Sie koppeln sich mit dem 6-stelligen Schlüssel, den der Fernseher anzeigt. Die Funktion ist neu und kann noch Ecken und Kanten haben.'),
    ],
    guias=[('lg-on', 'So schaltest du einen LG-Fernseher mit dem Handy ein'),
           ('lost-lg', 'LG Fernbedienung verloren: So nutzt du dein Handy'),
           ('hdmi', 'HDMI-Eingang am Fernseher ohne Fernbedienung wechseln'),
           ('guias', 'Alle Ratgeber, um den Fernseher mit dem Handy zu steuern')]),
  dict(clave='samsung', color='#3d7bff', corto='Samsung',
    titulo='Samsung TV Fernbedienung App fürs Handy | Mando TV',
    desc='Dein Handy oder PC als Samsung TV Fernbedienung für Tizen, per WLAN. Tasten, Tastatur, Apps und Einschalten gratis; Touchpad mit Pro. Ohne Werbung.',
    h1='Samsung TV Fernbedienung als App fürs Handy',
    intro='Mando TV ist eine Fernbedienungs-App für Samsung-Fernseher: Sie macht dein Handy oder deinen Computer über das WLAN zu Hause zur Fernbedienung deines Samsung Smart-TVs. Du brauchst weder ein Samsung-Konto noch musst du den Fernseher registrieren.',
    compat='Samsung Smart-TVs mit Tizen, Baujahr 2016 und neuer (Serien wie Crystal UHD, QLED, Neo QLED, The Frame und OLED).',
    h2=dict(funciones='Das kannst du mit deinem Samsung-Fernseher machen', como='So verbindest du deinen Samsung-Fernseher mit Mando TV',
            encender='Samsung-Fernseher mit dem Handy einschalten', preguntas='Fragen zu Samsung', guias='Ratgeber für Samsung'),
    funciones=[
      ('Alle Tasten', 'Steuerkreuz, OK, Zurück, Home, Lautstärke, Programme, Stummschaltung und Quelle.'),
      ('Touchpad (Pro)', 'Wische mit dem Finger durch die Menüs, ohne nach den Pfeiltasten zu suchen.'),
      ('Tastatur', 'Tippe Suchbegriffe und Passwörter mit der Tastatur deines Handys.'),
      ('Apps', 'Öffne Netflix, YouTube, Prime Video und deine anderen Apps mit einem Tipp.'),
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
    desc='Dein Handy oder PC als Roku Fernbedienung für Roku TV und Roku Player, per WLAN. Tasten, Tastatur, Kanäle, Eingänge und Einschalten gratis.',
    h1='Roku Fernbedienung als App fürs Handy',
    intro='Mando TV ist eine Fernbedienungs-App für Roku: Sie macht dein Handy oder deinen Computer über das WLAN zu Hause zur Fernbedienung deines Roku. Sie funktioniert mit Roku-TV-Geräten und mit Roku-Playern, die an den HDMI-Anschluss kommen.',
    compat='Roku-TV-Geräte (TCL, Hisense, Philips, Sharp, JVC und andere) und Roku-Player (Express, Streaming Stick, Ultra).',
    h2=dict(funciones='Das kannst du mit deinem Roku machen', como='So verbindest du deinen Roku mit Mando TV',
            encender='Roku mit dem Handy einschalten', preguntas='Fragen zu Roku', guias='Ratgeber für Roku'),
    funciones=[
      ('Alle Tasten', 'Steuerkreuz, OK, Zurück, Home, Lautstärke, Stummschaltung, Wiederholen und Wiedergabe.'),
      ('Tastatur', 'Tippe Suchbegriffe in Roku-Kanälen mit der Tastatur deines Handys.'),
      ('Kanäle', 'Öffne Netflix, YouTube und deine anderen Roku-Kanäle mit einem Tipp.'),
      ('Eingänge', 'Wechsle bei einem Roku TV in der App zu HDMI, Antenne oder AV.'),
      ('Fernseher einschalten', 'Bei Roku-TV-Geräten mit Schnellstart schaltet Mando TV sie von deinem Handy aus ein.'),
      ('Ohne Kopplung', 'Roku fragt nicht nach einem Code: Tippe in der Liste darauf und du bist verbunden.'),
      ('Fernbedienung klingeln lassen', 'Hat deine Roku-Fernbedienung einen Lautsprecher, etwa die Roku Voice Remote Pro, lässt Mando TV sie klingeln, damit du sie findest. Kostenlos, der Roku muss eingeschaltet sein.'),
    ],
    pasos=[
      'Verbinde Handy und Roku mit demselben WLAN.',
      'Öffne Mando TV: Dein Roku erscheint von selbst in der Liste. Tippe darauf.',
      'Falls die Verbindung nicht klappt, gehe am Roku zu Einstellungen > System > Erweiterte Systemeinstellungen > Steuerung durch mobile Apps und stelle den Netzwerkzugriff auf Standard oder Aktiviert.',
    ],
    encender='Aktiviere bei Roku-TV-Geräten unter Einstellungen > System > Energie die Option „TV-Schnellstart“. Roku-Player, die an einen anderen Fernseher angeschlossen sind, lassen sich so nicht einschalten. Danach fragt dich die App, wenn du den ausgeschalteten Fernseher in Mando TV antippst, ob sie ihn einschalten soll, und verbindet sich von selbst.',
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
    desc='Dein Handy oder PC als Android TV Fernbedienung (Sony, TCL, Xiaomi), per WLAN. Tasten, Tastatur, Apps und Einschalten gratis; Touchpad mit Pro.',
    h1='Android TV Fernbedienung als App fürs Handy',
    intro='Mando TV ist eine Fernbedienungs-App für Android TV: Sie macht dein Handy oder deinen Computer über das WLAN zu Hause zur Fernbedienung deines Android-TV- oder Google-TV-Fernsehers. Sie funktioniert auch vom iPhone und von Windows aus.',
    compat='Fernseher mit Google TV oder Android TV von Sony, Philips, TCL, Hisense, Sharp, Xiaomi, Toshiba, Panasonic, Haier, Skyworth, JVC, Thomson, Motorola, OnePlus, iFFALCON, Kogan, Vu und anderen Marken, dazu Chromecast mit Google TV, Google TV Streamer, onn. und Nvidia Shield. Manche dieser Marken verkaufen auch Modelle mit einem anderen System: Zeigt dein Fernseher den Startbildschirm von Google TV oder hat er den Google Play Store, steuert Mando TV ihn.',
    h2=dict(funciones='Das kannst du mit deinem Android TV machen', como='So verbindest du deinen Android TV mit Mando TV',
            encender='Android TV mit dem Handy einschalten', preguntas='Fragen zu Android TV', guias='Ratgeber für Android TV'),
    funciones=[
      ('Alle Tasten', 'Steuerkreuz, OK, Zurück, Home, Lautstärke, Stummschaltung und Wiedergabe.'),
      ('Touchpad (Pro)', 'Wische mit dem Finger, um schnell durch die Menüs von Google TV zu navigieren.'),
      ('Tastatur', 'Tippe Suchbegriffe und Passwörter mit der Tastatur deines Handys.'),
      ('Apps', 'Öffne YouTube, Netflix, Disney+ und deine anderen Apps mit einem Tipp.'),
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
      ('Was kostenlos ist und was Pro', 'Fernseher ein- und ausschalten, Pfeile, OK, Lautstärke, Programme, Zifferntasten, Tastatur, das Öffnen von Apps und das Wechseln des Eingangs sind kostenlos. Das Touchpad, Sprache und Routinen gehören zu Mando TV Pro, einem Einmalkauf ohne Abo.'),
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
      'Fertig. Pfeile, OK, Zurück, Home, Lautstärke, Programme und Tastatur sind kostenlos. Der Zeiger ist eine Pro-Funktion.',
      'Rufe bei verbundener App mit den Pfeilen und OK die Einstellungen auf und aktiviere „Fernseher per Mobilgerät einschalten“. Der Ratgeber [LG Fernseher mit dem Handy einschalten](@lg-on) zeigt, wo du die Option findest.',
    ],
    extra=[
      ('Wenn der Fernseher die Abfrage nicht anzeigt', 'Vielleicht ist die Erlaubnis schon gespeichert oder dein Handy ist in einem anderen Netzwerk. Prüfe, ob beide im selben WLAN sind und das VPN aus ist. Erscheint der Fernseher nicht in der Liste, hilft dir [Dein Handy findet den Fernseher nicht](@not-found) weiter.'),
      ('Wenn der Fernseher sein WLAN verloren hat', 'Stecke den Fernseher mit einem Netzwerkkabel in den Router, dann nutzt er es von selbst. Oder richte ein WLAN mit demselben Namen und Passwort wie vorher ein, denn der Fernseher verbindet sich meist von selbst damit.'),
      ('Wenn der Fernseher auf einem anderen Eingang hängt', 'Tippe auf deinem Handy auf Eingänge und wähle den HDMI-Anschluss. Mehr dazu steht in [HDMI-Eingang am Fernseher ohne Fernbedienung wechseln](@hdmi).'),
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
      'Tippe bei LG und Roku auf Eingänge und wähle den HDMI-Anschluss. Bei Samsung sendet Eingänge die Quelle-Taste an den Fernseher, und du wählst mit den Pfeilen und OK.',
      'Du kannst auch mit den Pfeilen und OK auf dem Startbildschirm des Fernsehers zu den Eingängen gehen. Je nach Marke und Baujahr heißen sie Quelle, Verbundene Geräte oder Eingänge. Bei einem Roku TV sind es die HDMI-Kacheln auf dem Startbildschirm.',
    ],
    extra=[
      ('Samsung', 'Hat das Menü der Taste am Fernseher keinen Punkt Quelle, öffne mit deinem Handy das Menü des Startbildschirms und suche links nach Quelle oder Verbundene Geräte. Du steuerst es mit den Pfeilen und OK in Mando TV, die kostenlos sind.'),
      ('LG', 'Drücke den Joystick am Fernseher und suche Eingänge. Mit deinem Handy kannst du in Mando TV auch die Eingangsliste öffnen und den gewünschten Eingang antippen.'),
      ('Roku TV', 'Auf dem Startbildschirm gibt es für jeden Eingang eine Kachel, zum Beispiel HDMI 1 oder HDMI 2. Bewege dich mit den Pfeilen und öffne sie mit OK, kostenlos.'),
      ('Wenn es ein Fernseher mit Android TV oder Google TV ist', 'In Mando TV gibt es die Eingangsliste für Android TV noch nicht. Nutze die Eingangstaste am Fernseher selbst oder erreiche die Eingänge mit den Pfeilen und OK vom Startbildschirm aus. Wenn du keine Fernbedienung hast und dich verbinden möchtest, lies [Android TV ohne Fernbedienung](@androidtv).'),
      ('Mehr Hilfe', 'Schaltet sich der Fernseher gar nicht ein oder weißt du nicht, wo du anfangen sollst, lies [Fernbedienung verloren](@lost-tv). Zum Spielen an der Konsole enthält der Ratgeber [Fernseher einschalten und auf Konsolen-HDMI wechseln, ohne Fernbedienung](@console) den HDMI-CEC-Trick.'),
    ],
    marca=None,
    faq=[
      ('Ist das Wechseln des HDMI-Eingangs kostenlos?', 'Ja. Die Eingangsliste in Mando TV ist kostenlos, genau wie das Einschalten des Fernsehers und die Pfeile, OK und Lautstärke. Die Eingänge erreichst du auch über das Menü des Fernsehers.'),
      ('Woher weiß ich, welchen HDMI-Eingang ich brauche?', 'Schau dir die HDMI-Anschlüsse am Fernseher an: Jeder hat eine Nummer. Nimm den, an dem das Kabel deiner Konsole oder deines Players steckt.'),
      ('Was ist, wenn sich der Fernseher nicht einschaltet?', 'Schalte ihn mit seiner Taste am Gerät ein. Hast du ihn schon einmal verbunden und das Einschalten über das Netzwerk aktiviert, kannst du ihn auch über dein Handy einschalten.'),
    ]),
  dict(clave='androidtv', corto='Android TV ohne Fernbedienung',
    titulo='Android TV ohne Fernbedienung: Nutze dein Handy',
    desc='Keine Android-TV- oder Google-TV-Fernbedienung? Verbinde dein Handy mit dem 6-stelligen Code auf dem Bildschirm. Gratis, ohne Konto, ohne Werbung.',
    h1='Android TV ohne Fernbedienung: So nutzt du dein Handy',
    intro='Wenn du die Fernbedienung deines Android TV oder Google TV verloren hast oder ihre Batterien leer sind, ersetzt dein Handy sie. Das Beste: Für die Verbindung brauchst du die Fernbedienung nicht, denn der Fernseher zeigt einen Code auf dem Bildschirm und du tippst ihn auf dem Handy ein. Es funktioniert bei Fernsehern von Sony, Philips, TCL, Hisense, Sharp und Xiaomi mit Android TV, bei Chromecast mit Google TV und bei Nvidia Shield.',
    pasos=[
      'Schalte den Fernseher mit der Taste am Gerät ein. Sie sitzt fast immer unten in der Mitte oder an der Rückseite nahe einer Ecke.',
      'Verbinde dein Handy mit demselben WLAN wie den Fernseher.',
      'Lade Mando TV herunter, das kostenlos ist und kein Google-Konto verlangt, und öffne die App. Tippe in der Liste auf deinen Fernseher.',
      'Der Fernseher zeigt einen Code aus 6 Buchstaben und Zahlen. Tippe ihn auf deinem Handy ein und tippe auf Koppeln. Dafür brauchst du die Fernbedienung nicht.',
      'Jetzt kannst du Pfeile, OK, Zurück, Home, Lautstärke, Stummschaltung und Tastatur nutzen. Sie sind kostenlos, ebenso die App-Liste. Das Touchpad ist Pro.',
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
      'Hat dein Fernseher „Schnellstart+“, aktiviere es ebenfalls.',
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
      'Wechselt er nicht, tippe in Mando TV auf Eingänge und wähle den HDMI-Anschluss, an dem die Konsole steckt: HDMI 1, HDMI 2 und so weiter.',
      'Für die Lautstärke nutzt du beim Spielen die großen Tasten in der App.',
    ],
    extra=[
      ('Der kostenlose Trick: Lass die Konsole den Fernseher umschalten', 'Die PS5 und die Xbox können den Fernseher einschalten und gleich beim Start auf ihren HDMI-Eingang springen, dank HDMI-CEC. Bei der PS5 findest du es unter Einstellungen > System > HDMI > HDMI-Geräteverknüpfung aktivieren. Öffne bei der Xbox Einstellungen > Allgemein > TV- und Anzeigeoptionen und suche die Option für die Gerätesteuerung. Am Fernseher heißt die Funktion je nach Marke anders: Anynet+ bei Samsung, SIMPLINK bei LG und BRAVIA Sync oder HDMI-Steuerung bei anderen.'),
      ('Wenn der Fernseher auf einem anderen Bild bleibt', 'Ist die Konsole an, aber der Fernseher zeigt noch Antenne oder eine App, hat er den Eingang nicht gewechselt. Tippe auf deinem Handy auf Eingänge und wähle den HDMI-Eingang der Konsole. Oder nutze die Pfeile und OK, um zu den Eingängen des Fernsehers zu kommen, oder die Taste am Fernseher selbst, und wähle den HDMI-Anschluss. Die Nummer ist der Anschluss, an dem du das Kabel der Konsole eingesteckt hast.'),
      ('Wenn es ein Roku TV ist', 'Die Taste am Fernseher, meist unten in der Mitte oder an der Rückseite, schaltet ihn ein. Von dort aus erledigt dein Handy den Rest.'),
    ],
    marca=None,
    faq=[
      ('Hat Mando TV etwas mit GTA VI zu tun?', 'Nein. Mando TV steht in keiner Verbindung zu Rockstar Games oder Take-Two. Die App hilft dir nur, keine Spielzeit zu verlieren, weil du die Fernbedienung nicht findest.'),
      ('Ist das Wechseln des HDMI-Eingangs kostenlos?', 'Ja. Die Eingangsliste in Mando TV ist kostenlos, genau wie das Einschalten des Fernsehers und die Pfeile, OK und Lautstärke. Du kannst die Konsole den Eingang auch mit HDMI-CEC von selbst wechseln lassen.'),
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
      'Fertig, jetzt kannst du dein Handy als Fernbedienung nutzen. Die Tasten, die Tastatur und die Apps sind kostenlos; das Touchpad ist eine Pro-Funktion.',
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
      ('Roku', 'Roku verlangt keine Kopplung: Tippe in der Liste darauf und du bist verbunden. Um ihn einzuschalten, aktiviere unter Einstellungen > System > Energie die Option „TV-Schnellstart“.'),
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
    desc='Nutze deinen Windows-PC als Fernbedienung für Samsung, LG, Roku oder Google TV per WLAN. Tasten, Tastatur und Apps gratis; PC-Tastenkürzel mit Pro.',
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
      ('Mit dem Fernseher vom PC aus sprechen (Pro)', 'Mit Mando TV Pro gibst du dem Fernseher Befehle über das Mikrofon des PCs: „öffne YouTube“, „mach lauter“ oder „schalte in 30 Minuten aus“, ganz wie du sprichst. Unter Windows wird die Sprache auf dem PC selbst erkannt: Du brauchst kein Internet, musst in den Windows-Einstellungen nichts ändern, und es funktioniert in den 6 Sprachen der App. Was du sagst, verlässt den PC nicht und wird nicht gespeichert. Nur bei sehr alten Prozessoren greift die App auf das Diktieren von Windows zurück. Dafür muss die Online-Spracherkennung in den Datenschutz-Einstellungen eingeschaltet und Deutsch (Deutschland) in Windows hinzugefügt sein. Fehlt dann etwas, sagt die App Bescheid und öffnet die Einstellung mit einem Button.'),
    ],
    marca=None,
    faq=[
      ('Brauche ich ein Kabel oder Bluetooth, um den Fernseher mit dem PC zu steuern?', 'Nein. Mando TV verbindet sich über dein Heimnetzwerk: PC und Fernseher müssen nur am selben Router hängen.'),
      ('Funktioniert es mit jedem Fernseher?', 'Es funktioniert mit Samsung-Fernsehern mit Tizen (Baujahr 2016 und neuer), LG mit webOS, Roku sowie Google TV oder Android TV (Sony, Philips, TCL, Hisense, Sharp, Xiaomi, Toshiba, Panasonic, Haier, Skyworth und andere).'),
      ('Was kostet es?', 'Die Tasten, die Tastatur und das Einschalten über das Netzwerk sind kostenlos und ohne Werbung. Mando TV Pro ist ein Einmalkauf ohne Abo für Extras wie das Touchpad, die PC-Tastenkürzel und die Mini-Fernbedienung.'),
      ('Warum versteht mich das Mikrofon unter Windows nicht?', 'Prüfe, ob die Sprachfunktion aktiv ist (sie gehört zu Pro) und ob das Mikrofon des PCs unter Windows funktioniert. Auf fast allen PCs wird die Sprache auf dem Gerät selbst erkannt, ganz ohne Internet. Nur bei sehr alten Prozessoren nutzt die App das Diktieren von Windows. Prüfe dann, ob die Online-Spracherkennung in den Datenschutz-Einstellungen von Windows eingeschaltet ist und Windows Deutsch (Deutschland) in den Spracheinstellungen hat. Mando TV nutzt diese Sprache nur, solange es zuhört.'),
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
      'Wähle unter „Netzwerkzugriff“ Standard oder Aktiviert. Ist es bei deinem Modell nur ein Schalter, lass ihn auf Aktiviert.',
      'Gehe zurück zu Mando TV auf deinem Handy und tippe auf deinen Roku. Die Tasten reagieren jetzt.',
    ],
    extra=[
      ('So erkennst du, ob das dein Problem ist', 'Das Zeichen ist eindeutig: Dein Handy sieht den Roku in der Liste und verbindet sich, aber nichts passiert, wenn du eine Taste antippst. Intern antwortet der Roku mit Fehler 403, was „verboten“ bedeutet. Mando TV erkennt das beim Verbinden und zeigt dir genau diese Schritte auf dem Bildschirm.'),
      ('Standard oder Aktiviert, was wähle ich?', 'Beides funktioniert: Mando TV braucht nur Befehle aus deinem Heimnetzwerk. Steht die Option auf Deaktiviert (bei neuerer Software Eingeschränkt), reagiert der Roku nicht auf Apps.'),
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
      ('Lass dich von der App führen', 'In der Fernseherliste gibt es eine Schaltfläche für den Fall, dass dein Fernseher nicht erscheint. Die App prüft die häufigsten Ursachen Schritt für Schritt (gleiches WLAN, VPN, Berechtigung für das lokale Netzwerk und mehr) und zeigt nach jeder Korrektur eine Schaltfläche zum erneuten Prüfen. Der Assistent ist kostenlos.'),
      ('Wo du die IP-Adresse des Fernsehers findest', 'Sie steht im Netzwerkmenü des Fernsehers und ist je nach Modell etwas anders. Bei LG: Einstellungen, Netzwerk, WLAN-Verbindung, Erweiterte WLAN-Einstellungen. Bei Samsung: Einstellungen, Allgemein, Netzwerk, Netzwerkstatus, IP-Einstellungen. Bei Roku: Einstellungen, Netzwerk, Info. Bei Android TV und Google TV: Einstellungen, Netzwerk & Internet, dann auf dein Netzwerk tippen. Es ist eine Zahl wie 192.168.1.86.'),
      ('Wenn er erscheint, aber die Verbindung abbricht', 'Bricht die Verbindung nach wenigen Sekunden ab, liegt die Ursache meist am Handy: ein VPN, der Wechsel in ein anderes WLAN oder der Energiesparmodus. Schalte das VPN aus, bleibe im selben WLAN und versuche es erneut.'),
      ('WLAN mit 2,4 und 5 GHz', 'Es spielt keine Rolle, ob dein Handy im 5-GHz-Netz und der Fernseher im 2,4-GHz-Netz ist, solange beide vom selben Router kommen. Hast du einen WLAN-Repeater und der Fernseher erscheint trotzdem nicht, gehe mit dem Handy näher an den Haupt-Router und versuche es erneut.'),
    ],
    marca=None,
    faq=[
      ('Kann ich den Fernseher mit mobilen Daten steuern?', 'Nein. Das Fernbedienungssignal läuft über dein WLAN zu Hause, deshalb müssen Handy und Fernseher im selben Netzwerk sein.'),
      ('Warum funktioniert es mit aktivem VPN nicht?', 'Weil das VPN den gesamten Datenverkehr deines Handys über ein anderes Netzwerk leitet und das Handy die Geräte bei dir zu Hause nicht mehr sieht. Schalte es aus, solange du die Fernbedienung nutzt.'),
      ('Funktioniert es mit Bluetooth oder Infrarot?', 'Bei Smart-TVs nutzt Mando TV das WLAN. Infrarot funktioniert nur auf Android-Handys mit Infrarotsender und ist für Fernseher gedacht, die keine Smart-TVs sind. Bluetooth gibt es in der Beta, kostenlos und nur ab Android 9: Das Handy verbindet sich mit dem Fernseher als Bluetooth-Tastatur und -Fernbedienung, ganz ohne WLAN. Es funktioniert mit Google TV, Android TV und Fire TV; bei anderen Marken, die Bluetooth-Tastaturen akzeptieren, kann es funktionieren, Roku akzeptiert sie nicht.'),
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
      ('Welche Fernseher nutzen diesen Code?', 'Die mit Android TV oder Google TV: Sony, Philips, TCL, Hisense, Sharp, Xiaomi, Chromecast mit Google TV und einige mehr.'),
      ('Brauche ich ein Google-Konto auf meinem Handy?', 'Nein. Der Code auf dem Bildschirm ist alles, was du brauchst.'),
      ('Ist das sicher?', 'Ja. Der Code beweist, dass du vor dem Fernseher sitzt: Niemand kann koppeln, ohne ihn auf dem Bildschirm zu sehen.'),
    ]),
  dict(clave='roku-lost', corto='Roku Fernbedienung verloren',
    titulo='Roku Fernbedienung verloren? Nutze dein Handy per WLAN',
    desc='Roku Fernbedienung verloren? Dein Handy ersetzt sie per WLAN. Einfache Schritte, auch wenn du den Router gewechselt hast und der Roku kein WLAN hat.',
    h1='Roku Fernbedienung verloren: So nutzt du dein Handy',
    intro='Wenn du deine Roku Fernbedienung verloren hast oder sie nicht mehr funktioniert, ersetzt dein Handy sie, solange der Roku noch mit deinem WLAN verbunden ist. Und wenn du das WLAN oder den Router gewechselt hast, gibt es auch dafür einen Ausweg.',
    pasos=[
      'Versuche zuerst, die Fernbedienung klingeln zu lassen. Hat deine Roku-Fernbedienung einen Lautsprecher, zum Beispiel die Roku Voice Remote Pro, öffne Mando TV, verbinde dich mit dem Roku und nutze die Option, die Fernbedienung klingeln zu lassen, damit du sie findest. Das klappt nur mit Roku-Fernbedienungen mit Lautsprecher, und der Roku muss eingeschaltet sein.',
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
      ('Kann mein Handy den Roku einschalten?', 'Ein angeschlossener Roku-Player ist immer an. Bei einem Roku TV schaltet Mando TV ihn per WLAN ein, wenn „TV-Schnellstart“ unter Einstellungen > System > Energie aktiviert ist.'),
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
            <li>Tippe in der Fernseherliste auf die Schaltfläche für den Fall, dass dein Fernseher nicht erscheint: Die App prüft die häufigsten Ursachen Schritt für Schritt (gleiches WLAN, VPN, Berechtigung für das lokale Netzwerk und mehr) und zeigt nach jeder Korrektur eine Schaltfläche zum erneuten Prüfen.</li>
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
          <p>Roku fragt nicht nach einer Erlaubnis. Klappt die Verbindung nicht, gehe am Roku zu Einstellungen > System > Erweiterte Systemeinstellungen > Steuerung durch mobile Apps und lass den Netzwerkzugriff auf Standard oder Aktiviert.</p>
        </details>
        <details><summary>Android TV und Google TV</summary>
          <p>Der Fernseher zeigt einen Code mit 6 Zeichen. Gib ihn genau so in Mando TV ein, wie er erscheint. Es funktioniert bei Sony, Philips, TCL, Hisense, Sharp, Xiaomi, Chromecast mit Google TV und anderen mit Android TV.</p>
        </details>
      </div>

      <h2 id="encender">Den Fernseher über die App einschalten</h2>
      <p>Mando TV schaltet den Fernseher über dein Heimnetzwerk ein. Dafür sind zwei Dinge nötig: Du hast dich mindestens einmal bei eingeschaltetem Fernseher verbunden, und am Fernseher ist das Einschalten über das Netzwerk aktiviert. Der Name der Einstellung ändert sich je nach Modell; das sind die häufigsten:</p>
      <div class="preguntas">
        <details><summary>LG</summary>
          <p>Suche in den Einstellungen (je nach Modell unter Allgemein oder Verbindung) nach „Fernseher per Mobilgerät einschalten“ und aktiviere „Über WLAN einschalten“. Gibt es „Schnellstart+“, aktiviere es ebenfalls.</p>
        </details>
        <details><summary>Samsung</summary>
          <p>Aktiviere „Mit Mobilgerät einschalten“ unter Einstellungen > Allgemein > Netzwerk > Experteneinstellungen.</p>
        </details>
        <details><summary>Roku</summary>
          <p>Aktiviere bei Roku-TV-Geräten „TV-Schnellstart“ unter Einstellungen > System > Energie. Roku-Player, die an einen Fernseher angeschlossen sind, lassen sich so nicht einschalten.</p>
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
      <p>Schreib uns an <a href="mailto:hola@mandotv.app?subject=Hilfe%20zu%20Mando%20TV">hola@mandotv.app</a>. Sag uns Marke und Modell deines Fernsehers und bei welchem Schritt du nicht weiterkommst. Schreib uns in deiner Sprache. Wir antworten auf Spanisch oder Englisch und, wenn du möchtest, in deiner Sprache mit Hilfe eines Übersetzers.</p>
'''

PRIVACIDAD = dict(
  titulo='Datenschutzerklärung | Mando TV',
  desc='Mando TV erhebt keine personenbezogenen Daten: keine Konten, keine Werbung, keine Tracker. Die App spricht nur mit deinem Fernseher innerhalb deines WLANs.',
  h1='Datenschutz',
  intro='Kurz gesagt: Mando TV erhebt deine Daten nicht. Es gibt keine Konten, keine Werbung, keine Tracker und keine eigenen Server, die speichern, was du tust.',
)
PRIVACIDAD_HTML = '''      <p class="fecha">Gültig seit dem 14. November 2026. Zuletzt aktualisiert am 21. November 2026.</p>

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

      <p>Wenn du Fotos oder Videos an den Fernseher sendest (eine Pro-Funktion), lädt der Fernseher nur die Dateien, die du auswählst, direkt von deinem Handy oder PC über dein WLAN zu Hause. Sie gehen weder über das Internet noch über uns, die App sieht deine übrigen Fotos nicht, und die Freigabe endet, sobald du diesen Bildschirm schließt.</p>
      <h2>Mikrofon und Sprache</h2>
      <p>Die Sprachsuche nutzt das Mikrofon nur, solange du auf die Sprechtaste tippst. Was du sagst, wird von der Spracherkennung deines Systems in Text umgewandelt: von Apple auf iPhone und Mac und von Google auf Android, jeweils nach deren eigenen Datenschutzbestimmungen. Unter Windows wird die Sprache auf deinem eigenen PC erkannt und verlässt das Gerät nicht; nur auf sehr alten Prozessoren nutzt die App die Spracheingabe von Windows, von Microsoft, nach deren Datenschutzbestimmungen. Mando TV nimmt das Audio weder auf noch speichert es, und der entstandene Text geht direkt an deinen Fernseher, genau wie das, was du mit der Tastatur eingibst.</p>

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


# >>> guías traídas del inglés (ensamblar.py)
# Adaptadas con Ollama (qwen3.6:35b) desde las guías inglesas y auditadas por Opus el 22-nov. Rutas en idiomas_sitio.py.
GUIAS += [
  dict(clave='no-sub', corto='Fernbedienungs-App ohne Abo', fecha='2026-11-23',
    titulo='Fernbedienungs-App für den Fernseher ohne Abo und Werbung',
    desc='Genervt von Fernbedienungs-Apps mit Werbung oder Wochen-Abo? Mando TV ist kostenlos und werbefrei, Pro ist ein optionaler Einmalkauf. Ehrlicher Vergleich.',
    h1='Eine Fernbedienungs-App ohne Abo und ohne Werbung',
    intro='Viele Universal-Fernbedienungen zeigen Werbung oder verlangen ein wöchentliches Abo, bevor sie funktionieren. Mando TV geht einen anderen Weg: Die Fernbedienung ist kostenlos, es gibt keine Werbung und kein Konto. Das optionale Pro kaufst du nur einmal. Hier der Vergleich, auch mit dem, was die App nicht kann.',
    pasos=[
      'Öffne vor der Installation die Store-Seite einer App und prüfe die In-App-Käufe. Wöchentliche oder monatliche Preise deuten auf ein Abo hin.',
      'Prüfe auf Google Play, ob auf der Seite „Enthält Werbung“ steht, und lies die neuesten Bewertungen mit wenigen Sternen: Dort tauchen oft unerwartete Bezahlschranken auf.',
      'Stelle sicher, dass die App deinen Fernseher über WLAN steuern kann. Mando TV funktioniert mit Samsung (ab 2016), LG webOS, Roku, Google TV, Android TV und Fire TV.',
      'Installiere Mando TV, verbinde dein Handy mit demselben WLAN wie den Fernseher und tippe in der Liste auf deinen Fernseher.',
      'Bestätige die Abfrage am Fernseher oder gib den angezeigten Code ein. Tasten, Lautstärke, Programme und Tastatur kosten nichts.',
    ],
    tabla=dict(titulo='Mando TV im Vergleich mit vielen Fernbedienungs-Apps',
      cabeza=['', 'Mando TV', 'Viele werbefinanzierte oder Abo-Apps'],
      filas=[
        ['Basis-Fernbedienung', 'Kostenlos', 'Oft kostenlos mit Werbung oder hinter einer Testphase versteckt'],
        ['Werbung', 'Keine', 'Häufig'],
        ['Abo', 'Keins. Pro ist ein optionaler Einmalkauf', 'Wöchentliche oder monatliche Pläne sind üblich'],
        ['Konto', 'Nicht nötig', 'Unterschiedlich'],
        ['Smart-TVs über WLAN', 'Samsung (ab 2016), LG webOS, Roku, Google TV, Android TV, Fire TV, Apple TV (Beta)', 'Je nach App'],
        ['Infrarot für ältere Fernseher', 'Kostenlos auf Android-Handys mit Infrarotsender (neu)', 'Einige Apps, nur bei Handys mit Infrarotsender'],
        ['Bluetooth', 'Beta ab Android 9, kostenlos', 'Je nach App'],
        ['Fotos und Videos auf den Fernseher', 'Pro, über WLAN (kein Spiegeln)', 'Je nach App'],
        ['Handys und Computer', 'iPhone, iPad und Windows, dazu Android im frühen Zugang', 'Unterschiedlich'],
        ['Bildschirmspiegelung', 'Kostenlos auf iPhone und iPad, über die Bildschirmsynchronisierung im Kontrollzentrum (Fernseher mit AirPlay)', 'Einige Apps bieten es an'],
      ],
      nota='Mando TV wird mit keiner bestimmten App verglichen. Die aktuellen Preise stehen auf der Store-Seite der jeweiligen App.'),
    extra=[
      ('Was Mando TV nicht macht', 'Eine eigene Bildschirmspiegelung hat es nicht: Auf iPhone und iPad führt es dich zur Bildschirmsynchronisierung im Kontrollzentrum, der Funktion des iPhone selbst, die mit Fernsehern mit AirPlay funktioniert. Mit Mando TV Pro kann es außerdem Fotos und Videos über dein WLAN an den Fernseher senden. Es steuert Smart-TVs über das Heim-WLAN. Fernseher ohne Smart-TV-Funktion lassen sich von einem Android-Handy mit Infrarotsender per Infrarot steuern. Ab Android 9 kann sich das Handy auch per Bluetooth als Tastatur und Fernbedienung mit Google TV, Android TV und Fire TV verbinden, ganz ohne WLAN. Diese Option ist in der Beta und kostenlos.'),
      ('Wie Mando TV Geld verdient', 'Nicht mit Werbung und nicht mit deinen Daten: Die App sammelt keine. Mando TV wird durch Pro finanziert, einen optionalen Einmalkauf für Extras. Die Basis-Fernbedienung ist kostenlos.'),
      ('Auf den Geräten, die du bereits hast', 'iPhone und iPad aus dem App Store, Windows-PCs aus dem Microsoft Store und Android über kostenlosen frühen Zugang auf Google Play. Siehe [Fernbedienungs-App fürs iPhone](@iphone) und [Fernbedienungs-App für Windows](@windows).'),
      ('Datenschutz', 'Kein Konto und kein Tracking in der App. Die Kommunikation mit dem Fernseher findet nur im lokalen Netzwerk statt, die Verbindungsdaten bleiben auf deinem Gerät verschlüsselt. Details in den [Datenschutzbestimmungen](@privacidad).'),
    ],
    marca=None,
    faq=[
      ('Gibt es eine Fernbedienungs-App ohne Abo?', 'Ja. Mando TV hat überhaupt kein Abo: Die Fernbedienung ist kostenlos und werbefrei, Pro ist ein optionaler Einmalkauf.'),
      ('Ist Mando TV wirklich kostenlos?', 'Ja. Pfeiltasten, OK, Zurück, Home, Lautstärke, Kanäle, Ziffern, Tastatur und Ein-/Ausschalten sind kostenlos, ohne Werbung und ohne Zeitlimit.'),
      ('Funktioniert es ohne WLAN?', 'Meistens nein. Mando TV steuert Smart-TVs über dein Heim-WLAN. Ausnahmen: Infrarot auf Android-Handys mit Infrarotsender, das auch mit Fernsehern ohne Smart-TV-Funktion oder ohne WLAN-Verbindung klappt, und Bluetooth, in der Beta ab Android 9, für Google TV, Android TV und Fire TV.'),
    ]),
  dict(clave='roku-app-alt', corto='Alternative zur Roku App', fecha='2026-11-23',
    titulo='Alternative zur Roku App: einfache Roku-Fernbedienung',
    desc='Eine Alternative zur Roku App als Fernbedienung: Mando TV steuert Roku-TVs und -Player über WLAN, ohne Konto und Werbung, dazu Samsung, LG und Google TV.',
    h1='Alternative zur Roku App: eine für alle Fernseher',
    intro='Die offizielle Roku App kann viel: Channel Store, Casting, Private Listening und eine Fernbedienung. Wenn du nur eine schnelle Fernbedienung suchst oder zu Hause auch einen Samsung-, LG- oder Google-TV-Fernseher hast, ist Mando TV eine einfache Alternative, die Roku über dein WLAN ohne Konto steuert.',
    pasos=[
      'Verbinde dein Handy und den Roku mit demselben WLAN.',
      'Lade Mando TV herunter und öffne es. Dein Roku-Fernseher oder Roku-Player erscheint in der Liste. Tippe darauf. Der Roku fragt nicht nach einem Code.',
      'Nutze die Pfeiltasten, OK, Zurück, Home, Lautstärke und die Tastatur. Gib Suchbegriffe in Roku-Kanälen mit der Handy-Tastatur ein.',
      'Wenn die Tasten nichts tun, gehe am Roku zu Einstellungen > System > Erweiterte Systemeinstellungen > Steuerung durch mobile Apps und stelle Netzwerkzugriff auf Standard oder Aktiviert (bei neuerer Roku-Software setze Steuerung durch mobile Apps auf Aktiviert).',
      'Optional: Aktiviere am Roku-Fernseher den „TV-Schnellstart“ unter Einstellungen > System > Energie, damit Mando TV den Fernseher einschalten kann.',
    ],
    extra=[
      ('Wo Mando TV besser passt', 'Eine App für mehrere Fernseher: Roku, Samsung, LG und Google TV oder Android TV. Ohne Konto, ohne Werbung. Sie funktioniert auch auf einem Windows-PC, was am Schreibtisch praktisch ist. Pfeiltasten und Lautstärke reagieren schnell, und mit der Tastatur tippst du Suchbegriffe ohne Mühe.'),
      ('Wo die offizielle Roku App besser ist', 'Behalte die Roku App für das, was sie über die Fernbedienung hinaus bietet, wie das Durchsuchen und Hinzufügen von Kanälen aus dem Roku Channel Store sowie das eigene Casting und Private Listening (Ton über Kopfhörer am Handy). Nutze beide, wenn du möchtest. Sie können auf demselben Handy laufen.'),
      ('Roku-TV-Geräte und Roku-Player', 'Beide funktionieren. Das umfasst Roku-TV-Modelle von TCL, Hisense, Philips und anderen sowie Roku Express, Streaming Stick und Ultra. Details findest du auf der [Seite zur Roku Fernbedienungs-App](@roku).'),
      ('Wenn die Roku App nicht mehr funktioniert', 'Wenn die Tasten nicht mehr reagieren, blockiert der Roku meist die Steuerung durch Apps. Die Anleitung [Roku App funktioniert nicht](@roku-403) zeigt die Einstellung, die das Problem behebt.'),
      ('Kostenlos und Pro', 'Pfeiltasten, OK, Zurück, Home, Lautstärke, Kanäle, Zifferntasten, Tastatur, Öffnen von Apps, Wechseln der Eingänge und Ein- oder Ausschalten sind kostenlos, ohne Werbung und ohne Abo. Mando TV Pro ist ein optionaler Einmalkauf für Extras.'),
    ],
    marca='roku',
    faq=[
      ('Brauche ich ein Roku-Konto, um Mando TV zu nutzen?', 'Nein. Mando TV kommuniziert mit dem Roku über dein Heimnetzwerk und fragt nicht nach einem Konto.'),
      ('Ersetzt Mando TV die Roku Mobile App vollständig?', 'Als Fernbedienung ja. Für den Channel Store, Casting und Private Listening behalte die offizielle Roku App.'),
      ('Funktioniert es mit meinem Roku Express oder Streaming Stick?', 'Ja. Alle Roku-Player und Roku-TV-Geräte werden auf die gleiche Weise gesteuert.'),
    ]),
  dict(clave='lg-thinq', corto='Alternative zur LG ThinQ App', fecha='2026-11-23',
    titulo='Alternative zur LG ThinQ App: LG-Fernbedienung ohne Konto',
    desc='Du suchst eine Alternative zur LG ThinQ App nur als Fernbedienung? Mando TV steuert LG-Fernseher mit webOS über WLAN, ohne LG-Konto und ohne Werbung.',
    h1='Alternative zur LG ThinQ App für deinen LG-Fernseher',
    intro='LG ThinQ ist die offizielle App von LG, gedacht für das ganze Smart Home: Hausgeräte, den Fernseher und mehr. Wenn du nur eine einfache Fernbedienung für deinen LG-Fernseher willst, erledigt Mando TV genau das über dein WLAN zu Hause, ohne dass du ein LG-Konto erstellen musst und ohne Werbung.',
    pasos=[
      'Verbinde dein Handy oder deinen PC (iPhone, Android oder Windows) und deinen LG-Fernseher mit demselben WLAN.',
      'Lade Mando TV herunter und öffne es. Dein LG-Fernseher erscheint von selbst in der Liste. Tippe darauf.',
      'Auf dem Fernseher erscheint eine Abfrage. Bestätige sie einmal mit der Fernbedienung des Fernsehers, dem Joystick unter dem Bildschirm oder der Magic Remote.',
      'Tasten, Lautstärke und Tastatur funktionieren sofort. Du brauchst kein LG-Konto und musst den Fernseher nicht registrieren.',
      'Optional: Aktiviere „Fernseher per Mobilgerät einschalten“ in den Fernseheinstellungen, damit du den Fernseher auch vom Handy aus einschalten kannst.',
    ],
    extra=[
      ('Mando TV oder LG ThinQ: was wofür', 'Nutze ThinQ, wenn du LG-Hausgeräte wie eine Waschmaschine, einen Kühlschrank oder eine Klimaanlage verwalten willst oder LG-Kontofunktionen brauchst. Nutze Mando TV, wenn du eine schnelle, einfache Fernbedienung für den Fernseher willst, die auch für Samsung, Roku und Google TV in derselben App funktioniert. Viele behalten beide: ThinQ für die Hausgeräte, Mando TV für den Fernseher.'),
      ('Was Mando TV auf einem LG-Fernseher macht', 'Es funktioniert mit LG-Smart-TVs mit webOS, also mit den meisten Modellen seit 2014, einschließlich LED, NanoCell, QNED und OLED. Es bietet dir die Pfeiltasten, OK, Zurück, Home, Lautstärke, Sender, Stumm, Wiedergabesteuerung und eine Tastatur zum Tippen in YouTube, Netflix oder dem Browser. Die App-Liste und die Eingangsliste sind ebenfalls kostenlos. Mit Pro bekommst du zusätzlich einen Zeiger wie bei der Magic Remote.'),
      ('Was Mando TV nicht macht', 'Es steuert keine LG-Hausgeräte, es nutzt dein LG-Konto nicht und es ersetzt nicht die LG-Kontodienste auf dem Fernseher. Es ist eine Fernbedienung, kein Smart-Home-Hub.'),
      ('Datenschutz und Werbung', 'Mando TV hat keine Werbung und kein Konto. Es spricht nur innerhalb deines Heimnetzes mit dem Fernseher und speichert den Verbindungsschlüssel verschlüsselt auf deinem Gerät. Alle Funktionen findest du auf der Seite [LG Fernbedienungs-App](@lg).'),
      ('Kostenlos und Pro', 'Pfeiltasten, OK, Zurück, Home, Lautstärke, Sender, Zifferntasten, Tastatur, Apps öffnen, Eingänge wechseln und Ein-/Ausschalten sind kostenlos, ohne Werbung und ohne Abo. Mando TV Pro ist ein optionaler Einmalkauf für Extras.'),
    ],
    marca='lg',
    faq=[
      ('Kann ich meinen LG-Fernseher ohne die LG ThinQ App steuern?', 'Ja. Mando TV verbindet sich direkt über dein WLAN mit LG-Fernsehern mit webOS. Du akzeptierst einmal eine Abfrage auf dem Fernseher und das war’s, ganz ohne LG-Konto.'),
      ('Funktioniert Mando TV mit dem Zeiger der LG Magic Remote?', 'Mando TV Pro hat einen Zeiger, den du mit dem Finger auf dem Handy-Bildschirm bewegst, ähnlich wie die Magic Remote den Pfeil bewegt.'),
      ('Ist Mando TV von LG?', 'Nein. Mando TV ist eine unabhängige App und steht in keiner Verbindung zu LG. LG und ThinQ gehören ihren Eigentümern und werden nur genannt, um die Kompatibilität zu beschreiben.'),
    ]),
  dict(clave='smartthings', corto='SmartThings-Alternative', fecha='2026-11-23',
    titulo='SmartThings geht nicht? Einfache Alternative für Samsung',
    desc='SmartThings zu langsam oder fehlerhaft? Mando TV steuert Samsung-Fernseher mit Tizen direkt über WLAN. Ohne Samsung-Konto, ohne Werbung. Schritt für Schritt.',
    h1='SmartThings-Alternative für Samsung-Fernseher',
    intro='SmartThings ist die Samsung-App für das ganze Smart Home, und ihre Fernbedienung läuft über dein Samsung-Konto. Wenn sie nicht mehr geht oder du eine schnelle Lösung suchst, steuert Mando TV Samsung-Fernseher mit Tizen, Baujahr 2016 und neuer, direkt über dein WLAN ohne Konto.',
    pasos=[
      'Verbinde dein Handy und den Samsung-Fernseher mit demselben WLAN.',
      'Lade Mando TV herunter und öffne die App. Dein Samsung-Fernseher erscheint von selbst in der Liste. Tippe darauf.',
      'Der Fernseher fragt, ob du die Verbindung erlauben willst. Wähle „Zulassen“ mit der Fernbedienung oder mit der Taste am Fernseher (nur beim ersten Mal).',
      'Nutze sofort die Pfeiltasten, OK, Zurück, Home, Lautstärke, Sender und die Tastatur.',
      'Optional: Aktiviere „Mit Mobilgerät einschalten“ unter Einstellungen > Allgemein > Netzwerk > Experteneinstellungen, damit Mando TV den Fernseher auch einschalten kann.',
    ],
    extra=[
      ('Warum eine Handy-Fernbedienung nicht mehr funktioniert', 'Die Ursachen sind meist einfach: Handy und Fernseher sind in unterschiedlichen WLANs, ein VPN ist aktiv oder der Fernseher ist im tiefen Standby. Bei SmartThings kann zusätzlich das Samsung-Konto Probleme machen, zum Beispiel wenn du abgemeldet wurdest. Mando TV spricht direkt mit dem Fernseher im Heimnetzwerk, es gibt kein Konto zum Anmelden. Weitere Tipps findest du unter [Dein Handy findet den Fernseher nicht](@not-found).'),
      ('Mando TV oder SmartThings: was wofür', 'Behalte SmartThings, wenn du es für Samsung-Hausgeräte, Lampen oder andere Smart-Home-Geräte nutzt oder für Funktionen deines Samsung-Kontos. Nutze Mando TV, wenn du einfach eine schnelle Fernbedienung für den Fernseher willst oder zu Hause auch ein Gerät von LG, Roku, Google TV oder Fire TV hast: Eine App steuert alle. Beide Apps können auf demselben Handy installiert sein.'),
      ('Wenn du die Erlaubnis versehentlich abgelehnt hast', 'Gehe am Fernseher zu Einstellungen > Allgemein > Externer Geräte-Manager > Geräteverbindungs-Manager und stelle Mando TV auf erlaubt.'),
      ('Keine Fernbedienung?', 'Du kannst die Abfrage mit der Taste am Fernseher selbst bestätigen. Die Anleitung [Samsung Fernseher ohne Original-Fernbedienung](@samsung-lost) zeigt dir, wie es geht.'),
      ('Kostenlos und Pro', 'Die Fernbedienung kannst du kostenlos laden und nutzen, ohne Werbung und ohne Abo. Mando TV Pro ist ein optionaler Einmalkauf für Extras.'),
    ],
    marca='samsung',
    faq=[
      ('Kann ich meinen Samsung-Fernseher ohne SmartThings steuern?', 'Ja. Mando TV verbindet sich direkt über dein WLAN mit Samsung-Fernsehern mit Tizen. Du erlaubst die Verbindung einmal am Fernseher, ohne Samsung-Konto.'),
      ('Steuert Mando TV auch Samsung-Hausgeräte?', 'Nein. Es ist nur eine Fernbedienung für den Fernseher. Für Hausgeräte und andere Smart-Home-Geräte behältst du SmartThings.'),
      ('Ist Mando TV von Samsung?', 'Nein. Mando TV ist eine unabhängige App und steht in keiner Verbindung zu Samsung. Samsung und SmartThings gehören ihren Eigentümern und werden nur genannt, um die Kompatibilität zu beschreiben.'),
    ]),
  dict(clave='googletv-alt', corto='Alternative zur Google-TV-Fernbedienung', fecha='2026-11-23',
    titulo='Google-TV-Fernbedienung geht nicht? Die Alternative',
    desc='Die Handy-Fernbedienung für Google TV findet den Fernseher nicht? Mando TV steuert Google TV und Android TV über WLAN, ohne Google-Konto und Werbung.',
    h1='Alternative zur Google-TV-Fernbedienung auf dem Handy',
    intro='Die Handy-Fernbedienung für Google TV und Android TV steckt in der App von Google selbst und ist mit deinem Google-Konto verknüpft. Findet sie den Fernseher nicht, kommst du nicht weiter. Mando TV ist eine separate Fernbedienungs-App, die sich mit dem Code aus 6 Zeichen auf dem Bildschirm koppelt und ohne Google-Konto funktioniert, auf einem iPhone, einem Android-Handy oder einem Windows-PC.',
    pasos=[
      'Schalte den Fernseher ein und verbinde dein Handy mit demselben WLAN.',
      'Lade Mando TV herunter und öffne die App. Tippe in der Liste auf deinen Fernseher mit Google TV oder Android TV.',
      'Der Fernseher zeigt einen Code mit 6 Zeichen an. Gib ihn in Mando TV ein und tippe auf Koppeln.',
      'Nutze die Pfeiltasten, OK, Zurück, Home, die Lautstärke und die Tastatur. Du musst dich nirgendwo anmelden.',
      'Optional: Suche in den Einstellungen des Fernsehers nach Wake on LAN oder „Einschalten über Netzwerk“, damit die App den Fernseher auch einschalten kann.',
    ],
    extra=[
      ('Warum die Handy-Fernbedienung den Fernseher nicht mehr findet', 'Meistens liegt es am Netzwerk: Handy und Fernseher sind in verschiedenen WLANs, ein VPN ist aktiv oder ein Gastnetzwerk trennt die Geräte. Behebe das zuerst, da es alle Fernbedienungs-Apps betrifft. Mehr dazu in [Dein Handy findet den Fernseher nicht](@not-found).'),
      ('Mit welchen Fernsehern es funktioniert', 'Fernseher mit Google TV und Android TV von Sony, TCL, Hisense, Philips, Sharp, Xiaomi, Toshiba und mehr, sowie Chromecast mit Google TV, Google TV Streamer und Nvidia Shield. Alle werden gleich gekoppelt, einmalig mit dem Code auf dem Bildschirm.'),
      ('Wo die App von Google besser ist', 'Die App von Google hilft dir auch dabei, Inhalte zum Ansehen zu finden und merkt sich deine Watchlist. Behalte sie dafür. Mando TV ist nur die Fernbedienung und steuert zusätzlich Samsung, LG, Roku und Fire-TV-Geräte aus derselben App sowie von einem Windows-PC aus.'),
      ('Wenn die alte Android-TV-Fernbedienungs-App fehlt', 'Google hat die Handy-Fernbedienung aus der alten Android TV Remote Control App in die Google TV App verschoben. Wenn du eine eigenständige Fernbedienung suchst, ist Mando TV eine Option.'),
      ('Kostenlos und Pro', 'Die Fernbedienung kannst du kostenlos laden und nutzen, ohne Werbung und ohne Abo. Mando TV Pro ist ein optionaler Einmalkauf für Extras.'),
    ],
    marca='android',
    faq=[
      ('Brauche ich ein Google-Konto, um Mando TV mit Google TV zu nutzen?', 'Nein. Der Code auf dem Fernseher reicht zur Kopplung aus.'),
      ('Funktioniert es mit Chromecast mit Google TV?', 'Ja. Die Kopplung läuft genauso, mit dem Code aus 6 Zeichen auf dem Bildschirm.'),
      ('Kann ich es von einem iPhone aus nutzen?', 'Ja. Mando TV ist im App Store für iPhone und iPad, im Microsoft Store für Windows und im kostenlosen frühen Zugang bei Google Play für Android verfügbar.'),
    ]),
  dict(clave='windows', corto='Fernbedienung für Windows-PC', fecha='2026-11-23',
    titulo='Fernbedienungs-App für Windows: Fernseher am PC steuern',
    desc='Steuere Samsung, LG, Roku, Google TV oder Fire TV von einem Windows-PC mit Mando TV: Tastenkürzel, Mini-Fernbedienung und WLAN. Im Microsoft Store.',
    h1='Fernbedienungs-App für den Windows-PC',
    intro='Mando TV hat eine Windows-App, die deinen PC oder Laptop über das Heimnetz in eine Fernbedienung für den Fernseher verwandelt. Tippe auf dem Fernseher mit deiner echten Tastatur, lass beim Arbeiten ein kleines Fernbedienungsfenster im Vordergrund und steuere Samsung, LG, Roku, Google TV oder Fire TV mit derselben App.',
    pasos=[
      'Installiere Mando TV kostenlos aus dem Microsoft Store auf einem PC mit Windows 10 oder 11.',
      'Stelle sicher, dass der PC und der Fernseher im selben Netzwerk sind, per WLAN oder Kabel am selben Router.',
      'Öffne Mando TV. Der Fernseher erscheint in der Liste. Klicke darauf.',
      'Bestätige die Abfrage am Fernseher, falls er fragt (LG, Samsung), oder gib den angezeigten Code ein (Google TV, Fire TV).',
      'Klicke auf die Tasten oder tippe eine Suche mit deiner Tastatur ein. Fertig.',
    ],
    extra=[
      ('Tastenkürzel (Pro)', 'Mit Pro wird deine PC-Tastatur zur Fernbedienung: Pfeiltasten zum Bewegen, Eingabetaste für OK, Rücktaste oder Esc zum Zurückgehen, Plus und Minus für die Lautstärke, M zum Stummschalten und Leertaste zum Pausieren.'),
      ('Mini-Fernbedienung (Pro)', 'Ein kleines Fernbedienungsfenster, das über allen anderen Fenstern bleibt. So änderst du die Lautstärke oder pausierst, ohne deine Arbeit zu unterbrechen.'),
      ('Tippen auf dem Fernseher vom PC aus', 'Die Bildschirmtastatur eines Fernsehers ist langsam. In Mando TV tippst du mit deiner echten Tastatur und der Text landet im Suchfeld des Fernsehers. Dieser Teil ist kostenlos.'),
      ('Mehr Details', 'Die Anleitung Schritt für Schritt findest du unter [Fernseher mit dem PC steuern](@pc). Für das Handy lies [Handy als Fernbedienung per WLAN](@wifi).'),
      ('Kostenlos und Pro', 'Die Pfeiltasten, OK, Zurück, Home, Lautstärke, Sender, Zifferntasten, Tastatur, Apps öffnen, Eingänge wechseln und Ein- oder Ausschalten sind kostenlos, ohne Werbung und ohne Abo. Mando TV Pro ist ein optionaler Einmalkauf für Extras. Unter Windows kaufst du Pro über den Microsoft Store.'),
      ('Sprachbefehle vom PC aus (Pro)', 'Mit Pro kannst du mit dem Fernseher über das PC-Mikrofon sprechen. Die Sprache wird direkt auf dem PC erkannt: Dafür brauchst du kein Internet und musst nichts in Windows einstellen. Was du sagst, verlässt nie den PC und wird nicht gespeichert. Nur bei sehr alten Prozessoren fällt die App auf die Windows-Spracheingabe zurück. Dafür muss die Online-Spracherkennung in den Datenschutz-Einstellungen eingeschaltet und deine Sprache in Windows hinzugefügt sein.'),
    ],
    marca=None,
    faq=[
      ('Braucht die Fernbedienungs-App für Windows Bluetooth oder ein Kabel?', 'Nein. Sie nutzt dein Heimnetzwerk. PC und Fernseher müssen nur am selben Router angeschlossen sein.'),
      ('Welche Fernseher kann ich von Windows aus steuern?', 'Samsung-Fernseher mit Tizen, LG-Fernseher mit webOS, Roku TV und Player, Google TV und Android TV sowie Fire TV.'),
      ('Kann ich das Fernsehbild auf dem PC sehen oder über die PC-Lautsprecher hören?', 'Nein. Mando TV ist nur eine Fernbedienung. Es spiegelt oder streamt das Fernsehbild nicht auf den Computer.'),
      ('Warum funktioniert die Sprache auf meinem Windows-PC nicht?', 'Die Sprachsteuerung ist eine Pro-Funktion. Prüfe also, ob Pro aktiv ist und das PC-Mikrofon funktioniert. Auf den meisten PCs wird die Sprache direkt auf dem PC erkannt, ohne Internet. Nur bei sehr alten Prozessoren nutzt die App die Windows-Spracheingabe: Dann schalte die Online-Spracherkennung in den Datenschutz-Einstellungen von Windows ein und füge deine Sprache in den Spracheinstellungen hinzu.'),
    ]),
  dict(clave='iphone', corto='Fernbedienungs-App fürs iPhone', fecha='2026-11-23',
    titulo='Fernbedienungs-App fürs iPhone: Samsung, LG, Roku, Google TV',
    desc='Nutze dein iPhone als Fernbedienung für Samsung, LG, Roku, Google TV und Fire TV über WLAN. Kostenlos im App Store, ohne Konto und ohne Werbung.',
    h1='Fernbedienungs-App fürs iPhone: eine für alle Fernseher',
    intro='Mando TV macht dein iPhone oder iPad zur Fernbedienung für Samsung, LG, Roku, Google TV oder Android TV sowie Fire TV, über dein WLAN zu Hause. Die App ist kostenlos im App Store, ohne Konto und ohne Werbung. Sie läuft auch auf Android und Windows.',
    pasos=[
      'Lade Mando TV kostenlos aus dem App Store herunter.',
      'Verbinde dein iPhone und den Fernseher mit demselben WLAN.',
      'Öffne Mando TV und tippe auf Erlauben, wenn iOS nach Zugriff auf das lokale Netzwerk fragt. Die App braucht es, um den Fernseher zu finden.',
      'Tippe in der Liste auf deinen Fernseher. Bestätige die Abfrage auf dem Fernseher, falls er fragt (LG und Samsung), oder gib den Code ein, den der Fernseher anzeigt (Google TV oder Fire TV).',
      'Nutze die Tasten, die Lautstärke und die Tastatur. Du bist verbunden.',
    ],
    extra=[
      ('Funktioniert mit diesen Fernsehern', 'LG webOS, Samsung Tizen (Baujahr 2016 und neuer), Roku TV und Roku-Player, Google TV und Android TV sowie Fire TV. Die Seiten der Marken sind [Samsung](@samsung), [LG](@lg), [Roku](@roku) und [Android TV](@android).'),
      ('Warum es nach lokalem Netzwerk fragt', 'Das iPhone blockiert den Zugriff von Apps auf Geräte in deinem Heimnetzwerk, es sei denn, du erlaubst es. Wenn der Fernseher nicht in der Liste erscheint, öffne Einstellungen > Mando TV und aktiviere „Lokales Netzwerk“. Die App kommuniziert nur mit deinem Fernseher innerhalb deines Heimnetzwerks.'),
      ('Warum Mando TV und nicht die App des Herstellers', 'Jede Fernsehmarke hat ihre eigene App und will eine eigene Einrichtung oder ein eigenes Konto. Mando TV ist eine App für alle, ohne Konto.'),
      ('Kostenlos und Pro auf dem iPhone', 'Pfeiltasten, OK, Zurück, Home, Lautstärke, Sender, Zifferntasten, Tastatur, Apps öffnen, Eingänge wechseln und Ein- oder Ausschalten sind kostenlos, ohne Werbung und ohne Abo. Mando TV Pro ist ein optionaler Einmalkauf für Extras, direkt in der App.'),
    ],
    marca=None,
    faq=[
      ('Ist Mando TV auf dem iPhone kostenlos?', 'Der Download ist kostenlos, ohne Werbung. Die Basis-Fernbedienung ist kostenlos, ebenso das Öffnen von Apps und das Wechseln der Eingänge. Extras sind Teil von Mando TV Pro, einem optionalen Einmalkauf.'),
      ('Funktioniert es auf dem iPad?', 'Ja. Die gleiche App läuft auf iPhone und iPad.'),
      ('Braucht eine Fernbedienungs-App fürs iPhone Bluetooth oder einen Infrarotsender?', 'Nicht auf dem iPhone. iPhones haben keinen Infrarotsender, daher ist die Infrarotsteuerung dort nicht verfügbar, und die Bluetooth-Option gibt es nur für Android 9 oder neuer, nicht für das iPhone. Auf dem iPhone steuert Mando TV Smart-TVs sowie Apple TV (Beta) über dein WLAN zu Hause.'),
    ]),
  dict(clave='firetv', corto='Fire-TV-Fernbedienung', fecha='2026-11-23',
    titulo='Fire-TV-Fernbedienungs-App für Handy und PC',
    desc='Fire-TV-Fernbedienung auf dem Handy: Steuere Fire TV Stick, Fire TV Cube oder einen Fernseher mit Fire TV per WLAN, mit 4-stelligem PIN. Ohne Amazon-App.',
    h1='Fire-TV-Fernbedienung für dein Handy oder deinen PC',
    intro='Wenn die Fire-TV-Fernbedienung weg ist oder die Batterien leer sind, steuert Mando TV einen Fire TV Stick, einen Fire TV Cube oder einen Fernseher mit integriertem Fire TV über das WLAN. Die Kopplung erfolgt mit einem 4-stelligen PIN. Fire TV ist neu in Mando TV, aktualisiere also zuerst die App.',
    pasos=[
      'Aktualisiere Mando TV auf die neueste Version aus dem App Store, Microsoft Store oder Google Play.',
      'Schalte den Fire TV ein und verbinde dein Handy mit demselben WLAN.',
      'Öffne Mando TV. Dein Fire TV erscheint in der Liste. Tippe darauf.',
      'Auf dem Bildschirm des Fernsehers erscheint ein 4-stelliger PIN. Gib ihn in Mando TV ein. Das machst du nur einmal.',
      'Nutze die Pfeiltasten, OK, Zurück, Home, Wiedergabe-Tasten und die Tastatur für Suchanfragen.',
    ],
    extra=[
      ('Unterstützte Fire-TV-Geräte', 'Fire TV Stick, Fire TV Stick 4K, Fire TV Cube und Fernseher mit integriertem Fire TV. Die Unterstützung ist neu, und wir konnten bisher nur wenige echte Geräte testen. Wenn etwas nicht wie erwartet funktioniert, schreibe uns dein Modell über die Hilfe-Seite.'),
      ('Fire TV einschalten', 'Mando TV schaltet einen Fire TV nicht über das Netzwerk ein. Schalte den Fernseher mit der Ein-Taste am Gerät ein: Ein eingesteckter Fire TV Stick oder Cube wacht meist durch HDMI-CEC auf, und bei einem Fernseher mit integriertem Fire TV ist der Fernseher der Fire TV. Danach steuerst du ihn vom Handy aus.'),
      ('Wenn dein Fire TV nicht erscheint', 'Stelle sicher, dass beide Geräte im selben WLAN sind und der Fire TV wach ist. Erlaube auf einem iPhone „Lokales Netzwerk“ für Mando TV in den Einstellungen. Siehe [dein Handy findet den Fernseher nicht](@not-found).'),
      ('Gar keine Fernbedienung?', 'Der Fire TV muss den PIN auf dem Bildschirm zeigen, also müssen Fernseher und Fire TV an sein und ein Bild zeigen. Wenn der Fernseher auf einem falschen Eingang steht, wechsle ihn mit den Tasten am Fernseher. Siehe [Eingang wechseln ohne Fernbedienung](@hdmi).'),
      ('Kostenlos und Pro', 'Pfeiltasten, OK, Zurück, Home, Lautstärke, Sender, Ziffern, Tastatur, Apps öffnen, Eingänge wechseln und Ein-/Ausschalten sind kostenlos, ohne Werbung und ohne Abo. Mando TV Pro ist ein optionaler Einmalkauf für Extras.'),
    ],
    marca=None,
    faq=[
      ('Brauche ich die Amazon Fire TV App?', 'Nein. Mando TV verbindet sich über dein WLAN mit dem Fire TV per PIN. Du brauchst kein Amazon-Konto auf dem Handy.'),
      ('Funktioniert es mit Fernsehern mit Fire TV und mit Fire TV Sticks?', 'Ja, genau dafür wurde es entwickelt. Die Unterstützung ist neu, halte die App aktuell und informiere uns über Modelle, die nicht wie erwartet funktionieren.'),
      ('Warum brauche ich einen PIN?', 'Der Fire TV zeigt einen 4-stelligen PIN an, um zu beweisen, dass du vor dem Fernseher sitzt. Niemand kann sich koppeln, ohne den Bildschirm zu sehen.'),
    ]),
  dict(clave='firetv-lost', corto='Fire-TV-Fernbedienung verloren', fecha='2026-11-23',
    titulo='Fire-TV-Fernbedienung verloren? So hilft dein Handy',
    desc='Fernbedienung vom Fire TV Stick verloren? Steuere ihn per WLAN mit dem Handy, gekoppelt mit einem 4-stelligen PIN. Tipps für neues WLAN und HDMI-CEC.',
    h1='Fire-TV-Fernbedienung verloren: So nutzt du dein Handy',
    intro='Wenn die Fernbedienung für deinen Fire TV Stick, Fire TV Cube oder Smart-TV mit Fire TV verloren ist oder nicht mehr funktioniert, übernimmt dein Handy die Steuerung, solange der Fire TV noch mit deinem WLAN verbunden ist. Die Kopplung erfolgt über einen 4-stelligen PIN auf dem Bildschirm, sodass du die alte Fernbedienung dafür nie brauchst.',
    pasos=[
      'Schalte den Fernseher mit der Taste am Gerät ein. Ein eingesteckter Fire TV Stick oder Cube wacht meist mit auf; bei aktiviertem HDMI-CEC wechselt der Fernseher oft automatisch auf seinen Eingang.',
      'Zeigt der Fernseher einen anderen Eingang, wechsle ihn mit der Eingangs- oder Quellentaste am Fernseher. Siehe [Eingang wechseln ohne Fernbedienung](@hdmi).',
      'Verbinde dein Handy mit demselben WLAN wie den Fire TV.',
      'Lade Mando TV herunter und öffne die App. Dein Fire TV erscheint in der Liste. Tippe darauf.',
      'Der Fernseher zeigt einen 4-stelligen PIN. Gib ihn in Mando TV ein. Das machst du nur einmal.',
      'Nutze die Pfeiltasten, OK, Zurück, Home, Lautstärke, Wiedergabe-Tasten und die Tastatur auf deinem Handy.',
    ],
    extra=[
      ('Teste zuerst die Fernseher-Fernbedienung (HDMI-CEC)', 'Viele Fernseher-Fernbedienungen können einen Fire TV Stick über HDMI-CEC steuern. Wenn die Fire-TV-Oberfläche zu sehen ist, drücke die Pfeile und OK auf der Fernbedienung des Fernsehers. Wenn nichts passiert, aktiviere CEC in den Einstellungen des Fernsehers (Anynet+ bei Samsung, SIMPLINK bei LG, BRAVIA Sync bei Sony) und am Fire TV die HDMI-CEC-Gerätesteuerung in den Display-Einstellungen („Display & Sounds“).'),
      ('Wenn du das WLAN gewechselt hast', 'Ohne Fernbedienung kannst du das neue WLAN-Passwort am Fire TV nicht eingeben, aber es gibt einen Ausweg: Erstelle auf einem zweiten Handy einen Hotspot mit exakt demselben Namen und Passwort wie dein altes WLAN. Der Fire TV verbindet sich automatisch damit. Verbinde das Handy mit Mando TV mit diesem Hotspot, kopple ihn mit dem PIN, gehe dann am Fire TV zu Einstellungen > Netzwerk und wähle dein neues WLAN aus. Verbinde zum Schluss auch dein Handy mit dem neuen WLAN.'),
      ('Eine Ersatz-Fernbedienung koppeln', 'Die meisten neuen Fire TV Fernbedienungen koppeln, indem du die Home-Taste etwa 10 Sekunden lang gedrückt hältst, in der Nähe des Fire TV. Falls es nicht klappt, öffne Einstellungen > Controller und Bluetooth-Geräte > Amazon Fire TV-Fernbedienungen > Neue Fernbedienung hinzufügen. Dieses Menü erreichst du auch über dein Handy mit Mando TV.'),
      ('Fire TV im Fernseher integriert', 'Bei Fernsehern mit integriertem Fire TV funktionieren die gleichen Schritte, da der Fernseher selbst der Fire TV ist.'),
      ('Bevor du startest', 'Die Fire TV-Unterstützung ist neu in Mando TV. Aktualisiere die App zuerst. Wenn dein Modell nicht wie erwartet reagiert, schreib uns über die [Hilfeseite](@soporte) und nenne das Modell.'),
      ('Kostenlos und Pro', 'Die Fernbedienung kannst du kostenlos laden und nutzen, ohne Werbung und ohne Abo. Mando TV Pro ist ein optionaler Einmalkauf für Extras.'),
    ],
    marca=('firetv', 'Fire-TV-Fernbedienung'),
    faq=[
      ('Kann ich einen Fire TV Stick mit dem Handy steuern, ohne die Fernbedienung?', 'Ja, solange der Fire TV an ist und mit deinem WLAN verbunden. Mando TV koppelt über den 4-stelligen PIN auf dem Fernseher, du brauchst die alte Fernbedienung also nicht.'),
      ('Funktioniert es, wenn der Fire TV in einem neuen WLAN ist?', 'Nicht direkt, da Handy und Fire TV im selben Netzwerk sein müssen. Bringe den Fire TV zuerst mit dem Hotspot-Trick auf dieser Seite wieder online.'),
      ('Brauche ich die Amazon Fire TV App oder ein Amazon-Konto?', 'Nein. Mando TV verbindet sich über dein Heimnetzwerk mit dem PIN und benötigt kein eigenes Konto.'),
    ]),
  dict(clave='turn-on', corto='Fernseher ohne Fernbedienung einschalten', fecha='2026-11-23',
    titulo='Fernseher ohne Fernbedienung einschalten (alle Marken)',
    desc='Fernseher ohne Fernbedienung einschalten: Wo die Taste bei Samsung, LG, TCL, Hisense und Sony sitzt. Plus HDMI-CEC und Handy-Tricks.',
    h1='So schaltest du einen Fernseher ohne Fernbedienung ein',
    intro='Fast jeder Fernseher hat noch eine physische Ein-/Aus-Taste. Sie ist nur gut versteckt. Hier siehst du, wo sie bei jeder Marke sitzt, plus zwei Wege, das Suchen beim nächsten Mal zu sparen: HDMI-CEC von einer Konsole oder einem Streaming-Gerät aus, und das Einschalten des Fernsehers über dein Handy per WLAN.',
    pasos=[
      'Schau unter die Mitte des Bildschirms, direkt hinter dem Markenlogo. Viele Fernseher haben dort eine kleine einzelne Taste oder einen Joystick, nach unten zeigend.',
      'Wenn sie dort nicht ist, tast dich an der Rückseite des Fernsehers in der Nähe der unteren Ecken entlang, dann an den linken und rechten Kanten.',
      'Drücke die Taste einmal. Bei vielen Fernsehern mit nur einer Taste öffnet ein kurzer Druck bei laufendem Gerät ein kleines Menü für Eingänge und Lautstärke, und ein langer Druck schaltet ihn aus.',
      'Immer noch nichts? Prüfe das Netzkabel an beiden Enden und versuche eine andere Steckdose. Wenn die Standby-Lampe nicht leuchtet, bekommt der Fernseher keinen Strom.',
      'Sobald der Fernseher an ist, richte ihn so ein, dass du die Taste nicht mehr brauchst: Aktiviere HDMI-CEC und das Einschalten über das Netzwerk, beides weiter unten erklärt.',
    ],
    extra=[
      ('Wo die Ein-/Aus-Taste sitzt, nach Marke', 'Samsung: eine Steuerungs-Taste oder ein Joystick unter der Mitte des Bildschirms oder auf der Rückseite an einer unteren Ecke. LG: eine Joystick-Taste unter dem LG-Logo bei den meisten Modellen. TCL und Hisense: meist eine kleine Taste unter der Mitte des Bildschirms oder auf der Rückseite in der Nähe einer unteren Ecke. Sony: auf der Rückseite oder an einer Seitenkante, unten nah am Rand. Die Positionen ändern sich je nach Modell. Wenn du sie nicht findest, suche die Bedienungsanleitung mit der Modellnummer auf dem Aufkleber auf der Rückseite.'),
      ('Den Fernseher über eine Konsole oder ein Streaming-Gerät einschalten (HDMI-CEC)', 'Mit aktiviertem HDMI-CEC schaltet das Einschalten einer PlayStation, einer Xbox, eines Roku-Players, eines Fire-TV-Sticks oder eines Chromecast auch den Fernseher ein und wechselt auf den richtigen Eingang. Jede Marke nennt die Einstellung anders: Anynet+ bei Samsung, SIMPLINK bei LG, BRAVIA Sync bei Sony und CEC bei den meisten anderen. Mehr in [Fernseher einschalten und auf HDMI der Konsole wechseln](@console).'),
      ('Den Fernseher über dein Handy einschalten', 'Smart-TVs können per WLAN aufgeweckt werden, wenn du das einmal erlaubst, und dann schaltet Mando TV sie von deinem Handy aus ein. Bei Samsung aktiviere „Mit Mobilgerät einschalten“ unter Einstellungen > Allgemein > Netzwerk > Experteneinstellungen. Bei LG aktiviere „Fernseher per Mobilgerät einschalten“ ([Schritt für Schritt](@lg-on)). Bei einem Roku-TV aktiviere „TV-Schnellstart“ unter Einstellungen > System > Energie. Bei Google TV und Android TV suche nach Wake on LAN oder „Einschalten über Netzwerk“, falls dein Modell das hat. Das machst du einmal, bei eingeschaltetem Fernseher.'),
      ('Wenn du keine Taste findest', 'Einige neuere Fernseher verstecken die einzige Taste so gut, dass es wirkt, als gäbe es keine. Suche nach einer kleinen Wölbung oder einem Lichtsensorbereich unter dem Bildschirm: Die Taste sitzt oft direkt daneben. Über WLAN braucht Mando TV, dass der Fernseher einmal an war und verbunden ist. Infrarot ist die Ausnahme: Auf einem Android-Handy mit Infrarotsender kann Mando TV einen Fernseher einschalten, der nie eingerichtet wurde, solange du das Handy auf den Fernseher richtest. Infrarot ist neu und funktioniert mit den Marken in der App-Codeliste.'),
      ('Kostenlos und Pro', 'Die Fernbedienung kannst du kostenlos laden und nutzen, ohne Werbung und ohne Abo. Mando TV Pro ist ein optionaler Einmalkauf für Extras.'),
    ],
    marca=None,
    faq=[
      ('Kann ich einen Fernseher mit dem Handy einschalten, wenn ich ihn nie eingerichtet habe?', 'Nicht über WLAN. Ein ausgeschalteter Fernseher wacht nur vom Netzwerk auf, wenn das Einschalten über das Netzwerk vorher aktiviert war. Beim ersten Mal nutze die Taste am Fernseher. Die Ausnahme ist ein Android-Handy mit Infrarotsender: Mando TV kann einen Fernseher ohne Einrichtung per Infrarot einschalten, wenn die Marke in der Codeliste steht oder du „Andere Marke oder weiß nicht“ wählst.'),
      ('Wie schalte ich einen Samsung-Fernseher ohne Fernbedienung ein?', 'Drücke die Steuerungs-Taste unter der Mitte des Bildschirms oder auf der Rückseite an einer unteren Ecke. Aktiviere dann „Mit Mobilgerät einschalten“, damit dein Handy ihn beim nächsten Mal einschalten kann.'),
      ('Wie schalte ich einen Roku-TV ohne Fernbedienung ein?', 'Nutze die Taste am Fernseher, meist unter der Mitte oder auf der Rückseite. Aktiviere dann „TV-Schnellstart“ unter Einstellungen > System > Energie, damit Mando TV ihn von deinem Handy aus einschalten kann.'),
      ('Warum schaltet sich mein Fernseher automatisch ein, wenn ich die Konsole einschalte?', 'Das ist HDMI-CEC. Es ist praktisch, und du kannst es in den Fernsehereinstellungen ausschalten, wenn du das bevorzugst.'),
    ]),
  dict(clave='sony', corto='Sony-Fernbedienung', fecha='2026-11-23',
    titulo='Sony Fernbedienungs-App für Handy und PC',
    desc='Mando TV steuert Sony-Bravia-Fernseher mit Google TV oder Android TV per WLAN. Beta-Unterstützung für Modelle von 2013 bis 2015 ohne Android.',
    h1='So steuerst du deinen Sony-Fernseher mit dem Handy',
    intro='Neuere Sony Bravia Smart-TVs nutzen Google TV, ältere Modelle ab 2015 Android TV. Mando TV steuert beide über dein WLAN vom iPhone, Android-Handy oder Windows-PC aus. Die App ersetzt die Original-Fernbedienung, wenn sie verloren gegangen ist oder die Batterien leer sind.',
    pasos=[
      'Prüfe, ob dein Sony-Fernseher den Startbildschirm von Google TV oder Android TV anzeigt. Das gilt für die meisten Sony Bravia Smart-TVs ab Baujahr 2015.',
      'Verbinde dein Handy und den Fernseher mit demselben WLAN.',
      'Öffne Mando TV und tippe in der Liste auf deinen Sony-Fernseher.',
      'Gib den Code aus 6 Zeichen ein, den der Fernseher auf dem Bildschirm anzeigt (nur beim ersten Mal). Du brauchst dafür keine Fernbedienung.',
      'Nutze die Pfeiltasten, OK, Zurück, Home, Lautstärke und die Tastatur.',
    ],
    extra=[
      ('Einen Sony-Fernseher vom Handy aus einschalten', 'Sony-Modelle mit Google TV oder Android TV können über das Netzwerk aufgeweckt werden, wenn „Remote start“ aktiviert ist. Die Option findest du meist unter Einstellungen > Netzwerk & Internet > Remote start (der Pfad kann je nach Modell leicht abweichen). Tippe dann in Mando TV auf den Fernseher, während er ausgeschaltet ist, und die App schaltet ihn ein.'),
      ('Wo sich die Ein-/Aus-Taste an einem Sony befindet', 'Bei den meisten Bravia-Fernsehern sitzt sie an der Rückseite, nahe der unteren linken oder rechten Ecke, oder an einer Seitenkante. Ein kurzer Druck schaltet den Fernseher ein. Mehr dazu findest du in [Fernseher ohne Fernbedienung einschalten](@turn-on).'),
      ('Ältere Sony-Fernseher', 'Sony-Bravia-Fernseher von 2013 bis 2015, die kein Android nutzen, werden in Mando TV im Beta-Status unterstützt. Das ist neu und kann noch Ecken und Kanten haben. Der Fernseher zeigt einen 4-stelligen PIN an, den du in der App eingeben musst. Andere Sony-Fernseher ohne Google TV oder Android TV werden derzeit nicht unterstützt.'),
      ('Kostenlos und Pro', 'Die Fernbedienung kannst du kostenlos laden und nutzen, ohne Werbung und ohne Abo. Mando TV Pro ist ein optionaler Einmalkauf für Extras.'),
    ],
    marca='android',
    faq=[
      ('Funktioniert Mando TV mit Sony-Bravia-Fernsehern?', 'Ja, mit Sony-Fernsehern, die Google TV oder Android TV nutzen. Das umfasst die meisten Sony Smart-TVs ab Baujahr 2015.'),
      ('Brauche ich eine Sony-App oder ein Google-Konto?', 'Nein. Mando TV koppelt sich mit dem Code auf dem Fernsehbildschirm und verlangt kein Konto.'),
      ('Funktioniert es mit älteren Sony-Bravia-Fernsehern ohne Android?', 'Ja, im Beta-Status, bei Bravia-Modellen von 2013 bis 2015 ohne Android. Die Kopplung erfolgt über einen 4-stelligen PIN, der auf dem Fernseher angezeigt wird.'),
      ('Kann ich auf meinem Sony-Fernseher vom Handy aus tippen?', 'Ja. Die Tastatur ist kostenlos und funktioniert in YouTube, Netflix und der Fernsehsuche.'),
    ]),
  dict(clave='tcl', corto='TCL-Fernbedienung', fecha='2026-11-23',
    titulo='TCL Fernbedienungs-App für Handy und PC',
    desc='TCL-Fernbedienung verloren? Die meisten TCL-Fernseher nutzen Roku TV oder Google TV. Mando TV steuert beides per WLAN, ohne Konto und Werbung.',
    h1='So steuerst du deinen TCL-Fernseher mit dem Handy',
    intro='TCL baut den Fernseher, die Software ist aber Roku TV oder Google TV (bei älteren Modellen Android TV). Mando TV steuert beide Systeme und funktioniert als Fernbedienung für deinen TCL-Fernseher über das WLAN. Kostenlos, ohne Konto und Werbung.',
    pasos=[
      'Finde heraus, welches System dein TCL nutzt. Zeigt der Startbildschirm ein einfaches Raster aus Kanal-Kacheln, ist es Roku TV. Sieht er wie Google TV oder Android TV mit Reihen voller Empfehlungen aus, ist es Google TV.',
      'Verbinde dein Handy und den TCL-Fernseher mit demselben WLAN.',
      'Öffne Mando TV. Der TCL erscheint von selbst in der Liste. Tippe darauf.',
      'Bei einem TCL mit Roku TV ist nichts weiter nötig. Bei einem TCL mit Google TV gibst du den Code aus 6 Zeichen ein, den der Fernseher auf dem Bildschirm zeigt (nur beim ersten Mal).',
      'Nutze die Pfeile, OK, Zurück, Home, Lautstärke und Tastatur. Schalte den Fernseher über die App ein, wenn du das Einschalten über das Netzwerk aktiviert hast (siehe unten).',
    ],
    extra=[
      ('Einen TCL-Fernseher vom Handy aus einschalten', 'Bei TCL Roku TV aktiviere „TV-Schnellstart“ unter Einstellungen > System > Energie. Bei TCL Google TV suche eine Option für Wake on LAN, „Einschalten über Netzwerk“ oder Fernstart in den Netzwerk- oder Energieeinstellungen. Manche Modelle bieten dies nicht. Schalte den Fernseher in diesem Fall mit der physischen Ein-/Aus-Taste ein, meist unten in der Mitte oder an der Rückseite.'),
      ('Wenn dein TCL nicht erscheint', 'Prüfe, ob Handy und Fernseher im selben WLAN sind. Router mit getrennten 2,4-GHz- und 5-GHz-Netzen können Geräte voneinander verstecken. Erlaube auf dem iPhone „Lokales Netzwerk“ für Mando TV in den Einstellungen. Du kannst den Fernseher auch hinzufügen, indem du seine IP-Adresse eingibst. Lies [Dein Handy findet den Fernseher nicht](@not-found).'),
      ('Mehr zu deinem TCL', 'Für TCL mit Roku TV siehe [Roku Fernbedienungs-App](@roku), für TCL mit Google TV oder Android TV [Android TV Fernbedienungs-App](@android).'),
      ('Kostenlos und Pro', 'Pfeiltasten, OK, Zurück, Home, Lautstärke, Kanäle, Ziffern, Tastatur, Apps öffnen, Eingänge wechseln und Ein-/Ausschalten sind kostenlos, ohne Werbung und Abo. Mando TV Pro ist ein optionaler Einmalkauf für Extras.'),
    ],
    marca=None,
    faq=[
      ('Funktioniert Mando TV mit jedem TCL-Fernseher?', 'Es funktioniert mit TCL-Fernsehern mit Roku TV, Google TV oder Android TV, also mit den meisten TCL-Smart-TVs. Ein TCL, der kein Smart-TV ist, kann nicht über WLAN gesteuert werden.'),
      ('Brauche ich die TCL App oder ein TCL-Konto?', 'Nein. Mando TV verbindet sich direkt über dein WLAN zu Hause und benötigt kein Konto.'),
      ('Mein TCL fragt nach einem Code. Wo ist er?', 'TCL-Modelle mit Google TV und Android TV zeigen einen Code aus 6 Zeichen auf dem Bildschirm. Gib ihn genau so in Mando TV ein. Ein TCL mit Roku TV fragt nicht nach einem Code.'),
    ]),
  dict(clave='hisense', corto='Hisense-Fernbedienung', fecha='2026-11-23',
    titulo='Hisense Fernbedienungs-App: Was am Handy funktioniert',
    desc='Hisense-Fernbedienung mit Mando TV: Steuerung für VIDAA, Roku TV, Google TV und Fire TV über WLAN. Ehrliche Übersicht, was funktioniert.',
    h1='Hisense Fernbedienungs-App: was funktioniert und was nicht',
    intro='Hisense-Fernseher sind innen nicht alle gleich. Je nach Modell nutzen sie das eigene VIDAA-System von Hisense, Roku TV, Google TV oder Fire TV. Mando TV funktioniert als Fernbedienung für Hisense auf allen vier Systemen, mit einer Ausnahme bei einigen neueren VIDAA-Modellen. Hier siehst du, wie du erkennst, welches System du hast und was dich erwartet.',
    pasos=[
      'Prüfe, welches System dein Hisense nutzt. VIDAA ist die eigene Oberfläche von Hisense. Roku TV zeigt ein Raster aus Kanal-Kacheln. Google TV zeigt Reihen mit Empfehlungen. Fire TV zeigt den Fire-TV-Startbildschirm mit Amazon-Reihen.',
      'Verbinde dein Handy und den Hisense-Fernseher mit demselben WLAN.',
      'Öffne Mando TV. Der Fernseher erscheint von selbst in der Liste. Tippe darauf.',
      'VIDAA- und Fire-TV-Modelle zeigen möglicherweise einen PIN mit vier Ziffern; Google TV zeigt einen Code mit sechs Zeichen. Gib ihn in die App ein. Roku TV fragt nach nichts. Das machst du nur einmal.',
      'Nutze die Pfeile, OK, Zurück, Home, Lautstärke und Tastatur von deinem Handy.',
    ],
    extra=[
      ('Hisense mit Roku TV oder Google TV', 'Diese funktionieren vollständig wie jeder andere Roku- oder Google-TV-Fernseher. Details auf den Seiten [Roku Fernbedienungs-App](@roku) und [Android TV Fernbedienungs-App](@android).'),
      ('Hisense mit Fire TV', 'Die Unterstützung für Fire TV ist neu in Mando TV. Aktualisiere die App auf die neueste Version aus deinem Store. Wie die Kopplung mit PIN funktioniert, steht auf der Seite [Fire-TV-Fernbedienungs-App](@firetv). Wenn etwas nicht wie erwartet funktioniert, schreibe uns über die Hilfe-Seite und nenne dein Modell.'),
      ('Hisense mit VIDAA', 'Die meisten VIDAA-Modelle funktionieren: Tasten, Lautstärke, Tastatur, Apps und Eingänge. Einige neuere VIDAA-Modelle akzeptieren nur die offizielle Hisense-App. Mando TV erkennt das beim Verbinden und sagt es dir klar, statt stillschweigend zu versagen. In diesem Fall sind die Hisense-App für dein Modell, die Tasten am Fernseher oder die Original-Fernbedienung der richtige Weg.'),
      ('Einen Hisense vom Handy aus einschalten', 'Bei Hisense Roku TV aktiviere „TV-Schnellstart“ unter Einstellungen > System > Energie. Bei Google TV suche nach einer Option für Wake on LAN oder „Einschalten über Netzwerk“. Wenn keine existiert, nutze die Ein-/Aus-Taste am Fernseher.'),
      ('Kostenlos und Pro', 'Pfeiltasten, OK, Zurück, Home, Lautstärke, Kanäle, Zifferntasten, Tastatur, Öffnen von Apps, Wechseln der Eingänge und Ein- oder Ausschalten sind kostenlos, ohne Werbung und ohne Abo. Mando TV Pro ist ein optionaler Einmalkauf für Extras.'),
    ],
    marca=None,
    faq=[
      ('Funktioniert Mando TV mit Hisense VIDAA?', 'Ja, mit den meisten VIDAA-Modellen. Einige neuere akzeptieren nur die offizielle Hisense-App; Mando TV erkennt das und sagt es dir. Hisense-Fernseher mit Roku TV, Google TV oder Fire TV werden ebenfalls unterstützt.'),
      ('Wie weiß ich, ob mein Hisense Roku TV, Google TV oder Fire TV ist?', 'Schau auf den Startbildschirm. Roku TV hat ein einfaches Raster aus Kacheln und ein Roku-Logo beim Start. Google TV hat Reihen mit Empfehlungen. Fire TV hat den Startbildschirm von Amazon Fire TV. Der Modellname unter Einstellungen > Über gibt ebenfalls Auskunft.'),
      ('Brauche ich ein Hisense- oder Google-Konto?', 'Nein. Mando TV verbindet sich direkt über dein WLAN zu Hause und hat kein eigenes Konto.'),
    ]),
  dict(clave='philips', corto='Philips-Fernbedienung', fecha='2026-11-23',
    titulo='Philips Fernbedienungs-App: Roku TV, Google TV, Android TV',
    desc='Mando TV steuert Philips-Fernseher mit Roku TV, Google TV oder Android TV über WLAN, vom Handy oder PC aus. Titan OS wird nicht unterstützt.',
    h1='Philips-Fernseher mit dem Handy steuern',
    intro='Philips-Fernseher nutzen je nach Land und Baujahr verschiedene Systeme: Roku TV in den USA, Google TV oder Android TV in vielen Ländern und Titan OS bei einigen neueren europäischen Modellen. Mando TV steuert die Modelle mit Roku TV, Google TV und Android TV über WLAN.',
    pasos=[
      'Prüfe den Startbildschirm. Roku TV zeigt ein Raster aus Kacheln. Google TV und Android TV zeigen Reihen von Empfehlungen von Google. Titan OS hat einen eigenen Startbildschirm.',
      'Verbinde dein Handy und den Fernseher mit demselben WLAN.',
      'Öffne Mando TV und tippe in der Liste auf deinen Philips-Fernseher.',
      'Roku TV fragt nach nichts. Google TV und Android TV zeigen einen Code mit 6 Zeichen: Gib ihn einmal in die App ein.',
      'Nutze die Pfeiltasten, OK, Zurück, Home, Lautstärke und Tastatur.',
    ],
    extra=[
      ('Philips Roku TV', 'Funktioniert wie jeder Roku-Fernseher. Um es vom Handy aus einzuschalten, aktiviere „TV-Schnellstart“ unter Einstellungen > System > Energie. Mehr auf der Seite [Roku Fernbedienungs-App](@roku).'),
      ('Philips mit Google TV oder Android TV', 'Umfasst viele Ambilight-Modelle. Sie koppeln mit dem Code auf dem Bildschirm. Um sie vom Handy aus einzuschalten, suche in den Netzwerk- oder Energieeinstellungen nach Wake on LAN oder „Einschalten über Netzwerk“. Bei einigen Modellen fehlt diese Option. Mehr auf der Seite [Android TV Fernbedienungs-App](@android).'),
      ('Ältere Philips-Fernseher ohne Android', 'Philips-Fernseher von 2011 bis 2015, die kein Android nutzen, werden in Mando TV in der Beta unterstützt. Sie ist neu und benötigt keinen Kopplungscode.'),
      ('Philips mit Titan OS', 'Titan OS ist ein anderes System, das Mando TV heute nicht steuert, und das sagen wir lieber klar. Neuere Philips-Modelle ohne Android sind ebenfalls nicht abgedeckt.'),
      ('Kostenlos und Pro', 'Die Fernbedienung kannst du kostenlos laden und nutzen, ohne Werbung und ohne Abo. Mando TV Pro ist ein optionaler Einmalkauf für Extras.'),
    ],
    marca=None,
    faq=[
      ('Funktioniert Mando TV mit Philips-Fernsehern?', 'Mit Philips-Fernsehern, die Roku TV, Google TV oder Android TV nutzen, ja, und in der Beta mit Philips-Fernsehern von 2011 bis 2015 ohne Android. Modelle mit Titan OS werden nicht unterstützt.'),
      ('Steuert Mando TV Ambilight?', 'Mando TV ist eine Fernbedienung: Sie sendet die Tasten, sodass du mit den Pfeilen und OK zu den Ambilight-Einstellungen kommst. Es gibt keine separaten Ambilight-Steuerungen.'),
      ('Brauche ich ein Philips- oder Google-Konto?', 'Nein. Mando TV verbindet sich über dein WLAN zu Hause und benötigt kein Konto.'),
    ]),
]
OTRAS_GUIAS += [
  ('no-sub', 'Eine Fernbedienungs-App ohne Abo und ohne Werbung'),
  ('roku-app-alt', 'Alternative zur Roku App: eine für alle Fernseher'),
  ('lg-thinq', 'Alternative zur LG ThinQ App für deinen LG-Fernseher'),
  ('smartthings', 'SmartThings-Alternative für Samsung-Fernseher'),
  ('googletv-alt', 'Alternative zur Google-TV-Fernbedienung auf dem Handy'),
  ('windows', 'Fernbedienungs-App für den Windows-PC'),
  ('iphone', 'Fernbedienungs-App fürs iPhone: eine für alle Fernseher'),
  ('firetv', 'Fire-TV-Fernbedienung für dein Handy oder deinen PC'),
  ('firetv-lost', 'Fire-TV-Fernbedienung verloren: So nutzt du dein Handy'),
  ('turn-on', 'So schaltest du einen Fernseher ohne Fernbedienung ein'),
  ('sony', 'So steuerst du deinen Sony-Fernseher mit dem Handy'),
  ('tcl', 'So steuerst du deinen TCL-Fernseher mit dem Handy'),
  ('hisense', 'Hisense Fernbedienungs-App: was funktioniert und was nicht'),
  ('philips', 'Philips-Fernseher mit dem Handy steuern'),
]
# <<< guías traídas del inglés
