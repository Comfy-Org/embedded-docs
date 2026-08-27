# ByteDance2ReferenceNodeV2

ByteDance Seedance 2.5 Reference to Video genera, edita o extiende videos utilizando los modelos ByteDance Seedance (Seedance 2.5, 2.0, 2.0 Fast y 2.0 Mini) guiados por un prompt de texto e imágenes, videos, audio o activos de biblioteca previamente subidos opcionales. Sube las referencias, envía una tarea de generación, espera a que se complete y devuelve el archivo de video final.

## Entradas

### Entradas comunes

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
|-----------|-------------|--------------|-----------|-------|
| `model` | Selector de modelo. Seedance 2.5 para el modelo más reciente, videos de hasta 30 segundos y salida mp4/mov; Seedance 2.0 para máxima calidad y 4K; Fast para optimizar la velocidad; Mini para la generación más rápida y de menor costo. Seleccionar un modelo cambia los widgets de entrada que se muestran a continuación. | DYNAMIC_COMBO | Sí | "Seedance 2.5"<br>"Seedance 2.0"<br>"Seedance 2.0 Fast"<br>"Seedance 2.0 Mini" |
| `seed` | La semilla controla si el nodo debe volver a ejecutarse; los resultados son no deterministas independientemente de la semilla. Predeterminado: 0. | INT | Sí | 0 a 2147483647 |
| `watermark` | Si se debe añadir una marca de agua al video. Predeterminado: False. Configuración avanzada. | BOOLEAN | Sí | true<br>false |

### Entradas de Seedance 2.5

Estas entradas aparecen cuando `model` está configurado en "Seedance 2.5".

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
|-----------|-------------|--------------|-----------|-------|
| `prompt` | Prompt de texto para la generación de video. Pon las líneas habladas entre comillas dobles para dirigir el diálogo generado. Predeterminado: cadena vacía. | STRING | Sí | Texto multilínea |
| `resolution` | Resolución del video de salida. Predeterminado: 720p. | COMBO | Sí | "480p"<br>"720p"<br>"1080p" |
| `ratio` | Relación de aspecto del video de salida. Predeterminado: 16:9. | COMBO | Sí | "16:9"<br>"4:3"<br>"1:1"<br>"3:4"<br>"9:16"<br>"21:9"<br>"adaptive" |
| `duration` | Duración del video de salida en segundos (4-30). Predeterminado: 5. | INT | Sí | 4 a 30 |
| `generate_audio` | Habilitar la generación de audio para el video de salida. Predeterminado: True. | BOOLEAN | Sí | true<br>false |
| `task_type` | Qué hacer con el material de referencia. Todos los valores excepto auto se validan cuando se envía la tarea, por lo que los ajustes incompatibles fallan antes de que comience la generación.<br>auto: el modelo infiere la tarea a partir del prompt y las entradas, y los ajustes que contradicen su interpretación solo fallan después de que la generación haya comenzado.<br>reference: genera un video nuevo guiado por las imágenes, videos y audio de referencia.<br>edit: modifica un video de referencia conectado (añadir, eliminar, reemplazar); la salida conserva la duración y la relación de aspecto del clip de origen, y los widgets de duración y relación de aspecto se ignoran.<br>extend: continúa un video de referencia conectado hacia adelante o hacia atrás; el prompt debe decir "extend forward", "extend backward" o "continue", la relación de aspecto sigue al clip de origen, y la salida contiene solo el segmento recién generado con la duración que establezcas, no el clip de origen. Predeterminado: auto. | COMBO | Sí | "auto"<br>"reference"<br>"edit"<br>"extend" |
| `output_format` | Formato de contenedor del video de salida. Predeterminado: mp4. | COMBO | Sí | "mp4" |

### Entradas de Seedance 2.0

Estas entradas aparecen cuando `model` está configurado en "Seedance 2.0".

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
|-----------|-------------|--------------|-----------|-------|
| `prompt` | Prompt de texto para la generación de video. Predeterminado: cadena vacía. | STRING | Sí | Texto multilínea |
| `resolution` | Resolución del video de salida. | COMBO | Sí | "480p"<br>"720p"<br>"1080p"<br>"4k" |
| `ratio` | Relación de aspecto del video de salida. Predeterminado: adaptive. | COMBO | Sí | "16:9"<br>"4:3"<br>"1:1"<br>"3:4"<br>"9:16"<br>"21:9"<br>"adaptive" |
| `duration` | Duración del video de salida en segundos (4-15). Predeterminado: 7. | INT | Sí | 4 a 15 |
| `generate_audio` | Habilitar la generación de audio para el video de salida. Predeterminado: True. | BOOLEAN | Sí | true<br>false |

### Entradas de Seedance 2.0 Fast y Seedance 2.0 Mini

