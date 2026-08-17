# ReferenceLatent

این گره، latent راهنما را برای یک مدل ویرایش تنظیم می‌کند. داده‌های conditioning و یک ورودی latent اختیاری دریافت می‌کند و سپس conditioning را تغییر می‌دهد تا اطلاعات latent مرجع را شامل شود. اگر مدل از آن پشتیبانی کند، می‌توانید چند گره ReferenceLatent را زنجیره کنید تا چند تصویر مرجع تنظیم کنید.

## ورودی‌ها

| پارامتر | توضیحات | نوع داده | الزامی | محدوده |
| --- | --- | --- | --- | --- |
| `conditioning` | داده‌های conditioning که باید با اطلاعات latent مرجع اصلاح شوند | CONDITIONING | بله | - |
| `latent` | داده‌های latent اختیاری برای استفاده به عنوان مرجع برای مدل ویرایش | LATENT | خیر | - |

## خروجی‌ها

| نام خروجی | توضیحات | نوع داده |
| --- | --- | --- |
| `output` | داده‌های conditioning اصلاح‌شده حاوی اطلاعات latent مرجع | CONDITIONING |

> این مستند با هوش مصنوعی تهیه شده است. اگر خطایی دیدید یا پیشنهادی برای بهبود دارید، خوشحال می‌شویم مشارکت کنید! [ویرایش در GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReferenceLatent/fa.md)

---
**Source fingerprint (SHA-256):** `40b02df8ac436480f478fcfa929cc2e13181954507f4bdcd70aade051a25f7d5`
