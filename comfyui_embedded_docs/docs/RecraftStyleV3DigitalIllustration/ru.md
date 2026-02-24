> Эта документация была создана с помощью ИИ. Если вы обнаружите ошибки или у вас есть предложения по улучшению, пожалуйста, внесите свой вклад! [Редактировать на GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftStyleV3DigitalIllustration/ru.md)

Этот узел настраивает стиль для использования с API Recraft, конкретно выбирая стиль "digital_illustration". Он позволяет выбрать дополнительный подстиль для дальнейшего уточнения художественного направления генерируемого изображения.

## Входы

| Параметр | Тип данных | Обязательный | Диапазон | Описание |
|-----------|-----------|----------|-------|-------------|
| `подстиль` | STRING | Нет | `"digital_illustration"`<br>`"digital_illustration_anime"`<br>`"digital_illustration_cartoon"`<br>`"digital_illustration_comic"`<br>`"digital_illustration_concept_art"`<br>`"digital_illustration_fantasy"`<br>`"digital_illustration_futuristic"`<br>`"digital_illustration_graffiti"`<br>`"digital_illustration_graphic_novel"`<br>`"digital_illustration_hyperrealistic"`<br>`"digital_illustration_ink"`<br>`"digital_illustration_manga"`<br>`"digital_illustration_minimalist"`<br>`"digital_illustration_pixel_art"`<br>`"digital_illustration_pop_art"`<br>`"digital_illustration_retro"`<br>`"digital_illustration_sci_fi"`<br>`"digital_illustration_sticker"`<br>`"digital_illustration_street_art"`<br>`"digital_illustration_surreal"`<br>`"digital_illustration_vector"` | Дополнительный подстиль для указания конкретного типа цифровой иллюстрации. Если не выбран, используется базовый стиль "digital_illustration". |

## Выходы

| Имя выхода | Тип данных | Описание |
|-------------|-----------|-------------|
| `recraft_style` | STYLEV3 | Настроенный объект стиля, содержащий выбранный стиль "digital_illustration" и опциональный подстиль, готовый для передачи в другие узлы API Recraft. |
