> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PerpNeg/es.md)

El nodo PerpNeg aplica guía negativa perpendicular al proceso de muestreo de un modelo. Este nodo modifica la función de configuración del modelo para ajustar las predicciones de ruido utilizando condicionamiento negativo y factores de escala. Ha quedado obsoleto y ha sido reemplazado por el nodo PerpNegGuider para una funcionalidad mejorada.

## Entradas

| Parámetro | Tipo de dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `model` | MODEL | Sí | - | El modelo al que se aplicará la guía negativa perpendicular |
| `empty_conditioning` | CONDITIONING | Sí | - | Condicionamiento vacío utilizado para los cálculos de guía negativa |
| `neg_scale` | FLOAT | No | 0.0 - 100.0 | Factor de escala para la guía negativa (predeterminado: 1.0) |

## Salidas

| Nombre de salida | Tipo de dato | Descripción |
|------------------|--------------|-------------|
| `model` | MODEL | El modelo modificado con guía negativa perpendicular aplicada |

**Nota**: Este nodo está obsoleto y ha sido reemplazado por PerpNegGuider. Está marcado como experimental y no debe utilizarse en flujos de trabajo de producción.

---
**Source fingerprint (SHA-256):** `6be4ab03cfbda33ed3966ecd579c1a5e3242bdfb163fecefb9c80073a8827cae`
