> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEDecodeAudio/es.md)

El nodo VAEDecodeAudio convierte representaciones latentes de vuelta a formas de onda de audio utilizando un Autoencoder Variacional. Toma muestras de audio codificadas y las procesa a través del VAE para reconstruir el audio original, aplicando normalización para garantizar niveles de salida consistentes. El audio resultante se devuelve con una frecuencia de muestreo estándar de 44100 Hz.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `muestras` | LATENT | Sí | - | Las muestras de audio codificadas en el espacio latente que serán decodificadas de vuelta a forma de onda de audio |
| `vae` | VAE | Sí | - | El modelo de Autoencoder Variacional utilizado para decodificar las muestras latentes en audio |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `AUDIO` | AUDIO | La forma de onda de audio decodificada con volumen normalizado y frecuencia de muestreo de 44100 Hz |