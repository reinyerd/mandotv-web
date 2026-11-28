# Textos en vietnamita (bạn) de mandotv.app. Los usa generar_idiomas.py. Escritos para las búsquedas de Vietnam.
# Las claves de las páginas (lg, lost-tv, ...) y sus rutas están en idiomas_sitio.py.
# Los nombres de menús de cada marca (LG, Samsung, Roku, Android TV, iPhone) son los mismos que usa la app en vietnamita
# (lib/l10n/app_vi.arb del proyecto de la app).

UI = dict(
  locale='vi_VN',
  aria_home='Mando TV, trang chủ', aria_main='Menu chính', nav_que='Tính năng', nav_ayuda='Trợ giúp', nav_contacto='Liên hệ',
  asunto='Xin%20chao%20Mando%20TV', inicio='Trang chủ', privacidad='Quyền riêng tư', aria_pie='Chân trang', aria_ruta='Đường dẫn trang',
  aria_marcas='Thương hiệu và hướng dẫn', hecho='Phát triển tại Chile',
  aviso='Mando TV là một ứng dụng độc lập. Ứng dụng không liên kết với các hãng TV được nhắc đến, cũng như Google, Amazon, Apple hay Roku, và không được họ bảo trợ. Các nhãn hiệu thuộc về chủ sở hữu và chỉ được nhắc đến để nêu khả năng tương thích. Android TV và Google TV là nhãn hiệu của Google LLC. Apple TV là nhãn hiệu của Apple Inc.',
  bajar='Tải miễn phí', descarga='Tải về trên', anticipada='Truy cập sớm trên',
  apple_aria='Tải Mando TV miễn phí trên App Store', ms_aria='Tải Mando TV miễn phí trên Microsoft Store',
  gp_aria='Truy cập sớm Mando TV trên Google Play cho Android', aria_desc='Tải Mando TV',
  b_como_btn='Cách kết nối', b_tiendas_label='Có trên các cửa hàng ứng dụng',
  b_nota='iPhone, iPad, Mac, Android và Windows. Tải miễn phí, không quảng cáo. Pro chỉ mua một lần, không cần đăng ký.',
  b_compat='TV tương thích', b_otras='Hãng khác', b_otras_p='Mando TV điều khiển tất cả các hãng này bằng cùng một ứng dụng:',
  g_guias='Hướng dẫn', g_ver='Xem các bước', g_pasos='Từng bước một', g_hazlo='Cách làm với Mando TV',
  g_tiendas='Mando TV là ứng dụng điều khiển TV từ xa đa năng. Tải miễn phí, không quảng cáo, không cần tài khoản. Pro là gói mua một lần tùy chọn, không cần đăng ký. Dành cho iPhone, iPad, Windows và Android:',
  g_nota='Android: truy cập sớm miễn phí trên Google Play. <a href="{enlace}">Tham gia chỉ với hai bước</a> và giúp chúng tôi lên cửa hàng chính thức.',
  g_mas_pagina='Xem thêm chi tiết tại trang {enlace}.', g_mas_marca='Xem thêm chi tiết theo hãng:',
  g_faq='Câu hỏi thường gặp', g_mas='Hướng dẫn khác', g_todas='Tất cả hướng dẫn', g_ayuda='Trợ giúp và hỗ trợ',
  g_idiomas='Hướng dẫn này bằng các ngôn ngữ khác',
)

# Pie de página y listas de marcas/guías: (clave, texto)
PIE = [
  ('samsung', 'Điều khiển TV Samsung'),
  ('lg', 'Điều khiển TV LG'),
  ('roku', 'Điều khiển Roku'),
  ('android', 'Điều khiển Android TV'),
  ('guias', 'Tất cả hướng dẫn'),
  ('lost-tv', 'Mất điều khiển TV'),
  ('lost-lg', 'Mất điều khiển TV LG'),
  ('lg-on', 'Bật TV LG bằng điện thoại'),
  ('hdmi', 'Đổi cổng HDMI khi không có điều khiển'),
  ('androidtv', 'Android TV không có điều khiển'),
  ('console', 'Bật TV và HDMI máy chơi game không cần điều khiển'),
  ('samsung-lost', 'TV Samsung không có điều khiển'),
  ('roku-lost', 'Mất điều khiển Roku'),
  ('roku-403', 'Ứng dụng Roku không hoạt động'),
  ('androidtv-code', 'Mã ghép nối Android TV'),
  ('not-found', 'Điện thoại không tìm thấy TV'),
  ('wifi', 'Điện thoại làm điều khiển qua Wi-Fi'),
  ('pc', 'Điều khiển TV bằng máy tính'),
]
NOMBRE_OTRA = {'lg': 'Ứng dụng điều khiển TV LG', 'samsung': 'Ứng dụng điều khiển TV Samsung', 'roku': 'Ứng dụng điều khiển Roku',
               'android': 'Ứng dụng điều khiển Android TV và Google TV'}
PAGINA_MARCA = {'lg': 'Ứng dụng điều khiển TV LG', 'samsung': 'Ứng dụng điều khiển TV Samsung', 'roku': 'Ứng dụng điều khiển Roku',
                'android': 'Ứng dụng điều khiển Android TV'}

OTRAS_GUIAS = [
  ('lg-on', 'Bật TV LG bằng điện thoại'),
  ('lost-tv', 'Mất điều khiển TV: bạn có thể làm gì'),
  ('lost-lg', 'Mất điều khiển TV LG: dùng điện thoại thay thế'),
  ('hdmi', 'Đổi cổng HDMI trên TV khi không có điều khiển'),
  ('androidtv', 'Android TV không có điều khiển: dùng điện thoại thay thế'),
  ('console', 'Bật TV và chuyển sang HDMI của máy chơi game, không cần điều khiển'),
  ('samsung-lost', 'TV Samsung không có điều khiển gốc: dùng điện thoại thay thế'),
  ('roku-lost', 'Mất điều khiển Roku: dùng điện thoại thay thế'),
  ('roku-403', 'Ứng dụng Roku không hoạt động: sửa lỗi 403'),
  ('androidtv-code', 'Android TV yêu cầu mã ghép nối: cần làm gì'),
  ('not-found', 'Điện thoại không tìm thấy TV: những điều cần kiểm tra'),
  ('wifi', 'Cách dùng điện thoại làm điều khiển qua Wi-Fi'),
  ('pc', 'Cách điều khiển TV bằng máy tính Windows'),
]

INDICE = dict(
  titulo='Hướng dẫn: điều khiển TV bằng điện thoại | Mando TV',
  desc='Hướng dẫn từng bước: dùng điện thoại hoặc máy tính làm điều khiển TV, bật TV, đổi cổng HDMI và xử lý sự cố với Samsung, LG, Roku.',
  h1='Hướng dẫn: dùng điện thoại làm điều khiển TV',
  intro='Các bước đơn giản để kết nối điều khiển TV Samsung, LG, Roku hoặc Android TV với Mando TV, bật TV và xử lý sự cố.',
  h2_guias='Tất cả hướng dẫn', h2_marcas='Ứng dụng điều khiển theo hãng',
  marcas_extra=[('sony', 'Ứng dụng điều khiển TV Sony'), ('philips', 'Ứng dụng điều khiển TV Philips')],
)

MARCAS = [
  dict(clave='lg', color='#e0457b', corto='LG',
    titulo='Ứng dụng điều khiển TV LG trên điện thoại, miễn phí | Mando TV',
    desc='Biến điện thoại hoặc máy tính thành điều khiển TV LG webOS qua Wi-Fi. Phím bấm, bàn phím, ứng dụng, nguồn vào và bật TV miễn phí; con trỏ có trong Pro.',
    h1='Ứng dụng điều khiển TV LG trên điện thoại',
    intro='Mando TV là ứng dụng điều khiển dành cho TV LG: ứng dụng biến điện thoại hoặc máy tính của bạn thành điều khiển cho Smart TV LG chạy webOS qua mạng Wi-Fi trong nhà. Rất tiện khi bạn làm mất điều khiển, hết pin hoặc đơn giản là muốn gõ nhanh hơn.',
    compat='Smart TV LG chạy webOS (hầu hết các model Smart TV LG từ năm 2014). Hoạt động với TV LED, NanoCell, QNED và OLED. Các Smart TV LG đời cũ dùng NetCast (2011 đến 2014, trước webOS) nay được hỗ trợ trong bản beta: ghép nối bằng khóa 6 chữ số hiện trên TV.',
    h2=dict(funciones='Bạn có thể làm gì với TV LG', como='Cách kết nối TV LG với Mando TV',
            encender='Bật TV LG bằng điện thoại', preguntas='Câu hỏi về LG', guias='Hướng dẫn cho LG'),
    funciones=[
      ('Đầy đủ phím bấm', 'Phím điều hướng, OK, Quay lại, Home, âm lượng, kênh, tắt tiếng và phát nội dung.'),
      ('Con trỏ như Magic Remote (Pro)', 'Di chuyển mũi tên trên màn hình bằng ngón tay, giống hệt Magic Remote của LG.'),
      ('Hai bàn phím', 'Gõ trong phần tìm kiếm của TV và hầu hết ứng dụng bằng bàn phím điện thoại. Với Bàn phím YouTube (Pro), gõ hoặc nói bạn muốn xem gì, YouTube sẽ mở trên TV với kết quả.'),
      ('Ứng dụng và nguồn vào', 'Mở các ứng dụng của bạn và chuyển sang HDMI, TV trực tiếp, AirPlay hoặc Screen Share.'),
      ('Đầu ra âm thanh (Pro)', 'Chuyển qua lại giữa loa của TV và loa thanh của bạn.'),
      ('Bật TV', 'Khi TV đang tắt, Mando TV bật TV qua mạng và tự động kết nối.'),
    ],
    pasos=[
      'Kết nối điện thoại và TV với cùng một mạng Wi-Fi.',
      'Mở Mando TV: TV LG của bạn tự xuất hiện trong danh sách. Hãy chạm vào TV đó.',
      'Trên TV sẽ hiện một yêu cầu xin quyền. Hãy xác nhận bằng điều khiển quen thuộc của bạn (chỉ lần đầu tiên).',
    ],
    encender='Trên TV LG, hãy mở Cài đặt và tìm "Turn on TV with Mobile" (mục này nằm trong Settings, General, Devices, External Devices; ở model cũ hơn là Connection, Mobile Connection Management). Bật "Turn on via Wi-Fi". Nếu có "Quick Start+", hãy bật luôn. Sau đó, khi bạn chạm vào TV đang tắt trong Mando TV, ứng dụng sẽ hỏi có muốn bật TV không và tự động kết nối.',
    faq=[
      ('Tôi có cần Magic Remote để dùng Mando TV không?', 'Chỉ lần đầu tiên, để xác nhận yêu cầu trên màn hình. Sau đó chỉ cần điện thoại của bạn.'),
      ('Mando TV có thay thế được ứng dụng LG ThinQ không?', 'Để điều khiển TV thì có: bạn không cần tài khoản LG và cũng không phải đăng ký TV. Mando TV kết nối trực tiếp qua Wi-Fi của bạn.'),
      ('Tôi có thể bật TV LG bằng điện thoại không?', 'Có, nếu bạn đã bật "Turn on TV with Mobile" trên TV và đã kết nối một lần khi TV đang bật.'),
      ('Có dùng được với TV LG đời cũ trước webOS không?', 'Có, trong bản beta, với Smart TV LG NetCast từ 2011 đến 2014. Chúng ghép nối bằng khóa 6 chữ số hiện trên TV. Tính năng này còn mới nên có thể chưa hoàn thiện.'),
    ],
    guias=[('lg-on', 'Cách bật TV LG bằng điện thoại'),
           ('lost-lg', 'Mất điều khiển TV LG: dùng điện thoại thay thế'),
           ('hdmi', 'Đổi cổng HDMI trên TV khi không có điều khiển'),
           ('guias', 'Tất cả hướng dẫn điều khiển TV bằng điện thoại')]),
  dict(clave='samsung', color='#3d7bff', corto='Samsung',
    titulo='Ứng dụng điều khiển TV Samsung trên điện thoại | Mando TV',
    desc='Biến điện thoại hoặc máy tính thành điều khiển TV Samsung Tizen qua Wi-Fi. Phím bấm, bàn phím, ứng dụng, bật TV miễn phí; touchpad trong Pro.',
    h1='Ứng dụng điều khiển TV Samsung trên điện thoại',
    intro='Mando TV là ứng dụng điều khiển dành cho TV Samsung: ứng dụng biến điện thoại hoặc máy tính của bạn thành điều khiển cho Smart TV Samsung qua mạng Wi-Fi trong nhà. Bạn không cần tài khoản Samsung và cũng không phải đăng ký TV.',
    compat='Smart TV Samsung chạy Tizen, sản xuất từ 2016 trở lên (các dòng như Crystal UHD, QLED, Neo QLED, The Frame và OLED).',
    h2=dict(funciones='Bạn có thể làm gì với TV Samsung', como='Cách kết nối TV Samsung với Mando TV',
            encender='Bật TV Samsung bằng điện thoại', preguntas='Câu hỏi về Samsung', guias='Hướng dẫn cho Samsung'),
    funciones=[
      ('Đầy đủ phím bấm', 'Phím điều hướng, OK, Quay lại, Home, âm lượng, kênh, tắt tiếng và nguồn vào.'),
      ('Touchpad (Pro)', 'Vuốt ngón tay để lướt qua các menu mà không cần tìm phím mũi tên.'),
      ('Hai bàn phím', 'Gõ trong phần tìm kiếm của TV và hầu hết ứng dụng bằng bàn phím điện thoại. Với Bàn phím YouTube (Pro), gõ hoặc nói bạn muốn xem gì, YouTube sẽ mở trên TV với kết quả.'),
      ('Ứng dụng', 'Mở Netflix, YouTube, Prime Video và các ứng dụng khác chỉ với một chạm.'),
      ('Bật TV', 'Khi TV đang tắt, Mando TV bật TV qua mạng và tự động kết nối.'),
      ('Không cần tài khoản', 'Kết nối đi thẳng qua Wi-Fi của bạn, không qua internet.'),
    ],
    pasos=[
      'Kết nối điện thoại và TV với cùng một mạng Wi-Fi.',
      'Mở Mando TV: TV Samsung của bạn tự xuất hiện trong danh sách. Hãy chạm vào TV đó.',
      'TV sẽ hỏi bạn có cho phép kết nối không. Dùng điều khiển để chọn "Allow" (chỉ lần đầu tiên).',
    ],
    encender='Trên TV Samsung, hãy mở Settings > General > Network > Expert Settings và bật "Power On with Mobile". Sau đó, khi bạn chạm vào TV đang tắt trong Mando TV, ứng dụng sẽ hỏi có muốn bật TV không và tự động kết nối.',
    faq=[
      ('Tôi lỡ từ chối quyền truy cập. Phải làm sao?', 'Trên TV, hãy vào Settings > General > External Device Manager > Device Connection Manager và cho phép Mando TV.'),
      ('Mando TV có thay thế được SmartThings không?', 'Để điều khiển TV thì có, mà không cần tài khoản Samsung. Mando TV kết nối trực tiếp qua Wi-Fi của bạn.'),
      ('Có dùng được với TV Samsung đời cũ không?', 'Ứng dụng dùng được với TV Samsung chạy Tizen, sản xuất từ 2016 trở lên. Các model trước đó dùng hệ thống khác mà chúng tôi chưa hỗ trợ.'),
    ],
    guias=[('samsung-lost', 'TV Samsung không có điều khiển gốc: dùng điện thoại thay thế'),
           ('smartthings', 'Lựa chọn thay thế SmartThings cho TV Samsung'),
           ('turn-on', 'Cách bật TV khi không có điều khiển'),
           ('hdmi', 'Đổi cổng HDMI trên TV khi không có điều khiển'),
           ('guias', 'Tất cả hướng dẫn điều khiển TV bằng điện thoại')]),
  dict(clave='roku', color='#a77bff', corto='Roku',
    titulo='Ứng dụng điều khiển Roku trên điện thoại, miễn phí | Mando TV',
    desc='Biến điện thoại hoặc máy tính thành điều khiển Roku cho Roku TV và Roku Player qua Wi-Fi. Phím bấm, bàn phím, kênh, nguồn vào và bật TV miễn phí.',
    h1='Ứng dụng điều khiển Roku trên điện thoại',
    intro='Mando TV là ứng dụng điều khiển dành cho Roku: ứng dụng biến điện thoại hoặc máy tính của bạn thành điều khiển cho Roku qua mạng Wi-Fi trong nhà. Ứng dụng dùng được với TV Roku TV và cả Roku Player cắm vào cổng HDMI.',
    compat='TV Roku TV (TCL, Hisense, Philips, Sharp, JVC và các hãng khác) và Roku Player (Express, Streaming Stick, Ultra).',
    h2=dict(funciones='Bạn có thể làm gì với Roku', como='Cách kết nối Roku với Mando TV',
            encender='Bật Roku bằng điện thoại', preguntas='Câu hỏi về Roku', guias='Hướng dẫn cho Roku'),
    funciones=[
      ('Đầy đủ phím bấm', 'Phím điều hướng, OK, Quay lại, Home, âm lượng, tắt tiếng, phát lại và phát nội dung.'),
      ('Hai bàn phím', 'Gõ trong phần tìm kiếm của Roku và trong các kênh có hỗ trợ bằng bàn phím điện thoại. Với Bàn phím YouTube (Pro), gõ hoặc nói bạn muốn xem gì, YouTube sẽ mở trên TV với kết quả.'),
      ('Kênh', 'Mở Netflix, YouTube và các kênh Roku khác chỉ với một chạm.'),
      ('Nguồn vào', 'Với Roku TV, chuyển sang HDMI, ăng-ten hoặc AV ngay trong ứng dụng.'),
      ('Bật TV', 'Với Roku TV có Fast TV start, Mando TV bật TV từ điện thoại của bạn.'),
      ('Không cần ghép nối', 'Roku không yêu cầu mã: chỉ cần chạm vào Roku trong danh sách là kết nối xong.'),
      ('Làm điều khiển kêu để tìm', 'Nếu điều khiển Roku của bạn có loa, chẳng hạn Roku Voice Remote Pro, Mando TV sẽ làm nó kêu để bạn tìm thấy. Miễn phí, Roku phải đang bật.'),
    ],
    pasos=[
      'Kết nối điện thoại và Roku với cùng một mạng Wi-Fi.',
      'Mở Mando TV: Roku của bạn tự xuất hiện trong danh sách. Hãy chạm vào Roku đó.',
      'Nếu không kết nối được, trên Roku hãy vào Settings > System > Advanced system settings > Control by mobile apps và đặt Network access thành Default hoặc Permissive (với phần mềm Roku mới hơn, hãy đặt Control by mobile apps thành Enabled).',
    ],
    encender='Với Roku TV, hãy vào Settings > System > Power và bật "Fast TV start". Roku Player cắm vào một TV khác không thể bật theo cách này. Sau đó, khi bạn chạm vào TV đang tắt trong Mando TV, ứng dụng sẽ hỏi có muốn bật TV không và tự động kết nối.',
    faq=[
      ('Có dùng được với Roku Express hoặc Streaming Stick không?', 'Có. Tất cả Roku Player và Roku TV đều được điều khiển theo cùng một cách.'),
      ('Mando TV không tìm thấy Roku của tôi. Phải làm sao?', 'Hãy kiểm tra cả hai thiết bị có dùng cùng Wi-Fi không và "Control by mobile apps" trên Roku có bị tắt không. Bạn cũng có thể thêm Roku bằng địa chỉ IP.'),
      ('Tôi có cần tài khoản Roku không?', 'Không. Mando TV kết nối trực tiếp qua Wi-Fi của bạn.'),
    ],
    guias=[('roku-403', 'Ứng dụng Roku không hoạt động (lỗi 403)'),
           ('roku-lost', 'Mất điều khiển Roku: dùng điện thoại thay thế'),
           ('tcl', 'Ứng dụng điều khiển TV TCL'),
           ('hisense', 'Ứng dụng điều khiển TV Hisense'),
           ('philips', 'Ứng dụng điều khiển TV Philips'),
           ('guias', 'Tất cả hướng dẫn điều khiển TV bằng điện thoại')]),
  dict(clave='android', color='#2fbf8f', corto='Android TV và Google TV',
    titulo='Ứng dụng điều khiển Google TV và Android TV | Mando TV',
    desc='Điều khiển Google TV và Android TV (Sony, TCL, Xiaomi) bằng điện thoại qua Wi-Fi. Phím bấm, bàn phím, ứng dụng và bật TV miễn phí; touchpad có trong Pro.',
    h1='Ứng dụng điều khiển Google TV và Android TV trên điện thoại',
    intro='Mando TV là ứng dụng điều khiển dành cho Android TV: ứng dụng biến điện thoại hoặc máy tính của bạn thành điều khiển cho TV Android TV hoặc Google TV qua mạng Wi-Fi trong nhà. Dùng được cả từ iPhone và Windows.',
    compat='TV dùng Google TV hoặc Android TV của Sony, Philips, TCL, Hisense, Sharp, Xiaomi, Toshiba, Panasonic, Haier, Skyworth, JVC, Thomson, Motorola, OnePlus, iFFALCON, Kogan, Vu và các hãng khác, cùng Chromecast với Google TV, Google TV Streamer, onn. và Nvidia Shield. Một số hãng này cũng bán model dùng hệ thống khác: nếu TV của bạn hiện màn hình chính Google TV hoặc có Google Play Store thì Mando TV điều khiển được.',
    h2=dict(funciones='Bạn có thể làm gì với Android TV', como='Cách kết nối Android TV với Mando TV',
            encender='Bật Android TV bằng điện thoại', preguntas='Câu hỏi về Android TV', guias='Hướng dẫn cho Android TV'),
    funciones=[
      ('Đầy đủ phím bấm', 'Phím điều hướng, OK, Quay lại, Home, âm lượng, tắt tiếng và phát nội dung.'),
      ('Touchpad (Pro)', 'Vuốt ngón tay để di chuyển nhanh qua các menu của Google TV.'),
      ('Hai bàn phím', 'Gõ trong phần tìm kiếm của TV và hầu hết ứng dụng bằng bàn phím điện thoại. Với Bàn phím YouTube (Pro), gõ hoặc nói bạn muốn xem gì, YouTube sẽ mở trên TV với kết quả.'),
      ('Ứng dụng', 'Mở YouTube, Netflix, Disney+ và các ứng dụng khác chỉ với một chạm.'),
      ('Bật TV', 'Với các model có bật qua mạng, Mando TV bật TV và tự động kết nối.'),
      ('iPhone, Android và máy tính', 'Hoạt động giống hệt nhau trên mọi điện thoại và máy tính.'),
    ],
    pasos=[
      'Kết nối điện thoại và TV với cùng một mạng Wi-Fi.',
      'Mở Mando TV: Android TV của bạn tự xuất hiện trong danh sách. Hãy chạm vào TV đó.',
      'TV sẽ hiện một mã gồm 6 ký tự. Hãy nhập mã đó vào Mando TV (chỉ lần đầu tiên).',
    ],
    encender='Tùy vào hãng. Hãy tìm trong cài đặt mạng hoặc nguồn điện mục "Wake on LAN", "Wake on network", "Network standby" hoặc "Remote start" rồi bật lên. Một số model không có tùy chọn này. Sau đó, khi bạn chạm vào TV đang tắt trong Mando TV, ứng dụng sẽ hỏi có muốn bật TV không và tự động kết nối.',
    faq=[
      ('Có dùng được với Chromecast với Google TV không?', 'Có, việc ghép nối dùng mã 6 ký tự hiện trên màn hình.'),
      ('Khác gì so với ứng dụng Google TV?', 'Mando TV không cần tài khoản Google, dùng được cả trên Windows và điều khiển TV LG, Samsung và Roku bằng cùng một ứng dụng.'),
      ('Mã không hiện trên màn hình. Phải làm sao?', 'Hãy đóng Mando TV, mở lại ứng dụng và chạm vào TV một lần nữa. Kiểm tra xem TV có đang ở chế độ tiết kiệm điện quá sâu không.'),
    ],
    guias=[('androidtv-code', 'Android TV yêu cầu mã ghép nối: cần làm gì'),
           ('androidtv', 'Android TV không có điều khiển: dùng điện thoại thay thế'),
           ('googletv-alt', 'Lựa chọn thay thế điều khiển Google TV trên điện thoại'),
           ('sony', 'Ứng dụng điều khiển TV Sony'),
           ('tcl', 'Ứng dụng điều khiển TV TCL'),
           ('hisense', 'Ứng dụng điều khiển TV Hisense'),
           ('philips', 'Ứng dụng điều khiển TV Philips'),
           ('guias', 'Tất cả hướng dẫn điều khiển TV bằng điện thoại')]),
]

