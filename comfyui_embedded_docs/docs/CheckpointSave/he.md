# שמירת Checkpoint

הצומת `Save Checkpoint` מיועד לשמור מודל Stable Diffusion שלם (כולל רכיבי UNet, CLIP ו-VAE) כקובץ צ'קפוינט בפורמט **.safetensors**.

הצומת Save Checkpoint משמש בעיקר בזרימות עבודה של מיזוג מודלים. לאחר יצירת מודל ממוזג חדש באמצעות צמתים כמו `ModelMergeSimple`, `ModelMergeBlocks` וכו', ניתן להשתמש בצומת זה כדי לשמור את התוצאה כקובץ צ'קפוינט לשימוש חוזר.

## קלטים

| פרמטר | תיאור | סוג נתונים |
| --- | --- | --- |
| `model` | הפרמטר `model` מייצג את המודל הראשי שיש לשמור את מצבו. הוא חיוני ללכידת המצב הנוכחי של המודל לצורך שחזור או ניתוח עתידיים. | MODEL |
| `clip` | הפרמטר `clip` מיועד למודל CLIP המשויך למודל הראשי, ומאפשר לשמור את מצבו לצד המודל הראשי. | CLIP |
| `vae` | הפרמטר `vae` מיועד למודל Variational Autoencoder (VAE), ומאפשר לשמור את מצבו לשימוש או ניתוח עתידיים לצד המודל הראשי וה-CLIP. | VAE |
| `filename_prefix` | פרמטר זה מגדיר את הקידומת של שם הקובץ שבו יישמר הצ'קפוינט. | STRING |

בנוסף, לצומת יש שני קלטים נסתרים עבור מטא-נתונים:

**prompt (PROMPT)**: מידע על פרומפט של זרימת העבודה  
**extra_pnginfo (EXTRA_PNGINFO)**: מידע נוסף על PNG

## פלטים

צומת זה יפיק קובץ צ'קפוינט, ונתיב קובץ הפלט המתאים הוא הספרייה `output/checkpoints/`.

## תאימות ארכיטקטורה

- נתמך במלואו נכון להיום: SDXL, SD3, SVD וארכיטקטורות נפוצות אחרות, ראו [קוד מקור](https://github.com/comfyanonymous/ComfyUI/blob/master/comfy_extras/nodes_model_merging.py#L176-L189)
- תמיכה בסיסית: ניתן לשמור ארכיטקטורות אחרות, אך ללא מידע מטא-נתונים תקני

## קישורים קשורים

קוד מקור קשור: [nodes_model_merging.py#L227](https://github.com/comfyanonymous/ComfyUI/blob/master/comfy_extras/nodes_model_merging.py#L227)

> מסמך זה נוצר על ידי בינה מלאכותית. אם מצאתם שגיאות או שיש לכם הצעות לשיפור, אתם מוזמנים לתרום! [עריכה ב-GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CheckpointSave/he.md)
