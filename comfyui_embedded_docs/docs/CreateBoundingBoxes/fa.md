# ایجاد جعبه‌های مرزی

کشیدن جعبه‌های مرزی در یک بوم. خروجی شامل عناصر پرامپت Ideogram، جعبه‌های مرزی در فضای پیکسلی و یک تصویر پیش‌نمایش است.

## ورودی‌ها

| پارامتر | توضیحات | نوع داده | الزامی | محدوده |
|-----------|-------------|-----------|----------|-------|
| `background` | تصویر اختیاری که به عنوان پس‌زمینه در بوم و پیش‌نمایش استفاده می‌شود. | IMAGE | No | - |
| `bboxes` | Bounding boxes, elements, or a JSON string to initialize the canvas. A new upstream value initializes the canvas; edits made on the canvas take priority and are kept until the upstream value changes again. | BOUNDING_BOX, ARRAY, STRING | No | - |
| `width` | عرض بوم و شبکه پیکسلی برای جعبه‌های مرزی. | INT | Yes | 64 to 16384 (step: 16) |
| `height` | ارتفاع بوم و شبکه پیکسلی برای جعبه‌های مرزی. | INT | Yes | 64 to 16384 (step: 16) |
| `editor_state` | جعبه‌های مرزی را رسم کنید و نوع هر جعبه، متن، توضیح و پالت رنگ را تعیین کنید. با عنصر پس‌زمینه شروع و با پیش‌زمینه پایان دهید. | BOUNDING_BOXES | Yes | - |
| `last_incoming` | Internal state managed by the canvas: the upstream bboxes value that last initialized it. Leave empty to re-initialize the canvas from the bboxes input on the next run. | BOUNDING_BOXES | No | - |

## خروجی‌ها

| نام خروجی | توضیحات | نوع داده |
|-------------|-------------|-----------|
| `preview` | An RGB image showing the canvas with all bounding boxes rendered, including labels, color palette swatches, and descriptive text. | IMAGE |
| `bboxes` | A list of bounding boxes in pixel coordinates, with each box containing x, y, width, and height values. | BOUNDING_BOX |
| `elements` | A structured array of element objects, each containing type, bounding box coordinates (normalized 0-1000), text (for text type), description, and color palette. | ARRAY |

> این مستند با هوش مصنوعی تهیه شده است. اگر خطایی دیدید یا پیشنهادی برای بهبود دارید، خوشحال می‌شویم مشارکت کنید! [ویرایش در GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateBoundingBoxes/fa.md)

---
**Source fingerprint (SHA-256):** `dc5545dffefdccf14f3919ff4d9966dbfd1a497dcd64e1863556d5728659ee94`
