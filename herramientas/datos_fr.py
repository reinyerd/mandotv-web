# Textos en francés (vouvoiement) de mandotv.app. Los usa generar_idiomas.py. Escritos para las búsquedas de Francia, Bélgica,
# Suiza francófona y Canadá. Las claves de las páginas y sus rutas están en idiomas_sitio.py.
# Los nombres de menús de cada marca y de los botones de la app son los mismos que usa la app en francés
# (lib/l10n/app_fr.arb del proyecto de la app).
# Tipografía francesa: se escribe con espacio normal antes de : ; ? ! y dentro de « », y al final del archivo se convierte en
# espacio duro (U+00A0) en todos los textos, para que la puntuación no quede sola al final de una línea.

UI = dict(
  locale='fr_FR',
  aria_home='Mando TV, accueil', aria_main='Principal', nav_que='Fonctions', nav_ayuda='Aide', nav_contacto='Contact',
  asunto='Bonjour%20Mando%20TV', inicio='Accueil', privacidad='Confidentialité', aria_pie='Pied de page', aria_ruta="Fil d'Ariane",
  aria_marcas='Marques et guides', hecho='Conçu au Chili',
  aviso="Mando TV est une app indépendante : elle n'est ni affiliée aux fabricants de TV cités ni à Google, Amazon ou Roku, ni approuvée par eux. Les marques appartiennent à leurs propriétaires et sont citées uniquement pour indiquer la compatibilité. Android TV et Google TV sont des marques de Google LLC.",
  bajar='Télécharger gratuitement', descarga='Télécharger sur', anticipada='Accès anticipé sur',
  apple_aria="Télécharger Mando TV gratuitement sur l'App Store", ms_aria='Télécharger Mando TV gratuitement sur le Microsoft Store',
  gp_aria='Accès anticipé à Mando TV sur Google Play pour Android', aria_desc='Télécharger Mando TV',
  b_como_btn='Comment se connecter', b_tiendas_label='Disponible dans les boutiques',
  b_nota='iPhone, iPad, Android et Windows. Téléchargement gratuit, sans publicité. Pro est un achat unique, sans abonnement.',
  b_compat='Téléviseurs compatibles', b_otras='Autres marques', b_otras_p='Mando TV pilote toutes ces marques depuis la même application :',
  g_guias='Guides', g_ver='Voir les étapes', g_pasos='Pas à pas', g_hazlo='Faites-le avec Mando TV',
  g_tiendas="Mando TV est une télécommande universelle pour votre téléviseur. Téléchargez-la gratuitement, sans publicité et sans compte. Pro est un achat unique facultatif, sans abonnement. Pour iPhone, iPad, Windows et Android :",
  g_nota='Android : accès anticipé gratuit sur Google Play. <a href="{enlace}">Participez en deux étapes</a> et aidez-nous à arriver dans la boutique.',
  g_mas_pagina='Plus de détails sur la page {enlace}.', g_mas_marca='Plus de détails par marque :',
  g_faq='Questions fréquentes', g_mas='Autres guides', g_todas='Tous les guides', g_ayuda='Aide et assistance',
  g_idiomas="Ce guide dans d'autres langues",
)

PIE = [
  ('samsung', 'Télécommande Samsung'),
  ('lg', 'Télécommande LG'),
  ('roku', 'Télécommande Roku'),
  ('android', 'Télécommande Android TV'),
  ('guias', 'Tous les guides'),
  ('lost-tv', 'Télécommande TV perdue'),
  ('lost-lg', 'Télécommande LG perdue'),
  ('lg-on', 'Allumer une TV LG avec le téléphone'),
  ('hdmi', "Changer d'entrée HDMI sans télécommande"),
  ('androidtv', 'Android TV sans télécommande'),
  ('console', 'Allumer la TV et passer au HDMI de la console'),
  ('samsung-lost', 'TV Samsung sans télécommande'),
  ('roku-lost', 'Télécommande Roku perdue'),
  ('roku-403', "L'application Roku ne fonctionne pas"),
  ('androidtv-code', "Code d'appairage Android TV"),
  ('not-found', 'Le téléphone ne trouve pas la TV'),
  ('wifi', 'Téléphone comme télécommande en Wi-Fi'),
  ('pc', 'Contrôler la TV depuis un PC'),
]
NOMBRE_OTRA = {'lg': 'Application télécommande LG', 'samsung': 'Application télécommande Samsung', 'roku': 'Application télécommande Roku',
               'android': 'Application télécommande Android TV et Google TV'}
PAGINA_MARCA = {'lg': 'application télécommande LG', 'samsung': 'application télécommande Samsung', 'roku': 'application télécommande Roku',
                'android': 'application télécommande Android TV'}

OTRAS_GUIAS = [
  ('lg-on', 'Allumer une TV LG avec le téléphone'),
  ('lost-tv', 'Télécommande de TV perdue : que faire'),
  ('lost-lg', 'Télécommande LG perdue : utilisez votre téléphone'),
  ('hdmi', "Changer d'entrée HDMI sur une TV sans télécommande"),
  ('androidtv', 'Android TV sans télécommande : utilisez votre téléphone'),
  ('console', 'Allumer la TV et passer au HDMI de la console sans télécommande'),
  ('samsung-lost', "TV Samsung sans la télécommande d'origine : utilisez votre téléphone"),
  ('roku-lost', 'Télécommande Roku perdue : utilisez votre téléphone'),
  ('roku-403', "L'application Roku ne fonctionne pas : corriger l'erreur 403"),
  ('androidtv-code', "Android TV demande un code d'appairage : que faire"),
  ('not-found', 'Votre téléphone ne trouve pas la TV : que vérifier'),
  ('wifi', 'Utiliser votre téléphone comme télécommande en Wi-Fi'),
  ('pc', 'Contrôler votre TV depuis un PC Windows'),
]

INDICE = dict(
  titulo='Guides : piloter la TV avec le téléphone | Mando TV',
  desc="Guides pas à pas pour utiliser votre téléphone ou PC comme télécommande : allumer la TV, changer d'entrée HDMI et résoudre les problèmes Samsung, LG, Roku.",
  h1='Guides : utiliser le téléphone comme télécommande',
  intro='Des étapes simples pour connecter, allumer et dépanner la télécommande de votre TV Samsung, LG, Roku ou Android TV avec Mando TV.',
  h2_guias='Tous les guides', h2_marcas='Application télécommande par marque',
)

