# Pikaffects

הצומת Pikaffects מייצר סרטונים עם אפקטים חזותיים שונים המוחלים על תמונת קלט. הוא משתמש ב-API ליצירת סרטונים של Pika כדי להמיר תמונות סטטיות לסרטונים מונפשים עם אפקטים ספציפיים כגון המסה, פיצוץ או ריחוף. הצומת דורש מפתח API ואסימון אימות כדי לגשת לשירות Pika.

## קלטים

| פרמטר | תיאור | סוג נתונים | נדרש | טווח |
| --- | --- | --- | --- | --- |
| `image` | תמונת העזר שעליה להחיל את ה-Pikaffect. | IMAGE | כן | - |
| `pikaffect` | האפקט החזותי הספציפי להחלה על התמונה (ברירת מחדל: "Cake-ify"). | COMBO | כן | "Cake-ify"<br>"Crumble"<br>"Crush"<br>"Decapitate"<br>"Deflate"<br>"Dissolve"<br>"Explode"<br>"Eye-pop"<br>"Inflate"<br>"Levitate"<br>"Melt"<br>"Peel"<br>"Poke"<br>"Squish"<br>"Ta-da"<br>"Tear" |
| `prompt_text` | תיאור טקסטואלי המנחה את יצירת הסרטון. | STRING | כן | - |
| `negative_prompt` | תיאור טקסטואלי של מה שיש להימנע ממנו בסרטון הנוצר. | STRING | כן | - |
| `seed` | ערך seed אקראי לתוצאות הניתנות לשחזור. | INT | כן | 0 עד 4294967295 |

## פלטים

| שם פלט | תיאור | סוג נתונים |
| --- | --- | --- |
| `output` | הסרטון שנוצר עם ה-Pikaffect המוחל. | VIDEO |

> מסמך זה נוצר על ידי בינה מלאכותית. אם מצאתם שגיאות או שיש לכם הצעות לשיפור, אתם מוזמנים לתרום! [עריכה ב-GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Pikaffects/he.md)

---
**Source fingerprint (SHA-256):** `68ebbee465763d463bf73678254eed38d37ebacb1c62d386bbe66961deffd5a8`
