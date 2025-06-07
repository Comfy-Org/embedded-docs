
El nodo SamplerCustom está diseñado para proporcionar un mecanismo de muestreo flexible y personalizable para diversas aplicaciones. Permite a los usuarios seleccionar y configurar diferentes estrategias de muestreo adaptadas a sus necesidades específicas, mejorando la adaptabilidad y eficiencia del proceso de muestreo.

## Entradas

| Parámetro | Data Type | Descripción |
|-----------|--------------|-------------|
| `model`   | `MODEL`      | El tipo de entrada 'model' especifica el modelo que se utilizará para el muestreo, desempeñando un papel crucial en la determinación del comportamiento y resultado del muestreo. |
| `add_noise` | `BOOLEAN`    | El tipo de entrada 'add_noise' permite a los usuarios especificar si se debe añadir ruido al proceso de muestreo, influyendo en la diversidad y características de las muestras generadas. |
| `noise_seed` | `INT`        | El tipo de entrada 'noise_seed' proporciona una semilla para la generación de ruido, asegurando la reproducibilidad y consistencia en el proceso de muestreo al añadir ruido. |
| `cfg`     | `FLOAT`      | El tipo de entrada 'cfg' establece la configuración para el proceso de muestreo, permitiendo un ajuste fino de los parámetros y comportamiento del muestreo. |
| `positive` | `CONDITIONING` | El tipo de entrada 'positive' representa información de condicionamiento positivo, guiando el proceso de muestreo hacia la generación de muestras que se alineen con atributos positivos especificados. |
| `negative` | `CONDITIONING` | El tipo de entrada 'negative' representa información de condicionamiento negativo, orientando el proceso de muestreo para evitar la generación de muestras que exhiban atributos negativos especificados. |
| `sampler` | `SAMPLER`    | El tipo de entrada 'sampler' selecciona la estrategia de muestreo específica a emplear, impactando directamente en la naturaleza y calidad de las muestras generadas. |
| `sigmas`  | `SIGMAS`     | El tipo de entrada 'sigmas' define los niveles de ruido a utilizar en el proceso de muestreo, afectando la exploración del espacio de muestras y la diversidad del resultado. |
| `latent_image` | `LATENT` | El tipo de entrada 'latent_image' proporciona una imagen latente inicial para el proceso de muestreo, sirviendo como punto de partida para la generación de muestras. |

## Salidas

| Parámetro | Data Type | Descripción |
|-----------|--------------|-------------|
| `output`  | `LATENT`     | El 'output' representa el resultado principal del proceso de muestreo, conteniendo las muestras generadas. |
| `denoised_output` | `LATENT` | El 'denoised_output' representa las muestras después de que se ha aplicado un proceso de eliminación de ruido, potencialmente mejorando la claridad y calidad de las muestras generadas. |
