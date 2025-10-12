> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan22FunControlToVideo/es.md)

El nodo Wan22FunControlToVideo prepara los acondicionamientos y representaciones latentes para la generación de video utilizando la arquitectura del modelo Wan. Procesa entradas de acondicionamiento positivo y negativo junto con imágenes de referencia y videos de control opcionales para crear las representaciones necesarias en el espacio latente para la síntesis de video. El nodo maneja el escalado espacial y las dimensiones temporales para generar datos de acondicionamiento apropiados para modelos de video.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | Sí | - | Acondicionamiento positivo para guiar la generación del video |
| `negative` | CONDITIONING | Sí | - | Acondicionamiento negativo para guiar la generación del video |
| `vae` | VAE | Sí | - | Modelo VAE utilizado para codificar imágenes al espacio latente |
| `width` | INT | No | 16 a MAX_RESOLUTION | Ancho del video de salida en píxeles (valor por defecto: 832, paso: 16) |
| `height` | INT | No | 16 a MAX_RESOLUTION | Alto del video de salida en píxeles (valor por defecto: 480, paso: 16) |
| `length` | INT | No | 1 a MAX_RESOLUTION | Número de fotogramas en la secuencia de video (valor por defecto: 81, paso: 4) |
| `batch_size` | INT | No | 1 a 4096 | Número de secuencias de video a generar (valor por defecto: 1) |
| `ref_image` | IMAGE | No | - | Imagen de referencia opcional para proporcionar guía visual |
| `control_video` | IMAGE | No | - | Video de control opcional para guiar el proceso de generación |

**Nota:** El parámetro `length` se procesa en fragmentos de 4 fotogramas, y el nodo maneja automáticamente el escalado temporal para el espacio latente. Cuando se proporciona `ref_image`, influye en el acondicionamiento a través de latentes de referencia. Cuando se proporciona `control_video`, afecta directamente a la representación latente de concatenación utilizada en el acondicionamiento.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | Acondicionamiento positivo modificado con datos latentes específicos para video |
| `negative` | CONDITIONING | Acondicionamiento negativo modificado con datos latentes específicos para video |
| `latent` | LATENT | Tensor latente vacío con dimensiones apropiadas para la generación de video |
