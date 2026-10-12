# Load3DAnimation

צומת Load3DAnimation הוא צומת ליבה לטעינה ועיבוד של קובצי מודלי 3D. בעת טעינת הצומת, הוא שולף אוטומטית משאבי 3D זמינים מ-`ComfyUI/input/3d/`. ניתן גם להעלות קובצי 3D נתמכים לתצוגה מקדימה באמצעות פונקציית ההעלאה.

> - רוב הפונקציות של צומת זה זהות לאלה של צומת Load 3D, אך צומת זה תומך בטעינת מודלים עם אנימציות, וניתן להציג תצוגה מקדימה של האנימציות המתאימות בצומת.
> - תוכן התיעוד הזה זהה לזה של צומת Load3D, מכיוון שמלבד תצוגה מקדימה והפעלה של אנימציות, היכולות שלהן זהות.

**פורמטים נתמכים**
נכון לעכשיו, צומת זה תומך במספר פורמטים של קובצי 3D, כולל `.gltf`, `.glb`, `.obj`, `.fbx` ו-`.stl`.

**העדפות צומת 3D**
ניתן להגדיר העדפות קשורות לצומת 3D בתפריט ההגדרות של ComfyUI. אנא עיין בתיעוד הבא להגדרות המתאימות:

[תפריט הגדרות](https://docs.comfy.org/interface/settings/3d)

מלבד פלטים רגילים של הצומת, ל-Load3D יש הגדרות רבות הקשורות לתצוגת 3D בתפריט הקנבס.

## קלטים

| שם פרמטר | תיאור | סוג | ברירת מחדל | טווח |
| --- | --- | --- | --- | --- |
| model_file | נתיב קובץ מודל 3D, תומך בהעלאה, כברירת מחדל קורא קובצי מודל מ-`ComfyUI/input/3d/` | בחירת קובץ | - | פורמטים נתמכים |
| width | רוחב רינדור הקנבס | INT | 1024 | 1-4096 |
| height | גובה רינדור הקנבס | INT | 1024 | 1-4096 |

## פלטים

| שם פלט | תיאור | סוג נתונים |
| --- | --- | --- |
| image | תמונה מרונדרת של הקנבס | IMAGE |
| mask | מסכה המכילה את מיקום המודל הנוכחי | MASK |
| mesh_path | נתיב קובץ המודל | STRING |
| normal | מפת נורמלים | IMAGE |
| lineart | פלט תמונת קווי מתאר; ניתן לכוונן את `edge_threshold` המתאים בתפריט המודל בקנבס | IMAGE |
| camera_info | מידע על המצלמה | LOAD3D_CAMERA |
| recording_video | וידאו מוקלט (רק כאשר קיימת הקלטה) | VIDEO |

תצוגה מקדימה של כל הפלטים:
![תצוגת כל הפלטים](../Load3D/asset/load3d_outputs.webp)

## תיאור אזור הקנבס

אזור הקנבס של צומת Load3D מכיל פעולות תצוגה רבות, כולל:

- הגדרות תצוגה מקדימה (רשת, צבע רקע, תצוגה מקדימה)
- שליטת מצלמה: שליטה ב-FOV, סוג מצלמה
- עוצמת תאורה גלובלית: כוונון עוצמת התאורה
- הקלטת וידאו: הקלטה וייצוא של סרטונים
- ייצוא מודל: תומך בפורמטים `GLB`, `OBJ`, `STL`
- ועוד

![ממשק צומת Load 3D](../Load3D/asset/load3d_ui.jpg)

1. מכיל מספר תפריטים ותפריטים מוסתרים של צומת Load 3D
2. תפריט ל`שינוי גודל חלון התצוגה המקדימה` ו`הקלטת וידאו בקנבס`
3. ציר פעולות תצוגת 3D
4. תמונה ממוזערת של תצוגה מקדימה
5. הגדרות גודל תצוגה מקדימה; שינוי קנה המידה של התצוגה המקדימה על ידי הגדרת מידות ואז שינוי גודל החלון

### 1. פעולות תצוגה

<video controls width="640" height="360">
  <source src="https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/Load3D/asset/view_operations.mp4" type="video/mp4">
  הדפדפן שלך אינו תומך בהפעלת וידאו.
</video>

פעולות שליטת תצוגה:

- לחיצה שמאלית + גרירה: סיבוב התצוגה
- לחיצה ימנית + גרירה: הזזת התצוגה
- גלגלת אמצעית או לחיצה אמצעית + גרירה: זום פנימה/החוצה
- ציר קואורדינטות: החלפת תצוגות

### 2. פונקציות התפריט השמאלי

![תפריט](https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/Load3d/asset/menu.webp)

בקנבס, חלק מההגדרות מוסתרות בתפריט. לחץ על כפתור התפריט כדי לפרוס תפריטים שונים

- 1. סצנה: כוללת רשת חלון תצוגה מקדימה, צבע רקע, הגדרות תצוגה מקדימה
- 2. מודל: מצב רינדור המודל, חומרי טקסטורה, הגדרות כיוון מעלה
- 3. מצלמה: החלפה בין תצוגות אורתוגרפיות לפרספקטיביות, וקביעת גודל זווית הפרספקטיבה
- 4. תאורה: עוצמת תאורה גלובלית של הסצנה
- 5. ייצוא: ייצוא המודל לפורמטים אחרים (GLB, OBJ, STL)

#### סצנה

![תפריט סצנה](https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/Load3d/asset/menu_scene.webp)

תפריט הסצנה מספק כמה פונקציות בסיסיות להגדרת הסצנה

1. הצג/הסתר רשת
2. קביעת צבע רקע
3. לחץ כדי להעלות תמונת רקע
4. הסתר את התצוגה המקדימה

#### מודל

![תפריט מודל](https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/Load3d/asset/menu_model.webp)

תפריט המודל מספק כמה פונקציות הקשורות למודל

1. **כיוון מעלה**: קביעת הציר שמהווה את כיוון המעלה של המודל
2. **מצב חומר**: החלפת מצבי רינדור המודל - Original, Normal, Wireframe, Lineart

#### מצלמה

![תפריט מצלמה](https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/Load3d/asset/menu_camera.webp)

תפריט זה מספק מעבר בין תצוגות אורתוגרפיות לפרספקטיביות, והגדרות גודל זווית פרספקטיבה

1. **מצלמה**: מעבר מהיר בין תצוגות אורתוגרפיות
2. **FOV**: כוונון זווית FOV

#### תאורה

![תפריט תאורה](https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/Load3d/asset/menu_light.webp)

באמצעות תפריט זה, ניתן לכוונן במהירות את עוצמת התאורה הגלובלית של הסצנה

#### ייצוא

![תפריט ייצוא](https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/Load3d/asset/menu_export.webp)

תפריט זה מספק את היכולת להמיר ולייצא פורמטים של מודלים במהירות

### 3. פונקציות התפריט הימני

<video controls width="640" height="360">
  <source src="https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/Load3D/asset/recording.mp4" type="video/mp4">
  הדפדפן שלך אינו תומך בהפעלת וידאו.
</video>

לתפריט הימני שתי פונקציות עיקריות:

1. **איפוס יחס תצוגה**: לאחר לחיצה על הכפתור, התצוגה תתאים את יחס אזור הרינדור של הקנבס בהתאם לרוחב ולגובה שהוגדרו
2. **הקלטת וידאו**: מאפשר להקליט פעולות תצוגת 3D נוכחיות כווידאו, מאפשר ייבוא, ויכול להיות מופק כ-`recording_video` לצמתים עוקבים

> מסמך זה נוצר על ידי בינה מלאכותית. אם מצאתם שגיאות או שיש לכם הצעות לשיפור, אתם מוזמנים לתרום! [עריכה ב-GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Load3DAnimation/he.md)
