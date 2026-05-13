> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SkipLayerGuidanceDiTSimple/es.md)

Versión simplificada del nodo SkipLayerGuidanceDiT que solo modifica el paso incondicional durante el proceso de eliminación de ruido. Este nodo aplica guía de salto de capas a capas específicas del transformador en modelos DiT (Diffusion Transformer) omitiendo selectivamente ciertas capas durante el paso incondicional según los parámetros de temporización y capas especificados.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Sí | - | El modelo al que se aplicará la guía de salto de capas |
| `double_layers` | STRING | No | - | Lista separada por comas de índices de capas de bloques dobles a omitir (predeterminado: "7, 8, 9") |
| `single_layers` | STRING | No | - | Lista separada por comas de índices de capas de bloques individuales a omitir (predeterminado: "7, 8, 9") |
| `start_percent` | FLOAT | No | 0.0 - 1.0 | El porcentaje inicial del proceso de eliminación de ruido cuando comienza la guía de salto de capas (predeterminado: 0.0) |
| `end_percent` | FLOAT | No | 0.0 - 1.0 | El porcentaje final del proceso de eliminación de ruido cuando finaliza la guía de salto de capas (predeterminado: 1.0) |

**Nota:** La guía de salto de capas solo se aplica cuando tanto `double_layers` como `single_layers` contienen índices de capas válidos. Si ambos están vacíos, el nodo devuelve el modelo original sin cambios. La guía de salto de capas está activa únicamente cuando el valor sigma del paso actual de eliminación de ruido se encuentra entre `start_percent` y `end_percent` (convertidos internamente a valores sigma).

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `model` | MODEL | El modelo modificado con guía de salto de capas aplicada a las capas especificadas |

---
**Source fingerprint (SHA-256):** `6795a67a63d9aa8b2adea3d96e49272d88c21d0642bb507e175a2fcf3a125f98`