GUIAS = [
  dict(clave='lost-tv', corto='Mất điều khiển TV',
    titulo='Mất điều khiển TV? Dùng điện thoại để điều khiển TV',
    desc='Mất điều khiển TV? Bật TV bằng nút trên máy và dùng điện thoại làm điều khiển. Các bước cho LG, Samsung, Roku, Android TV. Miễn phí.',
    h1='Mất điều khiển TV? Bạn có thể làm gì ngay bây giờ',
    intro='Mất điều khiển TV là chuyện nhà nào cũng gặp: nó biến mất đúng lúc bạn muốn xem gì đó. Tin vui là điện thoại của bạn có thể thay điều khiển qua Wi-Fi trong nhà. Dưới đây là các bước bạn nên làm theo thứ tự.',
    pasos=[
      'Bật TV bằng nút trên máy. Nút này hầu như luôn nằm ở giữa cạnh dưới hoặc mặt sau gần một góc. Có khi là một nút đơn, có khi là một cần điều khiển nhỏ.',
      'Kết nối điện thoại với cùng mạng Wi-Fi của TV.',
      'Tải Mando TV, hoàn toàn miễn phí và không cần tài khoản, rồi mở ứng dụng. TV của bạn tự xuất hiện trong danh sách. Hãy chạm vào TV đó.',
      'Xác nhận kết nối theo hãng TV của bạn. Với LG và Samsung, TV hiện một yêu cầu: hãy xác nhận bằng nút hoặc cần điều khiển ngay trên TV. Với Android TV và Google TV, bạn nhập mã 6 ký tự hiện trên màn hình. Roku thì không hỏi gì cả.',
      'Xong rồi. Phím mũi tên, OK, Quay lại, Home, âm lượng, kênh và bàn phím đều miễn phí.',
      'Cho lần sau: trong cài đặt của TV, hãy bật tính năng bật nguồn qua mạng (xem hướng dẫn theo hãng của bạn bên dưới). Khi đó bạn có thể bật TV từ điện thoại mà không cần chạm vào TV.',
    ],
    extra=[
      ('Chọn hướng dẫn theo hãng TV của bạn', 'LG: [Mất điều khiển TV LG](@lost-lg). Android TV và Google TV: [Android TV không có điều khiển](@androidtv). Samsung: [TV Samsung không có điều khiển](@samsung-lost). Roku: [Mất điều khiển Roku](@roku-lost).'),
      ('Nếu không bật được TV bằng nút trên máy', 'Trước khi đi tìm điều khiển khác, hãy kiểm tra dây nguồn đã cắm chắc chưa và ổ điện có điện không. Nếu nút trên TV không phản ứng gì, vấn đề nằm ở TV chứ không phải điều khiển.'),
      ('Nếu điều khiển đột nhiên không hoạt động', 'Hãy thử thay pin mới. Để kiểm tra xem điều khiển còn phát tín hiệu không, hãy hướng nó vào camera điện thoại rồi bấm một phím: trên nhiều điện thoại bạn sẽ thấy một đốm sáng tím trên màn hình. Nếu thấy đèn mà TV không phản ứng, có thể cảm biến trên TV đang bị che.'),
      ('Nếu bạn đổi router và TV mất Wi-Fi', 'Không có điều khiển thì khó kết nối TV với mạng mới hơn. Cách dễ nhất là cắm TV vào router bằng dây mạng. Bạn cũng có thể tạo Wi-Fi có cùng tên và mật khẩu như trước: TV thường tự kết nối lại.'),
      ('Miễn phí có gì và Pro có gì', 'Bật và tắt TV, phím mũi tên, OK, âm lượng, kênh, phím số, bàn phím, mở ứng dụng và đổi nguồn vào đều miễn phí. Touchpad, giọng nói và quy trình thuộc Mando TV Pro, gói mua một lần không cần đăng ký.'),
    ],
    marca=None,
    faq=[
      ('Tôi có thể bật TV bằng điện thoại nếu chưa từng kết nối không?', 'Lần đầu bạn bật TV bằng nút trên máy. Sau khi kết nối điện thoại và bật tính năng bật nguồn qua mạng trong cài đặt TV, bạn có thể bật TV từ ứng dụng.'),
      ('Tôi có cần mua điều khiển mới không?', 'Không nhất thiết. Với Mando TV, phím bấm, âm lượng, bàn phím và bật TV đều miễn phí. Nếu bạn vẫn thích điều khiển thật, hãy tìm đúng model TV của mình.'),
      ('Có dùng được khi TV không có Wi-Fi không?', 'Thường là không. Điện thoại và TV thường phải dùng cùng mạng Wi-Fi. Ngoại lệ là hồng ngoại trên điện thoại Android có bộ phát hồng ngoại, cũng điều khiển được TV không phải Smart TV, và Bluetooth trong bản beta từ Android 9, hoạt động hoàn toàn không cần Wi-Fi với Google TV, Android TV và Fire TV.'),
    ]),
  dict(clave='lost-lg', corto='Mất điều khiển TV LG',
    titulo='Mất điều khiển TV LG? Dùng điện thoại thay thế',
    desc='Không có điều khiển LG? Bật TV bằng nút trên máy, xác nhận yêu cầu và dùng điện thoại qua Wi-Fi. Không cần tài khoản LG, không quảng cáo.',
    h1='Mất điều khiển TV LG? Cách dùng điện thoại thay thế',
    intro='Nếu bạn làm mất điều khiển LG hoặc Magic Remote không còn hoạt động, điện thoại có thể thay thế qua Wi-Fi. Cách này dùng được với TV LG chạy webOS, tức là hầu hết Smart TV LG từ năm 2014. Bạn không cần tài khoản LG hay ứng dụng ThinQ.',
    pasos=[
      'Bật TV bằng nút dưới logo LG hoặc nút ở mặt sau. Ở nhiều model, nút này là một cần điều khiển: nhấn để mở menu và gạt để chọn.',
      'Kết nối điện thoại với cùng mạng Wi-Fi của TV.',
      'Mở Mando TV và chạm vào TV LG của bạn trong danh sách.',
      'TV hiện một yêu cầu xin quyền. Hãy xác nhận bằng cần điều khiển hoặc nút trên TV. Nếu điện thoại này đã từng kết nối, TV sẽ không hỏi lại.',
      'Xong rồi. Phím mũi tên, OK, Quay lại, Home, âm lượng, kênh và bàn phím đều miễn phí. Con trỏ là tính năng Pro.',
      'Khi ứng dụng đã kết nối, hãy dùng phím mũi tên và OK để mở Cài đặt và bật "Turn on TV with Mobile". Hướng dẫn [Bật TV LG bằng điện thoại](@lg-on) chỉ bạn nơi tìm tùy chọn này.',
    ],
    extra=[
      ('Nếu TV không hiện yêu cầu', 'Có thể quyền đã được lưu hoặc điện thoại đang ở mạng khác. Hãy kiểm tra cả hai có cùng Wi-Fi không và VPN đã tắt chưa. Nếu TV không xuất hiện trong danh sách, hãy xem [Điện thoại không tìm thấy TV](@not-found).'),
      ('Nếu TV mất Wi-Fi', 'Hãy cắm TV vào router bằng dây mạng, TV sẽ tự dùng dây. Hoặc tạo Wi-Fi có cùng tên và mật khẩu như trước, vì TV thường tự kết nối lại.'),
      ('Nếu TV đang kẹt ở một nguồn vào khác', 'Trên điện thoại, chạm vào Nguồn vào và chọn cổng HDMI. Xem thêm tại [Đổi cổng HDMI trên TV khi không có điều khiển](@hdmi).'),
    ],
    marca='lg',
    faq=[
      ('Tôi có cần Magic Remote để dùng Mando TV không?', 'Bạn chỉ cần một thứ ở lần đầu để xác nhận yêu cầu, và nút hoặc cần điều khiển ngay trên TV là đủ. Sau đó bạn chỉ dùng điện thoại.'),
      ('Tôi có cần ứng dụng LG ThinQ không?', 'Không. Mando TV kết nối trực tiếp qua Wi-Fi của bạn và không đòi tài khoản LG.'),
      ('Tôi có thể bật và tắt TV LG bằng điện thoại không?', 'Tắt thì được. Để bật, bạn cần đã bật "Turn on TV with Mobile" trên TV và kết nối một lần khi TV đang bật.'),
    ]),
  dict(clave='hdmi', corto='Đổi HDMI khi không có điều khiển',
    titulo='Đổi cổng HDMI không cần điều khiển (Samsung, LG, Roku)',
    desc='Đổi cổng HDMI khi không có điều khiển trên TV Samsung, LG hoặc Roku: bằng nút trên TV hoặc bằng điện thoại. Miễn phí, không quảng cáo.',
    h1='Cách đổi cổng HDMI trên TV khi không có điều khiển',
    intro='Máy chơi game hoặc thiết bị phát đã sẵn sàng, nhưng TV đang kẹt ở nguồn vào khác và điều khiển thì không thấy đâu. Để đổi cổng HDMI mà không có điều khiển, bạn có hai cách: dùng nút trên TV hoặc dùng điện thoại. Dưới đây là các bước cho Samsung, LG và Roku.',
    pasos=[
      'Thử cách đơn giản nhất trước: bật máy chơi game hoặc thiết bị phát. Nếu HDMI-CEC trên TV đã bật (Samsung gọi là Anynet+, LG gọi là SIMPLINK), TV sẽ tự chuyển sang nguồn vào đó.',
      'Nếu TV không tự chuyển, hãy dùng nút trên TV, ở giữa cạnh dưới hoặc mặt sau. Nhiều TV Samsung và LG có cần điều khiển, nhấn vào sẽ mở menu có Source hoặc Inputs.',
      'Trong menu đó, chọn nguồn vào: HDMI 1, HDMI 2 và tiếp theo. Con số là cổng mà dây cáp đang cắm.',
      'Nếu bạn thích dùng điện thoại, hãy kết nối với cùng Wi-Fi, mở Mando TV và chạm vào TV của bạn.',
      'Với LG và Roku, chạm vào Nguồn vào và chọn cổng HDMI. Với Samsung, Nguồn vào sẽ gửi phím Source đến TV, rồi bạn chọn bằng phím mũi tên và OK.',
      'Bạn cũng có thể dùng phím mũi tên và OK trên màn hình chính của TV để vào phần nguồn vào. Tùy hãng và năm sản xuất, mục này tên là Source, Connected Devices hoặc Inputs. Với Roku TV, đó là các ô HDMI trên màn hình chính.',
    ],
    extra=[
      ('Samsung', 'Nếu menu của nút trên TV không có mục Source, hãy dùng điện thoại mở menu ở màn hình chính và tìm Source hoặc Connected Devices ở bên trái. Bạn điều khiển bằng phím mũi tên và OK trong Mando TV, hoàn toàn miễn phí.'),
      ('LG', 'Nhấn cần điều khiển trên TV và tìm Inputs. Với điện thoại, bạn cũng có thể mở danh sách nguồn vào trong Mando TV và chạm vào nguồn vào cần dùng.'),
      ('Roku TV', 'Trên màn hình chính có một ô cho mỗi nguồn vào, ví dụ HDMI 1 hoặc HDMI 2. Di chuyển bằng phím mũi tên và mở bằng OK, miễn phí.'),
      ('Nếu là TV dùng Android TV hoặc Google TV', 'Mando TV chưa có danh sách nguồn vào cho Android TV. Hãy dùng nút đổi nguồn vào trên TV hoặc vào phần nguồn vào bằng phím mũi tên và OK từ màn hình chính. Nếu bạn không có điều khiển và muốn kết nối, hãy đọc [Android TV không có điều khiển](@androidtv).'),
      ('Cần thêm trợ giúp', 'Nếu TV không bật được hoặc bạn không biết bắt đầu từ đâu, hãy đọc [Mất điều khiển TV](@lost-tv). Nếu bạn chơi game trên máy console, hướng dẫn [Bật TV và chuyển sang HDMI của máy chơi game, không cần điều khiển](@console) có mẹo HDMI-CEC.'),
    ],
    marca=None,
    faq=[
      ('Đổi cổng HDMI có miễn phí không?', 'Có. Danh sách nguồn vào trong Mando TV là miễn phí, cũng như bật TV, phím mũi tên, OK và âm lượng. Bạn cũng có thể vào nguồn vào qua menu của TV.'),
      ('Làm sao biết tôi cần cổng HDMI nào?', 'Hãy nhìn các cổng HDMI trên TV: mỗi cổng có một con số. Chọn cổng mà dây cáp của máy chơi game hoặc thiết bị phát đang cắm.'),
      ('Nếu TV không bật thì sao?', 'Hãy bật bằng nút trên máy. Nếu bạn đã từng kết nối và bật tính năng bật nguồn qua mạng, bạn cũng có thể bật TV bằng điện thoại.'),
    ]),
  dict(clave='androidtv', corto='Android TV không có điều khiển',
    titulo='Android TV không có điều khiển: dùng điện thoại thay thế',
    desc='Không có điều khiển Android TV hoặc Google TV? Kết nối điện thoại bằng mã 6 ký tự trên màn hình. Miễn phí, không cần tài khoản, không quảng cáo.',
    h1='Android TV không có điều khiển: cách dùng điện thoại thay thế',
    intro='Nếu bạn làm mất điều khiển Android TV hoặc Google TV, hay pin đã hết, điện thoại có thể thay thế. Điều tuyệt vời là bạn không cần điều khiển để kết nối: TV hiện một mã trên màn hình và bạn nhập mã đó trên điện thoại. Cách này dùng được với TV Sony, Philips, TCL, Hisense, Sharp và Xiaomi chạy Android TV, Chromecast với Google TV và Nvidia Shield.',
    pasos=[
      'Bật TV bằng nút trên máy. Nút này hầu như luôn nằm ở giữa cạnh dưới hoặc mặt sau gần một góc.',
      'Kết nối điện thoại với cùng mạng Wi-Fi của TV.',
      'Tải Mando TV, hoàn toàn miễn phí và không cần tài khoản Google, rồi mở ứng dụng. Chạm vào TV của bạn trong danh sách.',
      'TV hiện một mã gồm 6 chữ cái và số. Nhập mã đó trên điện thoại rồi chạm vào Ghép nối. Bạn không cần điều khiển cho bước này.',
      'Bây giờ bạn có thể dùng phím mũi tên, OK, Quay lại, Home, âm lượng, tắt tiếng và bàn phím. Tất cả đều miễn phí, cả danh sách ứng dụng cũng vậy. Touchpad là Pro.',
      'Để lần sau bật TV từ điện thoại, hãy tìm trong cài đặt mạng hoặc nguồn điện mục "Wake on LAN", "Wake on network", "Network standby" hoặc "Remote start".',
    ],
    extra=[
      ('Nếu TV không bật được từ điện thoại', 'Không phải Android TV nào cũng bật được qua mạng; điều này tùy hãng và model. Nếu TV của bạn không có tính năng này, hãy bật bằng nút trên TV rồi tiếp tục trên điện thoại. Bạn vẫn tắt TV được từ ứng dụng.'),
      ('Chromecast với Google TV, Google TV Streamer và Shield', 'Chúng kết nối theo cùng cách: cùng Wi-Fi, chạm vào thiết bị trong danh sách và nhập mã. Nếu TV đang hiện nguồn vào khác, hãy chuyển sang cổng HDMI mà thiết bị đang cắm, như hướng dẫn trong [Đổi cổng HDMI trên TV khi không có điều khiển](@hdmi).'),
      ('Nếu mã không hiện hoặc báo sai', 'Hãy kiểm tra TV đã thật sự bật và không ở chế độ chờ. Mã thay đổi sau mỗi yêu cầu: chỉ mã mới nhất có hiệu lực. Xem thêm chi tiết tại [Android TV yêu cầu mã ghép nối](@androidtv-code).'),
      ('Ứng dụng của Google hay Mando TV', 'Google có ứng dụng riêng, yêu cầu bạn có tài khoản Google. Mando TV không đòi tài khoản, dùng được cả trên Windows và điều khiển TV LG, Samsung và Roku bằng cùng một ứng dụng.'),
    ],
    marca='android',
    faq=[
      ('Tôi có cần điều khiển để ghép nối điện thoại không?', 'Không. Mã hiện trên màn hình TV và bạn nhập mã trên điện thoại. Bạn chỉ cần bật TV, nếu cần thì bằng nút trên máy.'),
      ('Có dùng được với Hisense không?', 'Với TV Hisense chạy Android TV hoặc Google TV thì có. TV Hisense dùng hệ thống khác thì không tương thích.'),
      ('Tôi có thể gõ bằng bàn phím điện thoại không?', 'Có, có hai loại. Bàn phím miễn phí gõ được vào ô tìm kiếm và các ô văn bản của TV và của hầu hết ứng dụng. YouTube và Netflix chỉ nhận bàn phím trên màn hình của riêng chúng, nên với YouTube có Bàn phím YouTube (Pro): gõ hoặc nói bạn muốn xem gì, YouTube sẽ mở trên TV với kết quả. Netflix dùng bằng phím mũi tên và OK.'),
    ]),
  dict(clave='lg-on', corto='Bật TV LG bằng điện thoại',
    titulo='Bật TV LG bằng điện thoại (hướng dẫn)',
    desc='Bật TV LG qua Wi-Fi bằng điện thoại: bật "Turn on TV with Mobile" và dùng Mando TV. Từng bước, miễn phí.',
    h1='Cách bật TV LG bằng điện thoại',
    intro='Bạn có thể bật TV LG bằng điện thoại, nhưng trước hết cần bật một tùy chọn trong TV. Sau đó điện thoại sẽ bật TV LG qua Wi-Fi mà không cần điều khiển. Chỉ mất năm phút và bạn chỉ làm một lần.',
    pasos=[
      'Kết nối điện thoại và TV LG với cùng một mạng Wi-Fi.',
      'Trên TV, hãy mở Cài đặt và tìm "Turn on TV with Mobile". Mục này nằm trong Settings, General, Devices, External Devices (ở model cũ hơn là Connection, Mobile Connection Management).',
      'Bật "Turn on via Wi-Fi". Nếu TV nối mạng bằng dây, hãy bật tùy chọn dành cho dây mạng.',
      'Nếu TV có "Quick Start+", hãy bật luôn.',
      'Khi TV đang bật, mở Mando TV trên điện thoại và chạm vào TV LG trong danh sách. Xác nhận yêu cầu hiện trên màn hình. Nhờ vậy ứng dụng học được cách đánh thức TV.',
      'Tắt TV rồi thử: chạm vào TV trong Mando TV, ứng dụng sẽ hỏi có muốn bật TV không.',
    ],
    extra=[
      ('Nếu TV không bật', 'TV phải đang dùng cùng Wi-Fi khi bị tắt. Hãy kiểm tra tùy chọn vẫn đang bật và điện thoại ở cùng mạng. Nếu bạn đã đổi router, hãy kết nối lại một lần khi TV đang bật.'),
    ],
    marca='lg',
    faq=[
      ('Tôi có thể bật TV LG bằng điện thoại nếu chưa từng kết nối không?', 'Không. Trước hết bạn cần bật "Turn on TV with Mobile" trên TV và kết nối một lần với Mando TV khi TV đang bật.'),
      ('Tôi có cần ứng dụng LG ThinQ không?', 'Không. Mando TV kết nối trực tiếp qua Wi-Fi của bạn và không đòi tài khoản LG.'),
      ('Có dùng được với dữ liệu di động không?', 'Không. Điện thoại và TV phải dùng cùng mạng Wi-Fi.'),
    ]),
  dict(clave='console', corto='TV và console không cần điều khiển',
    titulo='Không có điều khiển? Bật TV, đổi cổng HDMI',
    desc='Ngày game ra mắt mà không có điều khiển? Bật TV và dùng điện thoại chuyển sang cổng HDMI của PS5 hoặc Xbox. Miễn phí, không quảng cáo.',
    h1='Cách bật TV và chuyển sang cổng HDMI của máy chơi game mà không cần điều khiển',
    intro='Ngày GTA VI ra mắt, máy chơi game đã sẵn sàng và điều khiển TV thì biến mất đâu đó giữa những chiếc gối sofa. Chuyện này xảy ra thường hơn bạn nghĩ. Với Mando TV, điện thoại của bạn bật TV và chuyển sang cổng của PlayStation hoặc Xbox qua Wi-Fi trong nhà.',
    pasos=[
      'Kết nối điện thoại với cùng mạng Wi-Fi của TV.',
      'Mở Mando TV và chạm vào TV của bạn trong danh sách (Samsung, LG, Roku hoặc Android TV).',
      'Nếu TV đang tắt, chạm vào Bật. Cách này hoạt động khi TV đã bật tính năng bật nguồn qua mạng. Nếu bạn chưa từng bật, hãy bật TV bằng nút trên máy lần này và bật tính năng đó cho lần sau.',
      'Bật máy chơi game. Nếu HDMI-CEC đã bật (xem mẹo miễn phí bên dưới), TV sẽ tự chuyển sang nguồn vào của máy.',
      'Nếu TV không tự chuyển, chạm vào Nguồn vào trong Mando TV và chọn cổng HDMI mà máy chơi game đang cắm: HDMI 1, HDMI 2 và tiếp theo.',
      'Khi chơi, hãy dùng các nút lớn trong ứng dụng để chỉnh âm lượng.',
    ],
    extra=[
      ('Mẹo miễn phí: để máy chơi game tự chuyển nguồn vào của TV', 'PS5 và Xbox có thể bật TV và nhảy ngay sang cổng HDMI của chúng khi khởi động, nhờ HDMI-CEC. Với PS5, bạn tìm trong Settings > System > HDMI > Enable HDMI Device Link. Với Xbox, mở Settings > General > TV & display options và tìm tùy chọn điều khiển thiết bị. Trên TV, tính năng này có tên khác nhau tùy hãng: Anynet+ của Samsung, SIMPLINK của LG, còn BRAVIA Sync hoặc HDMI control ở các hãng khác.'),
      ('Nếu TV vẫn hiện hình ảnh khác', 'Nếu máy chơi game đã bật nhưng TV vẫn hiện ăng-ten hoặc một ứng dụng, nghĩa là TV chưa đổi nguồn vào. Trên điện thoại, chạm vào Nguồn vào và chọn cổng HDMI của máy chơi game. Hoặc dùng phím mũi tên và OK để vào phần nguồn vào của TV, hay dùng nút trên TV, rồi chọn cổng HDMI. Con số là cổng mà bạn đã cắm dây cáp của máy chơi game.'),
      ('Nếu là Roku TV', 'Nút trên TV, thường ở giữa cạnh dưới hoặc mặt sau, sẽ bật TV. Từ đó điện thoại làm phần còn lại.'),
    ],
    marca=None,
    faq=[
      ('Mando TV có liên quan gì đến GTA VI không?', 'Không. Mando TV không có liên kết nào với Rockstar Games hay Take-Two. Ứng dụng chỉ giúp bạn không mất thời gian chơi vì không tìm thấy điều khiển.'),
      ('Đổi cổng HDMI có miễn phí không?', 'Có. Danh sách nguồn vào trong Mando TV là miễn phí, cũng như bật TV, phím mũi tên, OK và âm lượng. Bạn cũng có thể để máy chơi game tự đổi nguồn vào bằng HDMI-CEC.'),
      ('Có dùng được với TV của tôi không?', 'Ứng dụng dùng được với TV Samsung, LG, Roku và Android TV trong cùng Wi-Fi. Nếu TV của bạn thuộc hãng khác, mẹo HDMI-CEC vẫn có thể giúp bạn.'),
      ('Tôi có thể dùng nó để chơi GTA VI (GTA 6) trên PS5 hoặc Xbox không?', 'Mando TV không can thiệp vào máy chơi game hay trò chơi. Nó chỉ đảm bảo TV đã bật và đang ở đúng cổng HDMI để bạn ngồi xuống và chơi.'),
    ]),
  dict(clave='samsung-lost', corto='TV Samsung không có điều khiển',
    titulo='Mất điều khiển Samsung? Dùng điện thoại thay thế',
    desc='Mất hoặc hỏng điều khiển Samsung? Dùng điện thoại làm điều khiển TV Tizen qua Wi-Fi. Đơn giản với Mando TV, miễn phí, không quảng cáo.',
    h1='TV Samsung không có điều khiển gốc: cách dùng điện thoại thay thế',
    intro='Nếu bạn làm mất điều khiển Samsung hoặc nó không còn hoạt động, bạn có thể dùng điện thoại làm điều khiển qua Wi-Fi. Cách này dùng được với TV Samsung chạy Tizen, sản xuất từ 2016 trở lên.',
    pasos=[
      'Bật TV bằng nút trên máy. Ở hầu hết các model, nút nằm ở cạnh dưới hoặc mặt sau, đôi khi là một cần điều khiển nhỏ.',
      'Kiểm tra TV đã kết nối Wi-Fi của bạn và điện thoại cùng ở mạng đó.',
      'Mở Mando TV trên điện thoại. TV Samsung của bạn tự xuất hiện trong danh sách. Hãy chạm vào TV đó.',
      'TV yêu cầu bạn xác nhận kết nối. Ở hầu hết các model, bạn xác nhận bằng các nút trên TV hoặc cần điều khiển ở mặt sau.',
      'Xong rồi, giờ bạn có thể dùng điện thoại làm điều khiển. Phím bấm, bàn phím và ứng dụng đều miễn phí; touchpad là tính năng Pro.',
      'Để lần sau bật TV từ điện thoại, hãy vào Settings > General > Network > Expert Settings và bật "Power On with Mobile".',
    ],
    extra=[
      ('Nếu TV không hỏi quyền', 'Có thể quyền đã được lưu hoặc TV đang ở Wi-Fi khác. Hãy đóng Mando TV và mở lại ứng dụng khi TV đang bật. Nếu TV sản xuất trước 2016, nó dùng hệ thống khác mà chưa được hỗ trợ.'),
      ('Nếu bạn lỡ từ chối quyền', 'Trên TV, hãy vào Settings > General > External Device Manager > Device Connection Manager và cho phép Mando TV. Nếu điện thoại vẫn không tìm thấy TV, hãy đọc [Điện thoại không tìm thấy TV](@not-found).'),
    ],
    marca='samsung',
    faq=[
      ('Làm sao xác nhận kết nối nếu tôi không có điều khiển?', 'Ở hầu hết các model, bạn xác nhận bằng các nút trên TV hoặc cần điều khiển ở mặt sau. Nếu model của bạn không có nút, hãy viết đến hola@mandotv.app và chúng tôi sẽ giúp bạn.'),
      ('Mando TV có đòi tài khoản Samsung không?', 'Không. Kết nối đi thẳng qua Wi-Fi của bạn, không cần tài khoản Samsung.'),
      ('Có dùng được với TV Samsung đời cũ của tôi không?', 'Ứng dụng dùng được với TV Samsung chạy Tizen, sản xuất từ 2016 trở lên.'),
    ]),
  dict(clave='wifi', corto='Điện thoại làm điều khiển qua Wi-Fi',
    titulo='Dùng điện thoại làm điều khiển: điều khiển TV qua Wi-Fi',
    desc='Kết nối điện thoại với TV qua Wi-Fi và dùng làm điều khiển cho Samsung, LG, Roku và Google TV. Các bước theo từng hãng với Mando TV. Miễn phí.',
    h1='Cách kết nối điện thoại với TV qua Wi-Fi để làm điều khiển',
    intro='Bạn chỉ cần điện thoại và TV dùng chung Wi-Fi, cùng một ứng dụng điều khiển. Mando TV tự tìm thấy TV của bạn và dùng được với Samsung, LG, Roku, Google TV và Android TV.',
    pasos=[
      'Kết nối điện thoại và TV với cùng một mạng Wi-Fi.',
      'Mở Mando TV. TV của bạn tự xuất hiện trong danh sách. Hãy chạm vào TV đó.',
      'Xác nhận kết nối theo hãng TV của bạn (chi tiết ở bên dưới).',
      'Điều khiển TV bằng các phím hoặc bằng bàn phím điện thoại. Touchpad là tính năng Pro.',
    ],
    extra=[
      ('Samsung', 'TV hỏi bạn có cho phép kết nối không. Hãy xác nhận trên màn hình ở lần đầu. Dùng được với Tizen, sản xuất từ 2016 trở lên. Để bật TV từ điện thoại, hãy vào Settings > General > Network > Expert Settings và bật "Power On with Mobile".'),
      ('LG', 'TV hiện một yêu cầu xin quyền. Hãy xác nhận ở lần đầu. Để bật TV từ điện thoại, hãy tìm "Turn on TV with Mobile" trong cài đặt và bật "Turn on via Wi-Fi".'),
      ('Roku', 'Roku không yêu cầu ghép nối: chạm vào Roku trong danh sách là kết nối xong. Để bật TV, hãy vào Settings > System > Power và bật "Fast TV start".'),
      ('Google TV và Android TV', 'TV hiện một mã trên màn hình. Hãy nhập mã đó vào Mando TV ở lần đầu. Để bật TV, hãy tìm trong cài đặt mục "Wake on LAN", "Wake on network" hoặc "Network standby".'),
    ],
    marca=None,
    faq=[
      ('Tôi có cần internet để dùng điện thoại làm điều khiển không?', 'Bạn cần điện thoại và TV dùng chung Wi-Fi. Mando TV kết nối trực tiếp với TV qua mạng đó.'),
      ('Tại sao TV của tôi không hiện trong danh sách?', 'Hãy kiểm tra TV đã bật chưa và điện thoại không dùng dữ liệu di động hay Wi-Fi khác. Một số router có mạng khách, cách ly các thiết bị với nhau.'),
      ('Tôi có thể dùng Mando TV trên iPhone hoặc điện thoại Android không?', 'Trên iPhone và iPad thì có: ứng dụng đã có trên App Store. Với Windows, ứng dụng cũng có trên Microsoft Store. Android sắp ra mắt: bạn có thể tham gia truy cập sớm miễn phí trên Google Play.'),
    ]),
  dict(clave='pc', corto='Điều khiển TV bằng máy tính',
    titulo='Điều khiển TV bằng máy tính Windows (miễn phí)',
    desc='Dùng máy tính Windows làm điều khiển cho TV Samsung, LG, Roku hoặc Google TV qua Wi-Fi. Phím bấm, bàn phím, ứng dụng miễn phí; phím tắt trong Pro.',
    h1='Cách điều khiển TV bằng máy tính Windows',
    intro='Nếu bạn dành cả ngày trước máy tính, bạn không cần đi tìm điều khiển: Mando TV cho Windows điều khiển TV Samsung, LG, Roku, Google TV hoặc Android TV qua Wi-Fi trong nhà. Rất tiện để đổi ứng dụng, chỉnh âm lượng hoặc gõ tìm kiếm trên YouTube bằng bàn phím máy tính.',
    pasos=[
      'Tải Mando TV miễn phí từ Microsoft Store về máy tính chạy Windows 10 hoặc 11.',
      'Kiểm tra máy tính và TV cùng một mạng (Wi-Fi hoặc dây, nhưng qua cùng một router).',
      'Mở Mando TV: TV của bạn tự xuất hiện trong danh sách. Hãy chạm hoặc nhấp vào TV đó.',
      'Ở lần đầu, xác nhận kết nối trên màn hình TV (với Google TV và Android TV, bạn nhập mã mà TV hiện ra).',
      'Xong: dùng các phím hoặc bàn phím để gõ vào ô tìm kiếm của TV. Touchpad là tính năng Pro.',
    ],
    extra=[
      ('Phím tắt trên máy tính (Pro)', 'Với Mando TV Pro, bạn điều khiển TV bằng bàn phím máy tính: phím mũi tên để di chuyển, Enter cho OK, Backspace hoặc Esc để quay lại, + và - cho âm lượng, M để tắt tiếng và phím cách để tạm dừng.'),
      ('Điều khiển mini luôn nằm trên cùng (Pro)', 'Giữ một cửa sổ nhỏ chứa điều khiển luôn hiện trong lúc bạn làm việc hoặc chơi game trên máy tính.'),
      ('Nói chuyện với TV từ máy tính (Pro)', 'Với Mando TV Pro, bạn ra lệnh cho TV bằng micro của máy tính: "mở YouTube", "tăng âm lượng" hoặc "tắt sau 30 phút", cứ nói tự nhiên như bình thường. Trên Windows, giọng nói được nhận dạng ngay trên máy tính: bạn không cần internet, không phải đổi gì trong cài đặt Windows và nó hoạt động với 6 ngôn ngữ của ứng dụng. Những gì bạn nói không rời khỏi máy tính và không được lưu. Chỉ với bộ xử lý rất cũ, ứng dụng mới chuyển sang tính năng đọc chính tả của Windows. Khi đó cần bật nhận dạng giọng nói trực tuyến trong cài đặt quyền riêng tư và thêm Tiếng Việt (Việt Nam) vào Windows. Nếu thiếu gì, ứng dụng sẽ báo và mở cài đặt bằng một nút.'),
    ],
    marca=None,
    faq=[
      ('Tôi có cần dây cáp hay Bluetooth để điều khiển TV bằng máy tính không?', 'Không. Mando TV kết nối qua mạng gia đình: máy tính và TV chỉ cần dùng chung một router.'),
      ('Có dùng được với mọi TV không?', 'Ứng dụng dùng được với TV Samsung chạy Tizen (sản xuất từ 2016 trở lên), LG chạy webOS, Roku, cùng Google TV hoặc Android TV (Sony, Philips, TCL, Hisense, Sharp, Xiaomi, Toshiba, Panasonic, Haier, Skyworth và các hãng khác).'),
      ('Giá bao nhiêu?', 'Phím bấm, bàn phím và bật nguồn qua mạng đều miễn phí và không quảng cáo. Mando TV Pro là gói mua một lần không cần đăng ký, cho các tính năng bổ sung như touchpad, phím tắt trên máy tính và điều khiển mini.'),
      ('Tại sao micro không hiểu tôi trên Windows?', 'Hãy kiểm tra tính năng giọng nói đã bật chưa (tính năng này thuộc Pro) và micro của máy tính có hoạt động trong Windows không. Trên hầu hết máy tính, giọng nói được nhận dạng ngay trên máy mà không cần internet. Chỉ với bộ xử lý rất cũ, ứng dụng mới dùng tính năng đọc chính tả của Windows. Khi đó hãy kiểm tra nhận dạng giọng nói trực tuyến đã bật trong cài đặt quyền riêng tư của Windows và Windows đã có Tiếng Việt (Việt Nam) trong cài đặt ngôn ngữ. Mando TV chỉ dùng ngôn ngữ này trong lúc đang nghe.'),
    ]),
  dict(clave='roku-403', corto='Ứng dụng Roku không hoạt động',
    titulo='Ứng dụng Roku không hoạt động? Sửa lỗi 403',
    desc='Điện thoại đã kết nối nhưng Roku không phản hồi? Bật "Control by mobile apps" trong 5 bước và dùng điện thoại làm điều khiển trở lại.',
    h1='Ứng dụng Roku không hoạt động: cách khắc phục',
    intro='Nếu điện thoại tìm thấy Roku và kết nối được nhưng bấm phím nào cũng không có tác dụng, nguyên nhân gần như luôn là một cài đặt trên chính Roku đang chặn các ứng dụng điều khiển. Các phiên bản Roku mới hạn chế chặt hơn theo mặc định. Trong menu Roku, bạn sửa xong trong một phút.',
    pasos=[
      'Trên Roku, nhấn Home và vào Settings.',
      'Mở System rồi Advanced system settings.',
      'Vào "Control by mobile apps". Ở một số model, mục này tên là "External control".',
      'Trong "Network access", chọn Default hoặc Permissive. Nếu ở model của bạn đó chỉ là một công tắc, hãy để ở Enabled.',
      'Quay lại Mando TV trên điện thoại và chạm vào Roku của bạn. Các phím giờ đã phản hồi.',
    ],
    extra=[
      ('Cách nhận biết đây có phải vấn đề của bạn', 'Dấu hiệu rất rõ: điện thoại thấy Roku trong danh sách và kết nối được, nhưng chạm vào phím nào cũng không có gì xảy ra. Bên trong, Roku trả lời bằng lỗi 403, nghĩa là "bị cấm". Mando TV nhận ra điều này khi kết nối và hiện đúng các bước này trên màn hình.'),
      ('Default hay Permissive, nên chọn gì?', 'Default là đủ: nó nhận lệnh từ mạng gia đình của bạn, đúng thứ mà một chiếc điều khiển cần. Permissive mở hơn và chỉ cần trên những mạng khác thường. Nếu tùy chọn đang là Disabled (ở phần mềm mới hơn là Restricted), Roku sẽ không phản hồi ứng dụng.'),
      ('Nếu bạn không có điều khiển Roku', 'Nếu cài đặt đang là Disabled, chỉ có thể đổi bằng điều khiển Roku thật. Hãy mượn một chiếc để đổi một lần; sau đó bạn làm mọi thứ bằng điện thoại. Hãy đọc thêm [Mất điều khiển Roku](@roku-lost).'),
    ],
    marca='roku',
    faq=[
      ('Tại sao Roku của tôi không còn phản hồi dù trước đây vẫn dùng được?', 'Một bản cập nhật Roku có thể hạn chế cài đặt này chặt hơn. Nguyên nhân không nằm ở điện thoại hay Wi-Fi của bạn: bạn chỉ cần cho phép lại việc điều khiển bằng ứng dụng.'),
      ('Cách này áp dụng cho Roku TV và Roku Player không?', 'Có. Cài đặt nằm trong cùng một menu ở Roku Player và Roku TV.'),
      ('Để cài đặt ở Default có an toàn không?', 'Có. Nó chỉ chấp nhận lệnh từ các thiết bị trong mạng gia đình của bạn.'),
    ]),
  dict(clave='not-found', corto='Điện thoại không tìm thấy TV',
    titulo='Điện thoại không tìm thấy TV? 6 điều cần kiểm tra',
    desc='Ứng dụng điều khiển không tìm thấy TV? Kiểm tra Wi-Fi, VPN và quyền truy cập mạng cục bộ. Dành cho Samsung, LG, Roku và Android TV.',
    h1='Điện thoại không tìm thấy TV: những điều cần kiểm tra',
    intro='Bạn mở ứng dụng điều khiển mà danh sách trống, hoặc TV có hiện nhưng kết nối bị ngắt. Gần như luôn là do mạng chứ không phải TV. Hãy kiểm tra các điểm này theo thứ tự: điểm đầu tiên giải quyết được hầu hết các trường hợp.',
    pasos=[
      'Xem điện thoại đang ở Wi-Fi nào và TV ở Wi-Fi nào. Phải là cùng một mạng, cùng một tên. Mạng khách không dùng được vì nó cách ly các thiết bị với nhau.',
      'Tắt VPN trên điện thoại nếu bạn đang dùng. Khi VPN bật, điện thoại ra internet qua một mạng khác và không thấy các thiết bị trong nhà bạn, hoặc kết nối bị ngắt sau vài giây.',
      'Tắt dữ liệu di động một lúc. Một số điện thoại tự chuyển từ Wi-Fi sang dữ liệu di động khi sóng yếu.',
      'Bật TV và đợi TV khởi động xong. TV đang tắt sẽ không trả lời khi ứng dụng tìm kiếm.',
      'Trên iPhone, hãy kiểm tra ứng dụng đã có quyền "Local Network": Cài đặt > Quyền riêng tư & Bảo mật > Local Network.',
      'Nếu vẫn không hiện, hãy thêm TV thủ công: trong Mando TV chạm vào "Thêm bằng IP" và nhập địa chỉ IP của TV.',
    ],
    extra=[
      ('Để ứng dụng hướng dẫn bạn', 'Trong danh sách TV có một nút dành cho trường hợp TV của bạn không hiện. Ứng dụng kiểm tra từng nguyên nhân phổ biến một (cùng Wi-Fi, VPN, quyền truy cập mạng cục bộ và hơn nữa) và hiện nút kiểm tra lại sau mỗi lần bạn sửa. Trình hướng dẫn này miễn phí.'),
      ('Tìm địa chỉ IP của TV ở đâu', 'Địa chỉ nằm trong menu mạng của TV và hơi khác nhau tùy model. Với LG: Cài đặt, Mạng, Kết nối Wi-Fi, Cài đặt Wi-Fi nâng cao. Với Samsung: Settings, General, Network, Network Status, IP Settings. Với Roku: Settings, Network, About. Với Android TV và Google TV: Settings, Network & Internet, rồi chạm vào mạng của bạn. Đó là một dãy số như 192.168.1.86.'),
      ('Nếu TV hiện ra nhưng kết nối bị ngắt', 'Nếu kết nối ngắt sau vài giây, nguyên nhân thường nằm ở điện thoại: VPN, việc chuyển sang Wi-Fi khác hoặc chế độ tiết kiệm pin. Hãy tắt VPN, ở yên trong cùng một Wi-Fi và thử lại.'),
      ('Wi-Fi 2,4 và 5 GHz', 'Không quan trọng việc điện thoại ở mạng 5 GHz còn TV ở mạng 2,4 GHz, miễn là cả hai đều từ cùng một router. Nếu bạn có bộ kích sóng Wi-Fi mà TV vẫn không hiện, hãy đưa điện thoại lại gần router chính hơn rồi thử lại.'),
    ],
    marca=None,
    faq=[
      ('Tôi có thể điều khiển TV bằng dữ liệu di động không?', 'Không. Tín hiệu điều khiển đi qua Wi-Fi trong nhà bạn, vì vậy điện thoại và TV phải ở cùng một mạng.'),
      ('Tại sao khi bật VPN thì không dùng được?', 'Vì VPN chuyển toàn bộ lưu lượng của điện thoại qua một mạng khác và điện thoại không còn thấy các thiết bị trong nhà. Hãy tắt VPN trong lúc dùng điều khiển.'),
      ('Có dùng được qua Bluetooth hoặc hồng ngoại không?', 'Với Smart TV, Mando TV dùng Wi-Fi. Hồng ngoại chỉ hoạt động trên điện thoại Android có bộ phát hồng ngoại và dành cho các TV không phải Smart TV. Bluetooth có trong bản beta, miễn phí và chỉ từ Android 9: điện thoại kết nối với TV như một bàn phím và điều khiển Bluetooth, hoàn toàn không cần Wi-Fi. Dùng được với Google TV, Android TV và Fire TV; với các hãng khác chấp nhận bàn phím Bluetooth thì có thể dùng được, còn Roku không chấp nhận.'),
    ]),
  dict(clave='androidtv-code', corto='Mã ghép nối Android TV',
    titulo='Android TV yêu cầu mã ghép nối: cần làm gì',
    desc='Android TV hoặc Google TV của bạn hiện mã 6 ký tự khi kết nối. Cách nhập mã và việc cần làm khi mã không hiện hoặc bị báo sai.',
    h1='Android TV yêu cầu mã ghép nối: cần làm gì',
    intro='Khi bạn kết nối điện thoại với Android TV hoặc Google TV lần đầu, TV hiện một mã 6 ký tự trên màn hình. Điều này bình thường và chỉ xảy ra một lần: nhờ vậy không ai khác điều khiển được TV của bạn. Dưới đây là cách nhập mã và việc cần làm nếu mã không hiện.',
    pasos=[
      'Bật TV và để màn hình chính hiện lên.',
      'Mở Mando TV trên điện thoại, cùng Wi-Fi với TV, và chạm vào TV của bạn trong danh sách.',
      'Nhìn lên màn hình TV: một mã gồm 6 chữ cái và số sẽ hiện ra.',
      'Nhập đúng như mã đang hiển thị trên điện thoại rồi chạm vào Ghép nối. Các chữ cái chỉ từ A đến F, nên ký tự tròn luôn là số không.',
      'Xong. TV ghi nhớ điện thoại của bạn và sẽ không hỏi lại mã.',
    ],
    extra=[
      ('Nếu mã không hiện trên TV', 'Hãy kiểm tra TV đã thật sự bật và không ở chế độ chờ, và điện thoại ở cùng Wi-Fi. Trên điện thoại, chạm vào TV một lần nữa. Nếu vẫn không hiện, hãy khởi động lại TV: rút phích cắm mười giây, cắm lại rồi thử lại.'),
      ('Nếu mã bị báo sai', 'Mã thay đổi sau mỗi yêu cầu. Nếu bạn nhập lâu hoặc yêu cầu mã hai lần, chỉ mã cuối cùng trên màn hình mới có hiệu lực. Trên điện thoại, chạm vào TV một lần nữa và nhập mã mới.'),
      ('Nếu TV lại hỏi mã', 'Điều này xảy ra khi TV bị đặt lại về cài đặt gốc hoặc bạn xóa dữ liệu ứng dụng trên điện thoại. Hãy ghép nối lại, khi đó TV sẽ ghi nhớ. Nếu bạn không có điều khiển nào, hãy đọc [Android TV không có điều khiển](@androidtv).'),
    ],
    marca='android',
    faq=[
      ('TV nào dùng mã này?', 'Các TV có Android TV hoặc Google TV: Sony, Philips, TCL, Hisense, Sharp, Xiaomi, Chromecast với Google TV và một số hãng khác.'),
      ('Tôi có cần tài khoản Google trên điện thoại không?', 'Không. Mã trên màn hình là tất cả những gì bạn cần.'),
      ('Có an toàn không?', 'Có. Mã chứng minh bạn đang ngồi trước TV: không ai ghép nối được nếu không thấy mã trên màn hình.'),
    ]),
  dict(clave='roku-lost', corto='Mất điều khiển Roku',
    titulo='Mất điều khiển Roku? Dùng điện thoại qua Wi-Fi',
    desc='Mất điều khiển Roku? Điện thoại thay thế qua Wi-Fi. Các bước đơn giản, kể cả khi bạn đã đổi router và Roku mất Wi-Fi.',
    h1='Mất điều khiển Roku: cách dùng điện thoại thay thế',
    intro='Nếu bạn làm mất điều khiển Roku hoặc nó không còn hoạt động, điện thoại sẽ thay thế miễn là Roku vẫn kết nối với Wi-Fi của bạn. Và nếu bạn đã đổi Wi-Fi hoặc router, cũng có cách giải quyết.',
    pasos=[
      'Trước tiên, thử làm điều khiển kêu lên. Nếu điều khiển Roku của bạn có loa, chẳng hạn Roku Voice Remote Pro, hãy mở Mando TV, kết nối với Roku và dùng tùy chọn làm điều khiển kêu để tìm thấy nó. Cách này chỉ dùng được với điều khiển Roku có loa, và Roku phải đang bật.',
      'Bật TV và để Roku cắm nguyên như vậy. Bạn không cần chạm vào nó.',
      'Kết nối điện thoại với cùng Wi-Fi mà Roku đang dùng.',
      'Mở Mando TV. Roku tự xuất hiện trong danh sách. Hãy chạm vào Roku đó.',
      'Dùng phím mũi tên, OK, Home và Quay lại như với điều khiển quen thuộc. Roku không yêu cầu mã.',
      'Nếu các phím không có tác dụng, Roku đang chặn việc điều khiển bằng ứng dụng: hướng dẫn [Ứng dụng Roku không hoạt động](@roku-403) giải thích cách cho phép lại.',
    ],
    extra=[
      ('Nếu Roku mất Wi-Fi (đổi router hoặc chuyển nhà)', 'Không có điều khiển, bạn không vào được menu để thiết lập mạng mới, nhưng có một mẹo: Roku tự kết nối với mạng có cùng tên và mật khẩu với mạng cũ. Trên một điện thoại khác, hãy tạo điểm phát Wi-Fi với đúng tên và mật khẩu đó, kết nối điện thoại chạy Mando TV vào đó và Roku sẽ hiện trong danh sách. Từ đó vào Settings, Network và kết nối Roku với Wi-Fi mới.'),
      ('Nếu là Roku TV', 'Roku TV có một nút trên máy, hầu như luôn ở giữa cạnh dưới hoặc mặt sau, để bật TV. Chỉ cần vậy là bật được TV và tiếp tục bằng điện thoại.'),
      ('Nếu bạn muốn mua điều khiển khác', 'Hãy chọn loại phù hợp với model của bạn. Roku Player nhỏ đặt sau TV cần điều khiển không dùng hồng ngoại, vì hồng ngoại không tới được.'),
    ],
    marca='roku',
    faq=[
      ('Điện thoại có bật được Roku không?', 'Roku Player đang cắm điện luôn ở trạng thái bật. Với Roku TV, Mando TV bật TV qua Wi-Fi nếu "Fast TV start" trong Settings > System > Power đã được bật.'),
      ('Còn âm lượng thì sao?', 'Với Roku TV, điện thoại tăng và giảm âm lượng. Với Roku Player nối qua HDMI, việc này tùy vào TV: nhiều TV dùng được, một số thì không.'),
      ('Tôi có phải tạo tài khoản không?', 'Không. Mando TV không đòi tài khoản và còn điều khiển TV Samsung, LG và Android TV bằng cùng một ứng dụng.'),
    ]),
]

