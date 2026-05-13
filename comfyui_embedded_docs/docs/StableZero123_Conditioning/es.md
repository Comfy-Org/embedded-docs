> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableZero123_Conditioning/es.md)

El nodo StableZero123_Conditioning procesa una imagen de entrada y ángulos de cámara para generar datos de condicionamiento y representaciones latentes para la generación de modelos 3D. Utiliza un modelo de visión CLIP para codificar las características de la imagen, las combina con información de incrustación de cámara basada en ángulos de elevación y azimut, y produce condicionamiento positivo y negativo junto con una representación latente para tareas posteriores de generación 3D.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|---------------|-------------|-------|-------------|
| `visión_clip` | CLIP_VISION | Sí | - | El modelo de visión CLIP utilizado para codificar las características de la imagen |
| `imagen_inicial` | IMAGE | Sí | - | La imagen de entrada a procesar y codificar |
| `vae` | VAE | Sí | - | El modelo VAE utilizado para codificar píxeles al espacio latente |
| `ancho` | INT | Sí | 16 a MAX_RESOLUTION | Ancho de salida para la representación latente (predeterminado: 256, debe ser divisible por 8) |
| `altura` | INT | Sí | 16 a MAX_RESOLUTION | Alto de salida para la representación latente (predeterminado: 256, debe ser divisible por 8) |
| `tamaño_del_lote` | INT | Sí | 1 a 4096 | Número de muestras a generar en el lote (predeterminado: 1) |
| `elevación` | FLOAT | Sí | -180.0 a 180.0 | Ángulo de elevación de la cámara en grados (predeterminado: 0.0) |
| `acimut` | FLOAT | Sí | -180.0 a 180.0 | Ángulo de azimut de la cámara en grados (predeterminado: 0.0) |

**Nota:** Los parámetros `width` y `height` deben ser divisibles por 8, ya que el nodo los divide automáticamente entre 8 para crear las dimensiones de la representación latente.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|---------------|-------------|
| `negativo` | CONDITIONING | Datos de condicionamiento positivo que combinan características de imagen e incrustaciones de cámara |
| `latente` | CONDITIONING | Datos de condicionamiento negativo con características inicializadas en cero |
| `latent` | LATENT | Representación latente con dimensiones [batch_size, 4, height//8, width//8] |

---
**Source fingerprint (SHA-256):** `a9d6619c800119c9a619665f322d49ded1478ceb40df56ca5707b31242cb0e47`
