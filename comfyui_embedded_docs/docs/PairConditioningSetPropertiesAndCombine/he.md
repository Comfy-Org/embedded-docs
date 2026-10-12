# Cond Pair Set Props Combine

הצומת PairConditioningSetPropertiesAndCombine משנה ומאחד זוגות קונדישנינג על ידי החלת נתוני קונדישנינג חדשים על קלטי הקונדישנינג החיובי והשלילי הקיימים. הוא מאפשר לך להתאים את עוצמת הקונדישנינג המוחל ולשלוט באופן שבו אזור הקונדישנינג מוגדר. צומת זה שימושי במיוחד בתהליכי עבודה מתקדמים של מניפולציה על קונדישנינג, שבהם יש לך צורך למזג יחד מספר מקורות קונדישנינג.

## קלטים

| פרמטר | תיאור | סוג נתונים | חובה | טווח |
| --- | --- | --- | --- | --- |
| `positive` | קלט הקונדישנינג החיובי המקורי | CONDITIONING | כן | - |
| `negative` | קלט הקונדישנינג השלילי המקורי | CONDITIONING | כן | - |
| `positive_NEW` | קלט הקונדישנינג החיובי החדש להחלה | CONDITIONING | כן | - |
| `negative_NEW` | קלט הקונדישנינג השלילי החדש להחלה | CONDITIONING | כן | - |
| `strength` | מקדם העוצמה להחלת הקונדישנינג החדש (ברירת מחדל: 1.0) | FLOAT | כן | 0.0 to 10.0 |
| `set_cond_area` | שולט באופן שבו מוחל אזור הקונדישנינג (ברירת מחדל: "default") | STRING | כן | "default"<br>"mask bounds" |
| `mask` | מסכה אופציונלית להגבלת אזור החלת הקונדישנינג | MASK | לא | - |
| `hooks` | קבוצת hooks אופציונלית לשליטה מתקדמת | HOOKS | לא | - |
| `timesteps` | מפרט טווח timesteps אופציונלי | TIMESTEPS_RANGE | לא | - |

## פלטים

| שם פלט | תיאור | סוג נתונים |
| --- | --- | --- |
| `positive` | פלט הקונדישנינג החיובי המשולב | CONDITIONING |
| `negative` | פלט הקונדישנינג השלילי המשולב | CONDITIONING |

> מסמך זה נוצר על ידי בינה מלאכותית. אם מצאתם שגיאות או שיש לכם הצעות לשיפור, אתם מוזמנים לתרום! [עריכה ב-GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PairConditioningSetPropertiesAndCombine/he.md)

---
**Source fingerprint (SHA-256):** `d434fdc1ccbe3ddee6293a6300cc55d30cb5bf357025b26777791746f51e755e`
