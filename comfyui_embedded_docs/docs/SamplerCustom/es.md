> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerCustom/es.md)

El nodo SamplerCustom está diseñado para proporcionar un mecanismo de muestreo flexible y personalizable para diversas aplicaciones. Permite a los usuarios seleccionar y configurar diferentes estrategias de muestreo adaptadas a sus necesidades específicas, mejorando la adaptabilidad y eficiencia del proceso de muestreo.

## Entradas

| Parámetro | Tipo de Dato | Descripción |
|-----------|--------------|-------------|
| `modelo`   | `MODEL`      | El tipo de entrada 'model' especifica el modelo que se utilizará para el muestreo, desempeñando un papel crucial en la determinación del comportamiento y la salida del muestreo. |
| `añadir_ruido` | `BOOLEAN`    | El tipo de entrada 'add_noise' permite a los usuarios especificar si se debe agregar ruido al proceso de muestreo, influyendo en la diversidad y las características de las muestras generadas. |
| `semilla_ruido` | `INT`        | El tipo de entrada 'noise_seed' proporciona una semilla para la generación de ruido, garantizando la reproducibilidad y consistencia en el proceso de muestreo al agregar ruido. |
| `cfg`     | `FLOAT`      | El tipo de entrada 'cfg' establece la configuración para el proceso de muestreo, permitiendo un ajuste preciso de los parámetros y el comportamiento del muestreo. |
| `positivo` | `CONDITIONING` | El tipo de entrada 'positive' representa información de condicionamiento positivo, guiando el proceso de muestreo hacia la generación de muestras que se alineen con los atributos positivos especificados. |
| `negativo` | `CONDITIONING` | El tipo de entrada 'negative' representa información de condicionamiento negativo, desviando el proceso de muestreo de la generación de muestras que exhiban los atributos negativos especificados. |
| `muestreador` | `SAMPLER`    | El tipo de entrada 'sampler' selecciona la estrategia de muestreo específica que se empleará, impactando directamente en la naturaleza y calidad de las muestras generadas. |
| `sigmas`  | `SIGMAS`     | El tipo de entrada 'sigmas' define los niveles de ruido que se utilizarán en el proceso de muestreo, afectando la exploración del espacio de muestras y la diversidad de la salida. |
| `imagen_latente` | `LATENT` | El tipo de entrada 'latent_image' proporciona una imagen latente inicial para el proceso de muestreo, sirviendo como punto de partida para la generación de muestras. |

## Salidas

| Parámetro | Tipo de Dato | Descripción |
|-----------|--------------|-------------|
| `salida_sin_ruido`  | `LATENT`     | La 'output' representa el resultado principal del proceso de muestreo, conteniendo las muestras generadas. |
| `denoised_output` | `LATENT` | La 'denoised_output' representa las muestras después de que se ha aplicado un proceso de eliminación de ruido, mejorando potencialmente la claridad y calidad de las muestras generadas. |