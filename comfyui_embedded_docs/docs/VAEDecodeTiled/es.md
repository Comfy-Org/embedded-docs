# VAE Decodificar (Mosaico)

El nodo `VAEDecodeTiled` decodifica representaciones latentes en imágenes mediante un enfoque por teselas para manejar imágenes grandes de manera eficiente. Procesa la entrada en teselas más pequeñas para gestionar el uso de memoria manteniendo la calidad de la imagen. El nodo también admite VAEs de video procesando los fotogramas temporales en bloques con superposición para transiciones suaves.

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `samples` | La representación latente que se decodificará en imágenes | LATENT | Sí | - |
| `vae` | El modelo VAE utilizado para decodificar las muestras latentes | VAE | Sí | - |
| `tile_size` | El tamaño de cada tesela para el procesamiento (predeterminado: 512) | INT | Sí | 64-4096 (paso: 32) |
| `overlap` | La cantidad de superposición entre teselas adyacentes (predeterminado: 64) | INT | Sí | 0-4096 (paso: 32) |
| `temporal_size` | Solo se usa para VAEs de video: cantidad de fotogramas a decodificar a la vez (predeterminado: 64) | INT | Sí | 8-4096 (paso: 4) |
| `temporal_overlap` | Solo se usa para VAEs de video: cantidad de fotogramas a superponer (predeterminado: 8) | INT | Sí | 4-4096 (paso: 4) |

**Nota:** El nodo ajusta automáticamente los valores de superposición si exceden los límites prácticos. Si `tile_size` es menor que 4 veces el `overlap`, la superposición se reduce a una cuarta parte del tamaño de la tesela. De manera similar, si `temporal_size` es menor que el doble de `temporal_overlap`, la superposición temporal se reduce a la mitad. El nodo también tiene en cuenta las relaciones de compresión internas del VAE al calcular los tamaños de tesela y superposición tanto para las dimensiones espaciales como temporales. Para VAEs sin compresión temporal (VAEs que no son de video), se ignoran los parámetros `temporal_size` y `temporal_overlap`.

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `IMAGE` | La imagen o imágenes decodificadas generadas a partir de la representación latente. Al decodificar latentes de video, todos los fotogramas decodificados se combinan en una única lista de imágenes. | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEDecodeTiled/es.md)

---
**Source fingerprint (SHA-256):** `04136ba1abd0c74e780dc405f916a08b809630ae4f41c183049535488b40fd96`
