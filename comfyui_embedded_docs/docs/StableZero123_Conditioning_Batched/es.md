> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableZero123_Conditioning_Batched/es.md)

El nodo StableZero123_Conditioning_Batched procesa una imagen de entrada y genera datos de acondicionamiento para la generación de modelos 3D. Codifica la imagen utilizando modelos CLIP vision y VAE, luego crea incrustaciones de cámara basadas en ángulos de elevación y azimut para producir acondicionamiento positivo y negativo junto con representaciones latentes para procesamiento por lotes.

## Entradas

| Parámetro | Tipo de Datos | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `clip_vision` | CLIP_VISION | Sí | - | El modelo CLIP vision utilizado para codificar la imagen de entrada |
| `init_image` | IMAGE | Sí | - | La imagen inicial de entrada que se procesará y codificará |
| `vae` | VAE | Sí | - | El modelo VAE utilizado para codificar píxeles de imagen en el espacio latente |
| `width` | INT | No | 16 a MAX_RESOLUTION | El ancho de salida para la imagen procesada (por defecto: 256, debe ser divisible por 8) |
| `height` | INT | No | 16 a MAX_RESOLUTION | La altura de salida para la imagen procesada (por defecto: 256, debe ser divisible por 8) |
| `batch_size` | INT | No | 1 a 4096 | El número de muestras de acondicionamiento a generar en el lote (por defecto: 1) |
| `elevation` | FLOAT | No | -180.0 a 180.0 | El ángulo inicial de elevación de la cámara en grados (por defecto: 0.0) |
| `azimuth` | FLOAT | No | -180.0 a 180.0 | El ángulo inicial de azimut de la cámara en grados (por defecto: 0.0) |
| `elevation_batch_increment` | FLOAT | No | -180.0 a 180.0 | La cantidad a incrementar la elevación para cada elemento del lote (por defecto: 0.0) |
| `azimuth_batch_increment` | FLOAT | No | -180.0 a 180.0 | La cantidad a incrementar el azimut para cada elemento del lote (por defecto: 0.0) |

**Nota:** Los parámetros `width` y `height` deben ser divisibles por 8, ya que el nodo divide internamente estas dimensiones por 8 para la generación del espacio latente.

## Salidas

| Nombre de Salida | Tipo de Datos | Descripción |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | Los datos de acondicionamiento positivo que contienen incrustaciones de imagen y parámetros de cámara |
| `negative` | CONDITIONING | Los datos de acondicionamiento negativo con incrustaciones inicializadas a cero |
| `latent` | LATENT | La representación latente de la imagen procesada con información de indexación por lotes |