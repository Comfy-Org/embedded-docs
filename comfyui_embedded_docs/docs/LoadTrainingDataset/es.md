# Cargar conjunto de datos de entrenamiento

Este nodo carga un conjunto de datos de entrenamiento codificado (latentes y condicionamiento) desde el disco para usarlo en el entrenamiento. Después de seleccionar una carpeta de conjunto de datos previamente guardada, lee todos los archivos de fragmentos (shards) que contiene y devuelve los vectores latentes combinados y los datos de condicionamiento.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `folder_name` | Conjunto de datos guardado para cargar, desde el directorio de conjuntos de datos. | COMBO | Sí | Se completa dinámicamente con todas las carpetas de conjuntos de datos encontradas en los directorios de conjuntos de datos registrados. Solo se listan las carpetas que contienen un archivo `metadata.json` o archivos `.safetensors`. |

**Nota:** La carpeta de conjunto de datos seleccionada debe ser una subcarpeta de un directorio de conjuntos de datos registrado y debe contener al menos un archivo de fragmento llamado `shard_*.pkl`; de lo contrario, el nodo genera un error.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `latents` | Lista de diccionarios latentes cargados desde los fragmentos del conjunto de datos, cada uno con un tensor `samples`. | LATENT |
| `conditioning` | Lista de listas de condicionamiento cargadas desde los fragmentos del conjunto de datos, una por muestra. | CONDITIONING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadTrainingDataset/es.md)

---
**Source fingerprint (SHA-256):** `9f914b27f067460f6f3b54f3f2a7bb793c65b99c85e8aa14ab64894be26bd816`
