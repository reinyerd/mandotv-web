# Textos en coreano (해요체) de mandotv.app. Los usa generar_idiomas.py. Escritos para las búsquedas de Corea del Sur.
# Las claves de las páginas (lg, lost-tv, ...) y sus rutas están en idiomas_sitio.py.
# Los nombres de menús de cada marca (LG, Samsung, Roku, Android TV, iPhone) son los mismos que usa la app en coreano
# (lib/l10n/app_ko.arb del proyecto de la app).

UI = dict(
  locale='ko_KR',
  aria_home='Mando TV, 홈', aria_main='메인 메뉴', nav_que='기능', nav_ayuda='도움말', nav_contacto='문의',
  asunto='%EC%95%88%EB%85%95%ED%95%98%EC%84%B8%EC%9A%94%20Mando%20TV', inicio='홈', privacidad='개인정보처리방침', aria_pie='페이지 하단', aria_ruta='현재 위치 경로',
  aria_marcas='브랜드와 가이드', hecho='칠레에서 만들었어요',
  aviso='Mando TV는 독립적으로 만든 앱이에요. 언급된 TV 제조사, Google, Amazon, Apple, Roku와는 관련이 없고 이들의 후원이나 보증을 받지 않았어요. 상표는 각 소유자의 것이며 호환 여부를 알려 드리려는 목적으로만 쓰였어요. Android TV와 Google TV는 Google LLC의 상표예요. Apple TV는 Apple Inc.의 상표예요.',
  bajar='무료 다운로드', descarga='다운로드:', anticipada='얼리 액세스:',
  apple_aria='App Store에서 Mando TV 무료로 받기', ms_aria='Microsoft Store에서 Mando TV 무료로 받기',
  gp_aria='Android용 Mando TV를 Google Play 얼리 액세스로 받기', aria_desc='Mando TV 다운로드',
  b_como_btn='연결 방법 보기', b_tiendas_label='스토어에서 받을 수 있어요',
  b_nota='iPhone, iPad, Mac, Android, Windows에서 쓸 수 있어요. 무료로 다운로드하고 광고는 없어요. Pro는 구독 없이 한 번만 결제해요.',
  b_compat='호환되는 TV', b_otras='다른 브랜드', b_otras_p='Mando TV 앱 하나로 아래 브랜드를 모두 조작할 수 있어요.',
  g_guias='가이드', g_ver='방법 보기', g_pasos='단계별로 따라 하기', g_hazlo='Mando TV로 하는 방법',
  g_tiendas='Mando TV는 내 TV를 조작하는 범용 리모컨 앱이에요. 광고도 계정도 없이 무료로 받을 수 있고, Pro는 구독 없이 한 번만 결제하는 선택 기능이에요. iPhone, iPad, Windows, Android에서 받을 수 있어요.',
  g_nota='Android는 Google Play에서 무료 얼리 액세스로 제공해요. <a href="{enlace}">두 단계만 참여해 주시면</a> 정식 출시에 도움이 돼요.',
  g_mas_pagina='자세한 내용은 {enlace} 페이지에서 볼 수 있어요.', g_mas_marca='브랜드별 자세한 내용:',
  g_faq='자주 묻는 질문', g_mas='다른 가이드', g_todas='모든 가이드', g_ayuda='도움말 및 지원',
  g_idiomas='다른 언어로 보는 이 가이드',
)

# Pie de página y listas de marcas/guías: (clave, texto)
PIE = [
  ('samsung', '삼성 TV 리모컨'),
  ('lg', 'LG TV 리모컨'),
  ('roku', 'Roku 리모컨'),
  ('android', 'Android TV 리모컨'),
  ('guias', '모든 가이드'),
  ('lost-tv', 'TV 리모컨을 잃어버렸을 때'),
  ('lost-lg', 'LG 리모컨을 잃어버렸을 때'),
  ('lg-on', '스마트폰으로 LG TV 켜기'),
  ('hdmi', '리모컨 없이 HDMI 입력 바꾸기'),
  ('androidtv', '리모컨 없이 Android TV 쓰기'),
  ('console', '리모컨 없이 TV 켜고 게임기 HDMI로 바꾸기'),
  ('samsung-lost', '리모컨 없는 삼성 TV'),
  ('roku-lost', 'Roku 리모컨을 잃어버렸을 때'),
  ('roku-403', 'Roku 앱이 작동하지 않을 때'),
  ('androidtv-code', 'Android TV 페어링 코드'),
  ('not-found', '스마트폰이 TV를 찾지 못할 때'),
  ('wifi', 'Wi-Fi로 스마트폰을 리모컨으로 쓰기'),
  ('pc', 'PC로 TV 조작하기'),
]
NOMBRE_OTRA = {'lg': 'LG 리모컨 앱', 'samsung': '삼성 리모컨 앱', 'roku': 'Roku 리모컨 앱',
               'android': 'Android TV 및 Google TV 리모컨 앱'}
PAGINA_MARCA = {'lg': 'LG 리모컨 앱', 'samsung': '삼성 리모컨 앱', 'roku': 'Roku 리모컨 앱',
                'android': 'Android TV 리모컨 앱'}

OTRAS_GUIAS = [
  ('lg-on', '스마트폰으로 LG TV 켜기'),
  ('lost-tv', 'TV 리모컨을 잃어버렸을 때 할 수 있는 일'),
  ('lost-lg', 'LG 리모컨을 잃어버렸을 때 스마트폰으로 쓰는 방법'),
  ('hdmi', '리모컨 없이 TV의 HDMI 입력 바꾸기'),
  ('androidtv', '리모컨 없이 Android TV를 스마트폰으로 쓰는 방법'),
  ('console', '리모컨 없이 TV를 켜고 게임기 HDMI로 바꾸기'),
  ('samsung-lost', '삼성 TV 리모컨 없이 스마트폰으로 쓰는 방법'),
  ('roku-lost', 'Roku 리모컨을 잃어버렸을 때 스마트폰으로 쓰는 방법'),
  ('roku-403', 'Roku 앱이 작동하지 않을 때: 403 오류 해결하기'),
  ('androidtv-code', 'Android TV에서 페어링 코드를 물어볼 때 할 일'),
  ('not-found', '스마트폰이 TV를 찾지 못할 때 확인할 것'),
  ('wifi', 'Wi-Fi로 스마트폰을 리모컨으로 쓰는 방법'),
  ('pc', 'Windows PC로 TV 조작하는 방법'),
]

INDICE = dict(
  titulo='가이드: 스마트폰으로 TV 조작하기 | Mando TV',
  desc='스마트폰이나 PC를 리모컨으로 쓰고, TV를 켜고, HDMI를 바꾸고, 삼성·LG·Roku 문제를 해결하는 단계별 가이드예요.',
  h1='가이드: 스마트폰을 리모컨으로 쓰기',
  intro='Mando TV로 삼성, LG, Roku, Android TV 리모컨을 연결하고, TV를 켜고, 문제를 해결하는 쉬운 방법을 모았어요.',
  h2_guias='모든 가이드', h2_marcas='브랜드별 리모컨 앱',
  marcas_extra=[('sony', 'Sony TV 리모컨'), ('philips', 'Philips TV 리모컨')],
)

MARCAS = [
  dict(clave='lg', color='#e0457b', corto='LG',
    titulo='LG TV 리모컨 앱, 스마트폰으로 무료 | Mando TV',
    desc='스마트폰이나 PC를 webOS LG TV 리모컨으로 쓰세요. Wi-Fi로 연결하고, 버튼·키보드·앱·입력·전원 켜기는 무료, 포인터는 Pro예요.',
    h1='스마트폰으로 쓰는 LG TV 리모컨 앱',
    intro='Mando TV는 LG TV용 리모컨 앱이에요. 집 Wi-Fi를 통해 스마트폰이나 컴퓨터를 webOS가 탑재된 LG 스마트 TV의 리모컨으로 바꿔 줘요. 리모컨을 잃어버렸거나 배터리가 다 됐을 때, 아니면 그냥 더 빠르게 입력하고 싶을 때 편해요.',
    compat='webOS가 탑재된 LG 스마트 TV예요(2014년 이후 출시된 대부분의 LG 스마트 TV). LED, 나노셀, QNED, OLED TV에서 모두 쓸 수 있어요. webOS 이전의 NetCast가 탑재된 구형 LG 스마트 TV(2011~2014년)는 베타에서 새로 지원해요. TV 화면에 나오는 6자리 키로 페어링해요.',
    h2=dict(funciones='LG TV로 할 수 있는 일', como='LG TV를 Mando TV에 연결하는 방법',
            encender='스마트폰으로 LG TV 켜기', preguntas='LG 관련 질문', guias='LG 가이드'),
    funciones=[
      ('모든 버튼', '방향키, 확인, 뒤로, 홈, 볼륨, 채널, 음소거, 재생 버튼을 모두 쓸 수 있어요.'),
      ('매직 리모컨 같은 포인터(Pro)', 'LG 매직 리모컨처럼 손가락으로 화면 위의 화살표를 움직여요.'),
      ('키보드', 'YouTube, Netflix, TV 브라우저에서 스마트폰 키보드로 입력해요.'),
      ('앱과 입력', '앱을 열고 HDMI, 라이브 TV, AirPlay, 화면 공유로 바꿔요.'),
      ('오디오 출력(Pro)', 'TV 스피커와 사운드바 사이를 바꿔요.'),
      ('TV 켜기', 'TV가 꺼져 있으면 Mando TV가 네트워크로 켜고 알아서 연결해요.'),
    ],
    pasos=[
      '스마트폰과 TV를 같은 Wi-Fi에 연결하세요.',
      'Mando TV를 열면 목록에 LG TV가 저절로 나타나요. 눌러 주세요.',
      'TV 화면에 허용 여부를 묻는 창이 떠요. 쓰던 리모컨으로 허용해 주세요(처음 한 번만 해요).',
    ],
    encender='LG TV에서 설정을 열고 “모바일 기기로 TV 켜기”를 찾으세요(설정 > 일반 > 기기 > 외부 기기에 있어요. 구형 모델은 연결 > 모바일 연결 관리예요). “Wi-Fi로 켜기”를 활성화하세요. “빠른 시작+”가 있으면 그것도 활성화하세요. 그다음부터는 꺼진 TV를 Mando TV에서 누르면 앱이 켜도 되는지 물어보고, 켠 뒤에 알아서 연결해요.',
    faq=[
      ('Mando TV를 쓰려면 매직 리모컨이 꼭 있어야 하나요?', '처음 한 번만 화면의 허용 창을 확인할 때 필요해요. 그 뒤로는 스마트폰만 있으면 돼요.'),
      ('Mando TV가 LG ThinQ 앱을 대신할 수 있나요?', 'TV를 조작하는 용도라면 대신할 수 있어요. LG 계정도, TV 등록도 필요 없어요. Mando TV는 집 Wi-Fi로 바로 연결해요.'),
      ('스마트폰으로 LG TV를 켤 수 있나요?', '네, TV에서 “모바일 기기로 TV 켜기”를 활성화하고, TV가 켜져 있을 때 한 번 연결해 두면 켤 수 있어요.'),
      ('webOS 이전의 구형 LG TV에서도 쓸 수 있나요?', '베타에서는 2011~2014년의 LG NetCast 스마트 TV를 지원해요. TV 화면에 나오는 6자리 키로 페어링해요. 새로 나온 기능이라서 아직 매끄럽지 않은 부분이 있을 수 있어요.'),
    ],
    guias=[('lg-on', '스마트폰으로 LG TV 켜는 방법'),
           ('lost-lg', 'LG 리모컨을 잃어버렸을 때 스마트폰으로 쓰는 방법'),
           ('hdmi', '리모컨 없이 TV의 HDMI 입력 바꾸기'),
           ('guias', '스마트폰으로 TV를 조작하는 모든 가이드')]),
  dict(clave='samsung', color='#3d7bff', corto='삼성',
    titulo='삼성 TV 리모컨 앱, 스마트폰으로 쓰기 | Mando TV',
    desc='스마트폰이나 PC를 Tizen 삼성 TV 리모컨으로 쓰세요. Wi-Fi로 연결하고, 버튼·키보드·앱·전원 켜기는 무료, 터치패드는 Pro예요. 광고 없어요.',
    h1='스마트폰으로 쓰는 삼성 TV 리모컨 앱',
    intro='Mando TV는 삼성 TV용 리모컨 앱이에요. 집 Wi-Fi를 통해 스마트폰이나 컴퓨터를 삼성 스마트 TV의 리모컨으로 바꿔 줘요. 삼성 계정도, TV 등록도 필요 없어요.',
    compat='Tizen이 탑재된 2016년 이후 출시된 삼성 스마트 TV예요(Crystal UHD, QLED, Neo QLED, The Frame, OLED 같은 시리즈).',
    h2=dict(funciones='삼성 TV로 할 수 있는 일', como='삼성 TV를 Mando TV에 연결하는 방법',
            encender='스마트폰으로 삼성 TV 켜기', preguntas='삼성 관련 질문', guias='삼성 가이드'),
    funciones=[
      ('모든 버튼', '방향키, 확인, 뒤로, 홈, 볼륨, 채널, 음소거, 소스 버튼을 모두 쓸 수 있어요.'),
      ('터치패드(Pro)', '방향키를 찾을 필요 없이 손가락으로 메뉴 위를 쓸어 넘겨요.'),
      ('키보드', '스마트폰 키보드로 검색어와 비밀번호를 입력해요.'),
      ('앱', 'Netflix, YouTube, Prime Video 같은 앱을 한 번 눌러서 열어요.'),
      ('TV 켜기', 'TV가 꺼져 있으면 Mando TV가 네트워크로 켜고 알아서 연결해요.'),
      ('계정 없이', '인터넷을 거치지 않고 집 Wi-Fi로 바로 연결해요.'),
    ],
    pasos=[
      '스마트폰과 TV를 같은 Wi-Fi에 연결하세요.',
      'Mando TV를 열면 목록에 삼성 TV가 저절로 나타나요. 눌러 주세요.',
      'TV가 연결을 허용할지 물어봐요. 리모컨으로 “허용”을 선택하세요(처음 한 번만 해요).',
    ],
    encender='삼성 TV에서 설정 > 일반 > 네트워크 > 전문가 설정으로 들어가 “모바일 기기로 켜기”를 활성화하세요. 그다음부터는 꺼진 TV를 Mando TV에서 누르면 앱이 켜도 되는지 물어보고, 켠 뒤에 알아서 연결해요.',
    faq=[
      ('실수로 허용을 거부했어요. 어떻게 하나요?', 'TV에서 설정 > 일반 > 외부 장치 관리자 > 장치 연결 관리자로 들어가 Mando TV를 허용으로 바꾸세요.'),
      ('Mando TV가 SmartThings를 대신할 수 있나요?', 'TV를 조작하는 용도라면 대신할 수 있고, 삼성 계정도 필요 없어요. Mando TV는 집 Wi-Fi로 바로 연결해요.'),
      ('구형 삼성 TV에서도 쓸 수 있나요?', 'Tizen이 탑재된 2016년 이후의 삼성 TV에서 쓸 수 있어요. 그 이전 모델은 아직 지원하지 않는 다른 시스템을 써요.'),
    ],
    guias=[('samsung-lost', '삼성 TV 리모컨 없이 스마트폰으로 쓰는 방법'),
           ('smartthings', '삼성 TV를 위한 SmartThings 대안'),
           ('turn-on', '리모컨 없이 TV 켜는 방법'),
           ('hdmi', '리모컨 없이 TV의 HDMI 입력 바꾸기'),
           ('guias', '스마트폰으로 TV를 조작하는 모든 가이드')]),
  dict(clave='roku', color='#a77bff', corto='Roku',
    titulo='Roku 리모컨 앱, 스마트폰으로 무료 | Mando TV',
    desc='스마트폰이나 PC를 Roku TV와 Roku 플레이어의 리모컨으로 쓰세요. Wi-Fi로 연결하고, 버튼·키보드·채널·입력·전원 켜기는 무료예요.',
    h1='스마트폰으로 쓰는 Roku 리모컨 앱',
    intro='Mando TV는 Roku용 리모컨 앱이에요. 집 Wi-Fi를 통해 스마트폰이나 컴퓨터를 Roku의 리모컨으로 바꿔 줘요. Roku TV 기기와 HDMI 포트에 꽂는 Roku 플레이어에서 모두 쓸 수 있어요.',
    compat='Roku TV 기기(TCL, Hisense, Philips, Sharp, JVC 등)와 Roku 플레이어(Express, Streaming Stick, Ultra)예요.',
    h2=dict(funciones='Roku로 할 수 있는 일', como='Roku를 Mando TV에 연결하는 방법',
            encender='스마트폰으로 Roku 켜기', preguntas='Roku 관련 질문', guias='Roku 가이드'),
    funciones=[
      ('모든 버튼', '방향키, 확인, 뒤로, 홈, 볼륨, 음소거, 다시 보기, 재생 버튼을 모두 쓸 수 있어요.'),
      ('키보드', 'Roku 채널에서 스마트폰 키보드로 검색어를 입력해요.'),
      ('채널', 'Netflix, YouTube 같은 Roku 채널을 한 번 눌러서 열어요.'),
      ('입력', 'Roku TV라면 앱에서 HDMI, 안테나, AV로 바꿔요.'),
      ('TV 켜기', '빠른 시작이 있는 Roku TV 기기는 Mando TV가 스마트폰으로 켜 줘요.'),
      ('페어링 없이', 'Roku는 코드를 묻지 않아요. 목록에서 눌러 주기만 하면 연결돼요.'),
      ('리모컨 소리 울리기', 'Roku Voice Remote Pro처럼 스피커가 있는 Roku 리모컨이라면 Mando TV가 소리를 울려서 찾게 도와줘요. 무료이고, Roku가 켜져 있어야 해요.'),
    ],
    pasos=[
      '스마트폰과 Roku를 같은 Wi-Fi에 연결하세요.',
      'Mando TV를 열면 목록에 Roku가 저절로 나타나요. 눌러 주세요.',
      '연결되지 않으면 Roku에서 설정 > 시스템 > 고급 시스템 설정 > 모바일 앱으로 제어로 들어가 네트워크 액세스를 기본 또는 Permissive로 바꾸세요(최신 Roku 소프트웨어에서는 “모바일 앱으로 제어”를 활성화로 설정하세요).',
    ],
    encender='Roku TV 기기라면 설정 > 시스템 > 전원에서 “TV 빠른 시작”을 활성화하세요. 다른 TV에 꽂아 쓰는 Roku 플레이어는 이 방법으로 켤 수 없어요. 그다음부터는 꺼진 TV를 Mando TV에서 누르면 앱이 켜도 되는지 물어보고, 켠 뒤에 알아서 연결해요.',
    faq=[
      ('Roku Express나 Streaming Stick에서도 쓸 수 있나요?', '네. 모든 Roku 플레이어와 Roku TV 기기를 같은 방식으로 조작해요.'),
      ('Mando TV가 Roku를 찾지 못해요. 어떻게 하나요?', '둘이 같은 Wi-Fi에 있는지, Roku에서 “모바일 앱으로 제어”가 꺼져 있지 않은지 확인하세요. IP 주소로 직접 추가할 수도 있어요.'),
      ('Roku 계정이 필요한가요?', '아니요. Mando TV는 집 Wi-Fi로 바로 연결해요.'),
    ],
    guias=[('roku-403', 'Roku 앱이 작동하지 않을 때(403 오류)'),
           ('roku-lost', 'Roku 리모컨을 잃어버렸을 때 스마트폰으로 쓰는 방법'),
           ('tcl', 'TCL TV 리모컨'),
           ('hisense', 'Hisense TV 리모컨'),
           ('philips', 'Philips TV 리모컨'),
           ('guias', '스마트폰으로 TV를 조작하는 모든 가이드')]),
  dict(clave='android', color='#2fbf8f', corto='Android TV 및 Google TV',
    titulo='Google TV 및 Android TV 리모컨 앱 | Mando TV',
    desc='스마트폰이나 PC를 Google TV, Android TV(Sony, TCL, Hisense, Xiaomi) 리모컨으로 쓰세요. Wi-Fi로 연결, 버튼·키보드·앱·전원 켜기는 무료, 터치패드는 Pro예요.',
    h1='스마트폰으로 쓰는 Google TV 및 Android TV 리모컨 앱',
    intro='Mando TV는 Android TV용 리모컨 앱이에요. 집 Wi-Fi를 통해 스마트폰이나 컴퓨터를 Android TV 또는 Google TV의 리모컨으로 바꿔 줘요. iPhone과 Windows에서도 쓸 수 있어요.',
    compat='Sony, Philips, TCL, Hisense, Sharp, Xiaomi, Toshiba, Panasonic, Haier, Skyworth, JVC, Thomson, Motorola, OnePlus, iFFALCON, Kogan, Vu 등의 Google TV 또는 Android TV 탑재 TV와 Google TV가 탑재된 Chromecast, Google TV Streamer, onn., Nvidia Shield예요. 이 브랜드 중에는 다른 시스템의 모델도 파는 곳이 있어요. TV에 Google TV 홈 화면이 나오거나 Google Play 스토어가 있으면 Mando TV로 조작할 수 있어요.',
    h2=dict(funciones='Android TV로 할 수 있는 일', como='Android TV를 Mando TV에 연결하는 방법',
            encender='스마트폰으로 Android TV 켜기', preguntas='Android TV 관련 질문', guias='Android TV 가이드'),
    funciones=[
      ('모든 버튼', '방향키, 확인, 뒤로, 홈, 볼륨, 음소거, 재생 버튼을 모두 쓸 수 있어요.'),
      ('터치패드(Pro)', '손가락을 쓸어서 Google TV 메뉴를 빠르게 넘겨요.'),
      ('키보드', '스마트폰 키보드로 검색어와 비밀번호를 입력해요.'),
      ('앱', 'YouTube, Netflix, Disney+ 같은 앱을 한 번 눌러서 열어요.'),
      ('TV 켜기', '네트워크로 켜기를 지원하는 모델이라면 Mando TV가 TV를 켜고 알아서 연결해요.'),
      ('iPhone, Android, PC', '어떤 스마트폰, 어떤 컴퓨터에서든 똑같이 쓸 수 있어요.'),
    ],
    pasos=[
      '스마트폰과 TV를 같은 Wi-Fi에 연결하세요.',
      'Mando TV를 열면 목록에 Android TV가 저절로 나타나요. 눌러 주세요.',
      'TV 화면에 6자리 코드가 나와요. Mando TV에 입력해 주세요(처음 한 번만 해요).',
    ],
    encender='제조사마다 달라요. 네트워크나 전원 설정에서 “Wake on LAN”, “네트워크로 켜기”, “네트워크 대기 모드”, “Remote start”를 찾아보세요. 이 옵션이 없는 모델도 있어요. 그다음부터는 꺼진 TV를 Mando TV에서 누르면 앱이 켜도 되는지 물어보고, 켠 뒤에 알아서 연결해요.',
    faq=[
      ('Google TV가 탑재된 Chromecast에서도 쓸 수 있나요?', '네, 화면에 나오는 6자리 코드로 페어링해요.'),
      ('Google TV 앱과 무엇이 다른가요?', 'Mando TV는 Google 계정이 필요 없고, Windows에서도 쓸 수 있고, 앱 하나로 LG, 삼성, Roku TV까지 조작해요.'),
      ('코드가 화면에 나오지 않아요. 어떻게 하나요?', 'Mando TV를 닫았다가 다시 열고, TV를 한 번 더 눌러 보세요. TV가 깊은 절전 모드에 있지 않은지도 확인하세요.'),
    ],
    guias=[('androidtv-code', 'Android TV에서 페어링 코드를 물어볼 때 할 일'),
           ('androidtv', '리모컨 없이 Android TV를 스마트폰으로 쓰는 방법'),
           ('googletv-alt', '스마트폰용 Google TV 리모컨 대안'),
           ('sony', 'Sony TV 리모컨'),
           ('tcl', 'TCL TV 리모컨'),
           ('hisense', 'Hisense TV 리모컨'),
           ('philips', 'Philips TV 리모컨'),
           ('guias', '스마트폰으로 TV를 조작하는 모든 가이드')]),
]

