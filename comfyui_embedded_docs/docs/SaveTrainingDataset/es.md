# Guardar conjunto de datos de entrenamiento

Este nodo guarda un conjunto de datos de entrenamiento preparado en el disco duro de tu computadora. Toma datos codificados, que incluyen latentes de imagen y su condicionamiento de texto correspondiente, y los organiza en múltiples archivos más pequeños llamados fragmentos para facilitar su gestión. El nodo crea automáticamente una carpeta en tu directorio de salida y guarda tanto los archivos de datos como un archivo de metadatos que describe el conjunto de datos.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `latents` | Lista de diccionarios latentes provenientes de MakeTrainingDataset. | LATENT | Sí | N/A |
| `conditioning` | Lista de listas de condicionamiento provenientes de MakeTrainingDataset. | CONDITIONING | Sí | N/A |
| `folder_name` | Nombre de la carpeta para guardar el conjunto de datos (dentro del directorio de salida). (predeterminado: "training_dataset") | STRING | No | N/A |
| `shard_size` | Número de muestras por archivo de fragmento. (predeterminado: 1000) | INT | No | 1 a 100000 |

**Nota:** La cantidad de elementos en la lista `latents` debe coincidir exactamente con la cantidad de elementos en la lista `conditioning`. El nodo generará un error si estos recuentos no coinciden.

## Salidas

Este nodo no produce ningún dato de salida. Su función es guardar archivos en tu disco.

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveTrainingDataset/es.md)

---
**Source fingerprint (SHA-256):** `1b0108be7362c0cb8ba16ffbf94cf42be2d04159aacbabe1ff0890083d1733b3`
