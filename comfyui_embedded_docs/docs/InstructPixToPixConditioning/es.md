# InstructPixToPixConditioning

El nodo InstructPixToPixConditioning prepara datos de condicionamiento para la edición de imágenes InstructPix2Pix combinando indicaciones de texto positivas y negativas con datos de imagen. Procesa las imágenes de entrada a través de un codificador VAE para crear representaciones latentes y adjunta estos latentes a los datos de condicionamiento tanto positivos como negativos. El nodo maneja automáticamente las dimensiones de la imagen recortando a múltiplos de 8 píxeles para garantizar la compatibilidad con el proceso de codificación VAE.

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `positivo` | Datos de condicionamiento positivos que contienen indicaciones de texto y configuraciones para las características deseadas de la imagen | CONDITIONING | Sí | - |
| `negativo` | Datos de condicionamiento negativos que contienen indicaciones de texto y configuraciones para las características no deseadas de la imagen | CONDITIONING | Sí | - |
| `vae` | Modelo VAE utilizado para codificar las imágenes de entrada en representaciones latentes | VAE | Sí | - |
| `píxeles` | Imagen de entrada que se procesará y codificará en el espacio latente | IMAGE | Sí | - |

**Nota:** Las dimensiones de la imagen de entrada se ajustan automáticamente mediante un recorte central a múltiplos de 8 píxeles tanto en ancho como en alto para garantizar la compatibilidad con el proceso de codificación VAE.

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `positivo` | Datos de condicionamiento positivos que incluyen la representación latente de la imagen | CONDITIONING |
| `negativo` | Datos de condicionamiento negativos que incluyen la representación latente de la imagen | CONDITIONING |
| `latente` | Tensor latente vacío con las mismas dimensiones que la imagen codificada | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/InstructPixToPixConditioning/es.md)

---
**Source fingerprint (SHA-256):** `e9a5a05cdeafe9337ca2033111f1ad4f7314fa33d71a4764f62919857efc79f4`
