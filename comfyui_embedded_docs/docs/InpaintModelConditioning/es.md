El nodo InpaintModelConditioning está diseñado para facilitar el proceso de condicionamiento para modelos de inpainting, permitiendo la integración y manipulación de diversas entradas de condicionamiento para personalizar la salida de inpainting. Abarca una amplia gama de funcionalidades, desde cargar puntos de control de modelos específicos y aplicar modelos de estilo o control, hasta codificar y combinar elementos de condicionamiento, sirviendo así como una herramienta integral para personalizar tareas de inpainting.

## Entradas

| Parámetro | Tipo Comfy        | Descripción |
|-----------|--------------------|-------------|
| `positive`| `CONDITIONING`     | Representa la información o parámetros de condicionamiento positivo que se aplicarán al modelo de inpainting. Esta entrada es crucial para definir el contexto o las restricciones bajo las cuales se debe realizar la operación de inpainting, afectando significativamente la salida final. |
| `negative`| `CONDITIONING`     | Representa la información o parámetros de condicionamiento negativo que se aplicarán al modelo de inpainting. Esta entrada es esencial para especificar las condiciones o contextos a evitar durante el proceso de inpainting, influyendo así en la salida final. |
| `vae`     | `VAE`              | Especifica el modelo VAE que se utilizará en el proceso de condicionamiento. Esta entrada es crucial para determinar la arquitectura y los parámetros específicos del modelo VAE que se utilizarán. |
| `pixels`  | `IMAGE`            | Representa los datos de píxeles de la imagen que se va a inpaintar. Esta entrada es esencial para proporcionar el contexto visual necesario para la tarea de inpainting. |
| `mask`    | `MASK`             | Especifica la máscara que se aplicará a la imagen, indicando las áreas que se deben inpaintar. Esta entrada es crucial para definir las regiones específicas dentro de la imagen que requieren inpainting. |

## Salidas

| Parámetro | Tipo de Dato | Descripción |
|-----------|--------------|-------------|
| `positive`| `CONDITIONING` | La información de condicionamiento positivo modificada después del procesamiento, lista para ser aplicada al modelo de inpainting. Esta salida es esencial para guiar el proceso de inpainting de acuerdo con las condiciones positivas especificadas. |
| `negative`| `CONDITIONING` | La información de condicionamiento negativo modificada después del procesamiento, lista para ser aplicada al modelo de inpainting. Esta salida es esencial para guiar el proceso de inpainting de acuerdo con las condiciones negativas especificadas. |
| `latent`  | `LATENT`     | La representación latente derivada del proceso de condicionamiento. Esta salida es crucial para entender las características y rasgos subyacentes de la imagen que se está inpaintando.
