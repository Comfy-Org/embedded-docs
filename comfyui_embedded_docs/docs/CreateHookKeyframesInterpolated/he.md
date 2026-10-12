# צור Keyframes Hook Interp.

יוצר רצף של פריימי מפתח hook עם ערכי עוצמה שעברו אינטרפולציה בין נקודת התחלה לנקודת סיום. הצומת יוצר מספר פריימי מפתח שמעבירים את פרמטר העוצמה בצורה חלקה על פני טווח אחוזים מוגדר של תהליך היצירה, תוך שימוש בשיטות אינטרפולציה שונות לשליטה בעקומת המעבר.

## קלטים

| פרמטר | תיאור | סוג נתונים | חובה | טווח |
| --- | --- | --- | --- | --- |
| `strength_start` | ערך העוצמה ההתחלתי ברצף האינטרפולציה (ברירת מחדל: 1.0) | FLOAT | כן | 0.0 - 10.0 |
| `strength_end` | ערך העוצמה הסופי ברצף האינטרפולציה (ברירת מחדל: 1.0) | FLOAT | כן | 0.0 - 10.0 |
| `interpolation` | שיטת האינטרפולציה המשמשת למעבר בין ערכי העוצמה (ברירת מחדל: LINEAR) | COMBO | כן | `LINEAR`<br>`EASE_IN`<br>`EASE_OUT`<br>`EASE_IN_OUT`<br>`EASE_OUT_IN`<br>`SINE`<br>`CUBIC`<br>`QUARTIC`<br>`QUINTIC`<br>`EXPO`<br>`CIRC`<br>`BACK`<br>`BOUNCE`<br>`ELASTIC` |
| `start_percent` | אחוז מיקום ההתחלה בתהליך היצירה (ברירת מחדל: 0.0) | FLOAT | כן | 0.0 - 1.0 |
| `end_percent` | אחוז מיקום הסיום בתהליך היצירה (ברירת מחדל: 1.0) | FLOAT | כן | 0.0 - 1.0 |
| `keyframes_count` | מספר פריימי המפתח שיש ליצור ברצף האינטרפולציה (ברירת מחדל: 5) | INT | כן | 2 - 100 |
| `print_keyframes` | האם להדפיס מידע על פריימי המפתח שנוצרו ליומן (ברירת מחדל: False) | BOOLEAN | כן | True/False |
| `prev_hook_kf` | קבוצת פריימי מפתח hook קודמת אופציונלית שאליה יש לצרף | HOOK_KEYFRAMES | לא | - |

## פלטים

| שם פלט | תיאור | סוג נתונים |
| --- | --- | --- |
| `HOOK_KF` | קבוצת פריימי המפתח hook שנוצרה, המכילה את הרצף שעבר אינטרפולציה | HOOK_KEYFRAMES |

> מסמך זה נוצר על ידי בינה מלאכותית. אם מצאתם שגיאות או שיש לכם הצעות לשיפור, אתם מוזמנים לתרום! [עריכה ב-GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateHookKeyframesInterpolated/he.md)

---
**Source fingerprint (SHA-256):** `f90c96745ca1f02bbb02e08d2d82be1bbb1f3c80ac5d53a4c6bc07a0e2b8d76f`
