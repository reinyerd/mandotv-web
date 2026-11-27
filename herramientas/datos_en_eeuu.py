# Guías en inglés para búsquedas de EE. UU. (solo en inglés, sin gemelas en otros idiomas).
# Las usa generar_en.py (se añaden a GUIAS); las rutas viven en idiomas_sitio.py.
# Hechos comprobados contra el código de la app (C:\server\htdocs\control):
#   - Marcas con driver: LG webOS, Samsung (Tizen y 2010-2015), Roku, Android TV / Google TV, Fire TV (PIN de 4 dígitos,
#     lib/drivers/fire_tv.dart, desde la 1.0.8) y Hisense VIDAA (lib/drivers/vidaa.dart, publicado desde la 1.0.9:
#     "la mayoría de los modelos; algunos VIDAA recientes solo aceptan la app oficial de Hisense y la app lo avisa").
#   - Vizio SmartCast: beta desde la 1.0.12 (PIN de 4 dígitos, 2016 en adelante). TCL: solo se dicen las plataformas ya publicadas.
#   - Gratis y Pro: docs/PRO.md y funcionesProPorDefecto en lib/core/licencia.dart.
# Fire TV sale en la app 1.0.8. Poner True SOLO cuando la 1.0.8 esté publicada en las tiendas y volver a generar
# (python -I herramientas/generar_en.py .). Con False no se genera la guía de Fire TV ni se promete en ninguna página.
FIRE_TV_PUBLICADO = True

FREE_PRO = ('The arrows, OK, Back, Home, volume, channels, number keys, keyboard, opening apps, switching inputs and power on or off are free. '
            'The touchpad, voice commands, favorite apps, routines and the sleep timer are part of Mando TV Pro, '
            'a one-time purchase with no subscription.')

