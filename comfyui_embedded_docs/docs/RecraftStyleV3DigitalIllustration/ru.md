> Эта документация была создана с помощью ИИ. Если вы обнаружите ошибки или у вас есть предложения по улучшению, пожалуйста, внесите свой вклад! [Редактировать на GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftStyleV3DigitalIllustration/ru.md)

Этот узел настраивает стиль для использования с Recraft API, в частности выбирая стиль "digital_illustration". Он позволяет выбрать необязательный подстиль для дальнейшего уточнения художественного направления генерируемого изображения.

## Входные параметры

| Параметр | Тип данных | Обязательный | Диапазон | Описание |
|-----------|-----------|----------|-------|-------------|
| `substyle` | STRING | Нет | `"digital_illustration"`<br>`"digital_illustration_anime"`<br>`"digital_illustration_cartoon"`<br>`"digital_illustration_comic"`<br>`"digital_illustration_concept_art"`<br>`"digital_illustration_fantasy"`<br>`"digital_illustration_futuristic"`<br>`"digital_illustration_graffiti"`<br>`"digital_illustration_graphic_novel"`<br>`"digital_illustration_hyperrealistic"`<br>`"digital_illustration_ink"`<br>`"digital_illustration_manga"`<br>`"digital_illustration_minimalist"`<br>`"digital_illustration_pixel_art"`<br>`"digital_illustration_pop_art"`<br>`"digital_illustration_retro"`<br>`"digital_illustration_sci_fi"`<br>`"digital_illustration_sticker"`<br>`"digital_illustration_street_art"`<br>`"digital_illustration_surreal"`<br>`"digital_illustration_vector"` | Необязательный подстиль для указания конкретного типа цифровой иллюстрации. Если не выбран, используется базовый стиль "digital_illustration". |

## Выходные параметры

| Имя выходного параметра | Тип данных | Описание |
|-------------|-----------|-------------|
| `recraft_style` | STYLEV3 | Сконфигурированный объект стиля, содержащий выбранный стиль "digital_illustration" и необязательный подстиль, готовый для передачи другим узлам Recraft API. |

---
**Source fingerprint (SHA-256):** `e52790a670839608ee1cb576e802a54d3bf2ca879ec288a24acd4ac7db27021a`
