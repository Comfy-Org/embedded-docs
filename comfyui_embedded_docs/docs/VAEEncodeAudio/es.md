> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEEncodeAudio/es.md)

El nodo VAEEncodeAudio convierte datos de audio en una representación latente utilizando un Autoencoder Variacional (VAE). Toma una entrada de audio y la procesa a través del VAE para generar muestras latentes comprimidas que pueden utilizarse para tareas posteriores de generación o manipulación de audio. El nodo remuestrea automáticamente el audio para que coincida con la frecuencia de muestreo esperada del VAE si es necesario antes de la codificación.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `audio` | AUDIO | Sí | - | Los datos de audio a codificar, que contienen información de forma de onda y frecuencia de muestreo |
| `vae` | VAE | Sí | - | El modelo de Autoencoder Variacional utilizado para codificar el audio en el espacio latente |

**Nota:** La entrada de audio se remuestrea automáticamente para que coincida con la frecuencia de muestreo esperada del VAE (predeterminada: 44100 Hz) si la frecuencia de muestreo original difiere de este valor.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `LATENT` | LATENT | La representación de audio codificada en el espacio latente, que contiene muestras comprimidas |

---
**Source fingerprint (SHA-256):** `db509ab571154c4cedbfc6cae6591bd2b67b2c6e2261766565cdb0205b2c2ecc`