GUIAS = [
  dict(clave='lost-tv', corto='TV 리모컨 분실',
    titulo='TV 리모컨을 잃어버렸나요? 스마트폰으로 TV 조작하기',
    desc='TV 리모컨을 잃어버렸나요? TV 본체 버튼으로 켜고 스마트폰을 리모컨으로 쓰세요. LG, 삼성, Roku, Android TV 방법을 알려 드려요. 무료예요.',
    h1='TV 리모컨을 잃어버렸을 때 지금 할 수 있는 일',
    intro='리모컨을 잃어버리는 일은 어느 집에서나 있어요. 꼭 TV를 보려는 순간에 사라지죠. 다행히 스마트폰이 집 Wi-Fi를 통해 리모컨을 대신할 수 있어요. 순서대로 따라 해 보세요.',
    pasos=[
      'TV 본체의 버튼으로 TV를 켜세요. 버튼은 대개 아래쪽 가운데나 뒷면 모서리 근처에 있어요. 버튼이 하나일 때도 있고 작은 조이스틱일 때도 있어요.',
      '스마트폰을 TV와 같은 Wi-Fi에 연결하세요.',
      '무료이고 계정이 필요 없는 Mando TV를 받아서 열어 보세요. 목록에 TV가 저절로 나타나요. 눌러 주세요.',
      '브랜드에 맞게 연결을 확인하세요. LG와 삼성은 TV에 허용 여부를 묻는 창이 떠요. TV 본체의 버튼이나 조이스틱으로 허용해 주세요. Android TV와 Google TV는 화면에 나오는 6자리 코드를 입력하세요. Roku는 아무것도 묻지 않아요.',
      '끝났어요. 방향키, 확인, 뒤로, 홈, 볼륨, 채널, 키보드는 무료예요.',
      '다음을 위해 TV 설정에서 네트워크로 켜기를 활성화해 두세요(아래에서 내 브랜드 가이드를 찾아보세요). 그러면 TV에 손대지 않고 스마트폰으로 켤 수 있어요.',
    ],
    extra=[
      ('내 브랜드 가이드 고르기', 'LG는 [LG 리모컨을 잃어버렸을 때](@lost-lg), Android TV와 Google TV는 [리모컨 없이 Android TV 쓰기](@androidtv), 삼성은 [리모컨 없는 삼성 TV](@samsung-lost), Roku는 [Roku 리모컨을 잃어버렸을 때](@roku-lost)를 보세요.'),
      ('TV 버튼으로도 TV가 켜지지 않을 때', '다른 리모컨을 찾기 전에 전원 코드가 제대로 꽂혀 있는지, 콘센트에 전기가 들어오는지 확인하세요. TV 본체 버튼을 눌러도 반응이 없다면 리모컨이 아니라 TV의 문제예요.'),
      ('리모컨이 그냥 작동하지 않을 때', '새 배터리로 바꿔 보세요. 리모컨이 아직 신호를 보내는지 알아보려면 스마트폰 카메라로 리모컨을 비추고 버튼을 눌러 보세요. 많은 스마트폰에서 화면에 보라색 빛이 보여요. 빛이 보이는데 TV가 반응하지 않는다면 TV의 센서가 가려져 있을 수 있어요.'),
      ('공유기를 바꿔서 TV가 Wi-Fi에 연결되지 않을 때', '리모컨이 없으면 TV를 새 네트워크에 연결하기가 더 어려워요. 가장 쉬운 방법은 TV를 랜선으로 공유기에 직접 연결하는 거예요. 이전과 같은 이름과 비밀번호로 Wi-Fi를 만들어도 돼요. TV가 대개 저절로 연결돼요.'),
      ('무료와 Pro의 차이', 'TV 켜기와 끄기, 방향키, 확인, 볼륨, 채널, 숫자 버튼, 키보드, 앱 열기, 입력 바꾸기는 무료예요. 터치패드, 음성, 루틴은 구독 없이 한 번만 결제하는 Mando TV Pro에 포함돼요.'),
    ],
    marca=None,
    faq=[
      ('한 번도 연결한 적이 없어도 스마트폰으로 TV를 켤 수 있나요?', '처음에는 TV 본체의 버튼으로 켜세요. 스마트폰을 연결하고 TV 설정에서 네트워크로 켜기를 활성화해 두면 그다음부터는 앱으로 켤 수 있어요.'),
      ('새 리모컨을 사야 하나요?', '꼭 그렇지는 않아요. Mando TV로 버튼, 볼륨, 키보드, 전원 켜기를 무료로 쓸 수 있어요. 그래도 실물 리모컨이 좋다면 TV의 정확한 모델명으로 찾아보세요.'),
      ('TV가 Wi-Fi에 연결되어 있지 않아도 되나요?', '대부분은 안 돼요. 스마트폰과 TV는 보통 같은 Wi-Fi에 있어야 해요. 예외는 적외선 송신기가 있는 Android 스마트폰의 적외선으로, 스마트 TV가 아닌 TV도 조작할 수 있어요. 그리고 Android 9 이상의 Bluetooth 베타로, Wi-Fi 없이 Google TV, Android TV, Fire TV와 연결할 수 있어요.'),
    ]),
  dict(clave='lost-lg', corto='LG 리모컨 분실',
    titulo='LG 리모컨을 잃어버렸나요? 스마트폰으로 쓰세요',
    desc='LG 리모컨이 없나요? TV 본체 버튼으로 켜고, 허용 창을 확인한 뒤 스마트폰을 Wi-Fi 리모컨으로 쓰세요. LG 계정도 광고도 없어요.',
    h1='LG 리모컨을 잃어버렸을 때 스마트폰으로 쓰는 방법',
    intro='LG 리모컨을 잃어버렸거나 매직 리모컨이 더 이상 작동하지 않으면 스마트폰이 Wi-Fi로 대신해 줘요. webOS가 탑재된 LG TV, 즉 2014년 이후 나온 거의 모든 LG 스마트 TV에서 쓸 수 있어요. LG 계정도 ThinQ 앱도 필요 없어요.',
    pasos=[
      'LG 로고 아래쪽에 있는 버튼이나 뒷면의 버튼으로 TV를 켜세요. 많은 모델에서 이 버튼은 조이스틱이에요. 눌러서 메뉴를 열고, 움직여서 항목을 선택해요.',
      '스마트폰을 TV와 같은 Wi-Fi에 연결하세요.',
      'Mando TV를 열고 목록에서 LG TV를 눌러 주세요.',
      'TV에 허용 여부를 묻는 창이 떠요. TV 본체의 조이스틱이나 버튼으로 허용해 주세요. 이 스마트폰을 이미 한 번 연결했다면 다시 묻지 않아요.',
      '끝났어요. 방향키, 확인, 뒤로, 홈, 볼륨, 채널, 키보드는 무료예요. 포인터는 Pro 기능이에요.',
      '앱이 연결된 상태에서 방향키와 확인으로 설정을 열고 “모바일 기기로 TV 켜기”를 활성화하세요. [스마트폰으로 LG TV 켜기](@lg-on) 가이드에서 이 옵션이 어디 있는지 알려 드려요.',
    ],
    extra=[
      ('TV에 허용 창이 뜨지 않을 때', '이미 허용이 저장되어 있거나 스마트폰이 다른 네트워크에 있을 수 있어요. 둘이 같은 Wi-Fi에 있는지, VPN이 꺼져 있는지 확인하세요. 목록에 TV가 나타나지 않으면 [스마트폰이 TV를 찾지 못할 때](@not-found)를 보세요.'),
      ('TV의 Wi-Fi 연결이 끊어졌을 때', 'TV를 랜선으로 공유기에 직접 연결하면 저절로 그 연결을 써요. 이전과 같은 이름과 비밀번호로 Wi-Fi를 만들어도 돼요. TV가 대개 저절로 연결돼요.'),
      ('TV가 다른 입력에 머물러 있을 때', '스마트폰에서 입력을 누르고 HDMI 포트를 선택하세요. 자세한 내용은 [리모컨 없이 TV의 HDMI 입력 바꾸기](@hdmi)에 있어요.'),
    ],
    marca='lg',
    faq=[
      ('Mando TV를 쓰려면 매직 리모컨이 꼭 있어야 하나요?', '처음 한 번만 허용 창을 확인하기 위한 무언가가 필요하고, 그건 TV 본체의 버튼이나 조이스틱이면 돼요. 그 뒤로는 스마트폰만 써요.'),
      ('LG ThinQ 앱이 필요한가요?', '아니요. Mando TV는 집 Wi-Fi로 바로 연결하고 LG 계정을 요구하지 않아요.'),
      ('스마트폰으로 LG TV를 켜고 끌 수 있나요?', '끄기는 돼요. 켜려면 TV에서 “모바일 기기로 TV 켜기”를 활성화하고, TV가 켜져 있을 때 한 번 연결해 두어야 해요.'),
    ]),
  dict(clave='hdmi', corto='리모컨 없이 HDMI 바꾸기',
    titulo='리모컨 없이 HDMI 입력 바꾸기 (삼성, LG, Roku)',
    desc='삼성, LG, Roku에서 리모컨 없이 HDMI 입력 바꾸기: TV 본체 버튼이나 스마트폰으로 바꿔요. 시작은 무료이고 광고는 없어요.',
    h1='리모컨 없이 TV의 HDMI 입력 바꾸는 방법',
    intro='게임기나 스트리밍 플레이어는 준비됐는데 TV가 다른 입력에 머물러 있고 리모컨은 어디에도 없어요. 리모컨 없이 HDMI 입력을 바꾸는 방법은 두 가지예요. TV 본체의 버튼을 쓰거나 스마트폰을 쓰는 거예요. 삼성, LG, Roku별로 단계를 알려 드려요.',
    pasos=[
      '먼저 가장 쉬운 방법부터 해 보세요. 게임기나 플레이어를 켜세요. TV에서 HDMI-CEC가 활성화되어 있으면(삼성은 Anynet+, LG는 SIMPLINK라고 불러요) TV가 저절로 그 입력으로 바뀌어요.',
      '바뀌지 않으면 TV 본체의 버튼을 쓰세요. 아래쪽 가운데나 뒷면에 있어요. 많은 삼성과 LG TV에서는 조이스틱이고, 소스나 입력 항목이 있는 메뉴가 열려요.',
      '이 메뉴에서 입력을 고르세요. HDMI 1, HDMI 2 등이에요. 번호는 케이블이 꽂혀 있는 포트예요.',
      '스마트폰이 편하다면 같은 Wi-Fi에 연결하고 Mando TV를 열어 TV를 눌러 주세요.',
      'LG와 Roku는 입력을 누르고 HDMI 포트를 선택하세요. 삼성은 입력이 소스 버튼을 TV에 보내고, 방향키와 확인으로 선택해요.',
      '방향키와 확인으로 TV 홈 화면에서 입력으로 갈 수도 있어요. 브랜드와 출시 연도에 따라 소스, 연결된 기기, 입력이라고 불러요. Roku TV에서는 홈 화면의 HDMI 타일이에요.',
    ],
    extra=[
      ('삼성', 'TV 본체 버튼 메뉴에 소스 항목이 없다면 스마트폰으로 홈 화면 메뉴를 열고 왼쪽에서 소스나 연결된 기기를 찾으세요. 무료인 Mando TV의 방향키와 확인으로 조작해요.'),
      ('LG', 'TV의 조이스틱을 누르고 입력을 찾으세요. 스마트폰에서는 Mando TV의 입력 목록을 열어 원하는 입력을 눌러도 돼요.'),
      ('Roku TV', '홈 화면에 입력마다 타일이 있어요. 예를 들어 HDMI 1이나 HDMI 2예요. 방향키로 이동해서 확인으로 열어요. 무료예요.'),
      ('Android TV나 Google TV일 때', 'Mando TV에는 아직 Android TV용 입력 목록이 없어요. TV 본체의 입력 버튼을 쓰거나, 홈 화면에서 방향키와 확인으로 입력에 들어가세요. 리모컨 없이 연결하고 싶다면 [리모컨 없이 Android TV 쓰기](@androidtv)를 읽어 보세요.'),
      ('더 많은 도움', 'TV가 전혀 켜지지 않거나 어디서부터 해야 할지 모르겠다면 [TV 리모컨을 잃어버렸을 때](@lost-tv)를 읽어 보세요. 게임기로 게임을 한다면 [리모컨 없이 TV를 켜고 게임기 HDMI로 바꾸기](@console) 가이드에 HDMI-CEC 요령이 있어요.'),
    ],
    marca=None,
    faq=[
      ('HDMI 입력을 바꾸는 건 무료인가요?', '네. Mando TV의 입력 목록은 TV 켜기, 방향키, 확인, 볼륨처럼 무료예요. TV 메뉴로도 입력에 들어갈 수 있어요.'),
      ('어떤 HDMI 입력을 써야 하는지 어떻게 알아요?', 'TV의 HDMI 포트를 보세요. 포트마다 번호가 있어요. 게임기나 플레이어의 케이블이 꽂힌 포트의 번호를 고르세요.'),
      ('TV가 켜지지 않으면 어떻게 하나요?', 'TV 본체의 버튼으로 켜세요. 이미 한 번 연결해서 네트워크로 켜기를 활성화해 두었다면 스마트폰으로도 켤 수 있어요.'),
    ]),
  dict(clave='androidtv', corto='리모컨 없이 Android TV',
    titulo='리모컨 없는 Android TV: 스마트폰으로 쓰세요',
    desc='Android TV나 Google TV 리모컨이 없나요? 화면의 6자리 코드로 스마트폰을 연결하세요. 무료, 계정 없음, 광고 없음.',
    h1='리모컨 없이 Android TV를 스마트폰으로 쓰는 방법',
    intro='Android TV나 Google TV 리모컨을 잃어버렸거나 배터리가 다 됐다면 스마트폰이 대신해 줘요. 가장 좋은 점은 연결에 리모컨이 필요 없다는 거예요. TV 화면에 코드가 나오고 그 코드를 스마트폰에 입력하면 돼요. Android TV가 탑재된 Sony, Philips, TCL, Hisense, Sharp, Xiaomi TV와 Google TV가 탑재된 Chromecast, Nvidia Shield에서 쓸 수 있어요.',
    pasos=[
      'TV 본체의 버튼으로 TV를 켜세요. 버튼은 대개 아래쪽 가운데나 뒷면 모서리 근처에 있어요.',
      '스마트폰을 TV와 같은 Wi-Fi에 연결하세요.',
      '무료이고 Google 계정이 필요 없는 Mando TV를 받아서 열어 보세요. 목록에서 TV를 눌러 주세요.',
      'TV에 영문자와 숫자로 된 6자리 코드가 나와요. 스마트폰에 입력하고 페어링을 누르세요. 리모컨은 필요 없어요.',
      '이제 방향키, 확인, 뒤로, 홈, 볼륨, 음소거, 키보드를 쓸 수 있어요. 모두 무료이고 앱 목록도 무료예요. 터치패드는 Pro예요.',
      '다음에 스마트폰으로 TV를 켜려면 네트워크나 전원 설정에서 “Wake on LAN”, “네트워크로 켜기”, “네트워크 대기 모드”, “Remote start”를 찾아보세요.',
    ],
    extra=[
      ('스마트폰으로 TV가 켜지지 않을 때', '모든 Android TV가 네트워크로 켜지는 건 아니에요. 제조사와 모델에 따라 달라요. 내 TV에 이 기능이 없다면 TV 본체의 버튼으로 켜고 스마트폰으로 이어서 쓰세요. 끄는 건 앱으로 할 수 있어요.'),
      ('Google TV가 탑재된 Chromecast, Google TV Streamer, Shield', '같은 방식으로 연결해요. 같은 Wi-Fi에서 목록의 기기를 누르고 코드를 입력하세요. TV가 다른 입력을 보여 주고 있다면 [리모컨 없이 TV의 HDMI 입력 바꾸기](@hdmi)처럼 기기가 꽂힌 HDMI 포트로 바꾸세요.'),
      ('코드가 나오지 않거나 틀렸다고 나올 때', 'TV가 대기 상태가 아니라 정말 켜져 있는지 확인하세요. 코드는 요청할 때마다 바뀌고 가장 마지막 코드만 유효해요. 자세한 내용은 [Android TV에서 페어링 코드를 물어볼 때](@androidtv-code)에 있어요.'),
      ('Google 앱과 Mando TV', 'Google에는 Google 계정이 필요한 자체 앱이 있어요. Mando TV는 계정이 필요 없고, Windows에서도 쓸 수 있고, 앱 하나로 LG, 삼성, Roku TV까지 조작해요.'),
    ],
    marca='android',
    faq=[
      ('스마트폰을 페어링하려면 리모컨이 필요한가요?', '아니요. 코드가 TV 화면에 나오고 스마트폰에 입력하면 돼요. TV만 켜 두면 되고, 필요하면 TV 본체의 버튼으로 켜세요.'),
      ('Hisense에서도 쓸 수 있나요?', 'Android TV나 Google TV가 탑재된 Hisense TV라면 쓸 수 있어요. 다른 시스템의 Hisense TV는 호환되지 않아요.'),
      ('스마트폰 키보드로 입력할 수 있나요?', '네. 키보드는 무료이고 YouTube, Netflix 등 다른 앱의 검색에서 쓸 수 있어요.'),
    ]),
  dict(clave='lg-on', corto='스마트폰으로 LG TV 켜기',
    titulo='스마트폰으로 LG TV 켜기 (설정 방법)',
    desc='Wi-Fi로 스마트폰에서 LG TV를 켜세요. “모바일 기기로 TV 켜기”를 활성화하고 Mando TV를 쓰면 돼요. 단계별 안내, 무료.',
    h1='스마트폰으로 LG TV 켜는 방법',
    intro='스마트폰으로 LG TV를 켤 수 있어요. 다만 먼저 TV에서 설정 하나를 활성화해야 해요. 그다음부터는 리모컨 없이 스마트폰이 Wi-Fi로 LG TV를 켜 줘요. 5분이면 되고 한 번만 하면 돼요.',
    pasos=[
      '스마트폰과 LG TV를 같은 Wi-Fi에 연결하세요.',
      'TV에서 설정을 열고 “모바일 기기로 TV 켜기”를 찾으세요. 설정 > 일반 > 기기 > 외부 기기에 있어요(구형 모델은 연결 > 모바일 연결 관리).',
      '“Wi-Fi로 켜기”를 활성화하세요. TV가 랜선으로 연결되어 있다면 랜선용 옵션을 활성화하세요.',
      'TV에 “빠른 시작+”가 있으면 그것도 활성화하세요.',
      'TV가 켜져 있을 때 스마트폰에서 Mando TV를 열고 목록의 LG TV를 누르세요. 화면에 뜨는 허용 창을 확인해 주세요. 이렇게 하면 앱이 TV를 깨우는 방법을 배워요.',
      'TV를 끄고 시험해 보세요. Mando TV에서 TV를 누르면 앱이 켜도 되는지 물어봐요.',
    ],
    extra=[
      ('켜지지 않을 때', 'TV가 꺼질 때 같은 Wi-Fi에 있었어야 해요. 설정이 아직 활성화되어 있는지, 스마트폰이 같은 네트워크에 있는지 확인하세요. 공유기를 바꿨다면 TV를 켠 상태에서 다시 연결하세요.'),
    ],
    marca='lg',
    faq=[
      ('한 번도 연결하지 않았어도 스마트폰으로 LG TV를 켤 수 있나요?', '아니요. 먼저 TV에서 “모바일 기기로 TV 켜기”를 활성화하고, TV가 켜져 있을 때 Mando TV로 한 번 연결해야 해요.'),
      ('LG ThinQ 앱이 필요한가요?', '아니요. Mando TV는 집 Wi-Fi로 바로 연결하고 LG 계정을 요구하지 않아요.'),
      ('모바일 데이터로도 되나요?', '아니요. 스마트폰과 TV가 같은 Wi-Fi에 있어야 해요.'),
    ]),
  dict(clave='console', corto='리모컨 없이 TV와 게임기',
    titulo='리모컨이 없나요? TV 켜고 HDMI 바꾸기',
    desc='출시일인데 리모컨이 없나요? 스마트폰으로 TV를 켜고 PS5나 Xbox의 HDMI 입력으로 바꾸세요. 무료, 광고 없음.',
    h1='리모컨 없이 TV를 켜고 게임기 HDMI 입력으로 바꾸는 방법',
    intro='GTA VI 출시일이에요. 게임기는 준비됐는데 리모컨이 소파 쿠션 사이 어딘가로 사라졌어요. 생각보다 자주 있는 일이에요. Mando TV를 쓰면 스마트폰이 집 Wi-Fi로 TV를 켜고 PlayStation이나 Xbox의 입력으로 바꿔 줘요.',
    pasos=[
      '스마트폰을 TV와 같은 Wi-Fi에 연결하세요.',
      'Mando TV를 열고 목록에서 TV(삼성, LG, Roku, Android TV)를 누르세요.',
      'TV가 꺼져 있으면 켜기를 누르세요. TV에서 네트워크로 켜기를 활성화해 두었다면 켜져요. 한 번도 활성화한 적이 없다면 이번 한 번은 TV 본체의 버튼으로 켜고, 다음을 위해 활성화해 두세요.',
      '게임기를 켜세요. HDMI-CEC가 활성화되어 있으면(아래의 무료 요령을 보세요) TV가 저절로 게임기 입력으로 바뀌어요.',
      '바뀌지 않으면 Mando TV에서 입력을 누르고 게임기가 꽂힌 HDMI 포트(HDMI 1, HDMI 2 등)를 선택하세요.',
      '게임하는 동안 볼륨은 앱의 큰 버튼으로 조절하세요.',
    ],
    extra=[
      ('무료 요령: 게임기가 TV를 바꾸게 하기', 'PS5와 Xbox는 HDMI-CEC 덕분에 TV를 켜고 시작하자마자 자기 HDMI 입력으로 바꿀 수 있어요. PS5는 설정 > 시스템 > HDMI > HDMI 기기 링크 활성화에서 찾을 수 있어요. Xbox는 설정 > 일반 > TV 및 디스플레이 옵션을 열고 기기 제어 옵션을 찾으세요. TV에서는 브랜드에 따라 기능 이름이 달라요. 삼성은 Anynet+, LG는 SIMPLINK, 그 밖의 브랜드는 BRAVIA Sync나 HDMI 제어예요.'),
      ('TV가 다른 화면에 머물러 있을 때', '게임기는 켜졌는데 TV가 아직 안테나나 앱을 보여 주고 있다면 입력이 바뀌지 않은 거예요. 스마트폰에서 입력을 누르고 게임기의 HDMI 입력을 선택하세요. 또는 방향키와 확인으로 TV의 입력에 들어가거나 TV 본체의 버튼으로 HDMI 포트를 선택하세요. 번호는 게임기 케이블을 꽂은 포트예요.'),
      ('Roku TV일 때', 'TV 본체의 버튼은 대개 아래쪽 가운데나 뒷면에 있고 이 버튼으로 켤 수 있어요. 그다음부터는 스마트폰이 알아서 해 줘요.'),
    ],
    marca=None,
    faq=[
      ('Mando TV는 GTA VI와 관련이 있나요?', '아니요. Mando TV는 Rockstar Games나 Take-Two와 관련이 없어요. 리모컨을 찾느라 게임 시간을 잃지 않게 도와주는 앱일 뿐이에요.'),
      ('HDMI 입력을 바꾸는 건 무료인가요?', '네. Mando TV의 입력 목록은 TV 켜기, 방향키, 확인, 볼륨처럼 무료예요. HDMI-CEC로 게임기가 입력을 알아서 바꾸게 할 수도 있어요.'),
      ('내 TV에서도 되나요?', '같은 Wi-Fi에 있는 삼성, LG, Roku, Android TV에서 쓸 수 있어요. 다른 브랜드라도 HDMI-CEC 요령은 도움이 될 수 있어요.'),
      ('PS5나 Xbox에서 GTA VI(GTA 6)를 하는 데 쓸 수 있나요?', 'Mando TV는 게임기나 게임에는 관여하지 않아요. TV가 켜져 있고 올바른 HDMI 입력에 맞춰져 있게만 해 줘서 앉아서 바로 게임할 수 있게 해 줘요.'),
    ]),
  dict(clave='samsung-lost', corto='리모컨 없는 삼성 TV',
    titulo='삼성 리모컨을 잃어버렸나요? 스마트폰으로 쓰세요',
    desc='삼성 리모컨을 잃어버렸거나 고장 났나요? Wi-Fi로 스마트폰을 Tizen TV 리모컨으로 쓰세요. Mando TV로 간단하게, 무료, 광고 없음.',
    h1='삼성 TV 리모컨 없이 스마트폰으로 쓰는 방법',
    intro='삼성 리모컨을 잃어버렸거나 더 이상 작동하지 않는다면 스마트폰을 Wi-Fi 리모컨으로 쓸 수 있어요. Tizen이 탑재된 2016년 이후의 삼성 TV에서 쓸 수 있어요.',
    pasos=[
      'TV 본체의 버튼으로 TV를 켜세요. 대부분의 모델에서 아래쪽이나 뒷면에 있고, 작은 조이스틱일 때도 있어요.',
      'TV가 Wi-Fi에 연결되어 있고 스마트폰이 같은 네트워크에 있는지 확인하세요.',
      '스마트폰에서 Mando TV를 열면 목록에 삼성 TV가 저절로 나타나요. 눌러 주세요.',
      'TV가 연결을 확인해 달라고 해요. 대부분의 모델은 TV 본체의 버튼이나 뒷면의 조이스틱으로 확인할 수 있어요.',
      '끝났어요. 이제 스마트폰을 리모컨으로 쓸 수 있어요. 버튼, 키보드, 앱은 무료이고 터치패드는 Pro 기능이에요.',
      '다음에 스마트폰으로 TV를 켜려면 설정 > 일반 > 네트워크 > 전문가 설정에서 “모바일 기기로 켜기”를 활성화하세요.',
    ],
    extra=[
      ('TV가 허용을 묻지 않을 때', '이미 허용이 저장되어 있거나 TV가 다른 Wi-Fi에 있을 수 있어요. Mando TV를 닫고 TV를 켠 상태에서 앱을 다시 여세요. TV가 2016년보다 오래됐다면 아직 지원하지 않는 다른 시스템을 써요.'),
      ('실수로 허용을 거부했을 때', 'TV에서 설정 > 일반 > 외부 장치 관리자 > 장치 연결 관리자로 들어가 Mando TV를 허용으로 바꾸세요. 그래도 스마트폰이 TV를 찾지 못하면 [스마트폰이 TV를 찾지 못할 때](@not-found)를 읽어 보세요.'),
    ],
    marca='samsung',
    faq=[
      ('리모컨이 없는데 연결은 어떻게 확인하나요?', '대부분의 모델은 TV 본체의 버튼이나 뒷면의 조이스틱으로 확인할 수 있어요. 버튼이 없는 모델이라면 hola@mandotv.app으로 문의해 주세요. 도와 드릴게요.'),
      ('Mando TV는 삼성 계정이 필요한가요?', '아니요. 삼성 계정 없이 집 Wi-Fi로 바로 연결해요.'),
      ('오래된 삼성 TV에서도 되나요?', 'Tizen이 탑재된 2016년 이후의 삼성 TV에서 쓸 수 있어요.'),
    ]),
  dict(clave='wifi', corto='Wi-Fi로 스마트폰을 리모컨으로',
    titulo='스마트폰을 리모컨으로: Wi-Fi로 TV 조작하기',
    desc='스마트폰을 Wi-Fi로 TV에 연결해 삼성, LG, Roku, Google TV 리모컨으로 쓰세요. Mando TV로 브랜드별 단계를 알려 드려요. 무료.',
    h1='스마트폰을 Wi-Fi 리모컨으로 TV에 연결하는 방법',
    intro='스마트폰과 TV가 같은 Wi-Fi에 있고 리모컨 앱이 하나 있으면 돼요. Mando TV는 TV를 저절로 찾고 삼성, LG, Roku, Google TV, Android TV에서 쓸 수 있어요.',
    pasos=[
      '스마트폰과 TV를 같은 Wi-Fi에 연결하세요.',
      'Mando TV를 열면 목록에 TV가 저절로 나타나요. 눌러 주세요.',
      '브랜드에 맞게 연결을 확인하세요(자세한 내용은 아래에 있어요).',
      '버튼이나 스마트폰 키보드로 TV를 조작하세요. 터치패드는 Pro 기능이에요.',
    ],
    extra=[
      ('삼성', 'TV가 연결을 허용할지 물어봐요. 처음 한 번 화면에서 확인해 주세요. Tizen이 탑재된 2016년 이후의 TV에서 쓸 수 있어요. 스마트폰으로 TV를 켜려면 설정 > 일반 > 네트워크 > 전문가 설정에서 “모바일 기기로 켜기”를 활성화하세요.'),
      ('LG', 'TV에 허용 여부를 묻는 창이 떠요. 처음 한 번 확인해 주세요. 스마트폰으로 TV를 켜려면 설정에서 “모바일 기기로 TV 켜기”를 찾아 “Wi-Fi로 켜기”를 활성화하세요.'),
      ('Roku', 'Roku는 페어링이 필요 없어요. 목록에서 눌러 주기만 하면 연결돼요. 켜려면 설정 > 시스템 > 전원에서 “TV 빠른 시작”을 활성화하세요.'),
      ('Google TV와 Android TV', 'TV 화면에 코드가 나와요. 처음 한 번 Mando TV에 입력해 주세요. 켜려면 설정에서 “Wake on LAN”, “네트워크로 켜기”, “네트워크 대기 모드”를 찾아보세요.'),
    ],
    marca=None,
    faq=[
      ('스마트폰을 리모컨으로 쓰려면 인터넷이 필요한가요?', '스마트폰과 TV가 같은 Wi-Fi에 있으면 돼요. Mando TV는 그 네트워크로 TV에 바로 연결해요.'),
      ('왜 TV가 목록에 나타나지 않나요?', 'TV가 켜져 있는지, 스마트폰이 모바일 데이터나 다른 Wi-Fi를 쓰고 있지 않은지 확인하세요. 일부 공유기에는 기기끼리 서로 보이지 않게 하는 게스트 네트워크가 있어요.'),
      ('iPhone이나 Android 스마트폰에서 Mando TV를 쓸 수 있나요?', 'iPhone과 iPad는 App Store에서 이미 받을 수 있어요. Windows는 Microsoft Store에도 있어요. Android는 곧 나와요. Google Play의 무료 얼리 액세스에 참여할 수 있어요.'),
    ]),
  dict(clave='pc', corto='PC로 TV 조작하기',
    titulo='Windows PC로 TV 조작하기 (무료)',
    desc='Windows PC를 삼성, LG, Roku, Google TV 리모컨으로 쓰세요. Wi-Fi로 연결하고, 버튼·키보드·앱은 무료, PC 단축키는 Pro예요.',
    h1='Windows PC로 TV 조작하는 방법',
    intro='하루 종일 컴퓨터 앞에 있다면 리모컨을 찾을 필요가 없어요. Windows용 Mando TV는 집 Wi-Fi를 통해 삼성, LG, Roku, Google TV, Android TV를 조작해요. 앱을 바꾸거나 볼륨을 올리거나 PC 키보드로 YouTube에 입력할 때 편해요.',
    pasos=[
      'Windows 10 또는 11 컴퓨터에서 Microsoft Store로 Mando TV를 무료로 받으세요.',
      '컴퓨터와 TV가 같은 네트워크에 있는지 확인하세요(Wi-Fi든 랜선이든 같은 공유기에 연결되어 있으면 돼요).',
      'Mando TV를 열면 목록에 TV가 저절로 나타나요. 눌러 주세요.',
      '처음 한 번은 TV 화면에서 연결을 확인해 주세요(Google TV와 Android TV는 TV에 나오는 코드를 입력해요).',
      '끝났어요. 버튼이나 키보드로 TV의 검색창에 입력해 보세요. 터치패드는 Pro 기능이에요.',
    ],
    extra=[
      ('PC 단축키(Pro)', 'Mando TV Pro로 컴퓨터 키보드로 TV를 조작해요. 방향키로 이동하고, Enter는 확인, Backspace나 Esc는 뒤로, +와 -는 볼륨, M은 음소거, 스페이스바는 일시정지예요.'),
      ('항상 맨 위에 있는 미니 리모컨(Pro)', '작업하거나 PC로 게임을 하는 동안에도 작은 리모컨 창을 항상 보이게 둘 수 있어요.'),
      ('PC에서 TV에 말하기(Pro)', 'Mando TV Pro로 PC의 마이크를 통해 TV에 명령할 수 있어요. “YouTube 열어 줘”, “볼륨 올려 줘”, “30분 뒤에 꺼 줘”처럼 말하는 그대로 해요. Windows에서는 음성을 PC 안에서 인식해요. 인터넷이 필요 없고, Windows 설정을 바꿀 필요도 없고, 앱의 6개 언어에서 모두 작동해요. 말한 내용은 PC 밖으로 나가지 않고 저장되지도 않아요. 아주 오래된 프로세서에서만 앱이 Windows 받아쓰기를 대신 써요. 이때는 개인정보 설정에서 온라인 음성 인식을 켜고 Windows에 한국어(대한민국)가 추가되어 있어야 해요. 빠진 것이 있으면 앱이 알려 주고 버튼으로 해당 설정을 열어 줘요.'),
    ],
    marca=None,
    faq=[
      ('PC로 TV를 조작하려면 케이블이나 Bluetooth가 필요한가요?', '아니요. Mando TV는 집 네트워크로 연결해요. PC와 TV가 같은 공유기에 연결되어 있기만 하면 돼요.'),
      ('모든 TV에서 되나요?', 'Tizen이 탑재된 삼성 TV(2016년 이후), webOS가 탑재된 LG, Roku, Google TV나 Android TV(Sony, Philips, TCL, Hisense, Sharp, Xiaomi, Toshiba, Panasonic, Haier, Skyworth 등)에서 쓸 수 있어요.'),
      ('가격은 얼마인가요?', '버튼, 키보드, 네트워크로 켜기는 무료이고 광고가 없어요. Mando TV Pro는 터치패드, PC 단축키, 미니 리모컨 같은 추가 기능을 위한 것으로, 구독 없이 한 번만 결제해요.'),
      ('Windows에서 마이크가 내 말을 알아듣지 못해요.', '음성 기능이 켜져 있는지(Pro에 포함돼요), 그리고 Windows에서 PC 마이크가 작동하는지 확인하세요. 거의 모든 PC에서는 인터넷 없이 기기 안에서 음성을 인식해요. 아주 오래된 프로세서에서만 앱이 Windows 받아쓰기를 써요. 이때는 Windows 개인정보 설정에서 온라인 음성 인식이 켜져 있는지, 언어 설정에 한국어(대한민국)가 있는지 확인하세요. Mando TV는 듣고 있는 동안에만 이 언어를 써요.'),
    ]),
  dict(clave='roku-403', corto='Roku 앱이 작동하지 않을 때',
    titulo='Roku 앱이 작동하지 않나요? 403 오류 해결하기',
    desc='스마트폰은 연결됐는데 Roku가 반응하지 않나요? “모바일 앱으로 제어”를 5단계로 활성화하고 스마트폰을 다시 리모컨으로 쓰세요.',
    h1='Roku 앱이 작동하지 않을 때 해결하는 방법',
    intro='스마트폰이 Roku를 찾아서 연결은 되는데 어떤 버튼도 반응하지 않는다면, 거의 항상 Roku 안에서 리모컨 앱을 막는 설정 때문이에요. 최신 Roku 버전은 기본적으로 더 많이 제한해요. Roku 메뉴에서 1분이면 해결돼요.',
    pasos=[
      'Roku에서 홈을 누르고 설정으로 가세요.',
      '시스템을 열고 고급 시스템 설정으로 가세요.',
      '“모바일 앱으로 제어”로 들어가세요. 일부 모델에서는 “외부 제어”라고 불러요.',
      '“네트워크 액세스”에서 기본 또는 Permissive를 선택하세요. 모델에 따라 스위치 하나뿐이라면 활성화로 두세요.',
      '스마트폰의 Mando TV로 돌아와 Roku를 누르세요. 이제 버튼이 반응해요.',
    ],
    extra=[
      ('내 문제가 이것인지 알아보는 방법', '증상이 뚜렷해요. 스마트폰 목록에 Roku가 보이고 연결도 되는데 버튼을 눌러도 아무 일도 일어나지 않아요. 내부적으로 Roku는 “금지됨”을 뜻하는 403 오류로 응답해요. Mando TV는 연결할 때 이를 알아채고 화면에 바로 이 단계들을 보여 줘요.'),
      ('기본과 Permissive 중 무엇을 고르나요?', '기본이면 충분해요. 집 네트워크에서 오는 명령을 받아들이는데, 리모컨에 필요한 건 바로 그거예요. Permissive는 더 개방적이라서 특이한 네트워크에서만 필요해요.'),
      ('Roku 리모컨이 없을 때', '설정이 비활성화로 되어 있으면 실제 Roku 리모컨으로만 바꿀 수 있어요. 한 번만 바꾸게 하나 빌린 다음, 그 뒤로는 모든 걸 스마트폰으로 하세요. [Roku 리모컨을 잃어버렸을 때](@roku-lost)도 읽어 보세요.'),
    ],
    marca='roku',
    faq=[
      ('전에는 됐는데 왜 갑자기 Roku가 반응하지 않나요?', 'Roku 업데이트로 이 설정이 더 제한적으로 바뀔 수 있어요. 스마트폰이나 Wi-Fi 문제가 아니에요. 앱 제어를 다시 허용하기만 하면 돼요.'),
      ('Roku TV와 Roku 플레이어 둘 다 해당하나요?', '네. Roku 플레이어와 Roku TV 기기 모두 같은 메뉴에 이 설정이 있어요.'),
      ('설정을 기본으로 두어도 안전한가요?', '네. 집 네트워크 안의 기기가 보내는 명령만 받아들여요.'),
    ]),
  dict(clave='not-found', corto='스마트폰이 TV를 찾지 못할 때',
    titulo='스마트폰이 TV를 찾지 못하나요? 확인할 6가지',
    desc='리모컨 앱이 TV를 찾지 못하나요? Wi-Fi, VPN, 로컬 네트워크 접근을 확인하세요. 삼성, LG, Roku, Android TV 모두 해당돼요.',
    h1='스마트폰이 TV를 찾지 못할 때 확인할 것',
    intro='리모컨 앱을 열었는데 목록이 비어 있거나, TV가 나타나도 연결이 끊어져요. 거의 항상 TV가 아니라 네트워크 문제예요. 아래 항목을 순서대로 확인하세요. 첫 번째만으로 대부분 해결돼요.',
    pasos=[
      '스마트폰이 어느 Wi-Fi에 있고 TV가 어느 Wi-Fi에 있는지 확인하세요. 이름까지 같은 하나의 네트워크여야 해요. 게스트 네트워크는 기기끼리 분리하기 때문에 쓸 수 없어요.',
      'VPN을 쓰고 있다면 스마트폰에서 끄세요. VPN이 켜져 있으면 스마트폰이 다른 네트워크를 통해 인터넷에 나가서 집 안의 기기를 보지 못하거나, 몇 초 뒤에 연결이 끊어져요.',
      '모바일 데이터를 잠깐 끄세요. 일부 스마트폰은 신호가 약하면 Wi-Fi에서 모바일 데이터로 저절로 바뀌어요.',
      'TV를 켜고 완전히 부팅될 때까지 기다리세요. 꺼진 TV는 검색에 응답하지 않아요.',
      'iPhone이라면 앱에 “로컬 네트워크” 권한이 있는지 확인하세요. 설정 > 개인정보 보호 및 보안 > 로컬 네트워크예요.',
      '그래도 나타나지 않으면 직접 추가하세요. Mando TV에서 “IP로 추가”를 누르고 TV의 IP 주소를 입력하세요.',
    ],
    extra=[
      ('앱의 안내를 따라 하기', 'TV 목록에는 TV가 나타나지 않을 때 쓰는 버튼이 있어요. 앱이 가장 흔한 원인(같은 Wi-Fi, VPN, 로컬 네트워크 권한 등)을 단계별로 확인하고, 고칠 때마다 다시 확인하는 버튼을 보여 줘요. 이 도우미는 무료예요.'),
      ('TV의 IP 주소를 찾는 곳', 'TV의 네트워크 메뉴에 있고 모델마다 조금 달라요. LG는 설정, 네트워크, Wi-Fi 연결, 고급 Wi-Fi 설정이에요. 삼성은 설정, 일반, 네트워크, 네트워크 상태, IP 설정이에요. Roku는 설정, 네트워크, 정보예요. Android TV와 Google TV는 설정, 네트워크 및 인터넷에서 내 네트워크를 누르세요. 192.168.1.86 같은 숫자예요.'),
      ('나타나기는 하는데 연결이 끊어질 때', '몇 초 뒤에 연결이 끊어진다면 원인은 대개 스마트폰이에요. VPN, 다른 Wi-Fi로의 전환, 절전 모드 같은 것들이에요. VPN을 끄고 같은 Wi-Fi에 머문 채 다시 해 보세요.'),
      ('2.4GHz와 5GHz Wi-Fi', '둘 다 같은 공유기에서 나온다면 스마트폰이 5GHz 네트워크에, TV가 2.4GHz 네트워크에 있어도 상관없어요. Wi-Fi 증폭기가 있는데도 TV가 나타나지 않으면 스마트폰을 메인 공유기에 가까이 가져가서 다시 해 보세요.'),
    ],
    marca=None,
    faq=[
      ('모바일 데이터로 TV를 조작할 수 있나요?', '아니요. 리모컨 신호는 집 Wi-Fi를 통해 가기 때문에 스마트폰과 TV가 같은 네트워크에 있어야 해요.'),
      ('VPN이 켜져 있으면 왜 안 되나요?', 'VPN이 스마트폰의 모든 트래픽을 다른 네트워크로 보내서 스마트폰이 집 안의 기기를 보지 못하게 되기 때문이에요. 리모컨을 쓰는 동안에는 끄세요.'),
      ('Bluetooth나 적외선으로도 되나요?', '스마트 TV에서는 Mando TV가 Wi-Fi를 써요. 적외선은 적외선 송신기가 있는 Android 스마트폰에서만 되고 스마트 TV가 아닌 TV를 위한 거예요. Bluetooth는 베타로 Android 9 이상에서만 무료로 쓸 수 있어요. 스마트폰이 Bluetooth 키보드이자 리모컨으로 TV에 연결되고 Wi-Fi가 필요 없어요. Google TV, Android TV, Fire TV에서 작동하고, Bluetooth 키보드를 받아들이는 다른 브랜드에서도 될 수 있어요. Roku는 받아들이지 않아요.'),
    ]),
  dict(clave='androidtv-code', corto='Android TV 페어링 코드',
    titulo='Android TV에서 페어링 코드를 물어볼 때 할 일',
    desc='Android TV나 Google TV가 연결할 때 6자리 코드를 보여 줘요. 입력하는 방법과 코드가 나오지 않거나 틀렸다고 나올 때 해결하는 방법이에요.',
    h1='Android TV에서 페어링 코드를 물어볼 때 할 일',
    intro='스마트폰을 Android TV나 Google TV에 처음 연결하면 TV 화면에 6자리 코드가 나와요. 정상이고 한 번만 해요. 다른 사람이 내 TV를 조작하지 못하게 하려는 거예요. 코드를 입력하는 방법과 코드가 나오지 않을 때 할 일을 알려 드릴게요.',
    pasos=[
      'TV를 켜고 홈 화면이 보이게 두세요.',
      'TV와 같은 Wi-Fi에 있는 스마트폰에서 Mando TV를 열고 목록에서 TV를 누르세요.',
      'TV 화면을 보세요. 영문자와 숫자로 된 6자리 코드가 나와요.',
      '보이는 그대로 스마트폰에 입력하고 페어링을 누르세요. 영문자는 A부터 F까지뿐이라서 동그란 모양은 항상 숫자 0이에요.',
      '끝났어요. TV가 스마트폰을 기억하고, 다시는 코드를 묻지 않아요.',
    ],
    extra=[
      ('TV에 코드가 나오지 않을 때', 'TV가 대기 상태가 아니라 정말 켜져 있는지, 스마트폰이 같은 Wi-Fi에 있는지 확인하세요. 스마트폰에서 TV를 한 번 더 누르세요. 그래도 나오지 않으면 TV를 다시 시작하세요. 전원 플러그를 10초 동안 뽑았다가 다시 꽂고 시도해 보세요.'),
      ('코드가 틀렸다고 나올 때', '코드는 요청할 때마다 바뀌어요. 시간이 오래 걸렸거나 두 번 요청했다면 화면에 있는 마지막 코드만 유효해요. 스마트폰에서 TV를 한 번 더 누르고 새 코드를 입력하세요.'),
      ('TV가 코드를 다시 물어볼 때', 'TV를 공장 초기화했거나 스마트폰의 앱 데이터를 지웠을 때 그래요. 다시 페어링하면 저장돼요. 리모컨이 전혀 없다면 [리모컨 없이 Android TV 쓰기](@androidtv)를 읽어 보세요.'),
    ],
    marca='android',
    faq=[
      ('어떤 TV에서 이 코드를 쓰나요?', 'Android TV나 Google TV가 탑재된 TV예요. Sony, Philips, TCL, Hisense, Sharp, Xiaomi, Google TV가 탑재된 Chromecast 등이 있어요.'),
      ('스마트폰에 Google 계정이 있어야 하나요?', '아니요. 화면에 나오는 코드만 있으면 돼요.'),
      ('안전한가요?', '네. 코드는 TV 앞에 있다는 증거예요. 화면의 코드를 보지 못하면 아무도 페어링할 수 없어요.'),
    ]),
  dict(clave='roku-lost', corto='Roku 리모컨 분실',
    titulo='Roku 리모컨을 잃어버렸나요? 스마트폰을 Wi-Fi로 쓰세요',
    desc='Roku 리모컨을 잃어버렸나요? 스마트폰이 Wi-Fi로 대신해 줘요. 공유기를 바꿔서 Roku가 Wi-Fi에 연결되지 않을 때도 쉬운 방법이 있어요.',
    h1='Roku 리모컨을 잃어버렸을 때 스마트폰으로 쓰는 방법',
    intro='Roku 리모컨을 잃어버렸거나 더 이상 작동하지 않아도 Roku가 아직 내 Wi-Fi에 연결되어 있다면 스마트폰이 대신해 줘요. Wi-Fi나 공유기를 바꿨을 때도 해결 방법이 있어요.',
    pasos=[
      '먼저 리모컨의 소리를 울려 보세요. Roku Voice Remote Pro처럼 스피커가 있는 Roku 리모컨이라면 Mando TV를 열고 Roku에 연결한 다음, 리모컨 소리 울리기 옵션으로 찾아 보세요. 스피커가 있는 Roku 리모컨에서만 되고, Roku가 켜져 있어야 해요.',
      'TV를 켜고 Roku는 그대로 꽂아 두세요. 건드릴 필요가 없어요.',
      '스마트폰을 Roku가 쓰는 Wi-Fi에 연결하세요.',
      'Mando TV를 열면 목록에 Roku가 저절로 나타나요. 눌러 주세요.',
      '쓰던 리모컨처럼 방향키, 확인, 홈, 뒤로를 쓰세요. Roku는 코드를 묻지 않아요.',
      '버튼이 반응하지 않으면 Roku가 앱 제어를 막고 있는 거예요. [Roku 앱이 작동하지 않을 때](@roku-403) 가이드에서 허용하는 방법을 알려 드려요.',
    ],
    extra=[
      ('Roku가 Wi-Fi에 연결되어 있지 않을 때(공유기를 바꿨거나 이사했을 때)', '리모컨이 없으면 새 네트워크를 설정하는 메뉴에 들어갈 수 없지만 요령이 있어요. Roku는 예전 네트워크와 이름과 비밀번호가 같은 네트워크에 저절로 연결돼요. 다른 스마트폰에서 정확히 그 이름과 비밀번호로 Wi-Fi 핫스팟을 만들고, Mando TV를 쓰는 스마트폰을 거기에 연결하면 목록에 Roku가 나타나요. 거기서 설정, 네트워크로 가서 새 Wi-Fi에 연결하세요.'),
      ('Roku TV일 때', 'Roku TV 기기에는 TV를 켜는 본체 버튼이 있어요. 대개 아래쪽 가운데나 뒷면에 있어요. 그걸로 켜고 스마트폰으로 이어서 쓰면 돼요.'),
      ('다른 리모컨을 사고 싶을 때', '내 모델에 맞는지 확인하세요. TV 뒤에 숨은 작은 Roku 플레이어는 적외선이 닿지 않아서 적외선이 아닌 리모컨이 필요해요.'),
    ],
    marca='roku',
    faq=[
      ('스마트폰으로 Roku를 켤 수 있나요?', '연결된 Roku 플레이어는 항상 켜져 있어요. Roku TV는 설정 > 시스템 > 전원에서 “TV 빠른 시작”을 활성화해 두면 Mando TV가 Wi-Fi로 켜 줘요.'),
      ('볼륨은요?', 'Roku TV라면 스마트폰으로 볼륨을 올리고 내려요. HDMI로 연결한 Roku 플레이어는 TV에 따라 달라요. 되는 TV도 있고 안 되는 TV도 있어요.'),
      ('계정을 만들어야 하나요?', '아니요. Mando TV는 계정이 필요 없고 앱 하나로 삼성, LG, Android TV까지 조작해요.'),
    ]),
]

