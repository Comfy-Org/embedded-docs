# Caja Delimitadora

El nodo PrimitiveBoundingBox crea un área rectangular simple definida por su posición y tamaño. Toma coordenadas X e Y para la esquina superior izquierda, junto con valores de ancho y alto, y genera una estructura de datos de cuadro delimitador que puede ser utilizada por otros nodos en un flujo de trabajo.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `x` | La coordenada X de la esquina superior izquierda del cuadro delimitador (predeterminado: 0). | INT | Sí | 0 a 8192 |
| `y` | La coordenada Y de la esquina superior izquierda del cuadro delimitador (predeterminado: 0). | INT | Sí | 0 a 8192 |
| `width` | El ancho del cuadro delimitador (predeterminado: 512). | INT | Sí | 1 a 8192 |
| `height` | La altura del cuadro delimitador (predeterminado: 512). | INT | Sí | 1 a 8192 |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `bounding_box` | Una estructura de datos que contiene las propiedades `x`, `y`, `width` y `height` del rectángulo definido. | BOUNDING_BOX |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PrimitiveBoundingBox/es.md)

---
**Source fingerprint (SHA-256):** `715f1a2bd650ecd6ba2ea3c1d54636bc32dff4fb4aec8f088ee9b0994809412c`
