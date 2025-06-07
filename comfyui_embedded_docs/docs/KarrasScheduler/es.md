El nodo KarrasScheduler está diseñado para generar una secuencia de niveles de ruido (sigmas) basada en el programa de ruido de Karras et al. (2022). Este programador es útil para controlar el proceso de difusión en modelos generativos, permitiendo ajustes finos a los niveles de ruido aplicados en cada paso del proceso de generación.

## Entradas

| Parameter   | Data Type | Description                                                                                      |
|-------------|-------------|------------------------------------------------------------------------------------------------|
| `steps`     | INT         | Especifica el número de pasos en el programa de ruido, afectando la granularidad de la secuencia de sigmas generada. |
| `sigma_max` | FLOAT       | El valor máximo de sigma en el programa de ruido, estableciendo el límite superior de los niveles de ruido.                    |
| `sigma_min` | FLOAT       | El valor mínimo de sigma en el programa de ruido, estableciendo el límite inferior de los niveles de ruido.                    |
| `rho`       | FLOAT       | Un parámetro que controla la forma de la curva del programa de ruido, influyendo en cómo progresan los niveles de ruido de sigma_min a sigma_max. |

## Salidas

| Parameter | Data Type | Description                                                                 |
|-----------|-------------|-----------------------------------------------------------------------------|
| `sigmas`  | SIGMAS      | La secuencia generada de niveles de ruido (sigmas) siguiendo el programa de ruido de Karras et al. (2022). |
