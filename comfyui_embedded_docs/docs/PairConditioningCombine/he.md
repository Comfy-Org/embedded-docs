# Cond Pair Combine

צומת PairConditioningCombine ממזג שני זוגות התניה נפרדים (כל אחד מהם מורכב מהתניה חיובית ושלילית) לזוג משולב יחיד. הוא מקבל את ההתניה החיובית והשלילית משני מקורות שונים ומשלב ביניהם באמצעות הלוגיקה הפנימית של ComfyUI, ופולט התניה חיובית סופית אחת והתניה שלילית סופית אחת. צומת זה ניסיוני ומיועד לתהליכי עבודה מתקדמים של מניפולציה בהתניה.

## קלטים

| פרמטר | תיאור | סוג נתונים | נדרש | טווח |
| --- | --- | --- | --- | --- |
| `positive_A` | קלט התניה חיובית ראשון | CONDITIONING | כן | - |
| `negative_A` | קלט התניה שלילית ראשון | CONDITIONING | כן | - |
| `positive_B` | קלט התניה חיובית שני | CONDITIONING | כן | - |
| `negative_B` | קלט התניה שלילית שני | CONDITIONING | כן | - |

## פלטים

| שם פלט | תיאור | סוג נתונים |
| --- | --- | --- |
| `positive` | פלט התניה חיובית משולבת | CONDITIONING |
| `negative` | פלט התניה שלילית משולבת | CONDITIONING |

> מסמך זה נוצר על ידי בינה מלאכותית. אם מצאתם שגיאות או שיש לכם הצעות לשיפור, אתם מוזמנים לתרום! [עריכה ב-GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PairConditioningCombine/he.md)

---
**Source fingerprint (SHA-256):** `34c14207930ba31fea054b2e641e9666e738ed786aa117449c4a27667bde41b1`
