# VAE Decodificar (Mosaico)

El nodo VAEDecodeTiled decodifica representaciones latentes en imágenes mediante un enfoque por teselas para manejar imágenes grandes de manera eficiente. Procesa la entrada en teselas más pequeñas para gestionar el uso de memoria mientras mantiene la calidad de imagen. El nodo también admite VAEs de video procesando los fotogramas temporales en bloques con superposición para transiciones suaves.

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `muestras` | La representación latente que se decodificará en imágenes | LATENT | Sí | - |
| `vae` | El modelo VAE utilizado para decodificar las muestras latentes | VAE | Sí | - |
| `tamaño_mosaico` | El tamaño de cada tesela para el procesamiento (por defecto: 512) | INT | Sí | 64-4096 (step: 32) |
| `superposición` | La cantidad de superposición entre teselas adyacentes (por defecto: 64) | INT | Sí | 0-4096 (step: 32) |
| `tamaño_temporal` | Solo se usa para VAE de video: cantidad de fotogramas a decodificar a la vez (por defecto: 64) | INT | Sí | 8-4096 (step: 4) |
| `superposición_temporal` | Solo se usa para VAE de video: cantidad de fotogramas a superponer (por defecto: 8) | INT | Sí | 4-4096 (step: 4) |

**Nota:** El nodo ajusta automáticamente los valores de superposición si exceden los límites prácticos. Si `tile_size` es menor que 4 veces el `overlap`, la superposición se reduce a una cuarta parte del tamaño de la tesela. De manera similar, si `temporal_size` es menor que el doble de `temporal_overlap`, la superposición temporal se reduce a la mitad. El nodo también tiene en cuenta las relaciones de compresión internas del VAE al calcular los tamaños de tesela y superposición tanto para las dimensiones espaciales como temporales. Si la entrada latente es un lote anidado de latentes, solo se decodifica el primer elemento del lote.

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `IMAGE` | La imagen o imágenes decodificadas generadas a partir de la representación latente. Al decodificar latentes de video, la salida es una secuencia de fotogramas de imagen. | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEDecodeTiled/es.md)

---
**Source fingerprint (SHA-256):** `04136ba1abd0c74e780dc405f916a08b809630ae4f41c183049535488b40fd96`
