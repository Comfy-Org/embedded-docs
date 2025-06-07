El nodo KSampler está diseñado para operaciones avanzadas de muestreo dentro de modelos generativos, permitiendo la personalización de los procesos de muestreo a través de varios parámetros. Facilita la generación de nuevas muestras de datos manipulando representaciones de espacio latente, aprovechando el condicionamiento y ajustando los niveles de ruido.

## Entradas

| Parámetro       | Data Type | Descripción                                                                                                               |
|-----------------|-------------|---------------------------------------------------------------------------------------------------------------------------|
| `model`         | `MODEL`     | Especifica el modelo generativo a utilizar para el muestreo, desempeñando un papel crucial en la determinación de las características de las muestras generadas. |
| `seed`          | `INT`       | Controla la aleatoriedad del proceso de muestreo, asegurando la reproducibilidad de los resultados cuando se establece en un valor específico.                         |
| `steps`         | `INT`       | Determina el número de pasos a realizar en el proceso de muestreo, afectando el detalle y calidad de las muestras generadas.           |
| `cfg`           | `FLOAT`     | Ajusta el factor de condicionamiento, influyendo en la dirección y fuerza del condicionamiento aplicado durante el muestreo.                     |
| `sampler_name`  | COMBO[STRING] | Selecciona el algoritmo de muestreo específico a utilizar, impactando el comportamiento y resultado del proceso de muestreo.                     |
| `scheduler`     | COMBO[STRING] | Elige el algoritmo de programación para controlar el proceso de muestreo, afectando la progresión y dinámica del muestreo.           |
| `positive`      | `CONDITIONING` | Define el condicionamiento positivo para guiar el muestreo hacia atributos o características deseadas.                                         |
| `negative`      | `CONDITIONING` | Especifica el condicionamiento negativo para desviar el muestreo de ciertos atributos o características.                                     |
| `latent_image`  | `LATENT`    | Proporciona una representación de espacio latente para ser utilizada como punto de partida o referencia para el proceso de muestreo.                            |
| `denoise`       | `FLOAT`     | Controla el nivel de eliminación de ruido aplicado a las muestras, afectando la claridad y nitidez de las imágenes generadas.                   |

## Salidas

| Parámetro   | Data Type | Descripción |
|-------------|-------------|-------------|
| `latent`    | `LATENT`    | Representa la salida del espacio latente del proceso de muestreo, encapsulando las muestras generadas. |
