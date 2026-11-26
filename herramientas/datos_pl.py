# Textos en polaco (forma directa, Ty) de mandotv.app. Los usa generar_idiomas.py. Escritos para las búsquedas de Polonia.
# Las claves de las páginas (lg, lost-tv, ...) y sus rutas están en idiomas_sitio.py y en rutas/pl.json.
# Los nombres de menús de cada marca (LG, Samsung, Roku, Android TV, iPhone) son los mismos que usa la app en polaco
# (lib/l10n/app_pl.arb del proyecto de la app).

UI = dict(
  locale='pl_PL',
  aria_home='Mando TV, strona główna', aria_main='Menu główne', nav_que='Funkcje', nav_ayuda='Pomoc', nav_contacto='Kontakt',
  asunto='Witaj%20Mando%20TV', inicio='Strona główna', privacidad='Prywatność', aria_pie='Stopka', aria_ruta='Ścieżka nawigacji',
  aria_marcas='Marki i poradniki', hecho='Stworzone w Chile',
  aviso='Mando TV to niezależna aplikacja. Nie jest powiązana z wymienionymi producentami telewizorów ani z Google, Amazon, Apple czy Roku i nie jest przez nich wspierana. Marki należą do ich właścicieli i są wymieniane wyłącznie po to, by wskazać zgodność. Android TV i Google TV to znaki towarowe Google LLC. Apple TV to znak towarowy Apple Inc.',
  bajar='Pobierz za darmo', descarga='Pobierz z', anticipada='Wczesny dostęp w',
  apple_aria='Pobierz Mando TV za darmo z App Store', ms_aria='Pobierz Mando TV za darmo z Microsoft Store',
  gp_aria='Wczesny dostęp do Mando TV w Google Play na Androida', aria_desc='Pobierz Mando TV',
  b_como_btn='Jak się połączyć', b_tiendas_label='Dostępne w sklepach',
  b_nota='iPhone, iPad, Mac, Android i Windows. Darmowe pobieranie, bez reklam. Pro to jednorazowy zakup, bez subskrypcji.',
  b_compat='Zgodne telewizory', b_otras='Inne marki', b_otras_p='Mando TV steruje wszystkimi tymi markami jedną aplikacją:',
  g_guias='Poradniki', g_ver='Zobacz kroki', g_pasos='Krok po kroku', g_hazlo='Jak to zrobić z Mando TV',
  g_tiendas='Mando TV to uniwersalny pilot do Twojego telewizora. Pobierz go za darmo, bez reklam i bez konta. Pro to opcjonalny jednorazowy zakup, bez subskrypcji. Na iPhone, iPad, Windows i Androida:',
  g_nota='Android: darmowy wczesny dostęp w Google Play. <a href="{enlace}">Dołącz w dwóch krokach</a> i pomóż nam dotrzeć do sklepu.',
  g_mas_pagina='Więcej szczegółów znajdziesz na stronie {enlace}.', g_mas_marca='Więcej szczegółów według marki:',
  g_faq='Najczęstsze pytania', g_mas='Więcej poradników', g_todas='Wszystkie poradniki', g_ayuda='Pomoc i wsparcie',
  g_idiomas='Ten poradnik w innych językach',
)

# Pie de página y listas de marcas/guías: (clave, texto)
PIE = [
  ('samsung', 'Pilot Samsung'),
  ('lg', 'Pilot LG'),
  ('roku', 'Pilot Roku'),
  ('android', 'Pilot Android TV'),
  ('guias', 'Wszystkie poradniki'),
  ('lost-tv', 'Zgubiony pilot'),
  ('lost-lg', 'Zgubiony pilot LG'),
  ('lg-on', 'Włączanie telewizora LG telefonem'),
  ('hdmi', 'Zmiana wejścia HDMI bez pilota'),
  ('androidtv', 'Android TV bez pilota'),
  ('console', 'Telewizor i konsola HDMI bez pilota'),
  ('samsung-lost', 'Telewizor Samsung bez pilota'),
  ('roku-lost', 'Zgubiony pilot Roku'),
  ('roku-403', 'Aplikacja Roku nie działa'),
  ('androidtv-code', 'Kod parowania Android TV'),
  ('not-found', 'Telefon nie widzi telewizora'),
  ('wifi', 'Telefon jako pilot przez Wi-Fi'),
  ('pc', 'Sterowanie telewizorem z komputera'),
]
NOMBRE_OTRA = {'lg': 'Aplikacja pilot do LG', 'samsung': 'Aplikacja pilot do Samsung', 'roku': 'Aplikacja pilot do Roku',
               'android': 'Aplikacja pilot do Android TV i Google TV'}
PAGINA_MARCA = {'lg': 'Aplikacja pilot do LG', 'samsung': 'Aplikacja pilot do Samsung', 'roku': 'Aplikacja pilot do Roku',
                'android': 'Aplikacja pilot do Android TV'}

OTRAS_GUIAS = [
  ('lg-on', 'Jak włączyć telewizor LG telefonem'),
  ('lost-tv', 'Zgubiony pilot do telewizora: co możesz zrobić'),
  ('lost-lg', 'Zgubiony pilot LG: jak użyć telefonu'),
  ('hdmi', 'Jak zmienić wejście HDMI w telewizorze bez pilota'),
  ('androidtv', 'Android TV bez pilota: jak użyć telefonu'),
  ('console', 'Jak włączyć telewizor i przełączyć na HDMI konsoli bez pilota'),
  ('samsung-lost', 'Telewizor Samsung bez oryginalnego pilota: jak użyć telefonu'),
  ('roku-lost', 'Zgubiony pilot Roku: jak użyć telefonu'),
  ('roku-403', 'Aplikacja Roku nie działa: jak naprawić błąd 403'),
  ('androidtv-code', 'Android TV prosi o kod parowania: co zrobić'),
  ('not-found', 'Telefon nie widzi telewizora: co sprawdzić'),
  ('wifi', 'Jak używać telefonu jako pilota przez Wi-Fi'),
  ('pc', 'Jak sterować telewizorem z komputera z Windows'),
]

INDICE = dict(
  titulo='Poradniki: sterowanie telewizorem z telefonu | Mando TV',
  desc='Poradniki krok po kroku: telefon lub komputer jako pilot, włączanie telewizora, zmiana HDMI i rozwiązywanie problemów z Samsung, LG i Roku.',
  h1='Poradniki: telefon jako pilot do telewizora',
  intro='Proste kroki, które pomogą Ci połączyć pilota do telewizora Samsung, LG, Roku lub Android TV z Mando TV, włączyć telewizor i rozwiązać problemy.',
  h2_guias='Wszystkie poradniki', h2_marcas='Aplikacja pilot według marki',
  marcas_extra=[('sony', 'Pilot Sony'), ('philips', 'Pilot Philips')],
)

MARCAS = [
  dict(clave='lg', color='#e0457b', corto='LG',
    titulo='Pilot do telewizora LG na telefon, za darmo | Mando TV',
    desc='Telefon lub komputer jako pilot do telewizora LG z webOS, przez Wi-Fi. Przyciski, klawiatura, aplikacje, źródła i włączanie za darmo; wskaźnik w Pro.',
    h1='Pilot do telewizora LG jako aplikacja na telefon',
    intro='Mando TV to aplikacja pilot do telewizorów LG: zamienia Twój telefon lub komputer w pilota do smart TV LG z webOS, przez domową sieć Wi-Fi. Przydaje się, gdy zgubisz pilota, wyczerpią się baterie albo po prostu chcesz szybciej pisać.',
    compat='Smart TV LG z webOS (większość modeli smart TV LG od 2014 roku). Działa z telewizorami LED, NanoCell, QNED i OLED. Starsze smart TV LG z NetCast (od 2011 do 2014, przed webOS) są nowością w wersji beta: parują się 6-cyfrowym kluczem, który pokazuje telewizor.',
    h2=dict(funciones='Co możesz zrobić ze swoim telewizorem LG', como='Jak połączyć telewizor LG z Mando TV',
            encender='Włączanie telewizora LG telefonem', preguntas='Pytania o LG', guias='Poradniki dla LG'),
    funciones=[
      ('Wszystkie przyciski', 'Krzyżak kierunkowy, OK, Wstecz, Ekran główny, głośność, kanały, wyciszenie i odtwarzanie.'),
      ('Wskaźnik jak w Magic Remote (Pro)', 'Poruszaj strzałką po ekranie palcem, dokładnie jak w pilocie LG Magic Remote.'),
      ('Klawiatura', 'Pisz w YouTube, Netflix lub w przeglądarce telewizora na klawiaturze telefonu.'),
      ('Aplikacje i źródła', 'Otwieraj swoje aplikacje i przełączaj na HDMI, telewizję na żywo, AirPlay lub Screen Share.'),
      ('Wyjście audio (Pro)', 'Przełączaj dźwięk między głośnikami telewizora a soundbarem.'),
      ('Włączanie telewizora', 'Gdy jest wyłączony, Mando TV włącza go przez sieć i łączy się samo.'),
    ],
    pasos=[
      'Połącz telefon i telewizor z tą samą siecią Wi-Fi.',
      'Otwórz Mando TV: Twój telewizor LG sam pojawi się na liście. Stuknij go.',
      'Na telewizorze pojawi się prośba o zgodę. Zaakceptuj ją zwykłym pilotem (tylko za pierwszym razem).',
    ],
    encender='W telewizorze LG otwórz Ustawienia i znajdź opcję „Włącz TV przez urządzenie mobilne” (znajdziesz ją w Ogólne > Urządzenia > Urządzenia zewnętrzne, w starszych modelach w Połączenie > Zarządzanie połączeniem mobilnym). Włącz „Włącz przez Wi-Fi”. Jeśli jest „Quick Start+”, włącz też tę opcję. Potem, gdy stukniesz wyłączony telewizor w Mando TV, aplikacja zapyta, czy go włączyć, i połączy się sama.',
    faq=[
      ('Czy potrzebuję pilota Magic Remote, żeby używać Mando TV?', 'Tylko za pierwszym razem, żeby zaakceptować prośbę na ekranie. Potem wystarczy Twój telefon.'),
      ('Czy Mando TV zastępuje aplikację LG ThinQ?', 'Do sterowania telewizorem tak: nie potrzebujesz konta LG ani rejestracji telewizora. Mando TV łączy się bezpośrednio przez Twoją sieć Wi-Fi.'),
      ('Czy mogę włączyć telewizor LG telefonem?', 'Tak, jeśli w telewizorze włączysz „Włącz TV przez urządzenie mobilne” i raz połączysz się z nim, gdy jest włączony.'),
      ('Czy działa ze starszymi telewizorami LG sprzed webOS?', 'W wersji beta tak, ze smart TV LG NetCast z lat 2011 do 2014. Parują się 6-cyfrowym kluczem, który pokazuje telewizor. Funkcja jest nowa i może mieć jeszcze niedociągnięcia.'),
    ],
    guias=[('lg-on', 'Jak włączyć telewizor LG telefonem'),
           ('lost-lg', 'Zgubiony pilot LG: jak użyć telefonu'),
           ('hdmi', 'Jak zmienić wejście HDMI w telewizorze bez pilota'),
           ('guias', 'Wszystkie poradniki o sterowaniu telewizorem z telefonu')]),
  dict(clave='samsung', color='#3d7bff', corto='Samsung',
    titulo='Pilot do telewizora Samsung na telefon | Mando TV',
    desc='Telefon lub komputer jako pilot do telewizora Samsung z Tizen, przez Wi-Fi. Przyciski, klawiatura, aplikacje i włączanie za darmo; touchpad w Pro. Bez reklam.',
    h1='Pilot do telewizora Samsung jako aplikacja na telefon',
    intro='Mando TV to aplikacja pilot do telewizorów Samsung: zamienia Twój telefon lub komputer w pilota do smart TV Samsung przez domową sieć Wi-Fi. Nie potrzebujesz konta Samsung ani rejestracji telewizora.',
    compat='Smart TV Samsung z Tizen, rocznik 2016 i nowsze (serie takie jak Crystal UHD, QLED, Neo QLED, The Frame i OLED).',
    h2=dict(funciones='Co możesz zrobić ze swoim telewizorem Samsung', como='Jak połączyć telewizor Samsung z Mando TV',
            encender='Włączanie telewizora Samsung telefonem', preguntas='Pytania o Samsung', guias='Poradniki dla Samsung'),
    funciones=[
      ('Wszystkie przyciski', 'Krzyżak kierunkowy, OK, Wstecz, Ekran główny, głośność, kanały, wyciszenie i źródło.'),
      ('Touchpad (Pro)', 'Przesuwaj palcem po menu, bez szukania strzałek.'),
      ('Klawiatura', 'Wpisuj wyszukiwane hasła i hasła do kont na klawiaturze telefonu.'),
      ('Aplikacje', 'Otwieraj Netflix, YouTube, Prime Video i inne aplikacje jednym stuknięciem.'),
      ('Włączanie telewizora', 'Gdy jest wyłączony, Mando TV włącza go przez sieć i łączy się samo.'),
      ('Bez konta', 'Połączenie idzie bezpośrednio przez Twoją sieć Wi-Fi, bez pośrednictwa internetu.'),
    ],
    pasos=[
      'Połącz telefon i telewizor z tą samą siecią Wi-Fi.',
      'Otwórz Mando TV: Twój telewizor Samsung sam pojawi się na liście. Stuknij go.',
      'Telewizor zapyta, czy zezwalasz na połączenie. Pilotem wybierz „Zezwól” (tylko za pierwszym razem).',
    ],
    encender='W telewizorze Samsung otwórz Ustawienia > Ogólne > Sieć > Ustawienia ekspertów i włącz „Włączanie przez urządzenie mobilne”. Potem, gdy stukniesz wyłączony telewizor w Mando TV, aplikacja zapyta, czy go włączyć, i połączy się sama.',
    faq=[
      ('Zgoda została odrzucona przez pomyłkę. Co robić?', 'W telewizorze otwórz Ustawienia > Ogólne > Menedżer urządzeń zewnętrznych > Menedżer połączeń urządzeń i ustaw Mando TV jako dozwolone.'),
      ('Czy Mando TV zastępuje SmartThings?', 'Do sterowania telewizorem tak, i to bez konta Samsung. Mando TV łączy się bezpośrednio przez Twoją sieć Wi-Fi.'),
      ('Czy działa ze starszymi telewizorami Samsung?', 'Działa z telewizorami Samsung z Tizen, rocznik 2016 i nowsze. Wcześniejsze modele używają innego systemu, którego jeszcze nie obsługujemy.'),
    ],
    guias=[('samsung-lost', 'Telewizor Samsung bez oryginalnego pilota: jak użyć telefonu'),
           ('smartthings', 'Alternatywa dla SmartThings'),
           ('turn-on', 'Włączanie telewizora bez pilota'),
           ('hdmi', 'Jak zmienić wejście HDMI w telewizorze bez pilota'),
           ('guias', 'Wszystkie poradniki o sterowaniu telewizorem z telefonu')]),
  dict(clave='roku', color='#a77bff', corto='Roku',
    titulo='Pilot Roku na telefon, za darmo | Mando TV',
    desc='Telefon lub komputer jako pilot do Roku TV i odtwarzaczy Roku, przez Wi-Fi. Przyciski, klawiatura, kanały, źródła i włączanie za darmo.',
    h1='Pilot Roku jako aplikacja na telefon',
    intro='Mando TV to aplikacja pilot do Roku: zamienia Twój telefon lub komputer w pilota do Roku przez domową sieć Wi-Fi. Działa z telewizorami Roku TV i z odtwarzaczami Roku podłączanymi do portu HDMI.',
    compat='Telewizory Roku TV (TCL, Hisense, Philips, Sharp, JVC i inne) oraz odtwarzacze Roku (Express, Streaming Stick, Ultra).',
    h2=dict(funciones='Co możesz zrobić ze swoim Roku', como='Jak połączyć Roku z Mando TV',
            encender='Włączanie Roku telefonem', preguntas='Pytania o Roku', guias='Poradniki dla Roku'),
    funciones=[
      ('Wszystkie przyciski', 'Krzyżak kierunkowy, OK, Wstecz, Ekran główny, głośność, wyciszenie, powtórka i odtwarzanie.'),
      ('Klawiatura', 'Wpisuj wyszukiwane hasła w kanałach Roku na klawiaturze telefonu.'),
      ('Kanały', 'Otwieraj Netflix, YouTube i inne kanały Roku jednym stuknięciem.'),
      ('Źródła', 'W Roku TV przełączaj w aplikacji na HDMI, antenę lub AV.'),
      ('Włączanie telewizora', 'W telewizorach Roku TV z szybkim uruchamianiem Mando TV włącza je z Twojego telefonu.'),
      ('Bez parowania', 'Roku nie prosi o kod: stuknij go na liście i jesteś połączony.'),
      ('Znajdź mój pilot', 'Jeśli Twój pilot Roku ma głośnik, jak Roku Voice Remote Pro, Mando TV sprawi, że zadzwoni, żebyś go znalazł. Za darmo, Roku musi być włączone.'),
    ],
    pasos=[
      'Połącz telefon i Roku z tą samą siecią Wi-Fi.',
      'Otwórz Mando TV: Twoje Roku samo pojawi się na liście. Stuknij je.',
      'Jeśli połączenie się nie uda, w Roku otwórz Ustawienia > System > Zaawansowane ustawienia systemu > Sterowanie przez aplikacje mobilne i ustaw Dostęp do sieci na Domyślny lub Zezwalający (w nowszym oprogramowaniu Roku ustaw „Sterowanie przez aplikacje mobilne” na Włączone).',
    ],
    encender='W telewizorach Roku TV otwórz Ustawienia > System > Zasilanie i włącz „Szybkie uruchamianie TV”. Odtwarzaczy Roku podłączonych do innego telewizora nie da się w ten sposób włączyć. Potem, gdy stukniesz wyłączony telewizor w Mando TV, aplikacja zapyta, czy go włączyć, i połączy się sama.',
    faq=[
      ('Czy działa z Roku Express lub Streaming Stick?', 'Tak. Wszystkie odtwarzacze Roku i telewizory Roku TV steruje się w ten sam sposób.'),
      ('Mando TV nie znajduje mojego Roku. Co robić?', 'Sprawdź, czy oba urządzenia są w tej samej sieci Wi-Fi i czy w Roku nie jest wyłączone „Sterowanie przez aplikacje mobilne”. Możesz też dodać je po adresie IP.'),
      ('Czy potrzebuję konta Roku?', 'Nie. Mando TV łączy się bezpośrednio przez Twoją sieć Wi-Fi.'),
    ],
    guias=[('roku-403', 'Aplikacja Roku nie działa (błąd 403)'),
           ('roku-lost', 'Zgubiony pilot Roku: jak użyć telefonu'),
           ('tcl', 'Pilot TCL'),
           ('hisense', 'Pilot Hisense'),
           ('philips', 'Pilot Philips'),
           ('guias', 'Wszystkie poradniki o sterowaniu telewizorem z telefonu')]),
  dict(clave='android', color='#2fbf8f', corto='Android TV i Google TV',
    titulo='Pilot do Android TV na telefon | Mando TV',
    desc='Telefon lub komputer jako pilot do Android TV (Sony, TCL, Xiaomi), przez Wi-Fi. Przyciski, klawiatura, aplikacje i włączanie za darmo; touchpad w Pro.',
    h1='Pilot do Android TV jako aplikacja na telefon',
    intro='Mando TV to aplikacja pilot do Android TV: zamienia Twój telefon lub komputer w pilota do telewizora z Android TV lub Google TV przez domową sieć Wi-Fi. Działa też z iPhone i z Windows.',
    compat='Telewizory z Google TV lub Android TV marek Sony, Philips, TCL, Hisense, Sharp, Xiaomi, Toshiba, Panasonic, Haier, Skyworth, JVC, Thomson, Motorola, OnePlus, iFFALCON, Kogan, Vu i innych, a także Chromecast z Google TV, Google TV Streamer, onn. i Nvidia Shield. Niektóre z tych marek sprzedają też modele z innym systemem: jeśli Twój telewizor pokazuje ekran główny Google TV albo ma sklep Google Play, Mando TV nim steruje.',
    h2=dict(funciones='Co możesz zrobić ze swoim Android TV', como='Jak połączyć Android TV z Mando TV',
            encender='Włączanie Android TV telefonem', preguntas='Pytania o Android TV', guias='Poradniki dla Android TV'),
    funciones=[
      ('Wszystkie przyciski', 'Krzyżak kierunkowy, OK, Wstecz, Ekran główny, głośność, wyciszenie i odtwarzanie.'),
      ('Touchpad (Pro)', 'Przesuwaj palcem, żeby szybko poruszać się po menu Google TV.'),
      ('Klawiatura', 'Wpisuj wyszukiwane hasła i hasła do kont na klawiaturze telefonu.'),
      ('Aplikacje', 'Otwieraj YouTube, Netflix, Disney+ i inne aplikacje jednym stuknięciem.'),
      ('Włączanie telewizora', 'W modelach z włączaniem przez sieć Mando TV włącza telewizor i łączy się samo.'),
      ('iPhone, Android i komputer', 'Działa tak samo na każdym telefonie i komputerze.'),
    ],
    pasos=[
      'Połącz telefon i telewizor z tą samą siecią Wi-Fi.',
      'Otwórz Mando TV: Twój Android TV sam pojawi się na liście. Stuknij go.',
      'Telewizor pokaże 6-znakowy kod. Wpisz go w Mando TV (tylko za pierwszym razem).',
    ],
    encender='To zależy od producenta. W ustawieniach sieci lub zasilania poszukaj opcji „Wake on LAN”, „Włączanie przez sieć”, „Network standby” albo „Remote start”. Niektóre modele nie mają tej opcji. Potem, gdy stukniesz wyłączony telewizor w Mando TV, aplikacja zapyta, czy go włączyć, i połączy się sama.',
    faq=[
      ('Czy działa z Chromecast z Google TV?', 'Tak, parowanie odbywa się 6-znakowym kodem, który pojawia się na ekranie.'),
      ('Czym różni się od aplikacji Google TV?', 'Mando TV nie wymaga konta Google, działa też w Windows i steruje telewizorami LG, Samsung i Roku tą samą aplikacją.'),
      ('Kod nie pojawia się na ekranie. Co robić?', 'Zamknij Mando TV, otwórz aplikację ponownie i jeszcze raz stuknij telewizor. Sprawdź, czy telewizor nie jest w głębokim trybie oszczędzania energii.'),
    ],
    guias=[('androidtv-code', 'Android TV prosi o kod parowania: co zrobić'),
           ('androidtv', 'Android TV bez pilota: jak użyć telefonu'),
           ('googletv-alt', 'Alternatywa dla pilota Google TV'),
           ('sony', 'Pilot Sony'),
           ('tcl', 'Pilot TCL'),
           ('hisense', 'Pilot Hisense'),
           ('philips', 'Pilot Philips'),
           ('guias', 'Wszystkie poradniki o sterowaniu telewizorem z telefonu')]),
]

