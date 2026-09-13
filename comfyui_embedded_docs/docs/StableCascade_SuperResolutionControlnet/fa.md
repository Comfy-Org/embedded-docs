# StableCascade_SuperResolutionControlnet

این گره بخشی از گروه آزمایشی Stable Cascade است. این گره با رمزگذاری یک تصویر ورودی توسط VAE برای ساخت ورودی ControlNet، و با تولید جای‌نگهدارهای latent خالی (پرشده با صفر) برای مرحله C و مرحله B خط لوله Stable Cascade، ورودی‌های پردازش ابرتفکیک Stable Cascade را آماده می‌کند.

## ورودی‌ها

| پارامتر | توضیحات | نوع داده | الزامی | بازه |
| --- | --- | --- | --- | --- |
| `image` | تصویر ورودی که باید برای ابرتفکیک پردازش شود. فقط ۳ کانال رنگی اول (RGB) تصویر برای رمزگذاری استفاده می‌شوند. | IMAGE | بله | - |
| `vae` | مدل VAE مورد استفاده برای رمزگذاری تصویر ورودی | VAE | بله | - |

## خروجی‌ها

| نام خروجی | توضیحات | نوع داده |
| --- | --- | --- |
| `controlnet_input` | نمایش تصویر رمزگذاری‌شده با VAE که برای ورودی ControlNet مناسب است | IMAGE |
| `stage_c` | جای‌نگهدار latent (پرشده با صفر) برای مرحله C پردازش Stable Cascade، با ۱۶ کانال و ابعادی مبتنی بر اندازه تصویر ورودی تقسیم بر ۱۶ | LATENT |
| `stage_b` | جای‌نگهدار latent (پرشده با صفر) برای مرحله B پردازش Stable Cascade، با ۴ کانال و ابعادی مبتنی بر اندازه تصویر ورودی تقسیم بر ۲ | LATENT |

> این مستند با هوش مصنوعی تهیه شده است. اگر خطایی دیدید یا پیشنهادی برای بهبود دارید، خوشحال می‌شویم مشارکت کنید! [ویرایش در GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_SuperResolutionControlnet/fa.md)

---
**Source fingerprint (SHA-256):** `d9eff373ac7736f2e2f9788d1b43c04bb3212422aa1703d1d58ac512ce476925`
