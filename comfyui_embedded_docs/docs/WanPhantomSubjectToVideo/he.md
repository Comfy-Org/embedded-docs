# WanPhantomSubjectToVideo

צומת WanPhantomSubjectToVideo מכין נתוני conditioning ו-latent ליצירת וידאו של Wan. הוא יוצר טנזור וידאו latent ריק לפי ה-`width`, ה-`height`, ה-`length` וגודל ה-batch המבוקשים, וכאשר מסופקות תמונות עזר, הוא מקודד אותן באמצעות ה-VAE ומוסיף אותן ל-conditioning כהנחיה חזותית במימד הזמן.

## קלטים

| פרמטר | תיאור | סוג נתונים | נדרש | טווח |
| --- | --- | --- | --- | --- |
| `positive` | קלט conditioning חיובי להנחיית יצירת וידאו | CONDITIONING | כן | - |
| `negative` | קלט conditioning שלילי כדי להימנע ממאפיינים מסוימים | CONDITIONING | כן | - |
| `vae` | מודל VAE המשמש לקידוד תמונות העזר כאשר הן מסופקות | VAE | כן | - |
| `width` | רוחב וידאו הפלט בפיקסלים (ברירת מחדל: 832) | INT | כן | 16 to MAX_RESOLUTION (step 16) |
| `height` | גובה וידאו הפלט בפיקסלים (ברירת מחדל: 480) | INT | כן | 16 to MAX_RESOLUTION (step 16) |
| `length` | מספר הפריימים בווידאו שנוצר (ברירת מחדל: 81) | INT | כן | 1 to MAX_RESOLUTION (step 4) |
| `batch_size` | מספר הווידאוים ליצירה בו-זמנית (ברירת מחדל: 1) | INT | כן | 1 to 4096 |
| `images` | תמונות עזר אופציונליות המשמשות כהנחיה חזותית במימד הזמן | IMAGE | לא | - |

**הערה:** כאשר מסופקות `images`, הן מוגדלות אוטומטית כדי להתאים ל-`width` ול-`height` שצוינו, ורק `length` התמונות הראשונות משמשות לעיבוד. כל תמונה מקודדת עם ה-`vae` ומשורשרת לאורך מימד הזמן, ורק ערוצי ה-RGB של כל תמונה משמשים. כאשר `images` אינן מסופקות, כל שלושת פלטי ה-conditioning מוחזרים ללא שינוי מה-conditioning של הקלט.

## פלטים

| שם פלט | תיאור | סוג נתונים |
| --- | --- | --- |
| `positive` | conditioning חיובי עם שרשור במימד הזמן של תמונות העזר המקודדות כאשר מסופקות תמונות; אחרת קלט ה-`positive` מוחזר ללא שינוי | CONDITIONING |
| `negative_text` | conditioning שלילי עם שרשור במימד הזמן של תמונות העזר המקודדות כאשר מסופקות תמונות; אחרת קלט ה-`negative` מוחזר ללא שינוי | CONDITIONING |
| `negative_img_text` | conditioning שלילי עם שרשור מאופס במימד הזמן כאשר מסופקות תמונות; אחרת קלט ה-`negative` מוחזר ללא שינוי | CONDITIONING |
| `latent` | טנזור וידאו latent מלא באפסים עם 16 ערוצים; מספר הפריימים שלו נגזר מ-`length` והממדים המרחביים שלו מ-`height` ומ-`width` | LATENT |

> מסמך זה נוצר על ידי בינה מלאכותית. אם מצאתם שגיאות או שיש לכם הצעות לשיפור, אתם מוזמנים לתרום! [עריכה ב-GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanPhantomSubjectToVideo/he.md)

---
**Source fingerprint (SHA-256):** `a1853382f6e564f66262b69dd7b06cc58e26b93386a460a98e6fcc2ff6acf12b`
