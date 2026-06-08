El nodo **PhotoMakerEncode** procesa imágenes y texto para generar datos de condicionamiento para la generación de imágenes con IA. Toma una imagen de referencia y un mensaje de texto, luego crea *embeddings* que pueden usarse para guiar la generación de imágenes basándose en las características visuales de la imagen de referencia. El nodo busca específicamente el token "photomaker" en el texto para determinar dónde aplicar el condicionamiento basado en la imagen.

## Entradas

| Parámetro | Descripción | Tipo de dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `photomaker` | El modelo PhotoMaker utilizado para procesar la imagen y generar *embeddings* | PHOTOMAKER | Sí | - |
| `imagen` | La imagen de referencia que proporciona las características visuales para el condicionamiento | IMAGE | Sí | - |
| `clip` | El modelo CLIP utilizado para la tokenización y codificación de texto | CLIP | Sí | - |
| `texto` | El mensaje de texto para la generación de condicionamiento (predeterminado: "photograph of photomaker") | STRING | Sí | - |

**Nota:** Cuando el texto contiene la palabra "photomaker", el nodo aplica el condicionamiento basado en la imagen en esa posición del mensaje. Si no se encuentra "photomaker" en el texto, el nodo genera un condicionamiento de texto estándar sin influencia de la imagen.

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `CONDITIONING` | Los datos de condicionamiento que contienen *embeddings* de imagen y texto para guiar la generación de imágenes | CONDITIONING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PhotoMakerEncode/es.md)

---
**Source fingerprint (SHA-256):** `535fd3dbbe0e48205bebde030138ffca841dc94a18fd47db768a1066fe84bce4`
