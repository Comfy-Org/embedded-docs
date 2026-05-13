> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CFGNorm/es.md)

El nodo CFGNorm aplica una técnica de normalización al proceso de guía sin clasificador (CFG) en modelos de difusión. Ajusta la escala de la predicción con eliminación de ruido comparando las normas de las salidas condicionales e incondicionales, y luego aplica un multiplicador de intensidad para controlar el efecto. Esto ayuda a estabilizar el proceso de generación al prevenir valores extremos en el escalado de la guía.

## Entradas

| Parámetro | Tipo de Dato | Tipo de Entrada | Valor por Defecto | Rango | Descripción |
|-----------|--------------|-----------------|-------------------|-------|-------------|
| `model` | MODEL | requerido | - | - | El modelo de difusión al que se le aplicará la normalización CFG |
| `strength` | FLOAT | requerido | 1.0 | 0.0 - 100.0 | Controla la intensidad del efecto de normalización aplicado al escalado CFG |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `patched_model` | MODEL | Devuelve el modelo modificado con la normalización CFG aplicada a su proceso de muestreo |

---
**Source fingerprint (SHA-256):** `af9e5f965500b959ff46f781e9329524fc0a4b94af2ce6d74116fe27b0e9005e`
