# MinimaxHailuo03ContextIRNode

Este nodo utiliza MiniMax H3 Context IR para analizar tu descripción de texto y cualquier medio adjunto, y luego produce un prompt de video más robusto y estructurado. El prompt devuelto está diseñado para conectarse a la entrada `prompt` de un nodo de video MiniMax H3; si adjuntas medios allí, adjunta los mismos medios en el mismo orden, porque el prompt mejorado se refiere a los medios por posición.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `model` | Modelo a utilizar para la mejora del prompt. | COMBO | Sí | `"MiniMax H3"` |
| `prompt` | Descripción del video que deseas generar. No puede estar vacía. (predeterminado: `""`) | STRING | Sí | Cualquier texto |
| `duration` | Duración del video que deseas generar, en segundos (4-15). (predeterminado: 5) | INT | Sí | 4 a 15 |
| `ratio` | Relación de aspecto del video que deseas generar. `"adaptive"` requiere al menos una entrada de imagen, video o audio. (predeterminado: `"adaptive"`) | COMBO | Sí | `"adaptive"`<br>`"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"` |
| `reference_images` | Imágenes de referencia de sujeto o estilo, a las que se hace referencia en el prompt como "Image 1".."Image 9" en orden de conexión. Hasta 9 imágenes. | IMAGE | No | 0 a 9 imágenes |
| `reference_videos` | Videos de referencia de movimiento o escena, a los que se hace referencia en el prompt como "Video 1".."Video 3" en orden de conexión. Hasta 3 videos, de 2 a 15 segundos cada uno, 15 segundos en total. | VIDEO | No | 0 a 3 videos |
| `reference_audios` | Referencias de audio, a las que se hace referencia en el prompt como "Audio 1".."Audio 3" en orden de conexión. Hasta 3 clips, de 2 a 15 segundos cada uno, 15 segundos en total. No se pueden usar sin una imagen o video de referencia. | AUDIO | No | 0 a 3 clips |
| `first_frame` | Primer fotograma del video que deseas generar. No se puede combinar con medios de referencia. | IMAGE | No | Imagen única |
| `last_frame` | Último fotograma del video que deseas generar. No se puede combinar con medios de referencia. | IMAGE | No | Imagen única |

### Restricciones de los parámetros

- Las entradas `prompt`, `duration`, `ratio`, `reference_images`, `reference_videos` y `reference_audios` forman parte del grupo de opciones `model`.
- `first_frame` y `last_frame` no se pueden combinar con ningún medio de referencia.
- `reference_audios` no se puede usar a menos que también se conecte al menos una `reference_image` o `reference_video`.
- Cuando no se conectan fotogramas ni medios de referencia, `ratio` no se puede establecer en `"adaptive"`.
- Los videos de referencia deben durar aproximadamente de 2 a 15 segundos cada uno, con una duración total no mayor a 15 segundos. Su velocidad de fotogramas debe estar entre 23.9 y 60.5 FPS.
- Los audios de referencia deben durar aproximadamente de 2 a 15 segundos cada uno, con una duración total no mayor a 15 segundos.
- `first_frame`, `last_frame` y cada imagen de referencia deben tener al menos 256x256 píxeles y una relación de aspecto entre 0.4 y 2.5.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `STRING` | El prompt de video estructurado y mejorado generado por MiniMax H3 Context IR. Se puede conectar a la entrada `prompt` de un nodo de generación de video MiniMax H3. | STRING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03ContextIRNode/es.md)

---
**Source fingerprint (SHA-256):** `73015517f9c0f55f0aceeef935508a372e0d95668e4733d1c8100b53e4afa7e2`
