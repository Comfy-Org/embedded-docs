El nodo VAEDecodeAudio convierte representaciones latentes nuevamente en formas de onda de audio utilizando un Autoencoder Variacional. Toma muestras de audio codificadas y las procesa a través del VAE para reconstruir el audio original, aplicando normalización para garantizar niveles de salida consistentes. El audio resultante se devuelve con una frecuencia de muestreo estándar de 44100 Hz.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `muestras` | Las muestras de audio codificadas en el espacio latente que se decodificarán nuevamente a forma de onda de audio | LATENT | Sí | - |
| `vae` | El modelo de Autoencoder Variacional utilizado para decodificar las muestras latentes en audio | VAE | Sí | - |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `AUDIO` | La forma de onda de audio decodificada con volumen normalizado y frecuencia de muestreo de 44100 Hz | AUDIO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEDecodeAudio/es.md)

---
**Source fingerprint (SHA-256):** `15848d3763324cbae986949146d57352c68369713cd99a27d216797560836824`
