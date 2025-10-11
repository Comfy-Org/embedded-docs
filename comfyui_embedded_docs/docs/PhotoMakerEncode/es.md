> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PhotoMakerEncode/es.md)

El nodo PhotoMakerEncode procesa imágenes y texto para generar datos de condicionamiento para la generación de imágenes IA. Toma una imagen de referencia y un texto prompt, luego crea incrustaciones que pueden usarse para guiar la generación de imágenes basándose en las características visuales de la imagen de referencia. El nodo busca específicamente el token "photomaker" en el texto para determinar dónde aplicar el condicionamiento basado en imagen.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `photomaker` | PHOTOMAKER | Sí | - | El modelo PhotoMaker utilizado para procesar la imagen y generar las incrustaciones |
| `image` | IMAGE | Sí | - | La imagen de referencia que proporciona las características visuales para el condicionamiento |
| `clip` | CLIP | Sí | - | El modelo CLIP utilizado para la tokenización y codificación del texto |
| `text` | STRING | Sí | - | El texto prompt para la generación del condicionamiento (por defecto: "photograph of photomaker") |

**Nota:** Cuando el texto contiene la palabra "photomaker", el nodo aplica condicionamiento basado en imagen en esa posición del prompt. Si no se encuentra "photomaker" en el texto, el nodo genera condicionamiento de texto estándar sin influencia de la imagen.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `CONDITIONING` | CONDITIONING | Los datos de condicionamiento que contienen incrustaciones de imagen y texto para guiar la generación de imágenes |