# Textos en rumano (tu) de mandotv.app. Los usa generar_idiomas.py. Escritos para las búsquedas de Rumania y Moldavia.
# Las claves de las páginas (lg, lost-tv, ...) y sus rutas están en idiomas_sitio.py.
# Los nombres de menús de cada marca (LG, Samsung, Roku, Android TV, iPhone) son los mismos que usa la app en rumano
# (lib/l10n/app_ro.arb del proyecto de la app).

UI = dict(
  locale='ro_RO',
  aria_home='Mando TV, pagina principală', aria_main='Meniu principal', nav_que='Funcții', nav_ayuda='Ajutor', nav_contacto='Contact',
  asunto='Salut%20Mando%20TV', inicio='Pagina principală', privacidad='Confidențialitate', aria_pie='Subsol', aria_ruta='Calea de navigare',
  aria_marcas='Mărci și ghiduri', hecho='Creat în Chile',
  aviso='Mando TV este o aplicație independentă. Nu are nicio legătură cu producătorii de televizoare menționați și nici cu Google, Amazon, Apple sau Roku și nu este susținută de aceștia. Mărcile aparțin proprietarilor lor și sunt menționate doar pentru a indica compatibilitatea. Android TV și Google TV sunt mărci ale Google LLC. Apple TV este o marcă a Apple Inc.',
  bajar='Descarcă gratuit', descarga='Descarcă din', anticipada='Acces anticipat pe',
  apple_aria='Descarcă Mando TV gratuit din App Store', ms_aria='Descarcă Mando TV gratuit din Microsoft Store',
  gp_aria='Acces anticipat la Mando TV pe Google Play pentru Android', aria_desc='Descarcă Mando TV',
  b_como_btn='Cum te conectezi', b_tiendas_label='Disponibilă în magazine',
  b_nota='iPhone, iPad, Mac, Android și Windows. Descărcare gratuită, fără reclame. Pro este o achiziție unică, fără abonament.',
  b_compat='Televizoare compatibile', b_otras='Alte mărci', b_otras_p='Mando TV controlează toate aceste mărci cu aceeași aplicație:',
  g_guias='Ghiduri', g_ver='Vezi pașii', g_pasos='Pas cu pas', g_hazlo='Cum faci cu Mando TV',
  g_tiendas='Mando TV este o telecomandă universală pentru televizorul tău. Descarc-o gratuit, fără reclame și fără cont. Pro este o achiziție unică opțională, fără abonament. Pentru iPhone, iPad, Windows și Android:',
  g_nota='Android: acces anticipat gratuit pe Google Play. <a href="{enlace}">Participă în doi pași</a> și ajută-ne să ajungem în magazin.',
  g_mas_pagina='Găsești mai multe detalii pe pagina {enlace}.', g_mas_marca='Mai multe detalii, în funcție de marcă:',
  g_faq='Întrebări frecvente', g_mas='Alte ghiduri', g_todas='Toate ghidurile', g_ayuda='Ajutor și asistență',
  g_idiomas='Acest ghid în alte limbi',
)

# Pie de página y listas de marcas/guías: (clave, texto)
PIE = [
  ('samsung', 'Telecomandă Samsung'),
  ('lg', 'Telecomandă LG'),
  ('roku', 'Telecomandă Roku'),
  ('android', 'Telecomandă Android TV'),
  ('guias', 'Toate ghidurile'),
  ('lost-tv', 'Telecomandă pierdută'),
  ('lost-lg', 'Telecomandă LG pierdută'),
  ('lg-on', 'Pornește televizorul LG cu telefonul'),
  ('hdmi', 'Schimbă intrarea HDMI fără telecomandă'),
  ('androidtv', 'Android TV fără telecomandă'),
  ('console', 'Televizor și HDMI consolă fără telecomandă'),
  ('samsung-lost', 'Televizor Samsung fără telecomandă'),
  ('roku-lost', 'Telecomandă Roku pierdută'),
  ('roku-403', 'Aplicația Roku nu funcționează'),
  ('androidtv-code', 'Cod de asociere Android TV'),
  ('not-found', 'Telefonul nu găsește televizorul'),
  ('wifi', 'Telefon ca telecomandă prin Wi-Fi'),
  ('pc', 'Controlează televizorul de pe PC'),
]
NOMBRE_OTRA = {'lg': 'Aplicație telecomandă LG', 'samsung': 'Aplicație telecomandă Samsung', 'roku': 'Aplicație telecomandă Roku',
               'android': 'Aplicație telecomandă Android TV și Google TV'}
PAGINA_MARCA = {'lg': 'Aplicație telecomandă LG', 'samsung': 'Aplicație telecomandă Samsung', 'roku': 'Aplicație telecomandă Roku',
                'android': 'Aplicație telecomandă Android TV'}

OTRAS_GUIAS = [
  ('lg-on', 'Pornește televizorul LG cu telefonul'),
  ('lost-tv', 'Telecomandă pierdută: ce poți face'),
  ('lost-lg', 'Telecomandă LG pierdută: folosește telefonul'),
  ('hdmi', 'Schimbă intrarea HDMI a televizorului fără telecomandă'),
  ('androidtv', 'Android TV fără telecomandă: folosește telefonul'),
  ('console', 'Pornește televizorul și treci pe HDMI-ul consolei, fără telecomandă'),
  ('samsung-lost', 'Televizor Samsung fără telecomanda originală: folosește telefonul'),
  ('roku-lost', 'Telecomandă Roku pierdută: folosește telefonul'),
  ('roku-403', 'Aplicația Roku nu funcționează: rezolvă eroarea 403'),
  ('androidtv-code', 'Android TV cere un cod de asociere: ce ai de făcut'),
  ('not-found', 'Telefonul nu găsește televizorul: ce să verifici'),
  ('wifi', 'Cum folosești telefonul ca telecomandă prin Wi-Fi'),
  ('pc', 'Cum controlezi televizorul cu un PC cu Windows'),
]

INDICE = dict(
  titulo='Ghiduri: controlează televizorul cu telefonul | Mando TV',
  desc='Ghiduri pas cu pas: folosește telefonul sau PC-ul ca telecomandă, pornește televizorul, schimbă HDMI și rezolvă problemele la Samsung, LG, Roku.',
  h1='Ghiduri: folosește telefonul ca telecomandă',
  intro='Pași simpli pentru a conecta telecomanda televizorului tău Samsung, LG, Roku sau Android TV cu Mando TV, pentru a-l porni și a rezolva problemele.',
  h2_guias='Toate ghidurile', h2_marcas='Aplicație telecomandă în funcție de marcă',
  marcas_extra=[('sony', 'Aplicație telecomandă Sony'), ('philips', 'Aplicație telecomandă Philips')],
)

MARCAS = [
  dict(clave='lg', color='#e0457b', corto='LG',
    titulo='Aplicație telecomandă TV LG pentru telefon, gratis | Mando TV',
    desc='Telefonul sau PC-ul tău ca telecomandă TV LG cu webOS, prin Wi-Fi. Butoane, tastatură, aplicații, intrări și pornire gratis; cursor cu Pro.',
    h1='Telecomandă TV LG ca aplicație pentru telefon',
    intro='Mando TV este o aplicație de telecomandă pentru televizoarele LG: transformă telefonul sau computerul tău, prin Wi-Fi-ul de acasă, în telecomanda Smart TV-ului LG cu webOS. Te ajută când ai pierdut telecomanda, când bateriile s-au terminat sau când vrei pur și simplu să scrii mai repede.',
    compat='Smart TV LG cu webOS (majoritatea modelelor Smart TV LG din 2014 încoace). Funcționează cu televizoare LED, NanoCell, QNED și OLED. Smart TV-urile LG mai vechi cu NetCast (2011 până în 2014, înainte de webOS) sunt acum acceptate în versiunea beta: se asociază cu cheia de 6 cifre afișată de televizor.',
    h2=dict(funciones='Ce poți face cu televizorul tău LG', como='Cum îți conectezi televizorul LG cu Mando TV',
            encender='Pornește televizorul LG cu telefonul', preguntas='Întrebări despre LG', guias='Ghiduri pentru LG'),
    funciones=[
      ('Toate butoanele', 'Săgeți, OK, Înapoi, Acasă, volum, canale, mut și redare.'),
      ('Cursor ca la Magic Remote (Pro)', 'Mută săgeata pe ecran cu degetul, exact ca la LG Magic Remote.'),
      ('Tastatură', 'Scrie în YouTube, Netflix sau în browserul televizorului cu tastatura telefonului.'),
      ('Aplicații și intrări', 'Deschide-ți aplicațiile și treci pe HDMI, TV live, AirPlay sau Screen Share.'),
      ('Ieșire audio (Pro)', 'Comută între difuzoarele televizorului și soundbar.'),
      ('Pornește televizorul', 'Dacă este oprit, Mando TV îl pornește prin rețea și se conectează singură.'),
    ],
    pasos=[
      'Conectează telefonul și televizorul la același Wi-Fi.',
      'Deschide Mando TV: televizorul tău LG apare singur în listă. Atinge-l.',
      'Pe televizor apare o fereastră care cere permisiunea. Confirm-o cu telecomanda obișnuită (doar prima dată).',
    ],
    encender='Activează „Pornire TV de pe dispozitiv mobil” (la unele modele se numește „Pornire prin Wi-Fi”). O găsești la Setări > General > Dispozitive > Dispozitive externe (la modelele mai vechi: Conexiune > Gestionare conexiune mobilă). După aceea, când atingi în Mando TV televizorul oprit, aplicația te întreabă dacă vrei să îl pornească și se conectează singură.',
    faq=[
      ('Am nevoie de Magic Remote ca să folosesc Mando TV?', 'Doar prima dată, ca să confirmi fereastra de pe ecran. După aceea îți ajunge telefonul.'),
      ('Înlocuiește Mando TV aplicația LG ThinQ?', 'Pentru controlul televizorului, da: nu ai nevoie de cont LG și nici nu trebuie să înregistrezi televizorul. Mando TV se conectează direct prin Wi-Fi-ul tău.'),
      ('Pot porni televizorul LG cu telefonul?', 'Da, dacă ai activat pe televizor „Pornire TV de pe dispozitiv mobil” și te-ai conectat o dată cât timp televizorul era pornit.'),
      ('Funcționează cu televizoarele LG mai vechi, dinainte de webOS?', 'În versiunea beta, da, cu Smart TV-uri LG NetCast din 2011 până în 2014. Se asociază cu cheia de 6 cifre afișată de televizor. Funcția este nouă și poate avea încă mici probleme.'),
    ],
    guias=[('lg-on', 'Cum pornești un televizor LG cu telefonul'),
           ('lost-lg', 'Telecomandă LG pierdută: folosește telefonul'),
           ('hdmi', 'Schimbă intrarea HDMI a televizorului fără telecomandă'),
           ('guias', 'Toate ghidurile pentru a controla televizorul cu telefonul')]),
  dict(clave='samsung', color='#3d7bff', corto='Samsung',
    titulo='Aplicație telecomandă TV Samsung pentru telefon | Mando TV',
    desc='Telefonul sau PC-ul tău ca telecomandă TV Samsung cu Tizen, prin Wi-Fi. Butoane, tastatură, aplicații și pornire gratis; touchpad cu Pro. Fără reclame.',
    h1='Telecomandă TV Samsung ca aplicație pentru telefon',
    intro='Mando TV este o aplicație de telecomandă pentru televizoarele Samsung: transformă telefonul sau computerul tău, prin Wi-Fi-ul de acasă, în telecomanda Smart TV-ului Samsung. Nu ai nevoie de cont Samsung și nici nu trebuie să înregistrezi televizorul.',
    compat='Smart TV Samsung cu Tizen, fabricate în 2016 sau mai recent (serii precum Crystal UHD, QLED, Neo QLED, The Frame și OLED).',
    h2=dict(funciones='Ce poți face cu televizorul tău Samsung', como='Cum îți conectezi televizorul Samsung cu Mando TV',
            encender='Pornește televizorul Samsung cu telefonul', preguntas='Întrebări despre Samsung', guias='Ghiduri pentru Samsung'),
    funciones=[
      ('Toate butoanele', 'Săgeți, OK, Înapoi, Acasă, volum, canale, mut și sursă.'),
      ('Touchpad (Pro)', 'Glisează cu degetul prin meniuri, fără să cauți săgețile.'),
      ('Tastatură', 'Scrie căutări și parole cu tastatura telefonului.'),
      ('Aplicații', 'Deschide Netflix, YouTube, Prime Video și celelalte aplicații cu o atingere.'),
      ('Pornește televizorul', 'Dacă este oprit, Mando TV îl pornește prin rețea și se conectează singură.'),
      ('Fără cont', 'Conexiunea merge direct prin Wi-Fi-ul tău, fără să treacă prin internet.'),
    ],
    pasos=[
      'Conectează telefonul și televizorul la același Wi-Fi.',
      'Deschide Mando TV: televizorul tău Samsung apare singur în listă. Atinge-l.',
      'Televizorul te întreabă dacă permiți conexiunea. Alege cu telecomanda „Permite” (doar prima dată).',
    ],
    encender='Pe televizorul Samsung, la Setări > General > Rețea > Setări expert, activează „Pornire cu dispozitiv mobil”. După aceea, când atingi în Mando TV televizorul oprit, aplicația te întreabă dacă vrei să îl pornească și se conectează singură.',
    faq=[
      ('Am refuzat permisiunea din greșeală. Ce fac?', 'Pe televizor, mergi la Setări > General > Manager dispozitive externe > Manager conexiuni dispozitive și setează Mando TV ca permis.'),
      ('Înlocuiește Mando TV aplicația SmartThings?', 'Pentru controlul televizorului, da, și fără cont Samsung. Mando TV se conectează direct prin Wi-Fi-ul tău.'),
      ('Funcționează cu televizoarele Samsung mai vechi?', 'Funcționează cu televizoarele Samsung cu Tizen, fabricate în 2016 sau mai recent. Modelele mai vechi folosesc alt sistem, pe care încă nu îl acceptăm.'),
    ],
    guias=[('samsung-lost', 'Televizor Samsung fără telecomanda originală: folosește telefonul'),
           ('smartthings', 'Alternativă la SmartThings pentru televizoare Samsung'),
           ('turn-on', 'Cum pornești un televizor fără telecomandă'),
           ('hdmi', 'Schimbă intrarea HDMI a televizorului fără telecomandă'),
           ('guias', 'Toate ghidurile pentru a controla televizorul cu telefonul')]),
  dict(clave='roku', color='#a77bff', corto='Roku',
    titulo='Aplicație telecomandă Roku pentru telefon, gratis | Mando TV',
    desc='Telefonul sau PC-ul tău ca telecomandă Roku pentru Roku TV și Roku Player, prin Wi-Fi. Butoane, tastatură, canale, intrări și pornire gratis.',
    h1='Telecomandă Roku ca aplicație pentru telefon',
    intro='Mando TV este o aplicație de telecomandă pentru Roku: transformă telefonul sau computerul tău, prin Wi-Fi-ul de acasă, în telecomanda Roku-ului tău. Funcționează cu televizoare Roku TV și cu playere Roku conectate la portul HDMI.',
    compat='Televizoare Roku TV (TCL, Hisense, Philips, Sharp, JVC și altele) și playere Roku (Express, Streaming Stick, Ultra).',
    h2=dict(funciones='Ce poți face cu Roku-ul tău', como='Cum îți conectezi Roku-ul cu Mando TV',
            encender='Pornește Roku cu telefonul', preguntas='Întrebări despre Roku', guias='Ghiduri pentru Roku'),
    funciones=[
      ('Toate butoanele', 'Săgeți, OK, Înapoi, Acasă, volum, mut, reluare și redare.'),
      ('Tastatură', 'Scrie căutări în canalele Roku cu tastatura telefonului.'),
      ('Canale', 'Deschide Netflix, YouTube și celelalte canale Roku cu o atingere.'),
      ('Intrări', 'La un Roku TV, treci din aplicație pe HDMI, antenă sau AV.'),
      ('Pornește televizorul', 'La televizoarele Roku TV cu pornire rapidă, Mando TV le pornește de pe telefon.'),
      ('Fără asociere', 'Roku nu cere niciun cod: atinge-l în listă și ești conectat.'),
      ('Sună telecomanda', 'Dacă telecomanda ta Roku are difuzor, ca Roku Voice Remote Pro, Mando TV o face să sune ca să o găsești. Gratis, cu Roku pornit.'),
    ],
    pasos=[
      'Conectează telefonul și Roku-ul la același Wi-Fi.',
      'Deschide Mando TV: Roku-ul tău apare singur în listă. Atinge-l.',
      'Dacă nu se conectează, mergi pe Roku la Setări > Sistem > Setări avansate de sistem > Control prin aplicații mobile și setează accesul la rețea pe Implicit sau Permisiv (la software-ul Roku mai nou, setează „Control prin aplicații mobile” pe Activat).',
    ],
    encender='La televizoarele Roku TV, activează la Setări > Sistem > Alimentare opțiunea „Pornire rapidă TV”. Playerele Roku conectate la alt televizor nu pot fi pornite astfel. După aceea, când atingi în Mando TV televizorul oprit, aplicația te întreabă dacă vrei să îl pornească și se conectează singură.',
    faq=[
      ('Funcționează cu Roku Express sau cu Streaming Stick?', 'Da. Toate playerele Roku și televizoarele Roku TV se controlează în același fel.'),
      ('Mando TV nu găsește Roku-ul meu. Ce fac?', 'Verifică dacă ambele sunt în același Wi-Fi și dacă „Control prin aplicații mobile” nu este dezactivat pe Roku. Îl poți adăuga și după adresa IP.'),
      ('Am nevoie de cont Roku?', 'Nu. Mando TV se conectează direct prin Wi-Fi-ul tău.'),
    ],
    guias=[('roku-403', 'Aplicația Roku nu funcționează (eroarea 403)'),
           ('roku-lost', 'Telecomandă Roku pierdută: folosește telefonul'),
           ('tcl', 'Aplicație telecomandă TCL'),
           ('hisense', 'Aplicație telecomandă Hisense'),
           ('philips', 'Aplicație telecomandă Philips'),
           ('guias', 'Toate ghidurile pentru a controla televizorul cu telefonul')]),
  dict(clave='android', color='#2fbf8f', corto='Android TV și Google TV',
    titulo='Telecomandă Google TV și Android TV pe telefon | Mando TV',
    desc='Telecomandă Google TV și Android TV (Sony, TCL, Hisense, Xiaomi) pe telefon sau PC, prin Wi-Fi. Butoane, aplicații și pornire gratis; touchpad cu Pro.',
    h1='Telecomandă Google TV și Android TV ca aplicație pentru telefon',
    intro='Mando TV este o aplicație de telecomandă pentru Android TV: transformă telefonul sau computerul tău, prin Wi-Fi-ul de acasă, în telecomanda televizorului tău Android TV sau Google TV. Funcționează și de pe iPhone și de pe Windows.',
    compat='Televizoare cu Google TV sau Android TV de la Sony, Philips, TCL, Hisense, Sharp, Xiaomi, Toshiba, Panasonic, Haier, Skyworth, JVC, Thomson, Motorola, OnePlus, iFFALCON, Kogan, Vu și alte mărci, plus Chromecast cu Google TV, Google TV Streamer, onn. și Nvidia Shield. Unele dintre aceste mărci vând și modele cu alt sistem: dacă televizorul tău arată ecranul de start Google TV sau are Google Play Store, Mando TV îl controlează.',
    h2=dict(funciones='Ce poți face cu Android TV-ul tău', como='Cum îți conectezi Android TV-ul cu Mando TV',
            encender='Pornește Android TV cu telefonul', preguntas='Întrebări despre Android TV', guias='Ghiduri pentru Android TV'),
    funciones=[
      ('Toate butoanele', 'Săgeți, OK, Înapoi, Acasă, volum, mut și redare.'),
      ('Touchpad (Pro)', 'Glisează cu degetul ca să te miști rapid prin meniurile Google TV.'),
      ('Tastatură', 'Scrie căutări și parole cu tastatura telefonului.'),
      ('Aplicații', 'Deschide YouTube, Netflix, Disney+ și celelalte aplicații cu o atingere.'),
      ('Pornește televizorul', 'La modelele cu pornire prin rețea, Mando TV pornește televizorul și se conectează singură.'),
      ('iPhone, Android și PC', 'Funcționează la fel pe orice telefon și pe orice computer.'),
    ],
    pasos=[
      'Conectează telefonul și televizorul la același Wi-Fi.',
      'Deschide Mando TV: Android TV-ul tău apare singur în listă. Atinge-l.',
      'Televizorul afișează un cod de 6 caractere. Introdu-l în Mando TV (doar prima dată).',
    ],
    encender='Depinde de producător. Caută în setările de rețea sau de alimentare „Wake on LAN”, „Pornire prin rețea”, „Standby în rețea” sau „Remote start”. Unele modele nu au această opțiune. După aceea, când atingi în Mando TV televizorul oprit, aplicația te întreabă dacă vrei să îl pornească și se conectează singură.',
    faq=[
      ('Funcționează cu Chromecast cu Google TV?', 'Da, asocierea se face cu codul de 6 caractere care apare pe ecran.'),
      ('Cu ce diferă de aplicația Google TV?', 'Mando TV nu cere cont Google, funcționează și pe Windows și controlează televizoare LG, Samsung și Roku cu aceeași aplicație.'),
      ('Codul nu apare pe ecran. Ce fac?', 'Închide Mando TV, deschide din nou aplicația și atinge încă o dată televizorul. Verifică dacă televizorul nu este într-un mod de economisire a energiei foarte profund.'),
    ],
    guias=[('androidtv-code', 'Android TV cere un cod de asociere: ce ai de făcut'),
           ('androidtv', 'Android TV fără telecomandă: folosește telefonul'),
           ('googletv-alt', 'Alternativă la telecomanda Google TV de pe telefon'),
           ('sony', 'Aplicație telecomandă Sony'),
           ('tcl', 'Aplicație telecomandă TCL'),
           ('hisense', 'Aplicație telecomandă Hisense'),
           ('philips', 'Aplicație telecomandă Philips'),
           ('guias', 'Toate ghidurile pentru a controla televizorul cu telefonul')]),
]

