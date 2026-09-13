# المُعين Euler الأثري

تُنشئ عقدة SamplerEulerAncestral مُنشئ عينات Euler Ancestral يمكن استخدامه أثناء توليد الصور. يجمع هذا المُنشئ بين تكامل Euler وأخذ العينات السلفي (ancestral sampling)، مما يضيف درجة من العشوائية في كل خطوة لإنتاج نتائج متنوعة. تتيح لك العقدة ضبط مقدار العشوائية المطبقة عبر إعداداتها.

## المدخلات

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `eta` | يتحكم في حجم الخطوة ودرجة العشوائية في عملية أخذ العينات (الافتراضي: 1.0). هذا معامل متقدم. | FLOAT | نعم | 0.0 - 100.0 |
| `s_noise` | يتحكم في مقدار الضوضاء المضافة أثناء أخذ العينات (الافتراضي: 1.0). هذا معامل متقدم. | FLOAT | نعم | 0.0 - 100.0 |

## المخرجات

| Output Name | Description | Data Type |
| --- | --- | --- |
| `sampler` | يعيد مُنشئ عينات Euler Ancestral مُهيأً يمكن استخدامه في مسار أخذ العينات. | SAMPLER |

> تم إنشاء هذه الوثيقة بواسطة الذكاء الاصطناعي. إذا وجدت أي أخطاء أو لديك اقتراحات للتحسين، فلا تتردد في المساهمة! [تحرير على GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerEulerAncestral/ar.md)

---
**Source fingerprint (SHA-256):** `0d3c1f0ffe01eb6cc17fd53e743713f659218ec19001c670440472ae7d0d3887`
