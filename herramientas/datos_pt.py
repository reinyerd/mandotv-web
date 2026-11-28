# Textos en portugués de Brasil (pt-BR, "você") de mandotv.app. Los usa generar_idiomas.py. Escritos para las búsquedas de Brasil
# ("controle remoto", "celular", "TV"), no son traducción literal. Las claves y las rutas están en idiomas_sitio.py.
# Los nombres de menús de las TV no se inventan: cuando no hay certeza se describe la opción y se añade entre paréntesis
# el nombre en inglés que muestran las TV.

# Opciones de las TV que se repiten en varios textos.
LG_OPC = 'a opção de ligar a TV com o celular (em inglês, "TV On With Mobile"), que fica em Geral > Dispositivos > Dispositivos externos (nos modelos mais antigos, em Conexão > Gerenciamento de conexão móvel)'
LG_WIFI = 'a ativação via Wi-Fi ("Turn on via Wi-Fi")'
SAM_RUTA = 'Configurações > Geral > Rede > Configurações de especialista (Expert Settings) e ative a opção de ligar com um dispositivo móvel ("Power On with Mobile")'
SAM_PERM = 'Configurações > Geral > Gerenciador de dispositivos externos > Gerenciador de conexão de dispositivos ("Device Connection Manager") e deixe o Mando TV como permitido'
ROKU_APPS = 'Configurações > Sistema > Configurações avançadas do sistema > Controle por aplicativos móveis ("Control by mobile apps")'
ROKU_RAPIDO = 'a opção de início rápido da TV ("Fast TV start") em Configurações > Sistema > Energia'
AND_WOL = '"Wake on LAN" ou uma opção de ligar pela rede'
AND_WOL_RS = '"Wake on LAN", "Ligar pela rede" ou "Remote start"'

UI = dict(
  locale='pt_BR',
  aria_home='Mando TV, início', aria_main='Principal', nav_que='Recursos', nav_ayuda='Ajuda', nav_contacto='Contato',
  asunto='Ol%C3%A1%20Mando%20TV', inicio='Início', privacidad='Privacidade', aria_pie='Rodapé', aria_ruta='Caminho',
  aria_marcas='Marcas e guias', hecho='Feito no Chile',
  aviso='O Mando TV é um app independente: não é afiliado aos fabricantes de TV citados nem ao Google, à Amazon, à Apple ou à Roku, e não tem o apoio deles. As marcas pertencem aos seus donos e são mencionadas apenas para indicar compatibilidade. Android TV e Google TV são marcas do Google LLC. Apple TV é uma marca da Apple Inc.',
  bajar='Baixar grátis', descarga='Baixe na', anticipada='Teste antecipado no',
  apple_aria='Baixar o Mando TV grátis na App Store', ms_aria='Baixar o Mando TV grátis na Microsoft Store',
  gp_aria='Teste antecipado do Mando TV no Google Play para Android', aria_desc='Baixar o Mando TV',
  b_como_btn='Como conectar', b_tiendas_label='Disponível nas lojas',
  b_nota='iPhone, iPad, Mac, Android e Windows. Download grátis, sem anúncios. O Pro é uma compra única, sem assinatura.',
  b_compat='TVs compatíveis', b_otras='Outras marcas', b_otras_p='O Mando TV controla todas estas marcas no mesmo app:',
  g_guias='Guias', g_ver='Ver os passos', g_pasos='Passo a passo', g_hazlo='Faça com o Mando TV',
  g_tiendas='O Mando TV é um controle remoto universal para a sua TV. Baixe grátis, sem anúncios e sem conta. O Pro é uma compra única opcional, sem assinatura. Para iPhone, iPad, Windows e Android:',
  g_nota='Android: teste antecipado grátis no Google Play. <a href="{enlace}">Participe em dois passos</a> e nos ajude a chegar à loja.',
  g_mas_pagina='Mais detalhes na página {enlace}.', g_mas_marca='Mais detalhes por marca:',
  g_faq='Perguntas frequentes', g_mas='Outros guias', g_todas='Todos os guias', g_ayuda='Ajuda e suporte',
  g_idiomas='Este guia em outros idiomas',
)

PIE = [
  ('samsung', 'Controle remoto Samsung'),
  ('lg', 'Controle remoto LG'),
  ('roku', 'Controle remoto Roku'),
  ('android', 'Controle remoto Android TV'),
  ('guias', 'Todos os guias'),
  ('lost-tv', 'Perdi o controle da TV'),
  ('lost-lg', 'Perdi o controle da LG'),
  ('lg-on', 'Ligar TV LG pelo celular'),
  ('hdmi', 'Trocar entrada HDMI sem controle'),
  ('androidtv', 'Android TV sem controle'),
  ('console', 'Ligar a TV e o HDMI do console'),
  ('samsung-lost', 'TV Samsung sem controle'),
  ('roku-lost', 'Perdi o controle da Roku'),
  ('roku-403', 'O app da Roku não funciona'),
  ('androidtv-code', 'Código de pareamento Android TV'),
  ('not-found', 'O celular não encontra a TV'),
  ('wifi', 'Celular como controle por Wi-Fi'),
  ('pc', 'Controlar a TV pelo PC'),
]
NOMBRE_OTRA = {'lg': 'App de controle remoto para LG', 'samsung': 'App de controle remoto para Samsung', 'roku': 'App de controle remoto para Roku',
               'android': 'App de controle remoto para Android TV e Google TV'}
PAGINA_MARCA = {'lg': 'app de controle remoto para LG', 'samsung': 'app de controle remoto para Samsung', 'roku': 'app de controle remoto para Roku',
                'android': 'app de controle remoto para Android TV'}

OTRAS_GUIAS = [
  ('lg-on', 'Como ligar a TV LG pelo celular'),
  ('lost-tv', 'Perdi o controle da TV: o que fazer'),
  ('lost-lg', 'Perdi o controle da LG: use o celular'),
  ('hdmi', 'Como trocar a entrada HDMI da TV sem controle'),
  ('androidtv', 'Android TV sem controle remoto: use o celular'),
  ('console', 'Como ligar a TV e mudar para o HDMI do console sem o controle'),
  ('samsung-lost', 'TV Samsung sem o controle original: use o celular'),
  ('roku-lost', 'Perdi o controle da Roku: use o celular'),
  ('roku-403', 'O app da Roku não funciona: como resolver o erro 403'),
  ('androidtv-code', 'A Android TV pede um código de pareamento: o que fazer'),
  ('not-found', 'O celular não encontra a TV: o que verificar'),
  ('wifi', 'Como usar o celular como controle remoto por Wi-Fi'),
  ('pc', 'Como controlar a TV pelo PC com Windows'),
]

INDICE = dict(
  titulo='Guias: controlar a TV pelo celular | Mando TV',
  desc='Guias passo a passo para usar o celular ou o PC como controle remoto: ligar a TV, trocar a entrada HDMI e resolver problemas na Samsung, LG e Roku.',
  h1='Guias: use o celular como controle remoto da TV',
  intro='Passos simples para conectar, ligar e resolver problemas do controle da sua TV Samsung, LG, Roku ou Android TV com o Mando TV.',
  h2_guias='Todos os guias', h2_marcas='App de controle remoto por marca',
  marcas_extra=[('sony', 'Controle remoto Sony'), ('philips', 'Controle remoto Philips')],
)

MARCAS = [
  dict(clave='lg', color='#e0457b', corto='LG',
    titulo='Controle remoto LG pelo celular, app grátis | Mando TV',
    desc='Use o celular ou o PC como controle remoto da TV LG webOS, por Wi-Fi. Teclas, teclado, apps, entradas e ligar grátis; ponteiro no Pro.',
    h1='Controle remoto LG: app para o seu celular',
    intro='O Mando TV é um app de controle remoto para TV LG: ele transforma o celular ou o computador, pelo Wi-Fi de casa, no controle da sua Smart TV LG com webOS. Quebra um galho quando você perdeu o controle, as pilhas acabaram ou você só quer digitar mais rápido.',
    compat='Smart TVs LG com webOS (a maioria dos modelos LG Smart TV desde 2014). Funciona em TVs LED, NanoCell, QNED e OLED. As Smart TVs LG antigas com NetCast (2011 a 2014, antes do webOS) têm suporte novo, em beta: elas se emparelham com a chave de 6 dígitos que a TV mostra.',
    h2=dict(funciones='O que você pode fazer com a sua TV LG', como='Como conectar a TV LG ao Mando TV',
            encender='Ligar a TV LG pelo celular', preguntas='Perguntas sobre LG', guias='Guias para LG'),
    funciones=[
      ('Todas as teclas', 'Setas, OK, Voltar, Início, volume, canais, mudo e reprodução.'),
      ('Ponteiro como o Magic Remote (Pro)', 'Mova a seta na tela com o dedo, como no Magic Remote da LG.'),
      ('Dois teclados', 'Digite na busca da TV e na maioria dos aplicativos com o teclado do celular. Com o Teclado do YouTube (Pro), digite ou diga o que quer assistir e o YouTube abre na TV com os resultados.'),
      ('Apps e entradas', 'Abra seus aplicativos e mude para HDMI, TV ao vivo, AirPlay ou Screen Share.'),
      ('Saída de áudio (Pro)', 'Alterne entre os alto-falantes da TV e a sua soundbar.'),
      ('Ligar a TV', 'Se estiver desligada, o Mando TV liga pela rede e conecta sozinho.'),
    ],
    pasos=[
      'Conecte o celular e a TV ao mesmo Wi-Fi.',
      'Abra o Mando TV: a sua TV LG aparece sozinha na lista. Toque nela.',
      'Na tela da TV aparece um aviso pedindo permissão. Aceite com o controle de sempre (só na primeira vez).',
    ],
    encender='Na TV LG, abra as Configurações e procure ' + LG_OPC + '. Ative ' + LG_WIFI + '. Se existir a opção de início rápido ("Quick Start+" em inglês), ative também. Depois, quando você tocar na TV desligada no Mando TV, o app pergunta se você quer ligá-la e conecta sozinho.',
    faq=[
      ('Preciso do Magic Remote para usar o Mando TV?', 'Só na primeira vez, para aceitar o aviso na tela. Depois, o celular basta.'),
      ('O Mando TV substitui o app LG ThinQ?', 'Para controlar a TV, sim: não precisa de conta LG nem de registrar a TV. O Mando TV conecta direto pelo seu Wi-Fi.'),
      ('Dá para ligar a minha TV LG pelo celular?', 'Dá, se você ativar a opção de ligar a TV com o celular e já tiver conectado uma vez com a TV ligada.'),
      ('Funciona com TVs LG antigas, de antes do webOS?', 'Em beta, sim, com as Smart TVs LG NetCast de 2011 a 2014. Elas se emparelham com a chave de 6 dígitos que a TV mostra. É novo, então ainda pode ter detalhes a acertar.'),
    ],
    guias=[('lg-on', 'Como ligar a TV LG pelo celular'),
           ('lost-lg', 'Perdi o controle da LG: use o celular'),
           ('hdmi', 'Como trocar a entrada HDMI da TV sem controle'),
           ('guias', 'Todos os guias para controlar a TV pelo celular')]),
  dict(clave='samsung', color='#3d7bff', corto='Samsung',
    titulo='Controle remoto Samsung pelo celular, app | Mando TV',
    desc='Use o celular ou o PC como controle remoto da TV Samsung Tizen, por Wi-Fi. Teclas, teclado, apps e ligar grátis; touchpad no Pro. Sem anúncios.',
    h1='Controle remoto Samsung: app para o seu celular',
    intro='O Mando TV é um app de controle remoto para TV Samsung: ele transforma o celular ou o computador, pelo Wi-Fi de casa, no controle da sua Smart TV Samsung. Não precisa de conta Samsung nem de registrar a TV.',
    compat='Smart TVs Samsung com Tizen, modelos de 2016 em diante (linhas como Crystal UHD, QLED, Neo QLED, The Frame e OLED).',
    h2=dict(funciones='O que você pode fazer com a sua TV Samsung', como='Como conectar a TV Samsung ao Mando TV',
            encender='Ligar a TV Samsung pelo celular', preguntas='Perguntas sobre Samsung', guias='Guias para Samsung'),
    funciones=[
      ('Todas as teclas', 'Setas, OK, Voltar, Início, volume, canais, mudo e fonte.'),
      ('Touchpad (Pro)', 'Deslize o dedo para se mover pelos menus sem procurar as setas.'),
      ('Dois teclados', 'Digite na busca da TV e na maioria dos aplicativos com o teclado do celular. Com o Teclado do YouTube (Pro), digite ou diga o que quer assistir e o YouTube abre na TV com os resultados.'),
      ('Apps', 'Abra Netflix, YouTube, Prime Video e seus outros aplicativos com um toque.'),
      ('Ligar a TV', 'Se estiver desligada, o Mando TV liga pela rede e conecta sozinho.'),
      ('Sem conta', 'A conexão é direta, pelo seu Wi-Fi, sem passar pela internet.'),
    ],
    pasos=[
      'Conecte o celular e a TV ao mesmo Wi-Fi.',
      'Abra o Mando TV: a sua TV Samsung aparece sozinha na lista. Toque nela.',
      'A TV pergunta se você permite a conexão. Escolha "Permitir" com o controle (só na primeira vez).',
    ],
    encender='Na TV Samsung, abra ' + SAM_RUTA + '. Depois, quando você tocar na TV desligada no Mando TV, o app pergunta se você quer ligá-la e conecta sozinho.',
    faq=[
      ('Recusei a permissão sem querer. E agora?', 'Na TV, vá em ' + SAM_PERM + '.'),
      ('O Mando TV substitui o SmartThings?', 'Para controlar a TV, sim, e sem conta Samsung. O Mando TV conecta direto pelo seu Wi-Fi.'),
      ('Funciona em TVs Samsung mais antigas?', 'Funciona em TVs Samsung com Tizen, modelos de 2016 em diante. Os modelos anteriores usam outro sistema, que ainda não é compatível.'),
    ],
    guias=[('samsung-lost', 'TV Samsung sem o controle original: use o celular'),
           ('smartthings', 'Alternativa ao controle do SmartThings'),
           ('turn-on', 'Ligar a TV sem o controle'),
           ('hdmi', 'Como trocar a entrada HDMI da TV sem controle'),
           ('guias', 'Todos os guias para controlar a TV pelo celular')]),
  dict(clave='roku', color='#a77bff', corto='Roku',
    titulo='Controle remoto Roku pelo celular, app grátis | Mando TV',
    desc='Use o celular ou o PC como controle remoto da Roku TV ou do aparelho Roku, por Wi-Fi. Teclas, teclado, canais, entradas e ligar grátis.',
    h1='Controle remoto Roku: app para o seu celular',
    intro='O Mando TV é um app de controle remoto para Roku: ele transforma o celular ou o computador, pelo Wi-Fi de casa, no controle da sua Roku. Funciona com TVs Roku TV e com os aparelhos Roku que se ligam por HDMI.',
    compat='TVs Roku TV (TCL, Hisense, Philips, Sharp, JVC e outras) e aparelhos Roku (Express, Streaming Stick, Ultra).',
    h2=dict(funciones='O que você pode fazer com a sua Roku', como='Como conectar a Roku ao Mando TV',
            encender='Ligar a Roku pelo celular', preguntas='Perguntas sobre Roku', guias='Guias para Roku'),
    funciones=[
      ('Todas as teclas', 'Setas, OK, Voltar, Início, volume, mudo, voltar 10 segundos e reprodução.'),
      ('Dois teclados', 'Digite na busca da Roku e nos canais que aceitam com o teclado do celular. Com o Teclado do YouTube (Pro), digite ou diga o que quer assistir e o YouTube abre na TV com os resultados.'),
      ('Canais', 'Abra Netflix, YouTube e seus outros canais da Roku com um toque.'),
      ('Entradas', 'Em uma Roku TV, mude para HDMI, antena ou AV pelo app.'),
      ('Ligar a TV', 'Nas Roku TV com início rápido, o Mando TV liga a TV pelo celular.'),
      ('Sem pareamento', 'A Roku não pede código: toque nela na lista e pronto.'),
      ('Fazer o controle tocar', 'Se o seu controle Roku tem alto-falante, como o Roku Voice Remote Pro, o Mando TV faz o controle tocar para você achá-lo. É grátis, e o Roku precisa estar ligado.'),
    ],
    pasos=[
      'Conecte o celular e a Roku ao mesmo Wi-Fi.',
      'Abra o Mando TV: a sua Roku aparece sozinha na lista. Toque nela.',
      'Se não conectar, na Roku vá em ' + ROKU_APPS + ' e deixe o acesso à rede em Padrão ou Permissivo (nas versões mais novas do software da Roku, deixe "Control by mobile apps" em "Enabled").',
    ],
    encender='Nas Roku TV, ative ' + ROKU_RAPIDO + '. Os aparelhos Roku ligados em outra TV não podem ser ligados assim. Depois, quando você tocar na TV desligada no Mando TV, o app pergunta se você quer ligá-la e conecta sozinho.',
    faq=[
      ('Funciona com a Roku Express ou a Streaming Stick?', 'Sim. Todos os aparelhos Roku e as TVs Roku TV são controlados do mesmo jeito.'),
      ('O Mando TV não encontra a minha Roku. O que fazer?', 'Confirme que os dois estão no mesmo Wi-Fi e que o controle por aplicativos móveis não está desativado na Roku. Você também pode adicioná-la digitando o endereço IP.'),
      ('Preciso de uma conta Roku?', 'Não. O Mando TV conecta direto pelo seu Wi-Fi.'),
    ],
    guias=[('roku-403', 'O app da Roku não funciona (erro 403)'),
           ('roku-lost', 'Perdi o controle da Roku: use o celular'),
           ('tcl', 'Controle remoto TCL'),
           ('hisense', 'Controle remoto Hisense'),
           ('philips', 'Controle remoto Philips'),
           ('guias', 'Todos os guias para controlar a TV pelo celular')]),
  dict(clave='android', color='#2fbf8f', corto='Android TV e Google TV',
    titulo='Controle remoto Google TV e Android TV no celular | Mando TV',
    desc='Controle remoto Google TV e Android TV (Sony, TCL, Hisense, Xiaomi) no celular ou no PC, por Wi-Fi. Teclas, teclado, apps e ligar grátis; touchpad no Pro.',
    h1='Controle remoto Google TV e Android TV: app para o seu celular',
    intro='O Mando TV é um app de controle remoto para Android TV: ele transforma o celular ou o computador, pelo Wi-Fi de casa, no controle da sua Android TV ou Google TV. Funciona também a partir de um iPhone e do Windows.',
    compat='TVs com Google TV ou Android TV da Sony, Philips, TCL, Hisense, Sharp, Xiaomi, Toshiba, Panasonic, Haier, Skyworth, JVC, Thomson, Motorola, OnePlus, iFFALCON, Kogan, Vu e outras marcas, além do Chromecast com Google TV, Google TV Streamer, onn. e Nvidia Shield. Algumas dessas marcas também vendem modelos com outro sistema: se a sua TV mostra a tela inicial do Google TV ou tem a loja Google Play, o Mando TV controla.',
    h2=dict(funciones='O que você pode fazer com a sua Android TV', como='Como conectar a Android TV ao Mando TV',
            encender='Ligar a Android TV pelo celular', preguntas='Perguntas sobre Android TV', guias='Guias para Android TV'),
    funciones=[
      ('Todas as teclas', 'Setas, OK, Voltar, Início, volume, mudo e reprodução.'),
      ('Touchpad (Pro)', 'Deslize o dedo para se mover rápido pelos menus do Google TV.'),
      ('Dois teclados', 'Digite na busca da TV e na maioria dos aplicativos com o teclado do celular. Com o Teclado do YouTube (Pro), digite ou diga o que quer assistir e o YouTube abre na TV com os resultados.'),
      ('Apps', 'Abra YouTube, Netflix, Disney+ e seus outros aplicativos com um toque.'),
      ('Ligar a TV', 'Nos modelos que podem ser ligados pela rede, o Mando TV liga a TV e conecta sozinho.'),
      ('iPhone, Android e PC', 'Funciona do mesmo jeito em qualquer celular ou computador.'),
    ],
    pasos=[
      'Conecte o celular e a TV ao mesmo Wi-Fi.',
      'Abra o Mando TV: a sua Android TV aparece sozinha na lista. Toque nela.',
      'A TV mostra um código de 6 caracteres. Digite no Mando TV (só na primeira vez).',
    ],
    encender='Depende do fabricante. Procure nas configurações de rede ou de energia as opções ' + AND_WOL_RS + '. Alguns modelos não têm essa opção. Depois, quando você tocar na TV desligada no Mando TV, o app pergunta se você quer ligá-la e conecta sozinho.',
    faq=[
      ('Funciona com o Chromecast com Google TV?', 'Sim, o pareamento é feito com o código de 6 caracteres que aparece na tela.'),
      ('Qual a diferença para o app Google TV?', 'O Mando TV não precisa de conta Google, funciona também no Windows e controla TVs LG, Samsung e Roku no mesmo app.'),
      ('O código não aparece na tela. O que fazer?', 'Feche o Mando TV, abra o app de novo e toque na TV outra vez. Confirme que a TV não está em um modo de economia de energia profundo.'),
    ],
    guias=[('androidtv-code', 'A Android TV pede um código de pareamento: o que fazer'),
           ('androidtv', 'Android TV sem controle remoto: use o celular'),
           ('googletv-alt', 'Alternativa ao controle do Google TV'),
           ('sony', 'Controle remoto Sony'),
           ('tcl', 'Controle remoto TCL'),
           ('hisense', 'Controle remoto Hisense'),
           ('philips', 'Controle remoto Philips'),
           ('guias', 'Todos os guias para controlar a TV pelo celular')]),
]

