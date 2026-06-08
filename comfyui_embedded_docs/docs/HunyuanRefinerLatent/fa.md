گره `HunyuanRefinerLatent`، ورودی‌های conditioning و latent را برای عملیات refinement پردازش می‌کند. این گره با اعمال نویزافزایی (noise augmentation) بر روی هر دو conditioning مثبت و منفی و ترکیب داده‌های تصویر latent، یک خروجی latent جدید با ابعاد مشخص برای پردازش‌های بعدی تولید می‌کند.

## ورودی‌ها

| پارامتر | توضیحات | نوع داده | ضروری | محدوده |
| --- | --- | --- | --- | --- |
| `مثبت` | ورودی conditioning مثبت برای پردازش | CONDITIONING | بله | - |
| `منفی` | ورودی conditioning منفی برای پردازش | CONDITIONING | بله | - |
| `latent` | نمایش ورودی latent | LATENT | بله | - |
| `افزایش نویز` | میزان نویزافزایی اعمال‌شده (پیش‌فرض: 0.10) | FLOAT | بله | 0.0 - 1.0 |

## خروجی‌ها

| نام خروجی | توضیحات | نوع داده |
| --- | --- | --- |
| `مثبت` | conditioning مثبت پردازش‌شده با نویزافزایی اعمال‌شده و الحاق تصویر latent | CONDITIONING |
| `منفی` | conditioning منفی پردازش‌شده با نویزافزایی اعمال‌شده و الحاق تصویر latent | CONDITIONING |
| `latent` | خروجی latent جدید با ابعاد [batch_size, 32, height, width, channels] | LATENT |

> این مستند با هوش مصنوعی تهیه شده است. اگر خطایی دیدید یا پیشنهادی برای بهبود دارید، خوشحال می‌شویم مشارکت کنید! [ویرایش در GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanRefinerLatent/fa.md)

---
**Source fingerprint (SHA-256):** `f097b58f1948e5c0801f81b51a5189619695a6afa189368aff4c64b126fc5ce5`
