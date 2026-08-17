# FluxKontextMultiReferenceLatentMethod

Узел `FluxKontextMultiReferenceLatentMethod` изменяет данные `conditioning`, задавая конкретный метод `reference latents`. Он добавляет выбранный метод к входу `conditioning`, что влияет на обработку `reference latents` на последующих этапах генерации. Этот узел помечен как экспериментальный и является частью системы `conditioning` Flux.

## Входы

| Параметр | Описание | Тип данных | Обязательный | Диапазон |
| --- | --- | --- | --- | --- |
| `conditioning` | Данные `conditioning`, которые будут изменены с помощью метода `reference latents`. | CONDITIONING | Да | - |
| `reference_latents_method` | Метод, используемый для обработки `reference latents`. Если выбрано `"uxo"` или `"uso"`, оно будет преобразовано в `"uxo"`. Этот параметр помечен как расширенный. | COMBO | Да | `"offset"`<br>`"index"`<br>`"uxo/uno"`<br>`"index_timestep_zero"` |

## Выходы

| Имя выхода | Описание | Тип данных |
| --- | --- | --- |
| `conditioning` | Изменённые данные `conditioning` с применённым методом `reference latents`. | CONDITIONING |

> Эта документация была создана с помощью ИИ. Если вы обнаружите ошибки или у вас есть предложения по улучшению, пожалуйста, внесите свой вклад! [Редактировать на GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxKontextMultiReferenceLatentMethod/ru.md)

---
**Source fingerprint (SHA-256):** `cbe069d0c9f8adbf7f8c909b1cd644d9cd3730e934f0e5856213ff06fa8ecc56`
