# Breeze Voice Selector

בוחר קול Breeze מומלץ, או כל מזהה קול Breeze, ומעביר אותו ל-Breeze Text to Speech. הצומת רק מפענח מזהה ואינו מבצע קריאת API.

## קלטים

| פרמטר | תיאור | סוג נתונים | חובה | טווח |
| --- | --- | --- | --- | --- |
| `language` | קבוצת השפה של הקולות המומלצים, או `custom` להזנת מזהה. ברירת מחדל: `"English"`. | DYNAMIC_COMBO | כן | `"English"`<br>`"Chinese"`<br>`"Japanese"`<br>`"custom"` |

### קלטים עבור שפה "English", "Chinese" ו-"Japanese"

| פרמטר | תיאור | סוג נתונים | חובה | טווח |
| --- | --- | --- | --- | --- |
| `voice` | קול מומלץ בשפה זו. | COMBO | כן | אפשרויות מרובות זמינות |

### קלטים עבור שפה "custom"

| פרמטר | תיאור | סוג נתונים | חובה | טווח |
| --- | --- | --- | --- | --- |
| `voice_id` | כל מזהה קול Breeze, כגון קול שנוצר על ידי צמתי Breeze האחרים. אותיות, ספרות, `_` ו-`-` בלבד. ברירת מחדל: ריק. | STRING | כן | מזהה קול Breeze |

## פלטים

| שם פלט | תיאור | סוג נתונים |
| --- | --- | --- |
| `voice` | קול ה-Breeze שנבחר. | BREEZE_VOICE |

> מסמך זה נוצר על ידי בינה מלאכותית. אם מצאתם שגיאות או שיש לכם הצעות לשיפור, אתם מוזמנים לתרום! [עריכה ב-GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BreezeVoiceSelector/he.md)

---
**Source fingerprint (SHA-256):** `0bded8f1b6ec92abaec514ed843b3c138d804e3736758f5df3a2faf52e89a8b0`
