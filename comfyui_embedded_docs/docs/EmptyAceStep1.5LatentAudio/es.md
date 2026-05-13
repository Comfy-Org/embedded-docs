> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyAceStep1.5LatentAudio/es.md)

El nodo Empty Ace Step 1.5 Latent Audio crea un tensor latente vacío diseñado para procesamiento de audio. Genera un latente de audio silencioso con una duración y tamaño de lote específicos, que puede utilizarse como punto de partida para flujos de trabajo de generación de audio en ComfyUI. El nodo calcula la longitud del latente basándose en los segundos de entrada y una frecuencia de muestreo fija.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `seconds` | FLOAT | Sí | 1.0 - 1000.0 | La duración del audio a generar, en segundos (predeterminado: 120.0). |
| `batch_size` | INT | Sí | 1 - 4096 | El número de imágenes latentes en el lote (predeterminado: 1). |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `LATENT` | LATENT | Un tensor latente vacío que representa audio silencioso, con un identificador de tipo "audio". |

---
**Source fingerprint (SHA-256):** `8d2b0b8ea110362d5e43a72a27df0ff2012a8577fbaa4fef2bd7905c9c64bd6a`
