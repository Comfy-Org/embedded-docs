
Este nodo está diseñado para mejorar las capacidades de muestreo de un modelo al integrar técnicas de muestreo EDM (Modelos de Difusión Basados en Energía) continuas. Permite el ajuste dinámico de los niveles de ruido dentro del proceso de muestreo del modelo, ofreciendo un control más refinado sobre la calidad y diversidad de la generación.

## Entradas

| Parámetro   | Tipo de Dato | Tipo Python        | Descripción |
|-------------|--------------|----------------------|-------------|
| `model`     | `MODEL`     | `torch.nn.Module`   | El modelo que se mejorará con capacidades de muestreo EDM continuas. Sirve como base para aplicar las técnicas de muestreo avanzadas. |
| `sampling`  | COMBO[STRING] | `str`             | Especifica el tipo de muestreo que se aplicará, ya sea 'eps' para muestreo epsilon o 'v_prediction' para predicción de velocidad, influyendo en el comportamiento del modelo durante el proceso de muestreo. |
| `sigma_max` | `FLOAT`     | `float`             | El valor máximo de sigma para el nivel de ruido, permitiendo el control del límite superior en el proceso de inyección de ruido durante el muestreo. |
| `sigma_min` | `FLOAT`     | `float`             | El valor mínimo de sigma para el nivel de ruido, estableciendo el límite inferior para la inyección de ruido, afectando así la precisión del muestreo del modelo. |

## Salidas

| Parámetro | Tipo de Dato | Tipo Python        | Descripción |
|-----------|-------------|----------------------|-------------|
| `model`   | MODEL     | `torch.nn.Module`   | El modelo mejorado con capacidades de muestreo EDM continuas integradas, listo para su uso en tareas de generación.
