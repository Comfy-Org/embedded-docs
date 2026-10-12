# SaveTrainingDataset

צומת זה שומר מערך נתוני אימון מקודד לדיסק לטעינה יעילה במהלך האימון. הוא מקבל latentים של תמונות ואת ה-conditioning הטקסטואלי המתאים להם, מפצל אותם לקבצים קטנים יותר הנקראים shards, ומאחסן אותם בתיקייה בתוך ספריית datasets. הוא גם כותב קובץ מטא-נתונים המתאר את מערך הנתונים.

## קלטים

| פרמטר | תיאור | סוג נתונים | חובה | טווח |
| --- | --- | --- | --- | --- |
| `latents` | רשימת מילוני latent מ-MakeTrainingDataset. | LATENT | כן | N/A |
| `conditioning` | רשימת רשימות conditioning מ-MakeTrainingDataset. | CONDITIONING | כן | N/A |
| `folder_name` | שם התיקייה שאליה לשמור את מערך הנתונים, בתוך ספריית datasets. תתי-תיקיות כגון 'project/run1' מותרות. (ברירת מחדל: "training_dataset") | STRING | כן | N/A |
| `shard_size` | מספר הדגימות לכל קובץ shard. (ברירת מחדל: 1000) | INT | כן | 1 to 100000 |

**הערה:** מספר הפריטים ב-`latents` חייב להתאים בדיוק למספר הפריטים ב-`conditioning`; הצומת מעלה שגיאה אם מספרים אלה אינם תואמים. `folder_name` חייב לציין תת-תיקייה של ספריית datasets (לדוגמה `my_dataset`) — הוא לא יכול להיות ספריית datasets עצמה, ושמות תיקיות שהיו נפתרים מחוץ לספריית datasets נדחים. הפרמטר `shard_size` הוא הגדרה מתקדמת.

## פלטים

צומת זה אינו מפיק נתוני פלט כלשהם. תפקידו לשמור קבצים בדיסק שלך. כל shard נשמר כקובץ `shard_XXXX.pkl` בתיקייה שנבחרה, וקובץ `metadata.json` מתעד את המספר הכולל של דגימות, מספר ה-shards וגודל ה-shard.

> מסמך זה נוצר על ידי בינה מלאכותית. אם מצאתם שגיאות או שיש לכם הצעות לשיפור, אתם מוזמנים לתרום! [עריכה ב-GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveTrainingDataset/he.md)

---
**Source fingerprint (SHA-256):** `6d7b63a24ac42907b0f4a1358712cd0ed085982ecd308bce87e5376d9bbc2274`
