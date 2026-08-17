# Caja Delimitadora

El nodo PrimitiveBoundingBox crea un área rectangular simple definida por su posición y tamaño. Toma las coordenadas X e Y para la esquina superior izquierda, junto con los valores de ancho y alto, y genera una estructura de datos de bounding box que puede ser utilizada por otros nodos en un flujo de trabajo.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `x` | La coordenada X de la esquina superior izquierda del bounding box (por defecto: 0). | INT | Sí | 0 a 8192 |
| `y` | La coordenada Y de la esquina superior izquierda del bounding box (por defecto: 0). | INT | Sí | 0 a 8192 |
| `width` | El ancho del bounding box (por defecto: 512). | INT | Sí | 1 a 8192 |
| `height` | El alto del bounding box (por defecto: 512). | INT | Sí | 1 a 8192 |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `bounding_box` | Una estructura de datos que contiene las propiedades `x`, `y`, `width` y `height` del rectángulo definido. | BOUNDING_BOX |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PrimitiveBoundingBox/es.md)

---
**Source fingerprint (SHA-256):** `dc50286b09b8aaf7ff21eb699b9a04317f099b3deedb6cb7d4a1ec7668edeb97`
