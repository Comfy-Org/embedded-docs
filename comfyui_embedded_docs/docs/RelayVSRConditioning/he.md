# RelayVSRConditioning

RelayVSR Conditioning מכין את הקונדישנינג ואת ה-latent הריק להגדלת וידאו ב-RelayVSR. RelayVSR מריץ את מודל Wan 2.2 החד-שלבי שלו רק על כל פריים 15 בקליפ, ובנוסף על הפריים האחרון, כך שה-latent שהוא מחזיר מכיל רק את פריימי המפתח הללו. לאחר מכן VSR Decode משלים את הפריימים שביניהם.

## קלטים

| פרמטר | תיאור | סוג נתונים | חובה | טווח |
| --- | --- | --- | --- | --- |
| `model` | מודל הדיפוזיה RelayVSR, שנטען באמצעות Load Model: `relayvsr_x2_lightx2v_int8_convrot.safetensors` או `relayvsr_x4_int8_convrot.safetensors`. | MODEL | כן | N/A |
| `images` | הווידאו באיכות נמוכה ברזולוציה המקורית שלו. גורם ההגדלה של המודל קובע את גודל התוצאה. | IMAGE | כן | N/A |

## פלטים

| שם פלט | תיאור | סוג נתונים |
| --- | --- | --- |
| `positive` | קונדישנינג שנושא את פריימי המפתח שנבחרו כהנחיה באיכות נמוכה. | CONDITIONING |
| `latent` | latent ריק עם פריים אחד לכל פריים מפתח, מוכן לסמפלר. | LATENT |

## שימוש

חבר את `positive` לקלט ה-positive של הסמפלר, לאחר מכן בצע סמפול של ה-`latent` בצעד אחד עם CFG 1: אין פרומפט ואין מקודד טקסט בגרף. שלח את הפלט של הסמפלר, את אותם `images` ואת RelayVSR Flash VAE אל VSR Decode, ושמור על התאמה בין הזוג: מודל x2 עם דקודר x2, מודל x4 עם דקודר x4.

רק פריימי מפתח עוברים סמפול, כך שקליפ של 150 פריימים הופך ל-latent של 11 פריימים. הסמפלר עובד על חלק קטן מהווידאו, ו-VSR Decode משחזר את השאר.

> מסמך זה נוצר על ידי בינה מלאכותית. אם מצאתם שגיאות או שיש לכם הצעות לשיפור, אתם מוזמנים לתרום! [עריכה ב-GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RelayVSRConditioning/he.md)

---
**Source fingerprint (SHA-256):** `fd1a86262240430e4f2a811c2c9d8d62f0b6cdfccb26d5285e36d0d6de3b186f`
