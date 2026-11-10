# Breeze Voice Selector

يختار صوت Breeze مميزًا، أو أي معرّف صوت Breeze، ويمرره إلى Breeze Text to Speech. تُحدّد العقدة المعرّف فقط ولا تُجري أي استدعاء API.

## المدخلات

| المعامل | الوصف | نوع البيانات | مطلوب | النطاق |
| --- | --- | --- | --- | --- |
| `language` | مجموعة اللغة للأصوات المميزة، أو `custom` لإدخال معرّف. الافتراضي: `"English"`. | DYNAMIC_COMBO | نعم | `"English"`<br>`"Chinese"`<br>`"Japanese"`<br>`"custom"` |

### مدخلات اللغة "English" و"Chinese" و"Japanese"

| المعامل | الوصف | نوع البيانات | مطلوب | النطاق |
| --- | --- | --- | --- | --- |
| `voice` | الصوت المميز في تلك اللغة. | COMBO | نعم | خيارات متعددة متاحة |

### مدخلات اللغة "custom"

| المعامل | الوصف | نوع البيانات | مطلوب | النطاق |
| --- | --- | --- | --- | --- |
| `voice_id` | أي معرّف صوت Breeze، مثل صوت أُنشئ بواسطة عقد Breeze الأخرى. أحرف وأرقام و`_` و`-` فقط. الافتراضي: فارغ. | STRING | نعم | معرّف صوت Breeze |

## المخرجات

| اسم المخرج | الوصف | نوع البيانات |
| --- | --- | --- |
| `voice` | صوت Breeze المحدد. | BREEZE_VOICE |

> تم إنشاء هذه الوثيقة بواسطة الذكاء الاصطناعي. إذا وجدت أي أخطاء أو لديك اقتراحات للتحسين، فلا تتردد في المساهمة! [تحرير على GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BreezeVoiceSelector/ar.md)

---
**Source fingerprint (SHA-256):** `0bded8f1b6ec92abaec514ed843b3c138d804e3736758f5df3a2faf52e89a8b0`