GUIAS = [
  dict(clave='lost-tv', corto='Zgubiony pilot',
    titulo='Zgubiony pilot do TV? Steruj telewizorem z telefonu',
    desc='Zgubiony pilot do telewizora? Włącz telewizor przyciskiem na obudowie i użyj telefonu jako pilota. Kroki dla LG, Samsung, Roku, Android TV. Za darmo.',
    h1='Zgubiony pilot do telewizora? Co możesz zrobić teraz',
    intro='Zgubiony pilot zdarza się w każdym domu: znika akurat wtedy, gdy chcesz coś obejrzeć. Dobra wiadomość: Twój telefon może go zastąpić przez domową sieć Wi-Fi. Oto, co możesz zrobić po kolei.',
    pasos=[
      'Włącz telewizor przyciskiem na obudowie. Prawie zawsze jest na dole pośrodku albo z tyłu, blisko rogu. Czasem to pojedynczy przycisk, czasem mały joystick.',
      'Połącz telefon z tą samą siecią Wi-Fi co telewizor.',
      'Pobierz Mando TV, które jest darmowe i nie wymaga konta, i otwórz aplikację. Twój telewizor sam pojawi się na liście. Stuknij go.',
      'Potwierdź połączenie dla swojej marki. W LG i Samsung telewizor pokaże prośbę: zaakceptuj ją przyciskiem lub joystickiem na samym telewizorze. W Android TV i Google TV wpisz 6-znakowy kod widoczny na ekranie. Roku o nic nie pyta.',
      'Gotowe. Strzałki, OK, Wstecz, Ekran główny, głośność, kanały i klawiatura są darmowe.',
      'Na przyszłość: włącz w ustawieniach telewizora włączanie przez sieć (poradnik dla Twojej marki znajdziesz niżej). Wtedy telewizor włączysz z telefonu, bez dotykania go.',
    ],
    extra=[
      ('Wybierz poradnik dla swojej marki', 'LG: [Zgubiony pilot LG](@lost-lg). Android TV i Google TV: [Android TV bez pilota](@androidtv). Samsung: [Telewizor Samsung bez pilota](@samsung-lost). Roku: [Zgubiony pilot Roku](@roku-lost).'),
      ('Jeśli telewizor nie włącza się przyciskiem', 'Zanim zaczniesz szukać innego pilota, sprawdź, czy kabel jest dobrze wpięty, a w gniazdku jest prąd. Jeśli przycisk na telewizorze nic nie robi, problem jest w telewizorze, a nie w pilocie.'),
      ('Jeśli pilot po prostu przestał działać', 'Spróbuj z nowymi bateriami. Czy pilot jeszcze nadaje sygnał, sprawdzisz tak: skieruj go na aparat telefonu i naciśnij przycisk. W wielu telefonach zobaczysz na ekranie fioletowe światło. Jeśli je widzisz, a telewizor nie reaguje, możliwe, że czujnik w telewizorze jest zasłonięty.'),
      ('Jeśli zmieniłeś router i telewizor nie ma Wi-Fi', 'Bez pilota trudniej połączyć telewizor z nową siecią. Najłatwiej podłączyć telewizor kablem sieciowym do routera. Możesz też ustawić sieć Wi-Fi o tej samej nazwie i haśle co wcześniej: telewizor zwykle sam się z nią połączy.'),
      ('Co jest darmowe, a co w Pro', 'Włączanie i wyłączanie telewizora, strzałki, OK, głośność, kanały, klawisze cyfr, klawiatura, otwieranie aplikacji i zmiana źródła są darmowe. Touchpad, głos i rutyny należą do Mando TV Pro, jednorazowego zakupu bez subskrypcji.'),
    ],
    marca=None,
    faq=[
      ('Czy mogę włączyć telewizor telefonem, jeśli nigdy go nie łączyłem?', 'Za pierwszym razem włącz go przyciskiem na telewizorze. Gdy połączysz telefon i włączysz w ustawieniach telewizora włączanie przez sieć, będziesz mógł go włączać z aplikacji.'),
      ('Czy muszę kupić nowego pilota?', 'Niekoniecznie. Z Mando TV przyciski, głośność, klawiaturę i włączanie masz za darmo. Jeśli mimo to wolisz prawdziwego pilota, wyszukaj dokładny model swojego telewizora.'),
      ('Czy działa, gdy telewizor nie ma Wi-Fi?', 'Zwykle nie. Telefon i telewizor zazwyczaj muszą być w tej samej sieci Wi-Fi. Wyjątkiem jest podczerwień w telefonach z Androidem z nadajnikiem podczerwieni, która steruje też telewizorami bez funkcji smart TV, oraz Bluetooth w wersji beta od Androida 9, który działa bez Wi-Fi z Google TV, Android TV i Fire TV.'),
    ]),
  dict(clave='lost-lg', corto='Zgubiony pilot LG',
    titulo='Zgubiony pilot LG? Użyj telefonu jako pilota',
    desc='Nie masz pilota LG? Włącz telewizor przyciskiem na obudowie, zaakceptuj prośbę i steruj telefonem przez Wi-Fi. Bez konta LG, bez reklam.',
    h1='Zgubiony pilot LG? Jak użyć telefonu',
    intro='Jeśli zgubiłeś pilota LG albo Magic Remote przestał działać, Twój telefon zastąpi go przez Wi-Fi. Działa z telewizorami LG z webOS, czyli z prawie każdym smart TV LG od 2014 roku. Nie potrzebujesz konta LG ani aplikacji ThinQ.',
    pasos=[
      'Włącz telewizor przyciskiem pod logo LG albo przyciskiem z tyłu. W wielu modelach to joystick: naciśnij go, żeby otworzyć menu, i przesuń, żeby coś wybrać.',
      'Połącz telefon z tą samą siecią Wi-Fi co telewizor.',
      'Otwórz Mando TV i stuknij swój telewizor LG na liście.',
      'Telewizor pokaże prośbę o zgodę. Zaakceptuj ją joystickiem lub przyciskiem na telewizorze. Jeśli ten telefon był już połączony, nie zapyta ponownie.',
      'Gotowe. Strzałki, OK, Wstecz, Ekran główny, głośność, kanały i klawiatura są darmowe. Wskaźnik to funkcja Pro.',
      'Gdy aplikacja jest połączona, strzałkami i OK wejdź w Ustawienia i włącz „Włącz TV przez urządzenie mobilne”. Poradnik [Jak włączyć telewizor LG telefonem](@lg-on) pokazuje, gdzie jest ta opcja.',
    ],
    extra=[
      ('Jeśli telewizor nie pokazuje prośby', 'Możliwe, że zgoda jest już zapisana albo Twój telefon jest w innej sieci. Sprawdź, czy oba urządzenia są w tej samej sieci Wi-Fi i czy VPN jest wyłączony. Jeśli telewizor nie pojawia się na liście, pomoże Ci [Telefon nie widzi telewizora](@not-found).'),
      ('Jeśli telewizor stracił Wi-Fi', 'Podłącz telewizor kablem sieciowym do routera, a użyje go sam. Albo ustaw sieć Wi-Fi o tej samej nazwie i haśle co wcześniej, bo telewizor zwykle sam się z nią połączy.'),
      ('Jeśli telewizor utknął na innym wejściu', 'Na telefonie stuknij Źródła i wybierz port HDMI. Więcej znajdziesz w poradniku [Jak zmienić wejście HDMI w telewizorze bez pilota](@hdmi).'),
    ],
    marca='lg',
    faq=[
      ('Czy potrzebuję pilota Magic Remote, żeby używać Mando TV?', 'Potrzebujesz czegoś tylko za pierwszym razem, żeby zaakceptować prośbę, i wystarczy do tego przycisk lub joystick na samym telewizorze. Potem używasz już tylko telefonu.'),
      ('Czy potrzebuję aplikacji LG ThinQ?', 'Nie. Mando TV łączy się bezpośrednio przez Twoją sieć Wi-Fi i nie wymaga konta LG.'),
      ('Czy mogę wyłączać i włączać telewizor LG telefonem?', 'Wyłączać tak. Żeby go włączać, musisz mieć w telewizorze włączone „Włącz TV przez urządzenie mobilne” i raz się połączyć, gdy telewizor był włączony.'),
    ]),
  dict(clave='hdmi', corto='Zmiana HDMI bez pilota',
    titulo='Zmiana wejścia HDMI bez pilota (Samsung, LG, Roku)',
    desc='Jak zmienić wejście HDMI bez pilota w Samsung, LG lub Roku: przyciskiem na telewizorze albo telefonem. Na start za darmo, bez reklam.',
    h1='Jak zmienić wejście HDMI w telewizorze bez pilota',
    intro='Konsola albo odtwarzacz są gotowe, ale telewizor utknął na innym wejściu, a pilota nigdzie nie widać. Żeby zmienić wejście HDMI bez pilota, masz dwie możliwości: przycisk na samym telewizorze albo telefon. Oto kroki dla Samsung, LG i Roku.',
    pasos=[
      'Najpierw wypróbuj to, co najprostsze: włącz konsolę albo odtwarzacz. Jeśli w telewizorze jest włączone HDMI-CEC (w Samsung nazywa się Anynet+, w LG SIMPLINK), sam przełączy się na to wejście.',
      'Jeśli się nie przełączy, użyj przycisku na samym telewizorze, na dole pośrodku albo z tyłu. W wielu telewizorach Samsung i LG to joystick, który otwiera menu z pozycją Źródło lub Źródła.',
      'W tym menu wybierz wejście: HDMI 1, HDMI 2 i tak dalej. Numer to port, do którego wpięty jest kabel.',
      'Jeśli wolisz telefon, połącz go z tą samą siecią Wi-Fi, otwórz Mando TV i stuknij swój telewizor.',
      'W LG i Roku stuknij Źródła i wybierz port HDMI. W Samsung przycisk Źródła wysyła do telewizora klawisz Źródło, a Ty wybierasz strzałkami i OK.',
      'Możesz też strzałkami i OK przejść na ekranie głównym telewizora do źródeł. Zależnie od marki i rocznika nazywają się Źródło, Podłączone urządzenia lub Wejścia. W Roku TV to kafelki HDMI na ekranie głównym.',
    ],
    extra=[
      ('Samsung', 'Jeśli w menu przycisku na telewizorze nie ma pozycji Źródło, otwórz telefonem menu ekranu głównego i poszukaj po lewej pozycji Źródło lub Podłączone urządzenia. Sterujesz strzałkami i OK w Mando TV, które są darmowe.'),
      ('LG', 'Naciśnij joystick na telewizorze i znajdź Wejścia. Telefonem możesz też w Mando TV otworzyć listę źródeł i stuknąć właściwe wejście.'),
      ('Roku TV', 'Na ekranie głównym dla każdego wejścia jest kafelek, na przykład HDMI 1 lub HDMI 2. Poruszaj się strzałkami i otwórz go przyciskiem OK, za darmo.'),
      ('Jeśli to telewizor z Android TV lub Google TV', 'W Mando TV nie ma jeszcze listy źródeł dla Android TV. Użyj przycisku wejść na samym telewizorze albo dojdź do źródeł strzałkami i OK z ekranu głównego. Jeśli nie masz pilota i chcesz się połączyć, przeczytaj [Android TV bez pilota](@androidtv).'),
      ('Więcej pomocy', 'Jeśli telewizor w ogóle się nie włącza albo nie wiesz, od czego zacząć, przeczytaj [Zgubiony pilot](@lost-tv). Do grania na konsoli poradnik [Jak włączyć telewizor i przełączyć na HDMI konsoli bez pilota](@console) zawiera trik z HDMI-CEC.'),
    ],
    marca=None,
    faq=[
      ('Czy zmiana wejścia HDMI jest darmowa?', 'Tak. Lista źródeł w Mando TV jest darmowa, tak samo jak włączanie telewizora oraz strzałki, OK i głośność. Do źródeł możesz też dojść przez menu telewizora.'),
      ('Skąd mam wiedzieć, którego wejścia HDMI potrzebuję?', 'Spójrz na porty HDMI w telewizorze: każdy ma numer. Wybierz ten, do którego wpięty jest kabel konsoli lub odtwarzacza.'),
      ('Co jeśli telewizor się nie włącza?', 'Włącz go przyciskiem na obudowie. Jeśli już raz go połączyłeś i włączyłeś włączanie przez sieć, możesz też włączyć go telefonem.'),
    ]),
  dict(clave='androidtv', corto='Android TV bez pilota',
    titulo='Android TV bez pilota: użyj telefonu jako pilota',
    desc='Nie masz pilota do Android TV lub Google TV? Połącz telefon 6-znakowym kodem z ekranu. Za darmo, bez konta, bez reklam.',
    h1='Android TV bez pilota: jak użyć telefonu',
    intro='Jeśli zgubiłeś pilota do Android TV lub Google TV albo wyczerpały się w nim baterie, zastąpi go telefon. Najlepsze jest to, że do połączenia pilot nie jest potrzebny: telewizor pokazuje kod na ekranie, a Ty wpisujesz go w telefonie. Działa z telewizorami Sony, Philips, TCL, Hisense, Sharp i Xiaomi z Android TV, z Chromecast z Google TV i z Nvidia Shield.',
    pasos=[
      'Włącz telewizor przyciskiem na obudowie. Prawie zawsze jest na dole pośrodku albo z tyłu, blisko rogu.',
      'Połącz telefon z tą samą siecią Wi-Fi co telewizor.',
      'Pobierz Mando TV, które jest darmowe i nie wymaga konta Google, i otwórz aplikację. Stuknij swój telewizor na liście.',
      'Telewizor pokaże kod z 6 liter i cyfr. Wpisz go w telefonie i stuknij Sparuj. Pilot nie jest do tego potrzebny.',
      'Teraz możesz używać strzałek, OK, Wstecz, Ekranu głównego, głośności, wyciszenia i klawiatury. Są darmowe, podobnie jak lista aplikacji. Touchpad jest w Pro.',
      'Żeby następnym razem włączyć telewizor z telefonu, poszukaj w ustawieniach sieci lub zasilania opcji „Wake on LAN”, „Włączanie przez sieć”, „Network standby” albo „Remote start”.',
    ],
    extra=[
      ('Jeśli telewizora nie da się włączyć z telefonu', 'Nie każdy Android TV da się włączyć przez sieć; zależy to od producenta i modelu. Jeśli Twój nie ma tej funkcji, włącz go przyciskiem na telewizorze i kontynuuj na telefonie. Wyłączyć możesz go z aplikacji.'),
      ('Chromecast z Google TV, Google TV Streamer i Shield', 'Łączą się w ten sam sposób: ta sama sieć Wi-Fi, stuknij urządzenie na liście i wpisz kod. Jeśli telewizor pokazuje inne wejście, przełącz go na port HDMI, do którego podłączone jest urządzenie, jak opisano w [Jak zmienić wejście HDMI w telewizorze bez pilota](@hdmi).'),
      ('Jeśli kod się nie pojawia albo jest uznawany za błędny', 'Sprawdź, czy telewizor naprawdę jest włączony, a nie w trybie czuwania. Kod zmienia się przy każdej prośbie: działa tylko ostatni. Więcej szczegółów znajdziesz w [Android TV prosi o kod parowania](@androidtv-code).'),
      ('Aplikacja Google czy Mando TV', 'Google ma własną aplikację, do której potrzebujesz konta Google. Mando TV nie wymaga konta, działa też w Windows i steruje telewizorami LG, Samsung i Roku tą samą aplikacją.'),
    ],
    marca='android',
    faq=[
      ('Czy potrzebuję pilota, żeby sparować telefon?', 'Nie. Kod pojawia się na ekranie telewizora, a Ty wpisujesz go w telefonie. Wystarczy włączyć telewizor, w razie potrzeby przyciskiem na obudowie.'),
      ('Czy działa z Hisense?', 'W telewizorach Hisense z Android TV lub Google TV tak. Telewizory Hisense z innym systemem nie są zgodne.'),
      ('Czy mogę pisać na klawiaturze telefonu?', 'Tak. Klawiatura jest darmowa i działa przy wyszukiwaniu w YouTube, Netflix i innych aplikacjach.'),
    ]),
  dict(clave='lg-on', corto='Włączanie LG telefonem',
    titulo='Włączanie telewizora LG telefonem (instrukcja)',
    desc='Włącz telewizor LG telefonem przez Wi-Fi: aktywuj „Włącz TV przez urządzenie mobilne” i użyj Mando TV. Krok po kroku, za darmo.',
    h1='Jak włączyć telewizor LG telefonem',
    intro='Możesz włączyć telewizor LG telefonem, ale najpierw trzeba włączyć jedno ustawienie w telewizorze. Potem telefon włącza telewizor LG przez Twoją sieć Wi-Fi, zupełnie bez pilota. Zajmuje to pięć minut i robisz to tylko raz.',
    pasos=[
      'Połącz telefon i telewizor LG z tą samą siecią Wi-Fi.',
      'W telewizorze otwórz Ustawienia i znajdź „Włącz TV przez urządzenie mobilne”. Znajdziesz ją w Ogólne > Urządzenia > Urządzenia zewnętrzne (w starszych modelach w Połączenie > Zarządzanie połączeniem mobilnym).',
      'Włącz „Włącz przez Wi-Fi”. Jeśli telewizor jest podłączony kablem sieciowym, włącz zamiast tego opcję dla kabla.',
      'Jeśli telewizor ma „Quick Start+”, włącz też tę opcję.',
      'Przy włączonym telewizorze otwórz Mando TV w telefonie i stuknij na liście swój telewizor LG. Zaakceptuj prośbę, która pojawi się na ekranie. W ten sposób aplikacja uczy się go budzić.',
      'Wyłącz telewizor i spróbuj: stuknij telewizor w Mando TV, a aplikacja zapyta, czy go włączyć.',
    ],
    extra=[
      ('Jeśli się nie włącza', 'Telewizor musiał być w tej samej sieci Wi-Fi, gdy był wyłączany. Sprawdź, czy ustawienie nadal jest włączone, a telefon jest w tej samej sieci. Jeśli zmieniłeś router, połącz się ponownie przy włączonym telewizorze.'),
    ],
    marca='lg',
    faq=[
      ('Czy mogę włączyć telewizor LG telefonem, jeśli nigdy go nie łączyłem?', 'Nie. Najpierw musisz w telewizorze włączyć „Włącz TV przez urządzenie mobilne” i raz połączyć się z Mando TV, gdy telewizor jest włączony.'),
      ('Czy potrzebuję aplikacji LG ThinQ?', 'Nie. Mando TV łączy się bezpośrednio przez Twoją sieć Wi-Fi i nie wymaga konta LG.'),
      ('Czy działa przez dane komórkowe?', 'Nie. Telefon i telewizor muszą być w tej samej sieci Wi-Fi.'),
    ]),
  dict(clave='console', corto='Telewizor i konsola bez pilota',
    titulo='Bez pilota? Włącz telewizor i zmień HDMI telefonem',
    desc='Premiera gry i brak pilota? Włącz telewizor i przełącz telefonem na wejście HDMI PS5 lub Xbox. Za darmo, bez reklam.',
    h1='Jak włączyć telewizor i przełączyć bez pilota na wejście HDMI konsoli',
    intro='Premiera GTA VI, konsola gotowa, a pilot zniknął gdzieś między poduszkami sofy. Zdarza się to częściej, niż myślisz. Z Mando TV telefon włącza telewizor i przełącza go przez domową sieć Wi-Fi na wejście Twojej PlayStation lub Xbox.',
    pasos=[
      'Połącz telefon z tą samą siecią Wi-Fi co telewizor.',
      'Otwórz Mando TV i stuknij na liście swój telewizor (Samsung, LG, Roku lub Android TV).',
      'Jeśli telewizor jest wyłączony, stuknij Włącz. Zadziała, jeśli w telewizorze włączone jest włączanie przez sieć. Jeśli nigdy tego nie włączano, włącz telewizor ten jeden raz przyciskiem na obudowie i włącz tę opcję na przyszłość.',
      'Włącz konsolę. Jeśli HDMI-CEC jest włączone (zobacz darmowy trik niżej), telewizor sam przełączy się na jej wejście.',
      'Jeśli się nie przełączy, w Mando TV stuknij Źródła i wybierz port HDMI, do którego wpięta jest konsola: HDMI 1, HDMI 2 i tak dalej.',
      'Do głośności podczas grania używaj dużych przycisków w aplikacji.',
    ],
    extra=[
      ('Darmowy trik: niech konsola sama przełącza telewizor', 'PS5 i Xbox potrafią włączyć telewizor i od razu po uruchomieniu przeskoczyć na swoje wejście HDMI dzięki HDMI-CEC. W PS5 znajdziesz to w Ustawienia > System > HDMI > Włącz łącze urządzeń HDMI. W Xbox otwórz Ustawienia > Ogólne > Opcje telewizora i wyświetlania i poszukaj opcji sterowania urządzeniami. W telewizorze funkcja nazywa się różnie zależnie od marki: Anynet+ w Samsung, SIMPLINK w LG oraz BRAVIA Sync lub sterowanie HDMI w innych.'),
      ('Jeśli telewizor został na innym obrazie', 'Jeśli konsola jest włączona, ale telewizor nadal pokazuje antenę lub aplikację, nie zmienił wejścia. Na telefonie stuknij Źródła i wybierz wejście HDMI konsoli. Możesz też strzałkami i OK dojść do źródeł telewizora albo użyć przycisku na samym telewizorze i wybrać port HDMI. Numer to port, do którego wpiąłeś kabel konsoli.'),
      ('Jeśli to Roku TV', 'Przycisk na telewizorze, zwykle na dole pośrodku albo z tyłu, włącza go. Stamtąd resztę zrobi telefon.'),
    ],
    marca=None,
    faq=[
      ('Czy Mando TV ma coś wspólnego z GTA VI?', 'Nie. Mando TV nie ma żadnego związku z Rockstar Games ani Take-Two. Aplikacja tylko pomaga nie tracić czasu na granie przez to, że nie możesz znaleźć pilota.'),
      ('Czy zmiana wejścia HDMI jest darmowa?', 'Tak. Lista źródeł w Mando TV jest darmowa, tak samo jak włączanie telewizora oraz strzałki, OK i głośność. Możesz też pozwolić konsoli samej zmieniać wejście przez HDMI-CEC.'),
      ('Czy działa z moim telewizorem?', 'Działa z telewizorami Samsung, LG, Roku i Android TV w tej samej sieci Wi-Fi. Jeśli Twój jest innej marki, trik z HDMI-CEC nadal może Ci pomóc.'),
      ('Czy mogę tego użyć do grania w GTA VI (GTA 6) na PS5 lub Xbox?', 'Mando TV nie ingeruje ani w konsolę, ani w grę. Dba tylko o to, żeby telewizor był włączony i działał na właściwym wejściu HDMI, abyś mógł usiąść i grać.'),
    ]),
  dict(clave='samsung-lost', corto='Telewizor Samsung bez pilota',
    titulo='Zgubiony pilot Samsung? Użyj telefonu jako pilota',
    desc='Zgubiony lub zepsuty pilot Samsung? Użyj telefonu przez Wi-Fi jako pilota do telewizorów z Tizen. Prosto z Mando TV, za darmo, bez reklam.',
    h1='Telewizor Samsung bez oryginalnego pilota: jak użyć telefonu',
    intro='Jeśli zgubiłeś pilota Samsung albo przestał działać, możesz użyć telefonu jako pilota przez Wi-Fi. Działa z telewizorami Samsung z Tizen, rocznik 2016 i nowsze.',
    pasos=[
      'Włącz telewizor przyciskiem na obudowie. W większości modeli jest na dole albo z tyłu, czasem jako mały joystick.',
      'Sprawdź, czy telewizor jest połączony z Twoją siecią Wi-Fi, a telefon jest w tej samej sieci.',
      'Otwórz Mando TV w telefonie. Twój telewizor Samsung sam pojawi się na liście. Stuknij go.',
      'Telewizor poprosi o potwierdzenie połączenia. W większości modeli potwierdzisz je przyciskami na telewizorze albo joystickiem z tyłu.',
      'Gotowe, teraz możesz używać telefonu jako pilota. Przyciski, klawiatura i aplikacje są darmowe; touchpad to funkcja Pro.',
      'Żeby następnym razem włączyć telewizor z telefonu, wejdź w Ustawienia > Ogólne > Sieć > Ustawienia ekspertów i włącz „Włączanie przez urządzenie mobilne”.',
    ],
    extra=[
      ('Jeśli telewizor nie pyta o zgodę', 'Możliwe, że zgoda jest już zapisana albo telewizor jest w innej sieci Wi-Fi. Zamknij Mando TV i otwórz aplikację ponownie przy włączonym telewizorze. Jeśli telewizor jest starszy niż 2016, używa innego systemu, który nie jest jeszcze obsługiwany.'),
      ('Jeśli zgoda została odrzucona przez pomyłkę', 'W telewizorze otwórz Ustawienia > Ogólne > Menedżer urządzeń zewnętrznych > Menedżer połączeń urządzeń i ustaw Mando TV jako dozwolone. Jeśli telefon nadal nie widzi telewizora, przeczytaj [Telefon nie widzi telewizora](@not-found).'),
    ],
    marca='samsung',
    faq=[
      ('Jak potwierdzić połączenie, jeśli nie mam pilota?', 'W większości modeli potwierdzisz je przyciskami na telewizorze albo joystickiem z tyłu. Jeśli Twój model nie ma przycisków, napisz na hola@mandotv.app, a pomożemy.'),
      ('Czy Mando TV wymaga konta Samsung?', 'Nie. Połączenie idzie bezpośrednio przez Twoją sieć Wi-Fi, bez konta Samsung.'),
      ('Czy działa z moim starszym telewizorem Samsung?', 'Działa z telewizorami Samsung z Tizen, rocznik 2016 i nowsze.'),
    ]),
  dict(clave='wifi', corto='Telefon jako pilot przez Wi-Fi',
    titulo='Telefon jako pilot: sterowanie telewizorem przez Wi-Fi',
    desc='Połącz telefon z telewizorem przez Wi-Fi i używaj go jako pilota do Samsung, LG, Roku i Google TV. Kroki dla każdej marki z Mando TV. Za darmo.',
    h1='Jak połączyć telefon z telewizorem przez Wi-Fi jako pilota',
    intro='Potrzebujesz tylko telefonu i telewizora w tej samej sieci Wi-Fi oraz aplikacji pilota. Mando TV samo znajduje Twój telewizor i działa z Samsung, LG, Roku, Google TV i Android TV.',
    pasos=[
      'Połącz telefon i telewizor z tą samą siecią Wi-Fi.',
      'Otwórz Mando TV. Twój telewizor sam pojawi się na liście. Stuknij go.',
      'Potwierdź połączenie dla swojej marki (szczegóły poniżej).',
      'Steruj telewizorem przyciskami albo klawiaturą telefonu. Touchpad to funkcja Pro.',
    ],
    extra=[
      ('Samsung', 'Telewizor zapyta, czy zezwalasz na połączenie. Potwierdź je za pierwszym razem na ekranie. Działa z Tizen, rocznik 2016 i nowsze. Żeby włączać go z telefonu, w Ustawienia > Ogólne > Sieć > Ustawienia ekspertów włącz „Włączanie przez urządzenie mobilne”.'),
      ('LG', 'Telewizor pokaże prośbę o zgodę. Potwierdź ją za pierwszym razem. Żeby włączać go z telefonu, w ustawieniach znajdź „Włącz TV przez urządzenie mobilne” i włącz „Włącz przez Wi-Fi”.'),
      ('Roku', 'Roku nie wymaga parowania: stuknij je na liście i jesteś połączony. Żeby je włączać, w Ustawienia > System > Zasilanie włącz „Szybkie uruchamianie TV”.'),
      ('Google TV i Android TV', 'Telewizor pokaże kod na ekranie. Wpisz go w Mando TV za pierwszym razem. Żeby go włączać, w ustawieniach poszukaj „Wake on LAN”, „Włączanie przez sieć” albo „Network standby”.'),
    ],
    marca=None,
    faq=[
      ('Czy potrzebuję internetu, żeby używać telefonu jako pilota?', 'Potrzebujesz telefonu i telewizora w tej samej sieci Wi-Fi. Mando TV łączy się z telewizorem bezpośrednio przez tę sieć.'),
      ('Dlaczego mój telewizor nie pojawia się na liście?', 'Sprawdź, czy telewizor jest włączony, a telefon nie używa danych komórkowych ani innej sieci Wi-Fi. Niektóre routery mają sieć dla gości, która izoluje urządzenia od siebie.'),
      ('Czy mogę używać Mando TV na iPhone albo na telefonie z Androidem?', 'Na iPhone i iPad tak: aplikacja jest już w App Store. Dla Windows jest też w Microsoft Store. Android wkrótce: możesz dołączyć do darmowego wczesnego dostępu w Google Play.'),
    ]),
  dict(clave='pc', corto='Sterowanie telewizorem z komputera',
    titulo='Sterowanie telewizorem z komputera z Windows (za darmo)',
    desc='Używaj komputera z Windows jako pilota do Samsung, LG, Roku lub Google TV przez Wi-Fi. Przyciski, klawiatura i aplikacje za darmo; skróty klawiszowe w Pro.',
    h1='Jak sterować telewizorem z komputera z Windows',
    intro='Jeśli spędzasz dzień przy komputerze, nie musisz szukać pilota: Mando TV dla Windows steruje Twoim telewizorem Samsung, LG, Roku, Google TV lub Android TV przez domową sieć Wi-Fi. Przydaje się do zmiany aplikacji, ściszania albo pisania w YouTube na klawiaturze komputera.',
    pasos=[
      'Pobierz Mando TV za darmo z Microsoft Store na komputer z Windows 10 lub 11.',
      'Sprawdź, czy komputer i telewizor są w tej samej sieci (Wi-Fi lub kabel, ale przez ten sam router).',
      'Otwórz Mando TV: Twój telewizor sam pojawi się na liście. Stuknij go lub kliknij.',
      'Za pierwszym razem potwierdź połączenie na ekranie telewizora (w Google TV i Android TV wpisujesz kod, który pokazuje telewizor).',
      'Gotowe: używaj przycisków albo klawiatury, żeby pisać w polu wyszukiwania telewizora. Touchpad to funkcja Pro.',
    ],
    extra=[
      ('Skróty klawiszowe na komputerze (Pro)', 'Z Mando TV Pro sterujesz telewizorem klawiaturą komputera: strzałki do poruszania się, Enter jako OK, Backspace lub Esc do cofania, + i - do głośności, M do wyciszenia i spacja do pauzy.'),
      ('Mini pilot zawsze na wierzchu (Pro)', 'Trzymaj małe okno z pilotem zawsze widoczne, gdy pracujesz lub grasz na komputerze.'),
      ('Mów do telewizora z komputera (Pro)', 'Z Mando TV Pro wydajesz telewizorowi polecenia przez mikrofon komputera: „otwórz YouTube”, „zgłośnij” albo „wyłącz za 30 minut”, tak jak mówisz. W Windows mowa jest rozpoznawana na samym komputerze: nie potrzebujesz internetu, nie musisz zmieniać niczego w ustawieniach Windows i działa we wszystkich 6 językach aplikacji. To, co mówisz, nie opuszcza komputera i nie jest zapisywane. Tylko w bardzo starych procesorach aplikacja używa pisania głosowego Windows. Wtedy musi być włączone rozpoznawanie mowy online w ustawieniach prywatności i dodany w Windows język polski (Polska). Jeśli czegoś brakuje, aplikacja da znać i otworzy ustawienie przyciskiem.'),
    ],
    marca=None,
    faq=[
      ('Czy potrzebuję kabla albo Bluetooth, żeby sterować telewizorem z komputera?', 'Nie. Mando TV łączy się przez Twoją sieć domową: komputer i telewizor muszą tylko być podłączone do tego samego routera.'),
      ('Czy działa z każdym telewizorem?', 'Działa z telewizorami Samsung z Tizen (rocznik 2016 i nowsze), LG z webOS, Roku oraz Google TV lub Android TV (Sony, Philips, TCL, Hisense, Sharp, Xiaomi, Toshiba, Panasonic, Haier, Skyworth i inne).'),
      ('Ile to kosztuje?', 'Przyciski, klawiatura i włączanie przez sieć są darmowe i bez reklam. Mando TV Pro to jednorazowy zakup bez subskrypcji, z dodatkami takimi jak touchpad, skróty klawiszowe i mini pilot.'),
      ('Dlaczego mikrofon w Windows mnie nie rozumie?', 'Sprawdź, czy funkcja głosu jest aktywna (należy do Pro) i czy mikrofon komputera działa w Windows. Na prawie wszystkich komputerach mowa jest rozpoznawana na samym urządzeniu, bez internetu. Tylko w bardzo starych procesorach aplikacja używa pisania głosowego Windows. Wtedy sprawdź, czy rozpoznawanie mowy online jest włączone w ustawieniach prywatności Windows, a Windows ma w ustawieniach języka polski (Polska). Mando TV używa tego języka tylko wtedy, gdy słucha.'),
    ]),
  dict(clave='roku-403', corto='Aplikacja Roku nie działa',
    titulo='Aplikacja Roku nie działa? Napraw błąd 403',
    desc='Telefon połączony, a Roku nie reaguje? Włącz „Sterowanie przez aplikacje mobilne” w 5 krokach i znów używaj telefonu jako pilota.',
    h1='Aplikacja Roku nie działa: jak rozwiązać problem',
    intro='Jeśli telefon znajduje Roku i łączy się, ale żaden przycisk nic nie robi, to prawie zawsze wina ustawienia w samym Roku, które blokuje aplikacje pilota. Nowsze wersje Roku są domyślnie bardziej restrykcyjne. W menu Roku naprawisz to w minutę.',
    pasos=[
      'W Roku naciśnij Home i wejdź w Ustawienia.',
      'Otwórz System, a potem Zaawansowane ustawienia systemu.',
      'Wejdź w „Sterowanie przez aplikacje mobilne”. W niektórych modelach nazywa się „Sterowanie zewnętrzne”.',
      'W „Dostęp do sieci” wybierz Domyślny lub Zezwalający. Jeśli w Twoim modelu to tylko przełącznik, zostaw Włączone.',
      'Wróć do Mando TV w telefonie i stuknij swoje Roku. Przyciski już reagują.',
    ],
    extra=[
      ('Jak rozpoznać, że to Twój problem', 'Objaw jest jednoznaczny: telefon widzi Roku na liście i łączy się, ale nic się nie dzieje po stuknięciu przycisku. Wewnętrznie Roku odpowiada błędem 403, co znaczy „zabronione”. Mando TV rozpoznaje to przy łączeniu i pokazuje Ci dokładnie te kroki na ekranie.'),
      ('Domyślny czy Zezwalający, co wybrać?', 'Wystarczy Domyślny: przyjmuje polecenia z Twojej sieci domowej, a tego potrzebuje pilot. Zezwalający jest bardziej otwarty i potrzebny tylko w nietypowych sieciach. Jeśli opcja jest ustawiona na Wyłączony (w nowszym oprogramowaniu Ograniczony), Roku nie reaguje na aplikacje.'),
      ('Jeśli nie masz pilota Roku', 'Jeśli ustawienie jest na Wyłączony, można je zmienić tylko prawdziwym pilotem Roku. Pożycz go, żeby zmienić to jednorazowo; potem wszystko zrobisz telefonem. Przeczytaj też [Zgubiony pilot Roku](@roku-lost).'),
    ],
    marca='roku',
    faq=[
      ('Dlaczego moje Roku przestało reagować, choć wcześniej działało?', 'Aktualizacja Roku może bardziej ograniczać to ustawienie. To nie wina telefonu ani Twojego Wi-Fi: wystarczy znów zezwolić na sterowanie przez aplikacje.'),
      ('Czy dotyczy to Roku TV i odtwarzaczy Roku?', 'Tak. Ustawienie jest w tym samym menu w odtwarzaczach Roku i w telewizorach Roku TV.'),
      ('Czy bezpiecznie jest zostawić ustawienie na Domyślny?', 'Tak. Przyjmuje tylko polecenia z urządzeń w Twojej sieci domowej.'),
    ]),
  dict(clave='not-found', corto='Telefon nie widzi telewizora',
    titulo='Telefon nie widzi telewizora? 6 rzeczy do sprawdzenia',
    desc='Aplikacja pilot nie znajduje telewizora? Sprawdź Wi-Fi, VPN i dostęp do sieci lokalnej. Dla Samsung, LG, Roku i Android TV.',
    h1='Telefon nie widzi telewizora: co sprawdzić',
    intro='Otwierasz aplikację pilota, a lista jest pusta albo telewizor się pojawia, ale połączenie się zrywa. Prawie zawsze winna jest sieć, a nie telewizor. Sprawdź te punkty po kolei: pierwszy rozwiązuje większość przypadków.',
    pasos=[
      'Zobacz, w jakiej sieci Wi-Fi jest telefon, a w jakiej telewizor. To musi być ta sama sieć, o tej samej nazwie. Sieć dla gości nie działa, bo izoluje urządzenia od siebie.',
      'Wyłącz VPN w telefonie, jeśli go używasz. Przy włączonym VPN telefon wychodzi do internetu inną siecią i nie widzi urządzeń w Twoim domu albo połączenie zrywa się po kilku sekundach.',
      'Na chwilę wyłącz dane komórkowe. Niektóre telefony przy słabym sygnale same przełączają się z Wi-Fi na dane komórkowe.',
      'Włącz telewizor i poczekaj, aż skończy się uruchamiać. Wyłączony telewizor nie odpowiada na wyszukiwanie.',
      'Na iPhone sprawdź, czy aplikacja ma uprawnienie „Sieć lokalna”: Ustawienia > Prywatność i ochrona > Sieć lokalna.',
      'Jeśli nadal się nie pojawia, dodaj go ręcznie: w Mando TV stuknij „Dodaj po adresie IP” i wpisz adres IP telewizora.',
    ],
    extra=[
      ('Pozwól się poprowadzić aplikacji', 'Na liście telewizorów jest przycisk na wypadek, gdy Twój telewizor się nie pojawia. Aplikacja krok po kroku sprawdza najczęstsze przyczyny (ta sama sieć Wi-Fi, VPN, uprawnienie do sieci lokalnej i więcej) i po każdej poprawce pokazuje przycisk ponownego sprawdzenia. Kreator jest darmowy.'),
      ('Gdzie znaleźć adres IP telewizora', 'Jest w menu sieci telewizora i zależnie od modelu jest trochę inaczej. W LG: Ustawienia, Sieć, Połączenie Wi-Fi, Zaawansowane ustawienia Wi-Fi. W Samsung: Ustawienia, Ogólne, Sieć, Stan sieci, Ustawienia IP. W Roku: Ustawienia, Sieć, Informacje. W Android TV i Google TV: Ustawienia, Sieć i internet, potem stuknij swoją sieć. To liczba taka jak 192.168.1.86.'),
      ('Jeśli się pojawia, ale połączenie się zrywa', 'Jeśli połączenie zrywa się po kilku sekundach, przyczyna jest zwykle w telefonie: VPN, przełączenie na inną sieć Wi-Fi albo tryb oszczędzania energii. Wyłącz VPN, zostań w tej samej sieci Wi-Fi i spróbuj ponownie.'),
      ('Wi-Fi 2,4 i 5 GHz', 'Nie ma znaczenia, czy telefon jest w sieci 5 GHz, a telewizor w sieci 2,4 GHz, dopóki obie pochodzą z tego samego routera. Jeśli masz wzmacniacz Wi-Fi, a telewizor nadal się nie pojawia, podejdź z telefonem bliżej głównego routera i spróbuj ponownie.'),
    ],
    marca=None,
    faq=[
      ('Czy mogę sterować telewizorem przez dane komórkowe?', 'Nie. Sygnał pilota idzie przez Twoją domową sieć Wi-Fi, dlatego telefon i telewizor muszą być w tej samej sieci.'),
      ('Dlaczego nie działa przy włączonym VPN?', 'Bo VPN kieruje cały ruch telefonu inną siecią i telefon przestaje widzieć urządzenia w Twoim domu. Wyłącz go na czas korzystania z pilota.'),
      ('Czy działa przez Bluetooth lub podczerwień?', 'W smart TV Mando TV używa Wi-Fi. Podczerwień działa tylko w telefonach z Androidem z nadajnikiem podczerwieni i jest przeznaczona dla telewizorów, które nie są smart TV. Bluetooth jest w wersji beta, za darmo i tylko od Androida 9: telefon łączy się z telewizorem jak klawiatura i pilot Bluetooth, zupełnie bez Wi-Fi. Działa z Google TV, Android TV i Fire TV; z innymi markami, które akceptują klawiatury Bluetooth, może działać, Roku ich nie akceptuje.'),
    ]),
  dict(clave='androidtv-code', corto='Kod parowania Android TV',
    titulo='Android TV prosi o kod parowania: co zrobić',
    desc='Twój Android TV lub Google TV pokazuje przy łączeniu 6-znakowy kod. Jak go wpisać i co zrobić, gdy się nie pojawia albo jest błędny.',
    h1='Android TV prosi o kod parowania: co zrobić',
    intro='Gdy po raz pierwszy łączysz telefon z Android TV lub Google TV, telewizor pokazuje na ekranie 6-znakowy kod. To normalne i zdarza się tylko raz: dzięki temu nikt inny nie może sterować Twoim telewizorem. Oto jak go wpisać i co zrobić, gdy się nie pojawia.',
    pasos=[
      'Włącz telewizor i zostaw widoczny ekran główny.',
      'Otwórz Mando TV w telefonie, w tej samej sieci Wi-Fi co telewizor, i stuknij na liście swój telewizor.',
      'Spójrz na ekran telewizora: pojawi się kod z 6 liter i cyfr.',
      'Wpisz go w telefonie dokładnie tak, jak jest pokazany, i stuknij Sparuj. Litery są tylko od A do F, więc okrągły znak to zawsze cyfra zero.',
      'Gotowe. Telewizor zapamiętuje Twój telefon i nie pyta ponownie o kod.',
    ],
    extra=[
      ('Jeśli kod nie pojawia się w telewizorze', 'Sprawdź, czy telewizor naprawdę jest włączony, a nie w trybie czuwania, i czy telefon jest w tej samej sieci Wi-Fi. Stuknij telewizor w telefonie jeszcze raz. Jeśli nadal się nie pojawia, uruchom telewizor ponownie: wyjmij wtyczkę na dziesięć sekund, włóż ją z powrotem i spróbuj jeszcze raz.'),
      ('Jeśli kod jest uznawany za błędny', 'Kod zmienia się przy każdej prośbie. Jeśli zajęło Ci to dużo czasu albo poprosiłeś o niego dwa razy, działa tylko ostatni z ekranu. Stuknij telewizor w telefonie jeszcze raz i wpisz nowy kod.'),
      ('Jeśli telewizor znów pyta o kod', 'Dzieje się tak, gdy telewizor został przywrócony do ustawień fabrycznych albo usuwasz dane aplikacji w telefonie. Sparuj ponownie, a zostanie zapamiętany. Jeśli w ogóle nie masz pilota, przeczytaj [Android TV bez pilota](@androidtv).'),
    ],
    marca='android',
    faq=[
      ('Jakie telewizory używają tego kodu?', 'Te z Android TV lub Google TV: Sony, Philips, TCL, Hisense, Sharp, Xiaomi, Chromecast z Google TV i kilka innych.'),
      ('Czy potrzebuję konta Google w telefonie?', 'Nie. Kod na ekranie to wszystko, czego potrzebujesz.'),
      ('Czy to bezpieczne?', 'Tak. Kod dowodzi, że siedzisz przed telewizorem: nikt nie sparuje urządzenia, nie widząc go na ekranie.'),
    ]),
  dict(clave='roku-lost', corto='Zgubiony pilot Roku',
    titulo='Zgubiony pilot Roku? Użyj telefonu przez Wi-Fi',
    desc='Zgubiony pilot Roku? Telefon zastąpi go przez Wi-Fi. Proste kroki, także gdy zmieniłeś router i Roku nie ma Wi-Fi.',
    h1='Zgubiony pilot Roku: jak użyć telefonu',
    intro='Jeśli zgubiłeś pilota Roku albo przestał działać, zastąpi go telefon, o ile Roku jest nadal połączone z Twoją siecią Wi-Fi. A gdy zmieniła się sieć Wi-Fi albo router, na to też jest sposób.',
    pasos=[
      'Najpierw spróbuj sprawić, żeby pilot zadzwonił. Jeśli Twój pilot Roku ma głośnik, na przykład Roku Voice Remote Pro, otwórz Mando TV, połącz się z Roku i użyj opcji, która sprawia, że pilot dzwoni, żebyś go znalazł. Działa tylko z pilotami Roku z głośnikiem, a Roku musi być włączone.',
      'Włącz telewizor i zostaw Roku podłączone. Nie musisz niczego w nim dotykać.',
      'Połącz telefon z tą samą siecią Wi-Fi, której używa Roku.',
      'Otwórz Mando TV. Roku samo pojawi się na liście. Stuknij je.',
      'Używaj strzałek, OK, Home i Wstecz jak na swoim zwykłym pilocie. Roku nie prosi o kod.',
      'Jeśli przyciski nic nie robią, Roku blokuje sterowanie przez aplikacje: poradnik [Aplikacja Roku nie działa](@roku-403) wyjaśnia, jak je dopuścić.',
    ],
    extra=[
      ('Jeśli Roku nie ma Wi-Fi (zmiana routera lub przeprowadzka)', 'Bez pilota nie wejdziesz do menu, żeby ustawić nową sieć, ale jest sposób: Roku samo łączy się z siecią o tej samej nazwie i haśle co stara. Na innym telefonie ustaw hotspot Wi-Fi z dokładnie taką nazwą i hasłem, połącz telefon z Mando TV z tym hotspotem, a Roku pojawi się na liście. Stamtąd wejdź w Ustawienia, Sieć i połącz je z nowym Wi-Fi.'),
      ('Jeśli to Roku TV', 'Telewizory Roku TV mają przycisk na obudowie, prawie zawsze na dole pośrodku albo z tyłu, który włącza telewizor. To wystarczy, żeby go włączyć i kontynuować telefonem.'),
      ('Jeśli wolisz kupić inny pilot', 'Upewnij się, że pasuje do Twojego modelu. Małe odtwarzacze Roku schowane za telewizorem potrzebują pilota bez podczerwieni, bo podczerwień do nich nie dociera.'),
    ],
    marca='roku',
    faq=[
      ('Czy telefon może włączyć Roku?', 'Podłączony odtwarzacz Roku jest zawsze włączony. W Roku TV Mando TV włącza go przez Wi-Fi, jeśli w Ustawienia > System > Zasilanie jest włączone „Szybkie uruchamianie TV”.'),
      ('A głośność?', 'W Roku TV telefon zwiększa i zmniejsza głośność. W odtwarzaczu Roku podłączonym przez HDMI zależy to od telewizora: w wielu działa, w innych nie.'),
      ('Czy muszę zakładać konto?', 'Nie. Mando TV nie wymaga konta i steruje też telewizorami Samsung, LG i Android TV tą samą aplikacją.'),
    ]),
]

