# העברת סגנון תמונה Magnific

צומת זה מחיל את הסגנון החזותי מתמונת עזר על תמונת הקלט שלך. הוא משתמש בשירות AI חיצוני כדי לעבד את התמונות, ומאפשר לך לשלוט בחוזק העברת הסגנון ובשימור המבנה של התמונה המקורית.

## קלטים

| פרמטר | תיאור | סוג נתונים | חובה | טווח |
|-----------|-------------|-----------|----------|-------|
| `image` | התמונה שעליה יש להחיל העברת סגנון. | IMAGE | כן | - |
| `reference_image` | תמונת העזר שממנה יש לחלץ את הסגנון. | IMAGE | כן | - |
| `prompt` | הנחיית טקסט אופציונלית להכוונת העברת הסגנון. | STRING | לא | - |
| `style_strength` | אחוז חוזק הסגנון (ברירת מחדל: 100). | INT | לא | 0 to 100 |
| `structure_strength` | שומר על המבנה של התמונה המקורית (ברירת מחדל: 50). | INT | לא | 0 to 100 |
| `flavor` | וריאציית העברת סגנון. | COMBO | לא | "faithful"<br>"gen_z"<br>"psychedelia"<br>"detaily"<br>"clear"<br>"donotstyle"<br>"donotstyle_sharp" |
| `engine` | בחירת מנוע עיבוד. | COMBO | לא | "balanced"<br>"definio"<br>"illusio"<br>"3d_cartoon"<br>"colorful_anime"<br>"caricature"<br>"real"<br>"super_real"<br>"softy" |
| `portrait_mode` | הפעל מצב דיוקן לשיפורי פנים. | COMBO | לא | "disabled"<br>"enabled" |
| `portrait_style` | סגנון חזותי שמוחל על תמונות דיוקן. קלט זה זמין רק כאשר `portrait_mode` מוגדר ל־"enabled". | COMBO | לא | "standard"<br>"pop"<br>"super_pop" |
| `portrait_beautifier` | עוצמת ייפוי פנים בדיוקנאות. קלט זה זמין רק כאשר `portrait_mode` מוגדר ל־"enabled". | COMBO | לא | "none"<br>"beautify_face"<br>"beautify_face_max" |
| `fixed_generation` | כאשר מושבת, יש לצפות שכל יצירה תציג מידה של אקראיות, מה שמוביל לתוצאות מגוונות יותר (ברירת מחדל: True). | BOOLEAN | לא | - |

**אילוצים:**

* נדרשים בדיוק `image` אחד ו־`reference_image` אחד.
* יחס הגובה-רוחב של שתי התמונות חייב להיות בין 1:3 ל-3:1.
* הגובה והרוחב המינימליים של שתי התמונות חייבים להיות 160 פיקסלים.
* הפרמטרים `portrait_style` ו־`portrait_beautifier` פעילים רק כאשר `portrait_mode` מוגדר ל־"enabled".

## פלטים

| שם פלט | תיאור | סוג נתונים |
|-------------|-------------|-----------|
| `image` | התמונה המתקבלת לאחר החלת העברת הסגנון. | IMAGE |

> מסמך זה נוצר על ידי בינה מלאכותית. אם מצאתם שגיאות או שיש לכם הצעות לשיפור, אתם מוזמנים לתרום! [עריכה ב-GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MagnificImageStyleTransferNode/he.md)

---
**Source fingerprint (SHA-256):** `edffec024ebe7cbf7c42008e14c1b99d6fafcf5b9da62b0b560d194a585dc9ad`
