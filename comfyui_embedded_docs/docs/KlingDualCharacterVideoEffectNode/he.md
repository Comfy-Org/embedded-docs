# KlingDualCharacterVideoEffectNode

צומת Kling Dual Character Video Effect יוצר סרטונים עם אפקטים מיוחדים בהתבסס על הסצנה שנבחרה. הוא מקבל שתי תמונות וממקם את התמונה הראשונה בצד שמאל ואת התמונה השנייה בצד ימין של הווידאו המשולב. אפקטים חזותיים שונים מוחלים בהתאם לסצנת האפקט שנבחרה.

## קלטים

| פרמטר | תיאור | סוג נתונים | חובה | טווח |
|-----------|-------------|-----------|----------|-------|
| `image_left` | תמונת צד שמאל | IMAGE | כן | - |
| `image_right` | תמונת צד ימין | IMAGE | כן | - |
| `effect_scene` | סוג סצנת האפקט המיוחד להחלה על יצירת הווידאו | COMBO | כן | `"chat"`<br>`"dance"`<br>`"hug"`<br>`"kill"`<br>`"kiss"`<br>`"pat"`<br>`"punch"`<br>`"shrug"`<br>`"slap"`<br>`"tickle"` |
| `model_name` | המודל לשימוש באפקטים לדמויות (ברירת מחדל: "kling-v1") | COMBO | לא | `"kling-v1"`<br>`"kling-v1-5"`<br>`"kling-v1-6"` |
| `mode` | מצב יצירת הווידאו (ברירת מחדל: "std") | COMBO | לא | `"std"`<br>`"pro"` |
| `duration` | משך הווידאו הנוצר בשניות | COMBO | כן | `"5"`<br>`"10"` |

## פלטים

| שם פלט | תיאור | סוג נתונים |
|-------------|-------------|-----------|
| `output` | הווידאו הנוצר עם אפקטים לדמויות כפולות | VIDEO |
| `duration` | מידע משך הווידאו הנוצר | STRING |

> מסמך זה נוצר על ידי בינה מלאכותית. אם מצאתם שגיאות או שיש לכם הצעות לשיפור, אתם מוזמנים לתרום! [עריכה ב-GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingDualCharacterVideoEffectNode/he.md)

---
**Source fingerprint (SHA-256):** `314fc23940225eb4559ecc74f333bb23e9a4939bbb884c93341f4d6f6e7b64df`
