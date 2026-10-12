# TorchCompileModel

הצומת TorchCompileModel מחיל קומפילציה של PyTorch על מודל כדי למטב את ביצועיו. הוא יוצר עותק של מודל הקלט ועוטף אותו בפונקציונליות הקומפילציה של PyTorch באמצעות מנוע הקומפילציה שצוין. הדבר יכול לשפר את מהירות ההרצה של המודל בזמן הסקה.

## קלטים

| פרמטר | תיאור | סוג נתונים | נדרש | טווח |
| --- | --- | --- | --- | --- |
| `model` | המודל שיש לקמפל ולמטב | MODEL | כן | - |
| `backend` | מנוע הקומפילציה של PyTorch שיש להשתמש בו לאופטימיזציה (ברירת מחדל: "inductor") | STRING | כן | "inductor"<br>"cudagraphs" |

## פלטים

| שם פלט | תיאור | סוג נתונים |
| --- | --- | --- |
| `model` | המודל המקומפל עם קומפילציה של PyTorch שהוחלה עליו | MODEL |

> מסמך זה נוצר על ידי בינה מלאכותית. אם מצאתם שגיאות או שיש לכם הצעות לשיפור, אתם מוזמנים לתרום! [עריכה ב-GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TorchCompileModel/he.md)

---
**Source fingerprint (SHA-256):** `240c6eb84ce2b93fe4d7c04fcf69df571e662f17893a4fd8e721241ea082edc8`
