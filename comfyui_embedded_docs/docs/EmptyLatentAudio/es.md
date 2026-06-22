# EmptyLatentAudio

El nodo `EmptyLatentAudio` crea un tensor latente vacío para procesamiento de audio. Genera una representación latente de audio en blanco con una duración y tamaño de lote especificados, que puede utilizarse como punto de partida para flujos de trabajo de generación o procesamiento de audio. El nodo calcula automáticamente las dimensiones latentes apropiadas según la duración del audio y la frecuencia de muestreo.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `segundos` | La duración del audio en segundos (predeterminado: 47.6) | FLOAT | Sí | 1.0 - 1000.0 |
| `tamaño_del_lote` | El número de imágenes latentes en el lote (predeterminado: 1) | INT | Sí | 1 - 4096 |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `LATENT` | Devuelve un tensor latente vacío para procesamiento de audio con la duración y el tamaño de lote especificados. El tensor tiene una forma de [batch_size, 64, length], donde length se calcula a partir de la duración del audio y la frecuencia de muestreo. | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyLatentAudio/es.md)

---
**Source fingerprint (SHA-256):** `004f730131b179fe5ac072afe81b2e01a3937fceca5a260b4ae66f92774e96d9`
