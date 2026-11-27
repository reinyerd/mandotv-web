# Textos en checo (vykání) de mandotv.app. Los usa generar_idiomas.py. Escritos para las búsquedas de la República Checa.
# Las claves de las páginas (lg, lost-tv, ...) y sus rutas están en idiomas_sitio.py.
# Los nombres de menús de cada marca (LG, Samsung, Roku, Android TV, iPhone) son los mismos que usa la app en checo
# (lib/l10n/app_cs.arb del proyecto de la app).

UI = dict(
  locale='cs_CZ',
  aria_home='Mando TV, domovská stránka', aria_main='Hlavní nabídka', nav_que='Funkce', nav_ayuda='Nápověda', nav_contacto='Kontakt',
  asunto='Dobr%C3%BD%20den%20Mando%20TV', inicio='Domů', privacidad='Ochrana soukromí', aria_pie='Zápatí stránky', aria_ruta='Drobečková navigace',
  aria_marcas='Značky a návody', hecho='Vyvinuto v Chile',
  aviso='Mando TV je nezávislá aplikace. Nemá žádnou souvislost s uvedenými výrobci televizorů ani se společnostmi Google, Amazon, Apple či Roku a tyto společnosti ji nepodporují. Ochranné známky patří jejich vlastníkům a uvádíme je pouze kvůli popisu kompatibility. Android TV a Google TV jsou ochranné známky společnosti Google LLC. Apple TV je ochranná známka společnosti Apple Inc.',
  bajar='Stáhnout zdarma', descarga='Stáhnout z', anticipada='Předběžný přístup na',
  apple_aria='Stáhnout Mando TV zdarma z App Store', ms_aria='Stáhnout Mando TV zdarma z Microsoft Store',
  gp_aria='Předběžný přístup k Mando TV na Google Play pro Android', aria_desc='Stáhnout Mando TV',
  b_como_btn='Jak se připojit', b_tiendas_label='Dostupné v obchodech s aplikacemi',
  b_nota='iPhone, iPad, Mac, Android a Windows. Stažení zdarma, bez reklam. Pro je jednorázový nákup, bez předplatného.',
  b_compat='Kompatibilní televizory', b_otras='Další značky', b_otras_p='Mando TV ovládá všechny tyto značky jedinou aplikací:',
  g_guias='Návody', g_ver='Zobrazit postup', g_pasos='Krok za krokem', g_hazlo='Jak na to s Mando TV',
  g_tiendas='Mando TV je univerzální dálkový ovladač k vaší televizi. Stáhněte si ho zdarma, bez reklam a bez účtu. Pro je volitelný jednorázový nákup, bez předplatného. Pro iPhone, iPad, Windows a Android:',
  g_nota='Android: bezplatný předběžný přístup na Google Play. <a href="{enlace}">Zapojte se ve dvou krocích</a> a pomozte nám dostat se do obchodu.',
  g_mas_pagina='Více podrobností najdete na stránce {enlace}.', g_mas_marca='Více podrobností podle značky:',
  g_faq='Časté otázky', g_mas='Další návody', g_todas='Všechny návody', g_ayuda='Nápověda a podpora',
  g_idiomas='Tento návod v jiných jazycích',
)

# Pie de página y listas de marcas/guías: (clave, texto)
PIE = [
  ('samsung', 'Dálkový ovladač Samsung'),
  ('lg', 'Dálkový ovladač LG'),
  ('roku', 'Dálkový ovladač Roku'),
  ('android', 'Dálkový ovladač Android TV'),
  ('guias', 'Všechny návody'),
  ('lost-tv', 'Ztracený dálkový ovladač'),
  ('lost-lg', 'Ztracený ovladač LG'),
  ('lg-on', 'Zapnutí LG televize telefonem'),
  ('hdmi', 'Změna vstupu HDMI bez ovladače'),
  ('androidtv', 'Android TV bez ovladače'),
  ('console', 'Televize a HDMI konzole bez ovladače'),
  ('samsung-lost', 'Samsung televize bez ovladače'),
  ('roku-lost', 'Ztracený ovladač Roku'),
  ('roku-403', 'Aplikace Roku nefunguje'),
  ('androidtv-code', 'Párovací kód Android TV'),
  ('not-found', 'Telefon nenajde televizi'),
  ('wifi', 'Telefon jako ovladač přes Wi-Fi'),
  ('pc', 'Ovládání televize z počítače'),
]
NOMBRE_OTRA = {'lg': 'Ovládací aplikace pro LG', 'samsung': 'Ovládací aplikace pro Samsung', 'roku': 'Ovládací aplikace pro Roku',
               'android': 'Ovládací aplikace pro Android TV a Google TV'}
PAGINA_MARCA = {'lg': 'Ovládací aplikace pro LG', 'samsung': 'Ovládací aplikace pro Samsung', 'roku': 'Ovládací aplikace pro Roku',
                'android': 'Ovládací aplikace pro Android TV'}

OTRAS_GUIAS = [
  ('lg-on', 'Zapnutí LG televize telefonem'),
  ('lost-tv', 'Ztracený dálkový ovladač: co můžete udělat'),
  ('lost-lg', 'Ztracený ovladač LG: jak použít telefon'),
  ('hdmi', 'Změna vstupu HDMI na televizi bez ovladače'),
  ('androidtv', 'Android TV bez ovladače: jak použít telefon'),
  ('console', 'Zapnutí televize a přepnutí na HDMI konzole bez ovladače'),
  ('samsung-lost', 'Samsung televize bez původního ovladače: jak použít telefon'),
  ('roku-lost', 'Ztracený ovladač Roku: jak použít telefon'),
  ('roku-403', 'Aplikace Roku nefunguje: oprava chyby 403'),
  ('androidtv-code', 'Android TV žádá párovací kód: co dělat'),
  ('not-found', 'Telefon nenajde televizi: co zkontrolovat'),
  ('wifi', 'Jak používat telefon jako ovladač přes Wi-Fi'),
  ('pc', 'Jak ovládat televizi počítačem s Windows'),
]

INDICE = dict(
  titulo='Návody: ovládání televize telefonem | Mando TV',
  desc='Návody krok za krokem: telefon nebo počítač jako dálkový ovladač, zapnutí televize, změna HDMI a řešení potíží u Samsungu, LG a Roku.',
  h1='Návody: telefon jako dálkový ovladač',
  intro='Jednoduché postupy, jak propojit dálkový ovladač televize Samsung, LG, Roku nebo Android TV s aplikací Mando TV, zapnout televizi a vyřešit potíže.',
  h2_guias='Všechny návody', h2_marcas='Ovládací aplikace podle značky',
  marcas_extra=[('sony', 'Ovládací aplikace Sony'), ('philips', 'Ovládací aplikace Philips')],
)

MARCAS = [
  dict(clave='lg', color='#e0457b', corto='LG',
    titulo='Dálkový ovladač LG TV v telefonu, zdarma | Mando TV',
    desc='Telefon nebo počítač jako dálkový ovladač LG TV s webOS přes Wi-Fi. Tlačítka, klávesnice, aplikace, vstupy a zapnutí zdarma; ukazatel s Pro.',
    h1='Dálkový ovladač LG TV jako aplikace v telefonu',
    intro='Mando TV je ovládací aplikace pro televizory LG: přes domácí Wi-Fi z vašeho telefonu nebo počítače udělá dálkový ovladač k chytré televizi LG s webOS. Hodí se, když jste ovladač ztratili, došly v něm baterie nebo chcete jen rychleji psát.',
    compat='Chytré televize LG s webOS (většina chytrých modelů LG od roku 2014). Funguje s televizory LED, NanoCell, QNED i OLED. Starší chytré televize LG s NetCast (2011 až 2014, před webOS) nově podporujeme v betě: spárují se 6místným klíčem, který televize zobrazí.',
    h2=dict(funciones='Co můžete dělat se svou televizí LG', como='Jak připojit televizi LG k Mando TV',
            encender='Zapnutí LG televize telefonem', preguntas='Otázky k LG', guias='Návody pro LG'),
    funciones=[
      ('Všechna tlačítka', 'Směrový ovladač, OK, Zpět, Domů, hlasitost, programy, ztlumení a přehrávání.'),
      ('Ukazatel jako u Magic Remote (Pro)', 'Šipku po obrazovce posouváte prstem, stejně jako s ovladačem LG Magic Remote.'),
      ('Dvě klávesnice', 'Pište do vyhledávání televize a ve většině aplikací na klávesnici telefonu. S funkcí Klávesnice YouTube (Pro) napište nebo řekněte, co chcete sledovat, a YouTube se na televizi otevře s výsledky.'),
      ('Aplikace a vstupy', 'Otevřete své aplikace a přepněte na HDMI, živé vysílání, AirPlay nebo Screen Share.'),
      ('Zvukový výstup (Pro)', 'Přepínejte mezi reproduktory televize a soundbarem.'),
      ('Zapnutí televize', 'Když je vypnutá, Mando TV ji zapne přes síť a samo se připojí.'),
    ],
    pasos=[
      'Připojte telefon a televizi ke stejné síti Wi-Fi.',
      'Otevřete Mando TV: vaše televize LG se v seznamu objeví sama. Klepněte na ni.',
      'Na televizi se zobrazí dotaz s žádostí o povolení. Potvrďte ho svým obvyklým ovladačem (jen poprvé).',
    ],
    encender='Zapněte „Zapnout televizi pomocí mobilního zařízení“ (u některých modelů se jmenuje „Zapnout přes Wi-Fi“). Najdete ho v Nastavení > Obecné > Zařízení > Externí zařízení (u starších modelů Připojení > Správa mobilního připojení). Potom se vás aplikace při klepnutí na vypnutou televizi v Mando TV zeptá, zda ji má zapnout, a samo se připojí.',
    faq=[
      ('Potřebuji k používání Mando TV ovladač Magic Remote?', 'Jen poprvé, abyste potvrdili dotaz na obrazovce. Potom stačí telefon.'),
      ('Nahradí Mando TV aplikaci LG ThinQ?', 'K ovládání televize ano: nepotřebujete účet LG ani televizi nemusíte registrovat. Mando TV se připojuje přímo přes vaši Wi-Fi.'),
      ('Mohu LG televizi zapnout telefonem?', 'Ano, pokud máte v televizi zapnuté „Zapnout televizi pomocí mobilního zařízení“ a jednou jste se připojili, když byla zapnutá.'),
      ('Funguje to se staršími televizemi LG před érou webOS?', 'V betě ano, s chytrými televizemi LG s NetCast z let 2011 až 2014. Spárují se 6místným klíčem, který televize zobrazí. Funkce je nová a může mít ještě drobné nedostatky.'),
    ],
    guias=[('lg-on', 'Jak zapnout LG televizi telefonem'),
           ('lost-lg', 'Ztracený ovladač LG: jak použít telefon'),
           ('hdmi', 'Změna vstupu HDMI na televizi bez ovladače'),
           ('guias', 'Všechny návody k ovládání televize telefonem')]),
  dict(clave='samsung', color='#3d7bff', corto='Samsung',
    titulo='Dálkový ovladač Samsung TV v telefonu | Mando TV',
    desc='Telefon nebo počítač jako dálkový ovladač Samsung TV s Tizen přes Wi-Fi. Tlačítka, klávesnice, aplikace a zapnutí zdarma; touchpad s Pro. Bez reklam.',
    h1='Dálkový ovladač Samsung TV jako aplikace v telefonu',
    intro='Mando TV je ovládací aplikace pro televizory Samsung: přes domácí Wi-Fi z vašeho telefonu nebo počítače udělá dálkový ovladač k chytré televizi Samsung. Nepotřebujete účet Samsung ani televizi nemusíte registrovat.',
    compat='Chytré televize Samsung s Tizen, rok výroby 2016 a novější (řady jako Crystal UHD, QLED, Neo QLED, The Frame a OLED).',
    h2=dict(funciones='Co můžete dělat se svou televizí Samsung', como='Jak připojit televizi Samsung k Mando TV',
            encender='Zapnutí Samsung televize telefonem', preguntas='Otázky k Samsungu', guias='Návody pro Samsung'),
    funciones=[
      ('Všechna tlačítka', 'Směrový ovladač, OK, Zpět, Domů, hlasitost, programy, ztlumení a zdroj.'),
      ('Touchpad (Pro)', 'Prstem listujte nabídkami, aniž byste museli hledat šipky.'),
      ('Dvě klávesnice', 'Pište do vyhledávání televize a ve většině aplikací na klávesnici telefonu. S funkcí Klávesnice YouTube (Pro) napište nebo řekněte, co chcete sledovat, a YouTube se na televizi otevře s výsledky.'),
      ('Aplikace', 'Netflix, YouTube, Prime Video a další aplikace otevřete jedním klepnutím.'),
      ('Zapnutí televize', 'Když je vypnutá, Mando TV ji zapne přes síť a samo se připojí.'),
      ('Bez účtu', 'Připojení vede přímo přes vaši Wi-Fi, bez oklik přes internet.'),
    ],
    pasos=[
      'Připojte telefon a televizi ke stejné síti Wi-Fi.',
      'Otevřete Mando TV: vaše televize Samsung se v seznamu objeví sama. Klepněte na ni.',
      'Televize se zeptá, zda připojení povolujete. Ovladačem vyberte „Povolit“ (jen poprvé).',
    ],
    encender='V televizi Samsung zapněte v Nastavení > Obecné > Síť > Expertní nastavení možnost „Zapnout pomocí mobilního zařízení“. Potom se vás aplikace při klepnutí na vypnutou televizi v Mando TV zeptá, zda ji má zapnout, a samo se připojí.',
    faq=[
      ('Omylem jsem zakázal(a) povolení. Co mám dělat?', 'V televizi otevřete Nastavení > Obecné > Správce externích zařízení > Správce připojení zařízení a nastavte Mando TV na povoleno.'),
      ('Nahradí Mando TV aplikaci SmartThings?', 'K ovládání televize ano, a to bez účtu Samsung. Mando TV se připojuje přímo přes vaši Wi-Fi.'),
      ('Funguje to se staršími televizemi Samsung?', 'Funguje s televizemi Samsung s Tizen, rok výroby 2016 a novější. Dřívější modely používají jiný systém, který zatím nepodporujeme.'),
    ],
    guias=[('samsung-lost', 'Samsung televize bez původního ovladače: jak použít telefon'),
           ('smartthings', 'Alternativa k SmartThings pro televize Samsung'),
           ('turn-on', 'Jak zapnout televizi bez ovladače'),
           ('hdmi', 'Změna vstupu HDMI na televizi bez ovladače'),
           ('guias', 'Všechny návody k ovládání televize telefonem')]),
  dict(clave='roku', color='#a77bff', corto='Roku',
    titulo='Dálkový ovladač Roku v telefonu, zdarma | Mando TV',
    desc='Telefon nebo počítač jako dálkový ovladač Roku TV a přehrávačů Roku přes Wi-Fi. Tlačítka, klávesnice, kanály, vstupy a zapnutí zdarma.',
    h1='Dálkový ovladač Roku jako aplikace v telefonu',
    intro='Mando TV je ovládací aplikace pro Roku: přes domácí Wi-Fi z vašeho telefonu nebo počítače udělá dálkový ovladač k vašemu zařízení Roku. Funguje s televizory Roku TV i s přehrávači Roku zapojenými do HDMI.',
    compat='Televizory Roku TV (TCL, Hisense, Philips, Sharp, JVC a další) a přehrávače Roku (Express, Streaming Stick, Ultra).',
    h2=dict(funciones='Co můžete dělat se svým Roku', como='Jak připojit Roku k Mando TV',
            encender='Zapnutí Roku telefonem', preguntas='Otázky k Roku', guias='Návody pro Roku'),
    funciones=[
      ('Všechna tlačítka', 'Směrový ovladač, OK, Zpět, Domů, hlasitost, ztlumení, zopakování a přehrávání.'),
      ('Dvě klávesnice', 'Pište do vyhledávání Roku a v kanálech, které to umožňují, na klávesnici telefonu. S funkcí Klávesnice YouTube (Pro) napište nebo řekněte, co chcete sledovat, a YouTube se na televizi otevře s výsledky.'),
      ('Kanály', 'Netflix, YouTube a další kanály Roku otevřete jedním klepnutím.'),
      ('Vstupy', 'U Roku TV přepínejte v aplikaci na HDMI, anténu nebo AV.'),
      ('Zapnutí televize', 'U televizorů Roku TV s rychlým spuštěním je Mando TV zapne z vašeho telefonu.'),
      ('Bez párování', 'Roku nežádá kód: klepněte na něj v seznamu a jste připojeni.'),
      ('Rozeznění ovladače', 'Má-li váš ovladač Roku reproduktor, například Roku Voice Remote Pro, Mando TV ho rozezní, abyste ho našli. Zdarma, Roku musí být zapnuté.'),
    ],
    pasos=[
      'Připojte telefon a Roku ke stejné síti Wi-Fi.',
      'Otevřete Mando TV: vaše Roku se v seznamu objeví samo. Klepněte na ně.',
      'Pokud se připojení nezdaří, otevřete v Roku Nastavení > Systém > Rozšířená nastavení systému > Ovládání mobilními aplikacemi a nastavte síťový přístup na Výchozí nebo Permissive (u novějšího softwaru Roku nastavte „Ovládání mobilními aplikacemi“ na Povoleno).',
    ],
    encender='U televizorů Roku TV zapněte v Nastavení > Systém > Napájení možnost „Rychlé spuštění TV“. Přehrávače Roku zapojené do jiné televize se tímto způsobem zapnout nedají. Potom se vás aplikace při klepnutí na vypnutou televizi v Mando TV zeptá, zda ji má zapnout, a samo se připojí.',
    faq=[
      ('Funguje to s Roku Express nebo Streaming Stick?', 'Ano. Všechny přehrávače Roku a televizory Roku TV se ovládají stejným způsobem.'),
      ('Mando TV moje Roku nenajde. Co mám dělat?', 'Zkontrolujte, zda jsou obě zařízení ve stejné síti Wi-Fi a zda v Roku není vypnuté „Ovládání mobilními aplikacemi“. Můžete ho přidat také podle adresy IP.'),
      ('Potřebuji účet Roku?', 'Ne. Mando TV se připojuje přímo přes vaši Wi-Fi.'),
    ],
    guias=[('roku-403', 'Aplikace Roku nefunguje (chyba 403)'),
           ('roku-lost', 'Ztracený ovladač Roku: jak použít telefon'),
           ('tcl', 'Ovládací aplikace TCL'),
           ('hisense', 'Ovládací aplikace Hisense'),
           ('philips', 'Ovládací aplikace Philips'),
           ('guias', 'Všechny návody k ovládání televize telefonem')]),
  dict(clave='android', color='#2fbf8f', corto='Android TV a Google TV',
    titulo='Dálkový ovladač Google TV a Android TV | Mando TV',
    desc='Dálkový ovladač Google TV a Android TV (Sony, TCL, Xiaomi) v telefonu přes Wi-Fi. Tlačítka, klávesnice, aplikace a zapnutí zdarma; touchpad s Pro.',
    h1='Dálkový ovladač Google TV a Android TV jako aplikace v telefonu',
    intro='Mando TV je ovládací aplikace pro Android TV: přes domácí Wi-Fi z vašeho telefonu nebo počítače udělá dálkový ovladač k televizi s Android TV nebo Google TV. Funguje také z iPhonu a z Windows.',
    compat='Televizory s Google TV nebo Android TV od značek Sony, Philips, TCL, Hisense, Sharp, Xiaomi, Toshiba, Panasonic, Haier, Skyworth, JVC, Thomson, Motorola, OnePlus, iFFALCON, Kogan, Vu a dalších, dále Chromecast s Google TV, Google TV Streamer, onn. a Nvidia Shield. Některé z těchto značek prodávají i modely s jiným systémem: pokud televize zobrazuje úvodní obrazovku Google TV nebo má obchod Google Play, Mando TV ji ovládá.',
    h2=dict(funciones='Co můžete dělat se svou Android TV', como='Jak připojit Android TV k Mando TV',
            encender='Zapnutí Android TV telefonem', preguntas='Otázky k Android TV', guias='Návody pro Android TV'),
    funciones=[
      ('Všechna tlačítka', 'Směrový ovladač, OK, Zpět, Domů, hlasitost, ztlumení a přehrávání.'),
      ('Touchpad (Pro)', 'Přejížděním prstu rychle procházíte nabídkami Google TV.'),
      ('Dvě klávesnice', 'Pište do vyhledávání televize a ve většině aplikací na klávesnici telefonu. S funkcí Klávesnice YouTube (Pro) napište nebo řekněte, co chcete sledovat, a YouTube se na televizi otevře s výsledky.'),
      ('Aplikace', 'YouTube, Netflix, Disney+ a další aplikace otevřete jedním klepnutím.'),
      ('Zapnutí televize', 'U modelů se zapnutím přes síť Mando TV televizi zapne a samo se připojí.'),
      ('iPhone, Android a počítač', 'Funguje stejně na každém telefonu i počítači.'),
    ],
    pasos=[
      'Připojte telefon a televizi ke stejné síti Wi-Fi.',
      'Otevřete Mando TV: vaše Android TV se v seznamu objeví sama. Klepněte na ni.',
      'Televize zobrazí 6znakový kód. Zadejte ho do Mando TV (jen poprvé).',
    ],
    encender='Záleží na výrobci. V nastavení sítě nebo napájení hledejte „Wake on LAN“, „Zapnutí přes síť“, „Pohotovostní režim sítě“ nebo „Remote start“. Některé modely tuto možnost nemají. Potom se vás aplikace při klepnutí na vypnutou televizi v Mando TV zeptá, zda ji má zapnout, a samo se připojí.',
    faq=[
      ('Funguje to s Chromecastem s Google TV?', 'Ano, párování probíhá pomocí 6znakového kódu, který se zobrazí na obrazovce.'),
      ('Čím se liší od aplikace Google TV?', 'Mando TV nepotřebuje účet Google, funguje i ve Windows a jedinou aplikací ovládá také televizory LG, Samsung a Roku.'),
      ('Kód se na obrazovce nezobrazí. Co mám dělat?', 'Zavřete Mando TV, otevřete aplikaci znovu a znovu klepněte na televizi. Zkontrolujte, že televize není v hlubokém úsporném režimu.'),
    ],
    guias=[('androidtv-code', 'Android TV žádá párovací kód: co dělat'),
           ('androidtv', 'Android TV bez ovladače: jak použít telefon'),
           ('googletv-alt', 'Alternativa k ovladači Google TV v telefonu'),
           ('sony', 'Ovládací aplikace Sony'),
           ('tcl', 'Ovládací aplikace TCL'),
           ('hisense', 'Ovládací aplikace Hisense'),
           ('philips', 'Ovládací aplikace Philips'),
           ('guias', 'Všechny návody k ovládání televize telefonem')]),
]

