
El nodo PolyexponentialScheduler está diseñado para generar una secuencia de niveles de ruido (sigmas) basada en un programa de ruido poliexponencial. Este programa es una función polinómica en el logaritmo de sigma, permitiendo una progresión flexible y personalizable de los niveles de ruido a lo largo del proceso de difusión.

## Entradas

| Parámetro   | Data Type | Descripción                                                                                                                                                                                                                                                                                                                                                      |
|-------------|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `steps`     | INT         | Especifica el número de pasos en el proceso de difusión, afectando la granularidad de los niveles de ruido generados.                                                                                                                                                                                                                                                                        |
| `sigma_max` | FLOAT       | El nivel máximo de ruido, estableciendo el límite superior del programa de ruido.                                                                                                                                                                                                                                                                                                                                 |
| `sigma_min` | FLOAT       | El nivel mínimo de ruido, estableciendo el límite inferior del programa de ruido.                                                                                                                                                                                                                                                                                                                                 |
| `rho`       | FLOAT       | Un parámetro que controla la forma del programa de ruido poliexponencial, influyendo en cómo progresan los niveles de ruido entre los valores mínimo y máximo.                                                                                                                                                                                                               |

## Salidas

| Parámetro | Data Type | Descripción                                                                 |
|-----------|-------------|-----------------------------------------------------------------------------|
| `sigmas`  | SIGMAS      | La salida es una secuencia de niveles de ruido (sigmas) adaptada al programa de ruido poliexponencial especificado. |
