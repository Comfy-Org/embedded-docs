> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PerpNegGuider/es.md)

El nodo PerpNegGuider crea un sistema de guía para controlar la generación de imágenes mediante condicionamiento negativo perpendicular. Toma entradas de condicionamiento positivo, negativo y vacío, y aplica un algoritmo de guía especializado para dirigir el proceso de generación. Este nodo está diseñado para pruebas experimentales y proporciona un control preciso sobre la intensidad de la guía y la escala negativa.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `modelo` | MODEL | Sí | - | El modelo a utilizar para la generación de guía |
| `positivo` | CONDITIONING | Sí | - | El condicionamiento positivo que dirige la generación hacia el contenido deseado |
| `negativo` | CONDITIONING | Sí | - | El condicionamiento negativo que aleja la generación del contenido no deseado |
| `condicionamiento_vacío` | CONDITIONING | Sí | - | El condicionamiento vacío o neutral utilizado como referencia base |
| `cfg` | FLOAT | Sí | 0.0 - 100.0 | La escala de guía libre de clasificador que controla la intensidad con la que el condicionamiento influye en la generación (predeterminado: 8.0) |
| `escala_neg` | FLOAT | Sí | 0.0 - 100.0 | El factor de escala negativa que ajusta la intensidad del condicionamiento negativo (predeterminado: 1.0) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `guider` | GUIDER | Un sistema de guía configurado listo para usar en el proceso de generación |

---
**Source fingerprint (SHA-256):** `efd3f78d461ade9d16885923875bacffb5afeafcbe32fc2d207598e0efe3a8c6`
