> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVEmptyLatentAudio/es.md)

El nodo LTXV Empty Latent Audio crea un lote de tensores latentes de audio vacíos (rellenos de ceros). Utiliza la configuración de un modelo VAE de Audio proporcionado para determinar las dimensiones correctas del espacio latente, como el número de canales y bandas de frecuencia. Este latente vacío sirve como punto de partida para flujos de trabajo de generación o manipulación de audio dentro de ComfyUI.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `frames_number` | INT | Sí | 1 a 1000 | Número de fotogramas. El valor por defecto es 97. |
| `frame_rate` | INT | Sí | 1 a 1000 | Número de fotogramas por segundo. El valor por defecto es 25. |
| `batch_size` | INT | Sí | 1 a 4096 | El número de muestras de audio latente en el lote. El valor por defecto es 1. |
| `audio_vae` | VAE | Sí | N/A | El modelo VAE de Audio del cual obtener la configuración. Este parámetro es obligatorio. |

**Nota:** La entrada `audio_vae` es obligatoria. El nodo generará un error si no se proporciona.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `Latent` | LATENT | Un tensor latente de audio vacío con la estructura (muestras, frecuencia_de_muestreo, tipo) configurada para coincidir con el VAE de Audio de entrada. |
