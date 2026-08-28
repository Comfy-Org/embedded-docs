# VOIDSampler

VOIDSampler هو أداة أخذ عينات متخصصة من نوع DDIM لنماذج VOID الخاصة بإكمال الصور (inpainting). وهي تطبّق عملية إزالة الضوضاء نفسها التي دُرِّب عليها نموذج VOID، دون تحجيم الضوضاء الذي تطبّقه أدوات أخذ العينات القياسية من نوع KSampler. استخدم هذه العقدة مع SamplerCustom أو SamplerCustomAdvanced، مع ربطها بمصدر ضوضاء RandomNoise أو VOIDWarpedNoiseSource.

## المدخلات

لا تحتوي هذه العقدة على معاملات إدخال قابلة للتهيئة. وهي أداة أخذ عينات مستقلة تطبّق خوارزمية أخذ عينات DDIM ثابتة.

| المعامل | الوصف | نوع البيانات | مطلوب | النطاق |
| --- | --- | --- | --- | --- |
| *لا توجد مدخلات* | لا تقبل هذه العقدة أي معاملات إدخال. | - | - | - |

## المخرجات

| اسم المخرَج | الوصف | نوع البيانات |
| --- | --- | --- |
| `SAMPLER` | كائن أداة أخذ عينات يطبّق خوارزمية VOID DDIM، وجاهز للاتصال بعقدتي SamplerCustom أو SamplerCustomAdvanced. | SAMPLER |

> تم إنشاء هذه الوثيقة بواسطة الذكاء الاصطناعي. إذا وجدت أي أخطاء أو لديك اقتراحات للتحسين، فلا تتردد في المساهمة! [تحرير على GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDSampler/ar.md)

---
**Source fingerprint (SHA-256):** `b8bb6d3d7220cca4a6dd252efe9c92953b1c5c67c14365e5e0583bc9bdb133be`
