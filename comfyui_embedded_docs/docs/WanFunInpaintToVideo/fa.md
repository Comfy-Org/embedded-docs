# WanFunInpaintToVideo

گره WanFunInpaintToVideo داده‌های conditioning و latent را برای تولید ویدئو به سبک inpainting آماده می‌کند و از تصویر شروع و تصویر پایان اختیاری برای هدایت نتیجه استفاده می‌کند. این گره با عبور دادن conditioning، VAE و فریم‌های تصویر ارائه‌شده از همان منطق مورد استفاده برای تولید ویدئو با فریم اول و آخر کار می‌کند و conditioning به‌روزرسانی‌شده به‌همراه یک latent خالی برای نمونه‌گیری برمی‌گرداند.

## ورودی‌ها

| پارامتر | توضیحات | نوع داده | الزامی | محدوده |
| --- | --- | --- | --- | --- |
| `positive` | پرامپت‌های conditioning مثبت برای تولید ویدئو | CONDITIONING | بله | - |
| `negative` | پرامپت‌های conditioning منفی برای پرهیز در تولید ویدئو | CONDITIONING | بله | - |
| `vae` | مدل VAE مورد استفاده برای رمزگذاری و رمزگشایی فریم‌های ویدئو | VAE | بله | - |
| `width` | عرض ویدئوی خروجی بر حسب پیکسل (پیش‌فرض: 832، گام: 16) | INT | بله | 16 تا MAX_RESOLUTION |
| `height` | ارتفاع ویدئوی خروجی بر حسب پیکسل (پیش‌فرض: 480، گام: 16) | INT | بله | 16 تا MAX_RESOLUTION |
| `length` | تعداد فریم‌ها در دنباله ویدئو (پیش‌فرض: 81، گام: 4) | INT | بله | 1 تا MAX_RESOLUTION |
| `batch_size` | تعداد ویدئوها برای تولید در یک دسته (پیش‌فرض: 1) | INT | بله | 1 تا 4096 |
| `clip_vision_output` | خروجی CLIP vision اختیاری که به‌عنوان conditioning برای تصویر شروع استفاده می‌شود | CLIP_VISION_OUTPUT | خیر | - |
| `start_image` | تصویر فریم شروع اختیاری برای تولید ویدئو | IMAGE | خیر | - |
| `end_image` | تصویر فریم پایان اختیاری برای تولید ویدئو | IMAGE | خیر | - |

## خروجی‌ها

| نام خروجی | توضیحات | نوع داده |
| --- | --- | --- |
| `positive` | خروجی conditioning مثبت پردازش‌شده | CONDITIONING |
| `negative` | خروجی conditioning منفی پردازش‌شده | CONDITIONING |
| `latent` | نمایش latent ویدئوی تولیدشده | LATENT |

> این مستند با هوش مصنوعی تهیه شده است. اگر خطایی دیدید یا پیشنهادی برای بهبود دارید، خوشحال می‌شویم مشارکت کنید! [ویرایش در GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanFunInpaintToVideo/fa.md)

---
**Source fingerprint (SHA-256):** `70b58e961c5df12f94183245ce320197439b2505b47d0bb3ff643b25c9fe6175`
