# ComboOptionTestNode

צומת זה מקבל שתי בחירות מתיבות combo ומעביר אותן ישירות אל הפלטים שלו מבלי לשנות אותן.

## קלטים

| פרמטר | תיאור | סוג נתונים | חובה | טווח |
| --- | --- | --- | --- | --- |
| `combo` | הבחירה הראשונה, שנבחרת מתוך קבוצה של שלוש אפשרויות בדיקה. | COMBO | כן | `"option1"`<br>`"option2"`<br>`"option3"` |
| `combo2` | הבחירה השנייה, שנבחרת מתוך קבוצה שונה של שלוש אפשרויות בדיקה. | COMBO | כן | `"option4"`<br>`"option5"`<br>`"option6"` |

## פלטים

| שם פלט | תיאור | סוג נתונים |
| --- | --- | --- |
| `output_1` | מחזיר את הערך שנבחר בתיבת הבחירה הראשונה (`combo`), ללא שינוי. | COMBO |
| `output_2` | מחזיר את הערך שנבחר בתיבת הבחירה השנייה (`combo2`), ללא שינוי. | COMBO |

> מסמך זה נוצר על ידי בינה מלאכותית. אם מצאתם שגיאות או שיש לכם הצעות לשיפור, אתם מוזמנים לתרום! [עריכה ב-GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComboOptionTestNode/he.md)

---
**Source fingerprint (SHA-256):** `fe0b6a35680de55767af2c0d8a293010ddb4c4282cfdde7f9dff7a3a11ff1e5c`