MARCAS = [
  dict(clave='lg', color='#e0457b', corto='LG',
    titulo='Télécommande LG sur téléphone, appli gratuite | Mando TV',
    desc="Votre téléphone ou PC comme télécommande de TV LG webOS, en Wi-Fi. Touches, clavier, apps, sources et allumage gratuits ; pointeur avec Pro.",
    h1='Télécommande LG : application pour votre téléphone',
    intro="Mando TV est une application de télécommande pour TV LG : elle transforme votre téléphone ou votre ordinateur, via le Wi-Fi de la maison, en télécommande de votre Smart TV LG sous webOS. Elle dépanne si vous avez perdu la télécommande, si ses piles sont vides ou si vous voulez simplement écrire plus vite.",
    compat="Smart TV LG sous webOS (la plupart des modèles LG Smart TV depuis 2014). Fonctionne avec les téléviseurs LED, NanoCell, QNED et OLED.",
    h2=dict(funciones='Ce que vous pouvez faire avec votre TV LG', como='Comment connecter votre TV LG à Mando TV',
            encender='Allumer votre TV LG depuis le téléphone', preguntas='Questions sur LG', guias='Guides pour LG'),
    funciones=[
      ('Toutes les touches', 'Croix directionnelle, OK, Retour, Accueil, volume, chaînes, muet et lecture.'),
      ('Pointeur comme la Magic Remote (Pro)', "Déplacez la flèche sur l'écran avec le doigt, comme avec la Magic Remote de LG."),
      ('Clavier', "Écrivez dans YouTube, Netflix ou le navigateur de la TV avec le clavier de votre téléphone."),
      ('Apps et sources', 'Ouvrez vos applications et passez à HDMI, la TV en direct, AirPlay ou Screen Share.'),
      ('Sortie audio (Pro)', 'Basculez entre les haut-parleurs de la TV et votre barre de son.'),
      ('Allumer la TV', "Si elle est éteinte, Mando TV l'allume par le réseau et se connecte tout seul."),
    ],
    pasos=[
      'Connectez le téléphone et la TV au même réseau Wi-Fi.',
      'Ouvrez Mando TV : votre TV LG apparaît toute seule dans la liste. Touchez-la.',
      "Un message apparaît sur l'écran de la TV pour demander l'autorisation. Acceptez-le avec votre télécommande habituelle (seulement la première fois).",
    ],
    encender="Sur la TV LG, ouvrez les Paramètres et cherchez « Téléviseur en marche avec mobile » (dans Tous les paramètres > Général > Appareils > Appareils externes). Activez « Allumer via Wi-Fi ». Si « Démarrage rapide+ » existe, activez-le aussi. Ensuite, quand vous toucherez la TV éteinte dans Mando TV, l'application vous demandera si vous voulez l'allumer et se connectera toute seule.",
    faq=[
      ('Ai-je besoin de la Magic Remote pour utiliser Mando TV ?', "Seulement la première fois, pour accepter le message sur l'écran. Ensuite, votre téléphone suffit."),
      ("Mando TV remplace-t-elle l'application LG ThinQ ?", "Pour piloter la TV, oui : il ne faut ni compte LG ni enregistrer la TV. Mando TV se connecte directement par votre Wi-Fi."),
      ('Puis-je allumer ma TV LG depuis mon téléphone ?', "Oui, si vous activez « Téléviseur en marche avec mobile » sur la TV et que vous vous êtes connecté une fois pendant que la TV était allumée."),
    ],
    guias=[('lg-on', 'Comment allumer une TV LG avec le téléphone'),
           ('lost-lg', 'Télécommande LG perdue : utilisez votre téléphone'),
           ('hdmi', "Changer d'entrée HDMI sur une TV sans télécommande"),
           ('guias', 'Tous les guides pour piloter la TV avec le téléphone')]),
  dict(clave='samsung', color='#3d7bff', corto='Samsung',
    titulo='Télécommande Samsung sur téléphone, application | Mando TV',
    desc="Votre téléphone ou PC comme télécommande de TV Samsung Tizen, en Wi-Fi. Touches, clavier, apps et allumage gratuits ; pavé tactile avec Pro. Sans pub.",
    h1='Télécommande Samsung : application pour votre téléphone',
    intro="Mando TV est une application de télécommande pour TV Samsung : elle transforme votre téléphone ou votre ordinateur, via le Wi-Fi de la maison, en télécommande de votre Smart TV Samsung. Il ne faut ni compte Samsung ni enregistrer la TV.",
    compat="Smart TV Samsung sous Tizen, modèles 2016 et plus récents (séries comme Crystal UHD, QLED, Neo QLED, The Frame et OLED).",
    h2=dict(funciones='Ce que vous pouvez faire avec votre TV Samsung', como='Comment connecter votre TV Samsung à Mando TV',
            encender='Allumer votre TV Samsung depuis le téléphone', preguntas='Questions sur Samsung', guias='Guides pour Samsung'),
    funciones=[
      ('Toutes les touches', 'Croix directionnelle, OK, Retour, Accueil, volume, chaînes, muet et source.'),
      ('Pavé tactile (Pro)', 'Glissez le doigt pour vous déplacer dans les menus sans chercher les flèches.'),
      ('Clavier', 'Écrivez vos recherches et vos mots de passe avec le clavier de votre téléphone.'),
      ('Apps', "Ouvrez Netflix, YouTube, Prime Video et vos autres applications d'un seul geste."),
      ('Allumer la TV', "Si elle est éteinte, Mando TV l'allume par le réseau et se connecte tout seul."),
      ('Sans compte', 'La connexion se fait directement par votre Wi-Fi, sans passer par Internet.'),
    ],
    pasos=[
      'Connectez le téléphone et la TV au même réseau Wi-Fi.',
      'Ouvrez Mando TV : votre TV Samsung apparaît toute seule dans la liste. Touchez-la.',
      'La TV demande si vous autorisez la connexion. Choisissez « Autoriser » avec la télécommande (seulement la première fois).',
    ],
    encender="Sur la TV Samsung, ouvrez Paramètres > Général > Réseau > Paramètres d'expert et activez « Allumer avec un appareil mobile ». Ensuite, quand vous toucherez la TV éteinte dans Mando TV, l'application vous demandera si vous voulez l'allumer et se connectera toute seule.",
    faq=[
      ("J'ai refusé l'autorisation par erreur. Que faire ?", "Sur la TV, allez dans Paramètres > Général > Gestionnaire de périphériques externes > Gestionnaire de connexion de périphérique, et réglez Mando TV sur autorisé."),
      ('Mando TV remplace-t-elle SmartThings ?', "Pour piloter la TV, oui, et sans compte Samsung. Mando TV se connecte directement par votre Wi-Fi."),
      ('Fonctionne-t-elle avec les anciennes TV Samsung ?', "Elle fonctionne avec les TV Samsung sous Tizen, modèles 2016 et plus récents. Les modèles antérieurs utilisent un autre système que nous ne prenons pas encore en charge."),
    ],
    guias=[('samsung-lost', "TV Samsung sans la télécommande d'origine : utilisez votre téléphone"),
           ('hdmi', "Changer d'entrée HDMI sur une TV sans télécommande"),
           ('guias', 'Tous les guides pour piloter la TV avec le téléphone')]),
  dict(clave='roku', color='#a77bff', corto='Roku',
    titulo='Télécommande Roku sur téléphone, appli gratuite | Mando TV',
    desc="Votre téléphone ou PC comme télécommande de Roku TV ou de lecteur Roku, en Wi-Fi. Touches, clavier, chaînes, sources et allumage gratuits.",
    h1='Télécommande Roku : application pour votre téléphone',
    intro="Mando TV est une application de télécommande pour Roku : elle transforme votre téléphone ou votre ordinateur, via le Wi-Fi de la maison, en télécommande de votre Roku. Elle fonctionne avec les téléviseurs Roku TV et avec les lecteurs Roku qui se branchent en HDMI.",
    compat="Téléviseurs Roku TV (TCL, Hisense, Philips, Sharp, JVC et autres) et lecteurs Roku (Express, Streaming Stick, Ultra).",
    h2=dict(funciones='Ce que vous pouvez faire avec votre Roku', como='Comment connecter votre Roku à Mando TV',
            encender='Allumer votre Roku depuis le téléphone', preguntas='Questions sur Roku', guias='Guides pour Roku'),
    funciones=[
      ('Toutes les touches', 'Croix directionnelle, OK, Retour, Accueil, volume, muet, rejouer et lecture.'),
      ('Clavier', 'Écrivez vos recherches dans les chaînes Roku avec le clavier de votre téléphone.'),
      ('Chaînes', "Ouvrez Netflix, YouTube et vos autres chaînes Roku d'un seul geste."),
      ('Sources', "Sur un Roku TV, passez à HDMI, à l'antenne ou à AV depuis l'application."),
      ('Allumer la TV', 'Sur les Roku TV avec démarrage rapide, Mando TV les allume depuis votre téléphone.'),
      ('Sans association', "Roku ne demande aucun code : touchez-le dans la liste et vous êtes connecté."),
    ],
    pasos=[
      'Connectez le téléphone et le Roku au même réseau Wi-Fi.',
      'Ouvrez Mando TV : votre Roku apparaît tout seul dans la liste. Touchez-le.',
      "S'il ne se connecte pas, sur le Roku allez dans Paramètres > Système > Paramètres système avancés > Contrôle par applications mobiles, et réglez l'accès au réseau sur Par défaut ou Permissif.",
    ],
    encender="Sur les Roku TV, activez « Démarrage rapide de la TV » dans Paramètres > Système > Alimentation. Les lecteurs Roku branchés sur une autre TV ne peuvent pas être allumés ainsi. Ensuite, quand vous toucherez la TV éteinte dans Mando TV, l'application vous demandera si vous voulez l'allumer et se connectera toute seule.",
    faq=[
      ('Fonctionne-t-elle avec le Roku Express ou le Streaming Stick ?', 'Oui. Tous les lecteurs Roku et les téléviseurs Roku TV se pilotent de la même façon.'),
      ('Mando TV ne trouve pas mon Roku. Que faire ?', "Vérifiez que les deux sont sur le même réseau Wi-Fi et que « Contrôle par applications mobiles » n'est pas désactivé sur le Roku. Vous pouvez aussi l'ajouter en saisissant son adresse IP."),
      ('Faut-il un compte Roku ?', 'Non. Mando TV se connecte directement par votre Wi-Fi.'),
    ],
    guias=[('roku-403', "L'application Roku ne fonctionne pas (erreur 403)"),
           ('roku-lost', 'Télécommande Roku perdue : utilisez votre téléphone'),
           ('guias', 'Tous les guides pour piloter la TV avec le téléphone')]),
  dict(clave='android', color='#2fbf8f', corto='Android TV et Google TV',
    titulo='Télécommande Android TV sur téléphone | Mando TV',
    desc="Votre téléphone ou PC comme télécommande Android TV (Sony, TCL, Xiaomi), en Wi-Fi. Touches, clavier, apps et allumage gratuits ; pavé tactile avec Pro.",
    h1='Télécommande Android TV : application pour votre téléphone',
    intro="Mando TV est une application de télécommande pour Android TV : elle transforme votre téléphone ou votre ordinateur, via le Wi-Fi de la maison, en télécommande de votre Android TV ou Google TV. Elle fonctionne aussi depuis un iPhone et depuis Windows.",
    compat="Téléviseurs sous Google TV ou Android TV de Sony, Philips, TCL, Hisense, Sharp, Xiaomi, Toshiba, Panasonic, Haier, Skyworth, JVC, Thomson, Motorola, OnePlus, iFFALCON, Kogan, Vu et d'autres marques, ainsi que Chromecast avec Google TV, Google TV Streamer, onn. et Nvidia Shield. Certaines de ces marques vendent aussi des modèles avec un autre système : si votre TV affiche l'écran d'accueil de Google TV ou propose la boutique Google Play, Mando TV la pilote.",
    h2=dict(funciones='Ce que vous pouvez faire avec votre Android TV', como='Comment connecter votre Android TV à Mando TV',
            encender='Allumer votre Android TV depuis le téléphone', preguntas='Questions sur Android TV', guias='Guides pour Android TV'),
    funciones=[
      ('Toutes les touches', 'Croix directionnelle, OK, Retour, Accueil, volume, muet et lecture.'),
      ('Pavé tactile (Pro)', 'Glissez le doigt pour vous déplacer rapidement dans les menus de Google TV.'),
      ('Clavier', 'Écrivez vos recherches et vos mots de passe avec le clavier de votre téléphone.'),
      ('Apps', "Ouvrez YouTube, Netflix, Disney+ et vos autres applications d'un seul geste."),
      ('Allumer la TV', "Sur les modèles qui peuvent s'allumer par le réseau, Mando TV allume la TV et se connecte tout seul."),
      ('iPhone, Android et PC', 'Elle fonctionne de la même façon depuis tout téléphone ou ordinateur.'),
    ],
    pasos=[
      'Connectez le téléphone et la TV au même réseau Wi-Fi.',
      'Ouvrez Mando TV : votre Android TV apparaît tout seul dans la liste. Touchez-le.',
      "La TV affiche un code de 6 caractères. Saisissez-le dans Mando TV (seulement la première fois).",
    ],
    encender="Cela dépend du fabricant. Cherchez dans les paramètres réseau ou d'alimentation l'option « Wake on LAN », « Allumer par le réseau » ou « Activation par le réseau ». Certains modèles ne l'ont pas. Ensuite, quand vous toucherez la TV éteinte dans Mando TV, l'application vous demandera si vous voulez l'allumer et se connectera toute seule.",
    faq=[
      ('Fonctionne-t-elle avec Chromecast avec Google TV ?', "Oui, l'association se fait avec le code de 6 caractères qui apparaît à l'écran."),
      ("En quoi est-elle différente de l'application Google TV ?", "Mando TV n'a pas besoin de compte Google, fonctionne aussi depuis Windows et pilote les TV LG, Samsung et Roku depuis la même application."),
      ("Le code n'apparaît pas à l'écran. Que faire ?", "Fermez Mando TV, rouvrez l'application et touchez de nouveau la TV. Vérifiez que la TV n'est pas dans un mode d'économie d'énergie profond."),
    ],
    guias=[('androidtv-code', "Android TV demande un code d'appairage : que faire"),
           ('androidtv', 'Android TV sans télécommande : utilisez votre téléphone'),
           ('guias', 'Tous les guides pour piloter la TV avec le téléphone')]),
]

