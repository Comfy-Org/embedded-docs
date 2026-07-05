# StableZero123_Conditioning_Batched

El nodo `StableZero123_Conditioning_Batched` procesa una imagen de entrada y genera datos de condicionamiento para la generación de modelos 3D. Codifica la imagen utilizando modelos CLIP vision y VAE, luego crea incrustaciones de cámara basadas en ángulos de elevación y azimut para producir condicionamiento positivo y negativo, junto con representaciones latentes para procesamiento por lotes.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `clip_vision` | El modelo de visión CLIP utilizado para codificar la imagen de entrada | CLIP_VISION | Sí | - |
| `imagen_inicial` | La imagen de entrada inicial a procesar y codificar | IMAGE | Sí | - |
| `vae` | El modelo VAE utilizado para codificar píxeles de imagen en espacio latente | VAE | Sí | - |
| `ancho` | El ancho de salida para la imagen procesada (predeterminado: 256, debe ser divisible por 8) | INT | No | 16 a MAX_RESOLUTION |
| `altura` | La altura de salida para la imagen procesada (predeterminado: 256, debe ser divisible por 8) | INT | No | 16 a MAX_RESOLUTION |
| `tamaño_del_lote` | El número de muestras de condicionamiento a generar en el lote (predeterminado: 1) | INT | No | 1 a 4096 |
| `elevación` | El ángulo inicial de elevación de la cámara en grados (predeterminado: 0.0) | FLOAT | No | -180.0 a 180.0 |
| `acimut` | El ángulo inicial de azimut de la cámara en grados (predeterminado: 0.0) | FLOAT | No | -180.0 a 180.0 |
| `incremento_de_lote_de_elevación` | El incremento de elevación para cada elemento del lote (predeterminado: 0.0) | FLOAT | No | -180.0 a 180.0 |
| `incremento_de_lote_de_acimut` | El incremento de azimut para cada elemento del lote (predeterminado: 0.0) | FLOAT | No | -180.0 a 180.0 |

**Nota:** Los parámetros `width` y `height` deben ser divisibles por 8, ya que el nodo divide internamente estas dimensiones entre 8 para la generación del espacio latente.


| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `positive` | Los datos de condicionamiento positivo que contienen incrustaciones de imagen y parámetros de cámara | CONDITIONING |
| `negative` | Los datos de condicionamiento negativo con incrustaciones inicializadas en cero | CONDITIONING |
| `latent` | La representación latente de la imagen procesada con información de indexación por lotes | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableZero123_Conditioning_Batched/es.md)

---
**Source fingerprint (SHA-256):** `2b770f7a168a0d3e33da8bfa63383080709fa5d53846dbf6a4374bd1ef1746aa`
