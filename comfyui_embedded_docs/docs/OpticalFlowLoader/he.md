# טעינת מודל Optical Flow

טוען מודל זרימה אופטית (optical flow) מתיקיית `models/optical_flow/`. נכון לעכשיו, נתמך רק פורמט RAFT-large של torchvision, שהוא המודל שבו משתמש הצומת VOIDWarpedNoise. ComfyUI לא מוריד משקולות זרימה אופטית באופן אוטומטי; עליך למקם את קובץ ה-checkpoint באופן ידני בתיקיית `models/optical_flow/`.

## קלטים

| פרמטר | תיאור | סוג נתונים | חובה | טווח |
| --- | --- | --- | --- | --- |
| `model_name` | מודל זרימה אופטית (optical flow) לטעינה. יש למקם קבצים בתיקיית `optical_flow`. נכון להיום נתמך רק `raft_large.pth` של torchvision. | COMBO | כן | רשימת קבצים בתיקיית `models/optical_flow/` |

הערה: ה-checkpoint הנבחר חייב להיות state dict של torchvision RAFT-large המכיל מפתחות עם הקידומת `feature_encoder.`, `context_encoder.`, ו-`update_block.`. אם הקובץ אינו תואם לפורמט זה, הצומת מעלה ValueError.

## פלטים

| שם פלט | תיאור | סוג נתונים |
| --- | --- | --- |
| `OPTICAL_FLOW` | מודל הזרימה האופטית שנטען, מוגדר למצב הערכה (evaluation mode), עם דיוק fp16 בהתקנים שתומכים בכך (אחרת float32), ועטוף ב-ModelPatcher לשימוש עם צמתים אחרים. | OPTICAL_FLOW |

> מסמך זה נוצר על ידי בינה מלאכותית. אם מצאתם שגיאות או שיש לכם הצעות לשיפור, אתם מוזמנים לתרום! [עריכה ב-GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpticalFlowLoader/he.md)

---
**Source fingerprint (SHA-256):** `82e5d747679ede113ec4d72fd6eda4b8f20d098832612bebf26ef65de8b4b3dc`