GUIAS = [
  dict(clave='lost-tv', corto='Telecomandă pierdută',
    titulo='Telecomandă pierdută? Controlează televizorul cu telefonul',
    desc='Ți-ai pierdut telecomanda? Pornește televizorul de la buton și folosește telefonul ca telecomandă. Pași pentru LG, Samsung, Roku, Android TV. Gratis.',
    h1='Telecomandă pierdută? Ce poți face acum',
    intro='Telecomanda pierdută se întâmplă în orice casă: dispare exact când vrei să te uiți la ceva. Vestea bună: telefonul tău poate înlocui telecomanda prin Wi-Fi-ul de acasă. Iată ce poți face, pe rând.',
    pasos=[
      'Pornește televizorul cu butonul de pe aparat. Aproape întotdeauna se află jos, la mijloc, sau în spate, lângă un colț. Uneori este un singur buton, alteori un mic joystick.',
      'Conectează telefonul la același Wi-Fi ca televizorul.',
      'Descarcă Mando TV, care este gratuită și nu cere cont, și deschide aplicația. Televizorul tău apare singur în listă. Atinge-l.',
      'Confirmă conexiunea pentru marca ta. La LG și Samsung, televizorul afișează o fereastră: confirm-o cu butonul sau cu joystickul de pe televizor. La Android TV și Google TV, introduci un cod de 6 caractere care apare pe ecran. Roku nu cere nimic.',
      'Gata. Săgețile, OK, Înapoi, Acasă, volumul, canalele și tastatura sunt gratuite.',
      'Pentru data viitoare: activează în setările televizorului pornirea prin rețea (ghidul pentru marca ta este mai jos). Astfel poți porni televizorul de pe telefon, fără să te atingi de el.',
    ],
    extra=[
      ('Alege ghidul pentru marca ta', 'LG: [Telecomandă LG pierdută](@lost-lg). Android TV și Google TV: [Android TV fără telecomandă](@androidtv). Samsung: [Televizor Samsung fără telecomandă](@samsung-lost). Roku: [Telecomandă Roku pierdută](@roku-lost).'),
      ('Dacă televizorul nu pornește de la buton', 'Înainte să cauți altă telecomandă, verifică dacă cablul este bine băgat și dacă priza are curent. Dacă butonul de pe televizor nu face nimic, problema este la televizor, nu la telecomandă.'),
      ('Dacă telecomanda pur și simplu nu mai funcționează', 'Încearcă baterii noi. Poți verifica dacă mai trimite semnal îndreptând-o spre camera telefonului și apăsând un buton: la multe telefoane vezi o lumină violetă pe ecran. Dacă vezi lumina și televizorul nu reacționează, poate senzorul televizorului este acoperit.'),
      ('Dacă ai schimbat routerul și televizorul nu mai are Wi-Fi', 'Fără telecomandă este mai greu să conectezi televizorul la rețeaua nouă. Cel mai simplu este să legi televizorul la router cu un cablu de rețea. Poți configura și un Wi-Fi cu același nume și aceeași parolă ca înainte: televizorul se conectează de obicei singur la el.'),
      ('Ce este gratuit și ce este Pro', 'Pornirea și oprirea televizorului, săgețile, OK, volumul, canalele, tastele numerice, tastatura, deschiderea aplicațiilor și schimbarea intrării sunt gratuite. Touchpadul, vocea și rutinele fac parte din Mando TV Pro, o achiziție unică, fără abonament.'),
    ],
    marca=None,
    faq=[
      ('Pot porni televizorul cu telefonul dacă nu l-am conectat niciodată?', 'Prima dată îl pornești cu butonul de pe televizor. După ce ai conectat telefonul și ai activat în setările televizorului pornirea prin rețea, îl poți porni din aplicație.'),
      ('Trebuie să cumpăr o telecomandă nouă?', 'Nu neapărat. Cu Mando TV ai gratuit butoanele, volumul, tastatura și pornirea. Dacă totuși preferi o telecomandă adevărată, caută modelul exact al televizorului tău.'),
      ('Funcționează dacă televizorul nu are Wi-Fi?', 'De cele mai multe ori nu. Telefonul și televizorul trebuie, de regulă, să fie în același Wi-Fi. Excepțiile sunt infraroșul pe telefoanele Android cu emițător de infraroșu, care controlează și televizoare fără funcție Smart TV, și Bluetooth-ul din versiunea beta, de la Android 9, care funcționează fără Wi-Fi cu Google TV, Android TV și Fire TV.'),
    ]),
  dict(clave='lost-lg', corto='Telecomandă LG pierdută',
    titulo='Telecomandă LG pierdută? Folosește telefonul',
    desc='Nu ai telecomandă LG? Pornește televizorul de la buton, confirmă fereastra și folosește telefonul prin Wi-Fi. Fără cont LG, fără reclame.',
    h1='Telecomandă LG pierdută? Folosește telefonul',
    intro='Dacă ți-ai pierdut telecomanda LG sau Magic Remote nu mai funcționează, telefonul o înlocuiește prin Wi-Fi. Merge cu televizoarele LG cu webOS, adică aproape orice Smart TV LG din 2014 încoace. Nu ai nevoie de cont LG și nici de aplicația ThinQ.',
    pasos=[
      'Pornește televizorul cu butonul de jos, de sub sigla LG, sau cu butonul din spate. La multe modele este un joystick: apasă-l ca să deschizi meniul și mișcă-l ca să alegi.',
      'Conectează telefonul la același Wi-Fi ca televizorul.',
      'Deschide Mando TV și atinge în listă televizorul tău LG.',
      'Televizorul afișează o fereastră care cere permisiunea. Confirm-o cu joystickul sau cu butonul de pe televizor. Dacă ai mai conectat acest telefon, nu mai întreabă.',
      'Gata. Săgețile, OK, Înapoi, Acasă, volumul, canalele și tastatura sunt gratuite. Cursorul este o funcție Pro.',
      'Cu aplicația conectată, intră cu săgețile și OK în setări și activează „Pornire TV de pe dispozitiv mobil”. Ghidul [Pornește televizorul LG cu telefonul](@lg-on) îți arată unde găsești opțiunea.',
    ],
    extra=[
      ('Dacă televizorul nu afișează fereastra', 'Poate permisiunea este deja salvată sau telefonul este în altă rețea. Verifică dacă ambele sunt în același Wi-Fi și dacă VPN-ul este oprit. Dacă televizorul nu apare în listă, te ajută [Telefonul nu găsește televizorul](@not-found).'),
      ('Dacă televizorul și-a pierdut Wi-Fi-ul', 'Leagă televizorul la router cu un cablu de rețea și îl va folosi singur. Sau configurează un Wi-Fi cu același nume și aceeași parolă ca înainte, pentru că televizorul se conectează de obicei singur la el.'),
      ('Dacă televizorul a rămas pe altă intrare', 'Atinge pe telefon Intrări și alege portul HDMI. Mai multe găsești în [Schimbă intrarea HDMI a televizorului fără telecomandă](@hdmi).'),
    ],
    marca='lg',
    faq=[
      ('Am nevoie de Magic Remote ca să folosesc Mando TV?', 'Ai nevoie de ceva doar prima dată, ca să confirmi fereastra, și pentru asta ajunge butonul sau joystickul de pe televizor. După aceea folosești doar telefonul.'),
      ('Am nevoie de aplicația LG ThinQ?', 'Nu. Mando TV se conectează direct prin Wi-Fi-ul tău și nu cere cont LG.'),
      ('Pot opri și porni televizorul LG cu telefonul?', 'Oprirea, da. Pentru pornire trebuie să fi activat pe televizor „Pornire TV de pe dispozitiv mobil” și să te fi conectat o dată cât timp televizorul era pornit.'),
    ]),
  dict(clave='hdmi', corto='Schimbă HDMI fără telecomandă',
    titulo='Schimbă intrarea HDMI fără telecomandă (Samsung, LG, Roku)',
    desc='Schimbă intrarea HDMI fără telecomandă la Samsung, LG sau Roku: cu butonul de pe televizor sau cu telefonul. Gratis la început, fără reclame.',
    h1='Cum schimbi intrarea HDMI a televizorului fără telecomandă',
    intro='Consola sau playerul de streaming este gata, dar televizorul a rămas pe altă intrare, iar telecomanda nu se găsește nicăieri. Ca să schimbi intrarea HDMI fără telecomandă ai două variante: butonul de pe televizor sau telefonul. Iată pașii pentru Samsung, LG și Roku.',
    pasos=[
      'Încearcă mai întâi varianta cea mai simplă: pornește consola sau playerul. Dacă HDMI-CEC este activat pe televizor (la Samsung se numește Anynet+, la LG SIMPLINK), televizorul trece singur pe acea intrare.',
      'Dacă nu trece, folosește butonul de pe televizor, jos la mijloc sau în spate. La multe televizoare Samsung și LG este un joystick și deschide un meniu cu Sursă sau Intrări.',
      'În acest meniu alege intrarea: HDMI 1, HDMI 2 și așa mai departe. Numărul este portul în care este băgat cablul.',
      'Dacă preferi telefonul, conectează-l la același Wi-Fi, deschide Mando TV și atinge televizorul tău.',
      'La LG și Roku, atinge Intrări și alege portul HDMI. La Samsung, Intrări trimite tasta Sursă către televizor, iar tu alegi cu săgețile și OK.',
      'Poți ajunge la intrări și cu săgețile și OK de pe ecranul de start al televizorului. În funcție de marcă și de anul de fabricație, se numesc Sursă, Dispozitive conectate sau Intrări. La un Roku TV sunt casetele HDMI de pe ecranul de start.',
    ],
    extra=[
      ('Samsung', 'Dacă meniul butonului de pe televizor nu are opțiunea Sursă, deschide cu telefonul meniul ecranului de start și caută în stânga Sursă sau Dispozitive conectate. Îl controlezi cu săgețile și OK din Mando TV, care sunt gratuite.'),
      ('LG', 'Apasă joystickul de pe televizor și caută Intrări. Cu telefonul poți deschide în Mando TV și lista de intrări și atinge intrarea dorită.'),
      ('Roku TV', 'Pe ecranul de start există o casetă pentru fiecare intrare, de exemplu HDMI 1 sau HDMI 2. Mută-te cu săgețile și deschide-o cu OK, gratuit.'),
      ('Dacă este un televizor cu Android TV sau Google TV', 'În Mando TV nu există încă lista de intrări pentru Android TV. Folosește butonul de intrare de pe televizor sau ajunge la intrări cu săgețile și OK de pe ecranul de start. Dacă nu ai telecomandă și vrei să te conectezi, citește [Android TV fără telecomandă](@androidtv).'),
      ('Mai mult ajutor', 'Dacă televizorul nu pornește deloc sau nu știi de unde să începi, citește [Telecomandă pierdută](@lost-tv). Pentru jocurile pe consolă, ghidul [Pornește televizorul și treci pe HDMI-ul consolei, fără telecomandă](@console) conține trucul HDMI-CEC.'),
    ],
    marca=None,
    faq=[
      ('Este gratuită schimbarea intrării HDMI?', 'Da. Lista de intrări din Mando TV este gratuită, ca și pornirea televizorului, săgețile, OK și volumul. La intrări poți ajunge și prin meniul televizorului.'),
      ('Cum știu ce intrare HDMI am nevoie?', 'Uită-te la porturile HDMI de pe televizor: fiecare are un număr. Alege-l pe cel în care este băgat cablul consolei sau al playerului.'),
      ('Ce fac dacă televizorul nu pornește?', 'Pornește-l cu butonul de pe aparat. Dacă l-ai conectat deja o dată și ai activat pornirea prin rețea, îl poți porni și de pe telefon.'),
    ]),
  dict(clave='androidtv', corto='Android TV fără telecomandă',
    titulo='Android TV fără telecomandă: folosește telefonul',
    desc='Nu ai telecomandă Android TV sau Google TV? Conectează telefonul cu codul de 6 caractere de pe ecran. Gratis, fără cont, fără reclame.',
    h1='Android TV fără telecomandă: folosește telefonul',
    intro='Dacă ți-ai pierdut telecomanda Android TV sau Google TV ori bateriile ei s-au terminat, telefonul o înlocuiește. Cel mai bine: pentru conectare nu ai nevoie de telecomandă, pentru că televizorul afișează un cod pe ecran, iar tu îl scrii pe telefon. Funcționează cu televizoare Sony, Philips, TCL, Hisense, Sharp și Xiaomi cu Android TV, cu Chromecast cu Google TV și cu Nvidia Shield.',
    pasos=[
      'Pornește televizorul cu butonul de pe aparat. Aproape întotdeauna se află jos, la mijloc, sau în spate, lângă un colț.',
      'Conectează telefonul la același Wi-Fi ca televizorul.',
      'Descarcă Mando TV, care este gratuită și nu cere cont Google, și deschide aplicația. Atinge în listă televizorul tău.',
      'Televizorul afișează un cod de 6 litere și cifre. Scrie-l pe telefon și atinge Asociază. Pentru asta nu ai nevoie de telecomandă.',
      'Acum poți folosi săgețile, OK, Înapoi, Acasă, volumul, mut și tastatura. Sunt gratuite, la fel ca lista de aplicații. Touchpadul este Pro.',
      'Ca să pornești televizorul de pe telefon data viitoare, caută în setările de rețea sau de alimentare „Wake on LAN”, „Pornire prin rețea”, „Standby în rețea” sau „Remote start”.',
    ],
    extra=[
      ('Dacă televizorul nu pornește de pe telefon', 'Nu orice Android TV poate fi pornit prin rețea; depinde de producător și de model. Dacă al tău nu are funcția, pornește-l cu butonul de pe televizor și continuă de pe telefon. Îl poți opri din aplicație.'),
      ('Chromecast cu Google TV, Google TV Streamer și Shield', 'Se conectează în același fel: același Wi-Fi, atingi dispozitivul în listă și introduci codul. Dacă televizorul arată altă intrare, schimb-o pe portul HDMI în care este băgat dispozitivul, așa cum se explică în [Schimbă intrarea HDMI a televizorului fără telecomandă](@hdmi).'),
      ('Dacă codul nu apare sau este declarat greșit', 'Verifică dacă televizorul este cu adevărat pornit și nu în standby. Codul se schimbă la fiecare cerere: funcționează doar ultimul. Găsești mai multe detalii la [Android TV cere un cod de asociere](@androidtv-code).'),
      ('Aplicația Google sau Mando TV', 'Google are o aplicație proprie, pentru care ai nevoie de cont Google. Mando TV nu cere cont, funcționează și pe Windows și controlează televizoare LG, Samsung și Roku cu aceeași aplicație.'),
    ],
    marca='android',
    faq=[
      ('Am nevoie de telecomandă ca să asociez telefonul?', 'Nu. Codul apare pe ecranul televizorului, iar tu îl scrii pe telefon. Trebuie doar să pornești televizorul, la nevoie cu butonul de pe aparat.'),
      ('Funcționează cu un Hisense?', 'La televizoarele Hisense cu Android TV sau Google TV, da. Televizoarele Hisense cu alt sistem nu sunt compatibile.'),
      ('Pot scrie cu tastatura telefonului?', 'Da. Tastatura este gratuită și funcționează pentru căutarea în YouTube, Netflix și celelalte aplicații.'),
    ]),
  dict(clave='lg-on', corto='Pornește televizorul LG cu telefonul',
    titulo='Pornește televizorul LG cu telefonul (ghid)',
    desc='Pornește televizorul LG cu telefonul prin Wi-Fi: activează „Pornire TV de pe dispozitiv mobil” și folosește Mando TV. Pas cu pas, gratis.',
    h1='Cum pornești un televizor LG cu telefonul',
    intro='Poți porni un televizor LG cu telefonul, dar mai întâi trebuie să activezi o setare pe televizor. După aceea, telefonul pornește televizorul LG prin Wi-Fi-ul tău, fără telecomandă. Durează cinci minute și o faci o singură dată.',
    pasos=[
      'Conectează telefonul și televizorul LG la același Wi-Fi.',
      'Pe televizor, deschide setările și caută „Pornire TV de pe dispozitiv mobil”. O găsești la Setări > General > Dispozitive > Dispozitive externe (la modelele mai vechi: Conexiune > Gestionare conexiune mobilă).',
      'Activează „Pornire prin Wi-Fi”. Dacă televizorul tău este legat prin cablu de rețea, activează în schimb opțiunea pentru cablu.',
      'Dacă televizorul are „Quick Start+”, activează-l și pe acesta.',
      'Cu televizorul pornit, deschide Mando TV pe telefon și atinge în listă televizorul tău LG. Confirmă fereastra care apare pe ecran. Așa învață aplicația să îl trezească.',
      'Oprește televizorul și încearcă: atinge televizorul în Mando TV, iar aplicația te întreabă dacă vrei să îl pornească.',
    ],
    extra=[
      ('Dacă nu pornește', 'Televizorul trebuie să fi fost în același Wi-Fi când a fost oprit. Verifică dacă setarea este încă activă și dacă telefonul este în aceeași rețea. Dacă ai schimbat routerul, conectează-te din nou cu televizorul pornit.'),
    ],
    marca='lg',
    faq=[
      ('Pot porni televizorul LG cu telefonul dacă nu l-am conectat niciodată?', 'Nu. Mai întâi trebuie să activezi pe televizor „Pornire TV de pe dispozitiv mobil” și să te conectezi o dată cu Mando TV cât timp televizorul este pornit.'),
      ('Am nevoie de aplicația LG ThinQ?', 'Nu. Mando TV se conectează direct prin Wi-Fi-ul tău și nu cere cont LG.'),
      ('Funcționează cu date mobile?', 'Nu. Telefonul și televizorul trebuie să fie în același Wi-Fi.'),
    ]),
  dict(clave='console', corto='Televizor și consolă fără telecomandă',
    titulo='Fără telecomandă? Pornește televizorul, schimbă HDMI',
    desc='Ziua lansării și nu ai telecomandă? Pornește televizorul și treci cu telefonul pe intrarea HDMI a PS5 sau Xbox. Gratis, fără reclame.',
    h1='Cum pornești televizorul și treci fără telecomandă pe intrarea HDMI a consolei',
    intro='Ziua lansării GTA VI, consola este gata, iar telecomanda a dispărut pe undeva printre pernele canapelei. Se întâmplă mai des decât crezi. Cu Mando TV, telefonul tău pornește televizorul și trece, prin Wi-Fi-ul de acasă, pe intrarea PlayStation sau Xbox.',
    pasos=[
      'Conectează telefonul la același Wi-Fi ca televizorul.',
      'Deschide Mando TV și atinge în listă televizorul tău (Samsung, LG, Roku sau Android TV).',
      'Dacă televizorul este oprit, atinge Pornește. Merge dacă pe televizor este activată pornirea prin rețea. Dacă nu ai activat-o niciodată, pornește televizorul cu butonul de pe aparat doar de data aceasta și activeaz-o pentru data viitoare.',
      'Pornește consola. Dacă HDMI-CEC este activat (vezi mai jos trucul gratuit), televizorul trece singur pe intrarea ei.',
      'Dacă nu trece, atinge în Mando TV Intrări și alege portul HDMI în care este băgată consola: HDMI 1, HDMI 2 și așa mai departe.',
      'Pentru volum, în timpul jocului folosește butoanele mari din aplicație.',
    ],
    extra=[
      ('Trucul gratuit: lasă consola să schimbe televizorul', 'PS5 și Xbox pot porni televizorul și pot sări chiar de la pornire pe intrarea lor HDMI, datorită HDMI-CEC. La PS5 îl găsești la Setări > Sistem > HDMI > Activează legătura dispozitivelor HDMI. La Xbox, deschide Setări > General > Opțiuni TV și afișare și caută opțiunea pentru controlul dispozitivelor. Pe televizor, funcția se numește diferit în funcție de marcă: Anynet+ la Samsung, SIMPLINK la LG și BRAVIA Sync sau Control HDMI la altele.'),
      ('Dacă televizorul rămâne pe altă imagine', 'Dacă consola este pornită, dar televizorul arată încă antena sau o aplicație, nu a schimbat intrarea. Atinge pe telefon Intrări și alege intrarea HDMI a consolei. Sau folosește săgețile și OK ca să ajungi la intrările televizorului ori butonul de pe televizor și alege portul HDMI. Numărul este portul în care ai băgat cablul consolei.'),
      ('Dacă este un Roku TV', 'Butonul de pe televizor, de obicei jos la mijloc sau în spate, îl pornește. De acolo, telefonul se ocupă de restul.'),
    ],
    marca=None,
    faq=[
      ('Are Mando TV vreo legătură cu GTA VI?', 'Nu. Mando TV nu are nicio legătură cu Rockstar Games sau Take-Two. Aplicația doar te ajută să nu pierzi timp de joc pentru că nu găsești telecomanda.'),
      ('Este gratuită schimbarea intrării HDMI?', 'Da. Lista de intrări din Mando TV este gratuită, ca și pornirea televizorului, săgețile, OK și volumul. Poți lăsa și consola să schimbe singură intrarea prin HDMI-CEC.'),
      ('Funcționează cu televizorul meu?', 'Funcționează cu televizoare Samsung, LG, Roku și Android TV din același Wi-Fi. Dacă al tău este de altă marcă, trucul HDMI-CEC te poate ajuta oricum.'),
      ('Îl pot folosi ca să joc GTA VI (GTA 6) pe PS5 sau Xbox?', 'Mando TV nu intervine nici în consolă, nici în joc. Doar se asigură că televizorul este pornit și pe intrarea HDMI potrivită, ca să te poți așeza și juca.'),
    ]),
  dict(clave='samsung-lost', corto='Televizor Samsung fără telecomandă',
    titulo='Telecomandă Samsung pierdută? Folosește telefonul',
    desc='Telecomandă Samsung pierdută sau stricată? Folosește telefonul prin Wi-Fi ca telecomandă pentru televizoarele Tizen. Simplu cu Mando TV, gratis, fără reclame.',
    h1='Televizor Samsung fără telecomanda originală: folosește telefonul',
    intro='Dacă ți-ai pierdut telecomanda Samsung sau nu mai funcționează, poți folosi telefonul ca telecomandă prin Wi-Fi. Funcționează cu televizoare Samsung cu Tizen, fabricate în 2016 sau mai recent.',
    pasos=[
      'Pornește televizorul cu butonul de pe aparat. La majoritatea modelelor se află jos sau în spate, uneori ca un mic joystick.',
      'Verifică dacă televizorul este conectat la Wi-Fi-ul tău și dacă telefonul este în aceeași rețea.',
      'Deschide Mando TV pe telefon. Televizorul tău Samsung apare singur în listă. Atinge-l.',
      'Televizorul îți cere să confirmi conexiunea. La majoritatea modelelor o confirmi cu butoanele de pe televizor sau cu joystickul din spate.',
      'Gata, acum poți folosi telefonul ca telecomandă. Butoanele, tastatura și aplicațiile sunt gratuite; touchpadul este o funcție Pro.',
      'Ca să pornești televizorul de pe telefon data viitoare, mergi la Setări > General > Rețea > Setări expert și activează „Pornire cu dispozitiv mobil”.',
    ],
    extra=[
      ('Dacă televizorul nu cere permisiunea', 'Poate permisiunea este deja salvată sau televizorul este în alt Wi-Fi. Închide Mando TV și deschide din nou aplicația cu televizorul pornit. Dacă televizorul este mai vechi de 2016, folosește alt sistem, care încă nu este acceptat.'),
      ('Dacă ai refuzat permisiunea din greșeală', 'Pe televizor, mergi la Setări > General > Manager dispozitive externe > Manager conexiuni dispozitive și setează Mando TV ca permis. Dacă telefonul tot nu găsește televizorul, citește [Telefonul nu găsește televizorul](@not-found).'),
    ],
    marca='samsung',
    faq=[
      ('Cum confirm conexiunea dacă nu am telecomandă?', 'La majoritatea modelelor o confirmi cu butoanele de pe televizor sau cu joystickul din spate. Dacă modelul tău nu are butoane, scrie la hola@mandotv.app și te ajutăm.'),
      ('Cere Mando TV cont Samsung?', 'Nu. Conexiunea merge direct prin Wi-Fi-ul tău, fără cont Samsung.'),
      ('Funcționează cu televizorul meu Samsung mai vechi?', 'Funcționează cu televizoare Samsung cu Tizen, fabricate în 2016 sau mai recent.'),
    ]),
  dict(clave='wifi', corto='Telefon ca telecomandă prin Wi-Fi',
    titulo='Folosește telefonul ca telecomandă: controlează televizorul prin Wi-Fi',
    desc='Conectează telefonul prin Wi-Fi la televizor și folosește-l ca telecomandă la Samsung, LG, Roku și Google TV. Pași pentru fiecare marcă cu Mando TV. Gratis.',
    h1='Cum conectezi telefonul prin Wi-Fi la televizor, ca telecomandă',
    intro='Ai nevoie doar de telefon și de televizor în același Wi-Fi, plus o aplicație de telecomandă. Mando TV îți găsește singură televizorul și funcționează cu Samsung, LG, Roku, Google TV și Android TV.',
    pasos=[
      'Conectează telefonul și televizorul la același Wi-Fi.',
      'Deschide Mando TV. Televizorul tău apare singur în listă. Atinge-l.',
      'Confirmă conexiunea pentru marca ta (detaliile sunt mai jos).',
      'Controlează televizorul cu butoanele sau cu tastatura telefonului. Touchpadul este o funcție Pro.',
    ],
    extra=[
      ('Samsung', 'Televizorul te întreabă dacă permiți conexiunea. Confirm-o prima dată pe ecran. Funcționează cu Tizen, fabricat în 2016 sau mai recent. Ca să îl pornești de pe telefon, activează la Setări > General > Rețea > Setări expert opțiunea „Pornire cu dispozitiv mobil”.'),
      ('LG', 'Televizorul afișează o fereastră care cere permisiunea. Confirm-o prima dată. Ca să îl pornești de pe telefon, caută în setări „Pornire TV de pe dispozitiv mobil” și activează „Pornire prin Wi-Fi”.'),
      ('Roku', 'Roku nu cere asociere: atinge-l în listă și ești conectat. Ca să îl pornești, activează la Setări > Sistem > Alimentare opțiunea „Pornire rapidă TV”.'),
      ('Google TV și Android TV', 'Televizorul afișează un cod pe ecran. Introdu-l prima dată în Mando TV. Ca să îl pornești, caută în setări „Wake on LAN”, „Pornire prin rețea” sau „Standby în rețea”.'),
    ],
    marca=None,
    faq=[
      ('Am nevoie de internet ca să folosesc telefonul ca telecomandă?', 'Ai nevoie de telefon și de televizor în același Wi-Fi. Mando TV se conectează direct la televizorul tău prin această rețea.'),
      ('De ce nu apare televizorul meu în listă?', 'Verifică dacă televizorul este pornit și dacă telefonul nu folosește date mobile sau alt Wi-Fi. Unele routere au o rețea pentru oaspeți care separă dispozitivele între ele.'),
      ('Pot folosi Mando TV pe iPhone sau pe un telefon Android?', 'Pe iPhone și iPad, da: aplicația este deja în App Store. Pentru Windows este și în Microsoft Store. Android vine în curând: poți participa la accesul anticipat gratuit de pe Google Play.'),
    ]),
  dict(clave='pc', corto='Controlează televizorul de pe PC',
    titulo='Controlează televizorul cu PC-ul cu Windows (gratis)',
    desc='Folosește PC-ul cu Windows ca telecomandă pentru Samsung, LG, Roku sau Google TV prin Wi-Fi. Butoane, tastatură și aplicații gratis; scurtături de PC cu Pro.',
    h1='Cum controlezi televizorul cu un PC cu Windows',
    intro='Dacă îți petreci ziua în fața computerului, nu trebuie să cauți telecomanda: Mando TV pentru Windows îți controlează televizorul Samsung, LG, Roku, Google TV sau Android TV prin Wi-Fi-ul de acasă. Foarte util ca să schimbi aplicațiile, să dai volumul mai tare sau să scrii în YouTube cu tastatura PC-ului.',
    pasos=[
      'Descarcă gratuit Mando TV din Microsoft Store pe computerul tău cu Windows 10 sau 11.',
      'Verifică dacă computerul și televizorul sunt în aceeași rețea (Wi-Fi sau cablu, dar prin același router).',
      'Deschide Mando TV: televizorul tău apare singur în listă. Atinge-l sau fă clic pe el.',
      'Prima dată, confirmă conexiunea pe ecranul televizorului (la Google TV și Android TV introduci codul afișat de televizor).',
      'Gata: folosește butoanele sau tastatura ca să scrii în câmpul de căutare al televizorului. Touchpadul este o funcție Pro.',
    ],
    extra=[
      ('Scurtături de tastatură pe PC (Pro)', 'Cu Mando TV Pro controlezi televizorul cu tastatura computerului: săgeți pentru navigare, Enter pentru OK, Backspace sau Esc pentru Înapoi, + și - pentru volum, M pentru mut și bara de spațiu pentru pauză.'),
      ('Mini-telecomandă mereu deasupra (Pro)', 'Ține o fereastră mică cu telecomanda mereu vizibilă cât timp lucrezi sau joci pe PC.'),
      ('Vorbește cu televizorul de pe PC (Pro)', 'Cu Mando TV Pro dai comenzi televizorului prin microfonul PC-ului: „deschide YouTube”, „dă mai tare” sau „oprește în 30 de minute”, exact cum vorbești. Pe Windows, vocea este recunoscută chiar pe PC: nu ai nevoie de internet, nu trebuie să schimbi nimic în setările Windows și funcționează în cele 6 limbi ale aplicației. Ce spui nu părăsește PC-ul și nu este salvat. Doar la procesoarele foarte vechi aplicația folosește dictarea din Windows. Pentru asta trebuie să fie activată recunoașterea vocală online în setările de confidențialitate și să fie adăugată româna (România) în Windows. Dacă lipsește ceva, aplicația îți spune și deschide setarea cu un buton.'),
    ],
    marca=None,
    faq=[
      ('Am nevoie de cablu sau de Bluetooth ca să controlez televizorul cu PC-ul?', 'Nu. Mando TV se conectează prin rețeaua ta de acasă: PC-ul și televizorul trebuie doar să fie la același router.'),
      ('Funcționează cu orice televizor?', 'Funcționează cu televizoare Samsung cu Tizen (fabricate în 2016 sau mai recent), LG cu webOS, Roku, precum și Google TV sau Android TV (Sony, Philips, TCL, Hisense, Sharp, Xiaomi, Toshiba, Panasonic, Haier, Skyworth și altele).'),
      ('Cât costă?', 'Butoanele, tastatura și pornirea prin rețea sunt gratuite și fără reclame. Mando TV Pro este o achiziție unică, fără abonament, pentru extra precum touchpadul, scurtăturile de PC și mini-telecomanda.'),
      ('De ce nu mă înțelege microfonul pe Windows?', 'Verifică dacă funcția de voce este activă (face parte din Pro) și dacă microfonul PC-ului funcționează în Windows. Pe aproape toate PC-urile, vocea este recunoscută chiar pe dispozitiv, fără internet. Doar la procesoarele foarte vechi aplicația folosește dictarea din Windows. Verifică atunci dacă recunoașterea vocală online este activată în setările de confidențialitate din Windows și dacă Windows are româna (România) la setările de limbă. Mando TV folosește această limbă doar cât timp ascultă.'),
    ]),
  dict(clave='roku-403', corto='Aplicația Roku nu funcționează',
    titulo='Aplicația Roku nu funcționează? Rezolvă eroarea 403',
    desc='Telefon conectat, dar Roku nu reacționează? Activează „Control prin aplicații mobile” în 5 pași și folosește din nou telefonul ca telecomandă.',
    h1='Aplicația Roku nu funcționează: cum rezolvi problema',
    intro='Dacă telefonul găsește Roku-ul și se conectează, dar niciun buton nu face nimic, aproape întotdeauna este vorba de o setare a Roku-ului care blochează aplicațiile de telecomandă. Versiunile mai noi de Roku sunt implicit mai restrictive. Din meniul Roku se rezolvă într-un minut.',
    pasos=[
      'Apasă pe Roku Acasă și mergi la Setări.',
      'Deschide Sistem, apoi Setări avansate de sistem.',
      'Mergi la „Control prin aplicații mobile”. La unele modele se numește „Control extern”.',
      'La „Acces la rețea” alege Implicit sau Permisiv. Dacă la modelul tău este doar un comutator, lasă-l pe Activat.',
      'Întoarce-te în Mando TV pe telefon și atinge Roku-ul tău. Butoanele reacționează acum.',
    ],
    extra=[
      ('Cum îți dai seama dacă asta este problema ta', 'Semnul este clar: telefonul vede Roku-ul în listă și se conectează, dar nu se întâmplă nimic când atingi un buton. Intern, Roku răspunde cu eroarea 403, adică „interzis”. Mando TV detectează asta la conectare și îți arată chiar acești pași pe ecran.'),
      ('Implicit sau Permisiv, ce aleg?', 'Implicit este suficient: acceptă comenzile care vin din rețeaua ta de acasă, iar o telecomandă are nevoie doar de asta. Permisiv este mai deschis și este necesar doar în rețele neobișnuite.'),
      ('Dacă nu ai telecomanda Roku', 'Dacă setarea este pe Dezactivat, poate fi schimbată doar cu telecomanda Roku adevărată. Împrumut-o pe una ca să o schimbi o singură dată; după aceea poți face totul cu telefonul. Citește și [Telecomandă Roku pierdută](@roku-lost).'),
    ],
    marca='roku',
    faq=[
      ('De ce nu mai reacționează Roku-ul meu, deși înainte mergea?', 'O actualizare Roku poate restricționa mai mult această setare. Nu este vina telefonului sau a Wi-Fi-ului tău: trebuie doar să permiți din nou controlul prin aplicații.'),
      ('Se aplică la Roku TV și la playerele Roku?', 'Da. Setarea se află în același meniu la playerele Roku și la televizoarele Roku TV.'),
      ('Este sigur să las setarea pe Implicit?', 'Da. Acceptă doar comenzi de la dispozitive din rețeaua ta de acasă.'),
    ]),
  dict(clave='not-found', corto='Telefonul nu găsește televizorul',
    titulo='Telefonul nu găsește televizorul? 6 lucruri de verificat',
    desc='Aplicația de telecomandă nu găsește televizorul? Verifică Wi-Fi-ul, VPN-ul și accesul la rețeaua locală. Pentru Samsung, LG, Roku și Android TV.',
    h1='Telefonul nu găsește televizorul: ce să verifici',
    intro='Deschizi aplicația de telecomandă și lista este goală, sau televizorul apare, dar conexiunea se întrerupe. Aproape întotdeauna este vorba de rețea, nu de televizor. Verifică punctele acestea pe rând: primul rezolvă majoritatea cazurilor.',
    pasos=[
      'Uită-te în ce Wi-Fi este telefonul și în ce Wi-Fi este televizorul. Trebuie să fie aceeași rețea, cu același nume. O rețea pentru oaspeți nu merge, pentru că separă dispozitivele între ele.',
      'Oprește VPN-ul de pe telefon, dacă folosești unul. Cu VPN activ, telefonul iese pe internet printr-o altă rețea și nu vede dispozitivele de acasă, sau conexiunea se întrerupe după câteva secunde.',
      'Oprește pentru scurt timp datele mobile. Unele telefoane trec singure de la Wi-Fi la date mobile când semnalul este slab.',
      'Pornește televizorul și așteaptă să termine de pornit. Un televizor oprit nu răspunde la căutare.',
      'Pe iPhone, verifică dacă aplicația are permisiunea „Rețea locală”: Setări > Confidențialitate și securitate > Rețea locală.',
      'Dacă tot nu apare, adaugă-l manual: în Mando TV atinge „Adaugă după IP” și introdu adresa IP a televizorului.',
    ],
    extra=[
      ('Lasă aplicația să te ghideze', 'În lista de televizoare există un buton pentru cazul în care televizorul tău nu apare. Aplicația verifică pe rând cele mai frecvente cauze (același Wi-Fi, VPN, permisiunea pentru rețeaua locală și altele) și arată după fiecare corectare un buton de reverificare. Asistentul este gratuit.'),
      ('Unde găsești adresa IP a televizorului', 'O găsești în meniul de rețea al televizorului și diferă puțin în funcție de model. La LG: Setări, Rețea, Conexiune Wi-Fi, Setări Wi-Fi avansate. La Samsung: Setări, General, Rețea, Stare rețea, Setări IP. La Roku: Setări, Rețea, Despre. La Android TV și Google TV: Setări, Rețea și internet, apoi atingi rețeaua ta. Este un număr de felul 192.168.1.86.'),
      ('Dacă apare, dar conexiunea se întrerupe', 'Dacă conexiunea se întrerupe după câteva secunde, cauza este de obicei la telefon: un VPN, trecerea într-un alt Wi-Fi sau modul de economisire a energiei. Oprește VPN-ul, rămâi în același Wi-Fi și încearcă din nou.'),
      ('Wi-Fi de 2,4 și 5 GHz', 'Nu contează dacă telefonul este în rețeaua de 5 GHz și televizorul în cea de 2,4 GHz, atât timp cât ambele vin de la același router. Dacă ai un repetor Wi-Fi și televizorul tot nu apare, apropie-te cu telefonul de routerul principal și încearcă din nou.'),
    ],
    marca=None,
    faq=[
      ('Pot controla televizorul cu date mobile?', 'Nu. Semnalul telecomenzii merge prin Wi-Fi-ul tău de acasă, de aceea telefonul și televizorul trebuie să fie în aceeași rețea.'),
      ('De ce nu merge cu VPN activ?', 'Pentru că VPN-ul trimite tot traficul telefonului printr-o altă rețea, iar telefonul nu mai vede dispozitivele de acasă. Oprește-l cât timp folosești telecomanda.'),
      ('Funcționează cu Bluetooth sau cu infraroșu?', 'La Smart TV-uri, Mando TV folosește Wi-Fi-ul. Infraroșul funcționează doar pe telefoane Android cu emițător de infraroșu și este pentru televizoarele care nu sunt Smart TV. Bluetooth există în versiunea beta, gratuit și doar de la Android 9: telefonul se conectează la televizor ca tastatură și telecomandă Bluetooth, fără Wi-Fi. Funcționează cu Google TV, Android TV și Fire TV; la alte mărci care acceptă tastaturi Bluetooth poate funcționa, Roku nu le acceptă.'),
    ]),
  dict(clave='androidtv-code', corto='Cod de asociere Android TV',
    titulo='Android TV cere un cod de asociere: ce ai de făcut',
    desc='Android TV sau Google TV afișează la conectare un cod de 6 caractere. Iată cum îl introduci și ce faci dacă nu apare sau este greșit.',
    h1='Android TV cere un cod de asociere: ce ai de făcut',
    intro='Când conectezi pentru prima dată telefonul la un Android TV sau Google TV, televizorul afișează pe ecran un cod de 6 caractere. Este normal și se întâmplă o singură dată: așa te asiguri că nimeni altcineva nu îți poate controla televizorul. Iată cum îl introduci și ce faci dacă nu apare.',
    pasos=[
      'Pornește televizorul și lasă ecranul de start vizibil.',
      'Deschide Mando TV pe telefon, în același Wi-Fi ca televizorul, și atinge în listă televizorul tău.',
      'Uită-te la ecranul televizorului: apare un cod format din 6 litere și cifre.',
      'Scrie-l pe telefon exact cum apare și atinge Asociază. Literele merg doar de la A la F, deci un caracter rotund este întotdeauna cifra zero.',
      'Gata. Televizorul își amintește telefonul tău și nu mai cere codul.',
    ],
    extra=[
      ('Dacă codul nu apare pe televizor', 'Verifică dacă televizorul este cu adevărat pornit și nu în standby și dacă telefonul este în același Wi-Fi. Atinge din nou televizorul pe telefon. Dacă tot nu apare, repornește televizorul: scoate ștecherul zece secunde, bagă-l la loc și încearcă din nou.'),
      ('Dacă codul este declarat greșit', 'Codul se schimbă la fiecare cerere. Dacă ți-a luat mult timp sau l-ai cerut de două ori, funcționează doar ultimul de pe ecran. Atinge din nou televizorul pe telefon și introdu codul nou.'),
      ('Dacă televizorul cere din nou codul', 'Se întâmplă dacă televizorul a fost resetat la setările din fabrică sau dacă ștergi datele aplicației de pe telefon. Asociază din nou și rămâne salvat. Dacă nu ai deloc telecomandă, citește [Android TV fără telecomandă](@androidtv).'),
    ],
    marca='android',
    faq=[
      ('Ce televizoare folosesc acest cod?', 'Cele cu Android TV sau Google TV: Sony, Philips, TCL, Hisense, Sharp, Xiaomi, Chromecast cu Google TV și altele.'),
      ('Am nevoie de cont Google pe telefon?', 'Nu. Codul de pe ecran este tot ce îți trebuie.'),
      ('Este sigur?', 'Da. Codul dovedește că ești în fața televizorului: nimeni nu poate asocia fără să vadă codul de pe ecran.'),
    ]),
  dict(clave='roku-lost', corto='Telecomandă Roku pierdută',
    titulo='Telecomandă Roku pierdută? Folosește telefonul prin Wi-Fi',
    desc='Telecomandă Roku pierdută? Telefonul o înlocuiește prin Wi-Fi. Pași simpli, chiar dacă ai schimbat routerul și Roku nu are Wi-Fi.',
    h1='Telecomandă Roku pierdută: folosește telefonul',
    intro='Dacă ți-ai pierdut telecomanda Roku sau nu mai funcționează, telefonul o înlocuiește, atât timp cât Roku este încă conectat la Wi-Fi-ul tău. Iar dacă ai schimbat Wi-Fi-ul sau routerul, există o soluție și pentru asta.',
    pasos=[
      'Încearcă mai întâi să faci telecomanda să sune. Dacă telecomanda ta Roku are difuzor, de exemplu Roku Voice Remote Pro, deschide Mando TV, conectează-te la Roku și folosește opțiunea de a face telecomanda să sune, ca să o găsești. Merge doar cu telecomenzile Roku cu difuzor, iar Roku trebuie să fie pornit.',
      'Pornește televizorul și lasă Roku conectat. Nu trebuie să te atingi de el.',
      'Conectează telefonul la același Wi-Fi pe care îl folosește Roku.',
      'Deschide Mando TV. Roku apare singur în listă. Atinge-l.',
      'Folosește săgețile, OK, Acasă și Înapoi ca la telecomanda obișnuită. Roku nu cere niciun cod.',
      'Dacă butoanele nu fac nimic, Roku blochează controlul prin aplicații: ghidul [Aplicația Roku nu funcționează](@roku-403) explică cum îl permiți.',
    ],
    extra=[
      ('Dacă Roku nu are Wi-Fi (ai schimbat routerul sau te-ai mutat)', 'Fără telecomandă nu poți ajunge în meniu ca să configurezi rețeaua nouă, dar există un truc: Roku se conectează singur la o rețea care are același nume și aceeași parolă ca cea veche. Creează pe alt telefon un hotspot Wi-Fi cu exact acest nume și această parolă, conectează telefonul cu Mando TV la el și Roku apare în listă. De acolo mergi la Setări, Rețea și conectează-l la Wi-Fi-ul nou.'),
      ('Dacă este un Roku TV', 'Televizoarele Roku TV au un buton pe aparat, aproape întotdeauna jos la mijloc sau în spate, care pornește televizorul. Ajunge ca să îl pornești și să continui cu telefonul.'),
      ('Dacă preferi să cumperi altă telecomandă', 'Ai grijă să fie potrivită pentru modelul tău. Micile playere Roku aflate în spatele televizorului au nevoie de o telecomandă fără infraroșu, pentru că infraroșul nu ajunge la ele.'),
    ],
    marca='roku',
    faq=[
      ('Poate telefonul meu să pornească Roku?', 'Un player Roku conectat este mereu pornit. La un Roku TV, Mando TV îl pornește prin Wi-Fi dacă „Pornire rapidă TV” este activată la Setări > Sistem > Alimentare.'),
      ('Dar volumul?', 'La un Roku TV, telefonul dă volumul mai tare și mai încet. La un player Roku conectat prin HDMI, depinde de televizor: la multe merge, la altele nu.'),
      ('Trebuie să îmi fac un cont?', 'Nu. Mando TV nu cere cont și controlează, în plus, televizoare Samsung, LG și Android TV cu aceeași aplicație.'),
    ]),
]

