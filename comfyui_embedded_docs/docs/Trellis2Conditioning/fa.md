# Trellis2Conditioning

Trellis2Conditioning تصویر ورودی را به داده‌های conditioning برای مدل TRELLIS.2 تبدیل می‌کند. این گره از یک مدل بینایی CLIP برای رمزگذاری تصویر به دو مجموعه ویژگی (در مقیاس‌های 512 و 1024) استفاده می‌کند و آن‌ها را به‌صورت یک جفت conditioning مثبت بسته‌بندی می‌کند؛ همچنین یک جفت conditioning منفیِ پر از صفرِ متناظر ایجاد می‌کند که به‌عنوان مرجع خالی عمل می‌کند.

## ورودی‌ها

| پارامتر | توضیحات | نوع داده | الزامی | محدوده |
|-----------|-------------|-----------|----------|-------|
| `clip_vision_model` | مدل بینایی CLIP که برای رمزگذاری تصویر به ویژگی‌های conditioning استفاده می‌شود. | CLIP_VISION | بله | هر مدل بینایی CLIP موجود |
| `image` | تصویر پیش‌پردازش‌شده از ImageCropToMask (pad_factor=1.0 برای TRELLIS.2). | IMAGE | بله | هر تصویری |

## خروجی‌ها

| نام خروجی | توضیحات | نوع داده |
|-------------|-------------|-----------|
| `positive` | Conditioning شامل ویژگی‌های تصویر رمزگذاری‌شده در مقیاس‌های 512 و 1024 که به‌عنوان conditioning مثبت برای مدل TRELLIS.2 استفاده می‌شود. | CONDITIONING |
| `negative` | Conditioning پر از صفر با همان شکل conditioning مثبت که به‌عنوان مرجع منفی خالی استفاده می‌شود. | CONDITIONING |

> این مستند با هوش مصنوعی تهیه شده است. اگر خطایی دیدید یا پیشنهادی برای بهبود دارید، خوشحال می‌شویم مشارکت کنید! [ویرایش در GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Trellis2Conditioning/fa.md)

---
**Source fingerprint (SHA-256):** `467698e58558ceca9ac633d63aacf360a1eb674ac4ebd47de7423f85e62c0fe6`
