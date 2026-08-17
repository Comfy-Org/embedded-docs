# اكتشاف RT-DETR

```markdown
تقوم عقدة RT-DETR Detect بالكشف عن الأجسام في الصور المدخلة باستخدام نموذج RT-DETR. وهي تحدد الأجسام في الصورة وتُرجع إحداثيات الصناديق المحيطة (bounding boxes) لكل كشف، مع تصنيف يتوافق مع فئة مجموعة بيانات COCO. يمكنك تصفية النتائج حسب درجة الثقة وفئة الجسم، وتحديد العدد الأقصى من الاكتشافات المُرجعة لكل صورة.

## المدخلات

| المعامل | الوصف | نوع البيانات | مطلوب | النطاق |
| --- | --- | --- | --- | --- |
| `model` | نموذج RT-DETR المستخدم للكشف عن الأجسام. | MODEL | نعم | N/A |
| `image` | الصورة أو الصور المدخلة للكشف عن الأجسام فيها. تعالج العقدة الصور في دفعات يصل حجمها إلى 32 صورة وتعيد ضبط أبعادها داخليًا لأغراض الكشف. | IMAGE | نعم | N/A |
| `threshold` | الحد الأدنى لدرجة الثقة التي يجب أن يحققها الكشف ليكون ضمن النتائج (الافتراضي: 0.5). | FLOAT | نعم | N/A |
| `class_name` | تصفية الاكتشافات حسب الفئة. اضبطه على 'all' لتعطيل التصفية (الافتراضي: "all"). | COMBO | نعم | `"all"`<br>`"person"`<br>`"bicycle"`<br>`"car"`<br>`"motorcycle"`<br>`"airplane"`<br>`"bus"`<br>`"train"`<br>`"truck"`<br>`"boat"`<br>`"traffic light"`<br>`"fire hydrant"`<br>`"stop sign"`<br>`"parking meter"`<br>`"bench"`<br>`"bird"`<br>`"cat"`<br>`"dog"`<br>`"horse"`<br>`"sheep"`<br>`"cow"`<br>`"elephant"`<br>`"bear"`<br>`"zebra"`<br>`"giraffe"`<br>`"backpack"`<br>`"umbrella"`<br>`"handbag"`<br>`"tie"`<br>`"suitcase"`<br>`"frisbee"`<br>`"skis"`<br>`"snowboard"`<br>`"sports ball"`<br>`"kite"`<br>`"baseball bat"`<br>`"baseball glove"`<br>`"skateboard"`<br>`"surfboard"`<br>`"tennis racket"`<br>`"bottle"`<br>`"wine glass"`<br>`"cup"`<br>`"fork"`<br>`"knife"`<br>`"spoon"`<br>`"bowl"`<br>`"banana"`<br>`"apple"`<br>`"sandwich"`<br>`"orange"`<br>`"broccoli"`<br>`"carrot"`<br>`"hot dog"`<br>`"pizza"`<br>`"donut"`<br>`"cake"`<br>`"chair"`<br>`"couch"`<br>`"potted plant"`<br>`"bed"`<br>`"dining table"`<br>`"toilet"`<br>`"tv"`<br>`"laptop"`<br>`"mouse"`<br>`"remote"`<br>`"keyboard"`<br>`"cell phone"`<br>`"microwave"`<br>`"oven"`<br>`"toaster"`<br>`"sink"`<br>`"refrigerator"`<br>`"book"`<br>`"clock"`<br>`"vase"`<br>`"scissors"`<br>`"teddy bear"`<br>`"hair drier"`<br>`"toothbrush"` |
| `max_detections` | الحد الأقصى لعدد الاكتشافات التي سيتم إرجاعها لكل صورة. بالترتيب التنازلي لدرجة الثقة (الافتراضي: 100). | INT | نعم | N/A |

## المخرجات

| اسم المخرج | الوصف | نوع البيانات |
| --- | --- | --- |
| `bboxes` | قائمة بالصناديق المحيطة لكل صورة مدخلة. يحتوي كل صندوق على الإحداثيات (x، y، العرض، الارتفاع)، واسم الفئة، ودرجة الثقة. | BOUNDINGBOX |
```

> تم إنشاء هذه الوثيقة بواسطة الذكاء الاصطناعي. إذا وجدت أي أخطاء أو لديك اقتراحات للتحسين، فلا تتردد في المساهمة! [تحرير على GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RTDETR_detect/ar.md)

---
**Source fingerprint (SHA-256):** `658a47cae788da207a52edc6bf8a428c9f3d8cf415e5f20f71d6125ad6d49734`
