# ClipLoader

הצומת CLIPLoader טוען מודל מקודד טקסט (CLIP, T5 או דומה) מקובץ, ומעמיד אותו לרשות צמתים אחרים שזקוקים להמרת פרומפטים של טקסט לייצוגים מספריים. הוא תומך במגוון רחב של ארכיטקטורות מודלים, שכל אחת מהן דורשת סוג מקודד ספציפי.

## קלטים

| פרמטר | תיאור | סוג נתונים | נדרש | טווח |
|-----------|-------------|-----------|----------|-------|
| `clip_name` | שם הקובץ של מודל מקודד הטקסט לטעינה. עליו להיות קובץ הנמצא בספרייה `ComfyUI/models/text_encoders/`. | STRING | כן | רשימת קבצים הנמצאים בתיקיית `text_encoders` |
| `type` | סוג הארכיטקטורה של המודל הנטען. זה קובע איזה וריאנט מקודד ספציפי יש להשתמש בו (ברירת מחדל: `"stable_diffusion"`). | COMBO | כן | `"stable_diffusion"`<br>`"stable_cascade"`<br>`"sd3"`<br>`"stable_audio"`<br>`"mochi"`<br>`"ltxv"`<br>`"pixart"`<br>`"cosmos"`<br>`"lumina2"`<br>`"wan"`<br>`"hidream"`<br>`"chroma"`<br>`"ace"`<br>`"omnigen2"`<br>`"qwen_image"`<br>`"hunyuan_image"`<br>`"flux2"`<br>`"ovis"`<br>`"longcat_image"`<br>`"cogvideox"`<br>`"lens"`<br>`"pixeldit"`<br>`"ideogram4"`<br>`"boogu"`<br>`"krea2"`<br>`"joyimage"`<br>`"mage"`<br>`"minimax"`<br>`"yue2"`<br>`"flux3"`<br>`"moss_image"`<br>`"fibo2"` |
| `device` | ההתקן שעליו לטעון את המודל. `"default"` משתמש ב-GPU אם זמין, בעוד `"cpu"` כופה טעינה על CPU. זוהי אפשרות מתקדמת (ברירת מחדל: `"default"`). | COMBO | לא | `"default"`<br>`"cpu"` |

### מיפויים נתמכים של סוג למקודד

הפרמטר `type` בוחר את המקודד המתאים עבור ארכיטקטורת מודל נתונה. להלן מיפויים נפוצים:

| סוג | מקודד |
|------|---------|
| stable_diffusion | clip-l |
| stable_cascade | clip-g |
| sd3 | t5 xxl / clip-g / clip-l |
| stable_audio | t5 base |
| mochi | t5 xxl |
| cogvideox | t5 xxl (ריפוד של 226 טוקנים) |
| cosmos | t5 xxl ישן |
| lumina2 | gemma 2 2B |
| wan | umt5 xxl |
| hidream | llama-3.1 (מומלץ) או t5 |
| omnigen2 | qwen vl 2.5 3B |
| joyimage | qwen3-vl 8B |
| lens | gpt-oss-20b |
| pixeldit | gemma 2 2B elm |
| minimax | MiniMax H3 Qwen3-VL או Music3 Qwen/RVQ |
| flux3 | qwen3-vl 4B |
| fibo2 | qwen3-vl 4B |

## פלטים

| שם פלט | תיאור | סוג נתונים |
|-------------|-------------|-----------|
| `CLIP` | מודל מקודד הטקסט הנטען, מוכן לחיבור לצמתים אחרים לקידוד טקסט ולהתניה. | CLIP |

> מסמך זה נוצר על ידי בינה מלאכותית. אם מצאתם שגיאות או שיש לכם הצעות לשיפור, אתם מוזמנים לתרום! [עריכה ב-GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ClipLoader/he.md)

---
**Source fingerprint (SHA-256):** `75cf64ce955946681dee79035fc91b54be0a99e3fc22b8c4737929ce0bdff13e`
