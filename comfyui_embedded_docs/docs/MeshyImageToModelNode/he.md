# MeshyImageToModelNode

הצומת Meshy: Image to Model משתמש ב-API של Meshy כדי ליצור מודל תלת-ממדי מתמונת קלט בודדת. הוא מעלה את התמונה שלך, שולח משימת עיבוד, ומחזיר את קבצי המודל התלת-ממדיים שנוצרו (GLB ו-FBX) יחד עם מזהה המשימה לצורך התייחסות.

## קלטים

| פרמטר | תיאור | סוג נתונים | חובה | טווח |
| --- | --- | --- | --- | --- |
| `model` | מציין את גרסת מודל ה-AI לשימוש ביצירה. | COMBO | כן | `"meshy-7.1"`<br>`"meshy-7"`<br>`"meshy-6"`<br>`"latest"` |
| `image` | תמונת הקלט להמרה למודל תלת-ממדי. | IMAGE | כן | - |
| `should_remesh` | כאשר מוגדר ל-`"false"`, מחזיר רשת משולשת לא מעובדת. | DYNAMIC_COMBO | כן | `"true"`<br>`"false"` |
| `topology` | טופולוגיית הפוליגונים הרצויה למודל המרומש. קלט זה זמין רק כאשר `should_remesh` מוגדר ל-`"true"`. | COMBO | לא* | `"triangle"`<br>`"quad"` |
| `target_polycount` | מספר הפוליגונים הרצוי למודל המרומש. קלט זה זמין רק כאשר `should_remesh` מוגדר ל-`"true"`. ברירת מחדל: 300000. | INT | לא* | 100 - 300000 |
| `symmetry_mode` | שולט בסימטריה המיושמת על המודל התלת-ממדי שנוצר. | COMBO | כן | `"auto"`<br>`"on"`<br>`"off"` |
| `should_texture` | קובע אם נוצרות טקסטורות. הגדרה ל-`"false"` מדלגת על שלב הטקסטורה ומחזירה רשת ללא טקסטורות. | DYNAMIC_COMBO | כן | `"true"`<br>`"false"` |
| `enable_pbr` | יצירת מפות PBR (מתכתי, חספוס, נורמל) בנוסף לצבע הבסיס. קלט זה זמין רק כאשר `should_texture` מוגדר ל-`"true"`. ברירת מחדל: `False`. | BOOLEAN | לא* | - |
| `texture_prompt` | ספק הנחיית טקסט כדי להנחות את תהליך הטקסטורה. מקסימום 600 תווים. לא ניתן להשתמש בו בו-זמנית עם `texture_image`. קלט זה זמין רק כאשר `should_texture` מוגדר ל-`"true"`. ברירת מחדל: מחרוזת ריקה. | STRING | לא* | - |
| `texture_image` | ניתן להשתמש רק באחד מ-`texture_image` או `texture_prompt` בו-זמנית. קלט זה זמין רק כאשר `should_texture` מוגדר ל-`"true"`. | IMAGE | לא* | - |
| `texture_resolution` | רזולוציית טקסטורת צבע הבסיס. רזולוציות גבוהות יותר לוכדות יותר פרטי שטח. קלט זה זמין רק כאשר `should_texture` מוגדר ל-`"true"`. | COMBO | לא* | `"2k"`<br>`"4k"`<br>`"8k"` |
| `pose_mode` | ציין את מצב התנוחה עבור המודל שנוצר. זהו פרמטר מתקדם. | COMBO | כן | `""` (ריק)<br>`"A-pose"`<br>`"T-pose"` |
| `seed` | Seed קובע אם הצומת צריך לרוץ מחדש; התוצאות אינן דטרמיניסטיות ללא קשר ל-seed. ברירת מחדל: 0. | INT | כן | 0 - 2147483647 |
| `ultra_mode` | הפעל מעבר עידון נוסף עבור גיאומטריה בנאמנות גבוהה יותר עם פרטי שטח עדינים יותר. ברירת מחדל: `False`. | BOOLEAN | כן | - |
| `ultra_resolution` | רזולוציית מעבר האולטרה: `"2k"` מריץ אותו ב-2048³, `"4k"` ב-4096³ עבור פרטי השטח העדינים ביותר. 4k דורש את המודל `"meshy-7.1"` או `"latest"`. משמש רק כאשר `ultra_mode` מופעל (ברירת מחדל: `"2k"`). | COMBO | לא | `"2k"`<br>`"4k"` |

**הערה על אילוצי פרמטרים:**

* קלטי `topology` ו-`target_polycount` זמינים רק כאשר `should_remesh` מוגדר ל-`"true"`.
* קלטי `enable_pbr`, `texture_prompt`, `texture_image`, ו-`texture_resolution` זמינים רק כאשר `should_texture` מוגדר ל-`"true"`.
* כאשר `should_texture` מוגדר ל-`"true"`, לא ניתן להשתמש ב-`texture_prompt` וב-`texture_image` בו-זמנית. אם שניהם מסופקים, הצומת מעלה שגיאה.
* ל-`texture_prompt` אורך מקסימלי של 600 תווים.
* כאשר `ultra_mode` מופעל, יש להגדיר את הפרמטר `model` ל-`"meshy-7.1"`, `"meshy-7"` או `"latest"`; כל מודל אחר מעלה שגיאה. עם `"meshy-7"` מעבר האולטרה תמיד רץ ב-2048³, ורזולוציית האולטרה `"4k"` דורשת `"meshy-7.1"` או `"latest"`.

## פלטים

| שם פלט | תיאור | סוג נתונים |
| --- | --- | --- |
| `model_file` | שם הקובץ של מודל ה-GLB שנוצר. נשמר רק עבור תאימות לאחור. | STRING |
| `meshy_task_id` | המזהה הייחודי של משימת ה-API של Meshy, שיכול לשמש להתייחסות או לפתרון בעיות. | MESHY_TASK_ID |
| `GLB` | המודל התלת-ממדי שנוצר בפורמט קובץ GLB. | FILE3DGLB |
| `FBX` | המודל התלת-ממדי שנוצר בפורמט קובץ FBX. | FILE3DFBX |

> מסמך זה נוצר על ידי בינה מלאכותית. אם מצאתם שגיאות או שיש לכם הצעות לשיפור, אתם מוזמנים לתרום! [עריכה ב-GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyImageToModelNode/he.md)

---
**Source fingerprint (SHA-256):** `38528b48c3f792a459008a52f65fae248ef1dadafb37fe4dc6b697d25bc89f4f`
