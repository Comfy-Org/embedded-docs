# Tripo: הוספת מרקם למודל

## קלטים

### קלטים משותפים

| פרמטר | תיאור | סוג נתונים | חובה | טווח |
|-----------|-------------|-----------|----------|-------|
| `model_task_id` | מזהה המשימה של מודל המקור שהופק על ידי צומת Tripo קודם (יצירת מודל או פילוח מודל). | MODEL_TASK_ID / SEGMENT_TASK_ID | כן | - |
| `pbr` | מפות חומר PBR (צבע בסיס, מתכתי, חספוס, נורמל); כיבוי נותן טקסטורת צבע אחיד. (ברירת מחדל: true) | BOOLEAN | לא | true<br>false |
| `texture_seed` | Seed המשמש ליצירת טקסטורות. (ברירת מחדל: 42) קלט מתקדם. | INT | לא | 0 to 2147483647 |
| `texture_quality` | איכות הטקסטורות שנוצרות. `detailed` = טקסטורות HD, `extreme` = טקסטורות 8K Ultra. (ברירת מחדל: "standard") קלט מתקדם. | COMBO | לא | "standard"<br>"detailed"<br>"extreme" |
| `texture_alignment` | כיצד הטקסטורות מיושרות למודל. (ברירת מחדל: "original_image") קלט מתקדם. | COMBO | לא | "original_image"<br>"geometry" |
| `texture_prompt` | הנחיית טקסט אופציונלית ליצירת טקסטורות. נדרש בפועל עבור מודלים מיובאים (Tripo: Import Model), שאין להם תמונת מקור שממנה ניתן להסיק צבעים. לא ניתן לשלב עם תמונות עזר. (ברירת מחדל: ריק) | STRING | לא | - |
| `model_version` | מודל טקסטורות: v3.0 עבור meshes שנוצרו עם v3.x, v2.5 עבור meshes שנוצרו עם v2.5. (ברירת מחדל: v3_0_20250812) | COMBO | לא | גרסאות מודל טקסטורות של Tripo, ברירת מחדל "v3_0_20250812" |
| `style_image` | תמונת עזר לסגנון האמנותי של הטקסטורות. משמשת רק יחד עם `texture_prompt`. | IMAGE | לא | - |
| `reference` | תמונות עזר המנחות את הטקסטורות. לא ניתן לשלב עם `texture_prompt` או `style_image`. (ברירת מחדל: "none") | DYNAMIC_COMBO | לא | "none"<br>"image"<br>"multiview" |
| `part_names` | שמות חלקים מופרדים בפסיקים מ-Tripo: Segment Model שעבורם יש ליצור טקסטורות. ערך ריק מחיל טקסטורות על כל חלק. (ברירת מחדל: ריק) קלט מתקדם. | STRING | לא | - |

### קלטי עזר לתמונה

מוצג כאשר `reference` מוגדר ל-"image".

| פרמטר | תיאור | סוג נתונים | חובה | טווח |
|-----------|-------------|-----------|----------|-------|
| `reference_image` | תמונת עזר בודדת שיש לפעול לפיה בעת יצירת הטקסטורות. | IMAGE | כן | - |

### קלטי עזר מרובי מבטים

מוצג כאשר `reference` מוגדר ל-"multiview".

| פרמטר | תיאור | סוג נתונים | חובה | טווח |
|-----------|-------------|-----------|----------|-------|
| `image_front` | מבט חזית (0°). | IMAGE | כן | - |
| `image_left` | מבט שמאל (90°). | IMAGE | כן | - |
| `image_back` | מבט אחורי (180°). | IMAGE | כן | - |
| `image_right` | מבט ימין (270°). | IMAGE | כן | - |

**הערות לגבי אילוצי פרמטרים:**

- לא ניתן לשלב תמונות עזר (מצבי reference "image" או "multiview") עם `texture_prompt` או `style_image`.
- `style_image` מחייב לספק `texture_prompt`.
- כאשר לא ניתן `texture_prompt`, מודל המקור חייב להגיע ממשימה של text-to-model, image-to-model, multiview-to-model או texture-model. מודלים ללא תמונת מקור (מודלים מיובאים, שעברו פילוח, שהושלמו או שעברו רטופולוגיה) מחייבים `texture_prompt`, מכיוון ש-Tripo מקבל תמונות עזר רק עבור מודלים שהוא עצמו יצר.

## פלטים

| שם פלט | תיאור | סוג נתונים |
|-------------|-------------|-----------|
| `model task_id` | מזהה המשימה של פעולת הטקסטור, שניתן להעבירו לצמתי Tripo אחרים. | MODEL_TASK_ID |
| `GLB` | מודל עם טקסטורות בפורמט GLB. ריק כאשר המקור הוא quad mesh או ייבוא FBX. | FILE_3D_GLB |
| `FBX` | מודל עם טקסטורות בפורמט FBX. Tripo מחזיר FBX עבור quad meshes וייבוא FBX; אחרת ריק. | FILE_3D_FBX |

> מסמך זה נוצר על ידי בינה מלאכותית. אם מצאתם שגיאות או שיש לכם הצעות לשיפור, אתם מוזמנים לתרום! [עריכה ב-GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoTextureNodeV2/he.md)

---
**Source fingerprint (SHA-256):** `dd9b05e37fcdd29896a50451b92a267862ad94b59abfb8680c8b648390cca091`
