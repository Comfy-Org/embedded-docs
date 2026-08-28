# Cargar conjunto de datos de entrenamiento

Este nodo carga un dataset de entrenamiento codificado (latentes y condicionamiento) que se guardó previamente en disco. Lee todos los archivos de fragmentos de datos de una carpeta de dataset seleccionada en el directorio de datasets y devuelve los vectores latentes combinados y los datos de condicionamiento para su uso en flujos de trabajo de entrenamiento.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `folder_name` | Dataset guardado para cargar, desde el directorio de datasets. | COMBO | Sí | Una opción por carpeta de dataset encontrada en el directorio de datasets |

Nota: Las opciones de `folder_name` se construyen automáticamente escaneando el directorio de datasets. Una subcarpeta se lista como dataset cuando contiene un archivo `metadata.json` o al menos un archivo `.safetensors`. La carpeta de dataset seleccionada se busca en todos los directorios raíz de datasets configurados. El nodo lee todos los archivos llamados `shard_*.pkl` en la carpeta seleccionada y genera un error si no se encuentran archivos de fragmentos.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `latents` | Lista de diccionarios de latentes, donde cada diccionario contiene una clave `"samples"` con un tensor. | LATENT |
| `conditioning` | Lista de listas de condicionamiento, donde cada lista interna contiene datos de condicionamiento para la muestra correspondiente. | CONDITIONING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadTrainingDataset/es.md)

---
**Source fingerprint (SHA-256):** `9f914b27f067460f6f3b54f3f2a7bb793c65b99c85e8aa14ab64894be26bd816`
