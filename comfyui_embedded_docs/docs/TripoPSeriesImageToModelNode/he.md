# Tripo P2: מתמונה למודל

יוצר מודל תלת-ממדי low-poly עם טופולוגיה נקייה מתמונה בודדת באמצעות המודל P2 של Tripo. התוצאה מוחזרת כרשת משולשים (GLB) או, כאשר `model.quad` מופעל, כרשת דומיננטית של מרובעים (FBX).

## קלטים

### קלטים משותפים

| פרמטר | תיאור | סוג נתונים | חובה | טווח |
| --- | --- | --- | --- | --- |
| `model` | מודל Tripo מסדרת P לשימוש. בחירת מודל חושפת את הקלטים שלו למטה. | DYNAMIC_COMBO | כן | `"P2"` |

### קלטים של P2

| פרמטר | תיאור | סוג נתונים | חובה | טווח |
| --- | --- | --- | --- | --- |
| `model.image` | התמונה שממנה נוצר המודל. | IMAGE | כן | - |
| `model.quad` | החזר רשת דומיננטית של מרובעים בפלט FBX במקום רשת משולשים בפלט GLB (ברירת מחדל: False). | BOOLEAN | כן | True/False |
| `model.face_limit` | מספר הפאות המבוקש. `-1` נותן ל-Tripo לבחור. כאשר `model.quad` מופעל המגבלה היא 48 עד 25,000, אחרת 48 עד 50,000 (ברירת מחדל: -1). | INT | כן | -1, or 48 to 50000 |
| `model.texture` | רזולוציית טקסטורת צבע בסיס: standard היא 2K, detailed היא 4K ו-extreme היא 8K. `"none"` מחזיר רשת ללא טקסטורה (ברירת מחדל: `"standard"`). | COMBO | כן | `"standard"`<br>`"detailed"`<br>`"extreme"`<br>`"none"` |
| `model.pbr` | הוסף מפות מתכתיות, חספוס ונורמל לצבע הבסיס. לא חל כאשר `model.texture` הוא `"none"` (ברירת מחדל: True). | BOOLEAN | כן | True/False |
| `model.model_seed` | Seed עבור הגאומטריה (ברירת מחדל: 42). | INT | כן | 0 to 2147483647 |
| `model.texture_alignment` | התאם את הצבעים של תמונת הקלט, או התאם את הטקסטורות לגאומטריה שנוצרה. לא חל כאשר `model.texture` הוא `"none"` (ברירת מחדל: `"original_image"`). הגדרה מתקדמת. | COMBO | כן | `"original_image"`<br>`"geometry"` |
| `model.orientation` | `"align_image"` מסובב את המודל לנקודת המבט של תמונת הקלט. לא חל כאשר `model.texture` הוא `"none"` (ברירת מחדל: `"default"`). הגדרה מתקדמת. | COMBO | כן | `"default"`<br>`"align_image"` |
| `model.enable_image_autofix` | אפשר ל-Tripo לשפר תמונה ברזולוציה נמוכה או באיכות ירודה לפני המידול (ברירת מחדל: False). הגדרה מתקדמת. | BOOLEAN | כן | True/False |
| `model.texture_seed` | Seed עבור הטקסטורות (ברירת מחדל: 42). הגדרה מתקדמת. | INT | כן | 0 to 2147483647 |
| `model.auto_size` | כוונן את קנה המידה של המודל לגודלו בעולם האמיתי במטרים דרך טרנספורם הסצנה שלו. לא חל כאשר `model.texture` הוא `"none"` (ברירת מחדל: False). הגדרה מתקדמת. | BOOLEAN | כן | True/False |
| `model.export_uv` | בצע UV unwrap לרשת כשהיא ללא טקסטורה. רשתות עם טקסטורה תמיד עוברות unwrap (ברירת מחדל: True). הגדרה מתקדמת. | BOOLEAN | כן | True/False |
| `model.compress_geometry` | החל דחיסת גאומטריה meshopt: קבצים קטנים בהרבה, אך תצוגת התלת-ממד של ComfyUI לא יכולה להציג אותם. לא חל על רשתות מרובעים (ברירת מחדל: False). הגדרה מתקדמת. | BOOLEAN | כן | True/False |

**הערות:**

- `model.image` הוא חובה ורק התמונה הראשונה באצווה משמשת.
- `model.face_limit` הוא יעד ולא תקרה קשיחה, כך שהתוצאה יכולה להכיל יותר פאות מהמבוקש. `-1` משאיר את הבחירה ל-Tripo.
- `model.quad` קובע איזה פלט נושא את הרשת. כאשר הוא מופעל, המודל מגיע בפלט FBX ופלט GLB נשאר ריק; כאשר הוא מושבת, המודל מגיע ב-GLB ו-FBX נשאר ריק. הצומת מעלה שגיאה אם הפלט הריק הוא זה שחיברת.
- `model.texture`, `model.pbr`, `model.texture_seed`, `model.auto_size`, `model.texture_alignment` ו-`model.orientation` חלים רק על מודלים עם טקסטורה: עם `"none"` הצומת לא שולח הגדרות טקסטורה ומחזיר גאומטריה חשופה.
- `model.compress_geometry` אינו משפיע על רשתות מרובעים.

## פלטים

| שם פלט | תיאור | סוג נתונים |
| --- | --- | --- |
| `model task_id` | מזהה המשימה הייחודי עבור בקשת יצירת המודל. | MODEL_TASK_ID |
| `GLB` | המודל התלת-ממדי שנוצר בפורמט GLB. ריק כאשר `model.quad` מופעל. | FILE3DGLB |
| `FBX` | המודל התלת-ממדי שנוצר בפורמט FBX. מאוכלס רק כאשר `model.quad` מופעל. | FILE3DFBX |

> מסמך זה נוצר על ידי בינה מלאכותית. אם מצאתם שגיאות או שיש לכם הצעות לשיפור, אתם מוזמנים לתרום! [עריכה ב-GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoPSeriesImageToModelNode/he.md)

---
**Source fingerprint (SHA-256):** `9bfad31ee00546d0603ce3273502cfc93c79e3b125941fed255866aa83f770a5`
