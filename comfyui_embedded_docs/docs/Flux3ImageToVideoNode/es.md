# Flux3ImageToVideoNode

Flux 3 Image to Video anima de 1 a 10 imágenes con FLUX 3. Cada imagen se convierte en un fotograma del clip: una imagen lo abre, dos hacen una transición de la primera a la segunda, y más se distribuyen a lo largo del mismo o se fijan en momentos que tú elijas.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `prompt` | Cómo debe moverse y sonar la escena; el prompt se interpreta y expande antes de la generación. Debe contener al menos un carácter. | STRING | Sí | Texto multilínea (predeterminado: vacío) |
| `keyframes` | De 1 a 10 imágenes, en orden de reproducción. Cada una debe tener al menos 256x256 píxeles. Cada fotograma clave se convierte en un punto del clip. | IMAGE | Sí | De 1 a 10 imágenes |
| `placement` | 'spread across the clip' permite que FLUX 3 coloque las imágenes (una abre el clip, dos se convierten en su inicio y fin); 'at times' fija cada imagen en un segundo que tú elijas. | STRING | Sí | `"spread across the clip"` (predeterminado)<br>`"at times"` |
| `times` | Un tiempo en segundos por imagen, separados por comas y en orden creciente, p. ej. '0, 2.5, 5'. Obligatorio cuando `placement` es `"at times"`. | STRING | No | Segundos separados por comas (predeterminado: "0") |
| `aspect_ratio` | Relación de aspecto de salida. 'auto' elige una a partir del prompt y las entradas. | STRING | Sí | `"auto"` (predeterminado)<br>más otras opciones disponibles |
| `duration` | Duración del clip en segundos. 'auto' ajusta la duración al contenido. | STRING | Sí | `"auto"` (predeterminado)<br>más otras opciones disponibles |
| `resolution` | Resolución de salida. | STRING | Sí | `"720p"` (predeterminado)<br>`"1080p"` |
| `generate_audio` | Genera audio sincronizado (ambiente, voz, efectos). Desactivado produce un video sin pista de audio. | BOOLEAN | Sí | true / false (predeterminado: true) |
| `safety_tolerance` | Tolerancia de moderación; 0 es el más estricto. Las solicitudes que envían imágenes o video están limitadas a 2, sin importar lo que definas aquí. | INT | Sí | 0 a 4 (predeterminado: 2, configuración avanzada) |
| `seed` | Semilla para determinar si el nodo debe volver a ejecutarse; FLUX 3 elige su propia semilla, por lo que los resultados reales son no deterministas independientemente de este valor. | INT | Sí | 0 a 4294967295 (predeterminado: 42, con control después de generar) |

Nota: `keyframes` es obligatorio: el nodo genera un error si no se conecta ninguna imagen de fotograma clave. Cuando `placement` es `"spread across the clip"` y se proporcionan 3 o más imágenes, `duration` debe establecerse en un valor explícito (no `"auto"`); de lo contrario, el nodo genera un error. Cuando `placement` es `"at times"`, `times` debe proporcionar un tiempo en segundos por imagen, en orden creciente. Las solicitudes que envían imágenes están limitadas a una tolerancia de seguridad de 2, independientemente del valor definido.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `video` | El clip de video generado a partir de las imágenes de fotogramas clave con la relación de aspecto, duración, resolución y configuración de audio elegidas. | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Flux3ImageToVideoNode/es.md)

---
**Source fingerprint (SHA-256):** `3b9472194020ec98cd4e8c60463cdd0e9dc074ec6cbc1fc03d313894fa570ba8`
