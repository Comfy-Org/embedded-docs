# StableCascade_EmptyLatentImage

گرهٔ StableCascade_EmptyLatentImage تانسورهای نهفتهٔ خالی برای مدل‌های Stable Cascade ایجاد می‌کند. این گره دو نمایش نهفتهٔ جداگانه تولید می‌کند - یکی برای مرحلهٔ C و دیگری برای مرحلهٔ B - با ابعاد مناسب بر اساس وضوح ورودی و تنظیمات فشرده‌سازی. این گره نقطهٔ شروع خط لولهٔ تولید Stable Cascade را فراهم می‌کند.

## ورودی‌ها

| پارامتر | توضیحات | نوع داده | الزامی | محدوده |
| --- | --- | --- | --- | --- |
| `width` | عرض تصویر خروجی بر حسب پیکسل (پیش‌فرض: 1024، گام: 8) | INT | بله | 256 تا MAX_RESOLUTION |
| `height` | ارتفاع تصویر خروجی بر حسب پیکسل (پیش‌فرض: 1024، گام: 8) | INT | بله | 256 تا MAX_RESOLUTION |
| `compression` | ضریب فشرده‌سازی که ابعاد نهفته را برای مرحله C تعیین می‌کند (پیش‌فرض: 42، گام: 1). این یک پارامتر پیشرفته است. | INT | بله | 4 تا 128 |
| `batch_size` | تعداد نمونه‌های نهفته برای تولید در یک دسته (پیش‌فرض: 1) | INT | خیر | 1 تا 4096 |

## خروجی‌ها

| نام خروجی | توضیحات | نوع داده |
| --- | --- | --- |
| `stage_c` | تانسور نهفتهٔ مرحله C با ابعاد [batch_size, 16, height//compression, width//compression] | LATENT |
| `stage_b` | تانسور نهفتهٔ مرحله B با ابعاد [batch_size, 4, height//4, width//4] | LATENT |

> این مستند با هوش مصنوعی تهیه شده است. اگر خطایی دیدید یا پیشنهادی برای بهبود دارید، خوشحال می‌شویم مشارکت کنید! [ویرایش در GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_EmptyLatentImage/fa.md)

---
**Source fingerprint (SHA-256):** `f336f87d0ec14b3716efda2cfaa194b1f80707d64821bb56ade7d88d9bd5b53f`
