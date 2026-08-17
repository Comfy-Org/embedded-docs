# بارگذاری CLIP

گره CLIPLoader یک مدل رمزگذار متن (مانند CLIP، T5 یا مشابه) را از یک فایل بارگذاری می‌کند و آن را برای استفاده در سایر گره‌هایی که نیاز به تبدیل پرامپت‌های متنی به بازنمایی‌های عددی دارند، در دسترس قرار می‌دهد. این گره از طیف گسترده‌ای از معماری‌های مدل پشتیبانی می‌کند که هر یک به نوع رمزگذار خاصی نیاز دارد.

## ورودی‌ها

| پارامتر | توضیحات | نوع داده | الزامی | بازه |
|-----------|-------------|-----------|----------|-------|
| `clip_name` | نام فایل مدل رمزگذار متنی که باید بارگذاری شود. این فایل باید در پوشه `ComfyUI/models/text_encoders/` قرار داشته باشد. | COMBO | بله | فهرست فایل‌های موجود در پوشه `text_encoders` |
| `type` | نوع معماری مدلی که در حال بارگذاری است. این گزینه مشخص می‌کند از کدام گونه رمزگذار استفاده شود (پیش‌فرض: `"stable_diffusion"`). | COMBO | بله | `"stable_diffusion"`<br>`"stable_cascade"`<br>`"sd3"`<br>`"stable_audio"`<br>`"mochi"`<br>`"ltxv"`<br>`"pixart"`<br>`"cosmos"`<br>`"lumina2"`<br>`"wan"`<br>`"hidream"`<br>`"chroma"`<br>`"ace"`<br>`"omnigen2"`<br>`"qwen_image"`<br>`"hunyuan_image"`<br>`"flux2"`<br>`"ovis"`<br>`"longcat_image"`<br>`"cogvideox"`<br>`"lens"`<br>`"pixeldit"`<br>`"ideogram4"`<br>`"boogu"`<br>`"krea2"`<br>`"joyimage"`<br>`"mage"`<br>`"minimax"` |
| `device` | دستگاهی که مدل روی آن بارگذاری می‌شود. `"default"` از دستگاه پیش‌فرض (معمولاً GPU در صورت موجود بودن) استفاده می‌کند، در حالی که `"cpu"` بارگذاری روی CPU را اجباری می‌کند. این یک گزینه پیشرفته است (پیش‌فرض: `"default"`). | COMBO | خیر | `"default"`<br>`"cpu"` |

### نگاشت‌های نوع به رمزگذار پشتیبانی‌شده

پارامتر `type` رمزگذار صحیح را برای یک معماری مدل معین انتخاب می‌کند. نگاشت‌های رایج زیر در توضیحات گره فهرست شده‌اند:

| نوع | رمزگذار |
|------|---------|
| stable_diffusion | clip-l |
| stable_cascade | clip-g |
| sd3 | t5 xxl / clip-g / clip-l |
| stable_audio | t5 base |
| mochi | t5 xxl |
| cogvideox | t5 xxl (با پدینگ ۲۲۶ توکن) |
| cosmos | t5 xxl قدیمی |
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
| `clip` | مدل رمزگذار متن بارگذاری‌شده، آماده اتصال به سایر گره‌ها برای رمزگذاری متن و شرطی‌سازی (conditioning). | CLIP |

> این مستند با هوش مصنوعی تهیه شده است. اگر خطایی دیدید یا پیشنهادی برای بهبود دارید، خوشحال می‌شویم مشارکت کنید! [ویرایش در GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPLoader/fa.md)

---
**Source fingerprint (SHA-256):** `7c1586d01410d319468f7c8c153ef0717280804add868ba57bff0c6539fb5dd9`
