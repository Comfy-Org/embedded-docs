# LTXVContextWindows

צומת זה מגדיר חלונות הקשר עבור מודלים בסגנון LTXV במהלך הדגימה. הוא מחלק את היצירה לחלונות חופפים כדי לסייע בניהול השימוש בזיכרון ולשפר קוהרנטיות זמנית.

## קלטים

| פרמטר | תיאור | סוג נתונים | חובה | טווח |
|-----------|-------------|-----------|----------|-------|
| `model` | המודל שעליו להחיל חלונות הקשר במהלך הדגימה. | MODEL | כן | - |
| `context_length` | אורך חלון ההקשר בפריימים אמיתיים. חייב להיות 8*n + 1. (ברירת מחדל: 145) | INT | כן | מינימום: 1<br>מקסימום: nodes.MAX_RESOLUTION<br>צעד: 8 |
| `context_overlap` | חפיפת חלון ההקשר בפריימים אמיתיים. (ברירת מחדל: 40) | INT | כן | מינימום: 0<br>צעד: 8 |
| `context_schedule` | אלגוריתם תזמון תלוי-צעד עבור חלונות הקשר. (ברירת מחדל: "UNIFORM_STANDARD") | COMBO | כן | `"STATIC_STANDARD"`<br>`"UNIFORM_STANDARD"`<br>`"UNIFORM_LOOPED"`<br>`"BATCHED"` |
| `context_stride` | הצעד של חלון ההקשר; רלוונטי רק לתזמונים אחידים. (ברירת מחדל: 1) | INT | כן | מינימום: 1 |
| `closed_loop` | האם לסגור את לולאת חלון ההקשר; רלוונטי רק לתזמונים מבוססי לולאה. (ברירת מחדל: False) | BOOLEAN | כן | True<br>False |
| `fuse_method` | השיטה למיזוג חלונות ההקשר. האפשרויות הזמינות מוגדרות על ידי `ContextFuseMethods.LIST_STATIC`. (ברירת מחדל: "PYRAMID") | COMBO | כן | מוגדר על ידי `ContextFuseMethods.LIST_STATIC` |
| `freenoise` | האם להחיל ערבול רעש FreeNoise, משפר את שילוב החלונות. (ברירת מחדל: True) | BOOLEAN | כן | True<br>False |
| `retain_first_frame` | לשמר את פריים ה-latent הראשון בכל חלון הקשר (עשוי לעזור לשמר רפרנס ראשוני). (ברירת מחדל: False) | BOOLEAN | כן | True<br>False |
| `split_conds_to_windows` | האם לפצל מספר קונדישנינגים (שנוצרו על ידי ConditionCombine) לכל חלון בהתבסס על אינדקס אזור. (ברירת מחדל: False) | BOOLEAN | כן | True<br>False |

**הערה:** הערך של `context_length` מסופק בפריימים אמיתיים ומומר פנימית לפריימי latent באמצעות הנוסחה `((context_length - 1) // 8) + 1`, עם מינימום של 1. הערך של `context_overlap` מסופק גם הוא בפריימים אמיתיים ומומר לפריימי latent באמצעות חילוק שלם ב-8, עם מינימום של 0. הטולטיפ של `context_length` מציין שהוא חייב להתאים לתבנית 8*n + 1.

## פלטים

| שם פלט | תיאור | סוג נתונים |
|-------------|-------------|-----------|
| `MODEL` | המודל עם חלונות הקשר שהוחלו עליו לצורך דגימה. | MODEL |

> מסמך זה נוצר על ידי בינה מלאכותית. אם מצאתם שגיאות או שיש לכם הצעות לשיפור, אתם מוזמנים לתרום! [עריכה ב-GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVContextWindows/he.md)

---
**Source fingerprint (SHA-256):** `148649d0a938e08c932a163f5d7614332626fba37b8f79db7f92bbcf422e692f`
