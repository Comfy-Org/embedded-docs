# שיטת ייחוס מודל עריכה

הצומת FluxKontextMultiReferenceLatentMethod מעדכן נתוני התניה על ידי אחסון שיטת לטנטי עזר נבחרת בתוכם. השיטה המאוחסנת משמשת לאחר מכן כאשר מטפלים בלטנטי עזר בשלבי יצירה מאוחרים יותר. צומת זה מסומן כניסיוני ומשתייך למערכת ההתניה של Flux.

## קלטים

| פרמטר | תיאור | סוג נתונים | חובה | טווח |
| --- | --- | --- | --- | --- |
| `conditioning` | נתוני התניה שיש לשנות באמצעות שיטת לטנטי עזר | CONDITIONING | כן | - |
| `reference_latents_method` | השיטה המשמשת לעיבוד לטנטי עזר. אם נבחר ערך המכיל "uxo" או "uso", הוא מומר ל-"uxo" לפני אחסונו. פרמטר זה מסומן כמתקדם. | COMBO | כן | `"offset"`<br>`"index"`<br>`"uxo/uno"`<br>`"index_timestep_zero"`<br>`"index_timestep_zero_isolated"`<br>`"index_timestep_zero_text_start"` |

## פלטים

| שם פלט | תיאור | סוג נתונים |
| --- | --- | --- |
| `conditioning` | נתוני התניה ששונו לאחר החלת שיטת לטנטי עזר | CONDITIONING |

> מסמך זה נוצר על ידי בינה מלאכותית. אם מצאתם שגיאות או שיש לכם הצעות לשיפור, אתם מוזמנים לתרום! [עריכה ב-GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxKontextMultiReferenceLatentMethod/he.md)

---
**Source fingerprint (SHA-256):** `de2e3d34f9e47a90ff37300489bffef8082eb92deefbc2ce338b17b0d853ac77`
