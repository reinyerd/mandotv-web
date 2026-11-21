# Guías en inglés del 2026-11-21 (SEO EE. UU. y Europa): rescate, alternativas y marcas que funcionan con las
# plataformas que la app ya maneja. Las importa datos_en_eeuu.py (se suman a GUIAS_EEUU); rutas en idiomas_sitio.py.
#
# Reglas de estas páginas (pedido del 2026-11-21):
#   - No decir qué funciones son Pro (apps y entradas pueden pasar a gratis): solo "remote free, optional one-time Pro,
#     no ads, no subscription". Lo gratis que se nombra (flechas, OK, volumen, canales, números, teclado, encender o
#     apagar) es gratis hoy según funcionesProPorDefecto.
#   - La app funciona por Wi-Fi; el infrarrojo (gratis) solo en Android con emisor infrarrojo; Bluetooth: "in development".
#     Sin duplicar pantalla (no mirroring). Fotos y videos al TV: solo como "part of Mando TV Pro" al describir esa función.
#     TV antiguos (LG NetCast, Vizio, Sony 2013-2015, Panasonic, Philips 2011-2015): siempre "beta".
#   - Fire TV: el driver no tiene Wake on LAN (lib/drivers/fire_tv.dart, wakeOnLan: false): no prometer encenderlo.
#   - Marcas: uso nominativo (docs/MARCAS.md de la app), solo las plataformas que sus modelos usan de verdad.
# Fuentes de marcas (consultadas el 2026-11-21):
#   Sony: Bravia con Android TV desde 2015 y Google TV desde 2021 (lista oficial de Google, android.com/tv).
#   Insignia: Fire TV (bestbuy.com, series F20 a F70, 2026); Roku TV en modelos anteriores.
#   onn.: Roku TV, Google TV y "Powered by VIZIO" (walmart.com, cordcuttersnews.com); onn. en la lista de Google.
#   Toshiba: Fire TV en EE. UU. (bestbuy.com, aboutamazon.com 2021); Google TV / Android TV en la lista de Google.
#   Sharp: Roku TV en EE. UU. (roku.com/products/finder/roku-tv/sharp, news.sharpusa.com); Google TV fuera de EE. UU.
#   Philips: Roku TV en EE. UU. (roku.com/products/finder/roku-tv/philips); Android TV / Google TV; Titan OS en Europa.
#   Westinghouse: Roku TV y Xumo TV (corporate.comcast.com, westinghouse.com, 2025).
#   Pioneer: Roku TV (roku.com/products/finder/roku-tv/pioneer), Fire TV (aboutamazon.com 2021) y Xumo TV.

PRECIO = ('The remote is free to download and use, with no ads and no subscription. Mando TV Pro is an optional '
          'one-time purchase for extras.')

