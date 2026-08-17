# TextEncodeHunyuanVideo_ImagenAVideo

El nodo `TextEncodeHunyuanVideo_ImageToVideo` crea datos de condicionamiento para la generación de video combinando indicaciones de texto con incrustaciones de imagen. Utiliza un modelo CLIP para procesar tanto la entrada de texto como la información visual de una salida de visión CLIP, y luego genera tokens que fusionan estas dos fuentes según el ajuste de intercalación de imagen especificado.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `clip` | El modelo CLIP utilizado para la tokenización y codificación. | CLIP | Sí | - |
| `clip_vision_output` | Las incrustaciones visuales de un modelo de visión CLIP que proporcionan contexto de imagen. | CLIP_VISION_OUTPUT | Sí | - |
| `prompt` | La descripción de texto para guiar la generación de video. Admite entrada multilínea e indicaciones dinámicas. La indicación se formatea utilizando una plantilla que pide al modelo que describa el video basándose en la imagen de referencia, cubriendo aspectos como el contenido principal, los detalles de los objetos, las acciones, el fondo y los ángulos de cámara. | STRING | Sí | - |
| `image_interleave` | Cuánto influye la imagen en comparación con la indicación de texto. Un número mayor significa más influencia de la indicación de texto. (default: 2, parámetro avanzado) | INT | Sí | 1-512 |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `CONDITIONING` | Los datos de condicionamiento que combinan información de texto e imagen para la generación de video. | CONDITIONING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeHunyuanVideo_ImageToVideo/es.md)

---
**Source fingerprint (SHA-256):** `016b87ead6f7a6ca61eff220e57f59252018cc78e80ec8cff5b83223b8f90f73`
