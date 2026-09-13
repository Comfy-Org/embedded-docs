# VOIDWarpedNoiseSource

این گره یک LATENT (مانند خروجی گره VOIDWarpedNoise) را به یک منبع NOISE تبدیل می‌کند. این امکان را می‌دهد که نویز پیچ‌خورده از پیش محاسبه‌شده را به گره‌هایی وارد کنید که انتظار یک منبع نویز دارند، مانند SamplerCustomAdvanced.

## ورودی‌ها

| پارامتر | توضیح | نوع داده | الزامی | محدوده |
| --- | --- | --- | --- | --- |
| `warped_noise` | لاتنت نویز پیچ‌خورده از VOIDWarpedNoise | LATENT | بله | N/A |

## خروجی‌ها

| نام خروجی | توضیح | نوع داده |
| --- | --- | --- |
| `NOISE` | یک منبع NOISE که لاتنت ارائه‌شده را در خود جای می‌دهد و با SamplerCustomAdvanced قابل استفاده است | NOISE |

> این مستند با هوش مصنوعی تهیه شده است. اگر خطایی دیدید یا پیشنهادی برای بهبود دارید، خوشحال می‌شویم مشارکت کنید! [ویرایش در GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDWarpedNoiseSource/fa.md)

---
**Source fingerprint (SHA-256):** `61d7c82cb8a2acba28f980c4c42c6d4be12788b27676a5d30885799cf9c36185`
