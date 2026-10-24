# Text Encode MOSS-Image Edit

קידוד הוראת עריכה יחד עם תמונות עזר ל-conditioning עבור LoRA לעריכת MOSS-Image. חברו את הפלט כ-conditioning חיובי, והריצו מופע שני עם אותן תמונות עזר עבור ה-conditioning השלילי. תמונות העזר משמשות בגודל שבו הן מגיעות, לכן יש לשנות את קנה המידה שלהן לפני החיבור. צומת זה מסומן כניסיוני ב-ComfyUI. בלי VAE התמונות מגיעות רק למקודד הטקסט.

## קלטים

| פרמטר | תיאור | סוג נתונים | חובה | טווח |
| --- | --- | --- | --- | --- |
| `clip` | מודל ה-CLIP שמבצע טוקניזציה של ההוראה ומקודד אותה. | CLIP | כן | - |
| `prompt` | ההוראה המתארת את העריכה. תומך בטקסט רב-שורתי ובפרומפטים דינמיים. | STRING | כן | כל טקסט |
| `vae` | ה-VAE המשמש לקידוד תמונות העזר ל-latent-ים של עזר. אופציונלי: בלעדיו התמונות מגיעות רק למקודד הטקסט.| VAE | לא | - |
| `edit_format` | הפריסה שבה אומן ה-LoRA לעריכה. היא בוחרת את שיטת ה-latent-ים של העזר ואת השאלה אם מקודד הטקסט רואה גם את תמונות העזר. | COMBO | כן | `"ai-toolkit"`<br>`"ai-toolkit (kv_cache off)"`<br>`"Moss-Image-Edit"` |
| `images` | חריץ מתרחב: חברו תמונת עזר אחת או יותר (`image_1`, `image_2`, ...). כל תמונה משמשת בגודל שבו היא מגיעה, ערוץ האלפא שלה מושמט, והיא מקודדת ב-VAE ל-latent של עזר. כש-VAE מחובר ערוץ האלפא מושמט וכל תמונה מקודדת ל-latent של עזר; בלי VAE התמונות מגיעות רק למקודד הטקסט.| IMAGE | כן | תמונה אחת או יותר |
| `image_strength` | משנה כמה המודל שם לב לתמונות שמקודד הטקסט רואה (פורמטי ai-toolkit או בלי VAE): 0 מתעלם, 1 ללא שינוי, מעל 1 מדגיש. מתקדם. ברירת מחדל: 1.0. | FLOAT | כן | 0.0 to 100.0 (step 0.05) |

**הערה:** With `"ai-toolkit"` and `"ai-toolkit (kv_cache off)"`, or when no VAE is connected and `image_strength` is above 0, the text encoder also sees every reference, downscaled to at most 384x384 pixels and preceded by a `Picture N:` marker in the prompt, so the instruction can refer to them by number. With `"Moss-Image-Edit"` and a VAE connected, the references reach the model only as reference latents and the text encoder sees the instruction alone. `"ai-toolkit (kv_cache off)"` additionally keeps the references attending to the image being generated, so they are recomputed on every sampling step.

## פלטים

| שם פלט | תיאור | סוג נתונים |
| --- | --- | --- |
| `conditioning` | ההוראה המקודדת, כשה-latent-ים של העזר ושיטת ה-latent-ים התואמת של העזר מצורפים אליה. | CONDITIONING |

> מסמך זה נוצר על ידי בינה מלאכותית. אם מצאתם שגיאות או שיש לכם הצעות לשיפור, אתם מוזמנים לתרום! [עריכה ב-GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeMOSSImageEdit/he.md)

---
**Source fingerprint (SHA-256):** `673f098df6a8e466a5c8060009f446eac8f7556311a870de626c5f4bfc3ab196`
