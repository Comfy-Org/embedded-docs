# VOIDWarpedNoiseSource

تقوم هذه العقدة بتحويل LATENT (مثل المخرجات من عقدة VOIDWarpedNoise) إلى مصدر NOISE. يتيح لك ذلك تغذية ضوضاء مشوَّهة محسوبة مسبقًا إلى العقد التي تتوقع مصدر ضوضاء، مثل SamplerCustomAdvanced.

## المدخلات

| المعامل | الوصف | نوع البيانات | مطلوب | النطاق |
| --- | --- | --- | --- | --- |
| `warped_noise` | LATENT ضوضاء مشوَّهة من VOIDWarpedNoise | LATENT | نعم | لا ينطبق |

## المخرجات

| اسم المخرَج | الوصف | نوع البيانات |
| --- | --- | --- |
| `NOISE` | مصدر ضوضاء يغلّف LATENT المزوَّد، ويمكن استخدامه مع SamplerCustomAdvanced | NOISE |

> تم إنشاء هذه الوثيقة بواسطة الذكاء الاصطناعي. إذا وجدت أي أخطاء أو لديك اقتراحات للتحسين، فلا تتردد في المساهمة! [تحرير على GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDWarpedNoiseSource/ar.md)

---
**Source fingerprint (SHA-256):** `61d7c82cb8a2acba28f980c4c42c6d4be12788b27676a5d30885799cf9c36185`
