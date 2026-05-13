> تم إنشاء هذه الوثيقة بواسطة الذكاء الاصطناعي. إذا وجدت أي أخطاء أو لديك اقتراحات للتحسين، فلا تتردد في المساهمة! [تحرير على GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ControlNetApplySD3/ar.md)

## المدخلات

| المعامل | نوع البيانات | إلزامي | النطاق | الوصف |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | نعم | - | التكييف الإيجابي الذي سيتم تطبيق توجيه ControlNet عليه |
| `negative` | CONDITIONING | نعم | - | التكييف السلبي الذي سيتم تطبيق توجيه ControlNet عليه |
| `control_net` | CONTROL_NET | نعم | - | نموذج ControlNet المستخدم للتوجيه |
| `vae` | VAE | نعم | - | نموذج VAE المستخدم في العملية |
| `image` | IMAGE | نعم | - | الصورة المدخلة التي سيستخدمها ControlNet كدليل توجيه |
| `strength` | FLOAT | نعم | 0.0 - 10.0 | قوة تأثير ControlNet (القيمة الافتراضية: 1.0) |
| `start_percent` | FLOAT | نعم | 0.0 - 1.0 | نقطة البداية في عملية التوليد حيث يبدأ ControlNet بالتطبيق (القيمة الافتراضية: 0.0) |
| `end_percent` | FLOAT | نعم | 0.0 - 1.0 | نقطة النهاية في عملية التوليد حيث يتوقف ControlNet عن التطبيق (القيمة الافتراضية: 1.0) |

## المخرجات

| اسم المخرج | نوع البيانات | الوصف |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | التكييف الإيجابي المعدل مع تطبيق توجيه ControlNet |
| `negative` | CONDITIONING | التكييف السلبي المعدل مع تطبيق توجيه ControlNet |

---
**Source fingerprint (SHA-256):** `7bd24b19c159374bc86a773be9b563760bfae7e10d3333596788dbc52ef2f294`
