# VOIDWarpedNoiseSource

Этот узел преобразует LATENT (например, выход узла VOIDWarpedNoise) в источник NOISE. Это позволяет передавать предварительно вычисленный искажённый шум в узлы, которые ожидают источник шума, например SamplerCustomAdvanced.

## Входы

| Параметр | Описание | Тип данных | Обязательный | Диапазон |
| --- | --- | --- | --- | --- |
| `warped_noise` | Латент искажённого шума из VOIDWarpedNoise | LATENT | Да | N/A |

## Выходы

| Имя выхода | Описание | Тип данных |
| --- | --- | --- |
| `NOISE` | Источник шума, инкапсулирующий предоставленный латент; совместим с SamplerCustomAdvanced | NOISE |

> Эта документация была создана с помощью ИИ. Если вы обнаружите ошибки или у вас есть предложения по улучшению, пожалуйста, внесите свой вклад! [Редактировать на GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDWarpedNoiseSource/ru.md)

---
**Source fingerprint (SHA-256):** `61d7c82cb8a2acba28f980c4c42c6d4be12788b27676a5d30885799cf9c36185`
