> تم إنشاء هذه الوثيقة بواسطة الذكاء الاصطناعي. إذا وجدت أي أخطاء أو لديك اقتراحات للتحسين، فلا تتردد في المساهمة! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftStyleV3DigitalIllustration/ar.md)

يُعدّد هذا العقد أسلوبًا للاستخدام مع واجهة برمجة تطبيقات Recraft، حيث يختار تحديدًا أسلوب "digital_illustration". يتيح لك اختيار أسلوب فرعي اختياري لتحسين التوجيه الفني للصورة المُنشأة بشكل أكبر.

## المدخلات

| المعامل | نوع البيانات | إلزامي | النطاق | الوصف |
|-----------|-----------|----------|-------|-------------|
| `النمط الفرعي` | STRING | لا | `"digital_illustration"`<br>`"digital_illustration_anime"`<br>`"digital_illustration_cartoon"`<br>`"digital_illustration_comic"`<br>`"digital_illustration_concept_art"`<br>`"digital_illustration_fantasy"`<br>`"digital_illustration_futuristic"`<br>`"digital_illustration_graffiti"`<br>`"digital_illustration_graphic_novel"`<br>`"digital_illustration_hyperrealistic"`<br>`"digital_illustration_ink"`<br>`"digital_illustration_manga"`<br>`"digital_illustration_minimalist"`<br>`"digital_illustration_pixel_art"`<br>`"digital_illustration_pop_art"`<br>`"digital_illustration_retro"`<br>`"digital_illustration_sci_fi"`<br>`"digital_illustration_sticker"`<br>`"digital_illustration_street_art"`<br>`"digital_illustration_surreal"`<br>`"digital_illustration_vector"` | أسلوب فرعي اختياري لتحديد نوع معين من الرسم الرقمي التوضيحي. إذا لم يتم تحديده، يتم استخدام الأسلوب الأساسي "digital_illustration". |

## المخرجات

| اسم المخرج | نوع البيانات | الوصف |
|-------------|-----------|-------------|
| `recraft_style` | STYLEV3 | كائن أسلوب مُعدّ يحتوي على أسلوب "digital_illustration" المحدد والأسلوب الفرعي الاختياري، وجاهز ليتم تمريره إلى عُقد واجهة برمجة تطبيقات Recraft الأخرى. |
