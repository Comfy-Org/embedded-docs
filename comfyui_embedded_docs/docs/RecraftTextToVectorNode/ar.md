> تم إنشاء هذه الوثيقة بواسطة الذكاء الاصطناعي. إذا وجدت أي أخطاء أو لديك اقتراحات للتحسين، فلا تتردد في المساهمة! [تحرير على GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftTextToVectorNode/ar.md)

أنت خبير في الترجمة التقنية متخصص في توثيق عُقد ComfyUI من الإنجليزية إلى العربية.

## قواعد الترجمة

1. **المحتوى الذي يجب عدم ترجمته:**
   - أسماء المعاملات بين علامات الاقتباس الخلفية: `image`, `seed`, `model`
   - أنواع البيانات بالأحرف الكبيرة: IMAGE, STRING, INT, FLOAT, MODEL, CONDITIONING, إلخ
   - القيم في عمود Range: الأرقام، "auto"، أسماء الخيارات
   - الكود، مسارات الملفات

2. **المحتوى الذي يجب ترجمته:**
   - عناوين الأقسام: ## نظرة عامة, ## المدخلات, ## المخرجات
   - جميع النصوص الوصفية والتوضيحية
   - أوصاف المعاملات

3. **جودة الترجمة:**
   - استخدام اللغة العربية الفصحى المعاصرة
   - الحفاظ على نبرة احترافية ولكن سهلة الفهم
   - ضمان الدقة التقنية
   - استخدام المصطلحات التقنية العربية القياسية

4. **التنسيق:**
   - الحفاظ على جميع تنسيقات Markdown
   - الحفاظ على بنية الجداول
   - عدم إضافة أي ملاحظة أو رابط في بداية الوثيقة (سيتم إضافتها تلقائيًا)

الرجاء ترجمة الوثيقة التالية إلى العربية، دون تضمين الملاحظة الأولية للوثيقة:

يقوم هذا العقدة بإنشاء رسوم توضيحية متجهة بصيغة SVG بشكل متزامن بناءً على موجه نصي ودقة محددة. ترسل هذه العقدة الموجه الخاص بك إلى واجهة برمجة تطبيقات Recraft وتعيد محتوى SVG المُنشأ.

## المدخلات

| المعامل | نوع البيانات | إجباري | النطاق | الوصف |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | نعم | - | الموجه الخاص بإنشاء الصورة. (القيمة الافتراضية: "") |
| `substyle` | COMBO | نعم | `"2d_character"`<br>`"2d_gradient"`<br>`"2d_illustration"`<br>`"2d_flat_character"`<br>`"2d_flat_illustration"`<br>`"2d_art"`<br>`"2d_art_character"`<br>`"2d_pattern"`<br>`"2d_pixel_art"`<br>`"2d_cyberpunk"`<br>`"2d_engraving"`<br>`"2d_black_and_white"`<br>`"2d_ink"`<br>`"2d_sketch"`<br>`"2d_watercolor"`<br>`"2d_animation"`<br>`"2d_comic"`<br>`"2d_children_illustration"`<br>`"2d_vintage"`<br>`"2d_retro"`<br>`"2d_hand_drawn"`<br>`"2d_psychedelic"`<br>`"2d_graffiti"`<br>`"2d_ukiyo_e"`<br>`"2d_woodcut"`<br>`"2d_art_deco"`<br>`"2d_art_nouveau"`<br>`"2d_bauhaus"`<br>`"2d_constructivism"`<br>`"2d_cubism"`<br>`"2d_futurism"`<br>`"2d_glitch"`<br>`"2d_impressionism"`<br>`"2d_naive"`<br>`"2d_pointillism"`<br>`"2d_pop_art"`<br>`"2d_realism"`<br>`"2d_renaissance"`<br>`"2d_rococo"`<br>`"2d_romanticism"`<br>`"2d_surrealism"`<br>`"2d_suprematism"`<br>`"2d_symbolism"`<br>`"2d_expressionism"`<br>`"2d_abstract"`<br>`"2d_minimalism"`<br>`"2d_contemporary"`<br>`"2d_modern"`<br>`"2d_brutalism"`<br>`"2d_metaphysical"`<br>`"2d_mannerism"`<br>`"2d_baroque"`<br>`"2d_neoclassicism"`<br>`"2d_orientalism"`<br>`"2d_primitivism"`<br>`"2d_fauvism"`<br>`"2d_rayonism"`<br>`"2d_orphism"`<br>`"2d_vorticism"`<br>`"2d_dadaism"`<br>`"2d_neo_expressionism"`<br>`"2d_transavantgarde"`<br>`"2d_new_wild"`<br>`"2d_graffiti_classic"`<br>`"2d_graffiti_modern"`<br>`"2d_graffiti_wildstyle"`<br>`"2d_graffiti_bubble"`<br>`"2d_graffiti_throwup"`<br>`"2d_graffiti_tag"`<br>`"2d_graffiti_blockbuster"`<br>`"2d_graffiti_mural"`<br>`"2d_graffiti_stencil"`<br>`"2d_graffiti_3d"`<br>`"2d_graffiti_character"`<br>`"2d_graffiti_abstract"`<br>`"2d_graffiti_urban"`<br>`"2d_graffiti_neo_muralism"`<br>`"2d_graffiti_post_graffiti"`<br>`"2d_graffiti_street_art"` | النمط المحدد للرسم التوضيحي المتجه الذي سيتم استخدامه في الإنشاء. |
| `size` | COMBO | نعم | `"1024x1024"`<br>`"1024x2048"`<br>`"2048x1024"`<br>`"2048x2048"`<br>`"512x512"`<br>`"512x1024"`<br>`"1024x512"`<br>`"2048x512"`<br>`"512x2048"` | حجم الصورة المُنشأة. (القيمة الافتراضية: "1024x1024") |
| `n` | INT | نعم | 1-6 | عدد الصور المراد إنشاؤها. (القيمة الافتراضية: 1، الحد الأدنى: 1، الحد الأقصى: 6) |
| `seed` | INT | نعم | 0-18446744073709551615 | البذرة لتحديد ما إذا كان يجب إعادة تشغيل العقدة؛ النتائج الفعلية غير حتمية بغض النظر عن البذرة. (القيمة الافتراضية: 0، الحد الأدنى: 0، الحد الأقصى: 18446744073709551615) |
| `negative_prompt` | STRING | لا | - | وصف نصي اختياري للعناصر غير المرغوب فيها في الصورة. (القيمة الافتراضية: "") |
| `recraft_controls` | CONTROLS | لا | - | عناصر تحكم إضافية اختيارية في عملية الإنشاء عبر عقدة عناصر تحكم Recraft. |

**ملاحظة:** يتحكم المعامل `seed` فقط في وقت إعادة تشغيل العقدة ولكنه لا يجعل نتائج الإنشاء حتمية.

## المخرجات

| اسم المخرج | نوع البيانات | الوصف |
|-------------|-----------|-------------|
| `SVG` | SVG | الرسم التوضيحي المتجه المُنشأ بتنسيق SVG |

---
**Source fingerprint (SHA-256):** `3ac4057fa100a207c0400d0d01756899fc02261e3fb7d962fb0057e6c6519100`
