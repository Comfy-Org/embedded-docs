# VAE Decodificar audio (en mosaico)

Este nodo convierte una representación de audio comprimida (muestras latentes) de vuelta a una forma de onda de audio utilizando un Autoencoder Variacional (VAE). Procesa los datos en secciones más pequeñas y superpuestas (tiles) para gestionar el uso de memoria, lo que lo hace adecuado para manejar secuencias de audio más largas.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `samples` | La representación latente comprimida del audio a decodificar. | LATENT | Sí | N/A |
| `vae` | El modelo de Autoencoder Variacional utilizado para realizar la decodificación. | VAE | Sí | N/A |
| `tile_size` | El tamaño de cada tile de procesamiento. El audio se decodifica en secciones de esta longitud para conservar memoria (por defecto: 512). | INT | Sí | 32 a 8192 |
| `overlap` | El número de muestras que se superponen entre tiles adyacentes. Esto ayuda a reducir los artefactos en los bordes entre tiles (por defecto: 64). | INT | Sí | 0 a 1024 |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `output` | La forma de onda de audio decodificada. | AUDIO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEDecodeAudioTiled/es.md)

---
**Source fingerprint (SHA-256):** `5ddedf218ba27ab9f463646c1e5288091172f2d7fae8f2980bb2b5e4d3dca89c`
