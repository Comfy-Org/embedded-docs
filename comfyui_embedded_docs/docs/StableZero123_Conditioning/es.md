# StableZero123_Conditioning

El nodo StableZero123_Conditioning procesa una imagen de entrada y ángulos de cámara para generar datos de condicionamiento y representaciones latentes para la generación de modelos 3D. Utiliza un modelo de visión CLIP para codificar las características de la imagen, las combina con información de incrustaciones de la cámara basada en los ángulos de elevación y azimut, y produce condicionamientos positivos y negativos junto con una representación latente para tareas posteriores de generación 3D.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `visión_clip` | El modelo de visión CLIP utilizado para codificar las características de la imagen | CLIP_VISION | Sí | - |
| `imagen_inicial` | La imagen de entrada que se procesará y codificará | IMAGE | Sí | - |
| `vae` | El modelo VAE utilizado para codificar píxeles al espacio latente | VAE | Sí | - |
| `ancho` | Ancho de salida para la representación latente (por defecto: 256, debe ser divisible por 8) | INT | Sí | 16 a MAX_RESOLUTION |
| `altura` | Alto de salida para la representación latente (por defecto: 256, debe ser divisible por 8) | INT | Sí | 16 a MAX_RESOLUTION |
| `tamaño_del_lote` | Número de muestras a generar en el lote (por defecto: 1) | INT | Sí | 1 a 4096 |
| `elevación` | Ángulo de elevación de la cámara en grados (por defecto: 0.0) | FLOAT | Sí | -180.0 a 180.0 |
| `acimut` | Ángulo azimutal de la cámara en grados (por defecto: 0.0) | FLOAT | Sí | -180.0 a 180.0 |

**Nota:** Los parámetros `width` y `height` deben ser divisibles por 8, ya que el nodo los divide automáticamente entre 8 para crear las dimensiones de la representación latente.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `positivo` | Datos de condicionamiento positivos que combinan las características de la imagen y las incrustaciones de la cámara, incluida la imagen de entrada codificada por el VAE como un latente para concatenar | CONDITIONING |
| `negativo` | Datos de condicionamiento negativos con características inicializadas a cero y un latente inicializado a cero | CONDITIONING |
| `latente` | Representación latente inicializada a cero con dimensiones [batch_size, 4, height//8, width//8] | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableZero123_Conditioning/es.md)

---
**Source fingerprint (SHA-256):** `a694610c9f22fe0dab3ae02f4aabb33e3de8e5031c82dff5e8ba232c098f4a1d`
