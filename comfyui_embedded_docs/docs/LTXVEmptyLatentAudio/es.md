> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVEmptyLatentAudio/es.md)

El nodo LTXV Empty Latent Audio crea un lote de tensores de audio latente vacíos (rellenos con ceros). Utiliza la configuración de un modelo Audio VAE proporcionado para determinar las dimensiones correctas del espacio latente, como la cantidad de canales y bins de frecuencia. Este latente vacío sirve como punto de partida para flujos de trabajo de generación o manipulación de audio dentro de ComfyUI.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|---------------|-------------|-------|-------------|
| `frames_number` | INT | Sí | 1 a 1000 | Número de fotogramas. El valor predeterminado es 97. |
| `frame_rate` | INT | Sí | 1 a 1000 | Número de fotogramas por segundo. El valor predeterminado es 25. |
| `batch_size` | INT | Sí | 1 a 4096 | La cantidad de muestras de audio latente en el lote. El valor predeterminado es 1. |
| `audio_vae` | VAE | Sí | N/A | El modelo Audio VAE del cual obtener la configuración. Este parámetro es obligatorio. |

**Nota:** La entrada `audio_vae` es obligatoria. El nodo generará un error si no se proporciona.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|---------------|-------------|
| `Latent` | LATENT | Un tensor de audio latente vacío con la estructura (batch_size, z_channels, num_audio_latents, audio_freq) configurado para coincidir con el Audio VAE de entrada. La salida también incluye un campo `type` establecido en "audio". |

---
**Source fingerprint (SHA-256):** `1a8bfea98f14de014069016652b39542cfd9290cae2d870ab4e381e46aa1e08f`
