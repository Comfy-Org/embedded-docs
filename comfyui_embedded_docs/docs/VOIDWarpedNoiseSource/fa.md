# VOIDWarpedNoiseSource

## بررسی اجمالی

این گره یک LATENT (مانند خروجی گره VOIDWarpedNoise) را به یک منبع NOISE تبدیل می‌کند. این کار به شما امکان می‌دهد از نویز وارپ‌شده با گره SamplerCustomAdvanced برای تولید تصویر با کنترل بیشتر استفاده کنید.

## ورودی‌ها

| پارامتر | توضیحات | نوع داده | الزامی | محدوده |
| --- | --- | --- | --- | --- |
| `warped_noise` | لاتنت نویز وارپ‌شده از VOIDWarpedNoise | LATENT | بله | N/A |

## خروجی‌ها

| نام خروجی | توضیحات | نوع داده |
| --- | --- | --- |
| NOISE | منبع نویزی که می‌تواند با SamplerCustomAdvanced استفاده شود | NOISE |

> این مستند با هوش مصنوعی تهیه شده است. اگر خطایی دیدید یا پیشنهادی برای بهبود دارید، خوشحال می‌شویم مشارکت کنید! [ویرایش در GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDWarpedNoiseSource/fa.md)

---
**Source fingerprint (SHA-256):** `61d7c82cb8a2acba28f980c4c42c6d4be12788b27676a5d30885799cf9c36185`
