# CLIPTextEncodeControlnet

گره CLIPTextEncodeControlnet با استفاده از مدل CLIP، متن ورودی را پردازش کرده و رمزگذاری متنی حاصل را با داده‌های conditioning موجود ترکیب می‌کند. این گره، بردارهای متنی (embeddings) مشتق‌شده از متن را به‌عنوان پارامترهای cross-attention مخصوص controlnet به هر ورودی conditioning اضافه می‌کند و خروجی conditioning بهبودیافته‌ای برای کاربردهای controlnet تولید می‌کند.

## ورودی‌ها

| پارامتر | توضیحات | نوع داده | الزامی | محدوده |
| --- | --- | --- | --- | --- |
| `clip` | مدل CLIP مورد استفاده برای توکن‌سازی و رمزگذاری متن | CLIP | بله | - |
| `conditioning` | داده‌های conditioning موجود که با رمزگذاری متنی CLIP ترکیب می‌شوند | CONDITIONING | بله | - |
| `متن` | متن ورودی (prompt) که توسط مدل CLIP پردازش می‌شود. از متن چندخطی و promptهای پویا پشتیبانی می‌کند | STRING | بله | - |

**توجه:** هر سه ورودی (`clip`، `conditioning` و `text`) برای عملکرد این گره الزامی هستند. ورودی `text` از متن چندخطی و promptهای پویا برای پردازش انعطاف‌پذیر متن پشتیبانی می‌کند. این گره در کد منبع به‌عنوان آزمایشی (experimental) علامت‌گذاری شده است.

## خروجی‌ها

| نام خروجی | توضیحات | نوع داده |
| --- | --- | --- |
| CONDITIONING | داده‌های conditioning بهبودیافته با پارامترهای cross-attention کنترل‌نت اضافه‌شده (`cross_attn_controlnet` و `pooled_output_controlnet`) که از رمزگذاری متنی CLIP استخراج شده‌اند | CONDITIONING |

> این مستند با هوش مصنوعی تهیه شده است. اگر خطایی دیدید یا پیشنهادی برای بهبود دارید، خوشحال می‌شویم مشارکت کنید! [ویرایش در GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeControlnet/fa.md)

---
**Source fingerprint (SHA-256):** `95a798684ca8734bfff53c7b979b320f6834dc1a9553163d0e567243761000f1`
