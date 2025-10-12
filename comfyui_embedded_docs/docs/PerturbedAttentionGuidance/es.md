> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PerturbedAttentionGuidance/es.md)

El nodo PerturbedAttentionGuidance aplica guía de atención perturbada a un modelo de difusión para mejorar la calidad de generación. Modifica el mecanismo de auto-atención del modelo durante el muestreo reemplazándolo con una versión simplificada que se enfoca en las proyecciones de valor. Esta técnica ayuda a mejorar la coherencia y calidad de las imágenes generadas ajustando el proceso de eliminación de ruido condicional.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `modelo` | MODEL | Sí | - | El modelo de difusión al que aplicar la guía de atención perturbada |
| `escala` | FLOAT | No | 0.0 - 100.0 | La intensidad del efecto de guía de atención perturbada (por defecto: 3.0) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `modelo` | MODEL | El modelo modificado con la guía de atención perturbada aplicada |
