# Breeze Text to Speech

ממיר טקסט לדיבור באמצעות Breeze TTS 2. בחרו קול Breeze, בחרו את שפת הטקסט, ובאופן אופציונלי כוונו כיצד השורה מבוצעת. English ו-Chinese יכולות להשתמש בכל אחד משני המודלים של Breeze TTS 2; כל שפה אחרת משתמשת ב-Breeze TTS 2 Multilingual.

## קלטים

### קלטים משותפים

| פרמטר | תיאור | סוג נתונים | חובה | טווח |
| --- | --- | --- | --- | --- |
| `voice` | קול Breeze לדיבור, מתוך Breeze Voice Selector או מאחד מצמתי יצירת הקול של Breeze. | BREEZE_VOICE | כן | - |
| `text` | טקסט לדיבור, 1 עד 1000 תווים. תגי אודיו כגון `(laughs)` או `(sighs)` מבוצעים במקום להיקרא. ברירת מחדל: ריק. | STRING | כן | 1 עד 1000 תווים |
| `language` | שפת הטקסט. English ו-Chinese יכולות להשתמש בכל אחד מהמודלים; שפות אחרות משתמשות ב-Breeze TTS 2 Multilingual. קול נשמע במיטבו בשפתו שלו, לכן עבור שפה אחרת השתמשו בעותק שנוצר עם Breeze Voice Localize. | DYNAMIC_COMBO | כן | אפשרויות מרובות זמינות |
| `delivery` | כיצד השורה מבוצעת: `neutral` משאיר את הקול כפי שהוא, `directed` פועל לפי הוראות כתובות. ברירת מחדל: `"neutral"`. | DYNAMIC_COMBO | כן | `"neutral"`<br>`"directed"` |
| `speed` | מכפיל קצב שמשאיר את גובה הצליל ללא שינוי. ברירת מחדל: 1.0. | FLOAT | לא | 0.5 עד 2.0 (צעד 0.05) |
| `seed` | שולט אם הצומת תרוץ מחדש; התוצאות אינן דטרמיניסטיות ללא תלות ב-seed. ברירת מחדל: 42. | INT | לא | 0 עד 2147483647 |

### קלטים עבור השפות "English" ו-"Chinese"

הם מופיעים רק כאשר `language` הוא English או Chinese.

| פרמטר | תיאור | סוג נתונים | חובה | טווח |
| --- | --- | --- | --- | --- |
| `model` | `Breeze TTS 2` או `Breeze TTS 2 Multilingual`. ברירת מחדל: `"Breeze TTS 2"`. | COMBO | כן | `"Breeze TTS 2"`<br>`"Breeze TTS 2 Multilingual"` |

### קלטים עבור delivery "neutral"

| פרמטר | תיאור | סוג נתונים | חובה | טווח |
| --- | --- | --- | --- | --- |
| `speaker_boost` | שומר על הקול קרוב יותר לצליל המקורי שלו. ברירת מחדל: false. | BOOLEAN | לא | true<br>false |

### קלטים עבור delivery "directed"

| פרמטר | תיאור | סוג נתונים | חובה | טווח |
| --- | --- | --- | --- | --- |
| `instructions` | כיצד לבצע את הטקסט, בכתיבה באותה שפה כמו הטקסט. ברירת מחדל: ריק. | STRING | לא | טקסט רב-שורתי |
| `strength` | כמה חזק הקול פועל לפי ההוראות. ברירת מחדל: 4.0. | FLOAT | לא | 1.0 עד 10.0 (צעד 0.1) |

## פלטים

| שם פלט | תיאור | סוג נתונים |
| --- | --- | --- |
| `audio` | הדיבור שנוצר כקובץ אודיו WAV. | AUDIO |

> מסמך זה נוצר על ידי בינה מלאכותית. אם מצאתם שגיאות או שיש לכם הצעות לשיפור, אתם מוזמנים לתרום! [עריכה ב-GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BreezeTextToSpeech/he.md)

---
**Source fingerprint (SHA-256):** `e5e5201e8c951a878ef9e764db31e494285ddded6ec66d8e818ec132342bbe5c`
