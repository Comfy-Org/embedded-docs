# Google Gemini

This node allows users to interact with Google's Gemini AI models to generate text responses. You can provide multiple types of inputs including text, images, audio, video, and files as context for the model to generate more relevant and meaningful responses. The node handles all API communication and response parsing automatically.

**Note:** This node is marked as deprecated in the source code.

## Inputs

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `مطالبة` | مدخلات نصية للنموذج تُستخدم لتوليد استجابة. يمكنك تضمين تعليمات مفصلة أو أسئلة أو سياق للنموذج. الافتراضي: سلسلة فارغة. | STRING | نعم | - |
| `نموذج` | نموذج Gemini المستخدم لتوليد الاستجابات. الافتراضي: gemini-3-1-pro. | COMBO | نعم | "gemini-2.5-pro"<br>"gemini-2.5-flash"<br>"gemini-3-pro-preview"<br>"gemini-3-1-pro"<br>"gemini-3-1-flash-lite" |
| `بذرة` | عندما يتم تثبيت البذرة (seed) على قيمة محددة، يبذل النموذج قصارى جهده لتقديم نفس الاستجابة للطلبات المتكررة. ومع ذلك، لا يُضمن إخراج حتمي تمامًا. كما أن تغيير النموذج أو إعدادات المعلمات، مثل درجة الحرارة، قد يسبب اختلافات في الاستجابة حتى عند استخدام نفس قيمة البذرة. افتراضيًا، يتم استخدام قيمة بذرة عشوائية. الافتراضي: 42. | INT | نعم | 0 إلى 18446744073709551615 |
| `صور` | صورة (صور) اختيارية لاستخدامها كسياق للنموذج. لتضمين عدة صور، يمكنك استخدام عقدة Batch Images. الافتراضي: لا شيء. | IMAGE | لا | - |
| `صوت` | صوت اختياري لاستخدامه كسياق للنموذج. الافتراضي: لا شيء. | AUDIO | لا | - |
| `فيديو` | فيديو اختياري لاستخدامه كسياق للنموذج. الافتراضي: لا شيء. | VIDEO | لا | - |
| `ملفات` | ملف (ملفات) اختيارية لاستخدامها كسياق للنموذج. يقبل مدخلات من عقدة Gemini Generate Content Input Files. الافتراضي: لا شيء. | GEMINI_INPUT_FILES | لا | - |
| `system_prompt` | تعليمات أساسية تتحكم في سلوك الذكاء الاصطناعي. الافتراضي: سلسلة فارغة. هذه معلمة متقدمة. | STRING | لا | - |

تُستخدم جميع الصور المتصلة كسياق. عند توفير أكثر من 10 صور، يتم رفع أول 10 صور كمراجع ملفات، بينما تُرسل الصور المتبقية مباشرةً إلى الواجهة البرمجية (API).

## Outputs

| Output Name | Description | Data Type |
|-------------|-------------|-----------|
| `STRING` | الاستجابة النصية التي ينشئها نموذج Gemini. إذا لم يُنتج النموذج أي نص، تُرجع العقدة "استجابة فارغة من نموذج Gemini...". | STRING |

> تم إنشاء هذه الوثيقة بواسطة الذكاء الاصطناعي. إذا وجدت أي أخطاء أو لديك اقتراحات للتحسين، فلا تتردد في المساهمة! [تحرير على GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiNode/ar.md)

---
**Source fingerprint (SHA-256):** `d1c53a5d80182085a36302867c8875df696adec6aaea9a9519a21bd6b9543d8f`
