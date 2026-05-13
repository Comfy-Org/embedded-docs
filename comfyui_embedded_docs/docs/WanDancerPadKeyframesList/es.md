> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanDancerPadKeyframesList/es.md)

# Descripción General

Este nodo toma una secuencia de imágenes y una pista de audio opcional, y las divide en un número especificado de segmentos rellenados. Está diseñado para preparar secuencias de fotogramas clave para generación de video, donde cada segmento se rellena a una longitud uniforme y se crea una máscara correspondiente para indicar qué fotogramas son válidos.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `images` | IMAGE | Sí | N/D | La secuencia de imágenes de entrada que se dividirá en segmentos. |
| `segment_length` | INT | Sí | 1 a 10000 | Longitud de cada segmento en fotogramas (predeterminado: 149). |
| `num_segments` | INT | Sí | 1 a 100 | Cuántos segmentos rellenados emitir como listas (predeterminado: 1). |
| `audio` | AUDIO | No | N/D | Audio a segmentar para cada segmento emitido. |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `keyframes_sequence` | IMAGE | Una lista de secuencias de fotogramas clave rellenadas, una para cada segmento. |
| `keyframes_mask` | MASK | Una lista de máscaras que indican los fotogramas válidos para cada segmento. |
| `audio_segment` | AUDIO | Una lista de segmentos de audio, uno para cada segmento de video. |

---
**Source fingerprint (SHA-256):** `c6a3ddca3fd61fcdb287fecb6969796eebd65e70f1174abdab57912586d27d00`
