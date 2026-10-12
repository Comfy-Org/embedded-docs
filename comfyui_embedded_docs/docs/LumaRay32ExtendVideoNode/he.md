# LumaRay32ExtendVideoNode

Luma Ray 3.2 Extend Video ממשיך יצירת וידאו קודמת של Luma Ray 3.2 על ידי יצירת מקטע חדש באורך 5 שניות, או אחרי הקליפ המקורי (forward) או לפניו (backward). חבר את הפלט `generation_id` מצומת Luma Ray 3.2 קודם כדי להשתמש בקליפ הזה כפריים ההתחלתי (forward) או כפריים הסיום (backward) של ההארכה. ההארכות הן תמיד באורך 5 שניות.

## קלטים

### קלטים משותפים

| פרמטר | תיאור | סוג נתונים | נדרש | טווח |
|-----------|-------------|-----------|----------|-------|
| `source_generation_id` | מזהה יצירה (Generation ID) של וידאו Ray 3.2 קודם שיש להאריך. חבר את הפלט `generation_id` של צומת Luma Ray 3.2 אחר. ברירת מחדל: "" (ריק). ערך זה נדרש ואסור שיהיה ריק. | STRING | כן | – |
| `direction` | כיוון קדימה ממשיך אחרי הקליפ הקודם; כיוון אחורה נוסף לפניו. קדימה משתמש בקליפ המקור כפריים ההתחלתי; אחורה משתמש בו כפריים הסיום. בחירה ב-"Forward (continue after)" מוסיפה את האפשרות `loop`. | DYNAMIC_COMBO | כן | "Forward (continue after)"<br>"Backward (lead-in before)" |
| `prompt` | פרומפט טקסט עבור התוכן החדש. ברירת מחדל: "" (ריק). חייב להיות בין 1 ל-6000 תווים. | STRING | כן | 1 to 6000 characters |
| `resolution` | רזולוציית הפלט עבור מקטע הווידאו המוארך. ברירת מחדל: "720p". | COMBO | כן | "540p"<br>"720p"<br>"1080p" |
| `seed` | Seed לקביעה אם הצומת צריך לרוץ מחדש; התוצאות אינן דטרמיניסטיות ללא תלות ב-seed. ברירת מחדל: 0. | INT | כן | 0 to 0xFFFFFFFFFFFFFFFF (18446744073709551615) |

### קלטים של Forward (continue after)

| פרמטר | תיאור | סוג נתונים | נדרש | טווח |
|-----------|-------------|-----------|----------|-------|
| `loop` | הפעל לולאה על הווידאו המוארך בצורה חלקה (הארכת קדימה בלבד). ברירת מחדל: False. | BOOLEAN | לא | True<br>False |

### קלטים של Backward (lead-in before)

כיוון זה אינו מוסיף פרמטרים נוספים.

**הערה:** ההארכות הן תמיד 5 שניות. הפרמטר `loop` זמין רק כאשר `direction` הוא "Forward (continue after)"; כאשר משתמשים ב-"Backward (lead-in before)", האפשרות `loop` אינה זמינה. ה-`prompt` חייב להיות בין 1 ל-6000 תווים. ה-`source_generation_id` נדרש וחייב להיות מחובר לפלט `generation_id` של צומת Luma Ray 3.2 קודם.

## פלטים

| שם פלט | תיאור | סוג נתונים |
|-------------|-------------|-----------|
| `VIDEO` | מקטע הווידאו המוארך באורך 5 שניות שנוצר. | VIDEO |
| `generation_id` | מזהה ייחודי ליצירה זו, שניתן לחבר אותו לצומת Luma Ray 3.2 Extend Video אחרת להארכות נוספות. | STRING |

> מסמך זה נוצר על ידי בינה מלאכותית. אם מצאתם שגיאות או שיש לכם הצעות לשיפור, אתם מוזמנים לתרום! [עריכה ב-GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaRay32ExtendVideoNode/he.md)

---
**Source fingerprint (SHA-256):** `a67ca53d4bcb9f3fd82bc0482b579f5f7fe4bf866f8d83cb922e1082ad320057`
