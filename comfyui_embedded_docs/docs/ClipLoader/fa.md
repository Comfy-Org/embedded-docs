> این مستند با هوش مصنوعی تهیه شده است. اگر خطایی دیدید یا پیشنهادی برای بهبود دارید، خوشحال می‌شویم مشارکت کنید! [ویرایش در GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPLoader/fa.md)

گره CLIPLoader یک مدل رمزگذار متن (CLIP، T5 یا مشابه) را از یک فایل بارگذاری می‌کند و آن را برای استفاده در سایر گره‌هایی که نیاز به تبدیل پرامپت‌های متنی به نمایش‌های عددی دارند، در دسترس قرار می‌دهد. این گره از طیف گسترده‌ای از معماری‌های مدل پشتیبانی می‌کند که هرکدام به نوع رمزگذار خاصی نیاز دارند.

## ورودی‌ها

| پارامتر | نوع داده | اجباری | محدوده | توضیحات |
|-----------|-----------|----------|-------|-------------|
| `clip_name` | STRING | بله | فهرست فایل‌های موجود در پوشه `text_encoders` | نام فایل مدل رمزگذار متن برای بارگذاری. این فایل باید در دایرکتوری `ComfyUI/models/text_encoders/` یا `ComfyUI/models/clip/` قرار داشته باشد. |
| `type` | STRING | بله | `"stable_diffusion"`<br>`"stable_cascade"`<br>`"sd3"`<br>`"stable_audio"`<br>`"mochi"`<br>`"ltxv"`<br>`"pixart"`<br>`"cosmos"`<br>`"lumina2"`<br>`"wan"`<br>`"hidream"`<br>`"chroma"`<br>`"ace"`<br>`"omnigen2"`<br>`"qwen_image"`<br>`"hunyuan_image"`<br>`"flux2"`<br>`"ovis"`<br>`"longcat_image"`<br>`"cogvideox"` | نوع معماری مدل در حال بارگذاری. این پارامتر تعیین می‌کند که کدام نوع رمزگذار خاص استفاده شود. مقدار پیش‌فرض `"stable_diffusion"` است. |
| `device` | STRING | خیر | `"default"`<br>`"cpu"` | دستگاهی که مدل روی آن بارگذاری می‌شود. `"default"` در صورت وجود از GPU استفاده می‌کند، در حالی که `"cpu"` بارگذاری روی CPU را اجباری می‌کند. این یک گزینه پیشرفته است (پیش‌فرض: `"default"`). |

### نگاشت‌های پشتیبانی‌شده نوع به رمزگذار

پارامتر `type` رمزگذار مناسب را برای یک معماری مدل مشخص انتخاب می‌کند. موارد زیر نگاشت‌های رایج هستند:

| نوع | رمزگذار |
|------|---------|
| stable_diffusion | clip-l |
| stable_cascade | clip-g |
| sd3 | t5 xxl / clip-g / clip-l |
| stable_audio | t5 base |
| mochi | t5 xxl |
| cogvideox | t5 xxl (padding 226-توکن) |
| cosmos | t5 xxl قدیمی |
| lumina2 | gemma 2 2B |
| wan | umt5 xxl |
| hidream | llama-3.1 (توصیه‌شده) یا t5 |
| omnigen2 | qwen vl 2.5 3B |

## خروجی‌ها

| نام خروجی | نوع داده | توضیحات |
|-------------|-----------|-------------|
| `clip` | CLIP | مدل رمزگذار متن بارگذاری‌شده، آماده برای اتصال به سایر گره‌ها برای رمزگذاری متن و شرطی‌سازی. |

---
**Source fingerprint (SHA-256):** `1051bfe5570dff81719682cb09938bae4c03e94e0e72f7a2be84867cccb48017`
