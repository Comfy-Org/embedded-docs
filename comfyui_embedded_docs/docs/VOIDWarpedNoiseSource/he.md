# VOIDWarpedNoiseSource

צומת זה ממיר LATENT (כגון הפלט של הצומת VOIDWarpedNoise) למקור NOISE. הדבר מאפשר להזין רעש מעוות מחושב מראש אל צמתים שמצפים למקור רעש, כגון SamplerCustomAdvanced.

## קלטים

| פרמטר | תיאור | סוג נתונים | נדרש | טווח |
| --- | --- | --- | --- | --- |
| `warped_noise` | רעש מעוות מסוג LATENT מהצומת VOIDWarpedNoise | LATENT | כן | N/A |

## פלטים

| שם פלט | תיאור | סוג נתונים |
| --- | --- | --- |
| `NOISE` | מקור NOISE שעוטף את ה-LATENT שסופק, שמיש עם SamplerCustomAdvanced | NOISE |

> מסמך זה נוצר על ידי בינה מלאכותית. אם מצאתם שגיאות או שיש לכם הצעות לשיפור, אתם מוזמנים לתרום! [עריכה ב-GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDWarpedNoiseSource/he.md)

---
**Source fingerprint (SHA-256):** `61d7c82cb8a2acba28f980c4c42c6d4be12788b27676a5d30885799cf9c36185`
