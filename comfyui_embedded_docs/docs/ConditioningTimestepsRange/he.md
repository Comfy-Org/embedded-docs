# טווח Timesteps

הצומת ConditioningTimestepsRange יוצר שלושה טווחי צעדי זמן נפרדים לשליטה מתי אפקטי התניה מופעלים במהלך תהליך היצירה. הוא מקבל ערכי אחוז התחלה וסיום ומחלק את כל טווח צעדי הזמן (0.0 עד 1.0) לשלושה מקטעים: הטווח הראשי בין האחוזים שצוינו, הטווח שלפני אחוז ההתחלה, והטווח שאחרי אחוז הסיום.

## קלטים

| פרמטר | תיאור | סוג נתונים | חובה | טווח |
| --- | --- | --- | --- | --- |
| `start_percent` | אחוז ההתחלה של טווח צעדי הזמן (ברירת מחדל: 0.0) | FLOAT | כן | 0.0 - 1.0 |
| `end_percent` | אחוז הסיום של טווח צעדי הזמן (ברירת מחדל: 1.0) | FLOAT | כן | 0.0 - 1.0 |

## פלטים

| שם פלט | תיאור | סוג נתונים |
| --- | --- | --- |
| `TIMESTEPS_RANGE` | טווח צעדי הזמן הראשי המוגדר על ידי start_percent ו-end_percent | TIMESTEPS_RANGE |
| `BEFORE_RANGE` | טווח צעדי הזמן מ-0.0 עד start_percent | TIMESTEPS_RANGE |
| `AFTER_RANGE` | טווח צעדי הזמן מ-end_percent עד 1.0 | TIMESTEPS_RANGE |

> מסמך זה נוצר על ידי בינה מלאכותית. אם מצאתם שגיאות או שיש לכם הצעות לשיפור, אתם מוזמנים לתרום! [עריכה ב-GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningTimestepsRange/he.md)

---
**Source fingerprint (SHA-256):** `dee21b5ac80fabdeacf3f4a985550fff795702e02911400ae49a97baae834e5e`
