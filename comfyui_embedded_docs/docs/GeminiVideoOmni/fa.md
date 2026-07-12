# Google Gemini Omni (ویدیو)

تولید ویدیو همراه با صدا از یک پرامپت متنی با استفاده از مدل Gemini Omni Flash گوگل. به صورت اختیاری می‌توانید تصاویر و/یا ویدیوهای مرجع برای راهنمایی یا ویرایش نتیجه ارائه دهید. طول مورد نظر (۳ تا ۱۰ ثانیه) و نسبت تصویر (۱۶:۹ یا ۹:۱۶) را مستقیماً در پرامپت ذکر کنید.

## ورودی‌ها

| پارامتر | توضیحات | نوع داده | الزامی | محدوده |
|-----------|-------------|-----------|----------|-------|
| `model` | مدل ویدیویی Gemini که برای تولید ویدیو استفاده می‌شود. | MODEL | Yes | "Omni Flash" |
| `seed` | Seed تعیین می‌کند که node دوباره اجرا شود یا خیر؛ نتایج صرف‌نظر از seed غیرقطعی هستند. | INT | Yes | 0 to 2147483647 |
| `prompt` | The text prompt describing the video to generate. Must be at least one non-whitespace character after stripping leading/trailing whitespace. | STRING | Yes | Minimum 1 character after stripping whitespace |
| `images` | Optional reference images to guide the video generation. Maximum of 14 images total. | IMAGE | No | Multiple images allowed (max 14) |
| `videos` | Optional reference videos to guide or edit the video generation. Maximum of 3 videos, each up to 10 seconds. | VIDEO | No | Multiple videos allowed (max 3, each max 10s) |
| `temperature` | Controls randomness in generation (default: 1.0). | FLOAT | No | 0.0 to 2.0 |
| `top_p` | Nucleus sampling parameter (default: 0.95). | FLOAT | No | 0.0 to 1.0 |

## خروجی‌ها

| نام خروجی | توضیحات | نوع داده |
|-------------|-------------|-----------|
| `VIDEO` | The generated video with audio from the Gemini model. | VIDEO |
| `STRING` | Any text response from the model, such as reasoning or explanations. | STRING |

> این مستند با هوش مصنوعی تهیه شده است. اگر خطایی دیدید یا پیشنهادی برای بهبود دارید، خوشحال می‌شویم مشارکت کنید! [ویرایش در GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiVideoOmni/fa.md)

---
**Source fingerprint (SHA-256):** `046842b7ec736283bba355aaa038b02fcf2416020f5f7aee7b0150d2a05bcbe6`
