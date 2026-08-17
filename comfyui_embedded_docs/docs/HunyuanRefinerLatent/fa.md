# HunyuanRefinerLatent

گره HunyuanRefinerLatent ورودی‌های conditioning و latent را برای عملیات پالایش پردازش می‌کند. این گره با ترکیب داده‌های تصویر latent، افزایش نویز را بر روی هر دو conditioning مثبت و منفی اعمال کرده و خروجی latent جدیدی با ابعاد مشخص برای پردازش بیشتر تولید می‌کند.

## ورودی‌ها

| پارامتر | توضیحات | نوع داده | الزامی | محدوده |
| --- | --- | --- | --- | --- |
| `positive` | ورودی conditioning مثبت برای پردازش | CONDITIONING | بله | - |
| `negative` | ورودی conditioning منفی برای پردازش | CONDITIONING | بله | - |
| `latent` | ورودی نمایش نهفته (latent) | LATENT | بله | - |
| `noise_augmentation` | میزان افزایش نویز برای اعمال (پیش‌فرض: 0.10، گام: 0.01، پارامتر پیشرفته) | FLOAT | بله | 0.0 - 1.0 |

## خروجی‌ها

| نام خروجی | توضیحات | نوع داده |
| --- | --- | --- |
| `positive` | conditioning مثبت پردازش‌شده با افزایش نویز اعمال‌شده و الحاق تصویر latent | CONDITIONING |
| `negative` | conditioning منفی پردازش‌شده با افزایش نویز اعمال‌شده و الحاق تصویر latent | CONDITIONING |
| `latent` | latent جدید پر از صفر با همان اندازه دسته و همان سه بُعد آخر با `latent` ورودی، اما با 32 کانال | LATENT |

> این مستند با هوش مصنوعی تهیه شده است. اگر خطایی دیدید یا پیشنهادی برای بهبود دارید، خوشحال می‌شویم مشارکت کنید! [ویرایش در GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanRefinerLatent/fa.md)

---
**Source fingerprint (SHA-256):** `4c5669cf2ad5ba00e176876741b7d8d3f092cc58d2163871a10fd769ee4ff84c`
