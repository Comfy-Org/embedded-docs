# EmptyChromaRadianceLatentImage

צומת EmptyChromaRadianceLatentImage יוצר תמונת latent ריקה עם הממדים שתציין, לשימוש בתהליכי chroma radiance. הוא מפיק טנזור מלא באפסים שמשמש כנקודת התחלה לפעולות במרחב ה-latent, ומאפשר לך להגדיר את הרוחב, הגובה וגודל האצווה של תמונת ה-latent הריקה.

## קלטים

| פרמטר | תיאור | סוג נתונים | חובה | טווח |
| --- | --- | --- | --- | --- |
| `width` | רוחב תמונת ה-latent בפיקסלים (ברירת מחדל: 1024) | INT | כן | 16 עד MAX_RESOLUTION |
| `height` | גובה תמונת ה-latent בפיקסלים (ברירת מחדל: 1024) | INT | כן | 16 עד MAX_RESOLUTION |
| `batch_size` | מספר תמונות ה-latent ליצירה באצווה (ברירת מחדל: 1) | INT | כן | 1 עד 4096 |

הערה: `width` ו-`height` מוגדרים עם צעד של 16, כך שהערכים מותאמים בכפולות של 16.

## פלטים

| שם פלט | תיאור | סוג נתונים |
| --- | --- | --- |
| `samples` | טנזור תמונת ה-latent הריקה שנוצר, מלא באפסים, בצורה batch_size x 3 x height x width | LATENT |

> מסמך זה נוצר על ידי בינה מלאכותית. אם מצאתם שגיאות או שיש לכם הצעות לשיפור, אתם מוזמנים לתרום! [עריכה ב-GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyChromaRadianceLatentImage/he.md)

---
**Source fingerprint (SHA-256):** `870cc89fb021c258c214db153cda0a32a63da1b6bf92f09cbd3b8498c363096b`
