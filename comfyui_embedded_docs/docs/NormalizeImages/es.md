Este nodo ajusta los valores de píxeles de una imagen de entrada mediante un proceso de normalización matemática. Resta un valor medio especificado de cada píxel y luego divide el resultado por una desviación estándar especificada. Este es un paso de preprocesamiento común para preparar datos de imagen para otros modelos de aprendizaje automático.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `image` | La imagen de entrada que se va a normalizar. | IMAGE | Sí | - |
| `media` | Valor medio para la normalización (predeterminado: 0.5). | FLOAT | No | 0.0 - 1.0 |
| `desviación estándar` | Desviación estándar para la normalización (predeterminado: 0.5). | FLOAT | No | 0.001 - 1.0 |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `imágenes` | La imagen resultante después de aplicar el proceso de normalización. | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/NormalizeImages/es.md)

---
**Source fingerprint (SHA-256):** `9d08c8dba7d13c6f255ed786d3d2d3005bce425dc04b14b7199d868c3fc81fd9`
