# SeedVR2TemporalChunk

Este nodo divide un latente de video SeedVR2 en fragmentos temporales más pequeños con superposición, que pueden procesarse uno a la vez dentro de la VRAM disponible. Los fragmentos están diseñados para pasarse tanto al nodo Apply SeedVR2 Conditioning como a la entrada de latente del muestreador, y luego recombinarse mediante el nodo Merge SeedVR2 Latents.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Requerido | Rango |
|-----------|-------------|--------------|-----------|-------|
| `latent` | El latente SeedVR2 codificado por VAE que se va a dividir | LATENT | Sí | - |
| `temporal_overlap` | Fotogramas latentes compartidos entre fragmentos adyacentes y combinados con fundido cruzado al fusionar; 0 significa sin superposición (predeterminado: 0) | INT | No | 0 a 16384 |
| `chunking_mode` | manual = usa exactamente `frames_per_chunk`; auto = predice el fragmento más grande que quepa en la VRAM libre | COMBO | Sí | "auto"<br>"manual" |

Cuando `chunking_mode` está configurado en "manual", el siguiente parámetro estará disponible:

| Parámetro | Descripción | Tipo de Dato | Requerido | Rango |
|-----------|-------------|--------------|-----------|-------|
| `frames_per_chunk` | Fotogramas de píxeles por fragmento temporal (debe ser 4n+1: 1, 5, 9, 13, ...) (predeterminado: 21) | INT | Sí | 1 a 16384, paso 4 |

**Notas sobre las restricciones de parámetros:**
- El `latent` de entrada debe ser un latente de video de 5 dimensiones con forma (B, C, T, H, W) y exactamente 4 canales latentes
- Al usar el modo "manual", `frames_per_chunk` debe ser un valor 4n+1 (1, 5, 9, 13, 17, 21, ...)
- `temporal_overlap` se limita automáticamente para que sea menor que el tamaño del fragmento
- En el modo "auto", el nodo calcula el tamaño óptimo del fragmento basándose en la VRAM libre disponible

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
|------------------|-------------|--------------|
| `latents` | Los fragmentos temporales en orden secuencial | LATENT |
| `temporal_overlap` | La superposición efectiva de fotogramas latentes entre fragmentos adyacentes, para Merge SeedVR2 Latents | INT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SeedVR2TemporalChunk/es.md)

---
**Source fingerprint (SHA-256):** `40af2b690f74555efbe38f4cf76825417f52735ce90296a9ad662f78cfe4c6bf`
