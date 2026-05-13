> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAudioVAEDecode/es.md)

El nodo **LTXV Audio VAE Decode** convierte una representación latente de audio nuevamente en una forma de onda de audio. Utiliza un modelo especializado de Audio VAE para realizar este proceso de decodificación, generando una salida de audio con una frecuencia de muestreo específica.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `samples` | LATENT | Sí | N/A | El latente que se va a decodificar. |
| `audio_vae` | VAE | Sí | N/A | El modelo Audio VAE utilizado para decodificar el latente. |

**Nota:** Si el latente proporcionado está anidado (contiene múltiples latentes), el nodo utilizará automáticamente el último latente de la secuencia para la decodificación.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `Audio` | AUDIO | La forma de onda de audio decodificada y su frecuencia de muestreo asociada. La forma de onda es un tensor trasladado al mismo dispositivo que el latente de entrada, y la frecuencia de muestreo está determinada por el modelo Audio VAE. |

---
**Source fingerprint (SHA-256):** `e9df1da8ca0424cfc7ce97951e65154df845d98c3b73f76725fa657d851a3a07`
