# VOIDInpaintConditioning

گره VOIDInpaintConditioning داده‌های conditioning موردنیاز برای inpainting با مدل‌های CogVideoX را آماده می‌کند. این گره یک ویدیوی منبع و یک quadmask از‌پیش‌پردازش‌شده را دریافت می‌کند، آن‌ها را از طریق VAE رمزگذاری می‌کند و آن‌ها را در یک سیگنال conditioning با ۳۲ کانال (۱۶ کانال از ماسک + ۱۶ کانال از ویدیوی ماسک‌شده) ترکیب می‌کند که مدل از آن برای پر کردن نواحی ماسک‌شده استفاده می‌کند.

## ورودی‌ها

| پارامتر | توضیحات | نوع داده | الزامی | محدوده |
| --- | --- | --- | --- | --- |
| `positive` | conditioning مثبت که با اطلاعات latent مربوط به inpainting تکمیل می‌شود | CONDITIONING | بله | - |
| `negative` | conditioning منفی که با اطلاعات latent مربوط به inpainting تکمیل می‌شود | CONDITIONING | بله | - |
| `vae` | مدل VAE مورد استفاده برای رمزگذاری ماسک و ویدیوی ماسک‌شده به فضای latent | VAE | بله | - |
| `video` | فریم‌های ویدیوی منبع [T, H, W, 3] | IMAGE | بله | - |
| `quadmask` | quadmask از‌پیش‌پردازش‌شده از VOIDQuadmaskPreprocess [T, H, W] | MASK | بله | - |
| `width` | عرضی که ویدیو و ماسک به آن تغییر اندازه می‌دهند (پیش‌فرض: 672) | INT | بله | 16 to MAX_RESOLUTION (step: 8) |
| `height` | ارتفاعی که ویدیو و ماسک به آن تغییر اندازه می‌دهند (پیش‌فرض: 384) | INT | بله | 16 to MAX_RESOLUTION (step: 8) |
| `length` | تعداد فریم‌های پیکسلی برای پردازش. برای CogVideoX-Fun-V1.5 (patch_size_t=2)، latent_t باید زوج باشد — طول‌هایی که latent_t فرد تولید می‌کنند به پایین گرد می‌شوند (مثلاً 49 → 45) (پیش‌فرض: 45) | INT | بله | 1 to MAX_RESOLUTION (step: 1) |
| `batch_size` | اندازه دسته (batch size) برای latent نویز خروجی (پیش‌فرض: 1) | INT | بله | 1 تا 64 |

## خروجی‌ها

| نام خروجی | توضیحات | نوع داده |
| --- | --- | --- |
| `positive` | conditioning مثبت که اطلاعات latent مربوط به inpainting به آن اضافه شده است | CONDITIONING |
| `negative` | conditioning منفی که اطلاعات latent مربوط به inpainting به آن اضافه شده است | CONDITIONING |
| `latent` | یک تنسور latent نویز پر از صفر با شکل [batch_size, 16, latent_t, latent_h, latent_w] | LATENT |

> این مستند با هوش مصنوعی تهیه شده است. اگر خطایی دیدید یا پیشنهادی برای بهبود دارید، خوشحال می‌شویم مشارکت کنید! [ویرایش در GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDInpaintConditioning/fa.md)

---
**Source fingerprint (SHA-256):** `885e462c0f17a3e9610146a05ba3b9c879db0112d3961c95a83f63ba2cd511f1`
