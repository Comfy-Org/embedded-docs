# HeyGen Voice 1.0 Instant Clone

שכפול קול מהקלטה של דובר אחד באמצעות מנוע Voice 1.0 של HeyGen. הצומת מעלה את ההקלטה, יוצר שכפול קול מיידי, ממתין עד ש-HeyGen מסיים לעבד אותה, ומחזיר את `voice_id`. חברו אותו לצומת HeyGen Voice 1.0 Text to Speech, או ל-`custom_voice_id` בצמתים HeyGen Avatar Video ו-HeyGen Talking Photo. יצירת השכפול היא בחינם; החיוב הוא עבור הדיבור שתייצרו באמצעות הקול.

**הערה:** צומת זה מסומן כמיושן בקוד המקור. השתמשו ב-HeyGen Voice 1.0 Instant Clone Text to Speech כדי לשבט קול ולהקריא טקסט בצומת אחד.

## קלטים

| פרמטר | תיאור | סוג נתונים | חובה | טווח |
|-----------|-------------|-----------|----------|-------|
| `audio` | הקלטה של דובר אחד. השתמשו בלפחות 10 שניות של דיבור ברור; רק 3 הדקות הראשונות משמשות. | AUDIO | כן | N/A |
| `language` | השפה המדוברת בהקלטה (ברירת מחדל: "auto"). | COMBO | כן | `"auto"`<br>פריסטים מרובים של שפות |
| `similarity` | עד כמה הקול נצמד להקלטה (ברירת מחדל: "max"). | COMBO | כן | `"medium"`<br>`"high"`<br>`"extra_high"`<br>`"max"` |
| `remove_background_noise` | ניקוי רעשי רקע בהקלטה לפני השכפול (ברירת מחדל: True). | BOOLEAN | כן | True<br>False |
| `seed` | שנו את ה-seed כדי לשכפל את ההקלטה שוב; כל שכפול הוא קול מעט שונה (ברירת מחדל: 42). | INT | כן | 0 עד 2147483647 |

**הערה:** הקול נוצר בשם "ComfyUI Voice" בחשבון ה-HeyGen שלכם, וה-`voice_id` מופיע בפלט של הצומת, לכן חברו צומת תצוגת טקסט כדי לקרוא אותו. השאירו את `language` על "auto" אלא אם הדובר מדבר בשפה שקל להתבלבל בינה לבין שפה קרובה אליה. קלט ה-`seed` כולל פקד קבוע של Control After Generate בממשק, ולכן שנו אותו ידנית כאשר תרצו שכפול נוסף.

## פלטים

| שם פלט | תיאור | סוג נתונים |
|-------------|-------------|-----------|
| `voice_id` | המזהה של הקול המשוכפל, לשימוש חוזר בצומת HeyGen Voice 1.0 Text to Speech או כ-`custom_voice_id`. | STRING |

> מסמך זה נוצר על ידי בינה מלאכותית. אם מצאתם שגיאות או שיש לכם הצעות לשיפור, אתם מוזמנים לתרום! [עריכה ב-GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenVoiceCloneNode/he.md)

---
**Source fingerprint (SHA-256):** `a44924942311ca520e8d77d89119cb56c1b8030124ce608ae89efd72a0e2ad28`
