> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptySD3LatentImage/es.md)

El nodo EmptySD3LatentImage crea un tensor de imagen latente en blanco específicamente formateado para modelos Stable Diffusion 3. Genera un tensor lleno de ceros que tiene las dimensiones y estructura correctas esperadas por las canalizaciones de SD3. Esto se utiliza comúnmente como punto de partida para flujos de trabajo de generación de imágenes.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `ancho` | INT | Sí | 16 a MAX_RESOLUTION (paso: 16) | El ancho de la imagen latente de salida en píxeles (por defecto: 1024) |
| `altura` | INT | Sí | 16 a MAX_RESOLUTION (paso: 16) | La altura de la imagen latente de salida en píxeles (por defecto: 1024) |
| `tamaño_del_lote` | INT | Sí | 1 a 4096 | El número de imágenes latentes a generar en un lote (por defecto: 1) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `LATENT` | LATENT | Un tensor latente que contiene muestras en blanco con dimensiones compatibles con SD3 |