SOPORTE = dict(
  titulo='도움말: Mando TV로 TV 연결하고 켜기',
  desc='Mando TV 리모컨을 LG, 삼성, Roku, Android TV에 연결하고, 스마트폰으로 TV를 켜고, 문제를 해결하는 방법이에요.',
  h1='도움말',
  intro='가장 자주 묻는 질문을 단계 순서대로 모았어요. 찾는 내용이 없다면 <a href="mailto:hola@mandotv.app?subject=Mando%20TV%20%EB%8F%84%EC%9B%80%EB%A7%90">hola@mandotv.app</a>으로 보내 주세요. 답장해 드릴게요.',
)
SOPORTE_HTML = '''      <h2 id="encontrar">TV 찾기</h2>
      <div class="preguntas">
        <details open><summary>목록에 TV가 나타나지 않아요</summary>
          <ol>
            <li>스마트폰과 TV가 같은 Wi-Fi에 있는지 확인하세요. 공유기에 2.4GHz와 5GHz 네트워크가 서로 다른 이름으로 있으면 서로 보이지 않을 때가 있어요.</li>
            <li>TV가 켜져 있는지 확인하세요.</li>
            <li>iPhone이라면 설정, Mando TV에서 Mando TV에 “로컬 네트워크” 권한이 있는지 확인하세요.</li>
            <li>TV 목록에서 TV가 나타나지 않을 때 쓰는 버튼을 누르세요. 앱이 가장 흔한 원인(같은 Wi-Fi, VPN, 로컬 네트워크 권한 등)을 단계별로 확인하고, 고칠 때마다 다시 확인하는 버튼을 보여 줘요.</li>
            <li>그래도 나타나지 않으면 + 버튼을 누르고 브랜드를 고른 뒤 TV의 IP 주소를 입력하세요. TV의 네트워크 메뉴에서 볼 수 있어요(예: 192.168.1.50).</li>
          </ol>
        </details>
        <details><summary>모바일 데이터로도, 밖에서도 되나요?</summary>
          <p>아니요. Mando TV는 집 네트워크 안에서 TV와 통신해요. 그래서 스마트폰이 그 Wi-Fi에 연결되어 있어야 해요.</p>
        </details>
      </div>

      <h2 id="conectar">처음 연결하기</h2>
      <p>브랜드별 전체 가이드: <a href="@@R_lg@@">LG</a>, <a href="@@R_samsung@@">삼성</a>, <a href="@@R_roku@@">Roku</a>, <a href="@@R_android@@">Android TV</a>.</p>
      <div class="preguntas">
        <details><summary>LG</summary>
          <p>TV를 누르면 화면에 허용 여부를 묻는 창이 떠요. 쓰던 리모컨으로 허용해 주세요. 한 번만 하면 돼요.</p>
        </details>
        <details><summary>삼성</summary>
          <p>TV가 Mando TV의 연결을 허용할지 물어봐요. 리모컨으로 “허용”을 선택하세요. 실수로 거부했다면 설정 > 일반 > 외부 장치 관리자 > 장치 연결 관리자로 들어가 허용으로 바꾸세요.</p>
        </details>
        <details><summary>Roku</summary>
          <p>Roku는 허용 여부를 묻지 않아요. 연결되지 않으면 Roku에서 설정 > 시스템 > 고급 시스템 설정 > 모바일 앱으로 제어로 들어가 네트워크 액세스를 기본 또는 Permissive로 두세요(최신 Roku 소프트웨어에서는 “모바일 앱으로 제어”를 활성화로 설정하세요).</p>
        </details>
        <details><summary>Android TV와 Google TV</summary>
          <p>TV에 6자리 코드가 나와요. 나온 그대로 Mando TV에 입력하세요. Sony, Philips, TCL, Hisense, Sharp, Xiaomi, Google TV가 탑재된 Chromecast 등 Android TV가 탑재된 기기에서 쓸 수 있어요.</p>
        </details>
      </div>

      <h2 id="encender">앱으로 TV 켜기</h2>
      <p>Mando TV는 집 네트워크로 TV를 켜요. 두 가지가 필요해요. TV가 켜져 있을 때 최소 한 번은 연결해 둬야 하고, TV에서 네트워크로 켜기가 활성화되어 있어야 해요. 설정 이름은 모델마다 달라요. 가장 흔한 이름은 다음과 같아요.</p>
      <div class="preguntas">
        <details><summary>LG</summary>
          <p>설정 > 일반 > 기기 > 외부 기기(구형 모델은 연결 > 모바일 연결 관리)에서 “모바일 기기로 TV 켜기”를 찾아 “Wi-Fi로 켜기”를 활성화하세요. “빠른 시작+”가 있으면 그것도 활성화하세요.</p>
        </details>
        <details><summary>삼성</summary>
          <p>설정 > 일반 > 네트워크 > 전문가 설정에서 “모바일 기기로 켜기”를 활성화하세요.</p>
        </details>
        <details><summary>Roku</summary>
          <p>Roku TV 기기라면 설정 > 시스템 > 전원에서 “TV 빠른 시작”을 활성화하세요. TV에 꽂아 쓰는 Roku 플레이어는 이 방법으로 켤 수 없어요.</p>
        </details>
        <details><summary>Android TV와 Google TV</summary>
          <p>제조사마다 달라요. 네트워크나 전원 설정에서 “Wake on LAN”, “네트워크로 켜기”, “네트워크 대기 모드”, “Remote start”를 찾아보세요. 이 옵션이 없는 모델도 있어요.</p>
        </details>
      </div>

      <h2 id="falla">잘 되지 않을 때</h2>
      <div class="preguntas">
        <details><summary>연결이 끊기거나 반응이 없어요</summary>
          <ol>
            <li>리모컨 화면에서 다시 연결을 누르세요.</li>
            <li>그래도 안 되면 Mando TV를 닫았다가 다시 여세요.</li>
            <li>TV의 IP 주소가 바뀌었다면 목록에서 TV를 삭제하고 다시 추가하세요.</li>
          </ol>
        </details>
        <details><summary>오류 보고서 보내는 방법</summary>
          <ol>
            <li>Mando TV에서 맞춤 설정 버튼(위쪽의 조절 아이콘)을 누르세요.</li>
            <li>테스트 보고서 복사를 누르세요.</li>
            <li>TV의 브랜드와 모델명과 함께 hola@mandotv.app으로 보내는 이메일에 붙여 넣으세요.</li>
          </ol>
          <p>보고서에는 비밀번호도, 코드도, 입력한 내용도 들어 있지 않아요.</p>
        </details>
        <details><summary>Pro를 구매했는데 나타나지 않아요</summary>
          <p>맞춤 설정에서 구매 복원을 누르세요. 구매할 때 쓴 스토어 계정과 같은 계정이어야 해요. 그래도 나타나지 않으면 문의해 주세요.</p>
        </details>
      </div>

      <h2 id="guias">단계별 가이드</h2>
      <p><a href="@@R_guias@@">모든 가이드 보기</a></p>
      <ul>
@@GUIAS@@
      </ul>

      <h2 id="contacto">더 궁금한 점이 있나요?</h2>
      <p><a href="mailto:hola@mandotv.app?subject=Mando%20TV%20%EB%8F%84%EC%9B%80%EB%A7%90">hola@mandotv.app</a>으로 보내 주세요. TV의 브랜드와 모델명, 어느 단계에서 막혔는지 알려 주세요. 한국어로 써 주셔도 돼요. 스페인어나 영어로 답장해 드리고, 원하시면 번역기의 도움을 받아 한국어로도 답해 드려요.</p>
'''

