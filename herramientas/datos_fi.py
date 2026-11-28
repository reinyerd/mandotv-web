# Suomenkieliset tekstit (sinuttelu) mandotv.app-sivustolle. Niitä käyttää generar_idiomas.py. Kirjoitettu Suomen hakuja varten.
# Sivujen avaimet (lg, lost-tv, ...) ja niiden polut ovat tiedostossa idiomas_sitio.py.
# Kunkin merkin valikkojen nimet (LG, Samsung, Roku, Android TV, iPhone) ovat samat kuin sovelluksessa suomeksi
# (lib/l10n/app_fi.arb sovelluksen projektissa).

UI = dict(
  locale='fi_FI',
  aria_home='Mando TV, etusivu', aria_main='Päävalikko', nav_que='Ominaisuudet', nav_ayuda='Ohje', nav_contacto='Yhteystiedot',
  asunto='Hei%20Mando%20TV', inicio='Etusivu', privacidad='Tietosuoja', aria_pie='Sivun alaosa', aria_ruta='Polku',
  aria_marcas='Merkit ja oppaat', hecho='Tehty Chilessä',
  aviso='Mando TV on riippumaton sovellus. Se ei ole yhteydessä mainittuihin TV-valmistajiin eikä Googleen, Amazoniin, Appleen tai Rokuun, eivätkä ne tue sitä. Tavaramerkit kuuluvat omistajilleen, ja ne mainitaan vain yhteensopivuuden kertomiseksi. Android TV ja Google TV ovat Google LLC:n tavaramerkkejä. Apple TV on Apple Inc:n tavaramerkki.',
  bajar='Lataa ilmaiseksi', descarga='Lataa kohteesta', anticipada='Ennakkokäyttö:',
  apple_aria='Lataa Mando TV ilmaiseksi App Storesta', ms_aria='Lataa Mando TV ilmaiseksi Microsoft Storesta',
  gp_aria='Mando TV:n ennakkokäyttö Google Playssa Androidille', aria_desc='Lataa Mando TV',
  b_como_btn='Näin yhdistät', b_tiendas_label='Saatavilla sovelluskaupoista',
  b_nota='iPhone, iPad, Mac, Android ja Windows. Ilmainen lataus, ei mainoksia. Pro on kertamaksu, ei tilausta.',
  b_compat='Yhteensopivat televisiot', b_otras='Muut merkit', b_otras_p='Mando TV ohjaa kaikkia näitä merkkejä samalla sovelluksella:',
  g_guias='Oppaat', g_ver='Katso vaiheet', g_pasos='Vaihe vaiheelta', g_hazlo='Näin teet sen Mando TV:llä',
  g_tiendas='Mando TV on yleiskaukosäädin televisiollesi. Lataa se ilmaiseksi, ilman mainoksia ja ilman tiliä. Pro on valinnainen kertaosto, ei tilausta. iPhonelle, iPadille, Windowsille ja Androidille:',
  g_nota='Android: ilmainen ennakkokäyttö Google Playssa. <a href="{enlace}">Liity mukaan kahdella vaiheella</a> ja auta meitä pääsemään kauppaan.',
  g_mas_pagina='Lisätietoja löydät sivulta {enlace}.', g_mas_marca='Lisätietoja merkin mukaan:',
  g_faq='Usein kysyttyä', g_mas='Lisää oppaita', g_todas='Kaikki oppaat', g_ayuda='Ohje ja tuki',
  g_idiomas='Tämä opas muilla kielillä',
)

# Pie de página y listas de marcas/guías: (clave, texto)
PIE = [
  ('samsung', 'Samsung-kaukosäädin'),
  ('lg', 'LG-kaukosäädin'),
  ('roku', 'Roku-kaukosäädin'),
  ('android', 'Android TV -kaukosäädin'),
  ('guias', 'Kaikki oppaat'),
  ('lost-tv', 'Kaukosäädin hukassa'),
  ('lost-lg', 'LG-kaukosäädin hukassa'),
  ('lg-on', 'LG-televisio päälle puhelimella'),
  ('hdmi', 'HDMI-tulon vaihto ilman kaukosäädintä'),
  ('androidtv', 'Android TV ilman kaukosäädintä'),
  ('console', 'Televisio ja konsolin HDMI ilman kaukosäädintä'),
  ('samsung-lost', 'Samsung-televisio ilman kaukosäädintä'),
  ('roku-lost', 'Roku-kaukosäädin hukassa'),
  ('roku-403', 'Roku-sovellus ei toimi'),
  ('androidtv-code', 'Android TV:n pariliitoskoodi'),
  ('not-found', 'Puhelin ei löydä televisiota'),
  ('wifi', 'Puhelin kaukosäätimenä wifin kautta'),
  ('pc', 'Television ohjaus tietokoneella'),
]
NOMBRE_OTRA = {'lg': 'LG-kaukosäädinsovellus', 'samsung': 'Samsung-kaukosäädinsovellus', 'roku': 'Roku-kaukosäädinsovellus',
               'android': 'Android TV- ja Google TV -kaukosäädinsovellus'}
PAGINA_MARCA = {'lg': 'LG-kaukosäädinsovellus', 'samsung': 'Samsung-kaukosäädinsovellus', 'roku': 'Roku-kaukosäädinsovellus',
                'android': 'Android TV -kaukosäädinsovellus'}

OTRAS_GUIAS = [
  ('lg-on', 'LG-televisio päälle puhelimella'),
  ('lost-tv', 'Kaukosäädin hukassa: näin toimit'),
  ('lost-lg', 'LG-kaukosäädin hukassa: näin käytät puhelintasi'),
  ('hdmi', 'HDMI-tulon vaihto televisiossa ilman kaukosäädintä'),
  ('androidtv', 'Android TV ilman kaukosäädintä: näin käytät puhelintasi'),
  ('console', 'Television käynnistys ja konsolin HDMI-tuloon vaihto ilman kaukosäädintä'),
  ('samsung-lost', 'Samsung-televisio ilman alkuperäistä kaukosäädintä: näin käytät puhelintasi'),
  ('roku-lost', 'Roku-kaukosäädin hukassa: näin käytät puhelintasi'),
  ('roku-403', 'Roku-sovellus ei toimi: korjaa virhe 403'),
  ('androidtv-code', 'Android TV pyytää pariliitoskoodia: näin toimit'),
  ('not-found', 'Puhelimesi ei löydä televisiota: tarkista nämä'),
  ('wifi', 'Näin käytät puhelintasi kaukosäätimenä wifin kautta'),
  ('pc', 'Näin ohjaat televisiota Windows-tietokoneella'),
]

INDICE = dict(
  titulo='Oppaat: ohjaa televisiota puhelimella | Mando TV',
  desc='Opas vaihe vaiheelta: käytä puhelinta tai tietokonetta kaukosäätimenä, käynnistä televisio, vaihda HDMI ja ratkaise Samsung-, LG- ja Roku-ongelmat.',
  h1='Oppaat: puhelin kaukosäätimenä',
  intro='Helpot vaiheet, joilla yhdistät Samsung-, LG-, Roku- tai Android TV -television kaukosäätimen Mando TV:hen, käynnistät television ja ratkaiset ongelmat.',
  h2_guias='Kaikki oppaat', h2_marcas='Kaukosäädinsovellus merkin mukaan',
  marcas_extra=[('sony', 'Sony-kaukosäädinsovellus'), ('philips', 'Philips-kaukosäädinsovellus')],
)

MARCAS = [
  dict(clave='lg', color='#e0457b', corto='LG',
    titulo='LG TV -kaukosäädinsovellus puhelimeen, ilmainen | Mando TV',
    desc='Puhelimesi tai tietokoneesi LG TV -kaukosäätimenä webOS:lle wifin kautta. Painikkeet, näppäimistö, sovellukset, tulot ja käynnistys ilmaiseksi; osoitin Prolla.',
    h1='LG TV -kaukosäädin sovelluksena puhelimeen',
    intro='Mando TV on LG-televisioiden kaukosäädinsovellus: se muuttaa puhelimesi tai tietokoneesi kotisi wifin kautta webOS-pohjaisen LG-älytelevisiosi kaukosäätimeksi. Siitä on apua, kun kaukosäädin on hukassa, paristot ovat tyhjät tai haluat vain kirjoittaa nopeammin.',
    compat='LG-älytelevisiot, joissa on webOS (suurin osa LG-älytelevisioista vuodesta 2014 alkaen). Toimii LED-, NanoCell-, QNED- ja OLED-televisioiden kanssa. Vanhempia NetCast-pohjaisia LG-älytelevisioita (2011-2014, ennen webOS:ää) tuetaan nyt betassa: ne yhdistetään television näyttämällä 6-numeroisella avaimella.',
    h2=dict(funciones='Näin voit käyttää LG-televisiotasi', como='Näin yhdistät LG-televisiosi Mando TV:hen',
            encender='LG-television käynnistys puhelimella', preguntas='LG-kysymyksiä', guias='LG-oppaat'),
    funciones=[
      ('Kaikki painikkeet', 'Suuntapainikkeet, OK, Takaisin, Koti, äänenvoimakkuus, kanavat, mykistys ja toisto.'),
      ('Osoitin kuten Magic Remotessa (Pro)', 'Liikuta nuolta sormella näytöllä, aivan kuten LG Magic Remotella.'),
      ('Kaksi näppäimistöä', 'Kirjoita television hakuun ja useimmissa sovelluksissa puhelimesi näppäimistöllä. YouTube-näppäimistöllä (Pro) kirjoitat tai sanot, mitä haluat katsoa, ja YouTube avautuu televisiossa tuloksineen.'),
      ('Sovellukset ja tulot', 'Avaa sovelluksesi ja vaihda HDMI-, live-TV-, AirPlay- tai Screen Share -tuloon.'),
      ('Äänen ulostulo (Pro)', 'Vaihda television kaiuttimien ja soundbarin välillä.'),
      ('Television käynnistys', 'Jos televisio on sammutettu, Mando TV käynnistää sen verkon kautta ja yhdistää itse.'),
    ],
    pasos=[
      'Yhdistä puhelin ja televisio samaan wifiin.',
      'Avaa Mando TV: LG-televisiosi tulee listaan itsestään. Napauta sitä.',
      'Televisioon tulee kysymys, jossa pyydetään lupaa. Vahvista se tavallisella kaukosäätimellä (vain ensimmäisellä kerralla).',
    ],
    encender='Ota käyttöön ”Käynnistä TV mobiililaitteella” (joissakin malleissa sen nimi on ”Käynnistä wifin kautta”). Löydät sen kohdasta Asetukset > Yleiset > Laitteet > Ulkoiset laitteet (vanhemmissa malleissa Yhteys > Mobiiliyhteyden hallinta). Sen jälkeen, kun napautat sammutettua televisiota Mando TV:ssä, sovellus kysyy, haluatko käynnistää sen, ja yhdistää itse.',
    faq=[
      ('Tarvitsenko Magic Remoten Mando TV:n käyttöön?', 'Vain ensimmäisellä kerralla, jotta voit vahvistaa kysymyksen näytöllä. Sen jälkeen puhelimesi riittää.'),
      ('Korvaako Mando TV LG ThinQ -sovelluksen?', 'Television ohjaamiseen kyllä: et tarvitse LG-tiliä etkä tarvitse rekisteröidä televisiota. Mando TV yhdistää suoraan wifisi kautta.'),
      ('Voinko käynnistää LG-televisioni puhelimella?', 'Kyllä, kun olet ottanut televisiossa käyttöön ”Käynnistä TV mobiililaitteella” ja yhdistänyt kerran television ollessa päällä.'),
      ('Toimiiko se vanhempien, ennen webOS:ää tehtyjen LG-televisioiden kanssa?', 'Betassa kyllä, vuosien 2011-2014 LG NetCast -älytelevisioilla. Ne yhdistetään television näyttämällä 6-numeroisella avaimella. Ominaisuus on uusi, ja siinä voi vielä olla rosoisia kohtia.'),
    ],
    guias=[('lg-on', 'Näin käynnistät LG-television puhelimella'),
           ('lost-lg', 'LG-kaukosäädin hukassa: näin käytät puhelintasi'),
           ('hdmi', 'HDMI-tulon vaihto televisiossa ilman kaukosäädintä'),
           ('guias', 'Kaikki oppaat television ohjaamiseen puhelimella')]),
  dict(clave='samsung', color='#3d7bff', corto='Samsung',
    titulo='Samsung TV -kaukosäädinsovellus puhelimeen | Mando TV',
    desc='Puhelimesi tai tietokoneesi Samsung TV -kaukosäätimenä Tizenille wifillä. Painikkeet, näppäimistö, sovellukset ilmaiseksi; kosketuslevy Prolla.',
    h1='Samsung TV -kaukosäädin sovelluksena puhelimeen',
    intro='Mando TV on Samsung-televisioiden kaukosäädinsovellus: se muuttaa puhelimesi tai tietokoneesi kotisi wifin kautta Samsung-älytelevisiosi kaukosäätimeksi. Et tarvitse Samsung-tiliä etkä tarvitse rekisteröidä televisiota.',
    compat='Samsung-älytelevisiot, joissa on Tizen, valmistusvuosi 2016 tai uudempi (sarjat kuten Crystal UHD, QLED, Neo QLED, The Frame ja OLED).',
    h2=dict(funciones='Näin voit käyttää Samsung-televisiotasi', como='Näin yhdistät Samsung-televisiosi Mando TV:hen',
            encender='Samsung-television käynnistys puhelimella', preguntas='Samsung-kysymyksiä', guias='Samsung-oppaat'),
    funciones=[
      ('Kaikki painikkeet', 'Suuntapainikkeet, OK, Takaisin, Koti, äänenvoimakkuus, kanavat, mykistys ja lähde.'),
      ('Kosketuslevy (Pro)', 'Pyyhkäise sormella valikoissa ilman, että etsit nuolipainikkeita.'),
      ('Kaksi näppäimistöä', 'Kirjoita television hakuun ja useimmissa sovelluksissa puhelimesi näppäimistöllä. YouTube-näppäimistöllä (Pro) kirjoitat tai sanot, mitä haluat katsoa, ja YouTube avautuu televisiossa tuloksineen.'),
      ('Sovellukset', 'Avaa Netflix, YouTube, Prime Video ja muut sovelluksesi yhdellä napautuksella.'),
      ('Television käynnistys', 'Jos televisio on sammutettu, Mando TV käynnistää sen verkon kautta ja yhdistää itse.'),
      ('Ilman tiliä', 'Yhteys kulkee suoraan wifisi kautta, ilman kiertoa internetin kautta.'),
    ],
    pasos=[
      'Yhdistä puhelin ja televisio samaan wifiin.',
      'Avaa Mando TV: Samsung-televisiosi tulee listaan itsestään. Napauta sitä.',
      'Televisio kysyy, sallitko yhteyden. Valitse kaukosäätimellä ”Salli” (vain ensimmäisellä kerralla).',
    ],
    encender='Ota Samsung-televisiossa käyttöön ”Käynnistä mobiililaitteella” kohdasta Asetukset > Yleiset > Verkko > Asiantuntija-asetukset. Sen jälkeen, kun napautat sammutettua televisiota Mando TV:ssä, sovellus kysyy, haluatko käynnistää sen, ja yhdistää itse.',
    faq=[
      ('Kieltäydyin luvasta vahingossa. Mitä teen?', 'Mene televisiossa kohtaan Asetukset > Yleiset > Ulkoisten laitteiden hallinta > Laiteyhteyksien hallinta ja aseta Mando TV sallituksi.'),
      ('Korvaako Mando TV SmartThingsin?', 'Television ohjaamiseen kyllä, ja ilman Samsung-tiliä. Mando TV yhdistää suoraan wifisi kautta.'),
      ('Toimiiko se vanhempien Samsung-televisioiden kanssa?', 'Se toimii Samsung-televisioilla, joissa on Tizen ja valmistusvuosi 2016 tai uudempi. Aiemmat mallit käyttävät toista järjestelmää, jota emme vielä tue.'),
    ],
    guias=[('samsung-lost', 'Samsung-televisio ilman alkuperäistä kaukosäädintä: näin käytät puhelintasi'),
           ('smartthings', 'SmartThingsin vaihtoehto Samsung-televisioille'),
           ('turn-on', 'Näin käynnistät television ilman kaukosäädintä'),
           ('hdmi', 'HDMI-tulon vaihto televisiossa ilman kaukosäädintä'),
           ('guias', 'Kaikki oppaat television ohjaamiseen puhelimella')]),
  dict(clave='roku', color='#a77bff', corto='Roku',
    titulo='Roku-kaukosäädinsovellus puhelimeen, ilmainen | Mando TV',
    desc='Puhelimesi tai tietokoneesi Roku-kaukosäätimenä Roku TV:lle ja Roku-soittimelle wifin kautta. Painikkeet, näppäimistö, kanavat, tulot ja käynnistys ilmaiseksi.',
    h1='Roku-kaukosäädin sovelluksena puhelimeen',
    intro='Mando TV on Rokun kaukosäädinsovellus: se muuttaa puhelimesi tai tietokoneesi kotisi wifin kautta Rokusi kaukosäätimeksi. Se toimii Roku TV -laitteiden ja HDMI-liitäntään kytkettävien Roku-soittimien kanssa.',
    compat='Roku TV -laitteet (TCL, Hisense, Philips, Sharp, JVC ja muut) ja Roku-soittimet (Express, Streaming Stick, Ultra).',
    h2=dict(funciones='Näin voit käyttää Rokua', como='Näin yhdistät Rokusi Mando TV:hen',
            encender='Rokun käynnistys puhelimella', preguntas='Roku-kysymyksiä', guias='Roku-oppaat'),
    funciones=[
      ('Kaikki painikkeet', 'Suuntapainikkeet, OK, Takaisin, Koti, äänenvoimakkuus, mykistys, toisto uudelleen ja toisto.'),
      ('Kaksi näppäimistöä', 'Kirjoita Rokun hakuun ja kanavissa, jotka sen sallivat, puhelimesi näppäimistöllä. YouTube-näppäimistöllä (Pro) kirjoitat tai sanot, mitä haluat katsoa, ja YouTube avautuu televisiossa tuloksineen.'),
      ('Kanavat', 'Avaa Netflix, YouTube ja muut Roku-kanavasi yhdellä napautuksella.'),
      ('Tulot', 'Vaihda Roku TV:ssä sovelluksesta HDMI-, antenni- tai AV-tuloon.'),
      ('Television käynnistys', 'Pikakäynnistyksellä varustetuissa Roku TV -laitteissa Mando TV käynnistää television puhelimestasi.'),
      ('Ilman pariliitosta', 'Roku ei kysy koodia: napauta sitä listassa, niin olet yhdistetty.'),
      ('Kaukosäätimen soittaminen', 'Jos Roku-kaukosäätimessäsi on kaiutin, kuten Roku Voice Remote Prossa, Mando TV saa sen piippaamaan, jotta löydät sen. Ilmainen, Rokun on oltava päällä.'),
    ],
    pasos=[
      'Yhdistä puhelin ja Roku samaan wifiin.',
      'Avaa Mando TV: Rokusi tulee listaan itsestään. Napauta sitä.',
      'Jos yhteys ei muodostu, mene Rokussa kohtaan Asetukset > Järjestelmä > Järjestelmän lisäasetukset > Ohjaus mobiilisovelluksilla ja aseta verkon käyttö tilaan Oletus tai Permissive (uudemmassa Roku-ohjelmistossa aseta Ohjaus mobiilisovelluksilla tilaan Käytössä).',
    ],
    encender='Ota Roku TV -laitteissa käyttöön ”TV:n pikakäynnistys” kohdasta Asetukset > Järjestelmä > Virta. Toiseen televisioon kytkettyjä Roku-soittimia ei voi käynnistää näin. Sen jälkeen, kun napautat sammutettua televisiota Mando TV:ssä, sovellus kysyy, haluatko käynnistää sen, ja yhdistää itse.',
    faq=[
      ('Toimiiko se Roku Expressin tai Streaming Stickin kanssa?', 'Kyllä. Kaikkia Roku-soittimia ja Roku TV -laitteita ohjataan samalla tavalla.'),
      ('Mando TV ei löydä Rokuani. Mitä teen?', 'Tarkista, että molemmat ovat samassa wifissä ja että ”Ohjaus mobiilisovelluksilla” ei ole poissa käytöstä Rokussa. Voit lisätä sen myös IP-osoitteen avulla.'),
      ('Tarvitsenko Roku-tilin?', 'Et. Mando TV yhdistää suoraan wifisi kautta.'),
    ],
    guias=[('roku-403', 'Roku-sovellus ei toimi (virhe 403)'),
           ('roku-lost', 'Roku-kaukosäädin hukassa: näin käytät puhelintasi'),
           ('tcl', 'TCL-kaukosäädinsovellus'),
           ('hisense', 'Hisense-kaukosäädinsovellus'),
           ('philips', 'Philips-kaukosäädinsovellus'),
           ('guias', 'Kaikki oppaat television ohjaamiseen puhelimella')]),
  dict(clave='android', color='#2fbf8f', corto='Android TV ja Google TV',
    titulo='Google TV- ja Android TV -kaukosäädin | Mando TV',
    desc='Puhelin tai tietokone Google TV- ja Android TV -kaukosäätimenä (Sony, TCL, Xiaomi). Painikkeet, näppäimistö ja käynnistys ilmaiseksi; kosketuslevy Prolla.',
    h1='Google TV- ja Android TV -kaukosäädin sovelluksena puhelimeen',
    intro='Mando TV on Android TV:n kaukosäädinsovellus: se muuttaa puhelimesi tai tietokoneesi kotisi wifin kautta Android TV- tai Google TV -televisiosi kaukosäätimeksi. Se toimii myös iPhonella ja Windowsilla.',
    compat='Televisiot, joissa on Google TV tai Android TV, merkeiltä Sony, Philips, TCL, Hisense, Sharp, Xiaomi, Toshiba, Panasonic, Haier, Skyworth, JVC, Thomson, Motorola, OnePlus, iFFALCON, Kogan, Vu ja muut, sekä Chromecast with Google TV, Google TV Streamer, onn. ja Nvidia Shield. Osa näistä merkeistä myy myös malleja, joissa on toinen järjestelmä: jos televisiosi näyttää Google TV:n aloitusnäytön tai siinä on Google Play Kauppa, Mando TV ohjaa sitä.',
    h2=dict(funciones='Näin voit käyttää Android TV:tä ja Google TV:tä', como='Näin yhdistät Android TV:n ja Google TV:n Mando TV:hen',
            encender='Android TV:n ja Google TV:n käynnistys puhelimella', preguntas='Android TV- ja Google TV -kysymyksiä', guias='Android TV- ja Google TV -oppaat'),
    funciones=[
      ('Kaikki painikkeet', 'Suuntapainikkeet, OK, Takaisin, Koti, äänenvoimakkuus, mykistys ja toisto.'),
      ('Kosketuslevy (Pro)', 'Pyyhkäise sormella liikkuaksesi nopeasti Google TV:n valikoissa.'),
      ('Kaksi näppäimistöä', 'Kirjoita television hakuun ja useimmissa sovelluksissa puhelimesi näppäimistöllä. YouTube-näppäimistöllä (Pro) kirjoitat tai sanot, mitä haluat katsoa, ja YouTube avautuu televisiossa tuloksineen.'),
      ('Sovellukset', 'Avaa YouTube, Netflix, Disney+ ja muut sovelluksesi yhdellä napautuksella.'),
      ('Television käynnistys', 'Malleissa, joissa on käynnistys verkon kautta, Mando TV käynnistää television ja yhdistää itse.'),
      ('iPhone, Android ja tietokone', 'Se toimii samalla tavalla jokaisella puhelimella ja tietokoneella.'),
    ],
    pasos=[
      'Yhdistä puhelin ja televisio samaan wifiin.',
      'Avaa Mando TV: Android TV:si tulee listaan itsestään. Napauta sitä.',
      'Televisio näyttää 6-merkkisen koodin. Kirjoita se Mando TV:hen (vain ensimmäisellä kerralla).',
    ],
    encender='Se riippuu valmistajasta. Etsi verkko- tai virta-asetuksista kohtaa ”Wake on LAN”, ”Käynnistys verkon kautta”, ”Verkon valmiustila” tai ”Remote start”. Joissakin malleissa tätä asetusta ei ole. Sen jälkeen, kun napautat sammutettua televisiota Mando TV:ssä, sovellus kysyy, haluatko käynnistää sen, ja yhdistää itse.',
    faq=[
      ('Toimiiko se Chromecast with Google TV:n kanssa?', 'Kyllä, pariliitos tehdään näytölle tulevalla 6-merkkisellä koodilla.'),
      ('Miten se eroaa Google TV -sovelluksesta?', 'Mando TV ei tarvitse Google-tiliä, toimii myös Windowsilla ja ohjaa LG-, Samsung- ja Roku-televisioita samalla sovelluksella.'),
      ('Koodi ei tule näytölle. Mitä teen?', 'Sulje Mando TV, avaa sovellus uudelleen ja napauta televisiota vielä kerran. Tarkista, ettei televisio ole syvässä virransäästötilassa.'),
    ],
    guias=[('androidtv-code', 'Android TV pyytää pariliitoskoodia: näin toimit'),
           ('androidtv', 'Android TV ilman kaukosäädintä: näin käytät puhelintasi'),
           ('googletv-alt', 'Google TV -kaukosäätimen vaihtoehto puhelimelle'),
           ('sony', 'Sony-kaukosäädinsovellus'),
           ('tcl', 'TCL-kaukosäädinsovellus'),
           ('hisense', 'Hisense-kaukosäädinsovellus'),
           ('philips', 'Philips-kaukosäädinsovellus'),
           ('guias', 'Kaikki oppaat television ohjaamiseen puhelimella')]),
]

