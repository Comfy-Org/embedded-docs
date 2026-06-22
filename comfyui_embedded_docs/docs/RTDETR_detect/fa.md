# شناسایی RT-DETR

گره تشخیص RT-DETR، تشخیص اشیاء را بر روی تصاویر ورودی با استفاده از یک مدل RT-DETR انجام می‌دهد. این گره اشیاء را شناسایی کرده، کادرهای محدودکننده (bounding boxes) دور آن‌ها رسم می‌کند و آن‌ها را بر اساس کلاس‌های مجموعه داده COCO برچسب‌گذاری می‌کند. می‌توانید نتایج را بر اساس نمره اطمینان (confidence score)، کلاس شیء فیلتر کرده و تعداد کل تشخیص‌ها را محدود کنید.

## ورودی‌ها

| پارامتر | توضیحات | نوع داده | الزامی | محدوده |
| --- | --- | --- | --- | --- |
| `مدل` | مدل RT-DETR مورد استفاده برای تشخیص اشیاء. | MODEL | بله | ناموجود |
| `تصویر` | تصویر(های) ورودی برای تشخیص اشیاء در آن. این گره تصاویر را در دسته‌های حداکثر ۳۲ تایی پردازش می‌کند. | IMAGE | بله | ناموجود |
| `آستانه` | حداقل نمره اطمینانی که یک تشخیص باید داشته باشد تا در نتایج گنجانده شود (پیش‌فرض: ۰.۵). | FLOAT | خیر | ناموجود |
| `نام کلاس` | تشخیص‌ها را بر اساس کلاس فیلتر کنید. برای غیرفعال کردن فیلتر، روی 'all' تنظیم کنید (پیش‌فرض: "all"). | COMBO | خیر | `"all"`<br>`"person"`<br>`"bicycle"`<br>`"car"`<br>`"motorcycle"`<br>`"airplane"`<br>`"bus"`<br>`"train"`<br>`"truck"`<br>`"boat"`<br>`"traffic light"`<br>`"fire hydrant"`<br>`"stop sign"`<br>`"parking meter"`<br>`"bench"`<br>`"bird"`<br>`"cat"`<br>`"dog"`<br>`"horse"`<br>`"sheep"`<br>`"cow"`<br>`"elephant"`<br>`"bear"`<br>`"zebra"`<br>`"giraffe"`<br>`"backpack"`<br>`"umbrella"`<br>`"handbag"`<br>`"tie"`<br>`"suitcase"`<br>`"frisbee"`<br>`"skis"`<br>`"snowboard"`<br>`"sports ball"`<br>`"kite"`<br>`"baseball bat"`<br>`"baseball glove"`<br>`"skateboard"`<br>`"surfboard"`<br>`"tennis racket"`<br>`"bottle"`<br>`"wine glass"`<br>`"cup"`<br>`"fork"`<br>`"knife"`<br>`"spoon"`<br>`"bowl"`<br>`"banana"`<br>`"apple"`<br>`"sandwich"`<br>`"orange"`<br>`"broccoli"`<br>`"carrot"`<br>`"hot dog"`<br>`"pizza"`<br>`"donut"`<br>`"cake"`<br>`"chair"`<br>`"couch"`<br>`"potted plant"`<br>`"bed"`<br>`"dining table"`<br>`"toilet"`<br>`"tv"`<br>`"laptop"`<br>`"mouse"`<br>`"remote"`<br>`"keyboard"`<br>`"cell phone"`<br>`"microwave"`<br>`"oven"`<br>`"toaster"`<br>`"sink"`<br>`"refrigerator"`<br>`"book"`<br>`"clock"`<br>`"vase"`<br>`"scissors"`<br>`"teddy bear"`<br>`"hair drier"`<br>`"toothbrush"` |
| `حداکثر شناسایی` | حداکثر تعداد تشخیص‌هایی که به ازای هر تصویر بازگردانده می‌شود. به ترتیب نمره اطمینان نزولی (پیش‌فرض: ۱۰۰). | INT | خیر | ناموجود |

## خروجی‌ها

| نام خروجی | توضیحات | نوع داده |
| --- | --- | --- |
| `bboxes` | فهرستی از کادرهای محدودکننده برای هر تصویر ورودی. هر کادر شامل مختصات (x، y، عرض، ارتفاع)، یک برچسب کلاس و یک نمره اطمینان است. | BOUNDINGBOX |

> این مستند با هوش مصنوعی تهیه شده است. اگر خطایی دیدید یا پیشنهادی برای بهبود دارید، خوشحال می‌شویم مشارکت کنید! [ویرایش در GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RTDETR_detect/fa.md)

---
**Source fingerprint (SHA-256):** `0c32aa9e17b8ea81e52cb45df2a40f7c1faeb39fdf18dfc643d1d31ed0bfdefd`
