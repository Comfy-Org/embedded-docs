# צור Hook Model כ-LoRA (MO)

צומת זה יוצר וו (Hook) שמחיל מודל LoRA (התאמה בדרגה נמוכה) כדי לשנות רק את רכיב המודל של רשת עצבית. הוא טוען קובץ Checkpoint ומחיל אותו בעוצמה מוגדרת על המודל, בעוד רכיב ה-CLIP נשאר ללא שינוי. זהו צומת ניסיוני שמרחיב את הפונקציונליות של מחלקת הבסיס CreateHookModelAsLora.

## קלטים

| פרמטר | תיאור | סוג נתונים | חובה | טווח |
| --- | --- | --- | --- | --- |
| `ckpt_name` | קובץ ה-Checkpoint לטעינה כמודל LoRA. האפשרויות הזמינות תלויות בתכולת תיקיית ה-Checkpoints. | STRING | כן | אפשרויות מרובות זמינות |
| `strength_model` | מכפיל העוצמה להחלת ה-LoRA על רכיב המודל (ברירת מחדל: 1.0) | FLOAT | כן | -20.0 עד 20.0 |
| `prev_hooks` | ווים קודמים אופציונליים לשרשור עם הוו הזה | HOOKS | לא | - |

## פלטים

| שם פלט | תיאור | סוג נתונים |
| --- | --- | --- |
| `hooks` | קבוצת הווים שנוצרה ומכילה את שינוי מודל ה-LoRA | HOOKS |

> מסמך זה נוצר על ידי בינה מלאכותית. אם מצאתם שגיאות או שיש לכם הצעות לשיפור, אתם מוזמנים לתרום! [עריכה ב-GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateHookModelAsLoraModelOnly/he.md)

---
**Source fingerprint (SHA-256):** `adbeaede65aa89d48c59225ca1c8edc4c9394a364f93a00dae4a83a2270f093b`
