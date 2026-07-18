El nodo HunyuanImageToVideo convierte imágenes en representaciones latentes de video utilizando el modelo de video Hunyuan. Toma entradas de condicionamiento e imágenes de inicio opcionales para generar latentes de video que pueden ser procesados posteriormente por modelos de generación de video. El nodo admite diferentes tipos de guía para controlar cómo la imagen de inicio influye en el proceso de generación de video.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `positivo` | Entrada de condicionamiento positivo para guiar la generación de video | CONDITIONING | Sí | - |
| `vae` | Modelo VAE utilizado para codificar imágenes en el espacio latente | VAE | Sí | - |
| `ancho` | Ancho del video de salida en píxeles (predeterminado: 848, paso: 16) | INT | Sí | 16 a MAX_RESOLUTION |
| `altura` | Alto del video de salida en píxeles (predeterminado: 480, paso: 16) | INT | Sí | 16 a MAX_RESOLUTION |
| `longitud` | Número de fotogramas en el video de salida (predeterminado: 53, paso: 4) | INT | Sí | 1 a MAX_RESOLUTION |
| `tamaño_del_lote` | Cantidad de videos a generar simultáneamente (predeterminado: 1) | INT | Sí | 1 a 4096 |
| `tipo_de_orientación` | Método para incorporar la imagen de inicio en la generación de video (predeterminado: "v1 (concat)") | COMBO | Sí | "v1 (concat)"<br>"v2 (replace)"<br>"custom" |
| `imagen_inicial` | Imagen de inicio opcional para inicializar la generación de video | IMAGE | No | - |

**Nota:** Cuando se proporciona `start_image`, el nodo utiliza diferentes métodos de guía según el `guidance_type` seleccionado:

- "v1 (concat)": Concatena el latente de la imagen con el latente del video y aplica una máscara para fusionar la imagen en el video
- "v2 (replace)": Reemplaza los fotogramas iniciales del video con el latente de la imagen y aplica una máscara de ruido
- "custom": Utiliza la imagen como un latente de referencia para la guía

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `positivo` | Condicionamiento positivo modificado con guía de imagen aplicada cuando se proporciona start_image | CONDITIONING |
| `latente` | Representación latente de video lista para su posterior procesamiento por modelos de generación de video | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanImageToVideo/es.md)

---
**Source fingerprint (SHA-256):** `e55e935b7955b28b04014359c544a230c51ee91e21170be1ae4f50705d3e7bba`
