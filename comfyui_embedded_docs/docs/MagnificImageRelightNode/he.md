# Magnific Image Relight

צומת Magnific Image Relight מתאים את התאורה של תמונת קלט. הוא יכול להחיל תאורה סגנונית בהתאם להנחיית טקסט או להעביר את מאפייני התאורה מתמונת עזר אופציונלית. הצומת מציע בקרות שונות לכוונון עדין של הבהירות, הניגודיות והאווירה הכללית של הפלט הסופי.

## קלטים

| פרמטר | תיאור | סוג נתונים | חובה | טווח |
| --- | --- | --- | --- | --- |
| `image` | התמונה שעבורה יש לבצע התאמת תאורה מחדש. נדרשת תמונה אחת בדיוק. מידות מינימליות הן 160x160 פיקסלים. יחס הגובה-רוחב חייב להיות בין 1:3 ל-3:1. | IMAGE | כן | N/A |
| `prompt` | הנחיה תיאורית לתאורה. תומך בסימון הדגשה (1-1.4). ברירת מחדל היא מחרוזת ריקה. | STRING | לא | N/A |
| `light_transfer_strength` | עוצמת יישום העברת התאורה. ברירת מחדל: 100. | INT | כן | 0 to 100 |
| `style` | העדפת סגנון פלט. | COMBO | כן | `"standard"`<br>`"darker_but_realistic"`<br>`"clean"`<br>`"smooth"`<br>`"brighter"`<br>`"contrasted_n_hdr"`<br>`"just_composition"` |
| `interpolate_from_original` | מגביל את חופש היצירה כדי להתאים מקרוב יותר למקור. ברירת מחדל: False. | BOOLEAN | כן | N/A |
| `change_background` | משנה את הרקע בהתאם להנחיה/תמונת עזר. ברירת מחדל: True. | BOOLEAN | כן | N/A |
| `preserve_details` | שומר על מרקם ופרטים עדינים מהמקור. ברירת מחדל: True. | BOOLEAN | כן | N/A |
| `advanced_settings` | אפשרויות כוונון עדין לשליטה מתקדמת בתאורה. כאשר מוגדר ל-`"enabled"`, פרמטרים נוספים הופכים לזמינים. | DYNAMICCOMBO | כן | `"disabled"`<br>`"enabled"` |
| `reference_image` | תמונת עזר אופציונלית שממנה להעביר תאורה. אם סופקה, נדרשת תמונה אחת בדיוק. מידות מינימליות הן 160x160 פיקסלים. יחס הגובה-רוחב חייב להיות בין 1:3 ל-3:1. | IMAGE | לא | N/A |

**הערה לגבי הגדרות מתקדמות:** כאשר `advanced_settings` מוגדר ל-`"enabled"`, הפרמטרים המקוננים הבאים הופכים לפעילים:

* `whites`: מתאים את הטונים הבהירים ביותר בתמונה. טווח: 0 עד 100. ברירת מחדל: 50.
* `blacks`: מתאים את הטונים הכהים ביותר בתמונה. טווח: 0 עד 100. ברירת מחדל: 50.
* `brightness`: התאמת בהירות כללית. טווח: 0 עד 100. ברירת מחדל: 50.
* `contrast`: התאמת ניגודיות. טווח: 0 עד 100. ברירת מחדל: 50.
* `saturation`: התאמת רוויה של צבע. טווח: 0 עד 100. ברירת מחדל: 50.
* `engine`: בחירת מנוע עיבוד. אפשרויות: `"automatic"`, `"balanced"`, `"cool"`, `"real"`, `"illusio"`, `"fairy"`, `"colorful_anime"`, `"hard_transform"`, `"softy"`.
* `transfer_light_a`: עוצמת העברת האור. אפשרויות: `"automatic"`, `"low"`, `"medium"`, `"normal"`, `"high"`, `"high_on_faces"`.
* `transfer_light_b`: משנה גם את עוצמת העברת האור. ניתן לשלב עם הבקרה הקודמת להשפעות מגוונות. אפשרויות: `"automatic"`, `"composition"`, `"straight"`, `"smooth_in"`, `"smooth_out"`, `"smooth_both"`, `"reverse_both"`, `"soft_in"`, `"soft_out"`, `"soft_mid"`, `"style_shift"`, `"strong_shift"`.
* `fixed_generation`: מבטיח פלט עקבי עם אותן הגדרות. ברירת מחדל: True.

## פלטים

| שם פלט | תיאור | סוג נתונים |
| --- | --- | --- |
| `image` | התמונה שעברה תאורה מחדש. | IMAGE |

> מסמך זה נוצר על ידי בינה מלאכותית. אם מצאתם שגיאות או שיש לכם הצעות לשיפור, אתם מוזמנים לתרום! [עריכה ב-GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MagnificImageRelightNode/he.md)

---
**Source fingerprint (SHA-256):** `45fe68b21e1da7c367800915c803ad4cf1c5b80e9a2e91d80cae51b8a9531144`
