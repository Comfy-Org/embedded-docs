# UnclipCheckpointLoader

צומת זה יזהה מודלים הממוקמים בתיקייה `ComfyUI/models/checkpoints`, וכן יקרא מודלים מנתיבים נוספים המוגדרים בקובץ extra_model_paths.yaml. לעיתים ייתכן שתצטרך **לרענן את ממשק ComfyUI** כדי לאפשר לו לקרוא את קובצי המודל מהתיקייה המתאימה.

הצומת unCLIPCheckpointLoader מיועד לטעינת צ'קפוינטים המותאמים במיוחד למודלים של unCLIP. הוא מאפשר אחזור ואתחול של מודלים, מודולי CLIP vision ומודולי VAE מצ'קפוינט מוגדר, ומייעל את תהליך ההכנה עבור פעולות או ניתוחים נוספים.

## קלטים

| שדה | תיאור | Comfy dtype |
| --- | --- | --- |
| `ckpt_name` | מציין את שם הצ'קפוינט שיש לטעון; מזהה ומאחזר את קובץ הצ'קפוינט הנכון מתיקייה מוגדרת מראש, וקובע את האתחול של המודלים והתצורות. | `COMBO[STRING]` |

## פלטים

| שדה | תיאור | Comfy dtype | Python dtype |
| --- | --- | --- | --- |
| `model` | מייצג את המודל הראשי הנטען מהצ'קפוינט. | `MODEL` | `torch.nn.Module` |
| `clip` | מייצג את מודול CLIP הנטען מהצ'קפוינט, אם זמין. | `CLIP` | `torch.nn.Module` |
| `vae` | מייצג את מודול VAE הנטען מהצ'קפוינט, אם זמין. | `VAE` | `torch.nn.Module` |
| `clip_vision` | מייצג את מודול CLIP vision הנטען מהצ'קפוינט, אם זמין. | `CLIP_VISION` | `torch.nn.Module` |

> מסמך זה נוצר על ידי בינה מלאכותית. אם מצאתם שגיאות או שיש לכם הצעות לשיפור, אתם מוזמנים לתרום! [עריכה ב-GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/unCLIPCheckpointLoader/he.md)
