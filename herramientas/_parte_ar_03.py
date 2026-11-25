SOPORTE = dict(
  titulo='المساعدة: ربط التلفزيون بـ Mando TV وتشغيله',
  desc='كيف تربط ريموت Mando TV بتلفزيون LG أو Samsung أو Roku أو Android TV، وتشغّل التلفزيون من الجوال وتحل المشكلات.',
  h1='المساعدة',
  intro='أكثر الأسئلة شيوعًا، بترتيب الخطوات. إذا لم تجد سؤالك، فراسلنا على <a href="mailto:hola@mandotv.app?subject=Help%20with%20Mando%20TV">hola@mandotv.app</a> وسنرد عليك.',
)
SOPORTE_HTML = '''      <h2 id="encontrar">العثور على التلفزيون</h2>
      <div class="preguntas">
        <details open><summary>تلفزيوني لا يظهر في القائمة</summary>
          <ol>
            <li>تأكد من أن جوالك والتلفزيون على شبكة Wi-Fi نفسها. إذا كان في الراوتر شبكتان، 2.4 جيجاهرتز و5 جيجاهرتز، بأسمين مختلفين، فأحيانًا لا ترى الأجهزة بعضها.</li>
            <li>تأكد من أن التلفزيون يعمل.</li>
            <li>في iPhone تأكد من أن Mando TV لديه إذن "الشبكة المحلية"، من الإعدادات ثم Mando TV.</li>
            <li>اضغط في قائمة التلفزيونات على الزر الخاص بالحالة التي لا يظهر فيها تلفزيونك: يفحص التطبيق الأسباب الأكثر شيوعًا خطوة بخطوة (شبكة Wi-Fi نفسها، وVPN، وإذن الشبكة المحلية وغيرها) ويعرض بعد كل إصلاح زرًا لإعادة الفحص.</li>
            <li>وإذا لم يظهر بعد، فاضغط على الزر +، واختر العلامة، واكتب عنوان IP الخاص بالتلفزيون. تجده في قائمة الشبكة في التلفزيون (مثلًا 192.168.1.50).</li>
          </ol>
        </details>
        <details><summary>هل يعمل ببيانات الجوال أو وأنا خارج المنزل؟</summary>
          <p>لا. يتحدث Mando TV مع التلفزيون داخل شبكة منزلك، لذلك يجب أن يكون جوالك متصلًا بشبكة Wi-Fi هذه.</p>
        </details>
      </div>

      <h2 id="conectar">الاتصال لأول مرة</h2>
      <p>أدلة كاملة حسب العلامة: <a href="@@R_lg@@">LG</a> و<a href="@@R_samsung@@">Samsung</a> و<a href="@@R_roku@@">Roku</a> و<a href="@@R_android@@">Android TV</a>.</p>
      <div class="preguntas">
        <details><summary>LG</summary>
          <p>عندما تضغط على التلفزيون، تظهر على الشاشة رسالة تطلب الإذن. وافق عليها بالريموت المعتاد. تفعل ذلك مرة واحدة فقط.</p>
        </details>
        <details><summary>Samsung</summary>
          <p>سيسألك التلفزيون إن كنت تسمح باتصال Mando TV. اختر "Allow" بالريموت. وإذا رفضته بالخطأ، فافتح الإعدادات > General > External Device Manager > Device Connection Manager وغيّره إلى مسموح.</p>
        </details>
        <details><summary>Roku</summary>
          <p>لا يطلب Roku إذنًا. وإذا لم ينجح الاتصال، ففي Roku افتح الإعدادات > System > Advanced system settings > Control by mobile apps واترك Network access على Default أو Enabled.</p>
        </details>
        <details><summary>Android TV وGoogle TV</summary>
          <p>يعرض التلفزيون رمزًا من 6 خانات. اكتبه في Mando TV تمامًا كما يظهر. يعمل مع Sony وPhilips وTCL وHisense وSharp وXiaomi وChromecast with Google TV وغيرها بنظام Android TV.</p>
        </details>
      </div>

      <h2 id="encender">تشغيل التلفزيون من التطبيق</h2>
      <p>يشغّل Mando TV التلفزيون عبر شبكة منزلك. ولذلك يلزم أمران: أن تكون قد اتصلت مرة واحدة على الأقل والتلفزيون يعمل، وأن يكون التشغيل عبر الشبكة مفعّلًا في التلفزيون. يختلف اسم الإعداد حسب الطراز؛ هذه أشهر الأسماء:</p>
      <div class="preguntas">
        <details><summary>LG</summary>
          <p>ابحث في الإعدادات (حسب الطراز في General أو Connection) عن "Turn on TV with Mobile" وفعّل "Turn on via Wi-Fi". وإذا كان الخيار "Quick Start+" موجودًا، ففعّله أيضًا.</p>
        </details>
        <details><summary>Samsung</summary>
          <p>فعّل "Power On with Mobile" من الإعدادات > General > Network > Expert Settings.</p>
        </details>
        <details><summary>Roku</summary>
          <p>في أجهزة Roku TV، فعّل "Fast TV start" من الإعدادات > System > Power. مشغلات Roku الموصولة بتلفزيون لا يمكن تشغيلها بهذه الطريقة.</p>
        </details>
        <details><summary>Android TV وGoogle TV</summary>
          <p>يعتمد ذلك على الشركة المصنّعة. ابحث في إعدادات الشبكة أو الطاقة عن "Wake on LAN" أو "Wake on network" أو "Network standby". بعض الطرازات لا تحتوي على هذا الخيار.</p>
        </details>
      </div>

      <h2 id="falla">إذا لم يعمل شيء</h2>
      <div class="preguntas">
        <details><summary>ينقطع الاتصال أو لا توجد استجابة</summary>
          <ol>
            <li>اضغط في شاشة الريموت على إعادة الاتصال.</li>
            <li>وإذا لم يفد ذلك، فأغلق Mando TV وافتح التطبيق من جديد.</li>
            <li>وإذا حصل التلفزيون على عنوان IP آخر، فاحذفه من القائمة وأضفه من جديد.</li>
          </ol>
        </details>
        <details><summary>كيف ترسل لنا تقريرًا بالخطأ</summary>
          <ol>
            <li>اضغط في Mando TV على زر التخصيص (أشرطة التمرير في الأعلى).</li>
            <li>اضغط على نسخ تقرير الاختبار.</li>
            <li>الصقه في رسالة بريد إلكتروني إلى hola@mandotv.app مع علامة تلفزيونك وطرازه.</li>
          </ol>
          <p>لا يحتوي التقرير على كلمات مرور ولا رموز ولا أي شيء تكتبه.</p>
        </details>
        <details><summary>اشتريت Pro ولا يظهر</summary>
          <p>اضغط في التخصيص على استعادة الشراء، بحساب المتجر نفسه الذي اشتريت به. وإذا لم يظهر بعد، فراسلنا.</p>
        </details>
      </div>

      <h2 id="guias">أدلة خطوة بخطوة</h2>
      <p><a href="@@R_guias@@">عرض كل الأدلة</a></p>
      <ul>
@@GUIAS@@
      </ul>

      <h2 id="contacto">لا تزال لديك أسئلة؟</h2>
      <p>راسلنا على <a href="mailto:hola@mandotv.app?subject=Help%20with%20Mando%20TV">hola@mandotv.app</a>. أخبرنا بعلامة تلفزيونك وطرازه وفي أي خطوة توقفت. اكتب لنا بلغتك. نرد بالإسبانية أو الإنجليزية، وبلغتك إن أردت بمساعدة مترجم.</p>
'''

