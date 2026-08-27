# LtxApi25TextToVideo

LTX 2.5 Text To Video es un nodo de API que genera videos de calidad profesional a partir de una descripción textual utilizando el modelo LTX 2.5. Proporcionas un prompt y eliges ajustes de generación como el nivel del modelo, la duración, la resolución, la velocidad de cuadros y si se debe incluir audio; el nodo envía la tarea a la API de LTX y devuelve el video resultante.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `modelo` | El nivel del modelo LTX 2.5 que se usará para la generación de video. | STRING | Sí | "LTX-2.5 (Fast)"<br>"LTX-2.5 (Pro)" |
| `duración` | La duración del video generado. | INT | Sí | Entero |
| `resolución` | La resolución de salida del video. Las opciones disponibles dependen del `model` seleccionado. | STRING | Sí | Con "LTX-2.5 (Fast)":<br>"1280x720"<br>"720x1280"<br>"1920x1080"<br>"1080x1920"<br>"2560x1440"<br>"1440x2560"<br>"3840x2160"<br>"2160x3840"<br>Con "LTX-2.5 (Pro)":<br>"1280x720"<br>"720x1280"<br>"1920x1080"<br>"1080x1920" |
| `fps` | Velocidad de fotogramas del video generado (predeterminado: 25). | INT | No | Entero |
| `generar_audio` | Indica si se debe generar audio junto con el video (predeterminado: True). | BOOLEAN | No | True<br>False |
| `prompt` | La descripción textual del video a generar. Se requiere un prompt no vacío de hasta 10,000 caracteres (predeterminado: ""). | STRING | Sí | De 1 a 10000 caracteres |
| `semilla` | Valor de semilla utilizado para la generación reproducible (predeterminado: 42). | INT | No | Entero |

Nota: Las opciones disponibles de `model.resolution` dependen del `model` seleccionado. "LTX-2.5 (Fast)" admite resoluciones de hasta 2160x3840, mientras que "LTX-2.5 (Pro)" admite resoluciones de hasta 1920x1080.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `video` | El video generado devuelto por la API de LTX, listo para su uso posterior en el flujo de trabajo. Si la generación de audio estaba habilitada, el video incluye audio sincronizado. | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LtxApi25TextToVideo/es.md)

---
**Source fingerprint (SHA-256):** `02e131116fb0760cce2cea1e9bc49fa16dd7e4e296903fef5e44b7942b6e84c9`
