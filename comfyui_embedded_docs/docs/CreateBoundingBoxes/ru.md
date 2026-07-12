# Создать ограничивающие рамки

Нарисуйте ограничивающие рамки на холсте. Выходные данные: элементы промпта Ideogram, ограничивающие рамки в пикселях и изображение предпросмотра.

## Входы

| Параметр | Описание | Тип данных | Обязательный | Диапазон |
|-----------|-------------|-----------|----------|-------|
| `фон` | Необязательное изображение, используемое как фон на холсте и в предпросмотре. | IMAGE | No | - |
| `bboxes` | Bounding boxes, elements, or a JSON string to initialize the canvas. A new upstream value initializes the canvas; edits made on the canvas take priority and are kept until the upstream value changes again. | BOUNDING_BOX, ARRAY, STRING | No | - |
| `ширина` | Ширина холста и пиксельной сетки для ограничивающих рамок. | INT | Yes | 64 to 16384 (step: 16) |
| `высота` | Высота холста и пиксельной сетки для ограничивающих рамок. | INT | Yes | 64 to 16384 (step: 16) |
| `состояние_редактора` | Нарисуйте ограничивающие рамки и задайте для каждой рамки тип, текст, описание, цветовую палитру. Начинайте с фонового элемента, затем передний план. | BOUNDING_BOXES | Yes | - |
| `last_incoming` | Internal state managed by the canvas: the upstream bboxes value that last initialized it. Leave empty to re-initialize the canvas from the bboxes input on the next run. | BOUNDING_BOXES | No | - |

## Выходы

| Имя выхода | Описание | Тип данных |
|-------------|-------------|-----------|
| `preview` | An RGB image showing the canvas with all bounding boxes rendered, including labels, color palette swatches, and descriptive text. | IMAGE |
| `bboxes` | A list of bounding boxes in pixel coordinates, with each box containing x, y, width, and height values. | BOUNDING_BOX |
| `elements` | A structured array of element objects, each containing type, bounding box coordinates (normalized 0-1000), text (for text type), description, and color palette. | ARRAY |

> Эта документация была создана с помощью ИИ. Если вы обнаружите ошибки или у вас есть предложения по улучшению, пожалуйста, внесите свой вклад! [Редактировать на GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateBoundingBoxes/ru.md)

---
**Source fingerprint (SHA-256):** `dc5545dffefdccf14f3919ff4d9966dbfd1a497dcd64e1863556d5728659ee94`
