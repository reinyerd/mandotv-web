# Textos en chino tradicional (Taiwán, también se lee en Hong Kong) de mandotv.app. Los usa generar_idiomas.py. Escritos para las búsquedas de Taiwán.
# Las claves de las páginas (lg, lost-tv, ...) y sus rutas están en idiomas_sitio.py.
# Los nombres de menús de cada marca (LG, Samsung, Roku, Android TV, iPhone) son los mismos que usa la app en chino tradicional
# (lib/l10n/app_zh_Hant.arb del proyecto de la app).

UI = dict(
  locale='zh_TW',
  aria_home='Mando TV，首頁', aria_main='主選單', nav_que='功能', nav_ayuda='說明', nav_contacto='聯絡我們',
  asunto='%E4%BD%A0%E5%A5%BD%20Mando%20TV', inicio='首頁', privacidad='隱私權政策', aria_pie='頁尾', aria_ruta='導覽路徑',
  aria_marcas='品牌與教學', hecho='智利製造',
  aviso='Mando TV 是獨立的 App，與文中提到的電視品牌、Google、Amazon、Apple 或 Roku 皆無關聯，也未獲其背書。商標歸各自擁有者所有，僅用於說明相容性。Android TV 與 Google TV 是 Google LLC 的商標。Apple TV 是 Apple Inc. 的商標。',
  bajar='免費下載', descarga='下載自', anticipada='搶先體驗於',
  apple_aria='在 App Store 免費下載 Mando TV', ms_aria='在 Microsoft Store 免費下載 Mando TV',
  gp_aria='在 Google Play 搶先體驗 Mando TV（Android）', aria_desc='下載 Mando TV',
  b_como_btn='連線方式', b_tiendas_label='可在以下商店取得',
  b_nota='支援 iPhone、iPad、Mac、Android 與 Windows。免費下載，沒有廣告。Pro 為一次買斷，不需訂閱。',
  b_compat='支援的電視', b_otras='其他品牌', b_otras_p='Mando TV 用同一個 App 就能控制以下所有品牌：',
  g_guias='教學', g_ver='查看步驟', g_pasos='步驟說明', g_hazlo='用 Mando TV 這樣做',
  g_tiendas='Mando TV 是萬用電視遙控器。免費下載，沒有廣告，也不需要帳號。Pro 為選購的一次買斷方案，不需訂閱。支援 iPhone、iPad、Windows 與 Android：',
  g_nota='Android：Google Play 免費搶先體驗。<a href="{enlace}">兩個步驟就能加入</a>，幫助我們順利上架。',
  g_mas_pagina='更多詳細資訊請見 {enlace} 頁面。', g_mas_marca='依品牌查看更多資訊：',
  g_faq='常見問題', g_mas='更多教學', g_todas='所有教學', g_ayuda='說明與支援',
  g_idiomas='本教學的其他語言版本',
)

# Pie de página y listas de marcas/guías: (clave, texto)
PIE = [
  ('samsung', 'Samsung 電視遙控器'),
  ('lg', 'LG 電視遙控器'),
  ('roku', 'Roku 遙控器'),
  ('android', 'Android TV 遙控器'),
  ('guias', '所有教學'),
  ('lost-tv', '遙控器不見了'),
  ('lost-lg', 'LG 遙控器不見了'),
  ('lg-on', '用手機開啟 LG 電視'),
  ('hdmi', '沒有遙控器切換 HDMI 輸入'),
  ('androidtv', '沒有遙控器的 Android TV'),
  ('console', '沒有遙控器開電視並切換遊戲機 HDMI'),
  ('samsung-lost', '沒有遙控器的 Samsung 電視'),
  ('roku-lost', 'Roku 遙控器不見了'),
  ('roku-403', 'Roku App 無法使用'),
  ('androidtv-code', 'Android TV 配對碼'),
  ('not-found', '手機找不到電視'),
  ('wifi', '用 Wi-Fi 把手機當遙控器'),
  ('pc', '用電腦控制電視'),
]
NOMBRE_OTRA = {'lg': 'LG 電視遙控器 App', 'samsung': 'Samsung 電視遙控器 App', 'roku': 'Roku 遙控器 App',
               'android': 'Android TV 與 Google TV 遙控器 App'}
PAGINA_MARCA = {'lg': 'LG 電視遙控器 App', 'samsung': 'Samsung 電視遙控器 App', 'roku': 'Roku 遙控器 App',
                'android': 'Android TV 遙控器 App'}

OTRAS_GUIAS = [
  ('lg-on', '用手機開啟 LG 電視'),
  ('lost-tv', '遙控器不見了，你可以這樣做'),
  ('lost-lg', 'LG 遙控器不見了：用手機取代遙控器'),
  ('hdmi', '沒有遙控器也能切換電視的 HDMI 輸入'),
  ('androidtv', '沒有遙控器的 Android TV：用手機控制'),
  ('console', '沒有遙控器也能開電視並切換到遊戲機的 HDMI'),
  ('samsung-lost', '沒有原廠遙控器的 Samsung 電視：用手機控制'),
  ('roku-lost', 'Roku 遙控器不見了：用手機控制'),
  ('roku-403', 'Roku App 無法使用：排除 403 錯誤'),
  ('androidtv-code', 'Android TV 要求配對碼：該怎麼做'),
  ('not-found', '手機找不到電視：請檢查這幾點'),
  ('wifi', '用 Wi-Fi 把手機當電視遙控器'),
  ('pc', '用 Windows 電腦控制電視'),
]

INDICE = dict(
  titulo='教學：用手機控制電視 | Mando TV',
  desc='步驟教學：用手機或電腦當遙控器、開啟電視、切換 HDMI，並解決 Samsung、LG、Roku 的常見問題。',
  h1='教學：把手機當電視遙控器',
  intro='簡單幾個步驟，就能用 Mando TV 連接 Samsung、LG、Roku 或 Android TV 電視的遙控功能、開啟電視並排除問題。',
  h2_guias='所有教學', h2_marcas='依品牌選擇遙控器 App',
)

MARCAS = [
  dict(clave='lg', color='#e0457b', corto='LG',
    titulo='LG 電視遙控器 App，手機免費使用 | Mando TV',
    desc='用手機或電腦當 LG webOS 電視遙控器，透過 Wi-Fi 連線。按鍵、鍵盤、App、輸入來源與開機免費，游標功能為 Pro。',
    h1='LG 電視遙控器 App，手機就能用',
    intro='Mando TV 是 LG 電視的遙控器 App：透過家中的 Wi-Fi，讓你的手機或電腦變成 webOS LG 智慧電視的遙控器。遙控器弄丟了、電池沒電了，或是想更快輸入文字時，都很好用。',
    compat='採用 webOS 的 LG 智慧電視（2014 年起的大多數 LG 智慧電視機型）。支援 LED、NanoCell、QNED 與 OLED 電視。2011 至 2014 年、webOS 之前使用 NetCast 的舊款 LG 智慧電視，現已在測試版支援：以電視畫面顯示的 6 位數金鑰配對。',
    h2=dict(funciones='用手機控制 LG 電視，你可以做到', como='如何把 LG 電視連上 Mando TV',
            encender='用手機開啟 LG 電視', preguntas='LG 常見問題', guias='LG 教學'),
    funciones=[
      ('完整按鍵', '方向鍵、確定、返回、首頁、音量、頻道、靜音與播放控制。'),
      ('像 Magic Remote 的游標（Pro）', '用手指在螢幕上移動箭頭，就像使用 LG Magic Remote 一樣。'),
      ('鍵盤', '用手機鍵盤在 YouTube、Netflix 或電視瀏覽器裡輸入文字。'),
      ('App 與輸入來源', '開啟你的 App，並切換到 HDMI、直播電視、AirPlay 或螢幕分享。'),
      ('音訊輸出（Pro）', '在電視喇叭與 Soundbar 之間切換。'),
      ('開啟電視', '電視關機時，Mando TV 會透過網路開啟電視並自動連線。'),
    ],
    pasos=[
      '把手機與電視連上同一個 Wi-Fi。',
      '開啟 Mando TV：你的 LG 電視會自動出現在清單中，點選它即可。',
      '電視畫面會跳出詢問授權的提示，請用你平常的遙控器確認（只需要第一次）。',
    ],
    encender='在 LG 電視上開啟設定，找到「以行動裝置開啟電視」（依機型位於「一般」或「連線」之下），並啟用「透過 Wi-Fi 開啟」。如果有「快速啟動+」，也請一併啟用。之後，當你在 Mando TV 點選已關機的電視時，App 會詢問是否要開啟，並自動連線。',
    faq=[
      ('使用 Mando TV 需要 Magic Remote 嗎？', '只有第一次需要，用來確認電視畫面上的授權提示。之後只要用手機就行了。'),
      ('Mando TV 能取代 LG ThinQ App 嗎？', '就控制電視而言可以：不需要 LG 帳號，也不必註冊電視。Mando TV 直接透過你的 Wi-Fi 連線。'),
      ('我可以用手機開啟 LG 電視嗎？', '可以，只要你在電視上啟用「以行動裝置開啟電視」，並且曾在電視開機時連線過一次。'),
      ('支援 webOS 之前的舊款 LG 電視嗎？', '測試版支援，適用於 2011 至 2014 年的 LG NetCast 智慧電視，以電視畫面顯示的 6 位數金鑰配對。此功能是新推出的，可能還有不完善的地方。'),
    ],
    guias=[('lg-on', '如何用手機開啟 LG 電視'),
           ('lost-lg', 'LG 遙控器不見了：用手機取代遙控器'),
           ('hdmi', '沒有遙控器也能切換電視的 HDMI 輸入'),
           ('guias', '所有用手機控制電視的教學')]),
  dict(clave='samsung', color='#3d7bff', corto='Samsung',
    titulo='Samsung 電視遙控器 App，手機免費使用 | Mando TV',
    desc='用手機或電腦當 Samsung Tizen 電視遙控器，透過 Wi-Fi 連線。按鍵、鍵盤、App 與開機免費，觸控板為 Pro。沒有廣告。',
    h1='Samsung 電視遙控器 App，手機就能用',
    intro='Mando TV 是 Samsung 電視的遙控器 App：透過家中的 Wi-Fi，讓你的手機或電腦變成 Samsung 智慧電視的遙控器。不需要 Samsung 帳號，也不必註冊電視。',
    compat='採用 Tizen、2016 年及之後的 Samsung 智慧電視（Crystal UHD、QLED、Neo QLED、The Frame 與 OLED 等系列）。',
    h2=dict(funciones='用手機控制 Samsung 電視，你可以做到', como='如何把 Samsung 電視連上 Mando TV',
            encender='用手機開啟 Samsung 電視', preguntas='Samsung 常見問題', guias='Samsung 教學'),
    funciones=[
      ('完整按鍵', '方向鍵、確定、返回、首頁、音量、頻道、靜音與訊號源。'),
      ('觸控板（Pro）', '用手指滑動操作選單，不必再找方向鍵。'),
      ('鍵盤', '用手機鍵盤輸入搜尋內容與密碼。'),
      ('App', '輕點一下就開啟 Netflix、YouTube、Prime Video 與其他 App。'),
      ('開啟電視', '電視關機時，Mando TV 會透過網路開啟電視並自動連線。'),
      ('不需帳號', '連線直接透過你的 Wi-Fi，不必繞道網際網路。'),
    ],
    pasos=[
      '把手機與電視連上同一個 Wi-Fi。',
      '開啟 Mando TV：你的 Samsung 電視會自動出現在清單中，點選它即可。',
      '電視會詢問是否允許連線，請用遙控器選擇「允許」（只需要第一次）。',
    ],
    encender='在 Samsung 電視上，前往「設定 > 一般 > 網路 > 專家設定」，啟用「以行動裝置開機」。之後，當你在 Mando TV 點選已關機的電視時，App 會詢問是否要開啟，並自動連線。',
    faq=[
      ('我不小心拒絕了授權，該怎麼辦？', '在電視上前往「設定 > 一般 > 外接裝置管理員 > 裝置連線管理員」，把 Mando TV 改為允許。'),
      ('Mando TV 能取代 SmartThings 嗎？', '就控制電視而言可以，而且不需要 Samsung 帳號。Mando TV 直接透過你的 Wi-Fi 連線。'),
      ('支援較舊的 Samsung 電視嗎？', '支援採用 Tizen、2016 年及之後的 Samsung 電視。更早的機型使用另一種系統，我們目前還不支援。'),
    ],
    guias=[('samsung-lost', '沒有原廠遙控器的 Samsung 電視：用手機控制'),
           ('hdmi', '沒有遙控器也能切換電視的 HDMI 輸入'),
           ('guias', '所有用手機控制電視的教學')]),
  dict(clave='roku', color='#a77bff', corto='Roku',
    titulo='Roku 遙控器 App，手機免費使用 | Mando TV',
    desc='用手機或電腦當 Roku 電視與 Roku 播放器的遙控器，透過 Wi-Fi 連線。按鍵、鍵盤、頻道、輸入來源與開機免費。',
    h1='Roku 遙控器 App，手機就能用',
    intro='Mando TV 是 Roku 的遙控器 App：透過家中的 Wi-Fi，讓你的手機或電腦變成 Roku 的遙控器。支援 Roku 電視，也支援接在 HDMI 孔的 Roku 播放器。',
    compat='Roku 電視（TCL、Hisense、Philips、Sharp、JVC 等品牌）與 Roku 播放器（Express、Streaming Stick、Ultra）。',
    h2=dict(funciones='用手機控制 Roku，你可以做到', como='如何把 Roku 連上 Mando TV',
            encender='用手機開啟 Roku', preguntas='Roku 常見問題', guias='Roku 教學'),
    funciones=[
      ('完整按鍵', '方向鍵、確定、返回、首頁、音量、靜音、重播與播放控制。'),
      ('鍵盤', '用手機鍵盤在 Roku 頻道裡輸入搜尋內容。'),
      ('頻道', '輕點一下就開啟 Netflix、YouTube 與其他 Roku 頻道。'),
      ('輸入來源', '使用 Roku 電視時，可在 App 裡切換到 HDMI、天線或 AV。'),
      ('開啟電視', '支援快速啟動的 Roku 電視，Mando TV 可以從手機開啟。'),
      ('免配對', 'Roku 不會要求輸入代碼：在清單中點選它就連上了。'),
      ('讓遙控器發出聲音', '如果你的 Roku 遙控器有喇叭，例如 Roku Voice Remote Pro，Mando TV 可以讓它發出聲音，方便你找到。免費，且 Roku 必須開機。'),
    ],
    pasos=[
      '把手機與 Roku 連上同一個 Wi-Fi。',
      '開啟 Mando TV：你的 Roku 會自動出現在清單中，點選它即可。',
      '如果連不上，請在 Roku 上前往「設定 > 系統 > 進階系統設定 > 行動 App 控制」，並把網路存取設為「預設」或「已啟用」。',
    ],
    encender='使用 Roku 電視時，請前往「設定 > 系統 > 電源」，啟用「電視快速啟動」。接在其他電視上的 Roku 播放器無法用這個方式開機。之後，當你在 Mando TV 點選已關機的電視時，App 會詢問是否要開啟，並自動連線。',
    faq=[
      ('支援 Roku Express 或 Streaming Stick 嗎？', '支援。所有 Roku 播放器與 Roku 電視的控制方式都一樣。'),
      ('Mando TV 找不到我的 Roku，該怎麼辦？', '請確認兩者在同一個 Wi-Fi，並檢查 Roku 上的「行動 App 控制」沒有被關閉。你也可以用 IP 位址手動新增。'),
      ('需要 Roku 帳號嗎？', '不需要。Mando TV 直接透過你的 Wi-Fi 連線。'),
    ],
    guias=[('roku-403', 'Roku App 無法使用（403 錯誤）'),
           ('roku-lost', 'Roku 遙控器不見了：用手機控制'),
           ('guias', '所有用手機控制電視的教學')]),
  dict(clave='android', color='#2fbf8f', corto='Android TV 與 Google TV',
    titulo='Android TV 遙控器 App，手機免費使用 | Mando TV',
    desc='用手機或電腦當 Android TV 遙控器（Sony、TCL、小米），透過 Wi-Fi 連線。按鍵、鍵盤、App 與開機免費，觸控板為 Pro。',
    h1='Android TV 遙控器 App，手機就能用',
    intro='Mando TV 是 Android TV 的遙控器 App：透過家中的 Wi-Fi，讓你的手機或電腦變成 Android TV 或 Google TV 電視的遙控器。也能在 iPhone 與 Windows 上使用。',
    compat='搭載 Google TV 或 Android TV 的電視，包括 Sony、Philips、TCL、Hisense、Sharp、小米、Toshiba、Panasonic、Haier、Skyworth、JVC、Thomson、Motorola、OnePlus、iFFALCON、Kogan、Vu 等品牌，以及 Chromecast with Google TV、Google TV Streamer、onn. 與 Nvidia Shield。這些品牌中有些也販售採用其他系統的機型：如果你的電視顯示 Google TV 主畫面，或有 Google Play 商店，Mando TV 就能控制它。',
    h2=dict(funciones='用手機控制 Android TV，你可以做到', como='如何把 Android TV 連上 Mando TV',
            encender='用手機開啟 Android TV', preguntas='Android TV 常見問題', guias='Android TV 教學'),
    funciones=[
      ('完整按鍵', '方向鍵、確定、返回、首頁、音量、靜音與播放控制。'),
      ('觸控板（Pro）', '用手指滑動，快速瀏覽 Google TV 的選單。'),
      ('鍵盤', '用手機鍵盤輸入搜尋內容與密碼。'),
      ('App', '輕點一下就開啟 YouTube、Netflix、Disney+ 與其他 App。'),
      ('開啟電視', '支援透過網路開機的機型，Mando TV 會開啟電視並自動連線。'),
      ('iPhone、Android 與電腦', '在任何手機與電腦上用起來都一樣。'),
    ],
    pasos=[
      '把手機與電視連上同一個 Wi-Fi。',
      '開啟 Mando TV：你的 Android TV 會自動出現在清單中，點選它即可。',
      '電視會顯示 6 個字元的代碼，請在 Mando TV 中輸入（只需要第一次）。',
    ],
    encender='這取決於製造商。請在網路或電源設定中尋找「Wake on LAN」、「透過網路開機」或「網路待機」。有些機型沒有這個選項。之後，當你在 Mando TV 點選已關機的電視時，App 會詢問是否要開啟，並自動連線。',
    faq=[
      ('支援 Chromecast with Google TV 嗎？', '支援，配對方式是輸入畫面上顯示的 6 個字元代碼。'),
      ('和 Google TV App 有什麼不同？', 'Mando TV 不需要 Google 帳號，也能在 Windows 上使用，而且同一個 App 還能控制 LG、Samsung 與 Roku 電視。'),
      ('畫面上沒有出現代碼，該怎麼辦？', '請關閉 Mando TV，重新開啟 App 後，再點選一次電視。同時確認電視沒有處於深度省電模式。'),
    ],
    guias=[('androidtv-code', 'Android TV 要求配對碼：該怎麼做'),
           ('androidtv', '沒有遙控器的 Android TV：用手機控制'),
           ('guias', '所有用手機控制電視的教學')]),
]