GUIAS = [
  dict(clave='lost-tv', corto='Télécommande TV perdue',
    titulo='Télécommande TV perdue ? Pilotez la TV au téléphone',
    desc="Télécommande de TV perdue ? Allumez la TV avec son bouton et utilisez votre téléphone comme télécommande. LG, Samsung, Roku, Android TV. Gratuit.",
    h1='Télécommande de TV perdue ? Voici ce que vous pouvez faire',
    intro="Une télécommande perdue, cela arrive dans toutes les maisons : elle disparaît juste au moment où vous voulez regarder quelque chose. La bonne nouvelle, c'est que votre téléphone peut faire office de télécommande, via le Wi-Fi de la maison. Voici ce qu'il faut faire, dans l'ordre.",
    pasos=[
      "Allumez la TV avec son bouton physique. Il se trouve presque toujours en bas au centre, ou à l'arrière près d'un coin. Parfois c'est un simple bouton, parfois un tout petit joystick.",
      'Connectez votre téléphone au même réseau Wi-Fi que la TV.',
      "Téléchargez Mando TV, qui est gratuite et ne demande pas de compte, puis ouvrez-la. Votre TV apparaît toute seule dans la liste. Touchez-la.",
      "Acceptez la connexion pour votre marque. Sur LG et Samsung, la TV affiche un message : acceptez-le avec le bouton ou le joystick de la TV elle-même. Sur Android TV et Google TV, vous saisissez un code de 6 caractères qui apparaît à l'écran. Roku ne demande rien.",
      'Et voilà. Les flèches, OK, Retour, Accueil, le volume, les chaînes et le clavier sont gratuits.',
      "Pour la prochaine fois, activez dans les paramètres de la TV l'allumage par le réseau (le guide de votre marque est plus bas) et vous pourrez allumer la TV depuis le téléphone sans la toucher.",
    ],
    extra=[
      ('Choisissez le guide de votre marque', 'LG : [Télécommande LG perdue](@lost-lg). Android TV et Google TV : [Android TV sans télécommande](@androidtv). Samsung : [TV Samsung sans télécommande](@samsung-lost). Roku : [Télécommande Roku perdue](@roku-lost).'),
      ("Si la TV ne s'allume pas avec le bouton", "Avant de chercher une autre télécommande, vérifiez que le câble est bien branché et que la prise murale est alimentée. Si le bouton de la TV ne fait rien, le problème vient de la TV et non de la télécommande."),
      ("Si la télécommande a simplement cessé de fonctionner", "Essayez des piles neuves. Pour vérifier si elle émet encore un signal, pointez-la vers l'appareil photo de votre téléphone et appuyez sur une touche : sur beaucoup de téléphones, vous verrez une lumière violette à l'écran. Si la lumière apparaît et que la TV ne répond pas, le capteur de la TV est peut-être masqué."),
      ("Si vous avez changé de box et que la TV a perdu son Wi-Fi", "Sans télécommande, il est plus difficile de connecter la TV au nouveau réseau. Le plus simple est de brancher la TV à la box avec un câble réseau. Vous pouvez aussi créer un réseau Wi-Fi avec le même nom et le même mot de passe qu'avant : la TV s'y reconnecte généralement toute seule."),
      ("Ce qui est gratuit et ce qui est Pro", "Allumer et éteindre la TV, les flèches, OK, le volume, les chaînes, les chiffres, le clavier, l'ouverture des applications et le changement de source sont gratuits. Le pavé tactile, la voix et les routines font partie de Mando TV Pro, un achat unique sans abonnement."),
    ],
    marca=None,
    faq=[
      ("Puis-je allumer la TV avec mon téléphone si je ne l'ai jamais connectée ?", "Cette première fois, allumez-la avec le bouton de la TV. Après avoir connecté votre téléphone et activé l'allumage par le réseau dans les paramètres de la TV, vous pourrez l'allumer depuis l'application."),
      ('Dois-je acheter une nouvelle télécommande ?', "Pas forcément. Avec Mando TV, vous avez gratuitement les touches, le volume, le clavier et l'allumage. Si vous préférez quand même une télécommande physique, cherchez le modèle exact de votre TV."),
      ("Cela fonctionne-t-il si la TV n'a pas de Wi-Fi ?", "Non. Le téléphone et la TV doivent être sur le même réseau Wi-Fi. Une TV qui n'est pas une Smart TV ne peut pas être pilotée avec Mando TV."),
    ]),
  dict(clave='lost-lg', corto='Télécommande LG perdue',
    titulo='Télécommande LG perdue ? Utilisez votre téléphone',
    desc="Plus de télécommande LG ? Allumez la TV avec son bouton, acceptez le message et utilisez votre téléphone comme télécommande Wi-Fi. Sans compte LG.",
    h1='Télécommande LG perdue ? Comment utiliser votre téléphone',
    intro="Si vous avez perdu la télécommande de votre TV LG ou si la Magic Remote ne fonctionne plus, votre téléphone la remplace en Wi-Fi. Cela fonctionne sur les TV LG sous webOS, c'est-à-dire presque toutes les Smart TV LG depuis 2014. Il ne faut ni compte LG ni l'application ThinQ.",
    pasos=[
      "Allumez la TV avec le bouton du bas, sous le logo LG, ou celui de l'arrière. Sur beaucoup de modèles, il fait office de joystick : appuyez pour ouvrir le menu et déplacez-le pour choisir.",
      'Connectez votre téléphone au même réseau Wi-Fi que la TV.',
      'Ouvrez Mando TV et touchez votre TV LG dans la liste.',
      "La TV affiche un message qui demande l'autorisation. Acceptez-le avec le joystick ou le bouton de la TV. Si vous avez déjà connecté ce téléphone, elle ne le redemande pas.",
      "Et voilà. Les flèches, OK, Retour, Accueil, le volume, les chaînes et le clavier sont gratuits. Le pointeur est une fonction Pro.",
      "Une fois l'application connectée, entrez dans les Paramètres avec les flèches et OK, et activez « Téléviseur en marche avec mobile ». Le guide [Allumer une TV LG avec le téléphone](@lg-on) montre où le trouver.",
    ],
    extra=[
      ("Si la TV n'affiche pas le message", "L'autorisation est peut-être déjà enregistrée, ou votre téléphone est sur un autre réseau. Vérifiez que les deux sont sur le même réseau Wi-Fi et que le VPN est désactivé. Si la TV n'apparaît pas dans la liste, lisez [Votre téléphone ne trouve pas la TV](@not-found)."),
      ('Si la TV a perdu son Wi-Fi', "Branchez la TV à la box avec un câble réseau et elle l'utilisera toute seule. Ou créez un réseau Wi-Fi avec le même nom et le même mot de passe qu'avant, car la TV s'y reconnecte généralement toute seule."),
      ("Si la TV est bloquée sur une autre entrée", "Sur votre téléphone, touchez Sources et choisissez l'entrée HDMI. Plus de détails dans [Changer d'entrée HDMI sur une TV sans télécommande](@hdmi)."),
    ],
    marca='lg',
    faq=[
      ('Ai-je besoin de la Magic Remote pour utiliser Mando TV ?', "Il vous faut seulement de quoi accepter le message la première fois, et le bouton ou le joystick de la TV elle-même suffit. Ensuite, vous n'utilisez que votre téléphone."),
      ("Ai-je besoin de l'application LG ThinQ ?", "Non. Mando TV se connecte directement par votre Wi-Fi et ne demande pas de compte LG."),
      ('Puis-je éteindre et allumer ma TV LG depuis mon téléphone ?', "L'éteindre, oui. Pour l'allumer, il faut avoir activé « Téléviseur en marche avec mobile » sur la TV et s'être connecté une fois pendant que la TV était allumée."),
    ]),
  dict(clave='hdmi', corto='HDMI sans télécommande',
    titulo="Changer d'entrée HDMI sans télécommande (Samsung, LG, Roku)",
    desc="Changer d'entrée HDMI sans télécommande sur Samsung, LG ou Roku : avec le bouton de la TV ou votre téléphone. Gratuit pour commencer, sans pub.",
    h1="Comment changer d'entrée HDMI sur une TV sans télécommande",
    intro="La console ou le lecteur de streaming est prêt, mais la TV est restée sur une autre entrée et la télécommande est introuvable. Pour changer d'entrée HDMI sans télécommande, vous avez deux options : le bouton de la TV elle-même ou votre téléphone. Voici les étapes pour Samsung, LG et Roku.",
    pasos=[
      "Essayez d'abord le plus simple : allumez la console ou le lecteur. Si le HDMI-CEC est activé sur la TV (Anynet+ chez Samsung, SIMPLINK chez LG), elle passe toute seule sur cette entrée.",
      "Si elle ne change pas, utilisez le bouton de la TV elle-même, en bas au centre ou à l'arrière. Sur beaucoup de TV Samsung et LG, il fait office de joystick et ouvre un menu avec Source ou Entrées.",
      "Choisissez l'entrée dans ce menu : HDMI 1, HDMI 2, et ainsi de suite. Le numéro est celui de la prise où le câble est branché.",
      "Si vous préférez votre téléphone, connectez-le au même réseau Wi-Fi, ouvrez Mando TV et touchez votre TV.",
      "Sur LG et Roku, touchez Sources et choisissez l'entrée HDMI. Sur Samsung, Sources envoie à la TV la touche Source et vous choisissez avec les flèches et OK.",
      "Vous pouvez aussi utiliser les flèches et OK pour aller aux entrées depuis l'écran d'accueil de la TV. Selon la marque et l'année, elles s'appellent Source, Appareils connectés ou Entrées. Sur un Roku TV, ce sont les tuiles HDMI de l'écran d'accueil.",
    ],
    extra=[
      ('Samsung', "Si le menu du bouton de la TV n'a pas de Source, ouvrez avec votre téléphone le menu de l'écran d'accueil et cherchez Source ou Appareils connectés à gauche. Vous le pilotez avec les flèches et OK dans Mando TV, qui sont gratuits."),
      ('LG', "Appuyez sur le joystick de la TV et cherchez Entrées. Avec votre téléphone, dans Mando TV, vous pouvez aussi ouvrir la liste des sources et toucher celle que vous voulez."),
      ('Roku TV', "Sur l'écran d'accueil, il y a une tuile par entrée, comme HDMI 1 ou HDMI 2. Déplacez-vous avec les flèches et entrez avec OK, gratuitement."),
      ("Si c'est une TV sous Android TV ou Google TV", "Dans Mando TV, la liste des sources n'existe pas encore pour Android TV. Utilisez le bouton des entrées de la TV elle-même, ou atteignez-les avec les flèches et OK depuis l'écran d'accueil. Si vous n'avez pas de télécommande et voulez vous connecter, lisez [Android TV sans télécommande](@androidtv)."),
      ("Plus d'aide", "Si la TV ne s'allume même pas ou si vous ne savez pas par où commencer, lisez [Télécommande de TV perdue](@lost-tv). Pour jouer sur console, le guide [Allumer la TV et passer au HDMI de la console sans télécommande](@console) contient l'astuce du HDMI-CEC."),
    ],
    marca=None,
    faq=[
      ("Changer d'entrée HDMI est-il gratuit ?", "Oui. La liste des sources de Mando TV est gratuite, comme l'allumage de la TV, les flèches, OK et le volume. Vous pouvez aussi atteindre les entrées depuis le menu de la TV."),
      ("Comment savoir quelle entrée HDMI utiliser ?", "Regardez les prises HDMI de la TV : chacune a un numéro. Utilisez celle où est branché le câble de votre console ou de votre lecteur."),
      ("Et si la TV ne s'allume pas ?", "Allumez-la avec son bouton physique. Si vous l'avez déjà connectée et activé l'allumage par le réseau, vous pouvez aussi l'allumer depuis votre téléphone."),
    ]),
  dict(clave='androidtv', corto='Android TV sans télécommande',
    titulo='Android TV sans télécommande : utilisez le téléphone',
    desc="Plus de télécommande Android TV ou Google TV ? Connectez votre téléphone avec le code à 6 caractères affiché à l'écran. Gratuit, sans compte, sans pub.",
    h1='Android TV sans télécommande : comment utiliser votre téléphone',
    intro="Si vous avez perdu la télécommande de votre Android TV ou Google TV, ou si ses piles sont vides, votre téléphone la remplace. Le plus beau, c'est que la connexion n'a pas besoin de la télécommande : la TV affiche un code à l'écran et vous le saisissez sur votre téléphone. Cela fonctionne sur les TV Sony, Philips, TCL, Hisense, Sharp et Xiaomi sous Android TV, sur Chromecast avec Google TV et sur Nvidia Shield.",
    pasos=[
      "Allumez la TV avec son bouton physique. Il se trouve presque toujours en bas au centre, ou à l'arrière près d'un coin.",
      'Connectez votre téléphone au même réseau Wi-Fi que la TV.',
      "Téléchargez Mando TV, qui est gratuite et ne demande pas de compte Google, puis ouvrez-la. Touchez votre TV dans la liste.",
      "La TV affiche un code de 6 lettres et chiffres. Saisissez-le sur votre téléphone et touchez Associer. Vous n'avez pas besoin de la télécommande pour cela.",
      "Vous pouvez maintenant utiliser les flèches, OK, Retour, Accueil, le volume, le muet et le clavier. Ils sont gratuits, tout comme la liste des applications. Le pavé tactile est Pro.",
      "Pour l'allumer depuis votre téléphone la prochaine fois, cherchez « Wake on LAN », « Allumer par le réseau » ou « Activation par le réseau » dans les paramètres réseau ou d'alimentation de la TV.",
    ],
    extra=[
      ("Si votre TV ne s'allume pas depuis le téléphone", "Toutes les Android TV ne peuvent pas s'allumer par le réseau ; cela dépend du fabricant et du modèle. Si la vôtre n'a pas cette option, allumez-la avec le bouton de la TV et continuez depuis votre téléphone. Vous pouvez l'éteindre depuis l'application."),
      ('Chromecast avec Google TV, Google TV Streamer et Shield', "Ils se connectent de la même façon : même réseau Wi-Fi, touchez l'appareil dans la liste et saisissez le code. Si la TV affiche une autre entrée, passez sur l'entrée HDMI où l'appareil est branché, comme l'explique [Changer d'entrée HDMI sur une TV sans télécommande](@hdmi)."),
      ("Si le code n'apparaît pas ou s'il est refusé", "Vérifiez que la TV est vraiment allumée et pas en veille. Le code change à chaque demande : seul le dernier fonctionne. Vous trouverez plus de détails dans [Android TV demande un code d'appairage](@androidtv-code)."),
      ("Application Google ou Mando TV", "Google a sa propre application, qui demande un compte Google. Mando TV ne demande pas de compte, fonctionne aussi depuis Windows et pilote les TV LG, Samsung et Roku depuis la même application."),
    ],
    marca='android',
    faq=[
      ("Ai-je besoin de la télécommande pour associer mon téléphone ?", "Non. Le code apparaît sur l'écran de la TV et vous le saisissez sur votre téléphone. Il suffit d'allumer la TV, si besoin avec le bouton de la TV."),
      ('Cela fonctionne-t-il avec une Hisense ?', "Sur les TV Hisense qui ont Android TV ou Google TV, oui. Les TV Hisense avec un autre système ne sont pas compatibles."),
      ("Puis-je écrire avec le clavier de mon téléphone ?", "Oui. Le clavier est gratuit et fonctionne pour chercher dans YouTube, Netflix et les autres applications."),
    ]),
  dict(clave='lg-on', corto='Allumer une TV LG avec le téléphone',
    titulo='Allumer une TV LG avec son téléphone (pas à pas)',
    desc="Allumez votre TV LG avec votre téléphone en Wi-Fi : activez « Téléviseur en marche avec mobile » puis utilisez Mando TV. Gratuit, sans pub.",
    h1='Comment allumer une TV LG avec votre téléphone',
    intro="Vous pouvez allumer une TV LG avec votre téléphone, mais il faut d'abord activer un réglage sur la TV. Une fois cela fait, votre téléphone allume la TV LG via votre réseau Wi-Fi, sans télécommande. Cela prend cinq minutes et vous ne le faites qu'une fois.",
    pasos=[
      'Connectez votre téléphone et la TV LG au même réseau Wi-Fi.',
      "Sur la TV, ouvrez les Paramètres et cherchez « Téléviseur en marche avec mobile ». Il se trouve dans Tous les paramètres > Général > Appareils > Appareils externes.",
      "Activez « Allumer via Wi-Fi ». Si votre TV est connectée par un câble réseau, activez plutôt l'option du câble.",
      'Si votre TV a « Démarrage rapide+ », activez-le aussi.',
      "TV allumée, ouvrez Mando TV sur votre téléphone et touchez votre TV LG dans la liste. Acceptez le message qui apparaît à l'écran. C'est ainsi que l'application apprend à la réveiller.",
      "Éteignez la TV et testez : touchez la TV dans Mando TV et l'application vous demande si vous voulez l'allumer.",
    ],
    extra=[
      ("Si elle ne s'allume pas", "La TV devait être sur le même réseau Wi-Fi quand elle a été éteinte. Vérifiez que le réglage est toujours activé et que votre téléphone est sur ce même réseau. Si vous avez changé de box, connectez-vous une fois de plus avec la TV allumée."),
    ],
    marca='lg',
    faq=[
      ("Puis-je allumer la TV LG avec mon téléphone si je ne l'ai jamais connectée ?", "Non. Il faut d'abord activer « Téléviseur en marche avec mobile » sur la TV et vous connecter une fois avec Mando TV pendant que la TV est allumée."),
      ("Ai-je besoin de l'application LG ThinQ ?", "Non. Mando TV se connecte directement par votre Wi-Fi et ne demande pas de compte LG."),
      ('Cela fonctionne-t-il avec les données mobiles ?', 'Non. Le téléphone et la TV doivent être sur le même réseau Wi-Fi.'),
    ]),
  dict(clave='console', corto='TV et console sans télécommande',
    titulo='Sans télécommande ? Allumer la TV et passer au HDMI',
    desc="Jour de sortie et plus de télécommande ? Allumez la TV et passez à l'entrée HDMI de votre PS5 ou Xbox depuis le téléphone. Gratuit, sans pub.",
    h1="Comment allumer la TV et passer au HDMI de la console sans télécommande",
    intro="Jour de sortie de GTA VI, la console est prête et la télécommande de la TV a disparu entre les coussins du canapé. Cela arrive plus souvent qu'on ne le croit. Avec Mando TV, votre téléphone allume la TV et la passe sur l'entrée de votre PlayStation ou Xbox, via le Wi-Fi de la maison.",
    pasos=[
      'Connectez votre téléphone au même réseau Wi-Fi que la TV.',
      'Ouvrez Mando TV et touchez votre TV dans la liste (Samsung, LG, Roku ou Android TV).',
      "Si la TV est éteinte, touchez Allumer. Cela fonctionne si l'allumage par le réseau est activé sur la TV. Si vous ne l'avez jamais activé, allumez la TV cette fois avec le bouton de la TV elle-même et activez-le pour la prochaine fois.",
      "Allumez la console. Si le HDMI-CEC est activé (voir l'astuce gratuite plus bas), la TV passe toute seule sur son entrée.",
      "Si elle ne change pas, touchez Sources dans Mando TV et choisissez l'entrée HDMI où la console est branchée : HDMI 1, HDMI 2, et ainsi de suite.",
      "Pour le volume, utilisez les grosses touches de l'application pendant que vous jouez.",
    ],
    extra=[
      ("L'astuce gratuite : laissez la console changer la TV pour vous", "La PS5 et la Xbox peuvent allumer la TV et passer sur leur entrée HDMI dès qu'elles démarrent, grâce au HDMI-CEC. Sur la PS5, c'est dans Paramètres > Système > HDMI > Activer la liaison avec les appareils HDMI. Sur la Xbox, ouvrez Paramètres > Général > Options TV et affichage et cherchez l'option de contrôle des appareils. Sur la TV, la fonction porte un nom différent selon la marque : Anynet+ chez Samsung, SIMPLINK chez LG, et BRAVIA Sync ou contrôle HDMI chez d'autres."),
      ("Si la TV reste sur un autre écran", "Si la console est allumée mais que la TV affiche encore l'antenne ou une application, elle n'a pas changé d'entrée. Depuis votre téléphone, touchez Sources et choisissez le HDMI de la console. Vous pouvez aussi utiliser les flèches et OK pour atteindre les entrées de la TV, ou le bouton de la TV elle-même, et choisissez l'entrée HDMI. Le numéro est celui de la prise où vous avez branché le câble de la console."),
      ("Si c'est un Roku TV", "Le bouton physique de la TV, généralement en bas au centre ou à l'arrière, l'allume. À partir de là, votre téléphone fait le reste."),
    ],
    marca=None,
    faq=[
      ('Mando TV a-t-elle un rapport avec GTA VI ?', "Non. Mando TV n'est affiliée ni à Rockstar Games ni à Take-Two. Elle vous aide seulement à ne pas perdre de temps de jeu parce que vous ne trouvez pas la télécommande de la TV."),
      ("Changer d'entrée HDMI est-il gratuit ?", "Oui. La liste des sources de Mando TV est gratuite, comme l'allumage de la TV, les flèches, OK et le volume. Vous pouvez aussi laisser la console changer d'entrée toute seule avec le HDMI-CEC."),
      ('Cela fonctionnera-t-il avec ma TV ?', "Cela fonctionne avec les TV Samsung, LG, Roku et Android TV sur le même réseau Wi-Fi. Si la vôtre est d'une autre marque, l'astuce du HDMI-CEC peut quand même aider."),
      ('Puis-je l\'utiliser pour jouer à GTA VI (GTA 6) sur PS5 ou Xbox ?', "Mando TV ne touche ni à la console ni au jeu. Elle veille seulement à ce que la TV soit allumée et sur la bonne entrée HDMI pour que vous puissiez vous asseoir et jouer."),
    ]),
  dict(clave='samsung-lost', corto='TV Samsung sans télécommande',
    titulo='Télécommande Samsung perdue ? Utilisez le téléphone',
    desc="Télécommande Samsung perdue ou en panne ? Utilisez votre téléphone comme télécommande Wi-Fi sur TV Tizen. Simple avec Mando TV, gratuit, sans pub.",
    h1="TV Samsung sans la télécommande d'origine : utilisez votre téléphone",
    intro="Si vous avez perdu la télécommande de votre TV Samsung ou si elle ne fonctionne plus, vous pouvez utiliser votre téléphone comme télécommande via le Wi-Fi. Cela fonctionne sur les TV Samsung sous Tizen, modèles 2016 et plus récents.",
    pasos=[
      "Allumez la TV avec son bouton physique. Sur la plupart des modèles, il se trouve en bas ou à l'arrière, parfois sous forme de petit joystick.",
      'Vérifiez que la TV est connectée à votre Wi-Fi et que votre téléphone est sur le même réseau.',
      'Ouvrez Mando TV sur votre téléphone. Votre TV Samsung apparaît toute seule dans la liste. Touchez-la.',
      "La TV vous demande d'accepter la connexion. Sur la plupart des modèles, vous l'acceptez avec les boutons physiques de la TV ou avec le joystick de l'arrière.",
      "Et voilà, vous pouvez maintenant utiliser votre téléphone comme télécommande. Les touches, le clavier et les applications sont gratuits ; le pavé tactile est une fonction Pro.",
      "Pour l'allumer depuis votre téléphone la prochaine fois, allez dans Paramètres > Général > Réseau > Paramètres d'expert et activez « Allumer avec un appareil mobile ».",
    ],
    extra=[
      ("Si la TV ne demande pas l'autorisation", "L'autorisation est peut-être déjà enregistrée, ou la TV est sur un autre réseau Wi-Fi. Fermez Mando TV et rouvrez-la avec la TV allumée. Si la TV date d'avant 2016, elle utilise un autre système qui n'est pas encore pris en charge."),
      ("Si vous avez refusé l'autorisation par erreur", "Sur la TV, allez dans Paramètres > Général > Gestionnaire de périphériques externes > Gestionnaire de connexion de périphérique, et réglez Mando TV sur autorisé. Si votre téléphone ne trouve toujours pas la TV, lisez [Votre téléphone ne trouve pas la TV](@not-found)."),
    ],
    marca='samsung',
    faq=[
      ("Comment accepter la connexion si je n'ai pas de télécommande ?", "Sur la plupart des modèles, vous l'acceptez avec les boutons physiques de la TV ou avec le joystick de l'arrière. Si votre modèle n'a pas de boutons, écrivez à hola@mandotv.app et nous vous aiderons."),
      ('Mando TV demande-t-elle un compte Samsung ?', 'Non. Elle se connecte directement par votre Wi-Fi, sans compte Samsung.'),
      ('Fonctionne-t-elle avec ma TV Samsung plus ancienne ?', 'Elle fonctionne avec les TV Samsung sous Tizen, modèles 2016 et plus récents.'),
    ]),
  dict(clave='wifi', corto='Téléphone comme télécommande en Wi-Fi',
    titulo='Téléphone comme télécommande de TV en Wi-Fi',
    desc="Connectez votre téléphone à la TV en Wi-Fi et utilisez-le comme télécommande Samsung, LG, Roku et Google TV. Étapes par marque avec Mando TV. Gratuit.",
    h1='Comment connecter votre téléphone à la TV en Wi-Fi comme télécommande',
    intro="Il suffit de votre téléphone et de votre TV sur le même réseau Wi-Fi, plus une application de télécommande. Mando TV trouve votre TV toute seule et fonctionne avec Samsung, LG, Roku, Google TV et Android TV.",
    pasos=[
      'Connectez le téléphone et la TV au même réseau Wi-Fi.',
      'Ouvrez Mando TV. Votre TV apparaît toute seule dans la liste. Touchez-la.',
      'Acceptez la connexion pour votre marque (les détails de chacune sont plus bas).',
      'Pilotez la TV avec les touches ou le clavier de votre téléphone. Le pavé tactile est une fonction Pro.',
    ],
    extra=[
      ('Samsung', "La TV demande si vous autorisez la connexion. Acceptez-la à l'écran la première fois. Cela fonctionne avec Tizen, modèles 2016 et plus récents. Pour l'allumer depuis votre téléphone, activez « Allumer avec un appareil mobile » dans Paramètres > Général > Réseau > Paramètres d'expert."),
      ('LG', "La TV affiche un message qui demande l'autorisation. Acceptez-le la première fois. Pour l'allumer depuis votre téléphone, cherchez « Téléviseur en marche avec mobile » dans les Paramètres et activez « Allumer via Wi-Fi »."),
      ('Roku', "Roku ne demande pas d'association : touchez-le dans la liste et vous êtes connecté. Pour l'allumer, activez « Démarrage rapide de la TV » dans Paramètres > Système > Alimentation."),
      ('Google TV et Android TV', "La TV affiche un code à l'écran. Saisissez-le dans Mando TV la première fois. Pour l'allumer, cherchez « Wake on LAN », « Allumer par le réseau » ou « Activation par le réseau » dans les paramètres."),
    ],
    marca=None,
    faq=[
      ("Ai-je besoin d'Internet pour utiliser mon téléphone comme télécommande ?", "Il faut votre téléphone et la TV sur le même réseau Wi-Fi. Mando TV se connecte directement à votre TV par ce réseau."),
      ("Pourquoi ma TV n'apparaît-elle pas dans la liste ?", "Vérifiez que la TV est allumée et que votre téléphone n'utilise ni les données mobiles ni un autre réseau Wi-Fi. Certaines box ont un réseau invité qui isole les appareils."),
      ('Puis-je utiliser Mando TV depuis un iPhone ou un téléphone Android ?', "Oui sur iPhone et iPad : l'application est déjà sur l'App Store. Elle est aussi sur le Microsoft Store pour Windows. Android arrive bientôt : vous pouvez rejoindre l'accès anticipé gratuit sur Google Play."),
    ]),
  dict(clave='pc', corto='Contrôler la TV depuis un PC',
    titulo='Contrôler sa TV depuis un PC Windows (gratuit)',
    desc="Utilisez votre PC Windows comme télécommande de TV Samsung, LG, Roku ou Google TV en Wi-Fi. Touches, clavier et apps gratuits ; raccourcis avec Pro.",
    h1='Comment contrôler votre TV depuis un PC Windows',
    intro="Si vous passez la journée devant votre ordinateur, inutile de chercher la télécommande : Mando TV pour Windows pilote votre TV Samsung, LG, Roku, Google TV ou Android TV via le Wi-Fi de la maison. Pratique pour changer d'application, monter le volume ou écrire dans YouTube avec le clavier du PC.",
    pasos=[
      "Téléchargez Mando TV gratuitement depuis le Microsoft Store sur votre ordinateur sous Windows 10 ou 11.",
      "Vérifiez que l'ordinateur et la TV sont sur le même réseau (Wi-Fi ou câble, mais via la même box).",
      'Ouvrez Mando TV : votre TV apparaît toute seule dans la liste. Touchez-la ou cliquez dessus.',
      "Acceptez la connexion sur l'écran de la TV la première fois (sur Google TV et Android TV, saisissez le code affiché par la TV).",
      "Et voilà : utilisez les touches ou le clavier pour écrire dans le champ de recherche de la TV. Le pavé tactile est une fonction Pro.",
    ],
    extra=[
      ('Raccourcis clavier du PC (Pro)', "Avec Mando TV Pro, vous pilotez la TV avec le clavier de l'ordinateur : les flèches pour se déplacer, Entrée pour OK, Retour arrière ou Échap pour revenir, + et - pour le volume, M pour le muet et Espace pour la pause."),
      ('Mini télécommande toujours au premier plan (Pro)', "Gardez une petite fenêtre avec la télécommande toujours visible pendant que vous travaillez ou jouez sur votre PC."),
      ('Parler à la TV depuis le PC (Pro)', "Avec Mando TV Pro, vous donnez des ordres à la TV avec le micro du PC : « ouvre YouTube », « monte le son » ou « éteins dans 30 minutes », à votre façon. Sous Windows, l'app utilise la saisie vocale de Windows, qui a besoin de la « Reconnaissance vocale en ligne » activée dans les paramètres de confidentialité et de la langue ajoutée dans Windows (français de France ou du Canada). S'il manque quelque chose, l'app vous prévient et ouvre le réglage avec un bouton."),
    ],
    marca=None,
    faq=[
      ("Faut-il un câble ou le Bluetooth pour contrôler la TV depuis mon PC ?", "Non. Mando TV se connecte via votre réseau domestique : le PC et la TV doivent seulement être sur la même box."),
      ('Cela fonctionne-t-il avec toutes les TV ?', "Cela fonctionne avec les TV Samsung sous Tizen (2016 et plus récentes), LG sous webOS, Roku, et Google TV ou Android TV (Sony, Philips, TCL, Hisense, Sharp, Xiaomi, Toshiba, Panasonic, Haier, Skyworth et autres)."),
      ('Combien cela coûte-t-il ?', "Les touches, le clavier et l'allumage par le réseau sont gratuits et sans publicité. Mando TV Pro est un achat unique, sans abonnement, pour des extras comme le pavé tactile, les raccourcis clavier du PC et la mini télécommande."),
      ('Pourquoi le micro ne me comprend pas sous Windows ?', "Vérifiez deux choses : la « Reconnaissance vocale en ligne » est activée dans les paramètres de confidentialité de Windows, et Windows a le français (France) ou (Canada) dans les paramètres de langue. Mando TV utilise cette langue seulement pendant l'écoute."),
    ]),
  dict(clave='roku-403', corto="L'application Roku ne fonctionne pas",
    titulo="L'appli Roku ne fonctionne pas ? Corriger l'erreur 403",
    desc="Votre téléphone se connecte au Roku mais les touches ne font rien ? Activez « Contrôle par applications mobiles » sur le Roku en 5 étapes.",
    h1="L'application Roku ne fonctionne pas : comment la réparer",
    intro="Si votre téléphone trouve le Roku et se connecte, mais qu'aucune touche ne fait rien, c'est presque toujours un réglage du Roku lui-même qui bloque les applications de télécommande. Les versions récentes de Roku sont plus restrictives par défaut. Cela se corrige en une minute depuis le menu du Roku.",
    pasos=[
      'Sur le Roku, appuyez sur Accueil et allez dans Paramètres.',
      'Ouvrez Système puis Paramètres système avancés.',
      "Entrez dans « Contrôle par applications mobiles ». Sur certains modèles, il s'appelle « Contrôle externe ».",
      "Sous « Accès au réseau », choisissez Par défaut ou Permissif. Si sur votre modèle c'est seulement un interrupteur, laissez-le sur Activé.",
      'Revenez à Mando TV sur votre téléphone et touchez votre Roku. Les touches répondent maintenant.',
    ],
    extra=[
      ("Comment savoir si c'est votre problème", "Le signe est net : votre téléphone voit le Roku dans la liste et se connecte, mais rien ne se passe quand vous touchez une touche. En interne, le Roku répond par l'erreur 403, qui veut dire « interdit ». Mando TV le détecte à la connexion et vous montre ces mêmes étapes à l'écran."),
      ('Par défaut ou Permissif, lequel choisir ?', "Par défaut suffit : il accepte les commandes qui viennent de votre réseau domestique, ce dont une télécommande a besoin. Permissif est plus ouvert et n'est nécessaire que sur des réseaux inhabituels."),
      ("Si vous n'avez pas la télécommande du Roku", "Quand le réglage est sur Désactivé, il ne peut être changé qu'avec la télécommande physique du Roku. Empruntez-en une pour le changer une fois ; ensuite, vous pouvez tout faire avec votre téléphone. Lisez aussi [Télécommande Roku perdue](@roku-lost)."),
    ],
    marca='roku',
    faq=[
      ("Pourquoi mon Roku ne répond-il plus alors qu'il fonctionnait avant ?", "Une mise à jour du Roku peut rendre ce réglage plus restrictif. Ce n'est pas un problème de votre téléphone ni de votre Wi-Fi : il suffit d'autoriser de nouveau le contrôle par applications."),
      ('Cela concerne-t-il Roku TV et les lecteurs Roku ?', 'Oui. Le réglage est dans le même menu sur les lecteurs Roku et sur les téléviseurs Roku TV.'),
      ('Peut-on le laisser sur Par défaut sans risque ?', "Oui. Il n'accepte que les commandes des appareils de votre réseau domestique."),
    ]),
  dict(clave='not-found', corto='Le téléphone ne trouve pas la TV',
    titulo='Le téléphone ne trouve pas la TV ? 6 points à vérifier',
    desc="L'appli de télécommande ne trouve pas votre TV ou se déconnecte ? Vérifiez le Wi-Fi, le VPN et l'accès au réseau local. Samsung, LG, Roku, Android TV.",
    h1='Votre téléphone ne trouve pas la TV : que vérifier',
    intro="Vous ouvrez l'application de télécommande et la liste est vide, ou la TV apparaît mais la connexion se coupe. C'est presque toujours le réseau, pas la TV. Vérifiez ces points dans l'ordre : le premier règle la plupart des cas.",
    pasos=[
      "Regardez sur quel Wi-Fi est votre téléphone et sur lequel est la TV. Ce doit être le même réseau, avec le même nom. Un réseau invité ne fonctionnera pas, car il isole les appareils.",
      "Désactivez le VPN de votre téléphone, si vous en utilisez un. Avec le VPN activé, votre téléphone sort par un autre réseau et ne voit pas les appareils de chez vous, ou la connexion se coupe au bout de quelques secondes.",
      "Désactivez un instant les données mobiles. Certains téléphones passent tout seuls du Wi-Fi aux données mobiles quand le signal est faible.",
      "Allumez la TV et attendez qu'elle ait fini de démarrer. Une TV éteinte ne répond pas à la recherche.",
      "Sur un iPhone, vérifiez que l'application a l'autorisation Réseau local : Réglages > Confidentialité et sécurité > Réseau local.",
      "Si elle n'apparaît toujours pas, ajoutez-la à la main : dans Mando TV, touchez « Ajouter par IP » et saisissez l'adresse IP de la TV.",
    ],
    extra=[
      ("Où trouver l'adresse IP de la TV", "Elle se trouve dans le menu réseau de la TV et varie un peu selon le modèle. Sur LG : Paramètres, Réseau, Connexion Wi-Fi, Paramètres Wi-Fi avancés. Sur Samsung : Paramètres, Général, Réseau, État du réseau, Paramètres IP. Sur Roku : Paramètres, Réseau, À propos. Sur Android TV et Google TV : Paramètres, Réseau et Internet, puis touchez votre réseau. C'est un nombre comme 192.168.1.86."),
      ("Si elle apparaît mais que la connexion se coupe", "Quand la connexion se coupe au bout de quelques secondes, la cause se trouve généralement sur le téléphone : un VPN, un passage à un autre réseau Wi-Fi ou l'économiseur de batterie. Désactivez le VPN, restez sur le même Wi-Fi et réessayez."),
      ('Wi-Fi 2,4 et 5 GHz', "Peu importe que votre téléphone soit sur le réseau 5 GHz et la TV sur le 2,4 GHz, tant que les deux viennent de la même box. Si vous avez un répéteur Wi-Fi et que la TV n'apparaît toujours pas, rapprochez votre téléphone de la box principale et réessayez."),
    ],
    marca=None,
    faq=[
      ('Puis-je piloter la TV avec les données mobiles ?', "Non. Le signal de la télécommande passe par votre Wi-Fi domestique, donc votre téléphone et la TV doivent être sur le même réseau."),
      ('Pourquoi cela ne fonctionne-t-il pas avec le VPN activé ?', "Parce que le VPN envoie tout le trafic de votre téléphone par un autre réseau et que le téléphone ne voit plus les appareils de chez vous. Désactivez-le pendant que vous utilisez la télécommande."),
      ("Le Bluetooth ou l'infrarouge fonctionnent-ils ?", "Mando TV utilise uniquement le Wi-Fi. Elle n'a pas besoin du Bluetooth ni d'un émetteur infrarouge sur votre téléphone."),
    ]),
  dict(clave='androidtv-code', corto="Code d'appairage Android TV",
    titulo="Android TV demande un code d'appairage : que faire",
    desc="Votre Android TV ou Google TV affiche un code à 6 caractères à la connexion du téléphone. Comment le saisir et que faire s'il manque ou est refusé.",
    h1="Android TV demande un code d'appairage : que faire",
    intro="La première fois que vous connectez votre téléphone à une Android TV ou Google TV, la TV affiche un code de 6 caractères à l'écran. C'est normal et cela n'arrive qu'une fois : cela garantit que personne d'autre ne peut piloter votre TV. Voici comment le saisir et que faire s'il n'apparaît pas.",
    pasos=[
      "Allumez la TV et laissez l'écran d'accueil visible.",
      'Ouvrez Mando TV sur votre téléphone, sur le même Wi-Fi que la TV, et touchez votre TV dans la liste.',
      "Regardez l'écran de la TV : un code de 6 lettres et chiffres apparaît.",
      "Saisissez-le sur votre téléphone exactement comme il s'affiche et touchez Associer. Les lettres vont seulement de A à F : un caractère rond est donc toujours le chiffre zéro.",
      'Et voilà. La TV mémorise votre téléphone et ne redemande pas le code.',
    ],
    extra=[
      ("Si le code n'apparaît pas sur la TV", "Vérifiez que la TV est vraiment allumée et pas en veille, et que votre téléphone est sur le même Wi-Fi. Touchez de nouveau la TV sur votre téléphone. S'il n'apparaît toujours pas, redémarrez la TV : débranchez-la dix secondes, rebranchez-la et réessayez."),
      ("S'il indique que le code est faux", "Le code change à chaque demande. Si vous avez mis du temps ou l'avez demandé deux fois, seul le dernier affiché à l'écran fonctionne. Touchez de nouveau la TV sur votre téléphone et saisissez le nouveau code."),
      ("Si la TV redemande le code", "Cela arrive quand la TV est réinitialisée aux paramètres d'usine ou quand vous effacez les données de l'application sur votre téléphone. Associez de nouveau et c'est enregistré. Si vous n'avez aucune télécommande, lisez [Android TV sans télécommande](@androidtv)."),
    ],
    marca='android',
    faq=[
      ('Quelles TV utilisent ce code ?', "Celles sous Android TV ou Google TV : Sony, Philips, TCL, Hisense, Sharp, Xiaomi, Chromecast avec Google TV et plusieurs autres."),
      ("Ai-je besoin d'un compte Google sur mon téléphone ?", "Non. Le code affiché à l'écran suffit."),
      ('Est-ce sûr ?', "Oui. Le code prouve que vous êtes devant la TV : personne ne peut associer un appareil sans le voir à l'écran."),
    ]),
  dict(clave='roku-lost', corto='Télécommande Roku perdue',
    titulo='Télécommande Roku perdue ? Utilisez le téléphone en Wi-Fi',
    desc="Télécommande Roku perdue ? Votre téléphone la remplace en Wi-Fi. Étapes simples, même si vous avez changé de box et que le Roku n'a plus de Wi-Fi.",
    h1='Télécommande Roku perdue : comment utiliser votre téléphone',
    intro="Si vous avez perdu la télécommande de votre Roku ou si elle ne fonctionne plus, votre téléphone la remplace, tant que le Roku est encore connecté à votre Wi-Fi. Et si vous avez changé de Wi-Fi ou de box, il existe aussi une solution.",
    pasos=[
      "Allumez la TV et laissez le Roku branché. Vous n'avez rien à toucher dessus.",
      'Connectez votre téléphone au même Wi-Fi que celui du Roku.',
      'Ouvrez Mando TV. Le Roku apparaît tout seul dans la liste. Touchez-le.',
      "Utilisez les flèches, OK, Accueil et Retour comme sur votre télécommande habituelle. Le Roku ne demande aucun code.",
      "Si les touches ne font rien, le Roku bloque le contrôle par applications : le guide [L'application Roku ne fonctionne pas](@roku-403) explique comment l'autoriser.",
    ],
    extra=[
      ("Si le Roku n'a plus de Wi-Fi (changement de box ou déménagement)", "Sans télécommande, vous ne pouvez pas entrer dans le menu pour configurer le nouveau réseau, mais il y a une astuce : le Roku se connecte tout seul à un réseau qui a le même nom et le même mot de passe que l'ancien. Sur un autre téléphone, créez un point d'accès Wi-Fi avec exactement ce nom et ce mot de passe, connectez-y le téléphone qui a Mando TV et le Roku apparaîtra dans la liste. De là, allez dans Paramètres, Réseau et connectez-le au nouveau Wi-Fi."),
      ("Si c'est un Roku TV", "Les téléviseurs Roku TV ont un bouton physique, presque toujours en bas au centre ou à l'arrière, qui allume la TV. Cela suffit pour l'allumer et continuer avec votre téléphone."),
      ("Si vous préférez acheter une autre télécommande", "Assurez-vous qu'elle est compatible avec votre modèle. Les petits lecteurs Roku cachés derrière la TV ont besoin d'une télécommande qui n'est pas infrarouge, car l'infrarouge ne les atteint pas."),
    ],
    marca='roku',
    faq=[
      ('Mon téléphone peut-il allumer le Roku ?', "Un lecteur Roku branché est toujours allumé. Sur un Roku TV, Mando TV l'allume en Wi-Fi quand « Démarrage rapide de la TV » est activé dans Paramètres > Système > Alimentation."),
      ('Et le volume ?', "Sur un Roku TV, votre téléphone monte et baisse le volume. Sur un lecteur Roku connecté en HDMI, cela dépend de la TV : sur beaucoup cela fonctionne, sur d'autres non."),
      ('Dois-je créer un compte ?', "Non. Mando TV ne demande pas de compte et pilote aussi les TV Samsung, LG et Android TV depuis la même application."),
    ]),
]

