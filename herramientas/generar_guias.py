# Genera las páginas guía de mandotv.app (/guias/<tema>/index.html). Mismo patrón que generar_marcas.py.
# Uso: python -I herramientas/generar_guias.py <carpeta del sitio>
import json, os, html, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.dont_write_bytecode = True
import idiomas_sitio

SITIO = sys.argv[1]
URL = 'https://mandotv.app'
FECHA = '2026-11-15'
TIENDA = 'https://apps.microsoft.com/detail/9N3D7T1DP2SW?mode=direct'
TIENDA_APPLE = 'https://apps.apple.com/app/id6834927348'

MARCAS_ENLACES = [
  ('control-remoto-samsung', 'Control remoto Samsung'),
  ('control-remoto-lg', 'Control remoto LG'),
  ('control-remoto-roku', 'Control remoto Roku'),
  ('control-remoto-android-tv', 'Control remoto Android TV'),
  # 2026-11-21: marcas de Latinoamérica (generar_marcas.py + marcas_latam.py)
  ('control-remoto-master-g', 'Control remoto Master G'),
  ('control-remoto-kalley', 'Control remoto Kalley'),
  ('control-remoto-caixun', 'Control remoto Caixun'),
  ('control-remoto-hyundai', 'Control remoto Hyundai'),
  ('control-remoto-noblex', 'Control remoto Noblex'),
  ('control-remoto-bgh', 'Control remoto BGH'),
]

