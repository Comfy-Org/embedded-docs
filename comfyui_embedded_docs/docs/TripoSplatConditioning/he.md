# TripoSplatConditioning

צומת זה מקודד תמונת קלט באמצעות מקודד התמונות DINOv3 ו-VAE של Flux2 כדי להפיק נתוני התניה חיוביים ושליליים עבור מודל TripoSplat. הוא גם יוצר יעד רעש בגודל קבוע (latent בתוספת נתוני מצלמה) שמשמש כנקודת התחלה עבור KSampler.

## קלטים

| פרמטר | תיאור | סוג נתונים | חובה | טווח |
|-----------|-------------|-----------|----------|-------|
| `clip_vision` | מקודד תמונות DINOv3 ViT-H/16+ | CLIP_VISION | כן | - |
| `vae` | VAE של Flux2 | VAE | כן | - |
| `image` | תמונת הקלט לקידוד | IMAGE | כן | - |

## פלטים

| שם פלט | תיאור | סוג נתונים |
|-------------|-------------|-----------|
| `positive` | נתוני התניה חיוביים המכילים את רצף התכונות של DINOv3 ואת ה-latent של Flux2 VAE הנישא כ-latent עזר | CONDITIONING |
| `negative` | נתוני התניה שליליים המכילים תכונות DINOv3 מלאות באפסים ו-latent עזר של Flux2 VAE מלא באפסים | CONDITIONING |
| `latent` | יעד הרעש בגודל קבוע (latent + מצלמה) עבור ה-KSampler. ה-latent הוא רצף shape-code בעל צורה קבועה (8192 x 16) המשויך לטוקן מצלמה בודד (1 x 5) | LATENT |

> מסמך זה נוצר על ידי בינה מלאכותית. אם מצאתם שגיאות או שיש לכם הצעות לשיפור, אתם מוזמנים לתרום! [עריכה ב-GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoSplatConditioning/he.md)

---
**Source fingerprint (SHA-256):** `59ebeef272d125a2cc2045f4ff54f99268b1273d0a1fd46f7462e6d312f3a805`
