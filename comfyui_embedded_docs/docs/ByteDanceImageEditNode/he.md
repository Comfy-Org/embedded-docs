# ByteDanceImageEditNode

הצומת ByteDance Image Edit מאפשר לך לשנות תמונות באמצעות מודלים של AI של ByteDance דרך API. אתה מספק תמונת קלט והנחיית טקסט המתארת את השינויים הרצויים, והצומת מעבד את התמונה לפי ההוראות שלך. הצומת מטפל בתקשורת עם ה-API באופן אוטומטי ומחזיר את התמונה הערוכה.

## קלטים

| פרמטר | תיאור | סוג נתונים | סוג קלט | ברירת מחדל | טווח |
| --- | --- | --- | --- | --- | --- |
| `model` | שם מודל | MODEL | COMBO | seededit_3 | Image2ImageModelName options |
| `image` | תמונת הבסיס לעריכה | IMAGE | IMAGE | - | - |
| `prompt` | הנחיה לעריכת התמונה | STRING | STRING | "" | - |
| `seed` | ערך Seed לשימוש ביצירה | INT | INT | 0 | 0-2147483647 |
| `guidance_scale` | ערך גבוה יותר גורם לתמונה להיצמד יותר להנחיה | FLOAT | FLOAT | 5.5 | 1.0-10.0 |
| `watermark` | האם להוסיף סימן מים "AI generated" לתמונה | BOOLEAN | BOOLEAN | True | - |

## פלטים

| שם פלט | תיאור | סוג נתונים |
| --- | --- | --- |
| `IMAGE` | התמונה הערוכה המוחזרת מ-API של ByteDance | IMAGE |

> מסמך זה נוצר על ידי בינה מלאכותית. אם מצאתם שגיאות או שיש לכם הצעות לשיפור, אתם מוזמנים לתרום! [עריכה ב-GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceImageEditNode/he.md)

---
**Source fingerprint (SHA-256):** `9dc13d89f84756b545120efb5535e08ada163d4534975809f5056bdf7d8bfb73`
