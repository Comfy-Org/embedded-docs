> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadVideo/es.md)

El nodo Load Video carga archivos de video desde el directorio de entrada y los hace disponibles para su procesamiento en el flujo de trabajo. Lee archivos de video desde la carpeta de entrada designada y los emite como datos de video que pueden conectarse a otros nodos de procesamiento de video.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `archivo` | STRING | Sí | Múltiples opciones disponibles | El archivo de video a cargar desde el directorio de entrada |

**Nota:** Las opciones disponibles para el parámetro `file` se completan dinámicamente a partir de los archivos de video presentes en el directorio de entrada. Solo se muestran archivos de video con tipos de contenido compatibles.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `video` | VIDEO | Los datos de video cargados que pueden pasarse a otros nodos de procesamiento de video |
