# PairConditioningSetDefaultAndCombine

הצומת **PairConditioningSetDefaultAndCombine** מגדיר ערכי conditioning של ברירת מחדל ומשלב אותם עם נתוני conditioning מהקלט. הוא מקבל קלטי conditioning חיוביים ושליליים יחד עם מקבילי ברירת המחדל שלהם, ואז מעבד אותם דרך מערכת ה-hooks של ComfyUI כדי להפיק פלטי conditioning סופיים שמשלבים את ערכי ברירת המחדל.

## קלטים

| פרמטר | תיאור | סוג נתונים | חובה | טווח |
| --- | --- | --- | --- | --- |
| `positive` | קלט ה-conditioning החיובי הראשי שיש לעבד | CONDITIONING | כן | - |
| `negative` | קלט ה-conditioning השלילי הראשי שיש לעבד | CONDITIONING | כן | - |
| `positive_DEFAULT` | ערכי ה-conditioning החיוביים של ברירת המחדל שישמשו כגיבוי | CONDITIONING | כן | - |
| `negative_DEFAULT` | ערכי ה-conditioning השליליים של ברירת המחדל שישמשו כגיבוי | CONDITIONING | כן | - |
| `hooks` | קבוצת hooks אופציונלית ללוגיקת עיבוד מותאמת אישית | HOOKS | לא | - |

## פלטים

| שם פלט | תיאור | סוג נתונים |
| --- | --- | --- |
| `positive` | ה-conditioning החיובי המעובד, עם ערכי ברירת המחדל משולבים בו | CONDITIONING |
| `negative` | ה-conditioning השלילי המעובד, עם ערכי ברירת המחדל משולבים בו | CONDITIONING |

> מסמך זה נוצר על ידי בינה מלאכותית. אם מצאתם שגיאות או שיש לכם הצעות לשיפור, אתם מוזמנים לתרום! [עריכה ב-GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PairConditioningSetDefaultCombine/he.md)

---
**Source fingerprint (SHA-256):** `dfa47d0fe02e81db8b68d20ae9b765c2518773f4f7fc8caf774cb870267dbb21`
