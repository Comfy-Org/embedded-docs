# Text Encode MOSS-Image Edit

یک دستور ویرایش را همراه با تصاویر مرجع به شرطی‌سازی (conditioning) برای LoRA ویرایش MOSS-Image رمزگذاری می‌کند. خروجی را به‌عنوان شرطی‌سازی مثبت متصل کنید و یک نمونه دوم با همان مراجع برای شرطی‌سازی منفی اجرا کنید. مراجع با همان اندازه‌ای که می‌رسند استفاده می‌شوند؛ بنابراین پیش از اتصال آن‌ها را مقیاس‌بندی کنید. این گره در ComfyUI آزمایشی علامت‌گذاری شده است. بدون VAE تصاویر فقط به رمزگذار متن می‌روند.

## ورودی‌ها

| پارامتر | توضیحات | نوع داده | الزامی | بازه |
| --- | --- | --- | --- | --- |
| `clip` | مدل CLIP که دستور را توکن‌بندی و رمزگذاری می‌کند. | CLIP | بله | - |
| `prompt` | دستوری که ویرایش را توصیف می‌کند. از متن چندخطی و پرامپت‌های پویا پشتیبانی می‌کند. | STRING | بله | هر متنی |
| `vae` | VAEای که برای رمزگذاری تصاویر مرجع به لاتنت‌های مرجع استفاده می‌شود. اختیاری: بدون آن تصاویر فقط به رمزگذار متن می‌روند.| VAE | خیر | - |
| `edit_format` | چیدمانی که LoRA ویرایش با آن آموزش دیده است. روش لاتنت‌های مرجع و اینکه رمزگذار متن نیز مراجع را می‌بیند یا نه را انتخاب می‌کند. | COMBO | بله | `"ai-toolkit"`<br>`"ai-toolkit (kv_cache off)"`<br>`"Moss-Image-Edit"` |
| `images` | جایگاه قابل‌افزایش: یک یا چند تصویر مرجع (`image_1`، `image_2`، ...) را متصل کنید. هر تصویر با همان اندازه‌ای که می‌رسد استفاده می‌شود، کانال آلفای آن حذف می‌شود و با VAE به یک لاتنت مرجع رمزگذاری می‌شود. با اتصال VAE کانال آلفا حذف و هر تصویر به لاتنت مرجع رمزگذاری می‌شود؛ بدون VAE تصاویر فقط به رمزگذار متن می‌روند.| IMAGE | بله | 1 یا بیشتر تصویر |
| `image_strength` | میزان توجه مدل به تصاویری که رمزگذار متن می‌بیند را مقیاس می‌دهد (قالب‌های ai-toolkit یا بدون VAE): 0 نادیده، 1 بدون تغییر، بالاتر از 1 تأکید. پیشرفته. پیش‌فرض: 1.0. | FLOAT | بله | 0.0 to 100.0 (step 0.05) |

**توجه:** With `"ai-toolkit"` and `"ai-toolkit (kv_cache off)"`, or when no VAE is connected and `image_strength` is above 0, the text encoder also sees every reference, downscaled to at most 384x384 pixels and preceded by a `Picture N:` marker in the prompt, so the instruction can refer to them by number. With `"Moss-Image-Edit"` and a VAE connected, the references reach the model only as reference latents and the text encoder sees the instruction alone. `"ai-toolkit (kv_cache off)"` additionally keeps the references attending to the image being generated, so they are recomputed on every sampling step.

## خروجی‌ها

| نام خروجی | توضیحات | نوع داده |
| --- | --- | --- |
| `conditioning` | دستور رمزگذاری‌شده همراه با لاتنت‌های مرجع و روش متناظر لاتنت‌های مرجع پیوست‌شده. | CONDITIONING |

> این مستند با هوش مصنوعی تهیه شده است. اگر خطایی دیدید یا پیشنهادی برای بهبود دارید، خوشحال می‌شویم مشارکت کنید! [ویرایش در GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeMOSSImageEdit/fa.md)

---
**Source fingerprint (SHA-256):** `673f098df6a8e466a5c8060009f446eac8f7556311a870de626c5f4bfc3ab196`