GUIAS = [
  dict(slug='guias/encender-tv-lg-con-el-celular', corto='Encender TV LG con el celular',
    titulo='Cómo encender tu TV LG con el celular | Mando TV',
    desc='Aprende a encender tu TV LG con el celular por WiFi: activa "Encender TV con móvil" en el televisor y usa Mando TV. Paso a paso, gratis y sin anuncios.',
    h1='Cómo encender el TV LG con el celular',
    intro='Se puede, pero primero hay que activar una opción en el televisor. Una vez hecho, tu celular enciende el TV LG por la red WiFi, sin el control remoto. Son cinco minutos y lo haces una sola vez.',
    pasos=[
      'Conecta el celular y el TV LG a la misma red WiFi.',
      'En el TV, abre Configuración y busca "Encender TV con móvil". Según el modelo está en General o en Conexión.',
      'Activa "Encender a través de Wi-Fi". Si tu TV está conectado con cable de red, activa "Encender a través de cable".',
      'Si tu TV tiene "Quick Start+", actívalo también.',
      'Con el TV encendido, abre Mando TV en el celular y toca tu TV LG en la lista. Acepta el aviso que aparece en la pantalla. Así la app aprende a despertarlo.',
      'Apaga el TV y pruébalo: toca el TV en Mando TV y la app te pregunta si quieres encenderlo.',
    ],
    extra=[
      ('Si no enciende', 'El TV debe haber estado conectado a la misma red WiFi cuando se apagó. Revisa que la opción siga activada y que el celular esté en esa misma red. Si cambiaste de router, vuelve a conectarte una vez con el TV encendido.'),
    ],
    marca=('control-remoto-lg', 'Control remoto para TV LG'),
    faq=[
      ('¿Puedo encender el TV LG con el celular si nunca lo conecté?', 'No. Primero hay que activar "Encender TV con móvil" en el televisor y conectarse una vez con Mando TV con el TV encendido.'),
      ('¿Necesito la app LG ThinQ?', 'No. Mando TV se conecta directo por tu WiFi y no pide cuenta de LG.'),
      ('¿Funciona con el celular con datos móviles?', 'No. El celular y el TV deben estar en la misma red WiFi.'),
    ]),
  dict(slug='guias/control-remoto-samsung-sin-control', corto='TV Samsung sin control',
    titulo='¿Perdiste el control Samsung? Usa tu celular | Mando TV',
    desc='Si perdiste el control de tu TV Samsung o no funciona, usa tu celular como control remoto por WiFi. Pasos simples con Mando TV, gratis y sin anuncios.',
    h1='Control remoto Samsung sin el control original',
    intro='Si perdiste el control del TV Samsung o dejó de funcionar, puedes usar tu celular como control por WiFi. Sirve en televisores Samsung con Tizen, de 2016 en adelante.',
    pasos=[
      'Enciende el TV con el botón físico. En la mayoría de los modelos está abajo o detrás, a veces como un joystick pequeño.',
      'Revisa que el TV esté conectado a tu WiFi y que el celular esté en la misma red.',
      'Abre Mando TV en el celular. Tu TV Samsung aparece solo en la lista. Tócalo.',
      'El TV pide aceptar la conexión. En la mayoría de los modelos se acepta con los botones físicos del TV o con el joystick de atrás.',
      'Listo, ya puedes usar el celular como control. Los botones, el teclado y las apps son gratis; el touchpad es función Pro.',
      'Para encenderlo la próxima vez desde el celular, ve a Configuración > General > Red > Configuración experta y activa "Encender con dispositivo móvil".',
    ],
    extra=[
      ('Si el TV no pide permiso', 'Puede que el permiso ya esté guardado o que el TV esté en otra red WiFi. Cierra Mando TV y vuelve a abrirla con el TV encendido. Si el TV es anterior a 2016, usa otro sistema y todavía no es compatible.'),
    ],
    marca=('control-remoto-samsung', 'Control remoto para TV Samsung'),
    faq=[
      ('¿Cómo acepto la conexión si no tengo el control?', 'En la mayoría de los modelos se acepta con los botones físicos del TV o con el joystick de atrás. Si tu modelo no tiene botones, escríbenos a hola@mandotv.app y te ayudamos.'),
      ('¿Mando TV pide cuenta Samsung?', 'No. Se conecta directo por tu WiFi, sin cuenta Samsung.'),
      ('¿Funciona con mi Samsung antiguo?', 'Funciona con televisores Samsung con Tizen, de 2016 en adelante.'),
    ]),
  dict(slug='guias/conectar-celular-al-tv-por-wifi', corto='Celular como control por WiFi',
    titulo='Celular como control remoto del TV por WiFi | Mando TV',
    desc='Conecta tu celular al TV por WiFi y úsalo de control remoto en Samsung, LG, Roku y Google TV. Pasos para cada marca con Mando TV, gratis y sin anuncios.',
    h1='Cómo conectar el celular al TV por WiFi para usarlo de control',
    intro='Solo necesitas que el celular y el TV estén en la misma red WiFi y una app de control. Mando TV encuentra tu televisor solo y funciona con Samsung, LG, Roku, Google TV y Android TV.',
    pasos=[
      'Conecta el celular y el TV a la misma red WiFi.',
      'Abre Mando TV. Tu televisor aparece solo en la lista. Tócalo.',
      'Acepta la conexión según tu marca (abajo está el detalle de cada una).',
      'Usa los botones o el teclado del celular para manejar el TV. El touchpad es una función Pro.',
    ],
    extra=[
      ('Samsung', 'El TV pregunta si permites la conexión. Acéptala en la pantalla la primera vez. Funciona con Tizen, de 2016 en adelante. Para encenderlo desde el celular, activa "Encender con dispositivo móvil" en Configuración > General > Red > Configuración experta.'),
      ('LG', 'El TV muestra un aviso pidiendo permiso. Acéptalo la primera vez. Para encenderlo desde el celular, busca "Encender TV con móvil" en Configuración y activa "Encender a través de Wi-Fi".'),
      ('Roku', 'Roku no pide emparejar: lo tocas en la lista y listo. Para encenderlo, activa "Inicio rápido del TV" en Configuración > Sistema > Energía.'),
      ('Google TV y Android TV', 'El TV muestra un código en la pantalla. Escríbelo en Mando TV la primera vez. Para encenderlo, busca "Wake on LAN", "Encender por red" o "Activación en red" en los ajustes.'),
    ],
    marca=None,
    faq=[
      ('¿Necesito internet para usar el celular como control?', 'Necesitas que el celular y el TV estén en la misma red WiFi. Mando TV se conecta directo a tu TV por esa red.'),
      ('¿Por qué no aparece mi TV en la lista?', 'Revisa que el TV esté encendido y que el celular no esté usando datos móviles ni otra red WiFi. Algunos routers tienen una red de invitados que separa los equipos.'),
      ('¿Puedo usar Mando TV desde iPhone o Android?', 'Sí en iPhone y iPad: ya está en App Store. También en Microsoft Store para Windows. Pronto llega a Android.'),
    ]),
  dict(slug='guias/controlar-el-tv-desde-el-pc', corto='Controlar el TV desde el PC',
    titulo='Controlar el TV desde el PC con Windows (gratis) | Mando TV',
    desc='Usa tu PC con Windows como control remoto del TV Samsung, LG, Roku o Google TV por WiFi. Botones, teclado y apps gratis; atajos del PC con Pro.',
    h1='Cómo controlar el TV desde el PC con Windows',
    intro='Si pasas el día frente al computador, no necesitas buscar el control: Mando TV para Windows maneja tu televisor Samsung, LG, Roku, Google TV o Android TV por la red WiFi de tu casa. Sirve para cambiar de app, subir el volumen o escribir en YouTube con el teclado del PC.',
    pasos=[
      'Descarga Mando TV gratis desde Microsoft Store en tu computador con Windows 10 u 11.',
      'Revisa que el computador y el TV estén en la misma red (WiFi o cable, pero del mismo router).',
      'Abre Mando TV: tu televisor aparece solo en la lista. Tócalo o haz clic en él.',
      'Acepta la conexión en la pantalla del TV la primera vez (en Google TV y Android TV escribe el código que muestra el TV).',
      'Listo: usa los botones o el teclado para escribir en el buscador del TV. El touchpad es una función Pro.',
    ],
    extra=[
      ('Atajos del teclado del PC (Pro)', 'Con Mando TV Pro manejas el TV con el teclado del computador: flechas para moverte, Enter para OK, Retroceso o Esc para volver, + y − para el volumen, M para silenciar y Espacio para pausar.'),
      ('Mini control siempre encima (Pro)', 'Deja una ventana pequeña con el control siempre visible mientras trabajas o juegas en el PC.'),
      ('Hablarle al TV desde el PC (Pro)', 'Con Mando TV Pro le das órdenes al TV con el micrófono del PC: "abre YouTube", "súbele al volumen" o "apaga en 30 minutos", dichas como te salgan. En Windows la voz se reconoce en el propio PC: no necesita internet, no tienes que cambiar nada en los ajustes de Windows y funciona en los 6 idiomas de la app. Lo que dices no sale del PC y no se guarda. Solo en procesadores muy antiguos la app recurre al dictado de Windows, que necesita "Reconocimiento de voz en línea" activado en Configuración > Privacidad y seguridad > Voz y el idioma agregado en Windows (en español sirven Español (México) o Español (España); Mando TV elige la variante sola aunque tu teclado sea de otro país). En ese caso, si falta algo, la app te avisa y abre el ajuste con un botón.'),
    ],
    marca=None,
    faq=[
      ('¿Necesito un cable o Bluetooth para controlar el TV desde el PC?', 'No. Mando TV se conecta por la red de tu casa: basta con que el PC y el TV estén en el mismo router.'),
      ('¿Funciona con cualquier TV?', 'Con Samsung con Tizen (2016 en adelante), LG con webOS, Roku y Google TV o Android TV (Sony, Philips, TCL, Hisense, Sharp, Xiaomi, Toshiba, Panasonic, Haier, Skyworth y otros).'),
      ('¿Cuánto cuesta?', 'Los botones, el teclado y el encendido por red son gratis y sin anuncios. Mando TV Pro es un pago único, sin suscripción, para funciones extra como el touchpad, los atajos del teclado del PC y el mini control.'),
      ('¿Por qué el micrófono no me entiende en Windows?', 'Revisa que la voz esté activa (es una función de Pro) y que el micrófono del PC funcione en Windows. En casi todos los PC la voz se reconoce en el propio equipo, sin internet. Solo en procesadores muy antiguos la app usa el dictado de Windows: ahí revisa que "Reconocimiento de voz en línea" esté activado en Configuración > Privacidad y seguridad > Voz y que Windows tenga agregado un idioma que admita el dictado (en español, Español (México) o Español (España), en Configuración > Hora e idioma > Idioma y región). Mando TV usa la que corresponde solo mientras escucha.'),
    ]),
  # Páginas de rescate (2026-11-17): problemas reales que reportaron los testers. Cada una lleva pasos propios.
  dict(slug='guias/roku-no-responde-al-celular', corto='Roku no responde al celular', fecha='2026-11-17',
    titulo='Roku no responde al celular: error 403 | Mando TV',
    desc='Tu celular se conecta al Roku pero las teclas no hacen nada. Activa "Control por apps móviles" en el Roku en 5 pasos.',
    h1='Roku no responde al control del celular: la solución',
    intro='Si tu celular encuentra el Roku y se conecta, pero ninguna tecla hace nada, casi siempre es un ajuste del propio Roku que bloquea las apps de control. En las versiones recientes de Roku viene más restringido. Se arregla en un minuto desde el menú del Roku.',
    pasos=[
      'En el Roku, pulsa Inicio y entra en Configuración.',
      'Abre Sistema y luego Configuración avanzada del sistema.',
      'Entra en "Control por apps móviles". En algunos modelos se llama "Control externo".',
      'En "Acceso a la red" elige Predeterminado o Permisivo. Si en tu modelo es solo un interruptor, déjalo en Habilitado.',
      'Vuelve a Mando TV en el celular y toca tu Roku. Las teclas ya responden.',
    ],
    extra=[
      ('Cómo saber si este es tu problema', 'La señal es clara: el celular ve el Roku en la lista y se conecta, pero al tocar una tecla no pasa nada. Por dentro, el Roku contesta con el error 403, que significa "prohibido". Mando TV lo detecta al conectar y te muestra estos mismos pasos en la pantalla.'),
      ('Predeterminado o Permisivo, ¿cuál elijo?', 'Con Predeterminado alcanza: acepta las órdenes que llegan desde la red de tu casa, que es lo que necesita un control remoto. Permisivo es más abierto y solo hace falta en redes poco comunes.'),
      ('Si no tienes el control del Roku', 'Cuando el ajuste está en Deshabilitado, solo se puede cambiar con el control físico del Roku. Pide uno prestado para cambiarlo una sola vez; después ya puedes usar el celular para todo.'),
    ],
    marca=('control-remoto-roku', 'Control remoto para Roku'),
    faq=[
      ('¿Por qué mi Roku dejó de responder si antes funcionaba?', 'Una actualización del Roku puede dejar ese ajuste más restringido. No es una falla del celular ni del WiFi: basta con volver a permitir el control por apps.'),
      ('¿Sirve para Roku TV y para los reproductores Roku?', 'Sí. El ajuste está en el mismo menú en los reproductores Roku y en los televisores con Roku TV.'),
      ('¿Es seguro dejarlo en Predeterminado?', 'Sí. Solo acepta órdenes de aparatos conectados a la red de tu casa.'),
    ]),
  dict(slug='guias/el-celular-no-encuentra-el-tv', corto='El celular no encuentra el TV', fecha='2026-11-17',
    titulo='El celular no encuentra el TV: 6 cosas a revisar | Mando TV',
    desc='Si la app no encuentra tu TV o se corta al conectar, revisa el WiFi, la VPN y el permiso de red local. Paso a paso para Samsung, LG, Roku y Android TV.',
    h1='El celular no encuentra el TV: qué revisar',
    intro='Abres la app de control y la lista sale vacía, o el TV aparece pero se corta al conectar. Casi siempre es la red, no el televisor. Revisa estos puntos en orden: el primero resuelve la mayoría de los casos.',
    pasos=[
      'Mira a qué WiFi está conectado el celular y a cuál el TV. Tiene que ser la misma red, con el mismo nombre. La red de invitados no sirve, porque separa los aparatos entre sí.',
      'Apaga la VPN del celular, si usas una. Con la VPN encendida el celular sale por otra red y no ve los aparatos de tu casa, o corta la conexión a los pocos segundos.',
      'Desactiva los datos móviles un momento. Algunos teléfonos se pasan solos del WiFi a los datos cuando la señal es débil.',
      'Enciende el TV y espera a que termine de arrancar. Un TV apagado no responde a la búsqueda.',
      'En el iPhone, revisa que la app tenga permiso de Red local: Ajustes > Privacidad y seguridad > Red local.',
      'Si todavía no aparece, agrégalo a mano: en Mando TV toca "Agregar por IP" y escribe la dirección IP del televisor.',
    ],
    extra=[
      ('Deja que la app te guíe', 'En la lista de televisores toca el botón "¿No aparece tu TV?". La app revisa paso a paso las causas más comunes (la misma red WiFi, una VPN, el permiso de red local y más) y, después de cada arreglo, tienes un botón "Volver a comprobar". Es gratis.'),
      ('Dónde ver la dirección IP del TV', 'Está en el menú de red del televisor y cambia un poco según el modelo. En LG: Configuración > Red > Conexión Wi-Fi, en los ajustes avanzados. En Samsung: Configuración > General > Red > Estado de red > Configuración de IP. En Roku: Configuración > Red > Acerca de. En Android TV y Google TV: Configuración > Red e Internet, tocando tu red. Es un número como 192.168.1.86.'),
      ('Si aparece pero se corta al conectar', 'Cuando la conexión se cae a los pocos segundos, el corte suele venir del teléfono: una VPN, un cambio de red WiFi o el ahorro de batería. Apaga la VPN, quédate en el mismo WiFi y vuelve a intentar.'),
      ('WiFi de 2,4 y de 5 GHz', 'No importa que el celular esté en la red de 5 GHz y el TV en la de 2,4, siempre que las dos salgan del mismo router. Si tienes un repetidor y el TV sigue sin aparecer, acerca el celular al router principal y prueba de nuevo.'),
    ],
    marca=None,
    faq=[
      ('¿Puedo controlar el TV con datos móviles?', 'No. El control viaja por la red WiFi de tu casa, así que el celular y el TV deben estar en la misma red.'),
      ('¿Por qué con la VPN no funciona?', 'Porque la VPN manda todo el tráfico del celular por otra red y el teléfono deja de ver los aparatos de tu casa. Apágala mientras usas el control.'),
      ('¿Sirve el Bluetooth o el infrarrojo?', 'Para los televisores inteligentes, Mando TV usa el WiFi. El infrarrojo funciona solo en celulares Android que tengan emisor infrarrojo y sirve para televisores que no son inteligentes. El Bluetooth está disponible en beta y gratis, solo en Android 9 o más reciente: el celular se conecta al TV como teclado y control Bluetooth, sin WiFi. Sirve con Google TV, Android TV y Fire TV; con otras marcas que aceptan teclados Bluetooth podría funcionar, y Roku no los acepta.'),
    ]),
  dict(slug='guias/android-tv-codigo-de-emparejamiento', corto='Código de Android TV', fecha='2026-11-17',
    titulo='Android TV pide un código de emparejamiento | Mando TV',
    desc='Tu Android TV o Google TV muestra un código de 6 caracteres al conectar el celular. Cómo escribirlo, qué hacer si no aparece o si dice que es incorrecto.',
    h1='Android TV pide un código para conectar el celular: qué hacer',
    intro='La primera vez que conectas el celular a un Android TV o Google TV, el televisor muestra un código de 6 caracteres en la pantalla. Es normal y pasa una sola vez: sirve para que nadie más controle tu TV. Aquí está cómo escribirlo y qué hacer si no aparece.',
    pasos=[
      'Enciende el TV y deja a la vista la pantalla de inicio.',
      'Abre Mando TV en el celular, conectado al mismo WiFi que el TV, y toca tu televisor en la lista.',
      'Mira la pantalla del TV: aparece un código de 6 letras y números.',
      'Escríbelo en el celular tal como sale y toca Emparejar. Las letras solo van de la A a la F, así que un círculo siempre es el número cero.',
      'Listo. El TV recuerda tu celular y no vuelve a pedir el código.',
    ],
    extra=[
      ('Si el código no aparece en el TV', 'Revisa que el TV esté encendido de verdad y no en reposo, y que el celular esté en el mismo WiFi. Vuelve a tocar el televisor en el celular. Si sigue sin salir, reinicia el TV: desenchúfalo diez segundos, enchúfalo y repite.'),
      ('Si dice que el código es incorrecto', 'El código cambia cada vez que se pide. Si tardaste o lo pediste dos veces, vale solo el último que está en la pantalla. Vuelve a tocar el TV en el celular y escribe el código nuevo.'),
      ('Si el TV vuelve a pedir el código', 'Pasa cuando el TV se restablece de fábrica o cuando borras los datos de la app en el celular. Empareja otra vez y queda guardado.'),
    ],
    marca=('control-remoto-android-tv', 'Control remoto para Android TV'),
    faq=[
      ('¿Qué televisores usan este código?', 'Los que traen Android TV o Google TV: Sony, Philips, TCL, Hisense, Sharp, Xiaomi, el Chromecast con Google TV y varios más.'),
      ('¿Necesito una cuenta de Google en el celular?', 'No. El código de la pantalla es lo único que hace falta.'),
      ('¿Es seguro?', 'Sí. El código demuestra que estás frente al TV: sin verlo en la pantalla nadie puede emparejarse.'),
    ]),
  dict(slug='guias/perdi-el-control-del-roku', corto='Perdí el control del Roku', fecha='2026-11-17',
    titulo='Perdí el control del Roku: usa tu celular | Mando TV',
    desc='Si perdiste el control del Roku, tu celular lo reemplaza por WiFi. Pasos simples, y qué hacer si cambiaste de router y el Roku quedó sin conexión.',
    h1='Perdí el control del Roku: cómo usar el celular',
    intro='Si se te perdió el control del Roku o dejó de funcionar, el celular lo reemplaza, siempre que el Roku siga conectado a tu WiFi. Y si cambiaste de WiFi o de router, también hay una salida.',
    pasos=[
      'Antes de nada, intenta hacer sonar el control. Si tu control Roku tiene parlante (por ejemplo el Roku Voice Remote Pro), abre Mando TV, conéctate al Roku y usa la opción para hacer sonar el control, así lo encuentras. Solo funciona con controles Roku que tengan parlante y con el Roku encendido.',
      'Enciende el televisor y deja el Roku enchufado. No hace falta tocar nada en él.',
      'Conecta el celular al mismo WiFi que usa el Roku.',
      'Abre Mando TV. El Roku aparece solo en la lista. Tócalo.',
      'Usa las flechas, OK, Inicio y Atrás como en el control de siempre. El Roku no pide código.',
      'Si las teclas no hacen nada, el Roku tiene bloqueado el control por apps: la guía "Roku no responde al control del celular", más abajo, explica cómo permitirlo.',
    ],
    extra=[
      ('Si el Roku quedó sin WiFi (cambiaste de router o te mudaste)', 'Sin el control no puedes entrar al menú para ponerle la red nueva, pero hay un truco: el Roku se conecta solo a una red que tenga el mismo nombre y la misma clave que la anterior. Crea en otro teléfono una zona WiFi con ese nombre y esa clave exactos, conecta a ella el celular que tiene Mando TV y el Roku aparecerá en la lista. Desde ahí entra en Configuración > Red y conéctalo al WiFi nuevo.'),
      ('Si es un Roku TV', 'Los televisores con Roku TV tienen un botón físico, casi siempre abajo al centro o detrás, que enciende el TV. Con eso basta para encenderlo y seguir con el celular.'),
      ('Si prefieres comprar otro control', 'Fíjate que sea compatible con tu modelo. Los reproductores Roku pequeños que quedan escondidos detrás del TV necesitan un control que no sea de infrarrojo, porque el infrarrojo no les llega.'),
    ],
    marca=('control-remoto-roku', 'Control remoto para Roku'),
    faq=[
      ('¿El celular puede encender el Roku?', 'Un reproductor Roku enchufado está siempre encendido. Si es un Roku TV, Mando TV lo enciende por WiFi cuando el televisor tiene activado "Inicio rápido de TV" en Configuración > Sistema > Energía.'),
      ('¿Y el volumen?', 'En un Roku TV el celular sube y baja el volumen. En un reproductor Roku conectado por HDMI depende del televisor: en muchos funciona y en otros no.'),
      ('¿Tengo que crear una cuenta?', 'No. Mando TV no pide cuenta y además controla televisores Samsung, LG y Android TV desde la misma app.'),
    ]),
  dict(slug='guias/encender-tv-y-hdmi-de-la-consola-sin-control', corto='TV y consola sin control', fecha='2026-11-17',
    titulo='Encender el TV y cambiar a HDMI sin control (PS5, Xbox)',
    desc='¿Día de jugar GTA VI y sin control del TV? Enciende la tele y pasa al HDMI de tu PS5 o Xbox desde el celular. Gratis y sin anuncios.',
    modificada='2026-11-17',
    alternos={'es': URL + '/guias/encender-tv-y-hdmi-de-la-consola-sin-control/',
              'en': URL + '/en/guides/turn-on-tv-console-hdmi-without-remote/',
              'pt': URL + '/pt/guias/ligar-tv-e-hdmi-do-console-sem-controle/'},
    h1='Cómo encender el TV y cambiar al HDMI de la consola sin el control',
    intro='El estreno de GTA VI (o GTA 6, como lo buscan muchos), la consola lista y el control del televisor perdido entre los cojines. Pasa más de lo que parece. Con Mando TV el celular enciende el televisor y lo cambia al HDMI de tu PlayStation o Xbox, por el WiFi de tu casa.',
    pasos=[
      'Conecta el celular al mismo WiFi que el televisor.',
      'Abre Mando TV y toca tu televisor en la lista (Samsung, LG, Roku o Android TV).',
      'Si el TV está apagado, toca Encender. Funciona si el televisor tiene activado el encendido por red; si nunca lo activaste, enciéndelo esta vez con el botón del propio TV y actívalo para la próxima.',
      'Enciende la consola. Si tienes activado HDMI-CEC (el truco de más abajo), el televisor cambia solo a su entrada.',
      'Si no cambia solo, toca Entradas en Mando TV y elige el HDMI donde está la consola (HDMI 1, HDMI 2...).',
      'Para el volumen, usa los botones grandes de la app mientras juegas.',
    ],
    extra=[
      ('El truco gratis: que la consola cambie el TV sola', 'La PS5 y la Xbox pueden encender el televisor y pasarlo a su HDMI apenas se encienden, gracias a HDMI-CEC. En la PS5 está en Configuración > Sistema > HDMI > Activar Enlace de dispositivos HDMI. En la Xbox, en Configuración > General > Opciones de TV y pantalla > Control de dispositivos. En el televisor tiene otro nombre según la marca: Anynet+ en Samsung, SIMPLINK en LG y Control de dispositivos HDMI o BRAVIA Sync en otras.'),
      ('Si es un Roku TV', 'El botón físico del televisor, casi siempre abajo al centro o detrás, lo enciende. Desde ahí el celular hace el resto.'),
      ('Si el TV se queda en otra pantalla', 'Si la consola está encendida pero el televisor sigue en la antena o en una app, el TV no cambió de entrada. Con el celular, toca Entradas y elige el HDMI de la consola. Si prefieres, usa las flechas y OK para llegar a las entradas del TV, o el botón del propio televisor, y elige el HDMI. El número es el del puerto donde enchufaste el cable de la consola.'),
      ('Más ayuda', 'Si no sabes por dónde empezar, mira [Perdí el control del TV](/guias/perdi-el-control-del-tv/). Para solo cambiar de entrada, está la guía [Cambiar la entrada HDMI del TV sin control remoto](/guias/cambiar-entrada-hdmi-sin-control/).'),
    ],
    marca=None,
    faq=[
      ('¿Mando TV tiene algo que ver con GTA VI?', 'No. Mando TV no está afiliado a Rockstar Games ni a Take-Two. Solo te ayuda a que no te quedes sin jugar por no encontrar el control del televisor.'),
      ('¿Cambiar de entrada HDMI es gratis?', 'Sí. La lista de entradas de Mando TV es gratis, igual que encender el TV y usar las flechas, OK y el volumen. Además puedes dejar que la consola cambie la entrada sola con HDMI-CEC.'),
      ('¿Sirve con cualquier televisor?', 'Con televisores Samsung, LG, Roku y Android TV conectados al mismo WiFi. Si el tuyo es de otra marca, el truco de HDMI-CEC igual te sirve.'),
      ('¿Sirve para jugar GTA VI o GTA 6 en PS5 y Xbox?', 'Mando TV no toca la consola ni el juego. Solo deja el televisor encendido y en el HDMI correcto para que te sientes a jugar.'),
      ('¿Y si el TV no se enciende desde el celular?', 'Enciéndelo esta vez con el botón del propio TV y activa el encendido por red para la próxima. La guía de tu marca explica dónde está ese ajuste.'),
    ]),
  dict(slug='guias/perdi-el-control-del-tv', corto='Perdí el control del TV', fecha='2026-11-17',
    titulo='Perdí el control del TV: qué hacer ahora (paso a paso)',
    desc='¿Perdiste el control del TV? Enciéndelo con su botón y úsalo desde el celular. Pasos para LG, Samsung, Roku y Android TV. Gratis y sin anuncios.',
    h1='Perdí el control del TV: qué puedo hacer',
    intro='Pasa en todas las casas: el control no aparece justo cuando quieres ver algo. La buena noticia es que tu celular puede hacer de control, por el WiFi de la casa. Aquí está lo que tienes que hacer, en orden.',
    pasos=[
      'Enciende el TV con su botón físico. Casi siempre está abajo, al centro, o detrás en una esquina. A veces es un botón solo y a veces un joystick pequeño.',
      'Conecta el celular al mismo WiFi que el TV.',
      'Descarga Mando TV, que es gratis y no pide cuenta, y ábrela. Tu TV aparece solo en la lista. Tócalo.',
      'Acepta la conexión según tu marca. En LG y Samsung el TV muestra un aviso: se acepta con el botón o el joystick del propio TV. En Android TV y Google TV escribes un código de 6 caracteres que sale en la pantalla. En Roku no pide nada.',
      'Listo. Las flechas, OK, Atrás, Inicio, el volumen, los canales y el teclado son gratis.',
      'Para la próxima vez, activa el encendido por red en el TV (más abajo está la guía de tu marca) y lo enciendes desde el celular sin tocar el TV.',
    ],
    extra=[
      ('Elige la guía de tu marca', 'LG: [Perdí el control del TV LG](/guias/perdi-el-control-del-lg/). Samsung: [Control remoto Samsung sin el control original](/guias/control-remoto-samsung-sin-control/). Roku: [Perdí el control del Roku](/guias/perdi-el-control-del-roku/). Android TV y Google TV: [Android TV sin control remoto](/guias/android-tv-sin-control-remoto/).'),
      ('Si el TV no enciende con el botón', 'Antes de buscar otro control, revisa que el cable esté bien enchufado y que el enchufe de la pared tenga corriente. Si el botón del TV no hace nada, el problema es del televisor y no del control.'),
      ('Si el control solo dejó de funcionar', 'Prueba con pilas nuevas. Para saber si todavía manda señal, apúntalo a la cámara del celular y aprieta un botón: en muchos celulares se ve una luz morada en la pantalla. Si la luz sale y el TV no responde, el sensor del TV puede estar tapado.'),
      ('Si cambiaste de router y el TV quedó sin WiFi', 'Sin control es más difícil conectarlo a la red nueva. Lo más fácil es conectar el TV con un cable de red al router. También puedes crear una red WiFi con el mismo nombre y la misma clave de antes: el TV suele conectarse solo a ella.'),
      ('Lo gratis y lo Pro', 'Encender, apagar, flechas, OK, volumen, canales, números, teclado, abrir apps y cambiar de entrada son gratis. El touchpad, la voz y las rutinas son de Mando TV Pro, un pago único sin suscripción.'),
    ],
    marca=None,
    faq=[
      ('¿Puedo encender el TV con el celular si nunca lo conecté antes?', 'Esta primera vez, enciéndelo con el botón del TV. Después de conectar el celular y activar el encendido por red en el TV, ya puedes encenderlo desde la app.'),
      ('¿Necesito comprar un control nuevo?', 'No necesariamente. Con Mando TV tienes botones, volumen, teclado y encendido gratis. Si igual prefieres uno físico, busca el modelo exacto de tu TV.'),
      ('¿Funciona si el TV no tiene WiFi?', 'No. El celular y el TV tienen que estar en la misma red WiFi. Un TV que no es smart no se puede controlar con Mando TV.'),
    ]),
  dict(slug='guias/perdi-el-control-del-lg', corto='Perdí el control del TV LG', fecha='2026-11-17',
    titulo='Perdí el control del TV LG: cómo usar el celular',
    desc='¿Sin el control de tu TV LG? Enciéndelo con el botón, acepta el aviso y usa el celular de control por WiFi. Sin cuenta LG y sin anuncios.',
    h1='Perdí el control del TV LG: cómo usar el celular',
    intro='Si perdiste el Magic Remote o el control del TV LG dejó de funcionar, el celular lo reemplaza por WiFi. Sirve en los LG con webOS, que son casi todos los Smart TV LG desde 2014. No necesitas cuenta LG ni la app ThinQ.',
    pasos=[
      'Enciende el TV con el botón de abajo, bajo el logo de LG, o el que está detrás. En muchos modelos funciona como joystick: se presiona para abrir el menú y se mueve para elegir.',
      'Conecta el celular al mismo WiFi que el TV.',
      'Abre Mando TV y toca tu TV LG en la lista.',
      'El TV muestra un aviso pidiendo permiso. Acéptalo con el joystick o el botón del TV. Si ya habías conectado ese celular antes, no lo vuelve a pedir.',
      'Listo. Las flechas, OK, Atrás, Inicio, volumen, canales y teclado son gratis. El puntero es función Pro.',
      'Con la app conectada, entra en Configuración con las flechas y OK, y activa "Encender TV con móvil". La guía [Cómo encender el TV LG con el celular](/guias/encender-tv-lg-con-el-celular/) dice dónde está.',
    ],
    extra=[
      ('Si el TV no muestra el aviso', 'Puede que el permiso ya esté guardado, o que el celular esté en otra red. Revisa que los dos estén en el mismo WiFi y que la VPN esté apagada. Si el TV no aparece en la lista, mira [El celular no encuentra el TV](/guias/el-celular-no-encuentra-el-tv/).'),
      ('Si el TV quedó sin WiFi', 'Conecta el TV con un cable de red al router: lo usa solo. O crea una red WiFi con el mismo nombre y la misma clave de antes, porque el TV suele conectarse solo a ella.'),
      ('Si el TV quedó en otra entrada', 'Con el celular, toca Entradas y elige el HDMI. Más detalles en [Cambiar la entrada HDMI del TV sin control remoto](/guias/cambiar-entrada-hdmi-sin-control/).'),
    ],
    marca=('control-remoto-lg', 'Control remoto para TV LG'),
    faq=[
      ('¿Necesito el Magic Remote para usar Mando TV?', 'Solo hace falta algo para aceptar el aviso la primera vez, y sirve el botón o el joystick del propio TV. Después usas solo el celular.'),
      ('¿Necesito la app LG ThinQ?', 'No. Mando TV se conecta directo por tu WiFi y no pide cuenta de LG.'),
      ('¿Puedo apagar y encender el TV LG desde el celular?', 'Apagar sí. Para encender necesitas haber activado "Encender TV con móvil" en el televisor y haberte conectado una vez con el TV encendido.'),
    ]),
  dict(slug='guias/cambiar-entrada-hdmi-sin-control', corto='Cambiar HDMI sin control', fecha='2026-11-17',
    titulo='Cambiar la entrada HDMI del TV sin control remoto',
    desc='Cambia a HDMI sin control remoto en Samsung, LG o Roku: con el botón del TV o desde el celular. Gratis para empezar, sin anuncios.',
    h1='Cambiar la entrada HDMI del TV sin control remoto',
    intro='La consola o el reproductor están listos, pero el TV sigue en otra entrada y el control no aparece. Se puede cambiar de dos formas: con el botón del propio TV o desde el celular. Aquí van los pasos para Samsung, LG y Roku.',
    pasos=[
      'Prueba lo más simple: enciende la consola o el reproductor. Si el TV tiene HDMI-CEC activado (Anynet+ en Samsung, SIMPLINK en LG), cambia solo a esa entrada.',
      'Si no cambia, usa el botón del propio TV, abajo al centro o detrás. En muchos Samsung y LG funciona como joystick y abre un menú con Fuente o Entradas.',
      'Elige la entrada en ese menú: HDMI 1, HDMI 2 y así. El número es el del puerto donde está enchufado el cable.',
      'Si prefieres el celular, conéctalo al mismo WiFi, abre Mando TV y toca tu TV.',
      'En LG y Roku, toca Entradas y elige el HDMI. En Samsung, Entradas manda la tecla Fuente del TV y eliges con las flechas y OK.',
      'También puedes usar las flechas y OK para ir a las entradas de la pantalla de inicio del TV. Según la marca y el año, se llaman Fuente, Dispositivos conectados o Entradas. En un Roku TV son las tarjetas HDMI de la pantalla de inicio.',
    ],
    extra=[
      ('Samsung', 'Si el menú del botón del TV no tiene Fuente, abre el menú de la pantalla de inicio con el celular y busca Fuente o Dispositivos conectados a la izquierda. Se maneja con las flechas y OK de Mando TV, que son gratis.'),
      ('LG', 'Presiona el joystick del TV y busca Entradas. Con el celular, en Mando TV también puedes abrir la lista de entradas y tocar la que quieras.'),
      ('Roku TV', 'En la pantalla de inicio hay una tarjeta por cada entrada, como HDMI 1 o HDMI 2. Muévete con las flechas y entra con OK, gratis.'),
      ('Si es un TV con Android TV o Google TV', 'En Mando TV la lista de entradas todavía no está en Android TV. Usa el botón de entradas del propio TV, o llega a ellas con las flechas y OK desde el inicio. Si no tienes control y quieres conectarlo, mira [Android TV sin control remoto](/guias/android-tv-sin-control-remoto/).'),
      ('Más ayuda', 'Si el TV ni siquiera enciende o no sabes por dónde empezar, mira [Perdí el control del TV](/guias/perdi-el-control-del-tv/). Para jugar en consola, la guía [Encender el TV y cambiar a HDMI sin control](/guias/encender-tv-y-hdmi-de-la-consola-sin-control/) incluye el truco de HDMI-CEC.'),
    ],
    marca=None,
    faq=[
      ('¿Cambiar de entrada HDMI es gratis?', 'Sí. La lista de entradas de Mando TV es gratis, igual que encender el TV y usar flechas, OK y volumen. También puedes llegar a las entradas desde el menú del TV.'),
      ('¿Cómo sé cuál HDMI usar?', 'Mira los puertos HDMI del TV: cada uno tiene un número. Usa el del puerto donde está enchufado el cable de tu consola o reproductor.'),
      ('¿Qué hago si el TV no se enciende?', 'Enciéndelo con su botón físico. Si ya lo habías conectado antes y activaste el encendido por red, también puedes encenderlo desde el celular.'),
    ]),
  dict(slug='guias/android-tv-sin-control-remoto', corto='Android TV sin control', fecha='2026-11-17',
    titulo='Android TV sin control remoto: úsalo desde el celular',
    desc='¿Sin el control de tu Android TV o Google TV? Conecta el celular con el código de 6 caracteres de la pantalla. Gratis, sin cuenta y sin anuncios.',
    h1='Android TV sin control remoto: cómo usarlo desde el celular',
    intro='Si perdiste el control de tu Android TV o Google TV, o se quedó sin pilas, el celular lo reemplaza. Lo mejor es que conectarlo no necesita el control: el TV muestra un código en la pantalla y lo escribes en el celular. Sirve en Sony, Philips, TCL, Hisense, Sharp, Xiaomi con Android TV, Chromecast con Google TV y Nvidia Shield.',
    pasos=[
      'Enciende el TV con su botón físico. Casi siempre está abajo, al centro, o detrás en una esquina.',
      'Conecta el celular al mismo WiFi que el TV.',
      'Descarga Mando TV, que es gratis y no pide cuenta de Google, y ábrela. Toca tu TV en la lista.',
      'El TV muestra un código de 6 letras y números. Escríbelo en el celular y toca Emparejar. No necesitas el control para esto.',
      'Ya puedes usar las flechas, OK, Atrás, Inicio, volumen, silencio y teclado. Son gratis, igual que la lista de apps. El touchpad es Pro.',
      'Para encenderlo desde el celular la próxima vez, busca "Wake on LAN", "Encender por red" o "Activación remota" en los ajustes de red o de energía del TV.',
    ],
    extra=[
      ('Si tu TV no se enciende desde el celular', 'No todos los Android TV traen encendido por red; depende del fabricante y del modelo. Si el tuyo no lo tiene, enciéndelo con el botón del TV y sigue desde el celular. Apagarlo sí lo puedes hacer desde la app.'),
      ('Chromecast con Google TV, Google TV Streamer y Shield', 'Se conectan igual: mismo WiFi, tocas el aparato en la lista y escribes el código. Si el TV muestra otra entrada, cámbiala al HDMI donde está conectado, como explica [Cambiar la entrada HDMI del TV sin control remoto](/guias/cambiar-entrada-hdmi-sin-control/).'),
      ('Si el código no aparece o dice que es incorrecto', 'Revisa que el TV esté encendido de verdad y no en reposo. El código cambia cada vez que se pide: vale solo el último. Hay más detalles en [Android TV pide un código para conectar el celular](/guias/android-tv-codigo-de-emparejamiento/).'),
      ('App de Google o Mando TV', 'Google tiene su propia app con cuenta de Google. Mando TV no pide cuenta, funciona también desde Windows y maneja además televisores LG, Samsung y Roku desde la misma app.'),
    ],
    marca=('control-remoto-android-tv', 'Control remoto para Android TV y Google TV'),
    faq=[
      ('¿Necesito el control para emparejar el celular?', 'No. El código aparece en la pantalla del TV y lo escribes en el celular. Solo tienes que encender el TV, con el botón del televisor si hace falta.'),
      ('¿Sirve con un Hisense?', 'Con los Hisense que traen Android TV o Google TV, sí. Los Hisense con otro sistema no son compatibles.'),
      ('¿Puedo escribir con el teclado del celular?', 'Sí. El teclado es gratis y sirve para buscar en YouTube, Netflix y el resto de las apps.'),
    ]),
]


