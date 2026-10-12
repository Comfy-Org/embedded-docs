# PiDConditioning

מצרף latent וערך degrade_sigma ל-CONDITIONING כך שניתן להשתמש בו לפענוח PiD או להגדלה. זה מאפשר לך לשלוט במידת ההידרדרות של ה-latent לפני עיבודו.

## קלטים

| פרמטר | תיאור | סוג נתונים | חובה | טווח |
|-----------|-------------|-----------|----------|-------|
| `positive` | נתוני ה-conditioning שאליהם יש לצרף את ה-latent ואת ערך ה-degrade_sigma. | CONDITIONING | כן | - |
| `latent` | ה-latent (מ-VAEEncode או מ-KSampler) שיש לצרף ל-conditioning. | LATENT | כן | - |
| `latent_format` | הפורמט של ה-latent. לטנטים מסוג Flux1 (16 ערוצים) ו-Flux2 (128 ערוצים) מזוהים אוטומטית מממד הערוצים תחת "flux". עבור SD3 (16 ערוצים), SDXL (4 ערוצים) או QwenImage (16 ערוצים), יש לבחור ידנית (ברירת מחדל: "flux"). | COMBO | כן | `"flux"`<br>`"sd3"`<br>`"sdxl"`<br>`"qwenimage"` |
| `degrade_sigma` | מידת ההידרדרות להחלה. 0 פירושו latent נקי. יש להגדיל ערך זה כדי להסיר רעש מפלטי latent פגומים (ברירת מחדל: 0.0). | FLOAT | כן | 0.0 עד 1.0 (צעד: 0.01) |

הערה: כאשר `latent_format` מוגדר ל-`"flux"`, הצומת מזהה אוטומטית את סוג ה-latent מממד הערוצים: 128 ערוצים מטופלים כ-latent מסוג Flux2, ואילו 16 ערוצים מטופלים כ-latent מסוג Flux1.

הערה: ערך `latent_format` שאינו נתמך יגרום לשגיאה, אך כל האפשרויות הזמינות מטופלות על ידי הצומת.

## פלטים

| שם פלט | תיאור | סוג נתונים |
|-------------|-------------|-----------|
| `CONDITIONING` | נתוני ה-conditioning המקוריים שאליהם מצורפים ה-latent וערך ה-degrade_sigma. | CONDITIONING |

> מסמך זה נוצר על ידי בינה מלאכותית. אם מצאתם שגיאות או שיש לכם הצעות לשיפור, אתם מוזמנים לתרום! [עריכה ב-GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PiDConditioning/he.md)

---
**Source fingerprint (SHA-256):** `24f613b33e7872cb35f458aa5794a3cc4d37ceaecd43725039edef75f4a512bc`
