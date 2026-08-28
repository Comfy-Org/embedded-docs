# VAEEncodeAudio

El nodo VAEEncodeAudio convierte datos de audio en una representación latente utilizando un Autoencoder Variacional (VAE). Toma una entrada de audio y la procesa a través del VAE para generar muestras latentes comprimidas que pueden usarse para tareas de generación o manipulación de audio. El nodo remuestrea automáticamente el audio para que coincida con la frecuencia de muestreo esperada del VAE si es necesario antes de codificarlo.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `audio` | Los datos de audio a codificar, que contienen la forma de onda y la información de frecuencia de muestreo | AUDIO | Sí | - |
| `vae` | El modelo de Autoencoder Variacional utilizado para codificar el audio en el espacio latente | VAE | Sí | - |

**Nota:** La entrada de audio se remuestrea automáticamente para que coincida con la frecuencia de muestreo esperada por el VAE (predeterminada: 44100 Hz) si la frecuencia de muestreo original difiere de este valor. Si el audio de entrada es `None` (por ejemplo, si el video de origen no tiene pista de audio), el nodo generará un error.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `LATENT` | La representación de audio codificada en el espacio latente, que contiene muestras comprimidas | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEEncodeAudio/es.md)

---
**Source fingerprint (SHA-256):** `224563af40a377a37209b26ec8becf035560da273b18293634f684e18c5e63ed`
