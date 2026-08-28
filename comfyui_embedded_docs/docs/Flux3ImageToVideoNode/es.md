# Flux 3 Imagen a Video

Flux 3 Image to Video anima de 1 a 10 imágenes con FLUX 3. Cada imagen se convierte en un fotograma del clip: una imagen lo abre, dos hacen una transición de la primera a la segunda, y más se distribuyen a lo largo del clip o se fijan en los momentos que elijas.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Cómo debe moverse y sonar la escena; el prompt se interpreta y expande antes de la generación. Debe contener al menos un carácter. | STRING | Sí | Texto multilínea (predeterminado: vacío) |
| `keyframes` | De 1 a 10 imágenes, en orden de reproducción. Mínimo 256x256 píxeles cada una. Entrada ampliable: conecta imágenes como `image_1`, `image_2`, etc. | IMAGE | Sí | De 1 a 10 imágenes |
| `placement` | "spread across the clip" permite que FLUX 3 coloque las imágenes (una abre el clip, dos se convierten en su inicio y fin); "at times" fija cada imagen en un segundo que elijas. | DYNAMIC_COMBO | Sí | `"spread across the clip"` (predeterminado)<br>`"at times"` |
| `times` | Un tiempo en segundos por imagen, separado por comas y en orden creciente, p. ej. "0, 2.5, 5". Solo aparece cuando `placement` es "at times"; se requiere un tiempo para cada imagen de fotograma clave. | STRING | No | Segundos separados por comas (predeterminado: "0") |
| `aspect_ratio` | Relación de aspecto de salida. "auto" elige una a partir del prompt y las entradas. | COMBO | Sí | `"auto"` (predeterminado)<br>otras relaciones de aspecto disponibles |
| `duration` | Duración del clip en segundos. "auto" ajusta la duración al contenido. | COMBO | Sí | `"auto"` (predeterminado)<br>otras duraciones disponibles |
| `resolution` | Resolución de salida. | COMBO | Sí | `"720p"` (predeterminado)<br>`"1080p"` |
| `generate_audio` | Generar audio sincronizado (ambiente, voz, efectos). Desactivado produce un video sin pista de audio. | BOOLEAN | Sí | true / false (predeterminado: true) |
| `safety_tolerance` | Tolerancia de moderación, 0 es la más estricta. Las solicitudes que envían imágenes o video se limitan a 2 sin importar el valor que establezcas aquí. | INT | Sí | 0 a 4 (predeterminado: 2, ajuste avanzado) |
| `seed` | Semilla para determinar si el nodo debe volver a ejecutarse; FLUX 3 elige su propia semilla, por lo que los resultados reales son no deterministas independientemente de este valor. | INT | Sí | 0 a 4294967295 (predeterminado: 42, control después de generar) |

Nota: `keyframes` debe contener al menos una imagen; el nodo genera un error si no hay ninguna conectada. Cada imagen de fotograma clave debe tener al menos 256x256 píxeles y su relación de aspecto no puede ser más extrema que 64:1.

Cuando `placement` es "spread across the clip" y se conectan 3 o más keyframes, `duration` debe establecerse en un valor explícito, no en "auto"; de lo contrario, el nodo genera un error.

Cuando `placement` es "at times", `times` debe proporcionar un tiempo en segundos por imagen. Los tiempos deben aumentar, no pueden ser negativos, y el último tiempo no puede superar el final del clip (hasta 20 segundos cuando `duration` es "auto").

Debido a que este nodo envía imágenes, `safety_tolerance` se limita a 2 sin importar el valor que establezcas.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|-------------|-------------|-----------|
| `video` | El clip de video generado a partir de las imágenes de fotograma clave con la relación de aspecto, duración, resolución y configuración de audio elegidas. | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Flux3ImageToVideoNode/es.md)

---
**Source fingerprint (SHA-256):** `1c49838dfa13adc2ed70a51094f0dd860df7207970b8dceab6bb273653d7161c`
