> این مستند با هوش مصنوعی تهیه شده است. اگر خطایی دیدید یا پیشنهادی برای بهبود دارید، خوشحال می‌شویم مشارکت کنید! [ویرایش در GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanRefinerLatent/fa.md)

گره `HunyuanRefinerLatent`، ورودی‌های conditioning و latent را برای عملیات refinement پردازش می‌کند. این گره با اعمال نویزافزایی (noise augmentation) بر روی هر دو conditioning مثبت و منفی و ترکیب داده‌های تصویر latent، یک خروجی latent جدید با ابعاد مشخص برای پردازش‌های بعدی تولید می‌کند.

## ورودی‌ها

| پارامتر | نوع داده | ضروری | محدوده | توضیحات |
|---------|----------|-------|--------|---------|
| `مثبت` | CONDITIONING | بله | - | ورودی conditioning مثبت برای پردازش |
| `منفی` | CONDITIONING | بله | - | ورودی conditioning منفی برای پردازش |
| `latent` | LATENT | بله | - | نمایش ورودی latent |
| `افزایش نویز` | FLOAT | بله | 0.0 - 1.0 | میزان نویزافزایی اعمال‌شده (پیش‌فرض: 0.10) |

## خروجی‌ها

| نام خروجی | نوع داده | توضیحات |
|-----------|----------|---------|
| `مثبت` | CONDITIONING | conditioning مثبت پردازش‌شده با نویزافزایی اعمال‌شده و الحاق تصویر latent |
| `منفی` | CONDITIONING | conditioning منفی پردازش‌شده با نویزافزایی اعمال‌شده و الحاق تصویر latent |
| `latent` | LATENT | خروجی latent جدید با ابعاد [batch_size, 32, height, width, channels] |

---
**Source fingerprint (SHA-256):** `f097b58f1948e5c0801f81b51a5189619695a6afa189368aff4c64b126fc5ce5`
