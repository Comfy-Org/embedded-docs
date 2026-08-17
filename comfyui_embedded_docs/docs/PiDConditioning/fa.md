# PiD Conditioning

یک تصویر نهان (latent) و مقدار سیگمای تخریب (degrade sigma) را به داده‌ی CONDITIONING متصل می‌کند. این کار برای کدگشایی PiD (Pixel-in-Detail) یا بزرگ‌نمایی استفاده می‌شود و به شما امکان می‌دهد میزان تخریب latent را قبل از پردازش کنترل کنید.

## ورودی‌ها

| پارامتر | توضیحات | نوع داده | الزامی | محدوده |
|---------|-----------|-----------|--------|-------|
| `positive` | داده‌ی conditioning که latent و سیگمای تخریب به آن متصل می‌شوند. | CONDITIONING | بله | - |
| `latent` | تصویر نهان (از VAEEncode یا یک KSampler) که به conditioning متصل می‌شود. | LATENT | بله | - |
| `latent_format` | فرمت latent. latentهای Flux1 (16 کاناله) و Flux2 (128 کاناله) به‌طور خودکار از بُعد کانال در حالت "flux" تشخیص داده می‌شوند. برای SD3 (16 کاناله)، SDXL (4 کاناله)، یا QwenImage (16 کاناله)، به‌صورت دستی انتخاب کنید (پیش‌فرض: "flux"). | COMBO | بله | `"flux"`<br>`"sd3"`<br>`"sdxl"`<br>`"qwenimage"` |
| `degrade_sigma` | 0 = latent تمیز. افزایش دهید تا خروجی‌های نهان تخریب‌شده پاکسازی شوند (پیش‌فرض: 0.0). | FLOAT | بله | 0.0 تا 1.0 (گام: 0.01) |

توجه: وقتی `latent_format` روی "flux" باشد، گره به‌طور خودکار بر اساس بُعد کانال، نوع latent را تشخیص می‌دهد: Flux1 (16 کانال) یا Flux2 (128 کانال). اگر latent پردازش‌شده 5 بُعد داشته باشد، فقط اولین برش در امتداد آخرین بُعد استفاده می‌شود.

## خروجی‌ها

| نام خروجی | توضیحات | نوع داده |
|-------------|-----------|-----------|
| `CONDITIONING` | داده‌ی conditioning اصلی به همراه مقادیر latent و degrade sigma متصل‌شده. | CONDITIONING |

> این مستند با هوش مصنوعی تهیه شده است. اگر خطایی دیدید یا پیشنهادی برای بهبود دارید، خوشحال می‌شویم مشارکت کنید! [ویرایش در GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PiDConditioning/fa.md)

---
**Source fingerprint (SHA-256):** `24f613b33e7872cb35f458aa5794a3cc4d37ceaecd43725039edef75f4a512bc`
