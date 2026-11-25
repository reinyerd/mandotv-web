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
          <p>Roku nie prosi o zgodę. Jeśli połączenie się nie uda, w Roku wejdź w Ustawienia > System > Zaawansowane ustawienia systemu > Sterowanie przez aplikacje mobilne i zostaw Dostęp do sieci na Domyślny lub Zezwalający.</p>
        </details>
        <details><summary>Android TV i Google TV</summary>
          <p>Telewizor pokaże 6-znakowy kod. Wpisz go w Mando TV dokładnie tak, jak się pojawił. Działa z Sony, Philips, TCL, Hisense, Sharp, Xiaomi, Chromecast z Google TV i innymi z Android TV.</p>
        </details>
      </div>

      <h2 id="encender">Włączanie telewizora z aplikacji</h2>
      <p>Mando TV włącza telewizor przez Twoją sieć domową. Potrzebne są dwie rzeczy: raz połączyłeś się przy włączonym telewizorze, a w telewizorze jest włączone włączanie przez sieć. Nazwa ustawienia zmienia się zależnie od modelu; oto najczęstsze:</p>
      <div class="preguntas">
        <details><summary>LG</summary>
          <p>W ustawieniach (zależnie od modelu w Ogólne lub w Połączenie) poszukaj „Włącz TV przez urządzenie mobilne” i włącz „Włącz przez Wi-Fi”. Jeśli jest „Quick Start+”, włącz też tę opcję.</p>
        </details>
        <details><summary>Samsung</summary>
          <p>Włącz „Włączanie przez urządzenie mobilne” w Ustawienia > Ogólne > Sieć > Ustawienia ekspertów.</p>
        </details>
        <details><summary>Roku</summary>
          <p>W telewizorach Roku TV włącz „Szybkie uruchamianie TV” w Ustawienia > System > Zasilanie. Odtwarzaczy Roku podłączonych do telewizora nie da się w ten sposób włączyć.</p>
        </details>
        <details><summary>Android TV i Google TV</summary>
          <p>To zależy od producenta. W ustawieniach sieci lub zasilania poszukaj „Wake on LAN”, „Włączanie przez sieć” albo „Network standby”. Niektóre modele nie mają tej opcji.</p>
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

