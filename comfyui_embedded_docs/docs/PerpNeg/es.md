> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PerpNeg/es.md)

El nodo PerpNeg aplica guía negativa perpendicular al proceso de muestreo de un modelo. Este nodo modifica la función de configuración del modelo para ajustar las predicciones de ruido utilizando condicionamiento negativo y factores de escala. Ha quedado obsoleto y ha sido reemplazado por el nodo PerpNegGuider para una funcionalidad mejorada.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Sí | - | El modelo al que aplicar la guía negativa perpendicular |
| `empty_conditioning` | CONDITIONING | Sí | - | Condicionamiento vacío utilizado para los cálculos de guía negativa |
| `neg_scale` | FLOAT | No | 0.0 - 100.0 | Factor de escala para la guía negativa (por defecto: 1.0) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `model` | MODEL | El modelo modificado con la guía negativa perpendicular aplicada |

**Nota**: Este nodo está obsoleto y ha sido reemplazado por PerpNegGuider. Está marcado como experimental y no debe utilizarse en flujos de trabajo de producción.