GUIAS = [
  dict(clave='lost-tv', corto='Perdi o controle da TV',
    titulo='Perdi o controle da TV: use o celular como controle',
    desc='Perdeu o controle da TV? Ligue a TV pelo botão e use o celular como controle remoto. LG, Samsung, Roku e Android TV. Grátis e sem anúncios.',
    h1='Perdi o controle da TV: o que você pode fazer',
    intro='Perder o controle remoto acontece em toda casa: ele some justo na hora de assistir a algo. A boa notícia é que o celular pode virar o controle, pelo Wi-Fi de casa. Veja o que fazer, na ordem.',
    pasos=[
      'Ligue a TV pelo botão físico. Quase sempre fica embaixo no centro ou atrás, perto de um canto. Às vezes é um botão simples, às vezes um joystick pequeno.',
      'Conecte o celular ao mesmo Wi-Fi da TV.',
      'Baixe o Mando TV, que é grátis e não pede conta, e abra o app. A sua TV aparece sozinha na lista. Toque nela.',
      'Aceite a conexão conforme a sua marca. Na LG e na Samsung, a TV mostra um aviso: aceite com o botão ou o joystick da própria TV. Na Android TV e no Google TV, você digita um código de 6 caracteres que aparece na tela. A Roku não pede nada.',
      'Pronto. Setas, OK, Voltar, Início, volume, canais e teclado são grátis.',
      'Para a próxima vez, ative nas configurações da TV a ativação pela rede (o guia da sua marca está logo abaixo) e você poderá ligar a TV pelo celular sem encostar nela.',
    ],
    extra=[
      ('Escolha o guia da sua marca', 'LG: [Perdi o controle da LG](@lost-lg). Android TV e Google TV: [Android TV sem controle remoto](@androidtv). Samsung: [TV Samsung sem controle remoto](@samsung-lost). Roku: [Perdi o controle da Roku](@roku-lost).'),
      ('Se a TV não liga pelo botão', 'Antes de procurar outro controle, confira se o cabo de força está bem encaixado e se a tomada tem energia. Se o botão da TV não faz nada, o problema é da TV e não do controle.'),
      ('Se o controle só parou de funcionar', 'Teste com pilhas novas. Para saber se ele ainda emite sinal, aponte o controle para a câmera do celular e aperte uma tecla: em muitos celulares aparece uma luz violeta na tela. Se a luz aparece e a TV não responde, o sensor da TV pode estar coberto.'),
      ('Se você trocou de roteador e a TV perdeu o Wi-Fi', 'Sem controle, é mais difícil conectar a TV à rede nova. O mais simples é ligar a TV ao roteador com um cabo de rede. Você também pode criar uma rede Wi-Fi com o mesmo nome e a mesma senha de antes: em geral a TV se conecta sozinha.'),
      ('O que é grátis e o que é Pro', 'Ligar e desligar a TV, setas, OK, volume, canais, números, teclado, abrir aplicativos e trocar de entrada são grátis. O touchpad, a voz e as rotinas fazem parte do Mando TV Pro, uma compra única, sem assinatura.'),
    ],
    marca=None,
    faq=[
      ('Dá para ligar a TV pelo celular se eu nunca a conectei?', 'Nessa primeira vez, ligue pelo botão da TV. Depois de conectar o celular e ativar a ativação pela rede nas configurações da TV, você poderá ligá-la pelo app.'),
      ('Preciso comprar um controle novo?', 'Não necessariamente. Com o Mando TV você tem de graça as teclas, o volume, o teclado e o ligar. Se mesmo assim preferir um controle físico, procure o modelo exato da sua TV.'),
      ('Funciona se a TV não tiver Wi-Fi?', 'Na maioria dos casos, não. O celular e a TV normalmente precisam estar no mesmo Wi-Fi. As exceções são o infravermelho em celulares Android com emissor infravermelho, que também controla TVs que não são smart, e o Bluetooth em beta no Android 9 ou mais recente, que funciona sem Wi-Fi com Google TV, Android TV e Fire TV.'),
    ]),
  dict(clave='lost-lg', corto='Perdi o controle da LG',
    titulo='Perdi o controle da LG: use o celular | Mando TV',
    desc='Sem o controle da LG? Ligue a TV pelo botão, aceite o aviso e use o celular como controle remoto por Wi-Fi. Sem conta LG e sem anúncios.',
    h1='Perdi o controle da LG: como usar o celular',
    intro='Se você perdeu o controle da TV LG ou o Magic Remote parou de funcionar, o celular o substitui pelo Wi-Fi. Funciona em TVs LG com webOS, ou seja, quase todas as Smart TVs LG desde 2014. Não precisa de conta LG nem do app ThinQ.',
    pasos=[
      'Ligue a TV pelo botão que fica embaixo, sob o logo da LG, ou pelo de trás. Em muitos modelos ele funciona como joystick: aperte para abrir o menu e mova para escolher.',
      'Conecte o celular ao mesmo Wi-Fi da TV.',
      'Abra o Mando TV e toque na sua TV LG na lista.',
      'A TV mostra um aviso pedindo permissão. Aceite com o joystick ou o botão da TV. Se você já conectou esse celular antes, ela não pergunta de novo.',
      'Pronto. Setas, OK, Voltar, Início, volume, canais e teclado são grátis. O ponteiro é um recurso Pro.',
      'Com o app conectado, entre em Configurações com as setas e o OK e ative ' + LG_OPC + '. O guia [Como ligar a TV LG pelo celular](@lg-on) mostra onde achar.',
    ],
    extra=[
      ('Se a TV não mostra o aviso', 'A permissão pode já estar salva, ou o celular está em outra rede. Confira se os dois estão no mesmo Wi-Fi e se a VPN está desligada. Se a TV não aparece na lista, leia [O celular não encontra a TV](@not-found).'),
      ('Se a TV perdeu o Wi-Fi', 'Ligue a TV ao roteador com um cabo de rede e ela passa a usá-lo sozinha. Ou crie uma rede Wi-Fi com o mesmo nome e a mesma senha de antes, porque em geral a TV se conecta sozinha.'),
      ('Se a TV ficou presa em outra entrada', 'No celular, toque em Entradas e escolha o HDMI. Veja mais em [Como trocar a entrada HDMI da TV sem controle](@hdmi).'),
    ],
    marca='lg',
    faq=[
      ('Preciso do Magic Remote para usar o Mando TV?', 'Só precisa de algo para aceitar o aviso na primeira vez, e serve o botão ou o joystick da própria TV. Depois você usa só o celular.'),
      ('Preciso do app LG ThinQ?', 'Não. O Mando TV conecta direto pelo seu Wi-Fi e não pede conta LG.'),
      ('Consigo desligar e ligar a minha TV LG pelo celular?', 'Desligar, sim. Para ligar, é preciso ter ativado a opção de ligar a TV com o celular e ter conectado uma vez com a TV ligada.'),
    ]),
  dict(clave='hdmi', corto='HDMI sem controle',
    titulo='Trocar a entrada HDMI sem controle (Samsung, LG, Roku)',
    desc='Como trocar a entrada HDMI sem controle remoto na Samsung, LG ou Roku: pelo botão da TV ou pelo celular. Grátis para começar e sem anúncios.',
    h1='Como trocar a entrada HDMI da TV sem controle',
    intro='O console ou o streaming está pronto, mas a TV ficou em outra entrada e o controle sumiu. Para trocar a entrada HDMI sem controle, você tem duas opções: o botão da própria TV ou o celular. Veja os passos para Samsung, LG e Roku.',
    pasos=[
      'Tente o mais simples primeiro: ligue o console ou o aparelho. Se o HDMI-CEC estiver ativado na TV (Anynet+ na Samsung, SIMPLINK na LG), ela muda sozinha para essa entrada.',
      'Se não mudar, use o botão da própria TV, embaixo no centro ou atrás. Em muitas TVs Samsung e LG ele funciona como joystick e abre um menu com Fonte ou Entradas.',
      'Escolha a entrada nesse menu: HDMI 1, HDMI 2 e assim por diante. O número é o da porta onde o cabo está ligado.',
      'Se preferir o celular, conecte-o ao mesmo Wi-Fi, abra o Mando TV e toque na sua TV.',
      'Na LG e na Roku, toque em Entradas e escolha o HDMI. Na Samsung, Entradas envia à TV a tecla de fonte e você escolhe com as setas e o OK.',
      'Também dá para usar as setas e o OK para ir até as entradas a partir da tela inicial da TV. Conforme a marca e o ano, elas se chamam Fonte, Dispositivos conectados ou Entradas. Em uma Roku TV, são os blocos HDMI da tela inicial.',
    ],
    extra=[
      ('Samsung', 'Se o menu do botão da TV não tem Fonte, abra pelo celular o menu da tela inicial e procure Fonte ou Dispositivos conectados à esquerda. Você controla com as setas e o OK do Mando TV, que são grátis.'),
      ('LG', 'Aperte o joystick da TV e procure Entradas. Pelo celular, no Mando TV, você também pode abrir a lista de entradas e tocar na que quiser.'),
      ('Roku TV', 'Na tela inicial há um bloco para cada entrada, como HDMI 1 ou HDMI 2. Mova-se com as setas e entre com o OK, de graça.'),
      ('Se for uma TV com Android TV ou Google TV', 'No Mando TV, a lista de entradas ainda não existe para Android TV. Use o botão de entradas da própria TV, ou chegue a elas com as setas e o OK a partir da tela inicial. Se você está sem controle e quer se conectar, leia [Android TV sem controle remoto](@androidtv).'),
      ('Mais ajuda', 'Se a TV nem liga ou você não sabe por onde começar, leia [Perdi o controle da TV](@lost-tv). Para jogar no console, o guia [Como ligar a TV e mudar para o HDMI do console sem o controle](@console) traz o truque do HDMI-CEC.'),
    ],
    marca=None,
    faq=[
      ('Trocar a entrada HDMI é grátis?', 'Sim. A lista de entradas do Mando TV é grátis, assim como ligar a TV e usar as setas, o OK e o volume. Você também chega às entradas pelo menu da TV.'),
      ('Como sei qual entrada HDMI usar?', 'Olhe as portas HDMI da TV: cada uma tem um número. Use a porta onde está ligado o cabo do seu console ou aparelho.'),
      ('E se a TV não ligar?', 'Ligue pelo botão físico. Se você já a conectou e ativou a ativação pela rede, também pode ligá-la pelo celular.'),
    ]),
  dict(clave='androidtv', corto='Android TV sem controle',
    titulo='Android TV sem controle remoto: use o celular',
    desc='Sem o controle da Android TV ou do Google TV? Conecte o celular com o código de 6 caracteres da tela. Grátis, sem conta e sem anúncios.',
    h1='Android TV sem controle remoto: como usar o celular',
    intro='Se você perdeu o controle da Android TV ou do Google TV, ou as pilhas acabaram, o celular o substitui. O melhor é que a conexão não precisa do controle: a TV mostra um código na tela e você o digita no celular. Funciona em TVs Sony, Philips, TCL, Hisense, Sharp e Xiaomi com Android TV, no Chromecast com Google TV e na Nvidia Shield.',
    pasos=[
      'Ligue a TV pelo botão físico. Quase sempre fica embaixo no centro ou atrás, perto de um canto.',
      'Conecte o celular ao mesmo Wi-Fi da TV.',
      'Baixe o Mando TV, que é grátis e não pede conta Google, e abra o app. Toque na sua TV na lista.',
      'A TV mostra um código de 6 letras e números. Digite no celular e toque em Parear. Você não precisa do controle para isso.',
      'Agora você já pode usar as setas, OK, Voltar, Início, volume, mudo e teclado. São grátis, assim como a lista de aplicativos. O touchpad é Pro.',
      'Para ligar pelo celular da próxima vez, procure nas configurações de rede ou de energia da TV as opções ' + AND_WOL_RS + '.',
    ],
    extra=[
      ('Se a TV não liga pelo celular', 'Nem toda Android TV pode ser ligada pela rede; depende do fabricante e do modelo. Se a sua não tem essa opção, ligue pelo botão da TV e siga pelo celular. Você pode desligá-la pelo app.'),
      ('Chromecast com Google TV, Google TV Streamer e Shield', 'Conectam do mesmo jeito: mesmo Wi-Fi, toque no aparelho na lista e digite o código. Se a TV mostrar outra entrada, mude para a entrada HDMI onde o aparelho está ligado, como explica [Como trocar a entrada HDMI da TV sem controle](@hdmi).'),
      ('Se o código não aparece ou é recusado', 'Confira se a TV está mesmo ligada e não em espera. O código muda a cada pedido: só vale o último. Veja mais em [A Android TV pede um código de pareamento](@androidtv-code).'),
      ('App do Google ou Mando TV', 'O Google tem o próprio app, que pede conta Google. O Mando TV não pede conta, funciona também no Windows e controla TVs LG, Samsung e Roku no mesmo app.'),
    ],
    marca='android',
    faq=[
      ('Preciso do controle para parear o celular?', 'Não. O código aparece na tela da TV e você o digita no celular. Basta ligar a TV, se precisar pelo botão da própria TV.'),
      ('Funciona com TV Hisense?', 'Nas TVs Hisense que têm Android TV ou Google TV, sim. As Hisense com outro sistema não são compatíveis.'),
      ('Posso digitar com o teclado do celular?', 'Pode. São dois. O teclado grátis digita na busca e nos campos de texto da TV e da maioria dos aplicativos. YouTube e Netflix só aceitam o próprio teclado na tela, então para o YouTube existe o Teclado do YouTube (Pro): digite ou diga o que quer assistir e o YouTube abre na TV com os resultados. A Netflix é usada com as setas e o OK.'),
    ]),
  dict(clave='lg-on', corto='Ligar TV LG pelo celular',
    titulo='Como ligar a TV LG pelo celular (passo a passo)',
    desc='Ligue a TV LG pelo celular via Wi-Fi: ative a opção de ligar a TV com o celular e use o Mando TV. Passo a passo, grátis e sem anúncios.',
    h1='Como ligar a TV LG pelo celular',
    intro='Dá para ligar a TV LG pelo celular, mas antes é preciso ativar uma opção na TV. Feito isso, o celular liga a TV LG pela rede Wi-Fi, sem controle. Leva cinco minutos e você faz só uma vez.',
    pasos=[
      'Conecte o celular e a TV LG ao mesmo Wi-Fi.',
      'Na TV, abra as Configurações e procure ' + LG_OPC + '.',
      'Ative ' + LG_WIFI + '. Se a sua TV estiver conectada por cabo de rede, ative a opção do cabo.',
      'Se a sua TV tiver a opção de início rápido ("Quick Start+" em inglês), ative também.',
      'Com a TV ligada, abra o Mando TV no celular e toque na sua TV LG na lista. Aceite o aviso que aparece na tela. É assim que o app aprende a despertá-la.',
      'Desligue a TV e teste: toque na TV no Mando TV e o app pergunta se você quer ligá-la.',
    ],
    extra=[
      ('Se não ligar', 'A TV precisava estar no mesmo Wi-Fi quando foi desligada. Confira se a opção continua ativada e se o celular está nessa mesma rede. Se você trocou de roteador, conecte mais uma vez com a TV ligada.'),
    ],
    marca='lg',
    faq=[
      ('Dá para ligar a TV LG pelo celular se eu nunca a conectei?', 'Não. Primeiro é preciso ativar a opção de ligar a TV com o celular e conectar uma vez com o Mando TV, com a TV ligada.'),
      ('Preciso do app LG ThinQ?', 'Não. O Mando TV conecta direto pelo seu Wi-Fi e não pede conta LG.'),
      ('Funciona com dados móveis?', 'Não. O celular e a TV precisam estar no mesmo Wi-Fi.'),
    ]),
  dict(clave='console', corto='TV e console sem controle',
    titulo='Sem controle da TV? Ligar e mudar para o HDMI do console',
    desc='Dia de jogar GTA VI e o controle da TV sumiu? Ligue a TV e mude para o HDMI do PS5 ou Xbox pelo celular. Grátis e sem anúncios.',
    h1='Como ligar a TV e mudar para o HDMI do console sem o controle',
    intro='Dia de lançamento de GTA VI, o console pronto e o controle da TV sumiu no meio das almofadas. Acontece mais do que parece. Com o Mando TV, o celular liga a TV e muda para a entrada do seu PlayStation ou Xbox, pelo Wi-Fi da sua casa.',
    pasos=[
      'Conecte o celular ao mesmo Wi-Fi da TV.',
      'Abra o Mando TV e toque na sua TV na lista (Samsung, LG, Roku ou Android TV).',
      'Se a TV estiver desligada, toque em Ligar. Funciona se a TV estiver com a ativação pela rede ligada. Se você nunca ativou isso, ligue a TV desta vez pelo botão da própria TV e ative para a próxima.',
      'Ligue o console. Se o HDMI-CEC estiver ativado (veja o truque grátis abaixo), a TV muda sozinha para a entrada dele.',
      'Se não mudar, toque em Entradas no Mando TV e escolha o HDMI onde o console está ligado: HDMI 1, HDMI 2 e assim por diante.',
      'Para o volume, use os botões grandes do app enquanto você joga.',
    ],
    extra=[
      ('O truque grátis: deixe o console mudar a TV sozinho', 'O PS5 e o Xbox conseguem ligar a TV e mudar para a entrada HDMI deles assim que ligam, graças ao HDMI-CEC. No PS5 fica em Configurações > Sistema > HDMI > Ativar vínculo de dispositivo HDMI. No Xbox, abra Configurações > Geral > Opções de TV e vídeo e procure a opção de controle de dispositivos. Na TV, o recurso tem outro nome conforme a marca: Anynet+ na Samsung, SIMPLINK na LG e BRAVIA Sync ou controle HDMI em outras.'),
      ('Se a TV ficar em outra tela', 'Se o console está ligado mas a TV continua na antena ou em um app, ela não mudou de entrada. Pelo celular, toque em Entradas e escolha o HDMI do console. Você também pode usar as setas e o OK para chegar às entradas da TV, ou o botão da própria TV, e escolha o HDMI. O número é o da porta onde você ligou o cabo do console.'),
      ('Se for uma Roku TV', 'O botão físico da TV, quase sempre embaixo no centro ou atrás, liga o aparelho. Dali o celular faz o resto.'),
    ],
    marca=None,
    faq=[
      ('O Mando TV tem alguma relação com GTA VI?', 'Não. O Mando TV não é afiliado à Rockstar Games nem à Take-Two. Ele só ajuda você a não perder a hora de jogar por não achar o controle da TV.'),
      ('Trocar a entrada HDMI é grátis?', 'Sim. A lista de entradas do Mando TV é grátis, assim como ligar a TV e usar as setas, o OK e o volume. Você também pode deixar o console trocar a entrada sozinho com o HDMI-CEC.'),
      ('Funciona com a minha TV?', 'Funciona com TVs Samsung, LG, Roku e Android TV no mesmo Wi-Fi. Se a sua for de outra marca, o truque do HDMI-CEC ainda pode ajudar.'),
      ('Dá para usar para jogar GTA VI (GTA 6) no PS5 ou no Xbox?', 'O Mando TV não mexe no console nem no jogo. Ele só deixa a TV ligada e na entrada HDMI certa para você sentar e jogar.'),
    ]),
  dict(clave='samsung-lost', corto='TV Samsung sem controle',
    titulo='Perdi o controle da Samsung: use o celular | Mando TV',
    desc='Perdeu ou quebrou o controle da Samsung? Use o celular como controle remoto Wi-Fi em TVs Tizen. Simples com o Mando TV, grátis e sem anúncios.',
    h1='TV Samsung sem o controle original: use o celular',
    intro='Se você perdeu o controle da TV Samsung ou ele parou de funcionar, dá para usar o celular como controle pelo Wi-Fi. Funciona em TVs Samsung com Tizen, modelos de 2016 em diante.',
    pasos=[
      'Ligue a TV pelo botão físico. Na maioria dos modelos fica embaixo ou atrás, às vezes como um joystick pequeno.',
      'Confira se a TV está conectada ao seu Wi-Fi e se o celular está na mesma rede.',
      'Abra o Mando TV no celular. A sua TV Samsung aparece sozinha na lista. Toque nela.',
      'A TV pede para aceitar a conexão. Na maioria dos modelos, você aceita com os botões físicos da TV ou com o joystick de trás.',
      'Pronto, o celular já é o seu controle. As teclas, o teclado e os aplicativos são grátis; o touchpad é um recurso Pro.',
      'Para ligar pelo celular da próxima vez, vá em ' + SAM_RUTA + '.',
    ],
    extra=[
      ('Se a TV não pede a permissão', 'A permissão pode já estar salva, ou a TV está em outro Wi-Fi. Feche o Mando TV e abra de novo com a TV ligada. Se a TV for anterior a 2016, ela usa outro sistema, que ainda não é compatível.'),
      ('Se você recusou a permissão sem querer', 'Na TV, vá em ' + SAM_PERM + '. Se o celular continuar sem achar a TV, leia [O celular não encontra a TV](@not-found).'),
    ],
    marca='samsung',
    faq=[
      ('Como aceito a conexão se estou sem controle?', 'Na maioria dos modelos, você aceita com os botões físicos da TV ou com o joystick de trás. Se o seu modelo não tem botões, escreva para hola@mandotv.app e nós ajudamos.'),
      ('O Mando TV pede conta Samsung?', 'Não. Ele conecta direto pelo seu Wi-Fi, sem conta Samsung.'),
      ('Funciona na minha TV Samsung mais antiga?', 'Funciona em TVs Samsung com Tizen, modelos de 2016 em diante.'),
    ]),
  dict(clave='wifi', corto='Celular como controle por Wi-Fi',
    titulo='Celular como controle remoto da TV por Wi-Fi',
    desc='Conecte o celular à TV pelo Wi-Fi e use como controle remoto da Samsung, LG, Roku e Google TV. Passos por marca com o Mando TV. Grátis.',
    h1='Como conectar o celular à TV pelo Wi-Fi como controle remoto',
    intro='Basta o celular e a TV no mesmo Wi-Fi, mais um app de controle remoto. O Mando TV encontra a sua TV sozinho e funciona com Samsung, LG, Roku, Google TV e Android TV.',
    pasos=[
      'Conecte o celular e a TV ao mesmo Wi-Fi.',
      'Abra o Mando TV. A sua TV aparece sozinha na lista. Toque nela.',
      'Aceite a conexão conforme a sua marca (o detalhe de cada uma está abaixo).',
      'Controle a TV com as teclas ou com o teclado do celular. O touchpad é um recurso Pro.',
    ],
    extra=[
      ('Samsung', 'A TV pergunta se você permite a conexão. Aceite na tela na primeira vez. Funciona com Tizen, de 2016 em diante. Para ligá-la pelo celular, vá em ' + SAM_RUTA + '.'),
      ('LG', 'A TV mostra um aviso pedindo permissão. Aceite na primeira vez. Para ligá-la pelo celular, procure em Configurações ' + LG_OPC + ' e ative ' + LG_WIFI + '.'),
      ('Roku', 'A Roku não pede pareamento: toque nela na lista e pronto. Para ligá-la, ative ' + ROKU_RAPIDO + '.'),
      ('Google TV e Android TV', 'A TV mostra um código na tela. Digite no Mando TV na primeira vez. Para ligá-la, procure nas configurações a opção ' + AND_WOL + '.'),
    ],
    marca=None,
    faq=[
      ('Preciso de internet para usar o celular como controle?', 'Você precisa do celular e da TV no mesmo Wi-Fi. O Mando TV conecta direto à TV por essa rede.'),
      ('Por que a minha TV não aparece na lista?', 'Confira se a TV está ligada e se o celular não está usando dados móveis nem outro Wi-Fi. Alguns roteadores têm uma rede de visitantes que isola os aparelhos.'),
      ('Dá para usar o Mando TV em iPhone ou celular Android?', 'Sim no iPhone e no iPad: o app já está na App Store. Também está na Microsoft Store para Windows. O Android está chegando: você pode entrar no teste antecipado grátis no Google Play.'),
    ]),
  dict(clave='pc', corto='Controlar a TV pelo PC',
    titulo='Como controlar a TV pelo PC com Windows (grátis)',
    desc='Use o PC com Windows como controle remoto da TV Samsung, LG, Roku ou Google TV por Wi-Fi. Teclas, teclado e apps grátis; atalhos no Pro.',
    h1='Como controlar a TV pelo PC com Windows',
    intro='Se você passa o dia no computador, não precisa procurar o controle: o Mando TV para Windows controla a sua TV Samsung, LG, Roku, Google TV ou Android TV pelo Wi-Fi de casa. É prático para trocar de aplicativo, subir o volume ou digitar no YouTube com o teclado do PC.',
    pasos=[
      'Baixe o Mando TV grátis na Microsoft Store, no seu computador com Windows 10 ou 11.',
      'Confira se o computador e a TV estão na mesma rede (Wi-Fi ou cabo, mas no mesmo roteador).',
      'Abra o Mando TV: a sua TV aparece sozinha na lista. Toque ou clique nela.',
      'Aceite a conexão na tela da TV na primeira vez (no Google TV e na Android TV, digite o código que a TV mostra).',
      'Pronto: use as teclas ou o teclado para digitar na busca da TV. O touchpad é um recurso Pro.',
    ],
    extra=[
      ('Atalhos do teclado do PC (Pro)', 'Com o Mando TV Pro, você controla a TV com o teclado do computador: setas para se mover, Enter para o OK, Backspace ou Esc para voltar, + e - para o volume, M para o mudo e Espaço para pausar.'),
      ('Mini controle sempre à frente (Pro)', 'Deixe uma janela pequena com o controle sempre visível enquanto você trabalha ou joga no PC.'),
      ('Falar com a TV pelo PC (Pro)', 'Com o Mando TV Pro você dá ordens à TV pelo microfone do PC: "abre o YouTube", "aumenta o volume" ou "desliga em 30 minutos", do seu jeito. No Windows, a voz é reconhecida no próprio PC: não precisa de internet, você não precisa mudar nada nas configurações do Windows e funciona nos 6 idiomas do app. O que você diz não sai do PC e não é guardado. Só em processadores muito antigos o app recorre à digitação por voz do Windows, que precisa do "Reconhecimento de fala online" ativado nas configurações de privacidade e do idioma adicionado no Windows (Português (Brasil) ou (Portugal)). Nesse caso, se faltar algo, o app avisa e abre o ajuste com um botão.'),
    ],
    marca=None,
    faq=[
      ('Preciso de cabo ou Bluetooth para controlar a TV pelo PC?', 'Não. O Mando TV conecta pela rede da sua casa: o PC e a TV só precisam estar no mesmo roteador.'),
      ('Funciona com todas as TVs?', 'Funciona com TVs Samsung com Tizen (2016 em diante), LG com webOS, Roku e Google TV ou Android TV (Sony, Philips, TCL, Hisense, Sharp, Xiaomi, Toshiba, Panasonic, Haier, Skyworth e outras).'),
      ('Quanto custa?', 'As teclas, o teclado e o ligar pela rede são grátis e sem anúncios. O Mando TV Pro é uma compra única, sem assinatura, para extras como touchpad, atalhos do teclado do PC e o mini controle.'),
      ('Por que o microfone não me entende no Windows?', 'Confira se a voz está ativa (é um recurso do Pro) e se o microfone do PC funciona no Windows. Na maioria dos PCs a voz é reconhecida no próprio aparelho, sem internet. Só em processadores muito antigos o app usa a digitação por voz do Windows: aí confira se o "Reconhecimento de fala online" está ativado nas configurações de privacidade do Windows e se o Windows tem Português (Brasil) ou Português (Portugal) nas configurações de idioma. O Mando TV usa esse idioma só enquanto escuta.'),
    ]),
  dict(clave='roku-403', corto='O app da Roku não funciona',
    titulo='O app da Roku não funciona? Resolva o erro 403',
    desc='O celular conecta na Roku mas as teclas não fazem nada? Ative o controle por aplicativos móveis na Roku em 5 passos.',
    h1='O app da Roku não funciona: como resolver',
    intro='Se o celular acha a Roku e conecta, mas nenhuma tecla faz nada, quase sempre é uma configuração da própria Roku que bloqueia os apps de controle. As versões mais novas da Roku vêm mais restritivas por padrão. Dá para resolver em um minuto pelo menu da Roku.',
    pasos=[
      'Na Roku, aperte Início e entre em Configurações.',
      'Abra Sistema e depois Configurações avançadas do sistema.',
      'Entre em "Controle por aplicativos móveis" ("Control by mobile apps"). Em alguns modelos se chama "Controle externo".',
      'Em "Acesso à rede" ("Network access"), escolha Padrão ou Permissivo. Se no seu modelo for só um interruptor, deixe ligado.',
      'Volte ao Mando TV no celular e toque na sua Roku. Agora as teclas respondem.',
    ],
    extra=[
      ('Como saber se o seu problema é este', 'O sinal é claro: o celular vê a Roku na lista e conecta, mas nada acontece quando você toca em uma tecla. Por dentro, a Roku responde com o erro 403, que significa "proibido". O Mando TV detecta isso ao conectar e mostra estes mesmos passos na tela.'),
      ('Padrão ou Permissivo, qual escolher?', 'O Padrão basta: aceita as ordens que chegam da rede da sua casa, que é o que um controle remoto precisa. O Permissivo é mais aberto e só é necessário em redes pouco comuns.'),
      ('Se você está sem o controle da Roku', 'Quando a opção está em Desativado, só dá para mudá-la com o controle físico da Roku. Peça um emprestado para mudar uma vez; depois, você faz tudo pelo celular. Leia também [Perdi o controle da Roku](@roku-lost).'),
    ],
    marca='roku',
    faq=[
      ('Por que a minha Roku parou de responder se antes funcionava?', 'Uma atualização da Roku pode deixar essa opção mais restritiva. Não é problema do celular nem do Wi-Fi: basta permitir de novo o controle por aplicativos.'),
      ('Isso vale para Roku TV e para aparelhos Roku?', 'Sim. A opção fica no mesmo menu nos aparelhos Roku e nas TVs Roku TV.'),
      ('Dá para deixar em Padrão sem risco?', 'Sim. Ele só aceita ordens de aparelhos da rede da sua casa.'),
    ]),
  dict(clave='not-found', corto='O celular não encontra a TV',
    titulo='O celular não encontra a TV? 6 pontos para verificar',
    desc='O app de controle não acha a TV ou desconecta? Confira o Wi-Fi, a VPN e o acesso à rede local. Samsung, LG, Roku e Android TV.',
    h1='O celular não encontra a TV: o que verificar',
    intro='Você abre o app de controle e a lista está vazia, ou a TV aparece mas a conexão cai. Quase sempre é a rede, não a TV. Confira estes pontos na ordem: o primeiro resolve a maioria dos casos.',
    pasos=[
      'Veja em qual Wi-Fi está o celular e em qual está a TV. Precisa ser a mesma rede, com o mesmo nome. Uma rede de visitantes não funciona, porque isola os aparelhos.',
      'Desligue a VPN do celular, se usar uma. Com a VPN ativa, o celular sai por outra rede e não enxerga os aparelhos da sua casa, ou a conexão cai depois de alguns segundos.',
      'Desligue os dados móveis por um momento. Alguns celulares trocam sozinhos do Wi-Fi para os dados móveis quando o sinal está fraco.',
      'Ligue a TV e espere ela terminar de iniciar. Uma TV desligada não responde à busca.',
      'No iPhone, confira se o app tem a permissão de Rede local: Ajustes > Privacidade e Segurança > Rede Local.',
      'Se ainda não aparecer, adicione na mão: no Mando TV, toque em "Adicionar por IP" e digite o endereço IP da TV.',
    ],
    extra=[
      ('Deixe o app guiar você', 'Na lista de TVs há um botão para o caso de a sua TV não aparecer. O app confere passo a passo as causas mais comuns (o mesmo Wi-Fi, uma VPN, a permissão de rede local e mais) e, depois de cada correção, mostra um botão para conferir de novo. Esse assistente é grátis.'),
      ('Onde achar o endereço IP da TV', 'Fica no menu de rede da TV e muda um pouco conforme o modelo. Na LG: Configurações, Rede, Conexão Wi-Fi, configurações avançadas. Na Samsung: Configurações, Geral, Rede, Status da rede, Configurações de IP. Na Roku: Configurações, Rede, Sobre. Na Android TV e no Google TV: Configurações, Rede e internet, e toque na sua rede. É um número como 192.168.1.86.'),
      ('Se aparece mas a conexão cai', 'Quando a conexão cai depois de alguns segundos, a causa costuma estar no celular: uma VPN, a troca para outro Wi-Fi ou o economizador de bateria. Desligue a VPN, fique no mesmo Wi-Fi e tente de novo.'),
      ('Wi-Fi de 2,4 e de 5 GHz', 'Não importa se o celular está na rede de 5 GHz e a TV na de 2,4 GHz, desde que as duas venham do mesmo roteador. Se você tem um repetidor de Wi-Fi e a TV ainda não aparece, aproxime o celular do roteador principal e tente de novo.'),
    ],
    marca=None,
    faq=[
      ('Dá para controlar a TV com dados móveis?', 'Não. O sinal do controle passa pelo Wi-Fi da sua casa, então o celular e a TV precisam estar na mesma rede.'),
      ('Por que não funciona com a VPN ligada?', 'Porque a VPN manda todo o tráfego do celular por outra rede e o celular deixa de ver os aparelhos da sua casa. Desligue enquanto usa o controle.'),
      ('Funciona por Bluetooth ou infravermelho?', 'Para smart TVs, o Mando TV usa o Wi-Fi. O infravermelho só funciona em celulares Android com emissor infravermelho e serve para TVs que não são smart. O Bluetooth está disponível em beta, grátis e só no Android 9 ou mais recente: o celular se conecta à TV como teclado e controle Bluetooth, sem Wi-Fi. Funciona com Google TV, Android TV e Fire TV; em outras marcas que aceitam teclados Bluetooth pode funcionar, mas a Roku não os aceita.'),
    ]),
  dict(clave='androidtv-code', corto='Código de pareamento Android TV',
    titulo='A Android TV pede um código de pareamento: o que fazer',
    desc='A sua Android TV ou Google TV mostra um código de 6 caracteres ao conectar o celular. Como digitar e o que fazer se não aparecer ou for recusado.',
    h1='A Android TV pede um código de pareamento: o que fazer',
    intro='Na primeira vez que você conecta o celular a uma Android TV ou Google TV, a TV mostra na tela um código de 6 caracteres. É normal e só acontece uma vez: garante que mais ninguém controle a sua TV. Veja como digitar e o que fazer se ele não aparecer.',
    pasos=[
      'Ligue a TV e deixe a tela inicial visível.',
      'Abra o Mando TV no celular, no mesmo Wi-Fi da TV, e toque na sua TV na lista.',
      'Olhe a tela da TV: aparece um código de 6 letras e números.',
      'Digite no celular exatamente como aparece e toque em Parear. As letras vão só de A a F: um caractere redondo é sempre o número zero.',
      'Pronto. A TV memoriza o seu celular e não pede o código de novo.',
    ],
    extra=[
      ('Se o código não aparece na TV', 'Confira se a TV está mesmo ligada e não em espera, e se o celular está no mesmo Wi-Fi. Toque na TV de novo no celular. Se continuar sem aparecer, reinicie a TV: tire da tomada por dez segundos, ligue de novo e tente outra vez.'),
      ('Se disser que o código está errado', 'O código muda a cada pedido. Se você demorou ou pediu duas vezes, só vale o último que está na tela. Toque na TV de novo no celular e digite o código novo.'),
      ('Se a TV pedir o código de novo', 'Acontece quando a TV é restaurada para os dados de fábrica ou quando você apaga os dados do app no celular. Pareie de novo e fica salvo. Se você está sem nenhum controle, leia [Android TV sem controle remoto](@androidtv).'),
    ],
    marca='android',
    faq=[
      ('Quais TVs usam esse código?', 'As que têm Android TV ou Google TV: Sony, Philips, TCL, Hisense, Sharp, Xiaomi, Chromecast com Google TV e várias outras.'),
      ('Preciso de conta Google no celular?', 'Não. O código que aparece na tela basta.'),
      ('É seguro?', 'Sim. O código prova que você está diante da TV: ninguém consegue parear um aparelho sem ver a tela.'),
    ]),
  dict(clave='roku-lost', corto='Perdi o controle da Roku',
    titulo='Perdi o controle da Roku: use o celular por Wi-Fi',
    desc='Perdeu o controle da Roku? O celular o substitui por Wi-Fi. Passos simples, mesmo se você trocou de roteador e a Roku ficou sem Wi-Fi.',
    h1='Perdi o controle da Roku: como usar o celular',
    intro='Se você perdeu o controle da Roku ou ele parou de funcionar, o celular o substitui, desde que a Roku ainda esteja conectada ao seu Wi-Fi. E se você mudou de Wi-Fi ou de roteador, também existe uma saída.',
    pasos=[
      'Antes de tudo, tente fazer o controle tocar. Se o seu controle Roku tem alto-falante, como o Roku Voice Remote Pro, abra o Mando TV, conecte-se ao Roku e use a opção de fazer o controle tocar para encontrá-lo. Só funciona com controles Roku que têm alto-falante, e o Roku precisa estar ligado.',
      'Ligue a TV e deixe a Roku ligada. Você não precisa mexer em nada nela.',
      'Conecte o celular ao mesmo Wi-Fi da Roku.',
      'Abra o Mando TV. A Roku aparece sozinha na lista. Toque nela.',
      'Use as setas, o OK, o Início e o Voltar como no seu controle de sempre. A Roku não pede nenhum código.',
      'Se as teclas não fazem nada, a Roku está bloqueando o controle por aplicativos: o guia [O app da Roku não funciona](@roku-403) explica como liberar.',
    ],
    extra=[
      ('Se a Roku ficou sem Wi-Fi (trocou de roteador ou se mudou)', 'Sem controle, você não consegue entrar no menu para configurar a rede nova, mas há um truque: a Roku se conecta sozinha a uma rede com o mesmo nome e a mesma senha da anterior. Em outro celular, crie uma zona Wi-Fi com esse nome e essa senha exatos, conecte a ela o celular que tem o Mando TV e a Roku aparece na lista. Dali, entre em Configurações, Rede, e conecte-a ao Wi-Fi novo.'),
      ('Se for uma Roku TV', 'As TVs Roku TV têm um botão físico, quase sempre embaixo no centro ou atrás, que liga a TV. Basta para ligar e seguir pelo celular.'),
      ('Se preferir comprar outro controle', 'Confira se é compatível com o seu modelo. Os aparelhos Roku pequenos escondidos atrás da TV precisam de um controle que não seja infravermelho, porque o infravermelho não chega até eles.'),
    ],
    marca='roku',
    faq=[
      ('O celular consegue ligar a Roku?', 'Um aparelho Roku ligado na tomada fica sempre ligado. Em uma Roku TV, o Mando TV liga a TV por Wi-Fi quando a opção de início rápido da TV está ativada em Configurações > Sistema > Energia.'),
      ('E o volume?', 'Em uma Roku TV, o celular sobe e baixa o volume. Em um aparelho Roku ligado por HDMI, depende da TV: em muitas funciona e em outras não.'),
      ('Preciso criar uma conta?', 'Não. O Mando TV não pede conta e também controla TVs Samsung, LG e Android TV no mesmo app.'),
    ]),
]

