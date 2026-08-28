# تحسين الفيديو Topaz

The **Topaz Video Enhance V2** node breathes new life into video with powerful upscaling and recovery technology. It can increase the resolution of a video using different Topaz upscaler models, adjust the frame rate through frame interpolation, and apply creative or realistic enhancement settings.

## المدخلات

### المدخلات العامة

| المعامل | الوصف | نوع البيانات | إلزامي | النطاق |
| --- | --- | --- | --- | --- |
| `فيديو` | الفيديو المدخل المطلوب معالجته. يجب أن يكون بتنسيق حاوية MP4. | VIDEO | نعم | - |
| `نموذج التكبير` | نموذج الذكاء الاصطناعي المستخدم لرفع دقة الفيديو. تعتمد المعاملات الفرعية المتاحة على النموذج المحدد. يؤدي اختيار `"Disabled"` إلى تعطيل رفع الدقة. | DYNAMIC_COMBO | نعم | `"Astra 2"`<br>`"Starlight (Astra) Fast"`<br>`"Starlight (Astra) Creative"`<br>`"Starlight Precise 2.5"`<br>`"Disabled"` |
| `نموذج الاستيفاء` | نموذج الذكاء الاصطناعي المستخدم لاستيفاء الإطارات. تعتمد المعاملات الفرعية المتاحة على النموذج المحدد. يؤدي اختيار `"Disabled"` إلى تعطيل الاستيفاء. | DYNAMIC_COMBO | نعم | `"Disabled"`<br>`"apo-8"` |
| `مستوى الضغط الديناميكي` | مستوى CQP المستخدم لضغط الفيديو (الافتراضي: `"Low"`). | COMBO | لا | `"Low"`<br>`"Mid"`<br>`"High"` |

تصف الأقسام التالية المعاملات الفرعية التي تظهر لكل خيار من خيارات محددّي `upscaler_model` و`interpolation_model`. لا تُظهر خيارات `"Disabled"` أي معاملات إضافية.

### مدخلات Astra 2

| المعامل | الوصف | نوع البيانات | إلزامي | النطاق |
| --- | --- | --- | --- | --- |
| `upscaler_model.upscaler_resolution` | دقة الإخراج المستهدفة لرفع الدقة. | COMBO | نعم (عند تحديد "Astra 2") | `"FullHD (1080p)"`<br>`"4K (2160p)"` |
| `upscaler_model.creativity` | درجة الإبداع في رفع الدقة (الافتراضي: 0.5). | FLOAT | لا | 0.0 إلى 1.0 (الخطوة 0.1) |
| `upscaler_model.prompt` | موجّه وصف اختياري للمشهد (وصفي وليس توجيهيًا). يحدّ من الإدخال إلى 450 إطارًا (~15 ثانية بمعدل 30 إطارًا في الثانية) عند تعيينه (الافتراضي: فارغ). | STRING | لا | - |
| `upscaler_model.sharp` | الحدة قبل التحسين: 0.0=تمويه غاوسي، 0.5=تمرير مباشر (الافتراضي)، 1.0=شحذ USM. | FLOAT | لا | 0.0 إلى 1.0 (الخطوة 0.01) |
| `upscaler_model.realism` | يسحب الإخراج نحو الواقعية الفوتوغرافية. اتركه عند 0 لاستخدام قيمة النموذج الافتراضية (الافتراضي: 0.0). | FLOAT | لا | 0.0 إلى 1.0 (الخطوة 0.01) |

### مدخلات Starlight (Astra) Fast

| المعامل | الوصف | نوع البيانات | إلزامي | النطاق |
| --- | --- | --- | --- | --- |
| `upscaler_model.upscaler_resolution` | دقة الإخراج المستهدفة لرفع الدقة. | COMBO | نعم (عند تحديد هذا النموذج) | `"FullHD (1080p)"`<br>`"4K (2160p)"` |

### مدخلات Starlight (Astra) Creative

| المعامل | الوصف | نوع البيانات | إلزامي | النطاق |
| --- | --- | --- | --- | --- |
| `upscaler_model.upscaler_resolution` | دقة الإخراج المستهدفة لرفع الدقة. | COMBO | نعم (عند تحديد هذا النموذج) | `"FullHD (1080p)"`<br>`"4K (2160p)"` |
| `upscaler_model.creativity` | درجة الإبداع في رفع الدقة (الافتراضي: `"low"`). | COMBO | لا | `"low"`<br>`"middle"`<br>`"high"` |

