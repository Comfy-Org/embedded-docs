# FluxDisableGuidance

צומת זה משבית לחלוטין את ה-guidance embed במודלים של Flux ובמודלים דומים ל-Flux. הוא מקבל נתוני conditioning כקלט ומגדיר את ערך ה-guidance שלהם ל-None, ובכך מכבה למעשה conditioning מבוסס guidance עבור תהליך היצירה.

## קלטים

| פרמטר | תיאור | סוג נתונים | נדרש | טווח |
| --- | --- | --- | --- | --- |
| `conditioning` | נתוני ה-conditioning שיש לעבד ולהסיר מהם את ה-guidance | CONDITIONING | כן | - |

## פלטים

| שם פלט | תיאור | סוג נתונים |
| --- | --- | --- |
| `conditioning` | נתוני ה-conditioning ששונו, כאשר ה-guidance מושבת | CONDITIONING |

> מסמך זה נוצר על ידי בינה מלאכותית. אם מצאתם שגיאות או שיש לכם הצעות לשיפור, אתם מוזמנים לתרום! [עריכה ב-GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxDisableGuidance/he.md)

---
**Source fingerprint (SHA-256):** `da3286194f9f5e7e49dd7047d6b0a0c97bb2570eaa9281abbd3992a743302fbf`
