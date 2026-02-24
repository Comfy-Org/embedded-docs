> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveTrainingDataset/es.md)

Este nodo guarda un conjunto de datos de entrenamiento preparado en el disco duro de tu computadora. Toma datos codificados, que incluyen latentes de imagen y su condicionamiento de texto correspondiente, y los organiza en múltiples archivos más pequeños llamados fragmentos (shards) para facilitar su gestión. El nodo crea automáticamente una carpeta en tu directorio de salida y guarda tanto los archivos de datos como un archivo de metadatos que describe el conjunto de datos.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `latents` | LATENT | Sí | N/A | Lista de diccionarios de latentes provenientes de MakeTrainingDataset. |
| `conditioning` | CONDITIONING | Sí | N/A | Lista de listas de condicionamiento provenientes de MakeTrainingDataset. |
| `folder_name` | STRING | No | N/A | Nombre de la carpeta donde se guardará el conjunto de datos (dentro del directorio de salida). (por defecto: "training_dataset") |
| `shard_size` | INT | No | 1 a 100000 | Número de muestras por archivo fragmento (shard). (por defecto: 1000) |

**Nota:** El número de elementos en la lista `latents` debe coincidir exactamente con el número de elementos en la lista `conditioning`. El nodo generará un error si estos conteos no coinciden.

## Salidas

Este nodo no produce ningún dato de salida. Su función es guardar archivos en tu disco.