GUIAS = [
  dict(clave='lost-tv', corto='遙控器不見了',
    titulo='遙控器不見了？用手機控制電視',
    desc='遙控器不見了？先用電視上的按鍵開機，再把手機當遙控器。附 LG、Samsung、Roku、Android TV 的步驟，免費。',
    h1='遙控器不見了？你現在可以這樣做',
    intro='每個家庭都會遇到遙控器不見的時候：偏偏就在你想看電視的時候找不到。好消息是，你的手機可以透過家中的 Wi-Fi 取代遙控器。以下是依序該做的步驟。',
    pasos=[
      '用電視機身上的按鍵開機。它幾乎都在正下方中間，或是背面靠近角落的位置。有時是單一按鍵，有時是一個小搖桿。',
      '把手機連上與電視相同的 Wi-Fi。',
      '下載免費且不需要帳號的 Mando TV，然後開啟 App。你的電視會自動出現在清單中，點選它即可。',
      '依你的品牌確認連線。LG 與 Samsung 的電視會跳出提示：請用電視機身上的按鍵或搖桿確認。Android TV 與 Google TV 則要輸入畫面上顯示的 6 個字元代碼。Roku 什麼都不會問。',
      '完成。方向鍵、確定、返回、首頁、音量、頻道與鍵盤都是免費的。',
      '為了下次方便：請在電視設定中啟用透過網路開機（下方有各品牌的教學）。這樣你就能直接用手機開電視，連碰都不用碰。',
    ],
    extra=[
      ('選擇你的品牌教學', 'LG：[LG 遙控器不見了](@lost-lg)。Android TV 與 Google TV：[沒有遙控器的 Android TV](@androidtv)。Samsung：[沒有遙控器的 Samsung 電視](@samsung-lost)。Roku：[Roku 遙控器不見了](@roku-lost)。'),
      ('如果用按鍵也開不了電視', '在找別的遙控器之前，先檢查電源線是否插緊、插座有沒有電。如果電視上的按鍵也沒反應，問題出在電視，而不是遙控器。'),
      ('如果遙控器就是沒反應了', '先換新電池。想確認它還有沒有發出訊號，可以把遙控器對準手機相機並按下按鍵：許多手機的螢幕上會看到紫色亮光。如果看得到亮光但電視沒反應，可能是電視的感應器被擋住了。'),
      ('如果你換了路由器，電視連不上 Wi-Fi', '沒有遙控器時，要讓電視連上新網路比較麻煩。最簡單的做法是用網路線把電視接到路由器。你也可以建立一個名稱與密碼和之前相同的 Wi-Fi：電視通常會自動連上。'),
      ('免費與 Pro 的差別', '開關電視、方向鍵、確定、音量、頻道、數字鍵、鍵盤、開啟 App 與切換輸入來源都是免費的。觸控板、語音與例程屬於 Mando TV Pro，這是一次買斷的方案，不需訂閱。'),
    ],
    marca=None,
    faq=[
      ('我從來沒連過電視，可以用手機開電視嗎？', '第一次請用電視機身上的按鍵開機。等你把手機連上，並在電視設定中啟用透過網路開機後，就能用 App 開啟電視。'),
      ('我一定要買新的遙控器嗎？', '不一定。Mando TV 的按鍵、音量、鍵盤與開機都是免費的。如果你還是想要實體遙控器，請依電視的確切型號搜尋。'),
      ('電視沒有連上 Wi-Fi 也能用嗎？', '不行。手機與電視必須在同一個 Wi-Fi。不是智慧電視的電視，無法用 Mando TV 控制。'),
    ]),
  dict(clave='lost-lg', corto='LG 遙控器不見了',
    titulo='LG 遙控器不見了？用手機取代',
    desc='沒有 LG 遙控器？先用電視機身按鍵開機、確認提示，再用手機透過 Wi-Fi 控制。不需要 LG 帳號，沒有廣告。',
    h1='LG 遙控器不見了？用手機取代遙控器',
    intro='如果你的 LG 遙控器不見了，或 Magic Remote 壞了，手機可以透過 Wi-Fi 取代它。這適用於採用 webOS 的 LG 電視，也就是 2014 年以後的幾乎所有 LG 智慧電視。不需要 LG 帳號，也不用 ThinQ App。',
    pasos=[
      '用 LG 標誌下方的按鍵，或背面的按鍵開機。許多機型的按鍵是一個搖桿：按下去開啟選單，撥動來選擇項目。',
      '把手機連上與電視相同的 Wi-Fi。',
      '開啟 Mando TV，在清單中點選你的 LG 電視。',
      '電視會跳出詢問授權的提示。請用電視上的搖桿或按鍵確認。如果這支手機之前連過，就不會再問一次。',
      '完成。方向鍵、確定、返回、首頁、音量、頻道與鍵盤都是免費的。游標屬於 Pro 功能。',
      '連線後，用方向鍵與確定開啟設定，並啟用「以行動裝置開啟電視」。[用手機開啟 LG 電視](@lg-on)這篇教學會告訴你選項在哪裡。',
    ],
    extra=[
      ('如果電視沒有出現提示', '可能是授權已經儲存，或是手機在另一個網路。請確認兩者在同一個 Wi-Fi，並關閉 VPN。如果電視沒有出現在清單中，請參考[手機找不到電視](@not-found)。'),
      ('如果電視失去了 Wi-Fi 連線', '用網路線把電視接到路由器，它就會自動使用。或者建立一個名稱與密碼和之前相同的 Wi-Fi，電視通常會自動連上。'),
      ('如果電視停在其他輸入來源', '在手機上點選輸入來源，然後選擇 HDMI 孔。詳情請見[沒有遙控器也能切換電視的 HDMI 輸入](@hdmi)。'),
    ],
    marca='lg',
    faq=[
      ('使用 Mando TV 需要 Magic Remote 嗎？', '只有第一次需要確認提示，而這用電視機身上的按鍵或搖桿就夠了。之後只要用手機。'),
      ('需要 LG ThinQ App 嗎？', '不需要。Mando TV 直接透過你的 Wi-Fi 連線，也不需要 LG 帳號。'),
      ('我可以用手機開關 LG 電視嗎？', '關機可以。要開機的話，你必須在電視上啟用「以行動裝置開啟電視」，並且曾在電視開機時連線過一次。'),
    ]),
  dict(clave='hdmi', corto='沒有遙控器切換 HDMI',
    titulo='沒有遙控器切換 HDMI 輸入（Samsung、LG、Roku）',
    desc='沒有遙控器也能切換 Samsung、LG 或 Roku 的 HDMI 輸入：用電視上的按鍵或用手機。免費開始，沒有廣告。',
    h1='沒有遙控器，如何切換電視的 HDMI 輸入',
    intro='遊戲機或串流播放器已經準備好了，電視卻停在別的輸入來源，遙控器又找不到。沒有遙控器要切換 HDMI 輸入，有兩種方法：用電視本身的按鍵，或用手機。以下是 Samsung、LG 與 Roku 的步驟。',
    pasos=[
      '先試最簡單的方法：開啟遊戲機或播放器。如果電視啟用了 HDMI-CEC（Samsung 稱為 Anynet+，LG 稱為 SIMPLINK），它會自動切換到該輸入。',
      '如果沒有自動切換，就使用電視本身的按鍵，通常在正下方中間或背面。許多 Samsung 與 LG 電視的按鍵是一個搖桿，會開啟含有「訊號源」或「輸入來源」的選單。',
      '在該選單中選擇輸入來源：HDMI 1、HDMI 2，依此類推。數字就是你插線的那個孔。',
      '如果你想用手機，請連上相同的 Wi-Fi，開啟 Mando TV，並點選你的電視。',
      'LG 與 Roku 請點選輸入來源，然後選擇 HDMI 孔。Samsung 的輸入來源會把「訊號源」按鍵傳送到電視，再用方向鍵與確定選擇。',
      '你也可以在電視主畫面用方向鍵與確定進入輸入來源。依品牌與年份，它可能叫「訊號源」、「已連接的裝置」或「輸入來源」。Roku 電視則是主畫面上的 HDMI 圖塊。',
    ],
    extra=[
      ('Samsung', '如果電視按鍵的選單裡沒有「訊號源」，請用手機開啟主畫面選單，並在左側找「訊號源」或「已連接的裝置」。你可以用 Mando TV 裡免費的方向鍵與確定來操作。'),
      ('LG', '按下電視上的搖桿並找到輸入來源。用手機的話，也可以在 Mando TV 開啟輸入來源清單，並點選你要的輸入。'),
      ('Roku 電視', '主畫面上每個輸入來源都有一個圖塊，例如 HDMI 1 或 HDMI 2。用方向鍵移動，按確定開啟，免費。'),
      ('如果是 Android TV 或 Google TV 電視', 'Mando TV 目前還沒有 Android TV 的輸入來源清單。請使用電視本身的輸入按鍵，或從主畫面用方向鍵與確定進入輸入來源。如果你沒有遙控器又想連線，請閱讀[沒有遙控器的 Android TV](@androidtv)。'),
      ('更多協助', '如果電視完全無法開機，或你不知道從哪裡開始，請閱讀[遙控器不見了](@lost-tv)。如果是要玩遊戲機，[沒有遙控器也能開電視並切換到遊戲機的 HDMI](@console)這篇教學提供了 HDMI-CEC 的小技巧。'),
    ],
    marca=None,
    faq=[
      ('切換 HDMI 輸入是免費的嗎？', '是的。Mando TV 的輸入來源清單是免費的，開啟電視與方向鍵、確定、音量也一樣。你也可以從電視的選單進入輸入來源。'),
      ('我怎麼知道該用哪個 HDMI 輸入？', '看一下電視上的 HDMI 孔：每個都有編號。選你插遊戲機或播放器線材的那一個。'),
      ('如果電視打不開怎麼辦？', '用電視機身上的按鍵開機。如果你之前連線過，並且啟用了透過網路開機，也可以用手機開啟。'),
    ]),
  dict(clave='androidtv', corto='沒有遙控器的 Android TV',
    titulo='沒有遙控器的 Android TV：用手機控制',
    desc='沒有 Android TV 或 Google TV 遙控器？用畫面上的 6 位代碼連接手機。免費，不需要帳號，沒有廣告。',
    h1='沒有遙控器的 Android TV：用手機控制',
    intro='如果你的 Android TV 或 Google TV 遙控器不見了，或電池沒電了，手機可以取代它。最棒的是：連線時不需要遙控器，因為電視會在畫面上顯示代碼，你只要在手機上輸入即可。適用於 Sony、Philips、TCL、Hisense、Sharp 與小米的 Android TV 電視、Chromecast with Google TV 與 Nvidia Shield。',
    pasos=[
      '用電視機身上的按鍵開機。它幾乎都在正下方中間，或是背面靠近角落的位置。',
      '把手機連上與電視相同的 Wi-Fi。',
      '下載免費且不需要 Google 帳號的 Mando TV，然後開啟 App。在清單中點選你的電視。',
      '電視會顯示由 6 個字母與數字組成的代碼。在手機上輸入，然後點選「配對」。這個步驟不需要遙控器。',
      '現在你可以使用方向鍵、確定、返回、首頁、音量、靜音與鍵盤。它們都是免費的，App 清單也是。觸控板為 Pro。',
      '想要下次也能用手機開電視，請在網路或電源設定中尋找「Wake on LAN」、「透過網路開機」或「網路待機」。',
    ],
    extra=[
      ('如果你的電視無法用手機開機', '並非所有 Android TV 都能透過網路開機，這取決於製造商與機型。如果你的電視沒有這個功能，請用電視上的按鍵開機，再繼續用手機操作。關機則可以用 App 完成。'),
      ('Chromecast with Google TV、Google TV Streamer 與 Shield', '配對方式相同：連上同一個 Wi-Fi，在清單中點選裝置並輸入代碼。如果電視顯示其他輸入來源，請依[沒有遙控器也能切換電視的 HDMI 輸入](@hdmi)的說明，切換到接這個裝置的 HDMI 孔。'),
      ('如果代碼沒有出現，或顯示錯誤', '請確認電視確實已開機，而不是待機。每次要求都會產生新的代碼：只有最後一個有效。更多細節請見[Android TV 要求配對碼](@androidtv-code)。'),
      ('Google 的 App 或 Mando TV', 'Google 有自己的 App，需要 Google 帳號。Mando TV 不需要帳號，也能在 Windows 上使用，而且同一個 App 還能控制 LG、Samsung 與 Roku 電視。'),
    ],
    marca='android',
    faq=[
      ('配對手機需要遙控器嗎？', '不需要。代碼會顯示在電視畫面上，你再用手機輸入。你只需要開啟電視，必要時用機身上的按鍵即可。'),
      ('支援 Hisense 嗎？', '搭載 Android TV 或 Google TV 的 Hisense 電視可以。採用其他系統的 Hisense 電視則不相容。'),
      ('我可以用手機鍵盤輸入文字嗎？', '可以。鍵盤是免費的，可用於 YouTube、Netflix 與其他 App 的搜尋。'),
    ]),
  dict(clave='lg-on', corto='用手機開啟 LG 電視',
    titulo='用手機開啟 LG 電視（教學）',
    desc='用手機透過 Wi-Fi 開啟 LG 電視：啟用「以行動裝置開啟電視」，再用 Mando TV。步驟清楚，免費。',
    h1='如何用手機開啟 LG 電視',
    intro='你可以用手機開啟 LG 電視，但必須先在電視上啟用一項設定。之後，手機就能透過你的 Wi-Fi 開啟 LG 電視，完全不需要遙控器。只要五分鐘，而且只需要設定一次。',
    pasos=[
      '把手機與 LG 電視連上同一個 Wi-Fi。',
      '在電視上開啟設定，找到「以行動裝置開啟電視」。依機型，它位於「一般」或「連線」之下。',
      '啟用「透過 Wi-Fi 開啟」。如果你的電視是用網路線連接，請改為啟用網路線的選項。',
      '如果電視有「快速啟動+」，也請一併啟用。',
      '在電視開機的狀態下，用手機開啟 Mando TV，並在清單中點選你的 LG 電視。確認畫面上出現的提示。App 就是這樣學會如何喚醒它。',
      '把電視關機並試試看：在 Mando TV 點選電視，App 會詢問是否要開啟它。',
    ],
    extra=[
      ('如果無法開機', '電視在關機之前必須連在同一個 Wi-Fi。請確認設定仍然啟用，且手機在同一個網路。如果你換了路由器，請在電視開機時重新連線一次。'),
    ],
    marca='lg',
    faq=[
      ('我從沒連過 LG 電視，也能用手機開機嗎？', '不行。你必須先在電視上啟用「以行動裝置開啟電視」，並在電視開機時用 Mando TV 連線一次。'),
      ('需要 LG ThinQ App 嗎？', '不需要。Mando TV 直接透過你的 Wi-Fi 連線，也不需要 LG 帳號。'),
      ('可以用行動數據嗎？', '不行。手機與電視必須在同一個 Wi-Fi。'),
    ]),
  dict(clave='console', corto='沒有遙控器開電視與遊戲機',
    titulo='沒有遙控器？開電視並切換 HDMI',
    desc='發售日當天找不到遙控器？用手機開電視，並切換到 PS5 或 Xbox 的 HDMI 輸入。免費，沒有廣告。',
    h1='沒有遙控器，如何開電視並切換到遊戲機的 HDMI 輸入',
    intro='GTA VI 發售日，遊戲機準備就緒，遙控器卻不知道掉進哪個沙發縫裡。這種事比你想的更常發生。用 Mando TV，手機就能透過家中的 Wi-Fi 開電視，並切換到你的 PlayStation 或 Xbox 輸入。',
    pasos=[
      '把手機連上與電視相同的 Wi-Fi。',
      '開啟 Mando TV，並在清單中點選你的電視（Samsung、LG、Roku 或 Android TV）。',
      '如果電視是關機的，請點選「開機」。只要電視已啟用透過網路開機就可以。如果你從沒啟用過，這一次請先用電視上的按鍵開機，再為下次啟用。',
      '開啟遊戲機。如果啟用了 HDMI-CEC（請看下方的免費小技巧），電視會自動切換到它的輸入。',
      '如果沒有自動切換，請在 Mando TV 點選輸入來源，並選擇接遊戲機的 HDMI 孔：HDMI 1、HDMI 2，依此類推。',
      '玩遊戲時要調音量，就用 App 裡的大按鍵。',
    ],
    extra=[
      ('免費小技巧：讓遊戲機自己切換電視', '透過 HDMI-CEC，PS5 與 Xbox 可以在啟動時開啟電視，並直接跳到它們的 HDMI 輸入。PS5 請到「設定 > 系統 > HDMI > 啟用 HDMI 裝置連動」。Xbox 請開啟「設定 > 一般 > 電視與顯示選項」，並找到裝置控制的選項。電視端的功能名稱依品牌而異：Samsung 是 Anynet+，LG 是 SIMPLINK，Sony 是 BRAVIA Sync，其他品牌則稱為 HDMI 控制。'),
      ('如果電視停在別的畫面', '如果遊戲機已開機，但電視仍顯示天線或某個 App，表示它沒有切換輸入。在手機上點選輸入來源，並選擇遊戲機的 HDMI 輸入。或者用方向鍵與確定進入電視的輸入來源，或使用電視本身的按鍵，再選擇 HDMI 孔。數字就是你插遊戲機線材的那個孔。'),
      ('如果是 Roku 電視', '電視上的按鍵（通常在正下方中間或背面）可以開機。接下來交給手機就行了。'),
    ],
    marca=None,
    faq=[
      ('Mando TV 和 GTA VI 有關嗎？', '沒有。Mando TV 與 Rockstar Games 或 Take-Two 沒有任何關聯。這個 App 只是讓你不會因為找不到遙控器而浪費遊戲時間。'),
      ('切換 HDMI 輸入是免費的嗎？', '是的。Mando TV 的輸入來源清單是免費的，開啟電視與方向鍵、確定、音量也一樣。你也可以透過 HDMI-CEC 讓遊戲機自己切換輸入。'),
      ('我的電視可以用嗎？', '在同一個 Wi-Fi 下，Samsung、LG、Roku 與 Android TV 電視都可以。如果你的電視是其他品牌，HDMI-CEC 小技巧仍然可能幫上忙。'),
      ('我可以用它在 PS5 或 Xbox 上玩 GTA VI（GTA 6）嗎？', 'Mando TV 不會干涉遊戲機或遊戲。它只是確保電視開著，並停在正確的 HDMI 輸入，讓你坐下來就能玩。'),
    ]),
  dict(clave='samsung-lost', corto='沒有遙控器的 Samsung 電視',
    titulo='Samsung 遙控器不見了？用手機取代',
    desc='Samsung 遙控器不見或壞了？用手機透過 Wi-Fi 當 Tizen 電視遙控器。Mando TV 簡單好用，免費，沒有廣告。',
    h1='沒有原廠遙控器的 Samsung 電視：用手機控制',
    intro='如果你的 Samsung 遙控器不見了，或不能用了，可以透過 Wi-Fi 把手機當遙控器。適用於採用 Tizen、2016 年及之後的 Samsung 電視。',
    pasos=[
      '用電視機身上的按鍵開機。大多數機型的按鍵在正下方或背面，有時是一個小搖桿。',
      '確認電視已連上你的 Wi-Fi，且手機在同一個網路。',
      '在手機上開啟 Mando TV。你的 Samsung 電視會自動出現在清單中，點選它即可。',
      '電視會要求你確認連線。大多數機型可以用電視上的按鍵，或背面的搖桿來確認。',
      '完成，現在你可以把手機當遙控器。按鍵、鍵盤與 App 都是免費的；觸控板是 Pro 功能。',
      '想要下次也能用手機開電視，請前往「設定 > 一般 > 網路 > 專家設定」，並啟用「以行動裝置開機」。',
    ],
    extra=[
      ('如果電視沒有詢問授權', '可能是授權已經儲存，或電視在另一個 Wi-Fi。請關閉 Mando TV，並在電視開機時重新開啟 App。如果你的電視早於 2016 年，它使用另一種尚未支援的系統。'),
      ('如果你不小心拒絕了授權', '在電視上前往「設定 > 一般 > 外接裝置管理員 > 裝置連線管理員」，把 Mando TV 改為允許。如果手機還是找不到電視，請閱讀[手機找不到電視](@not-found)。'),
    ],
    marca='samsung',
    faq=[
      ('沒有遙控器，我要怎麼確認連線？', '大多數機型可以用電視上的按鍵，或背面的搖桿來確認。如果你的機型沒有按鍵，請寫信到 hola@mandotv.app，我們會協助你。'),
      ('Mando TV 需要 Samsung 帳號嗎？', '不需要。連線直接透過你的 Wi-Fi，不需要 Samsung 帳號。'),
      ('支援我較舊的 Samsung 電視嗎？', '支援採用 Tizen、2016 年及之後的 Samsung 電視。'),
    ]),
  dict(clave='wifi', corto='用 Wi-Fi 把手機當遙控器',
    titulo='手機當遙控器：用 Wi-Fi 控制電視',
    desc='用 Wi-Fi 把手機連上電視，當 Samsung、LG、Roku 與 Google TV 的遙控器。附各品牌步驟，用 Mando TV 免費使用。',
    h1='如何用 Wi-Fi 把手機當電視遙控器',
    intro='你只需要手機、在同一個 Wi-Fi 的電視，以及一個遙控器 App。Mando TV 會自動找到你的電視，支援 Samsung、LG、Roku、Google TV 與 Android TV。',
    pasos=[
      '把手機與電視連上同一個 Wi-Fi。',
      '開啟 Mando TV。你的電視會自動出現在清單中，點選它即可。',
      '依你的品牌確認連線（詳細說明在下方）。',
      '用按鍵或手機鍵盤來控制電視。觸控板是 Pro 功能。',
    ],
    extra=[
      ('Samsung', '電視會詢問是否允許連線。第一次請在螢幕上確認。適用於採用 Tizen、2016 年及之後的機型。想用手機開機，請在「設定 > 一般 > 網路 > 專家設定」中啟用「以行動裝置開機」。'),
      ('LG', '電視會跳出詢問授權的提示。第一次請確認。想用手機開機，請在設定中找到「以行動裝置開啟電視」，並啟用「透過 Wi-Fi 開啟」。'),
      ('Roku', 'Roku 不需要配對：在清單中點選它就連上了。想開機的話，請在「設定 > 系統 > 電源」中啟用「電視快速啟動」。'),
      ('Google TV 與 Android TV', '電視會在畫面上顯示代碼。第一次請在 Mando TV 中輸入。想開機的話，請在設定中尋找「Wake on LAN」、「透過網路開機」或「網路待機」。'),
    ],
    marca=None,
    faq=[
      ('把手機當遙控器需要網際網路嗎？', '你只需要手機與電視在同一個 Wi-Fi。Mando TV 透過這個網路直接連到你的電視。'),
      ('為什麼電視沒有出現在清單中？', '請確認電視已開機，且手機沒有使用行動數據或另一個 Wi-Fi。有些路由器有訪客網路，會把裝置彼此隔離。'),
      ('我可以在 iPhone 或 Android 手機上使用 Mando TV 嗎？', 'iPhone 與 iPad 可以：App 已在 App Store 上架。Windows 版也可在 Microsoft Store 取得。Android 即將推出：你可以加入 Google Play 的免費搶先體驗。'),
    ]),
  dict(clave='pc', corto='用電腦控制電視',
    titulo='用 Windows 電腦控制電視（免費）',
    desc='用 Windows 電腦透過 Wi-Fi 當 Samsung、LG、Roku 或 Google TV 的遙控器。按鍵、鍵盤與 App 免費，電腦快捷鍵為 Pro。',
    h1='如何用 Windows 電腦控制電視',
    intro='如果你整天都在電腦前，就不必再到處找遙控器：Windows 版 Mando TV 可以透過家中的 Wi-Fi 控制你的 Samsung、LG、Roku、Google TV 或 Android TV 電視。切換 App、調整音量，或用電腦鍵盤在 YouTube 輸入文字都很方便。',
    pasos=[
      '從 Microsoft Store 免費下載 Mando TV 到你的 Windows 10 或 11 電腦。',
      '確認電腦與電視在同一個網路（Wi-Fi 或網路線皆可，但要接同一台路由器）。',
      '開啟 Mando TV：你的電視會自動出現在清單中。點選或按一下它即可。',
      '第一次請在電視畫面上確認連線（Google TV 與 Android TV 則要輸入電視顯示的代碼）。',
      '完成：用按鍵或鍵盤，就能在電視的搜尋欄輸入文字。觸控板是 Pro 功能。',
    ],
    extra=[
      ('電腦快捷鍵（Pro）', '使用 Mando TV Pro，你可以用電腦鍵盤控制電視：方向鍵導覽、Enter 為確定、Backspace 或 Esc 為返回、+ 與 - 調整音量、M 為靜音、空白鍵為暫停。'),
      ('隨時置頂的迷你遙控器（Pro）', '工作或在電腦上玩遊戲時，讓一個小小的遙控器視窗隨時顯示在最上層。'),
      ('從電腦對電視說話（Pro）', '使用 Mando TV Pro，你可以透過電腦的麥克風對電視下指令：「開啟 YouTube」、「大聲一點」或「30 分鐘後關機」，用平常說話的方式就行。在 Windows 上，語音會在電腦本機辨識：不需要網際網路，也不必更改 Windows 設定，並支援 App 的 6 種語言。你說的話不會離開電腦，也不會被儲存。只有非常舊的處理器，App 才會改用 Windows 的語音聽寫。這時需要在隱私權設定中開啟線上語音辨識，並在 Windows 中新增繁體中文（台灣）。如果缺少任何一項，App 會通知你，並用按鈕開啟設定。'),
    ],
    marca=None,
    faq=[
      ('用電腦控制電視需要線材或藍牙嗎？', '不需要。Mando TV 透過你的家用網路連線：電腦與電視只要接同一台路由器即可。'),
      ('每一台電視都能用嗎？', '支援採用 Tizen 的 Samsung 電視（2016 年及之後）、採用 webOS 的 LG、Roku，以及 Google TV 或 Android TV（Sony、Philips、TCL、Hisense、Sharp、小米、Toshiba、Panasonic、Haier、Skyworth 等）。'),
      ('要多少錢？', '按鍵、鍵盤與透過網路開機都是免費的，且沒有廣告。Mando TV Pro 是一次買斷、不需訂閱的方案，提供觸控板、電腦快捷鍵與迷你遙控器等額外功能。'),
      ('為什麼麥克風在 Windows 上聽不懂我說的話？', '請確認語音功能已啟用（屬於 Pro），且電腦的麥克風在 Windows 中可以正常運作。幾乎所有電腦都能在本機辨識語音，完全不需要網際網路。只有非常舊的處理器，App 才會改用 Windows 的語音聽寫。這時請確認 Windows 隱私權設定中已開啟線上語音辨識，且語言設定中有繁體中文（台灣）。Mando TV 只在聆聽期間使用這個語言。'),
    ]),
  dict(clave='roku-403', corto='Roku App 無法使用',
    titulo='Roku App 無法使用？排除 403 錯誤',
    desc='手機已連線，但 Roku 沒有反應？只要 5 個步驟啟用「行動 App 控制」，就能再次用手機當遙控器。',
    h1='Roku App 無法使用：這樣解決',
    intro='如果你的手機找得到 Roku 也連得上，但按任何按鍵都沒反應，幾乎都是 Roku 本身有一項設定擋住了遙控器 App。較新的 Roku 版本預設限制更嚴格。在 Roku 選單中，一分鐘就能解決。',
    pasos=[
      '在 Roku 上按「首頁」，然後前往「設定」。',
      '開啟「系統」，再進入「進階系統設定」。',
      '前往「行動 App 控制」。部分機型稱為「外部控制」。',
      '在「網路存取」中選擇「預設」或「已啟用」。如果你的機型只有開關，請保持在「已啟用」。',
      '回到手機上的 Mando TV，點選你的 Roku。現在按鍵就有反應了。',
    ],
    extra=[
      ('如何知道這是你的問題', '徵兆很明確：你的手機在清單中看得到 Roku 並能連線，但點按任何按鍵都沒有反應。在內部，Roku 會回應 403 錯誤，意思是「禁止」。Mando TV 在連線時會偵測到這一點，並在畫面上顯示的正是這些步驟。'),
      ('選「預設」還是「已啟用」？', '兩者都可以：Mando TV 只需要來自你家用網路的指令。如果選項是「已停用」（較新的軟體則是「受限」），Roku 就不會回應 App。'),
      ('如果你沒有 Roku 遙控器', '如果設定是「已停用」，只有實體的 Roku 遙控器才能更改。向別人借一支來改一次；之後一切都可以用手機完成。也請閱讀[Roku 遙控器不見了](@roku-lost)。'),
    ],
    marca='roku',
    faq=[
      ('為什麼我的 Roku 以前能用，現在卻沒反應？', 'Roku 更新可能讓這項設定變得更嚴格。這不是你的手機或 Wi-Fi 的問題：你只需要重新允許 App 控制。'),
      ('Roku 電視與 Roku 播放器都適用嗎？', '適用。Roku 播放器與 Roku 電視的這項設定位於同一個選單。'),
      ('把設定保持在「預設」安全嗎？', '安全。它只接受來自你家用網路中裝置的指令。'),
    ]),
  dict(clave='not-found', corto='手機找不到電視',
    titulo='手機找不到電視？檢查這 6 件事',
    desc='遙控器 App 找不到電視？請檢查 Wi-Fi、VPN 與區域網路權限。適用於 Samsung、LG、Roku 與 Android TV。',
    h1='手機找不到電視：請檢查這幾點',
    intro='你開啟遙控器 App，清單卻是空的，或是電視出現了但連線一直中斷。幾乎都是網路問題，而不是電視的問題。請依序檢查這些項目：第一項就能解決大部分情況。',
    pasos=[
      '看看手機連的是哪個 Wi-Fi，電視又是哪一個。它們必須是同一個網路，名稱也要相同。訪客網路無法使用，因為它會把裝置彼此隔離。',
      '如果你有使用 VPN，請在手機上關閉。啟用 VPN 時，手機會透過另一個網路連上網際網路，看不到你家裡的裝置，或是連線在幾秒後就中斷。',
      '暫時關閉行動數據。有些手機在訊號弱時，會自己從 Wi-Fi 切換到行動數據。',
      '開啟電視並等它完全啟動。關機的電視不會回應搜尋。',
      'iPhone 請確認 App 擁有「區域網路」權限：「設定 > 隱私權與安全性 > 區域網路」。',
      '如果還是沒有出現，請手動新增：在 Mando TV 點選「以 IP 新增」，並輸入電視的 IP 位址。',
    ],
    extra=[
      ('讓 App 引導你', '在電視清單中，有一個按鈕是給電視沒有出現的情況使用。App 會一步一步檢查最常見的原因（相同的 Wi-Fi、VPN、區域網路權限等），並在每次修正後顯示重新檢查的按鈕。這個精靈是免費的。'),
      ('哪裡可以找到電視的 IP 位址', '它位於電視的網路選單中，依機型略有不同。LG：設定、網路、Wi-Fi 連線、進階 Wi-Fi 設定。Samsung：設定、一般、網路、網路狀態、IP 設定。Roku：設定、網路、關於。Android TV 與 Google TV：設定、網路與網際網路，再點選你的網路。它是類似 192.168.1.86 的一串數字。'),
      ('如果電視出現了但連線中斷', '如果連線在幾秒後中斷，原因通常出在手機：VPN、切換到另一個 Wi-Fi，或省電模式。請關閉 VPN，留在同一個 Wi-Fi，再試一次。'),
      ('2.4 GHz 與 5 GHz 的 Wi-Fi', '只要兩者來自同一台路由器，手機在 5 GHz 網路、電視在 2.4 GHz 網路都沒有關係。如果你有 Wi-Fi 延伸器，電視仍然沒有出現，請把手機靠近主路由器再試一次。'),
    ],
    marca=None,
    faq=[
      ('我可以用行動數據控制電視嗎？', '不行。遙控訊號是透過你家的 Wi-Fi 傳送，所以手機與電視必須在同一個網路。'),
      ('為什麼開著 VPN 就不能用？', '因為 VPN 會讓手機的所有流量都經過另一個網路，手機就看不到你家裡的裝置了。使用遙控器時請把它關閉。'),
      ('可以用藍牙或紅外線嗎？', '智慧電視是用 Wi-Fi。紅外線只能在有紅外線發射器的 Android 手機上使用，適用於不是智慧電視的電視。藍牙在測試版中提供，免費，且僅限 Android 9 以上：手機會以藍牙鍵盤與遙控器的身分連到電視，完全不需要 Wi-Fi。適用於 Google TV、Android TV 與 Fire TV；其他接受藍牙鍵盤的品牌可能也能用，Roku 則不接受。'),
    ]),
  dict(clave='androidtv-code', corto='Android TV 配對碼',
    titulo='Android TV 要求配對碼：該怎麼做',
    desc='Android TV 或 Google TV 在連線時顯示 6 個字元的代碼。教你如何輸入，以及代碼沒出現或錯誤時怎麼辦。',
    h1='Android TV 要求配對碼：該怎麼做',
    intro='第一次把手機連到 Android TV 或 Google TV 時，電視會在畫面上顯示 6 個字元的代碼。這是正常的，而且只會發生一次：這樣能確保沒有其他人可以控制你的電視。以下說明如何輸入，以及代碼沒出現時該怎麼辦。',
    pasos=[
      '開啟電視，並讓主畫面保持顯示。',
      '在手機上開啟 Mando TV，與電視連在同一個 Wi-Fi，並在清單中點選你的電視。',
      '看一下電視畫面：會出現由 6 個字母與數字組成的代碼。',
      '照著畫面上顯示的原樣在手機上輸入，然後點選「配對」。字母只會從 A 到 F，所以圓形的字元一定是數字零。',
      '完成。電視會記住你的手機，不會再問代碼。',
    ],
    extra=[
      ('如果電視上沒有出現代碼', '請確認電視確實已開機，而不是待機，且手機在同一個 Wi-Fi。在手機上再點選一次電視。如果還是沒有出現，請重新啟動電視：拔掉電源十秒鐘，再插回去，然後重試。'),
      ('如果代碼被判定為錯誤', '每次要求都會產生新的代碼。如果你花了很久，或要求了兩次，只有畫面上最後一個有效。在手機上再點選一次電視，並輸入新的代碼。'),
      ('如果電視再次要求代碼', '當電視被還原為原廠設定，或你清除了手機上的 App 資料時，就會發生這種情況。重新配對後就會儲存。如果你完全沒有遙控器，請閱讀[沒有遙控器的 Android TV](@androidtv)。'),
    ],
    marca='android',
    faq=[
      ('哪些電視會使用這個代碼？', '搭載 Android TV 或 Google TV 的電視：Sony、Philips、TCL、Hisense、Sharp、小米、Chromecast with Google TV 等等。'),
      ('我的手機需要 Google 帳號嗎？', '不需要。你只需要畫面上的代碼。'),
      ('這樣安全嗎？', '安全。代碼證明你人就在電視前：沒有人能在看不到畫面的情況下完成配對。'),
    ]),
  dict(clave='roku-lost', corto='Roku 遙控器不見了',
    titulo='Roku 遙控器不見了？用手機透過 Wi-Fi 控制',
    desc='Roku 遙控器不見了？手機可以用 Wi-Fi 取代它。步驟簡單，連換了路由器、Roku 沒有 Wi-Fi 的情況也有辦法。',
    h1='Roku 遙控器不見了：用手機控制',
    intro='如果你的 Roku 遙控器不見了或不能用了，只要 Roku 仍連著你的 Wi-Fi，手機就能取代它。如果你換了 Wi-Fi 或路由器，也有解決的辦法。',
    pasos=[
      '先試著讓遙控器發出聲音。如果你的 Roku 遙控器有喇叭，例如 Roku Voice Remote Pro，請開啟 Mando TV，連上 Roku，並使用讓遙控器發出聲音的選項來找到它。這只適用於有喇叭的 Roku 遙控器，且 Roku 必須開機。',
      '開啟電視，並讓 Roku 保持連接。你什麼都不用動。',
      '把手機連上 Roku 使用的同一個 Wi-Fi。',
      '開啟 Mando TV。Roku 會自動出現在清單中，點選它即可。',
      '像使用原本的遙控器一樣，使用方向鍵、確定、首頁與返回。Roku 不會要求輸入代碼。',
      '如果按鍵沒有反應，表示 Roku 擋住了 App 控制：[Roku App 無法使用](@roku-403)這篇教學會告訴你如何允許。',
    ],
    extra=[
      ('如果 Roku 沒有 Wi-Fi（換了路由器或搬家）', '沒有遙控器就無法進入選單設定新網路，但有個辦法：Roku 會自動連上名稱與密碼和舊網路相同的網路。請用另一支手機建立一個名稱與密碼完全相同的 Wi-Fi 熱點，並讓有 Mando TV 的手機連上它，Roku 就會出現在清單中。接著前往「設定」、「網路」，把它連上新的 Wi-Fi。'),
      ('如果是 Roku 電視', 'Roku 電視在機身上有一個按鍵，幾乎都在正下方中間或背面，可以開啟電視。這樣就足以開機，並繼續用手機操作。'),
      ('如果你想買另一支遙控器', '請確認它適用於你的機型。藏在電視後面的小型 Roku 播放器需要不靠紅外線的遙控器，因為紅外線無法傳到它。'),
    ],
    marca='roku',
    faq=[
      ('手機可以開啟 Roku 嗎？', '接上電視的 Roku 播放器永遠是開著的。使用 Roku 電視時，如果已在「設定 > 系統 > 電源」啟用「電視快速啟動」，Mando TV 就能透過 Wi-Fi 開啟。'),
      ('那音量呢？', '使用 Roku 電視時，手機可以調大調小音量。如果是用 HDMI 連接的 Roku 播放器，就要看電視：有些可以，有些不行。'),
      ('需要建立帳號嗎？', '不需要。Mando TV 不需要帳號，而且同一個 App 還能控制 Samsung、LG 與 Android TV 電視。'),
    ]),
]