GUIAS = [
  dict(clave='lost-tv', corto='Kaukosäädin hukassa',
    titulo='Kaukosäädin hukassa? Ohjaa televisiota puhelimella',
    desc='Kaukosäädin hukassa? Käynnistä TV laitteen painikkeella ja käytä puhelinta kaukosäätimenä. Ohjeet LG:lle, Samsungille, Rokulle ja Android TV:lle.',
    h1='Kaukosäädin hukassa? Tässä mitä voit tehdä nyt',
    intro='Kaukosäädin katoaa jokaisessa kodissa: se on poissa juuri silloin, kun haluat katsoa jotain. Hyvä uutinen: puhelimesi voi korvata kaukosäätimen kotisi wifin kautta. Tässä järjestyksessä, mitä voit tehdä.',
    pasos=[
      'Käynnistä televisio laitteessa olevalla painikkeella. Se on lähes aina alareunan keskellä tai takana lähellä nurkkaa. Joskus se on yksittäinen painike, joskus pieni ohjaussauva.',
      'Yhdistä puhelimesi samaan wifiin kuin televisio.',
      'Lataa Mando TV, joka on ilmainen eikä vaadi tiliä, ja avaa sovellus. Televisiosi tulee listaan itsestään. Napauta sitä.',
      'Vahvista yhteys merkillesi. LG:ssä ja Samsungissa televisio näyttää kysymyksen: vahvista se television omalla painikkeella tai ohjaussauvalla. Android TV:ssä ja Google TV:ssä kirjoitat näytölle tulevan 6-merkkisen koodin. Roku ei kysy mitään.',
      'Valmis. Nuolet, OK, Takaisin, Koti, äänenvoimakkuus, kanavat ja näppäimistö ovat ilmaisia.',
      'Seuraavaa kertaa varten: ota television asetuksissa käyttöön käynnistys verkon kautta (merkkisi opas on alla). Silloin voit käynnistää television puhelimella koskematta siihen.',
    ],
    extra=[
      ('Valitse oma merkkisi opas', 'LG: [LG-kaukosäädin hukassa](@lost-lg). Android TV ja Google TV: [Android TV ilman kaukosäädintä](@androidtv). Samsung: [Samsung-televisio ilman kaukosäädintä](@samsung-lost). Roku: [Roku-kaukosäädin hukassa](@roku-lost).'),
      ('Jos televisio ei käynnisty painikkeella', 'Ennen kuin etsit toista kaukosäädintä, tarkista, että johto on tiukasti kiinni ja pistorasiassa on virtaa. Jos television painike ei tee mitään, vika on televisiossa eikä kaukosäätimessä.'),
      ('Jos kaukosäädin ei vain enää toimi', 'Kokeile uusia paristoja. Voit tarkistaa, lähettääkö se vielä signaalia, suuntaamalla sen puhelimen kameraan ja painamalla näppäintä: monessa puhelimessa näytöllä näkyy violetti valo. Jos näet valon mutta televisio ei reagoi, television anturi voi olla peitossa.'),
      ('Jos olet vaihtanut reitittimen ja televisiolta puuttuu wifi', 'Ilman kaukosäädintä on vaikeampaa yhdistää televisio uuteen verkkoon. Helpoin tapa on kytkeä televisio reitittimeen verkkokaapelilla. Voit myös luoda wifin, jolla on sama nimi ja salasana kuin ennen: televisio yhdistää siihen yleensä itse.'),
      ('Mikä on ilmaista ja mikä Proa', 'Television käynnistys ja sammutus, nuolet, OK, äänenvoimakkuus, kanavat, numeronäppäimet, näppäimistö, sovellusten avaaminen ja tulon vaihto ovat ilmaisia. Kosketuslevy, ääni ja rutiinit kuuluvat Mando TV Pro -versioon, joka on kertaosto ilman tilausta.'),
    ],
    marca=None,
    faq=[
      ('Voinko käynnistää television puhelimella, jos en ole koskaan yhdistänyt sitä?', 'Ensimmäisellä kerralla käynnistät sen television painikkeella. Kun olet yhdistänyt puhelimesi ja ottanut television asetuksissa käyttöön käynnistyksen verkon kautta, voit käynnistää sen sovelluksella.'),
      ('Pitääkö minun ostaa uusi kaukosäädin?', 'Ei välttämättä. Mando TV:ssä painikkeet, äänenvoimakkuus, näppäimistö ja käynnistys ovat ilmaisia. Jos haluat silti oikean kaukosäätimen, etsi television tarkka malli.'),
      ('Toimiiko se, jos televisiolla ei ole wifiä?', 'Yleensä ei. Puhelimen ja television on yleensä oltava samassa wifissä. Poikkeuksia ovat infrapuna Android-puhelimilla, joissa on infrapunalähetin (sillä voi ohjata myös televisioita, jotka eivät ole älytelevisioita), sekä Bluetooth betassa Android 9:stä alkaen (toimii kokonaan ilman wifiä Google TV:n, Android TV:n ja Fire TV:n kanssa).'),
    ]),
  dict(clave='lost-lg', corto='LG-kaukosäädin hukassa',
    titulo='LG-kaukosäädin hukassa? Käytä puhelinta',
    desc='Ei LG-kaukosäädintä? Käynnistä televisio laitteen painikkeella, vahvista kysymys ja käytä puhelinta wifin kautta. Ei LG-tiliä, ei mainoksia.',
    h1='LG-kaukosäädin hukassa? Näin käytät puhelintasi',
    intro='Jos LG-kaukosäätimesi on hukassa tai Magic Remote ei enää toimi, puhelimesi korvaa sen wifin kautta. Se toimii webOS-pohjaisilla LG-televisioilla eli lähes kaikilla LG-älytelevisioilla vuodesta 2014. Et tarvitse LG-tiliä etkä ThinQ-sovellusta.',
    pasos=[
      'Käynnistä televisio alhaalla LG-logon alla olevalla painikkeella tai takana olevalla painikkeella. Monessa mallissa se on ohjaussauva: paina sitä avataksesi valikon ja liikuta sitä valitaksesi.',
      'Yhdistä puhelimesi samaan wifiin kuin televisio.',
      'Avaa Mando TV ja napauta listassa LG-televisiotasi.',
      'Televisio näyttää kysymyksen, jossa pyydetään lupaa. Vahvista se ohjaussauvalla tai television painikkeella. Jos olet jo aiemmin yhdistänyt tämän puhelimen, se ei kysy uudelleen.',
      'Valmis. Nuolet, OK, Takaisin, Koti, äänenvoimakkuus, kanavat ja näppäimistö ovat ilmaisia. Osoitin on Pro-ominaisuus.',
      'Kun sovellus on yhdistetty, avaa asetukset nuolilla ja OK:lla ja ota käyttöön ”Käynnistä TV mobiililaitteella”. Opas [LG-televisio päälle puhelimella](@lg-on) näyttää, mistä asetuksen löydät.',
    ],
    extra=[
      ('Jos televisio ei näytä kysymystä', 'Lupa voi jo olla tallennettuna tai puhelimesi on toisessa verkossa. Tarkista, että molemmat ovat samassa wifissä ja VPN on pois päältä. Jos televisio ei tule listaan, [Puhelimesi ei löydä televisiota](@not-found) auttaa eteenpäin.'),
      ('Jos televisio on menettänyt wifinsä', 'Kytke televisio reitittimeen verkkokaapelilla, niin se käyttää sitä itse. Tai luo wifi, jolla on sama nimi ja salasana kuin ennen, sillä televisio yhdistää siihen yleensä itse.'),
      ('Jos televisio on jumissa toisessa tulossa', 'Napauta puhelimessasi Tulot ja valitse HDMI-liitäntä. Lisää aiheesta: [HDMI-tulon vaihto televisiossa ilman kaukosäädintä](@hdmi).'),
    ],
    marca='lg',
    faq=[
      ('Tarvitsenko Magic Remoten Mando TV:n käyttöön?', 'Tarvitset jotakin vain ensimmäisellä kerralla kysymyksen vahvistamiseen, ja siihen riittää television oma painike tai ohjaussauva. Sen jälkeen käytät vain puhelintasi.'),
      ('Tarvitsenko LG ThinQ -sovelluksen?', 'Et. Mando TV yhdistää suoraan wifisi kautta eikä vaadi LG-tiliä.'),
      ('Voinko sammuttaa ja käynnistää LG-televisioni puhelimella?', 'Sammuttaa kyllä. Käynnistämiseen sinun on pitänyt ottaa televisiossa käyttöön ”Käynnistä TV mobiililaitteella” ja yhdistää kerran television ollessa päällä.'),
    ]),
  dict(clave='hdmi', corto='HDMI-tulon vaihto ilman kaukosäädintä',
    titulo='HDMI-tulon vaihto ilman kaukosäädintä (Samsung, LG, Roku)',
    desc='Vaihda HDMI-tuloa ilman kaukosäädintä Samsungilla, LG:llä tai Rokulla: television painikkeella tai puhelimella. Ilmainen alkuun, ei mainoksia.',
    h1='Näin vaihdat HDMI-tuloa televisiossa ilman kaukosäädintä',
    intro='Konsoli tai suoratoistosoitin on valmis, mutta televisio on jumissa toisessa tulossa eikä kaukosäädintä löydy mistään. HDMI-tulon vaihtoon ilman kaukosäädintä on kaksi tapaa: television oma painike tai puhelimesi. Tässä vaiheet Samsungille, LG:lle ja Rokulle.',
    pasos=[
      'Kokeile ensin helpointa: käynnistä konsoli tai soitin. Jos televisiossa on HDMI-CEC käytössä (Samsungilla se on nimeltään Anynet+, LG:llä SIMPLINK), se vaihtaa itse siihen tuloon.',
      'Jos se ei vaihda, käytä television omaa painiketta alareunan keskellä tai takana. Monessa Samsung- ja LG-televisiossa se on ohjaussauva, joka avaa valikon, jossa on Lähde tai Tulot.',
      'Valitse tämän valikon tulo: HDMI 1, HDMI 2 ja niin edelleen. Numero on liitäntä, johon johto on kytketty.',
      'Jos haluat käyttää puhelinta, yhdistä se samaan wifiin, avaa Mando TV ja napauta televisiotasi.',
      'LG:llä ja Rokulla napauta Tulot ja valitse HDMI-liitäntä. Samsungilla Tulot lähettää televisiolle Lähde-painikkeen, ja valitset nuolilla ja OK:lla.',
      'Voit myös siirtyä nuolilla ja OK:lla television aloitusnäytöltä tuloihin. Merkistä ja valmistusvuodesta riippuen niiden nimi on Lähde, Yhdistetyt laitteet tai Tulot. Roku TV:ssä ne ovat aloitusnäytön HDMI-ruutuja.',
    ],
    extra=[
      ('Samsung', 'Jos television painikkeen valikossa ei ole kohtaa Lähde, avaa puhelimellasi aloitusnäytön valikko ja etsi vasemmalta Lähde tai Yhdistetyt laitteet. Ohjaat sitä Mando TV:n nuolilla ja OK:lla, jotka ovat ilmaisia.'),
      ('LG', 'Paina television ohjaussauvaa ja etsi Tulot. Puhelimellasi voit myös avata Mando TV:ssä tuloluettelon ja napauttaa haluamaasi tuloa.'),
      ('Roku TV', 'Aloitusnäytöllä on jokaiselle tulolle oma ruutunsa, esimerkiksi HDMI 1 tai HDMI 2. Liiku nuolilla ja avaa OK:lla, ilmaiseksi.'),
      ('Jos kyseessä on Android TV- tai Google TV -televisio', 'Mando TV:ssä ei vielä ole Android TV:n tuloluetteloa. Käytä television omaa tulopainiketta tai pääset tuloihin nuolilla ja OK:lla aloitusnäytöltä. Jos sinulla ei ole kaukosäädintä ja haluat yhdistää, lue [Android TV ilman kaukosäädintä](@androidtv).'),
      ('Lisää apua', 'Jos televisio ei käynnisty lainkaan tai et tiedä mistä aloittaa, lue [Kaukosäädin hukassa](@lost-tv). Konsolipelaamista varten opas [Television käynnistys ja konsolin HDMI-tuloon vaihto ilman kaukosäädintä](@console) sisältää HDMI-CEC-vinkin.'),
    ],
    marca=None,
    faq=[
      ('Onko HDMI-tulon vaihto ilmaista?', 'Kyllä. Mando TV:n tuloluettelo on ilmainen, samoin kuin television käynnistys sekä nuolet, OK ja äänenvoimakkuus. Tuloihin pääset myös television valikon kautta.'),
      ('Mistä tiedän, mitä HDMI-tuloa tarvitsen?', 'Katso television HDMI-liitäntöjä: jokaisella on numero. Valitse se, johon konsolisi tai soittimesi johto on kytketty.'),
      ('Entä jos televisio ei käynnisty?', 'Käynnistä se laitteen omalla painikkeella. Jos olet jo kerran yhdistänyt sen ja ottanut käyttöön käynnistyksen verkon kautta, voit käynnistää sen myös puhelimella.'),
    ]),
  dict(clave='androidtv', corto='Android TV ilman kaukosäädintä',
    titulo='Android TV ilman kaukosäädintä: käytä puhelinta',
    desc='Ei Android TV- tai Google TV -kaukosäädintä? Yhdistä puhelimesi näytön 6-merkkisellä koodilla. Ilmaiseksi, ilman tiliä, ilman mainoksia.',
    h1='Android TV ilman kaukosäädintä: näin käytät puhelintasi',
    intro='Jos Android TV- tai Google TV -kaukosäätimesi on hukassa tai sen paristot ovat tyhjät, puhelimesi korvaa sen. Parasta: yhdistämiseen et tarvitse kaukosäädintä, sillä televisio näyttää koodin näytöllä ja kirjoitat sen puhelimeen. Se toimii Android TV -televisioilla merkeiltä Sony, Philips, TCL, Hisense, Sharp ja Xiaomi, Chromecast with Google TV:llä ja Nvidia Shieldillä.',
    pasos=[
      'Käynnistä televisio laitteen painikkeella. Se on lähes aina alareunan keskellä tai takana lähellä nurkkaa.',
      'Yhdistä puhelimesi samaan wifiin kuin televisio.',
      'Lataa Mando TV, joka on ilmainen eikä vaadi Google-tiliä, ja avaa sovellus. Napauta listassa televisiotasi.',
      'Televisio näyttää koodin, jossa on 6 kirjainta ja numeroa. Kirjoita se puhelimeesi ja napauta Muodosta pariliitos. Siihen et tarvitse kaukosäädintä.',
      'Nyt voit käyttää nuolia, OK:ta, Takaisin-, Koti-, äänenvoimakkuus- ja mykistyspainiketta sekä näppäimistöä. Ne ovat ilmaisia, samoin sovellusluettelo. Kosketuslevy on Pro.',
      'Jotta voit käynnistää television seuraavalla kerralla puhelimesta, etsi verkko- tai virta-asetuksista kohtaa ”Wake on LAN”, ”Käynnistys verkon kautta”, ”Verkon valmiustila” tai ”Remote start”.',
    ],
    extra=[
      ('Jos televisiota ei voi käynnistää puhelimesta', 'Kaikkia Android TV -televisioita ei voi käynnistää verkon kautta; se riippuu valmistajasta ja mallista. Jos omassasi ei ole ominaisuutta, käynnistä se television painikkeella ja jatka puhelimella. Sammuttaa voit sen sovelluksella.'),
      ('Chromecast with Google TV, Google TV Streamer ja Shield', 'Ne yhdistetään samalla tavalla: sama wifi, napauta laitetta listassa ja kirjoita koodi. Jos televisio näyttää toista tuloa, vaihda se HDMI-liitäntään, johon laite on kytketty, kuten kerrotaan oppaassa [HDMI-tulon vaihto televisiossa ilman kaukosäädintä](@hdmi).'),
      ('Jos koodi ei tule näkyviin tai sitä sanotaan vääräksi', 'Tarkista, että televisio on todella päällä eikä valmiustilassa. Koodi vaihtuu jokaisella pyynnöllä: vain viimeisin toimii. Lisätietoja löydät oppaasta [Android TV pyytää pariliitoskoodia](@androidtv-code).'),
      ('Googlen sovellus vai Mando TV', 'Googlella on oma sovelluksensa, johon tarvitset Google-tilin. Mando TV ei vaadi tiliä, toimii myös Windowsilla ja ohjaa LG-, Samsung- ja Roku-televisioita samalla sovelluksella.'),
    ],
    marca='android',
    faq=[
      ('Tarvitsenko kaukosäätimen puhelimen pariliitokseen?', 'Et. Koodi tulee television näytölle ja kirjoitat sen puhelimeen. Sinun tarvitsee vain käynnistää televisio, tarvittaessa laitteen painikkeella.'),
      ('Toimiiko se Hisensen kanssa?', 'Hisense-televisioissa, joissa on Android TV tai Google TV, kyllä. Hisense-televisiot, joissa on toinen järjestelmä, eivät ole yhteensopivia.'),
      ('Voinko kirjoittaa puhelimeni näppäimistöllä?', 'Kyllä, niitä on kaksi. Ilmainen näppäimistö kirjoittaa television ja useimpien sovellusten hakuun ja tekstikenttiin. YouTube ja Netflix hyväksyvät vain oman näytön näppäimistönsä, joten YouTubea varten on YouTube-näppäimistö (Pro): kirjoita tai sano, mitä haluat katsoa, ja YouTube avautuu televisiossa tuloksineen. Netflixiä käytetään nuolilla ja OK:lla.'),
    ]),
  dict(clave='lg-on', corto='LG-televisio päälle puhelimella',
    titulo='LG-television käynnistys puhelimella (ohje)',
    desc='Käynnistä LG-televisio puhelimella wifin kautta: ota käyttöön ”Käynnistä TV mobiililaitteella” ja käytä Mando TV:tä. Vaihe vaiheelta, ilmaiseksi.',
    h1='Näin käynnistät LG-television puhelimella',
    intro='LG-television voi käynnistää puhelimella, mutta sitä varten sinun on ensin otettava käyttöön yksi asetus televisiossa. Sen jälkeen puhelimesi käynnistää LG-television wifisi kautta ilman kaukosäädintä. Siihen menee viisi minuuttia ja teet sen vain kerran.',
    pasos=[
      'Yhdistä puhelimesi ja LG-televisio samaan wifiin.',
      'Avaa televisiossa asetukset ja etsi ”Käynnistä TV mobiililaitteella”. Löydät sen kohdasta Asetukset > Yleiset > Laitteet > Ulkoiset laitteet (vanhemmissa malleissa Yhteys > Mobiiliyhteyden hallinta).',
      'Ota käyttöön ”Käynnistä wifin kautta”. Jos televisiosi on yhdistetty verkkokaapelilla, ota sen sijaan käyttöön kaapelia koskeva vaihtoehto.',
      'Jos televisiossasi on ”Pikakäynnistys+”, ota sekin käyttöön.',
      'Avaa television ollessa päällä Mando TV puhelimessasi ja napauta listassa LG-televisiotasi. Vahvista näytölle tuleva kysymys. Näin sovellus oppii herättämään sen.',
      'Sammuta televisio ja kokeile: napauta Mando TV:ssä televisiota, niin sovellus kysyy, haluatko käynnistää sen.',
    ],
    extra=[
      ('Jos se ei käynnisty', 'Television on täytynyt olla samassa wifissä sammutettaessa. Tarkista, että asetus on edelleen käytössä ja puhelimesi on samassa verkossa. Jos olet vaihtanut reitittimen, yhdistä uudelleen television ollessa päällä.'),
    ],
    marca='lg',
    faq=[
      ('Voinko käynnistää LG-television puhelimella, jos en ole koskaan yhdistänyt sitä?', 'Et. Ensin sinun on otettava televisiossa käyttöön ”Käynnistä TV mobiililaitteella” ja yhdistettävä kerran Mando TV:hen television ollessa päällä.'),
      ('Tarvitsenko LG ThinQ -sovelluksen?', 'Et. Mando TV yhdistää suoraan wifisi kautta eikä vaadi LG-tiliä.'),
      ('Toimiiko se mobiilidatalla?', 'Ei. Puhelimen ja television on oltava samassa wifissä.'),
    ]),
  dict(clave='console', corto='Televisio ja konsoli ilman kaukosäädintä',
    titulo='Ei kaukosäädintä? Käynnistä televisio, vaihda HDMI',
    desc='Julkaisupäivä eikä kaukosäädintä? Käynnistä televisio ja vaihda puhelimella PS5:n tai Xboxin HDMI-tuloon. Ilmaiseksi, ilman mainoksia.',
    h1='Näin käynnistät television ja vaihdat konsolisi HDMI-tuloon ilman kaukosäädintä',
    intro='GTA VI:n julkaisupäivä, konsoli on valmiina ja kaukosäädin on kadonnut jonnekin sohvatyynyjen väliin. Sitä tapahtuu useammin kuin luulisi. Mando TV:llä puhelimesi käynnistää television ja vaihtaa kotisi wifin kautta PlayStationisi tai Xboxisi tuloon.',
    pasos=[
      'Yhdistä puhelimesi samaan wifiin kuin televisio.',
      'Avaa Mando TV ja napauta listassa televisiotasi (Samsung, LG, Roku tai Android TV).',
      'Jos televisio on sammutettu, napauta Käynnistä. Se onnistuu, jos televisiossa on käytössä käynnistys verkon kautta. Jos et ole ottanut sitä käyttöön, käynnistä televisio tämän yhden kerran laitteen painikkeella ja ota se käyttöön seuraavaa kertaa varten.',
      'Käynnistä konsoli. Jos HDMI-CEC on käytössä (katso ilmainen vinkki alla), televisio vaihtaa itse sen tuloon.',
      'Jos se ei vaihda, napauta Mando TV:ssä Tulot ja valitse HDMI-liitäntä, johon konsoli on kytketty: HDMI 1, HDMI 2 ja niin edelleen.',
      'Äänenvoimakkuutta säädät pelatessa sovelluksen isoilla painikkeilla.',
    ],
    extra=[
      ('Ilmainen vinkki: anna konsolin vaihtaa televisio', 'PS5 ja Xbox voivat käynnistää television ja hypätä heti käynnistyksessä sen HDMI-tuloon HDMI-CEC:n ansiosta. PS5:ssä löydät sen kohdasta Asetukset > Järjestelmä > HDMI > Ota HDMI-laitelinkki käyttöön. Avaa Xboxissa Asetukset > Yleiset > TV- ja näyttövaihtoehdot ja etsi laitteen ohjauksen asetus. Televisiossa toiminnon nimi vaihtelee merkin mukaan: Anynet+ Samsungilla, SIMPLINK LG:llä ja BRAVIA Sync tai HDMI-ohjaus muilla.'),
      ('Jos televisio jää toiseen kuvaan', 'Jos konsoli on päällä mutta televisio näyttää yhä antennia tai sovellusta, se ei ole vaihtanut tuloa. Napauta puhelimessasi Tulot ja valitse konsolin HDMI-tulo. Tai käytä nuolia ja OK:ta päästäksesi television tuloihin, tai television omaa painiketta, ja valitse HDMI-liitäntä. Numero on liitäntä, johon kytkit konsolin johdon.'),
      ('Jos kyseessä on Roku TV', 'Television painike, yleensä alareunan keskellä tai takana, käynnistää sen. Siitä eteenpäin puhelimesi hoitaa loput.'),
    ],
    marca=None,
    faq=[
      ('Onko Mando TV:llä jotain tekemistä GTA VI:n kanssa?', 'Ei. Mando TV ei ole yhteydessä Rockstar Gamesiin eikä Take-Twoon. Sovellus vain auttaa sinua välttämään pelaamatta jäämisen, kun et löydä kaukosäädintä.'),
      ('Onko HDMI-tulon vaihto ilmaista?', 'Kyllä. Mando TV:n tuloluettelo on ilmainen, samoin kuin television käynnistys sekä nuolet, OK ja äänenvoimakkuus. Voit myös antaa konsolin vaihtaa tulon itse HDMI-CEC:llä.'),
      ('Toimiiko se televisiollani?', 'Se toimii Samsung-, LG-, Roku- ja Android TV -televisioilla samassa wifissä. Jos omasi on toista merkkiä, HDMI-CEC-vinkki voi silti auttaa.'),
      ('Voinko käyttää sitä GTA VI:n (GTA 6) pelaamiseen PS5:llä tai Xboxilla?', 'Mando TV ei puutu konsoliin eikä peliin. Se huolehtii vain siitä, että televisio on päällä ja oikeassa HDMI-tulossa, jotta voit istua alas ja pelata.'),
    ]),
  dict(clave='samsung-lost', corto='Samsung-televisio ilman kaukosäädintä',
    titulo='Samsung-kaukosäädin hukassa? Käytä puhelinta',
    desc='Samsung-kaukosäädin hukassa tai rikki? Käytä puhelinta kaukosäätimenä Tizen-televisioon wifin kautta. Helppoa Mando TV:llä, ilmaiseksi, ilman mainoksia.',
    h1='Samsung-televisio ilman alkuperäistä kaukosäädintä: näin käytät puhelintasi',
    intro='Jos Samsung-kaukosäätimesi on hukassa tai ei enää toimi, voit käyttää puhelintasi kaukosäätimenä wifin kautta. Se toimii Samsung-televisioilla, joissa on Tizen ja valmistusvuosi 2016 tai uudempi.',
    pasos=[
      'Käynnistä televisio laitteen painikkeella. Useimmissa malleissa se on alhaalla tai takana, joskus pienenä ohjaussauvana.',
      'Tarkista, että televisio on yhdistetty wifiisi ja puhelimesi on samassa verkossa.',
      'Avaa Mando TV puhelimessasi. Samsung-televisiosi tulee listaan itsestään. Napauta sitä.',
      'Televisio pyytää sinua vahvistamaan yhteyden. Useimmissa malleissa vahvistat sen television painikkeilla tai takana olevalla ohjaussauvalla.',
      'Valmis, nyt voit käyttää puhelintasi kaukosäätimenä. Painikkeet, näppäimistö ja sovellukset ovat ilmaisia; kosketuslevy on Pro-ominaisuus.',
      'Jotta voit käynnistää television seuraavalla kerralla puhelimesta, mene kohtaan Asetukset > Yleiset > Verkko > Asiantuntija-asetukset ja ota käyttöön ”Käynnistä mobiililaitteella”.',
    ],
    extra=[
      ('Jos televisio ei pyydä lupaa', 'Lupa voi jo olla tallennettuna tai televisio on toisessa wifissä. Sulje Mando TV ja avaa sovellus uudelleen television ollessa päällä. Jos televisio on vuotta 2016 vanhempi, se käyttää toista järjestelmää, jota ei vielä tueta.'),
      ('Jos kieltäydyit luvasta vahingossa', 'Mene televisiossa kohtaan Asetukset > Yleiset > Ulkoisten laitteiden hallinta > Laiteyhteyksien hallinta ja aseta Mando TV sallituksi. Jos puhelimesi ei silti löydä televisiota, lue [Puhelimesi ei löydä televisiota](@not-found).'),
    ],
    marca='samsung',
    faq=[
      ('Miten vahvistan yhteyden, jos minulla ei ole kaukosäädintä?', 'Useimmissa malleissa vahvistat sen television painikkeilla tai takana olevalla ohjaussauvalla. Jos mallissasi ei ole painikkeita, kirjoita osoitteeseen hola@mandotv.app, niin autamme sinua.'),
      ('Vaatiiko Mando TV Samsung-tilin?', 'Ei. Yhteys kulkee suoraan wifisi kautta ilman Samsung-tiliä.'),
      ('Toimiiko se vanhemman Samsung-televisioni kanssa?', 'Se toimii Samsung-televisioilla, joissa on Tizen ja valmistusvuosi 2016 tai uudempi.'),
    ]),
  dict(clave='wifi', corto='Puhelin kaukosäätimenä wifin kautta',
    titulo='Puhelin kaukosäätimenä: ohjaa televisiota wifillä',
    desc='Yhdistä puhelimesi wifillä televisioon ja käytä sitä kaukosäätimenä Samsungille, LG:lle, Rokulle ja Google TV:lle. Vaiheet merkeittäin Mando TV:llä. Ilmaiseksi.',
    h1='Näin yhdistät puhelimesi wifillä televisioon kaukosäätimeksi',
    intro='Tarvitset vain puhelimesi ja television samassa wifissä sekä kaukosäädinsovelluksen. Mando TV löytää televisiosi itse ja toimii Samsungin, LG:n, Rokun, Google TV:n ja Android TV:n kanssa.',
    pasos=[
      'Yhdistä puhelin ja televisio samaan wifiin.',
      'Avaa Mando TV. Televisiosi tulee listaan itsestään. Napauta sitä.',
      'Vahvista yhteys merkillesi (tiedot ovat alempana).',
      'Ohjaa televisiota painikkeilla tai puhelimesi näppäimistöllä. Kosketuslevy on Pro-ominaisuus.',
    ],
    extra=[
      ('Samsung', 'Televisio kysyy, sallitko yhteyden. Vahvista se ensimmäisellä kerralla näytöllä. Se toimii Tizenillä, valmistusvuosi 2016 tai uudempi. Jotta voit käynnistää sen puhelimesta, ota käyttöön ”Käynnistä mobiililaitteella” kohdasta Asetukset > Yleiset > Verkko > Asiantuntija-asetukset.'),
      ('LG', 'Televisio näyttää kysymyksen, jossa pyydetään lupaa. Vahvista se ensimmäisellä kerralla. Jotta voit käynnistää sen puhelimesta, etsi asetuksista ”Käynnistä TV mobiililaitteella” ja ota käyttöön ”Käynnistä wifin kautta”.'),
      ('Roku', 'Roku ei vaadi pariliitosta: napauta sitä listassa, niin olet yhdistetty. Jotta voit käynnistää sen, ota käyttöön ”TV:n pikakäynnistys” kohdasta Asetukset > Järjestelmä > Virta.'),
      ('Google TV ja Android TV', 'Televisio näyttää koodin näytöllä. Kirjoita se Mando TV:hen ensimmäisellä kerralla. Jotta voit käynnistää sen, etsi asetuksista ”Wake on LAN”, ”Käynnistys verkon kautta” tai ”Verkon valmiustila”.'),
    ],
    marca=None,
    faq=[
      ('Tarvitsenko internetin käyttääkseni puhelinta kaukosäätimenä?', 'Tarvitset puhelimesi ja television samassa wifissä. Mando TV yhdistää tämän verkon kautta suoraan televisioosi.'),
      ('Miksi televisioni ei tule listaan?', 'Tarkista, että televisio on päällä eikä puhelimesi käytä mobiilidataa tai toista wifiä. Joissakin reitittimissä on vierasverkko, joka erottaa laitteet toisistaan.'),
      ('Voinko käyttää Mando TV:tä iPhonella tai Android-puhelimella?', 'iPhonella ja iPadilla kyllä: sovellus on jo App Storessa. Windowsille se on myös Microsoft Storessa. Android tulee pian: voit liittyä ilmaiseen ennakkokäyttöön Google Playssa.'),
    ]),
  dict(clave='pc', corto='Television ohjaus tietokoneella',
    titulo='Ohjaa televisiota Windows-tietokoneella (ilmaiseksi)',
    desc='Käytä Windows-tietokonetta kaukosäätimenä Samsungille, LG:lle, Rokulle tai Google TV:lle wifillä. Painikkeet, näppäimistö ja sovellukset ilmaiseksi.',
    h1='Näin ohjaat televisiotasi Windows-tietokoneella',
    intro='Jos vietät päivän tietokoneen ääressä, sinun ei tarvitse etsiä kaukosäädintä: Mando TV Windowsille ohjaa Samsung-, LG-, Roku-, Google TV- tai Android TV -televisiotasi kotisi wifin kautta. Kätevä sovellusten vaihtoon, äänen kovemmalle laittoon tai YouTubessa kirjoittamiseen tietokoneen näppäimistöllä.',
    pasos=[
      'Lataa Mando TV ilmaiseksi Microsoft Storesta Windows 10- tai 11-tietokoneellesi.',
      'Tarkista, että tietokone ja televisio ovat samassa verkossa (wifi tai kaapeli, mutta saman reitittimen kautta).',
      'Avaa Mando TV: televisiosi tulee listaan itsestään. Napauta tai napsauta sitä.',
      'Vahvista ensimmäisellä kerralla yhteys television näytöllä (Google TV:ssä ja Android TV:ssä kirjoitat television näyttämän koodin).',
      'Valmis: käytä painikkeita tai näppäimistöä kirjoittaaksesi television hakukenttään. Kosketuslevy on Pro-ominaisuus.',
    ],
    extra=[
      ('PC-pikanäppäimet (Pro)', 'Mando TV Prolla ohjaat televisiota tietokoneen näppäimistöllä: nuolinäppäimet liikkumiseen, Enter OK:ksi, askelpalautin tai Esc Takaisin-painikkeeksi, + ja - äänenvoimakkuuteen, M mykistykseen ja välilyönti taukoon.'),
      ('Pieni kaukosäädin aina päällimmäisenä (Pro)', 'Pidä pieni kaukosäädinikkuna aina näkyvissä, kun työskentelet tai pelaat tietokoneella.'),
      ('Puhu televisiolle tietokoneelta (Pro)', 'Mando TV Prolla annat televisiolle komentoja tietokoneen mikrofonilla: ”avaa YouTube”, ”lisää ääntä” tai ”sammuta 30 minuutin kuluttua”, juuri niin kuin puhut. Windowsissa puhe tunnistetaan itse tietokoneella: et tarvitse internetiä, sinun ei tarvitse muuttaa Windowsin asetuksia, ja se toimii sovelluksen 6 kielellä. Se, mitä sanot, ei poistu tietokoneelta eikä sitä tallenneta. Vain hyvin vanhoilla suorittimilla sovellus turvautuu Windowsin sanelutoimintoon. Silloin verkkopohjaisen puheentunnistuksen on oltava päällä tietosuora-asetuksissa ja Windowsiin on lisättävä suomi (Suomi). Jos jotain puuttuu, sovellus ilmoittaa siitä ja avaa asetuksen painikkeella.'),
    ],
    marca=None,
    faq=[
      ('Tarvitsenko kaapelin tai Bluetoothin television ohjaamiseen tietokoneella?', 'Et. Mando TV yhdistää kotiverkkosi kautta: tietokoneen ja television tarvitsee vain olla samassa reitittimessä.'),
      ('Toimiiko se jokaisella televisiolla?', 'Se toimii Samsung-televisioilla, joissa on Tizen (valmistusvuosi 2016 tai uudempi), LG:llä webOS:llä, Rokulla sekä Google TV:llä tai Android TV:llä (Sony, Philips, TCL, Hisense, Sharp, Xiaomi, Toshiba, Panasonic, Haier, Skyworth ja muut).'),
      ('Mitä se maksaa?', 'Painikkeet, näppäimistö ja käynnistys verkon kautta ovat ilmaisia ja ilman mainoksia. Mando TV Pro on kertaosto ilman tilausta lisäominaisuuksiin, kuten kosketuslevyyn, PC-pikanäppäimiin ja pieneen kaukosäätimeen.'),
      ('Miksi mikrofoni ei ymmärrä minua Windowsissa?', 'Tarkista, että puheominaisuus on käytössä (se kuuluu Pro-versioon) ja että tietokoneen mikrofoni toimii Windowsissa. Lähes kaikilla tietokoneilla puhe tunnistetaan laitteella itsellään, ilman internetiä. Vain hyvin vanhoilla suorittimilla sovellus käyttää Windowsin sanelua. Tarkista silloin, että verkkopohjainen puheentunnistus on päällä Windowsin tietosuora-asetuksissa ja että Windowsissa on suomi (Suomi) kieliasetuksissa. Mando TV käyttää tätä kieltä vain, kun se kuuntelee.'),
    ]),
  dict(clave='roku-403', corto='Roku-sovellus ei toimi',
    titulo='Roku-sovellus ei toimi? Korjaa virhe 403',
    desc='Puhelin yhdistetty, mutta Roku ei reagoi? Ota ”Ohjaus mobiilisovelluksilla” käyttöön 5 vaiheessa ja käytä puhelinta taas kaukosäätimenä.',
    h1='Roku-sovellus ei toimi: näin korjaat ongelman',
    intro='Jos puhelimesi löytää Rokun ja yhdistää, mutta mikään painike ei tee mitään, syy on lähes aina Rokun omassa asetuksessa, joka estää kaukosäädinsovellukset. Uudemmat Roku-versiot ovat oletuksena rajoitetumpia. Rokun valikossa se korjataan minuutissa.',
    pasos=[
      'Paina Rokussa Home ja mene kohtaan Asetukset.',
      'Avaa Järjestelmä ja sitten Järjestelmän lisäasetukset.',
      'Mene kohtaan ”Ohjaus mobiilisovelluksilla”. Joissakin malleissa se on nimeltään ”Ulkoinen ohjaus”.',
      'Valitse kohdassa ”Verkon käyttö” Oletus tai Permissive. Jos mallissasi on vain kytkin, jätä se tilaan Käytössä.',
      'Palaa puhelimesi Mando TV:hen ja napauta Rokuasi. Painikkeet reagoivat nyt.',
    ],
    extra=[
      ('Näin tunnistat, onko tämä ongelmasi', 'Merkki on yksiselitteinen: puhelimesi näkee Rokun listassa ja yhdistää, mutta mitään ei tapahdu, kun napautat painiketta. Sisäisesti Roku vastaa virheellä 403, joka tarkoittaa ”kielletty”. Mando TV tunnistaa sen yhdistäessään ja näyttää juuri nämä vaiheet näytöllä.'),
      ('Oletus vai Permissive, kumman valitsen?', 'Oletus riittää: se hyväksyy kotiverkostasi tulevat komennot, ja niitä kaukosäädin tarvitsee. Permissive on avoimempi, ja sitä tarvitaan vain epätavallisissa verkoissa.'),
      ('Jos sinulla ei ole Roku-kaukosäädintä', 'Jos asetus on Poissa käytöstä, sen voi muuttaa vain oikealla Roku-kaukosäätimellä. Lainaa sellainen muuttaaksesi sen kerran; sen jälkeen voit tehdä kaiken puhelimellasi. Lue myös [Roku-kaukosäädin hukassa](@roku-lost).'),
    ],
    marca='roku',
    faq=[
      ('Miksi Rokuni ei enää reagoi, vaikka se toimi aiemmin?', 'Roku-päivitys voi rajoittaa tätä asetusta enemmän. Vika ei ole puhelimessasi tai wifissäsi: sinun tarvitsee vain sallia ohjaus sovelluksilla uudelleen.'),
      ('Koskeeko tämä Roku TV:tä ja Roku-soittimia?', 'Kyllä. Asetus on Roku-soittimissa ja Roku TV -laitteissa samassa valikossa.'),
      ('Onko turvallista jättää asetus tilaan Oletus?', 'Kyllä. Se hyväksyy vain kotiverkkosi laitteilta tulevia komentoja.'),
    ]),
  dict(clave='not-found', corto='Puhelin ei löydä televisiota',
    titulo='Puhelin ei löydä televisiota? 6 asiaa tarkistettavaksi',
    desc='Eikö kaukosäädinsovellus löydä televisiotasi? Tarkista wifi, VPN ja paikallisen verkon käyttöoikeus. Samsungille, LG:lle, Rokulle ja Android TV:lle.',
    h1='Puhelimesi ei löydä televisiota: tarkista nämä',
    intro='Avaat kaukosäädinsovelluksen ja lista on tyhjä, tai televisio tulee näkyviin mutta yhteys katkeaa. Lähes aina syy on verkossa eikä televisiossa. Tarkista nämä kohdat järjestyksessä: ensimmäinen ratkaisee useimmat tapaukset.',
    pasos=[
      'Katso, missä wifissä puhelimesi on ja missä televisio. Sen on oltava sama verkko samalla nimellä. Vierasverkko ei toimi, koska se erottaa laitteet toisistaan.',
      'Sammuta puhelimesi VPN, jos käytät sellaista. VPN:n ollessa päällä puhelimesi menee internetiin toisen verkon kautta eikä näe kotisi laitteita, tai yhteys katkeaa muutamassa sekunnissa.',
      'Sammuta hetkeksi mobiilidata. Jotkin puhelimet vaihtavat heikon signaalin takia wifistä itse mobiilidataan.',
      'Käynnistä televisio ja odota, että se on käynnistynyt kokonaan. Sammutettu televisio ei vastaa hakuun.',
      'Tarkista iPhonella, että sovelluksella on ”Lähiverkko”-lupa: Asetukset > Tietosuoja ja turvallisuus > Lähiverkko.',
      'Jos se ei vieläkään tule näkyviin, lisää se käsin: napauta Mando TV:ssä ”Lisää IP-osoitteella” ja kirjoita television IP-osoite.',
    ],
    extra=[
      ('Anna sovelluksen opastaa', 'Televisioluettelossa on painike sitä tilannetta varten, ettei televisiosi näy. Sovellus tarkistaa yleisimmät syyt vaihe vaiheelta (sama wifi, VPN, lähiverkon käyttöoikeus ja muuta) ja näyttää jokaisen korjauksen jälkeen painikkeen uudelleen tarkistusta varten. Avustaja on ilmainen.'),
      ('Mistä löydät television IP-osoitteen', 'Se on television verkkovalikossa ja hieman erilainen mallista riippuen. LG:llä: Asetukset, Verkko, Wifi-yhteys, Wifin lisäasetukset. Samsungilla: Asetukset, Yleiset, Verkko, Verkon tila, IP-asetukset. Rokulla: Asetukset, Verkko, Tiedot. Android TV:ssä ja Google TV:ssä: Asetukset, Verkko ja internet, napauta sitten omaa verkkoasi. Se on luku, kuten 192.168.1.86.'),
      ('Jos televisio näkyy mutta yhteys katkeaa', 'Jos yhteys katkeaa muutaman sekunnin kuluttua, syy on yleensä puhelimessa: VPN, vaihto toiseen wifiin tai virransäästötila. Sammuta VPN, pysy samassa wifissä ja yritä uudelleen.'),
      ('Wifi 2,4 ja 5 GHz', 'Ei haittaa, vaikka puhelimesi on 5 GHz:n verkossa ja televisio 2,4 GHz:n verkossa, kunhan molemmat tulevat samasta reitittimestä. Jos sinulla on wifin toistin eikä televisio silti näy, mene puhelimen kanssa lähemmäs pääreititintä ja yritä uudelleen.'),
    ],
    marca=None,
    faq=[
      ('Voinko ohjata televisiota mobiilidatalla?', 'Et. Kaukosäätimen signaali kulkee kotisi wifin kautta, joten puhelimen ja television on oltava samassa verkossa.'),
      ('Miksi se ei toimi VPN:n ollessa päällä?', 'Koska VPN ohjaa kaiken puhelimesi liikenteen toisen verkon kautta, eikä puhelin enää näe kotisi laitteita. Sammuta se, kun käytät kaukosäädintä.'),
      ('Toimiiko se Bluetoothilla tai infrapunalla?', 'Älytelevisioilla Mando TV käyttää wifiä. Infrapuna toimii vain Android-puhelimilla, joissa on infrapunalähetin, ja on tarkoitettu televisioille, jotka eivät ole älytelevisioita. Bluetooth on betassa, ilmainen ja vain Android 9:stä alkaen: puhelin yhdistyy televisioon Bluetooth-näppäimistönä ja -kaukosäätimenä, kokonaan ilman wifiä. Se toimii Google TV:n, Android TV:n ja Fire TV:n kanssa; muilla merkeillä, jotka hyväksyvät Bluetooth-näppäimistöt, se voi toimia, Roku ei hyväksy niitä.'),
    ]),
  dict(clave='androidtv-code', corto='Android TV:n pariliitoskoodi',
    titulo='Android TV pyytää pariliitoskoodia: näin toimit',
    desc='Android TV tai Google TV näyttää yhdistettäessä 6-merkkisen koodin. Näin kirjoitat sen ja mitä teet, jos se ei tule näkyviin tai on väärä.',
    h1='Android TV pyytää pariliitoskoodia: näin toimit',
    intro='Kun yhdistät puhelimesi ensimmäistä kertaa Android TV:hen tai Google TV:hen, televisio näyttää näytöllä 6-merkkisen koodin. Se on normaalia ja tapahtuu vain kerran: näin varmistetaan, ettei kukaan muu voi ohjata televisiotasi. Tässä näet, miten kirjoitat sen ja mitä teet, jos se ei tule näkyviin.',
    pasos=[
      'Käynnistä televisio ja jätä aloitusnäyttö näkyviin.',
      'Avaa Mando TV puhelimessasi samassa wifissä kuin televisio ja napauta listassa televisiotasi.',
      'Katso television näyttöä: siihen tulee koodi, jossa on 6 kirjainta ja numeroa.',
      'Kirjoita se puhelimeesi täsmälleen sellaisena kuin se näytetään ja napauta Muodosta pariliitos. Kirjaimet ovat vain A:sta F:ään, joten pyöreä merkki on aina numero nolla.',
      'Valmis. Televisio muistaa puhelimesi eikä kysy koodia uudelleen.',
    ],
    extra=[
      ('Jos koodi ei tule television näytölle', 'Tarkista, että televisio on todella päällä eikä valmiustilassa ja että puhelimesi on samassa wifissä. Napauta puhelimessasi televisiota vielä kerran. Jos se ei vieläkään tule näkyviin, käynnistä televisio uudelleen: irrota virtajohto kymmeneksi sekunniksi, kytke se takaisin ja yritä uudelleen.'),
      ('Jos koodia sanotaan vääräksi', 'Koodi vaihtuu jokaisella pyynnöllä. Jos sinulla meni kauan tai pyysit sitä kahdesti, vain näytön viimeisin toimii. Napauta puhelimessasi televisiota vielä kerran ja kirjoita uusi koodi.'),
      ('Jos televisio kysyy koodia uudelleen', 'Näin käy, jos televisio on palautettu tehdasasetuksiin tai tyhjennät sovelluksen tiedot puhelimestasi. Tee pariliitos uudelleen, niin se tallentuu. Jos sinulla ei ole lainkaan kaukosäädintä, lue [Android TV ilman kaukosäädintä](@androidtv).'),
    ],
    marca='android',
    faq=[
      ('Mitkä televisiot käyttävät tätä koodia?', 'Ne, joissa on Android TV tai Google TV: Sony, Philips, TCL, Hisense, Sharp, Xiaomi, Chromecast with Google TV ja muutama muu.'),
      ('Tarvitsenko Google-tilin puhelimeeni?', 'Et. Näytön koodi on kaikki, mitä tarvitset.'),
      ('Onko tämä turvallista?', 'Kyllä. Koodi todistaa, että istut television edessä: kukaan ei voi tehdä pariliitosta näkemättä koodia näytöllä.'),
    ]),
  dict(clave='roku-lost', corto='Roku-kaukosäädin hukassa',
    titulo='Roku-kaukosäädin hukassa? Käytä puhelinta wifillä',
    desc='Roku-kaukosäädin hukassa? Puhelimesi korvaa sen wifin kautta. Helpot vaiheet, myös jos olet vaihtanut reitittimen eikä Rokulla ole wifiä.',
    h1='Roku-kaukosäädin hukassa: näin käytät puhelintasi',
    intro='Jos Roku-kaukosäätimesi on hukassa tai ei enää toimi, puhelimesi korvaa sen, kunhan Roku on yhä yhdistetty wifiisi. Ja jos olet vaihtanut wifin tai reitittimen, siihenkin on ratkaisu.',
    pasos=[
      'Yritä ensin saada kaukosäädin soimaan. Jos Roku-kaukosäätimessäsi on kaiutin, esimerkiksi Roku Voice Remote Prossa, avaa Mando TV, yhdistä Rokuun ja käytä toimintoa, joka saa kaukosäätimen soimaan, jotta löydät sen. Se toimii vain kaiuttimella varustetuilla Roku-kaukosäätimillä, ja Rokun on oltava päällä.',
      'Käynnistä televisio ja jätä Roku kytketyksi. Sinun ei tarvitse koskea siihen.',
      'Yhdistä puhelimesi samaan wifiin, jota Roku käyttää.',
      'Avaa Mando TV. Roku tulee listaan itsestään. Napauta sitä.',
      'Käytä nuolia, OK:ta, Kotia ja Takaisin-painiketta kuten tavallisella kaukosäätimellä. Roku ei pyydä koodia.',
      'Jos painikkeet eivät tee mitään, Roku estää ohjauksen sovelluksilla: opas [Roku-sovellus ei toimi](@roku-403) kertoo, miten sallit sen.',
    ],
    extra=[
      ('Jos Rokulla ei ole wifiä (reititin vaihdettu tai muutettu)', 'Ilman kaukosäädintä et pääse valikkoon määrittämään uutta verkkoa, mutta on temppu: Roku yhdistää itse verkkoon, jolla on sama nimi ja sama salasana kuin vanhalla. Luo toisella puhelimella wifi-hotspot juuri tällä nimellä ja salasanalla, yhdistä Mando TV -puhelin siihen, niin Roku tulee listaan. Mene sieltä kohtaan Asetukset, Verkko ja yhdistä se uuteen wifiin.'),
      ('Jos kyseessä on Roku TV', 'Roku TV -laitteissa on laitteen painike, lähes aina alareunan keskellä tai takana, joka käynnistää television. Se riittää käynnistämiseen ja jatkamiseen puhelimella.'),
      ('Jos haluat ostaa toisen kaukosäätimen', 'Varmista, että se sopii malliisi. Television taakse piilotetut pienet Roku-soittimet tarvitsevat kaukosäätimen ilman infrapunaa, koska infrapuna ei yllä niihin.'),
    ],
    marca='roku',
    faq=[
      ('Voiko puhelimeni käynnistää Rokun?', 'Kytketty Roku-soitin on aina päällä. Roku TV:n Mando TV käynnistää wifin kautta, jos ”TV:n pikakäynnistys” on otettu käyttöön kohdassa Asetukset > Järjestelmä > Virta.'),
      ('Entä äänenvoimakkuus?', 'Roku TV:ssä puhelimesi säätää äänenvoimakkuutta kovemmalle ja hiljaisemmalle. HDMI:llä kytketyssä Roku-soittimessa se riippuu televisiosta: monessa se toimii, joissakin ei.'),
      ('Pitääkö minun luoda tili?', 'Ei. Mando TV ei vaadi tiliä ja ohjaa lisäksi Samsung-, LG- ja Android TV -televisioita samalla sovelluksella.'),
    ]),
]