SOPORTE = dict(
  titulo='Ajuda: conectar e ligar a TV com o Mando TV',
  desc='Como conectar o controle Mando TV à sua TV LG, Samsung, Roku ou Android TV, ligá-la pelo celular e o que fazer se algo der errado.',
  h1='Ajuda',
  intro='As perguntas mais comuns, na ordem dos passos. Se não achar a sua, escreva para <a href="mailto:hola@mandotv.app?subject=Ajuda%20Mando%20TV">hola@mandotv.app</a> e nós respondemos. Escreva para nós no seu idioma. Respondemos em espanhol ou inglês e, se preferir, no seu idioma com a ajuda de um tradutor.',
)
SOPORTE_HTML = '''      <h2 id="encontrar">Encontrar a TV</h2>
      <div class="preguntas">
        <details open><summary>A minha TV não aparece na lista</summary>
          <ol>
            <li>Confira se o celular e a TV estão no mesmo Wi-Fi. Se o seu roteador tem uma rede de 2,4 GHz e outra de 5 GHz com nomes diferentes, às vezes elas não se enxergam.</li>
            <li>Confira se a TV está ligada.</li>
            <li>No iPhone, confira se o Mando TV tem a permissão "Rede Local" em Ajustes, Mando TV.</li>
            <li>Toque, na lista de TVs, no botão para o caso de a sua TV não aparecer: o app confere passo a passo as causas mais comuns (o mesmo Wi-Fi, uma VPN, a permissão de rede local e mais) e mostra um botão para conferir de novo depois de cada correção.</li>
            <li>Se ainda não aparecer, toque no botão +, escolha a marca e digite o endereço IP da TV. Você o vê no menu de rede da TV (por exemplo 192.168.1.50).</li>
          </ol>
        </details>
        <details><summary>Funciona com dados móveis ou fora de casa?</summary>
          <p>Não. O Mando TV fala com a TV dentro da rede da sua casa, então o celular precisa estar conectado a esse Wi-Fi.</p>
        </details>
      </div>

      <h2 id="conectar">Conectar pela primeira vez</h2>
      <p>Guias completos por marca: <a href="@@R_lg@@">LG</a>, <a href="@@R_samsung@@">Samsung</a>, <a href="@@R_roku@@">Roku</a> e <a href="@@R_android@@">Android TV</a>.</p>
      <div class="preguntas">
        <details><summary>LG</summary>
          <p>Quando você toca na TV, aparece um aviso na tela dela pedindo permissão. Aceite com o controle de sempre. Você faz isso uma vez só.</p>
        </details>
        <details><summary>Samsung</summary>
          <p>A TV pergunta se você permite a conexão do Mando TV. Escolha "Permitir" com o controle. Se você recusou sem querer, vá em Configurações > Geral > Gerenciador de dispositivos externos > Gerenciador de conexão de dispositivos ("Device Connection Manager") e mude para permitido.</p>
        </details>
        <details><summary>Roku</summary>
          <p>A Roku não pede permissão. Se a conexão falhar, na Roku vá em Configurações > Sistema > Configurações avançadas do sistema > Controle por aplicativos móveis ("Control by mobile apps") e deixe o acesso à rede em Padrão ou Permissivo (nas versões mais novas do software da Roku, deixe "Control by mobile apps" em "Enabled").</p>
        </details>
        <details><summary>Android TV e Google TV</summary>
          <p>A TV mostra um código de 6 caracteres. Digite no Mando TV exatamente como aparece. Funciona para Sony, Philips, TCL, Hisense, Sharp, Xiaomi, Chromecast com Google TV e outras com Android TV.</p>
        </details>
      </div>

      <h2 id="encender">Ligar a TV pelo app</h2>
      <p>O Mando TV liga a TV pela rede da sua casa. Para isso são necessárias duas coisas: ter conectado pelo menos uma vez com a TV ligada e ter ativado na TV a ativação pela rede. O nome da opção muda conforme o modelo; estas são as mais comuns:</p>
      <div class="preguntas">
        <details><summary>LG</summary>
          <p>Procure em Configurações ''' + LG_OPC + ''' e ative ''' + LG_WIFI + '''. Se existir a opção de início rápido ("Quick Start+" em inglês), ative também.</p>
        </details>
        <details><summary>Samsung</summary>
          <p>Ative a opção de ligar com um dispositivo móvel ("Power On with Mobile") em Configurações > Geral > Rede > Configurações de especialista (Expert Settings).</p>
        </details>
        <details><summary>Roku</summary>
          <p>Nas Roku TV, ative ''' + ROKU_RAPIDO + '''. Os aparelhos Roku ligados em uma TV não podem ser ligados assim.</p>
        </details>
        <details><summary>Android TV e Google TV</summary>
          <p>Depende do fabricante. Procure nas configurações de rede ou de energia as opções ''' + AND_WOL_RS + '''. Alguns modelos não têm.</p>
        </details>
      </div>

      <h2 id="falla">Se algo der errado</h2>
      <div class="preguntas">
        <details><summary>Desconecta ou não responde</summary>
          <ol>
            <li>Na tela do controle, toque em Reconectar.</li>
            <li>Se não resolver, feche o Mando TV e abra de novo.</li>
            <li>Se a TV mudou de endereço IP, remova-a da lista e adicione de novo.</li>
          </ol>
        </details>
        <details><summary>Como nos enviar um relatório de erro</summary>
          <ol>
            <li>No Mando TV, toque no botão Personalizar (os controles deslizantes no alto).</li>
            <li>Toque em Copiar relatório de teste.</li>
            <li>Cole em um e-mail para hola@mandotv.app com a marca e o modelo da sua TV.</li>
          </ol>
          <p>O relatório não inclui senhas, códigos nem nada do que você digita.</p>
        </details>
        <details><summary>Comprei o Pro e ele não aparece</summary>
          <p>Em Personalizar, toque em Restaurar compra, com a mesma conta da loja usada na compra. Se ainda não aparecer, escreva para nós.</p>
        </details>
      </div>

      <h2 id="guias">Guias passo a passo</h2>
      <p><a href="@@R_guias@@">Ver todos os guias</a></p>
      <ul>
@@GUIAS@@
      </ul>

      <h2 id="contacto">Ainda tem dúvidas?</h2>
      <p>Escreva para <a href="mailto:hola@mandotv.app?subject=Ajuda%20Mando%20TV">hola@mandotv.app</a>. Diga a marca e o modelo da sua TV e em qual passo você travou. Escreva para nós no seu idioma. Respondemos em espanhol ou inglês e, se preferir, no seu idioma com a ajuda de um tradutor.</p>
'''

