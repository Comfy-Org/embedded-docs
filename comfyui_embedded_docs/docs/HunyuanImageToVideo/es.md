> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanImageToVideo/es.md)

El nodo HunyuanImageToVideo convierte imágenes en representaciones latentes de video utilizando el modelo de video Hunyuan. Toma entradas de condicionamiento e imágenes iniciales opcionales para generar latentes de video que pueden ser procesados posteriormente por modelos de generación de video. El nodo admite diferentes tipos de guía para controlar cómo la imagen inicial influye en el proceso de generación de video.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `positivo` | CONDITIONING | Sí | - | Entrada de condicionamiento positivo para guiar la generación del video |
| `vae` | VAE | Sí | - | Modelo VAE utilizado para codificar imágenes en el espacio latente |
| `ancho` | INT | Sí | 16 a MAX_RESOLUTION | Ancho del video de salida en píxeles (por defecto: 848, paso: 16) |
| `altura` | INT | Sí | 16 a MAX_RESOLUTION | Alto del video de salida en píxeles (por defecto: 480, paso: 16) |
| `longitud` | INT | Sí | 1 a MAX_RESOLUTION | Número de fotogramas en el video de salida (por defecto: 53, paso: 4) |
| `tamaño_del_lote` | INT | Sí | 1 a 4096 | Número de videos a generar simultáneamente (por defecto: 1) |
| `tipo_de_orientación` | COMBO | Sí | "v1 (concat)"<br>"v2 (replace)"<br>"custom" | Método para incorporar la imagen inicial en la generación de video |
| `imagen_inicial` | IMAGE | No | - | Imagen inicial opcional para inicializar la generación del video |

**Nota:** Cuando se proporciona `start_image`, el nodo utiliza diferentes métodos de guía según el `guidance_type` seleccionado:
- "v1 (concat)": Concatena el latente de la imagen con el latente del video
- "v2 (replace)": Reemplaza los fotogramas iniciales del video con el latente de la imagen
- "custom": Utiliza la imagen como latente de referencia para la guía

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `latente` | CONDITIONING | Condicionamiento positivo modificado con la guía de imagen aplicada cuando se proporciona start_image |
| `latent` | LATENT | Representación latente de video lista para su posterior procesamiento por modelos de generación de video |