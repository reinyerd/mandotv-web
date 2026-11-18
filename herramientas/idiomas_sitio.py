# Mapa de idiomas del sitio: una sola fuente para las rutas gemelas y los hreflang de todos los generadores.
# Cada clave es una página y dice en qué carpeta o archivo vive en cada idioma (sin barra inicial; carpeta sin barra final).
# Para activar un idioma nuevo basta añadirlo a ACTIVOS cuando sus páginas ya existen.
# Lo usan generar_guias.py, generar_marcas.py, generar_en.py y generar_idiomas.py (importan este archivo por ruta).
URL = 'https://mandotv.app'
ACTIVOS = ['es', 'en', 'de', 'fr', 'pt']          # idiomas con páginas publicadas
ORDEN = ['es', 'en', 'de', 'fr', 'pt', 'it']  # orden de los hreflang
NOMBRES = {'es': 'Español', 'en': 'English', 'de': 'Deutsch', 'fr': 'Français', 'pt': 'Português (Brasil)', 'it': 'Italiano'}
CODIGO_LANG = {'es': 'es', 'en': 'en', 'de': 'de', 'fr': 'fr', 'pt': 'pt-BR', 'it': 'it'}

# (es, en, de, fr, pt, it): archivos terminan en .html; el resto son carpetas.
_FILAS = {
  'home': ('', 'en', 'de', 'fr', 'pt', 'it'),
  'lg': ('control-remoto-lg', 'en/lg-tv-remote', 'de/lg-fernbedienung', 'fr/telecommande-lg', 'pt/controle-remoto-lg', 'it/telecomando-lg'),
  'samsung': ('control-remoto-samsung', 'en/samsung-tv-remote', 'de/samsung-fernbedienung', 'fr/telecommande-samsung', 'pt/controle-remoto-samsung', 'it/telecomando-samsung'),
  'roku': ('control-remoto-roku', 'en/roku-remote', 'de/roku-fernbedienung', 'fr/telecommande-roku', 'pt/controle-remoto-roku', 'it/telecomando-roku'),
  'android': ('control-remoto-android-tv', 'en/android-tv-remote', 'de/android-tv-fernbedienung', 'fr/telecommande-android-tv', 'pt/controle-remoto-android-tv', 'it/telecomando-android-tv'),
  'guias': ('guias', 'en/guides', 'de/ratgeber', 'fr/guides', 'pt/guias', 'it/guide'),
  'lost-tv': ('guias/perdi-el-control-del-tv', 'en/guides/lost-tv-remote', 'de/ratgeber/fernbedienung-verloren', 'fr/guides/telecommande-tv-perdue', 'pt/guias/perdi-o-controle-da-tv', 'it/guide/telecomando-tv-perso'),
  'lost-lg': ('guias/perdi-el-control-del-lg', 'en/guides/lost-lg-remote', 'de/ratgeber/lg-fernbedienung-verloren', 'fr/guides/telecommande-lg-perdue', 'pt/guias/perdi-o-controle-da-lg', 'it/guide/telecomando-lg-perso'),
  'hdmi': ('guias/cambiar-entrada-hdmi-sin-control', 'en/guides/change-hdmi-input-without-remote', 'de/ratgeber/hdmi-eingang-wechseln-ohne-fernbedienung', 'fr/guides/changer-entree-hdmi-sans-telecommande', 'pt/guias/trocar-entrada-hdmi-sem-controle', 'it/guide/cambiare-ingresso-hdmi-senza-telecomando'),
  'androidtv': ('guias/android-tv-sin-control-remoto', 'en/guides/android-tv-without-remote', 'de/ratgeber/android-tv-ohne-fernbedienung', 'fr/guides/android-tv-sans-telecommande', 'pt/guias/android-tv-sem-controle-remoto', 'it/guide/android-tv-senza-telecomando'),
  'lg-on': ('guias/encender-tv-lg-con-el-celular', 'en/guides/turn-on-lg-tv-with-phone', 'de/ratgeber/lg-fernseher-mit-handy-einschalten', 'fr/guides/allumer-tv-lg-avec-telephone', 'pt/guias/ligar-tv-lg-pelo-celular', 'it/guide/accendere-tv-lg-con-lo-smartphone'),
  'console': ('guias/encender-tv-y-hdmi-de-la-consola-sin-control', 'en/guides/turn-on-tv-console-hdmi-without-remote', 'de/ratgeber/fernseher-und-konsole-ohne-fernbedienung', 'fr/guides/allumer-tv-et-hdmi-console-sans-telecommande', 'pt/guias/ligar-tv-e-hdmi-do-console-sem-controle', 'it/guide/accendere-tv-e-hdmi-console-senza-telecomando'),
  'samsung-lost': ('guias/control-remoto-samsung-sin-control', 'en/guides/samsung-tv-without-remote', 'de/ratgeber/samsung-fernseher-ohne-fernbedienung', 'fr/guides/tv-samsung-sans-telecommande', 'pt/guias/tv-samsung-sem-controle-remoto', 'it/guide/tv-samsung-senza-telecomando'),
  'roku-lost': ('guias/perdi-el-control-del-roku', 'en/guides/lost-roku-remote', 'de/ratgeber/roku-fernbedienung-verloren', 'fr/guides/telecommande-roku-perdue', 'pt/guias/perdi-o-controle-da-roku', 'it/guide/telecomando-roku-perso'),
  'roku-403': ('guias/roku-no-responde-al-celular', 'en/guides/roku-remote-app-not-working', 'de/ratgeber/roku-app-funktioniert-nicht', 'fr/guides/application-roku-ne-fonctionne-pas', 'pt/guias/roku-nao-responde-ao-celular', 'it/guide/app-roku-non-funziona'),
  'androidtv-code': ('guias/android-tv-codigo-de-emparejamiento', 'en/guides/android-tv-pairing-code', 'de/ratgeber/android-tv-kopplungscode', 'fr/guides/android-tv-code-appairage', 'pt/guias/android-tv-codigo-de-pareamento', 'it/guide/android-tv-codice-di-associazione'),
  'not-found': ('guias/el-celular-no-encuentra-el-tv', 'en/guides/phone-cant-find-tv', 'de/ratgeber/handy-findet-fernseher-nicht', 'fr/guides/telephone-ne-trouve-pas-la-tv', 'pt/guias/celular-nao-encontra-a-tv', 'it/guide/smartphone-non-trova-la-tv'),
  'wifi': ('guias/conectar-celular-al-tv-por-wifi', 'en/guides/connect-phone-to-tv-wifi', 'de/ratgeber/handy-als-fernbedienung-wlan', 'fr/guides/telephone-comme-telecommande-wifi', 'pt/guias/celular-como-controle-remoto-por-wifi', 'it/guide/smartphone-come-telecomando-wifi'),
  'pc': ('guias/controlar-el-tv-desde-el-pc', 'en/guides/control-tv-from-pc', 'de/ratgeber/fernseher-mit-dem-pc-steuern', 'fr/guides/controler-la-tv-depuis-le-pc', 'pt/guias/controlar-a-tv-pelo-pc', 'it/guide/controllare-la-tv-dal-pc'),
  'soporte': ('soporte.html', 'en/support.html', 'de/hilfe.html', 'fr/aide.html', 'pt/ajuda.html', 'it/assistenza.html'),
  'privacidad': ('privacidad.html', 'en/privacy.html', 'de/datenschutz.html', 'fr/confidentialite.html', 'pt/privacidade.html', 'it/privacy.html'),
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
        if v['es'] == es.strip('/'):
            return k
    return None


def hreflangs(clave):
    """Bloque <link rel=alternate> con todas las gemelas y x-default (siempre el español)."""
    a = alternos(clave)
    filas = [f'  <link rel="alternate" hreflang="{l}" href="{u}">' for l, u in a.items()]
    filas.append(f'  <link rel="alternate" hreflang="x-default" href="{a["es"]}">')
    return '\n'.join(filas) + '\n'


def enlaces_idiomas(clave, excluir):
    """[(idioma, ruta, nombre)] de las demás gemelas, para los selectores de idioma."""
    return [(l, ruta(clave, l), NOMBRES[l]) for l in ORDEN if l != excluir and existe(clave, l)]
