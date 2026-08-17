# OpenAI ChatGPT

تقوم هذه العقدة بتوليد استجابات نصية من نموذج OpenAI. ترسل مطالبتك النصية (وبشكل اختياري الصور أو الملفات) إلى نموذج OpenAI وتُعيد الاستجابة النصية المولدة.

## المدخلات

| المعامل | الوصف | نوع البيانات | مطلوب | النطاق |
|-----------|-------------|-----------|----------|-------|
| `prompt` | مدخلات نصية إلى النموذج، تُستخدم لتوليد استجابة (الافتراضي: فارغ) | STRING | نعم | - |
| `persist_context` | هذه المعلمة مهملة وليس لها أي تأثير (الافتراضي: False) | BOOLEAN | نعم | - |
| `model` | النموذج المستخدم لتوليد الاستجابة (الافتراضي: `gpt-5`) | COMBO | نعم | `gpt-5.6-sol`<br>`gpt-5.6-terra`<br>`gpt-5.6-luna`<br>`gpt-5.5-pro`<br>`gpt-5.5`<br>`gpt-5`<br>`gpt-5-mini`<br>`gpt-5-nano`<br>`gpt-4.1`<br>`gpt-4.1-mini`<br>`gpt-4.1-nano`<br>`o4-mini`<br>`o3`<br>`o1-pro`<br>`o1` |
| `images` | صور اختيارية لاستخدامها كسياق للنموذج. لتضمين عدة صور، يمكنك استخدام عقدة Batch Images | IMAGE | لا | - |
| `files` | ملفات اختيارية لاستخدامها كسياق للنموذج. تقبل مدخلات من عقدة OpenAI Chat Input Files | OPENAI_INPUT_FILES | لا | - |
| `advanced_options` | إعداد اختياري للنموذج. يقبل مدخلات من عقدة OpenAI Chat Advanced Options | OPENAI_CHAT_CONFIG | لا | - |

## المخرجات

| اسم المخرَج | الوصف | نوع البيانات |
|-------------|-------------|-----------|
| `output_text` | الاستجابة النصية المولدة بواسطة نموذج OpenAI | STRING |

> تم إنشاء هذه الوثيقة بواسطة الذكاء الاصطناعي. إذا وجدت أي أخطاء أو لديك اقتراحات للتحسين، فلا تتردد في المساهمة! [تحرير على GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIChatNode/ar.md)

---
**Source fingerprint (SHA-256):** `25bb3648a4e1ea5668486375153ac4c96b542082c88958d4f62b93adf1db5b2a`
