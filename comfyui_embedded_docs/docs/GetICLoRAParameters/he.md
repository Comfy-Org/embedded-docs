# שליפת פרמטרי IC-LoRA

צומת זה קורא את המטא-דאטה ממודל טעון LoRA כדי לחלץ פרמטרים של IC-LoRA, כגון מקדם הקטנה של הרפרנס. הוא מפיק את הפרמטרים האלה כאובייקט מובנה שניתן לחבר לצומת LTXVAddGuide כאשר LoRA דורש טיפול מיוחד במדריכים.

## קלטים

| פרמטר | תיאור | סוג נתונים | נדרש | טווח |
| --- | --- | --- | --- | --- |
| `iclora_model` | פלט ישיר מ-LoRA Loader עבור ה-IC-LoRA הספציפי שממנו יש לחלץ את המטא-דאטה. | MODEL | כן | N/A |

הערה: אם המטא-דאטה של LoRA חסרה או שאינה מכילה רשומת `reference_downscale_factor`, הצומת מפיק ערך ברירת מחדל של 1. כאשר הוא קיים, המקדם מעוגל ומוגדר לערך מינימלי של 1.

## פלטים

| שם פלט | תיאור | סוג נתונים |
| --- | --- | --- |
| `iclora_parameters` | פרמטרים של IC-LoRA שחולצו מהמטא-דאטה של LoRA (למשל, `reference_downscale_factor`). יש לחבר ל-LTXVAddGuide אם ה-LoRA דורש טיפול מיוחד במדריכים. | IC_LORA_PARAMETERS |

> מסמך זה נוצר על ידי בינה מלאכותית. אם מצאתם שגיאות או שיש לכם הצעות לשיפור, אתם מוזמנים לתרום! [עריכה ב-GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GetICLoRAParameters/he.md)

---
**Source fingerprint (SHA-256):** `5f6becad0c7673b8cde1e099bd7ba5be7106da958b8967f8e693ba2a704baaef`
