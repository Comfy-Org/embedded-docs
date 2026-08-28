# TextEncodeAceStepAudio1.5

گره TextEncodeAceStepAudio1.5 فراداده‌های مرتبط با متن و صدا را برای استفاده با مدل AceStepAudio 1.5 آماده می‌کند. این گره برچسب‌های توصیفی، متن آهنگ و پارامترهای موسیقی را دریافت کرده و سپس با استفاده از مدل CLIP آن‌ها را به قالبی شرطی (conditioning) مناسب برای تولید صدا تبدیل می‌کند.

## ورودی‌ها

| پارامتر | توضیحات | نوع داده | الزامی | محدوده |
| --- | --- | --- | --- | --- |
| `clip` | مدل CLIP که برای توکن‌سازی و رمزگذاری متن ورودی استفاده می‌شود. | CLIP | بله | N/A |
| `tags` | برچسب‌های توصیفی برای صدا، مانند سبک، حالت یا سازها. از ورودی چندخطی و پرامپت‌های پویا پشتیبانی می‌کند. | STRING | بله | N/A |
| `lyrics` | متن آهنگ برای قطعه صوتی. از ورودی چندخطی و پرامپت‌های پویا پشتیبانی می‌کند. | STRING | بله | N/A |
| `seed` | یک مقدار seed تصادفی برای تولید قابل تکرار. دارای ویجت control_after_generate است. پیش‌فرض: 0. | INT | خیر | 0 تا 18446744073709551615 |
| `bpm` | ضربان در دقیقه (BPM) برای صدای تولیدشده. پیش‌فرض: 120. | INT | خیر | 10 تا 300 |
| `duration` | مدت زمان دلخواه صدا بر حسب ثانیه. پیش‌فرض: 120.0. | FLOAT | خیر | 0.0 تا 2000.0 |
| `timesignature` | کسر میزان موسیقی. | COMBO | خیر | `"2"`<br>`"3"`<br>`"4"`<br>`"6"` |
| `language` | زبان متن ورودی. پیش‌فرض: "en". | COMBO | خیر | `"ar"`<br>`"az"`<br>`"bg"`<br>`"bn"`<br>`"ca"`<br>`"cs"`<br>`"da"`<br>`"de"`<br>`"el"`<br>`"en"`<br>`"es"`<br>`"fa"`<br>`"fi"`<br>`"fr"`<br>`"he"`<br>`"hi"`<br>`"hr"`<br>`"ht"`<br>`"hu"`<br>`"id"`<br>`"is"`<br>`"it"`<br>`"ja"`<br>`"ko"`<br>`"la"`<br>`"lt"`<br>`"ms"`<br>`"ne"`<br>`"nl"`<br>`"no"`<br>`"pa"`<br>`"pl"`<br>`"pt"`<br>`"ro"`<br>`"ru"`<br>`"sa"`<br>`"sk"`<br>`"sr"`<br>`"sv"`<br>`"sw"`<br>`"ta"`<br>`"te"`<br>`"th"`<br>`"tl"`<br>`"tr"`<br>`"uk"`<br>`"ur"`<br>`"vi"`<br>`"yue"`<br>`"zh"`<br>`"unknown"` |
| `keyscale` | گام موسیقی (ماژور یا مینور). | COMBO | خیر | `"C major"`<br>`"C# major"`<br>`"Db major"`<br>`"D major"`<br>`"D# major"`<br>`"Eb major"`<br>`"E major"`<br>`"F major"`<br>`"F# major"`<br>`"Gb major"`<br>`"G major"`<br>`"G# major"`<br>`"Ab major"`<br>`"A major"`<br>`"A# major"`<br>`"Bb major"`<br>`"B major"`<br>`"C minor"`<br>`"C# minor"`<br>`"Db minor"`<br>`"D minor"`<br>`"D# minor"`<br>`"Eb minor"`<br>`"E minor"`<br>`"F minor"`<br>`"F# minor"`<br>`"Gb minor"`<br>`"G minor"`<br>`"G# minor"`<br>`"Ab minor"`<br>`"A minor"`<br>`"A# minor"`<br>`"Bb minor"`<br>`"B minor"` |
| `generate_audio_codes` | فعال‌سازی LLM که کدهای صوتی را تولید می‌کند. این کار ممکن است کند باشد اما کیفیت صدای تولیدشده را افزایش می‌دهد. اگر به مدل یک مرجع صوتی می‌دهید، این گزینه را خاموش کنید. پیش‌فرض: True. | BOOLEAN | خیر | N/A |
| `cfg_scale` | مقیاس راهنمایی بدون طبقه‌بند (classifier-free guidance). مقادیر بیشتر باعث می‌شوند خروجی بیشتر از پرامپت پیروی کند. پیش‌فرض: 2.0. | FLOAT | خیر | 0.0 تا 100.0 |
| `temperature` | دمای نمونه‌برداری. مقادیر کمتر خروجی را قطعی‌تر می‌کنند. پیش‌فرض: 0.85. | FLOAT | خیر | 0.0 تا 2.0 |
| `top_p` | احتمال نمونه‌برداری هسته‌ای (top-p). پیش‌فرض: 0.9. | FLOAT | خیر | 0.0 تا 2000.0 |
| `top_k` | تعداد توکن‌های با بیشترین احتمال برای در نظر گرفتن (top-k). پیش‌فرض: 0. | INT | خیر | 0 تا 100 |
| `min_p` | آستانه حداقل احتمال برای نمونه‌برداری توکن (min-p). پیش‌فرض: 0.000. | FLOAT | خیر | 0.0 تا 1.0 |

## خروجی‌ها

| نام خروجی | توضیحات | نوع داده |
| --- | --- | --- |
| `CONDITIONING` | داده‌های شرطی (conditioning) که شامل متن رمزگذاری‌شده و پارامترهای صوتی برای مدل AceStepAudio 1.5 است. | CONDITIONING |

> این مستند با هوش مصنوعی تهیه شده است. اگر خطایی دیدید یا پیشنهادی برای بهبود دارید، خوشحال می‌شویم مشارکت کنید! [ویرایش در GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeAceStepAudio1.5/fa.md)

---
**Source fingerprint (SHA-256):** `4bc97ec6220514b71fafde610339f2dca4ded26f68b541ed43ea492f127321f8`
