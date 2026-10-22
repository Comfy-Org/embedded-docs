# ControlnetApply

שימוש ב-ControlNet מחייב עיבוד מקדים של תמונות קלט. מכיוון שצמתי ComfyUI הראשוניים אינם כוללים קדם-מעבדים ומודלים של ControlNet, יש להתקין תחילה קדם-מעבדים של ControlNet [הורדת קדם-מעבדים כאן](https://github.com/Fannovel16/comfy_controlnet_preprocessors) ואת מודלי ה-ControlNet המתאימים.

## קלטים

| פרמטר | סוג נתונים | פונקציה |
| --- | --- | --- |
| `positive` | `CONDITIONING` | נתוני התניה חיוביים, מהצומת CLIP Text Encoder או מקלטי התניה אחרים |
| `negative` | `CONDITIONING` | נתוני התניה שליליים, מהצומת CLIP Text Encoder או מקלטי התניה אחרים |
| `control_net` | `CONTROL_NET` | מודל ה-ControlNet שיש להחיל, שבדרך כלל מתקבל כקלט מהצומת ControlNet Loader |
| `image` | `IMAGE` | תמונה שעליה יחול ControlNet; יש לעבד אותה באמצעות קדם-מעבד |
| `vae` | `VAE` | קלט מודל VAE |
| `strength` | `FLOAT` | שולט בעוצמת התאמות הרשת, טווח ערכים 0~10. ערכים מומלצים בין 0.5~1.5 הם סבירים. ערכים נמוכים יותר מעניקים למודל חופש רב יותר, ואילו ערכים גבוהים יותר כופים אילוצים מחמירים יותר. ערכים גבוהים מדי עלולים להפיק תמונות מוזרות. ניתן לבדוק ולכוונן ערך זה כדי לכוונן את השפעת רשת הבקרה. |
| `start_percent` | `FLOAT` | ערך 0.000~1.000, קובע מתי להתחיל להחיל את ControlNet באחוזים, למשל, 0.2 פירושו שהנחיית ControlNet תתחיל להשפיע על יצירת התמונה ב-20% מתהליך הדיפוזיה |
| `end_percent` | `FLOAT` | ערך 0.000~1.000, קובע מתי להפסיק להחיל את ControlNet באחוזים, למשל, 0.8 פירושו שהנחיית ControlNet תפסיק להשפיע על יצירת התמונה ב-80% מתהליך הדיפוזיה |

### פלטים

| פרמטר | סוג נתונים | פונקציה |
| --- | --- | --- |
| `positive` | `CONDITIONING` | נתוני התניה חיוביים שעובדו על ידי ControlNet, ניתן להוציא אותם ל-ControlNet הבא או לצמתי K Sampler |
| `negative` | `CONDITIONING` | נתוני התניה שליליים שעובדו על ידי ControlNet, ניתן להוציא אותם ל-ControlNet הבא או לצמתי K Sampler |

> מסמך זה נוצר על ידי בינה מלאכותית. אם מצאתם שגיאות או שיש לכם הצעות לשיפור, אתם מוזמנים לתרום! [עריכה ב-GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ControlNetApply/he.md)
