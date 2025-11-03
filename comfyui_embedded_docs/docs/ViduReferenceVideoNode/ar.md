> تم إنشاء هذه الوثيقة بواسطة الذكاء الاصطناعي. إذا وجدت أي أخطاء أو لديك اقتراحات للتحسين، فلا تتردد في المساهمة! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ViduReferenceVideoNode/ar.md)

تُنشئ عقدة Vidu Reference Video مقاطع فيديو من صور مرجعية متعددة وموجه نصي. تستخدم العقدة نماذج الذكاء الاصطناعي لإنشاء محتوى فيديو متناسق بناءً على الصور المقدمة والوصف. تدعم العقدة إعدادات فيديو متنوعة تشمل المدة، ونسبة الأبعاد، والدقة، والتحكم في الحركة.

## المدخلات

| المعامل | نوع البيانات | مطلوب | النطاق | الوصف |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | نعم | `"vidu_q1"`<br>`"vidu_q2"`<br>`"vidu_q3"`<br>`"vidu_q4"`<br>`"vidu_q5"`<br>`"vidu_q6"`<br>`"vidu_q7"`<br>`"vidu_q8"`<br>`"vidu_q9"`<br>`"vidu_q10"`<br>`"vidu_q11"`<br>`"vidu_q12"`<br>`"vidu_q13"`<br>`"vidu_q14"`<br>`"vidu_q15"`<br>`"vidu_q16"`<br>`"vidu_q17"`<br>`"vidu_q18"`<br>`"vidu_q19"`<br>`"vidu_q20"`<br>`"vidu_q21"`<br>`"vidu_q22"`<br>`"vidu_q23"`<br>`"vidu_q24"`<br>`"vidu_q25"`<br>`"vidu_q26"`<br>`"vidu_q27"`<br>`"vidu_q28"`<br>`"vidu_q29"`<br>`"vidu_q30"`<br>`"vidu_q31"`<br>`"vidu_q32"`<br>`"vidu_q33"`<br>`"vidu_q34"`<br>`"vidu_q35"`<br>`"vidu_q36"`<br>`"vidu_q37"`<br>`"vidu_q38"`<br>`"vidu_q39"`<br>`"vidu_q40"`<br>`"vidu_q41"`<br>`"vidu_q42"`<br>`"vidu_q43"`<br>`"vidu_q44"`<br>`"vidu_q45"`<br>`"vidu_q46"`<br>`"vidu_q47"`<br>`"vidu_q48"`<br>`"vidu_q49"`<br>`"vidu_q50"`<br>`"vidu_q51"`<br>`"vidu_q52"`<br>`"vidu_q53"`<br>`"vidu_q54"`<br>`"vidu_q55"`<br>`"vidu_q56"`<br>`"vidu_q57"`<br>`"vidu_q58"`<br>`"vidu_q59"`<br>`"vidu_q60"`<br>`"vidu_q61"`<br>`"vidu_q62"`<br>`"vidu_q63"`<br>`"vidu_q64"`<br>`"vidu_q65"`<br>`"vidu_q66"`<br>`"vidu_q67"`<br>`"vidu_q68"`<br>`"vidu_q69"`<br>`"vidu_q70"`<br>`"vidu_q71"`<br>`"vidu_q72"`<br>`"vidu_q73"`<br>`"vidu_q74"`<br>`"vidu_q75"`<br>`"vidu_q76"`<br>`"vidu_q77"`<br>`"vidu_q78"`<br>`"vidu_q79"`<br>`"vidu_q80"`<br>`"vidu_q81"`<br>`"vidu_q82"`<br>`"vidu_q83"`<br>`"vidu_q84"`<br>`"vidu_q85"`<br>`"vidu_q86"`<br>`"vidu_q87"`<br>`"vidu_q88"`<br>`"vidu_q89"`<br>`"vidu_q90"`<br>`"vidu_q91"`<br>`"vidu_q92"`<br>`"vidu_q93"`<br>`"vidu_q94"`<br>`"vidu_q95"`<br>`"vidu_q96"`<br>`"vidu_q97"`<br>`"vidu_q98"`<br>`"vidu_q99"`<br>`"vidu_q100"` | اسم النموذج المستخدم في إنشاء الفيديو (الافتراضي: "vidu_q1") |
| `images` | IMAGE | نعم | - | الصور المستخدمة كمراجع لإنشاء فيديو بعناصر متناسقة (الحد الأقصى 7 صور) |
| `prompt` | STRING | نعم | - | وصف نصي لإنشاء الفيديو |
| `duration` | INT | لا | 5-5 | مدة الفيديو الناتج بالثواني (الافتراضي: 5) |
| `seed` | INT | لا | 0-2147483647 | البذرة المستخدمة في إنشاء الفيديو (0 للقيمة العشوائية) (الافتراضي: 0) |
| `aspect_ratio` | COMBO | لا | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"`<br>`"21:9"`<br>`"9:21"` | نسبة أبعاد الفيديو الناتج (الافتراضي: "16:9") |
| `resolution` | COMBO | لا | `"480p"`<br>`"720p"`<br>`"1080p"`<br>`"1440p"`<br>`"2160p"` | القيم المدعومة قد تختلف حسب النموذج والمدة (الافتراضي: "1080p") |
| `movement_amplitude` | COMBO | لا | `"auto"`<br>`"low"`<br>`"medium"`<br>`"high"` | سعة حركة العناصر في الإطار (الافتراضي: "auto") |

**القيود والحدود:**

- حقل `prompt` مطلوب ولا يمكن أن يكون فارغًا
- الحد الأقصى المسموح به هو 7 صور للاستخدام كمراجع
- يجب أن تكون نسبة أبعاد كل صورة بين 1:4 و 4:1
- يجب أن يكون الحد الأدنى لأبعاد كل صورة 128x128 بكسل
- المدة ثابتة عند 5 ثوانٍ

## المخرجات

| اسم المخرج | نوع البيانات | الوصف |
|-------------|-----------|-------------|
| `output` | VIDEO | الفيديو المُنشأ بناءً على الصور المرجعية والموجه النصي |