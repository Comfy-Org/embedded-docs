# PiD Conditioning

یک تصویر latent و یک مقدار سیگمای تخریب (degrade sigma) را به داده CONDITIONING می‌چسباند. این برای رمزگشایی یا بزرگ‌نمایی PiD (Pixel-in-Detail) استفاده می‌شود و به شما امکان می‌دهد میزان تخریب latent را قبل از پردازش کنترل کنید.

## ورودی‌ها

| پارامتر | توضیحات | نوع داده | الزامی | محدوده |
|-----------|-------------|-----------|----------|-------|
| `positive` | داده‌های CONDITIONING که latent و سیگمای تخریب به آن متصل می‌شوند. | CONDITIONING | بله | - |
| `latent` | latent (از VAEEncode یا یک KSampler) که به conditioning متصل می‌شود. | LATENT | بله | - |
| `latent_format` | قالب latent. latentهای Flux1 (16 کاناله) و Flux2 (128 کاناله) به‌صورت خودکار از بُعد کانال در حالت «flux» شناسایی می‌شوند. برای SD3 (16 کاناله)، SDXL (4 کاناله) یا QwenImage (16 کاناله)، به‌صورت دستی انتخاب کنید (پیش‌فرض: «flux»). | COMBO | بله | `"flux"`<br>`"sd3"`<br>`"sdxl"`<br>`"qwenimage"` |
| `degrade_sigma` | میزان تخریب اعمال‌شده. 0 به معنای latent تمیز است. این مقدار را افزایش دهید تا خروجی‌های latent آسیب‌دیده نویززدایی شوند (پیش‌فرض: 0.0). | FLOAT | بله | 0.0 تا 1.0 (گام: 0.01) |

توجه: وقتی `latent_format` روی `"flux"` تنظیم شده باشد، گره به‌صورت خودکار نوع latent را از بُعد کانال تشخیص می‌دهد: 128 کانال به‌عنوان latentهای Flux2 و 16 کانال به‌عنوان latentهای Flux1 در نظر گرفته می‌شوند.

## خروجی‌ها

| نام خروجی | توضیحات | نوع داده |
|-------------|-------------|-----------|
| `CONDITIONING` | داده‌های CONDITIONING اصلی با مقادیر latent و سیگمای تخریب متصل‌شده. | CONDITIONING |

> این مستند با هوش مصنوعی تهیه شده است. اگر خطایی دیدید یا پیشنهادی برای بهبود دارید، خوشحال می‌شویم مشارکت کنید! [ویرایش در GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PiDConditioning/fa.md)

---
**Source fingerprint (SHA-256):** `24f613b33e7872cb35f458aa5794a3cc4d37ceaecd43725039edef75f4a512bc`
