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
      'Listo, ya puedes usar el celular como control. Los botones y el teclado son gratis; el touchpad y las apps son función Pro.',
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
    desc='Usa tu PC con Windows como control remoto del TV Samsung, LG, Roku o Google TV por WiFi. Botones y teclado gratis; apps y atajos del PC con Pro.',
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
    ],
    marca=None,
    faq=[
      ('¿Necesito un cable o Bluetooth para controlar el TV desde el PC?', 'No. Mando TV se conecta por la red de tu casa: basta con que el PC y el TV estén en el mismo router.'),
      ('¿Funciona con cualquier TV?', 'Con Samsung con Tizen (2016 en adelante), LG con webOS, Roku y Google TV o Android TV (Sony, TCL, Philips, Xiaomi y otros).'),
      ('¿Cuánto cuesta?', 'Los botones, el teclado y el encendido por red son gratis y sin anuncios. Mando TV Pro es un pago único, sin suscripción, para funciones extra como el touchpad, las apps, los atajos del teclado del PC y el mini control.'),
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
      ('Dónde ver la dirección IP del TV', 'Está en el menú de red del televisor y cambia un poco según el modelo. En LG: Configuración > Red > Conexión Wi-Fi, en los ajustes avanzados. En Samsung: Configuración > General > Red > Estado de red > Configuración de IP. En Roku: Configuración > Red > Acerca de. En Android TV y Google TV: Configuración > Red e Internet, tocando tu red. Es un número como 192.168.1.86.'),
      ('Si aparece pero se corta al conectar', 'Cuando la conexión se cae a los pocos segundos, el corte suele venir del teléfono: una VPN, un cambio de red WiFi o el ahorro de batería. Apaga la VPN, quédate en el mismo WiFi y vuelve a intentar.'),
      ('WiFi de 2,4 y de 5 GHz', 'No importa que el celular esté en la red de 5 GHz y el TV en la de 2,4, siempre que las dos salgan del mismo router. Si tienes un repetidor y el TV sigue sin aparecer, acerca el celular al router principal y prueba de nuevo.'),
    ],
    marca=None,
    faq=[
      ('¿Puedo controlar el TV con datos móviles?', 'No. El control viaja por la red WiFi de tu casa, así que el celular y el TV deben estar en la misma red.'),
      ('¿Por qué con la VPN no funciona?', 'Porque la VPN manda todo el tráfico del celular por otra red y el teléfono deja de ver los aparatos de tu casa. Apágala mientras usas el control.'),
      ('¿Sirve el Bluetooth o el infrarrojo?', 'Mando TV usa solo WiFi. No necesita Bluetooth ni que el celular tenga infrarrojo.'),
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
      ('¿Qué televisores usan este código?', 'Los que traen Android TV o Google TV: Sony, TCL, Philips, Xiaomi, el Chromecast con Google TV y varios más.'),
      ('¿Necesito una cuenta de Google en el celular?', 'No. El código de la pantalla es lo único que hace falta.'),
      ('¿Es seguro?', 'Sí. El código demuestra que estás frente al TV: sin verlo en la pantalla nadie puede emparejarse.'),
    ]),
  dict(slug='guias/perdi-el-control-del-roku', corto='Perdí el control del Roku', fecha='2026-11-17',
    titulo='Perdí el control del Roku: usa tu celular | Mando TV',
    desc='Si perdiste el control del Roku, tu celular lo reemplaza por WiFi. Pasos simples, y qué hacer si cambiaste de router y el Roku quedó sin conexión.',
    h1='Perdí el control del Roku: cómo usar el celular',
    intro='Si se te perdió el control del Roku o dejó de funcionar, el celular lo reemplaza, siempre que el Roku siga conectado a tu WiFi. Y si cambiaste de WiFi o de router, también hay una salida.',
    pasos=[
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
      'Si no cambia solo, toca Entradas en Mando TV (función Pro) y elige el HDMI donde está la consola (HDMI 1, HDMI 2...).',
      'Para el volumen, usa los botones grandes de la app mientras juegas.',
    ],
    extra=[
      ('El truco gratis: que la consola cambie el TV sola', 'La PS5 y la Xbox pueden encender el televisor y pasarlo a su HDMI apenas se encienden, gracias a HDMI-CEC. En la PS5 está en Configuración > Sistema > HDMI > Activar Enlace de dispositivos HDMI. En la Xbox, en Configuración > General > Opciones de TV y pantalla > Control de dispositivos. En el televisor tiene otro nombre según la marca: Anynet+ en Samsung, SIMPLINK en LG y Control de dispositivos HDMI o BRAVIA Sync en otras.'),
      ('Si es un Roku TV', 'El botón físico del televisor, casi siempre abajo al centro o detrás, lo enciende. Desde ahí el celular hace el resto.'),
      ('Si el TV se queda en otra pantalla', 'Si la consola está encendida pero el televisor sigue en la antena o en una app, el TV no cambió de entrada. Con el celular, toca Entradas (función Pro) y elige el HDMI de la consola. Sin Pro, usa las flechas y OK para llegar a las entradas del TV, o el botón del propio televisor, y elige el HDMI. El número es el del puerto donde enchufaste el cable de la consola.'),
      ('Más ayuda', 'Si no sabes por dónde empezar, mira [Perdí el control del TV](/guias/perdi-el-control-del-tv/). Para solo cambiar de entrada, está la guía [Cambiar la entrada HDMI del TV sin control remoto](/guias/cambiar-entrada-hdmi-sin-control/).'),
    ],
    marca=None,
    faq=[
      ('¿Mando TV tiene algo que ver con GTA VI?', 'No. Mando TV no está afiliado a Rockstar Games ni a Take-Two. Solo te ayuda a que no te quedes sin jugar por no encontrar el control del televisor.'),
      ('¿Cambiar de entrada HDMI es gratis?', 'La lista de entradas es parte de Mando TV Pro, un pago único sin suscripción. Gratis puedes encender el TV, usar las flechas, OK y el volumen, y dejar que la consola cambie la entrada sola con HDMI-CEC.'),
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
      ('Lo gratis y lo Pro', 'Encender, apagar, flechas, OK, volumen, canales, números y teclado son gratis. El touchpad, la lista de apps, la lista de entradas, la voz y las rutinas son de Mando TV Pro, un pago único sin suscripción.'),
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
      'Listo. Las flechas, OK, Atrás, Inicio, volumen, canales y teclado son gratis. El puntero, la lista de apps y la de entradas son función Pro.',
      'Con la app conectada, entra en Configuración con las flechas y OK, y activa "Encender TV con móvil". La guía [Cómo encender el TV LG con el celular](/guias/encender-tv-lg-con-el-celular/) dice dónde está.',
    ],
    extra=[
      ('Si el TV no muestra el aviso', 'Puede que el permiso ya esté guardado, o que el celular esté en otra red. Revisa que los dos estén en el mismo WiFi y que la VPN esté apagada. Si el TV no aparece en la lista, mira [El celular no encuentra el TV](/guias/el-celular-no-encuentra-el-tv/).'),
      ('Si el TV quedó sin WiFi', 'Conecta el TV con un cable de red al router: lo usa solo. O crea una red WiFi con el mismo nombre y la misma clave de antes, porque el TV suele conectarse solo a ella.'),
      ('Si el TV quedó en otra entrada', 'Con el celular, toca Entradas (función Pro) y elige el HDMI. Más detalles en [Cambiar la entrada HDMI del TV sin control remoto](/guias/cambiar-entrada-hdmi-sin-control/).'),
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
      'En LG y Roku, toca Entradas (función Pro) y elige el HDMI. En Samsung, Entradas (función Pro) manda la tecla Fuente del TV y eliges con las flechas y OK.',
      'Sin Pro también se puede: con las flechas y OK ve a las entradas de la pantalla de inicio del TV. Según la marca y el año, se llaman Fuente, Dispositivos conectados o Entradas. En un Roku TV son las tarjetas HDMI de la pantalla de inicio.',
    ],
    extra=[
      ('Samsung', 'Si el menú del botón del TV no tiene Fuente, abre el menú de la pantalla de inicio con el celular y busca Fuente o Dispositivos conectados a la izquierda. Se maneja con las flechas y OK de Mando TV, que son gratis.'),
      ('LG', 'Presiona el joystick del TV y busca Entradas. Con el celular, en Mando TV también puedes abrir la lista de entradas (Pro) y tocar la que quieras.'),
      ('Roku TV', 'En la pantalla de inicio hay una tarjeta por cada entrada, como HDMI 1 o HDMI 2. Muévete con las flechas y entra con OK, gratis.'),
      ('Si es un TV con Android TV o Google TV', 'En Mando TV la lista de entradas todavía no está en Android TV. Usa el botón de entradas del propio TV, o llega a ellas con las flechas y OK desde el inicio. Si no tienes control y quieres conectarlo, mira [Android TV sin control remoto](/guias/android-tv-sin-control-remoto/).'),
      ('Más ayuda', 'Si el TV ni siquiera enciende o no sabes por dónde empezar, mira [Perdí el control del TV](/guias/perdi-el-control-del-tv/). Para jugar en consola, la guía [Encender el TV y cambiar a HDMI sin control](/guias/encender-tv-y-hdmi-de-la-consola-sin-control/) incluye el truco de HDMI-CEC.'),
    ],
    marca=None,
    faq=[
      ('¿Cambiar de entrada HDMI es gratis?', 'La lista de entradas es parte de Mando TV Pro, un pago único sin suscripción. Gratis puedes encender el TV, usar flechas, OK y volumen, y llegar a las entradas desde el menú del TV.'),
      ('¿Cómo sé cuál HDMI usar?', 'Mira los puertos HDMI del TV: cada uno tiene un número. Usa el del puerto donde está enchufado el cable de tu consola o reproductor.'),
      ('¿Qué hago si el TV no se enciende?', 'Enciéndelo con su botón físico. Si ya lo habías conectado antes y activaste el encendido por red, también puedes encenderlo desde el celular.'),
    ]),
  dict(slug='guias/android-tv-sin-control-remoto', corto='Android TV sin control', fecha='2026-11-17',
    titulo='Android TV sin control remoto: úsalo desde el celular',
    desc='¿Sin el control de tu Android TV o Google TV? Conecta el celular con el código de 6 caracteres de la pantalla. Gratis, sin cuenta y sin anuncios.',
    h1='Android TV sin control remoto: cómo usarlo desde el celular',
    intro='Si perdiste el control de tu Android TV o Google TV, o se quedó sin pilas, el celular lo reemplaza. Lo mejor es que conectarlo no necesita el control: el TV muestra un código en la pantalla y lo escribes en el celular. Sirve en Sony, TCL, Philips, Xiaomi, Hisense con Android TV, Chromecast con Google TV y Nvidia Shield.',
    pasos=[
      'Enciende el TV con su botón físico. Casi siempre está abajo, al centro, o detrás en una esquina.',
      'Conecta el celular al mismo WiFi que el TV.',
      'Descarga Mando TV, que es gratis y no pide cuenta de Google, y ábrela. Toca tu TV en la lista.',
      'El TV muestra un código de 6 letras y números. Escríbelo en el celular y toca Emparejar. No necesitas el control para esto.',
      'Ya puedes usar las flechas, OK, Atrás, Inicio, volumen, silencio y teclado. Son gratis. El touchpad y la lista de apps son Pro.',
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

LOGO = '<img src="/icono.svg?v=1a26271c80" alt="" width="34" height="34">'
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
    filas.append(f'  <link rel="alternate" hreflang="x-default" href="{alternos["es"]}">')
    return chr(10).join(filas) + chr(10)

def howto(nombre, desc, lang, pasos):
    return {"@type": "HowTo", "name": nombre, "description": desc, "inLanguage": lang,
            "step": [{"@type": "HowToStep", "position": n, "text": plano(p)} for n, p in enumerate(pasos, 1)]}

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
        {"@type": "ListItem", "position": 1, "name": "Inicio", "item": URL + "/"},
        {"@type": "ListItem", "position": 2, "name": "Guías", "item": URL + "/guias/"},
        {"@type": "ListItem", "position": 3, "name": g["h1"], "item": url}]},
      {"@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in g["faq"]]}]}
    pasos = '\n'.join(f'        <li>{fmt(p)}</li>' for p in g['pasos'])
    extra = '\n\n'.join(f'      <h2>{e(t)}</h2>\n      <p>{fmt(p)}</p>' for t, p in g['extra'])
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
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..100,600..900&family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/estilos.css?v=12">
  <script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
</head>
<body>
  <div class="cabecera-pagina">
    <div class="contenedor">
      <header class="barra">
        <a class="logo" href="/" aria-label="Mando TV, inicio">
          {LOGO}
          Mando TV
        </a>
        <nav aria-label="Principal">
          <a href="/#funciones">Qué hace</a>
          <a href="/soporte.html">Ayuda</a>
          <a class="boton-barra" href="mailto:hola@mandotv.app?subject=Hola%20Mando%20TV">Contacto</a>
        </nav>
      </header>
      <nav class="migas" aria-label="Ruta"><a href="/">Inicio</a> / <a href="/guias/">Guías</a> / <span>{e(g["corto"])}</span></nav>
      <h1>{e(g["h1"])}</h1>
      <p>{e(g["intro"])}</p>
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
        <li><a class="tienda" href="/#android" aria-label="Prueba anticipada de Mando TV en Google Play para Android"><svg viewBox="0 0 24 24" aria-hidden="true"><path fill="#00d7fe" d="M1.337.924a1.486 1.486 0 0 0-.112.568v21.017c0 .217.045.419.124.6l11.155-11.087L1.337.924z"/><path fill="#ffce00" d="M22.018 13.298l-3.919 2.218-3.515-3.493 3.543-3.521 3.891 2.202a1.49 1.49 0 0 1 0 2.594z"/><path fill="#00f076" d="M13.544 10.989l3.258-3.238L3.45.195a1.466 1.466 0 0 0-.946-.179l11.04 10.973z"/><path fill="#ff3a44" d="M13.544 13.056l-11 10.933c.298.036.612-.016.906-.183l13.324-7.54-3.23-3.21z"/></svg><span><small>Prueba anticipada en</small>Google Play</span></a></li>
      </ul>
      <p class="nota">Android: prueba anticipada gratis en Google Play. <a href="/#android">Únete en dos pasos</a> y ayúdanos a llegar a la tienda.</p>
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
          <a href="/">Inicio</a>
          <a href="/soporte.html">Ayuda</a>
          <a href="/privacidad.html">Privacidad</a>
          <a href="mailto:hola@mandotv.app">hola@mandotv.app</a>
          <button type="button" class="enlace-cookies" data-cookies>Cookies</button>
        </nav>
        <span>Hecho en Chile</span>
      </div>
{pie_marcas()}      <p class="pie-gigante" aria-hidden="true">MANDO</p>
      <small>Mando TV no está afiliado a LG, Samsung, Roku ni Google. Las marcas nombradas pertenecen a sus dueños y se mencionan solo para indicar compatibilidad.</small>
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
        {"@type": "ListItem", "position": 1, "name": "Inicio", "item": URL + "/"},
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
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..100,600..900&family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/estilos.css?v=12">
  <script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
</head>
<body>
  <div class="cabecera-pagina">
    <div class="contenedor">
      <header class="barra">
        <a class="logo" href="/" aria-label="Mando TV, inicio">
          {LOGO}
          Mando TV
        </a>
        <nav aria-label="Principal">
          <a href="/#funciones">Qué hace</a>
          <a href="/soporte.html">Ayuda</a>
          <a class="boton-barra" href="mailto:hola@mandotv.app?subject=Hola%20Mando%20TV">Contacto</a>
        </nav>
      </header>
      <nav class="migas" aria-label="Ruta"><a href="/">Inicio</a> / <span>Guías</span></nav>
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
          <a href="/">Inicio</a>
          <a href="/soporte.html">Ayuda</a>
          <a href="/privacidad.html">Privacidad</a>
          <a href="mailto:hola@mandotv.app">hola@mandotv.app</a>
          <button type="button" class="enlace-cookies" data-cookies>Cookies</button>
        </nav>
        <span>Hecho en Chile</span>
      </div>
{pie_marcas()}      <p class="pie-gigante" aria-hidden="true">MANDO</p>
      <small>Mando TV no está afiliado a LG, Samsung, Roku ni Google. Las marcas nombradas pertenecen a sus dueños y se mencionan solo para indicar compatibilidad.</small>
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
    aviso='Mando TV is not affiliated with LG, Samsung, Roku or Google. Brands named belong to their owners and are mentioned only to show compatibility.',
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
      'If it does not switch, tap Inputs in Mando TV (a Pro feature) and pick the HDMI port the console is plugged into: HDMI 1, HDMI 2 and so on.',
      'For the volume, use the big buttons in the app while you play.',
    ],
    extra=[
      ('The free trick: let the console switch the TV for you', 'The PS5 and the Xbox can turn on the TV and jump to their HDMI input as soon as they start, thanks to HDMI-CEC. On the PS5 it is under Settings > System > HDMI > Enable HDMI Device Link. On the Xbox, open Settings > General > TV & display options and look for the device control option. On the TV the feature has a different name depending on the brand: Anynet+ on Samsung, SIMPLINK on LG, and BRAVIA Sync or HDMI control on others.'),
      ('If the TV stays on another screen', 'If the console is on but the TV still shows the antenna or an app, the TV did not change input. From your phone, tap Inputs (Pro) and choose the console HDMI. Without Pro, use the arrows and OK to reach the TV inputs, or press the button on the TV itself, and pick the HDMI. The number is the port where you plugged in the console cable.'),
      ('If it is a Roku TV', 'The physical button on the TV, usually at the bottom center or on the back, turns it on. From there your phone does the rest.'),
    ],
    faq=[
      ('Does Mando TV have anything to do with GTA VI?', 'No. Mando TV is not affiliated with Rockstar Games or Take-Two. It only helps you avoid losing game time because you cannot find the TV remote.'),
      ('Is switching the HDMI input free?', 'The inputs list is part of Mando TV Pro, a one-time purchase with no subscription. For free you can turn the TV on, use the arrows, OK and volume, and let the console switch the input by itself with HDMI-CEC.'),
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
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..100,600..900&family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
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
      <p class="nota">{u["nota"]}</p>

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
