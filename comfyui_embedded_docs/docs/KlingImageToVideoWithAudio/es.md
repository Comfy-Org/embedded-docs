> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingImageToVideoWithAudio/es.md)

El nodo Kling Image(First Frame) to Video with Audio utiliza el modelo de IA Kling para generar un video corto a partir de una única imagen inicial y un mensaje de texto. Crea una secuencia de video que comienza con la imagen proporcionada y puede incluir opcionalmente audio generado por IA para acompañar el contenido visual.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|---------------|-------------|-------|-------------|
| `model_name` | COMBO | Sí | `"kling-v2-6"` | La versión específica del modelo de IA Kling a utilizar para la generación del video. |
| `fotograma_inicial` | IMAGE | Sí | - | La imagen que servirá como primer fotograma del video generado. La imagen debe tener al menos 300x300 píxeles y una relación de aspecto entre 1:2.5 y 2.5:1. |
| `prompt` | STRING | Sí | - | Mensaje de texto positivo. Describe el contenido del video que deseas generar. El mensaje debe tener entre 1 y 2500 caracteres. |
| `modo` | COMBO | Sí | `"pro"` | El modo operativo para la generación del video. |
| `duración` | COMBO | Sí | `5`<br>`10` | La duración del video a generar, en segundos. |
| `generar_audio` | BOOLEAN | No | - | Cuando está habilitado, el nodo generará audio para acompañar el video. Cuando está deshabilitado, el video será silencioso. (valor predeterminado: True) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|---------------|-------------|
| `video` | VIDEO | El archivo de video generado, que puede incluir audio dependiendo de la entrada `generar_audio`. |

---
**Source fingerprint (SHA-256):** `f161eedbc5d780805e3d0ca32b6be94cc78afcd2749e065c032ea20991b782fc`
