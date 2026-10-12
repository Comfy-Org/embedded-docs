# EpsilonScaling

מיישם את שיטת Epsilon Scaling ממאמר המחקר "Elucidating the Exposure Bias in Diffusion Models". שיטה זו משפרת את איכות הדגימות על ידי סקיילינג של הרעש החזוי במהלך תהליך הדגימה. היא משתמשת בלוח זמנים אחיד כדי למתן את הטיית החשיפה במודלים של דיפוזיה.

## קלטים

| פרמטר | תיאור | סוג נתונים | נדרש | טווח |
| --- | --- | --- | --- | --- |
| `model` | המודל שעליו להחיל Epsilon Scaling | MODEL | כן | - |
| `scaling_factor` | הגורם המשמש לסקיילינג של הרעש החזוי (ברירת מחדל: 1.005) | FLOAT | לא | 0.5 - 1.5 |

## פלטים

| שם פלט | תיאור | סוג נתונים |
| --- | --- | --- |
| `model` | המודל שעליו הוחל Epsilon Scaling | MODEL |

> מסמך זה נוצר על ידי בינה מלאכותית. אם מצאתם שגיאות או שיש לכם הצעות לשיפור, אתם מוזמנים לתרום! [עריכה ב-GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EpsilonScaling/he.md)