# >>> guías traídas del inglés (ensamblar.py)
# Adaptadas con Ollama (qwen3.6:35b) desde las guías inglesas y auditadas por Opus el 22-nov. Rutas en idiomas_sitio.py.
GUIAS += [
  dict(slug='guias/app-control-remoto-sin-suscripcion', corto='Control remoto sin suscripción', fecha='2026-11-23',
    titulo='App de control remoto sin suscripción ni anuncios',
    desc='¿Cansado de apps de control remoto con anuncios o suscripción semanal? Mando TV es gratis y sin anuncios, y Pro es un pago único opcional.',
    h1='Control remoto para el TV sin suscripción ni anuncios',
    intro='Muchas apps de control remoto muestran un anuncio cada pocos toques o piden una suscripción semanal antes de dejarte usar el control. Mando TV hace lo contrario: el control es gratis, sin anuncios y sin cuenta, y Pro, que es opcional, se paga una sola vez. Aquí está la comparación, también con lo que no hace.',
    pasos=[
      'Antes de instalar cualquier app, abre su página en la tienda y mira las compras dentro de la app. Los precios semanales o mensuales indican una suscripción.',
      'En Google Play, revisa si la ficha dice "Contiene anuncios" y lee las reseñas más recientes de pocas estrellas: ahí aparecen los cobros sorpresa.',
      'Revisa que la app funcione con tu TV por WiFi. Mando TV funciona con Samsung (2016 en adelante), LG webOS, Roku, Google TV y Android TV, y Fire TV.',
      'Instala Mando TV, conecta tu celular al mismo WiFi que el TV y toca tu TV en la lista.',
      'Acepta el aviso en el TV o escribe el código que muestra, y usa el control. Los botones, volumen, canales y teclado son gratis.',
    ],
    tabla=dict(titulo='Mando TV comparado con muchas apps de control',
      cabeza=['', 'Mando TV', 'Muchas apps con anuncios o suscripción'],
      filas=[
        ['Control básico', 'Gratis', 'A menudo gratis con anuncios, o bloqueado tras una prueba'],
        ['Anuncios', 'Ninguno', 'Comunes'],
        ['Suscripción', 'Ninguna. Pro es un pago único opcional', 'Los planes semanales o mensuales son comunes'],
        ['Cuenta', 'No hace falta', 'Varía'],
        ['Smart TV por WiFi', 'Samsung (2016 en adelante), LG webOS, Roku, Google TV y Android TV, Fire TV, Apple TV (beta)', 'Varía según la app'],
        ['Infrarrojo para televisores antiguos', 'Gratis en celulares Android con emisor infrarrojo (nuevo)', 'Algunas apps, solo en celulares con emisor infrarrojo'],
        ['Bluetooth', 'Beta en Android 9 o más reciente, gratis', 'Varía según la app'],
        ['Fotos y videos al TV', 'Pro, por WiFi (no es duplicar la pantalla)', 'Varía según la app'],
        ['Celulares y computadores', 'iPhone, iPad y Windows, y Android en prueba anticipada', 'Varía'],
        ['Duplicar la pantalla', 'Gratis en iPhone y iPad, con Duplicar pantalla del Centro de control (TV con AirPlay)', 'Algunas apps lo ofrecen'],
      ],
      nota='La comparación no apunta a ninguna app en particular. Revisa la ficha de cada app para ver sus precios actuales.'),
    extra=[
      ('Lo que Mando TV no hace', 'No tiene duplicación de pantalla propia: en el iPhone y el iPad te lleva a Duplicar pantalla, en el Centro de control, la función del propio iPhone, que sirve con televisores compatibles con AirPlay. Con Mando TV Pro también puede enviar fotos y videos al TV por el WiFi de tu casa. Controla los Smart TV por el WiFi de tu casa. Un TV que no es Smart TV se puede controlar por infrarrojo desde un celular Android con emisor infrarrojo. En Android 9 o más reciente, el celular también se conecta a Google TV, Android TV y Fire TV por Bluetooth como teclado y control, sin WiFi. Esta opción está en beta y es gratis.'),
      ('Cómo gana dinero Mando TV', 'No con anuncios ni con tus datos: la app no recopila ninguno. Mando TV se paga con Pro, un pago único opcional por extras. El control básico es gratis.'),
      ('En los dispositivos que ya tienes', 'iPhone y iPad desde la App Store, PC con Windows desde Microsoft Store, y Android con la prueba anticipada gratis de Google Play. Mira [control remoto del TV en el iPhone](/guias/app-control-remoto-para-iphone/) y [control remoto del TV en Windows](/guias/app-control-remoto-para-windows/).'),
      ('Privacidad', 'Sin cuenta ni seguimiento en la app. Se comunica con el TV dentro de la red de tu casa, y las claves de conexión con el TV quedan cifradas en tu equipo. Detalles en la [política de privacidad](/privacidad.html).'),
    ],
    marca=None,
    faq=[
      ('¿Hay una app de control remoto para el TV sin suscripción?', 'Sí. Mando TV no tiene suscripción: el control es gratis, sin anuncios, y Pro es un pago único opcional.'),
      ('¿Mando TV es realmente gratis?', 'Sí. Las flechas, OK, Atrás, Inicio, volumen, canales, teclas numéricas, teclado y encendido o apagado son gratis, sin anuncios ni límite de tiempo.'),
      ('¿Funciona sin WiFi?', 'Casi siempre no. Mando TV controla los Smart TV por el WiFi de tu casa. Hay dos excepciones: el infrarrojo en celulares Android con emisor infrarrojo, que también sirve para televisores que no son Smart TV o que nunca se conectaron al WiFi, y el Bluetooth, en beta en Android 9 o más reciente, que funciona con Google TV, Android TV y Fire TV.'),
    ]),
  dict(slug='guias/alternativa-a-la-app-de-roku', corto='Alternativa a la app de Roku', fecha='2026-11-23',
    titulo='Alternativa a la app de Roku: un control simple | Mando TV',
    desc='Una alternativa a la app de Roku para usarla como control: Mando TV controla Roku por WiFi, sin cuenta ni anuncios, y también Samsung, LG y Google TV.',
    h1='Alternativa a la app de Roku: un control para cada TV',
    intro='La app oficial de Roku hace varias cosas: tienda de canales, enviar contenido, escucha privada y control remoto. Si solo buscas un control rápido o tienes otros televisores Samsung, LG o Google TV en casa, Mando TV es una alternativa simple que controla el Roku por tu WiFi sin pedir cuenta.',
    pasos=[
      'Conecta el celular y el Roku a la misma red WiFi.',
      'Descarga y abre Mando TV. Tu Roku TV o reproductor aparece en la lista. Tócalo. El Roku no pide código.',
      'Usa las flechas, OK, Atrás, Inicio, volumen y el teclado. Escribe búsquedas en los canales de Roku con el teclado del celular.',
      'Si los botones no responden, en el Roku ve a Configuración > Sistema > Configuración avanzada del sistema > "Control por apps móviles" y en "Acceso a la red" elige Predeterminado o Permisivo (en versiones recientes del software de Roku, activa "Control por apps móviles").',
      'Opcional: en un Roku TV, activa el "Inicio rápido de TV" en Configuración > Sistema > Energía para que Mando TV pueda encenderlo.',
    ],
    extra=[
      ('Dónde destaca Mando TV', 'Una app para varios televisores: Roku, Samsung, LG y Google TV o Android TV. Sin cuenta ni anuncios. También funciona desde un PC con Windows, útil en el escritorio. Las flechas y el volumen responden rápido, y el teclado facilita escribir búsquedas.'),
      ('Dónde destaca la app oficial de Roku', 'Guarda la app de Roku para lo que ofrece más allá del control, como navegar y agregar canales desde la Tienda de canales de Roku, así como sus funciones propias para enviar contenido y de escucha privada. Usa ambas si prefieres. Las dos pueden estar en el mismo celular.'),
      ('Televisores Roku TV y reproductores Roku', 'Ambos funcionan. Incluye modelos Roku TV de TCL, Hisense, Philips y otros, y los reproductores Roku Express, Streaming Stick y Ultra. Más detalles en la [página del control remoto para Roku](/control-remoto-roku/).'),
      ('Si la app de Roku dejó de funcionar', 'Si los botones dejaron de responder, el Roku suele bloquear el control por apps. La guía [Roku no responde al celular (error 403)](/guias/roku-no-responde-al-celular/) explica el ajuste que lo soluciona.'),
      ('Qué es gratis y qué es Pro', 'Las flechas, OK, Atrás, Inicio, volumen, canales, teclas numéricas, teclado, abrir apps, cambiar entradas y encender o apagar son gratis, sin anuncios ni suscripción. Mando TV Pro es un pago único opcional para funciones extra.'),
    ],
    marca=('control-remoto-roku', 'Control remoto para Roku'),
    faq=[
      ('¿Necesito una cuenta de Roku para usar Mando TV?', 'No. Mando TV se comunica con el Roku por tu red local y no pide cuenta.'),
      ('¿Mando TV reemplaza completamente la app móvil de Roku?', 'Para el control remoto, sí. Para la tienda de canales, enviar contenido y la escucha privada, conserva la app oficial de Roku.'),
      ('¿Funciona en mi Roku Express o Streaming Stick?', 'Sí. Todos los reproductores Roku y televisores con Roku TV se controlan igual.'),
    ]),
  dict(slug='guias/alternativa-a-lg-thinq', corto='Alternativa a la app LG ThinQ', fecha='2026-11-23',
    titulo='Alternativa a LG ThinQ: control remoto del TV LG sin cuenta',
    desc='¿Buscas una alternativa a LG ThinQ solo para usar como control remoto de tu TV? Mando TV controla los TV LG con webOS por WiFi, sin cuenta de LG ni anuncios.',
    h1='Alternativa a LG ThinQ para controlar tu TV LG',
    intro='LG ThinQ es la app oficial de LG para manejar toda la casa inteligente: electrodomésticos, el televisor y más. Si solo quieres un control remoto simple para tu TV LG, Mando TV hace eso por el WiFi de tu casa, sin crear una cuenta de LG y sin anuncios.',
    pasos=[
      'Conecta el celular o el PC (iPhone, Android o Windows) y el TV LG a la misma red WiFi.',
      'Descarga Mando TV y ábrelo. Tu TV LG aparece solo en la lista. Tócalo.',
      'Aparece un aviso de permisos en la pantalla del TV. Acéptalo una vez con el control remoto, el joystick debajo de la pantalla o el Magic Remote.',
      'Usa los botones, el volumen y el teclado al instante. No se necesita cuenta de LG ni registro en el TV.',
      'Opcional: activa "Encender TV con móvil" en la configuración del TV para poder encenderlo también desde el celular.',
    ],
    extra=[
      ('Mando TV o LG ThinQ: cuál usar', 'Usa ThinQ si quieres gestionar electrodomésticos LG como una lavadora, un refrigerador o un aire acondicionado, o las funciones de la cuenta de LG. Usa Mando TV si buscas un control rápido y sencillo para el TV que también funciona con Samsung, Roku y Google TV en la misma app. Mucha gente usa las dos: ThinQ para electrodomésticos y Mando TV para el TV.'),
      ('Qué hace Mando TV en un TV LG', 'Funciona con los Smart TV LG con webOS, que son la mayoría de los modelos desde 2014, incluidos LED, NanoCell, QNED y OLED. Tiene las flechas, OK, Atrás, Inicio, volumen, canales, silencio, controles de reproducción y un teclado para escribir en YouTube, Netflix o el navegador. La lista de apps y la de entradas también son gratis. Con Pro tienes además un puntero como el del Magic Remote.'),
      ('Qué no hace Mando TV', 'No controla electrodomésticos LG, no usa tu cuenta de LG ni reemplaza los servicios de la cuenta de LG en el TV. Es un control remoto, no un centro para el hogar inteligente.'),
      ('Privacidad y anuncios', 'Mando TV no tiene anuncios ni cuenta. Se comunica con el TV dentro de la red de tu casa y guarda cifrada en tu equipo la clave de conexión con el TV. La [página del control remoto LG](/control-remoto-lg/) tiene la lista completa de funciones.'),
      ('Qué es gratis y qué es Pro', 'Las flechas, OK, Atrás, Inicio, volumen, canales, teclas numéricas, teclado, abrir apps, cambiar de entrada y encender o apagar son gratis, sin anuncios ni suscripción. Mando TV Pro es una compra única opcional para funciones adicionales.'),
    ],
    marca=('control-remoto-lg', 'Control remoto para TV LG'),
    faq=[
      ('¿Puedo controlar mi TV LG sin la app LG ThinQ?', 'Sí. Mando TV se conecta directamente a los TV LG con webOS por tu WiFi. Aceptas un aviso en el TV la primera vez y listo, sin cuenta de LG.'),
      ('¿Mando TV funciona con el puntero del Magic Remote?', 'Mando TV Pro tiene un puntero que mueves con el dedo en la pantalla del celular, tal como el Magic Remote mueve la flecha.'),
      ('¿Mando TV es de LG?', 'No. Mando TV es una app independiente y no está afiliada a LG. LG y ThinQ pertenecen a sus respectivos dueños y se nombran solo para describir la compatibilidad.'),
    ]),
  dict(slug='guias/alternativa-a-smartthings', corto='Alternativa a SmartThings para TV', fecha='2026-11-23',
    titulo='¿SmartThings no controla tu TV? Una alternativa simple',
    desc='Si el control de SmartThings falla o va lento, Mando TV controla tu TV Samsung con Tizen por WiFi, sin cuenta Samsung ni anuncios. Pasos y soluciones.',
    h1='Alternativa a SmartThings para televisores Samsung',
    intro='SmartThings es la app de Samsung para toda la casa inteligente, y su control del TV funciona con tu cuenta Samsung. Si dejó de funcionar o quieres algo rápido, Mando TV controla los televisores Samsung con Tizen, de 2016 en adelante, directo por el WiFi de tu casa y sin cuenta.',
    pasos=[
      'Conecta el celular y el TV Samsung a la misma red WiFi.',
      'Descarga y abre Mando TV. Tu TV Samsung aparece solo en la lista. Tócalo.',
      'El TV pide aceptar la conexión. Elige Permitir con el control remoto o con el botón del TV (solo la primera vez).',
      'Usa las flechas, OK, Volver, Inicio, volumen, canales y el teclado de inmediato.',
      'Opcional: activa "Encender con dispositivo móvil" en Configuración > General > Red > Configuración experta para que Mando TV también pueda encender el TV.',
    ],
    extra=[
      ('Por qué falla el control desde el celular', 'Las causas habituales son simples: el celular y el TV están en redes WiFi distintas, hay una VPN activa o el TV está en reposo profundo. Con SmartThings, la cuenta Samsung suma algo más que puede fallar, como que se cierre la sesión. Mando TV se comunica directo con el TV en tu red local, sin cuenta en la que iniciar sesión. Más soluciones en [el celular no encuentra el TV](/guias/el-celular-no-encuentra-el-tv/).'),
      ('Mando TV o SmartThings: cuál usar', 'Quédate con SmartThings si lo usas para electrodomésticos Samsung, luces u otros aparatos de la casa inteligente, o para funciones de la cuenta Samsung. Usa Mando TV cuando solo quieras un control rápido para el TV, o si tienes también un LG, Roku, Google TV o Fire TV: una sola app los controla a todos. Ambas pueden estar en el mismo celular.'),
      ('Si negaste el permiso por error', 'En el TV, ve a Configuración > General > Administrador de dispositivos externos > Administrador de conexión de dispositivos y deja Mando TV como permitido.'),
      ('¿No tienes control?', 'Puedes aceptar el aviso con el botón del propio TV. La guía [control remoto Samsung sin el control original](/guias/control-remoto-samsung-sin-control/) explica cómo.'),
      ('Gratis y Pro', 'El control se descarga y se usa gratis, sin anuncios ni suscripción. Mando TV Pro es un pago único opcional para funciones extra.'),
    ],
    marca=('control-remoto-samsung', 'Control remoto para TV Samsung'),
    faq=[
      ('¿Puedo controlar mi TV Samsung sin SmartThings?', 'Sí. Mando TV se conecta a los televisores Samsung con Tizen directo por tu WiFi. Aceptas la conexión una vez en el TV, sin cuenta Samsung.'),
      ('¿Mando TV controla electrodomésticos Samsung?', 'No. Es solo un control para TV. Usa SmartThings para electrodomésticos y otros dispositivos del hogar inteligente.'),
      ('¿Mando TV es de Samsung?', 'No. Mando TV es una app independiente y no está afiliada a Samsung. Samsung y SmartThings pertenecen a sus dueños y se nombran solo para describir compatibilidad.'),
    ]),
  dict(slug='guias/alternativa-a-la-app-google-tv', corto='Alternativa al control de Google TV', fecha='2026-11-23',
    titulo='¿El control de Google TV no funciona? Prueba otra app',
    desc='Si el celular no encuentra tu TV o el control falla, usa Mando TV. Controla Google TV y Android TV por WiFi sin cuenta de Google ni anuncios.',
    h1='Alternativa al control de Google TV en el celular',
    intro='El control del celular para Google TV y Android TV está dentro de la app de Google y requiere tu cuenta. Si no encuentra el TV, te quedas sin control. Mando TV es una app independiente que se empareja con el código de 6 caracteres en la pantalla del TV y funciona sin cuenta de Google, desde un iPhone, un celular Android o un PC con Windows.',
    pasos=[
      'Enciende el TV y conecta el celular a la misma red WiFi.',
      'Descarga Mando TV y ábrelo. Toca tu Google TV o Android TV en la lista.',
      'El TV muestra un código de 6 caracteres. Escríbelo en Mando TV y toca Emparejar.',
      'Usa las flechas, OK, Atrás, Inicio, volumen y el teclado. No hay que iniciar sesión en nada.',
      'Opcional: busca "Wake on LAN" o "Encender por red" en la configuración del TV para que la app también pueda encenderlo.',
    ],
    extra=[
      ('Por qué el control del celular deja de encontrar el TV', 'Lo más común es la red: el celular y el TV están en redes WiFi distintas, hay una VPN activa o una red de invitados los separa. Corrige eso primero, porque afecta a cualquier app de control. Mira [el celular no encuentra el TV](/guias/el-celular-no-encuentra-el-tv/).'),
      ('Con qué televisores funciona', 'TVs con Google TV y Android TV de Sony, TCL, Hisense, Philips, Sharp, Xiaomi, Toshiba y más, además del Chromecast con Google TV, Google TV Streamer y Nvidia Shield. Todos se emparejan igual, con el código en pantalla, una sola vez.'),
      ('Dónde la app de Google es mejor', 'La app de Google también te ayuda a encontrar qué ver y guarda tu lista de lo que quieres ver. Úsala para eso. Mando TV es solo el control remoto y además controla Samsung, LG, Roku y Fire TV desde la misma app, y desde un PC con Windows.'),
      ('Si ya no está la antigua app de control de Android TV', 'Google movió el control del celular de la antigua app Android TV Remote Control a la app Google TV. Si buscas un control remoto independiente, Mando TV es una opción.'),
      ('Gratis y Pro', 'El control se descarga y usa gratis, sin anuncios ni suscripción. Mando TV Pro es un pago único opcional para funciones extra.'),
    ],
    marca=('control-remoto-android-tv', 'Control remoto para Android TV y Google TV'),
    faq=[
      ('¿Necesito una cuenta de Google para usar Mando TV con Google TV?', 'No. El código en la pantalla del TV es todo lo que se necesita para emparejar.'),
      ('¿Funciona con Chromecast con Google TV?', 'Sí. Se empareja igual, con el código de 6 caracteres en la pantalla.'),
      ('¿Puedo usarlo desde un iPhone?', 'Sí. Mando TV está en la App Store para iPhone y iPad, en Microsoft Store para Windows, y en prueba anticipada gratis en Google Play para Android.'),
    ]),
  dict(slug='guias/app-control-remoto-para-windows', corto='Control remoto para Windows', fecha='2026-11-23',
    titulo='Control remoto para TV en Windows: usa tu PC | Mando TV',
    desc='Controla tu TV Samsung, LG, Roku, Google TV o Fire TV desde un PC con Windows: atajos de teclado, mini control y conexión por WiFi. En Microsoft Store.',
    h1='Control remoto para TV en Windows',
    intro='Mando TV tiene una app para Windows que convierte tu PC o laptop en un control remoto por la red de tu casa. Escribe en el TV con tu teclado real, deja una ventana pequeña del control encima mientras trabajas y controla televisores Samsung, LG, Roku, Google TV o Fire TV desde la misma app.',
    pasos=[
      'Instala Mando TV gratis desde Microsoft Store en un PC con Windows 10 o 11.',
      'Asegúrate de que el PC y el TV estén en la misma red, por WiFi o cable a través del mismo router.',
      'Abre Mando TV. El TV aparece en la lista. Haz clic en él.',
      'Acepta el aviso en el TV si lo pide (LG, Samsung), o escribe el código que muestra (Google TV, Fire TV).',
      'Haz clic en los botones o escribe una búsqueda con tu teclado. Listo.',
    ],
    extra=[
      ('Atajos de teclado (Pro)', 'Con Pro, el teclado del PC se convierte en el control: flechas para moverse, Enter para OK, Backspace o Esc para volver, más y menos para volumen, M para silenciar y Espacio para pausar.'),
      ('Mini control (Pro)', 'Una ventana pequeña del control que se queda encima de las otras ventanas, así puedes cambiar el volumen o pausar sin dejar lo que estás haciendo.'),
      ('Escribir en el TV desde el PC', 'El teclado en pantalla de un TV es lento. En Mando TV escribes con tu teclado real y el texto va a la búsqueda del TV. Esta parte es gratis.'),
      ('Más detalles', 'Para la versión paso a paso mira [cómo controlar el TV desde el PC con Windows](/guias/controlar-el-tv-desde-el-pc/). Para usar el celular, mira [cómo conectar el celular al TV por WiFi](/guias/conectar-celular-al-tv-por-wifi/).'),
      ('Gratis y Pro', 'Las flechas, OK, Atrás, Inicio, volumen, canales, teclas numéricas, teclado, abrir apps, cambiar entradas y encender o apagar son gratis, sin anuncios ni suscripción. Mando TV Pro es un pago único opcional para funciones extra. En Windows, Pro se compra a través de Microsoft Store.'),
      ('Comandos de voz desde el PC (Pro)', 'Con Pro puedes hablarle al TV por el micrófono del PC. El reconocimiento de voz se hace en el propio PC: no necesita internet ni cambiar ajustes de Windows. Lo que dices nunca sale del PC y no se guarda. Solo en procesadores muy antiguos la app usa la escritura por voz de Windows, que requiere activar "Reconocimiento de voz en línea" en Configuración > Privacidad y seguridad > Voz y tener tu idioma añadido en Windows.'),
    ],
    marca=None,
    faq=[
      ('¿La app de control remoto para TV en Windows necesita Bluetooth o cable?', 'No. Usa la red de tu casa. El PC y el TV solo deben estar conectados al mismo router.'),
      ('¿Qué televisores puedo controlar desde Windows?', 'Samsung con Tizen, LG con webOS, Roku TV y reproductores, Google TV y Android TV, y Fire TV.'),
      ('¿Puedo usar los parlantes del PC o la pantalla para ver el TV?', 'No. Mando TV es solo un control remoto. No muestra ni transmite la imagen del TV en el PC.'),
      ('¿Por qué no funciona la voz en mi PC con Windows?', 'La voz es una función Pro, así que revisa que Pro esté activo y que el micrófono del PC funcione. En la mayoría de los PC el reconocimiento se hace en el propio PC, sin internet. Solo en procesadores muy antiguos la app usa la escritura por voz de Windows: entonces activa "Reconocimiento de voz en línea" en Configuración > Privacidad y seguridad > Voz y añade tu idioma en Configuración > Hora e idioma.'),
    ]),
  dict(slug='guias/app-control-remoto-para-iphone', corto='Control remoto para iPhone', fecha='2026-11-23',
    titulo='App de control remoto para iPhone: Samsung, LG, Roku',
    desc='Usa tu iPhone como control remoto por WiFi para Samsung, LG, Roku, Google TV y Fire TV. Gratis en la App Store, sin cuenta ni anuncios.',
    h1='Control remoto en el iPhone para todos tus televisores',
    intro='Mando TV convierte tu iPhone o iPad en un control remoto para televisores Samsung, LG, Roku, Google TV o Android TV y Fire TV, por el WiFi de tu casa. Es gratis en la App Store, sin cuenta ni anuncios. También funciona en Android y Windows.',
    pasos=[
      'Descarga Mando TV gratis desde la App Store.',
      'Conecta tu iPhone y el televisor a la misma red WiFi.',
      'Abre Mando TV y toca Permitir cuando iOS pida acceso a la red local. La app lo necesita para encontrar el TV.',
      'Toca tu TV en la lista. Acepta el aviso en la pantalla del TV si lo pide (LG y Samsung), o escribe el código que muestra el TV (Google TV o Fire TV).',
      'Usa los botones, el volumen y el teclado. Ya estás conectado.',
    ],
    extra=[
      ('Funciona con estos televisores', 'LG webOS, Samsung Tizen (2016 en adelante), Roku TV y reproductores Roku, Google TV y Android TV, y Fire TV. Las páginas de cada marca son [Samsung](/control-remoto-samsung/), [LG](/control-remoto-lg/), [Roku](/control-remoto-roku/) y [Android TV](/control-remoto-android-tv/).'),
      ('Por qué pide acceso a la red local', 'El iPhone no deja que las apps vean los aparatos de tu red WiFi si no le das permiso. Si el TV no aparece en la lista, abre Ajustes > Mando TV y activa Red local. La app solo se comunica con tu TV dentro de la red de tu casa.'),
      ('Por qué una app para iPhone y no la del fabricante', 'Cada marca de TV tiene su propia app y cada una quiere su propio registro o cuenta. Mando TV es una sola app para todas, sin necesidad de cuenta.'),
      ('Gratis y Pro en iPhone', 'Las flechas, OK, Atrás, Inicio, volumen, canales, teclas numéricas, teclado, abrir apps, cambiar entradas y encender o apagar son gratis, sin anuncios ni suscripción. Mando TV Pro es un pago único opcional para funciones extra, y se compra dentro de la app.'),
    ],
    marca=None,
    faq=[
      ('¿Mando TV es gratis en el iPhone?', 'La descarga es gratis, sin anuncios. El control básico es gratis, así como abrir apps y cambiar entradas. Las funciones extra forman parte de Mando TV Pro, un pago único opcional.'),
      ('¿Funciona en iPad?', 'Sí. La misma app funciona en iPhone y iPad.'),
      ('¿Una app de control remoto para iPhone necesita Bluetooth o infrarrojo?', 'No en iPhone. Los iPhone no tienen emisor infrarrojo, por lo que el control infrarrojo no está disponible allí, y la opción de Bluetooth solo es para Android 9 o más reciente, no para iPhone. En el iPhone, Mando TV controla los Smart TV y Apple TV (en beta) a través del WiFi de tu casa.'),
    ]),
  dict(slug='guias/control-remoto-fire-tv-en-el-celular', corto='Control remoto para Fire TV', fecha='2026-11-23',
    titulo='Control remoto para Fire TV en el celular y el PC',
    desc='Usa el celular o el PC como control de un Fire TV Stick, Fire TV Cube o TV con Fire TV, por WiFi y con un PIN de 4 dígitos. Sin la app de Amazon.',
    h1='Control remoto para Fire TV desde tu celular o PC',
    intro='Si perdiste el control de tu Fire TV o se quedó sin batería, Mando TV te permite controlar un Fire TV Stick, un Fire TV Cube o un televisor con Fire TV integrado desde tu celular o PC, por la red WiFi de tu casa. El emparejamiento requiere un PIN de 4 dígitos. Fire TV es nuevo en Mando TV, así que primero actualiza la app.',
    pasos=[
      'Actualiza Mando TV a la última versión desde la App Store, Microsoft Store o Google Play.',
      'Enciende el Fire TV y conecta tu celular a la misma red WiFi.',
      'Abre Mando TV. Tu Fire TV aparece en la lista. Tócalo.',
      'La pantalla del TV muestra un PIN de 4 dígitos. Escríbelo en Mando TV. Solo debes hacerlo una vez.',
      'Usa las flechas, OK, Atrás, Inicio, los botones de reproducción y el teclado para escribir búsquedas.',
    ],
    extra=[
      ('Dispositivos Fire TV compatibles', 'Fire TV Stick, Fire TV Stick 4K, Fire TV Cube y televisores con Fire TV integrado. El soporte es nuevo y las pruebas en dispositivos reales son limitadas. Si algo no funciona como debe, escríbenos tu modelo desde la página de Ayuda.'),
      ('Cómo encender un Fire TV', 'Mando TV no enciende el Fire TV a través de la red. Enciende el televisor con su botón físico: un Fire TV Stick o Cube conectado a él suele encenderse junto con el TV gracias a HDMI-CEC, y en un televisor con Fire TV integrado, el TV es el propio Fire TV. Luego controla todo desde tu celular.'),
      ('Si tu Fire TV no aparece', 'Asegúrate de que ambos dispositivos estén en la misma red WiFi y de que el Fire TV esté encendido. En un iPhone, permite "Red local" para Mando TV en Ajustes. Mira [el celular no encuentra el TV](/guias/el-celular-no-encuentra-el-tv/).'),
      ('¿No tienes ningún control?', 'Necesitas que la pantalla del Fire TV muestre el PIN, por lo que el televisor y el Fire TV deben estar encendidos y mostrando imagen. Si el TV está en una entrada incorrecta, cámbiala con los botones físicos del televisor. Mira [cambiar la entrada HDMI sin control](/guias/cambiar-entrada-hdmi-sin-control/).'),
      ('Qué es gratis y qué es Pro', 'Las flechas, OK, Atrás, Inicio, volumen, canales, teclas numéricas, teclado, abrir apps, cambiar entradas y encender o apagar son gratis, sin anuncios ni suscripción. Mando TV Pro es un pago único opcional para funciones extra.'),
    ],
    marca=None,
    faq=[
      ('¿Necesito la app de Amazon Fire TV?', 'No. Mando TV se conecta al Fire TV por tu WiFi usando un PIN. No necesitas una cuenta de Amazon en el celular.'),
      ('¿Funciona con televisores con Fire TV y con Fire TV Stick?', 'Sí, para eso está diseñado. El soporte es nuevo; mantén la app actualizada y avísanos si algún modelo no funciona correctamente.'),
      ('¿Por qué necesito un PIN?', 'El Fire TV muestra un PIN de 4 dígitos para demostrar que estás frente al televisor. Nadie puede emparejarse sin ver la pantalla.'),
    ]),
  dict(slug='guias/perdi-el-control-del-fire-tv', corto='Perdí el control del Fire TV', fecha='2026-11-23',
    titulo='¿Perdiste el control del Fire TV? Usa tu celular',
    desc='¿Perdiste el control de tu Fire TV Stick? Contrólalo desde el celular por WiFi con un PIN de 4 dígitos. Soluciones para cambiar de red y HDMI-CEC.',
    h1='¿Perdiste el control del Fire TV? Usa tu celular',
    intro='Si perdiste o se dañó el control de tu Fire TV Stick, Fire TV Cube o Smart TV con Fire TV, puedes usar tu celular siempre que el dispositivo siga conectado a tu WiFi. El emparejamiento usa un PIN de 4 dígitos que aparece en la pantalla del TV, así que no necesitas el control antiguo para esto.',
    pasos=[
      'Enciende el TV con su botón físico. Un Fire TV Stick o Cube enchufado suele encenderse junto con él; si tienes HDMI-CEC activado, el TV a veces cambia solo a esa entrada.',
      'Si el TV muestra otra entrada, cámbiala con el botón de entradas del TV. Mira [cambiar la entrada HDMI sin control](/guias/cambiar-entrada-hdmi-sin-control/).',
      'Conecta tu celular a la misma red WiFi que el Fire TV.',
      'Descarga y abre Mando TV. Tu Fire TV aparece en la lista. Tócalo.',
      'El TV muestra un PIN de 4 dígitos. Escríbelo en Mando TV. Solo se hace una vez.',
      'Usa las flechas, OK, Atrás, Inicio, volumen, reproducción y el teclado desde tu celular.',
    ],
    extra=[
      ('Prueba primero el control del TV (HDMI-CEC)', 'Muchos controles de TV pueden manejar un Fire TV Stick a través de HDMI-CEC. Con el Fire TV en pantalla, pulsa las flechas y OK en el control del TV. Si no pasa nada, activa CEC en la configuración del TV (Anynet+ en Samsung, SIMPLINK en LG, BRAVIA Sync en Sony) y en el Fire TV, en el menú de pantalla y sonido ("Display & Sounds"), activa el control de dispositivos HDMI CEC.'),
      ('Si te mudaste o cambiaste el WiFi', 'Sin control no puedes escribir la nueva contraseña del WiFi en el Fire TV, pero hay una salida: desde otro celular, crea un punto de acceso con exactamente el mismo nombre y contraseña que tu WiFi anterior. El Fire TV se conecta solo. Conecta el celular con Mando TV a ese punto de acceso, empareja con el PIN, luego ve a Configuración > Red en el Fire TV y elige tu nuevo WiFi. Por último, conecta también el celular a la red nueva.'),
      ('Emparejar un control de repuesto', 'La mayoría de los controles nuevos de Fire TV se emparejan al mantener presionado el botón Inicio unos 10 segundos cerca del Fire TV. Si no se empareja, en Configuración entra al menú de controles y dispositivos Bluetooth ("Controllers & Bluetooth Devices") y elige agregar un control nuevo de Amazon Fire TV. Puedes llegar a ese menú desde tu celular con Mando TV.'),
      ('Fire TV integrado en el TV', 'En TVs con Fire TV integrado, los mismos pasos funcionan porque el TV es el Fire TV.'),
      ('Antes de empezar', 'El soporte para Fire TV llegó recientemente a Mando TV, así que actualiza la app primero. Si tu modelo no se comporta bien, escríbenos desde la [página de ayuda](/soporte.html) e incluye el nombre del modelo.'),
      ('Gratis y Pro', 'El control es gratis para descargar y usar, sin anuncios ni suscripción. Mando TV Pro es un pago único opcional para extras.'),
    ],
    marca=('guias/control-remoto-fire-tv-en-el-celular', 'Control remoto para Fire TV desde tu celular o PC'),
    faq=[
      ('¿Puedo controlar un Fire TV Stick con el celular sin el control?', 'Sí, si el Fire TV está encendido y conectado a tu WiFi. Mando TV se empareja con el PIN de 4 dígitos que muestra el TV, así que no necesitas el control antiguo en ningún momento.'),
      ('¿Funciona si el Fire TV está en una nueva red WiFi?', 'No directamente, porque el celular y el Fire TV deben estar en la misma red. Primero debes volver a conectar el Fire TV con el truco del punto de acceso descrito en esta guía.'),
      ('¿Necesito la app Amazon Fire TV o una cuenta de Amazon en mi celular?', 'No. Mando TV se conecta al Fire TV por tu red local usando el PIN y no requiere ninguna cuenta.'),
    ]),
  dict(slug='guias/encender-el-tv-sin-control', corto='Encender el TV sin control', fecha='2026-11-23',
    titulo='Cómo encender el TV sin control (todas las marcas)',
    desc='Aprende a encender tu TV sin control: dónde está el botón en Samsung, LG, TCL, Hisense y Sony, más HDMI-CEC y trucos desde el celular.',
    h1='Cómo encender el TV sin el control remoto',
    intro='Casi todos los televisores tienen un botón físico de encendido. Solo que está bien escondido. Aquí te decimos dónde buscar por marca, y dos formas de evitar la búsqueda la próxima vez: HDMI-CEC desde una consola o reproductor de streaming, y encender el TV desde tu celular por WiFi.',
    pasos=[
      'Mira debajo del centro de la pantalla, justo detrás del logo de la marca. Muchos televisores tienen un botón pequeño o un joystick ahí, apuntando hacia abajo.',
      'Si no está ahí, recorre la parte trasera del TV cerca de las esquinas inferiores, luego los bordes izquierdo y derecho.',
      'Presiona el botón una vez. En muchos televisores con un solo botón, con el TV ya encendido, una pulsación corta abre un menú pequeño de entradas y volumen, y una pulsación larga lo apaga.',
      '¿Sigue sin responder? Revisa el cable de alimentación en ambos extremos y prueba otro tomacorriente. Si la luz de reposo no se enciende, el TV no recibe energía.',
      'Una vez que el TV está encendido, configúralo para no necesitar el botón otra vez: activa HDMI-CEC y el encendido por red, explicados más abajo.',
    ],
    extra=[
      ('Dónde está el botón de encendido por marca', 'Samsung: un botón o joystick bajo el centro de la pantalla, o atrás en una esquina inferior. LG: un joystick debajo del logo LG en la mayoría de los modelos. TCL y Hisense: usualmente un botón pequeño debajo del centro de la pantalla o atrás cerca de una esquina inferior. Sony: atrás o en un borde lateral, cerca de abajo. Las ubicaciones cambian por modelo; si no lo encuentras, busca el manual con el número de modelo en la etiqueta trasera.'),
      ('Encender el TV desde una consola o reproductor de streaming (HDMI-CEC)', 'Con HDMI-CEC activado, encender una PlayStation, una Xbox, un reproductor Roku, un Fire TV Stick o un Chromecast también enciende el TV y cambia a la entrada correcta. Cada marca llama al ajuste con su propio nombre: Anynet+ en Samsung, SIMPLINK en LG, BRAVIA Sync en Sony, y CEC en la mayoría de los demás. Más detalles en [encender el TV y pasar al HDMI de la consola](/guias/encender-tv-y-hdmi-de-la-consola-sin-control/).'),
      ('Encender el TV desde tu celular', 'Los Smart TV pueden encenderse por WiFi si lo permites una vez, y luego Mando TV los enciende desde tu celular. En Samsung, activa "Encender con dispositivo móvil" en Configuración > General > Red > Configuración experta. En LG, activa "Encender TV con móvil" ([paso a paso](/guias/encender-tv-lg-con-el-celular/)). En un Roku TV, activa "Inicio rápido de TV" en Configuración > Sistema > Energía. En Google TV y Android TV, busca Wake on LAN o "Encender por red", si tu modelo lo tiene. Esto se hace una sola vez, con el TV encendido.'),
      ('Si no encuentras ningún botón', 'Algunos televisores recientes esconden tanto el único botón que parece que no hay ninguno. Busca un pequeño relieve o un área de sensor de luz debajo de la pantalla: el botón suele estar justo al lado. Por WiFi, Mando TV necesita que el TV haya estado encendido y conectado una vez. La excepción es el infrarrojo: en un celular Android con emisor infrarrojo, Mando TV puede encender un TV que nunca se configuró, siempre que apuntes el celular al TV. El infrarrojo es nuevo y funciona con las marcas que están en la lista de códigos de la app.'),
      ('Gratis y Pro', 'El control se descarga y se usa gratis, sin anuncios ni suscripción. Mando TV Pro es un pago único opcional para funciones extra.'),
    ],
    marca=None,
    faq=[
      ('¿Puedo encender el TV con mi celular si nunca lo configuré?', 'No por WiFi. Un TV apagado solo despierta desde la red si se activó el encendido por red antes. La primera vez, usa el botón del TV. La excepción es un celular Android con emisor infrarrojo: Mando TV puede encender el TV por infrarrojo sin configuración, si la marca está en su lista de códigos o eliges "Otra marca o no sé".'),
      ('¿Cómo enciendo un TV Samsung sin el control?', 'Presiona el botón de control bajo el centro de la pantalla o atrás en una esquina inferior. Luego activa "Encender con dispositivo móvil" para que tu celular lo encienda la próxima vez.'),
      ('¿Cómo enciendo un Roku TV sin el control?', 'Usa el botón del TV, usualmente bajo el centro o atrás. Luego activa "Inicio rápido de TV" en Configuración > Sistema > Energía para que Mando TV lo encienda desde tu celular.'),
      ('¿Por qué mi TV se enciende solo cuando enciendo la consola?', 'Eso es HDMI-CEC. Es útil, y puedes desactivarlo en la configuración del TV si lo prefieres.'),
    ]),
  dict(slug='guias/control-remoto-sony', corto='Control remoto Sony', fecha='2026-11-23',
    titulo='Control remoto para TV Sony en el celular y el PC',
    desc='Controla tu TV Sony Bravia con Google TV o Android TV desde el celular por WiFi. Y en beta, los Bravia de 2013 a 2015 sin Android.',
    h1='Control remoto para tu TV Sony desde el celular',
    intro='Los Smart TV Sony Bravia usan Google TV en los modelos recientes y Android TV en los anteriores, desde 2015. Mando TV controla ambos desde un iPhone, un celular Android o un PC con Windows por el WiFi de tu casa, así que te sirve de control remoto cuando el original se pierde o se queda sin pilas.',
    pasos=[
      'Revisa que tu Sony muestre la pantalla de inicio de Google TV o Android TV. Casi todos los Smart TV Bravia desde 2015 la tienen.',
      'Conecta el celular y el TV a la misma red WiFi.',
      'Abre Mando TV y toca tu Sony en la lista.',
      'Escribe el código de 6 caracteres que muestra el TV en pantalla (solo la primera vez). No necesitas el control para esto.',
      'Usa las flechas, OK, Atrás, Inicio, volumen y teclado.',
    ],
    extra=[
      ('Encender un Sony desde el celular', 'Los Sony con Google TV y Android TV se pueden encender por la red si está activado "Inicio remoto". Suele estar en Configuración > Red e Internet > Inicio remoto, aunque la ruta cambia ligeramente según el modelo. Luego toca el TV en Mando TV mientras está apagado y la app lo enciende.'),
      ('Dónde está el botón de encendido en un Sony', 'En la mayoría de los Bravia está atrás, cerca del borde inferior izquierdo o derecho, o en un borde lateral. Una pulsación corta enciende el TV. Más en [cómo encender un TV sin el control](/guias/encender-el-tv-sin-control/).'),
      ('Sony antiguos', 'Los Sony Bravia de 2013 a 2015 que no usan Android tienen soporte beta en Mando TV. Es nuevo, así que aún puede tener detalles por pulir. El TV muestra un PIN de 4 dígitos para escribir en la app. Otros Sony sin Google TV o Android TV no están cubiertos hoy.'),
      ('Gratis y Pro', 'El control se descarga y se usa gratis, sin anuncios ni suscripción. Mando TV Pro es un pago único opcional para funciones extra.'),
    ],
    marca=('control-remoto-android-tv', 'Control remoto para Android TV y Google TV'),
    faq=[
      ('¿Mando TV funciona con los TV Sony Bravia?', 'Sí, con los que usan Google TV o Android TV, que son la mayoría de los Smart TV Sony desde 2015.'),
      ('¿Necesito una app de Sony o cuenta de Google?', 'No. Mando TV se empareja con el código en pantalla y no pide cuenta.'),
      ('¿Funciona con Bravia antiguos sin Android?', 'En beta, sí, en modelos de 2013 a 2015 sin Android. Se empareja con un PIN de 4 dígitos que muestra el TV.'),
      ('¿Puedo escribir en mi Sony desde el celular?', 'Sí. El teclado es gratis y escribe en YouTube, Netflix y la caja de búsqueda del TV.'),
    ]),
  dict(slug='guias/control-remoto-tcl', corto='Control remoto TCL', fecha='2026-11-23',
    titulo='Control remoto TCL para iPhone, Android y PC | Mando TV',
    desc='¿Perdiste el control de tu TV TCL? La mayoría usa Roku TV o Google TV. Usa Mando TV por WiFi desde tu celular. Gratis, sin cuenta ni anuncios.',
    h1='Control remoto TCL para tu celular',
    intro='TCL fabrica el televisor, pero el sistema es Roku TV o Google TV (Android TV en modelos antiguos). Mando TV controla los dos, así que te sirve como control remoto del TCL desde el celular o el PC, por el WiFi de tu casa. Gratis, sin cuenta ni anuncios.',
    pasos=[
      'Identifica el sistema de tu TCL. Si la pantalla de inicio es una cuadrícula simple de canales, es Roku TV. Si parece Google TV o Android TV con filas de recomendaciones, es Google TV.',
      'Conecta el celular y el TV TCL a la misma red WiFi.',
      'Abre Mando TV. El TCL aparece solo en la lista. Tócalo.',
      'En un TCL con Roku TV no se necesita nada más. En uno con Google TV, escribe el código de 6 caracteres que muestra el televisor (solo la primera vez).',
      'Usa las flechas, OK, Atrás, Inicio, volumen y teclado. Enciende el TV desde la app si activaste el encendido por red (ver abajo).',
    ],
    extra=[
      ('Encender un TCL desde el celular', 'En TCL con Roku TV, activa "Inicio rápido de TV" en Configuración > Sistema > Energía. En TCL con Google TV, busca una opción como Wake on LAN, "Encender por red" o inicio remoto en la configuración de red o energía. Algunos modelos no la ofrecen. En ese caso, enciende el TV con el botón físico, casi siempre abajo al centro o atrás.'),
      ('Si tu TCL no aparece', 'Revisa que el celular y el TV estén en la misma red WiFi. Los routers con redes separadas de 2.4 GHz y 5 GHz pueden ocultar dispositivos. En un iPhone, permite "Red local" para Mando TV en Ajustes. También puedes agregar el TV escribiendo su dirección IP. Mira [el celular no encuentra el TV](/guias/el-celular-no-encuentra-el-tv/).'),
      ('Más detalles para tu TCL', 'Para un TCL con Roku TV, mira [control remoto para Roku](/control-remoto-roku/). Para un TCL con Google TV o Android TV, mira [control remoto para Android TV](/control-remoto-android-tv/).'),
      ('Gratis y Pro', 'Las flechas, OK, Atrás, Inicio, volumen, canales, teclas numéricas, teclado, abrir apps, cambiar entradas y encender o apagar son gratis, sin anuncios ni suscripción. Mando TV Pro es un pago único opcional para funciones extra.'),
    ],
    marca=None,
    faq=[
      ('¿Mando TV funciona con todos los TCL?', 'Funciona con los TCL que usan Roku TV, Google TV o Android TV, que son casi todos los Smart TV TCL. Un TCL que no es Smart TV no se puede controlar por WiFi.'),
      ('¿Necesito la app TCL o una cuenta?', 'No. Mando TV se conecta directo por tu WiFi y no pide ninguna cuenta.'),
      ('Mi TCL pide un código. ¿Dónde está?', 'Los modelos TCL con Google TV y Android TV muestran un código de 6 caracteres en la pantalla. Escríbelo en Mando TV tal como aparece. El TCL con Roku TV no pide código.'),
    ]),
  dict(slug='guias/control-remoto-hisense', corto='Control remoto Hisense', fecha='2026-11-23',
    titulo='Control remoto Hisense: qué funciona desde el celular',
    desc='Mando TV controla los TV Hisense con VIDAA, Roku TV, Google TV o Fire TV desde tu celular por WiFi. Guía honesta de lo que funciona y cómo.',
    h1='Control remoto Hisense en el celular: qué funciona y qué no',
    intro='Los televisores Hisense no son todos iguales por dentro. Según el modelo, usan el sistema propio VIDAA de Hisense, Roku TV, Google TV o Fire TV. Mando TV sirve como control remoto en los cuatro, con una excepción en algunos modelos recientes de VIDAA. Aquí te explicamos cómo saber cuál tienes y qué esperar.',
    pasos=[
      'Revisa qué sistema usa tu Hisense. VIDAA es la interfaz propia de Hisense. Roku TV muestra una cuadrícula de canales. Google TV presenta filas de recomendaciones. Fire TV muestra la pantalla de inicio con filas de Amazon.',
      'Conecta el celular y el TV Hisense a la misma red WiFi.',
      'Abre Mando TV. El TV aparece solo en la lista. Tócalo.',
      'Los modelos VIDAA y Fire TV pueden pedir un PIN de 4 dígitos; Google TV muestra un código de 6 caracteres. Escríbelo en la app. Roku TV no pide nada. Hazlo una sola vez.',
      'Usa las flechas, OK, Atrás, Inicio, volumen y teclado desde tu celular.',
    ],
    extra=[
      ('Hisense con Roku TV o Google TV', 'Estos funcionan igual que cualquier otro Roku o Google TV. Mira [control remoto para Roku](/control-remoto-roku/) y [control remoto para Android TV](/control-remoto-android-tv/) para los detalles de cada uno.'),
      ('Hisense con Fire TV', 'El soporte para Fire TV es nuevo en Mando TV. Actualiza la app a la última versión desde tu tienda y lee la [control remoto para Fire TV](/guias/control-remoto-fire-tv-en-el-celular/) para ver cómo funciona el emparejamiento por PIN. Si algo no se comporta bien, escríbenos desde la página de Ayuda y menciona tu modelo.'),
      ('Hisense con VIDAA', 'La mayoría de los modelos VIDAA funcionan: botones, volumen, teclado, apps y entradas. Algunos modelos recientes de VIDAA solo aceptan la app oficial de Hisense. Mando TV lo detecta al conectar y te lo dice claramente, en lugar de fallar sin avisar. En ese caso, usa la app de Hisense para tu modelo, los botones del TV o el control original.'),
      ('Encender un Hisense desde el celular', 'En Hisense con Roku TV, activa "Inicio rápido de TV" en Configuración > Sistema > Energía. En Google TV, busca una opción de Wake on LAN o "Encender por red". Si no existe, usa el botón de encendido del TV.'),
      ('Gratis y Pro', 'Las flechas, OK, Atrás, Inicio, volumen, canales, números, teclado, abrir apps, cambiar entradas y encender o apagar son gratis, sin anuncios ni suscripción. Mando TV Pro es un pago único opcional para funciones extra.'),
    ],
    marca=None,
    faq=[
      ('¿Mando TV funciona con Hisense VIDAA?', 'Sí, con la mayoría de los modelos VIDAA. Algunos recientes solo aceptan la app oficial de Hisense; Mando TV lo detecta y te avisa. Los televisores Hisense con Roku TV, Google TV o Fire TV también son compatibles.'),
      ('¿Cómo sé si mi Hisense es Roku TV, Google TV o Fire TV?', 'Mira la pantalla de inicio. Roku TV tiene una cuadrícula simple de canales y un logo de Roku al iniciar. Google TV muestra filas de recomendaciones. Fire TV tiene la pantalla de inicio de Amazon Fire TV. El nombre del modelo en Configuración > Acerca de también te lo indica.'),
      ('¿Necesito una cuenta de Hisense o Google?', 'No. Mando TV se conecta directo por tu WiFi y no pide ninguna cuenta.'),
    ]),
  dict(slug='guias/control-remoto-philips', corto='Control remoto Philips', fecha='2026-11-23',
    titulo='Control remoto Philips: Roku TV, Google TV y Android TV',
    desc='Usa tu celular como control de tu TV Philips por WiFi. Funciona con modelos Roku TV, Google TV y Android TV. Y una nota honesta sobre Titan OS.',
    h1='Control remoto para tu TV Philips desde el celular',
    intro='Los televisores Philips usan distintos sistemas según el país y el año: Roku TV en algunos mercados, Google TV o Android TV en muchos otros, y Titan OS en algunos modelos recientes de Europa. Mando TV controla los modelos con Roku TV, Google TV y Android TV desde tu celular o PC por WiFi.',
    pasos=[
      'Revisa la pantalla de inicio. Roku TV muestra una cuadrícula de canales. Google TV y Android TV muestran filas de recomendaciones de Google. Titan OS tiene su propia interfaz.',
      'Conecta el celular y el TV a la misma red WiFi.',
      'Abre Mando TV y toca tu TV Philips en la lista.',
      'Un Roku TV no pide nada. Google TV y Android TV muestran un código de 6 caracteres: escríbelo en la app una vez.',
      'Usa las flechas, OK, Atrás, Inicio, volumen y teclado.',
    ],
    extra=[
      ('Philips con Roku TV', 'Funciona como cualquier Roku TV. Para encenderlo desde el celular, activa "Inicio rápido de TV" en Configuración > Sistema > Energía. Más detalles en [control remoto para Roku](/control-remoto-roku/).'),
      ('Philips con Google TV o Android TV', 'Incluye muchos modelos con Ambilight. Se emparejan con el código que aparece en la pantalla. Para encenderlo desde el celular, busca "Wake on LAN" o "Encender por red" en los ajustes de red o energía. Algunos modelos no lo tienen. Más detalles en [control remoto para Android TV](/control-remoto-android-tv/).'),
      ('Philips antiguos sin Android', 'Los TVs Philips de 2011 a 2015 que no usan Android tienen soporte beta en Mando TV. Es nuevo y no requiere código de emparejamiento.'),
      ('Philips con Titan OS', 'Titan OS es un sistema diferente que Mando TV no controla hoy, y preferimos decirlo claro. Los modelos Philips nuevos sin Android tampoco están cubiertos.'),
      ('Gratis y Pro', 'El control se descarga y usa gratis, sin anuncios ni suscripción. Mando TV Pro es una pago único opcional para funciones extra.'),
    ],
    marca=None,
    faq=[
      ('¿Mando TV funciona con TVs Philips?', 'Con TVs Philips que usan Roku TV, Google TV o Android TV, sí. Con los modelos de 2011 a 2015 sin Android, en beta. Los modelos con Titan OS no son compatibles.'),
      ('¿Controla Ambilight?', 'Mando TV es un control remoto: envía las teclas, así que puedes llegar a los ajustes de Ambilight con las flechas y OK. No tiene controles separados para Ambilight.'),
      ('¿Necesito una cuenta Philips o Google?', 'No. Mando TV se conecta por el WiFi de tu casa y no pide cuenta.'),
    ]),
]
# <<< guías traídas del inglés

