# Detección RT-DETR

El nodo RT-DETR Detect realiza detección de objetos en imágenes de entrada utilizando un modelo RT-DETR. Identifica objetos, dibuja cuadros delimitadores a su alrededor y los etiqueta según las clases del conjunto de datos COCO. Puede filtrar los resultados por puntuación de confianza, clase de objeto y limitar el número total de detecciones.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `modelo` | El modelo RT-DETR utilizado para la detección de objetos. | MODEL | Sí | N/A |
| `imagen` | La(s) imagen(es) de entrada en las que detectar objetos. El nodo procesa imágenes en lotes de hasta 32. | IMAGE | Sí | N/A |
| `umbral` | La puntuación de confianza mínima que debe tener una detección para ser incluida en los resultados (predeterminado: 0.5). | FLOAT | No | N/A |
| `nombre_clase` | Filtra las detecciones por clase. Establecer en 'all' para desactivar el filtrado (predeterminado: "all"). | COMBO | No | `"all"`<br>`"person"`<br>`"bicycle"`<br>`"car"`<br>`"motorcycle"`<br>`"airplane"`<br>`"bus"`<br>`"train"`<br>`"truck"`<br>`"boat"`<br>`"traffic light"`<br>`"fire hydrant"`<br>`"stop sign"`<br>`"parking meter"`<br>`"bench"`<br>`"bird"`<br>`"cat"`<br>`"dog"`<br>`"horse"`<br>`"sheep"`<br>`"cow"`<br>`"elephant"`<br>`"bear"`<br>`"zebra"`<br>`"giraffe"`<br>`"backpack"`<br>`"umbrella"`<br>`"handbag"`<br>`"tie"`<br>`"suitcase"`<br>`"frisbee"`<br>`"skis"`<br>`"snowboard"`<br>`"sports ball"`<br>`"kite"`<br>`"baseball bat"`<br>`"baseball glove"`<br>`"skateboard"`<br>`"surfboard"`<br>`"tennis racket"`<br>`"bottle"`<br>`"wine glass"`<br>`"cup"`<br>`"fork"`<br>`"knife"`<br>`"spoon"`<br>`"bowl"`<br>`"banana"`<br>`"apple"`<br>`"sandwich"`<br>`"orange"`<br>`"broccoli"`<br>`"carrot"`<br>`"hot dog"`<br>`"pizza"`<br>`"donut"`<br>`"cake"`<br>`"chair"`<br>`"couch"`<br>`"potted plant"`<br>`"bed"`<br>`"dining table"`<br>`"toilet"`<br>`"tv"`<br>`"laptop"`<br>`"mouse"`<br>`"remote"`<br>`"keyboard"`<br>`"cell phone"`<br>`"microwave"`<br>`"oven"`<br>`"toaster"`<br>`"sink"`<br>`"refrigerator"`<br>`"book"`<br>`"clock"`<br>`"vase"`<br>`"scissors"`<br>`"teddy bear"`<br>`"hair drier"`<br>`"toothbrush"` |
| `máx_detecciones` | Número máximo de detecciones a devolver por imagen. En orden descendente de puntuación de confianza (predeterminado: 100). | INT | No | N/A |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `bboxes` | Una lista de cuadros delimitadores para cada imagen de entrada. Cada cuadro contiene coordenadas (x, y, ancho, alto), una etiqueta de clase y una puntuación de confianza. | BOUNDINGBOX |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RTDETR_detect/es.md)

---
**Source fingerprint (SHA-256):** `0c32aa9e17b8ea81e52cb45df2a40f7c1faeb39fdf18dfc643d1d31ed0bfdefd`
