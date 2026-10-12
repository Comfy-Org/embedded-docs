# טעינת מודל הגדלת latent

צומת `LatentUpscaleModelLoader` טוען מודל המתמחה בהגדלת ייצוגי latent מקובץ המאוחסן בתיקיית `latent_upscale_models` של ComfyUI. הוא מזהה אוטומטית את ארכיטקטורת המודל מתוך תוכן הקובץ (Hunyuan Video 720p, Hunyuan Video 1080p או Latent Upsampler) ומגדיר את המודל הפנימי המתאים, כך שהתוצאה מוכנה לשימוש על ידי צמתים אחרים.

## קלטים

| פרמטר | תיאור | סוג נתונים | חובה | טווח |
| --- | --- | --- | --- | --- |
| `model_name` | שם קובץ מודל הגדלת ה-latent שיש לטעון. האפשרויות הזמינות מאוכלסות באופן דינמי מהקבצים הקיימים בתיקיית `latent_upscale_models` של ComfyUI. | COMBO | כן | כל הקבצים בתיקיית `latent_upscale_models` |

## פלטים

| שם פלט | תיאור | סוג נתונים |
| --- | --- | --- |
| `model` | מודל הגדלת ה-latent שנטען, מוגדר ומוכן לשימוש. בהתאם לתוכן הקובץ שזוהה, זהו מעלה רזולוציה של Hunyuan Video 720p, מעלה רזולוציה של Hunyuan Video 1080p, או מודל Latent Upsampler עטוף. | LATENT_UPSCALE_MODEL |

> מסמך זה נוצר על ידי בינה מלאכותית. אם מצאתם שגיאות או שיש לכם הצעות לשיפור, אתם מוזמנים לתרום! [עריכה ב-GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentUpscaleModelLoader/he.md)

---
**Source fingerprint (SHA-256):** `7e23214b1b1fc11be84910a5a209c7990a5199120cb0e6b6c61302a442dcf153`
