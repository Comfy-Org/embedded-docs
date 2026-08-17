# VOIDWarpedNoiseSource

## نظرة عامة

تقوم هذه العقدة بتحويل `LATENT` (مثل المخرج من عقدة `VOIDWarpedNoise`) إلى مصدر `NOISE`. يتيح لك ذلك استخدام الضوضاء المشوهة مع عقدة `SamplerCustomAdvanced` لتوليد صور أكثر تحكمًا.

## المدخلات

| المعامل | الوصف | نوع البيانات | مطلوب | النطاق |
| --- | --- | --- | --- | --- |
| `warped_noise` | الـ `latent` الخاص بالضوضاء المشوهة من `VOIDWarpedNoise` | LATENT | نعم | N/A |

## المخرجات

| اسم المخرج | الوصف | نوع البيانات |
| --- | --- | --- |
| `NOISE` | مصدر ضوضاء يمكن استخدامه مع `SamplerCustomAdvanced` | NOISE |

> تم إنشاء هذه الوثيقة بواسطة الذكاء الاصطناعي. إذا وجدت أي أخطاء أو لديك اقتراحات للتحسين، فلا تتردد في المساهمة! [تحرير على GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDWarpedNoiseSource/ar.md)

---
**Source fingerprint (SHA-256):** `61d7c82cb8a2acba28f980c4c42c6d4be12788b27676a5d30885799cf9c36185`
