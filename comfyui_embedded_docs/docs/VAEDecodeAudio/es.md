# VAEDecodeAudio

El nodo VAEDecodeAudio convierte representaciones latentes de vuelta en formas de onda de audio utilizando un autoencoder variacional. Toma muestras de audio codificadas y las procesa a través del VAE para reconstruir el audio original, aplicando normalización para garantizar niveles de salida consistentes. El audio resultante se devuelve con una frecuencia de muestreo de 44100 Hz por defecto, o con la frecuencia de muestreo de las muestras de entrada si se proporciona.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Requerido | Rango |
|-----------|-------------|--------------|-----------|-------|
| `muestras` | Las muestras de audio codificadas en el espacio latente que se decodificarán de vuelta a forma de onda de audio | LATENT | Sí | - |
| `vae` | El modelo de autoencoder variacional utilizado para decodificar las muestras latentes en audio | VAE | Sí | - |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
|------------------|-------------|--------------|
| `AUDIO` | La forma de onda de audio decodificada con volumen normalizado y frecuencia de muestreo (por defecto: 44100 Hz, o la frecuencia de muestreo de las muestras `samples` de entrada si está presente) | AUDIO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEDecodeAudio/es.md)

---
**Source fingerprint (SHA-256):** `2a3f5c912d1d84eea7768979f6b8f0eaa9fe89041f3a3352434f38abd3c09fea`
