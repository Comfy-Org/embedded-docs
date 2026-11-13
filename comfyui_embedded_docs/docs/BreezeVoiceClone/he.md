# Breeze Voice Clone

יוצר קול Breeze מהקלטה של דובר אחד. הקול נשמר בחשבונך ומוחזר כ-handle של קול, יחד עם תצוגה מקדימה אודיו של איך שהוא נשמע.

## קלטים

| פרמטר | תיאור | סוג נתונים | נדרש | טווח |
| --- | --- | --- | --- | --- |
| `audio` | הקלטה של דובר אחד, באורך של לפחות 3 שניות. רק 60 השניות הראשונות משמשות. | AUDIO | כן | - |
| `remove_background_noise` | מנקה את ההקלטה לפני השיבוט. ברירת מחדל: false. | BOOLEAN | לא | true<br>false |
| `seed` | קובע אם הצומת תרוץ מחדש; התוצאות אינן דטרמיניסטיות ללא תלות ב-seed. ברירת מחדל: 42. | INT | לא | 0 עד 2147483647 |

## פלטים

| שם פלט | תיאור | סוג נתונים |
| --- | --- | --- |
| `voice` | קול ה-Breeze החדש, עבור Breeze Text to Speech. | BREEZE_VOICE |
| `preview` | תצוגה מקדימה אודיו של הקול המשובט. | AUDIO |

> מסמך זה נוצר על ידי בינה מלאכותית. אם מצאתם שגיאות או שיש לכם הצעות לשיפור, אתם מוזמנים לתרום! [עריכה ב-GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BreezeVoiceClone/he.md)

---
**Source fingerprint (SHA-256):** `3c2e461a8e1a38bfa494a687f5b77a375e9e81c77964493181d7c622a682c56f`
