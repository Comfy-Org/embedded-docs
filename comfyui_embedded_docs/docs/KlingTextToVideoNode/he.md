# Kling טקסט לווידאו

צומת Kling Text to Video יוצר סרטונים מתיאורי טקסט באמצעות API של Kling ליצירת סרטונים. הוא שולח את ה-prompt וההגדרות (יחס גובה-רוחב, מצב יצירה ו-CFG scale) ל-API, ממתין להשלמת משימת היצירה, ולאחר מכן מחזיר את הסרטון שנוצר יחד עם המזהה ומשך הזמן שלו.

## קלטים

| פרמטר | תיאור | סוג נתונים | חובה | טווח |
|-----------|-------------|-----------|----------|-------|
| `prompt` | פרומפט טקסט חיובי | STRING | כן | מקסימום 2500 תווים |
| `negative_prompt` | פרומפט טקסט שלילי | STRING | לא | מקסימום 2500 תווים |
| `cfg_scale` | ערך קנה מידה של תצורה ששולט עד כמה הסרטון עוקב אחרי הפרומפט (ברירת מחדל: 1.0) | FLOAT | לא | 0.0 עד 1.0 |
| `aspect_ratio` | הגדרת יחס הגובה-רוחב של הסרטון (ברירת מחדל: "16:9") | COMBO | לא | "16:9"<br>"9:16"<br>"1:1" |
| `mode` | התצורה לשימוש ביצירת הסרטון לפי הפורמט: mode / duration / model_name (ברירת מחדל: "pro mode / 5s duration / kling-v2-5-turbo") | COMBO | לא | "pro mode / 5s duration / kling-v2-5-turbo"<br>"pro mode / 10s duration / kling-v2-5-turbo" |

הערה: הפרמטר `prompt` הוא חובה ואסור שיהיה ריק. גם `prompt` וגם `negative_prompt` מוגבלים למקסימום 2500 תווים. אפשרות ה-`mode` של 10 שניות יקרה יותר מאפשרות 5 השניות.

## פלטים

| שם פלט | תיאור | סוג נתונים |
|-------------|-------------|-----------|
| `output` | פלט הסרטון שנוצר | VIDEO |
| `video_id` | מזהה ייחודי לסרטון שנוצר | STRING |
| `duration` | מידע על משך הסרטון שנוצר | STRING |

> מסמך זה נוצר על ידי בינה מלאכותית. אם מצאתם שגיאות או שיש לכם הצעות לשיפור, אתם מוזמנים לתרום! [עריכה ב-GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingTextToVideoNode/he.md)

---
**Source fingerprint (SHA-256):** `6a63b0b8bc45dc5a6300cdfe7a373399eeead36de6727f7aae2c026ba0deaea8`
