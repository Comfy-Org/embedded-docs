# LTXVConditioning

گره LTXVConditioning اطلاعات نرخ فریم را به هر دو ورودی conditioning مثبت و منفی برای مدل‌های تولید ویدیو اضافه می‌کند. این گره داده‌های conditioning موجود را گرفته و مقدار نرخ فریم مشخص‌شده را بر روی هر دو مجموعه conditioning اعمال می‌کند و آن‌ها را برای پردازش مدل ویدیویی مناسب می‌سازد.

## ورودی‌ها

| پارامتر | توضیحات | نوع داده | الزامی | محدوده |
| --- | --- | --- | --- | --- |
| `positive` | ورودی conditioning مثبت که اطلاعات نرخ فریم را دریافت خواهد کرد | CONDITIONING | بله | - |
| `negative` | ورودی conditioning منفی که اطلاعات نرخ فریم را دریافت خواهد کرد | CONDITIONING | بله | - |
| `frame_rate` | مقدار نرخ فریم برای اعمال روی هر دو مجموعه conditioning (پیش‌فرض: 25.0) | FLOAT | بله | 0.0 - 1000.0 |

## خروجی‌ها

| نام خروجی | توضیحات | نوع داده |
| --- | --- | --- |
| `positive` | conditioning مثبت با اطلاعات نرخ فریم اعمال‌شده | CONDITIONING |
| `negative` | conditioning منفی با اطلاعات نرخ فریم اعمال‌شده | CONDITIONING |

> این مستند با هوش مصنوعی تهیه شده است. اگر خطایی دیدید یا پیشنهادی برای بهبود دارید، خوشحال می‌شویم مشارکت کنید! [ویرایش در GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVConditioning/fa.md)

---
**Source fingerprint (SHA-256):** `c8546b691329f2934995f97a6db2e1393d2928bf1a7438fd079d52f87bee1c35`
