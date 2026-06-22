# ذخیره Checkpoint فقط تصویر

گره ImageOnlyCheckpointSave یک فایل checkpoint شامل مدل، رمزگذار دیداری CLIP و VAE ذخیره می‌کند. این گره یک فایل safetensors با پیشوند نام فایل مشخص‌شده ایجاد کرده و آن را در پوشه خروجی ذخیره می‌کند. این گره به‌طور خاص برای ذخیره‌سازی هم‌زمان اجزای مدل مرتبط با تصویر در یک فایل checkpoint طراحی شده است.

## ورودی‌ها

| پارامتر | توضیحات | نوع داده | الزامی | محدوده |
| --- | --- | --- | --- | --- |
| `مدل` | مدلی که در checkpoint ذخیره می‌شود | MODEL | بله | - |
| `clip_vision` | رمزگذار دیداری CLIP که در checkpoint ذخیره می‌شود | CLIP_VISION | بله | - |
| `vae` | VAE (رمزگذار خودکار وردشی) که در checkpoint ذخیره می‌شود | VAE | بله | - |
| `پیشوند نام فایل` | پیشوند نام فایل خروجی (پیش‌فرض: "checkpoints/ComfyUI") | STRING | بله | - |
| `prompt` | پارامتر پنهان برای داده‌های prompt workflow | PROMPT | خیر | - |
| `extra_pnginfo` | پارامتر پنهان برای فراداده‌های اضافی PNG | EXTRA_PNGINFO | خیر | - |

## خروجی‌ها

| نام خروجی | توضیحات | نوع داده |
| --- | --- | --- |
| - | این گره هیچ خروجی بازنمی‌گرداند | - |

> این مستند با هوش مصنوعی تهیه شده است. اگر خطایی دیدید یا پیشنهادی برای بهبود دارید، خوشحال می‌شویم مشارکت کنید! [ویرایش در GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageOnlyCheckpointSave/fa.md)

---
**Source fingerprint (SHA-256):** `d2a26933f0e2fcccf3c57f50038fb40ef5b23d00ccdd2e1d215b3cb78203b9fd`
