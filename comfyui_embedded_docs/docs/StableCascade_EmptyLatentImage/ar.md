# صورة كامنة فارغة من StableCascade

تنشئ عقدة `StableCascade_EmptyLatentImage` موترات كامنة فارغة لنماذج Stable Cascade. تُنشئ تمثيلين كامنين منفصلين - أحدهما للمرحلة C والآخر للمرحلة B - بأبعاد مناسبة بناءً على دقة الإدخال وإعدادات الضغط. توفر هذه العقدة نقطة البداية لخط أنابيب توليد Stable Cascade.

## المدخلات

| المعامل | الوصف | نوع البيانات | مطلوب | النطاق |
| --- | --- | --- | --- | --- |
| `width` | عرض الصورة الناتجة بالبكسل (الافتراضي: 1024، الخطوة: 8) | INT | نعم | 256 to MAX_RESOLUTION |
| `height` | ارتفاع الصورة الناتجة بالبكسل (الافتراضي: 1024، الخطوة: 8) | INT | نعم | 256 to MAX_RESOLUTION |
| `compression` | عامل الضغط الذي يحدد أبعاد المساحة الكامنة للمرحلة C (الافتراضي: 42، الخطوة: 1). هذه معلمة متقدمة. | INT | نعم | 4 to 128 |
| `batch_size` | عدد العينات الكامنة التي سيتم توليدها في دفعة واحدة (الافتراضي: 1) | INT | لا | 1 to 4096 |

## المخرجات

| اسم المخرج | الوصف | نوع البيانات |
| --- | --- | --- |
| `stage_c` | موتر كامن للمرحلة C بأبعاد [batch_size, 16, height//compression, width//compression] | LATENT |
| `stage_b` | موتر كامن للمرحلة B بأبعاد [batch_size, 4, height//4, width//4] | LATENT |

> تم إنشاء هذه الوثيقة بواسطة الذكاء الاصطناعي. إذا وجدت أي أخطاء أو لديك اقتراحات للتحسين، فلا تتردد في المساهمة! [تحرير على GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_EmptyLatentImage/ar.md)

---
**Source fingerprint (SHA-256):** `f336f87d0ec14b3716efda2cfaa194b1f80707d64821bb56ade7d88d9bd5b53f`
