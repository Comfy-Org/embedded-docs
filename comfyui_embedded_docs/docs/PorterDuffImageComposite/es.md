
El nodo PorterDuffImageComposite está diseñado para realizar la composición de imágenes utilizando los operadores de composición Porter-Duff. Permite la combinación de imágenes de origen y destino según varios modos de mezcla, habilitando la creación de efectos visuales complejos al manipular la transparencia de las imágenes y superponer imágenes de manera creativa.

## Entradas

| Parámetro | Data Type | Descripción |
| --------- | ------------ | ----------- |
| `source`  | `IMAGE`     | El tensor de imagen de origen que se compondrá sobre la imagen de destino. Juega un papel crucial en la determinación del resultado visual final basado en el modo de composición seleccionado. |
| `source_alpha` | `MASK` | El canal alfa de la imagen de origen, que especifica la transparencia de cada píxel en la imagen de origen. Afecta cómo la imagen de origen se mezcla con la imagen de destino. |
| `destination` | `IMAGE` | El tensor de imagen de destino que sirve como telón de fondo sobre el cual se compone la imagen de origen. Contribuye a la imagen compuesta final basada en el modo de mezcla. |
| `destination_alpha` | `MASK` | El canal alfa de la imagen de destino, definiendo la transparencia de los píxeles de la imagen de destino. Influye en la mezcla de las imágenes de origen y destino. |
| `mode` | COMBO[STRING] | El modo de composición Porter-Duff a aplicar, que determina cómo se mezclan las imágenes de origen y destino. Cada modo crea diferentes efectos visuales. |

## Salidas

| Parámetro | Data Type | Descripción |
| --------- | ------------ | ----------- |
| `image`   | `IMAGE`     | La imagen compuesta resultante de la aplicación del modo Porter-Duff especificado. |
| `mask`    | `MASK`      | El canal alfa de la imagen compuesta, indicando la transparencia de cada píxel. |
