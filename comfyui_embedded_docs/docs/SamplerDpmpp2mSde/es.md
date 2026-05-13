> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDpmpp2mSde/es.md)

Este nodo está diseñado para generar un muestreador para el modelo DPMPP_2M_SDE, permitiendo la creación de muestras basadas en tipos de solucionador, niveles de ruido y preferencias de dispositivo computacional especificados. Abstrae las complejidades de la configuración del muestreador, proporcionando una interfaz simplificada para generar muestras con configuraciones personalizadas.

## Entradas

| Parámetro       | Tipo de Dato | Descripción                                                                 |
|-----------------|-------------|-----------------------------------------------------------------------------|
| `solver_type`   | COMBO[STRING] | Especifica el tipo de solucionador a utilizar en el proceso de muestreo, ofreciendo opciones entre 'midpoint' y 'heun'. Esta elección influye en el método de integración numérica aplicado durante el muestreo. |
| `eta`           | `FLOAT`     | Determina el tamaño de paso en la integración numérica, afectando la granularidad del proceso de muestreo. Un valor más alto indica un tamaño de paso mayor. |
| `s_noise`       | `FLOAT`     | Controla el nivel de ruido introducido durante el proceso de muestreo, influyendo en la variabilidad de las muestras generadas. |
| `noise_device`  | COMBO[STRING] | Indica el dispositivo computacional ('gpu' o 'cpu') en el que se ejecuta el proceso de generación de ruido, afectando el rendimiento y la eficiencia. |

## Salidas

| Parámetro       | Tipo de Dato | Descripción                                                                 |
|-----------------|-------------|-----------------------------------------------------------------------------|
| `sampler`       | `SAMPLER`   | La salida es un muestreador configurado según los parámetros especificados, listo para generar muestras. |