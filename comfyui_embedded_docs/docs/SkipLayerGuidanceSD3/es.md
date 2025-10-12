> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SkipLayerGuidanceSD3/es.md)

El nodo SkipLayerGuidanceSD3 mejora la guía hacia una estructura detallada aplicando un conjunto adicional de guía libre de clasificador con capas omitidas. Esta implementación experimental está inspirada en Perturbed Attention Guidance y funciona omitiendo selectivamente ciertas capas durante el proceso de condicionamiento negativo para mejorar los detalles estructurales en la salida generada.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `modelo` | MODEL | Sí | - | El modelo al que aplicar la guía de capas omitidas |
| `capas` | STRING | Sí | - | Lista separada por comas de índices de capas a omitir (valor por defecto: "7, 8, 9") |
| `escala` | FLOAT | Sí | 0.0 - 10.0 | La intensidad del efecto de guía de capas omitidas (valor por defecto: 3.0) |
| `porcentaje_inicio` | FLOAT | Sí | 0.0 - 1.0 | El punto de inicio de la aplicación de la guía como porcentaje del total de pasos (valor por defecto: 0.01) |
| `porcentaje_final` | FLOAT | Sí | 0.0 - 1.0 | El punto final de la aplicación de la guía como porcentaje del total de pasos (valor por defecto: 0.15) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `modelo` | MODEL | El modelo modificado con la guía de capas omitidas aplicada |