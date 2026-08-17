# Guardar conjunto de datos de entrenamiento

Este nodo guarda un dataset de entrenamiento preparado en el disco duro de su computadora. Toma datos codificados, que incluyen los latentes de imagen y su condicionamiento de texto correspondiente, y los organiza en múltiples archivos más pequeños llamados shards para facilitar su gestión. El nodo crea automáticamente una carpeta en el directorio de datasets y guarda tanto los archivos de datos shard como un archivo de metadatos que describe el dataset.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `latents` | Lista de diccionarios de latentes procedentes de MakeTrainingDataset. | LATENT | Sí | N/A |
| `conditioning` | Lista de listas de condicionamiento procedentes de MakeTrainingDataset. | CONDITIONING | Sí | N/A |
| `folder_name` | Nombre de la carpeta donde se guardará el dataset, dentro del directorio de datasets. Se permiten subcarpetas como 'project/run1'. (por defecto: "training_dataset") | STRING | Sí | N/A |
| `shard_size` | Número de muestras por archivo shard. (por defecto: 1000) | INT | Sí | 1 a 100000 |

**Nota:** El número de elementos en la lista `latents` debe coincidir exactamente con el número de elementos en la lista `conditioning`. El nodo genera un error si estas cantidades no coinciden. El `folder_name` debe designar una subcarpeta del directorio de datasets: no se permite usar la carpeta raíz de datasets ni ninguna ruta que escape de él (como '..' o una ruta absoluta).

## Salidas

Este nodo no produce ningún dato de salida. Guarda el dataset como archivos shard numerados (por ejemplo `shard_0000.pkl`) y un archivo `metadata.json` dentro de la carpeta elegida en el directorio de datasets.

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveTrainingDataset/es.md)

---
**Source fingerprint (SHA-256):** `6d7b63a24ac42907b0f4a1358712cd0ed085982ecd308bce87e5376d9bbc2274`
