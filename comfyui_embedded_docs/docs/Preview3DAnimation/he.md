# Preview3DAnimation

הצומת Preview3DAnimation משמש בעיקר לתצוגה מקדימה של פלטי מודלים תלת-ממדיים. צומת זה מקבל שני קלטים: האחד הוא `camera_info` מצומת Load3D, והשני הוא הנתיב לקובץ המודל התלת-ממדי. נתיב קובץ המודל חייב להיות ממוקם בתיקיית `ComfyUI/output`.

**פורמטים נתמכים**
נכון לעכשיו, צומת זה תומך במספר פורמטים של קבצים תלת-ממדיים, כולל `.gltf`, `.glb`, `.obj`, `.fbx` ו-`.stl`.

**העדפות צומת תלת-ממד**
ניתן להגדיר העדפות קשורות עבור צמתים תלת-ממדיים בתפריט ההגדרות של ComfyUI. אנא עיין בתיעוד הבא עבור ההגדרות המתאימות:
[תפריט הגדרות](https://docs.comfy.org/interface/settings/3d)

## קלטים

| שם פרמטר | תיאור | סוג |
| --- | --- | --- |
| camera_info | מידע מצלמה | LOAD3D_CAMERA |
| model_file | נתיב קובץ מודל תחת `ComfyUI/output/` | STRING |

## תיאור אזור הקנבס

נכון לעכשיו, הצמתים הקשורים ל-3D ב-frontend של ComfyUI חולקים את אותו רכיב קנבס, ולכן פעולות הבסיס שלהם זהות ברובן למעט כמה הבדלים פונקציונליים.

> התוכן והממשק שלהלן מבוססים בעיקר על צומת Load3D. אנא עיין בממשק הצומת בפועל עבור תכונות ספציפיות.

אזור הקנבס כולל פעולות תצוגה שונות, כגון:

- הגדרות תצוגה מקדימה (רשת, צבע רקע, תצוגה מקדימה)
- בקרת מצלמה: FOV, סוג מצלמה
- עוצמת תאורה גלובלית: כוונון תאורה
- ייצוא מודל: תומך בפורמטים `GLB`, `OBJ`, `STL`
- וכו'.

![ממשק צומת Load 3D](../Preview3D/asset/preview3d_canvas.jpg)

1. מכיל מספר תפריטים ותפריטים מוסתרים של צומת Load 3D
2. ציר פעולות תצוגת 3D

### 1. פעולות תצוגה

<video controls width="640" height="360">
  <source src="https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/Load3D/asset/view_operations.mp4" type="video/mp4">
  הדפדפן שלך אינו תומך בהפעלת וידאו.
</video>

פעולות בקרת תצוגה:

- לחיצה שמאלית + גרירה: סיבוב התצוגה
- לחיצה ימנית + גרירה: הזזת התצוגה
- גלילת גלגלת אמצעית או לחיצה אמצעית + גרירה: התקרבות/התרחקות
- ציר קואורדינטות: החלפת תצוגות

### 2. פונקציות התפריט השמאלי

![תפריט](https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/Load3d/asset/menu.webp)

באזור התצוגה המקדימה, חלק מתפריטי פעולות התצוגה מוסתרים בתפריט. לחץ על כפתור התפריט כדי להרחיב תפריטים שונים.

- 1. סצנה: מכילה רשת של חלון התצוגה המקדימה, צבע רקע והגדרות תמונה ממוזערת
- 2. מודל: מצב רינדור המודל, חומר טקסטורה, הגדרות כיוון מעלה
- 3. מצלמה: מעבר בין תצוגה אורתוגרפית לתצוגת פרספקטיבה, הגדרת זווית פרספקטיבה
- 4. תאורה: עוצמת תאורה גלובלית של הסצנה
- 5. ייצוא: ייצוא המודל לפורמטים אחרים (GLB, OBJ, STL)

#### סצנה

![תפריט סצנה](https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/Load3d/asset/menu_scene.webp)

תפריט הסצנה מספק מספר פונקציות בסיסיות להגדרת הסצנה:

1. הצגה/הסתרה של רשת
2. הגדרת צבע רקע
3. לחיצה להעלאת תמונת רקע
4. הסתרת תמונה ממוזערת של התצוגה המקדימה

#### מודל

![תפריט מודל](https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/Load3d/asset/menu_model.webp)

תפריט המודל מספק מספר פונקציות הקשורות למודל:

1. **כיוון מעלה**: קביעת הציר שמייצג את כיוון המעלה עבור המודל
2. **מצב חומר**: החלפה בין מצבי רינדור המודל - Original, Normal, Wireframe, Lineart

#### מצלמה

![תפריט מצלמה](https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/Load3d/asset/menu_camera.webp)

תפריט זה מספק מעבר בין תצוגה אורתוגרפית לתצוגת פרספקטיבה, והגדרת גודל זווית הפרספקטיבה:

1. **מצלמה**: מעבר מהיר בין תצוגה אורתוגרפית לתצוגת פרספקטיבה
2. **FOV**: כוונון זווית FOV

#### תאורה

![תפריט תאורה](https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/Load3d/asset/menu_light.webp)

דרך תפריט זה ניתן לכוונן במהירות את עוצמת התאורה הגלובלית של הסצנה

#### ייצוא

![תפריט ייצוא](https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/Load3d/asset/menu_export.webp)

תפריט זה מספק את היכולת להמיר ולייצא פורמטים של מודלים במהירות

> מסמך זה נוצר על ידי בינה מלאכותית. אם מצאתם שגיאות או שיש לכם הצעות לשיפור, אתם מוזמנים לתרום! [עריכה ב-GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Preview3DAnimation/he.md)
