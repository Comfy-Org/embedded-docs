# تحميل نموذج التدفق البصري

يحمّل نموذج التدفق البصري من مجلد `models/optical_flow/`. حاليًا، يتم دعم صيغة RAFT-large من torchvision فقط، وهي النموذج المستخدم في عقدة VOIDWarpedNoise. لا يقوم ComfyUI بتنزيل أوزان التدفق البصري تلقائيًا؛ يجب وضع ملف نقطة التحقق يدويًا في مجلد `models/optical_flow/`.

## المدخلات

| المعامل | الوصف | نوع البيانات | مطلوب | النطاق |
| --- | --- | --- | --- | --- |
| `model_name` | نموذج التدفق البصري المراد تحميله. يجب وضع الملفات في مجلد `optical_flow`. حاليًا، يتم دعم `raft_large.pth` من torchvision فقط. | COMBO | نعم | قائمة الملفات في مجلد `models/optical_flow/` |

ملاحظة: يجب أن يكون ملف نقطة التحقق المحدد عبارة عن state dict بصيغة RAFT-large من torchvision يحتوي على مفاتيح مسبوقة بـ `feature_encoder.` و `context_encoder.` و `update_block.`. إذا كان الملف لا يطابق هذه الصيغة، تقوم العقدة برفع خطأ ValueError.

## المخرجات

| اسم المخرج | الوصف | نوع البيانات |
| --- | --- | --- |
| `OPTICAL_FLOW` | نموذج التدفق البصري المُحمَّل، مضبوطًا على وضع التقييم ودقة float32، ومغلفًا في ModelPatcher لاستخدامه مع العقد الأخرى. | OPTICAL_FLOW |

> تم إنشاء هذه الوثيقة بواسطة الذكاء الاصطناعي. إذا وجدت أي أخطاء أو لديك اقتراحات للتحسين، فلا تتردد في المساهمة! [تحرير على GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpticalFlowLoader/ar.md)

---
**Source fingerprint (SHA-256):** `5e79551545ad7ee2fd4856a47da29808a404342d1d5e57da0980058db6b11c3b`
