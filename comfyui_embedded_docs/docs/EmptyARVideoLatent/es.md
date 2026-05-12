> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyARVideoLatent/es.md)

## Descripción general

El nodo EmptyARVideoLatent crea una representación latente vacía para la generación de videos. Se utiliza para inicializar un proceso de generación de video proporcionando un tensor de ceros con las dimensiones, relación de aspecto y duración especificadas.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|---------------|-------------|-------|-------------|
| `width` | INT | Sí | 16 a 8192 (paso: 16) | El ancho de los fotogramas del video en píxeles (predeterminado: 832) |
| `height` | INT | Sí | 16 a 8192 (paso: 16) | La altura de los fotogramas del video en píxeles (predeterminado: 480) |
| `length` | INT | Sí | 1 a 1024 (paso: 4) | El número de fotogramas del video (predeterminado: 81) |
| `batch_size` | INT | Sí | 1 a 64 | La cantidad de videos a generar en un solo lote (predeterminado: 1) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|---------------|-------------|
| `LATENT` | LATENT | Un tensor latente lleno de ceros, que representa un espacio latente de video vacío con las dimensiones, duración y tamaño de lote especificados. La forma del tensor es [batch_size, 16, lat_t, height/8, width/8], donde lat_t se calcula a partir de la duración. |