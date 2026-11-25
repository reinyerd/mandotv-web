
SOPORTE = dict(
  titulo='Yardım: TV’yi Mando TV ile bağla ve aç',
  desc='Mando TV kumandasını LG, Samsung, Roku veya Android TV ile nasıl bağlarsın, TV’yi telefondan nasıl açarsın ve sorunları nasıl çözersin.',
  h1='Yardım',
  intro='En sık sorulan sorular, adımların sırasıyla. Seninkini bulamazsan bize <a href="mailto:hola@mandotv.app?subject=Mando%20TV%20yard%C4%B1m">hola@mandotv.app</a> adresinden yaz, yanıtlarız.',
)
SOPORTE_HTML = '''      <h2 id="encontrar">TV’yi bulma</h2>
      <div class="preguntas">
        <details open><summary>TV’m listede görünmüyor</summary>
          <ol>
            <li>Telefonunun ve TV’nin aynı Wi-Fi ağında olduğunu kontrol et. Router’ında farklı adlı bir 2,4 GHz ve bir 5 GHz ağ varsa bazen birbirlerini göremezler.</li>
            <li>TV’nin açık olduğundan emin ol.</li>
            <li>iPhone’da Mando TV’nin “Yerel Ağ” iznine sahip olduğunu kontrol et: Ayarlar, Mando TV.</li>
            <li>TV listesinde, TV’n görünmediğinde kullanabileceğin düğmeye dokun: uygulama en sık nedenleri adım adım kontrol eder (aynı Wi-Fi, VPN, yerel ağ izni ve daha fazlası) ve her düzeltmeden sonra yeniden kontrol etmen için bir düğme gösterir.</li>
            <li>Hâlâ görünmüyorsa + tuşuna dokun, markayı seç ve TV’nin IP adresini gir. Onu TV’nin ağ menüsünde görürsün (örneğin 192.168.1.50).</li>
          </ol>
        </details>
        <details><summary>Mobil veriyle ya da evden uzakta çalışır mı?</summary>
          <p>Hayır. Mando TV, TV’yle ev ağının içinde konuşur; bu yüzden telefonunun bu Wi-Fi’a bağlı olması gerekir.</p>
        </details>
      </div>

      <h2 id="conectar">İlk kez bağlanma</h2>
      <p>Markaya göre tam rehberler: <a href="@@R_lg@@">LG</a>, <a href="@@R_samsung@@">Samsung</a>, <a href="@@R_roku@@">Roku</a> ve <a href="@@R_android@@">Android TV</a>.</p>
      <div class="preguntas">
        <details><summary>LG</summary>
          <p>TV’ye dokunduğunda ekranda izin isteyen bir soru çıkar. Alışık olduğun kumandayla onayla. Bunu yalnızca bir kez yaparsın.</p>
        </details>
        <details><summary>Samsung</summary>
          <p>TV, Mando TV’nin bağlanmasına izin verip vermediğini sorar. Kumandayla “İzin ver”i seç. Yanlışlıkla reddettiysen Ayarlar > Genel > Harici Aygıt Yöneticisi > Aygıt Bağlantı Yöneticisi’ne git ve izinli olarak değiştir.</p>
        </details>
        <details><summary>Roku</summary>
          <p>Roku izin sormaz. Bağlantı kurulmazsa Roku’da Ayarlar > Sistem > Gelişmiş sistem ayarları > Mobil uygulamalarla kontrol’e git ve ağ erişimini Varsayılan veya Etkin olarak bırak.</p>
        </details>
        <details><summary>Android TV ve Google TV</summary>
          <p>TV 6 karakterli bir kod gösterir. Onu Mando TV’ye çıktığı gibi aynen gir. Android TV’li Sony, Philips, TCL, Hisense, Sharp, Xiaomi, Google TV’li Chromecast ve diğerlerinde çalışır.</p>
        </details>
      </div>

      <h2 id="encender">TV’yi uygulamadan açma</h2>
      <p>Mando TV, TV’yi ev ağın üzerinden açar. Bunun için iki şey gerekir: TV açıkken en az bir kez bağlanmış olman ve TV’de ağ üzerinden açmanın etkin olması. Ayarın adı modele göre değişir; en yaygın olanlar şunlar:</p>
      <div class="preguntas">
        <details><summary>LG</summary>
          <p>Ayarlarda (modele göre Genel ya da Bağlantı altında) “Mobil cihazla TV’yi aç”ı ara ve “Wi-Fi üzerinden aç”ı etkinleştir. “Hızlı Başlatma+” varsa onu da etkinleştir.</p>
        </details>
        <details><summary>Samsung</summary>
          <p>Ayarlar > Genel > Ağ > Uzman Ayarları altında “Mobil Cihazla Aç”ı etkinleştir.</p>
        </details>
        <details><summary>Roku</summary>
          <p>Roku TV cihazlarında Ayarlar > Sistem > Güç altında “TV hızlı başlatma”yı etkinleştir. Bir TV’ye takılı Roku oynatıcılar bu şekilde açılamaz.</p>
        </details>
        <details><summary>Android TV ve Google TV</summary>
          <p>Bu üreticiye göre değişir. Ağ ya da güç ayarlarında “Wake on LAN”, “Ağ üzerinden aç” ya da “Ağ beklemesi” seçeneğini ara. Bazı modellerde bu seçenek yoktur.</p>
        </details>
      </div>

      <h2 id="falla">Bir şey yolunda gitmezse</h2>
      <div class="preguntas">
        <details><summary>Bağlantı kopuyor ya da tepki gelmiyor</summary>
          <ol>
            <li>Kumanda ekranında Yeniden bağlan’a dokun.</li>
            <li>Yardımcı olmazsa Mando TV’yi kapat ve uygulamayı yeniden aç.</li>
            <li>TV başka bir IP adresi aldıysa onu listeden kaldır ve yeniden ekle.</li>
          </ol>
        </details>
        <details><summary>Bize hata raporu nasıl gönderirsin</summary>
          <ol>
            <li>Mando TV’de Kişiselleştir düğmesine dokun (üstteki ayar çubukları).</li>
            <li>Test raporunu kopyala’ya dokun.</li>
            <li>Raporu, TV’nin markası ve modeliyle birlikte hola@mandotv.app adresine bir e-postaya yapıştır.</li>
          </ol>
          <p>Rapor şifre, kod ve yazdığın hiçbir şeyi içermez.</p>
        </details>
        <details><summary>Pro’yu satın aldım ama görünmüyor</summary>
          <p>Kişiselleştir altında, satın aldığın mağaza hesabıyla Satın alımı geri yükle’ye dokun. Hâlâ görünmüyorsa bize yaz.</p>
        </details>
      </div>

      <h2 id="guias">Adım adım rehberler</h2>
      <p><a href="@@R_guias@@">Tüm rehberleri gör</a></p>
      <ul>
@@GUIAS@@
      </ul>

      <h2 id="contacto">Hâlâ sorun mu var?</h2>
      <p>Bize <a href="mailto:hola@mandotv.app?subject=Mando%20TV%20yard%C4%B1m">hola@mandotv.app</a> adresinden yaz. TV’nin markasını, modelini ve hangi adımda takıldığını söyle. Bize kendi dilinde yazabilirsin. İspanyolca veya İngilizce yanıtlarız, istersen çevirmen yardımıyla kendi dilinde de.</p>
'''

