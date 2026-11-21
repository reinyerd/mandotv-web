# Textos en portugués de Brasil (pt-BR, "você") de mandotv.app. Los usa generar_idiomas.py. Escritos para las búsquedas de Brasil
# ("controle remoto", "celular", "TV"), no son traducción literal. Las claves y las rutas están en idiomas_sitio.py.
# Los nombres de menús de las TV no se inventan: cuando no hay certeza se describe la opción y se añade entre paréntesis
# el nombre en inglés que muestran las TV.

# Opciones de las TV que se repiten en varios textos.
LG_OPC = 'a opção de ligar a TV com o celular (em inglês, "TV On With Mobile"), que fica em Geral > Dispositivos > Dispositivos externos (nos modelos mais antigos, em Conexão)'
LG_WIFI = 'a ativação via Wi-Fi ("Turn on via Wi-Fi")'
SAM_RUTA = 'Configurações > Geral > Rede > Configurações de especialista (Expert Settings) e ative a opção de ligar com um dispositivo móvel ("Power On with Mobile")'
SAM_PERM = 'Configurações > Geral > Gerenciador de dispositivos externos > Gerenciador de conexão de dispositivos ("Device Connection Manager") e deixe o Mando TV como permitido'
ROKU_APPS = 'Configurações > Sistema > Configurações avançadas do sistema > Controle por aplicativos móveis ("Control by mobile apps")'
ROKU_RAPIDO = 'a opção de início rápido da TV ("Fast TV start") em Configurações > Sistema > Energia'
AND_WOL = '"Wake on LAN" ou uma opção de ligar pela rede'

UI = dict(
  locale='pt_BR',
  aria_home='Mando TV, início', aria_main='Principal', nav_que='Recursos', nav_ayuda='Ajuda', nav_contacto='Contato',
  asunto='Ol%C3%A1%20Mando%20TV', inicio='Início', privacidad='Privacidade', aria_pie='Rodapé', aria_ruta='Caminho',
  aria_marcas='Marcas e guias', hecho='Feito no Chile',
  aviso='O Mando TV é um app independente: não é afiliado aos fabricantes de TV citados nem ao Google, à Amazon ou à Roku, e não tem o apoio deles. As marcas pertencem aos seus donos e são mencionadas apenas para indicar compatibilidade. Android TV e Google TV são marcas do Google LLC.',
  bajar='Baixar grátis', descarga='Baixe na', anticipada='Teste antecipado no',
  apple_aria='Baixar o Mando TV grátis na App Store', ms_aria='Baixar o Mando TV grátis na Microsoft Store',
  gp_aria='Teste antecipado do Mando TV no Google Play para Android', aria_desc='Baixar o Mando TV',
  b_como_btn='Como conectar', b_tiendas_label='Disponível nas lojas',
  b_nota='iPhone, iPad, Android e Windows. Download grátis, sem anúncios. O Pro é uma compra única, sem assinatura.',
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
)

