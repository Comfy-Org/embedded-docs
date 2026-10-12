# Quiver Text ל-SVG

צומת Quiver Text to SVG יוצר תמונת Scalable Vector Graphic (SVG) מתיאור טקסטואלי באמצעות המודלים של Quiver AI. באפשרותך לספק באופן אופציונלי תמונות עזר והוראות סגנון כדי להנחות את תהליך היצירה.

**הערה:** צומת זה מסומן כ-deprecated בקוד המקור.

## קלטים

| פרמטר | תיאור | סוג נתונים | חובה | טווח |
|-----------|-------------|-----------|----------|-------|
| `prompt` | תיאור טקסטואלי של פלט ה-SVG הרצוי. זוהי ההוראה העיקרית למה ליצור. | STRING | כן | N/A |
| `instructions` | הנחיות נוספות לסגנון או לעיצוב. זהו פרמטר אופציונלי ומתקדם. | STRING | לא | N/A |
| `reference_images` | עד 4 תמונות עזר להנחיית היצירה. זהו קלט אופציונלי. | IMAGE | לא | 0 עד 4 תמונות |
| `model` | המודל שיש להשתמש בו ליצירת SVG. בחירת מודל חושפת פרמטרים נוספים הספציפיים לאותו מודל: `temperature`, `top_p`, ו-`presence_penalty`. | DYNAMIC_COMBO | כן | `"arrow-2"`<br>`"arrow-2-telos"`<br>`"arrow-1.1"`<br>`"arrow-1.1-max"`<br>`"arrow-preview"` |
| `seed` | Seed הקובע אם הצומת צריך לרוץ מחדש; התוצאות בפועל אינן דטרמיניסטיות ללא קשר ל-seed. ברירת מחדל: 0. | INT | כן | 0 עד 2147483647 |
| `reasoning_effort` | כמות ההיסק שהמודל משקיע לפני הציור. רמות גבוהות יותר משפרות את הפרטים ועולות ביותר טוקנים. משמש רק את מודלי Arrow 2 (ברירת מחדל: "high"). | COMBO | לא | `"low"`<br>`"medium"`<br>`"high"`<br>`"xhigh"` |

**הערה:** הקלט `reference_images` מקבל מקסימום של 4 תמונות.

## פלטים

| שם פלט | תיאור | סוג נתונים |
|-------------|-------------|-----------|
| `SVG` | תמונת ה-Scalable Vector Graphic (SVG) שנוצרה. | SVG |

> מסמך זה נוצר על ידי בינה מלאכותית. אם מצאתם שגיאות או שיש לכם הצעות לשיפור, אתם מוזמנים לתרום! [עריכה ב-GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QuiverTextToSVGNode/he.md)

---
**Source fingerprint (SHA-256):** `e03e130a4aedbf003e898300b3a83e343fdfa5b3da35df20d55876d437bf5426`
