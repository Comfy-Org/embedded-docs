Узел RT-DETR Detect выполняет обнаружение объектов на входных изображениях с помощью модели RT-DETR. Он идентифицирует объекты, рисует ограничивающие рамки вокруг них и маркирует их в соответствии с классами набора данных COCO. Вы можете фильтровать результаты по порогу уверенности, классу объекта и ограничивать общее количество обнаружений.

## Входные параметры

| Параметр | Описание | Тип данных | Обязательный | Диапазон |
| --- | --- | --- | --- | --- |
| `model` | Модель RT-DETR, используемая для обнаружения объектов. | MODEL | Да | Н/Д |
| `image` | Входное изображение(я) для обнаружения объектов. Узел обрабатывает изображения пакетами до 32 штук. | IMAGE | Да | Н/Д |
| `threshold` | Минимальный порог уверенности, который должно иметь обнаружение, чтобы быть включённым в результаты (по умолчанию: 0.5). | FLOAT | Нет | Н/Д |
| `class_name` | Фильтрация обнаружений по классу. Установите значение 'all', чтобы отключить фильтрацию (по умолчанию: "all"). | COMBO | Нет | `"all"`<br>`"person"`<br>`"bicycle"`<br>`"car"`<br>`"motorcycle"`<br>`"airplane"`<br>`"bus"`<br>`"train"`<br>`"truck"`<br>`"boat"`<br>`"traffic light"`<br>`"fire hydrant"`<br>`"stop sign"`<br>`"parking meter"`<br>`"bench"`<br>`"bird"`<br>`"cat"`<br>`"dog"`<br>`"horse"`<br>`"sheep"`<br>`"cow"`<br>`"elephant"`<br>`"bear"`<br>`"zebra"`<br>`"giraffe"`<br>`"backpack"`<br>`"umbrella"`<br>`"handbag"`<br>`"tie"`<br>`"suitcase"`<br>`"frisbee"`<br>`"skis"`<br>`"snowboard"`<br>`"sports ball"`<br>`"kite"`<br>`"baseball bat"`<br>`"baseball glove"`<br>`"skateboard"`<br>`"surfboard"`<br>`"tennis racket"`<br>`"bottle"`<br>`"wine glass"`<br>`"cup"`<br>`"fork"`<br>`"knife"`<br>`"spoon"`<br>`"bowl"`<br>`"banana"`<br>`"apple"`<br>`"sandwich"`<br>`"orange"`<br>`"broccoli"`<br>`"carrot"`<br>`"hot dog"`<br>`"pizza"`<br>`"donut"`<br>`"cake"`<br>`"chair"`<br>`"couch"`<br>`"potted plant"`<br>`"bed"`<br>`"dining table"`<br>`"toilet"`<br>`"tv"`<br>`"laptop"`<br>`"mouse"`<br>`"remote"`<br>`"keyboard"`<br>`"cell phone"`<br>`"microwave"`<br>`"oven"`<br>`"toaster"`<br>`"sink"`<br>`"refrigerator"`<br>`"book"`<br>`"clock"`<br>`"vase"`<br>`"scissors"`<br>`"teddy bear"`<br>`"hair drier"`<br>`"toothbrush"` |
| `max_detections` | Максимальное количество обнаружений, возвращаемых для каждого изображения. В порядке убывания порога уверенности (по умолчанию: 100). | INT | Нет | Н/Д |

## Выходные параметры

| Имя выхода | Описание | Тип данных |
| --- | --- | --- |
| `bboxes` | Список ограничивающих рамок для каждого входного изображения. Каждая рамка содержит координаты (x, y, ширина, высота), метку класса и порог уверенности. | BOUNDINGBOX |

> Эта документация была создана с помощью ИИ. Если вы обнаружите ошибки или у вас есть предложения по улучшению, пожалуйста, внесите свой вклад! [Редактировать на GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RTDETR_detect/ru.md)

---
**Source fingerprint (SHA-256):** `0c32aa9e17b8ea81e52cb45df2a40f7c1faeb39fdf18dfc643d1d31ed0bfdefd`
