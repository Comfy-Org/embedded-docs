# איפוס התניה

צומת זה מאפס רכיבים ספציפיים בתוך מבנה הנתונים של ה-conditioning, ובכך מנטרל למעשה את השפעתם בשלבי העיבוד הבאים. הוא מיועד לפעולות conditioning מתקדמות שבהן נדרשת מניפולציה ישירה של הייצוג הפנימי של ה-conditioning.

## קלטים

| פרמטר | תיאור | Comfy dtype |
| --- | --- | --- |
| `CONDITIONING` | מבנה הנתונים של ה-conditioning שיש לשנות. צומת זה מאפס את רכיבי 'pooled_output' בכל רשומת conditioning, אם קיימים. | CONDITIONING |

## פלטים

| פרמטר | תיאור | Comfy dtype |
| --- | --- | --- |
| `CONDITIONING` | מבנה הנתונים של ה-conditioning לאחר השינוי, כאשר רכיבי 'pooled_output' מוגדרים לאפס במקומות הרלוונטיים. | CONDITIONING |

> מסמך זה נוצר על ידי בינה מלאכותית. אם מצאתם שגיאות או שיש לכם הצעות לשיפור, אתם מוזמנים לתרום! [עריכה ב-GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningZeroOut/he.md)
