# Empty HunyuanVideo 1.5 Latent

Este nodo crea un tensor latente vacío específicamente formateado para usarse con el modelo HunyuanVideo 1.5. Genera un punto de partida en blanco para la generación de video al asignar un tensor de ceros con el número de canales y las dimensiones espaciales correctos para el espacio latente del modelo.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `ancho` | El ancho del fotograma de video en píxeles. | INT | Sí | - |
| `alto` | La altura del fotograma de video en píxeles. | INT | Sí | - |
| `longitud` | El número de fotogramas en la secuencia de video. | INT | Sí | - |
| `tamaño_lote` | El número de muestras de video a generar en un lote (predeterminado: 1). | INT | No | - |

**Nota:** Las dimensiones espaciales del tensor latente generado se calculan dividiendo el `width` y el `height` de entrada entre 16. La dimensión temporal (fotogramas) se calcula como `((length - 1) // 4) + 1`. Estos cálculos usan división entera, por lo que `width` y `height` deben ser múltiplos de 16 para evitar el truncamiento.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `samples` | Un tensor latente vacío con dimensiones adecuadas para el modelo HunyuanVideo 1.5. El tensor tiene una forma de `[batch_size, 32, frames, height//16, width//16]`. La salida también incluye un valor `downscale_ratio_spacial` de 16. | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyHunyuanVideo15Latent/es.md)

---
**Source fingerprint (SHA-256):** `ce7ec75e8433c778d175a3e2ea260a4397aa5507428908b9a32f50fbe9e184c6`
