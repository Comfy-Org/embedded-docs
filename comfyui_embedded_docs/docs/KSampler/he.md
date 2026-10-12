# KSampler

ה-KSampler פועל כך: הוא משנה את מידע התמונה הלטנטית המקורית שסופקה בהתאם למודל מסוים ולתנאים חיוביים ושליליים כאחד.
תחילה, הוא מוסיף רעש לנתוני התמונה המקורית בהתאם ל-**seed** ול-**denoise strength** שהוגדרו, ואז מזין את ה-**Model** המוגדר מראש יחד עם תנאי ההנחיה **positive** ו-**negative** כדי ליצור את התמונה.

## קלטים

| שם פרמטר | תיאור | סוג נתון | חובה | ברירת מחדל | טווח/אפשרויות |
| --- | --- | --- | --- | --- | --- |
| Model | מודל קלט המשמש בתהליך הפחתת הרעש | checkpoint | כן | אין | - |
| seed | משמש ליצירת רעש אקראי; שימוש באותו "seed" מייצר תמונות זהות | Int | כן | 0 | 0 ~ 18446744073709551615 |
| steps | מספר השלבים לשימוש בתהליך הפחתת הרעש; שלבים רבים יותר משמעם תוצאות מדויקות יותר | Int | כן | 20 | 1 ~ 10000 |
| cfg | שולט במידת ההתאמה של התמונה הנוצרת לתנאי הקלט; מומלץ 6-8 | float | כן | 8.0 | 0.0 ~ 100.0 |
| sampler_name | בחירת דוגם (sampler) להפחתת רעש; משפיע על מהירות היצירה והסגנון | UI Option | כן | אין | אלגוריתמים מרובים |
| scheduler | שולט באופן הסרת הרעש; משפיע על תהליך היצירה | UI Option | כן | אין | מתזמנים מרובים |
| Positive | תנאים חיוביים המנחים את הפחתת הרעש; מה שתרצו שיופיע בתמונה | conditioning | כן | אין | - |
| Negative | תנאים שליליים המנחים את הפחתת הרעש; מה שלא תרצו שיופיע בתמונה | conditioning | כן | אין | - |
| Latent_Image | תמונה לטנטית המשמשת להפחתת רעש | Latent | כן | אין | - |
| denoise | קובע את יחס הסרת הרעש; ערכים נמוכים יותר משמעם פחות זיקה לתמונת הקלט | float | לא | 1.0 | 0.0 ~ 1.0 |
| control_after_generate | מאפשר לשנות את ה-seed לאחר כל פרומפט | UI Option | לא | אין | Random/Inc/Dec/Keep |

## פלט

| פרמטר | פונקציה |
| --- | --- |
| Latent | מוציא את הלטנט לאחר הפחתת הרעש של הדוגם |

## קוד מקור

[עודכן ב-15 במאי 2025]

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

> מסמך זה נוצר על ידי בינה מלאכותית. אם מצאתם שגיאות או שיש לכם הצעות לשיפור, אתם מוזמנים לתרום! [עריכה ב-GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KSampler/he.md)