GUIAS_EEUU = [
  dict(clave='lg-thinq', corto='LG ThinQ app alternative',
    titulo='LG ThinQ App Alternative: LG TV Remote, No Account',
    desc='Looking for an LG ThinQ alternative just to use as an LG TV remote? Mando TV controls LG webOS TVs over Wi-Fi with no LG account and no ads.',
    h1='LG ThinQ App Alternative for Your LG TV Remote',
    intro='LG ThinQ is LG\'s official app, built to run a whole smart home: appliances, the TV and more. If all you want is a clean remote for your LG TV, Mando TV does that one job over your home Wi-Fi, with no LG account to create and no ads.',
    pasos=[
      'Connect your phone (iPhone, Android or Windows PC) and your LG TV to the same Wi-Fi network.',
      'Download Mando TV and open it. Your LG TV shows up in the list on its own. Tap it.',
      'A permission prompt appears on the TV screen. Accept it once with the TV remote, the joystick under the screen or the Magic Remote.',
      'Use the buttons, the volume and the keyboard right away. No LG account and no TV registration are needed.',
      'Optional: turn on "TV On With Mobile" in the TV settings so you can also switch the TV on from your phone.',
    ],
    extra=[
      ('Mando TV vs LG ThinQ, in plain terms', 'Use ThinQ if you want to manage LG appliances such as a washer, a fridge or an air conditioner, or LG account features. Use Mando TV if you want a fast, simple remote for the TV that also works for Samsung, Roku and Google TV in the same app. Many people keep both: ThinQ for appliances, Mando TV for the TV.'),
      ('What Mando TV does on an LG TV', 'It works with LG smart TVs running webOS, which covers most LG smart TV models since 2014, including LED, NanoCell, QNED and OLED. It gives you the d-pad, OK, Back, Home, volume, channels, mute, playback controls and a keyboard for typing in the TV search and in most apps. The apps list and the inputs list are free too. With Pro you also get a pointer like the Magic Remote.'),
      ('What Mando TV does not do', 'It does not control LG appliances, it does not use your LG account and it does not replace the LG account services on the TV. It is a remote, not a smart home hub.'),
      ('Privacy and ads', 'Mando TV has no ads and no account. It talks to the TV inside your home network and keeps the TV connection key encrypted on your own device. The [LG TV remote page](/lg-tv-remote/) has the full list of features.'),
      ('What is free and what is Pro', FREE_PRO),
    ],
    marca=('/lg-tv-remote/', 'LG TV remote app'),
    faq=[
      ('Can I control my LG TV without the LG ThinQ app?', 'Yes. Mando TV connects to LG webOS TVs directly over your Wi-Fi. You accept one prompt on the TV the first time and that is it, with no LG account.'),
      ('Does Mando TV work with the LG Magic Remote pointer?', 'Mando TV Pro has a pointer you move with your finger on the phone screen, similar to how the Magic Remote moves the arrow.'),
      ('Is Mando TV made by LG?', 'No. Mando TV is an independent app and is not affiliated with LG. LG and ThinQ belong to their owners and are named only to describe compatibility.'),
    ]),

  dict(clave='roku-app-alt', corto='Roku app alternative',
    titulo='Roku Mobile App Alternative: A Simple Roku Remote',
    desc='A Roku mobile app alternative for the remote: Mando TV controls Roku TVs and players over Wi-Fi. No account, no ads, plus Samsung, LG and Google TV.',
    h1='Roku Mobile App Alternative: One Remote for Every TV',
    intro='The official Roku mobile app does a lot: channel store, casting, private listening and a remote. If you only want a fast remote, or you also have a Samsung, LG or Google TV in the house, Mando TV is a simple alternative that controls Roku over your Wi-Fi with no account.',
    pasos=[
      'Connect your phone and the Roku to the same Wi-Fi network.',
      'Download Mando TV and open it. Your Roku TV or Roku player shows up in the list. Tap it. Roku does not ask for a code.',
      'Use the d-pad, OK, Back, Home, volume and the keyboard. Type searches in Roku channels with your phone keyboard.',
      'If the buttons do nothing, on the Roku go to Settings, System, Advanced system settings, Control by mobile apps, and set network access to Default or Permissive (on newer Roku software, set Control by mobile apps to Enabled).',
      'Optional: on a Roku TV, turn on Fast TV start under Settings, System, Power so Mando TV can switch the TV on.',
    ],
    extra=[
      ('Where Mando TV fits better', 'One app for several TVs: Roku, Samsung, LG and Google TV or Android TV. No account, no ads. It also works from a Windows PC, which is handy at a desk. The d-pad and volume feel quick, and the keyboard makes typing a search painless.'),
      ('Where the official Roku app is better', 'Keep the Roku app for what it offers beyond the remote, such as browsing and adding channels from the Roku Channel Store and its own casting and private listening features. Use both if you like. They can run on the same phone.'),
      ('Roku TV sets and Roku players', 'Both work. That includes Roku TV models from TCL, Hisense, Philips and others, and Roku Express, Streaming Stick and Ultra. Details are on the [Roku remote app page](/roku-remote/).'),
      ('If the Roku app stopped working', 'If the buttons stopped responding, the Roku is usually blocking control by apps. The guide [Roku remote app not working](/guides/roku-remote-app-not-working/) walks through the setting that fixes it.'),
      ('What is free and what is Pro', FREE_PRO),
    ],
    marca=('/roku-remote/', 'Roku remote app'),
    faq=[
      ('Do I need a Roku account to use Mando TV?', 'No. Mando TV talks to the Roku over your home network and does not ask for an account.'),
      ('Does Mando TV replace the Roku mobile app completely?', 'For the remote, yes. For the channel store, casting and private listening, keep the official Roku app.'),
      ('Will it work on my Roku Express or Streaming Stick?', 'Yes. All Roku players and Roku TV sets are controlled the same way.'),
    ]),

  dict(clave='tcl', corto='TCL TV remote app',
    titulo='TCL TV Remote App for iPhone, Android and PC',
    desc='Lost your TCL TV remote? Most TCL TVs run Roku TV or Google TV, and Mando TV controls both over Wi-Fi from your phone. No account, no ads.',
    h1='TCL TV Remote App for Your Phone',
    intro='TCL makes the TV, but the software on it is Roku TV or Google TV (Android TV on older sets). Mando TV controls both, so it works as a TCL TV remote app from your phone or PC over your home Wi-Fi. Free, no account, no ads.',
    pasos=[
      'Find out which system your TCL runs. If the home screen is a simple grid of channel tiles, it is Roku TV. If it looks like Google TV or Android TV with rows of recommendations, it is Google TV.',
      'Connect your phone and the TCL TV to the same Wi-Fi network.',
      'Open Mando TV. The TCL shows up in the list on its own. Tap it.',
      'On a TCL with Roku TV, nothing else is needed. On a TCL with Google TV, type the 6-character code the TV shows on the screen (first time only).',
      'Use the d-pad, OK, Back, Home, volume and keyboard. Turn the TV on from the app if you enabled power-on over the network (see below).',
    ],
    extra=[
      ('Turn on a TCL TV from your phone', 'On TCL Roku TV, turn on Fast TV start under Settings, System, Power. On TCL Google TV, look for a Wake on LAN, "Turn on over network" or remote start option in the network or power settings. Some models do not offer it. In that case turn the TV on with the physical power button, usually on the bottom center or on the back.'),
      ('If your TCL does not show up', 'Check that your phone and the TV are on the same Wi-Fi network. Routers with separate 2.4 GHz and 5 GHz networks can hide devices from each other. On an iPhone, allow Local Network for Mando TV in Settings. You can also add the TV by typing its IP address. See [your phone cannot find the TV](/guides/phone-cant-find-tv/).'),
      ('Brand pages for your TCL', 'Setup details are on the [Roku remote app page](/roku-remote/) for TCL Roku TV and the [Android TV remote app page](/android-tv-remote/) for TCL Google TV and Android TV.'),
      ('What is free and what is Pro', FREE_PRO),
    ],
    faq=[
      ('Does Mando TV work with every TCL TV?', 'It works with TCL TVs that run Roku TV or Google TV or Android TV, which is most TCL smart TVs sold in the US. A TCL that is not a smart TV cannot be controlled over Wi-Fi.'),
      ('Do I need the TCL app or a TCL account?', 'No. Mando TV connects directly over your home Wi-Fi and needs no account of any kind.'),
      ('My TCL asks for a code. Where is it?', 'TCL Google TV and Android TV models show a 6-character code on the TV screen. Type it into Mando TV exactly as it appears. TCL Roku TV does not ask for a code.'),
    ]),

  dict(clave='hisense', corto='Hisense TV remote app',
    titulo='Hisense TV Remote App: What Works From Your Phone',
    desc='Hisense TV remote app: Mando TV controls Hisense TVs with VIDAA, Roku TV, Google TV or Fire TV from your phone over Wi-Fi. An honest guide to what works.',
    h1='Hisense TV Remote App: What Works and What Does Not',
    intro='Hisense TVs are not all the same inside. Depending on the model, they run Hisense\'s own VIDAA system, Roku TV, Google TV or Fire TV. Mando TV works as a Hisense TV remote app on all four, with one exception on some recent VIDAA models. Here is how to tell which one you have and what to expect.',
    pasos=[
      'Check which system your Hisense runs. VIDAA is Hisense\'s own interface. Roku TV has a grid of channel tiles. Google TV shows rows of recommendations. Fire TV shows the Fire TV home screen with Amazon rows.',
      'Connect your phone and the Hisense TV to the same Wi-Fi network.',
      'Open Mando TV. The TV shows up in the list on its own. Tap it.',
      'VIDAA and Fire TV models may show a 4-digit PIN; Google TV shows a 6-character code. Type it into the app. Roku TV asks for nothing. Do this once.',
      'Use the d-pad, OK, Back, Home, volume and keyboard from your phone.',
    ],
    extra=[
      ('Hisense with Roku TV or Google TV', 'These work fully like any other Roku or Google TV. See the [Roku remote app page](/roku-remote/) and the [Android TV remote app page](/android-tv-remote/) for the details of each.'),
      ('Hisense with Fire TV', 'Fire TV support is new in Mando TV. Update the app to the latest version from your store, and see the [Fire TV remote app page](/guides/fire-tv-remote-app/) for how the PIN pairing works. If something does not behave, write to us from the Help page and tell us your model.'),
      ('Hisense with VIDAA', 'Most VIDAA models work: buttons, volume, keyboard, apps and inputs. Some recent VIDAA models only accept Hisense\'s official app. Mando TV detects that when it connects and tells you plainly, instead of failing silently. In that case the Hisense app for your model, the buttons on the TV or the original remote are the way to go.'),
      ('Turn on a Hisense from your phone', 'On Hisense Roku TV, turn on Fast TV start under Settings, System, Power. On Google TV, look for a Wake on LAN or "Turn on over network" option. If neither exists, use the power button on the TV.'),
      ('What is free and what is Pro', FREE_PRO),
    ],
    faq=[
      ('Does Mando TV work with Hisense VIDAA?', 'Yes, with most VIDAA models. Some recent ones only accept Hisense\'s official app; Mando TV detects it and tells you. Hisense TVs with Roku TV, Google TV or Fire TV are supported too.'),
      ('How do I know if my Hisense is Roku TV, Google TV or Fire TV?', 'Look at the home screen. Roku TV has a plain grid of tiles and a Roku logo at start-up. Google TV has rows of recommendations. Fire TV has the Amazon Fire TV home screen. The model name in Settings, About also tells you.'),
      ('Do I need a Hisense or Google account?', 'No. Mando TV connects directly over your home Wi-Fi and has no account of its own.'),
    ]),

  dict(clave='vizio', corto='Vizio TV remote app',
    titulo='Vizio TV Remote App: Beta Support for SmartCast',
    desc='Vizio TV remote app: Mando TV now has beta support for Vizio SmartCast TVs from 2016 onward. Pair with a 4-digit PIN; turn on from standby with Quick Start.',
    h1='Vizio TV Remote App: Beta Support for SmartCast TVs',
    intro='Mando TV now has beta support for Vizio SmartCast TVs from 2016 onward. It is new, so it can still have rough edges, and we would rather say that plainly. Here is how to pair it, what to do if the Vizio will not turn on, and what else works when the remote is lost.',
    pasos=[
      'Turn the TV on with its physical power button if it is off. On most Vizio TVs it is on the back or under the screen, on the lower edge or a corner.',
      'Connect your phone and the Vizio to the same Wi-Fi network, then install Mando TV and open it.',
      'Pick your Vizio in the TV list. The TV shows a 4-digit PIN on its screen.',
      'Type that PIN into Mando TV. The pairing is saved, so you do not need the PIN again.',
      'Use the buttons, the volume and the keyboard from your phone. If the app cannot find the TV, restart the router and the TV and try again.',
    ],
    extra=[
      ('What beta means here', 'Vizio support is new and in beta. It covers SmartCast TVs from 2016 onward. Vizio TVs older than 2016 are not covered. If something does not behave, write to us from the Help page and tell us your model.'),
      ('Turning on a Vizio from standby', 'Mando TV can turn on a Vizio that is in standby, as long as Quick Start (also called quick power-on) is turned on in the TV settings. If the TV is fully off, use its physical power button.'),
      ('If you use a streaming stick', 'Many Vizio TVs have a Roku stick, a Fire TV stick or a Chromecast with Google TV plugged into an HDMI port. Mando TV controls the Roku, Fire TV and Google TV devices too, from the same app.'),
      ('Other ways to control a Vizio without the remote', 'Use the buttons on the TV, use the official Vizio phone app, or order a replacement remote that matches your model number, which is on the label on the back of the TV.'),
      ('If you own other TVs too', 'Mando TV is useful for the rest of the house: see the pages for [Samsung](/samsung-tv-remote/), [LG](/lg-tv-remote/), [Roku](/roku-remote/) and [Android TV](/android-tv-remote/).'),
    ],
    faq=[
      ('Does Mando TV work with Vizio TVs?', 'Yes, in beta, on Vizio SmartCast TVs from 2016 onward. It pairs with a 4-digit PIN shown on the TV. Vizio TVs older than 2016 are not covered.'),
      ('Can Mando TV turn on a Vizio?', 'Yes, if the TV is in standby and Quick Start (quick power-on) is on in the TV settings. A TV that is fully off needs its physical power button.'),
      ('What is the fastest way to control a Vizio TV with no remote?', 'Press the physical power button on the TV, then pair Mando TV with the PIN. The official Vizio phone app also works.'),
    ]),

  dict(clave='firetv', corto='Fire TV remote app',
    titulo='Fire TV Remote App for iPhone, Android and PC',
    desc='Fire TV remote app: control a Fire TV Stick, Cube or Fire TV Edition TV from your phone or PC over Wi-Fi with a 4-digit PIN. No Amazon app needed.',
    h1='Fire TV Remote App for Your Phone or PC',
    intro='If your Fire TV remote is lost or out of battery, Mando TV can control a Fire TV Stick, a Fire TV Cube or a TV with Fire TV built in from your phone or PC, over your home Wi-Fi. Pairing takes a 4-digit PIN. Fire TV support is new, so update the app first.',
    pasos=[
      'Update Mando TV to the latest version from the App Store, Microsoft Store or Google Play.',
      'Turn the Fire TV on and connect your phone to the same Wi-Fi network.',
      'Open Mando TV. Your Fire TV shows up in the list. Tap it.',
      'The TV screen shows a 4-digit PIN. Type it into Mando TV. You only do this once.',
      'Use the d-pad, OK, Back, Home, playback buttons and the keyboard to type searches.',
    ],
    extra=[
      ('Fire TV devices it is meant for', 'Fire TV Stick, Fire TV Stick 4K, Fire TV Cube and TVs with Fire TV built in, such as Amazon Fire TV Edition sets and some Hisense models. Support is new, and we have limited real-device testing. If something does not behave, tell us your model from the Help page.'),
      ('Turning on a Fire TV', 'Mando TV does not turn a Fire TV on over the network. Turn on the TV with its power button: a Fire TV Stick or Cube plugged into it usually wakes up with it through HDMI-CEC, and on a TV with Fire TV built in, the TV is the Fire TV. Then control it from your phone.'),
      ('If your Fire TV does not show up', 'Make sure both devices are on the same Wi-Fi network and that the Fire TV is awake. On an iPhone, allow Local Network for Mando TV in Settings. See [your phone cannot find the TV](/guides/phone-cant-find-tv/).'),
      ('No remote at all?', 'You need the Fire TV screen to show the PIN, so the TV and the Fire TV must be on and showing the picture. If the TV is on a wrong input, change it with the TV buttons. See [change the HDMI input without a remote](/guides/change-hdmi-input-without-remote/).'),
      ('What is free and what is Pro', FREE_PRO),
    ],
    faq=[
      ('Do I need the Amazon Fire TV app?', 'No. Mando TV connects to the Fire TV over your Wi-Fi with a PIN. You do not need an Amazon account on the phone.'),
      ('Does it work with Fire TV Edition TVs and Fire TV sticks?', 'Yes, that is what it was built for. Support is new, so keep the app updated and tell us about any model that does not behave.'),
      ('Why do I need a PIN?', 'The Fire TV shows a 4-digit PIN to prove you are in front of the TV. Nobody can pair without seeing the screen.'),
    ]),

  dict(clave='iphone', corto='TV remote app for iPhone',
    titulo='TV Remote App for iPhone: Samsung, LG, Roku, Google TV',
    desc='Use your iPhone as a TV remote for Samsung, LG, Roku, Google TV and Fire TV over Wi-Fi. Free on the App Store, no account and no ads.',
    h1='TV Remote App for iPhone: One Remote for Every TV',
    intro='Mando TV turns your iPhone or iPad into a TV remote for Samsung, LG, Roku, Google TV or Android TV, and Fire TV, over your home Wi-Fi. It is free on the App Store, with no account and no ads. It also works on Android and Windows.',
    pasos=[
      'Download Mando TV free from the App Store.',
      'Connect your iPhone and the TV to the same Wi-Fi network.',
      'Open Mando TV and tap Allow when iOS asks for Local Network access. The app needs it to find the TV.',
      'Tap your TV in the list. Accept the prompt on the TV screen if it asks (LG and Samsung), or type the code the TV shows (Google TV or Fire TV).',
      'Use the buttons, volume and the keyboard. You are connected.',
    ],
    extra=[
      ('Works with these TVs', 'LG webOS, Samsung Tizen (2016 and newer), Roku TV and Roku players, Google TV and Android TV, and Fire TV. The brand pages are [Samsung](/samsung-tv-remote/), [LG](/lg-tv-remote/), [Roku](/roku-remote/) and [Android TV](/android-tv-remote/).'),
      ('Why it asks for Local Network', 'iPhone blocks apps from seeing devices on your home network unless you allow it. If the TV is missing from the list, open Settings, Mando TV and turn on Local Network. The app only talks to your TV inside your home network.'),
      ('Why an iPhone and not the TV maker\'s app', 'Each TV brand has its own app, and each wants its own setup or account. Mando TV is one app for all of them, with no account.'),
      ('Free and Pro on iPhone', FREE_PRO + ' Pro is bought once inside the app, with no subscription.'),
    ],
    faq=[
      ('Is Mando TV free on iPhone?', 'The download is free, with no ads. The basic remote is free, and so are opening apps and switching inputs. Extras such as the touchpad, voice commands and routines are Mando TV Pro, a one-time purchase.'),
      ('Does it work on iPad?', 'Yes. The same app runs on iPhone and iPad.'),
      ('Does an iPhone remote app need Bluetooth or an infrared blaster?', 'Not on iPhone. iPhones have no infrared blaster, so infrared control is not available there, and the Bluetooth option is only for Android 9 or newer, not for iPhone. On iPhone, Mando TV controls smart TVs, and Apple TV in beta, over your home Wi-Fi.'),
    ]),

  dict(clave='windows', corto='TV remote app for Windows',
    titulo='TV Remote App for Windows PC: Control Your TV',
    desc='Control your Samsung, LG, Roku, Google TV or Fire TV from a Windows PC with Mando TV: keyboard shortcuts, a mini remote and Wi-Fi control. Microsoft Store.',
    h1='TV Remote App for Windows PC',
    # Video premium hecho con Remotion (23-nov) con pantallas reales de la app; el mismo está en / y en YouTube
    # (canal Mando TV): de ahí sale el embedUrl del VideoObject. MP4 propio de 720p, sin audio.
    video=dict(
      name='Mando TV in action: one remote for all your TVs',
      description='A 25-second tour of the Mando TV app, with no sound: turn the volume up, move through menus with the arrows and OK, type a search on the TV with the phone keyboard, switch inputs (Live TV, HDMI 1, HDMI 2), use it with LG, Samsung, Roku, Google TV, Fire TV, Hisense and more over Wi-Fi, and see what Free and Pro include. Mando TV is a free universal TV remote for iPhone, iPad, Android and Windows, with no ads and no account.',
      archivo='/media/mando-tv-in-action-en-720p.mp4', poster='/media/mando-tv-in-action-en.webp',
      miniatura='/media/mando-tv-in-action-en.jpg', youtube='RyhvFz0ZUDk', fecha='2026-11-23T03:35:00-03:00', duracion='PT25S',
      boton='Play · 0:25',
      texto='Mando TV in 25 seconds, no sound. The video shows the phone app; the Windows app has the same remote, and you type on the TV with your PC keyboard.'),
    intro='Mando TV has a Windows app that turns your PC or laptop into a TV remote over your home network. Type on the TV with your real keyboard, keep a small remote window on top while you work, and control Samsung, LG, Roku, Google TV or Fire TV from the same app.',
    pasos=[
      'Install Mando TV free from Microsoft Store on a Windows 10 or 11 PC.',
      'Make sure the PC and the TV are on the same network, over Wi-Fi or cable through the same router.',
      'Open Mando TV. The TV shows up in the list. Click it.',
      'Accept the prompt on the TV if it asks (LG, Samsung), or type the code it shows (Google TV, Fire TV).',
      'Click the buttons or type a search with your keyboard. Done.',
    ],
    extra=[
      ('Keyboard shortcuts (Pro)', 'With Pro, your PC keyboard becomes the remote: arrow keys to move, Enter for OK, Backspace or Esc to go back, plus and minus for volume, M to mute and Space to pause.'),
      ('Mini remote (Pro)', 'A small remote window that stays on top of other windows, so you can change the volume or pause without leaving what you are doing.'),
      ('Typing on the TV from the PC', 'The on-screen keyboard of a TV is slow. In Mando TV you type with your real keyboard and the text goes to the TV search box. That part is free.'),
      ('More details', 'For the step-by-step version see [how to control your TV from a Windows PC](/guides/control-tv-from-pc/). For phone-based control see [use your phone as a TV remote over Wi-Fi](/guides/connect-phone-to-tv-wifi/).'),
      ('What is free and what is Pro', FREE_PRO + ' On Windows, Pro is bought through Microsoft Store.'),
      ('Voice commands from the PC (Pro)', 'With Pro you can talk to the TV through the PC microphone. The voice is recognized on the PC itself: it needs no internet and no Windows settings to change. What you say never leaves the PC and is not stored. Only on very old processors does the app fall back to Windows voice typing, which needs "Online speech recognition" on in Settings > Privacy & security > Speech and your language added in Windows.'),
    ],
    faq=[
      ('Does the TV remote app for Windows need Bluetooth or a cable?', 'No. It uses your home network. The PC and the TV only have to be on the same router.'),
      ('Which TVs can I control from Windows?', 'Samsung Tizen TVs, LG webOS TVs, Roku TV and players, Google TV and Android TV, and Fire TV.'),
      ('Can I use my PC speakers or my screen to see the TV?', 'No. Mando TV is only a remote. It does not mirror or stream the TV picture to the computer.'),
      ('Why does voice not work on my Windows PC?', 'Voice is a Pro feature, so check that Pro is active and that the PC microphone works. On most PCs the voice is recognized on the PC itself, with no internet. Only on very old processors does the app use Windows voice typing: then turn on "Online speech recognition" in Settings > Privacy & security > Speech and add your language in Settings > Time & language.'),
    ]),
]


