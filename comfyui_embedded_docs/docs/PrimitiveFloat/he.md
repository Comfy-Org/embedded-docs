# PrimitiveFloat

צומת PrimitiveFloat יוצר ערך מספרי מסוג נקודה צפה שיכול לשמש בתהליך העבודה שלך. הוא מקבל קלט מספרי יחיד ומפיק את אותו ערך, מה שמאפשר לך להגדיר ולהעביר ערכי נקודה צפה בין צמתים שונים בצינור העבודה של ComfyUI.

## קלטים

| פרמטר | תיאור | סוג נתונים | נדרש | טווח |
| --- | --- | --- | --- | --- |
| `value` | ערך מספר הנקודה הצפה שיוחזר כפלט (ברירת מחדל: 0.0) | FLOAT | כן | -sys.maxsize to sys.maxsize (step: 0.1) |

## פלטים

| שם פלט | תיאור | סוג נתונים |
| --- | --- | --- |
| `output` | ערך מספר הנקודה הצפה של הקלט | FLOAT |

> מסמך זה נוצר על ידי בינה מלאכותית. אם מצאתם שגיאות או שיש לכם הצעות לשיפור, אתם מוזמנים לתרום! [עריכה ב-GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PrimitiveFloat/he.md)

---
**Source fingerprint (SHA-256):** `df57e5900e972e17da365fbbdb7b7db777dda6f9f938e1074f1a89451d4b7c73`
