# Text Encode MOSS-Image Edit

يقوم بتشفير تعليمة تعديل إلى جانب الصور المرجعية إلى تهيئة شرطية من أجل LoRA لتعديل MOSS-Image. وصّل المخرج كتهيئة شرطية موجبة، وشغّل نسخة ثانية مع المراجع نفسها من أجل التهيئة السلبية. تُستخدم المراجع بالحجم الذي تصل به، لذا قم بتحجيمها قبل التوصيل. هذه العقدة مُعلّمة كتجريبية في ComfyUI. بدون VAE تذهب الصور إلى مشفّر النص فقط.

## المدخلات

| المعامل | الوصف | نوع البيانات | مطلوب | النطاق |
| --- | --- | --- | --- | --- |
| `clip` | نموذج CLIP الذي يُجزّئ التعليمة إلى رموز ويشفّرها. | CLIP | نعم | - |
| `prompt` | التعليمة التي تصف التعديل. تدعم النص متعدد الأسطر والتوجيهات الديناميكية. | STRING | نعم | أي نص |
| `vae` | VAE المستخدم لتشفير الصور المرجعية إلى تمثيلات كامنة مرجعية. اختياري: بدونه تذهب الصور إلى مشفّر النص فقط.| VAE | لا | - |
| `edit_format` | التخطيط الذي دُرّب عليه LoRA التعديل. يحدد طريقة التمثيلات الكامنة المرجعية وما إذا كان مشفّر النص يرى المراجع أيضًا. | COMBO | نعم | `"ai-toolkit"`<br>`"ai-toolkit (kv_cache off)"`<br>`"Moss-Image-Edit"` |
| `images` | فتحة قابلة للتوسع: وصّل صورة مرجعية واحدة أو أكثر (`image_1`, `image_2`, ...). تُستخدم كل صورة بالحجم الذي تصل به، وتُسقَط قناة ألفا الخاصة بها، وتُشفَّر عبر VAE إلى تمثيل كامن مرجعي. عند توصيل VAE تُسقَط قناة ألفا وتُشفَّر كل صورة إلى تمثيل كامن مرجعي؛ بدون VAE تذهب الصور إلى مشفّر النص فقط.| IMAGE | نعم | صورة واحدة أو أكثر |
| `image_strength` | يضبط مدى انتباه النموذج للصور التي يراها مشفّر النص (تنسيقات ai-toolkit أو بدون VAE): 0 يتجاهلها، 1 بلا تغيير، وأعلى من 1 يؤكدها. متقدم. الافتراضي: 1.0. | FLOAT | نعم | 0.0 to 100.0 (step 0.05) |

**ملاحظة:** With `"ai-toolkit"` and `"ai-toolkit (kv_cache off)"`, or when no VAE is connected and `image_strength` is above 0, the text encoder also sees every reference, downscaled to at most 384x384 pixels and preceded by a `Picture N:` marker in the prompt, so the instruction can refer to them by number. With `"Moss-Image-Edit"` and a VAE connected, the references reach the model only as reference latents and the text encoder sees the instruction alone. `"ai-toolkit (kv_cache off)"` additionally keeps the references attending to the image being generated, so they are recomputed on every sampling step.

## المخرجات

| اسم المخرج | الوصف | نوع البيانات |
| --- | --- | --- |
| `conditioning` | التعليمة المشفرة مع التمثيلات الكامنة المرجعية وطريقة التمثيلات الكامنة المرجعية المطابقة مرفقة بها. | CONDITIONING |

> تم إنشاء هذه الوثيقة بواسطة الذكاء الاصطناعي. إذا وجدت أي أخطاء أو لديك اقتراحات للتحسين، فلا تتردد في المساهمة! [تحرير على GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeMOSSImageEdit/ar.md)

---
**Source fingerprint (SHA-256):** `673f098df6a8e466a5c8060009f446eac8f7556311a870de626c5f4bfc3ab196`
