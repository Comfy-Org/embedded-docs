# StabilityUpscaleCreativeNode

הגדל תמונה תוך שינויים מינימליים לרזולוציית 4K. צומת זה משתמש בטכנולוגיית ההגדלה היצירתית של Stability AI כדי לשפר את רזולוציית התמונה תוך שמירה על התוכן המקורי והוספת פרטים יצירתיים עדינים.

## קלטים

| פרמטר | תיאור | סוג נתונים | נדרש | טווח |
|-----------|-------------|-----------|----------|-------|
| `image` | התמונה הנכנסת שיש להגדיל | IMAGE | כן | - |
| `prompt` | מה תרצה לראות בתמונת הפלט. הנחיה חזקה ותיאורית שמגדירה בבירור אלמנטים, צבעים ונושאים תוביל לתוצאות טובות יותר. (ברירת מחדל: מחרוזת ריקה) | STRING | כן | - |
| `creativity` | שולט בסבירות ליצירת פרטים נוספים שאינם מותנים במידה רבה בתמונת האתחול. (ברירת מחדל: 0.3) | FLOAT | כן | 0.1-0.5 |
| `style_preset` | סגנון רצוי אופציונלי לתמונה שנוצרה. (ברירת מחדל: "None") | STRING | כן | `"3d-model"`<br>`"analog-film"`<br>`"anime"`<br>`"cinematic"`<br>`"comic-book"`<br>`"digital-art"`<br>`"enhance"`<br>`"fantasy-art"`<br>`"isometric"`<br>`"line-art"`<br>`"low-poly"`<br>`"modeling-compound"`<br>`"neon-punk"`<br>`"origami"`<br>`"photographic"`<br>`"pixel-art"`<br>`"tile-texture"` |
| `seed` | הזרע האקראי המשמש ליצירת הרעש. (ברירת מחדל: 0) | INT | כן | 0-4294967294 |
| `negative_prompt` | מילות מפתח של מה שאינך רוצה לראות בתמונת הפלט. זהו תכונה מתקדמת. (ברירת מחדל: מחרוזת ריקה) | STRING | לא | - |

## פלטים

| שם פלט | תיאור | סוג נתונים |
|-------------|-------------|-----------|
| `image` | התמונה המוגדלת ברזולוציית 4K | IMAGE |

> מסמך זה נוצר על ידי בינה מלאכותית. אם מצאתם שגיאות או שיש לכם הצעות לשיפור, אתם מוזמנים לתרום! [עריכה ב-GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StabilityUpscaleCreativeNode/he.md)

---
**Source fingerprint (SHA-256):** `dc9bfacee3bfa663cff22cd0bcef6759f7808e2ae8e19526de28d55a3bef26e6`
