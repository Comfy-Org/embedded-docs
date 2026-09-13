# Luma Ray 3.2 تمديد الفيديو

تُكمل عقدة Luma Ray 3.2 Extend Video عملية توليد فيديو سابقة من Luma Ray 3.2 عبر إنشاء مقطع جديد مدته 5 ثوانٍ إما بعد المقطع الأصلي (Forward) أو قبله (Backward). وصّل مخرَج `generation_id` من عقدة Luma Ray 3.2 سابقة لاستخدام ذلك المقطع كإطار بداية (Forward) أو إطار نهاية (Backward) للتمديد. تكون التمديدات دائمًا بطول 5 ثوانٍ.

## المدخلات

### المدخلات العامة

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `source_generation_id` | معرّف التوليد لفيديو Ray 3.2 السابق المراد تمديده. وصّل مخرَج `generation_id` من عقدة Luma Ray 3.2 أخرى. الافتراضي: "" (فارغ). هذه القيمة مطلوبة ويجب ألا تكون فارغة. | STRING | نعم | – |
| `الاتجاه` | الاتجاه Forward يتابع بعد المقطع السابق؛ أما Backward فيُضاف قبل المقطع السابق. يستخدم Forward المقطع المصدر كإطار بداية؛ ويستخدمه Backward كإطار نهاية. عند تحديد "Forward (continue after)" يُضاف خيار `loop`. | DYNAMIC_COMBO | نعم | "Forward (continue after)"<br>"Backward (lead-in before)" |
| `الموجه النصي` | موجّه نصي للمحتوى الجديد. الافتراضي: "" (فارغ). يجب أن يتراوح بين 1 و6000 حرف. | STRING | نعم | 1 إلى 6000 characters |
| `الدقة` | دقة الإخراج لمقطع الفيديو الممتد. الافتراضي: "720p". | COMBO | نعم | "540p"<br>"720p"<br>"1080p" |
| `البذرة` | بذرة لتحديد ما إذا كان يجب إعادة تشغيل العقدة؛ النتائج غير حتمية بغض النظر عن البذرة. الافتراضي: 0. | INT | نعم | 0 إلى 0xFFFFFFFFFFFFFFFF (18446744073709551615) |

### مدخلات Forward (continue after)

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `loop` | تكرار الفيديو الممتد بسلاسة (تمديد Forward فقط). الافتراضي: False. | BOOLEAN | لا | True<br>False |

### مدخلات Backward (lead-in before)

لا يضيف هذا الاتجاه أي معاملات إضافية.

**ملاحظة:** تكون التمديدات دائمًا 5 ثوانٍ. يتوفر المعامل `loop` فقط عندما تكون قيمة `direction` هي "Forward (continue after)"؛ عند استخدام "Backward (lead-in before)" لا يتوفر خيار `loop`. يجب أن يتراوح `prompt` بين 1 و6000 حرف. المعامل `source_generation_id` مطلوب ويجب توصيله من مخرَج `generation_id` لعقدة Luma Ray 3.2 سابقة.

## المخرجات

| Output Name | Description | Data Type |
|-------------|-------------|-----------|
| `VIDEO` | مقطع الفيديو الممتد المولّد البالغ 5 ثوانٍ. | VIDEO |
| `generation_id` | معرّف فريد لهذا التوليد، ويمكن توصيله بعقدة Luma Ray 3.2 Extend Video أخرى لتمديدات إضافية. | STRING |

> تم إنشاء هذه الوثيقة بواسطة الذكاء الاصطناعي. إذا وجدت أي أخطاء أو لديك اقتراحات للتحسين، فلا تتردد في المساهمة! [تحرير على GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaRay32ExtendVideoNode/ar.md)

---
**Source fingerprint (SHA-256):** `a67ca53d4bcb9f3fd82bc0482b579f5f7fe4bf866f8d83cb922e1082ad320057`
