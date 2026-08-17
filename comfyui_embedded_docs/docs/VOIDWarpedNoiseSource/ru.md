# VOIDWarpedNoiseSource

## Обзор

Этот узел преобразует LATENT (например, выходные данные узла VOIDWarpedNoise) в источник NOISE. Это позволяет использовать искажённый шум с узлом SamplerCustomAdvanced для более контролируемой генерации изображений.

## Входы

| Параметр | Описание | Тип данных | Обязательность | Диапазон |
| --- | --- | --- | --- | --- |
| `warped_noise` | Латент искажённого шума из VOIDWarpedNoise | LATENT | Да | N/A |

## Выходы

| Имя выхода | Описание | Тип данных |
| --- | --- | --- |
| `NOISE` | Источник шума, который можно использовать с SamplerCustomAdvanced | NOISE |

> Эта документация была создана с помощью ИИ. Если вы обнаружите ошибки или у вас есть предложения по улучшению, пожалуйста, внесите свой вклад! [Редактировать на GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDWarpedNoiseSource/ru.md)

---
**Source fingerprint (SHA-256):** `61d7c82cb8a2acba28f980c4c42c6d4be12788b27676a5d30885799cf9c36185`
