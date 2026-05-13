> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageQuantize/es.md)

El nodo ImageQuantize está diseñado para reducir la cantidad de colores en una imagen a un número específico, aplicando opcionalmente técnicas de tramado para mantener la calidad visual. Este proceso es útil para crear imágenes basadas en paletas o reducir la complejidad cromática para ciertas aplicaciones.

## Entradas

| Campo   | Tipo de Dato | Descripción                                                                       |
|---------|-------------|-----------------------------------------------------------------------------------|
| `imagen` | `IMAGE`     | El tensor de imagen de entrada que se va a cuantizar. Afecta la ejecución del nodo al ser los datos principales sobre los cuales se realiza la reducción de color. |
| `colores`| `INT`       | Especifica la cantidad de colores a los que se reducirá la imagen. Influye directamente en el proceso de cuantización al determinar el tamaño de la paleta de colores. |
| `difuminado`| COMBO[STRING] | Determina la técnica de tramado que se aplicará durante la cuantización, afectando la calidad visual y la apariencia de la imagen de salida. |

## Salidas

| Campo | Tipo de Dato | Descripción                                                                   |
|-------|-------------|-------------------------------------------------------------------------------|
| `imagen`| `IMAGE`     | La versión cuantizada de la imagen de entrada, con complejidad cromática reducida y opcionalmente tramada para mantener la calidad visual. |