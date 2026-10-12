# MergeTextLists

This node merges multiple text lists into a single, combined list. It is designed to receive text inputs as lists and concatenates them together. The node logs the total number of texts in the merged list.

## קלטים

| פרמטר | תיאור | סוג נתונים | נדרש | טווח |
| --- | --- | --- | --- | --- |
| `texts` | רשימות הטקסט שיש למזג. ניתן לחבר מספר רשימות לקלט, והן ישורשרו לרשימה אחת. | STRING | כן | N/A |

**הערה:** צומת זה מוגדר כתהליך קבוצתי (`is_group_process = True`), כלומר הוא מטפל אוטומטית במספר קלטי רשימות על ידי שרשורם יחד לפני שפונקציית העיבוד הראשית פועלת.

**הערה:** צומת זה מיושן והוחלף על ידי צומת Create List.

## פלטים

| שם פלט | תיאור | סוג נתונים |
| --- | --- | --- |
| `texts` | הרשימה הממוזגת היחידה המכילה את כל טקסטי הקלט. | STRING |

> מסמך זה נוצר על ידי בינה מלאכותית. אם מצאתם שגיאות או שיש לכם הצעות לשיפור, אתם מוזמנים לתרום! [עריכה ב-GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MergeTextLists/he.md)

---
**Source fingerprint (SHA-256):** `bb7f45725c2c41a18d8cd3040d093c11be2ceb03cf1849385aa55d12fd9eb555`
