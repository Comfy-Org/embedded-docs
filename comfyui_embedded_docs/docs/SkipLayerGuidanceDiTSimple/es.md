> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SkipLayerGuidanceDiTSimple/es.md)

Versión simplificada del nodo SkipLayerGuidanceDiT que solo modifica la pasada incondicional durante el proceso de eliminación de ruido. Este nodo aplica guía de capa de salto a capas específicas del transformador en modelos DiT (Diffusion Transformer) omitiendo selectivamente ciertas capas durante la pasada incondicional según los parámetros de tiempo y capa especificados.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Sí | - | El modelo al que aplicar la guía de capa de salto |
| `double_layers` | STRING | Sí | - | Lista separada por comas de índices de capas de bloque doble a omitir (valor por defecto: "7, 8, 9") |
| `single_layers` | STRING | Sí | - | Lista separada por comas de índices de capas de bloque simple a omitir (valor por defecto: "7, 8, 9") |
| `start_percent` | FLOAT | Sí | 0.0 - 1.0 | Porcentaje inicial del proceso de eliminación de ruido cuando comienza la guía de capa de salto (valor por defecto: 0.0) |
| `end_percent` | FLOAT | Sí | 0.0 - 1.0 | Porcentaje final del proceso de eliminación de ruido cuando se detiene la guía de capa de salto (valor por defecto: 1.0) |

**Nota:** La guía de capa de salto solo se aplica cuando tanto `double_layers` como `single_layers` contienen índices de capa válidos. Si ambos están vacíos, el nodo devuelve el modelo original sin cambios.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `model` | MODEL | El modelo modificado con la guía de capa de salto aplicada a las capas especificadas |