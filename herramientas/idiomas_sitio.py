# Mapa de idiomas del sitio: una sola fuente para las rutas gemelas y los hreflang de todos los generadores.
# Cada clave es una página y dice en qué carpeta o archivo vive en cada idioma (sin barra inicial; carpeta sin barra final).
# Para activar un idioma nuevo basta añadirlo a ACTIVOS cuando sus páginas ya existen.
# Lo usan generar_guias.py, generar_marcas.py, generar_en.py y generar_idiomas.py (importan este archivo por ruta).
URL = 'https://mandotv.app'
ACTIVOS = ['es', 'en', 'de', 'fr', 'pt', 'it']          # idiomas con páginas publicadas
ORDEN = ['es', 'en', 'de', 'fr', 'pt', 'it']  # orden de los hreflang
NOMBRES = {'es': 'Español', 'en': 'English', 'de': 'Deutsch', 'fr': 'Français', 'pt': 'Português (Brasil)', 'it': 'Italiano'}
CODIGO_LANG = {'es': 'es', 'en': 'en', 'de': 'de', 'fr': 'fr', 'pt': 'pt-BR', 'it': 'it'}

# (es, en, de, fr, pt, it): archivos terminan en .html; el resto son carpetas.
_FILAS = {
  'home': ('es', '', 'de', 'fr', 'pt', 'it'),  # 24-nov: la portada en inglés va en la raíz
  'lg': ('es/control-remoto-lg', 'lg-tv-remote', 'de/lg-fernbedienung', 'fr/telecommande-lg', 'pt/controle-remoto-lg', 'it/telecomando-lg'),
  'samsung': ('es/control-remoto-samsung', 'samsung-tv-remote', 'de/samsung-fernbedienung', 'fr/telecommande-samsung', 'pt/controle-remoto-samsung', 'it/telecomando-samsung'),
  'roku': ('es/control-remoto-roku', 'roku-remote', 'de/roku-fernbedienung', 'fr/telecommande-roku', 'pt/controle-remoto-roku', 'it/telecomando-roku'),
  'android': ('es/control-remoto-android-tv', 'android-tv-remote', 'de/android-tv-fernbedienung', 'fr/telecommande-android-tv', 'pt/controle-remoto-android-tv', 'it/telecomando-android-tv'),
  'guias': ('es/guias', 'guides', 'de/ratgeber', 'fr/guides', 'pt/guias', 'it/guide'),
  'lost-tv': ('es/guias/perdi-el-control-del-tv', 'guides/lost-tv-remote', 'de/ratgeber/fernbedienung-verloren', 'fr/guides/telecommande-tv-perdue', 'pt/guias/perdi-o-controle-da-tv', 'it/guide/telecomando-tv-perso'),
  'lost-lg': ('es/guias/perdi-el-control-del-lg', 'guides/lost-lg-remote', 'de/ratgeber/lg-fernbedienung-verloren', 'fr/guides/telecommande-lg-perdue', 'pt/guias/perdi-o-controle-da-lg', 'it/guide/telecomando-lg-perso'),
  'hdmi': ('es/guias/cambiar-entrada-hdmi-sin-control', 'guides/change-hdmi-input-without-remote', 'de/ratgeber/hdmi-eingang-wechseln-ohne-fernbedienung', 'fr/guides/changer-entree-hdmi-sans-telecommande', 'pt/guias/trocar-entrada-hdmi-sem-controle', 'it/guide/cambiare-ingresso-hdmi-senza-telecomando'),
  'androidtv': ('es/guias/android-tv-sin-control-remoto', 'guides/android-tv-without-remote', 'de/ratgeber/android-tv-ohne-fernbedienung', 'fr/guides/android-tv-sans-telecommande', 'pt/guias/android-tv-sem-controle-remoto', 'it/guide/android-tv-senza-telecomando'),
  'lg-on': ('es/guias/encender-tv-lg-con-el-celular', 'guides/turn-on-lg-tv-with-phone', 'de/ratgeber/lg-fernseher-mit-handy-einschalten', 'fr/guides/allumer-tv-lg-avec-telephone', 'pt/guias/ligar-tv-lg-pelo-celular', 'it/guide/accendere-tv-lg-con-lo-smartphone'),
  'console': ('es/guias/encender-tv-y-hdmi-de-la-consola-sin-control', 'guides/turn-on-tv-console-hdmi-without-remote', 'de/ratgeber/fernseher-und-konsole-ohne-fernbedienung', 'fr/guides/allumer-tv-et-hdmi-console-sans-telecommande', 'pt/guias/ligar-tv-e-hdmi-do-console-sem-controle', 'it/guide/accendere-tv-e-hdmi-console-senza-telecomando'),
  'samsung-lost': ('es/guias/control-remoto-samsung-sin-control', 'guides/samsung-tv-without-remote', 'de/ratgeber/samsung-fernseher-ohne-fernbedienung', 'fr/guides/tv-samsung-sans-telecommande', 'pt/guias/tv-samsung-sem-controle-remoto', 'it/guide/tv-samsung-senza-telecomando'),
  'roku-lost': ('es/guias/perdi-el-control-del-roku', 'guides/lost-roku-remote', 'de/ratgeber/roku-fernbedienung-verloren', 'fr/guides/telecommande-roku-perdue', 'pt/guias/perdi-o-controle-da-roku', 'it/guide/telecomando-roku-perso'),
  'roku-403': ('es/guias/roku-no-responde-al-celular', 'guides/roku-remote-app-not-working', 'de/ratgeber/roku-app-funktioniert-nicht', 'fr/guides/application-roku-ne-fonctionne-pas', 'pt/guias/roku-nao-responde-ao-celular', 'it/guide/app-roku-non-funziona'),
  'androidtv-code': ('es/guias/android-tv-codigo-de-emparejamiento', 'guides/android-tv-pairing-code', 'de/ratgeber/android-tv-kopplungscode', 'fr/guides/android-tv-code-appairage', 'pt/guias/android-tv-codigo-de-pareamento', 'it/guide/android-tv-codice-di-associazione'),
  'not-found': ('es/guias/el-celular-no-encuentra-el-tv', 'guides/phone-cant-find-tv', 'de/ratgeber/handy-findet-fernseher-nicht', 'fr/guides/telephone-ne-trouve-pas-la-tv', 'pt/guias/celular-nao-encontra-a-tv', 'it/guide/smartphone-non-trova-la-tv'),
  'wifi': ('es/guias/conectar-celular-al-tv-por-wifi', 'guides/connect-phone-to-tv-wifi', 'de/ratgeber/handy-als-fernbedienung-wlan', 'fr/guides/telephone-comme-telecommande-wifi', 'pt/guias/celular-como-controle-remoto-por-wifi', 'it/guide/smartphone-come-telecomando-wifi'),
  'pc': ('es/guias/controlar-el-tv-desde-el-pc', 'guides/control-tv-from-pc', 'de/ratgeber/fernseher-mit-dem-pc-steuern', 'fr/guides/controler-la-tv-depuis-le-pc', 'pt/guias/controlar-a-tv-pelo-pc', 'it/guide/controllare-la-tv-dal-pc'),
  # Guías solo en inglés (SEO EE. UU.): sin gemelas; el hreflang x-default apunta a la propia página.
  'lg-thinq': ('es/guias/alternativa-a-lg-thinq', 'guides/lg-thinq-app-alternative', 'de/ratgeber/lg-thinq-alternative', 'fr/guides/alternative-lg-thinq', 'pt/guias/alternativa-ao-lg-thinq', 'it/guide/alternativa-lg-thinq'),
  'roku-app-alt': ('es/guias/alternativa-a-la-app-de-roku', 'guides/roku-app-alternative', 'de/ratgeber/roku-app-alternative', 'fr/guides/alternative-application-roku', 'pt/guias/alternativa-ao-app-da-roku', 'it/guide/alternativa-app-roku'),
  'tcl': ('es/guias/control-remoto-tcl', 'guides/tcl-tv-remote-app', 'de/ratgeber/tcl-fernbedienungs-app', 'fr/guides/application-telecommande-tcl', 'pt/guias/controle-remoto-tcl', 'it/guide/app-telecomando-tcl'),
  'hisense': ('es/guias/control-remoto-hisense', 'guides/hisense-tv-remote-app', 'de/ratgeber/hisense-fernbedienungs-app', 'fr/guides/application-telecommande-hisense', 'pt/guias/controle-remoto-hisense', 'it/guide/app-telecomando-hisense'),
  'vizio': (None, 'guides/vizio-tv-remote-app', None, None, None, None),
  'firetv': ('es/guias/control-remoto-fire-tv-en-el-celular', 'guides/fire-tv-remote-app', 'de/ratgeber/fire-tv-fernbedienungs-app', 'fr/guides/application-telecommande-fire-tv', 'pt/guias/controle-remoto-fire-tv-no-celular', 'it/guide/app-telecomando-fire-tv'),
  'iphone': ('es/guias/app-control-remoto-para-iphone', 'guides/tv-remote-app-for-iphone', 'de/ratgeber/fernbedienungs-app-fuer-iphone', 'fr/guides/application-telecommande-pour-iphone', 'pt/guias/app-de-controle-remoto-para-iphone', 'it/guide/app-telecomando-per-iphone'),
  'windows': ('es/guias/app-control-remoto-para-windows', 'guides/tv-remote-app-for-windows', 'de/ratgeber/fernbedienungs-app-fuer-windows', 'fr/guides/application-telecommande-pour-windows', 'pt/guias/app-de-controle-remoto-para-windows', 'it/guide/app-telecomando-per-windows'),
  # 2026-11-21: rescate y alternativas (EE. UU.)
  'firetv-lost': ('es/guias/perdi-el-control-del-fire-tv', 'guides/lost-fire-tv-remote', 'de/ratgeber/fire-tv-fernbedienung-verloren', 'fr/guides/telecommande-fire-tv-perdue', 'pt/guias/perdi-o-controle-do-fire-tv', 'it/guide/telecomando-fire-tv-perso'),
  'turn-on': ('es/guias/encender-el-tv-sin-control', 'guides/turn-on-tv-without-remote', 'de/ratgeber/fernseher-ohne-fernbedienung-einschalten', 'fr/guides/allumer-tv-sans-telecommande', 'pt/guias/ligar-a-tv-sem-controle', 'it/guide/accendere-tv-senza-telecomando'),
  'no-sub': ('es/guias/app-control-remoto-sin-suscripcion', 'guides/tv-remote-app-no-subscription', 'de/ratgeber/fernbedienungs-app-ohne-abo', 'fr/guides/application-telecommande-sans-abonnement', 'pt/guias/app-de-controle-remoto-sem-assinatura', 'it/guide/app-telecomando-senza-abbonamento'),
  'smartthings': ('es/guias/alternativa-a-smartthings', 'guides/smartthings-tv-remote-alternative', 'de/ratgeber/smartthings-alternative', 'fr/guides/alternative-smartthings', 'pt/guias/alternativa-ao-smartthings', 'it/guide/alternativa-smartthings'),
  'googletv-alt': ('es/guias/alternativa-a-la-app-google-tv', 'guides/google-tv-remote-app-alternative', 'de/ratgeber/google-tv-app-alternative', 'fr/guides/alternative-application-google-tv', 'pt/guias/alternativa-ao-app-google-tv', 'it/guide/alternativa-app-google-tv'),
  # 2026-11-21: marcas que funcionan con Roku TV, Google TV / Android TV o Fire TV (EE. UU. y Europa)
  'sony': ('es/guias/control-remoto-sony', 'guides/sony-tv-remote-app', 'de/ratgeber/sony-fernbedienungs-app', 'fr/guides/application-telecommande-sony', 'pt/guias/controle-remoto-sony', 'it/guide/app-telecomando-sony'),
  'insignia': (None, 'guides/insignia-tv-remote-app', None, None, None, None),
  'onn': (None, 'guides/onn-tv-remote-app', None, None, None, None),
  'toshiba': (None, 'guides/toshiba-tv-remote-app', None, None, None, None),
  'sharp': (None, 'guides/sharp-tv-remote-app', None, None, None, None),
  'philips': ('es/guias/control-remoto-philips', 'guides/philips-tv-remote-app', 'de/ratgeber/philips-fernbedienungs-app', 'fr/guides/application-telecommande-philips', 'pt/guias/controle-remoto-philips', 'it/guide/app-telecomando-philips'),
  'westinghouse': (None, 'guides/westinghouse-tv-remote-app', None, None, None, None),
  'pioneer': (None, 'guides/pioneer-tv-remote-app', None, None, None, None),
  # 2026-11-21: marcas de Latinoamérica, solo en español (sin búsquedas en inglés)
  'master-g': ('es/control-remoto-master-g', None, None, None, None, None),
  'kalley': ('es/control-remoto-kalley', None, None, None, None, None),
  'caixun': ('es/control-remoto-caixun', None, None, None, None, None),
  'hyundai': ('es/control-remoto-hyundai', None, None, None, None, None),
  'noblex': ('es/control-remoto-noblex', None, None, None, None, None),
  'bgh': ('es/control-remoto-bgh', None, None, None, None, None),
  'soporte': ('es/soporte.html', 'support.html', 'de/hilfe.html', 'fr/aide.html', 'pt/ajuda.html', 'it/assistenza.html'),
  'privacidad': ('es/privacidad.html', 'privacy.html', 'de/datenschutz.html', 'fr/confidentialite.html', 'pt/privacidade.html', 'it/privacy.html'),
}
_COLS = ('es', 'en', 'de', 'fr', 'pt', 'it')
PAGINAS = {k: {l: v for l, v in zip(_COLS, fila) if v is not None} for k, fila in _FILAS.items()}


