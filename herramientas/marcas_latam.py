# Páginas de marca de Latinoamérica (2026-11-21), solo en español. Las importa generar_marcas.py (se suman a MARCAS).
# Solo se nombran las plataformas que esos modelos usan de verdad y que la app ya maneja (Google TV / Android TV y
# Roku TV). No se dice qué funciones son Pro: "control gratis, Pro opcional de pago único, sin anuncios ni suscripción".
# Fuentes (fichas de tiendas consultadas el 2026-11-21):
#   Master G: Google TV (MGG32HFK5, MGG43FFK5, MGG55UFKG: paris.cl, easy.cl, simple.ripley.cl, falabella.com) y
#     Android TV con Android 11 (MGAE32F, MGAE50F, MGAE55F, MGAE6500F: falabella.com, paris.cl, simple.ripley.cl).
#   Kalley: Roku TV (K-RTV32, 60RQ400) y Google TV (serie G315, K-GTV): ktronix.com, portafolio.co.
#   Caixun: Roku TV (C32V1HR, C43V1FR, C50V1UR) y Google TV (C55V1UG, C65V1UG, C43K1FG): falabella.com, sodimac.cl.
#   Hyundai: Google TV (HYLED3259QG, HYLED4326QG, HYLED4328G) y Android TV: simple.ripley.com.pe, exito.com, megatone.net.
#   Noblex: Google TV (DV50X8580, DV55X8580) y Android TV (DV43X7180): fravega.com, mercadolibre.com.ar.
#   BGH: Android TV (B4325FS5A) y Google TV (QLED 50 y 60): culturageek.com.ar, cronista.com.

_PRECIO = 'El control remoto es gratis, sin anuncios y sin suscripción. Pro es un pago único opcional.'

_FUNCIONES_GTV = [
  ('Todos los botones', 'Cruceta, OK, Atrás, Inicio, volumen, silencio y reproducción.'),
  ('Teclado', 'Escribe en YouTube, Netflix y el buscador del TV con el teclado de tu celular.'),
  ('Encender el TV', 'En los modelos con encendido por red, Mando TV lo enciende y se conecta solo.'),
  ('Sin cuenta', 'No pide cuenta de Google ni registrarte: se conecta directo por tu WiFi.'),
  ('iPhone, Android y PC', 'Funciona igual desde cualquier celular o computador con Windows.'),
  ('Todos los TV de la casa', 'La misma app maneja también Samsung, LG, Roku y otros televisores con Google TV.'),
]
_FUNCIONES_ROKU_GTV = [
  ('Todos los botones', 'Cruceta, OK, Atrás, Inicio, volumen, silencio y reproducción.'),
  ('Teclado', 'Escribe búsquedas en YouTube, Netflix y los demás canales con el teclado de tu celular.'),
  ('Encender el TV', 'En los modelos Roku TV con inicio rápido y en los Google TV con encendido por red, Mando TV lo enciende.'),
  ('Sin cuenta', 'No pide cuenta de Roku ni de Google: se conecta directo por tu WiFi.'),
  ('iPhone, Android y PC', 'Funciona igual desde cualquier celular o computador con Windows.'),
  ('Todos los TV de la casa', 'La misma app maneja también Samsung, LG y otros televisores con Roku o Google TV.'),
]
_PASOS_GTV = lambda marca: [
  f'Conecta el celular y el TV {marca} a la misma red WiFi.',
  f'Abre Mando TV: tu {marca} aparece solo en la lista. Tócalo.',
  'El televisor muestra un código de 6 caracteres. Escríbelo en Mando TV (solo la primera vez). No necesitas el control para esto.',
]
_PASOS_ROKU_GTV = lambda marca: [
  f'Conecta el celular y el TV {marca} a la misma red WiFi.',
  f'Abre Mando TV: tu {marca} aparece solo en la lista. Tócalo.',
  'Si es Roku TV, no pide nada. Si es Google TV o Android TV, escribe el código de 6 caracteres que aparece en la pantalla (solo la primera vez).',
]
_ENCENDER_GTV = ('Depende del modelo. Busca "Wake on LAN", "Encender por red" o "Activación remota" en los ajustes de red o de '
                 'energía del televisor. Algunos modelos no lo traen: en ese caso, enciéndelo con el botón del TV, que suele '
                 'estar abajo al centro o en la parte de atrás.')
