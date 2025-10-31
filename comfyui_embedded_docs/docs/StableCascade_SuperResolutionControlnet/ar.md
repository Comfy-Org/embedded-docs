> تم إنشاء هذه الوثيقة بواسطة الذكاء الاصطناعي. إذا وجدت أي أخطاء أو لديك اقتراحات للتحسين، فلا تتردد في المساهمة! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_SuperResolutionControlnet/ar.md)

# StableCascade_SuperResolutionControlnet

تُعد عقدة StableCascade_SuperResolutionControlnet مدخلات لمعالجة الدقة الفائقة في Stable Cascade. تأخذ العقدة صورة إدخال وتشفرها باستخدام VAE لإنشاء مدخلات controlnet، بينما تقوم أيضًا بإنشاء تمثيلات كامنة بديلة للمرحلة C والمرحلة B من خط أنابيب Stable Cascade.

## المدخلات

| المعامل      | نوع البيانات | مطلوب | النطاق | الوصف |
|--------------|---------------|--------|--------|--------|
| `صورة`      | IMAGE         | نعم    | -      | صورة الإدخال المراد معالجتها للدقة الفائقة |
| `vae`        | VAE           | نعم    | -      | نموذج VAE المستخدم لتشفير صورة الإدخال |

## المخرجات

| اسم المخرج         | نوع البيانات | الوصف |
|--------------------|---------------|--------|
| `المرحلة_ج` | IMAGE         | التمثيل المشفر للصورة المناسب لمدخلات controlnet |
| `المرحلة_ب`          | LATENT        | التمثيل الكامن البديل للمرحلة C من معالجة Stable Cascade |
| `stage_b`          | LATENT        | التمثيل الكامن البديل للمرحلة B من معالجة Stable Cascade |