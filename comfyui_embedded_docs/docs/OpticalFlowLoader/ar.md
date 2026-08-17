# تحميل نموذج التدفق البصري

## نظرة عامة

يقوم بتحميل نموذج تدفق بصري من مجلد `models/optical_flow/`. حاليًا، يُدعم فقط تنسيق RAFT-large من torchvision، وهو النموذج المستخدم في عقدة VOIDWarpedNoise. لا يقوم ComfyUI بتنزيل أوزان التدفق البصري تلقائيًا؛ يجب عليك وضع ملف نقطة التحقق يدويًا في مجلد `models/optical_flow/`.

## المدخلات

| المعامل | الوصف | نوع البيانات | مطلوب | النطاق |
| --- | --- | --- | --- | --- |
| `model_name` | نموذج التدفق البصري المراد تحميله. يجب وضع الملفات في مجلد `optical_flow`. حاليًا، يُدعم فقط `raft_large.pth` من torchvision. | COMBO | نعم | قائمة الملفات في مجلد `models/optical_flow/` |

يجب أن يكون الملف المحدد نقطة تحقق RAFT-large من torchvision. تتحقق العقدة من أن الملف يحتوي على مفاتيح RAFT المتوقعة (`feature_encoder.*`، `context_encoder.*`، و `update_block.*`) وتطرح خطأ ValueError إذا لم يتم التعرف على التنسيق.

## المخرجات

| اسم المخرَج | الوصف | نوع البيانات |
| --- | --- | --- |
| `OPTICAL_FLOW` | نموذج التدفق البصري المُحمَّل، مغلّف في ModelPatcher لاستخدامه مع العقد الأخرى. | OPTICAL_FLOW |

> تم إنشاء هذه الوثيقة بواسطة الذكاء الاصطناعي. إذا وجدت أي أخطاء أو لديك اقتراحات للتحسين، فلا تتردد في المساهمة! [تحرير على GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpticalFlowLoader/ar.md)

---
**Source fingerprint (SHA-256):** `5e79551545ad7ee2fd4856a47da29808a404342d1d5e57da0980058db6b11c3b`
