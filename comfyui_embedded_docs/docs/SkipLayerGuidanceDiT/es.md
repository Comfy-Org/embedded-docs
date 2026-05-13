> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SkipLayerGuidanceDiT/es.md)

Mejora la guía hacia una estructura detallada utilizando otro conjunto de CFG negativo con capas omitidas. Esta versión genérica de SkipLayerGuidance puede usarse en cualquier modelo DiT y está inspirada en Perturbed Attention Guidance. La implementación experimental original fue creada para SD3.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|---------------|-------------|-------|-------------|
| `model` | MODEL | Sí | - | El modelo al que se aplicará la guía de capas omitidas |
| `double_layers` | STRING | Sí | - | Números de capa separados por comas para bloques dobles a omitir (predeterminado: "7, 8, 9") |
| `single_layers` | STRING | Sí | - | Números de capa separados por comas para bloques individuales a omitir (predeterminado: "7, 8, 9") |
| `scale` | FLOAT | Sí | 0.0 - 10.0 | Factor de escala de guía (predeterminado: 3.0) |
| `start_percent` | FLOAT | Sí | 0.0 - 1.0 | Porcentaje inicial para la aplicación de la guía (predeterminado: 0.01) |
| `end_percent` | FLOAT | Sí | 0.0 - 1.0 | Porcentaje final para la aplicación de la guía (predeterminado: 0.15) |
| `rescaling_scale` | FLOAT | Sí | 0.0 - 10.0 | Factor de escala de reescalado para ajustar la magnitud de salida (predeterminado: 0.0, sin reescalado) |

**Nota:** Si tanto `double_layers` como `single_layers` están vacíos (no contienen números de capa), el nodo devuelve el modelo original sin aplicar ninguna guía.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|---------------|-------------|
| `model` | MODEL | El modelo modificado con la guía de capas omitidas aplicada |

---
**Source fingerprint (SHA-256):** `cf494fbeb33e7bc3b3f798e9e9b025623afad4ea6340ef628caa776c7d42ba12`
