# تهيئة PiD

يرفق كائنًا كامنًا (latent) وقيمة `degrade_sigma` ببيانات CONDITIONING بحيث يمكن استخدامها في فك ترميز PiD أو التحسين بالتكبير. يتيح لك ذلك التحكم في مقدار تدهور الـ latent قبل معالجته.

## المدخلات

| المعامل | الوصف | نوع البيانات | مطلوب | النطاق |
|-----------|-------------|-----------|----------|-------|
| `positive` | بيانات CONDITIONING المراد إرفاق `latent` وقيمة `degrade_sigma` بها. | CONDITIONING | نعم | - |
| `latent` | الـ latent (من VAEEncode أو KSampler) المراد إرفاقه ببيانات CONDITIONING. | LATENT | نعم | - |
| `latent_format` | تنسيق الـ latent. يتم اكتشاف تنسيقات Flux1 (16 قناة) وFlux2 (128 قناة) تلقائيًا من بُعد القنوات ضمن `"flux"`. أما بالنسبة إلى SD3 (16 قناة)، أو SDXL (4 قنوات)، أو QwenImage (16 قناة)، فاختره يدويًا (الافتراضي: `"flux"`). | COMBO | نعم | `"flux"`<br>`"sd3"`<br>`"sdxl"`<br>`"qwenimage"` |
| `degrade_sigma` | مقدار التدهور المراد تطبيقه. تعني القيمة 0 كائنًا كامنًا نظيفًا. زد هذه القيمة لإزالة الضوضاء من مخرجات latent التالفة (الافتراضي: 0.0). | FLOAT | نعم | 0.0 إلى 1.0 (step: 0.01) |

ملاحظة: عندما يتم ضبط `latent_format` على `"flux"`، تقوم العقدة تلقائيًا بالكشف عن نوع الـ latent من بُعد القنوات: تُعامَل 128 قناة كـ latents من نوع Flux2، بينما تُعامَل 16 قناة كـ latents من نوع Flux1.

ملاحظة: تؤدي قيمة `latent_format` غير المدعومة إلى خطأ، لكن العقدة تتعامل مع جميع الخيارات المتاحة.

## المخرجات

| اسم المخرج | الوصف | نوع البيانات |
|-------------|-----------|-----------|
| `CONDITIONING` | بيانات CONDITIONING الأصلية مع إرفاق `latent` وقيمة `degrade_sigma`. | CONDITIONING |

> تم إنشاء هذه الوثيقة بواسطة الذكاء الاصطناعي. إذا وجدت أي أخطاء أو لديك اقتراحات للتحسين، فلا تتردد في المساهمة! [تحرير على GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PiDConditioning/ar.md)

---
**Source fingerprint (SHA-256):** `24f613b33e7872cb35f458aa5794a3cc4d37ceaecd43725039edef75f4a512bc`
