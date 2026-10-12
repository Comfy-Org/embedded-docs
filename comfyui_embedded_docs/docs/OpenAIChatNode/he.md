# OpenAIChatNode

צומת זה מייצר תגובות טקסט ממודל OpenAI. הוא שולח את הנחיית הטקסט שלך, ובאופן אופציונלי תמונות או קבצים, למודל OpenAI ומחזיר את תגובת הטקסט שנוצרה.

## קלטים

| פרמטר | תיאור | סוג נתונים | נדרש | טווח |
|-----------|-------------|-----------|----------|-------|
| `prompt` | קלטי טקסט למודל, המשמשים ליצירת תגובה (ברירת מחדל: מחרוזת ריקה). | STRING | כן | - |
| `persist_context` | פרמטר זה מיושן ואין לו השפעה (ברירת מחדל: False). | BOOLEAN | כן | - |
| `model` | המודל המשמש ליצירת התגובה (ברירת מחדל: `gpt-5`) | COMBO | כן | `gpt-6-astra`<br>`gpt-6-sol`<br>`gpt-6-luna`<br>`gpt-5.6-sol`<br>`gpt-5.6-terra`<br>`gpt-5.6-luna`<br>`gpt-5.5-pro`<br>`gpt-5.5`<br>`gpt-5`<br>`gpt-5-mini`<br>`gpt-5-nano`<br>`gpt-4.1`<br>`gpt-4.1-mini`<br>`gpt-4.1-nano`<br>`o4-mini`<br>`o3`<br>`o1-pro`<br>`o1` |
| `images` | תמונה/תמונות אופציונליות לשימוש כהקשר עבור המודל. כדי לכלול מספר תמונות, ניתן להשתמש בצומת Batch Images. | IMAGE | לא | - |
| `files` | קובץ/קבצים אופציונליים לשימוש כהקשר עבור המודל. מקבל קלטים מצומת OpenAI Chat Input Files. | OPENAI_INPUT_FILES | לא | - |
| `advanced_options` | תצורה אופציונלית עבור המודל. מקבל קלטים מצומת OpenAI Chat Advanced Options. | OPENAI_CHAT_CONFIG | לא | - |

הערה: כאשר תצורת `advanced_options` שקובעת מאמץ הסקה מחוברת, ה-`model` הנבחר חייב לתמוך בערך מאמץ זה. לדוגמה, משפחת המודלים gpt-4.1 אינה תומכת במאמץ הסקה כלל, `gpt-6-sol` ו-`gpt-6-luna` תומכים בערכים none, low, medium, high, xhigh ו-max, `gpt-5.5` תומך בערכים none, low, medium, high ו-xhigh, ו-`gpt-5.5-pro` תומך בערכים medium, high ו-xhigh. אם מאמץ ההסקה אינו נתמך על ידי המודל הנבחר, הצומת מעלה שגיאה.

## פלטים

| שם פלט | תיאור | סוג נתונים |
|-------------|-------------|-----------|
| `output_text` | תגובת הטקסט שנוצרה על ידי מודל OpenAI. | STRING |

> מסמך זה נוצר על ידי בינה מלאכותית. אם מצאתם שגיאות או שיש לכם הצעות לשיפור, אתם מוזמנים לתרום! [עריכה ב-GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIChatNode/he.md)

---
**Source fingerprint (SHA-256):** `46b4558f1368191e2b4eb68f79e098f289c9eb80e1e05f7a516123c098295f2b`
