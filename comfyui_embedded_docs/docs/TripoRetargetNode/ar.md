> تم إنشاء هذه الوثيقة بواسطة الذكاء الاصطناعي. إذا وجدت أي أخطاء أو لديك اقتراحات للتحسين، فلا تتردد في المساهمة! [تحرير على GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoRetargetNode/ar.md)

بالتأكيد، إليك الترجمة العربية للوثيقة التقنية الخاصة بعقدة `TripoRetargetNode` مع الالتزام التام بقواعد الترجمة المحددة:

تطبق عقدة TripoRetargetNode رسومًا متحركة محددة مسبقًا على نماذج الشخصيات ثلاثية الأبعاد عن طريق إعادة توجيه بيانات الحركة. تستقبل العقدة نموذجًا ثلاثي الأبعاد تم تجهيزه مسبقًا بالهيكل العظمي (rigged) وتطبق عليه أحد الرسوم المتحركة الجاهزة، مما ينتج ملف نموذج ثلاثي الأبعاد متحرك كمخرجات. تتواصل العقدة مع واجهة Tripo API لمعالجة عملية إعادة توجيه الحركة.

## المدخلات

| المعامل | نوع البيانات | إلزامي | النطاق | الوصف |
|---|---|---|---|---|
| `original_model_task_id` | RIG_TASK_ID | نعم | - | معرف المهمة للنموذج ثلاثي الأبعاد المُجهز بالهيكل العظمي (rigged) والذي تمت معالجته مسبقًا لتطبيق الحركة عليه |
| `animation` | STRING | نعم | "preset:idle"<br>"preset:walk"<br>"preset:run"<br>"preset:dive"<br>"preset:climb"<br>"preset:jump"<br>"preset:slash"<br>"preset:shoot"<br>"preset:hurt"<br>"preset:fall"<br>"preset:turn"<br>"preset:quadruped:walk"<br>"preset:hexapod:walk"<br>"preset:octopod:walk"<br>"preset:serpentine:march"<br>"preset:aquatic:march" | الحركة الجاهزة (preset) المراد تطبيقها على النموذج ثلاثي الأبعاد. تشمل الخيارات حركات بشرية (الوقوف، المشي، الجري، الغوص، التسلق، القفز، الضرب بالسيف، إطلاق النار، التضرر، السقوط، الدوران) وحركات كائنات (مشي رباعي الأرجل، مشي سداسي الأرجل، مشي ثماني الأرجل، زحف أفعواني، زحف مائي). |
| `auth_token_comfy_org` | AUTH_TOKEN_COMFY_ORG | لا | - | رمز المصادقة للوصول إلى واجهة Comfy.org API (معامل مخفي) |
| `api_key_comfy_org` | API_KEY_COMFY_ORG | لا | - | مفتاح API للوصول إلى خدمة Comfy.org (معامل مخفي) |
| `unique_id` | UNIQUE_ID | لا | - | معرف فريد لتتبع العملية (معامل مخفي) |

## المخرجات

| اسم المخرج | نوع البيانات | الوصف |
|---|---|---|
| `model_file` | STRING | ملف النموذج ثلاثي الأبعاد المتحرك المُنشأ (لأغراض التوافق مع الإصدارات السابقة فقط) |
| `retarget task_id` | RETARGET_TASK_ID | معرف المهمة لتتبع عملية إعادة توجيه الحركة |
| `GLB` | FILE3DGLB | النموذج ثلاثي الأبعاد المتحرك بصيغة GLB |

---
**Source fingerprint (SHA-256):** `304326afdc1fa3e8c3593f151f771f93520e061802c831838c58ebc401b9e9e2`
