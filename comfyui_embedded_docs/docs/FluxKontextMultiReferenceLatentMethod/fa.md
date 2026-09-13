# روش مرجع مدل ویرایش

گره FluxKontextMultiReferenceLatentMethod داده‌های شرطی‌سازی را با ذخیره یک روش انتخابی برای latentهای مرجع در داخل آن به‌روزرسانی می‌کند. روش ذخیره‌شده سپس هنگام پردازش latentهای مرجع در مراحل تولید بعدی استفاده می‌شود. این گره آزمایشی علامت‌گذاری شده و به سیستم شرطی‌سازی Flux تعلق دارد.

## ورودی‌ها

| پارامتر | توضیحات | نوع داده | الزامی | محدوده |
| --- | --- | --- | --- | --- |
| `conditioning` | داده‌های شرطی‌سازی که باید با روش latentهای مرجع اصلاح شوند | CONDITIONING | بله | - |
| `reference_latents_method` | روشی که برای پردازش latentهای مرجع استفاده می‌شود. اگر مقداری شامل "uxo" یا "uso" انتخاب شود، پیش از ذخیره‌سازی به "uxo" تبدیل می‌شود. این پارامتر به‌عنوان پیشرفته علامت‌گذاری شده است. | COMBO | بله | `"offset"`<br>`"index"`<br>`"uxo/uno"`<br>`"index_timestep_zero"` |

## خروجی‌ها

| نام خروجی | توضیحات | نوع داده |
| --- | --- | --- |
| `conditioning` | داده‌های شرطی‌سازی اصلاح‌شده که روش latentهای مرجع روی آن‌ها اعمال شده است | CONDITIONING |

> این مستند با هوش مصنوعی تهیه شده است. اگر خطایی دیدید یا پیشنهادی برای بهبود دارید، خوشحال می‌شویم مشارکت کنید! [ویرایش در GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxKontextMultiReferenceLatentMethod/fa.md)

---
**Source fingerprint (SHA-256):** `cbe069d0c9f8adbf7f8c909b1cd644d9cd3730e934f0e5856213ff06fa8ecc56`
