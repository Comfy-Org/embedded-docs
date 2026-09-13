# Bria إزالة خلفية الصورة

تزيل هذه العقدة الخلفية من صورة باستخدام خدمة Bria RMBG 2.0. وهي ترسل الصورة إلى واجهة برمجة تطبيقات خارجية للمعالجة، ثم تعيد النتيجة بعد إزالة الخلفية.

## المدخلات

يكشف محدد `moderation` عن خيارات مراقبة إضافية عند ضبطه على `"true"`.

### المدخلات العامة

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `image` | الصورة المدخلة التي ستُزال خلفيتها. | IMAGE | نعم | - |
| `moderation` | إعدادات المراقبة. عند ضبطه على `"true"`، تصبح خيارات مراقبة إضافية متاحة. | DYNAMIC_COMBO | نعم | `"false"`<br>`"true"` |
| `seed` | يتحكم `seed` في ما إذا كان ينبغي إعادة تشغيل العقدة؛ النتائج غير حتمية بغض النظر عن `seed`. الافتراضي: `0`. | INT | نعم | 0 إلى 2147483647 |

### مدخلات moderation "true"

تظهر هذه المعاملات فقط عندما يكون `moderation` مضبوطًا على `"true"`. لا يضيف الخيار `"false"` أي مدخلات إضافية.

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `visual_input_moderation` | يمكّن مراقبة المحتوى المرئي على الصورة المدخلة. الافتراضي: `False`. | BOOLEAN | لا | - |
| `visual_output_moderation` | يمكّن مراقبة المحتوى المرئي على الصورة الناتجة. الافتراضي: `True`. | BOOLEAN | لا | - |

**ملاحظة:** تعتمد المعاملات `visual_input_moderation` و`visual_output_moderation` على المعامل `moderation`. وهي نشطة فقط عندما يكون `moderation` مضبوطًا على `"true"`.

## المخرجات

| Output Name | Description | Data Type |
|-------------|-------------|-----------|
| `image` | الصورة المعالجة بعد إزالة خلفيتها. | IMAGE |

> تم إنشاء هذه الوثيقة بواسطة الذكاء الاصطناعي. إذا وجدت أي أخطاء أو لديك اقتراحات للتحسين، فلا تتردد في المساهمة! [تحرير على GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaRemoveImageBackground/ar.md)

---
**Source fingerprint (SHA-256):** `f62dcd5c9406ec09f5aab44585dd7f25ae0f7d9a934faa10a58e46ef116df110`