MARCAS = [
  dict(clave='lg', color='#e0457b', corto='LG',
    titulo='Controle remoto LG pelo celular, app grátis | Mando TV',
    desc='Use o celular ou o PC como controle remoto da TV LG webOS, por Wi-Fi. Teclas, teclado, apps, entradas e ligar grátis; ponteiro no Pro.',
    h1='Controle remoto LG: app para o seu celular',
    intro='O Mando TV é um app de controle remoto para TV LG: ele transforma o celular ou o computador, pelo Wi-Fi de casa, no controle da sua Smart TV LG com webOS. Quebra um galho quando você perdeu o controle, as pilhas acabaram ou você só quer digitar mais rápido.',
    compat='Smart TVs LG com webOS (a maioria dos modelos LG Smart TV desde 2014). Funciona em TVs LED, NanoCell, QNED e OLED.',
    h2=dict(funciones='O que você pode fazer com a sua TV LG', como='Como conectar a TV LG ao Mando TV',
            encender='Ligar a TV LG pelo celular', preguntas='Perguntas sobre LG', guias='Guias para LG'),
    funciones=[
      ('Todas as teclas', 'Setas, OK, Voltar, Início, volume, canais, mudo e reprodução.'),
      ('Ponteiro como o Magic Remote (Pro)', 'Mova a seta na tela com o dedo, como no Magic Remote da LG.'),
      ('Teclado', 'Digite no YouTube, na Netflix ou no navegador da TV com o teclado do celular.'),
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
      ('Teclado', 'Digite buscas e senhas com o teclado do celular.'),
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
      ('Teclado', 'Digite suas buscas nos canais da Roku com o teclado do celular.'),
      ('Canais', 'Abra Netflix, YouTube e seus outros canais da Roku com um toque.'),
      ('Entradas', 'Em uma Roku TV, mude para HDMI, antena ou AV pelo app.'),
      ('Ligar a TV', 'Nas Roku TV com início rápido, o Mando TV liga a TV pelo celular.'),
      ('Sem pareamento', 'A Roku não pede código: toque nela na lista e pronto.'),
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
           ('guias', 'Todos os guias para controlar a TV pelo celular')]),
  dict(clave='android', color='#2fbf8f', corto='Android TV e Google TV',
    titulo='Controle remoto Android TV pelo celular | Mando TV',
    desc='Use o celular ou o PC como controle remoto da Android TV (Sony, TCL, Xiaomi), por Wi-Fi. Teclas, apps e ligar grátis; touchpad no Pro.',
    h1='Controle remoto Android TV: app para o seu celular',
    intro='O Mando TV é um app de controle remoto para Android TV: ele transforma o celular ou o computador, pelo Wi-Fi de casa, no controle da sua Android TV ou Google TV. Funciona também a partir de um iPhone e do Windows.',
    compat='TVs com Google TV ou Android TV da Sony, Philips, TCL, Hisense, Sharp, Xiaomi, Toshiba, Panasonic, Haier, Skyworth, JVC, Thomson, Motorola, OnePlus, iFFALCON, Kogan, Vu e outras marcas, além do Chromecast com Google TV, Google TV Streamer, onn. e Nvidia Shield. Algumas dessas marcas também vendem modelos com outro sistema: se a sua TV mostra a tela inicial do Google TV ou tem a loja Google Play, o Mando TV controla.',
    h2=dict(funciones='O que você pode fazer com a sua Android TV', como='Como conectar a Android TV ao Mando TV',
            encender='Ligar a Android TV pelo celular', preguntas='Perguntas sobre Android TV', guias='Guias para Android TV'),
    funciones=[
      ('Todas as teclas', 'Setas, OK, Voltar, Início, volume, mudo e reprodução.'),
      ('Touchpad (Pro)', 'Deslize o dedo para se mover rápido pelos menus do Google TV.'),
      ('Teclado', 'Digite buscas e senhas com o teclado do celular.'),
      ('Apps', 'Abra YouTube, Netflix, Disney+ e seus outros aplicativos com um toque.'),
      ('Ligar a TV', 'Nos modelos que podem ser ligados pela rede, o Mando TV liga a TV e conecta sozinho.'),
      ('iPhone, Android e PC', 'Funciona do mesmo jeito em qualquer celular ou computador.'),
    ],
    pasos=[
      'Conecte o celular e a TV ao mesmo Wi-Fi.',
      'Abra o Mando TV: a sua Android TV aparece sozinha na lista. Toque nela.',
      'A TV mostra um código de 6 caracteres. Digite no Mando TV (só na primeira vez).',
    ],
    encender='Depende do fabricante. Procure nas configurações de rede ou de energia a opção ' + AND_WOL + '. Alguns modelos não têm essa opção. Depois, quando você tocar na TV desligada no Mando TV, o app pergunta se você quer ligá-la e conecta sozinho.',
    faq=[
      ('Funciona com o Chromecast com Google TV?', 'Sim, o pareamento é feito com o código de 6 caracteres que aparece na tela.'),
      ('Qual a diferença para o app Google TV?', 'O Mando TV não precisa de conta Google, funciona também no Windows e controla TVs LG, Samsung e Roku no mesmo app.'),
      ('O código não aparece na tela. O que fazer?', 'Feche o Mando TV, abra o app de novo e toque na TV outra vez. Confirme que a TV não está em um modo de economia de energia profundo.'),
    ],
    guias=[('androidtv-code', 'A Android TV pede um código de pareamento: o que fazer'),
           ('androidtv', 'Android TV sem controle remoto: use o celular'),
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
      ('Funciona se a TV não tiver Wi-Fi?', 'Não. O celular e a TV precisam estar no mesmo Wi-Fi. Uma TV que não seja Smart TV não pode ser controlada com o Mando TV.'),
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
      'Para ligar pelo celular da próxima vez, procure nas configurações de rede ou de energia da TV a opção ' + AND_WOL + '.',
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
      ('Posso digitar com o teclado do celular?', 'Pode. O teclado é grátis e serve para buscar no YouTube, na Netflix e em outros aplicativos.'),
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
      ('Falar com a TV pelo PC (Pro)', 'Com o Mando TV Pro você dá ordens à TV pelo microfone do PC: "abre o YouTube", "aumenta o volume" ou "desliga em 30 minutos", do seu jeito. No Windows o app usa a digitação por voz do Windows, que precisa do "Reconhecimento de fala online" ativado nas configurações de privacidade e do idioma adicionado no Windows (Português (Brasil) ou (Portugal)). Se faltar algo, o app avisa e abre o ajuste com um botão.'),
    ],
    marca=None,
    faq=[
      ('Preciso de cabo ou Bluetooth para controlar a TV pelo PC?', 'Não. O Mando TV conecta pela rede da sua casa: o PC e a TV só precisam estar no mesmo roteador.'),
      ('Funciona com todas as TVs?', 'Funciona com TVs Samsung com Tizen (2016 em diante), LG com webOS, Roku e Google TV ou Android TV (Sony, Philips, TCL, Hisense, Sharp, Xiaomi, Toshiba, Panasonic, Haier, Skyworth e outras).'),
      ('Quanto custa?', 'As teclas, o teclado e o ligar pela rede são grátis e sem anúncios. O Mando TV Pro é uma compra única, sem assinatura, para extras como touchpad, atalhos do teclado do PC e o mini controle.'),
      ('Por que o microfone não me entende no Windows?', 'Confira duas coisas: que o "Reconhecimento de fala online" esteja ativado nas configurações de privacidade do Windows e que o Windows tenha Português (Brasil) ou Português (Portugal) nas configurações de idioma. O Mando TV usa esse idioma só enquanto escuta.'),
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
      ('Onde achar o endereço IP da TV', 'Fica no menu de rede da TV e muda um pouco conforme o modelo. Na LG: Configurações, Rede, Conexão Wi-Fi, configurações avançadas. Na Samsung: Configurações, Geral, Rede, Status da rede, Configurações de IP. Na Roku: Configurações, Rede, Sobre. Na Android TV e no Google TV: Configurações, Rede e internet, e toque na sua rede. É um número como 192.168.1.86.'),
      ('Se aparece mas a conexão cai', 'Quando a conexão cai depois de alguns segundos, a causa costuma estar no celular: uma VPN, a troca para outro Wi-Fi ou o economizador de bateria. Desligue a VPN, fique no mesmo Wi-Fi e tente de novo.'),
      ('Wi-Fi de 2,4 e de 5 GHz', 'Não importa se o celular está na rede de 5 GHz e a TV na de 2,4 GHz, desde que as duas venham do mesmo roteador. Se você tem um repetidor de Wi-Fi e a TV ainda não aparece, aproxime o celular do roteador principal e tente de novo.'),
    ],
    marca=None,
    faq=[
      ('Dá para controlar a TV com dados móveis?', 'Não. O sinal do controle passa pelo Wi-Fi da sua casa, então o celular e a TV precisam estar na mesma rede.'),
      ('Por que não funciona com a VPN ligada?', 'Porque a VPN manda todo o tráfego do celular por outra rede e o celular deixa de ver os aparelhos da sua casa. Desligue enquanto usa o controle.'),
      ('Funciona por Bluetooth ou infravermelho?', 'O Mando TV usa só o Wi-Fi. Não precisa de Bluetooth nem de emissor infravermelho no celular.'),
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
          <p>Depende do fabricante. Procure nas configurações de rede ou de energia a opção ''' + AND_WOL + '''. Alguns modelos não têm.</p>
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
  desc='O Mando TV não coleta dados pessoais: sem conta, sem anúncios e sem rastreadores. O app só fala com a sua TV, dentro do seu Wi-Fi.',
  h1='Privacidade',
  intro='Resumindo: o Mando TV não coleta os seus dados. Não há conta, anúncios, rastreadores nem um servidor nosso que guarde o que você faz.',
)
PRIVACIDAD_HTML = '''      <p class="fecha">Em vigor desde 14 de novembro de 2026. Última atualização: 15 de novembro de 2026.</p>

      <h2>Quem somos</h2>
      <p>O Mando TV é um app para controlar a sua TV pelo celular ou pelo computador. Esta política explica quais informações o app usa e o que faz com elas. Para qualquer dúvida, escreva para <a href="mailto:hola@mandotv.app">hola@mandotv.app</a>.</p>

      <h2>Quais dados coletamos</h2>
      <p>No app: nenhum. O app não envia a nós nem a terceiros nenhuma informação sobre você ou sobre como você o usa. Ele não usa nenhuma ferramenta de análise, publicidade ou rastreamento.</p>
      <p>Neste site: medimos as visitas de duas formas, explicadas na seção <a href="#cookies">Cookies neste site</a>.</p>

      <h2>O que o app guarda no seu aparelho</h2>
      <p>Para funcionar, o app guarda o seguinte apenas no seu celular ou computador:</p>
      <ul>
        <li>As TVs que você adicionou: nome, marca, endereço IP na sua rede e endereço físico da rede (MAC), usado para ligá-la.</li>
        <li>As chaves de conexão que cada TV entrega quando você aceita a permissão. Ficam guardadas criptografadas no armazenamento seguro do sistema (Chaveiro no iPhone e no Mac, Keystore no Android, armazenamento protegido no Windows).</li>
        <li>Suas preferências: tema claro ou escuro, cor de fundo, vibração e tipo de controle.</li>
        <li>Se você usa os recursos Pro: seus aplicativos favoritos, suas rotinas e suas últimas buscas no YouTube (você pode apagá-los pelo app).</li>
      </ul>
      <p>Se você apagar o app, tudo isso é apagado junto.</p>

      <h2>Com quem o app se comunica</h2>
      <p>Com as suas TVs, dentro da rede Wi-Fi da sua casa. Para encontrá-las, o app explora a sua rede local; por isso, no iPhone, ele pede a permissão "Rede Local". O texto que você digita no teclado do app vai direto para a TV e não é guardado.</p>
      <p>Além disso, ao abrir, o app baixa um pequeno arquivo público deste site (mandotv.app/app/config.json) para saber se há uma versão nova para instalar e quais recursos fazem parte do Mando TV Pro. É um download, como abrir uma página: o app não envia os seus dados, as suas TVs nem o que você faz. Só informa a versão do app e o sistema (por exemplo Android), para poder mostrar o aviso certo. Se você estiver sem internet, o app continua funcionando com o último arquivo baixado; se passarem mais de 30 dias sem conseguir baixá-lo, ele pedirá que você se conecte um instante à internet.</p>

      <h2>Microfone e voz</h2>
      <p>A busca por voz só usa o microfone enquanto você toca no botão para falar. O que você diz é convertido em texto pelo reconhecimento de voz do seu sistema: Apple no iPhone e no Mac, Google no Android e Microsoft no Windows, conforme as políticas de privacidade deles. O Mando TV não grava nem guarda o áudio, e o texto obtido vai direto para a sua TV, como o que você digita no teclado.</p>

      <h2>Relatório de teste</h2>
      <p>O app tem um botão "Copiar relatório de teste" para nos ajudar a corrigir erros. O relatório fica só na memória do app enquanto ele está aberto e nunca é enviado sozinho: é você quem decide copiá-lo e compartilhá-lo. Ele não inclui chaves de conexão, códigos de pareamento nem nada do que você digita; apenas os passos que o app seguiu, como a busca, a conexão e os erros.</p>

      <h2 id="cookies">Cookies neste site</h2>
      <p>Isto vale apenas para o site mandotv.app, não para o app.</p>
      <h3>Nunca usamos cookies</h3>
      <p>Contamos as visitas de forma anônima com o Cloudflare Web Analytics: quantas pessoas visitam o site, quais páginas leem e de que país. Ele não usa cookies, não usa o seu endereço IP para identificar você e não acompanha o que você faz em outros sites.</p>
      <h3>Com cookies, só se você aceitar</h3>
      <p>Se você tocar em "Aceitar" no aviso de cookies, ativamos o Google Analytics (do Google LLC) para entender melhor como o site é usado: páginas vistas, tempo na página, tipo de aparelho, cidade aproximada e de onde você veio. Para isso, ele guarda os cookies _ga e _ga_* no seu navegador por até 2 anos. O Google pode processar esses dados em servidores fora do Chile. Desativamos os recursos de publicidade e o Google Signals, e não usamos esses dados para mostrar anúncios a você.</p>
      <p>Se você tocar em "Rejeitar" ou não escolher nada, o Google Analytics não é carregado e nenhum cookie é guardado. Você pode mudar de ideia quando quiser com o botão "Cookies" no rodapé de cada página; se retirar a sua permissão, apagamos esses cookies.</p>
      <p>A sua escolha fica guardada no seu navegador (armazenamento local, que não é enviado a ninguém) para não perguntarmos de novo.</p>

      <h2>Compras</h2>
      <p>Se você comprar o Mando TV Pro, o pagamento é processado pela loja de aplicativos (App Store, Google Play ou Microsoft Store). Nós não recebemos nem guardamos os dados do seu cartão. A loja só confirma ao app que a compra existe.</p>

      <h2>E-mails que você nos envia</h2>
      <p>Se você escrever para <a href="mailto:hola@mandotv.app">hola@mandotv.app</a>, usamos o seu e-mail e o que você nos disser só para responder. Não compartilhamos nem usamos para publicidade. Você pode pedir a qualquer momento que apaguemos as suas mensagens.</p>

      <h2>Crianças</h2>
      <p>O app não coleta dados de ninguém, incluindo crianças.</p>

      <h2>Mudanças nesta política</h2>
      <p>Se um dia o que o app faz com os seus dados mudar, atualizaremos esta página e a data acima antes de a mudança chegar ao app.</p>
'''
