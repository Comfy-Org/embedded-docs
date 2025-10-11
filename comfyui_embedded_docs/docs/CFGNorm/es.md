> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CFGNorm/es.md)

El nodo CFGNorm aplica una técnica de normalización al proceso de guía libre de clasificador (CFG) en modelos de difusión. Ajusta la escala de la predicción desruidificada comparando las normas de las salidas condicionales e incondicionales, y luego aplica un multiplicador de fuerza para controlar el efecto. Esto ayuda a estabilizar el proceso de generación previniendo valores extremos en el escalado de guía.

## Entradas

| Parámetro | Tipo de Dato | Tipo de Entrada | Por Defecto | Rango | Descripción |
|-----------|-----------|------------|---------|-------|-------------|
| `model` | MODEL | requerido | - | - | El modelo de difusión al que aplicar la normalización CFG |
| `strength` | FLOAT | requerido | 1.0 | 0.0 - 100.0 | Controla la intensidad del efecto de normalización aplicado al escalado CFG |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `patched_model` | MODEL | Devuelve el modelo modificado con normalización CFG aplicada a su proceso de muestreo |