def ruta(clave, lang):
    """Ruta pública (con barra inicial) de una página en un idioma."""
    p = PAGINAS[clave][lang]
    if p.endswith('.html'):
        return '/' + p
    return '/' + p + '/' if p else '/'


def carpeta(clave, lang):
    """Carpeta o archivo relativo, sin barra inicial ni final."""
    return PAGINAS[clave][lang]


def existe(clave, lang):
    return lang in PAGINAS[clave] and lang in ACTIVOS


def alternos(clave):
    """{idioma: url absoluta} de las gemelas publicadas, en el orden de ORDEN."""
    return {l: URL + ruta(clave, l) for l in ORDEN if existe(clave, l)}


def clave_es(es):
    """Clave de una página a partir de su carpeta en español (por ejemplo 'guias/perdi-el-control-del-tv')."""
    for k, v in PAGINAS.items():
        if v.get('es') == es.strip('/'):
            return k
    return None


def hreflangs(clave):
    """Bloque <link rel=alternate> con todas las gemelas y x-default (el inglés si existe; si no, el español)."""
    a = alternos(clave)
    filas = [f'  <link rel="alternate" hreflang="{l}" href="{u}">' for l, u in a.items()]
    # x-default (24-nov): el inglés, que entiende más gente cuando el idioma de quien busca no está en el sitio;
    # si la página no existe en inglés (marcas solo de Latinoamérica), el español o la que haya.
    filas.append(f'  <link rel="alternate" hreflang="x-default" href="{a.get("en") or a.get("es") or next(iter(a.values()))}">')
    return '\n'.join(filas) + '\n'


