> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyAudio/es.md)

El nodo EmptyAudio genera un clip de audio silencioso con una duración, frecuencia de muestreo y configuración de canales específicas. Crea una forma de onda que contiene todos ceros, produciendo silencio completo durante la duración indicada. Este nodo es útil para crear audio de relleno o generar segmentos silenciosos en flujos de trabajo de audio.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `duration` | FLOAT | Sí | 0.0 a 1.8446744073709552e+19 | Duración del clip de audio vacío en segundos (predeterminado: 60.0) |
| `sample_rate` | INT | Sí | 1 a 192000 | Frecuencia de muestreo del clip de audio vacío (predeterminado: 44100) |
| `channels` | INT | Sí | 1 a 2 | Número de canales de audio (1 para mono, 2 para estéreo) (predeterminado: 2) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `AUDIO` | AUDIO | El clip de audio silencioso generado que contiene datos de forma de onda e información de frecuencia de muestreo |

---
**Source fingerprint (SHA-256):** `61b9cd6c8e518f28533b7586fdd1f909e5c356c7f2f7690da4e1ec7965d53c5d`
