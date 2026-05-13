> تم إنشاء هذه الوثيقة بواسطة الذكاء الاصطناعي. إذا وجدت أي أخطاء أو لديك اقتراحات للتحسين، فلا تتردد في المساهمة! [تحرير على GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodePixArtAlpha/ar.md)

# ترجمة وثيقة CLIPTextEncodePixArtAlpha

تم إنشاء هذه الوثائق بواسطة الذكاء الاصطناعي. إذا وجدت أي أخطاء أو لديك اقتراحات للتحسين، فلا تتردد في المساهمة! [تحرير على GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodePixArtAlpha/en.md)

يقوم هذا العقدة بتشفير النص وتعيين شرطية الدقة لنماذج PixArt Alpha. تعالج هذه العقدة إدخال النص وتضيف معلومات العرض والارتفاع لإنشاء بيانات شرطية خاصة بنماذج PixArt Alpha. لا تنطبق على نماذج PixArt Sigma.

## المدخلات

| المعامل | نوع البيانات | مطلوب | النطاق | الوصف |
|---------|--------------|-------|--------|-------|
| `width` | INT | نعم | 0 إلى MAX_RESOLUTION | بُعد العرض لشرطية الدقة (الافتراضي: 1024) |
| `height` | INT | نعم | 0 إلى MAX_RESOLUTION | بُعد الارتفاع لشرطية الدقة (الافتراضي: 1024) |
| `text` | STRING | نعم | - | إدخال النص المراد تشفيره، يدعم الإدخال متعدد الأسطر والمحفزات الديناميكية |
| `clip` | CLIP | نعم | - | نموذج CLIP المستخدم في الترميز والتشفير |

## المخرجات

| اسم المخرج | نوع البيانات | الوصف |
|------------|--------------|-------|
| `CONDITIONING` | CONDITIONING | بيانات شرطية مشفرة تحتوي على رموز النص ومعلومات الدقة |

---
**Source fingerprint (SHA-256):** `d15df3c7bcca10ec85f0689d6631a6b89aa89e609193c36b658b1bc97f90ee9a`
