## نمای کلی

این گره یک LATENT (مانند خروجی گره VOIDWarpedNoise) را به یک منبع NOISE تبدیل می‌کند. این امکان را فراهم می‌کند تا از نویز تغییرشکل‌یافته با گره SamplerCustomAdvanced برای تولید تصویر کنترل‌شده‌تر استفاده کنید.

## ورودی‌ها

| پارامتر | توضیحات | نوع داده | الزامی | محدوده |
| --- | --- | --- | --- | --- |
| `warped_noise` | نویز تغییرشکل‌یافته از گره VOIDWarpedNoise | LATENT | بله | نامشخص |

## خروجی‌ها

| نام خروجی | توضیحات | نوع داده |
| --- | --- | --- |
| `NOISE` | یک منبع نویز که می‌تواند با SamplerCustomAdvanced استفاده شود | NOISE |

> این مستند با هوش مصنوعی تهیه شده است. اگر خطایی دیدید یا پیشنهادی برای بهبود دارید، خوشحال می‌شویم مشارکت کنید! [ویرایش در GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDWarpedNoiseSource/fa.md)

---
**Source fingerprint (SHA-256):** `ff798d223da5cf705a40ad1f36cc403030105331d0cc4173e9553cd3718c5d93`