SOPORTE = dict(
  titulo='Pomoc: jak połączyć i włączyć telewizor z Mando TV',
  desc='Jak połączyć pilota Mando TV z LG, Samsung, Roku lub Android TV, włączyć telewizor z telefonu i rozwiązać problemy.',
  h1='Pomoc',
  intro='Najczęstsze pytania, w kolejności kroków. Jeśli nie znajdziesz swojego, napisz do nas na <a href="mailto:hola@mandotv.app?subject=Pomoc%20z%20Mando%20TV">hola@mandotv.app</a>, a odpowiemy.',
)
SOPORTE_HTML = '''      <h2 id="encontrar">Znajdowanie telewizora</h2>
      <div class="preguntas">
        <details open><summary>Mój telewizor nie pojawia się na liście</summary>
          <ol>
            <li>Sprawdź, czy telefon i telewizor są w tej samej sieci Wi-Fi. Jeśli Twój router ma sieć 2,4 GHz i 5 GHz o różnych nazwach, czasem się nie widzą.</li>
            <li>Upewnij się, że telewizor jest włączony.</li>
            <li>Na iPhone sprawdź, czy Mando TV ma uprawnienie „Sieć lokalna”, w Ustawienia, Mando TV.</li>
            <li>Na liście telewizorów stuknij przycisk na wypadek, gdy Twój telewizor się nie pojawia: aplikacja krok po kroku sprawdza najczęstsze przyczyny (ta sama sieć Wi-Fi, VPN, uprawnienie do sieci lokalnej i więcej) i po każdej poprawce pokazuje przycisk ponownego sprawdzenia.</li>
            <li>Jeśli nadal się nie pojawia, stuknij przycisk +, wybierz markę i wpisz adres IP telewizora. Zobaczysz go w menu sieci telewizora (na przykład 192.168.1.50).</li>
          </ol>
        </details>
        <details><summary>Czy działa przez dane komórkowe albo zdalnie?</summary>
          <p>Nie. Mando TV rozmawia z telewizorem w Twojej sieci domowej, więc telefon musi być połączony z tą siecią Wi-Fi.</p>
        </details>
      </div>

      <h2 id="conectar">Pierwsze połączenie</h2>
      <p>Pełne poradniki według marki: <a href="@@R_lg@@">LG</a>, <a href="@@R_samsung@@">Samsung</a>, <a href="@@R_roku@@">Roku</a> i <a href="@@R_android@@">Android TV</a>.</p>
      <div class="preguntas">
        <details><summary>LG</summary>
          <p>Gdy stukniesz telewizor, na ekranie pojawi się prośba o zgodę. Zaakceptuj ją zwykłym pilotem. Robisz to tylko raz.</p>
        </details>
        <details><summary>Samsung</summary>
          <p>Telewizor zapyta, czy zezwalasz na połączenie z Mando TV. Pilotem wybierz „Zezwól”. Jeśli przez pomyłkę odrzucisz zgodę, wejdź w Ustawienia > Ogólne > Menedżer urządzeń zewnętrznych > Menedżer połączeń urządzeń i zmień ją na dozwoloną.</p>
        </details>
        <details><summary>Roku</summary>
          <p>Roku nie prosi o zgodę. Jeśli połączenie się nie uda, w Roku wejdź w Ustawienia > System > Zaawansowane ustawienia systemu > Sterowanie przez aplikacje mobilne i zostaw Dostęp do sieci na Domyślny lub Zezwalający (w nowszym oprogramowaniu Roku ustaw „Sterowanie przez aplikacje mobilne” na Włączone).</p>
        </details>
        <details><summary>Android TV i Google TV</summary>
          <p>Telewizor pokaże 6-znakowy kod. Wpisz go w Mando TV dokładnie tak, jak się pojawił. Działa z Sony, Philips, TCL, Hisense, Sharp, Xiaomi, Chromecast z Google TV i innymi z Android TV.</p>
        </details>
      </div>

      <h2 id="encender">Włączanie telewizora z aplikacji</h2>
      <p>Mando TV włącza telewizor przez Twoją sieć domową. Potrzebne są dwie rzeczy: raz połączyłeś się przy włączonym telewizorze, a w telewizorze jest włączone włączanie przez sieć. Nazwa ustawienia zmienia się zależnie od modelu; oto najczęstsze:</p>
      <div class="preguntas">
        <details><summary>LG</summary>
          <p>W ustawieniach (w Ogólne > Urządzenia > Urządzenia zewnętrzne, w starszych modelach w Połączenie > Zarządzanie połączeniem mobilnym) poszukaj „Włącz TV przez urządzenie mobilne” i włącz „Włącz przez Wi-Fi”. Jeśli jest „Quick Start+”, włącz też tę opcję.</p>
        </details>
        <details><summary>Samsung</summary>
          <p>Włącz „Włączanie przez urządzenie mobilne” w Ustawienia > Ogólne > Sieć > Ustawienia ekspertów.</p>
        </details>
        <details><summary>Roku</summary>
          <p>W telewizorach Roku TV włącz „Szybkie uruchamianie TV” w Ustawienia > System > Zasilanie. Odtwarzaczy Roku podłączonych do telewizora nie da się w ten sposób włączyć.</p>
        </details>
        <details><summary>Android TV i Google TV</summary>
          <p>To zależy od producenta. W ustawieniach sieci lub zasilania poszukaj „Wake on LAN”, „Włączanie przez sieć”, „Network standby” albo „Remote start”. Niektóre modele nie mają tej opcji.</p>
        </details>
      </div>

      <h2 id="falla">Jeśli coś nie działa</h2>
      <div class="preguntas">
        <details><summary>Połączenie się zrywa albo nic nie reaguje</summary>
          <ol>
            <li>Na ekranie pilota stuknij Połącz ponownie.</li>
            <li>Jeśli to nie pomoże, zamknij Mando TV i otwórz aplikację ponownie.</li>
            <li>Jeśli telewizor dostał inny adres IP, usuń go z listy i dodaj ponownie.</li>
          </ol>
        </details>
        <details><summary>Jak wysłać nam raport o błędzie</summary>
          <ol>
            <li>W Mando TV stuknij przycisk Personalizuj (suwaki u góry).</li>
            <li>Stuknij Kopiuj raport testowy.</li>
            <li>Wklej go razem z marką i modelem telewizora do e-maila na hola@mandotv.app.</li>
          </ol>
          <p>Raport nie zawiera haseł, kodów ani niczego, co wpisujesz.</p>
        </details>
        <details><summary>Kupiłem Pro i nie widzę go</summary>
          <p>W Personalizuj stuknij Przywróć zakup, na tym samym koncie sklepu, na którym kupowałeś. Jeśli nadal się nie pojawia, napisz do nas.</p>
        </details>
      </div>

      <h2 id="guias">Poradniki krok po kroku</h2>
      <p><a href="@@R_guias@@">Zobacz wszystkie poradniki</a></p>
      <ul>
@@GUIAS@@
      </ul>

      <h2 id="contacto">Masz jeszcze pytania?</h2>
      <p>Napisz do nas na <a href="mailto:hola@mandotv.app?subject=Pomoc%20z%20Mando%20TV">hola@mandotv.app</a>. Podaj markę i model telewizora oraz krok, na którym utknąłeś. Pisz w swoim języku. Odpowiadamy po hiszpańsku lub angielsku, a jeśli chcesz, także w Twoim języku z pomocą tłumacza.</p>
'''

