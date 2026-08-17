# ARVideoI2V

## Resumen

Este nodo prepara una configuración de generación de video a partir de imagen para modelos de video AR (autorregresivos). Toma una imagen inicial, la codifica en el espacio latente mediante un VAE y almacena la imagen codificada en la configuración del modelo. Esto permite que el proceso de muestreo de video utilice la imagen como primer fotograma, lo que inicializa la generación sin necesidad de una arquitectura de modelo separada de imagen a video.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `model` | El modelo de video AR que se utilizará para la generación. | MODEL | Sí | - |
| `vae` | El modelo VAE utilizado para codificar la imagen inicial en el espacio latente. | VAE | Sí | - |
| `start_image` | La imagen inicial que servirá como primer fotograma del video generado. | IMAGE | Sí | - |
| `width` | El ancho de los fotogramas del video generado (por defecto: 832). | INT | Sí | 16 a 8192 (paso: 16) |
| `height` | La altura de los fotogramas del video generado (por defecto: 480). | INT | Sí | 16 a 8192 (paso: 16) |
| `length` | El número total de fotogramas del video generado (por defecto: 81). | INT | Sí | 1 a 1024 (paso: 4) |
| `batch_size` | El número de secuencias de video a generar en un solo lote (por defecto: 1). | INT | Sí | 1 a 64 |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| MODEL | El modelo clonado con la imagen inicial codificada almacenada en su configuración para la generación de video. | MODEL |
| LATENT | Un tensor latente vacío con forma `[batch_size, 16, lat_t, height/8, width/8]`, donde `lat_t = ((length - 1) // 4) + 1` es el número de fotogramas latentes derivado de la longitud de video solicitada. | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ARVideoI2V/es.md)

---
**Source fingerprint (SHA-256):** `984834951b9d5a22aef51c85a5019fd8ba58cdb2d6fff235371ed29f316896d8`
