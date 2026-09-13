# BriaRelight

این گره با استفاده از Bria فضای نورپردازی و جهت نور یک تصویر را تغییر می‌دهد. تصویر توسط Bria دوباره رندر می‌شود، بنابراین نتیجه با ورودی در سطح پیکسل هم‌تراز نیست؛ کل کادر با حدود ۱ مگاپیکسل بازتولید می‌شود.

## ورودی‌ها

### ورودی‌های مشترک

| پارامتر | توضیحات | نوع داده | الزامی | بازه |
|-----------|-------------|-----------|----------|-------|
| `image` | تصویری که نورپردازی آن تغییر می‌کند. هر کانال آلفا پیش از بارگذاری تصویر حذف می‌شود. | IMAGE | بله | - |
| `light_type` | فضای نورپردازی برای اعمال. | COMBO | بله | `"midday"`<br>`"blue hour light"`<br>`"low-angle sunlight"`<br>`"sunrise light"`<br>`"spotlight on subject"`<br>`"overcast light"`<br>`"soft overcast daylight lighting"`<br>`"cloud-filtered lighting"`<br>`"fog-diffused lighting"`<br>`"moonlight lighting"`<br>`"starlight nighttime"`<br>`"soft bokeh lighting"`<br>`"harsh studio lighting"` |
| `light_direction` | جهتی که نور از آن می‌آید. فضاهای نورپردازی سخت مانند midday، spotlight on subject و harsh studio lighting بیشترین واکنش را به آن نشان می‌دهند. | COMBO | بله | `"front"`<br>`"side"`<br>`"bottom"`<br>`"top-down"` |
| `moderation` | تنظیمات بازبینی محتوا. برای نمایش گزینه‌های بازبینی، `"true"` را انتخاب کنید، یا برای اجرا بدون آن‌ها `"false"` را انتخاب کنید. | DYNAMIC_COMBO | بله | `"false"`<br>`"true"` |

### ورودی‌های بازبینی محتوا

این گزینه‌ها زمانی ظاهر می‌شوند که `moderation` روی `"true"` تنظیم شده باشد.

| پارامتر | توضیحات | نوع داده | الزامی | بازه |
|-----------|-------------|-----------|----------|-------|
| `visual_input_moderation` | بازبینی محتوای تصویر ورودی را فعال می‌کند. پیش‌فرض: false. | BOOLEAN | خیر | `true`<br>`false` |
| `visual_output_moderation` | بازبینی محتوای تصویر خروجی تولیدشده را فعال می‌کند. پیش‌فرض: false. | BOOLEAN | خیر | `true`<br>`false` |

توجه: Bria کل کادر را با حدود ۱ مگاپیکسل دوباره رندر می‌کند، بنابراین نتیجه با ورودی در سطح پیکسل هم‌تراز نیست.

## خروجی‌ها

| نام خروجی | توضیحات | نوع داده |
|-------------|-------------|-----------|
| `image` | تصویر نورپردازی‌شدهٔ بازگردانده‌شده توسط Bria. | IMAGE |
| `structured_prompt` | توضیح ساخت‌یافتهٔ تصویر ویرایش‌شده، برای ویرایش بعدی با Bria FIBO Image Edit. | STRING |

> این مستند با هوش مصنوعی تهیه شده است. اگر خطایی دیدید یا پیشنهادی برای بهبود دارید، خوشحال می‌شویم مشارکت کنید! [ویرایش در GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaRelight/fa.md)

---
**Source fingerprint (SHA-256):** `21fbe2186c99a7e8d99d5659ac25c3ab1a757492916dba4135487d4b293cb4f6`
