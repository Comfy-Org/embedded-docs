# PhotoMakerLoader

El nodo PhotoMakerLoader carga un modelo PhotoMaker desde los archivos de modelo disponibles. Lee el archivo de modelo especificado y prepara el codificador de identidad PhotoMaker para su uso en tareas de generación de imágenes basadas en identidad. Este nodo está marcado como experimental y está destinado únicamente para fines de prueba.

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `nombre_del_modelo_photomaker` | El nombre del archivo de modelo PhotoMaker a cargar. Las opciones disponibles están determinadas por los archivos de modelo presentes en la carpeta `photomaker`. | STRING | Sí | Múltiples opciones disponibles |

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `photomaker_model` | El modelo PhotoMaker cargado que contiene el codificador de identidad, listo para su uso en operaciones de codificación de identidad. | PHOTOMAKER |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PhotoMakerLoader/es.md)

---
**Source fingerprint (SHA-256):** `4c55abacf8462d8de3d1f2a728d4b09ab1d1c8c6476d25cc4af5089508a721da`
