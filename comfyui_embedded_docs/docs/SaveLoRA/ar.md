# حفظ أوزان LoRA

The SaveLoRA node saves a LoRA (Low-Rank Adaptation) model to a file. It writes the LoRA model as a `.safetensors` file in the output directory. You can specify a filename prefix and an optional step count; when provided, the step count is included in the saved file name.

## المدخلات

| المعامل | الوصف | نوع البيانات | مطلوب | النطاق |
| --- | --- | --- | --- | --- |
| `lora` | نموذج LoRA المطلوب حفظه. لا تستخدم النموذج الذي تم تطبيق طبقات LoRA عليه. | LORA_MODEL | نعم | N/A |
| `prefix` | البادئة المستخدمة لملف LoRA المحفوظ (الافتراضي: "loras/ComfyUI_trained_lora"). | STRING | نعم | N/A |
| `steps` | اختياري: عدد الخطوات التي تم تدريب نموذج LoRA عليها، ويُستخدم لتسمية الملف المحفوظ. | INT | لا | N/A |

**ملاحظة:** يجب أن يكون مدخل `lora` نموذج LoRA نقيًا. لا تقم بتوفير نموذج أساسي تم تطبيق طبقات LoRA عليه.

## المخرجات

| اسم المخرج | الوصف | نوع البيانات |
| --- | --- | --- |
| *None* | لا تُخرج هذه العقدة أي بيانات إلى سير العمل. وهي عقدة إخراج تقوم بحفظ ملف على القرص. | N/A |

> تم إنشاء هذه الوثيقة بواسطة الذكاء الاصطناعي. إذا وجدت أي أخطاء أو لديك اقتراحات للتحسين، فلا تتردد في المساهمة! [تحرير على GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveLoRA/ar.md)

---
**Source fingerprint (SHA-256):** `02f1d15dd7a5181666f2dbf06c45c07b12c4a178985464e07b5f613bd628f906`
