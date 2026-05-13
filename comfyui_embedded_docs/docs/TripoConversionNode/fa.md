> این مستند با هوش مصنوعی تهیه شده است. اگر خطایی دیدید یا پیشنهادی برای بهبود دارید، خوشحال می‌شویم مشارکت کنید! [ویرایش در GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoConversionNode/fa.md)

### TripoConversionNode

گره TripoConversionNode مدل‌های سه‌بعدی را بین فرمت‌های مختلف فایل با استفاده از API سرویس Tripo تبدیل می‌کند. این گره یک شناسه وظیفه (task ID) از عملیات قبلی Tripo (تولید مدل، ریگینگ یا ریتارگتینگ) دریافت کرده و مدل حاصل را با گزینه‌های مختلف خروجی به فرمت دلخواه شما تبدیل می‌کند.

## ورودی‌ها

| پارامتر | نوع داده | اجباری | محدوده | توضیحات |
|-----------|-----------|----------|-------|-------------|
| `original_model_task_id` | MODEL_TASK_ID,RIG_TASK_ID,RETARGET_TASK_ID | بله | MODEL_TASK_ID<br>RIG_TASK_ID<br>RETARGET_TASK_ID | شناسه وظیفه از یک عملیات قبلی Tripo (تولید مدل، ریگینگ یا ریتارگتینگ) |
| `format` | COMBO | بله | GLTF<br>USDZ<br>FBX<br>OBJ<br>STL<br>3MF | فرمت فایل مقصد برای مدل سه‌بعدی تبدیل‌شده |
| `quad` | BOOLEAN | خیر | True/False | آیا مثلث‌ها به چهارضلعی تبدیل شوند (پیش‌فرض: False) |
| `face_limit` | INT | خیر | 1- تا 2000000 | حداکثر تعداد وجه در مدل خروجی، از 1- برای بدون محدودیت استفاده کنید (پیش‌فرض: 1-) |
| `texture_size` | INT | خیر | 128 تا 4096 | اندازه بافت‌های خروجی بر حسب پیکسل (پیش‌فرض: 4096) |
| `texture_format` | COMBO | خیر | BMP<br>DPX<br>HDR<br>JPEG<br>OPEN_EXR<br>PNG<br>TARGA<br>TIFF<br>WEBP | فرمت بافت‌های خروجی (پیش‌فرض: JPEG) |
| `force_symmetry` | BOOLEAN | خیر | True/False | آیا تقارن روی مدل اعمال شود (پیش‌فرض: False) |
| `flatten_bottom` | BOOLEAN | خیر | True/False | آیا کف مدل صاف شود (پیش‌فرض: False) |
| `flatten_bottom_threshold` | FLOAT | خیر | 0.0 تا 1.0 | آستانه صاف‌سازی کف (پیش‌فرض: 0.0) |
| `pivot_to_center_bottom` | BOOLEAN | خیر | True/False | آیا نقطه محوری به مرکز پایین مدل منتقل شود (پیش‌فرض: False) |
| `scale_factor` | FLOAT | خیر | 0.0 و بالاتر | ضریب مقیاس اعمال‌شده روی مدل (پیش‌فرض: 1.0) |
| `with_animation` | BOOLEAN | خیر | True/False | آیا داده‌های انیمیشن در خروجی گنجانده شود (پیش‌فرض: False) |
| `pack_uv` | BOOLEAN | خیر | True/False | آیا مختصات UV بسته‌بندی شود (پیش‌فرض: False) |
| `bake` | BOOLEAN | خیر | True/False | آیا بافت‌ها پخت شوند (پیش‌فرض: False) |
| `part_names` | STRING | خیر | لیست جدا شده با کاما | لیست جدا شده با کاما از نام قطعات برای گنجاندن در خروجی (پیش‌فرض: "") |
| `fbx_preset` | COMBO | خیر | blender<br>mixamo<br>3dsmax | پیش‌تنظیم خروجی FBX (پیش‌فرض: blender) |
| `export_vertex_colors` | BOOLEAN | خیر | True/False | آیا رنگ‌های رأس صادر شود (پیش‌فرض: False) |
| `export_orientation` | COMBO | خیر | align_image<br>default | حالت جهت‌گیری خروجی (پیش‌فرض: default) |
| `animate_in_place` | BOOLEAN | خیر | True/False | آیا مدل در مکان خود انیمیت شود (پیش‌فرض: False) |

**توجه:** `original_model_task_id` باید یک شناسه وظیفه معتبر از یک عملیات قبلی Tripo (تولید مدل، ریگینگ یا ریتارگتینگ) باشد. پارامترهای علامت‌گذاری‌شده به عنوان "پیشرفته" اختیاری هستند و فقط برای نیازهای خاص خروجی باید پیکربندی شوند.

## خروجی‌ها

| نام خروجی | نوع داده | توضیحات |
|-------------|-----------|-------------|
| *بدون خروجی نام‌گذاری‌شده* | - | این گره تبدیل را به صورت ناهمزمان پردازش کرده و نتیجه را از طریق سیستم API سرویس Tripo بازمی‌گرداند |

---
**Source fingerprint (SHA-256):** `b11ecab98701b7153a350f5e4980ddc2f446c0a12be3402ca98a5e6de60bd7ce`
