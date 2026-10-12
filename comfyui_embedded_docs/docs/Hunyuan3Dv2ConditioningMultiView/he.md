# Hunyuan3Dv2ConditioningMultiView

הצומת Hunyuan3Dv2ConditioningMultiView משלב פלטי CLIP vision של עד ארבעה מבטים (front, left, back, right) להתניה רב-מבטית יחידה. כל מבט שסופק מקבל קידוד מיקומי שמוסף להטמעת ה-CLIP vision שלו, וההטמעות המתקבלות משורשרות זו לזו. הצומת מפיק התניה חיובית המבוססת על ההטמעות המשולבות והתניה שלילית מלאה באפסים באותה צורה.

## קלטים

| פרמטר | תיאור | סוג נתונים | נדרש | טווח |
| --- | --- | --- | --- | --- |
| `front` | פלט CLIP vision עבור המבט הקדמי. קלט מבט אופציונלי. | CLIP_VISION_OUTPUT | לא | - |
| `left` | פלט CLIP vision עבור המבט השמאלי. קלט מבט אופציונלי. | CLIP_VISION_OUTPUT | לא | - |
| `back` | פלט CLIP vision עבור המבט האחורי. קלט מבט אופציונלי. | CLIP_VISION_OUTPUT | לא | - |
| `right` | פלט CLIP vision עבור המבט הימני. קלט מבט אופציונלי. | CLIP_VISION_OUTPUT | לא | - |

**הערה:** יש לספק לפחות קלט מבט אחד כדי שהצומת יפעל. הצומת מעבד רק מבטים שמכילים נתוני פלט תקינים של CLIP vision ומדלג על מבטים שאינם מחוברים. כל מבט מקבל קידוד מיקומי קבוע בהתאם לחריץ שלו (front, left, back, right), וההטמעות המעובדות מכל המבטים שסופקו מחוברות יחד לאורך ממד הרצף.

## פלטים

| שם פלט | תיאור | סוג נתונים |
| --- | --- | --- |
| `positive` | התניה חיובית המכילה את ההטמעות הרב-מבטיות המשולבות עם קידוד מיקומי. | CONDITIONING |
| `negative` | התניה שלילית עם ערכי אפס התואמים לצורת ההתניה החיובית. | CONDITIONING |

> מסמך זה נוצר על ידי בינה מלאכותית. אם מצאתם שגיאות או שיש לכם הצעות לשיפור, אתם מוזמנים לתרום! [עריכה ב-GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Hunyuan3Dv2ConditioningMultiView/he.md)

---
**Source fingerprint (SHA-256):** `1492b51661d0bb8f2c142c1b1e8ef104beed1b9dae532a970e2928e27ad71d69`
