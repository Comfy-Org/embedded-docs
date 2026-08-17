# TextEncodeZImageOmni

El nodo TextEncodeZImageOmni es un nodo de acondicionamiento avanzado que codifica un prompt de texto junto con imágenes de referencia opcionales en un formato de condicionamiento adecuado para modelos de generación de imágenes. Puede procesar hasta tres imágenes, codificándolas opcionalmente con un codificador de visión y/o un VAE para producir latentes de referencia, e integra estas referencias visuales con el prompt de texto utilizando una estructura de plantilla específica.

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `clip` | El modelo CLIP utilizado para tokenizar y codificar el prompt de texto. | CLIP | Sí |  |
| `image_encoder` | Un modelo codificador de visión opcional. Si se proporciona, se utilizará para codificar las imágenes de entrada y los embeddings resultantes se añadirán al condicionamiento. | CLIPVision | No |  |
| `prompt` | El prompt de texto que se va a codificar. Este campo admite entrada multilínea y prompts dinámicos. | STRING | Sí |  |
| `auto_resize_images` | Cuando está habilitado (por defecto: True), las imágenes de entrada se redimensionan automáticamente según su área de píxeles antes de pasarse al VAE para su codificación. Esta es una configuración avanzada. | BOOLEAN | No |  |
| `vae` | Un modelo VAE opcional. Si se proporciona, se utilizará para codificar las imágenes de entrada en representaciones latentes, que se añaden al condicionamiento como latentes de referencia. | VAE | No |  |
| `image1` | La primera imagen de referencia opcional. | IMAGE | No |  |
| `image2` | La segunda imagen de referencia opcional. | IMAGE | No |  |
| `image3` | La tercera imagen de referencia opcional. | IMAGE | No |  |

**Nota:** El nodo puede aceptar un máximo de tres imágenes (`image1`, `image2`, `image3`). Las entradas `image_encoder` y `vae` solo se utilizan si se proporciona al menos una imagen. Cuando `auto_resize_images` es True y hay un `vae` conectado, las imágenes se redimensionan para tener un área de píxeles total cercana a 1024x1024 píxeles, con dimensiones redondeadas a múltiplos de 8, antes de la codificación. Si no se proporcionan imágenes, el nodo codifica el prompt de texto sin referencias visuales.

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `CONDITIONING` | La salida de condicionamiento final, que contiene el prompt de texto codificado y puede incluir embeddings de imágenes codificadas y/o latentes de referencia si se proporcionaron imágenes. | CONDITIONING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeZImageOmni/es.md)

---
**Source fingerprint (SHA-256):** `b40a3150f536b6f37e2b53e6d9992fcb4fd32dceb540c0a76773a7ba1af9a7b8`
