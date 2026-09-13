# StableCascade_StageB_Conditioning

گره StableCascade_StageB_Conditioning داده‌های conditioning را برای تولید Stable Cascade Stage B آماده می‌کند؛ این کار با ترکیب اطلاعات conditioning موجود و نمایش نهفته پیشین تولیدشده توسط Stage C انجام می‌شود. این گره هر ورودی conditioning را کپی کرده و نمونه‌های نهفته Stage C را در آن ذخیره می‌کند تا مراحل تولید بعدی بتوانند از این اطلاعات پیشین برای نتایج منسجم‌تر استفاده کنند.

## ورودی‌ها

| پارامتر | توضیحات | نوع داده | الزامی | محدوده |
| --- | --- | --- | --- | --- |
| `conditioning` | داده‌های conditioning که باید با اطلاعات پیشین Stage C اصلاح شوند. هر ورودی در فهرست کپی شده و نمونه‌های Stage C به آن داده می‌شود. | CONDITIONING | بله | - |
| `stage_c` | نمایش نهفته از Stage C. مقدار `samples` آن به‌عنوان اطلاعات پیشین افزوده‌شده به conditioning استفاده می‌شود. | LATENT | بله | - |

## خروجی‌ها

| نام خروجی | توضیحات | نوع داده |
| --- | --- | --- |
| `CONDITIONING` | داده‌های conditioning اصلاح‌شده که اطلاعات پیشین Stage C در آن یکپارچه شده است. | CONDITIONING |

> این مستند با هوش مصنوعی تهیه شده است. اگر خطایی دیدید یا پیشنهادی برای بهبود دارید، خوشحال می‌شویم مشارکت کنید! [ویرایش در GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_StageB_Conditioning/fa.md)

---
**Source fingerprint (SHA-256):** `3154457773465e5b93221b6d83d2064b565cb653403e12e88615652c7832d1e8`
