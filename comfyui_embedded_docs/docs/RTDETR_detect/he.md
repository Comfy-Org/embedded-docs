# RTDETR_detect

הצומת RT-DETR Detect מבצע זיהוי אובייקטים בתמונות קלט באמצעות מודל RT-DETR. הוא מזהה אובייקטים, מחזיר תיבות תוחמות סביבם ומתייג אותם בהתאם למחלקות של מערך הנתונים COCO. ניתן לסנן את התוצאות לפי ציון ביטחון ומחלקת אובייקט, ולהגביל את מספר הזיהויים הכולל.

## קלטים

| פרמטר | תיאור | סוג נתונים | חובה | טווח |
| --- | --- | --- | --- | --- |
| `model` | מודל RT-DETR המשמש לזיהוי אובייקטים. | MODEL | כן | N/A |
| `image` | תמונת הקלט (או התמונות) שעבורה יש לזהות אובייקטים. הצומת מעבד תמונות בקבוצות של עד 32. | IMAGE | כן | N/A |
| `threshold` | ציון הביטחון המינימלי שזיהוי צריך לקבל כדי להיכלל בתוצאות (ברירת מחדל: 0.5). | FLOAT | כן | N/A |
| `class_name` | סנן זיהויים לפי מחלקה. הגדר ל-'all' כדי להשבית סינון (ברירת מחדל: `"all"`). | COMBO | כן | `"all"`<br>`"person"`<br>`"bicycle"`<br>`"car"`<br>`"motorcycle"`<br>`"airplane"`<br>`"bus"`<br>`"train"`<br>`"truck"`<br>`"boat"`<br>`"traffic light"`<br>`"fire hydrant"`<br>`"stop sign"`<br>`"parking meter"`<br>`"bench"`<br>`"bird"`<br>`"cat"`<br>`"dog"`<br>`"horse"`<br>`"sheep"`<br>`"cow"`<br>`"elephant"`<br>`"bear"`<br>`"zebra"`<br>`"giraffe"`<br>`"backpack"`<br>`"umbrella"`<br>`"handbag"`<br>`"tie"`<br>`"suitcase"`<br>`"frisbee"`<br>`"skis"`<br>`"snowboard"`<br>`"sports ball"`<br>`"kite"`<br>`"baseball bat"`<br>`"baseball glove"`<br>`"skateboard"`<br>`"surfboard"`<br>`"tennis racket"`<br>`"bottle"`<br>`"wine glass"`<br>`"cup"`<br>`"fork"`<br>`"knife"`<br>`"spoon"`<br>`"bowl"`<br>`"banana"`<br>`"apple"`<br>`"sandwich"`<br>`"orange"`<br>`"broccoli"`<br>`"carrot"`<br>`"hot dog"`<br>`"pizza"`<br>`"donut"`<br>`"cake"`<br>`"chair"`<br>`"couch"`<br>`"potted plant"`<br>`"bed"`<br>`"dining table"`<br>`"toilet"`<br>`"tv"`<br>`"laptop"`<br>`"mouse"`<br>`"remote"`<br>`"keyboard"`<br>`"cell phone"`<br>`"microwave"`<br>`"oven"`<br>`"toaster"`<br>`"sink"`<br>`"refrigerator"`<br>`"book"`<br>`"clock"`<br>`"vase"`<br>`"scissors"`<br>`"teddy bear"`<br>`"hair drier"`<br>`"toothbrush"` |
| `max_detections` | מספר מרבי של זיהויים להחזיר לכל תמונה. לפי סדר יורד של ציון הביטחון (ברירת מחדל: 100). | INT | כן | N/A |

## פלטים

| שם פלט | תיאור | סוג נתונים |
| --- | --- | --- |
| `bboxes` | רשימה של תיבות תוחמות עבור כל תמונת קלט. כל תיבה מכילה קואורדינטות (x, y, רוחב, גובה), תווית מחלקה וציון ביטחון. | BOUNDINGBOX |

> מסמך זה נוצר על ידי בינה מלאכותית. אם מצאתם שגיאות או שיש לכם הצעות לשיפור, אתם מוזמנים לתרום! [עריכה ב-GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RTDETR_detect/he.md)

---
**Source fingerprint (SHA-256):** `658a47cae788da207a52edc6bf8a428c9f3d8cf415e5f20f71d6125ad6d49734`
