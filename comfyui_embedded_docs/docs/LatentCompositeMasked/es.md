> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentCompositeMasked/es.md)

El nodo LatentCompositeMasked está diseñado para combinar dos representaciones latentes en coordenadas específicas, utilizando opcionalmente una máscara para una composición más controlada. Este nodo permite crear imágenes latentes complejas superponiendo partes de una imagen sobre otra, con la capacidad de redimensionar la imagen de origen para un ajuste perfecto.

## Entradas

| Parámetro | Tipo de Dato | Descripción |
|-----------|-------------|-------------|
| `destino` | `LATENT`    | La representación latente sobre la cual se compondrá otra representación latente. Actúa como la capa base para la operación de composición. |
| `fuente` | `LATENT`    | La representación latente que se va a componer sobre el destino. Esta capa de origen puede redimensionarse y posicionarse según los parámetros especificados. |
| `x` | `INT`       | La coordenada x en la representación latente de destino donde se colocará el origen. Permite un posicionamiento preciso de la capa de origen. |
| `y` | `INT`       | La coordenada y en la representación latente de destino donde se colocará el origen, lo que permite una superposición precisa. |
| `redimensionar_fuente` | `BOOLEAN` | Un indicador booleano que determina si la representación latente de origen debe redimensionarse para coincidir con las dimensiones del destino antes de la composición. |
| `máscara` | `MASK`     | Una máscara opcional que puede utilizarse para controlar la mezcla del origen sobre el destino. La máscara define qué partes del origen serán visibles en la composición final. |

## Salidas

| Parámetro | Tipo de Dato | Descripción |
|-----------|-------------|-------------|
| `latent`  | `LATENT`    | La representación latente resultante después de componer el origen sobre el destino, utilizando potencialmente una máscara para una mezcla selectiva. |