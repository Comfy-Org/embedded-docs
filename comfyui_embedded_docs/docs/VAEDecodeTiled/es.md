> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEDecodeTiled/es.md)

El nodo VAEDecodeTiled decodifica representaciones latentes en imágenes utilizando un enfoque en mosaicos para manejar imágenes grandes de manera eficiente. Procesa la entrada en mosaicos más pequeños para gestionar el uso de memoria manteniendo la calidad de la imagen. El nodo también admite VAEs de video procesando fotogramas temporales en fragmentos con superposición para transiciones suaves.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `muestras` | LATENT | Sí | - | La representación latente que se decodificará en imágenes |
| `vae` | VAE | Sí | - | El modelo VAE utilizado para decodificar las muestras latentes |
| `tamaño_mosaico` | INT | Sí | 64-4096 (paso: 32) | El tamaño de cada mosaico para el procesamiento (predeterminado: 512) |
| `superposición` | INT | Sí | 0-4096 (paso: 32) | La cantidad de superposición entre mosaicos adyacentes (predeterminado: 64) |
| `tamaño_temporal` | INT | Sí | 8-4096 (paso: 4) | Solo para VAEs de video: Cantidad de fotogramas a decodificar a la vez (predeterminado: 64) |
| `superposición_temporal` | INT | Sí | 4-4096 (paso: 4) | Solo para VAEs de video: Cantidad de fotogramas a superponer (predeterminado: 8) |

**Nota:** El nodo ajusta automáticamente los valores de superposición si exceden los límites prácticos. Si `tile_size` es menor a 4 veces el `overlap`, la superposición se reduce a un cuarto del tamaño del mosaico. De manera similar, si `temporal_size` es menor al doble del `temporal_overlap`, la superposición temporal se reduce a la mitad.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `IMAGE` | IMAGE | La imagen o imágenes decodificadas generadas a partir de la representación latente |
