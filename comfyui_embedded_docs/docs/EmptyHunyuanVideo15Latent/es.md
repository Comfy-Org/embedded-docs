# Empty HunyuanVideo 1.5 Latent

Este nodo crea un tensor latente vacío formateado específicamente para su uso con el modelo HunyuanVideo 1.5. Genera un punto de partida en blanco para la generación de video asignando un tensor de ceros con el número correcto de canales y dimensiones espaciales para el espacio latente del modelo.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `ancho` | El ancho del fotograma de video en píxeles. | INT | Sí | - |
| `alto` | La altura del fotograma de video en píxeles. | INT | Sí | - |
| `longitud` | El número de fotogramas en la secuencia de video. | INT | Sí | - |
| `tamaño_lote` | El número de muestras de video a generar en un lote (predeterminado: 1). | INT | No | - |

**Nota:** Las dimensiones espaciales del tensor latente generado se calculan dividiendo el `width` y `height` de entrada entre 16. La dimensión temporal (fotogramas) se calcula como `((length - 1) // 4) + 1`.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `samples` | Un tensor latente vacío con dimensiones adecuadas para el modelo HunyuanVideo 1.5. El tensor tiene una forma de `[batch_size, 32, frames, height//16, width//16]`. La salida también incluye un valor `downscale_ratio_spacial` de 16. | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyHunyuanVideo15Latent/es.md)

---
**Source fingerprint (SHA-256):** `eebc131adfe63f6bc8367f2a96b3ac7f3f3223c5b1fb308eda3ec09c94fff2ee`
