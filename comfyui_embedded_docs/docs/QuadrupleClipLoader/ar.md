> تم إنشاء هذه الوثيقة بواسطة الذكاء الاصطناعي. إذا وجدت أي أخطاء أو لديك اقتراحات للتحسين، فلا تتردد في المساهمة! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QuadrupleCLIPLoader/ar.md)

محمل CLIP الرباعي، QuadrupleCLIPLoader، هو أحد العُقد الأساسية في ComfyUI، تمت إضافته أولاً لدعم نموذج HiDream الإصدار I1. إذا وجدت هذه العقدة مفقودة، حاول تحديث ComfyUI إلى أحدث إصدار لضمان دعم العقدة.

يتطلب 4 نماذج CLIP، تتوافق مع المعاملات `clip_name1`، `clip_name2`، `clip_name3`، و `clip_name4`، وسيوفر ناتج نموذج CLIP للعقد اللاحقة.

ستكتشف هذه العقدة النماذج الموجودة في مجلد `ComfyUI/models/text_encoders`،
 كما ستقرأ النماذج من المسارات الإضافية المُكونة في ملف extra_model_paths.yaml.
 في بعض الأحيان، بعد إضافة النماذج، قد تحتاج إلى **إعادة تحميل واجهة ComfyUI** للسماح لها بقراءة ملفات النماذج في المجلد المقابل.