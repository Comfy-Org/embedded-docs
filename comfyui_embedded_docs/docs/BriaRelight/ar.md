# BriaRelight

يغيّر هذا العقد جو الإضاءة واتجاهها في الصورة باستخدام Bria. تُعاد معالجة الصورة بواسطة Bria، لذا لا تكون النتيجة متوافقة مع الإدخال على مستوى البكسل؛ إذ يُعاد توليد الإطار بالكامل بدقة تقارب 1 ميغابكسل.

## المدخلات

### المدخلات العامة

| المعامل | الوصف | نوع البيانات | مطلوب | النطاق |
|-----------|-------------|-----------|----------|-------|
| `image` | الصورة التي سيتم تغيير إضاءتها. يتم إسقاط أي قناة ألفا قبل رفع الصورة. | IMAGE | نعم | - |
| `light_type` | جو الإضاءة المراد تطبيقه. | COMBO | نعم | `"midday"`<br>`"blue hour light"`<br>`"low-angle sunlight"`<br>`"sunrise light"`<br>`"spotlight on subject"`<br>`"overcast light"`<br>`"soft overcast daylight lighting"`<br>`"cloud-filtered lighting"`<br>`"fog-diffused lighting"`<br>`"moonlight lighting"`<br>`"starlight nighttime"`<br>`"soft bokeh lighting"`<br>`"harsh studio lighting"` |
| `light_direction` | من أين يأتي الضوء. أكثر ما يتفاعل معه هذا الإعداد هي أجواء الإضاءة الصلبة مثل midday وspotlight on subject وharsh studio lighting. | COMBO | نعم | `"front"`<br>`"side"`<br>`"bottom"`<br>`"top-down"` |
| `moderation` | إعدادات الرقابة. اختر `"true"` لإظهار خيارات الرقابة، أو `"false"` للتشغيل من دونها. | DYNAMIC_COMBO | نعم | `"false"`<br>`"true"` |

### مدخلات الرقابة

تظهر هذه الخيارات عندما تكون قيمة `moderation` مضبوطة على `"true"`.

| المعامل | الوصف | نوع البيانات | مطلوب | النطاق |
|-----------|-------------|-----------|----------|-------|
| `visual_input_moderation` | تمكّن الرقابة على المحتوى في الصورة المدخلة. الافتراضي: false. | BOOLEAN | لا | `true`<br>`false` |
| `visual_output_moderation` | تمكّن الرقابة على المحتوى في الصورة الناتجة المولّدة. الافتراضي: false. | BOOLEAN | لا | `true`<br>`false` |

ملاحظة: تعيد Bria عرض الإطار بالكامل بدقة تقارب 1 ميغابكسل، لذا لا تكون النتيجة متوافقة مع الإدخال على مستوى البكسل.

## المخرجات

| اسم المخرج | الوصف | نوع البيانات |
|-------------|-------------|-----------|
| `image` | الصورة المعاد إضاءتها التي أرجعتها Bria. | IMAGE |
| `structured_prompt` | وصف منظم للصورة المعدّلة، لتعديل لاحق باستخدام Bria FIBO Image Edit. | STRING |

> تم إنشاء هذه الوثيقة بواسطة الذكاء الاصطناعي. إذا وجدت أي أخطاء أو لديك اقتراحات للتحسين، فلا تتردد في المساهمة! [تحرير على GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaRelight/ar.md)

---
**Source fingerprint (SHA-256):** `21fbe2186c99a7e8d99d5659ac25c3ab1a757492916dba4135487d4b293cb4f6`
