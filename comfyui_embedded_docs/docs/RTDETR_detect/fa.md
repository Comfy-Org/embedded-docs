# شناسایی RT-DETR

گره RT-DETR Detect با استفاده از یک مدل RT-DETR، تشخیص اشیاء را روی تصاویر ورودی انجام می‌دهد. این گره اشیاء موجود در تصویر را پیدا می‌کند و برای هر تشخیص، مختصات کادر محدودکننده را همراه با برچسب کلاس مربوطه از مجموعه‌داده COCO برمی‌گرداند. می‌توانید نتایج را بر اساس امتیاز اطمینان و کلاس شیء فیلتر کنید و تعداد کل تشخیص‌های برگشتی برای هر تصویر را محدود کنید.

## ورودی‌ها

| پارامتر | توضیحات | نوع داده | الزامی | محدوده |
| --- | --- | --- | --- | --- |
| `model` | مدل RT-DETR مورد استفاده برای تشخیص اشیاء. | MODEL | بله | N/A |
| `image` | تصویر(های) ورودی که اشیاء در آن‌ها تشخیص داده می‌شوند. گره تصاویر را در دسته‌های حداکثر ۳۲ تایی پردازش و برای تشخیص، ابعاد آن‌ها را به‌صورت داخلی تغییر اندازه می‌دهد. | IMAGE | بله | N/A |
| `threshold` | حداقل امتیاز اطمینانی که یک تشخیص باید داشته باشد تا در نتایج لحاظ شود (پیش‌فرض: 0.5). | FLOAT | بله | N/A |
| `class_name` | تشخیص‌ها را بر اساس کلاس فیلتر می‌کند. برای غیرفعال کردن فیلتر، مقدار «all» را قرار دهید (پیش‌فرض: "all"). | COMBO | بله | `"all"`<br>`"person"`<br>`"bicycle"`<br>`"car"`<br>`"motorcycle"`<br>`"airplane"`<br>`"bus"`<br>`"train"`<br>`"truck"`<br>`"boat"`<br>`"traffic light"`<br>`"fire hydrant"`<br>`"stop sign"`<br>`"parking meter"`<br>`"bench"`<br>`"bird"`<br>`"cat"`<br>`"dog"`<br>`"horse"`<br>`"sheep"`<br>`"cow"`<br>`"elephant"`<br>`"bear"`<br>`"zebra"`<br>`"giraffe"`<br>`"backpack"`<br>`"umbrella"`<br>`"handbag"`<br>`"tie"`<br>`"suitcase"`<br>`"frisbee"`<br>`"skis"`<br>`"snowboard"`<br>`"sports ball"`<br>`"kite"`<br>`"baseball bat"`<br>`"baseball glove"`<br>`"skateboard"`<br>`"surfboard"`<br>`"tennis racket"`<br>`"bottle"`<br>`"wine glass"`<br>`"cup"`<br>`"fork"`<br>`"knife"`<br>`"spoon"`<br>`"bowl"`<br>`"banana"`<br>`"apple"`<br>`"sandwich"`<br>`"orange"`<br>`"broccoli"`<br>`"carrot"`<br>`"hot dog"`<br>`"pizza"`<br>`"donut"`<br>`"cake"`<br>`"chair"`<br>`"couch"`<br>`"potted plant"`<br>`"bed"`<br>`"dining table"`<br>`"toilet"`<br>`"tv"`<br>`"laptop"`<br>`"mouse"`<br>`"remote"`<br>`"keyboard"`<br>`"cell phone"`<br>`"microwave"`<br>`"oven"`<br>`"toaster"`<br>`"sink"`<br>`"refrigerator"`<br>`"book"`<br>`"clock"`<br>`"vase"`<br>`"scissors"`<br>`"teddy bear"`<br>`"hair drier"`<br>`"toothbrush"` |
| `max_detections` | حداکثر تعداد تشخیص‌هایی که برای هر تصویر برگردانده می‌شود. به ترتیب نزولی امتیاز اطمینان (پیش‌فرض: 100). | INT | بله | N/A |

## خروجی‌ها

| نام خروجی | توضیحات | نوع داده |
| --- | --- | --- |
| `bboxes` | فهرستی از کادرهای محدودکننده برای هر تصویر ورودی. هر کادر شامل مختصات (x, y, width, height)، برچسب کلاس و امتیاز اطمینان است. | BOUNDINGBOX |

> این مستند با هوش مصنوعی تهیه شده است. اگر خطایی دیدید یا پیشنهادی برای بهبود دارید، خوشحال می‌شویم مشارکت کنید! [ویرایش در GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RTDETR_detect/fa.md)

---
**Source fingerprint (SHA-256):** `658a47cae788da207a52edc6bf8a428c9f3d8cf415e5f20f71d6125ad6d49734`
