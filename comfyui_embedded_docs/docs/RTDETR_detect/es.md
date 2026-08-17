# Detección RT-DETR

El nodo RT-DETR Detect realiza detección de objetos en imágenes de entrada utilizando un modelo RT-DETR. Encuentra objetos en la imagen y devuelve las coordenadas de los cuadros delimitadores para cada detección, etiquetadas con la clase correspondiente del conjunto de datos COCO. Puede filtrar los resultados por puntuación de confianza y clase de objeto, así como limitar el número total de detecciones devueltas por imagen.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `model` | El modelo RT-DETR utilizado para la detección de objetos. | MODEL | Sí | N/A |
| `image` | La(s) imagen(es) de entrada en las que se detectarán objetos. El nodo procesa las imágenes en lotes de hasta 32 y las redimensiona internamente para la detección. | IMAGE | Sí | N/A |
| `threshold` | La puntuación de confianza mínima que debe tener una detección para incluirse en los resultados (por defecto: 0.5). | FLOAT | Sí | N/A |
| `class_name` | Filtra las detecciones por clase. Establézcalo en `'all'` para desactivar el filtrado (por defecto: "all"). | COMBO | Sí | `"all"`<br>`"person"`<br>`"bicycle"`<br>`"car"`<br>`"motorcycle"`<br>`"airplane"`<br>`"bus"`<br>`"train"`<br>`"truck"`<br>`"boat"`<br>`"traffic light"`<br>`"fire hydrant"`<br>`"stop sign"`<br>`"parking meter"`<br>`"bench"`<br>`"bird"`<br>`"cat"`<br>`"dog"`<br>`"horse"`<br>`"sheep"`<br>`"cow"`<br>`"elephant"`<br>`"bear"`<br>`"zebra"`<br>`"giraffe"`<br>`"backpack"`<br>`"umbrella"`<br>`"handbag"`<br>`"tie"`<br>`"suitcase"`<br>`"frisbee"`<br>`"skis"`<br>`"snowboard"`<br>`"sports ball"`<br>`"kite"`<br>`"baseball bat"`<br>`"baseball glove"`<br>`"skateboard"`<br>`"surfboard"`<br>`"tennis racket"`<br>`"bottle"`<br>`"wine glass"`<br>`"cup"`<br>`"fork"`<br>`"knife"`<br>`"spoon"`<br>`"bowl"`<br>`"banana"`<br>`"apple"`<br>`"sandwich"`<br>`"orange"`<br>`"broccoli"`<br>`"carrot"`<br>`"hot dog"`<br>`"pizza"`<br>`"donut"`<br>`"cake"`<br>`"chair"`<br>`"couch"`<br>`"potted plant"`<br>`"bed"`<br>`"dining table"`<br>`"toilet"`<br>`"tv"`<br>`"laptop"`<br>`"mouse"`<br>`"remote"`<br>`"keyboard"`<br>`"cell phone"`<br>`"microwave"`<br>`"oven"`<br>`"toaster"`<br>`"sink"`<br>`"refrigerator"`<br>`"book"`<br>`"clock"`<br>`"vase"`<br>`"scissors"`<br>`"teddy bear"`<br>`"hair drier"`<br>`"toothbrush"` |
| `max_detections` | Número máximo de detecciones a devolver por imagen, en orden descendente de puntuación de confianza (por defecto: 100). | INT | Sí | N/A |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `bboxes` | Una lista de cuadros delimitadores para cada imagen de entrada. Cada cuadro contiene coordenadas (x, y, ancho, alto), una etiqueta de clase y una puntuación de confianza. | BOUNDINGBOX |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RTDETR_detect/es.md)

---
**Source fingerprint (SHA-256):** `658a47cae788da207a52edc6bf8a428c9f3d8cf415e5f20f71d6125ad6d49734`
