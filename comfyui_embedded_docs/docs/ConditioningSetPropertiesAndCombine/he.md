# ConditioningSetPropertiesAndCombine

הצומת ConditioningSetPropertiesAndCombine משנה נתוני התניה על ידי החלת מאפיינים מקלט התניה חדש על קלט התניה קיים. הוא משלב את שתי קבוצות ההתניה תוך שליטה בעוצמת ההתניה החדשה וקביעה כיצד יש להחיל את אזור ההתניה.

## קלטים

| פרמטר | תיאור | סוג נתונים | סוג קלט | ברירת מחדל | טווח |
| --- | --- | --- | --- | --- | --- |
| `cond` | נתוני ההתניה המקוריים שיש לשנות | CONDITIONING | חובה | - | - |
| `cond_NEW` | נתוני ההתניה החדשים המספקים מאפיינים להחלה | CONDITIONING | חובה | - | - |
| `strength` | שולט בעוצמת מאפייני ההתניה החדשים | FLOAT | חובה | 1.0 | 0.0 - 10.0 |
| `set_cond_area` | קובע כיצד מיושם אזור ההתניה | STRING | חובה | default | ["default", "mask bounds"] |
| `mask` | מסכה אופציונלית להגדרת אזורים ספציפיים להתניה | MASK | אופציונלי | - | - |
| `hooks` | פונקציות hook אופציונליות לעיבוד מותאם אישית | HOOKS | אופציונלי | - | - |
| `timesteps` | טווח צעדי זמן אופציונלי לשליטה מתי מוחלת ההתניה | TIMESTEPS_RANGE | אופציונלי | - | - |

**הערה:** כאשר מסופקת `mask`, הפרמטר `set_cond_area` יכול להשתמש ב-"mask bounds" כדי להגביל את החלת ההתניה לאזורים המכוסים במסכה.

## פלטים

| שם פלט | תיאור | סוג נתונים |
| --- | --- | --- |
| `CONDITIONING` | נתוני ההתניה המשולבים עם מאפיינים ששונו | CONDITIONING |

> מסמך זה נוצר על ידי בינה מלאכותית. אם מצאתם שגיאות או שיש לכם הצעות לשיפור, אתם מוזמנים לתרום! [עריכה ב-GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSetPropertiesAndCombine/he.md)

---
**Source fingerprint (SHA-256):** `da57eeae428a103cbad77af063419ed0e85aeaa0b8805c8c197df27613477fa8`