SOPORTE = dict(
  titulo='說明：連接 Mando TV 並開啟電視',
  desc='教你把 Mando TV 遙控器連接到 LG、Samsung、Roku 或 Android TV，用手機開啟電視，並解決常見問題。',
  h1='說明',
  intro='最常見的問題，依步驟順序排列。如果沒有找到你的問題，請寫信到 <a href="mailto:hola@mandotv.app?subject=Mando%20TV%20%E4%BD%BF%E7%94%A8%E6%B1%82%E5%8A%A9">hola@mandotv.app</a>，我們會回覆。',
)
SOPORTE_HTML = '''      <h2 id="encontrar">找到電視</h2>
      <div class="preguntas">
        <details open><summary>我的電視沒有出現在清單中</summary>
          <ol>
            <li>確認手機與電視在同一個 Wi-Fi。如果你的路由器有 2.4 GHz 與 5 GHz 兩個名稱不同的網路，它們有時會互相看不到。</li>
            <li>確認電視已開機。</li>
            <li>iPhone 請確認 Mando TV 擁有「區域網路」權限，位於「設定」、Mando TV 之下。</li>
            <li>在電視清單中，點選電視沒有出現時使用的按鈕：App 會一步一步檢查最常見的原因（相同的 Wi-Fi、VPN、區域網路權限等），並在每次修正後顯示重新檢查的按鈕。</li>
            <li>如果還是沒有出現，請點選 + 按鈕，選擇品牌，並輸入電視的 IP 位址。你可以在電視的網路選單中看到它（例如 192.168.1.50）。</li>
          </ol>
        </details>
        <details><summary>可以用行動數據或在外面使用嗎？</summary>
          <p>不行。Mando TV 是在你的家用網路內與電視通訊，所以手機必須連上這個 Wi-Fi。</p>
        </details>
      </div>

      <h2 id="conectar">第一次連線</h2>
      <p>依品牌的完整教學：<a href="@@R_lg@@">LG</a>、<a href="@@R_samsung@@">Samsung</a>、<a href="@@R_roku@@">Roku</a> 與 <a href="@@R_android@@">Android TV</a>。</p>
      <div class="preguntas">
        <details><summary>LG</summary>
          <p>當你點選電視時，畫面上會跳出詢問授權的提示。請用你平常的遙控器確認。你只需要做一次。</p>
        </details>
        <details><summary>Samsung</summary>
          <p>電視會詢問是否允許 Mando TV 連線。請用遙控器選擇「允許」。如果不小心拒絕了，請前往「設定 > 一般 > 外接裝置管理員 > 裝置連線管理員」，並改為允許。</p>
        </details>
        <details><summary>Roku</summary>
          <p>Roku 不會要求授權。如果連不上，請在 Roku 上前往「設定 > 系統 > 進階系統設定 > 行動 App 控制」，並把網路存取保持在「預設」或「已啟用」。</p>
        </details>
        <details><summary>Android TV 與 Google TV</summary>
          <p>電視會顯示 6 個字元的代碼。請照著畫面上的原樣在 Mando TV 中輸入。適用於 Sony、Philips、TCL、Hisense、Sharp、小米、Chromecast with Google TV，以及其他搭載 Android TV 的電視。</p>
        </details>
      </div>

      <h2 id="encender">透過 App 開啟電視</h2>
      <p>Mando TV 透過你的家用網路開啟電視。這需要兩個條件：你至少在電視開機時連線過一次，而且電視上已啟用透過網路開機。這項設定的名稱依機型而異，以下是最常見的：</p>
      <div class="preguntas">
        <details><summary>LG</summary>
          <p>在設定中（依機型位於「一般」或「連線」之下）找到「以行動裝置開啟電視」，並啟用「透過 Wi-Fi 開啟」。如果有「快速啟動+」，也請一併啟用。</p>
        </details>
        <details><summary>Samsung</summary>
          <p>在「設定 > 一般 > 網路 > 專家設定」中啟用「以行動裝置開機」。</p>
        </details>
        <details><summary>Roku</summary>
          <p>使用 Roku 電視時，請在「設定 > 系統 > 電源」中啟用「電視快速啟動」。接在電視上的 Roku 播放器無法用這個方式開機。</p>
        </details>
        <details><summary>Android TV 與 Google TV</summary>
          <p>這取決於製造商。請在網路或電源設定中尋找「Wake on LAN」、「透過網路開機」或「網路待機」。有些機型沒有這個選項。</p>
        </details>
      </div>

      <h2 id="falla">如果有地方不順利</h2>
      <div class="preguntas">
        <details><summary>連線中斷，或沒有任何反應</summary>
          <ol>
            <li>在遙控器畫面上點選「重新連線」。</li>
            <li>如果沒有幫助，請關閉 Mando TV，並重新開啟 App。</li>
            <li>如果電視取得了新的 IP 位址，請把它從清單中移除，再重新新增。</li>
          </ol>
        </details>
        <details><summary>如何傳送錯誤報告給我們</summary>
          <ol>
            <li>在 Mando TV 中點選「自訂」按鈕（上方的滑桿圖示）。</li>
            <li>點選「複製測試報告」。</li>
            <li>把它與電視的品牌與型號一起貼到寄給 hola@mandotv.app 的電子郵件中。</li>
          </ol>
          <p>報告不包含密碼、代碼，也不包含你輸入的任何內容。</p>
        </details>
        <details><summary>我買了 Pro，但是沒有出現</summary>
          <p>在「自訂」中點選「還原購買」，並使用你購買時的同一個商店帳號。如果仍然沒有出現，請寫信給我們。</p>
        </details>
      </div>

      <h2 id="guias">步驟教學</h2>
      <p><a href="@@R_guias@@">查看所有教學</a></p>
      <ul>
@@GUIAS@@
      </ul>

      <h2 id="contacto">還有問題嗎？</h2>
      <p>請寫信到 <a href="mailto:hola@mandotv.app?subject=Mando%20TV%20%E4%BD%BF%E7%94%A8%E6%B1%82%E5%8A%A9">hola@mandotv.app</a>。告訴我們電視的品牌與型號，以及你卡在哪一個步驟。你可以用自己的語言寫信給我們。我們以西班牙文或英文回覆，如果你需要，也可以借助翻譯工具用你的語言回覆。</p>
'''

