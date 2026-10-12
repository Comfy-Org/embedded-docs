# מנגנון הקשב של המודל

צומת זה בוחר את מימוש הקשב הצפוף (dense attention) עבור מודל, משכפל את המודל, מחיל את ה-backend שנבחר ומחזיר את השכפול המעודכן. כאשר משתמשים בו עם Block Sparse Attention, ה-backend הזה משמש בכל פעם שקשב sparse אינו פעיל או אינו נתמך. אם ה-backend שנבחר אינו זמין, הצומת עובר באופן אוטומטי ל-PyTorch attention.

## קלטים

| פרמטר | תיאור | סוג נתונים | חובה | טווח |
|-----------|-------------|-----------|----------|-------|
| `model` | המודל שעליו להחיל את התיקון. | MODEL | כן |  |
| `attention` | ה-backend של קשב צפוף להחלה. Comfy Kitchen attention משתמש בקשב INT8 מכומת וזמין רק ב-GPU של Nvidia ו-AMD. ברירת מחדל: "pytorch attention". אם ה-backend שנבחר אינו זמין, נעשה שימוש ב-PyTorch attention כגיבוי. | COMBO | כן | "pytorch attention"<br>"comfy kitchen attention" |

הערה: האפשרות "comfy kitchen attention" מוצגת רק כאשר מודול ה-INT8 attention של Comfy Kitchen זמין בסביבה הנוכחית.

## פלטים

| שם פלט | תיאור | סוג נתונים |
|-------------|-------------|-----------|
| `model` | שכפול של מודל הקלט שעליו הוחל ה-backend של הקשב שנבחר. | MODEL |

> מסמך זה נוצר על ידי בינה מלאכותית. אם מצאתם שגיאות או שיש לכם הצעות לשיפור, אתם מוזמנים לתרום! [עריכה ב-GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelAttentionBackend/he.md)

---
**Source fingerprint (SHA-256):** `4f6e4800c2a3bb09b47b7c8f0481e1b6de3070f57234e610df5d3ce60dfdb309`
