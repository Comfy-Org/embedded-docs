# اعمال Conditioning مدل SeedVR2

`conditioning` مثبت و منفی را از یک latent مربوط به VAE برای استفاده با مدل SeedVR2 می‌سازد. latent و ساختار مدل ورودی را اعتبارسنجی می‌کند، یک کانال ماسک به latent اضافه می‌کند و هر دو خروجی conditioning را بازمی‌گرداند.

## ورودی‌ها

| پارامتر | توضیحات | نوع داده | الزامی | محدوده |
|-----------|-------------|-----------|----------|-------|
| `model` | مدل SeedVR2. | MODEL | بله | - |
| `vae_conditioning` | latent مربوط به VAE مدل SeedVR2 که conditioning از آن ساخته می‌شود (نام نمایشی: latent). | LATENT | بله | - |

توجه: latent ورودی `vae_conditioning` باید یک تنسور ۵بعدی با چیدمان کانال‌اول در Comfy (B, C, T, H, W) باشد، که در آن C تعداد کانال مورد انتظار VAE مدل SeedVR2 است. اگر latent ۵بعدی نباشد، اگر تعداد کانال‌ها مطابقت نداشته باشد، یا اگر تنسور به‌نظر در چیدمان کانال‌آخر باشد، گره خطا می‌دهد. ورودی `model` باید ساختار مورد انتظار SeedVR2 را داشته باشد؛ گره مدل انتشار داخلی آن را تعیین می‌کند و conditioning مثبت و منفی آن را می‌خواند. در داخل، گره یک کانال ماسک ثابت به latent اضافه می‌کند و conditioning حاصل را به هر دو خروجی conditioning مثبت و منفی متصل می‌کند.

## خروجی‌ها

| نام خروجی | توضیحات | نوع داده |
|-------------|-------------|-----------|
| `positive` | conditioning مثبت برای نمونه‌گیری. | CONDITIONING |
| `negative` | conditioning منفی برای نمونه‌گیری. | CONDITIONING |

> این مستند با هوش مصنوعی تهیه شده است. اگر خطایی دیدید یا پیشنهادی برای بهبود دارید، خوشحال می‌شویم مشارکت کنید! [ویرایش در GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SeedVR2Conditioning/fa.md)

---
**Source fingerprint (SHA-256):** `28e508bdd776e2e3f5f2f93bfc29a1a1d1c34a11dbdc7f421d197ddbfa85f0f5`
