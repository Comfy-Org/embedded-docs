# ModelSamplingStableCascade

گره ModelSamplingStableCascade با اعمال مقدار شیفت بر پارامترهای نمونه‌برداری، نمونه‌برداری Stable Cascade را روی مدل اعمال می‌کند. این گره یک کلون اصلاح‌شده از مدل ورودی با پیکربندی نمونه‌برداری سفارشی برای تولید Stable Cascade ایجاد می‌کند.

## ورودی‌ها

| پارامتر | توضیحات | نوع داده | الزامی | محدوده |
| --- | --- | --- | --- | --- |
| `model` | مدل ورودی که نمونه‌برداری Stable Cascade روی آن اعمال می‌شود | MODEL | بله | - |
| `shift` | مقدار شیفتی که به پارامترهای نمونه‌برداری اعمال می‌شود (پیش‌فرض: 2.0) | FLOAT | بله | 0.0 - 100.0 (گام: 0.01) |

## خروجی‌ها

| نام خروجی | توضیحات | نوع داده |
| --- | --- | --- |
| `model` | مدل اصلاح‌شده با اعمال نمونه‌برداری Stable Cascade | MODEL |

> این مستند با هوش مصنوعی تهیه شده است. اگر خطایی دیدید یا پیشنهادی برای بهبود دارید، خوشحال می‌شویم مشارکت کنید! [ویرایش در GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingStableCascade/fa.md)

---
**Source fingerprint (SHA-256):** `358681a7c698d4335cde60780d5a8b134b75df4ea40102bf51544c53bbb08c42`
