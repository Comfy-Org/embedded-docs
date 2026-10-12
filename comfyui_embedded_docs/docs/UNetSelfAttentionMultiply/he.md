# UNetSelfAttentionMultiply

צומת UNetSelfAttentionMultiply מחיל מקדמי הכפלה על רכיבי ה-query, ה-key, ה-value וה-output של מנגנון ה-self-attention במודל UNet. הוא מאפשר לך לשנות את הקנה המידה של חלקים שונים בחישוב ה-attention כדי להתנסות באופן שבו משקולות ה-attention משפיעות על התנהגות המודל.

## קלטים

| פרמטר | תיאור | סוג נתון | חובה | טווח |
| --- | --- | --- | --- | --- |
| `model` | מודל ה-UNet שיש לשנות באמצעות מקדמי שינוי קנה מידה של ה-attention | MODEL | כן | - |
| `q` | מקדם הכפלה עבור רכיב ה-query (ברירת מחדל: 1.0) | FLOAT | לא | 0.0 - 10.0 |
| `k` | מקדם הכפלה עבור רכיב ה-key (ברירת מחדל: 1.0) | FLOAT | לא | 0.0 - 10.0 |
| `v` | מקדם הכפלה עבור רכיב ה-value (ברירת מחדל: 1.0) | FLOAT | לא | 0.0 - 10.0 |
| `out` | מקדם הכפלה עבור רכיב ה-output (ברירת מחדל: 1.0) | FLOAT | לא | 0.0 - 10.0 |

## פלטים

| שם פלט | תיאור | סוג נתון |
| --- | --- | --- |
| `MODEL` | מודל ה-UNet שהשתנה, עם רכיבי attention בקנה מידה מותאם | MODEL |

> מסמך זה נוצר על ידי בינה מלאכותית. אם מצאתם שגיאות או שיש לכם הצעות לשיפור, אתם מוזמנים לתרום! [עריכה ב-GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/UNetSelfAttentionMultiply/he.md)

---
**Source fingerprint (SHA-256):** `7a6039eb2faae56437a5eb6fe01be6d38e53c0632175a3405a1e24a476d4da82`
