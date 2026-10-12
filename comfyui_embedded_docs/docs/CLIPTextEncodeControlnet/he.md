# CLIPTextEncodeControlnet

צומת CLIP Text Encode (Controlnet) מקודד פרומפט טקסט באמצעות מודל CLIP ומוסיף את קידוד הטקסט הנוצר לנתוני התניה קיימים. הוא מאחסן את הטמעות הטקסט כפרמטרי cross-attention של controlnet בתוך כל רשומת התניה, כך שההתניה המוחזרת נושאת את מידע ה-controlnet הנוסף הזה.

## קלטים

| פרמטר | תיאור | סוג נתונים | נדרש | טווח |
| --- | --- | --- | --- | --- |
| `clip` | מודל ה-CLIP המשמש לטוקניזציה וקידוד טקסט | CLIP | כן | - |
| `conditioning` | נתוני התניה קיימים שיש לשלב עם קידוד הטקסט של CLIP | CONDITIONING | כן | - |
| `text` | פרומפט הטקסט שיעובד על ידי מודל CLIP. תומך בטקסט מרובה שורות ובפרומפטים דינמיים | STRING | כן | - |

**הערה:** כל שלושת הקלטים (`clip`, `conditioning` ו-`text`) נדרשים כדי שצומת זה יפעל. הקלט `text` תומך בטקסט מרובה שורות ובפרומפטים דינמיים לעיבוד טקסט גמיש. צומת זה מסומן כניסיוני בקוד המקור.

## פלטים

| שם פלט | תיאור | סוג נתונים |
| --- | --- | --- |
| `CONDITIONING` | נתוני התניה משופרים עם פרמטרי cross-attention של controlnet שנוספו (`cross_attn_controlnet` ו-`pooled_output_controlnet`) הנגזרים מקידוד הטקסט של CLIP | CONDITIONING |

> מסמך זה נוצר על ידי בינה מלאכותית. אם מצאתם שגיאות או שיש לכם הצעות לשיפור, אתם מוזמנים לתרום! [עריכה ב-GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeControlnet/he.md)

---
**Source fingerprint (SHA-256):** `95a798684ca8734bfff53c7b979b320f6834dc1a9553163d0e567243761000f1`
