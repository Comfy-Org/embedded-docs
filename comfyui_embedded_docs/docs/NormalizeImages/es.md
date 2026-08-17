# Normalizar Imágenes

Este nodo normaliza una imagen de entrada restando un valor medio especificado de cada píxel y luego dividiendo el resultado por una desviación estándar especificada. Este es un paso de preprocesamiento común para estandarizar los valores de píxeles y preparar los datos de imagen para su posterior procesamiento.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `image` | La imagen de entrada a normalizar. | IMAGE | Sí | - |
| `mean` | Valor medio para la normalización (por defecto: 0.5). | FLOAT | No | 0.0 - 1.0 |
| `std` | Desviación estándar para la normalización (por defecto: 0.5). | FLOAT | No | 0.001 - 1.0 |

Nota: La normalización se aplica a todo el lote de imágenes a la vez, y se admite cualquier tamaño de lote.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `image` | La imagen resultante después de haberse aplicado el proceso de normalización. | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/NormalizeImages/es.md)

---
**Source fingerprint (SHA-256):** `927451ed275254d87e42b52919143ee2f3d9833a2aa5b43c7315d798871f9a2d`
