> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/NormalizeImages/es.md)

Este nodo ajusta los valores de píxel de una imagen de entrada mediante un proceso matemático de normalización. Resta un valor medio especificado de cada píxel y luego divide el resultado por una desviación estándar especificada. Este es un paso de preprocesamiento común para preparar datos de imagen para otros modelos de aprendizaje automático.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Sí | - | La imagen de entrada que se va a normalizar. |
| `mean` | FLOAT | No | 0.0 - 1.0 | El valor medio que se restará de los píxeles de la imagen (valor por defecto: 0.5). |
| `std` | FLOAT | No | 0.001 - 1.0 | El valor de desviación estándar por el que se dividirán los píxeles de la imagen (valor por defecto: 0.5). |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `image` | IMAGE | La imagen resultante después de aplicar el proceso de normalización. |
