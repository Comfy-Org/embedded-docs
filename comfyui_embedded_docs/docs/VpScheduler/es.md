
El nodo VPScheduler está diseñado para generar una secuencia de niveles de ruido (sigmas) basada en el método de programación de Preservación de Varianza (VP). Esta secuencia es crucial para guiar el proceso de eliminación de ruido en modelos de difusión, permitiendo la generación controlada de imágenes u otros tipos de datos.

## Entradas

| Parámetro   | Data Type | Descripción                                                                                                                                      |
|-------------|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| `steps`     | INT         | Especifica el número de pasos en el proceso de difusión, afectando la granularidad de los niveles de ruido generados.                              |
| `beta_d`    | FLOAT       | Determina la distribución general del nivel de ruido, influyendo en la varianza de los niveles de ruido generados.                                 |
| `beta_min`  | FLOAT       | Establece el límite mínimo para el nivel de ruido, asegurando que el ruido no caiga por debajo de un cierto umbral.                              |
| `eps_s`     | FLOAT       | Ajusta el valor inicial de epsilon, afinando el nivel de ruido inicial en el proceso de difusión.                                    |

## Salidas

| Parámetro   | Data Type | Descripción                                                                                   |
|-------------|-------------|-----------------------------------------------------------------------------------------------|
| `sigmas`    | SIGMAS      | Una secuencia de niveles de ruido (sigmas) generada basada en el método de programación VP, utilizada para guiar el proceso de eliminación de ruido en modelos de difusión. |
