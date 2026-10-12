# Recraft Style - ספריית סגנונות אינסופית

צומת זה מאפשר לך לבחור סגנון מתוך ספריית הסגנונות האינסופית של Recraft (Infinite Style Library) באמצעות UUID קיים מראש. הוא מאחזר את פרטי הסגנון על סמך מזהה הסגנון שסופק ומחזיר אותם לשימוש בצמתי Recraft אחרים.

## קלטים

| פרמטר | תיאור | סוג נתונים | חובה | טווח |
|-----------|-------------|-----------|----------|-------|
| `style_id` | UUID של סגנון מתוך Infinite Style Library. | STRING | כן | כל UUID תקין |

**הערה:** הקלט `style_id` לא יכול להיות ריק. אם מסופקת מחרוזת ריקה, הצומת יזרוק חריגה.

## פלטים

| שם פלט | תיאור | סוג נתונים |
|-------------|-------------|-----------|
| `recraft_style` | אובייקט הסגנון הנבחר מתוך ספריית הסגנונות האינסופית של Recraft | STYLEV3 |

> מסמך זה נוצר על ידי בינה מלאכותית. אם מצאתם שגיאות או שיש לכם הצעות לשיפור, אתם מוזמנים לתרום! [עריכה ב-GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftStyleV3InfiniteStyleLibrary/he.md)

---
**Source fingerprint (SHA-256):** `4554acaaba9e83373d6fb44ea5465175182efcf7c9220c2328c4749c2febd40f`