_ENCENDER_ROKU_GTV = ('En los modelos Roku TV, activa "Inicio rápido de TV" en Configuración, Sistema, Energía. En los modelos '
                      'con Google TV o Android TV, busca "Wake on LAN" o "Encender por red" en los ajustes de red o de energía; '
                      'algunos modelos no lo traen.')
_COMO_SE = ('¿Cómo sé si mi TV es Roku TV o Google TV?', 'Mira la pantalla de inicio. Roku TV muestra una cuadrícula de '
            'mosaicos con el menú de Roku a la izquierda. Google TV muestra filas de recomendaciones con el menú de Google. '
            'También lo dice la caja o la ficha del modelo.')
_GUIAS_GTV = [('android-tv-codigo-de-emparejamiento', 'Android TV pide un código para conectar el celular'),
              ('android-tv-sin-control-remoto', 'Android TV sin control remoto: cómo usarlo desde el celular'),
              ('perdi-el-control-del-tv', 'Perdí el control del TV: qué hacer ahora')]
_GUIAS_ROKU_GTV = [('perdi-el-control-del-roku', 'Perdí el control del Roku: cómo usar el celular'),
                   ('roku-no-responde-al-celular', 'Roku no responde al celular: solución al error 403'),
                   ('android-tv-codigo-de-emparejamiento', 'Android TV pide un código para conectar el celular'),
                   ('perdi-el-control-del-tv', 'Perdí el control del TV: qué hacer ahora')]


def _oficial(marca):
    return (f'¿Mando TV es la app oficial de {marca}?', f'No. Mando TV es una app independiente y no está afiliada a {marca}. '
            'La marca se nombra solo para indicar con qué televisores funciona.')


