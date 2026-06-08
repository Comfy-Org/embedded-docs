گره VOIDInpaintConditioning داده‌های شرطی‌سازی مورد نیاز برای inpainting با مدل‌های CogVideoX را آماده می‌کند. این گره یک ویدئوی منبع و یک quadmask از پیش‌پردازش‌شده را دریافت کرده، آن‌ها را از طریق VAE رمزگذاری می‌کند و در یک سیگنال شرطی‌سازی ۳۲ کاناله ترکیب می‌کند که مدل از آن برای پر کردن نواحی پوشیده‌شده استفاده می‌کند.

## ورودی‌ها

| پارامتر | توضیحات | نوع داده | ضروری | محدوده |
| --- | --- | --- | --- | --- |
| `positive` | شرطی‌سازی مثبت که با اطلاعات نهان inpainting تقویت می‌شود | CONDITIONING | بله | - |
| `negative` | شرطی‌سازی منفی که با اطلاعات نهان inpainting تقویت می‌شود | CONDITIONING | بله | - |
| `vae` | مدل VAE مورد استفاده برای رمزگذاری ماسک و ویدئوی ماسک‌شده به فضای نهان | VAE | بله | - |
| `video` | فریم‌های ویدئوی منبع [T, H, W, 3] | IMAGE | بله | - |
| `quadmask` | quadmask از پیش‌پردازش‌شده از گره VOIDQuadmaskPreprocess [T, H, W] | MASK | بله | - |
| `width` | عرضی که ویدئو و ماسک به آن تغییر اندازه می‌دهند (پیش‌فرض: ۶۷۲) | INT | بله | ۱۶ تا MAX_RESOLUTION (گام: ۸) |
| `height` | ارتفاعی که ویدئو و ماسک به آن تغییر اندازه می‌دهند (پیش‌فرض: ۳۸۴) | INT | بله | ۱۶ تا MAX_RESOLUTION (گام: ۸) |
| `length` | تعداد فریم‌های پیکسلی برای پردازش. برای CogVideoX-Fun-V1.5 (patch_size_t=2)، latent_t باید زوج باشد — طول‌هایی که latent_t فرد تولید می‌کنند به پایین گرد می‌شوند (مثلاً ۴۹ → ۴۵) (پیش‌فرض: ۴۵) | INT | بله | ۱ تا MAX_RESOLUTION (گام: ۱) |
| `batch_size` | اندازه دسته برای خروجی نهان نویز (پیش‌فرض: ۱) | INT | بله | ۱ تا ۶۴ |

## خروجی‌ها

| نام خروجی | توضیحات | نوع داده |
| --- | --- | --- |
| `positive` | شرطی‌سازی مثبت با اطلاعات نهان inpainting اضافه‌شده | CONDITIONING |
| `negative` | شرطی‌سازی منفی با اطلاعات نهان inpainting اضافه‌شده | CONDITIONING |
| `latent` | تنسور نهان نویز پر از صفر با شکل [batch_size, 16, latent_t, latent_h, latent_w] | LATENT |

> این مستند با هوش مصنوعی تهیه شده است. اگر خطایی دیدید یا پیشنهادی برای بهبود دارید، خوشحال می‌شویم مشارکت کنید! [ویرایش در GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDInpaintConditioning/fa.md)

---
**Source fingerprint (SHA-256):** `a1fe36376d7930286c7a288f261dcf2961d6b13cc412d1a0d42af8a4f9ebeeaf`
