# EmptyAceStepLatentAudio

El nodo EmptyAceStepLatentAudio crea muestras de audio latente vacías de una duración específica. Genera un lote de latentes de audio silenciosos rellenos con ceros, donde la longitud se calcula en función de los segundos de entrada y los parámetros de procesamiento de audio. Este nodo es útil para inicializar flujos de trabajo de procesamiento de audio que requieren representaciones latentes.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `segundos` | La duración del audio en segundos (predeterminado: 120.0) | FLOAT | Sí | 1.0 - 1000.0 |
| `tamaño_del_lote` | El número de imágenes latentes en el lote (predeterminado: 1) | INT | Sí | 1 - 4096 |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `output` | Devuelve muestras de audio latente vacías con ceros. La salida contiene un tensor `samples` y un campo `type` establecido en "audio". | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyAceStepLatentAudio/es.md)

---
**Source fingerprint (SHA-256):** `79fcfb3cb26db8a2ef4480455a44255e0d1a16f122a762d7608a78b2330cc637`