SOPORTE = dict(
  titulo='Ohje: yhdistä televisio Mando TV:hen ja käynnistä se',
  desc='Näin yhdistät Mando TV -kaukosäätimen LG:hen, Samsungiin, Rokuun tai Android TV:hen, käynnistät television puhelimella ja ratkaiset ongelmat.',
  h1='Ohje',
  intro='Yleisimmät kysymykset vaiheiden järjestyksessä. Jos omaasi ei löydy, kirjoita meille osoitteeseen <a href="mailto:hola@mandotv.app?subject=Ohje%20Mando%20TV:hen">hola@mandotv.app</a>, niin vastaamme.',
)
SOPORTE_HTML = '''      <h2 id="encontrar">Television löytäminen</h2>
      <div class="preguntas">
        <details open><summary>Televisioni ei tule listaan</summary>
          <ol>
            <li>Tarkista, että puhelimesi ja televisio ovat samassa wifissä. Jos reitittimessäsi on 2,4 GHz:n ja 5 GHz:n verkko eri nimillä, ne eivät joskus näe toisiaan.</li>
            <li>Varmista, että televisio on päällä.</li>
            <li>Tarkista iPhonella, että Mando TV:llä on ”Lähiverkko”-lupa kohdassa Asetukset, Mando TV.</li>
            <li>Napauta televisioluettelossa painiketta ”Televisio ei näy?”: sovellus tarkistaa yleisimmät syyt vaihe vaiheelta (sama wifi, VPN, lähiverkon käyttöoikeus ja muuta) ja näyttää jokaisen korjauksen jälkeen painikkeen uudelleen tarkistusta varten.</li>
            <li>Jos se ei vieläkään tule näkyviin, napauta +-painiketta, valitse merkki ja kirjoita television IP-osoite. Näet sen television verkkovalikossa (esimerkiksi 192.168.1.50).</li>
          </ol>
        </details>
        <details><summary>Toimiiko se mobiilidatalla tai ollessani poissa kotoa?</summary>
          <p>Ei. Mando TV puhuu televisiolle kotiverkkosi sisällä, joten puhelimesi on oltava yhdistetty tähän wifiin.</p>
        </details>
      </div>

      <h2 id="conectar">Ensimmäinen yhdistäminen</h2>
      <p>Täydelliset oppaat merkeittäin: <a href="@@R_lg@@">LG</a>, <a href="@@R_samsung@@">Samsung</a>, <a href="@@R_roku@@">Roku</a> ja <a href="@@R_android@@">Android TV</a>.</p>
      <div class="preguntas">
        <details><summary>LG</summary>
          <p>Kun napautat televisiota, näytölle tulee kysymys, jossa pyydetään lupaa. Vahvista se tavallisella kaukosäätimellä. Teet sen vain kerran.</p>
        </details>
        <details><summary>Samsung</summary>
          <p>Televisio kysyy, sallitko Mando TV:n yhteyden. Valitse kaukosäätimellä ”Salli”. Jos kieltäydyit vahingossa, mene kohtaan Asetukset > Yleiset > Ulkoisten laitteiden hallinta > Laiteyhteyksien hallinta ja muuta se sallituksi.</p>
        </details>
        <details><summary>Roku</summary>
          <p>Roku ei pyydä lupaa. Jos yhteys ei muodostu, mene Rokussa kohtaan Asetukset > Järjestelmä > Järjestelmän lisäasetukset > Ohjaus mobiilisovelluksilla ja jätä verkon käyttö tilaan Oletus tai Permissive (uudemmassa Roku-ohjelmistossa aseta Ohjaus mobiilisovelluksilla tilaan Käytössä).</p>
        </details>
        <details><summary>Android TV ja Google TV</summary>
          <p>Televisio näyttää 6-merkkisen koodin. Kirjoita se Mando TV:hen täsmälleen sellaisena kuin se näkyy. Se toimii Sonyn, Philipsin, TCL:n, Hisensen, Sharpin, Xiaomin, Chromecast with Google TV:n ja muiden Android TV -laitteiden kanssa.</p>
        </details>
      </div>

      <h2 id="encender">Television käynnistys sovelluksella</h2>
      <p>Mando TV käynnistää television kotiverkkosi kautta. Siihen tarvitaan kaksi asiaa: olet yhdistänyt vähintään kerran television ollessa päällä, ja televisiossa on käytössä käynnistys verkon kautta. Asetuksen nimi vaihtelee mallin mukaan; nämä ovat yleisimmät:</p>
      <div class="preguntas">
        <details><summary>LG</summary>
          <p>Etsi ”Käynnistä TV mobiililaitteella” (tai ”Käynnistä wifin kautta”) kohdasta Asetukset > Yleiset > Laitteet > Ulkoiset laitteet (vanhemmissa malleissa Yhteys > Mobiiliyhteyden hallinta) ja ota se käyttöön.</p>
        </details>
        <details><summary>Samsung</summary>
          <p>Ota käyttöön ”Käynnistä mobiililaitteella” kohdasta Asetukset > Yleiset > Verkko > Asiantuntija-asetukset.</p>
        </details>
        <details><summary>Roku</summary>
          <p>Ota Roku TV -laitteissa käyttöön ”TV:n pikakäynnistys” kohdasta Asetukset > Järjestelmä > Virta. Televisioon kytkettyjä Roku-soittimia ei voi käynnistää näin.</p>
        </details>
        <details><summary>Android TV ja Google TV</summary>
          <p>Se riippuu valmistajasta. Etsi verkko- tai virta-asetuksista kohtaa ”Wake on LAN”, ”Käynnistys verkon kautta”, ”Verkon valmiustila” tai ”Remote start”. Joissakin malleissa tätä asetusta ei ole.</p>
        </details>
      </div>

      <h2 id="falla">Jos jokin ei toimi</h2>
      <div class="preguntas">
        <details><summary>Yhteys katkeaa tai mikään ei reagoi</summary>
          <ol>
            <li>Napauta kaukosäädinnäytöllä Yhdistä uudelleen.</li>
            <li>Jos se ei auta, sulje Mando TV ja avaa sovellus uudelleen.</li>
            <li>Jos televisio on saanut uuden IP-osoitteen, poista se luettelosta ja lisää uudelleen.</li>
          </ol>
        </details>
        <details><summary>Näin lähetät meille virheraportin</summary>
          <ol>
            <li>Napauta Mando TV:ssä Mukauta-painiketta (säätimet ylhäällä).</li>
            <li>Napauta Kopioi testiraportti.</li>
            <li>Liitä se sähköpostiin osoitteeseen hola@mandotv.app yhdessä television merkin ja mallin kanssa.</li>
          </ol>
          <p>Raportti ei sisällä salasanoja, koodeja eikä mitään, mitä kirjoitat.</p>
        </details>
        <details><summary>Ostin Pron, eikä se näy</summary>
          <p>Napauta Mukauta-kohdassa Palauta osto samalla kauppatilillä, jolla ostit. Jos se ei vieläkään näy, kirjoita meille.</p>
        </details>
      </div>

      <h2 id="guias">Oppaat vaihe vaiheelta</h2>
      <p><a href="@@R_guias@@">Katso kaikki oppaat</a></p>
      <ul>
@@GUIAS@@
      </ul>

      <h2 id="contacto">Onko sinulla vielä kysyttävää?</h2>
      <p>Kirjoita meille osoitteeseen <a href="mailto:hola@mandotv.app?subject=Ohje%20Mando%20TV:hen">hola@mandotv.app</a>. Kerro television merkki ja malli sekä missä vaiheessa jäit jumiin. Kirjoita meille omalla kielelläsi. Vastaamme espanjaksi tai englanniksi ja halutessasi omalla kielelläsi käännöstyökalun avulla.</p>
'''

