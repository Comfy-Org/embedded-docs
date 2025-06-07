El nodo KSamplerSelect está diseñado para seleccionar un sampler específico basado en el nombre del sampler proporcionado. Abstrae la complejidad de la selección de samplers, permitiendo a los usuarios cambiar fácilmente entre diferentes estrategias de muestreo para sus tareas.

## Entradas

| Parámetro         | Data Type | Descripción                                                                                      |
|-------------------|-------------|------------------------------------------------------------------------------------------------|
| `sampler_name`    | COMBO[STRING] | Especifica el nombre del sampler que se seleccionará. Este parámetro determina qué estrategia de muestreo se utilizará, afectando el comportamiento general del muestreo y los resultados. |

## Salidas

| Parámetro   | Data Type | Descripción                                                                 |
|-------------|-------------|-----------------------------------------------------------------------------|
| `sampler`   | `SAMPLER`   | Devuelve el objeto sampler seleccionado, listo para ser utilizado en tareas de muestreo. |
