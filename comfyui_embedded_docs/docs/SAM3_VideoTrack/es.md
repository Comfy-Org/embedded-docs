> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SAM3_VideoTrack/es.md)

Esta documentación fue generada por IA. Si encuentras algún error o tienes sugerencias de mejora, ¡no dudes en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SAM3_VideoTrack/en.md)

## Resumen

Rastrea objetos a través de fotogramas de video utilizando el rastreador basado en memoria de SAM3. Este nodo procesa una secuencia de fotogramas de video y mantiene las identidades de los objetos a lo largo de los fotogramas, utilizando máscaras iniciales o indicaciones de texto para definir qué rastrear.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|---------------|-------------|-------|-------------|
| `images` | IMAGE | Sí | Fotogramas de video por lotes | Fotogramas de video como imágenes por lotes |
| `model` | MODEL | Sí | Modelo SAM3 | El modelo SAM3 a utilizar para el rastreo |
| `initial_mask` | MASK | No | Una máscara por objeto | Máscara(s) para el primer fotograma a rastrear (una por objeto). Obligatorio si no se proporciona `conditioning`. |
| `conditioning` | CONDITIONING | No | Condicionamiento de texto | Condicionamiento de texto para detectar nuevos objetos durante el rastreo. Obligatorio si no se proporciona `initial_mask`. |
| `detection_threshold` | FLOAT | No | 0.0 a 1.0 (predeterminado: 0.5) | Umbral de puntuación para la detección mediante indicaciones de texto |
| `max_objects` | INT | No | 0 a ilimitado (predeterminado: 0) | Máximo de objetos rastreados (0=ilimitado). Las máscaras iniciales cuentan para este límite. |
| `detect_interval` | INT | No | 1 a ilimitado (predeterminado: 1) | Ejecutar detección cada N fotogramas (1=cada fotograma). Valores más altos ahorran cómputo. |

**Nota:** Se debe proporcionar `initial_mask` o `conditioning`. Si se omiten ambos, el nodo generará un error.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|---------------|-------------|
| `track_data` | SAM3TrackData | Datos de rastreo que contienen máscaras de objetos y metadatos en todos los fotogramas de video |