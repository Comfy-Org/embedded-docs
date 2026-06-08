عقدة Preview3D تُستخدم بشكل أساسي لمعاينة مخرجات النماذج ثلاثية الأبعاد. تستقبل هذه العقدة مدخلين: الأول هو `camera_info` القادم من عقدة Load3D، والثاني هو مسار ملف النموذج ثلاثي الأبعاد. يجب أن يكون مسار ملف النموذج موجودًا داخل مجلد `ComfyUI/output`.

**الصيغ المدعومة**
حاليًا، تدعم هذه العقدة صيغ ملفات ثلاثية الأبعاد متعددة، بما في ذلك `.gltf` و `.glb` و `.obj` و `.fbx` و `.stl`.

**تفضيلات العقد ثلاثية الأبعاد**
يمكن تكوين بعض التفضيلات ذات الصلة بالعقد ثلاثية الأبعاد في قائمة إعدادات ComfyUI. يُرجى الرجوع إلى الوثائق التالية للإعدادات المقابلة:
[قائمة الإعدادات](https://docs.comfy.org/interface/settings/3d)

## المدخلات

| اسم المعامل | الوصف | النوع |
| --- | --- | --- |
| camera_info | معلومات الكاميرا | LOAD3D_CAMERA |
| model_file | مسار ملف النموذج داخل `ComfyUI/output/` | LOAD3D_CAMERA |

## وصف منطقة اللوحة

حاليًا، تشترك العقد ذات الصلة بالرسوم ثلاثية الأبعاد في واجهة ComfyUI الأمامية في نفس مكون اللوحة، لذا فإن عملياتها الأساسية متطابقة إلى حد كبير باستثناء بعض الاختلافات الوظيفية.

> المحتوى والواجهة التاليان يعتمدان بشكل أساسي على عقدة Load3D. يُرجى الرجوع إلى واجهة العقدة الفعلية للوظائف المحددة.

تتضمن منطقة اللوحة عمليات عرض متنوعة، مثل:

- إعدادات عرض المعاينة (الشبكة، لون الخلفية، عرض المعاينة)
- التحكم في الكاميرا: مجال الرؤية (FOV)، نوع الكاميرا
- شدة الإضاءة العامة: ضبط الإضاءة
- تصدير النموذج: يدعم صيغ `GLB` و `OBJ` و `STL`
- إلخ.

![واجهة عقدة Load 3D](./asset/preview3d_canvas.jpg)

1. تحتوي على قوائم متعددة وقوائم مخفية لعقدة Load 3D
2. محور تشغيل العرض ثلاثي الأبعاد

### 1. عمليات العرض

<video controls width="640" height="360">
  <source src="https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/Load3D/asset/view_operations.mp4" type="video/mp4">
  متصفحك لا يدعم تشغيل الفيديو.
</video>

عمليات التحكم في العرض:

- النقر بزر الفأرة الأيسر + السحب: تدوير العرض
- النقر بزر الفأرة الأيمن + السحب: تحريك العرض (Pan)
- تمرير العجلة الوسطى أو النقر بزر الفأرة الأوسط + السحب: تكبير/تصغير
- محور الإحداثيات: تبديل طرق العرض

### 2. وظائف القائمة اليسرى

![القائمة](https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/Load3d/asset/menu.webp)

في منطقة المعاينة، تكون بعض قوائم عمليات العرض مخفية في القائمة. انقر على زر القائمة لتوسيع قوائم مختلفة.

- 1. المشهد (Scene): يحتوي على إعدادات شبكة نافذة المعاينة، لون الخلفية، والصورة المصغرة
- 2. النموذج (Model): وضع عرض النموذج، مادة النسيج، إعدادات الاتجاه العلوي
- 3. الكاميرا (Camera): التبديل بين العرض المتعامد والمنظوري، ضبط زاوية المنظور
- 4. الإضاءة (Light): شدة الإضاءة العامة للمشهد
- 5. التصدير (Export): تصدير النموذج إلى صيغ أخرى (GLB, OBJ, STL)

#### المشهد (Scene)

![قائمة المشهد](https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/Load3d/asset/menu_scene.webp)

توفر قائمة المشهد بعض وظائف إعدادات المشهد الأساسية:

1. إظهار/إخفاء الشبكة
2. تعيين لون الخلفية
3. النقر لرفع صورة خلفية
4. إخفاء الصورة المصغرة للمعاينة

#### النموذج (Model)

![قائمة_المشهد](https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/Load3d/asset/menu_model.webp)

توفر قائمة النموذج بعض الوظائف المتعلقة بالنموذج:

1. **الاتجاه العلوي**: تحديد المحور الذي يمثل الاتجاه العلوي للنموذج
2. **وضع المادة**: تبديل أوضاع عرض النموذج - أصلي (Original)، عادي (Normal)، إطار سلكي (Wireframe)، رسم خطي (Lineart)

#### الكاميرا (Camera)

![قائمة_النموذج_قائمة_الكاميرا](https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/Load3d/asset/menu_camera.webp)

توفر هذه القائمة التبديل بين العرض المتعامد والمنظوري، وضبط حجم زاوية المنظور:

1. **الكاميرا**: التبديل السريع بين العرض المتعامد والمنظوري
2. **مجال الرؤية (FOV)**: ضبط زاوية مجال الرؤية

#### الإضاءة (Light)

![قائمة_النموذج_قائمة_الكاميرا](https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/Load3d/asset/menu_light.webp)

من خلال هذه القائمة، يمكنك ضبط شدة الإضاءة العامة للمشهد بسرعة

#### التصدير (Export)

![قائمة_التصدير](https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/Load3d/asset/menu_export.webp)

توفر هذه القائمة إمكانية التحويل السريع وتصدير صيغ النماذج

> تم إنشاء هذه الوثيقة بواسطة الذكاء الاصطناعي. إذا وجدت أي أخطاء أو لديك اقتراحات للتحسين، فلا تتردد في المساهمة! [تحرير على GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Preview3D/ar.md)
