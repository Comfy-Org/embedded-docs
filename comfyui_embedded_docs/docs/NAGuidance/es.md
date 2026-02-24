> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/NAGuidance/es.md)

El nodo NAGuidance aplica Orientación de Atención Normalizada a un modelo. Esta técnica permite el uso de indicaciones negativas con modelos destilados o schnell modificando el mecanismo de atención del modelo durante el proceso de muestreo para dirigir la generación lejos de conceptos no deseados.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Sí | - | El modelo al que se aplicará la Orientación de Atención Normalizada. |
| `nag_scale` | FLOAT | Sí | 0.0 - 50.0 | El factor de escala de orientación. Valores más altos alejan más la generación de la indicación negativa. (por defecto: 5.0) |
| `nag_alpha` | FLOAT | Sí | 0.0 - 1.0 | El factor de mezcla para la atención normalizada. Un valor de 1.0 reemplaza completamente la atención original, mientras que 0.0 no tiene efecto. (por defecto: 0.5) |
| `nag_tau` | FLOAT | Sí | 1.0 - 10.0 | Un factor de escala utilizado para limitar la relación de normalización. (por defecto: 1.5) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `model` | MODEL | El modelo modificado con la Orientación de Atención Normalizada activada. |