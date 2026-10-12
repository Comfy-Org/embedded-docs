# ImageOnlyCheckpointSave

צומת זה שומר קובץ צ'קפוינט אשר כולל מודל יחד עם מקודד ה-CLIP vision שלו וה-VAE. הקובץ נכתב בפורמט safetensors לתיקיית הפלט, תוך שימוש בקידומת שם הקובץ שצוינה, כך שניתן לאחסן את רכיבי המודל הקשורים לתמונה כצ'קפוינט יחיד.

## קלטים

| פרמטר | תיאור | סוג נתונים | נדרש | טווח |
| --- | --- | --- | --- | --- |
| `model` | המודל שיש לשמור בצ'קפוינט | MODEL | כן | - |
| `clip_vision` | מקודד ה-CLIP vision שיש לשמור בצ'קפוינט | CLIP_VISION | כן | - |
| `vae` | ה-VAE (מקודד אוטומטי וריאציוני) שיש לשמור בצ'קפוינט | VAE | כן | - |
| `filename_prefix` | הקידומת עבור שם קובץ הפלט (ברירת מחדל: "checkpoints/ComfyUI") | STRING | כן | - |
| `prompt` | פרמטר מוסתר שמקבל את נתוני הפרומפט של זרימת העבודה | PROMPT | לא | - |
| `extra_pnginfo` | פרמטר מוסתר שמקבל מטא-נתוני PNG נוספים | EXTRA_PNGINFO | לא | - |

## פלטים

| שם פלט | תיאור | סוג נתונים |
| --- | --- | --- |
| - | צומת זה אינו מחזיר פלטים | - |

> מסמך זה נוצר על ידי בינה מלאכותית. אם מצאתם שגיאות או שיש לכם הצעות לשיפור, אתם מוזמנים לתרום! [עריכה ב-GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageOnlyCheckpointSave/he.md)

---
**Source fingerprint (SHA-256):** `8ff4b3a78d8da523eaa5f784f847e954ba73b4d6037e748dcce592b447fcdee9`
