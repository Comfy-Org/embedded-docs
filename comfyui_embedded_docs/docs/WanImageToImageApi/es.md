> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanImageToImageApi/es.md)

El nodo Wan Image to Image genera una imagen a partir de una o dos imágenes de entrada y un mensaje de texto. Transforma tus imágenes de entrada basándose en la descripción que proporciones, creando una nueva imagen que mantiene la relación de aspecto de tu entrada original. La imagen de salida tiene un tamaño fijo de 1.6 megapíxeles independientemente del tamaño de entrada.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | Sí | "wan2.5-i2i-preview" | Modelo a utilizar (por defecto: "wan2.5-i2i-preview"). |
| `image` | IMAGE | Sí | - | Edición de imagen única o fusión de múltiples imágenes, máximo 2 imágenes. |
| `prompt` | STRING | Sí | - | Mensaje utilizado para describir los elementos y características visuales, admite inglés/chino (por defecto: vacío). |
| `negative_prompt` | STRING | No | - | Mensaje de texto negativo para guiar lo que se debe evitar (por defecto: vacío). |
| `seed` | INT | No | 0 a 2147483647 | Semilla a utilizar para la generación (por defecto: 0). |
| `watermark` | BOOLEAN | No | - | Si agregar o no una marca de agua de "AI generated" al resultado (por defecto: true). |

**Nota:** Este nodo acepta exactamente 1 o 2 imágenes de entrada. Si proporcionas más de 2 imágenes o ninguna imagen, el nodo devolverá un error.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `image` | IMAGE | La imagen generada basada en las imágenes de entrada y los mensajes de texto. |
