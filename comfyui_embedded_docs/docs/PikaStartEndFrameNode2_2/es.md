> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PikaStartEndFrameNode2_2/es.md)

El nodo PikaFrames v2.2 genera un video combinando tu primer y último fotograma. Cargas dos imágenes para definir los puntos de inicio y fin, y la IA crea una transición suave entre ellas para producir un video completo.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `image_start` | IMAGE | Sí | - | La primera imagen a combinar. |
| `image_end` | IMAGE | Sí | - | La última imagen a combinar. |
| `prompt_text` | STRING | Sí | - | Texto descriptivo que indica el contenido deseado del video. |
| `negative_prompt` | STRING | Sí | - | Texto que describe lo que se debe evitar en el video. |
| `seed` | INT | Sí | - | Valor de semilla aleatoria para la consistencia en la generación. |
| `resolution` | STRING | Sí | - | Resolución del video de salida. |
| `duration` | INT | Sí | - | Duración del video generado. |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `output` | VIDEO | El video generado que combina los fotogramas de inicio y fin con transiciones de IA. |

---
**Source fingerprint (SHA-256):** `0a26f6db754c61d1f35e3fd9faceb631a8103ce9ff38190a5dd637991914e238`
