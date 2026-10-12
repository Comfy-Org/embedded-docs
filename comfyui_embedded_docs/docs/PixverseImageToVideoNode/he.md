# PixverseImageToVideoNode

יוצר וידאו מתמונה נייחת והנחיית טקסט באמצעות PixVerse. הצומת מעלה את תמונת הקלט, מחיל את הגדרות האיכות, משך והתנועה שנבחרו, ולאחר מכן מחזיר את הווידאו שנוצר כשההפקה מסתיימת.

## קלטים

| פרמטר | תיאור | סוג נתונים | נדרש | טווח |
|-----------|-------------|-----------|----------|-------|
| `image` | תמונת קלט להמרה לווידאו | IMAGE | כן | - |
| `prompt` | הנחיה ליצירת הווידאו (ברירת מחדל: מחרוזת ריקה) | STRING | כן | - |
| `quality` | הגדרת איכות הווידאו (ברירת מחדל: res_540p) | COMBO | כן | `res_540p`<br>`res_1080p` |
| `duration_seconds` | משך הווידאו שנוצר בשניות | COMBO | כן | `dur_2`<br>`dur_5`<br>`dur_10` |
| `motion_mode` | סגנון תנועה שמוחל על יצירת הווידאו | COMBO | כן | `normal`<br>`fast`<br>`slow`<br>`zoom_in`<br>`zoom_out`<br>`pan_left`<br>`pan_right`<br>`pan_up`<br>`pan_down`<br>`tilt_up`<br>`tilt_down`<br>`roll_clockwise`<br>`roll_counterclockwise` |
| `seed` | ערך Seed ליצירת הווידאו (ברירת מחדל: 0) | INT | כן | 0-2147483647 |
| `negative_prompt` | תיאור טקסט אופציונלי של אלמנטים לא רצויים בתמונה (ברירת מחדל: מחרוזת ריקה) | STRING | לא | - |
| `pixverse_template` | תבנית אופציונלית להשפעה על סגנון היצירה, שנוצרה על ידי צומת PixVerse Template | CUSTOM | לא | - |

**הערה:** בעת שימוש באיכות 1080p, מצב התנועה מוגדר אוטומטית למצב normal ומשך הזמן מוגבל ל-5 שניות. עבור משכי זמן שאינם 5 שניות, מצב התנועה מוגדר גם הוא אוטומטית למצב normal.

## פלטים

| שם פלט | תיאור | סוג נתונים |
|-------------|-------------|-----------|
| `output` | וידאו שנוצר בהתבסס על תמונת הקלט והפרמטרים | VIDEO |

> מסמך זה נוצר על ידי בינה מלאכותית. אם מצאתם שגיאות או שיש לכם הצעות לשיפור, אתם מוזמנים לתרום! [עריכה ב-GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseImageToVideoNode/he.md)

---
**Source fingerprint (SHA-256):** `93ea662a27159f55bf12e49ea230f0005813614ad07f5189d1fd61e7b937fd4b`
