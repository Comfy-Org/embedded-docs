# StableCascade_StageB_Conditioning

گره StableCascade_StageB_Conditioning داده‌های conditioning را برای تولید در مرحله B از Stable Cascade آماده می‌کند؛ این کار با ترکیب اطلاعات شرطی موجود با بازنمایی‌های نهان قبلی از مرحله C انجام می‌شود. این گره هر ورودی conditioning را کپی کرده و نمونه‌های نهان مرحله C را به آن اضافه می‌کند و بدین ترتیب فرایند تولید می‌تواند از اطلاعات پیشین برای خروجی‌های منسجم‌تر بهره‌مند شود.

## ورودی‌ها

| پارامتر | توضیحات | نوع داده | الزامی | محدوده |
| --- | --- | --- | --- | --- |
| `شرط‌گذاری` | داده‌های conditioning که باید با اطلاعات پیشین مرحله C اصلاح شوند | CONDITIONING | بله | - |
| `stage_c` | بازنمایی نهان از مرحله C حاوی نمونه‌های پیشین برای conditioning | LATENT | بله | - |

## خروجی‌ها

| نام خروجی | توضیحات | نوع داده |
| --- | --- | --- |
| `CONDITIONING` | داده‌های conditioning اصلاح‌شده با اطلاعات پیشین مرحله C یکپارچه‌شده | CONDITIONING |

> این مستند با هوش مصنوعی تهیه شده است. اگر خطایی دیدید یا پیشنهادی برای بهبود دارید، خوشحال می‌شویم مشارکت کنید! [ویرایش در GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_StageB_Conditioning/fa.md)

---
**Source fingerprint (SHA-256):** `3154457773465e5b93221b6d83d2064b565cb653403e12e88615652c7832d1e8`
