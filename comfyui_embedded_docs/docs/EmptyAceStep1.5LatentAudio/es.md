# EmptyAceStep1.5LatentAudio

El nodo The Empty Ace Step 1.5 Latent Audio crea un tensor latente vacío diseñado para el procesamiento de audio. Genera un latente de audio silencioso con una duración y un tamaño de lote específicos, que puede utilizarse como punto de partida para flujos de trabajo de generación de audio en ComfyUI. El nodo calcula la longitud del latente basándose en los segundos de entrada y una frecuencia de muestreo fija.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `seconds` | La duración del audio a generar, en segundos (predeterminado: 120.0). | FLOAT | Sí | 1.0 - 1000.0 |
| `batch_size` | El número de imágenes latentes en el lote (predeterminado: 1). | INT | Sí | 1 - 4096 |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `LATENT` | Un tensor latente vacío que representa audio silencioso, con un identificador de tipo "audio". La salida también incluye un valor `downscale_ratio_temporal` de 1764, que se utiliza para la reducción de escala temporal en el procesamiento de audio. | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyAceStep1.5LatentAudio/es.md)

---
**Source fingerprint (SHA-256):** `bb7120c91ce5d779147cb8553d6f96fa160d87468d4d87550fb6dd4ec89b1557`
