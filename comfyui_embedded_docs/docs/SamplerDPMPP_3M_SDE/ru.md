# Сэмплер DPMPP_3M_SDE

The SamplerDPMPP_3M_SDE node creates a DPM++ 3M SDE sampler for use in the sampling process. This sampler uses a third-order multistep stochastic differential equation method with configurable noise parameters. The node allows you to choose whether noise calculations are performed on the GPU or CPU.

## Входы

| Параметр | Описание | Тип данных | Обязательность | Диапазон |
| --- | --- | --- | --- | --- |
| `eta` | Управляет стохастичностью процесса сэмплирования (по умолчанию: 1.0) | FLOAT | Да | 0.0 - 100.0 |
| `s_noise` | Управляет количеством шума, добавляемого во время сэмплирования (по умолчанию: 1.0) | FLOAT | Да | 0.0 - 100.0 |
| `noise_device` | Выбирает устройство для вычислений шума: GPU или CPU (по умолчанию: "gpu") | COMBO | Да | "gpu"<br>"cpu" |

## Выходы

| Имя выхода | Описание | Тип данных |
| --- | --- | --- |
| `sampler` | Возвращает настроенный объект сэмплера для использования в процессах сэмплирования | SAMPLER |

> Эта документация была создана с помощью ИИ. Если вы обнаружите ошибки или у вас есть предложения по улучшению, пожалуйста, внесите свой вклад! [Редактировать на GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDPMPP_3M_SDE/ru.md)

---
**Source fingerprint (SHA-256):** `0f624398c67e50639fc41384b50b91bab93797bd785dda25f1f5fc649e46825b`