GUIAS_NUEVAS = [
  dict(clave='firetv-lost', corto='Lost Fire TV remote',
    titulo='Lost Your Fire TV Remote? Use Your Phone Instead',
    desc='Lost your Fire TV Stick remote? Control it from your phone over Wi-Fi with a 4-digit PIN, plus fixes for a new Wi-Fi network and HDMI-CEC.',
    h1='Lost Your Fire TV Remote: How to Use Your Phone',
    intro='If the remote for your Fire TV Stick, Fire TV Cube or Fire TV smart TV is lost or dead, your phone can take over, as long as the Fire TV is still connected to your home Wi-Fi. Pairing uses a 4-digit PIN that appears on the TV screen, so you never need the old remote for it.',
    pasos=[
      'Turn on the TV with its own power button. A Fire TV Stick or Cube plugged into it usually wakes up with it, and with HDMI-CEC the TV often switches to its input by itself.',
      'If the TV shows another input, change it with the input button on the TV. See [change the HDMI input without a remote](/en/guides/change-hdmi-input-without-remote/).',
      'Connect your phone to the same Wi-Fi network as the Fire TV.',
      'Download Mando TV and open it. Your Fire TV shows up in the list. Tap it.',
      'The TV shows a 4-digit PIN. Type it into Mando TV. You only do this once.',
      'Use the d-pad, OK, Back, Home, volume, playback buttons and the keyboard from your phone.',
    ],
    extra=[
      ('Try the TV remote first (HDMI-CEC)', 'Many TV remotes can drive a Fire TV Stick through HDMI-CEC. With the Fire TV on screen, press the arrows and OK on the TV remote. If nothing happens, turn on CEC in the TV settings (Anynet+ on Samsung, SIMPLINK on LG, BRAVIA Sync on Sony) and on the Fire TV under Settings, Display & Sounds, HDMI CEC Device Control.'),
      ('If you moved or changed your Wi-Fi', 'Without a remote you cannot type the new Wi-Fi password on the Fire TV, but there is a way out: on a second phone, create a hotspot with exactly the same network name and password as your old Wi-Fi. The Fire TV joins it by itself. Connect the phone with Mando TV to that hotspot, pair with the PIN, then go to Settings, Network on the Fire TV and choose your new Wi-Fi. Finally, move your phone to the new Wi-Fi too.'),
      ('Pairing a replacement remote', 'Most new Fire TV remotes pair when you hold the Home button for about 10 seconds near the Fire TV. If it does not pair, open Settings, Controllers & Bluetooth Devices, Amazon Fire TV Remotes, Add New Remote. You can reach that menu from your phone with Mando TV.'),
      ('Fire TV built into the TV', 'On TVs with Fire TV built in, such as many Insignia and Toshiba models, the same steps work because the TV is the Fire TV. See the [Insignia](/en/guides/insignia-tv-remote-app/) and [Toshiba](/en/guides/toshiba-tv-remote-app/) pages.'),
      ('Before you start', 'Fire TV support arrived recently in Mando TV, so update the app first. If your model does not behave, tell us from the [Help page](/en/support.html) and include the model name.'),
      ('Free and Pro', PRECIO),
    ],
    marca=('/en/guides/fire-tv-remote-app/', 'Fire TV remote app'),
    faq=[
      ('Can I control a Fire TV Stick with my phone without the remote?', 'Yes, if the Fire TV is on and connected to your Wi-Fi. Mando TV pairs with the 4-digit PIN shown on the TV, so you do not need the old remote at any point.'),
      ('Does it work if the Fire TV is on a new Wi-Fi network?', 'Not directly, because the phone and the Fire TV must be on the same network. Bring the Fire TV back online first with the hotspot trick described on this page.'),
      ('Do I need the Amazon Fire TV app or an Amazon account on my phone?', 'No. Mando TV connects to the Fire TV over your home network with the PIN and has no account of its own.'),
    ]),

  dict(clave='turn-on', corto='Turn on a TV without the remote',
    titulo='How to Turn On a TV Without the Remote (Every Brand)',
    desc='Turn on a TV without the remote: where the power button is on Samsung, LG, TCL, Hisense, Sony and Vizio TVs, plus HDMI-CEC and phone tricks.',
    h1='How to Turn On a TV Without the Remote',
    intro='Almost every TV still has a physical power button. It is just well hidden. Here is where to look by brand, plus two ways to skip the hunt next time: HDMI-CEC from a console or streaming device, and turning the TV on from your phone over Wi-Fi.',
    pasos=[
      'Look under the center of the screen, right behind the brand logo. Many TVs have a single small button or joystick there, facing down.',
      'If it is not there, feel along the back of the TV near the lower corners, then along the left and right edges.',
      'Press the button once. On many single-button TVs, once the TV is on, a short press opens a small menu for input and volume, and a long press turns it off.',
      'Still nothing? Check the power cable at both ends and try another wall outlet. If the standby light stays off, the TV is not getting power.',
      'Once the TV is on, set it up so you will not need the button again: turn on HDMI-CEC and power-on over the network, both explained below.',
    ],
    extra=[
      ('Where the power button is, by brand', 'Samsung: one control button or stick under the center of the screen, or on the back at a lower corner. LG: a joystick-style button under the LG logo on most models. TCL and Hisense: usually a small button under the middle of the screen or on the back near a lower corner. Sony: on the back or on a side edge, near the bottom. Vizio: on the back, at the lower left or lower right, or on the side. Spots change by model, so if you cannot find it, look up the user manual with the model number printed on the label on the back.'),
      ('Turn on the TV from a console or streaming device (HDMI-CEC)', 'With HDMI-CEC on, turning on a PlayStation, an Xbox, a Roku player, a Fire TV Stick or a Chromecast also turns on the TV and switches it to the right input. Each brand gives the setting its own name: Anynet+ on Samsung, SIMPLINK on LG, BRAVIA Sync on Sony, and CEC on most others. More in [turn on the TV and switch to your console HDMI](/en/guides/turn-on-tv-console-hdmi-without-remote/).'),
      ('Turn on the TV from your phone', 'Smart TVs can wake up over Wi-Fi if you allow it once, and then Mando TV turns them on from your phone. On Samsung, turn on "Power On with Mobile" under Settings, General, Network, Expert Settings. On LG, turn on "TV On With Mobile" ([step by step](/en/guides/turn-on-lg-tv-with-phone/)). On a Roku TV, turn on "Fast TV start" under Settings, System, Power. On Google TV and Android TV, look for Wake on LAN or "Turn on over network", if your model has it. You do this once, with the TV on.'),
      ('If you cannot find any button', 'Some recent TVs hide the only button so well that it feels like there is none. Look for a small bump or a light sensor area under the screen: the button is often right next to it. Over Wi-Fi, Mando TV needs the TV to have been on and connected once. Infrared is the exception: on an Android phone with an infrared blaster, Mando TV can turn on a TV that was never set up, as long as you point the phone at the TV. Infrared is new, and it works with the brands in the app code list.'),
      ('Free and Pro', PRECIO),
    ],
    marca=None,
    faq=[
      ('Can I turn on a TV with my phone if I never set it up?', 'Not over Wi-Fi. A TV that is off only wakes up from the network if power-on over the network was turned on beforehand. The first time, use the button on the TV. The exception is an Android phone with an infrared blaster: Mando TV can turn on a TV by infrared with no setup, if the brand is in its code list or you pick "Other brand / not sure".'),
      ('How do I turn on a Samsung TV without the remote?', 'Press the control button under the center of the screen or on the back at a lower corner. Then turn on "Power On with Mobile" so your phone can turn it on next time.'),
      ('How do I turn on a Roku TV without the remote?', 'Use the button on the TV, usually under the center or on the back. Then turn on "Fast TV start" under Settings, System, Power so Mando TV can turn it on from your phone.'),
      ('Why does my TV turn on by itself when I turn on the console?', 'That is HDMI-CEC. It is handy, and you can turn it off in the TV settings if you prefer.'),
    ]),

  dict(clave='no-sub', corto='TV remote app with no subscription',
    titulo='TV Remote App With No Subscription and No Ads',
    desc='Tired of TV remote apps with ads or weekly subscriptions? Mando TV is free with no ads, and Pro is an optional one-time purchase. Honest comparison.',
    h1='A TV Remote App With No Subscription and No Ads',
    intro='Many universal remote apps show an ad every few taps or ask for a weekly subscription before the remote works. Mando TV takes a different path: the remote is free, there are no ads and no account, and the optional Pro upgrade is paid once. Here is how it compares, including what it does not do.',
    pasos=[
      'Before you install any remote app, open its store page and look at the in-app purchases. Weekly or monthly prices there mean a subscription.',
      'On Google Play, check whether the page says "Contains ads", and read the most recent low-star reviews: that is where surprise paywalls show up.',
      'Check that the app supports your TV over Wi-Fi. Mando TV works with Samsung (2016 and newer), LG webOS, Roku, Google TV and Android TV, and Fire TV.',
      'Install Mando TV, connect your phone to the same Wi-Fi as the TV and tap your TV in the list.',
      'Accept the prompt on the TV or type the code it shows, and use the remote. The buttons, volume, channels and keyboard cost nothing.',
    ],
    tabla=dict(titulo='Mando TV compared with many remote apps',
      cabeza=['', 'Mando TV', 'Many ad-supported or subscription apps'],
      filas=[
        ['Basic remote', 'Free', 'Often free with ads, or locked behind a trial'],
        ['Ads', 'None', 'Common'],
        ['Subscription', 'None. Pro is an optional one-time purchase', 'Weekly or monthly plans are common'],
        ['Account', 'Not needed', 'Varies'],
        ['Smart TVs over Wi-Fi', 'Samsung (2016 and newer), LG webOS, Roku, Google TV and Android TV, Fire TV', 'Varies by app'],
        ['Infrared for older TVs', 'Free on Android phones with an infrared blaster (new)', 'Some apps, only on phones with an infrared blaster'],
        ['Photos and videos to the TV', 'Pro, over Wi-Fi (not mirroring)', 'Varies by app'],
        ['Screen mirroring', 'Not offered', 'Some apps offer it'],
        ['Phones and computers', 'iPhone, iPad and Windows, plus Android in early access', 'Varies'],
      ],
      nota='Mando TV is compared with no app in particular. Check each app\'s store page for its current prices.'),
    extra=[
      ('What Mando TV does not do', 'It does not mirror your phone screen to the TV. It can send photos and videos to the TV over your home Wi-Fi, which is part of Mando TV Pro, but that is not screen mirroring. It controls smart TVs over your home Wi-Fi. A TV that is not a smart TV can be controlled by infrared from an Android phone with an infrared blaster. A Bluetooth option is still in development.'),
      ('How Mando TV makes money', 'Not with ads and not with your data: the app collects none. Mando TV is paid for by Pro, an optional one-time purchase for extras. The basic remote is free.'),
      ('On the devices you already have', 'iPhone and iPad from the App Store, Windows PCs from Microsoft Store, and Android through free early access on Google Play. See [TV remote app for iPhone](/en/guides/tv-remote-app-for-iphone/) and [TV remote app for Windows](/en/guides/tv-remote-app-for-windows/).'),
      ('Privacy', 'No account and no tracking in the app. It talks to the TV inside your home network, and the TV connection keys stay encrypted on your device. Details in the [privacy policy](/en/privacy.html).'),
    ],
    marca=None,
    faq=[
      ('Is there a TV remote app with no subscription?', 'Yes. Mando TV has no subscription at all: the remote is free with no ads, and Pro is an optional one-time purchase.'),
      ('Is Mando TV really free?', 'Yes. The arrows, OK, Back, Home, volume, channels, number keys, keyboard and power on or off are free, with no ads and no time limit.'),
      ('Does it work without Wi-Fi?', 'Mostly no. Mando TV controls smart TVs over your home Wi-Fi. The exception is infrared on Android phones that have an infrared blaster, which also works with TVs that are not smart TVs and TVs that were never connected to Wi-Fi.'),
    ]),

  dict(clave='smartthings', corto='SmartThings TV remote alternative',
    titulo='SmartThings TV Remote Not Working? A Simple Alternative',
    desc='SmartThings TV remote not working or too slow? Mando TV controls Samsung Tizen TVs over Wi-Fi with no Samsung account and no ads. Steps and fixes.',
    h1='SmartThings TV Remote Alternative for Samsung TVs',
    intro='SmartThings is Samsung\'s app for the whole smart home, and its TV remote works through your Samsung account. If that remote stopped working, or you just want a quick one, Mando TV controls Samsung TVs with Tizen, 2016 models and newer, directly over your home Wi-Fi with no account.',
    pasos=[
      'Connect your phone and the Samsung TV to the same Wi-Fi network.',
      'Download Mando TV and open it. Your Samsung TV appears in the list on its own. Tap it.',
      'The TV asks whether to allow the connection. Choose Allow with the remote or with the control button on the TV (first time only).',
      'Use the d-pad, OK, Return, Home, volume, channels and the keyboard right away.',
      'Optional: turn on "Power On with Mobile" under Settings, General, Network, Expert Settings so Mando TV can also turn the TV on.',
    ],
    extra=[
      ('Why a phone remote stops working', 'The usual causes are simple: the phone and the TV are on different Wi-Fi networks, a VPN is on, or the TV is in a deep standby mode. With SmartThings, the Samsung account adds one more thing that can fail, such as being signed out. Mando TV talks to the TV directly inside your home network, so there is no account to sign in to. More fixes in [your phone cannot find the TV](/en/guides/phone-cant-find-tv/).'),
      ('Mando TV vs SmartThings, in plain terms', 'Keep SmartThings if you use it for Samsung appliances, lights or other smart home devices, or for Samsung account features. Use Mando TV when you just want a fast remote for the TV, or when you also have an LG, Roku, Google TV or Fire TV at home: one app controls all of them. Both can live on the same phone.'),
      ('If you denied the permission by mistake', 'On the TV, go to Settings, General, External Device Manager, Device Connection Manager, and set Mando TV to allowed.'),
      ('No remote at all?', 'You can accept the prompt with the control button on the TV itself. The guide [Samsung TV without a remote](/en/guides/samsung-tv-without-remote/) walks through it.'),
      ('Free and Pro', PRECIO),
    ],
    marca=('/en/samsung-tv-remote/', 'Samsung TV remote app'),
    faq=[
      ('Can I control my Samsung TV without SmartThings?', 'Yes. Mando TV connects to Samsung Tizen TVs directly over your Wi-Fi. You allow the connection once on the TV, with no Samsung account.'),
      ('Does Mando TV control Samsung appliances?', 'No. It is a TV remote only. Keep SmartThings for appliances and other smart home devices.'),
      ('Is Mando TV made by Samsung?', 'No. Mando TV is an independent app and is not affiliated with Samsung. Samsung and SmartThings belong to their owners and are named only to describe compatibility.'),
    ]),

  dict(clave='googletv-alt', corto='Google TV remote app alternative',
    titulo='Google TV Remote App Not Working? Try This Alternative',
    desc='Phone remote for Google TV not working or not finding your TV? Mando TV controls Google TV and Android TV over Wi-Fi with no Google account and no ads.',
    h1='Google TV Remote App Alternative for Your Phone',
    intro='The phone remote for Google TV and Android TV lives inside Google\'s own app and is tied to your Google account. When it cannot find the TV, you are stuck. Mando TV is a separate remote app that pairs with the 6-character code on the TV screen and works without a Google account, from an iPhone, an Android phone or a Windows PC.',
    pasos=[
      'Turn on the TV and connect your phone to the same Wi-Fi network.',
      'Download Mando TV and open it. Tap your Google TV or Android TV in the list.',
      'The TV shows a 6-character code. Type it into Mando TV and tap Pair.',
      'Use the d-pad, OK, Back, Home, volume and the keyboard. There is nothing to sign in to.',
      'Optional: look for Wake on LAN or "Turn on over network" in the TV settings so the app can also turn the TV on.',
    ],
    extra=[
      ('Why a phone remote stops finding the TV', 'Most of the time it is the network: the phone and the TV are on different Wi-Fi networks, a VPN is on, or a guest network keeps devices apart. Fix that first, because it affects every remote app. See [your phone cannot find the TV](/en/guides/phone-cant-find-tv/).'),
      ('Which TVs it works with', 'Google TV and Android TV sets from Sony, TCL, Hisense, Philips, Sharp, Xiaomi, Toshiba and more, plus Chromecast with Google TV, Google TV Streamer and Nvidia Shield. They all pair the same way, with the code on the screen, once.'),
      ('Where Google\'s app is better', 'Google\'s app also helps you find what to watch and keeps your watchlist. Keep it for that. Mando TV is just the remote, and it also controls Samsung, LG, Roku and Fire TV from the same app, and from a Windows PC.'),
      ('If the old Android TV remote app is gone', 'Google moved its phone remote from the old Android TV Remote Control app into the Google TV app. If you want a standalone remote instead, Mando TV is one.'),
      ('Free and Pro', PRECIO),
    ],
    marca=('/en/android-tv-remote/', 'Android TV remote app'),
    faq=[
      ('Do I need a Google account to use Mando TV with Google TV?', 'No. The code on the TV screen is all it takes to pair.'),
      ('Does it work with Chromecast with Google TV?', 'Yes. It pairs the same way, with the 6-character code on the screen.'),
      ('Can I use it from an iPhone?', 'Yes. Mando TV is on the App Store for iPhone and iPad, on Microsoft Store for Windows, and in free early access on Google Play for Android.'),
    ]),
]