### مدخلات Starlight Precise 2.5

| المعامل | الوصف | نوع البيانات | إلزامي | النطاق |
| --- | --- | --- | --- | --- |
| `upscaler_model.upscaler_resolution` | دقة الإخراج المستهدفة لرفع الدقة. | COMBO | نعم (عند تحديد هذا النموذج) | `"FullHD (1080p)"`<br>`"4K (2160p)"` |

### مدخلات apo-8

| المعامل | الوصف | نوع البيانات | إلزامي | النطاق |
| --- | --- | --- | --- | --- |
| `interpolation_model.interpolation_frame_rate` | معدل إطارات الإخراج (الافتراضي: 60). | INT | نعم (عند تحديد "apo-8") | 15 إلى 240 |
| `interpolation_model.interpolation_slowmo` | عامل الحركة البطيئة المطبق على الفيديو المدخل. على سبيل المثال، القيمة 2 تجعل الإخراج أبطأ مرتين وتضاعف المدة (الافتراضي: 1). | INT | لا | 1 إلى 16 |
| `interpolation_model.interpolation_duplicate` | تحليل الإدخال بحثًا عن الإطارات المكررة وإزالتها (الافتراضي: False). | BOOLEAN | لا | True<br>False |
| `interpolation_model.interpolation_duplicate_threshold` | حساسية الكشف عن الإطارات المكررة (الافتراضي: 0.01). | FLOAT | لا | 0.001 إلى 0.1 (الخطوة 0.001) |

**قيود مهمة:**

- يجب تفعيل واحد على الأقل من `upscaler_model` أو `interpolation_model`. إذا تم تعيين كلاهما على `"Disabled"`، تُطلق العقدة خطأً لعدم وجود شيء لمعالجته.
- يجب أن يكون الفيديو المدخل `video` بتنسيق حاوية MP4.
- يُقيَّد نموذج `"Astra 2"` بـ 9000 إطار إدخال. عند تعيين `prompt`، يكون الحد الأقصى 450 إطار إدخال (~15 ثانية بمعدل 30 إطارًا في الثانية). تُطلق العقدة خطأً إذا تجاوز الفيديو الحد المطبق.
- `upscaler_model.upscaler_resolution` مطلوب كلما تم تحديد نموذج رفع دقة غير `"Disabled"`. يستهدف `"FullHD (1080p)"` نتيجة 1080p بينما يستهدف `"4K (2160p)"` نتيجة 2160p؛ يتم حساب العرض والارتفاع الفعليين للإخراج من نسبة أبعاد الإدخال، مع تحديد أقصى ضلع طويل بـ 1920 أو 3840 بكسل على التوالي، وتقريبهما إلى عدد زوجي.
- `interpolation_model.interpolation_frame_rate` مطلوب عندما يكون `interpolation_model` هو `"apo-8"`.
- الملفات الكبيرة جدًا غير مدعومة حاليًا؛ تُقيَّد التحميلات بجزء واحد، وإلا تُطلق العقدة خطأً.
- يتم تمييز العديد من المعاملات (`sharp`, `realism`, `interpolation_slowmo`, `interpolation_duplicate`, `interpolation_duplicate_threshold`) على أنها متقدمة في واجهة المستخدم وقد تكون مخفية افتراضيًا.

## المخرجات

| اسم المخرَج | الوصف | نوع البيانات |
| --- | --- | --- |
| `video` | الفيديو المُحسَّن بعد تطبيق مرشحات رفع الدقة و/أو الاستيفاء المحددة. | VIDEO |

> تم إنشاء هذه الوثيقة بواسطة الذكاء الاصطناعي. إذا وجدت أي أخطاء أو لديك اقتراحات للتحسين، فلا تتردد في المساهمة! [تحرير على GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TopazVideoEnhanceV2/ar.md)

---
**Source fingerprint (SHA-256):** `14627dc772a6a46a645517bd34b545e0986a84561e24bdfe810b67f791ee47e3`
