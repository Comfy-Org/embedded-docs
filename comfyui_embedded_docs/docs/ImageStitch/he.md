# חבר תמונות

צומת זה מאפשר לחבר שתי תמונות יחד בכיוון מוגדר (למעלה, למטה, שמאלה, ימינה), עם תמיכה בהתאמת גדלים וריווח בין התמונות.

## קלטים

| שם פרמטר | תיאור | סוג נתונים | סוג קלט | ברירת מחדל | טווח |
| --- | --- | --- | --- | --- | --- |
| `image1` | התמונה הראשונה לחיבור | IMAGE | נדרש | - | - |
| `image2` | התמונה השנייה לחיבור; אם לא מסופקת, מוחזרת רק התמונה הראשונה | IMAGE | אופציונלי | None | - |
| `direction` | הכיוון לחיבור התמונה השנייה: right, down, left או up | STRING | נדרש | right | right/down/left/up |
| `match_image_size` | האם לשנות את גודל התמונה השנייה כדי שתתאים למידות התמונה הראשונה | BOOLEAN | נדרש | True | True/False |
| `spacing_width` | רוחב הריווח בין התמונות; חייב להיות מספר זוגי | INT | נדרש | 0 | 0-1024 |
| `spacing_color` | צבע הריווח בין התמונות המחוברות | STRING | נדרש | white | white/black/red/green/blue |

> עבור `spacing_color`, בעת שימוש בצבעים שאינם "white/black", אם `match_image_size` מוגדר ל-`false`, אזור הריפוד ימולא בצבע black

## פלטים

| שם פלט | תיאור | סוג נתונים |
| --- | --- | --- |
| `IMAGE` | התמונה המחוברת | IMAGE |

## דוגמת זרימת עבודה

בזרימת העבודה שלהלן, אנו משתמשים ב-3 תמונות קלט בגדלים שונים כדוגמאות:

- image1: 500x300
- image2: 400x250
- image3: 300x300

![workflow](./asset/workflow.webp)

**צומת חיבור התמונה הראשונה**

- `match_image_size`: false, התמונות יחוברו בגדלים המקוריים שלהן
- `direction`: up, `image2` יוצב מעל `image1`
- `spacing_width`: 20
- `spacing_color`: black

תמונת פלט 1:

![output1](./asset/output-1.webp)

**צומת חיבור התמונה השנייה**

- `match_image_size`: true, התמונה השנייה תותאם בקנה מידה לגובה או לרוחב של התמונה הראשונה
- `direction`: right, `image3` תופיע בצד ימין
- `spacing_width`: 20
- `spacing_color`: white

תמונת פלט 2:

![output2](./asset/output-2.webp)

> מסמך זה נוצר על ידי בינה מלאכותית. אם מצאתם שגיאות או שיש לכם הצעות לשיפור, אתם מוזמנים לתרום! [עריכה ב-GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageStitch/he.md)
