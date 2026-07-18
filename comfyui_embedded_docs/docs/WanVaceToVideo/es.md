# WanVaceToVideo

El nodo WanVaceToVideo procesa datos de condicionamiento de video para modelos de generación de video. Toma entradas de condicionamiento positivo y negativo junto con datos de control de video y prepara representaciones latentes para la generación de video. El nodo maneja el escalado de video, el enmascaramiento y la codificación VAE para crear la estructura de condicionamiento adecuada para modelos de video.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `positivo` | Entrada de condicionamiento positivo para guiar la generación | CONDITIONING | Sí | - |
| `negativo` | Entrada de condicionamiento negativo para guiar la generación | CONDITIONING | Sí | - |
| `vae` | Modelo VAE utilizado para codificar imágenes y fotogramas de video | VAE | Sí | - |
| `ancho` | Ancho del video de salida en píxeles (predeterminado: 832, paso: 16) | INT | Sí | 16 a MAX_RESOLUTION |
| `alto` | Alto del video de salida en píxeles (predeterminado: 480, paso: 16) | INT | Sí | 16 a MAX_RESOLUTION |
| `longitud` | Número de fotogramas en el video (predeterminado: 81, paso: 4) | INT | Sí | 1 a MAX_RESOLUTION |
| `tamaño_lote` | Número de videos a generar simultáneamente (predeterminado: 1) | INT | Sí | 1 a 4096 |
| `fuerza` | Intensidad de condición para el control VACE (predeterminado: 1.0, paso: 0.01). Esto no es una intensidad de LoRA. Los pesos de LoRA se aplican a través de nodos LoRA separados. | FLOAT | Sí | 0.0 a 1000.0 |
| `control_video` | Video de entrada opcional para condicionamiento de control | IMAGE | No | - |
| `máscaras_de_control` | Máscaras opcionales para controlar qué partes del video modificar | MASK | No | - |
| `imagen_de_referencia` | Imagen de referencia opcional para condicionamiento adicional | IMAGE | No | - |

**Nota:** Cuando se proporciona `control_video`, se escalará para que coincida con el ancho y alto especificados. Si se proporcionan `control_masks`, deben coincidir con las dimensiones del video de control. La `reference_image` se codifica a través del VAE y se antepone a la secuencia latente cuando se proporciona.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `negativo` | Condicionamiento positivo con datos de control de video aplicados | CONDITIONING |
| `latente` | Condicionamiento negativo con datos de control de video aplicados | CONDITIONING |
| `latente_recortado` | Tensor latente vacío listo para la generación de video | LATENT |
| `trim_latent` | Número de fotogramas latentes a recortar cuando se utiliza una imagen de referencia | INT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanVaceToVideo/es.md)

---
**Source fingerprint (SHA-256):** `66e50a360dc99ac49cac8f3f1c8649bf4298da2934c1bd9a0bc7cfbec620b291`
