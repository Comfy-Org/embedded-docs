# SenseNova Interleave Decode

حوِّل سجل interleave الذي يتركه SenseNova Conditioning إلى نص وصور وتفكير قابلين للاستخدام. شغِّله في نهاية الحلقة، مع تعطيل End Loop accumulate، لجمع كل ما أنتجه النموذج في تمريرة واحدة.

## المدخلات

| المعامل | الوصف | نوع البيانات | مطلوب | النطاق |
|-----------|-------------|-----------|----------|-------|
| `clip` | نموذج SenseNova CLIP المستخدم لفك ترميز الرموز المولّدة. | CLIP | نعم | - |
| `conditioning` | تهيئة interleave من SenseNova Conditioning. | CONDITIONING | نعم | - |
| `samples` | آخر latent بكسلي من KSampler، ويلزم عندما تنتهي الحلقة على طلب صورة. | LATENT | لا | - |

**القيود والسلوك:**

* يجب أن تأتي التهيئة من SenseNova Conditioning في مهمة `interleave` أو `self-correction`؛ وأي شيء آخر يؤدي إلى خطأ.
* عندما ينتظر النموذج صورة، اربط مخرَج LATENT الخاص بـ sampler بـ `samples`.
* تُستبعد الصور المرجعية الموصولة عند بداية التشغيل من المخرجات، ويتم تخطي مستهلكي الصور عندما لا تُولَّد أي صورة.

## المخرجات

| اسم المخرَج | الوصف | نوع البيانات |
|-------------|-------------|-----------|
| `text` | نص مفكوك الترميز من سجل interleave، مع استبدال علامات الصور بأسطر فارغة. | STRING |
| `images` | الصور التي ولّدها النموذج أثناء التشغيل. | IMAGE |
| `thinking` | نص استدلال النموذج، عندما ينتجه. | STRING |

> تم إنشاء هذه الوثيقة بواسطة الذكاء الاصطناعي. إذا وجدت أي أخطاء أو لديك اقتراحات للتحسين، فلا تتردد في المساهمة! [تحرير على GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SenseNovaInterleaveDecode/ar.md)

---
**Source fingerprint (SHA-256):** `62c7ded50c1348e2242319209729a17d543d80e4d01ddf173cf8b77e4fd0be50`
