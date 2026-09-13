# ذخیره شرطی‌سازی

این گره یک conditioning واحد را به‌صورت فایل safetensors در پوشه خروجی ذخیره می‌کند. فایل ذخیره‌شده را می‌توان به پوشه models/embeddings منتقل کرد و بعداً با Load Conditioning بارگذاری نمود، برای مثال برای رد کردن text encoder. گره conditioning را بدون تغییر عبور می‌دهد تا همچنان بتوان از آن در ادامه گردش‌کار استفاده کرد.

## ورودی‌ها

| پارامتر | توضیحات | نوع داده | الزامی | محدوده |
|-----------|-------------|-----------|----------|-------|
| `conditioning` | conditioning موردنظر برای ذخیره. فقط یک ورودی conditioning پشتیبانی می‌شود. | CONDITIONING | بله | - |
| `filename_prefix` | پیشوندی که برای ساخت نام فایل خروجی استفاده می‌شود. فایل با یک شمارنده عددی الحاق‌شده در پوشه خروجی نوشته می‌شود. پیش‌فرض: `conditioning/ComfyUI` | STRING | بله | - |

**نکته‌ها:**

- اگر ورودی `conditioning` بیش از یک ورودی داشته باشد (برای مثال پس از ترکیب conditioningها)، گره خطایی ایجاد می‌کند: "Save Conditioning supports a single conditioning entry, save it before combining."
- گزینه‌های conditioning که از نوع tensor، لیست/تاپل tensor، بولی، عدد صحیح، عدد اعشاری یا رشته هستند، همراه با conditioning ذخیره می‌شوند. گزینه‌هایی که `None` هستند نادیده گرفته می‌شوند. هر نوع گزینه دیگری خطایی ایجاد می‌کند مبنی بر اینکه گزینه قابل ذخیره نیست.

## خروجی‌ها

| نام خروجی | توضیحات | نوع داده |
|-------------|-------------|-----------|
| `conditioning` | همان conditioning ورودی، بدون تغییر. | CONDITIONING |

> این مستند با هوش مصنوعی تهیه شده است. اگر خطایی دیدید یا پیشنهادی برای بهبود دارید، خوشحال می‌شویم مشارکت کنید! [ویرایش در GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveConditioning/fa.md)

---
**Source fingerprint (SHA-256):** `07b7d2be5262c4782f237138d034b130322507e62ae8775b9c94634df8e7a3fa`
