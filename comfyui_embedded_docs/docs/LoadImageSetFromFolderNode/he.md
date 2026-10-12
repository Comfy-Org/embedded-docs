# LoadImageSetFromFolderNode

הצומת LoadImageSetFromFolderNode טוען מספר תמונות מתיקייה שצוינה לצורכי אימון. הוא מזהה אוטומטית פורמטי תמונות נפוצים ויכול לשנות את גודל התמונות באופן אופציונלי באמצעות שיטות שונות לפני החזרתן כאצווה.

## קלטים

| פרמטר | תיאור | סוג נתונים | נדרש | טווח |
| --- | --- | --- | --- | --- |
| `folder` | התיקייה שממנה יש לטעון תמונות. | STRING | כן | אפשרויות מרובות זמינות |
| `resize_method` | השיטה לשינוי גודל התמונות (ברירת מחדל: "None"). | STRING | לא | "None"<br>"Stretch"<br>"Crop"<br>"Pad" |

## פלטים

| שם פלט | תיאור | סוג נתונים |
| --- | --- | --- |
| `IMAGE` | האצווה של התמונות שנטענו כטנזור יחיד. | IMAGE |

> מסמך זה נוצר על ידי בינה מלאכותית. אם מצאתם שגיאות או שיש לכם הצעות לשיפור, אתם מוזמנים לתרום! [עריכה ב-GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImageSetFromFolderNode/he.md)

---
**Source fingerprint (SHA-256):** `46fcfbf6a2ad95e707e32e54ed7b4c06bfd1cc290df122042187689f41bed828`
