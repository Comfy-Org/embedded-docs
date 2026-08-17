# نوافذ سياق WAN (يدوي)

عقدة نوافذ سياق Wan (يدوي) تتيح لك ضبط نوافذ السياق يدويًا للنماذج الشبيهة بـ Wan مع معالجة ثنائية الأبعاد. تطبق إعدادات نوافذ السياق أثناء أخذ العينات عن طريق تحديد طول النافذة، والتداخل، وطريقة الجدولة، وتقنية الدمج، مما يمنحك التحكم في كيفية معالجة النموذج لمناطق السياق المختلفة.

## المدخلات

| المعامل | الوصف | نوع البيانات | مطلوب | النطاق |
| --- | --- | --- | --- | --- |
| `model` | النموذج الذي سيتم تطبيق نوافذ السياق عليه أثناء أخذ العينات. | MODEL | نعم | - |
| `context_length` | طول نافذة السياق بالإطارات الفعلية. يجب أن يكون 4*n + 1. (الافتراضي: 81) | INT | نعم | 1 to 16384 (step 4) |
| `context_overlap` | تداخل نافذة السياق بالإطارات الفعلية. (الافتراضي: 30) | INT | نعم | 0 or greater |
| `context_schedule` | خوارزمية جدولة تعتمد على الخطوة لنوافذ السياق. (الافتراضي: "uniform_standard") | COMBO | نعم | `"static_standard"`<br>`"uniform_standard"`<br>`"uniform_looped"`<br>`"batched"` |
| `context_stride` | خطوة نافذة السياق؛ تنطبق فقط على الجداول الموحدة. (الافتراضي: 1) | INT | نعم | 1 or greater |
| `closed_loop` | ما إذا كان سيتم إغلاق حلقة نافذة السياق؛ ينطبق فقط على الجداول الحلقية. (الافتراضي: False) | BOOLEAN | نعم | True or False |
| `fuse_method` | الطريقة المستخدمة لدمج نوافذ السياق. (الافتراضي: "pyramid") | COMBO | نعم | `"pyramid"`<br>`"gaussian"`<br>`"average"`<br>`"overlap"` |
| `freenoise` | ما إذا كان سيتم تطبيق خلط الضوضاء FreeNoise، مما يحسن مزج النوافذ. (الافتراضي: True) | BOOLEAN | نعم | True or False |
| `retain_first_frame` | الاحتفاظ بأول إطار I2V في كل نافذة سياق (قد يساعد في الاحتفاظ بالمرجع الأولي). (الافتراضي: False) | BOOLEAN | نعم | True or False |
| `split_conds_to_windows` | ما إذا كان سيتم تقسيم الشروط المتعددة (التي تم إنشاؤها بواسطة ConditionCombine) إلى كل نافذة بناءً على فهرس المنطقة. (الافتراضي: False) | BOOLEAN | نعم | True or False |

**ملاحظة:** يؤثر `context_stride` فقط على الجداول الموحدة، وينطبق `closed_loop` فقط على الجداول الحلقية. يجب أن يتبع `context_length` النمط 4n + 1. تقوم العقدة بتحويل `context_length` و `context_overlap` من الإطارات الفعلية إلى وحدات النموذج قبل تطبيقهما، مع فرض حد أدنى قدره 1 لـ `context_length` و 0 لـ `context_overlap`. المدخلات `context_stride` و `closed_loop` و `freenoise` و `split_conds_to_windows` هي خيارات متقدمة.

## المخرجات

| اسم المخرَج | الوصف | نوع البيانات |
| --- | --- | --- |
| `model` | النموذج مع تكوين نافذة السياق المطبق عليه. | MODEL |

> تم إنشاء هذه الوثيقة بواسطة الذكاء الاصطناعي. إذا وجدت أي أخطاء أو لديك اقتراحات للتحسين، فلا تتردد في المساهمة! [تحرير على GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanContextWindowsManual/ar.md)

---
**Source fingerprint (SHA-256):** `cf4927371e9d4b509f2e6e5319cd6109e3ef36da6b3faee278bcf8c906672857`
