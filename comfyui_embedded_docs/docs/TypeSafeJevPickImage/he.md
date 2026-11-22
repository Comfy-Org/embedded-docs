# TypeSafe Jev (Pick Image)

צומת TypeSafe Jev (Pick Image) בוחר תמונה אחת מתוך אצווה. חבר את `index` אל Get Image from Batch כדי לשמור את התמונה שנבחרה, או קרא את `confidence` כדי להחליט האם הבחירה טובה מספיק. זהו צומת API ומצריך חשבון Comfy.org ומפתח API.

## קלטים

| פרמטר | תיאור | סוג נתונים | חובה | טווח |
| --- | --- | --- | --- | --- |
| `model` | מודל Jev לשימוש. כרגע זמין מודל אחד בלבד: `jev-1.14.0`. | COMBO | כן | `"jev-1.14.0"` |
| `question` | איזו תמונה לבחור. חבר את הפרומפט אל `text` כדי לבחור את התמונה המתאימה לו ביותר (ברירת מחדל: `Which image best matches the prompt in text? If there is no text, which image has the best quality?`). | STRING | כן | 1 עד 1000 תווים |
| `images` | התמונות שמהן לבחור. קלט באצווה נספר פעם אחת עבור כל תמונה, כך שכל תמונה באצווה היא מועמדת. | IMAGE | כן | 2 עד 32 תמונות |
| `text` | הטקסט שהשאלה מתייחסת אליו, כגון הפרומפט שממנו נוצרו התמונות. | STRING | לא | 0 עד 3000 תווים |

**הערות:**

- הצומת מעלה שגיאה כאשר מחוברות פחות מ-2 או יותר מ-32 תמונות.
- `index` נספר מ-0, וזהו המיקום ש-Get Image from Batch מצפה לו.
- החיוב מבוסס טוקנים; תג המחיר על הצומת מציג את התעריף המשוער לכל 1M טוקנים.

## פלטים

| שם פלט | תיאור | סוג נתונים |
| --- | --- | --- |
| `index` | המיקום של התמונה שנבחרה באצווה, החל מ-0. | INT |
| `confidence` | מידת הביטחון של Jev, מ-0 (אין מנצח ברור) עד 1 (ודאי). | FLOAT |

> מסמך זה נוצר על ידי בינה מלאכותית. אם מצאתם שגיאות או שיש לכם הצעות לשיפור, אתם מוזמנים לתרום! [עריכה ב-GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TypeSafeJevPickImage/he.md)

---
**Source fingerprint (SHA-256):** `432ee9ba69ebc0b452de4b52e94abdc56a65dc694a463a3654efb62b172c7b93`
