# تحميل CLIP

تقوم عقدة CLIPLoader بتحميل نموذج مُشفّر نصي (CLIP أو T5 أو ما شابه) من ملف، مما يجعله متاحًا للاستخدام في عقد أخرى تحتاج إلى تحويل مطالبات النص إلى تمثيلات رقمية. وهي تدعم مجموعة واسعة من معماريات النماذج، ويتطلب كل منها نوع مُشفّر محددًا.

## المدخلات

| المعامل | الوصف | نوع البيانات | مطلوب | النطاق |
|-----------|-------------|-----------|----------|-------|
| `اسم CLIP` | اسم ملف نموذج مُشفّر النص المراد تحميله. يجب أن يكون ملفًا موجودًا في دليل `ComfyUI/models/text_encoders/`. | STRING | نعم | قائمة الملفات الموجودة في مجلد `text_encoders` |
| `النوع` | نوع معمارية النموذج الذي يتم تحميله. يحدد هذا أي متغير مُشفّر محدد لاستخدامه (الافتراضي: `"stable_diffusion"`). | COMBO | نعم | `"stable_diffusion"`<br>`"stable_cascade"`<br>`"sd3"`<br>`"stable_audio"`<br>`"mochi"`<br>`"ltxv"`<br>`"pixart"`<br>`"cosmos"`<br>`"lumina2"`<br>`"wan"`<br>`"hidream"`<br>`"chroma"`<br>`"ace"`<br>`"omnigen2"`<br>`"qwen_image"`<br>`"hunyuan_image"`<br>`"flux2"`<br>`"ovis"`<br>`"longcat_image"`<br>`"cogvideox"`<br>`"lens"`<br>`"pixeldit"`<br>`"ideogram4"`<br>`"boogu"`<br>`"krea2"`<br>`"joyimage"`<br>`"mage"`<br>`"minimax"`<br>`"yue2"` |
| `الجهاز` | الجهاز الذي سيتم تحميل النموذج عليه. يستخدم `"default"` وحدة معالجة الرسومات (GPU) إذا كانت متاحة، بينما يفرض `"cpu"` التحميل على وحدة المعالجة المركزية (CPU). هذا خيار متقدم (الافتراضي: `"default"`). | COMBO | لا | `"default"`<br>`"cpu"` |

### تعيينات النوع إلى المُشفّر المدعومة

يحدد المعامل `type` المُشفّر الصحيح لمعمارية نموذج معينة. فيما يلي التعيينات الشائعة:

| النوع | المُشفّر |
|------|---------|
| stable_diffusion | clip-l |
| stable_cascade | clip-g |
| sd3 | t5 xxl / clip-g / clip-l |
| stable_audio | t5 base |
| mochi | t5 xxl |
| cogvideox | t5 xxl (226-token padding) |
| cosmos | old t5 xxl |
| lumina2 | gemma 2 2B |
| wan | umt5 xxl |
| hidream | llama-3.1 (recommended) or t5 |
| omnigen2 | qwen vl 2.5 3B |
| joyimage | qwen3-vl 8B |
| lens | gpt-oss-20b |
| pixeldit | gemma 2 2B elm |
| minimax | MiniMax H3 Qwen3-VL or Music3 Qwen/RVQ |

## المخرجات

| اسم المخرج | الوصف | نوع البيانات |
|-------------|-------------|-----------|
| `CLIP` | نموذج مُشفّر النص المحمّل، جاهز للاتصال بعقد أخرى لتشفير النص والتكييف. | CLIP |

> تم إنشاء هذه الوثيقة بواسطة الذكاء الاصطناعي. إذا وجدت أي أخطاء أو لديك اقتراحات للتحسين، فلا تتردد في المساهمة! [تحرير على GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPLoader/ar.md)

---
**Source fingerprint (SHA-256):** `6df608d500520d9414acd82d9fd509b1e211a8385202cefd5579e8a8f397bc64`