SOPORTE = dict(
  titulo='Ajutor: conectează și pornește televizorul cu Mando TV',
  desc='Cum conectezi telecomanda Mando TV la LG, Samsung, Roku sau Android TV, cum pornești televizorul de pe telefon și cum rezolvi problemele.',
  h1='Ajutor',
  intro='Cele mai frecvente întrebări, în ordinea pașilor. Dacă nu o găsești pe a ta, scrie-ne la <a href="mailto:hola@mandotv.app?subject=Ajutor%20Mando%20TV">hola@mandotv.app</a> și îți răspundem.',
)
SOPORTE_HTML = '''      <h2 id="encontrar">Găsirea televizorului</h2>
      <div class="preguntas">
        <details open><summary>Televizorul meu nu apare în listă</summary>
          <ol>
            <li>Verifică dacă telefonul și televizorul sunt în același Wi-Fi. Dacă routerul tău are o rețea de 2,4 GHz și una de 5 GHz cu nume diferite, uneori nu se văd între ele.</li>
            <li>Asigură-te că televizorul este pornit.</li>
            <li>Pe iPhone, verifică dacă Mando TV are permisiunea „Rețea locală”, la Setări, Mando TV.</li>
            <li>În lista de televizoare, atinge butonul pentru cazul în care televizorul tău nu apare: aplicația verifică pe rând cele mai frecvente cauze (același Wi-Fi, VPN, permisiunea pentru rețeaua locală și altele) și arată după fiecare corectare un buton de reverificare.</li>
            <li>Dacă tot nu apare, atinge butonul +, alege marca și introdu adresa IP a televizorului. O vezi în meniul de rețea al televizorului (de exemplu 192.168.1.50).</li>
          </ol>
        </details>
        <details><summary>Funcționează cu date mobile sau de la distanță?</summary>
          <p>Nu. Mando TV vorbește cu televizorul în interiorul rețelei tale de acasă, deci telefonul trebuie să fie conectat la acel Wi-Fi.</p>
        </details>
      </div>

      <h2 id="conectar">Prima conectare</h2>
      <p>Ghiduri complete în funcție de marcă: <a href="@@R_lg@@">LG</a>, <a href="@@R_samsung@@">Samsung</a>, <a href="@@R_roku@@">Roku</a> și <a href="@@R_android@@">Android TV</a>.</p>
      <div class="preguntas">
        <details><summary>LG</summary>
          <p>Când atingi televizorul, pe ecran apare o fereastră care cere permisiunea. Confirm-o cu telecomanda obișnuită. O faci o singură dată.</p>
        </details>
        <details><summary>Samsung</summary>
          <p>Televizorul te întreabă dacă permiți conexiunea Mando TV. Alege cu telecomanda „Permite”. Dacă ai refuzat-o din greșeală, mergi la Setări > General > Manager dispozitive externe > Manager conexiuni dispozitive și schimb-o pe permis.</p>
        </details>
        <details><summary>Roku</summary>
          <p>Roku nu cere permisiune. Dacă nu se conectează, mergi pe Roku la Setări > Sistem > Setări avansate de sistem > Control prin aplicații mobile și lasă accesul la rețea pe Implicit sau Permisiv (la software-ul Roku mai nou, setează „Control prin aplicații mobile” pe Activat).</p>
        </details>
        <details><summary>Android TV și Google TV</summary>
          <p>Televizorul afișează un cod de 6 caractere. Introdu-l în Mando TV exact cum apare. Funcționează la Sony, Philips, TCL, Hisense, Sharp, Xiaomi, Chromecast cu Google TV și altele cu Android TV.</p>
        </details>
      </div>

      <h2 id="encender">Pornirea televizorului din aplicație</h2>
      <p>Mando TV pornește televizorul prin rețeaua ta de acasă. Pentru asta sunt necesare două lucruri: te-ai conectat cel puțin o dată cu televizorul pornit, iar pe televizor este activată pornirea prin rețea. Numele setării se schimbă în funcție de model; acestea sunt cele mai frecvente:</p>
      <div class="preguntas">
        <details><summary>LG</summary>
          <p>Caută „Pornire TV de pe dispozitiv mobil” (sau „Pornire prin Wi-Fi”) la Setări > General > Dispozitive > Dispozitive externe (la modelele mai vechi: Conexiune > Gestionare conexiune mobilă) și activeaz-o.</p>
        </details>
        <details><summary>Samsung</summary>
          <p>Activează „Pornire cu dispozitiv mobil” la Setări > General > Rețea > Setări expert.</p>
        </details>
        <details><summary>Roku</summary>
          <p>La televizoarele Roku TV, activează „Pornire rapidă TV” la Setări > Sistem > Alimentare. Playerele Roku conectate la un televizor nu pot fi pornite astfel.</p>
        </details>
        <details><summary>Android TV și Google TV</summary>
          <p>Depinde de producător. Caută în setările de rețea sau de alimentare „Wake on LAN”, „Pornire prin rețea”, „Standby în rețea” sau „Remote start”. Unele modele nu au această opțiune.</p>
        </details>
      </div>

      <h2 id="falla">Când ceva nu merge</h2>
      <div class="preguntas">
        <details><summary>Conexiunea se întrerupe sau nu primesc niciun răspuns</summary>
          <ol>
            <li>Pe ecranul telecomenzii, atinge Reconectează.</li>
            <li>Dacă nu ajută, închide Mando TV și deschide din nou aplicația.</li>
            <li>Dacă televizorul a primit altă adresă IP, scoate-l din listă și adaugă-l din nou.</li>
          </ol>
        </details>
        <details><summary>Cum ne trimiți un raport de eroare</summary>
          <ol>
            <li>În Mando TV, atinge butonul Personalizează (cursoarele de sus).</li>
            <li>Atinge Copiază raportul de test.</li>
            <li>Lipește-l, împreună cu marca și modelul televizorului tău, într-un e-mail către hola@mandotv.app.</li>
          </ol>
          <p>Raportul nu conține parole, coduri și nimic din ce scrii tu.</p>
        </details>
        <details><summary>Am cumpărat Pro și nu apare</summary>
          <p>Atinge la Personalizează Restabilește achiziția, cu același cont de magazin cu care ai cumpărat. Dacă tot nu apare, scrie-ne.</p>
        </details>
      </div>

      <h2 id="guias">Ghiduri pas cu pas</h2>
      <p><a href="@@R_guias@@">Vezi toate ghidurile</a></p>
      <ul>
@@GUIAS@@
      </ul>

      <h2 id="contacto">Mai ai întrebări?</h2>
      <p>Scrie-ne la <a href="mailto:hola@mandotv.app?subject=Ajutor%20Mando%20TV">hola@mandotv.app</a>. Spune-ne marca și modelul televizorului tău și la ce pas ai rămas. Scrie-ne în limba ta. Răspundem în spaniolă sau engleză și, dacă dorești, în limba ta, cu ajutorul unui traducător.</p>
'''

