# PhotoMakerLoader

El nodo PhotoMakerLoader carga un modelo PhotoMaker desde los archivos de modelo disponibles. Lee el archivo de modelo especificado y prepara el codificador de ID de PhotoMaker para usarse en tareas de generación de imágenes basadas en identidad. Este nodo está marcado como experimental y está pensado para fines de prueba.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `nombre_del_modelo_photomaker` | El nombre del archivo de modelo PhotoMaker que se va a cargar. Las opciones disponibles están determinadas por los archivos de modelo presentes en la carpeta `photomaker`. | COMBO | Sí | Múltiples opciones disponibles (se completan dinámicamente desde la carpeta `photomaker`) |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `photomaker_model` | El modelo PhotoMaker cargado que contiene el codificador de ID, listo para usarse en operaciones de codificación de identidad. | PHOTOMAKER |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PhotoMakerLoader/es.md)

---
**Source fingerprint (SHA-256):** `1b26630fadbdc144cd42ca7393f743b079ee7463deb9c8b31b628b5dc7432317`
