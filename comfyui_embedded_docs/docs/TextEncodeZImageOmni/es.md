> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeZImageOmni/es.md)

El nodo `TextEncodeZImageOmni` es un nodo de condicionamiento avanzado que codifica un mensaje de texto junto con imágenes de referencia opcionales en un formato de condicionamiento adecuado para modelos de generación de imágenes. Puede procesar hasta tres imágenes, codificándolas opcionalmente con un codificador de visión y/o un VAE para producir latentes de referencia, e integra estas referencias visuales con el mensaje de texto utilizando una estructura de plantilla específica.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|---------------|-------------|-------|-------------|
| `clip` | CLIP | Sí | | El modelo CLIP utilizado para tokenizar y codificar el mensaje de texto. |
| `codificador_de_imagen` | CLIPVision | No | | Un modelo de codificador de visión opcional. Si se proporciona, se utilizará para codificar las imágenes de entrada, y las incrustaciones resultantes se agregarán al condicionamiento. |
| `instrucción` | STRING | Sí | | El mensaje de texto a codificar. Este campo admite entrada multilínea y mensajes dinámicos. |
| `auto_redimensionar_imágenes` | BOOLEAN | No | | Cuando está habilitado (por defecto: Verdadero), las imágenes de entrada se redimensionarán automáticamente según su área de píxeles antes de pasarse al VAE para su codificación. |
| `vae` | VAE | No | | Un modelo VAE opcional. Si se proporciona, se utilizará para codificar las imágenes de entrada en representaciones latentes, que se agregan al condicionamiento como latentes de referencia. |
| `imagen1` | IMAGE | No | | La primera imagen de referencia opcional. |
| `imagen2` | IMAGE | No | | La segunda imagen de referencia opcional. |
| `imagen3` | IMAGE | No | | La tercera imagen de referencia opcional. |

**Nota:** El nodo puede aceptar un máximo de tres imágenes (`image1`, `image2`, `image3`). Las entradas `image_encoder` y `vae` solo se utilizan si se proporciona al menos una imagen. Cuando `auto_resize_images` es Verdadero y hay un `vae` conectado, las imágenes se redimensionan para tener un área total de píxeles cercana a 1024x1024 antes de la codificación.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|---------------|-------------|
| `CONDITIONING` | CONDITIONING | La salida de condicionamiento final, que contiene el mensaje de texto codificado y puede incluir incrustaciones de imágenes codificadas y/o latentes de referencia si se proporcionaron imágenes. |

---
**Source fingerprint (SHA-256):** `daa4205acdf72503180eeedb4142708d239d4ff0f689012a298264ae2d8ea949`
