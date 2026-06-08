El nodo PikaFrames v2.2 genera un video combinando tu primer y último fotograma. Cargas dos imágenes para definir los puntos de inicio y fin, y la IA crea una transición suave entre ellas para producir un video completo.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `image_start` | La primera imagen a combinar. | IMAGE | Sí | - |
| `image_end` | La última imagen a combinar. | IMAGE | Sí | - |
| `prompt_text` | Texto descriptivo que indica el contenido deseado del video. | STRING | Sí | - |
| `negative_prompt` | Texto que describe lo que se debe evitar en el video. | STRING | Sí | - |
| `seed` | Valor de semilla aleatoria para la consistencia en la generación. | INT | Sí | - |
| `resolution` | Resolución del video de salida. | STRING | Sí | - |
| `duration` | Duración del video generado. | INT | Sí | - |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `output` | El video generado que combina los fotogramas de inicio y fin con transiciones de IA. | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PikaStartEndFrameNode2_2/es.md)

---
**Source fingerprint (SHA-256):** `0a26f6db754c61d1f35e3fd9faceb631a8103ce9ff38190a5dd637991914e238`
