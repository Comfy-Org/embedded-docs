# إنشاء صناديق محيطة

رسم صناديق محيطة في لوحة الرسم. يخرج عناصر موجه Ideogram، وصناديق محيطة في مساحة البكسل، وصورة معاينة.

## المدخلات

| المعامل | الوصف | نوع البيانات | إلزامي | النطاق |
|-----------|-------------|-----------|----------|-------|
| `الخلفية` | صورة اختيارية تُستخدم كخلفية في لوحة الرسم والمعاينة. | IMAGE | No | - |
| `bboxes` | Bounding boxes, elements, or a JSON string to initialize the canvas. A new upstream value initializes the canvas; edits made on the canvas take priority and are kept until the upstream value changes again. | BOUNDING_BOX, ARRAY, STRING | No | - |
| `العرض` | عرض لوحة الرسم وشبكة البكسل للصناديق المحيطة. | INT | Yes | 64 to 16384 (step: 16) |
| `الارتفاع` | ارتفاع لوحة الرسم وشبكة البكسل للصناديق المحيطة. | INT | Yes | 64 to 16384 (step: 16) |
| `حالة المحرر` | ارسم الصناديق المحيطة وحدد نوع كل صندوق، النص، الوصف، لوحة الألوان. ابدأ بعنصر الخلفية أولاً والعناصر الأمامية أخيراً. | BOUNDING_BOXES | Yes | - |
| `last_incoming` | Internal state managed by the canvas: the upstream bboxes value that last initialized it. Leave empty to re-initialize the canvas from the bboxes input on the next run. | BOUNDING_BOXES | No | - |

## المخرجات

| اسم المخرج | الوصف | نوع البيانات |
|-------------|-------------|-----------|
| `preview` | An RGB image showing the canvas with all bounding boxes rendered, including labels, color palette swatches, and descriptive text. | IMAGE |
| `bboxes` | A list of bounding boxes in pixel coordinates, with each box containing x, y, width, and height values. | BOUNDING_BOX |
| `elements` | A structured array of element objects, each containing type, bounding box coordinates (normalized 0-1000), text (for text type), description, and color palette. | ARRAY |

> تم إنشاء هذه الوثيقة بواسطة الذكاء الاصطناعي. إذا وجدت أي أخطاء أو لديك اقتراحات للتحسين، فلا تتردد في المساهمة! [تحرير على GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateBoundingBoxes/ar.md)

---
**Source fingerprint (SHA-256):** `dc5545dffefdccf14f3919ff4d9966dbfd1a497dcd64e1863556d5728659ee94`
