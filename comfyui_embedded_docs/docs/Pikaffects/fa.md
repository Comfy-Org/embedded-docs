# Pikaffects

### مرور کلی

گره Pikaffects ویدیوهایی با افکت‌های بصری متنوع بر روی یک تصویر ورودی تولید می‌کند. این گره از API تولید ویدیوی Pika برای تبدیل تصاویر ثابت به ویدیوهای متحرک با افکت‌های خاص مانند ذوب شدن، انفجار یا شناور شدن استفاده می‌کند. برای دسترسی به سرویس Pika، این گره به یک کلید API و توکن احراز هویت نیاز دارد.

### ورودی‌ها

| پارامتر | توضیحات | نوع داده | الزامی | محدوده |
| --- | --- | --- | --- | --- |
| `image` | تصویر مرجع برای اعمال Pikaffect. | IMAGE | بله | - |
| `pikaffect` | افکت بصری خاص برای اعمال روی تصویر (پیش‌فرض: "Cake-ify"). | COMBO | بله | "Cake-ify"<br>"Crumble"<br>"Crush"<br>"Decapitate"<br>"Deflate"<br>"Dissolve"<br>"Explode"<br>"Eye-pop"<br>"Inflate"<br>"Levitate"<br>"Melt"<br>"Peel"<br>"Poke"<br>"Squish"<br>"Ta-da"<br>"Tear" |
| `prompt_text` | توضیحات متنی برای هدایت تولید ویدیو. | STRING | بله | - |
| `negative_prompt` | توضیحات متنی از مواردی که باید در ویدیوی تولید شده اجتناب شود. | STRING | بله | - |
| `seed` | مقدار تصادفی seed برای نتایج قابل تکرار. | INT | بله | 0 تا 4294967295 |

### خروجی‌ها

| نام خروجی | توضیحات | نوع داده |
| --- | --- | --- |
| `output` | ویدیوی تولید شده با Pikaffect اعمال شده. | VIDEO |

> این مستند با هوش مصنوعی تهیه شده است. اگر خطایی دیدید یا پیشنهادی برای بهبود دارید، خوشحال می‌شویم مشارکت کنید! [ویرایش در GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Pikaffects/fa.md)

---
**Source fingerprint (SHA-256):** `68ebbee465763d463bf73678254eed38d37ebacb1c62d386bbe66961deffd5a8`
