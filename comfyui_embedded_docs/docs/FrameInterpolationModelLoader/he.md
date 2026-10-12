# FrameInterpolationModelLoader

צומת זה טוען קובץ מודל אינטרפולציית פריימים ומכין אותו לשימוש בתהליך העבודה. הוא מזהה אוטומטית אם הקובץ הוא מודל FILM או RIFE ומגדיר את המודל בהתאם לחומרה הזמינה.

## קלטים

| פרמטר | תיאור | סוג נתונים | חובה | טווח |
| --- | --- | --- | --- | --- |
| `model_name` | בחר מודל אינטרפולציית פריימים לטעינה. יש למקם מודלים בתיקיית 'frame_interpolation'. | COMBO | כן | רשימת קבצי מודל בתיקיית `frame_interpolation` |

הערה: הצומת תומך בפורמטים של מודל FILM ו-RIFE. אם הקובץ הנבחר אינו בפורמט מוכר, תיווצר שגיאה.

## פלטים

| שם פלט | תיאור | סוג נתונים |
| --- | --- | --- |
| `FRAME_INTERPOLATION_MODEL` | מודל אינטרפולציית הפריימים שנטען והוגדר, מוכן לשימוש בצמתים אחרים. | INTERP_MODEL |

> מסמך זה נוצר על ידי בינה מלאכותית. אם מצאתם שגיאות או שיש לכם הצעות לשיפור, אתם מוזמנים לתרום! [עריכה ב-GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FrameInterpolationModelLoader/he.md)

---
**Source fingerprint (SHA-256):** `21f470ee2852dbd1b332ac4a506eaa20dc8578c04b63c4fe1a072878b57beaba`
