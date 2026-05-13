> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingContinuousEDM/es.md)

Este nodo está diseñado para mejorar las capacidades de muestreo de un modelo mediante la integración de técnicas continuas de muestreo EDM (Modelos de Difusión Basados en Energía). Permite el ajuste dinámico de los niveles de ruido dentro del proceso de muestreo del modelo, ofreciendo un control más refinado sobre la calidad y diversidad de la generación.

## Entradas

| Parámetro   | Tipo de dato | Tipo Python        | Descripción |
|-------------|--------------|----------------------|-------------|
| `model`     | `MODEL`     | `torch.nn.Module`   | El modelo a mejorar con capacidades continuas de muestreo EDM. Sirve como base para aplicar las técnicas avanzadas de muestreo. |
| `muestreo`  | COMBO[STRING] | `str`             | Especifica el tipo de muestreo a aplicar, ya sea 'eps' para muestreo épsilon o 'v_prediction' para predicción de velocidad, influyendo en el comportamiento del modelo durante el proceso de muestreo. |
| `sigma_max` | `FLOAT`     | `float`             | El valor sigma máximo para el nivel de ruido, permitiendo un control del límite superior en el proceso de inyección de ruido durante el muestreo. |
| `sigma_min` | `FLOAT`     | `float`             | El valor sigma mínimo para el nivel de ruido, estableciendo el límite inferior para la inyección de ruido, afectando así la precisión del muestreo del modelo. |

## Salidas

| Parámetro | Tipo de dato | Tipo Python        | Descripción |
|-----------|-------------|----------------------|-------------|
| `model`   | MODEL     | `torch.nn.Module`   | El modelo mejorado con capacidades integradas de muestreo EDM continuo, listo para su uso posterior en tareas de generación. |