> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanDancerPadKeyframes/es.md)

# Descripción General

Este nodo prepara una secuencia de fotogramas clave para un segmento específico dentro de un proceso de generación de video más largo. Toma un lote de imágenes de entrada y una pista de audio, calcula cuántos fotogramas totales debe tener el video completo según la duración del audio, y luego distribuye las imágenes de entrada como fotogramas clave a lo largo del segmento seleccionado, rellenando el resto con fotogramas en blanco. También extrae la porción correspondiente del audio para ese segmento.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|---------------|-------------|-------|-------------|
| `images` | IMAGE | Sí | Lote de imágenes | Las imágenes de entrada que se distribuirán como fotogramas clave. |
| `segment_length` | INT | Sí | 1 a 10000 | Longitud de este segmento en fotogramas (predeterminado: 149). |
| `segment_index` | INT | Sí | 0 a 100 | Índice del segmento (0 para el primero, 1 para el segundo, etc., predeterminado: 0). |
| `audio` | AUDIO | Sí | Datos de audio | Audio para calcular el total de fotogramas de salida y extraer el audio del segmento. |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|---------------|-------------|
| `keyframes_sequence` | IMAGE | Secuencia de fotogramas clave rellenada para el segmento especificado. |
| `keyframes_mask` | MASK | Máscara que indica los fotogramas válidos (1 para posiciones de fotogramas clave, 0 para posiciones rellenadas). |
| `audio_segment` | AUDIO | Segmento de audio correspondiente a este segmento de video. |