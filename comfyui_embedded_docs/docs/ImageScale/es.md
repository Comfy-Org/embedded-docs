> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageScale/es.md)

El nodo ImageScale está diseñado para redimensionar imágenes a dimensiones específicas, ofreciendo una selección de métodos de ampliación y la capacidad de recortar la imagen redimensionada. Abstrae la complejidad del escalado y recorte de imágenes, proporcionando una interfaz sencilla para modificar las dimensiones de la imagen según parámetros definidos por el usuario.

## Entradas

| Parámetro       | Tipo de Dato | Descripción                                                                           |
|-----------------|--------------|---------------------------------------------------------------------------------------|
| `image`         | `IMAGE`      | La imagen de entrada que se va a ampliar. Este parámetro es central para el funcionamiento del nodo, ya que sirve como dato principal sobre el cual se aplican las transformaciones de redimensionamiento. La calidad y las dimensiones de la imagen de salida están directamente influenciadas por las propiedades de la imagen original. |
| `upscale_method`| COMBO[STRING]| Especifica el método utilizado para ampliar la imagen. La elección del método puede afectar la calidad y las características de la imagen ampliada, influyendo en la fidelidad visual y los posibles artefactos en la salida redimensionada. |
| `width`         | `INT`        | El ancho objetivo para la imagen ampliada. Este parámetro influye directamente en las dimensiones de la imagen de salida, determinando la escala horizontal de la operación de redimensionamiento. |
| `height`        | `INT`        | La altura objetivo para la imagen ampliada. Este parámetro influye directamente en las dimensiones de la imagen de salida, determinando la escala vertical de la operación de redimensionamiento. |
| `crop`          | COMBO[STRING]| Determina si la imagen ampliada debe recortarse y de qué manera, ofreciendo opciones para deshabilitar el recorte o realizar un recorte centrado. Esto afecta la composición final de la imagen al eliminar potencialmente los bordes para ajustarse a las dimensiones especificadas. |

## Salidas

| Parámetro | Tipo de Dato | Descripción |
|-----------|--------------|-------------|
| `image`   | `IMAGE`      | La imagen ampliada (y opcionalmente recortada), lista para su posterior procesamiento o visualización. |