El nodo VAEDecodeTiled decodifica representaciones latentes en imágenes utilizando un enfoque por mosaicos para manejar imágenes grandes de manera eficiente. Procesa la entrada en mosaicos más pequeños para gestionar el uso de memoria mientras mantiene la calidad de la imagen. El nodo también admite VAEs de video procesando fotogramas temporales en fragmentos con superposición para transiciones suaves.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `muestras` | La representación latente que se decodificará en imágenes | LATENT | Sí | - |
| `vae` | El modelo VAE utilizado para decodificar las muestras latentes | VAE | Sí | - |
| `tamaño_mosaico` | El tamaño de cada mosaico para el procesamiento (predeterminado: 512) | INT | Sí | 64-4096 (paso: 32) |
| `superposición` | La cantidad de superposición entre mosaicos adyacentes (predeterminado: 64) | INT | Sí | 0-4096 (paso: 32) |
| `tamaño_temporal` | Solo se usa para VAEs de video: Cantidad de fotogramas a decodificar a la vez (predeterminado: 64) | INT | Sí | 8-4096 (paso: 4) |
| `superposición_temporal` | Solo se usa para VAEs de video: Cantidad de fotogramas a superponer (predeterminado: 8) | INT | Sí | 4-4096 (paso: 4) |

**Nota:** El nodo ajusta automáticamente los valores de superposición si exceden los límites prácticos. Si `tile_size` es menor que 4 veces la `overlap`, la superposición se reduce a un cuarto del tamaño del mosaico. De manera similar, si `temporal_size` es menor que el doble de `temporal_overlap`, la superposición temporal se reduce a la mitad. El nodo también tiene en cuenta las relaciones de compresión internas del VAE al calcular los tamaños de mosaico y superposición tanto para las dimensiones espaciales como temporales.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `IMAGE` | La imagen o imágenes decodificadas generadas a partir de la representación latente | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEDecodeTiled/es.md)

---
**Source fingerprint (SHA-256):** `193d5cb219d66855ae581d3e4488b7b6ae3a45b735fb0f9f784fea1f5d466e46`