GUIAS_PIE = [
  ('encender-tv-lg-con-el-celular', 'Cómo encender el TV LG con el celular'),
  ('control-remoto-samsung-sin-control', 'Control remoto Samsung sin el control original'),
  ('conectar-celular-al-tv-por-wifi', 'Cómo conectar el celular al TV por WiFi'),
  ('controlar-el-tv-desde-el-pc', 'Cómo controlar el TV desde el PC con Windows'),
  ('roku-no-responde-al-celular', 'Roku no responde al celular (error 403)'),
  ('el-celular-no-encuentra-el-tv', 'El celular no encuentra el TV'),
  ('android-tv-codigo-de-emparejamiento', 'Android TV pide un código de emparejamiento'),
  ('perdi-el-control-del-roku', 'Perdí el control del Roku'),
  ('encender-tv-y-hdmi-de-la-consola-sin-control', 'Encender el TV y pasar al HDMI de la consola sin control'),
  ('perdi-el-control-del-tv', 'Perdí el control del TV'),
  ('perdi-el-control-del-lg', 'Perdí el control del TV LG'),
  ('cambiar-entrada-hdmi-sin-control', 'Cambiar la entrada HDMI sin control'),
  ('android-tv-sin-control-remoto', 'Android TV sin control remoto'),
]
MARCAS_PIE = [
  ('control-remoto-samsung', 'Control remoto Samsung'),
  ('control-remoto-lg', 'Control remoto LG'),
  ('control-remoto-roku', 'Control remoto Roku'),
  ('control-remoto-android-tv', 'Control remoto Android TV'),
]