# ---------------------------------------------------------------------------------------------------------------
# Marcas (guías "<marca> TV remote app"): solo las plataformas que la app maneja y que esos modelos usan de verdad.
# ---------------------------------------------------------------------------------------------------------------
_ROKU_ENCENDER = 'To turn it on from your phone, turn on "Fast TV start" under Settings, System, Power.'
_GTV_ENCENDER = 'To turn it on from your phone, look for Wake on LAN or "Turn on over network" in the network or power settings. Some models do not have it.'
_FIRE_NUEVO = 'Fire TV support arrived recently in Mando TV, so update the app first, and tell us from the [Help page](/en/support.html) if your model does not behave.'

GUIAS_MARCAS = [
  dict(clave='sony', corto='Sony TV remote app',
    titulo='Sony TV Remote App for iPhone, Android and PC',
    desc='Sony Bravia TV remote app: Mando TV controls Sony TVs with Google TV or Android TV over Wi-Fi, and 2013 to 2015 Bravia without Android in beta.',
    h1='Sony TV Remote App for Your Phone',
    intro='Sony Bravia smart TVs run Google TV on recent models and Android TV on earlier ones, going back to 2015. Mando TV controls both from an iPhone, an Android phone or a Windows PC over your home Wi-Fi, so it works as a Sony TV remote app when the remote is lost or out of battery.',
    pasos=[
      'Check that your Sony shows the Google TV or Android TV home screen. Most Sony Bravia smart TVs since 2015 do.',
      'Connect your phone and the TV to the same Wi-Fi network.',
      'Open Mando TV and tap your Sony in the list.',
      'Type the 6-character code the TV shows on the screen (first time only). You do not need the remote for this.',
      'Use the d-pad, OK, Back, Home, volume and keyboard.',
    ],
    extra=[
      ('Turn on a Sony TV from your phone', 'Sony Google TV and Android TV models can wake up over the network when "Remote start" is on. It is usually under Settings, Network & Internet, Remote start, though the path changes a little by model. Then tap the TV in Mando TV while it is off and the app turns it on.'),
      ('Where the power button is on a Sony', 'On most Bravia TVs it is on the back, near the lower left or right edge, or on a side edge. A short press turns the TV on. More in [how to turn on a TV without the remote](/en/guides/turn-on-tv-without-remote/).'),
      ('Older Sony TVs', 'Sony Bravia TVs from 2013 to 2015 that do not run Android have beta support in Mando TV. It is new, so it can still have rough edges. The TV shows a 4-digit PIN to type into the app. Other Sony TVs without Google TV or Android TV are not covered today.'),
      ('Free and Pro', PRECIO),
    ],
    marca=('/en/android-tv-remote/', 'Android TV remote app'),
    faq=[
      ('Does Mando TV work with Sony Bravia TVs?', 'Yes, with Sony TVs that run Google TV or Android TV, which covers most Sony smart TVs since 2015.'),
      ('Do I need a Sony app or a Google account?', 'No. Mando TV pairs with the code on the TV screen and has no account.'),
      ('Does it work with older Sony Bravia TVs without Android?', 'In beta, yes, on Bravia models from 2013 to 2015 without Android. It pairs with a 4-digit PIN shown on the TV.'),
      ('Can I type on my Sony TV from my phone?', 'Yes. The keyboard is free and types into YouTube, Netflix and the TV search box.'),
    ]),

  dict(clave='insignia', corto='Insignia TV remote app',
    titulo='Insignia TV Remote App: Fire TV and Roku TV Models',
    desc='Insignia TV remote app: most Insignia smart TVs run Fire TV and some older ones Roku TV. Mando TV controls both from your phone or PC over Wi-Fi.',
    h1='Insignia TV Remote App for Your Phone',
    intro='Most Insignia smart TVs sold today have Fire TV built in, and some earlier Insignia models run Roku TV. Mando TV controls both over your home Wi-Fi, from an iPhone, an Android phone or a Windows PC, with no account and no ads.',
    pasos=[
      'Look at the home screen to see which system your Insignia runs. Fire TV shows rows of apps and Amazon content. Roku TV shows a grid of tiles with the Roku menu on the left.',
      'Connect your phone and the TV to the same Wi-Fi network.',
      'Open Mando TV and tap your Insignia in the list.',
      'On a Fire TV model, type the 4-digit PIN the TV shows. A Roku TV model asks for nothing.',
      'Use the d-pad, OK, Back, Home, volume and keyboard from your phone.',
    ],
    extra=[
      ('Insignia with Fire TV built in', 'The TV is the Fire TV, so the [Fire TV remote app](/en/guides/fire-tv-remote-app/) guide applies. ' + _FIRE_NUEVO + ' Lost the remote? See [lost your Fire TV remote](/en/guides/lost-fire-tv-remote/).'),
      ('Insignia with Roku TV', 'It works like any Roku TV, with no code. ' + _ROKU_ENCENDER + ' Details on the [Roku remote app page](/en/roku-remote/).'),
      ('Turn on an Insignia without the remote', 'The power button is usually under the center of the screen or on the back near a lower corner. See [how to turn on a TV without the remote](/en/guides/turn-on-tv-without-remote/).'),
      ('Insignia TVs that are not smart TVs', 'An Insignia without Fire TV or Roku TV cannot be controlled over Wi-Fi. Mando TV has infrared control for Android phones with an infrared blaster, but Insignia is not in its list of brand code sets. The "Other brand / not sure" option tries every code set, so whether it works depends on the model.'),
      ('Free and Pro', PRECIO),
    ],
    marca=None,
    faq=[
      ('Does Mando TV work with Insignia Fire TV models?', 'Yes. It pairs with the 4-digit PIN on the screen. Fire TV support is new, so keep the app updated.'),
      ('Can my phone turn on an Insignia TV?', 'On Roku TV models, yes, once "Fast TV start" is on. On Fire TV models, turn the TV on with its button and then use your phone.'),
      ('Do I need the Amazon Fire TV app?', 'No. Mando TV connects over your Wi-Fi and needs no Amazon account on the phone.'),
    ]),

  dict(clave='onn', corto='onn. TV remote app',
    titulo='onn. TV Remote App: Roku TV and Google TV Models',
    desc='onn. TV remote app: Mando TV controls onn. Roku TV and Google TV sets and the onn. Google TV streaming box over Wi-Fi. Honest note on VIZIO models.',
    h1='onn. TV Remote App for Your Phone',
    intro='onn. is Walmart\'s own brand, and its TVs come with different systems inside: Roku TV, Google TV and, on some newer sets, VIZIO\'s system. Mando TV controls the Roku TV and Google TV models, plus the onn. Google TV streaming box, over your home Wi-Fi.',
    pasos=[
      'Check the home screen. Roku TV shows a grid of tiles. Google TV shows rows of recommendations. Sets labeled "Powered by VIZIO" show the VIZIO home screen.',
      'Connect your phone and the TV to the same Wi-Fi network.',
      'Open Mando TV and tap your onn. TV in the list.',
      'A Roku TV asks for nothing. Google TV shows a 6-character code: type it into the app (first time only).',
      'Use the d-pad, OK, Back, Home, volume and keyboard.',
    ],
    extra=[
      ('onn. Roku TV', 'Works like any Roku TV. ' + _ROKU_ENCENDER + ' To change the input without the remote, the inputs are tiles on the home screen: move with the arrows and press OK. More on the [Roku remote app page](/en/roku-remote/).'),
      ('onn. Google TV and the onn. streaming box', 'Both pair with the 6-character code. For the streaming box, the TV power and input depend on the TV it is plugged into; with HDMI-CEC on, the TV usually follows. More on the [Android TV remote app page](/en/android-tv-remote/).'),
      ('onn. TVs powered by VIZIO', 'These run VIZIO\'s system. Mando TV has beta support for VIZIO SmartCast TVs, explained on the [Vizio TV remote app](/en/guides/vizio-tv-remote-app/) page, but we cannot promise that every onn. model powered by VIZIO works. If you plug a Roku, Fire TV or Google TV device into one, Mando TV can control that device.'),
      ('Free and Pro', PRECIO),
    ],
    marca=None,
    faq=[
      ('Does Mando TV work with onn. TVs?', 'With onn. TVs that run Roku TV or Google TV, yes. For onn. TVs powered by VIZIO, Mando TV has beta support for VIZIO SmartCast TVs, but we cannot promise those onn. models work.'),
      ('Does it work with the onn. Google TV streaming box?', 'Yes. It runs Google TV and pairs with the code on the screen.'),
      ('Do I need a Walmart or Google account?', 'No. Mando TV has no account and connects over your home Wi-Fi.'),
    ]),

  dict(clave='toshiba', corto='Toshiba TV remote app',
    titulo='Toshiba TV Remote App: Fire TV and Google TV Models',
    desc='Toshiba TV remote app: Mando TV controls Toshiba TVs with Fire TV, Google TV, Android TV or VIDAA from your phone or PC over Wi-Fi. No account.',
    h1='Toshiba TV Remote App for Your Phone',
    intro='In the US, Toshiba smart TVs come with Fire TV built in. In other countries Toshiba also sells TVs with Google TV or Android TV, and some with VIDAA. Mando TV controls all of them from your phone or PC over Wi-Fi, with one exception on some recent VIDAA models.',
    pasos=[
      'Check the home screen. Fire TV shows rows of apps and Amazon content. Google TV and Android TV show Google rows of recommendations. VIDAA has its own home screen.',
      'Connect your phone and the TV to the same Wi-Fi network.',
      'Open Mando TV and tap your Toshiba in the list.',
      'Fire TV and VIDAA models may show a 4-digit PIN; Google TV and Android TV models show a 6-character code. Type it into Mando TV once.',
      'Use the d-pad, OK, Back, Home, volume and keyboard.',
    ],
    extra=[
      ('Toshiba Fire TV', 'The TV is the Fire TV, so the [Fire TV remote app](/en/guides/fire-tv-remote-app/) guide applies. ' + _FIRE_NUEVO + ' Lost the remote? See [lost your Fire TV remote](/en/guides/lost-fire-tv-remote/).'),
      ('Toshiba Google TV and Android TV', 'They pair with the code on the screen. ' + _GTV_ENCENDER + ' More on the [Android TV remote app page](/en/android-tv-remote/).'),
      ('Toshiba with VIDAA', 'Most VIDAA models work. Some recent VIDAA models only accept the official app of the TV maker; Mando TV detects that when it connects and tells you plainly. More in the [Hisense TV remote app](/en/guides/hisense-tv-remote-app/) guide.'),
      ('Turn on a Toshiba without the remote', 'Look for the power button under the center of the screen or on the back near a lower corner. More in [how to turn on a TV without the remote](/en/guides/turn-on-tv-without-remote/).'),
      ('Free and Pro', PRECIO),
    ],
    marca=None,
    faq=[
      ('Does Mando TV work with Toshiba Fire TV?', 'Yes. It pairs with the 4-digit PIN on the screen. Fire TV support is new, so keep the app updated and tell us if your model does not behave.'),
      ('Does it work with Toshiba VIDAA TVs?', 'Yes, with most VIDAA models. Some recent ones only accept the official app; Mando TV detects it and tells you.'),
      ('Do I need an Amazon or Google account?', 'No. Mando TV has no account and connects over your home Wi-Fi.'),
    ]),

  dict(clave='sharp', corto='Sharp TV remote app',
    titulo='Sharp TV Remote App: Roku TV and Google TV Models',
    desc='Sharp TV remote app: Mando TV controls Sharp Roku TV models and Sharp Aquos TVs with Google TV or Android TV from your phone or PC over Wi-Fi.',
    h1='Sharp TV Remote App for Your Phone',
    intro='In the US, Sharp smart TVs run Roku TV. In many other countries, Sharp Aquos TVs run Google TV or Android TV. Mando TV controls both from your phone or PC over your home Wi-Fi, with no account and no ads.',
    pasos=[
      'Check the home screen. Roku TV shows a grid of tiles with the Roku menu. Google TV and Android TV show rows of recommendations.',
      'Connect your phone and the TV to the same Wi-Fi network.',
      'Open Mando TV and tap your Sharp in the list.',
      'A Roku TV asks for nothing. Google TV and Android TV show a 6-character code: type it into the app once.',
      'Use the d-pad, OK, Back, Home, volume and keyboard.',
    ],
    extra=[
      ('Sharp Roku TV', 'Works like any Roku TV, including Sharp\'s OLED Roku TV models. ' + _ROKU_ENCENDER + ' More on the [Roku remote app page](/en/roku-remote/).'),
      ('Sharp Aquos with Google TV or Android TV', 'Pairs with the code on the screen. ' + _GTV_ENCENDER + ' More on the [Android TV remote app page](/en/android-tv-remote/).'),
      ('Sharp TVs with another system', 'Sharp TVs without Roku TV, Google TV or Android TV are not controlled by Mando TV today.'),
      ('Free and Pro', PRECIO),
    ],
    marca=None,
    faq=[
      ('Does Mando TV work with Sharp TVs?', 'Yes, with Sharp TVs that run Roku TV, Google TV or Android TV.'),
      ('My Sharp Roku TV ignores the app. What do I do?', 'On the TV, go to Settings, System, Advanced system settings, Control by mobile apps, and allow network access. The guide [Roku remote app not working](/en/guides/roku-remote-app-not-working/) has the details.'),
      ('Do I need an account?', 'No. Mando TV connects over your home Wi-Fi and has no account.'),
    ]),

  dict(clave='philips', corto='Philips TV remote app',
    titulo='Philips TV Remote App: Roku TV, Google TV and Android TV',
    desc='Philips TV remote app: Mando TV controls Philips Roku TV models and Philips TVs with Google TV or Android TV over Wi-Fi. Honest note on Titan OS.',
    h1='Philips TV Remote App for Your Phone',
    intro='Philips TVs run different systems depending on the country and the year: Roku TV in the US, Google TV or Android TV in many countries, and Titan OS on some recent European models. Mando TV controls the Roku TV, Google TV and Android TV models from your phone or PC over Wi-Fi.',
    pasos=[
      'Check the home screen. Roku TV shows a grid of tiles. Google TV and Android TV show rows of recommendations from Google. Titan OS has its own home screen.',
      'Connect your phone and the TV to the same Wi-Fi network.',
      'Open Mando TV and tap your Philips in the list.',
      'A Roku TV asks for nothing. Google TV and Android TV show a 6-character code: type it into the app once.',
      'Use the d-pad, OK, Back, Home, volume and keyboard.',
    ],
    extra=[
      ('Philips Roku TV', 'Works like any Roku TV. ' + _ROKU_ENCENDER + ' More on the [Roku remote app page](/en/roku-remote/).'),
      ('Philips with Google TV or Android TV', 'Includes many Ambilight models. They pair with the code on the screen. ' + _GTV_ENCENDER + ' More on the [Android TV remote app page](/en/android-tv-remote/).'),
      ('Older Philips TVs without Android', 'Philips TVs from 2011 to 2015 that do not run Android have beta support in Mando TV. It is new, and it needs no pairing code.'),
      ('Philips with Titan OS', 'Titan OS is a different system that Mando TV does not control today, and we prefer to say so plainly. Newer Philips models without Android are not covered either.'),
      ('Free and Pro', PRECIO),
    ],
    marca=None,
    faq=[
      ('Does Mando TV work with Philips TVs?', 'With Philips TVs that run Roku TV, Google TV or Android TV, yes, and in beta with Philips TVs from 2011 to 2015 without Android. Titan OS models are not supported.'),
      ('Does it control Ambilight?', 'Mando TV is a remote: it sends the buttons, so you can reach the Ambilight settings with the arrows and OK. It has no separate Ambilight controls.'),
      ('Do I need a Philips or Google account?', 'No. Mando TV connects over your home Wi-Fi and has no account.'),
    ]),

  dict(clave='westinghouse', corto='Westinghouse TV remote app',
    titulo='Westinghouse TV Remote App for Roku TV Models',
    desc='Westinghouse TV remote app: Mando TV controls Westinghouse Roku TV models from your phone or PC over Wi-Fi. Honest note on newer Xumo TV models.',
    h1='Westinghouse TV Remote App for Your Phone',
    intro='Most Westinghouse smart TVs sold in recent years run Roku TV, and newer lines run Xumo TV. Mando TV controls the Roku TV models over your home Wi-Fi from an iPhone, an Android phone or a Windows PC. Xumo TV models are not supported.',
    pasos=[
      'Check the home screen. Roku TV shows a grid of tiles with the Roku menu on the left. Xumo TV shows the Xumo home screen.',
      'Connect your phone and the TV to the same Wi-Fi network.',
      'Open Mando TV and tap your Westinghouse in the list. Roku TV does not ask for a code.',
      'Use the d-pad, OK, Back, Home, volume and keyboard.',
      'If the buttons do nothing, allow control by mobile apps on the TV, as shown in [Roku remote app not working](/en/guides/roku-remote-app-not-working/).',
    ],
    extra=[
      ('Turn it on and change the input', _ROKU_ENCENDER + ' To change the input without the remote, the inputs are tiles on the home screen: move with the arrows and press OK. More on the [Roku remote app page](/en/roku-remote/).'),
      ('Westinghouse Xumo TV', 'Xumo TV uses a different system that Mando TV does not control. If you plug a Roku, Fire TV or Google TV device into one, Mando TV can control that device.'),
      ('Free and Pro', PRECIO),
    ],
    marca=('/en/roku-remote/', 'Roku remote app'),
    faq=[
      ('Does Mando TV work with Westinghouse TVs?', 'With Westinghouse Roku TV models, yes. Westinghouse Xumo TV models are not supported.'),
      ('Can my phone turn on a Westinghouse Roku TV?', 'Yes, once "Fast TV start" is on under Settings, System, Power.'),
      ('Do I need a Roku account?', 'No. Mando TV talks to the TV over your home network and has no account.'),
    ]),

  dict(clave='pioneer', corto='Pioneer TV remote app',
    titulo='Pioneer TV Remote App: Roku TV and Fire TV Models',
    desc='Pioneer TV remote app: Mando TV controls Pioneer Roku TV and Pioneer Fire TV models from your phone or PC over Wi-Fi. Honest note on Xumo models.',
    h1='Pioneer TV Remote App for Your Phone',
    intro='Pioneer smart TVs in the US come with Roku TV or Fire TV built in, and some newer ones with Xumo TV. Mando TV controls the Roku TV and Fire TV models over your home Wi-Fi, from your phone or a Windows PC.',
    pasos=[
      'Check the home screen. Roku TV shows a grid of tiles. Fire TV shows rows of apps and Amazon content. Xumo TV shows the Xumo home screen.',
      'Connect your phone and the TV to the same Wi-Fi network.',
      'Open Mando TV and tap your Pioneer in the list.',
      'A Roku TV asks for nothing. A Fire TV model shows a 4-digit PIN: type it into the app once.',
      'Use the d-pad, OK, Back, Home, volume and keyboard.',
    ],
    extra=[
      ('Pioneer Roku TV', 'Works like any Roku TV. ' + _ROKU_ENCENDER + ' More on the [Roku remote app page](/en/roku-remote/).'),
      ('Pioneer Fire TV', 'The TV is the Fire TV, so the [Fire TV remote app](/en/guides/fire-tv-remote-app/) guide applies. ' + _FIRE_NUEVO),
      ('Pioneer Xumo TV', 'Xumo TV uses a different system that Mando TV does not control today.'),
      ('Free and Pro', PRECIO),
    ],
    marca=None,
    faq=[
      ('Does Mando TV work with Pioneer TVs?', 'With Pioneer Roku TV and Fire TV models, yes. Xumo TV models are not supported.'),
      ('Can my phone turn on a Pioneer TV?', 'On Roku TV models, yes, once "Fast TV start" is on. On Fire TV models, turn the TV on with its button and then use your phone.'),
      ('Do I need an account?', 'No. Mando TV connects over your home Wi-Fi and has no account.'),
    ]),
]

# (clave, texto del enlace) de las guías de marca, para el índice, "More guides" y la sección de marcas.
GUIAS_MARCAS_EN = [(g['clave'], g['corto']) for g in GUIAS_MARCAS]
GUIAS_NUEVAS += GUIAS_MARCAS

# Comprobaciones: títulos y descripciones caben en Google; no se dice qué es Pro. Fecha real de publicación.
for _g in GUIAS_NUEVAS:
    _g.setdefault('fecha', '2026-11-21')
    assert len(_g['titulo']) <= 60, (_g['clave'], len(_g['titulo']))
    assert 110 <= len(_g['desc']) <= 160, (_g['clave'], len(_g['desc']))
    _texto = repr(_g)
    for _palabra in ('(Pro)', 'is Pro', 'are Pro', 'Pro feature', 'with Pro'):
        assert _palabra not in _texto, (_g['clave'], _palabra)
