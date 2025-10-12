> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyLTXVLatentVideo/es.md)

El nodo EmptyLTXVLatentVideo crea un tensor latente vacío para procesamiento de video. Genera un punto de partida en blanco con dimensiones específicas que puede utilizarse como entrada para flujos de trabajo de generación de video. El nodo produce una representación latente llena de ceros con el ancho, alto, longitud y tamaño de lote configurados.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `ancho` | INT | Sí | 64 a MAX_RESOLUTION | El ancho del tensor latente de video (valor por defecto: 768, paso: 32) |
| `altura` | INT | Sí | 64 a MAX_RESOLUTION | El alto del tensor latente de video (valor por defecto: 512, paso: 32) |
| `longitud` | INT | Sí | 1 a MAX_RESOLUTION | El número de fotogramas en el video latente (valor por defecto: 97, paso: 8) |
| `tamaño_del_lote` | INT | No | 1 a 4096 | El número de videos latentes a generar en un lote (valor por defecto: 1) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `samples` | LATENT | El tensor latente vacío generado con valores cero en las dimensiones especificadas |
