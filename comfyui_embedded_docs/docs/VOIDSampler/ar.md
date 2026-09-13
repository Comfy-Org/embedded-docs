# VOIDSampler

VOIDSampler هي أداة أخذ عينات DDIM متخصصة مُصممة لنماذج الترميم الداخلي VOID. تعيد إنتاج عملية إزالة الضوضاء الدقيقة التي دُرّب عليها VOID، مع تخطي تحجيم الضوضاء الذي تطبقه أدوات KSampler القياسية. استخدم هذه العقدة مع SamplerCustom أو SamplerCustomAdvanced، مقترنةً بـ RandomNoise أو VOIDWarpedNoiseSource.

## المدخلات

هذه العقدة لا تحتوي على أي معاملات إدخال قابلة للتهيئة. إنها أداة أخذ عينات مكتفية ذاتيًا تطبّق خوارزمية أخذ عينات DDIM ثابتة.

| المعامل | الوصف | نوع البيانات | مطلوب | النطاق |
| --- | --- | --- | --- | --- |
| *لا توجد مدخلات* | هذه العقدة لا تقبل أي معاملات إدخال. | - | - | - |

## المخرجات

| اسم المخرج | الوصف | نوع البيانات |
| --- | --- | --- |
| `SAMPLER` | كائن أداة أخذ عينات يطبّق خوارزمية VOID DDIM، وجاهز للاتصال بعقد SamplerCustom أو SamplerCustomAdvanced. | SAMPLER |

> تم إنشاء هذه الوثيقة بواسطة الذكاء الاصطناعي. إذا وجدت أي أخطاء أو لديك اقتراحات للتحسين، فلا تتردد في المساهمة! [تحرير على GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDSampler/ar.md)

---
**Source fingerprint (SHA-256):** `b8bb6d3d7220cca4a6dd252efe9c92953b1c5c67c14365e5e0583bc9bdb133be`
