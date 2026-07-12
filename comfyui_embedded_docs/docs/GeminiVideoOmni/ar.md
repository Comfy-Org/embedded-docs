# Google Gemini Omni (فيديو)

أنشئ فيديو مع صوت من مطالبة نصية باستخدام نموذج Google Gemini Omni Flash. يمكنك اختيار صور و/أو مقاطع فيديو مرجعية لتوجيه أو تعديل النتيجة. صف الطول المطلوب (٣-١٠ ثوانٍ) ونسبة العرض إلى الارتفاع (١٦:٩ أو ٩:١٦) مباشرة في المطالبة.

## المدخلات

| المعامل | الوصف | نوع البيانات | إلزامي | النطاق |
|-----------|-------------|-----------|----------|-------|
| `model` | نموذج Gemini للفيديو المستخدم في إنشاء الفيديو. | MODEL | Yes | "Omni Flash" |
| `seed` | البذرة تتحكم في ما إذا كان يجب إعادة تشغيل العقدة؛ النتائج غير حتمية بغض النظر عن البذرة. | INT | Yes | 0 to 2147483647 |
| `prompt` | The text prompt describing the video to generate. Must be at least one non-whitespace character after stripping leading/trailing whitespace. | STRING | Yes | Minimum 1 character after stripping whitespace |
| `images` | Optional reference images to guide the video generation. Maximum of 14 images total. | IMAGE | No | Multiple images allowed (max 14) |
| `videos` | Optional reference videos to guide or edit the video generation. Maximum of 3 videos, each up to 10 seconds. | VIDEO | No | Multiple videos allowed (max 3, each max 10s) |
| `temperature` | Controls randomness in generation (default: 1.0). | FLOAT | No | 0.0 to 2.0 |
| `top_p` | Nucleus sampling parameter (default: 0.95). | FLOAT | No | 0.0 to 1.0 |

## المخرجات

| اسم المخرج | الوصف | نوع البيانات |
|-------------|-------------|-----------|
| `VIDEO` | The generated video with audio from the Gemini model. | VIDEO |
| `STRING` | Any text response from the model, such as reasoning or explanations. | STRING |

> تم إنشاء هذه الوثيقة بواسطة الذكاء الاصطناعي. إذا وجدت أي أخطاء أو لديك اقتراحات للتحسين، فلا تتردد في المساهمة! [تحرير على GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiVideoOmni/ar.md)

---
**Source fingerprint (SHA-256):** `046842b7ec736283bba355aaa038b02fcf2416020f5f7aee7b0150d2a05bcbe6`
