> تم إنشاء هذه الوثيقة بواسطة الذكاء الاصطناعي. إذا وجدت أي أخطاء أو لديك اقتراحات للتحسين، فلا تتردد في المساهمة! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ResizeImageMaskNode/ar.md)

تقدم عقدة Resize Image/Mask طرقًا متعددة لتغيير أبعاد صورة أو قناع إدخال. يمكنها التحجيم باستخدام مضاعف، أو تعيين أبعاد محددة، أو مطابقة حجم إدخال آخر، أو التعديل بناءً على عدد البكسل، باستخدام طرق استيفاء متنوعة للحفاظ على الجودة.

## المدخلات

| المعامل | نوع البيانات | مطلوب | النطاق | الوصف |
|-----------|-----------|----------|-------|-------------|
| `input` | IMAGE أو MASK | نعم | N/A | الصورة أو القناع المراد تغيير حجمه. |
| `resize_type` | COMBO | نعم | `SCALE_BY`<br>`SCALE_DIMENSIONS`<br>`SCALE_LONGER_DIMENSION`<br>`SCALE_SHORTER_DIMENSION`<br>`SCALE_WIDTH`<br>`SCALE_HEIGHT`<br>`SCALE_TOTAL_PIXELS`<br>`MATCH_SIZE` | الطريقة المستخدمة لتحديد الحجم الجديد. تتغير المعاملات المطلوبة بناءً على النوع المحدد. |
| `multiplier` | FLOAT | لا | 0.01 إلى 8.0 | عامل التحجيم. مطلوب عندما يكون `resize_type` هو `SCALE_BY` (الافتراضي: 1.00). |
| `width` | INT | لا | 0 إلى 8192 | العرض المستهدف بالبكسل. مطلوب عندما يكون `resize_type` هو `SCALE_DIMENSIONS` أو `SCALE_WIDTH` (الافتراضي: 512). |
| `height` | INT | لا | 0 إلى 8192 | الارتفاع المستهدف بالبكسل. مطلوب عندما يكون `resize_type` هو `SCALE_DIMENSIONS` أو `SCALE_HEIGHT` (الافتراضي: 512). |
| `crop` | COMBO | لا | `"disabled"`<br>`"center"` | طريقة القص المطبقة عندما لا تتطابق الأبعاد مع نسبة العرض إلى الارتفاع. متاحة فقط عندما يكون `resize_type` هو `SCALE_DIMENSIONS` أو `MATCH_SIZE` (الافتراضي: "center"). |
| `longer_size` | INT | لا | 0 إلى 8192 | الحجم المستهدف للضلع الأطول في الصورة. مطلوب عندما يكون `resize_type` هو `SCALE_LONGER_DIMENSION` (الافتراضي: 512). |
| `shorter_size` | INT | لا | 0 إلى 8192 | الحجم المستهدف للضلع الأقصر في الصورة. مطلوب عندما يكون `resize_type` هو `SCALE_SHORTER_DIMENSION` (الافتراضي: 512). |
| `megapixels` | FLOAT | لا | 0.01 إلى 16.0 | العدد الإجمالي المستهدف للميجابكسل. مطلوب عندما يكون `resize_type` هو `SCALE_TOTAL_PIXELS` (الافتراضي: 1.0). |
| `match` | IMAGE أو MASK | لا | N/A | صورة أو قناع سيتم تغيير حجم الإدخال لمطابقة أبعاده. مطلوب عندما يكون `resize_type` هو `MATCH_SIZE`. |
| `scale_method` | COMBO | نعم | `"nearest-exact"`<br>`"bilinear"`<br>`"area"`<br>`"bicubic"`<br>`"lanczos"` | خوارزمية الاستيفاء المستخدمة للتحجيم (الافتراضي: "area"). |

**ملاحظة:** معامل `crop` متاح وذو صلة فقط عندما يكون `resize_type` مضبوطًا على `SCALE_DIMENSIONS` أو `MATCH_SIZE`. عند استخدام `SCALE_WIDTH` أو `SCALE_HEIGHT`، يتم تحجيم البعد الآخر تلقائيًا للحفاظ على نسبة العرض إلى الارتفاع الأصلية.

## المخرجات

| اسم المخرج | نوع البيانات | الوصف |
|-------------|-----------|-------------|
| `resized` | IMAGE أو MASK | الصورة أو القناع الذي تم تغيير حجمه، مطابقًا لنوع بيانات الإدخال. |
