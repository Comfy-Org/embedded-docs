# HeyGenVideoTranslateNode

## نظرة عامة

ترجمة فيديو منطوق إلى لغة أخرى مع استنساخ الصوت ومزامنة الشفاه. يقوم هذا العقد باستنساخ صوت المتحدث الأصلي وإعادة تحريك الفم ليتوافق مع الكلام المترجم، مما ينتج نتيجة طبيعية المظهر.

## المدخلات

| المعامل | الوصف | نوع البيانات | إلزامي | النطاق |
|---------|-------|---------------|---------|--------|
| `video` | فيديو يحتوي على كلام للترجمة. | VIDEO | نعم | - |
| `output_language` | اللغة المستهدفة للفيديو المترجم. | STRING | نعم | "Arabic"<br>"Bengali"<br>"Chinese"<br>"Danish"<br>"Dutch"<br>"English"<br>"French"<br>"German"<br>"Greek"<br>"Hindi"<br>"Indonesian"<br>"Italian"<br>"Japanese"<br>"Korean"<br>"Malay"<br>"Polish"<br>"Portuguese"<br>"Russian"<br>"Spanish"<br>"Swedish"<br>"Tamil"<br>"Telugu"<br>"Thai"<br>"Turkish"<br>"Ukrainian"<br>"Vietnamese" |
| `mode` | وضع 'speed' أسرع؛ وضع 'precision' ينتج مزامنة شفاه بجودة أعلى بتكلفة مضاعفة. | STRING | نعم | "speed"<br>"precision" |
| `translate_audio_only` | استبدال المسار الصوتي فقط مع الحفاظ على حركات الفم الأصلية (بدون مزامنة شفاه). (الافتراضي: False) | BOOLEAN | لا | True<br>False |
| `speaker_count` | عدد المتحدثين في الفيديو. 0 = كشف تلقائي. (الافتراضي: 0) | INT | لا | 0 إلى 10 |
| `seed` | لا يُرسل إلى HeyGen؛ قم بتغييره لفرض إعادة التشغيل. (الافتراضي: 42) | INT | لا | 0 إلى 2147483647 |

## المخرجات

| اسم المخرج | الوصف | نوع البيانات |
|------------|-------|---------------|
| `video` | الفيديو المترجم مع استنساخ الصوت ومزامنة الشفاه المطبقة. | VIDEO |

> تم إنشاء هذه الوثيقة بواسطة الذكاء الاصطناعي. إذا وجدت أي أخطاء أو لديك اقتراحات للتحسين، فلا تتردد في المساهمة! [تحرير على GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenVideoTranslateNode/ar.md)

---
**Source fingerprint (SHA-256):** `31056060b6309b8ec28b37b353322403e173fd2862b56021392dba24e7a15f69`
