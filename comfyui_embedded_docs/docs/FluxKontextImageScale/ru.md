Этот узел масштабирует входное изображение до оптимального размера, использованного при обучении модели Flux Kontext, используя алгоритм Lanczos, основываясь на соотношении сторон входного изображения. Этот узел особенно полезен при вводе изображений большого размера, так как чрезмерно большие входные данные могут привести к ухудшению качества выходных данных модели или проблемам, таким как появление нескольких субъектов на выходе.

## Входы

| Имя Параметра | Тип Данных | Тип Входа | Значение по Умолчанию | Диапазон Значений | Описание |
|---------------|------------|------------|----------------------|-------------------|-----------|
| `image` | IMAGE | Обязательный | - | - | Входное изображение для изменения размера |

## Выходы

| Имя Выхода | Тип Данных | Описание |
|------------|------------|-----------|
| `image` | IMAGE | Изображение с измененным размером |

## Список Предустановленных Размеров

Ниже приведен список стандартных размеров, использованных при обучении модели. Узел выберет размер, наиболее близкий к соотношению сторон входного изображения:

| Ширина | Высота | Соотношение Сторон |
|--------|--------|-------------------|
| 672    | 1568   | 0.429            |
| 688    | 1504   | 0.457            |
| 720    | 1456   | 0.494            |
| 752    | 1392   | 0.540            |
| 800    | 1328   | 0.603            |
| 832    | 1248   | 0.667            |
| 880    | 1184   | 0.743            |
| 944    | 1104   | 0.855            |
| 1024   | 1024   | 1.000            |
| 1104   | 944    | 1.170            |
| 1184   | 880    | 1.345            |
| 1248   | 832    | 1.500            |
| 1328   | 800    | 1.660            |
| 1392   | 752    | 1.851            |
| 1456   | 720    | 2.022            |
| 1504   | 688    | 2.186            |
| 1568   | 672    | 2.333            |
