# بارگذاری CLIP

گرهٔ CLIPLoader یک مدل انکودر متن (CLIP، T5 یا مشابه) را از یک فایل بارگذاری می‌کند و آن را برای استفاده در سایر گره‌هایی که باید پرامپت‌های متنی را به بازنمایی‌های عددی تبدیل کنند، در دسترس قرار می‌دهد. این گره از طیف گسترده‌ای از معماری‌های مدل پشتیبانی می‌کند که هرکدام به نوع انکودر مشخصی نیاز دارند.

## ورودی‌ها

| پارامتر | توضیحات | نوع داده | الزامی | محدوده |
|-----------|-------------|-----------|----------|-------|
| `clip_name` | نام فایل مدل انکودر متن که باید بارگذاری شود. این باید فایلی در پوشهٔ `ComfyUI/models/text_encoders/` باشد. | STRING | بله | فهرست فایل‌های یافت‌شده در پوشهٔ `text_encoders` |
| `type` | نوع معماری مدلی که بارگذاری می‌شود. این تعیین می‌کند کدام نوع انکودر مشخص استفاده شود (پیش‌فرض: `"stable_diffusion"`). | COMBO | بله | `"stable_diffusion"`<br>`"stable_cascade"`<br>`"sd3"`<br>`"stable_audio"`<br>`"mochi"`<br>`"ltxv"`<br>`"pixart"`<br>`"cosmos"`<br>`"lumina2"`<br>`"wan"`<br>`"hidream"`<br>`"chroma"`<br>`"ace"`<br>`"omnigen2"`<br>`"qwen_image"`<br>`"hunyuan_image"`<br>`"flux2"`<br>`"ovis"`<br>`"longcat_image"`<br>`"cogvideox"`<br>`"lens"`<br>`"pixeldit"`<br>`"ideogram4"`<br>`"boogu"`<br>`"krea2"`<br>`"joyimage"`<br>`"mage"`<br>`"minimax"`<br>`"yue2"` |
| `device` | دستگاهی که مدل روی آن بارگذاری می‌شود. `"default"` در صورت وجود از GPU استفاده می‌کند، در حالی که `"cpu"` بارگذاری روی CPU را اجباری می‌کند. این یک گزینهٔ پیشرفته است (پیش‌فرض: `"default"`). | COMBO | خیر | `"default"`<br>`"cpu"` |

### نگاشت‌های پشتیبانی‌شدهٔ نوع به انکودر

پارامتر `type` انکودر درست را برای یک معماری مدل مشخص انتخاب می‌کند. موارد زیر نگاشت‌های رایج هستند:

| نوع | انکودر |
|------|---------|
| stable_diffusion | clip-l |
| stable_cascade | clip-g |
| sd3 | t5 xxl / clip-g / clip-l |
| stable_audio | t5 base |
| mochi | t5 xxl |
| cogvideox | t5 xxl (پدینگ ۲۲۶ توکن) |
| cosmos | old t5 xxl |
| lumina2 | gemma 2 2B |
| wan | umt5 xxl |
| hidream | llama-3.1 (توصیه‌شده) یا t5 |
| omnigen2 | qwen vl 2.5 3B |
| joyimage | qwen3-vl 8B |
| lens | gpt-oss-20b |
| pixeldit | gemma 2 2B elm |
| minimax | MiniMax H3 Qwen3-VL یا Music3 Qwen/RVQ |

## خروجی‌ها

| نام خروجی | توضیحات | نوع داده |
|-------------|-------------|-----------|
| `CLIP` | مدل انکودر متنی بارگذاری‌شده، آماده برای اتصال به سایر گره‌ها برای انکودینگ متن و شرطی‌سازی. | CLIP |

> این مستند با هوش مصنوعی تهیه شده است. اگر خطایی دیدید یا پیشنهادی برای بهبود دارید، خوشحال می‌شویم مشارکت کنید! [ویرایش در GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPLoader/fa.md)

---
**Source fingerprint (SHA-256):** `6df608d500520d9414acd82d9fd509b1e211a8385202cefd5579e8a8f397bc64`