PRIVACIDAD = dict(
  titulo='Polityka prywatności | Mando TV',
  desc='Mando TV nie zbiera danych osobowych: bez kont, bez reklam, bez trackerów. Aplikacja rozmawia tylko z Twoim telewizorem w Twojej sieci Wi-Fi.',
  h1='Prywatność',
  intro='Krótko: Mando TV nie zbiera Twoich danych. Nie ma kont, reklam, trackerów ani własnych serwerów, które zapisywałyby, co robisz.',
)
PRIVACIDAD_HTML = '''      <p class="fecha">Obowiązuje od 14 listopada 2026. Ostatnia aktualizacja: 25 listopada 2026.</p>

      <h2>Kim jesteśmy</h2>
      <p>Mando TV to aplikacja, która pozwala sterować telewizorem z telefonu lub komputera. Ta polityka opisuje, jakich informacji używa aplikacja i co z nimi robi. W razie pytań napisz do nas na <a href="mailto:hola@mandotv.app">hola@mandotv.app</a>.</p>

      <h2>Jakie dane zbieramy</h2>
      <p>Aplikacja: żadnych. Aplikacja nie wysyła nam ani osobom trzecim żadnych informacji o Tobie ani o tym, jak z niej korzystasz. Nie używa narzędzi analitycznych, reklamowych ani śledzących.</p>
      <p>Ta strona internetowa: mierzymy odwiedziny na dwa sposoby, opisane w sekcji <a href="#cookies">Pliki cookie na tej stronie</a>.</p>

      <h2>Co aplikacja zapisuje na Twoim urządzeniu</h2>
      <p>Żeby działać, aplikacja zapisuje poniższe informacje wyłącznie na Twoim telefonie lub komputerze:</p>
      <ul>
        <li>Telewizory, które dodałeś: nazwa, marka, adres IP w Twojej sieci i adres sprzętowy karty sieciowej (MAC), używany do włączania.</li>
        <li>Klucze połączenia, które przekazuje każdy telewizor po potwierdzeniu zgody. Są zapisywane w zaszyfrowanej postaci w bezpiecznej pamięci systemu (Pęk kluczy na iPhone i Mac, Keystore na Androidzie, chroniona pamięć w Windows).</li>
        <li>Twoje ustawienia: jasny lub ciemny motyw, kolor tła, wibracja i rodzaj pilota.</li>
        <li>Jeśli korzystasz z funkcji Pro: ulubione aplikacje, rutyny i ostatnie wyszukiwania w YouTube (możesz je usunąć w aplikacji).</li>
      </ul>
      <p>Gdy usuniesz aplikację, wszystko to zostaje usunięte razem z nią.</p>

      <h2>Z kim rozmawia aplikacja</h2>
      <p>Z Twoimi telewizorami, w Twojej domowej sieci Wi-Fi. Żeby je znaleźć, aplikacja przeszukuje Twoją sieć lokalną; dlatego na iPhone prosi o uprawnienie „Sieć lokalna”. Tekst, który wpisujesz na klawiaturze aplikacji, trafia bezpośrednio do telewizora i nie jest zapisywany.</p>
      <p>Poza tym przy otwarciu aplikacja pobiera z tej strony mały publiczny plik (mandotv.app/app/config.json), żeby dowiedzieć się, czy jest nowa wersja, którą warto zainstalować, i które funkcje należą do Mando TV Pro. To zwykłe pobranie, jak przy otwarciu strony: aplikacja nie wysyła Twoich danych, telewizorów ani tego, co robisz. Podaje tylko wersję aplikacji i system (na przykład Android), żeby mogła pokazać odpowiedni komunikat. Jeśli nie masz internetu, aplikacja działa dalej z ostatnim pobranym plikiem; jeśli minie ponad 30 dni bez możliwości pobrania, aplikacja poprosi Cię o krótkie połączenie z internetem.</p>

      <p>Gdy wysyłasz zdjęcia lub filmy do telewizora (funkcja Pro), telewizor pobiera tylko pliki, które wybierzesz, bezpośrednio z Twojego telefonu lub komputera przez domową sieć Wi-Fi. Nie przechodzą przez internet ani przez nas, aplikacja nie widzi pozostałych Twoich zdjęć, a udostępnianie kończy się, gdy zamkniesz ten ekran.</p>
      <h2>Mikrofon i głos</h2>
      <p>Wyszukiwanie głosowe używa mikrofonu tylko wtedy, gdy trzymasz przycisk mówienia. To, co mówisz, zamienia na tekst rozpoznawanie mowy Twojego systemu: Apple na iPhone i Mac oraz Google na Androidzie, każde według własnej polityki prywatności. W Windows mowa jest rozpoznawana na Twoim własnym komputerze i nie opuszcza urządzenia; tylko w bardzo starych procesorach aplikacja używa pisania głosowego Windows, firmy Microsoft, według jej polityki prywatności. Mando TV nie nagrywa ani nie zapisuje dźwięku, a powstały tekst trafia bezpośrednio do Twojego telewizora, tak samo jak to, co wpisujesz na klawiaturze.</p>

      <h2>Dom: urządzenia z Apple Home i Google Home</h2>
      <p>Gdy otworzysz sekcję Dom (w fazie testów), aplikacja poprosi o zgodę na wyświetlanie urządzeń, które masz już w aplikacji Dom Apple (HomeKit) lub w Google Home. Dzięki tej zgodzie odczytuje ich nazwę, pomieszczenie i stan (włączone lub wyłączone, jasność, temperatura albo moment programu, w którym jest sprzęt AGD), żeby je pokazać i wysyłać im to, co stukniesz. Wszystko dzieje się między Twoim telefonem a systemem Apple lub Google: Mando TV nie zapisuje tej listy, nie wysyła jej ani nam, ani osobom trzecim i nie używa jej do reklam ani analiz. Na Androidzie Google Home działa z Twoim własnym kontem Google, według polityki prywatności Google. Zgodę możesz wycofać w dowolnym momencie: na iPhone w Ustawienia &gt; Prywatność i ochrona &gt; HomeKit, na Androidzie w ustawieniach konta Google.</p>
      <p>Gdy stukniesz „Jak Dom działał u Ciebie?”, otworzy się Twoja aplikacja poczty z wiadomością do hola@mandotv.app, która zawiera techniczne podsumowanie: wersję aplikacji, system oraz ile urządzeń każdego rodzaju się pojawiło i czy reagują. Nie ma w niej nazw urządzeń, pomieszczeń ani Twojego domu, a wiadomość zostanie wysłana tylko wtedy, gdy sam ją wyślesz.</p>

      <h2>Raport testowy</h2>
      <p>Aplikacja ma przycisk „Kopiuj raport testowy”, który pomaga nam naprawiać błędy. Raport zostaje tylko w pamięci aplikacji, dopóki jest otwarta, i nigdy nie jest wysyłany automatycznie: to Ty decydujesz, czy go skopiujesz i komuś przekażesz. Nie zawiera kluczy połączenia, kodów parowania ani niczego, co wpisujesz; tylko kroki, które wykonała aplikacja, takie jak wyszukiwanie, łączenie i błędy.</p>

      <h2 id="cookies">Pliki cookie na tej stronie</h2>
      <p>Dotyczy to tylko strony mandotv.app, a nie aplikacji.</p>
      <h3>Zawsze bez plików cookie</h3>
      <p>Liczymy odwiedziny anonimowo za pomocą Cloudflare Web Analytics: ile osób odwiedza stronę, jakie strony czytają i z jakiego kraju. Nie używa plików cookie, nie wykorzystuje Twojego adresu IP do identyfikacji i nie śledzi tego, co robisz na innych stronach.</p>
      <h3>Z plikami cookie, tylko jeśli się zgodzisz</h3>
      <p>Jeśli w komunikacie o plikach cookie stukniesz „Akceptuj”, włączymy Google Analytics (firmy Google LLC), żeby lepiej rozumieć, jak strona jest używana: wyświetlenia stron, czas wizyty, typ urządzenia, przybliżone miasto i skąd przychodzisz. W tym celu zapisuje w Twojej przeglądarce pliki cookie _ga i _ga_* na okres do 2 lat. Google może przetwarzać te dane na serwerach poza Chile. Wyłączyliśmy funkcje reklamowe i Google Signals i nie używamy tych danych do wyświetlania Ci reklam.</p>
      <p>Jeśli stukniesz „Odrzuć” albo nic nie wybierzesz, Google Analytics nie zostanie załadowane i nie zostanie zapisany żaden plik cookie. Swoją decyzję możesz zmienić w dowolnym momencie przyciskiem „Cookies” na dole każdej strony; jeśli wycofasz zgodę, usuniemy te pliki cookie.</p>
      <p>Twój wybór jest zapisywany w Twojej przeglądarce (pamięć lokalna, nikomu nie wysyłana), żebyśmy nie pytali Cię ponownie.</p>

      <h2>Zakupy</h2>
      <p>Gdy kupujesz Mando TV Pro, płatność obsługuje sklep z aplikacjami (App Store, Google Play lub Microsoft Store). Nie otrzymujemy ani nie zapisujemy danych Twojej karty. Sklep tylko potwierdza aplikacji, że zakup istnieje.</p>

      <h2>E-maile, które do nas wysyłasz</h2>
      <p>Gdy piszesz do nas na <a href="mailto:hola@mandotv.app">hola@mandotv.app</a>, używamy Twojego adresu e-mail i tego, co nam przekazujesz, wyłącznie po to, żeby Ci odpowiedzieć. Nie przekazujemy tego dalej ani nie używamy do reklam. W każdej chwili możesz zażądać usunięcia Twoich wiadomości.</p>

      <h2>Dzieci</h2>
      <p>Aplikacja nie zbiera danych od nikogo, także od dzieci.</p>

      <h2>Zmiany tej polityki</h2>
      <p>Jeśli kiedyś zmieni się to, co aplikacja robi z Twoimi danymi, zaktualizujemy tę stronę i datę powyżej, zanim zmiana dotrze do aplikacji.</p>
'''


