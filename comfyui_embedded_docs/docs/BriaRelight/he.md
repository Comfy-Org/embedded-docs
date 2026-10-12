# Bria שינוי תאורה

צומת זה משנה את אווירת התאורה ואת כיוונה של תמונה באמצעות Bria. התמונה מרונדרת מחדש על ידי Bria, כך שהתוצאה אינה מיושרת ברמת הפיקסל לקלט; כל הפריים נוצר מחדש ברזולוציה של כמיגה-פיקסל אחד.

## קלטים

### קלטים משותפים

| פרמטר | תיאור | סוג נתונים | נדרש | טווח |
|-----------|-------------|-----------|----------|-------|
| `image` | התמונה שאת התאורה שלה משנים. כל ערוץ אלפא נשמט לפני העלאת התמונה. | IMAGE | כן | - |
| `light_type` | אווירת התאורה להחלה. | COMBO | כן | `"midday"`<br>`"blue hour light"`<br>`"low-angle sunlight"`<br>`"sunrise light"`<br>`"spotlight on subject"`<br>`"overcast light"`<br>`"soft overcast daylight lighting"`<br>`"cloud-filtered lighting"`<br>`"fog-diffused lighting"`<br>`"moonlight lighting"`<br>`"starlight nighttime"`<br>`"soft bokeh lighting"`<br>`"harsh studio lighting"` |
| `light_direction` | מאיפה מגיע האור. אווירות של תאורה קשה כגון midday, spotlight on subject ו-harsh studio lighting מגיבות לכך יותר מכל. | COMBO | כן | `"front"`<br>`"side"`<br>`"bottom"`<br>`"top-down"` |
| `moderation` | הגדרות מודרציה. בחר `"true"` כדי לחשוף את אפשרויות המודרציה, או `"false"` כדי לפעול בלעדיהן. | DYNAMIC_COMBO | כן | `"false"`<br>`"true"` |

### קלטי מודרציה

אפשרויות אלו מופיעות כאשר `moderation` מוגדר ל-`"true"`.

| פרמטר | תיאור | סוג נתונים | נדרש | טווח |
|-----------|-------------|-----------|----------|-------|
| `visual_input_moderation` | מפעיל מודרציית תוכן על תמונת הקלט. ברירת מחדל: false. | BOOLEAN | לא | `true`<br>`false` |
| `visual_output_moderation` | מפעיל מודרציית תוכן על תמונת הפלט שנוצרה. ברירת מחדל: false. | BOOLEAN | לא | `true`<br>`false` |

הערה: Bria מרנדרת מחדש את כל הפריים ברזולוציה של כמיגה-פיקסל אחד, כך שהתוצאה אינה מיושרת ברמת הפיקסל לקלט.

## פלטים

| שם פלט | תיאור | סוג נתונים |
|-------------|-------------|-----------|
| `image` | התמונה עם התאורה החדשה שהוחזרה על ידי Bria. | IMAGE |
| `structured_prompt` | תיאור מובנה של התמונה הערוכה, לעריכה נוספת עם Bria FIBO Image Edit. | STRING |

> מסמך זה נוצר על ידי בינה מלאכותית. אם מצאתם שגיאות או שיש לכם הצעות לשיפור, אתם מוזמנים לתרום! [עריכה ב-GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaRelight/he.md)

---
**Source fingerprint (SHA-256):** `21fbe2186c99a7e8d99d5659ac25c3ab1a757492916dba4135487d4b293cb4f6`
