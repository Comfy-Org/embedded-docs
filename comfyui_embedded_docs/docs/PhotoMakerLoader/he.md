# PhotoMakerLoader

הצומת PhotoMakerLoader טוען מודל PhotoMaker מקובצי המודלים הזמינים. הוא קורא את הקובץ הנבחר, טוען את משקולות מקודד ה-ID שלו, ומכין את מקודד ה-ID של PhotoMaker לשימוש במשימות יצירת תמונות מבוססות זהות. צומת זה מסומן כניסיוני ומיועד למטרות בדיקה.

## קלטים

| פרמטר | תיאור | סוג נתונים | חובה | טווח |
| --- | --- | --- | --- | --- |
| `photomaker_model_name` | שם קובץ המודל PhotoMaker לטעינה. האפשרויות הזמינות נקבעות לפי קובצי המודלים הקיימים בתיקיית `photomaker`. | COMBO | כן | אפשרויות מרובות זמינות (מאוכלס באופן דינמי מתיקיית `photomaker`) |

## פלטים

| שם פלט | תיאור | סוג נתונים |
| --- | --- | --- |
| `photomaker_model` | מודל PhotoMaker הטעון המכיל את מקודד ה-ID, מוכן לשימוש בפעולות קידוד זהות. | PHOTOMAKER |

> מסמך זה נוצר על ידי בינה מלאכותית. אם מצאתם שגיאות או שיש לכם הצעות לשיפור, אתם מוזמנים לתרום! [עריכה ב-GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PhotoMakerLoader/he.md)

---
**Source fingerprint (SHA-256):** `1b26630fadbdc144cd42ca7393f743b079ee7463deb9c8b31b628b5dc7432317`