PRIVACIDAD = dict(
  titulo='Politica de confidențialitate | Mando TV',
  desc='Mando TV nu colectează date personale: fără conturi, fără reclame, fără trackere. Aplicația vorbește doar cu televizorul tău, în interiorul Wi-Fi-ului tău.',
  h1='Confidențialitate',
  intro='Pe scurt: Mando TV nu îți colectează datele. Nu există conturi, reclame, trackere și nici servere proprii care să păstreze ce faci.',
)
PRIVACIDAD_HTML = '''      <p class="fecha">În vigoare din 14 noiembrie 2026. Ultima actualizare: 26 noiembrie 2026.</p>

      <h2>Cine suntem</h2>
      <p>Mando TV este o aplicație cu care îți controlezi televizorul de pe telefon sau de pe computer. Această politică descrie ce informații folosește aplicația și ce face cu ele. Dacă ai întrebări, scrie-ne la <a href="mailto:hola@mandotv.app">hola@mandotv.app</a>.</p>

      <h2>Ce date colectăm</h2>
      <p>Aplicația: niciuna. Aplicația nu trimite nici nouă, nici unor terți informații despre tine sau despre cum o folosești. Nu folosește instrumente de analiză, de publicitate sau de urmărire.</p>
      <p>Acest site: măsurăm vizitele în două moduri, explicate în secțiunea <a href="#cookies">Cookie-uri pe acest site</a>.</p>

      <h2>Ce păstrează aplicația pe dispozitivul tău</h2>
      <p>Pentru a funcționa, aplicația păstrează următoarele doar pe telefonul sau computerul tău:</p>
      <ul>
        <li>Televizoarele pe care le-ai adăugat: nume, marcă, adresa IP din rețeaua ta și adresa hardware a plăcii de rețea (MAC), folosită pentru pornire.</li>
        <li>Cheile de conectare pe care le dă fiecare televizor când confirmi permisiunea. Sunt păstrate criptat în spațiul securizat al sistemului (Keychain pe iPhone și Mac, Keystore pe Android, spațiu protejat pe Windows).</li>
        <li>Setările tale: tema deschisă sau întunecată, culoarea de fundal, vibrația și tipul de telecomandă.</li>
        <li>Dacă folosești funcțiile Pro: aplicațiile tale favorite, rutinele tale și ultimele tale căutări în YouTube (le poți șterge din aplicație).</li>
      </ul>
      <p>Dacă ștergi aplicația, toate acestea se șterg odată cu ea.</p>

      <h2>Cu cine vorbește aplicația</h2>
      <p>Cu televizoarele tale, în interiorul Wi-Fi-ului tău de acasă. Ca să le găsească, aplicația caută în rețeaua ta locală; de aceea, pe iPhone cere permisiunea „Rețea locală”. Textul pe care îl scrii cu tastatura aplicației merge direct la televizor și nu este păstrat.</p>
      <p>În plus, la deschidere aplicația descarcă un mic fișier public de pe acest site (mandotv.app/app/config.json), ca să afle dacă există o versiune nouă pe care ar trebui să o instalezi și ce funcții fac parte din Mando TV Pro. Este o descărcare, ca atunci când deschizi o pagină: aplicația nu trimite datele tale, televizoarele tale sau ceea ce faci. Indică doar versiunea aplicației și sistemul (de exemplu Android), ca să îți poată arăta mesajul potrivit. Dacă nu ai internet, aplicația continuă cu ultimul fișier descărcat; dacă trec mai mult de 30 de zile fără să-l poată descărca, aplicația îți cere să te conectezi puțin la internet.</p>

      <p>Când trimiți fotografii sau videoclipuri la televizor (o funcție Pro), televizorul descarcă doar fișierele pe care le alegi, direct de pe telefonul sau PC-ul tău, prin Wi-Fi-ul de acasă. Acestea nu trec nici prin internet, nici prin noi, aplicația nu vede celelalte fotografii ale tale, iar partajarea se încheie îndată ce închizi acel ecran.</p>
      <h2>Microfon și voce</h2>
      <p>Pe iPhone, Mac și Android, căutarea vocală folosește microfonul doar cât timp ții atins butonul de vorbit. Ce spui este transformat în text de recunoașterea vocală a sistemului tău: de Apple pe iPhone și Mac și de Google pe Android, conform propriilor lor politici de confidențialitate. Pe Windows, vocea este recunoscută chiar pe PC-ul tău și nu părăsește dispozitivul; doar la procesoarele foarte vechi aplicația folosește introducerea vocală din Windows, de la Microsoft, conform politicii lor de confidențialitate. Pe Windows, microfonul se deschide când deschizi panoul vocal și se închide când îl închizi sau după 30 de secunde fără folosire; cât timp nu vorbești, nu se înregistrează și nu se păstrează nimic. Mando TV nu înregistrează și nu păstrează sunetul, iar textul rezultat merge direct la televizorul tău, exact ca ceea ce scrii cu tastatura.</p>

      <h2>Acasă: dispozitive din Apple Home și Google Home</h2>
      <p>Când deschizi secțiunea Acasă (în testare), aplicația cere permisiunea de a vedea dispozitivele pe care le ai deja în aplicația Casă de la Apple (HomeKit) sau în Google Home. Cu această permisiune citește numele, camera și starea lor (pornit sau oprit, luminozitate, temperatură sau în ce punct al programului se află un electrocasnic), ca să le afișeze și să le trimită ce atingi. Totul se petrece între telefonul tău și sistemul Apple sau Google: Mando TV nu păstrează această listă, nu o trimite nici nouă, nici unor terți și nu o folosește pentru publicitate sau analiză. Pe Android, Google Home funcționează cu propriul tău cont Google, conform politicii de confidențialitate Google. Poți retrage permisiunea oricând: pe iPhone la Setări &gt; Confidențialitate și securitate &gt; HomeKit, pe Android în setările contului tău Google.</p>
      <p>Când atingi „Cum a mers Acasă la tine?”, se deschide aplicația ta de e-mail cu un mesaj către hola@mandotv.app care conține un rezumat tehnic: versiunea aplicației, sistemul și câte dispozitive de fiecare tip au apărut și dacă răspund. Nu include nume de dispozitive, de camere sau ale casei tale, iar mesajul se trimite doar dacă îl trimiți tu.</p>

      <h2>Raportul de test</h2>
      <p>Aplicația are un buton „Copiază raportul de test” care ne ajută să rezolvăm erori. Raportul rămâne doar în memoria aplicației cât timp este deschisă și nu este trimis niciodată singur: tu decizi dacă îl copiezi și îl dai mai departe. Nu conține chei de conectare, coduri de asociere și nimic din ce introduci; doar pașii pe care i-a făcut aplicația, precum căutările, conectările și erorile.</p>

      <h2 id="cookies">Cookie-uri pe acest site</h2>
      <p>Aceasta se aplică doar site-ului mandotv.app, nu aplicației.</p>
      <h3>Întotdeauna fără cookie-uri</h3>
      <p>Numărăm vizitele anonim cu Cloudflare Web Analytics: câte persoane vizitează site-ul, ce pagini citesc și din ce țară. Nu folosește cookie-uri, nu folosește adresa ta IP ca să te identifice și nu urmărește ce faci pe alte site-uri.</p>
      <h3>Cu cookie-uri, doar dacă accepți</h3>
      <p>Dacă atingi „Acceptă” în mesajul despre cookie-uri, activăm Google Analytics (de la Google LLC) ca să înțelegem mai bine cum este folosit site-ul: pagini vizualizate, timp petrecut, tipul de dispozitiv, orașul aproximativ și de unde vii. Pentru asta păstrează cookie-urile _ga și _ga_* până la 2 ani în browserul tău. Google poate prelucra aceste date pe servere din afara Chile. Am dezactivat funcțiile de publicitate și Google Signals și nu folosim aceste date ca să îți arătăm reclame.</p>
      <p>Dacă atingi „Refuză” sau nu alegi nimic, Google Analytics nu se încarcă și nu se păstrează niciun cookie. Poți schimba oricând decizia cu butonul „Cookie-uri” de la finalul fiecărei pagini; dacă retragi acordul, ștergem aceste cookie-uri.</p>
      <p>Alegerea ta este păstrată în browserul tău (stocare locală, netrimisă nimănui), ca să nu te mai întrebăm încă o dată.</p>

      <h2>Achiziții</h2>
      <p>Când cumperi Mando TV Pro, plata este procesată de magazinul de aplicații (App Store, Google Play sau Microsoft Store). Nu primim și nu păstrăm datele cardului tău. Magazinul confirmă aplicației doar că achiziția există.</p>

      <h2>E-mailurile pe care ni le trimiți</h2>
      <p>Dacă ne scrii la <a href="mailto:hola@mandotv.app">hola@mandotv.app</a>, folosim adresa ta de e-mail și ce ne spui doar ca să îți răspundem. Nu le dăm mai departe și nu le folosim pentru publicitate. Poți cere oricând să ștergem mesajele tale.</p>

      <h2>Copii</h2>
      <p>Aplicația nu colectează date de la nimeni, nici de la copii.</p>

      <h2>Modificări ale acestei politici</h2>
      <p>Dacă într-o zi se schimbă ceea ce face aplicația cu datele tale, actualizăm această pagină și data de mai sus înainte ca schimbarea să ajungă în aplicație.</p>
'''


