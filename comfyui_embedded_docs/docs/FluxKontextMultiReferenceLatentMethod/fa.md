# روش مرجع مدل ویرایش

گره FluxKontextMultiReferenceLatentMethod داده‌های شرطی‌سازی را با ذخیره یک روش انتخابی برای latentهای مرجع در داخل آن به‌روزرسانی می‌کند. روش ذخیره‌شده سپس هنگام پردازش latentهای مرجع در مراحل تولید بعدی استفاده می‌شود. این گره آزمایشی علامت‌گذاری شده و به سیستم شرطی‌سازی Flux تعلق دارد.

## ورودی‌ها

| پارامتر | توضیحات | نوع داده | الزامی | محدوده |
| --- | --- | --- | --- | --- |
| `شرط‌گذاری` | داده‌های شرطی‌سازی که باید با روش latentهای مرجع اصلاح شوند | CONDITIONING | بله | - |
| `روش latent مرجع` | روشی که برای پردازش latentهای مرجع استفاده می‌شود. اگر مقداری شامل "uxo" یا "uso" انتخاب شود، پیش از ذخیره‌سازی به "uxo" تبدیل می‌شود. این پارامتر به‌عنوان پیشرفته علامت‌گذاری شده است. | COMBO | بله | `"offset"`<br>`"index"`<br>`"uxo/uno"`<br>`"index_timestep_zero"`<br>`"index_timestep_zero_isolated"`<br>`"index_timestep_zero_text_start"` |

## خروجی‌ها

| نام خروجی | توضیحات | نوع داده |
| --- | --- | --- |
| `conditioning` | داده‌های شرطی‌سازی اصلاح‌شده که روش latentهای مرجع روی آن‌ها اعمال شده است | CONDITIONING |

> این مستند با هوش مصنوعی تهیه شده است. اگر خطایی دیدید یا پیشنهادی برای بهبود دارید، خوشحال می‌شویم مشارکت کنید! [ویرایش در GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxKontextMultiReferenceLatentMethod/fa.md)

---
**Source fingerprint (SHA-256):** `de2e3d34f9e47a90ff37300489bffef8082eb92deefbc2ce338b17b0d853ac77`
