# OpenAI GPT Image 2.6 SVG

## סקירה כללית

הצומת OpenAI GPT Image 2.6 SVG מייצר SVG הניתן לעריכה מתוך פרומפט, באמצעות מודלי GPT Image של OpenAI. התוצאה היא סימון וקטורי, ולכן צורות וטקסט נשארים ניתנים לעריכה בעורך וקטורי. שני מודלים זמינים: `gpt-image-2.6-flare` ו-`gpt-image-2.6-sunburst`.

## קלטים

### קלטים משותפים

| פרמטר | תיאור | סוג נתון | חובה | טווח |
| --- | --- | --- | --- | --- |
| `model` | מודל ה-GPT Image שישמש ליצירת ה-SVG. | DYNAMIC_COMBO | כן | `"gpt-image-2.6-flare"`<br>`"gpt-image-2.6-sunburst"` |

### קלטים של gpt-image-2.6-flare ו-gpt-image-2.6-sunburst

שני המודלים חולקים את אותם פרמטרים.

| פרמטר | תיאור | סוג נתון | חובה | טווח |
| --- | --- | --- | --- | --- |
| `model.prompt` | תיאור ה-SVG לשרטוט. (ברירת מחדל: `""`) | STRING | כן | לא רלוונטי |
| `model.size` | גודל תמונת הייחוס שממנה נגזר ה-SVG. (ברירת מחדל: `"1024x1024"`) | COMBO | כן | `"1024x1024"`<br>`"1024x1536"`<br>`"1536x1024"` |
| `model.background` | הרקע של תמונת הייחוס. (ברירת מחדל: `"auto"`) | COMBO | כן | `"auto"`<br>`"opaque"`<br>`"transparent"` |
| `model.quality` | איכות תמונת הייחוס שממנה נגזר ה-SVG. (ברירת מחדל: `"low"`) | COMBO | כן | `"low"`<br>`"medium"`<br>`"high"`<br>`"xhigh"`<br>`"max"` |
| `model.complexity` | המידה שבה המודל מתכנן את תמונת הייחוס לפני הרינדור. (ברירת מחדל: `"high"`) | COMBO | כן | `"low"`<br>`"medium"`<br>`"high"` |
| `model.seed` | קובע אם הצומת ירוץ מחדש; התוצאות אינן דטרמיניסטיות ללא תלות ב-seed. (ברירת מחדל: `42`) | INT | כן | 0 עד 2147483647 |

## פלטים

| שם פלט | תיאור | סוג נתון |
| --- | --- | --- |
| `svg` | התמונה הווקטורית שנוצרה, כסימון SVG. | SVG |

> מסמך זה נוצר על ידי בינה מלאכותית. אם מצאתם שגיאות או שיש לכם הצעות לשיפור, אתם מוזמנים לתרום! [עריכה ב-GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIGPTImageSVGNode/he.md)

---
**Source fingerprint (SHA-256):** `8ac2f473b265d3b6857e6280a1c017301b124fc6d671ec83a59c677218062c90`
