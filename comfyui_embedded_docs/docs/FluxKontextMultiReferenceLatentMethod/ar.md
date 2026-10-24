# طريقة FluxKontextMultiReferenceLatent

تقوم عقدة FluxKontextMultiReferenceLatentMethod بتحديث بيانات التهيئة عبر تخزين طريقة مختارة للمتجهات الكامنة المرجعية داخلها. ثم تُستخدم الطريقة المخزَّنة عند معالجة المتجهات الكامنة المرجعية في خطوات التوليد اللاحقة. تم وضع علامة تجريبية على هذه العقدة، وهي تنتمي إلى نظام التهيئة Flux.

## المدخلات

| المعامل | الوصف | نوع البيانات | مطلوب | النطاق |
| --- | --- | --- | --- | --- |
| `التكييف` | بيانات التهيئة التي سيتم تعديلها باستخدام طريقة المتجهات الكامنة المرجعية | CONDITIONING | نعم | - |
| `طريقة المرجع الكامن` | الطريقة المستخدمة لمعالجة المتجهات الكامنة المرجعية. إذا تم تحديد قيمة تحتوي على "uxo" أو "uso"، فسيتم تحويلها إلى "uxo" قبل تخزينها. تم وضع علامة متقدم على هذا المعامل. | COMBO | نعم | `"offset"`<br>`"index"`<br>`"uxo/uno"`<br>`"index_timestep_zero"`<br>`"index_timestep_zero_isolated"`<br>`"index_timestep_zero_text_start"` |

## المخرجات

| اسم المخرج | الوصف | نوع البيانات |
| --- | --- | --- |
| `conditioning` | بيانات التهيئة المعدلة بعد تطبيق طريقة المتجهات الكامنة المرجعية | CONDITIONING |

> تم إنشاء هذه الوثيقة بواسطة الذكاء الاصطناعي. إذا وجدت أي أخطاء أو لديك اقتراحات للتحسين، فلا تتردد في المساهمة! [تحرير على GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxKontextMultiReferenceLatentMethod/ar.md)

---
**Source fingerprint (SHA-256):** `de2e3d34f9e47a90ff37300489bffef8082eb92deefbc2ce338b17b0d853ac77`
