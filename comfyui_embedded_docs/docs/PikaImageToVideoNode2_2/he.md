# PikaImageToVideoNode2_2

צומת Pika Image to Video שולח תמונה והנחיית טקסט אל Pika API בגרסה 2.2 כדי ליצור וידאו. הוא ממיר את תמונת הקלט שלך לפורמט וידאו בהתבסס על התיאור וההגדרות שסופקו. הצומת מטפל בתקשורת ה-API ומחזיר את הווידאו שנוצר כפלט.

## קלטים

| פרמטר | תיאור | סוג נתונים | חובה | טווח |
| --- | --- | --- | --- | --- |
| `image` | התמונה להמרה לוידאו | IMAGE | כן | - |
| `prompt_text` | תיאור הטקסט המנחה את יצירת הווידאו | STRING | כן | - |
| `negative_prompt` | טקסט המתאר ממה להימנע בווידאו | STRING | כן | - |
| `seed` | ערך seed אקראי לתוצאות ניתנות לשחזור | INT | כן | - |
| `resolution` | הגדרת רזולוציית וידאו הפלט | STRING | כן | - |
| `duration` | אורך הווידאו שנוצר בשניות | INT | כן | - |

## פלטים

| שם פלט | תיאור | סוג נתונים |
| --- | --- | --- |
| `output` | קובץ הווידאו שנוצר | VIDEO |

> מסמך זה נוצר על ידי בינה מלאכותית. אם מצאתם שגיאות או שיש לכם הצעות לשיפור, אתם מוזמנים לתרום! [עריכה ב-GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PikaImageToVideoNode2_2/he.md)

---
**Source fingerprint (SHA-256):** `aaa8dc49b94f0fae2010a3b61a3fb41e212fa9d2946a934a1a7c651fdced81b3`