GUIAS = [
  dict(clave='lost-tv', corto='Ztracený dálkový ovladač',
    titulo='Ztracený ovladač k televizi? Ovládejte ji telefonem',
    desc='Ztratili jste dálkový ovladač? Zapněte televizi tlačítkem na přístroji a použijte telefon jako ovladač. Postup pro LG, Samsung, Roku, Android TV. Zdarma.',
    h1='Ztracený dálkový ovladač? Co můžete udělat hned',
    intro='Ztracený dálkový ovladač se stane v každé domácnosti: zmizí přesně ve chvíli, kdy chcete něco sledovat. Dobrá zpráva je, že telefon ho přes domácí Wi-Fi dokáže nahradit. Tady je postup krok za krokem.',
    pasos=[
      'Zapněte televizi tlačítkem na přístroji. Bývá téměř vždy dole uprostřed nebo vzadu poblíž rohu. Někdy je to jedno tlačítko, jindy malý joystick.',
      'Připojte telefon ke stejné síti Wi-Fi jako televizi.',
      'Stáhněte si Mando TV, které je zdarma a nevyžaduje účet, a otevřete aplikaci. Vaše televize se v seznamu objeví sama. Klepněte na ni.',
      'Potvrďte připojení podle své značky. U LG a Samsungu televize zobrazí dotaz: potvrďte ho tlačítkem nebo joystickem na samotné televizi. U Android TV a Google TV zadáte 6znakový kód, který se objeví na obrazovce. Roku se na nic neptá.',
      'Hotovo. Šipky, OK, Zpět, Domů, hlasitost, programy a klávesnice jsou zdarma.',
      'Pro příště: v nastavení televize zapněte zapnutí přes síť (návod pro vaši značku najdete níže). Potom televizi zapnete z telefonu, aniž byste na ni sáhli.',
    ],
    extra=[
      ('Vyberte si návod pro svou značku', 'LG: [Ztracený ovladač LG](@lost-lg). Android TV a Google TV: [Android TV bez ovladače](@androidtv). Samsung: [Samsung televize bez ovladače](@samsung-lost). Roku: [Ztracený ovladač Roku](@roku-lost).'),
      ('Když se televize tlačítkem nezapne', 'Než začnete hledat jiný ovladač, zkontrolujte, zda je kabel pevně zasunutý a zásuvka pod proudem. Pokud tlačítko na televizi nic neudělá, problém je v televizi, ne v ovladači.'),
      ('Když ovladač prostě přestal fungovat', 'Zkuste nové baterie. Zda ještě vysílá signál, ověříte tak, že ho namíříte na kameru telefonu a stisknete tlačítko: u mnoha telefonů uvidíte na displeji fialové světlo. Pokud světlo vidíte a televize nereaguje, může být zakrytý snímač na televizi.'),
      ('Když jste vyměnili router a televize nemá Wi-Fi', 'Bez ovladače je těžší připojit televizi k nové síti. Nejjednodušší je zapojit televizi síťovým kabelem do routeru. Můžete také nastavit Wi-Fi se stejným názvem a heslem jako dříve: televize se k ní většinou připojí sama.'),
      ('Co je zdarma a co Pro', 'Zapnutí a vypnutí televize, šipky, OK, hlasitost, programy, číselná tlačítka, klávesnice, otevírání aplikací a přepínání vstupů jsou zdarma. Touchpad, hlas a rutiny patří do Mando TV Pro, což je jednorázový nákup bez předplatného.'),
    ],
    marca=None,
    faq=[
      ('Mohu televizi zapnout telefonem, když jsem ji nikdy nepřipojil(a)?', 'Poprvé ji zapnete tlačítkem na televizi. Až telefon připojíte a v nastavení televize zapnete zapnutí přes síť, můžete ji zapínat z aplikace.'),
      ('Musím si koupit nový ovladač?', 'Nemusíte. S Mando TV máte tlačítka, hlasitost, klávesnici a zapnutí zdarma. Pokud přesto chcete skutečný ovladač, hledejte podle přesného modelu televize.'),
      ('Funguje to, když televize nemá Wi-Fi?', 'Většinou ne. Telefon a televize musí být obvykle ve stejné síti Wi-Fi. Výjimkou je infračervený signál u telefonů s Androidem s infračerveným vysílačem, který ovládá i televize bez chytrých funkcí, a Bluetooth v betě od Androidu 9, který funguje zcela bez Wi-Fi s Google TV, Android TV a Fire TV.'),
    ]),
  dict(clave='lost-lg', corto='Ztracený ovladač LG',
    titulo='Ztracený ovladač LG? Použijte telefon',
    desc='Nemáte ovladač LG? Zapněte televizi tlačítkem na přístroji, potvrďte dotaz a ovládejte ji telefonem přes Wi-Fi. Bez účtu LG a bez reklam.',
    h1='Ztracený ovladač LG? Jak použít telefon',
    intro='Pokud jste ztratili ovladač LG nebo vám přestal fungovat Magic Remote, telefon ho přes Wi-Fi nahradí. Funguje to u televizí LG s webOS, tedy u téměř každé chytré televize LG od roku 2014. Nepotřebujete účet LG ani aplikaci ThinQ.',
    pasos=[
      'Zapněte televizi tlačítkem dole pod logem LG nebo tlačítkem vzadu. U mnoha modelů je to joystick: stisknutím otevřete nabídku a naklápěním vybíráte.',
      'Připojte telefon ke stejné síti Wi-Fi jako televizi.',
      'Otevřete Mando TV a v seznamu klepněte na svou televizi LG.',
      'Televize zobrazí dotaz s žádostí o povolení. Potvrďte ho joystickem nebo tlačítkem na televizi. Pokud jste tento telefon už jednou připojili, znovu se nezeptá.',
      'Hotovo. Šipky, OK, Zpět, Domů, hlasitost, programy a klávesnice jsou zdarma. Ukazatel je funkce Pro.',
      'S připojenou aplikací otevřete šipkami a OK nastavení a zapněte „Zapnout televizi pomocí mobilního zařízení“. Návod [Zapnutí LG televize telefonem](@lg-on) ukazuje, kde možnost najdete.',
    ],
    extra=[
      ('Když televize dotaz nezobrazí', 'Možná je povolení už uložené nebo je telefon v jiné síti. Zkontrolujte, zda jsou oba ve stejné Wi-Fi a zda je vypnuté VPN. Pokud se televize v seznamu neobjeví, pomůže vám návod [Telefon nenajde televizi](@not-found).'),
      ('Když televize ztratila Wi-Fi', 'Zapojte televizi síťovým kabelem do routeru, použije ho sama. Nebo nastavte Wi-Fi se stejným názvem a heslem jako dříve, protože se k ní televize většinou připojí sama.'),
      ('Když je televize na jiném vstupu', 'V telefonu klepněte na Vstupy a vyberte port HDMI. Více najdete v návodu [Změna vstupu HDMI na televizi bez ovladače](@hdmi).'),
    ],
    marca='lg',
    faq=[
      ('Potřebuji k používání Mando TV ovladač Magic Remote?', 'Potřebujete jen něco, čím poprvé potvrdíte dotaz, a k tomu stačí tlačítko nebo joystick na samotné televizi. Potom používáte už jen telefon.'),
      ('Potřebuji aplikaci LG ThinQ?', 'Ne. Mando TV se připojuje přímo přes vaši Wi-Fi a nevyžaduje účet LG.'),
      ('Mohu televizi LG telefonem vypnout i zapnout?', 'Vypnout ano. K zapnutí musíte mít v televizi zapnuté „Zapnout televizi pomocí mobilního zařízení“ a jednou se připojit, když byla zapnutá.'),
    ]),
  dict(clave='hdmi', corto='Změna HDMI bez ovladače',
    titulo='Změna vstupu HDMI bez ovladače (Samsung, LG, Roku)',
    desc='Změna vstupu HDMI bez ovladače u Samsungu, LG nebo Roku: tlačítkem na televizi nebo telefonem. Na začátek zdarma, bez reklam.',
    h1='Jak změnit vstup HDMI na televizi bez ovladače',
    intro='Konzole nebo přehrávač je připravený, ale televize zůstala na jiném vstupu a ovladač nikde. Vstup HDMI bez ovladače změníte dvěma způsoby: tlačítkem na samotné televizi, nebo telefonem. Tady je postup pro Samsung, LG a Roku.',
    pasos=[
      'Nejdřív zkuste to nejjednodušší: zapněte konzoli nebo přehrávač. Pokud je v televizi zapnuté HDMI-CEC (u Samsungu se jmenuje Anynet+, u LG SIMPLINK), televize na tento vstup přepne sama.',
      'Pokud nepřepne, použijte tlačítko na samotné televizi, dole uprostřed nebo vzadu. U mnoha televizí Samsung a LG je to joystick a otevře nabídku se Zdrojem nebo Vstupy.',
      'V této nabídce vyberte vstup: HDMI 1, HDMI 2 a tak dále. Číslo odpovídá portu, do kterého je zapojený kabel.',
      'Pokud dáváte přednost telefonu, připojte ho ke stejné síti Wi-Fi, otevřete Mando TV a klepněte na svou televizi.',
      'U LG a Roku klepněte na Vstupy a vyberte port HDMI. U Samsungu tlačítko Vstupy odešle do televize klávesu Zdroj a vybíráte šipkami a OK.',
      'Ke vstupům se dostanete také šipkami a OK na úvodní obrazovce televize. Podle značky a roku výroby se jmenují Zdroj, Připojená zařízení nebo Vstupy. U Roku TV jsou to dlaždice HDMI na úvodní obrazovce.',
    ],
    extra=[
      ('Samsung', 'Pokud v nabídce tlačítka na televizi není položka Zdroj, otevřete telefonem nabídku úvodní obrazovky a vlevo hledejte Zdroj nebo Připojená zařízení. Ovládáte ji šipkami a OK v Mando TV, které jsou zdarma.'),
      ('LG', 'Stiskněte joystick na televizi a najděte Vstupy. Telefonem můžete v Mando TV také otevřít seznam vstupů a klepnout na požadovaný.'),
      ('Roku TV', 'Na úvodní obrazovce je pro každý vstup dlaždice, například HDMI 1 nebo HDMI 2. Pohybujte se šipkami a otevřete ji tlačítkem OK, zdarma.'),
      ('Pokud jde o televizi s Android TV nebo Google TV', 'Seznam vstupů pro Android TV zatím v Mando TV není. Použijte tlačítko vstupu na samotné televizi nebo se ke vstupům dostaňte šipkami a OK z úvodní obrazovky. Pokud nemáte ovladač a chcete se připojit, přečtěte si [Android TV bez ovladače](@androidtv).'),
      ('Další pomoc', 'Pokud se televize vůbec nezapíná nebo nevíte, kde začít, přečtěte si [Ztracený dálkový ovladač](@lost-tv). Pro hraní na konzoli obsahuje návod [Zapnutí televize a přepnutí na HDMI konzole bez ovladače](@console) trik s HDMI-CEC.'),
    ],
    marca=None,
    faq=[
      ('Je změna vstupu HDMI zdarma?', 'Ano. Seznam vstupů v Mando TV je zdarma, stejně jako zapnutí televize a šipky, OK a hlasitost. Ke vstupům se dostanete také přes nabídku televize.'),
      ('Jak poznám, který vstup HDMI potřebuji?', 'Podívejte se na porty HDMI na televizi: každý má číslo. Vyberte ten, do kterého je zapojený kabel konzole nebo přehrávače.'),
      ('Co když se televize nezapne?', 'Zapněte ji tlačítkem na přístroji. Pokud jste ji už jednou připojili a zapnuli zapnutí přes síť, můžete ji zapnout také telefonem.'),
    ]),
  dict(clave='androidtv', corto='Android TV bez ovladače',
    titulo='Android TV bez ovladače: použijte telefon',
    desc='Nemáte ovladač k Android TV nebo Google TV? Připojte telefon 6znakovým kódem z obrazovky. Zdarma, bez účtu, bez reklam.',
    h1='Android TV bez ovladače: jak použít telefon',
    intro='Pokud jste ztratili ovladač k Android TV nebo Google TV nebo v něm došly baterie, telefon ho nahradí. A to nejlepší: k připojení ovladač nepotřebujete, protože televize zobrazí na obrazovce kód a vy ho opíšete do telefonu. Funguje to u televizí Sony, Philips, TCL, Hisense, Sharp a Xiaomi s Android TV, u Chromecastu s Google TV a u Nvidia Shield.',
    pasos=[
      'Zapněte televizi tlačítkem na přístroji. Bývá téměř vždy dole uprostřed nebo vzadu poblíž rohu.',
      'Připojte telefon ke stejné síti Wi-Fi jako televizi.',
      'Stáhněte si Mando TV, které je zdarma a nevyžaduje účet Google, a otevřete aplikaci. V seznamu klepněte na svou televizi.',
      'Televize zobrazí kód ze 6 písmen a číslic. Zadejte ho v telefonu a klepněte na Spárovat. Ovladač k tomu nepotřebujete.',
      'Nyní můžete používat šipky, OK, Zpět, Domů, hlasitost, ztlumení a klávesnici. Jsou zdarma, stejně jako seznam aplikací. Touchpad je Pro.',
      'Abyste příště mohli televizi zapnout z telefonu, v nastavení sítě nebo napájení hledejte „Wake on LAN“, „Zapnutí přes síť“, „Pohotovostní režim sítě“ nebo „Remote start“.',
    ],
    extra=[
      ('Když se televize z telefonu zapnout nedá', 'Ne každá Android TV se dá zapnout přes síť; záleží na výrobci a modelu. Pokud ji ta vaše neumí, zapněte ji tlačítkem na televizi a pokračujte v telefonu. Vypnout ji můžete z aplikace.'),
      ('Chromecast s Google TV, Google TV Streamer a Shield', 'Připojují se stejným způsobem: stejná Wi-Fi, klepnout na zařízení v seznamu a zadat kód. Pokud televize zobrazuje jiný vstup, přepněte ji na port HDMI, ve kterém je zařízení zapojené, jak popisuje návod [Změna vstupu HDMI na televizi bez ovladače](@hdmi).'),
      ('Když se kód nezobrazí nebo se hlásí jako chybný', 'Zkontrolujte, zda je televize opravdu zapnutá a ne v pohotovostním režimu. Kód se mění při každé žádosti: funguje jen ten poslední. Více podrobností najdete v návodu [Android TV žádá párovací kód](@androidtv-code).'),
      ('Aplikace Google, nebo Mando TV', 'Google má vlastní aplikaci, ke které potřebujete účet Google. Mando TV účet nevyžaduje, funguje i ve Windows a jedinou aplikací ovládá také televizory LG, Samsung a Roku.'),
    ],
    marca='android',
    faq=[
      ('Potřebuji k párování telefonu ovladač?', 'Ne. Kód se zobrazí na obrazovce televize a vy ho opíšete do telefonu. Stačí televizi zapnout, v případě potřeby tlačítkem na přístroji.'),
      ('Funguje to s Hisense?', 'U televizí Hisense s Android TV nebo Google TV ano. Televizory Hisense s jiným systémem kompatibilní nejsou.'),
      ('Mohu psát na klávesnici telefonu?', 'Ano, jsou dvě. Bezplatná klávesnice píše do vyhledávání a textových polí televize i většiny aplikací. YouTube a Netflix přijímají jen vlastní klávesnici na obrazovce, proto pro YouTube existuje Klávesnice YouTube (Pro): napište nebo řekněte, co chcete sledovat, a YouTube se na televizi otevře s výsledky. Netflix se ovládá šipkami a OK.'),
    ]),
  dict(clave='lg-on', corto='Zapnutí LG telefonem',
    titulo='Zapnutí LG televize telefonem (návod)',
    desc='Zapněte LG televizi telefonem přes Wi-Fi: aktivujte „Zapnout televizi pomocí mobilního zařízení“ a použijte Mando TV. Krok za krokem, zdarma.',
    h1='Jak zapnout LG televizi telefonem',
    intro='LG televizi můžete zapnout telefonem, nejdřív ale musíte v televizi zapnout jedno nastavení. Potom ji telefon přes vaši Wi-Fi zapne i bez ovladače. Zabere to pět minut a děláte to jen jednou.',
    pasos=[
      'Připojte telefon a televizi LG ke stejné síti Wi-Fi.',
      'V televizi otevřete Nastavení a najděte „Zapnout televizi pomocí mobilního zařízení“. Najdete ho v Nastavení > Obecné > Zařízení > Externí zařízení (u starších modelů Připojení > Správa mobilního připojení).',
      'Zapněte „Zapnout přes Wi-Fi“. Pokud je televize připojená síťovým kabelem, zapněte místo toho možnost pro kabel.',
      'Pokud má televize „Rychlé spuštění+“, zapněte i to.',
      'Při zapnuté televizi otevřete v telefonu Mando TV a v seznamu klepněte na svou televizi LG. Potvrďte dotaz, který se zobrazí na obrazovce. Tak se aplikace naučí televizi probudit.',
      'Vypněte televizi a zkuste to: v Mando TV klepněte na televizi a aplikace se zeptá, zda ji má zapnout.',
    ],
    extra=[
      ('Když se nezapne', 'Televize musela být ve stejné Wi-Fi, když se vypínala. Zkontrolujte, zda je nastavení stále aktivní a telefon je ve stejné síti. Pokud jste vyměnili router, připojte se znovu při zapnuté televizi.'),
    ],
    marca='lg',
    faq=[
      ('Mohu LG televizi zapnout telefonem, když jsem ji nikdy nepřipojil(a)?', 'Ne. Nejdřív musíte v televizi zapnout „Zapnout televizi pomocí mobilního zařízení“ a jednou se přes Mando TV připojit, když je televize zapnutá.'),
      ('Potřebuji aplikaci LG ThinQ?', 'Ne. Mando TV se připojuje přímo přes vaši Wi-Fi a nevyžaduje účet LG.'),
      ('Funguje to přes mobilní data?', 'Ne. Telefon a televize musí být ve stejné síti Wi-Fi.'),
    ]),
  dict(clave='console', corto='Televize a konzole bez ovladače',
    titulo='Bez ovladače? Zapněte televizi a změňte HDMI',
    desc='Vychází hra a nemáte ovladač? Zapněte televizi a telefonem přepněte na HDMI vstup PS5 nebo Xboxu. Zdarma, bez reklam.',
    h1='Jak zapnout televizi a přepnout bez ovladače na HDMI vstup konzole',
    intro='Den vydání GTA VI, konzole je připravená a ovladač od televize zmizel kdesi mezi polštáři gauče. Stává se to častěji, než by se zdálo. S Mando TV telefon zapne televizi a přes domácí Wi-Fi ji přepne na vstup vaší PlayStation nebo Xboxu.',
    pasos=[
      'Připojte telefon ke stejné síti Wi-Fi jako televizi.',
      'Otevřete Mando TV a v seznamu klepněte na svou televizi (Samsung, LG, Roku nebo Android TV).',
      'Pokud je televize vypnutá, klepněte na Zapnout. Funguje to, když máte v televizi zapnuté zapnutí přes síť. Pokud jste ho nikdy nezapnuli, zapněte televizi tentokrát tlačítkem na přístroji a pro příště to nastavte.',
      'Zapněte konzoli. Pokud je zapnuté HDMI-CEC (viz bezplatný trik níže), televize přepne na její vstup sama.',
      'Pokud nepřepne, klepněte v Mando TV na Vstupy a vyberte port HDMI, ve kterém je konzole: HDMI 1, HDMI 2 a tak dále.',
      'K ovládání hlasitosti při hraní použijte velká tlačítka v aplikaci.',
    ],
    extra=[
      ('Bezplatný trik: nechte konzoli přepnout televizi', 'PS5 i Xbox umí zapnout televizi a hned při startu přeskočit na svůj vstup HDMI díky HDMI-CEC. U PS5 to najdete v Nastavení > Systém > HDMI > Povolit propojení zařízení HDMI. U Xboxu otevřete Nastavení > Obecné > Možnosti TV a zobrazení a hledejte možnost ovládání zařízení. V televizi se funkce podle značky jmenuje jinak: Anynet+ u Samsungu, SIMPLINK u LG a BRAVIA Sync nebo ovládání HDMI u ostatních.'),
      ('Když televize zůstane na jiném obraze', 'Pokud je konzole zapnutá, ale televize stále ukazuje anténu nebo aplikaci, vstup nepřepnula. V telefonu klepněte na Vstupy a vyberte vstup HDMI konzole. Nebo se šipkami a OK dostaňte do vstupů televize, případně použijte tlačítko na samotné televizi, a vyberte port HDMI. Číslo odpovídá portu, do kterého jste zapojili kabel konzole.'),
      ('Když jde o Roku TV', 'Tlačítko na televizi, většinou dole uprostřed nebo vzadu, ji zapne. Zbytek už zařídí telefon.'),
    ],
    marca=None,
    faq=[
      ('Má Mando TV něco společného s GTA VI?', 'Ne. Mando TV nemá žádnou souvislost se společnostmi Rockstar Games ani Take-Two. Aplikace vám jen pomůže neztrácet herní čas hledáním ovladače.'),
      ('Je změna vstupu HDMI zdarma?', 'Ano. Seznam vstupů v Mando TV je zdarma, stejně jako zapnutí televize a šipky, OK a hlasitost. Konzoli také můžete nechat přepnout vstup sama pomocí HDMI-CEC.'),
      ('Funguje to s mou televizí?', 'Funguje s televizory Samsung, LG, Roku a Android TV ve stejné síti Wi-Fi. Pokud je vaše jiné značky, může vám trik s HDMI-CEC přesto pomoci.'),
      ('Mohu to použít ke hraní GTA VI (GTA 6) na PS5 nebo Xboxu?', 'Mando TV do konzole ani do hry nezasahuje. Jen zařídí, aby byla televize zapnutá a na správném vstupu HDMI, takže si můžete sednout a hrát.'),
    ]),
  dict(clave='samsung-lost', corto='Samsung televize bez ovladače',
    titulo='Ztracený ovladač Samsung? Použijte telefon',
    desc='Ztracený nebo rozbitý ovladač Samsung? Použijte telefon jako dálkový ovladač k televizi s Tizen přes Wi-Fi. Snadno s Mando TV, zdarma, bez reklam.',
    h1='Samsung televize bez původního ovladače: jak použít telefon',
    intro='Pokud jste ztratili ovladač Samsung nebo přestal fungovat, můžete telefon přes Wi-Fi použít jako dálkový ovladač. Funguje to u televizí Samsung s Tizen, rok výroby 2016 a novější.',
    pasos=[
      'Zapněte televizi tlačítkem na přístroji. U většiny modelů je dole nebo vzadu, někdy jako malý joystick.',
      'Zkontrolujte, zda je televize připojená k vaší Wi-Fi a telefon je ve stejné síti.',
      'Otevřete v telefonu Mando TV. Vaše televize Samsung se v seznamu objeví sama. Klepněte na ni.',
      'Televize vás požádá o potvrzení připojení. U většiny modelů ho potvrdíte tlačítky na televizi nebo joystickem vzadu.',
      'Hotovo, nyní můžete používat telefon jako dálkový ovladač. Tlačítka, klávesnice a aplikace jsou zdarma; touchpad je funkce Pro.',
      'Abyste příště mohli televizi zapnout z telefonu, otevřete Nastavení > Obecné > Síť > Expertní nastavení a zapněte „Zapnout pomocí mobilního zařízení“.',
    ],
    extra=[
      ('Když se televize o povolení nezeptá', 'Možná je povolení už uložené nebo je televize v jiné Wi-Fi. Zavřete Mando TV a otevřete aplikaci znovu při zapnuté televizi. Pokud je televize starší než 2016, používá jiný systém, který zatím nepodporujeme.'),
      ('Když jste povolení omylem zakázali', 'V televizi otevřete Nastavení > Obecné > Správce externích zařízení > Správce připojení zařízení a nastavte Mando TV na povoleno. Pokud telefon televizi stále nenajde, přečtěte si [Telefon nenajde televizi](@not-found).'),
    ],
    marca='samsung',
    faq=[
      ('Jak potvrdím připojení, když nemám ovladač?', 'U většiny modelů ho potvrdíte tlačítky na televizi nebo joystickem vzadu. Pokud váš model tlačítka nemá, napište na hola@mandotv.app a pomůžeme vám.'),
      ('Vyžaduje Mando TV účet Samsung?', 'Ne. Připojení vede přímo přes vaši Wi-Fi, bez účtu Samsung.'),
      ('Funguje to s mou starší televizí Samsung?', 'Funguje s televizemi Samsung s Tizen, rok výroby 2016 a novější.'),
    ]),
  dict(clave='wifi', corto='Telefon jako ovladač přes Wi-Fi',
    titulo='Telefon jako dálkový ovladač: ovládání televize přes Wi-Fi',
    desc='Připojte telefon přes Wi-Fi k televizi a používejte ho jako ovladač u Samsungu, LG, Roku a Google TV. Postup podle značky s Mando TV. Zdarma.',
    h1='Jak připojit telefon přes Wi-Fi k televizi jako dálkový ovladač',
    intro='Potřebujete jen telefon a televizi ve stejné síti Wi-Fi a ovládací aplikaci. Mando TV najde vaši televizi samo a funguje se Samsungem, LG, Roku, Google TV a Android TV.',
    pasos=[
      'Připojte telefon a televizi ke stejné síti Wi-Fi.',
      'Otevřete Mando TV. Vaše televize se v seznamu objeví sama. Klepněte na ni.',
      'Potvrďte připojení podle své značky (podrobnosti najdete níže).',
      'Televizi ovládejte tlačítky nebo klávesnicí telefonu. Touchpad je funkce Pro.',
    ],
    extra=[
      ('Samsung', 'Televize se zeptá, zda připojení povolujete. Poprvé ho potvrďte na obrazovce. Funguje to s Tizen, rok výroby 2016 a novější. Aby šla televize zapnout z telefonu, zapněte v Nastavení > Obecné > Síť > Expertní nastavení možnost „Zapnout pomocí mobilního zařízení“.'),
      ('LG', 'Televize zobrazí dotaz s žádostí o povolení. Poprvé ho potvrďte. Aby šla televize zapnout z telefonu, najděte v nastavení „Zapnout televizi pomocí mobilního zařízení“ a zapněte „Zapnout přes Wi-Fi“.'),
      ('Roku', 'Roku nevyžaduje párování: klepněte na něj v seznamu a jste připojeni. Pro zapnutí aktivujte v Nastavení > Systém > Napájení možnost „Rychlé spuštění TV“.'),
      ('Google TV a Android TV', 'Televize zobrazí na obrazovce kód. Poprvé ho zadejte do Mando TV. Pro zapnutí hledejte v nastavení „Wake on LAN“, „Zapnutí přes síť“ nebo „Pohotovostní režim sítě“.'),
    ],
    marca=None,
    faq=[
      ('Potřebuji k použití telefonu jako ovladače internet?', 'Potřebujete telefon a televizi ve stejné síti Wi-Fi. Mando TV se přes tuto síť připojuje přímo k televizi.'),
      ('Proč se moje televize v seznamu neobjevuje?', 'Zkontrolujte, zda je televize zapnutá a telefon nepoužívá mobilní data ani jinou Wi-Fi. Některé routery mají síť pro hosty, která zařízení od sebe odděluje.'),
      ('Mohu Mando TV používat na iPhonu nebo na telefonu s Androidem?', 'Na iPhonu a iPadu ano: aplikace už je v App Store. Pro Windows je také v Microsoft Store. Android přijde brzy: můžete se zapojit do bezplatného předběžného přístupu na Google Play.'),
    ]),
  dict(clave='pc', corto='Ovládání televize z počítače',
    titulo='Ovládání televize z počítače s Windows (zdarma)',
    desc='Použijte počítač s Windows jako dálkový ovladač k Samsungu, LG, Roku nebo Google TV přes Wi-Fi. Tlačítka, klávesnice a aplikace zdarma; zkratky s Pro.',
    h1='Jak ovládat televizi počítačem s Windows',
    intro='Pokud trávíte den u počítače, nemusíte hledat ovladač: Mando TV pro Windows ovládá vaši televizi Samsung, LG, Roku, Google TV nebo Android TV přes domácí Wi-Fi. Hodí se k přepínání aplikací, zesílení zvuku nebo psaní do YouTube na klávesnici počítače.',
    pasos=[
      'Stáhněte si Mando TV zdarma z Microsoft Store do počítače s Windows 10 nebo 11.',
      'Zkontrolujte, zda jsou počítač a televize ve stejné síti (Wi-Fi nebo kabel, ale přes stejný router).',
      'Otevřete Mando TV: vaše televize se v seznamu objeví sama. Klepněte nebo klikněte na ni.',
      'Poprvé potvrďte připojení na obrazovce televize (u Google TV a Android TV zadáte kód, který televize zobrazí).',
      'Hotovo: používejte tlačítka nebo klávesnici k psaní do vyhledávacího pole televize. Touchpad je funkce Pro.',
    ],
    extra=[
      ('Klávesové zkratky v počítači (Pro)', 'S Mando TV Pro ovládáte televizi klávesnicí počítače: šipky k pohybu, Enter pro OK, Backspace nebo Esc pro Zpět, + a - pro hlasitost, M pro ztlumení a mezerník pro pozastavení.'),
      ('Mini ovladač vždy navrchu (Pro)', 'Malé okno s ovladačem můžete mít stále na očích, zatímco pracujete nebo hrajete na počítači.'),
      ('Mluvte s televizí z počítače (Pro)', 'S Mando TV Pro dáváte televizi příkazy přes mikrofon počítače: „otevři YouTube“, „zesil“ nebo „vypni za 30 minut“, tak, jak mluvíte. Ve Windows se řeč rozpoznává přímo v počítači: nepotřebujete internet, nemusíte nic měnit v nastavení Windows a funguje to v 6 jazycích aplikace. To, co řeknete, počítač neopustí a neukládá se. Jen u velmi starých procesorů aplikace přechází na diktování Windows. Pro to musí být v nastavení soukromí zapnuté online rozpoznávání řeči a ve Windows přidána čeština (Česko). Pokud něco chybí, aplikace vám to oznámí a tlačítkem otevře příslušné nastavení.'),
    ],
    marca=None,
    faq=[
      ('Potřebuji k ovládání televize z počítače kabel nebo Bluetooth?', 'Ne. Mando TV se připojuje přes domácí síť: počítač a televize musí být jen u stejného routeru.'),
      ('Funguje to s každou televizí?', 'Funguje s televizemi Samsung s Tizen (rok výroby 2016 a novější), LG s webOS, Roku a Google TV nebo Android TV (Sony, Philips, TCL, Hisense, Sharp, Xiaomi, Toshiba, Panasonic, Haier, Skyworth a další).'),
      ('Kolik to stojí?', 'Tlačítka, klávesnice a zapnutí přes síť jsou zdarma a bez reklam. Mando TV Pro je jednorázový nákup bez předplatného za doplňky, jako je touchpad, klávesové zkratky v počítači a mini ovladač.'),
      ('Proč mi mikrofon ve Windows nerozumí?', 'Zkontrolujte, zda je hlasová funkce aktivní (patří do Pro) a zda ve Windows funguje mikrofon počítače. Na téměř všech počítačích se řeč rozpoznává přímo v zařízení, bez internetu. Jen u velmi starých procesorů aplikace používá diktování Windows. Pak zkontrolujte, zda je v nastavení soukromí Windows zapnuté online rozpoznávání řeči a zda má Windows v jazykových nastaveních češtinu (Česko). Mando TV tento jazyk používá, jen dokud poslouchá.'),
    ]),
  dict(clave='roku-403', corto='Aplikace Roku nefunguje',
    titulo='Aplikace Roku nefunguje? Oprava chyby 403',
    desc='Telefon je připojený, ale Roku nereaguje? Zapněte „Ovládání mobilními aplikacemi“ v 5 krocích a znovu používejte telefon jako ovladač.',
    h1='Aplikace Roku nefunguje: jak problém vyřešit',
    intro='Pokud telefon Roku najde a připojí se, ale žádné tlačítko nic neudělá, je to téměř vždy kvůli nastavení v samotném Roku, které blokuje ovládací aplikace. Novější verze Roku jsou ve výchozím stavu omezenější. V nabídce Roku to vyřešíte za minutu.',
    pasos=[
      'Na Roku stiskněte Domů a otevřete Nastavení.',
      'Otevřete Systém a potom Rozšířená nastavení systému.',
      'Přejděte na „Ovládání mobilními aplikacemi“. U některých modelů se jmenuje „Externí ovládání“.',
      'V části „Síťový přístup“ vyberte Výchozí nebo Permissive. Pokud je u vašeho modelu jen přepínač, nechte ho na Povoleno.',
      'Vraťte se v telefonu do Mando TV a klepněte na své Roku. Tlačítka teď reagují.',
    ],
    extra=[
      ('Jak poznáte, že je to váš problém', 'Příznak je jasný: telefon vidí Roku v seznamu a připojí se, ale po klepnutí na tlačítko se nic nestane. Uvnitř Roku odpovídá chybou 403, což znamená „zakázáno“. Mando TV to při připojení pozná a zobrazí vám přesně tento postup.'),
      ('Výchozí, nebo Permissive: co vybrat?', 'Stačí Výchozí: přijímá příkazy z vaší domácí sítě, což ovladač potřebuje. Permissive je otevřenější a je potřeba jen v neobvyklých sítích.'),
      ('Když nemáte ovladač Roku', 'Pokud je nastavení na Zakázáno, změníte ho jen skutečným ovladačem Roku. Půjčte si ho, abyste to jednou změnili; potom už všechno zvládnete telefonem. Přečtěte si také [Ztracený ovladač Roku](@roku-lost).'),
    ],
    marca='roku',
    faq=[
      ('Proč moje Roku přestalo reagovat, i když dřív fungovalo?', 'Aktualizace Roku může toto nastavení více omezit. Nezpůsobuje to váš telefon ani Wi-Fi: stačí znovu povolit ovládání aplikacemi.'),
      ('Týká se to Roku TV i přehrávačů Roku?', 'Ano. Nastavení je u přehrávačů Roku i televizorů Roku TV ve stejné nabídce.'),
      ('Je bezpečné nechat nastavení na Výchozí?', 'Ano. Přijímá jen příkazy ze zařízení ve vaší domácí síti.'),
    ]),
  dict(clave='not-found', corto='Telefon nenajde televizi',
    titulo='Telefon nenajde televizi? 6 věcí ke kontrole',
    desc='Ovládací aplikace nenajde vaši televizi? Zkontrolujte Wi-Fi, VPN a přístup k místní síti. Pro Samsung, LG, Roku a Android TV.',
    h1='Telefon nenajde televizi: co zkontrolovat',
    intro='Otevřete ovládací aplikaci a seznam je prázdný, nebo se televize objeví, ale připojení se přeruší. Skoro vždy je příčina v síti, ne v televizi. Projděte tyto body popořadě: první vyřeší většinu případů.',
    pasos=[
      'Podívejte se, v jaké Wi-Fi je telefon a v jaké televize. Musí to být stejná síť se stejným názvem. Síť pro hosty nefunguje, protože zařízení od sebe odděluje.',
      'Pokud používáte VPN, vypněte ji. Se zapnutou VPN telefon vede provoz do internetu přes jinou síť a zařízení u vás doma nevidí, nebo se připojení po několika sekundách přeruší.',
      'Na chvíli vypněte mobilní data. Některé telefony při slabém signálu přepnou z Wi-Fi na mobilní data samy.',
      'Zapněte televizi a počkejte, až se úplně spustí. Vypnutá televize na hledání neodpovídá.',
      'Na iPhonu zkontrolujte, zda má aplikace oprávnění „Místní síť“: Nastavení > Soukromí a zabezpečení > Místní síť.',
      'Pokud se stále neobjeví, přidejte ji ručně: v Mando TV klepněte na „Přidat podle IP“ a zadejte adresu IP televize.',
    ],
    extra=[
      ('Nechte se vést aplikací', 'V seznamu televizí je tlačítko pro případ, že se vaše televize nezobrazí. Aplikace krok za krokem zkontroluje nejčastější příčiny (stejná Wi-Fi, VPN, oprávnění k místní síti a další) a po každé opravě zobrazí tlačítko pro opakovanou kontrolu. Průvodce je zdarma.'),
      ('Kde najdete adresu IP televize', 'Je v nabídce sítě televize a podle modelu se trochu liší. U LG: Nastavení, Síť, Připojení Wi-Fi, Rozšířené nastavení Wi-Fi. U Samsungu: Nastavení, Obecné, Síť, Stav sítě, Nastavení IP. U Roku: Nastavení, Síť, Informace. U Android TV a Google TV: Nastavení, Síť a internet, potom klepněte na svou síť. Je to číslo jako 192.168.1.86.'),
      ('Když se objeví, ale připojení se přeruší', 'Pokud se připojení přeruší po několika sekundách, příčina je většinou v telefonu: VPN, přepnutí do jiné Wi-Fi nebo úsporný režim. Vypněte VPN, zůstaňte ve stejné Wi-Fi a zkuste to znovu.'),
      ('Wi-Fi 2,4 a 5 GHz', 'Nezáleží na tom, zda je telefon v síti 5 GHz a televize v síti 2,4 GHz, pokud obě pocházejí ze stejného routeru. Pokud máte opakovač Wi-Fi a televize se přesto neobjeví, přibližte se s telefonem k hlavnímu routeru a zkuste to znovu.'),
    ],
    marca=None,
    faq=[
      ('Mohu televizi ovládat přes mobilní data?', 'Ne. Signál ovladače vede přes vaši domácí Wi-Fi, proto musí být telefon a televize ve stejné síti.'),
      ('Proč to se zapnutou VPN nefunguje?', 'Protože VPN vede veškerý provoz telefonu přes jinou síť a telefon pak zařízení u vás doma nevidí. Vypněte ji, dokud ovladač používáte.'),
      ('Funguje to přes Bluetooth nebo infračervený signál?', 'U chytrých televizí Mando TV používá Wi-Fi. Infračervený signál funguje jen na telefonech s Androidem s infračerveným vysílačem a je určený pro televize, které nejsou chytré. Bluetooth je v betě, zdarma a jen od Androidu 9: telefon se k televizi připojí jako klávesnice a ovladač Bluetooth, zcela bez Wi-Fi. Funguje s Google TV, Android TV a Fire TV; u dalších značek, které přijímají klávesnice Bluetooth, může fungovat, Roku je nepřijímá.'),
    ]),
  dict(clave='androidtv-code', corto='Párovací kód Android TV',
    titulo='Android TV žádá párovací kód: co dělat',
    desc='Vaše Android TV nebo Google TV při připojení zobrazí 6znakový kód. Jak ho zadat a co dělat, když se nezobrazí nebo je chybný.',
    h1='Android TV žádá párovací kód: co dělat',
    intro='Když telefon poprvé připojujete k Android TV nebo Google TV, televize zobrazí na obrazovce 6znakový kód. Je to normální a stane se to jen jednou: zajišťuje, že vaši televizi nemůže ovládat nikdo jiný. Tady se dozvíte, jak ho zadat a co dělat, když se nezobrazí.',
    pasos=[
      'Zapněte televizi a nechte zobrazenou úvodní obrazovku.',
      'Otevřete v telefonu Mando TV, ve stejné Wi-Fi jako televize, a v seznamu klepněte na svou televizi.',
      'Podívejte se na obrazovku televize: zobrazí se kód ze 6 písmen a číslic.',
      'Zadejte ho v telefonu přesně tak, jak je zobrazen, a klepněte na Spárovat. Písmena jsou jen od A do F, takže kulatý znak je vždy číslice nula.',
      'Hotovo. Televize si váš telefon zapamatuje a na kód se znovu nezeptá.',
    ],
    extra=[
      ('Když se kód na televizi nezobrazí', 'Zkontrolujte, zda je televize opravdu zapnutá a ne v pohotovostním režimu, a zda je telefon ve stejné Wi-Fi. V telefonu znovu klepněte na televizi. Pokud se stále nezobrazí, televizi restartujte: odpojte ji na deset sekund ze zásuvky, zapojte zpět a zkuste to znovu.'),
      ('Když se kód hlásí jako chybný', 'Kód se mění při každé žádosti. Pokud jste zadávali dlouho nebo jste si ho vyžádali dvakrát, funguje jen ten poslední na obrazovce. V telefonu znovu klepněte na televizi a zadejte nový kód.'),
      ('Když se televize na kód zeptá znovu', 'To se stane, pokud byla televize obnovena do továrního nastavení nebo smažete data aplikace v telefonu. Spárujte znovu a uloží se. Pokud nemáte vůbec žádný ovladač, přečtěte si [Android TV bez ovladače](@androidtv).'),
    ],
    marca='android',
    faq=[
      ('Které televize tento kód používají?', 'Ty s Android TV nebo Google TV: Sony, Philips, TCL, Hisense, Sharp, Xiaomi, Chromecast s Google TV a některé další.'),
      ('Potřebuji v telefonu účet Google?', 'Ne. Stačí kód na obrazovce.'),
      ('Je to bezpečné?', 'Ano. Kód dokazuje, že sedíte před televizí: nikdo se nemůže spárovat, aniž by kód na obrazovce viděl.'),
    ]),
  dict(clave='roku-lost', corto='Ztracený ovladač Roku',
    titulo='Ztracený ovladač Roku? Použijte telefon přes Wi-Fi',
    desc='Ztratili jste ovladač Roku? Telefon ho přes Wi-Fi nahradí. Jednoduchý postup, i když jste vyměnili router a Roku nemá Wi-Fi.',
    h1='Ztracený ovladač Roku: jak použít telefon',
    intro='Pokud jste ztratili ovladač Roku nebo přestal fungovat, telefon ho nahradí, dokud je Roku stále připojené k vaší Wi-Fi. A pokud jste změnili Wi-Fi nebo router, existuje cesta i pro to.',
    pasos=[
      'Nejdřív zkuste ovladač rozeznít. Pokud má váš ovladač Roku reproduktor, například Roku Voice Remote Pro, otevřete Mando TV, připojte se k Roku a použijte možnost rozeznění ovladače, abyste ho našli. Funguje to jen s ovladači Roku s reproduktorem a Roku musí být zapnuté.',
      'Zapněte televizi a nechte Roku zapojené. Nemusíte na něj sahat.',
      'Připojte telefon ke stejné Wi-Fi, kterou používá Roku.',
      'Otevřete Mando TV. Roku se v seznamu objeví samo. Klepněte na ně.',
      'Používejte šipky, OK, Domů a Zpět jako na svém obvyklém ovladači. Roku se na kód neptá.',
      'Pokud tlačítka nic nedělají, Roku blokuje ovládání aplikacemi: návod [Aplikace Roku nefunguje](@roku-403) vysvětluje, jak ho povolit.',
    ],
    extra=[
      ('Když Roku nemá Wi-Fi (výměna routeru nebo stěhování)', 'Bez ovladače se nedostanete do nabídky a nenastavíte novou síť, ale existuje trik: Roku se samo připojí k síti, která má stejný název a heslo jako ta stará. Na jiném telefonu vytvořte hotspot Wi-Fi přesně s tímto názvem a heslem, připojte k němu telefon s Mando TV a Roku se objeví v seznamu. Odtud otevřete Nastavení, Síť a připojte ho k nové Wi-Fi.'),
      ('Když jde o Roku TV', 'Televizory Roku TV mají tlačítko na přístroji, téměř vždy dole uprostřed nebo vzadu, které televizi zapne. To stačí k zapnutí a dál pokračujete telefonem.'),
      ('Když raději koupíte jiný ovladač', 'Dbejte na to, aby odpovídal vašemu modelu. Malé přehrávače Roku za televizí potřebují ovladač bez infračerveného signálu, protože infračervený signál k nim nedosáhne.'),
    ],
    marca='roku',
    faq=[
      ('Může telefon Roku zapnout?', 'Připojený přehrávač Roku je stále zapnutý. U Roku TV ho Mando TV zapne přes Wi-Fi, pokud je v Nastavení > Systém > Napájení zapnuté „Rychlé spuštění TV“.'),
      ('A co hlasitost?', 'U Roku TV telefon hlasitost zesiluje a zeslabuje. U přehrávače Roku zapojeného přes HDMI to závisí na televizi: u mnoha funguje, u jiných ne.'),
      ('Musím si zakládat účet?', 'Ne. Mando TV účet nevyžaduje a stejnou aplikací ovládá také televizory Samsung, LG a Android TV.'),
    ]),
]

