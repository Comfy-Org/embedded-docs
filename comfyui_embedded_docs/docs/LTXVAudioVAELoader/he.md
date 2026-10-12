# LTXVAudioVAELoader

צומת LTXV Audio VAE Loader טוען מודל Audio Variational Autoencoder (VAE) מאומן מראש מקובץ צ'קפוינט. הוא קורא את הצ'קפוינט שצוין, שומר את משקלי ה-Audio VAE וה-vocoder, ומכין את המודל לשימוש בזרימות עבודה של יצירה או עיבוד אודיו בתוך ComfyUI.

## קלטים

| פרמטר | תיאור | סוג נתונים | חובה | טווח |
|-----------|-------------|-----------|----------|-------|
| `ckpt_name` | צ'קפוינט Audio VAE לטעינה. זוהי רשימה נפתחת המאוכלסת בכל הקבצים שנמצאים בתיקיית `checkpoints` של ComfyUI. | COMBO | כן | כל הקבצים בתיקיית `checkpoints`. הרשימה נוצרת בזמן ריצה. |

הקובץ הנבחר חייב להיות צ'קפוינט תקין של LTXV audio VAE. הצומת שומר רק את משקלי ה-Audio VAE וה-vocoder מהקובץ, ומעלה שגיאה אם המודל הנטען אינו VAE תקין.

## פלטים

| שם פלט | תיאור | סוג נתונים |
|-------------|-------------|-----------|
| `Audio VAE` | מודל Audio Variational Autoencoder (VAE) הנטען, מוכן לחיבור לצמתי עיבוד אודיו אחרים. | VAE |

> מסמך זה נוצר על ידי בינה מלאכותית. אם מצאתם שגיאות או שיש לכם הצעות לשיפור, אתם מוזמנים לתרום! [עריכה ב-GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAudioVAELoader/he.md)

---
**Source fingerprint (SHA-256):** `c91956645a9de0b8f56191f6c0c6bef43f13724ba59078ec9a885168bf2650e8`
