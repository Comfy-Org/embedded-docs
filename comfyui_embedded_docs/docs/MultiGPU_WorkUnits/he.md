# פיצול תור CFG לריבוי GPU

## סקירה כללית:

צומת MultiGPU CFG Split מאפשר עיבוד דיפוזיה באמצעות מספר GPUs המותקנים באותה מערכת. תוצאות הביצועים תלויות בתהליך העבודה, אך נמדדו האצות של עד פי 1.95 בתהליכי עבודה נפוצים.

## פרטים עיקריים:

אין תמיכה בערבוב סוגי GPU שונים; ה-GPUs המותקנים חייבים להיות זהים (למשל 2x 5090, או 2x 5080 וכו').

ComfyUI יזהה אוטומטית מספר GPUs מותקנים בעת האתחול.

## GPUs נתמכים:

כל תצורות dual GPU הומוגניות עם ארכיטקטורת Ampere+ (למשל 2 x 3090 או 2 x RTX6000 Pro)

## מודלים נתמכים:

* LTX-2.3  
* WAN 2.2  
* FLUX.2 Klein \- Base Versions  
* Z-Image  
* Stable Diffusion 3.5 Large  
* Hunyuan Video  
* Qwen-Image-Edit-2511  
* Hunyuan-3D-v2.1  
* SDXL

## קלטים

| פרמטר | תיאור | סוג נתונים | נדרש | טווח |
| --- | --- | --- | --- | --- |
| `model` | המודל שיש להכין לפיצול MultiGPU CFG לפני דגימה. | MODEL | כן | N/A |
| `max_gpus` | המספר המרבי של GPUs זהים לשימוש בפיצול עומס העבודה. יש להגדיר זאת למספר ה-GPUs התואמים המותקנים במערכת שלך. | INT | כן | מינימום: 1<br>צעד: 1<br>ברירת מחדל: 2 |

## פלטים

| שם פלט | תיאור | סוג נתונים |
| --- | --- | --- |
| `MODEL` | המודל שהוכן לפיצול MultiGPU CFG, מוכן לדגימה מואצת. | MODEL |

## צומת:

![image1.png](./asset/image1.png)  
יש להגדיר את השדה max\_gpus למספר המרבי של GPUs זהים המותקנים במערכת.

**מיקום הצומת:** יש למקם את MultiGPU CFG Split בין צומת Model Load לצומת Sampling. אם צמתים אחרים מחוברים לפלט המודל של צומת טעינת המודל, MultiGPU CFG צריך להיות הצומת האחרון בשרשרת לפני צומת Sampling.

![image2.png](./asset/image2.png)

**דרישות תהליך עבודה:** הצומת פועל על ידי פיצול תהליך העבודה של הדיפוזיה ברמת ה-CFG; בשל כך, ה-CFG בתהליך העבודה חייב להיות גדול מ-CFG=1. תהליכי עבודה מזוקקים (distilled) הדורשים CFG \=1 לא יציגו שיפור ביצועים בעת שימוש בצומת MultiGPU CFG Split להרצה על מספר GPUs.

## אימות ניצול Multi-GPU

בעת הרצת תהליך עבודה עם MultiGPU CFG Split מופעל, ניתן להסתכל ב-Windows Task Manager ולבחור בקטגוריית הביצועים  
![image3.png](./asset/image3.webp)  
![image4.png](./asset/image4.webp)  
אמורה להופיע פעילות בשני ה-GPUs המותקנים בזמן שה-sampler פועל בתהליך העבודה.

## תהליך עבודה לדוגמה Multi-GPU: (Wan 2.2 FP8)

[תהליך עבודה לדוגמה (Wan 2.2 FP8)](https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/MultiGPU_WorkUnits/asset/video_wan2_2_14B_t2v_mGPU.json)

> מסמך זה נוצר על ידי בינה מלאכותית. אם מצאתם שגיאות או שיש לכם הצעות לשיפור, אתם מוזמנים לתרום! [עריכה ב-GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MultiGPU_WorkUnits/he.md)

---
**Source fingerprint (SHA-256):** `7293ee785e29aea9a1a70a10444b99e89fb23c866505628ec57c209a2b8aaee0`
