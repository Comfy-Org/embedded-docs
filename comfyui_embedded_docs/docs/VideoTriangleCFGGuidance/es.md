> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VideoTriangleCFGGuidance/es.md)

El nodo VideoTriangleCFGGuidance aplica un patrón triangular de escalado de guía libre de clasificador a modelos de video. Modifica la escala de condicionamiento a lo largo del tiempo utilizando una función de onda triangular que oscila entre el valor mínimo de CFG y la escala de condicionamiento original. Esto crea un patrón de guía dinámico que puede ayudar a mejorar la consistencia y calidad de la generación de video.

## Entradas

| Parámetro | Tipo de Datos | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Sí | - | El modelo de video al que aplicar la guía triangular de CFG |
| `min_cfg` | FLOAT | Sí | 0.0 - 100.0 | El valor mínimo de escala CFG para el patrón triangular (por defecto: 1.0) |

## Salidas

| Nombre de Salida | Tipo de Datos | Descripción |
|-------------|-----------|-------------|
| `model` | MODEL | El modelo modificado con la guía triangular de CFG aplicada |