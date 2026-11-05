# RelayVSRConditioning

RelayVSR Conditioning מכין את הקונדישנינג ואת הלטנט הריק להגדלה (upscale) של וידאו ב-RelayVSR. RelayVSR מריץ את מודל Wan 2.2 החד-שלבי שלו רק בכל פריים 15 של הקליפ, בתוספת הפריים האחרון, כך שהלטנט שהוא מחזיר מכיל רק את פריימי המפתח האלה. לאחר מכן VSR Decode משלים את הפריימים שביניהם.

## קלטים

| פרמטר | תיאור | סוג נתון | חובה | טווח |
| --- | --- | --- | --- | --- |
| `model` | מודל הדיפוזיה RelayVSR, נטען עם Load Model: `relayvsr_x2_lightx2v_int8_convrot.safetensors` או `relayvsr_x4_int8_convrot.safetensors`. | MODEL | כן | N/A |
| `images` | הווידאו באיכות נמוכה ברזולוציה המקורית שלו. מקדם ההגדלה של המודל קובע את גודל התוצאה. | IMAGE | כן | N/A |

## פלטים

| שם פלט | תיאור | סוג נתון |
| --- | --- | --- |
| `positive` | קונדישנינג הנושא את פריימי המפתח שנבחרו כהנחיה באיכות נמוכה. | CONDITIONING |
| `latent` | לטנט ריק עם פריים אחד לכל פריים מפתח, מוכן לסמפלר. | LATENT |

## שימוש

בצעו דגימה של ה-`latent` בצעד אחד ב-CFG 1: אין פרומפט ואין מקודד טקסט בגרף. שלחו את פלט הסמפלר, את אותם `images` ואת RelayVSR Flash VAE אל VSR Decode, והקפידו על התאמה בין הזוג: מודל x2 עם מפענח x2, ומודל x4 עם מפענח x4.

רק פריימי מפתח נדגמים, כך שקליפ של 150 פריימים הופך ללטנט של 11 פריימים. הסמפלר עובד על חלק קטן מהווידאו, ו-VSR Decode משחזר את השאר.

> מסמך זה נוצר על ידי בינה מלאכותית. אם מצאתם שגיאות או שיש לכם הצעות לשיפור, אתם מוזמנים לתרום! [עריכה ב-GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RelayVSRConditioning/he.md)

---
**Source fingerprint (SHA-256):** `fd1a86262240430e4f2a811c2c9d8d62f0b6cdfccb26d5285e36d0d6de3b186f`
