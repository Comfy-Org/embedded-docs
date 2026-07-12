# SeedVR2TemporalChunk

Este nodo divide un latente de video SeedVR2 en fragmentos temporales más pequeños que pueden procesarse uno a la vez dentro de la VRAM disponible. Calcula automáticamente el tamaño óptimo de fragmento según la memoria de tu GPU o te permite especificar el tamaño manualmente, y genera los fragmentos en orden secuencial para su procesamiento.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
|-----------|-------------|-----------|----------|-------|
| `latent` | El latente SeedVR2 codificado por VAE a dividir. | LATENT | Sí | - |
| `temporal_overlap` | Fotogramas latentes compartidos entre fragmentos adyacentes y combinados con fundido cruzado al fusionar; 0 significa sin superposición (predeterminado: 0). | INT | No | 0 a 16384 |
| `chunking_mode` | Manual usa exactamente frames_per_chunk; auto predice el fragmento más grande que quepa en la VRAM libre. | COMBO | Sí | "auto"<br>"manual" |

Cuando `chunking_mode` está configurado en "manual", un parámetro adicional estará disponible:

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
|-----------|-------------|-----------|----------|-------|
| `frames_per_chunk` | Fotogramas de píxeles por fragmento temporal. Debe ser un valor 4n+1 (1, 5, 9, 13, 17, 21, ...) (predeterminado: 21). | INT | Sí | 1 a 16384 |

Nota: El parámetro `frames_per_chunk` solo aparece cuando `chunking_mode` está configurado en "manual". El valor debe cumplir la fórmula `(frames_per_chunk - 1) % 4 == 0`, lo que significa que debe ser uno de: 1, 5, 9, 13, 17, 21, etc.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
|-------------|-------------|-----------|
| `latents` | Los fragmentos temporales en orden secuencial. | LATENT |
| `temporal_overlap` | La superposición efectiva de fotogramas latentes entre fragmentos adyacentes, para Fusionar Latentes SeedVR2. | INT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SeedVR2TemporalChunk/es.md)

---
**Source fingerprint (SHA-256):** `40af2b690f74555efbe38f4cf76825417f52735ce90296a9ad662f78cfe4c6bf`