def enlaces_idiomas(clave, excluir):
    """[(idioma, ruta, nombre)] de las demás gemelas, para los selectores de idioma."""
    return [(l, ruta(clave, l), NOMBRES[l]) for l in ORDEN if l != excluir and existe(clave, l)]


# Guías de PC y Windows (GEO, 23-nov): ChatGPT y Gemini recomiendan Mando TV en Windows pero inventan un enlace de
# Microsoft Store que no existe. En estas páginas la ficha va también como texto visible y en un SoftwareApplication.
MS_STORE = 'https://apps.microsoft.com/detail/9N3D7T1DP2SW'
_MS_TEXTO = dict(es='Ficha en Microsoft Store:', en='Microsoft Store page:', de='Seite im Microsoft Store:',
                 fr='Fiche Microsoft Store :', pt='Página na Microsoft Store:', it='Scheda su Microsoft Store:')
RUTAS_PC = {v for k in ('pc', 'windows') for v in PAGINAS[k].values()}


def es_guia_pc(ruta):
    return ruta.strip('/') in RUTAS_PC


def linea_ms_store(lang):
    return f'<p class="nota">{_MS_TEXTO[lang]} <a href="{MS_STORE}">apps.microsoft.com/detail/9N3D7T1DP2SW</a></p>'


def app_windows(url):
    """Igual al SoftwareApplication de las portadas, para la app de Windows."""
    return {"@type": "SoftwareApplication", "name": "Mando TV", "applicationCategory": "UtilitiesApplication",
            "operatingSystem": "Windows 10, Windows 11", "url": url, "downloadUrl": MS_STORE, "installUrl": MS_STORE,
            "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD", "availability": "https://schema.org/InStock"},
            "author": {"@id": "https://mandotv.app/#org"}, "publisher": {"@id": "https://mandotv.app/#org"}}


def enlazar_mando(intro_html):
    """Primer "Mando TV" del párrafo (ya escapado) como enlace directo a la ficha de Microsoft Store."""
    return intro_html.replace('Mando TV', f'<a href="{MS_STORE}">Mando TV</a>', 1)
