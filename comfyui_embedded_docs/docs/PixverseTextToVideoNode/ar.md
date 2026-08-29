# بيكسفيرس نص إلى فيديو

Generates videos based on a text prompt and various generation parameters. This node creates video content using the PixVerse API, allowing control over aspect ratio, quality, duration, motion style, and more.

يُنشئ مقاطع فيديو استنادًا إلى نص موجه (prompt) ومعلمات توليد متنوعة. ينشئ هذا العقد محتوى فيديو باستخدام واجهة برمجة تطبيقات PixVerse، مما يتيح التحكم في نسبة العرض إلى الارتفاع، والجودة، والمدة، ونمط الحركة، والمزيد.

## Inputs  
## المدخلات

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `النص المطلوب` | Prompt for the video generation (default: "") | STRING | نعم | - |
| `نسبة العرض إلى الارتفاع` | Aspect ratio for the generated video | COMBO | نعم | `"16:9"`<br>`"9:16"`<br>`"1:1"` |
| `الجودة` | Video quality setting (default: "540p") | COMBO | نعم | `"540p"`<br>`"1080p"` |
| `مدة الثواني` | Duration of the generated video in seconds | COMBO | نعم | `"5"`<br>`"10"` |
| `وضع الحركة` | Motion style for the video generation | COMBO | نعم | `"normal"`<br>`"fast"` |
| `البذرة` | Seed for video generation (default: 0) | INT | نعم | 0 إلى 2147483647 |
| `نص المطالبة السلبية` | An optional text description of undesired elements on an image (default: "") | STRING | لا | - |
| `قالب بيكسفيرس` | An optional template to influence style of generation, created by the PixVerse Template node | CUSTOM | لا | - |

| المعامل | الوصف | نوع البيانات | مطلوب | النطاق |
|-----------|-------------|-----------|----------|-------|
| `النص المطلوب` | النص الموجّه لتوليد الفيديو (الافتراضي: "") | STRING | نعم | - |
| `نسبة العرض إلى الارتفاع` | نسبة العرض إلى الارتفاع للفيديو المُولّد | COMBO | نعم | `"16:9"`<br>`"9:16"`<br>`"1:1"` |
| `الجودة` | إعداد جودة الفيديو (الافتراضي: "540p") | COMBO | نعم | `"540p"`<br>`"1080p"` |
| `مدة الثواني` | مدة الفيديو المُولّد بالثواني | COMBO | نعم | `"5"`<br>`"10"` |
| `وضع الحركة` | نمط الحركة لتوليد الفيديو | COMBO | نعم | `"normal"`<br>`"fast"` |
| `البذرة` | Seed الخاص بتوليد الفيديو (الافتراضي: 0) | INT | نعم | 0 إلى 2147483647 |
| `نص المطالبة السلبية` | وصف نصي اختياري للعناصر غير المرغوب فيها في الصورة (الافتراضي: "") | STRING | لا | - |
| `قالب بيكسفيرس` | قالب اختياري للتأثير على نمط التوليد، تم إنشاؤه بواسطة عقدة PixVerse Template | CUSTOM | لا | - |

**Note:** The `prompt` must contain at least 1 character. When using 1080p quality, the motion mode is automatically set to `normal` and the duration is limited to 5 seconds. For non-5 second durations, the motion mode is also automatically set to `normal`.

**ملاحظة:** يجب أن يحتوي `prompt` على حرف واحد على الأقل. عند استخدام جودة 1080p، يتم ضبط نمط الحركة تلقائيًا على `normal` وتكون المدة محدودة بـ 5 ثوانٍ. إذا كانت المدة غير 5 ثوانٍ، فسيتم ضبط نمط الحركة أيضًا تلقائيًا على `normal`.

## Outputs  
## المخرجات

| Output Name | Description | Data Type |
|-------------|-------------|-----------|
| `output` | The generated video file | VIDEO |

| اسم المخرَج | الوصف | نوع البيانات |
|-------------|-------------|-----------|
| `output` | ملف الفيديو المُولّد | VIDEO |

> تم إنشاء هذه الوثيقة بواسطة الذكاء الاصطناعي. إذا وجدت أي أخطاء أو لديك اقتراحات للتحسين، فلا تتردد في المساهمة! [تحرير على GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseTextToVideoNode/ar.md)

---
**Source fingerprint (SHA-256):** `cb95579dc6c9afa17455b0216ec46571ad2c0455606cf3b9c725ca512c45f938`
