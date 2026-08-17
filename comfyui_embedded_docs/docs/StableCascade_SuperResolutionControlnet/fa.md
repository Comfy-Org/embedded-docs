# StableCascade_SuperResolutionControlnet

گره `StableCascade_SuperResolutionControlnet` ورودی‌های پردازش فوق‌تفکیک Stable Cascade را آماده می‌کند. این گره یک تصویر ورودی دریافت کرده و آن را با استفاده از یک VAE کدگذاری می‌کند تا ورودی ControlNet تولید شود؛ همچنین نمایش‌های نهفتهٔ مکان‌نشان (placeholder) را برای مرحله C و مرحله B خط لوله Stable Cascade ایجاد می‌کند.

## ورودی‌ها

| پارامتر | توضیحات | نوع داده | الزامی | محدوده |
| --- | --- | --- | --- | --- |
| `image` | تصویر ورودی که برای فوق‌تفکیک پردازش می‌شود | IMAGE | بله | - |
| `vae` | مدل VAE مورد استفاده برای کدگذاری تصویر ورودی | VAE | بله | - |

توجه: هنگام کدگذاری با VAE، تنها سه کانال رنگی اول تصویر ورودی استفاده می‌شود.

## خروجی‌ها

| نام خروجی | توضیحات | نوع داده |
| --- | --- | --- |
| `controlnet_input` | بازنمایی تصویر کدگذاری‌شده مناسب برای ورودی ControlNet | IMAGE |
| `stage_c` | بازنمایی نهفتهٔ مکان‌نشان برای مرحله C پردازش Stable Cascade، با ابعادی بر اساس اندازه تصویر ورودی تقسیم‌بر ۱۶ | LATENT |
| `stage_b` | بازنمایی نهفتهٔ مکان‌نشان برای مرحله B پردازش Stable Cascade، با ابعادی بر اساس اندازه تصویر ورودی تقسیم‌بر ۲ | LATENT |

> این مستند با هوش مصنوعی تهیه شده است. اگر خطایی دیدید یا پیشنهادی برای بهبود دارید، خوشحال می‌شویم مشارکت کنید! [ویرایش در GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_SuperResolutionControlnet/fa.md)

---
**Source fingerprint (SHA-256):** `d9eff373ac7736f2e2f9788d1b43c04bb3212422aa1703d1d58ac512ce476925`
