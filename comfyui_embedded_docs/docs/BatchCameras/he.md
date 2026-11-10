# Batch Cameras

מאחד מצלמות ומסלולי מצלמה לרשימת מצלמות אחת, לפי סדר הקלט. Render Mesh ו-Render Splat מרנדרים תמונה אחת לכל מצלמה ברשימה, וכך נבנה רינדור רב-מבטי.

## קלטים

| פרמטר | תיאור | סוג נתונים | חובה | טווח |
| --- | --- | --- | --- | --- |
| `cameras` | חריץ ניתן להרחבה של מצלמות, מ-Create Camera Info, מ-Create Camera Orbit או ממציג. רשימת מצלמות נחשבת לכל מצלמה שבה. | AUTOGROW | כן | 1 עד 50 מצלמות |

## פלטים

| שם פלט | תיאור | סוג נתונים |
| --- | --- | --- |
| `camera_info` | רשימת מצלמות אחת המכילה כל מצלמת קלט, לפי סדר הקלט. | LOAD3D_CAMERA |

> מסמך זה נוצר על ידי בינה מלאכותית. אם מצאתם שגיאות או שיש לכם הצעות לשיפור, אתם מוזמנים לתרום! [עריכה ב-GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BatchCameras/he.md)

---
**Source fingerprint (SHA-256):** `a5ddae7f539a2d70efc1b156f7b4ec4b219d7cf78544b882f7b8f9538ae9a88d`
