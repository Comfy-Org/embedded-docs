El nodo `ExponentialScheduler` está diseñado para generar una secuencia de valores sigma siguiendo un programa exponencial para procesos de muestreo de difusión. Proporciona un enfoque personalizable para controlar los niveles de ruido aplicados en cada paso del proceso de difusión, permitiendo un ajuste fino del comportamiento de muestreo.

## Entradas

| Parámetro   | Data Type | Descripción                                                                                   |
|-------------|-------------|---------------------------------------------------------------------------------------------|
| `steps`     | INT         | Especifica el número de pasos en el proceso de difusión. Influye en la longitud de la secuencia de sigma generada y, por lo tanto, en la granularidad de la aplicación de ruido. |
| `sigma_max` | FLOAT       | Define el valor máximo de sigma, estableciendo el límite superior de la intensidad del ruido en el proceso de difusión. Juega un papel crucial en la determinación del rango de niveles de ruido aplicados. |
| `sigma_min` | FLOAT       | Establece el valor mínimo de sigma, determinando el límite inferior de la intensidad del ruido. Este parámetro ayuda a ajustar el punto de inicio de la aplicación de ruido. |

## Salidas

| Parámetro | Data Type | Descripción                                                                                   |
|-----------|-------------|---------------------------------------------------------------------------------------------|
| `sigmas`  | SIGMAS      | Una secuencia de valores sigma generada según el programa exponencial. Estos valores se utilizan para controlar los niveles de ruido en cada paso del proceso de difusión. |
