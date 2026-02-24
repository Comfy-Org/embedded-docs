> Эта документация была создана с помощью ИИ. Если вы обнаружите ошибки или у вас есть предложения по улучшению, пожалуйста, внесите свой вклад! [Редактировать на GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftStyleV3VectorIllustrationNode/ru.md)

Этот узел настраивает стиль для использования с API Recraft, конкретно выбирая стиль `vector_illustration`. Он позволяет при необходимости выбрать более конкретный подстиль в рамках этой категории. Узел выводит объект конфигурации стиля, который можно передать другим узлам API Recraft.

## Входы

| Параметр | Тип данных | Обязательный | Диапазон | Описание |
|-----------|-----------|----------|-------|-------------|
| `substyle` | STRING | Нет | `"vector_illustration"`<br>`"vector_illustration_flat"`<br>`"vector_illustration_3d"`<br>`"vector_illustration_hand_drawn"`<br>`"vector_illustration_retro"`<br>`"vector_illustration_modern"`<br>`"vector_illustration_abstract"`<br>`"vector_illustration_geometric"`<br>`"vector_illustration_organic"`<br>`"vector_illustration_minimalist"`<br>`"vector_illustration_detailed"`<br>`"vector_illustration_colorful"`<br>`"vector_illustration_monochrome"`<br>`"vector_illustration_grayscale"`<br>`"vector_illustration_pastel"`<br>`"vector_illustration_vibrant"`<br>`"vector_illustration_muted"`<br>`"vector_illustration_warm"`<br>`"vector_illustration_cool"`<br>`"vector_illustration_neutral"`<br>`"vector_illustration_bold"`<br>`"vector_illustration_subtle"`<br>`"vector_illustration_playful"`<br>`"vector_illustration_serious"`<br>`"vector_illustration_elegant"`<br>`"vector_illustration_rustic"`<br>`"vector_illustration_urban"`<br>`"vector_illustration_nature"`<br>`"vector_illustration_fantasy"`<br>`"vector_illustration_sci_fi"`<br>`"vector_illustration_historical"`<br>`"vector_illustration_futuristic"`<br>`"vector_illustration_whimsical"`<br>`"vector_illustration_surreal"`<br>`"vector_illustration_realistic"`<br>`"vector_illustration_stylized"`<br>`"vector_illustration_cartoony"`<br>`"vector_illustration_anime"`<br>`"vector_illustration_comic"`<br>`"vector_illustration_pixel"`<br>`"vector_illustration_low_poly"`<br>`"vector_illustration_high_poly"`<br>`"vector_illustration_isometric"`<br>`"vector_illustration_orthographic"`<br>`"vector_illustration_perspective"`<br>`"vector_illustration_2d"`<br>`"vector_illustration_2.5d"`<br>`"vector_illustration_3d"`<br>`"vector_illustration_4d"` | Необязательный, более конкретный стиль в категории `vector_illustration`. Если не выбран, используется базовый стиль `vector_illustration`. |

## Выходы

| Имя выхода | Тип данных | Описание |
|-------------|-----------|-------------|
| `recraft_style` | STYLEV3 | Объект конфигурации стиля API Recraft, содержащий выбранный стиль `vector_illustration` и опциональный подстиль. Может быть подключен к другим узлам Recraft. |
