> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PhotoMakerEncode/es.md)

El nodo **PhotoMakerEncode** procesa imágenes y texto para generar datos de condicionamiento para la generación de imágenes con IA. Toma una imagen de referencia y un mensaje de texto, luego crea *embeddings* que pueden usarse para guiar la generación de imágenes basándose en las características visuales de la imagen de referencia. El nodo busca específicamente el token "photomaker" en el texto para determinar dónde aplicar el condicionamiento basado en la imagen.

## Entradas

| Parámetro | Tipo de dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `photomaker` | PHOTOMAKER | Sí | - | El modelo PhotoMaker utilizado para procesar la imagen y generar *embeddings* |
| `imagen` | IMAGE | Sí | - | La imagen de referencia que proporciona las características visuales para el condicionamiento |
| `clip` | CLIP | Sí | - | El modelo CLIP utilizado para la tokenización y codificación de texto |
| `texto` | STRING | Sí | - | El mensaje de texto para la generación de condicionamiento (predeterminado: "photograph of photomaker") |

**Nota:** Cuando el texto contiene la palabra "photomaker", el nodo aplica el condicionamiento basado en la imagen en esa posición del mensaje. Si no se encuentra "photomaker" en el texto, el nodo genera un condicionamiento de texto estándar sin influencia de la imagen.

## Salidas

| Nombre de salida | Tipo de dato | Descripción |
|------------------|--------------|-------------|
| `CONDITIONING` | CONDITIONING | Los datos de condicionamiento que contienen *embeddings* de imagen y texto para guiar la generación de imágenes |

---
**Source fingerprint (SHA-256):** `535fd3dbbe0e48205bebde030138ffca841dc94a18fd47db768a1066fe84bce4`
