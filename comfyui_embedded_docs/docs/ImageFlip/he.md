# היפוך תמונה

צומת ImageFlip הופך תמונות לאורך צירים שונים. הוא יכול להפוך תמונות אנכית לאורך ציר ה-x או אופקית לאורך ציר ה-y. הצומת משתמש בפעולות torch.flip כדי לבצע את ההיפוך בהתאם לשיטה הנבחרת.

## קלטים

| פרמטר | תיאור | סוג נתון | חובה | טווח |
| --- | --- | --- | --- | --- |
| `image` | תמונת הקלט שיש להפוך | IMAGE | כן | - |
| `flip_method` | כיוון ההיפוך להחלה (ברירת מחדל: "x-axis: vertically") | STRING | כן | "x-axis: vertically"<br>"y-axis: horizontally" |

## פלטים

| שם פלט | תיאור | סוג נתון |
| --- | --- | --- |
| `image` | תמונת הפלט לאחר ההיפוך | IMAGE |

> מסמך זה נוצר על ידי בינה מלאכותית. אם מצאתם שגיאות או שיש לכם הצעות לשיפור, אתם מוזמנים לתרום! [עריכה ב-GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageFlip/he.md)

---
**Source fingerprint (SHA-256):** `481cd167d57746f242fcc4b5f2e3bb0bff0184b5870626d5f24a34422464ddd6`