# >>> guías traídas del inglés (ensamblar.py)
# Adaptadas con Ollama (qwen3.6:35b) desde las guías inglesas y auditadas por Opus el 22-nov. Rutas en idiomas_sitio.py.
GUIAS += [
  dict(clave='no-sub', corto='Aplikacja pilot bez subskrypcji', fecha='2026-11-23',
    titulo='Aplikacja pilot do TV bez subskrypcji i reklam',
    desc='Męczą Cię aplikacje pilota z reklamami albo tygodniową subskrypcją? Mando TV jest darmowe i bez reklam, Pro to opcjonalny jednorazowy zakup. Uczciwe porównanie.',
    h1='Aplikacja pilot bez subskrypcji i bez reklam',
    intro='Wiele uniwersalnych pilotów pokazuje reklamy albo wymaga tygodniowej subskrypcji, zanim zaczną działać. Mando TV idzie inną drogą: pilot jest darmowy, nie ma reklam ani konta. Opcjonalne Pro kupujesz tylko raz. Oto porównanie, także z tym, czego aplikacja nie potrafi.',
    pasos=[
      'Przed instalacją otwórz stronę aplikacji w sklepie i sprawdź zakupy w aplikacji. Ceny tygodniowe lub miesięczne wskazują na subskrypcję.',
      'W Google Play sprawdź, czy na stronie jest napis „Zawiera reklamy”, i przeczytaj najnowsze opinie z małą liczbą gwiazdek: tam często wychodzą nieoczekiwane blokady płatności.',
      'Upewnij się, że aplikacja steruje Twoim telewizorem przez Wi-Fi. Mando TV działa z Samsung (od 2016), LG webOS, Roku, Google TV, Android TV i Fire TV.',
      'Zainstaluj Mando TV, połącz telefon z tą samą siecią Wi-Fi co telewizor i stuknij swój telewizor na liście.',
      'Zaakceptuj prośbę w telewizorze albo wpisz pokazany kod. Przyciski, głośność, kanały i klawiatura nic nie kosztują.',
    ],
    tabla=dict(titulo='Mando TV w porównaniu z wieloma aplikacjami pilota',
      cabeza=['', 'Mando TV', 'Wiele aplikacji z reklamami lub subskrypcją'],
      filas=[
        ['Podstawowy pilot', 'Za darmo', 'Często za darmo z reklamami albo ukryty za okresem próbnym'],
        ['Reklamy', 'Brak', 'Często'],
        ['Subskrypcja', 'Brak. Pro to opcjonalny jednorazowy zakup', 'Plany tygodniowe lub miesięczne są powszechne'],
        ['Konto', 'Niepotrzebne', 'Różnie'],
        ['Smart TV przez Wi-Fi', 'Samsung (od 2016), LG webOS, Roku, Google TV, Android TV, Fire TV, Apple TV (beta)', 'Zależy od aplikacji'],
        ['Podczerwień dla starszych telewizorów', 'Za darmo w telefonach z Androidem z nadajnikiem podczerwieni (nowość)', 'Niektóre aplikacje, tylko w telefonach z nadajnikiem podczerwieni'],
        ['Bluetooth', 'Beta od Androida 9, za darmo', 'Zależy od aplikacji'],
        ['Zdjęcia i filmy na telewizor', 'Pro, przez Wi-Fi (bez duplikowania ekranu)', 'Zależy od aplikacji'],
        ['Telefony i komputery', 'iPhone, iPad, Mac i Windows, a także Android we wczesnym dostępie', 'Różnie'],
        ['Duplikowanie ekranu', 'Za darmo na iPhone, iPad i Windows dzięki wbudowanej funkcji każdego z nich. W Windows Pro może też duplikować ekran komputera na telewizory LG, Samsung, Hisense i Android TV (beta)', 'Niektóre aplikacje to oferują'],
      ],
      nota='Mando TV nie jest porównywane z żadną konkretną aplikacją. Aktualne ceny są na stronie danej aplikacji w sklepie.'),
    extra=[
      ('Czego Mando TV nie robi', 'Na iPhone i iPad kieruje Cię do Powielania ekranu w Centrum sterowania, czyli funkcji samego iPhone, która działa z telewizorami z AirPlay. W Windows otwiera funkcję Prześlij (Windows + K), a Mando TV Pro może wysyłać ekran komputera przez Twoje Wi-Fi na telewizory LG, Samsung, Hisense i Android TV (beta, z kilkusekundowym opóźnieniem i bez dźwięku). Z Mando TV Pro może też wysyłać zdjęcia i filmy na telewizor przez Twoje Wi-Fi. Steruje smart TV przez domowe Wi-Fi. Telewizory bez funkcji smart TV można sterować podczerwienią z telefonu z Androidem z nadajnikiem podczerwieni. Od Androida 9 telefon może też połączyć się przez Bluetooth jako klawiatura i pilot z Google TV, Android TV i Fire TV, zupełnie bez Wi-Fi. Ta opcja jest w wersji beta i za darmo.'),
      ('Jak Mando TV zarabia', 'Nie na reklamach i nie na Twoich danych: aplikacja żadnych nie zbiera. Mando TV utrzymuje się z Pro, opcjonalnego jednorazowego zakupu z dodatkami. Podstawowy pilot jest darmowy.'),
      ('Na urządzeniach, które już masz', 'iPhone, iPad i Mac z App Store, komputery z Windows z Microsoft Store i Android przez darmowy wczesny dostęp w Google Play. Zobacz [Aplikacja pilot na iPhone](@iphone) i [Aplikacja pilot na Windows](@windows).'),
      ('Prywatność', 'Bez konta i bez śledzenia w aplikacji. Komunikacja z telewizorem odbywa się tylko w sieci lokalnej, a dane połączenia zostają zaszyfrowane na Twoim urządzeniu. Szczegóły w [Polityce prywatności](@privacidad).'),
    ],
    marca=None,
    faq=[
      ('Czy jest aplikacja pilot bez subskrypcji?', 'Tak. Mando TV w ogóle nie ma subskrypcji: pilot jest darmowy i bez reklam, a Pro to opcjonalny jednorazowy zakup.'),
      ('Czy Mando TV naprawdę jest darmowe?', 'Tak. Strzałki, OK, Wstecz, Ekran główny, głośność, kanały, cyfry, klawiatura oraz włączanie i wyłączanie są darmowe, bez reklam i bez limitu czasu.'),
      ('Czy działa bez Wi-Fi?', 'Najczęściej nie. Mando TV steruje smart TV przez Twoje domowe Wi-Fi. Wyjątki: podczerwień w telefonach z Androidem z nadajnikiem podczerwieni, która działa także z telewizorami bez funkcji smart TV lub bez połączenia z Wi-Fi, oraz Bluetooth, w wersji beta od Androida 9, dla Google TV, Android TV i Fire TV.'),
    ]),
  dict(clave='roku-app-alt', corto='Alternatywa dla aplikacji Roku', fecha='2026-11-23',
    titulo='Alternatywa dla aplikacji Roku: prosty pilot Roku',
    desc='Alternatywa dla aplikacji Roku jako pilot: Mando TV steruje telewizorami i odtwarzaczami Roku przez Wi-Fi, bez konta i reklam, a także Samsung, LG i Google TV.',
    h1='Alternatywa dla aplikacji Roku: jedna do wszystkich telewizorów',
    intro='Oficjalna aplikacja Roku potrafi dużo: sklep z kanałami, przesyłanie, Private Listening i pilot. Jeśli szukasz tylko szybkiego pilota albo w domu masz też telewizor Samsung, LG lub Google TV, Mando TV to prosta alternatywa, która steruje Roku przez Twoje Wi-Fi bez konta.',
    pasos=[
      'Połącz telefon i Roku z tą samą siecią Wi-Fi.',
      'Pobierz Mando TV i otwórz aplikację. Twój telewizor Roku lub odtwarzacz Roku pojawi się na liście. Stuknij go. Roku nie prosi o kod.',
      'Używaj strzałek, OK, Wstecz, Ekranu głównego, głośności i klawiatury. Wpisuj wyszukiwane hasła w kanałach Roku na klawiaturze telefonu.',
      'Jeśli przyciski nic nie robią, w Roku wejdź w Ustawienia > System > Zaawansowane ustawienia systemu > Sterowanie przez aplikacje mobilne i ustaw Dostęp do sieci na Domyślny lub Zezwalający (w nowszym oprogramowaniu Roku ustaw Sterowanie przez aplikacje mobilne na Włączone).',
      'Opcjonalnie: w telewizorze Roku włącz „Szybkie uruchamianie TV” w Ustawienia > System > Zasilanie, żeby Mando TV mogło włączać telewizor.',
    ],
    extra=[
      ('Gdzie Mando TV pasuje lepiej', 'Jedna aplikacja do kilku telewizorów: Roku, Samsung, LG oraz Google TV lub Android TV. Bez konta i bez reklam. Działa też na komputerze z Windows, co przy biurku jest wygodne. Strzałki i głośność reagują szybko, a klawiaturą wpiszesz wyszukiwane hasła bez wysiłku.'),
      ('Gdzie oficjalna aplikacja Roku jest lepsza', 'Zostaw aplikację Roku do tego, co oferuje poza pilotem, jak przeglądanie i dodawanie kanałów ze sklepu Roku Channel Store oraz własne przesyłanie i Private Listening (dźwięk w słuchawkach podłączonych do telefonu). Używaj obu, jeśli chcesz. Mogą działać na tym samym telefonie.'),
      ('Telewizory Roku TV i odtwarzacze Roku', 'Działają oba. Obejmuje to modele Roku TV marek TCL, Hisense, Philips i innych oraz Roku Express, Streaming Stick i Ultra. Szczegóły znajdziesz na [stronie aplikacji pilot do Roku](@roku).'),
      ('Gdy aplikacja Roku przestała działać', 'Jeśli przyciski przestały reagować, Roku zwykle blokuje sterowanie przez aplikacje. Poradnik [Aplikacja Roku nie działa](@roku-403) pokazuje ustawienie, które rozwiązuje problem.'),
      ('Za darmo i Pro', 'Strzałki, OK, Wstecz, Ekran główny, głośność, kanały, klawisze cyfr, klawiatura, otwieranie aplikacji, zmiana źródeł oraz włączanie i wyłączanie są darmowe, bez reklam i bez subskrypcji. Touchpad, polecenia głosowe, ulubione aplikacje, rutyny i wyłącznik czasowy należą do Mando TV Pro, jednorazowego zakupu bez subskrypcji.'),
    ],
    marca='roku',
    faq=[
      ('Czy potrzebuję konta Roku, żeby używać Mando TV?', 'Nie. Mando TV komunikuje się z Roku przez Twoją sieć domową i nie prosi o konto.'),
      ('Czy Mando TV w pełni zastępuje aplikację Roku Mobile?', 'Jako pilot tak. Do sklepu z kanałami, przesyłania i Private Listening zostaw oficjalną aplikację Roku.'),
      ('Czy działa z moim Roku Express lub Streaming Stick?', 'Tak. Wszystkie odtwarzacze Roku i telewizory Roku TV steruje się w ten sam sposób.'),
    ]),
  dict(clave='lg-thinq', corto='Alternatywa dla LG ThinQ', fecha='2026-11-23',
    titulo='Alternatywa dla LG ThinQ: pilot LG bez konta',
    desc='Szukasz alternatywy dla aplikacji LG ThinQ tylko jako pilota? Mando TV steruje telewizorami LG z webOS przez Wi-Fi, bez konta LG i bez reklam.',
    h1='Alternatywa dla aplikacji LG ThinQ do Twojego telewizora LG',
    intro='LG ThinQ to oficjalna aplikacja LG, stworzona dla całego inteligentnego domu: sprzętu AGD, telewizora i nie tylko. Jeśli chcesz tylko prostego pilota do telewizora LG, Mando TV robi dokładnie to przez Twoje domowe Wi-Fi, bez zakładania konta LG i bez reklam.',
    pasos=[
      'Połącz telefon lub komputer (iPhone, Android lub Windows) i telewizor LG z tą samą siecią Wi-Fi.',
      'Pobierz Mando TV i otwórz aplikację. Twój telewizor LG sam pojawi się na liście. Stuknij go.',
      'Na telewizorze pojawi się prośba. Zaakceptuj ją raz pilotem telewizora, joystickiem pod ekranem albo Magic Remote.',
      'Przyciski, głośność i klawiatura działają od razu. Nie potrzebujesz konta LG ani rejestracji telewizora.',
      'Opcjonalnie: włącz w ustawieniach telewizora „Włącz TV przez urządzenie mobilne”, żeby móc włączać telewizor także z telefonu.',
    ],
    extra=[
      ('Mando TV czy LG ThinQ: co do czego', 'Używaj ThinQ, gdy chcesz zarządzać sprzętem AGD LG, jak pralka, lodówka czy klimatyzator, albo potrzebujesz funkcji konta LG. Używaj Mando TV, gdy chcesz szybkiego, prostego pilota do telewizora, który w tej samej aplikacji działa też z Samsung, Roku i Google TV. Wiele osób zostawia obie: ThinQ do sprzętu AGD, Mando TV do telewizora.'),
      ('Co Mando TV robi w telewizorze LG', 'Działa ze smart TV LG z webOS, czyli z większością modeli od 2014 roku, w tym LED, NanoCell, QNED i OLED. Daje strzałki, OK, Wstecz, Ekran główny, głośność, kanały, wyciszenie, sterowanie odtwarzaniem i klawiaturę do pisania w YouTube, Netflix lub przeglądarce. Lista aplikacji i lista źródeł też są darmowe. W Pro dostajesz dodatkowo wskaźnik jak w Magic Remote.'),
      ('Czego Mando TV nie robi', 'Nie steruje sprzętem AGD LG, nie używa Twojego konta LG i nie zastępuje usług konta LG w telewizorze. To pilot, a nie centrala smart home.'),
      ('Prywatność i reklamy', 'Mando TV nie ma reklam ani konta. Rozmawia z telewizorem tylko w Twojej sieci domowej i zapisuje klucz połączenia w zaszyfrowanej postaci na Twoim urządzeniu. Wszystkie funkcje znajdziesz na stronie [Aplikacja pilot do LG](@lg).'),
      ('Za darmo i Pro', 'Strzałki, OK, Wstecz, Ekran główny, głośność, kanały, klawisze cyfr, klawiatura, otwieranie aplikacji, zmiana źródeł oraz włączanie i wyłączanie są darmowe, bez reklam i bez subskrypcji. Touchpad, polecenia głosowe, ulubione aplikacje, rutyny i wyłącznik czasowy należą do Mando TV Pro, jednorazowego zakupu bez subskrypcji.'),
    ],
    marca='lg',
    faq=[
      ('Czy mogę sterować telewizorem LG bez aplikacji LG ThinQ?', 'Tak. Mando TV łączy się bezpośrednio przez Twoje Wi-Fi z telewizorami LG z webOS. Raz akceptujesz prośbę w telewizorze i to wszystko, zupełnie bez konta LG.'),
      ('Czy Mando TV działa ze wskaźnikiem LG Magic Remote?', 'Mando TV Pro ma wskaźnik, który poruszasz palcem po ekranie telefonu, podobnie jak Magic Remote porusza strzałką.'),
      ('Czy Mando TV jest od LG?', 'Nie. Mando TV to niezależna aplikacja i nie jest powiązana z LG. LG i ThinQ należą do swoich właścicieli i są wymieniane wyłącznie po to, by opisać zgodność.'),
    ]),
  dict(clave='smartthings', corto='Alternatywa dla SmartThings', fecha='2026-11-23',
    titulo='SmartThings nie działa? Prosta alternatywa dla Samsung',
    desc='SmartThings za wolne albo z błędami? Mando TV steruje telewizorami Samsung z Tizen bezpośrednio przez Wi-Fi. Bez konta Samsung, bez reklam. Krok po kroku.',
    h1='Alternatywa dla SmartThings do telewizorów Samsung',
    intro='SmartThings to aplikacja Samsung do całego inteligentnego domu, a jej pilot działa przez Twoje konto Samsung. Jeśli przestała działać albo szukasz szybkiego rozwiązania, Mando TV steruje telewizorami Samsung z Tizen, rocznik 2016 i nowsze, bezpośrednio przez Wi-Fi, bez konta.',
    pasos=[
      'Połącz telefon i telewizor Samsung z tą samą siecią Wi-Fi.',
      'Pobierz Mando TV i otwórz aplikację. Twój telewizor Samsung sam pojawi się na liście. Stuknij go.',
      'Telewizor zapyta, czy zezwalasz na połączenie. Wybierz „Zezwól” pilotem albo przyciskiem na telewizorze (tylko za pierwszym razem).',
      'Od razu używaj strzałek, OK, Wstecz, Ekranu głównego, głośności, kanałów i klawiatury.',
      'Opcjonalnie: włącz „Włączanie przez urządzenie mobilne” w Ustawienia > Ogólne > Sieć > Ustawienia ekspertów, żeby Mando TV mogło też włączać telewizor.',
    ],
    extra=[
      ('Dlaczego pilot w telefonie przestał działać', 'Przyczyny są zwykle proste: telefon i telewizor są w różnych sieciach Wi-Fi, włączony jest VPN albo telewizor jest w głębokim czuwaniu. W SmartThings problem może też robić konto Samsung, na przykład gdy zostałeś wylogowany. Mando TV rozmawia bezpośrednio z telewizorem w sieci domowej, nie ma konta do logowania. Więcej wskazówek znajdziesz w [Telefon nie widzi telewizora](@not-found).'),
      ('Mando TV czy SmartThings: co do czego', 'Zostaw SmartThings, jeśli używasz go do sprzętu AGD Samsung, lamp lub innych urządzeń smart home albo do funkcji konta Samsung. Używaj Mando TV, gdy chcesz po prostu szybkiego pilota do telewizora albo w domu masz też urządzenie LG, Roku, Google TV lub Fire TV: jedna aplikacja steruje wszystkimi. Obie aplikacje mogą być zainstalowane na tym samym telefonie.'),
      ('Jeśli zgoda została odrzucona przez pomyłkę', 'W telewizorze otwórz Ustawienia > Ogólne > Menedżer urządzeń zewnętrznych > Menedżer połączeń urządzeń i ustaw Mando TV jako dozwolone.'),
      ('Nie masz pilota?', 'Prośbę możesz zaakceptować przyciskiem na samym telewizorze. Poradnik [Telewizor Samsung bez oryginalnego pilota](@samsung-lost) pokazuje, jak to zrobić.'),
      ('Za darmo i Pro', 'Pilot możesz pobrać i używać za darmo, bez reklam i bez subskrypcji. Mando TV Pro to opcjonalny jednorazowy zakup z dodatkami.'),
    ],
    marca='samsung',
    faq=[
      ('Czy mogę sterować telewizorem Samsung bez SmartThings?', 'Tak. Mando TV łączy się bezpośrednio przez Twoje Wi-Fi z telewizorami Samsung z Tizen. Raz zezwalasz na połączenie w telewizorze, bez konta Samsung.'),
      ('Czy Mando TV steruje też sprzętem AGD Samsung?', 'Nie. To tylko pilot do telewizora. Do sprzętu AGD i innych urządzeń smart home zostawiasz SmartThings.'),
      ('Czy Mando TV jest od Samsung?', 'Nie. Mando TV to niezależna aplikacja i nie jest powiązana z Samsung. Samsung i SmartThings należą do swoich właścicieli i są wymieniane wyłącznie po to, by opisać zgodność.'),
    ]),
  dict(clave='googletv-alt', corto='Alternatywa dla pilota Google TV', fecha='2026-11-23',
    titulo='Pilot Google TV nie działa? Alternatywa',
    desc='Pilot Google TV w telefonie nie widzi telewizora? Mando TV steruje Google TV i Android TV przez Wi-Fi, bez konta Google i reklam.',
    h1='Alternatywa dla pilota Google TV w telefonie',
    intro='Pilot w telefonie do Google TV i Android TV jest wbudowany w samą aplikację Google i powiązany z Twoim kontem Google. Jeśli nie widzi telewizora, utkniesz. Mando TV to osobna aplikacja pilot, która paruje się 6-znakowym kodem z ekranu i działa bez konta Google, na iPhone, telefonie z Androidem lub komputerze z Windows.',
    pasos=[
      'Włącz telewizor i połącz telefon z tą samą siecią Wi-Fi.',
      'Pobierz Mando TV i otwórz aplikację. Stuknij na liście swój telewizor z Google TV lub Android TV.',
      'Telewizor pokaże 6-znakowy kod. Wpisz go w Mando TV i stuknij Sparuj.',
      'Używaj strzałek, OK, Wstecz, Ekranu głównego, głośności i klawiatury. Nigdzie nie musisz się logować.',
      'Opcjonalnie: w ustawieniach telewizora poszukaj Wake on LAN albo „Włączanie przez sieć”, żeby aplikacja mogła też włączać telewizor.',
    ],
    extra=[
      ('Dlaczego pilot w telefonie przestał widzieć telewizor', 'Najczęściej to kwestia sieci: telefon i telewizor są w różnych sieciach Wi-Fi, włączony jest VPN albo sieć dla gości izoluje urządzenia. Napraw to najpierw, bo dotyczy wszystkich aplikacji pilota. Więcej w [Telefon nie widzi telewizora](@not-found).'),
      ('Z jakimi telewizorami działa', 'Telewizory z Google TV i Android TV marek Sony, TCL, Hisense, Philips, Sharp, Xiaomi, Toshiba i innych, a także Chromecast z Google TV, Google TV Streamer i Nvidia Shield. Wszystkie paruje się tak samo, jednorazowo kodem z ekranu.'),
      ('Gdzie aplikacja Google jest lepsza', 'Aplikacja Google pomaga też znaleźć treści do obejrzenia i pamięta Twoją listę do obejrzenia. Zostaw ją do tego. Mando TV to tylko pilot, a dodatkowo steruje urządzeniami Samsung, LG, Roku i Fire TV z tej samej aplikacji oraz z komputera z Windows.'),
      ('Jeśli brakuje starej aplikacji pilot do Android TV', 'Google przeniosło pilot w telefonie ze starej aplikacji Android TV Remote Control do aplikacji Google TV. Jeśli szukasz samodzielnego pilota, Mando TV to jedna z opcji.'),
      ('Za darmo i Pro', 'Pilot możesz pobrać i używać za darmo, bez reklam i bez subskrypcji. Mando TV Pro to opcjonalny jednorazowy zakup z dodatkami.'),
    ],
    marca='android',
    faq=[
      ('Czy potrzebuję konta Google, żeby używać Mando TV z Google TV?', 'Nie. Do sparowania wystarczy kod z telewizora.'),
      ('Czy działa z Chromecast z Google TV?', 'Tak. Parowanie przebiega tak samo, 6-znakowym kodem z ekranu.'),
      ('Czy mogę używać go na iPhone?', 'Tak. Mando TV jest dostępne w App Store na iPhone i iPad, w Microsoft Store na Windows oraz w darmowym wczesnym dostępie w Google Play na Androida.'),
    ]),
  dict(clave='windows', corto='Pilot na komputer z Windows', fecha='2026-11-23',
    titulo='Aplikacja pilot na Windows: telewizor z komputera',
    desc='Steruj Samsung, LG, Roku, Google TV lub Fire TV z komputera z Windows dzięki Mando TV: skróty klawiszowe, mini pilot i Wi-Fi. W Microsoft Store.',
    h1='Aplikacja pilot na komputer z Windows',
    intro='Mando TV ma aplikację na Windows, która zamienia Twój komputer lub laptop w pilota do telewizora przez sieć domową. Pisz w telewizorze na prawdziwej klawiaturze, zostaw podczas pracy małe okno pilota na wierzchu i steruj Samsung, LG, Roku, Google TV lub Fire TV tą samą aplikacją.',
    pasos=[
      'Zainstaluj Mando TV za darmo z Microsoft Store na komputerze z Windows 10 lub 11.',
      'Upewnij się, że komputer i telewizor są w tej samej sieci, przez Wi-Fi lub kabel do tego samego routera.',
      'Otwórz Mando TV. Telewizor pojawi się na liście. Kliknij go.',
      'Zaakceptuj prośbę w telewizorze, jeśli o nią pyta (LG, Samsung), albo wpisz pokazany kod (Google TV, Fire TV).',
      'Klikaj przyciski albo wpisz wyszukiwane hasło na klawiaturze. Gotowe.',
    ],
    extra=[
      ('Skróty klawiszowe (Pro)', 'W Pro klawiatura komputera staje się pilotem: strzałki do poruszania się, Enter jako OK, Backspace lub Esc do cofania, plus i minus do głośności, M do wyciszenia i spacja do pauzy.'),
      ('Mini pilot (Pro)', 'Małe okno pilota, które zostaje nad wszystkimi innymi oknami. Dzięki temu zmienisz głośność albo wstrzymasz odtwarzanie bez przerywania pracy.'),
      ('Pisanie w telewizorze z komputera', 'Klawiatura ekranowa telewizora jest powolna. W Mando TV piszesz na prawdziwej klawiaturze, a tekst trafia do pola wyszukiwania telewizora. Ta część jest darmowa.'),
      ('Więcej szczegółów', 'Instrukcję krok po kroku znajdziesz w [Sterowanie telewizorem z komputera](@pc). Dla telefonu przeczytaj [Telefon jako pilot przez Wi-Fi](@wifi).'),
      ('Za darmo i Pro', 'Strzałki, OK, Wstecz, Ekran główny, głośność, kanały, klawisze cyfr, klawiatura, otwieranie aplikacji, zmiana źródeł oraz włączanie i wyłączanie są darmowe, bez reklam i bez subskrypcji. Touchpad, polecenia głosowe, ulubione aplikacje, rutyny i wyłącznik czasowy należą do Mando TV Pro, jednorazowego zakupu bez subskrypcji. W Windows Pro kupujesz przez Microsoft Store.'),
      ('Polecenia głosowe z komputera (Pro)', 'W Pro możesz mówić do telewizora przez mikrofon komputera. Mowa jest rozpoznawana bezpośrednio na komputerze: nie potrzebujesz internetu i nie musisz niczego ustawiać w Windows. To, co mówisz, nigdy nie opuszcza komputera i nie jest zapisywane. Tylko w bardzo starych procesorach aplikacja przechodzi na pisanie głosowe Windows. Wtedy musi być włączone rozpoznawanie mowy online w ustawieniach prywatności i dodany w Windows Twój język.'),
    ],
    marca=None,
    faq=[
      ('Czy aplikacja pilot na Windows potrzebuje Bluetooth albo kabla?', 'Nie. Używa Twojej sieci domowej. Komputer i telewizor muszą tylko być podłączone do tego samego routera.'),
      ('Jakimi telewizorami mogę sterować z Windows?', 'Telewizorami Samsung z Tizen, LG z webOS, Roku TV i odtwarzaczami Roku, Google TV i Android TV oraz Fire TV.'),
      ('Czy mogę oglądać obraz z telewizora na komputerze albo słuchać go przez głośniki komputera?', 'Nie. Mando TV to tylko pilot. Nie duplikuje ani nie przesyła obrazu z telewizora na komputer.'),
      ('Dlaczego głos nie działa na moim komputerze z Windows?', 'Sterowanie głosem to funkcja Pro. Sprawdź więc, czy Pro jest aktywne, a mikrofon komputera działa. Na większości komputerów mowa jest rozpoznawana bezpośrednio na komputerze, bez internetu. Tylko w bardzo starych procesorach aplikacja używa pisania głosowego Windows: wtedy włącz rozpoznawanie mowy online w ustawieniach prywatności Windows i dodaj swój język w ustawieniach języka.'),
    ]),
  dict(clave='iphone', corto='Aplikacja pilot na iPhone', fecha='2026-11-23',
    titulo='Aplikacja pilot na iPhone: Samsung, LG, Roku, Google TV',
    desc='Używaj iPhone jako pilota do Samsung, LG, Roku, Google TV i Fire TV przez Wi-Fi. Za darmo w App Store, bez konta i bez reklam.',
    h1='Aplikacja pilot na iPhone: jedna do wszystkich telewizorów',
    intro='Mando TV zamienia iPhone lub iPad w pilota do Samsung, LG, Roku, Google TV lub Android TV oraz Fire TV, przez Twoje domowe Wi-Fi. Aplikacja jest darmowa w App Store, bez konta i bez reklam. Działa też na Androidzie i w Windows.',
    pasos=[
      'Pobierz Mando TV za darmo z App Store.',
      'Połącz iPhone i telewizor z tą samą siecią Wi-Fi.',
      'Otwórz Mando TV i stuknij Zezwól, gdy iOS zapyta o dostęp do sieci lokalnej. Aplikacja potrzebuje go, żeby znaleźć telewizor.',
      'Stuknij na liście swój telewizor. Zaakceptuj prośbę w telewizorze, jeśli o nią pyta (LG i Samsung), albo wpisz kod, który pokazuje telewizor (Google TV lub Fire TV).',
      'Używaj przycisków, głośności i klawiatury. Jesteś połączony.',
    ],
    extra=[
      ('Działa z tymi telewizorami', 'LG webOS, Samsung Tizen (rocznik 2016 i nowsze), Roku TV i odtwarzacze Roku, Google TV i Android TV oraz Fire TV. Strony marek to [Samsung](@samsung), [LG](@lg), [Roku](@roku) i [Android TV](@android).'),
      ('Dlaczego prosi o sieć lokalną', 'iPhone blokuje aplikacjom dostęp do urządzeń w Twojej sieci domowej, dopóki na to nie zezwolisz. Jeśli telewizor nie pojawia się na liście, otwórz Ustawienia > Mando TV i włącz „Sieć lokalna”. Aplikacja komunikuje się tylko z Twoim telewizorem w Twojej sieci domowej.'),
      ('Dlaczego Mando TV, a nie aplikacja producenta', 'Każda marka telewizorów ma własną aplikację i chce własnej konfiguracji lub konta. Mando TV to jedna aplikacja do wszystkich, bez konta.'),
      ('Za darmo i Pro na iPhone', 'Strzałki, OK, Wstecz, Ekran główny, głośność, kanały, klawisze cyfr, klawiatura, otwieranie aplikacji, zmiana źródeł oraz włączanie i wyłączanie są darmowe, bez reklam i bez subskrypcji. Touchpad, polecenia głosowe, ulubione aplikacje, rutyny i wyłącznik czasowy należą do Mando TV Pro, jednorazowego zakupu bez subskrypcji. Pro kupujesz raz, prosto w aplikacji.'),
    ],
    marca=None,
    faq=[
      ('Czy Mando TV na iPhone jest darmowe?', 'Pobranie jest darmowe, bez reklam. Podstawowy pilot jest darmowy, tak samo jak otwieranie aplikacji i zmiana źródeł. Dodatki, takie jak touchpad, polecenia głosowe i rutyny, należą do Mando TV Pro, jednorazowego zakupu.'),
      ('Czy działa na iPad?', 'Tak. Ta sama aplikacja działa na iPhone i iPad.'),
      ('Czy aplikacja pilot na iPhone potrzebuje Bluetooth albo nadajnika podczerwieni?', 'Nie na iPhone. iPhone nie ma nadajnika podczerwieni, więc sterowanie podczerwienią nie jest tam dostępne, a opcja Bluetooth jest tylko dla Androida 9 lub nowszego, nie dla iPhone. Na iPhone Mando TV steruje smart TV oraz Apple TV (beta) przez Twoje domowe Wi-Fi.'),
    ]),
  dict(clave='firetv', corto='Pilot Fire TV', fecha='2026-11-23',
    titulo='Aplikacja pilot do Fire TV na telefon i komputer',
    desc='Pilot do Fire TV w telefonie: steruj Fire TV Stick, Fire TV Cube lub telewizorem z Fire TV przez Wi-Fi, z 4-cyfrowym kodem PIN. Bez aplikacji Amazon.',
    h1='Pilot do Fire TV na telefon lub komputer',
    intro='Jeśli pilot do Fire TV zginął albo wyczerpały się baterie, Mando TV steruje Fire TV Stick, Fire TV Cube lub telewizorem z wbudowanym Fire TV przez Wi-Fi. Parowanie odbywa się 4-cyfrowym kodem PIN. Fire TV to nowość w Mando TV, więc najpierw zaktualizuj aplikację.',
    pasos=[
      'Zaktualizuj Mando TV do najnowszej wersji z App Store, Microsoft Store lub Google Play.',
      'Włącz Fire TV i połącz telefon z tą samą siecią Wi-Fi.',
      'Otwórz Mando TV. Twój Fire TV pojawi się na liście. Stuknij go.',
      'Na ekranie telewizora pojawi się 4-cyfrowy kod PIN. Wpisz go w Mando TV. Robisz to tylko raz.',
      'Używaj strzałek, OK, Wstecz, Ekranu głównego, przycisków odtwarzania i klawiatury do wyszukiwania.',
    ],
    extra=[
      ('Obsługiwane urządzenia Fire TV', 'Fire TV Stick, Fire TV Stick 4K, Fire TV Cube i telewizory z wbudowanym Fire TV, takie jak telewizory Amazon Fire TV Edition i niektóre modele Hisense. Obsługa jest nowa i dotąd mogliśmy przetestować tylko kilka prawdziwych urządzeń. Jeśli coś nie działa tak, jak powinno, napisz do nas, jaki masz model, przez stronę pomocy.'),
      ('Włączanie Fire TV', 'Mando TV nie włącza Fire TV przez sieć. Włącz telewizor przyciskiem zasilania na obudowie: podłączony Fire TV Stick lub Cube zwykle budzi się przez HDMI-CEC, a w telewizorze z wbudowanym Fire TV telewizor jest Fire TV. Potem sterujesz nim z telefonu.'),
      ('Jeśli Twój Fire TV się nie pojawia', 'Upewnij się, że oba urządzenia są w tej samej sieci Wi-Fi, a Fire TV nie śpi. Na iPhone zezwól w ustawieniach na „Sieć lokalna” dla Mando TV. Zobacz [Telefon nie widzi telewizora](@not-found).'),
      ('Nie masz żadnego pilota?', 'Fire TV musi pokazać kod PIN na ekranie, więc telewizor i Fire TV muszą być włączone i pokazywać obraz. Jeśli telewizor jest na złym wejściu, zmień je przyciskami na telewizorze. Zobacz [Zmiana wejścia bez pilota](@hdmi).'),
      ('Za darmo i Pro', 'Strzałki, OK, Wstecz, Ekran główny, głośność, kanały, cyfry, klawiatura, otwieranie aplikacji, zmiana źródeł oraz włączanie i wyłączanie są darmowe, bez reklam i bez subskrypcji. Touchpad, polecenia głosowe, ulubione aplikacje, rutyny i wyłącznik czasowy należą do Mando TV Pro, jednorazowego zakupu bez subskrypcji.'),
    ],
    marca=None,
    faq=[
      ('Czy potrzebuję aplikacji Amazon Fire TV?', 'Nie. Mando TV łączy się z Fire TV przez Twoje Wi-Fi za pomocą kodu PIN. Nie potrzebujesz konta Amazon w telefonie.'),
      ('Czy działa z telewizorami z Fire TV i z Fire TV Stick?', 'Tak, do tego został stworzony. Obsługa jest nowa, aktualizuj aplikację i daj nam znać o modelach, które nie działają tak, jak powinny.'),
      ('Dlaczego potrzebuję kodu PIN?', 'Fire TV pokazuje 4-cyfrowy kod PIN, żeby dowieść, że siedzisz przed telewizorem. Nikt nie sparuje urządzenia, nie widząc ekranu.'),
    ]),
  dict(clave='firetv-lost', corto='Zgubiony pilot Fire TV', fecha='2026-11-23',
    titulo='Zgubiony pilot Fire TV? Pomoże Ci telefon',
    desc='Zgubiony pilot do Fire TV Stick? Steruj nim telefonem przez Wi-Fi, parowanie 4-cyfrowym kodem PIN. Wskazówki dla nowego Wi-Fi i HDMI-CEC.',
    h1='Zgubiony pilot Fire TV: jak użyć telefonu',
    intro='Jeśli pilot do Fire TV Stick, Fire TV Cube lub smart TV z Fire TV zginął albo przestał działać, sterowanie przejmie telefon, o ile Fire TV jest nadal połączony z Twoim Wi-Fi. Parowanie odbywa się 4-cyfrowym kodem PIN na ekranie, więc starego pilota nigdy do tego nie potrzebujesz.',
    pasos=[
      'Włącz telewizor przyciskiem na obudowie. Podłączony Fire TV Stick lub Cube zwykle budzi się razem z nim; przy włączonym HDMI-CEC telewizor często sam przełącza się na jego wejście.',
      'Jeśli telewizor pokazuje inne wejście, zmień je przyciskiem wejść lub źródła na telewizorze. Zobacz [Zmiana wejścia bez pilota](@hdmi).',
      'Połącz telefon z tą samą siecią Wi-Fi co Fire TV.',
      'Pobierz Mando TV i otwórz aplikację. Twój Fire TV pojawi się na liście. Stuknij go.',
      'Telewizor pokaże 4-cyfrowy kod PIN. Wpisz go w Mando TV. Robisz to tylko raz.',
      'Używaj strzałek, OK, Wstecz, Ekranu głównego, głośności, przycisków odtwarzania i klawiatury w telefonie.',
    ],
    extra=[
      ('Najpierw wypróbuj pilota od telewizora (HDMI-CEC)', 'Wiele pilotów do telewizorów potrafi sterować Fire TV Stick przez HDMI-CEC. Gdy widać interfejs Fire TV, naciśnij strzałki i OK na pilocie telewizora. Jeśli nic się nie dzieje, włącz CEC w ustawieniach telewizora (Anynet+ w Samsung, SIMPLINK w LG, BRAVIA Sync w Sony), a w Fire TV włącz sterowanie urządzeniami HDMI CEC w ustawieniach wyświetlacza („Wyświetlacz i dźwięki”).'),
      ('Jeśli zmieniłeś Wi-Fi', 'Bez pilota nie wpiszesz hasła nowego Wi-Fi w Fire TV, ale jest wyjście: na drugim telefonie utwórz hotspot z dokładnie taką samą nazwą i hasłem jak stare Wi-Fi. Fire TV połączy się z nim automatycznie. Połącz telefon z Mando TV z tym hotspotem, sparuj go kodem PIN, potem w Fire TV wejdź w Ustawienia > Sieć i wybierz nowe Wi-Fi. Na koniec połącz też telefon z nowym Wi-Fi.'),
      ('Parowanie zapasowego pilota', 'Większość nowych pilotów Fire TV paruje się przez przytrzymanie przycisku Home przez około 10 sekund, w pobliżu Fire TV. Jeśli się nie uda, otwórz Ustawienia > Kontrolery i urządzenia Bluetooth > Piloty Amazon Fire TV > Dodaj nowy pilot. To menu osiągniesz też z telefonu przez Mando TV.'),
      ('Fire TV wbudowany w telewizor', 'W telewizorach z wbudowanym Fire TV, takich jak wiele modeli Insignia i Toshiba, obowiązują te same kroki, bo telewizor sam jest Fire TV.'),
      ('Zanim zaczniesz', 'Obsługa Fire TV to nowość w Mando TV. Najpierw zaktualizuj aplikację. Jeśli Twój model nie reaguje tak, jak powinien, napisz do nas przez [stronę pomocy](@soporte) i podaj model.'),
      ('Za darmo i Pro', 'Pilot możesz pobrać i używać za darmo, bez reklam i bez subskrypcji. Mando TV Pro to opcjonalny jednorazowy zakup z dodatkami.'),
    ],
    marca=('firetv', 'Pilot Fire TV'),
    faq=[
      ('Czy mogę sterować Fire TV Stick telefonem bez pilota?', 'Tak, o ile Fire TV jest włączony i połączony z Twoim Wi-Fi. Mando TV paruje się 4-cyfrowym kodem PIN z telewizora, więc stary pilot nie jest potrzebny.'),
      ('Czy działa, gdy Fire TV jest w nowym Wi-Fi?', 'Nie od razu, bo telefon i Fire TV muszą być w tej samej sieci. Najpierw przywróć Fire TV do sieci trikiem z hotspotem opisanym na tej stronie.'),
      ('Czy potrzebuję aplikacji Amazon Fire TV albo konta Amazon?', 'Nie. Mando TV łączy się z kodem PIN przez Twoją sieć domową i nie wymaga własnego konta.'),
    ]),
  dict(clave='turn-on', corto='Włączanie telewizora bez pilota', fecha='2026-11-23',
    titulo='Włączanie telewizora bez pilota (wszystkie marki)',
    desc='Jak włączyć telewizor bez pilota: gdzie jest przycisk w Samsung, LG, TCL, Hisense i Sony. Plus HDMI-CEC i triki z telefonem.',
    h1='Jak włączyć telewizor bez pilota',
    intro='Prawie każdy telewizor ma nadal fizyczny przycisk zasilania. Jest tylko dobrze schowany. Tu zobaczysz, gdzie jest w każdej marce, oraz dwa sposoby, by następnym razem nie musieć go szukać: HDMI-CEC z konsoli lub urządzenia do streamingu oraz włączanie telewizora telefonem przez Wi-Fi.',
    pasos=[
      'Spójrz pod środek ekranu, tuż za logo marki. W wielu telewizorach jest tam mały pojedynczy przycisk albo joystick skierowany w dół.',
      'Jeśli go tam nie ma, przesuń dłonią po tylnej ściance telewizora blisko dolnych rogów, potem po lewej i prawej krawędzi.',
      'Naciśnij przycisk raz. W wielu telewizorach z jednym przyciskiem krótkie naciśnięcie przy włączonym urządzeniu otwiera małe menu źródeł i głośności, a długie je wyłącza.',
      'Nadal nic? Sprawdź kabel zasilający na obu końcach i spróbuj z innego gniazdka. Jeśli dioda czuwania się nie świeci, telewizor nie dostaje prądu.',
      'Gdy telewizor jest włączony, ustaw go tak, żebyś nie potrzebował przycisku: włącz HDMI-CEC i włączanie przez sieć, oba opisane niżej.',
    ],
    extra=[
      ('Gdzie jest przycisk zasilania, według marki', 'Samsung: przycisk sterowania lub joystick pod środkiem ekranu albo z tyłu przy dolnym rogu. LG: przycisk joystick pod logo LG w większości modeli. TCL i Hisense: zwykle mały przycisk pod środkiem ekranu albo z tyłu blisko dolnego rogu. Sony: z tyłu lub na bocznej krawędzi, na dole blisko brzegu. Vizio: z tyłu, w lewym lub prawym dolnym rogu, albo z boku. Położenie zmienia się zależnie od modelu. Jeśli nie możesz go znaleźć, poszukaj instrukcji po numerze modelu z naklejki na tylnej ściance.'),
      ('Włączanie telewizora z konsoli lub urządzenia do streamingu (HDMI-CEC)', 'Przy włączonym HDMI-CEC włączenie PlayStation, Xbox, odtwarzacza Roku, Fire TV Stick lub Chromecast włącza też telewizor i przełącza na właściwe wejście. Każda marka nazywa to ustawienie inaczej: Anynet+ w Samsung, SIMPLINK w LG, BRAVIA Sync w Sony i CEC w większości innych. Więcej w [Jak włączyć telewizor i przełączyć na HDMI konsoli](@console).'),
      ('Włączanie telewizora telefonem', 'Smart TV można obudzić przez Wi-Fi, jeśli raz na to zezwolisz, a wtedy Mando TV włącza je z telefonu. W Samsung włącz „Włączanie przez urządzenie mobilne” w Ustawienia > Ogólne > Sieć > Ustawienia ekspertów. W LG włącz „Włącz TV przez urządzenie mobilne” ([krok po kroku](@lg-on)). W Roku TV włącz „Szybkie uruchamianie TV” w Ustawienia > System > Zasilanie. W Google TV i Android TV poszukaj Wake on LAN albo „Włączanie przez sieć”, jeśli Twój model to ma. Robisz to raz, przy włączonym telewizorze.'),
      ('Jeśli nie możesz znaleźć przycisku', 'Niektóre nowsze telewizory chowają jedyny przycisk tak dobrze, że wygląda, jakby go nie było. Poszukaj małego wybrzuszenia albo czujnika światła pod ekranem: przycisk często jest tuż obok. Przez Wi-Fi Mando TV potrzebuje, żeby telewizor raz był włączony i połączony. Wyjątkiem jest podczerwień: w telefonie z Androidem z nadajnikiem podczerwieni Mando TV może włączyć telewizor, który nigdy nie był konfigurowany, o ile skierujesz telefon na telewizor. Podczerwień to nowość i działa z markami z listy kodów w aplikacji.'),
      ('Za darmo i Pro', 'Pilot możesz pobrać i używać za darmo, bez reklam i bez subskrypcji. Mando TV Pro to opcjonalny jednorazowy zakup z dodatkami.'),
    ],
    marca=None,
    faq=[
      ('Czy mogę włączyć telewizor telefonem, jeśli nigdy go nie konfigurowałem?', 'Nie przez Wi-Fi. Wyłączony telewizor budzi się z sieci tylko wtedy, gdy wcześniej włączono włączanie przez sieć. Za pierwszym razem użyj przycisku na telewizorze. Wyjątkiem jest telefon z Androidem z nadajnikiem podczerwieni: Mando TV może włączyć telewizor bez konfiguracji przez podczerwień, jeśli marka jest na liście kodów albo wybierzesz „Inna marka lub nie wiem”.'),
      ('Jak włączyć telewizor Samsung bez pilota?', 'Naciśnij przycisk sterowania pod środkiem ekranu albo z tyłu przy dolnym rogu. Potem włącz „Włączanie przez urządzenie mobilne”, żeby telefon mógł go włączyć następnym razem.'),
      ('Jak włączyć Roku TV bez pilota?', 'Użyj przycisku na telewizorze, zwykle pod środkiem albo z tyłu. Potem włącz „Szybkie uruchamianie TV” w Ustawienia > System > Zasilanie, żeby Mando TV mogło go włączać z telefonu.'),
      ('Dlaczego mój telewizor włącza się sam, gdy włączam konsolę?', 'To HDMI-CEC. Jest wygodne, a jeśli wolisz, możesz je wyłączyć w ustawieniach telewizora.'),
    ]),
  dict(clave='sony', corto='Pilot Sony', fecha='2026-11-23',
    titulo='Aplikacja pilot do telewizora Sony na telefon i komputer',
    desc='Mando TV steruje telewizorami Sony Bravia z Google TV lub Android TV przez Wi-Fi. Wsparcie beta dla modeli z lat 2013 do 2015 bez Androida.',
    h1='Jak sterować telewizorem Sony z telefonu',
    intro='Nowsze smart TV Sony Bravia używają Google TV, starsze modele od 2015 roku Android TV. Mando TV steruje obydwoma przez Wi-Fi z iPhone, telefonu z Androidem lub komputera z Windows. Aplikacja zastępuje oryginalnego pilota, gdy zginął albo wyczerpały się baterie.',
    pasos=[
      'Sprawdź, czy Twój telewizor Sony pokazuje ekran główny Google TV lub Android TV. Dotyczy to większości smart TV Sony Bravia od rocznika 2015.',
      'Połącz telefon i telewizor z tą samą siecią Wi-Fi.',
      'Otwórz Mando TV i stuknij na liście swój telewizor Sony.',
      'Wpisz 6-znakowy kod, który telewizor pokazuje na ekranie (tylko za pierwszym razem). Nie potrzebujesz do tego pilota.',
      'Używaj strzałek, OK, Wstecz, Ekranu głównego, głośności i klawiatury.',
    ],
    extra=[
      ('Włączanie telewizora Sony z telefonu', 'Modele Sony z Google TV lub Android TV można obudzić przez sieć, gdy włączony jest „Remote start” (Zdalne uruchamianie). Opcję znajdziesz zwykle w Ustawienia > Sieć i internet > Remote start (ścieżka może się nieco różnić zależnie od modelu). Potem stuknij telewizor w Mando TV, gdy jest wyłączony, a aplikacja go włączy.'),
      ('Gdzie jest przycisk zasilania w Sony', 'W większości telewizorów Bravia jest z tyłu, blisko dolnego lewego lub prawego rogu, albo na bocznej krawędzi. Krótkie naciśnięcie włącza telewizor. Więcej w [Włączanie telewizora bez pilota](@turn-on).'),
      ('Starsze telewizory Sony', 'Telewizory Sony Bravia z lat 2013 do 2015, które nie używają Androida, są obsługiwane w Mando TV w wersji beta. To nowość i może mieć jeszcze niedociągnięcia. Telewizor pokazuje 4-cyfrowy kod PIN, który wpisujesz w aplikacji. Inne telewizory Sony bez Google TV lub Android TV nie są na razie obsługiwane.'),
      ('Za darmo i Pro', 'Pilot możesz pobrać i używać za darmo, bez reklam i bez subskrypcji. Mando TV Pro to opcjonalny jednorazowy zakup z dodatkami.'),
    ],
    marca='android',
    faq=[
      ('Czy Mando TV działa z telewizorami Sony Bravia?', 'Tak, z telewizorami Sony, które używają Google TV lub Android TV. Obejmuje to większość smart TV Sony od rocznika 2015.'),
      ('Czy potrzebuję aplikacji Sony albo konta Google?', 'Nie. Mando TV paruje się kodem z ekranu telewizora i nie wymaga konta.'),
      ('Czy działa ze starszymi telewizorami Sony Bravia bez Androida?', 'Tak, w wersji beta, z modelami Bravia z lat 2013 do 2015 bez Androida. Parowanie odbywa się 4-cyfrowym kodem PIN pokazywanym na telewizorze.'),
      ('Czy mogę pisać w telewizorze Sony z telefonu?', 'Tak. Klawiatura jest darmowa i działa w YouTube, Netflix i w wyszukiwarce telewizora.'),
    ]),
  dict(clave='tcl', corto='Pilot TCL', fecha='2026-11-23',
    titulo='Aplikacja pilot do telewizora TCL na telefon i komputer',
    desc='Zgubiony pilot TCL? Większość telewizorów TCL używa Roku TV lub Google TV. Mando TV steruje obydwoma przez Wi-Fi, bez konta i reklam.',
    h1='Jak sterować telewizorem TCL z telefonu',
    intro='TCL produkuje telewizor, ale oprogramowanie to Roku TV albo Google TV (w starszych modelach Android TV). Mando TV steruje obydwoma systemami i działa jako pilot do Twojego telewizora TCL przez Wi-Fi. Za darmo, bez konta i reklam.',
    pasos=[
      'Sprawdź, jakiego systemu używa Twój TCL. Jeśli ekran główny pokazuje prostą siatkę kafelków z kanałami, to Roku TV. Jeśli wygląda jak Google TV lub Android TV, z rzędami polecanych treści, to Google TV.',
      'Połącz telefon i telewizor TCL z tą samą siecią Wi-Fi.',
      'Otwórz Mando TV. TCL sam pojawi się na liście. Stuknij go.',
      'W TCL z Roku TV nic więcej nie jest potrzebne. W TCL z Google TV wpisz 6-znakowy kod, który telewizor pokazuje na ekranie (tylko za pierwszym razem).',
      'Używaj strzałek, OK, Wstecz, Ekranu głównego, głośności i klawiatury. Włączaj telewizor z aplikacji, jeśli masz włączone włączanie przez sieć (zobacz niżej).',
    ],
    extra=[
      ('Włączanie telewizora TCL z telefonu', 'W TCL z Roku TV włącz „Szybkie uruchamianie TV” w Ustawienia > System > Zasilanie. W TCL z Google TV poszukaj w ustawieniach sieci lub zasilania opcji Wake on LAN, „Włączanie przez sieć” albo zdalnego uruchamiania. Niektóre modele jej nie mają. W takim razie włącz telewizor fizycznym przyciskiem zasilania, zwykle na dole pośrodku albo z tyłu.'),
      ('Jeśli Twój TCL się nie pojawia', 'Sprawdź, czy telefon i telewizor są w tej samej sieci Wi-Fi. Routery z oddzielnymi sieciami 2,4 GHz i 5 GHz mogą ukrywać urządzenia przed sobą. Na iPhone zezwól w ustawieniach na „Sieć lokalna” dla Mando TV. Możesz też dodać telewizor, wpisując jego adres IP. Przeczytaj [Telefon nie widzi telewizora](@not-found).'),
      ('Więcej o Twoim TCL', 'Dla TCL z Roku TV zobacz [Aplikacja pilot do Roku](@roku), a dla TCL z Google TV lub Android TV [Aplikacja pilot do Android TV](@android).'),
      ('Za darmo i Pro', 'Strzałki, OK, Wstecz, Ekran główny, głośność, kanały, cyfry, klawiatura, otwieranie aplikacji, zmiana źródeł oraz włączanie i wyłączanie są darmowe, bez reklam i bez subskrypcji. Touchpad, polecenia głosowe, ulubione aplikacje, rutyny i wyłącznik czasowy należą do Mando TV Pro, jednorazowego zakupu bez subskrypcji.'),
    ],
    marca=None,
    faq=[
      ('Czy Mando TV działa z każdym telewizorem TCL?', 'Działa z telewizorami TCL z Roku TV, Google TV lub Android TV, czyli z większością smart TV TCL. TCL, który nie jest smart TV, nie da się sterować przez Wi-Fi.'),
      ('Czy potrzebuję aplikacji TCL albo konta TCL?', 'Nie. Mando TV łączy się bezpośrednio przez Twoje domowe Wi-Fi i nie wymaga konta.'),
      ('Mój TCL prosi o kod. Gdzie on jest?', 'Modele TCL z Google TV i Android TV pokazują na ekranie 6-znakowy kod. Wpisz go w Mando TV dokładnie tak, jak jest. TCL z Roku TV nie prosi o kod.'),
    ]),
  dict(clave='hisense', corto='Pilot Hisense', fecha='2026-11-23',
    titulo='Aplikacja pilot do Hisense: co działa w telefonie',
    desc='Pilot Hisense z Mando TV: sterowanie VIDAA, Roku TV, Google TV i Fire TV przez Wi-Fi. Uczciwy przegląd tego, co działa.',
    h1='Aplikacja pilot do Hisense: co działa, a co nie',
    intro='Telewizory Hisense nie są w środku wszystkie takie same. Zależnie od modelu używają własnego systemu VIDAA, Roku TV, Google TV lub Fire TV. Mando TV działa jako pilot do Hisense we wszystkich czterech systemach, z jednym wyjątkiem dla niektórych nowszych modeli VIDAA. Oto jak rozpoznać, jaki masz system i czego się spodziewać.',
    pasos=[
      'Sprawdź, jakiego systemu używa Twój Hisense. VIDAA to własny interfejs Hisense. Roku TV pokazuje siatkę kafelków z kanałami. Google TV pokazuje rzędy polecanych treści. Fire TV pokazuje ekran główny Fire TV z rzędami Amazon.',
      'Połącz telefon i telewizor Hisense z tą samą siecią Wi-Fi.',
      'Otwórz Mando TV. Telewizor sam pojawi się na liście. Stuknij go.',
      'Modele VIDAA i Fire TV mogą pokazać kod PIN z czterema cyframi; Google TV pokazuje kod z sześciu znaków. Wpisz go w aplikacji. Roku TV o nic nie pyta. Robisz to tylko raz.',
      'Używaj strzałek, OK, Wstecz, Ekranu głównego, głośności i klawiatury z telefonu.',
    ],
    extra=[
      ('Hisense z Roku TV lub Google TV', 'Działają w pełni jak każdy inny telewizor Roku lub Google TV. Szczegóły na stronach [Aplikacja pilot do Roku](@roku) i [Aplikacja pilot do Android TV](@android).'),
      ('Hisense z Fire TV', 'Obsługa Fire TV to nowość w Mando TV. Zaktualizuj aplikację do najnowszej wersji w swoim sklepie. Jak działa parowanie kodem PIN, opisuje strona [Aplikacja pilot do Fire TV](@firetv). Jeśli coś nie działa tak, jak powinno, napisz do nas przez stronę pomocy i podaj model.'),
      ('Hisense z VIDAA', 'Większość modeli VIDAA działa: przyciski, głośność, klawiatura, aplikacje i źródła. Niektóre nowsze modele VIDAA akceptują tylko oficjalną aplikację Hisense. Mando TV rozpoznaje to przy łączeniu i mówi Ci o tym wprost, zamiast cicho nie działać. W takim przypadku właściwą drogą jest aplikacja Hisense dla Twojego modelu, przyciski na telewizorze albo oryginalny pilot.'),
      ('Włączanie Hisense z telefonu', 'W Hisense z Roku TV włącz „Szybkie uruchamianie TV” w Ustawienia > System > Zasilanie. W Google TV poszukaj opcji Wake on LAN albo „Włączanie przez sieć”. Jeśli jej nie ma, użyj przycisku zasilania na telewizorze.'),
      ('Za darmo i Pro', 'Strzałki, OK, Wstecz, Ekran główny, głośność, kanały, klawisze cyfr, klawiatura, otwieranie aplikacji, zmiana źródeł oraz włączanie i wyłączanie są darmowe, bez reklam i bez subskrypcji. Touchpad, polecenia głosowe, ulubione aplikacje, rutyny i wyłącznik czasowy należą do Mando TV Pro, jednorazowego zakupu bez subskrypcji.'),
    ],
    marca=None,
    faq=[
      ('Czy Mando TV działa z Hisense VIDAA?', 'Tak, z większością modeli VIDAA. Niektóre nowsze akceptują tylko oficjalną aplikację Hisense; Mando TV to rozpoznaje i Ci o tym mówi. Telewizory Hisense z Roku TV, Google TV lub Fire TV też są obsługiwane.'),
      ('Skąd mam wiedzieć, czy mój Hisense to Roku TV, Google TV czy Fire TV?', 'Spójrz na ekran główny. Roku TV ma prostą siatkę kafelków i logo Roku przy uruchamianiu. Google TV ma rzędy polecanych treści. Fire TV ma ekran główny Amazon Fire TV. Nazwa modelu w Ustawienia > Informacje też to wskazuje.'),
      ('Czy potrzebuję konta Hisense albo Google?', 'Nie. Mando TV łączy się bezpośrednio przez Twoje domowe Wi-Fi i nie ma własnego konta.'),
    ]),
  dict(clave='philips', corto='Pilot Philips', fecha='2026-11-23',
    titulo='Aplikacja pilot do Philips: Roku TV, Google TV, Android TV',
    desc='Mando TV steruje telewizorami Philips z Roku TV, Google TV lub Android TV przez Wi-Fi, z telefonu lub komputera. Titan OS nie jest obsługiwany.',
    h1='Sterowanie telewizorem Philips z telefonu',
    intro='Telewizory Philips używają różnych systemów zależnie od kraju i rocznika: Roku TV w USA, Google TV lub Android TV w wielu krajach i Titan OS w niektórych nowszych modelach europejskich. Mando TV steruje modelami z Roku TV, Google TV i Android TV przez Wi-Fi.',
    pasos=[
      'Sprawdź ekran główny. Roku TV pokazuje siatkę kafelków. Google TV i Android TV pokazują rzędy polecanych treści od Google. Titan OS ma własny ekran główny.',
      'Połącz telefon i telewizor z tą samą siecią Wi-Fi.',
      'Otwórz Mando TV i stuknij na liście swój telewizor Philips.',
      'Roku TV o nic nie pyta. Google TV i Android TV pokazują 6-znakowy kod: wpisz go w aplikacji raz.',
      'Używaj strzałek, OK, Wstecz, Ekranu głównego, głośności i klawiatury.',
    ],
    extra=[
      ('Philips z Roku TV', 'Działa jak każdy telewizor Roku. Żeby włączać go z telefonu, włącz „Szybkie uruchamianie TV” w Ustawienia > System > Zasilanie. Więcej na stronie [Aplikacja pilot do Roku](@roku).'),
      ('Philips z Google TV lub Android TV', 'Obejmuje wiele modeli z Ambilight. Parują się kodem z ekranu. Żeby włączać je z telefonu, w ustawieniach sieci lub zasilania poszukaj Wake on LAN albo „Włączanie przez sieć”. W niektórych modelach tej opcji brakuje. Więcej na stronie [Aplikacja pilot do Android TV](@android).'),
      ('Starsze telewizory Philips bez Androida', 'Telewizory Philips z lat 2011 do 2015, które nie używają Androida, są obsługiwane w Mando TV w wersji beta. To nowość i nie wymaga kodu parowania.'),
      ('Philips z Titan OS', 'Titan OS to inny system, którym Mando TV obecnie nie steruje, i wolimy powiedzieć to wprost. Nowsze modele Philips bez Androida też nie są objęte.'),
      ('Za darmo i Pro', 'Pilot możesz pobrać i używać za darmo, bez reklam i bez subskrypcji. Mando TV Pro to opcjonalny jednorazowy zakup z dodatkami.'),
    ],
    marca=None,
    faq=[
      ('Czy Mando TV działa z telewizorami Philips?', 'Z telewizorami Philips, które używają Roku TV, Google TV lub Android TV, tak, a w wersji beta z telewizorami Philips z lat 2011 do 2015 bez Androida. Modele z Titan OS nie są obsługiwane.'),
      ('Czy Mando TV steruje Ambilight?', 'Mando TV to pilot: wysyła przyciski, więc strzałkami i OK dojdziesz do ustawień Ambilight. Nie ma oddzielnych sterowań Ambilight.'),
      ('Czy potrzebuję konta Philips albo Google?', 'Nie. Mando TV łączy się przez Twoje domowe Wi-Fi i nie wymaga konta.'),
    ]),
]
OTRAS_GUIAS += [
  ('no-sub', 'Aplikacja pilot bez subskrypcji i bez reklam'),
  ('roku-app-alt', 'Alternatywa dla aplikacji Roku: jedna do wszystkich telewizorów'),
  ('lg-thinq', 'Alternatywa dla aplikacji LG ThinQ do Twojego telewizora LG'),
  ('smartthings', 'Alternatywa dla SmartThings do telewizorów Samsung'),
  ('googletv-alt', 'Alternatywa dla pilota Google TV w telefonie'),
  ('windows', 'Aplikacja pilot na komputer z Windows'),
  ('iphone', 'Aplikacja pilot na iPhone: jedna do wszystkich telewizorów'),
  ('firetv', 'Pilot do Fire TV na telefon lub komputer'),
  ('firetv-lost', 'Zgubiony pilot Fire TV: jak użyć telefonu'),
  ('turn-on', 'Jak włączyć telewizor bez pilota'),
  ('sony', 'Jak sterować telewizorem Sony z telefonu'),
  ('tcl', 'Jak sterować telewizorem TCL z telefonu'),
  ('hisense', 'Aplikacja pilot do Hisense: co działa, a co nie'),
  ('philips', 'Sterowanie telewizorem Philips z telefonu'),
]
# <<< guías traídas del inglés
