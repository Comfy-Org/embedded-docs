> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_EmptyLatentImage/es.md)

El nodo StableCascade_EmptyLatentImage crea tensores latentes vacíos para modelos Stable Cascade. Genera dos representaciones latentes separadas - una para la etapa C y otra para la etapa B - con dimensiones apropiadas basadas en la resolución de entrada y configuraciones de compresión. Este nodo proporciona el punto de partida para el pipeline de generación de Stable Cascade.

## Entradas

| Parámetro | Tipo de Datos | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `ancho` | INT | Sí | 256 a MAX_RESOLUTION | El ancho de la imagen de salida en píxeles (por defecto: 1024, paso: 8) |
| `altura` | INT | Sí | 256 a MAX_RESOLUTION | La altura de la imagen de salida en píxeles (por defecto: 1024, paso: 8) |
| `compresión` | INT | Sí | 4 a 128 | El factor de compresión que determina las dimensiones latentes para la etapa C (por defecto: 42, paso: 1) |
| `tamaño_del_lote` | INT | No | 1 a 4096 | El número de muestras latentes a generar en un lote (por defecto: 1) |

## Salidas

| Nombre de Salida | Tipo de Datos | Descripción |
|-------------|-----------|-------------|
| `etapa_b` | LATENT | El tensor latente de etapa C con dimensiones [batch_size, 16, height//compression, width//compression] |
| `stage_b` | LATENT | El tensor latente de etapa B con dimensiones [batch_size, 4, height//4, width//4] |