SOPORTE = dict(
  titulo='Trợ giúp: kết nối và bật TV với Mando TV',
  desc='Cách kết nối điều khiển Mando TV với LG, Samsung, Roku hoặc Android TV, bật TV từ điện thoại và xử lý sự cố.',
  h1='Trợ giúp',
  intro='Những câu hỏi thường gặp nhất, theo thứ tự các bước. Nếu không thấy câu hỏi của bạn, hãy viết cho chúng tôi tại <a href="mailto:hola@mandotv.app?subject=Tro%20giup%20Mando%20TV">hola@mandotv.app</a> và chúng tôi sẽ trả lời.',
)
SOPORTE_HTML = '''      <h2 id="encontrar">Tìm TV của bạn</h2>
      <div class="preguntas">
        <details open><summary>TV của tôi không hiện trong danh sách</summary>
          <ol>
            <li>Kiểm tra điện thoại và TV có cùng mạng Wi-Fi không. Nếu router của bạn có mạng 2,4 GHz và 5 GHz với tên khác nhau, đôi khi chúng không thấy nhau.</li>
            <li>Đảm bảo TV đã được bật.</li>
            <li>Trên iPhone, kiểm tra Mando TV đã có quyền "Local Network" trong Cài đặt, Mando TV.</li>
            <li>Trong danh sách TV, chạm vào nút dành cho trường hợp TV của bạn không hiện: ứng dụng kiểm tra từng nguyên nhân phổ biến một (cùng Wi-Fi, VPN, quyền truy cập mạng cục bộ và hơn nữa) và hiện nút kiểm tra lại sau mỗi lần bạn sửa.</li>
            <li>Nếu vẫn không hiện, chạm vào nút +, chọn hãng và nhập địa chỉ IP của TV. Bạn xem được địa chỉ này trong menu mạng của TV (ví dụ 192.168.1.50).</li>
          </ol>
        </details>
        <details><summary>Có dùng được với dữ liệu di động hoặc khi ở ngoài không?</summary>
          <p>Không. Mando TV trò chuyện với TV trong mạng gia đình của bạn, vì vậy điện thoại phải kết nối với Wi-Fi đó.</p>
        </details>
      </div>

      <h2 id="conectar">Kết nối lần đầu</h2>
      <p>Hướng dẫn đầy đủ theo hãng: <a href="@@R_lg@@">LG</a>, <a href="@@R_samsung@@">Samsung</a>, <a href="@@R_roku@@">Roku</a> và <a href="@@R_android@@">Android TV</a>.</p>
      <div class="preguntas">
        <details><summary>LG</summary>
          <p>Khi bạn chạm vào TV, trên màn hình sẽ hiện một yêu cầu xin quyền. Hãy xác nhận bằng điều khiển quen thuộc của bạn. Bạn chỉ làm việc này một lần.</p>
        </details>
        <details><summary>Samsung</summary>
          <p>TV hỏi bạn có cho phép kết nối từ Mando TV không. Dùng điều khiển để chọn "Allow". Nếu bạn lỡ từ chối, hãy vào Settings > General > External Device Manager > Device Connection Manager và đổi thành cho phép.</p>
        </details>
        <details><summary>Roku</summary>
          <p>Roku không hỏi quyền. Nếu không kết nối được, trên Roku hãy vào Settings > System > Advanced system settings > Control by mobile apps và để Network access ở Default hoặc Permissive (với phần mềm Roku mới hơn, hãy đặt Control by mobile apps thành Enabled).</p>
        </details>
        <details><summary>Android TV và Google TV</summary>
          <p>TV hiện một mã gồm 6 ký tự. Hãy nhập đúng như mã hiện ra vào Mando TV. Dùng được với Sony, Philips, TCL, Hisense, Sharp, Xiaomi, Chromecast với Google TV và các TV khác chạy Android TV.</p>
        </details>
      </div>

      <h2 id="encender">Bật TV từ ứng dụng</h2>
      <p>Mando TV bật TV qua mạng gia đình của bạn. Cần hai điều: bạn đã kết nối ít nhất một lần khi TV đang bật, và trên TV đã bật tính năng bật nguồn qua mạng. Tên của cài đặt này thay đổi tùy model; đây là những tên phổ biến nhất:</p>
      <div class="preguntas">
        <details><summary>LG</summary>
          <p>Tìm trong Cài đặt (nằm trong Settings, General, Devices, External Devices; ở model cũ hơn là Connection, Mobile Connection Management) mục "Turn on TV with Mobile" và bật "Turn on via Wi-Fi". Nếu có "Quick Start+", hãy bật luôn.</p>
        </details>
        <details><summary>Samsung</summary>
          <p>Bật "Power On with Mobile" trong Settings > General > Network > Expert Settings.</p>
        </details>
        <details><summary>Roku</summary>
          <p>Với Roku TV, bật "Fast TV start" trong Settings > System > Power. Roku Player cắm vào một TV khác không thể bật theo cách này.</p>
        </details>
        <details><summary>Android TV và Google TV</summary>
          <p>Tùy vào hãng. Hãy tìm trong cài đặt mạng hoặc nguồn điện mục "Wake on LAN", "Wake on network", "Network standby" hoặc "Remote start". Một số model không có tùy chọn này.</p>
        </details>
      </div>

      <h2 id="falla">Khi có gì đó không hoạt động</h2>
      <div class="preguntas">
        <details><summary>Kết nối bị ngắt hoặc không có phản hồi</summary>
          <ol>
            <li>Trên màn hình điều khiển, chạm vào Kết nối lại.</li>
            <li>Nếu không được, hãy đóng Mando TV và mở lại ứng dụng.</li>
            <li>Nếu TV được cấp địa chỉ IP khác, hãy xóa TV khỏi danh sách rồi thêm lại.</li>
          </ol>
        </details>
        <details><summary>Cách gửi báo cáo lỗi cho chúng tôi</summary>
          <ol>
            <li>Trong Mando TV, chạm vào nút Tùy chỉnh (các thanh trượt ở phía trên).</li>
            <li>Chạm vào Sao chép báo cáo kiểm tra.</li>
            <li>Dán báo cáo vào một email gửi đến hola@mandotv.app, kèm hãng và model TV của bạn.</li>
          </ol>
          <p>Báo cáo không chứa mật khẩu, mã hay bất cứ thứ gì bạn gõ.</p>
        </details>
        <details><summary>Tôi đã mua Pro nhưng không thấy</summary>
          <p>Trong Tùy chỉnh, chạm vào Khôi phục giao dịch mua, bằng đúng tài khoản cửa hàng mà bạn đã dùng để mua. Nếu vẫn không thấy, hãy viết cho chúng tôi.</p>
        </details>
      </div>

      <h2 id="guias">Hướng dẫn từng bước</h2>
      <p><a href="@@R_guias@@">Xem tất cả hướng dẫn</a></p>
      <ul>
@@GUIAS@@
      </ul>

      <h2 id="contacto">Vẫn còn thắc mắc?</h2>
      <p>Hãy viết cho chúng tôi tại <a href="mailto:hola@mandotv.app?subject=Tro%20giup%20Mando%20TV">hola@mandotv.app</a>. Cho chúng tôi biết hãng và model TV của bạn, và bước bạn đang bị kẹt. Bạn cứ viết bằng ngôn ngữ của mình. Chúng tôi trả lời bằng tiếng Tây Ban Nha hoặc tiếng Anh và, nếu bạn muốn, bằng ngôn ngữ của bạn với sự hỗ trợ của công cụ dịch.</p>
'''

