# MinimaxHailuo03TextToVideoNode

Este nodo genera un video a partir de un prompt de texto utilizando el modelo MiniMax H3. Envía el texto junto con la configuración de video, como resolución, duración y relación de aspecto, a la API de MiniMax, y devuelve el video resultante como salida.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `model` | Modelo a utilizar para la generación de video. (predeterminado: "MiniMax H3"). Esta selección también incluye el prompt de texto, la resolución, la duración y la relación de aspecto para el video generado. | COMBO | Sí | `"MiniMax H3"` |
| `seed` | Semilla aleatoria. La misma solicitud con la misma semilla produce resultados similares, aunque no se garantiza que sean idénticos. (predeterminado: 42) | INT | Sí | 0 a 4294967295 |
| `watermark` | Indica si se añade una marca de agua AIGC al video. (predeterminado: false) | BOOLEAN | No | true<br>false |

Nota: El prompt de texto incluido en la opción `model` debe contener al menos un carácter que no sea un espacio en blanco. El precio estimado que se muestra para este nodo se calcula a partir de la duración del video seleccionado.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `VIDEO` | El video generado a partir del prompt de texto proporcionado. | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03TextToVideoNode/es.md)

---
**Source fingerprint (SHA-256):** `9478576dd02ed407a39c95c7227eb8e1482db8b77adc814691fbd807e4cc2893`
