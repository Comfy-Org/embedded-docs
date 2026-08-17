# ترميز نص CLIP لـ PixArt Alpha

يقوم هذا العقد بتشفير النص وضبط دقة التكييف (resolution conditioning) لنماذج PixArt Alpha. تعالج هذه العقدة إدخال النص وتضيف معلومات العرض والارتفاع لإنشاء بيانات تكييف (conditioning data) خصيصًا لنماذج PixArt Alpha. لا تنطبق على نماذج PixArt Sigma.

## المدخلات

| المعامل | الوصف | نوع البيانات | مطلوب | النطاق |
| --- | --- | --- | --- | --- |
| `width` | بُعد العرض لتكييف الدقة (الافتراضي: 1024) | INT | نعم | 0 to MAX_RESOLUTION |
| `height` | بُعد الارتفاع لتكييف الدقة (الافتراضي: 1024) | INT | نعم | 0 to MAX_RESOLUTION |
| `text` | نص الإدخال المراد تشفيره، يدعم الإدخال متعدد الأسطر والموجهات الديناميكية | STRING | نعم | - |
| `clip` | نموذج CLIP المستخدم في الترميز وتحويل النص إلى رموز | CLIP | نعم | - |

## المخرجات

| اسم المخرج | الوصف | نوع البيانات |
| --- | --- | --- |
| `CONDITIONING` | بيانات تكييف مشفرة تحتوي على رموز النص ومعلومات الدقة | CONDITIONING |

> تم إنشاء هذه الوثيقة بواسطة الذكاء الاصطناعي. إذا وجدت أي أخطاء أو لديك اقتراحات للتحسين، فلا تتردد في المساهمة! [تحرير على GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodePixArtAlpha/ar.md)

---
**Source fingerprint (SHA-256):** `d25a4117d39e3528cd0f64bc34462cd7b4076c67cb4e454c77fcc66490f89be6`
