# התניה (שרשור)

הצומת ConditioningConcat מיועד לשרשר וקטורי התניה, ובאופן ספציפי למזג את וקטור 'conditioning_from' לתוך וקטור 'conditioning_to'. פעולה זו חיונית בתרחישים שבהם יש לשלב מידע התניה משני מקורות לייצוג מאוחד אחד.

## קלטים

| פרמטר | תיאור | סוג נתונים ב-Comfy |
| --- | --- | --- |
| `conditioning_to` | מייצג את קבוצת וקטורי התניה הראשית שאליה ישורשרו וקטורי 'conditioning_from'. הוא משמש כבסיס לתהליך השרשור. | `CONDITIONING` |
| `conditioning_from` | מורכב מוקטורי התניה שיש לשרשר אל וקטורי 'conditioning_to'. פרמטר זה מאפשר לשלב מידע התניה נוסף לתוך הקבוצה הקיימת. | `CONDITIONING` |

## פלטים

| פרמטר | תיאור | סוג נתונים ב-Comfy |
| --- | --- | --- |
| `conditioning` | הפלט הוא קבוצה מאוחדת של וקטורי התניה, כתוצאה משרשור וקטורי 'conditioning_from' לתוך וקטורי 'conditioning_to'. | `CONDITIONING` |

> מסמך זה נוצר על ידי בינה מלאכותית. אם מצאתם שגיאות או שיש לכם הצעות לשיפור, אתם מוזמנים לתרום! [עריכה ב-GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningConcat/he.md)
