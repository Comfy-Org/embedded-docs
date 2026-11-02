# Patina PBR Material Maps

מפיק סט של מפות חומר PBR מתמונת טקסטורה קיימת: basecolor, normal, roughness, metalness ו-height. הפעל רק את המפות שאתה צריך, מכיוון שכל מפה מופעלת מוסיפה לעלות. השתמש בו כדי להשלים טקסטורה שאין לה עדיין מפות חומר, או כדי לבנות מחדש מפה בודדת פגומה.

## קלטים

| פרמטר | תיאור | סוג נתונים | חובה | טווח |
|-----------|-------------|-----------|----------|-------|
| `image` | התמונה או הרינדור שמשמשים להפקת מפות ה-PBR. | IMAGE | כן | - |
| `basecolor` | צור את מפת ה-basecolor (albedo). ברירת מחדל: True. | BOOLEAN | כן | true<br>false |
| `normal` | צור את מפת ה-normal. ברירת מחדל: True. | BOOLEAN | כן | true<br>false |
| `roughness` | צור את מפת ה-roughness. ברירת מחדל: False. | BOOLEAN | כן | true<br>false |
| `metalness` | צור את מפת ה-metalness. ברירת מחדל: False. | BOOLEAN | כן | true<br>false |
| `height` | צור את מפת ה-height (displacement). ברירת מחדל: False. | BOOLEAN | כן | true<br>false |
| `seed` | Seed עבור הסרת רעש ניתנת לשחזור. ברירת מחדל: 42. | INT | כן | 0 עד 2147483646 |
| `safety_checker` | הפעל את בדיקת בטיחות התוכן של הספק על הבקשה. הגדרה מתקדמת. ברירת מחדל: False. | BOOLEAN | כן | true<br>false |
| `auto_downscale` | הקטן אוטומטית תמונת קלט שהצד הארוך ביותר שלה עולה על 2048 פיקסלים, מגבלת הקלט של המודל, תוך שמירה על יחס הגובה-רוחב; תמונות קטנות יותר נשארות כפי שהן. השבת אותה כדי להחזיר שגיאה עבור תמונות גדולות מדי במקום זאת. הגדרה מתקדמת. ברירת מחדל: True. | BOOLEAN | לא | true<br>false |

**אילוצים והתנהגות:**

* יש להפעיל לפחות מפה אחת, אחרת ההרצה נכשלת.
* תמונת הקלט מוגבלת ל-2048 פיקסלים בצד הארוך ביותר שלה; או לתת ל-`auto_downscale` להקטין אותה, או שההרצה תיכשל בתמונה גדולה מדי.
* כל מפה מושבתת עדיין מחזירה פלט, אך כתמונת placeholder בגודל 1x1, לכן חבר רק את הפלטים שבאמת יצרת.

## פלטים

| שם פלט | תיאור | סוג נתונים |
|-------------|-------------|-----------|
| `basecolor` | מפת ה-basecolor (albedo) שנוצרה, או placeholder בגודל 1x1 כאשר המפה מושבתת. | IMAGE |
| `normal` | מפת ה-normal שנוצרה, או placeholder בגודל 1x1 כאשר המפה מושבתת. | IMAGE |
| `roughness` | מפת ה-roughness שנוצרה, או placeholder בגודל 1x1 כאשר המפה מושבתת. | IMAGE |
| `metalness` | מפת ה-metalness שנוצרה, או placeholder בגודל 1x1 כאשר המפה מושבתת. | IMAGE |
| `height` | מפת ה-height (displacement) שנוצרה, או placeholder בגודל 1x1 כאשר המפה מושבתת. | IMAGE |

> מסמך זה נוצר על ידי בינה מלאכותית. אם מצאתם שגיאות או שיש לכם הצעות לשיפור, אתם מוזמנים לתרום! [עריכה ב-GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PatinaPBRMapsNode/he.md)

---
**Source fingerprint (SHA-256):** `813c5bb3336c5ca54a9ca9ee95e84e7f27791170650248d0169acee39c4b3ce1`
