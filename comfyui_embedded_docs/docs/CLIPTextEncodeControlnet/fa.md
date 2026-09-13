# CLIPTextEncodeControlnet

گره CLIP Text Encode (Controlnet) یک پرامپت متنی را با یک مدل CLIP رمزگذاری می‌کند و رمزگذاری متنی حاصل را به داده‌های conditioning موجود می‌افزاید. این گره جاسازی‌های متنی را به‌صورت پارامترهای cross-attention مربوط به ControlNet درون هر ورودی conditioning ذخیره می‌کند، بنابراین conditioning بازگردانده‌شده حاوی آن اطلاعات اضافی ControlNet است.

## ورودی‌ها

| پارامتر | توضیحات | نوع داده | الزامی | محدوده |
| --- | --- | --- | --- | --- |
| `clip` | مدل CLIP مورد استفاده برای توکن‌سازی و رمزگذاری متن | CLIP | بله | - |
| `conditioning` | داده‌های conditioning موجود برای ترکیب با رمزگذاری متن CLIP | CONDITIONING | بله | - |
| `text` | پرامپت متنی که باید توسط مدل CLIP پردازش شود. از متن چندخطی و پرامپت‌های پویا پشتیبانی می‌کند | STRING | بله | - |

**توجه:** هر سه ورودی (`clip`، `conditioning` و `text`) برای عملکرد این گره الزامی هستند. ورودی `text` از متن چندخطی و پرامپت‌های پویا برای پردازش انعطاف‌پذیر متن پشتیبانی می‌کند. این گره در کد منبع به‌عنوان آزمایشی علامت‌گذاری شده است.

## خروجی‌ها

| نام خروجی | توضیحات | نوع داده |
| --- | --- | --- |
| `CONDITIONING` | داده‌های conditioning بهبودیافته با پارامترهای cross-attention افزوده‌شده ControlNet (`cross_attn_controlnet` و `pooled_output_controlnet`) که از رمزگذاری متن CLIP به دست آمده‌اند | CONDITIONING |

> این مستند با هوش مصنوعی تهیه شده است. اگر خطایی دیدید یا پیشنهادی برای بهبود دارید، خوشحال می‌شویم مشارکت کنید! [ویرایش در GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeControlnet/fa.md)

---
**Source fingerprint (SHA-256):** `95a798684ca8734bfff53c7b979b320f6834dc1a9553163d0e567243761000f1`
