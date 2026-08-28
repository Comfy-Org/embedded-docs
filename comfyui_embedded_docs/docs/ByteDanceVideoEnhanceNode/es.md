# ByteDanceVideoEnhanceNode

Este nodo amplía y restaura videos mediante ByteDance vCube. Puede aumentar la resolución hasta 8K, eliminar artefactos de compresión y ruido, mejorar el color y la nitidez, y opcionalmente interpolar fotogramas para obtener una mayor tasa de fotogramas. El video se sube al servicio vCube, se procesa con el ajuste preestablecido de mejora seleccionado y se devuelve como un archivo de video mejorado.

## Entradas

### Entradas comunes

Estas entradas siempre están visibles.

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `vídeo` | Video a mejorar. La resolución de origen debe ser como máximo 2560x1440 (2K); el tamaño de salida se define mediante la entrada de resolución. | VIDEO | Sí | Como máximo 2560x1440 (2K) |
| `versión_de_herramienta` | 'standard' equilibra velocidad y calidad con más de 10 algoritmos de mejora. 'professional' utiliza más de 30 algoritmos para una restauración de calidad cinematográfica, tarda aproximadamente 3 veces más y cuesta 10 veces más. | DYNAMIC_COMBO | Sí | "standard"<br>"professional" |
| `resolución` | Resolución de salida. El lado corto se ajusta al nivel elegido y el lado largo sigue la relación de aspecto del origen. 'source' mantiene el tamaño de origen, 'custom' establece el lado corto en píxeles. Los orígenes más anchos o altos que aproximadamente 2.2:1 se facturan un nivel de resolución superior. | DYNAMIC_COMBO | Sí | "720p"<br>"1080p"<br>"2k"<br>"4k"<br>"8k"<br>"source"<br>"custom" |
| `fps` | Tasa de fotogramas de salida. Una tasa superior a la del origen permite la interpolación de fotogramas por IA; una inferior elimina fotogramas. 'source' mantiene la tasa de origen, hasta 120 fps. Las tasas superiores a 30 fps cuestan 2 veces más; por encima de 60 fps, 4 veces más. (predeterminado: "source") | COMBO | Sí | "source" (predeterminado)<br>Rates numéricas de fotogramas hasta 120 fps |
| `nivel_de_tasa_de_bits` | Tasa de bits objetivo del archivo entregado, ajustada a la resolución y tasa de fotogramas de salida. (predeterminado: "medium") | COMBO | Sí | "low"<br>"medium"<br>"high" |

### Entradas estándar

Se muestran cuando `tool_version` está establecido en "standard".

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `scene` | Ajuste preestablecido adaptado al contenido: 'aigc' para material generado por IA, 'common' para video general, 'ugc' para clips de teléfono comprimidos, 'short_series' para dramas con rostros, 'old_film' para material de archivo rayado o con parpadeo. (predeterminado: "aigc") | COMBO | Sí | "aigc"<br>"common"<br>"ugc"<br>"short_series"<br>"old_film" |
| `enhance_style` | 'hd' aplica una mejora más nítida; 'natural' reduce la intensidad para obtener un aspecto más suave y menos afilado. (predeterminado: "hd") | COMBO | Sí | "hd"<br>"natural" |

### Entradas profesionales

Se muestran cuando `tool_version` está establecido en "professional".

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `enhance_style` | 'hd' aplica una mejora más nítida; 'natural' reduce la intensidad para obtener un aspecto más suave y menos afilado. (predeterminado: "hd") | COMBO | Sí | "hd"<br>"natural" |

### Entradas de resolución personalizada

Se muestran cuando `resolution` está establecido en "custom".

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `short_side` | Lado corto de la salida en píxeles; el lado largo sigue la relación de aspecto del origen. (predeterminado: 1080) | INT | Sí | Predeterminado: 1080; limitado por los límites mínimo y máximo de lado corto de vCube |

### Notas

- El video de origen debe tener como máximo 2560x1440 (2K). Los videos de mayor tamaño se rechazan y deben reducirse antes de mejorar.
- La duración del video de origen está limitada a la duración máxima admitida por el servicio vCube.
- Cuando `tool_version` es "standard", tanto `scene` como `enhance_style` están disponibles. Cuando es "professional", solo está disponible `enhance_style`.
- Cuando `resolution` es "custom", se requiere el valor de `short_side`. Los ajustes preestablecidos de resolución y "source" no utilizan `short_side`.
- Cuando `resolution` es "source", la salida mantiene la resolución de origen.
- Cuando `fps` es "source", la tasa de fotogramas de salida coincide con la tasa de fotogramas de origen, hasta 120 fps.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `video` | El video mejorado, ampliado y restaurado a la resolución y tasa de fotogramas solicitadas. | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceVideoEnhanceNode/es.md)

---
**Source fingerprint (SHA-256):** `bfdd55ce12cabd6e6504129084e86dcf96abd8db4ff64abbe5974c0da7a42bda`
