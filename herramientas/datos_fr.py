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
  aviso="Mando TV est une app indépendante : elle n'est ni affiliée aux fabricants de TV cités ni à Google, Amazon, Apple ou Roku, ni approuvée par eux. Les marques appartiennent à leurs propriétaires et sont citées uniquement pour indiquer la compatibilité. Android TV et Google TV sont des marques de Google LLC. Apple TV est une marque d'Apple Inc.",
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
    compat="Smart TV LG sous webOS (la plupart des modèles LG Smart TV depuis 2014). Fonctionne avec les téléviseurs LED, NanoCell, QNED et OLED. Les anciennes Smart TV LG sous NetCast (2011 à 2014, avant webOS) sont prises en charge, en bêta : elles s'appairent avec la clé à 6 chiffres affichée par la TV.",
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
      ("Fonctionne-t-elle avec les anciennes TV LG d'avant webOS ?", "En bêta, oui, avec les Smart TV LG NetCast de 2011 à 2014. Elles s'appairent avec la clé à 6 chiffres affichée par la TV. C'est nouveau, donc il peut encore rester des défauts."),
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
      ('Faire sonner la télécommande', "Si votre télécommande Roku a un haut-parleur, comme la Roku Voice Remote Pro, Mando TV la fait sonner pour que vous la retrouviez. C'est gratuit, et le Roku doit être allumé."),
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
      ('Parler à la TV depuis le PC (Pro)', "Avec Mando TV Pro, vous donnez des ordres à la TV avec le micro du PC : « ouvre YouTube », « monte le son » ou « éteins dans 30 minutes », à votre façon. Sous Windows, la voix est reconnue sur le PC lui-même : pas besoin d'Internet, aucun réglage de Windows à modifier, et elle fonctionne dans les 6 langues de l'app. Ce que vous dites ne quitte pas le PC et n'est pas conservé. Seuls les processeurs très anciens font passer l'app par la saisie vocale de Windows, qui a besoin de la « Reconnaissance vocale en ligne » activée dans les paramètres de confidentialité et de la langue ajoutée dans Windows (français de France ou du Canada). Dans ce cas, s'il manque quelque chose, l'app vous prévient et ouvre le réglage avec un bouton."),
    ],
    marca=None,
    faq=[
      ("Faut-il un câble ou le Bluetooth pour contrôler la TV depuis mon PC ?", "Non. Mando TV se connecte via votre réseau domestique : le PC et la TV doivent seulement être sur la même box."),
      ('Cela fonctionne-t-il avec toutes les TV ?', "Cela fonctionne avec les TV Samsung sous Tizen (2016 et plus récentes), LG sous webOS, Roku, et Google TV ou Android TV (Sony, Philips, TCL, Hisense, Sharp, Xiaomi, Toshiba, Panasonic, Haier, Skyworth et autres)."),
      ('Combien cela coûte-t-il ?', "Les touches, le clavier et l'allumage par le réseau sont gratuits et sans publicité. Mando TV Pro est un achat unique, sans abonnement, pour des extras comme le pavé tactile, les raccourcis clavier du PC et la mini télécommande."),
      ('Pourquoi le micro ne me comprend pas sous Windows ?', "Vérifiez que la voix est activée (c'est une fonction Pro) et que le micro du PC fonctionne sous Windows. Sur presque tous les PC, la voix est reconnue sur l'appareil, sans Internet. Seuls les processeurs très anciens passent par la saisie vocale de Windows : vérifiez alors que la « Reconnaissance vocale en ligne » est activée dans les paramètres de confidentialité de Windows et que Windows a le français (France) ou (Canada) dans les paramètres de langue. Mando TV utilise cette langue seulement pendant l'écoute."),
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
      ("Laissez l'app vous guider", "Dans la liste des TV, un bouton s'affiche pour le cas où votre TV n'apparaît pas. L'app vérifie pas à pas les causes les plus courantes (même réseau Wi-Fi, VPN, autorisation du réseau local et plus) et propose un bouton pour revérifier après chaque correction. Cet assistant est gratuit."),
      ("Où trouver l'adresse IP de la TV", "Elle se trouve dans le menu réseau de la TV et varie un peu selon le modèle. Sur LG : Paramètres, Réseau, Connexion Wi-Fi, Paramètres Wi-Fi avancés. Sur Samsung : Paramètres, Général, Réseau, État du réseau, Paramètres IP. Sur Roku : Paramètres, Réseau, À propos. Sur Android TV et Google TV : Paramètres, Réseau et Internet, puis touchez votre réseau. C'est un nombre comme 192.168.1.86."),
      ("Si elle apparaît mais que la connexion se coupe", "Quand la connexion se coupe au bout de quelques secondes, la cause se trouve généralement sur le téléphone : un VPN, un passage à un autre réseau Wi-Fi ou l'économiseur de batterie. Désactivez le VPN, restez sur le même Wi-Fi et réessayez."),
      ('Wi-Fi 2,4 et 5 GHz', "Peu importe que votre téléphone soit sur le réseau 5 GHz et la TV sur le 2,4 GHz, tant que les deux viennent de la même box. Si vous avez un répéteur Wi-Fi et que la TV n'apparaît toujours pas, rapprochez votre téléphone de la box principale et réessayez."),
    ],
    marca=None,
    faq=[
      ('Puis-je piloter la TV avec les données mobiles ?', "Non. Le signal de la télécommande passe par votre Wi-Fi domestique, donc votre téléphone et la TV doivent être sur le même réseau."),
      ('Pourquoi cela ne fonctionne-t-il pas avec le VPN activé ?', "Parce que le VPN envoie tout le trafic de votre téléphone par un autre réseau et que le téléphone ne voit plus les appareils de chez vous. Désactivez-le pendant que vous utilisez la télécommande."),
      ("Le Bluetooth ou l'infrarouge fonctionnent-ils ?", "Pour les Smart TV, Mando TV utilise le Wi-Fi. L'infrarouge ne fonctionne que sur les téléphones Android équipés d'un émetteur infrarouge et sert pour les TV qui ne sont pas des Smart TV. Le Bluetooth est disponible en bêta, gratuitement et seulement sur Android 9 ou plus récent : le téléphone se connecte à la TV comme un clavier et une télécommande Bluetooth, sans Wi-Fi. Il fonctionne avec Google TV, Android TV et Fire TV ; chez d'autres marques qui acceptent les claviers Bluetooth, il peut fonctionner, mais Roku ne les accepte pas."),
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
      "Avant tout, essayez de faire sonner la télécommande. Si votre télécommande Roku a un haut-parleur, comme la Roku Voice Remote Pro, ouvrez Mando TV, connectez-vous au Roku et utilisez l'option pour faire sonner la télécommande afin de la retrouver. Cela ne marche qu'avec les télécommandes Roku qui ont un haut-parleur, et le Roku doit être allumé.",
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
            <li>Touchez, dans la liste des TV, le bouton prévu pour le cas où votre TV n'apparaît pas : l'app vérifie pas à pas les causes les plus courantes (même réseau Wi-Fi, VPN, autorisation du réseau local et plus) et propose un bouton pour revérifier après chaque correction.</li>
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
PRIVACIDAD_HTML = '''      <p class="fecha">En vigueur depuis le 14 novembre 2026. Dernière mise à jour : 21 novembre 2026.</p>

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

      <p>Si vous envoyez des photos ou des vidéos à la TV (une fonction Pro), la TV télécharge uniquement les fichiers que vous choisissez, directement depuis votre téléphone ou votre PC via le Wi-Fi de votre domicile. Ils ne passent ni par Internet ni par nous, l'application ne voit pas le reste de vos photos et le partage s'arrête quand vous fermez cet écran.</p>
      <h2>Microphone et voix</h2>
      <p>La recherche vocale n'utilise le microphone que pendant que vous touchez le bouton pour parler. Ce que vous dites est converti en texte par la reconnaissance vocale de votre système : Apple sur iPhone et Mac et Google sur Android, selon leurs propres politiques de confidentialité. Sur Windows, la voix est reconnue sur votre propre PC et ne le quitte pas ; seuls les processeurs très anciens passent par la saisie vocale de Windows, de Microsoft, selon sa politique de confidentialité. Mando TV n'enregistre ni ne stocke l'audio, et le texte obtenu va directement à votre TV, comme ce que vous saisissez avec le clavier.</p>

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


# >>> guías traídas del inglés (ensamblar.py)
# Adaptadas con Ollama (qwen3.6:35b) desde las guías inglesas y auditadas por Opus el 22-nov. Rutas en idiomas_sitio.py.
GUIAS += [
  dict(clave='no-sub', corto='Télécommande sans abonnement', fecha='2026-11-23',
    titulo='Appli télécommande TV sans abonnement ni publicité',
    desc='Lassé des applis de télécommande avec pubs ou abonnement à la semaine ? Mando TV est gratuite et sans pub, et Pro est un achat unique facultatif.',
    h1='Une appli télécommande TV sans abonnement ni publicité',
    intro="Beaucoup d'applis de télécommande affichent des publicités ou demandent un abonnement avant de fonctionner. Mando TV fonctionne différemment : la télécommande est gratuite, sans pub ni compte, et l'option Pro se paie une seule fois. Voici la comparaison, y compris ce qu'elle ne fait pas.",
    pasos=[
      "Avant d'installer une appli de télécommande, ouvrez sa page dans la boutique et regardez les achats intégrés. Des prix hebdomadaires ou mensuels signifient un abonnement.",
      "Sur Google Play, vérifiez si la page indique « Contient des publicités » et lisez les avis récents à une ou deux étoiles : c'est là qu'apparaissent les mauvaises surprises payantes.",
      "Vérifiez que l'appli prend en charge votre TV via le Wi-Fi. Mando TV fonctionne avec Samsung (2016 et après), LG webOS, Roku, Google TV et Android TV, et Fire TV.",
      'Installez Mando TV, connectez votre téléphone au même Wi-Fi que la TV et touchez votre TV dans la liste.',
      "Acceptez l'invite sur la TV ou saisissez le code qu'elle affiche, puis utilisez la télécommande. Les touches, le volume, les chaînes et le clavier sont gratuits.",
    ],
    tabla=dict(titulo='Mando TV comparée à de nombreuses applis',
      cabeza=['', 'Mando TV', 'Nombreuses applis avec pubs ou abonnements'],
      filas=[
        ['Télécommande de base', 'Gratuite', 'Souvent gratuit avec pubs, ou verrouillé derrière un essai'],
        ['Publicités', 'Aucune', 'Fréquentes'],
        ['Abonnement', 'Aucun. Pro est un achat unique optionnel', 'Formules hebdomadaires ou mensuelles fréquentes'],
        ['Compte', 'Non nécessaire', "Varie selon l'appli"],
        ['Smart TV en Wi-Fi', 'Samsung (2016 et après), LG webOS, Roku, Google TV et Android TV, Fire TV, Apple TV (bêta)', "Varie selon l'appli"],
        ['Infrarouge pour anciennes TV', 'Gratuit sur les téléphones Android avec émetteur infrarouge (nouveau)', 'Certaines applis, uniquement sur les téléphones avec émetteur infrarouge'],
        ['Bluetooth', 'Bêta sur Android 9 ou plus récent, gratuit', "Varie selon l'appli"],
        ['Photos et vidéos vers la TV', "Pro, en Wi-Fi (pas de recopie d'écran)", "Varie selon l'appli"],
        ['Téléphones et ordinateurs', 'iPhone, iPad et Windows, et Android en accès anticipé', 'Varie'],
        ["Recopie de l'écran", "Gratuite sur iPhone et iPad, via Recopie de l'écran dans le Centre de contrôle (TV compatibles AirPlay)", 'Certaines applis le proposent'],
      ],
      nota="Mando TV n'est comparée à aucune appli en particulier. Consultez la fiche de chaque appli pour ses prix actuels."),
    extra=[
      ('Ce que Mando TV ne fait pas', "Elle n'a pas de recopie d'écran à elle : sur iPhone et iPad, elle vous guide vers Recopie de l'écran dans le Centre de contrôle, la fonction de l'iPhone lui-même, qui marche avec les TV compatibles AirPlay. Avec Mando TV Pro, elle peut aussi envoyer des photos et des vidéos à la TV via le Wi-Fi de la maison. Elle contrôle les Smart TV via le Wi-Fi de la maison. Une TV qui n'est pas une Smart TV peut être contrôlée par infrarouge depuis un téléphone Android avec un émetteur infrarouge. Sur Android 9 ou plus récent, le téléphone peut aussi se connecter à Google TV, Android TV et Fire TV via Bluetooth comme clavier et télécommande, sans Wi-Fi. Cette option est en bêta et gratuite."),
      ("Comment Mando TV gagne de l'argent", "Pas avec des publicités ni avec vos données : l'appli n'en collecte aucune. Mando TV est financée par Pro, un achat unique optionnel pour les extras. La télécommande de base est gratuite."),
      ('Sur les appareils que vous avez déjà', "iPhone et iPad depuis l'App Store, PC Windows depuis le Microsoft Store, et Android via un accès anticipé gratuit sur Google Play. Voir [appli télécommande TV pour iPhone](@iphone) et [appli télécommande TV pour Windows](@windows)."),
      ('Confidentialité', "Pas de compte ni de suivi dans l'appli. Elle communique avec la TV à l'intérieur de votre réseau domestique, et les clés de connexion restent chiffrées sur votre appareil. Détails dans la [politique de confidentialité](@privacidad)."),
    ],
    marca=None,
    faq=[
      ('Existe-t-il une télécommande TV sans abonnement ?', "Oui. Mando TV n'a aucun abonnement : la télécommande est gratuite, sans pub, et Pro est un achat unique optionnel."),
      ('Mando TV est-elle vraiment gratuite ?', "Oui. Les flèches, OK, Retour, Accueil, volume, chaînes, touches numériques, clavier et l'allumage ou l'extinction sont gratuits, sans pub ni limite de temps."),
      ('Fonctionne-t-elle sans Wi-Fi ?', "Généralement non. Mando TV contrôle les Smart TV via le Wi-Fi de la maison. Les exceptions sont l'infrarouge sur les téléphones Android équipés d'un émetteur infrarouge, qui fonctionne aussi avec les TV qui ne sont pas des Smart TV ou qui n'ont jamais été connectées au Wi-Fi, et le Bluetooth en bêta sur Android 9 ou plus récent, qui fonctionne avec Google TV, Android TV et Fire TV."),
    ]),
  dict(clave='roku-app-alt', corto="Alternative à l'appli Roku", fecha='2026-11-23',
    titulo="Alternative à l'application Roku : une télécommande simple",
    desc="Alternative à l'application Roku pour la télécommande : Mando TV contrôle TV et lecteurs Roku en Wi-Fi, sans compte ni pub, et aussi Samsung, LG, Google TV.",
    h1="Alternative à l'appli Roku : une seule télécommande",
    intro="L'application officielle Roku fait beaucoup de choses : boutique de chaînes, diffusion, écoute privée et télécommande. Si vous voulez juste une télécommande rapide, ou si vous avez aussi une TV Samsung, LG ou Google TV à la maison, Mando TV est une alternative simple qui contrôle le Roku via votre Wi-Fi sans compte.",
    pasos=[
      'Connectez votre téléphone et le Roku au même réseau Wi-Fi.',
      'Téléchargez Mando TV et ouvrez-la. Votre TV Roku ou votre lecteur Roku apparaît dans la liste. Touchez son nom. Le Roku ne demande pas de code.',
      'Utilisez le pavé directionnel, OK, Retour, Accueil, le volume et le clavier. Tapez vos recherches dans les chaînes Roku avec le clavier de votre téléphone.',
      "Si les touches ne font rien, sur le Roku allez dans Paramètres > Système > Paramètres système avancés > Contrôle par applications mobiles, et réglez l'accès au réseau sur Par défaut ou Permissif (sur les versions récentes du logiciel Roku, activez simplement « Contrôle par applications mobiles »).",
      'Optionnel : sur une TV Roku, activez le « Démarrage rapide de la TV » dans Paramètres > Système > Alimentation pour que Mando TV puisse allumer la TV.',
    ],
    extra=[
      ('Où Mando TV est plus adaptée', 'Une seule appli pour plusieurs TV : Roku, Samsung, LG et Google TV ou Android TV. Sans compte, sans pub. Elle fonctionne aussi depuis un PC Windows, ce qui est pratique au bureau. Les flèches et le volume répondent vite, et le clavier rend la saisie des recherches simple.'),
      ("Où l'application officielle Roku est plus adaptée", "Gardez l'application Roku pour ce qu'elle offre en plus de la télécommande, comme parcourir et ajouter des chaînes depuis la boutique de chaînes Roku, ainsi que ses propres fonctions de diffusion et d'écoute privée. Utilisez les deux si vous voulez. Elles peuvent fonctionner sur le même téléphone."),
      ('TV Roku et lecteurs Roku', "Les deux fonctionnent. Cela inclut les modèles de TV Roku de TCL, Hisense, Philips et d'autres, ainsi que les Roku Express, Streaming Stick et Ultra. Les détails sont sur la [page de l'application télécommande Roku](@roku)."),
      ("Si l'application Roku ne fonctionne plus", "Si les touches ont cessé de répondre, le Roku bloque probablement le contrôle par les applications. Le guide [L'appli Roku ne fonctionne pas](@roku-403) explique comment corriger ce réglage."),
      ('Gratuit et Pro', "Les flèches, OK, Retour, Accueil, volume, chaînes, touches numériques, clavier, ouverture d'applications, changement d'entrée, allumage et extinction sont gratuits, sans pub ni abonnement. Mando TV Pro est un achat unique optionnel pour les fonctions supplémentaires."),
    ],
    marca='roku',
    faq=[
      ("Ai-je besoin d'un compte Roku pour utiliser Mando TV ?", 'Non. Mando TV communique avec le Roku via votre réseau domestique et ne demande pas de compte.'),
      ("Mando TV remplace-t-elle complètement l'application mobile Roku ?", "Pour la télécommande, oui. Pour la boutique de chaînes, la diffusion et l'écoute privée, gardez l'application officielle Roku."),
      ('Cela fonctionnera-t-il sur mon Roku Express ou Streaming Stick ?', 'Oui. Tous les lecteurs Roku et TV Roku sont contrôlés de la même manière.'),
    ]),
  dict(clave='lg-thinq', corto='Alternative à LG ThinQ', fecha='2026-11-23',
    titulo='Alternative à LG ThinQ : télécommande TV LG sans compte',
    desc='Vous cherchez une alternative à LG ThinQ juste pour piloter votre TV LG ? Mando TV contrôle les TV LG sous webOS en Wi-Fi, sans compte LG ni publicité.',
    h1='Alternative à LG ThinQ comme télécommande de votre TV LG',
    intro="LG ThinQ est l'application officielle de LG, conçue pour gérer toute une maison connectée : appareils électroménagers, TV et plus. Si vous voulez juste une télécommande simple pour votre TV LG, Mando TV fait ce travail sur votre réseau Wi-Fi, sans compte LG à créer ni publicité.",
    pasos=[
      'Connectez votre téléphone ou votre PC (iPhone, Android ou Windows) et votre TV LG au même réseau Wi-Fi.',
      'Téléchargez Mando TV et ouvrez-la. Votre TV LG apparaît toute seule dans la liste. Touchez-la.',
      "Une demande d'autorisation s'affiche sur l'écran de la TV. Acceptez-la une fois avec la télécommande, le joystick sous l'écran ou la Magic Remote.",
      "Utilisez les touches, le volume et le clavier tout de suite. Aucun compte LG ni enregistrement de la TV n'est nécessaire.",
      "Optionnel : activez « Téléviseur en marche avec mobile » dans les paramètres de la TV pour pouvoir aussi l'allumer depuis votre téléphone.",
    ],
    extra=[
      ('Mando TV ou LG ThinQ : laquelle choisir', "Utilisez ThinQ si vous voulez gérer l'électroménager LG comme un lave-linge, un frigo ou une climatisation, ou les fonctionnalités du compte LG. Utilisez Mando TV si vous voulez une télécommande rapide et simple pour la TV qui fonctionne aussi avec Samsung, Roku et Google TV dans la même application. Beaucoup de gens gardent les deux : ThinQ pour l'électroménager, Mando TV pour la TV."),
      ('Ce que fait Mando TV sur une TV LG', 'Elle fonctionne avec les Smart TV LG sous webOS, ce qui couvre la plupart des modèles depuis 2014, y compris LED, NanoCell, QNED et OLED. Elle vous donne le pavé directionnel, OK, Retour, Accueil, le volume, les chaînes, le muet, les contrôles de lecture et un clavier pour taper dans YouTube, Netflix ou le navigateur. La liste des applications et celle des entrées sont aussi gratuites. Avec Pro, vous avez aussi un pointeur comme la Magic Remote.'),
      ('Ce que Mando TV ne fait pas', "Elle ne contrôle pas l'électroménager LG, elle n'utilise pas votre compte LG et elle ne remplace pas les services du compte LG sur la TV. C'est une télécommande, pas un hub domotique."),
      ('Confidentialité et publicité', "Mando TV n'a ni publicité ni compte. Elle communique avec la TV à l'intérieur de votre réseau domestique et garde la clé de connexion chiffrée sur votre propre appareil. La page [application télécommande LG](@lg) détaille toutes les fonctions."),
      ('Gratuit et Pro', "Les flèches, OK, Retour, Accueil, le volume, les chaînes, les touches numériques, le clavier, l'ouverture des applications, le changement d'entrées et la mise sous/hors tension sont gratuits, sans publicité ni abonnement. Mando TV Pro est un achat unique optionnel pour les extras."),
    ],
    marca='lg',
    faq=[
      ("Puis-je contrôler ma TV LG sans l'application LG ThinQ ?", "Oui. Mando TV se connecte directement aux TV LG webOS via votre Wi-Fi. Vous acceptez une demande sur la TV la première fois, et c'est tout, sans compte LG."),
      ('Mando TV fonctionne-t-elle avec le pointeur de la Magic Remote ?', "Mando TV Pro dispose d'un pointeur que vous déplacez avec votre doigt sur l'écran du téléphone, comme la Magic Remote déplace la flèche."),
      ('Mando TV est-elle une appli LG ?', "Non. Mando TV est une application indépendante et n'est pas affiliée à LG. LG et ThinQ appartiennent à leurs propriétaires et sont nommés uniquement pour décrire la compatibilité."),
    ]),
  dict(clave='smartthings', corto='Alternative à la télécommande SmartThings', fecha='2026-11-23',
    titulo='SmartThings ne fonctionne pas ? Une alternative simple',
    desc='La télécommande SmartThings est lente ou en panne ? Mando TV contrôle les TV Samsung sous Tizen par Wi-Fi, sans compte Samsung ni pub. Étapes et correctifs.',
    h1='Alternative à SmartThings pour les TV Samsung',
    intro="SmartThings est l'appli Samsung pour la maison connectée ; sa télécommande passe par votre compte Samsung. Si elle ne fonctionne plus ou si vous voulez une solution rapide, Mando TV contrôle les TV Samsung sous Tizen (modèles 2016 et après) directement sur votre Wi-Fi, sans compte.",
    pasos=[
      'Connectez votre téléphone et la TV Samsung au même réseau Wi-Fi.',
      'Téléchargez et ouvrez Mando TV. Votre TV Samsung apparaît dans la liste. Touchez-la.',
      "La TV demande d'autoriser la connexion. Choisissez Autoriser avec la télécommande ou le bouton de contrôle de la TV (une seule fois).",
      'Utilisez tout de suite les flèches, OK, Retour, Accueil, le volume, les chaînes et le clavier.',
      "Optionnel : activez « Allumer avec un appareil mobile » dans Paramètres > Général > Réseau > Paramètres d'expert pour allumer la TV depuis Mando TV.",
    ],
    extra=[
      ('Pourquoi la télécommande du téléphone ne répond plus', 'Les causes sont simples : réseau Wi-Fi différent, VPN activé ou veille profonde de la TV. Avec SmartThings, le compte Samsung peut aussi poser problème, par exemple si vous êtes déconnecté. Mando TV communique directement sur le réseau local, sans compte. Plus de solutions dans [Votre téléphone ne trouve pas la TV](@not-found).'),
      ('Mando TV ou SmartThings : laquelle choisir', "Gardez SmartThings pour l'électroménager Samsung, l'éclairage ou la maison connectée. Utilisez Mando TV pour une télécommande rapide, ou si vous avez aussi une TV LG, un Roku, une Google TV ou un Fire TV : une seule appli les contrôle tous. Les deux peuvent coexister."),
      ("Si vous avez refusé l'autorisation par erreur", 'Sur la TV, allez dans Paramètres > Général > Gestionnaire de périphériques externes > Gestionnaire de connexion de périphérique, et réglez Mando TV sur autorisé.'),
      ('Sans télécommande du tout ?', 'Vous pouvez accepter avec le bouton de contrôle de la TV. Le guide [TV Samsung sans télécommande](@samsung-lost) explique comment faire.'),
      ('Gratuit et Pro', 'La télécommande est gratuite, sans pub ni abonnement. Mando TV Pro est un achat unique optionnel pour les fonctions supplémentaires.'),
    ],
    marca='samsung',
    faq=[
      ('Puis-je contrôler ma TV Samsung sans SmartThings ?', 'Oui. Mando TV se connecte directement aux TV Samsung sous Tizen par Wi-Fi. Une seule autorisation sur la TV, sans compte Samsung.'),
      ("Mando TV contrôle-t-elle l'électroménager Samsung ?", "Non. C'est une télécommande TV uniquement. Gardez SmartThings pour l'électroménager et la maison connectée."),
      ('Mando TV est-elle une appli Samsung ?', "Non. Mando TV est indépendante et n'est pas affiliée à Samsung. Samsung et SmartThings appartiennent à leurs propriétaires et ne sont cités que pour indiquer la compatibilité."),
    ]),
  dict(clave='googletv-alt', corto="Alternative à l'appli télécommande Google TV", fecha='2026-11-23',
    titulo='La télécommande Google TV ne marche pas ? Une alternative',
    desc='La télécommande du téléphone ne trouve pas votre Google TV ? Mando TV contrôle Google TV et Android TV en Wi-Fi, sans compte Google ni pub.',
    h1='Alternative à la télécommande Google TV sur téléphone',
    intro="La télécommande sur téléphone pour Google TV et Android TV est intégrée à l'application de Google et liée à votre compte Google. Quand elle ne trouve pas la TV, vous êtes bloqué. Mando TV est une application de télécommande distincte qui s'appaire avec le code à 6 caractères affiché sur l'écran de la TV et fonctionne sans compte Google, depuis un iPhone, un téléphone Android ou un PC Windows.",
    pasos=[
      'Allumez la TV et connectez votre téléphone au même réseau Wi-Fi.',
      'Téléchargez Mando TV et ouvrez-la. Touchez votre Google TV ou Android TV dans la liste.',
      'La TV affiche un code à 6 caractères. Saisissez-le dans Mando TV et touchez Associer.',
      "Utilisez le pavé directionnel, OK, Retour, Accueil, le volume et le clavier. Aucune connexion à un compte n'est nécessaire.",
      "Optionnel : cherchez « Wake on LAN » ou une option pour allumer via le réseau dans les paramètres de la TV pour que l'application puisse aussi l'allumer.",
    ],
    extra=[
      ('Pourquoi la télécommande du téléphone ne trouve plus la TV', "Dans la plupart des cas, c'est le réseau : le téléphone et la TV sont sur des réseaux Wi-Fi différents, un VPN est activé, ou un réseau invité isole les appareils. Corrigez cela en premier, car cela affecte toutes les applications de télécommande. Lisez [Votre téléphone ne trouve pas la TV](@not-found)."),
      ('Avec quelles TV cela fonctionne', "Les TV sous Google TV et Android TV de Sony, TCL, Hisense, Philips, Sharp, Xiaomi, Toshiba et d'autres, ainsi que Chromecast avec Google TV, Google TV Streamer et Nvidia Shield. Toutes s'appairent de la même manière, avec le code affiché à l'écran, une seule fois."),
      ("Où l'application Google est meilleure", "L'application Google vous aide aussi à trouver quoi regarder et garde votre liste de choses à regarder. Gardez-la pour cela. Mando TV est juste la télécommande, et elle contrôle également Samsung, LG, Roku et Fire TV depuis la même application, et depuis un PC Windows."),
      ("Si l'ancienne application Android TV Remote a disparu", "Google a déplacé sa télécommande téléphonique de l'ancienne application Android TV Remote Control vers l'application Google TV. Si vous voulez une télécommande autonome, Mando TV en est une."),
      ('Gratuit et Pro', 'La télécommande est gratuite à télécharger et à utiliser, sans pub ni abonnement. Mando TV Pro est un achat unique optionnel pour des fonctionnalités supplémentaires.'),
    ],
    marca='android',
    faq=[
      ("Ai-je besoin d'un compte Google pour utiliser Mando TV avec Google TV ?", "Non. Le code affiché sur l'écran de la TV suffit pour l'appairage."),
      ('Cela fonctionne-t-il avec Chromecast avec Google TV ?', "Oui. L'appairage se fait de la même manière, avec le code à 6 caractères affiché à l'écran."),
      ("Puis-je l'utiliser depuis un iPhone ?", "Oui. Mando TV est disponible sur l'App Store pour iPhone et iPad, sur Microsoft Store pour Windows, et en accès anticipé gratuit sur Google Play pour Android."),
    ]),
  dict(clave='windows', corto='Télécommande TV pour Windows', fecha='2026-11-23',
    titulo='Appli télécommande TV pour PC Windows : pilotez votre TV',
    desc='Contrôlez Samsung, LG, Roku, Google TV ou Fire TV depuis un PC Windows avec Mando TV : raccourcis clavier, mini-télécommande et Wi-Fi. Microsoft Store.',
    h1='Appli télécommande TV pour PC Windows',
    intro="Mando TV dispose d'une application Windows qui transforme votre PC ou portable en télécommande via le réseau de la maison. Tapez sur la TV avec votre vrai clavier, gardez une petite fenêtre de télécommande au premier plan pendant que vous travaillez, et contrôlez Samsung, LG, Roku, Google TV ou Fire TV depuis la même application.",
    pasos=[
      'Installez Mando TV gratuitement depuis le Microsoft Store sur un PC Windows 10 ou 11.',
      'Vérifiez que le PC et la TV sont connectés au même réseau, en Wi-Fi ou par câble via le même routeur.',
      'Ouvrez Mando TV. La TV apparaît dans la liste. Cliquez dessus.',
      "Acceptez l'invite sur la TV si elle le demande (LG, Samsung), ou saisissez le code qu'elle affiche (Google TV, Fire TV).",
      "Cliquez sur les boutons ou tapez une recherche avec votre clavier. C'est terminé.",
    ],
    extra=[
      ('Raccourcis clavier (Pro)', 'Avec Pro, le clavier de votre PC devient la télécommande : flèches pour se déplacer, Entrée pour OK, Retour arrière ou Échap pour revenir en arrière, plus et moins pour le volume, M pour couper le son et Espace pour mettre en pause.'),
      ('Mini-télécommande (Pro)', 'Une petite fenêtre de télécommande qui reste au premier plan par-dessus les autres fenêtres, pour changer le volume ou mettre en pause sans quitter ce que vous faites.'),
      ('Taper du texte sur la TV depuis le PC', "Le clavier à l'écran d'une TV est lent. Dans Mando TV, vous tapez avec votre vrai clavier et le texte va dans la barre de recherche de la TV. Cette partie est gratuite."),
      ('Plus de détails', 'Pour la version étape par étape, consultez [comment contrôler votre TV depuis un PC Windows](@pc). Pour le contrôle via téléphone, lisez [utiliser votre téléphone comme télécommande via Wi-Fi](@wifi).'),
      ('Gratuit et Pro', "Les flèches, OK, Retour, Accueil, volume, chaînes, touches numériques, clavier, ouverture d'applications, changement d'entrée, allumage et extinction sont gratuits, sans pub ni abonnement. Mando TV Pro est un achat unique optionnel pour les extras. Sur Windows, Pro s'achète via le Microsoft Store."),
      ('Commandes vocales depuis le PC (Pro)', "Avec Pro, vous pouvez parler à la TV via le microphone du PC. La reconnaissance vocale se fait sur le PC lui-même : elle ne nécessite ni internet ni modification des paramètres Windows. Ce que vous dites ne quitte jamais le PC et n'est pas stocké. Sur les processeurs très anciens, l'application utilise la saisie vocale Windows, qui nécessite l'option « Reconnaissance vocale en ligne » activée dans Paramètres > Confidentialité et sécurité > Voix et votre langue ajoutée dans Windows."),
    ],
    marca=None,
    faq=[
      ("L'application télécommande TV pour Windows a-t-elle besoin de Bluetooth ou d'un câble ?", 'Non. Elle utilise votre réseau domestique. Le PC et la TV doivent simplement être connectés au même routeur.'),
      ('Quelles TV puis-je contrôler depuis Windows ?', 'Les TV Samsung sous Tizen, les TV LG sous webOS, Roku TV et les lecteurs Roku, Google TV et Android TV, ainsi que Fire TV.'),
      ("Puis-je voir l'image de la TV sur mon PC ou l'écouter sur ses haut-parleurs ?", "Non. Mando TV est uniquement une télécommande. Elle ne diffuse ni ne recopie l'image de la TV sur l'ordinateur."),
      ('Pourquoi la commande vocale ne fonctionne-t-elle pas sur mon PC Windows ?', "La voix est une fonctionnalité Pro, vérifiez donc que Pro est actif et que le microphone du PC fonctionne. Sur la plupart des PC, la reconnaissance vocale se fait localement, sans internet. Sur les processeurs très anciens, l'application utilise la saisie vocale Windows : activez alors « Reconnaissance vocale en ligne » dans Paramètres > Confidentialité et sécurité > Voix et ajoutez votre langue dans Paramètres > Heure et langue."),
    ]),
  dict(clave='iphone', corto='Télécommande TV pour iPhone', fecha='2026-11-23',
    titulo='Appli télécommande TV pour iPhone : Samsung, LG, Roku',
    desc="Utilisez votre iPhone comme télécommande Wi-Fi pour Samsung, LG, Roku, Google TV et Fire TV. Gratuite sur l'App Store, sans compte ni publicité.",
    h1='Télécommande TV sur iPhone : une seule pour toutes les TV',
    intro="Mando TV transforme votre iPhone ou iPad en télécommande pour les TV Samsung, LG, Roku, Google TV ou Android TV et Fire TV, via le Wi-Fi de la maison. Elle est gratuite sur l'App Store, sans compte ni publicité. Elle fonctionne aussi sur Android et Windows.",
    pasos=[
      "Téléchargez Mando TV gratuitement sur l'App Store.",
      'Connectez votre iPhone et la TV au même réseau Wi-Fi.',
      "Ouvrez Mando TV et touchez Autoriser quand iOS demande l'accès au réseau local. L'application en a besoin pour trouver la TV.",
      "Touchez votre TV dans la liste. Acceptez la demande à l'écran de la TV si elle s'affiche (LG et Samsung), ou saisissez le code que la TV affiche (Google TV ou Fire TV).",
      'Utilisez les touches, le volume et le clavier. Vous êtes connecté.',
    ],
    extra=[
      ('Les TV compatibles', 'LG webOS, Samsung sous Tizen (2016 et après), Roku TV et lecteurs Roku, Google TV et Android TV, et Fire TV. Les pages dédiées sont [Samsung](@samsung), [LG](@lg), [Roku](@roku) et [Android TV](@android).'),
      ("Pourquoi la demande d'accès au réseau local", "L'iPhone empêche les applis de voir les appareils de votre réseau, sauf si vous l'autorisez. Si la TV n'apparaît pas dans la liste, ouvrez Réglages > Mando TV et activez « Réseau local ». L'application communique uniquement avec votre TV à l'intérieur de votre réseau domestique."),
      ("Pourquoi Mando TV et pas l'appli du fabricant", 'Chaque marque de TV a sa propre application, chacune voulant son propre compte ou configuration. Mando TV est une seule application pour toutes, sans compte.'),
      ('Gratuit et Pro sur iPhone', "Les flèches, OK, Retour, Accueil, le volume, les chaînes, les touches numériques, le clavier, l'ouverture d'applications, le changement de source et l'allumage et l'extinction sont gratuits, sans publicité ni abonnement. Mando TV Pro est un achat unique facultatif pour les fonctions supplémentaires, directement dans l'application."),
    ],
    marca=None,
    faq=[
      ('Mando TV est-elle gratuite sur iPhone ?', "Le téléchargement est gratuit, sans publicité. La télécommande de base est gratuite, tout comme l'ouverture d'applications et le changement de source. Les fonctions supplémentaires font partie de Mando TV Pro, un achat unique optionnel."),
      ('Cela fonctionne-t-il sur iPad ?', 'Oui. La même application fonctionne sur iPhone et iPad.'),
      ("Une application de télécommande iPhone a-t-elle besoin du Bluetooth ou d'un émetteur infrarouge ?", "Pas sur iPhone. Les iPhone n'ont pas d'émetteur infrarouge, le contrôle infrarouge n'est donc pas disponible, et l'option Bluetooth est uniquement pour Android 9 ou plus récent, pas pour iPhone. Sur iPhone, Mando TV contrôle les Smart TV et l'Apple TV (en bêta) via le Wi-Fi de la maison."),
    ]),
  dict(clave='firetv', corto='Télécommande Fire TV', fecha='2026-11-23',
    titulo='Appli télécommande Fire TV pour iPhone, Android et PC',
    desc='Contrôlez un Fire TV Stick, un Fire TV Cube ou une TV Fire TV depuis votre téléphone ou votre PC, en Wi-Fi, avec un code à 4 chiffres. Sans appli Amazon.',
    h1='Appli télécommande Fire TV sur téléphone ou PC',
    intro="Si votre télécommande Fire TV est perdue ou sans piles, Mando TV peut contrôler un Fire TV Stick, un Fire TV Cube ou une TV avec Fire TV intégré depuis votre téléphone ou PC, via le Wi-Fi de la maison. L'appairage nécessite un code à 4 chiffres. La prise en charge de Fire TV est nouvelle, mettez donc d'abord l'application à jour.",
    pasos=[
      "Mettez Mando TV à jour vers la dernière version depuis l'App Store, le Microsoft Store ou Google Play.",
      'Allumez le Fire TV et connectez votre téléphone au même réseau Wi-Fi.',
      'Ouvrez Mando TV. Votre Fire TV apparaît dans la liste. Touchez-le.',
      "L'écran de la TV affiche un code à 4 chiffres. Saisissez-le dans Mando TV. Vous ne le faites qu'une fois.",
      'Utilisez les touches directionnelles, OK, Retour, Accueil, les boutons de lecture et le clavier pour taper vos recherches.',
    ],
    extra=[
      ('Appareils Fire TV compatibles', "Fire TV Stick, Fire TV Stick 4K, Fire TV Cube et TV avec Fire TV intégré. La prise en charge est nouvelle et nous l'avons encore peu testée sur de vrais appareils. Si quelque chose ne fonctionne pas correctement, indiquez-nous votre modèle depuis la page d'aide."),
      ('Allumer un Fire TV', "Mando TV n'allume pas un Fire TV via le réseau. Allumez la TV avec son bouton d'alimentation : un Fire TV Stick ou Cube branché dessus se réveille généralement grâce au HDMI-CEC, et sur une TV avec Fire TV intégré, la TV est le Fire TV. Contrôlez ensuite le tout depuis votre téléphone."),
      ("Si votre Fire TV n'apparaît pas", 'Vérifiez que les deux appareils sont sur le même réseau Wi-Fi et que le Fire TV est actif. Sur un iPhone, autorisez « Réseau local » pour Mando TV dans Réglages. Consultez [Votre téléphone ne trouve pas la TV](@not-found).'),
      ('Pas de télécommande du tout ?', "Le Fire TV doit afficher le code PIN à l'écran, donc la TV et le Fire TV doivent être allumés et afficher une image. Si la TV est sur une entrée incorrecte, changez-la avec les boutons de la TV. Consultez [Changer d'entrée HDMI sans télécommande](@hdmi)."),
      ('Gratuit et Pro', "Les flèches, OK, Retour, Accueil, le volume, les chaînes, les touches numériques, le clavier, l'ouverture d'applications, le changement d'entrée, l'allumage et l'extinction sont gratuits, sans publicité ni abonnement. Mando TV Pro est un achat unique facultatif pour des fonctionnalités supplémentaires."),
    ],
    marca=None,
    faq=[
      ("Ai-je besoin de l'application Amazon Fire TV ?", "Non. Mando TV se connecte au Fire TV via votre Wi-Fi avec un code PIN. Vous n'avez pas besoin d'un compte Amazon sur le téléphone."),
      ('Cela fonctionne-t-il avec les TV avec Fire TV intégré et les Fire TV Stick ?', "Oui, c'est pour cela qu'elle a été conçue. La prise en charge est nouvelle, gardez l'application à jour et signalez-nous tout modèle qui ne fonctionne pas correctement."),
      ("Pourquoi ai-je besoin d'un code PIN ?", "Le Fire TV affiche un code à 4 chiffres pour prouver que vous êtes devant la TV. Personne ne peut s'appairer sans voir l'écran."),
    ]),
  dict(clave='firetv-lost', corto='Télécommande Fire TV perdue', fecha='2026-11-23',
    titulo='Télécommande Fire TV perdue ? Utilisez votre téléphone',
    desc='Télécommande du Fire TV Stick perdue ? Contrôlez-le depuis votre téléphone en Wi-Fi avec un code PIN à 4 chiffres. Astuces nouveau Wi-Fi et HDMI-CEC.',
    h1='Télécommande Fire TV perdue : utilisez votre téléphone',
    intro="Si la télécommande de votre Fire TV Stick, Fire TV Cube ou Smart TV Fire TV est perdue ou en panne, votre téléphone peut prendre le relais, tant que l'appareil reste connecté à votre Wi-Fi. L'appairage utilise un code PIN à 4 chiffres affiché à l'écran, sans besoin de l'ancienne télécommande.",
    pasos=[
      "Allumez la TV avec son bouton physique. Un Fire TV Stick ou Cube branché s'allume souvent avec elle ; avec le HDMI-CEC, la TV passe parfois sur son entrée toute seule.",
      "Si la TV affiche une autre entrée, changez-la avec le bouton d'entrée de la TV. Voir [Changer l'entrée HDMI sans télécommande](@hdmi).",
      'Connectez votre téléphone au même réseau Wi-Fi que le Fire TV.',
      'Téléchargez Mando TV et ouvrez-la. Votre Fire TV apparaît dans la liste. Touchez-le.',
      "La TV affiche un code PIN à 4 chiffres. Saisissez-le dans Mando TV. Vous ne le faites qu'une fois.",
      'Utilisez le pavé directionnel, OK, Retour, Accueil, le volume, les touches de lecture et le clavier depuis votre téléphone.',
    ],
    extra=[
      ("Essayez d'abord la télécommande de la TV (HDMI-CEC)", "De nombreuses télécommandes de TV peuvent piloter un Fire TV Stick via HDMI-CEC. Avec le Fire TV à l'écran, appuyez sur les flèches et OK avec la télécommande de la TV. Si rien ne se passe, activez le CEC dans les réglages de la TV (Anynet+ chez Samsung, SIMPLINK chez LG, BRAVIA Sync chez Sony) et sur le Fire TV, dans les réglages d'affichage et de son (« Display & Sounds »), l'option de contrôle des appareils HDMI CEC."),
      ('Si vous avez déménagé ou changé de Wi-Fi', "Sans télécommande, vous ne pouvez pas saisir le nouveau mot de passe Wi-Fi sur le Fire TV, mais il y a une solution : sur un deuxième téléphone, créez un point d'accès avec exactement le même nom et mot de passe que votre ancien Wi-Fi. Le Fire TV s'y connecte automatiquement. Connectez le téléphone avec Mando TV à ce point d'accès, appairez-le avec le PIN, puis allez dans Paramètres > Réseau sur le Fire TV pour choisir votre nouveau Wi-Fi. Enfin, connectez aussi votre téléphone au nouveau Wi-Fi."),
      ('Appairer une télécommande de remplacement', "La plupart des nouvelles télécommandes Fire TV s'appairent en maintenant le bouton Accueil enfoncé environ 10 secondes près du Fire TV. Si cela ne fonctionne pas, ouvrez Paramètres > Manettes et appareils Bluetooth > Télécommandes Amazon Fire TV > Ajouter une nouvelle télécommande. Vous pouvez accéder à ce menu depuis votre téléphone avec Mando TV."),
      ('Fire TV intégré dans la TV', 'Sur les TV avec Fire TV intégré, les mêmes étapes fonctionnent car la TV est le Fire TV.'),
      ('Avant de commencer', "Fire TV est arrivé récemment dans Mando TV : mettez d'abord l'application à jour. Si votre modèle ne se comporte pas correctement, contactez-nous depuis la [page d'aide](@soporte) en indiquant le nom du modèle."),
      ('Gratuit et Pro', 'La télécommande est gratuite à télécharger et à utiliser, sans pub ni abonnement. Mando TV Pro est un achat unique facultatif pour des fonctionnalités supplémentaires.'),
    ],
    marca=('firetv', 'Télécommande Fire TV'),
    faq=[
      ('Puis-je contrôler un Fire TV Stick avec mon téléphone sans la télécommande ?', "Oui, si le Fire TV est allumé et connecté au Wi-Fi. Mando TV s'appaire avec le code PIN à 4 chiffres affiché à l'écran, donc vous n'avez jamais besoin de l'ancienne télécommande."),
      ('Cela fonctionne-t-il si le Fire TV est sur un nouveau réseau Wi-Fi ?', "Pas directement, car le téléphone et le Fire TV doivent être sur le même réseau. Rétablissez d'abord la connexion du Fire TV avec l'astuce du point d'accès décrite sur cette page."),
      ("Ai-je besoin de l'application Amazon Fire TV ou d'un compte Amazon ?", 'Non. Mando TV se connecte au Fire TV via votre réseau domestique avec le PIN et ne nécessite aucun compte.'),
    ]),
  dict(clave='turn-on', corto='Allumer la TV sans télécommande', fecha='2026-11-23',
    titulo='Comment allumer une TV sans la télécommande (toutes marques)',
    desc="Où se trouve le bouton d'alimentation sur les TV Samsung, LG, TCL, Hisense et Sony. Astuces HDMI-CEC et Wi-Fi pour allumer votre TV.",
    h1='Comment allumer une TV sans la télécommande',
    intro="Presque toutes les TV ont encore un bouton d'alimentation physique, simplement bien caché. Voici où le trouver par marque, puis deux méthodes pour éviter de chercher la prochaine fois : le HDMI-CEC depuis une console ou un lecteur de streaming, et l'allumage via votre téléphone sur le Wi-Fi.",
    pasos=[
      "Regardez sous le centre de l'écran, juste derrière le logo. Beaucoup de TV ont un petit bouton ou un joystick orienté vers le bas à cet endroit.",
      "S'il n'est pas là, passez la main au dos de la TV près des coins inférieurs, puis les bords gauche et droit.",
      "Appuyez une fois sur le bouton. Sur beaucoup de TV à bouton unique, une fois la TV allumée, une courte pression ouvre un petit menu pour la source et le volume, et une longue pression éteint l'appareil.",
      "Toujours rien ? Vérifiez le câble d'alimentation aux deux extrémités et essayez une autre prise murale. Si le voyant de veille reste éteint, la TV ne reçoit pas de courant.",
      "Une fois la TV allumée, configurez-la pour ne plus avoir besoin du bouton : activez le HDMI-CEC et l'allumage par réseau, expliqués ci-dessous.",
    ],
    extra=[
      ("Où se trouve le bouton d'alimentation par marque", "Samsung : un bouton de contrôle ou un joystick sous le centre de l'écran, ou à l'arrière sur un coin inférieur. LG : un joystick sous le logo LG sur la plupart des modèles. TCL et Hisense : généralement un petit bouton sous le milieu de l'écran ou à l'arrière près d'un coin inférieur. Sony : à l'arrière ou sur un bord latéral, près du bas. L'emplacement varie selon le modèle ; si vous ne le trouvez pas, consultez le manuel avec le numéro de modèle au dos."),
      ('Allumer la TV depuis une console ou un lecteur de streaming (HDMI-CEC)', "Avec le HDMI-CEC activé, l'allumage d'une PlayStation, d'une Xbox, d'un lecteur Roku, d'un Fire TV Stick ou d'un Chromecast allume aussi la TV et passe sur la bonne entrée. Chaque marque nomme ce réglage différemment : Anynet+ chez Samsung, SIMPLINK chez LG, BRAVIA Sync chez Sony, et CEC pour la plupart des autres. Plus de détails dans [Allumer la TV et passer à l'entrée HDMI de votre console](@console)."),
      ('Allumer la TV depuis votre téléphone', "Les Smart TV peuvent se réveiller via le Wi-Fi si vous l'autorisez une fois, puis Mando TV les allume. Sur Samsung, activez « Allumer avec un appareil mobile » dans Paramètres > Général > Réseau > Paramètres d'expert. Sur LG, activez « Téléviseur en marche avec mobile » ([pas à pas](@lg-on)). Sur une Roku TV, activez « Démarrage rapide de la TV » dans Paramètres > Système > Alimentation. Sur Google TV et Android TV, cherchez Wake on LAN ou l'allumage par réseau, si votre modèle le propose. Vous faites cela une fois, TV allumée."),
      ('Si vous ne trouvez aucun bouton', "Certaines TV récentes cachent tellement bien le seul bouton qu'il semble inexistant. Cherchez un petit renflement ou une zone de capteur lumineux sous l'écran : le bouton est souvent juste à côté. En Wi-Fi, Mando TV a besoin que la TV ait été allumée et connectée au moins une fois. L'infrarouge est l'exception : sur un téléphone Android avec émetteur infrarouge, Mando TV peut allumer une TV jamais configurée, tant que vous pointez le téléphone vers la TV. L'infrarouge est nouveau et fonctionne avec les marques de la liste de codes de l'appli."),
      ('Gratuit et Pro', 'La télécommande est gratuite à télécharger et à utiliser, sans publicité ni abonnement. Mando TV Pro est un achat unique facultatif pour des fonctions supplémentaires.'),
    ],
    marca=None,
    faq=[
      ("Puis-je allumer la TV avec mon téléphone si je ne l'ai jamais configurée ?", "Pas en Wi-Fi. Une TV éteinte ne se réveille par le réseau que si l'allumage par réseau était activé au préalable. La première fois, utilisez le bouton de la TV. L'exception est un téléphone Android avec émetteur infrarouge : Mando TV peut allumer une TV par infrarouge sans configuration, si la marque est dans sa liste ou si vous choisissez « Autre marque ou je ne sais pas »."),
      ('Comment allumer une TV Samsung sans la télécommande ?', "Appuyez sur le bouton de contrôle sous le centre de l'écran ou à l'arrière sur un coin inférieur. Puis activez « Allumer avec un appareil mobile » pour que votre téléphone puisse l'allumer la prochaine fois."),
      ('Comment allumer une Roku TV sans la télécommande ?', "Utilisez le bouton de la TV, généralement sous le centre ou à l'arrière. Puis activez « Démarrage rapide de la TV » dans Paramètres > Système > Alimentation pour que Mando TV puisse l'allumer depuis votre téléphone."),
      ("Pourquoi ma TV s'allume-t-elle toute seule quand j'allume la console ?", "C'est le HDMI-CEC. C'est pratique, et vous pouvez le désactiver dans les réglages de la TV si vous préférez."),
    ]),
  dict(clave='sony', corto='Télécommande Sony', fecha='2026-11-23',
    titulo='Appli télécommande Sony pour iPhone, Android et PC',
    desc='Mando TV contrôle les TV Sony Bravia sous Google TV ou Android TV en Wi-Fi, et en bêta les Bravia de 2013 à 2015 sans Android.',
    h1='Appli télécommande Sony pour votre téléphone',
    intro='Les Smart TV Sony Bravia utilisent Google TV sur les modèles récents et Android TV sur les plus anciens, depuis 2015. Mando TV contrôle les deux depuis un iPhone, un téléphone Android ou un PC Windows par le Wi-Fi de la maison, utile quand la télécommande est perdue ou à plat.',
    pasos=[
      "Vérifiez que votre Sony affiche l'écran d'accueil Google TV ou Android TV. C'est le cas de la plupart des Smart TV Bravia depuis 2015.",
      'Connectez votre téléphone et la TV au même réseau Wi-Fi.',
      'Ouvrez Mando TV et touchez votre Sony dans la liste.',
      "Saisissez le code à 6 caractères affiché sur l'écran de la TV (une seule fois). Vous n'avez pas besoin de la télécommande pour cela.",
      'Utilisez les touches directionnelles, OK, Retour, Accueil, le volume et le clavier.',
    ],
    extra=[
      ('Allumer une Sony depuis votre téléphone', "Les modèles Sony sous Google TV et Android TV peuvent se réveiller par le réseau quand « Démarrage à distance » est activé. Il se trouve généralement dans Paramètres > Réseau et Internet > Démarrage à distance, mais le chemin varie selon le modèle. Touchez ensuite la TV dans Mando TV quand elle est éteinte pour l'allumer."),
      ("Où se trouve le bouton d'alimentation sur une Sony", "Sur la plupart des Bravia, il est à l'arrière, près du coin inférieur gauche ou droit, ou sur un côté. Une pression courte allume la TV. Plus de détails dans [Allumer une TV sans télécommande](@turn-on)."),
      ('Anciennes TV Sony', "Les Sony Bravia de 2013 à 2015 sans Android sont en bêta dans Mando TV. C'est nouveau, donc des imperfections peuvent subsister. La TV affiche un code PIN à 4 chiffres à saisir dans l'application. Les autres Sony sans Google TV ou Android TV ne sont pas couvertes aujourd'hui."),
      ('Gratuit et Pro', "La télécommande est gratuite au téléchargement et à l'utilisation, sans pub ni abonnement. Mando TV Pro est un achat unique facultatif pour des fonctions supplémentaires."),
    ],
    marca='android',
    faq=[
      ('Mando TV fonctionne-t-elle avec les Sony Bravia ?', 'Oui, avec les Sony sous Google TV ou Android TV, ce qui couvre la plupart des Smart TV Sony depuis 2015.'),
      ("Ai-je besoin d'une appli Sony ou d'un compte Google ?", "Non. Mando TV s'appaire via le code affiché sur l'écran de la TV et ne demande aucun compte."),
      ('Cela fonctionne-t-il avec les anciennes Sony Bravia sans Android ?', "En bêta, oui, sur les modèles Bravia de 2013 à 2015 sans Android. L'appairage se fait via un code PIN à 4 chiffres affiché sur la TV."),
      ('Puis-je taper du texte sur ma Sony depuis mon téléphone ?', 'Oui. Le clavier est gratuit et fonctionne dans YouTube, Netflix et la barre de recherche de la TV.'),
    ]),
  dict(clave='tcl', corto='Télécommande TCL', fecha='2026-11-23',
    titulo='Appli télécommande TCL pour iPhone, Android et PC',
    desc='Télécommande TCL perdue\xa0? La plupart des TV TCL sont sous Roku TV ou Google TV. Mando TV les contrôle en Wi-Fi depuis le téléphone. Gratuit, sans pub.',
    h1='Appli télécommande TCL pour votre téléphone',
    intro='TCL fabrique la TV, mais le logiciel est Roku TV ou Google TV (Android TV sur les modèles plus anciens). Mando TV contrôle ces deux systèmes et sert de télécommande TCL depuis votre téléphone ou PC via le Wi-Fi. Gratuit, sans compte, sans pub.',
    pasos=[
      "Vérifiez le système de votre TCL. Si l'accueil est une grille simple de vignettes de chaînes, c'est Roku TV. Si cela ressemble à Google TV ou Android TV avec des rangées de recommandations, c'est Google TV.",
      'Connectez votre téléphone et la TV TCL au même réseau Wi-Fi.',
      'Ouvrez Mando TV. La TCL apparaît toute seule dans la liste. Touchez-la.',
      "Sur une TCL sous Roku TV, rien d'autre n'est nécessaire. Sur une TCL sous Google TV, saisissez le code à 6 caractères affiché à l'écran (une seule fois).",
      "Utilisez les touches directionnelles, OK, Retour, Accueil, le volume et le clavier. Allumez la TV depuis l'application si vous avez activé l'allumage par réseau (voir ci-dessous).",
    ],
    extra=[
      ('Allumer une TV TCL depuis le téléphone', "Sur les TCL sous Roku TV, activez « Démarrage rapide de la TV » dans Paramètres > Système > Alimentation. Sur les TCL sous Google TV, cherchez Wake on LAN, « Allumer par réseau » ou démarrage à distance dans les paramètres réseau ou d'alimentation. Certains modèles ne proposent pas cette option. Dans ce cas, allumez la TV avec le bouton physique, généralement en bas au centre ou à l'arrière."),
      ("Si votre TCL n'apparaît pas", 'Vérifiez que votre téléphone et la TV sont sur le même réseau Wi-Fi. Les routeurs séparant les réseaux 2,4 GHz et 5 GHz peuvent masquer les appareils entre eux. Sur un iPhone, autorisez « Réseau local » pour Mando TV dans Réglages. Vous pouvez aussi ajouter la TV en saisissant son adresse IP. Lisez [Votre téléphone ne trouve pas la TV](@not-found).'),
      ('Plus de détails pour votre TCL', 'Pour une TCL sous Roku TV, voir [application télécommande Roku](@roku). Pour une TCL sous Google TV ou Android TV, voir [application télécommande Android TV](@android).'),
      ('Gratuit et Pro', "Les flèches, OK, Retour, Accueil, le volume, les chaînes, les chiffres, le clavier, l'ouverture d'applications, le changement d'entrée et l'allumage ou l'extinction sont gratuits, sans pub ni abonnement. Mando TV Pro est un achat unique facultatif pour des fonctionnalités supplémentaires."),
    ],
    marca=None,
    faq=[
      ('Mando TV fonctionne-t-elle avec toutes les TCL ?', "Elle fonctionne avec les TV TCL sous Roku TV, Google TV ou Android TV, ce qui couvre la plupart des Smart TV TCL. Une TCL qui n'est pas une Smart TV ne peut pas être contrôlée par Wi-Fi."),
      ("Ai-je besoin de l'application TCL ou d'un compte ?", 'Non. Mando TV se connecte directement par le Wi-Fi de la maison et ne nécessite aucun compte.'),
      ('Ma TCL demande un code. Où est-il ?', "Les modèles TCL sous Google TV et Android TV affichent un code à 6 caractères à l'écran. Saisissez-le dans Mando TV exactement comme il s'affiche. La TCL sous Roku TV ne demande pas de code."),
    ]),
  dict(clave='hisense', corto='Télécommande Hisense', fecha='2026-11-23',
    titulo='Appli télécommande Hisense : ce qui marche sur téléphone',
    desc='Mando TV contrôle les TV Hisense sous VIDAA, Roku TV, Google TV ou Fire TV par Wi-Fi. Guide honnête sur ce qui marche et les limites.',
    h1='Appli télécommande Hisense : ce qui marche ou pas',
    intro="Les TV Hisense n'ont pas toutes le même système interne. Selon le modèle, elles fonctionnent sous VIDAA (le système Hisense), Roku TV, Google TV ou Fire TV. Mando TV agit comme télécommande pour les quatre, avec une exception sur certains modèles VIDAA récents. Voici comment identifier votre système et ce à quoi vous attendre.",
    pasos=[
      "Vérifiez le système de votre TV Hisense. VIDAA est l'interface propre à Hisense. Roku TV affiche une grille de vignettes de chaînes. Google TV montre des rangées de recommandations. Fire TV affiche l'écran d'accueil Fire TV avec des rangées Amazon.",
      'Connectez votre téléphone et la TV Hisense au même réseau Wi-Fi.',
      'Ouvrez Mando TV. La TV apparaît seule dans la liste. Touchez-la.',
      "Les modèles VIDAA et Fire TV peuvent afficher un code PIN à 4 chiffres ; Google TV affiche un code de 6 caractères. Saisissez-le dans l'application. Roku TV ne demande rien. Cette étape ne se fait qu'une fois.",
      'Utilisez les flèches, OK, Retour, Accueil, le volume et le clavier depuis votre téléphone.',
    ],
    extra=[
      ('Hisense avec Roku TV ou Google TV', "Elles fonctionnent pleinement comme n'importe quelle autre TV Roku ou Google TV. Consultez les pages [application télécommande Roku](@roku) et [application télécommande Android TV](@android) pour les détails."),
      ('Hisense avec Fire TV', "La prise en charge de Fire TV est nouvelle dans Mando TV. Mettez à jour l'application vers la dernière version depuis votre boutique, et consultez la page [appli télécommande Fire TV](@firetv) pour comprendre l'appairage par code PIN. Si quelque chose ne se comporte pas normalement, écrivez-nous depuis la page d'aide en indiquant votre modèle."),
      ('Hisense avec VIDAA', "La plupart des modèles VIDAA fonctionnent : boutons, volume, clavier, applications et entrées. Certains modèles VIDAA récents n'acceptent que l'application officielle de Hisense. Mando TV le détecte lors de la connexion et vous l'indique clairement, au lieu d'échouer silencieusement. Dans ce cas, utilisez l'application Hisense pour votre modèle, les boutons physiques de la TV ou la télécommande d'origine."),
      ('Allumer une Hisense depuis le téléphone', "Sur une Hisense Roku TV, activez « Démarrage rapide de la TV » dans Paramètres > Système > Alimentation. Sur Google TV, cherchez une option « Wake on LAN » ou « Allumer via le réseau ». Si aucune n'existe, utilisez le bouton d'alimentation physique de la TV."),
      ('Gratuit et Pro', "Les flèches, OK, Retour, Accueil, volume, chaînes, touches numériques, clavier, ouverture d'applications, changement d'entrées et allumage et extinction sont gratuits, sans publicité ni abonnement. Mando TV Pro est un achat unique facultatif pour les fonctionnalités supplémentaires."),
    ],
    marca=None,
    faq=[
      ('Mando TV fonctionne-t-elle avec Hisense VIDAA ?', "Oui, avec la plupart des modèles VIDAA. Certains récents n'acceptent que l'application officielle de Hisense ; Mando TV le détecte et vous l'indique. Les TV Hisense sous Roku TV, Google TV ou Fire TV sont également prises en charge."),
      ('Comment savoir si ma Hisense est Roku TV, Google TV ou Fire TV ?', "Regardez l'écran d'accueil. Roku TV affiche une grille simple de vignettes et un logo Roku au démarrage. Google TV montre des rangées de recommandations. Fire TV présente l'écran d'accueil Amazon Fire TV. Le nom du modèle dans Paramètres > À propos vous renseigne également."),
      ("Ai-je besoin d'un compte Hisense ou Google ?", 'Non. Mando TV se connecte directement par le Wi-Fi de la maison et ne nécessite aucun compte.'),
    ]),
  dict(clave='philips', corto='Télécommande Philips', fecha='2026-11-23',
    titulo='Appli télécommande Philips : Roku TV, Google TV, Android TV',
    desc='Mando TV contrôle les TV Philips sous Roku TV, Google TV ou Android TV en Wi-Fi, depuis votre téléphone ou PC. Et une note honnête sur Titan OS.',
    h1='Appli télécommande Philips pour votre téléphone',
    intro="Les TV Philips utilisent différents systèmes selon le pays et l'année : Roku TV aux États-Unis, Google TV ou Android TV dans de nombreux pays, et Titan OS sur certains modèles européens récents. Mando TV contrôle les modèles sous Roku TV, Google TV et Android TV depuis votre téléphone ou PC via le Wi-Fi.",
    pasos=[
      "Vérifiez l'écran d'accueil. Roku TV affiche une grille de vignettes. Google TV et Android TV affichent des rangées de recommandations Google. Titan OS a son propre écran d'accueil.",
      'Connectez votre téléphone et la TV au même réseau Wi-Fi.',
      'Ouvrez Mando TV et touchez votre Philips dans la liste.',
      "Une Roku TV ne demande rien. Google TV et Android TV affichent un code à 6 caractères : saisissez-le dans l'application une fois.",
      'Utilisez les touches directionnelles, OK, Retour, Accueil, le volume et le clavier.',
    ],
    extra=[
      ('Philips sous Roku TV', "Fonctionne comme n'importe quelle Roku TV. Pour l'allumer depuis votre téléphone, activez « Démarrage rapide de la TV » dans Paramètres > Système > Alimentation. Plus de détails sur la page [application télécommande Roku](@roku)."),
      ('Philips sous Google TV ou Android TV', "Inclut de nombreux modèles Ambilight. Ils s'appairent avec le code affiché à l'écran. Pour les allumer depuis votre téléphone, cherchez Wake on LAN ou « Allumer via le réseau » dans les paramètres réseau ou d'alimentation. Certains modèles ne l'ont pas. Plus de détails sur la page [application télécommande Android TV](@android)."),
      ('Anciens Philips sans Android', "Les TV Philips de 2011 à 2015 qui ne tournent pas sous Android sont prises en charge en bêta dans Mando TV. C'est nouveau, et aucun code d'appairage n'est nécessaire."),
      ('Philips sous Titan OS', "Titan OS est un système différent que Mando TV ne contrôle pas aujourd'hui, et nous préférons le dire clairement. Les nouveaux modèles Philips sans Android ne sont pas non plus pris en charge."),
      ('Gratuit et Pro', 'La télécommande est gratuite à télécharger et à utiliser, sans publicité ni abonnement. Mando TV Pro est un achat unique facultatif pour des fonctionnalités supplémentaires.'),
    ],
    marca=None,
    faq=[
      ('Mando TV fonctionne-t-elle avec les TV Philips ?', 'Avec les TV Philips sous Roku TV, Google TV ou Android TV, oui, et en bêta avec les TV Philips de 2011 à 2015 sans Android. Les modèles sous Titan OS ne sont pas pris en charge.'),
      ('Contrôle-t-elle Ambilight ?', 'Mando TV est une télécommande : elle envoie les touches, donc vous pouvez accéder aux paramètres Ambilight avec les flèches et OK. Elle ne dispose pas de contrôles Ambilight séparés.'),
      ("Ai-je besoin d'un compte Philips ou Google ?", "Non. Mando TV se connecte via le Wi-Fi de la maison et n'a pas besoin de compte."),
    ]),
]
OTRAS_GUIAS += [
  ('no-sub', 'Une appli télécommande TV sans abonnement ni publicité'),
  ('roku-app-alt', "Alternative à l'appli Roku : une seule télécommande"),
  ('lg-thinq', 'Alternative à LG ThinQ comme télécommande de votre TV LG'),
  ('smartthings', 'Alternative à SmartThings pour les TV Samsung'),
  ('googletv-alt', 'Alternative à la télécommande Google TV sur téléphone'),
  ('windows', 'Appli télécommande TV pour PC Windows'),
  ('iphone', 'Télécommande TV sur iPhone : une seule pour toutes les TV'),
  ('firetv', 'Appli télécommande Fire TV sur téléphone ou PC'),
  ('firetv-lost', 'Télécommande Fire TV perdue : utilisez votre téléphone'),
  ('turn-on', 'Comment allumer une TV sans la télécommande'),
  ('sony', 'Appli télécommande Sony pour votre téléphone'),
  ('tcl', 'Appli télécommande TCL pour votre téléphone'),
  ('hisense', 'Appli télécommande Hisense : ce qui marche ou pas'),
  ('philips', 'Appli télécommande Philips pour votre téléphone'),
]
# <<< guías traídas del inglés
