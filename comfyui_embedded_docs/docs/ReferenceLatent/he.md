# ReferenceLatent

צומת זה מגדיר את ה-latent המנחה עבור מודל עריכה. הוא מקבל נתוני conditioning וקלט latent אופציונלי, ואז משנה את ה-conditioning כך שיכלול מידע latent של עזר. אם המודל תומך בכך, ניתן לשרשר מספר צמתי Set Reference Latent כדי להגדיר מספר תמונות עזר.

## קלטים

| פרמטר | תיאור | סוג נתונים | חובה | טווח |
| --- | --- | --- | --- | --- |
| `conditioning` | נתוני ה-conditioning שיש לשנות כך שיכללו מידע latent של עזר | CONDITIONING | כן | - |
| `latent` | נתוני latent אופציונליים שישמשו כעזר עבור מודל העריכה. אם לא מסופקים, ה-conditioning מוחזר ללא שינוי | LATENT | לא | - |

## פלטים

| שם פלט | תיאור | סוג נתונים |
| --- | --- | --- |
| `output` | נתוני ה-conditioning המשונים המכילים מידע latent של עזר | CONDITIONING |

## הערות

- ה-latent של העזר מאוחסן כרשימה של טנסורי דגימה, ולכן חיבור של מספר צמתי Set Reference Latent ברצף מוסיף הפניות נוספות במקום להחליף את הקודמת.
- כאשר לא מחובר `latent`, הצומת מעביר את ה-`conditioning` הנכנס ללא שינויים.

> מסמך זה נוצר על ידי בינה מלאכותית. אם מצאתם שגיאות או שיש לכם הצעות לשיפור, אתם מוזמנים לתרום! [עריכה ב-GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReferenceLatent/he.md)

---
**Source fingerprint (SHA-256):** `40b02df8ac436480f478fcfa929cc2e13181954507f4bdcd70aade051a25f7d5`
