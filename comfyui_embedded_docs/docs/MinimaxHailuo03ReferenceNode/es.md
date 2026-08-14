# MinimaxHailuo03ReferenceNode

Este nodo genera un video utilizando el modelo MiniMax H3, usando imágenes, videos y audio de referencia para condicionar el resultado. Las referencias se mencionan en el prompt por su orden de conexión: "Image 1", "Image 2", "Video 1", "Audio 1", y así sucesivamente.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|-----------|----------|-------|
| `modelo` | Modelo a utilizar para la generación de video (por defecto: "MiniMax H3"). Al seleccionar "MiniMax H3" se proporcionan los ajustes `prompt`, `duration`, `resolution`, `ratio`, `reference_images`, `reference_videos` y `reference_audios` que se muestran a continuación. | STRING | Sí | "MiniMax H3" |
| `prompt` | Descripción de texto del video a generar. Los medios de referencia pueden mencionarse por su orden, por ejemplo "Image 1", "Image 2", "Video 1" o "Audio 1". | STRING | Sí | Longitud mínima: 1 carácter |
| `duration` | Duración del video generado en segundos. | INT | Sí | Múltiples opciones disponibles |
| `resolution` | Resolución de salida del video generado. | STRING | Sí | Múltiples opciones disponibles |
| `ratio` | Relación de aspecto del video generado. | STRING | Sí | Múltiples opciones disponibles |
| `reference_images` | Imágenes de referencia de sujeto o estilo, mencionadas en el prompt como "Image 1".."Image 9" en orden de conexión. Hasta 9 imágenes. | IMAGE | No | 0 a 9 imágenes |
| `reference_videos` | Videos de referencia de movimiento o escena, mencionados en el prompt como "Video 1".."Video 3" en orden de conexión. Hasta 3 videos, de 2 a 15 segundos cada uno, 15 segundos en total. | VIDEO | No | 0 a 3 videos |
| `reference_audios` | Referencias de audio, mencionadas en el prompt como "Audio 1".."Audio 3" en orden de conexión. Hasta 3 clips, de 2 a 15 segundos cada uno, 15 segundos en total. No se pueden utilizar sin una imagen o video de referencia. | AUDIO | No | 0 a 3 clips |
| `semilla` | Semilla aleatoria. La misma solicitud con la misma semilla produce resultados similares, aunque no se garantiza que sean idénticos (por defecto: 42). | INT | Sí | 0 a 4294967295 |
| `marca de agua` | Si se debe añadir una marca de agua AIGC al video (por defecto: false). | BOOLEAN | No | true<br>false |

### Restricciones de los parámetros

- Se requiere al menos una imagen de referencia o un video de referencia. No se acepta solo audio de referencia.
- Cada imagen de referencia debe tener una relación de aspecto entre aproximadamente 0.4 y 2.5 (2:5 a 5:2) y un ancho y alto mínimo de 256 píxeles.
- Cada video de referencia debe tener una duración de entre 2 y 15 segundos, con una frecuencia de imagen entre 23.976 y 60 FPS. La duración total de todos los videos de referencia no puede superar los 15 segundos.
- Cada clip de audio de referencia debe tener una duración de entre 2 y 15 segundos. La duración total de todos los clips de audio de referencia no puede superar los 15 segundos.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|-------------|-------------|-----------|
| `video` | El video generado. | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03ReferenceNode/es.md)

---
**Source fingerprint (SHA-256):** `beca020333a544188e6c21829eb8e63415aa5299efc676438e85662a5f08660d`
