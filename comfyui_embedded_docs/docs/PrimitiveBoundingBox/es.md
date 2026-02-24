> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PrimitiveBoundingBox/es.md)

El nodo PrimitiveBoundingBox crea un área rectangular simple definida por su posición y tamaño. Toma coordenadas X e Y para la esquina superior izquierda, junto con valores de ancho y alto, y genera una estructura de datos de cuadro delimitador que puede ser utilizada por otros nodos en un flujo de trabajo.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `x` | INT | No | 0 a 8192 | La coordenada X para la esquina superior izquierda del cuadro delimitador (por defecto: 0). |
| `y` | INT | No | 0 a 8192 | La coordenada Y para la esquina superior izquierda del cuadro delimitador (por defecto: 0). |
| `width` | INT | No | 1 a 8192 | El ancho del cuadro delimitador (por defecto: 512). |
| `height` | INT | No | 1 a 8192 | La altura del cuadro delimitador (por defecto: 512). |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `bounding_box` | BOUNDING_BOX | Una estructura de datos que contiene las propiedades `x`, `y`, `width` y `height` del rectángulo definido. |
