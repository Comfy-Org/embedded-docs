# ByteDanceImageEditNode

تتيح لك عقدة ByteDance Image Edit تعديل الصور باستخدام نماذج الذكاء الاصطناعي الخاصة بـ ByteDance عبر واجهة API. تقوم بتزويد صورة إدخال ومطالبة نصية تصف التغييرات المطلوبة، وتعالج العقدة الصورة وفقًا لتعليماتك. تتولى العقدة الاتصال بواجهة API تلقائيًا وتعيد الصورة المحررة.

## المدخلات

| المعامل | الوصف | نوع البيانات | نوع الإدخال | الافتراضي | النطاق |
| --- | --- | --- | --- | --- | --- |
| `model` | اسم النموذج | MODEL | COMBO | seededit_3 | خيارات Image2ImageModelName |
| `image` | الصورة الأساسية المراد تحريرها | IMAGE | IMAGE | - | - |
| `prompt` | تعليمات لتحرير الصورة | STRING | STRING | "" | - |
| `seed` | البذرة المستخدمة للتوليد | INT | INT | 0 | 0-2147483647 |
| `guidance_scale` | قيمة أعلى تجعل الصورة تتبع المطالبة النصية بشكل أقرب | FLOAT | FLOAT | 5.5 | 1.0-10.0 |
| `watermark` | ما إذا كان سيتم إضافة علامة مائية "AI generated" إلى الصورة | BOOLEAN | BOOLEAN | True | - |

## المخرجات

| اسم المخرَج | الوصف | نوع البيانات |
| --- | --- | --- |
| `IMAGE` | الصورة المحررة المُعادة من واجهة API الخاصة بـ ByteDance | IMAGE |

> تم إنشاء هذه الوثيقة بواسطة الذكاء الاصطناعي. إذا وجدت أي أخطاء أو لديك اقتراحات للتحسين، فلا تتردد في المساهمة! [تحرير على GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceImageEditNode/ar.md)

---
**Source fingerprint (SHA-256):** `9dc13d89f84756b545120efb5535e08ada163d4534975809f5056bdf7d8bfb73`
