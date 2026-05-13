> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeHunyuanVideo_ImageToVideo/es.md)

El nodo `TextEncodeHunyuanVideo_ImageToVideo` crea datos de condicionamiento para la generación de video combinando indicaciones de texto con incrustaciones de imagen. Utiliza un modelo CLIP para procesar tanto la entrada de texto como la información visual proveniente de una salida de visión CLIP, y luego genera tokens que fusionan estas dos fuentes según la configuración de intercalado de imagen especificada.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `clip` | CLIP | Sí | - | El modelo CLIP utilizado para la tokenización y codificación |
| `clip_vision_output` | CLIP_VISION_OUTPUT | Sí | - | Las incrustaciones visuales de un modelo de visión CLIP que proporcionan contexto de imagen |
| `prompt` | STRING | Sí | - | La descripción textual para guiar la generación de video, admite entrada multilínea e indicaciones dinámicas |
| `image_interleave` | INT | Sí | 1-512 | Cuánto influye la imagen en comparación con la indicación de texto. Un número más alto significa mayor influencia de la indicación de texto. (valor predeterminado: 2) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `CONDITIONING` | CONDITIONING | Los datos de condicionamiento que combinan información de texto e imagen para la generación de video |

---
**Source fingerprint (SHA-256):** `ee748bd1fb1733593eb4cb1187c5cc279171163cfbc389f039378d0e366fc231`
