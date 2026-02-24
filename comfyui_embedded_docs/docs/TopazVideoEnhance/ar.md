> تم إنشاء هذه الوثيقة بواسطة الذكاء الاصطناعي. إذا وجدت أي أخطاء أو لديك اقتراحات للتحسين، فلا تتردد في المساهمة! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TopazVideoEnhance/ar.md)

يستخدم عقد Topaz Video Enhance واجهة برمجة تطبيقات خارجية لتحسين جودة الفيديو. يمكنه رفع دقة الفيديو، وزيادة معدل الإطارات من خلال الاستيفاء، وتطبيق الضغط. يعالج العقد فيديو إدخال بتنسيق MP4 ويعيد نسخة محسنة بناءً على الإعدادات المحددة.

## المدخلات

| المعامل | نوع البيانات | مطلوب | النطاق | الوصف |
|-----------|-----------|----------|-------|-------------|
| `video` | VIDEO | نعم | - | ملف الفيديو المدخل المراد تحسينه. |
| `upscaler_enabled` | BOOLEAN | نعم | - | يُفعِّل أو يُعطِّل ميزة رفع دقة الفيديو (القيمة الافتراضية: True). |
| `upscaler_model` | COMBO | نعم | `"Proteus v3"`<br>`"Artemis v13"`<br>`"Artemis v14"`<br>`"Artemis v15"`<br>`"Gaia v6"`<br>`"Theia v3"`<br>`"Starlight (Astra) Creative"`<br>`"Starlight (Astra) Optimized"`<br>`"Starlight (Astra) Balanced"`<br>`"Starlight (Astra) Quality"`<br>`"Starlight (Astra) Speed"` | نموذج الذكاء الاصطناعي المستخدم لرفع دقة الفيديو. |
| `upscaler_resolution` | COMBO | نعم | `"FullHD (1080p)"`<br>`"4K (2160p)"` | الدقة المستهدفة للفيديو بعد رفع الدقة. |
| `upscaler_creativity` | COMBO | لا | `"low"`<br>`"middle"`<br>`"high"` | مستوى الإبداع (ينطبق فقط على Starlight (Astra) Creative). (القيمة الافتراضية: "low") |
| `interpolation_enabled` | BOOLEAN | لا | - | يُفعِّل أو يُعطِّل ميزة استيفاء الإطارات (القيمة الافتراضية: False). |
| `interpolation_model` | COMBO | لا | `"apo-8"` | النموذج المستخدم لاستيفاء الإطارات (القيمة الافتراضية: "apo-8"). |
| `interpolation_slowmo` | INT | لا | 1 إلى 16 | عامل الحركة البطيئة المطبق على فيديو الإدخال. على سبيل المثال، القيمة 2 تجعل المخرجات أبطأ مرتين وتضاعف المدة. (القيمة الافتراضية: 1) |
| `interpolation_frame_rate` | INT | لا | 15 إلى 240 | معدل إطارات المخرجات. (القيمة الافتراضية: 60) |
| `interpolation_duplicate` | BOOLEAN | لا | - | تحليل الإدخال للبحث عن إطارات مكررة وإزالتها. (القيمة الافتراضية: False) |
| `interpolation_duplicate_threshold` | FLOAT | لا | 0.001 إلى 0.1 | حساسية الكشف عن الإطارات المكررة. (القيمة الافتراضية: 0.01) |
| `dynamic_compression_level` | COMBO | لا | `"Low"`<br>`"Mid"`<br>`"High"` | مستوى CQP. (القيمة الافتراضية: "Low") |

**ملاحظة:** يجب تفعيل ميزة تحسين واحدة على الأقل. سيُظهر العقد خطأً إذا تم تعيين كل من `upscaler_enabled` و `interpolation_enabled` إلى `False`. يجب أن يكون فيديو الإدخال بتنسيق MP4.

## المخرجات

| اسم المخرج | نوع البيانات | الوصف |
|-------------|-----------|-------------|
| `video` | VIDEO | ملف الفيديو المحسَّن الناتج. |