# >>> guías traídas del inglés (ensamblar.py)
# Adaptadas con Ollama (qwen3.6:35b) desde las guías inglesas y auditadas por Opus el 22-nov. Rutas en idiomas_sitio.py.
GUIAS += [
  dict(clave='no-sub', corto='Aplicație telecomandă fără abonament', fecha='2026-11-23',
    titulo='Aplicație de telecomandă pentru TV fără abonament și reclame',
    desc='Te-ai săturat de aplicațiile de telecomandă cu reclame sau abonament săptămânal? Mando TV este gratuită și fără reclame, Pro este o achiziție unică opțională. Comparație cinstită.',
    h1='O aplicație de telecomandă fără abonament și fără reclame',
    intro='Multe telecomenzi universale afișează reclame sau cer un abonament săptămânal înainte să funcționeze. Mando TV merge pe alt drum: telecomanda este gratuită, nu există reclame și nici cont. Pro opțional îl cumperi o singură dată. Iată comparația, inclusiv cu ceea ce aplicația nu poate face.',
    pasos=[
      'Înainte de instalare, deschide pagina din magazin a unei aplicații și verifică achizițiile din aplicație. Prețurile săptămânale sau lunare indică un abonament.',
      'Pe Google Play, verifică dacă pagina spune „Conține reclame” și citește cele mai noi recenzii cu puține stele: acolo apar adesea blocaje neașteptate cu plată.',
      'Asigură-te că aplicația poate controla televizorul prin Wi-Fi. Mando TV funcționează cu Samsung (din 2016), LG webOS, Roku, Google TV, Android TV și Fire TV.',
      'Instalează Mando TV, conectează telefonul la același Wi-Fi ca televizorul și atinge în listă televizorul tău.',
      'Confirmă fereastra de pe televizor sau introdu codul afișat. Butoanele, volumul, canalele și tastatura nu costă nimic.',
    ],
    tabla=dict(titulo='Mando TV în comparație cu multe aplicații de telecomandă',
      cabeza=['', 'Mando TV', 'Multe aplicații cu reclame sau abonament'],
      filas=[
        ['Telecomandă de bază', 'Gratis', 'Adesea gratis cu reclame sau ascunsă în spatele unei perioade de probă'],
        ['Reclame', 'Niciuna', 'Frecvente'],
        ['Abonament', 'Niciunul. Pro este o achiziție unică opțională', 'Planurile săptămânale sau lunare sunt obișnuite'],
        ['Cont', 'Nu este necesar', 'Diferit'],
        ['Smart TV-uri prin Wi-Fi', 'Samsung (din 2016), LG webOS, Roku, Google TV, Android TV, Fire TV, Apple TV (beta)', 'În funcție de aplicație'],
        ['Infraroșu pentru televizoare mai vechi', 'Gratis pe telefoane Android cu emițător de infraroșu (nou)', 'Unele aplicații, doar pe telefoane cu emițător de infraroșu'],
        ['Bluetooth', 'Beta de la Android 9, gratis', 'În funcție de aplicație'],
        ['Fotografii și videoclipuri pe televizor', 'Pro, prin Wi-Fi (fără oglindire)', 'În funcție de aplicație'],
        ['Telefoane și computere', 'iPhone, iPad, Mac și Windows, plus Android în acces anticipat', 'Diferit'],
        ['Oglindirea ecranului', 'Gratis pe iPhone, iPad și Windows, cu funcția încorporată a fiecăruia. Pe Windows, Pro poate oglindi și ecranul PC-ului pe televizoare LG, Samsung, Hisense și Android TV (beta)', 'Unele aplicații o oferă'],
      ],
      nota='Mando TV nu este comparată cu o anumită aplicație. Prețurile actuale se află pe pagina din magazin a fiecărei aplicații.'),
    extra=[
      ('Ce nu face Mando TV', 'Pe iPhone și iPad te duce la Oglindirea ecranului din Centrul de control, funcția iPhone-ului însuși, care merge cu televizoare cu AirPlay. Pe Windows deschide Cast (Windows + K), iar Mando TV Pro poate trimite ecranul PC-ului la televizoare LG, Samsung, Hisense și Android TV prin Wi-Fi (beta, cu o întârziere de câteva secunde și fără sunet). Cu Mando TV Pro poate trimite și fotografii și videoclipuri la televizor prin Wi-Fi. Controlează Smart TV-uri prin Wi-Fi-ul de acasă. Televizoarele fără funcție Smart TV pot fi controlate prin infraroșu de pe un telefon Android cu emițător de infraroșu. De la Android 9, telefonul se poate conecta și prin Bluetooth, ca tastatură și telecomandă, la Google TV, Android TV și Fire TV, fără Wi-Fi. Această opțiune este în versiunea beta și gratuită.'),
      ('Cum câștigă bani Mando TV', 'Nu din reclame și nu din datele tale: aplicația nu colectează niciuna. Mando TV se finanțează prin Pro, o achiziție unică opțională pentru extra. Telecomanda de bază este gratuită.'),
      ('Pe dispozitivele pe care le ai deja', 'iPhone, iPad și Mac din App Store, PC-uri cu Windows din Microsoft Store și Android prin accesul anticipat gratuit de pe Google Play. Vezi [Aplicație telecomandă pentru iPhone](@iphone) și [Aplicație telecomandă pentru Windows](@windows).'),
      ('Confidențialitate', 'Fără cont și fără urmărire în aplicație. Comunicarea cu televizorul are loc doar în rețeaua locală, iar datele de conectare rămân criptate pe dispozitivul tău. Detalii în [Politica de confidențialitate](@privacidad).'),
    ],
    marca=None,
    faq=[
      ('Există o aplicație de telecomandă fără abonament?', 'Da. Mando TV nu are deloc abonament: telecomanda este gratuită și fără reclame, Pro este o achiziție unică opțională.'),
      ('Este Mando TV cu adevărat gratuită?', 'Da. Săgețile, OK, Înapoi, Acasă, volumul, canalele, cifrele, tastatura și pornirea/oprirea sunt gratuite, fără reclame și fără limită de timp.'),
      ('Funcționează fără Wi-Fi?', 'De cele mai multe ori nu. Mando TV controlează Smart TV-uri prin Wi-Fi-ul tău de acasă. Excepții: infraroșul pe telefoane Android cu emițător de infraroșu, care merge și cu televizoare fără funcție Smart TV sau fără conexiune Wi-Fi, și Bluetooth, în versiunea beta de la Android 9, pentru Google TV, Android TV și Fire TV.'),
    ]),
  dict(clave='roku-app-alt', corto='Alternativă la aplicația Roku', fecha='2026-11-23',
    titulo='Alternativă la aplicația Roku: telecomandă Roku simplă',
    desc='O alternativă la aplicația Roku ca telecomandă: Mando TV controlează televizoare și playere Roku prin Wi-Fi, fără cont și reclame, plus Samsung, LG și Google TV.',
    h1='Alternativă la aplicația Roku: una pentru toate televizoarele',
    intro='Aplicația oficială Roku poate multe: Channel Store, casting, Private Listening și o telecomandă. Dacă îți trebuie doar o telecomandă rapidă sau ai acasă și un televizor Samsung, LG sau Google TV, Mando TV este o alternativă simplă, care controlează Roku prin Wi-Fi-ul tău, fără cont.',
    pasos=[
      'Conectează telefonul și Roku la același Wi-Fi.',
      'Descarcă Mando TV și deschide-o. Televizorul Roku sau playerul Roku apare în listă. Atinge-l. Roku nu cere niciun cod.',
      'Folosește săgețile, OK, Înapoi, Acasă, volumul și tastatura. Introdu căutările în canalele Roku cu tastatura telefonului.',
      'Dacă butoanele nu fac nimic, mergi pe Roku la Setări > Sistem > Setări avansate de sistem > Control prin aplicații mobile și setează accesul la rețea pe Implicit sau Permisiv (la software Roku mai nou, setează Control prin aplicații mobile pe Activat).',
      'Opțional: activează pe televizorul Roku „Pornire rapidă TV” la Setări > Sistem > Alimentare, ca Mando TV să poată porni televizorul.',
    ],
    extra=[
      ('Unde se potrivește mai bine Mando TV', 'O aplicație pentru mai multe televizoare: Roku, Samsung, LG și Google TV sau Android TV. Fără cont, fără reclame. Funcționează și pe un PC cu Windows, ceea ce este practic la birou. Săgețile și volumul reacționează repede, iar cu tastatura scrii căutări fără efort.'),
      ('Unde este mai bună aplicația oficială Roku', 'Păstreaz-o pe cea Roku pentru ceea ce oferă dincolo de telecomandă, ca navigarea și adăugarea de canale din Roku Channel Store, precum și castingul propriu și Private Listening (sunetul în căștile de la telefon). Folosește-le pe amândouă, dacă vrei. Pot rula pe același telefon.'),
      ('Televizoare Roku TV și playere Roku', 'Ambele funcționează. Asta include modele Roku TV de la TCL, Hisense, Philips și altele, precum și Roku Express, Streaming Stick și Ultra. Detalii găsești pe [pagina aplicației de telecomandă Roku](@roku).'),
      ('Dacă aplicația Roku nu mai funcționează', 'Dacă butoanele nu mai reacționează, Roku blochează de obicei controlul prin aplicații. Ghidul [Aplicația Roku nu funcționează](@roku-403) arată setarea care rezolvă problema.'),
      ('Gratis și Pro', 'Săgețile, OK, Înapoi, Acasă, volumul, canalele, tastele numerice, tastatura, deschiderea aplicațiilor, schimbarea intrărilor și pornirea sau oprirea sunt gratuite, fără reclame și fără abonament. Touchpadul, comenzile vocale, aplicațiile favorite, rutinele și temporizatorul de oprire fac parte din Mando TV Pro, o achiziție unică fără abonament.'),
    ],
    marca='roku',
    faq=[
      ('Am nevoie de cont Roku ca să folosesc Mando TV?', 'Nu. Mando TV comunică cu Roku prin rețeaua ta de acasă și nu cere cont.'),
      ('Înlocuiește Mando TV complet aplicația Roku Mobile?', 'Ca telecomandă, da. Pentru Channel Store, casting și Private Listening, păstrează aplicația oficială Roku.'),
      ('Funcționează cu Roku Express sau cu Streaming Stick?', 'Da. Toate playerele Roku și televizoarele Roku TV se controlează în același fel.'),
    ]),
  dict(clave='lg-thinq', corto='Alternativă la aplicația LG ThinQ', fecha='2026-11-23',
    titulo='Alternativă la aplicația LG ThinQ: telecomandă LG fără cont',
    desc='Cauți o alternativă la aplicația LG ThinQ doar ca telecomandă? Mando TV controlează televizoare LG cu webOS prin Wi-Fi, fără cont LG și fără reclame.',
    h1='Alternativă la aplicația LG ThinQ pentru televizorul tău LG',
    intro='LG ThinQ este aplicația oficială LG, gândită pentru toată casa inteligentă: electrocasnice, televizor și altele. Dacă îți trebuie doar o telecomandă simplă pentru televizorul LG, Mando TV face exact asta prin Wi-Fi-ul tău de acasă, fără să trebuiască să creezi un cont LG și fără reclame.',
    pasos=[
      'Conectează telefonul sau PC-ul (iPhone, Android sau Windows) și televizorul LG la același Wi-Fi.',
      'Descarcă Mando TV și deschide-o. Televizorul tău LG apare singur în listă. Atinge-l.',
      'Pe televizor apare o fereastră. Confirm-o o dată cu telecomanda televizorului, cu joystickul de sub ecran sau cu Magic Remote.',
      'Butoanele, volumul și tastatura funcționează imediat. Nu ai nevoie de cont LG și nu trebuie să înregistrezi televizorul.',
      'Opțional: activează „Pornire TV de pe dispozitiv mobil” în setările televizorului, ca să poți porni televizorul și de pe telefon.',
    ],
    extra=[
      ('Mando TV sau LG ThinQ: care pentru ce', 'Folosește ThinQ dacă vrei să gestionezi electrocasnice LG, ca o mașină de spălat, un frigider sau un aparat de aer condiționat, sau dacă îți trebuie funcții ale contului LG. Folosește Mando TV dacă vrei o telecomandă rapidă și simplă pentru televizor, care funcționează în aceeași aplicație și pentru Samsung, Roku și Google TV. Mulți le păstrează pe amândouă: ThinQ pentru electrocasnice, Mando TV pentru televizor.'),
      ('Ce face Mando TV pe un televizor LG', 'Funcționează cu Smart TV-uri LG cu webOS, adică cu majoritatea modelelor din 2014 încoace, inclusiv LED, NanoCell, QNED și OLED. Îți oferă săgețile, OK, Înapoi, Acasă, volum, canale, mut, controlul redării și o tastatură pentru a scrie în YouTube, Netflix sau în browser. Lista de aplicații și lista de intrări sunt tot gratuite. Cu Pro primești în plus un cursor ca la Magic Remote.'),
      ('Ce nu face Mando TV', 'Nu controlează electrocasnice LG, nu folosește contul tău LG și nu înlocuiește serviciile contului LG de pe televizor. Este o telecomandă, nu un hub de casă inteligentă.'),
      ('Confidențialitate și reclame', 'Mando TV nu are reclame și nici cont. Vorbește cu televizorul doar în interiorul rețelei tale de acasă și păstrează cheia de conectare criptată pe dispozitivul tău. Toate funcțiile le găsești pe pagina [Aplicație telecomandă LG](@lg).'),
      ('Gratis și Pro', 'Săgețile, OK, Înapoi, Acasă, volumul, canalele, tastele numerice, tastatura, deschiderea aplicațiilor, schimbarea intrărilor și pornirea/oprirea sunt gratuite, fără reclame și fără abonament. Touchpadul, comenzile vocale, aplicațiile favorite, rutinele și temporizatorul de oprire fac parte din Mando TV Pro, o achiziție unică fără abonament.'),
    ],
    marca='lg',
    faq=[
      ('Pot controla televizorul LG fără aplicația LG ThinQ?', 'Da. Mando TV se conectează direct prin Wi-Fi-ul tău la televizoare LG cu webOS. Accepți o dată o fereastră pe televizor și gata, fără cont LG.'),
      ('Funcționează Mando TV cu cursorul LG Magic Remote?', 'Mando TV Pro are un cursor pe care îl miști cu degetul pe ecranul telefonului, similar cu felul în care Magic Remote mișcă săgeata.'),
      ('Este Mando TV de la LG?', 'Nu. Mando TV este o aplicație independentă și nu are nicio legătură cu LG. LG și ThinQ aparțin proprietarilor lor și sunt menționate doar pentru a descrie compatibilitatea.'),
    ]),
  dict(clave='smartthings', corto='Alternativă la SmartThings', fecha='2026-11-23',
    titulo='SmartThings nu merge? Alternativă simplă pentru Samsung',
    desc='SmartThings prea lent sau cu erori? Mando TV controlează televizoare Samsung cu Tizen direct prin Wi-Fi. Fără cont Samsung, fără reclame. Pas cu pas.',
    h1='Alternativă la SmartThings pentru televizoare Samsung',
    intro='SmartThings este aplicația Samsung pentru toată casa inteligentă, iar telecomanda ei merge prin contul tău Samsung. Dacă nu mai funcționează sau cauți o soluție rapidă, Mando TV controlează televizoare Samsung cu Tizen, fabricate în 2016 sau mai recent, direct prin Wi-Fi-ul tău, fără cont.',
    pasos=[
      'Conectează telefonul și televizorul Samsung la același Wi-Fi.',
      'Descarcă Mando TV și deschide aplicația. Televizorul tău Samsung apare singur în listă. Atinge-l.',
      'Televizorul te întreabă dacă vrei să permiți conexiunea. Alege „Permite” cu telecomanda sau cu butonul de pe televizor (doar prima dată).',
      'Folosește imediat săgețile, OK, Înapoi, Acasă, volumul, canalele și tastatura.',
      'Opțional: activează „Pornire cu dispozitiv mobil” la Setări > General > Rețea > Setări expert, ca Mando TV să poată porni și televizorul.',
    ],
    extra=[
      ('De ce nu mai merge o telecomandă de pe telefon', 'Cauzele sunt de obicei simple: telefonul și televizorul sunt în Wi-Fi-uri diferite, un VPN este activ sau televizorul este în standby profund. La SmartThings, mai poate crea probleme și contul Samsung, de exemplu dacă ai fost deconectat. Mando TV vorbește direct cu televizorul din rețeaua de acasă, nu există cont în care să te autentifici. Alte sfaturi găsești la [Telefonul nu găsește televizorul](@not-found).'),
      ('Mando TV sau SmartThings: care pentru ce', 'Păstrează SmartThings dacă îl folosești pentru electrocasnice Samsung, becuri sau alte dispozitive de casă inteligentă ori pentru funcții ale contului tău Samsung. Folosește Mando TV dacă vrei pur și simplu o telecomandă rapidă pentru televizor sau ai acasă și un dispozitiv LG, Roku, Google TV sau Fire TV: o singură aplicație le controlează pe toate. Ambele aplicații pot fi instalate pe același telefon.'),
      ('Dacă ai refuzat permisiunea din greșeală', 'Pe televizor, mergi la Setări > General > Manager dispozitive externe > Manager conexiuni dispozitive și setează Mando TV ca permis.'),
      ('Nu ai telecomandă?', 'Poți confirma fereastra cu butonul de pe televizor. Ghidul [Televizor Samsung fără telecomanda originală](@samsung-lost) îți arată cum.'),
      ('Gratis și Pro', 'Telecomanda o poți descărca și folosi gratuit, fără reclame și fără abonament. Mando TV Pro este o achiziție unică opțională pentru extra.'),
    ],
    marca='samsung',
    faq=[
      ('Pot controla televizorul Samsung fără SmartThings?', 'Da. Mando TV se conectează direct prin Wi-Fi-ul tău la televizoare Samsung cu Tizen. Permiți conexiunea o dată pe televizor, fără cont Samsung.'),
      ('Controlează Mando TV și electrocasnice Samsung?', 'Nu. Este doar o telecomandă pentru televizor. Pentru electrocasnice și alte dispozitive de casă inteligentă, păstrezi SmartThings.'),
      ('Este Mando TV de la Samsung?', 'Nu. Mando TV este o aplicație independentă și nu are nicio legătură cu Samsung. Samsung și SmartThings aparțin proprietarilor lor și sunt menționate doar pentru a descrie compatibilitatea.'),
    ]),
  dict(clave='googletv-alt', corto='Alternativă la telecomanda Google TV', fecha='2026-11-23',
    titulo='Telecomanda Google TV nu merge? Alternativa',
    desc='Telecomanda de pe telefon pentru Google TV nu găsește televizorul? Mando TV controlează Google TV și Android TV prin Wi-Fi, fără cont Google și reclame.',
    h1='Alternativă la telecomanda Google TV de pe telefon',
    intro='Telecomanda de pe telefon pentru Google TV și Android TV se află în aplicația Google și este legată de contul tău Google. Dacă nu găsește televizorul, rămâi pe loc. Mando TV este o aplicație de telecomandă separată, care se asociază cu codul de 6 caractere de pe ecran și funcționează fără cont Google, pe un iPhone, un telefon Android sau un PC cu Windows.',
    pasos=[
      'Pornește televizorul și conectează telefonul la același Wi-Fi.',
      'Descarcă Mando TV și deschide aplicația. Atinge în listă televizorul tău cu Google TV sau Android TV.',
      'Televizorul afișează un cod de 6 caractere. Introdu-l în Mando TV și atinge Asociază.',
      'Folosește săgețile, OK, Înapoi, Acasă, volumul și tastatura. Nu trebuie să te autentifici nicăieri.',
      'Opțional: caută în setările televizorului Wake on LAN sau „Pornire prin rețea”, ca aplicația să poată porni și televizorul.',
    ],
    extra=[
      ('De ce telecomanda de pe telefon nu mai găsește televizorul', 'De cele mai multe ori este vorba de rețea: telefonul și televizorul sunt în Wi-Fi-uri diferite, un VPN este activ sau o rețea pentru oaspeți separă dispozitivele. Rezolvă mai întâi asta, pentru că afectează toate aplicațiile de telecomandă. Mai multe la [Telefonul nu găsește televizorul](@not-found).'),
      ('Cu ce televizoare funcționează', 'Televizoare cu Google TV și Android TV de la Sony, TCL, Hisense, Philips, Sharp, Xiaomi, Toshiba și altele, precum și Chromecast cu Google TV, Google TV Streamer și Nvidia Shield. Toate se asociază la fel, o singură dată, cu codul de pe ecran.'),
      ('Unde este mai bună aplicația Google', 'Aplicația Google te ajută și să găsești conținut de vizionat și își amintește lista ta de urmărit. Păstreaz-o pentru asta. Mando TV este doar telecomanda și controlează în plus dispozitive Samsung, LG, Roku și Fire TV din aceeași aplicație, precum și de pe un PC cu Windows.'),
      ('Dacă lipsește vechea aplicație de telecomandă Android TV', 'Google a mutat telecomanda de pe telefon din vechea aplicație Android TV Remote Control în aplicația Google TV. Dacă îți trebuie o telecomandă de sine stătătoare, Mando TV este o opțiune.'),
      ('Gratis și Pro', 'Telecomanda o poți descărca și folosi gratuit, fără reclame și fără abonament. Mando TV Pro este o achiziție unică opțională pentru extra.'),
    ],
    marca='android',
    faq=[
      ('Am nevoie de cont Google ca să folosesc Mando TV cu Google TV?', 'Nu. Codul de pe televizor ajunge pentru asociere.'),
      ('Funcționează cu Chromecast cu Google TV?', 'Da. Asocierea merge la fel, cu codul de 6 caractere de pe ecran.'),
      ('Pot să o folosesc de pe un iPhone?', 'Da. Mando TV este disponibilă în App Store pentru iPhone și iPad, în Microsoft Store pentru Windows și în accesul anticipat gratuit de pe Google Play pentru Android.'),
    ]),
  dict(clave='windows', corto='Telecomandă pentru PC cu Windows', fecha='2026-11-23',
    titulo='Aplicație telecomandă pentru Windows: controlează TV-ul de pe PC',
    desc='Controlează Samsung, LG, Roku, Google TV sau Fire TV de pe un PC cu Windows cu Mando TV: scurtături de tastatură, mini telecomandă și Wi-Fi. În Microsoft Store.',
    h1='Aplicație de telecomandă pentru PC cu Windows',
    intro='Mando TV are o aplicație pentru Windows care transformă PC-ul sau laptopul într-o telecomandă pentru televizor, prin rețeaua de acasă. Scrii pe televizor cu tastatura ta reală, ții o mică fereastră de telecomandă deasupra celorlalte în timp ce lucrezi și controlezi Samsung, LG, Roku, Google TV sau Fire TV cu aceeași aplicație.',
    pasos=[
      'Instalează gratuit Mando TV din Microsoft Store pe un PC cu Windows 10 sau 11.',
      'Asigură-te că PC-ul și televizorul sunt în aceeași rețea, prin Wi-Fi sau prin cablu la același router.',
      'Deschide Mando TV. Televizorul apare în listă. Fă clic pe el.',
      'Confirmă fereastra de pe televizor, dacă te întreabă (LG, Samsung), sau introdu codul afișat (Google TV, Fire TV).',
      'Fă clic pe butoane sau scrie o căutare cu tastatura. Gata.',
    ],
    extra=[
      ('Scurtături de tastatură (Pro)', 'Cu Pro, tastatura PC-ului devine telecomandă: săgețile pentru deplasare, Enter pentru OK, Backspace sau Esc pentru înapoi, plus și minus pentru volum, M pentru mut și bara de spațiu pentru pauză.'),
      ('Mini telecomandă (Pro)', 'O mică fereastră de telecomandă care rămâne deasupra tuturor celorlalte ferestre. Așa schimbi volumul sau pui pauză fără să-ți întrerupi munca.'),
      ('Scrie pe televizor de pe PC', 'Tastatura de pe ecran a unui televizor este lentă. În Mando TV scrii cu tastatura ta reală, iar textul ajunge în câmpul de căutare al televizorului. Această parte este gratuită.'),
      ('Mai multe detalii', 'Ghidul pas cu pas îl găsești la [Controlează televizorul de pe PC](@pc). Pentru telefon, citește [Telefonul ca telecomandă prin Wi-Fi](@wifi).'),
      ('Gratis și Pro', 'Săgețile, OK, Înapoi, Acasă, volumul, canalele, tastele numerice, tastatura, deschiderea aplicațiilor, schimbarea intrărilor și pornirea sau oprirea sunt gratuite, fără reclame și fără abonament. Touchpadul, comenzile vocale, aplicațiile favorite, rutinele și temporizatorul de oprire fac parte din Mando TV Pro, o achiziție unică fără abonament. Pe Windows cumperi Pro prin Microsoft Store.'),
      ('Comenzi vocale de pe PC (Pro)', 'Cu Pro poți vorbi cu televizorul prin microfonul PC-ului. Vorbirea este recunoscută direct pe PC: nu ai nevoie de internet și nu trebuie să setezi nimic în Windows. Ce spui nu părăsește niciodată PC-ul și nu este salvat. Doar la procesoare foarte vechi aplicația revine la dictarea din Windows. Atunci trebuie activată recunoașterea vocală online în setările de confidențialitate și adăugată limba ta în Windows.'),
    ],
    marca=None,
    faq=[
      ('Are aplicația de telecomandă pentru Windows nevoie de Bluetooth sau de cablu?', 'Nu. Folosește rețeaua ta de acasă. PC-ul și televizorul trebuie doar să fie conectate la același router.'),
      ('Ce televizoare pot controla de pe Windows?', 'Televizoare Samsung cu Tizen, LG cu webOS, Roku TV și playere, Google TV și Android TV, precum și Fire TV.'),
      ('Pot vedea imaginea televizorului pe PC sau o pot auzi prin boxele PC-ului?', 'Nu. Mando TV este doar o telecomandă. Nu oglindește și nu transmite imaginea televizorului pe computer.'),
      ('De ce nu merge vocea pe PC-ul meu cu Windows?', 'Controlul vocal este o funcție Pro. Verifică deci dacă Pro este activ și dacă microfonul PC-ului funcționează. Pe majoritatea PC-urilor vorbirea este recunoscută direct pe PC, fără internet. Doar la procesoare foarte vechi aplicația folosește dictarea din Windows: atunci activează recunoașterea vocală online în setările de confidențialitate din Windows și adaugă limba ta în setările de limbă.'),
    ]),
  dict(clave='iphone', corto='Aplicație telecomandă pentru iPhone', fecha='2026-11-23',
    titulo='Aplicație de telecomandă pentru iPhone: Samsung, LG, Roku, Google TV',
    desc='Folosește iPhone-ul ca telecomandă pentru Samsung, LG, Roku, Google TV și Fire TV prin Wi-Fi. Gratis în App Store, fără cont și fără reclame.',
    h1='Aplicație de telecomandă pentru iPhone: una pentru toate televizoarele',
    intro='Mando TV transformă iPhone-ul sau iPad-ul într-o telecomandă pentru Samsung, LG, Roku, Google TV sau Android TV, precum și Fire TV, prin Wi-Fi-ul tău de acasă. Aplicația este gratuită în App Store, fără cont și fără reclame. Rulează și pe Android și pe Windows.',
    pasos=[
      'Descarcă gratuit Mando TV din App Store.',
      'Conectează iPhone-ul și televizorul la același Wi-Fi.',
      'Deschide Mando TV și atinge Permite când iOS cere acces la rețeaua locală. Aplicația are nevoie de el ca să găsească televizorul.',
      'Atinge în listă televizorul tău. Confirmă fereastra de pe televizor, dacă te întreabă (LG și Samsung), sau introdu codul pe care îl arată televizorul (Google TV sau Fire TV).',
      'Folosește butoanele, volumul și tastatura. Ești conectat.',
    ],
    extra=[
      ('Funcționează cu aceste televizoare', 'LG webOS, Samsung Tizen (fabricate în 2016 sau mai recent), Roku TV și playere Roku, Google TV și Android TV, precum și Fire TV. Paginile mărcilor sunt [Samsung](@samsung), [LG](@lg), [Roku](@roku) și [Android TV](@android).'),
      ('De ce cere acces la rețeaua locală', 'iPhone-ul blochează accesul aplicațiilor la dispozitivele din rețeaua ta de acasă, dacă nu permiți. Dacă televizorul nu apare în listă, deschide Setări > Mando TV și activează „Rețea locală”. Aplicația comunică doar cu televizorul tău, în interiorul rețelei de acasă.'),
      ('De ce Mando TV și nu aplicația producătorului', 'Fiecare marcă de televizoare are aplicația ei și vrea o configurare sau un cont propriu. Mando TV este o singură aplicație pentru toate, fără cont.'),
      ('Gratis și Pro pe iPhone', 'Săgețile, OK, Înapoi, Acasă, volumul, canalele, tastele numerice, tastatura, deschiderea aplicațiilor, schimbarea intrărilor și pornirea sau oprirea sunt gratuite, fără reclame și fără abonament. Touchpadul, comenzile vocale, aplicațiile favorite, rutinele și temporizatorul de oprire fac parte din Mando TV Pro, o achiziție unică fără abonament. Cumperi Pro o singură dată, direct în aplicație.'),
    ],
    marca=None,
    faq=[
      ('Este Mando TV gratuită pe iPhone?', 'Descărcarea este gratuită și fără reclame. Telecomanda de bază este gratuită, la fel deschiderea aplicațiilor și schimbarea intrărilor. Extra, precum touchpadul, comenzile vocale și rutinele, fac parte din Mando TV Pro, o achiziție unică.'),
      ('Funcționează pe iPad?', 'Da. Aceeași aplicație rulează pe iPhone și pe iPad.'),
      ('Are o aplicație de telecomandă pentru iPhone nevoie de Bluetooth sau de emițător de infraroșu?', 'Nu pe iPhone. iPhone-urile nu au emițător de infraroșu, deci controlul prin infraroșu nu este disponibil acolo, iar opțiunea Bluetooth există doar pentru Android 9 sau mai nou, nu pentru iPhone. Pe iPhone, Mando TV controlează Smart TV-uri, precum și Apple TV (beta), prin Wi-Fi-ul tău de acasă.'),
    ]),
  dict(clave='firetv', corto='Telecomandă Fire TV', fecha='2026-11-23',
    titulo='Aplicație telecomandă Fire TV pentru telefon și PC',
    desc='Telecomandă Fire TV pe telefon: controlează Fire TV Stick, Fire TV Cube sau un televizor cu Fire TV prin Wi-Fi, cu PIN de 4 cifre. Fără aplicația Amazon.',
    h1='Telecomandă Fire TV pentru telefon sau PC',
    intro='Dacă ai pierdut telecomanda Fire TV sau bateriile s-au terminat, Mando TV controlează un Fire TV Stick, un Fire TV Cube sau un televizor cu Fire TV integrat prin Wi-Fi. Asocierea se face cu un PIN de 4 cifre. Fire TV este nou în Mando TV, așa că actualizează mai întâi aplicația.',
    pasos=[
      'Actualizează Mando TV la ultima versiune din App Store, Microsoft Store sau Google Play.',
      'Pornește Fire TV și conectează telefonul la același Wi-Fi.',
      'Deschide Mando TV. Fire TV-ul tău apare în listă. Atinge-l.',
      'Pe ecranul televizorului apare un PIN de 4 cifre. Introdu-l în Mando TV. Îl faci o singură dată.',
      'Folosește săgețile, OK, Înapoi, Acasă, butoanele de redare și tastatura pentru căutări.',
    ],
    extra=[
      ('Dispozitive Fire TV compatibile', 'Fire TV Stick, Fire TV Stick 4K, Fire TV Cube și televizoare cu Fire TV integrat, cum ar fi televizoarele Amazon Fire TV Edition și unele modele Hisense. Suportul este nou și până acum am putut testa doar câteva dispozitive reale. Dacă ceva nu merge cum te aștepți, scrie-ne modelul tău prin pagina de ajutor.'),
      ('Cum pornești Fire TV', 'Mando TV nu pornește un Fire TV prin rețea. Pornește televizorul cu butonul de pe aparat: un Fire TV Stick sau Cube conectat se trezește de obicei prin HDMI-CEC, iar la un televizor cu Fire TV integrat, televizorul este chiar Fire TV. După aceea îl controlezi de pe telefon.'),
      ('Dacă Fire TV nu apare', 'Asigură-te că ambele dispozitive sunt în același Wi-Fi și că Fire TV este pornit. Pe iPhone, permite „Rețea locală” pentru Mando TV în Setări. Vezi [Telefonul nu găsește televizorul](@not-found).'),
      ('Nu ai deloc telecomandă?', 'Fire TV trebuie să arate PIN-ul pe ecran, deci televizorul și Fire TV trebuie să fie pornite și să afișeze imaginea. Dacă televizorul este pe o intrare greșită, schimb-o cu butoanele de pe televizor. Vezi [Schimbă intrarea fără telecomandă](@hdmi).'),
      ('Gratis și Pro', 'Săgețile, OK, Înapoi, Acasă, volumul, canalele, cifrele, tastatura, deschiderea aplicațiilor, schimbarea intrărilor și pornirea/oprirea sunt gratuite, fără reclame și fără abonament. Touchpadul, comenzile vocale, aplicațiile favorite, rutinele și temporizatorul de oprire fac parte din Mando TV Pro, o achiziție unică fără abonament.'),
    ],
    marca=None,
    faq=[
      ('Am nevoie de aplicația Amazon Fire TV?', 'Nu. Mando TV se conectează la Fire TV prin Wi-Fi-ul tău, cu PIN. Nu ai nevoie de cont Amazon pe telefon.'),
      ('Funcționează cu televizoare cu Fire TV și cu Fire TV Stick?', 'Da, exact pentru asta a fost creată. Suportul este nou, ține aplicația actualizată și spune-ne despre modelele care nu merg cum te aștepți.'),
      ('De ce am nevoie de un PIN?', 'Fire TV afișează un PIN de 4 cifre ca să dovedești că ești în fața televizorului. Nimeni nu se poate asocia fără să vadă ecranul.'),
    ]),
  dict(clave='firetv-lost', corto='Telecomandă Fire TV pierdută', fecha='2026-11-23',
    titulo='Ai pierdut telecomanda Fire TV? Telefonul te ajută',
    desc='Ai pierdut telecomanda Fire TV Stick? Controlează-l prin Wi-Fi cu telefonul, asociat cu un PIN de 4 cifre. Sfaturi pentru Wi-Fi nou și HDMI-CEC.',
    h1='Telecomandă Fire TV pierdută: folosește telefonul',
    intro='Dacă telecomanda pentru Fire TV Stick, Fire TV Cube sau Smart TV cu Fire TV s-a pierdut sau nu mai funcționează, telefonul preia controlul, atâta timp cât Fire TV este încă conectat la Wi-Fi-ul tău. Asocierea se face cu un PIN de 4 cifre pe ecran, așa că nu ai nevoie niciodată de vechea telecomandă pentru asta.',
    pasos=[
      'Pornește televizorul cu butonul de pe aparat. Un Fire TV Stick sau Cube conectat se trezește de obicei odată cu el; cu HDMI-CEC activat, televizorul trece adesea singur pe intrarea lui.',
      'Dacă televizorul arată altă intrare, schimb-o cu butonul de intrare sau de sursă de pe televizor. Vezi [Schimbă intrarea fără telecomandă](@hdmi).',
      'Conectează telefonul la același Wi-Fi ca Fire TV.',
      'Descarcă Mando TV și deschide aplicația. Fire TV-ul tău apare în listă. Atinge-l.',
      'Televizorul arată un PIN de 4 cifre. Introdu-l în Mando TV. Îl faci o singură dată.',
      'Folosește săgețile, OK, Înapoi, Acasă, volumul, butoanele de redare și tastatura de pe telefon.',
    ],
    extra=[
      ('Încearcă mai întâi telecomanda televizorului (HDMI-CEC)', 'Multe telecomenzi de televizor pot controla un Fire TV Stick prin HDMI-CEC. Dacă vezi interfața Fire TV, apasă săgețile și OK de pe telecomanda televizorului. Dacă nu se întâmplă nimic, activează CEC în setările televizorului (Anynet+ la Samsung, SIMPLINK la LG, BRAVIA Sync la Sony) și, pe Fire TV, controlul dispozitivelor HDMI-CEC în setările de afișare („Display & Sounds”).'),
      ('Dacă ai schimbat Wi-Fi-ul', 'Fără telecomandă nu poți introduce parola noului Wi-Fi pe Fire TV, dar există o soluție: creează pe un al doilea telefon un hotspot cu exact același nume și aceeași parolă ca vechiul tău Wi-Fi. Fire TV se conectează singur la el. Conectează telefonul cu Mando TV la acel hotspot, asociază-l cu PIN-ul, apoi mergi pe Fire TV la Setări > Rețea și alege noul tău Wi-Fi. La final, conectează și telefonul la noul Wi-Fi.'),
      ('Asocierea unei telecomenzi de schimb', 'Cele mai multe telecomenzi Fire TV noi se asociază ținând apăsat butonul Acasă cam 10 secunde, aproape de Fire TV. Dacă nu merge, deschide Setări > Controlere și dispozitive Bluetooth > Telecomenzi Amazon Fire TV > Adaugă o telecomandă nouă. Poți ajunge la acest meniu și de pe telefon, cu Mando TV.'),
      ('Fire TV integrat în televizor', 'La televizoarele cu Fire TV integrat, cum sunt multe modele Insignia și Toshiba, se aplică aceiași pași, pentru că televizorul însuși este Fire TV.'),
      ('Înainte de a începe', 'Suportul pentru Fire TV este nou în Mando TV. Actualizează mai întâi aplicația. Dacă modelul tău nu reacționează cum te aștepți, scrie-ne prin [pagina de ajutor](@soporte) și spune-ne modelul.'),
      ('Gratis și Pro', 'Telecomanda o poți descărca și folosi gratuit, fără reclame și fără abonament. Mando TV Pro este o achiziție unică opțională pentru extra.'),
    ],
    marca=('firetv', 'Telecomandă Fire TV'),
    faq=[
      ('Pot controla un Fire TV Stick cu telefonul, fără telecomandă?', 'Da, atâta timp cât Fire TV este pornit și conectat la Wi-Fi-ul tău. Mando TV se asociază prin PIN-ul de 4 cifre de pe televizor, deci nu ai nevoie de vechea telecomandă.'),
      ('Funcționează dacă Fire TV este într-un Wi-Fi nou?', 'Nu direct, pentru că telefonul și Fire TV trebuie să fie în aceeași rețea. Readu mai întâi Fire TV online cu trucul hotspotului de pe această pagină.'),
      ('Am nevoie de aplicația Amazon Fire TV sau de cont Amazon?', 'Nu. Mando TV se conectează prin rețeaua ta de acasă cu PIN și nu cere un cont propriu.'),
    ]),
  dict(clave='turn-on', corto='Pornește televizorul fără telecomandă', fecha='2026-11-23',
    titulo='Cum pornești televizorul fără telecomandă (toate mărcile)',
    desc='Pornește televizorul fără telecomandă: unde e butonul la Samsung, LG, TCL, Hisense, Sony și Vizio. Plus HDMI-CEC și trucuri cu telefonul.',
    h1='Cum pornești un televizor fără telecomandă',
    intro='Aproape orice televizor are încă un buton fizic de pornire și oprire. Doar că este bine ascuns. Aici vezi unde se află la fiecare marcă, plus două moduri de a nu mai căuta data viitoare: HDMI-CEC de la o consolă sau un dispozitiv de streaming și pornirea televizorului de pe telefon, prin Wi-Fi.',
    pasos=[
      'Uită-te sub mijlocul ecranului, chiar în spatele siglei mărcii. Multe televizoare au acolo un mic buton sau un joystick, îndreptat în jos.',
      'Dacă nu e acolo, pipăie partea din spate a televizorului, lângă colțurile de jos, apoi marginile din stânga și din dreapta.',
      'Apasă butonul o dată. La multe televizoare cu un singur buton, o apăsare scurtă cu aparatul pornit deschide un mic meniu pentru intrări și volum, iar o apăsare lungă îl oprește.',
      'Tot nimic? Verifică cablul de alimentare la ambele capete și încearcă altă priză. Dacă lampa de standby nu se aprinde, televizorul nu primește curent.',
      'Imediat ce televizorul e pornit, setează-l ca să nu mai ai nevoie de buton: activează HDMI-CEC și pornirea prin rețea, ambele explicate mai jos.',
    ],
    extra=[
      ('Unde se află butonul de pornire, în funcție de marcă', 'Samsung: un buton de control sau un joystick sub mijlocul ecranului ori în spate, într-un colț de jos. LG: un buton joystick sub sigla LG la majoritatea modelelor. TCL și Hisense: de obicei un mic buton sub mijlocul ecranului sau în spate, lângă un colț de jos. Sony: în spate sau pe o margine laterală, jos, aproape de margine. Vizio: în spate, jos în stânga sau jos în dreapta, ori pe lateral. Pozițiile diferă de la model la model. Dacă nu le găsești, caută manualul cu numărul modelului de pe eticheta din spate.'),
      ('Pornește televizorul de la o consolă sau de la un dispozitiv de streaming (HDMI-CEC)', 'Cu HDMI-CEC activat, pornirea unui PlayStation, a unui Xbox, a unui player Roku, a unui Fire TV Stick sau a unui Chromecast pornește și televizorul și trece pe intrarea corectă. Fiecare marcă numește setarea altfel: Anynet+ la Samsung, SIMPLINK la LG, BRAVIA Sync la Sony și CEC la majoritatea celorlalte. Mai mult la [Pornește televizorul și treci pe HDMI-ul consolei](@console).'),
      ('Pornește televizorul de pe telefon', 'Smart TV-urile pot fi trezite prin Wi-Fi dacă permiți asta o dată, iar apoi Mando TV le pornește de pe telefon. La Samsung, activează „Pornire cu dispozitiv mobil” la Setări > General > Rețea > Setări expert. La LG, activează „Pornire TV de pe dispozitiv mobil” ([pas cu pas](@lg-on)). La un televizor Roku, activează „Pornire rapidă TV” la Setări > Sistem > Alimentare. La Google TV și Android TV, caută Wake on LAN sau „Pornire prin rețea”, dacă modelul tău o are. Faci asta o singură dată, cu televizorul pornit.'),
      ('Dacă nu găsești niciun buton', 'Unele televizoare noi ascund singurul buton atât de bine, încât pare că nu există. Caută o mică proeminență sau o zonă cu senzor de lumină sub ecran: butonul este adesea chiar lângă ea. Prin Wi-Fi, Mando TV are nevoie ca televizorul să fi fost pornit o dată și conectat. Infraroșul este excepția: pe un telefon Android cu emițător de infraroșu, Mando TV poate porni un televizor care nu a fost niciodată configurat, atâta timp cât îndrepți telefonul spre televizor. Infraroșul este nou și funcționează cu mărcile din lista de coduri a aplicației.'),
      ('Gratis și Pro', 'Telecomanda o poți descărca și folosi gratuit, fără reclame și fără abonament. Mando TV Pro este o achiziție unică opțională pentru extra.'),
    ],
    marca=None,
    faq=[
      ('Pot porni un televizor cu telefonul dacă nu l-am configurat niciodată?', 'Nu prin Wi-Fi. Un televizor oprit se trezește din rețea doar dacă pornirea prin rețea a fost activată înainte. Prima dată folosește butonul de pe televizor. Excepția este un telefon Android cu emițător de infraroșu: Mando TV poate porni prin infraroșu un televizor neconfigurat, dacă marca este în lista de coduri sau alegi „Altă marcă sau nu știu”.'),
      ('Cum pornesc un televizor Samsung fără telecomandă?', 'Apasă butonul de control de sub mijlocul ecranului sau din spate, într-un colț de jos. Apoi activează „Pornire cu dispozitiv mobil”, ca telefonul să-l poată porni data viitoare.'),
      ('Cum pornesc un televizor Roku fără telecomandă?', 'Folosește butonul de pe televizor, de obicei sub mijloc sau în spate. Apoi activează „Pornire rapidă TV” la Setări > Sistem > Alimentare, ca Mando TV să-l poată porni de pe telefon.'),
      ('De ce se pornește televizorul singur când pornesc consola?', 'Este HDMI-CEC. Este practic și îl poți opri din setările televizorului, dacă preferi.'),
    ]),
  dict(clave='sony', corto='Telecomandă Sony', fecha='2026-11-23',
    titulo='Aplicație telecomandă Sony pentru telefon și PC',
    desc='Mando TV controlează televizoare Sony Bravia cu Google TV sau Android TV prin Wi-Fi. Suport beta pentru modelele din 2013 până în 2015 fără Android.',
    h1='Cum controlezi televizorul Sony cu telefonul',
    intro='Smart TV-urile Sony Bravia mai noi folosesc Google TV, iar modelele mai vechi, din 2015 încoace, Android TV. Mando TV le controlează pe amândouă prin Wi-Fi-ul tău, de pe iPhone, telefon Android sau PC cu Windows. Aplicația înlocuiește telecomanda originală când s-a pierdut sau bateriile s-au terminat.',
    pasos=[
      'Verifică dacă televizorul Sony afișează ecranul de start Google TV sau Android TV. Asta e valabil la majoritatea Smart TV-urilor Sony Bravia fabricate din 2015 încoace.',
      'Conectează telefonul și televizorul la același Wi-Fi.',
      'Deschide Mando TV și atinge în listă televizorul tău Sony.',
      'Introdu codul de 6 caractere pe care televizorul îl afișează pe ecran (doar prima dată). Nu ai nevoie de telecomandă pentru asta.',
      'Folosește săgețile, OK, Înapoi, Acasă, volumul și tastatura.',
    ],
    extra=[
      ('Pornește un televizor Sony de pe telefon', 'Modelele Sony cu Google TV sau Android TV pot fi trezite prin rețea dacă „Remote start” este activat. Găsești opțiunea de obicei la Setări > Rețea și internet > Remote start (calea poate diferi ușor în funcție de model). Apoi atinge televizorul în Mando TV cât timp este oprit, iar aplicația îl pornește.'),
      ('Unde se află butonul de pornire la un Sony', 'La majoritatea televizoarelor Bravia este în spate, lângă colțul din stânga jos sau din dreapta jos, ori pe o margine laterală. O apăsare scurtă pornește televizorul. Mai multe găsești la [Pornește televizorul fără telecomandă](@turn-on).'),
      ('Televizoare Sony mai vechi', 'Televizoarele Sony Bravia din 2013 până în 2015 care nu folosesc Android sunt acceptate în Mando TV în versiune beta. Este nou și poate avea încă mici defecte. Televizorul afișează un PIN de 4 cifre pe care trebuie să-l introduci în aplicație. Alte televizoare Sony fără Google TV sau Android TV nu sunt acceptate deocamdată.'),
      ('Gratis și Pro', 'Telecomanda o poți descărca și folosi gratuit, fără reclame și fără abonament. Mando TV Pro este o achiziție unică opțională pentru extra.'),
    ],
    marca='android',
    faq=[
      ('Funcționează Mando TV cu televizoarele Sony Bravia?', 'Da, cu televizoarele Sony care folosesc Google TV sau Android TV. Asta cuprinde majoritatea Smart TV-urilor Sony fabricate din 2015 încoace.'),
      ('Am nevoie de o aplicație Sony sau de cont Google?', 'Nu. Mando TV se asociază cu codul de pe ecranul televizorului și nu cere cont.'),
      ('Funcționează cu televizoare Sony Bravia mai vechi, fără Android?', 'Da, în versiune beta, la modelele Bravia din 2013 până în 2015 fără Android. Asocierea se face cu un PIN de 4 cifre afișat pe televizor.'),
      ('Pot scrie de pe telefon pe televizorul Sony?', 'Da. Tastatura este gratuită și funcționează în YouTube, Netflix și în căutarea televizorului.'),
    ]),
  dict(clave='tcl', corto='Telecomandă TCL', fecha='2026-11-23',
    titulo='Aplicație telecomandă TCL pentru telefon și PC',
    desc='Ai pierdut telecomanda TCL? Majoritatea televizoarelor TCL folosesc Roku TV sau Google TV. Mando TV le controlează pe ambele prin Wi-Fi, fără cont și reclame.',
    h1='Cum controlezi televizorul TCL cu telefonul',
    intro='TCL face televizorul, dar software-ul este Roku TV sau Google TV (la modelele mai vechi, Android TV). Mando TV controlează ambele sisteme și funcționează ca telecomandă pentru televizorul tău TCL prin Wi-Fi. Gratis, fără cont și fără reclame.',
    pasos=[
      'Află ce sistem folosește televizorul tău TCL. Dacă ecranul de start arată o grilă simplă de canale, este Roku TV. Dacă arată ca Google TV sau Android TV, cu rânduri pline de recomandări, este Google TV.',
      'Conectează telefonul și televizorul TCL la același Wi-Fi.',
      'Deschide Mando TV. TCL-ul apare singur în listă. Atinge-l.',
      'La un TCL cu Roku TV nu mai e nevoie de nimic. La un TCL cu Google TV, introdu codul de 6 caractere pe care televizorul îl arată pe ecran (doar prima dată).',
      'Folosește săgețile, OK, Înapoi, Acasă, volumul și tastatura. Pornește televizorul din aplicație dacă ai activat pornirea prin rețea (vezi mai jos).',
    ],
    extra=[
      ('Pornește un televizor TCL de pe telefon', 'La TCL cu Roku TV, activează „Pornire rapidă TV” la Setări > Sistem > Alimentare. La TCL cu Google TV, caută o opțiune pentru Wake on LAN, „Pornire prin rețea” sau pornire de la distanță în setările de rețea sau de alimentare. Unele modele nu o au. În acest caz, pornește televizorul cu butonul fizic, de obicei jos la mijloc sau în spate.'),
      ('Dacă TCL-ul tău nu apare', 'Verifică dacă telefonul și televizorul sunt în același Wi-Fi. Routerele cu rețele separate de 2,4 GHz și 5 GHz pot ascunde dispozitivele unele de altele. Pe iPhone, permite „Rețea locală” pentru Mando TV în Setări. Poți adăuga televizorul și introducând adresa lui IP. Citește [Telefonul nu găsește televizorul](@not-found).'),
      ('Mai multe despre TCL-ul tău', 'Pentru TCL cu Roku TV vezi [Aplicație telecomandă Roku](@roku), iar pentru TCL cu Google TV sau Android TV [Aplicație telecomandă Android TV](@android).'),
      ('Gratis și Pro', 'Săgețile, OK, Înapoi, Acasă, volumul, canalele, cifrele, tastatura, deschiderea aplicațiilor, schimbarea intrărilor și pornirea/oprirea sunt gratuite, fără reclame și fără abonament. Touchpadul, comenzile vocale, aplicațiile favorite, rutinele și temporizatorul de oprire fac parte din Mando TV Pro, o achiziție unică fără abonament.'),
    ],
    marca=None,
    faq=[
      ('Funcționează Mando TV cu orice televizor TCL?', 'Funcționează cu televizoarele TCL cu Roku TV, Google TV sau Android TV, adică cu majoritatea Smart TV-urilor TCL. Un TCL care nu este Smart TV nu poate fi controlat prin Wi-Fi.'),
      ('Am nevoie de aplicația TCL sau de cont TCL?', 'Nu. Mando TV se conectează direct prin Wi-Fi-ul tău de acasă și nu cere cont.'),
      ('TCL-ul meu cere un cod. Unde este?', 'Modelele TCL cu Google TV și Android TV arată pe ecran un cod de 6 caractere. Introdu-l exact așa în Mando TV. Un TCL cu Roku TV nu cere cod.'),
    ]),
  dict(clave='hisense', corto='Telecomandă Hisense', fecha='2026-11-23',
    titulo='Aplicație telecomandă Hisense: ce merge de pe telefon',
    desc='Telecomandă Hisense cu Mando TV: control pentru VIDAA, Roku TV, Google TV și Fire TV prin Wi-Fi. Prezentare cinstită a ceea ce funcționează.',
    h1='Aplicație telecomandă Hisense: ce merge și ce nu',
    intro='Televizoarele Hisense nu sunt la fel pe dinăuntru. În funcție de model, folosesc sistemul propriu Hisense VIDAA, Roku TV, Google TV sau Fire TV. Mando TV funcționează ca telecomandă pentru Hisense pe toate cele patru sisteme, cu o excepție la unele modele VIDAA mai noi. Aici vezi cum afli ce sistem ai și la ce să te aștepți.',
    pasos=[
      'Verifică ce sistem folosește Hisense-ul tău. VIDAA este interfața proprie Hisense. Roku TV arată o grilă de canale. Google TV arată rânduri cu recomandări. Fire TV arată ecranul de start Fire TV, cu rânduri Amazon.',
      'Conectează telefonul și televizorul Hisense la același Wi-Fi.',
      'Deschide Mando TV. Televizorul apare singur în listă. Atinge-l.',
      'Modelele VIDAA și Fire TV pot afișa un PIN de patru cifre; Google TV afișează un cod de șase caractere. Introdu-l în aplicație. Roku TV nu cere nimic. Faci asta o singură dată.',
      'Folosește săgețile, OK, Înapoi, Acasă, volumul și tastatura de pe telefon.',
    ],
    extra=[
      ('Hisense cu Roku TV sau Google TV', 'Acestea funcționează complet ca orice alt televizor Roku sau Google TV. Detalii pe paginile [Aplicație telecomandă Roku](@roku) și [Aplicație telecomandă Android TV](@android).'),
      ('Hisense cu Fire TV', 'Suportul pentru Fire TV este nou în Mando TV. Actualizează aplicația la ultima versiune din magazinul tău. Cum funcționează asocierea cu PIN găsești pe pagina [Aplicație telecomandă Fire TV](@firetv). Dacă ceva nu merge cum te aștepți, scrie-ne prin pagina de ajutor și spune-ne modelul.'),
      ('Hisense cu VIDAA', 'Majoritatea modelelor VIDAA funcționează: butoane, volum, tastatură, aplicații și intrări. Unele modele VIDAA mai noi acceptă doar aplicația oficială Hisense. Mando TV observă asta la conectare și îți spune clar, în loc să eșueze în tăcere. În acest caz, aplicația Hisense pentru modelul tău, butoanele de pe televizor sau telecomanda originală sunt calea potrivită.'),
      ('Pornește un Hisense de pe telefon', 'La Hisense cu Roku TV, activează „Pornire rapidă TV” la Setări > Sistem > Alimentare. La Google TV, caută o opțiune pentru Wake on LAN sau „Pornire prin rețea”. Dacă nu există, folosește butonul de pornire de pe televizor.'),
      ('Gratis și Pro', 'Săgețile, OK, Înapoi, Acasă, volumul, canalele, tastele numerice, tastatura, deschiderea aplicațiilor, schimbarea intrărilor și pornirea sau oprirea sunt gratuite, fără reclame și fără abonament. Touchpadul, comenzile vocale, aplicațiile favorite, rutinele și temporizatorul de oprire fac parte din Mando TV Pro, o achiziție unică fără abonament.'),
    ],
    marca=None,
    faq=[
      ('Funcționează Mando TV cu Hisense VIDAA?', 'Da, cu majoritatea modelelor VIDAA. Unele mai noi acceptă doar aplicația oficială Hisense; Mando TV observă asta și îți spune. Televizoarele Hisense cu Roku TV, Google TV sau Fire TV sunt de asemenea acceptate.'),
      ('Cum știu dacă Hisense-ul meu este Roku TV, Google TV sau Fire TV?', 'Uită-te la ecranul de start. Roku TV are o grilă simplă de dale și o siglă Roku la pornire. Google TV are rânduri cu recomandări. Fire TV are ecranul de start Amazon Fire TV. Numele modelului de la Setări > Despre îți spune și el.'),
      ('Am nevoie de cont Hisense sau Google?', 'Nu. Mando TV se conectează direct prin Wi-Fi-ul tău de acasă și nu are cont propriu.'),
    ]),
  dict(clave='philips', corto='Telecomandă Philips', fecha='2026-11-23',
    titulo='Aplicație telecomandă Philips: Roku TV, Google TV, Android TV',
    desc='Mando TV controlează televizoare Philips cu Roku TV, Google TV sau Android TV prin Wi-Fi, de pe telefon sau PC. Titan OS nu este acceptat.',
    h1='Controlează televizorul Philips cu telefonul',
    intro='Televizoarele Philips folosesc sisteme diferite în funcție de țară și de anul fabricației: Roku TV în SUA, Google TV sau Android TV în multe țări și Titan OS la unele modele europene mai noi. Mando TV controlează modelele cu Roku TV, Google TV și Android TV prin Wi-Fi.',
    pasos=[
      'Verifică ecranul de start. Roku TV arată o grilă de dale. Google TV și Android TV arată rânduri de recomandări de la Google. Titan OS are un ecran de start propriu.',
      'Conectează telefonul și televizorul la același Wi-Fi.',
      'Deschide Mando TV și atinge în listă televizorul tău Philips.',
      'Roku TV nu cere nimic. Google TV și Android TV arată un cod de 6 caractere: introdu-l o singură dată în aplicație.',
      'Folosește săgețile, OK, Înapoi, Acasă, volumul și tastatura.',
    ],
    extra=[
      ('Philips Roku TV', 'Funcționează ca orice televizor Roku. Ca să-l pornești de pe telefon, activează „Pornire rapidă TV” la Setări > Sistem > Alimentare. Mai mult pe pagina [Aplicație telecomandă Roku](@roku).'),
      ('Philips cu Google TV sau Android TV', 'Include multe modele Ambilight. Se asociază cu codul de pe ecran. Ca să le pornești de pe telefon, caută în setările de rețea sau de alimentare Wake on LAN sau „Pornire prin rețea”. La unele modele opțiunea lipsește. Mai mult pe pagina [Aplicație telecomandă Android TV](@android).'),
      ('Televizoare Philips mai vechi, fără Android', 'Televizoarele Philips din 2011 până în 2015 care nu folosesc Android sunt acceptate în Mando TV în versiune beta. Este nouă și nu are nevoie de cod de asociere.'),
      ('Philips cu Titan OS', 'Titan OS este un alt sistem, pe care Mando TV nu îl controlează astăzi, și preferăm să spunem asta clar. Nici modelele Philips mai noi fără Android nu sunt acoperite.'),
      ('Gratis și Pro', 'Telecomanda o poți descărca și folosi gratuit, fără reclame și fără abonament. Mando TV Pro este o achiziție unică opțională pentru extra.'),
    ],
    marca=None,
    faq=[
      ('Funcționează Mando TV cu televizoarele Philips?', 'Cu televizoarele Philips care folosesc Roku TV, Google TV sau Android TV, da, iar în versiune beta cu televizoarele Philips din 2011 până în 2015 fără Android. Modelele cu Titan OS nu sunt acceptate.'),
      ('Controlează Mando TV Ambilight?', 'Mando TV este o telecomandă: trimite butoanele, așa că ajungi cu săgețile și OK la setările Ambilight. Nu există comenzi separate pentru Ambilight.'),
      ('Am nevoie de cont Philips sau Google?', 'Nu. Mando TV se conectează prin Wi-Fi-ul tău de acasă și nu cere cont.'),
    ]),
]
OTRAS_GUIAS += [
  ('no-sub', 'O aplicație de telecomandă fără abonament și fără reclame'),
  ('roku-app-alt', 'Alternativă la aplicația Roku: una pentru toate televizoarele'),
  ('lg-thinq', 'Alternativă la aplicația LG ThinQ pentru televizorul tău LG'),
  ('smartthings', 'Alternativă la SmartThings pentru televizoare Samsung'),
  ('googletv-alt', 'Alternativă la telecomanda Google TV de pe telefon'),
  ('windows', 'Aplicație de telecomandă pentru PC cu Windows'),
  ('iphone', 'Aplicație de telecomandă pentru iPhone: una pentru toate televizoarele'),
  ('firetv', 'Telecomandă Fire TV pentru telefon sau PC'),
  ('firetv-lost', 'Telecomandă Fire TV pierdută: folosește telefonul'),
  ('turn-on', 'Cum pornești un televizor fără telecomandă'),
  ('sony', 'Cum controlezi televizorul Sony cu telefonul'),
  ('tcl', 'Cum controlezi televizorul TCL cu telefonul'),
  ('hisense', 'Aplicație telecomandă Hisense: ce merge și ce nu'),
  ('philips', 'Controlează televizorul Philips cu telefonul'),
]
# <<< guías traídas del inglés
