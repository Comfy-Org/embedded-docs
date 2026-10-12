# ComfySoftSwitchNode

הצומת Soft Switch בוחר בין שני ערכי קלט אפשריים בהתבסס על תנאי בוליאני. הוא מוציא את הערך מהקלט `on_true` כאשר `switch` הוא true, ואת הערך מהקלט `on_false` כאשר `switch` הוא false. צומת זה מתוכנן להיות עצלן (lazy), כלומר הוא מעריך רק את הקלט שנדרש בפועל בהתבסס על מצב ה-switch.

## קלטים

| פרמטר | תיאור | סוג נתונים | חובה | טווח |
| --- | --- | --- | --- | --- |
| `switch` | התנאי הבוליאני שקובע איזה קלט יועבר הלאה. כאשר true, נבחר הקלט `on_true`. כאשר false, נבחר הקלט `on_false`. | BOOLEAN | כן | True or False |
| `on_false` | הערך שיוחזר כאשר תנאי ה-`switch` הוא false. קלט זה אופציונלי, אך יש לחבר לפחות אחד מהקלטים `on_false` או `on_true`. | MATCH_TYPE | לא | אותו סוג נתונים כמו `on_true` |
| `on_true` | הערך שיוחזר כאשר תנאי ה-`switch` הוא true. קלט זה אופציונלי, אך יש לחבר לפחות אחד מהקלטים `on_false` או `on_true`. | MATCH_TYPE | לא | אותו סוג נתונים כמו `on_false` |

**הערה:** הקלטים `on_false` ו-`on_true` חייבים להיות מאותו סוג נתונים, כפי שמוגדר בתבנית הפנימית של הצומת. יש לחבר לפחות אחד משני הקלטים הללו, אחרת הצומת מחזיר את הודעת האימות "At least one of on_false or on_true must be connected to Switch node". מכיוון שהצומת עצלן, כאשר רק קלט אחד מחובר, הצומת תמיד מוציא את הערך של אותו קלט ללא קשר למצב ה-`switch`.

## פלטים

| שם פלט | תיאור | סוג נתונים |
| --- | --- | --- |
| `output` | הערך הנבחר. הוא תואם לסוג הנתונים של הקלט המחובר `on_false` או `on_true`. כאשר שני הקלטים מחוברים, הוא מוציא `on_true` אם `switch` הוא true, ו-`on_false` אם `switch` הוא false. | MATCH_TYPE |

> מסמך זה נוצר על ידי בינה מלאכותית. אם מצאתם שגיאות או שיש לכם הצעות לשיפור, אתם מוזמנים לתרום! [עריכה ב-GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfySoftSwitchNode/he.md)

---
**Source fingerprint (SHA-256):** `7bf4bed69d8fd8c360e971ab8068382cd8ebaa02004d5df44312977a7309ae00`
