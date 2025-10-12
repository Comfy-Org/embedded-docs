> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiInputFiles/es.md)

Carga y formatea archivos de entrada para su uso con la API de Gemini. Este nodo permite a los usuarios incluir archivos de texto (.txt) y PDF (.pdf) como contexto de entrada para el modelo Gemini. Los archivos se convierten al formato apropiado requerido por la API y pueden encadenarse para incluir múltiples archivos en una sola solicitud.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `file` | COMBO | Sí | Múltiples opciones disponibles | Archivos de entrada para incluir como contexto para el modelo. Por ahora solo acepta archivos de texto (.txt) y PDF (.pdf). Los archivos deben ser más pequeños que el límite máximo de tamaño de archivo de entrada. |
| `GEMINI_INPUT_FILES` | GEMINI_INPUT_FILES | No | N/A | Archivo(s) adicional opcional para agrupar junto con el archivo cargado desde este nodo. Permite el encadenamiento de archivos de entrada para que un solo mensaje pueda incluir múltiples archivos de entrada. |

**Nota:** El parámetro `file` solo muestra archivos de texto (.txt) y PDF (.pdf) que son más pequeños que el límite máximo de tamaño de archivo de entrada. Los archivos se filtran y ordenan automáticamente por nombre.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `GEMINI_INPUT_FILES` | GEMINI_INPUT_FILES | Datos de archivo formateados listos para usar con nodos Gemini LLM, que contienen el contenido del archivo cargado en el formato de API apropiado. |
