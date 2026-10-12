# Tripo: המרת מודל

צומת זה ממיר מודל Tripo 3D קיים לפורמט קובץ 3D אחר. הוא מקבל מזהה משימה (Task ID) של מודל שנוצר או עובד קודם לכן באמצעות פעולת Tripo (כגון יצירת מודל, ריגינג, ריטרגוט או סגמנטציה), שולח משימת המרה ל-API של Tripo, ממתין להשלמת המשימה, ולאחר מכן מחזיר את קובץ המודל המומר.

## קלטים

| פרמטר | תיאור | סוג נתונים | חובה | טווח |
|-----------|-------------|-----------|----------|-------|
| `original_model_task_id` | מזהה המשימה (Task ID) של מודל Tripo שיש להמיר. עליו להגיע ממשימת יצירת מודל, ריגינג, ריטרגוט או סגמנטציה קודמת של Tripo. אם המזהה חסר או ריק, הצומת מעלה שגיאה. | STRING | כן | MODEL_TASK_ID<br>RIG_TASK_ID<br>RETARGET_TASK_ID<br>SEGMENT_TASK_ID |
| `format` | פורמט קובץ היעד עבור מודל ה-3D המומר. | COMBO | כן | GLTF<br>USDZ<br>FBX<br>OBJ<br>STL<br>3MF |
| `quad` | להמיר משולשים לקוואדים כאשר מופעל (ברירת מחדל: False). | BOOLEAN | לא | True or False |
| `face_limit` | מספר הפאות המקסימלי במודל המומר. יש להגדיר -1 ללא הגבלה (ברירת מחדל: -1). | INT | לא | -1 to 2000000 |
| `texture_size` | רזולוציית טקסטורות הפלט בפיקסלים (ברירת מחדל: 4096). | INT | לא | 128 to 8192 |
| `texture_format` | פורמט הקובץ המשמש לטקסטורות מיוצאות (ברירת מחדל: JPEG). | COMBO | לא | BMP<br>DPX<br>HDR<br>JPEG<br>OPEN_EXR<br>PNG<br>TARGA<br>TIFF<br>WEBP |
| `force_symmetry` | לכפות סימטריה על המודל כאשר מופעל (ברירת מחדל: False). | BOOLEAN | לא | True or False |
| `flatten_bottom` | לשטח את החלק התחתון של המודל כאשר מופעל (ברירת מחדל: False). | BOOLEAN | לא | True or False |
| `flatten_bottom_threshold` | עומק השיטוח המשמש עם `flatten_bottom` (ברירת מחדל: 0.01). ערך זה מוחל רק כאשר `flatten_bottom` מופעל. | FLOAT | לא | 0.01 to 1.0 |
| `pivot_to_center_bottom` | להעביר את נקודת הציר למרכז החלק התחתון של המודל כאשר מופעל (ברירת מחדל: False). | BOOLEAN | לא | True or False |
| `scale_factor` | מקדם קנה מידה המוחל על המודל המומר (ברירת מחדל: 1.0). | FLOAT | לא | 0.01 and above |
| `with_animation` | לשמור על השלד והאנימציה של מודלים שעברו ריגינג או ריטרגוט (ברירת מחדל: True). | BOOLEAN | לא | True or False |
| `pack_uv` | לארוז מחדש את קואורדינטות ה-UV כאשר מופעל (ברירת מחדל: False). | BOOLEAN | לא | True or False |
| `bake` | לאפות חומרים מתקדמים לתוך טקסטורות הבסיס לצורך תאימות רחבה יותר (ברירת מחדל: True). | BOOLEAN | לא | True or False |
| `part_names` | רשימת שמות חלקי מודל מופרדת בפסיקים לשליחה להמרה. רשומות ריקות מתעלמות מהן ושמות כפולים מוסרים. יש להשאיר ריק כדי להשמיט אפשרות זו (ברירת מחדל: ריק). | STRING | לא | רשימת שמות חלקים מופרדת בפסיקים |
| `fbx_preset` | פריסט תאימות ל-FBX. bake_scale אופה את טרנספורמציית קנה המידה לתוך הגיאומטריה (ברירת מחדל: blender). | COMBO | לא | blender<br>mixamo<br>3dsmax<br>bake_scale |
| `export_vertex_colors` | לייצא צבעי קודקודים כאשר מופעל (ברירת מחדל: False). | BOOLEAN | לא | True or False |
| `export_orientation` | ציר קדימה של המודל המיוצא. default שומר על +x של Tripo (ברירת מחדל: default). | COMBO | לא | default<br>+x<br>-x<br>+y<br>-y |
| `animate_in_place` | להנפיש את המודל במקום כאשר מופעל (ברירת מחדל: False). | BOOLEAN | לא | True or False |

**הערה:** למעט `original_model_task_id` ו-`format`, כל הקלטים הם הגדרות מתקדמות אופציונליות. רוב ההגדרות שנותרות בערכי ברירת המחדל שלהן מושמטות מבקשת ההמרה כדי שה-API של Tripo יוכל להשתמש בהתנהגות הסטנדרטית שלו. האפשרויות `with_animation` ו-`bake` נשלחות תמיד. `flatten_bottom_threshold` מוחל רק כאשר `flatten_bottom` מופעל.

## פלטים

| שם פלט | תיאור | סוג נתונים |
|-------------|-------------|-----------|
| `model_3d` | מודל מומר בפורמט המבוקש. OBJ מסופק על ידי Tripo כארכיון ZIP (רשת, חומר וטקסטורות). | FILE_3D |

> מסמך זה נוצר על ידי בינה מלאכותית. אם מצאתם שגיאות או שיש לכם הצעות לשיפור, אתם מוזמנים לתרום! [עריכה ב-GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoConversionNode/he.md)

---
**Source fingerprint (SHA-256):** `b6be09bf6b1c5ccd6de5ae56ed28bfe1f0b81c1ca8ff61623e3094917c98d68a`
