# RecraftStyleV3VectorIllustrationNode

هذا العقد يهيئ نمطًا لاستخدامه مع واجهة برمجة تطبيقات Recraft، وتحديدًا اختيار نمط `vector_illustration`. يتيح لك اختيار نمط فرعي أكثر تحديدًا ضمن هذه الفئة، اختياريًا. يُخرج العقد كائن تهيئة للنمط يمكن تمريره إلى عقد أخرى خاصة بواجهة Recraft.

## المدخلات

| المعامل | الوصف | نوع البيانات | مطلوب | النطاق |
|---------|-------|---------------|-------|--------|
| `substyle` | نمط فرعي اختياري وأكثر تحديدًا ضمن فئة `vector_illustration`. إذا لم يتم تحديده، يُستخدم نمط `vector_illustration` الأساسي. | COMBO | لا | `"vector_illustration"`<br>`"vector_illustration_flat"`<br>`"vector_illustration_3d"`<br>`"vector_illustration_hand_drawn"`<br>`"vector_illustration_retro"`<br>`"vector_illustration_modern"`<br>`"vector_illustration_abstract"`<br>`"vector_illustration_geometric"`<br>`"vector_illustration_organic"`<br>`"vector_illustration_minimalist"`<br>`"vector_illustration_detailed"`<br>`"vector_illustration_colorful"`<br>`"vector_illustration_monochrome"`<br>`"vector_illustration_grayscale"`<br>`"vector_illustration_pastel"`<br>`"vector_illustration_vibrant"`<br>`"vector_illustration_muted"`<br>`"vector_illustration_warm"`<br>`"vector_illustration_cool"`<br>`"vector_illustration_neutral"`<br>`"vector_illustration_bold"`<br>`"vector_illustration_subtle"`<br>`"vector_illustration_playful"`<br>`"vector_illustration_serious"`<br>`"vector_illustration_elegant"`<br>`"vector_illustration_rustic"`<br>`"vector_illustration_urban"`<br>`"vector_illustration_nature"`<br>`"vector_illustration_fantasy"`<br>`"vector_illustration_sci_fi"`<br>`"vector_illustration_historical"`<br>`"vector_illustration_futuristic"`<br>`"vector_illustration_whimsical"`<br>`"vector_illustration_surreal"`<br>`"vector_illustration_realistic"`<br>`"vector_illustration_stylized"`<br>`"vector_illustration_cartoony"`<br>`"vector_illustration_anime"`<br>`"vector_illustration_comic"`<br>`"vector_illustration_pixel"`<br>`"vector_illustration_low_poly"`<br>`"vector_illustration_high_poly"`<br>`"vector_illustration_isometric"`<br>`"vector_illustration_orthographic"`<br>`"vector_illustration_perspective"`<br>`"vector_illustration_2d"`<br>`"vector_illustration_2.5d"`<br>`"vector_illustration_4d"` |

## المخرجات

| اسم المخرج | الوصف | نوع البيانات |
|------------|-------|--------------|
| `recraft_style` | كائن تهيئة نمط خاص بواجهة برمجة تطبيقات Recraft يحتوي على نمط `vector_illustration` المحدد والنمط الفرعي الاختياري. يمكن توصيله بعقد أخرى خاصة بـ Recraft. | STYLEV3 |

> تم إنشاء هذه الوثيقة بواسطة الذكاء الاصطناعي. إذا وجدت أي أخطاء أو لديك اقتراحات للتحسين، فلا تتردد في المساهمة! [تحرير على GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftStyleV3VectorIllustrationNode/ar.md)

---
**Source fingerprint (SHA-256):** `e88e7ea35b18acb55ec59814981cb36451d922d3287d23dcdb504289ea9f541b`
