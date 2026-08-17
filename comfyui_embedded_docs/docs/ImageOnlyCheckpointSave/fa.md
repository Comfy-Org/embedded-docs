# ذخیره Checkpoint فقط تصویر

گره ImageOnlyCheckpointSave یک فایل checkpoint شامل مدل، رمزگذار بینایی CLIP و VAE ذخیره می‌کند. این گره یک فایل safetensors با پیشوند نام فایل مشخص‌شده ایجاد کرده و آن را در پوشه خروجی ذخیره می‌کند. این گره به‌طور خاص برای ذخیره‌سازی اجزای مدل مرتبط با تصویر در یک فایل checkpoint واحد طراحی شده است.

## ورودی‌ها

| پارامتر | توضیحات | نوع داده | الزامی | بازه |
| --- | --- | --- | --- | --- |
| `model` | مدلی که در checkpoint ذخیره می‌شود | MODEL | بله | - |
| `clip_vision` | رمزگذار بینایی CLIP که در checkpoint ذخیره می‌شود | CLIP_VISION | بله | - |
| `vae` | VAE (خودرمزگذار متغیر) که در checkpoint ذخیره می‌شود | VAE | بله | - |
| `filename_prefix` | پیشوند نام فایل خروجی (پیش‌فرض: "checkpoints/ComfyUI") | STRING | بله | - |
| `prompt` | پارامتر پنهان برای داده‌های prompt گردش کار | PROMPT | خیر | - |
| `extra_pnginfo` | پارامتر پنهان برای فراداده‌های اضافی PNG | EXTRA_PNGINFO | خیر | - |

## خروجی‌ها

| نام خروجی | توضیحات | نوع داده |
| --- | --- | --- |
| - | این گره هیچ خروجی‌ای برنمی‌گرداند | - |

> این مستند با هوش مصنوعی تهیه شده است. اگر خطایی دیدید یا پیشنهادی برای بهبود دارید، خوشحال می‌شویم مشارکت کنید! [ویرایش در GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageOnlyCheckpointSave/fa.md)

---
**Source fingerprint (SHA-256):** `8ff4b3a78d8da523eaa5f784f847e954ba73b4d6037e748dcce592b447fcdee9`
