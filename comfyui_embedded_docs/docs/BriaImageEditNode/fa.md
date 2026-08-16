# ویرایش تصویر Bria

گره Bria FIBO Image Edit به شما امکان می‌دهد تا یک تصویر موجود را با استفاده از یک دستور متنی ویرایش کنید. این گره تصویر و prompt شما را به Bria API ارسال می‌کند، که از مدل FIBO برای تولید نسخه‌ی جدید و ویرایش‌شده‌ای از تصویر بر اساس درخواست شما استفاده می‌کند. همچنین می‌توانید یک mask ارائه دهید تا ویرایش‌ها را به ناحیه‌ی خاصی محدود کنید.
## ورودیها

### ورودیهای مشترک

| پارامتر | توضیحات | نوع داده | اجباری | محدوده |
|---|---|---|---|---|
| `model` | نسخه مدلی که برای ویرایش تصویر استفاده می‌شود. | COMBO | بله | `"FIBO"` |
| `image` | تصویر ورودی که می‌خواهید ویرایش کنید. | IMAGE | بله | - |
| `prompt` | دستورالعمل ویرایش تصویر (پیش‌فرض: خالی). | STRING | بله | - |
| `negative_prompt` | متنی که توصیف می‌کند چه چیزهایی را نمی‌خواهید در تصویر ویرایش‌شده ظاهر شوند (پیش‌فرض: خالی). | STRING | بله | - |
| `structured_prompt` | رشته‌ای شامل دستور ویرایش ساختاریافته در قالب JSON. به‌جای prompt معمولی برای کنترل دقیق و برنامه‌محور از این استفاده کنید (پیش‌فرض: خالی). | STRING | بله | - |
| `seed` | عددی که برای مقداردهی اولیه تولید تصادفی استفاده می‌شود و نتایج قابل تکرار را تضمین می‌کند (پیش‌فرض: 1). | INT | بله | 1 to 2147483647 |
| `guidance_scale` | مقدار بالاتر باعث می‌شود تصویر با دقت بیشتری از prompt پیروی کند (پیش‌فرض: 3.0). | FLOAT | بله | 3.0 to 5.0 |
| `steps` | تعداد گام‌های نویززدایی که مدل انجام خواهد داد (پیش‌فرض: 50). | INT | بله | 20 to 50 |
| `moderation` | تنظیمات پالایش. انتخاب `"true"` گزینه‌های پالایش بیشتری را برای محتوای prompt، ورودی بصری و خروجی بصری نشان می‌دهد. | DYNAMIC_COMBO | بله | `"false"`<br>`"true"` |
| `mask` | اگر این پارامتر حذف شود، ویرایش بر روی کل تصویر اعمال می‌شود. | MASK | خیر | - |

### ورودیهای نظارت

| پارامتر | توضیحات | نوع داده | اجباری | محدوده |
|---|---|---|---|---|
| `prompt_content_moderation` | prompt_content_moderation (پیش‌فرض: false) | BOOLEAN | خیر | `true`<br>`false` |
| `visual_input_moderation` | visual_input_moderation (پیش‌فرض: false) | BOOLEAN | خیر | `true`<br>`false` |
| `visual_output_moderation` | visual_output_moderation (پیش‌فرض: true) | BOOLEAN | خیر | `true`<br>`false` |

## خروجیها

| نام خروجی | توضیحات | نوع داده |
|---|---|---|
| `IMAGE` | The edited image returned by the Bria API. | IMAGE |
| `structured_prompt` | The structured prompt used or generated during the editing process. | STRING |

> این مستند با هوش مصنوعی تهیه شده است. اگر خطایی دیدید یا پیشنهادی برای بهبود دارید، خوشحال می‌شویم مشارکت کنید! [ویرایش در GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaImageEditNode/fa.md)

---
**Source fingerprint (SHA-256):** `e66aaa563a82407408f25b289011a491c8b158822fc2db8912daf73731750081`
