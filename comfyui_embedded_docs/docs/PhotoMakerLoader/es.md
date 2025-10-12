> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PhotoMakerLoader/es.md)

El nodo PhotoMakerLoader carga un modelo PhotoMaker a partir de los archivos de modelo disponibles. Lee el archivo de modelo especificado y prepara el codificador de ID de PhotoMaker para su uso en tareas de generación de imágenes basadas en identidad. Este nodo está marcado como experimental y está destinado a fines de prueba.

## Entradas

| Parámetro | Tipo de dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `nombre_del_modelo_photomaker` | STRING | Sí | Múltiples opciones disponibles | El nombre del archivo de modelo PhotoMaker a cargar. Las opciones disponibles están determinadas por los archivos de modelo presentes en la carpeta photomaker. |

## Salidas

| Nombre de salida | Tipo de dato | Descripción |
|-------------|-----------|-------------|
| `photomaker_model` | PHOTOMAKER | El modelo PhotoMaker cargado que contiene el codificador de ID, listo para su uso en operaciones de codificación de identidad. |