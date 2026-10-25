# שנה גודל תמונה/מסכה

הצומת Resize Image/Mask מספק מספר שיטות לשינוי הממדים של תמונת קלט או מסכה. הוא יכול לשנות גודל לפי מכפיל, לקבוע ממדים ספציפיים, להתאים לגודל של קלט אחר, או לכוונן לפי מספר פיקסלים, תוך שימוש בשיטות אינטרפולציה שונות לשם איכות.

## קלטים

| פרמטר | תיאור | סוג נתונים | נדרש | טווח |
| --- | --- | --- | --- | --- |
| `input` | התמונה או המסכה שיש לשנות את גודלן. | IMAGE or MASK | כן | N/A |
| `resize_type` | השיטה המשמשת לקביעת הגודל החדש. הפרמטרים הנדרשים משתנים בהתאם לסוג הנבחר. | COMBO | כן | `SCALE_BY`<br>`SCALE_DIMENSIONS`<br>`SCALE_LONGER_DIMENSION`<br>`SCALE_SHORTER_DIMENSION`<br>`SCALE_WIDTH`<br>`SCALE_HEIGHT`<br>`SCALE_TOTAL_PIXELS`<br>`MATCH_SIZE`<br>`SCALE_TO_MULTIPLE` |
| `multiplier` | מקדם שינוי הגודל. נדרש כאשר `resize_type` הוא `SCALE_BY` (ברירת מחדל: 1.00). | FLOAT | לא | 0.01 עד 8.0 |
| `width` | רוחב היעד בפיקסלים. נדרש כאשר `resize_type` הוא `SCALE_DIMENSIONS` או `SCALE_WIDTH` (ברירת מחדל: 512). | INT | לא | 0 עד 8192 |
| `height` | גובה היעד בפיקסלים. נדרש כאשר `resize_type` הוא `SCALE_DIMENSIONS` או `SCALE_HEIGHT` (ברירת מחדל: 512). | INT | לא | 0 עד 8192 |
| `crop` | שיטת החיתוך להחלה כאשר הממדים אינם תואמים את יחס הגובה-רוחב. זמין רק כאשר `resize_type` הוא `SCALE_DIMENSIONS` או `MATCH_SIZE` (ברירת מחדל: "center"). | COMBO | לא | `"disabled"`<br>`"center"` |
| `longer_size` | גודל היעד עבור הצלע הארוכה של התמונה. נדרש כאשר `resize_type` הוא `SCALE_LONGER_DIMENSION` (ברירת מחדל: 512). | INT | לא | 0 עד 8192 |
| `shorter_size` | גודל היעד עבור הצלע הקצרה של התמונה. נדרש כאשר `resize_type` הוא `SCALE_SHORTER_DIMENSION` (ברירת מחדל: 512). | INT | לא | 0 עד 8192 |
| `megapixels` | מספר המגה-פיקסלים הכולל ביעד. נדרש כאשר `resize_type` הוא `SCALE_TOTAL_PIXELS` (ברירת מחדל: 1.0). | FLOAT | לא | 0.01 עד 16.0 |
| `match` | תמונה או מסכה שאליהן יותאמו ממדי הקלט. נדרש כאשר `resize_type` הוא `MATCH_SIZE`. | IMAGE or MASK | לא | N/A |
| `multiple` | המספר שהרוחב והגובה הופכים לברי-חלוקה בו; שימושי ליישור לטנטים (למשל 8 או 64). נדרש כאשר `resize_type` הוא `SCALE_TO_MULTIPLE` (ברירת מחדל: 8). | INT | לא | 1 עד 8192 |
| `scale_method` | אלגוריתם האינטרפולציה המשמש לשינוי הגודל (ברירת מחדל: "area"). | COMBO | כן | `"nearest-exact"`<br>`"bilinear"`<br>`"area"`<br>`"bicubic"`<br>`"lanczos"` |

**הערה:** הפרמטר `crop` זמין ורלוונטי רק כאשר `resize_type` מוגדר ל-`SCALE_DIMENSIONS` או `MATCH_SIZE`. כאשר משתמשים ב-`SCALE_WIDTH` או `SCALE_HEIGHT`, הממד האחר מותאם אוטומטית כדי לשמור על יחס הגובה-רוחב המקורי.

## פלטים

| שם פלט | תיאור | סוג נתונים |
| --- | --- | --- |
| `resized` | התמונה או המסכה לאחר שינוי הגודל, בהתאמה לסוג הנתונים של הקלט. | IMAGE or MASK |

> מסמך זה נוצר על ידי בינה מלאכותית. אם מצאתם שגיאות או שיש לכם הצעות לשיפור, אתם מוזמנים לתרום! [עריכה ב-GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ResizeImageMaskNode/he.md)

---
**Source fingerprint (SHA-256):** `774795dae382b2baf828a1cbd8b860bad2e9c2977f9555d4ea1b282c8f8b0e12`
