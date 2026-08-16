# Grok Image Edit
## ورودیها

### ورودی‌های مشترک

| پارامتر | توضیحات | نوع داده | اجباری | محدوده |
|---|---|---|---|---|
| `model` | مدل تصویر Grok که باید استفاده شود. زیرپارامترهای نمایش‌داده‌شده در زیر بسته به مدل انتخابی تغییر می‌کنند. | DYNAMIC_COMBO | بله | "grok-imagine-image-2.0"<br>"grok-imagine-image-quality"<br>"grok-imagine-image-pro"<br>"grok-imagine-image" |
| `prompt` | متن راهنمای (prompt) مورد استفاده برای تولید تصویر. (پیش‌فرض: "") | STRING | بله | N/A |
| `seed` | مقدار Seed برای تعیین اینکه آیا گره باید دوباره اجرا شود؛ نتایج واقعی بدون توجه به Seed غیرقطعی هستند. (پیش‌فرض: 0) | INT | بله | 0 to 2147483647 |

### ورودی‌های grok-imagine-image-2.0

| پارامتر | توضیحات | نوع داده | اجباری | محدوده |
|---|---|---|---|---|
| `resolution` | رزولوشن خروجی تصاویر ویرایش‌شده. | COMBO | بله | "1K"<br>"2K" |
| `number_of_images` | تعداد تصاویر ویرایش‌شده برای تولید. (پیش‌فرض: 1) | INT | بله | 1 to 10 |
| `quality` | سطح کیفیت تصاویر تولیدشده. | COMBO | بله | "medium"<br>"low" |
| `aspect_ratio` | نسبت ابعاد تصویر ویرایش‌شده. (پیش‌فرض: "auto") | COMBO | بله | "auto"<br>"1:1"<br>"2:3"<br>"3:2"<br>"3:4"<br>"4:3"<br>"9:16"<br>"16:9"<br>"9:19.5"<br>"19.5:9"<br>"9:20"<br>"20:9"<br>"1:2"<br>"2:1" |

### ورودی‌های grok-imagine-image-quality و grok-imagine-image

| پارامتر | توضیحات | نوع داده | اجباری | محدوده |
|---|---|---|---|---|
| `resolution` | رزولوشن خروجی تصاویر ویرایش‌شده. | COMBO | بله | "1K"<br>"2K" |
| `number_of_images` | تعداد تصاویر ویرایش‌شده برای تولید. (پیش‌فرض: 1) | INT | بله | 1 to 10 |
| `aspect_ratio` | فقط زمانی مجاز است که چند تصویر متصل شده باشند. (پیش‌فرض: "auto") | COMBO | بله | "auto"<br>"1:1"<br>"2:3"<br>"3:2"<br>"3:4"<br>"4:3"<br>"9:16"<br>"16:9"<br>"9:19.5"<br>"19.5:9"<br>"9:20"<br>"20:9"<br>"1:2"<br>"2:1" |

### ورودی‌های grok-imagine-image-pro

| پارامتر | توضیحات | نوع داده | اجباری | محدوده |
|---|---|---|---|---|
| `resolution` | رزولوشن خروجی تصاویر ویرایش‌شده. | COMBO | بله | "1K"<br>"2K" |
| `number_of_images` | تعداد تصاویر ویرایش‌شده برای تولید. (پیش‌فرض: 1) | INT | بله | 1 to 10 |

### ورودی‌های مرجع

| پارامتر | توضیحات | نوع داده | اجباری | محدوده |
|---|---|---|---|---|
| `images` | اسلات افزایش‌پذیر: یک یا چند تصویر مرجع برای ویرایش متصل کنید. اسلات‌های شماره‌دار مانند `image_1`، `image_2`، `image_3` قابل افزودن هستند. حداکثر تعداد تصاویر به مدل انتخابی بستگی دارد (به بخش‌های مدل در بالا مراجعه کنید). | IMAGE | بله | 1 image for `grok-imagine-image-pro`<br>1 to 3 images for `grok-imagine-image-2.0`, `grok-imagine-image-quality`, and `grok-imagine-image` |

## خروجیها

| نام خروجی | توضیحات | نوع داده |
|---|---|---|
| `IMAGE` | The edited image(s) returned by the Grok API. If a single image is generated, it is returned directly. If multiple images are generated, they are concatenated into a single batch tensor. | IMAGE |

> این مستند با هوش مصنوعی تهیه شده است. اگر خطایی دیدید یا پیشنهادی برای بهبود دارید، خوشحال می‌شویم مشارکت کنید! [ویرایش در GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokImageEditNodeV2/fa.md)

---
**Source fingerprint (SHA-256):** `7d75b1cb8405c5024567b1119bcbd5e4b318152605f74b62bdd5173dda75949f`