PRIVACIDAD = dict(
  titulo='Gizlilik Politikası | Mando TV',
  desc='Mando TV kişisel veri toplamaz: hesap, reklam ve izleyici yok. Uygulama yalnızca Wi-Fi ağının içinde TV’nle konuşur.',
  h1='Gizlilik',
  intro='Kısacası: Mando TV verilerini toplamaz. Hesap, reklam, izleyici ve yaptıklarını kaydeden kendi sunucularımız yok.',
)
PRIVACIDAD_HTML = '''      <p class="fecha">14 Kasım 2026’dan beri geçerlidir. Son güncelleme: 25 Kasım 2026.</p>

      <h2>Biz kimiz</h2>
      <p>Mando TV, televizyonunu telefonundan ya da bilgisayarından kontrol etmeni sağlayan bir uygulamadır. Bu politika, uygulamanın hangi bilgileri kullandığını ve bunlarla ne yaptığını anlatır. Sorularında bize <a href="mailto:hola@mandotv.app">hola@mandotv.app</a> adresinden yazabilirsin.</p>

      <h2>Hangi verileri topluyoruz</h2>
      <p>Uygulama: hiçbirini. Uygulama, senin hakkında ya da onu nasıl kullandığın hakkında bize veya üçüncü kişilere hiçbir bilgi göndermez. Analiz, reklam veya izleme aracı kullanmaz.</p>
      <p>Bu web sitesi: Ziyaretleri, <a href="#cookies">Bu sitedeki çerezler</a> bölümünde açıklanan iki şekilde ölçüyoruz.</p>

      <h2>Uygulamanın cihazında sakladıkları</h2>
      <p>Çalışabilmek için uygulama aşağıdakileri yalnızca telefonunda ya da bilgisayarında saklar:</p>
      <ul>
        <li>Eklediğin televizyonlar: ad, marka, ağındaki IP adresi ve açmak için kullanılan ağın donanım adresi (MAC).</li>
        <li>İzni onayladığında her televizyonun verdiği bağlantı anahtarları. Bunlar sistemin güvenli deposunda şifreli olarak saklanır (iPhone ve Mac’te Anahtar Zinciri, Android’de Keystore, Windows’ta korumalı depolama).</li>
        <li>Ayarların: açık ya da koyu tema, arka plan rengi, titreşim ve kumanda türü.</li>
        <li>Pro özelliklerini kullanırsan: favori uygulamaların, rutinlerin ve son YouTube aramaların (bunları uygulamadan silebilirsin).</li>
      </ul>
      <p>Uygulamayı sildiğinde bunların hepsi onunla birlikte silinir.</p>

      <h2>Uygulama kimlerle konuşur</h2>
      <p>Televizyonlarınla, evindeki Wi-Fi ağının içinde. Onları bulmak için uygulama yerel ağını tarar; bu yüzden iPhone’da “Yerel Ağ” izni ister. Uygulamanın klavyesiyle yazdığın metin doğrudan televizyona gider ve kaydedilmez.</p>
      <p>Ayrıca uygulama açılırken bu web sitesinden küçük bir herkese açık dosya indirir (mandotv.app/app/config.json); amaç, kurman gereken yeni bir sürüm olup olmadığını ve hangi özelliklerin Mando TV Pro’ya ait olduğunu öğrenmektir. Bu, bir sayfayı açmak gibi bir indirmedir: uygulama ne verilerini, ne televizyonlarını ne de yaptığın şeyi gönderir. Yalnızca sana uygun bildirimi gösterebilmek için uygulama sürümünü ve sistemi (örneğin Android) belirtir. İnternetin yoksa uygulama en son indirdiği dosyayla çalışmaya devam eder; indirilemeden 30 günden fazla geçerse uygulama senden kısa bir süre internete bağlanmanı ister.</p>

      <p>Televizyona fotoğraf ya da video gönderirsen (bir Pro özelliği), televizyon yalnızca seçtiğin dosyaları doğrudan telefonundan veya bilgisayarından evindeki Wi-Fi üzerinden indirir. Bunlar ne internetten ne de bizden geçer, uygulama diğer fotoğraflarını görmez ve paylaşım, o ekranı kapattığında sona erer.</p>
      <h2>Mikrofon ve ses</h2>
      <p>Sesli arama, mikrofonu yalnızca konuşma düğmesine dokunduğun sürece kullanır. Söylediklerin sistemin konuşma tanıma özelliği tarafından metne çevrilir: iPhone ve Mac’te Apple, Android’de Google tarafından, her biri kendi gizlilik koşullarına göre. Windows’ta konuşma kendi bilgisayarında tanınır ve cihazdan çıkmaz; yalnızca çok eski işlemcilerde uygulama Microsoft’un Windows ses girişini kullanır, onların gizlilik koşullarına göre. Mando TV sesi ne kaydeder ne de saklar ve ortaya çıkan metin, klavyeyle yazdığın gibi doğrudan televizyonuna gider.</p>

      <h2>Ev: Apple Home ve Google Home cihazları</h2>
      <p>Ev bölümünü (test aşamasında) açtığında uygulama, Apple’ın Ev uygulamasında (HomeKit) ya da Google Home’da zaten bulunan cihazları görmek için izin ister. Bu izinle adlarını, odalarını ve durumlarını (açık ya da kapalı, parlaklık, sıcaklık veya bir ev aletinin programının hangi aşamada olduğu) okur; bunları göstermek ve dokunduğunu onlara iletmek için. Her şey telefonun ile Apple ya da Google’ın sistemi arasında gerçekleşir: Mando TV bu listeyi saklamaz, ne bize ne üçüncü kişilere gönderir ve ne reklam ne de analiz için kullanır. Android’de Google Home, kendi Google hesabınla ve Google’ın gizlilik politikasına göre çalışır. İzni istediğin zaman geri alabilirsin: iPhone’da Ayarlar &gt; Gizlilik ve Güvenlik &gt; HomeKit’ten, Android’de Google hesabının ayarlarından.</p>
      <p>“Ev senin için nasıl çalıştı?”ya dokunduğunda e-posta uygulaman, hola@mandotv.app adresine teknik bir özet içeren bir mesajla açılır: uygulamanın sürümü, sistem ve her türden kaç cihazın göründüğü ve yanıt verip vermedikleri. Cihazların, odaların ya da evinin adları yer almaz ve mesaj yalnızca sen kendin gönderirsen gönderilir.</p>

      <h2>Test raporu</h2>
      <p>Uygulamada, hataları gidermemize yardım eden bir “Test raporunu kopyala” düğmesi var. Rapor, uygulama açık olduğu sürece yalnızca uygulamanın belleğinde kalır ve kendiliğinden asla gönderilmez: kopyalayıp paylaşmak sana kalmış. Bağlantı anahtarlarını, eşleştirme kodlarını ve yazdığın hiçbir şeyi içermez; yalnızca uygulamanın attığı adımları içerir, örneğin aramalar, bağlantılar ve hatalar.</p>

      <h2 id="cookies">Bu sitedeki çerezler</h2>
      <p>Bu yalnızca mandotv.app web sitesi için geçerlidir, uygulama için değil.</p>
      <h3>Her zaman çerezsiz</h3>
      <p>Ziyaretleri Cloudflare Web Analytics ile anonim olarak sayıyoruz: sitenin kaç kişi tarafından ziyaret edildiği, hangi sayfaların okunduğu ve hangi ülkeden. Çerez kullanmaz, seni tanımlamak için IP adresini kullanmaz ve diğer web sitelerinde yaptıklarını izlemez.</p>
      <h3>Çerezli, yalnızca kabul edersen</h3>
      <p>Çerez bildiriminde “Kabul et”e dokunursan sitenin nasıl kullanıldığını daha iyi anlamak için (Google LLC’nin) Google Analytics’i etkinleştiririz: sayfa görüntülemeleri, kalış süresi, cihaz türü, yaklaşık şehir ve nereden geldiğin. Bunun için tarayıcında _ga ve _ga_* çerezlerini 2 yıla kadar saklar. Google bu verileri Şili dışındaki sunucularda işleyebilir. Reklam özelliklerini ve Google Signals’ı devre dışı bıraktık ve bu verileri sana reklam göstermek için kullanmıyoruz.</p>
      <p>“Reddet”e dokunursan ya da hiçbir şey seçmezsen Google Analytics yüklenmez ve hiçbir çerez saklanmaz. Kararını her sayfanın en altındaki “Çerezler” düğmesiyle istediğin zaman değiştirebilirsin; onayı geri çekersen bu çerezleri sileriz.</p>
      <p>Seçimin, bir daha sormamamız için tarayıcında saklanır (yerel depolama, kimseye gönderilmez).</p>

      <h2>Satın alımlar</h2>
      <p>Mando TV Pro’yu satın aldığında ödemeyi uygulama mağazası işler (App Store, Google Play veya Microsoft Store). Kart bilgilerini almayız ve saklamayız. Mağaza uygulamaya yalnızca satın alımın var olduğunu bildirir.</p>

      <h2>Bize gönderdiğin e-postalar</h2>
      <p>Bize <a href="mailto:hola@mandotv.app">hola@mandotv.app</a> adresinden yazdığında e-posta adresini ve bize anlattıklarını yalnızca sana yanıt vermek için kullanırız. Onları paylaşmayız ve reklam için kullanmayız. İstediğin zaman mesajlarının silinmesini isteyebilirsin.</p>

      <h2>Çocuklar</h2>
      <p>Uygulama hiç kimseden, çocuklardan da, veri toplamaz.</p>

      <h2>Bu politikadaki değişiklikler</h2>
      <p>Bir gün uygulamanın verilerinle yaptığı şey değişirse, değişiklik uygulamaya ulaşmadan önce bu sayfayı ve yukarıdaki tarihi güncelleriz.</p>
'''
