# ARVideoI2V

## Descripción general

Este nodo prepara una configuración de generación de imagen a video para modelos de video AR (Auto-Regresivos). Toma una imagen inicial, la codifica en el espacio latente usando un VAE y almacena la imagen codificada en la configuración del modelo. Esto permite que el proceso de muestreo de video utilice la imagen como primer fotograma, iniciando efectivamente la generación sin necesidad de una arquitectura de modelo separada de imagen a video.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `modelo` | El modelo de video AR que se utilizará para la generación. | MODEL | Sí | - |
| `vae` | El modelo VAE utilizado para codificar la imagen inicial en el espacio latente. | VAE | Sí | - |
| `imagen_inicial` | La imagen inicial que servirá como primer fotograma del video generado. | IMAGE | Sí | - |
| `ancho` | El ancho de los fotogramas del video generado (predeterminado: 832). | INT | Sí | 16 a 8192 (paso: 16) |
| `alto` | La altura de los fotogramas del video generado (predeterminado: 480). | INT | Sí | 16 a 8192 (paso: 16) |
| `longitud` | El número total de fotogramas en el video generado (predeterminado: 81). | INT | Sí | 1 a 1024 (paso: 4) |
| `tamaño_de_lote` | La cantidad de secuencias de video a generar en un solo lote (predeterminado: 1). | INT | Sí | 1 a 64 |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `MODEL` | El modelo clonado con la imagen de inicio codificada almacenada en su configuración para la generación de video. | MODEL |
| `LATENT` | Un tensor latente vacío con las dimensiones correctas para el proceso de generación de video. | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ARVideoI2V/es.md)

---
**Source fingerprint (SHA-256):** `0445b279ba49fa946050cfa70d1e6b13240eaa600b99dfe63f27c3203dc4b61b`
