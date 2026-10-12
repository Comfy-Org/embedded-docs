# LazyCache

LazyCache היא גרסה ניסיונית, תוצרת בית, של EasyCache שמוסיפה מטמון במהלך הדגימה כדי להפחית חישוב. היא מיועדת לתאימות אוניברסלית עם מודלים ב-ComfyUI, אם כי בדרך כלל היא מתפקדת פחות טוב מ-EasyCache ועשויה לעבוד טוב יותר רק במקרים נדירים.

## קלטים

| פרמטר | תיאור | סוג נתונים | נדרש | טווח |
| --- | --- | --- | --- | --- |
| `model` | המודל שאליו יש להוסיף את LazyCache. | MODEL | כן | - |
| `reuse_threshold` | הסף לשימוש חוזר בשלבים שנשמרו במטמון. ברירת מחדל: 0.2. | FLOAT | כן | 0.0 - 3.0 (step 0.01) |
| `start_percent` | שלב הדגימה היחסי שבו מתחילים להשתמש ב-LazyCache. ברירת מחדל: 0.15. | FLOAT | כן | 0.0 - 1.0 (step 0.01) |
| `end_percent` | שלב הדגימה היחסי שבו מסתיים השימוש ב-LazyCache. ברירת מחדל: 0.95. | FLOAT | כן | 0.0 - 1.0 (step 0.01) |
| `verbose` | האם לתעד מידע מפורט. ברירת מחדל: False. | BOOLEAN | כן | - |

הערה: `reuse_threshold`, `start_percent`, `end_percent` ו-`verbose` מסומנים כקלטים מתקדמים.

## פלטים

| שם פלט | תיאור | סוג נתונים |
| --- | --- | --- |
| `model` | המודל עם פונקציונליות LazyCache נוספת. | MODEL |

> מסמך זה נוצר על ידי בינה מלאכותית. אם מצאתם שגיאות או שיש לכם הצעות לשיפור, אתם מוזמנים לתרום! [עריכה ב-GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LazyCache/he.md)

---
**Source fingerprint (SHA-256):** `78f9c13473567e068fc2be35b2f8f5aa459d43d3f13300a6ea858af98d3e2a44`
