# حفظ Conditioning

تقوم هذه العقدة بحفظ conditioning واحد إلى مجلد الإخراج كملف safetensors. يمكن نقل الملف المحفوظ إلى مجلد models/embeddings وتحميله لاحقًا باستخدام Load Conditioning، على سبيل المثال لتخطي مشفّر النص. تمرّر العقدة الـ conditioning كما هو دون تغيير بحيث يمكن استخدامه لاحقًا في سير العمل.

## المدخلات

| المعامل | الوصف | نوع البيانات | مطلوب | النطاق |
|-----------|-------------|-----------|----------|-------|
| `conditioning` | الـ conditioning المراد حفظه. يتم دعم إدخال conditioning واحد فقط. | CONDITIONING | نعم | - |
| `filename_prefix` | البادئة المستخدمة لبناء اسم ملف الإخراج. يُكتب الملف في مجلد الإخراج مع إلحاق عدّاد رقمي. الافتراضي: `conditioning/ComfyUI` | STRING | نعم | - |

**ملاحظات:**

- إذا احتوى المدخل `conditioning` على أكثر من إدخال واحد (على سبيل المثال بعد دمج عدة conditionings)، فإن العقدة تُطلق خطأ: "Save Conditioning supports a single conditioning entry, save it before combining."
- تُحفظ خيارات الـ conditioning التي تكون موترات (tensors)، أو قوائم/مجموعات مرتبة من الموترات، أو قيمًا منطقية، أو أعدادًا صحيحة، أو أعدادًا عشرية، أو سلاسل نصية إلى جانب الـ conditioning. يتم تخطي الخيارات التي تكون `None`. أي نوع خيار آخر يؤدي إلى خطأ يوضح أن هذا الخيار لا يمكن حفظه.

## المخرجات

| اسم المخرج | الوصف | نوع البيانات |
|-------------|-------------|-----------|
| `conditioning` | نفس الـ conditioning الذي تم تمريره، دون تغيير. | CONDITIONING |

> تم إنشاء هذه الوثيقة بواسطة الذكاء الاصطناعي. إذا وجدت أي أخطاء أو لديك اقتراحات للتحسين، فلا تتردد في المساهمة! [تحرير على GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveConditioning/ar.md)

---
**Source fingerprint (SHA-256):** `07b7d2be5262c4782f237138d034b130322507e62ae8775b9c94634df8e7a3fa`
