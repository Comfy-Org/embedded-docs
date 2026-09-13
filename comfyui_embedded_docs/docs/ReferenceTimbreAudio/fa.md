# ReferenceTimbreAudio

این گره صدای مرجع را برای فرایند «ace step 1.5» تنظیم می‌کند. یک ورودی conditioning و به‌صورت اختیاری یک نمایش latent از صدا دریافت می‌کند، سپس آن داده latent را به conditioning متصل می‌کند تا گره‌های بعدی بتوانند از آن به‌عنوان latentهای تیمبر صدای مرجع استفاده کنند. این گره به‌عنوان آزمایشی علامت‌گذاری شده است.

## ورودی‌ها

| پارامتر | توضیحات | نوع داده | الزامی | محدوده |
| --- | --- | --- | --- | --- |
| `conditioning` | داده conditioning که اطلاعات صدای مرجع به آن متصل می‌شود. | CONDITIONING | بله |  |
| `latent` | یک نمایش latent اختیاری از صدای مرجع (پیش‌فرض: None). هنگامی که ارائه شود، نمونه‌های آن به conditioning به‌عنوان latentهای تیمبر صدای مرجع افزوده می‌شوند. | LATENT | خیر |  |

## خروجی‌ها

| نام خروجی | توضیحات | نوع داده |
| --- | --- | --- |
| `conditioning` | داده conditioning اصلاح‌شده که اکنون در صورت ارائه ورودی اختیاری `latent`، شامل latentهای تیمبر صدای مرجع است. | CONDITIONING |

> این مستند با هوش مصنوعی تهیه شده است. اگر خطایی دیدید یا پیشنهادی برای بهبود دارید، خوشحال می‌شویم مشارکت کنید! [ویرایش در GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReferenceTimbreAudio/fa.md)

---
**Source fingerprint (SHA-256):** `2ddccb7676fc45a5324ba32dde0cd2f8f24388ceec20c88a475e1aa9d4276be0`
