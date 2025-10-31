> تم إنشاء هذه الوثيقة بواسطة الذكاء الاصطناعي. إذا وجدت أي أخطاء أو لديك اقتراحات للتحسين، فلا تتردد في المساهمة! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KSampler/ar.md)

يعمل مُعين العينات KSampler بالطريقة التالية: يقوم بتعديل معلومات الصورة الكامنة الأصلية المُقدمة بناءً على نموذج محدد وكل من الشروط الإيجابية والسلبية.
أولاً، يضيف ضوضاء إلى بيانات الصورة الأصلية وفقًا لـ **البذرة** المحددة و**قوة إزالة الضوضاء**، ثم يُدخل **النموذج** المحدد مسبقًا مدمجًا مع شروط التوجيه **الإيجابية** و**السلبية** لتوليد الصورة.

## المدخلات

| اسم المعامل          | نوع البيانات | مطلوب | الافتراضي | النطاق/الخيارات           | الوصف                                                                               |
| --------------------- | ------------- | ------ | --------- | ------------------------- | ----------------------------------------------------------------------------------- |
| Model                 | checkpoint    | نعم    | None      | -                         | النموذج المدخل المستخدم في عملية إزالة الضوضاء                                      |
| seed                  | Int           | نعم    | 0         | 0 ~ 18446744073709551615 | يُستخدم لتوليد ضوضاء عشوائية، استخدام نفس "البذرة" ينتج صورًا متطابقة              |
| steps                 | Int           | نعم    | 20        | 1 ~ 10000                 | عدد الخطوات المستخدمة في عملية إزالة الضوضاء، المزيد من الخطوات يعني نتائج أكثر دقة |
| cfg                   | float         | نعم    | 8.0       | 0.0 ~ 100.0               | يتحكم في مدى تطابق الصورة المُنشأة مع شروط الإدخال، يُوصى بـ 6-8                     |
| sampler_name          | UI Option     | نعم    | None      | خوارزميات متعددة          | اختر مُعين العينات لإزالة الضوضاء، يؤثر على سرعة التوليد والأسلوب                   |
| scheduler             | UI Option     | نعم    | None      | مُجدولات متعددة           | يتحكم في كيفية إزالة الضوضاء، يؤثر على عملية التوليد                                 |
| Positive              | conditioning  | نعم    | None      | -                         | الشروط الإيجابية التي توجه عملية إزالة الضوضاء، ما تريد ظهوره في الصورة            |
| Negative              | conditioning  | نعم    | None      | -                         | الشروط السلبية التي توجه عملية إزالة الضوضاء، ما لا تريد ظهوره في الصورة           |
| Latent_Image          | Latent        | نعم    | None      | -                         | الصورة الكامنة المستخدمة في إزالة الضوضاء                                           |
| denoise               | float         | لا     | 1.0       | 0.0 ~ 1.0                 | يحدد نسبة إزالة الضوضاء، القيم الأقل تعني ارتباطًا أقل بالصورة المدخلة              |
| control_after_generate| UI Option     | لا     | None      | عشوائي/زيادة/نقصان/حفظ   | يوفر القدرة على تغيير البذرة بعد كل أمر                                             |

## المخرجات

| المعامل     | الوظيفة                                     |
| ----------- | ------------------------------------------- |
| Latent      | يُخرج الصورة الكامنة بعد إزالة الضوضاء بواسطة المُعين |

## الكود المصدري

[تم التحديث في 15 مايو 2025]

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
                "model": ("MODEL", {"tooltip": "The model used for denoising the input latent."}),
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff, "control_after_generate": True, "tooltip": "The random seed used for creating the noise."}),
                "steps": ("INT", {"default": 20, "min": 1, "max": 10000, "tooltip": "The number of steps used in the denoising process."}),
                "cfg": ("FLOAT", {"default": 8.0, "min": 0.0, "max": 100.0, "step":0.1, "round": 0.01, "tooltip": "The Classifier-Free Guidance scale balances creativity and adherence to the prompt. Higher values result in images more closely matching the prompt however too high values will negatively impact quality."}),
                "sampler_name": (comfy.samplers.KSampler.SAMPLERS, {"tooltip": "The algorithm used when sampling, this can affect the quality, speed, and style of the generated output."}),
                "scheduler": (comfy.samplers.KSampler.SCHEDULERS, {"tooltip": "The scheduler controls how noise is gradually removed to form the image."}),
                "positive": ("CONDITIONING", {"tooltip": "The conditioning describing the attributes you want to include in the image."}),
                "negative": ("CONDITIONING", {"tooltip": "The conditioning describing the attributes you want to exclude from the image."}),
                "latent_image": ("LATENT", {"tooltip": "The latent image to denoise."}),
                "denoise": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 1.0, "step": 0.01, "tooltip": "The amount of denoising applied, lower values will maintain the structure of the initial image allowing for image to image sampling."}),
            }
        }

    RETURN_TYPES = ("LATENT",)
    OUTPUT_TOOLTIPS = ("The denoised latent.",)
    FUNCTION = "sample"

    CATEGORY = "sampling"
    DESCRIPTION = "Uses the provided model, positive and negative conditioning to denoise the latent image."

    def sample(self, model, seed, steps, cfg, sampler_name, scheduler, positive, negative, latent_image, denoise=1.0):
        return common_ksampler(model, seed, steps, cfg, sampler_name, scheduler, positive, negative, latent_image, denoise=denoise)

```