# HeyGen תרגום וידאו

תרגם סרטון מדובר לשפה אחרת עם שיבוט קול וסנכרון שפתיים. צומת זה משכפל את קולו של הדובר המקורי ומבצע אנימציה מחדש לפה כך שיתאים לדיבור המתורגם, ומייצר תוצאה טבעית למראה.

## קלטים

| פרמטר | תיאור | סוג נתונים | נדרש | טווח |
|-----------|-------------|-----------|----------|-------|
| `video` | סרטון עם דיבור לתרגום. | VIDEO | כן | - |
| `output_language` | שפת היעד עבור הסרטון המתורגם. | COMBO | כן | "Arabic"<br>"Bengali"<br>"Chinese"<br>"Danish"<br>"Dutch"<br>"English"<br>"French"<br>"German"<br>"Greek"<br>"Hindi"<br>"Indonesian"<br>"Italian"<br>"Japanese"<br>"Korean"<br>"Malay"<br>"Polish"<br>"Portuguese"<br>"Russian"<br>"Spanish"<br>"Swedish"<br>"Tamil"<br>"Telugu"<br>"Thai"<br>"Turkish"<br>"Ukrainian"<br>"Vietnamese" |
| `mode` | 'speed' מהיר יותר; 'precision' מפיק סנכרון שפתיים באיכות גבוהה יותר במחיר גבוה יותר. (ברירת מחדל: "speed") | COMBO | כן | "speed"<br>"precision" |
| `translate_audio_only` | החלף רק את רצועת האודיו, תוך שמירה על תנועות הפה המקוריות (ללא סנכרון שפתיים). (ברירת מחדל: False) | BOOLEAN | לא | True<br>False |
| `speaker_count` | מספר הדוברים בסרטון. 0 = זיהוי אוטומטי. ערכים גדולים מ-0 נשלחים ל-API כמספר הדוברים. (ברירת מחדל: 0) | INT | לא | 0 to 10 |
| `seed` | לא נשלח ל-HeyGen; שנה אותו כדי לאלץ הרצה מחדש. (ברירת מחדל: 42) | INT | לא | 0 to 2147483647 |

## פלטים

| שם פלט | תיאור | סוג נתונים |
|-------------|-------------|-----------|
| `video` | הסרטון המתורגם עם שיבוט קול וסנכרון שפתיים מיושמים. | VIDEO |

> מסמך זה נוצר על ידי בינה מלאכותית. אם מצאתם שגיאות או שיש לכם הצעות לשיפור, אתם מוזמנים לתרום! [עריכה ב-GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenVideoTranslateNode/he.md)

---
**Source fingerprint (SHA-256):** `709438c0c713d6db750643cc48f75352c6f293ae1ff2fd82c1bacb03b2581923`
