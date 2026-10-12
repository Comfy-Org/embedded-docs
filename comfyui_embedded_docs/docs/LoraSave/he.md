# חילוץ ושמירת LoRA

הצומת LoraSave מחלץ ושומר קבצי LoRA (Low-Rank Adaptation) מתוך הבדלים בין מודלים. הוא יכול לעבד הבדלים במודל דיפוזיה, הבדלים במקודד טקסט, או את שניהם, ולהמיר אותם לפורמט LoRA עם דרגה וסוג מוגדרים. קובץ ה-LoRA שנוצר נשמר בספריית הפלט לשימוש מאוחר יותר.

## קלטים

| פרמטר | תיאור | סוג נתונים | חובה | טווח |
| --- | --- | --- | --- | --- |
| `filename_prefix` | הקידומת עבור שם קובץ הפלט (ברירת מחדל: "loras/ComfyUI_extracted_lora") | STRING | כן | - |
| `rank` | ערך הדרגה עבור ה-LoRA, השולט בגודל ובמורכבות (ברירת מחדל: 8) | INT | כן | 1-4096 |
| `lora_type` | סוג ה-LoRA ליצירה. "standard" מחלץ מטריצות בדרגה נמוכה באמצעות SVD; "full_diff" שומר את הפרש המשקלים המלא (ברירת מחדל: "standard") | COMBO | כן | `"standard"`<br>`"full_diff"` |
| `bias_diff` | האם לכלול הבדלי הטיה בחישוב ה-LoRA (ברירת מחדל: True) | BOOLEAN | כן | - |
| `model_diff` | הפלט של ModelSubtract שיומר ל-LoRA | MODEL | לא | - |
| `text_encoder_diff` | הפלט של CLIPSubtract שיומר ל-LoRA | CLIP | לא | - |

**הערה:** יש לספק לפחות אחד מהפרמטרים `model_diff` או `text_encoder_diff` כדי שהצומת תפעל. אם שניהם מושמטים, הצומת לא תפיק פלט.

## פלטים

| שם פלט | תיאור | סוג נתונים |
| --- | --- | --- |
| - | צומת זה שומר קובץ LoRA בספריית הפלט אך אינו מחזיר נתונים דרך זרימת העבודה | - |

> מסמך זה נוצר על ידי בינה מלאכותית. אם מצאתם שגיאות או שיש לכם הצעות לשיפור, אתם מוזמנים לתרום! [עריכה ב-GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoraSave/he.md)

---
**Source fingerprint (SHA-256):** `642510bfe083130cb2724d7ae38d30d4694c85a43c7ce27230690ddd9fe76b79`
