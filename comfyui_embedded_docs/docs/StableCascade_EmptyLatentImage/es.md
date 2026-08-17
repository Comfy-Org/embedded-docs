# StableCascade_EmptyLatentImage

El nodo StableCascade_EmptyLatentImage crea tensores latentes vacíos para los modelos Stable Cascade. Genera dos representaciones latentes separadas: una para la etapa C y otra para la etapa B, con dimensiones apropiadas según la resolución de entrada y la configuración de compresión. Este nodo proporciona el punto de partida para el flujo de generación de Stable Cascade.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `width` | El ancho de la imagen de salida en píxeles (predeterminado: 1024, paso: 8) | INT | Sí | 256 to MAX_RESOLUTION |
| `height` | La altura de la imagen de salida en píxeles (predeterminado: 1024, paso: 8) | INT | Sí | 256 to MAX_RESOLUTION |
| `compression` | El factor de compresión que determina las dimensiones latentes para la etapa C (predeterminado: 42, paso: 1). Este es un parámetro avanzado. | INT | Sí | 4 to 128 |
| `batch_size` | El número de muestras latentes a generar en un lote (predeterminado: 1) | INT | No | 1 to 4096 |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `stage_c` | El tensor latente de la etapa C con dimensiones [batch_size, 16, height//compression, width//compression] | LATENT |
| `stage_b` | El tensor latente de la etapa B con dimensiones [batch_size, 4, height//4, width//4] | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_EmptyLatentImage/es.md)

---
**Source fingerprint (SHA-256):** `f336f87d0ec14b3716efda2cfaa194b1f80707d64821bb56ade7d88d9bd5b53f`
