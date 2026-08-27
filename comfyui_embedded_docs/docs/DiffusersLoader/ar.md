# تحميل Diffusers

المدخلات والمخرجات لعقدة DiffusersLoader

تقوم عقدة DiffusersLoader بتحميل النماذج المدربة مسبقًا المحفوظة بصيغة diffusers. تبحث في مجلدات `diffusers` المُعدّة عن المجلدات التي تحتوي على ملف `model_index.json`، وتتيح لك تحديد أحدها، ثم تحميله كمكوّنات MODEL وCLIP وVAE المستخدمة في خط المعالجة. هذه العقدة مهملة، لكنها تبقى متاحة للتوافق مع نماذج Hugging Face بصيغة diffusers.

## المدخلات

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `مسار النموذج` | المسار إلى مجلد نموذج diffusers المراد تحميله. تقوم العقدة بمسح مجلدات diffusers المُعدّة تلقائيًا للبحث عن النماذج الصالحة وتعرض الخيارات المتاحة. | COMBO | نعم | خيارات متعددة متاحة<br>(تُملأ تلقائيًا من مجلدات diffusers) |

## المخرجات

| Output Name | Description | Data Type |
|-----------|-------------|-----------|
| `MODEL` | مكوّن النموذج المُحمَّل من صيغة diffusers. | MODEL |
| `CLIP` | مكوّن نموذج CLIP المُحمَّل من صيغة diffusers. | CLIP |
| `VAE` | مكوّن VAE (التشفير التلقائي المتغير) المُحمَّل من صيغة diffusers. | VAE |

> تم إنشاء هذه الوثيقة بواسطة الذكاء الاصطناعي. إذا وجدت أي أخطاء أو لديك اقتراحات للتحسين، فلا تتردد في المساهمة! [تحرير على GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DiffusersLoader/ar.md)

---
**Source fingerprint (SHA-256):** `75238342d05eac7528f981a2d4544accb6053891cd078a77751cc838054225d4`