SOPORTE = dict(
  titulo='Nápověda: připojení a zapnutí televize s Mando TV',
  desc='Jak připojit ovladač Mando TV k LG, Samsungu, Roku nebo Android TV, zapnout televizi z telefonu a vyřešit potíže.',
  h1='Nápověda',
  intro='Nejčastější otázky v pořadí jednotlivých kroků. Pokud svou nenajdete, napište nám na <a href="mailto:hola@mandotv.app?subject=Pomoc%20s%20Mando%20TV">hola@mandotv.app</a> a odpovíme.',
)
SOPORTE_HTML = '''      <h2 id="encontrar">Nalezení televize</h2>
      <div class="preguntas">
        <details open><summary>Moje televize se v seznamu neobjevuje</summary>
          <ol>
            <li>Zkontrolujte, zda jsou telefon a televize ve stejné síti Wi-Fi. Pokud má váš router síť 2,4 GHz a 5 GHz s různými názvy, někdy se navzájem nevidí.</li>
            <li>Ujistěte se, že je televize zapnutá.</li>
            <li>Na iPhonu zkontrolujte, zda má Mando TV oprávnění „Místní síť“, v Nastavení, Mando TV.</li>
            <li>V seznamu televizí klepněte na tlačítko pro případ, že se vaše televize nezobrazí: aplikace krok za krokem zkontroluje nejčastější příčiny (stejná Wi-Fi, VPN, oprávnění k místní síti a další) a po každé opravě zobrazí tlačítko pro opakovanou kontrolu.</li>
            <li>Pokud se stále neobjeví, klepněte na tlačítko +, vyberte značku a zadejte adresu IP televize. Najdete ji v nabídce sítě televize (například 192.168.1.50).</li>
          </ol>
        </details>
        <details><summary>Funguje to přes mobilní data nebo na cestách?</summary>
          <p>Ne. Mando TV komunikuje s televizí uvnitř vaší domácí sítě, proto musí být telefon připojený k této Wi-Fi.</p>
        </details>
      </div>

      <h2 id="conectar">První připojení</h2>
      <p>Úplné návody podle značky: <a href="@@R_lg@@">LG</a>, <a href="@@R_samsung@@">Samsung</a>, <a href="@@R_roku@@">Roku</a> a <a href="@@R_android@@">Android TV</a>.</p>
      <div class="preguntas">
        <details><summary>LG</summary>
          <p>Když klepnete na televizi, zobrazí se na obrazovce dotaz s žádostí o povolení. Potvrďte ho svým obvyklým ovladačem. Uděláte to jen jednou.</p>
        </details>
        <details><summary>Samsung</summary>
          <p>Televize se zeptá, zda povolujete připojení Mando TV. Ovladačem vyberte „Povolit“. Pokud jste ho omylem zakázali, otevřete Nastavení > Obecné > Správce externích zařízení > Správce připojení zařízení a změňte to na povoleno.</p>
        </details>
        <details><summary>Roku</summary>
          <p>Roku se na povolení neptá. Pokud se připojení nezdaří, otevřete v Roku Nastavení > Systém > Rozšířená nastavení systému > Ovládání mobilními aplikacemi a nechte síťový přístup na Výchozí nebo Permissive (u novějšího softwaru Roku nastavte „Ovládání mobilními aplikacemi“ na Povoleno).</p>
        </details>
        <details><summary>Android TV a Google TV</summary>
          <p>Televize zobrazí 6znakový kód. Zadejte ho do Mando TV přesně tak, jak se zobrazil. Funguje to u Sony, Philips, TCL, Hisense, Sharp, Xiaomi, Chromecastu s Google TV a dalších s Android TV.</p>
        </details>
      </div>

      <h2 id="encender">Zapnutí televize z aplikace</h2>
      <p>Mando TV zapíná televizi přes vaši domácí síť. K tomu jsou potřeba dvě věci: alespoň jednou jste se připojili při zapnuté televizi a v televizi je zapnuté zapnutí přes síť. Název nastavení se podle modelu liší; tady jsou ty nejčastější:</p>
      <div class="preguntas">
        <details><summary>LG</summary>
          <p>Najděte „Zapnout televizi pomocí mobilního zařízení“ (nebo „Zapnout přes Wi-Fi“) v Nastavení > Obecné > Zařízení > Externí zařízení (u starších modelů Připojení > Správa mobilního připojení) a zapněte ho.</p>
        </details>
        <details><summary>Samsung</summary>
          <p>Zapněte „Zapnout pomocí mobilního zařízení“ v Nastavení > Obecné > Síť > Expertní nastavení.</p>
        </details>
        <details><summary>Roku</summary>
          <p>U televizorů Roku TV zapněte „Rychlé spuštění TV“ v Nastavení > Systém > Napájení. Přehrávače Roku zapojené do televize se tímto způsobem zapnout nedají.</p>
        </details>
        <details><summary>Android TV a Google TV</summary>
          <p>Záleží na výrobci. V nastavení sítě nebo napájení hledejte „Wake on LAN“, „Zapnutí přes síť“, „Pohotovostní režim sítě“ nebo „Remote start“. Některé modely tuto možnost nemají.</p>
        </details>
      </div>

      <h2 id="falla">Když něco nefunguje</h2>
      <div class="preguntas">
        <details><summary>Připojení se přerušuje nebo televize nereaguje</summary>
          <ol>
            <li>Na obrazovce ovladače klepněte na Připojit znovu.</li>
            <li>Pokud to nepomůže, zavřete Mando TV a otevřete aplikaci znovu.</li>
            <li>Pokud televize dostala jinou adresu IP, odeberte ji ze seznamu a přidejte znovu.</li>
          </ol>
        </details>
        <details><summary>Jak nám poslat zprávu o chybě</summary>
          <ol>
            <li>V Mando TV klepněte na tlačítko Přizpůsobit (posuvníky nahoře).</li>
            <li>Klepněte na Kopírovat testovací zprávu.</li>
            <li>Vložte ji do e-mailu na hola@mandotv.app spolu se značkou a modelem televize.</li>
          </ol>
          <p>Zpráva neobsahuje hesla, kódy ani nic, co píšete.</p>
        </details>
        <details><summary>Koupil(a) jsem Pro a nezobrazuje se</summary>
          <p>V části Přizpůsobit klepněte na Obnovit nákup, se stejným účtem obchodu, ze kterého jste nakupovali. Pokud se stále nezobrazí, napište nám.</p>
        </details>
      </div>

      <h2 id="guias">Návody krok za krokem</h2>
      <p><a href="@@R_guias@@">Zobrazit všechny návody</a></p>
      <ul>
@@GUIAS@@
      </ul>

      <h2 id="contacto">Máte další otázky?</h2>
      <p>Napište nám na <a href="mailto:hola@mandotv.app?subject=Pomoc%20s%20Mando%20TV">hola@mandotv.app</a>. Uveďte značku a model televize a v kterém kroku jste uvízli. Pište nám ve svém jazyce. Odpovídáme španělsky nebo anglicky a na přání i ve vašem jazyce s pomocí překladače.</p>
'''

