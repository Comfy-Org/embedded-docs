> Эта документация была создана с помощью ИИ. Если вы обнаружите ошибки или у вас есть предложения по улучшению, пожалуйста, внесите свой вклад! [Редактировать на GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KSampler/ru.md)

## Обзор

KSampler работает следующим образом: он изменяет предоставленную исходную информацию латентного изображения на основе конкретной модели, а также позитивных и негативных условий.
Сначала он добавляет шум к исходным данным изображения в соответствии с установленными **seed** и **denoise strength**, затем подает предустановленную **Model** в сочетании с условиями позитивного и негативного guidance для генерации изображения.

## Входы

| Имя параметра          | Тип данных   | Обязательный | По умолчанию | Диапазон/Опции           | Описание                                                                           |
| ---------------------- | ------------ | ------------ | ------------ | ------------------------ | ---------------------------------------------------------------------------------- |
| Model                  | checkpoint   | Да           | None         | -                        | Входная модель, используемая в процессе шумоподавления                             |
| seed                   | Int          | Да           | 0            | 0 ~ 18446744073709551615 | Используется для генерации случайного шума; использование одинакового "seed" генерирует идентичные изображения |
| steps                  | Int          | Да           | 20           | 1 ~ 10000                | Количество шагов, используемых в процессе шумоподавления; больше шагов означает более точные результаты |
| cfg                    | float        | Да           | 8.0          | 0.0 ~ 100.0              | Определяет, насколько точно сгенерированное изображение соответствует входным условиям; рекомендуется 6-8 |
| sampler_name           | UI Option    | Да           | None         | Multiple algorithms      | Выбор сэмплера для шумоподавления; влияет на скорость генерации и стиль            |
| scheduler              | UI Option    | Да           | None         | Multiple schedulers      | Определяет, как удаляется шум; влияет на процесс генерации                         |
| Positive               | conditioning | Да           | None         | -                        | Позитивные условия, направляющие шумоподавление; то, что вы хотите видеть в изображении |
| Negative               | conditioning | Да           | None         | -                        | Негативные условия, направляющие шумоподавление; то, чего вы не хотите видеть в изображении |
| Latent_Image           | Latent       | Да           | None         | -                        | Латентное изображение, используемое для шумоподавления                             |
| denoise                | float        | Нет          | 1.0          | 0.0 ~ 1.0                | Определяет степень удаления шума; меньшие значения означают меньшую связь с входным изображением |
| control_after_generate | UI Option    | Нет          | None         | Random/Inc/Dec/Keep      | Предоставляет возможность изменять seed после каждого промпта                      |

## Выход

| Параметр | Функция                                      |
| -------------- | -------------------------------------------- |
| Latent         | Выводит латентное представление после шумоподавления сэмплером |

## Исходный код

[Обновлено 15 мая 2025 г.]

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