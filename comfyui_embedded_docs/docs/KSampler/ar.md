> تم إنشاء هذه الوثيقة بواسطة الذكاء الاصطناعي. إذا وجدت أي أخطاء أو لديك اقتراحات للتحسين، فلا تتردد في المساهمة! [تحرير على GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KSampler/ar.md)

يعمل مُحوّل العيّنات (KSampler) على النحو التالي: فهو يُعدّل معلومات الصورة الكامنة الأصلية المُقدّمة بناءً على نموذج مُحدّد وشروط إيجابية وسلبية.
أولاً، يُضيف تشويشاً إلى بيانات الصورة الأصلية وفقاً لقيمتَي **البذرة (seed)** و**قوة إزالة التشويش (denoise strength)** المُحدّدتَين، ثم يُدخل **النموذج (Model)** المُعدّ مُسبقاً مع شروط التوجيه **الإيجابية (positive)** و**السلبية (negative)** لتوليد الصورة.

## المدخلات

| اسم المُعامل | نوع البيانات | إلزامي | القيمة الافتراضية | النطاق/الخيارات | الوصف |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `Model` | checkpoint | نعم | لا يوجد | - | النموذج المُدخل المُستخدم في عملية إزالة التشويش |
| `seed` | Int | نعم | 0 | 0 ~ 18446744073709551615 | يُستخدم لتوليد تشويش عشوائي؛ استخدام نفس "البذرة" يُنتج صوراً متطابقة |
| `steps` | Int | نعم | 20 | 1 ~ 10000 | عدد الخطوات المستخدمة في عملية إزالة التشويش؛ كلما زادت الخطوات، كانت النتائج أكثر دقة |
| `cfg` | float | نعم | 8.0 | 0.0 ~ 100.0 | يتحكم في مدى تطابق الصورة المُولّدة مع شروط الإدخال؛ يُوصى باستخدام القيم بين 6-8 |
| `sampler_name` | UI Option | نعم | لا يوجد | خوارزميات متعددة | اختيار أداة أخذ العيّنات لإزالة التشويش، مما يؤثر على سرعة التوليد وأسلوبه |
| `scheduler` | UI Option | نعم | لا يوجد | جداول متعددة | يتحكم في كيفية إزالة التشويش، مما يؤثر على عملية التوليد |
| `Positive` | conditioning | نعم | لا يوجد | - | الشروط الإيجابية التي تُوجّه عملية إزالة التشويش، أي ما تريد ظهوره في الصورة |
| `Negative` | conditioning | نعم | لا يوجد | - | الشروط السلبية التي تُوجّه عملية إزالة التشويش، أي ما لا تريد ظهوره في الصورة |
| `Latent_Image` | Latent | نعم | لا يوجد | - | الصورة الكامنة المستخدمة في عملية إزالة التشويش |
| `denoise` | float | لا | 1.0 | 0.0 ~ 1.0 | يُحدد نسبة إزالة التشويش؛ القيم الأقل تعني ارتباطاً أضعف بالصورة المُدخلة |
| `control_after_generate` | UI Option | لا | لا يوجد | Random/Inc/Dec/Keep | يُتيح إمكانية تغيير البذرة بعد كل طلب توليد |

## المخرجات

| المُعامل | الوظيفة |
| :--- | :--- |
| `Latent` | يُخرج البيانات الكامنة بعد إزالة التشويش بواسطة أداة أخذ العيّنات |

## الكود المصدري

[آخر تحديث: 15 مايو 2025]

```Python

def common_ksampler(model, seed, steps, cfg, sampler_name, scheduler, positive, negative, latent, denoise=1.0, disable_noise=False, start_step=None, last_step=None, force_full_denoise=False):
    latent_image = latent["samples"]
    latent_image = comfy.sample.fix_empty_latent_channels(model, latent_image)

    if disable_noise:
        noise = torch.zeros(latent_image.size(), dtype=latent_image.dtype, layout=latent_image.layout, device="cpu")
    else:
        batch_inds = latent["batch_index"] if "batch_index" in latent else None
        noise = comfy.sample.prepare_noise(latent_image, seed, batch_inds)

    noise_mask = None
    if "noise_mask" in latent:
        noise_mask = latent["noise_mask"]

    callback = latent_preview.prepare_callback(model, steps)
    disable_pbar = not comfy.utils.PROGRESS_BAR_ENABLED
    samples = comfy.sample.sample(model, noise, steps, cfg, sampler_name, scheduler, positive, negative, latent_image,
                                  denoise=denoise, disable_noise=disable_noise, start_step=start_step, last_step=last_step,
                                  force_full_denoise=force_full_denoise, noise_mask=noise_mask, callback=callback, disable_pbar=disable_pbar, seed=seed)
    out = latent.copy()
    out["samples"] = samples
    return (out, )
class KSampler:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "model": ("MODEL", {"tooltip": "النموذج المستخدم لإزالة التشويش من البيانات الكامنة المُدخلة."}),
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff, "control_after_generate": True, "tooltip": "البذرة العشوائية المستخدمة لإنشاء التشويش."}),
                "steps": ("INT", {"default": 20, "min": 1, "max": 10000, "tooltip": "عدد الخطوات المستخدمة في عملية إزالة التشويش."}),
                "cfg": ("FLOAT", {"default": 8.0, "min": 0.0, "max": 100.0, "step":0.1, "round": 0.01, "tooltip": "مقياس التوجيه الخالي من المُصنّف (CFG) يُوازن بين الإبداع والالتزام بالنص التوجيهي. القيم الأعلى تُنتج صوراً أكثر تطابقاً مع النص التوجيهي، لكن القيم المرتفعة جداً ستؤثر سلباً على الجودة."}),
                "sampler_name": (comfy.samplers.KSampler.SAMPLERS, {"tooltip": "الخوارزمية المستخدمة عند أخذ العيّنات، يمكن أن تؤثر على جودة وسرعة وأسلوب المخرجات المُولّدة."}),
                "scheduler": (comfy.samplers.KSampler.SCHEDULERS, {"tooltip": "الجدول الزمني (scheduler) يتحكم في كيفية إزالة التشويش تدريجياً لتكوين الصورة."}),
                "positive": ("CONDITIONING", {"tooltip": "التوجيه (conditioning) الذي يصف السمات التي تريد تضمينها في الصورة."}),
                "negative": ("CONDITIONING", {"tooltip": "التوجيه (conditioning) الذي يصف السمات التي تريد استبعادها من الصورة."}),
                "latent_image": ("LATENT", {"tooltip": "الصورة الكامنة المراد إزالة التشويش منها."}),
                "denoise": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 1.0, "step": 0.01, "tooltip": "مقدار إزالة التشويش المُطبّق؛ القيم الأقل ستحافظ على بنية الصورة الأولية مما يسمح بأخذ عيّنات من صورة إلى صورة (image to image)."}),
            }
        }

    RETURN_TYPES = ("LATENT",)
    OUTPUT_TOOLTIPS = ("البيانات الكامنة بعد إزالة التشويش.",)
    FUNCTION = "sample"

    CATEGORY = "sampling"
    DESCRIPTION = "يستخدم النموذج المُقدّم والتوجيه الإيجابي والسلبي لإزالة التشويش من الصورة الكامنة."

    def sample(self, model, seed, steps, cfg, sampler_name, scheduler, positive, negative, latent_image, denoise=1.0):
        return common_ksampler(model, seed, steps, cfg, sampler_name, scheduler, positive, negative, latent_image, denoise=denoise)

```