# ModelAttentionBackend

This node lets you choose which attention backend a model uses for its attention computations. It creates a copy of the model and swaps in the attention function you select, which can affect performance or behavior. If the chosen backend is not available, it automatically falls back to PyTorch attention and logs a warning.

تسمح لك هذه العقدة باختيار الخلفية (backend) التي يستخدمها النموذج لعمليات الانتباه الخاصة به. وهي تنشئ نسخة من النموذج وتستبدل دالة الانتباه التي تختارها، مما قد يؤثر على الأداء أو السلوك. إذا لم تكن الخلفية المحددة متاحة، فإنها تتراجع تلقائيًا إلى انتباه PyTorch وتُسجّل تحذيرًا.

## المدخلات

| المعامل | الوصف | نوع البيانات | إلزامي | النطاق |
|-----------|-------------|-----------|----------|-------|
| `model` | النموذج الذي سيتم تطبيق خلفية الانتباه المحددة عليه. | MODEL | نعم |  |
| `attention` | خلفية الانتباه المستخدمة (الافتراضي: "pytorch attention"). إذا كانت الخلفية المحددة غير متاحة، يتم استخدام انتباه PyTorch كخيار احتياطي. | STRING | نعم | "pytorch attention"<br>"comfy kitchen attention" |

ملاحظة: يُدرج خيار "comfy kitchen attention" فقط عندما تكون وحدة انتباه comfy kitchen int8 متاحة في البيئة الحالية.

## المخرجات

| اسم المخرج | الوصف | نوع البيانات |
|-------------|-----------|-----------|
| `MODEL` | نسخة طبق الأصل من نموذج الإدخال مع تطبيق خلفية الانتباه المحددة. | MODEL |

> تم إنشاء هذه الوثيقة بواسطة الذكاء الاصطناعي. إذا وجدت أي أخطاء أو لديك اقتراحات للتحسين، فلا تتردد في المساهمة! [تحرير على GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelAttentionBackend/ar.md)

---
**Source fingerprint (SHA-256):** `4ba613cc0bf5b3e7f9effa895b98b3a3bd302e5d20e9d7e18d1633906c783244`