def pie_marcas():
    li = [f'        <li><a href="/{s}/">{n}</a></li>' for s, n in MARCAS_PIE]
    li.append('        <li><a href="/guias/">Todas las guías</a></li>')
    li += [f'        <li><a href="/guias/{s}/">{n}</a></li>' for s, n in GUIAS_PIE]
    return '      <ul class="marcas-enlaces pie-marcas" aria-label="Marcas y guías">\n' + '\n'.join(li) + '\n      </ul>\n'

LOGO = '<img src="/icono.svg?v=8cbaa68330" alt="" width="34" height="34">'
APPLE_SVG = '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M12.152 6.896c-.948 0-2.415-1.078-3.96-1.04-2.04.027-3.91 1.183-4.961 3.014-2.117 3.675-.546 9.103 1.519 12.09 1.013 1.454 2.208 3.09 3.792 3.039 1.52-.065 2.09-.987 3.935-.987 1.831 0 2.35.987 3.96.948 1.637-.026 2.676-1.48 3.676-2.948 1.156-1.688 1.636-3.325 1.662-3.415-.039-.013-3.182-1.221-3.22-4.857-.026-3.04 2.48-4.494 2.597-4.559-1.429-2.09-3.623-2.324-4.39-2.376-2-.156-3.675 1.09-4.61 1.09zM15.53 3.83c.843-1.012 1.4-2.427 1.245-3.83-1.207.052-2.662.805-3.532 1.818-.78.896-1.454 2.338-1.273 3.714 1.338.104 2.715-.688 3.559-1.701"/></svg>'
MS_SVG = '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="#f25022" d="M1 1h10.5v10.5H1z"/><path fill="#7fba00" d="M12.5 1H23v10.5H12.5z"/><path fill="#00a4ef" d="M1 12.5h10.5V23H1z"/><path fill="#ffb900" d="M12.5 12.5H23V23H12.5z"/></svg>'

