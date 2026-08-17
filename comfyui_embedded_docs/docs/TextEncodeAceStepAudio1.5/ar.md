# TextEncodeAceStepAudio1.5

عقدة **TextEncodeAceStepAudio1.5** تحضّر البيانات الوصفية المتعلقة بالنص والصوت لاستخدامها مع نموذج **AceStepAudio 1.5**. تأخذ وسومًا وصفية، وكلمات أغنية، ومعاملات موسيقية، ثم تستخدم نموذج CLIP لتحويلها إلى تنسيق تكييف (conditioning) مناسب لتوليد الصوت.

## المدخلات

| المعامل | الوصف | نوع البيانات | مطلوب | النطاق |
| --- | --- | --- | --- | --- |
| `clip` | نموذج CLIP المستخدم لتقطيع النص المدخل وترميزه. | CLIP | نعم | N/A |
| `tags` | وسوم وصفية للصوت، مثل النوع أو المزاج أو الآلات الموسيقية. يدعم الإدخال متعدد الأسطر والموجهات الديناميكية. | STRING | نعم | N/A |
| `lyrics` | كلمات الأغنية للمقطع الصوتي. يدعم الإدخال متعدد الأسطر والموجهات الديناميكية. | STRING | نعم | N/A |
| `seed` | قيمة بذرة عشوائية لتوليد قابل لإعادة الإنتاج. يحتوي على أداة تحكم بعد التوليد (control_after_generate). القيمة الافتراضية: 0. | INT | لا | 0 إلى 18446744073709551615 |
| `bpm` | عدد النغمات في الدقيقة (BPM) للصوت المُولَّد. القيمة الافتراضية: 120. | INT | لا | 10 إلى 300 |
| `duration` | المدة المطلوبة للصوت بالثواني. القيمة الافتراضية: 120.0. | FLOAT | لا | 0.0 إلى 2000.0 |
| `timesignature` | التوقيع الزمني الموسيقي. | COMBO | لا | `"2"`<br>`"3"`<br>`"4"`<br>`"6"` |
| `language` | لغة النص المدخل. القيمة الافتراضية: "en". | COMBO | لا | `"ar"`<br>`"az"`<br>`"bg"`<br>`"bn"`<br>`"ca"`<br>`"cs"`<br>`"da"`<br>`"de"`<br>`"el"`<br>`"en"`<br>`"es"`<br>`"fa"`<br>`"fi"`<br>`"fr"`<br>`"he"`<br>`"hi"`<br>`"hr"`<br>`"ht"`<br>`"hu"`<br>`"id"`<br>`"is"`<br>`"it"`<br>`"ja"`<br>`"ko"`<br>`"la"`<br>`"lt"`<br>`"ms"`<br>`"ne"`<br>`"nl"`<br>`"no"`<br>`"pa"`<br>`"pl"`<br>`"pt"`<br>`"ro"`<br>`"ru"`<br>`"sa"`<br>`"sk"`<br>`"sr"`<br>`"sv"`<br>`"sw"`<br>`"ta"`<br>`"te"`<br>`"th"`<br>`"tl"`<br>`"tr"`<br>`"uk"`<br>`"ur"`<br>`"vi"`<br>`"yue"`<br>`"zh"`<br>`"unknown"` |
| `keyscale` | المفتاح الموسيقي والسلّم (كبير أو صغير). | COMBO | لا | `"C major"`<br>`"C# major"`<br>`"Db major"`<br>`"D major"`<br>`"D# major"`<br>`"Eb major"`<br>`"E major"`<br>`"F major"`<br>`"F# major"`<br>`"Gb major"`<br>`"G major"`<br>`"G# major"`<br>`"Ab major"`<br>`"A major"`<br>`"A# major"`<br>`"Bb major"`<br>`"B major"`<br>`"C minor"`<br>`"C# minor"`<br>`"Db minor"`<br>`"D minor"`<br>`"D# minor"`<br>`"Eb minor"`<br>`"E minor"`<br>`"F minor"`<br>`"F# minor"`<br>`"Gb minor"`<br>`"G minor"`<br>`"G# minor"`<br>`"Ab minor"`<br>`"A minor"`<br>`"A# minor"`<br>`"Bb minor"`<br>`"B minor"` |
| `generate_audio_codes` | تفعيل نموذج اللغة الكبير (LLM) الذي يولّد أكواد الصوت. قد يكون هذا بطيئًا ولكنه سيزيد من جودة الصوت المُولَّد. أوقف تشغيله إذا كنت تقدم للنموذج مرجعًا صوتيًا. القيمة الافتراضية: True. | BOOLEAN | لا | N/A |
| `cfg_scale` | مقياس التوجيه بدون مصنف (classifier-free guidance). القيم الأعلى تجعل المخرجات تتبع الموجه بشكل أدق. القيمة الافتراضية: 2.0. | FLOAT | لا | 0.0 إلى 100.0 |
| `temperature` | درجة حرارة أخذ العينات. القيم الأقل تجعل المخرجات أكثر حتمية. القيمة الافتراضية: 0.85. | FLOAT | لا | 0.0 إلى 2.0 |
| `top_p` | احتمال أخذ العينات النووي (top-p). القيمة الافتراضية: 0.9. | FLOAT | لا | 0.0 إلى 2000.0 |
| `top_k` | عدد الرموز ذات الاحتمالية الأعلى التي يتم أخذها في الاعتبار (top-k). القيمة الافتراضية: 0. | INT | لا | 0 إلى 100 |
| `min_p` | الحد الأدنى لعتبة الاحتمالية لأخذ عينات الرموز (min-p). القيمة الافتراضية: 0.000. | FLOAT | لا | 0.0 إلى 1.0 |

## المخرجات

| اسم المخرَج | الوصف | نوع البيانات |
| --- | --- | --- |
| `CONDITIONING` | بيانات التكييف، التي تحتوي على النص المرمّز ومعاملات الصوت لنموذج AceStepAudio 1.5. | CONDITIONING |

> تم إنشاء هذه الوثيقة بواسطة الذكاء الاصطناعي. إذا وجدت أي أخطاء أو لديك اقتراحات للتحسين، فلا تتردد في المساهمة! [تحرير على GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeAceStepAudio1.5/ar.md)

---
**Source fingerprint (SHA-256):** `4bc97ec6220514b71fafde610339f2dca4ded26f68b541ed43ea492f127321f8`