MARCAS_LATAM = [
  dict(slug='es/control-remoto-master-g', nombre='Master G', corto='Master G', color='#f2742b',
    titulo='Control remoto para TV Master G en tu celular | Mando TV',
    desc='Usa tu celular o PC como control remoto de tu TV Master G con Google TV o Android TV, por WiFi. Gratis, sin anuncios y sin cuenta.',
    h1='Control remoto para TV Master G',
    intro='Los televisores Master G más nuevos traen Google TV y los anteriores, Android TV. Mando TV convierte tu celular o tu computador en el control remoto de tu Master G por la red WiFi de tu casa. Sirve si perdiste el control, si se le acabaron las pilas o si quieres escribir más rápido.',
    compat='Televisores Master G con Google TV, como la serie MGG (por ejemplo MGG32HFK5, MGG43FFK5 y MGG55UFKG), y con Android TV, como la serie MGAE con Android 11 (por ejemplo MGAE32F, MGAE50F y MGAE55F). Si tu Master G muestra la pantalla de inicio de Google TV o trae la tienda Google Play, Mando TV lo maneja. Los Master G más antiguos con otro sistema todavía no son compatibles.',
    funciones=_FUNCIONES_GTV, pasos=_PASOS_GTV('Master G'), encender=_ENCENDER_GTV,
    faq=[
      ('¿Mando TV funciona con mi TV Master G?', 'Sí, si tu Master G tiene Google TV o Android TV, como las series MGG y MGAE. Los modelos más antiguos con otro sistema todavía no son compatibles.'),
      ('¿Necesito el control original para conectar el celular?', 'No. El código de 6 caracteres aparece en la pantalla y lo escribes en el celular. Solo tienes que encender el TV, con el botón del televisor si hace falta.'),
      ('¿Es gratis?', _PRECIO),
      _oficial('Master G'),
    ],
    guias=_GUIAS_GTV),

  dict(slug='es/control-remoto-kalley', nombre='Kalley', corto='Kalley', color='#e5484d',
    titulo='Control remoto para TV Kalley en tu celular | Mando TV',
    desc='Usa tu celular o PC como control remoto de tu TV Kalley con Roku TV o Google TV, por WiFi. Gratis, sin anuncios y sin cuenta.',
    h1='Control remoto para TV Kalley',
    intro='Los televisores Kalley vienen con Roku TV o con Google TV, según el modelo. Mando TV maneja los dos sistemas y convierte tu celular o tu computador en el control remoto de tu Kalley por la red WiFi de tu casa.',
    compat='Televisores Kalley con Roku TV (por ejemplo K-RTV32 y 60RQ400) y con Google TV (por ejemplo la serie G315, como 43G315, 50G315 y 55G315, y los modelos K-GTV). Si tu Kalley muestra la pantalla de inicio de Roku o de Google TV, Mando TV lo maneja.',
    funciones=_FUNCIONES_ROKU_GTV, pasos=_PASOS_ROKU_GTV('Kalley'), encender=_ENCENDER_ROKU_GTV,
    faq=[
      ('¿Mando TV funciona con mi TV Kalley?', 'Sí, con los Kalley que tienen Roku TV o Google TV.'),
      _COMO_SE,
      ('¿Es gratis?', _PRECIO),
      _oficial('Kalley'),
    ],
    guias=_GUIAS_ROKU_GTV),

  dict(slug='es/control-remoto-caixun', nombre='Caixun', corto='Caixun', color='#1ba8b5',
    titulo='Control remoto para TV Caixun en tu celular | Mando TV',
    desc='Usa tu celular o PC como control remoto de tu TV Caixun con Roku TV o Google TV, por WiFi. Gratis, sin anuncios y sin cuenta.',
    h1='Control remoto para TV Caixun',
    intro='Los televisores Caixun vienen con Roku TV o con Google TV, según el modelo. Mando TV maneja los dos sistemas y convierte tu celular o tu computador en el control remoto de tu Caixun por la red WiFi de tu casa.',
    compat='Televisores Caixun con Roku TV (por ejemplo C32V1HR, C43V1FR y C50V1UR) y con Google TV (por ejemplo C43K1FG, C55V1UG y C65V1UG). Los Caixun con Android TV también funcionan. Si tu Caixun muestra la pantalla de inicio de Roku o de Google TV, Mando TV lo maneja.',
    funciones=_FUNCIONES_ROKU_GTV, pasos=_PASOS_ROKU_GTV('Caixun'), encender=_ENCENDER_ROKU_GTV,
    faq=[
      ('¿Mando TV funciona con mi TV Caixun?', 'Sí, con los Caixun que tienen Roku TV, Google TV o Android TV.'),
      _COMO_SE,
      ('Mi Caixun Roku TV no responde al celular, ¿qué hago?', 'En el TV ve a Configuración, Sistema, Configuración avanzada del sistema, Control por apps móviles, y deja el acceso a la red en Predeterminado o Permisivo.'),
      ('¿Es gratis?', _PRECIO),
      _oficial('Caixun'),
    ],
    guias=_GUIAS_ROKU_GTV),

  dict(slug='es/control-remoto-hyundai', nombre='Hyundai', corto='Hyundai', color='#2b8cff',
    titulo='Control remoto para TV Hyundai en tu celular | Mando TV',
    desc='Usa tu celular o PC como control remoto de tu TV Hyundai con Google TV o Android TV, por WiFi. Gratis, sin anuncios y sin cuenta.',
    h1='Control remoto para TV Hyundai',
    intro='Muchos televisores Hyundai que se venden en Latinoamérica traen Google TV o Android TV. Mando TV convierte tu celular o tu computador en el control remoto de tu Hyundai por la red WiFi de tu casa.',
    compat='Televisores Hyundai con Google TV (por ejemplo HYLED3259QG, HYLED4326QG y HYLED4328G) y con Android TV. Si tu Hyundai muestra la pantalla de inicio de Google TV o trae la tienda Google Play, Mando TV lo maneja. Los Hyundai con otro sistema todavía no son compatibles.',
    funciones=_FUNCIONES_GTV, pasos=_PASOS_GTV('Hyundai'), encender=_ENCENDER_GTV,
    faq=[
      ('¿Mando TV funciona con mi TV Hyundai?', 'Sí, si tu Hyundai tiene Google TV o Android TV. Los modelos con otro sistema todavía no son compatibles.'),
      ('¿Necesito el control original para conectar el celular?', 'No. El código de 6 caracteres aparece en la pantalla y lo escribes en el celular.'),
      ('¿Es gratis?', _PRECIO),
      _oficial('Hyundai'),
    ],
    guias=_GUIAS_GTV),

  dict(slug='es/control-remoto-noblex', nombre='Noblex', corto='Noblex', color='#8f6bff',
    titulo='Control remoto para TV Noblex en tu celular | Mando TV',
    desc='Usa tu celular o PC como control remoto de tu Smart TV Noblex con Google TV o Android TV, por WiFi. Gratis, sin anuncios y sin cuenta.',
    h1='Control remoto para TV Noblex',
    intro='Los Smart TV Noblex más nuevos traen Google TV y muchos anteriores, Android TV. Mando TV convierte tu celular o tu computador en el control remoto de tu Noblex por la red WiFi de tu casa.',
    compat='Smart TV Noblex con Google TV (por ejemplo DV50X8580 y DV55X8580) y con Android TV (por ejemplo DV43X7180). Si tu Noblex muestra la pantalla de inicio de Google TV o trae la tienda Google Play, Mando TV lo maneja. Los Noblex con otro sistema todavía no son compatibles.',
    funciones=_FUNCIONES_GTV, pasos=_PASOS_GTV('Noblex'), encender=_ENCENDER_GTV,
    faq=[
      ('¿Mando TV funciona con mi Smart TV Noblex?', 'Sí, si tu Noblex tiene Google TV o Android TV. Los modelos con otro sistema todavía no son compatibles.'),
      ('¿Necesito el control original para conectar el celular?', 'No. El código de 6 caracteres aparece en la pantalla y lo escribes en el celular.'),
      ('¿Es gratis?', _PRECIO),
      _oficial('Noblex'),
    ],
    guias=_GUIAS_GTV),

  dict(slug='es/control-remoto-bgh', nombre='BGH', corto='BGH', color='#22b07d',
    titulo='Control remoto para TV BGH en tu celular | Mando TV',
    desc='Usa tu celular o PC como control remoto de tu Smart TV BGH con Google TV o Android TV, por WiFi. Gratis, sin anuncios y sin cuenta.',
    h1='Control remoto para TV BGH',
    intro='Los Smart TV BGH traen Android TV o, en los modelos más nuevos, Google TV. Mando TV convierte tu celular o tu computador en el control remoto de tu BGH por la red WiFi de tu casa.',
    compat='Smart TV BGH con Android TV (por ejemplo B4325FS5A) y con Google TV, como los QLED 4K de 50 y 60 pulgadas. Si tu BGH muestra la pantalla de inicio de Google TV o trae la tienda Google Play, Mando TV lo maneja. Los BGH con otro sistema todavía no son compatibles.',
    funciones=_FUNCIONES_GTV, pasos=_PASOS_GTV('BGH'), encender=_ENCENDER_GTV,
    faq=[
      ('¿Mando TV funciona con mi Smart TV BGH?', 'Sí, si tu BGH tiene Android TV o Google TV. Los modelos con otro sistema todavía no son compatibles.'),
      ('¿Necesito el control original para conectar el celular?', 'No. El código de 6 caracteres aparece en la pantalla y lo escribes en el celular.'),
      ('¿Es gratis?', _PRECIO),
      _oficial('BGH'),
    ],
    guias=_GUIAS_GTV),
]

for _m in MARCAS_LATAM:
    assert len(_m['titulo']) <= 60, (_m['slug'], len(_m['titulo']))
    assert len(_m['desc']) <= 160, (_m['slug'], len(_m['desc']))
    assert 'Pro)' not in repr(_m) and 'función Pro' not in repr(_m), _m['slug']