PRIVACIDAD = dict(
  titulo='Chính sách quyền riêng tư | Mando TV',
  desc='Mando TV không yêu cầu tài khoản hay dữ liệu cá nhân: không quảng cáo, không trình theo dõi. Điều khiển nói chuyện trực tiếp với TV của bạn trong Wi-Fi của bạn.',
  h1='Quyền riêng tư',
  intro='Nói ngắn gọn: Mando TV không yêu cầu tài khoản hay dữ liệu cá nhân. Không có quảng cáo và không có trình theo dõi.',
)
PRIVACIDAD_HTML = '''      <p class="fecha">Có hiệu lực từ ngày 14 tháng 11 năm 2026. Cập nhật lần cuối ngày 28 tháng 11 năm 2026.</p>

      <h2>Chúng tôi là ai</h2>
      <p>Mando TV là ứng dụng giúp bạn điều khiển TV từ điện thoại hoặc máy tính. Chính sách này mô tả ứng dụng sử dụng những thông tin nào và làm gì với chúng. Nếu có thắc mắc, hãy viết cho chúng tôi tại <a href="mailto:hola@mandotv.app">hola@mandotv.app</a>.</p>

      <h2>Chúng tôi thu thập những dữ liệu nào</h2>
      <p>Ứng dụng: chỉ những gì cần cho bản dùng thử Pro miễn phí trên Android và Windows, được giải thích trong mục <a href="#prueba">Dùng thử Pro miễn phí</a>. Ngoài ra, ứng dụng không gửi cho chúng tôi hay bên thứ ba bất kỳ thông tin nào về bạn hoặc cách bạn dùng ứng dụng. Ứng dụng không dùng công cụ phân tích, quảng cáo hay theo dõi.</p>
      <p>Trang web này: chúng tôi đo lượt truy cập theo hai cách, được giải thích trong phần <a href="#cookies">Cookie trên trang web này</a>.</p>

      <h2>Những gì ứng dụng lưu trên thiết bị của bạn</h2>
      <p>Để hoạt động, ứng dụng chỉ lưu những thứ sau trên điện thoại hoặc máy tính của bạn:</p>
      <ul>
        <li>Các TV bạn đã thêm: tên, hãng, địa chỉ IP trong mạng của bạn và địa chỉ phần cứng của mạng (MAC) dùng để bật TV.</li>
        <li>Khóa kết nối mà mỗi TV cấp khi bạn xác nhận quyền. Khóa được mã hóa và lưu trong kho an toàn của hệ thống (Keychain trên iPhone và Mac, Keystore trên Android, kho được bảo vệ trên Windows).</li>
        <li>Cài đặt của bạn: giao diện sáng hoặc tối, màu nền, rung và kiểu điều khiển.</li>
        <li>Nếu bạn dùng các tính năng Pro: ứng dụng yêu thích, quy trình của bạn và các lần tìm kiếm YouTube gần đây (bạn có thể xóa chúng trong ứng dụng).</li>
        <li>Nếu bạn dùng: chế độ trẻ em (mã PIN chỉ được lưu dưới dạng mã đã bảo vệ) và các điều khiển mà người khác đã chia sẻ cho bạn.</li>
      </ul>
      <p>Khi bạn xóa ứng dụng, dữ liệu này cũng bị xóa theo, trừ hai trường hợp. Trên Android, nếu bạn dùng sao lưu của Google, các tùy chọn của ứng dụng (như danh sách TV và cài đặt của bạn) có thể nằm lại trong bản sao lưu Google của chính bạn và quay lại khi bạn cài lại ứng dụng; khóa kết nối không bao giờ nằm trong đó. Trên iPhone và Mac, khóa kết nối được giữ trong Keychain của hệ thống và có thể vẫn còn đó sau khi bạn xóa ứng dụng.</p>

      <h2>Ứng dụng trò chuyện với ai</h2>
      <p>Với các TV của bạn, trong mạng Wi-Fi của bạn tại nhà. Để tìm TV, ứng dụng quét mạng cục bộ của bạn; vì vậy trên iPhone, ứng dụng xin quyền "Local Network". Văn bản bạn gõ bằng bàn phím trong ứng dụng đi thẳng đến TV và không được lưu.</p>
      <p>Ngoài ra, khi mở, ứng dụng tải về một tệp công khai nhỏ từ trang web này (mandotv.app/app/config.json) để biết có phiên bản mới nào bạn nên cài hay không và những tính năng nào thuộc Mando TV Pro. Đây là một lượt tải xuống giống như khi mở một trang web: ứng dụng không gửi dữ liệu của bạn, TV của bạn hay những gì bạn làm. Ứng dụng chỉ cho biết phiên bản và hệ thống (ví dụ Android) để hiện đúng thông báo cho bạn. Nếu bạn không có internet, ứng dụng tiếp tục hoạt động với tệp tải về gần nhất; nếu quá 30 ngày mà không tải được, ứng dụng sẽ nhờ bạn kết nối internet trong chốc lát. Như mọi lần truy cập một trang web, lần tải đó cũng cho nhà cung cấp trang web của chúng tôi (Cloudflare) thấy địa chỉ IP của bạn.</p>

      <p>Khi bạn gửi ảnh hoặc video lên TV (tính năng Pro), TV chỉ tải các tệp bạn chọn, trực tiếp từ điện thoại hoặc máy tính của bạn qua Wi-Fi trong nhà. Chúng không đi qua internet hay qua chúng tôi, ứng dụng không thấy các ảnh còn lại của bạn, và việc chia sẻ kết thúc ngay khi bạn đóng màn hình đó. Bên trong mạng gia đình của bạn, quá trình truyền này không được mã hóa.</p>
      <p>Nếu bạn dùng "Hiển thị màn hình của tôi trên TV" (tính năng Pro), ứng dụng chỉ chụp màn hình của bạn trong lúc bạn đang phản chiếu, mã hóa video ngay trên thiết bị rồi gửi qua Wi-Fi nhà bạn thẳng tới chiếc TV bạn đã chọn. Dữ liệu không đi qua internet hay qua chúng tôi, không có gì được ghi hay lưu lại, và việc phản chiếu dừng khi bạn dừng nó hoặc đóng ứng dụng. TV hiển thị mọi thứ xuất hiện trên màn hình đó, kể cả thông báo, và bên trong mạng gia đình của bạn luồng này không được mã hóa.</p>
      <h2 id="prueba">Dùng thử Pro miễn phí (Android và Windows)</h2>
      <p>Để mỗi thiết bị chỉ được dùng thử Pro miễn phí một lần, khi bản dùng thử bắt đầu, ứng dụng gửi một lần hai thứ đến máy chủ của chúng tôi (api.mandotv.app, trên Cloudflare): một dấu vân tay đã mã hóa của mã định danh mà hệ thống cấp cho ứng dụng trên thiết bị đó (trên Android là ID Android riêng của ứng dụng; trên Windows là mã định danh thiết bị dành cho các ứng dụng của chúng tôi) và bản dùng thử của bạn đã chạy được bao lâu. Dấu vân tay này không cho biết đó là thiết bị nào hay bạn là ai, và máy chủ mã hóa nó thêm một lần nữa bằng khóa riêng trước khi lưu.</p>
      <p>Chúng tôi chỉ lưu dấu vân tay đó, ngày bắt đầu dùng thử và thiết bị là Android hay Windows. Chúng tôi không lưu địa chỉ IP của bạn (Cloudflare nhìn thấy nó khi phản hồi, như mọi kết nối khác). Chúng tôi chỉ dùng để việc cài lại ứng dụng không mang lại thêm một lần dùng thử, tức là để phòng chống gian lận, đây là lợi ích hợp pháp của chúng tôi; không bao giờ dùng cho quảng cáo hay để theo dõi bạn, và chúng tôi không chia sẻ với ai. Mỗi bản ghi tự động bị xóa sau 24 tháng. Nếu bạn không có internet, bản dùng thử vẫn hoạt động. Trên iPhone và Mac không có gì được gửi đi: App Store quản lý bản dùng thử.</p>

      <h2>Micro và giọng nói</h2>
      <p>Trên iPhone, Mac và Android, tìm kiếm bằng giọng nói chỉ dùng micro khi bạn đang chạm vào nút nói. Những gì bạn nói được chuyển thành văn bản bởi tính năng nhận dạng giọng nói của hệ thống: của Apple trên iPhone và Mac, của Google trên Android, theo chính sách quyền riêng tư của từng bên. Trên Windows, giọng nói được nhận dạng ngay trên máy tính của bạn và không rời khỏi máy. Chỉ khi công cụ này trên thiết bị không thể khởi động hoặc liên tục gặp lỗi (ví dụ do bộ xử lý quá cũ hoặc thiếu mô hình giọng nói), ứng dụng mới dùng tính năng nhập bằng giọng nói của Windows, của Microsoft, hoạt động trực tuyến nếu bạn đã bật nhận dạng giọng nói trực tuyến trong Windows, theo chính sách quyền riêng tư của họ. Trên Windows, micro mở khi bạn mở bảng giọng nói và tắt khi bạn đóng bảng này, hoặc sau 30 giây không sử dụng; khi bạn không nói, không có gì được ghi hay lưu lại. Mando TV không ghi hay lưu âm thanh, và văn bản tạo ra đi thẳng đến TV của bạn, giống như những gì bạn gõ bằng bàn phím.</p>

      <h2>Nhà: thiết bị từ Apple Home và Google Home</h2>
      <p>Khi bạn mở mục Nhà (đang thử nghiệm), ứng dụng xin quyền xem các thiết bị bạn đã có trong ứng dụng Nhà của Apple (HomeKit) hoặc trong Google Home. Với quyền này, ứng dụng đọc tên, phòng và trạng thái của chúng (bật hay tắt, độ sáng, nhiệt độ, hoặc thiết bị gia dụng đang ở bước nào trong chương trình của nó) để hiển thị và gửi cho chúng những gì bạn chạm vào. Mọi thứ diễn ra giữa điện thoại của bạn và hệ thống của Apple hoặc Google: Mando TV không lưu danh sách này, không gửi cho chúng tôi hay bên thứ ba và không dùng cho quảng cáo hay phân tích. Trên Android, Google Home hoạt động với tài khoản Google của chính bạn, theo chính sách quyền riêng tư của Google. Bạn có thể thu hồi quyền bất cứ lúc nào: trên iPhone trong Cài đặt &gt; Quyền riêng tư &amp; Bảo mật &gt; HomeKit, trên Android trong cài đặt tài khoản Google của bạn.</p>
      <p>Khi bạn chạm vào "Mục Nhà hoạt động thế nào với bạn?", ứng dụng email của bạn mở ra với một thư gửi đến hola@mandotv.app, chứa bản tóm tắt kỹ thuật: phiên bản ứng dụng, hệ thống, mỗi loại thiết bị xuất hiện bao nhiêu cái và chúng có phản hồi không. Thư không có tên thiết bị, phòng hay nhà của bạn, và chỉ được gửi khi chính bạn gửi.</p>

      <h2>Liên kết và văn bản bạn chia sẻ</h2>
      <p>Khi bạn chia sẻ một điều khiển (liên kết mandotv.app/m/), liên kết chứa thiết kế của điều khiển và một gợi ý để tìm TV của bạn: tên, hãng, mẫu và địa chỉ của TV trong mạng của bạn. Liên kết không bao giờ chứa khóa kết nối, mã PIN hay địa chỉ phần cứng của TV. Thông tin này nằm sau dấu #, nên không bao giờ đến máy chủ của chúng tôi, nhưng bất kỳ ai bạn gửi liên kết, ví dụ qua WhatsApp, đều có thể đọc được. Một quy trình được chia sẻ (liên kết mandotv.app/r/) chỉ chứa tên và các bước.</p>
      <p>Văn bản sao lưu bạn có thể sao chép trong phần cài đặt của ứng dụng chứa mục yêu thích, quy trình và cài đặt của bạn. Văn bản này không được mã hóa và chỉ đến nơi bạn dán nó.</p>

      <h2>Báo cáo kiểm tra</h2>
      <p>Ứng dụng có nút "Sao chép báo cáo kiểm tra" giúp chúng tôi sửa lỗi. Báo cáo chỉ nằm trong bộ nhớ của ứng dụng khi ứng dụng đang mở và không bao giờ tự động gửi: bạn quyết định có sao chép và chia sẻ hay không. Báo cáo không chứa khóa kết nối, mã ghép đôi hay bất cứ thứ gì bạn gõ. Báo cáo có các bước ứng dụng đã làm, như tìm kiếm, kết nối và các lỗi, cùng thông tin kỹ thuật: phiên bản ứng dụng, hệ thống của bạn, và hãng, mẫu cùng địa chỉ của TV trong mạng của bạn.</p>

      <h2 id="cookies">Cookie trên trang web này</h2>
      <p>Phần này chỉ áp dụng cho trang web mandotv.app, không áp dụng cho ứng dụng.</p>
      <h3>Luôn không dùng cookie</h3>
      <p>Chúng tôi đếm lượt truy cập ẩn danh bằng Cloudflare Web Analytics: có bao nhiêu người truy cập trang web, họ đọc những trang nào và từ quốc gia nào. Công cụ này không dùng cookie, không dùng địa chỉ IP của bạn để nhận diện bạn và không theo dõi những gì bạn làm trên các trang web khác.</p>
      <h3>Có cookie, chỉ khi bạn đồng ý</h3>
      <p>Nếu bạn chạm vào "Chấp nhận" trong thông báo cookie, chúng tôi bật Google Analytics (của Google LLC) để hiểu rõ hơn cách trang web được sử dụng: lượt xem trang, thời gian ở lại, loại thiết bị, thành phố ước chừng và nơi bạn đến từ đâu. Để làm vậy, công cụ này lưu cookie _ga và _ga_* tới 2 năm trong trình duyệt của bạn. Google có thể xử lý dữ liệu này trên máy chủ bên ngoài Chile. Chúng tôi đã tắt các tính năng quảng cáo và Google Signals và không dùng dữ liệu này để hiện quảng cáo cho bạn.</p>
      <p>Nếu bạn chạm vào "Từ chối" hoặc không chọn gì, Google Analytics sẽ không được tải và không có cookie nào được lưu. Bạn có thể đổi quyết định bất cứ lúc nào bằng nút "Cookie" ở cuối mỗi trang; nếu bạn rút lại sự đồng ý, chúng tôi sẽ xóa các cookie này.</p>
      <p>Lựa chọn của bạn được lưu trong trình duyệt của bạn (bộ nhớ cục bộ, không gửi cho ai) để chúng tôi không hỏi lại bạn. Bộ nhớ này cũng lưu ngôn ngữ bạn chọn ở cuối trang, để lần sau trang web mở bằng ngôn ngữ đó. Để hiện giá Pro của nước bạn, mỗi trang hỏi Cloudflare, nơi vốn đã phục vụ trang web này, xem bạn truy cập từ nước nào, hoặc dùng vùng của ngôn ngữ trình duyệt; câu trả lời đó không được lưu.</p>

      <h2>Giao dịch mua</h2>
      <p>Khi bạn mua Mando TV Pro, khoản thanh toán do cửa hàng ứng dụng xử lý (App Store, Google Play hoặc Microsoft Store). Chúng tôi không nhận và không lưu thông tin thẻ của bạn. Cửa hàng chỉ xác nhận với ứng dụng rằng giao dịch mua tồn tại.</p>

      <h2>Email bạn gửi cho chúng tôi</h2>
      <p>Khi bạn viết cho chúng tôi tại <a href="mailto:hola@mandotv.app">hola@mandotv.app</a>, chúng tôi chỉ dùng địa chỉ email của bạn và nội dung bạn gửi để trả lời bạn. Chúng tôi không chia sẻ chúng và không dùng cho quảng cáo. Bạn có thể yêu cầu chúng tôi xóa thư của bạn bất cứ lúc nào.</p>

      <h2>Trẻ em</h2>
      <p>Ứng dụng không thu thập dữ liệu cá nhân của bất kỳ ai, kể cả trẻ em.</p>

      <h2>Thay đổi chính sách này</h2>
      <p>Nếu một ngày nào đó điều ứng dụng làm với dữ liệu của bạn thay đổi, chúng tôi sẽ cập nhật trang này và ngày ở trên trước khi thay đổi đến với ứng dụng.</p>
'''