PRIVACIDAD = dict(
  titulo='Zásady ochrany osobních údajů | Mando TV',
  desc='Mando TV neshromažďuje osobní údaje: žádné účty, žádné reklamy, žádné sledovače. Aplikace komunikuje jen s vaší televizí uvnitř vaší sítě Wi-Fi.',
  h1='Ochrana soukromí',
  intro='Stručně: Mando TV vaše údaje neshromažďuje. Neexistují žádné účty, žádné reklamy, žádné sledovače ani vlastní servery, které by ukládaly, co děláte.',
)
PRIVACIDAD_HTML = '''      <p class="fecha">Platné od 14. listopadu 2026. Naposledy aktualizováno 26. listopadu 2026.</p>

      <h2>Kdo jsme</h2>
      <p>Mando TV je aplikace, kterou ovládáte televizi z telefonu nebo počítače. Tyto zásady popisují, jaké informace aplikace používá a co s nimi dělá. S dotazy nám napište na <a href="mailto:hola@mandotv.app">hola@mandotv.app</a>.</p>

      <h2>Jaké údaje shromažďujeme</h2>
      <p>Aplikace: žádné. Aplikace nám ani třetím stranám neposílá informace o vás ani o tom, jak ji používáte. Nepoužívá žádné analytické, reklamní ani sledovací nástroje.</p>
      <p>Tento web: návštěvy měříme dvěma způsoby, které jsou vysvětleny v části <a href="#cookies">Soubory cookie na tomto webu</a>.</p>

      <h2>Co aplikace ukládá ve vašem zařízení</h2>
      <p>Aby fungovala, aplikace ukládá následující údaje pouze ve vašem telefonu nebo počítači:</p>
      <ul>
        <li>Televize, které jste přidali: název, značku, adresu IP ve vaší síti a hardwarovou adresu sítě (MAC), která se používá k zapnutí.</li>
        <li>Klíče připojení, které každá televize předá, když potvrdíte povolení. Ukládají se šifrovaně v zabezpečeném úložišti systému (Klíčenka na iPhonu a Macu, Keystore v Androidu, chráněné úložiště ve Windows).</li>
        <li>Vaše nastavení: světlý nebo tmavý motiv, barvu pozadí, vibrace a typ ovladače.</li>
        <li>Pokud používáte funkce Pro: oblíbené aplikace, rutiny a poslední hledání v YouTube (v aplikaci je můžete smazat).</li>
      </ul>
      <p>Když aplikaci smažete, smaže se s ní všechno výše uvedené.</p>

      <h2>S kým aplikace komunikuje</h2>
      <p>S vašimi televizemi, uvnitř vaší domácí sítě Wi-Fi. Aby je našla, prohledává aplikace vaši místní síť; proto na iPhonu žádá o oprávnění „Místní síť“. Text, který zadáváte na klávesnici aplikace, jde přímo do televize a neukládá se.</p>
      <p>Aplikace navíc při otevření stáhne z tohoto webu malý veřejný soubor (mandotv.app/app/config.json), aby zjistila, zda existuje nová verze, kterou byste si měli nainstalovat, a které funkce patří do Mando TV Pro. Je to stažení, jako když otevřete stránku: aplikace neodesílá vaše údaje, vaše televize ani to, co děláte. Uvádí jen verzi aplikace a systém (například Android), aby vám mohla zobrazit správné upozornění. Pokud nemáte internet, aplikace pracuje dál s posledním staženým souborem; pokud uplyne více než 30 dní, aniž by se ho podařilo stáhnout, požádá vás, abyste se krátce připojili k internetu.</p>

      <p>Pokud do televize odesíláte fotografie nebo videa (funkce Pro), televize stahuje jen soubory, které vyberete, přímo z vašeho telefonu nebo počítače přes domácí Wi-Fi. Neprocházejí internetem ani námi, aplikace nevidí vaše ostatní fotografie a sdílení skončí, jakmile tuto obrazovku zavřete.</p>
      <h2>Mikrofon a hlas</h2>
      <p>Na iPhonu, Macu a v Androidu hlasové vyhledávání používá mikrofon jen po dobu, kdy držíte tlačítko pro mluvení. To, co řeknete, převádí na text rozpoznávání řeči vašeho systému: společnost Apple na iPhonu a Macu a společnost Google v Androidu, vždy podle jejich vlastních zásad ochrany soukromí. Ve Windows se řeč rozpoznává přímo ve vašem počítači a zařízení neopouští; jen u velmi starých procesorů aplikace používá hlasový vstup Windows od společnosti Microsoft, podle jejích zásad ochrany soukromí. Ve Windows se mikrofon zapne, když otevřete hlasový panel, a vypne se, když ho zavřete, nebo po 30 sekundách nepoužívání; dokud nemluvíte, nic se nenahrává ani neukládá. Mando TV zvuk nenahrává ani neukládá a výsledný text jde přímo do vaší televize, stejně jako to, co píšete na klávesnici.</p>

      <h2>Domácnost: zařízení z Apple Home a Google Home</h2>
      <p>Když otevřete oddíl Domácnost (ve zkušebním provozu), aplikace požádá o povolení zobrazit zařízení, která už máte v aplikaci Domácnost od Applu (HomeKit) nebo v Google Home. S tímto povolením čte jejich název, místnost a stav (zapnuto nebo vypnuto, jas, teplota nebo v jaké fázi programu je spotřebič), aby je zobrazila a odeslala jim to, na co klepnete. Všechno probíhá mezi vaším telefonem a systémem Applu nebo Googlu: Mando TV tento seznam neukládá, neposílá ho nám ani třetím stranám a nepoužívá ho k reklamě ani k analýzám. V Androidu funguje Google Home s vaším vlastním účtem Google, podle zásad ochrany soukromí Googlu. Povolení můžete kdykoli odebrat: na iPhonu v Nastavení &gt; Soukromí a zabezpečení &gt; HomeKit, v Androidu v nastavení svého účtu Google.</p>
      <p>Když klepnete na „Jak vám Domácnost fungovala?“, otevře se vaše e-mailová aplikace se zprávou pro hola@mandotv.app, která obsahuje technické shrnutí: verzi aplikace, systém a kolik zařízení každého druhu se zobrazilo a zda reagují. Názvy zařízení, místností ani vaší domácnosti v něm nejsou a zpráva se odešle, jen když ji sami odešlete.</p>

      <h2>Testovací zpráva</h2>
      <p>Aplikace má tlačítko „Kopírovat testovací zprávu“, které nám pomáhá opravovat chyby. Zpráva zůstává jen v paměti aplikace, dokud je otevřená, a nikdy se neodesílá sama: rozhodujete vy, zda ji zkopírujete a sdílíte. Neobsahuje klíče připojení, párovací kódy ani nic, co zadáváte; jen kroky, které aplikace provedla, jako je hledání, připojování a chyby.</p>

      <h2 id="cookies">Soubory cookie na tomto webu</h2>
      <p>Týká se to jen webu mandotv.app, ne aplikace.</p>
      <h3>Vždy bez souborů cookie</h3>
      <p>Návštěvy počítáme anonymně pomocí Cloudflare Web Analytics: kolik lidí web navštíví, jaké stránky čtou a z jaké země. Nepoužívá soubory cookie, vaši adresu IP nepoužívá k identifikaci a nesleduje, co děláte na jiných webech.</p>
      <h3>Se soubory cookie, jen pokud souhlasíte</h3>
      <p>Pokud v upozornění na soubory cookie klepnete na „Přijmout“, zapneme Google Analytics (od společnosti Google LLC), abychom lépe porozuměli tomu, jak se web používá: zobrazení stránek, dobu návštěvy, typ zařízení, přibližné město a odkud přicházíte. K tomu ve vašem prohlížeči ukládá soubory cookie _ga a _ga_* až na 2 roky. Google může tyto údaje zpracovávat na serverech mimo Chile. Reklamní funkce a Google Signals jsme vypnuli a tyto údaje nepoužíváme k zobrazování reklam.</p>
      <p>Pokud klepnete na „Odmítnout“ nebo nevyberete nic, Google Analytics se nenačte a neuloží se žádný soubor cookie. Své rozhodnutí můžete kdykoli změnit tlačítkem „Cookies“ na konci každé stránky; pokud souhlas odvoláte, tyto soubory cookie smažeme.</p>
      <p>Vaše volba se uloží ve vašem prohlížeči (místní úložiště, nikomu se neodesílá), abychom se vás znovu neptali.</p>

      <h2>Nákupy</h2>
      <p>Když si koupíte Mando TV Pro, platbu zpracovává obchod s aplikacemi (App Store, Google Play nebo Microsoft Store). Údaje o vaší kartě nepřijímáme ani neukládáme. Obchod aplikaci jen potvrdí, že nákup existuje.</p>

      <h2>E-maily, které nám posíláte</h2>
      <p>Když nám napíšete na <a href="mailto:hola@mandotv.app">hola@mandotv.app</a>, použijeme vaši e-mailovou adresu a to, co nám sdělíte, jen k tomu, abychom vám odpověděli. Nesdílíme je a nepoužíváme je k reklamě. Můžete kdykoli požádat o smazání svých zpráv.</p>

      <h2>Děti</h2>
      <p>Aplikace neshromažďuje údaje o nikom, ani o dětech.</p>

      <h2>Změny těchto zásad</h2>
      <p>Pokud se jednoho dne změní to, co aplikace dělá s vašimi údaji, aktualizujeme tuto stránku a datum nahoře dříve, než změna do aplikace dorazí.</p>
'''