def otras(actual):
    return '\n'.join(f'        <li><a href="/{g["slug"]}/">{html.escape(g["h1"])}</a></li>' for g in GUIAS if g is not actual)

ORG = {"@type": "Organization", "@id": URL + "/#org", "name": "Mando TV", "url": URL + "/"}

import re
def fmt(t):
    """Escapa el texto y convierte [texto](/ruta/) en enlaces internos."""
    return re.sub(r'\[([^\]]+)\]\((/[^)\s]*)\)', lambda m: f'<a href="{m[2]}">{m[1]}</a>', html.escape(t))

def plano(t):
    """Texto sin la marca de enlaces, para los datos estructurados."""
    return re.sub(r'\[([^\]]+)\]\((/[^)\s]*)\)', r'\1', t)

# hreflang de todas las gemelas (es, en, de, fr...): salen de idiomas_sitio.py.
def alternos_en(slug):
    clave = idiomas_sitio.clave_es(slug)
    return idiomas_sitio.alternos(clave) if clave else None

def hreflangs(alternos):
    if not alternos:
        return ''
    filas = [f'  <link rel="alternate" hreflang="{l}" href="{u}">' for l, u in alternos.items()]
    filas.append(f'  <link rel="alternate" hreflang="x-default" href="{alternos.get("en") or alternos["es"]}">')
    return chr(10).join(filas) + chr(10)

