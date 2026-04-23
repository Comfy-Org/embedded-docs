> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TencentSmartTopologyNode/es.md)

Este nodo realiza una retopología inteligente en un modelo 3D, que es el proceso de crear automáticamente una nueva malla más limpia con un recuento de polígonos más bajo. Se conecta a una API Tencent Hunyuan 3D para procesar el modelo, admitiendo formatos de archivo GLB y OBJ. El nodo devuelve el modelo procesado como un archivo OBJ.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `model_3d` | FILE3D | Sí | - | Modelo 3D de entrada (GLB u OBJ). El archivo debe estar en formato GLB u OBJ y no puede superar los 200MB. |
| `polygon_type` | STRING | Sí | `"triangle"`<br>`"quadrilateral"` | Tipo de composición de la superficie. |
| `face_level` | STRING | Sí | `"medium"`<br>`"high"`<br>`"low"` | Nivel de reducción de polígonos. |
| `seed` | INT | No | 0 a 2147483647 | La semilla controla si el nodo debe volver a ejecutarse; los resultados no son deterministas independientemente de la semilla. (por defecto: 0) |

**Nota:** El parámetro `seed` se utiliza para activar una re-ejecución del nodo, pero no se garantiza que la salida final sea la misma para un mismo valor de semilla.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `OBJ` | FILE3D | El modelo 3D procesado con topología optimizada, devuelto en formato OBJ. |