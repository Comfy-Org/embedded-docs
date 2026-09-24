# OpenAI ChatGPT

تولّد هذه العقدة ردودًا نصية من نموذج OpenAI. ترسل المطالبة النصية الخاصة بك، ومعها اختياريًا صور أو ملفات، إلى نموذج OpenAI وتعيد الرد النصي المُولَّد.

## المدخلات

| المعامل | الوصف | نوع البيانات | مطلوب | النطاق |
|-----------|-------------|-----------|----------|-------|
| `prompt` | مدخلات نصية إلى النموذج، تُستخدم لتوليد رد (القيمة الافتراضية: سلسلة نصية فارغة). | STRING | نعم | - |
| `persist_context` | هذا المعامل مهمل وليس له تأثير (القيمة الافتراضية: `False`). | BOOLEAN | نعم | - |
| `model` | النموذج المستخدم لتوليد الرد (القيمة الافتراضية: `gpt-5`) | COMBO | نعم | `gpt-6-astra`<br>`gpt-6-sol`<br>`gpt-6-luna`<br>`gpt-5.6-sol`<br>`gpt-5.6-terra`<br>`gpt-5.6-luna`<br>`gpt-5.5-pro`<br>`gpt-5.5`<br>`gpt-5`<br>`gpt-5-mini`<br>`gpt-5-nano`<br>`gpt-4.1`<br>`gpt-4.1-mini`<br>`gpt-4.1-nano`<br>`o4-mini`<br>`o3`<br>`o1-pro`<br>`o1` |
| `images` | صورة/صور اختيارية تُستخدم كسياق للنموذج. لتضمين صور متعددة، يمكنك استخدام عقدة Batch Images. | IMAGE | لا | - |
| `files` | ملف/ملفات اختيارية تُستخدم كسياق للنموذج. تقبل مدخلات من عقدة OpenAI Chat Input Files. | OPENAI_INPUT_FILES | لا | - |
| `advanced_options` | إعدادات اختيارية للنموذج. تقبل مدخلات من عقدة OpenAI Chat Advanced Options. | OPENAI_CHAT_CONFIG | لا | - |

ملاحظة: عند توصيل إعدادات `advanced_options` التي تحدد جهد الاستدلال، يجب أن يدعم `model` المحدد قيمة جهد الاستدلال تلك. على سبيل المثال، عائلة النماذج gpt-4.1 لا تدعم أي جهد استدلال، وgpt-6-sol وgpt-6-luna تدعمان none و low و medium و high و xhigh و max، وgpt-5.5 يدعم none و low و medium و high و xhigh، وgpt-5.5-pro يدعم medium و high و xhigh. إذا لم يكن جهد الاستدلال مدعومًا من النموذج المحدد، فسترفع العقدة خطأً.

## المخرجات

| اسم المخرج | الوصف | نوع البيانات |
|-------------|-------------|-----------|
| `output_text` | الرد النصي الذي يولّده نموذج OpenAI. | STRING |

> تم إنشاء هذه الوثيقة بواسطة الذكاء الاصطناعي. إذا وجدت أي أخطاء أو لديك اقتراحات للتحسين، فلا تتردد في المساهمة! [تحرير على GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIChatNode/ar.md)

---
**Source fingerprint (SHA-256):** `46b4558f1368191e2b4eb68f79e098f289c9eb80e1e05f7a516123c098295f2b`
