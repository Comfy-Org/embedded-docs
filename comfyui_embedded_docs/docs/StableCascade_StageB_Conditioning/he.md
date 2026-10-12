# StableCascade_StageB_Conditioning

הצומת StableCascade_StageB_Conditioning מכין נתוני התניה ליצירה בשלב B של Stable Cascade על ידי שילוב מידע התניה קיים עם ייצוג ה-latent המוקדם שנוצר בשלב C. הוא מעתיק כל רשומת התניה ומאחסן בתוכה את דגימות ה-latent משלב C, כך ששלבי יצירה מאוחרים יותר יוכלו להשתמש במידע מוקדם זה כדי לקבל תוצאות קוהרנטיות יותר.

## קלטים

| פרמטר | תיאור | סוג נתונים | נדרש | טווח |
| --- | --- | --- | --- | --- |
| `conditioning` | נתוני ההתניה שישתנו עם המידע המוקדם משלב C. כל רשומה ברשימה מועתקת ומקבלת את הדגימות משלב C. | CONDITIONING | כן | - |
| `stage_c` | הייצוג ה-latent משלב C. ערך ה-`samples` שלו משמש כמידע המוקדם שמתווסף להתניה. | LATENT | כן | - |

## פלטים

| שם פלט | תיאור | סוג נתונים |
| --- | --- | --- |
| `CONDITIONING` | נתוני ההתניה שהשתנו, עם המידע המוקדם משלב C משולב בהם. | CONDITIONING |

> מסמך זה נוצר על ידי בינה מלאכותית. אם מצאתם שגיאות או שיש לכם הצעות לשיפור, אתם מוזמנים לתרום! [עריכה ב-GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_StageB_Conditioning/he.md)

---
**Source fingerprint (SHA-256):** `3154457773465e5b93221b6d83d2064b565cb653403e12e88615652c7832d1e8`
