> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableZero123_Conditioning/es.md)

El nodo StableZero123_Conditioning procesa una imagen de entrada y ángulos de cámara para generar datos de condicionamiento y representaciones latentes para la generación de modelos 3D. Utiliza un modelo de visión CLIP para codificar las características de la imagen, las combina con información de incrustación de cámara basada en ángulos de elevación y azimut, y produce condicionamiento positivo y negativo junto con una representación latente para tareas posteriores de generación 3D.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `clip_vision` | CLIP_VISION | Sí | - | El modelo de visión CLIP utilizado para codificar las características de la imagen |
| `init_image` | IMAGE | Sí | - | La imagen de entrada que será procesada y codificada |
| `vae` | VAE | Sí | - | El modelo VAE utilizado para codificar píxeles al espacio latente |
| `width` | INT | No | 16 a MAX_RESOLUTION | Ancho de salida para la representación latente (por defecto: 256, debe ser divisible por 8) |
| `height` | INT | No | 16 a MAX_RESOLUTION | Altura de salida para la representación latente (por defecto: 256, debe ser divisible por 8) |
| `batch_size` | INT | No | 1 a 4096 | Número de muestras a generar en el lote (por defecto: 1) |
| `elevation` | FLOAT | No | -180.0 a 180.0 | Ángulo de elevación de la cámara en grados (por defecto: 0.0) |
| `azimuth` | FLOAT | No | -180.0 a 180.0 | Ángulo de azimut de la cámara en grados (por defecto: 0.0) |

**Nota:** Los parámetros `width` y `height` deben ser divisibles por 8, ya que el nodo automáticamente los divide por 8 para crear las dimensiones de la representación latente.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | Datos de condicionamiento positivo que combinan características de imagen e incrustaciones de cámara |
| `negative` | CONDITIONING | Datos de condicionamiento negativo con características inicializadas en cero |
| `latent` | LATENT | Representación latente con dimensiones [batch_size, 4, height//8, width//8] |