# MoonvalleyVideo2VideoNode

צומת Moonvalley Marey Video to Video ממיר וידאו קלט לוידאו חדש על בסיס תיאור טקסט. הוא משתמש ב-Moonvalley API כדי ליצור וידאו שתואם לפרומפט שלך תוך שמירה על מאפייני תנועה או תנוחה מהווידאו המקורי. ניתן לשלוט בסגנון ובתוכן של וידאו הפלט באמצעות פרומפטים טקסטואליים ופרמטרי יצירה שונים.

## קלטים

| פרמטר | תיאור | סוג נתונים | נדרש | טווח |
| --- | --- | --- | --- | --- |
| `prompt` | מתאר את הווידאו שיש ליצור (קלט מרובה שורות) | STRING | כן | - |
| `negative_prompt` | טקסט פרומפט שלילי (ברירת מחדל: רשימה ארוכה של מתארים שליליים) | STRING | לא | - |
| `seed` | ערך זרע אקראי (ברירת מחדל: 9) | INT | כן | 0 to 4294967295 |
| `video` | וידאו העזר המשמש ליצירת וידאו הפלט. חייב להיות באורך של לפחות 5 שניות. וידאו ארוך מ-5 שניות ייחתך אוטומטית. נתמך רק בפורמט MP4. | VIDEO | כן | - |
| `control_type` | בחירת סוג שליטה (ברירת מחדל: "Motion Transfer") | COMBO | לא | "Motion Transfer"<br>"Pose Transfer" |
| `motion_intensity` | משמש רק אם control_type הוא "Motion Transfer" (ברירת מחדל: 100) | INT | לא | 0 to 100 |
| `steps` | מספר שלבי הסקה (ברירת מחדל: 33) | INT | כן | 1 to 100 |

**הערה:** הפרמטר `motion_intensity` מוחל רק כאשר `control_type` מוגדר ל-"Motion Transfer". כאשר משתמשים ב-"Pose Transfer", פרמטר זה לא נלקח בחשבון.

## פלטים

| שם פלט | תיאור | סוג נתונים |
| --- | --- | --- |
| `output` | פלט הווידאו שנוצר | VIDEO |

> מסמך זה נוצר על ידי בינה מלאכותית. אם מצאתם שגיאות או שיש לכם הצעות לשיפור, אתם מוזמנים לתרום! [עריכה ב-GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoonvalleyVideo2VideoNode/he.md)

---
**Source fingerprint (SHA-256):** `8202a4be469afa16d77b9e0287c290b9c3f390347fc60f23878f50fd95a758e0`
