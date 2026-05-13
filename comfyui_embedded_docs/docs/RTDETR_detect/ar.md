> تم إنشاء هذه الوثيقة بواسطة الذكاء الاصطناعي. إذا وجدت أي أخطاء أو لديك اقتراحات للتحسين، فلا تتردد في المساهمة! [تحرير على GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RTDETR_detect/ar.md)

عقدة كشف RT-DETR تقوم بتنفيذ كشف الأجسام على الصور المدخلة باستخدام نموذج RT-DETR. تقوم بتحديد الأجسام، ورسم مربعات إحاطة حولها، وتسميتها وفقًا لفئات مجموعة بيانات COCO. يمكنك تصفية النتائج حسب درجة الثقة، وفئة الجسم، والحد من العدد الإجمالي للاكتشافات.

## المدخلات

| المعامل | نوع البيانات | إلزامي | النطاق | الوصف |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | نعم | غير متاح | نموذج RT-DETR المستخدم في كشف الأجسام. |
| `image` | IMAGE | نعم | غير متاح | الصورة (الصور) المدخلة لكشف الأجسام فيها. تعالج العقدة الصور في دفعات يصل حجمها إلى 32 صورة. |
| `threshold` | FLOAT | لا | غير متاح | الحد الأدنى لدرجة الثقة التي يجب أن يحققها الكشف ليتم تضمينه في النتائج (القيمة الافتراضية: 0.5). |
| `class_name` | COMBO | لا | `"all"`<br>`"person"`<br>`"bicycle"`<br>`"car"`<br>`"motorcycle"`<br>`"airplane"`<br>`"bus"`<br>`"train"`<br>`"truck"`<br>`"boat"`<br>`"traffic light"`<br>`"fire hydrant"`<br>`"stop sign"`<br>`"parking meter"`<br>`"bench"`<br>`"bird"`<br>`"cat"`<br>`"dog"`<br>`"horse"`<br>`"sheep"`<br>`"cow"`<br>`"elephant"`<br>`"bear"`<br>`"zebra"`<br>`"giraffe"`<br>`"backpack"`<br>`"umbrella"`<br>`"handbag"`<br>`"tie"`<br>`"suitcase"`<br>`"frisbee"`<br>`"skis"`<br>`"snowboard"`<br>`"sports ball"`<br>`"kite"`<br>`"baseball bat"`<br>`"baseball glove"`<br>`"skateboard"`<br>`"surfboard"`<br>`"tennis racket"`<br>`"bottle"`<br>`"wine glass"`<br>`"cup"`<br>`"fork"`<br>`"knife"`<br>`"spoon"`<br>`"bowl"`<br>`"banana"`<br>`"apple"`<br>`"sandwich"`<br>`"orange"`<br>`"broccoli"`<br>`"carrot"`<br>`"hot dog"`<br>`"pizza"`<br>`"donut"`<br>`"cake"`<br>`"chair"`<br>`"couch"`<br>`"potted plant"`<br>`"bed"`<br>`"dining table"`<br>`"toilet"`<br>`"tv"`<br>`"laptop"`<br>`"mouse"`<br>`"remote"`<br>`"keyboard"`<br>`"cell phone"`<br>`"microwave"`<br>`"oven"`<br>`"toaster"`<br>`"sink"`<br>`"refrigerator"`<br>`"book"`<br>`"clock"`<br>`"vase"`<br>`"scissors"`<br>`"teddy bear"`<br>`"hair drier"`<br>`"toothbrush"` | تصفية الاكتشافات حسب الفئة. اضبط على 'all' لتعطيل التصفية (القيمة الافتراضية: "all"). |
| `max_detections` | INT | لا | غير متاح | الحد الأقصى لعدد الاكتشافات المراد إرجاعها لكل صورة. بترتيب تنازلي لدرجة الثقة (القيمة الافتراضية: 100). |

## المخرجات

| اسم المخرج | نوع البيانات | الوصف |
|-------------|-----------|-------------|
| `bboxes` | BOUNDINGBOX | قائمة بمربعات الإحاطة لكل صورة مدخلة. يحتوي كل مربع على إحداثيات (س، ص، العرض، الارتفاع)، وتسمية الفئة، ودرجة الثقة. |

---
**Source fingerprint (SHA-256):** `0c32aa9e17b8ea81e52cb45df2a40f7c1faeb39fdf18dfc643d1d31ed0bfdefd`
