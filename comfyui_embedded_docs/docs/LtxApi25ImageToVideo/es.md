# LTX 2.5 Imagen a Video

Este nodo genera un video de calidad profesional a partir de una imagen inicial utilizando un modelo LTX 2.5. Usted describe el contenido del video con un prompt de texto, selecciona una variante del modelo y ajusta la duración, la resolución, la frecuencia de fotogramas y la generación de audio. Opcionalmente, se puede proporcionar un fotograma final para definir el final del video.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `imagen` | Primer fotograma que se utilizará para el video. | IMAGE | Sí | Exactamente una imagen |
| `modelo` | Grupo de ajustes del modelo. Selecciona la variante del modelo LTX 2.5 a utilizar. | COMBO | Sí | "LTX-2.5 (Fast)"<br>"LTX-2.5 (Pro)" |
| `duración` | Duración del video generado en segundos. | INT | Sí | Entero |
| `resolución` | Resolución del video generado. Las opciones disponibles pueden depender del modelo seleccionado. | COMBO | Sí | "1280x720"<br>"720x1280"<br>"1920x1080"<br>"1080x1920"<br>"2560x1440"<br>"1440x2560"<br>"3840x2160"<br>"2160x3840" |
| `fps` | Frecuencia de fotogramas del video generado. | INT | Sí | Entero (predeterminado: 25) |
| `generar_audio` | Indica si se debe generar audio para el video. | BOOLEAN | Sí | True<br>False (predeterminado: True) |
| `prompt` | Descripción de texto del contenido del video a generar. Debe tener entre 1 y 10000 caracteres. | STRING | Sí | De 1 a 10000 caracteres |
| `semilla` | Valor de semilla para la generación reproducible. Usar la misma semilla con los mismos ajustes produce el mismo resultado. | INT | Sí | Entero (predeterminado: 42) |
| `último_fotograma` | Último fotograma que se utilizará para el video. | IMAGE | No | Exactamente una imagen |

**Nota:** Solo se admite una imagen para `image`. Si se proporciona `last_frame`, también debe contener exactamente una imagen. Las opciones disponibles de `model.resolution` pueden variar según la variante de `model` seleccionada.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `video` | El video generado a partir de la imagen inicial proporcionada y los ajustes de generación. | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LtxApi25ImageToVideo/es.md)

---
**Source fingerprint (SHA-256):** `13db42e5e0d4237424b30b960ec12f5dd16808d21b85e100e5861c095b351c79`