def howto(nombre, desc, lang, pasos):
    return {"@type": "HowTo", "name": nombre, "description": desc, "inLanguage": lang,
            "step": [{"@type": "HowToStep", "position": n, "text": plano(p)} for n, p in enumerate(pasos, 1)]}

def tabla_html(t):
    """Tabla comparativa (igual que en generar_en.py): en el celular se desplaza dentro de su caja."""
    e = html.escape
    cabeza = ''.join(f'<th scope="col">{e(c)}</th>' for c in t['cabeza'])
    filas = '\n'.join('            <tr><th scope="row">' + e(f[0]) + '</th>' + ''.join(f'<td>{e(c)}</td>' for c in f[1:]) + '</tr>' for f in t['filas'])
    nota = f'\n      <p class="nota">{fmt(t["nota"])}</p>' if t.get('nota') else ''
    return f'''      <h2 id="comparacion">{e(t["titulo"])}</h2>
      <div class="tabla" role="region" aria-labelledby="comparacion" tabindex="0">
        <table>
          <thead><tr>{cabeza}</tr></thead>
          <tbody>
{filas}
          </tbody>
        </table>
      </div>''' + nota

def pagina(g):
    e = html.escape
    url = f'{URL}/{g["slug"]}/'
    ld = {"@context": "https://schema.org", "@graph": [
      {"@type": "Article", "headline": g["h1"], "description": g["desc"], "inLanguage": "es",
       "datePublished": g.get("fecha", FECHA), "dateModified": g.get("modificada", g.get("fecha", FECHA)), "mainEntityOfPage": url, "image": URL + "/social.png",
       "author": {"@id": URL + "/#org"}, "publisher": {"@id": URL + "/#org"}},
      ORG,
      howto(g["h1"], g["desc"], "es", g["pasos"]),
      {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Inicio", "item": URL + "/es/"},
        {"@type": "ListItem", "position": 2, "name": "Guías", "item": URL + "/guias/"},
        {"@type": "ListItem", "position": 3, "name": g["h1"], "item": url}]},
      {"@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in g["faq"]]}]}
    ms, intro = '', e(g['intro'])
    if idiomas_sitio.es_guia_pc(g['slug']):  # ficha de Microsoft Store visible, enlazada y en JSON-LD (GEO, 23-nov)
        ld['@graph'].append(idiomas_sitio.app_windows(url))
        ms = '\n      ' + idiomas_sitio.linea_ms_store('es')
        intro = idiomas_sitio.enlazar_mando(intro)
    pasos = '\n'.join(f'        <li>{fmt(p)}</li>' for p in g['pasos'])
    extra = '\n\n'.join(f'      <h2>{e(t)}</h2>\n      <p>{fmt(p)}</p>' for t, p in g['extra'])
    if g.get('tabla'):
        extra = tabla_html(g['tabla']) + '\n\n' + extra
    faq = '\n'.join(f'        <details><summary>{e(q)}</summary><p>{e(a)}</p></details>' for q, a in g['faq'])
    if g['marca']:
        marcas = f'<p>Más detalles en la página de <a href="/{g["marca"][0]}/">{e(g["marca"][1])}</a>.</p>'
    else:
        marcas = '<p>Más detalles por marca:</p>\n      <ul>\n' + '\n'.join(f'        <li><a href="/{s}/">{e(n)}</a></li>' for s, n in MARCAS_ENLACES) + '\n      </ul>'
    return f'''<!doctype html>
<html lang="es" style="--marca: #3d7bff">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="apple-itunes-app" content="app-id=6834927348">
  <title>{e(g["titulo"])}</title>
  <meta name="description" content="{e(g["desc"])}">
  <meta name="robots" content="index, follow, max-image-preview:large">
  <meta name="theme-color" content="#3d7bff">
  <link rel="canonical" href="{url}">
{hreflangs(alternos_en(g["slug"]) or g.get("alternos"))}  <meta property="og:site_name" content="Mando TV">
  <meta property="og:locale" content="es_LA">
  <meta property="og:type" content="article">
  <meta property="og:url" content="{url}">
  <meta property="og:title" content="{e(g["titulo"])}">
  <meta property="og:description" content="{e(g["desc"])}">
  <meta property="og:image" content="{URL}/social.png">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="apple-touch-icon" href="/apple-touch-icon.png">
  <link rel="icon" href="/icono.svg" type="image/svg+xml">
  <link rel="stylesheet" href="/estilos.css?v=12">
  <script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
</head>
<body>
  <div class="cabecera-pagina">
    <div class="contenedor">
      <header class="barra">
        <a class="logo" href="/es/" aria-label="Mando TV, inicio">
          {LOGO}
          Mando TV
        </a>
        <nav aria-label="Principal">
          <a href="/es/#funciones">Qué hace</a>
          <a href="/soporte.html">Ayuda</a>
          <a class="boton-barra" href="mailto:hola@mandotv.app?subject=Hola%20Mando%20TV">Contacto</a>
        </nav>
      </header>
      <nav class="migas" aria-label="Ruta"><a href="/es/">Inicio</a> / <a href="/guias/">Guías</a> / <span>{e(g["corto"])}</span></nav>
      <h1>{e(g["h1"])}</h1>
      <p>{intro}</p>
      <div class="acciones">
        <a class="boton" href="#pasos">Ver los pasos</a>
        <a class="boton claro" href="#mando-tv">Descargar gratis</a>
      </div>
    </div>
  </div>

  <main class="contenedor">
    <div class="documento">
      <h2 id="pasos">Paso a paso</h2>
      <ol>
{pasos}
      </ol>

{extra}

      <h2 id="mando-tv">Hazlo con Mando TV</h2>
      <p>Mando TV es un control remoto universal para tu televisor. Descárgalo gratis, sin anuncios y sin cuenta. Pro es un pago único opcional, sin suscripción. Para iPhone, iPad, Windows y Android:</p>
      <ul class="tiendas" aria-label="Descargar Mando TV">
        <li><a class="tienda" href="{TIENDA_APPLE}" target="_blank" rel="noopener" aria-label="Descargar Mando TV gratis en App Store">{APPLE_SVG}<span><small>Descárgalo en</small>App Store</span></a></li>
        <li><a class="tienda" href="{TIENDA}" target="_blank" rel="noopener" aria-label="Descargar Mando TV gratis en Microsoft Store">{MS_SVG}<span><small>Descárgalo en</small>Microsoft Store</span></a></li>
        <li><a class="tienda" href="/es/#android" aria-label="Prueba anticipada de Mando TV en Google Play para Android"><svg viewBox="0 0 24 24" aria-hidden="true"><path fill="#00d7fe" d="M1.337.924a1.486 1.486 0 0 0-.112.568v21.017c0 .217.045.419.124.6l11.155-11.087L1.337.924z"/><path fill="#ffce00" d="M22.018 13.298l-3.919 2.218-3.515-3.493 3.543-3.521 3.891 2.202a1.49 1.49 0 0 1 0 2.594z"/><path fill="#00f076" d="M13.544 10.989l3.258-3.238L3.45.195a1.466 1.466 0 0 0-.946-.179l11.04 10.973z"/><path fill="#ff3a44" d="M13.544 13.056l-11 10.933c.298.036.612-.016.906-.183l13.324-7.54-3.23-3.21z"/></svg><span><small>Prueba anticipada en</small>Google Play</span></a></li>
      </ul>
      <p class="nota">Android: prueba anticipada gratis en Google Play. <a href="/es/#android">Únete en dos pasos</a> y ayúdanos a llegar a la tienda.</p>{ms}
      {marcas}

      <h2 id="preguntas">Preguntas frecuentes</h2>
      <div class="preguntas">
{faq}
      </div>

      <h2 id="otras">Otras guías</h2>
      <ul>
{otras(g)}
        <li><a href="/guias/">Todas las guías</a></li>
        <li><a href="/soporte.html">Ayuda y soporte</a></li>
      </ul>
    </div>
  </main>

  <footer class="pie">
    <div class="contenedor">
      <div class="pie-enlaces">
        <nav aria-label="Pie de página">
          <a href="/es/">Inicio</a>
          <a href="/soporte.html">Ayuda</a>
          <a href="/privacidad.html">Privacidad</a>
          <a href="mailto:hola@mandotv.app">hola@mandotv.app</a>
          <button type="button" class="enlace-cookies" data-cookies>Cookies</button>
        </nav>
        <span>Hecho en Chile</span>
      </div>
{pie_marcas()}      <p class="pie-gigante" aria-hidden="true">MANDO</p>
      <small>Mando TV es una app independiente: no está afiliada a los fabricantes de televisores nombrados ni a Google, Amazon, Apple o Roku, ni cuenta con su respaldo. Las marcas pertenecen a sus dueños y se mencionan solo para indicar compatibilidad. Android TV y Google TV son marcas de Google LLC. Apple TV es una marca de Apple Inc.</small>
    </div>
  </footer>
  <script src="/correo.js?v=3" defer></script>
  <script src="/cookies.js?v=1" defer></script>
  <!-- Cloudflare Web Analytics: cuenta visitas sin cookies ni datos personales -->
  <script defer src="https://static.cloudflareinsights.com/beacon.min.js" data-cf-beacon='{{"token": "3a3f0250e4b04d5884b033b9a94302b4"}}'></script>
</body>
</html>
'''

def indice():
    e = html.escape
    url = f'{URL}/guias/'
    titulo = 'Guías para controlar tu TV con el celular | Mando TV'
    desc = 'Guías paso a paso para usar tu celular o PC como control remoto del TV: encender el TV, conectar por WiFi y resolver problemas en Samsung, LG y Roku.'
    ld = {"@context": "https://schema.org", "@graph": [
      ORG,
      {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Inicio", "item": URL + "/es/"},
        {"@type": "ListItem", "position": 2, "name": "Guías", "item": url}]},
      {"@type": "CollectionPage", "name": "Guías para usar tu celular como control remoto del TV", "description": desc, "url": url, "inLanguage": "es",
       "publisher": {"@id": URL + "/#org"},
       "mainEntity": {"@type": "ItemList", "itemListElement": [
         {"@type": "ListItem", "position": n, "name": g["h1"], "url": f'{URL}/{g["slug"]}/'} for n, g in enumerate(GUIAS, 1)]}}]}
    lista = '\n'.join(f'        <li><a href="/{g["slug"]}/">{e(g["h1"])}</a>: {e(g["desc"])}</li>' for g in GUIAS)
    return f"""<!doctype html>
<html lang="es" style="--marca: #3d7bff">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="apple-itunes-app" content="app-id=6834927348">
  <title>{e(titulo)}</title>
  <meta name="description" content="{e(desc)}">
  <meta name="robots" content="index, follow, max-image-preview:large">
  <meta name="theme-color" content="#3d7bff">
  <link rel="canonical" href="{url}">
{hreflangs(idiomas_sitio.alternos('guias'))}  <meta property="og:site_name" content="Mando TV">
  <meta property="og:locale" content="es_LA">
  <meta property="og:type" content="website">
  <meta property="og:url" content="{url}">
  <meta property="og:title" content="{e(titulo)}">
  <meta property="og:description" content="{e(desc)}">
  <meta property="og:image" content="{URL}/social.png">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="apple-touch-icon" href="/apple-touch-icon.png">
  <link rel="icon" href="/icono.svg" type="image/svg+xml">
  <link rel="stylesheet" href="/estilos.css?v=12">
  <script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
</head>
<body>
  <div class="cabecera-pagina">
    <div class="contenedor">
      <header class="barra">
        <a class="logo" href="/es/" aria-label="Mando TV, inicio">
          {LOGO}
          Mando TV
        </a>
        <nav aria-label="Principal">
          <a href="/es/#funciones">Qué hace</a>
          <a href="/soporte.html">Ayuda</a>
          <a class="boton-barra" href="mailto:hola@mandotv.app?subject=Hola%20Mando%20TV">Contacto</a>
        </nav>
      </header>
      <nav class="migas" aria-label="Ruta"><a href="/es/">Inicio</a> / <span>Guías</span></nav>
      <h1>Guías para usar tu celular como control remoto del TV</h1>
      <p>Pasos simples para conectar, encender y arreglar el control de tu televisor Samsung, LG, Roku o Android TV con Mando TV.</p>
    </div>
  </div>

  <main class="contenedor">
    <div class="documento">
      <h2 id="guias">Todas las guías</h2>
      <ul>
{lista}
      </ul>

      <h2 id="marcas">Control remoto por marca</h2>
      <ul>
{chr(10).join(f'        <li><a href="/{s}/">{e(n)}</a></li>' for s, n in MARCAS_ENLACES)}
        <li><a href="/soporte.html">Ayuda y soporte</a></li>
      </ul>
    </div>
  </main>

  <footer class="pie">
    <div class="contenedor">
      <div class="pie-enlaces">
        <nav aria-label="Pie de página">
          <a href="/es/">Inicio</a>
          <a href="/soporte.html">Ayuda</a>
          <a href="/privacidad.html">Privacidad</a>
          <a href="mailto:hola@mandotv.app">hola@mandotv.app</a>
          <button type="button" class="enlace-cookies" data-cookies>Cookies</button>
        </nav>
        <span>Hecho en Chile</span>
      </div>
{pie_marcas()}      <p class="pie-gigante" aria-hidden="true">MANDO</p>
      <small>Mando TV es una app independiente: no está afiliada a los fabricantes de televisores nombrados ni a Google, Amazon, Apple o Roku, ni cuenta con su respaldo. Las marcas pertenecen a sus dueños y se mencionan solo para indicar compatibilidad. Android TV y Google TV son marcas de Google LLC. Apple TV es una marca de Apple Inc.</small>
    </div>
  </footer>
  <script src="/correo.js?v=3" defer></script>
  <script src="/cookies.js?v=1" defer></script>
  <!-- Cloudflare Web Analytics: cuenta visitas sin cookies ni datos personales -->
  <script defer src="https://static.cloudflareinsights.com/beacon.min.js" data-cf-beacon='{{"token": "3a3f0250e4b04d5884b033b9a94302b4"}}'></script>
</body>
</html>
"""

os.makedirs(os.path.join(SITIO, 'guias'), exist_ok=True)
open(os.path.join(SITIO, 'guias', 'index.html'), 'w', encoding='utf-8', newline='\n').write(indice())
print('ok guias/ (índice)')

for g in GUIAS:
    d = os.path.join(SITIO, *g['slug'].split('/'))
    os.makedirs(d, exist_ok=True)
    open(os.path.join(d, 'index.html'), 'w', encoding='utf-8', newline='\n').write(pagina(g))
    print('ok', g['slug'], len(g['titulo']), len(g['desc']))


# ---------------------------------------------------------------------------------------------------------------
# Versiones en otros idiomas de la guía de la consola (2026-11-17): /en/guides/... (las demás: generar_idiomas.py)
# Textos escritos para cada idioma (no son traducción literal). hreflang de idiomas_sitio.py.
# ---------------------------------------------------------------------------------------------------------------
GPLAY_SVG = '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="#00d7fe" d="M1.337.924a1.486 1.486 0 0 0-.112.568v21.017c0 .217.045.419.124.6l11.155-11.087L1.337.924z"/><path fill="#ffce00" d="M22.018 13.298l-3.919 2.218-3.515-3.493 3.543-3.521 3.891 2.202a1.49 1.49 0 0 1 0 2.594z"/><path fill="#00f076" d="M13.544 10.989l3.258-3.238L3.45.195a1.466 1.466 0 0 0-.946-.179l11.04 10.973z"/><path fill="#ff3a44" d="M13.544 13.056l-11 10.933c.298.036.612-.016.906-.183l13.324-7.54-3.23-3.21z"/></svg>'

ALT_CONSOLA = idiomas_sitio.alternos('console')  # todas las gemelas activas

UI = {
  'en': dict(lang='en', locale='en_US', inicio='Home', ayuda='Help', contacto='Contact', ver='See the steps', bajar='Download free',
    pasos='Step by step', hazlo='Do it with Mando TV', faq='Frequently asked questions', idiomas='This guide in other languages',
    nombres={'es': 'Español', 'en': 'English', 'pt': 'Português (Brasil)'},
    tiendas='Mando TV is a universal TV remote. Download it free, with no ads and no account. Pro is an optional one-time purchase, no subscription. For iPhone, iPad, Windows and Android:',
    apple_aria='Download Mando TV free on the App Store', ms_aria='Download Mando TV free on Microsoft Store',
    gp_aria='Early access to Mando TV on Google Play for Android', descarga='Download on', anticipada='Early access on',
    nota='Android: free early access on Google Play. <a href="/#android">Join in two steps</a> and help us reach the store.',
    aviso='Mando TV is an independent app. It is not affiliated with or endorsed by the TV makers named, Google, Amazon, Apple or Roku. Trademarks belong to their owners and are used only to indicate compatibility. Android TV and Google TV are trademarks of Google LLC. Apple TV is a trademark of Apple Inc.',
    migas_inicio='Home', pie='Footer', principal='Main', ruta='Breadcrumb', aria_desc='Download Mando TV', privacidad='Privacy',
    guia_nombre='Guide'),
}

I18N = [
  dict(idioma='en', slug='en/guides/turn-on-tv-console-hdmi-without-remote', corto='TV and console without a remote', fecha='2026-11-17',
    titulo='No TV Remote? Turn On the TV and Switch to Console HDMI',
    desc='Launch day and no TV remote? Turn on your TV and switch to your PS5 or Xbox HDMI input from your phone. Free, no ads.',
    h1="How to turn on the TV and switch to your console's HDMI without the remote",
    intro="GTA VI launch day, the console ready to go, and the TV remote lost somewhere in the couch. It happens more than you would think. With Mando TV your phone turns on the TV and switches it to your PlayStation or Xbox input, over your home Wi-Fi.",
    pasos=[
      'Connect your phone to the same Wi-Fi network as the TV.',
      'Open Mando TV and tap your TV in the list (Samsung, LG, Roku or Android TV).',
      'If the TV is off, tap Turn on. This works if the TV has power-on over the network enabled. If you never turned that on, switch the TV on this one time with the button on the TV itself, and enable it for next time.',
      'Turn on the console. If HDMI-CEC is enabled (see the free trick below), the TV switches to its input on its own.',
      'If it does not switch, tap Inputs in Mando TV and pick the HDMI port the console is plugged into: HDMI 1, HDMI 2 and so on.',
      'For the volume, use the big buttons in the app while you play.',
    ],
    extra=[
      ('The free trick: let the console switch the TV for you', 'The PS5 and the Xbox can turn on the TV and jump to their HDMI input as soon as they start, thanks to HDMI-CEC. On the PS5 it is under Settings > System > HDMI > Enable HDMI Device Link. On the Xbox, open Settings > General > TV & display options and look for the device control option. On the TV the feature has a different name depending on the brand: Anynet+ on Samsung, SIMPLINK on LG, and BRAVIA Sync or HDMI control on others.'),
      ('If the TV stays on another screen', 'If the console is on but the TV still shows the antenna or an app, the TV did not change input. From your phone, tap Inputs and choose the console HDMI. If you prefer, use the arrows and OK to reach the TV inputs, or press the button on the TV itself, and pick the HDMI. The number is the port where you plugged in the console cable.'),
      ('If it is a Roku TV', 'The physical button on the TV, usually at the bottom center or on the back, turns it on. From there your phone does the rest.'),
    ],
    faq=[
      ('Does Mando TV have anything to do with GTA VI?', 'No. Mando TV is not affiliated with Rockstar Games or Take-Two. It only helps you avoid losing game time because you cannot find the TV remote.'),
      ('Is switching the HDMI input free?', 'Yes. The inputs list in Mando TV is free, just like turning the TV on and using the arrows, OK and volume. You can also let the console switch the input by itself with HDMI-CEC.'),
      ('Will it work with my TV?', 'It works with Samsung, LG, Roku and Android TV sets on the same Wi-Fi network. If yours is another brand, the HDMI-CEC trick can still help.'),
      ('Can I use it to play GTA VI (GTA 6) on PS5 or Xbox?', 'Mando TV does not touch the console or the game. It only gets the TV turned on and on the right HDMI input so you can sit down and play.'),
    ]),
]


def pagina_idioma(g):
    e = html.escape
    u = UI[g['idioma']]
    url = f'{URL}/{g["slug"]}/'
    lang = u['lang']
    ld = {"@context": "https://schema.org", "@graph": [
      {"@type": "Article", "headline": g["h1"], "description": g["desc"], "inLanguage": lang,
       "datePublished": g["fecha"], "dateModified": g["fecha"], "mainEntityOfPage": url, "image": URL + f"/social-{g['idioma']}.png",
       "author": {"@id": URL + "/#org"}, "publisher": {"@id": URL + "/#org"}},
      ORG,
      howto(g["h1"], g["desc"], lang, g["pasos"]),
      {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": u['inicio'], "item": URL + "/"},
        {"@type": "ListItem", "position": 2, "name": g["h1"], "item": url}]},
      {"@type": "FAQPage", "inLanguage": lang, "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in g["faq"]]}]}
    ms = ''
    if idiomas_sitio.es_guia_pc(g['slug']):  # ficha de Microsoft Store visible y en JSON-LD (GEO, 23-nov)
        ld['@graph'].append(idiomas_sitio.app_windows(url))
        ms = '\n      ' + idiomas_sitio.linea_ms_store(g['idioma'])
    pasos = '\n'.join(f'        <li>{e(p)}</li>' for p in g['pasos'])
    extra = '\n\n'.join(f'      <h2>{e(t)}</h2>\n      <p>{e(p)}</p>' for t, p in g['extra'])
    faq = '\n'.join(f'        <details><summary>{e(q)}</summary><p>{e(a)}</p></details>' for q, a in g['faq'])
    idiomas = '\n'.join(f'        <li><a href="{ALT_CONSOLA[l][len(URL):]}" hreflang="{l}" lang="{l}">{idiomas_sitio.NOMBRES[l]}</a></li>' for l in ALT_CONSOLA if l != g['idioma'])
    return f'''<!doctype html>
<html lang="{lang}" style="--marca: #3d7bff">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="apple-itunes-app" content="app-id=6834927348">
  <title>{e(g["titulo"])}</title>
  <meta name="description" content="{e(g["desc"])}">
  <meta name="robots" content="index, follow, max-image-preview:large">
  <meta name="theme-color" content="#3d7bff">
  <link rel="canonical" href="{url}">
{hreflangs(ALT_CONSOLA)}  <meta property="og:site_name" content="Mando TV">
  <meta property="og:locale" content="{u["locale"]}">
  <meta property="og:type" content="article">
  <meta property="og:url" content="{url}">
  <meta property="og:title" content="{e(g["titulo"])}">
  <meta property="og:description" content="{e(g["desc"])}">
  <meta property="og:image" content="{URL}/social-{g["idioma"]}.png">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="apple-touch-icon" href="/apple-touch-icon.png">
  <link rel="icon" href="/icono.svg" type="image/svg+xml">
  <link rel="stylesheet" href="/estilos.css?v=12">
  <script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
</head>
<body>
  <div class="cabecera-pagina">
    <div class="contenedor">
      <header class="barra">
        <a class="logo" href="/" aria-label="Mando TV, {u["inicio"]}">
          {LOGO}
          Mando TV
        </a>
        <nav aria-label="{u["principal"]}">
          <a href="/soporte.html">{u["ayuda"]}</a>
          <a class="boton-barra" href="mailto:hola@mandotv.app?subject=Hello%20Mando%20TV">{u["contacto"]}</a>
        </nav>
      </header>
      <nav class="migas" aria-label="{u["ruta"]}"><a href="/">{u["migas_inicio"]}</a> / <span>{e(g["corto"])}</span></nav>
      <h1>{e(g["h1"])}</h1>
      <p>{e(g["intro"])}</p>
      <div class="acciones">
        <a class="boton" href="#pasos">{u["ver"]}</a>
        <a class="boton claro" href="#mando-tv">{u["bajar"]}</a>
      </div>
    </div>
  </div>

  <main class="contenedor">
    <div class="documento">
      <h2 id="pasos">{u["pasos"]}</h2>
      <ol>
{pasos}
      </ol>

{extra}

      <h2 id="mando-tv">{u["hazlo"]}</h2>
      <p>{u["tiendas"]}</p>
      <ul class="tiendas" aria-label="{u["aria_desc"]}">
        <li><a class="tienda" href="{TIENDA_APPLE}" target="_blank" rel="noopener" aria-label="{u["apple_aria"]}">{APPLE_SVG}<span><small>{u["descarga"]}</small>App Store</span></a></li>
        <li><a class="tienda" href="{TIENDA}" target="_blank" rel="noopener" aria-label="{u["ms_aria"]}">{MS_SVG}<span><small>{u["descarga"]}</small>Microsoft Store</span></a></li>
        <li><a class="tienda" href="/#android" aria-label="{u["gp_aria"]}">{GPLAY_SVG}<span><small>{u["anticipada"]}</small>Google Play</span></a></li>
      </ul>
      <p class="nota">{u["nota"]}</p>{ms}

      <h2 id="preguntas">{u["faq"]}</h2>
      <div class="preguntas">
{faq}
      </div>

      <h2 id="otras">{u["idiomas"]}</h2>
      <ul>
{idiomas}
      </ul>
    </div>
  </main>

  <footer class="pie">
    <div class="contenedor">
      <div class="pie-enlaces">
        <nav aria-label="{u["pie"]}">
          <a href="/">{u["inicio"]}</a>
          <a href="/soporte.html">{u["ayuda"]}</a>
          <a href="/privacidad.html">{u["privacidad"]}</a>
          <a href="mailto:hola@mandotv.app">hola@mandotv.app</a>
          <button type="button" class="enlace-cookies" data-cookies>Cookies</button>
        </nav>
        <span>Made in Chile</span>
      </div>
      <p class="pie-gigante" aria-hidden="true">MANDO</p>
      <small>{u["aviso"]}</small>
    </div>
  </footer>
  <script src="/correo.js?v=3" defer></script>
  <script src="/cookies.js?v=1" defer></script>
  <!-- Cloudflare Web Analytics: cuenta visitas sin cookies ni datos personales -->
  <script defer src="https://static.cloudflareinsights.com/beacon.min.js" data-cf-beacon='{{"token": "3a3f0250e4b04d5884b033b9a94302b4"}}'></script>
</body>
</html>
'''


for g in I18N:
    d = os.path.join(SITIO, *g['slug'].split('/'))
    os.makedirs(d, exist_ok=True)
    open(os.path.join(d, 'index.html'), 'w', encoding='utf-8', newline='\n').write(pagina_idioma(g))
    print('ok', g['slug'], len(g['titulo']), len(g['desc']))
