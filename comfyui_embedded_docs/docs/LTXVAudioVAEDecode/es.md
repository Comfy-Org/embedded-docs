# Decodificar LTXV Audio VAE

```markdown
# LTXV Audio VAE Decode

El nodo LTXV Audio VAE Decode convierte una representación latente de audio de vuelta a una forma de onda de audio. Utiliza un modelo especializado de Audio VAE para realizar este proceso de decodificación, produciendo una salida de audio con una frecuencia de muestreo específica.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `samples` | El latente a decodificar. | LATENT | Sí | N/A |
| `audio_vae` | El modelo Audio VAE utilizado para decodificar el latente. | VAE | Sí | N/A |

**Nota:** Si el latente proporcionado está anidado (contiene múltiples latentes), el nodo utilizará automáticamente el último latente de la secuencia para la decodificación.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `Audio` | La forma de onda de audio decodificada y su frecuencia de muestreo asociada. La forma de onda es un tensor movido al mismo dispositivo que el latente de entrada, y la frecuencia de muestreo está determinada por el modelo Audio VAE. | AUDIO |
```

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAudioVAEDecode/es.md)

---
**Source fingerprint (SHA-256):** `fc94f3cb78ede86ada374444d613411cc9bb5849e5cdb8a24074babee50719b1`
