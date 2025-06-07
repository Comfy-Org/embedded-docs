El nodo CLIPTextEncode está diseñado para codificar entradas textuales utilizando un modelo CLIP, transformando el texto en una forma que puede ser utilizada para el condicionamiento en tareas generativas. Abstrae la complejidad de la tokenización y codificación de texto, proporcionando una interfaz simplificada para generar vectores de condicionamiento basados en texto.

Además de los prompts de texto normales, también puedes usar modelos de incrustación. Por ejemplo, si agregas un modelo de incrustación en el directorio `ComfyUI/models/embeddings`, puedes usar este modelo en el prompt.

Por ejemplo, si el nombre del modelo correspondiente es `EasyNegative`, puedes usar `embedding:EasyNegative,` en el prompt para usar este modelo correspondiente.

## Entradas

| Parámetro | Tipo de Dato | Descripción |
|-----------|-------------|-------------|
| `text`    | `STRING`    | El parámetro 'text' es la entrada textual que será codificada. Juega un papel crucial en la determinación del vector de condicionamiento de salida, ya que es la fuente principal de información para el proceso de codificación. |
| `clip`    | CLIP      | El parámetro 'clip' representa el modelo CLIP utilizado para la tokenización y codificación de texto. Es esencial para convertir la entrada textual en un vector de condicionamiento, influyendo en la calidad y relevancia de la salida generada. |

## Salidas

| Parámetro | Tipo de Dato | Descripción |
|-----------|--------------|-------------|
| `CONDITIONING` | CONDITIONING | La salida 'conditioning' es una representación vectorial del texto de entrada, codificada por el modelo CLIP. Sirve como un componente crucial para guiar los modelos generativos en la producción de salidas relevantes y coherentes. |
