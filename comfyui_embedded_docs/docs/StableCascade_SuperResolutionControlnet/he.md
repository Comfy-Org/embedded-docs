# StableCascade_SuperResolutionControlnet

צומת זה הוא חלק מקבוצת Stable Cascade הניסיונית. הוא מכין קלטים לעיבוד רזולוציה-על של Stable Cascade על ידי קידוד תמונת קלט עם VAE ליצירת קלט ControlNet, ועל ידי יצירת מצייני מקום לטנטיים ריקים (מלאים באפסים) עבור שלב C ושלב B של תהליך Stable Cascade.

## קלטים

| פרמטר | תיאור | סוג נתון | נדרש | טווח |
| --- | --- | --- | --- | --- |
| `image` | תמונת הקלט שיש לעבד עבור רזולוציה-על. רק 3 ערוצי הצבע הראשונים (RGB) של התמונה משמשים לקידוד. | IMAGE | כן | - |
| `vae` | מודל ה-VAE המשמש לקידוד תמונת הקלט | VAE | כן | - |

## פלטים

| שם פלט | תיאור | סוג נתון |
| --- | --- | --- |
| `controlnet_input` | ייצוג התמונה המקודד על ידי VAE המתאים כקלט ControlNet | IMAGE |
| `stage_c` | ייצוג לטנטי של ממלא מקום (מלא באפסים) עבור שלב C של עיבוד Stable Cascade, עם 16 ערוצים וממדים המבוססים על גודל תמונת הקלט חלקי 16 | LATENT |
| `stage_b` | ייצוג לטנטי של ממלא מקום (מלא באפסים) עבור שלב B של עיבוד Stable Cascade, עם 4 ערוצים וממדים המבוססים על גודל תמונת הקלט חלקי 2 | LATENT |

> מסמך זה נוצר על ידי בינה מלאכותית. אם מצאתם שגיאות או שיש לכם הצעות לשיפור, אתם מוזמנים לתרום! [עריכה ב-GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_SuperResolutionControlnet/he.md)

---
**Source fingerprint (SHA-256):** `d9eff373ac7736f2e2f9788d1b43c04bb3212422aa1703d1d58ac512ce476925`
