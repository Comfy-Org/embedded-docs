# طريقة FluxKontextMultiReferenceLatent

| المعامل | الوصف | نوع البيانات | مطلوب | النطاق |
| --- | --- | --- | --- | --- |
| `conditioning` | بيانات التكييف التي سيتم تعديلها باستخدام طريقة الكمونات المرجعية | CONDITIONING | نعم | - |
| `reference_latents_method` | الطريقة المستخدمة لمعالجة الكمونات المرجعية. إذا تم تحديد "uxo" أو "uso"، فسيتم تحويلها إلى "uxo". يُعلَّم هذا المعامل كمعامل متقدم. | COMBO | نعم | `"offset"`<br>`"index"`<br>`"uxo/uno"`<br>`"index_timestep_zero"` |

## المخرجات

| اسم المخرَج | الوصف | نوع البيانات |
| --- | --- | --- |
| `conditioning` | بيانات التكييف المعدَّلة مع تطبيق طريقة الكمونات المرجعية | CONDITIONING |

> تم إنشاء هذه الوثيقة بواسطة الذكاء الاصطناعي. إذا وجدت أي أخطاء أو لديك اقتراحات للتحسين، فلا تتردد في المساهمة! [تحرير على GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxKontextMultiReferenceLatentMethod/ar.md)

---
**Source fingerprint (SHA-256):** `cbe069d0c9f8adbf7f8c909b1cd644d9cd3730e934f0e5856213ff06fa8ecc56`
