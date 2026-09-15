# Двойной CFG Гид

Узел Dual CFG Guider создаёт систему guidance для сэмплинга, которая использует два входа conditioning вместе с одним входом отрицательного conditioning. Он применяет две отдельные шкалы guidance, чтобы управлять силой влияния каждого conditioning на сгенерированный результат, и поддерживает два способа комбинирования этих шкал: "regular" и "nested".

## Входы

| Параметр | Описание | Тип данных | Обязательный | Диапазон |
| --- | --- | --- | --- | --- |
| `модель` | Модель, используемая для guidance | MODEL | Да | - |
| `cond1` | Первый вход положительного conditioning | CONDITIONING | Да | - |
| `cond2` | Второй вход conditioning, используемый как эталон между первым положительным conditioning и отрицательным conditioning | CONDITIONING | Да | - |
| `отрицательный` | Вход отрицательного conditioning | CONDITIONING | Да | - |
| `cfg_conds` | Шкала guidance, применяемая к первому положительному conditioning (по умолчанию: 8.0) | FLOAT | Да | 0.0 - 100.0 |
| `cfg_cond2_negative` | Шкала guidance, применяемая между вторым conditioning и отрицательным conditioning (по умолчанию: 8.0) | FLOAT | Да | 0.0 - 100.0 |
| `стиль` | Применяемый стиль guidance (по умолчанию: "regular"). Если установлено "nested", guidance применяется вложенным образом | COMBO | Да | "regular"<br>"nested" |

Примечание: В стиле `regular` `cfg_cond2_negative` применяется между `cond2` и `negative`, а `cfg_conds` применяется между `cond1` и `cond2`. В стиле `nested` `cfg_conds` сначала применяется между `cond1` и `cond2`, после чего полученное предсказание направляется в сторону от `negative` с помощью `cfg_cond2_negative`.

Примечание: В стиле `regular`, когда `cfg_cond2_negative` равен 1.0, отрицательный conditioning пропускается, а когда `cfg_conds` также равен 1.0, второй conditioning тоже пропускается. Это уменьшает количество выполняемых вычислений модели.

## Выходы

| Имя выхода | Описание | Тип данных |
| --- | --- | --- |
| `GUIDER` | Настроенная система guidance, готовая к использованию при сэмплинге | GUIDER |

> Эта документация была создана с помощью ИИ. Если вы обнаружите ошибки или у вас есть предложения по улучшению, пожалуйста, внесите свой вклад! [Редактировать на GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DualCFGGuider/ru.md)

---
**Source fingerprint (SHA-256):** `ef28d109149cb545bcd76215fd99535905c1d395222149a029c1c210e2912e97`