PRIVACIDAD = dict(
  titulo='隱私權政策 | Mando TV',
  desc='Mando TV 不蒐集任何個人資料：沒有帳號、沒有廣告、沒有追蹤器。App 只會在你的 Wi-Fi 內與你的電視通訊。',
  h1='隱私權',
  intro='簡單來說：Mando TV 不蒐集你的資料。沒有帳號、沒有廣告、沒有追蹤器，也沒有任何會儲存你操作內容的自有伺服器。',
)
PRIVACIDAD_HTML = '''      <p class="fecha">自 2026 年 11 月 14 日起生效。最後更新日期：2026 年 11 月 25 日。</p>

      <h2>我們是誰</h2>
      <p>Mando TV 是一款讓你用手機或電腦控制電視的 App。本政策說明 App 會使用哪些資訊，以及如何處理。如有任何問題，請寫信到 <a href="mailto:hola@mandotv.app">hola@mandotv.app</a>。</p>

      <h2>我們蒐集哪些資料</h2>
      <p>App：沒有。App 不會向我們或任何第三方傳送關於你或你使用方式的任何資訊。它不使用任何分析、廣告或追蹤工具。</p>
      <p>本網站：我們以兩種方式統計造訪次數，詳見<a href="#cookies">本網站的 Cookie</a>一節。</p>

      <h2>App 在你的裝置上儲存什麼</h2>
      <p>為了正常運作，App 只會在你的手機或電腦上儲存以下內容：</p>
      <ul>
        <li>你新增的電視：名稱、品牌、在你網路中的 IP 位址，以及用於開機的網路硬體位址（MAC）。</li>
        <li>當你確認授權時，每台電視交給 App 的連線金鑰。它們會加密後存放在系統的安全儲存空間中（iPhone 與 Mac 的鑰匙圈、Android 的 Keystore、Windows 的受保護儲存空間）。</li>
        <li>你的偏好設定：淺色或深色主題、背景顏色、震動與遙控器類型。</li>
        <li>如果你使用 Pro 功能：你的常用 App、例程與最近的 YouTube 搜尋（你可以在 App 中刪除）。</li>
      </ul>
      <p>當你刪除 App 時，這一切也會隨之刪除。</p>

      <h2>App 與誰通訊</h2>
      <p>與你的電視通訊，範圍僅限你家中的 Wi-Fi。為了找到電視，App 會搜尋你的區域網路；因此在 iPhone 上，它會要求「區域網路」權限。你用 App 鍵盤輸入的文字會直接傳送到電視，不會被儲存。</p>
      <p>此外，App 開啟時會從本網站下載一個小型公開檔案（mandotv.app/app/config.json），以得知是否有你應該安裝的新版本，以及哪些功能屬於 Mando TV Pro。這就像開啟網頁一樣只是下載：App 不會傳送你的資料、你的電視或你的操作。它只會告知 App 版本與系統（例如 Android），好讓它顯示適當的提示。如果你沒有網際網路，App 會繼續使用上次下載的檔案；如果超過 30 天都無法下載，App 會請你暫時連上網際網路。</p>

      <p>當你傳送照片或影片到電視（Pro 功能）時，電視只會透過你家中的 Wi-Fi，直接從你的手機或電腦下載你選擇的檔案。它們不會經過網際網路，也不會經過我們，App 看不到你的其他照片，而且一旦你關閉該畫面，分享就會結束。</p>
      <h2>麥克風與語音</h2>
      <p>語音搜尋只會在你按住說話按鈕時使用麥克風。你說的話會由系統的語音辨識轉換為文字：iPhone 與 Mac 由 Apple 處理，Android 由 Google 處理，各依其自己的隱私權政策。在 Windows 上，語音會在你自己的電腦上辨識，不會離開裝置；只有非常舊的處理器，App 才會使用 Microsoft 提供的 Windows 語音輸入，並依其隱私權政策處理。Mando TV 不會錄下或儲存音訊，產生的文字會直接傳送到你的電視，就像你用鍵盤輸入的內容一樣。</p>

      <h2>家庭：Apple 家庭與 Google Home 的裝置</h2>
      <p>當你開啟「家庭」區塊（測試中）時，App 會要求權限，以查看你已經在 Apple 的「家庭」App（HomeKit）或 Google Home 中擁有的裝置。取得此權限後，它會讀取裝置的名稱、所在房間與狀態（開或關、亮度、溫度，或家電目前執行到程序的哪個階段），以便顯示它們，並把你點選的指令傳送給它們。一切都在你的手機與 Apple 或 Google 的系統之間進行：Mando TV 不會儲存這份清單，不會傳送給我們或第三方，也不會用於廣告或分析。在 Android 上，Google Home 使用你自己的 Google 帳號，並依 Google 的隱私權政策處理。你可以隨時撤銷權限：iPhone 在「設定 &gt; 隱私權與安全性 &gt; HomeKit」，Android 則在你的 Google 帳號設定中。</p>
      <p>當你點選「家庭功能對你好用嗎？」時，會開啟你的電子郵件 App，並建立一封寄給 hola@mandotv.app 的郵件，內含技術摘要：App 版本、系統，以及各類裝置出現的數量與它們是否有回應。其中不包含裝置、房間或你家的名稱，而且只有在你自己按下傳送時，郵件才會寄出。</p>

      <h2>測試報告</h2>
      <p>App 有一個「複製測試報告」按鈕，可協助我們修正錯誤。報告只會在 App 開啟期間保留在 App 的記憶體中，絕不會自動傳送：是否複製與分享，由你決定。它不包含連線金鑰、配對碼，也不包含你輸入的任何內容；只有 App 執行過的步驟，例如搜尋、連線與錯誤。</p>

      <h2 id="cookies">本網站的 Cookie</h2>
      <p>這只適用於 mandotv.app 網站，不適用於 App。</p>
      <h3>一律不使用 Cookie</h3>
      <p>我們使用 Cloudflare Web Analytics 匿名統計造訪次數：有多少人造訪網站、他們閱讀哪些頁面，以及來自哪個國家。它不使用 Cookie，不使用你的 IP 位址來識別你，也不會追蹤你在其他網站上的行為。</p>
      <h3>使用 Cookie，僅在你同意時</h3>
      <p>當你在 Cookie 提示中點選「接受」，我們會啟用 Google Analytics（Google LLC 提供），以更了解網站的使用情況：頁面瀏覽、停留時間、裝置類型、大約的城市，以及你從哪裡來。為此，它會在你的瀏覽器中儲存 _ga 與 _ga_* Cookie，最長 2 年。Google 可能會在智利以外的伺服器上處理這些資料。我們已停用廣告功能與 Google Signals，也不會使用這些資料向你顯示廣告。</p>
      <p>如果你點選「拒絕」或沒有選擇，就不會載入 Google Analytics，也不會儲存任何 Cookie。你可以隨時使用每個頁面底部的「Cookie」按鈕更改決定；如果你撤回同意，我們會刪除這些 Cookie。</p>
      <p>你的選擇會儲存在你的瀏覽器中（本機儲存空間，不會傳送給任何人），好讓我們不會再問你一次。</p>

      <h2>購買</h2>
      <p>當你購買 Mando TV Pro 時，付款由應用程式商店處理（App Store、Google Play 或 Microsoft Store）。我們不會收到也不會儲存你的卡片資料。商店只會向 App 確認購買紀錄存在。</p>

      <h2>你寄給我們的電子郵件</h2>
      <p>當你寫信到 <a href="mailto:hola@mandotv.app">hola@mandotv.app</a> 時，我們只會使用你的電子郵件地址與你告訴我們的內容來回覆你。我們不會分享，也不會用於廣告。你可以隨時要求我們刪除你的訊息。</p>

      <h2>兒童</h2>
      <p>App 不會蒐集任何人的資料，包括兒童。</p>

      <h2>本政策的變更</h2>
      <p>如果有一天 App 處理你資料的方式有所改變，我們會在變更到達 App 之前，更新本頁面與上方的日期。</p>
'''


