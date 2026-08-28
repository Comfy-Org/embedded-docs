# VOIDWarpedNoiseSource

## نظرة عامة

تحوّل هذه العقدة الكمون (LATENT) مثل المخرجات من عقدة VOIDWarpedNoise إلى مصدر ضجيج (NOISE). يتيح لك ذلك استخدام الضجيج المشوّه مع عقدة SamplerCustomAdvanced لتوليد صور أكثر تحكمًا.

## المدخلات

| المعامل | الوصف | نوع البيانات | مطلوب | النطاق |
| --- | --- | --- | --- | --- |
| `warped_noise` | كمون الضجيج المشوّه من VOIDWarpedNoise | LATENT | نعم | N/A |

## المخرجات

| اسم المخرج | الوصف | نوع البيانات |
| --- | --- | --- |
| `NOISE` | مصدر ضجيج يمكن استخدامه مع عقدة SamplerCustomAdvanced | NOISE |

> تم إنشاء هذه الوثيقة بواسطة الذكاء الاصطناعي. إذا وجدت أي أخطاء أو لديك اقتراحات للتحسين، فلا تتردد في المساهمة! [تحرير على GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDWarpedNoiseSource/ar.md)

---
**Source fingerprint (SHA-256):** `61d7c82cb8a2acba28f980c4c42c6d4be12788b27676a5d30885799cf9c36185`
