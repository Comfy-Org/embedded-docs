تم ترجمة الوثيقة التالية إلى العربية مع الالتزام بقواعد الترجمة المحددة:

هذه العقدة تقوم بتهيئة نمط لاستخدامه مع واجهة برمجة تطبيقات Recraft، مع تحديد نمط "الرسم التوضيحي الرقمي" تحديدًا. تتيح لك اختيار نمط فرعي اختياري لتحسين التوجيه الفني للصورة المُنشأة.

## المدخلات

| المعامل | الوصف | نوع البيانات | إلزامي | النطاق |
| --- | --- | --- | --- | --- |
| `النمط الفرعي` | نمط فرعي اختياري لتحديد نوع معين من الرسم التوضيحي الرقمي. إذا لم يتم تحديده، يتم استخدام النمط الأساسي "الرسم التوضيحي الرقمي". | STRING | لا | `"digital_illustration"`<br>`"digital_illustration_anime"`<br>`"digital_illustration_cartoon"`<br>`"digital_illustration_comic"`<br>`"digital_illustration_concept_art"`<br>`"digital_illustration_fantasy"`<br>`"digital_illustration_futuristic"`<br>`"digital_illustration_graffiti"`<br>`"digital_illustration_graphic_novel"`<br>`"digital_illustration_hyperrealistic"`<br>`"digital_illustration_ink"`<br>`"digital_illustration_manga"`<br>`"digital_illustration_minimalist"`<br>`"digital_illustration_pixel_art"`<br>`"digital_illustration_pop_art"`<br>`"digital_illustration_retro"`<br>`"digital_illustration_sci_fi"`<br>`"digital_illustration_sticker"`<br>`"digital_illustration_street_art"`<br>`"digital_illustration_surreal"`<br>`"digital_illustration_vector"` |

## المخرجات

| اسم المخرج | الوصف | نوع البيانات |
| --- | --- | --- |
| `recraft_style` | كائن نمط مُهيأ يحتوي على النمط المحدد "الرسم التوضيحي الرقمي" والنمط الفرعي الاختياري، جاهز للإرسال إلى عقد واجهة برمجة تطبيقات Recraft الأخرى. | STYLEV3 |

> تم إنشاء هذه الوثيقة بواسطة الذكاء الاصطناعي. إذا وجدت أي أخطاء أو لديك اقتراحات للتحسين، فلا تتردد في المساهمة! [تحرير على GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftStyleV3DigitalIllustration/ar.md)

---
**Source fingerprint (SHA-256):** `e52790a670839608ee1cb576e802a54d3bf2ca879ec288a24acd4ac7db27021a`
