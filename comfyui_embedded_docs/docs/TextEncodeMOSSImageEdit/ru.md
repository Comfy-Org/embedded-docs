# Text Encode MOSS-Image Edit

Кодирует инструкцию редактирования вместе с референсными изображениями в conditioning для LoRA редактирования MOSS-Image. Подключите выход как положительный conditioning и запустите второй экземпляр с теми же референсами для отрицательного. Референсы используются в том размере, в котором поступают, поэтому масштабируйте их перед подключением. Этот узел помечен в ComfyUI как экспериментальный. Без VAE изображения попадают только в текстовый энкодер.

## Входы

| Параметр | Описание | Тип данных | Обязательный | Диапазон |
| --- | --- | --- | --- | --- |
| `clip` | Модель CLIP, которая токенизирует инструкцию и кодирует её. | CLIP | Да | - |
| `prompt` | Инструкция, описывающая редактирование. Поддерживает многострочный текст и динамические промпты. | STRING | Да | Любой текст |
| `vae` | VAE, используемый для кодирования референсных изображений в референсные латенты. Необязательно: без него изображения попадают только в текстовый энкодер.| VAE | Нет | - |
| `edit_format` | Схема, с которой обучалась LoRA редактирования. Она выбирает метод референсных латентов и то, видит ли текстовый энкодер также референсы. | COMBO | Да | `"ai-toolkit"`<br>`"ai-toolkit (kv_cache off)"`<br>`"Moss-Image-Edit"` |
| `images` | Расширяемый слот: подключите одно или несколько референсных изображений (`image_1`, `image_2`, ...). Каждое изображение используется в том размере, в котором поступило, его альфа-канал отбрасывается, а изображение кодируется через VAE в референсный латент. При подключённом VAE альфа отбрасывается и каждое изображение кодируется в референсный латент; без VAE изображения попадают только в текстовый энкодер.| IMAGE | Да | 1 или более изображений |
| `image_strength` | Масштабирует внимание модели к изображениям, которые видит текстовый энкодер (форматы ai-toolkit или без VAE): 0 игнорирует, 1 без изменений, выше 1 усиливает. Расширенный. По умолчанию: 1.0. | FLOAT | Да | 0.0 to 100.0 (step 0.05) |

**Примечание:** With `"ai-toolkit"` and `"ai-toolkit (kv_cache off)"`, or when no VAE is connected and `image_strength` is above 0, the text encoder also sees every reference, downscaled to at most 384x384 pixels and preceded by a `Picture N:` marker in the prompt, so the instruction can refer to them by number. With `"Moss-Image-Edit"` and a VAE connected, the references reach the model only as reference latents and the text encoder sees the instruction alone. `"ai-toolkit (kv_cache off)"` additionally keeps the references attending to the image being generated, so they are recomputed on every sampling step.

## Выходы

| Имя выхода | Описание | Тип данных |
| --- | --- | --- |
| `conditioning` | Закодированная инструкция с прикреплёнными референсными латентами и соответствующим методом референсных латентов. | CONDITIONING |

> Эта документация была создана с помощью ИИ. Если вы обнаружите ошибки или у вас есть предложения по улучшению, пожалуйста, внесите свой вклад! [Редактировать на GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeMOSSImageEdit/ru.md)

---
**Source fingerprint (SHA-256):** `673f098df6a8e466a5c8060009f446eac8f7556311a870de626c5f4bfc3ab196`
