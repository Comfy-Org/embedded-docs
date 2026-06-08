گره KSampler به این صورت کار می‌کند: اطلاعات تصویر نهفته (latent) اصلی ارائه‌شده را بر اساس یک مدل مشخص و شرایط مثبت و منفی تغییر می‌دهد.
ابتدا، با توجه به **seed** (دانه) و **denoise strength** (قدرت نویززدایی) تعیین‌شده، به داده‌های تصویر اصلی نویز اضافه می‌کند، سپس **Model** (مدل) از پیش تعیین‌شده را به همراه شرایط هدایت **positive** (مثبت) و **negative** (منفی) برای تولید تصویر وارد می‌کند.

## ورودی‌ها

| نام پارامتر | توضیحات | نوع داده | اجباری | پیش‌فرض | محدوده/گزینه‌ها |
| --- | --- | --- | --- | --- | --- |
| Model | مدل ورودی استفاده‌شده برای فرآیند نویززدایی | checkpoint | بله | None | - |
| seed | برای تولید نویز تصادفی استفاده می‌شود، استفاده از "seed" یکسان تصاویر یکسانی تولید می‌کند | Int | بله | 0 | 0 ~ 18446744073709551615 |
| steps | تعداد مراحل استفاده‌شده در فرآیند نویززدایی، مراحل بیشتر به معنای نتایج دقیق‌تر است | Int | بله | 20 | 1 ~ 10000 |
| cfg | میزان تطابق تصویر تولیدشده با شرایط ورودی را کنترل می‌کند، 6-8 توصیه می‌شود | float | بله | 8.0 | 0.0 ~ 100.0 |
| sampler_name | انتخاب نمونه‌بردار برای نویززدایی، بر سرعت و سبک تولید تأثیر می‌گذارد | گزینه رابط کاربری | بله | None | الگوریتم‌های متعدد |
| scheduler | نحوه حذف نویز را کنترل می‌کند، بر فرآیند تولید تأثیر می‌گذارد | گزینه رابط کاربری | بله | None | زمان‌بندهای متعدد |
| Positive | شرایط مثبت هدایت‌کننده نویززدایی، آنچه می‌خواهید در تصویر ظاهر شود | conditioning | بله | None | - |
| Negative | شرایط منفی هدایت‌کننده نویززدایی، آنچه در تصویر نمی‌خواهید | conditioning | بله | None | - |
| Latent_Image | تصویر نهفته استفاده‌شده برای نویززدایی | Latent | بله | None | - |
| denoise | نسبت حذف نویز را تعیین می‌کند، مقادیر پایین‌تر به معنای ارتباط کمتر با تصویر ورودی است | float | خیر | 1.0 | 0.0 ~ 1.0 |
| control_after_generate | امکان تغییر seed پس از هر فراخوانی را فراهم می‌کند | گزینه رابط کاربری | خیر | None | Random/Inc/Dec/Keep |

## خروجی

| پارامتر | عملکرد                                   |
| -------------- | ------------------------------------------ |
| Latent         | خروجی نهفته پس از نویززدایی نمونه‌بردار را ارائه می‌دهد |

## کد منبع

[به‌روزرسانی در ۱۵ مه ۲۰۲۵]

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
                "model": ("MODEL", {"tooltip": "مدل استفاده‌شده برای نویززدایی از ورودی نهفته."}),
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff, "control_after_generate": True, "tooltip": "دانه تصادفی استفاده‌شده برای ایجاد نویز."}),
                "steps": ("INT", {"default": 20, "min": 1, "max": 10000, "tooltip": "تعداد مراحل استفاده‌شده در فرآیند نویززدایی."}),
                "cfg": ("FLOAT", {"default": 8.0, "min": 0.0, "max": 100.0, "step":0.1, "round": 0.01, "tooltip": "مقیاس راهنمایی بدون طبقه‌بندی (CFG) خلاقیت و پایبندی به فرمان را متعادل می‌کند. مقادیر بالاتر منجر به تصاویری می‌شود که بیشتر با فرمان مطابقت دارند، با این حال مقادیر بسیار بالا بر کیفیت تأثیر منفی می‌گذارند."}),
                "sampler_name": (comfy.samplers.KSampler.SAMPLERS, {"tooltip": "الگوریتم استفاده‌شده هنگام نمونه‌برداری، این می‌تواند بر کیفیت، سرعت و سبک خروجی تولیدشده تأثیر بگذارد."}),
                "scheduler": (comfy.samplers.KSampler.SCHEDULERS, {"tooltip": "زمان‌بند نحوه حذف تدریجی نویز برای تشکیل تصویر را کنترل می‌کند."}),
                "positive": ("CONDITIONING", {"tooltip": "شرطی‌سازی که ویژگی‌هایی را که می‌خواهید در تصویر بگنجانید توصیف می‌کند."}),
                "negative": ("CONDITIONING", {"tooltip": "شرطی‌سازی که ویژگی‌هایی را که می‌خواهید از تصویر حذف کنید توصیف می‌کند."}),
                "latent_image": ("LATENT", {"tooltip": "تصویر نهفته برای نویززدایی."}),
                "denoise": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 1.0, "step": 0.01, "tooltip": "میزان نویززدایی اعمال‌شده، مقادیر پایین‌تر ساختار تصویر اولیه را حفظ کرده و امکان نمونه‌برداری تصویر به تصویر را فراهم می‌کند."}),
            }
        }

    RETURN_TYPES = ("LATENT",)
    OUTPUT_TOOLTIPS = ("نهفته نویززدایی‌شده.",)
    FUNCTION = "sample"

    CATEGORY = "sampling"
    DESCRIPTION = "از مدل ارائه‌شده و شرطی‌سازی مثبت و منفی برای نویززدایی از تصویر نهفته استفاده می‌کند."

    def sample(self, model, seed, steps, cfg, sampler_name, scheduler, positive, negative, latent_image, denoise=1.0):
        return common_ksampler(model, seed, steps, cfg, sampler_name, scheduler, positive, negative, latent_image, denoise=denoise)

```

> این مستند با هوش مصنوعی تهیه شده است. اگر خطایی دیدید یا پیشنهادی برای بهبود دارید، خوشحال می‌شویم مشارکت کنید! [ویرایش در GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KSampler/fa.md)
