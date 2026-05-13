> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyAceStepLatentAudio/es.md)

El nodo EmptyAceStepLatentAudio crea muestras de audio latente vacías de una duración específica. Genera un lote de latentes de audio silenciosos rellenos con ceros, donde la longitud se calcula en función de los segundos de entrada y los parámetros de procesamiento de audio. Este nodo es útil para inicializar flujos de trabajo de procesamiento de audio que requieren representaciones latentes.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `seconds` | FLOAT | Sí | 1.0 - 1000.0 | La duración del audio en segundos (predeterminado: 120.0) |
| `batch_size` | INT | Sí | 1 - 4096 | El número de imágenes latentes en el lote (predeterminado: 1) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `output` | LATENT | Devuelve muestras de audio latente vacías con ceros. La salida contiene un tensor `samples` y un campo `type` establecido en "audio". |

---
**Source fingerprint (SHA-256):** `79fcfb3cb26db8a2ef4480455a44255e0d1a16f122a762d7608a78b2330cc637`
