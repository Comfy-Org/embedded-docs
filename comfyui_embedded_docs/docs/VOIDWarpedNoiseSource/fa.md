# VOIDWarpedNoiseSource

## نمای کلی

این گره یک LATENT (مانند خروجی گره VOIDWarpedNoise) را به یک منبع NOISE تبدیل می‌کند. این امکان را فراهم می‌کند تا نویز تغییرشکل‌یافته را با گره SamplerCustomAdvanced برای تولید تصویری کنترل‌شده‌تر استفاده کنید.

## ورودی‌ها

| پارامتر | توضیحات | نوع داده | الزامی | محدوده |
| --- | --- | --- | --- | --- |
| `warped_noise` | نویز تغییرشکل‌یافته لاتنت از VOIDWarpedNoise | LATENT | بله | N/A |

## خروجی‌ها

| نام خروجی | توضیحات | نوع داده |
| --- | --- | --- |
| `NOISE` | یک منبع نویز که می‌توان با SamplerCustomAdvanced استفاده کرد | NOISE |

> این مستند با هوش مصنوعی تهیه شده است. اگر خطایی دیدید یا پیشنهادی برای بهبود دارید، خوشحال می‌شویم مشارکت کنید! [ویرایش در GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDWarpedNoiseSource/fa.md)

---
**Source fingerprint (SHA-256):** `61d7c82cb8a2acba28f980c4c42c6d4be12788b27676a5d30885799cf9c36185`
