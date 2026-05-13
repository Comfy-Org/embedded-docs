> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ExponentialScheduler/es.md)

El nodo `ExponentialScheduler` está diseñado para generar una secuencia de valores sigma siguiendo un programa exponencial para procesos de muestreo por difusión. Proporciona un enfoque personalizable para controlar los niveles de ruido aplicados en cada paso del proceso de difusión, permitiendo un ajuste fino del comportamiento del muestreo.

## Entradas

| Parámetro   | Tipo de Dato | Descripción                                                                                   |
|-------------|--------------|-----------------------------------------------------------------------------------------------|
| `pasos`     | INT          | Especifica el número de pasos en el proceso de difusión. Influye en la longitud de la secuencia sigma generada y, por lo tanto, en la granularidad de la aplicación del ruido. |
| `sigma_max` | FLOAT        | Define el valor sigma máximo, estableciendo el límite superior de intensidad de ruido en el proceso de difusión. Desempeña un papel crucial en la determinación del rango de niveles de ruido aplicados. |
| `sigma_min` | FLOAT        | Establece el valor sigma mínimo, fijando el límite inferior de intensidad de ruido. Este parámetro ayuda a ajustar el punto de inicio de la aplicación del ruido. |

## Salidas

| Parámetro | Tipo de Dato | Descripción                                                                                   |
|-----------|--------------|-----------------------------------------------------------------------------------------------|
| `sigmas`  | SIGMAS       | Una secuencia de valores sigma generados según el programa exponencial. Estos valores se utilizan para controlar los niveles de ruido en cada paso del proceso de difusión. |