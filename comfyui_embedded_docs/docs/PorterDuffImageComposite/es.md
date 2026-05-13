> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PorterDuffImageComposite/es.md)

El nodo PorterDuffImageComposite está diseñado para realizar composición de imágenes utilizando los operadores de composición Porter-Duff. Permite la combinación de imágenes de origen y destino según varios modos de fusión, facilitando la creación de efectos visuales complejos al manipular la transparencia de las imágenes y superponerlas de formas creativas.

## Entradas

| Parámetro | Tipo de dato | Descripción |
| --------- | ------------ | ----------- |
| `source`  | `IMAGE`     | El tensor de la imagen de origen que se compondrá sobre la imagen de destino. Desempeña un papel crucial en la determinación del resultado visual final según el modo de composición seleccionado. |
| `source_alpha` | `MASK` | El canal alfa de la imagen de origen, que especifica la transparencia de cada píxel en la imagen de origen. Afecta cómo se fusiona la imagen de origen con la imagen de destino. |
| `destination` | `IMAGE` | El tensor de la imagen de destino que sirve como fondo sobre el cual se compone la imagen de origen. Contribuye a la imagen compuesta final según el modo de fusión. |
| `destination_alpha` | `MASK` | El canal alfa de la imagen de destino, que define la transparencia de los píxeles de la imagen de destino. Influye en la fusión de las imágenes de origen y destino. |
| `mode` | COMBO[STRING] | El modo de composición Porter-Duff a aplicar, que determina cómo se fusionan las imágenes de origen y destino. Cada modo crea diferentes efectos visuales. |

## Salidas

| Parámetro | Tipo de dato | Descripción |
| --------- | ------------ | ----------- |
| `image`   | `IMAGE`     | La imagen compuesta resultante de la aplicación del modo Porter-Duff especificado. |
| `mask`    | `MASK`      | El canal alfa de la imagen compuesta, que indica la transparencia de cada píxel. |