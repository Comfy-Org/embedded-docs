# TextEncodeHunyuanVideo_ImagenAVideo

El nodo `TextEncodeHunyuanVideo_ImageToVideo` crea datos de condicionamiento para la generación de video combinando indicaciones de texto con incrustaciones de imagen. Utiliza un modelo CLIP para procesar tanto la entrada de texto como la información visual proveniente de una salida de visión CLIP, y luego genera tokens que fusionan estas dos fuentes según la configuración de intercalado de imagen especificada.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `clip` | El modelo CLIP utilizado para la tokenización y codificación | CLIP | Sí | - |
| `salida_de_clip_vision` | Las incrustaciones visuales de un modelo de visión CLIP que proporcionan contexto de imagen | CLIP_VISION_OUTPUT | Sí | - |
| `indicación` | La descripción textual para guiar la generación de video, admite entrada multilínea e indicaciones dinámicas | STRING | Sí | - |
| `entrelazado_de_imagen` | Cuánto influye la imagen en comparación con la indicación de texto. Un número más alto significa mayor influencia de la indicación de texto. (valor predeterminado: 2) | INT | Sí | 1-512 |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `CONDITIONING` | Los datos de condicionamiento que combinan información de texto e imagen para la generación de video | CONDITIONING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeHunyuanVideo_ImageToVideo/es.md)

---
**Source fingerprint (SHA-256):** `ee748bd1fb1733593eb4cb1187c5cc279171163cfbc389f039378d0e366fc231`
