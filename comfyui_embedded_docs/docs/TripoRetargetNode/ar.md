# Tripo: إعادة توجيه النموذج المجهز

يطبّق TripoRetargetNode حركة جاهزة على نموذج ثلاثي الأبعاد موجود ومُجهّز بهيكل عظمي. يأخذ معرّف المهمة لنموذج تم تجهيزه بهيكل عظمي سابقًا، ويرسل طلب إعادة استهداف إلى Tripo API، ثم ينزّل ملف الحركة الناتج. يمكن إرجاع النموذج المتحرك بصيغة GLB أو FBX، مع هندسة شبكية اختيارية وتشغيل اختياري في المكان.

## المدخلات

| المعامل | الوصف | نوع البيانات | مطلوب | النطاق |
|-----------|-------------|-----------|----------|-------|
| `original_model_task_id` | معرّف المهمة للنموذج ثلاثي الأبعاد المُجهّز بهيكل عظمي سابقًا والمطلوب إعادة استهدافه. يجب أن تكون المهمة المرجعية مهمة تجهيز هيكل (rig). | RIG_TASK_ID | نعم | - |
| `animation` | الحركة الجاهزة المطلوب تطبيقها على النموذج المُجهّز بهيكل عظمي. تعمل حركات `preset:*` مع كلا نموذجي rig. حركات `preset:biped:*` مصممة لهياكل من الإصدار v1.0-20240301؛ ولا يقبل هيكل v2.5 سوى chop وclimb وdive وfall وhurt وidle وjump وrun وshoot وslash وturn وwalk. | COMBO | نعم | `"preset:idle"`<br>`"preset:walk"`<br>`"preset:run"`<br>`"preset:dive"`<br>`"preset:climb"`<br>`"preset:jump"`<br>`"preset:slash"`<br>`"preset:shoot"`<br>`"preset:hurt"`<br>`"preset:fall"`<br>`"preset:turn"`<br>`"preset:quadruped:walk"`<br>`"preset:hexapod:walk"`<br>`"preset:octopod:walk"`<br>`"preset:serpentine:march"`<br>`"preset:aquatic:march"`<br>بالإضافة إلى خيارات إضافية `"preset:biped:*"` تظهر في الواجهة |
| `out_format` | صيغة ملف الإخراج؛ تصل النتيجة إلى المخرج المطابق. (الافتراضي: glb) | COMBO | لا | `"glb"`<br>`"fbx"` |
| `export_with_geometry` | تضمين الشبكة في التصدير؛ عند إيقافه، يُصدَّر الهيكل العظمي المتحرك فقط. (الافتراضي: True) | BOOLEAN | لا | True<br>False |
| `animate_in_place` | تشغيل الحركة في المكان، دون إزاحة الجذر. (الافتراضي: False) | BOOLEAN | لا | True<br>False |
| `auth_token_comfy_org` | رمز مصادقة للوصول إلى Comfy.org API (معامل مخفي). | AUTH_TOKEN_COMFY_ORG | لا | - |
| `api_key_comfy_org` | مفتاح API للوصول إلى خدمة Comfy.org (معامل مخفي). | API_KEY_COMFY_ORG | لا | - |
| `unique_id` | معرّف فريد لتتبع العملية (معامل مخفي). | UNIQUE_ID | لا | - |

ملاحظة: تعمل الحركات في مجموعة `preset:*` مع كلا نموذجي rig. الحركات في مجموعة `preset:biped:*` مصممة لهياكل من الإصدار v1.0-20240301؛ ولا يقبل هيكل v2.5 سوى chop وclimb وdive وfall وhurt وidle وjump وrun وshoot وslash وturn وwalk. إذا أُنشئ الهيكل المرجعي وفق مواصفات Mixamo وإصدار نموذج يبدأ بـ `v1.0`، يفشل استدعاء إعادة الاستهداف بخطأ. يجب أن تكون صيغة الإخراج المطلوبة GLB أو FBX؛ وإذا أعادت الخدمة أي نوع ملف آخر، تُطلق العقدة خطأً.

## المخرجات

| اسم المخرج | الوصف | نوع البيانات |
|-------------|-------------|-----------|
| `model_file` | ملف نموذج ثلاثي الأبعاد متحرك تم إنشاؤه (للتوافق مع الإصدارات السابقة فقط). | STRING |
| `retarget task_id` | معرّف المهمة لتتبع عملية إعادة الاستهداف. | RETARGET_TASK_ID |
| `GLB` | النموذج ثلاثي الأبعاد المتحرك بصيغة GLB. يُملأ عندما تكون قيمة `out_format` هي glb. | FILE3DGLB |
| `FBX` | النموذج ثلاثي الأبعاد المتحرك بصيغة FBX. يُملأ عندما تكون قيمة `out_format` هي fbx. | FILE3DFBX |

> تم إنشاء هذه الوثيقة بواسطة الذكاء الاصطناعي. إذا وجدت أي أخطاء أو لديك اقتراحات للتحسين، فلا تتردد في المساهمة! [تحرير على GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoRetargetNode/ar.md)

---
**Source fingerprint (SHA-256):** `4814858b940ece13f85010ff81fcdac0258fe8550aebd914be2613e8f40c0e5a`
