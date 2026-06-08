El nodo StableZero123_Conditioning procesa una imagen de entrada y ángulos de cámara para generar datos de condicionamiento y representaciones latentes para la generación de modelos 3D. Utiliza un modelo de visión CLIP para codificar las características de la imagen, las combina con información de incrustación de cámara basada en ángulos de elevación y azimut, y produce condicionamiento positivo y negativo junto con una representación latente para tareas posteriores de generación 3D.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `visión_clip` | El modelo de visión CLIP utilizado para codificar las características de la imagen | CLIP_VISION | Sí | - |
| `imagen_inicial` | La imagen de entrada a procesar y codificar | IMAGE | Sí | - |
| `vae` | El modelo VAE utilizado para codificar píxeles al espacio latente | VAE | Sí | - |
| `ancho` | Ancho de salida para la representación latente (predeterminado: 256, debe ser divisible por 8) | INT | Sí | 16 a MAX_RESOLUTION |
| `altura` | Alto de salida para la representación latente (predeterminado: 256, debe ser divisible por 8) | INT | Sí | 16 a MAX_RESOLUTION |
| `tamaño_del_lote` | Número de muestras a generar en el lote (predeterminado: 1) | INT | Sí | 1 a 4096 |
| `elevación` | Ángulo de elevación de la cámara en grados (predeterminado: 0.0) | FLOAT | Sí | -180.0 a 180.0 |
| `acimut` | Ángulo de azimut de la cámara en grados (predeterminado: 0.0) | FLOAT | Sí | -180.0 a 180.0 |

**Nota:** Los parámetros `width` y `height` deben ser divisibles por 8, ya que el nodo los divide automáticamente entre 8 para crear las dimensiones de la representación latente.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `negativo` | Datos de condicionamiento positivo que combinan características de imagen e incrustaciones de cámara | CONDITIONING |
| `latente` | Datos de condicionamiento negativo con características inicializadas en cero | CONDITIONING |
| `latent` | Representación latente con dimensiones [batch_size, 4, height//8, width//8] | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableZero123_Conditioning/es.md)

---
**Source fingerprint (SHA-256):** `a9d6619c800119c9a619665f322d49ded1478ceb40df56ca5707b31242cb0e47`
