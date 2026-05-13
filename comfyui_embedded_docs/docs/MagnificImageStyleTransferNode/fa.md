> این مستند با هوش مصنوعی تهیه شده است. اگر خطایی دیدید یا پیشنهادی برای بهبود دارید، خوشحال می‌شویم مشارکت کنید! [ویرایش در GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MagnificImageStyleTransferNode/fa.md)

این گره، سبک بصری یک تصویر مرجع را به تصویر ورودی شما اعمال می‌کند. برای پردازش تصاویر از یک سرویس هوش مصنوعی خارجی استفاده می‌کند و به شما امکان می‌دهد قدرت انتقال سبک و حفظ ساختار تصویر اصلی را کنترل کنید.

## ورودی‌ها

| پارامتر | نوع داده | الزامی | محدوده | توضیحات |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | بله | - | تصویری که قرار است انتقال سبک روی آن اعمال شود. |
| `reference_image` | IMAGE | بله | - | تصویر مرجع برای استخراج سبک. |
| `prompt` | STRING | خیر | - | یک توضیح متنی اختیاری برای هدایت فرآیند انتقال سبک. |
| `style_strength` | INT | خیر | 0 تا 100 | درصد قدرت سبک (پیش‌فرض: 100). |
| `structure_strength` | INT | خیر | 0 تا 100 | میزان حفظ ساختار تصویر اصلی (پیش‌فرض: 50). |
| `flavor` | COMBO | خیر | "faithful"<br>"gen_z"<br>"psychedelia"<br>"detaily"<br>"clear"<br>"donotstyle"<br>"donotstyle_sharp" | طعم (حالت) انتقال سبک. |
| `engine` | COMBO | خیر | "balanced"<br>"definio"<br>"illusio"<br>"3d_cartoon"<br>"colorful_anime"<br>"caricature"<br>"real"<br>"super_real"<br>"softy" | انتخاب موتور پردازش. |
| `portrait_mode` | COMBO | خیر | "disabled"<br>"enabled" | فعال‌سازی حالت پرتره برای بهبود ویژگی‌های چهره. |
| `portrait_style` | COMBO | خیر | "standard"<br>"pop"<br>"super_pop" | سبک بصری اعمال‌شده روی تصاویر پرتره. این ورودی فقط زمانی در دسترس است که `portrait_mode` روی "enabled" تنظیم شده باشد. |
| `portrait_beautifier` | COMBO | خیر | "none"<br>"beautify_face"<br>"beautify_face_max" | شدت زیباسازی چهره در پرتره‌ها. این ورودی فقط زمانی در دسترس است که `portrait_mode` روی "enabled" تنظیم شده باشد. |
| `fixed_generation` | BOOLEAN | خیر | - | در صورت غیرفعال بودن، انتظار می‌رود هر بار تولید، درجه‌ای از تصادفی‌گری را معرفی کند که منجر به نتایج متنوع‌تری می‌شود (پیش‌فرض: True). |

**محدودیت‌ها:**

* دقیقاً یک `image` و یک `reference_image` الزامی است.
* هر دو تصویر باید نسبت ابعادی بین 1:3 و 3:1 داشته باشند.
* هر دو تصویر باید حداقل ارتفاع و عرض 160 پیکسل داشته باشند.
* پارامترهای `portrait_style` و `portrait_beautifier` فقط زمانی فعال و الزامی هستند که `portrait_mode` روی "enabled" تنظیم شده باشد.

## خروجی‌ها

| نام خروجی | نوع داده | توضیحات |
|-------------|-----------|-------------|
| `image` | IMAGE | تصویر نهایی پس از اعمال انتقال سبک. |

---
**Source fingerprint (SHA-256):** `4ae400183618953c369d089d39b878f0a24592967c29d779c577fb8b7339dea8`
