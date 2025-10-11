> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyAudio/es.md)

El nodo EmptyAudio genera un clip de audio silencioso con duración, frecuencia de muestreo y configuración de canales especificadas. Crea una forma de onda que contiene todos ceros, produciendo silencio completo para la duración dada. Este nodo es útil para crear audio de marcador de posición o generar segmentos silenciosos en flujos de trabajo de audio.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `duration` | FLOAT | Sí | 0.0 a 1.8446744073709552e+19 | Duración del clip de audio silencioso en segundos (por defecto: 60.0) |
| `sample_rate` | INT | Sí | - | Frecuencia de muestreo del clip de audio silencioso (por defecto: 44100) |
| `channels` | INT | Sí | 1 a 2 | Número de canales de audio (1 para mono, 2 para estéreo) (por defecto: 2) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `AUDIO` | AUDIO | El clip de audio silencioso generado que contiene datos de forma de onda e información de frecuencia de muestreo |