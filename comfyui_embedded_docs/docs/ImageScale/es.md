El nodo ImageScale está diseñado para redimensionar imágenes a dimensiones específicas, ofreciendo una selección de métodos de escalado y la capacidad de recortar la imagen redimensionada. Abstrae la complejidad del escalado y recorte de imágenes, proporcionando una interfaz sencilla para modificar las dimensiones de la imagen según los parámetros definidos por el usuario.

## Entradas

| Parámetro       | Data Type | Descripción                                                                           |
|-----------------|-------------|---------------------------------------------------------------------------------------|
| `image`         | `IMAGE`     | La imagen de entrada que se va a escalar. Este parámetro es central para la operación del nodo, sirviendo como el dato principal sobre el cual se aplican las transformaciones de redimensionamiento. La calidad y las dimensiones de la imagen de salida están directamente influenciadas por las propiedades de la imagen original. |
| `upscale_method`| COMBO[STRING] | Especifica el método utilizado para escalar la imagen. La elección del método puede afectar la calidad y las características de la imagen escalada, influyendo en la fidelidad visual y los posibles artefactos en la salida redimensionada. |
| `width`         | `INT`       | El ancho objetivo para la imagen escalada. Este parámetro influye directamente en las dimensiones de la imagen de salida, determinando la escala horizontal de la operación de redimensionamiento. |
| `height`        | `INT`       | La altura objetivo para la imagen escalada. Este parámetro influye directamente en las dimensiones de la imagen de salida, determinando la escala vertical de la operación de redimensionamiento. |
| `crop`          | COMBO[STRING] | Determina si y cómo se debe recortar la imagen escalada, ofreciendo opciones para deshabilitar el recorte o realizar un recorte centrado. Esto afecta la composición final de la imagen al potencialmente eliminar bordes para ajustarse a las dimensiones especificadas. |

## Salidas

| Parámetro | Data Type | Descripción |
|-----------|-------------|-------------|
| `image`   | `IMAGE`     | La imagen escalada (y opcionalmente recortada), lista para un procesamiento o visualización adicional. |
