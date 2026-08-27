# ClipLoader

عقدة CLIPLoader تقوم بتحميل نموذج مشفّر نصوص (CLIP أو T5 أو ما شابه) من ملف، وتجعله متاحًا للاستخدام في العُقد الأخرى التي تحتاج إلى تحويل مطالبات النصوص إلى تمثيلات رقمية. وهي تدعم مجموعة واسعة من بنى النماذج، ويتطلب كلٌّ منها نوعًا محددًا من المشفّرات.

## المدخلات

| المعامل | الوصف | نوع البيانات | إلزامي | النطاق |
|-----------|-------------|-----------|----------|---------|
| `اسم CLIP` | اسم ملف نموذج مشفّر النصوص المراد تحميله. يجب أن يكون ملفًا موجودًا داخل المجلد `ComfyUI/models/text_encoders/`. | STRING | نعم | قائمة الملفات الموجودة في مجلد `text_encoders` |
| `النوع` | نوع بنية النموذج الذي يتم تحميله. يحدد هذا المتغير أيّ نسخة مشفّر محددة سيتم استخدامها (الافتراضي: `"stable_diffusion"`). | COMBO | نعم | `"stable_diffusion"`<br>`"stable_cascade"`<br>`"sd3"`<br>`"stable_audio"`<br>`"mochi"`<br>`"ltxv"`<br>`"pixart"`<br>`"cosmos"`<br>`"lumina2"`<br>`"wan"`<br>`"hidream"`<br>`"chroma"`<br>`"ace"`<br>`"omnigen2"`<br>`"qwen_image"`<br>`"hunyuan_image"`<br>`"flux2"`<br>`"ovis"`<br>`"longcat_image"`<br>`"cogvideox"`<br>`"lens"`<br>`"pixeldit"`<br>`"ideogram4"`<br>`"boogu"`<br>`"krea2"`<br>`"joyimage"`<br>`"mage"`<br>`"minimax"` |
| `الجهاز` | الجهاز الذي سيتم تحميل النموذج عليه. تستخدم القيمة `"default"` وحدة معالجة الرسومات (GPU) إذا كانت متوفرة، بينما تفرض القيمة `"cpu"` التحميل عبر وحدة المعالجة المركزية (CPU). هذا خيار متقدم (الافتراضي: `"default"`). | COMBO | لا | `"default"`<br>`"cpu"` |

### الاقترانات المدعومة بين النوع والمشفّر

تحدد معلمة `type` المشفّر الصحيح لبنية نموذج معينة. فيما يلي الاقترانات الشائعة:

| النوع | المشفّر |
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
| hidream | llama-3.1 (موصى به) أو t5 |
| omnigen2 | qwen vl 2.5 3B |
| joyimage | qwen3-vl 8B |
| lens | gpt-oss-20b |
| pixeldit | gemma 2 2B elm |
| minimax | MiniMax H3 Qwen3-VL أو Music3 Qwen/RVQ |

## المخرجات

| اسم المخرَج | الوصف | نوع البيانات |
|-------------|-------------|-----------|
| `clip` | نموذج مشفّر النصوص المُحمَّل، وجاهز للاتصال بالعُقد الأخرى لترميز النصوص والتكييف. | CLIP |

> تم إنشاء هذه الوثيقة بواسطة الذكاء الاصطناعي. إذا وجدت أي أخطاء أو لديك اقتراحات للتحسين، فلا تتردد في المساهمة! [تحرير على GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ClipLoader/ar.md)

---
**Source fingerprint (SHA-256):** `7c1586d01410d319468f7c8c153ef0717280804add868ba57bff0c6539fb5dd9`
