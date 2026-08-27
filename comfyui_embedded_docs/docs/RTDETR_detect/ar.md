# اكتشاف RT-DETR

تقوم عقدة كشف RT-DETR بإجراء كشف الأجسام على الصور المدخلة باستخدام نموذج RT-DETR. وهي تحدد الأجسام، وتُرجع صناديق الإحاطة حولها، وتصنفها وفقًا لفئات مجموعة بيانات COCO. يمكنك تصفية النتائج حسب درجة الثقة، وفئة الكائن، وتحديد العدد الإجمالي للاكتشافات.

## المدخلات

| المعامل | الوصف | نوع البيانات | مطلوب | النطاق |
| --- | --- | --- | --- | --- |
| `model` | نموذج RT-DETR المستخدم في كشف الأجسام. | MODEL | نعم | N/A |
| `image` | الصورة (الصور) المدخلة لاكتشاف الأجسام فيها. تعالج العقدة الصور في دفعات يصل حجمها إلى 32. | IMAGE | نعم | N/A |
| `threshold` | الحد الأدنى لدرجة الثقة التي يجب أن يحققها الاكتشاف ليشمل في النتائج (الافتراضي: 0.5). | FLOAT | لا | N/A |
| `class_name` | تصفية المكتشفات حسب الفئة. عيّن القيمة إلى 'all' لتعطيل التصفية (الافتراضي: "all"). | COMBO | لا | `"all"`<br>`"person"`<br>`"bicycle"`<br>`"car"`<br>`"motorcycle"`<br>`"airplane"`<br>`"bus"`<br>`"train"`<br>`"truck"`<br>`"boat"`<br>`"traffic light"`<br>`"fire hydrant"`<br>`"stop sign"`<br>`"parking meter"`<br>`"bench"`<br>`"bird"`<br>`"cat"`<br>`"dog"`<br>`"horse"`<br>`"sheep"`<br>`"cow"`<br>`"elephant"`<br>`"bear"`<br>`"zebra"`<br>`"giraffe"`<br>`"backpack"`<br>`"umbrella"`<br>`"handbag"`<br>`"tie"`<br>`"suitcase"`<br>`"frisbee"`<br>`"skis"`<br>`"snowboard"`<br>`"sports ball"`<br>`"kite"`<br>`"baseball bat"`<br>`"baseball glove"`<br>`"skateboard"`<br>`"surfboard"`<br>`"tennis racket"`<br>`"bottle"`<br>`"wine glass"`<br>`"cup"`<br>`"fork"`<br>`"knife"`<br>`"spoon"`<br>`"bowl"`<br>`"banana"`<br>`"apple"`<br>`"sandwich"`<br>`"orange"`<br>`"broccoli"`<br>`"carrot"`<br>`"hot dog"`<br>`"pizza"`<br>`"donut"`<br>`"cake"`<br>`"chair"`<br>`"couch"`<br>`"potted plant"`<br>`"bed"`<br>`"dining table"`<br>`"toilet"`<br>`"tv"`<br>`"laptop"`<br>`"mouse"`<br>`"remote"`<br>`"keyboard"`<br>`"cell phone"`<br>`"microwave"`<br>`"oven"`<br>`"toaster"`<br>`"sink"`<br>`"refrigerator"`<br>`"book"`<br>`"clock"`<br>`"vase"`<br>`"scissors"`<br>`"teddy bear"`<br>`"hair drier"`<br>`"toothbrush"` |
| `max_detections` | الحد الأقصى لعدد المكتشفات التي يتم إرجاعها لكل صورة. مرتبة حسب درجة الثقة تنازليًا (الافتراضي: 100). | INT | لا | N/A |

## المخرجات

| اسم المخرج | الوصف | نوع البيانات |
| --- | --- | --- |
| `bboxes` | قائمة بصناديق الإحاطة لكل صورة مدخلة. يحتوي كل صندوق على الإحداثيات (x، y، العرض، الارتفاع)، وملصق الفئة، ودرجة الثقة. | BOUNDINGBOX |

> تم إنشاء هذه الوثيقة بواسطة الذكاء الاصطناعي. إذا وجدت أي أخطاء أو لديك اقتراحات للتحسين، فلا تتردد في المساهمة! [تحرير على GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RTDETR_detect/ar.md)

---
**Source fingerprint (SHA-256):** `658a47cae788da207a52edc6bf8a428c9f3d8cf415e5f20f71d6125ad6d49734`
