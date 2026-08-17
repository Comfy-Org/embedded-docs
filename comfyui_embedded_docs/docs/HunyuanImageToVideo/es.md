# HunyuanImageToVideo

El nodo HunyuanImageToVideo convierte imágenes en representaciones latentes de video utilizando el modelo de video Hunyuan. Acepta entradas de condicionamiento e imágenes iniciales opcionales para generar latentes de video que pueden procesarse posteriormente con modelos de generación de video. El nodo admite diferentes tipos de guía para controlar cómo la imagen inicial influye en el proceso de generación de video.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `positive` | Entrada de condicionamiento positivo para guiar la generación de video | CONDITIONING | Sí | - |
| `vae` | Modelo VAE utilizado para codificar imágenes en el espacio latente | VAE | Sí | - |
| `width` | Ancho del video de salida en píxeles (predeterminado: 848, paso: 16) | INT | Sí | 16 a MAX_RESOLUTION |
| `height` | Alto del video de salida en píxeles (predeterminado: 480, paso: 16) | INT | Sí | 16 a MAX_RESOLUTION |
| `length` | Número de fotogramas en el video de salida (predeterminado: 53, paso: 4) | INT | Sí | 1 a MAX_RESOLUTION |
| `batch_size` | Número de videos a generar simultáneamente (predeterminado: 1) | INT | Sí | 1 a 4096 |
| `guidance_type` | Método para incorporar la imagen inicial en la generación de video (predeterminado: "v1 (concat)") | COMBO | Sí | "v1 (concat)"<br>"v2 (replace)"<br>"custom" |
| `start_image` | Imagen inicial opcional para iniciar la generación de video | IMAGE | No | - |

**Nota:** Cuando se proporciona `start_image`, el nodo utiliza diferentes métodos de guía según el `guidance_type` seleccionado:

- "v1 (concat)": Concatena el latente de la imagen con el latente de video y aplica una máscara para fusionar la imagen en el video
- "v2 (replace)": Reemplaza los fotogramas iniciales del video con el latente de la imagen y aplica una máscara de ruido
- "custom": Utiliza la imagen como latente de referencia para la guía

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `positive` | Condicionamiento positivo modificado con la guía de imagen aplicada cuando se proporciona `start_image` | CONDITIONING |
| `latent` | Representación latente de video lista para su posterior procesamiento por modelos de generación de video | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanImageToVideo/es.md)

---
**Source fingerprint (SHA-256):** `0ed00d59513492f31760a18ce3b0edf10b64cad848ba52c4e47d5f61fae9accc`
