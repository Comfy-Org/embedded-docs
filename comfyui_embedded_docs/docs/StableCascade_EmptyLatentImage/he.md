# StableCascade_EmptyLatentImage

צומת StableCascade_EmptyLatentImage יוצר טנזורים לטנטיים ריקים עבור מודלים של Stable Cascade. הוא מייצר שני ייצוגים לטנטיים נפרדים - אחד עבור שלב C ואחד עבור שלב B - עם ממדים המחושבים מרזולוציית הקלט ומהגדרות הדחיסה. צומת זה מספק נקודת התחלה עבור צינור היצירה של Stable Cascade.

## קלטים

| פרמטר | תיאור | סוג נתונים | נדרש | טווח |
| --- | --- | --- | --- | --- |
| `width` | הרוחב של תמונת הפלט בפיקסלים (ברירת מחדל: 1024, צעד: 8) | INT | כן | 256 עד MAX_RESOLUTION |
| `height` | הגובה של תמונת הפלט בפיקסלים (ברירת מחדל: 1024, צעד: 8) | INT | כן | 256 עד MAX_RESOLUTION |
| `compression` | מקדם הדחיסה שקובע את ממדי ה-latent עבור שלב C (ברירת מחדל: 42, צעד: 1). זהו פרמטר מתקדם. | INT | כן | 4 עד 128 |
| `batch_size` | מספר דגימות ה-latent ליצירה באצווה (ברירת מחדל: 1) | INT | כן | 1 עד 4096 |

הערה: הערך `compression` קובע את גודל ה-latent של שלב C: הגובה והרוחב שלו הם הקלט `height` וה-`width` חלקי `compression`. ה-latent של שלב B תמיד משתמש בדחיסה קבועה של 4.

## פלטים

| שם פלט | תיאור | סוג נתונים |
| --- | --- | --- |
| `stage_c` | טנזור ה-latent של שלב C עם ממדים [batch_size, 16, height//compression, width//compression] | LATENT |
| `stage_b` | טנזור ה-latent של שלב B עם ממדים [batch_size, 4, height//4, width//4] | LATENT |

> מסמך זה נוצר על ידי בינה מלאכותית. אם מצאתם שגיאות או שיש לכם הצעות לשיפור, אתם מוזמנים לתרום! [עריכה ב-GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_EmptyLatentImage/he.md)

---
**Source fingerprint (SHA-256):** `f336f87d0ec14b3716efda2cfaa194b1f80707d64821bb56ade7d88d9bd5b53f`
