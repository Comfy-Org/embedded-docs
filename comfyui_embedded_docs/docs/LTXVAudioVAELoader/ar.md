# محمل LTXV Audio VAE

عقدة LTXV Audio VAE Loader تحمّل نموذج Audio Variational Autoencoder (VAE) مُدرَّبًا مسبقًا من ملف checkpoint. تقرأ نقطة التحقق المحددة، وتحتفظ بأوزان Audio VAE وvocoder، وتُهيّئ النموذج للاستخدام في مهام توليد الصوت أو معالجته ضمن ComfyUI.

## المدخلات

| المعامل | الوصف | نوع البيانات | مطلوب | النطاق |
|-----------|-------------|-----------|----------|-------|
| `ckpt_name` | نقطة تحقق Audio VAE المراد تحميلها. هذه قائمة منسدلة تُملأ بجميع الملفات الموجودة في مجلد `checkpoints` الخاص بـ ComfyUI. | COMBO | نعم | جميع الملفات في مجلد `checkpoints`. تُولَّد القائمة في وقت التشغيل. |

يجب أن يكون الملف المحدد نقطة تحقق صالحة لـ LTXV audio VAE. تحتفظ العقدة فقط بأوزان audio VAE وvocoder من الملف، وترفع خطأً إذا لم يكن النموذج المُحمَّل VAE صالحًا.

## المخرجات

| اسم المخرج | الوصف | نوع البيانات |
|-------------|-------------|-----------|
| `Audio VAE` | نموذج Audio Variational Autoencoder المُحمَّل، جاهز للاتصال بعُقد معالجة الصوت الأخرى. | VAE |

> تم إنشاء هذه الوثيقة بواسطة الذكاء الاصطناعي. إذا وجدت أي أخطاء أو لديك اقتراحات للتحسين، فلا تتردد في المساهمة! [تحرير على GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAudioVAELoader/ar.md)

---
**Source fingerprint (SHA-256):** `c91956645a9de0b8f56191f6c0c6bef43f13724ba59078ec9a885168bf2650e8`
