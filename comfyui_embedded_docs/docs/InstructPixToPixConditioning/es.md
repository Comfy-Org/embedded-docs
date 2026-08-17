# InstructPixToPixConditioning

El nodo `InstructPixToPixConditioning` prepara los datos de condicionamiento para la edición de imágenes InstructPix2Pix combinando una imagen de entrada con el condicionamiento de prompts de texto positivo y negativo. Codifica la imagen con el VAE en una representación latente, adjunta ese latente a ambos conjuntos de condicionamiento y crea un latente lleno de ceros con dimensiones coincidentes. Si el ancho o el alto de la imagen no es un múltiplo de 8 píxeles, la imagen se recorta automáticamente antes de la codificación.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `positive` | Datos de condicionamiento positivo que contienen prompts de texto y ajustes para las características deseadas de la imagen. | CONDITIONING | Sí | - |
| `negative` | Datos de condicionamiento negativo que contienen prompts de texto y ajustes para las características no deseadas de la imagen. | CONDITIONING | Sí | - |
| `vae` | Modelo VAE utilizado para codificar la imagen de entrada en una representación latente. | VAE | Sí | - |
| `pixels` | Imagen de entrada que se procesa y codifica en el espacio latente. | IMAGE | Sí | - |

**Nota:** La imagen de entrada se recorta automáticamente a un múltiplo de 8 píxeles tanto en ancho como en alto, redondeando hacia abajo, para garantizar la compatibilidad con el proceso de codificación del VAE.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `positive` | Datos de condicionamiento positivo con el latente de la imagen codificada adjunto. | CONDITIONING |
| `negative` | Datos de condicionamiento negativo con el latente de la imagen codificada adjunto. | CONDITIONING |
| `latent` | Tensor latente lleno de ceros con las mismas dimensiones que la imagen codificada. | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/InstructPixToPixConditioning/es.md)

---
**Source fingerprint (SHA-256):** `e9a5a05cdeafe9337ca2033111f1ad4f7314fa33d71a4764f62919857efc79f4`