# >>> guías traídas del inglés (ensamblar.py)
# Adaptadas con Ollama (qwen3.6:35b) desde las guías inglesas y auditadas por Opus el 22-nov. Rutas en idiomas_sitio.py.
GUIAS += [
  dict(clave='no-sub', corto='免訂閱的遙控器 App', fecha='2026-11-23',
    titulo='免訂閱、無廣告的電視遙控器 App',
    desc='受夠了有廣告或要按週訂閱的遙控器 App？Mando TV 免費、無廣告，Pro 是選購的一次買斷。誠實比較。',
    h1='免訂閱、無廣告的遙控器 App',
    intro='許多萬用遙控器 App 會顯示廣告，或要求按週訂閱後才能使用。Mando TV 走不同的路：遙控器免費，沒有廣告，也不需要帳號。選購的 Pro 只需要買一次。以下是比較，也包含這個 App 做不到的事。',
    pasos=[
      '安裝之前，先開啟 App 的商店頁面，檢查 App 內購買項目。按週或按月的價格代表訂閱制。',
      '在 Google Play 上，確認頁面是否寫著「含廣告」，並閱讀最新的低星評價：意外的付費牆常常出現在那裡。',
      '確認這個 App 能透過 Wi-Fi 控制你的電視。Mando TV 支援 Samsung（2016 年起）、LG webOS、Roku、Google TV、Android TV 與 Fire TV。',
      '安裝 Mando TV，把手機連上與電視相同的 Wi-Fi，並在清單中點選你的電視。',
      '確認電視上的提示，或輸入顯示的代碼。按鍵、音量、頻道與鍵盤都不用花錢。',
    ],
    tabla=dict(titulo='Mando TV 與許多遙控器 App 的比較',
      cabeza=['', 'Mando TV', '許多靠廣告或訂閱的 App'],
      filas=[
        ['基本遙控器', '免費', '常是含廣告的免費版，或藏在試用期後面'],
        ['廣告', '沒有', '很常見'],
        ['訂閱', '沒有。Pro 是選購的一次買斷', '按週或按月的方案很常見'],
        ['帳號', '不需要', '依 App 而異'],
        ['透過 Wi-Fi 的智慧電視', 'Samsung（2016 年起）、LG webOS、Roku、Google TV、Android TV、Fire TV、Apple TV（測試版）', '依 App 而異'],
        ['給舊電視的紅外線', 'Android 手機有紅外線發射器即可免費使用（新功能）', '部分 App 提供，且僅限有紅外線發射器的手機'],
        ['藍牙', 'Android 9 以上的測試版，免費', '依 App 而異'],
        ['照片與影片傳到電視', 'Pro，透過 Wi-Fi（不是螢幕鏡射）', '依 App 而異'],
        ['手機與電腦', 'iPhone、iPad 與 Windows，另有 Android 搶先體驗', '依 App 而異'],
        ['螢幕鏡射', 'iPhone 與 iPad 免費，透過控制中心的螢幕鏡像功能（支援 AirPlay 的電視）', '部分 App 提供'],
      ],
      nota='Mando TV 並未與任何特定 App 比較。最新價格請以各 App 的商店頁面為準。'),
    extra=[
      ('Mando TV 不做什麼', '它沒有自己的螢幕鏡射功能：在 iPhone 與 iPad 上，它會帶你前往控制中心的螢幕鏡像，這是 iPhone 本身的功能，可搭配支援 AirPlay 的電視。使用 Mando TV Pro，它還可以透過你的 Wi-Fi 把照片與影片傳送到電視。它是透過家用 Wi-Fi 控制智慧電視。不是智慧電視的電視，可以用有紅外線發射器的 Android 手機以紅外線控制。Android 9 以上，手機也能以藍牙鍵盤與遙控器的身分連到 Google TV、Android TV 與 Fire TV，完全不需要 Wi-Fi。這個選項在測試版，而且免費。'),
      ('Mando TV 怎麼賺錢', '不靠廣告，也不靠你的資料：App 不蒐集任何資料。Mando TV 靠 Pro 維持營運，這是選購的一次買斷方案，提供額外功能。基本遙控器是免費的。'),
      ('在你已有的裝置上', 'iPhone 與 iPad 從 App Store 下載，Windows 電腦從 Microsoft Store 下載，Android 則透過 Google Play 的免費搶先體驗。請參考[iPhone 遙控器 App](@iphone)與[Windows 遙控器 App](@windows)。'),
      ('隱私', 'App 內沒有帳號，也沒有追蹤。與電視的通訊只在區域網路內進行，連線資料會加密保存在你的裝置上。詳情請見[隱私權政策](@privacidad)。'),
    ],
    marca=None,
    faq=[
      ('有免訂閱的遙控器 App 嗎？', '有。Mando TV 完全沒有訂閱：遙控器免費、沒有廣告，Pro 是選購的一次買斷。'),
      ('Mando TV 真的免費嗎？', '是的。方向鍵、確定、返回、首頁、音量、頻道、數字、鍵盤與開關機都是免費的，沒有廣告，也沒有時間限制。'),
      ('沒有 Wi-Fi 也能用嗎？', '大多數情況不行。Mando TV 透過你的家用 Wi-Fi 控制智慧電視。例外是：有紅外線發射器的 Android 手機可用紅外線，也適用於不是智慧電視或沒有連上 Wi-Fi 的電視；以及 Android 9 以上測試版的藍牙，適用於 Google TV、Android TV 與 Fire TV。'),
    ]),
  dict(clave='roku-app-alt', corto='Roku App 替代方案', fecha='2026-11-23',
    titulo='Roku App 的替代方案：簡單好用的 Roku 遙控器',
    desc='Roku App 遙控功能的替代方案：Mando TV 透過 Wi-Fi 控制 Roku 電視與播放器，不需帳號、沒有廣告，並支援 Samsung、LG 與 Google TV。',
    h1='Roku App 的替代方案：一個 App 控制所有電視',
    intro='官方 Roku App 功能很多：頻道商店、投放、私人聆聽，還有遙控器。如果你只想要一個快速的遙控器，或家裡也有 Samsung、LG 或 Google TV 電視，Mando TV 是個簡單的替代方案，不需帳號就能透過 Wi-Fi 控制 Roku。',
    pasos=[
      '把手機與 Roku 連上同一個 Wi-Fi。',
      '下載並開啟 Mando TV。你的 Roku 電視或 Roku 播放器會出現在清單中，點選它即可。Roku 不會要求輸入代碼。',
      '使用方向鍵、確定、返回、首頁、音量與鍵盤。用手機鍵盤在 Roku 頻道中輸入搜尋內容。',
      '如果按鍵沒有反應，請在 Roku 上前往「設定 > 系統 > 進階系統設定 > 行動 App 控制」，並把網路存取設為「預設」或「已啟用」（較新的 Roku 軟體則把「行動 App 控制」設為「已啟用」）。',
      '選用：在 Roku 電視上於「設定 > 系統 > 電源」啟用「電視快速啟動」，讓 Mando TV 可以開啟電視。',
    ],
    extra=[
      ('Mando TV 更適合的地方', '一個 App 控制多台電視：Roku、Samsung、LG 與 Google TV 或 Android TV。不需帳號，沒有廣告。它也能在 Windows 電腦上使用，坐在書桌前很方便。方向鍵與音量反應很快，用鍵盤輸入搜尋內容也毫不費力。'),
      ('官方 Roku App 更好的地方', '請保留 Roku App，用於遙控器以外的功能，例如瀏覽並新增 Roku 頻道商店的頻道，以及它自己的投放與私人聆聽（用手機上的耳機聽聲音）。你想的話可以兩者並用，它們可以在同一支手機上運作。'),
      ('Roku 電視與 Roku 播放器', '兩者都支援。包括 TCL、Hisense、Philips 等品牌的 Roku 電視機型，以及 Roku Express、Streaming Stick 與 Ultra。詳情請見[Roku 遙控器 App 頁面](@roku)。'),
      ('如果 Roku App 不能用了', '如果按鍵不再有反應，通常是 Roku 擋住了 App 控制。[Roku App 無法使用](@roku-403)這篇教學會告訴你解決問題的設定。'),
      ('免費與 Pro', '方向鍵、確定、返回、首頁、音量、頻道、數字鍵、鍵盤、開啟 App、切換輸入來源與開關機都是免費的，沒有廣告，也不需訂閱。Mando TV Pro 是選購的一次買斷方案，提供額外功能。'),
    ],
    marca='roku',
    faq=[
      ('使用 Mando TV 需要 Roku 帳號嗎？', '不需要。Mando TV 透過你的家用網路與 Roku 通訊，也不會要求帳號。'),
      ('Mando TV 能完全取代 Roku 行動 App 嗎？', '作為遙控器可以。至於頻道商店、投放與私人聆聽，請保留官方 Roku App。'),
      ('支援我的 Roku Express 或 Streaming Stick 嗎？', '支援。所有 Roku 播放器與 Roku 電視的控制方式都一樣。'),
    ]),
  dict(clave='lg-thinq', corto='LG ThinQ App 替代方案', fecha='2026-11-23',
    titulo='LG ThinQ App 的替代方案：免帳號的 LG 遙控器',
    desc='想找只當遙控器用的 LG ThinQ App 替代方案？Mando TV 透過 Wi-Fi 控制採用 webOS 的 LG 電視，不需 LG 帳號，沒有廣告。',
    h1='你的 LG 電視可用的 LG ThinQ App 替代方案',
    intro='LG ThinQ 是 LG 的官方 App，為整個智慧家庭而設計：家電、電視等等。如果你只想要一個簡單的 LG 電視遙控器，Mando TV 透過你家中的 Wi-Fi 就能做到，不需要建立 LG 帳號，也沒有廣告。',
    pasos=[
      '把手機或電腦（iPhone、Android 或 Windows）與 LG 電視連上同一個 Wi-Fi。',
      '下載並開啟 Mando TV。你的 LG 電視會自動出現在清單中，點選它即可。',
      '電視上會出現提示。請用電視的遙控器、螢幕下方的搖桿或 Magic Remote 確認一次。',
      '按鍵、音量與鍵盤立刻可用。你不需要 LG 帳號，也不必註冊電視。',
      '選用：在電視設定中啟用「以行動裝置開啟電視」，讓你也能用手機開電視。',
    ],
    extra=[
      ('Mando TV 或 LG ThinQ：各自用在哪裡', '如果你想管理洗衣機、冰箱或冷氣等 LG 家電，或需要 LG 帳號的功能，請使用 ThinQ。如果你想要一個快速、簡單的電視遙控器，而且同一個 App 也能控制 Samsung、Roku 與 Google TV，請使用 Mando TV。許多人兩個都留著：ThinQ 管家電，Mando TV 管電視。'),
      ('Mando TV 在 LG 電視上做什麼', '它適用於採用 webOS 的 LG 智慧電視，也就是 2014 年以後的大多數機型，包括 LED、NanoCell、QNED 與 OLED。它提供方向鍵、確定、返回、首頁、音量、頻道、靜音、播放控制，以及可在 YouTube、Netflix 或瀏覽器輸入文字的鍵盤。App 清單與輸入來源清單也是免費的。使用 Pro 還能獲得像 Magic Remote 的游標。'),
      ('Mando TV 不做什麼', '它不會控制 LG 家電，不使用你的 LG 帳號，也不會取代電視上的 LG 帳號服務。它是遙控器，不是智慧家庭中樞。'),
      ('隱私與廣告', 'Mando TV 沒有廣告，也沒有帳號。它只在你的家用網路內與電視通訊，並把連線金鑰加密保存在你的裝置上。所有功能請見[LG 電視遙控器 App](@lg)頁面。'),
      ('免費與 Pro', '方向鍵、確定、返回、首頁、音量、頻道、數字鍵、鍵盤、開啟 App、切換輸入來源與開關機都是免費的，沒有廣告，也不需訂閱。Mando TV Pro 是選購的一次買斷方案，提供額外功能。'),
    ],
    marca='lg',
    faq=[
      ('不用 LG ThinQ App 也能控制我的 LG 電視嗎？', '可以。Mando TV 直接透過你的 Wi-Fi 連到採用 webOS 的 LG 電視。你只需要在電視上接受一次提示就完成了，完全不需要 LG 帳號。'),
      ('Mando TV 有 LG Magic Remote 的游標功能嗎？', 'Mando TV Pro 有一個游標，你可以用手指在手機螢幕上移動，就像 Magic Remote 移動箭頭一樣。'),
      ('Mando TV 是 LG 的產品嗎？', '不是。Mando TV 是獨立的 App，與 LG 沒有任何關聯。LG 與 ThinQ 歸其擁有者所有，僅用於說明相容性。'),
    ]),
  dict(clave='smartthings', corto='SmartThings 替代方案', fecha='2026-11-23',
    titulo='SmartThings 不能用？Samsung 的簡單替代方案',
    desc='SmartThings 太慢或出錯？Mando TV 透過 Wi-Fi 直接控制採用 Tizen 的 Samsung 電視。不需 Samsung 帳號，沒有廣告。步驟清楚。',
    h1='Samsung 電視的 SmartThings 替代方案',
    intro='SmartThings 是 Samsung 的智慧家庭 App，它的遙控器功能要透過你的 Samsung 帳號。如果它壞了，或你想要快速的解決辦法，Mando TV 可以透過你的 Wi-Fi，不需帳號就直接控制採用 Tizen、2016 年及之後的 Samsung 電視。',
    pasos=[
      '把手機與 Samsung 電視連上同一個 Wi-Fi。',
      '下載並開啟 Mando TV。你的 Samsung 電視會自動出現在清單中，點選它即可。',
      '電視會詢問是否允許連線。請用遙控器或電視上的按鍵選擇「允許」（只需要第一次）。',
      '立刻就能使用方向鍵、確定、返回、首頁、音量、頻道與鍵盤。',
      '選用：在「設定 > 一般 > 網路 > 專家設定」啟用「以行動裝置開機」，讓 Mando TV 也能開啟電視。',
    ],
    extra=[
      ('為什麼手機遙控器不能用了', '原因通常很簡單：手機與電視在不同的 Wi-Fi、VPN 已啟用，或電視處於深度待機。使用 SmartThings 時，Samsung 帳號也可能造成問題，例如你被登出了。Mando TV 直接與家用網路中的電視通訊，沒有需要登入的帳號。更多建議請見[手機找不到電視](@not-found)。'),
      ('Mando TV 或 SmartThings：各自用在哪裡', '如果你用 SmartThings 管理 Samsung 家電、燈具或其他智慧家庭裝置，或用於 Samsung 帳號的功能，請繼續保留它。如果你只是想要一個快速的電視遙控器，或家裡也有 LG、Roku、Google TV 或 Fire TV 的裝置，請使用 Mando TV：一個 App 控制全部。兩個 App 可以安裝在同一支手機上。'),
      ('如果你不小心拒絕了授權', '在電視上前往「設定 > 一般 > 外接裝置管理員 > 裝置連線管理員」，把 Mando TV 改為允許。'),
      ('沒有遙控器？', '你可以用電視本身的按鍵確認提示。[沒有原廠遙控器的 Samsung 電視](@samsung-lost)這篇教學會告訴你怎麼做。'),
      ('免費與 Pro', '遙控器可以免費下載與使用，沒有廣告，也不需訂閱。Mando TV Pro 是選購的一次買斷方案，提供額外功能。'),
    ],
    marca='samsung',
    faq=[
      ('不用 SmartThings 也能控制我的 Samsung 電視嗎？', '可以。Mando TV 直接透過你的 Wi-Fi 連到採用 Tizen 的 Samsung 電視。你只需要在電視上允許一次連線，不需要 Samsung 帳號。'),
      ('Mando TV 也能控制 Samsung 家電嗎？', '不能。它只是電視遙控器。家電與其他智慧家庭裝置，請繼續使用 SmartThings。'),
      ('Mando TV 是 Samsung 的產品嗎？', '不是。Mando TV 是獨立的 App，與 Samsung 沒有任何關聯。Samsung 與 SmartThings 歸其擁有者所有，僅用於說明相容性。'),
    ]),
  dict(clave='googletv-alt', corto='Google TV 遙控器替代方案', fecha='2026-11-23',
    titulo='Google TV 遙控器不能用？替代方案在這裡',
    desc='Google TV 的手機遙控器找不到電視？Mando TV 透過 Wi-Fi 控制 Google TV 與 Android TV，不需 Google 帳號，沒有廣告。',
    h1='手機版 Google TV 遙控器的替代方案',
    intro='Google TV 與 Android TV 的手機遙控器功能內建在 Google 自己的 App 中，並與你的 Google 帳號綁定。如果它找不到電視，你就沒辦法繼續。Mando TV 是獨立的遙控器 App，以畫面上的 6 個字元代碼配對，不需 Google 帳號，可在 iPhone、Android 手機或 Windows 電腦上使用。',
    pasos=[
      '開啟電視，並把手機連上同一個 Wi-Fi。',
      '下載並開啟 Mando TV。在清單中點選你的 Google TV 或 Android TV 電視。',
      '電視會顯示 6 個字元的代碼。在 Mando TV 中輸入，並點選「配對」。',
      '使用方向鍵、確定、返回、首頁、音量與鍵盤。你不需要登入任何地方。',
      '選用：在電視設定中尋找 Wake on LAN 或「透過網路開機」，讓 App 也能開啟電視。',
    ],
    extra=[
      ('為什麼手機遙控器找不到電視了', '大多數時候是網路問題：手機與電視在不同的 Wi-Fi、VPN 已啟用，或訪客網路隔離了裝置。請先解決這個問題，因為它會影響所有遙控器 App。更多資訊請見[手機找不到電視](@not-found)。'),
      ('適用的電視', '搭載 Google TV 與 Android TV 的 Sony、TCL、Hisense、Philips、Sharp、小米、Toshiba 等電視，以及 Chromecast with Google TV、Google TV Streamer 與 Nvidia Shield。配對方式都一樣，只要用畫面上的代碼完成一次即可。'),
      ('Google 的 App 更好的地方', 'Google 的 App 還能幫你找到想看的內容，並記住你的待看清單。為了這些功能，請繼續保留它。Mando TV 只是遙控器，另外還能在同一個 App 中控制 Samsung、LG、Roku 與 Fire TV 裝置，也能從 Windows 電腦操作。'),
      ('如果找不到舊的 Android TV 遙控器 App', 'Google 把手機遙控器功能從舊的 Android TV Remote Control App 移到了 Google TV App。如果你想找獨立的遙控器，Mando TV 是個選擇。'),
      ('免費與 Pro', '遙控器可以免費下載與使用，沒有廣告，也不需訂閱。Mando TV Pro 是選購的一次買斷方案，提供額外功能。'),
    ],
    marca='android',
    faq=[
      ('用 Mando TV 控制 Google TV 需要 Google 帳號嗎？', '不需要。電視上的代碼就足以完成配對。'),
      ('支援 Chromecast with Google TV 嗎？', '支援。配對方式相同，使用畫面上的 6 個字元代碼。'),
      ('可以在 iPhone 上使用嗎？', '可以。Mando TV 在 App Store 提供 iPhone 與 iPad 版，Microsoft Store 提供 Windows 版，Android 版則可透過 Google Play 的免費搶先體驗取得。'),
    ]),
  dict(clave='windows', corto='Windows 電腦遙控器', fecha='2026-11-23',
    titulo='Windows 遙控器 App：用電腦控制電視',
    desc='用 Mando TV 從 Windows 電腦控制 Samsung、LG、Roku、Google TV 或 Fire TV：快捷鍵、迷你遙控器與 Wi-Fi。可在 Microsoft Store 下載。',
    h1='Windows 電腦的遙控器 App',
    intro='Mando TV 有 Windows 版 App，透過家用網路把你的電腦或筆電變成電視遙控器。用你真正的鍵盤在電視上輸入文字，工作時讓一個小小的遙控器視窗留在最上層，並用同一個 App 控制 Samsung、LG、Roku、Google TV 或 Fire TV。',
    pasos=[
      '從 Microsoft Store 免費安裝 Mando TV 到 Windows 10 或 11 的電腦。',
      '確認電腦與電視在同一個網路，透過 Wi-Fi 或網路線接在同一台路由器。',
      '開啟 Mando TV。電視會出現在清單中，按一下它即可。',
      '如果電視有詢問（LG、Samsung），請確認提示；或輸入顯示的代碼（Google TV、Fire TV）。',
      '按一下按鍵，或用鍵盤輸入搜尋內容。完成。',
    ],
    extra=[
      ('快捷鍵（Pro）', '使用 Pro，你的電腦鍵盤就是遙控器：方向鍵移動、Enter 為確定、Backspace 或 Esc 為返回、加號與減號調整音量、M 為靜音、空白鍵為暫停。'),
      ('迷你遙控器（Pro）', '一個小小的遙控器視窗，會停留在所有其他視窗上方。這樣你調整音量或暫停時，不必中斷手邊的工作。'),
      ('從電腦在電視上輸入文字', '電視的螢幕鍵盤很慢。在 Mando TV 中，你可以用真正的鍵盤輸入，文字會出現在電視的搜尋欄。這個部分是免費的。'),
      ('更多詳情', '逐步教學請見[用電腦控制電視](@pc)。手機版請閱讀[用 Wi-Fi 把手機當遙控器](@wifi)。'),
      ('免費與 Pro', '方向鍵、確定、返回、首頁、音量、頻道、數字鍵、鍵盤、開啟 App、切換輸入來源與開關機都是免費的，沒有廣告，也不需訂閱。Mando TV Pro 是選購的一次買斷方案，提供額外功能。在 Windows 上，Pro 透過 Microsoft Store 購買。'),
      ('從電腦下語音指令（Pro）', '使用 Pro，你可以透過電腦的麥克風對電視說話。語音會直接在電腦上辨識：不需要網際網路，也不必在 Windows 中更改任何設定。你說的話絕不會離開電腦，也不會被儲存。只有非常舊的處理器，App 才會改用 Windows 的語音輸入。這時需要在隱私權設定中開啟線上語音辨識，並在 Windows 中新增你的語言。'),
    ],
    marca=None,
    faq=[
      ('Windows 遙控器 App 需要藍牙或線材嗎？', '不需要。它使用你的家用網路。電腦與電視只要接在同一台路由器即可。'),
      ('我可以從 Windows 控制哪些電視？', '採用 Tizen 的 Samsung 電視、採用 webOS 的 LG 電視、Roku 電視與播放器、Google TV 與 Android TV，以及 Fire TV。'),
      ('我可以在電腦上看電視畫面，或從電腦喇叭聽到聲音嗎？', '不行。Mando TV 只是遙控器。它不會把電視畫面鏡射或串流到電腦。'),
      ('為什麼語音在我的 Windows 電腦上不能用？', '語音控制是 Pro 功能。請確認 Pro 已啟用，且電腦的麥克風可以正常運作。在大多數電腦上，語音會直接在電腦上辨識，不需要網際網路。只有非常舊的處理器，App 才會使用 Windows 的語音輸入：這時請在 Windows 隱私權設定中開啟線上語音辨識，並在語言設定中新增你的語言。'),
    ]),
  dict(clave='iphone', corto='iPhone 遙控器 App', fecha='2026-11-23',
    titulo='iPhone 遙控器 App：Samsung、LG、Roku、Google TV',
    desc='用 iPhone 透過 Wi-Fi 當 Samsung、LG、Roku、Google TV 與 Fire TV 的遙控器。App Store 免費下載，不需帳號，沒有廣告。',
    h1='iPhone 遙控器 App：一個 App 控制所有電視',
    intro='Mando TV 透過你家中的 Wi-Fi，讓你的 iPhone 或 iPad 變成 Samsung、LG、Roku、Google TV、Android TV 與 Fire TV 的遙控器。App 在 App Store 免費下載，不需帳號，沒有廣告。它也能在 Android 與 Windows 上使用。',
    pasos=[
      '從 App Store 免費下載 Mando TV。',
      '把 iPhone 與電視連上同一個 Wi-Fi。',
      '開啟 Mando TV，當 iOS 詢問是否允許存取區域網路時，點選「允許」。App 需要這個權限才能找到電視。',
      '在清單中點選你的電視。如果電視有詢問（LG 與 Samsung），請在電視上確認提示；或輸入電視顯示的代碼（Google TV 或 Fire TV）。',
      '使用按鍵、音量與鍵盤。你已經連線了。',
    ],
    extra=[
      ('適用的電視', 'LG webOS、Samsung Tizen（2016 年及之後）、Roku 電視與 Roku 播放器、Google TV 與 Android TV，以及 Fire TV。各品牌頁面為 [Samsung](@samsung)、[LG](@lg)、[Roku](@roku) 與 [Android TV](@android)。'),
      ('為什麼會要求區域網路', 'iPhone 預設會阻止 App 存取你家用網路中的裝置，除非你允許。如果電視沒有出現在清單中，請開啟「設定 > Mando TV」，並啟用「區域網路」。App 只會在你的家用網路內與電視通訊。'),
      ('為什麼用 Mando TV，而不是品牌自己的 App', '每個電視品牌都有自己的 App，並要求各自的設定或帳號。Mando TV 是一個適用所有品牌的 App，不需帳號。'),
      ('iPhone 上的免費與 Pro', '方向鍵、確定、返回、首頁、音量、頻道、數字鍵、鍵盤、開啟 App、切換輸入來源與開關機都是免費的，沒有廣告，也不需訂閱。Mando TV Pro 是選購的一次買斷方案，提供額外功能，直接在 App 內購買。'),
    ],
    marca=None,
    faq=[
      ('Mando TV 在 iPhone 上免費嗎？', '下載是免費的，沒有廣告。基本遙控器免費，開啟 App 與切換輸入來源也是免費的。額外功能屬於 Mando TV Pro，這是選購的一次買斷方案。'),
      ('可以在 iPad 上使用嗎？', '可以。同一個 App 可在 iPhone 與 iPad 上運作。'),
      ('iPhone 的遙控器 App 需要藍牙或紅外線發射器嗎？', 'iPhone 不需要。iPhone 沒有紅外線發射器，所以無法使用紅外線控制，而藍牙選項只適用於 Android 9 以上，不適用於 iPhone。在 iPhone 上，Mando TV 透過你家中的 Wi-Fi 控制智慧電視，以及 Apple TV（測試版）。'),
    ]),
  dict(clave='firetv', corto='Fire TV 遙控器', fecha='2026-11-23',
    titulo='Fire TV 遙控器 App：手機與電腦都能用',
    desc='手機上的 Fire TV 遙控器：用 Wi-Fi 控制 Fire TV Stick、Fire TV Cube 或內建 Fire TV 的電視，以 4 位數 PIN 配對。不需 Amazon App。',
    h1='手機或電腦的 Fire TV 遙控器',
    intro='如果 Fire TV 遙控器不見了或電池沒電了，Mando TV 可以透過 Wi-Fi 控制 Fire TV Stick、Fire TV Cube 或內建 Fire TV 的電視。配對使用 4 位數 PIN。Fire TV 是 Mando TV 的新功能，所以請先更新 App。',
    pasos=[
      '從 App Store、Microsoft Store 或 Google Play 把 Mando TV 更新到最新版本。',
      '開啟 Fire TV，並把手機連上同一個 Wi-Fi。',
      '開啟 Mando TV。你的 Fire TV 會出現在清單中，點選它即可。',
      '電視畫面上會出現 4 位數的 PIN。在 Mando TV 中輸入。你只需要做一次。',
      '使用方向鍵、確定、返回、首頁、播放按鍵，以及用於搜尋的鍵盤。',
    ],
    extra=[
      ('支援的 Fire TV 裝置', 'Fire TV Stick、Fire TV Stick 4K、Fire TV Cube，以及內建 Fire TV 的電視。這項支援是新推出的，到目前為止我們只在少數真實裝置上測試過。如果有任何地方不如預期，請透過說明頁面告訴我們你的型號。'),
      ('開啟 Fire TV', 'Mando TV 無法透過網路開啟 Fire TV。請用電視機身上的電源按鍵開機：接上的 Fire TV Stick 或 Cube 通常會透過 HDMI-CEC 一起喚醒，而內建 Fire TV 的電視，電視本身就是 Fire TV。之後就可以用手機控制。'),
      ('如果找不到你的 Fire TV', '請確認兩個裝置在同一個 Wi-Fi，且 Fire TV 已喚醒。在 iPhone 上，請在設定中允許 Mando TV 使用「區域網路」。請參考[手機找不到電視](@not-found)。'),
      ('完全沒有遙控器？', 'Fire TV 必須在畫面上顯示 PIN，所以電視與 Fire TV 都必須開著並顯示畫面。如果電視停在錯誤的輸入來源，請用電視機身上的按鍵切換。請參考[沒有遙控器切換輸入](@hdmi)。'),
      ('免費與 Pro', '方向鍵、確定、返回、首頁、音量、頻道、數字、鍵盤、開啟 App、切換輸入來源與開關機都是免費的，沒有廣告，也不需訂閱。Mando TV Pro 是選購的一次買斷方案，提供額外功能。'),
    ],
    marca=None,
    faq=[
      ('我需要 Amazon Fire TV App 嗎？', '不需要。Mando TV 透過你的 Wi-Fi，以 PIN 連到 Fire TV。你的手機上不需要 Amazon 帳號。'),
      ('支援內建 Fire TV 的電視與 Fire TV Stick 嗎？', '支援，這正是它的設計用途。這項支援是新推出的，請保持 App 為最新版本，並告訴我們哪些機型沒有如預期運作。'),
      ('為什麼我需要 PIN？', 'Fire TV 會顯示 4 位數的 PIN，以證明你就在電視前。沒有人能在看不到畫面的情況下完成配對。'),
    ]),
  dict(clave='firetv-lost', corto='Fire TV 遙控器不見了', fecha='2026-11-23',
    titulo='Fire TV 遙控器不見了？手機可以幫你',
    desc='Fire TV Stick 遙控器不見了？用手機透過 Wi-Fi 控制，以 4 位數 PIN 配對。附新 Wi-Fi 與 HDMI-CEC 的小技巧。',
    h1='Fire TV 遙控器不見了：用手機控制',
    intro='如果你的 Fire TV Stick、Fire TV Cube 或內建 Fire TV 的智慧電視遙控器不見了或不能用了，只要 Fire TV 仍連著你的 Wi-Fi，手機就能接手控制。配對是透過畫面上的 4 位數 PIN，所以你完全不需要舊遙控器。',
    pasos=[
      '用電視機身上的按鍵開機。接上的 Fire TV Stick 或 Cube 通常會一起喚醒；如果啟用了 HDMI-CEC，電視常會自動切換到它的輸入。',
      '如果電視顯示其他輸入來源，請用電視上的輸入或訊號源按鍵切換。請參考[沒有遙控器切換輸入](@hdmi)。',
      '把手機連上與 Fire TV 相同的 Wi-Fi。',
      '下載並開啟 Mando TV。你的 Fire TV 會出現在清單中，點選它即可。',
      '電視會顯示 4 位數的 PIN。在 Mando TV 中輸入。你只需要做一次。',
      '在手機上使用方向鍵、確定、返回、首頁、音量、播放按鍵與鍵盤。',
    ],
    extra=[
      ('先試試電視遙控器（HDMI-CEC）', '許多電視遙控器可以透過 HDMI-CEC 控制 Fire TV Stick。如果看得到 Fire TV 介面，請在電視遙控器上按方向鍵與確定。如果沒有反應，請在電視設定中啟用 CEC（Samsung 是 Anynet+，LG 是 SIMPLINK，Sony 是 BRAVIA Sync），並在 Fire TV 的顯示設定（「Display & Sounds」）中啟用 HDMI-CEC 裝置控制。'),
      ('如果你換了 Wi-Fi', '沒有遙控器，你就無法在 Fire TV 上輸入新的 Wi-Fi 密碼，但有個辦法：用第二支手機建立一個熱點，名稱與密碼和你舊的 Wi-Fi 完全相同。Fire TV 會自動連上它。讓裝有 Mando TV 的手機連上這個熱點，以 PIN 配對，然後在 Fire TV 上前往「設定 > 網路」，並選擇你的新 Wi-Fi。最後，也把你的手機連上新的 Wi-Fi。'),
      ('配對替換用的遙控器', '大多數新的 Fire TV 遙控器，只要在 Fire TV 附近按住首頁鍵約 10 秒即可配對。如果沒有成功，請開啟「設定 > 控制器與藍牙裝置 > Amazon Fire TV 遙控器 > 新增遙控器」。你也可以用裝有 Mando TV 的手機進入這個選單。'),
      ('內建 Fire TV 的電視', '對於內建 Fire TV 的電視，步驟相同，因為電視本身就是 Fire TV。'),
      ('開始之前', 'Fire TV 支援是 Mando TV 的新功能。請先更新 App。如果你的機型沒有如預期運作，請透過[說明頁面](@soporte)寫信給我們，並告訴我們機型。'),
      ('免費與 Pro', '遙控器可以免費下載與使用，沒有廣告，也不需訂閱。Mando TV Pro 是選購的一次買斷方案，提供額外功能。'),
    ],
    marca=('firetv', 'Fire TV 遙控器'),
    faq=[
      ('沒有遙控器，我也能用手機控制 Fire TV Stick 嗎？', '可以，只要 Fire TV 開著並連上你的 Wi-Fi。Mando TV 透過電視上的 4 位數 PIN 配對，所以你不需要舊遙控器。'),
      ('如果 Fire TV 在新的 Wi-Fi 上還能用嗎？', '不能直接使用，因為手機與 Fire TV 必須在同一個網路。請先用本頁的熱點技巧，讓 Fire TV 重新連上網路。'),
      ('我需要 Amazon Fire TV App 或 Amazon 帳號嗎？', '不需要。Mando TV 透過你的家用網路，以 PIN 連線，也不需要自己的帳號。'),
    ]),
  dict(clave='turn-on', corto='沒有遙控器開電視', fecha='2026-11-23',
    titulo='沒有遙控器怎麼開電視（所有品牌）',
    desc='沒有遙控器怎麼開電視：Samsung、LG、TCL、Hisense 與 Sony 的電源鍵在哪裡。另附 HDMI-CEC 與手機的小技巧。',
    h1='沒有遙控器，如何開電視',
    intro='幾乎每台電視都還有一個實體的電源鍵，只是藏得很好。這裡告訴你各品牌的電源鍵在哪裡，另外還有兩個讓你下次不必再找的辦法：從遊戲機或串流裝置透過 HDMI-CEC，以及用手機透過 Wi-Fi 開電視。',
    pasos=[
      '看看螢幕正下方的中央，就在品牌標誌後面。許多電視在那裡有一個小小的單一按鍵或搖桿，朝下。',
      '如果不在那裡，請沿著電視背面靠近下方兩個角落摸索，再找左右兩側邊緣。',
      '按一下按鍵。許多只有一個按鍵的電視，在開機狀態下短按會開啟輸入來源與音量的小選單，長按則會關機。',
      '還是沒反應？請檢查電源線兩端，並換一個插座。如果待機燈沒亮，表示電視沒有通電。',
      '電視開機後，請把它設定成不再需要這個按鍵：啟用 HDMI-CEC 與透過網路開機，下方都有說明。',
    ],
    extra=[
      ('各品牌電源鍵的位置', 'Samsung：螢幕正下方中央的控制按鍵或搖桿，或背面下方的角落。LG：大多數機型在 LG 標誌下方有一個搖桿按鍵。TCL 與 Hisense：通常是螢幕正下方中央的小按鍵，或背面靠近下方角落。Sony：在背面或側邊邊緣，靠近邊緣的下方。位置依機型而異。如果找不到，請用背面貼紙上的型號搜尋使用說明書。'),
      ('用遊戲機或串流裝置開電視（HDMI-CEC）', '啟用 HDMI-CEC 後，開啟 PlayStation、Xbox、Roku 播放器、Fire TV Stick 或 Chromecast 時，也會開啟電視並切換到正確的輸入。每個品牌對這項設定的稱呼不同：Samsung 是 Anynet+，LG 是 SIMPLINK，Sony 是 BRAVIA Sync，大多數其他品牌稱為 CEC。更多資訊請見[沒有遙控器也能開電視並切換到遊戲機的 HDMI](@console)。'),
      ('用手機開電視', '只要你允許一次，智慧電視就能透過 Wi-Fi 喚醒，之後 Mando TV 就能從手機開啟它。Samsung 請在「設定 > 一般 > 網路 > 專家設定」啟用「以行動裝置開機」。LG 請啟用「以行動裝置開啟電視」（[步驟說明](@lg-on)）。Roku 電視請在「設定 > 系統 > 電源」啟用「電視快速啟動」。Google TV 與 Android TV，如果你的機型有這個功能，請尋找 Wake on LAN 或「透過網路開機」。你只需要在電視開機時設定一次。'),
      ('如果你找不到按鍵', '有些較新的電視把唯一的按鍵藏得非常好，讓人覺得好像根本沒有。請在螢幕下方尋找一個小小的凸起或光感應區：按鍵常常就在旁邊。透過 Wi-Fi 時，Mando TV 需要電視曾經開機並已連線。紅外線是例外：在有紅外線發射器的 Android 手機上，只要把手機對準電視，Mando TV 就能開啟一台從未設定過的電視。紅外線是新功能，適用於 App 代碼清單中的品牌。'),
      ('免費與 Pro', '遙控器可以免費下載與使用，沒有廣告，也不需訂閱。Mando TV Pro 是選購的一次買斷方案，提供額外功能。'),
    ],
    marca=None,
    faq=[
      ('我從沒設定過電視，可以用手機開電視嗎？', '無法透過 Wi-Fi。關機的電視只有在事先啟用透過網路開機時，才能被網路喚醒。第一次請用電視上的按鍵。例外是有紅外線發射器的 Android 手機：如果品牌在代碼清單中，或你選擇「其他品牌或不知道」，Mando TV 可以用紅外線開啟尚未設定的電視。'),
      ('沒有遙控器要怎麼開 Samsung 電視？', '按下螢幕正下方中央或背面下方角落的控制按鍵。然後啟用「以行動裝置開機」，下次就能用手機開機。'),
      ('沒有遙控器要怎麼開 Roku 電視？', '使用電視上的按鍵，通常在正下方中央或背面。然後在「設定 > 系統 > 電源」啟用「電視快速啟動」，讓 Mando TV 可以從手機開啟電視。'),
      ('為什麼我開遊戲機時，電視會自動開機？', '這是 HDMI-CEC。它很方便，如果你不喜歡，可以在電視設定中關閉。'),
    ]),
  dict(clave='sony', corto='Sony 遙控器', fecha='2026-11-23',
    titulo='Sony 電視遙控器 App：手機與電腦都能用',
    desc='Mando TV 透過 Wi-Fi 控制搭載 Google TV 或 Android TV 的 Sony Bravia 電視。測試版支援 2013 至 2015 年、不含 Android 的機型。',
    h1='如何用手機控制你的 Sony 電視',
    intro='較新的 Sony Bravia 智慧電視使用 Google TV，2015 年起的較舊機型使用 Android TV。Mando TV 可以透過你的 Wi-Fi，從 iPhone、Android 手機或 Windows 電腦控制這兩種電視。當原廠遙控器不見了或電池沒電時，這個 App 可以取代它。',
    pasos=[
      '確認你的 Sony 電視顯示的是 Google TV 或 Android TV 主畫面。2015 年起的大多數 Sony Bravia 智慧電視都是如此。',
      '把手機與電視連上同一個 Wi-Fi。',
      '開啟 Mando TV，並在清單中點選你的 Sony 電視。',
      '輸入電視畫面上顯示的 6 個字元代碼（只需要第一次）。這個步驟不需要遙控器。',
      '使用方向鍵、確定、返回、首頁、音量與鍵盤。',
    ],
    extra=[
      ('用手機開啟 Sony 電視', '搭載 Google TV 或 Android TV 的 Sony 機型，只要啟用了「Remote start」，就可以透過網路喚醒。這個選項通常位於「設定 > 網路與網際網路 > Remote start」（路徑可能依機型略有不同）。接著在電視關機時，於 Mando TV 點選電視，App 就會開啟它。'),
      ('Sony 的電源鍵在哪裡', '大多數 Bravia 電視的電源鍵在背面，靠近左下或右下的角落，或在側邊邊緣。短按一下即可開機。更多資訊請見[沒有遙控器怎麼開電視](@turn-on)。'),
      ('較舊的 Sony 電視', '2013 至 2015 年、不使用 Android 的 Sony Bravia 電視，在 Mando TV 中以測試版支援。這是新功能，可能還有不完善的地方。電視會顯示一個 4 位數的 PIN，你需要在 App 中輸入。其他沒有 Google TV 或 Android TV 的 Sony 電視，目前不支援。'),
      ('免費與 Pro', '遙控器可以免費下載與使用，沒有廣告，也不需訂閱。Mando TV Pro 是選購的一次買斷方案，提供額外功能。'),
    ],
    marca='android',
    faq=[
      ('Mando TV 支援 Sony Bravia 電視嗎？', '支援，適用於使用 Google TV 或 Android TV 的 Sony 電視。這涵蓋 2015 年起的大多數 Sony 智慧電視。'),
      ('我需要 Sony 的 App 或 Google 帳號嗎？', '不需要。Mando TV 以電視畫面上的代碼配對，不需要帳號。'),
      ('支援較舊、沒有 Android 的 Sony Bravia 電視嗎？', '支援，為測試版，適用於 2013 至 2015 年、沒有 Android 的 Bravia 機型。配對使用電視顯示的 4 位數 PIN。'),
      ('可以用手機在我的 Sony 電視上輸入文字嗎？', '可以。鍵盤是免費的，可用於 YouTube、Netflix 與電視搜尋。'),
    ]),
  dict(clave='tcl', corto='TCL 遙控器', fecha='2026-11-23',
    titulo='TCL 電視遙控器 App：手機與電腦都能用',
    desc='TCL 遙控器不見了？大多數 TCL 電視使用 Roku TV 或 Google TV。Mando TV 透過 Wi-Fi 控制這兩者，不需帳號，沒有廣告。',
    h1='如何用手機控制你的 TCL 電視',
    intro='TCL 製造電視，但軟體是 Roku TV 或 Google TV（較舊的機型則是 Android TV）。Mando TV 能控制這兩種系統，透過 Wi-Fi 當你 TCL 電視的遙控器。免費，不需帳號，沒有廣告。',
    pasos=[
      '先確認你的 TCL 使用哪種系統。如果主畫面是由頻道圖塊組成的簡單格狀排列，就是 Roku TV。如果看起來像 Google TV 或 Android TV，有一排排推薦內容，就是 Google TV。',
      '把手機與 TCL 電視連上同一個 Wi-Fi。',
      '開啟 Mando TV。TCL 會自動出現在清單中，點選它即可。',
      '使用 Roku TV 的 TCL 不需要其他操作。使用 Google TV 的 TCL 則要輸入電視畫面上顯示的 6 個字元代碼（只需要第一次）。',
      '使用方向鍵、確定、返回、首頁、音量與鍵盤。如果你已啟用透過網路開機，也可以用 App 開電視（見下方）。',
    ],
    extra=[
      ('用手機開啟 TCL 電視', 'TCL Roku TV 請在「設定 > 系統 > 電源」啟用「電視快速啟動」。TCL Google TV 請在網路或電源設定中尋找 Wake on LAN、「透過網路開機」或遠端啟動的選項。有些機型沒有這項功能。這時請用實體電源鍵開機，通常在正下方中央或背面。'),
      ('如果找不到你的 TCL', '請確認手機與電視在同一個 Wi-Fi。把 2.4 GHz 與 5 GHz 分開的路由器，可能會讓裝置彼此看不到。在 iPhone 上，請在設定中允許 Mando TV 使用「區域網路」。你也可以輸入電視的 IP 位址來新增。請閱讀[手機找不到電視](@not-found)。'),
      ('更多關於你的 TCL', '使用 Roku TV 的 TCL，請參考[Roku 遙控器 App](@roku)；使用 Google TV 或 Android TV 的 TCL，請參考[Android TV 遙控器 App](@android)。'),
      ('免費與 Pro', '方向鍵、確定、返回、首頁、音量、頻道、數字、鍵盤、開啟 App、切換輸入來源與開關機都是免費的，沒有廣告，也不需訂閱。Mando TV Pro 是選購的一次買斷方案，提供額外功能。'),
    ],
    marca=None,
    faq=[
      ('Mando TV 支援每一台 TCL 電視嗎？', '支援使用 Roku TV、Google TV 或 Android TV 的 TCL 電視，也就是大多數 TCL 智慧電視。不是智慧電視的 TCL，無法透過 Wi-Fi 控制。'),
      ('我需要 TCL App 或 TCL 帳號嗎？', '不需要。Mando TV 直接透過你家中的 Wi-Fi 連線，不需要帳號。'),
      ('我的 TCL 要求輸入代碼。代碼在哪裡？', '使用 Google TV 與 Android TV 的 TCL 機型，會在畫面上顯示 6 個字元的代碼。請照著原樣在 Mando TV 中輸入。使用 Roku TV 的 TCL 不會要求代碼。'),
    ]),
  dict(clave='hisense', corto='Hisense 遙控器', fecha='2026-11-23',
    titulo='Hisense 遙控器 App：手機上能用什麼',
    desc='用 Mando TV 當 Hisense 遙控器：透過 Wi-Fi 控制 VIDAA、Roku TV、Google TV 與 Fire TV。誠實說明哪些可以用。',
    h1='Hisense 遙控器 App：哪些可以用，哪些不行',
    intro='Hisense 電視的內部系統並不全都一樣。依機型，它們使用 Hisense 自家的 VIDAA 系統、Roku TV、Google TV 或 Fire TV。Mando TV 可以當這四種系統 Hisense 電視的遙控器，只有部分較新的 VIDAA 機型例外。這裡告訴你如何辨別自己用的是哪一種，以及可以預期什麼。',
    pasos=[
      '確認你的 Hisense 使用哪種系統。VIDAA 是 Hisense 自己的介面。Roku TV 顯示頻道圖塊的格狀排列。Google TV 顯示一排排推薦內容。Fire TV 顯示有 Amazon 內容排的 Fire TV 主畫面。',
      '把手機與 Hisense 電視連上同一個 Wi-Fi。',
      '開啟 Mando TV。電視會自動出現在清單中，點選它即可。',
      'VIDAA 與 Fire TV 機型可能會顯示 4 位數的 PIN；Google TV 則會顯示 6 個字元的代碼。請在 App 中輸入。Roku TV 什麼都不會問。你只需要做一次。',
      '用手機使用方向鍵、確定、返回、首頁、音量與鍵盤。',
    ],
    extra=[
      ('使用 Roku TV 或 Google TV 的 Hisense', '它們的運作方式和其他任何 Roku 或 Google TV 電視完全一樣。詳情請見[Roku 遙控器 App](@roku)與[Android TV 遙控器 App](@android)頁面。'),
      ('使用 Fire TV 的 Hisense', 'Fire TV 支援是 Mando TV 的新功能。請把 App 更新到商店中的最新版本。PIN 配對的運作方式，請見[Fire TV 遙控器 App](@firetv)頁面。如果有任何地方不如預期，請透過說明頁面寫信給我們，並告訴我們你的型號。'),
      ('使用 VIDAA 的 Hisense', '大多數 VIDAA 機型都能用：按鍵、音量、鍵盤、App 與輸入來源。部分較新的 VIDAA 機型只接受官方的 Hisense App。Mando TV 會在連線時偵測到這一點，並清楚告訴你，而不是默默失敗。這種情況下，適用於你機型的 Hisense App、電視上的按鍵或原廠遙控器，才是正確的做法。'),
      ('用手機開啟 Hisense', 'Hisense Roku TV 請在「設定 > 系統 > 電源」啟用「電視快速啟動」。Google TV 請尋找 Wake on LAN 或「透過網路開機」的選項。如果沒有，請使用電視上的電源鍵。'),
      ('免費與 Pro', '方向鍵、確定、返回、首頁、音量、頻道、數字鍵、鍵盤、開啟 App、切換輸入來源與開關機都是免費的，沒有廣告，也不需訂閱。Mando TV Pro 是選購的一次買斷方案，提供額外功能。'),
    ],
    marca=None,
    faq=[
      ('Mando TV 支援 Hisense VIDAA 嗎？', '支援，適用於大多數 VIDAA 機型。部分較新的機型只接受官方 Hisense App；Mando TV 會偵測到並告訴你。使用 Roku TV、Google TV 或 Fire TV 的 Hisense 電視也都支援。'),
      ('我怎麼知道我的 Hisense 是 Roku TV、Google TV 還是 Fire TV？', '看一下主畫面。Roku TV 有簡單的圖塊格狀排列，開機時會出現 Roku 標誌。Google TV 有一排排推薦內容。Fire TV 則是 Amazon Fire TV 的主畫面。「設定 > 關於」下的機型名稱也能告訴你。'),
      ('我需要 Hisense 或 Google 帳號嗎？', '不需要。Mando TV 直接透過你家中的 Wi-Fi 連線，沒有自己的帳號。'),
    ]),
  dict(clave='philips', corto='Philips 遙控器', fecha='2026-11-23',
    titulo='Philips 遙控器 App：Roku TV、Google TV、Android TV',
    desc='Mando TV 透過 Wi-Fi，從手機或電腦控制搭載 Roku TV、Google TV 或 Android TV 的 Philips 電視。不支援 Titan OS。',
    h1='用手機控制 Philips 電視',
    intro='Philips 電視依國家與年份使用不同系統：美國是 Roku TV，許多國家是 Google TV 或 Android TV，部分較新的歐洲機型則是 Titan OS。Mando TV 透過 Wi-Fi 控制搭載 Roku TV、Google TV 與 Android TV 的機型。',
    pasos=[
      '確認主畫面。Roku TV 顯示圖塊的格狀排列。Google TV 與 Android TV 顯示來自 Google 的一排排推薦內容。Titan OS 有自己的主畫面。',
      '把手機與電視連上同一個 Wi-Fi。',
      '開啟 Mando TV，並在清單中點選你的 Philips 電視。',
      'Roku TV 什麼都不會問。Google TV 與 Android TV 會顯示 6 個字元的代碼：請在 App 中輸入一次。',
      '使用方向鍵、確定、返回、首頁、音量與鍵盤。',
    ],
    extra=[
      ('Philips Roku TV', '運作方式和其他任何 Roku 電視一樣。想用手機開機，請在「設定 > 系統 > 電源」啟用「電視快速啟動」。更多資訊請見[Roku 遙控器 App](@roku)頁面。'),
      ('使用 Google TV 或 Android TV 的 Philips', '包含許多 Ambilight 機型。它們以畫面上的代碼配對。想用手機開機，請在網路或電源設定中尋找 Wake on LAN 或「透過網路開機」。部分機型沒有這個選項。更多資訊請見[Android TV 遙控器 App](@android)頁面。'),
      ('較舊、沒有 Android 的 Philips 電視', '2011 至 2015 年、不使用 Android 的 Philips 電視，在 Mando TV 的測試版中支援。這是新功能，而且不需要配對碼。'),
      ('使用 Titan OS 的 Philips', 'Titan OS 是另一種系統，Mando TV 目前無法控制，我們寧可直接說清楚。較新、沒有 Android 的 Philips 機型也不在支援範圍內。'),
      ('免費與 Pro', '遙控器可以免費下載與使用，沒有廣告，也不需訂閱。Mando TV Pro 是選購的一次買斷方案，提供額外功能。'),
    ],
    marca=None,
    faq=[
      ('Mando TV 支援 Philips 電視嗎？', '支援使用 Roku TV、Google TV 或 Android TV 的 Philips 電視，以及測試版中 2011 至 2015 年、沒有 Android 的 Philips 電視。不支援使用 Titan OS 的機型。'),
      ('Mando TV 能控制 Ambilight 嗎？', 'Mando TV 是遙控器：它會傳送按鍵，所以你可以用方向鍵與確定進入 Ambilight 設定。沒有另外獨立的 Ambilight 控制。'),
      ('我需要 Philips 或 Google 帳號嗎？', '不需要。Mando TV 透過你家中的 Wi-Fi 連線，不需要帳號。'),
    ]),
]
OTRAS_GUIAS += [
  ('no-sub', '免訂閱、無廣告的遙控器 App'),
  ('roku-app-alt', 'Roku App 的替代方案：一個 App 控制所有電視'),
  ('lg-thinq', '你的 LG 電視可用的 LG ThinQ App 替代方案'),
  ('smartthings', 'Samsung 電視的 SmartThings 替代方案'),
  ('googletv-alt', '手機版 Google TV 遙控器的替代方案'),
  ('windows', 'Windows 電腦的遙控器 App'),
  ('iphone', 'iPhone 遙控器 App：一個 App 控制所有電視'),
  ('firetv', '手機或電腦的 Fire TV 遙控器'),
  ('firetv-lost', 'Fire TV 遙控器不見了：用手機控制'),
  ('turn-on', '沒有遙控器，如何開電視'),
  ('sony', '如何用手機控制你的 Sony 電視'),
  ('tcl', '如何用手機控制你的 TCL 電視'),
  ('hisense', 'Hisense 遙控器 App：哪些可以用，哪些不行'),
  ('philips', '用手機控制 Philips 電視'),
]
# <<< guías traídas del inglés