SOPORTE = dict(
  titulo="Aide : connecter et allumer votre TV avec Mando TV",
  desc="Comment connecter la télécommande Mando TV à votre TV LG, Samsung, Roku ou Android TV, l'allumer depuis le téléphone et que faire en cas de problème.",
  h1='Aide',
  intro="Les questions les plus fréquentes, dans l'ordre des étapes. Si vous ne trouvez pas la vôtre, écrivez-nous à <a href=\"mailto:hola@mandotv.app?subject=Aide%20Mando%20TV\">hola@mandotv.app</a> et nous vous répondrons.",
)
SOPORTE_HTML = '''      <h2 id="encontrar">Trouver la TV</h2>
      <div class="preguntas">
        <details open><summary>Ma TV n'apparaît pas dans la liste</summary>
          <ol>
            <li>Vérifiez que votre téléphone et la TV sont sur le même réseau Wi-Fi. Si votre box a un réseau 2,4 GHz et un réseau 5 GHz avec des noms différents, ils ne se voient parfois pas.</li>
            <li>Assurez-vous que la TV est allumée.</li>
            <li>Sur un iPhone, vérifiez que Mando TV a l'autorisation « Réseau local » dans Réglages, Mando TV.</li>
            <li>Si elle n'apparaît toujours pas, touchez le bouton +, choisissez la marque et saisissez l'adresse IP de la TV. Vous la voyez dans le menu réseau de la TV (par exemple 192.168.1.50).</li>
          </ol>
        </details>
        <details><summary>Cela fonctionne-t-il avec les données mobiles ou hors de chez moi ?</summary>
          <p>Non. Mando TV communique avec la TV à l'intérieur de votre réseau domestique : votre téléphone doit donc être connecté à ce Wi-Fi.</p>
        </details>
      </div>

      <h2 id="conectar">Se connecter pour la première fois</h2>
      <p>Guides complets par marque : <a href="@@R_lg@@">LG</a>, <a href="@@R_samsung@@">Samsung</a>, <a href="@@R_roku@@">Roku</a> et <a href="@@R_android@@">Android TV</a>.</p>
      <div class="preguntas">
        <details><summary>LG</summary>
          <p>Quand vous touchez la TV, un message apparaît sur son écran pour demander l'autorisation. Acceptez-le avec votre télécommande habituelle. Vous ne le faites qu'une fois.</p>
        </details>
        <details><summary>Samsung</summary>
          <p>La TV demande si vous autorisez la connexion de Mando TV. Choisissez « Autoriser » avec la télécommande. Si vous avez refusé par erreur, allez dans Paramètres > Général > Gestionnaire de périphériques externes > Gestionnaire de connexion de périphérique et changez en autorisé.</p>
        </details>
        <details><summary>Roku</summary>
          <p>Roku ne demande pas d'autorisation. Si la connexion échoue, sur le Roku allez dans Paramètres > Système > Paramètres système avancés > Contrôle par applications mobiles et laissez l'accès au réseau sur Par défaut ou Permissif.</p>
        </details>
        <details><summary>Android TV et Google TV</summary>
          <p>La TV affiche un code de 6 caractères. Saisissez-le dans Mando TV exactement comme il apparaît. Cela fonctionne pour Sony, Philips, TCL, Hisense, Sharp, Xiaomi, Chromecast avec Google TV et d'autres sous Android TV.</p>
        </details>
      </div>

      <h2 id="encender">Allumer la TV depuis l'application</h2>
      <p>Mando TV allume la TV via votre réseau domestique. Il faut deux choses : vous êtes connecté au moins une fois avec la TV allumée, et l'allumage par le réseau est activé sur la TV. Le nom du réglage change selon le modèle ; voici les plus courants :</p>
      <div class="preguntas">
        <details><summary>LG</summary>
          <p>Cherchez « Téléviseur en marche avec mobile » dans les Paramètres (dans Tous les paramètres > Général > Appareils > Appareils externes) et activez « Allumer via Wi-Fi ». Si « Démarrage rapide+ » existe, activez-le aussi.</p>
        </details>
        <details><summary>Samsung</summary>
          <p>Activez « Allumer avec un appareil mobile » dans Paramètres > Général > Réseau > Paramètres d'expert.</p>
        </details>
        <details><summary>Roku</summary>
          <p>Sur les Roku TV, activez « Démarrage rapide de la TV » dans Paramètres > Système > Alimentation. Les lecteurs Roku branchés sur une TV ne peuvent pas être allumés ainsi.</p>
        </details>
        <details><summary>Android TV et Google TV</summary>
          <p>Cela dépend du fabricant. Cherchez « Wake on LAN », « Allumer par le réseau » ou « Activation par le réseau » dans les paramètres réseau ou d'alimentation. Certains modèles ne l'ont pas.</p>
        </details>
      </div>

      <h2 id="falla">En cas de problème</h2>
      <div class="preguntas">
        <details><summary>Elle se déconnecte ou ne répond pas</summary>
          <ol>
            <li>Sur l'écran de la télécommande, touchez Reconnecter.</li>
            <li>Si cela ne marche pas, fermez Mando TV et rouvrez-la.</li>
            <li>Si la TV a changé d'adresse IP, supprimez-la de la liste et ajoutez-la de nouveau.</li>
          </ol>
        </details>
        <details><summary>Comment nous envoyer un rapport d'erreur</summary>
          <ol>
            <li>Dans Mando TV, touchez le bouton Personnaliser (les curseurs en haut).</li>
            <li>Touchez Copier le rapport de test.</li>
            <li>Collez-le dans un e-mail à hola@mandotv.app avec la marque et le modèle de votre TV.</li>
          </ol>
          <p>Le rapport n'inclut ni mots de passe, ni codes, ni rien de ce que vous écrivez.</p>
        </details>
        <details><summary>J'ai acheté Pro et il n'apparaît pas</summary>
          <p>Dans Personnaliser, touchez Restaurer l'achat, avec le même compte de boutique que celui de l'achat. S'il n'apparaît toujours pas, écrivez-nous.</p>
        </details>
      </div>

      <h2 id="guias">Guides pas à pas</h2>
      <p><a href="@@R_guias@@">Voir tous les guides</a></p>
      <ul>
@@GUIAS@@
      </ul>

      <h2 id="contacto">Encore des questions ?</h2>
      <p>Écrivez-nous à <a href="mailto:hola@mandotv.app?subject=Aide%20Mando%20TV">hola@mandotv.app</a>. Indiquez la marque et le modèle de votre TV et l'étape où vous êtes bloqué. Écrivez-nous dans votre langue. Nous répondons en espagnol ou en anglais, et dans la vôtre avec l'aide d'un traducteur si vous préférez.</p>
'''

