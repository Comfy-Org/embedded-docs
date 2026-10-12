# TripoPSeriesMultiviewToModelNode

יוצר מודל תלת-ממדי low-poly עם טופולוגיה נקייה ממספר מבטים של אותו נושא באמצעות מודל P2 של Tripo. מבט חזיתי נדרש, וניתן להוסיף בין מבט אחד לשלושה מבין מבטי שמאל, אחור וימין כדי לשפר את התוצאה. המודל מוחזר כרשת משולשים (GLB) או, כאשר `model.quad` מופעל, כרשת עם רוב של מרובעים (FBX).

## קלטים

### קלטים משותפים

| פרמטר | תיאור | סוג נתונים | נדרש | טווח |
| --- | --- | --- | --- | --- |
| `model` | מודל Tripo מסדרת P לשימוש. בחירת מודל חושפת את הקלטים הייחודיים לו למטה. | DYNAMIC_COMBO | כן | `"P2"` |

### קלטים של P2

| פרמטר | תיאור | סוג נתונים | נדרש | טווח |
| --- | --- | --- | --- | --- |
| `model.image` | מבט חזית (0°) של הנושא. | IMAGE | כן | - |
| `model.image_left` | מבט שמאל (90°), הצד השמאלי של הנושא עצמו. | IMAGE | לא | - |
| `model.image_back` | מבט אחור (180°). | IMAGE | לא | - |
| `model.image_right` | מבט ימין (270°), הצד הימני של הנושא עצמו. | IMAGE | לא | - |
| `model.quad` | מחזיר רשת עם רוב של מרובעים בפלט FBX במקום רשת משולשים בפלט GLB (ברירת מחדל: False). | BOOLEAN | כן | True/False |
| `model.face_limit` | מספר פאות יעד. `-1` נותן ל-Tripo לבחור. כאשר `model.quad` מופעל, המגבלה היא 48 עד 25,000, אחרת 48 עד 50,000 (ברירת מחדל: -1). | INT | כן | -1, or 48 to 50000 |
| `model.texture` | רזולוציית טקסטורת צבע בסיס: standard היא 2K, detailed היא 4K ו-extreme היא 8K. `"none"` מחזיר רשת ללא טקסטורה (ברירת מחדל: `"standard"`). | COMBO | כן | `"standard"`<br>`"detailed"`<br>`"extreme"`<br>`"none"` |
| `model.pbr` | מוסיף מפות מתכתיות, חספוס ונורמל לצבע הבסיס. מתעלמים ממנו כאשר `model.texture` הוא `"none"` (ברירת מחדל: True). | BOOLEAN | כן | True/False |
| `model.model_seed` | זרע (seed) לגיאומטריה (ברירת מחדל: 42). | INT | כן | 0 to 2147483647 |
| `model.texture_alignment` | התאמת צבעי תמונות הקלט, או התאמת הטקסטורות לגיאומטריה שנוצרה. מתעלמים ממנו כאשר `model.texture` הוא `"none"` (ברירת מחדל: `"original_image"`). הגדרה מתקדמת. | COMBO | כן | `"original_image"`<br>`"geometry"` |
| `model.orientation` | `"align_image"` מסובב את המודל לנקודת המבט של תמונות הקלט. מתעלמים ממנו כאשר `model.texture` הוא `"none"` (ברירת מחדל: `"default"`). הגדרה מתקדמת. | COMBO | כן | `"default"`<br>`"align_image"` |
| `model.texture_seed` | זרע (seed) לטקסטורות (ברירת מחדל: 42). הגדרה מתקדמת. | INT | כן | 0 to 2147483647 |
| `model.auto_size` | מבצע סקיילינג למודל לגודלו במציאות במטרים דרך טרנספורמציית הסצנה שלו. מתעלמים ממנו כאשר `model.texture` הוא `"none"` (ברירת מחדל: False). הגדרה מתקדמת. | BOOLEAN | כן | True/False |
| `model.export_uv` | פריסת UV לרשת כשהיא ללא טקסטורה. רשתות עם טקסטורה תמיד נפרסות (ברירת מחדל: True). הגדרה מתקדמת. | BOOLEAN | כן | True/False |
| `model.compress_geometry` | הפעלת דחיסת גיאומטריה meshopt: קבצים קטנים בהרבה, אך תצוגת התלת-ממד של ComfyUI אינה יכולה להציג אותם. אינו חל על רשתות מרובעים (ברירת מחדל: False). הגדרה מתקדמת. | BOOLEAN | כן | True/False |

**הערות:**

- `model.image` הוא חובה, ולפחות אחד מבין `model.image_left`, `model.image_back` או `model.image_right` חייב להיות מחובר גם כן; הצומת מעלה שגיאה אם מבט החזית הוא התמונה היחידה.
- רק התמונה הראשונה מכל אצווה (batch) משמשת.
- `model.face_limit` הוא יעד ולא תקרה קשיחה, כך שהתוצאה יכולה להכיל יותר פאות מהמבוקש. `-1` משאיר את הבחירה ל-Tripo.
- `model.quad` קובע איזה פלט נושא את הרשת. כאשר הוא מופעל, המודל מגיע בפלט FBX ופלט GLB נשאר ריק; כאשר הוא מושבת, המודל מגיע ב-GLB ו-FBX נשאר ריק. הצומת מעלה שגיאה אם הפלט הריק הוא זה שחיברת.
- `model.texture`, `model.pbr`, `model.texture_seed`, `model.auto_size`, `model.texture_alignment` ו-`model.orientation` חלים רק על מודלים עם טקסטורה: כאשר `"none"`, הצומת אינו שולח הגדרות טקסטורה ומחזיר גיאומטריה חשופה.
- `model.compress_geometry` אינו משפיע על רשתות מרובעים.

## פלטים

| שם פלט | תיאור | סוג נתונים |
| --- | --- | --- |
| `model task_id` | מזהה המשימה הייחודי של בקשת יצירת המודל. | MODEL_TASK_ID |
| `GLB` | המודל התלת-ממדי שנוצר בפורמט GLB. ריק כאשר `model.quad` מופעל. | FILE3DGLB |
| `FBX` | המודל התלת-ממדי שנוצר בפורמט FBX. מאוכלס רק כאשר `model.quad` מופעל. | FILE3DFBX |

> מסמך זה נוצר על ידי בינה מלאכותית. אם מצאתם שגיאות או שיש לכם הצעות לשיפור, אתם מוזמנים לתרום! [עריכה ב-GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoPSeriesMultiviewToModelNode/he.md)

---
**Source fingerprint (SHA-256):** `cea0a65ca001bc8298af9fbe2a83f592abf497987e634b0126482f3d2a18571c`
