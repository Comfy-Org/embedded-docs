# تحميل نموذج تكبير latent

عقدة LatentUpscaleModelLoader تحمّل نموذجًا متخصصًا في تكبير التمثيلات الكامنة من ملف مخزّن في مجلد `latent_upscale_models` الخاص بـ ComfyUI. وتكتشف تلقائيًا بنية النموذج من محتويات الملف (Hunyuan Video 720p، أو Hunyuan Video 1080p، أو Latent Upsampler) وتهيئ النموذج الداخلي المطابق، بحيث تكون النتيجة جاهزة للاستخدام بواسطة عقد أخرى.

## المدخلات

| المعامل | الوصف | نوع البيانات | مطلوب | النطاق |
| --- | --- | --- | --- | --- |
| `model_name` | اسم ملف نموذج التكبير الكامن المراد تحميله. تُملأ الخيارات المتاحة ديناميكيًا من الملفات الموجودة في دليل `latent_upscale_models` الخاص بـ ComfyUI. | COMBO | نعم | كل الملفات في مجلد `latent_upscale_models` |

## المخرجات

| اسم المخرجات | الوصف | نوع البيانات |
| --- | --- | --- |
| `model` | نموذج التكبير الكامن المحمّل، المهيأ والجاهز للاستخدام. واعتمادًا على محتويات الملف المكتشفة، يكون هذا مُكبّر Hunyuan Video بدقة 720p، أو مُكبّر Hunyuan Video بدقة 1080p، أو نموذج Latent Upsampler مُغلّف. | LATENT_UPSCALE_MODEL |

> تم إنشاء هذه الوثيقة بواسطة الذكاء الاصطناعي. إذا وجدت أي أخطاء أو لديك اقتراحات للتحسين، فلا تتردد في المساهمة! [تحرير على GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentUpscaleModelLoader/ar.md)

---
**Source fingerprint (SHA-256):** `7e23214b1b1fc11be84910a5a209c7990a5199120cb0e6b6c61302a442dcf153`
