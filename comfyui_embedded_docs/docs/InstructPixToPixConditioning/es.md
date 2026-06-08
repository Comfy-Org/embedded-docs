El nodo InstructPixToPixConditioning prepara datos de condicionamiento para la edición de imágenes InstructPix2Pix combinando indicaciones de texto positivas y negativas con datos de imagen. Procesa las imágenes de entrada a través de un codificador VAE para crear representaciones latentes y adjunta estos latentes tanto a los datos de condicionamiento positivos como a los negativos. El nodo maneja automáticamente las dimensiones de la imagen recortándolas a múltiplos de 8 píxeles para garantizar la compatibilidad con el proceso de codificación VAE.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `positivo` | Datos de condicionamiento positivos que contienen indicaciones de texto y configuraciones para las características deseadas de la imagen | CONDITIONING | Sí | - |
| `negativo` | Datos de condicionamiento negativos que contienen indicaciones de texto y configuraciones para las características no deseadas de la imagen | CONDITIONING | Sí | - |
| `vae` | Modelo VAE utilizado para codificar las imágenes de entrada en representaciones latentes | VAE | Sí | - |
| `píxeles` | Imagen de entrada que se procesará y codificará en el espacio latente | IMAGE | Sí | - |

**Nota:** Las dimensiones de la imagen de entrada se ajustan automáticamente recortándolas al múltiplo de 8 píxeles más cercano tanto en ancho como en alto para garantizar la compatibilidad con el proceso de codificación VAE.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `negativo` | Datos de condicionamiento positivos con la representación de imagen latente adjunta | CONDITIONING |
| `latente` | Datos de condicionamiento negativos con la representación de imagen latente adjunta | CONDITIONING |
| `latent` | Tensor latente vacío con las mismas dimensiones que la imagen codificada | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/InstructPixToPixConditioning/es.md)

---
**Source fingerprint (SHA-256):** `4b2383c9d64efdb558758359bf544fc5a1be65c12b23b54152e2df79a6dd8d79`
