# TripoRetargetNode

TripoRetargetNode מחיל אנימציה מוגדרת מראש על מודל תלת-ממדי מרוגר קיים. הוא מקבל את מזהה המשימה של מודל שרוגר קודם לכן, שולח בקשת רטרגוט ל-API של Tripo, ומוריד את הקובץ המונפש שנוצר. ניתן להחזיר את המודל המונפש כ-GLB או FBX, עם גאומטריית mesh אופציונלית והפעלה במקום אופציונלית.

## קלטים

| פרמטר | תיאור | סוג נתונים | חובה | טווח |
|-----------|-------------|-----------|----------|-------|
| `original_model_task_id` | מזהה המשימה של המודל התלת-ממדי המרוגר שאליו יש להחיל רטרגוט. המשימה שאליה מפנים חייבת להיות משימת ריג. | RIG_TASK_ID | כן | - |
| `animation` | אנימציית הפריסט להחלה על המודל המרוגר. אנימציות `preset:*` עובדות עם שני סוגי מודלי הריג. אנימציות `preset:biped:*` מיועדות לריגים ממודל v1.0-20240301; ריג v2.5 מקבל רק chop, climb, dive, fall, hurt, idle, jump, run, shoot, slash, turn ו-walk. | COMBO | כן | `"preset:idle"`<br>`"preset:walk"`<br>`"preset:run"`<br>`"preset:dive"`<br>`"preset:climb"`<br>`"preset:jump"`<br>`"preset:slash"`<br>`"preset:shoot"`<br>`"preset:hurt"`<br>`"preset:fall"`<br>`"preset:turn"`<br>`"preset:quadruped:walk"`<br>`"preset:hexapod:walk"`<br>`"preset:octopod:walk"`<br>`"preset:serpentine:march"`<br>`"preset:aquatic:march"`<br>בתוספת אפשרויות `"preset:biped:*"` נוספות המוצגות בממשק המשתמש |
| `out_format` | פורמט קובץ הפלט; התוצאה מגיעה בפלט המתאים. (ברירת מחדל: glb) | COMBO | לא | `"glb"`<br>`"fbx"` |
| `export_with_geometry` | כלול את ה-mesh בייצוא; כבוי מייצא רק את השלד המונפש. (ברירת מחדל: True) | BOOLEAN | לא | True<br>False |
| `animate_in_place` | הפעל את האנימציה במקום, ללא תזוזה של השורש. (ברירת מחדל: False) | BOOLEAN | לא | True<br>False |
| `auth_token_comfy_org` | אסימון אימות לגישה ל-API של Comfy.org (פרמטר מוסתר). | AUTH_TOKEN_COMFY_ORG | לא | - |
| `api_key_comfy_org` | מפתח API לגישה לשירות Comfy.org (פרמטר מוסתר). | API_KEY_COMFY_ORG | לא | - |
| `unique_id` | מזהה ייחודי למעקב אחר הפעולה (פרמטר מוסתר). | UNIQUE_ID | לא | - |

הערה: אנימציות בקבוצת `preset:*` עובדות עם שני סוגי מודלי הריג. אנימציות בקבוצת `preset:biped:*` מיועדות לריגים ממודל v1.0-20240301; ריג v2.5 מקבל רק chop, climb, dive, fall, hurt, idle, jump, run, shoot, slash, turn ו-walk. אם הריג שאליו מפנים נוצר עם מפרט Mixamo וגרסת מודל שמתחילה ב-`v1.0`, קריאת הרטרגוט נכשלת עם שגיאה. פורמט הפלט המבוקש חייב להיות GLB או FBX; אם השירות מחזיר סוג קובץ אחר, הצומת מעלה שגיאה.

## פלטים

| שם פלט | תיאור | סוג נתונים |
|-------------|-------------|-----------|
| `model_file` | קובץ המודל התלת-ממדי המונפש שנוצר (לצורך תאימות לאחור בלבד). | STRING |
| `retarget task_id` | מזהה המשימה למעקב אחר פעולת הרטרגוט. | RETARGET_TASK_ID |
| `GLB` | המודל התלת-ממדי המונפש בפורמט GLB. מאוכלס כאשר `out_format` הוא glb. | FILE3DGLB |
| `FBX` | המודל התלת-ממדי המונפש בפורמט FBX. מאוכלס כאשר `out_format` הוא fbx. | FILE3DFBX |

> מסמך זה נוצר על ידי בינה מלאכותית. אם מצאתם שגיאות או שיש לכם הצעות לשיפור, אתם מוזמנים לתרום! [עריכה ב-GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoRetargetNode/he.md)

---
**Source fingerprint (SHA-256):** `4814858b940ece13f85010ff81fcdac0258fe8550aebd914be2613e8f40c0e5a`