PRIVACIDAD = dict(
  titulo='Política de privacidade | Mando TV',
  desc='O Mando TV não pede conta nem dados pessoais: sem anúncios e sem rastreadores. O controle remoto fala direto com a sua TV, dentro do seu Wi-Fi.',
  h1='Privacidade',
  intro='Resumindo: o Mando TV não pede conta nem dados pessoais. Não há anúncios nem rastreadores.',
)
PRIVACIDAD_HTML = '''      <p class="fecha">Em vigor desde 14 de novembro de 2026. Última atualização: 28 de novembro de 2026.</p>

      <h2>Quem somos</h2>
      <p>O Mando TV é um app para controlar a sua TV pelo celular ou pelo computador. Esta política explica quais informações o app usa e o que faz com elas. Para qualquer dúvida, escreva para <a href="mailto:hola@mandotv.app">hola@mandotv.app</a>.</p>

      <h2>Quais dados coletamos</h2>
      <p>No app: apenas o necessário para o teste grátis do Pro no Android e no Windows, explicado em <a href="#prueba">Teste grátis do Pro</a>. Fora isso, o app não envia a nós nem a terceiros nenhuma informação sobre você ou sobre como você o usa. Ele não usa nenhuma ferramenta de análise, publicidade ou rastreamento.</p>
      <p>Neste site: medimos as visitas de duas formas, explicadas na seção <a href="#cookies">Cookies neste site</a>.</p>

      <h2>O que o app guarda no seu aparelho</h2>
      <p>Para funcionar, o app guarda o seguinte apenas no seu celular ou computador:</p>
      <ul>
        <li>As TVs que você adicionou: nome, marca, endereço IP na sua rede e endereço físico da rede (MAC), usado para ligá-la.</li>
        <li>As chaves de conexão que cada TV entrega quando você aceita a permissão. Ficam guardadas criptografadas no armazenamento seguro do sistema (Chaveiro no iPhone e no Mac, Keystore no Android, armazenamento protegido no Windows).</li>
        <li>Suas preferências: tema claro ou escuro, cor de fundo, vibração e tipo de controle.</li>
        <li>Se você usa os recursos Pro: seus aplicativos favoritos, suas rotinas e suas últimas buscas no YouTube (você pode apagá-los pelo app).</li>
        <li>Se você usa: o modo infantil (o PIN é guardado apenas como um código protegido) e os controles que outras pessoas compartilharam com você.</li>
      </ul>
      <p>Se você apagar o app, esses dados são apagados junto, com duas exceções. No Android, se você usa o backup do Google, as preferências do app (como sua lista de TVs e seus ajustes) podem ficar no seu próprio backup do Google e voltar quando você reinstalar o app; as chaves de conexão nunca fazem parte dele. No iPhone e no Mac, as chaves de conexão ficam no Chaveiro do sistema e podem continuar lá depois que você apagar o app.</p>

      <h2>Com quem o app se comunica</h2>
      <p>Com as suas TVs, dentro da rede Wi-Fi da sua casa. Para encontrá-las, o app explora a sua rede local; por isso, no iPhone, ele pede a permissão "Rede Local". O texto que você digita no teclado do app vai direto para a TV e não é guardado.</p>
      <p>Além disso, ao abrir, o app baixa um pequeno arquivo público deste site (mandotv.app/app/config.json) para saber se há uma versão nova para instalar e quais recursos fazem parte do Mando TV Pro. É um download, como abrir uma página: o app não envia os seus dados, as suas TVs nem o que você faz. Só informa a versão do app e o sistema (por exemplo Android), para poder mostrar o aviso certo. Se você estiver sem internet, o app continua funcionando com o último arquivo baixado; se passarem mais de 30 dias sem conseguir baixá-lo, ele pedirá que você se conecte um instante à internet. Como em qualquer visita a um site, esse download também mostra o seu endereço IP ao provedor do nosso site (Cloudflare).</p>

      <p>Se você enviar fotos ou vídeos para a TV (um recurso Pro), a TV baixa só os arquivos que você escolher, direto do seu celular ou PC pelo Wi-Fi da sua casa. Eles não passam pela internet nem por nós, o app não vê o resto das suas fotos e o envio termina quando você fecha essa tela. Dentro da sua rede doméstica, essa transferência não é criptografada.</p>
      <p>Se você usa "Mostrar minha tela na TV" (um recurso Pro), o app captura a sua tela só enquanto você espelha, codifica no seu aparelho e envia pelo Wi-Fi de casa direto para a TV que você escolheu. Nada passa pela internet nem por nós, nada é gravado ou guardado, e o espelhamento termina quando você o encerra ou fecha o app. A TV mostra tudo o que aparece nessa tela, inclusive notificações, e dentro da sua rede doméstica a transmissão não é criptografada.</p>
      <h2 id="prueba">Teste grátis do Pro (Android e Windows)</h2>
      <p>Para que o teste grátis do Pro seja um por aparelho, quando ele começa o app envia uma vez ao nosso servidor (api.mandotv.app, na Cloudflare) duas coisas: uma impressão digital criptografada do identificador que o sistema dá ao app naquele aparelho (no Android, o ID Android próprio do app; no Windows, o identificador do aparelho para os nossos apps) e há quanto tempo o seu teste está em andamento. A impressão digital não revela qual é o aparelho nem quem você é, e o servidor a criptografa de novo com uma chave própria antes de guardá-la.</p>
      <p>Guardamos apenas essa impressão digital, a data em que o teste começou e se é Android ou Windows. Não guardamos o seu endereço IP (a Cloudflare o vê enquanto responde, como em qualquer conexão). Usamos isso só para que reinstalar o app não dê outro teste, o que é prevenção de fraude e nosso interesse legítimo; nunca para publicidade nem para seguir você, e não compartilhamos com ninguém. Cada registro é apagado automaticamente após 24 meses. Se você estiver sem internet, o teste funciona do mesmo jeito. No iPhone e no Mac nada é enviado: o teste é gerenciado pela App Store.</p>

      <h2>Microfone e voz</h2>
      <p>No iPhone, no Mac e no Android, a busca por voz só usa o microfone enquanto você toca no botão para falar. O que você diz é convertido em texto pelo reconhecimento de voz do seu sistema: Apple no iPhone e no Mac e Google no Android, conforme as políticas de privacidade deles. No Windows, a voz é reconhecida no seu próprio PC e não sai dele. Só se esse mecanismo do aparelho não conseguir iniciar ou continuar falhando (por exemplo, um processador antigo ou a falta do modelo de voz), o app usa o ditado do Windows, da Microsoft, que funciona on-line se você ativou o reconhecimento de voz on-line no Windows, conforme a política de privacidade dela. No Windows, o microfone abre quando você abre o painel de voz e fecha quando você o fecha, ou após 30 segundos sem uso; enquanto você não fala, nada é gravado nem guardado. O Mando TV não grava nem guarda o áudio, e o texto obtido vai direto para a sua TV, como o que você digita no teclado.</p>

      <h2>Casa: aparelhos do Apple Casa e do Google Home</h2>
      <p>Se você abrir a seção Casa (em teste), o app pede permissão para ver os aparelhos que você já tem no app Casa da Apple (HomeKit) ou no Google Home. Com essa permissão ele lê o nome, o cômodo e o estado deles (ligado ou desligado, brilho, temperatura ou em que parte do programa está um eletrodoméstico) para mostrá-los e enviar o que você tocar. Tudo acontece entre o seu celular e o sistema da Apple ou do Google: o Mando TV não guarda essa lista, não a envia para nós nem para terceiros e não a usa para publicidade nem análise. No Android, o Google Home funciona com a sua própria conta do Google, conforme a política de privacidade do Google. Você pode remover a permissão quando quiser: no iPhone, em Ajustes &gt; Privacidade e Segurança &gt; HomeKit; no Android, nas configurações da sua conta do Google.</p>
      <p>Se você tocar em "Como o Casa funcionou para você?", o seu app de e-mail abre com uma mensagem para hola@mandotv.app com um resumo técnico: a versão do app, o sistema e quantos aparelhos de cada tipo apareceram e se respondem. Não inclui nomes de aparelhos, de cômodos nem da sua casa, e só é enviado se você enviar.</p>

      <h2>Links e textos que você compartilha</h2>
      <p>Quando você compartilha um controle (um link mandotv.app/m/), o link leva o desenho do controle e uma pista para achar sua TV: nome, marca, modelo e endereço dentro da sua rede. Ele nunca leva chaves de conexão, PINs nem o endereço de hardware da TV. Essas informações viajam depois do sinal #, então nunca chegam aos nossos servidores, mas qualquer pessoa para quem você enviar o link, por exemplo pelo WhatsApp, pode lê-las. Uma rotina compartilhada (um link mandotv.app/r/) leva só o nome e os passos.</p>
      <p>O texto de backup que você pode copiar nos ajustes do app contém seus favoritos, rotinas e ajustes. Ele não é criptografado e vai só para onde você colar.</p>

      <h2>Relatório de teste</h2>
      <p>O app tem um botão "Copiar relatório de teste" para nos ajudar a corrigir erros. O relatório fica só na memória do app enquanto ele está aberto e nunca é enviado sozinho: é você quem decide copiá-lo e compartilhá-lo. Ele não inclui chaves de conexão, códigos de pareamento nem nada do que você digita. Inclui os passos que o app deu, como buscar, conectar e os erros, e dados técnicos: a versão do app, o seu sistema e a marca, o modelo e o endereço da sua TV dentro da sua rede.</p>

      <h2 id="cookies">Cookies neste site</h2>
      <p>Isto vale apenas para o site mandotv.app, não para o app.</p>
      <h3>Nunca usamos cookies</h3>
      <p>Contamos as visitas de forma anônima com o Cloudflare Web Analytics: quantas pessoas visitam o site, quais páginas leem e de que país. Ele não usa cookies, não usa o seu endereço IP para identificar você e não acompanha o que você faz em outros sites.</p>
      <h3>Com cookies, só se você aceitar</h3>
      <p>Se você tocar em "Aceitar" no aviso de cookies, ativamos o Google Analytics (do Google LLC) para entender melhor como o site é usado: páginas vistas, tempo na página, tipo de aparelho, cidade aproximada e de onde você veio. Para isso, ele guarda os cookies _ga e _ga_* no seu navegador por até 2 anos. O Google pode processar esses dados em servidores fora do Chile. Desativamos os recursos de publicidade e o Google Signals, e não usamos esses dados para mostrar anúncios a você.</p>
      <p>Se você tocar em "Rejeitar" ou não escolher nada, o Google Analytics não é carregado e nenhum cookie é guardado. Você pode mudar de ideia quando quiser com o botão "Cookies" no rodapé de cada página; se retirar a sua permissão, apagamos esses cookies.</p>
      <p>A sua escolha fica guardada no seu navegador (armazenamento local, que não é enviado a ninguém) para não perguntarmos de novo. O mesmo armazenamento guarda o idioma que você escolhe no rodapé da página, para que o site abra nele da próxima vez. Para mostrar o preço do Pro do seu país, cada página pergunta ao Cloudflare, que já serve este site, de que país você visita, ou usa a região do idioma do seu navegador; essa resposta não é guardada.</p>

      <h2>Compras</h2>
      <p>Se você comprar o Mando TV Pro, o pagamento é processado pela loja de aplicativos (App Store, Google Play ou Microsoft Store). Nós não recebemos nem guardamos os dados do seu cartão. A loja só confirma ao app que a compra existe.</p>

      <h2>E-mails que você nos envia</h2>
      <p>Se você escrever para <a href="mailto:hola@mandotv.app">hola@mandotv.app</a>, usamos o seu e-mail e o que você nos disser só para responder. Não compartilhamos nem usamos para publicidade. Você pode pedir a qualquer momento que apaguemos as suas mensagens.</p>

      <h2>Crianças</h2>
      <p>O app não coleta dados pessoais de ninguém, incluindo crianças.</p>

      <h2>Mudanças nesta política</h2>
      <p>Se um dia o que o app faz com os seus dados mudar, atualizaremos esta página e a data acima antes de a mudança chegar ao app.</p>
'''


