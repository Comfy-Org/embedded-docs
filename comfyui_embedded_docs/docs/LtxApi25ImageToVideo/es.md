# LtxApi25ImageToVideo

Este nodo genera un video de calidad profesional basado en una imagen inicial. Puedes elegir la variante del modelo LTX 2.5, describir el video con un prompt de texto, ajustar la duración, resolución, velocidad de fotogramas y generación de audio, y opcionalmente proporcionar un fotograma final. El resultado es un video que comienza a partir de la imagen proporcionada.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|-----------|----------|-------|
| `imagen` | Primera imagen (fotograma) que se utilizará para el video. | IMAGE | Sí | Exactamente una imagen |
| `modelo` | Grupo de configuración del modelo. Selecciona la variante del modelo LTX 2.5 a utilizar. | COMBO | Sí | "LTX-2.5 (Fast)"<br>"LTX-2.5 (Pro)" |
| `duración` | Duración del video generado en segundos. | INT | Sí | Entero |
| `resolución` | Resolución del video generado. Las opciones disponibles pueden depender del modelo seleccionado. | COMBO | Sí | "1280x720"<br>"720x1280"<br>"1920x1080"<br>"1080x1920"<br>"2560x1440"<br>"1440x2560"<br>"3840x2160"<br>"2160x3840" |
| `fps` | Velocidad de fotogramas del video generado. | INT | Sí | Entero (predeterminado: 25) |
| `generar_audio` | Si se debe generar audio para el video. | BOOLEAN | Sí | True<br>False |
| `prompt` | Descripción de texto del contenido del video a generar. Debe tener entre 1 y 10000 caracteres. | STRING | Sí | 1 a 10000 caracteres |
| `semilla` | Valor de semilla para generación reproducible. Usar la misma semilla con la misma configuración produce el mismo resultado. | INT | Sí | Entero (predeterminado: 42) |
| `último_fotograma` | Último fotograma que se utilizará para el video. | IMAGE | No | Exactamente una imagen |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|-------------|-------------|-----------|
| `video` | El video generado a partir de la imagen inicial proporcionada y la configuración de generación. | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LtxApi25ImageToVideo/es.md)

---
**Source fingerprint (SHA-256):** `13db42e5e0d4237424b30b960ec12f5dd16808d21b85e100e5861c095b351c79`
