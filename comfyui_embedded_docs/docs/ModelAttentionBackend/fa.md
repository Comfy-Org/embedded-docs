# بک‌اند توجه مدل

این گره پیاده‌سازی attention متراکم را برای یک مدل انتخاب می‌کند، مدل را کلون می‌کند، بک‌اند انتخاب‌شده را اعمال می‌کند و کلون وصله‌شده را برمی‌گرداند. هنگام استفاده همراه با Block Sparse Attention، این بک‌اند هر زمان که attention پراکنده غیرفعال یا پشتیبانی‌نشده باشد به کار می‌رود. اگر بک‌اند انتخاب‌شده در دسترس نباشد، گره به‌طور خودکار به attention PyTorch بازمی‌گردد.

## ورودی‌ها

| پارامتر | توضیحات | نوع داده | الزامی | محدوده |
|-----------|-------------|-----------|----------|-------|
| `model` | مدلی که باید وصله شود. | MODEL | بله |  |
| `attention` | بک‌اند attention متراکم برای اعمال. Comfy Kitchen attention از attention کوانتیزه‌شده INT8 استفاده می‌کند و فقط روی GPUهای Nvidia و AMD در دسترس است. پیش‌فرض: "pytorch attention". اگر بک‌اند انتخاب‌شده در دسترس نباشد، attention PyTorch به‌عنوان جایگزین استفاده می‌شود. | COMBO | بله | "pytorch attention"<br>"comfy kitchen attention" |

توجه: گزینه "comfy kitchen attention" فقط زمانی فهرست می‌شود که ماژول attention INT8 مربوط به Comfy Kitchen در محیط فعلی موجود باشد.

## خروجی‌ها

| نام خروجی | توضیحات | نوع داده |
|-------------|-------------|-----------|
| `model` | کلونی از مدل ورودی که بک‌اند attention انتخاب‌شده روی آن اعمال شده است. | MODEL |

> این مستند با هوش مصنوعی تهیه شده است. اگر خطایی دیدید یا پیشنهادی برای بهبود دارید، خوشحال می‌شویم مشارکت کنید! [ویرایش در GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelAttentionBackend/fa.md)

---
**Source fingerprint (SHA-256):** `4f6e4800c2a3bb09b47b7c8f0481e1b6de3070f57234e610df5d3ce60dfdb309`
