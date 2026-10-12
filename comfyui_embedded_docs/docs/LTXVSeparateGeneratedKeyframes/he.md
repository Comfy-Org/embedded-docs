# LTXVSeparateGeneratedKeyframes

## סקירה כללית

הצומת LTXV Separate Generated Keyframes מחלץ בחזרה מתוך latent שנדגם את ה-keyframes שנוצרו, שהוספו על ידי LTXV Add Generated Keyframes, ומסיר אותם מהקונדישינינג. השתמש בו לפני הגדלה מרחבית של latent הווידאו. אל תריץ תחילה את LTXV Crop Guides — הוא מתייחס ל-keyframes שנוצרו כמדריכים חד-פעמיים ומוחק אותם.

## קלטים

| פרמטר | תיאור | סוג נתונים | נדרש | טווח |
|-----------|-------------|-----------|----------|-------|
| `positive` | קונדישינינג חיובי שמכיל את מטא-הנתונים של generated-keyframe. המטא-נתונים מוסרים ממנו בפלט. | CONDITIONING | כן | N/A |
| `negative` | קונדישינינג שלילי שמכיל את מטא-הנתונים של generated-keyframe. המטא-נתונים מוסרים ממנו בפלט. | CONDITIONING | כן | N/A |
| `latent` | latent וידאו שמכיל את ה-keyframes שנוצרו. ה-keyframes מוסרים ממנו בפלט. | LATENT | כן | N/A |
| `keyframes_to_batch` | מחזיר את ה-keyframes כאצווה של latents חד-פריימיים. השאר כבוי כדי לקבל אותם כ-latent רב-פריימי יחיד, וזה מה שה-latent upsampler ו-Add Generated Keyframes מאוחר יותר מצפים לו. | BOOLEAN | לא | default: False |

### הערות על הקלטים

- `positive` חייב להכיל מטא-נתונים של generated-keyframe, אחרת הצומת מעלה שגיאה שאומרת לך להוסיף אותם קודם עם LTXV Add Generated Keyframes.
- `latent` חייב להיות latent וידאו פשוט (טנזור 5D). אם ה-latents של וידאו ואודיו עדיין משולבים, פצל אותם תחילה עם Separate AV Latent.
- מספר הטוקנים לכל פריים latent שנרשמו בעת הוספת ה-keyframes חייב להתאים למספר הטוקנים לכל פריים של ה-`latent` שסופק. אם ה-latent שונה בקנה מידה לאחר הוספת ה-keyframes, הם כבר לא מתיישרים והצומת מעלה שגיאה — הפרד אותם לפני הגדלת ה-latent.
- טווח הפריימים של ה-keyframes שנרשם חייב להיכנס בתוך ה-`latent` שסופק, אחרת הצומת מעלה שגיאה שה-keyframes נרשמו כנגד latent אחר.
- אינדקס רשומת ה-guide attention שנרשם חייב עדיין להתקיים בקונדישינינג. אם הקונדישינינג נבנה מחדש לאחר הוספת ה-keyframes, הצומת מעלה שגיאה.

## פלטים

| שם פלט | תיאור | סוג נתונים |
|-------------|-------------|-----------|
| `positive` | קונדישינינג חיובי עם מטא-נתוני generated-keyframe שהוסרו. | CONDITIONING |
| `negative` | קונדישינינג שלילי עם מטא-נתוני generated-keyframe שהוסרו. | CONDITIONING |
| `latent` | latent וידאו עם ה-keyframes שנוצרו שהוסרו. | LATENT |
| `keyframes` | ה-keyframes שהופרדו, מסומנים עם generated_keyframe_indices ו-generated_keyframe_num_frames. הזן אותם ל-Add Generated Keyframes מאוחר יותר כדי לאתחל חריצים חדשים, או ל-Generated Keyframes To Guides כדי להצמיד אותם כמדריכי תמונה קפואים (האינדקסים ממופים מחדש אם אורך הקנבס השתנה). | LATENT |

## הערות

- הפרמטר `keyframes_to_batch` קובע אם ה-keyframes מוחזרים כאצווה של latents חד-פריימיים או כ-latent רב-פריימי יחיד.
- הצומת מבטיח שה-keyframes שנוצרו מוסרים מהקונדישינינג ומה-latent לפני כל עיבוד נוסף.
- ניתן להשתמש בפלט `keyframes` כדי לאתחל חריצים חדשים עבור keyframes שנוצרו או כדי להצמיד אותם כמדריכי תמונה קפואים.
- הצומת מעלה `ValueError` אם ה-latent אינו מכיל keyframes שנוצרו או אם ה-keyframes אינם תואמים לפורמט הצפוי.
- הצומת מניח שה-keyframes שנוצרו נוספו באמצעות הצומת LTXV Add Generated Keyframes ושהם תואמים ל-latent הנוכחי.

> מסמך זה נוצר על ידי בינה מלאכותית. אם מצאתם שגיאות או שיש לכם הצעות לשיפור, אתם מוזמנים לתרום! [עריכה ב-GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVSeparateGeneratedKeyframes/he.md)

---
**Source fingerprint (SHA-256):** `295e49181e87445a1c47b2e9413d95b20585b12e89f26f13129ac5d97f913007`
