> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KarrasScheduler/es.md)

El nodo KarrasScheduler está diseñado para generar una secuencia de niveles de ruido (sigmas) basada en el programador de ruido de Karras et al. (2022). Este programador es útil para controlar el proceso de difusión en modelos generativos, permitiendo ajustes precisos en los niveles de ruido aplicados en cada paso del proceso de generación.

## Entradas

| Parámetro   | Tipo de Dato | Descripción                                                                                      |
|-------------|--------------|------------------------------------------------------------------------------------------------|
| `steps`     | INT          | Especifica el número de pasos en el programador de ruido, afectando la granularidad de la secuencia de sigmas generada. |
| `sigma_max` | FLOAT        | El valor máximo de sigma en el programador de ruido, estableciendo el límite superior de los niveles de ruido. |
| `sigma_min` | FLOAT        | El valor mínimo de sigma en el programador de ruido, estableciendo el límite inferior de los niveles de ruido. |
| `rho`       | FLOAT        | Un parámetro que controla la forma de la curva del programador de ruido, influyendo en cómo los niveles de ruido progresan desde sigma_min hasta sigma_max. |

## Salidas

| Parámetro | Tipo de Dato | Descripción                                                                 |
|-----------|--------------|-----------------------------------------------------------------------------|
| `sigmas`  | SIGMAS       | La secuencia generada de niveles de ruido (sigmas) siguiendo el programador de ruido de Karras et al. (2022). |