# >>> guías traídas del inglés (ensamblar.py)
# Adaptadas con Ollama (qwen3.6:35b) desde las guías inglesas y auditadas por Opus el 22-nov. Rutas en idiomas_sitio.py.
GUIAS += [
  dict(clave='no-sub', corto='App de controle sem assinatura', fecha='2026-11-23',
    titulo='App de controle remoto sem assinatura e sem anúncios',
    desc='Cansado de apps de controle remoto com anúncios ou assinatura semanal? O Mando TV é grátis e sem anúncios, e o Pro é uma compra única opcional.',
    h1='App de controle remoto sem assinatura e sem anúncios',
    intro='Muitos apps de controle remoto mostram anúncios a cada poucos toques ou pedem assinatura semanal antes de funcionar. O Mando TV segue outro caminho: o controle é grátis, sem anúncios e sem conta. O Pro, que é opcional, é pago uma vez só. Veja a comparação, inclusive o que ele não faz.',
    pasos=[
      'Antes de instalar qualquer app de controle, abra a página da loja e olhe as compras no app. Preços semanais ou mensais ali significam assinatura.',
      'No Google Play, verifique se a página diz "Contém anúncios" e leia as avaliações mais recentes com poucas estrelas: é lá que aparecem as cobranças surpresa.',
      'Confira se o app funciona com a sua TV pelo Wi-Fi. O Mando TV funciona com Samsung (2016 em diante), LG webOS, Roku, Google TV e Android TV, e Fire TV.',
      'Instale o Mando TV, conecte seu celular ao mesmo Wi-Fi da TV e toque na sua TV na lista.',
      'Aceite o aviso na TV ou digite o código que ela mostra. Use o controle. As teclas, o volume, os canais e o teclado são grátis.',
    ],
    tabla=dict(titulo='Mando TV comparado a muitos apps de controle',
      cabeza=['', 'Mando TV', 'Muitos apps com anúncios ou assinatura'],
      filas=[
        ['Controle básico', 'Grátis', 'Muitas vezes grátis com anúncios, ou travado atrás de um teste'],
        ['Anúncios', 'Nenhum', 'Comuns'],
        ['Assinatura', 'Nenhuma. O Pro é uma compra única opcional', 'Planos semanais ou mensais são comuns'],
        ['Conta', 'Não é necessária', 'Varia'],
        ['Smart TVs pelo Wi-Fi', 'Samsung (2016 em diante), LG webOS, Roku, Google TV e Android TV, Fire TV, Apple TV (beta)', 'Varia por app'],
        ['Infravermelho para TVs mais antigas', 'Grátis em celulares Android com emissor infravermelho (novo)', 'Alguns apps, só em celulares com emissor infravermelho'],
        ['Bluetooth', 'Beta no Android 9 e mais recente, grátis', 'Varia por app'],
        ['Fotos e vídeos para a TV', 'Pro, pelo Wi-Fi (não é espelhamento)', 'Varia por app'],
        ['Celulares e computadores', 'iPhone, iPad, Mac e Windows, e Android em teste antecipado', 'Varia'],
        ['Espelhamento de tela', 'Grátis no iPhone, no iPad e no Windows, com o recurso integrado de cada um. No Windows, o Pro também pode espelhar a tela do PC em TVs LG, Samsung, Hisense e Android TV (beta)', 'Alguns apps oferecem'],
      ],
      nota='A comparação não se refere a nenhum app em particular. Confira a página de cada app na loja para ver os preços atuais.'),
    extra=[
      ('O que o Mando TV não faz', 'No iPhone e no iPad, ele leva você ao Espelhar Tela da Central de Controle, o recurso do próprio iPhone, que funciona com TVs compatíveis com AirPlay. No Windows, ele abre o Transmitir (Windows + K), e o Mando TV Pro pode enviar a tela do PC pelo Wi-Fi da sua casa para TVs LG, Samsung, Hisense e Android TV (beta, com alguns segundos de atraso e sem som). Com o Mando TV Pro, ele também pode enviar fotos e vídeos para a TV pelo Wi-Fi da sua casa. Ele controla Smart TVs pelo Wi-Fi da sua casa. Uma TV que não é smart pode ser controlada por infravermelho de um celular Android com emissor infravermelho. No Android 9 ou mais recente, o celular também pode se conectar ao Google TV, Android TV e Fire TV pelo Bluetooth como teclado e controle, sem Wi-Fi. Essa opção está em beta e é grátis.'),
      ('Como o Mando TV ganha dinheiro', 'Não com anúncios nem com seus dados: o app não tem anúncios e não rastreia você. O Mando TV é pago pelo Pro, uma compra única opcional para recursos extras. O controle básico é grátis.'),
      ('Nos dispositivos que você já tem', 'iPhone, iPad e Mac pela App Store, PCs com Windows pela Microsoft Store, e Android por meio do teste antecipado grátis no Google Play. Veja [App de controle remoto para iPhone](@iphone) e [App de controle remoto para Windows](@windows).'),
      ('Privacidade', 'Sem conta e sem rastreamento no app. Ele se comunica com a TV só dentro da rede da sua casa, e as chaves de conexão com a TV ficam criptografadas no seu dispositivo. Detalhes na [política de privacidade](@privacidad).'),
    ],
    marca=None,
    faq=[
      ('Existe um app de controle remoto sem assinatura?', 'Sim. O Mando TV não tem nenhuma assinatura: o controle é grátis, sem anúncios, e o Pro é uma compra única opcional.'),
      ('O Mando TV é realmente grátis?', 'Sim. As setas, OK, Voltar, Início, volume, canais, teclas numéricas, teclado e ligar ou desligar são grátis, sem anúncios e sem limite de tempo.'),
      ('Funciona sem Wi-Fi?', 'Na maioria das vezes, não. O Mando TV controla Smart TVs pelo Wi-Fi da sua casa. As exceções são o infravermelho em celulares Android que têm emissor infravermelho, que também funciona com TVs que não são smart e TVs que nunca foram conectadas ao Wi-Fi, e o Bluetooth em beta no Android 9 ou mais recente, que funciona com Google TV, Android TV e Fire TV.'),
    ]),
  dict(clave='roku-app-alt', corto='Alternativa ao app da Roku', fecha='2026-11-23',
    titulo='Alternativa ao app da Roku: controle simples e grátis',
    desc='Controle sua Roku TV ou player pelo celular via Wi-Fi com o Mando TV. Sem conta, sem anúncios. Também controla Samsung, LG e Google TV.',
    h1='Controle Roku pelo celular: alternativa ao app oficial',
    intro='O app oficial da Roku faz várias coisas: loja de canais, transmissão de conteúdo, escuta privada e controle remoto. Se você quer só um controle rápido ou também tem uma TV Samsung, LG ou Google TV em casa, o Mando TV é uma alternativa simples que controla a Roku pela sua rede Wi-Fi, sem precisar de conta.',
    pasos=[
      'Conecte o celular e a Roku à mesma rede Wi-Fi.',
      'Baixe e abra o Mando TV. A sua Roku TV ou o seu player Roku aparece na lista. Toque no aparelho. A Roku não pede código.',
      'Use o direcional, OK, Voltar, Início, volume e o teclado. Digite buscas nos canais da Roku com o teclado do celular.',
      'Se as teclas não responderem, na Roku, vá em Configurações > Sistema > Configurações avançadas do sistema > Controle por aplicativos móveis ("Control by mobile apps") e defina o acesso à rede como Padrão ou Permissivo. Em versões mais novas do software da Roku, ative a opção de controle por aplicativos móveis.',
      'Opcional: em TVs Roku, ative a opção de início rápido da TV ("Fast TV start") em Configurações > Sistema > Energia para que o Mando TV possa ligar a TV.',
    ],
    extra=[
      ('Quando o Mando TV é melhor', 'Um app para várias TVs: Roku, Samsung, LG e Google TV ou Android TV. Sem conta, sem anúncios. Também funciona no Windows, o que é útil na mesa de trabalho. O direcional e o volume respondem rápido, e o teclado facilita digitar buscas.'),
      ('Quando o app oficial da Roku é melhor', 'Mantenha o app da Roku para o que ele oferece além do controle remoto, como navegar e adicionar canais na Loja de Canais da Roku, além das funções próprias de transmissão de conteúdo e escuta privada. Use os dois se preferir. Eles podem rodar no mesmo celular.'),
      ('TVs Roku e players Roku', 'Os dois funcionam. Inclui modelos de Roku TV de marcas como TCL, Hisense, Philips e outras, além dos players Roku Express, Streaming Stick e Ultra. Detalhes estão na [página do app de controle remoto para Roku](@roku).'),
      ('Se o app da Roku parou de funcionar', 'Se as teclas pararam de responder, a Roku provavelmente está bloqueando o controle por apps. O guia [Roku não responde ao celular](@roku-403) mostra como resolver.'),
      ('Grátis e Pro', 'As setas, OK, Voltar, Início, volume, canais, números, teclado, abrir apps, trocar entradas e ligar ou desligar são grátis, sem anúncios nem assinatura. O touchpad, os comandos de voz, os apps favoritos, as rotinas e o timer para desligar fazem parte do Mando TV Pro, uma compra única sem assinatura.'),
    ],
    marca='roku',
    faq=[
      ('Preciso de conta Roku para usar o Mando TV?', 'Não. O Mando TV se comunica com a Roku pela sua rede doméstica e não pede conta.'),
      ('O Mando TV substitui totalmente o app da Roku?', 'Para o controle remoto, sim. Para a loja de canais, transmissão de conteúdo e escuta privada, mantenha o app oficial da Roku.'),
      ('Funciona no meu Roku Express ou Streaming Stick?', 'Sim. Todos os players Roku e TVs Roku são controlados da mesma forma.'),
    ]),
  dict(clave='lg-thinq', corto='Alternativa ao app LG ThinQ', fecha='2026-11-23',
    titulo='Alternativa ao LG ThinQ: controle da TV LG sem conta',
    desc='Procura uma alternativa ao LG ThinQ só para controlar a TV? O Mando TV controla TVs LG com webOS pelo Wi-Fi, sem conta LG e sem anúncios.',
    h1='Alternativa ao app LG ThinQ para controlar a sua TV LG',
    intro='O LG ThinQ é o app oficial da LG, feito para gerenciar toda a casa inteligente: eletrodomésticos, a TV e mais. Se você quer só um controle simples para a TV, o Mando TV faz esse serviço pela rede Wi-Fi da sua casa, sem conta LG e sem anúncios.',
    pasos=[
      'Conecte o celular ou o PC (iPhone, Android ou Windows) e a TV LG ao mesmo Wi-Fi.',
      'Baixe o Mando TV e abra-o. A sua TV LG aparece na lista sozinha. Toque nela.',
      'A TV mostra uma mensagem pedindo permissão. Aceite uma vez com o controle da TV, o joystick embaixo da tela ou o Magic Remote.',
      'Use os botões, o volume e o teclado logo de cara. Não precisa de conta LG nem de cadastro na TV.',
      'Opcional: ative a opção de ligar a TV com o celular ("TV On With Mobile") nas Configurações da TV para também ligá-la pelo celular.',
    ],
    extra=[
      ('Mando TV ou LG ThinQ: qual usar', 'Use o ThinQ se quiser gerenciar eletrodomésticos LG como máquina de lavar, geladeira ou ar-condicionado, ou recursos da conta LG. Use o Mando TV se quiser um controle rápido e simples para a TV que também funciona com Samsung, Roku e Google TV no mesmo app. Muitas pessoas usam os dois: ThinQ para eletrodomésticos, Mando TV para a TV.'),
      ('O que o Mando TV faz na TV LG', 'Funciona com Smart TVs LG com webOS, ou seja, a maioria dos modelos desde 2014, incluindo LED, NanoCell, QNED e OLED. Oferece as setas, OK, Voltar, Início, volume, canais, mudo, controles de reprodução e um teclado para digitar na busca da TV e na maioria dos aplicativos. A lista de apps e a de entradas também são grátis. Com o Pro você ainda tem um ponteiro como o do Magic Remote.'),
      ('O que o Mando TV não faz', 'Não controla eletrodomésticos LG, não usa sua conta LG e não substitui os serviços da conta LG na TV. É só um controle remoto, não um hub de casa inteligente.'),
      ('Privacidade e anúncios', 'O Mando TV não tem anúncios nem pede conta. Ele se comunica com a TV dentro da sua rede doméstica e guarda a chave de conexão criptografada no seu dispositivo. A [página do app de controle remoto para LG](@lg) tem a lista completa de recursos.'),
      ('Grátis e Pro', 'As setas, OK, Voltar, Início, volume, canais, números, teclado, abrir apps, trocar entradas e ligar ou desligar são grátis, sem anúncios nem assinatura. O touchpad, os comandos de voz, os apps favoritos, as rotinas e o timer para desligar fazem parte do Mando TV Pro, uma compra única sem assinatura.'),
    ],
    marca='lg',
    faq=[
      ('Posso controlar a TV LG sem o app LG ThinQ?', 'Sim. O Mando TV se conecta às TVs LG com webOS direto pelo seu Wi-Fi. Você aceita um aviso na TV na primeira vez e pronto, sem conta LG.'),
      ('O Mando TV funciona com o ponteiro do Magic Remote?', 'O Mando TV Pro tem um ponteiro que você move com o dedo na tela do celular, do mesmo jeito que o Magic Remote move a seta.'),
      ('O Mando TV é feito pela LG?', 'Não. O Mando TV é um app independente e não tem vínculo com a LG. LG e ThinQ são marcas de seus respectivos donos, citadas apenas para indicar compatibilidade.'),
    ]),
  dict(clave='smartthings', corto='Alternativa ao controle do SmartThings', fecha='2026-11-23',
    titulo='SmartThings não funciona? Veja esta alternativa simples',
    desc='O controle do SmartThings não funciona ou está lento? Use o Mando TV para controlar TVs Samsung com Tizen pelo Wi-Fi, sem conta Samsung e sem anúncios.',
    h1='Alternativa ao controle do SmartThings para TVs Samsung',
    intro='O SmartThings é o app da Samsung para toda a casa inteligente, e seu controle de TV funciona pela sua conta Samsung. Se esse controle parou de funcionar ou você quer um mais rápido, o Mando TV controla TVs Samsung com Tizen (modelos de 2016 em diante) direto pelo Wi-Fi da sua casa, sem precisar de conta.',
    pasos=[
      'Conecte o celular e a TV Samsung ao mesmo Wi-Fi.',
      'Baixe o Mando TV e abra-o. Sua TV Samsung aparece sozinha na lista. Toque nela.',
      'A TV pede para aceitar a conexão. Escolha Permitir com o controle remoto ou com o botão da TV (só na primeira vez).',
      'Use as setas, OK, Voltar, Início, volume, canais e o teclado na hora.',
      'Opcional: em Configurações > Geral > Rede > Configurações de especialista (Expert Settings), ative a opção de ligar com um dispositivo móvel ("Power On with Mobile") para que o Mando TV também ligue a TV.',
    ],
    extra=[
      ('Por que o controle pelo celular para de funcionar', 'As causas mais comuns são simples: o celular e a TV estão em Wi-Fis diferentes, há uma VPN ligada ou a TV está em suspensão profunda. Com o SmartThings, a conta Samsung é mais uma coisa que pode falhar, como a sessão sair sozinha. O Mando TV fala direto com a TV na rede da sua casa, sem conta para entrar. Veja mais soluções em [O celular não encontra a TV](@not-found).'),
      ('Mando TV ou SmartThings: qual usar', 'Mantenha o SmartThings se você usa eletrodomésticos Samsung, luzes ou outros dispositivos da casa inteligente, ou recursos da conta Samsung. Use o Mando TV quando quiser só um controle rápido para a TV, ou se também tiver em casa uma TV LG, Roku, Google TV ou Fire TV: um só app controla todas. Os dois podem estar no mesmo celular.'),
      ('Se você recusou a permissão sem querer', 'Na TV, vá em Configurações > Geral > Gerenciador de dispositivos externos > Gerenciador de conexão de dispositivos ("Device Connection Manager") e deixe o Mando TV como permitido.'),
      ('Sem controle nenhum?', 'Você pode aceitar o aviso com o botão da própria TV. O guia [TV Samsung sem controle remoto](@samsung-lost) mostra como fazer isso.'),
      ('Grátis e Pro', 'O controle é grátis para baixar e usar, sem anúncios nem assinatura. O Mando TV Pro é uma compra única opcional para recursos extras.'),
    ],
    marca='samsung',
    faq=[
      ('Posso controlar a TV Samsung sem o SmartThings?', 'Sim. O Mando TV se conecta às TVs Samsung com Tizen direto pelo Wi-Fi. Você aceita a conexão uma vez na TV, sem conta Samsung.'),
      ('O Mando TV controla eletrodomésticos Samsung?', 'Não. É só um controle de TV. Mantenha o SmartThings para eletrodomésticos e outros dispositivos da casa inteligente.'),
      ('O Mando TV é feito pela Samsung?', 'Não. O Mando TV é um app independente e não tem afiliação com a Samsung. Samsung e SmartThings são marcas de seus respectivos donos, citadas apenas para indicar compatibilidade.'),
    ]),
  dict(clave='googletv-alt', corto='Alternativa ao controle do Google TV', fecha='2026-11-23',
    titulo='Controle do Google TV não funciona? Use esta alternativa',
    desc='O controle do celular para o Google TV não acha sua TV? O Mando TV controla o Google TV e Android TV pelo Wi-Fi, sem conta Google e sem anúncios.',
    h1='Alternativa ao controle do Google TV no seu celular',
    intro='O controle do celular para o Google TV e Android TV fica dentro do app da Google e depende da sua conta Google. Quando ele não acha a TV, você fica travado. O Mando TV é um app separado que pareia com o código de 6 caracteres na tela da TV e funciona sem conta Google, no iPhone, no Android ou no PC com Windows.',
    pasos=[
      'Ligue a TV e conecte o celular à mesma rede Wi-Fi.',
      'Baixe o Mando TV e abra-o. Toque na sua Google TV ou Android TV na lista.',
      'A TV mostra um código de 6 caracteres. Digite-o no Mando TV e toque em Parear.',
      'Use as setas, OK, Voltar, Início, volume e o teclado. Não precisa fazer login em nada.',
      'Opcional: procure "Wake on LAN" ou uma opção de ligar pela rede nas configurações da TV para que o app também ligue a TV.',
    ],
    extra=[
      ('Por que o controle do celular para de achar a TV', 'Na maioria das vezes é a rede: o celular e a TV estão em redes Wi-Fi diferentes, há uma VPN ativa ou uma rede de convidados separa os dispositivos. Resolva isso primeiro, pois afeta todo app de controle. Veja [O celular não encontra a TV](@not-found).'),
      ('Com quais TVs funciona', 'TVs com Google TV e Android TV da Sony, TCL, Hisense, Philips, Sharp, Xiaomi, Toshiba e outras, além do Chromecast com Google TV, Google TV Streamer e Nvidia Shield. Todas pareiam do mesmo jeito, com o código na tela, uma única vez.'),
      ('Onde o app da Google é melhor', 'O app da Google também ajuda a achar o que assistir e guarda a sua lista para assistir depois. Mantenha-o para isso. O Mando TV é só o controle remoto e ainda controla Samsung, LG, Roku e Fire TV no mesmo app e no PC.'),
      ('Se o antigo app de controle do Android TV sumiu', 'A Google moveu o controle do celular do antigo app Android TV Remote Control para o app Google TV. Se você quer um controle remoto independente, o Mando TV é uma opção.'),
      ('Grátis e Pro', 'O controle é grátis para baixar e usar, sem anúncios nem assinatura. O Mando TV Pro é uma compra única opcional para recursos extras.'),
    ],
    marca='android',
    faq=[
      ('Preciso de conta Google para usar o Mando TV com o Google TV?', 'Não. O código na tela da TV basta para parear.'),
      ('Funciona com o Chromecast com Google TV?', 'Sim. Pareia do mesmo jeito, com o código de 6 caracteres na tela.'),
      ('Posso usar no iPhone?', 'Sim. O Mando TV está na App Store para iPhone e iPad, na Microsoft Store para Windows e em teste antecipado grátis no Google Play para Android.'),
    ]),
  dict(clave='windows', corto='Controle remoto para Windows', fecha='2026-11-23',
    titulo='App de controle remoto para Windows: controle a TV pelo PC',
    desc='Controle a TV Samsung, LG, Roku, Google TV ou Fire TV pelo PC com o Mando TV: atalhos de teclado, mini controle e conexão via Wi-Fi. Na Microsoft Store.',
    h1='App de controle remoto da TV para PC com Windows',
    intro='O Mando TV tem um app para Windows que transforma seu PC ou notebook em um controle remoto pela rede da sua casa. Digite na TV com o teclado real, mantenha uma janela de controle pequena sobre as outras janelas enquanto trabalha e controle TVs Samsung, LG, Roku, Google TV ou Fire TV pelo mesmo app.',
    pasos=[
      'Instale o Mando TV grátis pela Microsoft Store em um PC com Windows 10 ou 11.',
      'Confira se o PC e a TV estão na mesma rede, via Wi-Fi ou cabo conectado ao mesmo roteador.',
      'Abra o Mando TV. A TV aparece na lista. Clique nela.',
      'Aceite o aviso na TV se ela pedir (LG, Samsung), ou digite o código que aparece (Google TV, Fire TV).',
      'Clique nos botões ou digite uma busca com seu teclado. Pronto.',
    ],
    extra=[
      ('Atalhos de teclado (Pro)', 'Com o Pro, o teclado do PC vira o controle: setas para mover, Enter para OK, Backspace ou Esc para voltar, mais e menos para volume, M para mudo e Espaço para pausar.'),
      ('Mini controle (Pro)', 'Uma janela de controle pequena que fica sobre as outras janelas, para você mudar o volume ou pausar sem sair do que está fazendo.'),
      ('Digitar na TV pelo PC', 'O teclado na tela da TV é lento. No Mando TV você digita com seu teclado real e o texto vai direto para a busca da TV. Essa parte é grátis.'),
      ('Mais detalhes', 'Para a versão passo a passo, veja [como controlar a TV pelo PC](@pc). Para controle pelo celular, leia [celular como controle remoto pelo Wi-Fi](@wifi).'),
      ('Grátis e Pro', 'As setas, OK, Voltar, Início, volume, canais, teclas numéricas, teclado, abrir apps, trocar entradas e ligar ou desligar são grátis, sem anúncios nem assinatura. O touchpad, os comandos de voz, os apps favoritos, as rotinas e o timer para desligar fazem parte do Mando TV Pro, uma compra única sem assinatura. No Windows, o Pro é comprado pela Microsoft Store.'),
      ('Comandos de voz pelo PC (Pro)', 'Com o Pro, você fala com a TV pelo microfone do PC. O reconhecimento de voz acontece no próprio PC: não precisa de internet nem de mudar configurações do Windows. O que você diz nunca sai do PC e não é armazenado. Apenas em processadores muito antigos o app usa a digitação por voz do Windows, que exige "Reconhecimento de fala online" ligado em Configurações > Privacidade e segurança > Fala e seu idioma adicionado no Windows.'),
    ],
    marca=None,
    faq=[
      ('O app de controle remoto para Windows precisa de Bluetooth ou cabo?', 'Não. Ele usa a rede da sua casa. O PC e a TV só precisam estar conectados ao mesmo roteador.'),
      ('Quais TVs posso controlar pelo Windows?', 'TVs Samsung com Tizen, LG com webOS, Roku TV e aparelhos Roku, Google TV e Android TV, e Fire TV.'),
      ('Posso ver a imagem da TV na tela do PC ou ouvir nos alto-falantes dele?', 'Não. O Mando TV é apenas um controle remoto. Ele não espelha nem transmite a imagem da TV para o computador.'),
      ('Por que a voz não funciona no meu PC com Windows?', 'A voz é um recurso Pro, então confira se o Pro está ativo e se o microfone do PC funciona. Na maioria dos PCs, a voz é reconhecida no próprio PC, sem internet. Apenas em processadores muito antigos o app usa a digitação por voz do Windows: ligue "Reconhecimento de fala online" em Configurações > Privacidade e segurança > Fala e adicione seu idioma em Configurações > Hora e idioma.'),
    ]),
  dict(clave='iphone', corto='Controle remoto para iPhone', fecha='2026-11-23',
    titulo='App de controle remoto para iPhone: Samsung, LG e Roku',
    desc='Use o iPhone como controle da TV Samsung, LG, Roku, Google TV e Fire TV pelo Wi-Fi. Grátis na App Store, sem conta e sem anúncios.',
    h1='Controle remoto no iPhone para todas as TVs',
    intro='O Mando TV transforma seu iPhone ou iPad em um controle remoto para TVs Samsung, LG, Roku, Google TV ou Android TV e Fire TV, pelo Wi-Fi da sua casa. É grátis na App Store, sem conta e sem anúncios. Também funciona no Android e no Windows.',
    pasos=[
      'Baixe o Mando TV grátis na App Store.',
      'Conecte o iPhone e a TV à mesma rede Wi-Fi.',
      'Abra o Mando TV e toque em Permitir quando o iOS pedir acesso à Rede Local. O app precisa disso para encontrar a TV.',
      'Toque na sua TV na lista. Aceite o aviso na tela da TV se ela pedir (LG e Samsung), ou digite o código que a TV mostrar (Google TV ou Fire TV).',
      'Use os botões, o volume e o teclado. Você está conectado.',
    ],
    extra=[
      ('Funciona com estas TVs', 'LG com webOS, Samsung com Tizen (2016 em diante), Roku TV e aparelhos Roku, Google TV e Android TV, e Fire TV. As páginas de cada marca são [Samsung](@samsung), [LG](@lg), [Roku](@roku) e [Android TV](@android).'),
      ('Por que o app pede a Rede Local', 'O iPhone não deixa os apps verem os aparelhos da sua rede sem a sua permissão. Se a TV não aparecer na lista, abra Ajustes > Mando TV e ative Rede Local. O app só conversa com sua TV dentro da sua casa.'),
      ('Por que um app para iPhone e não o da marca da TV', 'Cada marca de TV tem seu próprio app, e cada uma quer sua própria configuração ou conta. O Mando TV é um app para todas elas, sem conta.'),
      ('Grátis e Pro no iPhone', 'As setas, OK, Voltar, Início, volume, canais, números, teclado, abrir apps, trocar entradas e ligar ou desligar são grátis, sem anúncios nem assinatura. O touchpad, os comandos de voz, os apps favoritos, as rotinas e o timer para desligar fazem parte do Mando TV Pro, uma compra única sem assinatura. Você compra o Pro uma única vez, direto no app.'),
    ],
    marca=None,
    faq=[
      ('O Mando TV é grátis no iPhone?', 'O download é grátis, sem anúncios. O controle básico é grátis, assim como abrir apps e trocar entradas. Extras como o touchpad, os comandos de voz e as rotinas fazem parte do Mando TV Pro, uma compra única.'),
      ('Funciona no iPad?', 'Sim. O mesmo app roda no iPhone e no iPad.'),
      ('Um app de controle para iPhone precisa de Bluetooth ou emissor infravermelho?', 'No iPhone, não. O iPhone não tem emissor infravermelho, então o controle por infravermelho não está disponível lá, e a opção Bluetooth é só para Android 9 ou mais novo, não para iPhone. No iPhone, o Mando TV controla Smart TVs e Apple TV (beta) pela sua rede Wi-Fi.'),
    ]),
  dict(clave='firetv', corto='Controle remoto do Fire TV', fecha='2026-11-23',
    titulo='Controle remoto do Fire TV no celular ou no PC',
    desc='Controle o Fire TV Stick, Cube ou Smart TV com Fire TV pelo Wi-Fi usando um PIN de 4 dígitos. Sem precisar do app da Amazon.',
    h1='Controle o Fire TV pelo celular ou PC',
    intro='Se o controle do Fire TV sumiu ou as pilhas acabaram, o Mando TV controla o Fire TV Stick, o Fire TV Cube ou uma TV com Fire TV integrado pelo Wi-Fi. O pareamento exige um PIN de 4 dígitos. O Fire TV é novidade no Mando TV, então atualize o app antes.',
    pasos=[
      'Atualize o Mando TV para a versão mais recente na App Store, Microsoft Store ou Google Play.',
      'Ligue o Fire TV e conecte o celular à mesma rede Wi-Fi.',
      'Abra o Mando TV. O seu Fire TV aparece na lista. Toque nele.',
      'A tela da TV mostra um PIN de 4 dígitos. Digite-o no Mando TV. Você faz isso apenas uma vez.',
      'Use as setas, OK, Voltar, Início, botões de reprodução e o teclado para digitar buscas.',
    ],
    extra=[
      ('Dispositivos Fire TV compatíveis', 'Fire TV Stick, Fire TV Stick 4K, Fire TV Cube e TVs com Fire TV integrado, como as TVs Amazon Fire TV Edition e alguns modelos Hisense. O suporte é novo e os testes em dispositivos reais são limitados. Se algo não funcionar como esperado, informe o modelo pela página de Ajuda.'),
      ('Como ligar o Fire TV', 'O Mando TV não liga o Fire TV pela rede. Ligue a TV pelo botão de energia: um Fire TV Stick ou Cube conectado a ela geralmente acorda junto por HDMI-CEC; em uma TV com Fire TV integrado, a própria TV é o Fire TV. Depois, controle-a pelo celular.'),
      ('Se o Fire TV não aparecer', 'Confira se os dois dispositivos estão no mesmo Wi-Fi e se o Fire TV está ligado. No iPhone, permita a Rede Local para o Mando TV nos Ajustes. Veja [O celular não encontra a TV](@not-found).'),
      ('Sem controle nenhum?', 'Você precisa que o Fire TV mostre o PIN na tela; portanto, a TV e o Fire TV devem estar ligados e exibindo imagem. Se a TV estiver em uma entrada errada, mude-a com os botões físicos da TV. Veja [mudar a entrada HDMI sem controle](@hdmi).'),
      ('Grátis e Pro', 'As setas, OK, Voltar, Início, volume, canais, números, teclado, abrir apps, trocar de entrada e ligar ou desligar são grátis, sem anúncios nem assinatura. O touchpad, os comandos de voz, os apps favoritos, as rotinas e o timer para desligar fazem parte do Mando TV Pro, uma compra única sem assinatura.'),
    ],
    marca=None,
    faq=[
      ('Preciso do app da Amazon Fire TV?', 'Não. O Mando TV se conecta ao Fire TV pelo Wi-Fi com um PIN. Não é necessário ter uma conta Amazon no celular.'),
      ('Funciona com TVs com Fire TV integrado e com o Fire TV Stick?', 'Sim, foi feito para isso. O suporte é novo; mantenha o app atualizado e informe-nos sobre qualquer modelo que não funcione.'),
      ('Por que preciso de um PIN?', 'O Fire TV mostra um PIN de 4 dígitos para provar que você está diante da tela. Ninguém consegue parear sem ver a imagem.'),
    ]),
  dict(clave='firetv-lost', corto='Controle do Fire TV perdido', fecha='2026-11-23',
    titulo='Perdeu o controle do Fire TV? Use o celular',
    desc='Perdeu o controle do Fire TV Stick ou Cube? Controle-o pelo celular via Wi-Fi com um PIN de 4 dígitos. Soluções para nova rede Wi-Fi e HDMI-CEC.',
    h1='Controle do Fire TV perdido: use o celular',
    intro='Se o controle do seu Fire TV Stick, Fire TV Cube ou Smart TV com Fire TV se perdeu ou parou de funcionar, o celular assume o controle, desde que o Fire TV esteja conectado à sua rede Wi-Fi. O pareamento usa um PIN de 4 dígitos que aparece na tela da TV, então você nunca precisa do controle antigo para isso.',
    pasos=[
      'Ligue a TV pelo botão físico dela. Um Fire TV Stick ou Cube conectado a ela geralmente acorda junto, e com o HDMI-CEC ativado, a TV muitas vezes muda para a entrada dele sozinha.',
      'Se a TV mostrar outra entrada, mude-a usando o botão de entrada na TV. Veja [mudar a entrada HDMI sem controle](@hdmi).',
      'Conecte o celular à mesma rede Wi-Fi do Fire TV.',
      'Baixe e abra o Mando TV no celular. O seu Fire TV aparece na lista. Toque nele.',
      'A TV mostra um PIN de 4 dígitos. Digite-o no Mando TV. Você faz isso apenas uma vez.',
      'Use as setas, OK, Voltar, Início, volume, botões de reprodução e o teclado do seu celular.',
    ],
    extra=[
      ('Tente usar o controle da TV primeiro (HDMI-CEC)', 'Muitos controles de TV podem comandar um Fire TV Stick através do HDMI-CEC. Com a tela do Fire TV visível, pressione as setas e OK no controle da TV. Se nada acontecer, ative o CEC nas configurações da TV (Anynet+ na Samsung, SIMPLINK na LG, BRAVIA Sync na Sony) e, no Fire TV, ative o controle de dispositivos HDMI CEC nas configurações de tela e som ("Display & Sounds").'),
      ('Se você mudou ou trocou o Wi-Fi', 'Sem o controle, não é possível digitar a nova senha do Wi-Fi no Fire TV, mas há uma solução: em um segundo celular, crie um ponto de acesso com exatamente o mesmo nome e senha da sua rede Wi-Fi antiga. O Fire TV se conecta a ele automaticamente. Conecte o celular com o Mando TV a esse ponto de acesso, pareie com o PIN, vá depois em Configurações > Rede no Fire TV e escolha seu novo Wi-Fi. Por fim, conecte também o seu celular à nova rede.'),
      ('Parear um controle substituto', 'A maioria dos controles novos do Fire TV pareia ao segurar o botão Início por cerca de 10 segundos perto do Fire TV. Se não parear, vá em Configurações > Controles e dispositivos Bluetooth > Controles remotos Amazon Fire TV > Adicionar novo controle remoto. Você pode acessar esse menu pelo celular com o Mando TV.'),
      ('Fire TV integrado à TV', 'Em TVs com Fire TV integrado, como muitos modelos Insignia e Toshiba, os mesmos passos funcionam porque a própria TV é o Fire TV.'),
      ('Antes de começar', 'O suporte ao Fire TV chegou recentemente ao Mando TV; atualize o app primeiro. Se o seu modelo não funcionar como esperado, avise-nos na [página de ajuda](@soporte) incluindo o nome do modelo.'),
      ('Grátis e Pro', 'O controle é gratuito para baixar e usar, sem anúncios nem assinatura. O Mando TV Pro é uma compra única opcional para recursos extras.'),
    ],
    marca=('firetv', 'Controle remoto do Fire TV'),
    faq=[
      ('Posso controlar um Fire TV Stick pelo celular sem o controle?', 'Sim, se o Fire TV estiver ligado e conectado ao Wi-Fi. O Mando TV pareia com o PIN de 4 dígitos mostrado na TV, então você não precisa do controle antigo em momento algum.'),
      ('Funciona se o Fire TV estiver em uma rede Wi-Fi nova?', 'Não diretamente, porque o celular e o Fire TV precisam estar na mesma rede. Primeiro, coloque o Fire TV de volta online usando o truque do ponto de acesso descrito nesta página.'),
      ('Preciso do app Amazon Fire TV ou de uma conta Amazon no celular?', 'Não. O Mando TV se conecta ao Fire TV pela rede da sua casa usando o PIN e não exige nenhuma conta própria.'),
    ]),
  dict(clave='turn-on', corto='Ligar a TV sem o controle', fecha='2026-11-23',
    titulo='Como ligar a TV sem o controle (todas as marcas)',
    desc='Saiba onde fica o botão de ligar em TVs Samsung, LG, TCL, Hisense e Sony. Aprenda a usar HDMI-CEC e o celular para ligar a TV pelo Wi-Fi.',
    h1='Como ligar a TV sem o controle original',
    intro='Quase toda TV ainda tem um botão físico de ligar. Ele só fica bem escondido. Veja onde procurar por marca e duas formas de evitar essa busca no futuro: usar HDMI-CEC de um console ou aparelho de streaming, ou ligar a TV pelo celular via Wi-Fi.',
    pasos=[
      'Olhe embaixo do centro da tela, logo atrás do logotipo da marca. Muitas TVs têm um botão pequeno ou joystick ali, virado para baixo.',
      'Se não estiver lá, passe a mão pela parte de trás da TV perto dos cantos inferiores e depois pelas bordas laterais esquerda e direita.',
      'Pressione o botão uma vez. Em muitas TVs com botão único, quando a TV já está ligada, um aperto curto abre um menu pequeno para entrada e volume, e um aperto longo desliga.',
      'Ainda nada? Confira o cabo de energia nas duas pontas e tente outra tomada. Se a luz de standby não acender, a TV não está recebendo energia.',
      'Com a TV ligada, configure-a para não precisar mais do botão: ative o HDMI-CEC e o ligar pela rede, explicados abaixo.',
    ],
    extra=[
      ('Onde fica o botão de ligar por marca', 'Samsung: um botão ou joystick sob o centro da tela ou na parte de trás em um canto inferior. LG: um joystick sob a logo LG na maioria dos modelos. TCL e Hisense: geralmente um botão pequeno sob o meio da tela ou atrás perto de um canto inferior. Sony: na parte de trás ou numa borda lateral, perto da base. Vizio: na parte de trás, no canto inferior esquerdo ou inferior direito, ou na lateral. Os locais mudam por modelo; se não encontrar, procure o manual pelo número do modelo na etiqueta de trás.'),
      ('Ligar a TV por console ou aparelho de streaming (HDMI-CEC)', 'Com HDMI-CEC ativado, ligar um PlayStation, Xbox, Roku, Fire TV Stick ou Chromecast também liga a TV e muda para a entrada correta. Cada marca dá um nome diferente à configuração: Anynet+ na Samsung, SIMPLINK na LG, BRAVIA Sync na Sony e CEC na maioria das outras. Mais em [ligar a TV e mudar para o HDMI do console](@console).'),
      ('Ligar a TV pelo celular', 'Smart TVs podem ligar via Wi-Fi se você permitir uma vez, e então o Mando TV as liga pelo celular. Na Samsung, em Configurações > Geral > Rede > Configurações de especialista, ative a opção de ligar com um dispositivo móvel ("Power On with Mobile"). Na LG, ative a opção de ligar a TV com o celular ("TV On With Mobile") ([passo a passo](@lg-on)). Em uma Roku TV, ative o início rápido da TV ("Fast TV start") em Configurações > Sistema > Energia. No Google TV e Android TV, procure "Wake on LAN" ou uma opção de ligar pela rede, se o modelo tiver. Você faz isso uma vez, com a TV ligada.'),
      ('Se não encontrar nenhum botão', 'Algumas TVs recentes escondem tanto o único botão que parece que não existe. Procure um pequeno relevo ou área de sensor de luz sob a tela: o botão costuma ficar ao lado. Pelo Wi-Fi, o Mando TV precisa que a TV tenha estado ligada e conectada uma vez. A exceção é o infravermelho: em um celular Android com emissor infravermelho, o Mando TV pode ligar uma TV nunca configurada, bastando apontar o celular para ela. O infravermelho é novo e funciona com as marcas na lista de códigos do app.'),
      ('Grátis e Pro', 'O controle é grátis para baixar e usar, sem anúncios nem assinatura. O Mando TV Pro é uma compra única opcional para recursos extras.'),
    ],
    marca=None,
    faq=[
      ('Posso ligar a TV pelo celular se nunca configurei?', 'Pelo Wi-Fi, não. Uma TV desligada só acorda pela rede se o ligar pela rede tiver sido ativado antes. Na primeira vez, use o botão da TV. A exceção é um celular Android com emissor infravermelho: o Mando TV pode ligar por infravermelho sem configuração, se a marca estiver na lista ou você escolher "Outra marca ou não sei".'),
      ('Como ligo uma Samsung sem o controle?', 'Pressione o botão sob o centro da tela ou atrás num canto inferior. Depois ative a opção de ligar com um dispositivo móvel ("Power On with Mobile") para o celular ligar a TV na próxima vez.'),
      ('Como ligo uma Roku TV sem o controle?', 'Use o botão físico, geralmente sob o centro ou atrás. Depois ative o início rápido da TV ("Fast TV start") em Configurações > Sistema > Energia para o Mando TV ligar a TV pelo celular.'),
      ('Por que a TV liga sozinha quando ligo o console?', 'Isso é HDMI-CEC. É útil, mas você pode desativar nas configurações da TV se preferir.'),
    ]),
  dict(clave='sony', corto='Controle remoto Sony', fecha='2026-11-23',
    titulo='App de controle remoto para TV Sony: celular e PC',
    desc='Use o celular como controle da TV Sony com Google TV ou Android TV pelo Wi-Fi. E, em beta, as Bravia de 2013 a 2015 sem Android.',
    h1='Controle sua TV Sony pelo celular',
    intro='As Smart TVs Sony Bravia mais recentes rodam Google TV e as anteriores rodam Android TV, desde 2015. O Mando TV controla ambas de um iPhone, Android ou PC com Windows pela rede Wi-Fi da casa, funcionando como controle remoto quando o original se perde ou as pilhas acabam.',
    pasos=[
      'Confira se a tela inicial da Sony mostra Google TV ou Android TV. É o caso da maioria das Smart TVs Bravia desde 2015.',
      'Conecte o celular e a TV na mesma rede Wi-Fi.',
      'Abra o Mando TV e toque na sua Sony na lista.',
      'Digite o código de 6 caracteres que aparece na tela da TV (só na primeira vez). Você não precisa do controle para isso.',
      'Use as setas, OK, Voltar, Início, volume e teclado.',
    ],
    extra=[
      ('Ligar a TV Sony pelo celular', 'Modelos com Google TV e Android TV podem ligar pela rede quando o início remoto ("Remote start") está ativado. Geralmente fica em Configurações > Rede e Internet > Início remoto, embora o caminho mude um pouco por modelo. Depois, toque na TV no Mando TV enquanto ela estiver desligada para ligá-la.'),
      ('Onde fica o botão de liga/desliga numa Sony', 'Na maioria das Bravia, fica atrás, perto da borda inferior esquerda ou direita, ou numa lateral. Uma pressão curta liga a TV. Mais detalhes em [Como ligar a TV sem o controle](@turn-on).'),
      ('TVs Sony mais antigas', 'Smart TVs Bravia de 2013 a 2015 que não rodam Android têm suporte em beta no Mando TV. É novo, então pode ter alguns detalhes ainda em ajuste. A TV mostra um PIN de 4 dígitos para digitar no app. Outras Sony sem Google TV ou Android TV não são cobertas hoje.'),
      ('Grátis e Pro', 'O controle é grátis para baixar e usar, sem anúncios nem assinatura. O Mando TV Pro é uma compra única opcional para recursos extras.'),
    ],
    marca='android',
    faq=[
      ('O Mando TV funciona com Smart TVs Sony Bravia?', 'Sim, com TVs que rodam Google TV ou Android TV, o que cobre a maioria das Smart TVs Sony desde 2015.'),
      ('Preciso de app da Sony ou conta Google?', 'Não. O Mando TV pareia pelo código na tela da TV e não pede conta.'),
      ('Funciona com Bravia antigas sem Android?', 'Em beta, sim, em modelos de 2013 a 2015 sem Android. Pareia com um PIN de 4 dígitos mostrado na TV.'),
      ('Dá para digitar na Sony pelo celular?', 'Sim. O teclado do celular é grátis e digita na busca da TV e em outros campos de texto. Para o YouTube, o Mando TV também tem um Teclado do YouTube: digite ou diga o que quer assistir e o YouTube abre na TV com os resultados. A Netflix só aceita o próprio teclado na tela, então use as setas e o OK lá.'),
    ]),
  dict(clave='tcl', corto='Controle remoto TCL', fecha='2026-11-23',
    titulo='Controle remoto TCL no celular: iPhone, Android e PC',
    desc='Perdeu o controle da TCL? A maioria usa Roku TV ou Google TV. Controle sua TCL pelo Wi-Fi com o Mando TV. Grátis, sem conta, sem anúncios.',
    h1='Controle remoto da TV TCL no seu celular',
    intro='A TCL fabrica a TV, mas o sistema é Roku TV ou Google TV (Android TV em modelos mais antigos). O Mando TV controla os dois, então serve de controle remoto da TCL pelo celular ou pelo PC, via Wi-Fi. Grátis, sem conta, sem anúncios.',
    pasos=[
      'Descubra qual sistema sua TCL usa. Se a tela inicial for uma grade simples de canais, é Roku TV. Se parecer o Google TV ou Android TV com linhas de recomendações, é Google TV.',
      'Conecte o celular e a TCL à mesma rede Wi-Fi.',
      'Abra o Mando TV. A TCL aparece sozinha na lista. Toque nela.',
      'Em uma TCL com Roku TV, não precisa de mais nada. Em uma TCL com Google TV, digite o código de 6 caracteres que aparece na tela da TV (só na primeira vez).',
      'Use as setas, OK, Voltar, Início, volume e teclado. Ligue a TV pelo app se você ativou a opção de ligar pela rede (veja abaixo).',
    ],
    extra=[
      ('Ligar a TCL pelo celular', 'Na TCL com Roku TV, ative o início rápido da TV ("Fast TV start") em Configurações > Sistema > Energia. Na TCL com Google TV, procure "Wake on LAN" ou uma opção de ligar pela rede nas configurações de rede ou energia. Alguns modelos não oferecem isso. Nesse caso, ligue a TV pelo botão físico, geralmente no centro inferior ou atrás.'),
      ('Se a sua TCL não aparecer', 'Confira se o celular e a TV estão na mesma rede Wi-Fi. Roteadores com redes separadas de 2,4 GHz e 5 GHz podem esconder dispositivos uns dos outros. No iPhone, permita Rede Local para o Mando TV em Ajustes. Você também pode adicionar a TV digitando o endereço IP dela. Veja [O celular não encontra a TV](@not-found).'),
      ('Mais detalhes para a sua TCL', 'Para uma TCL com Roku TV, veja [app de controle remoto para Roku](@roku). Para uma TCL com Google TV ou Android TV, veja [app de controle remoto para Android TV](@android).'),
      ('Grátis e Pro', 'As setas, OK, Voltar, Início, volume, canais, teclas numéricas, teclado, abrir apps, trocar de entrada e ligar ou desligar são grátis, sem anúncios e sem assinatura. O touchpad, os comandos de voz, os apps favoritos, as rotinas e o timer para desligar fazem parte do Mando TV Pro, uma compra única sem assinatura.'),
    ],
    marca=None,
    faq=[
      ('O Mando TV funciona com todas as TCLs?', 'Funciona com TVs TCL com Roku TV, Google TV ou Android TV, ou seja, a maioria das Smart TVs TCL. Uma TCL que não é Smart TV não pode ser controlada pelo Wi-Fi.'),
      ('Preciso do app da TCL ou de uma conta TCL?', 'Não. O Mando TV se conecta direto pelo seu Wi-Fi e não precisa de nenhuma conta.'),
      ('Minha TCL pede um código. Onde está ele?', 'Os modelos TCL com Google TV e Android TV mostram um código de 6 caracteres na tela da TV. Digite-o no Mando TV exatamente como aparece. A TCL com Roku TV não pede código.'),
    ]),
  dict(clave='hisense', corto='Controle remoto Hisense', fecha='2026-11-23',
    titulo='Controle remoto Hisense no celular: o que funciona',
    desc='Controle sua TV Hisense pelo celular com o Mando TV. Funciona em VIDAA, Roku TV, Google TV e Fire TV via Wi-Fi. Guia honesto do que é possível.',
    h1='Controle remoto Hisense no celular: o que funciona ou não',
    intro='As TVs Hisense não são todas iguais por dentro. Dependendo do modelo, elas rodam o sistema próprio VIDAA da Hisense, Roku TV, Google TV ou Fire TV. O Mando TV funciona como controle remoto da Hisense nos quatro casos, com uma exceção em alguns modelos recentes de VIDAA. Veja como saber qual você tem e o que esperar.',
    pasos=[
      'Confira qual sistema a sua Hisense usa. O VIDAA é a interface própria da Hisense. A Roku TV mostra uma grade de canais. O Google TV exibe linhas de recomendações. O Fire TV mostra a tela inicial do Fire TV com as linhas da Amazon.',
      'Conecte o celular e a TV Hisense à mesma rede Wi-Fi.',
      'Abra o Mando TV. A TV aparece sozinha na lista. Toque nela.',
      'Os modelos VIDAA e Fire TV podem pedir um PIN de 4 dígitos; o Google TV mostra um código de 6 caracteres. Digite no app. A Roku TV não pede nada. Faça isso uma vez.',
      'Use as setas, OK, Voltar, Início, volume e teclado pelo celular.',
    ],
    extra=[
      ('Hisense com Roku TV ou Google TV', 'Essas funcionam totalmente como qualquer outra Roku ou Google TV. Veja [app de controle remoto para Roku](@roku) e [app de controle remoto para Android TV](@android) para os detalhes de cada uma.'),
      ('Hisense com Fire TV', 'O suporte ao Fire TV é novo no Mando TV. Atualize o app para a versão mais recente na sua loja e veja [controle remoto do Fire TV](@firetv) para entender como funciona o pareamento pelo PIN. Se algo não funcionar como esperado, escreva para nós pela página de Ajuda informando seu modelo.'),
      ('Hisense com VIDAA', 'A maioria dos modelos VIDAA funciona: botões, volume, teclado, aplicativos e entradas. Alguns modelos recentes de VIDAA aceitam apenas o app oficial da Hisense. O Mando TV detecta isso ao conectar e avisa claramente, em vez de falhar sem aviso. Nesse caso, use o app Hisense para seu modelo, os botões físicos da TV ou o controle original.'),
      ('Ligar a Hisense pelo celular', 'Na Hisense com Roku TV, ative o início rápido ("Fast TV start") em Configurações > Sistema > Energia. No Google TV, procure "Wake on LAN" ou uma opção de ligar pela rede. Se não existir, use o botão de ligar da própria TV.'),
      ('Grátis e Pro', 'As setas, OK, Voltar, Início, volume, canais, números, teclado, abrir aplicativos, trocar entradas e ligar ou desligar são grátis, sem anúncios nem assinatura. O touchpad, os comandos de voz, os apps favoritos, as rotinas e o timer para desligar fazem parte do Mando TV Pro, uma compra única sem assinatura.'),
    ],
    marca=None,
    faq=[
      ('O Mando TV funciona com Hisense VIDAA?', 'Sim, com a maioria dos modelos VIDAA. Alguns mais recentes só aceitam o app oficial da Hisense; o Mando TV detecta e avisa. TVs Hisense com Roku TV, Google TV ou Fire TV também são compatíveis.'),
      ('Como sei se minha Hisense é Roku TV, Google TV ou Fire TV?', 'Olhe a tela inicial. A Roku TV tem uma grade simples de canais e o logo da Roku ao ligar. O Google TV mostra linhas de recomendações. O Fire TV exibe a tela inicial do Amazon Fire TV. O nome do modelo em Configurações > Sobre também informa.'),
      ('Preciso de conta Hisense ou Google?', 'Não. O Mando TV se conecta direto pelo seu Wi-Fi e não pede nenhuma conta.'),
    ]),
  dict(clave='philips', corto='Controle remoto Philips', fecha='2026-11-23',
    titulo='Controle remoto Philips: Roku TV, Google TV e Android TV',
    desc='O Mando TV controla TVs Philips com Roku TV, Google TV ou Android TV pelo Wi-Fi, do celular ou do PC. E uma nota honesta sobre o Titan OS.',
    h1='Controle remoto da TV Philips no seu celular',
    intro='TVs Philips usam sistemas diferentes conforme o país e o ano: Roku TV nos EUA, Google TV ou Android TV em muitos países, e Titan OS em alguns modelos recentes da Europa. O Mando TV controla os modelos com Roku TV, Google TV e Android TV pelo celular ou PC via Wi-Fi.',
    pasos=[
      'Olhe a tela inicial. A Roku TV mostra uma grade de canais. A Google TV e a Android TV mostram linhas de recomendações do Google. O Titan OS tem sua própria tela inicial.',
      'Conecte o celular e a TV ao mesmo Wi-Fi.',
      'Abra o Mando TV e toque na sua Philips na lista.',
      'Uma Roku TV não pede nada. A Google TV e a Android TV mostram um código de 6 caracteres: digite-o no app uma vez.',
      'Use as setas, OK, Voltar, Início, volume e teclado.',
    ],
    extra=[
      ('Philips com Roku TV', 'Funciona como qualquer Roku TV. Para ligar pelo celular, ative a opção de início rápido da TV ("Fast TV start") em Configurações > Sistema > Energia. Mais detalhes em [app de controle remoto para Roku](@roku).'),
      ('Philips com Google TV ou Android TV', 'Inclui muitos modelos Ambilight. Eles são pareados pelo código na tela. Para ligar pelo celular, procure "Wake on LAN" ou uma opção de ligar pela rede nas configurações de rede ou energia. Alguns modelos não têm essa opção. Mais detalhes em [app de controle remoto para Android TV](@android).'),
      ('TVs Philips mais antigas sem Android', 'TVs Philips de 2011 a 2015 que não rodam Android têm suporte em beta no Mando TV. É novo e não precisa de código de pareamento.'),
      ('Philips com Titan OS', 'O Titan OS é um sistema diferente que o Mando TV não controla hoje, e preferimos dizer isso claramente. Modelos mais novos da Philips sem Android também não são cobertos.'),
      ('Grátis e Pro', 'O controle é grátis para baixar e usar, sem anúncios nem assinatura. O Mando TV Pro é uma compra única opcional para recursos extras.'),
    ],
    marca=None,
    faq=[
      ('O Mando TV funciona com TVs Philips?', 'Com TVs Philips que rodam Roku TV, Google TV ou Android TV, sim, e em beta com as TVs Philips de 2011 a 2015 sem Android. Modelos com Titan OS não são suportados.'),
      ('Controla o Ambilight?', 'O Mando TV é um controle remoto: ele envia os botões, então você pode acessar as configurações do Ambilight com as setas e o OK. Não há controles separados para o Ambilight.'),
      ('Preciso de conta Philips ou Google?', 'Não. O Mando TV se conecta pelo Wi-Fi da sua casa e não pede conta.'),
    ]),
]
OTRAS_GUIAS += [
  ('no-sub', 'App de controle remoto sem assinatura e sem anúncios'),
  ('roku-app-alt', 'Controle Roku pelo celular: alternativa ao app oficial'),
  ('lg-thinq', 'Alternativa ao app LG ThinQ para controlar a sua TV LG'),
  ('smartthings', 'Alternativa ao controle do SmartThings para TVs Samsung'),
  ('googletv-alt', 'Alternativa ao controle do Google TV no seu celular'),
  ('windows', 'App de controle remoto da TV para PC com Windows'),
  ('iphone', 'Controle remoto no iPhone para todas as TVs'),
  ('firetv', 'Controle o Fire TV pelo celular ou PC'),
  ('firetv-lost', 'Controle do Fire TV perdido: use o celular'),
  ('turn-on', 'Como ligar a TV sem o controle original'),
  ('sony', 'Controle sua TV Sony pelo celular'),
  ('tcl', 'Controle remoto da TV TCL no seu celular'),
  ('hisense', 'Controle remoto Hisense no celular: o que funciona ou não'),
  ('philips', 'Controle remoto da TV Philips no seu celular'),
]
# <<< guías traídas del inglés
