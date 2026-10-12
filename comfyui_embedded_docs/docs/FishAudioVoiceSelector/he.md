# בורר קולות Fish Audio

צומת Fish Audio Voice Selector בוחר קול מספריית Fish Audio להפקת דיבור מטקסט. באפשרותך לבחור אחד מהקולות המוגדרים מראש המובנים, או לבחור "custom" כדי להזין כל מזהה מודל קול מ-fish.audio.

## קלטים

### קלטים משותפים

| פרמטר | תיאור | סוג נתונים | נדרש | טווח |
|-----------|-------------|-----------|----------|-------|
| `voice` | בחר קול, או 'custom' כדי להזין כל מזהה מודל קול של fish.audio. | DYNAMIC_COMBO | כן | "Energetic Male (en)"<br>"Friendly Women (en)"<br>"Sarah (en)"<br>"Verity (en)"<br>"Polo (en)"<br>"Adrian (en)"<br>"E-girl (en)"<br>"Narrator (en)"<br>"Warm Conversational Voice (en)"<br>"Warm Storyteller (en)"<br>"Dramatic Character Male (en)"<br>"News Narrator (zh)"<br>"Lively Female (zh)"<br>"Gentle Female (zh)"<br>"Energetic Female (ja)"<br>"Calm Female (ja)"<br>"Calm Male (ja)"<br>"custom" |

אפשרויות הקול המוגדרות מראש מכסות קולות באנגלית (en), סינית (zh) ויפנית (ja), ואינן דורשות קלטים נוספים.

### קלטים מותאמים אישית

קלטים אלה מופיעים כאשר `voice` מוגדר ל-"custom".

| פרמטר | תיאור | סוג נתונים | נדרש | טווח |
|-----------|-------------|-----------|----------|-------|
| `voice_id` | מזהה מודל קול מ-fish.audio, למשל המזהה בכתובת https://fish.audio/m/<id>/. ברירת מחדל: מחרוזת ריקה. | STRING | כן | כל מזהה מודל קול תקף של Fish Audio |

הערה: כאשר `voice` מוגדר ל-"custom", `voice_id` חייב שלא להיות ריק לאחר הסרת רווחים; אחרת הצומת מעלה שגיאה "Custom voice ID is empty.". אם מועברת אפשרות קול שאינה מזוהה, הצומת מעלה שגיאה "Unknown voice".

## פלטים

| שם פלט | תיאור | סוג נתונים |
|-------------|-------------|-----------|
| `voice` | מזהה מודל הקול הנבחר של Fish Audio. עבור קול מוגדר מראש, מוחזר מזהה הקול המתאים מספריית Fish Audio; עבור "custom", מוחזר הערך `voice_id` שהוזן. | FISHAUDIO_VOICE |

> מסמך זה נוצר על ידי בינה מלאכותית. אם מצאתם שגיאות או שיש לכם הצעות לשיפור, אתם מוזמנים לתרום! [עריכה ב-GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FishAudioVoiceSelector/he.md)

---
**Source fingerprint (SHA-256):** `4f99a58aa7e6054f58fe84e61e4e1008b17828bd97d71ef0a4009c4de4052bbd`
