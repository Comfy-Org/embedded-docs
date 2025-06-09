
Este nodo está diseñado para generar un muestrador para el modelo DPMPP_2M_SDE, permitiendo la creación de muestras basadas en tipos de solucionadores especificados, niveles de ruido y preferencias de dispositivo computacional. Abstrae las complejidades de la configuración del muestrador, proporcionando una interfaz simplificada para generar muestras con configuraciones personalizadas.

## Entradas

| Parámetro       | Data Type | Descripción                                                                 |
|-----------------|-------------|-----------------------------------------------------------------------------|
| `solver_type`   | COMBO[STRING] | Especifica el tipo de solucionador que se utilizará en el proceso de muestreo, ofreciendo opciones entre 'midpoint' y 'heun'. Esta elección influye en el método de integración numérica aplicado durante el muestreo. |
| `eta`           | `FLOAT`     | Determina el tamaño del paso en la integración numérica, afectando la granularidad del proceso de muestreo. Un valor más alto indica un tamaño de paso mayor. |
| `s_noise`       | `FLOAT`     | Controla el nivel de ruido introducido durante el proceso de muestreo, influyendo en la variabilidad de las muestras generadas. |
| `noise_device`  | COMBO[STRING] | Indica el dispositivo computacional ('gpu' o 'cpu') en el cual se ejecuta el proceso de generación de ruido, afectando el rendimiento y la eficiencia. |

## Salidas

| Parámetro       | Data Type | Descripción                                                                 |
|-----------------|-------------|-----------------------------------------------------------------------------|
| `sampler`       | `SAMPLER`   | La salida es un muestrador configurado según los parámetros especificados, listo para generar muestras. |
