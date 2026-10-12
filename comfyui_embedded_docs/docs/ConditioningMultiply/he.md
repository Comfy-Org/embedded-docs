# ConditioningMultiply

צומת זה מכפיל את ערכי ה-conditioning בגורם מוגדר, ומאפשר לך לשנות את עוצמת ההשפעה של ה-conditioning על תהליך היצירה. הוא פועל על ידי החלת המכפיל הן על טנזור ה-conditioning הראשי והן על ערכי הפלט ה-pooled.

## קלטים

| פרמטר | תיאור | סוג נתונים | חובה | טווח |
|-----------|-------------|-----------|----------|-------|
| `conditioning` | נתוני ה-conditioning שיש לשנות את קנה המידה שלהם | CONDITIONING | כן | - |
| `multiplier` | הגורם שבו יש להכפיל את ערכי ה-conditioning (ברירת מחדל: 1.0) | FLOAT | כן | -100.0 עד 100.0 (צעד: 0.01) |

## פלטים

| שם פלט | תיאור | סוג נתונים |
|-------------|-------------|-----------|
| `CONDITIONING` | נתוני ה-conditioning שעברו שינוי קנה מידה, עם ערכים מוכפלים | CONDITIONING |

> מסמך זה נוצר על ידי בינה מלאכותית. אם מצאתם שגיאות או שיש לכם הצעות לשיפור, אתם מוזמנים לתרום! [עריכה ב-GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningMultiply/he.md)

---
**Source fingerprint (SHA-256):** `8d241e3d5d91e513c24ade5b4bece4bf879fe093a4be6d53dab11a5a0bf55616`
