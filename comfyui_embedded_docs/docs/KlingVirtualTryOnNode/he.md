# KlingVirtualTryOnNode

צומת Kling Virtual Try On. הזן תמונת אדם ותמונת בגד כדי להלביש את הבגד על האדם. ניתן למזג מספר תמונות של פריטי לבוש לתמונה אחת עם רקע לבן.

## קלטים

| פרמטר | תיאור | סוג נתונים | חובה | טווח |
|-----------|-------------|-----------|----------|-------|
| `human_image` | תמונת האדם שעליה ינסו את הבגדים | IMAGE | כן | - |
| `cloth_image` | תמונת הבגד שינסו על האדם | IMAGE | כן | - |
| `model_name` | מודל ההלבשה הווירטואלית לשימוש (ברירת מחדל: `"kolors-virtual-try-on-v1"`) | STRING | כן | `"kolors-virtual-try-on-v1"` |

## פלטים

| שם פלט | תיאור | סוג נתונים |
|-------------|-------------|-----------|
| `output` | התמונה המתקבלת המציגה את האדם עם פריט הלבוש לאחר ההלבשה | IMAGE |

> מסמך זה נוצר על ידי בינה מלאכותית. אם מצאתם שגיאות או שיש לכם הצעות לשיפור, אתם מוזמנים לתרום! [עריכה ב-GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingVirtualTryOnNode/he.md)

---
**Source fingerprint (SHA-256):** `bf256d8732f4c6acf65838812fc322e48ef886257bbb48c02b0cc6ab5d78dce5`
