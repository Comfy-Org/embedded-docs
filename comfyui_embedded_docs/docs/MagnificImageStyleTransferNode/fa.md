این گره، سبک بصری یک تصویر مرجع را به تصویر ورودی شما اعمال می‌کند. برای پردازش تصاویر از یک سرویس هوش مصنوعی خارجی استفاده می‌کند و به شما امکان می‌دهد قدرت انتقال سبک و حفظ ساختار تصویر اصلی را کنترل کنید.

## ورودی‌ها

| پارامتر | توضیحات | نوع داده | الزامی | محدوده |
| --- | --- | --- | --- | --- |
| `image` | تصویری که قرار است انتقال سبک روی آن اعمال شود. | IMAGE | بله | - |
| `reference_image` | تصویر مرجع برای استخراج سبک. | IMAGE | بله | - |
| `prompt` | یک توضیح متنی اختیاری برای هدایت فرآیند انتقال سبک. | STRING | خیر | - |
| `style_strength` | درصد قدرت سبک (پیش‌فرض: 100). | INT | خیر | 0 تا 100 |
| `structure_strength` | میزان حفظ ساختار تصویر اصلی (پیش‌فرض: 50). | INT | خیر | 0 تا 100 |
| `flavor` | طعم (حالت) انتقال سبک. | COMBO | خیر | "faithful"<br>"gen_z"<br>"psychedelia"<br>"detaily"<br>"clear"<br>"donotstyle"<br>"donotstyle_sharp" |
| `engine` | انتخاب موتور پردازش. | COMBO | خیر | "balanced"<br>"definio"<br>"illusio"<br>"3d_cartoon"<br>"colorful_anime"<br>"caricature"<br>"real"<br>"super_real"<br>"softy" |
| `portrait_mode` | فعال‌سازی حالت پرتره برای بهبود ویژگی‌های چهره. | COMBO | خیر | "disabled"<br>"enabled" |
| `portrait_style` | سبک بصری اعمال‌شده روی تصاویر پرتره. این ورودی فقط زمانی در دسترس است که `portrait_mode` روی "enabled" تنظیم شده باشد. | COMBO | خیر | "standard"<br>"pop"<br>"super_pop" |
| `portrait_beautifier` | شدت زیباسازی چهره در پرتره‌ها. این ورودی فقط زمانی در دسترس است که `portrait_mode` روی "enabled" تنظیم شده باشد. | COMBO | خیر | "none"<br>"beautify_face"<br>"beautify_face_max" |
| `fixed_generation` | در صورت غیرفعال بودن، انتظار می‌رود هر بار تولید، درجه‌ای از تصادفی‌گری را معرفی کند که منجر به نتایج متنوع‌تری می‌شود (پیش‌فرض: True). | BOOLEAN | خیر | - |

**محدودیت‌ها:**

* دقیقاً یک `image` و یک `reference_image` الزامی است.
* هر دو تصویر باید نسبت ابعادی بین 1:3 و 3:1 داشته باشند.
* هر دو تصویر باید حداقل ارتفاع و عرض 160 پیکسل داشته باشند.
* پارامترهای `portrait_style` و `portrait_beautifier` فقط زمانی فعال و الزامی هستند که `portrait_mode` روی "enabled" تنظیم شده باشد.

## خروجی‌ها

| نام خروجی | توضیحات | نوع داده |
| --- | --- | --- |
| `image` | تصویر نهایی پس از اعمال انتقال سبک. | IMAGE |

> این مستند با هوش مصنوعی تهیه شده است. اگر خطایی دیدید یا پیشنهادی برای بهبود دارید، خوشحال می‌شویم مشارکت کنید! [ویرایش در GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MagnificImageStyleTransferNode/fa.md)

---
**Source fingerprint (SHA-256):** `4ae400183618953c369d089d39b878f0a24592967c29d779c577fb8b7339dea8`
