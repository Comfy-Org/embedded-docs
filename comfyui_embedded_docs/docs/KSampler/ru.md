> Эта документация была создана с помощью ИИ. Если вы обнаружите ошибки или у вас есть предложения по улучшению, пожалуйста, внесите свой вклад! [Редактировать на GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KSampler/ru.md)

Вот перевод документации узла KSampler на русский язык:

KSampler работает следующим образом: он изменяет предоставленную исходную информацию о скрытом изображении на основе конкретной модели, а также позитивных и негативных условий.
Сначала он добавляет шум к исходным данным изображения в соответствии с заданными **seed** и **denoise strength**, затем подает предустановленную **Model** в сочетании с **позитивными** и **негативными** условиями управления для генерации изображения.

## Входные параметры

| Имя параметра         | Тип данных    | Обязательный | По умолчанию | Диапазон/Опции           | Описание                                                                                |
| ---------------------- | ------------ | ------------ | ------------ | ------------------------ | --------------------------------------------------------------------------------------- |
| Model                  | checkpoint   | Да           | Нет          | -                        | Модель, используемая для процесса шумоподавления                                        |
| seed                   | Int          | Да           | 0            | 0 ~ 18446744073709551615 | Используется для генерации случайного шума, одинаковый "seed" создает идентичные изображения |
| steps                  | Int          | Да           | 20           | 1 ~ 10000                | Количество шагов в процессе шумоподавления, больше шагов означает более точные результаты |
| cfg                    | float        | Да           | 8.0          | 0.0 ~ 100.0              | Контролирует, насколько сгенерированное изображение соответствует входным условиям, рекомендуется 6-8 |
| sampler_name           | UI Option    | Да           | Нет          | Несколько алгоритмов     | Выбор сэмплера для шумоподавления, влияет на скорость и стиль генерации                 |
| scheduler              | UI Option    | Да           | Нет          | Несколько планировщиков  | Управляет удалением шума, влияет на процесс генерации                                   |
| Positive               | conditioning | Да           | Нет          | -                        | Позитивные условия, направляющие шумоподавление, то, что вы хотите видеть на изображении |
| Negative               | conditioning | Да           | Нет          | -                        | Негативные условия, направляющие шумоподавление, то, чего вы не хотите на изображении    |
| Latent_Image           | Latent       | Да           | Нет          | -                        | Скрытое изображение, используемое для шумоподавления                                    |
| denoise                | float        | Нет          | 1.0          | 0.0 ~ 1.0                | Определяет коэффициент удаления шума, более низкие значения означают меньшую связь с исходным изображением |
| control_after_generate | UI Option    | Нет          | Нет          | Random/Inc/Dec/Keep      | Позволяет изменять seed после каждого запроса                                           |

## Выходные данные

| Параметр | Функция                                   |
| -------------- | ------------------------------------------ |
| Latent         | Выводит скрытое представление после шумоподавления сэмплером |

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
                "model": ("MODEL", {"tooltip": "Модель, используемая для шумоподавления входного скрытого представления."}),
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff, "control_after_generate": True, "tooltip": "Случайное начальное число, используемое для создания шума."}),
                "steps": ("INT", {"default": 20, "min": 1, "max": 10000, "tooltip": "Количество шагов, используемых в процессе шумоподавления."}),
                "cfg": ("FLOAT", {"default": 8.0, "min": 0.0, "max": 100.0, "step":0.1, "round": 0.01, "tooltip": "Шкала Classifier-Free Guidance балансирует между креативностью и соответствием запросу. Более высокие значения приводят к изображениям, более точно соответствующим запросу, однако слишком высокие значения негативно повлияют на качество."}),
                "sampler_name": (comfy.samplers.KSampler.SAMPLERS, {"tooltip": "Алгоритм, используемый при сэмплировании, может влиять на качество, скорость и стиль сгенерированного результата."}),
                "scheduler": (comfy.samplers.KSampler.SCHEDULERS, {"tooltip": "Планировщик управляет тем, как постепенно удаляется шум для формирования изображения."}),
                "positive": ("CONDITIONING", {"tooltip": "Условия, описывающие атрибуты, которые вы хотите включить в изображение."}),
                "negative": ("CONDITIONING", {"tooltip": "Условия, описывающие атрибуты, которые вы хотите исключить из изображения."}),
                "latent_image": ("LATENT", {"tooltip": "Скрытое изображение для шумоподавления."}),
                "denoise": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 1.0, "step": 0.01, "tooltip": "Степень применяемого шумоподавления, более низкие значения сохранят структуру исходного изображения, позволяя выполнять сэмплирование изображения в изображение."}),
            }
        }

    RETURN_TYPES = ("LATENT",)
    OUTPUT_TOOLTIPS = ("Скрытое представление после шумоподавления.",)
    FUNCTION = "sample"

    CATEGORY = "sampling"
    DESCRIPTION = "Использует предоставленную модель, позитивные и негативные условия для шумоподавления скрытого изображения."

    def sample(self, model, seed, steps, cfg, sampler_name, scheduler, positive, negative, latent_image, denoise=1.0):
        return common_ksampler(model, seed, steps, cfg, sampler_name, scheduler, positive, negative, latent_image, denoise=denoise)

```