PRIVACIDAD = dict(
  titulo='개인정보처리방침 | Mando TV',
  desc='Mando TV는 개인정보를 수집하지 않아요. 계정도, 광고도, 추적기도 없어요. 앱은 Wi-Fi 안에서 내 TV하고만 통신해요.',
  h1='개인정보처리방침',
  intro='간단히 말하면, Mando TV는 내 데이터를 수집하지 않아요. 계정도, 광고도, 추적기도 없고, 내가 하는 일을 저장하는 자체 서버도 없어요.',
)
PRIVACIDAD_HTML = '''      <p class="fecha">2026년 11월 14일부터 적용돼요. 2026년 11월 26일에 마지막으로 업데이트했어요.</p>

      <h2>우리는 누구인가요</h2>
      <p>Mando TV는 스마트폰이나 컴퓨터로 TV를 조작하는 앱이에요. 이 방침은 앱이 어떤 정보를 쓰고 그 정보로 무엇을 하는지 설명해요. 궁금한 점은 <a href="mailto:hola@mandotv.app">hola@mandotv.app</a>으로 보내 주세요.</p>

      <h2>수집하는 데이터</h2>
      <p>앱: 없어요. 앱은 나에 대한 정보나 앱을 어떻게 쓰는지를 우리나 제3자에게 보내지 않아요. 분석, 광고, 추적 도구도 쓰지 않아요.</p>
      <p>이 웹사이트: 방문을 두 가지 방식으로 측정해요. <a href="#cookies">이 웹사이트의 쿠키</a> 항목에서 설명해요.</p>

      <h2>앱이 내 기기에 저장하는 것</h2>
      <p>앱이 작동하려면 다음 정보를 내 스마트폰이나 컴퓨터에만 저장해요.</p>
      <ul>
        <li>내가 추가한 TV: 이름, 브랜드, 내 네트워크에서의 IP 주소, 켤 때 쓰는 네트워크 하드웨어 주소(MAC).</li>
        <li>허용을 확인할 때 각 TV가 건네는 연결 키. 시스템의 보안 저장소에 암호화해서 보관해요(iPhone과 Mac은 키체인, Android는 Keystore, Windows는 보호된 저장소).</li>
        <li>내 설정: 밝은 테마 또는 어두운 테마, 배경색, 진동, 리모컨 유형.</li>
        <li>Pro 기능을 쓰면: 즐겨찾기 앱, 루틴, 최근 YouTube 검색어(앱에서 삭제할 수 있어요).</li>
      </ul>
      <p>앱을 삭제하면 이 모든 정보도 함께 삭제돼요.</p>

      <h2>앱이 통신하는 대상</h2>
      <p>집 Wi-Fi 안에 있는 내 TV하고만 통신해요. TV를 찾으려고 앱이 내 로컬 네트워크를 살펴봐요. 그래서 iPhone에서는 “로컬 네트워크” 권한을 요청해요. 앱 키보드로 입력한 글자는 TV로 바로 가고 저장되지 않아요.</p>
      <p>또 앱을 열 때 이 웹사이트에서 작은 공개 파일(mandotv.app/app/config.json)을 내려받아요. 설치해야 할 새 버전이 있는지, 어떤 기능이 Mando TV Pro에 속하는지 알기 위해서예요. 웹페이지를 열 때와 같은 다운로드예요. 앱은 내 데이터나 TV, 내가 하는 일을 보내지 않아요. 알맞은 안내를 보여 주기 위해 앱 버전과 시스템(예: Android)만 알려요. 인터넷이 없으면 앱은 마지막으로 내려받은 파일로 계속 작동해요. 파일을 내려받지 못한 채 30일이 넘으면 앱이 잠깐 인터넷에 연결해 달라고 요청해요.</p>

      <p>사진이나 동영상을 TV로 보낼 때(Pro 기능), TV는 내가 고른 파일만 집 Wi-Fi를 통해 내 스마트폰이나 PC에서 바로 가져가요. 인터넷이나 우리를 거치지 않고, 앱은 나머지 사진을 보지 않으며, 이 화면을 닫으면 공유도 끝나요.</p>
      <h2>마이크와 음성</h2>
      <p>iPhone, Mac, Android에서 음성 검색은 말하기 버튼을 누르고 있는 동안에만 마이크를 써요. 내가 말한 내용은 기기 시스템의 음성 인식이 글자로 바꿔요. iPhone과 Mac은 Apple이, Android는 Google이 각자의 개인정보 방침에 따라 처리해요. Windows에서는 음성을 내 PC 안에서 인식하고 기기 밖으로 나가지 않아요. 아주 오래된 프로세서에서만 앱이 Microsoft의 Windows 음성 입력을 쓰고, 이때는 Microsoft의 개인정보 방침을 따라요. Windows에서는 음성 패널을 열면 마이크가 켜지고, 패널을 닫거나 30초 동안 쓰지 않으면 꺼져요. 말하지 않는 동안에는 아무것도 녹음하거나 저장하지 않아요. Mando TV는 오디오를 녹음하거나 저장하지 않고, 변환된 글자는 키보드로 입력한 내용처럼 내 TV로 바로 가요.</p>

      <h2>홈: Apple Home과 Google Home 기기</h2>
      <p>홈 화면(테스트 중)을 열면 앱이 이미 Apple 홈 앱(HomeKit)이나 Google Home에 있는 기기를 볼 수 있는 권한을 요청해요. 이 권한으로 기기의 이름, 방, 상태(켜짐 또는 꺼짐, 밝기, 온도, 가전제품의 프로그램 진행 상태)를 읽어서 보여 주고, 내가 누른 동작을 기기에 보내요. 모든 일은 내 스마트폰과 Apple 또는 Google 시스템 사이에서 이루어져요. Mando TV는 이 목록을 저장하지 않고, 우리나 제3자에게 보내지 않으며, 광고나 분석에 쓰지 않아요. Android에서는 Google Home이 내 Google 계정으로, Google의 개인정보 방침에 따라 작동해요. 권한은 언제든 거둘 수 있어요. iPhone은 설정 &gt; 개인정보 보호 및 보안 &gt; HomeKit에서, Android는 Google 계정 설정에서 할 수 있어요.</p>
      <p>“홈 기능이 어떠셨나요?”를 누르면 이메일 앱이 열리고 hola@mandotv.app으로 보내는 메시지에 기술 요약이 담겨요. 앱 버전, 시스템, 종류별로 몇 개의 기기가 나타났는지와 반응하는지 여부예요. 기기, 방, 집의 이름은 들어 있지 않고, 메시지는 내가 직접 보낼 때만 전송돼요.</p>

      <h2>테스트 보고서</h2>
      <p>앱에는 오류를 고치는 데 도움이 되는 “테스트 보고서 복사” 버튼이 있어요. 보고서는 앱이 열려 있는 동안 앱의 메모리에만 있고 저절로 전송되지 않아요. 복사해서 전달할지는 내가 결정해요. 연결 키도, 페어링 코드도, 입력한 내용도 들어 있지 않고, 검색, 연결, 오류처럼 앱이 수행한 단계만 있어요.</p>

      <h2 id="cookies">이 웹사이트의 쿠키</h2>
      <p>이 내용은 mandotv.app 웹사이트에만 해당하고 앱에는 해당하지 않아요.</p>
      <h3>항상 쿠키 없이</h3>
      <p>Cloudflare Web Analytics로 방문을 익명으로 집계해요. 몇 명이 웹사이트를 방문하는지, 어떤 페이지를 읽는지, 어느 나라에서 오는지를 봐요. 쿠키를 쓰지 않고, IP 주소로 나를 식별하지 않고, 다른 웹사이트에서 하는 일을 추적하지 않아요.</p>
      <h3>쿠키 사용, 동의한 경우에만</h3>
      <p>쿠키 안내에서 “수락”을 누르면 웹사이트가 어떻게 쓰이는지 더 잘 이해하려고 Google Analytics(Google LLC)를 켜요. 페이지 조회, 머문 시간, 기기 유형, 대략적인 도시, 방문 경로를 봐요. 이를 위해 _ga와 _ga_* 쿠키를 브라우저에 최대 2년간 저장해요. Google은 이 데이터를 칠레 밖의 서버에서 처리할 수 있어요. 광고 기능과 Google Signals는 꺼 두었고, 이 데이터를 광고를 보여 주는 데 쓰지 않아요.</p>
      <p>“거부”를 누르거나 아무것도 고르지 않으면 Google Analytics는 로드되지 않고 쿠키도 저장되지 않아요. 각 페이지 맨 아래의 “쿠키” 버튼으로 언제든 결정을 바꿀 수 있어요. 동의를 철회하면 이 쿠키를 삭제해요.</p>
      <p>선택한 내용은 다시 묻지 않으려고 내 브라우저에 저장돼요(로컬 저장소이고 누구에게도 보내지 않아요).</p>

      <h2>구매</h2>
      <p>Mando TV Pro를 구매하면 결제는 앱 스토어(App Store, Google Play, Microsoft Store)가 처리해요. 우리는 카드 정보를 받지도 저장하지도 않아요. 스토어는 구매가 있다는 사실만 앱에 확인해 줘요.</p>

      <h2>보내 주시는 이메일</h2>
      <p><a href="mailto:hola@mandotv.app">hola@mandotv.app</a>으로 보내 주시면 이메일 주소와 알려 주신 내용은 답장을 드리는 데에만 써요. 다른 곳에 넘기지 않고 광고에 쓰지 않아요. 언제든 메시지를 삭제해 달라고 요청하실 수 있어요.</p>

      <h2>어린이</h2>
      <p>앱은 어린이를 포함해 누구에게서도 데이터를 수집하지 않아요.</p>

      <h2>이 방침의 변경</h2>
      <p>앱이 내 데이터로 하는 일이 언젠가 바뀐다면, 변경이 앱에 적용되기 전에 이 페이지와 위의 날짜를 먼저 업데이트해요.</p>
'''