PRIVACIDAD = dict(
  titulo='Politique de confidentialité | Mando TV',
  desc="Mando TV ne collecte aucune donnée personnelle : ni compte, ni pub, ni traceur. L'application ne parle qu'à votre TV, dans votre réseau Wi-Fi.",
  h1='Confidentialité',
  intro="En bref : Mando TV ne collecte pas vos données. Il n'y a ni compte, ni publicité, ni traceur, ni serveur à nous qui conserve ce que vous faites.",
)
PRIVACIDAD_HTML = '''      <p class="fecha">En vigueur depuis le 14 novembre 2026. Dernière mise à jour : 15 novembre 2026.</p>

      <h2>Qui nous sommes</h2>
      <p>Mando TV est une application pour piloter votre TV depuis votre téléphone ou votre ordinateur. Cette politique explique quelles informations l'application utilise et ce qu'elle en fait. Pour toute question, écrivez-nous à <a href="mailto:hola@mandotv.app">hola@mandotv.app</a>.</p>

      <h2>Quelles données nous collectons</h2>
      <p>L'application : aucune. L'application n'envoie à nous ni à des tiers aucune information sur vous ni sur la façon dont vous l'utilisez. Elle n'utilise aucun outil d'analyse, de publicité ou de suivi.</p>
      <p>Ce site web : nous mesurons les visites de deux façons, expliquées dans la section <a href="#cookies">Cookies sur ce site web</a>.</p>

      <h2>Ce que l'application stocke sur votre appareil</h2>
      <p>Pour fonctionner, l'application stocke ce qui suit uniquement sur votre téléphone ou votre ordinateur :</p>
      <ul>
        <li>Les TV que vous avez ajoutées : nom, marque, adresse IP dans votre réseau et adresse matérielle du réseau (MAC), utilisée pour l'allumer.</li>
        <li>Les clés de connexion que chaque TV remet quand vous acceptez l'autorisation. Elles sont stockées chiffrées dans le stockage sécurisé du système (Trousseau sur iPhone et Mac, Keystore sur Android, stockage protégé sur Windows).</li>
        <li>Vos préférences : thème clair ou sombre, couleur de fond, vibration et type de télécommande.</li>
        <li>Si vous utilisez les fonctions Pro : vos applications favorites, vos routines et vos dernières recherches YouTube (vous pouvez les supprimer depuis l'application).</li>
      </ul>
      <p>Si vous supprimez l'application, tout cela est supprimé avec elle.</p>

      <h2>Avec qui l'application communique</h2>
      <p>Avec vos TV, à l'intérieur de votre réseau Wi-Fi domestique. Pour les trouver, l'application explore votre réseau local ; c'est pourquoi, sur un iPhone, elle demande l'autorisation « Réseau local ». Le texte que vous saisissez avec le clavier de l'application va directement à la TV et n'est pas stocké.</p>
      <p>De plus, à son ouverture, l'application télécharge un petit fichier public depuis ce site web (mandotv.app/app/config.json) pour savoir s'il existe une nouvelle version à installer et quelles fonctions font partie de Mando TV Pro. C'est un téléchargement, comme l'ouverture d'une page : l'application n'envoie ni vos données, ni vos TV, ni ce que vous faites. Elle indique seulement la version de l'application et le système (par exemple Android), pour pouvoir vous montrer le bon avis. Si vous n'avez pas Internet, l'application continue de fonctionner avec le dernier fichier téléchargé ; si plus de 30 jours passent sans pouvoir le télécharger, elle vous demandera de vous connecter un instant à Internet.</p>

      <h2>Microphone et voix</h2>
      <p>La recherche vocale n'utilise le microphone que pendant que vous touchez le bouton pour parler. Ce que vous dites est converti en texte par la reconnaissance vocale de votre système : Apple sur iPhone et Mac, Google sur Android et Microsoft sur Windows, selon leurs propres politiques de confidentialité. Mando TV n'enregistre ni ne stocke l'audio, et le texte obtenu va directement à votre TV, comme ce que vous saisissez avec le clavier.</p>

      <h2>Rapport de test</h2>
      <p>L'application a un bouton « Copier le rapport de test » pour nous aider à corriger les erreurs. Le rapport reste uniquement dans la mémoire de l'application tant qu'elle est ouverte et n'est jamais envoyé de lui-même : c'est vous qui décidez de le copier et de le partager. Il n'inclut ni clés de connexion, ni codes d'appairage, ni rien de ce que vous saisissez ; seulement les étapes suivies par l'application, comme la recherche, la connexion et les erreurs.</p>

      <h2 id="cookies">Cookies sur ce site web</h2>
      <p>Cela s'applique uniquement au site web mandotv.app, pas à l'application.</p>
      <h3>Jamais de cookies</h3>
      <p>Nous comptons les visites de façon anonyme avec Cloudflare Web Analytics : combien de personnes visitent le site, quelles pages elles lisent et depuis quel pays. Il n'utilise pas de cookies, n'utilise pas votre adresse IP pour vous identifier et ne suit pas ce que vous faites sur d'autres sites.</p>
      <h3>Avec des cookies, seulement si vous acceptez</h3>
      <p>Si vous touchez « Accepter » dans l'avis sur les cookies, nous activons Google Analytics (de Google LLC) pour mieux comprendre comment le site est utilisé : pages vues, temps passé sur la page, type d'appareil, ville approximative et provenance. Pour cela, il stocke les cookies _ga et _ga_* dans votre navigateur pendant 2 ans au maximum. Google peut traiter ces données sur des serveurs situés hors du Chili. Nous avons désactivé les fonctions publicitaires et Google Signals, et nous n'utilisons pas ces données pour vous montrer des publicités.</p>
      <p>Si vous touchez « Refuser » ou ne choisissez rien, Google Analytics n'est pas chargé et aucun cookie n'est stocké. Vous pouvez changer d'avis à tout moment avec le bouton « Cookies » en bas de chaque page ; si vous retirez votre autorisation, nous supprimons ces cookies.</p>
      <p>Votre choix est stocké dans votre navigateur (stockage local, envoyé à personne) pour que nous ne vous le demandions plus.</p>

      <h2>Achats</h2>
      <p>Si vous achetez Mando TV Pro, le paiement est traité par la boutique d'applications (App Store, Google Play ou Microsoft Store). Nous ne recevons ni ne stockons les données de votre carte. La boutique confirme seulement à l'application que l'achat existe.</p>

      <h2>E-mails que vous nous envoyez</h2>
      <p>Si vous nous écrivez à <a href="mailto:hola@mandotv.app">hola@mandotv.app</a>, nous utilisons votre adresse e-mail et ce que vous nous dites uniquement pour vous répondre. Nous ne la partageons pas et ne l'utilisons pas pour de la publicité. Vous pouvez nous demander de supprimer vos messages à tout moment.</p>

      <h2>Enfants</h2>
      <p>L'application ne collecte de données sur personne, y compris les enfants.</p>

      <h2>Modifications de cette politique</h2>
      <p>Si un jour ce que l'application fait de vos données change, nous mettrons à jour cette page et la date ci-dessus avant que le changement n'arrive dans l'application.</p>
'''


# --- Tipografía francesa: espacio duro antes de : ; ? ! y dentro de « » (solo en los textos de esta tabla) ---
def _fr(o):
  if isinstance(o, str):
    for a in (' :', ' ;', ' ?', ' !', ' »'):
      o = o.replace(a, ' ' + a[1:])
    return o.replace('« ', '« ')
  if isinstance(o, dict):
    return {k: _fr(v) for k, v in o.items()}
  if isinstance(o, list):
    return [_fr(x) for x in o]
  if isinstance(o, tuple):
    return tuple(_fr(x) for x in o)
  return o


for _n in ('UI', 'PIE', 'NOMBRE_OTRA', 'PAGINA_MARCA', 'OTRAS_GUIAS', 'INDICE', 'MARCAS', 'GUIAS', 'SOPORTE', 'SOPORTE_HTML', 'PRIVACIDAD', 'PRIVACIDAD_HTML'):
  globals()[_n] = _fr(globals()[_n])
