# LTXV Audio Latente Vacío

El nodo LTXV Empty Latent Audio crea un lote de tensores de audio latente vacíos (rellenos con ceros). Utiliza la configuración de un modelo Audio VAE proporcionado para determinar las dimensiones correctas del espacio latente, como el número de canales y contenedores de frecuencia, y calcula el número de latentes de audio a partir del número de fotogramas y la velocidad de fotogramas. Este latente vacío sirve como punto de partida para flujos de trabajo de generación o manipulación de audio dentro de ComfyUI.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `frames_number` | Número de fotogramas. El valor predeterminado es 97. | INT | Sí | 1 a 1000 |
| `frame_rate` | Número de fotogramas por segundo. El valor predeterminado es 25.0. Acepta valores FLOAT o INT. | FLOAT | Sí | 1.0 a 1000.0 |
| `batch_size` | El número de muestras de audio latente en el lote. El valor predeterminado es 1. | INT | Sí | 1 a 4096 |
| `audio_vae` | El modelo Audio VAE del que se obtiene la configuración. Este parámetro es obligatorio. | VAE | Sí | N/D |

**Nota:** La entrada `audio_vae` es obligatoria. El nodo generará un error si no se proporciona.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `Latent` | Un tensor de audio latente vacío con la estructura (batch_size, z_channels, num_audio_latents, audio_freq) configurado para coincidir con el Audio VAE de entrada. La salida también incluye un campo `type` establecido en "audio". | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVEmptyLatentAudio/es.md)

---
**Source fingerprint (SHA-256):** `3ac1bf17ebdba7c3a73bdd795f561b7bee31798d8a1efc11b972db1944f873a4`
