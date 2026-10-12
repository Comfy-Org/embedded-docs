# ConditioningSetProperties

## קלטים

| פרמטר | תיאור | סוג נתונים | סוג קלט | ברירת מחדל | טווח |
| --- | --- | --- | --- | --- | --- |
| `cond_NEW` | נתוני ההתניה שיש לשנות | CONDITIONING | חובה | - | - |
| `strength` | שולט בעוצמת אפקט ההתניה | FLOAT | חובה | 1.0 | 0.0 - 10.0 (step: 0.01) |
| `set_cond_area` | קובע כיצד חל אזור ההתניה. בחר "default" עבור התנהגות סטנדרטית או "mask bounds" כדי להגביל לאזור המסכה | STRING | חובה | default | ["default", "mask bounds"] |
| `mask` | מסכה אופציונלית להגבלת המקום שבו מוחלת ההתניה | MASK | אופציונלי | - | - |
| `hooks` | פונקציות hook אופציונליות לעיבוד מותאם אישית | HOOKS | אופציונלי | - | - |
| `timesteps` | טווח timesteps אופציונלי להגבלת מתי ההתניה פעילה | TIMESTEPS_RANGE | אופציונלי | - | - |

**הערה:** כאשר מסופקת `mask`, ניתן להגדיר את הפרמטר `set_cond_area` ל-"mask bounds" כדי להגביל את החלת ההתניה לאזור המסכה בלבד. הפרמטר `hooks` מאפשר עיבוד מותאם אישית באמצעות פונקציות hook, ו-`timesteps` מגביל את אפקט ההתניה לטווח ספציפי של timesteps במהלך היצירה.

## פלטים

| שם פלט | תיאור | סוג נתונים |
| --- | --- | --- |
| `CONDITIONING` | נתוני ההתניה ששונו עם מאפיינים מעודכנים | CONDITIONING |

> מסמך זה נוצר על ידי בינה מלאכותית. אם מצאתם שגיאות או שיש לכם הצעות לשיפור, אתם מוזמנים לתרום! [עריכה ב-GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSetProperties/he.md)

---
**Source fingerprint (SHA-256):** `5e3f5348f6df8f2fa1c1d42b883efcab3ee07d933e219f11fa48730aacc168d7`
