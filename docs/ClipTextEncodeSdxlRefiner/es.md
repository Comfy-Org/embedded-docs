Este nodo se especializa en refinar la codificación de las entradas de texto utilizando modelos CLIP, mejorando el condicionamiento para tareas generativas al incorporar puntuaciones estéticas y dimensiones.

## Tipos de entrada del Refinador de Codificación de Texto CLIP SDXL

| Parámetro | Tipo Comfy | Descripción |
| --- | --- | --- |
| `clip` | `CLIP` | Una instancia del modelo CLIP utilizada para la tokenización y codificación de texto, central para generar el condicionamiento. |
| `ascore` | `FLOAT` | El parámetro de puntuación estética influye en la salida del condicionamiento al proporcionar una medida de calidad estética. |
| `width` | `INT` | Especifica el ancho del condicionamiento de salida, afectando las dimensiones del contenido generado. |
| `height` | `INT` | Determina la altura del condicionamiento de salida, influyendo en las dimensiones del contenido generado. |
| `text` | `STRING` | La entrada de texto a codificar, que sirve como el descriptor principal del contenido para el condicionamiento. |

## Tipos de salida del Refinador de Codificación de Texto CLIP SDXL

| Parámetro | Tipo Comfy | Descripción |
| --- | --- | --- |
| `conditioning` | `CONDITIONING` | La salida de condicionamiento refinada, enriquecida con puntuaciones estéticas y dimensiones para una generación de contenido mejorada. 
