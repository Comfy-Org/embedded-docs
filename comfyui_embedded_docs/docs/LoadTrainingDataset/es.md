# Cargar conjunto de datos de entrenamiento

Esta documentación fue generada por IA. Si encuentras algún error o tienes sugerencias de mejora, ¡no dudes en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadTrainingDataset/en.md)

Este nodo carga un conjunto de datos de entrenamiento codificado que ha sido guardado previamente en disco. Busca y lee todos los archivos de fragmentos de datos de una carpeta especificada dentro del directorio de salida de ComfyUI, luego devuelve los vectores latentes combinados y los datos de condicionamiento para su uso en flujos de trabajo de entrenamiento.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `folder_name` | Nombre de la carpeta que contiene el conjunto de datos guardado, ubicada dentro del directorio de salida de ComfyUI (por defecto: "training_dataset"). | STRING | Sí | N/D |


| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `latents` | Una lista de diccionarios latentes, donde cada diccionario contiene una clave `"samples"` con un tensor. | LATENT |
| `conditioning` | Una lista de listas de condicionamiento, donde cada lista interna contiene datos de condicionamiento para una muestra correspondiente. | CONDITIONING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadTrainingDataset/es.md)

---
**Source fingerprint (SHA-256):** `0a07c97e2c6a32f77cd21ea7dbdd33e06fad82285696b88122fef369307e133d`