# >>> guías traídas del inglés (ensamblar.py)
# Adaptadas con Ollama (qwen3.6:35b) desde las guías inglesas y auditadas por Opus el 22-nov. Rutas en idiomas_sitio.py.
GUIAS += [
  dict(clave='no-sub', corto='Ứng dụng điều khiển không đăng ký', fecha='2026-11-23',
    titulo='Ứng dụng điều khiển TV không đăng ký, không quảng cáo',
    desc='Chán các ứng dụng điều khiển có quảng cáo hay đăng ký theo tuần? Mando TV miễn phí và không quảng cáo, Pro là gói mua một lần tùy chọn. So sánh trung thực.',
    h1='Ứng dụng điều khiển TV không đăng ký và không quảng cáo',
    intro='Nhiều ứng dụng điều khiển vạn năng hiện quảng cáo hoặc đòi đăng ký theo tuần trước khi dùng được. Mando TV đi theo hướng khác: điều khiển miễn phí, không quảng cáo, không cần tài khoản. Bạn chỉ mua gói Pro tùy chọn một lần. Dưới đây là so sánh, kể cả những gì ứng dụng không làm được.',
    pasos=[
      'Trước khi cài, hãy mở trang cửa hàng của ứng dụng và xem các giao dịch mua trong ứng dụng. Giá theo tuần hoặc theo tháng cho thấy đó là gói đăng ký.',
      'Trên Google Play, hãy xem trang có ghi "Chứa quảng cáo" không và đọc các đánh giá mới nhất ít sao: những gói trả phí bất ngờ thường xuất hiện ở đó.',
      'Đảm bảo ứng dụng điều khiển được TV của bạn qua Wi-Fi. Mando TV dùng được với Samsung (từ 2016), LG webOS, Roku, Google TV, Android TV và Fire TV.',
      'Cài Mando TV, kết nối điện thoại với cùng Wi-Fi của TV và chạm vào TV của bạn trong danh sách.',
      'Xác nhận yêu cầu trên TV hoặc nhập mã hiện ra. Phím bấm, âm lượng, kênh và bàn phím không mất phí.',
    ],
    tabla=dict(titulo='Mando TV so với nhiều ứng dụng điều khiển',
      cabeza=['', 'Mando TV', 'Nhiều ứng dụng có quảng cáo hoặc đăng ký'],
      filas=[
        ['Điều khiển cơ bản', 'Miễn phí', 'Thường miễn phí kèm quảng cáo hoặc ẩn sau thời gian dùng thử'],
        ['Quảng cáo', 'Không có', 'Thường gặp'],
        ['Đăng ký', 'Không có. Pro là gói mua một lần tùy chọn', 'Gói theo tuần hoặc theo tháng là phổ biến'],
        ['Tài khoản', 'Không cần', 'Tùy ứng dụng'],
        ['Smart TV qua Wi-Fi', 'Samsung (từ 2016), LG webOS, Roku, Google TV, Android TV, Fire TV, Apple TV (beta)', 'Tùy ứng dụng'],
        ['Hồng ngoại cho TV đời cũ', 'Miễn phí trên điện thoại Android có bộ phát hồng ngoại (mới)', 'Một số ứng dụng, chỉ với điện thoại có bộ phát hồng ngoại'],
        ['Bluetooth', 'Beta từ Android 9, miễn phí', 'Tùy ứng dụng'],
        ['Ảnh và video lên TV', 'Pro, qua Wi-Fi (không phản chiếu màn hình)', 'Tùy ứng dụng'],
        ['Điện thoại và máy tính', 'iPhone, iPad, Mac và Windows, cùng Android trong giai đoạn truy cập sớm', 'Tùy ứng dụng'],
        ['Phản chiếu màn hình', 'Miễn phí trên iPhone, iPad và Windows bằng tính năng có sẵn của từng thiết bị. Trên Windows, Pro còn phản chiếu được màn hình máy tính lên TV LG, Samsung, Hisense và Android TV (beta)', 'Một số ứng dụng có cung cấp'],
      ],
      nota='Mando TV không được so sánh với một ứng dụng cụ thể nào. Giá hiện hành có trên trang cửa hàng của từng ứng dụng.'),
    extra=[
      ('Những gì Mando TV không làm', 'Trên iPhone và iPad, ứng dụng hướng bạn đến tính năng Phản chiếu màn hình trong Trung tâm điều khiển, là tính năng của chính iPhone, dùng được với TV có AirPlay. Trên Windows, ứng dụng mở Cast (Windows + K), và Mando TV Pro có thể gửi màn hình máy tính lên TV LG, Samsung, Hisense và Android TV qua Wi-Fi của bạn (beta, trễ vài giây và không có âm thanh). Với Mando TV Pro, ứng dụng còn gửi được ảnh và video lên TV qua Wi-Fi của bạn. Ứng dụng điều khiển Smart TV qua Wi-Fi trong nhà. TV không phải Smart TV có thể được điều khiển bằng hồng ngoại từ điện thoại Android có bộ phát hồng ngoại. Từ Android 9, điện thoại cũng có thể kết nối qua Bluetooth như bàn phím và điều khiển với Google TV, Android TV và Fire TV, hoàn toàn không cần Wi-Fi. Tùy chọn này đang ở bản beta và miễn phí.'),
      ('Mando TV kiếm tiền như thế nào', 'Không bằng quảng cáo và không bằng dữ liệu của bạn: ứng dụng không có quảng cáo và không theo dõi bạn. Mando TV được duy trì nhờ Pro, gói mua một lần tùy chọn cho các tính năng bổ sung. Điều khiển cơ bản miễn phí.'),
      ('Trên những thiết bị bạn đã có', 'iPhone, iPad và Mac từ App Store, máy tính Windows từ Microsoft Store và Android qua truy cập sớm miễn phí trên Google Play. Xem [Ứng dụng điều khiển TV cho iPhone](@iphone) và [Ứng dụng điều khiển TV cho Windows](@windows).'),
      ('Quyền riêng tư', 'Không tài khoản và không theo dõi trong ứng dụng. Việc trao đổi với TV chỉ diễn ra trong mạng cục bộ, dữ liệu kết nối được mã hóa và lưu trên thiết bị của bạn. Chi tiết trong [Chính sách quyền riêng tư](@privacidad).'),
    ],
    marca=None,
    faq=[
      ('Có ứng dụng điều khiển TV không cần đăng ký không?', 'Có. Mando TV hoàn toàn không có đăng ký: điều khiển miễn phí và không quảng cáo, Pro là gói mua một lần tùy chọn.'),
      ('Mando TV có thật sự miễn phí không?', 'Có. Phím mũi tên, OK, Quay lại, Home, âm lượng, kênh, phím số, bàn phím và bật/tắt đều miễn phí, không quảng cáo và không giới hạn thời gian.'),
      ('Có dùng được khi không có Wi-Fi không?', 'Thường là không. Mando TV điều khiển Smart TV qua Wi-Fi trong nhà. Ngoại lệ: hồng ngoại trên điện thoại Android có bộ phát hồng ngoại, dùng được cả với TV không phải Smart TV hoặc không có kết nối Wi-Fi, và Bluetooth, trong bản beta từ Android 9, cho Google TV, Android TV và Fire TV.'),
    ]),
  dict(clave='roku-app-alt', corto='Lựa chọn thay thế ứng dụng Roku', fecha='2026-11-23',
    titulo='Lựa chọn thay thế ứng dụng Roku: điều khiển Roku đơn giản',
    desc='Thay thế ứng dụng Roku: Mando TV điều khiển Roku TV và Roku Player qua Wi-Fi, không tài khoản, không quảng cáo, cùng Samsung, LG và Google TV.',
    h1='Lựa chọn thay thế ứng dụng Roku: một ứng dụng cho mọi TV',
    intro='Ứng dụng Roku chính thức làm được nhiều việc: Channel Store, truyền màn hình, nghe riêng và cả điều khiển. Nếu bạn chỉ cần một chiếc điều khiển nhanh, hoặc trong nhà còn có TV Samsung, LG hay Google TV, Mando TV là lựa chọn thay thế đơn giản, điều khiển Roku qua Wi-Fi mà không cần tài khoản.',
    pasos=[
      'Kết nối điện thoại và Roku với cùng một mạng Wi-Fi.',
      'Tải Mando TV và mở lên. Roku TV hoặc Roku Player của bạn hiện trong danh sách. Hãy chạm vào đó. Roku không yêu cầu mã.',
      'Dùng phím mũi tên, OK, Quay lại, Home, âm lượng và bàn phím. Nhập từ khóa tìm kiếm trong các kênh Roku bằng bàn phím điện thoại.',
      'Nếu các phím không có tác dụng, trên Roku hãy vào Settings > System > Advanced system settings > Control by mobile apps và đặt Network access thành Default hoặc Permissive (với phần mềm Roku mới hơn, hãy đặt Control by mobile apps thành Enabled).',
      'Tùy chọn: bật "Fast TV start" trên Roku TV trong Settings > System > Power để Mando TV có thể bật TV.',
    ],
    extra=[
      ('Mando TV phù hợp hơn ở đâu', 'Một ứng dụng cho nhiều TV: Roku, Samsung, LG và Google TV hoặc Android TV. Không tài khoản, không quảng cáo. Ứng dụng cũng chạy trên máy tính Windows, rất tiện khi ngồi ở bàn làm việc. Phím mũi tên và âm lượng phản hồi nhanh, còn bàn phím giúp bạn gõ từ khóa tìm kiếm dễ dàng.'),
      ('Ứng dụng Roku chính thức tốt hơn ở đâu', 'Hãy giữ ứng dụng Roku cho những gì nó có ngoài phần điều khiển, như duyệt và thêm kênh từ Roku Channel Store, cùng tính năng truyền màn hình và nghe riêng (âm thanh qua tai nghe cắm vào điện thoại). Dùng cả hai nếu bạn muốn. Chúng có thể chạy trên cùng một điện thoại.'),
      ('Roku TV và Roku Player', 'Cả hai đều dùng được. Bao gồm các model Roku TV của TCL, Hisense, Philips và các hãng khác, cùng Roku Express, Streaming Stick và Ultra. Chi tiết có trên [trang ứng dụng điều khiển Roku](@roku).'),
      ('Khi ứng dụng Roku không còn hoạt động', 'Khi các phím không còn phản hồi, thường là Roku đang chặn việc điều khiển bằng ứng dụng. Hướng dẫn [Ứng dụng Roku không hoạt động](@roku-403) chỉ cho bạn cài đặt khắc phục vấn đề này.'),
      ('Miễn phí và Pro', 'Phím mũi tên, OK, Quay lại, Home, âm lượng, kênh, phím số, bàn phím, mở ứng dụng, đổi nguồn vào và bật hoặc tắt TV đều miễn phí, không quảng cáo và không đăng ký. Touchpad, lệnh thoại, ứng dụng yêu thích, quy trình và hẹn giờ tắt là một phần của Mando TV Pro, gói mua một lần không cần đăng ký.'),
    ],
    marca='roku',
    faq=[
      ('Tôi có cần tài khoản Roku để dùng Mando TV không?', 'Không. Mando TV trao đổi với Roku qua mạng gia đình của bạn và không đòi tài khoản.'),
      ('Mando TV có thay thế hoàn toàn ứng dụng Roku Mobile không?', 'Là điều khiển thì có. Với Channel Store, truyền màn hình và nghe riêng, hãy giữ ứng dụng Roku chính thức.'),
      ('Có dùng được với Roku Express hoặc Streaming Stick của tôi không?', 'Có. Tất cả Roku Player và Roku TV đều được điều khiển theo cùng một cách.'),
    ]),
  dict(clave='lg-thinq', corto='Lựa chọn thay thế LG ThinQ', fecha='2026-11-23',
    titulo='Lựa chọn thay thế ứng dụng LG ThinQ: điều khiển LG không tài khoản',
    desc='Cần lựa chọn thay thế LG ThinQ chỉ để làm điều khiển? Mando TV điều khiển TV LG webOS qua Wi-Fi, không tài khoản LG, không quảng cáo.',
    h1='Lựa chọn thay thế ứng dụng LG ThinQ cho TV LG của bạn',
    intro='LG ThinQ là ứng dụng chính thức của LG, dành cho cả ngôi nhà thông minh: đồ gia dụng, TV và hơn thế nữa. Nếu bạn chỉ muốn một chiếc điều khiển đơn giản cho TV LG, Mando TV làm đúng việc đó qua Wi-Fi trong nhà, không cần tạo tài khoản LG và không có quảng cáo.',
    pasos=[
      'Kết nối điện thoại hoặc máy tính (iPhone, Android hoặc Windows) và TV LG với cùng một mạng Wi-Fi.',
      'Tải Mando TV và mở lên. TV LG của bạn tự xuất hiện trong danh sách. Hãy chạm vào TV đó.',
      'Trên TV hiện một yêu cầu. Hãy xác nhận một lần bằng điều khiển của TV, cần điều khiển dưới màn hình hoặc Magic Remote.',
      'Phím bấm, âm lượng và bàn phím dùng được ngay. Bạn không cần tài khoản LG và không phải đăng ký TV.',
      'Tùy chọn: bật "Turn on TV with Mobile" trong cài đặt TV để bạn cũng bật được TV từ điện thoại.',
    ],
    extra=[
      ('Mando TV hay LG ThinQ: dùng cái nào cho việc gì', 'Hãy dùng ThinQ nếu bạn muốn quản lý đồ gia dụng LG như máy giặt, tủ lạnh hay máy lạnh, hoặc cần các tính năng của tài khoản LG. Hãy dùng Mando TV nếu bạn muốn một chiếc điều khiển nhanh, đơn giản cho TV, dùng được cả cho Samsung, Roku và Google TV trong cùng một ứng dụng. Nhiều người giữ cả hai: ThinQ cho đồ gia dụng, Mando TV cho TV.'),
      ('Mando TV làm gì trên TV LG', 'Ứng dụng dùng được với Smart TV LG chạy webOS, tức là hầu hết các model từ 2014, gồm LED, NanoCell, QNED và OLED. Ứng dụng có phím mũi tên, OK, Quay lại, Home, âm lượng, kênh, tắt tiếng, điều khiển phát và một bàn phím để gõ trong phần tìm kiếm của TV và hầu hết ứng dụng. Danh sách ứng dụng và danh sách nguồn vào cũng miễn phí. Với Pro, bạn có thêm con trỏ như Magic Remote.'),
      ('Những gì Mando TV không làm', 'Ứng dụng không điều khiển đồ gia dụng LG, không dùng tài khoản LG của bạn và không thay thế các dịch vụ tài khoản LG trên TV. Đây là một chiếc điều khiển, không phải trung tâm nhà thông minh.'),
      ('Quyền riêng tư và quảng cáo', 'Mando TV không có quảng cáo và không có tài khoản. Ứng dụng chỉ trò chuyện với TV trong mạng gia đình của bạn và lưu khóa kết nối được mã hóa trên thiết bị của bạn. Bạn xem toàn bộ tính năng trên trang [Ứng dụng điều khiển TV LG](@lg).'),
      ('Miễn phí và Pro', 'Phím mũi tên, OK, Quay lại, Home, âm lượng, kênh, phím số, bàn phím, mở ứng dụng, đổi nguồn vào và bật/tắt đều miễn phí, không quảng cáo và không đăng ký. Touchpad, lệnh thoại, ứng dụng yêu thích, quy trình và hẹn giờ tắt là một phần của Mando TV Pro, gói mua một lần không cần đăng ký.'),
    ],
    marca='lg',
    faq=[
      ('Tôi có thể điều khiển TV LG mà không cần ứng dụng LG ThinQ không?', 'Có. Mando TV kết nối trực tiếp qua Wi-Fi với TV LG chạy webOS. Bạn chấp nhận một yêu cầu trên TV một lần là xong, hoàn toàn không cần tài khoản LG.'),
      ('Mando TV có dùng được với con trỏ của LG Magic Remote không?', 'Mando TV Pro có con trỏ mà bạn di chuyển bằng ngón tay trên màn hình điện thoại, tương tự cách Magic Remote di chuyển mũi tên.'),
      ('Mando TV có phải của LG không?', 'Không. Mando TV là ứng dụng độc lập và không liên kết với LG. LG và ThinQ thuộc về chủ sở hữu và chỉ được nhắc đến để mô tả khả năng tương thích.'),
    ]),
  dict(clave='smartthings', corto='Lựa chọn thay thế SmartThings', fecha='2026-11-23',
    titulo='SmartThings không chạy? Lựa chọn đơn giản cho Samsung',
    desc='SmartThings quá chậm hoặc bị lỗi? Mando TV điều khiển TV Samsung Tizen trực tiếp qua Wi-Fi. Không tài khoản Samsung, không quảng cáo. Từng bước một.',
    h1='Lựa chọn thay thế SmartThings cho TV Samsung',
    intro='SmartThings là ứng dụng của Samsung cho cả ngôi nhà thông minh, và phần điều khiển của nó chạy qua tài khoản Samsung của bạn. Khi nó không còn hoạt động hoặc bạn cần một giải pháp nhanh, Mando TV điều khiển TV Samsung chạy Tizen, sản xuất từ 2016 trở lên, trực tiếp qua Wi-Fi mà không cần tài khoản.',
    pasos=[
      'Kết nối điện thoại và TV Samsung với cùng một mạng Wi-Fi.',
      'Tải Mando TV và mở ứng dụng. TV Samsung của bạn tự xuất hiện trong danh sách. Hãy chạm vào TV đó.',
      'TV hỏi bạn có cho phép kết nối không. Dùng điều khiển hoặc nút trên TV để chọn "Allow" (chỉ lần đầu tiên).',
      'Dùng ngay phím mũi tên, OK, Quay lại, Home, âm lượng, kênh và bàn phím.',
      'Tùy chọn: bật "Power On with Mobile" trong Settings > General > Network > Expert Settings để Mando TV cũng bật được TV.',
    ],
    extra=[
      ('Vì sao điều khiển trên điện thoại không còn hoạt động', 'Nguyên nhân thường đơn giản: điện thoại và TV ở các mạng Wi-Fi khác nhau, VPN đang bật hoặc TV đang ở chế độ chờ sâu. Với SmartThings, tài khoản Samsung cũng có thể gây lỗi, chẳng hạn khi bạn bị đăng xuất. Mando TV trò chuyện trực tiếp với TV trong mạng gia đình, không có tài khoản nào để đăng nhập. Xem thêm mẹo tại [Điện thoại không tìm thấy TV](@not-found).'),
      ('Mando TV hay SmartThings: dùng cái nào cho việc gì', 'Hãy giữ SmartThings nếu bạn dùng nó cho đồ gia dụng Samsung, đèn hay các thiết bị nhà thông minh khác, hoặc cho các tính năng của tài khoản Samsung. Hãy dùng Mando TV nếu bạn chỉ cần một chiếc điều khiển nhanh cho TV, hoặc trong nhà còn có thiết bị LG, Roku, Google TV hay Fire TV: một ứng dụng điều khiển tất cả. Cả hai ứng dụng có thể cài trên cùng một điện thoại.'),
      ('Nếu bạn lỡ từ chối quyền', 'Trên TV, hãy vào Settings > General > External Device Manager > Device Connection Manager và cho phép Mando TV.'),
      ('Không có điều khiển?', 'Bạn có thể xác nhận yêu cầu bằng nút trên chính TV. Hướng dẫn [TV Samsung không có điều khiển gốc](@samsung-lost) chỉ bạn cách làm.'),
      ('Miễn phí và Pro', 'Bạn tải và dùng điều khiển miễn phí, không quảng cáo và không đăng ký. Mando TV Pro là gói mua một lần tùy chọn cho các tính năng bổ sung.'),
    ],
    marca='samsung',
    faq=[
      ('Tôi có thể điều khiển TV Samsung mà không cần SmartThings không?', 'Có. Mando TV kết nối trực tiếp qua Wi-Fi với TV Samsung chạy Tizen. Bạn cho phép kết nối một lần trên TV, không cần tài khoản Samsung.'),
      ('Mando TV có điều khiển cả đồ gia dụng Samsung không?', 'Không. Đây chỉ là điều khiển cho TV. Với đồ gia dụng và các thiết bị nhà thông minh khác, bạn giữ SmartThings.'),
      ('Mando TV có phải của Samsung không?', 'Không. Mando TV là ứng dụng độc lập và không liên kết với Samsung. Samsung và SmartThings thuộc về chủ sở hữu và chỉ được nhắc đến để mô tả khả năng tương thích.'),
    ]),
  dict(clave='googletv-alt', corto='Lựa chọn thay thế điều khiển Google TV', fecha='2026-11-23',
    titulo='Điều khiển Google TV không chạy? Lựa chọn thay thế',
    desc='Điều khiển Google TV trên điện thoại không tìm thấy TV? Mando TV điều khiển Google TV và Android TV qua Wi-Fi, không tài khoản Google, không quảng cáo.',
    h1='Lựa chọn thay thế điều khiển Google TV trên điện thoại',
    intro='Điều khiển trên điện thoại cho Google TV và Android TV nằm ngay trong ứng dụng của Google và gắn với tài khoản Google của bạn. Nếu nó không tìm thấy TV, bạn đành bó tay. Mando TV là một ứng dụng điều khiển riêng, ghép nối bằng mã 6 ký tự trên màn hình và hoạt động không cần tài khoản Google, trên iPhone, điện thoại Android hoặc máy tính Windows.',
    pasos=[
      'Bật TV và kết nối điện thoại với cùng một mạng Wi-Fi.',
      'Tải Mando TV và mở ứng dụng. Chạm vào TV Google TV hoặc Android TV của bạn trong danh sách.',
      'TV hiện một mã gồm 6 ký tự. Nhập mã vào Mando TV và chạm vào Ghép nối.',
      'Dùng phím mũi tên, OK, Quay lại, Home, âm lượng và bàn phím. Bạn không phải đăng nhập ở đâu cả.',
      'Tùy chọn: tìm trong cài đặt TV mục Wake on LAN hoặc "Wake on network" để ứng dụng cũng bật được TV.',
    ],
    extra=[
      ('Vì sao điều khiển trên điện thoại không còn tìm thấy TV', 'Thường là do mạng: điện thoại và TV ở các mạng Wi-Fi khác nhau, VPN đang bật hoặc mạng khách cách ly các thiết bị. Hãy xử lý việc này trước, vì nó ảnh hưởng đến mọi ứng dụng điều khiển. Xem thêm tại [Điện thoại không tìm thấy TV](@not-found).'),
      ('Dùng được với những TV nào', 'TV chạy Google TV và Android TV của Sony, TCL, Hisense, Philips, Sharp, Xiaomi, Toshiba và nhiều hãng khác, cùng Chromecast với Google TV, Google TV Streamer và Nvidia Shield. Tất cả đều ghép nối theo cùng cách, một lần bằng mã trên màn hình.'),
      ('Ứng dụng của Google tốt hơn ở đâu', 'Ứng dụng của Google còn giúp bạn tìm nội dung để xem và nhớ danh sách xem sau của bạn. Hãy giữ nó cho việc đó. Mando TV chỉ là điều khiển, và còn điều khiển cả Samsung, LG, Roku và thiết bị Fire TV từ cùng một ứng dụng, cũng như từ máy tính Windows.'),
      ('Nếu thiếu ứng dụng điều khiển Android TV cũ', 'Google đã chuyển phần điều khiển trên điện thoại từ ứng dụng Android TV Remote Control cũ sang ứng dụng Google TV. Nếu bạn cần một ứng dụng điều khiển độc lập, Mando TV là một lựa chọn.'),
      ('Miễn phí và Pro', 'Bạn tải và dùng điều khiển miễn phí, không quảng cáo và không đăng ký. Mando TV Pro là gói mua một lần tùy chọn cho các tính năng bổ sung.'),
    ],
    marca='android',
    faq=[
      ('Tôi có cần tài khoản Google để dùng Mando TV với Google TV không?', 'Không. Mã trên TV là đủ để ghép nối.'),
      ('Có dùng được với Chromecast với Google TV không?', 'Có. Việc ghép nối diễn ra giống hệt, bằng mã 6 ký tự trên màn hình.'),
      ('Tôi có thể dùng từ iPhone không?', 'Có. Mando TV có trên App Store cho iPhone và iPad, trên Microsoft Store cho Windows và trong chương trình truy cập sớm miễn phí trên Google Play cho Android.'),
    ]),
  dict(clave='windows', corto='Điều khiển cho máy tính Windows', fecha='2026-11-23',
    titulo='Ứng dụng điều khiển TV cho Windows: điều khiển TV từ máy tính',
    desc='Điều khiển Samsung, LG, Roku, Google TV hoặc Fire TV từ máy tính Windows với Mando TV: phím tắt, điều khiển mini và Wi-Fi. Có trên Microsoft Store.',
    h1='Ứng dụng điều khiển TV cho máy tính Windows',
    intro='Mando TV có ứng dụng cho Windows, biến máy tính hoặc laptop của bạn thành điều khiển cho TV qua mạng gia đình. Gõ trên TV bằng bàn phím thật, để một cửa sổ điều khiển nhỏ luôn nằm trên cùng khi làm việc và điều khiển Samsung, LG, Roku, Google TV hoặc Fire TV bằng cùng một ứng dụng.',
    pasos=[
      'Cài Mando TV miễn phí từ Microsoft Store trên máy tính chạy Windows 10 hoặc 11.',
      'Đảm bảo máy tính và TV ở cùng một mạng, qua Wi-Fi hoặc dây mạng nối vào cùng một router.',
      'Mở Mando TV. TV hiện trong danh sách. Hãy nhấp vào TV đó.',
      'Xác nhận yêu cầu trên TV nếu TV hỏi (LG, Samsung), hoặc nhập mã hiện ra (Google TV, Fire TV).',
      'Nhấp vào các phím hoặc gõ nội dung tìm kiếm bằng bàn phím của bạn. Xong.',
    ],
    extra=[
      ('Phím tắt (Pro)', 'Với Pro, bàn phím máy tính trở thành điều khiển: phím mũi tên để di chuyển, Enter cho OK, Backspace hoặc Esc để quay lại, Plus và Minus cho âm lượng, M để tắt tiếng và phím cách để tạm dừng.'),
      ('Điều khiển mini (Pro)', 'Một cửa sổ điều khiển nhỏ luôn nằm trên mọi cửa sổ khác. Nhờ vậy bạn chỉnh âm lượng hoặc tạm dừng mà không làm gián đoạn công việc.'),
      ('Gõ trên TV từ máy tính', 'Bàn phím trên màn hình của TV rất chậm. Trong Mando TV, bạn gõ bằng bàn phím thật và nội dung hiện vào ô tìm kiếm của TV. Phần này miễn phí.'),
      ('Xem thêm chi tiết', 'Hướng dẫn từng bước có tại [Điều khiển TV bằng máy tính](@pc). Với điện thoại, hãy đọc [Điện thoại làm điều khiển qua Wi-Fi](@wifi).'),
      ('Miễn phí và Pro', 'Phím mũi tên, OK, Quay lại, Home, âm lượng, kênh, phím số, bàn phím, mở ứng dụng, đổi nguồn vào và bật hoặc tắt TV đều miễn phí, không quảng cáo và không đăng ký. Touchpad, lệnh thoại, ứng dụng yêu thích, quy trình và hẹn giờ tắt là một phần của Mando TV Pro, gói mua một lần không cần đăng ký. Trên Windows, bạn mua Pro qua Microsoft Store.'),
      ('Lệnh bằng giọng nói từ máy tính (Pro)', 'Với Pro, bạn có thể nói chuyện với TV qua micro của máy tính. Giọng nói được nhận dạng ngay trên máy tính: bạn không cần internet và không phải cài đặt gì trong Windows. Những gì bạn nói không bao giờ rời khỏi máy tính và không được lưu. Chỉ với bộ xử lý rất cũ, ứng dụng mới chuyển sang tính năng nhập bằng giọng nói của Windows. Khi đó cần bật nhận dạng giọng nói trực tuyến trong cài đặt quyền riêng tư và thêm ngôn ngữ của bạn vào Windows.'),
    ],
    marca=None,
    faq=[
      ('Ứng dụng điều khiển cho Windows có cần Bluetooth hay dây cáp không?', 'Không. Ứng dụng dùng mạng gia đình của bạn. Máy tính và TV chỉ cần nối vào cùng một router.'),
      ('Tôi điều khiển được những TV nào từ Windows?', 'TV Samsung chạy Tizen, TV LG chạy webOS, Roku TV và Player, Google TV và Android TV, cùng Fire TV.'),
      ('Tôi có xem được hình TV trên máy tính hoặc nghe qua loa máy tính không?', 'Không. Mando TV chỉ là điều khiển. Ứng dụng không phản chiếu hay phát hình TV lên máy tính.'),
      ('Tại sao giọng nói không chạy trên máy tính Windows của tôi?', 'Điều khiển bằng giọng nói là tính năng Pro. Vì vậy hãy kiểm tra Pro đang hoạt động và micro của máy tính dùng được. Trên hầu hết máy tính, giọng nói được nhận dạng ngay trên máy mà không cần internet. Chỉ với bộ xử lý rất cũ, ứng dụng mới dùng tính năng nhập bằng giọng nói của Windows: khi đó hãy bật nhận dạng giọng nói trực tuyến trong cài đặt quyền riêng tư của Windows và thêm ngôn ngữ của bạn trong cài đặt ngôn ngữ.'),
    ]),
  dict(clave='iphone', corto='Ứng dụng điều khiển cho iPhone', fecha='2026-11-23',
    titulo='Ứng dụng điều khiển TV cho iPhone: Samsung, LG, Roku, Google TV',
    desc='Dùng iPhone làm điều khiển cho Samsung, LG, Roku, Google TV và Fire TV qua Wi-Fi. Miễn phí trên App Store, không tài khoản, không quảng cáo.',
    h1='Ứng dụng điều khiển TV cho iPhone: một ứng dụng cho mọi TV',
    intro='Mando TV biến iPhone hoặc iPad của bạn thành điều khiển cho Samsung, LG, Roku, Google TV hoặc Android TV và Fire TV, qua Wi-Fi trong nhà. Ứng dụng miễn phí trên App Store, không cần tài khoản và không quảng cáo. Ứng dụng cũng chạy trên Android và Windows.',
    pasos=[
      'Tải Mando TV miễn phí từ App Store.',
      'Kết nối iPhone và TV với cùng một mạng Wi-Fi.',
      'Mở Mando TV và chạm vào Cho phép khi iOS hỏi quyền truy cập mạng cục bộ. Ứng dụng cần quyền này để tìm thấy TV.',
      'Chạm vào TV của bạn trong danh sách. Xác nhận yêu cầu trên TV nếu TV hỏi (LG và Samsung), hoặc nhập mã mà TV hiện ra (Google TV hoặc Fire TV).',
      'Dùng các phím, âm lượng và bàn phím. Bạn đã kết nối xong.',
    ],
    extra=[
      ('Dùng được với những TV này', 'LG webOS, Samsung Tizen (sản xuất từ 2016 trở lên), Roku TV và Roku Player, Google TV và Android TV, cùng Fire TV. Các trang theo hãng là [Samsung](@samsung), [LG](@lg), [Roku](@roku) và [Android TV](@android).'),
      ('Vì sao ứng dụng hỏi về mạng cục bộ', 'iPhone chặn ứng dụng truy cập các thiết bị trong mạng gia đình của bạn, trừ khi bạn cho phép. Nếu TV không hiện trong danh sách, hãy mở Cài đặt > Mando TV và bật "Local Network". Ứng dụng chỉ trò chuyện với TV của bạn trong mạng gia đình.'),
      ('Vì sao dùng Mando TV thay vì ứng dụng của hãng', 'Mỗi hãng TV có ứng dụng riêng và muốn bạn thiết lập hoặc tạo tài khoản riêng. Mando TV là một ứng dụng cho tất cả, không cần tài khoản.'),
      ('Miễn phí và Pro trên iPhone', 'Phím mũi tên, OK, Quay lại, Home, âm lượng, kênh, phím số, bàn phím, mở ứng dụng, đổi nguồn vào và bật hoặc tắt TV đều miễn phí, không quảng cáo và không đăng ký. Touchpad, lệnh thoại, ứng dụng yêu thích, quy trình và hẹn giờ tắt là một phần của Mando TV Pro, gói mua một lần không cần đăng ký. Bạn mua Pro một lần ngay trong ứng dụng.'),
    ],
    marca=None,
    faq=[
      ('Mando TV trên iPhone có miễn phí không?', 'Tải về miễn phí, không quảng cáo. Điều khiển cơ bản miễn phí, cũng như mở ứng dụng và đổi nguồn vào. Các tính năng bổ sung như touchpad, lệnh thoại và quy trình thuộc Mando TV Pro, gói mua một lần.'),
      ('Có dùng được trên iPad không?', 'Có. Cùng một ứng dụng chạy trên iPhone và iPad.'),
      ('Ứng dụng điều khiển cho iPhone có cần Bluetooth hay bộ phát hồng ngoại không?', 'Không trên iPhone. iPhone không có bộ phát hồng ngoại nên điều khiển hồng ngoại không có ở đó, và tùy chọn Bluetooth chỉ dành cho Android 9 trở lên, không dành cho iPhone. Trên iPhone, Mando TV điều khiển Smart TV và Apple TV (beta) qua Wi-Fi trong nhà.'),
    ]),
  dict(clave='firetv', corto='Điều khiển Fire TV', fecha='2026-11-23',
    titulo='Ứng dụng điều khiển Fire TV cho điện thoại và máy tính',
    desc='Điều khiển Fire TV trên điện thoại: điều khiển Fire TV Stick, Fire TV Cube hoặc TV có Fire TV qua Wi-Fi, ghép nối bằng PIN 4 chữ số. Không cần ứng dụng Amazon.',
    h1='Điều khiển Fire TV cho điện thoại hoặc máy tính của bạn',
    intro='Khi điều khiển Fire TV bị mất hoặc hết pin, Mando TV điều khiển Fire TV Stick, Fire TV Cube hoặc TV có Fire TV tích hợp qua Wi-Fi. Việc ghép nối dùng PIN 4 chữ số. Fire TV là tính năng mới trong Mando TV, vì vậy hãy cập nhật ứng dụng trước.',
    pasos=[
      'Cập nhật Mando TV lên phiên bản mới nhất từ App Store, Microsoft Store hoặc Google Play.',
      'Bật Fire TV và kết nối điện thoại với cùng một mạng Wi-Fi.',
      'Mở Mando TV. Fire TV của bạn hiện trong danh sách. Hãy chạm vào đó.',
      'Trên màn hình TV hiện một PIN 4 chữ số. Hãy nhập PIN vào Mando TV. Bạn chỉ làm việc này một lần.',
      'Dùng phím mũi tên, OK, Quay lại, Home, các phím phát và bàn phím để tìm kiếm.',
    ],
    extra=[
      ('Các thiết bị Fire TV được hỗ trợ', 'Fire TV Stick, Fire TV Stick 4K, Fire TV Cube và TV có Fire TV tích hợp, như TV Amazon Fire TV Edition và một số model Hisense. Việc hỗ trợ còn mới và cho đến nay chúng tôi mới thử được trên rất ít thiết bị thật. Nếu có gì không hoạt động như mong đợi, hãy cho chúng tôi biết model của bạn qua trang trợ giúp.'),
      ('Bật Fire TV', 'Mando TV không bật Fire TV qua mạng. Hãy bật TV bằng nút nguồn trên máy: Fire TV Stick hoặc Cube đang cắm thường tự thức dậy nhờ HDMI-CEC, còn với TV có Fire TV tích hợp thì chính TV là Fire TV. Sau đó bạn điều khiển từ điện thoại.'),
      ('Nếu Fire TV của bạn không hiện', 'Hãy đảm bảo cả hai thiết bị ở cùng Wi-Fi và Fire TV đang thức. Trên iPhone, hãy cho phép "Local Network" cho Mando TV trong Cài đặt. Xem [Điện thoại không tìm thấy TV](@not-found).'),
      ('Không có điều khiển nào cả?', 'Fire TV cần hiện PIN trên màn hình, vì vậy TV và Fire TV phải bật và có hình. Nếu TV đang ở nguồn vào sai, hãy đổi bằng các nút trên TV. Xem [Đổi nguồn vào khi không có điều khiển](@hdmi).'),
      ('Miễn phí và Pro', 'Phím mũi tên, OK, Quay lại, Home, âm lượng, kênh, phím số, bàn phím, mở ứng dụng, đổi nguồn vào và bật/tắt đều miễn phí, không quảng cáo và không đăng ký. Touchpad, lệnh thoại, ứng dụng yêu thích, quy trình và hẹn giờ tắt là một phần của Mando TV Pro, gói mua một lần không cần đăng ký.'),
    ],
    marca=None,
    faq=[
      ('Tôi có cần ứng dụng Amazon Fire TV không?', 'Không. Mando TV kết nối với Fire TV qua Wi-Fi của bạn bằng PIN. Bạn không cần tài khoản Amazon trên điện thoại.'),
      ('Có dùng được với TV có Fire TV và với Fire TV Stick không?', 'Có, ứng dụng được tạo ra đúng cho việc đó. Việc hỗ trợ còn mới, hãy luôn cập nhật ứng dụng và báo cho chúng tôi những model không hoạt động như mong đợi.'),
      ('Tại sao tôi cần PIN?', 'Fire TV hiện một PIN 4 chữ số để chứng minh bạn đang ngồi trước TV. Không ai ghép nối được nếu không nhìn thấy màn hình.'),
    ]),
  dict(clave='firetv-lost', corto='Mất điều khiển Fire TV', fecha='2026-11-23',
    titulo='Mất điều khiển Fire TV? Điện thoại giúp bạn thế nào',
    desc='Mất điều khiển Fire TV Stick? Điều khiển qua Wi-Fi bằng điện thoại, ghép nối bằng PIN 4 chữ số. Mẹo khi đổi Wi-Fi và HDMI-CEC.',
    h1='Mất điều khiển Fire TV: cách dùng điện thoại thay thế',
    intro='Nếu điều khiển của Fire TV Stick, Fire TV Cube hoặc Smart TV có Fire TV bị mất hay không còn hoạt động, điện thoại sẽ đảm nhận việc điều khiển miễn là Fire TV vẫn kết nối với Wi-Fi của bạn. Việc ghép nối dùng PIN 4 chữ số trên màn hình, nên bạn không bao giờ cần đến điều khiển cũ.',
    pasos=[
      'Bật TV bằng nút trên máy. Fire TV Stick hoặc Cube đang cắm thường thức dậy theo; khi HDMI-CEC được bật, TV thường tự chuyển sang nguồn vào của nó.',
      'Nếu TV hiện nguồn vào khác, hãy đổi bằng nút nguồn vào hoặc nút Source trên TV. Xem [Đổi nguồn vào khi không có điều khiển](@hdmi).',
      'Kết nối điện thoại với cùng Wi-Fi của Fire TV.',
      'Tải Mando TV và mở ứng dụng. Fire TV của bạn hiện trong danh sách. Hãy chạm vào đó.',
      'TV hiện một PIN 4 chữ số. Hãy nhập PIN vào Mando TV. Bạn chỉ làm việc này một lần.',
      'Dùng phím mũi tên, OK, Quay lại, Home, âm lượng, các phím phát và bàn phím trên điện thoại của bạn.',
    ],
    extra=[
      ('Thử điều khiển của TV trước (HDMI-CEC)', 'Nhiều điều khiển TV có thể điều khiển Fire TV Stick qua HDMI-CEC. Khi thấy giao diện Fire TV, hãy bấm phím mũi tên và OK trên điều khiển của TV. Nếu không có gì xảy ra, hãy bật CEC trong cài đặt của TV (Anynet+ trên Samsung, SIMPLINK trên LG, BRAVIA Sync trên Sony) và trên Fire TV bật HDMI CEC Device Control trong cài đặt hiển thị ("Display & Sounds").'),
      ('Nếu bạn đã đổi Wi-Fi', 'Không có điều khiển, bạn không nhập được mật khẩu Wi-Fi mới trên Fire TV, nhưng có một cách: trên một điện thoại thứ hai, hãy tạo điểm phát Wi-Fi có đúng tên và mật khẩu như Wi-Fi cũ. Fire TV sẽ tự kết nối. Kết nối điện thoại chạy Mando TV vào điểm phát đó, ghép nối bằng PIN, rồi trên Fire TV vào Settings > Network và chọn Wi-Fi mới của bạn. Cuối cùng, hãy kết nối cả điện thoại với Wi-Fi mới.'),
      ('Ghép nối điều khiển thay thế', 'Hầu hết điều khiển Fire TV mới ghép nối bằng cách giữ nút Home khoảng 10 giây, ở gần Fire TV. Nếu không được, hãy mở Settings > Controllers & Bluetooth Devices > Amazon Fire TV Remotes > Add New Remote. Bạn cũng vào được menu này từ điện thoại bằng Mando TV.'),
      ('Fire TV tích hợp trong TV', 'Với TV có Fire TV tích hợp, như nhiều model của Insignia và Toshiba, các bước đều giống nhau vì chính TV là Fire TV.'),
      ('Trước khi bắt đầu', 'Hỗ trợ Fire TV là tính năng mới trong Mando TV. Hãy cập nhật ứng dụng trước. Nếu model của bạn không phản hồi như mong đợi, hãy viết cho chúng tôi qua [trang trợ giúp](@soporte) và cho biết model.'),
      ('Miễn phí và Pro', 'Bạn tải và dùng điều khiển miễn phí, không quảng cáo và không đăng ký. Mando TV Pro là gói mua một lần tùy chọn cho các tính năng bổ sung.'),
    ],
    marca=('firetv', 'Điều khiển Fire TV'),
    faq=[
      ('Tôi có thể điều khiển Fire TV Stick bằng điện thoại khi không có điều khiển không?', 'Có, miễn là Fire TV đang bật và kết nối Wi-Fi của bạn. Mando TV ghép nối bằng PIN 4 chữ số trên TV, nên bạn không cần điều khiển cũ.'),
      ('Có dùng được khi Fire TV đang ở Wi-Fi mới không?', 'Không trực tiếp, vì điện thoại và Fire TV phải ở cùng một mạng. Trước tiên hãy đưa Fire TV trở lại mạng bằng mẹo điểm phát Wi-Fi trên trang này.'),
      ('Tôi có cần ứng dụng Amazon Fire TV hay tài khoản Amazon không?', 'Không. Mando TV kết nối qua mạng gia đình của bạn bằng PIN và không cần tài khoản riêng.'),
    ]),
  dict(clave='turn-on', corto='Bật TV không cần điều khiển', fecha='2026-11-23',
    titulo='Bật TV không cần điều khiển (mọi hãng)',
    desc='Bật TV khi không có điều khiển: nút nguồn nằm ở đâu trên Samsung, LG, TCL, Hisense, Sony và Vizio. Kèm mẹo HDMI-CEC và điện thoại.',
    h1='Cách bật TV khi không có điều khiển',
    intro='Hầu như TV nào cũng còn một nút nguồn vật lý. Chỉ là nó được giấu khá kỹ. Dưới đây là vị trí nút ở từng hãng, cùng hai cách để lần sau khỏi phải tìm: HDMI-CEC từ máy chơi game hoặc thiết bị phát, và bật TV bằng điện thoại qua Wi-Fi.',
    pasos=[
      'Nhìn dưới giữa màn hình, ngay sau logo hãng. Nhiều TV có ở đó một nút nhỏ hoặc một cần điều khiển hướng xuống dưới.',
      'Nếu không có ở đó, hãy mò dọc mặt sau của TV gần các góc dưới, rồi đến cạnh trái và cạnh phải.',
      'Nhấn nút một lần. Ở nhiều TV chỉ có một nút, khi TV đang bật, nhấn ngắn sẽ mở một menu nhỏ để chọn nguồn vào và âm lượng, còn nhấn giữ sẽ tắt TV.',
      'Vẫn không được? Hãy kiểm tra dây nguồn ở cả hai đầu và thử ổ cắm khác. Nếu đèn chờ không sáng, TV không có điện.',
      'Khi TV đã bật, hãy thiết lập để bạn không còn cần đến nút đó nữa: bật HDMI-CEC và bật nguồn qua mạng, cả hai được giải thích bên dưới.',
    ],
    extra=[
      ('Vị trí nút nguồn theo từng hãng', 'Samsung: một nút điều khiển hoặc cần điều khiển dưới giữa màn hình, hoặc ở mặt sau gần một góc dưới. LG: một nút cần điều khiển dưới logo LG ở hầu hết các model. TCL và Hisense: thường là một nút nhỏ dưới giữa màn hình hoặc ở mặt sau gần một góc dưới. Sony: ở mặt sau hoặc cạnh bên, phía dưới sát mép. Vizio: ở mặt sau, phía dưới bên trái hoặc dưới bên phải, hoặc ở cạnh bên. Vị trí thay đổi theo từng model. Nếu không tìm thấy, hãy tra sách hướng dẫn bằng số model ghi trên nhãn ở mặt sau.'),
      ('Bật TV từ máy chơi game hoặc thiết bị phát (HDMI-CEC)', 'Khi HDMI-CEC được bật, việc bật PlayStation, Xbox, Roku Player, Fire TV Stick hoặc Chromecast cũng bật TV và chuyển sang đúng nguồn vào. Mỗi hãng gọi cài đặt này một tên: Anynet+ ở Samsung, SIMPLINK ở LG, BRAVIA Sync ở Sony và CEC ở hầu hết các hãng khác. Xem thêm trong [Bật TV và chuyển sang HDMI của máy chơi game](@console).'),
      ('Bật TV bằng điện thoại', 'Smart TV có thể được đánh thức qua Wi-Fi nếu bạn cho phép một lần, và khi đó Mando TV bật TV từ điện thoại của bạn. Với Samsung, hãy bật "Power On with Mobile" trong Settings > General > Network > Expert Settings. Với LG, hãy bật "Turn on TV with Mobile" ([từng bước](@lg-on)). Với Roku TV, hãy bật "Fast TV start" trong Settings > System > Power. Với Google TV và Android TV, hãy tìm Wake on LAN hoặc "Wake on network" nếu model của bạn có. Bạn chỉ làm một lần, khi TV đang bật.'),
      ('Nếu bạn không tìm thấy nút nào', 'Một số TV đời mới giấu nút duy nhất kỹ đến mức tưởng như không có. Hãy tìm một chỗ lồi nhỏ hoặc vùng cảm biến ánh sáng dưới màn hình: nút thường nằm ngay cạnh đó. Qua Wi-Fi, Mando TV cần TV đã từng bật và đã kết nối. Hồng ngoại là ngoại lệ: trên điện thoại Android có bộ phát hồng ngoại, Mando TV có thể bật một chiếc TV chưa từng được thiết lập, miễn là bạn hướng điện thoại vào TV. Hồng ngoại là tính năng mới và dùng được với các hãng có trong danh sách mã của ứng dụng.'),
      ('Miễn phí và Pro', 'Bạn tải và dùng điều khiển miễn phí, không quảng cáo và không đăng ký. Mando TV Pro là gói mua một lần tùy chọn cho các tính năng bổ sung.'),
    ],
    marca=None,
    faq=[
      ('Tôi có thể bật TV bằng điện thoại nếu chưa từng thiết lập không?', 'Không qua Wi-Fi. TV đang tắt chỉ thức dậy từ mạng khi tính năng bật nguồn qua mạng đã được bật từ trước. Lần đầu hãy dùng nút trên TV. Ngoại lệ là điện thoại Android có bộ phát hồng ngoại: Mando TV có thể bật TV bằng hồng ngoại mà không cần thiết lập, nếu hãng có trong danh sách mã hoặc bạn chọn "Hãng khác hoặc tôi không biết".'),
      ('Làm sao bật TV Samsung khi không có điều khiển?', 'Hãy nhấn nút điều khiển dưới giữa màn hình hoặc ở mặt sau gần một góc dưới. Sau đó bật "Power On with Mobile" để lần sau điện thoại bật được TV.'),
      ('Làm sao bật Roku TV khi không có điều khiển?', 'Hãy dùng nút trên TV, thường ở dưới giữa hoặc mặt sau. Sau đó bật "Fast TV start" trong Settings > System > Power để Mando TV bật được TV từ điện thoại của bạn.'),
      ('Tại sao TV của tôi tự bật khi tôi bật máy chơi game?', 'Đó là HDMI-CEC. Tính năng này rất tiện, và bạn có thể tắt nó trong cài đặt của TV nếu thích.'),
    ]),
  dict(clave='sony', corto='Điều khiển Sony', fecha='2026-11-23',
    titulo='Ứng dụng điều khiển TV Sony cho điện thoại và máy tính',
    desc='Mando TV điều khiển TV Sony Bravia chạy Google TV hoặc Android TV qua Wi-Fi. Hỗ trợ bản beta cho các model 2013 đến 2015 không dùng Android.',
    h1='Cách điều khiển TV Sony bằng điện thoại',
    intro='Các Smart TV Sony Bravia mới dùng Google TV, còn các model cũ từ 2015 dùng Android TV. Mando TV điều khiển cả hai qua Wi-Fi từ iPhone, điện thoại Android hoặc máy tính Windows. Ứng dụng thay thế điều khiển gốc khi nó bị mất hoặc hết pin.',
    pasos=[
      'Kiểm tra TV Sony của bạn có hiện màn hình chính của Google TV hoặc Android TV không. Điều này đúng với hầu hết Smart TV Sony Bravia sản xuất từ 2015.',
      'Kết nối điện thoại và TV với cùng một mạng Wi-Fi.',
      'Mở Mando TV và chạm vào TV Sony của bạn trong danh sách.',
      'Nhập mã 6 ký tự mà TV hiện trên màn hình (chỉ lần đầu tiên). Bạn không cần điều khiển cho bước này.',
      'Dùng phím mũi tên, OK, Quay lại, Home, âm lượng và bàn phím.',
    ],
    extra=[
      ('Bật TV Sony từ điện thoại', 'Các model Sony chạy Google TV hoặc Android TV có thể được đánh thức qua mạng khi "Remote start" được bật. Tùy chọn này thường nằm trong Settings > Network & Internet > Remote start (đường dẫn có thể hơi khác tùy model). Sau đó, trong Mando TV hãy chạm vào TV khi TV đang tắt và ứng dụng sẽ bật TV.'),
      ('Nút nguồn của TV Sony nằm ở đâu', 'Ở hầu hết các TV Bravia, nút nằm ở mặt sau, gần góc dưới bên trái hoặc bên phải, hoặc ở một cạnh bên. Nhấn ngắn sẽ bật TV. Xem thêm trong [Bật TV không cần điều khiển](@turn-on).'),
      ('TV Sony đời cũ', 'Các TV Sony Bravia từ 2013 đến 2015 không dùng Android được Mando TV hỗ trợ ở trạng thái beta. Tính năng này còn mới và có thể chưa hoàn thiện. TV hiện một PIN 4 chữ số mà bạn cần nhập vào ứng dụng. Các TV Sony khác không có Google TV hoặc Android TV hiện chưa được hỗ trợ.'),
      ('Miễn phí và Pro', 'Bạn tải và dùng điều khiển miễn phí, không quảng cáo và không đăng ký. Mando TV Pro là gói mua một lần tùy chọn cho các tính năng bổ sung.'),
    ],
    marca='android',
    faq=[
      ('Mando TV có dùng được với TV Sony Bravia không?', 'Có, với các TV Sony chạy Google TV hoặc Android TV. Điều này bao gồm hầu hết Smart TV Sony sản xuất từ 2015.'),
      ('Tôi có cần ứng dụng Sony hay tài khoản Google không?', 'Không. Mando TV ghép nối bằng mã trên màn hình TV và không đòi tài khoản.'),
      ('Có dùng được với TV Sony Bravia đời cũ không dùng Android không?', 'Có, ở trạng thái beta, với các model Bravia từ 2013 đến 2015 không dùng Android. Việc ghép nối dùng PIN 4 chữ số hiện trên TV.'),
      ('Tôi có thể gõ từ điện thoại trên TV Sony không?', 'Có. Bàn phím điện thoại miễn phí và gõ được vào ô tìm kiếm của TV và các ô văn bản khác. Với YouTube, Mando TV còn có Bàn phím YouTube: gõ hoặc nói bạn muốn xem gì, YouTube sẽ mở trên TV với kết quả. Netflix chỉ nhận bàn phím trên màn hình của riêng nó, nên ở đó hãy dùng phím mũi tên và OK.'),
    ]),
  dict(clave='tcl', corto='Điều khiển TCL', fecha='2026-11-23',
    titulo='Ứng dụng điều khiển TV TCL cho điện thoại và máy tính',
    desc='Mất điều khiển TCL? Hầu hết TV TCL dùng Roku TV hoặc Google TV. Mando TV điều khiển cả hai qua Wi-Fi, không tài khoản, không quảng cáo.',
    h1='Cách điều khiển TV TCL bằng điện thoại',
    intro='TCL sản xuất TV, nhưng phần mềm là Roku TV hoặc Google TV (ở các model cũ là Android TV). Mando TV điều khiển cả hai hệ thống và hoạt động như điều khiển cho TV TCL của bạn qua Wi-Fi. Miễn phí, không tài khoản, không quảng cáo.',
    pasos=[
      'Tìm hiểu TV TCL của bạn dùng hệ thống nào. Nếu màn hình chính là một lưới đơn giản gồm các ô kênh thì đó là Roku TV. Nếu giống Google TV hoặc Android TV với các hàng đề xuất thì đó là Google TV.',
      'Kết nối điện thoại và TV TCL với cùng một mạng Wi-Fi.',
      'Mở Mando TV. TV TCL tự xuất hiện trong danh sách. Hãy chạm vào đó.',
      'Với TCL dùng Roku TV, bạn không cần làm gì thêm. Với TCL dùng Google TV, bạn nhập mã 6 ký tự mà TV hiện trên màn hình (chỉ lần đầu tiên).',
      'Dùng phím mũi tên, OK, Quay lại, Home, âm lượng và bàn phím. Hãy bật TV từ ứng dụng nếu bạn đã bật tính năng bật nguồn qua mạng (xem bên dưới).',
    ],
    extra=[
      ('Bật TV TCL từ điện thoại', 'Với TCL Roku TV, hãy bật "Fast TV start" trong Settings > System > Power. Với TCL Google TV, hãy tìm tùy chọn Wake on LAN, "Wake on network" hoặc khởi động từ xa trong cài đặt mạng hoặc nguồn điện. Một số model không có tùy chọn này. Khi đó, hãy bật TV bằng nút nguồn vật lý, thường ở dưới giữa hoặc ở mặt sau.'),
      ('Nếu TV TCL của bạn không hiện', 'Kiểm tra điện thoại và TV có cùng Wi-Fi không. Router có mạng 2,4 GHz và 5 GHz tách riêng có thể làm các thiết bị không thấy nhau. Trên iPhone, hãy cho phép "Local Network" cho Mando TV trong Cài đặt. Bạn cũng có thể thêm TV bằng cách nhập địa chỉ IP của nó. Hãy đọc [Điện thoại không tìm thấy TV](@not-found).'),
      ('Xem thêm về TCL của bạn', 'Với TCL dùng Roku TV, xem [Ứng dụng điều khiển Roku](@roku), với TCL dùng Google TV hoặc Android TV, xem [Ứng dụng điều khiển Android TV](@android).'),
      ('Miễn phí và Pro', 'Phím mũi tên, OK, Quay lại, Home, âm lượng, kênh, phím số, bàn phím, mở ứng dụng, đổi nguồn vào và bật/tắt đều miễn phí, không quảng cáo và không đăng ký. Touchpad, lệnh thoại, ứng dụng yêu thích, quy trình và hẹn giờ tắt là một phần của Mando TV Pro, gói mua một lần không cần đăng ký.'),
    ],
    marca=None,
    faq=[
      ('Mando TV có dùng được với mọi TV TCL không?', 'Ứng dụng dùng được với TV TCL chạy Roku TV, Google TV hoặc Android TV, tức là hầu hết Smart TV TCL. TV TCL không phải Smart TV thì không điều khiển được qua Wi-Fi.'),
      ('Tôi có cần ứng dụng TCL hay tài khoản TCL không?', 'Không. Mando TV kết nối trực tiếp qua Wi-Fi trong nhà bạn và không cần tài khoản.'),
      ('TV TCL của tôi yêu cầu mã. Mã ở đâu?', 'Các model TCL dùng Google TV và Android TV hiện mã 6 ký tự trên màn hình. Hãy nhập đúng như vậy vào Mando TV. TCL dùng Roku TV không yêu cầu mã.'),
    ]),
  dict(clave='hisense', corto='Điều khiển Hisense', fecha='2026-11-23',
    titulo='Ứng dụng điều khiển Hisense: điện thoại làm được gì',
    desc='Điều khiển Hisense với Mando TV: điều khiển VIDAA, Roku TV, Google TV và Fire TV qua Wi-Fi. Tổng quan trung thực về những gì hoạt động.',
    h1='Ứng dụng điều khiển Hisense: cái gì chạy được và cái gì không',
    intro='TV Hisense không phải chiếc nào bên trong cũng giống nhau. Tùy model, chúng dùng hệ thống VIDAA riêng của Hisense, Roku TV, Google TV hoặc Fire TV. Mando TV hoạt động như điều khiển cho Hisense trên cả bốn hệ thống, với một ngoại lệ ở vài model VIDAA mới hơn. Dưới đây là cách nhận biết bạn dùng hệ thống nào và điều bạn có thể mong đợi.',
    pasos=[
      'Kiểm tra TV Hisense của bạn dùng hệ thống nào. VIDAA là giao diện riêng của Hisense. Roku TV hiện một lưới các ô kênh. Google TV hiện các hàng đề xuất. Fire TV hiện màn hình chính Fire TV với các hàng của Amazon.',
      'Kết nối điện thoại và TV Hisense với cùng một mạng Wi-Fi.',
      'Mở Mando TV. TV tự xuất hiện trong danh sách. Hãy chạm vào đó.',
      'Các model VIDAA và Fire TV có thể hiện một PIN bốn chữ số; Google TV hiện một mã sáu ký tự. Hãy nhập vào ứng dụng. Roku TV không hỏi gì cả. Bạn chỉ làm việc này một lần.',
      'Dùng phím mũi tên, OK, Quay lại, Home, âm lượng và bàn phím từ điện thoại của bạn.',
    ],
    extra=[
      ('Hisense dùng Roku TV hoặc Google TV', 'Chúng hoạt động đầy đủ như mọi TV Roku hay Google TV khác. Chi tiết trên các trang [Ứng dụng điều khiển Roku](@roku) và [Ứng dụng điều khiển Android TV](@android).'),
      ('Hisense dùng Fire TV', 'Hỗ trợ Fire TV là tính năng mới trong Mando TV. Hãy cập nhật ứng dụng lên phiên bản mới nhất từ cửa hàng của bạn. Cách ghép nối bằng PIN có trên trang [Ứng dụng điều khiển Fire TV](@firetv). Nếu có gì không hoạt động như mong đợi, hãy viết cho chúng tôi qua trang trợ giúp và cho biết model của bạn.'),
      ('Hisense dùng VIDAA', 'Hầu hết các model VIDAA đều dùng được: phím bấm, âm lượng, bàn phím, ứng dụng và nguồn vào. Một số model VIDAA mới hơn chỉ chấp nhận ứng dụng chính thức của Hisense. Mando TV nhận ra điều này khi kết nối và nói rõ cho bạn, thay vì âm thầm không chạy. Trong trường hợp đó, ứng dụng Hisense dành cho model của bạn, các nút trên TV hoặc điều khiển gốc là cách đúng.'),
      ('Bật Hisense từ điện thoại', 'Với Hisense Roku TV, hãy bật "Fast TV start" trong Settings > System > Power. Với Google TV, hãy tìm tùy chọn Wake on LAN hoặc "Wake on network". Nếu không có, hãy dùng nút nguồn trên TV.'),
      ('Miễn phí và Pro', 'Phím mũi tên, OK, Quay lại, Home, âm lượng, kênh, phím số, bàn phím, mở ứng dụng, đổi nguồn vào và bật hoặc tắt TV đều miễn phí, không quảng cáo và không đăng ký. Touchpad, lệnh thoại, ứng dụng yêu thích, quy trình và hẹn giờ tắt là một phần của Mando TV Pro, gói mua một lần không cần đăng ký.'),
    ],
    marca=None,
    faq=[
      ('Mando TV có dùng được với Hisense VIDAA không?', 'Có, với hầu hết các model VIDAA. Một số model mới hơn chỉ chấp nhận ứng dụng chính thức của Hisense; Mando TV nhận ra điều đó và báo cho bạn. TV Hisense dùng Roku TV, Google TV hoặc Fire TV cũng được hỗ trợ.'),
      ('Làm sao biết Hisense của tôi dùng Roku TV, Google TV hay Fire TV?', 'Hãy nhìn màn hình chính. Roku TV có một lưới ô đơn giản và logo Roku khi khởi động. Google TV có các hàng đề xuất. Fire TV có màn hình chính của Amazon Fire TV. Tên model trong Settings > About cũng cho bạn biết.'),
      ('Tôi có cần tài khoản Hisense hay Google không?', 'Không. Mando TV kết nối trực tiếp qua Wi-Fi trong nhà bạn và không có tài khoản riêng.'),
    ]),
  dict(clave='philips', corto='Điều khiển Philips', fecha='2026-11-23',
    titulo='Ứng dụng điều khiển Philips: Roku TV, Google TV, Android TV',
    desc='Mando TV điều khiển TV Philips chạy Roku TV, Google TV hoặc Android TV qua Wi-Fi, từ điện thoại hoặc máy tính. Titan OS chưa được hỗ trợ.',
    h1='Điều khiển TV Philips bằng điện thoại',
    intro='TV Philips dùng các hệ thống khác nhau tùy quốc gia và năm sản xuất: Roku TV ở Mỹ, Google TV hoặc Android TV ở nhiều nước, và Titan OS ở một số model châu Âu mới. Mando TV điều khiển các model dùng Roku TV, Google TV và Android TV qua Wi-Fi.',
    pasos=[
      'Kiểm tra màn hình chính. Roku TV hiện một lưới các ô. Google TV và Android TV hiện các hàng đề xuất của Google. Titan OS có màn hình chính riêng.',
      'Kết nối điện thoại và TV với cùng một mạng Wi-Fi.',
      'Mở Mando TV và chạm vào TV Philips của bạn trong danh sách.',
      'Roku TV không hỏi gì cả. Google TV và Android TV hiện mã 6 ký tự: hãy nhập vào ứng dụng một lần.',
      'Dùng phím mũi tên, OK, Quay lại, Home, âm lượng và bàn phím.',
    ],
    extra=[
      ('Philips dùng Roku TV', 'Hoạt động như mọi TV Roku. Để bật TV từ điện thoại, hãy bật "Fast TV start" trong Settings > System > Power. Xem thêm trên trang [Ứng dụng điều khiển Roku](@roku).'),
      ('Philips dùng Google TV hoặc Android TV', 'Gồm nhiều model Ambilight. Chúng ghép nối bằng mã trên màn hình. Để bật TV từ điện thoại, hãy tìm trong cài đặt mạng hoặc nguồn điện mục Wake on LAN hoặc "Wake on network". Một số model không có tùy chọn này. Xem thêm trên trang [Ứng dụng điều khiển Android TV](@android).'),
      ('TV Philips đời cũ không dùng Android', 'Các TV Philips từ 2011 đến 2015 không dùng Android được Mando TV hỗ trợ trong bản beta. Tính năng này còn mới và không cần mã ghép nối.'),
      ('Philips dùng Titan OS', 'Titan OS là một hệ thống khác mà Mando TV hiện chưa điều khiển được, và chúng tôi muốn nói rõ điều đó. Các model Philips mới không dùng Android cũng chưa được hỗ trợ.'),
      ('Miễn phí và Pro', 'Bạn tải và dùng điều khiển miễn phí, không quảng cáo và không đăng ký. Mando TV Pro là gói mua một lần tùy chọn cho các tính năng bổ sung.'),
    ],
    marca=None,
    faq=[
      ('Mando TV có dùng được với TV Philips không?', 'Có với các TV Philips dùng Roku TV, Google TV hoặc Android TV, và trong bản beta với các TV Philips từ 2011 đến 2015 không dùng Android. Các model dùng Titan OS chưa được hỗ trợ.'),
      ('Mando TV có điều khiển Ambilight không?', 'Mando TV là một chiếc điều khiển: ứng dụng gửi các phím, nên bạn dùng mũi tên và OK để vào cài đặt Ambilight. Không có điều khiển Ambilight riêng.'),
      ('Tôi có cần tài khoản Philips hay Google không?', 'Không. Mando TV kết nối qua Wi-Fi trong nhà bạn và không cần tài khoản.'),
    ]),
]
OTRAS_GUIAS += [
  ('no-sub', 'Ứng dụng điều khiển TV không đăng ký và không quảng cáo'),
  ('roku-app-alt', 'Lựa chọn thay thế ứng dụng Roku: một ứng dụng cho mọi TV'),
  ('lg-thinq', 'Lựa chọn thay thế ứng dụng LG ThinQ cho TV LG của bạn'),
  ('smartthings', 'Lựa chọn thay thế SmartThings cho TV Samsung'),
  ('googletv-alt', 'Lựa chọn thay thế điều khiển Google TV trên điện thoại'),
  ('windows', 'Ứng dụng điều khiển TV cho máy tính Windows'),
  ('iphone', 'Ứng dụng điều khiển TV cho iPhone: một ứng dụng cho mọi TV'),
  ('firetv', 'Điều khiển Fire TV cho điện thoại hoặc máy tính của bạn'),
  ('firetv-lost', 'Mất điều khiển Fire TV: cách dùng điện thoại thay thế'),
  ('turn-on', 'Cách bật TV khi không có điều khiển'),
  ('sony', 'Cách điều khiển TV Sony bằng điện thoại'),
  ('tcl', 'Cách điều khiển TV TCL bằng điện thoại'),
  ('hisense', 'Ứng dụng điều khiển Hisense: cái gì chạy được và cái gì không'),
  ('philips', 'Điều khiển TV Philips bằng điện thoại'),
]
# <<< guías traídas del inglés
