> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/InstructPixToPixConditioning/es.md)

El nodo InstructPixToPixConditioning prepara datos de condicionamiento para la edición de imágenes InstructPix2Pix combinando prompts de texto positivos y negativos con datos de imagen. Procesa las imágenes de entrada a través de un codificador VAE para crear representaciones latentes y adjunta estos latentes tanto a los datos de condicionamiento positivos como negativos. El nodo maneja automáticamente las dimensiones de la imagen recortando a múltiplos de 8 píxeles para garantizar compatibilidad con el proceso de codificación VAE.

## Entradas

| Parámetro | Tipo de Datos | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `positivo` | CONDITIONING | Sí | - | Datos de condicionamiento positivo que contienen prompts de texto y configuraciones para las características deseadas de la imagen |
| `negativo` | CONDITIONING | Sí | - | Datos de condicionamiento negativo que contienen prompts de texto y configuraciones para las características no deseadas de la imagen |
| `vae` | VAE | Sí | - | Modelo VAE utilizado para codificar las imágenes de entrada en representaciones latentes |
| `píxeles` | IMAGE | Sí | - | Imagen de entrada que será procesada y codificada en el espacio latente |

**Nota:** Las dimensiones de la imagen de entrada se ajustan automáticamente recortando al múltiplo más cercano de 8 píxeles tanto en ancho como en alto para garantizar compatibilidad con el proceso de codificación VAE.

## Salidas

| Nombre de Salida | Tipo de Datos | Descripción |
|-------------|-----------|-------------|
| `negativo` | CONDITIONING | Datos de condicionamiento positivo con representación latente de imagen adjunta |
| `latente` | CONDITIONING | Datos de condicionamiento negativo con representación latente de imagen adjunta |
| `latent` | LATENT | Tensor latente vacío con las mismas dimensiones que la imagen codificada |