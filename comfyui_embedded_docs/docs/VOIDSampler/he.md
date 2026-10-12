# VOIDSampler

VOIDSampler הוא סמפלר DDIM ייעודי המיועד למודלי inpainting של VOID. הוא משחזר את תהליך הסרת הרעש המדויק שבו אומן VOID, תוך דילוג על התאמת קנה המידה של הרעש שסמפלרי KSampler סטנדרטיים מיישמים. השתמש בצומת זה יחד עם SamplerCustom או SamplerCustomAdvanced, בשילוב עם RandomNoise או VOIDWarpedNoiseSource.

## קלטים

לצומת זה אין פרמטרי קלט ניתנים להגדרה. זהו סמפלר עצמאי שמיישם אלגוריתם דגימת DDIM קבוע.

| פרמטר | תיאור | סוג נתונים | נדרש | טווח |
| --- | --- | --- | --- | --- |
| *ללא קלטים* | צומת זה אינו מקבל פרמטרי קלט כלשהם. | - | - | - |

## פלטים

| שם פלט | תיאור | סוג נתונים |
| --- | --- | --- |
| `SAMPLER` | אובייקט סמפלר שמיישם את אלגוריתם VOID DDIM, מוכן לחיבור לצמתים SamplerCustom או SamplerCustomAdvanced. | SAMPLER |

> מסמך זה נוצר על ידי בינה מלאכותית. אם מצאתם שגיאות או שיש לכם הצעות לשיפור, אתם מוזמנים לתרום! [עריכה ב-GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDSampler/he.md)

---
**Source fingerprint (SHA-256):** `b8bb6d3d7220cca4a6dd252efe9c92953b1c5c67c14365e5e0583bc9bdb133be`
