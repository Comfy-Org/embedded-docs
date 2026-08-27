# FishAudioVoiceSelector

```markdown
تختار عقدة Fish Audio Voice Selector صوتًا من مكتبة Fish Audio لتوليد الكلام من النص. يمكنك اختيار أحد الأصوات المعدة مسبقًا، أو اختيار "custom" لإدخال أي معرّف نموذج صوتي من fish.audio.

## المدخلات

### المدخلات العامة

| المعامل | الوصف | نوع البيانات | مطلوب | النطاق |
|-----------|-------------|-----------|----------|-------|
| `voice` | اختر صوتًا، أو 'custom' لإدخال أي معرّف نموذج صوتي من fish.audio. | DYNAMIC_COMBO | نعم | "Energetic Male (en)"<br>"Friendly Women (en)"<br>"Sarah (en)"<br>"Verity (en)"<br>"Polo (en)"<br>"Adrian (en)"<br>"E-girl (en)"<br>"Narrator (en)"<br>"Warm Conversational Voice (en)"<br>"Warm Storyteller (en)"<br>"Dramatic Character Male (en)"<br>"News Narrator (zh)"<br>"Lively Female (zh)"<br>"Gentle Female (zh)"<br>"Energetic Female (ja)"<br>"Calm Female (ja)"<br>"Calm Male (ja)"<br>"custom" |

تغطي خيارات الأصوات المعدة مسبقًا أصوات اللغة الإنجليزية (en) والصينية (zh) واليابانية (ja) ولا تتطلب أي مدخلات إضافية.

### المدخلات المخصصة

تظهر هذه المدخلات عندما يتم تعيين `voice` إلى "custom".

| المعامل | الوصف | نوع البيانات | مطلوب | النطاق |
|-----------|-------------|-----------|----------|-------|
| `voice_id` | معرّف نموذج الصوت من fish.audio، مثل المعرّف في https://fish.audio/m/<id>/. الافتراضي: سلسلة فارغة. | STRING | نعم | أي معرّف نموذج صوتي صالح من Fish Audio |

ملاحظة: عندما يتم تعيين `voice` إلى "custom"، يجب ألا يكون `voice_id` فارغًا بعد إزالة المسافات البيضاء؛ وإلا ترفع العقدة خطأ "Custom voice ID is empty.". إذا تم تمرير خيار صوت غير معروف، ترفع العقدة خطأ "Unknown voice".

## المخرجات

| اسم المخرج | الوصف | نوع البيانات |
|-------------|-------------|-----------|
| `voice` | معرّف نموذج الصوت المحدد من Fish Audio. بالنسبة للأصوات المعدة مسبقًا، يتم إرجاع معرّف الصوت المقابل من مكتبة Fish Audio؛ أما بالنسبة إلى "custom"، فيتم إرجاع قيمة `voice_id` المُدخلة. | FISHAUDIO_VOICE |
```

> تم إنشاء هذه الوثيقة بواسطة الذكاء الاصطناعي. إذا وجدت أي أخطاء أو لديك اقتراحات للتحسين، فلا تتردد في المساهمة! [تحرير على GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FishAudioVoiceSelector/ar.md)

---
**Source fingerprint (SHA-256):** `4f99a58aa7e6054f58fe84e61e4e1008b17828bd97d71ef0a4009c4de4052bbd`
