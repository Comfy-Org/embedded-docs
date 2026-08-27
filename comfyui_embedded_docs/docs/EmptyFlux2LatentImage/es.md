# Empty Flux 2 Latent

El nodo Empty Flux 2 Latent crea una representación latente en blanco y vacía. Genera un tensor rellenado con ceros, que sirve como punto de partida para el proceso de eliminación de ruido (denoising) del modelo Flux. Las dimensiones del latente están determinadas por el ancho y alto de entrada, reducidos por un factor de 16.

## Entradas

| Parámetro | Descripción | Tipo de dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `ancho` | El ancho de la imagen final a generar. El ancho del latente será este valor dividido entre 16. El valor predeterminado es 1024. | INT | Sí | 16 a 8192 |
| `alto` | El alto de la imagen final a generar. El alto del latente será este valor dividido entre 16. El valor predeterminado es 1024. | INT | Sí | 16 a 8192 |
| `tamaño_lote` | El número de muestras latentes a generar en un solo lote. El valor predeterminado es 1. | INT | No | 1 a 4096 |

**Nota:** Las entradas `width` y `height` deben ser divisibles entre 16, ya que el nodo las divide internamente por este factor para crear las dimensiones latentes.

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `samples` | Un tensor latente rellenado con ceros. La forma es `[batch_size, 128, height // 16, width // 16]`. | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyFlux2LatentImage/es.md)

---
**Source fingerprint (SHA-256):** `f8356568f0ab521a3f246d1f672492e74f9a2f449694961b913bd14a5f0f3878`
