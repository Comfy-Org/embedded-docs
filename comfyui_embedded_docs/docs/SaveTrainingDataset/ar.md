# حفظ مجموعة بيانات التدريب

## المدخلات

| المعامل | الوصف | نوع البيانات | مطلوب | النطاق |
| --- | --- | --- | --- | --- |
| `latents` | قائمة بقواميس الكمون (latent dicts) القادمة من MakeTrainingDataset. | LATENT | نعم | N/A |
| `conditioning` | قائمة بقوائم التكييف القادمة من MakeTrainingDataset. | CONDITIONING | نعم | N/A |
| `folder_name` | اسم المجلد الذي ستُحفظ فيه مجموعة البيانات، داخل دليل datasets. يُسمح بالمجلدات الفرعية مثل 'project/run1'. (الافتراضي: "training_dataset") | STRING | نعم | N/A |
| `shard_size` | عدد العينات في كل ملف جزء (shard). (الافتراضي: 1000) | INT | نعم | 1 إلى 100000 |

**ملاحظة:** يجب أن يتطابق عدد العناصر في `latents` تمامًا مع عدد العناصر في `conditioning`؛ تُصدر العقدة خطأً إذا لم تتطابق هذه الأعداد. كما يجب أن يشير `folder_name` إلى مجلد فرعي داخل دليل datasets (على سبيل المثال `my_dataset`) — ولا يمكن أن يكون هو دليل datasets نفسه، وتُرفض أسماء المجلدات التي قد ينتج عنها مسار خارج دليل datasets.

## المخرجات

لا تُنتج هذه العقدة أي بيانات مخرجة. وظيفتها حفظ الملفات على قرصك. يُحفظ كل جزء (shard) كملف `shard_XXXX.pkl` في المجلد المختار، ويسجّل ملف `metadata.json` العدد الإجمالي للعينات، وعدد الأجزاء، وحجم الجزء.

> تم إنشاء هذه الوثيقة بواسطة الذكاء الاصطناعي. إذا وجدت أي أخطاء أو لديك اقتراحات للتحسين، فلا تتردد في المساهمة! [تحرير على GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveTrainingDataset/ar.md)

---
**Source fingerprint (SHA-256):** `6d7b63a24ac42907b0f4a1358712cd0ed085982ecd308bce87e5376d9bbc2274`