PRIVACIDAD = dict(
  titulo='Tietosuojaseloste | Mando TV',
  desc='Mando TV ei pyydä tiliä eikä henkilötietoja: ei mainoksia, ei seurantaa. Kaukosäädin puhuu suoraan televisiosi kanssa wifisi sisällä.',
  h1='Tietosuoja',
  intro='Lyhyesti: Mando TV ei pyydä tiliä eikä henkilötietoja. Ei ole mainoksia eikä seurantaa.',
)
PRIVACIDAD_HTML = '''      <p class="fecha">Voimassa 14. marraskuuta 2026 alkaen. Päivitetty viimeksi 28. marraskuuta 2026.</p>

      <h2>Keitä olemme</h2>
      <p>Mando TV on sovellus, jolla ohjaat televisiotasi puhelimellasi tai tietokoneellasi. Tässä selosteessa kerrotaan, mitä tietoja sovellus käyttää ja mitä se niillä tekee. Jos sinulla on kysyttävää, kirjoita meille osoitteeseen <a href="mailto:hola@mandotv.app">hola@mandotv.app</a>.</p>

      <h2>Mitä tietoja keräämme</h2>
      <p>Sovellus: vain se, mitä Androidin ja Windowsin ilmaiseen Pro-kokeilujaksoon tarvitaan, kuvattu kohdassa <a href="#prueba">Ilmainen Pro-kokeilujakso</a>. Sen lisäksi sovellus ei lähetä meille eikä kolmansille osapuolille tietoja sinusta tai siitä, miten käytät sitä. Se ei käytä analytiikka-, mainonta- tai seurantatyökaluja.</p>
      <p>Tämä verkkosivusto: mittaamme käyntejä kahdella tavalla, jotka selitetään kohdassa <a href="#cookies">Evästeet tällä verkkosivustolla</a>.</p>

      <h2>Mitä sovellus tallentaa laitteellesi</h2>
      <p>Toimiakseen sovellus tallentaa seuraavat tiedot vain puhelimeesi tai tietokoneellesi:</p>
      <ul>
        <li>Lisäämäsi televisiot: nimi, merkki, IP-osoite verkossasi ja verkon laiteosoite (MAC), jota käytetään käynnistykseen.</li>
        <li>Yhteysavaimet, jotka kukin televisio antaa, kun vahvistat luvan. Ne tallennetaan salattuina järjestelmän suojattuun tallennustilaan (iPhonen ja Macin avainnippu, Androidin Keystore, Windowsin suojattu tallennustila).</li>
        <li>Asetuksesi: vaalea tai tumma teema, taustaväri, värinä ja kaukosäätimen tyyppi.</li>
        <li>Jos käytät Pro-ominaisuuksia: suosikkisovelluksesi, rutiinisi ja viimeisimmät YouTube-hakusi (voit poistaa ne sovelluksessa).</li>
        <li>Jos käytät niitä: lapsitila (PIN-koodi tallennetaan vain suojattuna koodina) ja kaukosäätimet, jotka muut ovat jakaneet sinulle.</li>
      </ul>
      <p>Kun poistat sovelluksen, nämä tiedot poistuvat sen mukana, kahta poikkeusta lukuun ottamatta. Androidissa sovelluksen asetukset (kuten televisioluettelosi ja valintasi) voivat jäädä omaan Google-varmuuskopioosi, jos käytät Googlen varmuuskopiointia, ja palata, kun asennat sovelluksen uudelleen; yhteysavaimet eivät koskaan kuulu siihen. iPhonessa ja Macissa yhteysavaimet säilyvät järjestelmän avainnipussa ja voivat jäädä sinne sovelluksen poistamisen jälkeen.</p>

      <h2>Kenen kanssa sovellus puhuu</h2>
      <p>Televisioidesi kanssa, kotisi wifin sisällä. Löytääkseen ne sovellus hakee paikallisesta verkostasi; siksi se pyytää iPhonella ”Lähiverkko”-lupaa. Teksti, jonka kirjoitat sovelluksen näppäimistöllä, menee suoraan televisioon eikä sitä tallenneta.</p>
      <p>Lisäksi sovellus lataa avattaessa pienen julkisen tiedoston tältä verkkosivustolta (mandotv.app/app/config.json) saadakseen selville, onko olemassa uusi versio, jonka kannattaa asentaa, ja mitkä ominaisuudet kuuluvat Mando TV Pro -versioon. Se on lataus kuten sivun avaaminen: sovellus ei lähetä tietojasi, televisioitasi eikä sitä, mitä teet. Se ilmoittaa vain sovelluksen version ja järjestelmän (esimerkiksi Android), jotta se voi näyttää sinulle oikean ilmoituksen. Jos sinulla ei ole internetiä, sovellus jatkaa viimeksi ladatulla tiedostolla; jos kuluu yli 30 päivää ilman, että tiedostoa on voitu ladata, sovellus pyytää sinua yhdistämään hetkeksi internetiin. Kuten minkä tahansa verkkosivun käynnissä, myös sivustomme palveluntarjoaja (Cloudflare) näkee IP-osoitteesi tämän lataamisen yhteydessä.</p>

      <p>Kun lähetät valokuvia tai videoita televisioon (Pro-ominaisuus), televisio lataa vain valitsemasi tiedostot suoraan puhelimestasi tai tietokoneeltasi kotisi wifin kautta. Ne eivät kulje internetin eivätkä meidän kauttamme, sovellus ei näe muita kuviasi, ja jako päättyy heti, kun suljet tämän näytön. Kotiverkossasi tämä siirto ei ole salattu.</p>
      <p>Jos käytät toimintoa ”Näytä näyttöni TV:ssä” (Pro-toiminto), sovellus tallentaa näyttösi vain peilauksen ajan, koodaa sen laitteellasi ja lähettää sen kodin wifi-verkossa suoraan valitsemaasi televisioon. Se ei kulje internetin eikä meidän kauttamme, mitään ei tallenneta eikä säilytetä, ja peilaus päättyy, kun lopetat sen tai suljet sovelluksen. Televisio näyttää kaiken, mitä näytöllä näkyy, myös ilmoitukset, ja kotiverkossasi lähetys ei ole salattu.</p>
      <h2 id="prueba">Ilmainen Pro-kokeilujakso (Android ja Windows)</h2>
      <p>Jotta ilmainen Pro-kokeilujakso on vain yksi laitetta kohden, sovellus lähettää kokeilun alkaessa kerran palvelimellemme (api.mandotv.app, Cloudflaressa) kaksi asiaa: salatun sormenjäljen tunnisteesta, jonka järjestelmä antaa sovellukselle kyseisellä laitteella (Androidilla sovelluksen oma Android-tunniste, Windowsissa laitetunniste sovelluksillemme), sekä sen, kuinka kauan kokeilujaksosi on kestänyt. Sormenjälki ei paljasta, mikä laite on kyseessä tai kuka olet, ja palvelin salaa sen vielä kerran omalla avaimellaan ennen tallennusta.</p>
      <p>Tallennamme vain tuon sormenjäljen, kokeilun alkamispäivän ja sen, onko kyseessä Android vai Windows. IP-osoitettasi emme tallenna (Cloudflare näkee sen vastatessaan, kuten missä tahansa yhteydessä). Käytämme tietoa vain siihen, ettei sovelluksen uudelleenasennus anna uutta kokeilujaksoa, eli väärinkäytösten ehkäisyyn, mikä on oikeutettu etumme; emme koskaan mainontaan tai sinun seuraamiseesi, emmekä jaa sitä kenellekään. Jokainen tietue poistuu automaattisesti 24 kuukauden kuluttua. Jos sinulla ei ole internetiä, kokeilujakso toimii silti. iPhonella ja Macilla ei lähetetä mitään: kokeilujaksosta huolehtii App Store.</p>

      <h2>Mikrofoni ja ääni</h2>
      <p>iPhonella, Macilla ja Androidilla äänihaku käyttää mikrofonia vain, kun napautat puhepainiketta. Se, mitä sanot, muunnetaan tekstiksi järjestelmäsi puheentunnistuksella: Applen iPhonella ja Macilla ja Googlen Androidilla, kummankin omien tietosuojaehtojen mukaan. Windowsissa puhe tunnistetaan omalla tietokoneellasi eikä poistu sieltä. Vain jos laitteen oma tunnistusmoottori ei käynnisty tai epäonnistuu jatkuvasti (esimerkiksi vanhan suorittimen tai puuttuvan puhemallin vuoksi), sovellus käyttää Windowsin puhesyöttöä, Microsoftin, joka toimii verkossa, jos olet ottanut Windowsissa käyttöön verkossa toimivan puheentunnistuksen, Microsoftin tietosuojaehtojen mukaan. Windowsissa mikrofoni avautuu, kun avaat ääniruudun, ja sulkeutuu, kun suljet sen tai kun sitä ei ole käytetty 30 sekuntiin; kun et puhu, mitään ei tallenneta eikä säilytetä. Mando TV ei tallenna ääntä eikä säilytä sitä, ja syntynyt teksti menee suoraan televisioosi, aivan kuten se, mitä kirjoitat näppäimistöllä.</p>

      <h2>Koti: Apple Homen ja Google Homen laitteet</h2>
      <p>Kun avaat Koti-osion (testivaiheessa), sovellus pyytää lupaa nähdä laitteet, jotka sinulla jo on Applen Koti-sovelluksessa (HomeKit) tai Google Homessa. Tällä luvalla se lukee niiden nimen, huoneen ja tilan (päällä vai pois, kirkkaus, lämpötila tai missä vaiheessa kodinkoneen ohjelma on), näyttääkseen ne ja lähettääkseen niille sen, mitä napautat. Kaikki tapahtuu puhelimesi ja Applen tai Googlen järjestelmän välillä: Mando TV ei tallenna tätä luetteloa, ei lähetä sitä meille eikä kolmansille osapuolille eikä käytä sitä mainontaan tai analytiikkaan. Androidilla Google Home toimii omalla Google-tililläsi Googlen tietosuojaselosteen mukaan. Voit peruuttaa luvan milloin tahansa: iPhonella kohdassa Asetukset &gt; Tietosuoja ja turvallisuus &gt; HomeKit, Androidilla Google-tilisi asetuksissa.</p>
      <p>Kun napautat ”Miten Koti toimi sinulla?”, sähköpostisovelluksesi avautuu viestillä osoitteeseen hola@mandotv.app, joka sisältää teknisen yhteenvedon: sovelluksen version, järjestelmän sekä sen, kuinka monta kunkin tyyppistä laitetta ilmestyi ja reagoivatko ne. Laitteiden, huoneiden tai kotisi nimiä ei sisällytetä, ja viesti lähetetään vain, jos lähetät sen itse.</p>

      <h2>Jakamasi linkit ja tekstit</h2>
      <p>Kun jaat kaukosäätimen (linkki mandotv.app/m/), linkki sisältää kaukosäätimen ulkoasun ja vihjeen television löytämiseksi: sen nimen, merkin, mallin ja osoitteen verkossasi. Se ei koskaan sisällä yhteysavaimia, PIN-koodeja tai television laiteosoitetta. Tiedot kulkevat #-merkin jälkeen, joten ne eivät koskaan päädy palvelimillemme, mutta jokainen, jolle linkin lähetät, esimerkiksi WhatsAppilla, voi lukea ne. Jaettu rutiini (linkki mandotv.app/r/) sisältää vain nimen ja vaiheet.</p>
      <p>Varmuuskopioteksti, jonka voit kopioida sovelluksen asetuksista, sisältää suosikkisi, rutiinisi ja asetuksesi. Se ei ole salattu ja menee vain sinne, mihin sen liität.</p>

      <h2>Testiraportti</h2>
      <p>Sovelluksessa on painike ”Kopioi testiraportti”, joka auttaa meitä korjaamaan virheitä. Raportti pysyy vain sovelluksen muistissa sen ollessa auki, eikä sitä koskaan lähetetä itsestään: sinä päätät, kopioitko ja jaatko sen. Se ei sisällä yhteysavaimia, parinmuodostuskoodeja eikä mitään, mitä kirjoitat. Se sisältää sovelluksen tekemät vaiheet, kuten haun, yhdistämisen ja virheet, sekä teknisiä tietoja: sovelluksen version, järjestelmäsi sekä televisiosi merkin, mallin ja osoitteen verkossasi.</p>

      <h2 id="cookies">Evästeet tällä verkkosivustolla</h2>
      <p>Tämä koskee vain mandotv.app-verkkosivustoa, ei sovellusta.</p>
      <h3>Aina ilman evästeitä</h3>
      <p>Laskemme käynnit anonyymisti Cloudflare Web Analyticsilla: kuinka moni vierailee sivustolla, mitä sivuja luetaan ja mistä maasta. Se ei käytä evästeitä, ei käytä IP-osoitettasi tunnistamiseen eikä seuraa, mitä teet muilla verkkosivustoilla.</p>
      <h3>Evästeillä, vain jos hyväksyt</h3>
      <p>Jos napautat evästeilmoituksessa ”Hyväksy”, otamme käyttöön Google Analyticsin (Google LLC:n palvelu) ymmärtääksemme paremmin, miten sivustoa käytetään: sivunäytöt, käyntien kesto, laitetyyppi, likimääräinen kaupunki ja mistä tulet. Sitä varten se tallentaa selaimeesi evästeet _ga ja _ga_* enintään 2 vuodeksi. Google voi käsitellä näitä tietoja Chilen ulkopuolella sijaitsevilla palvelimilla. Olemme poistaneet käytöstä mainontatoiminnot ja Google Signalsin emmekä käytä näitä tietoja mainosten näyttämiseen.</p>
      <p>Jos napautat ”Hylkää” tai et valitse mitään, Google Analyticsia ei ladata eikä mitään evästettä tallenneta. Voit muuttaa valintasi milloin tahansa jokaisen sivun lopussa olevalla ”Evästeet”-painikkeella; jos peruutat suostumuksesi, poistamme nämä evästeet.</p>
      <p>Valintasi tallennetaan selaimeesi (paikallinen tallennustila, ei lähetetä kenellekään), jotta emme kysy sinulta uudelleen. Samaan tallennustilaan tallentuu myös sivun alareunasta valitsemasi kieli, jotta sivusto aukeaa seuraavalla kerralla sillä kielellä. Näyttääkseen maasi Pro-hinnan jokainen sivu kysyy Cloudflarelta, joka jo palvelee tätä sivustoa, mistä maasta vierailet, tai käyttää selaimesi kielen aluetta; vastausta ei tallenneta.</p>

      <h2>Ostokset</h2>
      <p>Kun ostat Mando TV Pron, maksun käsittelee sovelluskauppa (App Store, Google Play tai Microsoft Store). Emme saa emmekä tallenna korttitietojasi. Kauppa vahvistaa sovellukselle vain sen, että osto on olemassa.</p>

      <h2>Sähköpostit, joita lähetät meille</h2>
      <p>Kun kirjoitat meille osoitteeseen <a href="mailto:hola@mandotv.app">hola@mandotv.app</a>, käytämme sähköpostiosoitettasi ja kertomaasi vain vastataksemme sinulle. Emme jaa niitä emmekä käytä niitä mainontaan. Voit milloin tahansa vaatia, että poistamme viestisi.</p>

      <h2>Lapset</h2>
      <p>Sovellus ei kerää henkilötietoja keneltäkään, ei myöskään lapsilta.</p>

      <h2>Tämän selosteen muutokset</h2>
      <p>Jos sovelluksen tapa käsitellä tietojasi joskus muuttuu, päivitämme tämän sivun ja yllä olevan päivämäärän ennen kuin muutos tavoittaa sovelluksen.</p>
'''


