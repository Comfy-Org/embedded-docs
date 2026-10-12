# TextEncodeAceStepAudio1.5

הצומת TextEncodeAceStepAudio1.5 מכין טקסט ומטא-נתונים הקשורים לאודיו לשימוש עם מודל AceStepAudio 1.5. הוא מקבל תגיות תיאוריות, מילות שיר ופרמטרים מוזיקליים, ואז משתמש במודל CLIP כדי להמיר אותם לפורמט conditioning המתאים ליצירת אודיו.

## קלטים

| פרמטר | תיאור | סוג נתונים | חובה | טווח |
| --- | --- | --- | --- | --- |
| `clip` | מודל ה-CLIP המשמש לטוקניזציה ולקידוד טקסט הקלט. | CLIP | כן | N/A |
| `tags` | תגיות תיאוריות עבור האודיו, כגון ז'אנר, מצב רוח או כלי נגינה. תומך בקלט רב-שורתי ובפרומפטים דינמיים. | STRING | כן | N/A |
| `lyrics` | מילות השיר עבור הרצועה. תומך בקלט רב-שורתי ובפרומפטים דינמיים. | STRING | כן | N/A |
| `seed` | ערך seed אקראי ליצירה ניתנת לשחזור. כולל ווידג'ט control_after_generate. ברירת מחדל: 0. | INT | לא | 0 to 18446744073709551615 |
| `bpm` | מספר הפעימות בדקה (BPM) עבור האודיו המיוצר. ברירת מחדל: 120. | INT | לא | 10 to 300 |
| `duration` | משך האודיו הרצוי בשניות. ברירת מחדל: 120.0. | FLOAT | לא | 0.0 to 2000.0 |
| `timesignature` | המשקל המוזיקלי (time signature). | COMBO | לא | `"2"`<br>`"3"`<br>`"4"`<br>`"6"` |
| `language` | שפת טקסט הקלט. ברירת מחדל: "en". | COMBO | לא | `"ar"`<br>`"az"`<br>`"bg"`<br>`"bn"`<br>`"ca"`<br>`"cs"`<br>`"da"`<br>`"de"`<br>`"el"`<br>`"en"`<br>`"es"`<br>`"fa"`<br>`"fi"`<br>`"fr"`<br>`"he"`<br>`"hi"`<br>`"hr"`<br>`"ht"`<br>`"hu"`<br>`"id"`<br>`"is"`<br>`"it"`<br>`"ja"`<br>`"ko"`<br>`"la"`<br>`"lt"`<br>`"ms"`<br>`"ne"`<br>`"nl"`<br>`"no"`<br>`"pa"`<br>`"pl"`<br>`"pt"`<br>`"ro"`<br>`"ru"`<br>`"sa"`<br>`"sk"`<br>`"sr"`<br>`"sv"`<br>`"sw"`<br>`"ta"`<br>`"te"`<br>`"th"`<br>`"tl"`<br>`"tr"`<br>`"uk"`<br>`"ur"`<br>`"vi"`<br>`"yue"`<br>`"zh"`<br>`"unknown"` |
| `keyscale` | המפתח והסולם המוזיקליים (מז'ור או מינור). | COMBO | לא | `"C major"`<br>`"C# major"`<br>`"Db major"`<br>`"D major"`<br>`"D# major"`<br>`"Eb major"`<br>`"E major"`<br>`"F major"`<br>`"F# major"`<br>`"Gb major"`<br>`"G major"`<br>`"G# major"`<br>`"Ab major"`<br>`"A major"`<br>`"A# major"`<br>`"Bb major"`<br>`"B major"`<br>`"C minor"`<br>`"C# minor"`<br>`"Db minor"`<br>`"D minor"`<br>`"D# minor"`<br>`"Eb minor"`<br>`"E minor"`<br>`"F minor"`<br>`"F# minor"`<br>`"Gb minor"`<br>`"G minor"`<br>`"G# minor"`<br>`"Ab minor"`<br>`"A minor"`<br>`"A# minor"`<br>`"Bb minor"`<br>`"B minor"` |
| `generate_audio_codes` | הפעל את ה-LLM שמייצר קודי אודיו. פעולה זו עשויה להיות איטית, אך היא תשפר את איכות האודיו המיוצר. כבה אפשרות זו אם אתה מספק למודל רפרנס אודיו. ברירת מחדל: True. | BOOLEAN | לא | N/A |
| `cfg_scale` | סולם ההנחיה נטול המסווג (classifier-free guidance). ערכים גבוהים יותר גורמים לפלט לפעול ביתר קפדה לפי הפרומפט. ברירת מחדל: 2.0. | FLOAT | לא | 0.0 to 100.0 |
| `temperature` | טמפרטורת דגימה. ערכים נמוכים יותר הופכים את הפלט לדטרמיניסטי יותר. ברירת מחדל: 0.85. | FLOAT | לא | 0.0 to 2.0 |
| `top_p` | הסתברות דגימת הגרעין (top-p). ברירת מחדל: 0.9. | FLOAT | לא | 0.0 to 2000.0 |
| `top_k` | מספר האסימונים בעלי ההסתברות הגבוהה ביותר שיש לשקול (top-k). ברירת מחדל: 0. | INT | לא | 0 to 100 |
| `min_p` | סף ההסתברות המינימלי לדגימת אסימונים (min-p). ברירת מחדל: 0.000. | FLOAT | לא | 0.0 to 1.0 |

## פלטים

| שם פלט | תיאור | סוג נתונים |
| --- | --- | --- |
| `CONDITIONING` | נתוני ההתניה, הכוללים את הטקסט המקודד ואת פרמטרי האודיו עבור מודל AceStepAudio 1.5. | CONDITIONING |

> מסמך זה נוצר על ידי בינה מלאכותית. אם מצאתם שגיאות או שיש לכם הצעות לשיפור, אתם מוזמנים לתרום! [עריכה ב-GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeAceStepAudio1.5/he.md)

---
**Source fingerprint (SHA-256):** `4bc97ec6220514b71fafde610339f2dca4ded26f68b541ed43ea492f127321f8`
