# شناسایی RT-DETR

گره RT-DETR Detect با استفاده از یک مدل RT-DETR، تشخیص اشیاء را روی تصاویر ورودی انجام می‌دهد. این گره اشیاء را شناسایی کرده، جعبه‌های محدودکننده دور آن‌ها برمی‌گرداند و آن‌ها را بر اساس کلاس‌های مجموعه داده COCO برچسب‌گذاری می‌کند. می‌توانید نتایج را بر اساس نمره اطمینان، کلاس شیء فیلتر کرده و تعداد کل تشخیص‌ها را محدود کنید.

## ورودی‌ها

| پارامتر | توضیحات | نوع داده | الزامی | محدوده |
| --- | --- | --- | --- | --- |
| `مدل` | مدل RT-DETR که برای تشخیص اشیاء استفاده می‌شود. | MODEL | بله | N/A |
| `تصویر` | تصویر(های) ورودی برای تشخیص اشیاء در آن‌ها. این گره تصاویر را در دسته‌های حداکثر ۳۲ تایی پردازش می‌کند. | IMAGE | بله | N/A |
| `آستانه` | حداقل نمره اطمینانی که یک تشخیص باید داشته باشد تا در نتایج گنجانده شود (پیش‌فرض: 0.5). | FLOAT | خیر | N/A |
| `نام کلاس` | تشخیص‌ها را بر اساس کلاس فیلتر کنید. برای غیرفعال کردن فیلتر، مقدار را روی 'all' قرار دهید (پیش‌فرض: "all"). | COMBO | خیر | `"all"`<br>`"person"`<br>`"bicycle"`<br>`"car"`<br>`"motorcycle"`<br>`"airplane"`<br>`"bus"`<br>`"train"`<br>`"truck"`<br>`"boat"`<br>`"traffic light"`<br>`"fire hydrant"`<br>`"stop sign"`<br>`"parking meter"`<br>`"bench"`<br>`"bird"`<br>`"cat"`<br>`"dog"`<br>`"horse"`<br>`"sheep"`<br>`"cow"`<br>`"elephant"`<br>`"bear"`<br>`"zebra"`<br>`"giraffe"`<br>`"backpack"`<br>`"umbrella"`<br>`"handbag"`<br>`"tie"`<br>`"suitcase"`<br>`"frisbee"`<br>`"skis"`<br>`"snowboard"`<br>`"sports ball"`<br>`"kite"`<br>`"baseball bat"`<br>`"baseball glove"`<br>`"skateboard"`<br>`"surfboard"`<br>`"tennis racket"`<br>`"bottle"`<br>`"wine glass"`<br>`"cup"`<br>`"fork"`<br>`"knife"`<br>`"spoon"`<br>`"bowl"`<br>`"banana"`<br>`"apple"`<br>`"sandwich"`<br>`"orange"`<br>`"broccoli"`<br>`"carrot"`<br>`"hot dog"`<br>`"pizza"`<br>`"donut"`<br>`"cake"`<br>`"chair"`<br>`"couch"`<br>`"potted plant"`<br>`"bed"`<br>`"dining table"`<br>`"toilet"`<br>`"tv"`<br>`"laptop"`<br>`"mouse"`<br>`"remote"`<br>`"keyboard"`<br>`"cell phone"`<br>`"microwave"`<br>`"oven"`<br>`"toaster"`<br>`"sink"`<br>`"refrigerator"`<br>`"book"`<br>`"clock"`<br>`"vase"`<br>`"scissors"`<br>`"teddy bear"`<br>`"hair drier"`<br>`"toothbrush"` |
| `حداکثر شناسایی` | حداکثر تعداد تشخیص‌هایی که برای هر تصویر برگردانده می‌شود. به ترتیب نمره اطمینان نزولی (پیش‌فرض: 100). | INT | خیر | N/A |

## خروجی‌ها

| نام خروجی | توضیحات | نوع داده |
| --- | --- | --- |
| `bboxes` | فهرستی از جعبه‌های محدودکننده برای هر تصویر ورودی. هر جعبه شامل مختصات (x, y, width, height)، برچسب کلاس و نمره اطمینان است. | BOUNDINGBOX |

> این مستند با هوش مصنوعی تهیه شده است. اگر خطایی دیدید یا پیشنهادی برای بهبود دارید، خوشحال می‌شویم مشارکت کنید! [ویرایش در GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RTDETR_detect/fa.md)

---
**Source fingerprint (SHA-256):** `658a47cae788da207a52edc6bf8a428c9f3d8cf415e5f20f71d6125ad6d49734`
