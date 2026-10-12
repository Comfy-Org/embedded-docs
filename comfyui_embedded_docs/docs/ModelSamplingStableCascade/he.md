# ModelSamplingStableCascade

הצומת ModelSamplingStableCascade מיישם הגדרות דגימה של Stable Cascade על מודל על ידי החלת ערך shift על פרמטרי הדגימה. הוא מחזיר עותק patched של מודל הקלט עם תצורת דגימת Stable Cascade מותאמת אישית, ומשאיר את המודל המקורי ללא שינוי.

## קלטים

| פרמטר | תיאור | סוג נתונים | חובה | טווח |
| --- | --- | --- | --- | --- |
| `model` | מודל הקלט שעליו יש להחיל דגימת Stable Cascade | MODEL | כן | - |
| `shift` | ערך ה-shift המוחל על פרמטרי הדגימה (ברירת מחדל: 2.0) | FLOAT | כן | 0.0 - 100.0 (step 0.01) |

## פלטים

| שם פלט | תיאור | סוג נתונים |
| --- | --- | --- |
| `model` | המודל המשונה שעבורו הוחלה דגימת Stable Cascade | MODEL |

> מסמך זה נוצר על ידי בינה מלאכותית. אם מצאתם שגיאות או שיש לכם הצעות לשיפור, אתם מוזמנים לתרום! [עריכה ב-GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingStableCascade/he.md)

---
**Source fingerprint (SHA-256):** `358681a7c698d4335cde60780d5a8b134b75df4ea40102bf51544c53bbb08c42`
