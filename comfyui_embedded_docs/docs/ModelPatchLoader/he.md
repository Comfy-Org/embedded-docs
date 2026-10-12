# טעינת תיקון מודל

צומת ModelPatchLoader טוען קובץ תיקון מודל מתיקיית `model_patches` ומכין אותו לשימוש בזרימת עבודה. הוא מזהה אוטומטית את סוג התיקון contained בקובץ, בונה את הארכיטקטורה המתאימה, טוען את המשקולות השמורות, ועוטף הכול ב-model patcher כך שניתן יהיה להחיל אותו על מודלים אחרים. הוא תומך בפורמטי תיקון מיוחדים רבים, כולל ענפי ControlNet נוספים, מודלי embedding של תכונות, מתאמים, מודולי הנחיה של אנימציה/LLLite ומודולים דומים.

## קלטים

| פרמטר | תיאור | סוג נתונים | חובה | טווח |
| --- | --- | --- | --- | --- |
| `name` | שם הקובץ של תיקון המודל לטעינה מתיקיית `model_patches`. יש לבחור אחד מקובצי התיקון הזמינים מהרשימה. | COMBO | כן | רשימה דינמית של כל קובצי תיקון המודל שנמצאו בתיקיית `model_patches` |

הערה: צומת זה מסומן כניסיוני. סוג התיקון מזוהה אוטומטית מתוכן הקובץ, כך שאין צורך בבחירה ידנית של סוג. הצומת קורא מטא-נתוני checkpoint ובוחן מפתחות משקולות כדי להחליט איזו ארכיטקטורה לבנות (לדוגמה Qwen Image block-wise ControlNet, Qwen Image 2.1 Fun ControlNet, Z-Image ControlNet, Wan Uni3C ControlNet, MiniMax H3 Fun ControlNet, SigLIP feature projection, Lightricks duration head, Anima LLLite, MultiTalk או SUPIR). המשקולות נטענות עם טעינה בטוחה מופעלת, והמודל ממוקם על התקן offload בתוך `CoreModelPatcher` כך שאפשר יהיה להחיל אותו מאוחר יותר על מודל אחר.

## פלטים

| שם פלט | תיאור | סוג נתונים |
| --- | --- | --- |
| `MODEL_PATCH` | תיקון המודל הטעון, עטוף ב-model patcher, מוכן להחלה על מודל בזרימת העבודה | MODEL_PATCH |

> מסמך זה נוצר על ידי בינה מלאכותית. אם מצאתם שגיאות או שיש לכם הצעות לשיפור, אתם מוזמנים לתרום! [עריכה ב-GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelPatchLoader/he.md)

---
**Source fingerprint (SHA-256):** `83b607f3c2b4b210e6ca3d310ef974757a6caf3c83f1d2d5165f3b8248928e9c`
