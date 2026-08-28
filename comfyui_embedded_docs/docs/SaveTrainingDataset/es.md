# Guardar conjunto de datos de entrenamiento

Este nodo guarda un dataset de entrenamiento codificado en disco para poder cargarlo de forma eficiente durante el entrenamiento. Toma los latentes de imagen y su condicionamiento de texto correspondiente, los divide en archivos más pequeños llamados shards y los almacena en una carpeta dentro del directorio de datasets. También escribe un archivo de metadatos que describe el dataset.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `latents` | Lista de dicts de latentes de MakeTrainingDataset. | LATENT | Sí | N/A |
| `conditioning` | Lista de listas de condicionamiento de MakeTrainingDataset. | CONDITIONING | Sí | N/A |
| `folder_name` | Nombre de la carpeta en la que se guardará el dataset, dentro del directorio de datasets. Se permiten subcarpetas como 'project/run1'. (predeterminado: "training_dataset") | STRING | Sí | N/A |
| `shard_size` | Número de muestras por archivo shard. (predeterminado: 1000) | INT | Sí | 1 a 100000 |

**Nota:** El número de elementos en `latents` debe coincidir exactamente con el número de elementos en `conditioning`; el nodo genera un error si estos recuentos no coinciden. `folder_name` debe ser el nombre de una subcarpeta del directorio de datasets (por ejemplo, `my_dataset`); no puede ser el propio directorio de datasets, y se rechazan los nombres de carpeta que se resuelvan fuera del directorio de datasets.

## Salidas

Este nodo no produce ningún dato de salida. Su función es guardar archivos en su disco. Cada shard se guarda como un archivo `shard_XXXX.pkl` en la carpeta elegida, y un archivo `metadata.json` registra el número total de muestras, el número de shards y el tamaño de shard.

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveTrainingDataset/es.md)

---
**Source fingerprint (SHA-256):** `6d7b63a24ac42907b0f4a1358712cd0ed085982ecd308bce87e5376d9bbc2274`
