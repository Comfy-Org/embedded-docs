> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KSamplerSelect/es.md)

El nodo KSamplerSelect está diseñado para seleccionar un muestreador específico basado en el nombre proporcionado. Abstrae la complejidad de la selección del muestreador, permitiendo a los usuarios cambiar fácilmente entre diferentes estrategias de muestreo para sus tareas.

## Entradas

| Parámetro         | Tipo de Dato | Descripción                                                                                      |
|-------------------|-------------|------------------------------------------------------------------------------------------------|
| `sampler_name`    | COMBO[STRING] | Especifica el nombre del muestreador a seleccionar. Este parámetro determina qué estrategia de muestreo se utilizará, afectando el comportamiento general del muestreo y los resultados. |

## Salidas

| Parámetro   | Tipo de Dato | Descripción                                                                 |
|-------------|-------------|-----------------------------------------------------------------------------|
| `sampler`   | `SAMPLER`   | Devuelve el objeto muestreador seleccionado, listo para ser utilizado en tareas de muestreo. |