Estas entradas aparecen cuando `model` está configurado en "Seedance 2.0 Fast" o "Seedance 2.0 Mini". Ambos modelos comparten el mismo conjunto de entradas.

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
|-----------|-------------|--------------|-----------|-------|
| `prompt` | Prompt de texto para la generación de video. Predeterminado: cadena vacía. | STRING | Sí | Texto multilínea |
| `resolution` | Resolución del video de salida. | COMBO | Sí | "480p"<br>"720p" |
| `ratio` | Relación de aspecto del video de salida. Predeterminado: adaptive. | COMBO | Sí | "16:9"<br>"4:3"<br>"1:1"<br>"3:4"<br>"9:16"<br>"21:9"<br>"adaptive" |
| `duration` | Duración del video de salida en segundos (4-15). Predeterminado: 7. | INT | Sí | 4 a 15 |
| `generate_audio` | Habilitar la generación de audio para el video de salida. Predeterminado: True. | BOOLEAN | Sí | true<br>false |

### Entradas de referencia

Estas ranuras de referencia ampliables están disponibles para todos los modelos. El número máximo de ranuras difiere según el modelo: Seedance 2.5 admite hasta 30 imágenes, 10 videos, 10 audios y 30 activos; Seedance 2.0, 2.0 Fast y 2.0 Mini admiten hasta 9 imágenes, 3 videos, 3 audios y 9 activos.

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
|-----------|-------------|--------------|-----------|-------|
| `reference_images` | Ranura ampliable: conecta de 1 a N imágenes de referencia que guían la salida. El límite de cantidad es por modelo (consulta las secciones de modelos). Las imágenes se validan por relación de aspecto (0.4 a 2.5) y se reducen automáticamente a un lado máximo de 6000 píxeles. | IMAGE | No | 1..9 ranuras (familia Seedance 2.0)<br>1..30 ranuras (Seedance 2.5) |
| `reference_videos` | Ranura ampliable: conecta de 1 a N videos de referencia. El límite de cantidad es por modelo (consulta las secciones de modelos). Cada video debe tener al menos 1.8 segundos de duración y debe ajustarse a los límites de píxeles del modelo y la resolución seleccionados. | VIDEO | No | 1..3 ranuras (familia Seedance 2.0)<br>1..10 ranuras (Seedance 2.5) |
| `reference_audios` | Ranura ampliable: conecta de 1 a N pistas de audio de referencia. El límite de cantidad es por modelo (consulta las secciones de modelos). Cada audio debe tener al menos 1.8 segundos de duración. | AUDIO | No | 1..3 ranuras (familia Seedance 2.0)<br>1..10 ranuras (Seedance 2.5) |
| `reference_assets` | Ranura ampliable: conecta de 1 a N cadenas de ID de activo para medios ya subidos a la biblioteca virtual de Seedance. Cada activo debe estar activo. Puedes referirte a un activo en el prompt con tokens como `asset1` o `asset 1`; el nodo los reemplaza con la etiqueta posicional del activo (por ejemplo "Image 2" o "Video 1"). | STRING | No | 1..9 ranuras (familia Seedance 2.0)<br>1..30 ranuras (Seedance 2.5) |
| `auto_downscale` | Reducir automáticamente la escala de los videos de referencia que superen el presupuesto de píxeles del modelo para la resolución seleccionada. Se conserva la relación de aspecto; los videos que ya están dentro de los límites no se modifican. Predeterminado: True. | BOOLEAN | No | true<br>false |
| `auto_upscale` | Ampliar automáticamente la escala de los videos de referencia que estén por debajo del recuento mínimo de píxeles del modelo para la resolución seleccionada. Se conserva la relación de aspecto; los videos que ya cumplen el mínimo no se modifican. Nota: ampliar una fuente de baja resolución no añade detalle real y puede producir generaciones de menor calidad. Predeterminado: False. Configuración avanzada. | BOOLEAN | No | true<br>false |

**Nota:** Se requiere al menos una imagen, video o activo de referencia para ejecutar el nodo (Seedance 2.5 también acepta referencias solo de audio). Los videos y audios de referencia deben tener cada uno al menos 1.8 segundos de duración, y la duración combinada de todos los videos de referencia (y, por separado, de todos los audios de referencia) no debe exceder el máximo de segundos totales del modelo seleccionado. Las imágenes de referencia deben tener una relación de aspecto entre aproximadamente 2:5 y 5:2 (0.4 a 2.5), tener al menos 300x300 píxeles, y se reducen automáticamente a un lado máximo de 6000 píxeles. Las opciones `task_type` "edit" y "extend" solo están disponibles con Seedance 2.5 y ambas requieren al menos un video de referencia; cuando se usa "edit", la salida conserva la duración y la relación de aspecto del clip de origen y los widgets `duration` y `ratio` se ignoran, y cuando se usa "extend", la salida contiene solo el segmento recién generado con la duración que establezcas. Los activos referenciados deben estar en estado activo; de lo contrario, la tarea falla.

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
|------------------|-------------|--------------|
| `video` | El video generado, descargado del proveedor una vez que se completa la tarea de generación. Contiene audio cuando la generación de audio está habilitada. | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2ReferenceNodeV2/es.md)

---
**Source fingerprint (SHA-256):** `3a6bba12e719204ba5dba9d7d5f2b4c5285ed68974ee015b6e4a7892a1cf0933`