# >>> guías traídas del inglés (ensamblar.py)
# Adaptadas con Ollama (qwen3.6:35b) desde las guías inglesas y auditadas por Opus el 22-nov. Rutas en idiomas_sitio.py.
GUIAS += [
  dict(clave='no-sub', corto='구독 없는 리모컨 앱', fecha='2026-11-23',
    titulo='구독 없고 광고 없는 TV 리모컨 앱',
    desc='광고가 나오거나 주 단위 구독을 요구하는 리모컨 앱이 지겨우신가요? Mando TV는 무료에 광고가 없고, Pro는 선택 사항으로 한 번만 결제해요. 솔직한 비교.',
    h1='구독도 광고도 없는 리모컨 앱',
    intro='많은 범용 리모컨 앱은 광고를 보여 주거나 쓰기 전에 주 단위 구독을 요구해요. Mando TV는 달라요. 리모컨은 무료이고, 광고도 계정도 없어요. 선택 사항인 Pro는 한 번만 결제해요. 앱이 할 수 없는 것까지 포함해서 비교해 드릴게요.',
    pasos=[
      '설치하기 전에 앱의 스토어 페이지를 열어 앱 내 구매 항목을 확인하세요. 주 단위나 월 단위 가격이 있으면 구독이라는 뜻이에요.',
      'Google Play라면 페이지에 “광고 포함”이라고 되어 있는지 확인하고, 별점이 낮은 최신 리뷰를 읽어 보세요. 예상하지 못한 결제 장벽이 자주 나와요.',
      '앱이 Wi-Fi로 내 TV를 조작할 수 있는지 확인하세요. Mando TV는 삼성(2016년 이후), LG webOS, Roku, Google TV, Android TV, Fire TV에서 쓸 수 있어요.',
      'Mando TV를 설치하고 스마트폰을 TV와 같은 Wi-Fi에 연결한 다음, 목록에서 TV를 누르세요.',
      'TV의 허용 창을 확인하거나 화면에 나온 코드를 입력하세요. 버튼, 볼륨, 채널, 키보드는 무료예요.',
    ],
    tabla=dict(titulo='Mando TV와 많은 리모컨 앱 비교',
      cabeza=['', 'Mando TV', '광고나 구독이 있는 많은 앱'],
      filas=[
        ['기본 리모컨', '무료', '광고와 함께 무료이거나 체험 기간 뒤에 숨어 있는 경우가 많아요'],
        ['광고', '없음', '자주 있어요'],
        ['구독', '없음. Pro는 선택 사항으로 한 번만 결제', '주 단위나 월 단위 요금제가 흔해요'],
        ['계정', '필요 없음', '앱마다 달라요'],
        ['Wi-Fi로 조작하는 스마트 TV', '삼성(2016년 이후), LG webOS, Roku, Google TV, Android TV, Fire TV, Apple TV(베타)', '앱마다 달라요'],
        ['구형 TV용 적외선', '적외선 송신기가 있는 Android 스마트폰에서 무료(신규)', '일부 앱만, 적외선 송신기가 있는 스마트폰에서만'],
        ['Bluetooth', 'Android 9 이상 베타, 무료', '앱마다 달라요'],
        ['TV로 사진과 동영상 보내기', 'Pro, Wi-Fi로(미러링 아님)', '앱마다 달라요'],
        ['스마트폰과 컴퓨터', 'iPhone, iPad, Mac, Windows, 그리고 얼리 액세스의 Android', '앱마다 달라요'],
        ['화면 미러링', 'iPhone, iPad, Windows에서 각 기기의 내장 기능으로 무료예요. Windows에서는 Pro로 PC 화면을 LG, 삼성, Hisense, Android TV에도 미러링할 수 있어요(베타)', '일부 앱이 제공해요'],
      ],
      nota='Mando TV는 특정 앱과 비교하지 않아요. 최신 가격은 각 앱의 스토어 페이지에서 확인하세요.'),
    extra=[
      ('Mando TV가 하지 않는 것', 'iPhone과 iPad에서는 AirPlay가 되는 TV에서 쓰는 iPhone 자체 기능인 제어 센터의 화면 미러링으로 안내해 드려요. Windows에서는 전송(Windows + K)을 열어 주고, Mando TV Pro는 집 Wi-Fi로 PC 화면을 LG, 삼성, Hisense, Android TV로 보낼 수 있어요(베타, 몇 초 지연되고 소리는 나오지 않아요). Mando TV Pro로는 Wi-Fi로 TV에 사진과 동영상을 보낼 수도 있어요. 집 Wi-Fi로 스마트 TV를 조작해요. 스마트 기능이 없는 TV는 적외선 송신기가 있는 Android 스마트폰으로 적외선 조작을 할 수 있어요. Android 9 이상이라면 스마트폰이 Bluetooth 키보드이자 리모컨으로 Google TV, Android TV, Fire TV에 Wi-Fi 없이 연결할 수도 있어요. 이 옵션은 베타이고 무료예요.'),
      ('Mando TV가 수익을 내는 방법', '광고로도, 내 데이터로도 아니에요. 앱은 데이터를 수집하지 않아요. Mando TV는 추가 기능을 위한 선택 사항인 Pro를 한 번 결제하는 것으로 운영돼요. 기본 리모컨은 무료예요.'),
      ('이미 가지고 있는 기기에서', 'iPhone, iPad, Mac은 App Store, Windows PC는 Microsoft Store, Android는 Google Play의 무료 얼리 액세스예요. [iPhone용 리모컨 앱](@iphone)과 [Windows용 리모컨 앱](@windows)을 보세요.'),
      ('개인정보', '앱에는 계정도 추적도 없어요. TV와의 통신은 로컬 네트워크에서만 이루어지고, 연결 정보는 내 기기에 암호화되어 저장돼요. 자세한 내용은 [개인정보처리방침](@privacidad)에 있어요.'),
    ],
    marca=None,
    faq=[
      ('구독 없는 리모컨 앱이 있나요?', '네. Mando TV는 구독이 전혀 없어요. 리모컨은 무료에 광고가 없고, Pro는 선택 사항으로 한 번만 결제해요.'),
      ('Mando TV는 정말 무료인가요?', '네. 방향키, 확인, 뒤로, 홈, 볼륨, 채널, 숫자, 키보드, 전원 켜기와 끄기는 무료이고 광고도 시간 제한도 없어요.'),
      ('Wi-Fi 없이도 되나요?', '대부분은 안 돼요. Mando TV는 집 Wi-Fi로 스마트 TV를 조작해요. 예외가 있어요. 적외선 송신기가 있는 Android 스마트폰의 적외선은 스마트 기능이 없거나 Wi-Fi에 연결되지 않은 TV에서도 되고, Bluetooth는 Android 9 이상 베타에서 Google TV, Android TV, Fire TV에 쓸 수 있어요.'),
    ]),
  dict(clave='roku-app-alt', corto='Roku 앱 대안', fecha='2026-11-23',
    titulo='Roku 앱 대안: 간단한 Roku 리모컨',
    desc='Roku 앱 대신 쓸 리모컨: Mando TV는 계정과 광고 없이 Wi-Fi로 Roku TV와 플레이어를 조작하고, 삼성, LG, Google TV도 함께 조작해요.',
    h1='Roku 앱 대안: 모든 TV를 하나로',
    intro='공식 Roku 앱은 채널 스토어, 캐스팅, 프라이빗 리스닝, 리모컨까지 많은 걸 해요. 빠른 리모컨만 필요하거나 집에 삼성, LG, Google TV도 있다면 Mando TV가 계정 없이 Wi-Fi로 Roku를 조작하는 간단한 대안이에요.',
    pasos=[
      '스마트폰과 Roku를 같은 Wi-Fi에 연결하세요.',
      'Mando TV를 받아서 여세요. 목록에 Roku TV나 Roku 플레이어가 나타나요. 눌러 주세요. Roku는 코드를 묻지 않아요.',
      '방향키, 확인, 뒤로, 홈, 볼륨, 키보드를 쓰세요. Roku 채널의 검색어는 스마트폰 키보드로 입력하세요.',
      '버튼이 반응하지 않으면 Roku에서 설정 > 시스템 > 고급 시스템 설정 > 모바일 앱으로 제어로 들어가 네트워크 액세스를 기본 또는 Permissive로 바꾸세요(최신 Roku 소프트웨어에서는 모바일 앱으로 제어를 활성화로 두세요).',
      '선택 사항: Roku TV의 설정 > 시스템 > 전원에서 “TV 빠른 시작”을 활성화하면 Mando TV가 TV를 켤 수 있어요.',
    ],
    extra=[
      ('Mando TV가 더 잘 맞는 경우', '앱 하나로 여러 TV를 쓸 수 있어요. Roku, 삼성, LG, Google TV, Android TV예요. 계정도 광고도 없어요. Windows PC에서도 쓸 수 있어서 책상에서 편해요. 방향키와 볼륨이 빠르게 반응하고, 키보드로 검색어를 쉽게 입력해요.'),
      ('공식 Roku 앱이 더 나은 경우', '리모컨 외에 Roku 앱이 주는 기능, 예를 들어 Roku 채널 스토어에서 채널을 찾고 추가하는 일이나 자체 캐스팅, 프라이빗 리스닝(스마트폰에 연결한 이어폰으로 듣기)을 위해서는 Roku 앱을 그대로 두세요. 원하면 둘 다 쓰세요. 한 스마트폰에서 같이 쓸 수 있어요.'),
      ('Roku TV 기기와 Roku 플레이어', '둘 다 쓸 수 있어요. TCL, Hisense, Philips 등의 Roku TV 모델과 Roku Express, Streaming Stick, Ultra가 포함돼요. 자세한 내용은 [Roku 리모컨 앱 페이지](@roku)에 있어요.'),
      ('Roku 앱이 더 이상 작동하지 않을 때', '버튼이 반응하지 않는다면 대부분 Roku가 앱 제어를 막고 있어요. [Roku 앱이 작동하지 않을 때](@roku-403) 가이드에 문제를 해결하는 설정이 나와 있어요.'),
      ('무료와 Pro', '방향키, 확인, 뒤로, 홈, 볼륨, 채널, 숫자 버튼, 키보드, 앱 열기, 입력 바꾸기, 전원 켜기와 끄기는 무료이고 광고도 구독도 없어요. 터치패드, 음성 명령, 즐겨찾기 앱, 루틴, 취침 타이머는 구독 없이 한 번만 결제하는 Mando TV Pro에 포함돼요.'),
    ],
    marca='roku',
    faq=[
      ('Mando TV를 쓰려면 Roku 계정이 필요한가요?', '아니요. Mando TV는 집 네트워크로 Roku와 통신하고 계정을 요구하지 않아요.'),
      ('Mando TV가 Roku 모바일 앱을 완전히 대신하나요?', '리모컨으로는 그래요. 채널 스토어, 캐스팅, 프라이빗 리스닝은 공식 Roku 앱을 그대로 쓰세요.'),
      ('Roku Express나 Streaming Stick에서도 되나요?', '네. 모든 Roku 플레이어와 Roku TV 기기를 같은 방식으로 조작해요.'),
    ]),
  dict(clave='lg-thinq', corto='LG ThinQ 앱 대안', fecha='2026-11-23',
    titulo='LG ThinQ 앱 대안: 계정 없는 LG 리모컨',
    desc='리모컨 용도로만 쓸 LG ThinQ 앱 대안을 찾으시나요? Mando TV는 LG 계정과 광고 없이 Wi-Fi로 webOS LG TV를 조작해요.',
    h1='내 LG TV를 위한 LG ThinQ 앱 대안',
    intro='LG ThinQ는 가전과 TV 등 집 전체를 아우르는 LG의 공식 앱이에요. LG TV용 간단한 리모컨만 필요하다면 Mando TV가 LG 계정을 만들 필요 없이, 광고도 없이 집 Wi-Fi로 그 일을 해 줘요.',
    pasos=[
      '스마트폰이나 PC(iPhone, Android, Windows)와 LG TV를 같은 Wi-Fi에 연결하세요.',
      'Mando TV를 받아서 여세요. 목록에 LG TV가 저절로 나타나요. 눌러 주세요.',
      'TV에 허용 창이 떠요. TV 리모컨이나 화면 아래의 조이스틱, 매직 리모컨으로 한 번 허용해 주세요.',
      '버튼, 볼륨, 키보드를 바로 쓸 수 있어요. LG 계정도 필요 없고 TV를 등록하지 않아도 돼요.',
      '선택 사항: TV 설정에서 “모바일 기기로 TV 켜기”를 활성화하면 스마트폰으로 TV를 켤 수도 있어요.',
    ],
    extra=[
      ('Mando TV와 LG ThinQ, 무엇에 쓰나요', '세탁기, 냉장고, 에어컨 같은 LG 가전을 관리하거나 LG 계정 기능이 필요하다면 ThinQ를 쓰세요. TV용 빠르고 간단한 리모컨이 필요하거나 같은 앱으로 삼성, Roku, Google TV까지 쓰고 싶다면 Mando TV를 쓰세요. 많은 분이 둘 다 써요. 가전은 ThinQ로, TV는 Mando TV로요.'),
      ('LG TV에서 Mando TV가 하는 일', 'webOS가 탑재된 LG 스마트 TV, 즉 2014년 이후 대부분의 모델에서 쓸 수 있고 LED, 나노셀, QNED, OLED가 포함돼요. 방향키, 확인, 뒤로, 홈, 볼륨, 채널, 음소거, 재생 조작, 그리고 YouTube, Netflix, 브라우저에 입력할 키보드를 쓸 수 있어요. 앱 목록과 입력 목록도 무료예요. Pro에서는 매직 리모컨 같은 포인터도 더해져요.'),
      ('Mando TV가 하지 않는 것', 'LG 가전은 조작하지 않고, LG 계정을 쓰지 않으며, TV에 있는 LG 계정 서비스를 대신하지도 않아요. 리모컨이지 스마트홈 허브가 아니에요.'),
      ('개인정보와 광고', 'Mando TV에는 광고도 계정도 없어요. 집 네트워크 안에서만 TV와 통신하고 연결 키를 내 기기에 암호화해서 저장해요. 모든 기능은 [LG 리모컨 앱](@lg) 페이지에서 볼 수 있어요.'),
      ('무료와 Pro', '방향키, 확인, 뒤로, 홈, 볼륨, 채널, 숫자 버튼, 키보드, 앱 열기, 입력 바꾸기, 전원 켜기와 끄기는 무료이고 광고도 구독도 없어요. 터치패드, 음성 명령, 즐겨찾기 앱, 루틴, 취침 타이머는 구독 없이 한 번만 결제하는 Mando TV Pro에 포함돼요.'),
    ],
    marca='lg',
    faq=[
      ('LG ThinQ 앱 없이 LG TV를 조작할 수 있나요?', '네. Mando TV는 집 Wi-Fi로 webOS가 탑재된 LG TV에 바로 연결해요. TV에서 허용 창을 한 번 누르면 끝이고 LG 계정은 필요 없어요.'),
      ('Mando TV에도 LG 매직 리모컨 같은 포인터가 있나요?', 'Mando TV Pro에는 스마트폰 화면에서 손가락으로 움직이는 포인터가 있어요. 매직 리모컨이 화살표를 움직이는 것과 비슷해요.'),
      ('Mando TV는 LG에서 만든 앱인가요?', '아니요. Mando TV는 독립적으로 만든 앱이고 LG와 관련이 없어요. LG와 ThinQ는 각 소유자의 것이며 호환 여부를 설명하려는 목적으로만 언급돼요.'),
    ]),
  dict(clave='smartthings', corto='SmartThings 대안', fecha='2026-11-23',
    titulo='SmartThings가 안 되나요? 삼성용 간단한 대안',
    desc='SmartThings가 느리거나 오류가 나나요? Mando TV는 Wi-Fi로 Tizen 삼성 TV를 바로 조작해요. 삼성 계정도 광고도 없어요. 단계별 안내.',
    h1='삼성 TV를 위한 SmartThings 대안',
    intro='SmartThings는 집 전체를 아우르는 삼성의 앱이고, 리모컨 기능은 삼성 계정을 통해 작동해요. 앱이 안 되거나 빠른 방법이 필요하다면 Mando TV가 Tizen이 탑재된 2016년 이후의 삼성 TV를 계정 없이 집 Wi-Fi로 바로 조작해요.',
    pasos=[
      '스마트폰과 삼성 TV를 같은 Wi-Fi에 연결하세요.',
      'Mando TV를 받아서 여세요. 목록에 삼성 TV가 저절로 나타나요. 눌러 주세요.',
      'TV가 연결을 허용할지 물어봐요. 리모컨이나 TV 본체의 버튼으로 “허용”을 선택하세요(처음 한 번만 해요).',
      '방향키, 확인, 뒤로, 홈, 볼륨, 채널, 키보드를 바로 쓰세요.',
      '선택 사항: 설정 > 일반 > 네트워크 > 전문가 설정에서 “모바일 기기로 켜기”를 활성화하면 Mando TV가 TV를 켤 수도 있어요.',
    ],
    extra=[
      ('스마트폰 리모컨이 더 이상 작동하지 않는 이유', '원인은 대부분 간단해요. 스마트폰과 TV가 서로 다른 Wi-Fi에 있거나, VPN이 켜져 있거나, TV가 깊은 대기 상태에 있어요. SmartThings는 삼성 계정에서 로그아웃된 경우처럼 계정 문제가 더해질 수 있어요. Mando TV는 집 네트워크 안의 TV와 바로 통신하고 로그인할 계정이 없어요. 더 많은 팁은 [스마트폰이 TV를 찾지 못할 때](@not-found)에 있어요.'),
      ('Mando TV와 SmartThings, 무엇에 쓰나요', '삼성 가전, 조명, 다른 스마트홈 기기나 삼성 계정 기능에 SmartThings를 쓰고 있다면 그대로 두세요. TV용 빠른 리모컨만 필요하거나 집에 LG, Roku, Google TV, Fire TV 기기도 있다면 Mando TV를 쓰세요. 앱 하나로 모두 조작해요. 두 앱을 한 스마트폰에 같이 설치할 수 있어요.'),
      ('실수로 허용을 거부했을 때', 'TV에서 설정 > 일반 > 외부 장치 관리자 > 장치 연결 관리자로 들어가 Mando TV를 허용으로 바꾸세요.'),
      ('리모컨이 없을 때', 'TV 본체의 버튼으로 허용 창을 확인할 수 있어요. [삼성 TV 리모컨 없이 스마트폰으로 쓰는 방법](@samsung-lost) 가이드에서 방법을 알려 드려요.'),
      ('무료와 Pro', '리모컨은 무료로 받아서 쓸 수 있고 광고도 구독도 없어요. Mando TV Pro는 추가 기능을 위한 선택 사항으로 한 번만 결제해요.'),
    ],
    marca='samsung',
    faq=[
      ('SmartThings 없이 삼성 TV를 조작할 수 있나요?', '네. Mando TV는 집 Wi-Fi로 Tizen이 탑재된 삼성 TV에 바로 연결해요. TV에서 연결을 한 번 허용하면 되고 삼성 계정은 필요 없어요.'),
      ('Mando TV가 삼성 가전도 조작하나요?', '아니요. TV용 리모컨일 뿐이에요. 가전과 다른 스마트홈 기기는 SmartThings를 그대로 쓰세요.'),
      ('Mando TV는 삼성에서 만든 앱인가요?', '아니요. Mando TV는 독립적으로 만든 앱이고 삼성과 관련이 없어요. 삼성과 SmartThings는 각 소유자의 것이며 호환 여부를 설명하려는 목적으로만 언급돼요.'),
    ]),
  dict(clave='googletv-alt', corto='Google TV 리모컨 대안', fecha='2026-11-23',
    titulo='Google TV 리모컨이 안 되나요? 대안이 있어요',
    desc='Google TV 스마트폰 리모컨이 TV를 찾지 못하나요? Mando TV는 Google 계정과 광고 없이 Wi-Fi로 Google TV와 Android TV를 조작해요.',
    h1='스마트폰용 Google TV 리모컨 대안',
    intro='Google TV와 Android TV의 스마트폰 리모컨은 Google 앱 안에 있고 Google 계정과 연결돼요. TV를 찾지 못하면 더 이상 진행할 수 없어요. Mando TV는 별도의 리모컨 앱이에요. 화면에 나오는 6자리 코드로 페어링하고, iPhone, Android 스마트폰, Windows PC에서 Google 계정 없이 작동해요.',
    pasos=[
      'TV를 켜고 스마트폰을 같은 Wi-Fi에 연결하세요.',
      'Mando TV를 받아서 여세요. 목록에서 Google TV나 Android TV를 누르세요.',
      'TV에 6자리 코드가 나와요. Mando TV에 입력하고 페어링을 누르세요.',
      '방향키, 확인, 뒤로, 홈, 볼륨, 키보드를 쓰세요. 어디에도 로그인할 필요가 없어요.',
      '선택 사항: TV 설정에서 Wake on LAN이나 “네트워크로 켜기”를 찾아 두면 앱이 TV를 켤 수도 있어요.',
    ],
    extra=[
      ('스마트폰 리모컨이 TV를 찾지 못하는 이유', '대개 네트워크 때문이에요. 스마트폰과 TV가 서로 다른 Wi-Fi에 있거나, VPN이 켜져 있거나, 게스트 네트워크가 기기끼리 분리하고 있어요. 모든 리모컨 앱에 해당하는 문제이니 먼저 해결하세요. 자세한 내용은 [스마트폰이 TV를 찾지 못할 때](@not-found)에 있어요.'),
      ('어떤 TV에서 되나요', 'Sony, TCL, Hisense, Philips, Sharp, Xiaomi, Toshiba 등의 Google TV와 Android TV, 그리고 Google TV가 탑재된 Chromecast, Google TV Streamer, Nvidia Shield예요. 모두 같은 방식으로 한 번만 화면의 코드로 페어링해요.'),
      ('Google 앱이 더 나은 경우', 'Google 앱은 볼 만한 콘텐츠를 찾는 데도 도움을 주고 내 시청 목록도 기억해요. 그런 용도로는 그대로 쓰세요. Mando TV는 리모컨일 뿐이고, 같은 앱으로 삼성, LG, Roku, Fire TV 기기도 조작하고 Windows PC에서도 조작할 수 있어요.'),
      ('예전 Android TV 리모컨 앱이 보이지 않을 때', 'Google은 스마트폰 리모컨을 예전 Android TV Remote Control 앱에서 Google TV 앱으로 옮겼어요. 독립된 리모컨을 찾고 있다면 Mando TV도 하나의 선택지예요.'),
      ('무료와 Pro', '리모컨은 무료로 받아서 쓸 수 있고 광고도 구독도 없어요. Mando TV Pro는 추가 기능을 위한 선택 사항으로 한 번만 결제해요.'),
    ],
    marca='android',
    faq=[
      ('Mando TV를 Google TV에서 쓰려면 Google 계정이 필요한가요?', '아니요. TV에 나오는 코드만으로 페어링이 돼요.'),
      ('Google TV가 탑재된 Chromecast에서도 되나요?', '네. 화면에 나오는 6자리 코드로 똑같이 페어링해요.'),
      ('iPhone에서도 쓸 수 있나요?', '네. Mando TV는 iPhone과 iPad는 App Store에서, Windows는 Microsoft Store에서, Android는 Google Play의 무료 얼리 액세스로 받을 수 있어요.'),
    ]),
  dict(clave='windows', corto='Windows PC용 리모컨', fecha='2026-11-23',
    titulo='Windows용 리모컨 앱: PC로 TV 조작하기',
    desc='Mando TV로 Windows PC에서 삼성, LG, Roku, Google TV, Fire TV를 조작하세요. 단축키, 미니 리모컨, Wi-Fi 지원. Microsoft Store에 있어요.',
    h1='Windows PC용 리모컨 앱',
    intro='Mando TV에는 집 네트워크를 통해 PC나 노트북을 TV 리모컨으로 바꿔 주는 Windows 앱이 있어요. 실제 키보드로 TV에 입력하고, 일하는 동안 작은 리모컨 창을 맨 위에 두고, 같은 앱으로 삼성, LG, Roku, Google TV, Fire TV를 조작하세요.',
    pasos=[
      'Windows 10 또는 11 PC에서 Microsoft Store로 Mando TV를 무료로 설치하세요.',
      'PC와 TV가 같은 네트워크에 있는지 확인하세요. Wi-Fi든 랜선이든 같은 공유기에 연결되어 있으면 돼요.',
      'Mando TV를 열면 목록에 TV가 나타나요. 클릭하세요.',
      'TV가 물으면 허용 창을 확인하세요(LG, 삼성). 아니면 화면에 나온 코드를 입력하세요(Google TV, Fire TV).',
      '버튼을 클릭하거나 키보드로 검색어를 입력하세요. 끝났어요.',
    ],
    extra=[
      ('단축키(Pro)', 'Pro를 쓰면 PC 키보드가 리모컨이 돼요. 방향키로 이동하고, Enter는 확인, Backspace나 Esc는 뒤로, 더하기와 빼기는 볼륨, M은 음소거, 스페이스바는 일시정지예요.'),
      ('미니 리모컨(Pro)', '다른 모든 창 위에 머무는 작은 리모컨 창이에요. 하던 일을 멈추지 않고 볼륨을 바꾸거나 일시정지할 수 있어요.'),
      ('PC에서 TV에 입력하기', 'TV의 화면 키보드는 느려요. Mando TV에서는 실제 키보드로 입력하면 글자가 TV의 검색창에 들어가요. 이 기능은 무료예요.'),
      ('더 많은 정보', '단계별 안내는 [PC로 TV 조작하기](@pc)에 있어요. 스마트폰은 [Wi-Fi로 스마트폰을 리모컨으로 쓰기](@wifi)를 읽어 보세요.'),
      ('무료와 Pro', '방향키, 확인, 뒤로, 홈, 볼륨, 채널, 숫자 버튼, 키보드, 앱 열기, 입력 바꾸기, 전원 켜기와 끄기는 무료이고 광고도 구독도 없어요. 터치패드, 음성 명령, 즐겨찾기 앱, 루틴, 취침 타이머는 구독 없이 한 번만 결제하는 Mando TV Pro에 포함돼요. Windows에서는 Microsoft Store로 Pro를 구매해요.'),
      ('PC에서 음성 명령하기(Pro)', 'Pro로 PC 마이크를 통해 TV에 말할 수 있어요. 음성은 PC 안에서 바로 인식해요. 인터넷이 필요 없고 Windows에서 따로 설정할 것도 없어요. 말한 내용은 PC 밖으로 나가지 않고 저장되지도 않아요. 아주 오래된 프로세서에서만 앱이 Windows 음성 입력으로 대신해요. 이때는 개인정보 설정에서 온라인 음성 인식을 켜고 Windows에 내 언어를 추가해 두어야 해요.'),
    ],
    marca=None,
    faq=[
      ('Windows용 리모컨 앱에 Bluetooth나 케이블이 필요한가요?', '아니요. 집 네트워크를 써요. PC와 TV가 같은 공유기에 연결되어 있기만 하면 돼요.'),
      ('Windows에서 어떤 TV를 조작할 수 있나요?', 'Tizen이 탑재된 삼성 TV, webOS가 탑재된 LG TV, Roku TV와 플레이어, Google TV와 Android TV, Fire TV예요.'),
      ('PC에서 TV 화면을 보거나 PC 스피커로 들을 수 있나요?', '아니요. Mando TV는 리모컨일 뿐이에요. TV 화면을 컴퓨터로 미러링하거나 스트리밍하지 않아요.'),
      ('Windows PC에서 음성이 작동하지 않는 이유는 무엇인가요?', '음성 조작은 Pro 기능이에요. 먼저 Pro가 활성화되어 있는지, PC 마이크가 작동하는지 확인하세요. 대부분의 PC에서는 음성을 PC 안에서 인터넷 없이 인식해요. 아주 오래된 프로세서에서만 앱이 Windows 음성 입력을 써요. 이때는 Windows 개인정보 설정에서 온라인 음성 인식을 켜고 언어 설정에 내 언어를 추가하세요.'),
    ]),
  dict(clave='iphone', corto='iPhone용 리모컨 앱', fecha='2026-11-23',
    titulo='iPhone용 리모컨 앱: 삼성, LG, Roku, Google TV',
    desc='iPhone을 Wi-Fi로 삼성, LG, Roku, Google TV, Fire TV 리모컨으로 쓰세요. App Store에서 무료이고 계정도 광고도 없어요.',
    h1='iPhone용 리모컨 앱: 모든 TV를 하나로',
    intro='Mando TV는 집 Wi-Fi를 통해 iPhone이나 iPad를 삼성, LG, Roku, Google TV, Android TV, Fire TV의 리모컨으로 바꿔 줘요. App Store에서 무료이고 계정도 광고도 없어요. Android와 Windows에서도 쓸 수 있어요.',
    pasos=[
      'App Store에서 Mando TV를 무료로 받으세요.',
      'iPhone과 TV를 같은 Wi-Fi에 연결하세요.',
      'Mando TV를 열고, iOS가 로컬 네트워크 접근을 물으면 허용을 누르세요. TV를 찾는 데 필요해요.',
      '목록에서 TV를 누르세요. TV가 물으면 TV의 허용 창을 확인하거나(LG와 삼성), TV에 나온 코드를 입력하세요(Google TV나 Fire TV).',
      '버튼, 볼륨, 키보드를 쓰세요. 연결됐어요.',
    ],
    extra=[
      ('이런 TV에서 작동해요', 'LG webOS, 삼성 Tizen(2016년 이후), Roku TV와 Roku 플레이어, Google TV와 Android TV, Fire TV예요. 브랜드별 페이지는 [삼성](@samsung), [LG](@lg), [Roku](@roku), [Android TV](@android)예요.'),
      ('왜 로컬 네트워크를 묻나요', 'iPhone은 허용하지 않으면 앱이 집 네트워크의 기기에 접근하지 못하게 막아요. TV가 목록에 나타나지 않으면 설정 > Mando TV를 열고 “로컬 네트워크”를 활성화하세요. 앱은 집 네트워크 안의 내 TV하고만 통신해요.'),
      ('제조사 앱이 아니라 Mando TV를 쓰는 이유', 'TV 브랜드마다 자체 앱이 있고 각자의 설정이나 계정을 원해요. Mando TV는 계정 없이 모두를 위한 앱 하나예요.'),
      ('iPhone에서의 무료와 Pro', '방향키, 확인, 뒤로, 홈, 볼륨, 채널, 숫자 버튼, 키보드, 앱 열기, 입력 바꾸기, 전원 켜기와 끄기는 무료이고 광고도 구독도 없어요. 터치패드, 음성 명령, 즐겨찾기 앱, 루틴, 취침 타이머는 구독 없이 한 번만 결제하는 Mando TV Pro에 포함돼요. Pro는 앱 안에서 한 번만 결제해요.'),
    ],
    marca=None,
    faq=[
      ('iPhone에서 Mando TV는 무료인가요?', '다운로드는 무료이고 광고가 없어요. 기본 리모컨은 무료이고 앱 열기와 입력 바꾸기도 무료예요. 터치패드, 음성 명령, 루틴 같은 추가 기능은 한 번만 결제하는 Mando TV Pro에 포함돼요.'),
      ('iPad에서도 되나요?', '네. 같은 앱이 iPhone과 iPad에서 작동해요.'),
      ('iPhone용 리모컨 앱에 Bluetooth나 적외선 송신기가 필요한가요?', 'iPhone에서는 필요 없어요. iPhone에는 적외선 송신기가 없어서 적외선 조작은 쓸 수 없고, Bluetooth 옵션은 Android 9 이상에만 있고 iPhone에는 없어요. iPhone에서 Mando TV는 집 Wi-Fi로 스마트 TV와 Apple TV(베타)를 조작해요.'),
    ]),
  dict(clave='firetv', corto='Fire TV 리모컨', fecha='2026-11-23',
    titulo='스마트폰과 PC용 Fire TV 리모컨 앱',
    desc='스마트폰으로 쓰는 Fire TV 리모컨: Wi-Fi로 Fire TV Stick, Fire TV Cube, Fire TV 내장 TV를 조작해요. 4자리 PIN으로 연결하고 Amazon 앱은 필요 없어요.',
    h1='스마트폰이나 PC로 쓰는 Fire TV 리모컨',
    intro='Fire TV 리모컨이 없어졌거나 배터리가 다 됐다면 Mando TV가 Wi-Fi로 Fire TV Stick, Fire TV Cube, Fire TV가 내장된 TV를 조작해요. 4자리 PIN으로 연결해요. Fire TV는 Mando TV에서 새로 지원하는 기능이니 먼저 앱을 업데이트하세요.',
    pasos=[
      'App Store, Microsoft Store, Google Play에서 Mando TV를 최신 버전으로 업데이트하세요.',
      'Fire TV를 켜고 스마트폰을 같은 Wi-Fi에 연결하세요.',
      'Mando TV를 열면 목록에 Fire TV가 나타나요. 눌러 주세요.',
      'TV 화면에 4자리 PIN이 나와요. Mando TV에 입력하세요. 한 번만 하면 돼요.',
      '방향키, 확인, 뒤로, 홈, 재생 버튼, 검색용 키보드를 쓰세요.',
    ],
    extra=[
      ('지원하는 Fire TV 기기', 'Fire TV Stick, Fire TV Stick 4K, Fire TV Cube, Fire TV가 내장된 TV(Amazon Fire TV Edition TV와 일부 Hisense 모델 등)예요. 지원은 새로 시작했고 지금까지 실제 기기를 몇 대만 시험해 봤어요. 기대한 대로 작동하지 않으면 도움말 페이지로 모델명을 알려 주세요.'),
      ('Fire TV 켜기', 'Mando TV는 네트워크로 Fire TV를 켜지 않아요. TV 본체의 전원 버튼으로 TV를 켜세요. 꽂혀 있는 Fire TV Stick이나 Cube는 대개 HDMI-CEC로 깨어나고, Fire TV 내장 TV는 TV 자체가 Fire TV예요. 그다음부터는 스마트폰으로 조작하세요.'),
      ('Fire TV가 나타나지 않을 때', '두 기기가 같은 Wi-Fi에 있는지, Fire TV가 깨어 있는지 확인하세요. iPhone이라면 설정에서 Mando TV의 “로컬 네트워크”를 허용하세요. [스마트폰이 TV를 찾지 못할 때](@not-found)를 보세요.'),
      ('리모컨이 전혀 없을 때', 'Fire TV는 화면에 PIN을 보여 줘야 해요. 그래서 TV와 Fire TV가 켜져 있고 화면이 나와야 해요. TV가 엉뚱한 입력에 있다면 TV 본체의 버튼으로 바꾸세요. [리모컨 없이 입력 바꾸기](@hdmi)를 보세요.'),
      ('무료와 Pro', '방향키, 확인, 뒤로, 홈, 볼륨, 채널, 숫자, 키보드, 앱 열기, 입력 바꾸기, 전원 켜기와 끄기는 무료이고 광고도 구독도 없어요. 터치패드, 음성 명령, 즐겨찾기 앱, 루틴, 취침 타이머는 구독 없이 한 번만 결제하는 Mando TV Pro에 포함돼요.'),
    ],
    marca=None,
    faq=[
      ('Amazon Fire TV 앱이 필요한가요?', '아니요. Mando TV는 집 Wi-Fi로 PIN을 써서 Fire TV에 연결해요. 스마트폰에 Amazon 계정이 필요 없어요.'),
      ('Fire TV가 내장된 TV와 Fire TV Stick에서 모두 되나요?', '네, 바로 그 용도로 만들었어요. 지원이 새로 시작했으니 앱을 최신으로 유지하고, 기대한 대로 작동하지 않는 모델은 알려 주세요.'),
      ('왜 PIN이 필요한가요?', 'Fire TV는 내가 TV 앞에 있다는 것을 확인하려고 4자리 PIN을 보여 줘요. 화면을 보지 못하면 아무도 페어링할 수 없어요.'),
    ]),
  dict(clave='firetv-lost', corto='Fire TV 리모컨 분실', fecha='2026-11-23',
    titulo='Fire TV 리모컨을 잃어버렸나요? 스마트폰으로 쓰세요',
    desc='Fire TV Stick 리모컨을 잃어버렸나요? 4자리 PIN으로 연결해 스마트폰으로 Wi-Fi 조작하세요. 새 Wi-Fi와 HDMI-CEC 요령도 알려 드려요.',
    h1='Fire TV 리모컨을 잃어버렸을 때 스마트폰으로 쓰는 방법',
    intro='Fire TV Stick, Fire TV Cube, Fire TV 탑재 스마트 TV의 리모컨을 잃어버렸거나 더 이상 작동하지 않아도 Fire TV가 아직 내 Wi-Fi에 연결되어 있다면 스마트폰이 대신해 줘요. 연결은 화면에 나오는 4자리 PIN으로 하니까 예전 리모컨이 전혀 필요 없어요.',
    pasos=[
      'TV 본체의 버튼으로 TV를 켜세요. 꽂혀 있는 Fire TV Stick이나 Cube는 대개 함께 깨어나요. HDMI-CEC가 활성화되어 있으면 TV가 자동으로 그 입력으로 바뀔 때가 많아요.',
      'TV가 다른 입력을 보여 주고 있다면 TV 본체의 입력 또는 소스 버튼으로 바꾸세요. [리모컨 없이 입력 바꾸기](@hdmi)를 보세요.',
      '스마트폰을 Fire TV와 같은 Wi-Fi에 연결하세요.',
      'Mando TV를 받아서 여세요. 목록에 Fire TV가 나타나요. 눌러 주세요.',
      'TV에 4자리 PIN이 나와요. Mando TV에 입력하세요. 한 번만 하면 돼요.',
      '방향키, 확인, 뒤로, 홈, 볼륨, 재생 버튼, 스마트폰 키보드를 쓰세요.',
    ],
    extra=[
      ('먼저 TV 리모컨을 시험해 보세요(HDMI-CEC)', '많은 TV 리모컨이 HDMI-CEC로 Fire TV Stick을 조작할 수 있어요. Fire TV 화면이 보이면 TV 리모컨의 방향키와 확인을 눌러 보세요. 아무 일도 없으면 TV 설정에서 CEC를 활성화하고(삼성은 Anynet+, LG는 SIMPLINK, Sony는 BRAVIA Sync) Fire TV의 디스플레이 설정(“디스플레이 및 사운드”)에서 HDMI-CEC 기기 제어를 켜세요.'),
      ('Wi-Fi를 바꿨을 때', '리모컨이 없으면 Fire TV에 새 Wi-Fi 비밀번호를 입력할 수 없지만 방법이 있어요. 다른 스마트폰에서 예전 Wi-Fi와 이름과 비밀번호가 똑같은 핫스팟을 만드세요. Fire TV가 자동으로 연결돼요. Mando TV를 쓰는 스마트폰을 그 핫스팟에 연결해 PIN으로 페어링하고, Fire TV에서 설정 > 네트워크로 가서 새 Wi-Fi를 선택하세요. 마지막으로 스마트폰도 새 Wi-Fi에 연결하세요.'),
      ('교체용 리모컨 페어링하기', '대부분의 새 Fire TV 리모컨은 Fire TV 가까이에서 홈 버튼을 약 10초 동안 누르고 있으면 페어링돼요. 안 되면 설정 > 컨트롤러 및 Bluetooth 기기 > Amazon Fire TV 리모컨 > 새 리모컨 추가를 여세요. 이 메뉴는 Mando TV로 스마트폰에서도 열 수 있어요.'),
      ('TV에 Fire TV가 내장된 경우', 'Insignia와 Toshiba의 여러 모델처럼 Fire TV가 내장된 TV도 TV 자체가 Fire TV이므로 같은 단계로 하면 돼요.'),
      ('시작하기 전에', 'Fire TV 지원은 Mando TV에서 새로 시작했어요. 먼저 앱을 업데이트하세요. 내 모델이 기대한 대로 반응하지 않으면 [도움말 페이지](@soporte)로 모델명을 알려 주세요.'),
      ('무료와 Pro', '리모컨은 무료로 받아서 쓸 수 있고 광고도 구독도 없어요. Mando TV Pro는 추가 기능을 위한 선택 사항으로 한 번만 결제해요.'),
    ],
    marca=('firetv', 'Fire TV 리모컨'),
    faq=[
      ('리모컨 없이 스마트폰으로 Fire TV Stick을 조작할 수 있나요?', '네, Fire TV가 켜져 있고 내 Wi-Fi에 연결되어 있다면요. Mando TV는 TV에 나오는 4자리 PIN으로 페어링하니까 예전 리모컨이 필요 없어요.'),
      ('Fire TV가 새 Wi-Fi에 있어도 되나요?', '바로는 안 돼요. 스마트폰과 Fire TV가 같은 네트워크에 있어야 하거든요. 먼저 이 페이지의 핫스팟 요령으로 Fire TV를 다시 온라인으로 만드세요.'),
      ('Amazon Fire TV 앱이나 Amazon 계정이 필요한가요?', '아니요. Mando TV는 집 네트워크로 PIN을 써서 연결하고 별도의 계정이 필요 없어요.'),
    ]),
  dict(clave='turn-on', corto='리모컨 없이 TV 켜기', fecha='2026-11-23',
    titulo='리모컨 없이 TV 켜기 (모든 브랜드)',
    desc='리모컨 없이 TV 켜기: 삼성, LG, TCL, Hisense, Sony, Vizio의 전원 버튼 위치. HDMI-CEC와 스마트폰으로 켜는 요령도 알려 드려요.',
    h1='리모컨 없이 TV 켜는 방법',
    intro='거의 모든 TV에는 아직 물리적인 전원 버튼이 있어요. 잘 숨어 있을 뿐이에요. 브랜드별로 어디에 있는지, 그리고 다음에는 찾지 않아도 되는 두 가지 방법을 알려 드릴게요. 게임기나 스트리밍 기기의 HDMI-CEC, 그리고 스마트폰으로 Wi-Fi를 통해 TV를 켜는 방법이에요.',
    pasos=[
      '화면 아래쪽 가운데, 브랜드 로고 바로 뒤를 보세요. 많은 TV에 아래를 향한 작은 버튼 하나나 조이스틱이 있어요.',
      '거기에 없다면 TV 뒷면의 아래쪽 모서리 근처를 더듬어 보고, 그다음 왼쪽과 오른쪽 가장자리를 살펴보세요.',
      '버튼을 한 번 누르세요. 버튼이 하나뿐인 많은 TV는 켜져 있을 때 짧게 누르면 입력과 볼륨을 위한 작은 메뉴가 열리고, 길게 누르면 꺼져요.',
      '그래도 반응이 없나요? 전원 코드를 양쪽 끝에서 확인하고 다른 콘센트에 꽂아 보세요. 대기 표시등이 켜지지 않으면 TV에 전기가 들어오지 않는 거예요.',
      'TV가 켜지면 이제 버튼이 필요 없도록 설정해 두세요. HDMI-CEC와 네트워크로 켜기를 활성화하세요. 둘 다 아래에서 설명해요.',
    ],
    extra=[
      ('브랜드별 전원 버튼 위치', '삼성: 화면 아래쪽 가운데의 컨트롤 버튼이나 조이스틱, 또는 뒷면 아래쪽 모서리예요. LG: 대부분의 모델에서 LG 로고 아래의 조이스틱 버튼이에요. TCL과 Hisense: 대개 화면 아래쪽 가운데의 작은 버튼이나 뒷면의 아래쪽 모서리 근처예요. Sony: 뒷면이나 가장자리, 아래쪽 테두리 가까이에 있어요. Vizio: 뒷면의 왼쪽 아래나 오른쪽 아래, 또는 옆면에 있어요. 위치는 모델마다 달라요. 찾지 못하면 뒷면 스티커의 모델 번호로 사용 설명서를 찾아보세요.'),
      ('게임기나 스트리밍 기기로 TV 켜기(HDMI-CEC)', 'HDMI-CEC가 활성화되어 있으면 PlayStation, Xbox, Roku 플레이어, Fire TV Stick, Chromecast를 켤 때 TV도 함께 켜지고 올바른 입력으로 바뀌어요. 브랜드마다 설정 이름이 달라요. 삼성은 Anynet+, LG는 SIMPLINK, Sony는 BRAVIA Sync, 대부분의 다른 브랜드는 CEC예요. 자세한 내용은 [리모컨 없이 TV를 켜고 게임기 HDMI로 바꾸기](@console)에 있어요.'),
      ('스마트폰으로 TV 켜기', '스마트 TV는 한 번 허용해 두면 Wi-Fi로 깨울 수 있고, 그러면 Mando TV가 스마트폰에서 켜 줘요. 삼성은 설정 > 일반 > 네트워크 > 전문가 설정에서 “모바일 기기로 켜기”를 활성화하세요. LG는 “모바일 기기로 TV 켜기”를 활성화하세요([단계별 안내](@lg-on)). Roku TV는 설정 > 시스템 > 전원에서 “TV 빠른 시작”을 활성화하세요. Google TV와 Android TV는 모델이 지원한다면 Wake on LAN이나 “네트워크로 켜기”를 찾아보세요. TV가 켜져 있을 때 한 번만 하면 돼요.'),
      ('버튼을 찾지 못할 때', '일부 최신 TV는 하나뿐인 버튼을 너무 잘 숨겨서 없는 것처럼 보여요. 화면 아래의 작은 돌출부나 조도 센서 부분을 찾아보세요. 버튼은 바로 옆에 있을 때가 많아요. Wi-Fi로 하려면 Mando TV에 TV가 한 번 켜진 상태로 연결되어 있어야 해요. 적외선은 예외예요. 적외선 송신기가 있는 Android 스마트폰에서는 TV를 향해 스마트폰을 겨누기만 하면 한 번도 설정하지 않은 TV도 Mando TV로 켤 수 있어요. 적외선은 새로 추가된 기능이고 앱의 코드 목록에 있는 브랜드에서 작동해요.'),
      ('무료와 Pro', '리모컨은 무료로 받아서 쓸 수 있고 광고도 구독도 없어요. Mando TV Pro는 추가 기능을 위한 선택 사항으로 한 번만 결제해요.'),
    ],
    marca=None,
    faq=[
      ('한 번도 설정하지 않은 TV를 스마트폰으로 켤 수 있나요?', 'Wi-Fi로는 안 돼요. 꺼진 TV는 네트워크로 켜기가 미리 활성화되어 있을 때만 네트워크에서 깨어나요. 처음에는 TV 본체의 버튼을 쓰세요. 예외는 적외선 송신기가 있는 Android 스마트폰이에요. 브랜드가 코드 목록에 있거나 “다른 브랜드 또는 모름”을 고르면 Mando TV가 설정하지 않은 TV도 적외선으로 켤 수 있어요.'),
      ('리모컨 없이 삼성 TV를 켜려면 어떻게 하나요?', '화면 아래쪽 가운데나 뒷면 아래쪽 모서리의 컨트롤 버튼을 누르세요. 그다음 “모바일 기기로 켜기”를 활성화하면 다음부터 스마트폰으로 켤 수 있어요.'),
      ('리모컨 없이 Roku TV를 켜려면 어떻게 하나요?', '보통 아래쪽 가운데나 뒷면에 있는 TV 본체의 버튼을 쓰세요. 그다음 설정 > 시스템 > 전원에서 “TV 빠른 시작”을 활성화하면 Mando TV가 스마트폰에서 켤 수 있어요.'),
      ('게임기를 켜면 왜 TV가 저절로 켜지나요?', 'HDMI-CEC 때문이에요. 편리한 기능이고, 원하지 않으면 TV 설정에서 끌 수 있어요.'),
    ]),
  dict(clave='sony', corto='Sony 리모컨', fecha='2026-11-23',
    titulo='스마트폰과 PC용 Sony 리모컨 앱',
    desc='Mando TV는 Wi-Fi로 Google TV나 Android TV가 탑재된 Sony Bravia TV를 조작해요. Android 없는 2013~2015년 모델은 베타로 지원해요.',
    h1='스마트폰으로 Sony TV 조작하는 방법',
    intro='최신 Sony Bravia 스마트 TV는 Google TV를 쓰고, 2015년 이후의 이전 모델은 Android TV를 써요. Mando TV는 iPhone, Android 스마트폰, Windows PC에서 Wi-Fi로 둘 다 조작해요. 리모컨을 잃어버렸거나 배터리가 다 됐을 때 앱이 원래 리모컨을 대신해 줘요.',
    pasos=[
      'Sony TV에 Google TV나 Android TV 홈 화면이 나오는지 확인하세요. 2015년 이후 출시된 대부분의 Sony Bravia 스마트 TV가 그래요.',
      '스마트폰과 TV를 같은 Wi-Fi에 연결하세요.',
      'Mando TV를 열고 목록에서 Sony TV를 누르세요.',
      'TV 화면에 나오는 6자리 코드를 입력하세요(처음 한 번만 해요). 리모컨은 필요 없어요.',
      '방향키, 확인, 뒤로, 홈, 볼륨, 키보드를 쓰세요.',
    ],
    extra=[
      ('스마트폰으로 Sony TV 켜기', 'Google TV나 Android TV가 탑재된 Sony 모델은 “Remote start”가 활성화되어 있으면 네트워크로 깨울 수 있어요. 이 옵션은 대개 설정 > 네트워크 및 인터넷 > Remote start에 있어요(모델에 따라 경로가 조금 다를 수 있어요). 그다음 TV가 꺼져 있을 때 Mando TV에서 TV를 누르면 앱이 켜 줘요.'),
      ('Sony TV의 전원 버튼 위치', '대부분의 Bravia TV는 뒷면의 왼쪽 또는 오른쪽 아래 모서리 근처나 가장자리에 있어요. 짧게 누르면 TV가 켜져요. 더 자세한 내용은 [리모컨 없이 TV 켜기](@turn-on)에 있어요.'),
      ('구형 Sony TV', 'Android를 쓰지 않는 2013~2015년의 Sony Bravia TV는 Mando TV에서 베타로 지원해요. 새로 추가된 기능이라 아직 매끄럽지 않은 부분이 있을 수 있어요. TV에 4자리 PIN이 나오고 앱에 입력해야 해요. Google TV나 Android TV가 없는 다른 Sony TV는 지금은 지원하지 않아요.'),
      ('무료와 Pro', '리모컨은 무료로 받아서 쓸 수 있고 광고도 구독도 없어요. Mando TV Pro는 추가 기능을 위한 선택 사항으로 한 번만 결제해요.'),
    ],
    marca='android',
    faq=[
      ('Mando TV가 Sony Bravia TV에서 작동하나요?', '네, Google TV나 Android TV를 쓰는 Sony TV에서 작동해요. 2015년 이후 출시된 대부분의 Sony 스마트 TV가 해당돼요.'),
      ('Sony 앱이나 Google 계정이 필요한가요?', '아니요. Mando TV는 TV 화면에 나오는 코드로 페어링하고 계정을 요구하지 않아요.'),
      ('Android가 없는 구형 Sony Bravia TV에서도 되나요?', '네, 베타로 Android가 없는 2013~2015년 Bravia 모델에서 작동해요. TV에 표시되는 4자리 PIN으로 페어링해요.'),
      ('Sony TV에 스마트폰으로 입력할 수 있나요?', '네. 키보드는 무료이고 YouTube, Netflix, TV 검색에서 쓸 수 있어요.'),
    ]),
  dict(clave='tcl', corto='TCL 리모컨', fecha='2026-11-23',
    titulo='스마트폰과 PC용 TCL 리모컨 앱',
    desc='TCL 리모컨을 잃어버렸나요? 대부분의 TCL TV는 Roku TV나 Google TV예요. Mando TV는 계정과 광고 없이 Wi-Fi로 둘 다 조작해요.',
    h1='스마트폰으로 TCL TV 조작하는 방법',
    intro='TCL이 TV를 만들지만 소프트웨어는 Roku TV나 Google TV(구형 모델은 Android TV)예요. Mando TV는 두 시스템을 모두 조작하고 Wi-Fi로 TCL TV의 리모컨 역할을 해요. 무료이고 계정도 광고도 없어요.',
    pasos=[
      'TCL이 어떤 시스템을 쓰는지 확인하세요. 홈 화면에 채널 타일이 단순한 격자로 나오면 Roku TV예요. 추천 콘텐츠 줄이 가득한 Google TV나 Android TV 같은 화면이면 Google TV예요.',
      '스마트폰과 TCL TV를 같은 Wi-Fi에 연결하세요.',
      'Mando TV를 열면 목록에 TCL이 저절로 나타나요. 눌러 주세요.',
      'Roku TV가 탑재된 TCL은 더 할 일이 없어요. Google TV가 탑재된 TCL은 TV 화면에 나오는 6자리 코드를 입력하세요(처음 한 번만 해요).',
      '방향키, 확인, 뒤로, 홈, 볼륨, 키보드를 쓰세요. 네트워크로 켜기를 활성화했다면(아래를 보세요) 앱으로 TV를 켜세요.',
    ],
    extra=[
      ('스마트폰으로 TCL TV 켜기', 'TCL Roku TV는 설정 > 시스템 > 전원에서 “TV 빠른 시작”을 활성화하세요. TCL Google TV는 네트워크나 전원 설정에서 Wake on LAN, “네트워크로 켜기”, 원격 시작 옵션을 찾으세요. 이를 지원하지 않는 모델도 있어요. 그럴 때는 대개 아래쪽 가운데나 뒷면에 있는 물리적인 전원 버튼으로 켜세요.'),
      ('TCL이 나타나지 않을 때', '스마트폰과 TV가 같은 Wi-Fi에 있는지 확인하세요. 2.4GHz와 5GHz 네트워크가 분리된 공유기는 기기를 서로 보이지 않게 할 수 있어요. iPhone이라면 설정에서 Mando TV의 “로컬 네트워크”를 허용하세요. TV의 IP 주소를 입력해서 추가할 수도 있어요. [스마트폰이 TV를 찾지 못할 때](@not-found)를 읽어 보세요.'),
      ('내 TCL에 대해 더 알아보기', 'Roku TV가 탑재된 TCL은 [Roku 리모컨 앱](@roku)을, Google TV나 Android TV가 탑재된 TCL은 [Android TV 리모컨 앱](@android)을 보세요.'),
      ('무료와 Pro', '방향키, 확인, 뒤로, 홈, 볼륨, 채널, 숫자, 키보드, 앱 열기, 입력 바꾸기, 전원 켜기와 끄기는 무료이고 광고도 구독도 없어요. 터치패드, 음성 명령, 즐겨찾기 앱, 루틴, 취침 타이머는 구독 없이 한 번만 결제하는 Mando TV Pro에 포함돼요.'),
    ],
    marca=None,
    faq=[
      ('Mando TV가 모든 TCL TV에서 작동하나요?', 'Roku TV, Google TV, Android TV가 탑재된 TCL TV에서 작동해요. 대부분의 TCL 스마트 TV가 해당돼요. 스마트 TV가 아닌 TCL은 Wi-Fi로 조작할 수 없어요.'),
      ('TCL 앱이나 TCL 계정이 필요한가요?', '아니요. Mando TV는 집 Wi-Fi로 바로 연결하고 계정이 필요 없어요.'),
      ('TCL이 코드를 물어봐요. 어디에 있나요?', 'Google TV와 Android TV가 탑재된 TCL 모델은 화면에 6자리 코드를 보여 줘요. 나온 그대로 Mando TV에 입력하세요. Roku TV가 탑재된 TCL은 코드를 묻지 않아요.'),
    ]),
  dict(clave='hisense', corto='Hisense 리모컨', fecha='2026-11-23',
    titulo='Hisense 리모컨 앱: 스마트폰에서 되는 것',
    desc='Mando TV로 쓰는 Hisense 리모컨: VIDAA, Roku TV, Google TV, Fire TV를 Wi-Fi로 조작해요. 되는 것을 솔직하게 정리했어요.',
    h1='Hisense 리모컨 앱: 되는 것과 안 되는 것',
    intro='Hisense TV는 속이 모두 같지 않아요. 모델에 따라 Hisense 자체 시스템인 VIDAA, Roku TV, Google TV, Fire TV 중 하나를 써요. Mando TV는 일부 최신 VIDAA 모델을 제외하고 이 네 시스템의 Hisense에서 모두 리모컨으로 쓸 수 있어요. 어떤 시스템인지 알아보는 방법과 기대할 수 있는 것을 알려 드릴게요.',
    pasos=[
      'Hisense가 어떤 시스템을 쓰는지 확인하세요. VIDAA는 Hisense의 자체 화면이에요. Roku TV는 채널 타일 격자가 보여요. Google TV는 추천 콘텐츠 줄이 보여요. Fire TV는 Amazon 줄이 있는 Fire TV 홈 화면이 보여요.',
      '스마트폰과 Hisense TV를 같은 Wi-Fi에 연결하세요.',
      'Mando TV를 열면 목록에 TV가 저절로 나타나요. 눌러 주세요.',
      'VIDAA와 Fire TV 모델은 4자리 PIN을 보여 줄 수 있고, Google TV는 6자리 코드를 보여 줘요. 앱에 입력하세요. Roku TV는 아무것도 묻지 않아요. 한 번만 하면 돼요.',
      '스마트폰으로 방향키, 확인, 뒤로, 홈, 볼륨, 키보드를 쓰세요.',
    ],
    extra=[
      ('Roku TV나 Google TV가 탑재된 Hisense', '다른 Roku TV나 Google TV와 똑같이 모두 작동해요. 자세한 내용은 [Roku 리모컨 앱](@roku)과 [Android TV 리모컨 앱](@android) 페이지에 있어요.'),
      ('Fire TV가 탑재된 Hisense', 'Fire TV 지원은 Mando TV에서 새로 시작했어요. 스토어에서 앱을 최신 버전으로 업데이트하세요. PIN 페어링 방법은 [Fire TV 리모컨 앱](@firetv) 페이지에 있어요. 기대한 대로 작동하지 않으면 도움말 페이지로 모델명을 알려 주세요.'),
      ('VIDAA가 탑재된 Hisense', '대부분의 VIDAA 모델에서 버튼, 볼륨, 키보드, 앱, 입력이 작동해요. 일부 최신 VIDAA 모델은 Hisense 공식 앱만 받아들여요. Mando TV는 연결할 때 이를 알아채고 조용히 실패하지 않고 분명하게 알려 줘요. 이럴 때는 내 모델용 Hisense 앱, TV 본체의 버튼, 원래 리모컨이 맞는 방법이에요.'),
      ('스마트폰으로 Hisense 켜기', 'Hisense Roku TV는 설정 > 시스템 > 전원에서 “TV 빠른 시작”을 활성화하세요. Google TV는 Wake on LAN이나 “네트워크로 켜기” 옵션을 찾으세요. 없다면 TV의 전원 버튼을 쓰세요.'),
      ('무료와 Pro', '방향키, 확인, 뒤로, 홈, 볼륨, 채널, 숫자 버튼, 키보드, 앱 열기, 입력 바꾸기, 전원 켜기와 끄기는 무료이고 광고도 구독도 없어요. 터치패드, 음성 명령, 즐겨찾기 앱, 루틴, 취침 타이머는 구독 없이 한 번만 결제하는 Mando TV Pro에 포함돼요.'),
    ],
    marca=None,
    faq=[
      ('Mando TV가 Hisense VIDAA에서 작동하나요?', '네, 대부분의 VIDAA 모델에서 작동해요. 일부 최신 모델은 Hisense 공식 앱만 받아들이는데, Mando TV가 이를 알아채고 알려 줘요. Roku TV, Google TV, Fire TV가 탑재된 Hisense TV도 지원해요.'),
      ('내 Hisense가 Roku TV인지 Google TV인지 Fire TV인지 어떻게 알아요?', '홈 화면을 보세요. Roku TV는 단순한 타일 격자이고 시작할 때 Roku 로고가 나와요. Google TV는 추천 콘텐츠 줄이 있어요. Fire TV는 Amazon Fire TV 홈 화면이에요. 설정 > 정보에서 모델명으로도 알 수 있어요.'),
      ('Hisense나 Google 계정이 필요한가요?', '아니요. Mando TV는 집 Wi-Fi로 바로 연결하고 자체 계정이 없어요.'),
    ]),
  dict(clave='philips', corto='Philips 리모컨', fecha='2026-11-23',
    titulo='Philips 리모컨 앱: Roku TV, Google TV, Android TV',
    desc='Mando TV는 Wi-Fi로 스마트폰이나 PC에서 Roku TV, Google TV, Android TV가 탑재된 Philips TV를 조작해요. Titan OS는 지원하지 않아요.',
    h1='스마트폰으로 Philips TV 조작하기',
    intro='Philips TV는 나라와 출시 연도에 따라 다른 시스템을 써요. 미국은 Roku TV, 많은 나라는 Google TV나 Android TV, 일부 최신 유럽 모델은 Titan OS예요. Mando TV는 Roku TV, Google TV, Android TV가 탑재된 모델을 Wi-Fi로 조작해요.',
    pasos=[
      '홈 화면을 확인하세요. Roku TV는 타일 격자가 보여요. Google TV와 Android TV는 Google의 추천 콘텐츠 줄이 보여요. Titan OS는 자체 홈 화면이 있어요.',
      '스마트폰과 TV를 같은 Wi-Fi에 연결하세요.',
      'Mando TV를 열고 목록에서 Philips TV를 누르세요.',
      'Roku TV는 아무것도 묻지 않아요. Google TV와 Android TV는 6자리 코드를 보여 줘요. 앱에 한 번만 입력하세요.',
      '방향키, 확인, 뒤로, 홈, 볼륨, 키보드를 쓰세요.',
    ],
    extra=[
      ('Philips Roku TV', '다른 Roku TV와 똑같이 작동해요. 스마트폰으로 켜려면 설정 > 시스템 > 전원에서 “TV 빠른 시작”을 활성화하세요. 자세한 내용은 [Roku 리모컨 앱](@roku) 페이지에 있어요.'),
      ('Google TV나 Android TV가 탑재된 Philips', 'Ambilight 모델이 많이 포함돼요. 화면에 나오는 코드로 페어링해요. 스마트폰으로 켜려면 네트워크나 전원 설정에서 Wake on LAN이나 “네트워크로 켜기”를 찾아보세요. 일부 모델에는 이 옵션이 없어요. 자세한 내용은 [Android TV 리모컨 앱](@android) 페이지에 있어요.'),
      ('Android가 없는 구형 Philips TV', 'Android를 쓰지 않는 2011~2015년의 Philips TV는 Mando TV에서 베타로 지원해요. 새로 추가된 기능이고 페어링 코드가 필요 없어요.'),
      ('Titan OS가 탑재된 Philips', 'Titan OS는 Mando TV가 지금은 조작하지 못하는 다른 시스템이에요. 분명하게 말씀드리는 편이 낫다고 생각해요. Android가 없는 최신 Philips 모델도 지원하지 않아요.'),
      ('무료와 Pro', '리모컨은 무료로 받아서 쓸 수 있고 광고도 구독도 없어요. Mando TV Pro는 추가 기능을 위한 선택 사항으로 한 번만 결제해요.'),
    ],
    marca=None,
    faq=[
      ('Mando TV가 Philips TV에서 작동하나요?', 'Roku TV, Google TV, Android TV를 쓰는 Philips TV에서는 작동하고, 베타로 Android가 없는 2011~2015년 Philips TV도 지원해요. Titan OS가 탑재된 모델은 지원하지 않아요.'),
      ('Mando TV로 Ambilight를 조작할 수 있나요?', 'Mando TV는 리모컨이에요. 버튼을 보내 주니까 방향키와 확인으로 Ambilight 설정에 들어갈 수 있어요. Ambilight를 위한 별도 조작은 없어요.'),
      ('Philips나 Google 계정이 필요한가요?', '아니요. Mando TV는 집 Wi-Fi로 연결하고 계정이 필요 없어요.'),
    ]),
]
OTRAS_GUIAS += [
  ('no-sub', '구독도 광고도 없는 리모컨 앱'),
  ('roku-app-alt', 'Roku 앱 대안: 모든 TV를 하나로'),
  ('lg-thinq', '내 LG TV를 위한 LG ThinQ 앱 대안'),
  ('smartthings', '삼성 TV를 위한 SmartThings 대안'),
  ('googletv-alt', '스마트폰용 Google TV 리모컨 대안'),
  ('windows', 'Windows PC용 리모컨 앱'),
  ('iphone', 'iPhone용 리모컨 앱: 모든 TV를 하나로'),
  ('firetv', '스마트폰이나 PC로 쓰는 Fire TV 리모컨'),
  ('firetv-lost', 'Fire TV 리모컨을 잃어버렸을 때 스마트폰으로 쓰는 방법'),
  ('turn-on', '리모컨 없이 TV 켜는 방법'),
  ('sony', '스마트폰으로 Sony TV 조작하는 방법'),
  ('tcl', '스마트폰으로 TCL TV 조작하는 방법'),
  ('hisense', 'Hisense 리모컨 앱: 되는 것과 안 되는 것'),
  ('philips', '스마트폰으로 Philips TV 조작하기'),
]
# <<< guías traídas del inglés