# >>> guías traídas del inglés (ensamblar.py)
# Adaptadas con Ollama (qwen3.6:35b) desde las guías inglesas y auditadas por Opus el 22-nov. Rutas en idiomas_sitio.py.
GUIAS += [
  dict(clave='no-sub', corto='Kaukosäädinsovellus ilman tilausta', fecha='2026-11-23',
    titulo='Television kaukosäädinsovellus ilman tilausta ja mainoksia',
    desc='Kyllästynyt mainoksiin tai viikkotilauksiin kaukosäädinsovelluksissa? Mando TV on ilmainen ja mainokseton, Pro on valinnainen kertaosto. Rehellinen vertailu.',
    h1='Kaukosäädinsovellus ilman tilausta ja ilman mainoksia',
    intro='Moni yleiskaukosäädin näyttää mainoksia tai vaatii viikkotilauksen ennen kuin se toimii. Mando TV kulkee toista tietä: kaukosäädin on ilmainen, mainoksia ei ole eikä tiliä tarvita. Valinnaisen Pron ostat vain kerran. Tässä vertailu, myös siitä, mitä sovellus ei osaa.',
    pasos=[
      'Avaa ennen asennusta sovelluksen kauppasivu ja tarkista sovelluksen sisäiset ostokset. Viikko- tai kuukausihinnat viittaavat tilaukseen.',
      'Tarkista Google Playssa, lukeeko sivulla ”Sisältää mainoksia”, ja lue uusimmat arvostelut, joissa on vähän tähtiä: niissä paljastuu usein odottamattomia maksumuureja.',
      'Varmista, että sovellus voi ohjata televisiotasi wifin kautta. Mando TV toimii Samsungin (vuodesta 2016), LG webOS:n, Rokun, Google TV:n, Android TV:n ja Fire TV:n kanssa.',
      'Asenna Mando TV, yhdistä puhelimesi samaan wifiin kuin televisio ja napauta listassa televisiotasi.',
      'Vahvista televisiossa näkyvä kysymys tai kirjoita näytetty koodi. Painikkeet, äänenvoimakkuus, kanavat ja näppäimistö eivät maksa mitään.',
    ],
    tabla=dict(titulo='Mando TV verrattuna moniin kaukosäädinsovelluksiin',
      cabeza=['', 'Mando TV', 'Monet mainosrahoitteiset tai tilaussovellukset'],
      filas=[
        ['Perus-kaukosäädin', 'Ilmainen', 'Usein ilmainen mainoksilla tai piilotettu kokeilujakson taakse'],
        ['Mainokset', 'Ei ole', 'Yleisiä'],
        ['Tilaus', 'Ei ole. Pro on valinnainen kertaosto', 'Viikko- tai kuukausisuunnitelmat ovat tavallisia'],
        ['Tili', 'Ei tarvita', 'Vaihtelee'],
        ['Älytelevisiot wifin kautta', 'Samsung (vuodesta 2016), LG webOS, Roku, Google TV, Android TV, Fire TV, Apple TV (beta)', 'Sovelluksesta riippuen'],
        ['Infrapuna vanhemmille televisioille', 'Ilmainen Android-puhelimilla, joissa on infrapunalähetin (uutta)', 'Joissakin sovelluksissa, vain infrapunalähettimellä varustetuilla puhelimilla'],
        ['Bluetooth', 'Beta Android 9:stä alkaen, ilmainen', 'Sovelluksesta riippuen'],
        ['Kuvat ja videot televisioon', 'Pro, wifin kautta (ei peilausta)', 'Sovelluksesta riippuen'],
        ['Puhelimet ja tietokoneet', 'iPhone, iPad, Mac ja Windows, lisäksi Android ennakkokäytössä', 'Vaihtelee'],
        ['Näytön peilaus', 'Ilmainen iPhonella, iPadilla ja Windowsissa kunkin omalla sisäänrakennetulla toiminnolla. Windowsissa Pro voi lisäksi peilata tietokoneen näytön LG:n, Samsungin, Hisensen ja Android TV:n televisioihin (beta)', 'Joissakin sovelluksissa'],
      ],
      nota='Mando TV:tä ei verrata mihinkään tiettyyn sovellukseen. Ajankohtaiset hinnat näkyvät kunkin sovelluksen kauppasivulla.'),
    extra=[
      ('Mitä Mando TV ei tee', 'iPhonella ja iPadilla se ohjaa sinut Ohjauskeskuksen näytön peilaukseen, joka on iPhonen oma toiminto ja toimii televisioilla, joissa on AirPlay. Windowsissa se avaa Lähetä-toiminnon (Windows + K), ja Mando TV Pro voi lähettää tietokoneen näytön wifisi kautta LG:n, Samsungin, Hisensen ja Android TV:n televisioihin (beta, muutaman sekunnin viiveellä ja ilman ääntä). Mando TV Prolla se voi lisäksi lähettää kuvia ja videoita televisioon wifisi kautta. Se ohjaa älytelevisioita kotiwifin kautta. Televisioita, jotka eivät ole älytelevisioita, voi ohjata Android-puhelimella, jossa on infrapunalähetin, infrapunalla. Android 9:stä alkaen puhelin voi myös yhdistyä Bluetoothilla näppäimistönä ja kaukosäätimenä Google TV:hen, Android TV:hen ja Fire TV:hen kokonaan ilman wifiä. Tämä vaihtoehto on betassa ja ilmainen.'),
      ('Miten Mando TV ansaitsee rahaa', 'Ei mainoksilla eikä tiedoillasi: sovelluksessa ei ole mainoksia, eikä se seuraa sinua. Mando TV rahoitetaan Prolla, valinnaisella kertaostolla lisäominaisuuksiin. Perus-kaukosäädin on ilmainen.'),
      ('Laitteilla, jotka sinulla jo on', 'iPhone, iPad ja Mac App Storesta, Windows-tietokoneet Microsoft Storesta ja Android ilmaisella ennakkokäytöllä Google Playssa. Katso [Kaukosäädinsovellus iPhonelle](@iphone) ja [Kaukosäädinsovellus Windowsille](@windows).'),
      ('Tietosuoja', 'Ei tiliä eikä seurantaa sovelluksessa. Yhteys televisioon tapahtuu vain paikallisessa verkossa, ja yhteystiedot pysyvät laitteellasi salattuina. Lisätietoja [tietosuojaselosteessa](@privacidad).'),
    ],
    marca=None,
    faq=[
      ('Onko olemassa kaukosäädinsovellusta ilman tilausta?', 'On. Mando TV:ssä ei ole tilausta lainkaan: kaukosäädin on ilmainen ja mainokseton, Pro on valinnainen kertaosto.'),
      ('Onko Mando TV todella ilmainen?', 'On. Nuolipainikkeet, OK, Takaisin, Koti, äänenvoimakkuus, kanavat, numerot, näppäimistö sekä käynnistys ja sammutus ovat ilmaisia, ilman mainoksia ja ilman aikarajaa.'),
      ('Toimiiko se ilman wifiä?', 'Enimmäkseen ei. Mando TV ohjaa älytelevisioita kotiwifisi kautta. Poikkeukset: infrapuna Android-puhelimilla, joissa on infrapunalähetin, joka toimii myös televisioilla, jotka eivät ole älytelevisioita tai joilla ei ole wifi-yhteyttä, ja Bluetooth, betassa Android 9:stä alkaen, Google TV:lle, Android TV:lle ja Fire TV:lle.'),
    ]),
  dict(clave='roku-app-alt', corto='Roku-sovelluksen vaihtoehto', fecha='2026-11-23',
    titulo='Roku-sovelluksen vaihtoehto: helppo Roku-kaukosäädin',
    desc='Vaihtoehto Roku-sovellukselle: Mando TV ohjaa Roku-televisioita ja -soittimia wifillä ilman tiliä ja mainoksia, sekä Samsungia, LG:tä ja Google TV:tä.',
    h1='Roku-sovelluksen vaihtoehto: yksi kaikille televisioille',
    intro='Virallinen Roku-sovellus osaa paljon: Channel Store, lähetys, yksityinen kuuntelu ja kaukosäädin. Jos etsit vain nopeaa kaukosäädintä tai kotonasi on myös Samsung-, LG- tai Google TV -televisio, Mando TV on helppo vaihtoehto, joka ohjaa Rokua wifisi kautta ilman tiliä.',
    pasos=[
      'Yhdistä puhelimesi ja Roku samaan wifiin.',
      'Lataa Mando TV ja avaa se. Roku-televisiosi tai Roku-soittimesi tulee listaan. Napauta sitä. Roku ei pyydä koodia.',
      'Käytä nuolipainikkeita, OK:ta, Takaisin-, Koti- ja äänenvoimakkuuspainiketta sekä näppäimistöä. Kirjoita hakusanat Roku-kanavissa puhelimen näppäimistöllä.',
      'Jos painikkeet eivät tee mitään, mene Rokussa kohtaan Asetukset > Järjestelmä > Järjestelmän lisäasetukset > Ohjaus mobiilisovelluksilla ja aseta verkon käytöksi Oletus tai Permissive (uudemmassa Roku-ohjelmistossa aseta Ohjaus mobiilisovelluksilla tilaan Käytössä).',
      'Valinnainen: ota Roku-televisiossa käyttöön ”TV:n pikakäynnistys” kohdasta Asetukset > Järjestelmä > Virta, jotta Mando TV voi käynnistää television.',
    ],
    extra=[
      ('Missä Mando TV sopii paremmin', 'Yksi sovellus useille televisioille: Roku, Samsung, LG ja Google TV tai Android TV. Ilman tiliä, ilman mainoksia. Se toimii myös Windows-tietokoneella, mikä on kätevää työpöydän ääressä. Nuolipainikkeet ja äänenvoimakkuus reagoivat nopeasti, ja näppäimistöllä kirjoitat hakusanat vaivatta.'),
      ('Missä virallinen Roku-sovellus on parempi', 'Pidä Roku-sovellus siihen, mitä se tarjoaa kaukosäätimen lisäksi, kuten kanavien selaamiseen ja lisäämiseen Roku Channel Storesta sekä sen omaan lähetykseen ja yksityiseen kuunteluun (ääni kuulokkeilla puhelimessa). Käytä molempia, jos haluat. Ne voivat toimia samassa puhelimessa.'),
      ('Roku TV -laitteet ja Roku-soittimet', 'Molemmat toimivat. Tähän kuuluvat TCL:n, Hisensen, Philipsin ja muiden Roku TV -mallit sekä Roku Express, Streaming Stick ja Ultra. Lisätietoja löydät [Roku-kaukosäädinsovelluksen sivulta](@roku).'),
      ('Jos Roku-sovellus ei enää toimi', 'Jos painikkeet eivät enää reagoi, Roku estää yleensä ohjauksen sovelluksilla. Opas [Roku-sovellus ei toimi](@roku-403) näyttää asetuksen, joka korjaa ongelman.'),
      ('Ilmainen ja Pro', 'Nuolipainikkeet, OK, Takaisin, Koti, äänenvoimakkuus, kanavat, numeronäppäimet, näppäimistö, sovellusten avaaminen, tulojen vaihto sekä käynnistys ja sammutus ovat ilmaisia, ilman mainoksia ja ilman tilausta. Kosketuslevy, puhekomennot, suosikkisovellukset, rutiinit ja uniajastin kuuluvat Mando TV Pro -versioon, joka on kertaosto ilman tilausta.'),
    ],
    marca='roku',
    faq=[
      ('Tarvitsenko Roku-tilin käyttääkseni Mando TV:tä?', 'Et. Mando TV puhuu Rokulle kotiverkkosi kautta eikä pyydä tiliä.'),
      ('Korvaako Mando TV Roku Mobile -sovelluksen kokonaan?', 'Kaukosäätimenä kyllä. Channel Storea, lähetystä ja yksityistä kuuntelua varten pidä virallinen Roku-sovellus.'),
      ('Toimiiko se Roku Expressini tai Streaming Stickini kanssa?', 'Kyllä. Kaikkia Roku-soittimia ja Roku TV -laitteita ohjataan samalla tavalla.'),
    ]),
  dict(clave='lg-thinq', corto='LG ThinQ -sovelluksen vaihtoehto', fecha='2026-11-23',
    titulo='LG ThinQ -sovelluksen vaihtoehto: LG-kaukosäädin ilman tiliä',
    desc='Etsitkö LG ThinQ -sovellukselle vaihtoehtoa vain kaukosäätimeksi? Mando TV ohjaa webOS-pohjaisia LG-televisioita wifin kautta, ilman LG-tiliä ja mainoksia.',
    h1='LG ThinQ -sovelluksen vaihtoehto LG-televisiollesi',
    intro='LG ThinQ on LG:n virallinen sovellus koko älykodille: kodinkoneille, televisiolle ja muulle. Jos haluat vain helpon kaukosäätimen LG-televisiollesi, Mando TV hoitaa juuri sen kotisi wifin kautta, ilman että sinun tarvitsee luoda LG-tiliä ja ilman mainoksia.',
    pasos=[
      'Yhdistä puhelimesi tai tietokoneesi (iPhone, Android tai Windows) ja LG-televisiosi samaan wifiin.',
      'Lataa Mando TV ja avaa se. LG-televisiosi tulee listaan itsestään. Napauta sitä.',
      'Televisioon tulee kysymys. Vahvista se kerran television kaukosäätimellä, näytön alla olevalla ohjaussauvalla tai Magic Remotella.',
      'Painikkeet, äänenvoimakkuus ja näppäimistö toimivat heti. Et tarvitse LG-tiliä etkä tarvitse rekisteröidä televisiota.',
      'Valinnainen: ota television asetuksissa käyttöön ”Käynnistä TV mobiililaitteella”, jotta voit käynnistää television myös puhelimella.',
    ],
    extra=[
      ('Mando TV vai LG ThinQ: kumpi mihinkin', 'Käytä ThinQ:ta, jos haluat hallita LG:n kodinkoneita, kuten pesukonetta, jääkaappia tai ilmastointilaitetta, tai tarvitset LG-tilin toimintoja. Käytä Mando TV:tä, jos haluat nopean ja helpon television kaukosäätimen, joka toimii samassa sovelluksessa myös Samsungille, Rokulle ja Google TV:lle. Moni pitää molemmat: ThinQ kodinkoneille, Mando TV televisiolle.'),
      ('Mitä Mando TV tekee LG-televisiossa', 'Se toimii webOS-pohjaisilla LG-älytelevisioilla eli useimmilla malleilla vuodesta 2014, mukaan lukien LED, NanoCell, QNED ja OLED. Se antaa sinulle nuolipainikkeet, OK:n, Takaisin-, Koti-, äänenvoimakkuus-, kanava-, mykistys- ja toistopainikkeet sekä näppäimistön kirjoittamiseen television haussa ja useimmissa sovelluksissa. Sovellusluettelo ja tuloluettelo ovat myös ilmaisia. Prolla saat lisäksi osoittimen kuten Magic Remotessa.'),
      ('Mitä Mando TV ei tee', 'Se ei ohjaa LG:n kodinkoneita, se ei käytä LG-tiliäsi eikä korvaa television LG-tilipalveluja. Se on kaukosäädin, ei älykodin keskus.'),
      ('Tietosuoja ja mainokset', 'Mando TV:ssä ei ole mainoksia eikä tiliä. Se puhuu televisiolle vain kotiverkkosi sisällä ja tallentaa yhteysavaimen salattuna laitteellesi. Kaikki ominaisuudet löydät sivulta [LG-kaukosäädinsovellus](@lg).'),
      ('Ilmainen ja Pro', 'Nuolipainikkeet, OK, Takaisin, Koti, äänenvoimakkuus, kanavat, numeronäppäimet, näppäimistö, sovellusten avaaminen, tulojen vaihto sekä käynnistys ja sammutus ovat ilmaisia, ilman mainoksia ja ilman tilausta. Kosketuslevy, puhekomennot, suosikkisovellukset, rutiinit ja uniajastin kuuluvat Mando TV Pro -versioon, joka on kertaosto ilman tilausta.'),
    ],
    marca='lg',
    faq=[
      ('Voinko ohjata LG-televisiotani ilman LG ThinQ -sovellusta?', 'Voit. Mando TV yhdistää suoraan wifisi kautta webOS-pohjaisiin LG-televisioihin. Hyväksyt kysymyksen kerran televisiossa, ja sillä selvä, ilman LG-tiliä.'),
      ('Toimiiko Mando TV LG Magic Remoten osoittimen kanssa?', 'Mando TV Prossa on osoitin, jota liikutat sormella puhelimen näytöllä, samaan tapaan kuin Magic Remote liikuttaa nuolta.'),
      ('Onko Mando TV LG:n tekemä?', 'Ei. Mando TV on riippumaton sovellus eikä ole yhteydessä LG:hen. LG ja ThinQ kuuluvat omistajilleen, ja ne mainitaan vain yhteensopivuuden kuvaamiseksi.'),
    ]),
  dict(clave='smartthings', corto='SmartThingsin vaihtoehto', fecha='2026-11-23',
    titulo='SmartThings ei toimi? Helppo vaihtoehto Samsungille',
    desc='SmartThings hidas tai rikki? Mando TV ohjaa Tizen-pohjaisia Samsung-televisioita suoraan wifillä. Ei Samsung-tiliä, ei mainoksia. Askel askeleelta.',
    h1='SmartThingsin vaihtoehto Samsung-televisioille',
    intro='SmartThings on Samsungin sovellus koko älykodille, ja sen kaukosäädin kulkee Samsung-tilisi kautta. Jos se ei enää toimi tai etsit nopeaa ratkaisua, Mando TV ohjaa Tizen-pohjaisia Samsung-televisioita, valmistusvuosi 2016 tai uudempi, suoraan wifisi kautta ilman tiliä.',
    pasos=[
      'Yhdistä puhelimesi ja Samsung-televisio samaan wifiin.',
      'Lataa Mando TV ja avaa sovellus. Samsung-televisiosi tulee listaan itsestään. Napauta sitä.',
      'Televisio kysyy, haluatko sallia yhteyden. Valitse ”Salli” kaukosäätimellä tai television painikkeella (vain ensimmäisellä kerralla).',
      'Käytä heti nuolipainikkeita, OK:ta, Takaisin-, Koti- ja äänenvoimakkuuspainiketta, kanavia ja näppäimistöä.',
      'Valinnainen: ota käyttöön ”Käynnistä mobiililaitteella” kohdasta Asetukset > Yleiset > Verkko > Asiantuntija-asetukset, jotta Mando TV voi myös käynnistää television.',
    ],
    extra=[
      ('Miksi puhelinkaukosäädin ei enää toimi', 'Syyt ovat yleensä yksinkertaisia: puhelin ja televisio ovat eri wifeissä, VPN on päällä tai televisio on syvässä valmiustilassa. SmartThingsissä ongelmia voi aiheuttaa lisäksi Samsung-tili, esimerkiksi jos sinut on kirjattu ulos. Mando TV puhuu suoraan televisiolle kotiverkossa, eikä kirjauduttavaa tiliä ole. Lisää vinkkejä löydät oppaasta [Puhelimesi ei löydä televisiota](@not-found).'),
      ('Mando TV vai SmartThings: kumpi mihinkin', 'Pidä SmartThings, jos käytät sitä Samsungin kodinkoneisiin, lamppuihin tai muihin älykodin laitteisiin tai Samsung-tilisi toimintoihin. Käytä Mando TV:tä, jos haluat vain nopean television kaukosäätimen tai kotonasi on myös LG-, Roku-, Google TV- tai Fire TV -laite: yksi sovellus ohjaa kaikkia. Molemmat sovellukset voivat olla asennettuina samaan puhelimeen.'),
      ('Jos kieltäydyit luvasta vahingossa', 'Mene televisiossa kohtaan Asetukset > Yleiset > Ulkoisten laitteiden hallinta > Laiteyhteyksien hallinta ja aseta Mando TV sallituksi.'),
      ('Ei kaukosäädintä?', 'Voit vahvistaa kysymyksen television omalla painikkeella. Opas [Samsung-televisio ilman alkuperäistä kaukosäädintä](@samsung-lost) näyttää, miten.'),
      ('Ilmainen ja Pro', 'Kaukosäätimen voi ladata ja sitä voi käyttää ilmaiseksi, ilman mainoksia ja ilman tilausta. Mando TV Pro on valinnainen kertaosto lisäominaisuuksiin.'),
    ],
    marca='samsung',
    faq=[
      ('Voinko ohjata Samsung-televisiotani ilman SmartThingsiä?', 'Voit. Mando TV yhdistää suoraan wifisi kautta Tizen-pohjaisiin Samsung-televisioihin. Sallit yhteyden kerran televisiossa, ilman Samsung-tiliä.'),
      ('Ohjaako Mando TV myös Samsungin kodinkoneita?', 'Ei. Se on vain television kaukosäädin. Kodinkoneisiin ja muihin älykodin laitteisiin pidät SmartThingsin.'),
      ('Onko Mando TV Samsungin tekemä?', 'Ei. Mando TV on riippumaton sovellus eikä ole yhteydessä Samsungiin. Samsung ja SmartThings kuuluvat omistajilleen, ja ne mainitaan vain yhteensopivuuden kuvaamiseksi.'),
    ]),
  dict(clave='googletv-alt', corto='Google TV -kaukosäätimen vaihtoehto', fecha='2026-11-23',
    titulo='Google TV -kaukosäädin ei toimi? Vaihtoehto',
    desc='Eikö Google TV:n puhelinkaukosäädin löydä televisiota? Mando TV ohjaa Google TV:tä ja Android TV:tä wifin kautta, ilman Google-tiliä ja mainoksia.',
    h1='Google TV -kaukosäätimen vaihtoehto puhelimelle',
    intro='Google TV:n ja Android TV:n puhelinkaukosäädin on Googlen oman sovelluksen sisällä ja sidottu Google-tiliisi. Jos se ei löydä televisiota, et pääse eteenpäin. Mando TV on erillinen kaukosäädinsovellus, joka tekee pariliitoksen näytön 6-merkkisellä koodilla ja toimii ilman Google-tiliä, iPhonella, Android-puhelimella tai Windows-tietokoneella.',
    pasos=[
      'Käynnistä televisio ja yhdistä puhelimesi samaan wifiin.',
      'Lataa Mando TV ja avaa sovellus. Napauta listassa Google TV- tai Android TV -televisiotasi.',
      'Televisio näyttää 6-merkkisen koodin. Kirjoita se Mando TV:hen ja napauta Muodosta pariliitos.',
      'Käytä nuolipainikkeita, OK:ta, Takaisin-, Koti- ja äänenvoimakkuuspainiketta sekä näppäimistöä. Sinun ei tarvitse kirjautua mihinkään.',
      'Valinnainen: etsi television asetuksista Wake on LAN tai ”Käynnistys verkon kautta”, jotta sovellus voi myös käynnistää television.',
    ],
    extra=[
      ('Miksi puhelinkaukosäädin ei enää löydä televisiota', 'Useimmiten syy on verkossa: puhelin ja televisio ovat eri wifeissä, VPN on päällä tai vierasverkko erottaa laitteet. Korjaa se ensin, sillä se vaikuttaa kaikkiin kaukosäädinsovelluksiin. Lisää oppaassa [Puhelimesi ei löydä televisiota](@not-found).'),
      ('Millä televisioilla se toimii', 'Google TV- ja Android TV -televisiot merkeiltä Sony, TCL, Hisense, Philips, Sharp, Xiaomi, Toshiba ja muut sekä Chromecast with Google TV, Google TV Streamer ja Nvidia Shield. Kaikki yhdistetään samalla tavalla, kerran näytön koodilla.'),
      ('Missä Googlen sovellus on parempi', 'Googlen sovellus auttaa myös löytämään katsottavaa ja muistaa katselulistasi. Pidä se siihen. Mando TV on vain kaukosäädin, ja se ohjaa lisäksi Samsung-, LG-, Roku- ja Fire TV -laitteita samasta sovelluksesta sekä Windows-tietokoneelta.'),
      ('Jos vanha Android TV -kaukosäädinsovellus puuttuu', 'Google on siirtänyt puhelinkaukosäätimen vanhasta Android TV Remote Control -sovelluksesta Google TV -sovellukseen. Jos etsit itsenäistä kaukosäädintä, Mando TV on yksi vaihtoehto.'),
      ('Ilmainen ja Pro', 'Kaukosäätimen voi ladata ja sitä voi käyttää ilmaiseksi, ilman mainoksia ja ilman tilausta. Mando TV Pro on valinnainen kertaosto lisäominaisuuksiin.'),
    ],
    marca='android',
    faq=[
      ('Tarvitsenko Google-tilin käyttääkseni Mando TV:tä Google TV:n kanssa?', 'Et. Television koodi riittää pariliitokseen.'),
      ('Toimiiko se Chromecast with Google TV:n kanssa?', 'Kyllä. Pariliitos tehdään samalla tavalla, näytön 6-merkkisellä koodilla.'),
      ('Voinko käyttää sitä iPhonelta?', 'Kyllä. Mando TV on saatavilla App Storessa iPhonelle ja iPadille, Microsoft Storessa Windowsille ja ilmaisessa ennakkokäytössä Google Playssa Androidille.'),
    ]),
  dict(clave='windows', corto='Kaukosäädin Windows-tietokoneelle', fecha='2026-11-23',
    titulo='Kaukosäädinsovellus Windowsille: ohjaa televisiota tietokoneella',
    desc='Ohjaa Samsungia, LG:tä, Rokua, Google TV:tä tai Fire TV:tä Windows-tietokoneelta Mando TV:llä: pikanäppäimet, pieni kaukosäädin ja wifi. Microsoft Storessa.',
    h1='Kaukosäädinsovellus Windows-tietokoneelle',
    intro='Mando TV:llä on Windows-sovellus, joka muuttaa tietokoneesi tai kannettavasi kotiverkon kautta television kaukosäätimeksi. Kirjoita televisioon oikealla näppäimistölläsi, pidä pieni kaukosäädinikkuna päällimmäisenä työskennellessäsi ja ohjaa Samsungia, LG:tä, Rokua, Google TV:tä tai Fire TV:tä samalla sovelluksella.',
    pasos=[
      'Asenna Mando TV ilmaiseksi Microsoft Storesta Windows 10- tai 11-tietokoneelle.',
      'Varmista, että tietokone ja televisio ovat samassa verkossa, wifillä tai kaapelilla samaan reitittimeen.',
      'Avaa Mando TV. Televisio tulee listaan. Napsauta sitä.',
      'Vahvista kysymys televisiossa, jos se kysyy (LG, Samsung), tai kirjoita näytetty koodi (Google TV, Fire TV).',
      'Napsauta painikkeita tai kirjoita haku näppäimistölläsi. Valmis.',
    ],
    extra=[
      ('Pikanäppäimet (Pro)', 'Prolla tietokoneen näppäimistöstä tulee kaukosäädin: nuolinäppäimet liikkumiseen, Enter OK:ksi, askelpalautin tai Esc Takaisin-painikkeeksi, plus ja miinus äänenvoimakkuuteen, M mykistykseen ja välilyönti taukoon.'),
      ('Pieni kaukosäädin (Pro)', 'Pieni kaukosäädinikkuna, joka pysyy kaikkien muiden ikkunoiden päällä. Näin muutat äänenvoimakkuutta tai pysäytät katkaisematta työtäsi.'),
      ('Kirjoittaminen televisioon tietokoneelta', 'Television näyttönäppäimistö on hidas. Mando TV:ssä kirjoitat oikealla näppäimistölläsi ja teksti päätyy television hakukenttään. Tämä osa on ilmainen.'),
      ('Lisätietoja', 'Vaihe vaiheelta -ohjeen löydät oppaasta [Television ohjaus tietokoneella](@pc). Puhelinta varten lue [Puhelin kaukosäätimenä wifin kautta](@wifi).'),
      ('Ilmainen ja Pro', 'Nuolipainikkeet, OK, Takaisin, Koti, äänenvoimakkuus, kanavat, numeronäppäimet, näppäimistö, sovellusten avaaminen, tulojen vaihto sekä käynnistys ja sammutus ovat ilmaisia, ilman mainoksia ja ilman tilausta. Kosketuslevy, puhekomennot, suosikkisovellukset, rutiinit ja uniajastin kuuluvat Mando TV Pro -versioon, joka on kertaosto ilman tilausta. Windowsissa ostat Pron Microsoft Storen kautta.'),
      ('Puhekomennot tietokoneelta (Pro)', 'Prolla voit puhua televisiolle tietokoneen mikrofonilla. Puhe tunnistetaan suoraan tietokoneella: siihen et tarvitse internetiä etkä tarvitse muuttaa mitään Windowsissa. Se, mitä sanot, ei koskaan poistu tietokoneelta eikä sitä tallenneta. Vain hyvin vanhoilla suorittimilla sovellus turvautuu Windowsin puhesyöttöön. Silloin verkkopohjaisen puheentunnistuksen on oltava päällä tietosuoja-asetuksissa ja kielesi lisättynä Windowsiin.'),
    ],
    marca=None,
    faq=[
      ('Tarvitseeko Windowsin kaukosäädinsovellus Bluetoothin tai kaapelin?', 'Ei. Se käyttää kotiverkkoasi. Tietokoneen ja television tarvitsee vain olla kytkettyinä samaan reitittimeen.'),
      ('Mitä televisioita voin ohjata Windowsista?', 'Tizen-pohjaiset Samsung-televisiot, webOS-pohjaiset LG-televisiot, Roku TV ja soittimet, Google TV ja Android TV sekä Fire TV.'),
      ('Voinko nähdä television kuvan tietokoneella tai kuunnella sen tietokoneen kaiuttimista?', 'Et. Mando TV on vain kaukosäädin. Se ei peilaa eikä suoratoista television kuvaa tietokoneelle.'),
      ('Miksi puhe ei toimi Windows-tietokoneellani?', 'Puheohjaus on Pro-ominaisuus. Tarkista siis, että Pro on käytössä ja tietokoneen mikrofoni toimii. Useimmilla tietokoneilla puhe tunnistetaan suoraan tietokoneella, ilman internetiä. Vain hyvin vanhoilla suorittimilla sovellus käyttää Windowsin puhesyöttöä: silloin ota verkkopohjainen puheentunnistus käyttöön Windowsin tietosuoja-asetuksissa ja lisää kielesi kieliasetuksiin.'),
    ]),
  dict(clave='iphone', corto='Kaukosäädinsovellus iPhonelle', fecha='2026-11-23',
    titulo='Kaukosäädinsovellus iPhonelle: Samsung, LG, Roku, Google TV',
    desc='Käytä iPhoneasi kaukosäätimenä Samsungille, LG:lle, Rokulle, Google TV:lle ja Fire TV:lle wifin kautta. Ilmainen App Storessa, ilman tiliä ja mainoksia.',
    h1='Kaukosäädinsovellus iPhonelle: yksi kaikille televisioille',
    intro='Mando TV muuttaa iPhonesi tai iPadisi kaukosäätimeksi Samsungille, LG:lle, Rokulle, Google TV:lle tai Android TV:lle sekä Fire TV:lle kotisi wifin kautta. Sovellus on ilmainen App Storessa, ilman tiliä ja ilman mainoksia. Se toimii myös Androidilla ja Windowsilla.',
    pasos=[
      'Lataa Mando TV ilmaiseksi App Storesta.',
      'Yhdistä iPhonesi ja televisio samaan wifiin.',
      'Avaa Mando TV ja napauta Salli, kun iOS kysyy lupaa lähiverkon käyttöön. Sovellus tarvitsee sen löytääkseen television.',
      'Napauta listassa televisiotasi. Vahvista televisiossa näkyvä kysymys, jos se kysyy (LG ja Samsung), tai kirjoita television näyttämä koodi (Google TV tai Fire TV).',
      'Käytä painikkeita, äänenvoimakkuutta ja näppäimistöä. Olet yhdistetty.',
    ],
    extra=[
      ('Toimii näillä televisioilla', 'LG webOS, Samsung Tizen (valmistusvuosi 2016 tai uudempi), Roku TV ja Roku-soittimet, Google TV ja Android TV sekä Fire TV. Merkkien sivut ovat [Samsung](@samsung), [LG](@lg), [Roku](@roku) ja [Android TV](@android).'),
      ('Miksi se kysyy lähiverkkoa', 'iPhone estää sovelluksia käyttämästä kotiverkkosi laitteita, ellet salli sitä. Jos televisio ei tule listaan, avaa Asetukset > Mando TV ja ota käyttöön ”Lähiverkko”. Sovellus puhuu vain televisiosi kanssa kotiverkkosi sisällä.'),
      ('Miksi Mando TV eikä valmistajan sovellus', 'Jokaisella televisiomerkillä on oma sovelluksensa, ja se haluaa oman määrityksensä tai tilinsä. Mando TV on yksi sovellus kaikille, ilman tiliä.'),
      ('Ilmainen ja Pro iPhonella', 'Nuolipainikkeet, OK, Takaisin, Koti, äänenvoimakkuus, kanavat, numeronäppäimet, näppäimistö, sovellusten avaaminen, tulojen vaihto sekä käynnistys ja sammutus ovat ilmaisia, ilman mainoksia ja ilman tilausta. Kosketuslevy, puhekomennot, suosikkisovellukset, rutiinit ja uniajastin kuuluvat Mando TV Pro -versioon, joka on kertaosto ilman tilausta. Ostat Pron kerran suoraan sovelluksessa.'),
    ],
    marca=None,
    faq=[
      ('Onko Mando TV ilmainen iPhonella?', 'Lataus on ilmainen, ilman mainoksia. Perus-kaukosäädin on ilmainen, samoin sovellusten avaaminen ja tulojen vaihto. Lisäominaisuudet, kuten kosketuslevy, puhekomennot ja rutiinit, kuuluvat Mando TV Pro -versioon, joka on kertaosto.'),
      ('Toimiiko se iPadilla?', 'Kyllä. Sama sovellus toimii iPhonella ja iPadilla.'),
      ('Tarvitseeko iPhonen kaukosäädinsovellus Bluetoothin tai infrapunalähettimen?', 'Ei iPhonella. iPhoneissa ei ole infrapunalähetintä, joten infrapunaohjaus ei ole siellä käytettävissä, ja Bluetooth-vaihtoehto on vain Android 9:lle tai uudemmalle, ei iPhonelle. iPhonella Mando TV ohjaa älytelevisioita sekä Apple TV:tä (beta) kotisi wifin kautta.'),
    ]),
  dict(clave='firetv', corto='Fire TV -kaukosäädin', fecha='2026-11-23',
    titulo='Fire TV -kaukosäädinsovellus puhelimelle ja tietokoneelle',
    desc='Fire TV -kaukosäädin puhelimessa: ohjaa Fire TV Stickiä, Cubea tai Fire TV -televisiota wifillä 4-numeroisella PIN-koodilla. Ilman Amazon-sovellusta.',
    h1='Fire TV -kaukosäädin puhelimelle tai tietokoneelle',
    intro='Jos Fire TV -kaukosäädin on hukassa tai paristot ovat tyhjät, Mando TV ohjaa Fire TV Stickiä, Fire TV Cubea tai televisiota, jossa on sisäänrakennettu Fire TV, wifin kautta. Pariliitos tehdään 4-numeroisella PIN-koodilla. Fire TV on uusi Mando TV:ssä, joten päivitä ensin sovellus.',
    pasos=[
      'Päivitä Mando TV uusimpaan versioon App Storesta, Microsoft Storesta tai Google Playsta.',
      'Käynnistä Fire TV ja yhdistä puhelimesi samaan wifiin.',
      'Avaa Mando TV. Fire TV tulee listaan. Napauta sitä.',
      'Television näytölle tulee 4-numeroinen PIN-koodi. Kirjoita se Mando TV:hen. Teet sen vain kerran.',
      'Käytä nuolipainikkeita, OK:ta, Takaisin-, Koti- ja toistopainikkeita sekä näppäimistöä hakuihin.',
    ],
    extra=[
      ('Tuetut Fire TV -laitteet', 'Fire TV Stick, Fire TV Stick 4K, Fire TV Cube ja televisiot, joissa on sisäänrakennettu Fire TV, kuten Amazon Fire TV Edition -televisiot ja jotkin Hisense-mallit. Tuki on uusi, ja olemme voineet testata toistaiseksi vain muutamaa oikeaa laitetta. Jos jokin ei toimi odotetusti, kerro mallisi meille Ohje-sivun kautta.'),
      ('Fire TV:n käynnistys', 'Mando TV ei käynnistä Fire TV:tä verkon kautta. Käynnistä televisio laitteen virtapainikkeella: kytketty Fire TV Stick tai Cube herää yleensä HDMI-CEC:n kautta, ja televisiossa, jossa on sisäänrakennettu Fire TV, televisio on Fire TV. Sen jälkeen ohjaat sitä puhelimesta.'),
      ('Jos Fire TV ei tule näkyviin', 'Varmista, että molemmat laitteet ovat samassa wifissä ja Fire TV on hereillä. Salli iPhonella Mando TV:lle ”Lähiverkko” asetuksissa. Katso [Puhelimesi ei löydä televisiota](@not-found).'),
      ('Ei lainkaan kaukosäädintä?', 'Fire TV:n on näytettävä PIN-koodi näytöllä, joten television ja Fire TV:n on oltava päällä ja näytettävä kuva. Jos televisio on väärässä tulossa, vaihda se television painikkeilla. Katso [Tulon vaihto ilman kaukosäädintä](@hdmi).'),
      ('Ilmainen ja Pro', 'Nuolipainikkeet, OK, Takaisin, Koti, äänenvoimakkuus, kanavat, numerot, näppäimistö, sovellusten avaaminen, tulojen vaihto sekä käynnistys ja sammutus ovat ilmaisia, ilman mainoksia ja ilman tilausta. Kosketuslevy, puhekomennot, suosikkisovellukset, rutiinit ja uniajastin kuuluvat Mando TV Pro -versioon, joka on kertaosto ilman tilausta.'),
    ],
    marca=None,
    faq=[
      ('Tarvitsenko Amazon Fire TV -sovelluksen?', 'Et. Mando TV yhdistää Fire TV:hen wifisi kautta PIN-koodilla. Et tarvitse Amazon-tiliä puhelimessa.'),
      ('Toimiiko se Fire TV -televisioiden ja Fire TV Stickien kanssa?', 'Kyllä, juuri sitä varten se on kehitetty. Tuki on uusi, pidä sovellus ajan tasalla ja kerro meille malleista, jotka eivät toimi odotetusti.'),
      ('Miksi tarvitsen PIN-koodin?', 'Fire TV näyttää 4-numeroisen PIN-koodin todistaakseen, että istut television edessä. Kukaan ei voi tehdä pariliitosta näkemättä näyttöä.'),
    ]),
  dict(clave='firetv-lost', corto='Fire TV -kaukosäädin hukassa', fecha='2026-11-23',
    titulo='Fire TV -kaukosäädin hukassa? Näin puhelimesi auttaa',
    desc='Fire TV Stickin kaukosäädin hukassa? Ohjaa sitä puhelimella wifin kautta, pariliitos 4-numeroisella PIN-koodilla. Vinkit uuteen wifiin ja HDMI-CEC:hen.',
    h1='Fire TV -kaukosäädin hukassa: näin käytät puhelintasi',
    intro='Jos Fire TV Stickin, Fire TV Cuben tai Fire TV -älytelevision kaukosäädin on hukassa tai ei enää toimi, puhelimesi ottaa ohjauksen, kunhan Fire TV on yhä yhdistetty wifiisi. Pariliitos tehdään näytön 4-numeroisella PIN-koodilla, joten vanhaa kaukosäädintä et tarvitse siihen koskaan.',
    pasos=[
      'Käynnistä televisio laitteen painikkeella. Kytketty Fire TV Stick tai Cube herää yleensä mukana; jos HDMI-CEC on käytössä, televisio vaihtaa usein itse sen tuloon.',
      'Jos televisio näyttää toista tuloa, vaihda se television tulo- tai lähdepainikkeella. Katso [Tulon vaihto ilman kaukosäädintä](@hdmi).',
      'Yhdistä puhelimesi samaan wifiin kuin Fire TV.',
      'Lataa Mando TV ja avaa sovellus. Fire TV tulee listaan. Napauta sitä.',
      'Televisio näyttää 4-numeroisen PIN-koodin. Kirjoita se Mando TV:hen. Teet sen vain kerran.',
      'Käytä puhelimesi nuolipainikkeita, OK:ta, Takaisin-, Koti-, äänenvoimakkuus- ja toistopainikkeita sekä näppäimistöä.',
    ],
    extra=[
      ('Kokeile ensin television kaukosäädintä (HDMI-CEC)', 'Monet television kaukosäätimet voivat ohjata Fire TV Stickiä HDMI-CEC:n kautta. Kun Fire TV:n käyttöliittymä on näkyvissä, paina television kaukosäätimen nuolia ja OK:ta. Jos mitään ei tapahdu, ota CEC käyttöön television asetuksissa (Anynet+ Samsungilla, SIMPLINK LG:llä, BRAVIA Sync Sonylla) ja Fire TV:ssä HDMI-CEC-laiteohjaus näyttöasetuksissa (”Näyttö ja äänet”).'),
      ('Jos olet vaihtanut wifin', 'Ilman kaukosäädintä et voi kirjoittaa uutta wifin salasanaa Fire TV:hen, mutta on keino: luo toisella puhelimella hotspot täsmälleen samalla nimellä ja salasanalla kuin vanhalla wifillä. Fire TV yhdistää siihen automaattisesti. Yhdistä Mando TV -puhelin tähän hotspotiin, tee pariliitos PIN-koodilla, mene sitten Fire TV:ssä kohtaan Asetukset > Verkko ja valitse uusi wifisi. Yhdistä lopuksi myös puhelimesi uuteen wifiin.'),
      ('Korvaavan kaukosäätimen pariliitos', 'Useimmat uudet Fire TV -kaukosäätimet liitetään pitämällä Koti-painiketta alhaalla noin 10 sekuntia Fire TV:n lähellä. Jos se ei onnistu, avaa Asetukset > Ohjaimet ja Bluetooth-laitteet > Amazon Fire TV -kaukosäätimet > Lisää uusi kaukosäädin. Tähän valikkoon pääset myös puhelimestasi Mando TV:llä.'),
      ('Television sisäänrakennettu Fire TV', 'Televisioissa, joissa on sisäänrakennettu Fire TV, kuten monissa Insignia- ja Toshiba-malleissa, samat vaiheet toimivat, koska televisio itse on Fire TV.'),
      ('Ennen kuin aloitat', 'Fire TV -tuki on uusi Mando TV:ssä. Päivitä sovellus ensin. Jos mallisi ei reagoi odotetusti, kirjoita meille [Ohje-sivun](@soporte) kautta ja kerro malli.'),
      ('Ilmainen ja Pro', 'Kaukosäätimen voi ladata ja sitä voi käyttää ilmaiseksi, ilman mainoksia ja ilman tilausta. Mando TV Pro on valinnainen kertaosto lisäominaisuuksiin.'),
    ],
    marca=('firetv', 'Fire TV -kaukosäädin'),
    faq=[
      ('Voinko ohjata Fire TV Stickiä puhelimella ilman kaukosäädintä?', 'Voit, kunhan Fire TV on päällä ja yhdistetty wifiisi. Mando TV tekee pariliitoksen television 4-numeroisella PIN-koodilla, joten vanhaa kaukosäädintä et tarvitse.'),
      ('Toimiiko se, jos Fire TV on uudessa wifissä?', 'Ei suoraan, koska puhelimen ja Fire TV:n on oltava samassa verkossa. Saa Fire TV ensin takaisin verkkoon tämän sivun hotspot-vinkillä.'),
      ('Tarvitsenko Amazon Fire TV -sovelluksen tai Amazon-tilin?', 'Et. Mando TV yhdistää kotiverkkosi kautta PIN-koodilla eikä vaadi omaa tiliä.'),
    ]),
  dict(clave='turn-on', corto='Television käynnistys ilman kaukosäädintä', fecha='2026-11-23',
    titulo='Television käynnistys ilman kaukosäädintä (kaikki merkit)',
    desc='Käynnistä televisio ilman kaukosäädintä: missä painike on Samsungissa, LG:ssä, TCL:ssä, Hisensessä ja Sonyssa. Lisäksi HDMI-CEC ja puhelinvinkit.',
    h1='Näin käynnistät television ilman kaukosäädintä',
    intro='Lähes jokaisessa televisiossa on yhä fyysinen virtapainike. Se vain on hyvin piilossa. Tässä näet, missä se on kullakin merkillä, sekä kaksi tapaa säästyä etsimiseltä seuraavalla kerralla: HDMI-CEC konsolista tai suoratoistolaitteesta ja television käynnistys puhelimellasi wifin kautta.',
    pasos=[
      'Katso näytön keskikohdan alle, heti merkin logon taakse. Monessa televisiossa siellä on pieni yksittäinen painike tai ohjaussauva, osoittaen alaspäin.',
      'Jos se ei ole siellä, tunnustele television takaosaa alakulmien läheltä, sitten vasenta ja oikeaa reunaa.',
      'Paina painiketta kerran. Monessa televisiossa, jossa on vain yksi painike, lyhyt painallus laitteen ollessa päällä avaa pienen tulo- ja äänenvoimakkuusvalikon, ja pitkä painallus sammuttaa sen.',
      'Edelleen ei mitään? Tarkista virtajohto molemmista päistä ja kokeile toista pistorasiaa. Jos valmiustilan merkkivalo ei pala, televisio ei saa virtaa.',
      'Kun televisio on päällä, määritä se niin, ettet tarvitse painiketta enää: ota käyttöön HDMI-CEC ja käynnistys verkon kautta, molemmat selitetään alempana.',
    ],
    extra=[
      ('Missä virtapainike on, merkin mukaan', 'Samsung: ohjauspainike tai ohjaussauva näytön keskikohdan alla tai takana alakulmassa. LG: ohjaussauvapainike LG-logon alla useimmissa malleissa. TCL ja Hisense: yleensä pieni painike näytön keskikohdan alla tai takana alakulman lähellä. Sony: takana tai sivureunassa, alhaalla lähellä reunaa. Vizio: takana alavasemmalla tai alaoikealla tai sivussa. Paikat vaihtelevat mallin mukaan. Jos et löydä sitä, etsi käyttöohje takana olevan tarran mallinumerolla.'),
      ('Television käynnistys konsolilla tai suoratoistolaitteella (HDMI-CEC)', 'Kun HDMI-CEC on käytössä, PlayStationin, Xboxin, Roku-soittimen, Fire TV Stickin tai Chromecastin käynnistäminen käynnistää myös television ja vaihtaa oikeaan tuloon. Jokainen merkki nimeää asetuksen eri tavalla: Anynet+ Samsungilla, SIMPLINK LG:llä, BRAVIA Sync Sonylla ja CEC useimmilla muilla. Lisää oppaassa [Television käynnistys ja konsolin HDMI-tuloon vaihto](@console).'),
      ('Television käynnistys puhelimella', 'Älytelevisiot voidaan herättää wifin kautta, kun sallit sen kerran, ja sitten Mando TV käynnistää ne puhelimestasi. Samsungilla ota käyttöön ”Käynnistä mobiililaitteella” kohdasta Asetukset > Yleiset > Verkko > Asiantuntija-asetukset. LG:llä ota käyttöön ”Käynnistä TV mobiililaitteella” ([vaihe vaiheelta](@lg-on)). Roku TV:ssä ota käyttöön ”TV:n pikakäynnistys” kohdasta Asetukset > Järjestelmä > Virta. Google TV:ssä ja Android TV:ssä etsi Wake on LAN tai ”Käynnistys verkon kautta”, jos mallissasi on se. Teet sen kerran, television ollessa päällä.'),
      ('Jos et löydä painiketta', 'Jotkin uudemmat televisiot piilottavat ainoan painikkeen niin hyvin, että tuntuu kuin sitä ei olisi. Etsi pientä kohoumaa tai valoanturin aluetta näytön alta: painike on usein heti sen vieressä. Wifin kautta Mando TV tarvitsee, että televisio on ollut kerran päällä ja yhdistetty. Infrapuna on poikkeus: Android-puhelimella, jossa on infrapunalähetin, Mando TV voi käynnistää television, jota ei ole koskaan määritetty, kunhan osoitat puhelimella televisiota. Infrapuna on uusi ja toimii sovelluksen koodiluettelon merkeillä.'),
      ('Ilmainen ja Pro', 'Kaukosäätimen voi ladata ja sitä voi käyttää ilmaiseksi, ilman mainoksia ja ilman tilausta. Mando TV Pro on valinnainen kertaosto lisäominaisuuksiin.'),
    ],
    marca=None,
    faq=[
      ('Voinko käynnistää television puhelimella, jos en ole koskaan määrittänyt sitä?', 'Et wifin kautta. Sammutettu televisio herää verkosta vain, jos käynnistys verkon kautta on otettu aiemmin käyttöön. Ensimmäisellä kerralla käytä television painiketta. Poikkeus on Android-puhelin, jossa on infrapunalähetin: Mando TV voi käynnistää television ilman määritystä infrapunalla, jos merkki on koodiluettelossa tai valitset ”Muu merkki tai en tiedä”.'),
      ('Miten käynnistän Samsung-television ilman kaukosäädintä?', 'Paina ohjauspainiketta näytön keskikohdan alla tai takana alakulmassa. Ota sitten käyttöön ”Käynnistä mobiililaitteella”, jotta puhelimesi voi käynnistää sen seuraavalla kerralla.'),
      ('Miten käynnistän Roku TV:n ilman kaukosäädintä?', 'Käytä television painiketta, yleensä keskikohdan alla tai takana. Ota sitten käyttöön ”TV:n pikakäynnistys” kohdasta Asetukset > Järjestelmä > Virta, jotta Mando TV voi käynnistää sen puhelimestasi.'),
      ('Miksi televisioni käynnistyy automaattisesti, kun käynnistän konsolin?', 'Se on HDMI-CEC. Se on kätevä, ja voit sammuttaa sen television asetuksista, jos haluat.'),
    ]),
  dict(clave='sony', corto='Sony-kaukosäädin', fecha='2026-11-23',
    titulo='Sony-kaukosäädinsovellus puhelimelle ja tietokoneelle',
    desc='Mando TV ohjaa Sony Bravia -televisioita, joissa on Google TV tai Android TV, wifin kautta. Betatuki vuosien 2013-2015 malleille ilman Androidia.',
    h1='Näin ohjaat Sony-televisiotasi puhelimella',
    intro='Uudemmat Sony Bravia -älytelevisiot käyttävät Google TV:tä, vanhemmat vuodesta 2015 alkaen Android TV:tä. Mando TV ohjaa molempia wifisi kautta iPhonelta, Android-puhelimelta tai Windows-tietokoneelta. Sovellus korvaa alkuperäisen kaukosäätimen, kun se on hukassa tai paristot ovat tyhjät.',
    pasos=[
      'Tarkista, näyttääkö Sony-televisiosi Google TV:n tai Android TV:n aloitusnäytön. Se pätee useimpiin Sony Bravia -älytelevisioihin valmistusvuodesta 2015 alkaen.',
      'Yhdistä puhelimesi ja televisio samaan wifiin.',
      'Avaa Mando TV ja napauta listassa Sony-televisiotasi.',
      'Kirjoita 6-merkkinen koodi, jonka televisio näyttää näytöllä (vain ensimmäisellä kerralla). Siihen et tarvitse kaukosäädintä.',
      'Käytä nuolipainikkeita, OK:ta, Takaisin-, Koti- ja äänenvoimakkuuspainiketta sekä näppäimistöä.',
    ],
    extra=[
      ('Sony-television käynnistys puhelimella', 'Sony-mallit, joissa on Google TV tai Android TV, voidaan herättää verkon kautta, kun ”Remote start” on otettu käyttöön. Asetuksen löydät yleensä kohdasta Asetukset > Verkko ja internet > Remote start (polku voi vaihdella hieman mallin mukaan). Napauta sitten Mando TV:ssä televisiota sen ollessa sammutettuna, ja sovellus käynnistää sen.'),
      ('Missä Sonyn virtapainike on', 'Useimmissa Bravia-televisioissa se on takana, alavasemman tai alaoikean kulman lähellä, tai sivureunassa. Lyhyt painallus käynnistää television. Lisää oppaassa [Television käynnistys ilman kaukosäädintä](@turn-on).'),
      ('Vanhemmat Sony-televisiot', 'Sony Bravia -televisioita vuosilta 2013-2015, jotka eivät käytä Androidia, tuetaan Mando TV:ssä betatilassa. Se on uutta ja siinä voi vielä olla rosoisia kohtia. Televisio näyttää 4-numeroisen PIN-koodin, jonka kirjoitat sovellukseen. Muita Sony-televisioita ilman Google TV:tä tai Android TV:tä ei tällä hetkellä tueta.'),
      ('Ilmainen ja Pro', 'Kaukosäätimen voi ladata ja sitä voi käyttää ilmaiseksi, ilman mainoksia ja ilman tilausta. Mando TV Pro on valinnainen kertaosto lisäominaisuuksiin.'),
    ],
    marca='android',
    faq=[
      ('Toimiiko Mando TV Sony Bravia -televisioiden kanssa?', 'Kyllä, Sony-televisioiden kanssa, joissa on Google TV tai Android TV. Se kattaa useimmat Sony-älytelevisiot valmistusvuodesta 2015 alkaen.'),
      ('Tarvitsenko Sony-sovelluksen tai Google-tilin?', 'Et. Mando TV tekee pariliitoksen television näytön koodilla eikä vaadi tiliä.'),
      ('Toimiiko se vanhempien Sony Bravia -televisioiden kanssa ilman Androidia?', 'Kyllä, betatilassa, vuosien 2013-2015 Bravia-malleilla ilman Androidia. Pariliitos tehdään televisiossa näytettävällä 4-numeroisella PIN-koodilla.'),
      ('Voinko kirjoittaa Sony-televisioon puhelimesta?', 'Kyllä. Puhelimen näppäimistö on ilmainen ja kirjoittaa television hakuun ja muihin tekstikenttiin. YouTubea varten Mando TV:ssä on myös YouTube-näppäimistö: kirjoita tai sano, mitä haluat katsoa, ja YouTube avautuu televisiossa tuloksineen. Netflix hyväksyy vain oman näytön näppäimistönsä, joten käytä siinä nuolia ja OK:ta.'),
    ]),
  dict(clave='tcl', corto='TCL-kaukosäädin', fecha='2026-11-23',
    titulo='TCL-kaukosäädinsovellus puhelimelle ja tietokoneelle',
    desc='TCL-kaukosäädin hukassa? Useimmat TCL-televisiot käyttävät Roku TV:tä tai Google TV:tä. Mando TV ohjaa molempia wifin kautta, ilman tiliä ja mainoksia.',
    h1='Näin ohjaat TCL-televisiotasi puhelimella',
    intro='TCL valmistaa television, mutta ohjelmisto on Roku TV tai Google TV (vanhemmissa malleissa Android TV). Mando TV ohjaa molempia järjestelmiä ja toimii TCL-televisiosi kaukosäätimenä wifin kautta. Ilmainen, ilman tiliä ja mainoksia.',
    pasos=[
      'Selvitä, mitä järjestelmää TCL:si käyttää. Jos aloitusnäytöllä on yksinkertainen ruudukko kanavaruuduista, se on Roku TV. Jos se näyttää Google TV:ltä tai Android TV:ltä, suosituksia täynnä olevine riveineen, se on Google TV.',
      'Yhdistä puhelimesi ja TCL-televisio samaan wifiin.',
      'Avaa Mando TV. TCL tulee listaan itsestään. Napauta sitä.',
      'TCL:llä, jossa on Roku TV, mitään muuta ei tarvita. TCL:llä, jossa on Google TV, kirjoitat 6-merkkisen koodin, jonka televisio näyttää näytöllä (vain ensimmäisellä kerralla).',
      'Käytä nuolia, OK:ta, Takaisin-, Koti- ja äänenvoimakkuuspainiketta sekä näppäimistöä. Käynnistä televisio sovelluksella, jos olet ottanut käyttöön käynnistyksen verkon kautta (katso alla).',
    ],
    extra=[
      ('TCL-television käynnistys puhelimella', 'TCL Roku TV:ssä ota käyttöön ”TV:n pikakäynnistys” kohdasta Asetukset > Järjestelmä > Virta. TCL Google TV:ssä etsi verkko- tai virta-asetuksista Wake on LAN, ”Käynnistys verkon kautta” tai etäkäynnistys. Joissakin malleissa sitä ei ole. Käynnistä televisio silloin fyysisellä virtapainikkeella, yleensä alhaalla keskellä tai takana.'),
      ('Jos TCL ei tule näkyviin', 'Tarkista, että puhelin ja televisio ovat samassa wifissä. Reitittimet, joissa 2,4 GHz:n ja 5 GHz:n verkot on eroteltu, voivat piilottaa laitteet toisiltaan. Salli iPhonella Mando TV:lle ”Lähiverkko” asetuksissa. Voit myös lisätä television kirjoittamalla sen IP-osoitteen. Lue [Puhelimesi ei löydä televisiota](@not-found).'),
      ('Lisää TCL:stäsi', 'TCL:lle, jossa on Roku TV, katso [Roku-kaukosäädinsovellus](@roku), TCL:lle, jossa on Google TV tai Android TV, [Android TV -kaukosäädinsovellus](@android).'),
      ('Ilmainen ja Pro', 'Nuolipainikkeet, OK, Takaisin, Koti, äänenvoimakkuus, kanavat, numerot, näppäimistö, sovellusten avaaminen, tulojen vaihto sekä käynnistys ja sammutus ovat ilmaisia, ilman mainoksia ja tilausta. Kosketuslevy, puhekomennot, suosikkisovellukset, rutiinit ja uniajastin kuuluvat Mando TV Pro -versioon, joka on kertaosto ilman tilausta.'),
    ],
    marca=None,
    faq=[
      ('Toimiiko Mando TV jokaisen TCL-television kanssa?', 'Se toimii TCL-televisioilla, joissa on Roku TV, Google TV tai Android TV, eli useimmilla TCL-älytelevisioilla. TCL:ää, joka ei ole älytelevisio, ei voi ohjata wifin kautta.'),
      ('Tarvitsenko TCL-sovelluksen tai TCL-tilin?', 'Et. Mando TV yhdistää suoraan kotisi wifin kautta eikä vaadi tiliä.'),
      ('TCL:ni pyytää koodia. Missä se on?', 'TCL-mallit, joissa on Google TV ja Android TV, näyttävät 6-merkkisen koodin näytöllä. Kirjoita se Mando TV:hen täsmälleen sellaisena kuin se näkyy. TCL, jossa on Roku TV, ei pyydä koodia.'),
    ]),
  dict(clave='hisense', corto='Hisense-kaukosäädin', fecha='2026-11-23',
    titulo='Hisense-kaukosäädinsovellus: mikä toimii puhelimella',
    desc='Hisense-kaukosäädin Mando TV:llä: ohjaus VIDAA:lle, Roku TV:lle, Google TV:lle ja Fire TV:lle wifin kautta. Rehellinen yleiskuva siitä, mikä toimii.',
    h1='Hisense-kaukosäädinsovellus: mikä toimii ja mikä ei',
    intro='Hisense-televisiot eivät ole sisältä kaikki samanlaisia. Mallista riippuen ne käyttävät Hisensen omaa VIDAA-järjestelmää, Roku TV:tä, Google TV:tä tai Fire TV:tä. Mando TV toimii Hisensen kaukosäätimenä kaikilla neljällä järjestelmällä, yhtä poikkeusta lukuun ottamatta joissakin uudemmissa VIDAA-malleissa. Tässä näet, miten tunnistat järjestelmäsi ja mitä odottaa.',
    pasos=[
      'Tarkista, mitä järjestelmää Hisensesi käyttää. VIDAA on Hisensen oma käyttöliittymä. Roku TV näyttää ruudukon kanavaruuduista. Google TV näyttää suosituksia sisältäviä rivejä. Fire TV näyttää Fire TV:n aloitusnäytön Amazon-riveineen.',
      'Yhdistä puhelimesi ja Hisense-televisio samaan wifiin.',
      'Avaa Mando TV. Televisio tulee listaan itsestään. Napauta sitä.',
      'VIDAA- ja Fire TV -mallit voivat näyttää nelinumeroisen PIN-koodin; Google TV näyttää kuusimerkkisen koodin. Kirjoita se sovellukseen. Roku TV ei kysy mitään. Teet sen vain kerran.',
      'Käytä puhelimesi nuolia, OK:ta, Takaisin-, Koti- ja äänenvoimakkuuspainiketta sekä näppäimistöä.',
    ],
    extra=[
      ('Hisense ja Roku TV tai Google TV', 'Nämä toimivat täysin kuten mikä tahansa muu Roku- tai Google TV -televisio. Lisätietoja sivuilla [Roku-kaukosäädinsovellus](@roku) ja [Android TV -kaukosäädinsovellus](@android).'),
      ('Hisense ja Fire TV', 'Fire TV -tuki on uusi Mando TV:ssä. Päivitä sovellus uusimpaan versioon kaupastasi. Miten pariliitos PIN-koodilla toimii, kerrotaan sivulla [Fire TV -kaukosäädinsovellus](@firetv). Jos jokin ei toimi odotetusti, kirjoita meille Ohje-sivun kautta ja kerro mallisi.'),
      ('Hisense ja VIDAA', 'Useimmat VIDAA-mallit toimivat: painikkeet, äänenvoimakkuus, näppäimistö, sovellukset ja tulot. Jotkin uudemmat VIDAA-mallit hyväksyvät vain virallisen Hisense-sovelluksen. Mando TV tunnistaa sen yhdistäessään ja kertoo siitä selvästi sen sijaan, että epäonnistuisi hiljaa. Silloin oikea tie on mallisi Hisense-sovellus, television painikkeet tai alkuperäinen kaukosäädin.'),
      ('Hisensen käynnistys puhelimella', 'Hisense Roku TV:ssä ota käyttöön ”TV:n pikakäynnistys” kohdasta Asetukset > Järjestelmä > Virta. Google TV:ssä etsi Wake on LAN- tai ”Käynnistys verkon kautta” -asetusta. Jos sellaista ei ole, käytä television virtapainiketta.'),
      ('Ilmainen ja Pro', 'Nuolipainikkeet, OK, Takaisin, Koti, äänenvoimakkuus, kanavat, numeronäppäimet, näppäimistö, sovellusten avaaminen, tulojen vaihto sekä käynnistys ja sammutus ovat ilmaisia, ilman mainoksia ja ilman tilausta. Kosketuslevy, puhekomennot, suosikkisovellukset, rutiinit ja uniajastin kuuluvat Mando TV Pro -versioon, joka on kertaosto ilman tilausta.'),
    ],
    marca=None,
    faq=[
      ('Toimiiko Mando TV Hisense VIDAA:n kanssa?', 'Kyllä, useimpien VIDAA-mallien kanssa. Jotkin uudemmat hyväksyvät vain virallisen Hisense-sovelluksen; Mando TV tunnistaa sen ja kertoo siitä sinulle. Hisense-televisioita, joissa on Roku TV, Google TV tai Fire TV, tuetaan myös.'),
      ('Mistä tiedän, onko Hisenseni Roku TV, Google TV vai Fire TV?', 'Katso aloitusnäyttöä. Roku TV:ssä on yksinkertainen ruudukko ja Roku-logo käynnistyksessä. Google TV:ssä on suosituksia sisältäviä rivejä. Fire TV:ssä on Amazon Fire TV:n aloitusnäyttö. Myös mallin nimi kohdassa Asetukset > Tietoja kertoo sen.'),
      ('Tarvitsenko Hisense- tai Google-tilin?', 'Et. Mando TV yhdistää suoraan kotisi wifin kautta eikä vaadi omaa tiliä.'),
    ]),
  dict(clave='philips', corto='Philips-kaukosäädin', fecha='2026-11-23',
    titulo='Philips-kaukosäädinsovellus: Roku TV, Google TV, Android TV',
    desc='Mando TV ohjaa Philips-televisioita, joissa on Roku TV, Google TV tai Android TV, wifin kautta puhelimelta tai tietokoneelta. Titan OS:ää ei tueta.',
    h1='Philips-television ohjaus puhelimella',
    intro='Philips-televisiot käyttävät maasta ja valmistusvuodesta riippuen eri järjestelmiä: Roku TV Yhdysvalloissa, Google TV tai Android TV monissa maissa ja Titan OS joissakin uudemmissa eurooppalaisissa malleissa. Mando TV ohjaa malleja, joissa on Roku TV, Google TV ja Android TV, wifin kautta.',
    pasos=[
      'Tarkista aloitusnäyttö. Roku TV näyttää ruudukon ruutuja. Google TV ja Android TV näyttävät Googlen suosituksia sisältäviä rivejä. Titan OS:llä on oma aloitusnäyttönsä.',
      'Yhdistä puhelimesi ja televisio samaan wifiin.',
      'Avaa Mando TV ja napauta listassa Philips-televisiotasi.',
      'Roku TV ei kysy mitään. Google TV ja Android TV näyttävät 6-merkkisen koodin: kirjoita se sovellukseen kerran.',
      'Käytä nuolipainikkeita, OK:ta, Takaisin-, Koti- ja äänenvoimakkuuspainiketta sekä näppäimistöä.',
    ],
    extra=[
      ('Philips Roku TV', 'Toimii kuten mikä tahansa Roku-televisio. Jotta voit käynnistää sen puhelimesta, ota käyttöön ”TV:n pikakäynnistys” kohdasta Asetukset > Järjestelmä > Virta. Lisää sivulla [Roku-kaukosäädinsovellus](@roku).'),
      ('Philips ja Google TV tai Android TV', 'Kattaa monet Ambilight-mallit. Ne yhdistetään näytön koodilla. Jotta voit käynnistää ne puhelimesta, etsi verkko- tai virta-asetuksista Wake on LAN tai ”Käynnistys verkon kautta”. Joissakin malleissa tätä asetusta ei ole. Lisää sivulla [Android TV -kaukosäädinsovellus](@android).'),
      ('Vanhemmat Philips-televisiot ilman Androidia', 'Philips-televisioita vuosilta 2011-2015, jotka eivät käytä Androidia, tuetaan Mando TV:ssä betassa. Se on uusi eikä tarvitse pariliitoskoodia.'),
      ('Philips ja Titan OS', 'Titan OS on toinen järjestelmä, jota Mando TV ei nykyisin ohjaa, ja sanomme sen mieluummin selvästi. Uudemmat Philips-mallit ilman Androidia eivät myöskään kuulu tuen piiriin.'),
      ('Ilmainen ja Pro', 'Kaukosäätimen voi ladata ja sitä voi käyttää ilmaiseksi, ilman mainoksia ja ilman tilausta. Mando TV Pro on valinnainen kertaosto lisäominaisuuksiin.'),
    ],
    marca=None,
    faq=[
      ('Toimiiko Mando TV Philips-televisioiden kanssa?', 'Philips-televisioiden kanssa, joissa on Roku TV, Google TV tai Android TV, kyllä, ja betassa vuosien 2011-2015 Philips-televisioiden kanssa ilman Androidia. Malleja, joissa on Titan OS, ei tueta.'),
      ('Ohjaako Mando TV Ambilightia?', 'Mando TV on kaukosäädin: se lähettää painikkeet, joten nuolilla ja OK:lla pääset Ambilight-asetuksiin. Erillisiä Ambilight-säätimiä ei ole.'),
      ('Tarvitsenko Philips- tai Google-tilin?', 'Et. Mando TV yhdistää kotisi wifin kautta eikä vaadi tiliä.'),
    ]),
]
OTRAS_GUIAS += [
  ('no-sub', 'Kaukosäädinsovellus ilman tilausta ja ilman mainoksia'),
  ('roku-app-alt', 'Roku-sovelluksen vaihtoehto: yksi kaikille televisioille'),
  ('lg-thinq', 'LG ThinQ -sovelluksen vaihtoehto LG-televisiollesi'),
  ('smartthings', 'SmartThingsin vaihtoehto Samsung-televisioille'),
  ('googletv-alt', 'Google TV -kaukosäätimen vaihtoehto puhelimelle'),
  ('windows', 'Kaukosäädinsovellus Windows-tietokoneelle'),
  ('iphone', 'Kaukosäädinsovellus iPhonelle: yksi kaikille televisioille'),
  ('firetv', 'Fire TV -kaukosäädin puhelimelle tai tietokoneelle'),
  ('firetv-lost', 'Fire TV -kaukosäädin hukassa: näin käytät puhelintasi'),
  ('turn-on', 'Näin käynnistät television ilman kaukosäädintä'),
  ('sony', 'Näin ohjaat Sony-televisiotasi puhelimella'),
  ('tcl', 'Näin ohjaat TCL-televisiotasi puhelimella'),
  ('hisense', 'Hisense-kaukosäädinsovellus: mikä toimii ja mikä ei'),
  ('philips', 'Philips-television ohjaus puhelimella'),
]
# <<< guías traídas del inglés
