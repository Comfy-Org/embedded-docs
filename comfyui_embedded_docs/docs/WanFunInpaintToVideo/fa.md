> این مستند با هوش مصنوعی تهیه شده است. اگر خطایی دیدید یا پیشنهادی برای بهبود دارید، خوشحال می‌شویم مشارکت کنید! [ویرایش در GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanFunInpaintToVideo/fa.md)

### گره WanFunInpaintToVideo

گره `WanFunInpaintToVideo` با ترمیم (inpainting) بین تصاویر شروع و پایان، دنباله‌های ویدیویی ایجاد می‌کند. این گره با دریافت conditioning مثبت و منفی به همراه فریم‌های تصویری اختیاری، لاتنت‌های ویدیو را تولید می‌کند. این گره تولید ویدیو را با پارامترهای قابل تنظیم ابعاد و طول مدیریت می‌کند.

## ورودی‌ها

| پارامتر | نوع داده | ضروری | محدوده | توضیحات |
|---------|----------|-------|--------|---------|
| `positive` | CONDITIONING | بله | - | راهنمای conditioning مثبت برای تولید ویدیو |
| `negative` | CONDITIONING | بله | - | راهنمای conditioning منفی برای جلوگیری از تولید در ویدیو |
| `vae` | VAE | بله | - | مدل VAE برای عملیات رمزگذاری/رمزگشایی |
| `width` | INT | بله | 16 تا MAX_RESOLUTION | عرض ویدیوی خروجی بر حسب پیکسل (پیش‌فرض: 832، گام: 16) |
| `height` | INT | بله | 16 تا MAX_RESOLUTION | ارتفاع ویدیوی خروجی بر حسب پیکسل (پیش‌فرض: 480، گام: 16) |
| `length` | INT | بله | 1 تا MAX_RESOLUTION | تعداد فریم‌های دنباله ویدیو (پیش‌فرض: 81، گام: 4) |
| `batch_size` | INT | بله | 1 تا 4096 | تعداد ویدیوهای تولید شده در یک دسته (پیش‌فرض: 1) |
| `clip_vision_output` | CLIP_VISION_OUTPUT | خیر | - | خروجی vision CLIP اختیاری برای conditioning اضافی |
| `start_image` | IMAGE | خیر | - | فریم تصویر شروع اختیاری برای تولید ویدیو |
| `end_image` | IMAGE | خیر | - | فریم تصویر پایان اختیاری برای تولید ویدیو |

## خروجی‌ها

| نام خروجی | نوع داده | توضیحات |
|-----------|----------|---------|
| `positive` | CONDITIONING | خروجی conditioning مثبت پردازش‌شده |
| `negative` | CONDITIONING | خروجی conditioning منفی پردازش‌شده |
| `latent` | LATENT | نمایش لاتنت ویدیوی تولیدشده |

---
**Source fingerprint (SHA-256):** `bbc5c2614f5fc21877345b3f01686ea57bee5108cdb253fb5dbf4b2cce9e59dd`
