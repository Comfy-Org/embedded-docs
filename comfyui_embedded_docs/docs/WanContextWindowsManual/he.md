# Wan Context Windows

הצומת WAN Context Windows (Manual) מאפשר לך להגדיר ידנית חלונות הקשר (context windows) עבור מודלים מסוג Wan לווידאו. הוא מחיל את ההגדרות הללו במהלך הדגימה (sampling), ומעניק לך שליטה על אורך החלון, החפיפה, התזמון ושיטת המיזוג המשמשת בזמן שהמודל מעבד וידאו. אורך ההקשר והחפיפה מוגדרים בפריימים אמיתיים ומומרים פנימית לעיבוד הדו-ממדי של המודל.

## קלטים

| פרמטר | תיאור | סוג נתון | חובה | טווח |
| --- | --- | --- | --- | --- |
| `model` | המודל שעליו להחיל חלונות הקשר במהלך הדגימה. | MODEL | כן | - |
| `context_length` | אורך חלון ההקשר בפריימים אמיתיים. חייב להיות 4*n + 1 (ברירת מחדל: 81). | INT | כן | 1 עד 16384 (MAX_RESOLUTION), צעד 4 |
| `context_overlap` | החפיפה של חלון ההקשר בפריימים אמיתיים (ברירת מחדל: 30). | INT | כן | 0 ומעלה |
| `context_schedule` | אלגוריתם תזמון תלוי-צעד עבור חלונות הקשר (ברירת מחדל: "uniform_standard"). | COMBO | כן | `"static_standard"`<br>`"uniform_standard"`<br>`"uniform_looped"`<br>`"batched"` |
| `context_stride` | הצעד (stride) של חלון ההקשר; רלוונטי רק ללוחות זמנים uniform (ברירת מחדל: 1). | INT | כן | 1 ומעלה |
| `closed_loop` | האם לסגור את לולאת חלון ההקשר; רלוונטי רק ללוחות זמנים looped (ברירת מחדל: False). | BOOLEAN | כן | - |
| `fuse_method` | השיטה שבה יש להשתמש כדי למזג את חלונות ההקשר (ברירת מחדל: "pyramid"). | COMBO | כן | `"pyramid"`<br>`"gaussian"`<br>`"average"`<br>`"overlap"` |
| `freenoise` | האם להחיל ערבוב רעש FreeNoise, משפר את מיזוג החלונות (ברירת מחדל: True). | BOOLEAN | כן | - |
| `retain_first_frame` | לשמור את פריים ה-I2V הראשון בכל חלון הקשר (עשוי לעזור לשמר את הייחוס הראשוני) (ברירת מחדל: False). | BOOLEAN | כן | - |
| `split_conds_to_windows` | האם לפצל מספר תנאי conditioning (שנוצרו על ידי ConditionCombine) לכל חלון בהתבסס על אינדקס אזור (ברירת מחדל: False). | BOOLEAN | כן | - |

**הערה:** `context_stride` משפיע רק על לוחות זמנים uniform, ו-`closed_loop` חל רק על לוחות זמנים looped. אורך ההקשר והחפיפה מוגדרים בפריימים אמיתיים ומומרים אוטומטית ומוגבלים (clamped) לערכי מינימום חוקיים במהלך העיבוד (`context_length` הופך ל-((length - 1) / 4) + 1, `context_overlap` הופך ל-overlap / 4). `context_length` חייב להיות בצורה 4*n + 1. `retain_first_frame` מיועד לשימוש במצב תמונה-לווידאו. `split_conds_to_windows` מצפה למספר תנאי conditioning שנוצרו על ידי הצומת ConditionCombine. הפרמטר `fuse_method` כולל מספר אפשרויות מעבר ל-"pyramid" בלבד.

## פלטים

| שם פלט | תיאור | סוג נתון |
| --- | --- | --- |
| `model` | המודל עם תצורת חלונות ההקשר שהוחלה. | MODEL |

> מסמך זה נוצר על ידי בינה מלאכותית. אם מצאתם שגיאות או שיש לכם הצעות לשיפור, אתם מוזמנים לתרום! [עריכה ב-GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanContextWindowsManual/he.md)

---
**Source fingerprint (SHA-256):** `cf4927371e9d4b509f2e6e5319cd6109e3ef36da6b3faee278bcf8c906672857`