# >>> guías traídas del inglés (ensamblar.py)
# Adaptadas con Ollama (qwen3.6:35b) desde las guías inglesas y auditadas por Opus el 22-nov. Rutas en idiomas_sitio.py.
GUIAS += [
  dict(clave='no-sub', corto='Ovládací aplikace bez předplatného', fecha='2026-11-23',
    titulo='Ovládací aplikace k televizi bez předplatného a reklam',
    desc='Máte dost ovládacích aplikací s reklamami nebo týdenním předplatným? Mando TV je zdarma a bez reklam, Pro je volitelný jednorázový nákup. Upřímné srovnání.',
    h1='Ovládací aplikace bez předplatného a bez reklam',
    intro='Mnoho univerzálních ovladačů zobrazuje reklamy nebo před použitím vyžaduje týdenní předplatné. Mando TV jde jinou cestou: ovladač je zdarma, bez reklam a bez účtu. Volitelné Pro koupíte jen jednou. Tady je srovnání, včetně toho, co aplikace neumí.',
    pasos=[
      'Před instalací otevřete stránku aplikace v obchodě a zkontrolujte nákupy v aplikaci. Týdenní nebo měsíční ceny napovídají předplatné.',
      'Na Google Play zkontrolujte, zda stránka uvádí „Obsahuje reklamy“, a přečtěte si nejnovější recenze s nízkým počtem hvězdiček: často se v nich objevují nečekané placené zdi.',
      'Ujistěte se, že aplikace umí ovládat vaši televizi přes Wi-Fi. Mando TV funguje se Samsungem (od roku 2016), LG webOS, Roku, Google TV, Android TV a Fire TV.',
      'Nainstalujte Mando TV, připojte telefon ke stejné síti Wi-Fi jako televizi a v seznamu klepněte na svou televizi.',
      'Potvrďte dotaz v televizi nebo zadejte zobrazený kód. Tlačítka, hlasitost, programy a klávesnice jsou zdarma.',
    ],
    tabla=dict(titulo='Mando TV ve srovnání s mnoha ovládacími aplikacemi',
      cabeza=['', 'Mando TV', 'Mnoho aplikací s reklamami nebo předplatným'],
      filas=[
        ['Základní ovladač', 'Zdarma', 'Často zdarma s reklamami nebo skrytý za zkušební dobou'],
        ['Reklamy', 'Žádné', 'Časté'],
        ['Předplatné', 'Žádné. Pro je volitelný jednorázový nákup', 'Týdenní nebo měsíční plány jsou běžné'],
        ['Účet', 'Není potřeba', 'Různé'],
        ['Chytré televize přes Wi-Fi', 'Samsung (od 2016), LG webOS, Roku, Google TV, Android TV, Fire TV, Apple TV (beta)', 'Podle aplikace'],
        ['Infračervený signál pro starší televize', 'Zdarma na telefonech s Androidem s infračerveným vysílačem (novinka)', 'Některé aplikace, jen u telefonů s infračerveným vysílačem'],
        ['Bluetooth', 'Beta od Androidu 9, zdarma', 'Podle aplikace'],
        ['Fotografie a videa v televizi', 'Pro, přes Wi-Fi (bez zrcadlení)', 'Podle aplikace'],
        ['Telefony a počítače', 'iPhone, iPad, Mac a Windows, k tomu Android v předběžném přístupu', 'Různé'],
        ['Zrcadlení obrazovky', 'Zdarma na iPhonu, iPadu a ve Windows s vestavěnou funkcí každého systému. Ve Windows může Pro navíc zrcadlit obrazovku počítače na televize LG, Samsung, Hisense a Android TV (beta)', 'Některé aplikace ho nabízejí'],
      ],
      nota='Mando TV nesrovnáváme s žádnou konkrétní aplikací. Aktuální ceny najdete na stránce dané aplikace v obchodě.'),
    extra=[
      ('Co Mando TV nedělá', 'Na iPhonu a iPadu vás nasměruje na Zrcadlení obrazovky v Ovládacím centru, funkci samotného iPhonu, která funguje s televizemi s AirPlay. Ve Windows otevře Vysílat (Windows + K) a Mando TV Pro dokáže odesílat obrazovku počítače přes vaši Wi-Fi na televize LG, Samsung, Hisense a Android TV (beta, s několikavteřinovým zpožděním a bez zvuku). S Mando TV Pro dokáže také odesílat fotografie a videa do televize přes Wi-Fi. Ovládá chytré televize přes domácí Wi-Fi. Televize bez chytrých funkcí lze ovládat z telefonu s Androidem s infračerveným vysílačem pomocí infračerveného signálu. Od Androidu 9 se telefon může k Google TV, Android TV a Fire TV připojit také přes Bluetooth jako klávesnice a ovladač, zcela bez Wi-Fi. Tato možnost je v betě a zdarma.'),
      ('Jak Mando TV vydělává', 'Ne reklamami a ne vašimi údaji: aplikace žádné neshromažďuje. Mando TV se financuje z Pro, volitelného jednorázového nákupu za doplňky. Základní ovladač je zdarma.'),
      ('Na zařízeních, která už máte', 'iPhone, iPad a Mac z App Store, počítače s Windows z Microsoft Store a Android prostřednictvím bezplatného předběžného přístupu na Google Play. Viz [Ovládací aplikace pro iPhone](@iphone) a [Ovládací aplikace pro Windows](@windows).'),
      ('Ochrana soukromí', 'V aplikaci není žádný účet ani sledování. Komunikace s televizí probíhá jen v místní síti, údaje o připojení zůstávají šifrované ve vašem zařízení. Podrobnosti jsou v [Zásadách ochrany osobních údajů](@privacidad).'),
    ],
    marca=None,
    faq=[
      ('Existuje ovládací aplikace bez předplatného?', 'Ano. Mando TV nemá předplatné vůbec: ovladač je zdarma a bez reklam, Pro je volitelný jednorázový nákup.'),
      ('Je Mando TV opravdu zdarma?', 'Ano. Šipky, OK, Zpět, Domů, hlasitost, kanály, číslice, klávesnice a zapnutí či vypnutí jsou zdarma, bez reklam a bez časového omezení.'),
      ('Funguje to bez Wi-Fi?', 'Většinou ne. Mando TV ovládá chytré televize přes domácí Wi-Fi. Výjimky: infračervený signál na telefonech s Androidem s infračerveným vysílačem, který funguje i s televizemi bez chytrých funkcí nebo bez připojení k Wi-Fi, a Bluetooth, v betě od Androidu 9, pro Google TV, Android TV a Fire TV.'),
    ]),
  dict(clave='roku-app-alt', corto='Alternativa k aplikaci Roku', fecha='2026-11-23',
    titulo='Alternativa k aplikaci Roku: jednoduchý ovladač Roku',
    desc='Alternativa k aplikaci Roku jako ovladač: Mando TV ovládá Roku TV a přehrávače přes Wi-Fi, bez účtu a reklam, a také Samsung, LG a Google TV.',
    h1='Alternativa k aplikaci Roku: jedna pro všechny televize',
    intro='Oficiální aplikace Roku toho umí hodně: Channel Store, vysílání obsahu, soukromý poslech a dálkový ovladač. Pokud hledáte jen rychlý ovladač nebo máte doma také televizi Samsung, LG nebo Google TV, je Mando TV jednoduchou alternativou, která ovládá Roku přes vaši Wi-Fi bez účtu.',
    pasos=[
      'Připojte telefon a Roku ke stejné síti Wi-Fi.',
      'Stáhněte si Mando TV a otevřete ho. Vaše Roku TV nebo přehrávač Roku se objeví v seznamu. Klepněte na něj. Roku se na kód neptá.',
      'Používejte šipky, OK, Zpět, Domů, hlasitost a klávesnici. Hledané výrazy v kanálech Roku pište na klávesnici telefonu.',
      'Pokud tlačítka nic nedělají, otevřete v Roku Nastavení > Systém > Rozšířená nastavení systému > Ovládání mobilními aplikacemi a nastavte síťový přístup na Výchozí nebo Permissive (u novějšího softwaru Roku nastavte Ovládání mobilními aplikacemi na Povoleno).',
      'Volitelně: v televizi Roku TV zapněte „Rychlé spuštění TV“ v Nastavení > Systém > Napájení, aby ji Mando TV mohlo zapnout.',
    ],
    extra=[
      ('Kde se Mando TV hodí víc', 'Jedna aplikace pro více televizí: Roku, Samsung, LG a Google TV nebo Android TV. Bez účtu, bez reklam. Funguje i na počítači s Windows, což se hodí u stolu. Šipky a hlasitost reagují rychle a na klávesnici snadno napíšete hledané výrazy.'),
      ('Kde je oficiální aplikace Roku lepší', 'Ponechte si aplikaci Roku pro to, co nabízí nad rámec ovladače, například procházení a přidávání kanálů z Roku Channel Store, vlastní vysílání obsahu a soukromý poslech (zvuk do sluchátek v telefonu). Používejte obě, pokud chcete. Mohou běžet na stejném telefonu.'),
      ('Televizory Roku TV a přehrávače Roku', 'Fungují obojí. Patří sem modely Roku TV od TCL, Hisense, Philips a dalších, stejně jako Roku Express, Streaming Stick a Ultra. Podrobnosti najdete na [stránce ovládací aplikace pro Roku](@roku).'),
      ('Když aplikace Roku přestane fungovat', 'Pokud tlačítka přestanou reagovat, Roku většinou blokuje ovládání aplikacemi. Návod [Aplikace Roku nefunguje](@roku-403) ukazuje nastavení, které problém vyřeší.'),
      ('Zdarma a Pro', 'Šipky, OK, Zpět, Domů, hlasitost, kanály, číselná tlačítka, klávesnice, otevírání aplikací, přepínání vstupů a zapnutí či vypnutí jsou zdarma, bez reklam a bez předplatného. Touchpad, hlasové příkazy, oblíbené aplikace, rutiny a časovač vypnutí jsou součástí Mando TV Pro, jednorázového nákupu bez předplatného.'),
    ],
    marca='roku',
    faq=[
      ('Potřebuji k používání Mando TV účet Roku?', 'Ne. Mando TV komunikuje s Roku přes vaši domácí síť a účet nevyžaduje.'),
      ('Nahradí Mando TV mobilní aplikaci Roku úplně?', 'Jako ovladač ano. Pro Channel Store, vysílání obsahu a soukromý poslech si ponechte oficiální aplikaci Roku.'),
      ('Funguje to s mým Roku Express nebo Streaming Stick?', 'Ano. Všechny přehrávače Roku a televizory Roku TV se ovládají stejným způsobem.'),
    ]),
  dict(clave='lg-thinq', corto='Alternativa k aplikaci LG ThinQ', fecha='2026-11-23',
    titulo='Alternativa k aplikaci LG ThinQ: ovladač LG bez účtu',
    desc='Hledáte alternativu k aplikaci LG ThinQ jen jako ovladač? Mando TV ovládá televizory LG s webOS přes Wi-Fi, bez účtu LG a bez reklam.',
    h1='Alternativa k aplikaci LG ThinQ pro vaši televizi LG',
    intro='LG ThinQ je oficiální aplikace LG určená pro celou chytrou domácnost: domácí spotřebiče, televizi a další. Pokud chcete jen jednoduchý ovladač k televizi LG, Mando TV to zvládne přes vaši domácí Wi-Fi, aniž byste museli zakládat účet LG, a bez reklam.',
    pasos=[
      'Připojte telefon nebo počítač (iPhone, Android nebo Windows) a televizi LG ke stejné síti Wi-Fi.',
      'Stáhněte si Mando TV a otevřete ho. Vaše televize LG se v seznamu objeví sama. Klepněte na ni.',
      'V televizi se zobrazí dotaz. Jednou ho potvrďte ovladačem televize, joystickem pod obrazovkou nebo ovladačem Magic Remote.',
      'Tlačítka, hlasitost a klávesnice fungují hned. Nepotřebujete účet LG ani televizi nemusíte registrovat.',
      'Volitelně: v nastavení televize zapněte „Zapnout televizi pomocí mobilního zařízení“, abyste televizi mohli zapnout i z telefonu.',
    ],
    extra=[
      ('Mando TV, nebo LG ThinQ: co na co', 'ThinQ použijte, když chcete spravovat domácí spotřebiče LG, jako je pračka, lednice nebo klimatizace, nebo potřebujete funkce účtu LG. Mando TV použijte, když chcete rychlý a jednoduchý ovladač k televizi, který ve stejné aplikaci funguje i pro Samsung, Roku a Google TV. Mnoho lidí si ponechá obě: ThinQ pro spotřebiče, Mando TV pro televizi.'),
      ('Co Mando TV umí na televizi LG', 'Funguje s chytrými televizemi LG s webOS, tedy s většinou modelů od roku 2014, včetně LED, NanoCell, QNED a OLED. Nabízí šipky, OK, Zpět, Domů, hlasitost, programy, ztlumení, ovládání přehrávání a klávesnici pro psaní ve vyhledávání televize a ve většině aplikací. Seznam aplikací a seznam vstupů jsou také zdarma. S Pro získáte navíc ukazatel jako u Magic Remote.'),
      ('Co Mando TV nedělá', 'Neovládá domácí spotřebiče LG, nepoužívá váš účet LG a nenahrazuje služby účtu LG v televizi. Je to ovladač, ne centrála chytré domácnosti.'),
      ('Ochrana soukromí a reklamy', 'Mando TV nemá reklamy ani účet. Komunikuje s televizí jen uvnitř vaší domácí sítě a klíč připojení ukládá šifrovaně ve vašem zařízení. Všechny funkce najdete na stránce [Ovládací aplikace pro LG](@lg).'),
      ('Zdarma a Pro', 'Šipky, OK, Zpět, Domů, hlasitost, programy, číselná tlačítka, klávesnice, otevírání aplikací, přepínání vstupů a zapnutí či vypnutí jsou zdarma, bez reklam a bez předplatného. Touchpad, hlasové příkazy, oblíbené aplikace, rutiny a časovač vypnutí jsou součástí Mando TV Pro, jednorázového nákupu bez předplatného.'),
    ],
    marca='lg',
    faq=[
      ('Mohu televizi LG ovládat bez aplikace LG ThinQ?', 'Ano. Mando TV se připojuje přímo přes vaši Wi-Fi k televizím LG s webOS. Jednou potvrdíte dotaz v televizi a hotovo, bez účtu LG.'),
      ('Funguje Mando TV s ukazatelem ovladače LG Magic Remote?', 'Mando TV Pro má ukazatel, který posouváte prstem po displeji telefonu, podobně jako Magic Remote posouvá šipku.'),
      ('Patří Mando TV společnosti LG?', 'Ne. Mando TV je nezávislá aplikace a nemá žádnou souvislost s LG. LG a ThinQ patří jejich vlastníkům a uvádíme je jen kvůli popisu kompatibility.'),
    ]),
  dict(clave='smartthings', corto='Alternativa k SmartThings', fecha='2026-11-23',
    titulo='SmartThings nefunguje? Jednoduchá alternativa pro Samsung',
    desc='SmartThings je pomalé nebo chybuje? Mando TV ovládá televize Samsung s Tizen přímo přes Wi-Fi. Bez účtu Samsung, bez reklam. Krok za krokem.',
    h1='Alternativa k SmartThings pro televize Samsung',
    intro='SmartThings je aplikace Samsung pro celou chytrou domácnost a její ovladač funguje přes váš účet Samsung. Pokud přestal fungovat nebo hledáte rychlé řešení, Mando TV ovládá televize Samsung s Tizen, rok výroby 2016 a novější, přímo přes vaši Wi-Fi bez účtu.',
    pasos=[
      'Připojte telefon a televizi Samsung ke stejné síti Wi-Fi.',
      'Stáhněte si Mando TV a otevřete aplikaci. Vaše televize Samsung se v seznamu objeví sama. Klepněte na ni.',
      'Televize se zeptá, zda chcete připojení povolit. Ovladačem nebo tlačítkem na televizi vyberte „Povolit“ (jen poprvé).',
      'Hned používejte šipky, OK, Zpět, Domů, hlasitost, programy a klávesnici.',
      'Volitelně: zapněte „Zapnout pomocí mobilního zařízení“ v Nastavení > Obecné > Síť > Expertní nastavení, aby mohlo Mando TV televizi také zapnout.',
    ],
    extra=[
      ('Proč ovladač v telefonu přestane fungovat', 'Příčiny bývají jednoduché: telefon a televize jsou v různých sítích Wi-Fi, je zapnutá VPN nebo je televize v hlubokém pohotovostním režimu. U SmartThings může problémy dělat i účet Samsung, například pokud jste byli odhlášeni. Mando TV komunikuje přímo s televizí v domácí síti, žádný účet k přihlášení neexistuje. Další tipy najdete v návodu [Telefon nenajde televizi](@not-found).'),
      ('Mando TV, nebo SmartThings: co na co', 'SmartThings si ponechte, pokud ho používáte pro spotřebiče Samsung, světla nebo jiná zařízení chytré domácnosti či pro funkce účtu Samsung. Mando TV použijte, když chcete jen rychlý ovladač k televizi nebo máte doma také zařízení LG, Roku, Google TV či Fire TV: jedna aplikace ovládá všechna. Obě aplikace mohou být nainstalované na stejném telefonu.'),
      ('Když jste povolení omylem zakázali', 'V televizi otevřete Nastavení > Obecné > Správce externích zařízení > Správce připojení zařízení a nastavte Mando TV na povoleno.'),
      ('Nemáte ovladač?', 'Dotaz můžete potvrdit tlačítkem na samotné televizi. Návod [Samsung televize bez původního ovladače](@samsung-lost) vám ukáže, jak na to.'),
      ('Zdarma a Pro', 'Ovladač si můžete zdarma stáhnout a používat, bez reklam a bez předplatného. Mando TV Pro je volitelný jednorázový nákup za doplňky.'),
    ],
    marca='samsung',
    faq=[
      ('Mohu televizi Samsung ovládat bez SmartThings?', 'Ano. Mando TV se připojuje přímo přes vaši Wi-Fi k televizím Samsung s Tizen. Připojení jednou povolíte v televizi, bez účtu Samsung.'),
      ('Ovládá Mando TV i spotřebiče Samsung?', 'Ne. Je to jen ovladač k televizi. Pro spotřebiče a další zařízení chytré domácnosti si ponechte SmartThings.'),
      ('Patří Mando TV společnosti Samsung?', 'Ne. Mando TV je nezávislá aplikace a nemá žádnou souvislost se Samsungem. Samsung a SmartThings patří jejich vlastníkům a uvádíme je jen kvůli popisu kompatibility.'),
    ]),
]
GUIAS += [
  dict(clave='googletv-alt', corto='Alternativa k ovladači Google TV', fecha='2026-11-23',
    titulo='Ovladač Google TV nefunguje? Alternativa',
    desc='Ovladač Google TV v telefonu nenajde televizi? Mando TV ovládá Google TV a Android TV přes Wi-Fi, bez účtu Google a bez reklam.',
    h1='Alternativa k ovladači Google TV v telefonu',
    intro='Ovladač v telefonu pro Google TV a Android TV je součástí samotné aplikace Googlu a je svázaný s vaším účtem Google. Pokud televizi nenajde, nedostanete se dál. Mando TV je samostatná ovládací aplikace, která se páruje 6znakovým kódem z obrazovky a funguje bez účtu Google, na iPhonu, telefonu s Androidem i počítači s Windows.',
    pasos=[
      'Zapněte televizi a připojte telefon ke stejné síti Wi-Fi.',
      'Stáhněte si Mando TV a otevřete aplikaci. V seznamu klepněte na svou televizi s Google TV nebo Android TV.',
      'Televize zobrazí 6znakový kód. Zadejte ho do Mando TV a klepněte na Spárovat.',
      'Používejte šipky, OK, Zpět, Domů, hlasitost a klávesnici. Nikam se nemusíte přihlašovat.',
      'Volitelně: v nastavení televize hledejte Wake on LAN nebo „Zapnutí přes síť“, aby aplikace mohla televizi také zapnout.',
    ],
    extra=[
      ('Proč ovladač v telefonu televizi už nenajde', 'Většinou je to kvůli síti: telefon a televize jsou v různých sítích Wi-Fi, je zapnutá VPN nebo síť pro hosty zařízení odděluje. Vyřešte to jako první, protože to ovlivňuje všechny ovládací aplikace. Více v návodu [Telefon nenajde televizi](@not-found).'),
      ('S jakými televizemi to funguje', 'Televize s Google TV a Android TV od Sony, TCL, Hisense, Philips, Sharp, Xiaomi, Toshiba a dalších, dále Chromecast s Google TV, Google TV Streamer a Nvidia Shield. Všechny se párují stejně, jednou kódem z obrazovky.'),
      ('Kde je aplikace Googlu lepší', 'Aplikace Googlu vám pomáhá také hledat obsah ke sledování a pamatuje si váš seznam sledovaných. Ponechte si ji pro tento účel. Mando TV je jen ovladač a navíc ze stejné aplikace ovládá Samsung, LG, Roku a zařízení Fire TV, a to i z počítače s Windows.'),
      ('Když chybí stará ovládací aplikace Android TV', 'Google přesunul ovladač v telefonu ze staré aplikace Android TV Remote Control do aplikace Google TV. Pokud hledáte samostatný ovladač, je Mando TV jednou z možností.'),
      ('Zdarma a Pro', 'Ovladač si můžete zdarma stáhnout a používat, bez reklam a bez předplatného. Mando TV Pro je volitelný jednorázový nákup za doplňky.'),
    ],
    marca='android',
    faq=[
      ('Potřebuji k používání Mando TV s Google TV účet Google?', 'Ne. K párování stačí kód na televizi.'),
      ('Funguje to s Chromecastem s Google TV?', 'Ano. Párování probíhá stejně, pomocí 6znakového kódu na obrazovce.'),
      ('Mohu to používat z iPhonu?', 'Ano. Mando TV je dostupné v App Store pro iPhone a iPad, v Microsoft Store pro Windows a v bezplatném předběžném přístupu na Google Play pro Android.'),
    ]),
  dict(clave='windows', corto='Ovladač pro počítač s Windows', fecha='2026-11-23',
    titulo='Ovládací aplikace pro Windows: televize z počítače',
    desc='Ovládejte Samsung, LG, Roku, Google TV nebo Fire TV z počítače s Windows pomocí Mando TV: klávesové zkratky, mini ovladač a Wi-Fi. V Microsoft Store.',
    h1='Ovládací aplikace pro počítač s Windows',
    intro='Mando TV má aplikaci pro Windows, která z vašeho počítače nebo notebooku přes domácí síť udělá dálkový ovladač k televizi. Pište do televize na skutečné klávesnici, nechte při práci malé okno ovladače navrchu a ovládejte Samsung, LG, Roku, Google TV nebo Fire TV jedinou aplikací.',
    pasos=[
      'Nainstalujte si Mando TV zdarma z Microsoft Store do počítače s Windows 10 nebo 11.',
      'Ujistěte se, že jsou počítač a televize ve stejné síti, přes Wi-Fi nebo kabelem u stejného routeru.',
      'Otevřete Mando TV. Televize se objeví v seznamu. Klikněte na ni.',
      'Potvrďte dotaz v televizi, pokud se zeptá (LG, Samsung), nebo zadejte zobrazený kód (Google TV, Fire TV).',
      'Klikejte na tlačítka nebo napište hledání na klávesnici. Hotovo.',
    ],
    extra=[
      ('Klávesové zkratky (Pro)', 'S Pro se klávesnice počítače stane ovladačem: šipky k pohybu, Enter pro OK, Backspace nebo Esc pro návrat, plus a minus pro hlasitost, M pro ztlumení a mezerník pro pozastavení.'),
      ('Mini ovladač (Pro)', 'Malé okno ovladače, které zůstává nad všemi ostatními okny. Hlasitost změníte nebo pozastavíte, aniž byste přerušili práci.'),
      ('Psaní do televize z počítače', 'Klávesnice na obrazovce televize je pomalá. V Mando TV píšete na skutečné klávesnici a text se objeví ve vyhledávacím poli televize. Tato část je zdarma.'),
      ('Více podrobností', 'Postup krok za krokem najdete v návodu [Ovládání televize z počítače](@pc). Pro telefon si přečtěte [Telefon jako ovladač přes Wi-Fi](@wifi).'),
      ('Zdarma a Pro', 'Šipky, OK, Zpět, Domů, hlasitost, programy, číselná tlačítka, klávesnice, otevírání aplikací, přepínání vstupů a zapnutí či vypnutí jsou zdarma, bez reklam a bez předplatného. Touchpad, hlasové příkazy, oblíbené aplikace, rutiny a časovač vypnutí jsou součástí Mando TV Pro, jednorázového nákupu bez předplatného. Ve Windows kupujete Pro přes Microsoft Store.'),
      ('Hlasové příkazy z počítače (Pro)', 'S Pro můžete s televizí mluvit přes mikrofon počítače. Řeč se rozpoznává přímo v počítači: nepotřebujete internet a nemusíte nic nastavovat ve Windows. To, co řeknete, počítač nikdy neopustí a neukládá se. Jen u velmi starých procesorů aplikace přechází na hlasový vstup Windows. Pro to musí být v nastavení soukromí zapnuté online rozpoznávání řeči a ve Windows přidán váš jazyk.'),
    ],
    marca=None,
    faq=[
      ('Potřebuje ovládací aplikace pro Windows Bluetooth nebo kabel?', 'Ne. Používá vaši domácí síť. Počítač a televize musí být jen připojené ke stejnému routeru.'),
      ('Jaké televize mohu z Windows ovládat?', 'Televize Samsung s Tizen, LG s webOS, Roku TV a přehrávače, Google TV a Android TV a také Fire TV.'),
      ('Mohu vidět obraz televize na počítači nebo slyšet zvuk z reproduktorů počítače?', 'Ne. Mando TV je jen ovladač. Obraz televize na počítač nezrcadlí ani nestreamuje.'),
      ('Proč mi na počítači s Windows nefunguje hlas?', 'Hlasové ovládání je funkce Pro. Zkontrolujte tedy, zda je Pro aktivní a mikrofon počítače funguje. Na většině počítačů se řeč rozpoznává přímo v počítači, bez internetu. Jen u velmi starých procesorů aplikace používá hlasový vstup Windows: pak zapněte online rozpoznávání řeči v nastavení soukromí Windows a přidejte svůj jazyk v jazykových nastaveních.'),
    ]),
  dict(clave='iphone', corto='Ovládací aplikace pro iPhone', fecha='2026-11-23',
    titulo='Ovládací aplikace pro iPhone: Samsung, LG, Roku, Google TV',
    desc='Použijte iPhone jako dálkový ovladač k Samsungu, LG, Roku, Google TV a Fire TV přes Wi-Fi. Zdarma v App Store, bez účtu a bez reklam.',
    h1='Ovládací aplikace pro iPhone: jedna pro všechny televize',
    intro='Mando TV udělá z vašeho iPhonu nebo iPadu dálkový ovladač k Samsungu, LG, Roku, Google TV nebo Android TV a také Fire TV, přes domácí Wi-Fi. Aplikace je v App Store zdarma, bez účtu a bez reklam. Funguje také na Androidu a ve Windows.',
    pasos=[
      'Stáhněte si Mando TV zdarma z App Store.',
      'Připojte iPhone a televizi ke stejné síti Wi-Fi.',
      'Otevřete Mando TV a klepněte na Povolit, když iOS požádá o přístup k místní síti. Aplikace ho potřebuje k nalezení televize.',
      'V seznamu klepněte na svou televizi. Potvrďte dotaz v televizi, pokud se zeptá (LG a Samsung), nebo zadejte kód, který televize zobrazí (Google TV nebo Fire TV).',
      'Používejte tlačítka, hlasitost a klávesnici. Jste připojeni.',
    ],
    extra=[
      ('Funguje s těmito televizemi', 'LG webOS, Samsung Tizen (rok výroby 2016 a novější), Roku TV a přehrávače Roku, Google TV a Android TV a také Fire TV. Stránky značek jsou [Samsung](@samsung), [LG](@lg), [Roku](@roku) a [Android TV](@android).'),
      ('Proč se ptá na místní síť', 'iPhone blokuje aplikacím přístup k zařízením ve vaší domácí síti, pokud to nepovolíte. Pokud se televize v seznamu neobjeví, otevřete Nastavení > Mando TV a zapněte „Místní síť“. Aplikace komunikuje jen s vaší televizí uvnitř vaší domácí sítě.'),
      ('Proč Mando TV a ne aplikace výrobce', 'Každá značka televize má vlastní aplikaci a chce vlastní nastavení nebo účet. Mando TV je jedna aplikace pro všechny, bez účtu.'),
      ('Zdarma a Pro na iPhonu', 'Šipky, OK, Zpět, Domů, hlasitost, programy, číselná tlačítka, klávesnice, otevírání aplikací, přepínání vstupů a zapnutí či vypnutí jsou zdarma, bez reklam a bez předplatného. Touchpad, hlasové příkazy, oblíbené aplikace, rutiny a časovač vypnutí jsou součástí Mando TV Pro, jednorázového nákupu bez předplatného. Pro si koupíte jednou přímo v aplikaci.'),
    ],
    marca=None,
    faq=[
      ('Je Mando TV na iPhonu zdarma?', 'Stažení je zdarma, bez reklam. Základní ovladač je zdarma, stejně jako otevírání aplikací a přepínání vstupů. Doplňky, jako je touchpad, hlasové příkazy a rutiny, jsou součástí Mando TV Pro, jednorázového nákupu.'),
      ('Funguje to na iPadu?', 'Ano. Stejná aplikace běží na iPhonu i iPadu.'),
      ('Potřebuje ovládací aplikace pro iPhone Bluetooth nebo infračervený vysílač?', 'Na iPhonu ne. iPhony infračervený vysílač nemají, proto tam infračervené ovládání není k dispozici, a možnost Bluetooth existuje jen pro Android 9 nebo novější, ne pro iPhone. Na iPhonu Mando TV ovládá chytré televize i Apple TV (beta) přes domácí Wi-Fi.'),
    ]),
  dict(clave='firetv', corto='Ovladač Fire TV', fecha='2026-11-23',
    titulo='Ovládací aplikace Fire TV pro telefon a počítač',
    desc='Ovladač Fire TV v telefonu: ovládejte Fire TV Stick, Fire TV Cube nebo televizi s Fire TV přes Wi-Fi, se 4místným PIN. Bez aplikace Amazon.',
    h1='Ovladač Fire TV pro telefon nebo počítač',
    intro='Když je ovladač Fire TV pryč nebo v něm došly baterie, Mando TV ovládá Fire TV Stick, Fire TV Cube nebo televizi s integrovaným Fire TV přes Wi-Fi. Párování probíhá 4místným PIN. Fire TV je v Mando TV novinka, proto nejdřív aktualizujte aplikaci.',
    pasos=[
      'Aktualizujte Mando TV na nejnovější verzi z App Store, Microsoft Store nebo Google Play.',
      'Zapněte Fire TV a připojte telefon ke stejné síti Wi-Fi.',
      'Otevřete Mando TV. Vaše Fire TV se objeví v seznamu. Klepněte na něj.',
      'Na obrazovce televize se zobrazí 4místný PIN. Zadejte ho do Mando TV. Uděláte to jen jednou.',
      'Používejte šipky, OK, Zpět, Domů, tlačítka přehrávání a klávesnici pro hledání.',
    ],
    extra=[
      ('Podporovaná zařízení Fire TV', 'Fire TV Stick, Fire TV Stick 4K, Fire TV Cube a televize s integrovaným Fire TV, například televize Amazon Fire TV Edition a některé modely Hisense. Podpora je nová a zatím jsme mohli vyzkoušet jen několik skutečných zařízení. Pokud něco nefunguje podle očekávání, napište nám model přes stránku nápovědy.'),
      ('Zapnutí Fire TV', 'Mando TV Fire TV přes síť nezapíná. Zapněte televizi tlačítkem na přístroji: zapojený Fire TV Stick nebo Cube se většinou probudí díky HDMI-CEC a u televize s integrovaným Fire TV je televize samotná Fire TV. Potom ji ovládáte z telefonu.'),
      ('Když se vaše Fire TV nezobrazí', 'Ujistěte se, že jsou obě zařízení ve stejné Wi-Fi a Fire TV je probuzené. Na iPhonu povolte Mando TV v Nastavení „Místní síť“. Viz [Telefon nenajde televizi](@not-found).'),
      ('Žádný ovladač?', 'Fire TV musí zobrazit PIN na obrazovce, takže televize i Fire TV musí být zapnuté a zobrazovat obraz. Pokud je televize na špatném vstupu, přepněte ji tlačítky na televizi. Viz [Změna vstupu bez ovladače](@hdmi).'),
      ('Zdarma a Pro', 'Šipky, OK, Zpět, Domů, hlasitost, programy, číslice, klávesnice, otevírání aplikací, přepínání vstupů a zapnutí či vypnutí jsou zdarma, bez reklam a bez předplatného. Touchpad, hlasové příkazy, oblíbené aplikace, rutiny a časovač vypnutí jsou součástí Mando TV Pro, jednorázového nákupu bez předplatného.'),
    ],
    marca=None,
    faq=[
      ('Potřebuji aplikaci Amazon Fire TV?', 'Ne. Mando TV se připojuje k Fire TV přes vaši Wi-Fi pomocí PIN. V telefonu nepotřebujete účet Amazon.'),
      ('Funguje to s televizemi s Fire TV i s Fire TV Stick?', 'Ano, přesně pro to bylo vytvořeno. Podpora je nová, udržujte aplikaci aktuální a napište nám o modelech, které nefungují podle očekávání.'),
      ('Proč potřebuji PIN?', 'Fire TV zobrazí 4místný PIN, aby dokázalo, že sedíte před televizí. Nikdo se nemůže spárovat, aniž by viděl obrazovku.'),
    ]),
  dict(clave='firetv-lost', corto='Ztracený ovladač Fire TV', fecha='2026-11-23',
    titulo='Ztracený ovladač Fire TV? Pomůže telefon',
    desc='Ztratili jste ovladač k Fire TV Stick? Ovládejte ho telefonem přes Wi-Fi, spárovaným 4místným PIN. Tipy pro novou Wi-Fi a HDMI-CEC.',
    h1='Ztracený ovladač Fire TV: jak použít telefon',
    intro='Když je ovladač k vašemu Fire TV Stick, Fire TV Cube nebo chytré televizi s Fire TV ztracený nebo nefunguje, převezme ovládání telefon, dokud je Fire TV stále připojené k vaší Wi-Fi. Párování probíhá 4místným PIN na obrazovce, takže starý ovladač k tomu nikdy nepotřebujete.',
    pasos=[
      'Zapněte televizi tlačítkem na přístroji. Zapojený Fire TV Stick nebo Cube se většinou probudí také; při zapnutém HDMI-CEC televize často přepne na jeho vstup automaticky.',
      'Pokud televize zobrazuje jiný vstup, přepněte ji tlačítkem vstupu nebo zdroje na televizi. Viz [Změna vstupu bez ovladače](@hdmi).',
      'Připojte telefon ke stejné síti Wi-Fi jako Fire TV.',
      'Stáhněte si Mando TV a otevřete aplikaci. Vaše Fire TV se objeví v seznamu. Klepněte na něj.',
      'Televize zobrazí 4místný PIN. Zadejte ho do Mando TV. Uděláte to jen jednou.',
      'Používejte šipky, OK, Zpět, Domů, hlasitost, tlačítka přehrávání a klávesnici v telefonu.',
    ],
    extra=[
      ('Nejdřív vyzkoušejte ovladač televize (HDMI-CEC)', 'Mnoho ovladačů televizí umí ovládat Fire TV Stick přes HDMI-CEC. Když je vidět rozhraní Fire TV, stiskněte šipky a OK na ovladači televize. Pokud se nic neděje, zapněte CEC v nastavení televize (Anynet+ u Samsungu, SIMPLINK u LG, BRAVIA Sync u Sony) a ve Fire TV ovládání zařízení HDMI-CEC v nastavení zobrazení („Display & Sounds“).'),
      ('Když jste změnili Wi-Fi', 'Bez ovladače nemůžete ve Fire TV zadat heslo nové Wi-Fi, ale existuje cesta: na druhém telefonu vytvořte hotspot přesně se stejným názvem a heslem jako vaše stará Wi-Fi. Fire TV se k němu připojí automaticky. K tomuto hotspotu připojte telefon s Mando TV, spárujte ho pomocí PIN, potom ve Fire TV otevřete Nastavení > Síť a vyberte novou Wi-Fi. Nakonec připojte k nové Wi-Fi i telefon.'),
      ('Spárování náhradního ovladače', 'Většina nových ovladačů Fire TV se páruje podržením tlačítka Domů asi 10 sekund v blízkosti Fire TV. Pokud to nefunguje, otevřete Nastavení > Ovladače a zařízení Bluetooth > Ovladače Amazon Fire TV > Přidat nový ovladač. K této nabídce se dostanete také z telefonu s Mando TV.'),
      ('Fire TV integrované v televizi', 'U televizí s integrovaným Fire TV, například u mnoha modelů Insignia a Toshiba, platí stejný postup, protože televize je samotná Fire TV.'),
      ('Než začnete', 'Podpora Fire TV je v Mando TV nová. Nejdřív aktualizujte aplikaci. Pokud váš model nereaguje podle očekávání, napište nám přes [stránku nápovědy](@soporte) a uveďte model.'),
      ('Zdarma a Pro', 'Ovladač si můžete zdarma stáhnout a používat, bez reklam a bez předplatného. Mando TV Pro je volitelný jednorázový nákup za doplňky.'),
    ],
    marca=('firetv', 'Ovladač Fire TV'),
    faq=[
      ('Mohu ovládat Fire TV Stick telefonem bez ovladače?', 'Ano, pokud je Fire TV zapnuté a připojené k vaší Wi-Fi. Mando TV se páruje přes 4místný PIN na televizi, takže starý ovladač nepotřebujete.'),
      ('Funguje to, když je Fire TV v nové Wi-Fi?', 'Ne přímo, protože telefon a Fire TV musí být ve stejné síti. Nejdřív Fire TV znovu připojte pomocí triku s hotspotem z této stránky.'),
      ('Potřebuji aplikaci Amazon Fire TV nebo účet Amazon?', 'Ne. Mando TV se připojuje přes vaši domácí síť pomocí PIN a nevyžaduje vlastní účet.'),
    ]),
  dict(clave='turn-on', corto='Zapnutí televize bez ovladače', fecha='2026-11-23',
    titulo='Zapnutí televize bez ovladače (všechny značky)',
    desc='Zapnutí televize bez ovladače: kde je tlačítko u Samsungu, LG, TCL, Hisense a Sony. Plus HDMI-CEC a triky s telefonem.',
    h1='Jak zapnout televizi bez ovladače',
    intro='Téměř každá televize má stále fyzické tlačítko zapnutí a vypnutí. Je jen dobře schované. Tady uvidíte, kde je u jednotlivých značek, plus dva způsoby, jak si příště hledání ušetřit: HDMI-CEC z konzole nebo streamovacího zařízení a zapnutí televize z telefonu přes Wi-Fi.',
    pasos=[
      'Podívejte se pod střed obrazovky, přímo za logo značky. Mnoho televizí tam má malé jediné tlačítko nebo joystick, směřující dolů.',
      'Pokud tam není, ohmatejte zadní stranu televize poblíž dolních rohů, potom levý a pravý okraj.',
      'Stiskněte tlačítko jednou. U mnoha televizí s jediným tlačítkem krátký stisk při zapnuté televizi otevře malou nabídku vstupů a hlasitosti a dlouhý stisk ji vypne.',
      'Pořád nic? Zkontrolujte napájecí kabel na obou koncích a zkuste jinou zásuvku. Pokud nesvítí kontrolka pohotovostního režimu, televize nedostává proud.',
      'Jakmile je televize zapnutá, nastavte ji tak, abyste tlačítko už nepotřebovali: zapněte HDMI-CEC a zapnutí přes síť, obojí je vysvětleno níže.',
    ],
    extra=[
      ('Kde je tlačítko zapnutí podle značky', 'Samsung: ovládací tlačítko nebo joystick pod středem obrazovky nebo vzadu u dolního rohu. LG: joystick pod logem LG u většiny modelů. TCL a Hisense: většinou malé tlačítko pod středem obrazovky nebo vzadu poblíž dolního rohu. Sony: vzadu nebo na boční hraně, dole blízko okraje. Vizio: vzadu, dole vlevo nebo dole vpravo, nebo na boku. Umístění se podle modelu liší. Pokud ho nenajdete, vyhledejte návod k obsluze podle čísla modelu na štítku na zadní straně.'),
      ('Zapnutí televize z konzole nebo streamovacího zařízení (HDMI-CEC)', 'Při zapnutém HDMI-CEC zapnutí PlayStation, Xboxu, přehrávače Roku, Fire TV Stick nebo Chromecastu zapne také televizi a přepne na správný vstup. Každá značka nastavení nazývá jinak: Anynet+ u Samsungu, SIMPLINK u LG, BRAVIA Sync u Sony a CEC u většiny ostatních. Více v návodu [Zapnutí televize a přepnutí na HDMI konzole](@console).'),
      ('Zapnutí televize z telefonu', 'Chytré televize lze přes Wi-Fi probudit, pokud to jednou povolíte, a potom je Mando TV zapne z telefonu. U Samsungu zapněte „Zapnout pomocí mobilního zařízení“ v Nastavení > Obecné > Síť > Expertní nastavení. U LG zapněte „Zapnout televizi pomocí mobilního zařízení“ ([krok za krokem](@lg-on)). U Roku TV zapněte „Rychlé spuštění TV“ v Nastavení > Systém > Napájení. U Google TV a Android TV hledejte Wake on LAN nebo „Zapnutí přes síť“, pokud ho váš model má. Uděláte to jednou, při zapnuté televizi.'),
      ('Když tlačítko nenajdete', 'Některé novější televize schovávají jediné tlačítko tak dobře, že to vypadá, jako by žádné nebylo. Hledejte malé vybouleniny nebo oblast světelného senzoru pod obrazovkou: tlačítko bývá hned vedle. Přes Wi-Fi potřebuje Mando TV, aby byla televize jednou zapnutá a připojená. Výjimkou je infračervený signál: na telefonu s Androidem s infračerveným vysílačem může Mando TV zapnout televizi, která nikdy nebyla nastavena, pokud telefon namíříte na televizi. Infračervený signál je novinka a funguje se značkami v seznamu kódů v aplikaci.'),
      ('Zdarma a Pro', 'Ovladač si můžete zdarma stáhnout a používat, bez reklam a bez předplatného. Mando TV Pro je volitelný jednorázový nákup za doplňky.'),
    ],
    marca=None,
    faq=[
      ('Mohu televizi zapnout telefonem, když jsem ji nikdy nenastavil(a)?', 'Ne přes Wi-Fi. Vypnutá televize se probudí ze sítě, jen pokud bylo zapnutí přes síť dříve povoleno. Poprvé použijte tlačítko na televizi. Výjimkou je telefon s Androidem s infračerveným vysílačem: Mando TV dokáže zapnout televizi bez nastavení infračerveným signálem, pokud je značka v seznamu kódů nebo zvolíte „Jiná značka nebo nevím“.'),
      ('Jak zapnu televizi Samsung bez ovladače?', 'Stiskněte ovládací tlačítko pod středem obrazovky nebo vzadu u dolního rohu. Potom zapněte „Zapnout pomocí mobilního zařízení“, aby ji příště mohl zapnout telefon.'),
      ('Jak zapnu Roku TV bez ovladače?', 'Použijte tlačítko na televizi, většinou pod středem nebo vzadu. Potom zapněte „Rychlé spuštění TV“ v Nastavení > Systém > Napájení, aby ji Mando TV mohlo zapnout z telefonu.'),
      ('Proč se moje televize zapne sama, když zapnu konzoli?', 'To je HDMI-CEC. Je to praktické a v nastavení televize ho můžete vypnout, pokud dáváte přednost.'),
    ]),
]
GUIAS += [
  dict(clave='sony', corto='Ovladač Sony', fecha='2026-11-23',
    titulo='Ovládací aplikace Sony pro telefon a počítač',
    desc='Mando TV ovládá televize Sony Bravia s Google TV nebo Android TV přes Wi-Fi. Podpora v betě pro modely z let 2013 až 2015 bez Androidu.',
    h1='Jak ovládat televizi Sony telefonem',
    intro='Novější chytré televize Sony Bravia používají Google TV, starší modely od roku 2015 Android TV. Mando TV ovládá obojí přes vaši Wi-Fi z iPhonu, telefonu s Androidem nebo počítače s Windows. Aplikace nahradí původní ovladač, když se ztratí nebo v něm dojdou baterie.',
    pasos=[
      'Zkontrolujte, zda vaše televize Sony zobrazuje úvodní obrazovku Google TV nebo Android TV. Týká se to většiny chytrých televizí Sony Bravia od roku výroby 2015.',
      'Připojte telefon a televizi ke stejné síti Wi-Fi.',
      'Otevřete Mando TV a v seznamu klepněte na svou televizi Sony.',
      'Zadejte 6znakový kód, který televize zobrazí na obrazovce (jen poprvé). Ovladač k tomu nepotřebujete.',
      'Používejte šipky, OK, Zpět, Domů, hlasitost a klávesnici.',
    ],
    extra=[
      ('Zapnutí televize Sony z telefonu', 'Modely Sony s Google TV nebo Android TV lze probudit přes síť, pokud je zapnuté „Remote start“. Možnost najdete většinou v Nastavení > Síť a internet > Remote start (cesta se může podle modelu mírně lišit). Potom v Mando TV klepněte na televizi, když je vypnutá, a aplikace ji zapne.'),
      ('Kde je tlačítko zapnutí u Sony', 'U většiny televizí Bravia je vzadu, poblíž dolního levého nebo pravého rohu, nebo na boční hraně. Krátký stisk televizi zapne. Více najdete v návodu [Zapnutí televize bez ovladače](@turn-on).'),
      ('Starší televize Sony', 'Televize Sony Bravia z let 2013 až 2015, které nepoužívají Android, jsou v Mando TV podporovány ve stavu beta. Je to novinka a může mít ještě drobné nedostatky. Televize zobrazí 4místný PIN, který musíte zadat v aplikaci. Další televize Sony bez Google TV nebo Android TV zatím podporovány nejsou.'),
      ('Zdarma a Pro', 'Ovladač si můžete zdarma stáhnout a používat, bez reklam a bez předplatného. Mando TV Pro je volitelný jednorázový nákup za doplňky.'),
    ],
    marca='android',
    faq=[
      ('Funguje Mando TV s televizemi Sony Bravia?', 'Ano, s televizemi Sony, které používají Google TV nebo Android TV. Patří sem většina chytrých televizí Sony od roku výroby 2015.'),
      ('Potřebuji aplikaci Sony nebo účet Google?', 'Ne. Mando TV se páruje kódem na obrazovce televize a účet nevyžaduje.'),
      ('Funguje to se staršími televizemi Sony Bravia bez Androidu?', 'Ano, ve stavu beta, u modelů Bravia z let 2013 až 2015 bez Androidu. Párování probíhá 4místným PIN, který televize zobrazí.'),
      ('Mohu na televizi Sony psát z telefonu?', 'Ano. Klávesnice telefonu je zdarma a píše do vyhledávání televize a do dalších textových polí. Mando TV má také funkci Klávesnice YouTube: napište nebo řekněte, co chcete sledovat, a YouTube se na televizi otevře s výsledky. Netflix přijímá jen vlastní klávesnici na obrazovce, proto tam použijte šipky a OK.'),
    ]),
  dict(clave='tcl', corto='Ovladač TCL', fecha='2026-11-23',
    titulo='Ovládací aplikace TCL pro telefon a počítač',
    desc='Ztracený ovladač TCL? Většina televizí TCL používá Roku TV nebo Google TV. Mando TV ovládá obojí přes Wi-Fi, bez účtu a reklam.',
    h1='Jak ovládat televizi TCL telefonem',
    intro='TCL vyrábí televizi, ale software je Roku TV nebo Google TV (u starších modelů Android TV). Mando TV ovládá oba systémy a funguje jako dálkový ovladač k vaší televizi TCL přes Wi-Fi. Zdarma, bez účtu a reklam.',
    pasos=[
      'Zjistěte, jaký systém vaše TCL používá. Pokud úvodní obrazovka ukazuje jednoduchou mřížku dlaždic kanálů, je to Roku TV. Pokud vypadá jako Google TV nebo Android TV s řadami doporučení, je to Google TV.',
      'Připojte telefon a televizi TCL ke stejné síti Wi-Fi.',
      'Otevřete Mando TV. TCL se v seznamu objeví samo. Klepněte na něj.',
      'U TCL s Roku TV není potřeba nic dalšího. U TCL s Google TV zadáte 6znakový kód, který televize zobrazí na obrazovce (jen poprvé).',
      'Používejte šipky, OK, Zpět, Domů, hlasitost a klávesnici. Televizi zapněte z aplikace, pokud jste zapnuli zapnutí přes síť (viz níže).',
    ],
    extra=[
      ('Zapnutí televize TCL z telefonu', 'U TCL s Roku TV zapněte „Rychlé spuštění TV“ v Nastavení > Systém > Napájení. U TCL s Google TV hledejte v nastavení sítě nebo napájení možnost Wake on LAN, „Zapnutí přes síť“ nebo vzdálené spuštění. Některé modely ji nenabízejí. V takovém případě televizi zapněte fyzickým tlačítkem, většinou dole uprostřed nebo vzadu.'),
      ('Když se vaše TCL nezobrazí', 'Zkontrolujte, zda jsou telefon a televize ve stejné Wi-Fi. Routery s oddělenými sítěmi 2,4 GHz a 5 GHz mohou zařízení před sebou schovat. Na iPhonu povolte Mando TV v Nastavení „Místní síť“. Televizi můžete přidat také zadáním její adresy IP. Přečtěte si [Telefon nenajde televizi](@not-found).'),
      ('Více k vaší TCL', 'Pro TCL s Roku TV viz [Ovládací aplikace pro Roku](@roku), pro TCL s Google TV nebo Android TV [Ovládací aplikace pro Android TV](@android).'),
      ('Zdarma a Pro', 'Šipky, OK, Zpět, Domů, hlasitost, kanály, číslice, klávesnice, otevírání aplikací, přepínání vstupů a zapnutí či vypnutí jsou zdarma, bez reklam a předplatného. Touchpad, hlasové příkazy, oblíbené aplikace, rutiny a časovač vypnutí jsou součástí Mando TV Pro, jednorázového nákupu bez předplatného.'),
    ],
    marca=None,
    faq=[
      ('Funguje Mando TV s každou televizí TCL?', 'Funguje s televizemi TCL s Roku TV, Google TV nebo Android TV, tedy s většinou chytrých televizí TCL. TCL, která není chytrá, se přes Wi-Fi ovládat nedá.'),
      ('Potřebuji aplikaci TCL nebo účet TCL?', 'Ne. Mando TV se připojuje přímo přes vaši domácí Wi-Fi a účet nevyžaduje.'),
      ('Moje TCL žádá kód. Kde je?', 'Modely TCL s Google TV a Android TV zobrazí 6znakový kód na obrazovce. Zadejte ho do Mando TV přesně tak, jak je zobrazen. TCL s Roku TV na kód nežádá.'),
    ]),
  dict(clave='hisense', corto='Ovladač Hisense', fecha='2026-11-23',
    titulo='Ovládací aplikace Hisense: co funguje v telefonu',
    desc='Ovladač Hisense s Mando TV: ovládání VIDAA, Roku TV, Google TV a Fire TV přes Wi-Fi. Upřímný přehled toho, co funguje.',
    h1='Ovládací aplikace Hisense: co funguje a co ne',
    intro='Televize Hisense nejsou uvnitř všechny stejné. Podle modelu používají vlastní systém Hisense VIDAA, Roku TV, Google TV nebo Fire TV. Mando TV funguje jako ovladač k Hisense na všech čtyřech systémech, s jednou výjimkou u některých novějších modelů VIDAA. Tady zjistíte, jak poznat, jaký systém máte a co vás čeká.',
    pasos=[
      'Zjistěte, jaký systém vaše Hisense používá. VIDAA je vlastní rozhraní Hisense. Roku TV zobrazuje mřížku dlaždic kanálů. Google TV zobrazuje řady doporučení. Fire TV zobrazuje úvodní obrazovku Fire TV s řadami Amazonu.',
      'Připojte telefon a televizi Hisense ke stejné síti Wi-Fi.',
      'Otevřete Mando TV. Televize se v seznamu objeví sama. Klepněte na ni.',
      'Modely VIDAA a Fire TV mohou zobrazit PIN se čtyřmi číslicemi; Google TV zobrazí kód se šesti znaky. Zadejte ho do aplikace. Roku TV se na nic neptá. Uděláte to jen jednou.',
      'Používejte šipky, OK, Zpět, Domů, hlasitost a klávesnici v telefonu.',
    ],
    extra=[
      ('Hisense s Roku TV nebo Google TV', 'Fungují zcela jako každá jiná televize Roku nebo Google TV. Podrobnosti na stránkách [Ovládací aplikace pro Roku](@roku) a [Ovládací aplikace pro Android TV](@android).'),
      ('Hisense s Fire TV', 'Podpora Fire TV je v Mando TV nová. Aktualizujte aplikaci na nejnovější verzi ve svém obchodě. Jak funguje párování pomocí PIN, najdete na stránce [Ovladač Fire TV](@firetv). Pokud něco nefunguje podle očekávání, napište nám přes stránku nápovědy a uveďte model.'),
      ('Hisense s VIDAA', 'Většina modelů VIDAA funguje: tlačítka, hlasitost, klávesnice, aplikace a vstupy. Některé novější modely VIDAA přijímají jen oficiální aplikaci Hisense. Mando TV to při připojení pozná a jasně vám to řekne, místo aby tiše selhalo. V takovém případě je správnou cestou aplikace Hisense pro váš model, tlačítka na televizi nebo původní ovladač.'),
      ('Zapnutí Hisense z telefonu', 'U Hisense s Roku TV zapněte „Rychlé spuštění TV“ v Nastavení > Systém > Napájení. U Google TV hledejte možnost Wake on LAN nebo „Zapnutí přes síť“. Pokud žádná neexistuje, použijte tlačítko zapnutí na televizi.'),
      ('Zdarma a Pro', 'Šipky, OK, Zpět, Domů, hlasitost, kanály, číselná tlačítka, klávesnice, otevírání aplikací, přepínání vstupů a zapnutí či vypnutí jsou zdarma, bez reklam a bez předplatného. Touchpad, hlasové příkazy, oblíbené aplikace, rutiny a časovač vypnutí jsou součástí Mando TV Pro, jednorázového nákupu bez předplatného.'),
    ],
    marca=None,
    faq=[
      ('Funguje Mando TV s Hisense VIDAA?', 'Ano, s většinou modelů VIDAA. Některé novější přijímají jen oficiální aplikaci Hisense; Mando TV to pozná a řekne vám to. Televize Hisense s Roku TV, Google TV nebo Fire TV jsou také podporovány.'),
      ('Jak poznám, zda je moje Hisense Roku TV, Google TV nebo Fire TV?', 'Podívejte se na úvodní obrazovku. Roku TV má jednoduchou mřížku dlaždic a při startu logo Roku. Google TV má řady doporučení. Fire TV má úvodní obrazovku Amazon Fire TV. Název modelu v Nastavení > Informace také napoví.'),
      ('Potřebuji účet Hisense nebo Google?', 'Ne. Mando TV se připojuje přímo přes vaši domácí Wi-Fi a nemá vlastní účet.'),
    ]),
  dict(clave='philips', corto='Ovladač Philips', fecha='2026-11-23',
    titulo='Ovládací aplikace Philips: Roku TV, Google TV, Android TV',
    desc='Mando TV ovládá televize Philips s Roku TV, Google TV nebo Android TV přes Wi-Fi, z telefonu nebo počítače. Titan OS není podporován.',
    h1='Jak ovládat televizi Philips telefonem',
    intro='Televize Philips používají podle země a roku výroby různé systémy: Roku TV v USA, Google TV nebo Android TV v mnoha zemích a Titan OS u některých novějších evropských modelů. Mando TV ovládá modely s Roku TV, Google TV a Android TV přes Wi-Fi.',
    pasos=[
      'Zkontrolujte úvodní obrazovku. Roku TV zobrazuje mřížku dlaždic. Google TV a Android TV zobrazují řady doporučení od Googlu. Titan OS má vlastní úvodní obrazovku.',
      'Připojte telefon a televizi ke stejné síti Wi-Fi.',
      'Otevřete Mando TV a v seznamu klepněte na svou televizi Philips.',
      'Roku TV se na nic neptá. Google TV a Android TV zobrazí 6znakový kód: zadejte ho do aplikace jednou.',
      'Používejte šipky, OK, Zpět, Domů, hlasitost a klávesnici.',
    ],
    extra=[
      ('Philips Roku TV', 'Funguje jako každá televize Roku. Aby šla zapnout z telefonu, zapněte „Rychlé spuštění TV“ v Nastavení > Systém > Napájení. Více na stránce [Ovládací aplikace pro Roku](@roku).'),
      ('Philips s Google TV nebo Android TV', 'Patří sem mnoho modelů s Ambilight. Párují se kódem na obrazovce. Aby šly zapnout z telefonu, hledejte v nastavení sítě nebo napájení Wake on LAN nebo „Zapnutí přes síť“. U některých modelů tato možnost chybí. Více na stránce [Ovládací aplikace pro Android TV](@android).'),
      ('Starší televize Philips bez Androidu', 'Televize Philips z let 2011 až 2015, které nepoužívají Android, jsou v Mando TV podporovány v betě. Je nová a nevyžaduje párovací kód.'),
      ('Philips s Titan OS', 'Titan OS je jiný systém, který Mando TV dnes neovládá, a raději to říkáme jasně. Novější modely Philips bez Androidu také nejsou podporovány.'),
      ('Zdarma a Pro', 'Ovladač si můžete zdarma stáhnout a používat, bez reklam a bez předplatného. Mando TV Pro je volitelný jednorázový nákup za doplňky.'),
    ],
    marca=None,
    faq=[
      ('Funguje Mando TV s televizemi Philips?', 'S televizemi Philips, které používají Roku TV, Google TV nebo Android TV, ano, a v betě s televizemi Philips z let 2011 až 2015 bez Androidu. Modely s Titan OS podporovány nejsou.'),
      ('Ovládá Mando TV Ambilight?', 'Mando TV je ovladač: odesílá tlačítka, takže se šipkami a OK dostanete do nastavení Ambilight. Samostatné ovládání Ambilight neexistuje.'),
      ('Potřebuji účet Philips nebo Google?', 'Ne. Mando TV se připojuje přes vaši domácí Wi-Fi a účet nevyžaduje.'),
    ]),
]
OTRAS_GUIAS += [
  ('no-sub', 'Ovládací aplikace bez předplatného a bez reklam'),
  ('roku-app-alt', 'Alternativa k aplikaci Roku: jedna pro všechny televize'),
  ('lg-thinq', 'Alternativa k aplikaci LG ThinQ pro vaši televizi LG'),
  ('smartthings', 'Alternativa k SmartThings pro televize Samsung'),
  ('googletv-alt', 'Alternativa k ovladači Google TV v telefonu'),
  ('windows', 'Ovládací aplikace pro počítač s Windows'),
  ('iphone', 'Ovládací aplikace pro iPhone: jedna pro všechny televize'),
  ('firetv', 'Ovladač Fire TV pro telefon nebo počítač'),
  ('firetv-lost', 'Ztracený ovladač Fire TV: jak použít telefon'),
  ('turn-on', 'Jak zapnout televizi bez ovladače'),
  ('sony', 'Jak ovládat televizi Sony telefonem'),
  ('tcl', 'Jak ovládat televizi TCL telefonem'),
  ('hisense', 'Ovládací aplikace Hisense: co funguje a co ne'),
  ('philips', 'Jak ovládat televizi Philips telefonem'),
]
# <<< guías traídas del inglés
