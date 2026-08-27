# EmptyMiniMaxMusic3LatentAudio

Este nodo crea un latente de audio vacío (relleno de ceros) para el modelo MiniMax Music3. Convierte la duración solicitada en segundos en los marcos de audio correspondientes y produce un tensor latente en blanco del tamaño correcto, listo para usarse como punto de partida para la generación de música.

## Entradas

| Parámetro | Descripción | Tipo de dato | Obligatorio | Rango |
|-----------|-------------|--------------|-------------|-------|
| `seconds` | La duración del latente de audio en segundos (por defecto: 120.0). El valor se convierte a marcos de audio y se limita a los límites de duración admitidos por el modelo. | FLOAT | Sí | 0.04 a (MAX_AUDIO_FRAMES / AUDIO_FRAMES_PER_SECOND), paso 0.04 |
| `batch_size` | La cantidad de latentes de audio a generar en un solo lote (por defecto: 1). | INT | Sí | 1 a 4096 |

Nota: El valor de `seconds` se redondea al marco de audio más cercano y se limita a un mínimo de 1 marco y un máximo de `MAX_AUDIO_FRAMES` marcos, por lo que la longitud real del latente puede diferir ligeramente del valor exacto introducido.

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
|------------------|-------------|--------------|
| `LATENT` | Un tensor latente de audio relleno de ceros de forma (batch_size, 128, latent_length). Incluye metadatos que marcan la muestra como datos de audio con una relación de reducción temporal de 512. | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyMiniMaxMusic3LatentAudio/es.md)

---
**Source fingerprint (SHA-256):** `77e6a69702a837c958c2954bba061c979152f034bc7774a5b6c97ea8d57bda4b`
