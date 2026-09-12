# ModelSamplingSD3

This node applies Stable Diffusion 3 style sampling settings to a model. It makes a copy of the model and replaces its sampling method with a flow-based sampling configuration that uses the given `shift` value, which controls how the sampling distribution is shaped.

## ورودی‌ها

| پارامتر | توضیحات | نوع داده | الزامی | محدوده |
| --- | --- | --- | --- | --- |
| `مدل` | مدل ورودی برای اعمال پارامترهای نمونه‌گیری SD3 روی آن | MODEL | بله | - |
| `شیفت` | پارامتر `shift` نمونه‌گیری را کنترل می‌کند (پیش‌فرض: 3.0) | FLOAT | بله | 0.0 - 100.0 (step: 0.01) |

نکته: مقدار `shift` همراه با یک ضریب داخلی ثابت 1000 اعمال می‌شود. اگر مدل اصلی تنظیم مقیاس نویز داشته باشد، آن مقدار به مدل تغییر‌یافته منتقل می‌شود. مدل اصلی تغییر نمی‌کند؛ یک نسخه کلون‌شده و وصله‌شده بازگردانده می‌شود.

## خروجی‌ها

| نام خروجی | توضیحات | نوع داده |
| --- | --- | --- |
| `model` | مدل تغییر‌یافته با پارامترهای نمونه‌گیری SD3 اعمال‌شده | MODEL |

> این مستند با هوش مصنوعی تهیه شده است. اگر خطایی دیدید یا پیشنهادی برای بهبود دارید، خوشحال می‌شویم مشارکت کنید! [ویرایش در GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingSD3/fa.md)

---
**Source fingerprint (SHA-256):** `a77e38c2cebf6f21f841a953ec5c59096eaf60ffc205c24f34f635e54c5718cb`
