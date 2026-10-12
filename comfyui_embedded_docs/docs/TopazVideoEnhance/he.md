# Topaz שיפור וידאו (מורשת)

צומת Topaz Video Enhance מפיח חיים חדשים בווידאו עם טכנולוגיית הגדלת רזולוציה ושחזור עוצמתית, תוך שימוש ב-API חיצוני לשיפור איכות הווידאו. הוא יכול להגדיל את רזולוציית הווידאו, להעלות את קצב הפריימים באמצעות אינטרפולציה ולהחיל דחיסה. הצומת מעבד וידאו MP4 כקלט ומחזיר גרסה משופרת בהתאם להגדרות שנבחרו. צומת זה מסומן כמיושן (legacy).

## קלטים

| פרמטר | תיאור | סוג נתונים | חובה | טווח |
|-----------|-------------|-----------|----------|-------|
| `video` | קובץ הווידאו הקלט שיש לשפר. | VIDEO | כן | - |
| `upscaler_enabled` | מפעיל או מבטל את תכונת הגדלת הרזולוציה של הווידאו (ברירת מחדל: True). | BOOLEAN | כן | - |
| `upscaler_model` | מודל ה-AI המשמש להגדלת הרזולוציה של הווידאו. | COMBO | כן | `"Starlight (Astra) Fast"`<br>`"Starlight (Astra) Creative"`<br>`"Starlight Precise 2.5"` |
| `upscaler_resolution` | רזולוציית היעד עבור הווידאו המוגדל. | COMBO | כן | `"FullHD (1080p)"`<br>`"4K (2160p)"` |
| `upscaler_creativity` | רמת יצירתיות (חלה רק על Starlight (Astra) Creative). (ברירת מחדל: "low") | COMBO | לא | `"low"`<br>`"middle"`<br>`"high"` |
| `interpolation_enabled` | מפעיל או מבטל את תכונת אינטרפולציית הפריימים (ברירת מחדל: False). | BOOLEAN | לא | - |
| `interpolation_model` | המודל המשמש לאינטרפולציית פריימים (ברירת מחדל: "apo-8"). | COMBO | לא | `"apo-8"` |
| `interpolation_slowmo` | מקדם הילוך איטי המוחל על וידאו הקלט. לדוגמה, 2 הופך את הפלט לאיטי פי שניים ומכפיל את משך הזמן. (ברירת מחדל: 1) | INT | לא | 1 עד 16 |
| `interpolation_frame_rate` | קצב פריימים בפלט. (ברירת מחדל: 60) | INT | לא | 15 עד 240 |
| `interpolation_duplicate` | מנתח את הקלט לאיתור פריימים כפולים ומסיר אותם. (ברירת מחדל: False) | BOOLEAN | לא | - |
| `interpolation_duplicate_threshold` | רגישות זיהוי לפריימים כפולים. (ברירת מחדל: 0.01) | FLOAT | לא | 0.001 עד 0.1 |
| `dynamic_compression_level` | רמת CQP. (ברירת מחדל: "Low") | COMBO | לא | `"Low"`<br>`"Mid"`<br>`"High"` |

**הערה:** יש להפעיל לפחות תכונת שיפור אחת. הצומת יפיק שגיאה אם גם `upscaler_enabled` וגם `interpolation_enabled` מוגדרים ל-False. וידאו הקלט חייב להיות בפורמט MP4. ההגדרה `upscaler_creativity` חלה רק כאשר `upscaler_model` מוגדר ל-"Starlight (Astra) Creative". קבצי וידאו גדולים מאוד הדורשים העלאה מרובת חלקים אינם נתמכים.

## פלטים

| שם פלט | תיאור | סוג נתונים |
|-------------|-------------|-----------|
| `video` | קובץ הווידאו המשופר בפלט. | VIDEO |

> מסמך זה נוצר על ידי בינה מלאכותית. אם מצאתם שגיאות או שיש לכם הצעות לשיפור, אתם מוזמנים לתרום! [עריכה ב-GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TopazVideoEnhance/he.md)

---
**Source fingerprint (SHA-256):** `b3b14a301b529256ddf04b7e3a9b99814ad5bfa149366b2a5c51c396dbffb190`
