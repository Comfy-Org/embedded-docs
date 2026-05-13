> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RunwayTextToImageNode/es.md)

El nodo **Runway Text to Image** genera imágenes a partir de indicaciones de texto utilizando el modelo Gen 4 de Runway. Puedes proporcionar una descripción textual y, opcionalmente, incluir una imagen de referencia para guiar el proceso de generación. El nodo gestiona la comunicación con la API y devuelve la imagen generada.

## Entradas

| Parámetro | Tipo de dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `texto_descriptivo` | STRING | Sí | - | Indicación de texto para la generación (predeterminado: "") |
| `proporción` | COMBO | Sí | "16:9"<br>"1:1"<br>"21:9"<br>"2:3"<br>"3:2"<br>"4:5"<br>"5:4"<br>"9:16"<br>"9:21" | Relación de aspecto para la imagen generada |
| `imagen_referencia` | IMAGE | No | - | Imagen de referencia opcional para guiar la generación |

**Nota:** La imagen de referencia debe tener dimensiones que no superen los 7999x7999 píxeles y una relación de aspecto entre 0.5 y 2.0. Cuando se proporciona una imagen de referencia, esta guía el proceso de generación de la imagen.

## Salidas

| Nombre de salida | Tipo de dato | Descripción |
|------------------|--------------|-------------|
| `output` | IMAGE | La imagen generada basada en la indicación de texto y la imagen de referencia opcional |

---
**Source fingerprint (SHA-256):** `140f8e6b07216892d84f2d7fbc3afaf1c390e98ddedf27d4926032066a783f67`
