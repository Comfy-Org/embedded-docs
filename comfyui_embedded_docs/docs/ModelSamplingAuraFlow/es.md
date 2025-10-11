> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingAuraFlow/es.md)

El nodo ModelSamplingAuraFlow aplica una configuración de muestreo especializada a modelos de difusión, diseñada específicamente para arquitecturas de modelo AuraFlow. Modifica el comportamiento de muestreo del modelo aplicando un parámetro de desplazamiento que ajusta la distribución de muestreo. Este nodo hereda del framework de muestreo de modelos SD3 y proporciona un control preciso sobre el proceso de muestreo.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Sí | - | El modelo de difusión al que aplicar la configuración de muestreo AuraFlow |
| `shift` | FLOAT | Sí | 0.0 - 100.0 | El valor de desplazamiento a aplicar a la distribución de muestreo (por defecto: 1.73) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `model` | MODEL | El modelo modificado con la configuración de muestreo AuraFlow aplicada |