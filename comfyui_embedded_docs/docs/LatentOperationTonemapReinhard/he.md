# LatentOperationTonemapReinhard

צומת זה יוצר פעולת latent שמחילה מיפוי טונים של Reinhard על וקטורי latent. הוא מנרמל כל וקטור latent, מודד את התפלגות העוצמה הכוללת (ממוצע וסטיית תקן), ולאחר מכן דוחס ערכי עוצמה קיצוניים באמצעות עקומת Reinhard, כאשר החוזק הכולל נשלט על ידי מכפיל. הצומת מסומן כניסיוני (ניתן לחפש גם כ־"hdr latent").

## קלטים

| פרמטר | תיאור | סוג נתונים | חובה | טווח |
| --- | --- | --- | --- | --- |
| `multiplier` | שולט בעוצמת אפקט מיפוי הטונים (ברירת מחדל: 1.0) | FLOAT | כן | 0.0 to 100.0 (step 0.01) |

## פלטים

| שם פלט | תיאור | סוג נתונים |
| --- | --- | --- |
| `operation` | מחזיר פעולת מיפוי טונים שניתן להחיל על וקטורי latent | LATENT_OPERATION |

> מסמך זה נוצר על ידי בינה מלאכותית. אם מצאתם שגיאות או שיש לכם הצעות לשיפור, אתם מוזמנים לתרום! [עריכה ב-GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentOperationTonemapReinhard/he.md)

---
**Source fingerprint (SHA-256):** `19d58c288967ab27eb1e84e60bc35a6d6c8b4e643168de689132396ae0ee3cbe`
