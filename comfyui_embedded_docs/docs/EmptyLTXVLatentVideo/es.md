# EmptyLTXVLatentVideo

El nodo EmptyLTXVLatentVideo crea un tensor latente vacío para la generación de videos. Produce una representación latente rellena de ceros con el ancho, alto, longitud y tamaño de lote especificados, lista para usarse como punto de partida en flujos de trabajo de video LTXV. El latente almacena el video en una forma comprimida: las dimensiones espaciales se dividen entre 32 y el recuento de fotogramas se reduce por un factor de 8.

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `width` | El ancho del video latente en píxeles (predeterminado: 768, paso: 32) | INT | Sí | 64 to MAX_RESOLUTION |
| `height` | La altura del video latente en píxeles (predeterminado: 512, paso: 32) | INT | Sí | 64 to MAX_RESOLUTION |
| `length` | El número de fotogramas del video latente (predeterminado: 97, paso: 8) | INT | Sí | 1 to MAX_RESOLUTION |
| `batch_size` | El número de videos latentes a generar en un lote (predeterminado: 1) | INT | No | 1 to 4096 |

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `samples` | El tensor latente vacío generado, relleno de ceros. El latente también lleva un valor `downscale_ratio_spacial` de 32, que describe la reducción de escala espacial aplicada al ancho y a la altura. | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyLTXVLatentVideo/es.md)

---
**Source fingerprint (SHA-256):** `0b1e57baf9730d852b03b6bccbb8a033e2be9b9cd2420a0aa3638c31f6d3cd26`