# Con Fire TV sin publicar: se quita la guía y toda promesa de control de Fire TV (los textos de arriba son los de True).
_CAMBIOS = {
  'hisense': [
    ("Roku TV, Google TV or Fire TV from your phone over Wi-Fi. Honest guide", "Roku TV or Google TV from your phone over Wi-Fi. Honest guide"),
    ("Mando TV works as a Hisense TV remote app on the first three.", "Mando TV works as a Hisense TV remote app on Roku TV and Google TV models."),
    (" Fire TV shows the Fire TV home screen with Amazon rows.", ""),
    (" Fire TV shows a 4-digit PIN to type into the app.", ""),
    ("Fire TV support is new in Mando TV. Update the app to the latest version from your store, and see the [Fire TV remote app page](/guides/fire-tv-remote-app/) for how the PIN pairing works. If something does not behave, write to us from the Help page and tell us your model.",
     "Fire TV support is coming in the next app update, so we do not claim it yet. Until then, a Hisense with Fire TV is controlled with the Amazon Fire TV app or its own remote."),
    ("Hisense TVs that run Roku TV, Google TV or Fire TV are supported.", "Hisense TVs that run Roku TV or Google TV are supported. Fire TV support is coming in the next app update."),
    ("Roku TV, Google TV or Fire TV?', 'Look", "Roku TV, Google TV or Fire TV?', 'Look"),
  ],
  'vizio': [
    ("a Roku stick, a Fire TV stick or a Chromecast", "a Roku stick or a Chromecast"),
    ("controls the Roku, Fire TV and Google TV devices too", "controls the Roku and Google TV devices too"),
  ],
  'iphone': [
    ("Roku, Google TV and Fire TV over Wi-Fi", "Roku and Google TV over Wi-Fi"),
    ("Google TV or Android TV, and Fire TV, over", "Google TV or Android TV, over"),
    ("(Google TV or Fire TV)", "(Google TV)"),
    ("Google TV and Android TV, and Fire TV. The brand", "Google TV and Android TV. The brand"),
  ],
  'windows': [
    ("Roku, Google TV or Fire TV from a Windows", "Roku or Google TV from a Windows"),
    ("Roku, Google TV or Fire TV from the same app", "Roku or Google TV from the same app"),
    ("(Google TV, Fire TV)", "(Google TV)"),
    ("Google TV and Android TV, and Fire TV.", "Google TV and Android TV."),
  ],
}
if not FIRE_TV_PUBLICADO:
  GUIAS_EEUU = [g for g in GUIAS_EEUU if g['clave'] != 'firetv']
  _hechos = set()
  for g in GUIAS_EEUU:
    for a, b in _CAMBIOS.get(g['clave'], []):
      for k, v in list(g.items()):
        if isinstance(v, str) and a in v:
          g[k] = v.replace(a, b); _hechos.add((g['clave'], a))
        elif isinstance(v, list):
          nv = []
          for x in v:
            if isinstance(x, str) and a in x:
              x = x.replace(a, b); _hechos.add((g['clave'], a))
            elif isinstance(x, tuple):
              y = tuple(s.replace(a, b) if isinstance(s, str) else s for s in x)
              if y != x:
                _hechos.add((g['clave'], a))
              x = y
            nv.append(x)
          g[k] = nv
  _faltan = [(c, a) for c, l in _CAMBIOS.items() for a, b in l if (c, a) not in _hechos and a != b]
  assert not _faltan, _faltan

# 2026-11-21: rescate, alternativas y marcas nuevas (datos_en_nuevas.py).
from datos_en_nuevas import GUIAS_NUEVAS, GUIAS_MARCAS_EN
GUIAS_EEUU += GUIAS_NUEVAS
