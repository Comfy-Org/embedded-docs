# تعديل صورة Grok

قم بتعديل صورة موجودة بناءً على موجه نصي. ترسل هذه العقدة صورك ووصفًا نصيًا إلى Grok API، الذي يقوم بتعديل الصور وفقًا لتعليماتك ويعيد النتيجة.
## المدخلات

### المدخلات المشتركة

| المعامل | الوصف | نوع البيانات | إلزامي | النطاق |
|---|---|---|---|---|
| `النموذج` | نموذج Grok للصور الذي سيتم استخدامه. تتغير المعاملات الفرعية الموضحة أدناه اعتمادًا على النموذج المحدد. | DYNAMIC_COMBO | نعم | "grok-imagine-image-2.0"<br>"grok-imagine-image-quality"<br>"grok-imagine-image-pro"<br>"grok-imagine-image" |
| `الموجه` | الموجّه النصي المستخدم لإنشاء الصورة. (الافتراضي: "") | STRING | نعم | N/A |
| `البذرة` | البذرة لتحديد ما إذا كان ينبغي إعادة تشغيل العقدة؛ النتائج الفعلية غير حتمية بغض النظر عن البذرة. (الافتراضي: 0) | INT | نعم | 0 to 2147483647 |

### مدخلات grok-imagine-image-2.0

| المعامل | الوصف | نوع البيانات | إلزامي | النطاق |
|---|---|---|---|---|
| `resolution` | دقة الإخراج للصور المعدلة. | COMBO | نعم | "1K"<br>"2K" |
| `number_of_images` | عدد الصور المعدلة التي سيتم إنشاؤها. (الافتراضي: 1) | INT | نعم | 1 to 10 |
| `quality` | مستوى جودة الصور المُنشأة. | COMBO | نعم | "medium"<br>"low" |
| `aspect_ratio` | نسبة العرض إلى الارتفاع للصورة المعدلة. (الافتراضي: "auto") | COMBO | نعم | "auto"<br>"1:1"<br>"2:3"<br>"3:2"<br>"3:4"<br>"4:3"<br>"9:16"<br>"16:9"<br>"9:19.5"<br>"19.5:9"<br>"9:20"<br>"20:9"<br>"1:2"<br>"2:1" |

### مدخلات grok-imagine-image-quality و grok-imagine-image

| المعامل | الوصف | نوع البيانات | إلزامي | النطاق |
|---|---|---|---|---|
| `resolution` | دقة الإخراج للصور المعدلة. | COMBO | نعم | "1K"<br>"2K" |
| `number_of_images` | عدد الصور المعدلة التي سيتم إنشاؤها. (الافتراضي: 1) | INT | نعم | 1 to 10 |
| `aspect_ratio` | مسموح به فقط عند توصيل صور متعددة. (الافتراضي: "auto") | COMBO | نعم | "auto"<br>"1:1"<br>"2:3"<br>"3:2"<br>"3:4"<br>"4:3"<br>"9:16"<br>"16:9"<br>"9:19.5"<br>"19.5:9"<br>"9:20"<br>"20:9"<br>"1:2"<br>"2:1" |

### مدخلات grok-imagine-image-pro

| المعامل | الوصف | نوع البيانات | إلزامي | النطاق |
|---|---|---|---|---|
| `resolution` | دقة الإخراج للصور المعدلة. | COMBO | نعم | "1K"<br>"2K" |
| `number_of_images` | عدد الصور المعدلة التي سيتم إنشاؤها. (الافتراضي: 1) | INT | نعم | 1 to 10 |

### المدخلات المرجعية

| المعامل | الوصف | نوع البيانات | إلزامي | النطاق |
|---|---|---|---|---|
| `images` | فتحة قابلة للتوسع: قم بتوصيل صورة مرجعية واحدة أو أكثر لتعديلها. يمكن إضافة فتحات مرقمة مثل `image_1` و`image_2` و`image_3`. يعتمد العدد الأقصى للصور على النموذج المحدد (انظر أقسام النماذج أعلاه). | IMAGE | نعم | 1 image for `grok-imagine-image-pro`<br>1 to 3 images for `grok-imagine-image-2.0`, `grok-imagine-image-quality`, and `grok-imagine-image` |

## المخرجات

| اسم المخرج | الوصف | نوع البيانات |
|---|---|---|
| `IMAGE` | The edited image(s) returned by the Grok API. If a single image is generated, it is returned directly. If multiple images are generated, they are concatenated into a single batch tensor. | IMAGE |

> تم إنشاء هذه الوثيقة بواسطة الذكاء الاصطناعي. إذا وجدت أي أخطاء أو لديك اقتراحات للتحسين، فلا تتردد في المساهمة! [تحرير على GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokImageEditNodeV2/ar.md)

---
**Source fingerprint (SHA-256):** `7d75b1cb8405c5024567b1119bcbd5e4b318152605f74b62bdd5173dda75949f`
